#!/usr/bin/env python3
"""loop_items.py — the `item` kind: its factory, its check over the composed items, and its plants
(TOOL-dDeclaredLoop-24).

    python loop_items.py check [--selftest]
    python loop_items.py new <name> --step <step> --actor <actor> --witness-by <text> --owner <build>
                         [--input <layer:what>]... [--allowance <text>] [--returns <record>]
    python loop_items.py --fixture --plant <case>

THE KIND. The kinds register's `kind.item` row names this module's `new` as its factory, `item-schema.toml`
beside this file as its row schema and the leg `loop item kind` as its gate. A repository adds an item, or
patches or excludes one of gov's, from its overlay, as it does any registered kind's row; every check here
reads the COMPOSITION of gov's `[[item]]` rows with the repository's at HEAD, never the overlay's text.
The composition is the playbook kit's `overlay_rows.py compose --kind item`, found through `resolve_kit_dir`
and run as a subprocess, so this kit imports no playbook module and takes no edge to that kit.

`check` composes the repository the kit sits in, then grades the definition holding the composed rows as
its `[[item]]` table: `check_program`, `check_witness_classes` and `check_item_declarations` of
`loop_lib.py`; the schema's `[[fixed-row]]` set joined with each step's exit and the floor item
`item.test.verdict`, both ways; the `[[record-version]]` rows against the memory-tree kit's record table;
and each record input of a composed item joined to an item of its needs closure that returns that kind at
that version. It prints `loop: items composed · <n> row(s) · <m> repository`, one `loop: patch <row> on
<tag> · <field> <op> · <class>` line per classified patch operation, one `loop: record-version <kind> · <n>
· <hash>` line per version row, `loop: record inputs · <n> joined`, and each refusal as `loop: refused ·
...`. Exit 0 green, 1 a refusal, the composition's included, 2 unarmed: the playbook kit unresolved, the
kind unregistered, its schema absent, or HEAD holding no definition. `check --selftest` runs `check` over
the tree, then every plant through `loop_lib.run_selftest_cases`.

`new` appends one gov `[[item]]` row to the definition beside this file, its routes sending `done` to the
step's exit item, and grades the file as written with the definition's own checks, since the composition
reads HEAD and the row is not committed; a refusal restores the file's bytes and exits 1. A name that is
not one tag segment, the name `adopter`, a tag the definition declares, a step that is no gov step, a flag
owed by the actor's kind and absent, and one a `role:` actor takes from its role each exit 2 before any
write. The register's factory verb runs it: `python <prefix>/playbook/core.py new item <name> ...`.

`--fixture --plant <case>` builds a scratch repository under the host temp directory holding a copy of
the kits the check reaches from this working tree, loop, playbook, memory-tree, policy and roles, at
their places under the tool root, committed, so a plant reads this tree's code and not HEAD's; it writes
the plant, commits it, runs `check` there as a subprocess and relays its output and its exit, 1 where a
step the plant owes beside `check` does not answer as owed. The cases are `PLANTS`.

`read_item_members` and `write_item_plant` are the step gate's `item` class: every gov item tag of the
definition under a tree, and the first `[[item]]` table taken out of a clone's definition, staged.

WHAT THIS DOES NOT CHECK: that a `fields` hash re-pinned with no `version` bump was meant, since the rule
reads no base; that a record input's text before its kind names a layer the record lives in; a role item's
`returns`, which its role states and the record join does not read; and an untyped kind's version, which
reads 1.
"""
import hashlib
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from loop_lib import (DEFINITION, SEG, STEP_TAGS, LoopError, check_item_declarations, check_loop,  # noqa: E402
                      check_program, check_witness_classes, read_definition, read_item_rows, read_layer_tags,
                      read_memory_tree, read_role_defaults, resolve_kit_dir, run_selftest_cases)

SAY = "loop"
KIND = "item"
SCHEMA = "item-schema.toml"
FLOOR_ITEM = "item.test.verdict"
ADOPTER = "adopter"
#: A record kind as an input's text after its layer tag, or as a `returns`: its name, and its version or none.
RECORD_REF = re.compile(r"record-kind\.(%s)(?:@([1-9][0-9]*))?" % SEG.pattern)
#: The key order a factory row and a fixture row are written in, the definition's own.
ROW_KEYS = ("tag", "step", "actor", "needs", "inputs", "allowance", "returns", "outcomes", "witness", "owner",
            "routes")
#: The kits a plant's scratch repository copies, each `(home, the file that finds it)`; roles is optional.
SCRATCH_KITS = (("loop", "loop_lib.py"), ("playbook", "overlay_rows.py"), ("memory-tree", "build_records.py"),
                ("policy", "policy.py"), ("roles", "roles_lib.py"))
