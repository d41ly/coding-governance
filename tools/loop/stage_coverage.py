#!/usr/bin/env python3
"""stage_coverage.py — every part of the product joined both ways to the stage it serves (TOOL-dDeclaredLoop-4).

    python stage_coverage.py                          # the tree: the part join, then the stage half
    python stage_coverage.py --fixture --plant <case> # the tree with one break of PLANTS made in memory
    python stage_coverage.py --selftest               # the tree, then every plant

A claim is a non-empty list of the [[step]] tags the loop definition beside this file declares, or the
one-word list ["none"]: the part serves no build stage. Any other value is no claim, the part unclaimed.
Each kind's claim has one home: a dossier's top-level `stage` key, read through the codebase-map kit's
`load_map_tree`; a gate-leg row's last key `stage`, in the manifest at the tool root; a workflow's
`step` in the definition's [[workflow]] row; a role's, derived from its `workflow:` through that row;
and a hook's [[hook]] row of the definition, its key's `{prefix}/` expanded to the tool root's
repo-relative path. `derive_part_claims` joins the five populations (the map's feature dossiers, the
manifest's rows, the roles kit's workflows, its role slots, and the map's `git-hooks` and
`harness-hooks` inventory keys) to the claims through the memory-tree kit's `compute_coverage`, with an
empty baseline: an unclaimed part is red, and a claim naming no part is red as stale.
`derive_stage_witnesses` reads each step's exit item and its witness class through `check_loop` and
`check_witness_classes`; a refusal of either is red as the reader words it.

Lines: `stage-coverage: part · <kind> · <n> parts · <u> unclaimed · <s> stale`, or `· unarmed — no <kind>
in the tree`, red; `stage-coverage: role <slot> · workflow <name> · <stage>`; `stage-coverage: stage ·
<step> · exit <item> · witness <class>`; then `stage-coverage: unclaimed <kind> <name> · <no claim | the
value>`, `stage-coverage: stale <kind> <name>` and `stage-coverage: refused · <why>`. Exit 0, 1 on any
red, 2 `unarmed` where the codebase-map, roles or memory-tree kit does not resolve through
`resolve_kit_dir`. The kits take no edge: the leg is gov's own [[exempt_leg]].

WHAT THIS DOES NOT CHECK: whether a claimed stage is the right one, a review's judgement; whether a
dossier's stage agrees with the stages of the parts it claims; whether a witness holds; a claim on a
kit, Skill, guide or gotcha class, or FOUNDATION.md's fence.
"""
import argparse
import json
import os
import pathlib
import sys

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from loop_lib import (LoopError, check_loop, check_witness_classes, read_definition,  # noqa: E402
                      read_memory_tree, read_role_defaults, resolve_kit_dir, run_selftest_cases)

SAY = "stage-coverage"
KINDS = ("dossier", "leg", "workflow", "role", "hook")
#: `--plant`'s cases: what each breaks in memory, its owed exit, and the line its outcome prints, by
#: its opening and a needle.
PLANTS = {"unclaimed-leg": ("the first leg row's stage taken out", 1, "%s: unclaimed leg " % SAY, "no claim"),
          "unclaimed-hook": ("the [[hook]] row of the first harness key taken out", 1,
                             "%s: unclaimed hook " % SAY, "no claim"),
          "stale-hook": ("a [[hook]] row whose key no inventory holds", 1, "%s: stale hook " % SAY,
                         "no-such-hook.js"),
          "bad-tag": ("the first dossier's claim set to step.ship", 1, "%s: unclaimed dossier " % SAY, "step.ship"),
          "stage-no-witness": ("the witness of step.build's exit item taken out", 1, "%s: refused · " % SAY,
                               "item.build.exit"),
          "role-derived": ("the build workflow row's step set to step.test", 0, "%s: role gov-builder " % SAY,
                           "step.test"),
          "no-legs": ("the leg rows emptied", 1, "%s: part · leg · unarmed" % SAY, "")}


