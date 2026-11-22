#!/usr/bin/env python3
"""handoff.py — a role and one task's inputs, rendered into one hashed prompt file (TOOL-aOrientedCast-2).

    python handoff.py render --role <name> --build <slug> [--unit <id>] [--item <tag> [--allowance <path>]...]
                             [--card <path>]
                             [--input <key>=<value>]... [--upstream <rows file>]
                             [--out <path> | --stdout | --stand-in]
                             [--part full|task]
    python handoff.py facts --build <slug> [--unit <id>] --input <key>=<value>...
    python handoff.py harness-args <harness>
    python handoff.py stage-efforts <workflow> [--model <id>]
    python handoff.py role-efforts [--model <id>]
    python handoff.py check <file>
    python handoff.py roster
    python handoff.py agents (--handoff <path> | --run <run-id>) [--session <file>] [--write]

`render` fills the work-order template, `templates/work-order.template.md` in this kit, whose slots are
`role`, `roles_lib.render_role`'s output, closing with the role's `## Never`, `## Ceiling` and `## Return`
sections, the ceiling's gate legs the merged grant, the role's `gates` field else the house file's
`[gates]` row (TOOL-dBoundRoles-2 S6, TOOL-dBoundRoles-21 S6), then a `### Drive` block holding the charter's drive lines for the
role where it has any (PLAY-dOrderedCharter-6); `opening`; `reads`, a block per input the role's `reads`
declares, in that order, then the optional `input:code` every role carries (PLAY-dOrderedCharter-27): the
text of the file `--input code=` names, measured against `memory.code-budget` by the load-set check; and
`practices`, a `### Practices at <step>` block
of one `- [<name>] <reach>` line per active practice reaching the step its workflow row names, the lines the
load-set check's run prints under `--reach` (PLAY-dOrderedCharter-21). A slot with nothing to fill leaves no line.
The charter's blocks ride once, in the role's agent file, never in the prompt; the render still grades the
role's `rules` tags, each library note printed on stderr as `handoff: note — ` (PLAY-dOrderedCharter-5 S3).
THE SINGLE CARRY (TOOL-dBoundRoles-15): the policy key `instructions.task-charter` selects whether a task
carries the charter blocks, read once per render through `roles_lib.read_policy_setting` and checked by
`roles_lib.check_single_carry` before any file is written. The harness kind is `static` where a file the
backend loads carries the charter at spawn, the agent file for a spawned type and the charter file for a
`--stand-in` or an `agent: false` render, which the main loop does; `inline` is a backend loading neither,
and only an `inline` task carries the blocks. Every route of today's one adapter is `static`, so
`when-not-static`, the default, puts no charter in any task, and `always` refuses with exit 1, naming the
key, the role and the file that carries its charter, since the charter would reach it twice. With no
policy kit the render prints one `instructions.task-charter unread` note and takes `when-not-static`.
Where the playbook kit's document registry reads, each block sits in the envelope of its level
(PLAY-dOrderedCharter-5 S2), opened under its section's heading: the `## Role` body in the agent file's row,
level 5; first under `## Task` the practices block at level 0, doc `<charter>#practices-at-<step>` and the
charter row's direction; then the rest of the task at level 6, doc the prompt file's path. With no playbook
kit it renders unranked and prints one `envelope — unarmed` note; a registry that does not read refuses.
It writes the file under the build's `prompts/` folder, printing its repo-relative path. `--part task` prints
the marker line, a blank line and the `## Task` section instead; `--stdout` writes nothing and prints.
Outside `--stand-in` it prints one stderr line after the notes, `handoff: description — <name>`, the
spawn's name `<build> · <unit> · <workflow>`, the unit part left out with no `--unit`: the `Agent`
call passes it as `description`, and the hooks kit's spawn guard derives the same name and refuses
any other (TOOL-aOrientedCast-27). stdout is unchanged by it in every mode.
`--stand-in` declares that the main loop does the role's work itself, because its tool cannot spawn
a sub-agent (TOOL-aOrientedCast-19): it refuses with exit 1, writing nothing, unless a valid row of
the owner's `<MEMORY_ROOT>/project/role-stand-in-waiver.txt` names the role and the build, and
otherwise writes the derived name with a `-stand-in` tail before `.md`, which the catalogue
checker's R15 joins with that row. It does not check that the tool truly cannot spawn, nor relax
any hook or gate.
The marker is `<!-- gov:handoff role=<slot> build=<slug> unit=<id|-> item=<tag|-> path=<rel> role-sha=<12hex>
task-sha=<12hex> -->` (TOOL-dBoundRoles-17 S1): `item=` names the item the work order was cut for, `--item`'s
tag in the `item.<step>.<name>` shape or `-` without it, a malformed tag refused with exit 1 writing nothing;
the shape is checked first. A marker written before `item=` still parses, every reader taking its fields
by group name.
THE WORK ORDER PER ITEM (TOOL-dBoundRoles-3): with `--item`, the render reads the item's declaration from the
loop kit, its `loop_lib.py declaration --item <tag> --json` run in a subprocess under a bound, the kit found
by `resolve_kit_dir`, and refuses with exit 1, writing nothing, an item the loop does not declare, one whose
actor is not `role:<the --role slot>`, and no loop kit. The task then closes, after the `reads` blocks, with
five blocks, `roles_lib.WORK_ORDER_BLOCKS`: `### item`, the tag, its step and its outcome set; `### inputs`,
each of the item's inputs handed as content under its own `### <field tag>` heading, its fact line two below
and its content fenced after it, an optional one the render cannot resolve named on the `Not supplied` line; `### allowance`, the path
prefixes `roles_lib.derive_allowance` gives the item's write class: none, the build's `spec/` or `reviews/`
folder, the memory root, or for a `product` item each path `--allowance` grants, which must sit under a
`ROUTED_PATHS` entry, a `product` item granted none refused, so pass the unit's `--dispatch --writes` set and
never the whole of `ROUTED_PATHS`; `### return`, the item's resolved return; and `### witness`, its witness
class and `by`. All five sit inside `## Task`, so `task-sha` covers them. `--allowance` without `--item`
refuses. The hooks kit's spawn guard admits such a work order only in a session whose card routes its unit.
A research return names the work order it answers on a `**Answers:** <path> task-sha=<12hex>` line,
`roles_lib.derive_answers_value`'s value, which the catalogue checker's R16 grades.
The marker carries two hashes, each the first 12 hex digits of the SHA-256 of one section's bytes
with CRLF folded to LF: `## Role` up to the byte before the `## Task` line, and `## Task` to the end
of the file. `check` re-derives both and compares the marker's `path` with the file's own, and for a
marker whose `item=` is a tag refuses a task missing any of the five blocks, naming it; then every
envelope opened must close, and the levels must never decrease down each part, `## Role` and `## Task`,
each failure naming the envelope; it prints each part's levels in order, or `unranked` for a file holding
no envelope, which passes (PLAY-dOrderedCharter-5 S4).
`harness-args` prints, as one line of sorted JSON, the union of the stage maps, `key → role` of each
`[[workflow.stages]]` row, of every workflow whose harness names that script. `stage-efforts`
prints, the same way, the reasoning effort resolved for every stage row of ONE workflow: a harness
call passes it as its `efforts` argument (TOOL-aOrientedCast-10). The order is TOOL-dBoundRoles-21's
with TOOL-dBoundRoles-22's step: the policy keys `roles.effort.<workflow>.<stage>`,
`roles.effort.<role>` and `roles.effort.default` of the working directory's repository, then
`house/policy.toml` where present, then the stage row's `effort`, then the role's declared `effort`.
`role-efforts` prints, the same way,
the level of every role whose `agent` is true, and a direct spawn passes its role's value. With
`--model <id>` the two verbs resolve the levels the policy's profiles give that model id; without
the flag, or for an id no profile matches, they resolve the default tables, so `stage-efforts`
with no flag prints what it printed before the flag existed, and each `role-efforts` value is that
role's rendered `effort:` line (TOOL-aProfiledEffort-2). `roster` prints the charter's roles
section, one line per role, ``- `<slot>`: <description> <when>. Output: <output>.``, where `<when>`
is `Optional` for a `mandatory` of `no`, `Optional, <text>` for `no — <text>`, else `Mandatory
<value>`, `{{MEMORY_ROOT}}` is the conf's value, and the order is the workflow table's; a line past
200 characters, a missing key or an empty catalogue refuses with nothing printed. It reads no
charter (TOOL-aOrientedCast-17).

`agents` prints the governing doc's `agent` line for each agent its selector names, then its
`returned` line once it has returned, each shape read from the doc's micro-format fence and filled
by placeholder name from the session's own records and the role index; a field
nothing answers prints `unknown` (TOOL-aOrientedCast-20). `--handoff` names a direct spawn, every
`Agent` call whose prompt opens with the file's marker line as the hooks kit's spawn guard reads it,
through `roles_lib.extract_prompt_marker` (TOOL-aOrientedCast-25); `--run` a harness run, one agent
per `started` entry of its journal. The session is `--session`, else the transcript
CLAUDE_CODE_SESSION_ID names. A harness agent's unit is the one unit id its journal label names, else
the label (TOOL-aOrientedCast-27). With `--write`, each line holding no `unknown` is added, once, to the
build's one `<MEMORY_ROOT>/builds/<build>/build/*-agent-ledger.md`, its prompt link re-rooted at
that folder; without it nothing is written and one note names the held lines and `--write`, so a
mid-pass call leaves the tree as it found it. Pass `--write` only at a bookkeeping step, when no
pass is running. The session's parsed calls are kept in one record per session file under
`<git-common-dir>/handoff-calls/`, keyed by this file's sha256, the file's resolved path and the
sha256 of the bytes it consumed, so a later call parses only the lines appended since; any other
record is a miss and a read from byte 0, and deleting the folder clears it (TOOL-aTrimmedWait-7).

Sources, by key family: `task:` the card's `## task` field, read by the kickoff checker's grammar
(stated above its `check_card_task`, and ported here because that one is shell) under the labels
that checker's `--task-skeleton` prints, so a skeleton that does not yield eight refuses; `card:` the lines
under the card's last `## <heading>`; `brief:` the `### <sub-head>` under the brief record's
`## The brief`, and `brief:prompt` that record's `## The prompt` section; `input:` the `--input`
argument; `upstream:rows` the rows file `--upstream` names, the loop kit's `upstream.py rows` output,
then `UPSTREAM_CONTRACT`, the line every row id is answered by, an empty file supplying nothing
(TOOL-dDeclaredLoop-29); a rule tag the governing doc's practices. The card is `--card`, else the file the
kickoff checker's `--card --path` prints for CLAUDE_CODE_SESSION_ID, so the card's location stays
that checker's rule. A required key resolving to nothing, an empty value or a placeholder refuses
and writes nothing; an optional one is named on the `Not supplied` line. A relative path
given to `--card`, `--out`, an `--input`, `--upstream` or `check` is read from the repository root.

Every value is handed as content (TOOL-dBoundRoles-13): its block opens with a fact line,
`<!-- gov:fact key=<key> class=<class> -->`, `roles_lib.FACT_RE`'s grammar, then the content inside a fence of
backticks one longer than its longest backtick run and at least three, `roles_lib.render_handed_fence`'s, so a
fact or marker line the content quotes is content to every reader, each of which walks
`roles_lib.read_unfenced_lines` (TOOL-dBoundRoles-38); a task section that ends inside a fence refuses,
naming the block and the line, and writes nothing. A typed input, `TYPED_INPUTS`, is authored text and
is written unfenced: a line of it that reads as a heading, a fact line, a marker line or a `Framed by:`
line, or a fence it never closes, refuses naming `input:<name>` and the line (TOOL-dBoundRoles-45). The key is
`roles_lib.derive_fact_key`'s: `record:<path>@<sha12>` for `input:spec`, `input:prompt`, a brief value and the
`upstream:rows` file, `record:card/<session id>` for a card value (a `--card` inside the repository keys by
its own path, else `card/<stem>`), `blob:<path>@<blob12>:1-<n>` for `input:code`, and `cmd:<argv12>:<out12>`
over the fixed argv `--input`, NUL, `<name>` for a typed argument; the class is `roles_lib.derive_fact_class`'s,
so no agent types one. The hooks kit's spawn guard re-derives each `blob:` and `record:` key at the spawn and
refuses a moved one. `facts` prints, as one line of JSON, the list `[{name, key, class, text}]` of each
`--input` as `render` hands it, refusing as it refuses; a caller that cannot spawn through the guard, the
unit harness's caller, passes it on.

Exit 0 on success, 1 on a refusal naming its key, file, role or missing waiver row, 2 on usage or an unarmed
environment: no repository, no MEMORY_ROOT, no CHARTER (`roster` and `facts` need none). `agents` exits 1
on no marker in the handoff, no matching call, no run journal, a missing shape, an underived
placeholder or two ledgers in one build, and 2 with no session file or role index as well.

WHAT THIS DOES NOT CHECK: whether a card or brief value says anything true, since a value present,
single and not a placeholder is copied verbatim; whether a rendered role is current against the
catalogue, since `check` hashes the file's own bytes and nothing more; and whether a secret sits in
a card or a brief, which the charter's `[security]` rule guards and this script does not. For
`agents`: the transcript format is no contract, so a renamed field reads as `unknown`; an `effort`
or a `model` is what the transcript records, not proved to be what the API applied; an effort no
transcript record carries prints `unknown`, never the agent type's `effort:` line, which is the
default tables' level and not the level a profile dispatched (TOOL-aProfiledEffort-4); a file written
through Bash is not counted as written; the session read may not be the one the build ran in; and
a ledger line edited by hand passes, since nothing re-derives the ledger; a `handoff-calls` record
forged with a matching prefix and parser hash is trusted as the transcript's own lines are, and a
transcript rewritten so its consumed bytes keep their sha256 resumes from the stale record.
For `--model`: the id is not checked to be the model the session or the spawned agent runs, since
the caller types it, and an id no profile matches answers the default levels with no note. For
`--allowance`: that a granted path exists or is the unit's dispatched write set, since the caller passes it,
so a caller granting a whole `ROUTED_PATHS` entry is admitted.
"""
import argparse
import datetime
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys

