"""check_policy.py - the policy kit's arms, run over a repository, and the fixture that proves each
one can red (TOOL-dGroundRules-1).

    python <this kit>/check_policy.py [--repo <dir>]   # every arm in ARMS; exit 0 green, 1 red
    python <this kit>/check_policy.py --fixture [--strict-from <dir>] [<case>]  # every case, or the one named
    python <this kit>/check_policy.py --live   # headless sessions under a rendered agent limit

`<dir>` defaults to the git top level of the working directory. Each arm prints
`policy-check: <arm> · <n> finding(s) · <population>`, then one line per finding. What a population
of zero means each `ARMS` entry declares as its `empty` (TOOL-dGroundRules-21 S5): `finding`, so an
arm that read nothing cannot read green, or `announce`, where an empty population is a legal state,
which prints `policy-check: <arm> · not graded · <why>` and no finding. An arm may also announce
itself, answering None for its population, where its subject cannot exist yet.

THE ARMS read the repository's `.governance/policy.toml` and this kit's catalogue and shrink-only
list: `arm_schema` grades each file key with the value check, `arm_shape` audits the catalogue's
rows, `arm_summaries` grades the list as `policy.py lists --check` does, `arm_direction` reds a
loop bound or deadline row that does not declare `direction = "raise-loosens"` (TOOL-dGroundRules-11),
and `arm_on_invalid` reds what `policy.py check` refuses at HEAD (TOOL-dGroundRules-4).
`arm_reader_coverage` reds a catalogue key whose owner build has landed, every spec in its build
folder terminal at the landed revision, and that no call of READER_SHAPES in the tracked code reads
(TOOL-dGroundRules-8); it grades nothing until an owner lands, and announces so. The mirror's
three (TOOL-dGroundRules-5): `arm_mirror_parity` reds a working-tree `.governance/policy.json` that
differs from its render at HEAD, or is absent where HEAD carries the policy file or a mirror, and
announces otherwise (TOOL-dGroundRules-21 S15); `arm_mirror_landed` reds a key the policy file at
the landed revision sets that the helper `policy-mirror.js` and the reader answer differently, one
`node` call per key; `arm_mirror_readers` reds a tracked code file outside this kit, the memory root,
`help/` and the self-tests that READS `policy.json`, by `arm_single_reader`. `arm_legacy_homes` reds
each report `policy.py lists --check` makes on the legacy-homes list (TOOL-dGroundRules-7); where
this kit holds no list, as in every install, it prints `policy-check: arm_legacy_homes · not graded
· <why>` (TOOL-dGroundRules-17).

THE FIXTURE makes one git repository per case under the system temp directory, with a short prefix
because a long path fails a Windows clone: a copy of this kit's catalogue and list at the kit's own
path in its repository, and a policy file at its scaffold, committed, with a remote-tracking ref at
that commit. Each case plants its break on the copy and runs its arm, which must red NAMING the
planted key, then runs the arm again on the unplanted copy, which must be green. Each plant edits a
real shipped row where one serves. WHAT IT DOES NOT CHECK: that the shipped catalogue's values are
v2's, which is the build's acceptance probe, not an arm.

`adopter-fresh-target` is an outcome case, no plant (TOOL-dGroundRules-16): this kit installed into a
fresh `git init` by the deployer, its `apply` with the closure of its `requires`, run from a
scratch clone whose HEAD commits the working tree under test, so an uncommitted edit is graded
(TOOL-dGroundRules-26), and only through `run_govkit`, which refuses the source's own root, the
refusal `govkit-source-root-refused` observes (TOOL-dGroundRules-27), the tool root compared with the receipt both ways (TOOL-dGroundRules-24),
`--scaffold`, then `--check` with the install staged and again once it is committed, where every arm
must grade clean or announce; and the README's "Each arm in an adopter" table joined to ARMS both
ways. Green on a correct build; its RED is a failed snapshot step, a refused `apply`, a stray or
missing receipt path, or an arm that finds a problem in an adopter's tree.

`reader-landed` and `reader-parsed` are outcome cases too (TOOL-dGroundRules-2): each builds its own
repositories, runs `policy.py get` in them and prints one line per observation. `reader-landed`
reds a read of the working tree or of local HEAD without `--rev`, a fallback past a refused revision,
key or remote ladder; `reader-parsed` reds a policy file line that runs, or one that is not TOML
read as a value.

`resolution-order` is an outcome case (TOOL-dGroundRules-3), one repository per scenario read at
`--rev HEAD`: it reds a default read over a key the file sets, an unset key or an absent file that
refuses or reads anything but the catalogue default with its case's reason, a named preset missing
from the reason, and a row with no default that prints a value; that row is planted in a copy of
this kit, never in the tracked catalogue.

`on-invalid-classes` and `on-invalid-strict` are outcome cases (TOOL-dGroundRules-4). The first plants
each failure class of the invalid-file branch in its own repository, and reds a default or the invalid
file's own value read while the file is invalid, a fallback past `refuse`, and an `arm_on_invalid`
silent over a malformed file with no valid revision. The second reads v2's `[presets]` table from the
one file directly in the directory `--strict-from` names whose name ends `-architecture-v2.md`, red
naming the count when there is none or more than one, derives its population, plants strict's value of
each kept key in a valid revision with a malformed one after it, and reds any read that is not
strict's value from `last-valid` or an empty population; with no `--strict-from` it prints NOT RUN,
which is never a pass.

The fixture's repository also carries a tracked consumer outside the kit, `hooks/consumer.js`, that
reads policy through the helper, and the mirror rendered at its commit in the working tree.
`mirror-hand-edited`, `mirror-absent` and `mirror-direct-reader` are plant cases of the mirror's
parity and readers arms. `mirror-worktree-loosened`, `mirror-stale-last-valid`, `mirror-stale-refuse`
and `mirror-absent-refuse` are outcome cases (TOOL-dGroundRules-5): each copies policy.py,
policy-mirror.js and policy-shim.sh into the kit copy, pushes a landed revision L to a bare remote,
and asserts what the helper, the hooks kit's agent-cap.js and `arm_mirror_landed` answer there.
`mirror-landed-parity` holds the shim's `landed` to `derive_landed_revision` in six ladder states.
`mirror-commit-rewrite` (TOOL-dGroundRules-65) commits the mirror rendered at its parent, rewrites
that commit with `git commit-tree` as the lander does, and reds a `mirror --check` that is not fresh
at either commit, or a helper reading the rewrite that leaves the render's `{rev}` unfilled.
`mirror-landed-merge` (TOOL-dGroundRules-14) replays the lander's landing: a branch's policy change
merged `--no-ff` onto main, the mirror rendered over the merge, the merge rewritten by `commit-tree`
over its parents and pushed as main; it reds a mirror the check, `arm_mirror_parity` or the helper
calls stale at that rewrite.

The `guard-*` cases are outcome cases of the minimal guard (TOOL-dGroundRules-6): each copies
`guard.py`, `guarded-paths.txt` and `policy.py` into the kit copy, commits a policy file capping a
tracked `.claude/skills/x/SKILL.md`, whose key carries slashes and a leading dot, and `small.md`, and
the spec folder's class row (TOOL-dGroundRules-21 S22),
beside a runtime table setting agents-in-flight to 4, stages its plant from `GUARD_PLANTS`, and
judges `guard.py --staged` by its exit code and the reasons it prints. `guard-admits-raise` is the one
plant that must exit 0; `guard-merge-side` concludes a conflicted merge with the branch's side, exit
0, then with a third text, exit 1. The mirror shape's three (TOOL-dGroundRules-19): `guard-mirror-render`
commits a catalogue row and stages the regenerated mirror alone, exit 0; `guard-mirror-beside-catalogue`
stages it beside the row, exit 1; `guard-mirror-branch-green` commits the admitted mirror on a branch
and reads `mirror --check` fresh at the new HEAD.

`legacy-homes` is an outcome case (TOOL-dGroundRules-7): per case, a repository holding a copy of
policy.py, a `.unattended.conf`, a gate file and a house file where the copy resolves HOUSE_HOME,
pushed to one bare remote with the legacy list seeded, so the landed revision resolves. Each case
plants its break and judges the copy's `lists --check` and `lists --write` by exit code and exact
reports, printing `case <name>: red|green`.

`reader-coverage` is an outcome case (TOOL-dGroundRules-8): per case of RC_CASES, a repository holding
a kit copy whose catalogue carries the planted key, a planted spec under `bPlanted`'s build folder and
the planted consumers, pushed to one bare remote, then the spec's working-tree token; it judges
`check_reader_coverage` by the key it reds and the count it grades, printing `case <name>: red|green`.

The `limit-` cases are outcome cases of the agent limit (TOOL-dGroundRules-10), one repository each
with no remote, so local main is its landed revision. `limit-conf-lowers`, `limit-conf-no-raise` and
`limit-conf-malformed` plant `.agent-cap.conf` and read `policy.py get runtime.agents-in-flight`, the
last `policy.py mirror --print` too, which must refuse at the same line;
`limit-conf-mirror` and `limit-conf-last-valid` (TOOL-dGroundRules-15) plant a lowering, the second
over a malformed file whose last valid revision sets 6, render the mirror and red a `get` or a
helper reading the fresh mirror that does not answer the lowered value;
`limit-settings-render` commits two policy values and runs `policy.py settings`; the seven `limit-hook-`
cases copy the hooks kit's agent-cap.js and scratch-guard.js beside a copy of this kit, so rule 7 reads
the fixture's own limit, and judge each call by its exit code and the text its criterion names;
`limit-hook-writer-split` (TOOL-dGroundRules-18) pipes the workflows kit's build-harness template,
rendered at 6, through `--only=scripts`, so rule 2 judges its `gov:fixed-writers` split by that limit.

THE SIZE CAPS (TOOL-dGroundRules-9) add two arms and three kinds of case. `arm_limits_readers` reds a
tracked code file outside this kit, the memory root, `help/` and the self-tests that reads the
template-size limits file on a line that is not a comment or a docstring, or names `LIMITS_NAME`,
the second row of `arm_single_reader` (TOOL-dGroundRules-21 S20, S29); `arm_cap_census` joins
`caps.toml` to the tree both ways, announcing a row whose enforcer does not ship or whose kit is not
installed (TOOL-dGroundRules-17). `budgets-pinned-outside`, `budgets-pinned-exempt`,
`budgets-pinned-unknown` and `budgets-family-value` are plant cases of `arm_schema`. The other named
`budgets-` cases are outcome cases, one repository per observation. One `budgets-cap-<name>` case per
census row, declared in CAP_CASES, builds a scratch repository on main with no remote, plants the
cap's subject over its value, read from the source, and runs the row's enforcer under `warn` and under
`refuse`: a `switch` row must warn and pass, then refuse naming `budgets.enforce`, and one that is not a
family runs a third time with its value at 0 in the policy file, which must pass unchecked
(TOOL-dGroundRules-75); an outside row must
answer the same under both, and the reader must refuse to answer it.

WHAT SHIPS (TOOL-dGroundRules-17) adds two cases that read only this kit and its source repository,
so they hold on gov's tree alone. `legacy-homes-present` reds this kit's directory without
`legacy-homes.txt`, or a `kit.toml` with no `project-owned` rule naming it. `budgets-ships-join` reds a
census row whose `ships = false` disagrees with the deployer registry's `[[exempt]]` paths either way,
naming the row, and a registry that exempts no census enforcer.

WHERE IT INSTALLS (TOOL-dGroundRules-22): `arm_cap_census` reads a tree with a
`.governance/install.json` as an adopter, grading each shipped row of an installed kit at its
`installed` path. With no receipt (TOOL-dGroundRules-29) a tree holding one `govkit/registry.toml`
0 to 2 deep is the source, each row graded at its `enforcer`; a tree holding none is unadopted, every
row announced and none graded; two are a finding naming both. `census-receiptless-target` reads a
bare repository so, then again with the registry copied in, where every enforcer reds.
`census-ambiguous-registry` (TOOL-dGroundRules-34 S13) is a plant case of `arm_cap_census`: two
registries, one and two deep, red as the one finding naming both, and green unplanted.
`census-window-edge` (TOOL-dGroundRules-39) is an outcome case on the window's edges: a `<d>` three
deep and a bare top-level `registry.toml` are never candidates, and a two-deep one always is.
`census-adopter-receipt` is an outcome case: a planted receipt naming no `check-line-length`, each
named kit's enforcers at their `installed` paths, read green with the line-length row announced, red
naming `manifest-bytes` once its planted enforcer is deleted, and green again restored.
`budgets-ships-join` holds those two fields to the deployer on gov's tree (TOOL-dGroundRules-23): it
loads the deployer from the source repository and reds, naming the row, the entry and the destination,
a shipped row whose `kit` does not write its enforcer at `installed`, or whose enforcer another entry
writes.

THE MINORS BATCH (TOOL-dGroundRules-21) adds outcome cases, each named in its function's docstring:
`adopter-suite` runs the adopter's sibling suite; `on-invalid-utf16`, `on-invalid-shallow` and
`resolution-derived-default` the reader's refusals; `mirror-stale-legacy`, `mirror-shim-exit-one`
and `mirror-absent-adopter` the mirror's; `legacy-homes-main-dropped` the lists' one compare base;
`reader-coverage-relocated` and `reader-quoted-pattern` reader coverage; `limit-settings-elsewhere`,
`limit-hook-settings-malformed`, `limit-hook-reader-throws` and `limit-fresh-target-spawn` the agent
limit's settings; `budgets-zero-cap`, `budgets-reader-refused` and `limits-reader-docstring` the
size caps. `budgets-unset-derived` (TOOL-dGroundRules-62) reads an unset cap's derived default as no
file value under the last valid revision, and an unparsed file with none before it as a refusal.

Rule 7 bounds every settings layer it reads (TOOL-dGroundRules-61): `limit-settings-elsewhere-project-over`
refuses a project file above the limit beside a declared file at it, `limit-settings-declared-absent`
refuses a `GOV_SETTINGS_JSON` that names no file, and `limit-settings-elsewhere` plants the project
file at the limit before its declared file goes above it.

`limit-hook-landed-unread` (TOOL-dGroundRules-73) moves the limit fixture to `master`: with no remote,
then with one remote and no remote HEAD, rule 7 must deny naming the missing `main` ref and its remedy
and never `settings --write`, and admit under `GOV_DEFAULT_BRANCH=master`, then after
`git remote set-head <remote> -a`.

`--live` (S9) is no case: it drives headless `claude -p` sessions in a fixture repository under a
rendered limit and under a control with none, reads each agent's start and end stamps, and prints
each run's peak overlap. It costs real sessions, so no leg runs it.

Later units add arms to ARMS and cases to CASES.
"""
import ast
import contextlib
import hashlib
import importlib.util
import io
import json
import os
import posixpath
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import time
import tomllib
from collections import namedtuple
from pathlib import Path

sys.dont_write_bytecode = True  # a gate leg leaves no bytecode cache in an adopter's kit dir
import policy  # noqa: E402  (the module beside this file)
import budgets  # noqa: E402  (the size caps' module beside this file, TOOL-dGroundRules-9)

KIT = policy.KIT
POLICY_FILE = (".governance", "policy.toml")
POLICY_REL = "/".join(POLICY_FILE)
FIXTURE_REMOTE = "upstream"
PLANTED = "zz.planted"


def load_rows(kit):
    """-> (rows, None), or (None, the one finding a catalogue that does not parse is)."""
    try:
        return policy.load_catalogue(kit), None
    except (OSError, tomllib.TOMLDecodeError) as exc:
        return None, (policy.CATALOGUE, f"does not parse: {exc}")


def arm_schema(repo, kit):
    """Each problem `policy.validate` finds in the policy file: a key its catalogue row refuses, and a
    key no row matches (TOOL-dGroundRules-4 re-points this arm through the one judge), and the
    `[budgets]` table's rule over the cap census `repo` holds at this kit's path (TOOL-dGroundRules-9).
    A census that does not read, or a file that is not UTF-8, is the one finding. No policy file, or
    one setting no key, is a population of 0, which this arm announces (TOOL-dGroundRules-21 S5)."""
    rows, bad = load_rows(kit)
    if bad:
        return 0, "the catalogue did not parse", [bad]
    path = Path(repo, *POLICY_FILE)
    if not path.is_file():
        return 0, f"{POLICY_REL} is absent, so no key was graded", []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        return 0, f"{POLICY_REL} did not decode", [(POLICY_REL, f"not UTF-8: {exc}")]
    try:
        census = budgets.read_cap_census(repo)
    except policy.Refusal as exc:
        return 0, "the cap census did not read", [(f"{exc.path}:{exc.line}", exc.why)]
    problems = policy.validate(text, rows, census)
    if problems and not problems[0].key:
        return 0, f"{POLICY_REL} did not parse", [(POLICY_REL, f"does not parse: {problems[0].why}")]
    n = sum(1 for _ in policy.scan_keys(tomllib.loads(policy.derive_bomless_text(text)), rows))
    return n, f"{n} key(s) of {POLICY_REL} against {len(rows)} row(s)", [(p.key, p.why) for p in problems]


def arm_shape(repo, kit):
    """Each finding of the catalogue's shape audit."""
    rows, bad = load_rows(kit)
    if bad:
        return 0, "the catalogue did not parse", [bad]
    sets = [r for r in rows if isinstance(r.get("allowed"), dict) and r["allowed"].get("type") in policy.SET_TYPES]
    never = sum(1 for r in sets if r.get("empty") == "never")
    return len(rows), f"{len(rows)} row(s), {len(sets)} set-valued, {never} never-empty", policy.check_shape(rows)


def arm_summaries(repo, kit):
    """Each finding of `policy.py lists --check`: the shrink-only list against the catalogue and its base."""
    rows, bad = load_rows(kit)
    if bad:
        return 0, "the catalogue did not parse", [bad]
    with policy.run_without_git_env():  # the base `lists --check` reads, by the one comparison
        compare = policy.resolve_compare_base(kit)
    findings, note = policy.check_list(kit, compare)
    return len(rows), f"{len(policy.derive_unsummarised(rows))} of {len(rows)} row(s) unsummarised · {note}", findings


def arm_direction(repo, kit):
    """Each `check_direction` pair; the population is the rows `derive_bounds` selects."""
    rows, bad = load_rows(kit)
    if bad:
        return 0, "the catalogue did not parse", [bad]
    n = len(policy.derive_bounds(rows))
    return n, f"{n} loop bound and deadline row(s)", policy.check_direction(rows)


def check_head(repo):
    """True where HEAD names a commit in `repo`: before the first commit there is no HEAD to grade."""
    return bool((policy.run_git(repo, "rev-parse", "--verify", "-q", "HEAD^{commit}") or "").strip())


def arm_on_invalid(repo, kit):
    """The `policy.py check` verdict over the repository's HEAD, the candidate a push lands: its
    Refusal, an invalid policy file with no fallback, is the one finding (TOOL-dGroundRules-4). A HEAD
    that names no commit, or one holding no policy file, grades nothing and is announced
    (TOOL-dGroundRules-21 S15)."""
    if not check_head(repo):
        return None, "HEAD names no commit, so no policy file is committed to check", []
    try:
        line = policy.check_revision(repo, "HEAD")
    except policy.Refusal as exc:
        return 1, f"{POLICY_REL} at HEAD", [(f"{exc.path}:{exc.line}", exc.why)]
    line = line.removeprefix("policy: check · ")
    return (None if " is absent at " in line else 1), line, []


# ---- the JSON mirror (TOOL-dGroundRules-5) ------------------------------------------------------

MIRROR_FILE = tuple(policy.MIRROR_REL.split("/"))
# The reader and what `validate` reads beside it: the caps module and its census (TOOL-dGroundRules-9).
# Every kit copy that runs the reader carries all three.
READER_FILES = ("policy.py", "budgets.py", budgets.CENSUS)
MIRROR_KIT_FILES = (*READER_FILES, "policy-mirror.js", "policy-shim.sh")
CODE_PATHSPECS = ("*.js", "*.mjs", "*.cjs", "*.py", "*.sh", ".githooks/*")
MIRROR_REMEDY = "run: python <this kit>/policy.py mirror --write"


def arm_mirror_parity(repo, kit):
    """The working-tree mirror against `policy.render_mirror(repo, "HEAD")`: a mirror that differs,
    named by its first difference, or one absent where HEAD carries the policy file or a mirror. An
    absent mirror where HEAD carries neither, which nothing in an adopter writes before its first
    landing, or a HEAD that names no commit, is announced and grades nothing (TOOL-dGroundRules-21
    S15). A render the reader refuses is the one finding."""
    path = Path(repo, *MIRROR_FILE)
    if not check_head(repo):
        return None, "HEAD names no commit, so no mirror is rendered to compare", []
    carried = [rel for rel in (POLICY_REL, policy.MIRROR_REL)
               if (policy.run_git(repo, "cat-file", "-e", f"HEAD:{rel}") is not None)]
    if not path.is_file() and not carried:
        return None, f"HEAD carries neither {POLICY_REL} nor {policy.MIRROR_REL}, so no landing has rendered one", []
    try:
        want = policy.render_mirror(repo, "HEAD")
    except policy.Refusal as exc:
        return 1, f"{policy.MIRROR_REL} against its render at HEAD", [(f"{exc.path}:{exc.line}", exc.why)]
    drift = policy.check_mirror_text(want, path.read_bytes() if path.is_file() else None)
    n = len(json.loads(want)["keys"])
    population = f"{n} key(s) of {policy.MIRROR_REL} against its render at HEAD"
    if drift is None:
        return n, population, []
    if drift == "absent":
        return n, population, [(policy.MIRROR_REL, f"absent; {MIRROR_REMEDY}")]
    return n, population, [(drift, f"differs from the render at HEAD; {MIRROR_REMEDY}")]


def render_get(value):
    """A value as `policy.py get` prints it: a string as itself, a list one member per line."""
    return "".join((v if isinstance(v, str) else policy.render_toml_value(v)) + "\n"
                   for v in (value if isinstance(value, list) else [value]))


def arm_mirror_landed(repo, kit):
    """For each key the policy file at the landed revision L sets, the helper's CLI, `node
    policy-mirror.js get <key> --repo <repo>`, one call per key, against the reader's `resolve` at L
    as `get` prints it: a value the two answer differently, or one refusing where the other answers,
    is a finding. A landed revision that does not resolve is announced, and one whose policy file
    sets no key is a population of 0, announced by its `empty` (TOOL-dGroundRules-25 S26)."""
    try:
        sha, _how = policy.derive_landed_revision(repo)
    except policy.Refusal as exc:  # announced: no landing yet is legal (TOOL-dGroundRules-25 S26)
        return None, f"no landed revision: {exc.why}", []
    try:
        text = policy.read_policy_text(repo, sha)
        keys = sorted(policy.render_dotted(p) for p in policy.parse_policy(text)) if text is not None else []
    except policy.Refusal as exc:
        return 0, f"no landed revision: {exc.why}", []
    except tomllib.TOMLDecodeError:
        return 0, f"{POLICY_REL} at {sha[:8]} is not TOML, so it sets no key to compare", []
    out = []
    for key in keys:
        try:
            want = (0, render_get(policy.resolve(key, repo).value))
        except policy.Refusal as exc:
            want = (2, str(exc))
        try:
            p = subprocess.run(["node", str(Path(kit) / "policy-mirror.js"), "get", key, "--repo", str(repo)],
                               capture_output=True, text=True, encoding="utf-8", errors="replace")
            got = (p.returncode, p.stdout.replace("\r", "") if p.returncode == 0 else p.stderr.strip())
        except OSError as exc:
            got = (None, f"node did not run: {exc}")
        if got[0] != want[0] or (want[0] == 0 and got[1] != want[1]):
            out.append((key, f"the helper answers {got[1].strip()!r} (exit {got[0]}), the reader {want[1].strip()!r} (exit {want[0]})"))
    return len(keys), f"{len(keys)} key(s) the policy file sets at {sha[:8]}, the helper against the reader", out


def read_memory_root(repo):
    """MEMORY_ROOT from the repository's `.memory-tree.conf`, else `memory`."""
    try:
        text = Path(repo, ".memory-tree.conf").read_text(encoding="utf-8")
    except OSError:
        return "memory"
    m = re.search(r'^\s*MEMORY_ROOT\s*=\s*"?([^"#\s]+)"?', text, flags=re.M)
    return m[1].strip("/") if m else "memory"


def arm_legacy_homes(repo, kit):
    """Each report `policy.py lists --check` makes on the legacy-homes list (TOOL-dGroundRules-7): the
    rows derived from the repository's legacy policy homes against this kit's list and the list at the
    landed revision. A Refusal, an unreadable landed revision or house file, is the one finding. Where
    `kit` holds no list, the arm grades nothing and says so: the list is gov's own, withheld from
    installs by this kit's descriptor (TOOL-dGroundRules-17), and the `legacy-homes-present` case holds
    gov's own copy present. It says the same, and grades nothing, wherever `derive_census_tree` answers
    `adopter` or `invalid` (TOOL-dGroundRules-32 S11), a list at the installed kit's directory included: an adopter's list cannot hold gov's
    rows, so grading one would red every adopter (TOOL-dGroundRules-25 S11). A receipt that does not
    read, or two registries, is the one finding."""
    try:
        graded = policy.check_legacy_graded(repo, kit)
    except policy.Refusal as exc:
        return 0, "the tree under test did not derive", [(exc.path, exc.why)]
    if not graded:
        return None, policy.LEGACY_WITHHELD, []
    try:
        with policy.run_without_git_env():  # the base `lists --check` reads, by the one comparison
            compare = policy.resolve_compare_base(kit)
        reports, notes, rows, _new = policy.check_legacy_homes(repo, kit, compare)
    except policy.Refusal as exc:
        return 0, "the legacy homes were not graded", [(f"{exc.path}:{exc.line}", exc.why)]
    population = " · ".join([f"{len(rows)} row(s) derived from the legacy homes", *notes])
    return len(rows), population, [("legacy homes", r) for r in reports]


# ---- reader coverage (TOOL-dGroundRules-8) -----------------------------------------------------

# The reader shapes, one row per consumer shape: (the files the row reads, a suffix or a directory
# ending `/`, and its pattern). Group 2 is the key text the call passes; a new shape is one row.
READER_SHAPES = (
    # a call whose first argument is the key as a string literal: resolve("k"), mirror.get('k'), and
    # a literal holding the other quotes inside it, resolve(f'budgets."{cap}"') (TOOL-dGroundRules-21 S27)
    ((".py", ".js", ".mjs", ".cjs"),
     re.compile(r"[A-Za-z_$][\w$]*\([ \t]*(?:[fFrRbB]{1,2})?(['\"`])((?:(?!\1)[^\n\\])*)\1")),
    # a key joined around a name inside a quoted segment: resolve('budgets."' + name + '"'), read as
    # `budgets."{name}"` (S27)
    ((".py", ".js", ".mjs", ".cjs"),
     re.compile(r"[A-Za-z_$][\w$]*\([ \t]*(['\"])([^'\"\n]*\.\")\1[ \t]*\+[ \t]*([A-Za-z_$][\w$.]*)[ \t]*\+[ \t]*(['\"])\"\4")),
    # the reader CLI's get: policy.py get k, "$kit/policy.py" get "k" | ...
    ((".sh", ".githooks/"),
     re.compile(r"policy\.py[\"']?[ \t]+get[ \t]+([\"']?)([^\s'\"]+?)\1(?=[ \t;)|&]|$)")),
)
READER_SKIPPED = re.compile(r"(?:^|/)(?:[^/]*\.test\.(?:sh|js)|selftest[^/]*\.py|test_[^/]*\.py)$")
# a `*` or `<name>` segment: a quoted segment, which may hold `.` and an interpolated name, or one
# run of no quote, space, `.`, `(` or `)` (TOOL-dGroundRules-21 S27)
PATTERN_SEGMENT = r"(?:\"[^\"\n]*\"|[^'\"`\s.()]+)"


def derive_landed_owners(repo, kit=KIT):
    """-> the catalogue owners whose build has landed: at the landed revision `policy.py get` reads,
    the build folder `<memory root>/builds/<owner>/spec/` holds at least one spec and every spec's
    status header carries a token in tree_lib's TERMINAL, the memory root read from that revision's
    `.memory-tree.conf`. The landed revision's Refusal passes through. `tree_lib` is reached as the
    recall kit reaches it, through the inlined `resolve_kit_dir` from `kit`'s own location, the
    memory-tree kit named in this kit's `requires`, so a miss is a Refusal naming where the resolver
    looked, never "no build landed" (TOOL-dGroundRules-21 S26). A git read that fails is a Refusal
    naming it."""
    rows = policy.load_catalogue(kit)
    sha, _how = policy.derive_landed_revision(repo)
    try:
        tree_lib = load_tree_lib(kit)
    except (LookupError, ImportError) as exc:
        raise policy.Refusal("kit.toml", 0, f"requires memory-tree, which does not resolve: {exc}") from None
    owners = sorted({str(r["owner"]) for r in rows if r.get("owner")})
    if not owners:  # an ls-tree with no pathspec would list the whole revision
        return set()
    try:
        conf = tree_lib.read_blobs_at(repo, [(sha, ".memory-tree.conf")])[(sha, ".memory-tree.conf")]
        root = tree_lib.parse_conf(conf or "", {"MEMORY_ROOT": "memory"})["MEMORY_ROOT"].strip("/")
        listed = tree_lib.read_git_output(repo, ("ls-tree", "-r", "--name-only", sha, "--",
                                                 *(f"{root}/builds/{o}/spec/" for o in owners)))
        specs = [p for p in listed.decode("utf-8", "replace").split("\n") if p.endswith(".md")]
        texts = tree_lib.read_blobs_at(repo, [(sha, p) for p in specs])
    except OSError as exc:
        raise policy.Refusal(".memory-tree.conf", 0, f"the landed builds at {sha[:8]} do not read: {exc}") from None
    landed = set()
    for owner in owners:
        mine = [p for p in specs if p.startswith(f"{root}/builds/{owner}/spec/")]
        tokens = [next((m["token"] for m in map(tree_lib.HDR_RE.match, (texts[(sha, p)] or "").split("\n")) if m), None)
                  for p in mine]
        if tokens and all(t in tree_lib.TERMINAL for t in tokens):
            landed.add(owner)
    return landed


def scan_reader_keys(repo, kit=KIT):
    """-> every key text a call of READER_SHAPES passes in the tracked code of `repo`, read from disk:
    `git ls-files` with a row's suffix or under its directory, outside the memory root and `help/`,
    never a `*.test.sh`, `*.test.js`, `selftest*.py` or `test_*.py`, nor this module at `kit`'s path,
    whose fixtures name keys without consuming them. A line opening `#` or `//` is a comment."""
    own = (policy.run_git(kit, "rev-parse", "--show-prefix") or "").strip() + Path(__file__).name
    skip = (read_memory_root(repo) + "/", "help/")
    spelled = set()
    for f in (policy.run_git(repo, "ls-files", "-z", "--", *CODE_PATHSPECS) or "").split("\0"):
        if not f or f.startswith(skip) or f == own or READER_SKIPPED.search(f):
            continue
        shapes = [rx for files, rx in READER_SHAPES
                  if any(f.startswith(p) if p.endswith("/") else f.endswith(p) for p in files)]
        try:
            text = Path(repo, f).read_text(encoding="utf-8", errors="replace") if shapes else ""
        except OSError:
            continue
        for line in text.splitlines():
            if not line.lstrip().startswith(("#", "//")):
                # a joined key's text is its literal with the name spliced in as `{name}"`
                spelled.update(m[2] + ("{" + m[3] + "}\"" if m.re.groups == 4 else "")
                               for rx in shapes for m in rx.finditer(line))
    return spelled


def check_key_read(key, spelled, names):
    """True when a spelled key text reads catalogue key `key`: the key itself, or, for a key holding
    a `*` or `<name>` segment, a text that spells it with each such segment one PATTERN_SEGMENT run
    and that is no other catalogue key of `names`."""
    if key in spelled:
        return True
    segs = key.split(".")
    if not any(s == "*" or (s.startswith("<") and s.endswith(">")) for s in segs):
        return False
    rx = re.compile(r"\.".join(PATTERN_SEGMENT if s == "*" or (s.startswith("<") and s.endswith(">"))
                               else re.escape(s) for s in segs))
    return any(s not in names and rx.fullmatch(s) for s in spelled)


def check_reader_coverage(repo, landed=None, kit=KIT):
    """-> (the count of keys graded, one finding per graded key with no reader): a key is graded when
    its catalogue owner has landed, `derive_landed_owners` unless `landed` names the set, and read
    when `scan_reader_keys` finds a call passing it. Prints the summary line on every run, and the
    announce line when it graded nothing. A Refusal reading the landed revision passes through."""
    rows = policy.load_catalogue(kit)
    sha, _how = policy.derive_landed_revision(repo)
    owners = derive_landed_owners(repo, kit) if landed is None else set(landed)
    graded = [r for r in rows if r.get("owner") in owners]
    spelled = scan_reader_keys(repo, kit) if graded else set()
    names = {str(r.get("name")) for r in rows}
    findings = [f"reader coverage: {r['name']} (owner {r['owner']}, landed at {sha[:8]}) has no reader"
                for r in graded if not check_key_read(str(r["name"]), spelled, names)]
    print(f"reader coverage: graded {len(graded)} of {len(rows)} catalogue key(s); "
          f"landed owners: {', '.join(sorted(owners)) or 'none'}")
    if not graded:
        print(f"reader coverage: graded 0, so this arm checked nothing at {sha[:8]}")
    return len(graded), findings


def arm_reader_coverage(repo, kit):
    """`check_reader_coverage` over the repository: its population the catalogue's keys whose owner
    has landed, so before any Owner build lands it is 0, which this arm announces, never a finding
    (TOOL-dGroundRules-21 S5), and so is a landed revision that does not resolve, before any landing
    (TOOL-dGroundRules-25 S26). A Refusal, a landed build or memory-tree kit that does not read, is the
    one finding."""
    rows, bad = load_rows(kit)
    if bad:
        return 0, "the catalogue did not parse", [bad]
    try:
        policy.derive_landed_revision(repo)
    except policy.Refusal as exc:  # announced: no landing yet is legal (TOOL-dGroundRules-25 S26)
        return None, f"no landed revision: {exc.why}", []
    try:
        n, findings = check_reader_coverage(repo, kit=kit)
    except policy.Refusal as exc:
        return len(rows), "no landed owners to grade", [(f"{exc.path}:{exc.line}", exc.why)]
    return (n, f"{n} of {len(rows)} catalogue key(s) graded for a reader" + ("" if n else ", no owner build landed"),
            [tuple(f.split(": ", 1)) for f in findings])


# ---- the size caps (TOOL-dGroundRules-9) --------------------------------------------------------

# A request of the size switch as an enforcer spells it: a verb of budgets.py's CLI, a
# `resolve_caps` list, or the roles kit's `read_cap_answer`. `args` is the CLI's argument run, `list`
# the Python list's body and `one` the single request; a `$`-led or braced cap is DYNAMIC, named by
# the subject at run time.
REQUEST_SHAPES = re.compile(
    r"budgets\.py[\"']?[ \t]+(?P<verb>resolve|check)(?P<args>[^\n|;&)]*)"
    r"|resolve_caps\(\s*\[(?P<list>[^\]]*)\]"
    r"|read_cap_answer\(\s*(?P<one>[^,)]*)")
# An enforcer that asks the switch at all: a shape above, the policy kit's resolver anchor, or a
# call of budgets.py's own CLI entry from an embedded program.
ASKS_SHAPE = re.compile(r"budgets\.py|resolve_caps\(|read_cap_answer\(|budgets\.main\(")
LITERAL_SHAPE = re.compile(r"""[fFrRbB]{0,2}(["'])([^"'\n]*)\1""")
COMMENT_LEADS = ("#", "//")


def scan_cap_requests(text):
    """-> one entry per request REQUEST_SHAPES finds on a line that is not a comment: the cap a
    literal names, or None for a dynamic request. A request's cap is its text before `=`; a `check`
    run's last argument is the measure, never a cap."""
    out = []
    for line in text.splitlines():
        if line.lstrip().startswith(COMMENT_LEADS):
            continue
        for m in REQUEST_SHAPES.finditer(line):
            if m["verb"]:
                toks = [t.strip("\"'") for t in m["args"].split()]
                toks = [t for t in toks if t and not t.startswith("-") and ">" not in t]
                caps = toks[:-1] if m["verb"] == "check" else toks
            else:
                body = m["list"] if m["list"] is not None else m["one"]
                caps = [s for _q, s in LITERAL_SHAPE.findall(body)] or [None]
            out += [None if c is None or c.startswith("$") or "{" in c.split("=")[0] else c.split("=")[0]
                    for c in caps]
    return out


def derive_docstring_lines(text):
    """The 1-based lines inside a Python file's module, class and function docstrings, which read as
    comments; an empty set for text that does not parse."""
    try:
        tree = ast.parse(text)
    except (SyntaxError, ValueError):
        return set()
    out = set()
    for node in ast.walk(tree):
        body = getattr(node, "body", None)
        if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)) and body:
            first = body[0]
            if isinstance(first, ast.Expr) and isinstance(getattr(first, "value", None), ast.Constant) \
                    and isinstance(first.value.value, str):
                out.update(range(first.lineno, (first.end_lineno or first.lineno) + 1))
    return out


