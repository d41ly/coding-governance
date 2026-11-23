"""memory_measure.py — the acceptance re-measure: memory bytes per memory-reading agent over every read
channel (TOOL-dTotalRecall-12). gov:kit runlog@1.18

    python <this kit>/runlog.py memory [--from <utc>] [--to <utc>] [--transcripts <projects dir>]
    python <this kit>/runlog.py memory --landed <rev> [--transcripts <projects dir>]
    python <this kit>/runlog.py memory --fixture --plant <case>

WHAT IT COUNTS. A measure counting Read calls alone passes by construction once memory reads move into
work orders and `record show`, so every read channel is counted (`READ_CHANNELS`): `read`, the result
bytes of a tool `extract.py#TOOL_CLASSES` classes `read` whose `file_path`, `notebook_path` or `path`
input names a memory path; `shell`, the result bytes of a `extract.py#SHELL_TOOLS` call whose command
names a memory path in any word or runs a read verb (`READ_VERBS`), split by `extract.py#extract_segments`;
and `slice`, the bytes of a work order's inlined slices, read by `read_slice_bytes`, a STAND-IN that
returns None until the build writing the slice manifest gives it a body. A None reads as the channel
`unarmed`, never as zero bytes.

A MEMORY PATH is a word of THIS clone's memory tree (TOOL-dTotalRecall-43 S16, S17), the root
`runlog_lib.py#resolve_memory_root` returns. The word and the main worktree are folded by the kit's one
fold, `model.py#derive_path_key` (TOOL-dTotalRecall-53 S24 S33): every `\\` to `/`, an MSYS `/<letter>/`
to `<letter>:/`, a drive letter lower-cased, and on Windows the whole path. A relative word is resolved
against the working directory the call's transcript record carries, so `./memory/x` and
`../../memory/x` read as the paths they name; with none recorded, `.` segments fold away and a word
climbing out with `..` counts nowhere. An absolute word counts only when it starts with the main
worktree, or a `.claude/worktrees/<name>` worktree of it, then `/<root>/`, so the harness's auto-memory
directory and another repository's `memory/` never count; an unresolved relative word counts when it
starts `<root>/` or is `<root>` alone, so a kit directory whose name merely begins with the root's name
never matches. A PowerShell command is folded before it is split, because `\\` is no escape character there.

THE POPULATION. Every subagent transcript, direct and workflow, under the project directories the
harness names for this clone: its main worktree, the parent of the git common dir, each character
outside `[A-Za-z0-9-]` folded to `-`, and that name followed by `--claude-worktrees-`. An agent's start
is its first timestamped record; its type the `agentType` of its `agent-<id>.meta.json` kept through
`extract.py#_derive_label`, else `unknown`; it reads memory when its total over the channels is above
zero.

THE VERDICT, under `--landed`: the thirty days from that commit's committer time are the window, and
the median, `sorted(v)[min(len(v) - 1, int(len(v) * 0.5))]` over the agents reading memory, is graded
against `TARGET_BYTES`. `pass` (0) only when the window has closed, the slice channel is armed and the
median is below the target; `fail` (1) when the first two hold and it is not; otherwise `not-due`,
`unarmed` or `empty`, in that order, each exit 3. The slice channel is armed when at least one agent was
measured and no measured agent's slice read None.

WHAT IT KEEPS. Counts only: no path, command or result text is printed or written, and an agent type
prints only as `_derive_label` keeps it. It writes no file; `--fixture` writes its planted transcripts
under a scratch directory of the system temp dir and removes it.

WHAT IT DOES NOT CHECK. The shell channel is an upper bound: a command naming a memory path may print
more than memory. A command nested in `bash -c`, `eval` or `$(...)` is not descended into, as
`extract_segments` states. The harness's project-directory encoding is observed, not documented; a
changed encoding reads as `empty`, never `pass`. An agent whose transcript was last written before the
window opens is not read. The byte counter is `extract.py#read_result_bytes`, shared with
replay_scorer's `measure_bytes_before_act` (TOOL-dTotalRecall-43 S53).
"""
import datetime
import json
import os
import pathlib
import posixpath
import re
import shutil
import subprocess
import sys
import tempfile
import uuid

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import extract as ex  # noqa: E402
import model as mdl  # noqa: E402  the kit's one path fold
import runlog_lib as rl  # noqa: E402

