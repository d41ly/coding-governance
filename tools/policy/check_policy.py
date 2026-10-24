"""check_policy.py - the policy kit's arms, run over a repository, and the fixture that proves each
one can red (TOOL-dGroundRules-1).

    python <this kit>/check_policy.py [--repo <dir>]   # every arm in ARMS; exit 0 green, 1 red
    python <this kit>/check_policy.py --fixture [--strict-from <dir>] [<case>]  # every case, or the one named

`<dir>` defaults to the git top level of the working directory. Each arm prints
`policy-check: <arm> · <n> finding(s) · <population>`, then one line per finding; a population of
zero is a finding, so an arm that read nothing cannot read green.

THE ARMS read the repository's `.governance/policy.toml` and this kit's catalogue and shrink-only
list: `arm_schema` grades each file key with the value check, `arm_shape` audits the catalogue's
rows, `arm_summaries` grades the list as `policy.py lists --check` does, `arm_direction` reds a
loop bound or deadline row that does not declare `direction = "raise-loosens"` (TOOL-dGroundRules-11),
and `arm_on_invalid` reds what `policy.py check` refuses at HEAD (TOOL-dGroundRules-4).
`arm_reader_coverage` reds a catalogue key whose owner build has landed, every spec in its build
folder terminal at the landed revision, and that no call of READER_SHAPES in the tracked code reads
(TOOL-dGroundRules-8); it grades nothing until an owner lands, and says so. The mirror's
three (TOOL-dGroundRules-5): `arm_mirror_parity` reds a working-tree `.governance/policy.json` that
is absent or differs from its render at HEAD; `arm_mirror_landed` reds a key the policy file at the
landed revision sets that the helper `policy-mirror.js` and the reader answer differently, one
`node` call per key; `arm_mirror_readers` reds a tracked code file outside this kit, the memory root
and `help/` that names `policy.json`. `arm_legacy_homes` reds each report `policy.py lists --check`
makes on the legacy-homes list (TOOL-dGroundRules-7).

THE FIXTURE makes one git repository per case under the system temp directory, with a short prefix
because a long path fails a Windows clone: a copy of this kit's catalogue and list at the kit's own
path in its repository, and a policy file at its scaffold, committed, with a remote-tracking ref at
that commit. Each case plants its break on the copy and runs its arm, which must red NAMING the
planted key, then runs the arm again on the unplanted copy, which must be green. Each plant edits a
real shipped row where one serves. WHAT IT DOES NOT CHECK: that the shipped catalogue's values are
v2's, which is the build's acceptance probe, not an arm.

`adopter-fresh-target` is an outcome case, no plant (TOOL-dGroundRules-16): this kit installed into a
fresh `git init` by the deployer, `govkit.py apply` with the closure of its `requires`, run from a
scratch clone whose HEAD commits the working tree under test, so an uncommitted edit is graded
(TOOL-dGroundRules-26), the tool root compared with the receipt both ways (TOOL-dGroundRules-24),
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
and asserts what the helper, a four-line fixture hook and `arm_mirror_landed` answer there.
`mirror-landed-parity` holds the shim's `landed` to `derive_landed_revision` in four ladder states.
`mirror-commit-rewrite` (TOOL-dGroundRules-65) commits the mirror rendered at its parent, rewrites
that commit with `git commit-tree` as the lander does, and reds a `mirror --check` that is not fresh
at either commit, or a helper reading the rewrite that leaves the render's `{rev}` unfilled.
`mirror-landed-merge` (TOOL-dGroundRules-14) replays the lander's landing: a branch's policy change
merged `--no-ff` onto main, the mirror rendered over the merge, the merge rewritten by `commit-tree`
over its parents and pushed as main; it reds a mirror the check, `arm_mirror_parity` or the helper
calls stale at that rewrite.

The `guard-*` cases are outcome cases of the minimal guard (TOOL-dGroundRules-6): each copies
`guard.py`, `guarded-paths.txt` and `policy.py` into the kit copy, commits a policy file capping a
tracked `big.md` and `small.md` and the class row `docs/*/`, stages its plant from `GUARD_PLANTS`, and
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

Later units add arms to ARMS and cases to CASES.
"""
import contextlib
import io
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path

