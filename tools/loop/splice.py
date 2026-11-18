#!/usr/bin/env python3
"""splice.py — the `stage` kind: a repository's own stage, spliced between two adjacent gov stages by
pinned rows of the build's transition table (TOOL-dDeclaredLoop-25).

    python splice.py check [--selftest]
    python splice.py new <name> --after <step> --before <step> --actor <kind:name> --witness-by <text>
                     --owner <build> [--input <layer:what>]... [--allowance <text>] [--returns <record>]
    python splice.py --fixture --plant <case>

THE KIND. The kinds register's `kind.stage` row names this module's `new` as its factory, `stage-schema.toml`
beside this file as its row schema and the leg `loop splice check` as its gate. A repository's stage is a
`[[stage]]` table of its overlay, `.governance/instructions.toml`, tagged `step.adopter.<name>`: `after` and
`before` two adjacent gov steps A and B, `pin` the pin of the build row R it splits, and `exit` its exit
item, an `[[item]]` of the overlay tagged `item.adopter.<name>.<item>` whose `step` is the stage's tag. Gov's
steps are the definition's `[[step]]` table, which no factory writes, so every composed stage is the
repository's. Every read is the COMPOSITION at HEAD, the playbook kit's `overlay_rows.py compose`, run as a
subprocess through `loop_items.read_composition`, so this kit imports no playbook module.

THE EXPANSION. R is the build row whose `from` holds A's state, whose `item` is A's exit and whose `to` is
B's state. `derive_splice_rows` splits it into R1, from A's state on R's item and outcome into the stage's
state, and R2, from the stage's state on the stage's exit and R's outcome into B's state, each with R's
witness; the stage's state is `adopter-<name>`, derived by `derive_stage_state`, never typed. The spliced
table holds R1 and R2 and not R; every other row stays as shipped. R's pin is `derive_row_pin`: the
memory-tree kit's `derive_pin_hash` of R's canonical JSON.

`check_splices` is the frame check, in order: a stage tag succeeded by a change record is re-pointed
through its `Successor`, one line per re-point, a successor of `none` or of more than one tag refused;
then per stage the tag is `step.adopter.<name>`, its name no gov step's; no gov step is excluded; `after`
and `before` are gov steps, B's order A's plus one; at most one stage per pair; R exists and the pin is its
pin; the exit is an item of the stage whose outcome R's outcome routes to `transition`; each of the
stage's items holds under `check_witness_classes`; and `check_program` admits each `item.adopter.` item
only for a composed stage. Each refusal names the stage, the rule and the tag.

`check` composes the stage and item kinds at HEAD, reads `instructions.exclude` at HEAD through the
policy kit and the change records through the memory-tree kit, and prints `loop: splices composed · <n>
splice(s)`, each re-point and derived row, then each refusal as `loop: refused · ...`. Exit 0 green, 1 a
refusal, 2 unarmed: a kit that does not resolve, or a kind the composition does not answer.

`new` validates every argument and exits 2 before any write: a name that is not one tag segment, is
`adopter` or is a gov step's last segment, `--after` and `--before` that are not adjacent gov steps in
that order, a pair HEAD's composition already splices, or an actor flag owed or barred. It derives the
stage row, its pin from the working definition's R, and its exit item `item.adopter.<name>.exit` through
`loop_items.derive_new_item_row`, grades both in memory with `check_splices` and
`check_item_declarations`, and on green appends both tables to the overlay, prints the path and exits 0;
a refusal prints each line and exits 1, having written nothing. The register's factory verb runs it:
`python <prefix>/playbook/core.py new stage <name> ...`.

`--fixture --plant <case>` runs one case of `PLANTS`. Every case but `factory` is made in memory over this
tree's definition, the stage rows, items, exclusions and records passed to `check_splices` as data;
`factory` runs the register's factory in a scratch repository `loop_items.build_scratch_tree` builds, then
`check` and the item kind's check there, then the same factory again. `check --selftest` runs `check` over
the tree, then every case through `loop_lib.run_selftest_cases`.

`read_stage_members` and `write_stage_plant` are the step gate's `stage` class: every `[[step]]` tag of
the definition under a tree, read ungraded, and the first `[[step]]` table taken out of a clone's
definition, staged.

WHAT THIS DOES NOT CHECK: that the move engine reads the spliced table, which it does not yet; a repository
stage tag vanishing between two revisions; whether the stage's actor exists or its witness holds; where
breakpoints sit; and an `amends` or `supersedes` edge on a stage row, which the composition refuses, since
gov ships no stage row for its pin to match.
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from loop_items import (OVERLAY, build_scratch_tree, derive_definition_rel, derive_new_item_row,  # noqa: E402
                        read_composition, render_item_row, render_toml_value, run_factory, run_scratch_check)
from loop_lib import (DEFINITION, ROUTE_TRANSITION, SEG, STEP_TAGS, LoopError, check_item_declarations,  # noqa: E402
                      check_loop, check_program, check_witness_classes, read_definition, read_item_rows,
                      read_memory_tree, read_role_defaults, run_selftest_cases)
from loop_table import ROW_KEYS  # noqa: E402

SAY = "loop"
KIND = "stage"
ADOPTER = "adopter"
LEVEL = "build"
EXCLUDE_KEY = "instructions.exclude"
STAGE_TAG = re.compile(r"step\.%s\.(%s)" % (ADOPTER, SEG.pattern))
GOV_NAMES = frozenset(t.rpartition(".")[2] for t in STEP_TAGS)
#: The stage of the spec's data model, every in-memory case's base, and its exit item's fields.
FIXTURE_STAGE = {"tag": "step.adopter.security-review", "after": "step.test", "before": "step.deploy",
                 "exit": "item.adopter.security-review.exit"}
FIXTURE_EXIT = ("command:security-review", "the review record", "your-build", ["layer.flow:the verified tree"],
                "the review record", "record-kind.security-review")
FACTORY_ARGV = ("new", "stage", "demo", "--after", "step.test", "--before", "step.deploy", "--actor", "command:demo",
                "--input", "layer.flow:the demo input", "--allowance", "the demo record", "--returns",
                "record-kind.demo", "--witness-by", "the demo record", "--owner", "dDeclaredLoop")
PLANTS = {
    "between-test-deploy": "the data model's stage, between step.test and step.deploy",
    "removes": "instructions.exclude holding step.test, beside that stage",
    "reorders": "after step.deploy, before step.test",
    "replaces": "a stage tagged step.test",
    "before-plan": "no after, before step.plan",
    "after-deploy": "after step.deploy, no before",
    "non-adjacent": "after step.build, before step.deploy",
    "two-splices": "a second stage between step.test and step.deploy",
    "gov-rename": "after the old tag step.verify, a change record succeeding it by step.test",
    "stale-pin": "the stage's pin one hex digit off",
    "exit-elsewhere": "exit naming item.test.exit, a gov item of step.test",
    "exit-unwitnessed": "the exit item's witness taken out",
    "orphan-item": "an item.adopter.ghost.check beside no stage ghost",
    "factory": "core.py new stage demo in a scratch, committed, both checks over it, then the same new again",
}
#: Each selftest case: its name, its argv, its owed exit, and the opening and needle of the line it owes.
CASES = (("check", ["check"], 0, "loop: splices composed", "splice(s)"),
         ("between-test-deploy", None, 0, "loop: splice step.adopter.security-review",
          "R2 adopter-security-review → deploying"),
         ("removes", None, 1, "loop: refused", "the gov stage step.test is excluded"),
         ("reorders", None, 1, "loop: refused", "not adjacent in order"),
         ("replaces", None, 1, "loop: refused", "the stage step.test · tag"),
         ("before-plan", None, 1, "loop: refused", "no gov stage precedes it"),
         ("after-deploy", None, 1, "loop: refused", "no gov stage follows it"),
         ("non-adjacent", None, 1, "loop: refused", "step.build and step.deploy are not adjacent"),
         ("two-splices", None, 1, "loop: refused", "step.adopter.security-review and step.adopter.second-review"),
         ("gov-rename", None, 0, "loop: re-point step.adopter.security-review", "after step.verify → step.test"),
         ("gov-rename R1", ["--fixture", "--plant", "gov-rename"], 0, "loop: splice step.adopter.security-review",
          "R1 testing → adopter-security-review"),
         ("stale-pin", None, 1, "loop: refused", "is stale"),
         ("exit-elsewhere", None, 1, "loop: refused", "item.test.exit is no item of the stage"),
         ("exit-unwitnessed", None, 1, "loop: refused", "item.adopter.security-review.exit carries no witness"),
         ("orphan-item", None, 1, "loop: refused", "item.adopter.ghost.check"),
         ("factory", None, 0, "loop: fixture · new again", "step.test and step.deploy"))


# --------------------------------------------------------------------------------------- the expansion
def derive_stage_state(tag):
    """The state of the stage `tag`, `step.adopter.<name>`: `adopter-<name>`, derived and never typed."""
    return "%s-%s" % (ADOPTER, STAGE_TAG.fullmatch(tag).group(1))


def derive_row_pin(row):
    """The pin of one transition row: the memory-tree kit's `derive_pin_hash` of its canonical JSON."""
    read_memory_tree("design_lib.py")
    from design_lib import derive_pin_hash
    return derive_pin_hash(json.dumps(row, sort_keys=True, separators=(",", ":"), ensure_ascii=False))


