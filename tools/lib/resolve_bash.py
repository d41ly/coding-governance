"""resolve_bash -- the bash that can SEE a script, found by RUNNING each candidate (TOOL-dGroundRules-25 S28).

The canonical copy of the run-gates kit's rule, `profile_bar.py`'s `resolve_bash`. `<prefix>/lib/` is
gov-internal and ships nothing, so a consumer carries the block below INLINE, byte-identical, and
`<prefix>/lib/resolve-python.test.sh`'s parity table reds a copy that drifts. The policy kit's
`check_policy.py` carries it; the other copies, which return a different shape, are
`TOOL-dSettledRoster-6`'s ask, not this block's.
"""
import os
import shutil
import subprocess


# >>> resolve_bash_py -- canonical copy: resolve_bash.py in the gov lib dir (byte-identical; gated)
def resolve_bash(script):
    r"""The bash that can SEE `script`, by RUNNING each candidate, or None. GOV_BASH first, then the
    bash PATH names, then Git for Windows' two paths, each kept only when `test -f` on the script
    exits 0 under it. On Windows PATH order commonly puts the System32 WSL launcher first, which
    cannot open a `C:/` path, and a stub that exits 127 can sit there too (gotcha
    subprocess-resolves-a-different-shell); being on PATH is not evidence."""
    cands = [os.environ.get("GOV_BASH", ""), shutil.which("bash") or "",
             "C:/Program Files/Git/bin/bash.exe", "C:/Program Files/Git/usr/bin/bash.exe", "bash"]
    tried = []
    for c in cands:
        if not c or c in tried:
            continue
        tried.append(c)
        try:
            r = subprocess.run([c, "-c", 'test -f "$1"', "_", str(script)], capture_output=True, timeout=20)
        except (OSError, subprocess.SubprocessError):
            continue
        if r.returncode == 0:
            return c
    return None
# <<< resolve_bash_py
