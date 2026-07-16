# gov:kit pytest-parallel-guardrails@1.0
"""aiosqlite closed-loop seam patch — copy this block into your tests/conftest.py (module level).

THE CLASS THIS KILLS: a suite pairing per-test event loops (pytest-asyncio function scope) with
DB work that can still be in flight when a test's loop closes. aiosqlite's worker thread then
posts the result with `future.get_loop().call_soon_threadsafe(...)` on the CLOSED loop ->
RuntimeError -> upstream's `except BaseException` branch posts AGAIN (same closed loop) -> the
second raise escapes `_connection_worker_thread` -> THE WORKER THREAD DIES while the connection
object lives on. Every later op on that connection — including `Connection.close()` — awaits a
future nobody resolves: a 0-CPU infinite hang that wedges a whole `-n auto` run.

Loop-side fixes CANNOT close this: pytest-asyncio >=1.1 already cancels pending tasks at
loop-scope end, but the aiosqlite worker is not a task and may post AFTER `loop.close()` no
matter how perfectly teardown drained. The only complete fix is at the seam: when the
destination loop is closed the result is undeliverable EITHER WAY (its awaiter can never be
woken), so drop the delivery and KEEP THE WORKER ALIVE. Healthy paths are byte-identical.

Verified against aiosqlite 0.22.x (protocol: `(future | None, function)` queue tuples +
`_STOP_RUNNING_SENTINEL`); unfixed upstream as of 0.22.1 (omnilib/aiosqlite — #241/PR#305 fixed
only close() ordering). Pair this with the kit's forced-race regression gate
(`aiosqlite_worker_resilience.test-template.py`, renamed to `test_*.py` in your suite) so a
future aiosqlite bump re-proves the behavior in YOUR environment.
"""

import warnings

import aiosqlite
import aiosqlite.core as _aiosqlite_core

_TESTED_AIOSQLITE = "0.22."
if not aiosqlite.__version__.startswith(_TESTED_AIOSQLITE):
    # Warn, never fail: your forced-race gate is the real check on a new release.
    warnings.warn(
        f"aiosqlite {aiosqlite.__version__} is outside the seam patch's tested range "
        f"({_TESTED_AIOSQLITE}x); re-run the worker-resilience gate before trusting it.",
        RuntimeWarning,
        stacklevel=2,
    )


def _resilient_connection_worker_thread(tx) -> None:
    """aiosqlite's `_connection_worker_thread`, with closed-loop posts made non-fatal."""
    while True:
        future, function = tx.get()
        try:
            result = function()
            if future is not None:
                try:
                    future.get_loop().call_soon_threadsafe(
                        _aiosqlite_core.set_result, future, result
                    )
                except RuntimeError:
                    # Destination loop already closed (a per-test loop torn down with this op
                    # in flight). Undeliverable either way — stay alive.
                    pass
            if result is _aiosqlite_core._STOP_RUNNING_SENTINEL:
                break
        except BaseException as e:  # noqa: B036 — mirrors upstream
            if future is not None:
                try:
                    future.get_loop().call_soon_threadsafe(
                        _aiosqlite_core.set_exception, future, e
                    )
                except RuntimeError:
                    pass


# Connection.__init__ resolves the module global at call time, so patching the module attribute
# covers every connection the suite will ever create. Must run before any engine/connection is
# created — conftest module level guarantees that.
_aiosqlite_core._connection_worker_thread = _resilient_connection_worker_thread
