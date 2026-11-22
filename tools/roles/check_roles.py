#!/usr/bin/env python3
"""check_roles.py — the role files, the workflow table and the governing doc agree (TOOL-aOrientedCast-1).

    python check_roles.py [--root <dir>] [--write]
    python check_roles.py --print-tag-rows role|stage < <a role file or workflows.toml>

The kit directory is this script's own directory and the tool root its parent; `--root` defaults to
the git toplevel of the working directory. One line per defect, `roles: <path>: <rule> — <what>`,
then one summary line naming every count it graded and each overlay's bytes. Exit 0 clean, 1 on any
defect, 2 when the check is unarmed. `--write` renders the README's catalogue region and writes it,
touching nothing else, then grades as usual. `--print-tag-rows` prints the tag index's rows of the
text on stdin and grades nothing (TOOL-dBoundRoles-14), as `print_tag_rows` says.

  R0  no `.memory-tree.conf`, no CHARTER key in it, or no file at that path; a blank or absent
      MEMORY_ROOT in it (TOOL-aOrientedCast-19); a governing doc that
      carries no practice rule tag, between its practices markers or under a numbered first heading,
      and no `## §<n> — ` heading, a tagged doc lacking a carried section (`## Protocols`,
      `## Facts`), or a practice tag repeated (exit 2)
  R1  zero role files or zero workflow entries, or a tagged charter no role's `rules` cites a tag
      of: a check that graded nothing is DEAD PROBE
  R2  a front-matter defect: unknown, indented, repeated or missing key, the keys and which are
      required read from `role-schema.toml` through `roles_lib.load_role_schema`, an absent or
      invalid schema exit 2 (`rules` may be empty; `mandatory`, `output`, `never` and `return` may
      not, on any role); `name` not the file stem; `writes` outside its set; `agent` not
      true/false; `tools`, `model` or `effort` absent on an agent role, or an `effort` outside the
      five levels; a role file whose slot is `default`, reserved for the blanket key
      `roles.effort.default` (TOOL-dBoundRoles-21 S3, S4); a `gates` field on an `agent: false`
      role or naming a leg as R12 grades a `[gates]` row; a `return` template
      `parse_return_template` refuses, a required `outcome` of a closed set among what it owes
      (TOOL-dBoundRoles-2); a `layer` that is no `layer.<seg>` tag or names no `[[layer]]` row of the
      playbook kit's `layers.toml`, joined only where that register resolves and a `roles: note:`
      otherwise; an `acts-as` other than `item` or `cycle`. The summary counts the roles per layer
      and per `acts-as` value (TOOL-dBoundRoles-1). A `shapes` value that is no list of distinct
      kinds of `roles_lib.WORKFLOW_KINDS` (TOOL-dBoundRoles-16 S5)
  R3  a `reads` key outside the vocabulary, named twice, or `card:reuse` or `upstream:rows` without `?`,
      each entry read through `parse_read_key`, so `task:title` and its tag `field.task.title` are one key
  R4  a `rules` entry that is not a lowercase tag optionally ending in `?`, a tag named twice, or a
      bare tag naming no practice of a tagged charter; an optional (`?`) tag its practices lack
      prints one `roles: note:`. A pre-tag (v3.x) charter resolves no tag and prints one note
  R5  a body empty, over its slot's ceiling, carrying a `# `/`## ` line or a token other than
      {{MEMORY_ROOT}}, or spelling the file name of a protocol the charter's Protocols section
      names; a body line carrying `never`, `do not`, `don't` or `must not`, matched ignoring case as
      whole words, one line each naming its line, since a limit lives in `never` and the body
      states the job (TOOL-dBoundRoles-2 S3); a slot with no ceiling row. The ceiling half obeys
      the policy kit's size switch for the family cap `role-body` (TOOL-dGroundRules-9): under `warn` it prints a `BUDGET WARN` line and
      is no defect; with no policy kit, or a refusing reader, it is a defect as before
  R6  a workflow entry with an unknown, missing or repeated key or name, a missing name of the twelve,
      an unknown `driver`, or a `trigger` carrying a newline; a workflow no `[[workflow]]` row of
      the loop definition places, a loop row naming no workflow here, or a loop definition that
      does not read, one line (TOOL-dDeclaredLoop-1): a workflow's order and step are the loop
      definition's, so a `stage` or `step` key here is an unknown key. An entry may omit
      `stages`, `merge`, `twin`, `of` and `experiment`, and one listing no role `kind`, `checklist`
      and `orientation` too (TOOL-dBoundRoles-16 S2)
  R7  a role whose `workflow` names no entry, or whose entry does not list it
  R8  a `roles` entry naming no role file; an agent or workflow driver with no role; a role file no
      entry lists
  R9  a workflow driver whose harness is not a `{prefix}/<home>/<file>.js` path, or that declares no
      `[[workflow.stages]]` row; stage rows on another driver, or a `stages` that is no array of
      tables; and per row (TOOL-dBoundRoles-22 S4), a `key` outside its pattern or repeated in its
      entry, a `role` outside the entry's roles or naming an `agent: false` role, a `fan` or `cap`
      that is not an integer of at least 1, an `effort` outside the five levels, a `receives` or
      `returns` that is no list or holds an entry outside the loop kit's row kinds, and a `cap` above
      `runtime.agents-in-flight` (TOOL-dBoundRoles-22 S5), each one line naming the entry and the
      stage. The row kinds are what the loop kit's `upstream.py kinds` prints; where it does not
      answer, each entry is graded by the `seg` shape alone and one `roles: note:` says so. With no
      policy kit the cap arm prints one `roles: note:` calling it unarmed and grades no cap. A
      well-formed harness the tree does not hold prints one `roles: note:`. THE SHAPES
      (TOOL-dBoundRoles-16): a `[[kind]]` row naming no kind of the five, a kind no row names, a
      row's unknown key, a `fan` or `cap` that is not an integer of at least 1 (on the `experiment`
      row, present at all), a `merge` outside its four values, a `twin` neither `never` nor a dotted
      policy key, and a `cap` above the agent limit; an entry's or a row's `kind` naming no row; a
      `checklist` or `orientation` neither `none` nor a `unit.<seg>` tag, or a tag the playbook
      kit's `read_units` holds no unit of, a `roles: note:` calling the join unarmed where that kit
      does not resolve; an entry's `merge` or `twin` as the row's; a `twin` entry whose `of` names
      no other entry, and `of` on any other; a `[workflow.experiment]` table on a non-experiment
      entry, or an experiment entry's table missing or breaking one of its rules, as
      `check_experiment_table` lists them; and one line per role and kind naming every stage whose
      kind, its row's else its entry's, the role's `shapes` does not declare. A row's `fan` and
      `cap` are graded after its kind's defaults, and a cap above the limit at the row only where
      the row sets it, since its kind's row is graded once. The summary counts the entries per kind
      and the unit tags resolved
  R10 a house overlay naming no role, or carrying a `# `/`## ` line, a token other than
      {{MEMORY_ROOT}}, or the file name of a protocol the charter's Protocols section names
  R11 the README's catalogue region absent, or different from a fresh render
  R12 a `house/policy.toml` defect, one line per line of `roles_lib.load_policy`'s refusal: the file
      unreadable or not TOML, an absent file being an empty fallback that no defect names, since each
      level then falls to the policy keys and the role's declared `effort` (TOOL-dBoundRoles-21 S7);
      an unknown key, no `default`, a level outside the five, a role entry
      naming no role file or an `agent: false` role, a stages table naming no workflow or a
      workflow with no stage rows, or a stage key that workflow's rows do not hold; under
      `effort.profiles`, a profile that is not a table, any of those defects in its own `default`,
      `roles` and `stages`, or a `match` that is absent, not a list of strings, empty, holding an
      entry that is not one word, or holding a word an earlier profile holds
      (TOOL-aProfiledEffort-1); under `[gates]`, a key
      naming no role file or an `agent: false` role, a value that is not a list of strings, or a
      leg name the tool root's gate manifest does not hold, checked only when that manifest reads
      and a `roles: note:` otherwise (TOOL-aOrientedCast-11); a name ending in `?` is optional, so
      a leg the manifest lacks is a `roles: note:` too, and a `?` alone names no leg
      (TOOL-aOrientedCast-13). A row there applies only to a role whose file carries no `gates`
      field, and both homes are graded by `roles_lib.check_gate_names` (TOOL-dBoundRoles-21 S6)
  R13 a `mandatory` value carrying a token other than {{MEMORY_ROOT}}; or one calling its role
      mandatory (anything but `no` or `no — <when>`) whose `workflow` entry's `enforced-by` holds no
      hook entry, one whose first word is a `.js` file name, and that carries no
      `unenforced — <why>` clause (TOOL-aOrientedCast-17); and each `never` entry
      `roles_lib.check_never_entries` refuses: no ` — `, an enforcer that is neither a script a kit
      holds (its first word a `.js`, `.py` or `.sh` file in the tool root or one directory under
      it), a `leg: <name>` of the tool root's gate manifest (a note where it does not read), nor
      `unenforced — <why>` with a reason (TOOL-dBoundRoles-2 S2). The summary counts the entries
      graded and the `unenforced` ones
  R14 an `output` value carrying a token other than {{MEMORY_ROOT}}; or a `spec`, `review`,
      `product` or `records` writer's `output` lacking its class's folder spelling from
      WRITE_FOLDERS (TOOL-aOrientedCast-17)
  R15 a row of `<MEMORY_ROOT>/project/role-stand-in-waiver.txt` with a bad date, attribution, role,
      build or reason, or repeating a held `(build, role)`; a `*-stand-in.md` handoff under a
      build's `prompts/` with no marker, or whose `(build, role)` no row covers; a row covering no
      such declaration (stale). Every valid row prints one `roles: note: stand-in waiver` line
      (TOOL-aOrientedCast-19)

WHAT THIS DOES NOT CHECK, because a structural check reads as a semantic one to everybody who did not
write it: the MEANING of a body; the truth of an `enforced-by` entry; a `tools:` name, which moves
with the CLI; a command harness, which is graded for presence only; and whether the kit of a harness
the tree does not hold should be installed, which is a `note` here and the wiring check's to report;
whether a cited rule suits its role; and whether a bare tag exists in every v4.x seed an adopter may
hold. An overlay's size is printed and never graded: it is the adopter's own text. R13 reads a
first word ending in `.js` as a hook by spelling convention alone, never asking whether that script
exists, is wired or refuses an inline stand-in. A `never` entry's script is graded for presence
alone and its leg for a name in the manifest: whether that enforcer refuses what the entry names is a
review question. R5's body arm sees only its four words, so a limit phrased otherwise ("you are not
designing in this pass") passes; R14 does not compare an `output` with where the role
actually writes; and a `mandatory` value's when-clause is never tested for truth. R15 does not check
whether the tool truly could not spawn, whether the `owner` who signed a row is the owner, whether a
reason says anything, whether a marker's build matches its folder, an inline stand-in nobody
declared, or a declared stand-in that was in fact spawned, which is harmless overstatement. R9 does
not compare a stage row's `fan` or `cap` with the harness literal it states, nor `cap` with `fan`,
nor whether a stage truly takes and hands on the row kinds it names, nor a key a row adds beside its
seven fields and its `kind`. Nor does it check what a merge or a twin does, which the harnesses own;
that a listed role of a stage-less entry declares the entry's kind; the value a `twin` key holds; a
unit's status, so a retired tag still joins; or that an experiment's `cases` file is a case set.
"""
import json
import os
import pathlib
import re
import subprocess
import sys
import tomllib

