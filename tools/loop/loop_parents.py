#!/usr/bin/env python3
"""loop_parents.py — a dependent build's route on its parent's withdrawal (TOOL-dDeclaredLoop-15).

    python loop_parents.py route --build <slug> --state <state> [--root <path>]
    python loop_parents.py --selftest
    python loop_parents.py --fixture --plant <case> [--value <v>] [--state <s>]

`read_withdrawn_parents(build, root)` reads the slugs of the build README's `parents:` or `depends-on:`
front matter, the `after` targets of the memory-tree kit's `parse_relations` over its `parse_front_matter`
(TOOL-dTotalRecall-6 S9), the builds folder `<root>/<records root>/builds` by
the loop kit's `resolve_memory_root` (TOOL-dDeclaredLoop-116). A parent reads withdrawn on today's
stand-in for its
`withdrawn` post: its run-state file `RUN.md`, read at the tip of `refs/remotes/<remote>/<run-branch>`
where that ref holds it, else in the tree (TOOL-dDeclaredLoop-56 S39), has a run fact `phase` that
`loop_table.py`'s `derive_phase_position` maps, with `halt-code` and `hold-code` where set, to the state
`withdrawn` (S18), so an `ABORTED` parent halted `budget-exhausted` reads `incomplete`; a phase no row
reads is an adopter phase where the `PHASES_EXTRA` of `<root>`'s `.unattended.conf` names it, read with
`tree=root` (TOOL-dDeclaredLoop-70), and reads no state, as the plant `parent-in-extra-phase` shows. The facts are
read by the policy kit's `read_run_fact`, the remote by `claims.py`'s inline ladder and the branch by the
tree copy's `run-branch:` fact. A phase the map refuses exits 2 `unanswered` naming the parent. A parent
with no run-state file anywhere prints `parent <p> · not withdrawn (no run record)` before the route.

`derive_parent_route(build, state, root)` answers as `deps.on-parent-withdrawn`, read by the policy
kit's `resolve` at the landed revision, says. The move is the definition's parent row,
`derive_move("build", state, "item.deploy.parents", "withdrawn", {})`, so a state that row does not
admit answers `held`:

    route replan · parent <p> · move <state> → planning · item.deploy.parents
    route adopt-parent-work · parent <p> · move <state> → planning · item.deploy.parents
    inventory <p> <sha>          (per withdrawn parent: its kept branch tip, design.inventory's input)
    route withdraw-too · parent <p> · owner-item · propose item.life.close withdrawn · left by record-kind.disposition
    route <value> · parent <p> · held: <state> admits no parent row
    route none                   (no parent reads withdrawn, or no `parents:` or `depends-on:` key)

`<p>` is each withdrawn parent, space-separated, in `parents:` or `depends-on:` order. The kept branch is
the ref the parent's `run-branch:` fact names, else `branch-ref:`, resolved to its commit in `--root`.
`withdraw-too` proposes the build's withdrawal to the owner and moves nothing; its disposition is the
owner's record. The route writes nothing: the caller records the move or files the owner item.

`route` exits 0 with its answer; 2 printing `loop: unanswered · <why>` on an unreadable `parents:` or
`depends-on:` slug, a state outside the build's open states, a policy refusal, `no kept branch`; and 2
printing `loop: unarmed · <why>` where the policy kit or the memory-tree kit does not resolve, never a default.
The loop kit takes no edge to the policy kit, which is why.

`--fixture --plant <case>` builds a scratch repository holding the child build `tChild`, whose README
names `parents: tParent` (`depends-on: tParent` under the plant `depends-on-parent`), and the
parent's run-state file, commits `.governance/policy.toml` setting the key to `--value` where one is given, runs `route` there in `--state` (default `designing`), prints
whether the tree changed, and removes the scratch. `--selftest` runs every case through
`run_selftest_cases`. Exit 0 when every case holds, 1 otherwise.

WHAT THIS DOES NOT CHECK: a parent's planning ending (deferred, retired, refused or answered), which
has no run-state fact; a parent hold past `flow.wait-ceiling`; that a parent aborted for a reason it
later resumes from is not withdrawn, which it reads as until its next run; a policy value set on an
unlanded branch.
"""
import argparse
import pathlib
import sys
import tempfile

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from loop_lib import read_definition, read_memory_tree, resolve_kit_dir, resolve_memory_root, run_selftest_cases  # noqa: E402
from loop_table import TransitionRefused, derive_move, read_transition_rows  # noqa: E402
from loop_witness import read_git, remove_tree, run_fixture_git, write_fixture_files  # noqa: E402

