"""check_policy.py - the policy kit's arms, run over a repository, and the fixture that proves each
one can red (TOOL-dGroundRules-1).

    python <this kit>/check_policy.py [--repo <dir>]   # every arm in ARMS; exit 0 green, 1 red
    python <this kit>/check_policy.py --fixture [<case>]  # every case, or the one named

`<dir>` defaults to the git top level of the working directory. Each arm prints
`policy-check: <arm> · <n> finding(s) · <population>`, then one line per finding; a population of
zero is a finding, so an arm that read nothing cannot read green.

THE ARMS read the repository's `.governance/policy.toml` and this kit's catalogue and shrink-only
list: `arm_schema` grades each file key with the value check, `arm_shape` audits the catalogue's
rows, `arm_summaries` grades the list as `policy.py lists --check` does, and `arm_direction` reds a
loop bound or deadline row that does not declare `direction = "raise-loosens"` (TOOL-dGroundRules-11).

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
    """Each key of the policy file its catalogue row refuses, and each key no row matches."""
    rows, bad = load_rows(kit)
    if bad:
        return 0, "the catalogue did not parse", [bad]
    path = Path(repo, *POLICY_FILE)
    if not path.is_file():
        return 0, f"{POLICY_REL} is absent, so no key was graded", []
    try:
        doc = tomllib.loads(path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as exc:
        return 0, f"{POLICY_REL} did not parse", [(POLICY_REL, f"does not parse: {exc}")]
    findings, n = [], 0
    for segs, row, value in policy.scan_keys(doc, rows):
        n += 1
        if row is None:
            findings.append((policy.render_dotted(segs), "no catalogue row matches this key"))
            continue
        why = policy.check_value(row, value)
        if why:
            findings.append((policy.render_dotted(segs), why))
    return n, f"{n} key(s) of {POLICY_REL} against {len(rows)} row(s)", findings


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


ARMS = [arm_schema, arm_shape, arm_summaries, arm_direction]


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


USAGE = "usage: python check_policy.py [--repo <dir>] | --fixture [<case>]"


def main(argv):
    if argv[:1] == ["--fixture"] and len(argv) <= 2:
        return run_fixture(*argv[1:])
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
