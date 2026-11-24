#!/usr/bin/env python3
"""scenario.py — the `scenario` kind: what kind of work a build is, the scenarios it was placed under, the
rows they activate, conflicts between them, and the switch at a step boundary (TOOL-dDeclaredLoop-27).

    python scenario.py select [--fact <name>=<value>]...
    python scenario.py check [--selftest]
    python scenario.py slots --build <slug> --rev <rev>
    python scenario.py --fixture --plant <case>

THE KIND. The kinds register's `kind.scenario` row names `factories.py scenario` as its factory,
`scenario-schema.toml` beside this file as its row schema and the leg `loop scenario fixtures` as its
gate. Gov's pack is `scenarios.toml` beside this file, the `scenario` namespace's source; a repository adds
its own `[[scenario]]` rows to its overlay, tagged scenario.adopter.<name>. Every read composes through the
playbook kit's `overlay_rows.py compose --kind scenario`, run as a subprocess by `loop_items.py`'s
`read_composition`, so this kit takes no edge to that kit. A row's `extends` names the scenario whose
`admits`, `entry`, `activates` and `then` it starts from, each key it sets standing in place of the
parent's whole (`derive_extended_rows`).

ADMISSION. `derive_admitted_scenarios(facts, rows, default)` answers every composed scenario whose
`admits` holds over the request's facts, each fact it names present with a listed value, in composition
order, gov's pack before the overlay; where none holds, `scenario.<default>`, the default the policy key
`flow.scenario-default` resolves to through the policy kit. A default naming no composed scenario, and a
value the policy kit refuses, are refused naming the key and the value. A predicate naming no fact never
holds.

THE COMPOSITION. `derive_activated_rows(placed, rows, mode)` merges the placed scenarios' `activates`,
per kind and per row tag, in declared order, each row carrying `source`, the last scenario that set it.
Two placed scenarios setting one field of one row to different values conflict: under `refuse`, the
default of `flow.scenario-conflict`, it raises `ScenarioConflict`, naming both scenarios, the row and the
field; under `declared-order` the later scenario wins and the settlement
`<row tag>:<field>:<winner>:<loser>` is answered beside the rows. `read_activated_rows(root, rev, placed)`
reads the scenario composition and the mode at the pin `rev`, and `position.py` hands the item rows on to
the item composition through `compose --rows -`.

THE PIN AND THE SWITCH. `loop_transition.py`'s writer calls `derive_move_scenarios(root, state, facts,
moves)` on every move: the scenarios are the admission over the move's facts where no earlier move of the
build carries `scenario`, and otherwise the newest such move's, each whose `then` names the step whose
state the move leaves giving way to the scenario that entry names (`derive_step_scenarios`). It answers
`(scenario, settled)` joined by `+`, or None where the scenario composition at HEAD answers unarmed.

THE SLOT (KICK-dKeptSession-20). A row's `preset`, a shipped preset's name, and `overrides`, a table
from a dotted policy key to its value, scope policy to the builds placed under it, inherited through
`extends` whole as every other field. `derive_slot_policy(placed, rows, mode)` composes the placed
scenarios' slots in declared order by `derive_activated_rows`' rule: two naming two presets, or setting
one override key to different values, raise `ScenarioConflict` under `refuse` and settle for the later
under `declared-order`. `slots --build <slug> --rev <rev>` reads the build's moves by `read_transitions`,
takes the scenarios the newest move carrying `scenario` names, reads the rows and `flow.scenario-conflict`
at `<rev>`, and prints the composed slot as one JSON object, `{"preset": {"name", "from"} or null,
"overrides": {<key>: {"value", "from"}}}`, or `null` for a build no move places or placed scenarios
carrying no slot; the policy kit's `read_revision` runs it for a read naming a build. Exit 0; 1 printing
`loop: refused · <why>` on a conflict under `refuse` or a refused read; 2 printing `loop: unarmed ·
<why>` where a kit does not resolve. `check_scenario_policy(rows, root)` runs, for each row carrying a
slot, the policy kit's `presets.py slot` and then `presets.py pairs` as subprocesses, so a slot setting
a key presets never touch, or breaking a pair rule, is refused at `check`.

`select` composes at HEAD and prints the placed tags on one line, space-separated, one `loop: settled ·
<entry>` line per settlement and the facts it read. `check` holds every rule of `check_scenarios` over
gov's pack as the working tree holds it and the repository's rows the composition answers at HEAD, then
composes each kind a scenario activates with its rows and holds each slot to `check_scenario_policy`; it
prints each refusal as `loop: refused · <scenario> · ...` and closes with `loop: scenarios composed · <n>
scenario(s) · <m> repository`. Exit 0 green; 1 a refusal, a conflict under `refuse` or a refused default;
2 printing `loop: unarmed · <why>` where the playbook or policy kit does not resolve, the kind is
unregistered, its schema is absent or HEAD holds no pack, and on a usage error. `check --selftest` runs `check` and `select --fact entry=patch` over
the tree, then every plant through `loop_lib.run_selftest_cases`.

`--fixture --plant <case>` runs `then-cycle` and `extends-cycle` over rows in memory; every other plant
runs in one scratch repository, `composition.py`'s `build_composition_base` with a second build `tFixTwo`,
reset per plant: it commits the plant's overlay rows and policy values, runs `select`, `check`, the
transition writer and the position engine of this tree as subprocesses there, and closes with
`loop: fixture · <case> · held` or `· MISSED <why>`. The cases are `PLANTS`.

WHAT THIS DOES NOT CHECK: that a fact a repository predicate names is one placement will supply; that the
first move's `to` is the placed scenarios' `entry`; that an activated row duplicates an overlay row's tag,
which the composition admits as two own rows; and the kind checks beyond the composition, the item kind's
`check_program` and the stage kind's `check_splices`, over a scenario's activated rows. A scenario no
predicate ever admits passes; `select` prints the facts it read. A slot is checked against the policy
file the working tree holds, so a file committed later can still break a pair a slot assigns.
"""
import json
import pathlib
import subprocess
import sys
import tomllib

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from composition import FX_BUILD, FX_UNIT, build_composition_base, read_composition_at  # noqa: E402
from loop_items import derive_definition_rel, derive_repo_item, read_composition, render_toml_value  # noqa: E402
from loop_lib import STEP_TAGS, LoopError, read_definition, resolve_kit_dir, run_selftest_cases, scan_cycles  # noqa: E402
from loop_parents import read_policy_kit  # noqa: E402
from loop_table import ENTRY, read_transition_rows  # noqa: E402
from loop_transition import read_transitions  # noqa: E402
from loop_witness import read_clean_env, read_git, remove_tree, run_fixture_git, write_fixture_files  # noqa: E402

