#!/usr/bin/env python3
"""handoff.py — a role and one task's inputs, rendered into one hashed prompt file (TOOL-aOrientedCast-2).

    python handoff.py render --role <name> --build <slug> [--unit <id>] [--card <path>]
                             [--input <key>=<value>]... [--out <path> | --stdout | --stand-in]
                             [--part full|task]
    python handoff.py harness-args <harness>
    python handoff.py stage-efforts <workflow>
    python handoff.py check <file>
    python handoff.py roster
    python handoff.py agents (--handoff <path> | --run <run-id>) [--session <file>] [--write]

`render` composes the role as `roles_lib.render_role` renders it with a task block holding exactly
the inputs the role's `reads` declares, in that order, then `roles_lib.render_charter_blocks` for
the role as the last block: the section 1 rule lines its `rules` tags cite and the charter's carried
sections (TOOL-aOrientedCast-16), each library note printed on stderr as `handoff: note — `. It writes
the file under the build's `prompts/` folder, printing its repo-relative path. `--part task` prints
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
The marker carries two hashes, each the first 12 hex digits of the SHA-256 of one section's bytes
with CRLF folded to LF: `## Role` up to the byte before the `## Task` line, and `## Task` to the end
of the file. `check` re-derives both and compares the marker's `path` with the file's own.
`harness-args` prints, as one line of sorted JSON, the union of the `stages` tables of every
workflow whose harness names that script. `stage-efforts` prints, the same way, the reasoning effort
`house/policy.toml` resolves for every stage key of ONE workflow's `stages` table: a harness call
passes it as its `efforts` argument (TOOL-aOrientedCast-10). `roster` prints the charter's roles
section, one line per role, ``- `<slot>`: <description> <when>. Output: <output>.``, where `<when>`
is `Optional` for a `mandatory` of `no`, `Optional, <text>` for `no — <text>`, else `Mandatory
<value>`, `{{MEMORY_ROOT}}` is the conf's value, and the order is the workflow table's; a line past
200 characters, a missing key or an empty catalogue refuses with nothing printed. It reads no
charter (TOOL-aOrientedCast-17).

`agents` prints the governing doc's `agent` line for each agent its selector names, then its
`returned` line once it has returned, each shape read from the doc's micro-format fence and filled
by placeholder name from the session's own records, the role index and the agent types; a field
nothing answers prints `unknown` (TOOL-aOrientedCast-20). `--handoff` names a direct spawn, every
`Agent` call whose prompt opens with the file's marker line as the hooks kit's spawn guard reads it,
through `roles_lib.extract_prompt_marker` (TOOL-aOrientedCast-25); `--run` a harness run, one agent
per `started` entry of its journal. The session is `--session`, else the transcript
CLAUDE_CODE_SESSION_ID names. A harness agent's unit is the one unit id its journal label names, else
the label (TOOL-aOrientedCast-27). With `--write`, each line holding no `unknown` is added, once, to the
build's one `<MEMORY_ROOT>/builds/<build>/build/*-agent-ledger.md`, its prompt link re-rooted at
that folder; without it nothing is written and one note names the held lines and `--write`, so a
mid-pass call leaves the tree as it found it. Pass `--write` only at a bookkeeping step, when no
pass is running.

Sources, by key family: `task:` the card's `## task` field, read by the kickoff checker's grammar
(stated above its `check_card_task`, and ported here because that one is shell) under the labels
that checker's `--task-skeleton` prints, so a skeleton that does not yield eight refuses; `card:` the lines
under the card's last `## <heading>`; `brief:` the `### <sub-head>` under the brief record's
`## The brief`; `input:` the `--input` argument; a rule tag the governing doc's section 1. The card is
`--card`, else the file the kickoff checker's `--card --path` prints for CLAUDE_CODE_SESSION_ID, so
the card's location stays that checker's rule. A required key resolving to nothing, an empty value
or a placeholder refuses and writes nothing; an optional one is named on the `Not supplied` line.
A relative path given to `--card`, `--out`, an `--input` or `check` is read from the repository root.

Exit 0 on success, 1 on a refusal naming its key, file, role or missing waiver row, 2 on usage or an unarmed
environment: no repository, no MEMORY_ROOT, no CHARTER (`roster` needs no CHARTER). `agents` exits 1
on no marker in the handoff, no matching call, no run journal, a missing shape, an underived
placeholder or two ledgers in one build, and 2 with no session file or role index as well.

WHAT THIS DOES NOT CHECK: whether a card or brief value says anything true, since a value present,
single and not a placeholder is copied verbatim; whether a rendered role is current against the
catalogue, since `check` hashes the file's own bytes and nothing more; and whether a secret sits in
a card or a brief, which the charter's `[security]` rule guards and this script does not. For
`agents`: the transcript format is no contract, so a renamed field reads as `unknown`; an `effort`
or a `model` is what the transcript records, not proved to be what the API applied; a file written
through Bash is not counted as written; the session read may not be the one the build ran in; and
a ledger line edited by hand passes, since nothing re-derives the ledger.
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
INPUT_NAMES = ("spec", "diff", "question", "prompt")
PATH_INPUTS = ("spec", "prompt")
PLACEHOLDERS = ("…", "...", "tbd", "todo", "n/a", "none", "-", "?")
KICKOFF_HOME, KICKOFF_CHECKER = "session-kickoff", "manifest-check.sh"
CHECKER_BOUND_S = 30
SLUG_RE = lib.SLUG_RE
UNIT_RE = re.compile(r"^[A-Z]+-([A-Za-z]+)-[0-9]+$")
READY_RE = re.compile(r"^(- )?READY — ")
BLANK_EDGES_RE = re.compile(r"\A\s*\n|\n\s*\Z")
MARKER_RE = lib.MARKER_RE
ROLE_HEAD_RE, TASK_HEAD_RE = re.compile(r"^## Role$", re.M), re.compile(r"^## Task$", re.M)
PROMPT_HEAD_RE = re.compile(r"^## The prompt[ \t]*$", re.M)
BRIEF_HEAD_RE = re.compile(r"^## The brief[ \t]*$", re.M)
# ponytail: the playbook's one-line region refuses a rendered rule past 200 characters; spelled
# again because a kit file may not import a sibling kit. A drift fails closed either way.
ROSTER_LINE_MAX = 200
#: `agents` (TOOL-aOrientedCast-20): the ledger's file-name tail, the value of a field nothing
#: answers, and the tool uses whose paths a `returned` line counts as written.
LEDGER_TAIL = "-agent-ledger.md"
UNKNOWN = "unknown"
WRITE_TOOLS = ("Write", "Edit", "MultiEdit", "NotebookEdit")
SESSION_ID_RE = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
#: A run id or an agent id reaches a path only in this shape; so does a role naming an agent type.
PATH_ID_RE = re.compile(r"^[A-Za-z0-9_-]{1,64}$")
LABEL_UNIT_RE = re.compile(r"[A-Z]+-[A-Za-z]+-[0-9]+")
EFFORT_LINE_RE = re.compile(r"^effort:[ \t]*(\S+)$", re.M)
SHAPE_FIELD_RE = re.compile(r"<([^<>]+)>")
NOTIFICATION_RE = re.compile(r"<task-notification>(.*?)</task-notification>", re.S)
#: The session file's lines worth parsing: every other line is skipped unparsed, by its bytes.
SESSION_LINE_TOKENS = (b'"Agent"', b'"Workflow"', b"toolUseResult", b"task-notification")


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
    verbatim with blank edges trimmed; None when the card has no such heading."""
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