def derive_code_files(repo, kit):
    """The tracked code files, CODE_PATHSPECS, outside this kit's directory, the memory root and
    `help/`, and not a self-test by READER_SKIPPED: the population both size-cap arms read."""
    skip = tuple(p for p in ((policy.run_git(kit, "rev-parse", "--show-prefix") or "").strip(),
                             read_memory_root(repo) + "/", "help/") if p)
    return [f for f in (policy.run_git(repo, "ls-files", "-z", "--", *CODE_PATHSPECS) or "").split("\0")
            if f and not f.startswith(skip) and not READER_SKIPPED.search(f)]


# A READ of a file, never a mention (TOOL-dGroundRules-21 S18): a call or command that opens it,
# followed on its line by the file's name.
READ_SHAPE = r"(?:readFileSync|\bopen\(|\bcat\b|git show)"


def arm_single_reader(repo, path, reader_dir, const=""):
    """Each tracked code file of `derive_code_files`, outside `reader_dir`, the directory holding the
    file's one reader, the memory root, `help/` and the self-tests, that READS the file `path` names:
    a line that is neither a comment nor inside a Python docstring and spells READ_SHAPE followed on
    the line by the file's name, or names `const`, the constant its one reader defines for that name.
    ONE scanner for every file with one reader (TOOL-dGroundRules-21 S20): the mirror's arm and the
    limits file's are two rows of it in ARMS, so a mention in a comment, a docstring or a test's data
    reds neither, and a direct read reds both alike."""
    name = posixpath.basename(path)
    rx = re.compile(READ_SHAPE + r".*" + re.escape(name) + (rf"|\b{re.escape(const)}\b" if const else ""))
    prefix = (policy.run_git(reader_dir, "rev-parse", "--show-prefix") or "").strip()
    files = derive_code_files(repo, reader_dir)
    out = []
    for f in files:
        text = policy.read_text_or_none(Path(repo, f))
        if text is None or (name not in text and not (const and const in text)):
            continue
        doc = derive_docstring_lines(text) if f.endswith(".py") else set()
        hits = [str(n) for n, ln in enumerate(text.splitlines(), 1)
                if n not in doc and not ln.lstrip().startswith(COMMENT_LEADS) and rx.search(ln)]
        if hits:
            out.append((f, f"reads {name} at line {', '.join(hits)}; its one reader is in {prefix or 'this kit'}, "
                           "so ask that reader rather than reading the file"))
    return len(files), f"{len(files)} tracked code file(s) outside {prefix or 'the kit'}, the memory root, help/ and the self-tests", out


RECEIPT_REL, REGISTRY_REL = policy.RECEIPT_REL, policy.REGISTRY_REL  # the census tree is the core module's (TOOL-dGroundRules-76)


def arm_cap_census(repo, kit):
    """The cap census joined to the tree both ways (TOOL-dGroundRules-9).

    Census to tree, by the tree `derive_census_tree` answers (TOOL-dGroundRules-22): on the source
    tree each row's enforcer is a file at its `enforcer` path, `{prefix}` read as the directory holding
    the found `govkit/`, `ships` unread; on an `unadopted` tree, neither receipt nor registry, every
    row is announced as an adopter with no kit installed reads it (TOOL-dGroundRules-29); in an adopter a
    `ships = false` row is announced, `<name> · enforcer not shipped`, a row whose `kit` the receipt's
    `kits` lacks is announced, `<name> · kit <kit> not installed`, and every other row's enforcer is
    a file at its `installed` path, `{prefix}` read as the receipt's `prefix`. Each announce is one
    `cap census:` line. A graded `switch` row's enforcer asks the policy kit and names the cap on a
    line that is not a comment, a `limits:` row's naming it by the subject's key at run time; an
    outside row's enforcer makes no request naming it; and each row has its case in CAP_CASES. Tree
    to census: a request in a `derive_code_files` file naming a cap no row names, a CAP_CASES case for
    no row, and a row of the limits file in the tree, parsed by `budgets.parse_limits_rows`, no
    `limits:` row names. A census or a receipt that does not read, or two registries, is the one finding."""
    try:
        census = budgets.read_cap_census(repo)
    except policy.Refusal as exc:
        return 0, "the cap census did not read", [(f"{exc.path}:{exc.line}", exc.why)]
    try:
        tree, held = policy.derive_census_tree(repo)  # the receipt in an adopter, the tool root on the source
    except policy.Refusal as exc:
        return 0, "the tree under test did not derive", [(exc.path, exc.why)]
    if tree == "invalid":  # TOOL-dGroundRules-32 S11: a receipt of the wrong shape is no adopter that installed nothing
        return 0, "the install receipt did not read", [(RECEIPT_REL, f"its {held} is not of the shape the deployer writes")]
    out, told = [], []
    for cap in census.values():
        if tree == "source":
            rel = budgets.resolve_prefix_token(cap.enforcer, held)
            missing = f"its enforcer {rel} is not a file in this tree"
        elif not cap.ships:
            told.append(f"{cap.name} · enforcer not shipped")
            rel = None
        elif tree == "unadopted" or cap.kit not in (held.get("kits") or []):
            told.append(f"{cap.name} · kit {cap.kit} not installed")
            rel = None
        else:
            rel = budgets.resolve_prefix_token(cap.installed, held.get("prefix"))
            missing = f"its enforcer is not a file at {rel}, where kit {cap.kit} installs it"
        path = Path(repo, rel) if rel else None
        if path and not path.is_file():
            out.append((cap.name, missing))
        elif path:
            text = policy.read_text_or_none(path) or ""
            code = "\n".join(ln for ln in text.splitlines() if not ln.lstrip().startswith(COMMENT_LEADS))
            if cap.cls == "switch" and not ASKS_SHAPE.search(code):
                out.append((cap.name, f"its enforcer {rel} asks the policy kit nothing, so the switch never reaches it"))
            elif cap.cls == "switch" and not cap.home.startswith("limits:") \
                    and not re.search(rf"(?<![\w.-]){re.escape(cap.name)}(?![\w-])", code):
                out.append((cap.name, f"its enforcer {rel} never names it outside a comment"))
            elif cap.cls != "switch" and cap.name in scan_cap_requests(text):
                out.append((cap.name, f"is {cap.cls}, outside the switch, and its enforcer {rel} requests a mode for it"))
        if cap.name not in CAP_CASES:
            out.append((cap.name, f"has no budgets-cap-{cap.name} case in CAP_CASES"))
    out += [(name, "is a CAP_CASES case for no census row") for name in CAP_CASES if name not in census]
    files, asked = derive_code_files(repo, kit), 0
    for f in files:
        for cap in scan_cap_requests(policy.read_text_or_none(Path(repo, f)) or ""):
            asked += 1
            if cap is not None and cap not in census:
                out.append((cap, f"is requested by {f} and names no census row"))
    lrel = budgets.derive_limits_rel()
    lrows = budgets.parse_limits_rows(policy.read_text_or_none(Path(repo, lrel)))
    homes = {c.home.partition(":")[2] for c in census.values() if c.home.startswith("limits:")}
    out += [(k, f"is a row of {lrel} no limits: census row names, so nothing enforces it")
            for k in sorted(set(lrows) - homes)]
    for ln in told:
        print(f"cap census: {ln}")
    return len(census), (f"{len(census)} census row(s) joined to their enforcers and cases, {len(told)} announced "
                         f"· {asked} request(s) in {len(files)} tracked code file(s) · {len(lrows)} row(s) of {lrel}"), out


# One row per arm: its name, its function (repo, kit) -> (population, why, findings), what a
# population of 0 means, `finding` or `announce` (TOOL-dGroundRules-21 S5), the choice the README's
# "Each arm in an adopter" table opens its last column with, and the reason for that choice. Every row
# declares both, and `arms-empty-declared` reds one that does not (TOOL-dGroundRules-25 S26): an
# undeclared `empty` reads a 0 as a finding, so it can only red, never pass silently.
Arm = namedtuple("Arm", "name run empty why", defaults=(None, None))
ARMS = [
    Arm("arm_schema", arm_schema, empty="announce",
        why="no policy file, or one setting no key, is legal before --scaffold"),
    Arm("arm_shape", arm_shape, empty="finding", why="the catalogue ships in the kit, so it always has rows"),
    Arm("arm_summaries", arm_summaries, empty="finding", why="the catalogue the list is graded against ships in the kit"),
    Arm("arm_direction", arm_direction, empty="finding", why="the catalogue's bound rows ship in the kit"),
    Arm("arm_on_invalid", arm_on_invalid, empty="finding",
        why="its population is HEAD, never 0; a HEAD that names no commit or holds no file is announced"),
    Arm("arm_mirror_parity", arm_mirror_parity, empty="finding",
        why="HEAD's mirror always holds keys; a HEAD naming no commit, or carrying neither file, is announced"),
    Arm("arm_mirror_landed", arm_mirror_landed, empty="announce",
        why="a landed revision that does not resolve, or sets no key, is legal before the first landing"),
    Arm("arm_mirror_readers", lambda repo, kit: arm_single_reader(repo, policy.MIRROR_REL, kit), empty="announce",
        why="a tree with no tracked code is legal"),
    Arm("arm_legacy_homes", arm_legacy_homes, empty="finding",
        why="gov's own list derives rows; with no list, or in an adopter's tree, it is announced"),
    Arm("arm_reader_coverage", arm_reader_coverage, empty="announce",
        why="no owner build landed, or no landed revision, is legal"),
    Arm("arm_limits_readers", lambda repo, kit: arm_single_reader(repo, budgets.LIMITS_NAME, kit, "LIMITS_NAME"),
        empty="announce", why="a tree with no tracked code is legal"),
    Arm("arm_cap_census", arm_cap_census, empty="finding", why="the census ships in the kit, so it always has rows"),
]
ARM = {a.name: a for a in ARMS}


def run_arm(arm, repo, kit):
    """-> (the verdict `main` prints after the arm's name, findings) for an Arm row:
    `<k> finding(s) · <population>`, or `not graded · <why>` where the arm answers None for its
    population, an announce that grades nothing (TOOL-dGroundRules-17), or answers 0 with no finding
    and declares `empty = "announce"` (TOOL-dGroundRules-21 S5); a 0 under `finding` is one more
    finding, so an arm that read nothing cannot read green."""
    n, population, findings = arm.run(repo, kit)
    if n is None or (n == 0 and arm.empty == "announce" and not findings):
        return f"not graded · {population}", findings
    if n == 0:
        findings = findings + [("population", f"zero, so this arm graded nothing: {population}")]
    return f"{len(findings)} finding(s) · {population}", findings


# ---- the fixture -------------------------------------------------------------------------------

def set_row_block(text, name, edit):
    """`text` with the [[key]] block whose name is `name` passed through `edit`."""
    blocks = text.split("[[key]]\n")
    for i, b in enumerate(blocks):
        if b.startswith(f"name = {policy.render_json(name)}\n"):
            blocks[i] = edit(b)
            return "[[key]]\n".join(blocks)
    raise ValueError(f"the catalogue has no row {name}")


def write_edit(path, edit):
    path.write_text(edit(path.read_text(encoding="utf-8")), encoding="utf-8", newline="\n")


def derive_first_set_row(rows):
    return next(r["name"] for r in rows if isinstance(r.get("allowed"), dict) and r["allowed"].get("type") in policy.SET_TYPES)


def render_planted_row(summary):
    return (f'\n[[key]]\nname = "{PLANTED}"\nallowed = ["a"]\ndefault = "a"\n'
            + (f'summary = "{summary}"\n' if summary else "") + 'owner = "dGroundRules"\n')


def seed_empty_value(row):
    """The policy file sets this never-empty row's key to [], a placeholder segment filled as x."""
    segs = tuple("x" if s == "*" or (s.startswith("<") and s.endswith(">")) else s for s in row["name"].split("."))

    def seed(repo, kit, rows):
        Path(repo, *POLICY_FILE).write_text(f"{policy.render_dotted(segs)} = []\n", encoding="utf-8", newline="\n")
        return policy.render_dotted(segs), "never empty"
    return seed


def seed_no_empty(repo, kit, rows):
    name = derive_first_set_row(rows)
    write_edit(kit / policy.CATALOGUE, lambda t: set_row_block(
        t, name, lambda b: "".join(ln for ln in b.splitlines(keepends=True) if not ln.startswith("empty ="))))
    return name, "declares no `empty` rule"


def seed_unknown_field(repo, kit, rows):
    name = derive_first_set_row(rows)
    write_edit(kit / policy.CATALOGUE, lambda t: set_row_block(t, name, lambda b: b.replace("\n", '\nemtpy = "never"\n', 1)))
    return name, "unknown field `emtpy`"


def seed_usage_out_of_set(repo, kit, rows):
    write_edit(kit / policy.CATALOGUE, lambda t: set_row_block(
        t, "budgets.enforce", lambda b: re.sub(r"^usage = .*$", "usage = 'budgets.enforce = \"loud\"'", b, flags=re.M)))
    return "budgets.enforce", "its usage is refused"


def seed_summary_new_key(repo, kit, rows):
    write_edit(kit / policy.CATALOGUE, lambda t: t + render_planted_row(None))
    return PLANTED, "is not listed"


def seed_usage_new_key(repo, kit, rows):
    write_edit(kit / policy.CATALOGUE, lambda t: t + render_planted_row("A planted row with a summary and no usage."))
    return PLANTED, "is not listed"


def seed_list_grew(repo, kit, rows):
    write_edit(kit / policy.CATALOGUE, lambda t: t + render_planted_row(None))
    write_edit(kit / policy.LIST, lambda t: t + PLANTED + "\n")
    return PLANTED, "added to a shrink-only list"


def derive_first_bound(rows):
    return policy.derive_bounds(rows)[0]["name"]


def seed_direction_missing(repo, kit, rows):
    name = derive_first_bound(rows)
    write_edit(kit / policy.CATALOGUE, lambda t: set_row_block(
        t, name, lambda b: "".join(ln for ln in b.splitlines(keepends=True) if not ln.startswith("direction ="))))
    return name, "declares no direction"


def seed_direction_new_bound(repo, kit, rows):
    write_edit(kit / policy.CATALOGUE, lambda t: t + '\n[[key]]\nname = "zz.loop"\n'
               'allowed = { type = "retry-count", min = 1 }\ndefault = 3\nowner = "dGroundRules"\n')
    return "zz.loop", "declares no direction"


def seed_direction_wrong_value(repo, kit, rows):
    name = derive_first_bound(rows)
    write_edit(kit / policy.CATALOGUE, lambda t: set_row_block(
        t, name, lambda b: re.sub(r"^direction = .*$", 'direction = "raise-tightens"', b, flags=re.M)))
    return name, "must be raise-loosens"


# ---- the adopter's fresh target (TOOL-dGroundRules-16) ------------------------------------------

FRESH_TARGET = "adopter-fresh-target"
ADOPTER_SECTION = "Each arm in an adopter"


resolve_kit_dir = policy.resolve_kit_dir  # the kit's one inlined copy, in policy.py


def load_tree_lib(kit=KIT):
    """The memory-tree kit's `tree_lib`, its directory found by `resolve_kit_dir` from `kit`, this
    kit's own location unless a copy names its own (TOOL-dGroundRules-21 S25) -> the module;
    LookupError where no memory-tree kit is installed, ImportError where it does not import."""
    lib = str(resolve_kit_dir("memory-tree", "tree_lib.py", kit))
    if lib not in sys.path:
        sys.path.insert(0, lib)
    import tree_lib
    return tree_lib


# The run-gates kit's rule, profile_bar.py's `resolve_bash` (TOOL-dGroundRules-21 S14), inlined from
# its canonical block (TOOL-dGroundRules-25 S28).
# >>> resolve_bash_py -- canonical copy: resolve_bash.py in the gov lib dir (byte-identical; gated)
def resolve_bash(script):
    r"""The bash that can SEE `script`, by RUNNING each candidate, or None. GOV_BASH first, then the
    bash PATH names, then Git for Windows' two paths, each kept only when `test -f` on the script
    exits 0 under it. On Windows PATH order commonly puts the System32 WSL launcher first, which
    cannot open a `C:/` path, and a stub that exits 127 can sit there too (gotcha
    subprocess-resolves-a-different-shell); being on PATH is not evidence."""
    cands = [os.environ.get("GOV_BASH", ""), shutil.which("bash") or "",
             "C:/Program Files/Git/bin/bash.exe", "C:/Program Files/Git/usr/bin/bash.exe", "bash"]
    tried = []
    for c in cands:
        if not c or c in tried:
            continue
        tried.append(c)
        try:
            r = subprocess.run([c, "-c", 'test -f "$1"', "_", str(script)], capture_output=True, timeout=20)
        except (OSError, subprocess.SubprocessError):
            continue
        if r.returncode == 0:
            return c
    return None
# <<< resolve_bash_py


def run_adopter_suite(name):
    """`adopter-suite` (TOOL-dGroundRules-21 S4): `adopt-policy.test.sh`, the adopter's sibling suite,
    which arms each of its refusal branches, run under the bash `resolve_bash` finds able to see it,
    so a leg executes the arms `check-arms.py` reads. The pass is its exit 0 AND its closing count line
    naming at least one arm passed and none failed (TOOL-dGroundRules-25 S29): a suite that is absent,
    that no bash can see, or that never reached its count is a WRONG, never a skip."""
    suite = KIT / "adopt-policy.test.sh"
    if not suite.is_file():
        return print_checks(name, [(name, f"{suite.name} beside the adopter", False, "absent, so no arm ran")])
    bash = resolve_bash(suite.as_posix())
    if bash is None:
        return print_checks(name, [(name, "a bash that can see the suite", False, "none: set GOV_BASH")])
    rc, out = run_case_argv(KIT, [bash, suite.as_posix()])
    count = re.search(r"^==== ([1-9][0-9]*) passed, 0 failed ====$", out, flags=re.M)
    return print_checks(name, [(name, f"bash {suite.name} exits 0 naming its arm count", rc == 0 and bool(count),
                                f"exit {rc} · {render_said(out, 'passed')}")])


def extract_arm_rows(text):
    """The README's "Each arm in an adopter" table -> {backticked first-column name: the leading word
    of its last column, `announce` or `finding` as written}, in order (TOOL-dGroundRules-25 S8)."""
    parts = text.replace("\r", "").split(f"\n## {ADOPTER_SECTION}\n", 1)
    section = parts[1].split("\n## ", 1)[0] if len(parts) == 2 else ""
    return {m[1]: m[2] for m in re.finditer(r"^\| `([^`]+)` \|.*\| ([A-Za-z-]*)[^|]*\|[ \t]*$", section, flags=re.M)}


def check_arm_lines(out, names):
    """-> one message per arm of `names` whose `--check` line in `out` is neither graded with no
    finding nor an announce, carrying its finding lines."""
    lines = out.replace("\r", "").split("\n")
    bad = []
    for arm in names:
        head = f"policy-check: {arm} · "
        at = next((i for i, ln in enumerate(lines) if ln.startswith(head)), None)
        if at is None:
            bad.append(f"{arm} printed neither its graded line nor an announce line")
            continue
        verdict = lines[at][len(head):]
        if verdict.startswith(("0 finding(s) · ", "not graded · ")):
            continue
        found = []
        for ln in lines[at + 1:]:
            if not ln.startswith("  "):
                break
            found.append(ln.strip())
        bad.append(f"{arm} {verdict.split(' · ')[0]}: " + "; ".join(found))
    return bad


SNAPSHOT_ROOTS = set()  # each root build_source_snapshot made, resolved: the roots run_govkit admits (TOOL-dGroundRules-34 S9)


