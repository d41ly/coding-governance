"""roles_lib — the one reader of the role catalogue, and the one composition of a role (TOOL-aOrientedCast-1).

Reads the role files under `agents/`, the workflow table `workflows.toml`, the memory-tree conf and
the governing doc: its practices' rule tags and its carried sections (TOOL-aOrientedCast-16). It is
also the one reader of the owner's stand-in waiver registry and of the stand-in declarations under
the builds' `prompts/` folders (TOOL-aOrientedCast-19), and of the governing doc's micro-format
fence, `<!-- microformats -->` to `<!-- /microformats -->`, whose `agent` and `returned` shapes
`handoff.py agents` fills (TOOL-aOrientedCast-20): each marker a whole line and the last definition
of a head winning, as the hooks kit's format guard reads the fence (TOOL-aOrientedCast-25). Its
`extract_prompt_marker` reads an `Agent` prompt's marker line as the hooks kit's spawn guard does.
`render_role` is the one composition of a role with the repository's own rules for it, the overlay's
level-5 units selecting it, which `read_role_units` reads (TOOL-dBoundRoles-19), and `render_charter_blocks`
the one composition of the charter text a role carries: every consumer that hands a role to an agent
calls both, so a role reaches an agent the same way by every route. `render_static_block` composes the
two into the agent file's body, the block R5 measures against the role's `budget`, and
`check_single_carry` keeps `instructions.task-charter` from carrying the charter twice (TOOL-dBoundRoles-15).
`render_role_section` is the one composition of a handoff's `## Role` section and `derive_section_sha` the
one hash of it, so the role index's `role-sha` and a handoff marker's are one value (TOOL-dBoundRoles-6).
`derive_fact_key` is the one key of a handed fact and `derive_fact_class` its one class, written on the
`FACT_RE` line `render_fact_line` composes (TOOL-dBoundRoles-13). `render_handed_fence` fences each handed
value and `read_unfenced_lines` is the one fence walker every reader of a fact or marker line walks, so a
line quoted inside handed content is content (TOOL-dBoundRoles-38). `check_return` is the one checker of a
direct return against its role's typed `return` template, shared interface I16 (TOOL-dBoundRoles-5). Stdlib only; every text read
folds CRLF to LF and names its encoding.

The front-matter grammar: a `---` block at line 1, one `key: value` per line at COLUMN 0, values kept
RAW (a list is comma-separated on one line, the form Claude Code's own `tools:` takes). An indented,
a repeated or an unknown key is refused, because a simple parser drops an indented key without a
word and a repeated one silently keeps the last. The keys are the rows of `role-schema.toml` beside
this file, read by `load_role_schema` at import (TOOL-dBoundRoles-2): `never` is parsed by
`parse_never_entries` and graded by `check_never_entries`, `return` by `parse_return_template`, and
`render_role` closes a role with the `## Never`, `## Ceiling` and `## Return` sections
`render_role_fields` composes.
"""
import datetime
import hashlib
import json
import pathlib
import re
import tomllib

KIT_ROLES_VERSION = "1.25"

#: The closed `reads` vocabulary, one literal: each family and its field names. A key is
#: `<family>:<field>`, its tag `field.<family>.<field>` (TOOL-dBoundRoles-14), either spelling legal in a
#: `reads` value and a trailing `?` marking one optional. The tag index reads this assignment from the
#: committed blob, so it stays one literal.
READ_FAMILIES = {"task": ("title", "goal", "in", "out", "todo", "reuse", "acceptance", "gates"),
                 "card": ("route", "records", "classes", "read", "open", "reuse"),
                 "brief": ("prompt", "goal", "items", "acceptance", "gates", "non-goals"),
                 # `work-order`, the destination's resolved work order, is filled only by `handoff.py render
                 # --for <role>`, never by an `--input` (TOOL-dBoundRoles-4 S1)
                 "input": ("spec", "diff", "question", "prompt", "work-order"),
                 # the rows an item's upstream items established, handed on by `handoff.py render --upstream`,
                 # legal only optional since only an item naming upstream items has them (TOOL-dDeclaredLoop-29)
                 "upstream": ("rows",)}
READ_KEYS = frozenset("%s:%s" % (f, n) for f, names in READ_FAMILIES.items() for n in names)

#: The reasoning-effort levels a role or a stage may take (TOOL-aOrientedCast-10). Read from Claude
#: Code 2.1.292, whose agent loader and `Workflow` `agent()` options both take these five names; the
#: integer form only the loader accepts is refused, so one level is legal on both carriers.
EFFORT_LEVELS = tuple("low medium high xhigh max".split())
#: The floor every resolved or declared level holds (TOOL-dBoundRoles-23 S5), its one spelling: a level below
#: it passes `check_effort_floor` only from a `roles.effort.*` key of the guarded policy file, and only while
#: that file's `policy-file.guard` is `owner-only`, under which the owner's terminal commit writes there.
EFFORT_FLOOR = "medium"
EFFORT_POLICY_FILE = ".governance/policy.toml"
EFFORT_POLICY_PREFIX = "roles.effort."
EFFORT_GUARD_KEY, EFFORT_GUARD_OWNER = "policy-file.guard", "owner-only"
POLICY_EFFORT_KEYS = ("default", "roles", "stages")
#: One word of a model id, a run of lower-case letters and digits (TOOL-aProfiledEffort-1):
#: `resolve_profile` splits a lower-cased id into them, and a profile's `match` entry is exactly one.
MODEL_SEGMENT_RE = re.compile(r"[a-z0-9]+")
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
#: The practices' marker pair inside the region (PLAY-dOrderedCharter-2 S6): the rule lines sit between them,
#: each marker a whole line, so a role's tag resolves to its practice line whatever the headings say.
PRACTICES_OPEN, PRACTICES_CLOSE = "<!-- gov:practices -->", "<!-- /gov:practices -->"
#: A charter seeded before the markers holds its practices under a numbered first heading, read through
#: this pattern alone until it is reseeded.
SECTION_ONE_RE = re.compile(r"^## 1\. ")
#: A practice's rule line, `- [<tag>] <text>`; the whole line is the rule.
RULE_LINE_RE = re.compile(r"^- \[([a-z0-9][a-z0-9-]*)\] ")
#: One entry of a role's `rules` value: a tag, a trailing `?` marking it optional.
RULE_KEY_RE = re.compile(r"^[a-z0-9][a-z0-9-]*\??$")
#: The charter headings every agent type and handoff carries whole, in this order (§8 F3).
CARRIED_SECTIONS = ("Protocols", "Facts")
#: A v3.x charter's numbered heading, kept only to tell a pre-tag charter from an unknown doc.
SECTION_RE = re.compile(r"^## (§\d+) — ")
LEGACY_NOTE = ("%s is a pre-tag charter: it carries `## §<n> — ` headings and no practice rule tag, "
               "so no role's rules resolve and no agent type or handoff carries the charter; reseed "
               "the charter template from gov, then re-render")
HARNESS_RE = re.compile(r"^\{prefix\}/([^/{}\s]+)/([^/{}\s]+)$")
#: A `{{TOOL_ROOT}}<home>/<file>` citation, the shape `derive_kit_paths` reads (render-doc.sh:162).
TOOL_ROOT_CITE_RE = re.compile(r"\{\{TOOL_ROOT\}\}([\w.-]+)/([\w.-]+)")
#: A build slug, as `handoff.py render --build` takes it and a stand-in waiver row names it.
SLUG_RE = re.compile(r"^[A-Za-z]+$")
#: The rendered handoff's marker line; `handoff.py` reads this one pattern (TOOL-aOrientedCast-19), every
#: reader by group name. `item=` is optional, so a marker written before it parses with `item` None; the
#: renderer always writes it, the item tag or `-` (TOOL-dBoundRoles-17 S1).
MARKER_RE = re.compile(r"^<!-- gov:handoff role=(?P<role>\S+) build=(?P<build>\S+) "
                       r"unit=(?P<unit>\S+)(?: item=(?P<item>\S+))? path=(?P<path>\S+) "
                       r"role-sha=(?P<role_sha>[0-9a-f]{12}) task-sha=(?P<task_sha>[0-9a-f]{12}) -->$", re.M)
#: A handed fact's line (TOOL-dBoundRoles-13 S3): the one grammar of the line `render_handoff` writes atop each
#: `reads` block, its key `derive_fact_key`'s and its class `derive_fact_class`'s; the hooks kit's spawn guard
#: spells it again, as a kit imports no sibling kit. A text's fact lines are read only on the lines
#: `read_unfenced_lines` yields, so a fact line quoted inside handed content is content (TOOL-dBoundRoles-38 S4).
FACT_RE = re.compile(r"^<!-- gov:fact key=(?P<key>\S+) class=(?P<class>witnessed|decided|claimed) -->$", re.M)
#: An anchor (TOOL-dBoundRoles-24 S1): a backticked span whose text opens with a fact-key prefix `derive_fact_key`
#: writes, `blob:`, `record:` or `cmd:`, its text the group `span`. The group `key` is set only where the span is a
#: whole key of its form, `blob:<path>@<12 hex>:<lo>-<hi>`, `record:<id>@<12 hex>` or `cmd:<12 hex>:<12 hex>`; a
#: span the prefix opens with any other shape is a malformed anchor. A blob's `lo <= hi` is `check_anchors`'.
ANCHOR_RE = re.compile(r"`(?P<span>(?P<key>blob:[^`\s]+@[0-9a-f]{12}:[1-9][0-9]*-[1-9][0-9]*"
                       r"|record:[^`\s]+@[0-9a-f]{12}|cmd:[0-9a-f]{12}:[0-9a-f]{12})|(?:blob|record|cmd):[^`]*)`")
#: The `--input` names whose value is typed on the command line rather than read from a file: each is keyed
#: `cmd:` over the fixed argv `--input`, NUL, `<name>`, which is how `derive_fact_class` tells it `claimed`.
ARGUMENT_INPUTS = ("diff", "question")
#: A record's status header whose tail carries `ratified <date>`, which classes its facts `decided`.
RATIFIED_RE = re.compile(r"^\*\*Status:\*\*.*\bratified [0-9]{4}-[0-9]{2}-[0-9]{2}\b", re.M)
#: An `item=` tag the renderer admits: `item.<step>.<name>`, the loop kit's item tag shape, its segment the
#: loop kit's `SEG`, the adopter form `item.<step>.adopter.<name>` included (TOOL-dBoundRoles-17 S3).
ITEM_VALUE_RE = re.compile(r"^item(\.[a-z0-9][a-z0-9-]*){2,}$")
#: A return's header line naming the work order it answers (TOOL-dBoundRoles-17 S4): the value
#: `derive_answers_value` writes, behind the bold key. A harness return's `answers` field is the same
#: value without the key.
ANSWERS_RE = re.compile(r"^\*\*Answers:\*\* (?P<path>\S+) task-sha=(?P<task_sha>[0-9a-f]{12})$", re.M)
ANSWERS_KEY = "**Answers:**"
#: A harness or direct return's `answers` value: `ANSWERS_RE`'s body without its bold key, derived from it
#: so the two cannot drift (TOOL-dBoundRoles-5 S1, the form TOOL-dBoundRoles-17 §4 grades `answers` by).
ANSWERS_VALUE_RE = re.compile(ANSWERS_RE.pattern.replace("^" + re.escape(ANSWERS_KEY) + " ", "^", 1))
#: The work-order legacy population's home under `<MEMORY_ROOT>/project/`, seeded once (R16), and the
#: line a seed that failed leaves at its head, the memory-tree kit's `legacy_ledger.UNARMED_LEAD`.
WORK_ORDER_LEGACY = "work-order-legacy.txt"
LEGACY_UNARMED_LEAD = "# unarmed · "
#: The owner's stand-in waiver registry under `<MEMORY_ROOT>/project/`, and the file-name tail a
#: handoff rendered by a stand-in carries before `.md` (TOOL-aOrientedCast-19).
STAND_IN_WAIVER = "role-stand-in-waiver.txt"
STAND_IN_TAIL = "-stand-in"
WAIVER_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
WAIVER_OWNER_RE = re.compile(r"^owner \S+$")
#: The governing doc's micro-format fence and one definition line inside it (TOOL-aOrientedCast-20).
MICROFORMATS_OPEN, MICROFORMATS_CLOSE = "<!-- microformats -->", "<!-- /microformats -->"
MICROFORMAT_LINE_RE = re.compile(r"^- `(.*)`$")
#: The one line an agent-type or handoff render prints with no playbook kit, so no registry ranks its
#: blocks (PLAY-dOrderedCharter-5 F4); `%s` is the resolver's refusal, which names where it looked.
UNRANKED_NOTE = "envelope — unarmed · no playbook kit, so the blocks render unranked: %s"
#: Where an agent role's type renders, repo-relative: the file whose body `render_static_block` composes.
AGENTS_REL = ".claude/agents"
#: The work-order template under a kit directory, and its slot line; a ranked section's `LEAD_SLOTS` open
#: its envelope (PLAY-dOrderedCharter-5 S2). `render_role_section` reads the template of the kit it is handed.
WORK_ORDER_REL = "templates/work-order.template.md"
WORK_ORDER_SLOT_RE = re.compile(r"<!-- slot: ([a-z-]+) -->")
WORK_ORDER_LEAD_SLOTS = ("practices",)
WORK_ORDER_TASK_RE = re.compile(r"^## Task$", re.M)
#: The record kind `work-order`, `record-kind.work-order` (TOOL-dBoundRoles-3 S6, §8 F1): its folder, its name
#: grammar, `handoff.py#derive_prompt_name`'s, its door, its required parts in order (the marker with `item=`, the
#: two sections and the five blocks of an item's task) and its readers, on the one line a grep of its name prints.
#: dTotalRecall's registry reads it when it lands.
WORK_ORDER_KIND = {"kind": "work-order", "tag": "record-kind.work-order", "folder": "<MEMORY_ROOT>/builds/<slug>/prompts/", "name": "<date>-prompt-<unit id>-<n>-<role without gov-><tail>.md", "door": "handoff.py render --item", "parts": ("<!-- gov:handoff ... item=<tag> ... -->", "## Role", "## Task", "### item", "### inputs", "### allowance", "### return", "### witness"), "readers": ("handoff.py#check_handoff", "spawn-guard.js rule 6", "check_roles.py R16")}
#: The five blocks an item's work order carries at the end of `## Task`, in order: the kind's parts after the
#: marker and the two sections, so `render_handoff` writes and `check_handoff` reads one list.
WORK_ORDER_BLOCKS = WORK_ORDER_KIND["parts"][3:]
#: The work order's frame, shared interface I15 (TOOL-dBoundRoles-23 S1): aScoutedSeam's prompt skeleton, its
#: nine slots in order. Every block of the work-order template's `reads` fill carries one, and `derive_frame`
#: sorts that fill by it; the practices, the card's block and the opening line ahead of it carry none (§8 F5).
FRAME_SLOTS = ("role", "material", "boundaries", "population", "upstream", "contract", "added", "no-stop", "return")
#: The bound on a list the frame renders, and on a return's `list` field where no population sets one (S3,
#: §4 "The bound"), pinned from the night pass two's reuse-scout contract, "at most twelve seams" (NT-10).
FRAME_LIST_BOUND = 12
#: A `list` field's bound as a work order's `### return` block states it, and the pattern `check_return`
#: reads it back by, so the bound lives in the rendered work order and nowhere else.
RETURN_BOUND_LINE = "%s: at most %d entries"
RETURN_BOUND_RE = re.compile(r"^(?P<field>[A-Za-z][A-Za-z0-9_-]*): at most (?P<bound>[0-9]+) entries$")
#: The charter's drive section heading and one drive line, `- <stage> · <role> — ` (PLAY-dOrderedCharter-6).
DRIVE_HEAD = "## Drive — "
DRIVE_LINE_RE = re.compile(r"^- \S+ · (\S+) — ")


class RolesError(Exception):
    """The one exception of this kit; its message names the file and the rule."""


#: The role kind's field declaration beside this file (TOOL-dBoundRoles-2 S1), and the closed values of
#: each row's three graded keys.
ROLE_SCHEMA = "role-schema.toml"
SCHEMA_OWNERS = ("claude", "gov")
SCHEMA_SHAPES = ("slot", "text", "list", "class", "bool", "entries", "template")
SCHEMA_REQUIRED = ("every", "agent", "optional")
#: A row's key: a hyphenated word, letters and digits opening on a letter, single hyphens between them
#: (TOOL-dBoundRoles-1 S1), so `acts-as` loads and `-x`, `x-` and `x--y` do not.
SCHEMA_KEY_RE = r"[A-Za-z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)*"


def load_role_schema():
    """The `[[field]]` rows of `role-schema.toml` beside this file, in file order, each a dict holding
    `key`, `owner`, `shape`, `required` and `empty` (False unless the row says true). An absent file, one
    that is not TOML, a `[kind]` whose name is not `role`, or a row with a missing, repeated or
    out-of-set value raises RolesError naming the file, R2."""
    path = pathlib.Path(__file__).absolute().parent / ROLE_SCHEMA
    where = path.as_posix()
    try:
        with open(path, "rb") as fh:
            data = tomllib.load(fh)
    except OSError as e:
        raise RolesError("%s: R2 — the role schema cannot be read — %s" % (where, e.strerror))
    except tomllib.TOMLDecodeError as e:
        raise RolesError("%s: R2 — the role schema is not valid TOML — %s" % (where, e))
    if not isinstance(data.get("kind"), dict) or data["kind"].get("name") != "role":
        raise RolesError("%s: R2 — [kind] name is not \"role\"" % where)
    rows, seen = data.get("field"), set()
    if not isinstance(rows, list) or not rows or not all(isinstance(r, dict) for r in rows):
        raise RolesError("%s: R2 — 'field' is not a non-empty array of tables" % where)
    out = []
    for i, r in enumerate(rows, 1):
        for name, allowed in (("owner", SCHEMA_OWNERS), ("shape", SCHEMA_SHAPES), ("required", SCHEMA_REQUIRED)):
            if r.get(name) not in allowed:
                raise RolesError("%s: R2 — field %d's %s %r is not one of %s"
                                 % (where, i, name, r.get(name), " ".join(allowed)))
        key = r.get("key")
        if not isinstance(key, str) or not re.fullmatch(SCHEMA_KEY_RE, key):
            raise RolesError("%s: R2 — field %d's key %r is not one word" % (where, i, key))
        if key in seen:
            raise RolesError("%s: R2 — field key '%s' is repeated" % (where, key))
        if not isinstance(r.get("empty", False), bool):
            raise RolesError("%s: R2 — field '%s' empty is not true or false" % (where, key))
        seen.add(key)
        out.append({"key": key, "owner": r["owner"], "shape": r["shape"], "required": r["required"],
                    "empty": r.get("empty", False)})
    return out