sys.dont_write_bytecode = True  # a gate leg leaves no bytecode cache in an adopter's kit dir
import policy  # noqa: E402  (the module beside this file)

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
    key no row matches (TOOL-dGroundRules-4 re-points this arm through the one judge)."""
    rows, bad = load_rows(kit)
    if bad:
        return 0, "the catalogue did not parse", [bad]
    path = Path(repo, *POLICY_FILE)
    if not path.is_file():
        return 0, f"{POLICY_REL} is absent, so no key was graded", []
    text = path.read_text(encoding="utf-8")
    problems = policy.validate(text, rows)
    if problems and not problems[0].key:
        return 0, f"{POLICY_REL} did not parse", [(POLICY_REL, f"does not parse: {problems[0].why}")]
    n = sum(1 for _ in policy.scan_keys(tomllib.loads(text), rows))
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
    findings, note = policy.check_list(kit)
    return len(rows), f"{len(policy.derive_unsummarised(rows))} of {len(rows)} row(s) unsummarised · {note}", findings


def arm_direction(repo, kit):
    """Each `check_direction` pair; the population is the rows `derive_bounds` selects."""
    rows, bad = load_rows(kit)
    if bad:
        return 0, "the catalogue did not parse", [bad]
    n = len(policy.derive_bounds(rows))
    return n, f"{n} loop bound and deadline row(s)", policy.check_direction(rows)


def arm_on_invalid(repo, kit):
    """The `policy.py check` verdict over the repository's HEAD, the candidate a push lands: its
    Refusal, an invalid policy file with no fallback, is the one finding (TOOL-dGroundRules-4)."""
    try:
        line = policy.check_revision(repo, "HEAD")
    except policy.Refusal as exc:
        return 1, f"{POLICY_REL} at HEAD", [(f"{exc.path}:{exc.line}", exc.why)]
    return 1, line.removeprefix("policy: check · "), []


# ---- the JSON mirror (TOOL-dGroundRules-5) ------------------------------------------------------

MIRROR_FILE = tuple(policy.MIRROR_REL.split("/"))
MIRROR_KIT_FILES = ("policy.py", "policy-mirror.js", "policy-shim.sh")
CODE_PATHSPECS = ("*.js", "*.mjs", "*.cjs", "*.py", "*.sh", ".githooks/*")
MIRROR_REMEDY = "run: python <this kit>/policy.py mirror --write"


def arm_mirror_parity(repo, kit):
    """The working-tree mirror against `policy.render_mirror(repo, "HEAD")`: a mirror that differs,
    named by its first difference, or one absent where this kit is present. A render the reader
    refuses is the one finding."""
    try:
        want = policy.render_mirror(repo, "HEAD")
    except policy.Refusal as exc:
        return 1, f"{policy.MIRROR_REL} against its render at HEAD", [(f"{exc.path}:{exc.line}", exc.why)]
    path = Path(repo, *MIRROR_FILE)
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
    is a finding."""
    try:
        sha, _how = policy.derive_landed_revision(repo)
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


def arm_mirror_readers(repo, kit):
    """Each tracked code file, `*.js`, `*.mjs`, `*.cjs`, `*.py`, `*.sh` and `.githooks/*`, outside this
    kit's directory, the memory root and `help/`, that names `policy.json`: every consumer reads the
    mirror through the helper."""
    skip = tuple(p for p in ((policy.run_git(kit, "rev-parse", "--show-prefix") or "").strip(),
                             read_memory_root(repo) + "/", "help/") if p)
    files = [f for f in (policy.run_git(repo, "ls-files", "-z", "--", *CODE_PATHSPECS) or "").split("\0")
             if f and not f.startswith(skip)]
    out = []
    for f in files:
        try:
            if b"policy.json" in Path(repo, f).read_bytes():
                out.append((f, "names policy.json; read the mirror through policy-mirror.js's readPolicy"))
        except OSError:
            continue
    return len(files), f"{len(files)} tracked code file(s) outside the kit, the memory root and help/", out


def arm_legacy_homes(repo, kit):
    """Each report `policy.py lists --check` makes on the legacy-homes list (TOOL-dGroundRules-7): the
    rows derived from the repository's legacy policy homes against this kit's list and the list at the
    landed revision. A Refusal, an unreadable landed revision or house file, is the one finding."""
    try:
        reports, notes, rows, _new = policy.check_legacy_homes(repo, kit)
    except policy.Refusal as exc:
        return 0, "the legacy homes were not graded", [(f"{exc.path}:{exc.line}", exc.why)]
    population = " · ".join([f"{len(rows)} row(s) derived from the legacy homes", *notes])
    return len(rows), population, [("legacy homes", r) for r in reports]


# ---- reader coverage (TOOL-dGroundRules-8) -----------------------------------------------------

# The reader shapes, one row per consumer shape: (the files the row reads, a suffix or a directory
# ending `/`, and its pattern). Group 2 is the key text the call passes; a new shape is one row.
READER_SHAPES = (
    # a call whose first argument is the key as a string literal: resolve("k"), mirror.get('k')
    ((".py", ".js", ".mjs", ".cjs"),
     re.compile(r"[A-Za-z_$][\w$]*\([ \t]*(?:[fFrRbB]{1,2})?(['\"`])([^'\"`\n]*)\1")),
    # the reader CLI's get: policy.py get k, "$kit/policy.py" get "k" | ...
    ((".sh", ".githooks/"),
     re.compile(r"policy\.py[\"']?[ \t]+get[ \t]+([\"']?)([^\s'\"]+?)\1(?=[ \t;)|&]|$)")),
)
READER_SKIPPED = re.compile(r"(?:^|/)(?:[^/]*\.test\.(?:sh|js)|selftest[^/]*\.py|test_[^/]*\.py)$")
PATTERN_SEGMENT = r"[^'\"`\s.()]+"  # a `*` or `<name>` segment: one run of no quote, space, `.`, `(` or `)`


