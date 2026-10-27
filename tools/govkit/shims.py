#!/usr/bin/env python3
"""shims.py — forwarders for a moved command, hook path or module import (TOOL-dSafePassage-6).

    python <this kit>/shims.py --write | --check
    python <this kit>/shims.py --fixture --plant <sh|js|py|module> [--mode warn|journal|unset|bogus]
    python <this kit>/shims.py --fixture --plant window --window <0|1|2|4> --releases <n> [--unlanded]
    python <this kit>/shims.py --fixture --plant parity-edit

`shims.toml` beside this file declares one `[[shim]]` row per moved surface. `--write` renders each
open row's forwarder at its `from` path from one template per language, `--check` compares each with
its render and asserts each closed row's file is absent. A forwarder reads the adopter's
`install.on-shim-call` through the policy kit's reader for its language, at the landed revision, in
the repository the call runs in: `warn` (the default, and every failed read) prints one stderr line
and journals the call, `journal` journals it silently; neither ever blocks the forward. The journal is
`git rev-parse --git-path govkit/shim-calls.jsonl`, one JSON object per call, never its arguments.

`check_shim_windows` refuses a row set `closed = true` before `install.deprecation-window` releases
have been cut since the commit that landed it on the default branch, and holds every row while no
release exists: `read_releases` is the stand-in that returns none until dShippedRelease defines its
release tags. `govkit selfcheck` arm 11 runs both checks.

Exit 0 clean · 1 a finding, or a fixture observation that missed its case · 2 cannot run or observe.
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import posixpath
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import tomllib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import govkit  # noqa: E402 — the deployer's own tool-root, token and policy readers, as matrix.py imports it

SHIMS_NAME = "shims.toml"
KINDS = ("command", "hook", "module")
LANGS = {".sh": "sh", ".js": "js", ".py": "py"}
MARKER = "gov:shim"
JOURNAL = "govkit/shim-calls.jsonl"
# A path segment: no quote, space, `$` or backslash can reach a rendered forwarder.
SEGMENT = re.compile(r"[A-Za-z0-9_][A-Za-z0-9._-]*")
NO_RELEASE = "no release has been cut: dShippedRelease defines release tags"
# The location variables a hook exports: the fixture's git reads the scratch repository it names.
GIT_LOCATION_VARS = ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_OBJECT_DIRECTORY",
                     "GIT_ALTERNATE_OBJECT_DIRECTORIES", "GIT_COMMON_DIR", "GIT_NAMESPACE", "GIT_PREFIX")


def read_shim_rows(root) -> list[dict]:
    """-> every `[[shim]]` row of `root`'s `shims.toml`, validated, its `from` and `to` resolved
    through `{prefix}` to repo-relative paths and `policy` set to the policy kit's directory there.
    A malformed row, a duplicate id or an unreadable file is a Refusal: the declaration is the one
    write boundary every forwarder's bytes pass through."""
    root = pathlib.Path(root)
    path = govkit.resolve_tool_path(root, govkit.GOVKIT_DIR.name, SHIMS_NAME)
    try:
        doc = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as exc:
        raise govkit.Refusal(f"shims: cannot read {path.as_posix()}: {exc}") from None
    troot = govkit.derive_tool_root(root)
    rows, seen = [], set()
    for n, raw in enumerate(doc.get("shim") or [], 1):
        where = f"{SHIMS_NAME} row {n}"
        if not isinstance(raw, dict) or set(raw) != {"id", "kind", "from", "to", "closed"}:
            raise govkit.Refusal(f"shims: {where} must hold exactly id, kind, from, to and closed")
        if not isinstance(raw["id"], str) or not all(SEGMENT.fullmatch(s) for s in raw["id"].split("/")):
            raise govkit.Refusal(f"shims: {where} id {raw['id']!r} is not an <entry>/<slug> id")
        if raw["id"] in seen:
            raise govkit.Refusal(f"shims: {where} repeats the id {raw['id']}")
        seen.add(raw["id"])
        if raw["kind"] not in KINDS:
            raise govkit.Refusal(f"shims: {where} kind {raw['kind']!r} is none of {', '.join(KINDS)}")
        if not isinstance(raw["closed"], bool):
            raise govkit.Refusal(f"shims: {where} closed must be true or false")
        row = dict(raw)
        for k in ("from", "to"):
            spelled = raw[k] if isinstance(raw[k], str) else ""
            rel = govkit.resolve_prefix_token(spelled, troot)
            if not rel or not all(SEGMENT.fullmatch(s) for s in rel.split("/")):
                raise govkit.Refusal(f"shims: {where} {k} {raw[k]!r} is not a relative path inside the tree")
            row[k] = rel
        ext = posixpath.splitext(row["from"])[1]
        if ext not in LANGS or posixpath.splitext(row["to"])[1] != ext or row["from"] == row["to"]:
            raise govkit.Refusal(f"shims: {where} from and to must be two .sh, .js or .py paths of one language")
        if raw["kind"] == "module" and ext != ".py":
            raise govkit.Refusal(f"shims: {where} is a module row, so its paths end in .py")
        row["lang"] = LANGS[ext]
        row["policy"] = govkit.resolve_prefix_token("{prefix}/policy", troot)
        rows.append(row)
    return rows