READ_CHANNELS = ("slice", "read", "shell")
# `record find`'s CLI adapter, a kit-relative tail matched on a program word's end. Held as its two
# segments because it names a sibling kit's file, which a shipped file never spells as one path.
RECALL_ADAPTER = ("memory-recall", "query.py")
# `None` as the verb means any verb. An entry carrying `/` matches the folded program word's tail.
READ_VERBS = frozenset({("record", "show"), ("record", "find"), ("gov", "tag"),
                        ("gov_record.py", "show"), ("gov_record.py", "find"), ("gov_tag.py", None),
                        ("/".join(RECALL_ADAPTER), None)})
PATH_INPUTS = ("file_path", "notebook_path", "path")
TARGET_BYTES = 33000  # 33 KB, a KB of 1,000 bytes: the systems record's target, an owner ruling to move
WINDOW_DAYS = 30
DAY_SECONDS = 86400
VERDICT_EXITS = {"pass": 0, "fail": 1, "not-due": 3, "unarmed": 3, "empty": 3}
PROJECT_NAME_RE = re.compile(r"[^A-Za-z0-9-]")
WORKTREE_INFIX = "--claude-worktrees-"
# The folder a linked worktree of this clone sits in under its main worktree, the harness's own layout.
WORKTREES_DIR = ".claude/worktrees"
DRIVE_RE = re.compile(r"^[A-Za-z]:(?:/|$)")
# The harness's folder for a Workflow run's agent transcripts under a session's `subagents/`: a transcript
# layout name, not a kit, so the fixture names it once here.
HARNESS_RUN_DIR = "workflows"
POOLED = "all, pooled"
UNKNOWN_TYPE = "unknown"


# ---------------------------------------------------------------------------------- one tool call

def check_absolute_path(folded) -> bool:
    """Whether a folded path word is absolute: a `/` root or a drive."""
    return folded.startswith("/") or bool(DRIVE_RE.match(folded))


def check_memory_word(word, memory_root, main_worktree=None, cwd=None) -> bool:
    """Whether one word names a memory path of THIS clone (TOOL-dTotalRecall-43 S16, S17), the word, the
    root, `cwd` and the main worktree each folded by `model.derive_path_key`, the kit's one fold
    (TOOL-dTotalRecall-53 S24 S33). A relative word is resolved against `cwd`, the command's working
    directory, where it is an absolute path; else its `.` segments fold away and it counts when it starts
    with `<root>/` or is `<root>` alone, a word climbing out with `..` counting nowhere. An absolute word
    counts only when it starts with the main worktree, or a `.claude/worktrees/<name>` worktree of it, then
    `/<root>/`; so the harness's own auto-memory directory and another repository's `memory/` never count,
    and with no main worktree known no absolute word does."""
    if not isinstance(word, str) or not word:
        return False
    root = mdl.derive_path_key(memory_root)
    folded = mdl.derive_path_key(word)
    if not check_absolute_path(folded):
        base = mdl.derive_path_key(cwd) if isinstance(cwd, str) else ""
        if not check_absolute_path(base):
            folded = posixpath.normpath(folded) if folded else folded
            return folded.startswith(root + "/") or folded == root
        folded = f"{base}/{folded}"
    folded = posixpath.normpath(folded)
    if main_worktree is None:
        return False
    main = mdl.derive_path_key(str(main_worktree))
    if folded.startswith(f"{main}/{root}/"):
        return True
    lead = f"{main}/{WORKTREES_DIR}/"
    if not folded.startswith(lead):
        return False
    name, _sep, rest = folded[len(lead):].partition("/")
    return bool(name) and rest.startswith(root + "/")