OVERLAY = ".governance/instructions.toml"
POLICY_FILE = ".governance/policy.toml"
FACTORY_ARGV = ("new", "item", "demo", "--step", "step.test", "--actor", "command:demo", "--input",
                "layer.flow:the demo input", "--allowance", "the demo record", "--returns", "record-kind.demo",
                "--witness-by", "the demo record", "--owner", "dDeclaredLoop")
PLANTS = {
    "factory": "core.py new item demo appends item.test.demo, check reads it, and the same new again exits 2",
    "repo-cycle": "two repository items of the test step, each needing the other",
    "repo-unresolved-need": "a repository item needing an item no row declares",
    "repo-input-unproduced": "a repository item reading record-kind.acceptance@1 with no needed item returning it",
    "repo-input-produced": "the same item needing item.build.acceptance",
    "version-unbumped": "the acceptance kind's required fields changed in the record table at version 1",
    "version-bumped": "the same change, the version 2 and the hash re-pinned",
    "version-stale-input": "that bump, beside the produced item's input still at @1",
    "patch-witness": "an amends of item.test.select's witness",
    "patch-outcomes": "an amends adding an outcome to item.test.select",
    "supersede-floor": "a supersedes of the floor item item.test.verdict",
    "supersede-exit": "a supersedes of the exit item item.build.exit",
    "exclude-needed": "item.test.select excluded, which item.test.verdict needs",
    "exclude-breakpoint": "item.test.flakes excluded, which no item needs and review.breakpoints names",
    "patch-remove-need": "an amends removing item.test.select's need of item.test.merge",
    "patch-add-need": "an amends adding a need of item.build.exit to item.test.merge",
    "patch-routes": "an amends writing item.test.select's routes whole",
    "amended-cycle": "an amends adding item.test.verdict to item.test.merge's needs, the overlay text holding no cycle",
    "exit-unfixed": "the schema holding no [[fixed-row]] for item.build.exit",
    "schema-absent": "the schema file removed",
    "definition-uncommitted": "the definition's removal committed and the definition staged again, as a first install leaves it",
}
#: Each selftest case: the case, its owed exit, and the opening and needle of the line it owes.
CASES = (("check", 0, "loop: items composed", "row(s)"),
         ("factory", 0, "loop: fixture · new again", "item.test.demo"),
         ("repo-cycle", 1, "loop: refused", "cycle"),
         ("repo-unresolved-need", 1, "loop: refused", "item.test.adopter.nosuch"),
         ("repo-input-unproduced", 1, "loop: refused", "layer.memory:record-kind.acceptance@1"),
         ("repo-input-produced", 0, "loop: record inputs", "1 joined"),
         ("version-unbumped", 1, "loop: refused", "record-kind.acceptance"),
         ("version-bumped", 0, "loop: record-version record-kind.acceptance", "· 2 ·"),
         ("version-stale-input", 1, "loop: refused", "layer.memory:record-kind.acceptance@1"),
         ("patch-witness", 1, "loop: refused", "principle=principle.p2"),
         ("patch-outcomes", 1, "loop: refused", "principle=principle.p24"),
         ("supersede-floor", 1, "loop: refused", "the fixed row item.test.verdict"),
         ("supersede-exit", 1, "loop: refused", "the fixed row item.build.exit"),
         ("exclude-needed", 1, "loop: refused", "item.test.verdict still holds"),
         ("exclude-breakpoint", 1, "loop: refused", "review.breakpoints"),
         ("patch-remove-need", 0, "loop: patch", "needs remove · widens"),
         ("patch-add-need", 0, "loop: patch", "needs add · narrows"),
         ("patch-routes", 0, "loop: patch", "routes add · widens"),
         ("amended-cycle", 1, "loop: refused", "cycle"),
         ("exit-unfixed", 1, "loop: refused", "item.build.exit"),
         ("schema-absent", 2, "loop: fixture · compose", "unarmed"),
         ("definition-uncommitted", 2, "loop: fixture · render after the commit", "gov:item"))
#: The render probe a plant runs in its scratch: the item rows `read_kind_rows` composes, or the `gov:item`
#: lines of `render_delta_report`, argv[1] the scratch's playbook kit.
RENDER_PROBE = """import pathlib, sys
sys.path.insert(0, sys.argv[1])
import render_playbook as rp
if sys.argv[2] == "rows":
    print(len([k for k, _s, _w in rp.read_kind_rows(pathlib.Path.cwd(), set(), []) if k == "item"]))
else:
    try:
        lines = rp.render_delta_report(pathlib.Path.cwd())
    except rp.Refusal as exc:
        print("refused: %s" % exc)
        sys.exit(1)
    print(sum(1 for ln in lines if "[gov:item " in ln))
"""


def derive_definition_rel():
    """The definition's path in the tree this kit sits in, tree-relative: the same at every clone of it."""
    root = next((d for d in (KIT, *KIT.parents) if (d / ".git").exists()), KIT.parent)
    return (KIT.relative_to(root) / DEFINITION).as_posix()