SAY = "loop"
KIND = "scenario"
PACK = "scenarios.toml"
NONE = "none"
DEFAULT_KEY = "flow.scenario-default"
CONFLICT_KEY = "flow.scenario-conflict"
REFUSE = "refuse"
#: The schema's fields, each a scalar, in the order a row is written.
FIELDS = ("extends", "admits", "entry", "activates", "then", "preset", "overrides")
#: The fields `extends` hands from a parent to a row that does not set them.
INHERITED = ("admits", "entry", "activates", "then", "preset", "overrides")
#: The slot's two fields (KICK-dKeptSession-20): a row setting either carries a slot.
SLOT = ("preset", "overrides")
OVERLAY = ".governance/instructions.toml"
POLICY_FILE = ".governance/policy.toml"
FX_BUILD_2 = "tFixTwo"
HANDOVER = "GOV_POSITION_STATES"
OUT_OF_NONE = ("--from", ENTRY, "--item", "item.entry.claim", "--outcome", "claimed", "--fact", "disposition=new")
PLAN_EXIT = ("--from", "planning", "--item", "item.plan.exit", "--outcome", "recorded")
FARM = "item.test.adopter.device-farm"
PLANTS = {
    "two-builds": "scenario.adopter.mobile activating a device farm; tFix placed under entry=feature, tFixTwo under "
                  "entry=feature and platform=mobile, each position read",
    "drops-stage": "a scenario activating an item row that supersedes item.test.exit at its pin",
    "reorders-stage": "a scenario activating an amends of item.test.select setting step = step.deploy",
    "replaces-stage": "a scenario activating a kind.stage row tagged step.test",
    "conflict": "scenario.adopter.a and scenario.adopter.b each setting the device farm's actor, under refuse",
    "conflict-ordered": "the same two, flow.scenario-conflict = declared-order",
    "bad-default": "flow.scenario-default = nowhere, the policy file's one revision",
    "default-excluded": "flow.scenario-default = patch, instructions.exclude = [scenario.patch]",
    "then": "scenario.adopter.a giving way to scenario.adopter.b at step.plan; out of none, then planning -> designing",
    "mid-step-switch": "two-builds' tFixTwo, a second activated row committed, then planning -> designing",
    "derived-field": "one move out of none with --field scenario=scenario.patch",
    "then-cycle": "two rows whose then names each other, in memory",
    "extends-cycle": "two rows whose extends names each other, in memory",
    "slot-builds": "preset = standard; tFix under a strict slot, tFix2 under a velocity slot, each read by get "
                   "--build, then the file setting hooks.bypass",
    "slot-conflict": "slot-builds' two rows, tFix placed under both, under refuse, then declared-order",
    "slot-refused": "one slot overriding runtime.agents-in-flight, one under velocity overriding "
                    "review.design.round-count = 4, each refused by check",
}
STRICT_SLOT = "scenario.adopter.strict-slot"
VELOCITY_SLOT = "scenario.adopter.velocity-slot"


class ScenarioConflict(ValueError):
    """Two placed scenarios setting one field of one activated row to different values, under `refuse`."""


# ------------------------------------------------------------------------------------------ the rows
def derive_extended_rows(rows):
    """`rows` in order, each a copy whose `INHERITED` fields start from its parent's,
    read through the parent's own chain; a key the row sets stands in place of the parent's whole. A parent
    no row holds, or a chain that cycles, hands nothing further: `check_scenarios` refuses both."""
    by_tag = {r.get("tag"): r for r in rows}

    def derive_chain_row(row, seen):
        parent = by_tag.get(row.get("extends"))
        if parent is None or parent.get("tag") in seen:
            return dict(row)
        base = derive_chain_row(parent, seen | {parent.get("tag")})
        return {**{k: base[k] for k in INHERITED if k in base}, **row}
    return [derive_chain_row(r, {r.get("tag")}) for r in rows]


def check_default(default, rows):
    """`scenario.<default>` where a composed row holds it; ValueError naming the key and the value else."""
    tag = "%s.%s" % (KIND, default)
    if tag not in {r.get("tag") for r in rows}:
        raise ValueError("%s = %s names no composed scenario: %s is not in the scenario composition" % (
            DEFAULT_KEY, default, tag))
    return tag


def derive_admitted_scenarios(facts, rows, default):
    """The tags of every row of `rows` whose `admits` holds over `facts`, in composition order; `[the
    default's tag]` where none holds. ValueError where `default` names no composed scenario."""
    fallback = check_default(default, rows)
    out = []
    for row in rows:
        admits = row.get("admits")
        if isinstance(admits, dict) and admits and all(
                k in facts and isinstance(vals, list) and facts[k] in vals for k, vals in admits.items()):
            out.append(row["tag"])
    return out or [fallback]


