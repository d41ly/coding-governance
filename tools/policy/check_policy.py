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

THE FIXTURE makes one git repository per case under the system temp directory, with a short prefix
because a long path fails a Windows clone: a copy of this kit's catalogue and list at the kit's own
path in its repository, and a policy file at its scaffold, committed, with a remote-tracking ref at
that commit. Each case plants its break on the copy and runs its arm, which must red NAMING the
planted key, then runs the arm again on the unplanted copy, which must be green. Each plant edits a
real shipped row where one serves. WHAT IT DOES NOT CHECK: that the shipped catalogue's values are
v2's, which is the build's acceptance probe, not an arm.

`adopter-fresh-target` is an outcome case, no plant (TOOL-dGroundRules-16): this kit installed into a
fresh `git init` by a copy, `--scaffold`, then `--check` before and after the first commit, where every
arm must grade clean or announce; and the README's "Each arm in an adopter" table joined to ARMS both
ways. Green on a correct build; its RED is an arm that finds a problem in an adopter's tree.

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

Later units add arms to ARMS and cases to CASES.
"""
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


ARMS = [arm_schema, arm_shape, arm_summaries, arm_direction, arm_on_invalid]


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


def run_fresh_target(name):
    """This kit and each kit its kit.toml `requires` copied into a fresh `git init` at their own paths,
    as an install places them; `--scaffold`, then `--check` before the first commit and after it, each
    exiting 0 with every arm graded clean or announced; and the README's table joined to ARMS both
    ways. Prints its lines. -> (assertions, wrong)."""
    names = [a.__name__ for a in ARMS]
    listed = extract_arm_rows((KIT / "README.md").read_text(encoding="utf-8"))
    wrong = [f"{n} is in ARMS with no row in README.md \"{ADOPTER_SECTION}\" (unlisted)" for n in names if n not in listed]
    wrong += [f"README.md \"{ADOPTER_SECTION}\" lists {n}, which ARMS lacks (stale)" for n in listed if n not in names]
    asserted = len(set(names) | set(listed)) + 1
    bash = resolve_bash()
    t = Path(tempfile.mkdtemp(prefix="pol-"))
    try:
        run_fixture_git(t, "init", "-q")
        kits = [KIT]
        # ponytail: `requires` names kit ids and is read as each kit's home, which they equal for every
        # kit gov homes under its own id; a kit homed elsewhere is a WRONG naming it, never a skip.
        for home in tomllib.loads((KIT / "kit.toml").read_text(encoding="utf-8")).get("requires", []):
            try:
                kits.append(resolve_kit_dir(home, "kit.toml", KIT))
            except LookupError as exc:
                wrong.append(f"kit.toml requires {home}, which this tree does not resolve: {exc}")
        rels = {d: (policy.run_git(d, "rev-parse", "--show-prefix") or "").strip() for d in kits}  # derived, never spelled
        for d, rel in rels.items():
            shutil.copytree(d, t / rel, dirs_exist_ok=True, ignore=shutil.ignore_patterns("__pycache__"))
        adopter = (t / rels[KIT] / "adopt-policy.sh").as_posix()
        if bash is None:
            wrong.append("no bash on PATH shares this filesystem: each was a System32 or WindowsApps launcher, "
                         "or none ran; set GOV_BASH")
        else:
            def run_adopter(mode):
                p = subprocess.run([bash, adopter, mode, "--target", t.as_posix()],
                                   capture_output=True, text=True, encoding="utf-8", errors="replace")
                return p.returncode, p.stdout + p.stderr
            rc, out = run_adopter("--scaffold")
            if rc:
                wrong.append(f"--scaffold exited {rc}: {out.strip()}")
            for phase in ("before the first commit", "after the first commit"):
                if phase.startswith("after"):
                    (t / "README.md").write_text("A fresh adopter of the policy kit.\n", encoding="utf-8", newline="\n")
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
    for w in wrong:
        print(f"policy-fixture: {name} · WRONG: {w}")
    if not wrong:
        print(f"policy-fixture: {name} · every arm graded clean or announced, before and after the first "
              f"commit · the README table names exactly the {len(names)} arm(s) of ARMS")
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


def check_get(scenario, repo, args, want, env=None, kit=KIT, verb="get"):
    """`<kit>/policy.py <verb> <args>` run in `repo` -> (scenario, what, ok, what it observed), `want`
    judging (exit code, stdout, stderr), CR stripped."""
    p = subprocess.run([sys.executable, str(kit / "policy.py"), verb, *args], cwd=repo, env=env,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    out, err = p.stdout.replace("\r", ""), p.stderr.replace("\r", "")
    seen = f"exit {p.returncode} · stdout {out.strip() or '(none)'!r} · stderr {err.strip() or '(none)'!r}"
    return scenario, f"{verb} " + " ".join(args), want(p.returncode, out, err), seen


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
]


def derive_cases(rows):
    """One `schema-empty-<name>` case per never-empty row of the shipped catalogue, then CASES."""
    return [(f"schema-empty-{r['name']}", arm_schema, seed_empty_value(r)) for r in rows if r.get("empty") == "never"] + CASES


def run_fixture_git(repo, *args):
    subprocess.run(["git", "-C", str(repo), "-c", "user.name=policy-fixture", "-c", "user.email=policy-fixture@invalid",
                    "-c", "commit.gpgsign=false", *args], check=True, capture_output=True)


def build_repo(rows):
    """A committed copy of this kit's catalogue and list at the kit's own path, the scaffold beside it,
    and a remote-tracking ref at that commit. -> (repo, kit copy)."""
    repo = Path(tempfile.mkdtemp(prefix="pol-"))
    prefix = (policy.run_git(KIT, "rev-parse", "--show-prefix") or "").strip()  # derived, never spelled
    kit = repo / prefix if prefix else repo
    kit.mkdir(parents=True, exist_ok=True)
    for name in (policy.CATALOGUE, policy.LIST):
        (kit / name).write_bytes((KIT / name).read_bytes().replace(b"\r\n", b"\n"))
    Path(repo, POLICY_FILE[0]).mkdir()
    Path(repo, *POLICY_FILE).write_bytes(policy.render_scaffold(rows).encode("utf-8"))
    run_fixture_git(repo, "init", "-q")
    run_fixture_git(repo, "symbolic-ref", "HEAD", "refs/heads/main")
    run_fixture_git(repo, "add", "-A")
    run_fixture_git(repo, "commit", "-q", "-m", "policy fixture")
    run_fixture_git(repo, "remote", "add", FIXTURE_REMOTE, repo.as_posix())
    run_fixture_git(repo, "update-ref", f"refs/remotes/{FIXTURE_REMOTE}/main", "HEAD")
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
            files = [kit / policy.CATALOGUE, kit / policy.LIST, Path(repo, *POLICY_FILE)]
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