#: Every front-matter key a role file may carry, in the schema's order: derived from it, never typed.
FRONT_MATTER_KEYS = tuple(r["key"] for r in load_role_schema())

#: THE OUTCOME TABLE (TOOL-dBoundRoles-26 S3, §4): each refusal arm's actor kind, a `build:<slug>` actor's kind
#: `build`, mapped to its route, whether the item goes back to the refused agent (`bounded` by `roles.retries`,
#: or `never`) and the rework draw TOOL-dDeclaredLoop-30 takes for it. Only `self` re-offers the item; every
#: other route is taken in the driver step that read the return. `load_refusal_arm` holds its keys to the
#: arm's actor kinds both ways, and `resolve_refusal_route` is its one reader.
REFUSAL_ROUTES = {"self": ("retry", "bounded", "re-dispatch"),
                  "producer": ("route-back", "never", "route-back"),
                  "driver": ("driver", "never", "re-dispatch"),
                  "owner": ("owner", "never", "none"),
                  "build": ("ask", "never", "none")}


def load_refusal_arm():
    """The `[return.refusal]` table of `role-schema.toml` beside this file (TOOL-dBoundRoles-26 S1), the arm
    every role's `return` carries, as `{"outcome", "fields", "actors"}`: `outcome` one closed-set value,
    `fields` its named fields, `actor` among them, and `actors` each actor form, a `<kind>:<slug>` form
    naming its slug by the placeholder `<slug>`. RolesError, R2, naming the file where the table is absent
    or breaks one of those shapes, or where the actor kinds are not `REFUSAL_ROUTES`' keys, both ways."""
    path = pathlib.Path(__file__).absolute().parent / ROLE_SCHEMA
    where = path.as_posix()
    try:
        with open(path, "rb") as fh:
            arm = (tomllib.load(fh).get("return") or {}).get("refusal")
    except (OSError, tomllib.TOMLDecodeError) as e:
        raise RolesError("%s: R2 — the role schema does not read — %s" % (where, getattr(e, "strerror", None) or e))
    if not isinstance(arm, dict):
        raise RolesError("%s: R2 — [return.refusal] is absent, so no role's return carries the refusal arm" % where)
    outcome, fields, actors = arm.get("outcome"), arm.get("fields"), arm.get("actors")
    if not isinstance(outcome, str) or not RETURN_VALUE_RE.match(outcome):
        raise RolesError("%s: R2 — [return.refusal] outcome %r is not %s" % (where, outcome, RETURN_VALUE_RE.pattern))
    if not isinstance(fields, list) or "actor" not in fields or not all(
            isinstance(f, str) and RETURN_NAME_RE.match(f) and f != "outcome" for f in fields):
        raise RolesError("%s: R2 — [return.refusal] fields %r is no list of field names holding actor" % (where, fields))
    if not isinstance(actors, list) or not actors or not all(
            isinstance(a, str) and re.fullmatch(r"[a-z]+(:<slug>)?", a) for a in actors):
        raise RolesError("%s: R2 — [return.refusal] actors %r is no list of <kind> or <kind>:<slug> forms"
                         % (where, actors))
    kinds = [a.split(":")[0] for a in actors]
    if sorted(kinds) != sorted(REFUSAL_ROUTES):
        raise RolesError("%s: R2 — [return.refusal] actors name the kinds %s, and REFUSAL_ROUTES routes %s"
                         % (where, ", ".join(kinds), ", ".join(REFUSAL_ROUTES)))
    return {"outcome": outcome, "fields": list(fields), "actors": list(actors)}
#: Where each writer class's output lives, spelled as `output` must carry it (R14) and as a rendered
#: role's ceiling names it. The product class has no single folder, so its spelling is the conf key
#: that declares its paths.
WRITE_FOLDERS = {"spec": "{{MEMORY_ROOT}}/builds/<slug>/spec/",
                 "review": "{{MEMORY_ROOT}}/builds/<slug>/reviews/",
                 "product": "ROUTED_PATHS", "records": "{{MEMORY_ROOT}}/"}
#: A `never` entry's limit and enforcer are split at the first of these (TOOL-dBoundRoles-2 S2).
NEVER_SEP = " — "
#: The stated absence of an enforcer, its reason non-empty: R13's `unenforced — <why>` spelling.
UNENFORCED_PREFIX = "unenforced — "
#: A gate-leg enforcer, the leg's manifest name after it.
LEG_PREFIX = "leg: "
#: A script enforcer's first word: a file name ending in one of these.
ENFORCER_SCRIPT_RE = re.compile(r"^[^\s/\\]+\.(?:js|py|sh)$")
#: The return template's grammar (TOOL-dBoundRoles-2 S4): a field name, a closed set's value, the named types.
RETURN_NAME_RE = re.compile(r"^[a-z][A-Za-z0-9-]*$")
RETURN_VALUE_RE = re.compile(r"^[a-z][a-z0-9-]*$")
RETURN_TYPES = ("text", "sha", "path", "list", "int")
#: How a rendered `## Return` names each named type.
RETURN_TYPE_WORDS = {"text": "text", "sha": "a sha", "path": "a path", "list": "a list", "int": "an integer"}
#: A direct return read against its template (TOOL-dBoundRoles-5 S1): a `sha` value's shape, the fenced
#: `json` block the return object is read from, the last one of the reply, and a `key: value` line naming
#: a field in the template's name grammar.
RETURN_SHA_RE = re.compile(r"^[0-9a-fA-F]{7,40}$")
RETURN_JSON_FENCE_RE = re.compile(r"^ {0,3}(`{3,})json[ \t]*\n(.*?)^ {0,3}\1[ \t]*$", re.M | re.S)
RETURN_LINE_RE = re.compile(r"^(%s):[ \t]*(.*?)[ \t]*$" % RETURN_NAME_RE.pattern[1:-1])
#: A body line carrying a limit, which belongs in `never` (R5's body arm).
PROHIBITION_RE = re.compile(r"(?i)\b(never|do not|don't|must not)\b")


def parse_never_entries(value):
    """`[(limit, enforcer)]` of a `never` value, in order: the `;`-separated entries, each split at its
    first ` — `, both halves stripped; an entry with no ` — ` has the enforcer ''."""
    out = []
    for entry in (value or "").split(";"):
        entry = entry.strip()
        if entry:
            limit, _sep, enforcer = entry.partition(NEVER_SEP)
            out.append((limit.strip(), enforcer.strip()))
    return out


def resolve_enforcer_path(tool_root, name):
    """The path of the script `name` in the tool root or one directory under it, the root first and then
    the directories in name order; None where neither holds it."""
    root = pathlib.Path(tool_root)
    if (root / name).is_file():
        return root / name
    try:
        dirs = sorted(d for d in root.iterdir() if d.is_dir())
    except OSError:
        return None
    return next((d / name for d in dirs if (d / name).is_file()), None)


def check_never_entries(value, tool_root, notes=None):
    """The defects of a `never` value against the install at `tool_root`, one string per entry that fails
    (TOOL-dBoundRoles-2 S2). Each entry's enforcer is, in this order: a script, its first word a `.js`,
    `.py` or `.sh` file `resolve_enforcer_path` finds; a gate leg, `leg: <name>`, a leg of the tool root's
    gate manifest, checked only when that manifest reads and a note appended to `notes` otherwise; or a
    stated absence, `unenforced — <why>`, its reason non-empty. An empty value, an entry with no ` — `, an
    enforcer of none of the three forms, a script no kit holds and a leg the manifest lacks each fail."""
    entries, defects, legs = parse_never_entries(value), [], False
    if not entries:
        return ["never names no limit; each entry is '<limit> — <enforcer>'"]
    for limit, enforcer in entries:
        shown = "'%s'" % (limit + (NEVER_SEP + enforcer if enforcer else ""))
        first = enforcer.split()[0] if enforcer.split() else ""
        if not limit or not enforcer:
            defects.append("never entry %s names no enforcer; write '<limit> — <enforcer>', the enforcer a "
                           "script, 'leg: <name>' or 'unenforced — <why>'" % shown)
        elif ENFORCER_SCRIPT_RE.match(first):
            if resolve_enforcer_path(tool_root, first) is None:
                defects.append("never entry %s names %s, which no kit holds: no file of that name sits in the "
                               "tool root or one directory under it" % (shown, first))
        elif enforcer.startswith(LEG_PREFIX):
            leg = enforcer[len(LEG_PREFIX):].strip()
            if legs is False:
                legs = load_gate_leg_names(tool_root)
            if not leg:
                defects.append("never entry %s names no leg after 'leg: '" % shown)
            elif legs is None:
                if notes is not None:
                    notes.append("%s cannot be read, so the never entry %s's leg is not checked"
                                 % ((pathlib.Path(tool_root) / GATE_MANIFEST).as_posix(), shown))
            elif leg not in legs:
                defects.append("never entry %s names the leg '%s', which %s does not hold"
                               % (shown, leg, (pathlib.Path(tool_root) / GATE_MANIFEST).as_posix()))
        elif enforcer.startswith(UNENFORCED_PREFIX.rstrip()) and first == "unenforced":
            if not enforcer.startswith(UNENFORCED_PREFIX) or not enforcer[len(UNENFORCED_PREFIX):].strip():
                defects.append("never entry %s states no enforcer without a reason; write 'unenforced — <why>'"
                               % shown)
        else:
            defects.append("never entry %s names an enforcer of no known form; write a script, "
                           "'leg: <name>' or 'unenforced — <why>'" % shown)
    return defects


def parse_return_template(value):
    """`[(name, type, optional)]` of a `return` template, in order (TOOL-dBoundRoles-2 S4): `type` one of
    RETURN_TYPES, or a closed set as a tuple of values, a bare word none of the named types being a set
    of one. RolesError, R2, on an empty template or entry, an entry that is not `<name>:<type>[?]`, a
    repeated name, an empty set, a value named twice in one set, or no required `outcome` whose type is
    a closed set."""
    out, names = [], set()
    entries = [e.strip() for e in (value or "").split(",")]
    if not (value or "").strip():
        raise RolesError("R2 — the return template is empty; it holds an 'outcome:<value>|<value>' entry")
    for entry in entries:
        name, sep, kind = entry.partition(":")
        name, kind = name.strip(), kind.strip()
        optional = kind.endswith("?")
        kind = kind[:-1].strip() if optional else kind
        if not sep or not RETURN_NAME_RE.match(name):
            raise RolesError("R2 — return entry %r is not '<name>:<type>[?]', the name %s"
                             % (entry, RETURN_NAME_RE.pattern))
        if name in names:
            raise RolesError("R2 — return field '%s' is named twice" % name)
        names.add(name)
        if kind in RETURN_TYPES:
            out.append((name, kind, optional))
            continue
        values = [v.strip() for v in kind.split("|")]
        if not kind or not all(values):
            raise RolesError("R2 — return field '%s' has an empty type or an empty value in its set" % name)
        for v in values:
            if not RETURN_VALUE_RE.match(v):
                raise RolesError("R2 — return field '%s' value %r is not %s" % (name, v, RETURN_VALUE_RE.pattern))
        if len(set(values)) != len(values):
            raise RolesError("R2 — return field '%s' names a value twice in its set" % name)
        out.append((name, tuple(values), optional))
    if not any(n == "outcome" and isinstance(t, tuple) and not o for n, t, o in out):
        raise RolesError("R2 — the return template holds no required 'outcome' field whose type is a closed "
                         "set of values")
    return out


def render_refusal_arm(arm):
    """The one line naming the refusal arm `arm`, `load_refusal_arm`'s, that `## Return` closes with
    (TOOL-dBoundRoles-26 S1): its `outcome: <value>`, then each field, `actor` as one of its forms."""
    fields = ["%s (%s)" % (f, "one of " + ", ".join(arm["actors"]) if f == "actor" else "text") for f in arm["fields"]]
    return "Or refuse, returning outcome: %s; %s." % (arm["outcome"], "; ".join(fields))


def check_refusal_arm(obj, arm=None):
    """The defect lines of a refused return object `obj` read against the refusal arm (TOOL-dBoundRoles-26 S2),
    `arm` `load_refusal_arm`'s when None; `[]` for a valid refusal. Each arm field absent or not a non-empty
    string, a `remedy` spelling the record's separator ` · ` or a line break, and an `actor` none of the arm's
    forms, a `<kind>:<slug>` form's slug off `SLUG_RE` included, is one line naming the field."""
    arm = arm or load_refusal_arm()
    defects = []
    for name in arm["fields"]:
        value = obj.get(name)
        if not isinstance(value, str) or not value.strip():
            defects.append("%s — the refusal arm's %s is absent or empty" % (name, name))
        elif name != "actor" and (" · " in value or "\n" in value or "\r" in value):
            defects.append("%s — %s spells the record's separator ' · ' or a line break; it is one line"
                           % (name, json.dumps(value, ensure_ascii=False)[:80]))
    actor = obj.get("actor")
    if isinstance(actor, str) and actor.strip() and derive_refusal_kind(actor, arm) is None:
        defects.append("actor — %s is none of %s" % (json.dumps(actor, ensure_ascii=False)[:80], ", ".join(arm["actors"])))
    return defects


def derive_refusal_kind(actor, arm):
    """The kind of the refusal actor `actor` under `arm`'s forms: the form itself for a bare one, `<kind>` for
    `<kind>:<slug>` whose slug matches `SLUG_RE`; None for any other value."""
    for form in arm["actors"]:
        kind, sep, _slug = form.partition(":")
        if (not sep and actor == form) or (sep and actor.startswith(kind + ":")
                                           and SLUG_RE.match(actor[len(kind) + 1:])):
            return kind
    return None


def render_role_fields(keys, gates=()):
    """The `## Never`, `## Ceiling` and `## Return` sections of a role's front matter `keys`
    (TOOL-dBoundRoles-2 S6), the gate legs `gates` granted it. `## Never` and `## Return` render only
    where their key is non-empty; the ceiling always renders, an absent value as `none`. `## Return` closes
    with `render_refusal_arm`'s line, the refusal arm every role carries (TOOL-dBoundRoles-26 S1)."""
    out = []
    entries = parse_never_entries(keys.get("never", ""))
    if entries:
        lines = []
        for limit, enforcer in entries:
            if enforcer.startswith(UNENFORCED_PREFIX):
                lines.append("- %s — unenforced: %s" % (limit, enforcer[len(UNENFORCED_PREFIX):].strip()))
            else:
                lines.append("- %s — enforced by %s" % (limit, enforcer) if enforcer else "- %s" % limit)
        out.append("## Never\n\n" + "\n".join(lines))
    writes = keys.get("writes") or "none"
    folder = WRITE_FOLDERS.get(writes)
    out.append("## Ceiling\n\n- tools: %s\n- writes: %s\n- gate legs: %s" % (
        keys.get("tools") or "none", writes + (", in " + folder if folder else ""),
        ", ".join(gates) if gates else "none"))
    if keys.get("return"):
        fields = []
        for name, kind, optional in parse_return_template(keys["return"]):
            what = "one of " + ", ".join(kind) if isinstance(kind, tuple) else RETURN_TYPE_WORDS[kind]
            fields.append("%s (%s%s)" % (name, what, ", optional" if optional else ""))
        out.append("## Return\n\nReturn one object holding these fields, in this order: %s.\n\n%s"
                   % ("; ".join(fields), render_refusal_arm(load_refusal_arm())))
    return "\n\n".join(out)


def derive_allowance(declaration, slug, granted, memory_root, routed):
    """The allowance of an item's work order as repo-relative path prefixes, in order (TOOL-dBoundRoles-3 S3, §4
    "The allowance"), from `declaration`, the loop kit's `declaration` verb's answer: `[]` for `none`; for `spec`,
    `review` and `records` the class's `WRITE_FOLDERS` folder, its `{{MEMORY_ROOT}}` the conf's `memory_root` and
    `<slug>` the render's build; for `product` each path of `granted`, the caller's `--allowance` values, once,
    each under an entry of `routed`, the conf's `ROUTED_PATHS` value, by that key's grammar: an entry ending `/`
    covers itself and every path under it, any other entry names one file. RolesError naming the item and the
    class or the path for an allowance outside `WRITE_FOLDERS` and `none`, a `product` item granted no path, a
    path granted to any other class, and a granted path that is empty, absolute, climbs through `..` or sits
    under no entry."""
    tag, allowance, granted = declaration.get("tag"), declaration.get("allowance"), list(granted or ())
    if allowance != "none" and allowance not in WRITE_FOLDERS:
        raise RolesError("the item %s declares the allowance %r, which is none of none, %s"
                         % (tag, allowance, ", ".join(WRITE_FOLDERS)))
    if allowance != "product":
        if granted:
            raise RolesError("--allowance %s: the item %s's allowance is the %s class, which takes no granted "
                             "path; only a product item does" % (granted[0], tag, allowance))
        return [] if allowance == "none" else [
            WRITE_FOLDERS[allowance].replace(MEMORY_ROOT_TOKEN, memory_root).replace("<slug>", slug)]
    if not granted:
        raise RolesError("the item %s's allowance is the product class, which takes only the paths the dispatch "
                         "grants: pass --allowance <path> once per path of the unit's --dispatch --writes set" % tag)
    entries = [e[2:] if e.startswith("./") else e for e in (routed or "").split()]
    out = []
    for path in granted:
        p = path.replace("\\", "/")
        p = p[2:] if p.startswith("./") else p
        if not p or p.startswith(("/", "~")) or re.match(r"^[A-Za-z]:", p) or ".." in p.split("/"):
            raise RolesError("--allowance %s is not a repo-relative path inside the repository" % path)
        if not any(p == e or (e.endswith("/") and (p == e.rstrip("/") or p.startswith(e))) for e in entries):
            raise RolesError("--allowance %s sits under no ROUTED_PATHS entry (%s): an allowance reaches no path "
                             "outside the routed paths" % (path, " ".join(entries) or "none declared"))
        if p not in out:
            out.append(p)
    return out


# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — a `.governance/install.json` row whose `path` exists inside this tree and whose
       `source` ends in <home>/<anchor>, or a `rendered` row whose `source`, its template, sits
       directly under <home>/ and whose `path` names a file <anchor>. The only record of a RENAMED
       kit dir: no probe finds a memory-recall kit an adopter homed at `scripts/recall/`.
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
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
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


# >>> render_envelope — canonical copy: envelope.py in the gov lib dir (byte-identical; gated)
def render_envelope(doc, level, direction, body):
    """`body` between the opener and the closer naming `doc`; an empty body renders the two lines alone."""
    if body and not body.endswith("\n"):
        body += "\n"
    return "[%s · Level %d · %s]\n%s[/%s]\n" % (doc, level, direction, body, doc)


def read_envelopes(text):
    """Each whole line of `text` that is an envelope line, in order: `(line number, "open", doc, level,
    direction)` for an opener and `(line number, "close", doc, None, None)` for a closer."""
    import re
    opener = re.compile(r"^\[([^\[\]/][^\[\]]*?) · Level (\d+) · ([^\]]*)\]$")
    closer = re.compile(r"^\[/([^\[\]]+)\]$")
    found = []
    for n, line in enumerate(text.replace("\r\n", "\n").split("\n"), 1):
        m = opener.match(line)
        if m:
            found.append((n, "open", m.group(1), int(m.group(2)), m.group(3)))
            continue
        m = closer.match(line)
        if m:
            found.append((n, "close", m.group(1), None, None))
    return found
# <<< render_envelope


def read_cap_answer(request, root, kit_dir):
    """`(value, mode, rule)` the policy kit answers for ONE census cap (TOOL-dGroundRules-9), `request`
    in its CLI grammar, `<cap>[=default:<n>]`, read in the repository at `root`. The kit is found by
    `resolve_kit_dir` from `kit_dir`, and its `budgets.resolve_caps` answers: a value is the policy
    file's where it sets one, else what was handed in, None for a family. No kit, or any refusal of
    the reader, answers the handed-in value under `refuse`, as before that unit, the rule saying why.
    The roles kit's reach into the policy kit's caps, which `check_roles` and `handoff` share; a policy
    key is read through `read_policy_setting` instead."""
    import sys
    cap, _eq, how = request.partition("=")
    held = int(how.split(":", 1)[1]) if how.startswith("default:") else None
    try:
        kit = str(resolve_kit_dir("policy", "budgets.py", kit_dir))
        if kit not in sys.path:
            sys.path.insert(0, kit)
        import budgets  # the policy kit's caps module, found above
        try:
            a = budgets.resolve_caps([request], str(root))[cap]
            return a.value, a.mode, a.rule
        except budgets.policy.Refusal as exc:
            why = "the policy reader refused: %s" % exc
    except (LookupError, ImportError) as exc:
        why = "no policy kit answered: %s" % exc
    return held, "refuse", "%s; a breach refuses as before" % why


#: The policy kit's refusal of a key whose catalogue row carries a derived default, its `DERIVED_WHY`
#: (the policy kit's `policy.py#DERIVED_WHY`) spelled again, since a kit imports no sibling kit, under the
#: name the playbook kit spells it: a key refused with it is unset (TOOL-dBoundRoles-21 §8 F8).
POLICY_DERIVED_LINE = "a derived default no reader computes yet"
#: Each `(key, root)` read this process, mapped to `(value, source)`, `(None, None)` for an unset key, so
#: a key is read once per process and root (TOOL-dBoundRoles-21 §8 F7); under None, the one note printed
#: when no policy kit answers.
_POLICY_ANSWERS = {}


def read_policy_setting(key, root, with_default=False):
    """The value of the policy key `key` in the repository at `root`, or None where it is unset
    (TOOL-dBoundRoles-21 S1). It runs `<policy kit>/policy.py get <key> --json` in `root`, the kit found
    through `resolve_kit_dir` from this file's own directory, since a kit imports no sibling kit, so `get`
    reads the landed revision. A `source` of `file` or `last-valid` answers the `value`; `default`
    answers None, or the value under `with_default`. A refusal whose stderr carries POLICY_DERIVED_LINE
    is an unset key, None in both forms; any other refusal raises RolesError naming the key and the
    reader's line. No policy kit answers None for every key and prints one note on stderr. Each key is
    read once per process and root, its answer kept in `_POLICY_ANSWERS`.

    WHAT THIS DOES NOT CHECK: that POLICY_DERIVED_LINE still equals the policy kit's `DERIVED_WHY`, a
    reword there turning every unset key into a refusal; nor which row a derived refusal names."""
    import os
    import subprocess
    import sys
    at = (key, pathlib.Path(root).absolute().as_posix())
    if at not in _POLICY_ANSWERS:
        try:
            kit = resolve_kit_dir("policy", "policy.py", pathlib.Path(__file__).absolute().parent)
        except LookupError as exc:
            if None not in _POLICY_ANSWERS:
                _POLICY_ANSWERS[None] = str(exc)
                print("roles: note — no policy kit answers, so every roles.effort and roles.model key "
                      "reads unset: %s" % exc, file=sys.stderr)
            return None
        env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
        try:
            p = subprocess.run([sys.executable, str(kit / "policy.py"), "get", key, "--json"], cwd=str(root),
                               capture_output=True, text=True, encoding="utf-8", errors="replace",
                               stdin=subprocess.DEVNULL, env=env)
        except OSError as exc:
            raise RolesError("%s — the policy reader did not run: %s" % (key, exc))
        err = [ln for ln in (p.stderr or "").splitlines() if ln.strip()]
        if p.returncode == 0:
            try:
                hit = json.loads(p.stdout)
                _POLICY_ANSWERS[at] = (hit["value"], hit["source"])
            except (ValueError, KeyError, TypeError):
                raise RolesError("%s — the policy reader printed no value and source: %r" % (key, p.stdout))
        elif any(POLICY_DERIVED_LINE in ln for ln in err):
            _POLICY_ANSWERS[at] = (None, None)
        else:
            raise RolesError("%s — the policy reader refused: %s"
                             % (key, err[-1] if err else "policy.py get exited %d" % p.returncode))
    value, source = _POLICY_ANSWERS[at]
    if value is None or not (with_default or source in ("file", "last-valid")):
        return None
    return value


#: TOOL-dBoundRoles-11 S5: the question kinds the owner-question reader answers, and the answer words.
OWNER_QUESTION_KEY = "run.on-owner-question"
OWNER_QUESTION_KINDS = ("fork", "owner-gate", "ratification", "owner-write", "refusal")
OWNER_QUESTION_ANSWERS = ("resolve", "park-item", "park-build", "stop-run", "owner", "choose-ending")
#: The endings best effort chooses among once the build's rework budget is spent (TOOL-dBoundRoles-26 S5, §8 F3),
#: ranked most work kept first: the key's three ending values, in this order.
OWNER_ENDINGS = OWNER_QUESTION_ANSWERS[1:4]


def resolve_owner_question(kind, attended, repo, budget_spent=False):
    """'resolve' | 'park-item' | 'park-build' | 'stop-run' | 'owner' | 'choose-ending', the key read once by
    `read_policy_setting` (TOOL-dBoundRoles-11 S5). A question of kind `fork`, `owner-gate` or `refusal`, an
    `owner` refusal's (TOOL-dBoundRoles-26 S5), raised while the owner is away answers
    `run.on-owner-question`'s value at the landed revision of `repo`, its catalogue default
    `best-effort-recorded` read as `resolve`: the role that meets the fork resolves it by `principle.p18` and
    records it. With `budget_spent`, the build's rework budget spent as `budget.py`'s `ending` line states,
    `best-effort-recorded` answers `choose-ending` instead, its options `OWNER_ENDINGS` alone and never
    `resolve`, so best effort takes no further lap. A question raised while the owner attends, a
    `ratification` and an `owner-write` each answer `owner`, the cases the key leaves to the owner and
    `run.on-owner-silence`. An unknown kind raises RolesError naming it; a refused read raises the reader's
    RolesError, naming the key and the reader's line; no policy kit, the reader's None, raises RolesError
    naming the key and the absent kit. A value outside the catalogue's four raises RolesError naming it.

    WHAT THIS DOES NOT CHECK: which build or item asked, or that `budget_spent` is true of the build, which
    the caller reads."""
    if kind not in OWNER_QUESTION_KINDS:
        raise RolesError("%s — the question kind '%s' is none of %s" % (OWNER_QUESTION_KEY, kind,
                                                                        ", ".join(OWNER_QUESTION_KINDS)))
    if attended or kind in ("ratification", "owner-write"):
        return "owner"
    value = read_policy_setting(OWNER_QUESTION_KEY, repo, with_default=True)
    if value is None:
        raise RolesError("%s — no policy kit answers it beside the roles kit, so no owner-question can be "
                         "answered for the owner: install the policy kit, or the owner answers" % OWNER_QUESTION_KEY)
    answer = "resolve" if value == "best-effort-recorded" else value
    if answer not in OWNER_QUESTION_ANSWERS[:4]:   # the four the key's values answer; `owner` is never one
        raise RolesError("%s — reads %r, none of best-effort-recorded, park-item, park-build and stop-run"
                         % (OWNER_QUESTION_KEY, value))
    return "choose-ending" if answer == "resolve" and budget_spent else answer


def check_effort_floor(level, source, root=None):
    """Refuse a level below `EFFORT_FLOOR` by its source (TOOL-dBoundRoles-23 S5, S6, §4 "The floor"). `source`
    names where the level was read: a `roles.effort.*` key, which `read_policy_setting` reads from the policy
    file, or any other source, the house file, a role's declaration or a stage row. A level at the floor or
    above, or one outside `EFFORT_LEVELS` (the level checks name that), passes. Below it, a policy-file key
    passes only while `policy-file.guard`, read through `read_policy_setting` in the repository at `root` (the
    working directory when None), is `owner-only` or unread, the owner's terminal commit being what writes
    the file there; under any other value RolesError names the guard and its value. Every other source is a
    RolesError naming the level, its source, the floor and the owner as the remedy's actor.

    WHAT THIS DOES NOT CHECK: whose commit wrote a policy-file level. The guard's run admission lands a live
    run's change under every `policy-file.guard` value, and a floor reading provenance from the file alone
    cannot tell it from the owner's; that path is the guard's to close (§8 F6)."""
    if level not in EFFORT_LEVELS or EFFORT_LEVELS.index(level) >= EFFORT_LEVELS.index(EFFORT_FLOOR):
        return
    remedy = ("only the owner sets a lower level, as a %s* key in the guarded policy file %s"
              % (EFFORT_POLICY_PREFIX, EFFORT_POLICY_FILE))
    if str(source).startswith(EFFORT_POLICY_PREFIX):
        guard = read_policy_setting(EFFORT_GUARD_KEY, root if root is not None else ".", with_default=True)
        if guard is None or guard == EFFORT_GUARD_OWNER:
            return
        raise RolesError("%s from %s in %s is below the floor %s, and %s is %s, under which an agent's change "
                         "may write that file; %s, while %s is %s"
                         % (level, source, EFFORT_POLICY_FILE, EFFORT_FLOOR, EFFORT_GUARD_KEY, guard, remedy,
                            EFFORT_GUARD_KEY, EFFORT_GUARD_OWNER))
    raise RolesError("%s from %s is below the floor %s; %s" % (level, source, EFFORT_FLOOR, remedy))


def check_load_set(root, kit_dir, blocks, points=(), reach=False):
    """`(refused, lines)` of the playbook kit's load-set check for `blocks`, `[(slot, role block bytes)]`
    (PLAY-dOrderedCharter-11 S4): ONE run of its `check` verb, each slot's reader set checked for a missing
    required unit and its block measured against its body ceiling, and each of `points`, `[(load point,
    bytes)]`, measured against its own cap: the `code` slot's block (PLAY-dOrderedCharter-27). With `reach`
    the same run also prints each reader's reach units, one `load-set — reach ·` line each, for the caller
    to take out of the notes (PLAY-dOrderedCharter-21). The kit
    is found by `resolve_kit_dir` and run as a subprocess, since a kit imports no sibling kit; with none
    found the check is one `unarmed` line and the render proceeds. The caller places each line: a `Missing required unit:` line
    in the reader's text, a `**Load gaps:**` line in the prompt record, any other as a note."""
    import os
    import subprocess
    import sys
    try:
        kit = resolve_kit_dir("playbook", "load_sets.py", kit_dir)
    except LookupError as exc:
        return False, ["load-set — unarmed · no playbook kit: %s" % exc]
    argv = [sys.executable, str(kit / "load_sets.py"), "check", "--root", str(root)]
    for slot, size in blocks:
        argv += ["--reader", "role." + slot, "--load-point", "role.%s=%d" % (slot, size)]
    for name, size in points:
        argv += ["--load-point", "%s=%d" % (name, size)]
    if reach:
        argv.append("--reach")
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    try:
        r = subprocess.run(argv, cwd=str(root), env=env, capture_output=True, encoding="utf-8",
                           errors="replace", stdin=subprocess.DEVNULL, timeout=120)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return True, ["load-set — refused · the load-set check did not run: %s" % exc]
    lines = [ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()]
    if r.returncode not in (0, 1):
        return True, lines or ["load-set — refused · the load-set check exited %d" % r.returncode]
    return r.returncode == 1, lines


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


def load_document_registry(kit_dir):
    """The rows of the playbook kit's document registry, `documents.toml`, found from `kit_dir` by
    `resolve_kit_dir`. No playbook kit raises its LookupError, which the caller prints as one
    `UNRANKED_NOTE` and renders unranked; a registry that is there and does not read raises RolesError
    naming it (PLAY-dOrderedCharter-5 F4)."""
    reg = resolve_kit_dir("playbook", "documents.toml", kit_dir) / "documents.toml"
    try:
        rows = tomllib.loads(reg.read_text(encoding="utf-8")).get("document") or []
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as exc:
        raise RolesError("%s: the document registry does not read, so no envelope can rank a block — %s"
                         % (reg.as_posix(), exc))
    return [r for r in rows if isinstance(r, dict)] if isinstance(rows, list) else []


def read_envelope_row(rows, rel, memory_root):
    """`(level, direction)` of the registry row among `rows` whose path matches the document `rel`, else
    None (PLAY-dOrderedCharter-3 S4); `rows` None, no registry, reads as None too, so a tree without one
    renders no envelope. A row's `*` holds within one segment, and a held row envelopes nothing."""
    import fnmatch
    want = rel.split("/")
    for row in rows or []:
        path = str(row.get("path", "")).replace("{memory_root}", memory_root).split("/")
        if "hold" not in row and len(path) == len(want) and all(
                fnmatch.fnmatchcase(w, p) for w, p in zip(want, path)):
            level, direction = row.get("level"), row.get("direction")
            ok = isinstance(level, int) and not isinstance(level, bool) and isinstance(direction, str)
            return (level, direction) if ok else None
    return None


def parse_charter(text, where):
    """The governing doc as `{"shape", "rules", "carried"}`; RolesError (R0) on a doc this kit cannot read.

    Only the playbook region is read when the text holds its two markers once each, in order. A
    section is a `## ` line and the lines up to the next one. The `- [<tag>] ` lines between the
    practices markers, each a whole line with the opener first, are the rules, kept whole in charter
    order; a charter carrying no such pair, one seeded before them, has its rules read from the
    section `SECTION_ONE_RE` heads. Each CARRIED_SECTIONS name is the first section headed by it, as
    `(heading, body)` with the body's blank edges trimmed. With a rule the shape is `tagged` and every
    carried section is required; with none and a `## §<n> — ` heading it is `legacy`, carrying nothing;
    otherwise the doc is refused. `where` is the path every message names.
    """
    text = text.replace("\r\n", "\n")
    i = text.find(PLAYBOOK_OPEN)
    j = text.find(PLAYBOOK_CLOSE, i + len(PLAYBOOK_OPEN)) if i >= 0 else -1
    if j >= 0 and text.count(PLAYBOOK_OPEN) == 1 and text.count(PLAYBOOK_CLOSE) == 1:
        text = text[i + len(PLAYBOOK_OPEN):j]
    # PLAY-dOrderedCharter-3 S4: an envelope's opener or closer is no section's line, so none rides into a
    # Charter block, where the closer would read as another document's
    enveloped = {n for n, *_ in read_envelopes(text)}
    kept = [ln for n, ln in enumerate(text.split("\n"), 1) if n not in enveloped]
    sections = []
    for line in kept:
        if line.startswith("## "):
            sections.append((line, []))
        elif sections:
            sections[-1][1].append(line)
    a = kept.index(PRACTICES_OPEN) if PRACTICES_OPEN in kept else -1
    b = kept.index(PRACTICES_CLOSE) if PRACTICES_CLOSE in kept else -1
    if 0 <= a < b:
        held = kept[a + 1:b]
    else:   # a charter seeded before the markers
        held = next((body for head, body in sections if SECTION_ONE_RE.match(head)), [])
    rules = {}
    for line in held:
        m = RULE_LINE_RE.match(line)
        if m and m.group(1) in rules:
            raise RolesError("%s: R0 — the governing doc repeats the practice rule tag [%s]"
                             % (where, m.group(1)))
        if m:
            rules[m.group(1)] = line
    if not rules:
        if any(SECTION_RE.match(ln) for ln in text.split("\n")):
            return {"shape": "legacy", "rules": {}, "carried": []}
        raise RolesError("%s: R0 — the governing doc carries no practice rule tag, between the practices "
                         "markers or under a numbered first heading, and no '## §<n> — ' heading, so it is "
                         "no charter this kit reads" % where)
    carried = []
    for name in CARRIED_SECTIONS:
        hit = next(((head, body) for head, body in sections
                    if head == "## " + name or head.startswith("## %s " % name)), None)
        if hit is None:
            raise RolesError("%s: R0 — the governing doc carries practice rule tags and no '## %s' "
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


def read_unfenced_lines(text):
    """`(line number, line)` for every line of `text` outside a fence, then `(opened at, None)` when the
    text ends inside one (TOOL-dBoundRoles-38 S3). A fence opens on a line of at most three spaces of
    indent and then three or more backticks or three or more tildes, and closes only on a line of the
    same character whose run is at least as long, with nothing after it but whitespace; a fence line is
    yielded by neither end. The hooks kit's `readUnfencedLines` is the same walker. `tree_lib.unfenced_lines`'
    shape, copied with the length rule: a shorter run inside a longer fence is content."""
    fence, opened_at = "", 0
    for n, line in enumerate(str(text).split("\n"), 1):
        m = re.match(r" {0,3}(`{3,}|~{3,})(.*)", line, re.S)
        if not fence:
            if m:
                fence, opened_at = m.group(1), n
                continue
            yield n, line
        elif m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence) \
                and re.fullmatch(r"[ \t\r]*", m.group(2)):
            fence = ""
    if fence:
        yield opened_at, None


