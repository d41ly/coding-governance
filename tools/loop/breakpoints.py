#!/usr/bin/env python3
"""breakpoints.py — a build's breakpoints at any item boundary: reviews and owner gates one list (TOOL-dDeclaredLoop-19).

    python breakpoints.py list --build <slug> [--spec-audit] [--delegated-fork]
    python breakpoints.py stage --stage <stage> --build <slug> [--rev <rev>]
    python breakpoints.py --fixture --plant <case>
    python breakpoints.py --selftest

THE LIST. A breakpoint is a position at an item boundary, `before`, `at` or `after` an item tag, a
disposer, a `reviewer` or the `owner`, and a cause. `derive_breakpoints` is the one rule that lists them:
`review.<stage>`, per gov step in its order, places the stage's review of `STAGE_REVIEWS` under `owed`, and
under `owed-above-tier` where some unit's spec header reads Tier-2; under `opt-in` it places Design's spec
audit only where `--spec-audit` says the run pinned a dated opt-in, and nothing at the other four; `off`
places nothing. `autonomy` places an owner gate at `item.plan.exit` under `plan-only`, its default; adds one
at `item.design.exit` and one before `item.deploy.mandate` under `three-gates`; and adds one at each step's
`exit` item under `every-stage`. Each member of `review.breakpoints`, read at the build's composition pin by
`composition.py`'s `read_tag_policy`, places a reviewer `breakpoint` before it with cause `placement`. Under
`decisions.major = "author-owner-ratifies"`, given `--delegated-fork`, the owner item sits at
`item.build.ratify` with cause `ratification`. Each owner's request placed as a `breakpoint`
(TOOL-dPlacedRequest-5), a tracked disposition record of the build whose `Item` is `item.entry.place` and
`Disposition` `breakpoint`, read by `read_placed_breakpoints`, places a reviewer breakpoint: the name its
`Reason` opens with, `spec audit`, `gate review`, `closing review` or `landing review` at that review's
position, cause `owed` for `spec audit`, the audit the placement makes owed, and `placement` for the other
three, and `item <tag>` before that tag, cause `placement`. One position from two declarations is listed
once, and the list is sorted by the position item's place among the composed rows, then before, at, after.

THE RELEASE. An owner line's last field is its release: `authorization` for the plan gate, which the
unattended driver's `check_authorization` verifies at the pinned BASE; `released <stem> <word>` where the
owner's newest disposition record whose `Item` is the line's tag answers, read by `adapt.py`'s
`read_disposition_release`; else `held`. `run.on-owner-question` is not read here. An owner GATE of a build
opened before the placement reads `passed before placement` ahead of those answers (TOOL-dDeclaredLoop-53):
the placement is the oldest commit adding this module's own file, the opening the oldest adding the build's
README under the memory root, and the build was opened before it where both are found and the opening does
not contain the placement. Either not found reads as after, so the gate keeps its answer; the owner item
and the review lines always do. The README path takes the driver's root, `resolve_memory_root_source`'s:
the unattended driver reads each build's README at `$M/builds/<slug>/README.md` (`unattended.sh`'s
`readme_of`), `$M` the `MEMORY_ROOT` its `.unattended.conf` sets, and where `.memory-tree.conf` names a
root too the two are checked, not assumed, to agree, by the `records root:` refusal. Where an owner gate
stays `held` and no commit adds that README, `list` ends with `breakpoints: held · no commit adds <path> ·
root from <.unattended.conf|.memory-tree.conf|default>`, the conf the root came from (TOOL-dDeclaredLoop-64,
TOOL-dDeclaredLoop-75 S8, S30).

THE READS. `autonomy`, `decisions.major` and the five `review.<stage>` keys at the landed revision, or at
`--rev`, through the policy kit's `resolve_read` over one `read_revision`, the kit found by
`loop_parents.py`'s `read_policy_kit`; an unset `review.<stage>` reads the catalogue's derived default,
`owed` for `build` and `opt-in` for the other four. The steps are `loop_lib.py`'s `read_steps`, the
composed tags at the pin `loop_items.py`'s `read_composed_items`, and each unit's tier
`loop_transition.py`'s `read_build_headers`.

Exit: `list` prints one line per breakpoint and exits 0,

    breakpoint: <name> · <before|at|after> <item tag> · <reviewer|owner> · <cause>[ · <release>]

`stage` prints `breakpoints: stage <stage> · <value> · <owed|opt-in|not-owed>` and exits 0, `owed` under
`owed` or under `owed-above-tier` where a unit reads Tier-2, `not-owed` under `off` or `owed-above-tier`
with none, `opt-in` under `opt-in`. Both exit 2 printing `breakpoints: refused · <why>` on a policy refusal,
a slug outside `[A-Za-z0-9_-]+`, a stage outside the five, a value outside its key's set or a position the
composed rows do not declare, and `breakpoints: unarmed · <why>` where a kit does not resolve, never a
default. `--fixture --plant <case>` builds a scratch repository under the host temp directory, runs the case
and prints `held` or `MISSED`; `--selftest` runs every plant.

WHAT THIS DOES NOT CHECK: a fork's class, since no fork record carries one, so every fork the agent
resolved under delegation reads as major; whether the disposition record's writer is the owner, and
whether a placed breakpoint's request was the owner's own, which `placement.py check` held before it was
written; a review breakpoint firing, which is the main loop's `--trigger`.
"""
import argparse
import ast
import contextlib
import io
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from adapt import read_disposition_release  # noqa: E402
from composition import build_composition_base, read_step_composition, read_tag_policy  # noqa: E402
from loop_items import read_composed_items  # noqa: E402
from loop_lib import (SEG, LoopError, derive_conf_reads, derive_fixture_boundary, read_memory_tree,  # noqa: E402
                      read_steps, resolve_kit_dir, resolve_memory_root, resolve_memory_root_source,
                      run_selftest_cases)
from loop_parents import read_policy_kit  # noqa: E402
from loop_transition import (FX_BUILD, FX_SPEC, FX_UNIT, read_build_headers, read_build_specs,  # noqa: E402
                             read_transitions, write_transition_plant)
from loop_witness import (read_clean_env, read_git, remove_tree, resolve_bash, run_fixture_git,  # noqa: E402
                          write_fixture_files)
from position import check_is_ancestor  # noqa: E402

SAY = "breakpoints"
#: Which review each stage owns and where, the one typed fact (the flow-steps record).
STAGE_REVIEWS = {"plan": ("breakpoint", "before", "item.plan.exit"),
                 "design": ("spec audit", "after", "item.design.reason"),
                 "build": ("closing review", "after", "item.build.recommend"),
                 "test": ("gate review", "before", "item.test.exit"),
                 "deploy": ("landing review", "before", "item.deploy.notify")}