SH_TEMPLATE = r"""#!/usr/bin/env bash
# @MARKER@ — rendered by shims.py from shims.toml; edit the row, never this file.
# @FROM@ moved to @TO@: this forwarder is held until install.deprecation-window closes it.
case "${BASH_SOURCE[0]}" in */*) _shim_here=${BASH_SOURCE[0]%/*} ;; *) _shim_here=. ;; esac
_shim_mode=warn _shim_why=@WHY@
if _shim_out=$(bash "$_shim_here/@POLICY@/policy-shim.sh" get install.on-shim-call </dev/null 2>/dev/null); then
  case "$_shim_out" in
    *'"value": "journal"}') _shim_mode=journal _shim_why="" ;;
    *'"value": "warn"}') _shim_why="" ;;
  esac
fi
[ "$_shim_mode" = journal ] || printf '%s%s\n' @MOVED@ "$_shim_why" >&2
_shim_log=$(git rev-parse --is-inside-work-tree --git-path @JOURNAL@ </dev/null 2>/dev/null) || _shim_log=""
case "$_shim_log" in
  true$'\n'?*)
    _shim_log=${_shim_log#true$'\n'}
    { mkdir -p "${_shim_log%/*}" && printf '%s%s%s%s%s\n' @J1@ "$(date -u +%Y-%m-%dT%H:%M:%SZ)" @J2@ "$_shim_mode" '"}' >>"$_shim_log"; } 2>/dev/null ;;
  *) printf '%s\n' @NOGIT@ >&2 ;;
esac
exec bash "$_shim_here/@TO_REL@" "$@"
"""

JS_TEMPLATE = r"""#!/usr/bin/env node
// @MARKER@ — rendered by shims.py from shims.toml; edit the row, never this file.
// @FROM@ moved to @TO@: this forwarder is held until install.deprecation-window closes it.
"use strict";
const fs = require("fs");
const path = require("path");
const { spawnSync } = require("child_process");
let mode = "warn";
let why = @WHY@;
try {
  const hit = require(path.join(__dirname, @POLICY@, "policy-mirror.js")).readPolicy("install.on-shim-call", { repo: process.cwd() });
  if (hit.value === "journal" || hit.value === "warn") [mode, why] = [hit.value, ""];
} catch (_e) {
  // a read that fails reads warn, and the line says so; it never blocks the forward
}
if (mode !== "journal") process.stderr.write(@MOVED@ + why + "\n");
const g = spawnSync("git", ["rev-parse", "--is-inside-work-tree", "--git-path", @JOURNAL@], { encoding: "utf8", stdio: ["ignore", "pipe", "ignore"], windowsHide: true });
const lines = g.status === 0 ? g.stdout.split(/\r?\n/) : [];
if (lines[0] === "true" && lines[1]) {
  try {
    fs.mkdirSync(path.dirname(lines[1]), { recursive: true });
    const utc = new Date().toISOString().replace(/\.\d+Z$/, "Z");
    fs.appendFileSync(lines[1], JSON.stringify({ utc, shim: @ID@, from: @FROM_Q@, to: @TO_Q@, mode }) + "\n");
  } catch (_e) {
    // a journal that cannot be written never blocks the forward
  }
} else process.stderr.write(@NOGIT@ + "\n");
const r = spawnSync(process.execPath, [path.join(__dirname, @TO_REL@), ...process.argv.slice(2)], { stdio: "inherit" });
process.exit(r.status === null ? 1 : r.status);
"""