def derive_activated_rows(placed, rows, mode):
    """`({kind tag: [row]}, [settlement])` of the placed scenarios' `activates`, merged per kind and row tag
    in declared order, each row's `source` the last scenario that set it. ScenarioConflict under `refuse`
    where two set one field to different values; under `declared-order` the later wins and the settlement
    `<row tag>:<field>:<winner>:<loser>` is answered."""
    by_tag = {r.get("tag"): r for r in rows}
    merged, setter, settled = {}, {}, []
    for scen in placed:
        for kind, krows in (by_tag.get(scen, {}).get("activates") or {}).items():
            into = merged.setdefault(kind, {})
            for row in krows if isinstance(krows, list) else []:
                tag = row.get("tag")
                if tag not in into:
                    into[tag] = {**row, "source": scen}
                    setter[(kind, tag)] = {f: scen for f in row}
                    continue
                held = into[tag]
                for field, value in row.items():
                    if field in ("tag", "source"):
                        continue
                    if field in held and held[field] != value:
                        loser = setter[(kind, tag)][field]
                        if mode == REFUSE:
                            raise ScenarioConflict(
                                "%s and %s each activate %s and set its %s to different values, and %s = refuse" % (
                                    loser, scen, tag, field, CONFLICT_KEY))
                        settled.append("%s:%s:%s:%s" % (tag, field, scen, loser))
                    held[field] = value
                    setter[(kind, tag)][field] = scen
                held["source"] = scen
    return {k: list(v.values()) for k, v in merged.items()}, settled


def derive_slot_policy(placed, rows, mode):
    """`{"preset": {"name", "from"} or None, "overrides": {<key>: {"value", "from"}}}` of the placed
    scenarios' slots, composed in declared order, each `from` the last scenario that set it; None where no
    placed row carries a slot. Two naming two presets, or setting one override key to different values,
    raise ScenarioConflict under `refuse`, naming both and the field; under `declared-order` the later wins,
    the rule `derive_activated_rows` holds an activated row's fields to."""
    by_tag = {r.get("tag"): r for r in rows}
    preset, overrides, slotted = None, {}, False
    for scen in placed:
        row = by_tag.get(scen, {})
        if not any(f in row for f in SLOT):
            continue
        slotted = True
        name = row.get("preset")
        if name is not None:
            if preset is not None and preset["name"] != name and mode == REFUSE:
                raise ScenarioConflict("%s and %s each set the slot's preset to different values, %s and %s, and %s "
                                       "= refuse" % (preset["from"], scen, preset["name"], name, CONFLICT_KEY))
            preset = {"name": name, "from": scen}
        for key, value in (row.get("overrides") or {}).items() if isinstance(row.get("overrides"), dict) else ():
            held = overrides.get(key)
            if held is not None and held["value"] != value and mode == REFUSE:
                raise ScenarioConflict("%s and %s each set the slot's override %s to different values, and %s = "
                                       "refuse" % (held["from"], scen, key, CONFLICT_KEY))
            overrides[key] = {"value": value, "from": scen}
    return {"preset": preset, "overrides": overrides} if slotted else None


def derive_step_scenarios(placed, step, rows):
    """`placed` at the exit of `step`: each scenario whose `then` names `step` gives way to the scenario that
    entry names, the rest kept in order, no tag twice. ValueError naming a placed tag no row holds."""
    by_tag = {r.get("tag"): r for r in rows}
    out = []
    for tag in placed:
        if tag not in by_tag:
            raise ValueError("the build's scenario %s is in no composed row" % tag)
        heir = next((e.get("scenario") for e in by_tag[tag].get("then") or []
                     if isinstance(e, dict) and step is not None and e.get("at") == step), None)
        nxt = heir or tag
        if nxt not in out:
            out.append(nxt)
    return out


# ------------------------------------------------------------------------------------------ the reads
def read_scenario_policy(root, key, rev):
    """The value `key` resolves to at `rev` through the policy kit; ValueError naming the key and the
    policy kit's reason where it refuses, LookupError where the kit does not resolve."""
    policy, _guard = read_policy_kit()
    try:
        return policy.resolve(key, str(root), rev).value
    except policy.Refusal as e:
        raise ValueError("%s is refused by the policy kit: %s" % (key, getattr(e, "why", e))) from None


def read_scenario_rows(root, rev=None):
    """The composed scenario rows of `root` at HEAD, or at `rev`, extended: None where the composition is
    unarmed; ValueError naming its first line where it refuses."""
    rc, payload, lines = (read_composition(root, KIND) if rev is None else read_composition_at(root, rev, kind=KIND))
    if rc == 2:
        return None
    if rc != 0:
        raise ValueError("the scenario composition does not read: %s" % (lines[0] if lines else "exit %d" % rc))
    return derive_extended_rows(payload["rows"])


def read_activated_rows(root, rev, placed):
    """`{kind tag: [row]}` the scenarios `placed` activate, read at the pin `rev`: the scenario composition
    and `flow.scenario-conflict` both at `rev`; `{}` where the composition is unarmed there."""
    rows = read_scenario_rows(root, rev)
    if rows is None:
        return {}
    return derive_activated_rows(placed, rows, read_scenario_policy(root, CONFLICT_KEY, rev))[0]


def derive_move_scenarios(root, state, facts, moves):
    """`(scenario, settled)` of the move out of `state` the transition writer records, `moves` the build's
    moves newest first, each value joined by `+`; None where the scenario composition at HEAD is unarmed.
    ValueError on a refused composition, default or policy value and on a conflict under `refuse`."""
    rows = read_scenario_rows(root)
    if rows is None:
        return None
    held = next((m["scenario"] for m in moves if m.get("scenario")), None)
    if held is None:
        placed = derive_admitted_scenarios(facts, rows, read_scenario_policy(root, DEFAULT_KEY, "HEAD"))
    else:
        data, _where = read_definition(KIT)
        step = next((s.get("tag") for s in data.get("step", []) if s.get("state") == state), None)
        placed = derive_step_scenarios(held.split("+"), step, rows)
    settled = derive_activated_rows(placed, rows, read_scenario_policy(root, CONFLICT_KEY, "HEAD"))[1]
    return "+".join(placed), "+".join(settled)