#: Each key's catalogued values; `review.<stage>`'s derived default, `owed` for Build, `opt-in` elsewhere.
REVIEW_VALUES = ("off", "opt-in", "owed", "owed-above-tier")
AUTONOMY_VALUES = ("plan-only", "three-gates", "every-stage")
MAJOR_VALUES = ("author-rubric", "author-owner-ratifies", "owner-only")
REVIEW_DEFAULTS = {"build": "owed"}
PLAN_GATE = "item.plan.exit"
RATIFY = "item.build.ratify"
RELATIONS = ("before", "at", "after")
PRE_PLACEMENT = "passed before placement"
#: The review breakpoints an owner's request may place, each the stage whose review it is (TOOL-dPlacedRequest-5 S1).
PLACED_REVIEWS = {row[0]: stage for stage, row in STAGE_REVIEWS.items() if stage != "plan"}
#: The disposition record that declares a placed breakpoint: its item, its word, and the `Reason` separator
#: before the request's content key; an item boundary's name opens `item `.
PLACED_ITEM, PLACED_WORD, PLACED_REQUEST, PLACED_TAG = "item.entry.place", "breakpoint", " · request ", "item "
read_memory_tree("id_grammar.py")
from id_grammar import SlugPattern  # noqa: E402  the slug grammar, bound at first use (TOOL-dTotalRecall-5 S7)
SLUG = SlugPattern(lambda g: g.BUILD_SLUG_RE.pattern)
PLANTS = {"values": "no policy file, then autonomy three-gates and every-stage, then review.test owed",
          "placed": "review.breakpoints naming item.build.unit-pass, then item.build.nothing, then the owner's "
                    "placed spec audit and placed item item.build.unit-pass, each a disposition record",
          "ratification": "decisions.major author-owner-ratifies with and without --delegated-fork, a disposition "
                          "record of item.build.ratify, author-rubric, and the driver's plan_state delegated mode",
          "stage": "review.design owed-above-tier over a Tier-2 and a Tier-1 spec, then no policy file",
          "driver-close": "the driver's --close over a delegated fork under author-owner-ratifies, then the "
                          "disposition record and the sourced check_owner_gates",
          "driver-optin": "the sourced driver's check_authorization under review.design owed and off, then none",
          "driver-plan": "the driver's --plan under autonomy three-gates, and --plan --paths, then the sourced "
                         "check_phase_gates past item.design.exit and item.build.exit, into and out of the conf's "
                         "adopter phase STAGING, before and after item.design.exit's disposition record",
          "pre-placement": "under autonomy three-gates, a build opened on history the kits' commit does not reach "
                           "and merged in, one opened after it and one uncommitted, listed by the scratch's own "
                           "module, then the first read by this tree's",
          "driver-pre-placement": "the same history with the driver copied beside the scratch's loop kit, its "
                                  "sourced check_owner_gates over the build opened before and the one after",
          "pre-placement-records-root": "the same history under MEMORY_ROOT=records, build tRec opened under "
                                        "records/builds/ and tWrong under memory/builds/, listed by the scratch's "
                                        "own module, then tWrong again with no policy file",
          "unattended-root": "the same history under the driver's conf naming MEMORY_ROOT=records and a memory "
                             "tree's conf naming none, build tRec opened under records/builds/ and tWrong under "
                             "memory/builds/, each listed by the scratch's own module",
          "confs-disagree": "the driver's conf naming MEMORY_ROOT=records beside the memory tree's memory, then "
                            "the list",
          "no-own-conf-read": "this module's own file graded on its syntax tree for a reader call or a conf name, "
                              "no scratch repository",
          "readded": "the scratch kits' commit, then this module taken out of the scratch and committed back"}


# ------------------------------------------------------------------------------------------ the rule
def derive_breakpoints(values, steps, tags, facts):
    """`[{name, relation, position, disposer, cause, release}]`: the breakpoints `values`, `{key: value}`,
    place over the gov `steps` and the composed `tags`, in composed order, given `facts`: `spec_audit` and
    `delegated` true or false, `tiers` each unit's tier and `placed` the breakpoints the owner's requests
    placed, `read_placed_breakpoints`' entries. An owner line's release is `authorization` at
    the plan gate and `held` elsewhere. ValueError naming the key on a value outside its set, and on a
    position `tags` lacks."""
    for key, allowed in [("autonomy", AUTONOMY_VALUES), ("decisions.major", MAJOR_VALUES)] + [
            ("review." + s, REVIEW_VALUES) for s in STAGE_REVIEWS]:
        if values.get(key) not in allowed:
            raise ValueError("%s is %r, none of %s" % (key, values.get(key), ", ".join(allowed)))
    out = []

    def write_line(name, relation, position, disposer, cause, why):
        """One breakpoint appended, unless one at that position and disposer stands."""
        if position not in tags:
            raise ValueError("%s places %s %s, an item the composed rows do not declare" % (why, relation, position))
        if any((b["relation"], b["position"], b["disposer"]) == (relation, position, disposer) for b in out):
            return
        release = "" if disposer == "reviewer" else "authorization" if position == PLAN_GATE else "held"
        out.append({"name": name, "relation": relation, "position": position, "disposer": disposer,
                    "cause": cause, "release": release})

    tier2 = "2" in facts.get("tiers", ())
    for step in steps:
        stage = step["tag"].rsplit(".", 1)[-1]
        if stage not in STAGE_REVIEWS:
            continue
        value, (name, relation, position) = values["review." + stage], STAGE_REVIEWS[stage]
        if value == "owed" or (value == "owed-above-tier" and tier2):
            write_line(name, relation, position, "reviewer", "owed", "review." + stage)
        elif value == "opt-in" and stage == "design" and facts.get("spec_audit"):
            write_line(name, relation, position, "reviewer", "opt-in", "review." + stage)
    autonomy = values["autonomy"]
    write_line("owner gate", "at", PLAN_GATE, "owner", "autonomy", "autonomy")
    if autonomy in ("three-gates", "every-stage"):
        write_line("owner gate", "at", "item.design.exit", "owner", "autonomy", "autonomy")
        write_line("owner gate", "before", "item.deploy.mandate", "owner", "autonomy", "autonomy")
    if autonomy == "every-stage":
        for step in steps:
            write_line("owner gate", "at", step["exit"], "owner", "autonomy", "autonomy")
    for member in values.get("review.breakpoints") or ():
        if member not in tags:
            raise ValueError("review.breakpoints names %s, an item the composed rows at the build's pin do not "
                             "declare" % member)
        write_line("breakpoint", "before", member, "reviewer", "placement", "review.breakpoints")
    for placed in facts.get("placed") or ():
        write_line(placed["name"], placed["relation"], placed["position"], "reviewer", placed["cause"],
                   "the placed breakpoint %s" % placed["id"])
    if values["decisions.major"] == "author-owner-ratifies" and facts.get("delegated"):
        write_line("owner item", "at", RATIFY, "owner", "ratification", "decisions.major")
    order = {t: n for n, t in enumerate(tags)}
    return sorted(out, key=lambda b: (order[b["position"]], RELATIONS.index(b["relation"])))