KIT_DIR = pathlib.Path(__file__).absolute().parent
sys.path.insert(0, str(KIT_DIR))
import roles_lib as lib  # noqa: E402  (the kit's own library, beside this file)

#: The build's interface 6: the `task:` field keys, in order. Their card labels are NOT typed here:
#: each render reads them off the kickoff checker's `--task-skeleton` and zips them with these
#: (TOOL-aOrientedCast-15 S3), so the checker that grades a card is the one source of its labels.
TASK_FIELDS = ("title", "goal", "in", "out", "todo", "reuse", "acceptance", "gates")
#: The typed names are the library's `ARGUMENT_INPUTS`, which `derive_fact_class` reads (TOOL-dBoundRoles-13).
INPUT_NAMES = ("spec",) + lib.ARGUMENT_INPUTS + ("prompt", "code")
PATH_INPUTS = ("spec", "prompt", "code")
#: The typed inputs (TOOL-dBoundRoles-45 S1): the names whose value is the caller's argument, derived from the two
#: constants above and never typed a third time. Each is authored text, written unfenced under the
#: authored-line rule, `lib.check_authored_lines`.
TYPED_INPUTS = tuple(n for n in INPUT_NAMES if n not in PATH_INPUTS)
#: Every role's `code` slot (PLAY-dOrderedCharter-27): derived for each role, never written into its `reads`,
#: so its key is read as optional and the CLI admits it for any role; its block holds the file's text.
CODE_INPUT = "code"
#: The `upstream:rows` key (TOOL-dDeclaredLoop-29): its block is the rows file `--upstream` names, then this
#: contract, so the return answers exactly the ids the block lists.
UPSTREAM_KEY = "upstream:rows"
UPSTREAM_CONTRACT = ("Answer every row id above exactly once, in a `## Upstream` section of your return, one line "
                     "per row: `- <row id> · used|bypassed|not-applicable · <reason>`, a reason on every line, "
                     "and no row id this block does not list. `used` means your work honours the row, "
                     "`bypassed` that it departs from it, and `not-applicable` that the row does not bear on it.")
PLACEHOLDERS =("…", "...", "tbd", "todo", "n/a", "none", "-", "?")
KICKOFF_HOME, KICKOFF_CHECKER = "session-kickoff", "manifest-check.sh"
CHECKER_BOUND_S = 30
#: The bound on the loop kit's `declaration` verb, which reads the loop definition and the role catalogue.
DECLARATION_BOUND_S = 60
SLUG_RE = lib.SLUG_RE
UNIT_RE = re.compile(r"^[A-Z]+-([A-Za-z]+)-[0-9]+$")
READY_RE = re.compile(r"^(- )?READY — ")
BLANK_EDGES_RE = re.compile(r"\A\s*\n|\n\s*\Z")
WORK_ORDER = KIT_DIR / lib.WORK_ORDER_REL
MARKER_RE = lib.MARKER_RE
ROLE_HEAD_RE, TASK_HEAD_RE = re.compile(r"^## Role$", re.M), re.compile(r"^## Task$", re.M)
PROMPT_HEAD_RE = re.compile(r"^## The prompt[ \t]*$", re.M)
BRIEF_HEAD_RE = re.compile(r"^## The brief[ \t]*$", re.M)
# ponytail: the playbook's one-line region refuses a rendered rule past 200 characters; spelled
# again because a kit file may not import a sibling kit. A drift fails closed either way.
ROSTER_LINE_MAX = 200
#: `load_sets.py check --reach`'s line opening, one per reach unit, then `role.<name> · <tag> · <reach>`.
REACH_LINE = "load-set — reach · "
#: The note a render prints where no policy kit answers `instructions.task-charter` (TOOL-dBoundRoles-15 §8 F2).
TASK_CHARTER_NOTE = "instructions.task-charter unread: no policy kit; the single carry takes when-not-static"
#: The ranked handoff (PLAY-dOrderedCharter-5 S2): the practices block's envelope doc, which leads the task
#: part at level 0 as `lib.WORK_ORDER_LEAD_SLOTS` names it, and the task's own level and direction.
PRACTICES_DOC = "%s#practices-at-%s"
TASK_LEVEL = 6
TASK_DIRECTION = "The task: this unit's goal, scope and acceptance; yields to levels 0 to 5"
#: PLAY-dOrderedCharter-8 S7: the card file the kickoff checker renders into each session tree, at level 1
CARD_FILE_REL = ".claude/orientation-card.md"
#: `agents` (TOOL-aOrientedCast-20): the ledger's file-name tail, the value of a field nothing
#: answers, and the tool uses whose paths a `returned` line counts as written.
LEDGER_TAIL = "-agent-ledger.md"
UNKNOWN = "unknown"
WRITE_TOOLS = ("Write", "Edit", "MultiEdit", "NotebookEdit")
SESSION_ID_RE = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
#: A run id or an agent id reaches a path only in this shape.
PATH_ID_RE = re.compile(r"^[A-Za-z0-9_-]{1,64}$")
LABEL_UNIT_RE = re.compile(r"[A-Z]+-[A-Za-z]+-[0-9]+")
SHAPE_FIELD_RE = re.compile(r"<([^<>]+)>")
NOTIFICATION_RE = re.compile(r"<task-notification>(.*?)</task-notification>", re.S)
#: The session file's lines worth parsing: every other line is skipped unparsed, by its bytes.
SESSION_LINE_TOKENS = (b'"Agent"', b'"Workflow"', b"toolUseResult", b"task-notification")
#: TOOL-aTrimmedWait-7: the folder under the git common dir holding one parsed-calls record per
#: session file, and the record's keys, every one checked by read_session_record before use.
SESSION_CACHE_DIR = "handoff-calls"
SESSION_RECORD_KEYS = frozenset(("parser", "session", "offset", "prefix", "calls", "notified", "bad"))


def read_git_stdout(repo: pathlib.Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, text=True, encoding="utf-8", check=True
    ).stdout


git = read_git_stdout  # the name the inlined common_git_dir block calls


# >>> common_git_dir -- canonical copy: common_dir.py in the gov lib dir (byte-identical; gated)
def common_git_dir(repo: pathlib.Path) -> pathlib.Path:
    """The MAIN repository's git directory, shared by every worktree.

    ``--git-dir`` in a linked worktree is ``.git/worktrees/<name>``, which ``git worktree remove``
    deletes outright -- taking the query log with it. It is also RELATIVE (bare ``.git``) when run
    at the repo root and absolute elsewhere, so the raw value is not a usable path either way.
    """
    raw = git(repo, "rev-parse", "--git-common-dir").strip()
    p = pathlib.Path(raw)
    return p.resolve() if p.is_absolute() else (repo / raw).resolve()
# <<< common_git_dir


def check_placeholder(value):
    """True when a value is empty or a placeholder by the kickoff grammar: whitespace collapsed, one of
    … ... tbd todo n/a none - ? in any case, only `.` and `…`, or one `<slot>` with no inner bracket."""
    v = " ".join(value.split())
    return (v.lower() in PLACEHOLDERS or not v.replace(".", "").replace("…", "")
            or re.fullmatch(r"<[^<>]*>", v) is not None)


def render_spawn_name(slug, unit, workflow):
    """A direct spawn's name, `<build> · <unit> · <workflow>`, the unit part left out for no unit or
    `-` (TOOL-aOrientedCast-27). The hooks kit's spawn guard derives the same string from the marker
    and the role index, its own copy because a kit file imports no sibling kit."""
    return " · ".join(p for p in (slug, "" if unit in (None, "-") else unit, workflow) if p)


def extract_label_unit(label):
    """The one distinct unit id a harness agent's label names, else None: a spec writer serving a
    group names several and so no one unit (TOOL-aOrientedCast-27)."""
    hits = set(LABEL_UNIT_RE.findall(label or ""))
    return hits.pop() if len(hits) == 1 else None


def extract_card_section(text, heading):
    """The lines under the card's LAST `## <heading>`, up to the next `## ` heading or READY line,
    verbatim with blank edges trimmed; None when the card has no such heading. It also reads a
    brief record's `## The prompt` (TOOL-dPavedRoad-3)."""
    found = cur = None
    for line in text.split("\n"):
        if line.rstrip() == "## " + heading:
            found = cur = []
        elif cur is not None and (line.startswith("## ") or READY_RE.match(line)):
            cur = None
        elif cur is not None:
            cur.append(line)
    return None if found is None else BLANK_EDGES_RE.sub("", "\n".join(found))


def extract_task_fields(text, labels):
    """`{field: value}` for each field of `labels`, a `{card label: field}` map, that the card's
    `## task` carries exactly once. `labels` None keys each field by its own label, in the order the
    section first names it: how `render_handoff` reads the label set off `--task-skeleton`.

    The kickoff checker's grammar: a line loses its leading whitespace, its `>` run and one `- ` or
    `* `; a line then opening `<!--` or `UNVERIFIED — ` is skipped; a line opening `**` is a field
    whose label runs to the first `:**` when that precedes the first closing `**`, else to that
    `**`, and its value is the rest plus each line up to the next field line. The value keeps its
    line breaks; it is trimmed and loses one leading balanced `(…)` qualifier and one leading `:`.
    A field absent or repeated is left out; emptiness and placeholders are the caller's verdict.
    """
    section = extract_card_section(text, "task")
    raw, count, cur = {}, {}, None
    for line in (section or "").split("\n"):
        s = re.sub(r"^[-*] ", "", re.sub(r"^(> ?)+", "", line.lstrip()))
        if s.startswith(("<!--", "UNVERIFIED — ")):
            continue
        rest, b = s[2:], s[2:].find("**")
        if s.startswith("**") and b >= 0:
            k = rest.find(":**")
            label, tail = (rest[:k], rest[k + 3:]) if 0 <= k < b else (rest[:b], rest[b + 2:])
            cur = label.strip() if labels is None else labels.get(label.strip())
            if cur:
                count[cur] = count.get(cur, 0) + 1
                raw.setdefault(cur, tail)
        elif cur and count[cur] == 1:
            raw[cur] += "\n" + s
    fields = {}
    for field, v in raw.items():
        if count[field] != 1:
            continue
        v, depth = v.strip(), 0
        if v.startswith("("):
            for i, ch in enumerate(v):
                depth += (ch == "(") - (ch == ")")
                if ch == ")" and depth == 0:
                    v = v[i + 1:]
                    break
        v = v.strip()
        fields[field] = (v[1:] if v.startswith(":") else v).strip()
    return fields


def extract_brief_section(text, sub_head):
    """The first `### <sub-head>` under the record's `## The brief`, matched ignoring case, up to the
    next `###` or `##` heading, verbatim with blank edges trimmed; None when it is absent."""
    in_brief, found, cur = False, None, None
    for line in text.split("\n"):
        if line.startswith("## "):
            in_brief, cur = line.rstrip() == "## The brief", None
        elif line.startswith("### "):
            cur = [] if in_brief and found is None and line[4:].strip().lower() == sub_head else None
            found = cur if cur is not None else found
        elif cur is not None:
            cur.append(line)
    return None if found is None else BLANK_EDGES_RE.sub("", "\n".join(found))


# >>> resolve_bash_py -- canonical copy: resolve_bash.py in the gov lib dir (byte-identical; gated)
BASH_NAMES = ("bash.exe", "bash")


