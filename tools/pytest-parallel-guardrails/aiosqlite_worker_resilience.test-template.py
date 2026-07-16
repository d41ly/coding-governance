# gov:kit pytest-parallel-guardrails@1.0
"""Forced-race regression gate for the aiosqlite closed-loop seam patch.

COPY into your test suite AND RENAME to `test_aiosqlite_worker_resilience.py` (this file is
deliberately named off pytest's `test_*.py` glob so a crawl over the vendored kit dir cannot
collect it). Then fix the ONE marked import below to wherever your conftest defines the patched
worker function.

What it proves, deterministically (no timing lottery): an op EXECUTING on the aiosqlite worker
thread while its awaiting event loop closes — the exact race behind the wedged-suite class. On
unpatched aiosqlite 0.22.x this kills the worker and the next op on the connection hangs
forever; with the seam patch the worker survives, the connection stays usable from a new loop,
and `close()` completes. Also pins that the patch is actually installed, so a conftest refactor
cannot silently drop it.
"""

import asyncio
import threading
import time

import aiosqlite
import aiosqlite.core as aiosqlite_core

# ONE ADOPTER EDIT: import the patched worker from YOUR conftest module.
from tests.conftest import _resilient_connection_worker_thread


def test_patch_is_installed() -> None:
    """The seam patch must be live for every connection the suite creates."""
    assert aiosqlite_core._connection_worker_thread is _resilient_connection_worker_thread


def test_worker_survives_post_to_closed_loop_and_connection_stays_usable(tmp_path) -> None:
    release = threading.Event()

    # -- loop 1: open a connection and leave an op IN FLIGHT while we close the loop
    loop = asyncio.new_event_loop()
    conn = loop.run_until_complete(aiosqlite.connect(tmp_path / "resilience.db"))
    worker = conn._thread
    assert worker.is_alive()

    victim_future = loop.create_future()

    def blocked_op():
        # Holds the worker inside function() until the test has closed the loop,
        # guaranteeing the result post targets a CLOSED loop.
        release.wait(timeout=10)
        return 42

    conn._tx.put_nowait((victim_future, blocked_op))
    # let the worker dequeue and enter blocked_op (either order still exercises the seam)
    time.sleep(0.2)
    loop.close()  # the awaiting loop dies with the op in flight
    release.set()  # worker finishes -> posts to the closed loop -> the seam

    # Unpatched, the worker dies within milliseconds of the post; give it a beat, then a fast
    # death shows up here with a precise message. (A merely-slow worker passes — the roundtrip
    # below is the authoritative, event-based survival proof.)
    worker.join(timeout=1.5)
    assert worker.is_alive(), (
        "aiosqlite worker thread died posting to a closed event loop — the seam patch "
        "(gov:kit pytest-parallel-guardrails) is not effective"
    )

    # -- loop 2: the SAME connection must still serve ops and close cleanly. Deterministic: a
    # dead worker can never resolve these futures, so the failure mode is the wait_for timeout,
    # not a timing-sensitive assert.
    loop2 = asyncio.new_event_loop()
    try:

        async def roundtrip() -> int:
            cursor = await conn.execute("SELECT 1")
            row = await cursor.fetchone()
            await cursor.close()
            return row[0]

        assert loop2.run_until_complete(asyncio.wait_for(roundtrip(), timeout=30)) == 1
        # close() queues an op too — on a dead worker THIS is what used to hang forever
        loop2.run_until_complete(asyncio.wait_for(conn.close(), timeout=30))
        # the worker breaks AFTER posting the sentinel result — join, don't race it
        worker.join(timeout=10)
        assert not worker.is_alive()  # clean shutdown via the stop sentinel
    finally:
        loop2.close()