def render_breakpoint_line(b):
    """`breakpoint: <name> · <relation> <tag> · <disposer> · <cause>[ · <release>]`."""
    return "breakpoint: %s · %s %s · %s · %s%s" % (b["name"], b["relation"], b["position"], b["disposer"],
                                                   b["cause"], " · " + b["release"] if b["release"] else "")


# ------------------------------------------------------------------------------------------ the reads
def read_policy_values(root, rev=None):
    """`{key: value}` of `autonomy`, `decisions.major` and the five `review.<stage>` keys at `rev`, else the
    landed revision, over one policy read. ValueError on a refusal; LookupError where the kit does not resolve."""
    policy, _guard = read_policy_kit()
    try:
        read = policy.read_revision(str(root), rev)
    except policy.Refusal as e:
        raise ValueError("the policy file does not read: %s" % e) from None

    def read_value(key):
        """One key's value over the read; a `review.<stage>` key's derived default where the file sets none."""
        path = policy.parse_key(key)
        try:
            return policy.resolve_read(path, policy.read_catalogue_row(path, read["rows"]), read).value
        except policy.DerivedDefault:
            return REVIEW_DEFAULTS.get(key.rsplit(".", 1)[-1], "opt-in")
        except policy.Refusal as e:
            raise ValueError("%s does not resolve: %s" % (key, e)) from None

    # Each key a string literal at its read, the policy kit's reader coverage counting no other shape.
    return {"autonomy": read_value("autonomy"), "decisions.major": read_value("decisions.major"),
            "review.plan": read_value("review.plan"), "review.design": read_value("review.design"),
            "review.build": read_value("review.build"), "review.test": read_value("review.test"),
            "review.deploy": read_value("review.deploy")}


def check_slug(build):
    """ValueError where `build` is outside the slug grammar, before it reaches a path."""
    if not SLUG.fullmatch(build or ""):
        raise ValueError("the build %r is outside [A-Za-z0-9_-]+" % build)


def read_first_add(root, rel):
    """The oldest commit on `HEAD`'s history of `root` that adds `rel`, or None where none does or git refuses."""
    rc, out = read_git(root, "log", "--diff-filter=A", "--format=%H", "--", rel)
    found = out.split()
    return found[-1] if rc == 0 and found else None


def derive_placed_position(name):
    """`(relation, position, cause)` of a breakpoint an owner's request names `name` (TOOL-dPlacedRequest-5
    S1, S5): a review of `PLACED_REVIEWS` at its `STAGE_REVIEWS` position, cause `owed` for `spec audit` and
    `placement` for the other three; `item <tag>` before that tag, cause `placement`. ValueError naming any
    other name, an empty one included."""
    tag = name[len(PLACED_TAG):] if name.startswith(PLACED_TAG) else None
    if tag is not None:
        head, _dot, rest = tag.partition(".")
        if head == "item" and rest and all(SEG.fullmatch(s) for s in rest.split(".")):
            return "before", tag, "placement"
    elif name in PLACED_REVIEWS:
        _name, relation, position = STAGE_REVIEWS[PLACED_REVIEWS[name]]
        return relation, position, "owed" if PLACED_REVIEWS[name] == "design" else "placement"
    raise ValueError("breakpoint %r is none of %s, or item <tag>" % (name, ", ".join(PLACED_REVIEWS)))


def read_placed_breakpoints(build, root):
    """`[{id, name, relation, position, cause}]`, one per tracked disposition record of `build` whose `Item`
    is `PLACED_ITEM` and whose `Disposition` is `PLACED_WORD`, oldest first (TOOL-dPlacedRequest-5 S5): the
    name its `Reason` reads before ` · request `, `breakpoint` for an item boundary as `review.breakpoints`
    names one, and its position by `derive_placed_position`. ValueError naming a record whose name that
    refuses."""
    read_memory_tree("build_records.py")
    from build_records import read_disposition, read_records
    found = [r for r in read_records(root, {"MEMORY_ROOT": resolve_memory_root(root)}, "disposition", read_disposition)
             if r["build"] == build and not r["malformed"] and r.get("Item", "").strip("`") == PLACED_ITEM
             and r.get("Disposition", "").strip("`") == PLACED_WORD]
    out = []
    for rec in sorted(found, key=lambda r: (r["id"][:10], r["n"] or 0)):
        name = rec.get("Reason", "").strip("`").split(PLACED_REQUEST)[0].strip()
        try:
            relation, position, cause = derive_placed_position(name)
        except ValueError as e:
            raise ValueError("the placed breakpoint %s: %s" % (rec["id"], e)) from None
        out.append({"id": rec["id"], "name": "breakpoint" if name.startswith(PLACED_TAG) else name,
                    "relation": relation, "position": position, "cause": cause})
    return out


def read_build_item_rows(build, root):
    """The composed item rows at `build`'s composition pin, the rows its breakpoints are listed over and a
    placed item boundary is checked against."""
    return read_composed_items(root, read_step_composition(root, read_transitions(build, root))[0])


