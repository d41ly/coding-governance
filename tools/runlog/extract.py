#!/usr/bin/env python3
"""extract.py — the runlog kit's transcript extractor (TOOL-dLoggedFlight-6). gov:kit runlog@1.0

The driver's journal lines cover a small share of what a run does. The rest — every tool call, every
owner turn, the compactions, the limits and the token cost — is recorded only in Claude Code's session
transcripts, on the machine that ran the build. This module reads those transcripts and keeps a
STRUCTURAL event list: no command text, no narration, no owner-turn text, no tool output. A command
is classified in memory and the text is dropped; the one command that yields tokens, a driver call,
is passed through the kit's redaction table before its verb and slug are read.

It is the Claude Code adapter and says so: the transcript format is not a contract, eight engine
versions appeared in one month, so unknown keys are tolerated, an unknown record type is counted,
and a torn line lands in the coverage block rather than raising. The rules it applies, and what each
was measured against, are in the kit README's extractor section and the unit's spec; they are not
restated here.

Reading is streamed. `read_records` holds one parsed record at a time, per open file, and it opens
one file at a time; everything the extractor keeps between records is a compact tuple. `parse_record`
is the one place a line becomes a record, which is the seam the self-test counts live records through.

Every path is passed in or resolved from the environment and git; a session id is shape-checked
before it reaches a path, and every constructed path is contained under its root. This file names
nothing outside itself.
"""
from __future__ import annotations

import datetime
import hashlib
import json
import os
import pathlib
import re
import sys
import time
from dataclasses import dataclass

HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import runlog_lib as rl  # noqa: E402

SCHEMA = 1
# The CLOSED lists the self-test holds its fixtures against, in both directions: a member with no
# fixture producing it reds, and so does a fixture producing something that is not a member.
KINDS = ("tool", "tool_end", "owner", "keepalive", "compact", "api_error", "limit", "denial",
         "workflow", "agent", "usage")
CLASSES = ("driver", "git-commit", "git-merge", "git-push", "bar", "test", "read", "write", "edit",
           "workflow", "agent", "cron", "ask", "other")
FLAGS = ("destructive", "piped")
SOURCES = ("main", "agent", "workflow")
OWNER_VIA = ("typed", "queued", "interrupt")
ATTRIBUTIONS = ("driver", "given", "heuristic")
# The record types a transcript was measured to carry. Anything else is counted by name, never read.
KNOWN_TYPES = frozenset({"user", "assistant", "attachment", "system", "queue-operation", "summary",
                         "last-prompt", "custom-title", "ai-title", "atis-latch", "mode",
                         "file-history-snapshot", "file-history-delta", "frame-link"})

# A session id is a lowercase UUID and nothing else. It becomes a path component, so this shape is the
# gate every id passes before a glob or a write sees it.
SID_RE = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
# A value persisted from a transcript's structured fields — a label, a model, a status, a type name.
LABEL_RE = re.compile(r"[A-Za-z0-9._:-]{1,64}")
# A driver call's slug is read by the kit's ONE slug grammar, `rl.SLUG_RE`, the driver's own spelling.
VERB_RE = re.compile(r"--[a-z][a-z-]{1,30}")
ENV_ASSIGN_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*=.*", re.S)
HEREDOC_RE = re.compile(r"<<-?[ \t]*(['\"]?)([A-Za-z_][A-Za-z0-9_]*)\1")
NOTIFICATION_RE = re.compile(r"<task-notification>(.*?)</task-notification>", re.S)
TOOL_USE_ID_RE = re.compile(r"<tool-use-id>([A-Za-z0-9_-]{1,80})</tool-use-id>")
STATUS_RE = re.compile(r"<status>([a-z_]{1,20})</status>")
SUMMARY_RE = re.compile(r"<summary>(.*?)</summary>", re.S)
EXIT_CODE_RE = re.compile(r"exit code (-?[0-9]{1,5})", re.I)
RESULT_RC_RE = re.compile(r"Exit code (-?[0-9]{1,5})")
HOOK_LEAD_RE = re.compile(r"\s*(?:Pre|Post)ToolUse:")
LEAD_TAG_RE = re.compile(r"\s*<([a-z][a-z0-9-]{0,40})>")
EPOCH_RE = re.compile(r"[0-9]{1,12}(?:\.[0-9]{1,9})?")

INTERRUPT_LEAD = "[Request interrupted by user"
DRIVER_SCRIPT = "unattended.sh"
BAR_SCRIPT = "run-gates.sh"
GIT_NAMES = frozenset({"git", "git.exe"})
GIT_OPTS_WITH_ARG = frozenset({"-C", "-c", "--git-dir", "--work-tree", "--namespace",
                               "--config-env"})
GIT_CLASSES = {"commit": "git-commit", "merge": "git-merge", "push": "git-push"}
WRAPPERS = frozenset({"sudo", "command", "exec", "time", "nice", "env", "nohup"})
INTERPRETERS = frozenset({"bash", "sh", "zsh", "dash", "python", "python3", "py", "node", "pwsh",
                          "powershell"})
TEST_TAILS = (".test.sh", ".test.py", ".test.js")
TEST_NAMES = frozenset({"selftest.py", "selftest.sh", "pytest"})
SHELL_TOOLS = frozenset({"Bash", "PowerShell"})
TOOL_CLASSES = {"Read": "read", "Grep": "read", "Glob": "read", "LS": "read", "NotebookRead": "read",
                "Write": "write", "Edit": "edit", "MultiEdit": "edit", "NotebookEdit": "edit",
                "Workflow": "workflow", "Agent": "agent", "Task": "agent", "CronCreate": "cron",
                "CronDelete": "cron", "CronList": "cron", "AskUserQuestion": "ask"}
