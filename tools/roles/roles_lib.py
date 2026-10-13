"""roles_lib — the one reader of the role catalogue, and the one composition of a role (TOOL-aOrientedCast-1).

Reads the role files under `agents/`, the workflow table `workflows.toml`, the memory-tree conf and
the governing doc: its section 1 rule tags and its carried sections (TOOL-aOrientedCast-16). It is
also the one reader of the owner's stand-in waiver registry and of the stand-in declarations under
the builds' `prompts/` folders (TOOL-aOrientedCast-19), and of the governing doc's micro-format
fence, `<!-- microformats -->` to `<!-- /microformats -->`, whose `agent` and `returned` shapes
`handoff.py agents` fills (TOOL-aOrientedCast-20): each marker a whole line and the last definition
of a head winning, as the hooks kit's format guard reads the fence (TOOL-aOrientedCast-25). Its
`extract_prompt_marker` reads an `Agent` prompt's marker line as the hooks kit's spawn guard does.
`render_role` is the one composition of a role with its house overlay, and `render_charter_blocks`
the one composition of the charter text a role carries: every consumer that hands a role to an agent
calls both, so a role reaches an agent the same way by every route. Stdlib only; every text read
folds CRLF to LF and names its encoding.

The front-matter grammar: a `---` block at line 1, one `key: value` per line at COLUMN 0, values kept
RAW (a list is comma-separated on one line, the form Claude Code's own `tools:` takes). An indented,
a repeated or an unknown key is refused, because a simple parser drops an indented key without a
word and a repeated one silently keeps the last.
"""
import datetime
import json
import pathlib
import re
import tomllib

KIT_ROLES_VERSION = "1.5"

#: Every front-matter key a role file may carry: Claude Code's own, then gov's.
#: Split from one string, because a quoted `"tools"` beside a quoted segment reads to the
#: install-prefix ban as a kit path (TOOL-aOrientedCast-8 S14).
FRONT_MATTER_KEYS = tuple("name description tools model maxTurns "
                          "workflow reads writes rules returns agent mandatory output".split())

#: The closed `reads` vocabulary: `<family>:<field>`, a trailing `?` marking one optional.
READ_KEYS = frozenset(
    ["task:" + f for f in ("title", "goal", "in", "out", "todo", "reuse", "acceptance", "gates")]
    + ["card:" + f for f in ("route", "records", "classes", "read", "open", "reuse")]
    + ["brief:" + f for f in ("goal", "items", "acceptance", "gates", "non-goals")]
    + ["input:" + f for f in ("spec", "diff", "question", "prompt")])

#: The reasoning-effort levels a role or a stage may take (TOOL-aOrientedCast-10). Read from Claude
#: Code 2.1.292, whose agent loader and `Workflow` `agent()` options both take these five names; the
#: integer form only the loader accepts is refused, so one level is legal on both carriers.
EFFORT_LEVELS = tuple("low medium high xhigh max".split())
POLICY_EFFORT_KEYS = ("default", "roles", "stages")
#: The policy file's tables (TOOL-aOrientedCast-11 adds `gates`).
POLICY_TABLES = ("effort", "gates")
#: The gate manifest's file name under the tool root: the leg list the merge-bar runner reads.
GATE_MANIFEST = "gate-legs.json"

#: The only render token a role body or an overlay may carry.
MEMORY_ROOT_TOKEN = "{{MEMORY_ROOT}}"
TOKEN_RE = re.compile(r"\{\{[^{}]*\}\}")
FRONT_MATTER_RE = re.compile(r"---[ \t]*\n(.*?)\n---[ \t]*(?:\n|$)", re.S)
CONF_LINE_RE = re.compile(
    r"^\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)=(?:\"([^\"]*)\"|'([^']*)'|(\S*))(?:\s+#.*)?\s*$")