def read_breakpoints(build, root, spec_audit=False, delegated=False):
    """`derive_breakpoints` over `build`'s policy, steps, composed tags, tiers and placed breakpoints, each
    owner line's release
    read: `passed before placement` on each owner gate of a build opened before this module was placed,
    else `released <stem> <word>` where the owner's disposition record of its tag answers. An owner gate
    still `held` where the opening read found no commit adding the README carries `unopened`, that path,
    and `root_from`, the conf `resolve_memory_root_source` read the root from (TOOL-dDeclaredLoop-75 S8)."""
    check_slug(build)
    root = pathlib.Path(root).absolute()
    values = read_policy_values(root)
    values["review.breakpoints"] = read_tag_policy("review.breakpoints", root, build)
    tags = [r.get("tag") for r in read_build_item_rows(build, root)]
    tiers = [tier for _uid, _status, tier in read_build_headers(build, root)]
    out = derive_breakpoints(values, read_steps(KIT), tags,
                             {"spec_audit": spec_audit, "delegated": delegated, "tiers": tiers,
                              "placed": read_placed_breakpoints(build, root)})
    early, unopened, source = False, None, None
    if any(b["name"] == "owner gate" for b in out):   # TOOL-dDeclaredLoop-53: opened before the placement
        try:
            placement = read_first_add(root, (KIT / "breakpoints.py").resolve().relative_to(root.resolve()).as_posix())
        except ValueError:
            placement = None
        if placement:
            mem, source = resolve_memory_root_source(root)
            readme = "%s/builds/%s/README.md" % (mem, build)
            opening = read_first_add(root, readme)
            early = bool(opening) and not check_is_ancestor(root, placement, opening)
            unopened = None if opening else readme   # TOOL-dDeclaredLoop-64: the path a hold looked for
    for b in out:
        if early and b["name"] == "owner gate":
            b["release"] = PRE_PLACEMENT
        elif b["release"] == "held":
            hit = read_disposition_release(root, build, b["position"], ())
            if hit:
                b["release"] = "released %s %s" % hit
            elif unopened and b["name"] == "owner gate":
                b["unopened"], b["root_from"] = unopened, source
    return out


def read_stage_review(build, root, stage, rev=None):
    """`(value, answer)` of `review.<stage>` at `rev`, else the landed revision: `owed`, `not-owed` or
    `opt-in`, `owed-above-tier` reading `owed` where a unit of `build` reads Tier-2."""
    check_slug(build)
    if stage not in STAGE_REVIEWS:
        raise ValueError("--stage %s is none of %s" % (stage, ", ".join(STAGE_REVIEWS)))
    value = read_policy_values(root, rev)["review." + stage]
    if value not in REVIEW_VALUES:
        raise ValueError("review.%s is %r, none of %s" % (stage, value, ", ".join(REVIEW_VALUES)))
    if value == "owed-above-tier":
        tiered = any(tier == "2" for _uid, _status, tier in read_build_headers(build, root))
        return value, "owed" if tiered else "not-owed"
    return value, {"owed": "owed", "off": "not-owed", "opt-in": "opt-in"}[value]




# ------------------------------------------------------------------------------------------ the plants
def write_pre_placement_plant(memory_root="memory", opened=("memory/builds/tPre/README.md",), confs=None):
    """`(top, the scratch's loop kit)`: `build_scratch_tree`'s kits commit, the placement; each README of
    `opened` added on a root commit it does not precede and merged in; then `confs`, `{path: text}`, else
    `.memory-tree.conf` at `MEMORY_ROOT=<memory_root>`, with `autonomy = "three-gates"`,
    `decisions.major = "author-owner-ratifies"` and build `tPost` committed; and `tNone`'s README written,
    never committed, both under `memory_root`."""
    confs = confs or {".memory-tree.conf": "MEMORY_ROOT=%s\n" % memory_root}
    from loop_items import POLICY_FILE, build_scratch_tree, derive_definition_rel
    top = build_scratch_tree()[0]
    readme = memory_root + "/builds/%s/README.md"
    try:
        run_fixture_git(top, "branch", "-M", "main")   # the policy kit's landed read, with no remote
        run_fixture_git(top, "checkout", "-q", "--orphan", "pre")
        run_fixture_git(top, "rm", "-r", "-q", "--cached", ".")
        write_fixture_files(top, {rel: "# %s\n" % rel.split("/")[-2] for rel in opened})
        run_fixture_git(top, "add", *opened)
        run_fixture_git(top, "commit", "-q", "-m", "builds opened on history the placement does not reach")
        run_fixture_git(top, "checkout", "-q", "-f", "main")
        run_fixture_git(top, "merge", "-q", "--allow-unrelated-histories", "-m", "the builds merged in", "pre")
        write_fixture_files(top, {readme % "tPost": "# tPost\n", POLICY_FILE: 'autonomy = "three-gates"\n\n'
                                  '[decisions]\nmajor = "author-owner-ratifies"\n', **confs})
        run_fixture_git(top, "add", readme % "tPost", POLICY_FILE, *confs)
        run_fixture_git(top, "commit", "-q", "-m", "tPost opened after the placement, three gates")
        write_fixture_files(top, {readme % "tNone": "# tNone\n"})
        return top, top / pathlib.PurePosixPath(derive_definition_rel()).parent
    except BaseException:
        remove_tree(top)
        raise


def run_sourced(repo, script, driver=None):
    """`(exit, output)` of `script` run by bash in `repo` after the unattended `driver` is sourced, this
    tree's where None; LookupError where the driver or a bash to run it does not resolve."""
    driver = driver or resolve_kit_dir("unattended", "unattended.sh", KIT) / "unattended.sh"
    bash = resolve_bash(driver)
    if bash is None:
        raise LookupError("no bash can run %s" % driver.as_posix())
    env = {k: v for k, v in read_clean_env().items() if k not in ("GOV_POSITION_STATES", "GOV_DEFAULT_BRANCH")}
    p = subprocess.run([bash, "-c", '. "$1" || exit 2; ' + script, "_", driver.as_posix()],
                       cwd=str(repo), capture_output=True, text=True, encoding="utf-8", errors="replace", env=env,
                       timeout=900)
    return p.returncode, p.stdout + p.stderr