def wrong_shell_at(path, wsl):
    """True when `path` is a Windows checkout under WSL: `wsl` set and `path` under a single-letter
    `/mnt/<drive>/`, WSL's mount of a Windows drive (TOOL-dWitnessedBar-27). The twin of the shell
    block `refuse_wrong_shell`'s `wrong_shell_at` in `refuse-wrong-shell.sh` in the gov lib dir; a
    WSL path on its own disk, and any path where no WSL marker is set, is green."""
    p = str(path)
    return bool(wsl) and len(p) > 6 and p.startswith("/mnt/") and "a" <= p[5] <= "z" and p[6] == "/"


def scan_bash(script="", host=""):
    r"""`(found, tried, refusal)`: the bash to run, found by RUNNING each candidate, never by its name.

    GOV_BASH first, and when it is set nothing after it is tried; then Git's own `bin/bash.exe`, the
    third parent of `git --exec-path`; then each PATH directory's BASH_NAMES, a System32 or
    WindowsApps launcher reported and never run. A candidate passes when one run prints `uname -s` as
    its first line and exits 0, `test -f` on `script` included when one is given; on a `windows` host
    the answer must start MINGW or MSYS, so WSL's launcher, which answers `Linux` and drops `$1`, is
    refused under any name (gotcha subprocess-resolves-a-different-shell). Past GOV_BASH every
    candidate is run, `tried` holding one `<candidate>: <why>` for each and a repeat never twice;
    `found` is the first that passed, or "" with `refusal` naming every `tried` line, and the bare name
    `bash` is never returned. `host` is `windows` or `posix`, this host's when empty. No memo: an
    adapter keeps its own, so this stays a function a truth table can call twice. On a `posix` host
    the hosting file is judged first: WSL running it from a Windows checkout under `/mnt/` returns
    no `found`, an empty `tried` and the wrong-shell refusal, before any candidate is tried."""
    host = host or ("windows" if os.name == "nt" else "posix")
    if host == "posix":
        here = os.path.abspath(__file__)
        wsl = bool(os.environ.get("WSL_DISTRO_NAME")) or os.path.exists("/proc/sys/fs/binfmt_misc/WSLInterop")
        if wrong_shell_at(here, wsl):
            return "", [], ("WSL is running " + here + " from a Windows checkout under /mnt/; "
                            "run it with Git's bash (C:/Program Files/Git/bin/bash.exe)")
    tried, seen = [], set()

    def run_probe(cand):
        try:
            r = subprocess.run([cand, "-c", 'uname -s && { [ -z "$1" ] || test -f "$1"; }', "_", str(script)],
                               stdin=subprocess.DEVNULL, capture_output=True, timeout=20)
        except (OSError, subprocess.SubprocessError):
            return "did not run"
        u = r.stdout.decode("utf-8", "replace").replace("\x00", "").split("\n")[0].strip()
        if not u:
            return "did not run"
        if host == "windows" and not u.startswith(("MINGW", "MSYS")):
            return "answered " + u
        return "runs" if r.returncode == 0 else "cannot see " + str(script)

    def check_candidate(cand):
        key = cand.lower() if host == "windows" else cand
        if key in seen:
            return False
        seen.add(key)
        low = cand.lower()
        why = "a launcher" if "/system32/" in low or "/windowsapps/" in low else run_probe(cand)
        tried.append(cand + ": " + why)
        return why == "runs"

    gov = os.environ.get("GOV_BASH", "")
    if gov:
        why = run_probe(gov)
        tried.append(gov + ": " + why)
        if why == "runs":
            return gov, tried, ""
        return "", tried, ("GOV_BASH is set to '" + gov + "' and " + why + ", so nothing after it is tried: "
                           "an override that is set and unusable is refused, never a fall-through")
    try:
        r = subprocess.run(["git", "--exec-path"], stdin=subprocess.DEVNULL, capture_output=True, timeout=20)
        ex = r.stdout.decode("utf-8", "replace").strip().replace("\\", "/") if r.returncode == 0 else ""
    except (OSError, subprocess.SubprocessError):
        ex = ""
    found = ""
    if not ex:
        tried.append("git --exec-path: did not run")
    else:
        cand = "/".join(ex.rstrip("/").split("/")[:-3]) + "/bin/bash.exe"
        if not os.path.isfile(cand):
            tried.append(cand + ": absent")
        elif check_candidate(cand):
            found = cand
    for d in os.environ.get("PATH", "").split(os.pathsep):
        for name in BASH_NAMES:
            cand = (d.rstrip("/\\") + "/" + name).replace("\\", "/")
            if d and os.path.isfile(cand) and check_candidate(cand):
                found = found or cand
    if found:
        return found, tried, ""
    return "", tried, ("no bash runs" + (" that can see " + str(script) if script else "") + ": "
                       + "; ".join(tried) + "; set GOV_BASH to Git's bash")
# <<< resolve_bash_py


def resolve_bash():
    """The bash the one `resolve_bash_py` block above finds, GOV_BASH first and each candidate RUN, a
    System32 or WindowsApps launcher refused (the different-shell gotcha class); None when none is
    found, which leaves the card absent and named."""
    return scan_bash()[0] or None


def resolve_kickoff_checker(root):
    """The kickoff checker: through the inline kit resolver from this tool root, else the ONE file of
    that name the repository tracks — gov homes that kit under `skills/`, which no probe walks to,
    and keeps no receipt. None when neither answers, or the index names two."""
    try:
        return lib.resolve_kit_dir(KICKOFF_HOME, KICKOFF_CHECKER, KIT_DIR.parent) / KICKOFF_CHECKER
    except LookupError:
        pass
    r = subprocess.run(["git", "-C", str(root), "ls-files", "--", KICKOFF_CHECKER, "*/" + KICKOFF_CHECKER],
                       capture_output=True, encoding="utf-8")
    hits = [ln for ln in r.stdout.splitlines() if ln.strip()] if r.returncode == 0 else []
    return root / hits[0] if len(hits) == 1 and (root / hits[0]).is_file() else None


def resolve_card_path(root, card_arg):
    """`(path, why)`: the card file, or None and why there is none. `--card` when given; else the
    path the kickoff checker's `--card --path` prints for CLAUDE_CODE_SESSION_ID, run with stdin
    closed and a bound, so the card's location is never re-derived here (§8 F1)."""
    if card_arg is not None:
        p = pathlib.Path(os.path.normpath(root / card_arg))
        return (p, None) if p.is_file() else (None, "--card names no file, %s" % p.as_posix())
    sid = os.environ.get("CLAUDE_CODE_SESSION_ID", "")
    if not sid:
        return None, "CLAUDE_CODE_SESSION_ID is unset and no --card was given"
    checker, bash = resolve_kickoff_checker(root), resolve_bash()
    if checker is None or bash is None:
        return None, "no %s resolved to locate the card" % ("kickoff checker" if checker is None else "bash")
    try:
        r = subprocess.run([bash, str(checker), "--card", "--path", "--session", sid], cwd=root,
                           stdin=subprocess.DEVNULL, capture_output=True, encoding="utf-8",
                           errors="replace", timeout=CHECKER_BOUND_S)
    except (OSError, subprocess.TimeoutExpired) as e:
        return None, "the kickoff checker's --card --path did not answer: %s" % e
    out = r.stdout.strip()
    if r.returncode != 0 or not out:
        return None, "the kickoff checker's --card --path exited %d: %s" % (
            r.returncode, (out or r.stderr.strip()).split("\n")[0])
    m = re.match(r"^/([A-Za-z])/(.*)$", out) if os.name == "nt" else None
    p = pathlib.Path("%s:/%s" % (m.group(1), m.group(2)) if m else out)  # an MSYS bash prints /c/…
    return (p, None) if p.is_file() else (None, "the kickoff checker printed %s, which names no file" % out)


def resolve_brief_record(prompts_dir, prompt_path):
    """The brief record: `--input prompt=` when given, else the ONE file under the build's `prompts/`
    carrying both a `## The prompt` and a `## The brief` line; None when none does. Two or more
    refuse, naming each, since a guess would hand an agent another build's brief."""
    if prompt_path is not None:
        return prompt_path
    hits = [p for p in sorted(prompts_dir.glob("*.md"))
            if PROMPT_HEAD_RE.search(text := lib.load_text(p)) and BRIEF_HEAD_RE.search(text)]
    if len(hits) > 1:
        raise lib.RolesError("%s holds %d brief records (%s); name one with --input prompt=<path>" % (
            prompts_dir.as_posix(), len(hits), ", ".join(p.name for p in hits)))
    return hits[0] if hits else None


def derive_prompt_name(prompts_dir, date, unit_id, role, tail=""):
    """`<date>-prompt-<id>-<n>-<role without gov-><tail>.md`, `<n>` one above the highest that date
    and id already use under the folder, by any role, so the derived path never overwrites a file."""
    stem = "%s-prompt-%s-" % (date, unit_id)
    seq_re = re.compile(re.escape(stem) + r"([0-9]+)-")
    used = [int(m.group(1)) for p in prompts_dir.glob(stem + "*") if (m := seq_re.match(p.name))]
    return "%s%d-%s%s.md" % (stem, max(used, default=0) + 1,
                             role[4:] if role.startswith("gov-") else role, tail)


def render_card_block(root):
    """PLAY-dOrderedCharter-8 S7: `## Card`, holding the card file's first line, the `## route` section of
    what that line opens and its last line, the file's own envelope copied and never typed here; "" when
    `<root>/.claude/orientation-card.md` is absent or carries no route."""
    path = root / CARD_FILE_REL
    if not path.is_file():
        return ""
    lines = lib.load_text(path).rstrip("\n").split("\n")
    route = extract_card_section("\n".join(lines[1:-1]), "route") if len(lines) > 2 else None
    return "## Card\n\n%s\n%s\n%s" % (lines[0], route, lines[-1]) if route else ""


def read_repo_file(root, name, value):
    """`(rel, bytes, text)` of the file `value` names under `root`, its text UTF-8 with CRLF folded; a value
    naming no file inside the repository, or one that does not read as UTF-8, raises RolesError naming `name`."""
    p = pathlib.Path(os.path.normpath(root / value))
    if root not in p.parents or not p.is_file():
        raise lib.RolesError("%s — %s names no file inside the repository" % (name, value))
    try:
        raw = p.read_bytes()
        return p.relative_to(root).as_posix(), raw, raw.decode("utf-8").replace("\r\n", "\n")
    except (OSError, UnicodeDecodeError) as e:
        raise lib.RolesError("%s — %s cannot be read as UTF-8: %s" % (name, value, e))


def derive_input_facts(root, inputs):
    """`{"input:<name>": (key, text)}` of each `--input`, in the order given (TOOL-dBoundRoles-13 S3): `spec`
    and `prompt` hand the file's text keyed `record:<path>@<sha12>`, `code` the file's text keyed
    `blob:<path>@<blob12>:1-<n>` (§8 F4), and a typed argument its value keyed `cmd:` over the fixed argv
    `--input`, NUL, `<name>`. `render_handoff` and the `facts` verb both cut here, so one input keys one way
    by either route; a path input naming no file inside the repository raises RolesError naming it."""
    out = {}
    for name, v in inputs.items():
        if name in PATH_INPUTS and v:
            rel, raw, text = read_repo_file(root, "input:" + name, v)
            key = lib.derive_fact_key("blob" if name == CODE_INPUT else "record", rel, raw)
        else:
            text, key = v, lib.derive_fact_key("cmd", ["--input", name], v)
        out["input:" + name] = (key, text.replace("\r\n", "\n"))
    return out


def print_input_facts(root, memory_root, slug, inputs):
    """S5 of TOOL-dBoundRoles-13: one line of JSON, the list `[{name, key, class, text}]` of each `--input` as
    `render_handoff` hands it, the text with its blank edges trimmed as a block's is; the build folder that does
    not exist, an input naming no file and an empty or placeholder value refuse as the render refuses."""
    build_dir = root / memory_root / "builds" / slug
    if not build_dir.is_dir():
        raise lib.RolesError("the build folder %s does not exist" % build_dir.as_posix())
    facts = []
    for name, (key, text) in derive_input_facts(root, inputs).items():
        text = BLANK_EDGES_RE.sub("", text)
        if check_placeholder(text):
            raise lib.RolesError("%s — not supplied; pass --input %s=<value>" % (name, name[6:]))
        line = lib.FACT_RE.match(lib.render_fact_line(key, root))
        facts.append({"name": name, "key": key, "class": line.group("class"), "text": text})
    write_json_line(facts)