def resolve_bash():
    """GOV_BASH, else the first bash on PATH that is not a System32 or WindowsApps launcher, which on
    Windows sees another filesystem (the different-shell gotcha class); None when none is found.
    ponytail: existence only, no run probe — the one call made with it is the probe, and its failure
    leaves the card absent and named."""
    if os.environ.get("GOV_BASH"):
        return os.environ["GOV_BASH"]
    for d in os.environ.get("PATH", "").split(os.pathsep):
        for name in ("bash.exe", "bash"):
            cand = os.path.join(d, name)
            low = cand.replace("\\", "/").lower()
            if os.path.isfile(cand) and "/system32/" not in low and "/windowsapps/" not in low:
                return cand
    return None


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


def derive_section_sha(section):
    """The first 12 lowercase hex digits of the SHA-256 of a section's bytes, CRLF folded to LF."""
    return hashlib.sha256(section.replace("\r\n", "\n").encode("utf-8")).hexdigest()[:12]


def render_handoff(root, memory_root, charter_path, role, keys, slug, unit, card_arg, inputs, out_path,
                   notes=None, tail=""):
    """`(path, text, task_part)` of the prompt file; raises RolesError naming every key that refused.
    The charter library's notes are appended to `notes` when a list is given; `tail` goes before
    the derived name's `.md`."""
    build_dir = root / memory_root / "builds" / slug
    if not build_dir.is_dir():
        raise lib.RolesError("the build folder %s does not exist" % build_dir.as_posix())
    unit_id = unit
    if unit_id is None:
        fm = lib.FRONT_MATTER_RE.match(lib.load_text(build_dir / "README.md")) \
            if (build_dir / "README.md").is_file() else None
        ids = re.search(r"^ids:[ \t]*(\S+)", fm.group(1), re.M) if fm else None
        if not ids:
            raise lib.RolesError("no --unit, and %s/README.md names no ids: in its front matter"
                                 % build_dir.as_posix())
        unit_id = ids.group(1)
    values, refusals = {}, []
    for name, v in inputs.items():
        if name in PATH_INPUTS and v:
            p = pathlib.Path(os.path.normpath(root / v))
            if root not in p.parents or not p.is_file():
                raise lib.RolesError("input:%s — %s names no file inside the repository" % (name, v))
            v = p.relative_to(root).as_posix()
        values["input:" + name] = v.replace("\r\n", "\n")
    reads = [x.strip() for x in keys.get("reads", "").split(",") if x.strip()]
    card = brief = None
    why, labels = {}, {}
    if any(k.startswith("task:") for k in reads):
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
    if any(k.startswith(("task:", "card:")) for k in reads):
        card, why["card"] = resolve_card_path(root, card_arg)
        card_text = lib.load_text(card) if card else ""
        values.update(("task:" + f, v) for f, v in extract_task_fields(card_text, labels).items())
        for k in reads:
            if k.startswith("card:") and card:
                section = extract_card_section(card_text, k.rstrip("?")[5:])
                if section is not None:
                    values[k.rstrip("?")] = section
    if any(k.startswith("brief:") for k in reads):
        prompts = build_dir / "prompts"
        brief = resolve_brief_record(prompts, values.get("input:prompt") and root / values["input:prompt"])
        why["brief record"] = None if brief else (
            "no file under %s carries both a '## The prompt' and a '## The brief' line" % prompts.as_posix())
        brief_text = lib.load_text(brief) if brief else ""
        for k in reads:
            if k.startswith("brief:") and brief:
                section = extract_brief_section(brief_text, k.rstrip("?")[6:])
                if section is not None:
                    values[k.rstrip("?")] = section
    sources = {"task": ("card", card), "card": ("card", card), "brief": ("brief record", brief),
               "input": ("arguments", None)}
    blocks, absent, reasons = [], [], []
    for k in reads:
        key = k.rstrip("?")
        v = BLANK_EDGES_RE.sub("", values.get(key, ""))
        if not check_placeholder(v):
            blocks.append("### %s\n\n%s" % (key, v))
            continue
        src, path = sources[key.split(":")[0]]
        what = ("no %s: %s" % (src, why[src])) if why.get(src) else (
            "the %s %s carries no single filled value for it: absent, repeated, empty or a placeholder"
            % (src, path.as_posix()) if path else "not supplied; pass --input %s=<value>" % key[6:])
        if not k.endswith("?"):
            refusals.append("%s — %s" % (key, what))
        else:
            absent.append(key)
            reasons += [what] if why.get(src) and what not in reasons else []
    doc = charter_path.relative_to(root).as_posix() if root in charter_path.parents else charter_path.as_posix()
    charter = lib.parse_charter(lib.load_text(charter_path), doc)
    if charter["shape"] == "legacy" and notes is not None:
        notes.append(lib.LEGACY_NOTE % doc)
    try:
        charter_blocks = lib.render_charter_blocks(
            charter, (KIT_DIR / "agents" / (role + ".agent.md")).as_posix(), keys.get("rules", ""), notes)
    except lib.RolesError as e:
        refusals += str(e).split("\n")
    else:
        blocks += [charter_blocks.rstrip("\n")] if charter_blocks else []
    if refusals:
        raise lib.RolesError("\n".join(refusals))
    opening = ("This handoff is for build `%s`, unit `%s`." % (slug, unit_id) if unit
               else "This handoff is for build `%s`, and names no single unit." % slug)
    if absent:
        opening += "\nNot supplied, optional: %s%s." % (
            ", ".join("`%s`" % k for k in absent), " — " + "; ".join(reasons) if reasons else "")
    role_sec = "## Role\n\n%s\n\n" % lib.render_role(KIT_DIR, role, memory_root).strip("\n")
    task_sec = "\n\n".join(["## Task", opening] + blocks) + "\n"
    path = out_path or build_dir / "prompts" / derive_prompt_name(
        build_dir / "prompts", datetime.date.today().isoformat(), unit_id, role, tail)
    rel = path.relative_to(root).as_posix()
    marker = "<!-- gov:handoff role=%s build=%s unit=%s path=%s role-sha=%s task-sha=%s -->" % (
        role, slug, unit or "-", rel, derive_section_sha(role_sec), derive_section_sha(task_sec))
    head = "**Serves:** journal %s\n\n# %s handoff — %s\n\n%s\n\n" % (unit_id, role, unit_id, marker)
    return path, head + role_sec + task_sec, marker + "\n\n" + task_sec