KIT_DIR = pathlib.Path(__file__).absolute().parent
sys.path.insert(0, str(KIT_DIR))
try:
    import roles_lib as lib  # noqa: E402  (the kit's own library, beside this file)
except Exception as _e:  # the library derives its key set from role-schema.toml at import: exit 2 naming it
    if type(_e).__name__ != "RolesError":
        raise
    print("roles: %s" % _e)
    sys.exit(2)

#: Bytes of each slot's BASE body, CR stripped. A new role is priced when it is added.
BODY_CEILINGS = {
    "gov-orienter": 3072, "gov-researcher": 3072, "gov-reuse-scout": 1536,
    "gov-spec-writer": 4096, "gov-builder": 4096,
    "gov-reviewer": 4096, "gov-skeptic": 3072, "gov-synthesizer": 3072, "gov-session": 2048,
    "gov-tester": 3072, "gov-prompt-writer": 3072, "gov-planner": 3072, "gov-architect": 3072,
}
WORKFLOW_NAMES = ("orient", "research", "reuse", "handoff", "spec-write", "spec-review", "build",
                  "closing-review", "gate-bar", "bookkeeping", "plan", "design")
WORKFLOW_KEYS = ("name", "driver", "harness", "roles", "stages", "enforced-by", "trigger",
                 "kind", "checklist", "orientation", "merge", "twin", "of", "experiment")
