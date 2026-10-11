#!/usr/bin/env python3
"""check_roles.py — the role files, the workflow table and the governing doc agree (TOOL-aOrientedCast-1).

    python check_roles.py [--root <dir>] [--write]

The kit directory is this script's own directory and the tool root its parent; `--root` defaults to
the git toplevel of the working directory. One line per defect, `roles: <path>: <rule> — <what>`,
then one summary line naming every count it graded and each overlay's bytes. Exit 0 clean, 1 on any
defect, 2 when the check is unarmed. `--write` renders the README's catalogue region and writes it,
touching nothing else, then grades as usual.

  R0  no `.memory-tree.conf`, no CHARTER key in it, or no file at that path (exit 2)
  R1  zero role files or zero workflow entries: a check that graded nothing is DEAD PROBE
  R2  a front-matter defect: unknown, indented, repeated or missing key; `name` not the file stem;
      `writes` outside its set; `agent` not true/false; `tools` or `model` absent on an agent role
  R3  a `reads` key outside the vocabulary, named twice, or `card:reuse` without `?`
  R4  a `charter` id that is not `§` and digits, or names no heading in the governing doc
  R5  a body empty, over its slot's ceiling, carrying a `# `/`## ` line or a token other than
      {{MEMORY_ROOT}}; a slot with no ceiling row
  R6  a workflow entry with an unknown, missing or repeated key or name, a missing name of the ten,
      a non-integer or negative `stage`, an unknown `driver`, or a `trigger` carrying a newline
  R7  a role whose `workflow` names no entry, or whose entry does not list it
  R8  a `roles` entry naming no role file; an agent or workflow driver with no role; a role file no
      entry lists
  R9  a workflow driver whose harness is not a `{prefix}/<home>/<file>.js` path; a `stages` table on
      another driver, a key outside its pattern, or a value outside the entry's roles or naming an
      `agent: false` role. A well-formed harness the tree does not hold prints one `roles: note:`
  R10 a house overlay naming no role, or carrying a `# `/`## ` line or a token other than {{MEMORY_ROOT}}
  R11 the README's catalogue region absent, or different from a fresh render
  R12 a `house/policy.toml` defect, one line per line of `roles_lib.load_policy`'s refusal: the file
      absent or not TOML, an unknown key, no `default`, a level outside the five, a role entry
      naming no role file or an `agent: false` role, a stages table naming no workflow or a
      workflow with no stages, or a stage key that workflow does not hold

WHAT THIS DOES NOT CHECK, because a structural check reads as a semantic one to everybody who did not
write it: the MEANING of a body; the truth of an `enforced-by` entry; a `tools:` name, which moves
with the CLI; a command harness, which is graded for presence only; and whether the kit of a harness
the tree does not hold should be installed, which is a `note` here and the wiring check's to report.
An overlay's size is printed and never graded: it is the adopter's own text.
"""
import pathlib
import re
import subprocess
import sys

KIT_DIR = pathlib.Path(__file__).absolute().parent
sys.path.insert(0, str(KIT_DIR))
import roles_lib as lib  # noqa: E402  (the kit's own library, beside this file)

#: Bytes of each slot's BASE body, CR stripped. A new role is priced when it is added.
BODY_CEILINGS = {
    "gov-orienter": 3072, "gov-researcher": 3072, "gov-reuse-scout": 1536,
    "gov-spec-writer": 4096, "gov-spec-reviewer": 4096, "gov-builder": 4096,
    "gov-diff-reviewer": 4096, "gov-skeptic": 3072, "gov-synthesizer": 3072, "gov-session": 2048,
}
WORKFLOW_NAMES = ("orient", "research", "reuse", "handoff", "spec-write", "spec-review", "build",
                  "closing-review", "gate-bar", "bookkeeping")
WORKFLOW_KEYS = ("name", "stage", "driver", "harness", "roles", "stages", "enforced-by", "trigger")
DRIVERS = ("agent", "workflow", "program", "main-loop")
WRITES = ("none", "spec", "product", "review", "records")
REQUIRED_ROLE_KEYS = ("name", "description", "workflow", "reads", "writes", "charter", "returns")
STAGE_KEY_RE = re.compile(r"^[a-z][A-Za-z]*$")
JS_HARNESS_RE = re.compile(r"^\{prefix\}/[^/{}\s]+/[^/{}\s]+\.js$")
REGION_OPEN, REGION_CLOSE = "<!-- gen:roles-catalogue -->", "<!-- /gen:roles-catalogue -->"