def check_read_verb(words) -> bool:
    """Whether one segment runs a read verb: its program word, by basename, then its verb word; an
    entry carrying `/` matches the folded program word's tail instead."""
    k = ex._derive_program(words)
    if k is None:
        return False
    program = "/" + words[k].replace("\\", "/")
    base = ex._derive_basename(words[k])
    verb = words[k + 1] if k + 1 < len(words) else None
    for name, want in READ_VERBS:
        hit = program.endswith("/" + name) if "/" in name else base == name
        if hit and (want is None or verb == want):
            return True
    return False


def derive_read_channel(name, tool_input, memory_root, main_worktree=None, cwd=None):
    """`read`, `shell` or None for one tool call, decided from its input in memory and keeping none of it;
    a path word is matched by `check_memory_word` against this clone's `main_worktree`, a relative one
    resolved against `cwd`, the working directory its transcript record carries."""
    if not isinstance(tool_input, dict):
        return None
    if name in ex.SHELL_TOOLS:
        command = tool_input.get("command")
        if not isinstance(command, str) or not command.strip():
            return None
        if name == "PowerShell":
            command = command.replace("\\", "/")
        for words, _sep in ex.extract_segments(command):
            if check_read_verb(words) or any(check_memory_word(w, memory_root, main_worktree, cwd) for w in words):
                return "shell"
        return None
    if ex.TOOL_CLASSES.get(name) == "read":
        if any(check_memory_word(tool_input.get(key), memory_root, main_worktree, cwd) for key in PATH_INPUTS):
            return "read"
    return None


# ---------------------------------------------------------------------------------- one agent

def read_slice_bytes(agent_path):
    """The bytes of the slices a work order inlined for this agent. A STAND-IN: None, the channel
    `unarmed`, until the executor that writes the slice manifest gives this a body (TOOL-dTotalRecall-12 S9)."""
    return None


def measure_agent_memory(path, memory_root, read_slice, coverage=None, main_worktree=None) -> dict:
    """`{"slice": int | None, "read": int, "shell": int}` for one agent transcript, walked through
    `read_records` over a one-file tree and `extract.py#read_result_bytes`, the one result-byte counter;
    torn lines and an unreadable file are counted into `coverage`. A path word counts against this
    clone's `main_worktree` (`check_memory_word`)."""
    path = pathlib.Path(path)
    tree = ex.SessionTree(sid=path.stem, main=path)
    totals = {"read": 0, "shell": 0}
    pending = {}
    cwd = [None]   # the working directory of the record whose events are read, as the harness records it

    def read_cwd_records():
        """Each transcript record, its `cwd` noted before its events are read (TOOL-dTotalRecall-53 S24)."""
        for _src, _file_no, _lineno, rec in ex.read_records(tree, coverage):
            if isinstance(rec, dict) and isinstance(rec.get("cwd"), str):
                cwd[0] = rec["cwd"]
            yield rec

    for kind, tid, name, value in ex.read_result_bytes(read_cwd_records()):
        if not isinstance(tid, str):
            continue
        if kind == "use":
            channel = derive_read_channel(name, value, memory_root, main_worktree, cwd[0])
            if channel:
                pending[tid] = channel
        else:
            channel = pending.pop(tid, None)
            if channel:
                totals[channel] += value
    return {"slice": read_slice(path), **totals}


def read_agent_start(path):
    """Epoch seconds of an agent transcript's first timestamped record; None when it has none."""
    try:
        with open(path, "rb") as fh:
            for raw in fh:
                if not raw.strip():
                    continue
                try:
                    rec = ex.parse_record(raw)
                except ValueError:
                    continue
                t = ex.parse_time(rec.get("timestamp"))
                if t is not None:
                    return t
    except OSError:
        return None
    return None


def read_agent_type(path) -> str:
    """The `agentType` of the agent's `.meta.json`, kept through `_derive_label`, else `unknown`."""
    meta = pathlib.Path(path).with_name(pathlib.Path(path).name[:-len(".jsonl")] + ".meta.json")
    try:
        rec = ex.parse_record(meta.read_bytes()) if meta.is_file() else {}
    except (OSError, ValueError):
        rec = {}
    return ex._derive_label(rec.get("agentType")) or UNKNOWN_TYPE


# ---------------------------------------------------------------------------------- the population