#: The entry keys R6 lets every entry omit: its stage rows, the two its kind defaults, and the two only a
#: `twin` or an `experiment` entry carries (TOOL-dBoundRoles-16 S2).
OPTIONAL_WORKFLOW_KEYS = ("stages", "merge", "twin", "of", "experiment")
#: The shape keys an entry listing no role may omit, as `bookkeeping` carries none (TOOL-dBoundRoles-16 S2).
SHAPE_KEYS = ("kind", "checklist", "orientation")
#: A `[[kind]]` row's keys, an entry's `merge` values and its `[workflow.experiment]` table's keys (S1, S4).
KIND_ROW_KEYS = ("kind", "fan", "cap", "merge", "twin")
MERGES = ("none", "concat", "synth", "defect-map")
EXPERIMENT_KEYS = ("cases", "variants", "fan", "scorer", "judge", "reruns")
#: A `checklist` or `orientation` tag's shape, the `unit` namespace's; R9 then joins it to a declared unit.
UNIT_TAG_RE = re.compile(r"^unit(\.[a-z0-9][a-z0-9-]*)+$")
#: A `twin` value other than `never`: a dotted policy key, whose value this kit never reads (S2).
POLICY_KEY_RE = re.compile(r"^[a-z][a-z0-9-]*(\.[a-z][a-z0-9-]*)+$")
DRIVERS = ("agent", "workflow", "program", "main-loop")
WRITES = ("none", "spec", "product", "review", "records")
#: The two `acts-as` values (TOOL-dBoundRoles-1 S1): a role acting in an item, or one serving the cycle.
ACTS_AS = ("item", "cycle")
#: A `layer` value's shape, the playbook register's tag grammar; R2 joins it to a row of that register.
LAYER_TAG_RE = re.compile(r"^layer(\.[a-z][a-z0-9-]*)+$")
#: The keys every role carries and those only an agent role must, and the required keys that may be
#: empty: derived from the role schema's rows, never typed (TOOL-dBoundRoles-2 S1).
_SCHEMA = lib.load_role_schema()
REQUIRED_ROLE_KEYS = tuple(r["key"] for r in _SCHEMA if r["required"] == "every")
AGENT_ROLE_KEYS = tuple(r["key"] for r in _SCHEMA if r["required"] == "agent")
EMPTY_ROLE_KEYS = frozenset(r["key"] for r in _SCHEMA if r["empty"])
#: Where each writer class's output lives (R14): the library's one table, which the rendered ceiling reads.
WRITE_FOLDERS = lib.WRITE_FOLDERS
#: A `mandatory` value calling its role optional: exactly `no`, or `no — <when it is used>` (R13).
NOT_MANDATORY_RE = re.compile(r"^no(?: — .+)?$")
#: A mandatory value's own statement that no hook enforces it (R13).
UNENFORCED_RE = re.compile(r"\bunenforced — \S")
#: An `enforced-by` entry naming a hook: its first word is a `.js` script's file name (R13).
HOOK_ENTRY_RE = re.compile(r"^[^\s/\\]+\.js(?=[\s,]|$)")
#: A backticked path ending in `.md` in the carried Protocols body: a protocol's file.
PROTOCOL_PATH_RE = re.compile(r"`([^`\s]*\.md)`")
STAGE_KEY_RE = re.compile(r"^[a-z][A-Za-z]*$")
#: A row kind's shape where the loop kit does not print its closed set: one tag segment, the loop kit's
#: `loop_lib.py#SEG` spelled again, since a kit imports no sibling kit (TOOL-dBoundRoles-22 §4).
ROW_KIND_SEG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
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
    out += ["| " + " | ".join(render_cell(lib.derive_stage_map(w) if k == "stages" else w.get(k))
                              for k in WORKFLOW_KEYS) + " |" for w in workflows]
    cols = ("workflow", "writes", "reads", "rules", "agent", "return")
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


def read_layer_tags(kit_dir):
    """`(tags, "")`, the `tag` of each `[[layer]]` row of the playbook kit's `layers.toml`, the kit found from
    `kit_dir` through `resolve_kit_dir`; `(None, why)` where it does not resolve or does not read, so R2's
    layer join is a note and never a pass (TOOL-dBoundRoles-1 S1)."""
    try:
        path = lib.resolve_kit_dir("playbook", "layers.toml", kit_dir) / "layers.toml"
        with open(path, "rb") as fh:
            rows = tomllib.load(fh).get("layer") or []
    except LookupError as e:
        return None, str(e)
    except (OSError, tomllib.TOMLDecodeError, UnicodeDecodeError) as e:
        return None, "the layer register does not read: %s" % e
    return {r.get("tag") for r in rows if isinstance(r, dict) and isinstance(r.get("tag"), str)}, ""


def read_unit_tags(root, kit_dir):
    """`(tags, "")`, the tag of every instruction unit the playbook kit's `read_units` reads in the
    repository at `root`, the kit found from `kit_dir` through `resolve_kit_dir` and its reader
    imported, as `read_cap_answer` reaches the policy kit; `(None, why)` where it does not resolve,
    import or read, so R9's unit join is a note and never a pass (TOOL-dBoundRoles-16 S6)."""
    try:
        kit = str(lib.resolve_kit_dir("playbook", "instruction_units.py", kit_dir))
        if kit not in sys.path:
            sys.path.insert(0, kit)
        import instruction_units  # the playbook kit's unit reader, found above
        return {u.tag for u in instruction_units.read_units(root) if u.tag}, ""
    except LookupError as e:
        return None, str(e)
    except ImportError as e:
        return None, "the playbook kit's unit reader does not import: %s" % e
    except ValueError as e:   # its UnitRowError and LevelError, a row or a git read it refuses
        return None, "the instruction units do not read: %s" % str(e).split("\n", 1)[0]


def read_scorer_instances(kit_dir):
    """`(keys, "")`, the `INSTANCES` keys of the workflows kit's `replay_scorer.py`, found from `kit_dir`
    through `resolve_kit_dir` and imported (TOOL-dFairHearing-12 S1); `(None, why)` where it does not
    resolve or import, so an experiment's scorer is a note and never a pass (TOOL-dBoundRoles-16 S4)."""
    try:
        kit = str(lib.resolve_kit_dir("workflows", "replay_scorer.py", kit_dir))
        if kit not in sys.path:
            sys.path.insert(0, kit)
        import replay_scorer  # the workflows kit's scorer factory, found above
        return set(replay_scorer.INSTANCES), ""
    except LookupError as e:
        return None, str(e)
    except (ImportError, AttributeError, SyntaxError) as e:
        return None, "the scorer factory does not import: %s" % e


def check_tracked_path(root, path):
    """True where `path`, repository-relative and forward-slashed, names one file git tracks at `root`."""
    if not isinstance(path, str) or not path.strip():
        return False
    p = subprocess.run(["git", "-C", str(root), "ls-files", "--", path], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", stdin=subprocess.DEVNULL,
                       env={k: v for k, v in os.environ.items() if not k.startswith("GIT_")})
    return p.returncode == 0 and p.stdout.splitlines() == [path]