def read_split_row(stage, data):
    """R, the build row of `data`'s `[[transition]]` table a stage splits: its `from` holds the state of the
    stage's `after`, its `item` is that step's exit and its `to` is the state of its `before`; None where
    either names no gov step or no row holds."""
    steps = {s.get("tag"): s for s in data.get("step", [])}
    a, b = steps.get(stage.get("after")), steps.get(stage.get("before"))
    if a is None or b is None:
        return None
    return next((r for r in data.get("transition", []) if r.get("level") == LEVEL and a.get("state") in (
        r.get("from") or []) and r.get("item") == a.get("exit") and r.get("to") == b.get("state")), None)


def derive_splice_rows(stage, data):
    """`(R1, R2)` of one stage over `data`, each carrying `loop_table.ROW_KEYS`: R1 from A's state on R's item
    and outcome into the stage's state, R2 from the stage's state on its exit and R's outcome into B's
    state, each with R's witness. LoopError where R does not hold."""
    r = read_split_row(stage, data)
    if r is None:
        raise LoopError(DEFINITION, "the stage %s splits no build row" % stage.get("tag"))
    steps = {s.get("tag"): s for s in data.get("step", [])}
    state = derive_stage_state(stage["tag"])
    r1 = (LEVEL, [steps[stage["after"]]["state"]], r["item"], r["outcome"], state, r["witness"])
    r2 = (LEVEL, [state], stage["exit"], r["outcome"], steps[stage["before"]]["state"], r["witness"])
    return dict(zip(ROW_KEYS, r1)), dict(zip(ROW_KEYS, r2))