def render_handed_fence(content):
    """`content` between an opening and a closing line of backticks and nothing else, the run one more
    than the longest run of backticks anywhere in `content` and at least three, so no line of it can
    close the fence (TOOL-dBoundRoles-38 S1). The content's bytes sit unchanged between the opening
    line's newline and the closing line; an empty value is an empty fence."""
    content = str(content)
    bar = "`" * max([3] + [len(run) + 1 for run in re.findall(r"`+", content)])
    return "%s\n%s%s%s" % (bar, content, "" if not content or content.endswith("\n") else "\n", bar)


def check_block_fences(section, extents):
    """One refusal line per fence defect of `section`, walked by `read_unfenced_lines`, at each block's extents
    (TOOL-dBoundRoles-48 S1); `[]` when every block holds. `extents` lists `(key, first, last, fence)` per
    block, its first and last line in `section`, and `fence` the `(opening, closing)` lines of a handed block's
    fence or None for an authored one. A line names the key and the line for each block whose first line the
    walk reads inside a fence, each handed block whose heading or fact line it reads inside one, each handed
    content line it reads outside its fence, and a walk that ends inside one, named by the block holding the
    line the fence opened at. So a walk that ends balanced after an authored block flipped the fence state
    across a handed one still refuses."""
    read, opened = set(), None
    for n, line in read_unfenced_lines(section):
        if line is None:
            opened = n
        else:
            read.add(n)
    lines, out = str(section).split("\n"), []
    for key, first, _last, fence in extents:
        if first not in read:
            out.append("%s — its first line, line %d of the ## Task section, is read inside a fence a block before "
                       "it left open, so the block would stand as content; close that fence in the value that "
                       "opened it and render again" % (key, first))
        if fence is None:
            continue
        hidden = next((n for n in range(first, fence[0]) if lines[n - 1].strip() and n not in read), None)
        if hidden is not None:
            out.append("%s — line %d of the ## Task section, its heading or fact line, is read inside a fence, so "
                       "the handed block would not stand as one; close the fence a block before it opened and "
                       "render again" % (key, hidden))
        out += ["%s — line %d of the ## Task section, inside the handed fence of lines %d-%d, is read outside "
                "a fence, so the handed content would stand as executor lines; close the fence a block before "
                "it opened and render again" % (key, n, fence[0], fence[1])
                for n in range(fence[0] + 1, fence[1]) if n in read]
    if opened is not None:
        holder = [key for key, first, last, _f in extents if first <= opened <= last]
        out.append("%s — a fence opened at line %d of the ## Task section is never closed, so every fact line "
                   "after it would be read as content; close it in the value that opened it and render again"
                   % (holder[-1] if holder else "the ## Task section", opened))
    return out


#: The line shapes a typed input may not carry (TOOL-dBoundRoles-45 S2), each one a handoff's reader acts on:
#: a heading of level one to three, a fact line, a `gov:handoff` marker line and a framing line.
AUTHORED_LINE_SHAPES = (("a heading", re.compile(r"#{1,3} ")), ("a fact line", FACT_RE),
                        ("a gov:handoff marker line", MARKER_RE), ("a Framed by: line", re.compile(r"Framed by:")))


def check_authored_lines(value, field):
    """One refusal line per line of `value` that matches a shape of `AUTHORED_LINE_SHAPES`, naming `field` and
    the line's number, then one more where `read_unfenced_lines(value)` ends on its open-fence yield, naming
    the line the fence opened at; `[]` for a value that would stand as text alone. A typed input is written
    unfenced, so a line of one of those shapes would stand as an executor line; a fence the value opens and
    closes is legal (TOOL-dBoundRoles-45 S2)."""
    text, out = str(value), []
    for n, line in enumerate(text.split("\n"), 1):
        what = next((what for what, shape in AUTHORED_LINE_SHAPES if shape.match(line)), None)
        if what:
            out.append("%s — line %d reads as %s, which a typed input may not carry: it is written unfenced, so "
                       "the line would stand as one; hand quoted text as a file through --input spec=<path>"
                       % (field, n, what))
    out +=["%s — a fence opened at line %d of the value is never closed, so every line after it would be read "
            "as content; close it in the value and render again" % (field, n)
            for n, line in read_unfenced_lines(text) if line is None]
    return out


def extract_prompt_marker(prompt):
    """The `MARKER_RE` match of the marker line an `Agent` prompt opens with, read as the hooks
    kit's spawn guard reads it (its rule 6): exactly one line outside every fence, carriage returns
    removed, is a whole marker line, and it is the prompt's first line once CRLF is folded, the two ends
    trimmed and that line's trailing whitespace dropped. None otherwise (TOOL-aOrientedCast-25); a marker
    line inside a fence is handed content and is not counted (TOOL-dBoundRoles-38 S4)."""
    text = str(prompt)
    marks = [ln for ln in (raw.replace("\r", "") for _n, raw in read_unfenced_lines(text) if raw is not None)
             if MARKER_RE.fullmatch(ln)]
    first = text.replace("\r\n", "\n").strip().split("\n")[0].rstrip()
    return MARKER_RE.fullmatch(first) if len(marks) == 1 and first == marks[0] else None


def check_rule_tags(charter, value):
    """`(defects, notes)` for one role's raw `rules` value against `parse_charter`'s structure.

    An entry that is not a lowercase tag (optionally ending in `?`) or repeats a tag is a defect on
    either shape. On a tagged charter a bare tag its practices lack is a defect and an optional one a
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
            defects.append("rules tag '%s' names no practice of the governing doc" % tag)
        else:
            notes.append("rules tag '%s' names no practice of the governing doc, so this role "
                         "carries no such rule here" % e)
    return defects, notes


def render_charter_blocks(charter, where, value, notes=None):
    """The charter text a role agent carries: `### Charter rules` holding the practice lines the
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


def derive_field_tag(key):
    """A native read key's tag: `task:title` is `field.task.title`."""
    return "field." + key.replace(":", ".", 1)


def parse_read_key(entry):
    """`(native key, optional)` of one `reads` entry in either spelling: one trailing `?` is the
    optional flag, `field.<family>.<name>` folds to `<family>:<name>`, and any other entry is returned
    unchanged, so a key outside the vocabulary stays outside it (TOOL-dBoundRoles-14 S4)."""
    entry = entry.strip()
    optional = entry.endswith("?")
    key = entry[:-1] if optional else entry
    parts = key.split(".")
    if len(parts) == 3 and parts[0] == "field" and all(parts):
        key = "%s:%s" % (parts[1], parts[2])
    return key, optional


def derive_stage_field_tag(key):
    """A harness stage key's tag: each capital lower-cased with a hyphen before it, `specWriter` to
    `field.stage.spec-writer`. R9's STAGE_KEY_RE admits no digit and no hyphen, so the fold is
    injective (TOOL-dBoundRoles-14 §8 F2)."""
    return "field.stage." + re.sub(r"[A-Z]", lambda m: "-" + m.group(0).lower(), key)


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


def load_workflow_table(kit_dir):
    """`workflows.toml` beside the kit, parsed: the one read `load_workflows` and `load_workflow_kinds`
    take. An unreadable file, or one that is not TOML, raises RolesError naming it, R6."""
    path = pathlib.Path(kit_dir) / "workflows.toml"
    try:
        with open(path, "rb") as fh:
            return tomllib.load(fh)
    except OSError as e:
        raise RolesError("%s: R6 — cannot be read — %s" % (path.as_posix(), e.strerror))
    except tomllib.TOMLDecodeError as e:
        raise RolesError("%s: R6 — not valid TOML — %s" % (path.as_posix(), e))


def load_workflows(kit_dir):
    """`workflows.toml`'s `[[workflow]]` entries, as a list in file order, each entry's `stages` its
    `[[workflow.stages]]` rows as a list of row dicts in file order (TOOL-dBoundRoles-22 S2). The rows
    are not validated here: R9 grades them, and `derive_stage_rows` is the one read of them."""
    entries = load_workflow_table(kit_dir).get("workflow", [])
    if not isinstance(entries, list) or not all(isinstance(e, dict) for e in entries):
        raise RolesError("%s: R6 — 'workflow' is not an array of tables"
                         % (pathlib.Path(kit_dir) / "workflows.toml").as_posix())
    return entries


#: The five workflow kinds (TOOL-dBoundRoles-16 S1), each named by one `[[kind]]` row of `workflows.toml`
#: holding its defaults. The set is closed here because `twin` and `experiment` carry fields of their own,
#: `of` and the `[workflow.experiment]` table, which R9 grades by the kind's name.
WORKFLOW_KINDS = ("single", "per-unit", "panel", "twin", "experiment")


def load_workflow_kinds(kit_dir):
    """`{kind: row}` of `workflows.toml`'s `[[kind]]` rows, in file order (TOOL-dBoundRoles-16 S1): the
    named defaults `derive_stage_rows` applies. A `kind` that is no array of tables, a row whose `kind`
    is not a string, or a kind two rows name raises RolesError naming the file, R9, since each makes the
    map ambiguous. The values are not graded here: R9 grades them."""
    where = (pathlib.Path(kit_dir) / "workflows.toml").as_posix()
    rows = load_workflow_table(kit_dir).get("kind", [])
    if not isinstance(rows, list) or not all(isinstance(r, dict) for r in rows):
        raise RolesError("%s: R9 — 'kind' is not an array of [[kind]] tables" % where)
    out = {}
    for i, row in enumerate(rows, 1):
        name = row.get("kind")
        if not isinstance(name, str):
            raise RolesError("%s: R9 — [[kind]] row %d's kind %r is not a string" % (where, i, name))
        if name in out:
            raise RolesError("%s: R9 — [[kind]] row %d repeats the kind '%s'" % (where, i, name))
        out[name] = row
    return out


def derive_stage_rows(entry, kinds):
    """One workflow entry's stage rows with its kind's defaults applied (TOOL-dBoundRoles-16 S1), the
    one place a default is applied: each a copy of its row carrying `kind`, the row's own else its
    entry's; `fan` and `cap`, the row's own else its kind row's, and for an `experiment` kind the
    entry's `[workflow.experiment]` table's `fan` for both; and `merge` and `twin`, the entry's own else
    its kind row's. `kinds` is `load_workflow_kinds`' map; `{}` applies no default. A value none of them
    gives stays absent, for R9 to name, and a row that is not a table is skipped, as R9 names it."""
    rows = entry.get("stages") if isinstance(entry, dict) else None
    out = []
    for row in rows if isinstance(rows, list) else ():
        if not isinstance(row, dict):
            continue
        got, kind = dict(row), row.get("kind", entry.get("kind"))
        held = kinds.get(kind, {}) if isinstance(kind, str) else {}
        if kind == "experiment":
            table = entry.get("experiment")
            fan = table.get("fan") if isinstance(table, dict) else None
            held = dict(held, **({"fan": fan, "cap": fan} if fan is not None else {}))
        if kind is not None:
            got["kind"] = kind
        for field in ("fan", "cap"):
            if field not in got and field in held:
                got[field] = held[field]
        for field in ("merge", "twin"):
            value = entry.get(field, held.get(field))
            if field not in got and value is not None:
                got[field] = value
        out.append(got)
    return out


def derive_stage_map(entry):
    """The ordered `{stage key: role}` map of one workflow entry's stage rows (TOOL-dBoundRoles-22 S2),
    read from `derive_stage_rows`, which no key or role defaults: the one map every reader of an
    entry's stages takes. `{}` where the entry holds no rows, and a row that is not a table, or whose
    `key` or `role` is not a string, is skipped, since R9 names it. A key repeated in its entry keeps
    its first row's role."""
    out = {}
    for row in derive_stage_rows(entry, {}):
        if isinstance(row.get("key"), str) and isinstance(row.get("role"), str):
            out.setdefault(row["key"], row["role"])
    return out


def parse_role_shapes(value):
    """The kinds a role's `shapes` value declares (TOOL-dBoundRoles-16 S5), comma-separated, in order."""
    return [s.strip() for s in (value or "").split(",") if s.strip()]


def read_agent_limit(root):
    """The repository's agent limit (TOOL-dBoundRoles-22 S5): the resolved value of
    `runtime.agents-in-flight` in the repository at `root`, whatever its source, through
    `read_policy_setting` with its catalogue default, or None where no policy kit answers. A refusal of
    the reader raises its RolesError."""
    value = read_policy_setting("runtime.agents-in-flight", root, with_default=True)
    return None if value is None else int(value)


def read_workflow_order(kit_dir):
    """`{workflow name: order}` from the loop definition (TOOL-dDeclaredLoop-1): each workflow's build
    order, 0 for an any-time one, which this kit's table no longer carries. The loop kit is found by
    `resolve_kit_dir` from `kit_dir` and its reader imported, as `read_cap_answer` reaches the policy
    kit. No loop kit, or a definition its reader refuses, raises RolesError naming it."""
    import sys
    try:
        kit = str(resolve_kit_dir("loop", "loop_lib.py", kit_dir))
        if kit not in sys.path:
            sys.path.insert(0, kit)
        import loop_lib  # the loop kit's reader, found above
    except (LookupError, ImportError) as exc:
        raise RolesError("no loop kit places the workflows: %s" % exc)
    try:
        return loop_lib.read_workflow_order(kit)
    except loop_lib.LoopError as exc:
        raise RolesError("the loop definition does not read: %s" % exc)


def extract_workflow_harnesses(workflows):
    """The `harness` value of each `[[workflow]]` entry whose `driver` is `workflow`, in table order."""
    return [w.get("harness") for w in workflows if w.get("driver") == "workflow"]


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


def check_gate_names(names, legs, where):
    """`(defects, notes)` of one role's granted leg names `names` against `legs`, the tool root's gate
    manifest's names or None where it does not read (TOOL-dBoundRoles-21 S6), `where` the prefix each
    line opens with, `<file>: <rule> — <key>`. A name ending in `?` is optional (TOOL-aOrientedCast-13):
    a leg the manifest lacks is a note rather than a defect, and a `?` alone names no leg. Both grant
    homes, the house file's `[gates]` row and a role's `gates` field, are graded here."""
    defects, notes = [], []
    for n in names:
        leg = n[:-1] if n.endswith("?") else n
        if not leg:
            defects.append("%s — %r names no leg" % (where, n))
        elif legs is not None and leg not in legs:
            if leg == n:
                defects.append("%s — %r names no leg of %s" % (where, n, GATE_MANIFEST))
            else:
                notes.append("holds no leg '%s', which %s marks optional, so it is granted no such leg here"
                             % (leg, where))
    return defects, notes


