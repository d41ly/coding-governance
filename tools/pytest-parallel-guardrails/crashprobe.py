"""crashprobe — attribute otherwise-invisible pytest-xdist worker deaths.

Part of the pytest-parallel-guardrails kit (see README.md). Diagnostic tool: arm it while
hunting a "worker crashed" mystery, read the per-worker logs, then remove it.

Why worker deaths are invisible without this: execnet redirects a worker's fd 0 and fd 1 to
devnull on every platform — and on Windows fd 2 as well — so pytest-timeout's `+++ Timeout +++`
banner (stdout) and any stderr-bound diagnostic are discarded. A pytest-timeout expiry under
`timeout_method = "thread"` then ends the process with `os._exit(1)`, which xdist reports only
as `worker 'gwN' crashed while running '<test>'`. This plugin records, in a per-worker log file
that survives all of that:

  A) a pytest-timeout kill  -> the patched `os._exit` logs the victim test, the caller's stack,
     and every thread's stack BEFORE the process dies;
  B) a native crash (segfault/abort in a C extension) -> `faulthandler` writes the C-level
     traceback of every thread into the same log;
  C) every test's start/end with elapsed wall-clock and RSS, so memory pressure and the
     last-test-before-death are readable even when neither A nor B fired.

A and B cannot be confused: a timeout kill produces the `os._exit` block, a native crash the
faulthandler block.

Loading (verified — a bare `pytest -p crashprobe` with this file only sitting in the rootdir
does NOT import, because the pytest console script does not put the rootdir on sys.path):

    PYTHONPATH=path/to/kit pytest -p crashprobe ...          # env var form
    pytest -p crashprobe ...                                 # with `pythonpath = ["..."]` ini
    python -m pytest -p crashprobe ...                       # cwd form (file in cwd)

Output: one `probe-<workerid>.log` per xdist worker (`probe-master.log` when not distributed)
in `$CRASHPROBE_DIR` (created if needed), else the current working directory. Line-buffered so
a hard kill cannot lose the final lines.

Stdlib only. Works on Windows and POSIX (RSS via ctypes/psapi on Windows, `resource` on POSIX —
each import is guarded so neither platform's absence breaks the other).
"""

import faulthandler
import os
import sys
import time
import traceback

try:
    import pytest

    _hook_trylast = pytest.hookimpl(trylast=True)
except ImportError:  # bare-stdlib import (the kit self-test); hooks never fire without pytest

    def _hook_trylast(fn):
        return fn


KIT_PYTEST_GUARDRAILS_VERSION = "1.0"

_WID = os.environ.get("PYTEST_XDIST_WORKER", "master")
_DIR = os.environ.get("CRASHPROBE_DIR") or os.getcwd()
os.makedirs(_DIR, exist_ok=True)

# Line-buffered: a hard kill (os._exit / native crash) must not lose the last lines.
_LOG = open(os.path.join(_DIR, f"probe-{_WID}.log"), "w", buffering=1, encoding="utf-8")

_T0 = time.time()
_cur = {"test": "<none>", "start": _T0}


def _rss_mb() -> float:
    """Current working set in MB (Windows) or peak RSS in MB (POSIX; ru_maxrss is a PEAK,
    documented as such in the log header). Returns -1.0 when unavailable."""
    if os.name == "nt":
        try:
            import ctypes
            from ctypes import wintypes

            class PMC(ctypes.Structure):
                _fields_ = [
                    ("cb", wintypes.DWORD),
                    ("PageFaultCount", wintypes.DWORD),
                    ("PeakWorkingSetSize", ctypes.c_size_t),
                    ("WorkingSetSize", ctypes.c_size_t),
                    ("QuotaPeakPagedPoolUsage", ctypes.c_size_t),
                    ("QuotaPagedPoolUsage", ctypes.c_size_t),
                    ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t),
                    ("QuotaNonPagedPoolUsage", ctypes.c_size_t),
                    ("PagefileUsage", ctypes.c_size_t),
                    ("PeakPagefileUsage", ctypes.c_size_t),
                ]

            gcp = ctypes.windll.kernel32.GetCurrentProcess
            gcp.restype = wintypes.HANDLE
            gpmi = ctypes.windll.psapi.GetProcessMemoryInfo
            gpmi.argtypes = [wintypes.HANDLE, ctypes.POINTER(PMC), wintypes.DWORD]
            gpmi.restype = wintypes.BOOL

            pmc = PMC()
            pmc.cb = ctypes.sizeof(PMC)
            if not gpmi(gcp(), ctypes.byref(pmc), pmc.cb):
                return -1.0
            return pmc.WorkingSetSize / (1024 * 1024)
        except Exception:
            return -1.0
    try:
        import resource

        rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # Linux reports KiB; macOS reports bytes.
        return rss / 1024 if sys.platform != "darwin" else rss / (1024 * 1024)
    except Exception:
        return -1.0


def _w(msg: str) -> None:
    _LOG.write(f"[{time.time() - _T0:8.1f}s rss={_rss_mb():7.1f}MB] {msg}\n")


_real_exit = os._exit


def _traced_exit(code):
    # The single most important block: who called os._exit, and on which test. pytest-timeout's
    # thread method ends the worker this way; without the patch the death is unattributed.
    try:
        _w(
            f"!!! os._exit({code}) CALLED — victim test: {_cur['test']} "
            f"(running {time.time() - _cur['start']:.1f}s)"
        )
        _LOG.write("--- python stack of the os._exit caller ---\n")
        _LOG.write("".join(traceback.format_stack()))
        _LOG.write("--- all thread stacks ---\n")
        _LOG.flush()
        faulthandler.dump_traceback(file=_LOG, all_threads=True)
        _LOG.flush()
        os.fsync(_LOG.fileno())
    except Exception:
        pass
    _real_exit(code)


os._exit = _traced_exit
_w(
    f"probe armed — pid={os.getpid()} worker={_WID} python={sys.version.split()[0]} "
    f"kit={KIT_PYTEST_GUARDRAILS_VERSION} (POSIX rss column = PEAK ru_maxrss)"
)


@_hook_trylast
def pytest_configure(config):
    """Arm faulthandler AFTER pytest's builtin faulthandler plugin.

    `faulthandler.enable` is process-global last-wins, and pytest's builtin plugin calls
    `enable(file=dup(stderr))` at configure time — an import-time arm here would be silently
    superseded and native-crash tracebacks would go to the (worker-redirected) stderr instead
    of the probe log. `trylast` puts this after the builtin. `faulthandler_timeout` dumps are
    unaffected either way: `dump_traceback_later` takes its own file handle per call.
    """
    faulthandler.enable(file=_LOG, all_threads=True)
    _w("faulthandler re-armed onto the probe log (post-builtin)")


def pytest_runtest_logstart(nodeid, location):
    _cur["test"] = nodeid
    _cur["start"] = time.time()
    _w(f"START {nodeid}")


def pytest_runtest_logfinish(nodeid, location):
    _w(f"END   {nodeid} ({time.time() - _cur['start']:.1f}s)")
    _cur["test"] = f"<between tests, last={nodeid}>"
    _cur["start"] = time.time()


def pytest_sessionfinish(session, exitstatus):
    _w(f"sessionfinish exitstatus={exitstatus}")
    _LOG.flush()