def derive_spliced_table(stages, data):
    """`data`'s `[[transition]]` rows with each stage's R taken out and its R1 and R2 in R's place."""
    rows = list(data.get("transition", []))
    for stage in stages:
        r = read_split_row(stage, data)
        if r in rows:
            at = rows.index(r)
            rows[at:at + 1] = derive_splice_rows(stage, data)
    return rows


# ------------------------------------------------------------------------------------- the frame check
def resolve_stage_steps(stages, data, records):
    """`(stages, lines, refusals)`: each stage whose `after` or `before` names a tag the definition's steps
    do not hold, which a change record of `records` ends with a `Successor`, re-pointed record by record to
    a step tag the definition holds, one line per re-point; a successor of `none` or of more than one tag
    refused naming the record."""
    held = {s.get("tag") for s in data.get("step", [])}
    heirs = {r.get("Unit"): r for r in records if r.get("Unit") and r.get("Successor")}
    out, lines, refusals = [], [], []
    for stage in stages:
        stage = dict(stage)
        for key in ("after", "before"):
            old = tag = stage.get(key)
            seen = set()
            while isinstance(tag, str) and tag not in held and tag in heirs and tag not in seen:
                seen.add(tag)
                rec = heirs[tag]
                named = [h.strip().strip("`") for h in rec["Successor"].split(",")]
                if named == ["none"] or len(named) != 1:
                    refusals.append("the stage %s · successor · the record %s ends %s with %s, not one tag" % (
                        stage.get("tag"), rec.get("id"), tag, rec["Successor"]))
                    break
                tag = named[0]
            if tag != old and tag in held:
                stage[key] = tag
                lines.append("%s: re-point %s · %s %s → %s" % (SAY, stage.get("tag"), key, old, tag))
        out.append(stage)
    return out, lines, refusals