def resolve_display_path(root, p):
    """`p` relative to the root, forward-slashed; absolute when it lies outside it."""
    p, root = pathlib.Path(p).absolute(), pathlib.Path(root).absolute()
    return p.relative_to(root).as_posix() if root in p.parents else p.as_posix()


def render_cell(v):
    """One table cell: a list comma-joined, a table as `key → value` pairs, a pipe escaped."""
    if isinstance(v, dict):
        v = ", ".join("%s → %s" % kv for kv in v.items())
    elif isinstance(v, list):
        v = ", ".join(str(x) for x in v)
    return (str(v) if v not in (None, "") else "—").replace("|", "\\|")


def render_catalogue_region(roles, workflows):
    """The two tables between the region markers, in file order."""
    out =["", "**Workflows**, from `workflows.toml`:", "",
           "| " + " | ".join(WORKFLOW_KEYS) + " |", "|" + "---|" * len(WORKFLOW_KEYS)]
    out += ["| " + " | ".join(render_cell(w.get(k)) for k in WORKFLOW_KEYS) + " |" for w in workflows]
    cols = ("workflow", "writes", "reads", "charter", "agent", "returns")
    out += ["", "**Roles**, from `agents/*.agent.md`:", "",
            "| role | " + " | ".join(cols) + " |", "|" + "---|" * (len(cols) + 1)]
    for slot, r in roles.items():
        keys = dict(r["keys"], agent=r["keys"].get("agent", "true"))
        out.append("| `%s` | " % slot + " | ".join(render_cell(keys.get(c)) for c in cols) + " |")
    return "\n".join(out + [""]) + "\n"


def check_catalogue_region(text, region):
    """None when the README carries the region as rendered; else what is wrong with it."""
    i = text.find(REGION_OPEN)
    j = text.find(REGION_CLOSE, i + 1) if i >= 0 else -1
    if i < 0 or j < 0:
        return "the catalogue region's markers are absent; restore them and run --write"
    if text[i + len(REGION_OPEN):j] != region:
        return "the catalogue region differs from a fresh render; run --write"
    return None