# Among a shell command's segments, the class is the FIRST of these that any segment names: a push
# that follows a commit in one `&&` chain is a push.
SHELL_PRIORITY = ("driver", "git-push", "git-merge", "git-commit", "bar", "test")
SEPARATORS = ("&&", "||", "|&", "|", ";", "&", "\n", "(", ")")
# The characters a separator can start with. The tokenizer tries the separator list only at these, so
# an ordinary character costs one set lookup rather than one `startswith` per separator. Profiled over
# the largest local session, trying the whole list at every character cost more than parsing the JSON.
SEPARATOR_HEADS = frozenset(sep[0] for sep in SEPARATORS)
REPO_KEY_HEX = 16
STATE_DIR_NAME = "runlog"
SESSIONS_DIR = "sessions"


@dataclass(frozen=True)
class SessionTree:
    """One session's transcript files. `main` is None when no transcript for `sid` is on this machine."""
    sid: str
    main: pathlib.Path | None = None
    agents: tuple = ()
    workflow_agents: tuple = ()
    workflows: tuple = ()
    copies: int = 0
    escaped: int = 0


# ---------------------------------------------------------------------------------- small values

def parse_time(value) -> float | None:
    """Epoch seconds from an ISO-8601 stamp, an epoch string, or a number (milliseconds when huge)."""
    if isinstance(value, bool) or value is None:
        return None
    if isinstance(value, (int, float)):
        v = float(value)
        return v / 1000.0 if v > 1e11 else v
    if not isinstance(value, str) or not value.strip():
        return None
    s = value.strip()
    if EPOCH_RE.fullmatch(s):
        return float(s)
    try:
        stamp = datetime.datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None
    if stamp.tzinfo is None:
        stamp = stamp.replace(tzinfo=datetime.timezone.utc)
    return stamp.timestamp()


def _derive_token(value) -> str | None:
    return value if isinstance(value, str) and LABEL_RE.fullmatch(value) else None


def _derive_label(value) -> str | None:
    """A label kept only when it is token-shaped AND the redaction table finds nothing in it."""
    token = _derive_token(value)
    return token if token is not None and not rl.scan_secrets(token) else None


def _derive_int(value) -> int | None:
    return value if isinstance(value, int) and not isinstance(value, bool) else None


def _derive_status(value) -> int | None:
    """An HTTP-style status as an int, whether the transcript wrote it as a number or a string."""
    if isinstance(value, str) and value.isdigit() and len(value) <= 3:
        return int(value)
    return _derive_int(value)


def _derive_hash(text: str) -> bytes:
    return hashlib.sha256(text.strip().encode("utf-8", "surrogatepass")).digest()[:16]


def _derive_basename(word: str) -> str:
    return word.replace("\\", "/").rsplit("/", 1)[-1]


def _check_inside(path: pathlib.Path, root: pathlib.Path) -> bool:
    try:
        return path.resolve().is_relative_to(root)
    except OSError:
        return False


# ---------------------------------------------------------------------------------- locations

def resolve_projects_root(env=None, platform=None, override=None) -> pathlib.Path:
    """Where Claude Code keeps its transcripts: `override`, else `$CLAUDE_CONFIG_DIR/projects`, else the
    profile's `.claude/projects`. Every root is read from `env`, so a caller can aim all of them."""
    if override:
        return pathlib.Path(override)
    env = os.environ if env is None else env
    plat = sys.platform if platform is None else platform
    if env.get("CLAUDE_CONFIG_DIR"):
        return pathlib.Path(env["CLAUDE_CONFIG_DIR"]) / "projects"
    home = (env.get("USERPROFILE") or env.get("HOME")) if plat.startswith("win") else env.get("HOME")
    if not home:
        raise ValueError("runlog: no transcripts root resolves: CLAUDE_CONFIG_DIR and the profile's "
                         "home are both unset; pass --transcripts")
    return pathlib.Path(home) / ".claude" / "projects"


def resolve_state_dir(env=None, platform=None) -> pathlib.Path:
    """The user-profile store: `RUNLOG_STATE_DIR`, else the platform's per-user state dir + `runlog`.

    Refuses by name rather than guessing, and refuses a RELATIVE override, which would put extracts
    inside whatever tree the command ran in, where git can commit them.
    """
    env = os.environ if env is None else env
    plat = sys.platform if platform is None else platform
    override = env.get("RUNLOG_STATE_DIR")
    if override:
        path = pathlib.Path(override)
        if not path.is_absolute():
            raise ValueError(f"runlog: RUNLOG_STATE_DIR is relative ({override!r}); the store is "
                             "absolute or extracts land in whatever tree the command ran in")
        return path
    if plat.startswith("win"):
        base = env.get("LOCALAPPDATA")
        if not base:
            raise ValueError("runlog: no store resolves: LOCALAPPDATA is unset; set RUNLOG_STATE_DIR")
        return pathlib.Path(base) / STATE_DIR_NAME
    home = env.get("HOME")
    if not home:
        raise ValueError("runlog: no store resolves: HOME is unset; set RUNLOG_STATE_DIR")
    if plat == "darwin":
        return pathlib.Path(home) / "Library" / "Application Support" / STATE_DIR_NAME
    xdg = env.get("XDG_STATE_HOME") or os.path.join(home, ".local", "state")
    return pathlib.Path(xdg) / STATE_DIR_NAME


def resolve_repo_key(start=None) -> str:
    """The first 16 hex of sha256 over the NORMALISED git common dir, so every worktree of one clone
    shares one store and two clones never do."""
    common = rl.resolve_journal_root(start).parent
    norm = os.path.normcase(os.path.normpath(str(common))).replace("\\", "/")
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()[:REPO_KEY_HEX]