PY_PRELUDE = r"""# @MARKER@ — rendered by shims.py from shims.toml; edit the row, never this file.
# @FROM@ moved to @TO@: this forwarder is held until install.deprecation-window closes it.
import json as _shim_json
import os as _shim_os
import subprocess as _shim_sp
import sys as _shim_sys
import time as _shim_time

_SHIM_HERE = _shim_os.path.dirname(_shim_os.path.abspath(__file__))


def _run_shim_prelude():
    # a read that fails reads warn, and the line says so; neither branch blocks the forward
    mode, why = "warn", @WHY@
    try:
        p = _shim_sp.run([_shim_sys.executable, _shim_os.path.join(_SHIM_HERE, @POLICY@, "policy.py"), "get", @KEY@],
                         stdin=_shim_sp.DEVNULL, capture_output=True, text=True)
        if p.returncode == 0 and p.stdout.strip() in ("warn", "journal"):
            mode, why = p.stdout.strip(), ""
    except OSError:
        pass
    if mode != "journal":
        print(@MOVED@ + why, file=_shim_sys.stderr)
    try:
        g = _shim_sp.run(["git", "rev-parse", "--is-inside-work-tree", "--git-path", @JOURNAL@],
                         stdin=_shim_sp.DEVNULL, capture_output=True, text=True)
        lines = g.stdout.splitlines() if g.returncode == 0 else []
    except OSError:
        lines = []
    if lines[:1] == ["true"] and len(lines) > 1:
        line = {"utc": _shim_time.strftime("%Y-%m-%dT%H:%M:%SZ", _shim_time.gmtime()), "shim": @ID@,
                "from": @FROM_Q@, "to": @TO_Q@, "mode": mode}
        try:
            _shim_os.makedirs(_shim_os.path.dirname(lines[1]) or ".", exist_ok=True)
            with open(lines[1], "a", encoding="utf-8", newline="\n") as f:
                f.write(_shim_json.dumps(line) + "\n")
        except OSError:
            pass
    else:
        print(@NOGIT@, file=_shim_sys.stderr)


_run_shim_prelude()
_SHIM_TARGET = _shim_os.path.join(_SHIM_HERE, @TO_REL@)
"""

PY_COMMAND_TAIL = r"""import runpy as _shim_runpy

_shim_sys.argv[0] = _SHIM_TARGET
_shim_sys.path[0] = _shim_os.path.dirname(_SHIM_TARGET)
_shim_runpy.run_path(_SHIM_TARGET, run_name="__main__")
"""

PY_MODULE_TAIL = r"""import importlib.util as _shim_iu

_shim_spec = _shim_iu.spec_from_file_location(__name__, _SHIM_TARGET)
_shim_mod = _shim_iu.module_from_spec(_shim_spec)
_shim_spec.loader.exec_module(_shim_mod)
_shim_sys.modules[__name__] = _shim_mod
"""


def render_shim(row: dict) -> str:
    """The forwarder `row` renders: its language's template with its marker line, its target and the
    policy kit spelled relative to the forwarder's own directory, so it works at any install prefix,
    and every literal quoted for its language."""
    here = posixpath.dirname(row["from"]) or "."
    to_rel = posixpath.relpath(row["to"], here)
    policy_rel = posixpath.relpath(row["policy"], here)
    moved = (f"gov: {row['from']} has moved to {row['to']}; this forwarder is held only until "
             f"its deprecation window closes")
    why = " (the policy could not be read, so this reads warn)"
    nogit = f"gov: shim {row['id']} journaled nothing: the call runs outside a git work tree"
    if row["lang"] == "sh":
        q = shlex.quote
        j1 = '{"utc": "'
        j2 = ('", "shim": ' + json.dumps(row["id"]) + ', "from": ' + json.dumps(row["from"])
              + ', "to": ' + json.dumps(row["to"]) + ', "mode": "')
        subs = {"@WHY@": q(why), "@POLICY@": policy_rel, "@MOVED@": q(moved), "@JOURNAL@": JOURNAL,
                "@J1@": q(j1), "@J2@": q(j2), "@NOGIT@": q(nogit), "@TO_REL@": to_rel}
        text = SH_TEMPLATE
    else:
        q = json.dumps
        subs = {"@WHY@": q(why), "@POLICY@": q(policy_rel), "@MOVED@": q(moved), "@JOURNAL@": q(JOURNAL),
                "@NOGIT@": q(nogit), "@TO_REL@": q(to_rel), "@ID@": q(row["id"]),
                "@FROM_Q@": q(row["from"]), "@TO_Q@": q(row["to"]), "@KEY@": q("install.on-shim-call")}
        if row["lang"] == "js":
            text = JS_TEMPLATE
        else:
            text = PY_PRELUDE + (PY_MODULE_TAIL if row["kind"] == "module" else PY_COMMAND_TAIL)
    subs |= {"@MARKER@": f"{MARKER} {row['id']}", "@FROM@": row["from"], "@TO@": row["to"]}
    for k, v in subs.items():
        text = text.replace(k, v)
    return text