#: The playbook render's region markers. A charter rendered into a larger file sits between them,
#: and only that span is read, so an adopter's own sections around it never reach an agent.
PLAYBOOK_OPEN, PLAYBOOK_CLOSE = "<!-- gov:playbook -->", "<!-- /gov:playbook -->"
SECTION_ONE_RE = re.compile(r"^## 1\. ")
#: A section 1 rule line, `- [<tag>] <text>`; the whole line is the rule.
RULE_LINE_RE = re.compile(r"^- \[([a-z0-9][a-z0-9-]*)\] ")
#: One entry of a role's `rules` value: a tag, a trailing `?` marking it optional.
RULE_KEY_RE = re.compile(r"^[a-z0-9][a-z0-9-]*\??$")
#: The section 3 headings every agent type and handoff carries whole, in this order (§8 F3).
CARRIED_SECTIONS = ("Protocols", "Facts")
#: A v3.x charter's numbered heading, kept only to tell a pre-tag charter from an unknown doc.
SECTION_RE = re.compile(r"^## (§\d+) — ")
LEGACY_NOTE = ("%s is a pre-tag charter: it carries `## §<n> — ` headings and no section 1 rule tag, "
               "so no role's rules resolve and no agent type or handoff carries the charter; reseed "
               "the charter template from gov, then re-render")
HARNESS_RE = re.compile(r"^\{prefix\}/([^/{}\s]+)/([^/{}\s]+)$")
#: A build slug, as `handoff.py render --build` takes it and a stand-in waiver row names it.
SLUG_RE = re.compile(r"^[A-Za-z]+$")
#: The rendered handoff's marker line; `handoff.py` reads this one pattern (TOOL-aOrientedCast-19).
MARKER_RE = re.compile(r"^<!-- gov:handoff role=(\S+) build=(\S+) unit=(\S+) path=(\S+) "
                       r"role-sha=([0-9a-f]{12}) task-sha=([0-9a-f]{12}) -->$", re.M)
#: The owner's stand-in waiver registry under `<MEMORY_ROOT>/project/`, and the file-name tail a
#: handoff rendered by a stand-in carries before `.md` (TOOL-aOrientedCast-19).
STAND_IN_WAIVER = "role-stand-in-waiver.txt"
STAND_IN_TAIL = "-stand-in"
WAIVER_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
WAIVER_OWNER_RE = re.compile(r"^owner \S+$")
#: The governing doc's micro-format fence and one definition line inside it (TOOL-aOrientedCast-20).
MICROFORMATS_OPEN, MICROFORMATS_CLOSE = "<!-- microformats -->", "<!-- /microformats -->"
MICROFORMAT_LINE_RE = re.compile(r"^- `(.*)`$")


class RolesError(Exception):
    """The one exception of this kit; its message names the file and the rule."""


# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — the `.governance/install.json` row whose `source` ends in <home>/<anchor> and
       whose `path` exists inside this tree. The only record of a RENAMED kit dir: no probe finds
       a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        if str(row.get("source") or "").split("/")[-2:] != [home, anchor]:
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir


def load_text(path):
    """A file's text, UTF-8, CRLF folded to LF; a missing file raises RolesError naming it."""
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read().replace("\r\n", "\n")
    except OSError as e:
        raise RolesError("%s: cannot be read — %s" % (pathlib.Path(path).as_posix(), e.strerror))


def read_conf_key(path, key):
    """The LAST `<key>=` assignment's value in a shell-style conf, or None when the key is absent.

    The hooks kit's conf grammar, ported line for line: an optional `export`, a double-quoted,
    single-quoted or bare value, a trailing `# comment` only behind whitespace. The key is compared
    as a string and never put into a regex.
    """
    value = None
    for line in load_text(path).split("\n"):
        m = CONF_LINE_RE.match(line)
        if m and m.group(1) == key:
            value = next(g for g in (m.group(2), m.group(3), m.group(4)) if g is not None)
    return value


def resolve_charter_path(root):
    """The governing doc: the `CHARTER` value of `<root>/.memory-tree.conf`, refused when absent."""
    conf = pathlib.Path(root) / ".memory-tree.conf"
    if not conf.is_file():
        raise RolesError("%s: R0 — no .memory-tree.conf, so no CHARTER declares the governing doc"
                         % conf.as_posix())
    value = read_conf_key(conf, "CHARTER")
    if not value:
        raise RolesError("%s: R0 — declares no CHARTER key, so the governing doc is undeclared"
                         % conf.as_posix())
    charter = pathlib.Path(root) / value
    if not charter.is_file():
        raise RolesError("%s: R0 — CHARTER names %s, which is not a file" % (conf.as_posix(), value))
    return charter