def build_session_tree(main, copies=1) -> SessionTree:
    """The tree beside a known main transcript: its agents, its workflow agents and its workflow files.

    A file resolving outside the session dir is not listed; it is counted in `escaped`.
    """
    main = pathlib.Path(main)
    sid = main.name[:-len(".jsonl")] if main.name.endswith(".jsonl") else main.stem
    sdir = main.with_name(sid)
    agents, wagents, flows = [], [], []
    escaped = 0
    if sdir.is_dir():
        inside = sdir.resolve()
        sub = sdir / "subagents"
        for path in sorted(sub.rglob("agent-*.jsonl")) if sub.is_dir() else ():
            if not _check_inside(path, inside):
                escaped += 1
                continue
            (wagents if path.relative_to(sub).parts[0] == "workflows" else agents).append(path)
        flow_dir = sdir / "workflows"
        for path in sorted(flow_dir.glob("wf_*.json")) if flow_dir.is_dir() else ():
            if not _check_inside(path, inside):
                escaped += 1
                continue
            flows.append(path)
    return SessionTree(sid=sid, main=main, agents=tuple(agents), workflow_agents=tuple(wagents),
                       workflows=tuple(flows), copies=copies, escaped=escaped)


def resolve_session_tree(sid, projects_root) -> SessionTree:
    """The tree for `sid`, found by ONE glob of `<projects_root>/*/<sid>.jsonl`.

    The id is shape-checked before any path sees it, and a hit resolving outside the root is refused
    by name. No hit is a state, not a refusal: the tree comes back with `main` None.
    """
    if not isinstance(sid, str) or SID_RE.fullmatch(sid) is None:
        raise ValueError(f"runlog: {str(sid)[:80]!r} is not a session id; a session id is a lowercase "
                         "UUID, and nothing else reaches a path")
    root = pathlib.Path(projects_root)
    inside = root.resolve()
    hits = sorted(root.glob(f"*/{sid}.jsonl"))
    outside = [h for h in hits if not _check_inside(h, inside)]
    if outside:
        raise ValueError(f"runlog: session {sid} resolves outside the transcripts root through "
                         f"{len(outside)} project dir(s), and nothing outside the root is read")
    if not hits:
        return SessionTree(sid=sid)
    main = max(hits, key=lambda p: (p.stat().st_size, p.as_posix()))
    return build_session_tree(main, copies=len(hits))


# ---------------------------------------------------------------------------------- the reader

def parse_record(raw) -> dict:
    """One transcript line into a record. Raises ValueError on a line that is not a JSON object."""
    try:
        rec = json.loads(raw)
    except RecursionError as exc:
        raise ValueError("a transcript line nested too deep to parse") from exc
    if not isinstance(rec, dict):
        raise ValueError("a transcript line that is not a JSON object")
    return rec


def _build_file_list(tree: SessionTree) -> list:
    if tree.main is None:
        return []
    return ([("main", tree.main)] + [("agent", p) for p in tree.agents]
            + [("workflow", p) for p in tree.workflow_agents])


def read_records(tree: SessionTree, coverage=None):
    """Yield `(src, file_no, lineno, record)` for every good line, ONE FILE AT A TIME.

    At most one parsed record is alive per open file: the record is handed out and never kept here,
    so what the caller drops is freed. A torn line and an unreadable file are counted into
    `coverage` when one is given, and never raise.
    """
    cov = {} if coverage is None else coverage
    for file_no, (src, path) in enumerate(_build_file_list(tree)):
        try:
            fh = open(path, "rb")
        except OSError:
            cov["unreadable"] = cov.get("unreadable", 0) + 1
            continue
        cov["files"] = cov.get("files", 0) + 1
        with fh:
            for lineno, raw in enumerate(fh, 1):
                if not raw.strip():
                    continue
                try:
                    yield src, file_no, lineno, parse_record(raw)
                except ValueError:
                    cov["torn"] = cov.get("torn", 0) + 1


def _read_json_file(path, coverage) -> dict | None:
    try:
        return parse_record(pathlib.Path(path).read_bytes())
    except OSError:
        coverage["unreadable"] += 1
    except ValueError:
        coverage["torn"] += 1
    return None


# ---------------------------------------------------------------------------------- classification

def _remove_heredocs(command: str) -> str:
    """Drop every heredoc body, delimiter line included. A body is text, never a command."""
    if "<<" not in command:
        return command
    out, pending = [], []
    for line in command.split("\n"):
        if pending:
            if line.strip() == pending[0]:
                pending.pop(0)
            continue
        out.append(line)
        for m in HEREDOC_RE.finditer(line):
            if m.start() > 0 and line[m.start() - 1] == "<":
                continue
            pending.append(m.group(2))
    return "\n".join(out)


def _read_separator(text: str, i: int) -> str | None:
    for sep in SEPARATORS:
        if text.startswith(sep, i):
            if sep == "&" and ((i > 0 and text[i - 1] in "<>") or text.startswith("&>", i)):
                return None
            return sep
    return None


def extract_segments(command: str) -> list:
    """A shell command as `(words, separator-after)` pairs, honouring quotes, escapes and heredocs.

    A mention inside quotes stays inside ONE word and a heredoc body is dropped whole, so a commit
    message that names a destructive command is not one. This is not a shell: `$(...)` inside quotes,
    `bash -c` and `eval` are not descended into, and a call nested in one is not seen.
    """
    text = _remove_heredocs(command)
    segs, words, cur = [], [], []
    in_word = False
    i, n = 0, len(text)
    while i < n:
        ch = text[i]
        if ch == "'":
            j = text.find("'", i + 1)
            j = n if j < 0 else j
            cur.append(text[i + 1:j])
            in_word, i = True, j + 1
            continue
        if ch == '"':
            j, buf = i + 1, []
            while j < n and text[j] != '"':
                if text[j] == "\\" and j + 1 < n and text[j + 1] in '"\\$`':
                    buf.append(text[j + 1])
                    j += 2
                    continue
                buf.append(text[j])
                j += 1
            cur.append("".join(buf))
            in_word, i = True, j + 1
            continue
        if ch == "\\" and i + 1 < n:
            if text[i + 1] != "\n":
                cur.append(text[i + 1])
                in_word = True
            i += 2
            continue
        if ch in " \t\r":
            if in_word:
                words.append("".join(cur))
                cur, in_word = [], False
            i += 1
            continue
        if ch == "#" and not in_word:
            j = text.find("\n", i)
            i = n if j < 0 else j
            continue
        sep = _read_separator(text, i) if ch in SEPARATOR_HEADS else None
        if sep:
            if in_word:
                words.append("".join(cur))
                cur, in_word = [], False
            segs.append((words, sep))
            words = []
            i += len(sep)
            continue
        cur.append(ch)
        in_word = True
        i += 1
    if in_word:
        words.append("".join(cur))
    if words:
        segs.append((words, ""))
    return segs