def check_handoff(root, path):
    """`(ok, lines)`: the marker's two hashes re-derived from the file's own bytes, CRLF folded, and
    its `path` compared with the file's repo-relative path; one line per mismatch, else one line
    naming the path and both hashes."""
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
    role_sha = derive_section_sha(text[role_m.start():task_m.start()])
    task_sha = derive_section_sha(text[task_m.start():])
    bad = ["handoff: %s: %s — the marker says %s, the file gives %s" % (rel, what, said, actual)
           for what, said, actual in (("role-sha", marker.group(5), role_sha),
                                      ("task-sha", marker.group(6), task_sha),
                                      ("path", marker.group(4), rel))
           if said != actual]
    return not bad, bad or ["%s role-sha=%s task-sha=%s" % (rel, role_sha, task_sha)]


def print_harness_args(harness):
    """Print the union of the `stages` tables of every workflow whose harness path ends in the script
    `harness` (its file name without extension) as one line of sorted JSON; RolesError when no
    workflow's harness carries it or one stage key maps to two roles."""
    union, hit = {}, False
    for w in lib.load_workflows(KIT_DIR):
        tokens = [t for t in str(w.get("harness", "")).split() if "/" in t]
        if not any(t.rsplit("/", 1)[-1].rsplit(".", 1)[0] == harness for t in tokens):
            continue
        hit = True
        for key, slot in (w.get("stages") or {}).items():
            if union.get(key, slot) != slot:
                raise lib.RolesError("stage key %s maps to both %s and %s across the workflows of %s"
                                     % (key, union[key], slot, harness))
            union[key] = slot
    if not hit:
        raise lib.RolesError("no workflow's harness is the script %s" % harness)
    sys.stdout.buffer.write((json.dumps(union, sort_keys=True, separators=(",", ":"),
                                        ensure_ascii=False) + "\n").encode("utf-8"))