def check_experiment_table(table, limit, root, kit_dir, notes):
    """What is wrong with an `experiment` entry's `[workflow.experiment]` table (TOOL-dBoundRoles-16 S4),
    one string per rule it breaks: `cases` a tracked file; `variants` a non-empty list of distinct
    `seg` words; `fan` an integer from 1 to `limit`, the agent limit, or from 1 where None; exactly one
    of `scorer`, an `INSTANCES` key of `replay_scorer.py`, and `judge`, a tracked label-key file; and
    every `reruns` key `<variant>.<level>` of a listed variant and an effort level, its value an integer
    of at least 1, each variant keyed at least once. A scorer factory that does not resolve appends one
    line to `notes` instead."""
    if not isinstance(table, dict):
        return ["declares no [workflow.experiment] table, which an experiment entry owes"]
    bad = ["experiment holds the unknown key '%s'" % k for k in table if k not in EXPERIMENT_KEYS]
    if not check_tracked_path(root, table.get("cases")):
        bad.append("experiment cases %r names no tracked file" % (table.get("cases"),))
    variants = table.get("variants")
    if (not isinstance(variants, list) or not variants or len(set(map(str, variants))) != len(variants)
            or not all(isinstance(v, str) and ROW_KIND_SEG_RE.match(v) for v in variants)):
        bad.append("experiment variants %r is not a non-empty list of distinct seg words" % (variants,))
        variants = [v for v in variants if isinstance(v, str)] if isinstance(variants, list) else []
    fan = table.get("fan")
    if not isinstance(fan, int) or isinstance(fan, bool) or fan < 1 or (limit is not None and fan > limit):
        bad.append("experiment fan %r is not an integer from 1 to %s" % (
            fan, "runtime.agents-in-flight %d" % limit if limit is not None else "the agent limit"))
    if "scorer" in table and "judge" in table:
        bad.append("experiment names both scorer and judge; it names exactly one")
    elif "scorer" not in table and "judge" not in table:
        bad.append("experiment names neither scorer nor judge; it names exactly one")
    elif "scorer" in table:
        held, why = read_scorer_instances(kit_dir)
        if held is None:
            notes.append("roles: note: no scorer factory answers, so an experiment's scorer %r is not joined to "
                         "an INSTANCES key: %s" % (table["scorer"], why))
        elif table["scorer"] not in held:
            bad.append("experiment scorer %r is no INSTANCES key of replay_scorer.py, whose keys are %s"
                       % (table["scorer"], ", ".join(sorted(held))))
    elif not check_tracked_path(root, table["judge"]):
        bad.append("experiment judge %r names no tracked label-key file" % (table["judge"],))
    reruns = table.get("reruns")
    if not isinstance(reruns, dict) or not reruns:
        bad.append("experiment reruns %r is not a table keyed <variant>.<level>" % (reruns,))
        return bad
    keyed = set()
    for key, value in reruns.items():
        variant, _dot, level = key.rpartition(".")
        if variant not in variants:
            bad.append("experiment reruns key %r names the variant %r, which variants does not list" % (key, variant))
        elif level not in lib.EFFORT_LEVELS:
            bad.append("experiment reruns key %r names the level %r, not one of %s"
                       % (key, level, " ".join(lib.EFFORT_LEVELS)))
        else:
            keyed.add(variant)
        if not isinstance(value, int) or isinstance(value, bool) or value < 1:
            bad.append("experiment reruns %r is %r, not an integer of at least 1" % (key, value))
    unkeyed = [v for v in variants if v not in keyed]
    if unkeyed:
        bad.append("experiment reruns keys no level of the variant(s) %s" % ", ".join(unkeyed))
    return bad


