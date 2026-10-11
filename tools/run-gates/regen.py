#!/usr/bin/env python3
"""regen.py — regenerate every generated output the kits declare, or prove each one fresh.

    python <prefix>/run-gates/regen.py --list    # the resolved items, in the order --write runs them
    python <prefix>/run-gates/regen.py --check   # run every check; writes nothing
    python <prefix>/run-gates/regen.py --write   # run every write, stage by stage
    bash <prefix>/run-gates/run-gates.sh --regen | --regen-check | --regen-list   # the same three

TOOL-aPrimedIndex-2. A merge bar graded these outputs at the END of a run, so a session learned an
index was stale an hour in, regenerated it, and ran the whole bar again. This verb is the one command
that regenerates them all, and the runner calls `--check` before its first leg (TOOL-aPrimedIndex-3).

WHAT IT READS. Every TRACKED `kit.toml` one directory below the tool root, the population the
unattended kit's `resolve_generated_indexes` reads, with tomllib. The tree is the current directory's
git toplevel; the tool root is where this kit sits below its own repository, applied to that tree. Two tables declare an item:
  - a `[[generated]]` row carrying `write`, `check` (argv arrays) and `stage` (a positive integer),
    all three or none — an index over the records or the code;
  - a `[[regenerate]]` row carrying `stage` — a render from a kit template. Its check is the row's
    own `check` argv, else its kit's `[check]` argv; a staged row with neither is refused.
Rows sharing one write and one check are ONE item. Stage 1 renders from kit templates, stage 2 the
indexes over the records, stage 3 the codebase map, which reads the output of both; `--write` runs
the stages in order and the items of one stage concurrently, because one stage's outputs are disjoint.

EXIT 0 every item fresh, or written · 1 an item stale, failed or timed out · 2 REFUSED: a descriptor
that does not parse, a malformed row, an unresolved token, or no repository above this kit.

WHAT IT DOES NOT CHECK. That a declared write writes what its row names, or that a check grades it:
the descriptor states both and nothing here compares them. A check red for a reason a regeneration
cannot fix reads as stale; its output tail is printed so a reader can tell. A command that outlives
`GATE_REGEN_BOUND` is killed by its own pid only, so a descendant it spawned can outlive it.
"""
import os
import shutil
import subprocess
import sys
import time
import tomllib
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

TOKENS = ("kit", "prefix", "memory_root", "map_root")
TAIL_LINES = 8
DEFAULT_JOBS = 4
DEFAULT_BOUND = 900


class Refusal(Exception):
    """A declaration this verb cannot read as written."""


def derive_repo_root(start):
    """The directory holding `.git` at or above `start`, by walking, never by asking git: inside a git
    hook an inherited GIT_DIR pins git's answer to the current directory (the unattended kit's
    `derive_self_rel` makes the same walk for the same reason)."""
    here = Path(start)
    for d in (here, *here.parents):
        if (d / ".git").exists():
            return d
    raise Refusal(f"no repository at or above {here}, so this kit's place in its tree is unknown")


def read_toplevel():
    """The tree to regenerate: the current directory's git toplevel, the one the runner has already
    moved into. Not this kit's own repository: a suite driving the runner from a scratch repository
    grades that repository, as the runner's legs do."""
    r = subprocess.run(["git", "rev-parse", "--show-toplevel"], stdout=subprocess.PIPE,
                       stderr=subprocess.DEVNULL, encoding="utf-8", errors="replace")
    if r.returncode != 0 or not r.stdout.strip():
        raise Refusal("the current directory is not inside a git repository, so there is no tree to "
                      "regenerate")
    return Path(r.stdout.strip())


def read_conf_value(path, key):
    """`key`'s value in a sourced `KEY=value` conf, read as bash reads the restricted grammar these
    confs document, or None when the file or the key is absent. The last assignment wins."""
    try:
        lines = Path(path).read_text(encoding="utf-8").splitlines()
    except OSError:
        return None
    out = None
    for raw in lines:
        s = raw.strip()
        if s.startswith("export "):
            s = s[len("export "):].lstrip()
        if not s.startswith(key + "="):
            continue
        v = s[len(key) + 1:]
        if v[:1].isspace() or v == "":
            out = ""
        elif v[:1] in {'"', "'"}:
            close = v.find(v[0], 1)
            out = v[1:close] if close >= 0 else v[1:]
        else:
            out = v.split()[0]
    return out