def build_source_snapshot(source_root):
    """The root of a scratch clone whose HEAD commits `source_root`'s working tree over its HEAD
    (TOOL-dGroundRules-26). The deployer installs its own checkout's HEAD, never a working tree, so a
    case that installs through the clone's deployer grades the bytes under test, a file only the
    working tree holds included. `--shared` reads the source's objects through alternates, and with
    GIT_DIR set to the clone every new object lands in the clone's store, never the source's. `add -A`
    runs over a copy of the source's index with the source as work tree, and with the source's
    exclude file copied into the clone's (TOOL-dGroundRules-34 S1, S3), so the `.gitignore` files, that
    exclude file and the `core.excludesFile` the source reads, passed as `-c` (TOOL-dGroundRules-43
    S10), decide what counts, the rules `git status` in the
    source reads, and a file whose stat matches is not re-hashed. Every `--git-path` is absolute (S28),
    never resolved against the caller's working directory. A gitlink the source's index does not
    carry, a nested repository no ignore rule covers, is refused naming it and the exclude file (S4).
    Every git call runs with the memory-tree kit's GIT_ENV_LEAKS stripped, the copy the reader inlines
    (TOOL-dGroundRules-21 S9), so an ambient GIT_DIR or GIT_INDEX_FILE cannot retarget it. The root is
    added, resolved, to SNAPSHOT_ROOTS, the one set `run_govkit` admits (S9). The caller removes the
    root. -> Path; RuntimeError naming the failed step and git's first stderr line, the clone already
    removed."""
    base = {k: v for k, v in os.environ.items() if k not in policy.GIT_ENV_LEAKS}

    def run(step, *args, cwd=None, **env):
        p = subprocess.run(["git", "-c", "user.name=policy-fixture", "-c", "user.email=policy-fixture@invalid",
                            "-c", "commit.gpgsign=false", *args], cwd=cwd, env={**base, **env},
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        if p.returncode:
            first = next((ln.strip() for ln in p.stderr.splitlines() if ln.strip()), "git printed nothing on stderr")
            raise RuntimeError(f"the snapshot's {step} step exited {p.returncode}: {first}")
        return p.stdout.strip()

    source = Path(source_root)
    s = Path(tempfile.mkdtemp(prefix="pol-"))
    try:
        run("clone", "clone", "--quiet", "--shared", "--no-checkout", source.as_posix(), s.as_posix())
        index = s / ".git" / "snapshot-index"
        held, ex = (Path(run(step, "-C", source.as_posix(), "rev-parse", "--path-format=absolute", "--git-path", rel))
                    for step, rel in (("index", "index"), ("exclude", "info/exclude")))
        if held.is_file():  # a source with no index yet starts the snapshot from an empty one
            shutil.copyfile(held, index)
        if ex.is_file():  # a linked worktree's resolves to the common directory's, which every checkout shares
            (s / ".git" / "info").mkdir(exist_ok=True)
            shutil.copyfile(ex, s / ".git" / "info" / "exclude")
        env = {"GIT_DIR": (s / ".git").as_posix(), "GIT_WORK_TREE": source.as_posix(), "GIT_INDEX_FILE": index.as_posix()}
        # TOOL-dGroundRules-43 S10: the source's effective core.excludesFile, every scope it sees, its
        # worktree configuration included; the clone's GIT_DIR alone would read the global one only
        xf = (policy.run_git(source, "config", "--type=path", "--get", "core.excludesFile") or "").strip()
        run("add", *(("-c", f"core.excludesFile={xf}") if xf else ()), "add", "-A", cwd=source, **env)
        tree = run("write-tree", "write-tree", **env)
        commit = run("commit-tree", "commit-tree", tree, "-p", "HEAD", "-m", "the working tree under test", **env)
        run("checkout", "-C", s.as_posix(), "checkout", "--quiet", "--detach", commit)
        links = [{ln.split("\t", 1)[1] for ln in run(step, "-C", repo.as_posix(), *argv).splitlines()
                  if ln.startswith("160000 ")} for step, repo, argv in
                 (("ls-tree", s, ("ls-tree", "-r", "HEAD")), ("ls-files", source, ("ls-files", "-s")))]
        nested = sorted(links[0] - links[1])
        if nested:
            raise RuntimeError(f"the snapshot holds {', '.join(nested)} as a gitlink the source's index does not "
                               f"carry: a nested repository no ignore rule covers; ignore it in {ex.as_posix()}")
    except BaseException:
        remove_repo(s)
        raise
    SNAPSHOT_ROOTS.add(s.resolve())
    return s


def derive_requires_closure(ids):
    """-> (the registry ids `ids` and the closure of each entry's descriptor `requires`, in order; one
    message per id the deployer's registry does not resolve). Each id is read as a REGISTRY id, its
    descriptor the `descriptor` field of the registry under this kit's tool root, `{prefix}` resolved,
    never as a kit home: `agent-cap` is homed in `hooks` (TOOL-dGroundRules-25 S6)."""
    troot = budgets.derive_tool_root()
    top = Path((policy.run_git(KIT, "rev-parse", "--show-toplevel") or "").strip() or KIT.parent)
    reg = top / budgets.resolve_prefix_token("{prefix}/govkit/registry.toml", troot)
    try:
        entries = {str(e.get("id")): str(e.get("descriptor")) for e in
                   tomllib.loads(reg.read_text(encoding="utf-8")).get("entry", []) if isinstance(e, dict)}
    except (OSError, tomllib.TOMLDecodeError) as exc:
        return list(ids), [f"the deployer's registry does not read: {type(exc).__name__}: {exc}"]
    out, todo, wrong = [], list(ids), []
    while todo:
        eid = todo.pop(0)
        if eid in out:
            continue
        out.append(eid)
        if eid not in entries:
            wrong.append(f"{eid} is selected or required and is no entry of {reg.relative_to(top).as_posix()}")
            continue
        try:
            desc = top / budgets.resolve_prefix_token(entries[eid], troot)
            todo += tomllib.loads(desc.read_text(encoding="utf-8")).get("requires", [])
        except (OSError, tomllib.TOMLDecodeError) as exc:
            wrong.append(f"the descriptor of {eid} does not read: {type(exc).__name__}: {exc}")
    return out, wrong


def resolve_govkit(root):
    """The deployer under `root` (TOOL-dGroundRules-34 S7, S8), located by `resolve_kit_dir`, home
    `govkit`, anchor `govkit.py`, from `<root>/<tool root>/policy`, the tool root this kit's own, as
    `budgets.derive_tool_root` resolves it (TOOL-dGroundRules-24 S4, TOOL-dGroundRules-43 S15).
    The one line of this file spelling the deployer's file name: every deployer run and the in-process
    load of `budgets-ships-join` take the path from here. -> Path; RuntimeError carrying the locator's
    LookupError text whole, the three places looked, so a missing deployer is one named WRONG wherever
    it is asked for."""
    try:  # TOOL-dGroundRules-43 S15: the kit's one locator, its refusal raised as the RuntimeError callers catch
        return resolve_kit_dir("govkit", "govkit.py", Path(root) / budgets.derive_tool_root() / "policy") / "govkit.py"
    except LookupError as exc:
        raise RuntimeError(str(exc)) from None


def read_deploy_answers(source_root):
    """`DEPLOY_FULL`'s `[answers]` in the deployer's own suite beside it under `source_root`
    (TOOL-dGroundRules-34 S23), read with `ast`, never imported: importing the suite runs its vintage
    pin and prints. The module's `DEPLOY_FULL` assignment, its constant string parts joined, a
    formatted part dropped, parsed with `tomllib`. -> {key: value}; RuntimeError naming the file where
    no such assignment is, or where the joined text does not parse into an `[answers]` table."""
    suite = resolve_govkit(source_root).with_name("selftest.py")
    try:
        tree = ast.parse(suite.read_text(encoding="utf-8"))
    except (OSError, SyntaxError, ValueError) as exc:
        raise RuntimeError(f"{suite.as_posix()} does not parse: {exc}") from None
    value = next((n.value for n in tree.body if isinstance(n, ast.Assign)
                  and any(isinstance(t, ast.Name) and t.id == "DEPLOY_FULL" for t in n.targets)), None)
    parts = value.values if isinstance(value, ast.JoinedStr) else [value]
    text = "".join(p.value for p in parts if isinstance(p, ast.Constant) and isinstance(p.value, str))
    try:
        answers = tomllib.loads(text).get("answers") if value is not None else None
    except tomllib.TOMLDecodeError as exc:
        raise RuntimeError(f"DEPLOY_FULL in {suite.as_posix()} does not parse: {exc}") from None
    if not isinstance(answers, dict) or not answers:
        raise RuntimeError(f"no [answers] table of DEPLOY_FULL to install with in {suite.as_posix()}")
    return {str(k): str(v) for k, v in answers.items()}


def remove_gate_runner(desc):
    """Drop the `[gate_runner]` table `intake` seeds into the descriptor `desc` (TOOL-dGroundRules-34
    S22), its header comment and any `[gate_runner.*]` sub-table with it: a fixture target has no gate
    history, and with the table `apply` grades each leg it emits as new and reds. RuntimeError naming
    `desc` when the stripped text still parses to a `gate_runner` key or does not parse."""
    kept, skip = [], False
    for line in desc.read_text(encoding="utf-8").splitlines(keepends=True):
        if line.startswith(("# [gate_runner]", "[gate_runner")):
            skip = True
        elif skip and line.startswith("["):
            skip = False
        if not skip:
            kept.append(line)
    text = "".join(kept)
    try:
        left = "gate_runner" in tomllib.loads(text)
    except tomllib.TOMLDecodeError as exc:
        raise RuntimeError(f"{desc.as_posix()} does not parse once its [gate_runner] is stripped: {exc}") from None
    if left:
        raise RuntimeError(f"{desc.as_posix()} still declares a gate_runner after the strip")
    desc.write_text(text, encoding="utf-8", newline="")


def build_install_target(name, ids):
    """A fresh target ready for the deployer (TOOL-dGroundRules-24, -26): `build_source_snapshot`'s
    clone of the tree under test, and beside it `git init` with a pinned autocrlf and a one-line README,
    over which the snapshot's deployer runs `intake` (TOOL-dGroundRules-34 S22): `ids` as `--kits`,
    this kit's tool root's name as the `prefix` answer, and one `--answer` per key of
    `read_deploy_answers`, so `intake` writes `.governance/deploy.toml`, the answers the closure needs
    and its `[gate_runner]` seed, and this builder types no descriptor and no answer list; the seed is
    then stripped (`remove_gate_runner`), and the target committed once, through `run_fixture_git`.
    Prints the snapshot line, with the snapshot's file count and the seconds it took (S27). -> (target, snapshot), which `run_govkit` installs from; the caller removes
    both directories. RuntimeError naming what is missing or which step failed, `intake`'s own refusal
    included, nothing left behind."""
    root = KIT.parent  # this kit's own resolved tool root; the target's prefix is its name, never spelled
    top = derive_source_top()
    if not top.parts:
        raise RuntimeError(f"no tree under test to snapshot: {KIT.as_posix()} is in no git repository")
    began = time.monotonic()
    try:
        s = build_source_snapshot(top)
    except (RuntimeError, OSError) as exc:
        raise RuntimeError(f"nothing was installed to grade: {exc}") from None
    took = time.monotonic() - began
    t = Path(tempfile.mkdtemp(prefix="pol-"))
    try:
        answers = read_deploy_answers(top)
        snap, over = (policy.run_git(s, "rev-parse", "HEAD", "HEAD^") or "? ?").split()
        files = len((policy.run_git(s, "ls-tree", "-r", "HEAD") or "").splitlines())
        print(f"{name}: installing from snapshot {snap[:8]} of the working tree over HEAD {over[:8]} · "
              f"{files} files · {took:.1f}s")
        run_fixture_git(t, "init", "-q")
        run_fixture_git(t, "config", "core.autocrlf", "false")
        (t / "README.md").write_text("A fresh adopter of the policy kit.\n", encoding="utf-8", newline="\n")
        rc, out = run_govkit(s, top, "intake", "--target", t.as_posix(), "--kits", ",".join(ids),
                             "--answer", f"prefix={root.name}",
                             *(a for k, v in answers.items() for a in ("--answer", f"{k}={v}")))
        if rc:
            raise RuntimeError(f"the deployer's intake --kits {','.join(ids)} exited {rc}: {out.strip()}")
        remove_gate_runner(t / ".governance" / "deploy.toml")
        run_fixture_git(t, "add", "-A")
        run_fixture_git(t, "commit", "-q", "-m", "a fresh target")
    except BaseException:
        remove_repo(t)
        remove_repo(s)
        raise
    return t, s


def run_govkit(snapshot_root, source_root, *argv):
    """The one run of the deployer a case makes (TOOL-dGroundRules-27): `python <the deployer
    resolve_govkit finds under snapshot_root> <argv>`, with the remote probe off and GIT_ENV_LEAKS
    stripped. The deployer installs its own checkout's HEAD, so any root `build_source_snapshot` did
    not make, `source_root` itself, a directory under it, a clone made by another route or the two
    arguments swapped, would grade some HEAD, never the bytes under test: a `snapshot_root` whose
    resolved path is not in SNAPSHOT_ROOTS is a RuntimeError naming it and `build_source_snapshot`,
    before any process starts (TOOL-dGroundRules-34 S9, S10). RuntimeError naming the path it looked at
    when the snapshot holds no deployer. -> (exit, output).

    Not the govkit kit's `run_in_gov` (its `matrix.py`), nor the `clone -q --local` checkout that
    harness runs it from (TOOL-dGroundRules-34 S33): this kit cannot import a sibling kit's test
    harness, `run_in_gov` has no source-root refusal, and its frozen clone grades HEAD, the exposure
    units 26 and 27 close for the policy cases."""
    if Path(snapshot_root).resolve() not in SNAPSHOT_ROOTS:
        raise RuntimeError(f"run_govkit: {Path(snapshot_root).as_posix()} is no root build_source_snapshot made "
                           f"of {Path(source_root).as_posix()}; take build_source_snapshot first")
    govkit = resolve_govkit(snapshot_root)  # the clone's deployer installs its HEAD
    env = {k: v for k, v in os.environ.items() if k not in policy.GIT_ENV_LEAKS}
    p = subprocess.run([sys.executable, str(govkit), *argv], capture_output=True, text=True, encoding="utf-8",
                       errors="replace", env=dict(env, GOVKIT_NO_REMOTE_PROBE="1"))
    return p.returncode, (p.stdout + p.stderr).replace("\r", "")


def read_receipt_rows(t):
    """The install receipt's `files` rows of target `t`, each a dict."""
    return [r for r in json.loads(Path(t, RECEIPT_REL).read_text(encoding="utf-8")).get("files") or []
            if isinstance(r, dict)]


def run_fresh_target(name):
    """This kit installed by the deployer into a fresh target (TOOL-dGroundRules-24, -26): by
    `build_install_target`, then the deployer's `apply` through `run_govkit` with this kit's id and `run-gates`, and the closure
    of their `requires` read as registry ids (TOOL-dGroundRules-25 S6, S7). Every file under the
    target's tool root must be a receipt row's `path`, the deployer's `check` must print no `is in the
    receipt and not on disk` line (TOOL-dGroundRules-32 S18), the receipt's `gov_source` must be the
    snapshot root (TOOL-dGroundRules-34 S29), and no `legacy-homes.txt` may be installed (S5). Then the installed `adopt-policy.sh`, found through
    its receipt row: `--scaffold`, exit 0 printing `mirror deferred` and writing no mirror, the
    install being staged (TOOL-dGroundRules-31); `--check` with the install staged; the install
    committed; `--scaffold` again, which renders the mirror once its inputs are committed, and the
    installed `policy.py mirror --check`, exit 0; the mirror committed (S7); `--check` again; and the installed `regen.py --check`, exit 0, the adopter's bar's
    preflight. Each `--check` must exit 0 with every arm graded clean or announced (S26), print
    `arm_schema` grading the scaffold's keys with no finding, `arm_mirror_readers` grading at least one
    staged code file of the memory-tree kit with no finding, the reader-coverage arm `not graded`, and
    `arm_legacy_homes` `not graded · the list is gov's own` (S5); with an adopter-written list at the
    installed kit's directory, `--check` must still announce it and find nothing (S11). The README's
    table is joined to ARMS both ways, and each row's last column opens with its arm's `empty` (S8); and
    an Arm planted with a population of 0 must print one finding under `finding` and none, `not graded`,
    under `announce` (TOOL-dGroundRules-21 S5). A missing deployer, a refused `run_govkit` or a refused `apply` is a WRONG,
    and nothing after it runs. Prints its lines. -> (assertions, wrong)."""
    names = [a.name for a in ARMS]
    listed = extract_arm_rows((KIT / "README.md").read_text(encoding="utf-8"))
    wrong = [f"{n} is in ARMS with no row in README.md \"{ADOPTER_SECTION}\" (unlisted)" for n in names if n not in listed]
    wrong += [f"README.md \"{ADOPTER_SECTION}\" lists {n}, which ARMS lacks (stale)" for n in listed if n not in names]
    wrong += [f"{a.name} declares empty = {a.empty!r} and its README.md \"{ADOPTER_SECTION}\" row opens its last "
              f"column with {listed[a.name]!r}" for a in ARMS if a.name in listed and listed[a.name] != a.empty]
    asserted = 2 * len(set(names) | set(listed)) + 2
    for empty, want in (("finding", "1 finding(s) · "), ("announce", "not graded · ")):
        verdict, _f = run_arm(Arm("planted", lambda _r, _k: (0, "a planted empty population", []), empty), None, KIT)
        asserted += 1
        if not verdict.startswith(want):
            wrong.append(f"an Arm planted with population 0 under `{empty}` printed {verdict!r}, not {want!r}")
    keys = sum(1 for _ in policy.scan_keys(tomllib.loads(policy.render_scaffold(policy.load_catalogue(KIT))), []))
    lines = {"arm_schema": re.compile(rf"0 finding\(s\) · {keys} key\(s\) of "),
             "arm_mirror_readers": re.compile(r"0 finding\(s\) · [1-9][0-9]* tracked code file\(s\)"),
             "arm_reader_coverage": re.compile(r"not graded · "),
             "arm_legacy_homes": re.compile(r"not graded · the list is gov's own")}
    desc = tomllib.loads((KIT / "kit.toml").read_text(encoding="utf-8"))
    ids, missed = derive_requires_closure([desc["id"], "run-gates"])
    wrong += missed
    root, rows, t, s = KIT.parent, None, None, None
    try:
        try:  # a refused run_govkit is this case's WRONG, as a failed snapshot is (TOOL-dGroundRules-27)
            t, s = build_install_target(name, ids)
            rc, out = run_govkit(s, derive_source_top(), "apply", "--target", t.as_posix(), "--kits", ",".join(ids))
            if rc:
                wrong.append(f"the deployer's apply --kits {','.join(ids)} exited {rc}, so nothing was installed to "
                             f"grade: {out.strip()}")
            else:
                rows = read_receipt_rows(t)
                # TOOL-dGroundRules-34 S29: the checkout that installed the target is the snapshot.
                said = json.loads(Path(t, RECEIPT_REL).read_text(encoding="utf-8")).get("gov_source")
                asserted += 1
                if not isinstance(said, str) or Path(said).resolve() != s.resolve():
                    wrong.append(f"the receipt's gov_source is {said!r}, not the snapshot {s.as_posix()}, so the "
                                 "tree under test is not what installed the target")
        except (RuntimeError, OSError, subprocess.CalledProcessError) as exc:
            wrong.append(str(exc))
        if rows is not None:
            paths = {r.get("path") for r in rows}
            held = sorted(f.relative_to(t).as_posix() for f in (t / root.name).rglob("*") if f.is_file())
            stray = [f"{f} is under the tool root and is no receipt row's path (stray)" for f in held if f not in paths]
            # TOOL-dGroundRules-32 S18: a receipt row missing from disk is the deployer's own check's to say.
            _rc, said = run_govkit(s, derive_source_top(), "check", "--target", t.as_posix())
            stray += [ln.strip() for ln in said.split("\n") if "is in the receipt and not on disk" in ln]
            stray += [f"{f} is installed, and the list is gov's own, withheld from every install (S5)"
                      for f in held if posixpath.basename(f) == policy.LEGACY_LIST]
            asserted += len(held) + 2
            wrong += stray
            if not stray:
                print(f"policy-fixture: {name} · apply --kits {','.join(ids)} exited 0 into its target · the "
                      f"{len(held)} file(s) under {root.name}/ are each a receipt row's path, and govkit check "
                      f"finds every receipt row on disk · no {policy.LEGACY_LIST} installed")
            adopter = next((r["path"] for r in rows if r.get("kit") == desc["id"]
                            and str(r.get("path")).endswith("/adopt-policy.sh")), None)
            regen = next((r["path"] for r in rows if r.get("kit") == "run-gates"
                          and str(r.get("path")).endswith("/regen.py")), None)
            bash = resolve_bash((t / adopter).as_posix()) if adopter else None
            if adopter is None:
                wrong.append(f"the receipt has no row of kit {desc['id']} whose path ends in adopt-policy.sh")
            elif bash is None:
                wrong.append("no bash on PATH shares this filesystem: each was a System32 or WindowsApps launcher, "
                             "or none ran; set GOV_BASH")
            else:
                def run_adopter(mode):
                    p = subprocess.run([bash, (t / adopter).as_posix(), mode, "--target", t.as_posix()],
                                       capture_output=True, text=True, encoding="utf-8", errors="replace")
                    return p.returncode, p.stdout + p.stderr

                def grade_check(phase):
                    nonlocal asserted
                    rc, out = run_adopter("--check")
                    bad = check_arm_lines(out, names)
                    asserted += len(names) + 1 + len(lines)
                    wrong.extend(f"{phase}: {b}" for b in bad)
                    for arm, rx in lines.items():
                        said = next((ln for ln in out.replace("\r", "").split("\n")
                                     if ln.startswith(f"policy-check: {arm} · ")), "(no line)")
                        if not rx.search(said):
                            wrong.append(f"{phase}: {arm} printed {said!r}, not /{rx.pattern}/")
                    if rc:
                        wrong.append(f"{phase}: --check exited {rc}" + ("" if bad else f": {out.strip()}"))
                rc, out = run_adopter("--scaffold")  # TOOL-dGroundRules-31: the install is staged, so the mirror defers
                asserted += 1
                deferred, mirrored = "mirror deferred" in out, Path(t, *MIRROR_FILE).is_file()
                if rc or not deferred or mirrored:
                    wrong.append(f"the install-day --scaffold exited {rc}, printed {'' if deferred else 'no '}`mirror "
                                 f"deferred` and left {'a' if mirrored else 'no'} {policy.MIRROR_REL}: {out.strip()}")
                # TOOL-dGroundRules-41 S1: the help page's `## Install` section restates the printed deferral
                # line; one of its lines must hold the line's halves either side of the input name, in order.
                printed = next((ln.strip() for ln in out.replace("\r", "").split("\n")
                                if ln.strip().startswith("adopt-policy: mirror deferred")), None)
                if printed is not None:
                    asserted += 1
                    head, _sep, rest = printed.partition(" · ")
                    head += _sep
                    tail = rest[len(rest.split(" ", 1)[0]):]  # ponytail: an input name holds no space
                    try:
                        page = (derive_source_top() / "help" / "policy.md").read_text(encoding="utf-8")
                    except OSError:
                        page = None
                    plines = (page or "").replace("\r", "").split("\n")
                    at = next((i for i, ln in enumerate(plines) if ln.startswith("## Install")), None)
                    section = []  # (1-based page line number, line)
                    for i, ln in enumerate(plines[at + 1:] if at is not None else [], (at or 0) + 2):
                        if ln.startswith("## "):
                            break
                        section.append((i, ln))
                    # TOOL-dGroundRules-50 S1: the parity's own find yields the line it found, so the section is read once.
                    found = next((i for i, ln in section if head in ln and tail in ln[ln.index(head) + len(head):]), None)
                    if page is None or at is None or found is None:
                        why = ("is unreadable, so nothing restates" if page is None else "has no `## Install` section" if at is None
                               else "has no line under `## Install` holding")
                        wrong.append(f"help/policy.md {why} the deferral line the install-day --scaffold "
                                     f"printed: {printed}")
                    else:
                        print(f"policy-fixture: {name} · help/policy.md:{found} carries the deferral line")
                grade_check("with the install staged")
                run_fixture_git(t, "add", "-A")
                run_fixture_git(t, "commit", "-q", "-m", "install the policy kit")
                # ponytail: the memory-tree kit, which `requires` brings in, seeds its conf and stops on its
                # first run, and an adopter re-runs it to finish; the bar's preflight grades that tree. A
                # second kit that seeds and stops would be a second line here, or a loop over the receipt.
                mt = next((r["path"] for r in rows if str(r.get("path")).endswith("/adopt-memory-tree.sh")), None)
                if mt:
                    rc, out = run_case_argv(t, ["bash", mt, "--scaffold"])
                    if rc:
                        wrong.append(f"the memory-tree adopter's re-run exited {rc}: {render_said(out, 'memory-tree')}")
                rc, out = run_adopter("--scaffold")  # S7: the mirror renders once its inputs are committed
                asserted += 1
                if rc or not Path(t, *MIRROR_FILE).is_file():
                    wrong.append(f"--scaffold after the first commit exited {rc} and wrote "
                                 f"{'a' if Path(t, *MIRROR_FILE).is_file() else 'no'} {policy.MIRROR_REL}: {out.strip()}")
                else:
                    asserted += 1
                    rc, out = run_case_argv(t, [sys.executable, (t / adopter).with_name("policy.py").as_posix(),
                                                "mirror", "--check"])
                    if rc:
                        wrong.append(f"the installed policy.py mirror --check after the re-run exited {rc}: {out.strip()}")
                run_fixture_git(t, "add", "-A")
                run_fixture_git(t, "commit", "-q", "--allow-empty", "-m", "the mirror")
                grade_check("once the install and its mirror are committed")
                asserted += 1
                if regen is None:
                    wrong.append("the receipt has no row of kit run-gates whose path ends in regen.py")
                else:
                    rc, out = run_case_argv(t, [sys.executable, (t / regen).as_posix(), "--check"])
                    if rc:
                        wrong.append(f"the installed {regen} --check exited {rc}, so the bar's preflight refuses: "
                                     f"{render_said(out, 'STALE')}")
                # S11: an adopter-authored list at the installed kit's directory is never graded.
                (t / adopter).with_name(policy.LEGACY_LIST).write_text("# an adopter's own list\nzz.home\tzz\n",
                                                                       encoding="utf-8", newline="\n")
                grade_check(f"with an adopter-written {policy.LEGACY_LIST} beside the installed kit")
    finally:
        for d in (t, s):
            if d is not None:
                remove_repo(d)
    for w in wrong:
        print(f"policy-fixture: {name} · WRONG: {w}")
    if not wrong:
        print(f"policy-fixture: {name} · every arm graded clean or announced, with the install staged, once it "
              f"and its mirror are committed, and beside an adopter's list · the installed regen.py --check "
              f"exits 0 · the README table names exactly the {len(names)} arm(s) of ARMS, each with its empty")
    return asserted, len(wrong)


PLAN_LINE = re.compile(r"^\s*(\S+)\s+\[([^\]]*)\]\s+(\S+)")  # a `plan` row: its mark, role and destination


def run_legacy_withheld_install(name):
    """`legacy-homes-withheld-install` (TOOL-dGroundRules-25 S9): the target `build_install_target`
    makes for this kit and its `requires` closure, the deployer's `plan` over it through `run_govkit`,
    then `apply`. The plan
    must hold the legacy-home list as one `ORDER [project-owned]` row and as no `write` or `SIDE`
    row, and the applied target must hold no file of that name; a refused `apply` is a WRONG carrying
    its output (TOOL-dGroundRules-32 S16)."""
    ids, missed = derive_requires_closure([tomllib.loads((KIT / "kit.toml").read_text(encoding="utf-8"))["id"]])
    checks = [("the selection", "every id resolves in the registry", False, m) for m in missed]
    t = s = None
    try:
        t, s = build_install_target(name, ids)
        args = ("--target", t.as_posix(), "--kits", ",".join(ids))
        rc, out = run_govkit(s, derive_source_top(), "plan", *args)
        rows = [m.groups() for m in map(PLAN_LINE.match, out.split("\n")) if m and m[3].endswith("/" + policy.LEGACY_LIST)]
        said = "; ".join(f"{k} [{r.strip()}] {d}" for k, r, d in rows) or "no row"
        checks.append(("plan", f"exit 0, one ORDER [project-owned] row for {policy.LEGACY_LIST} and no write or SIDE row",
                       rc == 0 and [(k, r.strip()) for k, r, _d in rows] == [("ORDER", "project-owned")], f"exit {rc} · {said}"))
        rc, out = run_govkit(s, derive_source_top(), "apply", *args)
        # The install is read from its receipt, never from apply's exit alone: an adopter step that
        # refuses after the files land still leaves them, and an empty target would hold no list.
        installed = Path(t, RECEIPT_REL).is_file() and any(r.get("kit") == ids[0] for r in read_receipt_rows(t))
        held = sorted(f.relative_to(t).as_posix() for f in t.rglob(policy.LEGACY_LIST))
        checks.append(("apply", f"the receipt holds kit {ids[0]}'s rows and the target no {policy.LEGACY_LIST}",
                       installed and not held, f"apply exit {rc} · receipt {'holds' if installed else 'LACKS'} "
                       f"{ids[0]} · {held or 'none held'}"))
        checks.append(("apply", "exit 0 with DEPLOY_FULL's answers", rc == 0, f"exit {rc} · {out.strip().replace(chr(10), ' · ') if rc else 'ok'}"))
    except (RuntimeError, OSError, subprocess.CalledProcessError) as exc:
        checks.append((name, "the target", False, f"{type(exc).__name__}: {exc}"))
    finally:
        for d in (t, s):
            if d is not None:
                remove_repo(d)
    return print_checks(name, checks)


def run_census_default_adopter(name):
    """`census-default-adopter` (TOOL-dGroundRules-25 S12): this kit, its `requires` closure and
    `kickoff-manifest` installed by `apply` into the target `build_install_target` makes, with the
    answers that entry asks for, `DEPLOY_FULL`'s (TOOL-dGroundRules-32 S16), and without
    `check-line-length`; a refused `apply` carries its output. `arm_cap_census` over it must
    announce `line-length · kit check-line-length not installed`, grade the `manifest-bytes` row at the
    receipt's destination of `manifest-check.sh`, so no announce names it, and find nothing."""
    ids, missed = derive_requires_closure([tomllib.loads((KIT / "kit.toml").read_text(encoding="utf-8"))["id"],
                                           "kickoff-manifest"])
    checks = [("the selection", "every id resolves in the registry", False, m) for m in missed]
    t = s = None
    try:
        t, s = build_install_target(name, ids)
        rc, out = run_govkit(s, derive_source_top(), "apply", "--target", t.as_posix(), "--kits", ",".join(ids))
        installed = Path(t, RECEIPT_REL).is_file()
        checks.append(("apply", f"--kits {','.join(ids)} wrote its receipt", installed, f"apply exit {rc} · receipt "
                       + ("written" if installed else "ABSENT")))
        checks.append(("apply", "exit 0 with DEPLOY_FULL's answers", rc == 0, f"exit {rc} · {out.strip().replace(chr(10), ' · ') if rc else 'ok'}"))
        if installed:
            dest = next((r["path"] for r in read_receipt_rows(t) if str(r.get("path")).endswith("/manifest-check.sh")), None)
            with contextlib.redirect_stdout(io.StringIO()) as said:
                _n, _pop, found = arm_cap_census(t, KIT)
            want = "cap census: line-length · kit check-line-length not installed"
            checks.append(("the census", f"{want!r}, manifest-bytes graded at {dest}, and no finding",
                           bool(dest) and want in said.getvalue().splitlines()
                           and "cap census: manifest-bytes ·" not in said.getvalue() and not found,
                           f"{render_said(said.getvalue(), 'line-length ·')} · {found or 'no finding'}"))
    except (RuntimeError, OSError, subprocess.CalledProcessError) as exc:
        checks.append((name, "the target", False, f"{type(exc).__name__}: {exc}"))
    finally:
        for d in (t, s):
            if d is not None:
                remove_repo(d)
    return print_checks(name, checks)


def run_govkit_source_root_refused(name):
    """`govkit-source-root-refused` (TOOL-dGroundRules-27 S5): `run_govkit` with the source's toplevel
    as both roots and `--help`, which exits 0 if it runs, must raise a RuntimeError naming that root and
    `build_source_snapshot`; a call that returns is a WRONG naming its exit and output."""
    top = derive_source_top()
    try:
        rc, out = run_govkit(top, top, "--help")
        checks = [(name, "the source's own root refused", False, f"the deployer ran: exit {rc} · {out.strip()}")]
    except RuntimeError as exc:
        checks = [(name, f"a RuntimeError naming {top.as_posix()} and build_source_snapshot",
                   top.as_posix() in str(exc) and "build_source_snapshot" in str(exc), str(exc))]
    return print_checks(name, checks)


def run_arms_empty_declared(name):
    """`arms-empty-declared` (TOOL-dGroundRules-25 S26): every ARMS row declares `empty`, `finding` or
    `announce`, and the reason for it; one that does not is a WRONG naming it."""
    return print_checks(name, [(a.name, "declares empty and why", a.empty in ("finding", "announce") and bool(a.why),
                                f"empty = {a.empty!r} · why = {a.why!r}") for a in ARMS])


def run_arms_empty_target(name):
    """`arms-empty-target` (TOOL-dGroundRules-25 S27): `check_policy.py --repo` over a target holding
    one committed README, no policy file and no tracked code: `arm_schema`, `arm_reader_coverage` and
    `arm_mirror_readers` must each print `not graded`. Then the scaffold written as its policy file:
    `arm_schema` must grade the scaffold's keys, a count derived from it, with no finding."""
    t = Path(tempfile.mkdtemp(prefix="pol-"))
    checks = []
    try:
        run_fixture_git(t, "init", "-q")
        (t / "README.md").write_text("An empty target.\n", encoding="utf-8", newline="\n")
        run_fixture_git(t, "add", "-A")
        run_fixture_git(t, "commit", "-q", "-m", "an empty target")
        _rc, out = run_case_argv(t, [sys.executable, str(KIT / "check_policy.py"), "--repo", t.as_posix()])
        for arm in ("arm_schema", "arm_reader_coverage", "arm_mirror_readers"):
            said = render_said(out, f"policy-check: {arm} · ")
            checks.append(("the empty target", arm, said.startswith(f"policy-check: {arm} · not graded · "), said))
        rows = policy.load_catalogue(KIT)
        keys = sum(1 for _ in policy.scan_keys(tomllib.loads(policy.render_scaffold(rows)), []))
        write_policy(t, policy.render_scaffold(rows))
        _rc, out = run_case_argv(t, [sys.executable, str(KIT / "check_policy.py"), "--repo", t.as_posix()])
        said = render_said(out, "policy-check: arm_schema · ")
        checks.append(("the scaffolded target", f"arm_schema grades the scaffold's {keys} key(s) with no finding",
                       said.startswith(f"policy-check: arm_schema · 0 finding(s) · {keys} key(s) of "), said))
    except subprocess.CalledProcessError as exc:
        checks.append((name, "the fixture's git", False, f"git exited {exc.returncode}: {(exc.stderr or '').strip()}"))
    finally:
        remove_repo(t)
    return print_checks(name, checks)


# ---- the reader (TOOL-dGroundRules-2) ----------------------------------------------------------

FIXTURE_SECOND = "mirror"
READER_POLICY = '[budgets]\nenforce = "{enforce}"\n\n[runtime]\nagents-in-flight = 3\n'


def write_policy(repo, text):
    Path(repo, POLICY_FILE[0]).mkdir(exist_ok=True)
    Path(repo, *POLICY_FILE).write_text(text, encoding="utf-8", newline="\n")


def build_reader_repo(path, *texts):
    """A git repository at `path` on `main`, one commit per text in order, each holding that text as
    the policy file, or no policy file where the text is None."""
    path.mkdir()
    run_fixture_git(path, "init", "-q")
    run_fixture_git(path, "symbolic-ref", "HEAD", "refs/heads/main")
    for text in texts:
        if text is None:
            Path(path, *POLICY_FILE).unlink(missing_ok=True)
        else:
            write_policy(path, text)
        run_fixture_git(path, "add", "-A")
        run_fixture_git(path, "commit", "-q", "--allow-empty", "-m", "policy")
    return path


def check_run(scenario, what, argv, want, cwd=None, env=None):
    """`argv` run in `cwd` -> (scenario, what, ok, what it observed), `want` judging (exit code,
    stdout, stderr), CR stripped. A program that does not start is exit None."""
    try:
        p = subprocess.run(argv, cwd=cwd, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace")
        rc, out, err = p.returncode, p.stdout.replace("\r", ""), p.stderr.replace("\r", "")
    except OSError as exc:
        rc, out, err = None, "", f"{argv[0]} did not run: {exc}"
    seen = f"exit {rc} · stdout {out.strip() or '(none)'!r} · stderr {err.strip() or '(none)'!r}"
    return scenario, what, want(rc, out, err), seen


def check_get(scenario, repo, args, want, env=None, kit=KIT, verb="get"):
    """`<kit>/policy.py <verb> <args>` run in `repo` -> (scenario, what, ok, what it observed), `want`
    judging (exit code, stdout, stderr), CR stripped."""
    return check_run(scenario, f"{verb} " + " ".join(args), [sys.executable, str(kit / "policy.py"), verb, *args],
                     want, repo, env)


def print_checks(name, checks):
    """One `policy-fixture:` line per check, the outcome it observed. -> (assertions, wrong)."""
    for scenario, what, ok, seen in checks:
        print(f"policy-fixture: {name} · {scenario} · {what} · " + (seen if ok else f"WRONG: {seen}"))
    return len(checks), sum(not c[2] for c in checks)


def run_reader_landed(name):
    """The reader at the landed revision. `remote`: a bare remote whose main sets warn and 3, a clone
    with an unpushed commit and a working-tree edit both setting refuse. `two-remote`: two remotes, no
    upstream, GOV_REMOTE unset then naming the second. `no-remote`: local main warn, the tree refuse."""
    t = Path(tempfile.mkdtemp(prefix="pol-"))
    try:
        build_reader_repo(t / "s", READER_POLICY.format(enforce="warn"))
        run_fixture_git(t, "clone", "-q", "--bare", "s", "r.git")
        run_fixture_git(t, "clone", "-q", "-o", FIXTURE_REMOTE, "r.git", "c")
        c = t / "c"
        write_policy(c, READER_POLICY.format(enforce="refuse"))
        run_fixture_git(c, "commit", "-q", "-am", "unpushed")
        write_policy(c, "# an uncommitted edit\n" + READER_POLICY.format(enforce="refuse"))
        tip = (policy.run_git(c, "rev-parse", f"refs/remotes/{FIXTURE_REMOTE}/main") or "").strip()[:8] or "(no tip)"
        checks = [
            check_get("remote", c, ["budgets.enforce"], lambda rc, o, e: rc == 0 and o == "warn\n"),
            check_get("remote", c, ["budgets.enforce", "--rev", "HEAD"], lambda rc, o, e: rc == 0 and o == "refuse\n"),
            check_get("remote", c, ["budgets.enforce", "--explain"],
                      lambda rc, o, e: rc == 0 and f" · file · set in {POLICY_REL} at {tip}," in e),
            check_get("remote", c, ["budgets.enforce", "--rev", "nosuchrev"],
                      lambda rc, o, e: rc == 2 and not o and e.startswith("policy: refused · ") and "nosuchrev" in e),
            check_get("remote", c, ["runtime.agents-in-flite"],
                      lambda rc, o, e: rc == 2 and not o and "catalogue.toml" in e and "not a catalogue key" in e),
            check_get("remote", c, ["budgets."], lambda rc, o, e: rc == 2 and not o and "not one TOML key" in e),
            check_get("remote", c, ["runtime.agents-in-flight"], lambda rc, o, e: rc == 0 and o == "3\n"),
        ]
        w = t / "w"
        w.mkdir()
        run_fixture_git(w, "init", "-q")
        run_fixture_git(w, "symbolic-ref", "HEAD", "refs/heads/main")
        for remote, enforce in ((FIXTURE_REMOTE, "warn"), (FIXTURE_SECOND, "refuse")):
            src = build_reader_repo(t / f"src-{enforce}", READER_POLICY.format(enforce=enforce))
            run_fixture_git(w, "remote", "add", remote, src.as_posix())
            run_fixture_git(w, "fetch", "-q", remote)
        checks += [
            check_get("two-remote", w, ["budgets.enforce"],
                      lambda rc, o, e: rc == 2 and not o and "Name it: export GOV_REMOTE=<remote>." in e),
            check_get("two-remote", w, ["budgets.enforce"], lambda rc, o, e: rc == 0 and o == "refuse\n",
                      env={**os.environ, "GOV_REMOTE": FIXTURE_SECOND}),
        ]
        n = build_reader_repo(t / "n", READER_POLICY.format(enforce="warn"))
        write_policy(n, READER_POLICY.format(enforce="refuse"))
        checks += [
            check_get("no-remote", n, ["budgets.enforce"], lambda rc, o, e: rc == 0 and o == "warn\n"),
            check_get("no-remote", n, ["budgets.enforce", "--explain"],
                      lambda rc, o, e: rc == 0 and "local main" in e and "no remote" in e),
        ]
    finally:
        remove_repo(t)
    return print_checks(name, checks)


def run_reader_parsed(name):
    """The reader parses and never sources: a policy file whose first line is a shell command refuses
    naming line 1, one whose comments carry command substitutions reads its value, and the marker
    either would create by running does not exist after both."""
    t = Path(tempfile.mkdtemp(prefix="pol-"))
    try:
        marker = (t / "marker").as_posix()
        cmd = build_reader_repo(t / "cmd", f"touch {marker}\n" + READER_POLICY.format(enforce="warn"))
        sub = build_reader_repo(t / "sub", f"# $(touch {marker})\nbudgets.enforce = \"warn\"  # `touch {marker}`\n")
        checks = [
            check_get("command-line", cmd, ["budgets.enforce"],
                      lambda rc, o, e: rc == 2 and not o and e.startswith(f"policy: refused · {POLICY_REL}:1 · ")),
            check_get("substitution-comments", sub, ["budgets.enforce"], lambda rc, o, e: rc == 0 and o == "warn\n"),
        ]
        ran = Path(marker).exists()
        checks.append(("marker", "no line of either file ran", not ran, f"the marker {'exists' if ran else 'does not exist'}"))
    finally:
        remove_repo(t)
    return print_checks(name, checks)


# ---- the resolution order (TOOL-dGroundRules-3) -------------------------------------------------

def run_resolution_order(name):
    """One repository per case, each read at `--rev HEAD`: a key the file sets and one it does not, an
    absent file, a file naming `strict` without and with an override, and a copy of this kit whose
    `budgets.enforce` row carries no default, read where the file does not set the key."""
    t = Path(tempfile.mkdtemp(prefix="pol-"))
    try:
        sets = build_reader_repo(t / "sets", '[budgets]\nenforce = "refuse"\n')
        absent = build_reader_repo(t / "absent", None)
        named = build_reader_repo(t / "named", 'preset = "strict"\n')
        over = build_reader_repo(t / "over", 'preset = "strict"\n\n[budgets]\nenforce = "refuse"\n')
        other = build_reader_repo(t / "other", "[runtime]\nagents-in-flight = 3\n")
        kit = t / "kit"
        kit.mkdir()
        for f in (*READER_FILES, policy.CATALOGUE):
            (kit / f).write_bytes((KIT / f).read_bytes().replace(b"\r\n", b"\n"))
        write_edit(kit / policy.CATALOGUE, lambda text: set_row_block(
            text, "budgets.enforce", lambda b: re.sub(r"^default = .*\n", "", b, flags=re.M)))
        get = ["--rev", "HEAD", "--explain"]
        checks = [
            check_get("file-sets", sets, ["budgets.enforce", *get],
                      lambda rc, o, e: rc == 0 and o == "refuse\n" and " · file · set in " in e),
            check_get("file-silent", sets, ["runtime.agents-in-flight", *get],
                      lambda rc, o, e: rc == 0 and o == "6\n" and " · default · not set in " in e),
            check_get("file-absent", absent, ["budgets.enforce", *get],
                      lambda rc, o, e: rc == 0 and o == "warn\n" and f" · default · {POLICY_REL} is absent at " in e),
            check_get("preset-named", named, ["budgets.enforce", *get],
                      lambda rc, o, e: rc == 0 and o == "warn\n" and " · default · " in e
                      and "preset strict, not applied until dKeptSession" in e),
            check_get("preset-overridden", over, ["budgets.enforce", *get],
                      lambda rc, o, e: rc == 0 and o == "refuse\n" and " · file · " in e),
            check_get("no-default", other, ["budgets.enforce", "--rev", "HEAD"],
                      lambda rc, o, e: rc == 2 and not o and "catalogue.toml" in e
                      and "the row budgets.enforce carries no default" in e, kit=kit),
        ]
    finally:
        remove_repo(t)
    return print_checks(name, checks)


# ---- the invalid-file branch (TOOL-dGroundRules-4) ----------------------------------------------

STRICT_FROM = None  # the directory `--fixture --strict-from` names; None prints `on-invalid-strict` NOT RUN
V2_SUFFIX = "-architecture-v2.md"  # v2 is the one file in that directory whose name ends so
PRESETS_HEADING = "\n## [presets]"
PRESETS_HEADER = "| Key | velocity |"
MALFORMED = "this line is not toml\n"


def run_on_invalid_classes(name):
    """One repository per failure class, each read at `--rev HEAD`, V a valid revision and C the one
    after it: absent; malformed after V and with nothing before it, where `arm_on_invalid` reds and
    then, the file made valid, does not; a missing key; an out-of-set value; a key no catalogue row
    matches; `refuse` then malformed; and an out-of-set `policy-file.on-invalid` with and without a
    value of it in V."""
    good = '[budgets]\nenforce = "refuse"\n'
    bad = '[budgets]\nenforce = refuse\n'  # line 2 is no TOML value
    t = Path(tempfile.mkdtemp(prefix="pol-"))
    try:
        absent = build_reader_repo(t / "absent", None)
        after = build_reader_repo(t / "after", good, bad)
        alone = build_reader_repo(t / "alone", bad)
        missing = build_reader_repo(t / "missing", '[budgets]\nenforce = "warn"\n')
        oos = build_reader_repo(t / "oos", good, '[budgets]\nenforce = "refuze"\n\n[runtime]\nagents-in-flight = 3\n')
        unknown = build_reader_repo(t / "unknown", good, '[budgets]\nenforce = "warn"\n\n[runtime]\nagents-in-flite = 3\n')
        refuse = build_reader_repo(t / "refuse", '[policy-file]\non-invalid = "refuse"\n', bad)
        never = build_reader_repo(t / "never", '[policy-file]\non-invalid = "refuse"\n', '[policy-file]\non-invalid = "never"\n')
        unset = build_reader_repo(t / "unset", good, '[budgets]\nenforce = "warn"\n\n[policy-file]\non-invalid = "never"\n')
        v = (policy.run_git(after, "rev-parse", "HEAD~1") or "").strip()[:8] or "(no V)"
        get, head = ["--rev", "HEAD", "--explain"], ["--rev", "HEAD"]
        refused = f"policy: refused · {POLICY_REL}:2 · "

        def build_fallback(value, line, *needles):
            return lambda rc, o, e: (rc == 0 and o == value and " · last-valid · " in e
                                     and f"is invalid, line {line}: " in e and all(n in e for n in needles))
        checks = [
            check_get("absent", absent, ["budgets.enforce", *get],
                      lambda rc, o, e: rc == 0 and o == "warn\n" and " · default · " in e),
            check_get("absent", absent, head, lambda rc, o, e: rc == 0 and "is absent at" in o, verb="check"),
            check_get("malformed-after-valid", after, ["budgets.enforce", *get],
                      build_fallback("refuse\n", 2, f"the last valid revision {v}")),
            check_get("malformed-after-valid", after, head,
                      lambda rc, o, e: rc == 0 and f"the last valid revision {v}" in o, verb="check"),
            check_get("malformed-alone", alone, ["budgets.enforce", *head],
                      lambda rc, o, e: rc == 2 and not o and e.startswith(refused) and "no valid revision" in e),
            check_get("malformed-alone", alone, head,
                      lambda rc, o, e: rc == 2 and not o and e.startswith(refused), verb="check"),
            check_get("missing-key", missing, ["runtime.agents-in-flight", *get],
                      lambda rc, o, e: rc == 0 and o == "6\n" and " · default · " in e),
            check_get("out-of-set", oos, ["budgets.enforce", *get], build_fallback("refuse\n", 2, "refuze")),
            check_get("out-of-set", oos, ["runtime.agents-in-flight", *get], build_fallback("6\n", 2, "the catalogue default")),
            check_get("unknown-key", unknown, ["budgets.enforce", *get],
                      build_fallback("refuse\n", 5, "runtime.agents-in-flite: no catalogue row matches")),
            check_get("refuse-then-malformed", refuse, ["budgets.enforce", *head],
                      lambda rc, o, e: rc == 2 and not o and e.startswith(refused) and "on-invalid is refuse" in e),
            check_get("refuse-then-malformed", refuse, head,
                      lambda rc, o, e: rc == 2 and e.startswith(refused) and "on-invalid is refuse" in e, verb="check"),
        ]
        for args, verb in ((["budgets.enforce", *head], "get"), (["policy-file.on-invalid", *head], "get"), (head, "check")):
            checks.append(check_get("on-invalid-out-of-set", never, args,
                                    lambda rc, o, e: rc == 2 and e.startswith(refused) and "on-invalid is refuse" in e, verb=verb))
        checks.append(check_get("on-invalid-out-of-set-unset", unset, ["budgets.enforce", *get], build_fallback("refuse\n", 5)))
        for fixed in (False, True):
            if fixed:
                write_policy(alone, good)
                run_fixture_git(alone, "commit", "-q", "-am", "the file made valid")
            _n, population, findings = arm_on_invalid(alone, KIT)
            ok = not findings if fixed else len(findings) == 1 and findings[0][0] == f"{POLICY_REL}:2"
            checks.append(("malformed-alone" + (", made valid" if fixed else ""), "arm_on_invalid", ok,
                           f"{len(findings)} finding(s) · " + ("; ".join(f"{k}: {w}" for k, w in findings) or population)))
    finally:
        remove_repo(t)
    return print_checks(name, checks)


def derive_strict_value(row, cell):
    """A `strict` cell of v2's presets table read as `row` expects: a `, `-separated list for a
    set-valued row, a number for a typed range, the member a closed list spells, else the cell's
    text, which `check_value` then judges."""
    allowed = row.get("allowed")
    t = allowed.get("type") if isinstance(allowed, dict) else None
    if t in policy.SET_TYPES:
        return cell.split(", ")
    if t in policy.COUNT_TYPES or t in policy.DURATION_TYPES:
        for kind in (int, float) if t in policy.DURATION_TYPES else (int,):
            try:
                return kind(cell)
            except ValueError:
                pass
        return cell
    members = allowed if isinstance(allowed, list) else allowed.get("of", []) + allowed.get("or", []) if isinstance(allowed, dict) else []
    return next((m for m in members if (m if isinstance(m, str) else policy.render_toml_value(m)) == cell), cell)


def check_same_value(a, b):
    """True when two policy values are one: a set-valued pair compared as a set, else type and value."""
    if isinstance(a, list) and isinstance(b, list):
        return {policy.render_json(m) for m in a} == {policy.render_json(m) for m in b}
    return policy.check_member(a, [b])


def derive_strict_population(text, rows):
    """-> (kept {key: strict's value}, excluded [(key, why)], cells) from v2's `[presets]` table, the
    one whose header row opens `| Key | velocity |`. A key is kept when its strict cell, read as its
    catalogue row expects, is a value `check_value` admits and differs from the row's default; every
    other row is excluded with why, and of two keys where one is a dotted prefix of the other, which
    no TOML file can hold together, the longer is kept."""
    parts = text.replace("\r", "").split(PRESETS_HEADING, 1)
    lines = parts[1].split("\n## ", 1)[0].split("\n") if len(parts) == 2 else []
    at = next((i for i, ln in enumerate(lines) if ln.startswith(PRESETS_HEADER)), None)
    if at is None:
        return {}, [], 0
    col = [c.strip() for c in lines[at].strip().strip("|").split("|")].index("strict")
    kept, excluded, cells = {}, [], 0
    for ln in lines[at + 2:]:
        if not ln.startswith("|"):
            break
        row_cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        key, cell = row_cells[0].strip("`"), row_cells[col]
        cells += 1
        if "<" in key or "*" in key:
            excluded.append((key, "a placeholder key, which names no one key to plant"))
            continue
        try:
            row = policy.read_catalogue_row(policy.parse_key(key), rows)
        except policy.Refusal as exc:
            excluded.append((key, f"no catalogue row: {exc.why}"))
            continue
        value = derive_strict_value(row, cell)
        why = policy.check_value(row, value)
        if why:
            excluded.append((key, f"the cell {cell!r} is no value its row admits: {why}"))
        elif check_same_value(value, row.get("default")):
            excluded.append((key, "strict's value is the default, which cannot tell a fallback from a read"))
        else:
            kept[key] = value
    for key in sorted(kept):
        longer = next((k for k in kept if k.startswith(key + ".")), None)
        if longer:
            excluded.append((key, f"a dotted prefix of {longer}, which no TOML file can hold beside it"))
            del kept[key]
    return kept, excluded, cells


def run_on_invalid_strict(name):
    """Strict's value of every derived key, read at a malformed revision after a valid one setting
    each: every read must be strict's value with source `last-valid`, never a default. Without
    `--strict-from` it prints NOT RUN, which is never a pass. v2 is the one file directly in that
    directory whose name ends `-architecture-v2.md`; none, or more than one, is red naming the count."""
    if STRICT_FROM is None:
        print(f"policy-fixture: {name} · NOT RUN · no --strict-from <dir> names the directory holding v2's "
              "architecture record, so strict's values have no source; this is not a pass")
        return 0, 0
    found = sorted(p for p in Path(STRICT_FROM).glob("*" + V2_SUFFIX) if p.is_file())
    if len(found) != 1:
        print(f"policy-fixture: {name} · WRONG: --strict-from {STRICT_FROM} holds {len(found)} file(s) whose "
              f"name ends {V2_SUFFIX}, not one: {', '.join(p.name for p in found) or '(none)'}")
        return 1, 1
    v2 = found[0].as_posix()
    try:
        text = found[0].read_text(encoding="utf-8")
    except OSError as exc:
        print(f"policy-fixture: {name} · WRONG: {v2} does not read: {exc}")
        return 1, 1
    rows = policy.load_catalogue(KIT)
    kept, excluded, cells = derive_strict_population(text, rows)
    print(f"policy-fixture: {name} · {cells} strict cell(s) in {v2} · population {len(kept)} key(s), "
          f"{len(excluded)} excluded")
    for key, why in excluded:
        print(f"policy-fixture: {name} · excluded {key}: {why}")
    if not kept:
        print(f"policy-fixture: {name} · WRONG: the population is empty, so nothing was planted")
        return 1, 1
    plant = "".join(f"{key} = {policy.render_toml_value(v)}\n" for key, v in kept.items())
    wrong = [f"the valid revision is invalid, line {p.line}: {p.key}: {p.why}" for p in policy.validate(plant, rows)]
    t = Path(tempfile.mkdtemp(prefix="pol-"))
    try:
        repo = build_reader_repo(t / "strict", plant, plant + MALFORMED)
        for key, value in kept.items():
            try:
                hit = policy.resolve(key, repo, "HEAD")
            except policy.Refusal as exc:
                wrong.append(f"{key} refused: {exc}")
                continue
            if hit.source != "last-valid" or not check_same_value(hit.value, value):
                wrong.append(f"{key} read {policy.render_json(hit.value)} from {hit.source}, "
                             f"not strict's {policy.render_json(value)} from last-valid")
    finally:
        remove_repo(t)
    for w in wrong:
        print(f"policy-fixture: {name} · WRONG: {w}")
    if not wrong:
        print(f"policy-fixture: {name} · each of the {len(kept)} key(s) read strict's value from last-valid "
              f"at the malformed revision")
    return len(kept) + 2, len(wrong)


DERIVED_ROW = '\n[[key]]\nname = "zz.derived"\nallowed = ["a"]\ndefault = { derived = "x" }\nowner = "dGroundRules"\n'


def run_reader_refusals(name):
    """The reader's three refusals of TOOL-dGroundRules-21, one repository each. `on-invalid-utf16`
    (S10): V valid, then C the same file written as UTF-16LE with its BOM, as a PowerShell redirect
    writes it; `get` at C must read V's value from `last-valid`, its reason holding `not UTF-8`.
    `on-invalid-shallow` (S13): V valid, then C malformed, cloned `--depth 1`; `get` at C must refuse
    naming the shallow history, and a full clone fall back to V. `resolution-derived-default` (S12): a
    kit copy at its own path in the repository whose catalogue carries DERIVED_ROW; `get` on it must
    exit 2 naming the row and `a derived default`, and the mirror rendered there hold no such key."""
    good, bad = '[budgets]\nenforce = "refuse"\n', '[budgets]\nenforce = refuse\n'
    t = Path(tempfile.mkdtemp(prefix="pol-"))
    checks = []
    try:
        if name == "on-invalid-utf16":
            r = build_reader_repo(t / "u", good)
            Path(r, *POLICY_FILE).write_bytes(b"\xff\xfe" + good.encode("utf-16-le"))
            run_fixture_git(r, "add", "-A")
            run_fixture_git(r, "commit", "-q", "-m", "C, written by a PowerShell redirect")
            checks.append(check_get("C in UTF-16LE", r, ["budgets.enforce", "--rev", "HEAD", "--explain"], lambda rc, o, e:
                                    rc == 0 and o == "refuse\n" and " · last-valid · " in e and "not UTF-8" in e))
        elif name == "on-invalid-bom":
            # TOOL-dGroundRules-25 S30: one valid revision written with a UTF-8 BOM, as an editor or a
            # PowerShell write leaves it. With no earlier revision, a BOM read as invalid would fall
            # to the catalogue default; the file's own value with source `file` is the pass.
            r = build_reader_repo(t / "b", None)
            Path(r, POLICY_FILE[0]).mkdir()
            Path(r, *POLICY_FILE).write_bytes(b"\xef\xbb\xbf" + good.encode("utf-8"))
            run_fixture_git(r, "add", "-A")
            run_fixture_git(r, "commit", "-q", "-m", "a valid file with a BOM")
            checks.append(check_get("a BOM", r, ["budgets.enforce", "--rev", "HEAD", "--explain"], lambda rc, o, e:
                                    rc == 0 and o == "refuse\n" and "policy: budgets.enforce · file · " in e))
            # TOOL-dGroundRules-32 S12: the schema arm and the guard read the BOM-led file as the reader does.
            _n, why, found = arm_schema(r, KIT)
            checks.append(("arm_schema", "no parse failure over the BOM-led file", "did not parse" not in why,
                           f"{why} · {found or 'no finding'}"))
            g, gk = build_guard_repo()
            try:
                Path(g, *POLICY_FILE).write_bytes(b"\xef\xbb\xbf" + GUARD_POLICY.encode("utf-8"))
                run_fixture_git(g, "commit", "-q", "-am", "the policy file written with a BOM")
                for rel, edit in GUARD_PLANTS["guard-admits-raise"][0][1]:
                    Path(g, rel).write_text(edit(Path(g, rel).read_text(encoding="utf-8")), encoding="utf-8", newline="\n")
                    run_fixture_git(g, "add", "--", rel)
                checks.append(check_run("the raise over a BOM", "guard.py --staged", [sys.executable, str(gk / "guard.py"),
                                        "--staged"], lambda rc, o, e: rc == 0 and "policy-guard: admitted · " in o, cwd=g))
            finally:
                remove_repo(g)
        elif name == "on-invalid-shallow":
            src = build_reader_repo(t / "src", good, bad)
            for kind, depth in (("shallow", ["--depth", "1"]), ("full", [])):
                run_fixture_git(t, "clone", "-q", *depth, src.as_uri(), kind)
            # TOOL-dGroundRules-25 S31: the clone is shallow before its read is graded, so the branch is exercised.
            shallow = run_fixture_git(t / "shallow", "rev-parse", "--is-shallow-repository")
            checks.append(("--depth 1", "git rev-parse --is-shallow-repository", shallow == "true",
                           f"is-shallow-repository {shallow}"))
            checks += [check_get("--depth 1", t / "shallow", ["budgets.enforce", "--rev", "HEAD"], lambda rc, o, e:
                                 rc == 2 and not o and "history is shallow at " in e and "fetch more history" in e),
                       check_get("full history", t / "full", ["budgets.enforce", "--rev", "HEAD", "--explain"],
                                 lambda rc, o, e: rc == 0 and o == "refuse\n" and " · last-valid · " in e)]
        else:  # resolution-derived-default
            r = t / "d"
            prefix = (policy.run_git(KIT, "rev-parse", "--show-prefix") or "").strip()
            kit = r / prefix
            kit.mkdir(parents=True)
            for f in (*READER_FILES, policy.CATALOGUE):
                (kit / f).write_bytes((KIT / f).read_bytes().replace(b"\r\n", b"\n"))
            write_edit(kit / policy.CATALOGUE, lambda text: text + DERIVED_ROW)
            write_policy(r, good)
            run_fixture_git(r, "init", "-q")
            run_fixture_git(r, "symbolic-ref", "HEAD", "refs/heads/main")
            run_fixture_git(r, "add", "-A")
            run_fixture_git(r, "commit", "-q", "-m", "a catalogue row with a derived default")
            checks.append(check_get("the derived row", r, ["zz.derived", "--rev", "HEAD"], lambda rc, o, e:
                                    rc == 2 and not o and "zz.derived" in e and "a derived default" in e, kit=kit))
            p = subprocess.run([sys.executable, str(kit / "policy.py"), "mirror", "--print"], cwd=r,
                               capture_output=True)
            try:
                held = json.loads(p.stdout.decode("utf-8")).get("keys", {})
            except ValueError:
                held = None
            checks.append(("the mirror", "rendered with no zz.derived key, and budgets.enforce held",
                           p.returncode == 0 and held is not None and "zz.derived" not in held and "budgets.enforce" in held,
                           f"exit {p.returncode} · {len(held or {})} key(s) · {p.stderr.decode('utf-8', 'replace').strip() or 'no stderr'}"))
    except subprocess.CalledProcessError as exc:
        checks.append((name, "the fixture's git", False, f"git exited {exc.returncode}: {(exc.stderr or '').strip()}"))
    finally:
        remove_repo(t)
    return print_checks(name, checks)


READER_REFUSAL_CASES = ("on-invalid-utf16", "on-invalid-bom", "on-invalid-shallow", "resolution-derived-default")


# ---- the JSON mirror (TOOL-dGroundRules-5) ------------------------------------------------------

AGENTS_KEY = "runtime.agents-in-flight"
CONSUMER_FILE = ("hooks", "consumer.js")
# Its comment names the mirror, which `arm_mirror_readers` must not read as a read (TOOL-dGroundRules-21 AC18).
CONSUMER_TEXT = ("// A consumer outside the policy kit: it reads policy through the helper, never policy.json itself.\n"
                 "const { readPolicy } = require(@helper@);\n"
                 f"module.exports = () => readPolicy({json.dumps(AGENTS_KEY)}).value;\n")
DIRECT_READER = 'module.exports = () => JSON.parse(require("fs").readFileSync(".governance/policy.json", "utf8"));\n'
LANDED_POLICY = '[policy-file]\non-invalid = "{on}"\n\n[runtime]\nagents-in-flight = {n}\n'


def seed_mirror_hand_edited(repo, kit, rows):
    """The working-tree mirror's agents-in-flight value set to 8, its blob ids kept."""
    path = Path(repo, *MIRROR_FILE)
    doc = json.loads(path.read_bytes())
    doc["keys"][AGENTS_KEY]["value"] = 8
    path.write_bytes((json.dumps(doc, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii"))
    return AGENTS_KEY, "differs from the render"


def seed_mirror_absent(repo, kit, rows):
    Path(repo, *MIRROR_FILE).unlink()
    return policy.MIRROR_REL, "absent"


def seed_mirror_direct_reader(repo, kit, rows):
    """The tracked consumer outside the kit made to read the mirror with readFileSync."""
    Path(repo, *CONSUMER_FILE).write_text(DIRECT_READER, encoding="utf-8", newline="\n")
    return "/".join(CONSUMER_FILE), "reads policy.json"


def build_landed_repo(rows):
    """build_repo's fixture with this kit's policy.py, policy-mirror.js and policy-shim.sh copied beside
    its catalogue and committed with no mirror, its remote moved to a bare repository. -> (repo, kit, bare)."""
    repo, kit = build_repo(rows)
    for f in MIRROR_KIT_FILES:
        (kit / f).write_bytes((KIT / f).read_bytes().replace(b"\r\n", b"\n"))
    Path(repo, *MIRROR_FILE).unlink()
    bare = Path(tempfile.mkdtemp(prefix="pol-"))
    run_fixture_git(bare, "init", "-q", "--bare")
    run_fixture_git(repo, "remote", "set-url", FIXTURE_REMOTE, bare.as_posix())
    run_fixture_git(repo, "add", "-A")
    run_fixture_git(repo, "commit", "-q", "-m", "the mirror helper")
    return repo, kit, bare


def set_landed(repo, on, n, render):
    """One commit on main whose policy file sets `policy-file.on-invalid` and agents-in-flight, carrying,
    when `render`, the mirror rendered at the commit before it; pushed, so the remote's main is L. -> L8."""
    if render:
        Path(repo, *MIRROR_FILE).write_bytes(policy.render_mirror(repo, "HEAD"))
    write_policy(repo, LANDED_POLICY.format(on=on, n=n))
    run_fixture_git(repo, "add", "-A")
    run_fixture_git(repo, "commit", "-q", "--allow-empty", "-m", "landed")
    run_fixture_git(repo, "push", "-q", FIXTURE_REMOTE, "main")
    return (policy.run_git(repo, "rev-parse", "HEAD") or "").strip()[:8]


def run_mirror_landed(name):
    """The helper over a landed revision L in a bare remote. `mirror-worktree-loosened`: L sets the
    limit to 2 with its fresh mirror, the working-tree mirror says 8, and a fixture hook asked for 3
    must refuse. `mirror-stale-last-valid`: L sets 3 and carries the mirror rendered at 2, read as 3
    with a reason opening `mirror stale at`. `mirror-stale-refuse`: the same under `refuse`, a refusal
    naming the mirror, which `arm_mirror_landed` reds. `mirror-absent-refuse`: L carries no mirror,
    refused under `refuse`, then read as the reader reads it under `last-valid`.
    `mirror-commit-rewrite` (TOOL-dGroundRules-65): `mirror --write` at A, committed as B, and B
    rewritten by `git commit-tree` over its tree and parents into B', as `--prepare` folds a merge:
    `mirror --check` fresh at B and at B', and the helper reading B' as L fills `{rev}` with L8.
    `mirror-landed-merge` (TOOL-dGroundRules-14): main with its fresh mirror pushed as L, a branch b
    setting budgets.enforce, b merged --no-ff onto main detached, `mirror --write` over the merge, and
    `commit-tree` over the written tree with parents main and b, pushed as main: at that rewrite
    `mirror --check` is fresh, `arm_mirror_parity` finds nothing, and the helper reads the key from
    the mirror with no `mirror stale at`. A failed git step is a WRONG naming the step."""
    rows = policy.load_catalogue(KIT)
    repo, kit, bare = build_landed_repo(rows)
    try:
        helper = ["node", str(kit / "policy-mirror.js"), "get", AGENTS_KEY, "--repo", str(repo)]
        what, at_l = "policy-mirror.js get " + AGENTS_KEY, "at L"
        refused = f"policy: refused · {policy.MIRROR_REL}:0 · "
        checks = []
        if name == "mirror-worktree-loosened":
            set_landed(repo, "last-valid", 2, False)
            set_landed(repo, "last-valid", 2, True)
            mirror = Path(repo, *MIRROR_FILE)
            doc = json.loads(mirror.read_bytes())
            doc["keys"][AGENTS_KEY]["value"] = 8
            mirror.write_bytes((json.dumps(doc, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii"))
            # The hooks kit's agent-cap.js beside the kit copy, its settings at 3 (TOOL-dGroundRules-10):
            # rule 7 must read L's limit of 2, never the working-tree mirror's 8.
            hooks = resolve_kit_dir("hooks", "agent-cap.js", KIT)
            hook = repo / (policy.run_git(hooks, "rev-parse", "--show-prefix") or "").strip() / "agent-cap.js"
            hook.parent.mkdir(parents=True, exist_ok=True)
            for f in HOOK_FILES:
                (hook.parent / f).write_bytes((hooks / f).read_bytes().replace(b"\r\n", b"\n"))
            write_settings(repo, render_limit_env(3))
            checks += [check_hook_call(at_l, "agent-cap.js rule 7 with settings at 3", hook, render_spawn(repo, "u3"),
                                       lambda rc, err: rc == 2 and "above runtime.agents-in-flight 2" in err),
                       check_run(at_l, what, helper, lambda rc, o, e: rc == 0 and o == "2\n")]
        elif name == "mirror-stale-last-valid":
            set_landed(repo, "last-valid", 2, False)
            at = set_landed(repo, "last-valid", 3, True)
            checks.append(check_run(at_l, what + " --explain", helper + ["--explain"], lambda rc, o, e: rc == 0
                                    and o == "3\n" and f"policy: {AGENTS_KEY} · file · mirror stale at {at}; " in e))
        elif name == "mirror-stale-refuse":
            set_landed(repo, "last-valid", 2, False)
            at = set_landed(repo, "refuse", 3, True)
            checks.append(check_run(at_l, what, helper, lambda rc, o, e: rc == 2 and not o
                                    and e.startswith(f"{refused}stale at {at}; policy-file.on-invalid is refuse")))
        elif name == "mirror-commit-rewrite":
            # Once per reason kind (TOOL-dGroundRules-25 S1), each builder's reason rendered at A: a
            # file setting the key, a file present without it, the file absent, and an invalid file
            # over a valid ancestor, the `last-valid` kind, so a builder naming the rendered commit
            # reds the kind that exercises it.
            cli = [sys.executable, str(kit / "policy.py"), "mirror"]
            kinds = (("file", LANDED_POLICY.format(on="last-valid", n=3)),
                     ("default, the file present without the key", '[budgets]\nenforce = "warn"\n'),
                     ("default, the file absent", None),
                     ("last-valid", LANDED_POLICY.format(on="last-valid", n=3)), ("last-valid", MALFORMED))
            for kind, text in kinds:
                if text is None:
                    Path(repo, *POLICY_FILE).unlink()
                else:
                    write_policy(repo, text)
                run_fixture_git(repo, "add", "-A")
                run_fixture_git(repo, "commit", "-q", "--allow-empty", "-m", f"A, the policy file of kind {kind}")
                if text == LANDED_POLICY.format(on="last-valid", n=3) and kind == "last-valid":
                    continue  # the valid ancestor the invalid file falls back to
                checks.append(check_run(f"{kind} · A", "policy.py mirror --write", cli + ["--write"],
                                        lambda rc, o, e: rc == 0 and o.startswith("policy: mirror written"), cwd=repo))
                run_fixture_git(repo, "add", "--", policy.MIRROR_REL)
                run_fixture_git(repo, "commit", "-q", "-m", "the mirror, rendered at its parent")
                b = run_fixture_git(repo, "rev-parse", "HEAD")
                parents = run_fixture_git(repo, "rev-parse", "HEAD^@").split()
                rewrite = run_fixture_git(repo, "commit-tree", f"{b}^{{tree}}", *(a for p in parents for a in ("-p", p)),
                                          "-m", "the mirror, rewritten by commit-tree")
                checks.append((f"{kind} · B'", "a new commit over B's tree and parents", rewrite != b,
                               f"B {b[:8]} · B' {rewrite[:8]}"))
                for at, sha in (("B, the commit carrying the mirror", b), ("B', its commit-tree rewrite", rewrite)):
                    run_fixture_git(repo, "reset", "-q", "--hard", sha)
                    checks.append(check_run(f"{kind} · {at}", "policy.py mirror --check", cli + ["--check"],
                                            lambda rc, o, e: rc == 0 and o == "policy: mirror fresh\n", cwd=repo))
            run_fixture_git(repo, "push", "-q", FIXTURE_REMOTE, "main")
            checks.append(check_run("B' landed as L", what + " --explain", helper + ["--explain"], lambda rc, o, e:
                                    rc == 0 and f"at {rewrite[:8]}, the landed revision" in e and "{rev}" not in e))
        elif name == "mirror-landed-merge":
            # The landing's order (TOOL-dGroundRules-14), as push-main.sh --prepare runs it: b merged
            # --no-ff onto main detached, the mirror written again over the merge, the merge rewritten by
            # commit-tree over its own parents, and the rewrite pushed as main.
            cli = [sys.executable, str(kit / "policy.py"), "mirror"]
            msg, rewrite, step = "merge: land b onto main", None, "main committed with its mirror, pushed as L"
            try:
                Path(repo, *MIRROR_FILE).write_bytes(policy.render_mirror(repo, "HEAD"))
                run_fixture_git(repo, "add", "--", policy.MIRROR_REL)
                run_fixture_git(repo, "commit", "-q", "-m", "main, its mirror fresh")
                run_fixture_git(repo, "push", "-q", FIXTURE_REMOTE, "main")
                step = "1, budgets.enforce committed on branch b"
                run_fixture_git(repo, "checkout", "-q", "-b", "b")
                write_edit(Path(repo, *POLICY_FILE), lambda t: t.replace('enforce = "warn"\n', 'enforce = "refuse"\n'))
                run_fixture_git(repo, "commit", "-q", "-am", "the branch being landed")
                step = "2, b merged --no-ff onto main, detached"
                run_fixture_git(repo, "checkout", "-q", "--detach", "main")
                run_fixture_git(repo, "merge", "-q", "--no-ff", "b", "-m", msg)
                checks.append(check_run("the merge", "policy.py mirror --write", cli + ["--write"],
                                        lambda rc, o, e: rc == 0 and o.startswith("policy: mirror written"), cwd=repo))
                step = "4, the merge rewritten by commit-tree over its parents"
                run_fixture_git(repo, "add", "-A")
                rewrite = run_fixture_git(repo, "commit-tree", run_fixture_git(repo, "write-tree"),
                                          "-p", "main", "-p", "b", "-m", msg)
                run_fixture_git(repo, "update-ref", "--no-deref", "HEAD", rewrite)
                step = "5, the rewrite pushed as main"
                run_fixture_git(repo, "push", "-q", FIXTURE_REMOTE, "HEAD:refs/heads/main")
            except subprocess.CalledProcessError as exc:
                checks.append((f"step {step}", "the replay", False,
                               f"git exited {exc.returncode}: {(exc.stderr or '').strip() or '(no stderr)'}"))
                rewrite = None
            if rewrite:
                at = "the rewrite"
                checks.append(check_run(at, "policy.py mirror --check", cli + ["--check"],
                                        lambda rc, o, e: rc == 0 and o == "policy: mirror fresh\n", cwd=repo))
                _n, population, findings = arm_mirror_parity(repo, kit)
                checks.append((at, "arm_mirror_parity", not findings, f"{len(findings)} finding(s) · "
                               + ("; ".join(f"{k}: {w}" for k, w in findings) or population)))
                checks.append(check_run(at + " landed as L", "policy-mirror.js get budgets.enforce --explain",
                                        ["node", str(kit / "policy-mirror.js"), "get", "budgets.enforce", "--repo",
                                         str(repo), "--explain"], lambda rc, o, e: rc == 0 and o == "refuse\n"
                                        and " · file · mirror " not in e and f"at {rewrite[:8]}, the landed revision" in e))
        elif name == "mirror-stale-legacy":
            # TOOL-dGroundRules-21 S17: the mirror fresh on its policy and catalogue blobs, then a landing
            # that changes `.agent-cap.conf` alone; the mirror's legacy blob no longer matches L.
            set_landed(repo, "last-valid", 3, False)
            Path(repo, *MIRROR_FILE).write_bytes(policy.render_mirror(repo, "HEAD"))
            run_fixture_git(repo, "add", "--", policy.MIRROR_REL)
            run_fixture_git(repo, "commit", "-q", "-m", "the mirror, fresh")
            Path(repo, policy.LEGACY_FANOUT).write_text("FANOUT_CAP=2\n", encoding="utf-8", newline="\n")
            run_fixture_git(repo, "add", "--", policy.LEGACY_FANOUT)
            run_fixture_git(repo, "commit", "-q", "-m", "a conf-only landing")
            run_fixture_git(repo, "push", "-q", FIXTURE_REMOTE, "main")
            at = run_fixture_git(repo, "rev-parse", "HEAD")[:8]
            checks.append(check_run(at_l, what + " --explain", helper + ["--explain"], lambda rc, o, e: rc == 0
                                    and o == "2\n" and f" · mirror stale at {at}; " in e))
        elif name == "mirror-shim-exit-one":
            # TOOL-dGroundRules-21 S16: every shim outcome but exit 0 and its own refusal is a PolicyRefusal
            # naming the status, never an undefined value or another throw.
            set_landed(repo, "last-valid", 3, False)
            shim = kit / "policy-shim.sh"
            enforce = ["node", str(kit / "policy-mirror.js"), "get", "budgets.enforce", "--repo", str(repo)]
            for label, body in (("a shim exiting 1", "exit 1\n"), ("a shim killed by a signal", "kill -9 $$\n")):
                shim.write_text("#!/usr/bin/env bash\necho planted >&2\n" + body, encoding="utf-8", newline="\n")
                checks.append(check_run(label, "policy-mirror.js get budgets.enforce", enforce, lambda rc, o, e: rc == 2
                                        and not o and e.startswith(refused) and "policy-shim.sh landed failed: status " in e))
        else:  # mirror-absent-refuse
            at = set_landed(repo, "refuse", 3, False)
            checks.append(check_run(at_l, what + " under refuse", helper, lambda rc, o, e: rc == 2 and not o
                                    and e.startswith(f"{refused}absent at {at}; policy-file.on-invalid is refuse")))
            at = set_landed(repo, "last-valid", 3, False)
            want = render_get(policy.resolve(AGENTS_KEY, repo).value)
            checks.append(check_run(at_l, what + " --explain under last-valid", helper + ["--explain"], lambda rc, o, e:
                                    rc == 0 and o == want and f" · file · mirror absent at {at}; " in e))
        _n, population, findings = arm_mirror_landed(repo, kit)
        named = any(k == AGENTS_KEY for k, _w in findings)
        ok = named if name in ("mirror-stale-refuse", "mirror-shim-exit-one") else not findings
        checks.append((at_l, "arm_mirror_landed", ok, f"{len(findings)} finding(s) · "
                       + ("; ".join(f"{k}: {w}" for k, w in findings) or population)))
    finally:
        remove_repo(repo)
        remove_repo(bare)
    asserted, wrong = print_checks(name, checks)
    if name == "mirror-landed-merge" and not wrong:
        print(f"policy-fixture: {name} · fresh at the rewrite")
    return asserted, wrong


def run_mirror_absent_adopter(name):
    """`mirror-absent-adopter` (TOOL-dGroundRules-21 S15): an adopter with no mirror, over a target
    whose HEAD carries neither the policy file nor a mirror, the policy file scaffolded in its working
    tree, and over a target with no commit at all. `arm_mirror_parity` and `arm_on_invalid` must each
    print `not graded` and no finding over both."""
    t = Path(tempfile.mkdtemp(prefix="pol-"))
    checks = []
    try:
        carried = t / "carried"
        build_reader_repo(carried, None)
        write_policy(carried, policy.render_scaffold(policy.load_catalogue(KIT)))
        (t / "bare").mkdir()
        run_fixture_git(t / "bare", "init", "-q")
        for target, repo in (("HEAD carries neither", carried), ("no commit", t / "bare")):
            for arm in ("arm_mirror_parity", "arm_on_invalid"):
                verdict, findings = run_arm(ARM[arm], repo, KIT)
                checks.append((target, arm, verdict.startswith("not graded · ") and not findings,
                               f"{verdict} · {findings or 'no finding'}"))
    except subprocess.CalledProcessError as exc:
        checks.append((name, "the fixture's git", False, f"git exited {exc.returncode}: {(exc.stderr or '').strip()}"))
    finally:
        remove_repo(t)
    return print_checks(name, checks)


def run_mirror_landed_parity(name):
    """The shim's `landed` against the reader's `derive_landed_revision` in six ladder states, each
    remote's main a different commit: two remotes with GOV_REMOTE naming the second; two without;
    one remote; no remote; no remote, on master; one remote with no remote HEAD, on master. The same
    sha in each, or both refusing with the same whole line (TOOL-dGroundRules-73, TOOL-dGroundRules-80).
    The shim runs under the bash `resolve_bash` finds able to see it, whatever PATH puts first, and
    the case names it."""
    repo, kit, bare = build_landed_repo(policy.load_catalogue(KIT))
    checks = []
    try:
        bash = resolve_bash((kit / "policy-shim.sh").as_posix())
        if bash is None:
            print(f"policy-fixture: {name} · WRONG: no bash can see the shim: GOV_BASH, PATH's bash and Git for "
                  "Windows' two were each tried; set GOV_BASH")
            return 1, 1
        print(f"policy-fixture: {name} · the shim runs under {bash}")
        run_fixture_git(repo, "push", "-q", FIXTURE_REMOTE, "main")
        run_fixture_git(repo, "remote", "add", FIXTURE_SECOND, repo.as_posix())
        run_fixture_git(repo, "update-ref", f"refs/remotes/{FIXTURE_SECOND}/main", "HEAD~1")
        for state, drop, gov in (("two remotes, GOV_REMOTE", None, FIXTURE_SECOND), ("two remotes", None, None),
                                 ("one remote", FIXTURE_SECOND, None), ("no remote", FIXTURE_REMOTE, None),
                                 ("no remote, on master", None, None),
                                 ("one remote, no remote HEAD, on master", None, None)):
            if drop:
                run_fixture_git(repo, "remote", "remove", drop)
            if state == "no remote, on master":
                run_fixture_git(repo, "branch", "-m", "main", "master")
            if state == "one remote, no remote HEAD, on master":
                run_fixture_git(repo, "remote", "add", FIXTURE_REMOTE, bare.as_posix())
                run_fixture_git(repo, "update-ref", f"refs/remotes/{FIXTURE_REMOTE}/master", "HEAD")
            if gov:
                os.environ["GOV_REMOTE"] = gov
            try:
                want, why, line = policy.derive_landed_revision(repo)[0], "", ""
            except policy.Refusal as exc:
                want, why, line = None, exc.why, str(exc)
            finally:
                os.environ.pop("GOV_REMOTE", None)
            checks.append(check_run(
                state, f"policy-shim.sh landed against derive_landed_revision ({want[:8] if want else 'refused: ' + why})",
                [bash, (kit / "policy-shim.sh").as_posix(), "landed"],
                lambda rc, o, e, want=want, line=line: rc == 0 and o.strip() == want if want else rc == 2 and not o and e.strip() == line,
                cwd=repo, env={**os.environ, **({"GOV_REMOTE": gov} if gov else {})}))
    finally:
        remove_repo(repo)
        remove_repo(bare)
    return print_checks(name, checks)


# ---- the minimal guard (TOOL-dGroundRules-6) ----------------------------------------------------

GUARD_FILES = ("guard.py", "guarded-paths.txt", *READER_FILES)  # the reader: the mirror shape's `mirror --print`
GUARD_MIRROR = ("guard-mirror-render", "guard-mirror-beside-catalogue", "guard-mirror-branch-green")
GUARD_INPUTS = ("guard-mirror-beside-conf", "guard-mirror-inputs-join")  # TOOL-dGroundRules-25 S19, S21
DEPLOY_REL = ".governance/deploy.toml"
DECISIONS_REL = "memory/DECISIONS.md"
# A measured-file cap whose key carries slashes and a leading dot, and the spec folder's class row, so
# the guard's key handling is proved on the shapes the census holds, not on one-segment names
# (TOOL-dGroundRules-21 S22).
BIG_FILE = ".claude/skills/x/SKILL.md"
# The [runtime] table leads the file: guard-not-budgets raises its count, which sits outside budgets.*,
# and a row appended at the end, as guard-new-row's is, still lands under [budgets] (TOOL-dGroundRules-77).
GUARD_POLICY = f'[runtime]\nagents-in-flight = 4\n\n[budgets]\n"{BIG_FILE}" = 100\n"small.md" = 50\n"memory/builds/*/spec/" = 10\n'
BIG, SMALL, CLASS = f'"{BIG_FILE}" = 100\n', '"small.md" = 50\n', '"memory/builds/*/spec/" = 10\n'
FLIGHT = "agents-in-flight = 4\n"
RAISED = (POLICY_REL, lambda t: t.replace(BIG, '# RAISED 100 -> 120, 2026-10-23, TOOL-x-1, measured 118 bytes\n'
                                                 f'"{BIG_FILE}" = 120\n'))
UNARGUED = (POLICY_REL, lambda t: t.replace(BIG, f'"{BIG_FILE}" = 120\n'))
ROW = (DECISIONS_REL, lambda t: t + f"- TOOL-x-1 · {BIG_FILE} raised to 120\n")
NO_RAISED, NO_ROW = "no RAISED", f"no {DECISIONS_REL} row"
# case -> [(scenario, [(path, edit of its text, "" when absent)], the exit wanted, needles stdout
# must carry, needles it must not)]; each scenario is staged alone over a fresh commit.
GUARD_PLANTS = {
    "guard-admits-raise": [("raise", [RAISED, ROW], 0, [f"policy-guard: admitted · budgets.\"{BIG_FILE}\" 100 -> 120"], [])],
    "guard-lowered": [("lowered", [(POLICY_REL, lambda t: t.replace(BIG, f'# RAISED 100 -> 90\n"{BIG_FILE}" = 90\n')), ROW],
                       1, ["a lowering"], [])],
    "guard-two-raised": [("two raised", [RAISED, (POLICY_REL, lambda t: t.replace(SMALL, '# RAISED 50 -> 60\n'
                                                                                   '"small.md" = 60\n')), ROW],
                          1, ["2 keys changed"], [])],
    "guard-class-row": [("class row", [(POLICY_REL, lambda t: t.replace(
        CLASS, '# RAISED 10 -> 20\n"memory/builds/*/spec/" = 20\n')), ROW], 1, ["not a measured-file cap"], [])],
    "guard-beside-change": [("beside a change", [RAISED, (POLICY_REL, lambda t: t.replace(
        "[budgets]\n", '[budgets]\nenforce = "refuse"\n')), ROW], 1, ["2 keys changed"], [])],
    "guard-beside-path": [("beside a path", [RAISED, ROW, (DEPLOY_REL, lambda t: t + 'planted = "a line"\n')],
                           1, [f"refused · {DEPLOY_REL} · "], [])],
    "guard-no-record": [("no record", [UNARGUED], 1, [NO_RAISED, NO_ROW], [])],
    "guard-no-argument": [("no argument", [UNARGUED, ROW], 1, [NO_RAISED], [NO_ROW])],
    "guard-no-row": [("no row", [RAISED], 1, [NO_ROW], [NO_RAISED])],
    "guard-other-paths": [
        ("mirror", [(policy.MIRROR_REL, lambda t: t + "\n")], 1,
         [f"refused · {policy.MIRROR_REL} · differs from its render at HEAD",
          f"git restore --staged --worktree {policy.MIRROR_REL}"], []),
        ("instructions", [(".governance/instructions.toml", lambda t: 'planted = "a manifest"\n')], 1,
         ["refused · .governance/instructions.toml · "], []),
        ("deploy", [(DEPLOY_REL, lambda t: t.replace("fixture", "planted"))], 1, [f"refused · {DEPLOY_REL} · "], []),
    ],
    "guard-new-row": [("new row", [(POLICY_REL, lambda t: t + '# RAISED 0 -> 10\n"new.md" = 10\n'), ROW],
                       1, ['a key was added: budgets."new.md"'], [])],
    "guard-removed-row": [("removed row", [(POLICY_REL, lambda t: t.replace(SMALL, "")), ROW],
                           1, ["a key was removed"], [])],
    "guard-other-line": [("another line", [RAISED, ROW, (POLICY_REL, lambda t: t.replace(CLASS, CLASS + "# planted\n"))],
                          1, ["another line of the policy file changed"], [])],
    "guard-not-budgets": [("not budgets", [(POLICY_REL, lambda t: t.replace(FLIGHT, "# RAISED 4 -> 6\nagents-in-flight = 6\n")), ROW],
                           1, ["only a cap under budgets.*"], [])],
    "guard-not-a-count": [("not a count", [(POLICY_REL, lambda t: t.replace(SMALL, '"small.md" = "60"\n')), ROW],
                           1, ["is not a count"], [])],
}


def build_guard_repo():
    """build_repo's fixture with guard.py and its list copied beside the catalogue, a tracked BIG_FILE
    and small.md, a deploy.toml, a decision log holding one row, and a policy file whose [budgets]
    table sets BIG_FILE to 100, "small.md" to 50 and the class row "memory/builds/*/spec/" to 10,
    behind a runtime table setting agents-in-flight to 4, all committed. -> (repo, kit copy)."""
    repo, kit = build_repo(policy.load_catalogue(KIT))
    for f in GUARD_FILES:
        (kit / f).write_bytes((KIT / f).read_bytes().replace(b"\r\n", b"\n"))
    for rel, text in ((BIG_FILE, "big\n"), ("small.md", "small\n"), (DEPLOY_REL, 'deployer = "fixture"\n'),
                      (DECISIONS_REL, "# decisions\n\n- TOOL-x-0 · the first row\n"), (POLICY_REL, GUARD_POLICY)):
        Path(repo, rel).parent.mkdir(parents=True, exist_ok=True)
        Path(repo, rel).write_text(text, encoding="utf-8", newline="\n")
    run_fixture_git(repo, "add", "-A")
    run_fixture_git(repo, "commit", "-q", "-m", "the guard and its subjects")
    return repo, kit


def run_guard_case(name):
    """`guard.py --staged` over build_guard_repo, judged by its exit code and stdout: each scenario of
    GUARD_PLANTS staged alone, or for `guard-merge-side` a merge of a branch whose policy file differs,
    conflicted, concluded with the branch's side (exit 0, a parent's blob) and then with a third text
    (exit 1). The GUARD_MIRROR cases (TOOL-dGroundRules-19) commit a catalogue row and run
    `mirror --write`: `guard-mirror-render` stages the mirror alone, exit 0;
    `guard-mirror-beside-catalogue` first moves the row back into the index, exit 1;
    `guard-mirror-branch-green` does it on a branch, commits the admitted mirror, and runs
    `mirror --check` at the new HEAD, which must be fresh."""
    repo, kit = build_guard_repo()
    guard = [sys.executable, str(kit / "guard.py"), "--staged"]
    checks = []
    try:
        if name == "guard-merge-side":
            for branch, n in (("side", 60), ("main", 55)):
                run_fixture_git(repo, "checkout", "-q", *(["-b"] if branch == "side" else []), branch)
                write_policy(repo, GUARD_POLICY.replace(SMALL, f'"small.md" = {n}\n'))
                run_fixture_git(repo, "commit", "-q", "-am", branch)
            try:
                run_fixture_git(repo, "merge", "-q", "side")
            except subprocess.CalledProcessError:
                pass  # the conflict is the point; MERGE_HEAD says whether it happened
            merging = bool((policy.run_git(repo, "rev-parse", "-q", "--verify", "MERGE_HEAD") or "").strip())
            checks.append(("merge", "a conflicted merge of side is in progress", merging,
                           "MERGE_HEAD " + ("resolves" if merging else "does not resolve")))
            run_fixture_git(repo, "checkout", "--theirs", "--", POLICY_REL)
            run_fixture_git(repo, "add", "--", POLICY_REL)
            checks.append(check_run("merge, the branch's side", "guard.py --staged", guard,
                                    lambda rc, o, e: rc == 0, cwd=repo))
            write_policy(repo, GUARD_POLICY.replace(SMALL, '"small.md" = 70\n'))
            run_fixture_git(repo, "add", "--", POLICY_REL)
            checks.append(check_run("merge, a third text", "guard.py --staged", guard,
                                    lambda rc, o, e: rc == 1 and "policy-guard: refused" in o, cwd=repo))
        if name in GUARD_MIRROR:
            beside = name == "guard-mirror-beside-catalogue"
            if name == "guard-mirror-branch-green":
                run_fixture_git(repo, "checkout", "-q", "-b", "side")
            write_edit(kit / policy.CATALOGUE, lambda t: t + render_planted_row("a catalogue row an agent adds"))
            run_fixture_git(repo, "add", "--", str(kit / policy.CATALOGUE))
            run_fixture_git(repo, "commit", "-q", "-m", "a catalogue row")
            checks.append(check_get("the row committed", repo, ["--write"], lambda rc, o, e: rc == 0
                                    and o.startswith("policy: mirror written"), kit=kit, verb="mirror"))
            if beside:  # the row back in the index beside the mirror rendered over it
                run_fixture_git(repo, "reset", "-q", "--soft", "HEAD~1")
            run_fixture_git(repo, "add", "--", policy.MIRROR_REL)
            want, needle = (1, f"its input {budgets.derive_kit_rel()}{policy.CATALOGUE} is staged changed") if beside \
                else (0, "equals its render at HEAD")
            checks.append(check_run("the mirror staged" + (" beside the row" if beside else " alone"), "guard.py --staged",
                                    guard, lambda rc, o, e: rc == want and needle in o, cwd=repo))
            if name == "guard-mirror-branch-green":
                run_fixture_git(repo, "commit", "-q", "-m", "the mirror, regenerated")
                checks.append(check_get("the mirror committed", repo, ["--check"], lambda rc, o, e: rc == 0
                                        and o == "policy: mirror fresh\n", kit=kit, verb="mirror"))
        if name in GUARD_INPUTS:
            # TOOL-dGroundRules-25 S19, S21: an input the mirror records, staged changed beside a mirror
            # rendered at HEAD. `-beside-conf` stages `.agent-cap.conf`, an input no guarded path names;
            # `-inputs-join` first commits a render recording one input more than today's, so the guard
            # reads its inputs from the mirror's own record, never from a list of its own.
            extra = policy.LEGACY_FANOUT
            if name == "guard-mirror-inputs-join":
                extra = ".zz-recorded.conf"
                write_edit(kit / "policy.py", lambda t: t.replace("LEGACY_INPUTS = (LEGACY_FANOUT,)",
                                                                  f"LEGACY_INPUTS = (LEGACY_FANOUT, {extra!r})"))
                run_fixture_git(repo, "add", "-A")
                run_fixture_git(repo, "commit", "-q", "-m", "a render recording one more input")
            checks.append(check_get("HEAD", repo, ["--write"], lambda rc, o, e: rc == 0
                                    and o.startswith("policy: mirror written"), kit=kit, verb="mirror"))
            recorded = json.loads(Path(repo, *MIRROR_FILE).read_bytes()).get("legacy_blobs", {})
            checks.append(("the render", f"records {extra} under legacy_blobs", extra in recorded, f"legacy_blobs {sorted(recorded)}"))
            Path(repo, extra).write_text("FANOUT_CAP=2\n", encoding="utf-8", newline="\n")
            run_fixture_git(repo, "add", "--", extra, policy.MIRROR_REL)
            checks.append(check_run(f"the mirror staged beside {extra}", "guard.py --staged", guard, lambda rc, o, e:
                                    rc == 1 and f"its input {extra} is staged changed" in o, cwd=repo))
        for scenario, edits, want, present, absent in GUARD_PLANTS.get(name, []):
            for rel, edit in edits:
                path = Path(repo, rel)
                path.write_text(edit(path.read_text(encoding="utf-8") if path.exists() else ""),
                                encoding="utf-8", newline="\n")
                run_fixture_git(repo, "add", "--", rel)
            checks.append(check_run(scenario, "guard.py --staged", guard, lambda rc, o, e, want=want, present=present,
                                    absent=absent: rc == want and all(n in o for n in present)
                                    and not any(n in o for n in absent), cwd=repo))
            run_fixture_git(repo, "reset", "-q", "--hard")
    finally:
        remove_repo(repo)
    return print_checks(name, checks)


# ---- the legacy policy homes (TOOL-dGroundRules-7) ----------------------------------------------

LEGACY_CONF = 'REVIEW_ROUNDS="3"\nKEPT_KEY="1"\n'
LEGACY_GATE = "#!/usr/bin/env sh\n# The fixture's gate file.\n#   GOV_PYTHON=<launcher>  a documented key\nINHERITED_RED=land\n"
LEGACY_HOUSE = '[effort]\ndefault = "medium"\n\n[gates]\n'
LEGACY_REPORT = "  legacy homes: "
LEGACY_CASES = ("today", "planted-row", "growth", "shrink", "retrofit", "unmarked", "absent-homes", "withheld")


def build_legacy_repo(t, gate, house):
    """A repository at `t`/r holding a copy of this kit's policy.py, catalogue and summary list at the
    kit's own path, a `.unattended.conf`, the gate file's text `gate` (none where None) and, where
    `house`, a house file where the copy resolves HOUSE_HOME; committed on main and pushed to one bare
    remote, then the copy's `lists --write` seeding the legacy list over a header-only one, committed
    and pushed, so the landed list is that seed. -> the kit copy."""
    repo = t / "r"
    kit = repo / (policy.run_git(KIT, "rev-parse", "--show-prefix") or "").strip()  # derived, never spelled
    kit.mkdir(parents=True)
    for f in (*READER_FILES, policy.CATALOGUE, policy.LIST):
        (kit / f).write_bytes((KIT / f).read_bytes().replace(b"\r\n", b"\n"))
    homes = {repo / ".unattended.conf": LEGACY_CONF}
    if gate is not None:
        homes[Path(repo, policy.GATE_FILE)] = gate
    if house:
        homes[kit.parent / policy.HOUSE_HOME[len(policy.TOOL_ROOT):]] = LEGACY_HOUSE  # where resolve_kit_dir probes
    for path, text in homes.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")
    run_fixture_git(t, "init", "-q", "--bare", "b.git")
    run_fixture_git(repo, "init", "-q")
    run_fixture_git(repo, "symbolic-ref", "HEAD", "refs/heads/main")
    run_fixture_git(repo, "remote", "add", FIXTURE_REMOTE, (t / "b.git").as_posix())
    for msg in ("the legacy homes", "the legacy list, seeded"):
        if msg.endswith("seeded"):  # `lists --write` updates a list and never creates one (TOOL-dGroundRules-17)
            (kit / policy.LEGACY_LIST).write_text(policy.LEGACY_HEADER, encoding="utf-8", newline="\n")
            run_legacy_lists(kit, "--write")
        run_fixture_git(repo, "add", "-A")
        run_fixture_git(repo, "commit", "-q", "-m", msg)
        run_fixture_git(repo, "push", "-q", FIXTURE_REMOTE, "main")
    return kit


def run_legacy_lists(kit, verb):
    """The kit copy's `policy.py lists <verb>`, run in its repository -> (exit code, stdout and stderr)."""
    p = subprocess.run([sys.executable, str(kit / "policy.py"), "lists", verb], cwd=kit, capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    return p.returncode, (p.stdout + p.stderr).replace("\r", "")


def check_legacy_lists(case, kit, verb, want_rc, want_reports, label=None):
    """The kit copy's `lists <verb>` judged by its exit code and its exact `legacy homes` reports ->
    ((scenario, what, ok, what it observed), its output)."""
    rc, out = run_legacy_lists(kit, verb)
    reports = [ln[len(LEGACY_REPORT):] for ln in out.split("\n") if ln.startswith(LEGACY_REPORT)]
    ok = rc == want_rc and reports == want_reports
    seen = f"exit {rc} · {len(reports)} report(s)" + "".join(f" · {r}" for r in reports)
    return (label or f"case {case}: {'green' if rc == 0 else 'red' if rc == 1 else 'refused'}", f"lists {verb}", ok,
            seen + ("" if ok else f" · output {out.strip()!r}")), out


def run_legacy_homes(name):
    """The legacy-homes list over a planted repository per case, each judged by the copy's `lists`
    verbs: `today` green unplanted; `planted-row` a typed row appended, red with the typed-row report
    alone; `growth` a conf key added and its row typed into the list, red with the new-home report
    alone, and `lists --write` exiting 1 with the list unchanged; `shrink` a conf key removed, red
    with the stale-list report alone, then green after `lists --write` with the row gone; `retrofit`
    a cutoff and a pin added, green with no row for either; `unmarked` a gate key GATE_ENV_MARKS
    lacks in the landed list, red with the no-mark report; `absent-homes` no gate file and no house
    file, green with one announce line for each; `withheld` the list deleted, the install shape,
    green with the not-graded line and no report (TOOL-dGroundRules-76)."""
    checks = []
    for case in LEGACY_CASES:
        t = Path(tempfile.mkdtemp(prefix="pol-"))
        try:
            gate = None if case == "absent-homes" else LEGACY_GATE + ("GATE_PLANTED=1\n" if case == "unmarked" else "")
            kit = build_legacy_repo(t, gate, case != "absent-homes")
            conf, listed = t / "r" / ".unattended.conf", kit / policy.LEGACY_LIST
            if case == "planted-row":
                write_edit(listed, lambda s: s + ".unattended.conf PLANTED_KEY owner-policy\n")
                checks.append(check_legacy_lists(case, kit, "--check", 1, ["typed row .unattended.conf PLANTED_KEY owner-policy"])[0])
            elif case == "growth":
                write_edit(conf, lambda s: s + 'PLANTED_NEW="1"\n')
                write_edit(listed, lambda s: s + ".unattended.conf PLANTED_NEW owner-policy\n")
                held = listed.read_bytes()
                new = [f".unattended.conf PLANTED_NEW is a new legacy home and the list is shrink-only; carry it as a key "
                       f"in {policy.derive_catalogue_rel()} instead"]
                checks.append(check_legacy_lists(case, kit, "--check", 1, new)[0])
                check = check_legacy_lists(case, kit, "--write", 1, new, label=f"case {case}: lists --write")[0]
                same = listed.read_bytes() == held
                checks.append(check[:2] + (check[2] and same, check[3] + f" · the list {'unchanged' if same else 'CHANGED'}"))
            elif case == "shrink":
                write_edit(conf, lambda s: s.replace('KEPT_KEY="1"\n', ""))
                checks.append(check_legacy_lists(case, kit, "--check", 1, [
                    "stale list at .unattended.conf KEPT_KEY owner-policy, re-run lists --write"])[0])
                checks.append(check_legacy_lists(case, kit, "--write", 0, [], label=f"case {case}: lists --write")[0])
                gone = " KEPT_KEY " not in listed.read_text(encoding="utf-8")
                check = check_legacy_lists(case, kit, "--check", 0, [], label=f"case {case}, after lists --write: green")[0]
                checks.append(check[:2] + (check[2] and gone, check[3] + f" · the row {'gone' if gone else 'STILL LISTED'}"))
            elif case == "retrofit":
                write_edit(conf, lambda s: s + 'PLANTED_CUTOFF="2026-11-01"\nPLANTED_PIN="3"\n')
                checks.append(check_legacy_lists(case, kit, "--check", 0, [])[0])
                check = check_legacy_lists(case, kit, "--write", 0, [], label=f"case {case}: lists --write")[0]
                rows = [r for r in policy.parse_list(listed.read_text(encoding="utf-8")) if " PLANTED_" in r]
                checks.append(check[:2] + (check[2] and not rows, check[3] + f" · {len(rows)} PLANTED_ row(s) listed"))
            elif case == "withheld":
                listed.unlink()  # the install shape: kit.toml withholds the list (TOOL-dGroundRules-17)
                check, out = check_legacy_lists(case, kit, "--check", 0, [])
                told = f"policy lists: {policy.LEGACY_LIST} · not graded · {policy.LEGACY_WITHHELD}" in out.split("\n")
                checks.append(check[:2] + (check[2] and told, check[3] + f" · {'announced not graded' if told else 'NO not-graded line'}"))
            else:
                check, out = check_legacy_lists(case, kit, "--check", 1 if case == "unmarked" else 0,
                                                [f"GATE_PLANTED in {policy.GATE_FILE} has no mark in GATE_ENV_MARKS"]
                                                if case == "unmarked" else [])
                if case == "absent-homes":
                    told = [h for h in (policy.GATE_FILE, policy.HOUSE_HOME)
                            if sum(ln.startswith(f"legacy homes: no {h} ") for ln in out.split("\n")) == 1]
                    check = check[:2] + (check[2] and len(told) == 2, check[3] + f" · announced: {', '.join(told) or 'none'}")
                checks.append(check)
        except subprocess.CalledProcessError as exc:
            checks.append((f"case {case}: not built", "the fixture's git", False,
                           f"git exited {exc.returncode}: {(exc.stderr or '').strip() or '(no stderr)'}"))
        finally:
            remove_repo(t)
    return print_checks(name, checks)


def run_legacy_main_dropped(name):
    """`legacy-homes-main-dropped` (TOOL-dGroundRules-21 S24): a branch opened from main and committed
    once, then main drops the conf key KEPT_KEY with its row and lands; the branch's merge-base still
    holds the row and the branch's derivation still carries the key. The branch's `lists --check` must
    report no `new legacy home`, and exit 0: the base is the merge-base, never the landed tip."""
    t = Path(tempfile.mkdtemp(prefix="pol-"))
    checks = []
    try:
        kit = build_legacy_repo(t, LEGACY_GATE, True)
        repo, conf = t / "r", t / "r" / ".unattended.conf"
        run_fixture_git(repo, "checkout", "-q", "-b", "b")
        Path(repo, "branch-work.md").write_text("the branch's own change\n", encoding="utf-8", newline="\n")
        run_fixture_git(repo, "add", "-A")
        run_fixture_git(repo, "commit", "-q", "-m", "the branch, opened before main dropped a key")
        run_fixture_git(repo, "checkout", "-q", "main")
        write_edit(conf, lambda s: s.replace('KEPT_KEY="1"\n', ""))
        run_legacy_lists(kit, "--write")
        run_fixture_git(repo, "commit", "-q", "-am", "main drops KEPT_KEY and its row")
        run_fixture_git(repo, "push", "-q", FIXTURE_REMOTE, "main")
        run_fixture_git(repo, "checkout", "-q", "b")
        check, out = check_legacy_lists("main-dropped", kit, "--check", 0, [], label="the branch after main dropped KEPT_KEY")
        grew = "is a new legacy home" in out
        checks.append(check[:2] + (check[2] and not grew, check[3] + f" · {'a NEW LEGACY HOME reported' if grew else 'no new legacy home'}"))
    except subprocess.CalledProcessError as exc:
        checks.append((name, "the fixture's git", False, f"git exited {exc.returncode}: {(exc.stderr or '').strip()}"))
    finally:
        remove_repo(t)
    return print_checks(name, checks)


def run_legacy_present(name):
    """`legacy-homes-present` (TOOL-dGroundRules-17): this kit's own directory holds the legacy list,
    and its `kit.toml` withholds the list from installs by a `project-owned` rule naming it. Where the
    list is absent `arm_legacy_homes` announces itself not graded, so on gov's tree this case is what
    reds a list deleted there; the leg running it is gov's alone."""
    held = (KIT / policy.LEGACY_LIST).is_file()
    try:
        rules = tomllib.loads((KIT / "kit.toml").read_text(encoding="utf-8")).get("files", [])
        seen = "no such rule"
    except (OSError, tomllib.TOMLDecodeError) as exc:
        rules, seen = [], f"kit.toml does not read: {exc}"
    withheld = any(r.get("role") == "project-owned" and policy.LEGACY_LIST in
                   (r.get("include") if isinstance(r.get("include"), list) else [r.get("include")]) for r in rules)
    return print_checks(name, [
        ("the list", f"{policy.LEGACY_LIST} in this kit's directory", held,
         f"{'present' if held else 'absent'} in {KIT.as_posix()}"),
        ("the descriptor", f"a project-owned kit.toml rule naming {policy.LEGACY_LIST}", withheld,
         "withheld from installs" if withheld else seen)])


# ---- reader coverage (TOOL-dGroundRules-8) -----------------------------------------------------

RC_KEY, RC_OWNER = "fixture.planted", "bPlanted"
RC_SPEC = "memory/builds/bPlanted/spec/2026-10-23-spec-TOOL-bPlanted-1.md"
RC_HEADER = "# TOOL-bPlanted-1 — a planted spec\n\n**Status:** {} · rev-1 · 2026-10-23 · node d · Tier-1 · base 0123abcd\n"
RC_CALL = 'value = resolve("fixture.planted")\n'
RC_CLI = "python policy.py get fixture.planted\n"
# case -> (catalogue rows (key, owner), the planted spec's token at the landed revision, its token in
# the working tree, the tracked files planted {path: text}, the key that must red or None, the count
# of keys graded). `not-a-reader` also carries this module, copied to the kit copy's path.
RC_CASES = {
    "landed-no-reader": ([(RC_KEY, RC_OWNER)], "CLOSED", "CLOSED", {}, RC_KEY, 1),
    "unlanded": ([(RC_KEY, RC_OWNER)], "OPEN", "OPEN", {}, None, 0),
    "no-build": ([(RC_KEY, "bAbsent")], "CLOSED", "CLOSED", {}, None, 0),
    "reader-python": ([(RC_KEY, RC_OWNER)], "CLOSED", "CLOSED", {"consumer.py": RC_CALL}, None, 1),
    "reader-cli": ([(RC_KEY, RC_OWNER)], "CLOSED", "CLOSED", {"consumer.sh": RC_CLI}, None, 1),
    "reader-js": ([(RC_KEY, RC_OWNER)], "CLOSED", "CLOSED",
                  {"consumer.js": "const value = mirror.get('fixture.planted');\n"}, None, 1),
    "not-a-reader": ([(RC_KEY, RC_OWNER)], "CLOSED", "CLOSED",
                     {"notes.md": RC_CALL, "consumer.test.sh": RC_CLI, "consumer.py": "# " + RC_CALL,
                      policy.MIRROR_REL: json.dumps({"keys": {RC_KEY: {"value": "a"}}}) + "\n"},
                     RC_KEY, 1),
    "history-not-tree": ([(RC_KEY, RC_OWNER)], "CLOSED", "OPEN", {}, RC_KEY, 1),
    "tree-not-history": ([(RC_KEY, RC_OWNER)], "OPEN", "CLOSED", {}, None, 0),
    "pattern-read": ([("fixture.*", RC_OWNER)], "CLOSED", "CLOSED",
                     {"consumer.sh": 'python policy.py get "fixture.$name"\n'}, None, 1),
    "pattern-only-sibling": ([("fixture.*", RC_OWNER), ("fixture.exact", RC_OWNER)], "CLOSED", "CLOSED",
                             {"consumer.sh": "python policy.py get fixture.exact\n"}, "fixture.*", 2),
}


def build_reader_coverage_repo(t, name, spec=None, prefix=None, tree_lib=True):
    """The case's repository at `t`/r on main: the kit copy at this kit's own path, or at `prefix`,
    holding a catalogue of the case's rows (`spec`, else RC_CASES[name]), the planted spec with its
    landed token, and the planted files, committed and pushed to one bare remote, so the landed
    revision is that commit; then the spec's working-tree token written over it, and, where `tree_lib`,
    the memory-tree kit's `tree_lib.py` untracked beside the kit copy, where `resolve_kit_dir` finds
    it from there (TOOL-dGroundRules-21 S26). -> the kit copy."""
    rows, at_landing, in_tree, plants, _red, _n = spec or RC_CASES[name]
    repo = t / "r"
    own = (policy.run_git(KIT, "rev-parse", "--show-prefix") or "").strip()  # derived, never spelled
    kit = repo / (prefix or own)
    files = {**plants, RC_SPEC: RC_HEADER.format(at_landing)}
    if name == "not-a-reader":  # this module names the key in reader shapes, as its fixtures do
        files[(kit / Path(__file__).name).relative_to(repo).as_posix()] = Path(__file__).read_text(encoding="utf-8")
    files[(kit / policy.CATALOGUE).relative_to(repo).as_posix()] = "".join(
        f'[[key]]\nname = "{k}"\nallowed = ["a"]\ndefault = "a"\nowner = "{o}"\n\n' for k, o in rows)
    for rel, text in files.items():
        Path(repo, rel).parent.mkdir(parents=True, exist_ok=True)
        Path(repo, rel).write_text(text, encoding="utf-8", newline="\n")
    run_fixture_git(t, "init", "-q", "--bare", "b.git")
    run_fixture_git(repo, "init", "-q")
    run_fixture_git(repo, "symbolic-ref", "HEAD", "refs/heads/main")
    run_fixture_git(repo, "remote", "add", FIXTURE_REMOTE, (t / "b.git").as_posix())
    run_fixture_git(repo, "add", "-A")
    run_fixture_git(repo, "commit", "-q", "-m", "the landed state")
    run_fixture_git(repo, "push", "-q", FIXTURE_REMOTE, "main")
    Path(repo, RC_SPEC).write_text(RC_HEADER.format(in_tree), encoding="utf-8", newline="\n")
    if tree_lib:
        (kit.parent / "memory-tree").mkdir(parents=True, exist_ok=True)
        shutil.copyfile(load_tree_lib().__file__, kit.parent / "memory-tree" / "tree_lib.py")
    return kit


def run_reader_coverage(name):
    """`check_reader_coverage` over one repository per RC_CASES case, printing `case <name>: red|green`:
    a red case must find exactly one key with no reader, its key and owner named; a green case none;
    each must grade its count of keys, and a case grading none must print the announce line."""
    checks = []
    for case, (_rows, _at, _in, _plants, red, want_n) in RC_CASES.items():
        t = Path(tempfile.mkdtemp(prefix="pol-"))
        try:
            kit = build_reader_coverage_repo(t, case)
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                n, findings = check_reader_coverage(t / "r", kit=kit)
            told = "so this arm checked nothing at" in out.getvalue()
            ok = n == want_n and (told or n) and (
                len(findings) == 1 and f": {red} (owner {RC_OWNER}, landed at " in findings[0] if red else not findings)
            checks.append((f"case {case}: {'red' if findings else 'green'}", "check_reader_coverage", bool(ok),
                           f"graded {n} · " + ("; ".join(findings) or out.getvalue().strip().replace("\n", " · "))))
        except subprocess.CalledProcessError as exc:
            checks.append((f"case {case}: not built", "the fixture's git", False,
                           f"git exited {exc.returncode}: {(exc.stderr or '').strip() or '(no stderr)'}"))
        except policy.Refusal as exc:
            checks.append((f"case {case}: refused", "check_reader_coverage", False, str(exc)))
        finally:
            remove_repo(t)
    return print_checks(name, checks)


RELOCATED_PREFIX = "vendor/gov/policy/"  # a tool root unlike gov's own, so no path can be guessed
# The two read shapes a correct build of units 4 and 9 spells for a pattern key (TOOL-dGroundRules-21 S27).
QUOTED_READS = {"an f-string's quoted segment": "value = resolve(f'budgets.\"{cap}\"')\n",
                "a name joined into a quoted segment": "value = resolve('budgets.\"' + name + '\"')\n"}


def run_reader_relocated(name):
    """`reader-coverage-relocated` (TOOL-dGroundRules-21 S25, S26): `landed-no-reader`'s repository with
    the kits at RELOCATED_PREFIX's tool root, the memory-tree kit's `tree_lib.py` beside the policy kit
    there. The reader-coverage arm must grade the landed owner, 1 key, and red it; with `tree_lib.py`
    absent it must refuse, one finding naming where the resolver looked. Never a population of 0."""
    checks = []
    for present in (True, False):
        t = Path(tempfile.mkdtemp(prefix="pol-"))
        scenario = "memory-tree beside it" if present else "memory-tree absent"
        try:
            kit = build_reader_coverage_repo(t, "landed-no-reader", prefix=RELOCATED_PREFIX, tree_lib=present)
            with contextlib.redirect_stdout(io.StringIO()):
                verdict, findings = run_arm(ARM["arm_reader_coverage"], t / "r", kit)
            said = "; ".join(f"{k}: {w}" for k, w in findings)
            ok = (verdict.startswith("1 finding(s) · 1 of ") and f"{RC_KEY} (owner {RC_OWNER}" in said if present
                  else verdict.startswith("1 finding(s)") and "looked in" in said and "memory-tree" in said)
            checks.append((scenario, "arm_reader_coverage at " + RELOCATED_PREFIX, bool(ok) and "not graded" not in verdict,
                           f"{verdict} · {said or 'no finding'}"))
        except subprocess.CalledProcessError as exc:
            checks.append((scenario, "the fixture's git", False, f"git exited {exc.returncode}: {(exc.stderr or '').strip()}"))
        finally:
            remove_repo(t)
    return print_checks(name, checks)


def run_reader_quoted(name):
    """`reader-quoted-pattern` (TOOL-dGroundRules-21 S27): a catalogue row `budgets.*` whose owner has
    landed, read by each of QUOTED_READS in a tracked consumer, must grade 1 key and find no reader
    missing; with neither planted it must red `budgets.*`."""
    checks = []
    for what, plant in (*QUOTED_READS.items(), ("no reader", None)):
        t = Path(tempfile.mkdtemp(prefix="pol-"))
        spec = ([("budgets.*", RC_OWNER)], "CLOSED", "CLOSED", {"consumer.py": plant} if plant else {}, None, 1)
        try:
            kit = build_reader_coverage_repo(t, name, spec=spec)
            with contextlib.redirect_stdout(io.StringIO()):
                n, findings = check_reader_coverage(t / "r", kit=kit)
            ok = n == 1 and (not findings if plant else len(findings) == 1 and ": budgets.* (owner " in findings[0])
            checks.append((what, "check_reader_coverage", ok, f"graded {n} · {'; '.join(findings) or 'no finding'}"))
        except (subprocess.CalledProcessError, policy.Refusal) as exc:
            checks.append((what, "the fixture", False, str(exc)))
        finally:
            remove_repo(t)
    return print_checks(name, checks)


# ---- the agent limit (TOOL-dGroundRules-10) ------------------------------------------------------

LIMIT_POLICY = "[runtime]\nagents-in-flight = {n}\n"
HOOK_FILES = ("agent-cap.js", "scratch-guard.js")
SETTINGS_FILE = (".claude", "settings.json")
SETTINGS_LOCAL = (".claude", "settings.local.json")
# The retired print mode's flag in two halves, so the grep `limit-hook-env-cap` runs over the tool root
# finds no carrier of it here either.
RETIRED_FLAG = "--print" + "-cap"
HANDOFF_ROLE = "## Role\n\nYou research.\n\n"
HANDOFF_TASK = "## Task\n\nThis handoff is for build `bx`, unit `T-1`.\n"
HANDOFF_FILE = "memory/builds/bx/prompts/2026-10-24-prompt-T-1-researcher.md"
HARNESS_FILE = "harness/h.js"
HARNESS_TEXT = "export const meta = { name: 'h', description: 'one agent' }\nconst s = await agent('one')\n"
LIMIT_ROLES = {"roles": {"gov-researcher": {"agent": True, "workflow": "research", "writes": "none"}},
               "harnesses": [HARNESS_FILE]}
# A verifier split at 6 (TOOL-dGroundRules-18 AC3), which rule 2 judges against MAX_VERIFIERS whatever the limit.
VERIFIER_SPLIT = ("const K = 6\nconst g = chunk(all, Math.ceil(all.length / K)) // gov:fixed-verifiers\n"
                  "const r = await boundedParallel(g.map((x) => () => agent(x)), 5)\n")


def write_settings(repo, env, rel=SETTINGS_FILE):
    """`.claude/settings.json`, or the file `rel` names, holding `env` as its env, or `{}` for None."""
    Path(repo, rel[0]).mkdir(exist_ok=True)
    Path(repo, *rel).write_text(json.dumps({} if env is None else {"env": env}, indent=2) + "\n",
                                encoding="utf-8", newline="\n")


def render_limit_env(n):
    return {v: str(n) for v in policy.SETTINGS_VARS}


def build_limit_repo(path, policy_text, conf=None, mirror=True):
    """A git repository at `path` on `main`, no remote, so local main is its landed revision: this
    kit's reader, mirror helper and shim beside its catalogue at the kit's own path, the hooks kit's
    agent-cap.js and scratch-guard.js at theirs, `policy_text` as the policy file (None: none) and
    `conf` as `.agent-cap.conf`, committed; then, when `mirror`, the mirror rendered at that commit,
    committed over it: a malformed conf refuses the render (TOOL-dGroundRules-15), so its case has none.
    -> (repo, kit copy, hook copy)."""
    hooks = resolve_kit_dir("hooks", "agent-cap.js", KIT)
    path.mkdir()
    kit = path / (policy.run_git(KIT, "rev-parse", "--show-prefix") or "").strip()
    hook_dir = path / (policy.run_git(hooks, "rev-parse", "--show-prefix") or "").strip()
    for src, dst, names in ((KIT, kit, (policy.CATALOGUE, *MIRROR_KIT_FILES)), (hooks, hook_dir, HOOK_FILES)):
        dst.mkdir(parents=True, exist_ok=True)
        for f in names:
            (dst / f).write_bytes((Path(src) / f).read_bytes().replace(b"\r\n", b"\n"))
    if policy_text is not None:
        write_policy(path, policy_text)
    if conf is not None:
        Path(path, policy.LEGACY_FANOUT).write_bytes(conf.encode("utf-8"))
    run_fixture_git(path, "init", "-q")
    run_fixture_git(path, "symbolic-ref", "HEAD", "refs/heads/main")
    run_fixture_git(path, "add", "-A")
    run_fixture_git(path, "commit", "-q", "-m", "the agent limit's fixture")
    if not mirror:
        return path, kit, hook_dir / "agent-cap.js"
    Path(path, *MIRROR_FILE).parent.mkdir(exist_ok=True)
    Path(path, *MIRROR_FILE).write_bytes(policy.render_mirror(path, "HEAD"))
    run_fixture_git(path, "add", "-A")
    run_fixture_git(path, "commit", "-q", "-m", "its mirror")
    return path, kit, hook_dir / "agent-cap.js"


def check_hook_call(scenario, what, hook, payload, want, env=None, args=(), cwd=None):
    """`node <hook> <args>` in `cwd` with the JSON `payload` on stdin -> (scenario, what, ok, what it
    observed), `want` judging (exit code, stderr). CLAUDE_PROJECT_DIR is dropped, so rule 6 reads the
    payload cwd alone."""
    env = {k: v for k, v in (env or os.environ).items() if k != "CLAUDE_PROJECT_DIR"}
    try:
        p = subprocess.run(["node", str(hook), *args], input=json.dumps(payload), capture_output=True, text=True,
                           encoding="utf-8", errors="replace", env=env, cwd=cwd)
        rc, err = p.returncode, p.stderr.replace("\r", "")
    except OSError as exc:
        rc, err = None, f"node did not run: {exc}"
    return scenario, what, want(rc, err), f"exit {rc} · stderr {err.strip()[:400] or '(none)'!r}"


def render_workflow(repo, script):
    return {"tool_name": "Workflow", "cwd": str(repo), "tool_input": {"script": script}}


def render_spawn(repo, uid, prompt="x", **extra):
    return {"tool_name": "Agent", "cwd": str(repo), "session_id": "limit-s", "prompt_id": "limit-p",
            "tool_use_id": uid, "tool_input": {"prompt": prompt, **extra}}


def write_handoff_fixture(repo):
    """The roles index, one handoff prompt file and one harness of `limit-hook-admits-eight`, the marker
    and digest computed as the renderer defines them. -> the Agent call's `tool_input`."""
    digest = lambda s: hashlib.sha256(s.encode("utf-8")).hexdigest()[:12]  # noqa: E731
    marker = (f"<!-- gov:handoff role=gov-researcher build=bx unit=T-1 path={HANDOFF_FILE} "
              f"role-sha={digest(HANDOFF_ROLE)} task-sha={digest(HANDOFF_TASK)} -->")
    for rel, text in ((HANDOFF_FILE, f"**Serves:** journal T-1\n\n# a handoff\n\n{marker}\n\n{HANDOFF_ROLE}{HANDOFF_TASK}"),
                      (HARNESS_FILE, HARNESS_TEXT), (".claude/roles.json", json.dumps(LIMIT_ROLES))):
        Path(repo, rel).parent.mkdir(parents=True, exist_ok=True)
        Path(repo, rel).write_text(text, encoding="utf-8", newline="\n")
    return {"subagent_type": "gov-researcher", "description": "bx · T-1 · research", "prompt": f"{marker}\n\n{HANDOFF_TASK}"}


def run_limit_case(name):
    """One planted repository per `limit-` case (TOOL-dGroundRules-10), judged by exit code and the
    text each criterion names. The conf cases read `policy.py get` at the landed revision; the render
    case commits two policy values; the hook cases run the hooks kit's agent-cap.js beside a copy of
    this kit, so rule 7 reads the fixture's own landed limit, with each payload's cwd the fixture."""
    t = Path(tempfile.mkdtemp(prefix="pol-"))
    checks = []
    default = next(r["default"] for r in policy.load_catalogue(KIT) if r.get("name") == AGENTS_KEY)
    has = lambda *needles: lambda rc, err: rc == 2 and all(n in err for n in needles)  # noqa: E731
    admits = lambda rc, err: rc == 0  # noqa: E731
    try:
        if name == "limit-conf-lowers":
            repo, kit, _hook = build_limit_repo(t / "r", None, "FANOUT_CAP=2\n")
            checks += [check_get(name, repo, [AGENTS_KEY], lambda rc, o, e: rc == 0 and o == "2\n", kit=kit),
                       check_get(name, repo, [AGENTS_KEY, "--explain"], lambda rc, o, e: rc == 0
                                 and f"lowered to 2 by FANOUT_CAP at {policy.LEGACY_FANOUT}:1" in e, kit=kit)]
        elif name == "limit-conf-no-raise":
            repo, kit, _hook = build_limit_repo(t / "r", None, "# a lower-only home\nFANOUT_CAP=8\n")
            checks.append(check_get(name, repo, [AGENTS_KEY, "--explain"], lambda rc, o, e: rc == 0
                                    and o == f"{default}\n" and f"FANOUT_CAP=8 at {policy.LEGACY_FANOUT}:2 does not lower it" in e,
                                    kit=kit))
        elif name == "limit-conf-malformed":
            repo, kit, _hook = build_limit_repo(t / "r", None, "FANOUT_CAP=abc\n", mirror=False)
            refused = f"policy: refused · {policy.LEGACY_FANOUT}:1 · FANOUT_CAP must be an integer of at least 1"
            checks += [check_get(name, repo, [AGENTS_KEY], lambda rc, o, e: rc == 2 and not o and e.strip() == refused,
                                 kit=kit),
                       check_get(name, repo, ["--print"], lambda rc, o, e: rc == 2 and not o and e.strip() == refused,
                                 kit=kit, verb="mirror")]
        elif name in ("limit-conf-mirror", "limit-conf-last-valid"):
            # The lowering's one home is resolve_read (TOOL-dGroundRules-15): the mirror, rendered
            # through it, must hold what `get` prints, read by the helper from that fresh mirror.
            if name == "limit-conf-mirror":
                n, source = 2, "default"
                repo, kit, _hook = build_limit_repo(t / "r", None, f"FANOUT_CAP={n}\n")
            else:
                n, source = 3, "last-valid"
                repo, kit, _hook = build_limit_repo(t / "r", LIMIT_POLICY.format(n=6))
                for rel, text, what in ((policy.LEGACY_FANOUT, f"FANOUT_CAP={n}\n", "the conf"),
                                        (POLICY_REL, MALFORMED, "a malformed policy file")):
                    Path(repo, rel).write_text(text, encoding="utf-8", newline="\n")
                    run_fixture_git(repo, "add", "-A")
                    run_fixture_git(repo, "commit", "-q", "-m", what)
                Path(repo, *MIRROR_FILE).write_bytes(policy.render_mirror(repo, "HEAD"))
                run_fixture_git(repo, "commit", "-q", "-am", "its mirror")
            lowered = f"lowered to {n} by FANOUT_CAP at {policy.LEGACY_FANOUT}:1"
            checks += [
                check_get(name, repo, [AGENTS_KEY, "--explain"], lambda rc, o, e: rc == 0 and o == f"{n}\n"
                          and f" · {source} · " in e and lowered in e, kit=kit),
                check_run(name, f"policy-mirror.js get {AGENTS_KEY} --explain",
                          ["node", str(kit / "policy-mirror.js"), "get", AGENTS_KEY, "--repo", str(repo), "--explain"],
                          lambda rc, o, e: rc == 0 and o == f"{n}\n" and f" · {source} · " in e and lowered in e
                          and "mirror absent at" not in e and "mirror stale at" not in e)]
        elif name == "limit-settings-render":
            repo, kit, _hook = build_limit_repo(t / "r", LIMIT_POLICY.format(n=8))
            settings = Path(repo, *SETTINGS_FILE)
            read_env = lambda: json.loads(settings.read_text(encoding="utf-8")).get("env", {})  # noqa: E731
            checks.append(check_get("at 8", repo, ["--write"], lambda rc, o, e: rc == 0, kit=kit, verb="settings"))
            checks.append(("at 8", "both env keys", read_env() == render_limit_env(8), f"env {read_env()}"))
            write_policy(repo, LIMIT_POLICY.format(n=6))
            run_fixture_git(repo, "commit", "-q", "-am", "a policy write of 6")
            checks.append(check_get("after 6", repo, ["--check"], lambda rc, o, e: rc == 1 and all(
                f"env.{v} is \"8\", {AGENTS_KEY} resolves 6" in o for v in policy.SETTINGS_VARS), kit=kit, verb="settings"))
            checks.append(check_get("after 6", repo, ["--write"], lambda rc, o, e: rc == 0, kit=kit, verb="settings"))
            checks.append(("after 6", "both env keys", read_env() == render_limit_env(6), f"env {read_env()}"))
            checks.append(check_get("after 6", repo, ["--check"], lambda rc, o, e: rc == 0, kit=kit, verb="settings"))
        elif name == "limit-hook-admits-eight":
            repo, kit, hook = build_limit_repo(t / "r", LIMIT_POLICY.format(n=8), "FANOUT_CAP=8\n")
            checks.append(check_get("at 8", repo, ["--write"], lambda rc, o, e: rc == 0, kit=kit, verb="settings"))
            spawn = write_handoff_fixture(repo)
            checks += [check_hook_call(name, "a handoff-valid Agent call", hook,
                                       {**render_spawn(repo, "u8"), "tool_input": spawn}, admits),
                       check_hook_call(name, "the registered harness", hook, {
                           "tool_name": "Workflow", "cwd": str(repo), "tool_input": {
                               "scriptPath": str(Path(repo, HARNESS_FILE)), "args": {"roles": {"r": "gov-researcher"}}}}, admits)]
        elif name == "limit-hook-six-spawns":
            repo, kit, hook = build_limit_repo(t / "r", LIMIT_POLICY.format(n=2))
            write_settings(repo, render_limit_env(2))
            checks += [check_hook_call(name, f"spawn {i} of one prompt", hook, render_spawn(repo, f"u{i}"), admits)
                       for i in range(1, 7)]
            ledger = Path(run_fixture_git(repo, "rev-parse", "--path-format=absolute", "--git-common-dir"), "agent-cap")
            checks.append((name, "no slot ledger under the git common dir", not ledger.exists(),
                           f"{ledger.as_posix()} {'exists' if ledger.exists() else 'is absent'}"))
        elif name == "limit-hook-rules-kept":
            repo, kit, hook = build_limit_repo(t / "r", LIMIT_POLICY.format(n=2))
            write_settings(repo, render_limit_env(2))
            checks += [
                check_hook_call(name, "a raw parallel over items.map", hook, render_workflow(
                    repo, "const items = [1, 2]\nconst r = await parallel(items.map((i) => () => i))\n"), admits),
                check_hook_call(name, "boundedParallel(thunks, 50)", hook, render_workflow(
                    repo, "const r = await boundedParallel(thunks, 50)\n"), admits),
                check_hook_call(name, "a verifier per finding", hook, render_workflow(
                    repo, "const v = await boundedParallel(all.map((f) => () => agent(f.claim)), 5)\n"),
                    has("MAX_VERIFIERS")),
                check_hook_call(name, "a ref-keyed verdict join", hook, render_workflow(
                    repo, "const m = new Map()\nm.set(f.ref, v)\n"), has("ref-keyed verdict join"))]
        elif name == "limit-hook-env-cap":
            repo, kit, hook = build_limit_repo(t / "r", LIMIT_POLICY.format(n=2))
            write_settings(repo, render_limit_env(2))
            checks.append(check_hook_call(name, "AGENT_CAP=50 over a clean script", hook, render_workflow(
                repo, "const r = await agent('one')\n"), admits, env={**os.environ, "AGENT_CAP": "50"}))
            top = (policy.run_git(KIT, "rev-parse", "--show-toplevel") or "").strip()
            tool_root = posixpath.dirname((policy.run_git(KIT, "rev-parse", "--show-prefix") or "").strip().rstrip("/")) or "."
            g = subprocess.run(["git", "-C", top, "grep", "-n", "-e", RETIRED_FLAG, "--", tool_root],
                               capture_output=True, text=True, encoding="utf-8", errors="replace")
            checks.append((name, "no file under the tool root asks the retired print mode",
                           g.returncode == 1 and not g.stdout.strip(),
                           f"git grep exit {g.returncode} · {g.stdout.strip()[:400] or '(nothing printed)'}"))
        elif name == "limit-hook-settings-over":
            repo, kit, hook = build_limit_repo(t / "r", LIMIT_POLICY.format(n=2))
            call = render_workflow(repo, "const r = await agent('one')\n")
            refused = has("CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS", "policy.py settings --write")
            for label, env, want in (("settings at 3", render_limit_env(3), refused), ("no env", None, refused),
                                     ("settings at 2", render_limit_env(2), admits)):
                write_settings(repo, env)
                checks.append(check_hook_call(label, "a Workflow call", hook, call, want))
            write_settings(repo, render_limit_env(3))
            remove_repo(kit)
            checks.append(check_hook_call("settings at 3, the policy kit absent", "a Workflow call", hook, call, admits))
        elif name == "limit-hook-landed-unread":
            # TOOL-dGroundRules-73: a default branch other than main with no remote HEAD refuses with its own
            # remedy, under rule 7's refused-read denial, never the settings remedy.
            repo, kit, hook = build_limit_repo(t / "r", LIMIT_POLICY.format(n=2))
            write_settings(repo, render_limit_env(2))
            run_fixture_git(repo, "branch", "-m", "master")
            call = render_workflow(repo, "const r = await agent('one')\n")
            unread = lambda *needles: lambda rc, err: has(*needles)(rc, err) and "settings --write" not in err  # noqa: E731
            checks += [
                check_hook_call("no remote, on master", "a Workflow call", hook, call, unread(
                    "rule 7", "the landed agent limit cannot be read", "refs/heads/main names no commit",
                    "export GOV_DEFAULT_BRANCH=<branch>")),
                check_hook_call("no remote, GOV_DEFAULT_BRANCH=master", "a Workflow call", hook, call, admits,
                                env={**os.environ, "GOV_DEFAULT_BRANCH": "master"})]
            bare = t / "o.git"
            bare.mkdir()
            run_fixture_git(bare, "init", "-q", "--bare")
            # the bare's HEAD names the branch pushed below, whatever this node's init.defaultBranch (TOOL-dGroundRules-80)
            run_fixture_git(bare, "symbolic-ref", "HEAD", "refs/heads/master")
            run_fixture_git(repo, "remote", "add", FIXTURE_REMOTE, bare.as_posix())
            run_fixture_git(repo, "push", "-q", FIXTURE_REMOTE, "master")
            checks.append(check_hook_call("one remote, no remote HEAD", "a Workflow call", hook, call, unread(
                f"refs/remotes/{FIXTURE_REMOTE}/main names no commit", f"git remote set-head {FIXTURE_REMOTE} -a")))
            run_fixture_git(repo, "remote", "set-head", FIXTURE_REMOTE, "-a")
            checks.append(check_hook_call("after remote set-head -a", "a Workflow call", hook, call, admits))
        elif name == "limit-hook-local-over":
            repo, kit, hook = build_limit_repo(t / "r", LIMIT_POLICY.format(n=2))
            write_settings(repo, render_limit_env(2))
            local = "/".join(SETTINGS_LOCAL)
            for var, call in ((policy.SETTINGS_VARS[0], render_spawn(repo, "u-local")),
                              (policy.SETTINGS_VARS[1], render_workflow(repo, "const r = await agent('one')\n"))):
                write_settings(repo, {var: "5"}, SETTINGS_LOCAL)
                checks.append(check_hook_call(f"{local} sets {var} to 5", f"a {call['tool_name']} call", hook, call,
                                              has(local, var)))
        elif name == "limit-hook-writer-split":
            # TOOL-dGroundRules-18: the build harness's template rendered at 6, its spec-writer split judged by
            # rule 2 against the landed limit; a verifier split at 6 against MAX_VERIFIERS whatever the limit;
            # and the writer split against MAX_VERIFIERS once no policy-mirror.js sits beside the hooks kit.
            wf = resolve_kit_dir("workflows", "unattended-build.template.js", KIT)
            render = (wf / "unattended-build.template.js").read_text(encoding="utf-8").replace("{{FANOUT_CAP}}", "6")
            scripts = ("--only=scripts",)
            for i, (n, script, what, want) in enumerate((
                    (6, render, "the render at 6 under a landed limit of 6", admits),
                    (4, render, "the render at 6 under a landed limit of 4",
                     has("gov:fixed-writers", "resolves to 6", f"above the bound 4: {AGENTS_KEY}")),
                    (6, VERIFIER_SPLIT, "a verifier split at 6 under a landed limit of 6",
                     has("gov:fixed-verifiers", "above the bound 5: MAX_VERIFIERS")))):
                repo, kit, hook = build_limit_repo(t / f"r{i}", LIMIT_POLICY.format(n=n))
                checks.append(check_hook_call(name, what, hook, render_workflow(repo, script), want, args=scripts, cwd=repo))
            (kit / "policy-mirror.js").unlink()
            checks.append(check_hook_call(name, "the render at 6, policy-mirror.js removed", hook, render_workflow(
                repo, render), has("gov:fixed-writers", "above the bound 5: MAX_VERIFIERS, as no policy kit"), args=scripts, cwd=repo))
        elif name == "limit-settings-elsewhere":
            # TOOL-dGroundRules-21 S34: GOV_SETTINGS_JSON names the settings in force, for the render and rule 7.
            repo, kit, hook = build_limit_repo(t / "r", LIMIT_POLICY.format(n=2))
            named = (t / "elsewhere" / "settings.json").as_posix()
            env = {**os.environ, "GOV_SETTINGS_JSON": named}
            read_env = lambda: json.loads(Path(named).read_text(encoding="utf-8")).get("env", {})  # noqa: E731
            call = render_workflow(repo, "const r = await agent('one')\n")
            # The named file exists, as a declared file must (TOOL-dGroundRules-25 S32), holding the old
            # value 3; a hard link to it is the reader that must never meet half a file (S33).
            Path(named).parent.mkdir()
            Path(named).write_text(json.dumps({"env": render_limit_env(3)}) + "\n", encoding="utf-8", newline="\n")
            link, old = t / "elsewhere-link.json", Path(named).read_bytes()
            os.link(named, link)
            checks.append(check_get("GOV_SETTINGS_JSON set", repo, ["--write"], lambda rc, o, e: rc == 0, env=env,
                                    kit=kit, verb="settings"))
            written = Path(named).is_file() and read_env() == render_limit_env(2)
            checks.append(("GOV_SETTINGS_JSON set", "the named file holds both keys, .claude/settings.json unwritten",
                           written and not Path(repo, *SETTINGS_FILE).exists(), f"named {'written' if written else 'NOT written'}"))
            # S33: the write is atomic by its effect, a new inode in place, never the old one rewritten.
            kept, moved = link.read_bytes() == old, os.stat(named).st_ino != os.stat(link).st_ino
            left = sorted(p.name for p in Path(named).parent.iterdir() if p.name != "settings.json")
            checks.append(("--write over a hard-linked file", "the link keeps the old bytes, the target is a new "
                           "inode, and no temporary file is left beside it", kept and moved and not left,
                           f"link {'kept' if kept else 'REWRITTEN'} · inode {'new' if moved else 'SAME'} · "
                           f"left beside it: {left or 'nothing'}"))
            checks += [check_hook_call("GOV_SETTINGS_JSON at 2", "a Workflow call", hook, call, admits, env=env),
                       check_hook_call("GOV_SETTINGS_JSON unset", "a Workflow call", hook, call,
                                       has("/".join(SETTINGS_FILE), "is absent"))]
            # TOOL-dGroundRules-61 S4: the project file planted at 2, so a pick of one value by precedence,
            # the declared file ranked lowest, would take the project's 2 and admit; every layer is bounded.
            write_settings(repo, render_limit_env(2))
            Path(named).write_text(json.dumps({"env": render_limit_env(3)}) + "\n", encoding="utf-8", newline="\n")
            checks.append(check_hook_call("GOV_SETTINGS_JSON at 3", "a Workflow call", hook, call,
                                          has(named, "above runtime.agents-in-flight 2"), env=env))
        elif name in ("limit-settings-elsewhere-project-over", "limit-settings-declared-absent"):
            # TOOL-dGroundRules-61 S1-S3: a declared file outside the checkout never hides the project's
            # layer, and a declaration that names no file refuses rather than reading as a layer setting nothing.
            repo, kit, hook = build_limit_repo(t / "r", LIMIT_POLICY.format(n=2))
            named = (t / "elsewhere" / "settings.json").as_posix()
            env = {**os.environ, "GOV_SETTINGS_JSON": named}
            call = render_workflow(repo, "const r = await agent('one')\n")
            var = policy.SETTINGS_VARS[1]
            if name == "limit-settings-elsewhere-project-over":
                Path(named).parent.mkdir()
                Path(named).write_text(json.dumps({"env": render_limit_env(2)}) + "\n", encoding="utf-8", newline="\n")
                write_settings(repo, {var: "2"})
                checks.append(check_hook_call("declared at 2, project at 2 (control)", "a Workflow call", hook, call,
                                              admits, env=env))
                write_settings(repo, {var: "3"})
                checks.append(check_hook_call(f"declared at 2, project {var} at 3", "a Workflow call", hook, call,
                                              has("/".join(SETTINGS_FILE), var, "above runtime.agents-in-flight 2"), env=env))
            else:
                write_settings(repo, render_limit_env(2))
                checks.append(check_hook_call("GOV_SETTINGS_JSON names no file, project at 2", "a Workflow call", hook,
                                              call, has(named, "not a file"), env=env))
        elif name == "limit-settings-env-stale":
            # TOOL-dGroundRules-25 S32: the landing's render names the tracked file, so an exported
            # GOV_SETTINGS_JSON naming a fresh scratch file cannot hide a stale tracked one from
            # `regen.py --check`; and a declared variable that is not a file refuses.
            repo, kit, hook = build_limit_repo(t / "r", LIMIT_POLICY.format(n=2))
            regen = resolve_kit_dir("run-gates", "regen.py", KIT) / "regen.py"
            dst = repo / (policy.run_git(regen.parent, "rev-parse", "--show-prefix") or "").strip() / "regen.py"
            dst.parent.mkdir(parents=True, exist_ok=True)
            for src, to in ((regen, dst), (KIT / "kit.toml", kit / "kit.toml")):
                to.write_bytes(src.read_bytes().replace(b"\r\n", b"\n"))
            write_settings(repo, render_limit_env(3))
            run_fixture_git(repo, "add", "-A")
            run_fixture_git(repo, "commit", "-q", "-m", "the regenerator, the descriptor and a stale settings file")
            scratch = t / "scratch-settings.json"
            scratch.write_text(json.dumps({"env": render_limit_env(2)}) + "\n", encoding="utf-8", newline="\n")
            rc, out = run_case_argv(repo, [sys.executable, dst.as_posix(), "--check"],
                                    env={"GOV_SETTINGS_JSON": scratch.as_posix()})
            checks.append(("GOV_SETTINGS_JSON at a fresh scratch file", "regen.py --check exits non-zero naming "
                           + "/".join(SETTINGS_FILE), rc != 0 and "/".join(SETTINGS_FILE) in out,
                           f"exit {rc} · {render_said(out, 'settings')}"))
            checks.append(check_get("GOV_SETTINGS_JSON names a directory", repo, ["--write"], lambda rc, o, e: rc == 2
                                    and "not a file" in e, env={**os.environ, "GOV_SETTINGS_JSON": t.as_posix()},
                                    kit=kit, verb="settings"))
        elif name == "limit-hook-settings-malformed":
            # TOOL-dGroundRules-21 S38: a settings file that does not parse, and a cwd in no checkout, refuse.
            repo, kit, hook = build_limit_repo(t / "r", LIMIT_POLICY.format(n=2))
            Path(repo, SETTINGS_FILE[0]).mkdir(exist_ok=True)
            Path(repo, *SETTINGS_FILE).write_text("{\n", encoding="utf-8", newline="\n")
            checks.append(check_hook_call("settings.json is `{`", "an Agent call", hook, render_spawn(repo, "u-bad"),
                                          has("/".join(SETTINGS_FILE), "does not parse as JSON")))
            (t / "outside").mkdir()
            checks.append(check_hook_call("a cwd in no checkout", "an Agent call", hook, render_spawn(t / "outside", "u-out"),
                                          has("rule 7", "in no git checkout")))
        elif name == "limit-hook-reader-throws":
            # TOOL-dGroundRules-21 S38: a reader that throws anything but a PolicyRefusal denies, naming the step.
            repo, kit, hook = build_limit_repo(t / "r", LIMIT_POLICY.format(n=2))
            write_settings(repo, render_limit_env(2))
            (kit / "policy-mirror.js").write_text(
                "class PolicyRefusal extends Error {}\n"
                "module.exports = { PolicyRefusal, readPolicy() { throw new TypeError('a planted throw') } }\n",
                encoding="utf-8", newline="\n")
            checks.append(check_hook_call(name, "an Agent call", hook, render_spawn(repo, "u-throw"),
                                          has("rule 7", "reading the landed limit", "a planted throw")))
        elif name == "limit-fresh-target-spawn":
            # TOOL-dGroundRules-21 S37: --scaffold renders the settings wherever HEAD resolves, so an adopter
            # spawns on install day without running the render by hand.
            repo, kit, hook = build_limit_repo(t / "r", None, mirror=False)
            (kit / "adopt-policy.sh").write_bytes((KIT / "adopt-policy.sh").read_bytes().replace(b"\r\n", b"\n"))
            rc, out = run_case_argv(repo, ["bash", (kit / "adopt-policy.sh").as_posix(), "--scaffold", "--target", repo.as_posix()])
            checks.append(("--scaffold over a committed target", "exit 0, the settings written", rc == 0
                           and Path(repo, *SETTINGS_FILE).is_file(), f"exit {rc} · {render_said(out, 'settings')}"))
            checks.append(check_hook_call(name, "the first Agent call", hook, render_spawn(repo, "u-first"), admits))
        else:
            checks.append((name, "a known limit case", False, "no such case"))
    except (subprocess.CalledProcessError, LookupError, policy.Refusal) as exc:
        checks.append((name, "the fixture", False, f"{type(exc).__name__}: {getattr(exc, 'stderr', '') or exc}"))
    finally:
        remove_repo(t)
    return print_checks(name, checks)


LIMIT_CASES = ("limit-conf-lowers", "limit-conf-no-raise", "limit-conf-malformed", "limit-conf-mirror",
               "limit-conf-last-valid", "limit-settings-render",
               "limit-hook-admits-eight", "limit-hook-six-spawns", "limit-hook-rules-kept", "limit-hook-env-cap",
               "limit-hook-settings-over", "limit-hook-landed-unread", "limit-hook-local-over", "limit-hook-writer-split",
               "limit-settings-elsewhere", "limit-hook-settings-malformed", "limit-hook-reader-throws",
               "limit-fresh-target-spawn", "limit-settings-env-stale",
               "limit-settings-elsewhere-project-over", "limit-settings-declared-absent")


# ---- the size caps' cases (TOOL-dGroundRules-9) --------------------------------------------------
#
# Every census enforcer runs from the SOURCE tree against a scratch repository on main with no remote,
# so local main is the landed revision the policy reader reads: the plant's files and a policy file at
# `warn` or `refuse`, committed. A copy-installed enforcer that finds the policy kit beside ITSELF runs
# as a copy beside a copy of the policy kit, at their source paths. Each value the plant measures is
# READ from the source, never typed: the limits file's row, the constant a shell or Python file sets.

BUDGET_POLICY = '[budgets]\nenforce = "{mode}"\n'
CAP_CASE_PREFIX = "budgets-cap-"
CASE_SPEC = "memory/builds/tOne/spec/2026-09-02-spec-TOOL-tOne-1.md"
CASE_SPEC_TEXT = ("# TOOL-tOne-1 — a unit\n\n**Status:** OPEN · rev-1 · 2026-09-02 · node t · Tier-1 · base 0123abcd · "
                  "streams tooling\n\n## 6. Acceptance criteria\n\n- **AC1** — `{pre}gate-legs.json` exists.\n\n"
                  "## 7. Gates\n\n`real leg`.\n\n")
HYGIENE_CONF = 'MEMORY_ROOT=memory\nDISCIPLINES="arch"\nFAMILIES="arch:ARCH"\n'
ROLES_CONF = "MEMORY_ROOT=memory\nCHARTER=AGENTS.md\n"
MANIFEST_REL = "memory/guides/SESSION-KICKOFF.md"
MANIFEST_TEXT = ("# Kickoff manifest — a case\n<!-- kickoff-manifest: v{fmt} · a case -->\n<!-- manifest-audit\n"
                 "last-audit: 2026-07-12T12:00:01+00:00 @ {sha}\nwatch: Makefile\nverify-paths: docs/GOV.md\n"
                 "last-body-change: {sha}\n-->\n## §A\n{skeleton}\n## §B\ngate fence:\n```bash\nmake all\n```\n{body}")
SHA_SHAPE = re.compile(r"\b[0-9a-f]{7,40}\b")


def derive_source_top():
    """The checkout this kit sits in, as git spells it: the tree every census enforcer runs from."""
    return Path((policy.run_git(KIT, "rev-parse", "--show-toplevel") or "").strip())


def derive_enforcer_rel(cap):
    """A census row's enforcer, its `{prefix}` resolved against this kit's tool root."""
    return budgets.resolve_prefix_token(cap.enforcer, budgets.derive_tool_root())


def derive_enforcer_path(cap):
    """A census row's enforcer in the source tree, absolute: the file a plant runs from there."""
    return (derive_source_top() / derive_enforcer_rel(cap)).as_posix()


def read_source_number(rel, key):
    """The integer the source file at `rel` assigns `key` where an assignment opens a line or follows a
    `;`: `KEY=n`, `KEY = n`, `KEY=${KEY:-n}`, `KEY="n"`, `n` with `_` separators read as one number."""
    text = (derive_source_top() / rel).read_text(encoding="utf-8")
    m = re.search(rf"(?:^|;)[ \t]*{re.escape(key)}[ \t]*=[ \t]*(?:\$\{{{re.escape(key)}:-)?\"?([0-9_]+)", text, re.M)
    if m is None:
        raise LookupError(f"{rel} assigns no number to {key}")
    return int(m[1].replace("_", ""))


def read_source_limits():
    """(the limits file's path, its text and its rows) in the source tree under test, its rows by the
    policy reader's own `parse_limits_rows`: a plant copies the text it measures against."""
    lrel = budgets.derive_limits_rel()
    text = policy.read_text_or_none(derive_source_top() / lrel) or ""
    return lrel, text.replace("\r\n", "\n"), budgets.parse_limits_rows(text)


def write_case_file(root, rel, text):
    Path(root, rel).parent.mkdir(parents=True, exist_ok=True)
    Path(root, rel).write_bytes(text if isinstance(text, bytes) else text.encode("utf-8"))


def build_cap_repo(t, files, mode, extra="", copies=(), post=None):
    """The case's repository at `t`, on main with no remote: each directory of `copies` copied from the
    source tree to its own path, CRLF folded, then `files` ({path: text}), then a policy file setting
    `budgets.enforce` to `mode` with `extra` below it, committed; `post(t)` then writes and commits."""
    top = derive_source_top()
    t.mkdir(parents=True, exist_ok=True)
    for rel in copies:
        shutil.copytree(top / rel, t / rel, ignore=shutil.ignore_patterns("__pycache__"), dirs_exist_ok=True)
        for f in (t / rel).rglob("*"):
            if f.is_file():
                f.write_bytes(f.read_bytes().replace(b"\r\n", b"\n"))
    for rel, text in files.items():
        write_case_file(t, rel, text)
    write_policy(t, BUDGET_POLICY.format(mode=mode) + extra)
    run_fixture_git(t, "init", "-q")
    run_fixture_git(t, "symbolic-ref", "HEAD", "refs/heads/main")
    run_fixture_git(t, "add", "-A")
    run_fixture_git(t, "commit", "-q", "-m", "the case's landed revision")
    if post is not None:
        post(t)
        run_fixture_git(t, "add", "-A")
        run_fixture_git(t, "commit", "-q", "--allow-empty", "-m", "the case's plant")
    return t


def render_said(out, mark):
    """The one line of `out` carrying `mark`, else its last line, cut at 300: an observation's line."""
    return next((ln for ln in out.splitlines() if mark and mark in ln), (out.strip().splitlines() or ["(no output)"])[-1])[:300]


def run_case_argv(cwd, argv, env=None, stdin=None):
    """-> (exit code, stdout and stderr with CR stripped); a `bash` argv[0] is `resolve_bash`'s, an
    `env` value of None drops that variable, and `stdin` is the text piped in."""
    if argv[0] == "bash":
        argv = [resolve_bash(Path(cwd, str(argv[1])).as_posix()) or "bash", *argv[1:]]
    merged = {**os.environ, **(env or {})}
    try:
        p = subprocess.run([str(a) for a in argv], cwd=cwd, capture_output=True, text=True, encoding="utf-8",
                           errors="replace", input=stdin, env={k: v for k, v in merged.items() if v is not None})
    except OSError as exc:
        return None, f"{argv[0]} did not run: {exc}"
    return p.returncode, (p.stdout + p.stderr).replace("\r", "")


def derive_template_size_plant(cap):
    """A subject at the row's key one byte over the row, the limits file at its source path."""
    lrel, text, rows = read_source_limits()
    v = int(rows[cap.name][0])
    return {"files": {lrel: text, cap.name: "x" * (v + 1)}, "argv": ["bash", derive_enforcer_path(cap), cap.name],
            "warn": f"BUDGET WARN — {cap.name} · {cap.name} · {v + 1} bytes over {v}",
            "refuse": "budgets.enforce is refuse"}


def derive_spec_class_plant(cap):
    """One live spec one byte over the class row, in the smallest tree the spec-token lint grades."""
    lrel, text, rows = read_source_limits()
    v = int(rows[cap.name][0])
    troot = budgets.derive_tool_root()
    pre = f"{troot}/" if troot else ""
    spec = CASE_SPEC_TEXT.format(pre=pre)
    spec += ("0" * 99 + "\n") * ((v + 1 - len(spec.encode("utf-8"))) // 100 + 1)
    return {"files": {f"{pre}gate-legs.json": '[{"name":"real leg"}]\n', f"{pre}gate.sh": "#!/bin/sh\n",
                      "memory/project/spec-token-waivers.txt": "# waivers\n", lrel: text, CASE_SPEC: spec},
            "argv": [sys.executable, derive_enforcer_path(cap)],
            "warn": f"BUDGET WARN — {cap.name} · {CASE_SPEC} ·", "refuse": f"size <- {CASE_SPEC}"}


def derive_line_length_plant(cap):
    """A subject with one line a character past the gate's hard default, the family's value."""
    rel = derive_enforcer_rel(cap)
    v = read_source_number(rel, "HARD_DEFAULT")
    return {"files": {"subject.md": "y" * (v + 1) + "\n"}, "argv": ["bash", derive_enforcer_path(cap), "subject.md"],
            "warn": f"BUDGET WARN — line-length · subject.md · {v + 1} chars over {v}",
            "refuse": "budgets.enforce is refuse"}


def derive_hygiene_plant(cap):
    """One memory file over one of check 6's or 7's caps, the value the engine declares for the
    cap's conf key; a cap the engine leaves at 0, unchecked, takes 10 from the policy file."""
    rel = derive_enforcer_rel(cap)
    v, extra = read_source_number(rel, cap.home.rpartition(":")[2]), ""
    if v == 0:
        v, extra = 10, f'"{cap.name}" = 10\n'
    kind, axis = cap.name.rsplit("-", 1)
    files = {".memory-tree.conf": HYGIENE_CONF, "memory/backlog/ARCH.md": "# ARCH\n"}
    path, head, width = {"guide": ("memory/guides/g.md", "", 199), "index": ("memory/backlog/ARCH.md", "# ARCH\n", 250),
                         "entry": ("memory/backlog/ARCH.md", "# ARCH\n", 0), "dossier": ("memory/map/features/d.md", "", 120),
                         "readme": ("memory/builds/bOne/README.md", "", 300),
                         "readme-entry": ("memory/builds/bOne/README.md", "", 0)}[kind]
    if kind == "dossier":
        files[".codebase-map.conf"] = "MAP_ROOT=memory/map\n"
    body = {"bytes": ("x" * width + "\n") * (v // (width + 1) + 1), "lines": "x\n" * (v + 1), "chars": "x" * (v + 1) + "\n"}
    files[path] = head + body[axis]
    return {"files": files, "extra": extra, "argv": ["bash", derive_enforcer_path(cap), "--only", "6,7"],
            "warn": f"BUDGET WARN — {cap.name} ·", "refuse": "budgets.enforce is refuse"}


def derive_readme_slot_plant(cap):
    """A bound build README whose first canonical slot is one byte over its declared ceiling, the
    canon and the ceilings read from the declaration the census names."""
    rel = derive_enforcer_rel(cap)
    decl = budgets.resolve_prefix_token(cap.home.split(":", 1)[1].rpartition(":")[0], budgets.derive_tool_root())
    heads = [tuple(ln.split("\t", 1)) for ln in (derive_source_top() / decl).read_text(encoding="utf-8").splitlines()
             if ln.startswith("## ") and "\t" in ln]
    v = int(heads[0][1])
    bodies = ["x" * (v + 1), "- one", "- one"] + [""] * len(heads)
    slots = "".join(f"{h}\n\n{b}\n\n" if b else f"{h}\n\n" for (h, _v), b in zip(heads, bodies))
    readme = ("---\nslug: tOne\nnode: t\nopened: 2026-01-01\nstreams: s\nroster: ARCH\nids: ARCH-tOne-1\n---\n\n# tOne\n\n"
              f"{slots}<!-- roster:units -->\n| # | Unit |\n<!-- /roster:units -->\n\n<!-- gen:build-index -->\n"
              "<!-- /gen:build-index -->\n")
    readme_rel = "memory/builds/tOne/README.md"
    return {"files": {".memory-tree.conf": "MEMORY_ROOT=memory\n", readme_rel: readme,
                      "memory/project/readme-contract.txt": f"exempt-pin: 0\n{readme_rel}\n"},
            "argv": [sys.executable, derive_enforcer_path(cap), "--check-format"],
            "warn": f"BUDGET WARN — readme-slot · {readme_rel} `{heads[0][0]}` · {v + 1} bytes over {v}",
            "refuse": "over its declared ceiling"}


def derive_role_body_plant(cap):
    """The roles kit and the policy kit copied in, and one role body 5000 bytes longer, past every
    slot's ceiling."""
    rel = derive_enforcer_rel(cap)
    roles = posixpath.dirname(rel)
    agent = sorted((derive_source_top() / roles / "agents").glob("*.agent.md"))[0]
    text = agent.read_text(encoding="utf-8").replace("\r\n", "\n") + "\n" + "x" * 5000 + "\n"
    return {"files": {".memory-tree.conf": ROLES_CONF, "AGENTS.md": (derive_source_top() / "AGENTS.md").read_bytes(),
                      f"{roles}/agents/{agent.name}": text},
            "copies": (roles, budgets.derive_kit_rel().rstrip("/")), "argv": [sys.executable, rel],
            "warn": "BUDGET WARN — role-body ·", "refuse": "-byte ceiling (budgets.enforce is refuse)"}


def derive_one_line_rule_plant(cap):
    """A copy of the render engine beside a copy of the policy kit, a template whose one-line region
    holds a rule one character past the engine's cap, and the smallest descriptor and registry."""
    rel = derive_enforcer_rel(cap)
    v = read_source_number(rel, "ONE_LINE_MAX")
    eng = posixpath.dirname(rel)
    return {"files": {rel: (derive_source_top() / rel).read_bytes(), f"{eng}/playbook.kit.toml": "",
                      f"{eng}/registry.toml": '[[entry]]\nid = "lexicon"\n',
                      ".governance/deploy.toml": 'kits = ["lexicon"]\n\n[answers]\nplaybook_path = "CHARTER.md"\n',
                      "CHARTER.md": f"<!-- one-line -->\n- {'x' * v}\n<!-- /one-line -->\nend\n"},
            "copies": (budgets.derive_kit_rel().rstrip("/"),), "argv": [sys.executable, rel, "--target", "{repo}"],
            "warn": "BUDGET WARN — one-line-rule", "refuse": f"past the {v} a one-line rule may take"}


def derive_roster_line_plant(cap):
    """The roles kit and the policy kit copied in, and the first role's description lengthened past
    the roster cap."""
    rel = derive_enforcer_rel(cap)
    v = read_source_number(rel, "ROSTER_LINE_MAX")
    roles = posixpath.dirname(rel)
    agent = sorted((derive_source_top() / roles / "agents").glob("*.agent.md"))[0]
    text = re.sub(r"^(description: .*)\.$", lambda m: m[1] + "x" * v + ".",
                  agent.read_text(encoding="utf-8").replace("\r\n", "\n"), count=1, flags=re.M)
    return {"files": {".memory-tree.conf": ROLES_CONF, f"{roles}/agents/{agent.name}": text},
            "copies": (roles, budgets.derive_kit_rel().rstrip("/")), "argv": [sys.executable, rel, "roster"],
            "warn": f"BUDGET WARN — roster-line · {agent.name[:-len('.agent.md')]}",
            "refuse": "(budgets.enforce is refuse)"}


def derive_manifest_plant(cap, kit=True, body=None, env=None, argv_tail=()):
    """A kickoff manifest over its cap, stamped at the base commit, in a repository whose policy kit is
    TRACKED, as the checker's last rung finds it; `kit` False holds none. `body` replaces the plant."""
    rel = derive_enforcer_rel(cap)
    key = {"manifest-bytes": "MAX_MANIFEST_BYTES", "manifest-line": "MANIFEST_LINE_MAX",
           "manifest-trap": "MANIFEST_TRAP_MAX"}.get(cap.name)
    v = read_source_number(rel, key) if key else 0
    plants = {"manifest-bytes": ("y" * 99 + "\n") * (v // 100 + 1), "manifest-line": "y" * (v + 1) + "\n",
              "manifest-trap": ("\n### Environment traps worth front-loading\n\n- " + "y" * 98 + "\n"
                                + ("  " + "y" * 98 + "\n") * (v // 100 + 1))}
    fmt = re.search(r'^MANIFEST_FORMAT="([0-9.]+)"', (derive_source_top() / rel).read_text(encoding="utf-8"), re.M)[1]
    skeleton = run_case_argv(derive_source_top(), ["bash", rel, "--task-skeleton"])[1].rstrip("\n")

    def write_manifest(t):
        sha = run_fixture_git(t, "rev-parse", "HEAD")
        write_case_file(t, MANIFEST_REL, MANIFEST_TEXT.format(fmt=fmt, sha=sha, skeleton=skeleton,
                                                               body=plants.get(cap.name, "") if body is None else body))
    return {"files": {"Makefile": "all:\n\ttrue\n", "docs/GOV.md": "gov\n"}, "post": write_manifest, "env": env,
            "copies": (budgets.derive_kit_rel().rstrip("/"),) if kit else (),
            "argv": ["bash", derive_enforcer_path(cap), *argv_tail],
            "warn": f"BUDGET WARN — {cap.name} ·", "refuse": "budgets.enforce is refuse"}


def derive_universal_plant(cap):
    """Two universal class records against the conf's UNIVERSAL_BUDGET of 1, the catalogue's index
    written and committed."""
    rel = derive_enforcer_rel(cap)
    uni = "---\nname: {n}\ndescription: d\nuniversal: true\n---\n\nEverywhere. No machine gate.\n"
    return {"files": {".memory-tree.conf": HYGIENE_CONF + 'UNIVERSAL_BUDGET="1"\n', "memory/HYGIENE.md": "sentinel\n",
                      "memory/README.md": "# r\n", "memory/DECISIONS.md": "# d\n",
                      "memory/gotchas/u1.md": uni.format(n="u1"), "memory/gotchas/u2.md": uni.format(n="u2")},
            "post": lambda t: run_case_argv(t, [sys.executable, derive_source_top() / rel, "--write"]),
            "argv": [sys.executable, derive_enforcer_path(cap), "--check"],
            "warn": "BUDGET WARN — universal-gotchas", "refuse": "against a budget of 1"}


def derive_recall_export_plant(cap):
    """The recall kit and the policy kit copied in, so the kit's repository is the case's, and a query
    log of one query a day, long enough that its export passes the cap."""
    rel = derive_enforcer_rel(cap)
    v = read_source_number(rel, "EXPORT_CAP")

    def write_query_log(t):
        log = Path(run_fixture_git(t, "rev-parse", "--path-format=absolute", "--git-common-dir"), "recall", "queries.jsonl")
        log.parent.mkdir(parents=True, exist_ok=True)
        log.write_text("".join(json.dumps({"qid": i + 1, "type": "query", "at": f"{2000 + i // 336:04d}-{i % 336 // 28 + 1:02d}-"
                                           f"{i % 28 + 1:02d}T00:00:00Z", "n_hits": 1, "results": []}) + "\n"
                               for i in range(v // 25)), encoding="utf-8", newline="\n")
    return {"files": {".memory-tree.conf": HYGIENE_CONF, "memory/README.md": "# r\n"}, "post": write_query_log,
            "copies": (posixpath.dirname(rel), budgets.derive_kit_rel().rstrip("/")),
            "argv": [sys.executable, rel, "--export", "--tag", "z"],
            "warn": "BUDGET WARN — recall-export", "refuse": "over the"}


def derive_outside_probe_plant(cap):
    """An outside row's enforcer run under each value, breaching its cap where it has a CLI to reach
    it: the orientation card at a 1-byte cap, Codex's canonical one byte over CODEX_MAX, a charter
    citing a file under no cap, and a subagent route longer than the hook's context cap. A library
    with no CLI, the runlog record's and the feature card's, is imported and its constant printed:
    that run cannot breach, so the arm that holds it outside the switch is `arm_cap_census`'s join,
    and the reader's refusal this case asserts beside it."""
    rel = derive_enforcer_rel(cap)
    key = cap.home.rpartition(":")[2]
    if cap.name == "orientation-card":
        return derive_manifest_plant(cap, body="", env={key: "1"}, argv_tail=(
            "--card", "--write", "--session", "00000000-0000-4000-8000-000000000000")) | {"warn": "over the 1-byte cap"}
    src = derive_enforcer_path(cap)
    if cap.name == "cited-file-cap":  # a waiver list, no number: a charter cites a file no cap covers
        return {"files": {".memory-tree.conf": HYGIENE_CONF + "CHARTER=AGENTS.md\n", "memory/README.md": "# r\n",
                          "AGENTS.md": "# Charter\n\nRead `memory/HYGIENE.md` first.\n", "memory/HYGIENE.md": "# Hygiene\n"},
                "argv": [sys.executable, src, "--check"], "warn": "under no byte cap"}
    v = read_source_number(rel, f"const {key}" if rel.endswith(".js") else key)
    if cap.name == "codex-instructions":
        return {"files": {"AGENTS.md": "x" * v + "\n"}, "argv": ["bash", src], "warn": f"over {v}"}
    if rel.endswith(".js"):  # the subagent context: a routed card of more route lines than the cap holds

        def write_card(t):
            card = Path(run_fixture_git(t, "rev-parse", "--path-format=absolute", "--git-common-dir"), "orientation", "case.md")
            card.parent.mkdir(parents=True, exist_ok=True)
            card.write_text("## route\n- build: bX\n" + "".join(
                f"- unit: TOOL-bX-{i} · spec memory/builds/bX/spec/2026-01-01-spec-TOOL-bX-{i}.md\n"
                for i in range(v // 50)), encoding="utf-8", newline="\n")
        return {"files": {".memory-tree.conf": 'MEMORY_ROOT=memory\nROUTED_PATHS="tools/"\n'}, "post": write_card,
                "argv": ["node", src], "env": {"CLAUDE_PROJECT_DIR": None},
                "stdin": json.dumps({"hook_event_name": "SubagentStart", "session_id": "case", "cwd": "{repo}"}),
                "warn": f"capped at {v} characters"}
    mod = Path(rel).stem
    return {"files": {}, "argv": [sys.executable, "-B", "-c", f"import sys; sys.path.insert(0, {posixpath.dirname(src)!r}); "
                                  f"import {mod}; print({mod}.{key})"], "warn": str(v)}


def derive_zero_plant(cap, p):
    """`p`, a census row's plant, with the row's value at 0 in the policy file and none in its legacy
    home, so the reader answers 0 from the file: a `limits:` row's line left out of the limits file the
    plant writes, a `conf:` key's assignment left out of that conf, a `constant:` home untouched."""
    form, _c, rest = cap.home.partition(":")
    files = dict(p["files"])
    if form == "limits":
        lrel = budgets.derive_limits_rel()
        files[lrel] = "".join(ln for ln in files[lrel].splitlines(True) if not ln.startswith(cap.name + "\t"))
    elif form == "conf":
        path, _c, key = rest.rpartition(":")
        rx = re.compile(budgets.SHELL_KEY.format(re.escape(key)))
        if path in files:
            files[path] = "".join(ln for ln in files[path].splitlines(True) if not rx.match(ln))
    return {**p, "files": files, "extra": f'"{cap.name}" = 0\n'}


# The census row -> its plant. DECLARED, never derived from the census, so `arm_cap_census` reads a
# census row with no case, and a case with no row, as the defects they are.
CAP_CASES = {
    "coding-governance-agents.template.md": derive_template_size_plant, "AGENTS.md": derive_template_size_plant,
    "skills/session-kickoff/SKILL.md": derive_template_size_plant, "memory/guides/BUILD-METHOD.md": derive_template_size_plant,
    "memory/guides/UNATTENDED-PROTOCOL.md": derive_template_size_plant, ".claude/skills/unattended/SKILL.md": derive_template_size_plant,
    "memory/builds/*/spec/": derive_spec_class_plant, "line-length": derive_line_length_plant,
    "guide-bytes": derive_hygiene_plant, "guide-lines": derive_hygiene_plant, "index-bytes": derive_hygiene_plant, "index-lines": derive_hygiene_plant,
    "readme-bytes": derive_hygiene_plant, "readme-lines": derive_hygiene_plant, "dossier-bytes": derive_hygiene_plant,
    "dossier-lines": derive_hygiene_plant, "entry-chars": derive_hygiene_plant, "readme-entry-chars": derive_hygiene_plant,
    "readme-slot": derive_readme_slot_plant, "role-body": derive_role_body_plant, "one-line-rule": derive_one_line_rule_plant,
    "roster-line": derive_roster_line_plant, "manifest-bytes": derive_manifest_plant, "manifest-line": derive_manifest_plant,
    "manifest-trap": derive_manifest_plant, "universal-gotchas": derive_universal_plant, "recall-export": derive_recall_export_plant,
    "orientation-card": derive_outside_probe_plant, "cited-file-cap": derive_outside_probe_plant,
    "codex-instructions": derive_outside_probe_plant, "runlog-record": derive_outside_probe_plant,
    "feature-card": derive_outside_probe_plant, "hook-context": derive_outside_probe_plant,
}


def run_cap_plant(t, cap, plant, mode, extra=""):
    """One plant built at `t` under `mode` and its enforcer run there -> (exit code, output, plant)."""
    p = plant(cap)
    repo = build_cap_repo(t, p["files"], mode, p.get("extra", "") + extra, p.get("copies", ()), p.get("post"))
    stdin = p["stdin"].replace("{repo}", repo.as_posix()) if p.get("stdin") else None
    rc, out = run_case_argv(repo, [str(a).replace("{repo}", repo.as_posix()) for a in p["argv"]], p.get("env"), stdin)
    return rc, out, p


def run_cap_mode(t, cap, plant, mode):
    """One mode of a census case at `t`: -> (exit code, output, plant) or the exception the plant
    raised, the repository removed either way."""
    try:
        return run_cap_plant(t, cap, plant, mode)
    except (subprocess.CalledProcessError, OSError, LookupError, KeyError, policy.Refusal) as exc:
        return exc
    finally:
        if t.exists():
            remove_repo(t)


def run_cap_case(name):
    """`budgets-cap-<name>` (AC5, AC6): the census row's plant built twice, at `warn` and at `refuse`,
    in fresh repositories, and its enforcer run. A `switch` row must exit 0 printing its BUDGET WARN
    line under `warn` and refuse naming `budgets.enforce` under `refuse`; a `switch` row that is not a
    family runs a third mode, `zero` (TOOL-dGroundRules-75): `derive_zero_plant` under `refuse`, which
    must exit 0 with no breach line and no awk error, a 0 read as unchecked; its modes run at once,
    each at its own path. An outside row must print the same exit and output under both, its marker in
    it, so its two modes run in turn at ONE path; and the policy reader must refuse to answer it."""
    cap_name = name[len(CAP_CASE_PREFIX):]
    checks, seen = [], {}
    try:
        cap = budgets.read_cap_census(derive_source_top()).get(cap_name)
    except policy.Refusal as exc:
        return print_checks(name, [(name, "the cap census", False, str(exc))])
    plant = CAP_CASES.get(cap_name)
    if cap is None or plant is None:
        return print_checks(name, [(name, "a census row and its plant", False,
                                    f"census row {'found' if cap else 'absent'} · plant {'found' if plant else 'absent'}")])
    t = Path(tempfile.mkdtemp(prefix="pol-"))
    try:
        if cap.cls == "switch":
            import concurrent.futures
            # A family takes no policy value, so it has no zero run.
            modes = ("warn", "refuse") if cap.family else ("warn", "refuse", "zero")

            def run_mode(m):
                if m == "zero":
                    return run_cap_mode(t / m, cap, lambda c: derive_zero_plant(c, plant(c)), "refuse")
                return run_cap_mode(t / m, cap, plant, m)
            with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
                runs = dict(zip(modes, pool.map(run_mode, modes)))
        else:
            runs = {m: run_cap_mode(t / "r", cap, plant, m) for m in ("warn", "refuse")}
        for mode, got in runs.items():
            if isinstance(got, Exception):
                checks.append((mode, "the plant", False, f"{type(got).__name__}: {getattr(got, 'stderr', '') or got}"))
                continue
            rc, out, p = got
            seen[mode] = (rc, SHA_SHAPE.sub("<sha>", out))
            mark = p["refuse" if mode in ("refuse", "zero") and cap.cls == "switch" else "warn"]
            said = render_said(out, mark)
            if mode == "zero":
                checks.append(("zero", "a value of 0 under refuse: exit 0, no breach line, no awk error",
                               rc == 0 and mark not in out and "BUDGET WARN" not in out and "awk:" not in out,
                               f"exit {rc} · {said}"))
            elif cap.cls == "switch":
                ok = (rc == 0) if mode == "warn" else (rc not in (0, None))
                checks.append((mode, f"exit {'0' if mode == 'warn' else 'non-zero'} and {mark!r}", ok and mark in out,
                               f"exit {rc} · {said}"))
            else:
                checks.append((mode, f"the outside enforcer ran, {mark!r} in its output", rc is not None and mark in out,
                               f"exit {rc} · {said}"))
        if cap.cls != "switch":
            same = len(seen) == 2 and seen["warn"] == seen["refuse"]
            checks.append(("warn and refuse", "the same exit and output", same,
                           "identical" if same else f"warn {seen.get('warn')!r:.300} · refuse {seen.get('refuse')!r:.300}"))
            try:
                budgets.resolve_caps([cap.name], str(derive_source_top()))
                checks.append(("reader", "budgets.resolve_caps refuses an outside cap", False, "it answered"))
            except policy.Refusal as exc:
                checks.append(("reader", "budgets.resolve_caps refuses an outside cap", "outside the switch" in exc.why, str(exc)))
    finally:
        remove_repo(t)
    return print_checks(name, checks)


def seed_budget_pin(cap_name, needle, row=None):
    """A plant of `budgets.pinned` naming `cap_name`, with `row` appended to the kit copy's census."""
    def seed(repo, kit, rows):
        if row:
            write_edit(kit / budgets.CENSUS, lambda t: t + row)
        write_edit(Path(repo, *POLICY_FILE), lambda t: t.replace("pinned = []", f'pinned = ["{cap_name}"]'))
        return "budgets.pinned", needle
    return seed


def seed_family_value(repo, kit, rows):
    write_edit(Path(repo, *POLICY_FILE), lambda t: t.replace("pinned = []", "pinned = []\nrole-body = 9000"))
    return "budgets.role-body", "role-body is a family cap"


# A planted row whose enforcer no install holds, so `ships = false` and no `kit` or `installed`.
EXEMPT_ROW = ('\n[[cap]]\nname = "zz-exempt"\nclass = "exempt"\nunit = "bytes"\nenforcer = "{prefix}/zz.sh"\n'
              'home = "constant:{prefix}/zz.sh:ZZ"\nfamily = false\nresearch = 0\nships = false\n')
# AC1's four plants on the policy file, each graded by `arm_schema` through `validate`.
BUDGET_SCHEMA_SEEDS = {
    "budgets-pinned-outside": seed_budget_pin("codex-instructions", "codex-instructions is consumer, outside the switch"),
    "budgets-pinned-exempt": seed_budget_pin("zz-exempt", "zz-exempt is exempt, outside the switch", EXEMPT_ROW),
    "budgets-pinned-unknown": seed_budget_pin("no-such-cap", "no-such-cap names no row of the cap census"),
    "budgets-family-value": seed_family_value,
}


def seed_ambiguous_registry(repo, kit, rows):
    """`census-ambiguous-registry` (TOOL-dGroundRules-34 S13): two deployer registries in a receipt-less
    repository, `<d>` one deep (this kit's tool root) and two deep (RELOCATED_PREFIX's), both inside the
    window `derive_census_tree` searches, so the tree is never guessed to be gov's at either."""
    found = sorted(posixpath.join(d, REGISTRY_REL) for d in
                   (budgets.derive_tool_root(), posixpath.dirname(RELOCATED_PREFIX.rstrip("/"))))
    for rel in found:
        write_case_file(repo, rel, "")
    return ", ".join(found), f"{len(found)} {REGISTRY_REL} candidates"


def run_budget_case(name):
    """The named outcome cases of the size switch (AC2, AC3, AC4, AC7, AC9, AC10, AC11), each over its
    own repositories under one temp root, printing one line per observation."""
    top, checks = derive_source_top(), []
    t = Path(tempfile.mkdtemp(prefix="pol-"))
    try:
        census = budgets.read_cap_census(top)
        lrel, ltext, lrows = read_source_limits()
        no_agents = "".join(ln for ln in ltext.splitlines(True) if not ln.startswith("AGENTS.md\t"))
        bud = [sys.executable, KIT / "budgets.py"]
        if name == "budgets-pinned-warn":
            rc, out, _p = run_cap_plant(t / "pin", census["AGENTS.md"], derive_template_size_plant, "warn", 'pinned = ["AGENTS.md"]\n')
            checks.append(("pinned under warn", "exit 1 naming budgets.pinned", rc == 1 and "budgets.pinned" in out,
                           f"exit {rc} · {render_said(out, 'budgets.pinned')}"))
            rc, out, _p = run_cap_plant(t / "free", census["AGENTS.md"], derive_template_size_plant, "warn")
            checks.append(("unpinned under warn", "exit 0 printing BUDGET WARN", rc == 0 and "BUDGET WARN" in out,
                           f"exit {rc} · {render_said(out, 'BUDGET WARN')}"))
        elif name == "budgets-two-homes":
            line = lrows["AGENTS.md"][1]
            r = build_cap_repo(t / "both", {lrel: ltext}, "warn", '"AGENTS.md" = 30000\n')
            rc, out = run_case_argv(r, [*bud, "resolve", "AGENTS.md"])
            want = f"policy: refused · {lrel}:{line} · budgets.AGENTS.md is held in both homes"
            checks.append(("row and key", "exit 2 naming both homes", rc == 2 and out.strip() == want, f"exit {rc} · {out.strip()}"))
            r = build_cap_repo(t / "key", {lrel: no_agents}, "warn", '"AGENTS.md" = 30000\n')
            rc, out = run_case_argv(r, [*bud, "resolve", "AGENTS.md"])
            checks.append(("key alone", "30000 with source file", rc == 0 and out.strip() == "AGENTS.md\t30000\twarn\tfile", f"exit {rc} · {out.strip()!r}"))
        elif name == "budgets-limits-reader":
            r = build_cap_repo(t / "r", {lrel: no_agents, "hooks/consumer.sh": "#!/bin/sh\necho reads no cap\n"},
                               "warn", '"AGENTS.md" = 20480\n')
            _n, _pop, found = ARM["arm_limits_readers"].run(r, KIT)
            checks.append(("unplanted", "arm_limits_readers green", not found, f"{found or 'no finding'}"))
            write_case_file(r, "scripts/reader.sh", f"#!/bin/sh\ncat {lrel}\n")
            run_fixture_git(r, "add", "scripts/reader.sh")
            _n, _pop, found = ARM["arm_limits_readers"].run(r, KIT)
            checks.append(("a script reading the limits file", "red naming it", [k for k, _w in found] == ["scripts/reader.sh"], f"{found}"))
        elif name == "budgets-census-join":
            enforcers = {derive_enforcer_rel(c): (top / derive_enforcer_rel(c)).read_bytes() for c in census.values()}
            reg = posixpath.join(budgets.derive_tool_root(), REGISTRY_REL)  # the repository stands for gov's tree
            r = build_cap_repo(t / "r", {**enforcers, lrel: ltext, reg: (top / reg).read_bytes()}, "warn",
                               copies=(budgets.derive_kit_rel().rstrip("/"),))
            _n, _pop, found = arm_cap_census(r, KIT)
            checks.append(("the census's enforcers copied whole", "arm_cap_census green", not found, f"{found or 'no finding'}"))
            ll = derive_enforcer_rel(census["line-length"])
            write_case_file(r, ll, enforcers[ll] + b'\n"$PY_BIN" "$pk/budgets.py" resolve no-such-cap\n')
            _n, _pop, found = arm_cap_census(r, KIT)
            checks.append(("a request for no-such-cap", "red naming it", any(k == "no-such-cap" for k, _w in found), f"{found}"))
            write_case_file(r, ll, enforcers[ll])
            kit_census = Path(r, budgets.derive_kit_rel(), budgets.CENSUS)
            write_edit(kit_census, lambda x: x + EXEMPT_ROW.replace("zz-exempt", "zz-planted"))
            _n, _pop, found = arm_cap_census(r, KIT)
            checks.append(("a census row with no case", "red naming it", any(k == "zz-planted" and "case" in w for k, w in found), f"{found}"))
        elif name == "budgets-switch-refuse":
            for mode, want in (("refuse", 1), ("warn", 0)):
                r = build_cap_repo(t / mode, {lrel: ltext}, mode)
                rc, out = run_case_argv(r, [*bud, "check", "AGENTS.md", "999999"])
                checks.append((f"enforce = {mode}", f"exit {want} naming budgets.enforce", rc == want and "budgets.enforce" in out, f"exit {rc} · {out.strip()}"))
        elif name == "budgets-unset-derived":
            # TOOL-dGroundRules-62 S4: the unset cap's derived default is no file value, under the last valid
            # revision too, while a file that does not parse with none before it still refuses. (a) one
            # unparsed commit; (b) V warn pinning the cap, then C unparsed; (c) V warn, no pin, then C.
            v = lrows["AGENTS.md"][0]
            unparsed = lambda r: write_policy(r, '[budgets]\nenforce = refuse\n')
            for repo, extra, post, mode, rule, told in (
                    ("a", "enforce = refuse\n", None, "refuse", budgets.READER_REFUSED, 1),
                    ("b", 'pinned = ["AGENTS.md"]\n', unparsed, "refuse", "budgets.pinned names it", 0),
                    ("c", "", unparsed, "warn", "budgets.enforce is warn", 0)):
                r = build_cap_repo(t / repo, {lrel: ltext}, "warn", extra, post=post)
                rc, out = run_case_argv(r, [*bud, "resolve", "--explain", "AGENTS.md"])
                row, said = f"AGENTS.md\t{v}\t{mode}\tdefault", out.count("policy: refused")
                checks.append((f"repository ({repo})", f"{row!r}, the rule {rule!r}, {told} refusal line(s)",
                               rc == 0 and row in out.splitlines() and f" · {rule} · " in out and said == told,
                               f"exit {rc} · said {said} time(s) · {render_said(out, 'budgets: AGENTS.md')}"))
        elif name == "budgets-no-kit":
            rc, out, _p = run_cap_plant(t / "r", census["manifest-bytes"], lambda c: derive_manifest_plant(c, kit=False), "refuse")
            told = out.count("no policy kit is installed")
            checks.append(("no policy kit", "check 7 refuses and the absence is said once",
                           rc == 1 and "MANIFEST check 7 FAILED" in out and told == 1,
                           f"exit {rc} · said {told} time(s) · {render_said(out, 'check 7 FAILED')}"))
        elif name == "budgets-zero-cap":
            # TOOL-dGroundRules-21 S28: a cap of 0 is valid, and unchecked, as its census home holds 0 today.
            cap = census["index-lines"]
            p = derive_hygiene_plant(cap)
            r = build_cap_repo(t / "r", p["files"], "refuse", f'"{cap.name}" = 0\n')
            rc, out = run_case_argv(r, [sys.executable, KIT / "policy.py", "check"])
            checks.append((f'"{cap.name}" = 0', "policy.py check exit 0, the file valid", rc == 0 and " is valid" in out,
                           f"exit {rc} · {out.strip()}"))
            rc, out = run_case_argv(r, p["argv"])
            checks.append((f'"{cap.name}" = 0, an index over every other value, under refuse', "the enforcer exits 0",
                           rc == 0 and "check 6 FAILED" not in out and "check 7 FAILED" not in out,
                           f"exit {rc} · {render_said(out, 'FAILED')}"))
            # The control: the same index under a value it is over refuses, so the 0 above is what passed it.
            r = build_cap_repo(t / "control", p["files"], "refuse", f'"{cap.name}" = 10\n')
            rc, out = run_case_argv(r, p["argv"])
            checks.append((f'"{cap.name}" = 10, the same index, under refuse', "the enforcer refuses",
                           rc not in (0, None), f"exit {rc} · {render_said(out, 'FAILED')}"))
        elif name == "budgets-reader-refused":
            # TOOL-dGroundRules-21 S31: a reader that refuses gives the cap `refuse`, never `warn`, and the
            # refusal prints once; with no launcher the enforcer takes its no-kit branch and says why.
            cap = census["AGENTS.md"]
            subject = "x" * 49153  # over the handed-in default, the value a refused landed read leaves
            r = build_cap_repo(t / "two", {lrel: ltext, cap.name: subject}, "warn")
            for remote in ("a", "b"):
                run_fixture_git(r, "remote", "add", remote, r.as_posix())
            rc, out = run_case_argv(r, ["bash", derive_enforcer_path(cap), cap.name])
            told = out.count("Name it: export GOV_REMOTE=<remote>.")
            checks.append(("two remotes, no GOV_REMOTE, under warn", "refused, the ladder's refusal said once",
                           rc not in (0, None) and told == 1 and "BUDGET WARN" not in out,
                           f"exit {rc} · said {told} time(s) · {render_said(out, 'FAILED')}"))
            stubs = t / "stubs"
            for launcher in ("python3", "python", "py"):
                write_case_file(stubs, launcher, "#!/bin/sh\nexit 9009\n")
                os.chmod(stubs / launcher, 0o755)
            r = build_cap_repo(t / "bare", {lrel: ltext, cap.name: subject}, "warn")
            rc, out = run_case_argv(r, ["bash", derive_enforcer_path(cap), cap.name],
                                    env={"PATH": stubs.as_posix() + os.pathsep + os.environ.get("PATH", ""),
                                         "GOV_PYTHON": None, "TEMPLATE_SIZE_PY": None})
            checks.append(("no python launcher", "refused, saying no launcher resolved",
                           rc not in (0, None) and "no python launcher" in out, f"exit {rc} · {render_said(out, 'launcher')}"))
        elif name == "limits-reader-docstring":
            # TOOL-dGroundRules-21 S29, S30: a docstring, and a comment, naming the limits file, each with a read
            # shape on its line, are no readers; a line that reads it is.
            doc = f'"""Never cat {budgets.LIMITS_NAME} here: open(...) it through budgets.py."""\n# cat {budgets.LIMITS_NAME}\n'
            r = build_cap_repo(t / "r", {lrel: ltext, "scripts/notes.py": doc}, "warn")
            _n, _pop, found = ARM["arm_limits_readers"].run(r, KIT)
            checks.append(("a docstring and a comment", "arm_limits_readers green", not found, f"{found or 'no finding'}"))
            write_case_file(r, "scripts/notes.py", doc + f'rows = open("{budgets.LIMITS_NAME}").read()\n')
            _n, _pop, found = ARM["arm_limits_readers"].run(r, KIT)
            checks.append(("a line that opens it", "red naming that file", [k for k, _w in found] == ["scripts/notes.py"], f"{found}"))
        elif name == "budgets-correctness-kept":
            bm = "memory/guides/BUILD-METHOD.md"
            r = build_cap_repo(t / "r", {lrel: ltext, bm: "**Budget: <=1 bytes, <=1 lines**\nbody\n"}, "warn")
            rc, out = run_case_argv(r, ["bash", derive_enforcer_path(census[bm]), bm])
            checks.append(("a budget line disagreeing with its row, under warn", "exit 6", rc == 6,
                           f"exit {rc} · {render_said(out, 'check 6 FAILED')}"))
        elif name == "census-receiptless-target":
            # TOOL-dGroundRules-29: no receipt and no registry, every row announced and none graded; this
            # kit's registry copied in under its tool root, the tree reads as gov's and every enforcer reds.
            r = build_cap_repo(t / "r", {}, "warn")
            reg = posixpath.join(budgets.derive_tool_root(), REGISTRY_REL)
            for planted in (False, True):
                if planted:
                    write_case_file(r, reg, (top / reg).read_bytes())
                with contextlib.redirect_stdout(io.StringIO()) as said:
                    _n, _pop, found = arm_cap_census(r, KIT)
                told = [ln for ln in said.getvalue().splitlines() if ln.startswith("cap census: ")]
                red = {k for k, w in found if "is not a file" in w}
                if planted:
                    checks.append((f"{reg} copied in", "no announce and a finding naming every row",
                                   not told and red == set(census), f"{len(told)} announced · {len(red)} of {len(census)} row(s) red"))
                else:
                    ok = len(told) == len(census) and all(ln.endswith((" not installed", " · enforcer not shipped")) for ln in told)
                    checks.append(("no receipt and no registry", f"{len(census)} announce line(s) and no finding",
                                   ok and not found, f"{len(told)} announced · {found or 'no finding'}"))
        else:
            checks.append((name, "a known budgets case", False, "no such case"))
    except (subprocess.CalledProcessError, OSError, LookupError, KeyError, policy.Refusal) as exc:
        checks.append((name, "the fixture", False, f"{type(exc).__name__}: {getattr(exc, 'stderr', '') or exc}"))
    finally:
        remove_repo(t)
    return print_checks(name, checks)


BUDGET_CASES = ("budgets-pinned-warn", "budgets-two-homes", "budgets-limits-reader", "budgets-census-join",
                "budgets-switch-refuse", "budgets-no-kit", "budgets-correctness-kept", "budgets-zero-cap",
                "budgets-reader-refused", "limits-reader-docstring", "budgets-unset-derived")


def run_ships_join(name):
    """`budgets-ships-join` (TOOL-dGroundRules-17): the census rows carrying `ships = false` are exactly
    those whose enforcer the deployer's registry exempts, an `[[exempt]]` path equal to the enforcer or
    a directory above it, both ways. The registry is `govkit/registry.toml` under this kit's tool root
    in the source repository, which no adopter holds. One line per row either side names, and a WRONG
    where the registry names no census enforcer, which would join nothing. TOOL-dGroundRules-23: each
    shipped row's `kit` and `installed` equal what govkit's own `resolve_entry` under `canonical_ctx`
    says, and no other entry writes its enforcer; a census with no shipped row is a WRONG too."""
    top = derive_source_top()
    reg = top / budgets.derive_tool_root() / "govkit" / "registry.toml"
    try:
        census = budgets.read_cap_census(top)
        exempt = [str(r.get("path")) for r in tomllib.loads(reg.read_text(encoding="utf-8")).get("exempt", [])]
    except (OSError, tomllib.TOMLDecodeError, policy.Refusal) as exc:
        return print_checks(name, [(name, "the census and the registry", False, f"{type(exc).__name__}: {exc}")])
    checks, rows = [], 0
    for cap in census.values():
        by = next((p for p in exempt if cap.enforcer == p or cap.enforcer.startswith(p + "/")), None)
        rows += by is not None
        if by or not cap.ships:
            checks.append((cap.name, "ships = false exactly where the registry exempts its enforcer",
                           bool(by) != cap.ships, f"{cap.enforcer} · {'exempt as ' + by if by else 'not exempt'} · "
                           f"ships = {str(cap.ships).lower()}"))
    checks.append(("the join", "a census enforcer the registry exempts", rows > 0,
                   f"{rows} row(s) of {len(census)}, exempt by {reg.relative_to(top).as_posix()}"))
    # TOOL-dGroundRules-23: each shipped row's `kit` and `installed` against what the deployer's own
    # resolver says the entry writes, both ways: the row's entry writes its enforcer at `installed`, and
    # no other entry writes that source. A `ships = false` row carrying either field never gets here:
    # read_cap_census refuses it above, naming the row, and that Refusal is this case's WRONG.
    troot = budgets.derive_tool_root()
    try:  # TOOL-dGroundRules-34 S7, S8: the working tree's deployer, the one sanctioned read outside a snapshot
        gk = resolve_govkit(top)
    except RuntimeError as exc:
        checks.append(("the deployer", "the deployer is located", False, str(exc)))
        return print_checks(name, checks)
    try:
        spec = importlib.util.spec_from_file_location("govkit_ships_join", gk)
        govkit = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(govkit)
    except Exception as exc:  # noqa: BLE001 (a deployer that does not import is this case's WRONG)
        checks.append(("the deployer", "the deployer loads", False, f"{gk.relative_to(top).as_posix()}: {type(exc).__name__}: {exc}"))
        return print_checks(name, checks)
    try:  # TOOL-dGroundRules-32 S8: the registry read the deployer's `shipped` verb makes, its refusal naming every problem
        descs = govkit.read_shipped_descriptors(top)
    except govkit.Refusal as exc:
        checks.append(("the deployer", "every registry descriptor reads", False, str(exc).replace("\n", "; ")))
        return print_checks(name, checks)
    try:
        writes = {eid: govkit.resolve_entry(top, desc, govkit.canonical_ctx(eid))["writes"]
                  for eid, (desc, _p) in descs.items()}
    except Exception as exc:  # noqa: BLE001 (a deployer that does not resolve is this case's WRONG)
        checks.append(("the deployer", "the deployer resolves every entry", False,
                       f"{gk.relative_to(top).as_posix()}: {type(exc).__name__}: {exc}"))
        return print_checks(name, checks)
    shipped = [cap for cap in census.values() if cap.ships]
    for cap in shipped:
        src = budgets.resolve_prefix_token(cap.enforcer, troot)
        hits = sorted((eid, dest) for eid, w in writes.items() for dest, row in w.items() if row.get("src") == src)
        want = [(cap.kit, budgets.resolve_prefix_token(cap.installed, troot))]
        checks.append((cap.name, "its kit writes its enforcer at installed, and no other entry writes it",
                       hits == want, f"row: kit {cap.kit} · installed {cap.installed} · the resolver writes {src} as "
                       f"{', '.join(f'{e} -> {d}' for e, d in hits) or 'no entry'}"))
    checks.append(("the destination join", "a shipped census row", bool(shipped),
                   f"{len(shipped)} shipped row(s) of {len(census)}, against {len(writes)} registry entries "
                   f"resolved by {gk.name}"))
    return print_checks(name, checks)


FIXTURES_LEG = "policy fixtures"
# A shell enforcer's `.` or `source` line, its operand the file it sources.
SOURCED = re.compile(r"""^\s*(?:\.|source)\s+["']?([^"'\s;)]+)""", re.M)


def derive_enforcer_imports(top, rel):
    """The files in the enforcer's own directory that the repo-relative enforcer `rel` reaches, read
    transitively, sorted: each module a Python file imports, at any depth of its body, that sits beside
    it, and each file a shell file sources that sits beside it, its operand read by basename
    (TOOL-dGroundRules-25 S24). An edit to one of them changes what the enforcer runs, so the leg whose
    cases run the enforcer must run on it too (gotcha held-suite-guard-misses-a-sibling-kit). A file
    that does not read or parse reaches nothing."""
    out, todo = set(), [rel]
    while todo:
        cur = todo.pop()
        here = posixpath.dirname(cur)
        text = policy.read_text_or_none(Path(top, cur)) or ""
        found = []
        if cur.endswith(".py"):
            try:
                tree = ast.parse(text)
            except SyntaxError:
                tree = ast.Module(body=[], type_ignores=[])
            for n in ast.walk(tree):
                if isinstance(n, ast.Import):
                    found += [a.name.split(".")[0] + ".py" for a in n.names]
                elif isinstance(n, ast.ImportFrom) and n.module and not n.level:
                    found.append(n.module.split(".")[0] + ".py")
        elif cur.endswith(".sh"):
            found = [posixpath.basename(m[1]) for m in SOURCED.finditer(text)]
        for f in found:
            dep = posixpath.join(here, f)
            if dep != rel and dep not in out and Path(top, dep).is_file():
                out.add(dep)
                todo.append(dep)
    return sorted(out)


def read_legs_for(top, checker, paths):
    """`python <checker> --legs-for -` run at `top` with `paths` on stdin -> {path: the legs whose guard
    it trips}: gov's one trip rule, never a second one spelled here (TOOL-dGroundRules-25 S25). A
    checker that does not run or exits non-zero is a RuntimeError naming it."""
    try:
        p = subprocess.run([sys.executable, str(checker), "--legs-for", "-"], cwd=top, input="\n".join(paths),
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
    except OSError as exc:
        raise RuntimeError(f"{checker.name} did not run: {exc}") from None
    if p.returncode:
        raise RuntimeError(f"{checker.name} --legs-for exited {p.returncode}: {render_said(p.stdout + p.stderr, 'REFUSING')}")
    legs, cur = {}, None
    for ln in p.stdout.replace("\r", "").split("\n"):
        if ln.startswith("  ") and cur is not None and " <- " in ln and not ln.strip().startswith("UNEVALUATED "):
            legs[cur].add(ln.strip().split(" <- ", 1)[0])
        elif ln and not ln.startswith((" ", "legs-for:")):
            cur = ln.removesuffix(" (not tracked at HEAD)")
            legs.setdefault(cur, set())
    return legs


def run_fixtures_guard_census(name):
    """`fixtures-guard-census` (TOOL-dGroundRules-20): every path a `budgets-cap-` case runs must trip
    the `policy fixtures` leg, by the spec-token checker's `--legs-for -` under this kit's tool root in
    the source repository, gov's one trip rule (TOOL-dGroundRules-25 S25): each distinct census
    enforcer, each file `derive_enforcer_imports` finds it reaching (S24), and `gate-legs.json`, which
    this case reads (S23). An edit to one outside the guard skips the leg that runs it. One line per
    path, and a WRONG where the census has no row, the manifest no such leg, or the checker is absent
    or refuses, since a join over nothing, or with no judge, proves nothing."""
    top, troot = derive_source_top(), budgets.derive_tool_root()
    legs = top / troot / "gate-legs.json"
    checker = top / budgets.resolve_prefix_token("{prefix}/check-spec-tokens.py", troot)
    reg = top / budgets.resolve_prefix_token("{prefix}/govkit/registry.toml", troot)
    try:
        census = budgets.read_cap_census(top)
        row = next((r for r in json.loads(legs.read_text(encoding="utf-8")) if r.get("name") == FIXTURES_LEG), None)
        descs = {str(e.get("id")): budgets.resolve_prefix_token(str(e.get("descriptor")), troot)
                 for e in tomllib.loads(reg.read_text(encoding="utf-8")).get("entry", []) if isinstance(e, dict)}
    except (OSError, ValueError, AttributeError, policy.Refusal) as exc:
        return print_checks(name, [(name, "the census, the gate manifest and the registry", False,
                                    f"{type(exc).__name__}: {exc}")])
    runs = {legs.relative_to(top).as_posix(): ["this case, which reads it"]}
    for cap in census.values():
        e = budgets.resolve_prefix_token(cap.enforcer, troot)
        runs.setdefault(e, []).append(CAP_CASE_PREFIX + cap.name)
        for dep in derive_enforcer_imports(top, e):
            runs.setdefault(dep, []).append(f"{e}, which reaches it")
    # TOOL-dGroundRules-32 S3, S10: each census kit's descriptor, from the registry's `descriptor` field;
    # each kit of this kit's `requires` closure, its descriptor and its `[adopt]` script, which the
    # fresh-target case installs and runs; and run-gates' descriptor and the `regen.py` beside it, which
    # that case runs too. None is typed here: an id the registry lacks has no path to grade, so a WRONG.
    closure, missed = derive_requires_closure([tomllib.loads((KIT / "kit.toml").read_text(encoding="utf-8"))["id"]])
    owed = [(k, "a census kit's descriptor") for k in dict.fromkeys(c.kit for c in census.values() if c.kit)]
    owed += [(k, "a requires-closure kit's descriptor") for k in closure] + [("run-gates", "the fresh-target case")]
    for kid, why in owed:
        if kid not in descs:
            missed.append(f"{kid} is {why} and no entry of {reg.relative_to(top).as_posix()}")
            continue
        runs.setdefault(descs[kid], []).append(f"{why}, {kid}")
    for kid in closure + ["run-gates"]:
        d = descs.get(kid)
        try:
            desc = tomllib.loads((top / d).read_text(encoding="utf-8")) if d else {}
        except (OSError, tomllib.TOMLDecodeError) as exc:
            missed.append(f"the descriptor of {kid} does not read: {type(exc).__name__}: {exc}")
            continue
        home = posixpath.join(troot, desc["home"]) if desc.get("home") else posixpath.dirname(d or "")
        steps = [a.replace("{kit}", home) for a in (desc.get("adopt") or {}).get("argv", []) if "{kit}/" in a]
        for p in steps if kid != "run-gates" else [posixpath.join(home, "regen.py")]:
            runs.setdefault(p, []).append(f"the fresh-target case, which runs {kid}'s {posixpath.basename(p)}")
    checks = [("the join", f"a census row and the {FIXTURES_LEG} leg", bool(census) and row is not None,
               f"{len(runs)} path(s) of {len(census)} row(s) · leg {'found' if row else 'absent'} in "
               f"{legs.relative_to(top).as_posix()}")]
    checks += [("the registry", "every kit this case owes a path resolves", False, m) for m in missed]
    if not checker.is_file():
        return print_checks(name, checks + [("the judge", "the spec-token checker beside the manifest", False,
                                             f"{checker.relative_to(top).as_posix()} is absent, so no path was judged")])
    try:
        tripped = read_legs_for(top, checker, list(runs))
    except RuntimeError as exc:
        return print_checks(name, checks + [("the judge", "the spec-token checker's --legs-for", False, str(exc))])
    for p, why in runs.items():
        ok = FIXTURES_LEG in tripped.get(p, ())
        checks.append((p, f"trips the {FIXTURES_LEG} leg", ok, f"run by {', '.join(why[:3])}" if ok else
                       f"{p} is run by {', '.join(why[:3])} and trips no {FIXTURES_LEG} guard"))
    return print_checks(name, checks)


SOURCE_READS = set()  # what `add_source_read` kept: source files this process opened to read, top-relative
UNMAPPED_READS = set()  # the SOURCE_READS kept as spelled because `source_from_cache` refused their cache name
TRACE_ROOTS = []  # [the source top, the case temporary root or None, the source's git directories], set where `--fixture` installs the hook


def read_source_git_dirs(top):
    """The source's git directory and common directory, as git answers at `top` (TOOL-dGroundRules-38 S1),
    absolute and resolved: in a primary checkout one `.git` under the top level, twice; in a linked
    worktree two directories outside it. Asked of `top`, never of the caller's working directory.
    -> (git dir, common dir); RuntimeError naming rev-parse where git does not answer both."""
    out = policy.run_git(top, "rev-parse", "--path-format=absolute", "--git-dir", "--git-common-dir")
    dirs = (out or "").splitlines()
    if len(dirs) != 2 or not all(dirs):
        raise RuntimeError(f"git rev-parse --git-dir --git-common-dir at {Path(top).as_posix()} did not answer both")
    return tuple(os.path.realpath(d) for d in dirs)


def add_source_read(event, args):
    """The audit hook `--fixture` installs before its first case (TOOL-dGroundRules-33 S2): an `open`
    event whose mode reads and writes nothing, a None mode read by its flags, which carry none of
    `O_WRONLY`, `O_RDWR` or `O_CREAT` (TOOL-dGroundRules-43 S9), on a path that resolves, against the working directory,
    under the source repository's top level, under no case's temporary directory and under neither of
    the source's git directories (TOOL-dGroundRules-38 S2: the snapshot's index and exclude-file copies
    are git's reads, never a source file's), is kept in SOURCE_READS, top-relative in `/` form. Only this process's reads are seen, never a subprocess's.
    A hook that raised would fail the very open it audits, so a path that does not resolve keeps nothing.
    A bytecode-cache read is kept as the source file it was compiled from (TOOL-dGroundRules-35 S1), so
    a warm load still records its `.py`; a cache name `source_from_cache` refuses is kept as spelled,
    and in UNMAPPED_READS too, so the trace names it (TOOL-dGroundRules-52 S25)."""
    if event != "open" or not TRACE_ROOTS:
        return
    try:
        path, mode, flags = args[0], args[1], args[2]
        if isinstance(path, int):
            return
        if mode is None:  # TOOL-dGroundRules-43 S9: `os.open` carries its intent in the flags alone
            if flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT):
                return
        elif not isinstance(mode, str) or any(c in mode for c in "wax+"):
            return
        p = os.fsdecode(path)
        refused = False
        # TOOL-dGroundRules-52 S20: no `.pyc.<digits>` cut, since S9's flag filter above drops importlib's temporary write
        if os.path.basename(os.path.dirname(p)) == "__pycache__" and p.endswith(".pyc"):
            try:
                p = importlib.util.source_from_cache(p)
            except ValueError:
                refused = True
        p = os.path.realpath(p)
        top, tmp, git_dirs = TRACE_ROOTS
        n = os.path.normcase(p)
        if any(n.startswith(os.path.normcase(d) + os.sep) for d in git_dirs):
            return
        if n.startswith(os.path.normcase(top) + os.sep) and not (tmp and n.startswith(os.path.normcase(tmp) + os.sep)):
            rel = os.path.relpath(p, top).replace(os.sep, "/")
            SOURCE_READS.add(rel)
            if refused:  # TOOL-dGroundRules-52 S25: named by the trace, never only counted by a set-aside
                UNMAPPED_READS.add(rel)
    except Exception:  # noqa: BLE001 - the hook must never fail an open
        return


def check_guard_trace():
    """The guard trace's join (TOOL-dGroundRules-33 S3): every path `add_source_read` kept that exists
    under the source top when this runs (TOOL-dGroundRules-43 S9, the rest counted as absent) and git does
    not ignore (`derive_guardable_reads`, TOOL-dGroundRules-36), piped to the spec-token checker's
    `--legs-for -` through `read_legs_for`, gov's one trip rule, and a WRONG naming each path that trips
    no `policy fixtures` guard: an edit to it alone would skip the leg whose cases read it. The count
    line comes first, then the set-aside count on every run, so an empty trace is seen, and is a WRONG of
    its own, as is an ignore query or a checker that does not run: a join over nothing, or with no
    judge, proves nothing. -> (assertions, wrong)."""
    kept = sorted(SOURCE_READS)
    print(f"policy-fixture: guard-trace · {len(kept)} source read(s)")
    for p in sorted(UNMAPPED_READS):  # TOOL-dGroundRules-52 S25, before any set-aside can hide it
        print(f"policy-fixture: guard-trace · unmapped cache read {p}")
    top = derive_source_top()
    # TOOL-dGroundRules-43 S9: a read of a path absent now, a failed probe or a file since removed,
    # is no source file a guard could cover, so it is counted and set aside, never joined
    present = [p for p in kept if (top / p).exists()]
    print(f"policy-fixture: guard-trace · {len(kept) - len(present)} absent read(s) set aside")
    kept = present
    try:
        kept, n = derive_guardable_reads(kept, top)
    except RuntimeError as exc:
        print(f"policy-fixture: guard-trace · WRONG: {exc}, so no read was joined to the guard")
        return 1, 1
    print(f"policy-fixture: guard-trace · {n} ignored read(s) set aside")
    if not kept:
        print("policy-fixture: guard-trace · WRONG: no source read was traced, so nothing was joined to the guard")
        return 1, 1
    checker = top / budgets.resolve_prefix_token("{prefix}/check-spec-tokens.py", budgets.derive_tool_root())
    try:
        tripped = read_legs_for(top, checker, kept)
    except RuntimeError as exc:
        print(f"policy-fixture: guard-trace · WRONG: {exc}, so no read was joined to the guard")
        return 1, 1
    missed = [p for p in kept if FIXTURES_LEG not in tripped.get(p, ())]
    for p in missed:
        print(f"policy-fixture: guard-trace · WRONG {p} · not under the {FIXTURES_LEG} guard")
    return 1 + len(kept), len(missed)


def derive_guardable_reads(kept, top):
    """The kept reads git does not ignore (TOOL-dGroundRules-36 S1), asked of `git check-ignore --stdin`
    at `top`, so `.gitignore`, the exclude file and `core.excludesFile` decide and no pattern is spelled
    here. A path git ignores never reaches the runner's diff, so no guard can trip on it. Exit 1 means
    none is ignored; a git that does not start, or any other exit, is a RuntimeError naming
    check-ignore, never "nothing ignored". Paths go in and come out NUL-terminated under `-z`, through
    `os.fsencode` and `os.fsdecode`, so git never C-quotes one and no path is refused by a narrower
    encoding (TOOL-dGroundRules-52 S6, S14). -> (guardable, the count of kept paths set aside)."""
    env = {k: v for k, v in os.environ.items() if k not in policy.GIT_ENV_LEAKS}
    try:
        # bytes in: a text-mode pipe on Windows writes `\r\n`, and git reads `p\r` as a path no rule matches
        p = subprocess.run(["git", "-C", str(top), "check-ignore", "--stdin", "-z"],
                           input=b"".join(os.fsencode(k) + b"\0" for k in kept), env=env, capture_output=True)
    except OSError as exc:
        raise RuntimeError(f"git check-ignore did not run: {exc}") from None
    if p.returncode not in (0, 1):
        said = render_said((p.stdout + p.stderr).decode("utf-8", "replace"), "fatal")
        raise RuntimeError(f"git check-ignore exited {p.returncode}: {said}")
    ignored = {os.fsdecode(b) for b in p.stdout.split(b"\0") if b}
    return [k for k in kept if k not in ignored], sum(k in ignored for k in kept)


def check_guard_lines():
    """Every entry of the `policy fixtures` guard names a file git tracks (TOOL-dGroundRules-37 S1):
    the guard trips by its literal spelling, tracked or not, so the trace's join cannot see a dead
    entry, and a gitignored or never-staged path a sweep wrote there guards nothing the runner's
    `git diff` lists. Each entry, `{prefix}` resolved, is asked of `git ls-files` at the source top,
    the index and never the disk (S3), and one that lists nothing is a WRONG. The count line comes
    first (S2); a manifest that does not parse or holds no such row is a WRONG of its own, never zero
    dead lines. -> (assertions, wrong)."""
    top, troot = derive_source_top(), budgets.derive_tool_root()
    try:
        rows = json.loads((top / troot / "gate-legs.json").read_text(encoding="utf-8"))
        row = next((r for r in rows if r.get("name") == FIXTURES_LEG), None)
    except (OSError, ValueError, TypeError, AttributeError) as exc:
        print(f"policy-fixture: guard-trace · WRONG: the manifest did not parse: {exc}, so no guard line was checked")
        return 1, 1
    if row is None:
        print(f"policy-fixture: guard-trace · WRONG: the manifest holds no {FIXTURES_LEG} row, so no guard line was checked")
        return 1, 1
    guard = row.get("guard") or []
    print(f"policy-fixture: guard-trace · {len(guard)} guard line(s) checked")
    dead = [e for e in guard if not (policy.run_git(top, "ls-files", "--", budgets.resolve_prefix_token(e, troot)) or "").strip()]
    for e in dead:
        print(f"policy-fixture: guard-trace · WRONG guard {e} · names no file git tracks")
    return 1 + len(guard), len(dead)


ADOPTER_KITS =("policy", "memory-tree", "kickoff-manifest")  # the planted receipt's kits: no check-line-length
ADOPTER_PREFIX = "vendor/gov"  # the planted tool root, unlike gov's own, so `{prefix}` must be read from the receipt


def run_census_adopter_receipt(name):
    """`census-adopter-receipt` (TOOL-dGroundRules-22): a scratch repository on main holding an install
    receipt whose `kits` is ADOPTER_KITS and whose `prefix` is ADOPTER_PREFIX, each census enforcer of
    those kits copied from the source to its `installed` path there, and no deployer. `arm_cap_census`
    must announce `line-length · kit check-line-length not installed`, announce no `manifest-bytes`
    line and find nothing; with the planted `manifest-check.sh` deleted it must red naming
    `manifest-bytes` and that path; restored, it must find nothing."""
    top, checks = derive_source_top(), []
    t = Path(tempfile.mkdtemp(prefix="pol-"))
    try:
        census = budgets.read_cap_census(top)
        planted = {budgets.resolve_prefix_token(c.installed, ADOPTER_PREFIX): (top / derive_enforcer_rel(c)).read_bytes()
                   for c in census.values() if c.kit in ADOPTER_KITS}
        receipt = json.dumps({"prefix": ADOPTER_PREFIX, "kits": list(ADOPTER_KITS)})
        r = build_cap_repo(t / "r", {**planted, RECEIPT_REL: receipt}, "warn")
        mb = budgets.resolve_prefix_token(census["manifest-bytes"].installed, ADOPTER_PREFIX)

        def run_census():
            with contextlib.redirect_stdout(io.StringIO()) as said:
                _n, _pop, found = arm_cap_census(r, KIT)
            return said.getvalue(), found
        said, found = run_census()
        want = "cap census: line-length · kit check-line-length not installed"
        checks.append(("the kits installed", f"{want!r}, no manifest-bytes announce and no finding",
                       want in said.splitlines() and "cap census: manifest-bytes ·" not in said and not found,
                       f"{render_said(said, 'line-length ·')} · {found or 'no finding'}"))
        Path(r, mb).unlink()
        _said, found = run_census()
        checks.append((f"{mb} deleted", "red naming manifest-bytes and its installed path",
                       any(k == "manifest-bytes" and mb in w for k, w in found), f"{found}"))
        write_case_file(r, mb, planted[mb])
        _said, found = run_census()
        checks.append((f"{mb} restored", "no finding", not found, f"{found or 'no finding'}"))
    except (subprocess.CalledProcessError, OSError, LookupError, KeyError, policy.Refusal) as exc:
        checks.append((name, "the fixture", False, f"{type(exc).__name__}: {getattr(exc, 'stderr', '') or exc}"))
    finally:
        remove_repo(t)
    return print_checks(name, checks)


def derive_window_edge_paths():
    """`census-window-edge`'s registries (TOOL-dGroundRules-39 S3) -> (written, planted). `written`:
    REGISTRY_REL under this kit's tool root, one deep; under a `<d>` three deep, outside the window;
    and a bare `registry.toml` at the top level, under no `govkit/`. `planted`: REGISTRY_REL under
    RELOCATED_PREFIX's tool root, two deep, inside the window."""
    written = (posixpath.join(budgets.derive_tool_root(), REGISTRY_REL), posixpath.join("a/b/c", REGISTRY_REL),
               posixpath.basename(REGISTRY_REL))
    return written, posixpath.join(posixpath.dirname(RELOCATED_PREFIX.rstrip("/")), REGISTRY_REL)


def run_census_window_edge(name):
    """`census-window-edge` (TOOL-dGroundRules-39 S1): the edges of the window `derive_census_tree`
    searches with no receipt. Over `derive_window_edge_paths`' written registries, each a copy of the
    source's, in a receipt-less repository it must answer ("source", this kit's tool root), the
    depth-3 and top-level files uncounted; with the planted depth-2 one added it must refuse naming exactly that one and the
    depth-1 one, its line reading `RED as planted`. An outcome case: an armed one's unplanted run
    would grade every census enforcer and find each absent."""
    written, planted = derive_window_edge_paths()
    checks, t = [], Path(tempfile.mkdtemp(prefix="pol-"))

    def ask():
        try:
            return policy.derive_census_tree(t)
        except policy.Refusal as exc:
            return f"refused {exc.path}"
    try:
        registry = (derive_source_top() / written[0]).read_bytes()  # each plant a copy of the source's registry
        run_fixture_git(t, "init", "-q")
        for rel in written:
            write_case_file(t, rel, registry)
        want, got = ("source", budgets.derive_tool_root()), ask()
        checks.append((", ".join(written), f"{want}, the depth-3 and top-level registries uncounted",
                       got == want, f"{got}"))
        write_case_file(t, planted, registry)
        want, got = f"refused {', '.join(sorted((written[0], planted)))}", ask()
        checks.append((f"{planted} planted", want, got == want, "RED as planted" if got == want else f"{got}"))
    except (subprocess.CalledProcessError, OSError) as exc:
        checks.append((name, "the fixture", False, f"{type(exc).__name__}: {getattr(exc, 'stderr', '') or exc}"))
    finally:
        remove_repo(t)
    return print_checks(name, checks)


# ---- the live observation (TOOL-dGroundRules-10 S9) ------------------------------------------------

LIVE_LIMIT = 2
LIVE_BOUND = 900
STAMP = ("import sys, time\n"
         "name, log = sys.argv[1], sys.argv[2]\n"
         "with open(log, 'a', encoding='utf-8') as f:\n"
         "    f.write('start %s %d\\n' % (name, time.time_ns()))\n"
         "time.sleep(20)\n"
         "with open(log, 'a', encoding='utf-8') as f:\n"
         "    f.write('end %s %d\\n' % (name, time.time_ns()))\n")


def render_workflow_prompt(runs, log):
    """A prompt asking for `runs` Workflow calls in ONE message, each a script of four agents that each
    run the stamp script under a name `r<run>-<agent>`."""
    blocks = []
    for r in range(1, runs + 1):
        blocks.append(
            "```js\nexport const meta = { name: 'live-limit-%d', description: 'four stamps' }\n"
            "await parallel([1, 2, 3, 4].map((i) => () => agent(`Run exactly this command with the Bash tool "
            "and nothing else, then reply done: python stamp.py r%d-${i} %s`)))\n```" % (r, r, log))
    return (f"Call the Workflow tool {'once' if runs == 1 else f'{runs} times in ONE message'}, "
            f"passing {'this script' if runs == 1 else 'these scripts, one per call'} as `script`, and do "
            "nothing else:\n\n" + "\n\n".join(blocks))


def render_spawn_prompt(log):
    return ("In ONE message, call the Agent tool three times with run_in_background true, each with the "
            "general-purpose type and this prompt, its name a1, a2 and a3 in turn: `Run exactly this command "
            f"with the Bash tool and nothing else, then reply done: python stamp.py <name> {log}`. Then wait "
            "for every agent that started and reply done.")


def derive_peak(lines, prefix=""):
    """-> (peak overlap, names that stamped) of the `start <name> <ns>` / `end <name> <ns>` lines whose
    name opens `prefix`; an end sorts before a start at the same instant."""
    events, names = [], set()
    for ln in lines:
        f = ln.split()
        if len(f) == 3 and f[0] in ("start", "end") and f[1].startswith(prefix) and f[2].isdigit():
            events.append((int(f[2]), 0 if f[0] == "end" else 1))
            names.add(f[1])
    peak = cur = 0
    for _ns, kind in sorted(events):
        cur += 1 if kind else -1
        peak = max(peak, cur)
    return peak, names


def read_tool_errors(stream):
    """-> the count of tool results the session's stream-json output marks as errors."""
    n = 0
    for ln in stream.splitlines():
        try:
            ev = json.loads(ln)
        except ValueError:
            continue
        content = (ev.get("message") or {}).get("content") if isinstance(ev, dict) else None
        n += sum(1 for c in content or [] if isinstance(c, dict) and c.get("type") == "tool_result" and c.get("is_error"))
    return n


def run_live_session(claude, repo, prompt, log):
    """One headless session in `repo` -> (stamp lines, stream-json text, a failure or "")."""
    env = {k: v for k, v in os.environ.items() if k not in (*policy.SETTINGS_VARS, "CLAUDE_PROJECT_DIR")}
    try:
        p = subprocess.run([claude, "-p", prompt, "--output-format", "stream-json", "--verbose",
                            "--permission-mode", "bypassPermissions"], cwd=repo, env=env, capture_output=True,
                           text=True, encoding="utf-8", errors="replace", timeout=LIVE_BOUND)
        why = "" if p.returncode == 0 else f"claude exited {p.returncode}: {(p.stderr or '').strip()[:300]}"
        stream = p.stdout
    except (OSError, subprocess.TimeoutExpired) as exc:
        why, stream = f"claude did not finish: {exc}", ""
    lines = Path(log).read_text(encoding="utf-8").splitlines() if Path(log).is_file() else []
    return lines, stream, why


def run_live():
    """`--live`: a fixture repository whose policy sets the limit to LIVE_LIMIT, its settings rendered by
    `policy.py settings --write`, and headless `claude -p` sessions whose agents each run the stamp
    script, a start and an end line around a 20-second sleep. Each scenario runs under the render and
    under the control, `{}` as the settings. AC15: a Workflow of four agents peaks at most at the limit,
    and the control at 3 or more. AC16: three background Agents in one message stamp at most the limit
    at once, the third's tool result an error with no stamp of its own; the control stamps all three,
    overlapping. AC17: two Workflow runs of four in one message, each run's peak at most the limit; the
    session's total peak is printed, never asserted. Exit 0 every check held, 1 one did not, 2 no
    `claude` on PATH."""
    claude = shutil.which("claude")
    if claude is None:
        print("policy-live: NOT RUN — no claude on PATH, and a run that observed nothing is never a pass")
        return 2
    t = Path(tempfile.mkdtemp(prefix="pol-"))
    checks = []
    try:
        repo = build_reader_repo(t / "r", LIMIT_POLICY.format(n=LIVE_LIMIT))
        Path(repo, "stamp.py").write_text(STAMP, encoding="utf-8", newline="\n")
        for control in (False, True):
            arm = "control, no env" if control else f"settings at {LIVE_LIMIT}"
            if control:
                write_settings(repo, None)
            else:
                p = subprocess.run([sys.executable, str(KIT / "policy.py"), "settings", "--write"], cwd=repo,
                                   capture_output=True, text=True, encoding="utf-8", errors="replace")
                checks.append((arm, "policy.py settings --write", p.returncode == 0, p.stdout.strip() or p.stderr.strip()))
            for scenario in ("AC15", "AC16", "AC17"):
                log = (t / f"{scenario}-{int(control)}.log").as_posix()
                prompt = render_spawn_prompt(log) if scenario == "AC16" else render_workflow_prompt(
                    2 if scenario == "AC17" else 1, log)
                lines, stream, why = run_live_session(claude, repo, prompt, log)
                if why:
                    checks.append((scenario, arm, False, why))
                    continue
                if scenario == "AC15":
                    peak, names = derive_peak(lines)
                    ok = peak >= 3 if control else peak <= LIVE_LIMIT and len(names) == 4
                    checks.append((scenario, arm, ok, f"peak {peak} over {len(names)} stamp(s)"))
                elif scenario == "AC16":
                    peak, names = derive_peak(lines)
                    errors = read_tool_errors(stream)
                    ok = (len(names) == 3 and peak >= 3) if control else (peak <= LIVE_LIMIT and len(names) == 2 and errors >= 1)
                    checks.append((scenario, arm, ok, f"peak {peak} · {len(names)} stamped · {errors} tool error(s)"))
                else:
                    peaks = [derive_peak(lines, f"r{r}-")[0] for r in (1, 2)]
                    total = derive_peak(lines)[0]
                    ok = True if control else all(pk <= LIVE_LIMIT for pk in peaks)
                    checks.append((scenario, arm, ok, f"run peaks {peaks} · the session's total peak {total}, printed and not asserted"))
    finally:
        remove_repo(t)
    asserted, wrong = print_checks("live", checks)
    print(f"policy-live: {asserted} check(s) · {wrong} wrong")
    return 1 if wrong or not asserted else 0


CASES = [
    ("shape-no-empty", ARM["arm_shape"], seed_no_empty),
    ("shape-unknown-field", ARM["arm_shape"], seed_unknown_field),
    ("usage-out-of-set", ARM["arm_shape"], seed_usage_out_of_set),
    ("summary-new-key", ARM["arm_summaries"], seed_summary_new_key),
    ("usage-new-key", ARM["arm_summaries"], seed_usage_new_key),
    ("list-grew", ARM["arm_summaries"], seed_list_grew),
    ("direction-missing", ARM["arm_direction"], seed_direction_missing),
    ("direction-new-bound", ARM["arm_direction"], seed_direction_new_bound),
    ("direction-wrong-value", ARM["arm_direction"], seed_direction_wrong_value),
    (FRESH_TARGET, None, run_fresh_target),  # an outcome case: no plant and no one arm
    ("adopter-suite", None, run_adopter_suite),  # the adopter's sibling suite, which arms its refusals
    ("legacy-homes-withheld-install", None, run_legacy_withheld_install),  # the plan's row and the applied target (TOOL-dGroundRules-25)
    ("census-default-adopter", None, run_census_default_adopter),  # the census over a real install without check-line-length
    ("govkit-source-root-refused", None, run_govkit_source_root_refused),  # run_govkit refuses the tree under test's own root
    ("arms-empty-declared", None, run_arms_empty_declared),  # every ARMS row declares its empty and why
    ("arms-empty-target", None, run_arms_empty_target),  # the announcing arms over an empty target, arm_schema over its scaffold
    ("reader-landed", None, run_reader_landed),  # outcome cases: the reader over its own repositories
    ("reader-parsed", None, run_reader_parsed),
    ("resolution-order", None, run_resolution_order),
    ("on-invalid-classes", None, run_on_invalid_classes),
    ("on-invalid-strict", None, run_on_invalid_strict),
    *((c, None, run_reader_refusals) for c in READER_REFUSAL_CASES),  # the reader's refusals (TOOL-dGroundRules-21)
    ("mirror-hand-edited", ARM["arm_mirror_parity"], seed_mirror_hand_edited),
    ("mirror-absent", ARM["arm_mirror_parity"], seed_mirror_absent),
    ("mirror-direct-reader", ARM["arm_mirror_readers"], seed_mirror_direct_reader),
    ("mirror-worktree-loosened", None, run_mirror_landed),  # outcome cases: the helper over a landed L
    ("mirror-stale-last-valid", None, run_mirror_landed),
    ("mirror-stale-refuse", None, run_mirror_landed),
    ("mirror-absent-refuse", None, run_mirror_landed),
    ("mirror-commit-rewrite", None, run_mirror_landed),
    ("mirror-landed-merge", None, run_mirror_landed),
    ("mirror-stale-legacy", None, run_mirror_landed),
    ("mirror-shim-exit-one", None, run_mirror_landed),
    ("mirror-absent-adopter", None, run_mirror_absent_adopter),
    ("mirror-landed-parity", None, run_mirror_landed_parity),
    *((g, None, run_guard_case) for g in [*GUARD_PLANTS, "guard-merge-side", *GUARD_MIRROR, *GUARD_INPUTS]),  # outcome cases: guard.py --staged
    ("legacy-homes", None, run_legacy_homes),  # an outcome case: one planted repository per case
    ("legacy-homes-main-dropped", None, run_legacy_main_dropped),  # the base is the merge-base, not the tip
    ("legacy-homes-present", None, run_legacy_present),  # gov's own list held and withheld from installs
    ("reader-coverage", None, run_reader_coverage),  # an outcome case: one planted repository per case
    ("reader-coverage-relocated", None, run_reader_relocated),  # the kits at a tool root unlike gov's
    ("reader-quoted-pattern", None, run_reader_quoted),  # a pattern key read through a quoted segment
    *((c, None, run_limit_case) for c in LIMIT_CASES),  # outcome cases: the agent limit, one repository each
    *((c, ARM["arm_schema"], s) for c, s in BUDGET_SCHEMA_SEEDS.items()),  # the size switch's schema plants
    *((c, None, run_budget_case) for c in BUDGET_CASES),  # outcome cases: the size switch
    ("budgets-ships-join", None, run_ships_join),  # the census's ships flags against the registry's exemptions
    ("fixtures-guard-census", None, run_fixtures_guard_census),  # the census's enforcers inside this leg's guard
    ("census-adopter-receipt", None, run_census_adopter_receipt),  # the census graded at each row's installed path
    ("census-receiptless-target", None, run_budget_case),  # no receipt and no registry: every row announced
    ("census-ambiguous-registry", ARM["arm_cap_census"], seed_ambiguous_registry),  # two registries: one finding naming both
    ("census-window-edge", None, run_census_window_edge),  # the window's edges: depth 3 and a bare top-level file uncounted
    *((CAP_CASE_PREFIX + n, None, run_cap_case) for n in CAP_CASES),  # one per census row
]


def derive_cases(rows):
    """One `schema-empty-<name>` case per never-empty row of the shipped catalogue, then CASES."""
    return [(f"schema-empty-{r['name']}", ARM["arm_schema"], seed_empty_value(r)) for r in rows if r.get("empty") == "never"] + CASES


def run_fixture_git(repo, *args):
    """`git <args>` in a fixture repository, as the fixture's committer -> its stdout, stripped."""
    return subprocess.run(["git", "-C", str(repo), "-c", "user.name=policy-fixture", "-c", "user.email=policy-fixture@invalid",
                           "-c", "commit.gpgsign=false", *args], check=True, capture_output=True,
                          text=True, encoding="utf-8", errors="replace").stdout.strip()


def build_repo(rows):
    """A committed copy of this kit's catalogue and list at the kit's own path, the scaffold beside it,
    a consumer outside the kit that reads policy through the helper, and a remote-tracking ref at that
    commit; then the mirror rendered at it, in the working tree. -> (repo, kit copy)."""
    repo = Path(tempfile.mkdtemp(prefix="pol-"))
    prefix = (policy.run_git(KIT, "rev-parse", "--show-prefix") or "").strip()  # derived, never spelled
    kit = repo / prefix if prefix else repo
    kit.mkdir(parents=True, exist_ok=True)
    for name in (policy.CATALOGUE, policy.LIST, budgets.CENSUS):
        (kit / name).write_bytes((KIT / name).read_bytes().replace(b"\r\n", b"\n"))
    Path(repo, POLICY_FILE[0]).mkdir()
    Path(repo, *POLICY_FILE).write_bytes(policy.render_scaffold(rows).encode("utf-8"))
    Path(repo, *CONSUMER_FILE[:-1]).mkdir()
    Path(repo, *CONSUMER_FILE).write_text(CONSUMER_TEXT.replace("@helper@", json.dumps(f"../{prefix}policy-mirror.js")),
                                          encoding="utf-8", newline="\n")
    run_fixture_git(repo, "init", "-q")
    run_fixture_git(repo, "symbolic-ref", "HEAD", "refs/heads/main")
    run_fixture_git(repo, "add", "-A")
    run_fixture_git(repo, "commit", "-q", "-m", "policy fixture")
    run_fixture_git(repo, "remote", "add", FIXTURE_REMOTE, repo.as_posix())
    run_fixture_git(repo, "update-ref", f"refs/remotes/{FIXTURE_REMOTE}/main", "HEAD")
    Path(repo, *MIRROR_FILE).write_bytes(policy.render_mirror(repo, "HEAD"))
    return repo, kit


def remove_repo(repo):
    def set_writable(func, path, _exc):
        os.chmod(path, stat.S_IWRITE)
        func(path)
    shutil.rmtree(repo, **({"onexc": set_writable} if sys.version_info >= (3, 12) else {"onerror": set_writable}))


def run_fixture(only=None):
    for var in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GOV_REMOTE", "GOV_DEFAULT_BRANCH"):
        os.environ.pop(var, None)  # the fixture's own repository and remote, whatever the caller exported
    if sys.pycache_prefix is not None:  # TOOL-dGroundRules-52 S15: a prefixed cache read has no `__pycache__` parent to map
        print("policy-fixture: guard-trace · WRONG sys.pycache_prefix is set")
        return 1
    rows = policy.load_catalogue(KIT)
    cases = [c for c in derive_cases(rows) if only in (None, c[0])]
    if not cases:
        print(f"policy-fixture: no case named {only}", file=sys.stderr)
        return 2
    top = derive_source_top()
    if top.parts:  # outside a repository nothing is traced, and the empty trace is check_guard_trace's WRONG
        try:
            git_dirs = read_source_git_dirs(top)
        except RuntimeError as exc:
            print(f"policy-fixture: guard-trace · WRONG: {exc}, so no case ran")
            return 1
        top, tmp = os.path.realpath(top), os.path.realpath(tempfile.gettempdir())
        # a case's directory sits under tempfile's root, so that root holding the source shelters no case
        TRACE_ROOTS[:] = [top, None if os.path.normcase(top).startswith(os.path.normcase(tmp) + os.sep) else tmp, git_dirs]
        sys.addaudithook(add_source_read)
    asserted, wrong = 0, 0
    for name, arm, seed in cases:
        if arm is None:  # an outcome case runs itself
            a, w = seed(name)
            asserted += a
            wrong += w
            continue
        repo, kit = build_repo(rows)
        try:
            files = [kit / policy.CATALOGUE, kit / policy.LIST, kit / budgets.CENSUS, Path(repo, *POLICY_FILE),
                     Path(repo, *MIRROR_FILE), Path(repo, *CONSUMER_FILE)]
            saved = {p: p.read_bytes() for p in files}
            held = set(repo.rglob("*"))
            key, needle = seed(repo, kit, rows)
            _pop, findings = run_arm(arm, repo, kit)
            hit = any(k == key and needle in why for k, why in findings)
            asserted += 1
            wrong += not hit
            print(f"policy-fixture: {name} · " + ("RED as planted" if hit else
                  f"WRONG: no finding names {key} with '{needle}'; it found {findings or 'nothing'}"))
            if name == "summary-new-key":
                # The list never gains a name: `lists --write` over the planted copy leaves it out,
                # and `lists --check` stays red.
                policy.write_list(kit)
                kept = PLANTED in policy.parse_list((kit / policy.LIST).read_text(encoding="utf-8"))
                still = any(k == PLANTED for k, _w in policy.check_list(kit, policy.resolve_compare_base(kit))[0])
                asserted += 2
                wrong += kept + (not still)
                print(f"policy-fixture: {name} · lists --write " + ("WRONG: it added the planted row" if kept else
                      "left the planted row out") + " · lists --check " + ("still red" if still else "WRONG: green"))
            for p, b in saved.items():
                p.write_bytes(b)
            for p in set(repo.rglob("*")) - held:  # a file the seed added is no part of the unplanted copy
                if p.is_file() and ".git" not in p.relative_to(repo).parts:
                    p.unlink()
            _pop, findings = run_arm(arm, repo, kit)
            asserted += 1
            wrong += bool(findings)
            print(f"policy-fixture: {name} · " + (f"WRONG: unplanted reds {findings}" if findings else "green unplanted"))
        finally:
            remove_repo(repo)
    for check in (check_guard_trace, check_guard_lines):
        a, w = check()
        asserted += a
        wrong += w
    print(f"policy-fixture: {asserted} assertion(s) executed · {wrong} wrong")
    return 1 if wrong or not asserted else 0


USAGE = "usage: python check_policy.py [--repo <dir>] | --fixture [--strict-from <dir>] [<case>] | --live"


def main(argv):
    global STRICT_FROM
    if argv == ["--live"]:
        return run_live()
    if argv[:1] == ["--fixture"]:
        rest = argv[1:]
        if rest[:1] == ["--strict-from"] and len(rest) >= 2:
            STRICT_FROM, rest = rest[1], rest[2:]
        if len(rest) <= 1 and rest[:1] != ["--strict-from"]:
            return run_fixture(*rest)
        print(USAGE, file=sys.stderr)
        return 2
    if argv and not (len(argv) == 2 and argv[0] == "--repo"):
        print(USAGE, file=sys.stderr)
        return 2
    repo = argv[1] if argv else (policy.run_git(Path.cwd(), "rev-parse", "--show-toplevel") or "").strip()
    if not repo or not Path(repo).is_dir():
        print(f"policy-check: no repository to grade ({repo or 'the working directory is in none'})", file=sys.stderr)
        return 2
    red = 0
    for arm in ARMS:
        verdict, findings = run_arm(arm, repo, KIT)
        print(f"policy-check: {arm.name} · {verdict}")
        for key, why in findings:
            print(f"  {key}: {why}")
        red += len(findings)
    return 1 if red else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
