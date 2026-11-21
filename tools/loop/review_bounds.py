#!/usr/bin/env python3
"""review_bounds.py — every review loop's round bound, read from the owner's policy file
(TOOL-dDeclaredLoop-21).

    python review_bounds.py show [--rev <rev>]
    python review_bounds.py pin [--rev <rev>]
    python review_bounds.py --fixture [--plant <case>]

THE FOUR KEYS. `read_review_bounds(root, rev=None)` reads `review.max-rounds`,
`review.design.rounds`, `review.design.round-count` and `review.follow-up`, each through the policy
kit's `resolve`, found beside this kit by `resolve_kit_dir`, at `rev` or else the landed revision.
Until a policy file sets them they read the catalogue's defaults: 3, `one`, 2 and `after-high`.

THE TWO BOUNDS it derives. The SPEC bound, a spec audit's: 1 under `one`, `review.design.round-count`
under `fixed-count`, and `review.max-rounds` under each `until-*` value, whose stopping rule is the
convergence routing's. The CLOSING bound, the closing review's: 1 under `review.follow-up = "never"`,
`review.max-rounds` otherwise. `review.max-rounds` is the ceiling of every loop: the driver reads
`CEILING` one round past it.

THE TWO TARGET WORDS (TOOL-dDeclaredLoop-32), each `blockers`, `highs` or `all`: the count a loop
converges at when it reads zero. The SPEC target is `review.design.rounds`' word, `highs` under
`until-no-high`, `all` under `until-clean` and `blockers` under the other three; the CLOSING target is
`review.follow-up`'s, `highs` under `after-high`, `all` under `while-finding` and `blockers` under
`never`. `flow.route-backs`, read as the four keys are, is printed beside them as `route-backs=`.

THE FOUR DISPOSAL KEYS `review.dispose` reads (TOOL-dDeclaredLoop-20), each through `resolve` as the
others are and printed after `route-backs=`: `review.findings` (`findings=`, default `blocker-high-own`),
`review.unverified` (`unverified=`, default `ask`), `review.left-shift` (`left-shift=`, default
`second-occurrence`) and `review.blocks` (`blocks=`, default `every-review`). The policy kit holds each
to its catalogued values.

THE PIN VALUES, `read_review_pin(root, rev=None)`: `review.opt-in`, `review.unclassed`, `review.twin`,
`review.design-audit.runs` and `review.design-audit.seed`, which `pin` prints as the five flags the
workflows kit's `review_pin.py` takes. An empty `review.opt-in` passes as `none`; a non-empty one is
refused by name, because no lens map turns a set of lens names into `review_pin.py`'s object yet.

THE REFUSAL, `BoundsRefused`. A value below 1, a value outside its key's catalogued values, and under
`fixed-count` a `review.design.round-count` above `review.max-rounds`, naming both keys and both
values; a count EQUAL to the ceiling is admitted. A policy kit refusal is relayed as one. Where the
policy kit does not resolve, `LookupError`: an install may carry this kit without it.

`show` prints `max-rounds=<n> spec-bound=<n> closing-bound=<n> follow-up=<value> spec-target=<word>
closing-target=<word> route-backs=<n> findings=<value> unverified=<value> left-shift=<value>
blocks=<value>` on one line, exit 0; `pin` prints `--opt-in none --unclassed <value> --twin <value>
--design-audit-runs <n> --design-audit-seed <value>` on one line, exit 0;
`review-bounds: refused · <why>` on a refusal and `review-bounds: unarmed · <why>` where the policy
kit does not resolve, each exit 2. `check_review_bounds(root)` is the same read at HEAD for
`loop_lib.py --check`, the leg `loop definition`.

`--fixture` runs every plant of `PLANTS`, `--plant <case>` one, each in a scratch repository of its
own under the system temp directory: a policy file committed there, then `show --rev HEAD` run in it,
or `pin --rev HEAD` for the `pin` and `opt-in-set` plants.
The `no-driver` plant copies this module and the policy kit's three files into a tree holding no
unattended kit, and the `no-policy-kit` plant this module alone. Each prints `review-bounds: fixture ·
<case> · held` or `· MISSED <why>`. Exit 0 held, 1 missed, 2 where a scratch could not be built.

WHAT THIS DOES NOT CHECK: that the driver or the unattended leg reads the bound it prints, nor that
a round's recorded counts are true, nor that a raise was the owner's.
"""
import argparse
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
SAY = "review-bounds"
DESIGN_ROUNDS = ("one", "until-no-blocker", "until-no-high", "until-clean", "fixed-count")
FOLLOW_UPS = ("after-high", "while-finding", "never")
SPEC_TARGETS = {"until-no-high": "highs", "until-clean": "all"}        # every other value: blockers
CLOSING_TARGETS = {"after-high": "highs", "while-finding": "all", "never": "blockers"}
POLICY_FILES = ("policy.py", "budgets.py", "catalogue.toml")