# ------------------------------------------------------------------------------------------ the check
def check_scenarios(rows, data, kinds):
    """One refusal per rule of the spec's section 4 a row of `rows`, the composed scenarios, breaks, each
    `<scenario> · <why>`; `data` the loop definition and `kinds` the kind tags a scenario may activate."""
    tags = {r.get("tag") for r in rows}
    tables = read_transition_rows(data, "the definition")
    states = {s.get("tag"): s.get("state") for s in data.get("step", [])}
    entered = {r.get("to") for r in tables["transition"] if r.get("level") == "build" and ENTRY in (r.get("from") or [])}
    out = []
    for raw, row in zip(rows, derive_extended_rows(rows)):
        tag = str(raw.get("tag"))
        said = []
        if not tag.startswith(KIND + "."):
            said.append("the tag does not open %s." % KIND)
        for key in raw:
            if key not in ("tag", "origin", "source", *FIELDS):
                said.append("key %s is no field the scenario schema declares" % key)
        if raw.get("extends") != NONE and raw.get("extends") not in tags:
            said.append("extends %s is neither none nor a composed scenario's tag" % raw.get("extends"))
        admits = row.get("admits")
        if not isinstance(admits, dict):
            said.append("admits %r is no table from a fact to its admitting values" % (admits,))
        else:
            for fact, vals in admits.items():
                if not (isinstance(vals, list) and vals and all(isinstance(v, str) and v for v in vals)):
                    said.append("admits fact %s holds %r, no non-empty list of values" % (fact, vals))
        entry = row.get("entry")
        if entry not in STEP_TAGS:
            said.append("entry %s is no gov step" % entry)
        elif states.get(entry) not in entered:
            said.append("entry %s · its state %s is entered by no build row out of %s" % (entry, states.get(entry), ENTRY))
        acts = row.get("activates")
        if not isinstance(acts, dict):
            said.append("activates %r is no table from a kind tag to its rows" % (acts,))
        else:
            for kind, krows in acts.items():
                if kind not in kinds:
                    said.append("activates kind %s, which is no kind the register lists with a schema but kind.%s" % (
                        kind, KIND))
                elif not (isinstance(krows, list) and all(isinstance(r, dict) and isinstance(r.get("tag"), str)
                                                          for r in krows)):
                    said.append("activates kind %s with no list of rows each carrying a string tag" % kind)
        then = row.get("then")
        if not isinstance(then, list):
            said.append("then %r is no list of { at, scenario } entries" % (then,))
        else:
            for e in then:
                if not (isinstance(e, dict) and e.get("at") in STEP_TAGS and e.get("scenario") in tags):
                    said.append("then entry %r · its at is no gov step or its scenario no composed scenario's tag" % (e,))
        out += ["%s · %s" % (tag, why) for why in said]
    for label, edges in (("extends", {r.get("tag"): [r.get("extends")] for r in rows}),
                         ("then", {r.get("tag"): [e.get("scenario") for e in r.get("then") or [] if isinstance(e, dict)]
                                   for r in derive_extended_rows(rows) if isinstance(r.get("then"), list)})):
        edges = {k: [v for v in vs if isinstance(v, str)] for k, vs in edges.items() if isinstance(k, str)}
        for cycle in scan_cycles(edges):
            out.append("%s · the %s edges cycle: %s" % (cycle[0], label, " -> ".join(cycle + cycle[:1])))
    return out


def run_presets_verb(script, argv, feed, root):
    """`(exit, stdout, lines)` of the policy kit's `presets.py` at `script` run with `argv` in `root`, `feed`
    on its stdin and the git variables `read_clean_env` drops unset."""
    p = subprocess.run([sys.executable, str(script), *argv], input=feed, cwd=str(root), capture_output=True,
                       text=True, encoding="utf-8", errors="replace", env=read_clean_env(PYTHONIOENCODING="utf-8"),
                       timeout=600)
    return p.returncode, p.stdout, [ln for ln in (p.stdout + p.stderr).replace("\r", "").splitlines() if ln.strip()]


def check_scenario_policy(rows, root):
    """One refusal per slot of `rows`, the extended scenario rows, that the policy kit refuses, each
    `<scenario> · <key> · <why>`: the slot through `presets.py slot --repo <root>`, then the assignment it
    prints through `presets.py pairs`, each a subprocess in `root`. A verb exiting other than 0 with no
    refusal line is one refusal naming the verb and its first line, never a pass. A row carrying no slot
    runs no verb; LookupError where the policy kit does not resolve for a row carrying one."""
    out, script, said = [], None, "presets: refused · "
    for row in rows:
        if not any(f in row for f in SLOT):
            continue
        if script is None:
            script = resolve_kit_dir("policy", "presets.py", KIT) / "presets.py"
        feed = json.dumps({"scenario": row.get("tag"), "preset": row.get("preset"),
                           "overrides": row.get("overrides", {})})
        for argv in (["slot", "--repo", str(root)], ["pairs"]):
            try:
                rc, stdout, lines = run_presets_verb(script, argv, feed, root)
            except (OSError, subprocess.TimeoutExpired) as exc:
                rc, stdout, lines = -1, "", ["did not run: %s" % exc]
            refused = [ln[len(said):] for ln in lines if ln.startswith(said)]
            if rc == 0:
                feed = stdout
                continue
            out += refused if rc == 1 and refused else ["%s · presets.py %s exited %d: %s" % (
                row.get("tag"), argv[0], rc, lines[0] if lines else "(no output)")]
            break
    return out