def _derive_git_subcommand(args: list) -> tuple:
    i = 0
    while i < len(args):
        a = args[i]
        if a in GIT_OPTS_WITH_ARG:
            i += 2
            continue
        if a.startswith("-"):
            i += 1
            continue
        return a, args[i + 1:]
    return None, []


def _check_destructive(sub, args) -> bool:
    """Whether one git subcommand, with its arguments, throws away work or history."""
    a = set(args)
    if sub == "reset":
        return "--hard" in a
    if sub == "clean":
        return any(x == "--force" or (x.startswith("-") and not x.startswith("--") and "f" in x[1:])
                   for x in args)
    if sub == "push":
        return (bool(a & {"--force", "-f", "--mirror", "--delete", "-d"})
                or any(x.startswith("--force-with-lease") or (not x.startswith("-") and x[:1] in "+:")
                       for x in args if x))
    if sub == "branch":
        return "-D" in a or (bool(a & {"-d", "--delete"}) and bool(a & {"-f", "--force"}))
    if sub == "checkout":
        return bool(a & {"-f", "--force", "--", "."})
    if sub == "restore":
        return not (a & {"--staged", "-S"}) or bool(a & {"--worktree", "-W"})
    if sub == "stash":
        return bool(args) and args[0] in ("drop", "clear")
    if sub == "worktree":
        return bool(args) and args[0] == "remove" and bool(a & {"-f", "--force"})
    if sub == "update-ref":
        return "-d" in a
    return False


def _derive_program(words: list) -> int | None:
    """The index of the word a segment RUNS: past env assignments and wrappers, and past an
    interpreter and its options, so `bash -x run.sh` runs `run.sh` and `grep x run.sh` runs grep.
    None when the segment runs inline code (`-c`) or nothing at all."""
    i = 0
    while i < len(words):
        word = words[i]
        if ENV_ASSIGN_RE.fullmatch(word) or word in WRAPPERS:
            i += 1
        elif word == "timeout":
            i += 2 if i + 1 < len(words) and words[i + 1][:1].isdigit() else 1
        else:
            break
    if i >= len(words):
        return None
    if _derive_basename(words[i]).lower().removesuffix(".exe") not in INTERPRETERS:
        return i
    j = i + 1
    while j < len(words) and words[j].startswith("-"):
        if words[j] == "-c":
            return None
        if words[j] == "-m" and j + 1 < len(words):
            return j + 1
        j += 1
    return j if j < len(words) else i


def _derive_segment(words: list) -> tuple:
    """`(class or None, destructive, verb, slug)` for one segment of a shell command, read off the
    word the segment runs and never off a word it merely names."""
    k = _derive_program(words)
    if k is None:
        return None, False, None, None
    base = _derive_basename(words[k])
    if base == DRIVER_SCRIPT:
        verb = slug = None
        for j in range(k + 1, len(words)):
            if VERB_RE.fullmatch(words[j]):
                verb = words[j]
                if j + 1 < len(words) and rl.SLUG_RE.fullmatch(words[j + 1]):
                    slug = words[j + 1]
                break
        return "driver", False, verb, slug
    if base in GIT_NAMES:
        sub, args = _derive_git_subcommand(words[k + 1:])
        return GIT_CLASSES.get(sub), _check_destructive(sub, args), None, None
    if base == BAR_SCRIPT:
        return "bar", False, None, None
    if base in TEST_NAMES or base.endswith(TEST_TAILS):
        return "test", False, None, None
    return None, False, None, None


def derive_tool_class(name, tool_input) -> tuple:
    """`(cls, flags, verb, slug)` of one tool call, decided from its input IN MEMORY.

    Nothing of the input survives but these four. A shell command naming the driver is redacted
    before its tokens are read, so a verb or slug can never carry a value the table recognises.
    """
    if name not in SHELL_TOOLS:
        return TOOL_CLASSES.get(name, "other"), (), None, None
    command = tool_input.get("command") if isinstance(tool_input, dict) else None
    if not isinstance(command, str) or not command.strip():
        return "other", (), None, None
    if DRIVER_SCRIPT in command:
        command = rl.render_redacted(command)
    found, flags = set(), set()
    verb = slug = None
    for words, sep in extract_segments(command):
        cls, destructive, v, s = _derive_segment(words)
        if cls:
            found.add(cls)
        if destructive:
            flags.add("destructive")
        if cls == "driver":
            if sep in ("|", "|&"):
                flags.add("piped")
            if verb is None:
                verb, slug = v, s
    cls = next((c for c in SHELL_PRIORITY if c in found), "other")
    if cls != "driver":
        verb = slug = None
    return cls, tuple(sorted(flags)), verb, slug


# ---------------------------------------------------------------------------------- one record

def _read_text(rec) -> str | None:
    """A user record's typed text: its string content or its text blocks joined; None for a result."""
    msg = rec.get("message")
    if not isinstance(msg, dict):
        return None
    content = msg.get("content")
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return None
    parts = []
    for block in content:
        if not isinstance(block, dict):
            continue
        if block.get("type") == "tool_result":
            return None
        if block.get("type") == "text" and isinstance(block.get("text"), str):
            parts.append(block["text"])
    return "\n".join(parts) if parts else None


def _derive_owner_class(rec, text) -> str | None:
    """`interrupt`, `human` or `candidate` for a main-file text record, before the keepalive join."""
    if text.startswith(INTERRUPT_LEAD):
        return "interrupt"
    origin = rec.get("origin")
    kind = origin.get("kind") if isinstance(origin, dict) else origin
    if kind == "human":
        return "human"
    if kind is not None:
        return None
    if rec.get("isCompactSummary") is True:
        return None
    m = LEAD_TAG_RE.match(text)
    if m and (m.group(1).startswith("local-command-") or m.group(1) == "task-notification"):
        return None
    return "candidate"