def derive_landed_owners(repo, kit=KIT):
    """-> the catalogue owners whose build has landed: at the landed revision `policy.py get` reads,
    the build folder `<memory root>/builds/<owner>/spec/` holds at least one spec and every spec's
    status header carries a token in tree_lib's TERMINAL, the memory root read from that revision's
    `.memory-tree.conf`. The landed revision's Refusal passes through; no memory-tree kit beside
    this one reads no build as landed, saying so. A git read that fails is a Refusal naming it."""
    rows = policy.load_catalogue(kit)
    sha, _how = policy.derive_landed_revision(repo)
    try:
        tree_lib = load_tree_lib()
    except (LookupError, ImportError):
        print("reader coverage: no memory-tree kit beside the policy kit, so no build reads as landed")
        return set()
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
                spelled.update(m[2] for rx in shapes for m in rx.finditer(line))
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
    """`check_reader_coverage` over the repository: its population the catalogue's keys joined to the
    landed owners, so a graded count of 0 is the announce line it prints, never a finding. A Refusal,
    a landed revision or landed build that does not read, is the one finding."""
    rows, bad = load_rows(kit)
    if bad:
        return 0, "the catalogue did not parse", [bad]
    try:
        n, findings = check_reader_coverage(repo, kit=kit)
    except policy.Refusal as exc:
        return len(rows), "no landed revision to join the owners to", [(f"{exc.path}:{exc.line}", exc.why)]
    return (len(rows), f"{n} of {len(rows)} catalogue key(s) graded for a reader",
            [tuple(f.split(": ", 1)) for f in findings])


ARMS = [arm_schema, arm_shape, arm_summaries, arm_direction, arm_on_invalid, arm_mirror_parity,
        arm_mirror_landed, arm_mirror_readers, arm_legacy_homes, arm_reader_coverage]


def run_arm(arm, repo, kit):
    """-> (population, findings), a zero population being one more finding."""
    n, population, findings = arm(repo, kit)
    if n == 0:
        findings = findings + [("population", f"zero, so this arm graded nothing: {population}")]
    return population, findings


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


# The kit-dir resolver, INLINED byte-identically from the canonical copy named on its marker line and
# gated by the resolve-python self-test: a kit may not import a sibling.
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


def load_tree_lib():
    """The memory-tree kit's `tree_lib`, its directory found by `resolve_kit_dir` from this kit -> the
    module; LookupError where no memory-tree kit is installed, ImportError where it does not import."""
    lib = str(resolve_kit_dir("memory-tree", "tree_lib.py", KIT))
    if lib not in sys.path:
        sys.path.insert(0, lib)
    import tree_lib
    return tree_lib


def resolve_bash():
    """The bash sharing this filesystem, by path, or None: on Windows the bare name reaches the
    System32 WSL launcher before PATH (gotcha subprocess-resolves-a-different-shell). GOV_BASH
    overrides; a candidate is taken only if it runs."""
    override = os.environ.get("GOV_BASH")
    cands = [override] if override else [
        p for d in os.environ.get("PATH", "").split(os.pathsep) for p in (os.path.join(d, "bash.exe"), os.path.join(d, "bash"))
        if os.path.isfile(p) and not any(s in p.replace("\\", "/").lower() for s in ("/system32/", "/windowsapps/"))]
    for cand in cands:
        try:
            if subprocess.run([cand, "-c", ":"], capture_output=True).returncode == 0:
                return cand
        except OSError:
            pass
    return None


def extract_arm_rows(text):
    """The backticked first-column names of the README's "Each arm in an adopter" table, in order."""
    parts = text.replace("\r", "").split(f"\n## {ADOPTER_SECTION}\n", 1)
    section = parts[1].split("\n## ", 1)[0] if len(parts) == 2 else ""
    return re.findall(r"^\| `([^`]+)` \|", section, flags=re.M)


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