def run_breakpoint_plant(case):
    """One plant: its lines, then `breakpoints: fixture · <case> · held` or `MISSED <why>`; 0 held, 1 missed,
    2 where a kit does not resolve."""
    top = pathlib.Path(tempfile.mkdtemp(prefix="loop-breakpoints-")).absolute()
    misses, here = [], os.getcwd()
    try:
        print("%s: fixture · plant %s · %s" % (SAY, case, PLANTS[case]))

        def check(cond, why):
            """A miss named where `cond` does not hold."""
            if not cond:
                misses.append(why)

        def run_verb(repo, argv):
            """`(exit, lines)` of this module's `main(argv)` run in process at `repo`, echoed."""
            out = io.StringIO()
            os.chdir(repo)
            try:
                with contextlib.redirect_stdout(out):
                    rc = main(argv)
            finally:
                os.chdir(here)
            lines = out.getvalue().splitlines()
            print("%s: fixture · %s · exit %d · %s" % (SAY, " ".join(argv), rc, " / ".join(lines) or "nothing"))
            return rc, lines

        def write_policy(repo, text, message):
            """The policy file `text`, removed where None, committed, and pushed where `repo` has a remote."""
            path = pathlib.Path(repo, ".governance", "policy.toml")
            if text is None:
                path.unlink(missing_ok=True)
            else:
                write_fixture_files(repo, {".governance/policy.toml": text})
            run_fixture_git(repo, "add", "-A")
            run_fixture_git(repo, "commit", "-q", "--allow-empty", "-m", message)
            if run_fixture_git(repo, "remote"):
                run_fixture_git(repo, "push", "-q", run_fixture_git(repo, "remote"), "main")

        def check_owner_lines(lines):
            """A miss for each owner line ending in no release, and for an owner item not caused by ratification."""
            for ln in lines:
                if " · owner · " in ln and not re.search(r" · (authorization|held|released \S+ \S+|%s)$"
                                                         % PRE_PLACEMENT, ln):
                    misses.append("an owner line names no release: %s" % ln)
                if ln.startswith("breakpoint: owner item ") and " · ratification · " not in ln:
                    misses.append("the owner item's cause is not ratification: %s" % ln)

        def write_disposition_record(repo, build, unit, item=RATIFY, word="ratified"):
            """The owner's committed disposition record of `item`, the owner item by default, `word`: its stem."""
            read_memory_tree("build_records.py")
            from build_records import write_disposition
            rel = write_disposition(repo, build, unit, item, word, "terminal")
            run_fixture_git(repo, "add", "-A")
            run_fixture_git(repo, "commit", "-q", "-m", "the owner's disposition")
            return pathlib.PurePosixPath(rel).stem

        plan = "breakpoint: owner gate · at item.plan.exit · owner · autonomy · authorization"
        closing = "breakpoint: closing review · after item.build.recommend · reviewer · owed"
        gate = "breakpoint: owner gate · %s %s · owner · autonomy · held"
        owner = "breakpoint: owner item · at item.build.ratify · owner · ratification · "
        listed = ["list", "--build", FX_BUILD]
        if case in ("values", "ratification", "stage", "confs-disagree"):
            write_transition_plant(top, "default")
        if case == "values":   # AC1, AC7
            three = [plan, gate % ("at", "item.design.exit"), closing, gate % ("before", "item.deploy.mandate")]
            every = three[:3] + [gate % ("at", "item.build.exit"), gate % ("at", "item.test.exit"), three[3],
                                 gate % ("at", "item.deploy.close")]
            for policy, owed in ((None, [plan, closing]), ('autonomy = "three-gates"\n', three),
                                 ('autonomy = "every-stage"\n', every),
                                 ('[review]\ntest = "owed"\n',
                                  [plan, closing, "breakpoint: gate review · before item.test.exit · reviewer · owed"])):
                write_policy(top, policy, "the policy %r" % policy)
                rc, lines = run_verb(top, listed)
                check(rc == 0 and lines == owed, "under %r the list read %s" % (policy, lines))
                check_owner_lines(lines)
        elif case == "placed":   # AC2, over a tree holding this tree's kits, whose tag resolver reads a member
            repo = build_composition_base()[0]
            try:
                write_policy(repo, '[review]\nbreakpoints = ["item.build.unit-pass"]\n', "placed")
                rc, lines = run_verb(repo, listed)
                check(rc == 0 and lines == [plan, "breakpoint: breakpoint · before item.build.unit-pass · reviewer · "
                                                  "placement", closing], "the placed member read %s" % lines)
                write_policy(repo, '[review]\nbreakpoints = ["item.build.nothing"]\n', "undeclared")
                rc, lines = run_verb(repo, listed)
                check(rc == 2 and len(lines) == 1 and lines[0].startswith("%s: refused · " % SAY)
                      and "review.breakpoints" in lines[0] and "item.build.nothing" in lines[0],
                      "the undeclared member read exit %d, %s" % (rc, lines))
                # TOOL-dPlacedRequest-5 AC5: the owner's placed breakpoints, each a disposition record
                read_memory_tree("build_records.py")
                from build_records import write_disposition
                for name in ("spec audit", "item item.build.unit-pass"):
                    write_disposition(repo, FX_BUILD, FX_UNIT, PLACED_ITEM, PLACED_WORD, "prompt",
                                      "%s%s3f9c2a7d01be" % (name, PLACED_REQUEST))
                write_policy(repo, None, "the owner's placed breakpoints")
                rc, lines = run_verb(repo, listed)
                check(rc == 0 and lines == [plan, "breakpoint: spec audit · after item.design.reason · reviewer · owed",
                                            "breakpoint: breakpoint · before item.build.unit-pass · reviewer · "
                                            "placement", closing], "the placed records read %s" % lines)
                write_disposition(repo, FX_BUILD, FX_UNIT, PLACED_ITEM, PLACED_WORD, "prompt",
                                  "design review%s3f9c2a7d01be" % PLACED_REQUEST)
                write_policy(repo, None, "a placed breakpoint naming no review")
                rc, lines = run_verb(repo, listed)
                check(rc == 2 and len(lines) == 1 and "the placed breakpoint " in lines[0]
                      and "'design review' is none of" in lines[0], "the unknown name read exit %d, %s" % (rc, lines))
            finally:
                remove_tree(repo)
        elif case == "ratification":   # AC3, AC4, AC7
            write_policy(top, '[decisions]\nmajor = "author-owner-ratifies"\n', "ratifies")
            rc, lines = run_verb(top, listed + ["--delegated-fork"])
            check(rc == 0 and owner + "held" in lines, "the delegated fork's list read %s" % lines)
            check_owner_lines(lines)
            rc, lines = run_verb(top, listed)
            check(rc == 0 and not any("owner item" in ln for ln in lines), "with no delegated fork it read %s" % lines)
            stem = write_disposition_record(top, FX_BUILD, FX_UNIT)
            rc, lines = run_verb(top, listed + ["--delegated-fork"])
            check(rc == 0 and owner + "released %s ratified" % stem in lines, "the released item read %s" % lines)
            check_owner_lines(lines)
            write_policy(top, '[decisions]\nmajor = "author-rubric"\n', "rubric")
            rc, lines = run_verb(top, listed + ["--delegated-fork"])
            check(rc == 0 and not any("owner item" in ln for ln in lines), "under author-rubric it read %s" % lines)
            fork = "## 8. Open questions\n\n- **F1 — which way?** Options: (a) or (b). %s: (a).\n"
            forks = {"delegated": "RESOLVED (agent, 2026-01-01, delegated)", "owner": "RESOLVED (owner, 2026-01-01)",
                     "quoted": "`RESOLVED (agent, 2026-01-01, delegated)` quoted, RESOLVED (owner, 2026-01-01)"}
            write_fixture_files(top, {"s/2026-01-01-spec-%s.md" % k: fork % v for k, v in forks.items()})
            for name, owed in (("delegated", "DELEGATED"), ("owner", "NONE"), ("quoted", "NONE")):
                for cutoff in ("", "2025-01-01"):
                    rc, out = run_sourced(top, 'plan_state s/2026-01-01-spec-%s.md "%s" delegated' % (name, cutoff))
                    print("%s: fixture · plan_state %s, cutoff %s · %s" % (SAY, name, cutoff or "none", out.strip()))
                    check(out.strip() == owed, "plan_state over the %s fork, cutoff %r, read %r" % (name, cutoff, out))
        elif case == "stage":   # AC6
            header = "# %s — a unit\n\n**Status:** INPROGRESS · rev-1 · 2026-01-01 · node a · Tier-%d\n"
            for tier, owed in ((2, "owed"), (1, "not-owed")):
                write_fixture_files(top, {FX_SPEC: header % (FX_UNIT, tier)})
                write_policy(top, '[review]\ndesign = "owed-above-tier"\n', "Tier-%d" % tier)
                rc, lines = run_verb(top, ["stage", "--stage", "design", "--build", FX_BUILD])
                check(rc == 0 and lines == ["%s: stage design · owed-above-tier · %s" % (SAY, owed)],
                      "over a Tier-%d spec it read %s" % (tier, lines))
            write_policy(top, None, "no policy")
            for stage, owed in (("design", "opt-in"), ("build", "owed")):
                rc, lines = run_verb(top, ["stage", "--stage", stage, "--build", FX_BUILD])
                check(rc == 0 and lines == ["%s: stage %s · %s · %s" % (SAY, stage, owed, owed)],
                      "with no policy file %s read %s" % (stage, lines))
            heads, specs = read_build_headers(FX_BUILD, top), read_build_specs(FX_BUILD, top)
            print("%s: fixture · headers %s · specs %s" % (SAY, heads, specs))
            check(heads == [(FX_UNIT, "INPROGRESS", "1")] and specs == [(FX_UNIT, "INPROGRESS")],
                  "read_build_headers %s beside read_build_specs %s" % (heads, specs))
        elif case == "confs-disagree":   # TOOL-dDeclaredLoop-72 AC3: two confs naming two roots
            write_fixture_files(top, {".unattended.conf": "MEMORY_ROOT=records\n"})
            rc, lines = run_verb(top, listed)
            owed = ("%s: refused · records root: .unattended.conf says records, .memory-tree.conf says memory — the "
                    "driver writes under records" % SAY)
            check(rc == 2 and lines == [owed], "the list read exit %d, %s" % (rc, lines))
        elif case == "readded":   # TOOL-dDeclaredLoop-67 AC31 (S48): the placement is the oldest add, never the newest
            from loop_items import build_scratch_tree, derive_definition_rel
            scratch = build_scratch_tree()[0]
            try:
                module = (pathlib.PurePosixPath(derive_definition_rel()).parent / pathlib.Path(__file__).name).as_posix()
                placement = read_first_add(scratch, module)
                run_fixture_git(scratch, "rm", "-q", "--", module)
                run_fixture_git(scratch, "commit", "-q", "-m", "the module taken out")
                run_fixture_git(scratch, "checkout", "-q", "HEAD~1", "--", module)
                run_fixture_git(scratch, "commit", "-q", "-m", "the module committed back")
                adds = read_git(scratch, "log", "--diff-filter=A", "--format=%H", "--", module)[1].split()
                first = read_first_add(scratch, module)
                print("%s: fixture · readded · %d add(s) · placement %s · read %s" % (
                    SAY, len(adds), (placement or "none")[:8], (first or "none")[:8]))
                check(len(adds) == 2, "the scratch history holds %d add(s) of %s, not two" % (len(adds), module))
                check(placement is not None and first == placement,
                      "the placement read %s after the re-add, not the first add %s" % (first, placement))
            finally:
                remove_tree(scratch)
        elif case == "no-own-conf-read":   # TOOL-dDeclaredLoop-76 AC1: this module's own file, no scratch tree
            own = pathlib.Path(__file__)
            try:
                bound = [f.name for f in derive_fixture_boundary(ast.parse(own.read_text(encoding="utf-8"), str(own)))]
                hits = derive_conf_reads(own)
            except SyntaxError as e:
                bound, hits = [], []
                check(False, "%s does not parse: %s" % (own.name, e))
            except LoopError as e:   # TOOL-dDeclaredLoop-86 S21: a missing loop_lib or a stale tree_lib, a miss
                bound, hits = [], []
                check(False, str(e))
            print("%s: fixture · fixture boundary: %d functions — %s" % (SAY, len(bound), ", ".join(bound) or "none"))
            for line, kind in hits:
                print("%s: fixture · conf read · %s:%d %s" % (SAY, own.name, line, kind))
            check(not hits, "%d conf read(s) in %s" % (len(hits), own.name))
        elif case in ("pre-placement", "driver-pre-placement", "pre-placement-records-root", "unattended-root"):
            # TOOL-dDeclaredLoop-53 AC1 to AC4; TOOL-dDeclaredLoop-64 AC1 to AC3 under the records root;
            # TOOL-dDeclaredLoop-72 AC2 under the root the driver's conf names
            readme = "%s/builds/%s/README.md"
            records = case == "pre-placement-records-root"
            if case == "unattended-root":
                scratch, kit = write_pre_placement_plant("records", (readme % ("records", "tRec"),
                                                                     readme % ("memory", "tWrong")), {
                    ".unattended.conf": "MEMORY_ROOT=records\n", ".memory-tree.conf": ""})
            else:
                scratch, kit = (write_pre_placement_plant("records", (readme % ("records", "tRec"),
                                                                     readme % ("memory", "tWrong")))
                                if records else write_pre_placement_plant())
            try:
                three = [plan, gate % ("at", "item.design.exit"), closing, gate % ("before", "item.deploy.mandate")]
                pre = "breakpoint: owner gate · %s %s · owner · autonomy · " + PRE_PLACEMENT
                # TOOL-dDeclaredLoop-75 AC8: the held line names the conf its root came from
                unopened = "%s: held · no commit adds %s · root from %%s" % (SAY, readme)

                def run_scratch_breakpoints(build, *flags):
                    """`(exit, lines)` of the scratch's own module listing `build` in the scratch, echoed."""
                    p = subprocess.run([sys.executable, str(kit / "breakpoints.py"), "list", "--build", build,
                                        *flags], cwd=str(scratch), capture_output=True, text=True,
                                       encoding="utf-8", errors="replace",
                                       env=read_clean_env(PYTHONIOENCODING="utf-8"), timeout=300)
                    lines = p.stdout.splitlines()
                    print("%s: fixture · scratch list %s · exit %d · %s" % (
                        SAY, " ".join((build,) + flags), p.returncode, " / ".join(lines) or p.stderr.strip()))
                    return p.returncode, lines

                if case == "unattended-root":
                    rc, lines = run_scratch_breakpoints("tRec")
                    check(rc == 0 and lines == [pre % ("at", PLAN_GATE), pre % ("at", "item.design.exit"), closing,
                                                pre % ("before", "item.deploy.mandate")],
                          "the build opened under the driver's records root read %s" % lines)
                    check_owner_lines(lines)
                    rc, lines = run_scratch_breakpoints("tWrong")
                    check(rc == 0 and lines == three + [unopened % ("records", "tWrong", ".unattended.conf")],
                          "the build opened under memory/ beneath the driver's records root read %s" % lines)
                elif records:
                    rc, lines = run_scratch_breakpoints("tRec")   # AC1
                    check(rc == 0 and lines == [pre % ("at", PLAN_GATE), pre % ("at", "item.design.exit"), closing,
                                                pre % ("before", "item.deploy.mandate")],
                          "the build opened under the records root read %s" % lines)
                    check_owner_lines(lines)
                    rc, lines = run_scratch_breakpoints("tWrong")   # AC2
                    check(rc == 0 and lines == three + [unopened % ("records", "tWrong", ".memory-tree.conf")],
                          "the build opened under memory/ in a records tree read %s" % lines)
                    check_owner_lines(lines)
                    write_policy(scratch, None, "no policy file")   # AC3
                    rc, lines = run_scratch_breakpoints("tWrong")
                    check(rc == 0 and lines == [plan, closing], "tWrong with no policy file read %s" % lines)
                elif case == "pre-placement":
                    rc, lines = run_scratch_breakpoints("tPre")   # AC1
                    check(rc == 0 and lines == [pre % ("at", PLAN_GATE), pre % ("at", "item.design.exit"), closing,
                                                pre % ("before", "item.deploy.mandate")],
                          "the build opened before the placement read %s" % lines)
                    check_owner_lines(lines)
                    rc, lines = run_scratch_breakpoints("tPost")
                    check(rc == 0 and lines == three, "the build opened after the placement read %s" % lines)
                    for build in ("tPre", "tPost"):   # AC2
                        rc, lines = run_scratch_breakpoints(build, "--delegated-fork")
                        check(rc == 0 and owner + "held" in lines and closing in lines,
                              "%s with a delegated fork read %s" % (build, lines))
                    rc, lines = run_scratch_breakpoints("tNone")   # AC3
                    check(rc == 0 and lines == three + [unopened % ("memory", "tNone", ".memory-tree.conf")],
                          "the build whose README no commit adds read %s" % lines)
                    try:
                        lines = [render_breakpoint_line(b) for b in read_breakpoints("tPre", scratch)]
                    except ValueError as e:
                        lines = ["refused: %s" % e]
                    print("%s: fixture · this tree's module over the scratch, tPre · %s" % (SAY, " / ".join(lines)))
                    check(lines == three, "this tree's module, outside the scratch, read tPre as %s" % lines)
                else:   # AC4
                    src = resolve_kit_dir("unattended", "unattended.sh", KIT)
                    shutil.copytree(src, kit.parent / src.name, ignore=shutil.ignore_patterns("__pycache__"))
                    root = next((d for d in (KIT, *KIT.parents) if (d / ".git").exists()), KIT)
                    if not (root / ".unattended.conf").is_file():
                        raise LookupError("the driver plant copies .unattended.conf from %s, which holds none"
                                          % root.as_posix())
                    write_fixture_files(scratch, {".unattended.conf": (root / ".unattended.conf").read_text(
                        encoding="utf-8") + '\nSPEC_TOKENS_CLI=""\nRUN_CLAIMS="off"\n'})
                    for build, owed, needle in (("tPre", 0, ""), ("tPost", 1, "item.design.exit")):
                        rc, out = run_sourced(scratch, "load_driver_conf && check_owner_gates %s" % build,
                                              kit.parent / src.name / "unattended.sh")
                        print("%s: fixture · the scratch's check_owner_gates %s · exit %d · %s" % (
                            SAY, build, rc, out.strip().replace("\n", " / ")[:600]))
                        check(rc == owed and (not owed or "UNATTENDED check 82 FAILED" in out and needle in out),
                              "check_owner_gates %s exited %d, owed %d naming %r" % (build, rc, owed, needle))
            finally:
                remove_tree(scratch)
        else:
            from position import FX_IDS, FX_SLUG, run_driver, write_position_plant
            root = next((d for d in (KIT, *KIT.parents) if (d / ".git").exists()), KIT)
            repo = write_position_plant(top, "plan-line", root)[0]
            with open(repo / ".unattended.conf", "a", encoding="utf-8", newline="\n") as fh:
                fh.write('\nSPEC_TOKENS_CLI=""\nRUN_CLAIMS="off"\n')
                if case == "driver-plan":   # TOOL-dDeclaredLoop-63 AC2: an adopter phase the loop kit has no row of
                    fh.write('PHASES_EXTRA="STAGING"\n')
            if case == "driver-close":   # AC3
                spec = repo / "memory" / "builds" / FX_SLUG / "spec" / ("2026-01-01-spec-%s.md" % FX_IDS[0])
                text = spec.read_text(encoding="utf-8").replace(
                    "## 8. Open questions\nnone\n", "## 8. Open questions\n- **F1 — which way?** Options: (a) or (b). "
                                                    "RESOLVED (agent, 2026-01-01, delegated): (a).\n")
                write_fixture_files(repo, {spec.relative_to(repo).as_posix(): text})
                write_policy(repo, '[decisions]\nmajor = "author-owner-ratifies"\n', "a delegated fork the owner ratifies")
                out, rc = run_driver(repo, "--close", FX_SLUG)
                print("%s: fixture · --close · exit %d · %s" % (SAY, rc, out.strip().replace("\n", " / ")[:600]))
                check(rc == 1 and "UNATTENDED check 82 FAILED" in out and RATIFY in out,
                      "--close over the delegated fork was not refused naming %s" % RATIFY)
                write_disposition_record(repo, FX_SLUG, FX_IDS[0])
                rc, out = run_sourced(repo, "load_driver_conf && check_owner_gates %s" % FX_SLUG)
                print("%s: fixture · check_owner_gates · exit %d · %s" % (SAY, rc, out.strip().replace("\n", " / ")))
                check(rc == 0, "check_owner_gates after the disposition record exited %d" % rc)
            elif case == "driver-optin":   # AC5
                readme = repo / "memory" / "builds" / FX_SLUG / "README.md"
                bare = readme.read_text(encoding="utf-8")
                keyed = bare.replace("slug: %s\n" % FX_SLUG, "slug: %s\nspec-audit: 2026-01-01\n" % FX_SLUG, 1)
                for policy, text, owed in (('[review]\ndesign = "owed"\n', bare, None),
                                           ('[review]\ndesign = "off"\n', keyed, ("", "policy")),
                                           (None, keyed, ("2026-01-01", "readme"))):
                    write_fixture_files(repo, {readme.relative_to(repo).as_posix(): text})
                    write_policy(repo, policy, "the opt-in under %r" % policy)
                    owed = owed or (run_fixture_git(repo, "show", "-s", "--format=%cs", "HEAD"), "policy")
                    rc, out = run_sourced(repo, 'load_driver_conf; check_authorization %s "$(git rev-parse HEAD)" >/dev/null; printf '
                                                '"\\nauth=%%s from=%%s\\n" "$AUTH_SPEC_AUDIT" "$AUTH_SPEC_AUDIT_FROM"'
                                                % FX_SLUG)
                    said = out.strip().splitlines()[-1] if out.strip() else ""
                    print("%s: fixture · check_authorization under %r · %s" % (SAY, policy, said))
                    check(said == "auth=%s from=%s" % owed, "under %r it read %r, owed %s" % (policy, said, owed))
            elif case == "driver-plan":   # AC8
                write_policy(repo, 'autonomy = "three-gates"\n', "three gates")
                out, rc = run_driver(repo, "--plan", FX_SLUG)
                said = [ln.rstrip("\r") for ln in out.splitlines()]
                print("%s: fixture · --plan · exit %d · %s" % (SAY, rc, " / ".join(said[-8:])))
                at = next((n for n, ln in enumerate(said) if ln.startswith("frontier: ")), None)
                _rc, lines = run_verb(repo, ["list", "--build", FX_SLUG])
                check(rc == 0 and at is not None and said[at - 1].startswith("next: ") and said[at + 1:] == lines
                      and len(lines) == 4, "--plan's lines after frontier: are not the list's four")
                out, rc = run_driver(repo, "--plan", FX_SLUG, "--paths")
                check(rc == 0 and "breakpoint: " not in out, "--plan --paths printed a breakpoint: line")
                # TOOL-dDeclaredLoop-52 AC5: the --phase hold reads only the gates at the exits a move crosses
                def check_sourced(call, owed, needle=""):
                    """A miss where the sourced `call`, given the slug, does not exit `owed`, or exits 1 naming no
                    `needle` in a check 82 refusal."""
                    call = call % FX_SLUG
                    rc, out = run_sourced(repo, "load_driver_conf && " + call)
                    print("%s: fixture · %s · exit %d · %s" % (SAY, call, rc, out.strip().replace("\n", " / ")[:600]))
                    check(rc == owed and (not owed or "UNATTENDED check 82 FAILED" in out and needle in out),
                          "%s exited %d, owed %d naming %r" % (call, rc, owed, needle))

                check_sourced("check_phase_gates %s SPECCING BUILDING", 1, "item.design.exit")
                check_sourced("check_phase_gates %s BUILDING VERIFYING", 0)
                # TOOL-dDeclaredLoop-63 AC2: the conf's adopter phase STAGING, which no phase row reads, is
                # entered crossing nothing and left counting from the first step, so the held design exit
                # holds it; observed before the record below releases that exit
                check_sourced("check_phase_gates %s REVIEWING STAGING", 0)
                check_sourced("check_phase_gates %s STAGING BUILDING", 1, "item.design.exit")
                write_disposition_record(repo, FX_SLUG, FX_IDS[0], "item.design.exit", "recorded")
                check_sourced("check_phase_gates %s SPECCING BUILDING", 0)
                check_sourced("check_owner_gates %s", 1, "held at item.deploy.mandate;")
    except LookupError as e:
        print("%s: fixture · %s · unarmed: %s" % (SAY, case, e))
        return 2
    finally:
        os.chdir(here)
        remove_tree(top)
    print("%s: fixture · %s · %s" % (SAY, case, "held" if not misses else "MISSED " + "; ".join(misses)))
    return 0 if not misses else 1