def load_policy(kit_dir, roles, workflows, notes=None):
    """The parsed `house/policy.toml`, validated against the roles and the workflow table.

    Every defect is collected, then raised once as a RolesError with one line per defect, each
    naming the file, the dotted key and the rule (R12). An absent file is an empty fallback
    (TOOL-dBoundRoles-21 S7): the returned policy holds no `effort` table, so each level falls to the
    policy keys and the role's declared `effort`. An unreadable or unparsable file refuses.

    `gates` in the returned policy is the MERGED grant (TOOL-dBoundRoles-21 S6, §8 F10): each role
    slot maps to the legs of its `gates` field, else to the house file's `[gates]` row only where the
    role sets no field, so every reader takes this one map. `[gates]` (TOOL-aOrientedCast-11) maps a
    role slot whose `agent` is true to the gate legs it may run, by name; both homes are graded by
    `check_gate_names` against the tool root's gate manifest, only when that manifest reads; when it
    does not, one line is appended to `notes` (when given) instead of a defect. A name ending in `?`
    is OPTIONAL (TOOL-aOrientedCast-13): a leg the manifest lacks is a note rather than a defect, and
    the returned grant carries every name with its `?` taken off. `declared` maps each role slot to
    its front matter's `effort`, the last step of the effort order.

    `[effort.profiles.<name>]` (TOOL-aProfiledEffort-1) is a level table for one model family: a
    `match` list of words and the keys of `[effort]` itself, graded by the same helper. A word two
    profiles hold is a defect on the later one. Which words are model families is not checked, so
    two profiles holding different words of one id load, and `resolve_profile` refuses that id.

    Every level of either table is held to `EFFORT_FLOOR` (TOOL-dBoundRoles-23 S5): a house level below it is
    an R12 defect naming the floor and the policy key the owner writes instead, `check_effort_floor`'s line.
    """
    path = pathlib.Path(kit_dir) / "house" / "policy.toml"
    where = path.as_posix()
    present = True
    try:
        with open(path, "rb") as fh:
            data = tomllib.load(fh)
    except FileNotFoundError:   # the empty fallback: no house level, no house grant
        data, present = {}, False
    except OSError as e:
        raise RolesError("%s: R12 — the policy file cannot be read — %s" % (where, e.strerror))
    except tomllib.TOMLDecodeError as e:
        raise RolesError("%s: R12 — the policy file is not valid TOML — %s" % (where, e))
    bad = []

    def check_level(key, value):
        if value not in EFFORT_LEVELS:
            bad.append("%s: R12 — %s — %r is not a level; the levels are %s"
                       % (where, key, value, ", ".join(EFFORT_LEVELS)))
            return
        # TOOL-dBoundRoles-23 S5: the house file is a fallback held to the floor, a profile's levels included
        try:
            check_effort_floor(value, "the house file's " + key)
        except RolesError as e:
            bad.append("%s: R12 — %s — %s" % (where, key, e))

    by_name = {w.get("name"): w for w in workflows}

    def check_effort_table(at, table, own):
        """The checks of one level table, `[effort]` or a profile, whose dotted key is `at` and
        which holds the key `own` beside POLICY_EFFORT_KEYS."""
        for k in table:
            if k not in POLICY_EFFORT_KEYS + (own,):
                bad.append("%s: R12 — %s.%s — unknown key; %s holds %s"
                           % (where, at, k, at, ", ".join(POLICY_EFFORT_KEYS + (own,))))
        if "default" not in table:
            bad.append("%s: R12 — %s.default — is absent" % (where, at))
        else:
            check_level(at + ".default", table["default"])
        role_levels = table.get("roles", {})
        if not isinstance(role_levels, dict):
            role_levels = {}
            bad.append("%s: R12 — %s.roles — is not a table" % (where, at))
        for slot, level in role_levels.items():
            key = "%s.roles.%s" % (at, slot)
            check_level(key, level)
            if slot not in roles:
                bad.append("%s: R12 — %s — names no role file" % (where, key))
            elif roles[slot]["keys"].get("agent", "true") == "false":
                bad.append("%s: R12 — %s — names an agent: false role, so no agent type carries it"
                           % (where, key))
        stage_levels = table.get("stages", {})
        if not isinstance(stage_levels, dict):
            stage_levels = {}
            bad.append("%s: R12 — %s.stages — is not a table" % (where, at))
        for name, levels in stage_levels.items():
            key = "%s.stages.%s" % (at, name)
            if not isinstance(levels, dict):
                bad.append("%s: R12 — %s — is not a table" % (where, key))
                continue
            if name not in by_name:
                bad.append("%s: R12 — %s — names no workflow" % (where, key))
                continue
            held = derive_stage_map(by_name[name])
            if not held:
                bad.append("%s: R12 — %s — the workflow %s has no stage rows" % (where, key, name))
                continue
            for stage, level in levels.items():
                check_level("%s.%s" % (key, stage), level)
                if stage not in held:
                    bad.append("%s: R12 — %s.%s — is not a stage key of %s, whose keys are %s"
                               % (where, key, stage, name, ", ".join(sorted(held))))

    for k in data:
        if k not in POLICY_TABLES:
            bad.append("%s: R12 — %s — unknown top-level key; the tables are %s"
                       % (where, k, " and ".join(POLICY_TABLES)))
    effort = data.get("effort", {})
    if not isinstance(effort, dict):
        effort = {}
        bad.append("%s: R12 — effort — is not a table" % where)
    if present:
        check_effort_table("effort", effort, "profiles")
    profiles = effort.get("profiles", {})
    if not isinstance(profiles, dict):
        profiles = {}
        bad.append("%s: R12 — effort.profiles — is not a table" % where)
    matched = {}
    for name, profile in profiles.items():
        at = "effort.profiles." + name
        if not isinstance(profile, dict):
            bad.append("%s: R12 — %s — is not a table" % (where, at))
            continue
        check_effort_table(at, profile, "match")
        words = profile.get("match")
        if "match" not in profile:
            bad.append("%s: R12 — %s.match — is absent" % (where, at))
        elif not isinstance(words, list) or not all(isinstance(w, str) for w in words):
            bad.append("%s: R12 — %s.match — is not a list of strings" % (where, at))
        elif not words:
            bad.append("%s: R12 — %s.match — is empty, so the profile matches no model" % (where, at))
        else:
            for word in words:
                if not MODEL_SEGMENT_RE.fullmatch(word):
                    bad.append("%s: R12 — %s.match — %r is not one word; an entry is one run of "
                               "lower-case letters and digits" % (where, at, word))
                elif matched.setdefault(word, name) != name:
                    bad.append("%s: R12 — %s.match — %r is also in effort.profiles.%s.match, so two "
                               "profiles match one model" % (where, at, word, matched[word]))
    gates = data.get("gates", {})
    if not isinstance(gates, dict):
        gates = {}
        bad.append("%s: R12 — gates — is not a table" % where)
    manifest = (pathlib.Path(kit_dir).parent / GATE_MANIFEST).as_posix()
    # each role's `gates` field, comma-separated as `[gates]` spells a row's names (TOOL-dBoundRoles-21 S6)
    fields = {slot: [n.strip() for n in r["keys"]["gates"].split(",") if n.strip()]
              for slot, r in roles.items() if "gates" in r["keys"]}
    legs = load_gate_leg_names(pathlib.Path(kit_dir).parent) if gates or fields else None
    graded = []   # `(where, names)` of every grant, the house rows first, then the fields
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
        graded.append(("%s: R12 — %s" % (where, key), names))
    for slot, names in fields.items():
        at = "%s: R2 — gates" % roles[slot]["path"].as_posix()
        if roles[slot]["keys"].get("agent", "true") == "false":
            bad.append("%s — is set on an agent: false role, so no agent type carries it" % at)
        graded.append((at, names))
    for at, names in graded:
        defects, said = check_gate_names(names, legs, at)
        bad.extend(defects)
        if notes is not None:
            notes.extend("%s %s" % (manifest, n) for n in said)
    if (gates or fields) and legs is None and notes is not None:
        notes.append("%s cannot be read, so the leg names under [gates] in %s and in the roles' gates "
                     "fields are not checked" % (manifest, where))
    if bad:
        raise RolesError("\n".join(bad))
    data["gates"] = {slot: [n[:-1] if n.endswith("?") else n for n in names]
                     for slot, names in {**gates, **fields}.items()}
    data["declared"] = {slot: r["keys"].get("effort") for slot, r in roles.items()}
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
        found.append({"path": rel, "role": m.group("role"), "build": m.group("build"), "unit": m.group("unit")})
    return found, defects


def derive_answers_value(path, task_sha):
    """`<path> task-sha=<task_sha>`, the one value a return's `**Answers:**` line and a harness return's
    `answers` field carry: `path` the work order's repo-relative path, forward-slashed (TOOL-dBoundRoles-17 S4)."""
    return "%s task-sha=%s" % (pathlib.PurePath(str(path).replace("\\", "/")).as_posix(), task_sha)


def extract_return_object(text, template):
    """`(object, why)` of a direct reply read against `template`, `parse_return_template`'s triples
    (TOOL-dBoundRoles-5 S1): the reply's last fenced `json` block, which must parse as a JSON object;
    else the whole reply where it parses as one JSON object; else, for a template with no `list` field,
    the `key: value` lines outside every fence naming the template's fields, the block shape the
    orientation return takes, the first line naming a field winning and an `int` field's digits read as
    an integer. `(None, why)` where none of the three holds, `why` saying which."""
    text = str(text or "").replace("\r\n", "\n")
    blocks = RETURN_JSON_FENCE_RE.findall(text)
    if blocks:
        try:
            obj = json.loads(blocks[-1][1])
        except (ValueError, RecursionError):
            obj = None
        return (obj, "") if isinstance(obj, dict) else (None, "the reply's last `json` block is no JSON object")
    try:
        obj = json.loads(text.strip())
    except (ValueError, RecursionError):
        obj = None
    if isinstance(obj, dict):
        return obj, ""
    if any(kind == "list" for _name, kind, _optional in template):
        return None, ("the reply holds no `json` block and is no JSON object, and a template with a `list` "
                      "field is read from JSON alone")
    kinds = {name: kind for name, kind, _optional in template}
    found = {}
    for _n, line in read_unfenced_lines(text):
        m = RETURN_LINE_RE.match((line or "").strip())
        if m and m.group(1) in kinds and m.group(1) not in found:
            value = m.group(2)
            found[m.group(1)] = int(value) if kinds[m.group(1)] == "int" and re.fullmatch(r"-?[0-9]+", value) \
                else value
    if found:
        return found, ""
    return None, ("the reply holds no `json` block, is no JSON object, and names none of the template's "
                  "fields on a `key: value` line")


def check_return_value(name, kind, value, root):
    """The defect lines of one return field's value by the value rules of TOOL-dBoundRoles-5 §4: `text`
    a non-empty string; `sha` 7 to 40 hex digits naming a commit `git cat-file -e <sha>^{commit}`
    resolves in `root`; `path` a repo-relative string with no `..` segment naming a file under `root`;
    `list` a JSON array; `int` a JSON integer; a closed set one of its values."""
    import os
    import subprocess
    shown = json.dumps(value, ensure_ascii=False)
    shown = shown if len(shown) <= 80 else shown[:77] + "..."
    if isinstance(kind, tuple):
        if isinstance(value, str) and value in kind:
            return []
        return ["%s — %s is outside its set %s" % (name, shown, "|".join(kind))]
    if kind == "list":
        ok = isinstance(value, list)
    elif kind == "int":
        ok = isinstance(value, int) and not isinstance(value, bool)
    else:
        ok = isinstance(value, str) and bool(value.strip())
    if not ok:
        return ["%s — %s is not %s" % (name, shown, "a non-empty string" if kind == "text"
                                        else "a string, as %s is" % RETURN_TYPE_WORDS[kind]
                                        if kind in ("sha", "path") else RETURN_TYPE_WORDS[kind])]
    if kind == "sha":
        if not RETURN_SHA_RE.match(value):
            return ["%s — %s is not a sha of 7 to 40 hex digits" % (name, shown)]
        env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
        try:
            p = subprocess.run(["git", "-C", str(root), "cat-file", "-e", value + "^{commit}"],
                               capture_output=True, stdin=subprocess.DEVNULL, env=env)
            named = p.returncode == 0
        except OSError:
            named = False
        if not named:
            return ["%s — %s names no commit in %s" % (name, shown, pathlib.Path(root).as_posix())]
    if kind == "path":
        rel = value.replace("\\", "/")
        if rel.startswith("/") or re.match(r"^[A-Za-z]:", rel) or ".." in rel.split("/"):
            return ["%s — %s is not a repo-relative path free of `..` segments" % (name, shown)]
        if not (pathlib.Path(root) / rel).is_file():
            return ["%s — %s names no file under %s" % (name, shown, pathlib.Path(root).as_posix())]
    return []


def check_return(role, text, root=None, work_order=None):
    """The defect lines of a direct return checked against its role's typed `return` template, shared
    interface I16 (TOOL-dBoundRoles-5 S1); an empty list is a valid return. `role` is a slot of
    `load_roles`, its template read by `parse_return_template`, and the return object is
    `extract_return_object`'s. Each line names a field, or `return object`, and the rule: no return
    object; a required field absent; a field the template does not name; a value `check_return_value`
    refuses, a `sha` naming no commit in `root` and a `path` naming no file under it included; an
    `answers` value off `ANSWERS_VALUE_RE`; and, with `work_order` a `(path, task_sha)` pair, an
    `answers` other than `derive_answers_value`'s for it, `answers` then admitted beside the template's
    fields. `root` defaults to the toplevel of the working directory. RolesError on a slot the catalogue
    lacks, or a role file or template that does not parse.

    With `work_order` given, a `list` field longer than the bound the work order's return contract states
    for it, `read_return_bounds`' read of that file under `root`, is a defect naming the field and the
    bound (TOOL-dBoundRoles-23 S3).

    A return whose `outcome` is the refusal arm's, `load_refusal_arm`'s `refused`, is read against that arm
    rather than the role's template, the role's own `answers` field kept beside it: each arm field is graded
    by `check_refusal_arm`, an `actor` outside the arm's five forms and an empty `rule` or `remedy` each a line
    naming the field, and a field neither names is a defect as above (TOOL-dBoundRoles-26 S2).

    WHAT THIS DOES NOT CHECK: that an `answers` is present where the work order is given, the field's
    presence being TOOL-dBoundRoles-17's; what a `text` value says; nor which commit a `sha` names; nor a
    bound where the work order file does not read or its `### return` block states none."""
    import subprocess
    roles = load_roles(pathlib.Path(__file__).absolute().parent)
    if role not in roles:
        raise RolesError("no role '%s' in the catalogue; its slots are %s" % (role, ", ".join(roles)))
    template = parse_return_template(roles[role]["keys"].get("return"))
    if root is None:
        try:
            g = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True,
                               encoding="utf-8", errors="replace", stdin=subprocess.DEVNULL)
            root = g.stdout.strip() if g.returncode == 0 and g.stdout.strip() else "."
        except OSError:
            root = "."
    obj, why = extract_return_object(text, template)
    # TOOL-dBoundRoles-26 S2: a return whose `outcome` is the refusal arm's is read against the arm, not the
    # role's template: its fields read again under the arm's names, the role's own `answers` kept beside them,
    # and each arm field graded by `check_refusal_arm` alone
    arm = load_refusal_arm()
    refusing = False
    if obj is None or obj.get("outcome") == arm["outcome"]:
        shape = [("outcome", (arm["outcome"],), False)] + [(f, "text", False) for f in arm["fields"]] \
            + [t for t in template if t[0] == "answers"]
        refused, _why = extract_return_object(text, shape + ([] if any(t[0] == "answers" for t in shape)
                                                             else [("answers", "text", True)]))
        if isinstance(refused, dict) and refused.get("outcome") == arm["outcome"]:
            template, obj, refusing = shape, refused, True
    if obj is None:
        return ["return object — %s" % why]
    kinds = {name: kind for name, kind, _optional in template}
    defects = check_refusal_arm(obj, arm) if refusing else []
    for name, kind, optional in template:
        if refusing and name in arm["fields"]:
            continue
        if name in obj:
            defects += check_return_value(name, kind, obj[name], root)
        elif not optional:
            defects.append("%s — a required field is absent" % name)
    admitted = "answers" in kinds or work_order is not None
    for name in obj:
        if name not in kinds and not (name == "answers" and admitted):
            defects.append("%s — a field the template does not name; its fields are %s" % (name, ", ".join(kinds)))
    if "answers" in obj and admitted:
        said = obj["answers"]
        if not isinstance(said, str) or not ANSWERS_VALUE_RE.fullmatch(said):
            defects.append("answers — %s is not `<work order path> task-sha=<12 hex>`"
                           % json.dumps(said, ensure_ascii=False)[:80])
        elif work_order is not None and said != derive_answers_value(*work_order):
            defects.append("answers — %s is not %s, the work order this agent was handed"
                           % (json.dumps(said, ensure_ascii=False), derive_answers_value(*work_order)))
    bounds = read_return_bounds(root, work_order) if work_order is not None else {}
    for name, kind, _optional in template:
        value = obj.get(name)
        if kind == "list" and name in bounds and isinstance(value, list) and len(value) > bounds[name]:
            defects.append("%s — %d entries, past the bound of %d the work order's return contract states, `%s`"
                           % (name, len(value), bounds[name], RETURN_BOUND_LINE % (name, bounds[name])))
    return defects


def read_return_bounds(root, work_order):
    """`{field: bound}` of the `RETURN_BOUND_RE` lines of the last `### return` block of the work order
    `work_order`, a `(path, task_sha)` pair, its file read under `root` (TOOL-dBoundRoles-23 S3): the lines
    `read_unfenced_lines` yields from that heading to the next heading, so a line inside handed content is
    none. `{}` where the path is not repo-relative and free of `..` segments, or its file does not read as
    UTF-8. WHAT IT DOES NOT CHECK: that the file's task-sha is the pair's."""
    rel = str(work_order[0] or "").replace("\\", "/")
    if not rel or rel.startswith("/") or re.match(r"^[A-Za-z]:", rel) or ".." in rel.split("/"):
        return {}
    try:
        text = (pathlib.Path(root) / rel).read_bytes().decode("utf-8").replace("\r\n", "\n")
    except (OSError, UnicodeDecodeError):
        return {}
    bounds, inside = {}, False
    for _n, line in read_unfenced_lines(text):
        if line is None:
            continue
        if line.startswith("#"):
            inside = line.rstrip() == "### return"
            bounds = {} if inside else bounds
            continue
        m = RETURN_BOUND_RE.match(line.rstrip()) if inside else None
        if m:
            bounds[m.group("field")] = int(m.group("bound"))
    return bounds


def read_answered_work_order(root, said):
    """`(rel, text, marker, why)` of the work order a return's `answers` value `said` names, read under `root`
    (TOOL-dBoundRoles-12 S3, and TOOL-dBoundRoles-26 S4's producer route): `rel` its repo-relative path, `text`
    its text with CRLF folded, `marker` its first `MARKER_RE` line outside a fence. Where one fails, `why` is the
    `answers — ` line naming it and the items not reached are None: a value off `ANSWERS_VALUE_RE`, a path that
    is not repo-relative and free of `..` segments, a file that does not read as UTF-8, and no marker line;
    `why` is '' for a work order that reads with its marker."""
    m = ANSWERS_VALUE_RE.fullmatch(said) if isinstance(said, str) else None
    if not m:
        return None, None, None, ("answers — %s is not `<work order path> task-sha=<12 hex>`"
                                  % json.dumps(said, ensure_ascii=False)[:80])
    rel = m.group("path")
    if rel.startswith("/") or re.match(r"^[A-Za-z]:", rel) or ".." in rel.split("/"):
        return rel, None, None, "answers — %s is not a repo-relative path free of `..` segments" % rel
    try:
        text = (pathlib.Path(root) / rel).read_bytes().decode("utf-8").replace("\r\n", "\n")
    except (OSError, UnicodeDecodeError) as e:
        return rel, None, None, ("answers — the work order %s cannot be read under %s: %s"
                                 % (rel, pathlib.Path(root).as_posix(), getattr(e, "strerror", None) or e))
    marker = next((mk for _n, line in read_unfenced_lines(text) if line is not None
                   for mk in [MARKER_RE.fullmatch(line)] if mk), None)
    if marker is None:
        return rel, text, None, ("answers — %s carries no gov:handoff marker line outside a fence, so it is no "
                                 "rendered work order and names no role" % rel)
    return rel, text, marker, ""