def derive_project_dirs(projects_root, main_worktree) -> list:
    """The project directories holding this clone's sessions: the harness's encoding of the main
    worktree, and that name followed by `--claude-worktrees-`. A directory resolving outside the root
    is not read."""
    root = pathlib.Path(projects_root)
    if not root.is_dir():
        return []
    name = PROJECT_NAME_RE.sub("-", str(main_worktree))
    inside = root.resolve()
    return [d for d in sorted(root.iterdir())
            if (d.name == name or d.name.startswith(name + WORKTREE_INFIX)) and d.is_dir()
            and ex._check_inside(d, inside)]


def check_in_window(start, window) -> bool:
    t_from, t_to = window
    if start is None:
        return t_from is None and t_to is None
    return (t_from is None or start >= t_from) and (t_to is None or start < t_to)


def measure_memory_population(projects_root, main_worktree, memory_root, window, read_slice) -> dict:
    """Every agent of this clone's sessions whose start lies in `window`, `(from, to)` with None an open
    bound, measured: `{"sessions", "agents": [(type, channels)], "coverage"}`."""
    coverage = {"torn": 0, "unreadable": 0}
    agents, sessions = [], 0
    t_from = window[0]
    for project in derive_project_dirs(projects_root, main_worktree):
        for main in sorted(project.glob("*.jsonl")):
            tree = ex.build_session_tree(main)
            seen = False
            for path in tree.agents + tree.workflow_agents:
                try:
                    if t_from is not None and path.stat().st_mtime < t_from:
                        continue  # last written before the window opens, so it cannot start inside it
                except OSError:
                    coverage["unreadable"] += 1
                    continue
                if not check_in_window(read_agent_start(path), window):
                    continue
                seen = True
                agents.append((read_agent_type(path),
                               measure_agent_memory(path, memory_root, read_slice, coverage, main_worktree)))
            sessions += seen
    return {"sessions": sessions, "agents": agents, "coverage": coverage}


# ---------------------------------------------------------------------------------- the figures

def derive_quantile(values, q):
    """The `[ms2-instrument]`'s quantile, `sorted(v)[min(len(v) - 1, int(len(v) * q))]`; None over none."""
    if not values:
        return None
    ordered = sorted(values)
    return ordered[min(len(ordered) - 1, int(len(ordered) * q))]


def derive_total(channels) -> int:
    return channels["read"] + channels["shell"] + (channels["slice"] or 0)


def check_slice_armed(agents) -> bool:
    """Armed when at least one agent was measured and none of them read the slice channel as None."""
    return bool(agents) and all(channels["slice"] is not None for _type, channels in agents)


def derive_memory_verdict(totals, now, window, slice_armed):
    """`(word, exit code)` over the totals of the agents reading memory in the window."""
    if window[1] is None or now < window[1]:
        word = "not-due"
    elif not slice_armed:
        word = "unarmed"
    elif not totals:
        word = "empty"
    else:
        word = "pass" if derive_quantile(totals, 0.5) < TARGET_BYTES else "fail"
    return word, VERDICT_EXITS[word]