def derive_record_hash(row):
    """The first eight hex of the SHA-256 of one record table row's `required` and `closed`, canonical JSON."""
    body = {"required": row.get("required", ()), "closed": row.get("closed", ())}
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
                          .encode("utf-8")).hexdigest()[:8]


def derive_record_ref(text):
    """`(record-kind.<name>, version or None)` where `text` names a record kind whole, else None."""
    m = RECORD_REF.fullmatch(text.strip()) if isinstance(text, str) else None
    return ("record-kind.%s" % m.group(1), int(m.group(2)) if m.group(2) else None) if m else None


def render_toml_value(value):
    """`value` as TOML: an inline table, an array, or a JSON-spelled string, number or boolean."""
    if isinstance(value, dict):
        return "{ %s }" % ", ".join("%s = %s" % (k, render_toml_value(v)) for k, v in value.items())
    if isinstance(value, list):
        return "[%s]" % ", ".join(render_toml_value(v) for v in value)
    return json.dumps(value, ensure_ascii=False)


def render_item_row(row):
    """One `[[item]]` table, its keys in `ROW_KEYS` order first, then any other."""
    keys = [k for k in ROW_KEYS if k in row] + [k for k in row if k not in ROW_KEYS]
    return "[[item]]\n" + "".join("%s = %s\n" % (k, render_toml_value(row[k])) for k in keys)


# ------------------------------------------------------------------------------------------ the check
def read_composition(root):
    """`(exit, payload, lines)` of the playbook kit's `overlay_rows.py compose --kind item` over `root`, run
    with the memory-tree kit's git leaks unset, so an inherited `GIT_DIR` never retargets the read: exit 0
    with the JSON payload, 1 with the refusal's lines, 2 with the unarmed lines."""
    try:
        script = resolve_kit_dir("playbook", "overlay_rows.py", KIT) / "overlay_rows.py"
    except LookupError as e:
        return 2, None, [str(e)]
    try:
        from loop_witness import read_clean_env
        env = read_clean_env(PYTHONIOENCODING="utf-8")
    except (LookupError, ImportError) as e:
        return 2, None, [str(e)]
    try:
        p = subprocess.run([sys.executable, str(script), "compose", "--kind", KIND], cwd=str(root),
                           capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=300, env=env)
    except subprocess.TimeoutExpired:
        return 2, None, ["%s compose did not return within 300 s" % script.as_posix()]
    lines = [ln for ln in (p.stdout + p.stderr).splitlines() if ln.strip()]
    if p.returncode == 0:
        try:
            return 0, json.loads(p.stdout), []
        except ValueError as e:
            return 1, None, ["the composition printed no JSON: %s" % e]
    return (p.returncode if p.returncode in (1, 2) else 1), None, lines or ["compose exited %d" % p.returncode]


def check_record_versions(data, rows):
    """`(lines, refusals, versions)`: one `loop: record-version` line per `[[record-version]]` row of `data`,
    a refusal per row naming no typed kind, given twice, with no integer version from 1, or whose `fields`
    differs from its kind's hash in the memory-tree kit's record table while its version stays, and one per
    typed kind an item of `rows` returns or reads that no row pins; `versions` `{kind: version}`."""
    read_memory_tree("build_records.py")
    from build_records import KINDS
    table = data.get("record-version", [])
    if not isinstance(table, list) or not all(isinstance(r, dict) for r in table):
        return [], ["'record-version' is not an array of tables"], {}
    lines, refusals, versions = [], [], {}
    for n, row in enumerate(table, 1):
        kind, version, pinned = row.get("kind"), row.get("version"), row.get("fields")
        name = kind[len("record-kind."):] if isinstance(kind, str) and kind.startswith("record-kind.") else None
        if name not in KINDS:
            refusals.append("record-version row %d (%s) names no typed record kind, a key of the record table: %s"
                            % (n, kind, " ".join(sorted(KINDS))))
            continue
        if kind in versions:
            refusals.append("record-version row %d (%s) pins a kind an earlier row pins" % (n, kind))
            continue
        if not isinstance(version, int) or isinstance(version, bool) or version < 1:
            refusals.append("record-version %s version %r is no integer from 1" % (kind, version))
            continue
        now = derive_record_hash(KINDS[name])
        versions[kind] = version
        lines.append("%s: record-version %s · %d · %s" % (SAY, kind, version, now))
        if pinned != now:
            refusals.append("record-version %s fields %s is not %s, the hash of its row in the record table, while "
                            "its version stays %d: its meaning changed with no bump · remedy: bump the version and "
                            "re-pin fields" % (kind, pinned, now, version))
    for row in rows:
        refs = [("returns", row.get("returns"))] + [("input", t.partition(":")[2]) for t in row.get("inputs") or []
                                                     if isinstance(t, str)]
        for field, text in refs:
            ref = derive_record_ref(text)
            if ref and ref[0][len("record-kind."):] in KINDS and ref[0] not in versions:
                refusals.append("the item %s %s names %s, a typed record kind no [[record-version]] row pins" % (
                    row.get("tag"), field, ref[0]))
    return lines, refusals, versions