def check_splices(stages, data, exclude, records, items):
    """`(lines, refusals)` of the composed `stages` over `data`, a definition `check_loop` holds, by the frame
    rules in order: the tag `step.adopter.<name>`, its name no gov step's; no gov step in `exclude`; `after`
    and `before` adjacent gov steps in order; at most one stage per pair; R held and pinned; the exit an item
    of the stage routing R's outcome to `transition`; each stage item witnessed; and `check_program`
    admitting `items` with the composed stages. Each stage re-pointed through `records` first."""
    stages, lines, refusals = resolve_stage_steps(stages, data, records)
    steps = {s.get("tag"): s for s in data.get("step", [])}
    pairs, spliced = {}, []
    for stage in stages:
        tag = stage.get("tag")
        m = STAGE_TAG.fullmatch(tag) if isinstance(tag, str) else None
        if m is None or m.group(1) in GOV_NAMES:
            refusals.append("the stage %s · tag · holds no `%s` seat of one name of its own: a repository stage "
                            "is step.%s.<name>, its name no gov step's" % (tag, ADOPTER, ADOPTER))
            continue
        refusals += ["the stage %s · removes · the gov stage %s is excluded, and gov's five stages stay whole" % (
            tag, g) for g in steps if g in exclude]
        a, b = steps.get(stage.get("after")), steps.get(stage.get("before"))
        if a is None or b is None:
            key, side = ("after", "precedes") if a is None else ("before", "follows")
            refusals.append("the stage %s · adjacent · its %s %r is no gov step, so no gov stage %s it" % (
                tag, key, stage.get(key), side))
            continue
        if b.get("order") != a.get("order") + 1:
            refusals.append("the stage %s · adjacent · %s and %s are not adjacent in order: its before is the gov "
                            "step after its after" % (tag, a["tag"], b["tag"]))
            continue
        pairs.setdefault((a["tag"], b["tag"]), []).append(tag)
        r = read_split_row(stage, data)
        if r is None:
            refusals.append("the stage %s · pin · no build row from %s on %s into %s to split" % (
                tag, a.get("state"), a.get("exit"), b.get("state")))
            continue
        if stage.get("pin") != derive_row_pin(r):
            refusals.append("the stage %s · pin · %s is stale: the split row %s → %s on %s pins %s" % (
                tag, stage.get("pin"), a.get("state"), b.get("state"), r.get("item"), derive_row_pin(r)))
            continue
        exit_row = next((i for i in items if i.get("tag") == stage.get("exit")), {})
        if exit_row.get("step") != tag or r.get("outcome") not in (exit_row.get("outcomes") or []) or (
                exit_row.get("routes") or {}).get(r.get("outcome")) != ROUTE_TRANSITION:
            refusals.append("the stage %s · exit · %s is no item of the stage whose outcome %s routes to %s" % (
                tag, stage.get("exit"), r.get("outcome"), ROUTE_TRANSITION))
            continue
        unwitnessed = []
        for item in (i for i in items if i.get("step") == tag):
            try:
                check_witness_classes(dict(data, item=[item]), DEFINITION)
            except LoopError as e:
                unwitnessed.append("the stage %s · witness · %s" % (tag, e))
        refusals += unwitnessed
        if not unwitnessed:
            spliced.append(stage)
            for name, row in zip(("R1", "R2"), derive_splice_rows(stage, data)):
                lines.append("%s: splice %s · %s %s → %s · %s · %s" % (
                    SAY, tag, name, " ".join(row["from"]), row["to"], row["item"], row["outcome"]))
    refusals += ["the stages %s · one per pair · each splices between %s and %s, and at most one stage sits "
                 "between two gov steps" % (" and ".join(tags), a, b) for (a, b), tags in pairs.items()
                 if len(tags) > 1]
    try:
        check_program(dict(data, item=list(items)), DEFINITION, None,
                      [s.get("tag") for s in stages if isinstance(s.get("tag"), str)])
    except LoopError as e:
        refusals.append("program · %s" % e)
    table = derive_spliced_table(spliced, data)
    refusals += ["the stage %s · split · the row %s on %s survives the splice" % (s["tag"], r["to"], r["item"])
                 for s in spliced if (r := read_split_row(s, data)) in table]
    if spliced:
        lines.append("%s: splice table · %d build row(s) · %d split" % (
            SAY, sum(1 for r in table if r.get("level") == LEVEL), len(spliced)))
    return lines, refusals


