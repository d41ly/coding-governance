#!/usr/bin/env python3
"""handoff.py — a role and one task's inputs, rendered into one hashed prompt file (TOOL-aOrientedCast-2).

    python handoff.py render --role <name> --build <slug> [--unit <id>] [--card <path>]
                             [--input <key>=<value>]... [--out <path> | --stdout] [--part full|task]
    python handoff.py harness-args <harness>
    python handoff.py check <file>

`render` composes the role as `roles_lib.render_role` renders it with a task block holding exactly
the inputs the role's `reads` declares, in that order, then one block per `charter` id, and writes
the file under the build's `prompts/` folder, printing its repo-relative path. `--part task` prints
the marker line, a blank line and the `## Task` section instead; `--stdout` writes nothing and prints.
The marker carries two hashes, each the first 12 hex digits of the SHA-256 of one section's bytes
with CRLF folded to LF: `## Role` up to the byte before the `## Task` line, and `## Task` to the end
of the file. `check` re-derives both and compares the marker's `path` with the file's own.
`harness-args` prints, as one line of sorted JSON, the union of the `stages` tables of every
workflow whose harness names that script.

Sources, by key family: `task:` the card's `## task` field, read by the kickoff checker's grammar
(stated above its `check_card_task`, and ported here because that one is shell); `card:` the lines
under the card's last `## <heading>`; `brief:` the `### <sub-head>` under the brief record's
`## The brief`; `input:` the `--input` argument; a charter id the governing doc's section. The card is
`--card`, else the file the kickoff checker's `--card --path` prints for CLAUDE_CODE_SESSION_ID, so
the card's location stays that checker's rule. A required key resolving to nothing, an empty value
or a placeholder refuses and writes nothing; an optional one is named on the `Not supplied` line.
A relative path given to `--card`, `--out`, an `--input` or `check` is read from the repository root.

Exit 0 on success, 1 on a refusal naming its key, file or role, 2 on usage or an unarmed
environment: no repository, no MEMORY_ROOT, no CHARTER.

WHAT THIS DOES NOT CHECK: whether a card or brief value says anything true, since a value present,
single and not a placeholder is copied verbatim; whether a rendered role is current against the
catalogue, since `check` hashes the file's own bytes and nothing more; and whether a secret sits in
a card or a brief, which the charter's §5 rule guards and this script does not.
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

#: The build's interface 6: a `task:` field and its card label, as the kickoff grammar extracts it.
TASK_LABELS = {"title": "Title", "goal": "Goal (1–2 sentences)", "in": "IN scope",
               "out": "OUT / non-goals", "todo": "To-do", "reuse": "Reuse",
               "acceptance": "Acceptance check", "gates": "Gates it must pass"}
INPUT_NAMES = ("spec", "diff", "question", "prompt")
PATH_INPUTS = ("spec", "prompt")
PLACEHOLDERS = ("…", "...", "tbd", "todo", "n/a", "none", "-", "?")
KICKOFF_HOME, KICKOFF_CHECKER = "session-kickoff", "manifest-check.sh"
CHECKER_BOUND_S = 30
SLUG_RE = re.compile(r"^[A-Za-z]+$")
UNIT_RE = re.compile(r"^[A-Z]+-([A-Za-z]+)-[0-9]+$")
READY_RE = re.compile(r"^(- )?READY — ")
BLANK_EDGES_RE = re.compile(r"\A\s*\n|\n\s*\Z")
MARKER_RE = re.compile(r"^<!-- gov:handoff role=(\S+) build=(\S+) unit=(\S+) path=(\S+) "
                       r"role-sha=([0-9a-f]{12}) task-sha=([0-9a-f]{12}) -->$", re.M)
ROLE_HEAD_RE, TASK_HEAD_RE = re.compile(r"^## Role$", re.M), re.compile(r"^## Task$", re.M)
PROMPT_HEAD_RE = re.compile(r"^## The prompt[ \t]*$", re.M)
BRIEF_HEAD_RE = re.compile(r"^## The brief[ \t]*$", re.M)


def check_placeholder(value):
    """True when a value is empty or a placeholder by the kickoff grammar: whitespace collapsed, one of
    … ... tbd todo n/a none - ? in any case, only `.` and `…`, or one `<slot>` with no inner bracket."""
    v = " ".join(value.split())
    return (v.lower() in PLACEHOLDERS or not v.replace(".", "").replace("…", "")
            or re.fullmatch(r"<[^<>]*>", v) is not None)


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


def extract_task_fields(text):
    """`{field: value}` for each interface-6 field the card's `## task` carries exactly once.

    The kickoff checker's grammar: a line loses its leading whitespace, its `>` run and one `- ` or
    `* `; a line then opening `<!--` or `UNVERIFIED — ` is skipped; a line opening `**` is a field
    whose label runs to the first `:**` when that precedes the first closing `**`, else to that
    `**`, and its value is the rest plus each line up to the next field line. The value keeps its
    line breaks; it is trimmed and loses one leading balanced `(…)` qualifier and one leading `:`.
    A field absent or repeated is left out; emptiness and placeholders are the caller's verdict.
    """
    section = extract_card_section(text, "task")
    by_label = {label: field for field, label in TASK_LABELS.items()}
    raw, count, cur = {}, {}, None
    for line in (section or "").split("\n"):
        s = re.sub(r"^[-*] ", "", re.sub(r"^(> ?)+", "", line.lstrip()))
        if s.startswith(("<!--", "UNVERIFIED — ")):
            continue
        rest, b = s[2:], s[2:].find("**")
        if s.startswith("**") and b >= 0:
            k = rest.find(":**")
            label, tail = (rest[:k], rest[k + 3:]) if 0 <= k < b else (rest[:b], rest[b + 2:])
            cur = by_label.get(label.strip())
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


def derive_prompt_name(prompts_dir, date, unit_id, role):
    """`<date>-prompt-<id>-<n>-<role without gov->.md`, `<n>` one above the highest that date and id
    already use under the folder, by any role, so the derived path never overwrites a file."""
    stem = "%s-prompt-%s-" % (date, unit_id)
    seq_re = re.compile(re.escape(stem) + r"([0-9]+)-")
    used = [int(m.group(1)) for p in prompts_dir.glob(stem + "*") if (m := seq_re.match(p.name))]
    return "%s%d-%s.md" % (stem, max(used, default=0) + 1, role[4:] if role.startswith("gov-") else role)


def derive_section_sha(section):
    """The first 12 lowercase hex digits of the SHA-256 of a section's bytes, CRLF folded to LF."""
    return hashlib.sha256(section.replace("\r\n", "\n").encode("utf-8")).hexdigest()[:12]