def check_roles(root, kit_dir, write=False):
    """`(defects, notes, summary)`; raises RolesError when the check is unarmed (R0)."""
    root, kit_dir = pathlib.Path(root), pathlib.Path(kit_dir)
    tool_root = kit_dir.parent
    charter_path = lib.resolve_charter_path(root)
    memory_root = lib.read_conf_key(root / ".memory-tree.conf", "MEMORY_ROOT")
    if not memory_root:
        raise lib.RolesError("%s: R0 — declares no MEMORY_ROOT key, or a blank one, so no memory root "
                             "holds the stand-in waiver registry" % (root / ".memory-tree.conf").as_posix())
    doc = resolve_display_path(root, charter_path)
    charter = lib.parse_charter(lib.load_text(charter_path), doc)
    defects, notes = [], []
    if charter["shape"] == "legacy":
        notes.append("roles: note: " + lib.LEGACY_NOTE % doc)
    protocols = dict(zip(lib.CARRIED_SECTIONS, charter["carried"])).get("Protocols", ("", ""))[1]
    protocol_files = sorted({m.rsplit("/", 1)[-1] for m in PROTOCOL_PATH_RE.findall(protocols)})

    def add_defect(path, rule, what):
        defects.append("roles: %s: %s — %s" % (resolve_display_path(root, path), rule, what))

    roles, n_reads, n_rules, n_outputs, n_mandatory, cited = {}, 0, 0, 0, 0, set()
    n_never, n_unenforced = 0, 0
    layer_tags, layer_why = read_layer_tags(kit_dir)
    if layer_tags is None:
        notes.append("roles: note: no layer register answered, so each role's layer is not joined to a row: %s"
                     % layer_why)
    by_layer, by_acts = {}, {}
    body_mode = None  # the `role-body` cap's (mode, rule), asked at the first body over its ceiling
    for p in sorted((kit_dir / "agents").glob("*.agent.md")):
        slot = p.name[:-len(".agent.md")]
        try:
            text = lib.load_text(p)
            keys, body = lib.parse_front_matter(resolve_display_path(root, p), text)
        except lib.RolesError as e:
            defects.append("roles: %s" % e)
            continue
        roles[slot] = {"path": p, "keys": keys, "body": body}
        for k in REQUIRED_ROLE_KEYS:
            if k not in keys or (k not in EMPTY_ROLE_KEYS and not keys[k]):
                add_defect(p, "R2", "front-matter key '%s' is missing" % k)
        if keys.get("return"):
            try:
                lib.parse_return_template(keys["return"])
            except lib.RolesError as e:
                add_defect(p, "R2", "return '%s': %s" % (keys["return"], str(e).split(" — ", 1)[-1]))
        if keys.get("name") and keys["name"] != slot:
            add_defect(p, "R2", "name '%s' is not the file stem '%s'" % (keys["name"], slot))
        if keys.get("writes") and keys["writes"] not in WRITES:
            add_defect(p, "R2", "writes '%s' is not one of %s" % (keys["writes"], " ".join(WRITES)))
        layer, acts = keys.get("layer"), keys.get("acts-as")
        if layer:
            by_layer[layer] = by_layer.get(layer, 0) + 1
            if not LAYER_TAG_RE.match(layer):
                add_defect(p, "R2", "layer '%s' is not a layer.<seg> tag" % layer)
            elif layer_tags is not None and layer not in layer_tags:
                add_defect(p, "R2", "layer '%s' names no [[layer]] row of the layer register" % layer)
        if acts:
            by_acts[acts] = by_acts.get(acts, 0) + 1
            if acts not in ACTS_AS:
                add_defect(p, "R2", "acts-as '%s' is not one of %s" % (acts, " ".join(ACTS_AS)))
        # TOOL-dBoundRoles-16 S5: the kinds the role runs in, each one of the five, none named twice
        shapes = lib.parse_role_shapes(keys.get("shapes"))
        off = [s for s in shapes if s not in lib.WORKFLOW_KINDS]
        if off or len(set(shapes)) != len(shapes):
            add_defect(p, "R2", "shapes '%s' is not a list of distinct kinds of %s"
                       % (keys["shapes"], " ".join(lib.WORKFLOW_KINDS)))
        if keys.get("agent", "true") not in ("true", "false"):
            add_defect(p, "R2", "agent '%s' is not true or false" % keys["agent"])
        if keys.get("agent", "true") == "true":
            for k in AGENT_ROLE_KEYS:
                if not keys.get(k):
                    add_defect(p, "R2", "'%s' is absent on an agent role" % k)
        # TOOL-dBoundRoles-21 S3, S4: the declared effort is a level, and `default` is no slot, since
        # `roles.effort.default` is the blanket level that `roles.effort.<role>` would read as a role
        if keys.get("effort") and keys["effort"] not in lib.EFFORT_LEVELS:
            add_defect(p, "R2", "effort '%s' is not one of %s" % (keys["effort"], " ".join(lib.EFFORT_LEVELS)))
        if slot == "default":
            add_defect(p, "R2", "the slot 'default' is reserved: roles.effort.default is the blanket level, so "
                       "roles.effort.<role> would read a role of that name as the blanket")
        seen = set()
        for item in [x.strip() for x in keys.get("reads", "").split(",") if x.strip()]:
            n_reads += 1
            base, optional = lib.parse_read_key(item)  # either spelling, `task:title` or `field.task.title`
            if base not in lib.READ_KEYS:
                add_defect(p, "R3", "reads key '%s' is outside the vocabulary" % item)
            if base in seen:
                add_defect(p, "R3", "reads key '%s' is named twice" % base)
            if base == "card:reuse" and not optional:
                add_defect(p, "R3", "card:reuse must be optional, 'card:reuse?': that section is not on every card")
            if base == "upstream:rows" and not optional:
                add_defect(p, "R3", "upstream:rows must be optional, 'upstream:rows?': only an item naming "
                                    "upstream items is handed rows")
            seen.add(base)
        entries = [x.strip() for x in keys.get("rules", "").split(",") if x.strip()]
        n_rules += len(entries)
        cited.update(e.rstrip("?") for e in entries)
        tag_defects, tag_notes = lib.check_rule_tags(charter, keys.get("rules", ""))
        for what in tag_defects:
            add_defect(p, "R4", what)
        notes.extend("roles: note: %s: %s" % (resolve_display_path(root, p), n) for n in tag_notes)
        for name in protocol_files:
            if name in body:
                add_defect(p, "R5", "body spells the protocol file %s; name the protocol, never its file" % name)
        ceiling = BODY_CEILINGS.get(slot)
        size = len(body.encode("utf-8"))
        if ceiling is None:
            add_defect(p, "R5", "slot '%s' has no ceiling row in BODY_CEILINGS" % slot)
        elif size > ceiling:
            # THE SWITCH (TOOL-dGroundRules-9): `role-body` is a family cap, so the policy kit is
            # asked only its mode, once, at the first body over its slot's ceiling. Under `warn` the
            # breach is a BUDGET WARN line and no defect; R5's other defects never move.
            if body_mode is None:
                body_mode = lib.read_cap_answer("role-body", root, kit_dir)[1:]
            if body_mode[0] == "warn":
                # The runner's `gate-warn` marker on the warning's next line, inside its own note, so it prints
                # where the notes print (TOOL-dWitnessedBar-29 S2); `read_cap_answer` loaded its factory.
                budgets = sys.modules.get("budgets")
                shown = resolve_display_path(root, p)
                notes.append("BUDGET WARN — role-body · %s · %d bytes over %d · %s" % (shown, size, ceiling, body_mode[1])
                             + ("\n" + budgets.render_warn_marker(shown, "role-body · %d bytes over %d" % (size, ceiling))
                                if budgets else ""))
            else:
                add_defect(p, "R5", "body is %d bytes, over its %d-byte ceiling (%s)" % (size, ceiling, body_mode[1]))
        if not body.strip():
            add_defect(p, "R5", "body is empty")
        if any(ln.startswith(("# ", "## ")) for ln in body.split("\n")):
            add_defect(p, "R5", "body carries a '# ' or '## ' heading line")
        # THE BODY ARM (TOOL-dBoundRoles-2 S3): a limit lives in `never` with its enforcer, so a body line
        # carrying a prohibition word is one defect naming its line in the file.
        folded = text.replace("\r\n", "\n")
        first = folded.count("\n", 0, folded.find(body, lib.FRONT_MATTER_RE.match(folded).end())) + 1
        for i, ln in enumerate(body.split("\n")):
            hit = lib.PROHIBITION_RE.search(ln)
            if hit:
                add_defect(p, "R5", "body line %d carries '%s', a limit: %r; move it to `never` as "
                           "'<limit> — <enforcer>' and keep the job in the body" % (first + i, hit.group(0), ln.strip()))
        entries = lib.parse_never_entries(keys.get("never", ""))
        n_never += len(entries)
        n_unenforced += sum(1 for _l, e in entries if e.startswith(lib.UNENFORCED_PREFIX))
        if keys.get("never"):
            never_notes = []
            for what in lib.check_never_entries(keys["never"], tool_root, never_notes):
                add_defect(p, "R13", what)
            notes.extend("roles: note: %s: %s" % (resolve_display_path(root, p), n) for n in never_notes)
        for token in sorted(set(lib.TOKEN_RE.findall(body)) - {lib.MEMORY_ROOT_TOKEN}):
            add_defect(p, "R5", "body carries the token %s; only %s renders" % (token, lib.MEMORY_ROOT_TOKEN))
        output = keys.get("output", "")
        for token in sorted(set(lib.TOKEN_RE.findall(output)) - {lib.MEMORY_ROOT_TOKEN}):
            add_defect(p, "R14", "output carries the token %s; only %s renders" % (token, lib.MEMORY_ROOT_TOKEN))
        folder = WRITE_FOLDERS.get(keys.get("writes"))
        if folder:
            n_outputs += 1
            if folder not in output:
                add_defect(p, "R14", "output '%s' does not name the %s class's folder, %s"
                           % (output, keys["writes"], folder))
    files = {p.name[:-len(".agent.md")] for p in (kit_dir / "agents").glob("*.agent.md")}
    if not files:
        add_defect(kit_dir / "agents", "R1", "DEAD PROBE: no role file, so this check graded nothing")
    elif charter["shape"] == "tagged" and not cited & set(charter["rules"]):
        add_defect(charter_path, "R1", "DEAD PROBE: no role's rules cites a practice tag of "
                   "this charter, so no rule reaches any agent")

    table = kit_dir / "workflows.toml"
    try:
        workflows = lib.load_workflows(kit_dir)
    except lib.RolesError as e:
        defects.append("roles: %s" % e)
        workflows = []
    if not workflows:
        add_defect(table, "R1", "DEAD PROBE: no workflow entry, so this check graded nothing")
    kind_rows = {}
    if workflows:
        try:
            kind_rows = lib.load_workflow_kinds(kit_dir)
        except lib.RolesError as e:
            defects.append("roles: %s" % e)
    # THE STAGE ROWS' TWO OUTSIDE READS (TOOL-dBoundRoles-22 S4, S5), each once per run: the agent limit a
    # `cap` is graded against, and the loop kit's closed set of row kinds, by its `kinds` verb.
    limit, limit_why = None, None
    try:
        limit = lib.read_agent_limit(root)
    except lib.RolesError as e:
        add_defect(table, "R9", "the agent limit does not read, so no stage cap is graded: %s" % e)
        limit_why = "refused"
    if limit is None and limit_why is None:
        limit_why = "unarmed"
        notes.append("roles: note: the stage cap arm is unarmed — no policy kit answers runtime.agents-in-flight, "
                     "so no stage row's cap is graded")
    kinds, kinds_why = None, None
    try:
        loop_kit = lib.resolve_kit_dir("loop", "upstream.py", kit_dir)
        p = subprocess.run([sys.executable, "-B", str(loop_kit / "upstream.py"), "kinds"], cwd=str(root),
                           capture_output=True, text=True, encoding="utf-8", errors="replace",
                           stdin=subprocess.DEVNULL, timeout=60,
                           env={k: v for k, v in os.environ.items() if not k.startswith("GIT_")})
        printed = [ln.strip() for ln in (p.stdout or "").splitlines() if ln.strip()]
        if p.returncode == 0 and printed:
            kinds = printed
        else:
            kinds_why = "its upstream.py kinds exited %d printing no kind" % p.returncode
    except LookupError as e:
        kinds_why = str(e)
    except (OSError, subprocess.SubprocessError) as e:
        kinds_why = "its upstream.py kinds did not run: %s" % e
    # THE KINDS (TOOL-dBoundRoles-16 S1, S3): each of the five named by one row, its keys known, its fan and
    # cap integers of at least 1, the cap at or under the agent limit, and `experiment`'s taken from its
    # entry's table; a cap a row takes from its kind is bounded here, once, and never again per row.
    def check_twin_value(at, value):
        if value != "never" and not (isinstance(value, str) and POLICY_KEY_RE.match(value)):
            add_defect(table, "R9", "%s twin %r is neither never nor a dotted policy key" % (at, value))
    for name, row in kind_rows.items():
        at = "kind row '%s'" % name
        if name not in lib.WORKFLOW_KINDS:
            add_defect(table, "R9", "%s names no kind of %s" % (at, " ".join(lib.WORKFLOW_KINDS)))
        for k in row:
            if k not in KIND_ROW_KEYS:
                add_defect(table, "R9", "%s has an unknown key '%s'" % (at, k))
        for field in ("fan", "cap"):
            v = row.get(field)
            if name == "experiment":
                if field in row:
                    add_defect(table, "R9", "%s carries %s; an experiment takes both from its entry's table's fan"
                               % (at, field))
            elif not isinstance(v, int) or isinstance(v, bool) or v < 1:
                add_defect(table, "R9", "%s: %s %r is not an integer of at least 1" % (at, field, v))
        if row.get("merge") not in MERGES:
            add_defect(table, "R9", "%s merge %r is not one of %s" % (at, row.get("merge"), " ".join(MERGES)))
        check_twin_value(at, row.get("twin"))
        cap = row.get("cap")
        if limit is not None and isinstance(cap, int) and not isinstance(cap, bool) and cap > limit:
            add_defect(table, "R9", "%s caps %d agents, above runtime.agents-in-flight %d" % (at, cap, limit))
    for name in lib.WORKFLOW_KINDS:
        if workflows and name not in kind_rows:
            add_defect(table, "R9", "no [[kind]] row declares the kind '%s'" % name)
    unit_tags, unit_why = read_unit_tags(root, kit_dir)
    if unit_tags is None:
        notes.append("roles: note: the unit join is unarmed — no playbook kit reads the instruction units, so "
                     "no checklist or orientation tag is joined to a declared unit: %s" % unit_why)
    named_units, by_kind = set(), {}
    stage_kinds = {}   # (slot, kind) -> the stages a role runs in under a kind its `shapes` does not declare
    table_names = {w.get("name") for w in workflows}
    n_stage_rows, kinds_noted = 0, False
    by_name = {}
    for i, w in enumerate(workflows, 1):
        where = "entry %d (%s)" % (i, w.get("name", "unnamed"))
        for k in w:
            if k not in WORKFLOW_KEYS:
                add_defect(table, "R6", "%s has an unknown key '%s'" % (where, k))
        lists_role = isinstance(w.get("roles"), list) and bool(w["roles"])
        for k in WORKFLOW_KEYS:
            if k not in OPTIONAL_WORKFLOW_KEYS and (lists_role or k not in SHAPE_KEYS) and k not in w:
                add_defect(table, "R6", "%s is missing key '%s'" % (where, k))
        name = w.get("name")
        if name not in WORKFLOW_NAMES:
            add_defect(table, "R6", "%s names an unknown workflow" % where)
        elif name in by_name:
            add_defect(table, "R6", "%s repeats the name '%s'" % (where, name))
        else:
            by_name[name] = w
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
        # THE SHAPE (TOOL-dBoundRoles-16 S2, S4, S6): the kind a row of the kinds, each unit tag a declared
        # unit, the merge and twin rule, `of` on a twin entry alone, the experiment table on an experiment's.
        kind = w.get("kind")
        if "kind" in w:
            if not isinstance(kind, str) or kind not in kind_rows:
                add_defect(table, "R9", "%s kind %r names no [[kind]] row" % (where, kind))
            else:
                by_kind[kind] = by_kind.get(kind, 0) + 1
        for field in ("checklist", "orientation"):
            tag = w.get(field)
            if field not in w or tag == "none":
                continue
            if not isinstance(tag, str) or not UNIT_TAG_RE.match(tag):
                add_defect(table, "R9", "%s %s %r is neither none nor a unit.<seg> tag" % (where, field, tag))
            elif unit_tags is not None and tag not in unit_tags:
                add_defect(table, "R9", "%s %s '%s' names no declared unit of the instruction units"
                           % (where, field, tag))
            elif unit_tags is not None:
                named_units.add(tag)
        if "merge" in w and w["merge"] not in MERGES:
            add_defect(table, "R9", "%s merge %r is not one of %s" % (where, w["merge"], " ".join(MERGES)))
        if "twin" in w:
            check_twin_value(where, w["twin"])
        if kind == "twin":
            if not isinstance(w.get("of"), str) or w["of"] not in table_names or w["of"] == w.get("name"):
                add_defect(table, "R9", "%s is a twin entry and its of %r names no other entry"
                           % (where, w.get("of")))
        elif "of" in w:
            add_defect(table, "R9", "%s carries of on a %r entry; only a twin entry runs another twice" % (where, kind))
        if kind == "experiment":
            for what in check_experiment_table(w.get("experiment"), limit, root, kit_dir, notes):
                add_defect(table, "R9", "%s %s" % (where, what))
        elif "experiment" in w:
            add_defect(table, "R9", "%s carries a [workflow.experiment] table on a %r entry" % (where, kind))
        if w.get("driver") == "workflow":
            harness = w.get("harness", "")
            if not isinstance(harness, str) or not JS_HARNESS_RE.match(harness):
                add_defect(table, "R9", "%s harness %r is not a {prefix}/<home>/<file>.js path" % (where, harness))
            else:
                _, held = lib.resolve_harness_path(tool_root, harness)
                if not held:
                    notes.append("roles: note: %s harness %s is not held by this tree" % (where, harness))
        stages = w.get("stages")
        if stages is None:
            if w.get("driver") == "workflow":
                add_defect(table, "R9", "%s is driven by a workflow and declares no [[workflow.stages]] row, "
                           "so no harness stage takes a role" % where)
        elif w.get("driver") != "workflow":
            add_defect(table, "R9", "%s carries stage rows on a '%s' driver" % (where, w.get("driver")))
        elif not isinstance(stages, list) or not stages or not all(isinstance(r, dict) for r in stages):
            add_defect(table, "R9", "%s stages is not a non-empty array of [[workflow.stages]] tables" % where)
        else:
            seen_keys = set()
            for raw, row in zip(stages, lib.derive_stage_rows(w, kind_rows)):
                n_stage_rows += 1
                key = row.get("key")
                stage = "%s stage %s" % (where, key if isinstance(key, str) else repr(key))
                if not isinstance(key, str) or not STAGE_KEY_RE.match(key):
                    add_defect(table, "R9", "%s: key %r does not match %s" % (stage, key, STAGE_KEY_RE.pattern))
                elif key in seen_keys:
                    add_defect(table, "R9", "%s: the key is repeated in its entry" % stage)
                seen_keys.add(key if isinstance(key, str) else None)
                slot = row.get("role")
                if slot not in listed:
                    add_defect(table, "R9", "%s maps to %r, which its roles do not list" % (stage, slot))
                elif slot in roles and roles[slot]["keys"].get("agent", "true") == "false":
                    add_defect(table, "R9", "%s maps to '%s', an agent: false role" % (stage, slot))
                # TOOL-dBoundRoles-16 S2, S5: the row's kind, its own else its entry's, is a kind its role
                # declares; a role that declares none is R2's, so it is named once
                row_kind = row.get("kind")
                if "kind" in raw and (not isinstance(raw["kind"], str) or raw["kind"] not in kind_rows):
                    add_defect(table, "R9", "%s: kind %r names no [[kind]] row" % (stage, raw["kind"]))
                elif (isinstance(row_kind, str) and row_kind in kind_rows and slot in listed and slot in roles
                      and roles[slot]["keys"].get("shapes")
                      and row_kind not in lib.parse_role_shapes(roles[slot]["keys"]["shapes"])):
                    stage_kinds.setdefault((slot, row_kind), []).append("%s.%s" % (w.get("name"), key))
                for field in ("fan", "cap"):
                    v = row.get(field)
                    if not isinstance(v, int) or isinstance(v, bool) or v < 1:
                        add_defect(table, "R9", "%s: %s %r is not an integer of at least 1" % (stage, field, v))
                if row.get("effort") not in lib.EFFORT_LEVELS:
                    add_defect(table, "R9", "%s: effort %r is not one of %s"
                               % (stage, row.get("effort"), " ".join(lib.EFFORT_LEVELS)))
                for field in ("receives", "returns"):
                    v = row.get(field)
                    if not isinstance(v, list) or not all(isinstance(x, str) for x in v):
                        add_defect(table, "R9", "%s: %s %r is not a list of row kinds" % (stage, field, v))
                        continue
                    if kinds is None and v and not kinds_noted:
                        kinds_noted = True
                        notes.append("roles: note: no loop kit prints its row kinds, so each stage row's "
                                     "receives and returns are graded by the seg shape alone: %s" % kinds_why)
                    off = [x for x in v if (x not in kinds if kinds is not None else not ROW_KIND_SEG_RE.match(x))]
                    if off:
                        add_defect(table, "R9", "%s: %s holds %s, outside the row kinds %s" % (
                            stage, field, ", ".join(repr(x) for x in off),
                            " ".join(kinds) if kinds is not None else "(the seg shape %s)" % ROW_KIND_SEG_RE.pattern))
                cap = raw.get("cap")   # a cap the row's kind gives it is bounded at its [[kind]] row
                if limit is not None and isinstance(cap, int) and not isinstance(cap, bool) and cap > limit:
                    add_defect(table, "R9", "%s caps %d agents, above runtime.agents-in-flight %d" % (stage, cap, limit))
    for (slot, kind), at in stage_kinds.items():
        add_defect(roles[slot]["path"], "R9", "shapes '%s' does not declare the kind '%s', which its stage(s) %s "
                   "run in" % (roles[slot]["keys"]["shapes"], kind, ", ".join(at)))
    for name in WORKFLOW_NAMES:
        if workflows and name not in by_name:
            add_defect(table, "R6", "the workflow '%s' has no entry" % name)
    # THE JOIN WITH THE LOOP DEFINITION, both ways (TOOL-dDeclaredLoop-1): a workflow's order and step
    # are written there alone, so each workflow here has one row there and each row there names one here.
    if workflows:
        try:
            placed = lib.read_workflow_order(kit_dir)
        except lib.RolesError as e:
            add_defect(table, "R6", str(e))
        else:
            for name in by_name:
                if name not in placed:
                    add_defect(table, "R6", "the workflow '%s' has no [[workflow]] row in the loop "
                               "definition, so no loop row places it" % name)
            for name in placed:
                if name not in by_name:
                    add_defect(table, "R6", "the loop definition's [[workflow]] row '%s' names no "
                               "workflow of this table" % name)

    listed_anywhere = {s for w in workflows if isinstance(w.get("roles"), list) for s in w["roles"]}
    for slot, r in roles.items():
        wf = r["keys"].get("workflow")
        if wf and wf not in by_name:
            add_defect(r["path"], "R7", "workflow '%s' names no entry in workflows.toml" % wf)
        elif wf and slot not in by_name[wf].get("roles", []):
            add_defect(r["path"], "R7", "the '%s' entry's roles does not list %s" % (wf, slot))
        value = r["keys"].get("mandatory", "")
        for token in sorted(set(lib.TOKEN_RE.findall(value)) - {lib.MEMORY_ROOT_TOKEN}):
            add_defect(r["path"], "R13", "mandatory carries the token %s; only %s renders"
                       % (token, lib.MEMORY_ROOT_TOKEN))
        if not value or NOT_MANDATORY_RE.match(value) or wf not in by_name:
            continue
        n_mandatory += 1
        enforced = by_name[wf].get("enforced-by")
        hooked = isinstance(enforced, list) and any(
            isinstance(e, str) and HOOK_ENTRY_RE.match(e) for e in enforced)
        if not hooked and not UNENFORCED_RE.search(value):
            add_defect(r["path"], "R13", "mandatory '%s' calls this role mandatory, and the '%s' entry's "
                       "enforced-by names no hook; name the hook script there, or say 'unenforced — <why>' "
                       "in the value" % (value, wf))
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
        for name in protocol_files:
            if name in text:
                add_defect(p, "R10", "overlay spells the protocol file %s; name the protocol, never its file" % name)

    try:
        policy_notes = []
        lib.load_policy(kit_dir, roles, workflows, policy_notes)
        notes.extend("roles: note: %s" % n for n in policy_notes)
    except lib.RolesError as e:
        defects.extend("roles: %s" % ln for ln in str(e).split("\n"))

    # R15 — the owner's stand-in waiver rows joined with the declarations, both ways (TOOL-aOrientedCast-19).
    waivers, bad = lib.load_stand_in_waivers(root, memory_root, roles)
    declared, scan_bad = lib.scan_stand_in_declarations(root, memory_root)
    defects.extend("roles: %s" % ln for ln in bad + scan_bad)
    registry = (pathlib.Path(memory_root) / "project" / lib.STAND_IN_WAIVER).as_posix()
    for d in declared:
        if (d["build"], d["role"]) not in waivers:
            add_defect(root / d["path"], "R15", "no waiver row in %s covers this stand-in for role %s in "
                       "build %s" % (registry, d["role"], d["build"]))
    held = {(d["build"], d["role"]) for d in declared}
    for (build, role), w in waivers.items():
        if (build, role) not in held:
            defects.append("roles: %s:%d: R15 — stale: it covers no stand-in declaration of role %s "
                           "under %s/builds/%s/prompts/" % (registry, w["line"], role, memory_root, build))
        notes.append("roles: note: stand-in waiver %s owner %s %s %s — %s"
                     % (w["date"], w["who"], role, build, w["reason"]))

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

    summary = ("roles: graded %d roles, %d overlays, %d workflows (by kind %s; %s), %d stage rows against "
               "runtime.agents-in-flight %s, %d reads keys, %d mandatory roles, "
               "%d writer outputs, %d never entries (%d unenforced), %d rule tags and %d protocol file "
               "names against %s, a %s charter; roles by layer %s, by acts-as %s; "
               "overlay bytes %s; %d stand-in waiver(s), %d stand-in declaration(s); %d defect(s)" % (
                   len(files), len(overlays), len(workflows),
                   ", ".join("%s=%d" % kv for kv in sorted(by_kind.items())) or "none",
                   "%d unit tag(s) resolved" % len(named_units) if unit_tags is not None else "units unarmed",
                   n_stage_rows,
                   limit if limit is not None else limit_why, n_reads, n_mandatory, n_outputs, n_never,
                   n_unenforced, n_rules,
                   len(protocol_files), doc,
                   "tagged" if charter["shape"] == "tagged" else "pre-tag",
                   ", ".join("%s=%d" % kv for kv in sorted(by_layer.items())) or "none",
                   ", ".join("%s=%d" % kv for kv in sorted(by_acts.items())) or "none",
                   ", ".join("%s=%d" % kv for kv in overlays.items()) or "none",
                   len(waivers), len(declared), len(defects)))
    return defects, notes, summary