#: A work order's upstream rows block, and one of its rows, `- <upstream item>#<row id> · <kind> · <text>`, the
#: loop kit's `upstream.py rows` line (TOOL-dDeclaredLoop-29), its item read by `extract_upstream_item`.
UPSTREAM_ROWS_KEY = "upstream:rows"
UPSTREAM_ROW_RE = re.compile(r"^- (?P<item>item(?:\.[a-z0-9][a-z0-9-]*){2,})#\S+ · ")


def extract_upstream_item(text):
    """The upstream item of the first row of the work order `text`'s `### upstream:rows` block, in the rows' own
    order (TOOL-dBoundRoles-26 §4, the producer route): the first `UPSTREAM_ROW_RE` line, handed content inside
    the block's fence included, between that heading outside a fence and the next heading outside one; None
    where the work order holds no such block or the block no row."""
    lines = str(text or "").split("\n")
    heads = [n for n, line in read_unfenced_lines(text or "") if line is not None and line.startswith("#")]
    start = next((n for n in heads if lines[n - 1].rstrip() == "### " + UPSTREAM_ROWS_KEY), None)
    if start is None:
        return None
    end = next((n for n in heads if n > start), len(lines) + 1)
    return next((m.group("item") for line in lines[start:end - 1] for m in [UPSTREAM_ROW_RE.match(line)] if m), None)


#: The policy key bounding how often an item goes back to the agent that returned it (TOOL-dBoundRoles-5 S3).
RETRIES_KEY = "roles.retries"


def resolve_refusal_route(refusal, role, build, repo, budget_spent=False):
    """The route of the refused return object `refusal` by its `actor`, `REFUSAL_ROUTES`' one reader
    (TOOL-dBoundRoles-26 S3): `{"actor", "route", "reoffer", "draw", "fields"}`, `fields` the route line's
    trailing fields in order. `role` and `build` are the answered work order's marker's, `-` with none; `repo`
    the repository whose policy keys are read. `self` is `retry`, re-offered `bounded`, its field the
    `roles.retries` bound and the role; `producer` is `route-back` to the item of the first upstream row of the
    work order the return's `answers` names, `extract_upstream_item`'s, and with no such item `driver`, its
    field saying why; `owner` is `owner`, its field `resolve_owner_question(kind="refusal")`'s answer with the
    owner away and `budget_spent` handed on, and `choose-ending` names `OWNER_ENDINGS` in rank; `build:<slug>`
    is `ask build:<slug>`. Every route but `retry` re-offers `never`. Each closes with `build <build>` and the
    draw TOOL-dDeclaredLoop-30 takes. RolesError naming the actor where it is none of the arm's forms, and the
    owner reader's own refusal."""
    arm = load_refusal_arm()
    actor = refusal.get("actor")
    kind = derive_refusal_kind(actor, arm) if isinstance(actor, str) else None
    if kind is None:
        raise RolesError("actor — %s is none of %s" % (json.dumps(actor, ensure_ascii=False)[:80],
                                                       ", ".join(arm["actors"])))
    route, reoffer, draw = REFUSAL_ROUTES[kind]
    fields = []
    if kind == "self":
        retries = read_policy_setting(RETRIES_KEY, repo, with_default=True)
        fields.append("retries %s · role %s" % ("unread" if retries is None else retries, role))
    elif kind == "producer":
        said = refusal.get("answers")
        _rel, text, _marker, why = read_answered_work_order(repo, said) if said is not None else (
            None, None, None, "the return names no work order it answers")
        item = extract_upstream_item(text) if text is not None else None
        if item:
            fields.append("item %s" % item)
        else:
            route, reoffer, draw = REFUSAL_ROUTES["driver"]
            fields.append("item none — %s, so the driver performs the remedy" % (
                why.split("answers — ", 1)[-1] or "the work order %s holds no %s row" % (_rel, UPSTREAM_ROWS_KEY)))
    elif kind == "owner":
        answer = resolve_owner_question("refusal", False, repo, budget_spent)
        fields.append("answer %s" % answer + (" · endings %s" % " > ".join(OWNER_ENDINGS)
                                              if answer == "choose-ending" else ""))
    elif kind == "build":
        route = "%s %s" % (route, actor)
    fields += ["build %s" % build, "draw %s" % draw]
    return {"actor": actor, "route": route, "reoffer": reoffer, "draw": draw, "fields": fields}


def derive_frame(blocks):
    """The blocks of a work order's `reads` fill in frame order (TOOL-dBoundRoles-23 S1, shared interface I15):
    each block a tuple whose first item is its slot and second its text, any further items carried along,
    sorted by the slot's place in `FRAME_SLOTS`, a stable sort, so two blocks of one slot keep the order
    they were added in. RolesError naming every block, by its first line, whose slot is none or outside
    `FRAME_SLOTS`, so no block is placed silently."""
    bad = [b for b in blocks if b[0] not in FRAME_SLOTS]
    if bad:
        raise RolesError("\n".join("the frame block %s carries the slot %r, which is not one of %s"
                                   % (str(b[1]).split("\n", 1)[0], b[0], ", ".join(FRAME_SLOTS)) for b in bad))
    return sorted(blocks, key=lambda b: FRAME_SLOTS.index(b[0]))


def scan_work_orders(root, memory_root, slots):
    """`(found, counts)` of rule R16 over the two populations of TOOL-dBoundRoles-17 §4, every record read
    and none written. A HANDOFF is a file `<MEMORY_ROOT>/builds/<slug>/prompts/<date>-prompt-<id>-<n>-<tail>
    [-<suffix>].md` whose `<tail>` is one of `slots` without `gov-`, the name `derive_prompt_name` writes; it
    offends with no marker line, or a marker carrying no `item=`. A RETURN is a record under
    `<MEMORY_ROOT>/builds/<slug>/build/` whose first `**Serves:**` kind is `research` and whose text, its
    own `**Answers:**` lines set aside, names exactly one handoff's file name, in whatever path cites it;
    it offends with no `ANSWERS_RE` line, or one whose path is not that handoff's or whose `task-sha` is
    not that handoff's marker's. `found` is `[(repo-relative path, what)]`, sorted, one per offence; an
    unreadable record is one. `counts` holds `handoffs` and `returns`. WHAT IT DOES NOT CHECK: a handoff
    under another name, a return of another kind or naming its work order by no file name, a return
    naming two work orders, nor whether a marker's `item=` names an item the loop defines."""
    root = pathlib.Path(root)
    tails = sorted((s[4:] if s.startswith("gov-") else s for s in slots), key=len, reverse=True)
    if not tails:
        return [], {"handoffs": 0, "returns": 0}
    name_re = re.compile(r"^\d{4}-\d{2}-\d{2}-prompt-\S+?-[0-9]+-(?:%s)(?:-[a-z0-9-]+)?\.md$"
                         % "|".join(re.escape(t) for t in tails))
    builds = root / memory_root / "builds"
    found, handoffs = [], {}
    for p in sorted(builds.glob("*/prompts/*.md")):
        if not name_re.match(p.name):
            continue
        rel = p.relative_to(root).as_posix()
        try:
            m = MARKER_RE.search(load_text(p))
        except (RolesError, UnicodeDecodeError) as e:
            found.append((rel, "the work order cannot be read as UTF-8 — %s" % e))
            handoffs[p.name] = (rel, None)
            continue
        handoffs[p.name] = (rel, m)
        if not m:
            found.append((rel, "the work order carries no gov:handoff marker line; render it with handoff.py "
                               "render, whose marker names the item it was cut for"))
        elif m.group("item") is None:
            found.append((rel, "the work order's marker carries no item= field; render it with handoff.py "
                               "render, which writes item=<tag> or item=-"))
    names_re = re.compile(r"\d{4}-\d{2}-\d{2}-prompt-[A-Za-z0-9-]+\.md")
    serves_re = re.compile(r"^\*\*Serves:\*\*[ \t]+(\S+)", re.M)
    n_returns = 0
    for p in sorted(builds.glob("*/build/*.md")):
        rel = p.relative_to(root).as_posix()
        try:
            text = load_text(p)
        except (RolesError, UnicodeDecodeError) as e:
            found.append((rel, "the record cannot be read as UTF-8 — %s" % e))
            continue
        kind = serves_re.search(text)
        if not kind or kind.group(1) != "research":
            continue
        lines = text.split("\n")
        rest = "\n".join(ln for ln in lines if not ln.startswith(ANSWERS_KEY))
        named = sorted({n for n in names_re.findall(rest) if n in handoffs})
        if len(named) != 1:
            continue
        n_returns += 1
        want, marker = handoffs[named[0]]
        said = [a for a in (ANSWERS_RE.fullmatch(ln) for ln in lines) if a]
        if not said:
            found.append((rel, "the return names the work order %s and carries no '%s %s' line"
                          % (want, ANSWERS_KEY, derive_answers_value(want, "<12hex>"))))
        for a in said:
            if a.group("path") != want:
                found.append((rel, "the %s line names %s, and the work order its text names is %s"
                              % (ANSWERS_KEY, a.group("path"), want)))
            elif marker is None:
                found.append((rel, "the %s line's task-sha %s cannot be compared: %s carries no readable "
                                   "gov:handoff marker" % (ANSWERS_KEY, a.group("task_sha"), want)))
            elif a.group("task_sha") != marker.group("task_sha"):
                found.append((rel, "the %s line's task-sha %s is not %s, the task-sha of %s's marker"
                              % (ANSWERS_KEY, a.group("task_sha"), marker.group("task_sha"), want)))
    return sorted(found), {"handoffs": len(handoffs), "returns": n_returns}


def read_work_order_legacy(root, memory_root):
    """`(rows, why)` of the work-order legacy home `<MEMORY_ROOT>/project/work-order-legacy.txt`: `rows` the
    set of repo-relative paths it lists, one per line, `#` lines and blank ones skipped, each read as an
    exact path and never a pattern; None with `why` where the home is absent, does not read, or holds a
    failed seed's `# unarmed · ` line among its first two, so R16 grades nothing and says why."""
    home = pathlib.Path(root) / memory_root / "project" / WORK_ORDER_LEGACY
    try:
        text = home.read_bytes().decode("utf-8").replace("\r\n", "\n")
    except FileNotFoundError:
        return None, "no %s/project/%s" % (memory_root, WORK_ORDER_LEGACY)
    except (OSError, UnicodeDecodeError) as e:
        return None, "%s/project/%s does not read — %s" % (memory_root, WORK_ORDER_LEGACY, e)
    lines = text.split("\n")
    if any(ln.startswith(LEGACY_UNARMED_LEAD) for ln in lines[:2]):
        return None, "%s/project/%s is unarmed: %s" % (memory_root, WORK_ORDER_LEGACY,
                                                        next(ln for ln in lines[:2] if ln.startswith(LEGACY_UNARMED_LEAD)))
    return {ln.strip() for ln in lines if ln.strip() and not ln.startswith("#")}, ""


def resolve_profile(policy, model):
    """The name of the one `[effort.profiles.<name>]` table whose `match` holds a word of the model
    id, or None when none does or no model is named (TOOL-aProfiledEffort-1); None is also the answer
    for an id that holds no word, given before any profile is read (TOOL-aProfiledEffort-4). The
    words are the id's runs of letters and digits after lower-casing, so an entry matches a whole
    word and never a substring. Two profiles matching one model raise a RolesError: no profile wins by file order."""
    words = set(MODEL_SEGMENT_RE.findall((model or "").lower()))
    if not words:
        return None
    hits = [name for name, profile in policy.get("effort", {}).get("profiles", {}).items()
            if words.intersection(profile["match"])]
    if len(hits) > 1:
        raise RolesError("R12 — the model %r — matches %s, so no one profile's levels are its own"
                         % (model, " and ".join("effort.profiles.%s.match" % n for n in hits)))
    return hits[0] if hits else None


def resolve_house_table(policy, model):
    """The house file's level table `model` takes, the profile `resolve_profile` names or else
    `[effort]`; None where the house file is absent, its empty fallback."""
    if "effort" not in policy:
        return None
    name = resolve_profile(policy, model)
    return policy["effort"]["profiles"][name] if name else policy["effort"]


def resolve_effort(policy, slot, model, root):
    """A role's level for its agent type, the first of (TOOL-dBoundRoles-21 S2, §4 "The order"): the
    policy key `roles.effort.<slot>`, then `roles.effort.default`, both read in the repository at
    `root`; then the house file's level table `model` takes, its `roles` entry, else its `default`;
    then the role's declared `effort`. RolesError where none of them gives a level, and where the level it
    takes is below `EFFORT_FLOOR` from a source `check_effort_floor` refuses (TOOL-dBoundRoles-23 S5)."""
    source = "roles.effort." + slot
    level = read_policy_setting(source, root)
    if level is None:
        source = "roles.effort.default"
        level = read_policy_setting(source, root)
    if level is None:
        table = resolve_house_table(policy, model)
        if table is not None:
            tail = "roles." + slot if slot in table.get("roles", {}) else "default"
            level, source = table.get("roles", {}).get(slot, table["default"]), derive_house_source(policy, model, tail)
    if level is None:
        level, source = policy.get("declared", {}).get(slot), "the role %s's declared effort" % slot
    if not level:
        raise RolesError("%s — no policy key, no house file and no declared effort give the role a level"
                         % slot)
    check_effort_floor(level, source, root)
    return level


def derive_house_source(policy, model, tail):
    """The source `check_effort_floor` names for a house-file level: `the house file's <table>.<tail>`, the
    table `effort.profiles.<name>` where `resolve_profile` names one for `model`, else `effort`."""
    name = resolve_profile(policy, model)
    return "the house file's %s.%s" % ("effort.profiles." + name if name else "effort", tail)


def resolve_stage_efforts(policy, workflow, model, root):
    """`{stage key: level}` for every stage row of a workflow entry, in row order, each the first of
    (TOOL-dBoundRoles-21 S2; TOOL-dBoundRoles-22 S3, §4 "The effort"): the policy keys
    `roles.effort.<workflow>.<stage>`, `roles.effort.<role>` and `roles.effort.default`, read in the
    repository at `root`; then the house file's level table `model` takes, where present, its
    `stages.<workflow>` entry, else its `roles` entry, else its `default`; then the row's own `effort`;
    then the role's declared `effort`, through `resolve_effort`. The rows are `derive_stage_rows`',
    the one read of them (TOOL-dBoundRoles-16 S8), so a row a kind defaults is resolved. Each level taken is
    held to `EFFORT_FLOOR` by its source, `check_effort_floor`'s RolesError naming it (TOOL-dBoundRoles-23 S5)."""
    name, out = workflow.get("name"), {}
    table = held = None   # the house table, resolved at the first stage no key gives a level
    rows = {}
    for row in derive_stage_rows(workflow, {}):
        if isinstance(row.get("key"), str):
            rows.setdefault(row["key"], row)
    for key, slot in derive_stage_map(workflow).items():
        level = None
        for source in (f"roles.effort.{name}.{key}", f"roles.effort.{slot}", "roles.effort.default"):
            level = read_policy_setting(source, root)
            if level is not None:
                break
        if level is None:
            if not held:
                table, held = resolve_house_table(policy, model), True
            if table is not None:
                staged = table.get("stages", {}).get(name, {}).get(key)
                tail = ("stages.%s.%s" % (name, key) if staged else
                        "roles." + slot if slot in table.get("roles", {}) else "default")
                level = staged or table.get("roles", {}).get(slot, table["default"])
                source = derive_house_source(policy, model, tail)
        if level is None:
            level, source = rows[key].get("effort"), "the stage row %s.%s's own effort" % (name, key)
        if level is None:
            out[key] = resolve_effort(policy, slot, model, root)
            continue
        check_effort_floor(level, source, root)
        out[key] = level
    return out


#: Each harness adapter's equivalent of a role's declared `model` (TOOL-dBoundRoles-21 S5): `claude-code`,
#: the one adapter, takes the declared value as written.
HARNESS_MODEL_EQUIVALENT = {"claude-code": lambda declared: declared}


def resolve_role_model(slot, harness, root, kit_dir=None):
    """The model the role `slot` runs on `harness` (TOOL-dBoundRoles-21 S5): the policy key
    `roles.model.<slot>.<harness>` read in the repository at `root`, else the harness adapter's
    equivalent of the role's declared `model`, read from the role file in `kit_dir`, this file's own
    directory unless given, None where the role declares none. An unknown harness is a RolesError,
    never a guess."""
    if harness not in HARNESS_MODEL_EQUIVALENT:
        raise RolesError("the harness '%s' has no model adapter; the adapters are %s"
                         % (harness, ", ".join(sorted(HARNESS_MODEL_EQUIVALENT))))
    value = read_policy_setting(f"roles.model.{slot}.{harness}", root)
    if value is not None:
        return value
    kit = pathlib.Path(kit_dir) if kit_dir is not None else pathlib.Path(__file__).absolute().parent
    path = kit / "agents" / (slot + ".agent.md")
    if not path.is_file():
        raise RolesError("%s: R8 — no role file, so the role %s declares no model" % (path.as_posix(), slot))
    keys, _body = parse_front_matter(path.as_posix(), load_text(path))
    return HARNESS_MODEL_EQUIVALENT[harness](keys.get("model"))