class BoundsRefused(ValueError):
    """A review bound the owner's policy file sets and this module refuses, or the policy kit refused."""


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


def read_policy_module():
    """The policy kit's `policy` module, found beside this kit; LookupError where it does not resolve."""
    policy_dir = resolve_kit_dir("policy", "policy.py", KIT)
    if str(policy_dir) not in sys.path:
        sys.path.insert(0, str(policy_dir))
    import policy
    return policy


def derive_review_bounds(max_rounds, design, count, follow, route_backs=3):
    """-> {max-rounds, spec-bound, closing-bound, follow-up, spec-target, closing-target, route-backs}
    from the five values; BoundsRefused on a value below 1 (below 0 for `route_backs`), one outside its
    catalogued values, or a fixed count above the ceiling."""
    for key, value, low in (("review.max-rounds", max_rounds, 1), ("review.design.round-count", count, 1),
                            ("flow.route-backs", route_backs, 0)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise BoundsRefused("%s is %r, which is no whole number of rounds" % (key, value))
        if value < low:
            raise BoundsRefused("%s is %d, below %d, so no round could be held" % (key, value, low))
    if design not in DESIGN_ROUNDS:
        raise BoundsRefused("review.design.rounds is %r, outside %s" % (design, " ".join(DESIGN_ROUNDS)))
    if follow not in FOLLOW_UPS:
        raise BoundsRefused("review.follow-up is %r, outside %s" % (follow, " ".join(FOLLOW_UPS)))
    if design == "fixed-count" and count > max_rounds:
        raise BoundsRefused("review.design.round-count is %d, above review.max-rounds %d under review.design.rounds "
                            "fixed-count, so the ceiling would stop the audit before its count; a count equal to "
                            "the ceiling is admitted" % (count, max_rounds))
    spec = {"one": 1, "fixed-count": count}.get(design, max_rounds)
    return {"max-rounds": max_rounds, "spec-bound": spec,
            "closing-bound": 1 if follow == "never" else max_rounds, "follow-up": follow,
            "spec-target": SPEC_TARGETS.get(design, "blockers"), "closing-target": CLOSING_TARGETS[follow],
            "route-backs": route_backs}


def read_review_bounds(root=".", rev=None):
    """-> the derived bounds over the policy file of `root` at `rev`, else the landed revision, with the
    four disposal keys beside them. BoundsRefused on a refusal, the policy kit's included; LookupError
    where that kit does not resolve. Each key reaches `resolve` as a literal, the shape the policy kit's
    reader coverage reads."""
    policy = read_policy_module()
    root = str(root)
    try:
        max_rounds = policy.resolve("review.max-rounds", root, rev).value
        design = policy.resolve("review.design.rounds", root, rev).value
        count = policy.resolve("review.design.round-count", root, rev).value
        follow = policy.resolve("review.follow-up", root, rev).value
        route_backs = policy.resolve("flow.route-backs", root, rev).value
        disposal = {"findings": policy.resolve("review.findings", root, rev).value,
                    "unverified": policy.resolve("review.unverified", root, rev).value,
                    "left-shift": policy.resolve("review.left-shift", root, rev).value,
                    "blocks": policy.resolve("review.blocks", root, rev).value}
    except policy.Refusal as e:
        raise BoundsRefused(str(e)) from None
    bounds = derive_review_bounds(max_rounds, design, count, follow, route_backs)
    bounds.update(disposal)
    return bounds


def read_review_pin(root=".", rev=None):
    """-> {opt-in, unclassed, twin, runs, seed}, the five values `review_pin.py` takes, over the policy
    file of `root` at `rev`, else the landed revision. BoundsRefused on a non-empty `review.opt-in` and
    on a policy kit refusal; LookupError where that kit does not resolve."""
    policy = read_policy_module()
    root = str(root)
    try:
        opt_in = policy.resolve("review.opt-in", root, rev).value
        pin = {"unclassed": policy.resolve("review.unclassed", root, rev).value,
               "twin": policy.resolve("review.twin", root, rev).value,
               "runs": policy.resolve("review.design-audit.runs", root, rev).value,
               "seed": policy.resolve("review.design-audit.seed", root, rev).value}
    except policy.Refusal as e:
        raise BoundsRefused(str(e)) from None
    if opt_in:
        raise BoundsRefused("review.opt-in is %s, and no lens map turns a set of lens names into the object "
                            "review_pin.py takes, so only the empty set is read" % " ".join(map(str, opt_in)))
    pin["opt-in"] = "none"
    return pin


def render_pin_flags(pin):
    """The one line `pin` prints: the five flags `review_pin.py` takes."""
    return "--opt-in %s --unclassed %s --twin %s --design-audit-runs %d --design-audit-seed %s" % (
        pin["opt-in"], pin["unclassed"], pin["twin"], pin["runs"], pin["seed"])


def render_bounds_line(bounds):
    """The one line `show` prints."""
    return ("max-rounds=%d spec-bound=%d closing-bound=%d follow-up=%s spec-target=%s closing-target=%s route-backs=%d "
            "findings=%s unverified=%s left-shift=%s blocks=%s") % (
        bounds["max-rounds"], bounds["spec-bound"], bounds["closing-bound"], bounds["follow-up"],
        bounds["spec-target"], bounds["closing-target"], bounds["route-backs"], bounds["findings"],
        bounds["unverified"], bounds["left-shift"], bounds["blocks"])


def check_review_bounds(root):
    """`loop_lib.py --check`'s arm: (the show line or None, [refusals]) over `root`'s policy file at
    HEAD. LookupError where the policy kit does not resolve, which the caller prints as unarmed."""
    try:
        return render_bounds_line(read_review_bounds(root, "HEAD")), []
    except BoundsRefused as e:
        return None, ["the review bounds do not read: %s" % e]


# Each plant: (policy file text or None, owed exit, a needle the output holds). `no-driver` and
# `no-policy-kit` run a copy of this module in a tree holding no unattended kit. A plant `PLANT_VERBS` names
# runs that verb in place of `show`.
COUNT_ABOVE = '[review]\nmax-rounds = 3\n\n[review.design]\nrounds = "fixed-count"\nround-count = 4\n'
PLANTS = {
    "defaults": (None, 0, "max-rounds=3 spec-bound=1 closing-bound=3 follow-up=after-high spec-target=blockers "
                          "closing-target=highs route-backs=3 findings=blocker-high-own unverified=ask "
                          "left-shift=second-occurrence blocks=every-review"),
    "disposal-keys": ('[review]\nfindings = "all-own"\nunverified = "block"\nleft-shift = "every-class"\n'
                      'blocks = "none"\n', 0, "route-backs=3 findings=all-own unverified=block left-shift=every-class "
                                              "blocks=none"),
    "pin": ('[review]\nunclassed = "reason"\n', 0, "--opt-in none --unclassed reason --twin never "
                                                     "--design-audit-runs 2 --design-audit-seed reverted-escapes"),
    "opt-in-set": ('[review]\nopt-in = ["fresh-eyes"]\n', 2, "%s: refused · review.opt-in is fresh-eyes" % SAY),
    "targets": ('[review]\nfollow-up = "while-finding"\n\n[review.design]\nrounds = "until-clean"\n\n[flow]\n'
                'route-backs = 2\n', 0, "spec-target=all closing-target=all route-backs=2"),
    "count-equal": ('[review]\nmax-rounds = 3\n\n[review.design]\nrounds = "fixed-count"\nround-count = 3\n',
                    0, "spec-bound=3"),
    "count-above": (COUNT_ABOVE, 2, "review.design.round-count is 4, above review.max-rounds 3"),
    "count-zero": ('[review.design]\nround-count = 0\n', 2, "review.design.round-count is 0, below 1"),
    "max-zero": ('[review]\nmax-rounds = 0\n', 2, "review.max-rounds is 0, below 1"),
    "until": ('[review]\nmax-rounds = 5\n\n[review.design]\nrounds = "until-clean"\n', 0,
              "max-rounds=5 spec-bound=5 closing-bound=5"),
    "never": ('[review]\nfollow-up = "never"\n', 0, "closing-bound=1 follow-up=never"),
    "while-finding": ('[review]\nfollow-up = "while-finding"\n', 0, "closing-bound=3 follow-up=while-finding"),
    "no-driver": (COUNT_ABOVE, 2, "review.design.round-count is 4, above review.max-rounds 3"),
    "no-policy-kit": (None, 2, "%s: unarmed · " % SAY),
}
PLANT_VERBS = {"pin": "pin", "opt-in-set": "pin"}


def run_git(repo, *args):
    """A git command in a scratch repository under a fixed identity; CalledProcessError on a failure."""
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    return subprocess.run(["git", "-c", "user.name=fx", "-c", "user.email=fx@example.invalid", "-c",
                           "commit.gpgsign=false", "-c", "core.autocrlf=false", *args], cwd=str(repo), check=True,
                          capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)


def build_plant_repo(scratch, case):
    """The scratch repository `case` runs in, its files committed on `main`; -> the module to run."""
    text = PLANTS[case][0]
    module = pathlib.Path(__file__).absolute()
    if case in ("no-driver", "no-policy-kit"):
        loop_dir = scratch / "kits" / module.parent.name
        loop_dir.mkdir(parents=True)
        shutil.copy2(module, loop_dir / module.name)
        module = loop_dir / module.name
        if case == "no-driver":
            policy_dir = read_policy_module().KIT
            (scratch / "kits" / policy_dir.name).mkdir()
            for name in POLICY_FILES:
                shutil.copy2(policy_dir / name, scratch / "kits" / policy_dir.name / name)
    if text is not None:
        (scratch / ".governance").mkdir()
        (scratch / ".governance" / "policy.toml").write_bytes(text.encode("utf-8"))
    (scratch / "README.md").write_bytes(b"review bounds plant\n")
    run_git(scratch, "init", "-q", "-b", "main", "--template=")
    run_git(scratch, "add", "-A")
    run_git(scratch, "commit", "-q", "-m", "plant %s" % case, "--no-verify")
    return module


def run_plant(case):
    """-> 0 held, 1 missed, 2 the scratch could not be built; one closing line printed either way."""
    from loop_witness import remove_tree   # the loop kit's remover: git's objects are read-only on Windows
    _text, owed, needle = PLANTS[case]
    scratch = pathlib.Path(tempfile.mkdtemp(prefix="rb"))
    try:
        try:
            module = build_plant_repo(scratch, case)
        except (OSError, LookupError, subprocess.CalledProcessError) as e:
            print("%s: fixture · %s · MISSED the scratch could not be built: %s" % (SAY, case, e))
            return 2
        env = {k: v for k, v in os.environ.items() if k not in ("GOV_REMOTE", "GOV_DEFAULT_BRANCH")}
        p = subprocess.run([sys.executable, "-I", str(module), PLANT_VERBS.get(case, "show"), "--rev", "HEAD"], cwd=str(scratch),
                           capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)
        said = (p.stdout + p.stderr).strip()
        print("%s: fixture · %s · exit %d · %s" % (SAY, case, p.returncode, said.splitlines()[0] if said else ""))
        if p.returncode == owed and needle in said:
            print("%s: fixture · %s · held" % (SAY, case))
            return 0
        print("%s: fixture · %s · MISSED exit %d, owed %d and a line naming %r" % (SAY, case, p.returncode, owed, needle))
        return 1
    finally:
        remove_tree(scratch)


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="review_bounds.py")
    ap.add_argument("verb", nargs="?", choices=["show", "pin"])
    ap.add_argument("--rev")
    ap.add_argument("--fixture", action="store_true")
    ap.add_argument("--plant", choices=sorted(PLANTS))
    a = ap.parse_args(argv)
    if a.fixture == bool(a.verb) or (a.plant and not a.fixture) or (a.rev and not a.verb):
        ap.print_usage(sys.stderr)
        return 2
    if a.fixture:
        rcs = [run_plant(case) for case in ([a.plant] if a.plant else PLANTS)]
        missed = [c for c, rc in zip([a.plant] if a.plant else PLANTS, rcs) if rc]
        print("%s: fixture · %d plant(s) · %d missed%s" % (SAY, len(rcs), len(missed),
                                                          (": " + " ".join(missed)) if missed else ""))
        return max(rcs)
    try:
        print(render_pin_flags(read_review_pin(".", a.rev)) if a.verb == "pin"
              else render_bounds_line(read_review_bounds(".", a.rev)))
    except BoundsRefused as e:
        print("%s: refused · %s" % (SAY, e))
        return 2
    except LookupError as e:
        print("%s: unarmed · %s" % (SAY, e))
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