def parse_charter(text, where):
    """The governing doc as `{"shape", "rules", "carried"}`; RolesError (R0) on a doc this kit cannot read.

    Only the playbook region is read when the text holds its two markers once each, in order. A
    section is a `## ` line and the lines up to the next one. Section 1's `- [<tag>] ` lines are the
    rules, kept whole in charter order; each CARRIED_SECTIONS name is the first section headed by it,
    as `(heading, body)` with the body's blank edges trimmed. With a rule the shape is `tagged` and
    every carried section is required; with none and a `## §<n> — ` heading it is `legacy`, carrying
    nothing; otherwise the doc is refused. `where` is the path every message names.
    """
    text = text.replace("\r\n", "\n")
    i = text.find(PLAYBOOK_OPEN)
    j = text.find(PLAYBOOK_CLOSE, i + len(PLAYBOOK_OPEN)) if i >= 0 else -1
    if j >= 0 and text.count(PLAYBOOK_OPEN) == 1 and text.count(PLAYBOOK_CLOSE) == 1:
        text = text[i + len(PLAYBOOK_OPEN):j]
    sections = []
    for line in text.split("\n"):
        if line.startswith("## "):
            sections.append((line, []))
        elif sections:
            sections[-1][1].append(line)
    rules = {}
    one = next((body for head, body in sections if SECTION_ONE_RE.match(head)), [])
    for line in one:
        m = RULE_LINE_RE.match(line)
        if m and m.group(1) in rules:
            raise RolesError("%s: R0 — the governing doc repeats the rule tag [%s] in section 1"
                             % (where, m.group(1)))
        if m:
            rules[m.group(1)] = line
    if not rules:
        if any(SECTION_RE.match(ln) for ln in text.split("\n")):
            return {"shape": "legacy", "rules": {}, "carried": []}
        raise RolesError("%s: R0 — the governing doc carries neither a section 1 rule tag nor a "
                         "'## §<n> — ' heading, so it is no charter this kit reads" % where)
    carried = []
    for name in CARRIED_SECTIONS:
        hit = next(((head, body) for head, body in sections
                    if head == "## " + name or head.startswith("## %s " % name)), None)
        if hit is None:
            raise RolesError("%s: R0 — the governing doc carries section 1 rule tags and no '## %s' "
                             "section, which every role agent carries" % (where, name))
        body = list(hit[1])
        while body and not body[0].strip():
            body.pop(0)
        while body and not body[-1].strip():
            body.pop()
        carried.append((hit[0][3:], "\n".join(body)))
    return {"shape": "tagged", "rules": rules, "carried": carried}


def extract_microformat_shapes(text):
    """`{head: definition}` for every ``- `<definition>` `` line between the fence's two markers,
    each marker a whole line: the first line that is exactly `<!-- microformats -->` and the first
    that is exactly `<!-- /microformats -->`, CRLF folded. Keyed by the text before the
    definition's first ` — `; a head defined twice keeps its last definition. `{}` when either
    marker is absent or the closer comes first. This is how the hooks kit's format guard and the
    run-log kit's prose reader read the fence (TOOL-aOrientedCast-20, TOOL-aOrientedCast-25)."""
    lines = text.replace("\r\n", "\n").split("\n")
    if MICROFORMATS_OPEN not in lines or MICROFORMATS_CLOSE not in lines:
        return {}
    a, b = lines.index(MICROFORMATS_OPEN), lines.index(MICROFORMATS_CLOSE)
    shapes = {}
    for line in lines[a + 1:b]:
        m = MICROFORMAT_LINE_RE.match(line)
        if m:
            shapes[m.group(1).split(" — ", 1)[0]] = m.group(1)
    return shapes


def extract_prompt_marker(prompt):
    """The `MARKER_RE` match of the marker line an `Agent` prompt opens with, read as the hooks
    kit's spawn guard reads it (its rule 6): exactly one line, carriage returns removed, is a whole
    marker line, and it is the prompt's first line once CRLF is folded, the two ends trimmed and
    that line's trailing whitespace dropped. None otherwise (TOOL-aOrientedCast-25)."""
    text = str(prompt)
    marks = [ln for ln in (raw.replace("\r", "") for raw in text.split("\n")) if MARKER_RE.fullmatch(ln)]
    first = text.replace("\r\n", "\n").strip().split("\n")[0].rstrip()
    return MARKER_RE.fullmatch(first) if len(marks) == 1 and first == marks[0] else None