def print_stage_efforts(workflow):
    """Print the resolved level of every stage key of one workflow's `stages` table as one line of
    sorted JSON (TOOL-aOrientedCast-10); RolesError on an unknown name, a workflow with no `stages`
    table, or a policy defect. Keyed by workflow, not harness: a harness serving two workflows runs
    one role at two levels, which a union cannot carry."""
    workflows = lib.load_workflows(KIT_DIR)
    policy = lib.load_policy(KIT_DIR, lib.load_roles(KIT_DIR), workflows)
    entry = next((w for w in workflows if w.get("name") == workflow), None)
    if entry is None:
        raise lib.RolesError("no workflow named %s in workflows.toml" % workflow)
    if not isinstance(entry.get("stages"), dict):
        raise lib.RolesError("the workflow %s has no stages table, so no harness stage takes a level"
                             % workflow)
    sys.stdout.buffer.write((json.dumps(lib.resolve_stage_efforts(policy, entry), sort_keys=True,
                                        separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8"))


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
            warned.append("BUDGET WARN — roster-line · %s · %d chars over %d · %s" % (slot, len(line), cap, rule))
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


def load_session_calls(path):
    """`(calls, notified, bad)` of one session file, read once, line by line. `calls` holds each
    `Agent` and `Workflow` call as `{"id", "name", "input", "result"}` in call order, `result` its
    record's `toolUseResult` or None; `notified` maps a tool-use id to the `<status>` (None when it
    carries none) of a `<task-notification>` naming it, delivered in a user record or still queued
    in a `queued_command` attachment or a `queue-operation` record; `bad` counts the lines that did
    not parse. Only a line whose bytes carry one of SESSION_LINE_TOKENS is parsed."""
    calls, by_id, notified, bad = [], {}, {}, 0
    with open(path, "rb") as fh:
        for raw in fh:
            if not any(t in raw for t in SESSION_LINE_TOKENS):
                continue
            try:
                rec = json.loads(raw)
            except (ValueError, RecursionError):
                rec = None
            if not isinstance(rec, dict):
                bad += 1
                continue
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
    return calls, notified, bad


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
    line once it has returned, filled by name from the session's records, the role index and the
    agent types (TOOL-aOrientedCast-20). When `write` is true, add each line holding no UNKNOWN
    field to the build's agent ledger; else write nothing and note the held lines and `--write`
    (TOOL-aOrientedCast-25). RolesError on a refusal, with nothing printed."""
    from render_agents import AGENTS_REL, INDEX_REL  # the renderer's two paths, as print_roster imports the checker's
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
    calls, notified, bad = load_session_calls(session)
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
        build, run = marker.group(2), "direct"
        for c in hits:
            aid = c["result"]["agentId"]
            tr = read_transcript(sdir / "subagents", aid)
            unit = marker.group(3) if marker.group(3) != "-" else tr["description"]
            returned = c["id"] in notified or c["result"].get("status") == "completed"
            agents.append((aid, tr, marker.group(1), unit, (hpath.name, marker.group(4)),
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
        if level is None and role and PATH_ID_RE.match(role) and (root / AGENTS_REL / (role + ".md")).is_file():
            fm = lib.FRONT_MATTER_RE.match(lib.load_text(root / AGENTS_REL / (role + ".md")))
            hit = EFFORT_LINE_RE.search(fm.group(1)) if fm else None
            level = hit.group(1) if hit else None
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
    r.add_argument("--card")
    r.add_argument("--input", action="append", default=[])
    dest = r.add_mutually_exclusive_group()
    dest.add_argument("--out")
    dest.add_argument("--stdout", action="store_true")
    dest.add_argument("--stand-in", action="store_true")
    r.add_argument("--part", choices=("full", "task"), default="full")
    sub.add_parser("harness-args").add_argument("harness")
    sub.add_parser("stage-efforts").add_argument("workflow")
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
    if a.verb in ("harness-args", "stage-efforts"):
        try:
            if a.verb == "harness-args":
                print_harness_args(a.harness)
            else:
                print_stage_efforts(a.workflow)
            return 0
        except lib.RolesError as e:
            print("handoff: %s" % e, file=sys.stderr)
            return 1
    inputs = {}
    if a.verb == "render":
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
        charter_path = None if a.verb == "roster" else lib.resolve_charter_path(root)
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
        roles = lib.load_roles(KIT_DIR)
        if a.role not in roles:
            raise lib.RolesError("no role '%s' in the catalogue; its slots are %s" % (a.role, ", ".join(roles)))
        keys = roles[a.role]["keys"]
        read = {x.strip().rstrip("?") for x in keys.get("reads", "").split(",")}
        for name in inputs:
            if name != "prompt" and "input:" + name not in read:
                ap.error("input:%s is a key %s does not read" % (name, a.role))
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
                                               lib.STAND_IN_TAIL if a.stand_in else "")
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