def render_handoff(root, memory_root, charter_path, role, keys, slug, unit, card_arg, inputs, out_path):
    """`(path, text, task_part)` of the prompt file; raises RolesError naming every key that refused."""
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
    why = {}
    if any(k.startswith(("task:", "card:")) for k in reads):
        card, why["card"] = resolve_card_path(root, card_arg)
        card_text = lib.load_text(card) if card else ""
        values.update(("task:" + f, v) for f, v in extract_task_fields(card_text).items())
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
    sections = lib.extract_charter_sections(lib.load_text(charter_path))
    for cid in [x.strip() for x in keys.get("charter", "").split(",") if x.strip()]:
        if cid not in sections:
            refusals.append("charter %s — names no section of %s" % (cid, charter_path.as_posix()))
        else:
            blocks.append("### charter %s\n\n%s" % (cid, sections[cid]))
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
        build_dir / "prompts", datetime.date.today().isoformat(), unit_id, role)
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
    r.add_argument("--part", choices=("full", "task"), default="full")
    sub.add_parser("harness-args").add_argument("harness")
    sub.add_parser("check").add_argument("file")
    a = ap.parse_args(argv)
    if a.verb == "harness-args":
        try:
            print_harness_args(a.harness)
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
        charter_path = lib.resolve_charter_path(root)
    except lib.RolesError as e:
        print("handoff: %s" % e, file=sys.stderr)
        return 2
    try:
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
        path, text, task_part = render_handoff(root, memory_root, charter_path, a.role, keys, a.build,
                                               a.unit, a.card, inputs, out)
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