def read_stage_parts():
    """Every population and claim home as read from the tree: `{"dossier": {stem: stage or None},
    "leg": {name: stage or None}, "hook": [inventory keys], "hook_rows": [[hook] rows], "workflow":
    [roles-kit names], "role": {slot: its workflow key or None}, "definition": (data, where), "prefix":
    the tool root's repo-relative path}`. LookupError where a kit does not resolve; ValueError, a
    reader's refusal, where a source does not read."""
    map_dir = resolve_kit_dir("codebase-map", "map_lib.py", KIT)
    read_memory_tree("coverage_join.py")
    roles, why = read_role_defaults(KIT)
    if roles is None:
        raise LookupError(why)
    for found in (map_dir, resolve_kit_dir("roles", "roles_lib.py", KIT)):
        if str(found) not in sys.path:
            sys.path.insert(0, str(found))
    import map_lib  # the codebase-map kit's reader, found above
    import roles_lib  # the roles kit's reader, found above
    root = map_lib.repo_root()
    try:
        inventories = json.loads((map_lib.map_root() / "generated" / "inventories.json").read_text(
            encoding="utf-8")).get("inventories", {})
        tree = map_lib.load_map_tree(tuple(inventories))
        legs = json.loads((KIT.parent / "gate-legs.json").read_text(encoding="utf-8"))
        workflows = roles_lib.load_workflows(resolve_kit_dir("roles", "roles_lib.py", KIT))
    except (OSError, map_lib.MapError, roles_lib.RolesError) as e:
        raise ValueError(str(e))
    data, where = read_definition(KIT)
    prefix = pathlib.Path(os.path.relpath(KIT.parent, root)).as_posix()
    return {"dossier": {d.feature: list(d.stage) if d.stage is not None else None for d in tree.dossiers},
            "leg": {r.get("name"): r.get("stage") for r in legs},
            "hook": list(inventories.get("git-hooks", [])) + list(inventories.get("harness-hooks", [])),
            "hook_rows": data.get("hook", []),
            "workflow": [w.get("name") for w in workflows],
            "role": {slot: r["keys"].get("workflow") for slot, r in roles.items()},
            "definition": (data, where), "prefix": "" if prefix == "." else prefix + "/"}


def check_stage_claim(value, tags):
    """Whether `value` is a claim: a non-empty list of `tags`, or exactly ["none"]."""
    return isinstance(value, list) and bool(value) and (value == ["none"] or all(t in tags for t in value))


def derive_part_claims(parts, loop):
    """`(lines, reds)` of the part join over `parts` as `read_stage_parts` returns them and `loop`, the
    definition as `check_loop` returns it: one `part` line per kind, one `role` line per role whose
    workflow names a [[workflow]] row, then each unclaimed part and each stale claim."""
    import coverage_join  # the memory-tree kit's factory, put on the path by read_stage_parts
    tags = [s["tag"] for s in loop["step"]]
    steps = {w["name"]: w["step"] for w in loop["workflow"]}
    hooks = {}
    for row in parts["hook_rows"]:
        hooks[str(row.get("key")).replace("{prefix}/", parts["prefix"])] = row.get("stage")
    values = {"dossier": parts["dossier"], "leg": parts["leg"], "hook": hooks,
              "role": {s: w for s, w in parts["role"].items() if w is not None}}
    inventories = {"dossier": list(parts["dossier"]), "leg": list(parts["leg"]), "workflow": parts["workflow"],
                   "role": list(parts["role"]), "hook": parts["hook"]}
    claims = {kind: tuple(n for n, v in values[kind].items() if check_stage_claim(v, tags))
              for kind in ("dossier", "leg", "hook")}
    claims["workflow"] = tuple(steps)
    claims["role"] = tuple(s for s, w in parts["role"].items() if w in steps)
    cov = coverage_join.compute_coverage(inventories, {"stage-claims": claims}, {})
    lines, reds = [], []
    for kind in KINDS:
        if not inventories[kind]:
            reds.append("%s: part · %s · unarmed — no %s in the tree" % (SAY, kind, kind))
            continue
        lines.append("%s: part · %s · %d parts · %d unclaimed · %d stale" % (
            SAY, kind, len(inventories[kind]), len(cov.unclaimed.get(kind, [])), len(cov.stale_claims.get(kind, []))))
    for slot in claims["role"]:
        lines.append("%s: role %s · workflow %s · %s" % (SAY, slot, parts["role"][slot], steps[parts["role"][slot]]))
    for kind in KINDS:
        for name in cov.unclaimed.get(kind, []):
            value = values.get(kind, {}).get(name)
            reds.append("%s: unclaimed %s %s · %s" % (SAY, kind, name,
                                                     "no claim" if value is None else json.dumps(value)))
        for owned in cov.stale_claims.get(kind, []):
            reds.append("%s: stale %s %s" % (SAY, kind, owned.split(": ", 1)[1]))
    return lines, reds