def write_shims(root) -> list[str]:
    """Render every open row's forwarder at its `from` path, LF, and return the paths written."""
    root = pathlib.Path(root)
    wrote = []
    for row in read_shim_rows(root):
        if row["closed"]:
            continue
        dest = root / row["from"]
        text = render_shim(row)
        if not dest.is_file() or dest.read_bytes() != text.encode("utf-8"):
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(text.encode("utf-8"))
            wrote.append(row["from"])
    return wrote


def check_shim_parity(root) -> tuple[int, list[str]]:
    """-> (rows graded, findings): an open row whose forwarder is absent or differs from its render,
    and a closed row whose file is still present."""
    root = pathlib.Path(root)
    rows = read_shim_rows(root)
    findings = []
    for row in rows:
        dest = root / row["from"]
        if row["closed"]:
            if dest.exists():
                findings.append(f"shims: {row['id']} is closed and {row['from']} is still present")
        elif not dest.is_file():
            findings.append(f"shims: {row['id']} has no forwarder at {row['from']}; run shims.py --write")
        elif dest.read_bytes() != render_shim(row).encode("utf-8"):
            findings.append(f"shims: {row['id']}'s forwarder {row['from']} differs from its render; "
                            f"a forwarder is never edited by hand, run shims.py --write")
    return len(rows), findings


def read_releases(root) -> list[str]:
    """The release commits cut in `root`, oldest first. The stand-in: no release tag is defined until
    dShippedRelease defines one, so it reads no tag and returns none (NO_RELEASE says why)."""
    return []


def run_git(root, *args: str) -> subprocess.CompletedProcess:
    env = {k: v for k, v in os.environ.items() if k not in GIT_LOCATION_VARS}
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True,
                          encoding="utf-8", errors="replace", stdin=subprocess.DEVNULL, env=env)


def resolve_shim_landing(root, shim_id: str) -> str:
    """The oldest commit on the default branch's first-parent history whose `shims.toml` carries the
    row `shim_id`, or "" when no landed commit does. The default branch is the remote ladder's,
    the remote's ref first and the local branch after it, `main` where the ladder names none."""
    remote, branch, _observed, refusal = govkit.resolve_remote(root)
    if refusal:
        return ""
    branch = branch or "main"
    tr = govkit.derive_tool_root(root)
    rel = "/".join([*([tr] if tr else []), govkit.GOVKIT_DIR.name, SHIMS_NAME])
    for ref in ([f"refs/remotes/{remote}/{branch}"] if remote else []) + [f"refs/heads/{branch}"]:
        if run_git(root, "rev-parse", "--verify", "-q", f"{ref}^{{commit}}").returncode != 0:
            continue
        p = run_git(root, "log", "--first-parent", "--reverse", "--format=%H", f"-S{json.dumps(shim_id)}",
                    ref, "--", rel)
        return (p.stdout.split() or [""])[0] if p.returncode == 0 else ""
    return ""


def derive_shim_window(landing: str, releases: list[str], window: int, root) -> tuple[bool, int]:
    """-> (may close, releases since): a row landed at `landing` may close when at least one release
    has been cut and at least `window` of `releases` descend from `landing`, a release at the landing
    commit included. A row on no landed commit is held. `root` is the repository git asks."""
    since = sum(run_git(root, "merge-base", "--is-ancestor", landing, r).returncode == 0
                for r in releases) if landing else 0
    return bool(landing and releases) and since >= window, since