def _derive_notifications(text) -> list:
    """`(tool_use_id, status, rc)` per notification block a text carries."""
    blocks = NOTIFICATION_RE.findall(text) or [text]
    out = []
    for block in blocks:
        status = STATUS_RE.search(block)
        summary = SUMMARY_RE.search(block)
        codes = EXIT_CODE_RE.findall(summary.group(1)) if summary else []
        rc = int(codes[-1]) if codes else None
        for tid in TOOL_USE_ID_RE.findall(block):
            out.append((tid, status.group(1) if status else None, rc))
    return out


def _read_result_text(block) -> str:
    content = block.get("content")
    if isinstance(content, str):
        return content[:200]
    if isinstance(content, list):
        for item in content:
            if isinstance(item, dict) and isinstance(item.get("text"), str):
                return item["text"][:200]
    return ""


def _scan_assistant(rec, src, t, key, items, usage, cron_out) -> None:
    msg = rec.get("message") if isinstance(rec.get("message"), dict) else {}
    content = msg.get("content")
    if isinstance(content, list):
        for sub, block in enumerate(content):
            if not isinstance(block, dict) or block.get("type") != "tool_use":
                continue
            name = block.get("name")
            inp = block.get("input") if isinstance(block.get("input"), dict) else {}
            cls, flags, verb, slug = derive_tool_class(name, inp)
            tid = block.get("id") if isinstance(block.get("id"), str) else None
            items.append((t, key[0], key[1], sub, "use",
                          (tid, _derive_token(name) or "other", cls, flags, verb, slug, src)))
            # A keepalive fires into the MAIN file, so only a main-loop CronCreate can arm one. The
            # restriction also keeps this join and `scan_owner_turns`, which reads the main file
            # alone, from ever disagreeing about the same record.
            if name == "CronCreate" and src == "main" and isinstance(inp.get("prompt"), str):
                cron_out.append((t, key[0], key[1], sub, "cron", _derive_hash(inp["prompt"])))
    if rec.get("isApiErrorMessage") is True:
        quota = rec.get("quotaLimits")
        if isinstance(quota, dict) and quota.get("status") == "rejected":
            items.append((t, key[0], key[1], 0, "limit",
                          (src, _derive_token(quota.get("rateLimitType")),
                           _derive_int(quota.get("resetsAt")))))
        else:
            items.append((t, key[0], key[1], 0, "api_error",
                          (src, _derive_status(rec.get("apiErrorStatus")),
                           _derive_token(rec.get("error")), None)))
        return
    use = msg.get("usage")
    if isinstance(use, dict):
        rid = rec.get("requestId")
        ukey = ("r", rid) if isinstance(rid, str) and rid else (
            ("m", msg.get("id")) if isinstance(msg.get("id"), str) else ("l", key))
        vals = tuple(_derive_int(use.get(f)) or 0 for f in (
            "input_tokens", "output_tokens", "cache_read_input_tokens",
            "cache_creation_input_tokens"))
        have = usage.get(ukey)
        if have is None:
            usage[ukey] = [t, key[0], key[1], src, _derive_token(msg.get("model")), *vals]
        else:
            if t < have[0]:
                have[0] = t
            for i, v in enumerate(vals, 5):
                if v > have[i]:
                    have[i] = v


def _scan_user(rec, src, t, key, items, wf_runs) -> None:
    msg = rec.get("message") if isinstance(rec.get("message"), dict) else {}
    content = msg.get("content")
    results = [b for b in content if isinstance(b, dict) and b.get("type") == "tool_result"] \
        if isinstance(content, list) else []
    if results:
        tur = rec.get("toolUseResult")
        tur = tur if isinstance(tur, dict) else {}
        is_async = len(results) == 1 and ("backgroundTaskId" in tur or tur.get("isAsync") is True
                                           or tur.get("status") == "async_launched")
        run_id = _derive_token(tur.get("runId"))
        if run_id:
            wf_runs.add(run_id)
        denial = _derive_token(rec.get("toolDenialKind"))
        for sub, block in enumerate(results):
            lead = _read_result_text(block)
            m = RESULT_RC_RE.match(lead)
            hook = HOOK_LEAD_RE.match(lead) is not None
            items.append((t, key[0], key[1], sub, "result",
                          (block.get("tool_use_id"), block.get("is_error") is True,
                           int(m.group(1)) if m else None, is_async,
                           denial if sub == 0 else None, hook, "toolDenialKind" in rec and sub == 0,
                           src)))
        return
    text = _read_text(rec)
    if text is None:
        return
    if "<tool-use-id>" in text:
        items.append((t, key[0], key[1], 0, "notify", tuple(_derive_notifications(text))))
    if src != "main":
        return
    oclass = _derive_owner_class(rec, text)
    if oclass == "interrupt":
        items.append((t, key[0], key[1], 0, "owner", "interrupt"))
    elif oclass == "human":
        items.append((t, key[0], key[1], 0, "owner", "typed"))
    elif oclass == "candidate":
        items.append((t, key[0], key[1], 0, "text", (_derive_hash(text), rec.get("isMeta") is True)))