def run_selftest():
    """Every plant, each held."""
    cases = [(c, ["--fixture", "--plant", c], 0, "%s: fixture · %s · held" % (SAY, c), "") for c in PLANTS]
    return run_selftest_cases(main, cases, "%s: selftest" % SAY)


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if argv == ["--selftest"]:
        return run_selftest()
    if len(argv) == 3 and argv[:2] == ["--fixture", "--plant"] and argv[2] in PLANTS:
        return run_breakpoint_plant(argv[2])
    root = pathlib.Path.cwd()
    try:
        if argv[:1] == ["list"]:
            ap = argparse.ArgumentParser(prog="breakpoints.py list", description="a build's breakpoints, one per line")
            ap.add_argument("--build", required=True)
            ap.add_argument("--spec-audit", action="store_true")
            ap.add_argument("--delegated-fork", action="store_true")
            args = ap.parse_args(argv[1:])
            found = read_breakpoints(args.build, root, args.spec_audit, args.delegated_fork)
            for b in found:
                print(render_breakpoint_line(b))
            held = next((b for b in found if b.get("unopened")), None)
            if held:   # TOOL-dDeclaredLoop-64: its own head, never an owner line's bytes; 75 S8: the root's source
                print("%s: held · no commit adds %s · root from %s" % (SAY, held["unopened"], held["root_from"]))
            return 0
        if argv[:1] == ["stage"]:
            ap = argparse.ArgumentParser(prog="breakpoints.py stage", description="one stage's review reading")
            for flag in ("--stage", "--build"):
                ap.add_argument(flag, required=True)
            ap.add_argument("--rev")
            args = ap.parse_args(argv[1:])
            value, answer = read_stage_review(args.build, root, args.stage, args.rev)
            print("%s: stage %s · %s · %s" % (SAY, args.stage, value, answer))
            return 0
    except LookupError as e:
        print("%s: unarmed · %s" % (SAY, str(e).replace("\n", " ")))
        return 2
    except (ValueError, OSError) as e:
        print("%s: refused · %s" % (SAY, str(e).replace("\n", " ")))
        return 2
    print("usage: python breakpoints.py list --build <slug> [--spec-audit] [--delegated-fork] | stage --stage <%s> "
          "--build <slug> [--rev <rev>] | --fixture --plant <%s> | --selftest" % ("|".join(STAGE_REVIEWS), "|".join(PLANTS)),
          file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