def check_roles(root, kit_dir, write=False):
    """`(defects, notes, summary)`; raises RolesError when the check is unarmed (R0)."""
    root, kit_dir = pathlib.Path(root), pathlib.Path(kit_dir)
    tool_root = kit_dir.parent
    charter_path = lib.resolve_charter_path(root)
    sections = lib.extract_charter_sections(lib.load_text(charter_path))
    defects, notes = [], []

    def add_defect(path, rule, what):
        defects.append("roles: %s: %s — %s" % (resolve_display_path(root, path), rule, what))

    roles, n_reads, n_charter = {}, 0, 0
    for p in sorted((kit_dir / "agents").glob("*.agent.md")):
        slot = p.name[:-len(".agent.md")]
        try:
            keys, body = lib.parse_front_matter(resolve_display_path(root, p), lib.load_text(p))
        except lib.RolesError as e:
            defects.append("roles: %s" % e)
            continue
        roles[slot] = {"path": p, "keys": keys, "body": body}
        for k in REQUIRED_ROLE_KEYS:
            if k not in keys or (k != "charter" and not keys[k]):
                add_defect(p, "R2", "front-matter key '%s' is missing" % k)
        if keys.get("name") and keys["name"] != slot:
            add_defect(p, "R2", "name '%s' is not the file stem '%s'" % (keys["name"], slot))
        if keys.get("writes") and keys["writes"] not in WRITES:
            add_defect(p, "R2", "writes '%s' is not one of %s" % (keys["writes"], " ".join(WRITES)))
        if keys.get("agent", "true") not in ("true", "false"):
            add_defect(p, "R2", "agent '%s' is not true or false" % keys["agent"])
        if keys.get("agent", "true") == "true":
            for k in "tools model".split():
                if not keys.get(k):
                    add_defect(p, "R2", "'%s' is absent on an agent role" % k)
        seen = set()
        for item in [x.strip() for x in keys.get("reads", "").split(",") if x.strip()]:
            n_reads += 1
            base = item[:-1] if item.endswith("?") else item
            if base not in lib.READ_KEYS:
                add_defect(p, "R3", "reads key '%s' is outside the vocabulary" % item)
            if base in seen:
                add_defect(p, "R3", "reads key '%s' is named twice" % base)
            if item == "card:reuse":
                add_defect(p, "R3", "card:reuse must be optional, 'card:reuse?': that section is not on every card")
            seen.add(base)
        for cid in [x.strip() for x in keys.get("charter", "").split(",") if x.strip()]:
            n_charter += 1
            if not re.fullmatch(r"§\d+", cid):
                add_defect(p, "R4", "charter id '%s' is not § and digits" % cid)
            elif cid not in sections:
                add_defect(p, "R4", "charter %s names no heading in %s" % (cid, resolve_display_path(root, charter_path)))
        ceiling = BODY_CEILINGS.get(slot)
        size = len(body.encode("utf-8"))
        if ceiling is None:
            add_defect(p, "R5", "slot '%s' has no ceiling row in BODY_CEILINGS" % slot)
        elif size > ceiling:
            add_defect(p, "R5", "body is %d bytes, over its %d-byte ceiling" % (size, ceiling))
        if not body.strip():
            add_defect(p, "R5", "body is empty")
        if any(ln.startswith(("# ", "## ")) for ln in body.split("\n")):
            add_defect(p, "R5", "body carries a '# ' or '## ' heading line")
        for token in sorted(set(lib.TOKEN_RE.findall(body)) - {lib.MEMORY_ROOT_TOKEN}):
            add_defect(p, "R5", "body carries the token %s; only %s renders" % (token, lib.MEMORY_ROOT_TOKEN))
    files = {p.name[:-len(".agent.md")] for p in (kit_dir / "agents").glob("*.agent.md")}
    if not files:
        add_defect(kit_dir / "agents", "R1", "DEAD PROBE: no role file, so this check graded nothing")

    table = kit_dir / "workflows.toml"
    try:
        workflows = lib.load_workflows(kit_dir)
    except lib.RolesError as e:
        defects.append("roles: %s" % e)
        workflows = []
    if not workflows:
        add_defect(table, "R1", "DEAD PROBE: no workflow entry, so this check graded nothing")
    by_name = {}
    for i, w in enumerate(workflows, 1):
        where = "entry %d (%s)" % (i, w.get("name", "unnamed"))
        for k in w:
            if k not in WORKFLOW_KEYS:
                add_defect(table, "R6", "%s has an unknown key '%s'" % (where, k))
        for k in WORKFLOW_KEYS:
            if k != "stages" and k not in w:
                add_defect(table, "R6", "%s is missing key '%s'" % (where, k))
        name = w.get("name")
        if name not in WORKFLOW_NAMES:
            add_defect(table, "R6", "%s names an unknown workflow" % where)
        elif name in by_name:
            add_defect(table, "R6", "%s repeats the name '%s'" % (where, name))
        else:
            by_name[name] = w
        stage = w.get("stage")
        if "stage" in w and (not isinstance(stage, int) or isinstance(stage, bool) or stage < 0):
            add_defect(table, "R6", "%s stage %r is not an integer at or above 0" % (where, stage))
        if "driver" in w and w["driver"] not in DRIVERS:
            add_defect(table, "R6", "%s driver %r is not one of %s" % (where, w["driver"], " ".join(DRIVERS)))
        trig = w.get("trigger")
        if "trigger" in w and (not isinstance(trig, str) or not trig.strip() or "\n" in trig):
            add_defect(table, "R6", "%s trigger is not one non-empty line" % where)
        if "enforced-by" in w and not w["enforced-by"]:
            add_defect(table, "R6", "%s enforced-by is empty" % where)
        listed = w.get("roles", [])
        if not isinstance(listed, list) or not all(isinstance(x, str) for x in listed):
            add_defect(table, "R6", "%s roles is not a list of slot keys" % where)
            listed = []
        for slot in listed:
            if slot not in files:
                add_defect(table, "R8", "%s lists '%s', which names no role file" % (where, slot))
        if w.get("driver") in ("agent", "workflow") and not listed:
            add_defect(table, "R8", "%s is driven by '%s' and names no role" % (where, w["driver"]))
        if w.get("driver") == "workflow":
            harness = w.get("harness", "")
            if not isinstance(harness, str) or not JS_HARNESS_RE.match(harness):
                add_defect(table, "R9", "%s harness %r is not a {prefix}/<home>/<file>.js path" % (where, harness))
            else:
                _, held = lib.resolve_harness_path(tool_root, harness)
                if not held:
                    notes.append("roles: note: %s harness %s is not held by this tree" % (where, harness))
        stages = w.get("stages")
        if stages is not None:
            if w.get("driver") != "workflow":
                add_defect(table, "R9", "%s carries a stages table on a '%s' driver" % (where, w.get("driver")))
            elif not isinstance(stages, dict):
                add_defect(table, "R9", "%s stages is not a table" % where)
            else:
                for key, slot in stages.items():
                    if not STAGE_KEY_RE.match(key):
                        add_defect(table, "R9", "%s stage key '%s' does not match %s" % (where, key, STAGE_KEY_RE.pattern))
                    if slot not in listed:
                        add_defect(table, "R9", "%s stage %s maps to '%s', which its roles do not list" % (where, key, slot))
                    elif slot in roles and roles[slot]["keys"].get("agent", "true") == "false":
                        add_defect(table, "R9", "%s stage %s maps to '%s', an agent: false role" % (where, key, slot))
    for name in WORKFLOW_NAMES:
        if workflows and name not in by_name:
            add_defect(table, "R6", "the workflow '%s' has no entry" % name)

    listed_anywhere = {s for w in workflows if isinstance(w.get("roles"), list) for s in w["roles"]}
    for slot, r in roles.items():
        wf = r["keys"].get("workflow")
        if wf and wf not in by_name:
            add_defect(r["path"], "R7", "workflow '%s' names no entry in workflows.toml" % wf)
        elif wf and slot not in by_name[wf].get("roles", []):
            add_defect(r["path"], "R7", "the '%s' entry's roles does not list %s" % (wf, slot))
    for slot in sorted(files - listed_anywhere):
        add_defect(kit_dir / "agents" / (slot + ".agent.md"), "R8", "no workflow entry lists this role")

    overlays = {}
    for p in sorted((kit_dir / "house").glob("*.md")):
        text = lib.load_text(p)
        overlays[p.stem] = len(text.encode("utf-8"))
        if p.stem not in files:
            add_defect(p, "R10", "overlay names no role: there is no agents/%s.agent.md" % p.stem)
        if any(ln.startswith(("# ", "## ")) for ln in text.split("\n")):
            add_defect(p, "R10", "overlay carries a '# ' or '## ' heading line")
        for token in sorted(set(lib.TOKEN_RE.findall(text)) - {lib.MEMORY_ROOT_TOKEN}):
            add_defect(p, "R10", "overlay carries the token %s; only %s renders" % (token, lib.MEMORY_ROOT_TOKEN))

    try:
        lib.load_policy(kit_dir, roles, workflows)
    except lib.RolesError as e:
        defects.extend("roles: %s" % ln for ln in str(e).split("\n"))

    readme = kit_dir / "README.md"
    region = render_catalogue_region(roles, workflows)
    text = lib.load_text(readme) if readme.is_file() else ""
    i = text.find(REGION_OPEN)
    j = text.find(REGION_CLOSE, i + 1) if i >= 0 else -1
    if write and j >= 0:
        text = text[:i + len(REGION_OPEN)] + region + text[j:]
        with open(readme, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
    problem = check_catalogue_region(text, region)
    if problem:
        add_defect(readme, "R11", problem)

    summary = ("roles: graded %d roles, %d overlays, %d workflows, %d reads keys, %d charter ids "
               "against %s; overlay bytes %s; %d defect(s)" % (
                   len(files), len(overlays), len(workflows), n_reads, n_charter, resolve_display_path(root, charter_path),
                   ", ".join("%s=%d" % kv for kv in overlays.items()) or "none", len(defects)))
    return defects, notes, summary


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    args, root, write = list(argv), None, False
    while args:
        a = args.pop(0)
        if a == "--write":
            write = True
        elif a == "--root" and args:
            root = args.pop(0)
        else:
            print("usage: python check_roles.py [--root <dir>] [--write]", file=sys.stderr)
            return 2
    if root is None:
        r = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, encoding="utf-8")
        if r.returncode != 0 or not r.stdout.strip():
            print("roles: R0 — the working directory is in no git repository; pass --root", file=sys.stderr)
            return 2
        root = r.stdout.strip()
    try:
        defects, notes, summary = check_roles(root, KIT_DIR, write)
    except lib.RolesError as e:
        print("roles: %s" % e)
        return 2
    for line in defects + notes:
        print(line)
    print(summary)
    return 1 if defects else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