SAY = "loop"
KEY = "deps.on-parent-withdrawn"
PARENT_ITEM = "item.deploy.parents"
#: The run fact `phase` value that stands in for a parent's `withdrawn` post.
WITHDRAWN_PHASE = "ABORTED"
#: The run facts naming the kept branch, in the order the unattended driver reads them.
KEPT_FACTS = ("run-branch", "branch-ref")
PLANTS = {"withdrawn-parent": "phase: ABORTED, run-branch naming a branch the scratch holds",
          "depends-on-parent": "withdrawn-parent, the child README naming depends-on: tParent in place of parents:",
          "no-kept-branch": "phase: ABORTED, its run-branch ref deleted from the scratch",
          "live-parent": "phase: BUILDING",
          "no-parents": "the child README carries no parents: key",
          "incomplete-parent": "phase: ABORTED with halt-code: budget-exhausted, which maps to incomplete",
          "aborted-on-run-branch": "the tree's copy phase: BUILDING, the run branch's tracking tip phase: ABORTED",
          "no-run-record": "the parent's build folder holds no RUN.md",
          "parent-in-extra-phase": "phase: STAGING, which the scratch's .unattended.conf sets in PHASES_EXTRA"}
FX_KEPT = "refs/heads/branch/tParent-run"


def read_policy_kit():
    """The policy kit's `policy` and `guard` modules, found beside this kit; LookupError where absent."""
    policy_dir = resolve_kit_dir("policy", "policy.py", KIT)
    if str(policy_dir) not in sys.path:
        sys.path.insert(0, str(policy_dir))
    import guard
    import policy
    return policy, guard


def read_withdrawn_parents(build, root):
    """`{parent slug: its run-state text, or None for no run record}` for each parent in `build`'s
    README `parents:` or `depends-on:`, the `after` targets of the memory-tree kit's `parse_relations`
    (TOOL-dTotalRecall-6 S9), that reads withdrawn or has no run record, in written order. A parent's text is
    its `RUN.md` at the tip of `refs/remotes/<remote>/<run-branch>` where that ref holds the file, the
    remote by the loop kit's inline ladder and the branch the `run-branch:` fact of the tree's own copy,
    else the tree's copy (TOOL-dDeclaredLoop-56 S39). It reads withdrawn where `derive_phase_position`
    maps its `phase`, with its `halt-code` and `hold-code` where set, to the state `withdrawn`
    (TOOL-dDeclaredLoop-56 S18). ValueError on an unreadable README, a slug naming no build folder or a
    phase the map refuses; LookupError where the memory-tree or policy kit does not resolve."""
    read_memory_tree("gen_build_index.py")
    from claims import resolve_remote
    from gen_build_index import ORDER_TYPE, Problem, parse_front_matter, parse_relations, read_relation_rows
    from loop_table import derive_phase_position
    _policy, guard = read_policy_kit()
    memory_root = resolve_memory_root(root)
    builds = pathlib.Path(root) / memory_root / "builds"
    try:
        fm = parse_front_matter(str(builds / build / "README.md"), build)
        parents = [e["target"] for e in parse_relations(fm, read_relation_rows(), str(root)) if e["type"] == ORDER_TYPE]
    except (Problem, OSError) as e:
        raise ValueError("the build %s's README does not read: %s" % (build, e)) from None
    remote = resolve_remote(root)[0]
    out = {}
    for slug in parents:
        if not (builds / slug).is_dir():
            raise ValueError("parents: or depends-on: names %s, which is not a build folder under %s" % (
                slug, builds.as_posix()))
        run = builds / slug / "RUN.md"
        text = run.read_bytes().decode("utf-8", "replace") if run.is_file() else None
        branch = (guard.read_run_fact(text, "run-branch") or "").strip().removeprefix("refs/heads/") if text else ""
        if remote and branch:
            rc, tip = read_git(root, "show", "refs/remotes/%s/%s:%s/builds/%s/RUN.md" % (remote, branch, memory_root, slug))
            text = tip if rc == 0 else text
        if text is None:
            out[slug] = None
            continue
        phase = guard.read_run_fact(text, "phase")
        facts = {k: guard.read_run_fact(text, k) for k in ("halt-code", "hold-code")}
        facts = {k: v for k, v in facts.items() if v}
        try:
            # tree=root: a phase no row reads is read against the conf of the tree that wrote it (TOOL-dDeclaredLoop-70)
            state = derive_phase_position(phase, facts, tree=root)[0]
        except LookupError as e:
            raise ValueError("the parent %s's phase %s maps to no state: %s" % (slug, phase, e)) from None
        if state == "withdrawn":
            out[slug] = text
    return out