def read_descriptors(root, tool_rel):
    """`(kit dir, parsed descriptor)` for every tracked `kit.toml` one directory below the tool root."""
    pattern = f":(glob){tool_rel + '/' if tool_rel else ''}*/kit.toml"
    r = subprocess.run(["git", "-c", "core.quotepath=off", "ls-files", "-z", "--", pattern], cwd=root,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise Refusal(f"git ls-files could not list the kit descriptors: {r.stderr.strip()}")
    out = []
    for rel in sorted(p for p in r.stdout.split("\0") if p):
        try:
            with open(root / rel, "rb") as fh:
                out.append((str(Path(rel).parent.as_posix()), tomllib.load(fh)))
        except (OSError, tomllib.TOMLDecodeError) as e:
            raise Refusal(f"{rel} does not parse as TOML, so its declarations cannot be read: {e}")
    return out


def resolve_argv(argv, ctx, where):
    """`argv` with the four descriptor tokens resolved, or a Refusal naming `where`."""
    if not isinstance(argv, list) or not argv or not all(isinstance(a, str) and a for a in argv):
        raise Refusal(f"{where}: an argv must be a non-empty list of non-empty strings, got {argv!r}")
    out = []
    for a in argv:
        for t in TOKENS:
            a = a.replace("{" + t + "}", ctx[t])
        if "{" in a or "}" in a:
            raise Refusal(f"{where}: '{a}' carries a token this verb does not resolve "
                          f"(it resolves {', '.join('{' + t + '}' for t in TOKENS)})")
        out.append(a)
    return out


def check_when(root, when, where):
    """True when a row's `when = "<conf>:<KEY>=<value>"` holds at the repo root."""
    conf, _, kv = str(when).partition(":")
    key, eq, want = kv.partition("=")
    if not conf or not key or not eq:
        raise Refusal(f"{where}: a when must read <conf file>:<KEY>=<value>, got {when!r}")
    return read_conf_value(root / conf, key) == want


def check_stage(stage, where):
    """A positive integer, or a Refusal."""
    if isinstance(stage, bool) or not isinstance(stage, int) or stage < 1:
        raise Refusal(f"{where}: stage must be a positive integer, got {stage!r}")
    return stage


def build_items(root, tool_rel, descriptors):
    """Every declared item, joined by its (write, check) pair, sorted into run order."""
    mem = read_conf_value(root / ".memory-tree.conf", "MEMORY_ROOT") or "memory"
    mapr = read_conf_value(root / ".codebase-map.conf", "MAP_ROOT")
    if mapr is None:
        mapr = "memory/map"
    items = {}
    for kit_rel, d in descriptors:
        kit = str(d.get("id") or Path(kit_rel).name)
        ctx = {"kit": kit_rel, "prefix": tool_rel or ".", "memory_root": mem, "map_root": mapr}
        here = f"{kit_rel}/kit.toml"
        for row in d.get("generated") or []:
            keys = [k for k in ("write", "check", "stage") if k in row]
            if not keys:
                continue
            where = f"{here} [[generated]] {row.get('path', '(no path)')}"
            if len(keys) != 3:
                raise Refusal(f"{where}: carries {', '.join(keys)} of write, check and stage, and a row "
                              f"carries all three or none")
            if "when" in row and not check_when(root, row["when"], where):
                continue
            path = resolve_argv([str(row.get("path") or "")], ctx, where)[0] if row.get("path") else ""
            add = (resolve_argv(row["write"], ctx, where), resolve_argv(row["check"], ctx, where),
                   check_stage(row["stage"], where), kit, path, where)
            add_item(items, *add)
        kit_check = (d.get("check") or {}).get("argv")
        for row in d.get("regenerate") or []:
            where = f"{here} [[regenerate]] {' '.join(map(str, row.get('argv') or []))}"
            if "stage" not in row:
                if "check" in row:
                    raise Refusal(f"{where}: carries a check and no stage, so it joins no stage")
                continue
            chk = row.get("check") or kit_check
            if not chk:
                raise Refusal(f"{where}: is staged, carries no check, and its kit's [check] declares no "
                              f"argv, so nothing can prove it fresh")
            outputs = ", ".join(str(w) for w in row.get("writes") or []) or f"the {kit} render"
            add_item(items, resolve_argv(row.get("argv"), ctx, where), resolve_argv(chk, ctx, where),
                     check_stage(row["stage"], where), kit, outputs, where)
    return sorted(items.values(), key=lambda i: (i["stage"], i["kit"], i["outputs"][0]))


def add_item(items, write, check, stage, kit, output, where):
    """Join one row into `items` under its (write, check) pair."""
    key = (tuple(write), tuple(check))
    item = items.setdefault(key, {"write": write, "check": check, "stage": stage, "kit": kit,
                                  "outputs": [], "where": where})
    if item["stage"] != stage:
        raise Refusal(f"{where}: declares stage {stage} for the item {item['where']} declares stage "
                      f"{item['stage']}, and one item runs in one stage")
    if output and output not in item["outputs"]:
        item["outputs"].append(output)
    if not item["outputs"]:
        item["outputs"].append(f"the {kit} outputs")


def render_argv(argv):
    """The argv as a reader would type it."""
    return " ".join(a if a and not any(c.isspace() for c in a) else repr(a) for a in argv)


def run_command(argv, root, bound):
    """`(status, output, seconds)`: status is the exit code, or 'TIMEOUT', or 127 when it cannot start."""
    run = list(argv)
    if run[0] in ("python", "python3"):
        run[0] = sys.executable
    else:
        # ON PATH, FIRST. Windows' process creation searches its system directory BEFORE `PATH`, and on
        # a node with WSL installed `bash` there is WSL's, which cannot read a linked worktree's `.git`
        # file and reported every Git-Bash check "not a git repo" (measured 2026-10-11, node `a`).
        run[0] = shutil.which(run[0]) or run[0]
    env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
    # NO INHERITED PWD. bash keeps an inherited PWD that names its working directory by another
    # spelling, and node `a`'s TEMP is an 8.3 short name git spells long: an adopter comparing the two
    # rendered `../../../../../DAILY-~1/...` paths into a Skill (measured 2026-10-11 in a clone there).
    env.pop("PWD", None)
    t0 = time.monotonic()
    try:
        r = subprocess.run(run, cwd=root, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT, encoding="utf-8", errors="replace", env=env,
                           timeout=bound)
        return r.returncode, r.stdout or "", round(time.monotonic() - t0)
    except subprocess.TimeoutExpired as e:
        out = e.output if isinstance(e.output, str) else (e.output or b"").decode("utf-8", "replace")
        return "TIMEOUT", out, round(time.monotonic() - t0)
    except OSError as e:
        return 127, f"cannot start {run[0]}: {e}", round(time.monotonic() - t0)


def print_tail(out):
    """The last lines of a command's output, indented under its verdict line."""
    for line in [ln for ln in out.splitlines() if ln.strip()][-TAIL_LINES:]:
        print(f"regen:     | {line}")


def print_items(items):
    """`--list`: every item in run order, then a derived count line."""
    for i in items:
        print(f"regen: stage {i['stage']} · {i['kit']} · {', '.join(i['outputs'])}")
        print(f"regen:   write  {render_argv(i['write'])}")
        print(f"regen:   check  {render_argv(i['check'])}")
    stages = sorted({i['stage'] for i in items})
    print(f"regen: {len(items)} declared across {len({i['kit'] for i in items})} kit(s), "
          f"in {len(stages)} stage(s)")


def run_checks(items, root, jobs, bound):
    """`--check`: every check concurrently, one verdict line each in run order; 0 fresh, 1 otherwise."""
    t0 = time.monotonic()
    with ThreadPoolExecutor(max_workers=jobs) as pool:
        results = list(pool.map(lambda i: run_command(i["check"], root, bound), items))
    stale = 0
    for i, (status, out, secs) in zip(items, results):
        head = f"stage {i['stage']} · {i['kit']} · {', '.join(i['outputs'])}"
        if status == 0:
            print(f"regen: fresh · {head} ({secs}s)")
            continue
        stale += 1
        why = "timed out" if status == "TIMEOUT" else f"exit {status}"
        print(f"regen: STALE · {head} · check: {render_argv(i['check'])} ({why}, {secs}s)")
        print_tail(out)
    print(f"regen: {len(items)} declared · {len(items) - stale} fresh · {stale} stale · "
          f"{round(time.monotonic() - t0)}s")
    return 1 if stale else 0


def read_dirty_paths(root):
    """`{path: content hash}` for every path git reports changed or untracked; a deleted path maps to ''."""
    r = subprocess.run(["git", "-c", "core.quotepath=off", "status", "--porcelain", "-z",
                        "--untracked-files=all"], cwd=root, stdout=subprocess.PIPE,
                       stderr=subprocess.DEVNULL, encoding="utf-8", errors="replace",
                       env=dict(os.environ, GIT_OPTIONAL_LOCKS="0"))
    paths, entries = [], r.stdout.split("\0")
    k = 0
    while k < len(entries):
        e = entries[k]
        k += 1
        if len(e) < 4:
            continue
        paths.append(e[3:])
        if e[0] in "RC":
            k += 1
    present = [p for p in paths if (root / p).is_file()]
    hashes = {}
    if present:
        h = subprocess.run(["git", "hash-object", "--stdin-paths"], cwd=root, input="\n".join(present),
                           stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, encoding="utf-8",
                           errors="replace")
        hashes = dict(zip(present, h.stdout.split()))
    return {p: hashes.get(p, "") for p in paths}


def run_writes(items, root, jobs, bound):
    """`--write`: stage by stage, the items of one stage concurrently; stops after a failed stage."""
    t0 = time.monotonic()
    r = subprocess.run(["git", "-c", "core.quotepath=off", "ls-files", "--others", "--exclude-standard",
                        "-z"], cwd=root, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                       encoding="utf-8", errors="replace")
    untracked = [p for p in r.stdout.split("\0") if p]
    if untracked:
        shown = ", ".join(untracked[:5]) + (", …" if len(untracked) > 5 else "")
        print(f"regen: NOTE — {len(untracked)} untracked file(s); a generator that enumerates tracked "
              f"files does not see one until it is added: {shown}")
    moved_all = []
    for stage in sorted({i["stage"] for i in items}):
        group = [i for i in items if i["stage"] == stage]
        before = read_dirty_paths(root)
        with ThreadPoolExecutor(max_workers=jobs) as pool:
            results = list(pool.map(lambda i: run_command(i["write"], root, bound), group))
        after = read_dirty_paths(root)
        moved = sorted(p for p in set(before) | set(after) if before.get(p) != after.get(p))
        moved_all += [p for p in moved if p not in moved_all]
        failed = 0
        for i, (status, out, secs) in zip(group, results):
            if status == 0:
                continue
            failed += 1
            why = "timed out" if status == "TIMEOUT" else f"exit {status}"
            print(f"regen: FAILED · stage {stage} · {i['kit']} · {', '.join(i['outputs'])} · write: "
                  f"{render_argv(i['write'])} ({why}, {secs}s)")
            print_tail(out)
        print(f"regen: stage {stage} · {len(group)} item(s) · {'failed' if failed else 'written'} · "
              f"moved: {', '.join(moved) if moved else 'none'}")
        if failed:
            print(f"regen: stopped after stage {stage} — a later stage reads what this one writes")
            return 1
    print(f"regen: {len(items)} declared · {len(items)} written · {len(moved_all)} file(s) moved · "
          f"{round(time.monotonic() - t0)}s")
    return 0


def read_knob(name, default):
    """A positive integer from the environment, or a Refusal naming the knob."""
    raw = os.environ.get(name, "")
    if raw == "":
        return default
    if not raw.isdigit() or int(raw) < 1:
        raise Refusal(f"{name} must be a positive integer, got {raw!r}")
    return int(raw)


def main(argv):
    modes = ("--list", "--check", "--write")
    if len(argv) != 2 or argv[1] not in modes:
        print(f"usage: {Path(argv[0]).name} {' | '.join(modes)}", file=sys.stderr)
        return 2
    try:
        kit_dir = Path(os.path.abspath(os.path.dirname(__file__)))
        tool_rel = Path(os.path.relpath(kit_dir.parent, derive_repo_root(kit_dir))).as_posix()
        root = read_toplevel()
        tool_rel = "" if tool_rel == "." else tool_rel
        items = build_items(root, tool_rel, read_descriptors(root, tool_rel))
        jobs = read_knob("GATE_REGEN_JOBS", DEFAULT_JOBS)
        bound = read_knob("GATE_REGEN_BOUND", DEFAULT_BOUND)
    except Refusal as e:
        print(f"regen: REFUSED — {e}")
        return 2
    if argv[1] == "--list":
        print_items(items)
        return 0
    if not items:
        print("regen: 0 declared — no kit descriptor carries a staged row, so nothing was checked or written")
        return 0
    if argv[1] == "--check":
        return run_checks(items, root, jobs, bound)
    return run_writes(items, root, jobs, bound)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