def read_item_declaration(item, role):
    """The declaration of the item `item` as the loop kit's `loop_lib.py declaration --item <tag> --json` prints it,
    run in a subprocess with stdin closed under `DECLARATION_BOUND_S`, the kit found by
    `resolve_kit_dir("loop", "loop_lib.py", KIT_DIR)` (TOOL-dBoundRoles-3 S1, §8 F5, F6). RolesError naming the
    loop kit where none resolves or its verb does not answer, the tag with the verb's first line where it exits
    non-zero, and the item's actor where it is not `role:<role>`."""
    try:
        script = lib.resolve_kit_dir("loop", "loop_lib.py", KIT_DIR) / "loop_lib.py"
    except LookupError as e:
        raise lib.RolesError("--item %s: no loop kit declares the item — %s" % (item, e))
    try:
        r = subprocess.run([sys.executable, str(script), "declaration", "--item", item, "--json"],
                           stdin=subprocess.DEVNULL, capture_output=True, encoding="utf-8", errors="replace",
                           timeout=DECLARATION_BOUND_S, env=dict(os.environ, PYTHONIOENCODING="utf-8"))
    except (OSError, subprocess.TimeoutExpired) as e:
        raise lib.RolesError("--item %s: the loop kit's %s declaration did not answer: %s" % (item, script.as_posix(), e))
    said = (r.stderr.strip() or r.stdout.strip() or "nothing printed").split("\n")[0]
    try:
        declaration = json.loads(r.stdout) if r.returncode == 0 else None
    except ValueError:
        declaration, said = None, "its output is no JSON"
    if not isinstance(declaration, dict):
        raise lib.RolesError("--item %s: the loop kit's declaration verb exited %d: %s" % (item, r.returncode, said))
    if declaration.get("actor") != "role:" + role:
        raise lib.RolesError("--item %s is the item of %s, not role:%s: a work order is cut only for the role its "
                             "item names" % (item, declaration.get("actor"), role))
    return declaration


def render_work_order_blocks(item, declaration, prefixes, inputs):
    """The five blocks an item's work order closes its task with, `lib.WORK_ORDER_BLOCKS` in order
    (TOOL-dBoundRoles-3 S2, §4 "The blocks"): the tag, its step and its outcome set; `inputs`, the rendered
    sub-blocks, or `none`; the allowance's `prefixes` as one `- <path>` line each, or `none`; the declaration's
    `returns`; and its witness's class and `by`. A field the declaration leaves empty reads `none`."""
    witness = declaration.get("witness") if isinstance(declaration.get("witness"), dict) else {}
    bodies = ("%s · %s · outcomes: %s" % (item, declaration.get("step") or "none",
                                          ", ".join(declaration.get("outcomes") or ()) or "none"),
              "\n\n".join(inputs) or "none",
              "\n".join("- " + p for p in prefixes) or "none",
              declaration.get("returns") or "none",
              "%s · %s" % (witness.get("class") or "none", witness.get("by") or "none"))
    return ["%s\n\n%s" % (head, body) for head, body in zip(lib.WORK_ORDER_BLOCKS, bodies)]


def render_handoff(root, memory_root, charter_path, role, keys, slug, unit, card_arg, inputs, out_path,
                   notes=None, tail="", upstream=None, item=None, allowance=()):
    """`(path, text, task_part)` of the prompt file; raises RolesError naming every key that refused.
    The charter library's notes are appended to `notes` when a list is given; `tail` goes before
    the derived name's `.md`; `upstream` is the rows file `--upstream` names, the `upstream:rows` source;
    `item` the item tag the marker's `item=` carries, `-` when None (TOOL-dBoundRoles-17 S3), a tag
    outside `ITEM_VALUE_RE` refused before anything is read. With `item`, its declaration is read from the loop
    kit and the task closes with `lib.WORK_ORDER_BLOCKS` (TOOL-dBoundRoles-3 S2), its allowance
    `lib.derive_allowance`'s over `allowance`, the paths `--allowance` grants."""
    if item is not None and not lib.ITEM_VALUE_RE.match(item):
        raise lib.RolesError("--item '%s' is not an item tag item.<step>.<name>, each segment lowercase "
                             "letters, digits and '-'" % item)
    build_dir = root / memory_root / "builds" / slug
    if not build_dir.is_dir():
        raise lib.RolesError("the build folder %s does not exist" % build_dir.as_posix())
    # TOOL-dBoundRoles-3 S1 S3: the item's declaration and its allowance, refused before any value is read
    declaration = prefixes = None
    if item is not None:
        declaration = read_item_declaration(item, role)
        conf = root / ".memory-tree.conf"
        prefixes = lib.derive_allowance(declaration, slug, allowance, memory_root,
                                        lib.read_conf_key(conf, "ROUTED_PATHS") if conf.is_file() else None)
    elif allowance:
        raise lib.RolesError("--allowance %s: only an item's work order takes an allowance; pass --item <tag>"
                             % allowance[0])
    # TOOL-dBoundRoles-13 S3: every `reads` value is handed as content under the key it was cut by, the
    # rows file's `record:` key (§8 F4) on its rows, the renderer's contract after them unkeyed
    values, fact_keys = {}, {}
    if upstream:
        rel, raw, rows = read_repo_file(root, UPSTREAM_KEY, upstream)
        rows = rows.strip("\n")
        if rows.strip():   # an empty rows file hands nothing, so the key reads as not supplied
            values[UPSTREAM_KEY] = rows + "\n\n" + UPSTREAM_CONTRACT
            fact_keys[UPSTREAM_KEY] = lib.derive_fact_key("record", rel, raw)
    for name, (key, text) in derive_input_facts(root, inputs).items():
        values[name], fact_keys[name] = text, key
    # PLAY-dOrderedCharter-11 S4: the role's load set and its block's budget, before any card or brief is read;
    # a supplied code block is measured beside it, CR stripped (PLAY-dOrderedCharter-27 S4)
    # TOOL-dBoundRoles-2 S6: the role closes with its never list, its ceiling and its return, the ceiling's
    # gate legs the policy's merged grant (TOOL-dBoundRoles-21 S6), loaded as `print_role_efforts` loads
    # it, so both routes render one block
    roles = lib.load_roles(KIT_DIR)
    doc = charter_path.relative_to(root).as_posix() if root in charter_path.parents else charter_path.as_posix()
    # TOOL-dBoundRoles-15 S6: the single carry, read once per render and checked before any file is written;
    # every route of today's one adapter is `static`, so no task carries the charter and `always` refuses
    stand_in = tail == lib.STAND_IN_TAIL
    carry = lib.read_policy_setting("instructions.task-charter", root)
    if carry is None and None in lib._POLICY_ANSWERS and notes is not None:   # no policy kit answered
        notes.append(TASK_CHARTER_NOTE)
    kind, carrier = lib.derive_harness_kind(keys, stand_in, doc)
    lib.check_single_carry(carry, kind, role, carrier)
    granted = lib.load_policy(KIT_DIR, roles, lib.load_workflows(KIT_DIR)).get("gates", {})
    role_text = lib.render_role(KIT_DIR, role, memory_root, granted.get(role, ()))
    charter_text = lib.load_text(charter_path)
    try:   # a doc that is no charter refuses where it always has, after the load set and the reads
        charter, charter_error = lib.parse_charter(charter_text, doc), None
    except lib.RolesError as e:
        charter, charter_error = None, e
    if charter is not None and charter["shape"] == "legacy" and notes is not None:
        notes.append(lib.LEGACY_NOTE % doc)
    try:
        rows = lib.load_document_registry(KIT_DIR)
    except LookupError as exc:   # no playbook kit: the roles kit does not require it (F4)
        rows = None
        if notes is not None:
            notes.append(lib.UNRANKED_NOTE % exc)
    # PLAY-dOrderedCharter-5 S3: the charter rides once, in the agent file; the render still grades the tags,
    # here, where the load-set check measures the whole static block (TOOL-dBoundRoles-15 §8 F7)
    block, tag_refusals = role_text, []
    if charter is not None:
        try:
            block = lib.render_static_block(KIT_DIR, role, roles[role], memory_root, charter, notes,
                                            granted.get(role, ()), (), rows, doc)
        except lib.RolesError as e:
            tag_refusals = str(e).split("\n")
    code = values.get("input:" + CODE_INPUT)
    refused, gate = lib.check_load_set(root, KIT_DIR, [(role, len(block.encode("utf-8")))],
                                       [(CODE_INPUT, len(code.replace("\r", "").encode("utf-8")))] if code else [],
                                       reach=True)
    if refused:
        raise lib.RolesError("\n".join(gate))
    # PLAY-dOrderedCharter-21 S3: the role's reach units, off the same run and out of the notes
    reach = [ln[len(REACH_LINE):].split(" · ", 2) for ln in gate if ln.startswith(REACH_LINE)]
    gate = [ln for ln in gate if not ln.startswith(REACH_LINE)]
    missing = [ln for ln in gate if ln.startswith("Missing required unit:")]
    gaps = [ln for ln in gate if ln.startswith("**Load gaps:**")]
    if notes is not None:
        notes.extend(ln for ln in gate if ln not in missing and ln not in gaps)
    unit_id = unit
    if unit_id is None:
        fm = lib.FRONT_MATTER_RE.match(lib.load_text(build_dir / "README.md")) \
            if (build_dir / "README.md").is_file() else None
        ids = re.search(r"^ids:[ \t]*(\S+)", fm.group(1), re.M) if fm else None
        if not ids:
            raise lib.RolesError("no --unit, and %s/README.md names no ids: in its front matter"
                                 % build_dir.as_posix())
        unit_id = ids.group(1)
    refusals = []
    # TOOL-dBoundRoles-14 S4: each entry in either spelling, read as its native key, so a `field.` tag
    # dispatches to its family and its block keeps the native `### <key>` heading
    reads = [k + "?" * o for k, o in (lib.parse_read_key(x) for x in keys.get("reads", "").split(",") if x.strip())]
    if not any(k.rstrip("?") == "input:" + CODE_INPUT for k in reads):
        reads.append("input:%s?" % CODE_INPUT)  # the derived optional key every role carries
    # TOOL-dBoundRoles-3 S2: the item's inputs, each read as its native key, so every source either list names is read
    item_keys = [k + "?" * o for k, o in (lib.parse_read_key(x) for x in (declaration or {}).get("inputs") or ()
                                         if isinstance(x, str) and x.strip())]
    wanted = reads + item_keys
    card = brief = None
    why, labels = {}, {}
    if any(k.startswith("task:") for k in wanted):
        # The card labels, read off the checker that grades a card rather than typed beside it
        # (TOOL-aOrientedCast-15 S3): the same bounded, stdin-closed run `resolve_card_path` makes.
        checker, bash = resolve_kickoff_checker(root), resolve_bash()
        if checker is None or bash is None:
            raise lib.RolesError("task: — no %s resolved to read the card labels from --task-skeleton"
                                 % ("kickoff checker" if checker is None else "bash"))
        try:
            r = subprocess.run([bash, str(checker), "--task-skeleton"], cwd=root, stdin=subprocess.DEVNULL,
                               capture_output=True, encoding="utf-8", errors="replace", timeout=CHECKER_BOUND_S)
        except (OSError, subprocess.TimeoutExpired) as e:
            raise lib.RolesError("task: — the kickoff checker %s --task-skeleton did not answer: %s"
                                 % (checker.as_posix(), e))
        derived = list(extract_task_fields("## task\n" + r.stdout, None)) if r.returncode == 0 else []
        if len(derived) != len(TASK_FIELDS):
            raise lib.RolesError("task: — the kickoff checker %s --task-skeleton exited %d with %d field "
                                 "labels, and the task fields are %d" % (checker.as_posix(), r.returncode,
                                                                          len(derived), len(TASK_FIELDS)))
        labels = dict(zip(derived, TASK_FIELDS))
    if any(k.startswith(("task:", "card:")) for k in wanted):
        card, why["card"] = resolve_card_path(root, card_arg)
        card_text = lib.load_text(card) if card else ""
        if card:
            # the session's card is `card/<session id>`; a `--card` inside the repository its own path, else
            # `card/<stem>` (TOOL-dBoundRoles-13 S1)
            ref = (card.relative_to(root).as_posix() if card_arg is not None and root in card.parents else
                   "card/%s" % (card.stem if card_arg is not None else os.environ.get("CLAUDE_CODE_SESSION_ID", "")))
            fact_keys["task"] = fact_keys["card"] = lib.derive_fact_key("record", ref, card.read_bytes())
        values.update(("task:" + f, v) for f, v in extract_task_fields(card_text, labels).items())
        for k in wanted:
            if k.startswith("card:") and card:
                section = extract_card_section(card_text, k.rstrip("?")[5:])
                if section is not None:
                    values[k.rstrip("?")] = section
    if any(k.startswith("brief:") for k in wanted):
        prompts = build_dir / "prompts"
        brief = resolve_brief_record(prompts, inputs.get("prompt") and pathlib.Path(
            os.path.normpath(root / inputs["prompt"])))
        why["brief record"] = None if brief else (
            "no file under %s carries both a '## The prompt' and a '## The brief' line" % prompts.as_posix())
        brief_text = lib.load_text(brief) if brief else ""
        if brief:
            fact_keys["brief"] = lib.derive_fact_key("record", brief.relative_to(root).as_posix(), brief.read_bytes())
        for k in wanted:
            if k.startswith("brief:") and brief:
                # TOOL-dPavedRoad-3: the owner's words are the record's own `## The prompt` section,
                # read as a card section is; every other brief key is a sub-head of `## The brief`.
                field = k.rstrip("?")[6:]
                section = (extract_card_section(brief_text, "The prompt") if field == "prompt"
                           else extract_brief_section(brief_text, field))
                if section is not None:
                    values[k.rstrip("?")] = section
    sources = {"task": ("card", card), "card": ("card", card), "brief": ("brief record", brief),
               "input": ("arguments", None), "upstream": ("arguments", None)}
    blocks, absent, reasons = [], [], []
    for k in reads:
        key = k.rstrip("?")
        v = BLANK_EDGES_RE.sub("", values.get(key, ""))
        if not check_placeholder(v):
            # TOOL-dBoundRoles-13 S3: the fact line, then the content, under the `reads` key's heading; the content
            # inside a fence no line of it can close, the fact line outside it (TOOL-dBoundRoles-38 S2); a typed
            # input is authored text, written unfenced and refused where a line would stand as an executor line
            # or its fence never closes (TOOL-dBoundRoles-45 S1 S2)
            fact = fact_keys.get(key) or fact_keys[key.split(":")[0]]
            typed = key.startswith("input:") and key[6:] in TYPED_INPUTS
            if typed:
                refusals += lib.check_authored_lines(v, key)
            blocks.append("### %s\n\n%s\n\n%s" % (key, lib.render_fact_line(fact, root),
                                                  v if typed else lib.render_handed_fence(v)))
            continue
        src, path = sources[key.split(":")[0]]
        what = ("no %s: %s" % (src, why[src])) if why.get(src) else (
            "the %s %s carries no single filled value for it: absent, repeated, empty or a placeholder"
            % (src, path.as_posix()) if path else "not supplied; pass --upstream <rows file>" if key == UPSTREAM_KEY
            else "not supplied; pass --input %s=<value>" % key[6:])
        if not k.endswith("?"):
            refusals.append("%s — %s" % (key, what))
        else:
            absent.append(key)
            reasons += [what] if why.get(src) and what not in reasons else []
    if declaration is not None:
        # TOOL-dBoundRoles-3 S2: each input of the item handed as content under its own level-3 heading, a `reads`
        # key spelled as its `field.` tag, its fact line two below; one it cannot resolve refuses or is not supplied
        subs = []
        for k in item_keys:
            key = k.rstrip("?")
            head = lib.derive_field_tag(key) if key in lib.READ_KEYS else key
            v = BLANK_EDGES_RE.sub("", values.get(key, ""))
            fact = fact_keys.get(key) or fact_keys.get(key.split(":")[0])
            if fact and not check_placeholder(v):
                subs.append("### %s\n\n%s\n\n%s" % (head, lib.render_fact_line(fact, root), lib.render_handed_fence(v)))
            elif not k.endswith("?"):
                if not any(r.startswith(key + " — ") for r in refusals):
                    refusals.append("%s — the item %s's input carries no value this render resolves" % (head, item))
            elif key not in absent:
                absent.append(key)
        blocks += render_work_order_blocks(item, declaration, prefixes, subs)
    if charter_error is not None:
        raise charter_error
    refusals += tag_refusals
    if refusals:
        raise lib.RolesError("\n".join(refusals))
    opening = ("This handoff is for build `%s`, unit `%s`." % (slug, unit_id) if unit
               else "This handoff is for build `%s`, and names no single unit." % slug)
    if missing:
        opening += "\n" + "\n".join(missing)
    if absent:
        opening += "\nNot supplied, optional: %s%s." % (
            ", ".join("`%s`" % k for k in absent), " — " + "; ".join(reasons) if reasons else "")
    step = reach[0][1].rsplit(".", 1)[1] if reach else None
    practices = ("### Practices at %s\n\n" % step + "\n".join(
        "- [%s] %s" % (tag.split(".")[1], text) for _reader, tag, text in reach)) if reach else ""
    path = out_path or build_dir / "prompts" / derive_prompt_name(
        build_dir / "prompts", datetime.date.today().isoformat(), unit_id, role, tail)
    rel = path.relative_to(root).as_posix()
    wraps = None
    if rows is not None:   # PLAY-dOrderedCharter-5 S2: each block in the envelope of its level
        wraps = {"## Task": (rel, TASK_LEVEL, TASK_DIRECTION)}
        row = lib.read_envelope_row(rows, doc, memory_root)
        if practices and row is not None:
            practices = lib.render_envelope(PRACTICES_DOC % (doc, step), row[0], row[1], practices)
    # PLAY-dOrderedCharter-8 S7: the card's level-1 block leads the task part after the level-0 practices
    card_block = render_card_block(root)
    if card_block:
        practices = practices.rstrip("\n") + "\n\n" + card_block if practices else card_block
    # TOOL-dBoundRoles-6 S4: the role section is the library's one composition, the one the role index's
    # `role-sha` hashes, with its drive lines and its agent file's envelope; the task part is the template's
    role_sec = lib.render_role_section(KIT_DIR, role, memory_root, charter_text, granted.get(role, ()), rows)
    task_sec = lib.render_work_order_section(WORK_ORDER, lib.extract_work_order_parts(WORK_ORDER)[1], {
        "opening": opening, "reads": "\n\n".join(blocks), "practices": practices}, wraps) + "\n"
    # TOOL-dBoundRoles-38 S5: a section whose walk ends inside a fence would hide every later fact line from
    # the spawn's re-cut, so it refuses, naming the block the fence opened in and its line, and nothing is written
    block_at = "the task's opening"
    for n, line in lib.read_unfenced_lines(task_sec):
        if line is None:
            raise lib.RolesError("%s — a fence opened at line %d of the ## Task section is never closed, so every "
                                 "fact line after it would be read as content; close it in the value that opened "
                                 "it and render again" % (block_at, n))
        if line.startswith(("## ", "### ")):
            block_at = line
    marker ="<!-- gov:handoff role=%s build=%s unit=%s item=%s path=%s role-sha=%s task-sha=%s -->" % (
        role, slug, unit or "-", item or "-", rel, lib.derive_section_sha(role_sec), lib.derive_section_sha(task_sec))
    head = "**Serves:** journal %s\n%s\n# %s handoff — %s\n\n%s\n\n" % (
        unit_id, "".join(g + "\n" for g in gaps), role, unit_id, marker)
    return path, head + role_sec + task_sec, marker + "\n\n" + task_sec