def build_source_snapshot(source_root):
    """The root of a scratch clone whose HEAD commits `source_root`'s working tree over its HEAD
    (TOOL-dGroundRules-26). The deployer installs its own checkout's HEAD, never a working tree, so a
    case that installs through the clone's `govkit.py` grades the bytes under test, a file only the
    working tree holds included. `--shared` reads the source's objects through alternates, and with
    GIT_DIR set to the clone every new object lands in the clone's store, never the source's. `add -A`
    runs over a copy of the source's index with the source as work tree, so the source's ignore rules
    decide what counts and a file whose stat matches is not re-hashed. Every git call runs with the
    memory-tree kit's GIT_ENV_LEAKS stripped, so an ambient GIT_DIR or GIT_INDEX_FILE cannot retarget
    it. The caller removes the root. -> Path; RuntimeError naming the failed step and git's first
    stderr line, the clone already removed."""
    try:
        leaks = load_tree_lib().GIT_ENV_LEAKS
    except LookupError as exc:
        raise RuntimeError(f"no GIT_ENV_LEAKS to strip: {exc}") from None
    base = {k: v for k, v in os.environ.items() if k not in leaks}

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
        held = source / run("index", "-C", source.as_posix(), "rev-parse", "--git-path", "index")
        if held.is_file():  # a source with no index yet starts the snapshot from an empty one
            shutil.copyfile(held, index)
        env = {"GIT_DIR": (s / ".git").as_posix(), "GIT_WORK_TREE": source.as_posix(), "GIT_INDEX_FILE": index.as_posix()}
        run("add", "add", "-A", cwd=source, **env)
        tree = run("write-tree", "write-tree", **env)
        commit = run("commit-tree", "commit-tree", tree, "-p", "HEAD", "-m", "the working tree under test", **env)
        run("checkout", "-C", s.as_posix(), "checkout", "--quiet", "--detach", commit)
    except BaseException:
        remove_repo(s)
        raise
    return s


def run_fresh_target(name):
    """This kit installed by the deployer into a fresh target: `git init` with a pinned autocrlf, a
    one-line README and a `.governance/deploy.toml`, committed once, then `govkit.py apply` with this
    kit's id and the closure of its kit.toml `requires` (TOOL-dGroundRules-24), run from
    `build_source_snapshot`'s clone of the tree under test, which the descriptor's `gov_source` names
    and whose commit the case prints over the source's HEAD (TOOL-dGroundRules-26). Every file under the
    target's tool root must be a receipt row's `path`, and every engine or seed row's `path` must
    exist. Then the installed `adopt-policy.sh`, found through its receipt row: `--scaffold`, and
    `--check` with the install staged and again once it is committed, each exiting 0 with every arm
    graded clean or announced; and the README's table joined to ARMS both ways. A missing `govkit.py`
    or a refused `apply` is a WRONG, and nothing after it runs. Prints its lines. -> (assertions, wrong)."""
    names = [a.__name__ for a in ARMS]
    listed = extract_arm_rows((KIT / "README.md").read_text(encoding="utf-8"))
    wrong = [f"{n} is in ARMS with no row in README.md \"{ADOPTER_SECTION}\" (unlisted)" for n in names if n not in listed]
    wrong += [f"README.md \"{ADOPTER_SECTION}\" lists {n}, which ARMS lacks (stale)" for n in listed if n not in names]
    asserted = len(set(names) | set(listed)) + 2
    bash = resolve_bash()
    desc = tomllib.loads((KIT / "kit.toml").read_text(encoding="utf-8"))
    ids, todo = [desc["id"]], list(desc.get("requires", []))
    # ponytail: `requires` names kit ids and is read as each kit's home, which they equal for every
    # kit gov homes under its own id; a kit homed elsewhere is a WRONG naming it, never a skip.
    while todo:
        home = todo.pop(0)
        if home in ids:
            continue
        ids.append(home)
        try:
            todo += tomllib.loads((resolve_kit_dir(home, "kit.toml", KIT) / "kit.toml").read_text(encoding="utf-8")).get("requires", [])
        except LookupError as exc:
            wrong.append(f"kit.toml requires {home}, which this tree does not resolve: {exc}")
    root = KIT.parent  # this kit's own resolved tool root; the target's prefix is its name, never spelled
    govkit = root / "govkit" / "govkit.py"
    top = (policy.run_git(KIT, "rev-parse", "--show-toplevel", "--show-prefix") or "").split("\n")
    rows, s = None, None
    t = Path(tempfile.mkdtemp(prefix="pol-"))
    try:
        if not govkit.is_file():
            wrong.append(f"no deployer to install with: looked for govkit.py at {govkit.as_posix()}, under this kit's tool root")
        elif len(top) < 2 or not top[0]:
            wrong.append(f"no tree under test to snapshot: {KIT.as_posix()} is in no git repository")
        else:
            try:
                s = build_source_snapshot(top[0])
            except (RuntimeError, OSError) as exc:
                wrong.append(f"nothing was installed to grade: {exc}")
        if s is not None:
            snap, over = (policy.run_git(s, "rev-parse", "HEAD", "HEAD^") or "? ?").split()
            print(f"{name}: installing from snapshot {snap[:8]} of the working tree over HEAD {over[:8]}")
            govkit = s / Path(top[1]).parent / "govkit" / "govkit.py"  # the clone's own deployer installs its HEAD
            run_fixture_git(t, "init", "-q")
            run_fixture_git(t, "config", "core.autocrlf", "false")
            (t / "README.md").write_text("A fresh adopter of the policy kit.\n", encoding="utf-8", newline="\n")
            Path(t, POLICY_FILE[0]).mkdir()
            Path(t, POLICY_FILE[0], "deploy.toml").write_text(
                f'gov_source = {json.dumps(s.as_posix())}\nprefix = {json.dumps(root.name)}\nkits = {json.dumps(ids)}\n',
                encoding="utf-8", newline="\n")
            run_fixture_git(t, "add", "-A")
            run_fixture_git(t, "commit", "-q", "-m", "a fresh target")
            p = subprocess.run([sys.executable, str(govkit), "apply", "--target", t.as_posix(), "--kits", ",".join(ids)],
                               capture_output=True, text=True, encoding="utf-8", errors="replace",
                               env=dict(os.environ, GOVKIT_NO_REMOTE_PROBE="1"))
            if p.returncode:
                wrong.append(f"govkit.py apply --kits {','.join(ids)} exited {p.returncode}, so nothing was installed "
                             f"to grade: {(p.stdout + p.stderr).strip()}")
            else:
                rows = [r for r in json.loads(Path(t, POLICY_FILE[0], "install.json").read_text(encoding="utf-8")).get("files") or []
                        if isinstance(r, dict)]
        if rows is not None:
            paths = {r.get("path") for r in rows}
            held = sorted(f.relative_to(t).as_posix() for f in (t / root.name).rglob("*") if f.is_file())
            owed = [r["path"] for r in rows if r.get("role") in ("engine", "seed")]
            stray = [f"{f} is under the tool root and is no receipt row's path (stray)" for f in held if f not in paths]
            stray += [f"{f} is an engine or seed row of the receipt and is absent from the target (missing)"
                      for f in owed if not Path(t, f).is_file()]
            asserted += len(held) + len(owed)
            wrong += stray
            if not stray:
                print(f"policy-fixture: {name} · apply --kits {','.join(ids)} exited 0 into its target · the "
                      f"{len(held)} file(s) under {root.name}/ are each a receipt row's path, and its {len(owed)} "
                      f"engine or seed row(s) are each present · no stray or missing receipt path")
            adopter = next((r["path"] for r in rows if r.get("kit") == desc["id"]
                            and str(r.get("path")).endswith("/adopt-policy.sh")), None)
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
                rc, out = run_adopter("--scaffold")
                if rc:
                    wrong.append(f"--scaffold exited {rc}: {out.strip()}")
                for phase in ("with the install staged", "once the install is committed"):
                    if phase.startswith("once"):
                        run_fixture_git(t, "add", "-A")
                        run_fixture_git(t, "commit", "-q", "-m", "install the policy kit")
                    rc, out = run_adopter("--check")
                    bad = check_arm_lines(out, names)
                    asserted += len(names) + 1
                    wrong += [f"{phase}: {b}" for b in bad]
                    if rc:
                        wrong.append(f"{phase}: --check exited {rc}" + ("" if bad else f": {out.strip()}"))
    finally:
        remove_repo(t)
        if s is not None:
            remove_repo(s)
    for w in wrong:
        print(f"policy-fixture: {name} · WRONG: {w}")
    if not wrong:
        print(f"policy-fixture: {name} · every arm graded clean or announced, with the install staged and "
              f"once it is committed · the README table names exactly the {len(names)} arm(s) of ARMS")
    return asserted, len(wrong)


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
        for f in ("policy.py", policy.CATALOGUE):
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