# ------------------------------------------------------------------------------------------- the check
def read_splice_inputs(root):
    """`(exit, (stages, items, exclude, records), lines)` at `root`'s HEAD: the composed stage and item rows,
    `instructions.exclude` through the policy kit and the change records through the memory-tree kit; exit
    1 with a composition's or the policy's refusal, 2 with the unarmed lines where a kit does not resolve."""
    rows = {}
    for kind in (KIND, "item"):
        code, payload, said = read_composition(root, kind)
        if code:
            return code, None, said
        rows[kind] = [{k: v for k, v in r.items() if k not in ("origin", "source")} for r in payload["rows"]]
    try:
        from loop_parents import read_policy_kit
        policy, _guard = read_policy_kit()
        read_memory_tree("build_records.py")
        from build_records import read_changes
    except (LookupError, ImportError) as e:
        return 2, None, [str(e)]
    try:
        exclude = list(policy.resolve(EXCLUDE_KEY, str(root), "HEAD").value or [])
    except policy.Refusal as e:
        return 1, None, ["%s does not resolve at HEAD: %s" % (EXCLUDE_KEY, e)]
    return 0, (rows[KIND], rows["item"], exclude, read_changes(root)), []


def run_splice_check(stages, data, exclude, records, items):
    """`check_splices` over its data, printed: the count line, each re-point and derived row, each refusal.
    -> 0 green, 1 a refusal."""
    lines, refusals = check_splices(stages, data, exclude, records, items)
    print("%s: splices composed · %d splice(s)" % (SAY, len(stages)))
    for line in lines:
        print(line)
    for r in refusals:
        print("%s: refused · %s" % (SAY, r))
    return 1 if refusals else 0


def run_check():
    """The `check` verb over the tree this kit sits in: -> its exit."""
    root = next((d for d in (KIT, *KIT.parents) if (d / ".git").exists()), KIT)
    try:
        data, where = read_definition(KIT)
        check_loop(data, where)
    except LoopError as e:
        print("%s: refused · %s" % (SAY, e))
        return 1
    code, got, said = read_splice_inputs(root)
    if code:
        for line in said:
            print("%s: %s · %s" % (SAY, "splices unarmed" if code == 2 else "refused", line))
        return code
    stages, items, exclude, records = got
    return run_splice_check(stages, data, exclude, records, items)