def print_tag_rows(mode, text):
    """`--print-tag-rows role|stage` (TOOL-dBoundRoles-14 S2, S3): one JSON object per member,
    `{"tag", "line", "text"}`, of the text handed on stdin and of nothing else, so the tag index's rows
    stay keyed by committed blob. `role`: a role file's `role.<name>` at its `name:` line, its text the
    raw `rules` value, through `parse_front_matter`. `stage`: each distinct stage key of every
    `[[workflow]]` entry's stage rows, through `derive_stage_map`, `derive_stage_field_tag`'s fold at the
    first `key =` line of a `[[workflow.stages]]` row carrying it (TOOL-dBoundRoles-22 S2), its text the
    key. The rows are not validated: a malformed name is the shape check's to red.
    A text that does not parse prints the defect on stderr, exit 2."""
    text = text.replace("\r\n", "\n")
    rows = []
    if mode == "role":
        try:
            keys, _body = lib.parse_front_matter("<stdin>", text)
        except lib.RolesError as e:
            print("roles: %s" % e, file=sys.stderr)
            return 2
        if keys.get("name"):
            n = next((i for i, ln in enumerate(text.split("\n"), 1) if ln.startswith("name:")), 1)
            rows.append({"tag": "role." + keys["name"], "line": n, "text": keys.get("rules", "")})
    else:
        try:
            entries = tomllib.loads(text).get("workflow") or []
        except tomllib.TOMLDecodeError as e:
            print("roles: <stdin>: R6 — not valid TOML — %s" % e, file=sys.stderr)
            return 2
        # the line of each row's `key =`, read inside a `[[workflow.stages]]` table only, first one wins
        at, table = {}, None
        for i, ln in enumerate(text.split("\n"), 1):
            head = re.match(r"\s*\[\[?\s*([^\]]*?)\s*\]\]?", ln)
            if head:
                table = head.group(1)
                continue
            m = re.match(r"""\s*key\s*=\s*(["'])(.*?)\1""", ln)
            if table == "workflow.stages" and m:
                at.setdefault(m.group(2), i)
        seen = set()
        for entry in entries if isinstance(entries, list) else ():
            for key in lib.derive_stage_map(entry):
                tag = lib.derive_stage_field_tag(key)
                if tag in seen:
                    continue
                seen.add(tag)
                rows.append({"tag": tag, "line": at.get(key, 1), "text": key})
    for row in rows:
        print(json.dumps(row, ensure_ascii=False))
    return 0


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    args, root, write = list(argv), None, False
    if args[:1] == ["--print-tag-rows"] and args[1:] in (["role"], ["stage"]):
        return print_tag_rows(args[1], sys.stdin.buffer.read().decode("utf-8", "replace"))
    while args:
        a = args.pop(0)
        if a == "--write":
            write = True
        elif a == "--root" and args:
            root = args.pop(0)
        else:
            print("usage: python check_roles.py [--root <dir>] [--write] | --print-tag-rows role|stage",
                  file=sys.stderr)
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