def check_rule_tags(charter, value):
    """`(defects, notes)` for one role's raw `rules` value against `parse_charter`'s structure.

    An entry that is not a lowercase tag (optionally ending in `?`) or repeats a tag is a defect on
    either shape. On a tagged charter a bare tag section 1 lacks is a defect and an optional one a
    note; on a legacy charter every well-formed entry is admitted and resolves to nothing.
    """
    defects, notes, seen = [], [], set()
    for e in [x.strip() for x in value.split(",") if x.strip()]:
        if not RULE_KEY_RE.match(e):
            defects.append("rules entry '%s' is not a lowercase tag, optionally ending in ?" % e)
            continue
        tag = e.rstrip("?")
        if tag in seen:
            defects.append("rules tag '%s' is named twice" % tag)
            continue
        seen.add(tag)
        if charter["shape"] != "tagged" or tag in charter["rules"]:
            continue
        if e == tag:
            defects.append("rules tag '%s' names no section 1 rule of the governing doc" % tag)
        else:
            notes.append("rules tag '%s' names no section 1 rule of the governing doc, so this role "
                         "carries no such rule here" % e)
    return defects, notes


def render_charter_blocks(charter, where, value, notes=None):
    """The charter text a role agent carries: `### Charter rules` holding the section 1 lines the
    `rules` value cites, in charter order, when it cites any, then each carried section under a
    `### ` heading, joined by one blank line and ending in one newline; `""` on a legacy charter.

    A defect raises RolesError, one `<where>: R4 — <defect>` line each; a note is appended to
    `notes` as `<where>: <note>` when a list is given.
    """
    defects, found = check_rule_tags(charter, value)
    if defects:
        raise RolesError("\n".join("%s: R4 — %s" % (where, d) for d in defects))
    if notes is not None:
        notes.extend("%s: %s" % (where, n) for n in found)
    if charter["shape"] != "tagged":
        return ""
    cited = {x.strip().rstrip("?") for x in value.split(",")}
    lines = [line for tag, line in charter["rules"].items() if tag in cited]
    blocks = ["### Charter rules\n\n" + "\n".join(lines)] if lines else []
    blocks += ["### %s\n\n%s" % (head, body) for head, body in charter["carried"]]
    return "\n\n".join(blocks) + "\n"


def parse_front_matter(path, text):
    """`(keys, body)` of a role file: the keys RAW, the body with its blank edges trimmed."""
    text = text.replace("\r\n", "\n")
    m = FRONT_MATTER_RE.match(text)
    if not m:
        raise RolesError("%s: R2 — no front matter; a role file opens with a '---' block at line 1" % path)
    keys = {}
    for i, line in enumerate(m.group(1).split("\n"), 2):
        if not line.strip():
            continue
        if line[:1].isspace():
            raise RolesError("%s:%d: R2 — front-matter key is indented; keys live at column 0" % (path, i))
        if ":" not in line:
            raise RolesError("%s:%d: R2 — front-matter line is not 'key: value'" % (path, i))
        k, _, v = line.partition(":")
        k = k.strip()
        if k not in FRONT_MATTER_KEYS:
            raise RolesError("%s:%d: R2 — unknown front-matter key '%s'" % (path, i, k))
        if k in keys:
            raise RolesError("%s:%d: R2 — front-matter key '%s' is repeated" % (path, i, k))
        keys[k] = v.strip()
    return keys, text[m.end():].strip("\n")


def load_roles(kit_dir):
    """Every `agents/*.agent.md`, parsed, keyed by slot: `{slot: {"path", "keys", "body"}}`."""
    roles = {}
    for p in sorted((pathlib.Path(kit_dir) / "agents").glob("*.agent.md")):
        keys, body = parse_front_matter(p.as_posix(), load_text(p))
        roles[p.name[:-len(".agent.md")]] = {"path": p, "keys": keys, "body": body}
    return roles