def check_shim_windows(root, releases=None) -> list[str]:
    """One refusal line per `closed = true` row its window does not yet allow. A refused read of
    `install.deprecation-window`, or no policy kit, holds every closed row."""
    rows = [r for r in read_shim_rows(root) if r["closed"]]
    if not rows:
        return []
    why = ""
    if releases is None:
        releases, why = read_releases(root), NO_RELEASE
    try:
        window = int(govkit.read_policy_value("install.deprecation-window", root)[0])
    except (LookupError, govkit.Refusal, ValueError, TypeError) as exc:
        return [f"shims: {r['id']} is closed and held: install.deprecation-window could not be read: {exc}"
                for r in rows]
    out = []
    for r in rows:
        landing = resolve_shim_landing(root, r["id"])
        allowed, since = derive_shim_window(landing, releases, window, root)
        if allowed:
            continue
        out.append(f"shims: {r['id']} is closed and held: landed at {landing[:8] or 'no default-branch commit'}, "
                   f"{since} release(s) cut since of {len(releases)}, window {window}"
                   + (f" ({why})" if why and not releases else ""))
    return out


# ------------------------------------------------------------------------------------- the fixture
TARGETS = {
    "sh": 'printf "args:"; for a in "$@"; do printf " [%s]" "$a"; done; printf "\\n"\n'
          'printf "stdin: [%s]\\n" "$(cat)"\nexit 3\n',
    "js": 'const input = require("fs").readFileSync(0, "utf8");\n'
          'console.log("args:" + process.argv.slice(2).map((a) => ` [${a}]`).join(""));\n'
          'console.log(`stdin: [${input}]`);\nprocess.exit(3);\n',
    "py": 'import sys\nprint("args:" + "".join(f" [{a}]" for a in sys.argv[1:]))\n'
          'print(f"stdin: [{sys.stdin.read()}]")\nsys.exit(3)\n',
    "module": 'import sys\nNAME = "newmod"\n\n\ndef main(argv):\n'
              '    print("args:" + "".join(f" [{a}]" for a in argv))\n'
              '    print(f"stdin: [{sys.stdin.read()}]")\n    return 3\n',
}
CALLER = ('import os\nimport sys\n\nimport oldmod\n\n'
          'print("names: " + oldmod.NAME + " " + os.path.basename(oldmod.__file__))\n'
          'sys.exit(oldmod.main(sys.argv[1:]))\n')


def build_scratch(t: pathlib.Path) -> None:
    run_git(t, "init", "-q", "-b", "main")
    run_git(t, "config", "user.email", "shims@fixture.invalid")
    run_git(t, "config", "user.name", "shims fixture")
    run_git(t, "config", "core.autocrlf", "false")
    (t / "tools" / "govkit").mkdir(parents=True)
    (t / "tools" / "govkit" / govkit.REGISTRY_NAME).write_text("", encoding="utf-8")


def run_commit(t: pathlib.Path, msg: str) -> str:
    run_git(t, "add", "-A")
    run_git(t, "-c", "core.hooksPath=/dev/null", "commit", "-qm", msg)
    return run_git(t, "rev-parse", "HEAD").stdout.strip()


def write_policy(t: pathlib.Path, body: str) -> None:
    (t / ".governance").mkdir(exist_ok=True)
    (t / ".governance" / "policy.toml").write_text(body, encoding="utf-8", newline="\n")