def read_activatable_kinds(root):
    """The kind tags a scenario may activate: every kind the register under `root` lists with a schema,
    `pins.read_row_kinds` of the playbook kit, but `kind.scenario`. LookupError where that kit does not
    resolve."""
    found = resolve_kit_dir("playbook", "pins.py", KIT)
    if str(found) not in sys.path:
        sys.path.append(str(found))
    import pins
    return {r.get("tag") for r in pins.read_row_kinds(root)} - {"kind.%s" % KIND}


def read_repo_root():
    """The top of the work tree at the working directory, or the working directory itself."""
    rc, top = read_git(".", "rev-parse", "--show-toplevel")
    return pathlib.Path(top if rc == 0 and top else ".").absolute()


def run_check():
    """`check` over the repository at the working directory: -> its exit."""
    root = read_repo_root()
    rc, payload, lines = read_composition(root, KIND)
    if rc == 2:
        print("%s: unarmed · %s" % (SAY, " | ".join(lines) or "the scenario composition answers unarmed"))
        return 2
    if rc != 0:
        for line in lines:
            print("%s: refused · the scenario composition · %s" % (SAY, line))
        return 1
    try:
        kinds = read_activatable_kinds(root)
        pack = root / pathlib.Path(derive_definition_rel()).parent / PACK
        gov = [{**r, "origin": KIND} for r in tomllib.loads(pack.read_text(encoding="utf-8")).get(KIND, [])]
        data, _where = read_definition(KIT)
    except LookupError as e:
        print("%s: unarmed · %s" % (SAY, e))
        return 2
    except (OSError, tomllib.TOMLDecodeError, LoopError) as e:
        print("%s: refused · %s does not read: %s" % (SAY, PACK, e))
        return 1
    repo = [r for r in payload["rows"] if r.get("origin") == "repository"]
    rows = gov + repo
    refusals = check_scenarios(rows, data, kinds)
    for row in derive_extended_rows(rows):
        for kind, krows in (row.get("activates") or {}).items() if isinstance(row.get("activates"), dict) else ():
            if kind not in kinds or not isinstance(krows, list):
                continue
            got, _p, said = read_composition(root, kind.partition(".")[2], [{**r, "source": row["tag"]} for r in krows])
            refusals += ["%s · %s · %s" % (row["tag"], kind, ln) for ln in (said if got != 0 else [])]
    try:
        refusals += check_scenario_policy(derive_extended_rows(rows), root)
    except LookupError as e:
        print("%s: unarmed · %s" % (SAY, e))
        return 2
    for why in refusals:
        print("%s: refused · %s" % (SAY, why))
    print("%s: scenarios composed · %d scenario(s) · %d repository" % (SAY, len(rows), len(repo)))
    return 1 if refusals else 0


def run_select(facts):
    """`select` over the repository at the working directory, `facts` `{name: value}`: -> its exit."""
    root = read_repo_root()
    try:
        rows = read_scenario_rows(root)
        if rows is None:
            print("%s: unarmed · the scenario composition at HEAD answers unarmed" % SAY)
            return 2
        placed = derive_admitted_scenarios(facts, rows, read_scenario_policy(root, DEFAULT_KEY, "HEAD"))
        settled = derive_activated_rows(placed, rows, read_scenario_policy(root, CONFLICT_KEY, "HEAD"))[1]
    except LookupError as e:
        print("%s: unarmed · %s" % (SAY, e))
        return 2
    except ValueError as e:
        print("%s: refused · %s" % (SAY, e))
        return 1
    print(" ".join(placed))
    for entry in settled:
        print("%s: settled · %s" % (SAY, entry))
    print("%s: facts · %s" % (SAY, " ".join("%s=%s" % kv for kv in sorted(facts.items())) or "none"))
    return 0


def run_slots(build, rev):
    """`slots --build <build> --rev <rev>` over the repository at the working directory: the slot
    `derive_slot_policy` composes for the scenarios the build's newest move carrying `scenario` names, the
    rows and `flow.scenario-conflict` read at `rev`, printed as JSON, `null` where none: -> its exit."""
    root = read_repo_root()
    try:
        held = next((m["scenario"] for m in read_transitions(build, root) if m.get("scenario")), None)
        slot = None
        if held is not None:
            rows = read_scenario_rows(root, rev)
            if rows is None:
                print("%s: unarmed · the scenario composition at %s answers unarmed" % (SAY, rev))
                return 2
            slot = derive_slot_policy(held.split("+"), rows, read_scenario_policy(root, CONFLICT_KEY, rev))
    except LookupError as e:
        print("%s: unarmed · %s" % (SAY, e))
        return 2
    except (ValueError, OSError) as e:
        print("%s: refused · %s" % (SAY, e))
        return 1
    print(json.dumps(slot, sort_keys=True))
    return 0


# ------------------------------------------------------------------------------------------ the plants
def render_scenario_row(row):
    """One `[[scenario]]` table of an overlay, its keys in the schema's order."""
    return "[[scenario]]\n" + "".join("%s = %s\n" % (k, render_toml_value(row[k])) for k in ("tag", *FIELDS)
                                      if k in row)


def derive_plant_scenario(name, admits, activates=None, then=(), extends="scenario.feature"):
    """A repository scenario row of the plants, tagged at the adopter seat."""
    return {"tag": "%s.adopter.%s" % (KIND, name), "extends": extends, "admits": admits, "entry": "step.plan",
            "activates": activates or {}, "then": list(then)}


def derive_farm_row(actor="command:device-farm", name="device-farm"):
    """The plants' activated item: a device farm of the test step needing the floor item."""
    return {**derive_repo_item(name, ["item.test.verdict"], ["layer.flow:the verified tree"]), "actor": actor}