def _scan_record(rec, src, t, key, items, usage, wf_runs, cron) -> None:
    typ = rec.get("type")
    if typ == "assistant":
        _scan_assistant(rec, src, t, key, items, usage, cron)
    elif typ == "user":
        _scan_user(rec, src, t, key, items, wf_runs)
    elif typ == "attachment":
        att = rec.get("attachment")
        if not isinstance(att, dict) or att.get("type") != "queued_command":
            return
        prompt = att.get("prompt")
        if isinstance(prompt, str) and "<tool-use-id>" in prompt:
            items.append((t, key[0], key[1], 0, "notify", tuple(_derive_notifications(prompt))))
        origin = att.get("origin")
        if (src == "main" and att.get("commandMode") == "prompt" and isinstance(origin, dict)
                and origin.get("kind") == "human"):
            items.append((t, key[0], key[1], 0, "owner", "queued"))
    elif typ == "queue-operation":
        text = rec.get("content")
        if isinstance(text, str) and "<tool-use-id>" in text:
            items.append((t, key[0], key[1], 0, "notify", tuple(_derive_notifications(text))))
    elif typ == "system":
        subtype = rec.get("subtype")
        if subtype == "compact_boundary":
            meta = rec.get("compactMetadata") if isinstance(rec.get("compactMetadata"), dict) else {}
            items.append((t, key[0], key[1], 0, "compact",
                          (src, _derive_token(meta.get("trigger")), _derive_int(meta.get("preTokens")))))
        elif subtype == "api_error":
            err = rec.get("error")
            status = _derive_int(err.get("status")) if isinstance(err, dict) else None
            label = _derive_token(err) if isinstance(err, str) else (
                _derive_token(err.get("type")) if isinstance(err, dict) else None)
            items.append((t, key[0], key[1], 0, "api_error",
                          (src, status, label, _derive_int(rec.get("retryAttempt")))))


# ---------------------------------------------------------------------------------- one session

def _build_coverage(tree: SessionTree) -> dict:
    return {"tree": "absent" if tree.main is None else "present", "files": 0, "records": 0,
            "torn": 0, "dup_uuids": 0, "unknown_types": {}, "untimed": 0, "wf_missing": 0,
            "escaped": tree.escaped, "unreadable": 0, "copies": tree.copies}


def _build_events(items, usage, cron_items) -> list:
    """Turn the sorted compact items into events. Order-dependent joins happen HERE, after the sort."""
    events = []
    calls, pending = {}, {}
    cron = set()
    call_no = 0
    for t, _f, _l, _s, tag, p in sorted(items + cron_items, key=lambda it: it[:4]):
        if tag == "cron":
            cron.add(p)
        elif tag == "use":
            tid, name, cls, flags, verb, slug, src = p
            call_no += 1
            ev = {"t": t, "kind": "tool", "src": src, "call": call_no, "tool": name, "cls": cls,
                  "flags": list(flags), "bg": False, "end": None, "dur": None, "err": None,
                  "rc": None}
            if cls == "driver":
                ev["verb"], ev["slug"] = verb, slug
            if tid is not None and tid not in calls:
                calls[tid] = len(events)
            events.append(ev)
        elif tag == "result":
            tid, err, rc, is_async, denial, hook, denied, src = p
            idx = calls.get(tid) if isinstance(tid, str) else None
            ev = events[idx] if idx is not None else None
            if ev is not None and ev["err"] is None:
                ev["err"] = err
                if is_async:
                    ev["bg"] = True
                    pending[tid] = idx
                else:
                    ev["end"] = t
                    ev["dur"] = round(t - ev["t"], 3)
                    if ev["tool"] in SHELL_TOOLS:
                        ev["rc"] = rc if rc is not None else (None if err else 0)
            if denied or hook:
                events.append({"t": t, "kind": "denial", "src": src,
                               "call": ev["call"] if ev is not None else None, "reason": denial,
                               "hook": hook})
        elif tag == "notify":
            for tid, status, rc in p:
                idx = pending.pop(tid, None)
                if idx is None:
                    continue
                ev = events[idx]
                ev["end"] = t
                ev["dur"] = round(t - ev["t"], 3)
                events.append({"t": t, "kind": "tool_end", "src": ev["src"], "call": ev["call"],
                               "status": _derive_token(status), "rc": rc})
        elif tag == "text":
            digest, is_meta = p
            if digest in cron:
                events.append({"t": t, "kind": "keepalive"})
            elif not is_meta:
                events.append({"t": t, "kind": "owner", "via": "typed"})
        elif tag == "owner":
            events.append({"t": t, "kind": "owner", "via": p})
        elif tag == "compact":
            src, trigger, pre = p
            events.append({"t": t, "kind": "compact", "src": src, "trigger": trigger,
                           "pre_tokens": pre})
        elif tag == "api_error":
            src, status, error, retry = p
            events.append({"t": t, "kind": "api_error", "src": src, "status": status, "error": error,
                           "retry": retry})
        elif tag == "limit":
            src, ltype, resets = p
            events.append({"t": t, "kind": "limit", "src": src, "limit_type": ltype, "resets": resets})
        elif tag == "workflow":
            events.append({"t": t, "kind": "workflow", **p})
        elif tag == "agent":
            src, label, depth = p
            events.append({"t": t, "kind": "agent", "src": src, "label": label, "depth": depth})
    for t, _f, _l, src, model, tin, tout, tcr, tcw in sorted(usage.values(), key=lambda u: u[:3]):
        events.append({"t": t, "kind": "usage", "src": src, "model": model, "in": tin, "out": tout,
                       "cache_read": tcr, "cache_write": tcw})
    events.sort(key=lambda e: e["t"])
    for ev in events:
        ev["t"] = round(ev["t"], 3)
    return events