def load_workflows(kit_dir):
    """`workflows.toml`'s `[[workflow]]` entries, as a list in file order."""
    path = pathlib.Path(kit_dir) / "workflows.toml"
    try:
        with open(path, "rb") as fh:
            data = tomllib.load(fh)
    except OSError as e:
        raise RolesError("%s: R6 — cannot be read — %s" % (path.as_posix(), e.strerror))
    except tomllib.TOMLDecodeError as e:
        raise RolesError("%s: R6 — not valid TOML — %s" % (path.as_posix(), e))
    entries = data.get("workflow", [])
    if not isinstance(entries, list) or not all(isinstance(e, dict) for e in entries):
        raise RolesError("%s: R6 — 'workflow' is not an array of tables" % path.as_posix())
    return entries


def load_gate_leg_names(tool_root):
    """The leg names of `<tool root>/gate-legs.json`, or None when it is absent, unreadable, not
    JSON, or not a list of objects each carrying a string `name`."""
    try:
        with open(pathlib.Path(tool_root) / GATE_MANIFEST, encoding="utf-8") as fh:
            legs = json.load(fh)
    except (OSError, ValueError):
        return None
    if not isinstance(legs, list) or not all(isinstance(g, dict) and isinstance(g.get("name"), str) for g in legs):
        return None
    return {g["name"] for g in legs}


def load_policy(kit_dir, roles, workflows, notes=None):
    """The parsed `house/policy.toml`, validated against the roles and the workflow table.

    Every defect is collected, then raised once as a RolesError with one line per defect, each
    naming the file, the dotted key and the rule (R12). An absent or unparsable file refuses
    (TOOL-aOrientedCast-10 §8 F3): no fallback level stands in for the owner's.

    `[gates]` (TOOL-aOrientedCast-11) maps a role slot whose `agent` is true to the gate legs it may
    run, by name. A name is checked against the tool root's gate manifest only when that manifest
    reads; when it does not, one line is appended to `notes` (when given) instead of a defect.
    A name ending in `?` is OPTIONAL (TOOL-aOrientedCast-13): a leg the manifest lacks is a note
    rather than a defect, and the returned policy carries every name with its `?` taken off.
    """
    path = pathlib.Path(kit_dir) / "house" / "policy.toml"
    where = path.as_posix()
    try:
        with open(path, "rb") as fh:
            data = tomllib.load(fh)
    except OSError as e:
        raise RolesError("%s: R12 — the policy file cannot be read — %s" % (where, e.strerror))
    except tomllib.TOMLDecodeError as e:
        raise RolesError("%s: R12 — the policy file is not valid TOML — %s" % (where, e))
    bad = []

    def check_level(key, value):
        if value not in EFFORT_LEVELS:
            bad.append("%s: R12 — %s — %r is not a level; the levels are %s"
                       % (where, key, value, ", ".join(EFFORT_LEVELS)))

    for k in data:
        if k not in POLICY_TABLES:
            bad.append("%s: R12 — %s — unknown top-level key; the tables are %s"
                       % (where, k, " and ".join(POLICY_TABLES)))
    effort = data.get("effort", {})
    if not isinstance(effort, dict):
        effort = {}
        bad.append("%s: R12 — effort — is not a table" % where)
    for k in effort:
        if k not in POLICY_EFFORT_KEYS:
            bad.append("%s: R12 — effort.%s — unknown key; effort holds %s"
                       % (where, k, ", ".join(POLICY_EFFORT_KEYS)))
    if "default" not in effort:
        bad.append("%s: R12 — effort.default — is absent" % where)
    else:
        check_level("effort.default", effort["default"])
    role_levels = effort.get("roles", {})
    if not isinstance(role_levels, dict):
        role_levels = {}
        bad.append("%s: R12 — effort.roles — is not a table" % where)
    for slot, level in role_levels.items():
        key = "effort.roles." + slot
        check_level(key, level)
        if slot not in roles:
            bad.append("%s: R12 — %s — names no role file" % (where, key))
        elif roles[slot]["keys"].get("agent", "true") == "false":
            bad.append("%s: R12 — %s — names an agent: false role, so no agent type carries it"
                       % (where, key))
    stage_levels = effort.get("stages", {})
    if not isinstance(stage_levels, dict):
        stage_levels = {}
        bad.append("%s: R12 — effort.stages — is not a table" % where)
    by_name = {w.get("name"): w for w in workflows}
    for name, table in stage_levels.items():
        key = "effort.stages." + name
        if not isinstance(table, dict):
            bad.append("%s: R12 — %s — is not a table" % (where, key))
            continue
        if name not in by_name:
            bad.append("%s: R12 — %s — names no workflow" % (where, key))
            continue
        held = by_name[name].get("stages")
        if not isinstance(held, dict):
            bad.append("%s: R12 — %s — the workflow %s has no stages table" % (where, key, name))
            continue
        for stage, level in table.items():
            check_level("%s.%s" % (key, stage), level)
            if stage not in held:
                bad.append("%s: R12 — %s.%s — is not a stage key of %s, whose keys are %s"
                           % (where, key, stage, name, ", ".join(sorted(held))))
    gates = data.get("gates", {})
    if not isinstance(gates, dict):
        gates = {}
        bad.append("%s: R12 — gates — is not a table" % where)
    manifest = (pathlib.Path(kit_dir).parent / GATE_MANIFEST).as_posix()
    legs = load_gate_leg_names(pathlib.Path(kit_dir).parent) if gates else None
    for slot, names in gates.items():
        key = "gates." + slot
        if slot not in roles:
            bad.append("%s: R12 — %s — names no role file" % (where, key))
        elif roles[slot]["keys"].get("agent", "true") == "false":
            bad.append("%s: R12 — %s — names an agent: false role, so no agent type carries it"
                       % (where, key))
        if not isinstance(names, list) or not all(isinstance(n, str) for n in names):
            bad.append("%s: R12 — %s — is not a list of strings" % (where, key))
            continue
        for n in names:
            leg = n[:-1] if n.endswith("?") else n
            if not leg:
                bad.append("%s: R12 — %s — %r names no leg" % (where, key, n))
            elif legs is not None and leg not in legs:
                if leg == n:
                    bad.append("%s: R12 — %s — %r names no leg of %s" % (where, key, n, manifest))
                elif notes is not None:
                    notes.append("%s holds no leg '%s', which gates.%s marks optional, so %s is "
                                 "granted no such leg here" % (manifest, leg, slot, slot))
    if gates and legs is None and notes is not None:
        notes.append("%s cannot be read, so the leg names under [gates] in %s are not checked"
                     % (manifest, where))
    if bad:
        raise RolesError("\n".join(bad))
    for slot in gates:
        gates[slot] = [n[:-1] if n.endswith("?") else n for n in gates[slot]]
    return data