# ---- the JSON mirror (TOOL-dGroundRules-5) ------------------------------------------------------

AGENTS_KEY = "runtime.agents-in-flight"
CONSUMER_FILE = ("hooks", "consumer.js")
CONSUMER_TEXT = ("// A consumer outside the policy kit: it reads policy through the helper, never the file itself.\n"
                 "const { readPolicy } = require(@helper@);\n"
                 f"module.exports = () => readPolicy({json.dumps(AGENTS_KEY)}).value;\n")
DIRECT_READER = 'module.exports = () => JSON.parse(require("fs").readFileSync(".governance/policy.json", "utf8"));\n'
# The fixture hook: four lines of Node that require the helper, read the limit, and refuse a request above it.
FIXTURE_HOOK = ("const { readPolicy } = require(@helper@);\n"
                f"const limit = readPolicy({json.dumps(AGENTS_KEY)}, {{ repo: __dirname }}).value;\n"
                "const asked = 3;\n"
                "process.exit(asked > limit ? 2 : 0);\n")
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
    return "/".join(CONSUMER_FILE), "names policy.json"


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
            Path(repo, "hook.js").write_text(FIXTURE_HOOK.replace("@helper@", json.dumps(str(kit / "policy-mirror.js"))),
                                             encoding="utf-8", newline="\n")
            checks += [check_run(at_l, "the fixture hook asked for 3", ["node", str(repo / "hook.js")],
                                 lambda rc, o, e: rc == 2, cwd=repo),
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
            cli = [sys.executable, str(kit / "policy.py"), "mirror"]
            checks.append(check_run("A", "policy.py mirror --write", cli + ["--write"],
                                    lambda rc, o, e: rc == 0 and o.startswith("policy: mirror written"), cwd=repo))
            run_fixture_git(repo, "add", "--", policy.MIRROR_REL)
            run_fixture_git(repo, "commit", "-q", "-m", "the mirror, rendered at its parent")
            b = run_fixture_git(repo, "rev-parse", "HEAD")
            parents = run_fixture_git(repo, "rev-parse", "HEAD^@").split()
            rewrite = run_fixture_git(repo, "commit-tree", f"{b}^{{tree}}", *(a for p in parents for a in ("-p", p)),
                                      "-m", "the mirror, rewritten by commit-tree")
            checks.append(("B'", "a new commit over B's tree and parents", rewrite != b, f"B {b[:8]} · B' {rewrite[:8]}"))
            for at, sha in (("B, the commit carrying the mirror", b), ("B', its commit-tree rewrite", rewrite)):
                run_fixture_git(repo, "reset", "-q", "--hard", sha)
                checks.append(check_run(at, "policy.py mirror --check", cli + ["--check"],
                                        lambda rc, o, e: rc == 0 and o == "policy: mirror fresh\n", cwd=repo))
            run_fixture_git(repo, "push", "-q", FIXTURE_REMOTE, "main")
            checks.append(check_run("B' landed as L", what + " --explain", helper + ["--explain"], lambda rc, o, e:
                                    rc == 0 and f"at {rewrite[:8]}, the landed revision" in e and "{rev}" not in e))
        elif name == "mirror-landed-merge":
            # The landing's order (TOOL-dGroundRules-14), as push-main.sh --prepare runs it: b merged
            # --no-ff onto main detached, the mirror regenerated over the merge, the merge rewritten by
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
        ok = named if name == "mirror-stale-refuse" else not findings
        checks.append((at_l, "arm_mirror_landed", ok, f"{len(findings)} finding(s) · "
                       + ("; ".join(f"{k}: {w}" for k, w in findings) or population)))
    finally:
        remove_repo(repo)
        remove_repo(bare)
    asserted, wrong = print_checks(name, checks)
    if name == "mirror-landed-merge" and not wrong:
        print(f"policy-fixture: {name} · fresh at the rewrite")
    return asserted, wrong


def run_mirror_landed_parity(name):
    """The shim's `landed` against the reader's `derive_landed_revision` in four ladder states, each
    remote's main a different commit: two remotes with GOV_REMOTE naming the second; two without;
    one remote; no remote. The same sha, or both refusing, in each."""
    bash = resolve_bash()
    if bash is None:
        print(f"policy-fixture: {name} · WRONG: no bash on PATH shares this filesystem; set GOV_BASH")
        return 1, 1
    repo, kit, bare = build_landed_repo(policy.load_catalogue(KIT))
    checks = []
    try:
        run_fixture_git(repo, "push", "-q", FIXTURE_REMOTE, "main")
        run_fixture_git(repo, "remote", "add", FIXTURE_SECOND, repo.as_posix())
        run_fixture_git(repo, "update-ref", f"refs/remotes/{FIXTURE_SECOND}/main", "HEAD~1")
        for state, drop, gov in (("two remotes, GOV_REMOTE", None, FIXTURE_SECOND), ("two remotes", None, None),
                                 ("one remote", FIXTURE_SECOND, None), ("no remote", FIXTURE_REMOTE, None)):
            if drop:
                run_fixture_git(repo, "remote", "remove", drop)
            if gov:
                os.environ["GOV_REMOTE"] = gov
            try:
                want, why = policy.derive_landed_revision(repo)[0], ""
            except policy.Refusal as exc:
                want, why = None, exc.why
            finally:
                os.environ.pop("GOV_REMOTE", None)
            checks.append(check_run(
                state, f"policy-shim.sh landed against derive_landed_revision ({want[:8] if want else 'refused: ' + why})",
                [bash, (kit / "policy-shim.sh").as_posix(), "landed"],
                lambda rc, o, e, want=want: rc == 0 and o.strip() == want if want else rc == 2 and not o and e.startswith("policy: refused · "),
                cwd=repo, env={**os.environ, **({"GOV_REMOTE": gov} if gov else {})}))
    finally:
        remove_repo(repo)
        remove_repo(bare)
    return print_checks(name, checks)


# ---- the minimal guard (TOOL-dGroundRules-6) ----------------------------------------------------

GUARD_FILES = ("guard.py", "guarded-paths.txt", "policy.py")  # policy.py: the mirror shape's `mirror --print`
GUARD_MIRROR = ("guard-mirror-render", "guard-mirror-beside-catalogue", "guard-mirror-branch-green")
DEPLOY_REL = ".governance/deploy.toml"
DECISIONS_REL = "memory/DECISIONS.md"
GUARD_POLICY = '[budgets]\n"big.md" = 100\n"small.md" = 50\n"docs/*/" = 10\n'
BIG, SMALL, CLASS = '"big.md" = 100\n', '"small.md" = 50\n', '"docs/*/" = 10\n'
RAISED = (POLICY_REL, lambda t: t.replace(BIG, '# RAISED 100 -> 120, 2026-10-23, TOOL-x-1, measured 118 bytes\n'
                                                 '"big.md" = 120\n'))
UNARGUED = (POLICY_REL, lambda t: t.replace(BIG, '"big.md" = 120\n'))
ROW = (DECISIONS_REL, lambda t: t + "- TOOL-x-1 · big.md raised to 120\n")
NO_RAISED, NO_ROW = "no RAISED", f"no {DECISIONS_REL} row"
# case -> [(scenario, [(path, edit of its text, "" when absent)], the exit wanted, needles stdout
# must carry, needles it must not)]; each scenario is staged alone over a fresh commit.
GUARD_PLANTS = {
    "guard-admits-raise": [("raise", [RAISED, ROW], 0, ["policy-guard: admitted · budgets.\"big.md\" 100 -> 120"], [])],
    "guard-lowered": [("lowered", [(POLICY_REL, lambda t: t.replace(BIG, '# RAISED 100 -> 90\n"big.md" = 90\n')), ROW],
                       1, ["a lowering"], [])],
    "guard-two-raised": [("two raised", [RAISED, (POLICY_REL, lambda t: t.replace(SMALL, '# RAISED 50 -> 60\n'
                                                                                   '"small.md" = 60\n')), ROW],
                          1, ["2 keys changed"], [])],
    "guard-class-row": [("class row", [(POLICY_REL, lambda t: t.replace(CLASS, '# RAISED 10 -> 20\n"docs/*/" = 20\n')),
                                       ROW], 1, ["not a measured-file cap"], [])],
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
                       1, ["a key was added"], [])],
    "guard-removed-row": [("removed row", [(POLICY_REL, lambda t: t.replace(SMALL, "")), ROW],
                           1, ["a key was removed"], [])],
}