def extract_session(tree: SessionTree, attribution="given", slugs=()) -> dict:
    """One session's structural extract: the data model the kit README states. Never raises on a
    transcript's contents: a torn line, an unknown type or a missing file lands in `coverage`."""
    cov = _build_coverage(tree)
    versions: dict = {}
    items, cron_items = [], []
    usage: dict = {}
    seen: set = set()
    first_t: dict = {}
    wf_runs: set = set()
    tree_bytes = 0
    for _src, path in _build_file_list(tree):
        try:
            tree_bytes += path.stat().st_size
        except OSError:
            pass
    for src, file_no, lineno, rec in read_records(tree, cov):
        cov["records"] += 1
        uid = rec.get("uuid")
        if isinstance(uid, str):
            if uid in seen:
                cov["dup_uuids"] += 1
                continue
            seen.add(uid)
        typ = rec.get("type")
        if typ not in KNOWN_TYPES:
            name = _derive_token(typ) or "other"
            cov["unknown_types"][name] = cov["unknown_types"].get(name, 0) + 1
            continue
        version = _derive_token(rec.get("version"))
        if version:
            versions[version] = versions.get(version, 0) + 1
        if src == "main" and rec.get("isSidechain") is True:
            src = "agent"
        t = parse_time(rec.get("timestamp"))
        if t is None:
            # Scanned into throwaway lists, so a record that would have yielded an event is COUNTED
            # as untimed rather than silently dropped, and one that yields nothing is not counted.
            probe, probe_cron = [], []
            _scan_record(rec, src, 0.0, (file_no, lineno), probe, {}, set(), probe_cron)
            if probe or probe_cron:
                cov["untimed"] += 1
            continue
        if file_no > 0 and (file_no not in first_t or t < first_t[file_no]):
            first_t[file_no] = t
        _scan_record(rec, src, t, (file_no, lineno), items, usage, wf_runs, cron_items)
    files = _build_file_list(tree)
    for file_no, (src, path) in enumerate(files):
        if file_no == 0:
            continue
        if file_no not in first_t:
            cov["untimed"] += 1
            continue
        meta_path = path.with_name(path.name[:-len(".jsonl")] + ".meta.json")
        meta = (_read_json_file(meta_path, cov) if meta_path.exists() else None) or {}
        items.append((first_t[file_no], file_no, 0, 0, "agent",
                      (src, _derive_label(meta.get("agentType")), _derive_int(meta.get("spawnDepth")))))
    present = set()
    for path in tree.workflows:
        present.add(path.stem)
        flow = _read_json_file(path, cov)
        if flow is None:
            continue
        t = parse_time(flow.get("startTime"))
        if t is None:
            t = parse_time(flow.get("timestamp"))
        if t is None:
            cov["untimed"] += 1
            continue
        items.append((t, len(files), 0, 0, "workflow",
                      {"label": _derive_label(flow.get("workflowName")),
                       "status": _derive_token(flow.get("status")),
                       "dur_ms": _derive_int(flow.get("durationMs")),
                       "agents": _derive_int(flow.get("agentCount")),
                       "tool_calls": _derive_int(flow.get("totalToolCalls")),
                       "tokens": _derive_int(flow.get("totalTokens"))}))
    cov["wf_missing"] = len(wf_runs - present)
    return {"schema": SCHEMA, "sid": tree.sid, "attribution": attribution, "slugs": sorted(set(slugs)),
            "tree_bytes": tree_bytes, "engine_versions": dict(sorted(versions.items())),
            "coverage": cov, "events": _build_events(items, usage, cron_items)}


def build_usage(events) -> dict:
    """Token totals per split from a session's `usage` events: one request counts once, where it ran."""
    out = {src: {"requests": 0, "in": 0, "out": 0, "cache_read": 0, "cache_write": 0}
           for src in SOURCES}
    for ev in events:
        if ev.get("kind") != "usage" or ev.get("src") not in out:
            continue
        row = out[ev["src"]]
        row["requests"] += 1
        for f in ("in", "out", "cache_read", "cache_write"):
            row[f] += ev.get(f) or 0
    return out


def scan_owner_turns(tree: SessionTree) -> list:
    """The owner turns and keepalive fires of a session: its main file's `owner` and `keepalive` events."""
    main_only = SessionTree(sid=tree.sid, main=tree.main)
    return [ev for ev in extract_session(main_only)["events"] if ev["kind"] in ("owner", "keepalive")]


def write_session(session: dict, store) -> pathlib.Path:
    """Write one extract to `<store>/sessions/<sid>.json` through a temp file, contained under `store`."""
    sid = session.get("sid")
    if not isinstance(sid, str) or SID_RE.fullmatch(sid) is None:
        raise ValueError(f"runlog: refusing to write an extract for {str(sid)[:80]!r}, which is not a "
                         "session id")
    store = pathlib.Path(store)
    target = store / SESSIONS_DIR / f"{sid}.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    if not _check_inside(target, store.resolve()):
        raise ValueError(f"runlog: the extract for {sid} would land outside its store")
    tmp = target.with_name(f".{sid}.{os.getpid()}.tmp")
    tmp.write_bytes((json.dumps(session, separators=(",", ":"), ensure_ascii=True) + "\n")
                    .encode("ascii"))
    os.replace(tmp, target)
    return target


# ---------------------------------------------------------------------------------- attribution

def read_session_ids(slug, journal_path) -> tuple:
    """`(candidates, refused)`: every UUID-shaped `sess.*` value in `slug`'s START lines, whatever the
    variable is called, and the count of `sess.*` values refused for their shape."""
    journal = rl.read_journal(journal_path)
    found, refused = set(), 0
    for line in journal.lines:
        f = line.fields
        if f.get("ev") != "start" or f.get("slug") != slug:
            continue
        for k, v in f.items():
            if not k.startswith("sess.") or not v:
                continue
            if SID_RE.fullmatch(v):
                found.add(v)
            else:
                refused += 1
    return sorted(found), refused


def scan_preflights(projects_root, slug=None) -> list:
    """`(sid, slug)` for every local session whose main file RUNS `unattended.sh --preflight <slug>`.

    Only a shell call's input counts: a mention in a tool's output or in narration is not a run.
    The attribution is a heuristic and every consumer is told so.
    """
    root = pathlib.Path(projects_root)
    if not root.is_dir():
        return []
    inside = root.resolve()
    out = set()
    for path in sorted(root.glob("*/*.jsonl")):
        sid = path.name[:-len(".jsonl")]
        if SID_RE.fullmatch(sid) is None or not _check_inside(path, inside):
            continue
        try:
            fh = open(path, "rb")
        except OSError:
            continue
        with fh:
            for raw in fh:
                if b"--preflight" not in raw or DRIVER_SCRIPT.encode() not in raw:
                    continue
                try:
                    rec = parse_record(raw)
                except ValueError:
                    continue
                msg = rec.get("message")
                if rec.get("type") != "assistant" or not isinstance(msg, dict):
                    continue
                for block in msg.get("content") or ():
                    if not isinstance(block, dict) or block.get("type") != "tool_use":
                        continue
                    cls, _flags, verb, found = derive_tool_class(block.get("name"), block.get("input"))
                    if cls == "driver" and verb == "--preflight" and found and (
                            slug is None or found == slug):
                        out.add((sid, found))
    return sorted(out)