def build_scenario_base():
    """`(top, base sha, gov item pins)`: `build_composition_base`'s scratch with the build `tFixTwo` committed."""
    top, _sha = build_composition_base()
    try:
        write_fixture_files(top, {"memory/builds/%s/README.md" % FX_BUILD_2:
                                  "---\nslug: %s\nnode: a\nopened: 2026-01-01\nstreams: tooling\nroster: TOOL\n"
                                  "ids: TOOL-tFixTwo-1\n---\n\n# %s\n" % (FX_BUILD_2, FX_BUILD_2)})
        run_fixture_git(top, "add", "-A")
        run_fixture_git(top, "commit", "-qm", "the build %s" % FX_BUILD_2)
        rc, payload, lines = read_composition(top)
        if rc != 0:
            raise LookupError("the scratch's item composition exited %d: %s" % (rc, " | ".join(lines)[:300]))
        return top, run_fixture_git(top, "rev-parse", "HEAD"), payload["pins"]
    except BaseException:
        remove_tree(top)
        raise


def run_scratch_verb(top, script, *argv):
    """`(exit, lines)` of this kit's `script` run with `argv` in the scratch `top`."""
    env = read_clean_env(PYTHONIOENCODING="utf-8", **{HANDOVER: "unit\t%s\tREADY\n" % FX_UNIT})
    p = subprocess.run([sys.executable, str(KIT / script), *argv], cwd=str(top), capture_output=True, text=True,
                       encoding="utf-8", errors="replace", env=env, timeout=600)
    return p.returncode, [ln for ln in (p.stdout + p.stderr).splitlines() if ln.strip()]


def write_scenario_plant(top, case, pins):
    """`case`'s overlay rows and policy values in the scratch `top`, committed."""
    gov = {r["tag"]: r for r in read_definition(KIT)[0].get("item", [])}
    mobile = derive_plant_scenario("mobile", {"entry": ["feature"], "platform": ["mobile"]},
                                   {"kind.item": [derive_farm_row()]})
    pair = [derive_plant_scenario(n, {"entry": ["feature"]}, {"kind.item": [derive_farm_row("command:farm-%s" % n)]})
            for n in ("a", "b")]
    slots = [dict(derive_plant_scenario("strict-slot", {"entry": ["feature"], "precision": ["high"]}), preset="strict"),
             dict(derive_plant_scenario("velocity-slot", {"entry": ["feature"], "pace": ["fast"]}), preset="velocity")]
    overlay = {
        "two-builds": [mobile], "mid-step-switch": [mobile], "conflict": pair, "conflict-ordered": pair,
        "drops-stage": [derive_plant_scenario("drops", {"entry": ["never"]}, {"kind.item": [dict(
            {k: v for k, v in gov["item.test.exit"].items() if k != "tag"}, tag="item.test.adopter.exit-own",
            edges="supersedes=item.test.exit@%s" % pins["item.test.exit"])]})],
        "reorders-stage": [derive_plant_scenario("reorders", {"entry": ["never"]}, {"kind.item": [{
            "tag": "item.test.adopter.select-moved", "edges": "amends=item.test.select@%s" % pins["item.test.select"],
            "step": "step.deploy"}]})],
        "replaces-stage": [derive_plant_scenario("replaces", {"entry": ["never"]}, {"kind.stage": [{
            "tag": "step.test", "after": "step.build", "before": "step.deploy", "pin": "0123abcd",
            "exit": "item.test.exit"}]})],
        "then": [derive_plant_scenario("a", {"entry": ["feature"]}, then=[{"at": "step.plan",
                                                                           "scenario": "scenario.adopter.b"}]),
                 derive_plant_scenario("b", {"entry": ["never"]})],
        "slot-builds": slots, "slot-conflict": slots,
        "slot-refused": [dict(derive_plant_scenario("never-key", {"entry": ["never"]}),
                              overrides={"runtime.agents-in-flight": 9}),
                         dict(derive_plant_scenario("pair-break", {"entry": ["never"]}), preset="velocity",
                              overrides={"review.design.round-count": 4})],
    }.get(case)
    policy = {"slot-builds": 'preset = "standard"\n',
              "conflict-ordered": '[flow]\nscenario-conflict = "declared-order"\n',
              "bad-default": '[flow]\nscenario-default = "nowhere"\n',
              "default-excluded": '[flow]\nscenario-default = "patch"\n\n[instructions]\nexclude = ["scenario.patch"]\n'
              }.get(case)
    files = {OVERLAY: "\n".join(render_scenario_row(r) for r in overlay)} if overlay else {}
    if policy:
        files[POLICY_FILE] = policy
    write_fixture_files(top, files)
    run_fixture_git(top, "add", "-A")
    run_fixture_git(top, "commit", "-q", "--allow-empty", "-m", "plant %s" % case)
    return mobile