def resolve_kept_tip(parent, text, root):
    """The commit of `parent`'s kept branch, the ref its first `KEPT_FACTS` fact names; ValueError
    `no kept branch` where neither fact is set or the ref names no commit."""
    _policy, guard = read_policy_kit()
    ref = next((v.strip() for v in (guard.read_run_fact(text, f) for f in KEPT_FACTS) if v and v.strip()), None)
    if ref:
        rc, sha = read_git(root, "rev-parse", "--verify", "--quiet", "--end-of-options", "%s^{commit}" % ref)
        if rc == 0 and sha:
            return ref, sha
    raise ValueError("no kept branch: %s's run state names %s, which resolves to no commit in %s" % (
        parent, ref or "neither run-branch nor branch-ref", pathlib.Path(root).as_posix()))


def derive_parent_route(build, state, root):
    """The route's lines for `build` in `state` under `root`: §4's answer for the policy value read.
    ValueError on a state outside the build's open states, an unreadable parent, a policy refusal or
    no kept branch; LookupError where a kit it reads does not resolve."""
    policy, _guard = read_policy_kit()
    tables = read_transition_rows(*read_definition(KIT))
    if state not in tables["states"]["build"]:
        raise ValueError("the state %s is no open build state: %s" % (state, " ".join(tables["states"]["build"])))
    try:
        value = policy.resolve(KEY, str(root)).value
    except policy.Refusal as e:
        raise ValueError("%s does not resolve: %s" % (KEY, e)) from None
    read = read_withdrawn_parents(build, root)
    lines = ["parent %s · not withdrawn (no run record)" % p for p, text in read.items() if text is None]
    withdrawn = {p: text for p, text in read.items() if text is not None}
    if not withdrawn:
        return lines + ["route none"]
    head = "route %s · parent %s" % (value, " ".join(withdrawn))
    if value == "withdraw-too":
        return lines + ["%s · owner-item · propose item.life.close withdrawn · left by record-kind.disposition" % head]
    try:
        _row, to = derive_move("build", state, PARENT_ITEM, "withdrawn", {}, tables)
    except TransitionRefused:
        return lines + ["%s · held: %s admits no parent row" % (head, state)]
    lines += ["%s · move %s → %s · %s" % (head, state, to, PARENT_ITEM)]
    if value == "adopt-parent-work":
        lines += ["inventory %s %s" % (p, resolve_kept_tip(p, text, root)[1]) for p, text in withdrawn.items()]
    return lines