def check_item_composition(data, where, rows, fixed, layers, roles, versions):
    """`(lines, refusals)` of the composed `rows` held as `data`'s `[[item]]` table: `check_program`,
    `check_witness_classes` and `check_item_declarations`; `fixed`, the schema's `[[fixed-row]]` tags, joined
    both ways with each step's exit and the floor item; then each record input joined to an item of its
    needs closure returning that kind at that version, `versions` the pinned ones and 1 for any other."""
    held = dict(data, item=rows)
    refusals = []
    try:
        check_program(held, where, layers)
        check_witness_classes(held, where)
    except LoopError as e:
        refusals.append(str(e))
    refusals += check_item_declarations(rows, roles[0], roles[1])[1]
    schema = (pathlib.Path(derive_definition_rel()).parent / SCHEMA).as_posix()
    declared = {r.get("tag"): r for r in rows}
    for step in data.get("step", []):
        if step.get("exit") not in fixed:
            refusals.append("the step %s exit %s holds no [[fixed-row]] in %s" % (step.get("tag"), step.get("exit"),
                                                                                 schema))
    if FLOOR_ITEM not in fixed:
        refusals.append("the floor item %s holds no [[fixed-row]] in %s" % (FLOOR_ITEM, schema))
    refusals += ["the [[fixed-row]] %s of %s names no declared item" % (t, schema) for t in sorted(fixed)
                 if t not in declared]

    def derive_version(ref):
        return ref[1] or versions.get(ref[0], 1)

    joined = 0
    for row in rows:
        for text in row.get("inputs") or []:
            ref = derive_record_ref(text.partition(":")[2]) if isinstance(text, str) else None
            if ref is None:
                continue
            want, seen, todo = derive_version(ref), set(), [row.get("tag")]
            while todo:
                for entry in (declared.get(todo.pop()) or {}).get("needs") or []:
                    for t in entry if isinstance(entry, list) else [entry]:
                        if t not in seen:
                            seen.add(t)
                            todo.append(t)
            made = [t for t in sorted(seen) if (got := derive_record_ref((declared.get(t) or {}).get("returns")))
                    and got[0] == ref[0] and derive_version(got) == want]
            if made:
                joined += 1
            else:
                refusals.append("the item %s input %r reads %s@%d, which no item in its needs closure returns at "
                                "that version" % (row.get("tag"), text, ref[0], want))
    return ["%s: record inputs · %d joined" % (SAY, joined)], refusals


def run_check():
    """The `check` verb over the tree this kit sits in: -> its exit."""
    root = next((d for d in (KIT, *KIT.parents) if (d / ".git").exists()), KIT)
    try:
        data, where = read_definition(KIT)
        check_loop(data, where)
    except LoopError as e:
        print("%s: refused · %s" % (SAY, e))
        return 1
    code, payload, said = read_composition(root)
    if code == 2:
        print("%s: items unarmed · %s" % (SAY, said[0]))
        for line in said[1:]:
            print("%s: items unarmed · %s" % (SAY, line))
        return 2
    if code:
        for line in said:
            print("%s: refused · %s" % (SAY, line))
        return 1
    rows = [{k: v for k, v in r.items() if k not in ("origin", "source")} for r in payload["rows"]]
    print("%s: items composed · %d row(s) · %d repository" % (
        SAY, len(rows), sum(1 for r in payload["rows"] if r.get("origin") == "repository")))
    for op in payload["operations"]:
        print("%s: patch %s on %s · %s %s · %s" % (SAY, op["row"], op["tag"], op["field"], op["op"], op["class"]))
    try:
        layers = read_layer_tags(KIT)
    except LookupError:
        layers = None
    try:
        with open(KIT / SCHEMA, "rb") as fh:
            fixed = {r.get("tag") for r in tomllib.load(fh).get("fixed-row", []) if isinstance(r, dict)}
        version_lines, refusals, versions = check_record_versions(data, rows)
    except (OSError, tomllib.TOMLDecodeError, LookupError, ImportError) as e:
        print("%s: items unarmed · %s" % (SAY, e))
        return 2
    join_lines, more = check_item_composition(data, where, rows, fixed, layers, read_role_defaults(KIT), versions)
    for line in version_lines + join_lines:
        print(line)
    for r in more + refusals:
        print("%s: refused · %s" % (SAY, r))
    return 1 if more or refusals else 0