def build_guard_repo():
    """build_repo's fixture with guard.py and its list copied beside the catalogue, a tracked big.md and
    small.md, a deploy.toml, a decision log holding one row, and a policy file whose [budgets] table
    sets "big.md" = 100, "small.md" = 50 and "docs/*/" = 10, all committed. -> (repo, kit copy)."""
    repo, kit = build_repo(policy.load_catalogue(KIT))
    for f in GUARD_FILES:
        (kit / f).write_bytes((KIT / f).read_bytes().replace(b"\r\n", b"\n"))
    for rel, text in (("big.md", "big\n"), ("small.md", "small\n"), (DEPLOY_REL, 'deployer = "fixture"\n'),
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
            want, needle = (1, "commit the policy file or catalogue first") if beside else (0, "equals its render at HEAD")
            checks.append(check_run("the mirror staged" + (" beside the row" if beside else " alone"), "guard.py --staged",
                                    guard, lambda rc, o, e: rc == want and needle in o, cwd=repo))
            if name == "guard-mirror-branch-green":
                run_fixture_git(repo, "commit", "-q", "-m", "the mirror, regenerated")
                checks.append(check_get("the mirror committed", repo, ["--check"], lambda rc, o, e: rc == 0
                                        and o == "policy: mirror fresh\n", kit=kit, verb="mirror"))
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
LEGACY_CASES = ("today", "planted-row", "growth", "shrink", "retrofit", "unmarked", "absent-homes")


def build_legacy_repo(t, gate, house):
    """A repository at `t`/r holding a copy of this kit's policy.py, catalogue and summary list at the
    kit's own path, a `.unattended.conf`, the gate file's text `gate` (none where None) and, where
    `house`, a house file where the copy resolves HOUSE_HOME; committed on main and pushed to one bare
    remote, then the copy's `lists --write` seeding the legacy list, committed and pushed, so the
    landed list is that seed. -> the kit copy."""
    repo = t / "r"
    kit = repo / (policy.run_git(KIT, "rev-parse", "--show-prefix") or "").strip()  # derived, never spelled
    kit.mkdir(parents=True)
    for f in ("policy.py", policy.CATALOGUE, policy.LIST):
        (kit / f).write_bytes((KIT / f).read_bytes().replace(b"\r\n", b"\n"))
    homes = {repo / ".unattended.conf": LEGACY_CONF}
    if gate is not None:
        homes[Path(repo, policy.GATE_FILE)] = gate
    if house:
        homes[policy.resolve_tool_home(policy.HOUSE_HOME, kit)] = LEGACY_HOUSE
    for path, text in homes.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")
    run_fixture_git(t, "init", "-q", "--bare", "b.git")
    run_fixture_git(repo, "init", "-q")
    run_fixture_git(repo, "symbolic-ref", "HEAD", "refs/heads/main")
    run_fixture_git(repo, "remote", "add", FIXTURE_REMOTE, (t / "b.git").as_posix())
    for msg in ("the legacy homes", "the legacy list, seeded"):
        if msg.endswith("seeded"):
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
    file, green with one announce line for each."""
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


def build_reader_coverage_repo(t, name):
    """The case's repository at `t`/r on main: the kit copy at this kit's own path holding a catalogue
    of the case's rows, the planted spec with its landed token, and the planted files, committed and
    pushed to one bare remote, so the landed revision is that commit; then the spec's working-tree
    token written over it. -> the kit copy."""
    rows, at_landing, in_tree, plants, _red, _n = RC_CASES[name]
    repo = t / "r"
    kit = repo / (policy.run_git(KIT, "rev-parse", "--show-prefix") or "").strip()  # derived, never spelled
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


CASES = [
    ("shape-no-empty", arm_shape, seed_no_empty),
    ("shape-unknown-field", arm_shape, seed_unknown_field),
    ("usage-out-of-set", arm_shape, seed_usage_out_of_set),
    ("summary-new-key", arm_summaries, seed_summary_new_key),
    ("usage-new-key", arm_summaries, seed_usage_new_key),
    ("list-grew", arm_summaries, seed_list_grew),
    ("direction-missing", arm_direction, seed_direction_missing),
    ("direction-new-bound", arm_direction, seed_direction_new_bound),
    ("direction-wrong-value", arm_direction, seed_direction_wrong_value),
    (FRESH_TARGET, None, run_fresh_target),  # an outcome case: no plant and no one arm
    ("reader-landed", None, run_reader_landed),  # outcome cases: the reader over its own repositories
    ("reader-parsed", None, run_reader_parsed),
    ("resolution-order", None, run_resolution_order),
    ("on-invalid-classes", None, run_on_invalid_classes),
    ("on-invalid-strict", None, run_on_invalid_strict),
    ("mirror-hand-edited", arm_mirror_parity, seed_mirror_hand_edited),
    ("mirror-absent", arm_mirror_parity, seed_mirror_absent),
    ("mirror-direct-reader", arm_mirror_readers, seed_mirror_direct_reader),
    ("mirror-worktree-loosened", None, run_mirror_landed),  # outcome cases: the helper over a landed L
    ("mirror-stale-last-valid", None, run_mirror_landed),
    ("mirror-stale-refuse", None, run_mirror_landed),
    ("mirror-absent-refuse", None, run_mirror_landed),
    ("mirror-commit-rewrite", None, run_mirror_landed),
    ("mirror-landed-merge", None, run_mirror_landed),
    ("mirror-landed-parity", None, run_mirror_landed_parity),
    *((g, None, run_guard_case) for g in [*GUARD_PLANTS, "guard-merge-side", *GUARD_MIRROR]),  # outcome cases: guard.py --staged
    ("legacy-homes", None, run_legacy_homes),  # an outcome case: one planted repository per case
    ("reader-coverage", None, run_reader_coverage),  # an outcome case: one planted repository per case
]


def derive_cases(rows):
    """One `schema-empty-<name>` case per never-empty row of the shipped catalogue, then CASES."""
    return [(f"schema-empty-{r['name']}", arm_schema, seed_empty_value(r)) for r in rows if r.get("empty") == "never"] + CASES


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
    for name in (policy.CATALOGUE, policy.LIST):
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
    rows = policy.load_catalogue(KIT)
    cases = [c for c in derive_cases(rows) if only in (None, c[0])]
    if not cases:
        print(f"policy-fixture: no case named {only}", file=sys.stderr)
        return 2
    asserted, wrong = 0, 0
    for name, arm, seed in cases:
        if arm is None:  # an outcome case runs itself
            a, w = seed(name)
            asserted += a
            wrong += w
            continue
        repo, kit = build_repo(rows)
        try:
            files = [kit / policy.CATALOGUE, kit / policy.LIST, Path(repo, *POLICY_FILE), Path(repo, *MIRROR_FILE),
                     Path(repo, *CONSUMER_FILE)]
            saved = {p: p.read_bytes() for p in files}
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
                still = any(k == PLANTED for k, _w in policy.check_list(kit)[0])
                asserted += 2
                wrong += kept + (not still)
                print(f"policy-fixture: {name} · lists --write " + ("WRONG: it added the planted row" if kept else
                      "left the planted row out") + " · lists --check " + ("still red" if still else "WRONG: green"))
            for p, b in saved.items():
                p.write_bytes(b)
            _pop, findings = run_arm(arm, repo, kit)
            asserted += 1
            wrong += bool(findings)
            print(f"policy-fixture: {name} · " + (f"WRONG: unplanted reds {findings}" if findings else "green unplanted"))
        finally:
            remove_repo(repo)
    print(f"policy-fixture: {asserted} assertion(s) executed · {wrong} wrong")
    return 1 if wrong or not asserted else 0


USAGE = "usage: python check_policy.py [--repo <dir>] | --fixture [--strict-from <dir>] [<case>]"


def main(argv):
    global STRICT_FROM
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
        population, findings = run_arm(arm, repo, KIT)
        print(f"policy-check: {arm.__name__} · {len(findings)} finding(s) · {population}")
        for key, why in findings:
            print(f"  {key}: {why}")
        red += len(findings)
    return 1 if red else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