# ---------------------------------------------------------------------------------------- the factory
def render_stage_row(row):
    """One `[[stage]]` table, its keys in the row's order."""
    return "[[stage]]\n" + "".join("%s = %s\n" % (k, render_toml_value(v)) for k, v in row.items())


def write_overlay_rows(root, text):
    """`text` appended to the overlay under `root`, made where absent, in the file's own line ending."""
    path = pathlib.Path(root) / OVERLAY
    path.parent.mkdir(parents=True, exist_ok=True)
    before = path.read_bytes() if path.is_file() else b""
    nl = b"\r\n" if b"\r\n" in before else b"\n"
    lead = (b"" if before.endswith(b"\n") else nl) + nl if before else b""
    path.write_bytes(before + lead + text.encode("utf-8").replace(b"\n", nl))
    return path


def run_new(argv):
    """The `new` verb: -> its exit."""
    ap = argparse.ArgumentParser(prog="splice.py new")
    ap.add_argument("name")
    for flag in ("--after", "--before", "--actor", "--witness-by", "--owner"):
        ap.add_argument(flag, required=True)
    ap.add_argument("--input", action="append")
    ap.add_argument("--allowance")
    ap.add_argument("--returns")
    a = ap.parse_args(argv)
    root = next((d for d in (KIT, *KIT.parents) if (d / ".git").exists()), KIT)
    try:
        data, where = read_definition(KIT)
        check_loop(data, where)
    except LoopError as e:
        print("%s: refused · %s" % (SAY, e))
        return 1
    tag, exit_tag = "step.%s.%s" % (ADOPTER, a.name), "item.%s.%s.exit" % (ADOPTER, a.name)
    steps = {s["tag"]: s for s in data["step"]}
    after, before = steps.get(a.after), steps.get(a.before)
    why = ("the name %r is not one tag segment of the shape %s" % (a.name, SEG.pattern)
           if not SEG.fullmatch(a.name) else "the name %s is the repository's seat, never a stage's" % ADOPTER
           if a.name == ADOPTER else "the name %s is a gov step's" % a.name if a.name in GOV_NAMES
           else "%s and %s are not adjacent gov steps in that order: %s" % (a.after, a.before, " ".join(STEP_TAGS))
           if after is None or before is None or before["order"] != after["order"] + 1 else None)
    if why:
        print("%s: refused · new %s · %s" % (SAY, tag, why))
        return 2
    code, got, said = read_splice_inputs(root)
    if code:
        for line in said:
            print("%s: %s · new %s · %s" % (SAY, "unarmed" if code == 2 else "refused", tag, line))
        return code
    stages, items, exclude, records = got
    holder = next((s.get("tag") for s in stages if (s.get("after"), s.get("before")) == (a.after, a.before)), None)
    r = read_split_row({"after": a.after, "before": a.before}, data)
    try:
        why = ("HEAD's composition holds the stage %s between %s and %s already" % (holder, a.after, a.before)
               if holder else "no build row from %s on %s into %s to split" % (
                   after["state"], after["exit"], before["state"]) if r is None else None)
        exit_row = None if why else derive_new_item_row(exit_tag, tag, a.actor, a.witness_by, a.owner,
                                                        {r["outcome"]: ROUTE_TRANSITION}, a.input, a.allowance,
                                                        a.returns)
    except ValueError as e:
        why = str(e)
    if why:
        print("%s: refused · new %s · %s" % (SAY, tag, why))
        return 2
    row = {"tag": tag, "after": a.after, "before": a.before, "pin": derive_row_pin(r), "exit": exit_tag}
    _lines, refusals = check_splices(stages + [row], data, exclude, records, items + [exit_row])
    refusals += check_item_declarations([exit_row], *read_role_defaults(KIT))[1]
    for why in refusals:
        print("%s: refused · new %s · %s" % (SAY, tag, why))
    if refusals:
        print("%s: new · %s refused, nothing written" % (SAY, tag))
        return 1
    path = write_overlay_rows(root, render_stage_row(row) + "\n" + render_item_row(exit_row))
    print("%s: new · appended %s and %s to %s" % (SAY, tag, exit_tag, path.as_posix()))
    return 0