def run_scenario_plant(case, base):
    """One plant: in memory for the two cycle plants, else over the scratch `base`, `(top, sha, pins)`,
    reset to its commit first: -> 0 held, 1 missed."""
    print("%s: fixture · plant %s · %s" % (SAY, case, PLANTS[case]))
    misses = []

    def check_owed(label, held, said):
        print("%s: fixture · %s · %s" % (SAY, label, said))
        if not held:
            misses.append("%s: %s" % (label, said))

    def read_line(lines, needle):
        return next((ln for ln in lines if needle in ln), "no line naming %s" % needle)

    if case in ("then-cycle", "extends-cycle"):
        a, b = (derive_plant_scenario(n, {"entry": ["feature"]}) for n in ("a", "b"))
        if case == "then-cycle":
            a["then"] = [{"at": "step.plan", "scenario": b["tag"]}]
            b["then"] = [{"at": "step.design", "scenario": a["tag"]}]
        else:
            a["extends"], b["extends"] = b["tag"], a["tag"]
        data = read_definition(KIT)[0]
        said = [w for w in check_scenarios([a, b], data, {"kind.item"}) if "cycle" in w]
        check_owed("refused", any(a["tag"] in w and b["tag"] in w for w in said), " | ".join(said) or "no cycle refused")
        print("%s: fixture · %s · %s" % (SAY, case, "held" if not misses else "MISSED " + "; ".join(misses)))
        return 1 if misses else 0
    top, sha, pins = base
    run_fixture_git(top, "reset", "-q", "--hard", sha)
    run_fixture_git(top, "clean", "-qfdx")

    def write_move(build, tail, *facts, fields=()):
        argv = ["record", "--build", build, "--root", str(top), *tail, "--witness", "HEAD"]
        argv += [a for f in facts for a in ("--fact", f)] + [a for f in fields for a in ("--field", f)]
        return run_scratch_verb(top, "loop_transition.py", *argv)

    def read_trailer():
        return run_fixture_git(top, "log", "-1", "--format=%(trailers:key=Gov-Transition,valueonly)")

    def read_position(build):
        lines = run_scratch_verb(top, "position.py", build)[1]
        head = read_line(lines, "position — ")
        if "does not read" in head:
            misses.append("the position of %s did not read its composition: %s" % (build, head))
        return read_line(lines, "scenario=")

    try:
        mobile = write_scenario_plant(top, case, pins)
        if case in ("two-builds", "mid-step-switch"):
            if case == "two-builds":
                write_move(FX_BUILD, OUT_OF_NONE, "entry=feature")
            rc, lines = write_move(FX_BUILD_2, OUT_OF_NONE, "entry=feature", "platform=mobile")
            check_owed("record", rc == 0, read_line(lines, "recorded"))
            if case == "two-builds":
                got = read_position(FX_BUILD)
                check_owed("position %s" % FX_BUILD, "scenario=scenario.feature · 0 activated" in got, got)
            got = read_position(FX_BUILD_2)
            check_owed("position %s" % FX_BUILD_2,
                       "scenario=scenario.feature+scenario.adopter.mobile · 1 activated" in got, got)
            if case == "mid-step-switch":
                mobile["activates"]["kind.item"].append(derive_farm_row("command:device-lab", "device-lab"))
                write_fixture_files(top, {OVERLAY: render_scenario_row(mobile)})
                run_fixture_git(top, "commit", "-qam", "a second activated row")
                got = read_position(FX_BUILD_2)
                check_owed("before the move", "· 1 activated" in got, got)
                rc, lines = write_move(FX_BUILD_2, PLAN_EXIT)
                got = read_position(FX_BUILD_2)
                check_owed("after the move", rc == 0 and "· 2 activated" in got, got)
        elif case in ("drops-stage", "reorders-stage", "replaces-stage"):
            rc, lines = run_scratch_verb(top, "scenario.py", "check")
            owed = {"drops-stage": ("scenario.adopter.drops", "item.test.exit", "principle.p20"),
                    "reorders-stage": ("scenario.adopter.reorders", "field step", "principle.p20"),
                    "replaces-stage": ("scenario.adopter.replaces", "step.test", "owned")}[case]
            line = next((ln for ln in lines if ln.startswith("%s: refused" % SAY) and all(w in ln for w in owed)), None)
            check_owed("check", rc == 1 and line is not None, "exit %d · %s" % (rc, line or " | ".join(lines)[-300:]))
        elif case in ("conflict", "conflict-ordered"):
            rc, lines = run_scratch_verb(top, "scenario.py", "select", "--fact", "entry=feature")
            before = run_fixture_git(top, "rev-list", "--count", "HEAD")
            mrc, mlines = write_move(FX_BUILD, OUT_OF_NONE, "entry=feature")
            after = run_fixture_git(top, "rev-list", "--count", "HEAD")
            settlement = "%s:actor:scenario.adopter.b:scenario.adopter.a" % FARM
            if case == "conflict":
                line = read_line(lines, "refused")
                check_owed("select", rc == 1 and all(w in line for w in ("scenario.adopter.a", "scenario.adopter.b",
                                                                           FARM, "actor")), "exit %d · %s" % (rc, line))
                check_owed("record", mrc == 2 and before == after, "exit %d · commits %s -> %s · %s" % (
                    mrc, before, after, read_line(mlines, "unanswered")))
            else:
                check_owed("select", rc == 0 and "%s: settled · %s" % (SAY, settlement) in lines,
                           "exit %d · %s" % (rc, read_line(lines, "settled")))
                trailer = read_trailer()
                check_owed("record", mrc == 0 and "scenario-settled=%s" % settlement in trailer,
                           "exit %d · %s" % (mrc, trailer))
        elif case in ("bad-default", "default-excluded"):
            rc, lines = run_scratch_verb(top, "scenario.py", "select")
            value = "nowhere" if case == "bad-default" else "patch"
            line = read_line(lines, "refused")
            check_owed("select", rc == 1 and DEFAULT_KEY in line and value in line, "exit %d · %s" % (rc, line))
        elif case == "then":
            write_move(FX_BUILD, OUT_OF_NONE, "entry=feature")
            first = read_trailer()
            rc, _lines = write_move(FX_BUILD, PLAN_EXIT)
            second = read_trailer()
            check_owed("first trailer", "scenario=scenario.feature+scenario.adopter.a" in first, first)
            check_owed("second trailer", rc == 0 and "scenario=scenario.feature+scenario.adopter.b" in second, second)
        elif case == "derived-field":
            rc, lines = write_move(FX_BUILD, OUT_OF_NONE, "entry=feature", fields=("scenario=scenario.patch",))
            line = read_line(lines, "derived")
            check_owed("record", rc == 2 and "--field scenario is derived" in line, "exit %d · %s" % (rc, line))
        elif case in ("slot-builds", "slot-conflict"):
            policy_py = str(resolve_kit_dir("policy", "policy.py", KIT) / "policy.py")

            def read_policy_value(label, value, owed, key, *argv):
                rc, lines = run_scratch_verb(top, policy_py, "get", key, *argv)
                line = read_line(lines, "policy: ")
                check_owed(label, (rc == 0 and value in lines and all(w in line for w in owed)) if value else
                           (rc == 2 and all(w in line for w in owed)), "exit %d · %s" % (rc, " | ".join(lines)))

            def write_policy_file(text):
                write_fixture_files(top, {POLICY_FILE: text})
                run_fixture_git(top, "add", "-A")
                run_fixture_git(top, "commit", "-qm", "the policy file")

            moves = ([(FX_BUILD, "precision=high"), (FX_BUILD_2, "pace=fast")] if case == "slot-builds" else
                     [(FX_BUILD, "precision=high", "pace=fast")])
            for build, *facts in moves:
                rc, lines = write_move(build, OUT_OF_NONE, "entry=feature", *facts)
                check_owed("record %s" % build, rc == 0, read_line(lines, "recorded"))
            if case == "slot-builds":
                read_policy_value("get --build %s" % FX_BUILD, "refused", ("· preset ·", STRICT_SLOT),
                                  "hooks.bypass", "--build", FX_BUILD, "--explain")
                read_policy_value("get --build %s" % FX_BUILD_2, "allowed", ("· preset ·", VELOCITY_SLOT),
                                  "hooks.bypass", "--build", FX_BUILD_2, "--explain")
                read_policy_value("review.max-rounds --build %s" % FX_BUILD_2, "2", (), "review.max-rounds",
                                  "--build", FX_BUILD_2)
                read_policy_value("get, no build", "allowed", ("· preset · preset standard",), "hooks.bypass",
                                  "--explain")
                read_policy_value("get --build tNone", "allowed", ("· preset · preset standard",), "hooks.bypass",
                                  "--build", "tNone", "--explain")
                write_policy_file('preset = "standard"\n\n[hooks]\nbypass = "allowed"\n')
                read_policy_value("the file's own value", "allowed", ("· file ·",), "hooks.bypass", "--build",
                                  FX_BUILD, "--explain")
            else:
                read_policy_value("under refuse", None, ("refused", STRICT_SLOT, VELOCITY_SLOT, "preset"),
                                  "hooks.bypass", "--build", FX_BUILD)
                write_policy_file('[flow]\nscenario-conflict = "declared-order"\n')
                read_policy_value("under declared-order", "allowed", ("· preset ·", VELOCITY_SLOT), "hooks.bypass",
                                  "--build", FX_BUILD, "--explain")
        elif case == "slot-refused":
            rc, lines = run_scratch_verb(top, "scenario.py", "check")
            for label, owed in (("never", ("scenario.adopter.never-key", "runtime.agents-in-flight",
                                           "a key presets never touch")),
                                ("pair", ("scenario.adopter.pair-break", "review.max-rounds",
                                          "review.design.round-count"))):
                line = next((ln for ln in lines if ln.startswith("%s: refused" % SAY) and all(w in ln for w in owed)),
                            None)
                check_owed("check %s" % label, rc == 1 and line is not None,
                           "exit %d · %s" % (rc, line or " | ".join(lines)[-400:]))
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError, ValueError, LookupError, KeyError) as exc:
        misses.append("the plant could not run: %s %s" % (exc, (getattr(exc, "stderr", "") or "").strip()[:300]))
    print("%s: fixture · %s · %s" % (SAY, case, "held" if not misses else "MISSED " + "; ".join(misses)))
    return 1 if misses else 0