def write_parent_plant(top, case, value):
    """The scratch repository at `top` for `case`, committed on `main`; the kept ref's `(ref, sha)` where
    the plant holds it, else None."""
    def build_readme(slug, extra=""):
        return ("---\nslug: %s\nnode: a\nopened: 2026-01-01\nstreams: tooling\nroster: none\nids: none\n%s---\n"
                "# %s\n" % (slug, extra, slug))
    phase = {"live-parent": "BUILDING", "aborted-on-run-branch": "BUILDING", "parent-in-extra-phase": "STAGING"}.get(
        case, WITHDRAWN_PHASE)
    run_text = "# tParent - run state\n\n## Run facts\nphase: %%s\n%srun-branch: %s\n" % (
        "halt-code: budget-exhausted\n" if case == "incomplete-parent" else "", FX_KEPT)
    run_fixture_git(top, "init", "-q", "--template=", "-b", "main")
    write_fixture_files(top, {
        ".memory-tree.conf": "MEMORY_ROOT=memory\n",
        "memory/builds/tChild/README.md": build_readme("tChild", {"no-parents": "", "depends-on-parent": "depends-on: tParent\n"}
                                                       .get(case, "parents: tParent\n")),
        "memory/builds/tParent/README.md": build_readme("tParent")})
    if case != "no-run-record":
        write_fixture_files(top, {"memory/builds/tParent/RUN.md": run_text % phase})
    if case == "parent-in-extra-phase":
        write_fixture_files(top, {".unattended.conf": 'PHASES_EXTRA="STAGING"\n'})
    if value is not None:
        write_fixture_files(top, {".governance/policy.toml": '[deps]\non-parent-withdrawn = "%s"\n' % value})
    run_fixture_git(top, "add", "-A")
    run_fixture_git(top, "commit", "-q", "-m", "fixture")
    if case == "no-kept-branch":
        return None
    run_fixture_git(top, "checkout", "-q", "-b", FX_KEPT.removeprefix("refs/heads/"))
    write_fixture_files(top, {"kept.txt": "the parent's kept work\n"})
    if case == "aborted-on-run-branch":  # the run branch's copy aborted and published; the tree's still building
        write_fixture_files(top, {"memory/builds/tParent/RUN.md": run_text % WITHDRAWN_PHASE})
    run_fixture_git(top, "add", "-A")
    run_fixture_git(top, "commit", "-q", "-m", "kept")
    run_fixture_git(top, "checkout", "-q", "main")
    if case == "aborted-on-run-branch":
        run_fixture_git(top, "remote", "add", "origin", (top / "origin.git").as_posix())
        fx = run_fixture_git(top, "remote")   # the fixture remote's name read back from git, never spelled
        run_fixture_git(top, "update-ref", "refs/remotes/%s/%s" % (fx, FX_KEPT.removeprefix("refs/heads/")), FX_KEPT)
        run_fixture_git(top, "update-ref", "refs/remotes/%s/main" % fx, "main")  # the policy's landed revision
        run_fixture_git(top, "remote", "set-head", fx, "main")
    return FX_KEPT, run_fixture_git(top, "rev-parse", FX_KEPT)


def run_fixture(case, value, state):
    """`route` over a scratch repository planted as `case`, the tree compared before and after."""
    top = pathlib.Path(tempfile.mkdtemp(prefix="loop-parents-"))
    try:
        print("%s: fixture · plant %s" % (SAY, case))
        kept = write_parent_plant(top, case, value)
        if kept:
            print("%s: fixture · kept %s %s" % (SAY, *kept))
        before = [run_fixture_git(top, "rev-parse", "HEAD"), run_fixture_git(top, "status", "--porcelain")]
        rc = main(["route", "--build", "tChild", "--state", state, "--root", str(top)])
        after = [run_fixture_git(top, "rev-parse", "HEAD"), run_fixture_git(top, "status", "--porcelain")]
        print("%s: fixture · tree %s" % (SAY, "unchanged" if before == after else "changed"))
        return rc
    finally:
        remove_tree(top)