def render_role(kit_dir, name, memory_root, gates=()):
    """The role's base body with `{{MEMORY_ROOT}}` substituted, then the repository's own rules for it, the
    overlay's level-5 units selecting `role.<name>` at HEAD of the repository holding `kit_dir`
    (`read_role_units`), between the playbook render's marked pair `<!-- gov:repo -->` and
    `<!-- /gov:repo -->` (TOOL-dBoundRoles-19 S3), then its `## Never`, `## Ceiling` and `## Return`
    sections, `render_role_fields`' of its front matter and the gate legs `gates` granted it
    (TOOL-dBoundRoles-2 S6), so every route closes the role alike. A house text file under the kit is
    read by no render: the upgrade step `HOUSE_STEP` moves it into the overlay."""
    kit = pathlib.Path(kit_dir).absolute()
    path = kit / "agents" / (name + ".agent.md")
    keys, body = parse_front_matter(path.as_posix(), load_text(path))
    for token in TOKEN_RE.findall(body):
        if token != MEMORY_ROOT_TOKEN:
            raise RolesError("%s: R5 — carries the render token %s; only %s renders"
                             % (path.as_posix(), token, MEMORY_ROOT_TOKEN))
    root = next((d for d in (kit, *kit.parents) if (d / ".git").exists()), kit)
    units = read_role_units(root, kit, name)
    for unit, text in units:
        for token in TOKEN_RE.findall(text):
            if token != MEMORY_ROOT_TOKEN:
                raise RolesError("%s#%s: R10 — carries the render token %s; only %s renders"
                                 % (OVERLAY_FILE, unit.tag, token, MEMORY_ROOT_TOKEN))
    out = body
    if units:
        import render_playbook  # the playbook kit, on the path `read_role_units` put it on
        out += "\n\n" + "\n".join([render_playbook.REPO_OPEN, "\n\n".join(t for _u, t in units),
                                   render_playbook.REPO_CLOSE])
    out += "\n\n" + render_role_fields(keys, gates)
    return out.replace(MEMORY_ROOT_TOKEN, memory_root) + "\n"


def read_role_units(root, kit_dir, slot=None):
    """`((unit, text), ...)`, the overlay's level-5 units that select a `role.` tag, `role.<slot>` alone where
    `slot` is given, each with its rendered text, CRLF folded and its edge newlines cut: a repository's own
    rules for a role (TOOL-dBoundRoles-19 S3, S4). They are read at HEAD of the repository at `root` through
    the playbook kit's `render_playbook.read_repo_units`, which reads `overlay.read_overlay` and keeps the
    units whose `trigger` holds, and rendered by `instruction_units.render_unit`, in overlay order. The rows
    at HEAD are looked at first, so a tree whose overlay holds no such row reads no sibling kit and gets ().
    A refused read or render, or no playbook kit to read the rows a role selects, is a RolesError naming it."""
    import sys
    text = read_head_text(root, "HEAD", OVERLAY_FILE)
    want = (ROLE_TAG + slot) if slot else None

    def test_scope(scope):
        return isinstance(scope, (list, tuple)) and any(
            isinstance(s, str) and (s == want if want else s.startswith(ROLE_TAG)) for s in scope)

    try:
        rows = (tomllib.loads(text).get("unit") if text else None) or []
    except tomllib.TOMLDecodeError:
        rows = None   # the overlay reader below names the fault
    if isinstance(rows, list) and not any(isinstance(r, dict) and r.get("level") == ROLE_UNIT_LEVEL
                                          and test_scope(r.get("scope")) for r in rows):
        return ()
    try:
        kit = str(resolve_kit_dir("playbook", "render_playbook.py", kit_dir))
    except LookupError as exc:
        raise RolesError("%s: holds a level-%d unit selecting a role, and no playbook kit reads it: %s"
                         % (OVERLAY_FILE, ROLE_UNIT_LEVEL, exc)) from None
    if kit not in sys.path:
        sys.path.insert(0, kit)
    import render_playbook  # the playbook kit's renderer, found above
    try:
        units = render_playbook.read_repo_units(pathlib.Path(root))
        import overlay
        reader = overlay.derive_policy_reader(root)
        return tuple((u, overlay.iu.render_unit(u, reader, root).replace("\r\n", "\n").strip("\n"))
                     for u in units if u.level == ROLE_UNIT_LEVEL and test_scope(u.scope))
    except (render_playbook.Refusal, ValueError) as exc:   # the read's refusal, a UnitRowError, OverlayRefused
        raise RolesError("%s: the overlay's role units are refused: %s" % (OVERLAY_FILE, exc)) from None


def render_static_block(kit_dir, slot, role, memory_root, charter, notes, gates=(), missing=(), rows=None,
                        charter_doc=""):
    """The role's static block, the one composition of the bytes an agent file carries after its front
    matter (TOOL-dBoundRoles-15 S1): `render_role`'s output with `gates`, the legs its `## Ceiling`
    names, then each of `missing`, the `Missing required unit:` lines the load-set check printed for it;
    and `## Charter` with `render_charter_blocks`' blocks for `role`'s `rules`. With `rows`, the document
    registry, the charter comes first, in the envelope of the charter's row at `charter_doc`, then the
    role, all in the agent file's own envelope (PLAY-dOrderedCharter-5 S1); with `rows` None the role
    comes first and the charter after it, unenveloped. A charter that yields no block renders no
    `## Charter`. R5 measures these bytes against the role's `budget`, so the charter is inside its
    ceiling."""
    body = render_role(kit_dir, slot, memory_root, gates)
    if missing:
        body += "\n" + "\n".join(missing) + "\n"
    blocks = render_charter_blocks(charter, role["path"].as_posix(), role["keys"].get("rules", ""), notes)
    if blocks and rows is None:
        body += "\n## Charter\n\n" + blocks
    elif blocks:
        blocks = "## Charter\n\n" + blocks
        row = read_envelope_row(rows, charter_doc, memory_root)
        if row is not None:
            blocks = render_envelope(charter_doc, row[0], row[1], blocks)
        body = blocks + "\n" + body
    # PLAY-dOrderedCharter-3 S4: the body after the front matter in its envelope, where a registry row names it
    rel = "%s/%s.md" % (AGENTS_REL, slot)
    row = read_envelope_row(rows, rel, memory_root)
    if row is not None:
        body = render_envelope(rel, row[0], row[1], body)
    return body


def derive_section_sha(section):
    """The first 12 lowercase hex digits of the SHA-256 of a section's bytes, CRLF folded to LF: a handoff
    marker's `role-sha` and `task-sha`, and the role index's `role-sha` (TOOL-dBoundRoles-6 S4)."""
    return hashlib.sha256(section.replace("\r\n", "\n").encode("utf-8")).hexdigest()[:12]


def derive_fact_key(form, ref, data, lines=None):
    """A handed fact's key (TOOL-dBoundRoles-13 S1), the one deriver. `form` is `blob`, `record` or `cmd`.
    `blob`: `blob:<ref>@<blob12>:<lo>-<hi>`, `ref` the file's repo-relative path, `data` its bytes or text,
    `lines` the excerpt's `(lo, hi)`, the whole file when None. `record`: `record:<ref>@<sha12>`, `ref` a
    repo-relative path or `card/<session id>`. `blob12` and `sha12` are the first 12 hex digits of the git
    blob id of `data` with CRLF folded to LF, so one fact keys one way on every checkout. `cmd`:
    `cmd:<argv12>:<out12>`, `ref` the argv list and `data` its output, each the first 12 hex digits of the
    SHA-256 of the argv joined by NUL and of the output's UTF-8 bytes."""
    raw = data.encode("utf-8") if isinstance(data, str) else bytes(data)
    if form == "cmd":
        argv = "\0".join(ref).encode("utf-8")
        return "cmd:%s:%s" % (hashlib.sha256(argv).hexdigest()[:12], hashlib.sha256(raw).hexdigest()[:12])
    raw = raw.replace(b"\r\n", b"\n")
    blob = hashlib.sha1(b"blob %d\0" % len(raw) + raw).hexdigest()[:12]
    if form == "record":
        return "record:%s@%s" % (ref, blob)
    if form != "blob":
        raise RolesError("derive_fact_key: the form '%s' is none of blob, record, cmd" % form)
    if lines is None:
        lines = (1, raw.count(b"\n") + (0 if raw.endswith(b"\n") or not raw else 1))
    return "blob:%s@%s:%d-%d" % (ref, blob, lines[0], lines[1])


def derive_fact_class(key, root):
    """A fact key's class by §4 "The classes" of TOOL-dBoundRoles-13, read off the key and its source's own
    bytes under `root`, never an agent's word: `decided` for `.governance/policy.toml`, the memory root's
    `DECISIONS.md` and a record whose status header tail carries `ratified <date>`; `claimed` for any other
    `record:` key, the card's included, and for a `cmd:` key over a typed `--input` argument; `witnessed`
    for any other `blob:` or `cmd:` key."""
    root = pathlib.Path(root)
    if key.startswith("cmd:"):
        typed = {"cmd:%s" % hashlib.sha256(("--input\0" + n).encode("utf-8")).hexdigest()[:12] for n in ARGUMENT_INPUTS}
        return "claimed" if key.rsplit(":", 1)[0] in typed else "witnessed"
    form, _, rest = key.partition(":")
    path = rest.rsplit("@", 1)[0]
    if form == "record" and path.startswith("card/"):
        return "claimed"
    conf = root / ".memory-tree.conf"
    memory_root = read_conf_key(conf, "MEMORY_ROOT") if conf.is_file() else None
    decided = path == ".governance/policy.toml" or (memory_root and path == "%s/DECISIONS.md" % memory_root)
    if not decided and (root / path).is_file():
        try:
            decided = bool(RATIFIED_RE.search(load_text(root / path)))
        except (RolesError, UnicodeDecodeError):
            decided = False
    return "decided" if decided else "witnessed" if form == "blob" else "claimed"


def render_fact_line(key, root):
    """`<!-- gov:fact key=<key> class=<class> -->`, the class `derive_fact_class`'s; a key `FACT_RE` cannot
    read back, a path holding whitespace say, raises RolesError naming it."""
    line = "<!-- gov:fact key=%s class=%s -->" % (key, derive_fact_class(key, root))
    if not FACT_RE.match(line):
        raise RolesError("the fact key %r does not read back through FACT_RE: a path holding whitespace "
                         "cannot be handed as a keyed fact" % key)
    return line


def check_anchors(text, handed):
    """One line per anchor span in text that is malformed or names no key in handed:
    'anchor `<span>` — malformed: <form expected>' or
    'anchor `<span>` — resolves to no fact this work order hands'. [] when every anchor resolves.
    An anchor is an `ANCHOR_RE` span on a line `read_unfenced_lines` yields, so a span inside a fenced block is
    never graded; `handed` is the set of keys the work order hands. Each span is named once, in first-seen order,
    and nothing is written (TOOL-dBoundRoles-24 S2)."""
    forms = {"blob": "blob:<path>@<12 hex>:<lo>-<hi>, lo <= hi, both positive integers",
             "record": "record:<id>@<12 hex>", "cmd": "cmd:<12 hex>:<12 hex>"}
    out, seen = [], set()
    for _n, line in read_unfenced_lines(text):
        for m in ANCHOR_RE.finditer(line or ""):
            span, key = m.group("span"), m.group("key")
            if span in seen:
                continue
            seen.add(span)
            if key and key.startswith("blob:"):
                lo, hi = key.rsplit(":", 1)[1].split("-")
                key = key if int(lo) <= int(hi) else None
            if key is None:
                out.append("anchor `%s` — malformed: %s" % (span, forms[span.split(":", 1)[0]]))
            elif key not in handed:
                out.append("anchor `%s` — resolves to no fact this work order hands" % span)
    return out


def extract_drive_lines(text, role):
    """The charter's drive lines whose role is `role`: each `- <stage> · <role> — ` line of the section the
    drive heading opens, as the playbook render composed it from the selected kits' `[[drive]]` rows
    (PLAY-dOrderedCharter-6), so a subagent holds its role's lines as the main session does."""
    out, inside = [], False
    for line in text.replace("\r\n", "\n").split("\n"):
        if line.startswith("## "):
            inside = line.startswith(DRIVE_HEAD)
        elif inside and DRIVE_LINE_RE.match(line) and DRIVE_LINE_RE.match(line).group(1) == role:
            out.append(line.rstrip())
    return out


def extract_work_order_parts(template):
    """`(role part, task part)` of the work-order template at `template`, split at its own `## Task` line,
    its blank edges trimmed; RolesError where it holds none."""
    text = load_text(template).strip("\n")
    task = WORK_ORDER_TASK_RE.search(text)
    if not task:
        raise RolesError("%s carries no '## Task' line" % pathlib.Path(template).as_posix())
    return text[:task.start()], text[task.start():]


def render_work_order_section(template, section, fills, wraps=None):
    """One part of the work-order template: each paragraph kept, a slot line its fill, a slot filled with
    nothing dropped. A part whose heading line `wraps` keys is ranked (PLAY-dOrderedCharter-5 S2): the fills
    of `WORK_ORDER_LEAD_SLOTS`, each already in its own lower-level envelope, open it, and the rest of its
    body follows inside the envelope `(doc, level, direction)` the key names, every envelope under the
    heading. A slot `fills` lacks raises RolesError naming `template`."""
    paras, lead = [], []
    wrap = (wraps or {}).get(section.strip("\n").split("\n", 1)[0])
    for para in section.strip("\n").split("\n\n"):
        slot = WORK_ORDER_SLOT_RE.fullmatch(para)
        if slot and slot.group(1) not in fills:
            raise RolesError("%s names the slot '%s', which no handoff fills"
                             % (pathlib.Path(template).as_posix(), slot.group(1)))
        (lead if slot and wrap and slot.group(1) in WORK_ORDER_LEAD_SLOTS else paras).append(
            fills[slot.group(1)] if slot else para)
    paras = [p for p in paras if p]
    if wrap:
        rest = [render_envelope(*wrap, "\n\n".join(paras[1:]))] if paras[1:] else []
        paras = paras[:1] + ["\n".join(p.rstrip("\n") for p in lead + rest if p)]
    return "\n\n".join(p for p in paras if p)


def render_role_section(kit_dir, slot, memory_root, charter_text, gates=(), rows=None):
    """The `## Role` section a handoff carries and the role index's `role-sha` hashes (TOOL-dBoundRoles-6 S4):
    the work-order template's role part under `kit_dir`, its slot filled with `render_role`'s output for
    `slot` and `gates`, its blank edges trimmed, then, where `charter_text` holds drive lines for the role,
    its `### Drive` block; with `rows`, the document registry, the body in the envelope of the agent file's
    row; then two newlines. One composition, so a handoff and its agent type agree exactly when both were
    rendered from one role text and one charter's drive lines."""
    template = pathlib.Path(kit_dir) / WORK_ORDER_REL
    role_part, _task = extract_work_order_parts(template)
    drive = extract_drive_lines(charter_text, slot)
    fill = render_role(kit_dir, slot, memory_root, gates).strip("\n") + (
        "\n\n### Drive\n\n" + "\n".join(drive) if drive else "")
    wraps = None
    agent = "%s/%s.md" % (AGENTS_REL, slot)
    row = read_envelope_row(rows, agent, memory_root)
    if row is not None:
        wraps = {"## Role": (agent, row[0], row[1])}
    return render_work_order_section(template, role_part, {"role": fill}, wraps) + "\n\n"


def read_role_budget(role):
    """The role's `budget`, the byte ceiling of its whole static block (TOOL-dBoundRoles-15 S2), as an
    integer; None where its front matter carries no `budget`. A value that is no decimal integer raises
    RolesError naming the role file and the value, R5."""
    value = role["keys"].get("budget")
    if not value:
        return None
    if not re.fullmatch(r"[0-9]+", value):
        raise RolesError("%s: R5 — budget '%s' is not a decimal byte count" % (role["path"].as_posix(), value))
    return int(value)


#: The two harness kinds (TOOL-dBoundRoles-15 §4): `static`, a backend that loads the role's charter from
#: a file at spawn, and `inline`, one that loads neither file, so only its task can carry the charter.
HARNESS_KINDS = ("static", "inline")
#: The `instructions.task-charter` values, the first the default a read of None takes.
TASK_CHARTER_VALUES = ("when-not-static", "always")
SINGLE_CARRY_LINE = ("instructions.task-charter is always, and %s loads the charter from %s: the charter "
                     "would reach the agent twice; set when-not-static")


def derive_harness_kind(keys, stand_in, charter_doc):
    """`(kind, carrier)` for a render of the role whose front-matter keys are `keys`: the harness kind and
    the file that loads its charter at spawn (TOOL-dBoundRoles-15 §4 "The harness kind"). An `agent`-true
    role spawned by its type is `static`, carried by `.claude/agents/<slot>.md`; a `--stand-in` render and
    any render of an `agent: false` role are the main loop's, `static` too, carried by the charter file,
    `charter_doc`, which Claude Code loads at level 0. Today's one adapter derives no `inline` route: the
    adapter that loads neither file says so in its own row, which this function reads once it exists."""
    if stand_in or keys.get("agent", "true") == "false":
        return "static", charter_doc
    return "static", "%s/%s.md" % (AGENTS_REL, keys.get("name", ""))


def check_single_carry(value, kind, role, carrier):
    """Whether the task carries the role's charter blocks (TOOL-dBoundRoles-15 S5), for the
    `instructions.task-charter` `value` (None reads as `when-not-static`) and the harness `kind`: only an
    `inline` kind does. `always` with a `static` kind raises RolesError naming the key, its value, the role
    and `carrier`, since the charter would then reach the agent twice."""
    value = value or TASK_CHARTER_VALUES[0]
    if value not in TASK_CHARTER_VALUES:
        raise RolesError("instructions.task-charter is %r, not one of %s" % (value, " ".join(TASK_CHARTER_VALUES)))
    if kind not in HARNESS_KINDS:
        raise RolesError("the harness kind %r is not one of %s" % (kind, " ".join(HARNESS_KINDS)))
    if kind == "static" and value == "always":
        raise RolesError(SINGLE_CARRY_LINE % (role, carrier))
    return kind == "inline"


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