# ---------------------------------------------------------------------------------------- the factory
def write_item_row(row):
    """Append `row` to the definition beside this file and grade the file as written: -> the refusals, the
    file's bytes restored where there is one."""
    path = KIT / DEFINITION
    before = path.read_bytes()
    nl = b"\r\n" if b"\r\n" in before else b"\n"
    lead = b"" if before.endswith(b"\n") else nl
    path.write_bytes(before + lead + ("\n" + render_item_row(row)).encode("utf-8").replace(b"\n", nl))
    try:
        data, where = read_definition(KIT)
        check_loop(data, where)
        try:
            layers = read_layer_tags(KIT)
        except LookupError:
            layers = None
        check_program(data, where, layers)
        check_witness_classes(data, where)
        roles, why = read_role_defaults(KIT)
        refusals = check_item_declarations(read_item_rows(data, where), roles, why)[1]
    except LoopError as e:
        refusals = [str(e)]
    if refusals:
        path.write_bytes(before)
    return refusals


def run_new(argv):
    """The `new` verb: -> its exit."""
    import argparse
    ap = argparse.ArgumentParser(prog="loop_items.py new")
    ap.add_argument("name")
    for flag in ("--step", "--actor", "--witness-by", "--owner"):
        ap.add_argument(flag, required=True)
    ap.add_argument("--input", action="append")
    ap.add_argument("--allowance")
    ap.add_argument("--returns")
    a = ap.parse_args(argv)
    try:
        data, where = read_definition(KIT)
        check_loop(data, where)
    except LoopError as e:
        print("%s: refused · %s" % (SAY, e))
        return 1
    steps = {s["tag"]: s for s in data["step"]}
    tag = "item.%s.%s" % (a.step.rpartition(".")[2], a.name)
    role = a.actor.startswith("role:")
    given = [f for f, v in (("--input", a.input), ("--allowance", a.allowance), ("--returns", a.returns)) if v]
    why = ("the name %r is not one tag segment of the shape %s" % (a.name, SEG.pattern)
           if not SEG.fullmatch(a.name) else "the name %s is the repository's seat, never a gov item's" % ADOPTER
           if a.name == ADOPTER else "the step %s is no gov step: %s" % (a.step, " ".join(STEP_TAGS))
           if a.step not in steps else "the definition declares %s already" % tag
           if tag in {r.get("tag") for r in read_item_rows(data, where)}
           else "a %s actor takes %s from its role" % (a.actor, " and ".join(given)) if role and given
           else "a %s actor owes %s" % (a.actor, " and ".join(
               f for f in ("--input", "--allowance", "--returns") if f not in given))
           if not role and len(given) < 3 else None)
    if why:
        print("%s: refused · new %s · %s" % (SAY, tag, why))
        return 2
    row = {"tag": tag, "step": a.step, "actor": a.actor, "needs": []}
    if not role:
        row.update(inputs=a.input, allowance=a.allowance, returns=a.returns)
    row.update(outcomes=["done"], witness={"class": "history", "by": a.witness_by}, owner=a.owner,
               routes={"done": steps[a.step]["exit"]})
    refusals = write_item_row(row)
    for r in refusals:
        print("%s: refused · new %s · %s" % (SAY, tag, r))
    if refusals:
        print("%s: new · %s refused, the definition's bytes restored" % (SAY, tag))
        return 1
    print("%s: new · appended %s to %s" % (SAY, tag, (KIT / DEFINITION).as_posix()))
    return 0


# ------------------------------------------------------------------------------- the step gate's class
def read_item_members(root):
    """The step gate's `item` class: every gov `[[item]]` tag of the definition under `root`, graded by
    nothing, so a plant that breaks a need still reads; an empty set where the tree holds no definition."""
    path = pathlib.Path(root) / derive_definition_rel()
    if not path.is_file():
        return set()
    data, where = read_definition(path.parent)
    return {r["tag"] for r in read_item_rows(data, where) if isinstance(r.get("tag"), str)}