def check_handoff(root, path):
    """`(ok, lines)`: the marker's two hashes re-derived from the file's own bytes, CRLF folded, and
    its `path` compared with the file's repo-relative path, and for a marker whose `item=` is a tag each of
    `lib.WORK_ORDER_BLOCKS` looked for as a whole line inside `## Task` (TOOL-dBoundRoles-3 S6); one line per
    mismatch or missing block, else one line naming the path and both hashes."""
    p = pathlib.Path(os.path.normpath(root / path))
    rel = p.relative_to(root).as_posix() if root in p.parents else p.as_posix()
    try:
        with open(p, "rb") as fh:
            text = fh.read().decode("utf-8").replace("\r\n", "\n")
    except (OSError, UnicodeDecodeError) as e:
        return False, ["handoff: %s: cannot be read as UTF-8 — %s" % (rel, e)]
    marker = MARKER_RE.search(text)
    role_m = ROLE_HEAD_RE.search(text, marker.end()) if marker else None
    task_m = TASK_HEAD_RE.search(text, role_m.end()) if role_m else None
    if not task_m:
        return False, ["handoff: %s: no gov:handoff marker line followed by a '## Role' and a "
                       "'## Task' line" % rel]
    role_sha = lib.derive_section_sha(text[role_m.start():task_m.start()])
    task_sha = lib.derive_section_sha(text[task_m.start():])
    bad = ["handoff: %s: %s — the marker says %s, the file gives %s" % (rel, what, said, actual)
           for what, said, actual in (("role-sha", marker.group("role_sha"), role_sha),
                                      ("task-sha", marker.group("task_sha"), task_sha),
                                      ("path", marker.group("path"), rel))
           if said != actual]
    # TOOL-dBoundRoles-3 S6: a work order cut for an item carries the kind's five blocks inside `## Task`
    item = marker.group("item")
    if item not in (None, "-"):
        task_text = text[task_m.start():]
        bad += ["handoff: %s: item=%s — the work order lacks its '%s' block inside '## Task', a part of the %s kind"
                % (rel, item, head, lib.WORK_ORDER_KIND["kind"]) for head in lib.WORK_ORDER_BLOCKS
                if not re.search(r"^%s[ \t]*$" % re.escape(head), task_text, re.M)]
    ranked, levels = check_envelope_order(rel, text, role_m.start(), task_m.start())
    bad += ranked
    return not bad, bad or ["%s role-sha=%s task-sha=%s" % (rel, role_sha, task_sha), levels]


def check_envelope_order(rel, text, role_at, task_at):
    """`(bad, levels)` of PLAY-dOrderedCharter-5 S4 over a prompt file's text: every envelope opened closes,
    in nesting order, and the openers' levels never decrease down each part, `## Role` from `role_at` and
    `## Task` from `task_at`, which a native agent receives apart. `levels` is the one line naming each
    part's levels in order; a file holding no envelope is `unranked` and passes, since a prompt record
    rendered before the envelopes is frozen."""
    found = lib.read_envelopes(text)
    if not found:
        return [], "%s envelopes — unranked: none carried, so no level is graded" % rel
    bad, stack = [], []
    for n, kind, doc, _level, _direction in found:
        if kind == "open":
            stack.append((n, doc))
        elif stack and stack[-1][1] == doc:
            stack.pop()
        else:
            bad.append("handoff: %s: line %d closes the envelope %s, and %s" % (
                rel, n, doc, "the open one is %s" % stack[-1][1] if stack else "none is open"))
    bad += ["handoff: %s: the envelope %s opened at line %d has no closer" % (rel, doc, n) for n, doc in stack]
    said = []
    for part, start, end in (("## Role", role_at, task_at), ("## Task", task_at, len(text))):
        first, last = text.count("\n", 0, start) + 1, text.count("\n", 0, end) + 1
        opened = [(n, doc, level) for n, kind, doc, level, _d in found if kind == "open" and first <= n <= last]
        for (_n, was, low), (n, doc, level) in zip(opened, opened[1:]):
            if level < low:
                bad.append("handoff: %s: the envelope %s at line %d opens at level %d after %s at level %d, "
                           "and levels never decrease down the %s part" % (rel, doc, n, level, was, low, part))
        said.append("%s %s" % (part[3:], " ".join(str(lv) for _n, _d, lv in opened) or "none"))
    return bad, "%s envelopes — %s" % (rel, " · ".join(said))


def write_json_line(obj):
    """One line of sorted, compact JSON on stdout: the shape a harness argument takes."""
    sys.stdout.buffer.write((json.dumps(obj, sort_keys=True, separators=(",", ":"),
                                        ensure_ascii=False) + "\n").encode("utf-8"))


def print_harness_args(harness):
    """Print the union of the stage maps, `derive_stage_map` of each entry's stage rows
    (TOOL-dBoundRoles-22 S2), of every workflow whose harness path ends in the script `harness` (its
    file name without extension) as one line of sorted JSON; RolesError when no workflow's harness
    carries it or one stage key maps to two roles."""
    union, hit = {}, False
    for w in lib.load_workflows(KIT_DIR):
        tokens = [t for t in str(w.get("harness", "")).split() if "/" in t]
        if not any(t.rsplit("/", 1)[-1].rsplit(".", 1)[0] == harness for t in tokens):
            continue
        hit = True
        for key, slot in lib.derive_stage_map(w).items():
            if union.get(key, slot) != slot:
                raise lib.RolesError("stage key %s maps to both %s and %s across the workflows of %s"
                                     % (key, union[key], slot, harness))
            union[key] = slot
    if not hit:
        raise lib.RolesError("no workflow's harness is the script %s" % harness)
    write_json_line(union)