# ------------------------------------------------------------------------------- the step gate's class
def read_stage_members(root):
    """The step gate's `stage` class: every `[[step]]` tag of the definition under `root`, read ungraded, as
    the `item` class reads its rows; an empty set where the tree holds no definition."""
    path = pathlib.Path(root) / derive_definition_rel()
    if not path.is_file():
        return set()
    data, _where = read_definition(path.parent)
    return {r["tag"] for r in data.get("step", []) if isinstance(r, dict) and isinstance(r.get("tag"), str)}


def write_stage_plant(clone):
    """The step gate's `stage` plant: the first `[[step]]` table taken out of the clone's definition, staged.
    -> its member id."""
    import tomllib
    rel = derive_definition_rel()
    path = pathlib.Path(clone) / rel
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^\[\[step\]\]\r?\n.*?(?=^\[|\Z)", text, re.M | re.S)
    if m is None:
        raise ValueError("the stage plant found no [[step]] table in %s" % rel)
    tag = tomllib.loads(m.group(0))["step"][0]["tag"]
    path.write_text(text[:m.start()] + text[m.end():], encoding="utf-8", newline="")
    subprocess.run(["git", "-C", str(clone), "add", "--", rel], check=True, capture_output=True)
    return "stage:%s" % tag


# ------------------------------------------------------------------------------------------ the plants
def run_scratch_splice(top):
    """`(exit, lines)` of the scratch's own `splice.py check`, run in `top` with the git leaks unset."""
    from loop_witness import read_clean_env
    script = top / pathlib.Path(derive_definition_rel()).parent / pathlib.Path(__file__).name
    p = subprocess.run([sys.executable, str(script), "check"], cwd=str(top), capture_output=True, text=True,
                       encoding="utf-8", errors="replace", env=read_clean_env(PYTHONIOENCODING="utf-8"), timeout=300)
    return p.returncode, [ln for ln in (p.stdout + p.stderr).splitlines() if ln.strip()]


def run_factory_case():
    """The `factory` case: the register's factory in a scratch, committed, `check` and the item kind's check
    there, then the same factory again, owed exit 2 naming the pair. -> the exit."""
    from loop_witness import remove_tree, run_fixture_git
    try:
        top, _sha, _pins = build_scratch_tree()
    except (LookupError, OSError, ValueError, subprocess.CalledProcessError) as exc:
        print("%s: fixture · UNARMED · the scratch could not be built: %s" % (SAY, exc))
        return 2
    bad = []

    def check_owed_step(step, got, owed, needles, line):
        print("%s: fixture · %s · exit %d · %s" % (SAY, step, got, line))
        if got != owed or not all(n in line for n in needles):
            bad.append("%s exited %d, owed %d and a line naming %s" % (step, got, owed, " and ".join(needles)))

    try:
        rc, line = run_factory(top, FACTORY_ARGV)
        check_owed_step("new", rc, 0, ("step.adopter.demo",), line)
        run_fixture_git(top, "add", "-A")
        run_fixture_git(top, "commit", "-q", "--allow-empty", "-m", "plant factory")
        rc, said = run_scratch_splice(top)
        for ln in said:
            print(ln)
        check_owed_step("check", rc, 0, ("splices composed · 1 splice(s)",), said[0] if said else "no output")
        rc, _payload, said = run_scratch_check(top)
        check_owed_step("item check", rc, 0, ("· 1 repository",),
                        next((ln for ln in said if "items composed" in ln), said[-1] if said else "no output"))
        rc, line = run_factory(top, FACTORY_ARGV)
        check_owed_step("new again", rc, 2, ("step.test", "step.deploy"), line)
    except (subprocess.CalledProcessError, OSError, LookupError) as exc:
        bad.append("the factory case could not run: %s" % exc)
    finally:
        remove_tree(top)
    for why in bad:
        print("%s: fixture · FAIL · %s" % (SAY, why))
    return 1 if bad else 0


def run_fixture(case):
    """One case of `PLANTS`, every case but `factory` made in memory over this tree's definition: -> its exit."""
    print("%s: fixture · plant %s · %s" % (SAY, case, PLANTS[case]))
    if case == "factory":
        return run_factory_case()
    try:
        data, where = read_definition(KIT)
        check_loop(data, where)
    except LoopError as e:
        print("%s: refused · %s" % (SAY, e))
        return 1
    stage = dict(FIXTURE_STAGE, pin=derive_row_pin(read_split_row(FIXTURE_STAGE, data)))
    actor, by, owner, inputs, allowance, returns = FIXTURE_EXIT
    exit_row = derive_new_item_row(stage["exit"], stage["tag"], actor, by, owner, {"recorded": ROUTE_TRANSITION},
                                   inputs, allowance, returns)
    stages, items, exclude, records = [stage], read_item_rows(data, where) + [exit_row], [], []
    if case == "removes":
        exclude = ["step.test"]
    elif case == "reorders":
        stage.update(after="step.deploy", before="step.test")
    elif case == "replaces":
        stage["tag"] = "step.test"
    elif case == "before-plan":
        del stage["after"]
        stage["before"] = "step.plan"
    elif case == "after-deploy":
        stage["after"] = "step.deploy"
        del stage["before"]
    elif case == "non-adjacent":
        stage.update(after="step.build", before="step.deploy")
    elif case == "two-splices":
        stages.append(dict(stage, tag="step.adopter.second-review", exit="item.adopter.second-review.exit"))
        items.append(dict(exit_row, tag="item.adopter.second-review.exit", step="step.adopter.second-review"))
    elif case == "gov-rename":
        stage["after"] = "step.verify"
        records = [{"id": "fixture-change-1", "Unit": "step.verify", "Successor": "step.test"}]
    elif case == "stale-pin":
        stage["pin"] = stage["pin"][:-1] + ("1" if stage["pin"][-1] == "0" else "0")
    elif case == "exit-elsewhere":
        stage["exit"] = "item.test.exit"
    elif case == "exit-unwitnessed":
        exit_row.pop("witness")
    elif case == "orphan-item":
        items.append(dict(exit_row, tag="item.adopter.ghost.check", step="step.adopter.ghost"))
    return run_splice_check(stages, data, exclude, records, items)


def run_selftest():
    """`check` over the tree, then every case: -> 0 when every case holds."""
    cases = [(name, argv or ["--fixture", "--plant", name], owed, opening, needle)
             for name, argv, owed, opening, needle in CASES]
    return run_selftest_cases(lambda argv: run_check() if argv == ["check"] else run_fixture(argv[2]), cases,
                              "%s: splice selftest" % SAY)


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if argv == ["check"]:
        return run_check()
    if argv == ["check", "--selftest"]:
        return run_selftest()
    if argv[:1] == ["new"]:
        return run_new(argv[1:])
    if len(argv) == 3 and argv[:2] == ["--fixture", "--plant"] and argv[2] in PLANTS:
        return run_fixture(argv[2])
    print("usage: python splice.py check [--selftest] | new <name> --after <step> --before <step> --actor <actor> "
          "--witness-by <text> --owner <build> [--input <layer:what>]... [--allowance <text>] [--returns <record>] "
          "| --fixture --plant <%s>" % "|".join(PLANTS), file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
