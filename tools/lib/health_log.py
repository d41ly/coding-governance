"""health_log — the health log's Python appender, canonical copy (TOOL-aGraftedHelix-8, interface I3).

`<prefix>/lib/` is gov-internal and ships nothing, so every Python writer carries the block below
INLINE, byte-identical, and `<prefix>/lib/resolve-python.test.sh`'s parity table reds a copy that
drifts. Its shell twin, with the same contract, is the `health_log_sh` block in `health-log.sh`
beside this file, and the same test's behaviour arm runs both against one scratch log.
"""

# >>> health_log_py — canonical copy: health_log.py in gov's lib dir (byte-identical; gated)
# I3, THE HEALTH LOG (TOOL-aGraftedHelix-8): `<git-common-dir>/health.log`, one LF-terminated UTF-8
# line per automatic self-heal, four TAB-separated fields: utc (`YYYY-MM-DDTHH:MM:SS+00:00`), source
# and event (each `^[a-z][a-z0-9-]*$`), and a detail whose TAB, CR and LF are each folded to one space
# and which is cut to 240 characters. At HEALTH_LOG_CAP_LINES lines the appender first keeps the
# newest half, through a temp file and a rename, then appends. `derive_health_log(common_dir)` returns
# the path and spawns nothing; `resolve_health_log(repo_dir)` asks git once per process and returns
# it, or "" when git cannot answer; `add_health_event(log, source, event, detail)` is the only writer.
# A refused token, an empty path or a failed write prints ONE `health: NOTE -` line on stderr and
# returns None: it never raises into its caller. WHAT IT DOES NOT DO: serialize concurrent writers (a
# trim racing an append can lose that line; ponytail: one rename, a lock file if a lost line is ever
# observed); validate what a detail means; or tell a repository with no writer installed from one
# where nothing healed.
import datetime as _hl_datetime
import os as _hl_os
import re as _hl_re
import subprocess as _hl_subprocess
import sys as _hl_sys

HEALTH_LOG_CAP_LINES = 500
_HL_TOKEN = _hl_re.compile(r"[a-z][a-z0-9-]*\Z")
_HL_CACHE = {}


def derive_health_log(common_dir):
    return "%s/health.log" % common_dir


def resolve_health_log(repo_dir):
    key = str(repo_dir)
    if key not in _HL_CACHE:
        common = ""
        try:
            done = _hl_subprocess.run(
                ["git", "-C", key, "rev-parse", "--path-format=absolute", "--git-common-dir"],
                capture_output=True, timeout=60)
            if done.returncode == 0:
                common = done.stdout.decode("utf-8", "replace").strip()
        except (OSError, _hl_subprocess.SubprocessError):
            common = ""
        _HL_CACHE[key] = derive_health_log(common) if common else ""
    return _HL_CACHE[key]


def add_health_event(log, source, event, detail):
    why = ""
    if not _HL_TOKEN.match(str(source)):
        why = "source %r is not a lowercase token" % (source,)
    if not _HL_TOKEN.match(str(event)):
        why = "event %r is not a lowercase token" % (event,)
    if not log:
        why = "no log path resolved"
    if not why:
        try:
            stamp = _hl_datetime.datetime.now(_hl_datetime.timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%S+00:00")
            text = _hl_re.sub(r"[\t\r\n]", " ", str(detail))[:240]
            line = ("%s\t%s\t%s\t%s\n" % (stamp, source, event, text)).encode("utf-8")
            try:
                with open(log, "rb") as fh:
                    held = fh.readlines()
            except FileNotFoundError:
                held = []
            if len(held) >= HEALTH_LOG_CAP_LINES:
                trim = "%s.trim.%d" % (log, _hl_os.getpid())
                with open(trim, "wb") as fh:
                    fh.writelines(held[-(HEALTH_LOG_CAP_LINES // 2):])
                _hl_os.replace(trim, log)
            with open(log, "ab") as fh:
                fh.write(line)
            return None
        except Exception as exc:  # never into the caller: a completed heal must not become a traceback
            why = "the write failed: %s" % exc
    _hl_sys.stderr.write("health: NOTE - %s: %s; nothing written\n" % (log or "(no path)", why))
    return None
# <<< health_log_py