def run_forward_plant(t: pathlib.Path, lang: str, mode: str) -> int:
    ext = ".py" if lang == "module" else f".{lang}"
    stem_old, stem_new = ("oldmod", "newmod") if lang == "module" else ("old", "new")
    row = {"id": f"fixture/moved-{lang}", "kind": "module" if lang == "module" else "command",
           "from": f"tools/demo/{stem_old}{ext}", "to": f"tools/moved/{stem_new}{ext}", "closed": False,
           "lang": "py" if lang == "module" else lang, "policy": "tools/policy"}
    kit = pathlib.Path(govkit.resolve_kit_dir("policy", "policy.py", govkit.GOVKIT_DIR))
    shutil.copytree(kit, t / "tools" / "policy",
                    ignore=shutil.ignore_patterns("__pycache__", "*.test.sh", "legacy-homes.txt"))
    for rel, text in ((row["to"], TARGETS[lang]), (row["from"], render_shim(row))):
        (t / rel).parent.mkdir(parents=True, exist_ok=True)
        (t / rel).write_bytes(text.encode("utf-8"))
    if lang == "module":
        (t / "tools" / "demo" / "caller.py").write_bytes(CALLER.encode("utf-8"))
    if mode != "unset":
        write_policy(t, f'[install]\non-shim-call = "{mode}"\n')
    run_commit(t, f"a moved surface, mode {mode}")
    mirror = subprocess.run([sys.executable, str(t / "tools" / "policy" / "policy.py"), "mirror", "--write"],
                            cwd=t, capture_output=True, text=True, stdin=subprocess.DEVNULL)
    if mirror.returncode == 0:
        run_commit(t, "the policy mirror")
    rendered = render_shim(row).splitlines()
    to_spelled = posixpath.relpath(row["to"], posixpath.dirname(row["from"]))
    first = {"sh": "#!/usr/bin/env bash", "js": "#!/usr/bin/env node"}.get(
        row["lang"], f"# {MARKER} {row['id']} — rendered by shims.py from shims.toml; edit the row, never this file.")
    marker = next((ln.split(MARKER, 1)[1].split()[0] for ln in rendered if MARKER in ln), "none")
    body = render_shim(row)
    obs = [("first line", rendered[0], first), ("marker", f"{MARKER} {marker}", f"{MARKER} {row['id']}"),
           ("target", to_spelled, "../moved/" + posixpath.basename(row["to"])),
           ("target spelled relative to the forwarder", str(to_spelled in body and not posixpath.isabs(to_spelled)
                                                          and "{prefix}" not in body and t.as_posix() not in body), "True")]
    if lang == "sh":
        argv = [govkit.resolve_bash(), row["from"]]
    elif lang == "js":
        node = shutil.which("node")
        if not node:
            print("shims fixture: cannot observe: node not found on PATH")
            return 2
        argv = [node, row["from"]]
    else:
        argv = [sys.executable, "tools/demo/caller.py" if lang == "module" else row["from"]]
    env = {k: v for k, v in os.environ.items() if k not in GIT_LOCATION_VARS}
    p = subprocess.run([*argv, "a", "b c"], cwd=t, input="in", capture_output=True, text=True,
                       encoding="utf-8", errors="replace", env=env)
    out = p.stdout.splitlines()
    err = [ln for ln in p.stderr.splitlines() if ln.strip()]
    jpath = t / run_git(t, "rev-parse", "--git-path", JOURNAL).stdout.strip()
    jlines = jpath.read_text(encoding="utf-8").splitlines() if jpath.is_file() else []
    expect_err = "none" if mode == "journal" else (
        f"gov: {row['from']} has moved to {row['to']}; this forwarder is held only until its deprecation "
        f"window closes" + (" (the policy could not be read, so this reads warn)" if mode == "bogus" else ""))
    obs += [("exit", str(p.returncode), "3"),
            ("args", next((ln for ln in out if ln.startswith("args:")), "none"), "args: [a] [b c]"),
            ("stdin", next((ln for ln in out if ln.startswith("stdin:")), "none"), "stdin: [in]"),
            ("stderr", " | ".join(err) or "none", expect_err),
            ("journal", f"{len(jlines)} line(s)", "1 line(s)")]
    if lang == "module":
        obs.append(("names", next((ln for ln in out if ln.startswith("names:")), "none"), "names: newmod newmod.py"))
    try:
        entry = json.loads(jlines[0]) if jlines else {}
    except ValueError:
        entry = {}
    want_mode = "journal" if mode == "journal" else "warn"
    obs.append(("journal line", " ".join(f"{k}={entry[k]}" for k in sorted(entry) if k != "utc") or "none",
                f"from={row['from']} mode={want_mode} shim={row['id']} to={row['to']}"))
    obs.append(("journal keys", ",".join(entry) or "none", "utc,shim,from,to,mode"))
    obs.append(("journal carries no argument", str(bool(jlines) and "b c" not in jlines[0] and '"a"' not in jlines[0]), "True"))
    return print_observations(f"plant {lang} · mode {mode}", obs)


def print_observations(case: str, obs: list[tuple[str, str, str]]) -> int:
    print(f"shims fixture: {case}")
    bad = 0
    for name, seen, want in obs:
        ok = seen == want
        bad += not ok
        print(f"  {name}: {seen} · expects {want} · {'ok' if ok else 'MISS'}")
    print(f"shims fixture: {len(obs) - bad} of {len(obs)} observation(s) matched")
    return 1 if bad else 0