def resolve_cited_paths(text, kit_dir, target_root, workflows):
    """`[(cite, rel)]` in first-seen order, one per distinct citation in text that this install
    holds, rel repo-relative. A citation of a `workflow`-driver harness of workflows resolves as
    `resolve_harness_path` does, with `here` at the tool root, so the Skill names a harness where the
    role index lists it (TOOL-dRenderedAnchor-2). Only a `workflow`-driver harness of the workflow table
    resolves through the role index's call: every other citation resolves with `here` at kit_dir, the
    call `derive_kit_paths` makes, so its probes stop at `<tool root>/<home>/` and a receipt row still
    places it (TOOL-dRenderedAnchor-3). A citation nothing holds, or held outside target_root, is
    not listed, and the caller's plain prefix substitution answers it; a path outside target_root
    could not be named repo-relative."""
    kit = pathlib.Path(kit_dir).absolute()
    root = pathlib.Path(target_root).absolute()
    harnesses = {m.groups() for m in (HARNESS_RE.match(h) for h in extract_workflow_harnesses(workflows)
                                      if isinstance(h, str)) if m}
    found, seen = [], set()
    for m in TOOL_ROOT_CITE_RE.finditer(text):
        if m.group(0) in seen:
            continue
        seen.add(m.group(0))
        here = kit.parent if m.groups() in harnesses else kit
        try:
            path = (resolve_kit_dir(m.group(1), m.group(2), here) / m.group(2)).relative_to(root)
        except (LookupError, ValueError):
            continue
        found.append((m.group(0), path.as_posix()))
    return found


# ------------------------------------------------------------------------- the composition (TOOL-dBoundRoles-20)
#: The repository's overlay, whose `[[role]]` and `[[workflow]]` rows the playbook kit's `compose` verb reads at
#: HEAD beside gov's; a repository row's `path` names it, since it has no role file.
OVERLAY_FILE = ".governance/instructions.toml"
#: A repository's own rules for a role (TOOL-dBoundRoles-19 S2): the overlay's units at the playbook kit's
#: ladder level `LEVELS[5]`, `role`, whose `scope` holds the role's tag `role.<slot>`.
ROLE_UNIT_LEVEL, ROLE_TAG = 5, "role."
#: The upgrade step that moves a house text file into the overlay, named by the checker's leftover-file note.
HOUSE_STEP = "roles/house-overlays-to-instructions"
#: The two row schemas beside this file, in the playbook kit's row grammar (S2): the role kind's, which
#: check_roles.py's R2 joins to `role-schema.toml` both ways, and the workflow kind's, which R6 joins to its keys.
ROLE_ROW_SCHEMA, WORKFLOW_ROW_SCHEMA = "role-row-schema.toml", "workflow-schema.toml"
#: A `role-schema.toml` shape read as a row of the composition: these three a `set`, every other a `scalar`.
SET_SHAPES = ("list", "entries", "class")
#: The keys a composed row carries beside its fields: its tag, where it was read, and an edge's own keys.
DERIVED_ROW_KEYS = ("tag", "origin", "source", "edges", "add", "remove")
#: The core layer (TOOL-dBoundRoles-1's `layer.roles`), whose roles' write class `check_core_fields` holds.
CORE_LAYER = "layer.roles"
#: Where a composed role or workflow entry comes from, the first gov's own and never written to a render.
ROW_ORIGINS = ("gov", "repository", "scenario")


def read_head_text(root, rev, rel):
    """The text of `rel` at the revision `rev` of the repository at `root`, through `git show`, its inherited
    `GIT_` variables unset; None where git names no such blob or no repository answers."""
    import os
    import subprocess
    try:
        p = subprocess.run(["git", "-C", str(root), "show", "%s:%s" % (rev, rel)], capture_output=True,
                           encoding="utf-8", errors="replace", stdin=subprocess.DEVNULL,
                           env={k: v for k, v in os.environ.items() if not k.startswith("GIT_")})
    except OSError:
        return None
    return p.stdout if p.returncode == 0 else None


def read_composition_demand(root, rev, kind):
    """Whether the composition of `kind` at `rev` can differ from gov's own rows (S3, the migration's
    "gov's rows compose to themselves with an empty overlay"): the overlay there holds a `[[<kind>]]` table,
    or the policy file there sets `instructions.exclude`, whose exclusions and the refusals they meet the
    verb alone reads. A file that does not parse demands the verb, which names the fault."""
    for rel, path in ((OVERLAY_FILE, (kind,)), (EFFORT_POLICY_FILE, ("instructions", "exclude"))):
        text = read_head_text(root, rev, rel)
        try:
            doc = tomllib.loads(text) if text else {}
        except tomllib.TOMLDecodeError:
            return True
        value = doc.get(".".join(path))
        for key in path if value is None else ():
            doc = doc.get(key) if isinstance(doc, dict) else None
        if value or (value is None and doc):
            return True
    return False


def read_kind_composition(root, rev, kind, rows, kit_dir):
    """`(exit, payload, lines)` of the playbook kit's `compose --kind <kind>` over `root` at `rev`, `rows` the
    activated rows handed to `--rows -` or None, run through the loop kit's `composition.read_composition_at`,
    the module found from `kit_dir` by `resolve_kit_dir` and imported inside this function, as
    `read_workflow_order` imports `loop_lib` (section 8 F10); exit 2 with one line where the loop kit does not
    resolve or import, or `rev` names no commit."""
    import sys
    try:
        kit = str(resolve_kit_dir("loop", "composition.py", kit_dir))
        if kit not in sys.path:
            sys.path.insert(0, kit)
        import composition  # the loop kit's caller of the compose verb, found above
    except (LookupError, ImportError) as exc:
        return 2, None, ["no loop kit runs the compose verb: %s" % exc]
    try:
        return composition.read_composition_at(root, rev, kind, rows)
    except ValueError as exc:
        return 2, None, [str(exc)]


def derive_repository_slot(tag):
    """The slot or name a composed row's tag names: `role.<slot>` its `<slot>`, and a repository row's
    `<word>.adopter.<name>` its `<name>`, the owner seat's `adopter` dropped."""
    parts = str(tag or "").split(".")
    return ".".join(parts[2:] if len(parts) > 2 and parts[1] == "adopter" else parts[1:])


def derive_row_keys(row, shapes):
    """A composed role row's front-matter keys RAW, as `parse_front_matter` keeps them: a `list` or `class`
    list joined by `, `, an `entries` list by `; `, a boolean `true` or `false`, any other value its text;
    `shapes` is `{key: role-schema.toml shape}`, and `DERIVED_ROW_KEYS` are left out."""
    out = {}
    for key, value in row.items():
        if key in DERIVED_ROW_KEYS:
            continue
        if isinstance(value, list):
            value = ("; " if shapes.get(key) == "entries" else ", ").join(str(v) for v in value)
        elif isinstance(value, bool):
            value = "true" if value else "false"
        out[key] = str(value)
    return out


def compose_roles(root, rev="HEAD", kit_dir=None, rows=None, gov=None):
    """`(roles, notes, refusals)` of the role kind composed at `rev` in the repository at `root` (S3): gov's
    roles, `gov` where the caller parsed them else `load_roles(kit_dir)`, and the overlay's `[[role]]` rows,
    `rows` the activated rows of the scenarios a build was placed under (S11, `scenario.read_activated_rows`'
    `kind.role` list) handed after them, composed by the playbook kit's `compose` verb through
    `read_kind_composition`. `roles` is `{slot: role}` in the shape `load_roles` returns, each role carrying
    `origin`, one of ROW_ORIGINS, and `tag`: an excluded gov role is absent, a patched or replaced one keeps
    its file's path and body with the composed keys, and a repository or scenario row's `path` is the overlay
    with `#<tag>` behind it, so a defect names the row, its body empty, its slot `derive_repository_slot`'s. Where the overlay holds no row of the kind, no
    exclusion is set and no rows are handed, gov's roles are returned and no verb runs. The verb answering
    unarmed returns gov's roles with one note naming it; refusing, gov's roles with its lines as `refusals`;
    composing, `check_core_fields`' refusals and one per repository slot a gov role already holds."""
    kit_dir = pathlib.Path(kit_dir or pathlib.Path(__file__).absolute().parent)
    own = load_roles(kit_dir) if gov is None else gov
    own = {slot: dict(r, origin=ROW_ORIGINS[0], tag="role." + slot) for slot, r in own.items()}
    if rows is None and not read_composition_demand(root, rev, "role"):
        return own, [], []
    code, payload, lines = read_kind_composition(root, rev, "role", rows, kit_dir)
    if code == 2:
        return own, ["the role composition is unarmed, so gov's roles are graded alone: %s" % " | ".join(lines)], []
    if code:
        return own, [], lines
    shapes = {r["key"]: r["shape"] for r in load_role_schema()}
    states, composed = payload.get("states") or {}, {r.get("tag"): r for r in payload.get("rows") or ()}
    out, refusals = {}, check_core_fields(payload, own)
    for slot, role in own.items():
        state = states.get(role["tag"], "unchanged")
        if state == "excluded":
            continue
        if state in ("amended", "replaced", "stale") and role["tag"] in composed:
            role = dict(role, keys=derive_row_keys(composed[role["tag"]], shapes))
        out[slot] = role
    handed = {r.get("tag") for r in rows or () if isinstance(r, dict)}
    for tag, row in composed.items():
        if row.get("origin") != ROW_ORIGINS[1] or tag in states:
            continue
        slot = derive_repository_slot(tag)
        if slot in out or slot in own:
            refusals.append("%s · %s · its slot %s is a gov role's · remedy: name the row role.adopter.<another "
                            "name>" % (OVERLAY_FILE, tag, slot))
            continue
        out[slot] = {"path": pathlib.Path(root) / ("%s#%s" % (OVERLAY_FILE, tag)), "body": "",
                     "keys": derive_row_keys(row, shapes), "origin": ROW_ORIGINS[2] if tag in handed else ROW_ORIGINS[1], "tag": tag}
    return out, [], refusals


def compose_workflows(root, rev="HEAD", kit_dir=None, rows=None, gov=None):
    """`(workflows, notes, refusals)` of the workflow kind composed at `rev` in the repository at `root` (S3),
    as `compose_roles` composes the role kind: gov's `[[workflow]]` entries, `gov` where the caller read them
    else `load_workflows(kit_dir)`, in table order, then each repository and scenario row. A gov entry
    excluded is absent and one patched or replaced is the composed row, keyed as the table keys it; a
    repository or scenario row carries `origin` and `tag` beside its keys, which a gov entry never does,
    so gov's own entries reach every reader byte for byte."""
    kit_dir = pathlib.Path(kit_dir or pathlib.Path(__file__).absolute().parent)
    own = list(load_workflows(kit_dir) if gov is None else gov)
    if rows is None and not read_composition_demand(root, rev, "workflow"):
        return own, [], []
    code, payload, lines = read_kind_composition(root, rev, "workflow", rows, kit_dir)
    if code == 2:
        return own, ["the workflow composition is unarmed, so gov's entries are graded alone: %s"
                     % " | ".join(lines)], []
    if code:
        return own, [], lines
    states, composed = payload.get("states") or {}, {r.get("tag"): r for r in payload.get("rows") or ()}
    out = []
    for entry in own:
        tag = "workflow.%s" % entry.get("name")
        state = states.get(tag, "unchanged")
        if state == "excluded":
            continue
        if state in ("amended", "replaced", "stale") and tag in composed:
            entry = {k: v for k, v in composed[tag].items() if k not in DERIVED_ROW_KEYS}
        out.append(entry)
    handed = {r.get("tag") for r in rows or () if isinstance(r, dict)}
    for tag, row in composed.items():
        if row.get("origin") == ROW_ORIGINS[1] and tag not in states:
            out.append(dict({k: v for k, v in row.items() if k not in DERIVED_ROW_KEYS},
                            origin=ROW_ORIGINS[2] if tag in handed else ROW_ORIGINS[1], tag=tag))
    return out, [], []


def check_core_fields(composition, gov):
    """The refusals the row grammar cannot state (S5, section 4 "Why a core role's write class needs its own
    check"), over the role `composition`, the compose verb's payload, and `gov`, `{slot: role}` of gov's own
    roles: each classified operation on `writes` of a gov role whose `layer` is CORE_LAYER, naming the role,
    the field and the overlay row; and each amends, supersedes or exclusion of a gov role whose `acts-as` is
    `cycle`, naming the role, `acts-as` and the source. Both read the role's own front matter at check
    time, so a `cycle` row a later build registers, the driver's, is fixed whole on arrival."""
    by_tag = {"role." + slot: r for slot, r in gov.items()}
    out = []
    for op in composition.get("operations") or ():
        role = by_tag.get(op.get("tag"))
        if op.get("field") == "writes" and role is not None and role["keys"].get("layer") == CORE_LAYER:
            out.append("%s · %s patches %s · field writes · a core role's write class is fixed, its layer %s · "
                       "remedy: drop the field from the row" % (OVERLAY_FILE, op.get("row"), op.get("tag"), CORE_LAYER))
    for tag, state in sorted((composition.get("states") or {}).items()):
        role = by_tag.get(tag)
        if role is None or role["keys"].get("acts-as") != "cycle" or state in ("unchanged", "orphaned"):
            continue
        how, source = {"excluded": ("excludes", "instructions.exclude"),
                       "replaced": ("supersedes", OVERLAY_FILE)}.get(state, ("amends", OVERLAY_FILE))
        out.append("%s · %s %s · acts-as cycle · a cycle role is fixed whole: no row amends, supersedes or "
                   "excludes it · remedy: drop the row" % (source, how, tag))
    return out


def derive_role_kind(slot, workflows):
    """The shape kind the role `slot` runs in (TOOL-dBoundRoles-16): the kind of the first stage row mapping
    it, its row's own else its entry's, in the entry its `workflow` names first and then in table order; else
    the `kind` of the first entry listing it; None where no entry lists it."""
    listed = [w for w in workflows if isinstance(w.get("roles"), list) and slot in w["roles"]]
    for w in listed:
        for row in derive_stage_rows(w, {}):
            if row.get("role") == slot and isinstance(row.get("kind"), str):
                return row["kind"]
    return next((w["kind"] for w in listed if isinstance(w.get("kind"), str)), None)


def check_actor_patch(item, role, original, workflows=()):
    """The refusals of one actor patch (S6, section 4 "The actor patch"; the main loop's decision of round two,
    its fourth point): `item` the composed item row whose actor a pinned `amends` patched to the repository
    role `role`, gov's row having named the role `original`, both roles as `compose_roles` returns them. A
    role-acted item carries no `returns` nor `allowance`, both its role's, so the template is `original`'s
    `return`, every row of which must be a row of `role`'s, the refusal arm both carry included; the ceiling
    is `original`'s `writes`, every class of which must be one of `role`'s; and the shape kind the item runs
    in, `derive_role_kind` of `original` over `workflows`, must be among `role`'s `shapes`. `[]` admits."""
    name, tag = role.get("tag") or role["keys"].get("name"), item.get("tag")
    out = []
    try:
        want = parse_return_template(original["keys"].get("return"))
        have = set(parse_return_template(role["keys"].get("return")))
    except RolesError as exc:
        want, have = [], set()
        out.append("role %s or item %s's original role carries a return that does not parse: %s" % (name, tag, exc))
    lacking = [n for n, t, o in want if (n, t, o) not in have]
    if lacking:
        out.append("role %s lacks item %s's return template, the rows %s of %s's return"
                   % (name, tag, ", ".join(lacking), original["keys"].get("name")))
    held = {c.strip() for c in role["keys"].get("writes", "").split(",") if c.strip()}
    for cls in [c.strip() for c in original["keys"].get("writes", "").split(",") if c.strip()]:
        if cls not in held:
            out.append("role %s's ceiling does not cover %s, the %s class item %s writes"
                       % (name, WRITE_FOLDERS.get(cls, cls), cls, tag))
    kind = derive_role_kind(original["keys"].get("name"), workflows)
    if kind is not None and kind not in parse_role_shapes(role["keys"].get("shapes")):
        out.append("role %s does not declare shape %s, the kind item %s runs in" % (name, kind, tag))
    return out


def check_role_acts(roles, items, workflows):
    """The matrix arm "every core item role acts in at least one core item" over the composition (S7; the main
    loop's decision of round two, its second point): one refusal per role of `roles`, composed, whose `acts-as`
    is `item` that no composed `[[item]]` of `items` names as its `actor` and no composed entry of `workflows`
    lists in its `roles`, gov's and the repository's alike. An actor `role:<slot>` or
    `role:adopter.<name>` reads as the slot `derive_repository_slot` derives."""
    acting = {s for w in workflows if isinstance(w.get("roles"), list) for s in w["roles"]}
    for row in items or ():
        actor = row.get("actor")
        if isinstance(actor, str) and actor.startswith("role:"):
            acting.add(derive_repository_slot("role." + actor[len("role:"):]))
    return ["role %s acts as item and acts in no composed item or workflow entry · remedy: list it in an entry's "
            "roles or name it an item's actor, or take it out with what left it idle" % slot
            for slot, r in roles.items() if r["keys"].get("acts-as") == "item" and slot not in acting]


def check_row_schema(kit_dir, name, keys):
    """S2, the field join (section 8 F9): the defects of the row schema `name` beside `kit_dir` against
    `keys`, `{key: "set" or "scalar"}` the kind's keys as the checker reads them: a `[[field]]` row naming no
    such key, a key no row names, and a row whose `shape` is not the key's. A file that does not read is one
    defect naming it."""
    path = pathlib.Path(kit_dir) / name
    try:
        with open(path, "rb") as fh:
            rows = tomllib.load(fh).get("field") or []
    except (OSError, tomllib.TOMLDecodeError) as exc:
        return ["%s does not read: %s" % (name, exc)]
    fields = {r.get("name"): r.get("shape") for r in rows if isinstance(r, dict)}
    out = ["%s field '%s' names no key the checker reads" % (name, f) for f in fields if f not in keys]
    out += ["%s holds no [[field]] row for the key '%s'" % (name, k) for k in keys if k not in fields]
    out += ["%s field '%s' is shaped %r, and its key reads as a %s" % (name, f, s, keys[f])
            for f, s in fields.items() if f in keys and s != keys[f]]
    return out