# ---------------------------------------------------------------------------------- narration

def extract_narration(tree: SessionTree, t_from: float, t_to: float) -> list:
    """`(t, who, text)` for the agent's own text blocks and the owner's turns inside `[t_from, t_to]`,
    main file only, EVERY text passed through the redaction table. Nothing here is written anywhere.

    `who` is `agent` or `owner`. A keepalive fire is neither and is left out, by the same join the
    extract uses — an EARLIER CronCreate in this file with the same prompt; thinking blocks, tool
    calls and tool output are never read as text.
    """
    if tree.main is None:
        return []
    cron: dict = {}
    found, seen = [], set()
    for _src, _no, lineno, rec in read_records(SessionTree(sid=tree.sid, main=tree.main)):
        uid = rec.get("uuid")
        if isinstance(uid, str):
            if uid in seen:
                continue
            seen.add(uid)
        if rec.get("isSidechain") is True:
            continue
        typ = rec.get("type")
        msg = rec.get("message") if isinstance(rec.get("message"), dict) else {}
        t = parse_time(rec.get("timestamp"))
        if typ == "assistant":
            for block in msg.get("content") or ():
                if not isinstance(block, dict):
                    continue
                if block.get("type") == "tool_use" and block.get("name") == "CronCreate":
                    inp = block.get("input") if isinstance(block.get("input"), dict) else {}
                    if isinstance(inp.get("prompt"), str) and t is not None:
                        digest = _derive_hash(inp["prompt"])
                        cron[digest] = min(cron.get(digest, (t, lineno)), (t, lineno))
                elif (block.get("type") == "text" and isinstance(block.get("text"), str)
                      and t is not None and t_from <= t <= t_to):
                    found.append((t, lineno, "agent", block["text"], None))
        elif typ == "user" and t is not None and t_from <= t <= t_to:
            text = _read_text(rec)
            if text is None:
                continue
            oclass = _derive_owner_class(rec, text)
            if oclass in ("interrupt", "human"):
                found.append((t, lineno, "owner", text, None))
            elif oclass == "candidate":
                found.append((t, lineno, "owner", text, (_derive_hash(text), rec.get("isMeta") is True)))
        elif typ == "attachment" and t is not None and t_from <= t <= t_to:
            att = rec.get("attachment")
            origin = att.get("origin") if isinstance(att, dict) else None
            if (isinstance(att, dict) and att.get("type") == "queued_command"
                    and att.get("commandMode") == "prompt" and isinstance(origin, dict)
                    and origin.get("kind") == "human" and isinstance(att.get("prompt"), str)):
                found.append((t, lineno, "owner", att["prompt"], None))
    out = []
    for t, lineno, who, text, join in sorted(found, key=lambda f: f[:2]):
        if join is not None and (join[1] or cron.get(join[0], (t, lineno)) < (t, lineno)):
            continue
        out.append((t, who, rl.render_redacted(text)))
    return out


# ---------------------------------------------------------------------------------- measurement

def _read_peak_bytes() -> int | None:
    """This process's peak working set in bytes, or None where the platform gives no reading."""
    if sys.platform.startswith("win"):
        try:
            import ctypes
            from ctypes import wintypes

            class ProcessMemoryCounters(ctypes.Structure):
                _fields_ = [("cb", wintypes.DWORD), ("PageFaultCount", wintypes.DWORD),
                            ("PeakWorkingSetSize", ctypes.c_size_t),
                            ("WorkingSetSize", ctypes.c_size_t),
                            ("QuotaPeakPagedPoolUsage", ctypes.c_size_t),
                            ("QuotaPagedPoolUsage", ctypes.c_size_t),
                            ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t),
                            ("QuotaNonPagedPoolUsage", ctypes.c_size_t),
                            ("PagefileUsage", ctypes.c_size_t), ("PeakPagefileUsage", ctypes.c_size_t)]

            counters = ProcessMemoryCounters()
            counters.cb = ctypes.sizeof(counters)
            kernel = ctypes.WinDLL("kernel32")
            kernel.GetCurrentProcess.restype = wintypes.HANDLE
            psapi = ctypes.WinDLL("psapi")
            psapi.GetProcessMemoryInfo.argtypes = [wintypes.HANDLE, ctypes.c_void_p, wintypes.DWORD]
            if psapi.GetProcessMemoryInfo(kernel.GetCurrentProcess(), ctypes.byref(counters),
                                          counters.cb):
                return int(counters.PeakWorkingSetSize)
        except (OSError, AttributeError):
            return None
        return None
    try:
        import resource
    except ImportError:
        return None
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(peak) if sys.platform == "darwin" else int(peak) * 1024


def measure_tree(root) -> dict:
    """Stream every session under a projects root through the extractor and REPORT: bytes, records,
    events, the rate and this process's peak working set. Writes nothing and grades nothing."""
    root = pathlib.Path(root)
    mains = sorted(p for p in root.glob("*/*.jsonl") if SID_RE.fullmatch(p.name[:-len(".jsonl")]))
    sessions = records = events = size = 0
    t0 = time.perf_counter()
    for main in mains:
        tree = build_session_tree(main)
        session = extract_session(tree)
        sessions += 1
        size += session["tree_bytes"]
        records += session["coverage"]["records"]
        events += len(session["events"])
    wall = time.perf_counter() - t0
    peak = _read_peak_bytes()
    return {"sessions": sessions, "bytes": size, "records": records, "events": events,
            "seconds": round(wall, 3), "rate_mb_s": round(size / 1e6 / wall, 2) if wall > 0 else None,
            "peak_mb": round(peak / 1e6, 1) if peak else None}