def load_stand_in_waivers(root, memory_root, roles):
    """`(rows, defects)` of `<MEMORY_ROOT>/project/role-stand-in-waiver.txt` (TOOL-aOrientedCast-19).

    `rows` maps `(build, role)` to `{"line", "date", "who", "role", "build", "reason"}` for each
    valid row; `defects` holds one `<registry>:<line>: R15 — <what>` line per invalid row, naming
    the first field that fails. A row is five TAB-separated fields split at the first four TABs,
    `<date>`, `owner <who>`, `<role>`, `<build>`, `<reason>`; blank lines and `#` lines are ignored. A
    second row for a `(build, role)` already held is a defect, and the first stays valid. An absent
    registry yields neither; nothing here raises on a row. `roles` is `load_roles`'s shape.
    """
    rel = (pathlib.Path(memory_root) / "project" / STAND_IN_WAIVER).as_posix()
    path = pathlib.Path(root) / rel
    rows, defects = {}, []
    if not path.is_file():
        return rows, defects
    try:
        text = load_text(path)
    except (RolesError, UnicodeDecodeError) as e:
        return rows, ["%s: R15 — the registry cannot be read as UTF-8 — %s" % (rel, e)]
    for n, line in enumerate(text.split("\n"), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        fields = line.split("\t", 4)
        what = None
        if len(fields) < 5:
            what = "is %d TAB-separated field(s), and a row is five: date, owner, role, build, reason" % len(fields)
        else:
            date, who, role, build, reason = fields
            try:
                dated = WAIVER_DATE_RE.match(date) and datetime.date.fromisoformat(date)
            except ValueError:
                dated = None
            agent = roles.get(role, {}).get("keys", {}).get("agent", "true")
            if not dated:
                what = "date '%s' is not a YYYY-MM-DD calendar date" % date
            elif not WAIVER_OWNER_RE.match(who):
                what = "attribution '%s' is not 'owner <who>', so the row is not the owner's" % who
            elif role not in roles:
                what = "role '%s' names no role file" % role
            elif agent == "false":
                what = "role '%s' is an agent: false role, which is never spawned, so nothing stands in for it" % role
            elif not SLUG_RE.match(build):
                what = "build '%s' is not a slug of letters" % build
            elif not reason.strip():
                what = "the reason is empty; a waiver says why the role cannot be spawned"
            elif (build, role) in rows:
                what = "repeats the row for role %s in build %s at line %d" % (role, build, rows[(build, role)]["line"])
            else:
                rows[(build, role)] = {"line": n, "date": date, "who": who[len("owner "):], "role": role,
                                       "build": build, "reason": reason.strip()}
        if what:
            defects.append("%s:%d: R15 — %s" % (rel, n, what))
    return rows, defects


def scan_stand_in_declarations(root, memory_root):
    """`(declarations, defects)`: every `<MEMORY_ROOT>/builds/*/prompts/*-stand-in.md`, sorted, read
    through its `gov:handoff` marker as `{"path", "role", "build", "unit"}`, `path` root-relative
    (TOOL-aOrientedCast-19). A tailed file with no marker line is one `<path>: R15 — ` defect: its
    name declares a stand-in and it names no role. A handoff without the tail is never read."""
    root = pathlib.Path(root)
    found, defects = [], []
    for p in sorted((root / memory_root / "builds").glob("*/prompts/*%s.md" % STAND_IN_TAIL)):
        rel = p.relative_to(root).as_posix()
        try:
            m = MARKER_RE.search(load_text(p))
        except (RolesError, UnicodeDecodeError) as e:
            defects.append("%s: R15 — the stand-in declaration cannot be read as UTF-8 — %s" % (rel, e))
            continue
        if not m:
            defects.append("%s: R15 — named as a stand-in declaration and carries no gov:handoff "
                           "marker line, so it names no role" % rel)
            continue
        found.append({"path": rel, "role": m.group(1), "build": m.group(2), "unit": m.group(3)})
    return found, defects


def resolve_effort(policy, slot):
    """A role's level: its `[effort.roles]` entry, else `default`."""
    effort = policy["effort"]
    return effort.get("roles", {}).get(slot, effort["default"])


def resolve_stage_efforts(policy, workflow):
    """`{stage key: level}` for every key of a workflow entry's `stages` table: its
    `[effort.stages.<workflow>]` entry, else the level of the slot the table maps it to."""
    over = policy["effort"].get("stages", {}).get(workflow.get("name"), {})
    return {key: over.get(key, resolve_effort(policy, slot))
            for key, slot in (workflow.get("stages") or {}).items()}


def render_role(kit_dir, name, memory_root):
    """The role's base body with `{{MEMORY_ROOT}}` substituted, then its house overlay when non-empty."""
    kit = pathlib.Path(kit_dir)
    path = kit / "agents" / (name + ".agent.md")
    _, body = parse_front_matter(path.as_posix(), load_text(path))
    overlay_path = kit / "house" / (name + ".md")
    overlay = load_text(overlay_path).strip("\n") if overlay_path.is_file() else ""
    for src, rule, text in ((path, "R5", body), (overlay_path, "R10", overlay)):
        for token in TOKEN_RE.findall(text):
            if token != MEMORY_ROOT_TOKEN:
                raise RolesError("%s: %s — carries the render token %s; only %s renders"
                                 % (src.as_posix(), rule, token, MEMORY_ROOT_TOKEN))
    out = body + ("\n\n## House rules\n\n" + overlay if overlay.strip() else "")
    return out.replace(MEMORY_ROOT_TOKEN, memory_root) + "\n"


def resolve_harness_path(tool_root, harness):
    """`(path, held)` for a `{prefix}/<home>/<file>` harness; `<tool root>/<home>/<file>, False` unheld."""
    m = HARNESS_RE.match(harness or "")
    if not m:
        raise RolesError("harness '%s' is not a {prefix}/<home>/<file> path" % harness)
    home, anchor = m.group(1), m.group(2)
    try:
        return resolve_kit_dir(home, anchor, tool_root) / anchor, True
    except LookupError:
        return pathlib.Path(tool_root).absolute() / home / anchor, False