def run_selftest():
    """`check` and `select --fact entry=patch` over the tree, then every plant over one scratch base, reset
    per plant, through `run_selftest_cases`: -> 0 when every case holds."""
    try:
        base = build_scenario_base()
    except (LookupError, OSError, ValueError, subprocess.CalledProcessError) as exc:
        print("%s: scenario selftest · UNARMED · the scratch could not be built: %s" % (SAY, exc))
        return 2
    try:
        def run_case(argv):
            if argv[0] == "check":
                return run_check()
            if argv[0] == "select":
                return run_select({"entry": "patch"})
            return run_scenario_plant(argv[2], base)
        cases = [("check", ["check"], 0, "%s: scenarios composed" % SAY, "scenario(s)"),
                 ("select", ["select"], 0, "scenario.patch", "")]
        cases += [(c, ["--fixture", "--plant", c], 0, "%s: fixture · %s · held" % (SAY, c), "") for c in PLANTS]
        return run_selftest_cases(run_case, cases, "%s: scenario selftest" % SAY)
    finally:
        remove_tree(base[0])


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    usage = ("usage: python scenario.py select [--fact <name>=<value>]... | check [--selftest] | slots --build "
             "<slug> --rev <rev> | --fixture --plant <%s>" % "|".join(PLANTS))
    if argv == ["check", "--selftest"]:
        return run_selftest()
    if argv == ["check"]:
        return run_check()
    if len(argv) == 5 and argv[0] == "slots" and argv[1] == "--build" and argv[3] == "--rev" and argv[2] and argv[4]:
        return run_slots(argv[2], argv[4])
    if argv[:1] == ["select"] and len(argv) % 2 == 1 and all(f == "--fact" for f in argv[1::2]):
        facts = {}
        for text in argv[2::2]:
            name, eq, value = text.partition("=")
            if not (name and eq and value) or name in facts:
                print("%s: unarmed · --fact takes <name>=<value>, each name once, and %r is not" % (SAY, text))
                return 2
            facts[name] = value
        return run_select(facts)
    if len(argv) == 3 and argv[:2] == ["--fixture", "--plant"] and argv[2] in PLANTS:
        if argv[2] in ("then-cycle", "extends-cycle"):
            return run_scenario_plant(argv[2], None)
        try:
            base = build_scenario_base()
        except (LookupError, OSError, ValueError, subprocess.CalledProcessError) as exc:
            print("%s: fixture · UNARMED · the scratch could not be built: %s" % (SAY, exc))
            return 2
        try:
            return run_scenario_plant(argv[2], base)
        finally:
            remove_tree(base[0])
    print("%s: unarmed · %s" % (SAY, usage))
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