def render_utc(t) -> str:
    if t is None:
        return "open"
    return datetime.datetime.fromtimestamp(t, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def render_figure(value) -> str:
    return "-" if value is None else f"{value:,}"


def render_type_row(label, agents, armed) -> str:
    reading = [c for c in agents if derive_total(c) > 0]
    cells = [f"{len(agents):,}", f"{len(reading):,}"]
    for pick in (derive_total, lambda c: c["read"], lambda c: c["shell"]):
        values = [pick(c) for c in reading]
        cells += [render_figure(derive_quantile(values, 0.5)), render_figure(derive_quantile(values, 0.9))]
    if armed:
        values = [c["slice"] for c in reading]
        cells += [render_figure(derive_quantile(values, 0.5)), render_figure(derive_quantile(values, 0.9))]
    else:
        cells += ["unarmed", "unarmed"]
    cells += [f"{sum(c['read'] for c in agents):,}", f"{sum(c['shell'] for c in agents):,}",
              f"{sum(c['slice'] for c in agents):,}" if armed else "unarmed"]
    return f"memory: {label:<20}" + "".join(f"{cell:>11}" for cell in cells)


def render_memory_report(population, window, verdict=None) -> list:
    """The report's lines, every figure derived here; the verdict line only when `verdict` is given as
    `(word, exit code)`."""
    agents = population["agents"]
    armed = check_slice_armed(agents)
    state = "armed" if armed else "unarmed"
    totals = [derive_total(c) for _t, c in agents if derive_total(c) > 0]
    cov = population["coverage"]
    lines = [f"memory: window {render_utc(window[0])} .. {render_utc(window[1])} · sessions "
             f"{population['sessions']:,} · agents {len(agents):,} · reading memory {len(totals):,} · torn "
             f"{cov.get('torn', 0)} · unreadable {cov.get('unreadable', 0)} · slice {state}"]
    if not population["sessions"]:
        lines.append(f"memory: no session in the window · slice {state}")
    elif not totals:
        lines.append(f"memory: no agent in the window read memory · slice {state}")
    heads = ("agents", "reading", "median B", "p90 B", "read med", "read p90", "shell med", "shell p90",
             "slice med", "slice p90", "read B", "shell B", "slice B")
    lines.append(f"memory: {'agent type':<20}" + "".join(f"{h:>11}" for h in heads))
    by_type = {}
    for kind, channels in agents:
        by_type.setdefault(kind, []).append(channels)
    for kind in sorted(by_type):
        lines.append(render_type_row(kind, by_type[kind], armed))
    lines.append(render_type_row(POOLED, [c for _t, c in agents], armed))
    if verdict is not None:
        median = derive_quantile(totals, 0.5)
        lines.append(f"memory: verdict {verdict[0]} · median {'-' if median is None else median} B · target "
                     f"{TARGET_BYTES} B · agents {len(totals)} · slice {state}")
    return lines


# ---------------------------------------------------------------------------------- the landing

def resolve_landed_time(rev, root):
    """The committer time of `rev`, refused unless it names a commit that is an ancestor of `HEAD`.
    ValueError naming the refusal."""
    def run(*args):
        return subprocess.run(["git", *args], cwd=str(root), capture_output=True, text=True,
                              encoding="utf-8", errors="replace")
    if not isinstance(rev, str) or not rev or rev.startswith("-"):
        raise ValueError(f"runlog: --landed {rev!r} is not a revision")
    found = run("rev-parse", "--verify", "--quiet", "--end-of-options", rev + "^{commit}")
    sha = found.stdout.strip()
    if found.returncode != 0 or not sha:
        raise ValueError(f"runlog: --landed {rev!r} names no commit of this repository")
    if run("merge-base", "--is-ancestor", sha, "HEAD").returncode != 0:
        raise ValueError(f"runlog: --landed {rev!r} is not an ancestor of HEAD, so it landed nothing here")
    stamp = run("show", "-s", "--format=%ct", sha).stdout.strip()
    if not stamp.isdigit():
        raise ValueError(f"runlog: --landed {rev!r} has no committer time git would print")
    return float(stamp)


# ---------------------------------------------------------------------------------- the fixture

FIXTURE_CASES = ("read-memory", "read-other", "grep-memory", "shell-path", "record-show", "gov-tag",
                 "recall-query", "shell-other", "foreign-dir", "outside-window", "median-under",
                 "median-over", "not-due", "unarmed", "empty", "privacy",
                 "harness-memory", "msys-path", "foreign-memory-path", "bare-root", "msys-d-drive", "dot-relative",
                 "parent-relative")
FIXTURE_CLOCK = "2026-12-15T00:00:00Z"
# The scratch main worktree the planted project directories encode, and every planted absolute memory path
# sits under (TOOL-dTotalRecall-43 S16): the memory measure counts this clone's tree alone.
FIXTURE_MAIN = "C:/fx/repo"
FIXTURE_FOREIGN = "C:/fx/other-tree"
FIXTURE_MARKER = "TOTALRECALL-12-MARKER"
FX_MEMORY_FILE = "C:\\fx\\repo\\memory\\builds\\b\\RUN.md"
FX_KIT_FILE = "C:\\fx\\repo\\tools\\memory-tree\\README.md"
FX_SKILL_FILE = "tools\\memory-recall\\SKILL.md"
# One planted agent: where its transcript sits, its type, its start in days after the landing, its tool
# calls as (tool, input, result bytes, or a list of text-item sizes), and its planted slice bytes, read
# only where the case arms the channel.
FIXTURE_PLANTS = {
    "read-memory": {"agents": [("main", "gov-builder", 1, [("Read", {"file_path": FX_MEMORY_FILE}, 1200)], 0)],
                    "torn": True},
    "read-other": {"agents": [("main", "gov-builder", 1, [("Read", {"file_path": FX_KIT_FILE}, 900),
                                                           ("Read", {"file_path": FX_SKILL_FILE}, 300)], 0)]},
    "grep-memory": {"agents": [("main", "gov-builder", 1, [
        ("Grep", {"pattern": "ask", "path": "C:\\fx\\repo\\memory\\builds"}, [400, 300])], 0)]},
    "shell-path": {"agents": [("main", "gov-builder", 1, [
        ("Bash", {"command": "cat memory/DECISIONS.md | head -5"}, 500),
        ("PowerShell", {"command": "Get-Content C:\\fx\\repo\\memory\\DECISIONS.md"}, 300)], 0)]},
    "record-show": {"agents": [("main", "gov-builder", 1, [
        ("Bash", {"command": 'python "C:\\fx\\repo\\tools\\memory-tree\\gov_record.py" show TOOL-x-1'}, 1500)],
        0)]},
    "gov-tag": {"agents": [("main", "gov-builder", 1, [
        ("Bash", {"command": 'python "C:\\fx\\repo\\tools\\playbook\\gov_tag.py" where feature.x'}, 400),
        ("Bash", {"command": "gov tag show feature.x"}, 300)], 0)]},
    "recall-query": {"agents": [("main", "gov-builder", 1, [
        ("Bash", {"command": 'python "C:\\fx\\repo\\tools\\memory-recall\\query.py" "a question" --terms "a b"'},
         800)], 0)]},
    "shell-other": {"agents": [("main", "gov-builder", 1, [
        ("Bash", {"command": "git log --oneline -5"}, 300),
        ("Bash", {"command": 'grep -rn ask "C:\\fx\\repo\\tools\\memory-recall"'}, 200),
        ("Bash", {"command": "python -c 'print(1)' memories"}, 100)], 0)]},
    # TOOL-dTotalRecall-43 S16, S17: the harness's own auto-memory directory and another repository's
    # memory/ count zero; this clone's memory/ spelled from its MSYS root, and the bare root, count.
    "harness-memory": {"agents": [("main", "gov-builder", 1, [
        ("Read", {"file_path": "C:\\Users\\u\\.claude\\projects\\p\\memory\\MEMORY.md"}, 700)], 0)]},
    "msys-path": {"agents": [("main", "gov-builder", 1, [
        ("Read", {"file_path": "/c/fx/repo/memory/LIVE.md"}, 450),
        ("Read", {"file_path": "/c/fx/repo/.claude/worktrees/side/memory/LIVE.md"}, 50)], 0)]},
    "foreign-memory-path": {"agents": [("main", "gov-builder", 1, [
        ("Read", {"file_path": "C:\\fx\\other-tree\\memory\\DECISIONS.md"}, 800),
        ("Bash", {"command": "cat /c/fx/other-tree/memory/LIVE.md"}, 200)], 0)]},
    "bare-root": {"agents": [("main", "gov-builder", 1, [("Bash", {"command": "ls memory"}, 350)], 0)]},
    # TOOL-dTotalRecall-53 S24: a clone on another drive read through its MSYS root, its main worktree spelled
    # in another case on Windows, whose paths are case-blind; and two relative words resolved against the
    # working directory each call's records carry. `main` is the plant's main worktree where it is not
    # FIXTURE_MAIN; `cwd` the working directory every record of its agents carries.
    "msys-d-drive": {"main": "D:/FX/Repo" if os.name == "nt" else "D:/fx/repo", "agents": [("main", "gov-builder", 1, [
        ("Read", {"file_path": "/d/fx/repo/memory/LIVE.md"}, 450)], 0)]},
    "dot-relative": {"cwd": FIXTURE_MAIN, "agents": [("main", "gov-builder", 1, [
        ("Bash", {"command": "cat ./memory/LIVE.md"}, 300)], 0)]},
    "parent-relative": {"cwd": FIXTURE_MAIN + "/sub/dir", "agents": [("main", "gov-builder", 1, [
        ("Bash", {"command": "cat ../../memory/LIVE.md"}, 250)], 0)]},
    "foreign-dir": {"agents": [("main", "gov-builder", 1, [("Read", {"file_path": FX_MEMORY_FILE}, 600)], 0),
                               ("foreign", "gov-builder", 1, [("Read", {"file_path": FX_MEMORY_FILE}, 5000)], 0)]},
    "outside-window": {"agents": [("main", "gov-builder", 1, [("Read", {"file_path": FX_MEMORY_FILE}, 600)], 0),
                                  ("main", "gov-builder", -1, [("Read", {"file_path": FX_MEMORY_FILE}, 5000)],
                                   0)]},
    "median-under": {"armed": True, "agents": [
        ("main", "gov-builder", 1, [("Read", {"file_path": FX_MEMORY_FILE}, 20000)], 11000),
        ("worktree", "gov-reviewer", 2, [("Read", {"file_path": FX_MEMORY_FILE}, 2000),
                                         ("Bash", {"command": "cat memory/LIVE.md"}, 10000)], 20000),
        ("workflow", "lens", 3, [("Bash", {"command": "gov tag show feature.x"}, 40000)], 0)]},
    "median-over": {"armed": True, "agents": [
        ("main", "gov-builder", 1, [("Read", {"file_path": FX_MEMORY_FILE}, 20000)], 11000),
        ("worktree", "gov-reviewer", 2, [("Read", {"file_path": FX_MEMORY_FILE}, 2000),
                                         ("Bash", {"command": "cat memory/LIVE.md"}, 12000)], 20000),
        ("workflow", "lens", 3, [("Bash", {"command": "gov tag show feature.x"}, 40000)], 0)]},
    "not-due": {"armed": True, "landed_days": 10,
                "agents": [("main", "gov-builder", 1, [("Read", {"file_path": FX_MEMORY_FILE}, 1200)], 0)]},
    "unarmed": {"agents": [("main", "gov-builder", 1, [("Read", {"file_path": FX_MEMORY_FILE}, 1200)], 0),
                           ("workflow", "lens", 2, [("Bash", {"command": "cat memory/LIVE.md"}, 700)], 0)]},
    "empty": {"armed": True, "agents": [("main", "gov-builder", 1, [("Read", {"file_path": FX_KIT_FILE}, 900)], 0)]},
    "privacy": {"agents": [("main", "gov-builder", 1, [
        ("Bash", {"command": f"cat memory/{FIXTURE_MARKER}.md"}, f"{FIXTURE_MARKER} result text"),
        ("Read", {"file_path": f"memory/{FIXTURE_MARKER}.md"}, f"{FIXTURE_MARKER} read text")], 0)]},
}


def build_fixture_result(result):
    """A `tool_result` content: `n` bytes of text, a list of text items of those sizes, or text verbatim."""
    if isinstance(result, int):
        return "x" * result
    if isinstance(result, list):
        return [{"type": "text", "text": "y" * n} for n in result]
    return result


def build_fixture_agent(start, calls, cwd=None) -> list:
    """One agent transcript's records: a timestamped task, then each call as a `tool_use` and its result,
    each record carrying `cwd` where the plant gives one, as the harness records it."""
    records = [{"type": "user", "timestamp": render_utc(start), "message": {"role": "user", "content": "the task"}}]
    for i, (tool, tool_input, result) in enumerate(calls, 1):
        tid = f"toolu_fx_{i:03d}"
        records.append({"type": "assistant", "timestamp": render_utc(start + 2 * i - 1), "message": {
            "role": "assistant", "content": [{"type": "tool_use", "id": tid, "name": tool, "input": tool_input}]}})
        records.append({"type": "user", "timestamp": render_utc(start + 2 * i), "message": {
            "role": "user", "content": [{"type": "tool_result", "tool_use_id": tid,
                                         "content": build_fixture_result(result)}]}})
    if cwd is not None:
        for rec in records:
            rec["cwd"] = cwd
    return records


def write_fixture_lines(path, records):
    """One record per line, the shape the kit's self-test writes; a string record is written verbatim."""
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = [r if isinstance(r, str) else json.dumps(r) for r in records]
    path.write_bytes(("\n".join(rows) + "\n").encode("utf-8"))


def write_memory_fixture(base, case):
    """The case's transcripts under `<base>/projects`: `(projects, landed, slices)`, `slices` each
    agent transcript's name -> its planted slice bytes."""
    plant = FIXTURE_PLANTS[case]
    clock = ex.parse_time(FIXTURE_CLOCK)
    landed = clock - plant.get("landed_days", 40) * DAY_SECONDS
    projects = pathlib.Path(base) / "projects"
    main_dir = PROJECT_NAME_RE.sub("-", plant.get("main", FIXTURE_MAIN))
    homes = {"main": main_dir, "workflow": main_dir, "worktree": main_dir + WORKTREE_INFIX + "side",
             "foreign": PROJECT_NAME_RE.sub("-", FIXTURE_FOREIGN)}
    slices = {}
    for n, (where, kind, days, calls, slice_bytes) in enumerate(plant["agents"]):
        sid = str(uuid.uuid4())
        home = projects / homes[where]
        start = landed + days * DAY_SECONDS
        write_fixture_lines(home / f"{sid}.jsonl", [{"type": "user", "timestamp": render_utc(start),
                                                     "message": {"role": "user", "content": "main"}}])
        sub = home / sid / "subagents"
        if where == "workflow":
            sub = sub / HARNESS_RUN_DIR / "wf_fixture"
        name = f"agent-fx{n}"
        records = build_fixture_agent(start, calls, plant.get("cwd"))
        if plant.get("torn") and n == 0:
            records.append('{"type": "assistant", "torn')
        write_fixture_lines(sub / f"{name}.jsonl", records)
        # A transcript is last written at or after its last record, and the population reads that
        # write time first; the fixture's clock is not the machine's, so the time is set to match.
        last = start + 2 * len(calls)
        os.utime(sub / f"{name}.jsonl", (last, last))
        (sub / f"{name}.meta.json").write_bytes(json.dumps({"agentType": kind}).encode("utf-8"))
        slices[f"{name}.jsonl"] = slice_bytes
    return projects, landed, slices


def print_memory_fixture(case) -> int:
    """Plant `case` in a scratch transcripts root, measure it as the CLI does, print the report and its
    verdict, remove the scratch, and return the verdict's exit code. Only here does a slice reader
    return bytes, and only where the case arms the channel."""
    base = pathlib.Path(tempfile.mkdtemp(prefix="runlog-memory-"))
    try:
        projects, landed, slices = write_memory_fixture(base, case)
        read_slice = read_slice_bytes
        if FIXTURE_PLANTS[case].get("armed"):
            def read_slice(agent_path):
                return slices.get(pathlib.Path(agent_path).name, 0)
        window = (landed, landed + WINDOW_DAYS * DAY_SECONDS)
        population = measure_memory_population(projects, FIXTURE_PLANTS[case].get("main", FIXTURE_MAIN),
                                               rl.MEMORY_ROOT_DEFAULT, window, read_slice)
        totals = [derive_total(c) for _t, c in population["agents"] if derive_total(c) > 0]
        verdict = derive_memory_verdict(totals, ex.parse_time(FIXTURE_CLOCK), window,
                                        check_slice_armed(population["agents"]))
        sys.stdout.write("\n".join(render_memory_report(population, window, verdict)) + "\n")
        sys.stdout.flush()
        return verdict[1]
    finally:
        shutil.rmtree(base, ignore_errors=True)
