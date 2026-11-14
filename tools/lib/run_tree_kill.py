"""run_tree_kill -- kill a timed-out child and what it started, then reap it (TOOL-dDeclaredLoop-42 S4).

The canonical copy of the run-gates kit's tree kill, `regen.py`'s `run_tree_kill`. `<prefix>/lib/` is
gov-internal and ships nothing, so a consumer carries the block below INLINE, byte-identical, and
`<prefix>/lib/resolve-python.test.sh`'s parity table reds a copy that drifts. Two carry it: the
run-gates kit's `regen.py` and the loop kit's `loop_witness.py`. On Windows `taskkill /T` may miss an
MSYS descendant, so a caller bounds itself by sending output to a file, never by this kill alone.
"""
import os
import signal
import subprocess


# >>> run_tree_kill_py -- canonical copy: run_tree_kill.py in the gov lib dir (byte-identical; gated)
def run_tree_kill(proc):
    """Kill a timed-out child and what it started, then reap it: `taskkill /T` on Windows, the child's
    own process group on POSIX. Each step is best-effort, because the child may already be gone."""
    try:
        if os.name == "nt":
            subprocess.run(["taskkill", "/F", "/T", "/PID", str(proc.pid)], stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, timeout=30)
        else:
            os.killpg(proc.pid, signal.SIGKILL)
    except (OSError, subprocess.SubprocessError):
        pass
    try:
        proc.kill()
    except OSError:
        pass
    try:
        proc.wait(timeout=10)
    except subprocess.TimeoutExpired:
        pass
# <<< run_tree_kill_py
