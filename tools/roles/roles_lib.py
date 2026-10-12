"""roles_lib — the one reader of the role catalogue, and the one composition of a role (TOOL-aOrientedCast-1).

Reads the role files under `agents/`, the workflow table `workflows.toml`, the memory-tree conf and
the governing doc's `§<n>` sections. `render_role` is the one composition of a role with its house
overlay: every consumer that hands a role to an agent calls it, so a role reaches an agent the same
way by every route. Stdlib only; every text read folds CRLF to LF and names its encoding.

The front-matter grammar: a `---` block at line 1, one `key: value` per line at COLUMN 0, values kept
RAW (a list is comma-separated on one line, the form Claude Code's own `tools:` takes). An indented,
a repeated or an unknown key is refused, because a simple parser drops an indented key without a
word and a repeated one silently keeps the last.
"""
import json
import pathlib
import re
import tomllib

KIT_ROLES_VERSION = "1.2"

#: Every front-matter key a role file may carry: Claude Code's own, then gov's.
#: Split from one string, because a quoted `"tools"` beside a quoted segment reads to the
#: install-prefix ban as a kit path (TOOL-aOrientedCast-8 S14).
FRONT_MATTER_KEYS = tuple("name description tools model maxTurns "
                          "workflow reads writes charter returns agent".split())

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
SECTION_RE = re.compile(r"^## (§\d+) — ")
HARNESS_RE = re.compile(r"^\{prefix\}/([^/{}\s]+)/([^/{}\s]+)$")


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


def extract_charter_sections(text):
    """`{"§<n>": body}` for every `## §<n> — ` heading; a body runs to the next `## ` line."""
    sections, current, lines = {}, None, []
    for line in text.replace("\r\n", "\n").split("\n") + ["## "]:
        if line.startswith("## "):
            if current is not None and current not in sections:
                sections[current] = "\n".join(lines).strip("\n")
            m = SECTION_RE.match(line)
            current, lines = (m.group(1) if m else None), []
        elif current is not None:
            lines.append(line)
    return sections


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