def print_stage_efforts(workflow, model, root):
    """Print the resolved level of every stage row's key of one workflow as one line of sorted JSON
    (TOOL-aOrientedCast-10; TOOL-dBoundRoles-22 S2); RolesError on an unknown name, a workflow with no
    stage rows, or a policy defect. Keyed by workflow, not harness: a harness serving two workflows runs
    one role at two levels, which a union cannot carry. `model` goes to the resolver unchanged
    (TOOL-aProfiledEffort-2), and `root`, the repository whose policy keys it reads first
    (TOOL-dBoundRoles-21 S7)."""
    workflows = lib.load_workflows(KIT_DIR)
    policy = lib.load_policy(KIT_DIR, lib.load_roles(KIT_DIR), workflows)
    entry = next((w for w in workflows if w.get("name") == workflow), None)
    if entry is None:
        raise lib.RolesError("no workflow named %s in workflows.toml" % workflow)
    if not lib.derive_stage_map(entry):
        raise lib.RolesError("the workflow %s has no stage rows, so no harness stage takes a level"
                             % workflow)
    write_json_line(lib.resolve_stage_efforts(policy, entry, model, root))


def print_role_efforts(model, root):
    """Print the resolved level of every role whose `agent` is true as one line of sorted JSON
    (TOOL-aProfiledEffort-2), the policy keys of the repository at `root` read first
    (TOOL-dBoundRoles-21 S7); RolesError on a policy defect."""
    roles = lib.load_roles(KIT_DIR)
    policy = lib.load_policy(KIT_DIR, roles, lib.load_workflows(KIT_DIR))
    write_json_line({slot: lib.resolve_effort(policy, slot, model, root) for slot, role in roles.items()
                     if role["keys"].get("agent", "true") == "true"})


def print_roster(memory_root):
    """Print one charter line per role, `- `<slot>`: <description> <when>. Output: <output>.`, in the
    workflow table's order (TOOL-aOrientedCast-17); RolesError naming every role whose line is past
    its cap or lacks a key, and on an empty catalogue, with nothing printed.

    THE CAP OBEYS THE SWITCH (TOOL-dGroundRules-9): the census cap `roster-line`, ROSTER_LINE_MAX
    handed in as its default, answered once by `lib.read_cap_answer` in the working directory's
    repository. Under `warn` a line past it renders, and its `BUDGET WARN` line goes to stderr, never
    into the roster a render reads; under `refuse` it refuses as before, naming the rule."""
    from check_roles import NOT_MANDATORY_RE  # the checker's one reading of an optional role
    roles = lib.load_roles(KIT_DIR)
    if not roles:
        raise lib.RolesError("%s holds no role file, so the roster is empty"
                             % (KIT_DIR / "agents").as_posix())
    index = {}
    for i, w in enumerate(lib.load_workflows(KIT_DIR)):
        index.setdefault(w.get("name"), (i, w.get("roles") if isinstance(w.get("roles"), list) else []))

    def derive_rank(slot):
        hit = index.get(roles[slot]["keys"].get("workflow"))
        if hit is None:
            return (1, 0, 0, slot)
        listed = hit[1]
        return (0, hit[0], listed.index(slot) if slot in listed else len(listed), slot)

    lines, bad, warned = [], [], []
    cap, mode, rule = lib.read_cap_answer("roster-line=default:%d" % ROSTER_LINE_MAX, ".", KIT_DIR)
    for slot in sorted(roles, key=derive_rank):
        keys = roles[slot]["keys"]
        missing = [k for k in ("description", "mandatory", "output") if not keys.get(k)]
        if missing:
            bad.append("role %s has no %s, so its roster line cannot be composed"
                       % (slot, " and no ".join(missing)))
            continue
        mandatory, output = keys["mandatory"].rstrip("."), keys["output"].rstrip(".")
        if mandatory == "no":
            when = "Optional"
        elif NOT_MANDATORY_RE.match(mandatory):
            when = "Optional, " + mandatory[len("no — "):]
        else:
            when = "Mandatory " + mandatory
        line = ("- `%s`: %s %s. Output: %s." % (slot, keys["description"], when, output)).replace(
            lib.MEMORY_ROOT_TOKEN, memory_root)
        if cap and len(line) > cap and mode == "warn":
            # The runner's `gate-warn` marker on the warning's next line, on its stream (TOOL-dWitnessedBar-29 S2, §8
            # F4); `read_cap_answer` loaded its factory to answer `warn`.
            budgets = sys.modules.get("budgets")
            warned.append("BUDGET WARN — roster-line · %s · %d chars over %d · %s" % (slot, len(line), cap, rule)
                          + ("\n" + budgets.render_warn_marker(slot, "roster-line · %d chars over %d" % (len(line), cap))
                             if budgets else ""))
        elif cap and len(line) > cap:
            bad.append("roster line for %s is %d characters, past the %d a one-line charter rule may "
                       "take; shorten its description, mandatory or output (%s)" % (slot, len(line), cap, rule))
        lines.append(line)
    if bad:
        raise lib.RolesError("\n".join(bad))
    for w in warned:
        print(w, file=sys.stderr)
    sys.stdout.buffer.write(("\n".join(lines) + "\n").encode("utf-8"))


def resolve_session_file(root, session_arg):
    """`(path, why)`: the session's transcript, or None and why there is none. `--session` when given,
    read from the repository root when relative; else CLAUDE_CODE_SESSION_ID, which must be a
    lowercase UUID before it reaches a path, globbed as `<projects>/*/<id>.jsonl`, the largest hit
    winning. `<projects>` is `$CLAUDE_CONFIG_DIR/projects`, else `.claude/projects` under USERPROFILE
    on Windows and HOME elsewhere. That is the run-log kit's rule for finding a session, spelled
    again here because a kit file imports no sibling kit."""
    if session_arg is not None:
        p = pathlib.Path(os.path.normpath(root / session_arg))
        return (p, None) if p.is_file() else (None, "--session names no file, %s" % p.as_posix())
    sid = os.environ.get("CLAUDE_CODE_SESSION_ID", "")
    if not sid:
        return None, "CLAUDE_CODE_SESSION_ID is unset and no --session was given"
    if not SESSION_ID_RE.match(sid):
        return None, "CLAUDE_CODE_SESSION_ID %r is not a lowercase UUID, and nothing else reaches a path" % sid[:80]
    if os.environ.get("CLAUDE_CONFIG_DIR"):
        projects = pathlib.Path(os.environ["CLAUDE_CONFIG_DIR"]) / "projects"
    else:
        home = (os.environ.get("USERPROFILE") or os.environ.get("HOME")) if sys.platform.startswith("win") \
            else os.environ.get("HOME")
        if not home:
            return None, "CLAUDE_CONFIG_DIR and the profile's home are both unset; pass --session"
        projects = pathlib.Path(home) / ".claude" / "projects"
    hits = sorted(projects.glob("*/%s.jsonl" % sid))
    if not hits:
        return None, "no session file %s/*/%s.jsonl; pass --session" % (projects.as_posix(), sid)
    return max(hits, key=lambda p: (p.stat().st_size, p.as_posix())), None


def parse_session_line(raw, state):
    """Fold one session-file line's bytes into `state`, `{"calls", "by_id", "notified", "bad"}`: the
    per-line body of load_session_calls, shared by its cold and its resumed read."""
    if not any(t in raw for t in SESSION_LINE_TOKENS):
        return
    try:
        rec = json.loads(raw)
    except (ValueError, RecursionError):
        rec = None
    if not isinstance(rec, dict):
        state["bad"] += 1
        return
    calls, by_id, notified = state["calls"], state["by_id"], state["notified"]
    msg = rec.get("message") if isinstance(rec.get("message"), dict) else {}
    content, texts = msg.get("content"), []
    if rec.get("type") == "user" and isinstance(content, str):
        texts.append(content)
    for b in content if isinstance(content, list) else []:
        if not isinstance(b, dict):
            continue
        if rec.get("type") == "assistant" and b.get("type") == "tool_use" \
                and b.get("name") in ("Agent", "Workflow"):
            call = {"id": b.get("id"), "name": b["name"], "result": None,
                    "input": b.get("input") if isinstance(b.get("input"), dict) else {}}
            calls.append(call)
            by_id[call["id"]] = call
        elif b.get("type") == "tool_result" and b.get("tool_use_id") in by_id \
                and isinstance(rec.get("toolUseResult"), dict):
            by_id[b["tool_use_id"]]["result"] = rec["toolUseResult"]
        elif rec.get("type") == "user" and b.get("type") == "text" and isinstance(b.get("text"), str):
            texts.append(b["text"])
    att = rec.get("attachment")
    if isinstance(att, dict) and att.get("type") == "queued_command" and isinstance(att.get("prompt"), str):
        texts.append(att["prompt"])
    if rec.get("type") == "queue-operation" and isinstance(rec.get("content"), str):
        texts.append(rec["content"])
    for block in (n for t in texts for n in NOTIFICATION_RE.findall(t)):
        tid = re.search(r"<tool-use-id>([^<]*)</tool-use-id>", block)
        status = re.search(r"<status>([^<]*)</status>", block)
        if tid:
            notified[tid.group(1).strip()] = status.group(1).strip() if status else None


def read_session_record(path, parser, session):
    """The session record at `path` (TOOL-aTrimmedWait-7), or None when it is absent, unreadable, or
    any key fails: exactly SESSION_RECORD_KEYS, `parser` and `session` equal to the given ones, `offset`
    an int from 0 to the session file's size, `prefix` 64 lowercase hex, `calls` the call dicts,
    `notified` a map of string to string or None, `bad` an int of at least 0. None is a miss."""
    try:
        with open(path, encoding="utf-8") as fh:
            rec = json.load(fh)
        size = os.path.getsize(session)
    except (OSError, ValueError, RecursionError):
        return None
    if not isinstance(rec, dict) or set(rec) != SESSION_RECORD_KEYS:
        return None
    nat = lambda v: isinstance(v, int) and not isinstance(v, bool) and v >= 0  # noqa: E731
    calls, notified = rec["calls"], rec["notified"]
    ok = (rec["parser"] == parser and rec["session"] == session and nat(rec["offset"]) and rec["offset"] <= size
          and isinstance(rec["prefix"], str) and re.fullmatch(r"[0-9a-f]{64}", rec["prefix"]) is not None
          and nat(rec["bad"]) and isinstance(calls, list) and isinstance(notified, dict)
          and all(isinstance(c, dict) and set(c) == {"id", "name", "input", "result"}
                  and not isinstance(c["id"], (list, dict)) and c["name"] in ("Agent", "Workflow")
                  and isinstance(c["input"], dict) and (c["result"] is None or isinstance(c["result"], dict))
                  for c in calls)
          and all(isinstance(v, str) or v is None for v in notified.values()))
    return rec if ok else None


def write_session_record(path, rec):
    """Write `rec` to `path` through `<path>.<pid>.tmp` and os.replace, creating its folder. Any
    OSError removes the temporary file and returns: a record not written is a later miss."""
    tmp = path.with_name("%s.%d.tmp" % (path.name, os.getpid()))
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps(rec))
        os.replace(tmp, path)
    except OSError:
        try:
            os.unlink(tmp)
        except OSError:
            pass


def load_session_calls(path, cache_dir=None):
    """`(calls, notified, bad)` of one session file, read once, line by line. `calls` holds each
    `Agent` and `Workflow` call as `{"id", "name", "input", "result"}` in call order, `result` its
    record's `toolUseResult` or None; `notified` maps a tool-use id to the `<status>` (None when it
    carries none) of a `<task-notification>` naming it, delivered in a user record or still queued
    in a `queued_command` attachment or a `queue-operation` record; `bad` counts the lines that did
    not parse. Only a line whose bytes carry one of SESSION_LINE_TOKENS is parsed.
    With `cache_dir` (TOOL-aTrimmedWait-7), the record there for this file, valid by
    read_session_record and its `prefix` the sha256 of the file's first `offset` bytes, resumes the
    read at `offset`; the record is written back when the complete lines read moved `offset`, and only
    then is an unterminated last line parsed, so a record never holds a torn line."""
    state = {"calls": [], "by_id": {}, "notified": {}, "bad": 0}
    offset, h, rec, record, tail = 0, hashlib.sha256(), None, None, b""
    if cache_dir is not None:
        session = pathlib.Path(path).resolve().as_posix()
        record = pathlib.Path(cache_dir) / (hashlib.sha256(session.encode("utf-8")).hexdigest()[:16] + ".json")
        parser = hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
        rec = read_session_record(record, parser, session)
    with open(path, "rb") as fh:
        if rec is not None:
            left = rec["offset"]
            while left:
                chunk = fh.read(min(left, 1 << 20))
                if not chunk:
                    break
                h.update(chunk)
                left -= len(chunk)
            if not left and h.hexdigest() == rec["prefix"]:
                state.update(calls=rec["calls"], notified=rec["notified"], bad=rec["bad"])
                for call in state["calls"]:
                    state["by_id"][call["id"]] = call
                offset = rec["offset"]
            else:
                rec, h = None, hashlib.sha256()
                fh.seek(0)
        for raw in fh:
            if record is not None:
                if not raw.endswith(b"\n"):
                    tail = raw
                    break
                h.update(raw)
                offset += len(raw)
            parse_session_line(raw, state)
    if record is not None and (rec is None or offset != rec["offset"]):
        write_session_record(record, {"parser": parser, "session": session, "offset": offset,
                                      "prefix": h.hexdigest(), "calls": state["calls"],
                                      "notified": state["notified"], "bad": state["bad"]})
    if tail:
        parse_session_line(tail, state)
    return state["calls"], state["notified"], state["bad"]