def derive_stage_witnesses(data, where):
    """`(lines, reds)`: one `stage` line per step naming its exit item and that item's witness class, as
    `check_loop` and `check_witness_classes` read `data`; their refusal is the one red, as worded."""
    try:
        steps = check_loop(data, where)["step"]
        classes = {site: cls for site, cls, _by in check_witness_classes(data, where)}
    except LoopError as e:
        return [], ["%s: refused · %s" % (SAY, e)]
    return ["%s: stage · %s · exit %s · witness %s" % (SAY, s["tag"], s["exit"], classes.get(s["exit"], "none"))
            for s in steps], []


def write_stage_plant(case, parts):
    """`parts`, as read, with the break `case` names made in them, in place."""
    data = parts["definition"][0]
    if case == "unclaimed-leg":
        parts["leg"][next(iter(parts["leg"]))] = None
    elif case == "unclaimed-hook":
        first = next(k for k in parts["hook"] if " " in k)
        parts["hook_rows"] = [r for r in parts["hook_rows"]
                              if str(r.get("key")).replace("{prefix}/", parts["prefix"]) != first]
    elif case == "stale-hook":
        parts["hook_rows"] = parts["hook_rows"] + [{"key": "PreToolUse {prefix}/hooks/no-such-hook.js",
                                                    "stage": ["step.build"]}]
    elif case == "bad-tag":
        parts["dossier"][next(iter(parts["dossier"]))] = ["step.ship"]
    elif case == "stage-no-witness":
        exit_tag = next(s["exit"] for s in data["step"] if s.get("tag") == "step.build")
        next(r for r in data["item"] if r.get("tag") == exit_tag).pop("witness", None)
    elif case == "role-derived":
        next(w for w in data["workflow"] if w.get("name") == "build")["step"] = "step.test"
    elif case == "no-legs":
        parts["leg"] = {}


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="stage_coverage.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("--fixture", action="store_true", help="read the tree with one plant made in memory")
    ap.add_argument("--plant", choices=list(PLANTS))
    ap.add_argument("--selftest", action="store_true", help="the tree, then every plant")
    args = ap.parse_args(argv)
    if args.fixture != bool(args.plant) or (args.selftest and args.fixture):
        ap.error("--fixture takes --plant <case>, and --selftest takes neither")
    if args.selftest:
        cases = [("tree", [], 0, "%s: part · leg · " % SAY, "parts")]
        cases += [(p, ["--fixture", "--plant", p], PLANTS[p][1], PLANTS[p][2], PLANTS[p][3]) for p in PLANTS]
        return run_selftest_cases(main, cases, "%s: selftest" % SAY)
    try:
        parts = read_stage_parts()
    except LookupError as e:
        print("%s: unarmed · %s" % (SAY, e))
        return 2
    except (ValueError, LoopError) as e:
        print("%s: refused · %s" % (SAY, e))
        return 1
    if args.plant:
        print("%s: fixture · plant %s · %s" % (SAY, args.plant, PLANTS[args.plant][0]))
        write_stage_plant(args.plant, parts)
    data, where = parts["definition"]
    try:
        part_lines, part_reds = derive_part_claims(parts, check_loop(data, where))
    except LoopError:
        part_lines, part_reds = [], []  # the stage half prints the definition's refusal
    stage_lines, stage_reds = derive_stage_witnesses(data, where)
    for line in part_lines + stage_lines + part_reds + stage_reds:
        print(line)
    return 1 if part_reds or stage_reds else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