def run_window_plant(t: pathlib.Path, window: int, n: int, unlanded: bool) -> int:
    write_policy(t, f"[install]\ndeprecation-window = {window}\n")
    run_commit(t, f"window {window}")
    decl = t / "tools" / "govkit" / SHIMS_NAME
    row = ('[[shim]]\nid = "fixture/moved"\nkind = "command"\nfrom = "{prefix}/demo/old.sh"\n'
           'to = "{prefix}/demo/new.sh"\nclosed = false\n')
    decl.write_text("" if unlanded else row, encoding="utf-8", newline="\n")
    run_commit(t, "the row lands")
    releases = []
    for i in range(n):
        (t / "release.txt").write_text(f"{i}\n", encoding="utf-8")
        releases.append(run_commit(t, f"release {i + 1}"))
    decl.write_text(row.replace("closed = false", "closed = true"), encoding="utf-8", newline="\n")
    found = check_shim_windows(t, releases)
    print(f"shims fixture: plant window · window {window} · {n} release(s){' · unlanded' if unlanded else ''}")
    for line in found:
        print(f"  {line}")
    print(f"shims fixture: the closed row is {'held' if found else 'allowed to close'}")
    return 1 if found else 0


def run_parity_plant(t: pathlib.Path) -> int:
    (t / "tools" / "govkit" / SHIMS_NAME).write_text(
        '[[shim]]\nid = "fixture/moved"\nkind = "command"\nfrom = "{prefix}/demo/old.sh"\n'
        'to = "{prefix}/demo/new.sh"\nclosed = false\n', encoding="utf-8", newline="\n")
    write_shims(t)
    before = check_shim_parity(t)[1]
    with open(t / "tools" / "demo" / "old.sh", "a", encoding="utf-8", newline="\n") as f:
        f.write("echo edited by hand\n")
    after = check_shim_parity(t)[1]
    return print_observations("plant parity-edit", [
        ("--check exit on the render", str(int(bool(before))), "0"),
        ("--check exit on a forwarder edited by hand", str(int(bool(after))), "1"),
        ("its finding", (after or ["none"])[0].split(";")[0], "shims: fixture/moved's forwarder tools/demo/old.sh differs from its render")])


def run_fixture(plant: str, mode: str, window: int, releases: int, unlanded: bool) -> int:
    t = pathlib.Path(tempfile.mkdtemp(prefix="shim-"))
    try:
        build_scratch(t)
        if plant == "window":
            return run_window_plant(t, window, releases, unlanded)
        if plant == "parity-edit":
            return run_parity_plant(t)
        return run_forward_plant(t, plant, mode)
    except (govkit.Refusal, LookupError, OSError) as exc:
        print(f"shims fixture: cannot observe: {exc}")
        return 2
    finally:
        shutil.rmtree(t, ignore_errors=True)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog="shims.py")
    verb = ap.add_mutually_exclusive_group(required=True)
    verb.add_argument("--write", action="store_true")
    verb.add_argument("--check", action="store_true")
    verb.add_argument("--fixture", action="store_true")
    ap.add_argument("--plant", choices=("sh", "js", "py", "module", "window", "parity-edit"))
    ap.add_argument("--mode", choices=("warn", "journal", "unset", "bogus"), default="warn")
    ap.add_argument("--window", type=int, choices=(0, 1, 2, 4), default=2)
    ap.add_argument("--releases", type=int, default=0)
    ap.add_argument("--unlanded", action="store_true")
    args = ap.parse_args(argv)
    if args.fixture:
        if not args.plant:
            ap.error("--fixture needs --plant")
        return run_fixture(args.plant, args.mode, args.window, args.releases, args.unlanded)
    root = govkit.repo_root()
    try:
        if args.write:
            for rel in write_shims(root):
                print(f"shims: wrote {rel}")
        n, findings = check_shim_parity(root)
    except govkit.Refusal as exc:
        print(exc)
        return 2
    for f in findings:
        print(f)
    print(f"shims: {n} row(s) graded · {len(findings)} finding(s)")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", newline="\n")
    raise SystemExit(main(sys.argv[1:]))