def load_agent_transcript(path):
    """What one agent's transcript and the `.meta.json` beside it record, each None when nothing does:
    `type` and `description` from the meta; `effort` and `model`, the last `assistant` record's
    carrying one; `wall`, the seconds from the transcript's first `timestamp` to its last; `tokens`,
    the sum over distinct `message.id` values of the largest `output_tokens`, because one response
    is split into records each carrying its usage as it streamed, which is the run-log kit's
    per-request rule; and `files`, the set of distinct paths its WRITE_TOOLS uses name."""
    out = dict.fromkeys(("type", "description", "effort", "model", "wall", "tokens"))
    out["files"] = set()
    try:
        with open(path.with_name(path.name[:-len(".jsonl")] + ".meta.json"), encoding="utf-8") as fh:
            meta = json.load(fh)
    except (OSError, ValueError):
        meta = None
    for key, src in (("type", "agentType"), ("description", "description")):
        if isinstance(meta, dict) and isinstance(meta.get(src), str) and meta[src].strip():
            out[key] = meta[src].strip()
    stamps, per_id = [], {}
    try:
        with open(path, "rb") as fh:
            raw_lines = fh.read().split(b"\n")
    except OSError:
        raw_lines = []
    for n, raw in enumerate(raw_lines):
        try:
            rec = json.loads(raw) if raw.strip() else None
        except (ValueError, RecursionError):
            rec = None
        if not isinstance(rec, dict):
            continue
        try:
            stamps.append(datetime.datetime.fromisoformat(rec["timestamp"].replace("Z", "+00:00")))
        except (KeyError, AttributeError, TypeError, ValueError):
            pass
        msg = rec.get("message")
        if rec.get("type") != "assistant" or not isinstance(msg, dict):
            continue
        if isinstance(rec.get("effort"), str) and rec["effort"]:
            out["effort"] = rec["effort"]
        # ponytail: `<synthetic>` marks a record Claude Code wrote itself, which no model ran
        if isinstance(msg.get("model"), str) and msg["model"] and msg["model"] != "<synthetic>":
            out["model"] = msg["model"]
        tokens = (msg.get("usage") or {}).get("output_tokens") if isinstance(msg.get("usage"), dict) else None
        if isinstance(tokens, int) and not isinstance(tokens, bool):
            mid = msg.get("id") if isinstance(msg.get("id"), str) else ("record", n)
            per_id[mid] = max(per_id.get(mid, 0), tokens)
        for b in msg.get("content") if isinstance(msg.get("content"), list) else []:
            if isinstance(b, dict) and b.get("type") == "tool_use" and b.get("name") in WRITE_TOOLS \
                    and isinstance(b.get("input"), dict):
                # ponytail: NotebookEdit names its file `notebook_path`, every other write tool `file_path`
                target = b["input"].get("file_path") or b["input"].get("notebook_path")
                if isinstance(target, str) and target:
                    out["files"].add(target)
    if stamps:
        out["wall"] = max(0, int((stamps[-1] - stamps[0]).total_seconds()))
    if per_id:
        out["tokens"] = sum(per_id.values())
    return out


def load_run_journal(path):
    """One harness run's agents from its `journal.jsonl`, one per `started` entry in journal order, as
    `{"id", "label", "returned", "failed", "result"}`: `returned` once a `result` or `failed` entry
    names the agent, `result` that `result` entry's value. A line that does not parse is skipped."""
    agents, by_id = [], {}
    for line in lib.load_text(path).split("\n"):
        try:
            e = json.loads(line) if line.strip() else None
        except (ValueError, RecursionError):
            e = None
        if not isinstance(e, dict) or not isinstance(e.get("agentId"), str):
            continue
        if e.get("type") == "started" and e["agentId"] not in by_id:
            by_id[e["agentId"]] = {"id": e["agentId"], "returned": False, "failed": False, "result": None,
                                   "label": e["label"] if isinstance(e.get("label"), str) and e["label"] else None}
            agents.append(by_id[e["agentId"]])
        elif e.get("type") in ("result", "failed") and e["agentId"] in by_id:
            by_id[e["agentId"]].update(returned=True, failed=e["type"] == "failed" or by_id[e["agentId"]]["failed"],
                                       **({"result": e.get("result")} if e["type"] == "result" else {}))
    return agents


def render_shape_line(definition, fields):
    """`- <definition>` with each `<name>` replaced by `fields[name]`, every ` · ` inside a value made
    `, ` and every line break a space, so no value can add a field; RolesError naming a placeholder
    the dict does not hold, since a line printed from a guessed shape is no line."""
    head = definition.split(" — ", 1)[0]

    def render_field(m):
        if m.group(1) not in fields:
            raise lib.RolesError("the governing doc's %s shape names %s, a field handoff.py agents does "
                                 "not derive" % (head, m.group(1)))
        return " ".join(str(fields[m.group(1)]).splitlines()).replace(" · ", ", ")
    return "- " + SHAPE_FIELD_RE.sub(render_field, definition)


def render_outcome(failed, status, result, files):
    """What a `returned` line says the agent produced, the first that applies: `failed` for a journal
    `failed` entry, a notification's status when it is not `completed`; `committed <sha>` or `not
    committed` for a result holding a boolean `committed`, the unit harness's verdict; else `wrote
    <n> files`, the distinct paths its write tool uses name."""
    if failed:
        return "failed"
    if status and status != "completed":
        return status
    if isinstance(result, dict) and isinstance(result.get("committed"), bool):
        sha = result.get("sha")
        return "committed %s" % sha if result["committed"] and isinstance(sha, str) else "not committed"
    return "wrote 1 file" if len(files) == 1 else "wrote %d files" % len(files)