def write_item_plant(clone):
    """The step gate's `item` plant: the first `[[item]]` table taken out of the clone's definition, staged.
    -> its member id."""
    rel = derive_definition_rel()
    path = pathlib.Path(clone) / rel
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^\[\[item\]\]\n.*?(?=^\[\[|\Z)", text, re.M | re.S)
    if m is None:
        raise ValueError("the item plant found no [[item]] table in %s" % rel)
    tag = tomllib.loads(m.group(0))["item"][0]["tag"]
    path.write_text(text[:m.start()] + text[m.end():], encoding="utf-8", newline="")
    subprocess.run(["git", "-C", str(clone), "add", "--", rel], check=True, capture_output=True)
    return "item:%s" % tag


# ------------------------------------------------------------------------------------------ the plants
def build_scratch_tree():
    """`(top, base sha, gov pins)`: a scratch repository holding each kit of `SCRATCH_KITS` this tree
    resolves, at its place under the tool root, committed, and the pin of each gov item at that commit.
    LookupError where a kit but roles does not resolve; the directory is removed on any failure."""
    from loop_witness import remove_tree, run_fixture_git, write_fixture_files
    top = pathlib.Path(tempfile.mkdtemp(prefix="li-"))
    try:
        tool_rel = pathlib.Path(derive_definition_rel()).parent.parent
        for home, anchor in SCRATCH_KITS:
            try:
                src = resolve_kit_dir(home, anchor, KIT)
            except LookupError:
                if home == "roles":
                    continue
                raise
            shutil.copytree(src, top / tool_rel / src.name, ignore=shutil.ignore_patterns("__pycache__"))
        write_fixture_files(top, {".memory-tree.conf": "MEMORY_ROOT=memory\n"})
        run_fixture_git(top, "init", "-q", "--template=")
        run_fixture_git(top, "add", "-A")
        run_fixture_git(top, "commit", "-qm", "the scratch kits")
        code, payload, said = run_scratch_check(top, compose=True)
        if code != 0:
            raise LookupError("the scratch's compose exited %d: %s" % (code, " | ".join(said)[:300]))
        return top, run_fixture_git(top, "rev-parse", "HEAD"), payload["pins"]
    except BaseException:
        remove_tree(top)
        raise


def run_scratch_check(top, compose=False):
    """The scratch's own `check`, or with `compose` its `overlay_rows.py compose --kind item`, run in `top`
    with the memory-tree kit's git leaks unset: `(exit, the JSON payload or None, its lines)`."""
    from loop_witness import read_clean_env
    tool = top / pathlib.Path(derive_definition_rel()).parent
    argv = ([str(tool.parent / resolve_kit_dir("playbook", "overlay_rows.py", KIT).name / "overlay_rows.py"),
             "compose", "--kind", KIND] if compose else [str(tool / pathlib.Path(__file__).name), "check"])
    p = subprocess.run([sys.executable, *argv], cwd=str(top), capture_output=True, text=True, encoding="utf-8",
                       errors="replace", env=read_clean_env(PYTHONIOENCODING="utf-8"), timeout=300)
    lines = [ln for ln in (p.stdout + p.stderr).splitlines() if ln.strip()]
    payload = json.loads(p.stdout) if compose and p.returncode == 0 else None
    return p.returncode, payload, lines


def run_render_probe(top, mode):
    """`(exit, last line)` of `RENDER_PROBE` in `top`, `mode` `rows` or `delta`."""
    from loop_witness import read_clean_env
    kit = top / pathlib.Path(derive_definition_rel()).parent.parent / resolve_kit_dir(
        "playbook", "overlay_rows.py", KIT).name
    p = subprocess.run([sys.executable, "-c", RENDER_PROBE, str(kit), mode], cwd=str(top), capture_output=True,
                       text=True, encoding="utf-8", errors="replace", env=read_clean_env(PYTHONIOENCODING="utf-8"),
                       timeout=300)
    lines = [ln for ln in (p.stdout + p.stderr).splitlines() if ln.strip()]
    return p.returncode, lines[-1] if lines else "no output"


def run_factory(top):
    """`(exit, last line)` of the register's factory verb, `core.py new item demo ...`, in the scratch `top`."""
    from loop_witness import read_clean_env
    core = top / pathlib.Path(derive_definition_rel()).parent.parent / resolve_kit_dir(
        "playbook", "core.py", KIT).name / "core.py"
    p = subprocess.run([sys.executable, str(core), *FACTORY_ARGV], cwd=str(top), capture_output=True, text=True,
                       encoding="utf-8", errors="replace", env=read_clean_env(PYTHONIOENCODING="utf-8"), timeout=300)
    said = [ln for ln in (p.stdout + p.stderr).splitlines() if ln.strip()]
    return p.returncode, said[-1] if said else "no output"


def derive_repo_item(name, needs=(), inputs=("layer.flow:the fixture's input",)):
    """A repository item of the test step, whole, tagged at the adopter seat."""
    return {"tag": "item.test.%s.%s" % (ADOPTER, name), "step": "step.test", "actor": "command:fixture",
            "needs": list(needs), "inputs": list(inputs), "allowance": "the fixture's record",
            "returns": "record-kind.fixture", "outcomes": ["done"],
            "witness": {"class": "history", "by": "the fixture's record"}, "owner": "dDeclaredLoop",
            "routes": {"done": "item.test.exit"}}


def write_fixture_plant(top, case, pins, bad):
    """Write `case`'s plant in the scratch `top` and commit it, `pins` gov's item pins at the base; a step
    the plant owes beside `check` and does not answer as owed appends to `bad`."""
    from loop_witness import run_fixture_git, write_fixture_files
    defn, schema = derive_definition_rel(), (pathlib.Path(derive_definition_rel()).parent / SCHEMA).as_posix()
    gov = {r["tag"]: r for r in tomllib.loads((top / defn).read_text(encoding="utf-8"))["item"]}

    def render_patch_row(name, edge, target, **fields):
        return render_item_row({"tag": "item.test.%s.%s" % (ADOPTER, name),
                                "edges": "%s=%s@%s" % (edge, target, pins[target]), **fields})

    def write_record_bump(text):
        read_memory_tree("build_records.py")
        from build_records import KINDS
        req = KINDS["acceptance"]["required"]
        spelled = '"required": (%s)' % ", ".join(json.dumps(f) for f in req)
        rel = top / pathlib.Path(defn).parent.parent / resolve_kit_dir("memory-tree", "build_records.py", KIT).name
        table = (rel / "build_records.py").read_text(encoding="utf-8")
        if table.count(spelled) != 1:
            raise ValueError("the record table spells the acceptance kind's fields other than %s" % spelled)
        (rel / "build_records.py").write_text(table.replace(spelled, spelled[:-1] + ', "Note")'), encoding="utf-8",
                                              newline="")
        if text is None:
            return
        now = derive_record_hash(dict(KINDS["acceptance"], required=(*req, "Note")))
        body = (top / defn).read_text(encoding="utf-8")
        old = re.search(r'kind = "record-kind\.acceptance"\nversion = 1\nfields = "[0-9a-f]{8}"\n', body)
        if old is None:
            raise ValueError("the definition holds no version-1 row for record-kind.acceptance")
        (top / defn).write_text(body.replace(old.group(0), 'kind = "record-kind.acceptance"\nversion = 2\n'
                                             'fields = "%s"\n' % now), encoding="utf-8", newline="")

    reader = "layer.memory:record-kind.acceptance@1"
    overlay = {
        "repo-cycle": [derive_repo_item("cycle-a", ["item.test.adopter.cycle-b"]),
                       derive_repo_item("cycle-b", ["item.test.adopter.cycle-a"])],
        "repo-unresolved-need": [derive_repo_item("needy", ["item.test.adopter.nosuch"])],
        "repo-input-unproduced": [derive_repo_item("reader", [], [reader])],
        "repo-input-produced": [derive_repo_item("reader", ["item.build.acceptance"], [reader])],
        "version-stale-input": [derive_repo_item("reader", ["item.build.acceptance"], [reader])],
    }.get(case)
    text = "\n".join(render_item_row(r) for r in overlay) if overlay else {
        "patch-witness": render_patch_row("select-seen", "amends", "item.test.select",
                               witness={"class": "history", "by": "a patched witness"}),
        "patch-outcomes": render_patch_row("select-skips", "amends", "item.test.select", add={"outcomes": ["skipped"]}),
        "supersede-floor": render_patch_row("verdict-own", "supersedes", FLOOR_ITEM,
                                 **{k: v for k, v in gov.get(FLOOR_ITEM, {}).items() if k != "tag"}),
        "supersede-exit": render_patch_row("build-exit-own", "supersedes", "item.build.exit",
                                **{k: v for k, v in gov.get("item.build.exit", {}).items() if k != "tag"}),
        "patch-remove-need": render_patch_row("select-free", "amends", "item.test.select", remove={"needs": ["item.test.merge"]}),
        "patch-add-need": render_patch_row("merge-waits", "amends", "item.test.merge", add={"needs": ["item.build.exit"]}),
        "patch-routes": render_patch_row("select-routed", "amends", "item.test.select", routes={"selected": "item.test.merge"}),
        "amended-cycle": render_patch_row("merge-after-verdict", "amends", "item.test.merge", add={"needs": [FLOOR_ITEM]}),
    }.get(case)
    if text:
        write_fixture_files(top, {OVERLAY: text})
    if case == "exclude-needed":
        write_fixture_files(top, {POLICY_FILE: '[instructions]\nexclude = ["item.test.select"]\n'})
    elif case == "exclude-breakpoint":
        write_fixture_files(top, {POLICY_FILE: '[instructions]\nexclude = ["item.test.flakes"]\n\n'
                                               '[review]\nbreakpoints = ["item.test.flakes"]\n'})
    elif case in ("version-unbumped", "version-bumped", "version-stale-input"):
        write_record_bump(None if case == "version-unbumped" else "re-pin")
    elif case == "exit-unfixed":
        body = (top / schema).read_text(encoding="utf-8")
        block = '[[fixed-row]]\ntag = "item.build.exit"\nfixed-by = ["principle=principle.p20"]\n'
        if block not in body:
            raise ValueError("the schema holds no [[fixed-row]] block for item.build.exit as %r" % block)
        (top / schema).write_text(body.replace(block, ""), encoding="utf-8", newline="")
    elif case == "schema-absent":
        (top / schema).unlink()
    elif case == "factory":
        rc, line = run_factory(top)
        print("%s: fixture · new · exit %d · %s" % (SAY, rc, line))
        if rc != 0:
            bad.append("core.py new item demo exited %d, not 0: %s" % (rc, line))
    run_fixture_git(top, "add", "-A")
    run_fixture_git(top, "commit", "-q", "--allow-empty", "-m", "plant %s" % case)
    if case == "definition-uncommitted":
        run_fixture_git(top, "rm", "-q", "--cached", "--", defn)
        run_fixture_git(top, "commit", "-qm", "the definition's removal")
        run_fixture_git(top, "add", "--", defn)


def run_fixture(case, base):
    """One plant over the scratch `base`, `(top, sha, pins)`, reset to its commit first: -> the exit."""
    from loop_witness import run_fixture_git
    top, sha, pins = base
    run_fixture_git(top, "reset", "-q", "--hard", sha)
    run_fixture_git(top, "clean", "-qfdx")
    print("%s: fixture · plant %s · %s" % (SAY, case, PLANTS[case]))
    bad = []
    try:
        write_fixture_plant(top, case, pins, bad)
    except (subprocess.CalledProcessError, OSError, ValueError, LookupError, KeyError) as exc:
        print("%s: fixture · FAIL · the plant %s could not be built: %s %s" % (
            SAY, case, exc, (getattr(exc, "stderr", "") or "").strip()[:300]))
        return 1
    code, _payload, said = run_scratch_check(top)
    for line in said:
        print(line)

    def check_owed_step(step, got, owed, needle, line):
        print("%s: fixture · %s · exit %d · %s" % (SAY, step, got, line))
        if got != owed or needle not in line:
            bad.append("%s exited %d, owed %d and a line naming %r" % (step, got, owed, needle))

    defn = derive_definition_rel()
    if case == "factory":
        rc, line = run_factory(top)
        check_owed_step("new again", rc, 2, "item.test.demo", line)
    elif case in ("schema-absent", "definition-uncommitted"):
        rc, _p, said = run_scratch_check(top, compose=True)
        path = (pathlib.Path(defn).parent / SCHEMA).as_posix() if case == "schema-absent" else defn
        check_owed_step("compose", rc, 2, path, said[0] if said else "no output")
        if not (said and "unarmed" in said[0]):
            bad.append("compose printed no unarmed line: %s" % said[:2])
        rc, line = run_render_probe(top, "rows" if case == "schema-absent" else "delta")
        check_owed_step("render" if case == "schema-absent" else "render before the commit", rc, 0, "0", line)
        if line != "0":
            bad.append("the render composed %s item line(s), owed none" % line)
        if case == "definition-uncommitted":
            run_fixture_git(top, "commit", "-qm", "the staged definition")
            count = str(len(gov_rows := tomllib.loads((top / defn).read_text(encoding="utf-8"))["item"]))
            rc, line = run_render_probe(top, "delta")
            check_owed_step("render after the commit", rc, 0, count, "%s gov:item line(s), %d [[item]] table(s)" % (
                line, len(gov_rows)))
            if line != count:
                bad.append("the render after the commit printed %s gov:item line(s), owed %s" % (line, count))
    for why in bad:
        print("%s: fixture · FAIL · %s" % (SAY, why))
    return 1 if bad else code


def run_selftest():
    """`check` over the tree, then every plant over one scratch base: -> 0 when every case holds."""
    from loop_witness import remove_tree
    try:
        base = build_scratch_tree()
    except (LookupError, OSError, ValueError, subprocess.CalledProcessError) as exc:
        print("%s: item kind selftest · UNARMED · the scratch could not be built: %s" % (SAY, exc))
        return 2
    try:
        cases = [(case, ["check"] if case == "check" else ["--fixture", "--plant", case], owed, opening, needle)
                 for case, owed, opening, needle in CASES]
        return run_selftest_cases(lambda argv: run_check() if argv == ["check"] else run_fixture(argv[2], base),
                                  cases, "%s: item kind selftest" % SAY)
    finally:
        remove_tree(base[0])


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if argv == ["check"]:
        return run_check()
    if argv == ["check", "--selftest"]:
        return run_selftest()
    if argv[:1] == ["new"]:
        return run_new(argv[1:])
    if len(argv) == 3 and argv[:2] == ["--fixture", "--plant"] and argv[2] in PLANTS:
        from loop_witness import remove_tree
        try:
            base = build_scratch_tree()
        except (LookupError, OSError, ValueError, subprocess.CalledProcessError) as exc:
            print("%s: fixture · UNARMED · the scratch could not be built: %s" % (SAY, exc))
            return 2
        try:
            return run_fixture(argv[2], base)
        finally:
            remove_tree(base[0])
    print("usage: python loop_items.py check [--selftest] | new <name> --step <step> --actor <actor> --witness-by "
          "<text> --owner <build> [--input <layer:what>]... [--allowance <text>] [--returns <record>] | "
          "--fixture --plant <%s>" % "|".join(PLANTS), file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