def run_selftest():
    """Every plant's owed answer through `run_selftest_cases`."""
    fx = ["--fixture", "--plant"]
    move = "route %s · parent tParent · move designing → planning · " + PARENT_ITEM
    cases = [("replan", fx + ["withdrawn-parent", "--value", "replan"], 0, move % "replan", ""),
             ("held", fx + ["withdrawn-parent", "--value", "replan", "--state", "testing"], 0, "route replan",
              "held: testing admits no parent row"),
             ("not open", fx + ["withdrawn-parent", "--state", "landed"], 2, "%s: unanswered" % SAY, "landed"),
             ("adopt", fx + ["withdrawn-parent", "--value", "adopt-parent-work"], 0, "inventory tParent ", ""),
             ("no kept branch", fx + ["no-kept-branch", "--value", "adopt-parent-work"], 2, "%s: unanswered" % SAY,
              "no kept branch"),
             ("withdraw-too", fx + ["withdrawn-parent", "--value", "withdraw-too"], 0, "route withdraw-too",
              "owner-item · propose item.life.close withdrawn"),
             ("withdraw-too tree", fx + ["withdrawn-parent", "--value", "withdraw-too"], 0,
              "%s: fixture · tree unchanged" % SAY, ""),
             ("live", fx + ["live-parent"], 0, "route none", ""),
             ("no parents", fx + ["no-parents"], 0, "route none", ""),
             ("incomplete", fx + ["incomplete-parent"], 0, "route none", ""),
             ("run branch", fx + ["aborted-on-run-branch"], 0, move % "replan", ""),
             ("no run record", fx + ["no-run-record"], 0, "parent tParent · not withdrawn (no run record)", ""),
             ("no run record route", fx + ["no-run-record"], 0, "route none", ""),
             ("default", fx + ["withdrawn-parent"], 0, move % "replan", ""),
             ("depends-on-parent", fx + ["depends-on-parent"], 0, move % "replan", ""),
             ("extra phase", fx + ["parent-in-extra-phase"], 0, "route none", ""),
             ("bogus", fx + ["withdrawn-parent", "--value", "bogus"], 2, "%s: unanswered" % SAY, KEY)]
    return run_selftest_cases(main, cases, "%s: parents selftest" % SAY)


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="loop_parents.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("--selftest", action="store_true", help="run every plant's case")
    ap.add_argument("--fixture", action="store_true", help="run route over a scratch repository")
    ap.add_argument("--plant", choices=list(PLANTS))
    ap.add_argument("--value", help="the scratch policy file's value of %s; none commits no file" % KEY)
    ap.add_argument("--state", dest="fx_state", default="designing", help="the child's state, designing by default")
    sub = ap.add_subparsers(dest="verb")
    rt = sub.add_parser("route", help="answer a build's route on its parents' withdrawal")
    rt.add_argument("--build", required=True)
    rt.add_argument("--state", required=True)
    rt.add_argument("--root", default=".")
    args = ap.parse_args(argv)
    if args.selftest:
        if args.fixture or args.verb:
            ap.error("--selftest takes no verb and no --fixture")
        return run_selftest()
    if args.fixture != bool(args.plant) or (args.fixture and args.verb):
        ap.error("--fixture takes --plant <case> and no verb")
    if args.fixture:
        return run_fixture(args.plant, args.value, args.fx_state)
    if args.verb != "route":
        ap.error("a verb, route, or --fixture --plant <case>, or --selftest")
    try:
        lines = derive_parent_route(args.build, args.state, pathlib.Path(args.root))
    except LookupError as e:
        print("%s: unarmed · %s" % (SAY, e))
        return 2
    except ValueError as e:
        print("%s: unanswered · %s" % (SAY, e))
        return 2
    for line in lines:
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