def render_wall(seconds):
    """`45s` under a minute, `7m47s` under an hour, `1h02m` beyond; UNKNOWN for None."""
    if seconds is None:
        return UNKNOWN
    if seconds < 60:
        return "%ds" % seconds
    if seconds < 3600:
        return "%dm%02ds" % divmod(seconds, 60)
    return "%dh%02dm" % (seconds // 3600, seconds % 3600 // 60)


def render_tokens(count):
    """A count under 1000 as is, one at or above it in thousands to one decimal; UNKNOWN for None."""
    if count is None:
        return UNKNOWN
    return str(count) if count < 1000 else "%.1fk" % (count / 1000)


def write_agent_ledger(root, memory_root, build, lines):
    """Add each of `lines` (already re-rooted at the ledger's folder) whose head and last field no line
    of the ledger holds, and return one note naming what happened. The ledger is the one
    `*-agent-ledger.md` under `<MEMORY_ROOT>/builds/<build>/build/`, else it is created as
    `<today>-build-<first id>-agent-ledger.md`; its Serves line is re-derived on every write from the
    unit ids the build's specs define on their first line. Two ledgers raise RolesError naming both;
    no build, no build folder or no specced id writes nothing. The file is rewritten whole, UTF-8
    with LF line ends, only when it changes."""
    if not build:
        return "no build names these agents, so no agent ledger is written"
    bdir = root / memory_root / "builds" / build
    if not bdir.is_dir():
        return "%s does not exist, so no agent ledger is written" % bdir.relative_to(root).as_posix()
    folder = bdir / "build"
    found = sorted(folder.glob("*" + LEDGER_TAIL)) if folder.is_dir() else []
    if len(found) > 1:
        raise lib.RolesError("%s holds %d agent ledgers, %s; one build keeps one" % (
            folder.relative_to(root).as_posix(), len(found), " and ".join(p.name for p in found)))
    id_re = re.compile(r"^# ([A-Z]+)-%s-([0-9]+) — " % re.escape(build))
    ids = set()
    for p in sorted((bdir / "spec").rglob("*.md")) if (bdir / "spec").is_dir() else []:
        m = id_re.match(lib.load_text(p).split("\n", 1)[0])
        if m:
            ids.add((m.group(1), int(m.group(2))))
    if not ids:
        return ("no spec under %s/spec defines a unit id on its first line, so the ledger would serve "
                "nothing and is not written" % bdir.relative_to(root).as_posix())
    ids = ["%s-%s-%d" % (fam, build, num) for fam, num in sorted(ids)]
    path = found[0] if found else folder / ("%s-build-%s%s" % (datetime.date.today().isoformat(), ids[0],
                                                                 LEDGER_TAIL))
    serves = "**Serves:** journal " + " ".join(ids)
    old = lib.load_text(path) if path.is_file() else None
    text = re.sub(r"^\*\*Serves:\*\*.*$", lambda _: serves, old, count=1, flags=re.M) if old is not None else (
        "# %s — agent ledger\n\n%s\n\nGenerated by the roles kit's `handoff.py agents`: one line per agent "
        "dispatch and return, each added once and never edited.\n\n" % (build, serves))

    def derive_key(line):
        return line[2:].split(" — ", 1)[0], line.rsplit(" · ", 1)[-1]
    held = {derive_key(ln) for ln in text.split("\n") if ln.startswith("- ")}
    added = 0
    for line in lines:
        if derive_key(line) not in held:
            text = (text if text.endswith("\n") else text + "\n") + line + "\n"
            held.add(derive_key(line))
            added += 1
    if text == old or (old is None and not added):
        return "%s: 0 line(s) added" % path.relative_to(root).as_posix()
    folder.mkdir(exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return "%s: %d line(s) added" % (path.relative_to(root).as_posix(), added)


def print_agent_lines(root, memory_root, charter_path, session, handoff_arg, run_id, write=False):
    """Print the governing doc's `agent` line for each agent the selector names, then its `returned`
    line once it has returned, filled by name from the session's records and the role index
    (TOOL-aOrientedCast-20). When `write` is true, add each line holding no UNKNOWN
    field to the build's agent ledger; else write nothing and note the held lines and `--write`
    (TOOL-aOrientedCast-25). RolesError on a refusal, with nothing printed."""
    from render_agents import INDEX_REL  # the renderer's index path, as print_roster imports the checker's
    doc = charter_path.relative_to(root).as_posix() if root in charter_path.parents else charter_path.as_posix()
    shapes = lib.extract_microformat_shapes(lib.load_text(charter_path))
    for head in ("agent", "returned"):
        if head not in shapes:
            raise lib.RolesError("the governing doc %s defines no `%s` shape in its micro-format fence, so "
                                 "no %s line can be composed" % (doc, head, head))
    try:
        index = json.loads(lib.load_text(root / INDEX_REL))
    except ValueError as e:
        raise lib.RolesError("%s is not JSON — %s; re-render it with render_agents.py --write" % (INDEX_REL, e))
    held = index.get("roles") if isinstance(index, dict) and isinstance(index.get("roles"), dict) else {}
    try:  # TOOL-aTrimmedWait-7: no common dir reads as before, with no record
        cache_dir = common_git_dir(root) / SESSION_CACHE_DIR
    except (OSError, subprocess.CalledProcessError):
        cache_dir = None
    calls, notified, bad = load_session_calls(session, cache_dir)
    notes = ["%s: %d line(s) did not parse as JSON and were skipped" % (session.as_posix(), bad)] if bad else []
    sdir = session.with_name(session.name[:-len(".jsonl")] if session.name.endswith(".jsonl") else session.stem)

    def resolve_repo_path(value, need_file):
        p = pathlib.Path(os.path.normpath(root / value)) if isinstance(value, str) and value else None
        ok = p is not None and root in p.parents and (p.is_file() or not need_file)
        return p.relative_to(root).as_posix() if ok else None

    def read_transcript(folder, aid):  # an agent id reaches a path only in PATH_ID_RE's shape
        if PATH_ID_RE.match(aid):
            return load_agent_transcript(folder / ("agent-%s.jsonl" % aid))
        return dict(dict.fromkeys(("type", "description", "effort", "model", "wall", "tokens")), files=set())

    agents = []  # (agent id, transcript, role fallback, unit, prompt path, model fallback, returned, outcome)
    if handoff_arg is not None:
        hpath = pathlib.Path(os.path.normpath(root / handoff_arg))
        hrel = hpath.relative_to(root).as_posix() if root in hpath.parents else hpath.as_posix()
        marker = MARKER_RE.search(lib.load_text(hpath))
        if not marker:
            raise lib.RolesError("%s carries no gov:handoff marker line, so no Agent call can be matched to "
                                 "it" % hrel)
        hits = [c for c in calls if c["name"] == "Agent"
                and (m := lib.extract_prompt_marker(c["input"].get("prompt", ""))) and m.group(0) == marker.group(0)
                and isinstance(c["result"], dict) and isinstance(c["result"].get("agentId"), str)]
        if not hits:
            raise lib.RolesError("no Agent call in %s opens its prompt with the marker line of %s and has a "
                                 "result naming its agent" % (session.as_posix(), hrel))
        build, run = marker.group("build"), "direct"
        for c in hits:
            aid = c["result"]["agentId"]
            tr = read_transcript(sdir / "subagents", aid)
            unit = marker.group("unit") if marker.group("unit") != "-" else tr["description"]
            returned = c["id"] in notified or c["result"].get("status") == "completed"
            agents.append((aid, tr, marker.group("role"), unit, (hpath.name, marker.group("path")),
                           c["result"].get("resolvedModel"), returned,
                           render_outcome(False, notified.get(c["id"]), None, tr["files"])))
    else:
        journal = sdir / "subagents" / "workflows" / run_id / "journal.jsonl"
        if not journal.is_file():
            raise lib.RolesError("run %s has no journal: %s is absent" % (run_id, journal.as_posix()))
        started = load_run_journal(journal)
        wf = next((c for c in calls if c["name"] == "Workflow" and isinstance(c["result"], dict)
                   and c["result"].get("runId") == run_id), None)
        args = (wf or {}).get("input", {}).get("args")
        if isinstance(args, str):
            try:
                args = json.loads(args)
            except ValueError:
                args = None
        args = args if isinstance(args, dict) else {}
        prompt = resolve_repo_path(args.get("briefPath"), True) \
            or resolve_repo_path((wf or {}).get("input", {}).get("scriptPath"), False)
        if wf is None:
            notes.append("no Workflow call in %s has run %s, so its prompt link is unknown and its build is "
                          "the session card's" % (session.as_posix(), run_id))
        build = args.get("slug") if isinstance(args.get("slug"), str) and SLUG_RE.match(args["slug"]) else None
        if build is None and started:
            card, why = resolve_card_path(root, None)
            route = extract_card_section(lib.load_text(card), "route") if card else None
            m = re.search(r"^- build:[ \t]*(\S+)[ \t]*$", route or "", re.M)
            build = m.group(1) if m and SLUG_RE.match(m.group(1)) else None
            if build is None:
                notes.append("no build from the Workflow call's slug or the session card's last route: %s"
                             % (why or "the route names no `- build: <slug>` line"))
        if not started:
            notes.append("run %s has started no agent yet" % run_id)
        run = run_id
        for e in started:
            tr = read_transcript(sdir / "subagents" / "workflows" / run_id, e["id"])
            unit = extract_label_unit(e["label"]) or e["label"] or tr["description"]
            agents.append((e["id"], tr, None, unit, (prompt.rsplit("/", 1)[-1], prompt) if prompt else (None, None),
                           None, e["returned"], render_outcome(e["failed"], None, e["result"], tr["files"])))
    out, ledger = [], []
    for aid, tr, role_fallback, unit, (name, path), model_fallback, returned, outcome in agents:
        role = tr["type"] or role_fallback
        level = tr["effort"]
        entry = held.get(role) if isinstance(held.get(role), dict) else {}
        gates = entry.get("gates") if isinstance(entry.get("gates"), list) else []
        fields = {"role": role, "level": level, "model": tr["model"] or model_fallback, "unit-id|label": unit,
                  "name": name, "path": path,
                  "class": entry.get("writes") if isinstance(entry.get("writes"), str) and entry["writes"] else "none",
                  "legs|none": ", ".join(str(g) for g in gates) or "none", "run-id|direct": run, "agent-id": aid,
                  "outcome": outcome, "wall": render_wall(tr["wall"]), "tokens": render_tokens(tr["tokens"])}
        fields = {k: UNKNOWN if v is None or v == "" else v for k, v in fields.items()}
        for head in ("agent", "returned") if returned else ("agent",):
            used = SHAPE_FIELD_RE.findall(shapes[head])
            out.append(render_shape_line(shapes[head], fields))
            missing = [k for k in used if fields.get(k) == UNKNOWN]
            if missing:
                notes.append("run %s/%s: no record answers %s, so its %s line holds %s and stays out of the "
                             "ledger" % (run, aid, ", ".join(dict.fromkeys(missing)), head, UNKNOWN))
                continue
            folder = root / memory_root / "builds" / str(build) / "build"
            rooted = dict(fields, path=os.path.relpath(root / path, folder).replace("\\", "/")) \
                if fields["path"] != UNKNOWN else fields
            ledger.append(render_shape_line(shapes[head], rooted))
    if ledger and write:
        notes.append(write_agent_ledger(root, memory_root, build, ledger))
    elif ledger:
        notes.append("%d complete line(s) held, nothing written; pass --write to add them to the agent "
                     "ledger at a bookkeeping step, when no pass is running" % len(ledger))
    if out:
        sys.stdout.buffer.write(("\n".join(out) + "\n").encode("utf-8"))
    for line in notes:
        print("handoff: note — %s" % line, file=sys.stderr)


def main(argv):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="handoff.py", description="Render, check and map role handoffs.")
    sub = ap.add_subparsers(dest="verb", required=True)
    r = sub.add_parser("render")
    r.add_argument("--role", required=True)
    r.add_argument("--build", required=True)
    r.add_argument("--unit")
    r.add_argument("--item")
    r.add_argument("--allowance", action="append", default=[])
    r.add_argument("--card")
    r.add_argument("--input", action="append", default=[])
    r.add_argument("--upstream")
    dest = r.add_mutually_exclusive_group()
    dest.add_argument("--out")
    dest.add_argument("--stdout", action="store_true")
    dest.add_argument("--stand-in", action="store_true")
    r.add_argument("--part", choices=("full", "task"), default="full")
    fa = sub.add_parser("facts")
    fa.add_argument("--build", required=True)
    fa.add_argument("--unit")
    fa.add_argument("--input", action="append", default=[])
    sub.add_parser("harness-args").add_argument("harness")
    se = sub.add_parser("stage-efforts")
    se.add_argument("workflow")
    se.add_argument("--model")
    sub.add_parser("role-efforts").add_argument("--model")
    sub.add_parser("check").add_argument("file")
    sub.add_parser("roster")
    ag = sub.add_parser("agents")
    sel = ag.add_mutually_exclusive_group(required=True)
    sel.add_argument("--handoff")
    sel.add_argument("--run")
    ag.add_argument("--session")
    ag.add_argument("--write", action="store_true")
    a = ap.parse_args(argv)
    if a.verb == "agents" and a.run is not None and not PATH_ID_RE.match(a.run):
        ap.error("--run '%s' is not a run id of letters, digits, '_' and '-'" % a.run)
    if getattr(a, "model", None) is not None and not a.model.strip():
        ap.error("--model is empty: name the model id in use, or leave the flag off for the default levels")
    if a.verb in ("harness-args", "stage-efforts", "role-efforts"):
        try:
            if a.verb == "harness-args":
                print_harness_args(a.harness)
                return 0
            # the repository whose policy keys the levels read first (TOOL-dBoundRoles-21 S7): the
            # working directory's toplevel, else the directory itself, where the reader refuses by name
            g = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, encoding="utf-8")
            root = pathlib.Path(g.stdout.strip() if g.returncode == 0 and g.stdout.strip() else os.getcwd())
            if a.verb == "stage-efforts":
                print_stage_efforts(a.workflow, a.model, root)
            else:
                print_role_efforts(a.model, root)
            return 0
        except lib.RolesError as e:
            print("handoff: %s" % e, file=sys.stderr)
            return 1
    inputs = {}
    if a.verb == "facts" and not a.input:
        ap.error("facts: name at least one --input <name>=<value>")
    if a.verb in ("render", "facts"):
        for item in a.input:
            name, eq, value = item.partition("=")
            if not eq or name not in INPUT_NAMES or name in inputs:
                ap.error("--input %s: the name must be one of %s, given once as <name>=<value>; '%s' is not"
                         % (item, ", ".join(INPUT_NAMES), name))
            if name == "diff" and "\n" in value:
                ap.error("--input diff is one line")
            inputs[name] = value
        m = UNIT_RE.match(a.unit or "")
        if not SLUG_RE.match(a.build):
            ap.error("--build '%s' is not a slug of letters" % a.build)
        if a.unit is not None and not m:
            ap.error("--unit '%s' does not read <FAMILY>-<slug>-<digits>" % a.unit)
        if m and m.group(1) != a.build:
            ap.error("--unit %s carries the slug %s, not the build's %s: a slug mismatch"
                     % (a.unit, m.group(1), a.build))
    g = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, encoding="utf-8")
    if g.returncode != 0 or not g.stdout.strip():
        print("handoff: the working directory is in no git repository", file=sys.stderr)
        return 2
    root = pathlib.Path(g.stdout.strip())
    if a.verb == "check":
        ok, lines = check_handoff(root, a.file)
        sys.stdout.buffer.write(("\n".join(lines) + "\n").encode("utf-8"))
        return 0 if ok else 1
    conf = root / ".memory-tree.conf"
    memory_root = lib.read_conf_key(conf, "MEMORY_ROOT") if conf.is_file() else None
    try:
        if not memory_root:
            raise lib.RolesError("%s declares no MEMORY_ROOT, or is absent" % conf.as_posix())
        # the roster reads no charter: on a first install the playbook render writes it
        charter_path = None if a.verb in ("roster", "facts") else lib.resolve_charter_path(root)
    except lib.RolesError as e:
        print("handoff: %s" % e, file=sys.stderr)
        return 2
    if a.verb == "agents":
        from render_agents import INDEX_REL
        session, why = resolve_session_file(root, a.session)
        if session is None or not (root / INDEX_REL).is_file():
            print("handoff: %s" % (why or "%s is absent, so no line can name a role's write class or gate "
                                         "legs; render it with render_agents.py --write" % INDEX_REL),
                  file=sys.stderr)
            return 2
        try:
            print_agent_lines(root, memory_root, charter_path, session, a.handoff, a.run, a.write)
        except lib.RolesError as e:
            print("\n".join("handoff: " + ln for ln in str(e).split("\n")), file=sys.stderr)
            return 1
        return 0
    try:
        if a.verb == "roster":
            print_roster(memory_root)
            return 0
        if a.verb == "facts":
            print_input_facts(root, memory_root, a.build, inputs)
            return 0
        roles = lib.load_roles(KIT_DIR)
        if a.role not in roles:
            raise lib.RolesError("no role '%s' in the catalogue; its slots are %s" % (a.role, ", ".join(roles)))
        keys = roles[a.role]["keys"]
        read = {lib.parse_read_key(x)[0] for x in keys.get("reads", "").split(",") if x.strip()}
        for name in inputs:
            if name not in ("prompt", CODE_INPUT) and "input:" + name not in read:
                ap.error("input:%s is a key %s does not read" % (name, a.role))
        if a.upstream and UPSTREAM_KEY not in read:
            ap.error("--upstream: %s is a key %s does not read" % (UPSTREAM_KEY, a.role))
        prompts = root / memory_root / "builds" / a.build / "prompts"
        out = a.out and pathlib.Path(os.path.normpath(root / a.out))
        if out and prompts not in out.parents:
            ap.error("--out %s is not under %s, the only folder the spawn guard admits a marker in"
                     % (a.out, prompts.relative_to(root).as_posix()))
        if a.stand_in:
            waivers, bad = lib.load_stand_in_waivers(root, memory_root, roles)
            if (a.build, a.role) not in waivers:
                raise lib.RolesError("\n".join([
                    "--stand-in: no valid row in %s/project/%s waives role %s in build %s, so this "
                    "stand-in is not the owner's; the owner adds the TAB-separated row "
                    "'<date> owner <who> %s %s <reason>'" % (memory_root, lib.STAND_IN_WAIVER, a.role,
                                                               a.build, a.role, a.build)] + bad))
        notes = []
        path, text, task_part = render_handoff(root, memory_root, charter_path, a.role, keys, a.build,
                                               a.unit, a.card, inputs, out, notes,
                                               lib.STAND_IN_TAIL if a.stand_in else "", a.upstream, item=a.item,
                                               allowance=a.allowance)
        for line in notes:
            print("handoff: note — %s" % line, file=sys.stderr)
        if not a.stand_in:
            print("handoff: description — %s" % render_spawn_name(a.build, a.unit, keys["workflow"]),
                  file=sys.stderr)
    except lib.RolesError as e:
        print("\n".join("handoff: " + ln for ln in str(e).split("\n")), file=sys.stderr)
        return 1
    if not a.stdout:
        path.parent.mkdir(exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
    shown = task_part if a.part == "task" else (text if a.stdout else path.relative_to(root).as_posix() + "\n")
    sys.stdout.buffer.write(shown.encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
