#!/usr/bin/env python3
"""guard.py — the policy file's guard: its commit verdict, its push arm and the expansion rule (TOOL-dDeclaredLoop-2).

    python guard.py --staged                      # the pre-commit block's verdict, from the top level
    python guard.py --push-range <base>..<tip>    # the pre-push arm over a default-branch update
    python guard.py --fixture --plant <case>
    python guard.py --selftest

THE VERDICT, `check_staged`. The pre-commit block runs it only when a path the policy kit's
`guarded-paths.txt` lists at HEAD is staged and standard error is no terminal, so every call is an
agent's commit. It wraps dGroundRules-6's minimal guard, the policy kit's `guard.py`, found through
`read_policy_kit`, and copies none of it. In order:

1. The touch set, the minimal guard's `read_guarded_paths` met with the staged names, less a merge's
   parent sides. Empty: exit 0.
2. Guard-self, at `floor.guard-self` `on`: a staged change of the list file, or of a leaf of
   `policy-file.guard`, `policy-file.proof` or `floor`, is refused naming the key and `floor.guard-self`
   unless the minimal guard's `check_run_mandate` admits the branch: the live run's admission precedes
   it, the owner's 2026-11-12 ruling. No value of `policy-file.guard` admits such a change off a live
   run's branch.
3. Record, at `floor.record-changes` `on`: each changed leaf needs a staged change record whose `Unit` is
   the leaf's row tag, `policy.<row name>` or a family tag such as `policy.budgets`, and a staged
   change of the list file one whose `Unit` is `kit.policy`. Each missing one is refused, naming it.
4. The value's rule, `resolve("policy-file.guard")` at the landed revision, never the staged file, so a
   commit cannot loosen the rule that judges it. `owner-only` and `agents-within-mandate` admit where
   the minimal guard, run as a subprocess so its exit cannot end this one mid-step, exits 0: one cap
   raised with its RAISED line and decision row, the mirror's render, or a live run's branch.
   `agents-with-reason` also admits a change touching the policy file alone with a decision row.
5. Each refusal prints `loop-guard: refused · <path> · <why>` and the remedy; an admission prints
   `loop-guard: admitted · <rule>`; the minimal guard's own lines pass through.

THE PUSH ARM, `check_push_range`. Every non-merge commit of the range, read through the memory-tree
kit's `read_commits` with the key `Gov-Policy`, whose parent holds the policy file and whose own
blob of it differs, is graded leaf by leaf: each changed leaf owes one trailer line
`Gov-Policy: policy.<key> <old> -> <new>`, the key spelled by `render_dotted` and each value compact
JSON, `none` for a leaf the file did not set; and the commit adds a change record naming the leaf's
row tag. A commit adding the file is printed and not graded. Exit 1 names the commit and the key;
at `floor.record-changes` `off` each finding is reported after `floor: record-changes off`, exit 0.

THE EXPANSION RULE, `check_expansion_value(key, value, points)`. A `[[selects]]` row of this kit's
`loop.toml` names a key, a value and the layer point that value needs; where `points`, those the core
rows of the playbook kit's `layers.toml` declare, lack it, `policy-file.on-missing-expansion` decides:
`refuse` raises LoopError naming the key, the value and the point, `fallback-reported` prints one
`loop-guard: fallback` line and returns the catalogue default. A row missing a string `key`, `value`
or `point` is a LoopError naming it.

`--fixture --plant <case>` builds one scratch repository under the host temp directory, a branch
`main` with no remote, a tracked `AGENTS.md` and a policy file setting its cap, the policy kit's list
at the kit's own path and a memory tree holding the build `tFix`; the kits are this tree's. It runs
each scenario of the case, prints `loop-guard: fixture · <scenario> · exit <n> · held` or `· MISSED`,
then `loop-guard: fixture · plant <case> · <k> of <n> scenario(s) held`, and exits as the last
scenario did when every one held, else 3. `--selftest` runs every plant through `run_selftest_cases`.

Exit: 0 admitted or clean, 1 refused, 2 when a reader, a kit or git does not answer: deny by default.

WHAT THIS DOES NOT CHECK: a change to the list file alone, which stages no listed path, so the
pre-commit block never calls the verdict; a run's own switch of the floor, which only its change record
and the push arm witness; a pty wrapper giving an agent a terminal (SA-1), `git commit --no-verify` and
`git push --no-verify`; that a change record's argument is true; and a commit adding the policy file,
which the push arm skips (§8 F11) and the verdict refuses off a live run's branch.
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys
import tempfile
import tomllib

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from floor import read_floor, read_policy_modules  # noqa: E402
from loop_lib import LoopError, read_definition, read_memory_tree, resolve_kit_dir, run_selftest_cases  # noqa: E402
from loop_witness import read_clean_env, read_git, remove_tree, run_fixture_git, write_fixture_files  # noqa: E402

SAY = "loop-guard"
TRAILER_KEY = "Gov-Policy"
LIST_TAG = "kit.policy"
#: the leaves the guard's own switch holds, each a key path prefix
SELF_KEYS = (("policy-file", "guard"), ("policy-file", "proof"), ("floor",))
#: a change record's name, the change kind's grammar under any memory root
CHANGE_NAME = re.compile(r"(?:^|/)builds/[^/]+/build/\d{4}-\d{2}-\d{2}-build-[A-Za-z]+-[A-Za-z0-9]+-\d+-change-\d+\.md$")
REMEDY = ("loop-guard: the owner commits from a terminal, or an agent writes through the loop kit's policy_edit.py: "
          "`set` on a live run's branch, `raise` for one measured-file cap; every change carries its change record.")


# ------------------------------------------------------------------------------------------ shared reads
def derive_row_tag(policy, key):
    """The row tag of the leaf `key`, a key path: `policy.<row name>` for a row of literal segments, the
    family tag `policy.<prefix>` for a row carrying a placeholder, as the tag index mints them; a map
    row's member takes its row's tag. None where no catalogue row names the leaf."""
    rows = policy.load_catalogue(policy.KIT)
    for path in (key, key[:-1]):
        try:
            row = policy.read_catalogue_row(path, rows)
        except policy.Refusal:
            continue
        if path != key and (row.get("allowed") or {}).get("type") != "map":
            return None
        segs = str(row["name"]).split(".")
        cut = next((i for i, s in enumerate(segs) if s == "*" or (s.startswith("<") and s.endswith(">"))), len(segs))
        return "policy." + ".".join(segs[:cut]) if cut else None
    return None


def render_policy_trailer(policy, key, old, new):
    """The `Gov-Policy:` trailer's value for one changed leaf: `policy.<key> <old> -> <new>`, each value
    compact JSON, `none` for a leaf the file did not set."""
    def render_side(v):
        return "none" if v is None else json.dumps(v, ensure_ascii=False, separators=(",", ":"))
    return "policy.%s %s -> %s" % (policy.render_dotted(key), render_side(old), render_side(new))


def parse_policy_bytes(blob):
    """The policy file's bytes parsed, one leading BOM off, or {} for None; None where they do not parse."""
    if blob is None:
        return {}
    try:
        return tomllib.loads(blob.decode("utf-8").removeprefix("﻿"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError):
        return None


def read_core_points():
    """Every point a core row of the playbook kit's `layers.toml` declares; empty where that kit does not
    resolve or its register does not read, so every selecting value meets the expansion rule."""
    try:
        path = resolve_kit_dir("playbook", "layers.toml", KIT) / "layers.toml"
        rows = tomllib.loads(path.read_text(encoding="utf-8")).get("layer") or []
    except (LookupError, OSError, UnicodeDecodeError, tomllib.TOMLDecodeError):
        return set()
    return {p for r in rows if isinstance(r, dict) and r.get("kind") == "core" for p in r.get("declares") or ()}


def check_expansion_value(key, value, points, root="."):
    """`value` for `key`, where no `[[selects]]` row ties it to a point `points` lacks; else, as
    `policy-file.on-missing-expansion` at `root`'s landed revision says, a LoopError naming the key, the
    value and the point under `refuse`, or the catalogue default, one line printed, under
    `fallback-reported`. A `[[selects]]` row missing a string `key`, `value` or `point` is a LoopError."""
    data, where = read_definition(KIT)
    rows = data.get("selects", [])
    if not isinstance(rows, list):
        raise LoopError(where, "'selects' is not an array of tables")
    for n, row in enumerate(rows, 1):
        missing = [f for f in ("key", "value", "point") if not isinstance(row, dict) or not isinstance(row.get(f), str)]
        if missing:
            raise LoopError(where, "[[selects]] row %d carries no string %s" % (n, ", ".join(missing)))
    hit = next((r for r in rows if r["key"] == key and r["value"] == value), None)
    if hit is None or hit["point"] in points:
        return value
    policy, _guard = read_policy_modules()
    said = "%s = %s selects %s, which no core row of the playbook kit's layers.toml declares" % (key, value, hit["point"])
    try:
        on = policy.resolve("policy-file.on-missing-expansion", str(root)).value
    except policy.Refusal as e:
        raise LoopError(where, "%s, and policy-file.on-missing-expansion does not read: %s" % (said, e)) from None
    if on != "fallback-reported":
        raise LoopError(where, "%s; policy-file.on-missing-expansion is %s" % (said, on))
    default = policy.read_catalogue_row(policy.parse_key(key), policy.load_catalogue(policy.KIT))["default"]
    print("%s: fallback · %s · read as the catalogue default %s, as policy-file.on-missing-expansion = "
          "fallback-reported says" % (SAY, said, default))
    return default


# ------------------------------------------------------------------------------------------ the verdict
def derive_list_rel(mguard):
    """The repo-relative path of the policy kit's list file, as the minimal guard reads it at HEAD."""
    kit = pathlib.Path(mguard.__file__).absolute().parent
    return mguard.run_git("-C", str(kit), "rev-parse", "--show-prefix").decode("utf-8").strip() + mguard.LIST


def read_staged_units(mguard):
    """The `Unit` of each change record the staged change adds, read through the memory-tree kit's
    `read_change` from the index the hook hands over."""
    read_memory_tree("build_records.py")
    from build_records import read_change
    names = mguard.run_git("diff", "--cached", "--name-only", "--no-renames", "--diff-filter=A", "-z")
    units = set()
    for rel in (n for n in names.decode("utf-8").split("\0") if CHANGE_NAME.search(n)):
        text = mguard.run_git("cat-file", "blob", mguard.read_blob_id("", rel)).decode("utf-8", "replace")
        units.add(read_change(rel, text).get("Unit"))
    return units


def check_staged():
    """§4's verdict over the staged change -> its exit: 0 admitted, 1 refused, 2 not judged."""
    try:
        policy, mguard = read_policy_modules()
        floor = read_floor()
    except (LookupError, LoopError) as e:
        print("%s: cannot judge · %s" % (SAY, e))
        return 2
    guarded = mguard.read_guarded_paths()
    touched = mguard.check_parent_sides(mguard.read_touched_paths(guarded)) if guarded else {}
    if not touched:
        return 0
    list_rel = derive_list_rel(mguard)
    list_changed = bool(mguard.check_parent_sides(mguard.read_touched_paths([list_rel])))
    changes = {}
    if mguard.POLICY in touched:
        old, new = (parse_policy_bytes(None if oid is None else mguard.run_git("cat-file", "blob", oid))
                    for oid in (mguard.read_blob_id("HEAD", mguard.POLICY), mguard.read_blob_id("", mguard.POLICY)))
        changes = None if old is None or new is None else mguard.derive_leaf_changes(old, new)
    refused = []
    # Step 2: guard-self, the run admission before it.
    selfs = [(list_rel, "the guarded paths list")] if list_changed else []
    if changes is None:
        selfs.append((mguard.POLICY, "a policy file that does not parse, so no leaf it changes is known"))
    else:
        selfs += [(mguard.POLICY, policy.render_dotted(k)) for k in sorted(changes)
                  if any(k[:len(s)] == s for s in SELF_KEYS)]
    if selfs and floor["guard-self"] == "off":
        print("floor: guard-self off · reported · %s" % ", ".join(n for _p, n in selfs))
    elif selfs:
        admission, _whys = mguard.check_run_mandate()
        if admission is None:
            refused += [(p, "%s: the guard's own switch, refused under floor.guard-self for every agent commit off a "
                            "live run's branch, whatever policy-file.guard reads" % n) for p, n in selfs]
        else:
            print("%s: admitted · guard-self · %s · the run-branch of %s" % (SAY, ", ".join(n for _p, n in selfs),
                                                                         admission))
    # Step 3: every change recorded.
    owed = [(list_rel, list_rel, LIST_TAG)] if list_changed else []
    for key in sorted(changes or {}):
        owed.append((mguard.POLICY, policy.render_dotted(key), derive_row_tag(policy, key)))
    try:
        units = read_staged_units(mguard) if owed else set()
    except LookupError as e:
        print("%s: cannot judge · the change records do not read: %s" % (SAY, e))
        return 2
    missing = [(p, "%s changed, and no staged change record names %s" % (n, t) if t else
                "%s changed, and no catalogue row names it, so no change record can" % n)
               for p, n, t in owed if t is None or t not in units]
    if missing and floor["record-changes"] == "off":
        print("floor: record-changes off")
        for p, why in missing:
            print("%s: reported · %s · %s" % (SAY, p, why))
    else:
        refused += [(p, "%s: write it through policy_edit.py, or the memory-tree kit's change door" % why)
                    for p, why in missing]
    # Step 4: the value's rule, read at the landed revision.
    try:
        value = policy.resolve("policy-file.guard").value
    except policy.Refusal as e:
        print("%s: cannot judge · %s" % (SAY, e))
        return 2
    p = subprocess.run([sys.executable, mguard.__file__, "--staged"], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    sys.stdout.write(p.stdout + p.stderr)
    if p.returncode not in (0, 1):
        print("%s: cannot judge · the minimal guard exited %d" % (SAY, p.returncode))
        return 2
    rule = "policy-file.guard = %s · the minimal guard admits it" % value
    if p.returncode and value == "agents-with-reason" and set(touched) == {mguard.POLICY} and mguard.check_decisions_row():
        rule = "policy-file.guard = agents-with-reason · the policy file alone, with its decision row"
    elif p.returncode:
        refused += [(path, "policy-file.guard = %s admits an agent's write only as one cap raised with its RAISED line "
                           "and decision row, the mirror's render%s, or a live run's branch" % (
                               value, ", the policy file alone with a decision row" if value == "agents-with-reason" else ""))
                    for path in sorted(touched)]
    # Step 5: the verdict.
    for path, why in refused:
        print("%s: refused · %s · %s" % (SAY, path, why))
    if refused:
        print(REMEDY)
        return 1
    print("%s: admitted · %s" % (SAY, rule))
    return 0


# ------------------------------------------------------------------------------------------ the push arm
def read_policy_blob(rev, rel):
    """The policy file's bytes in the commit `rev`, or None where it holds none; OSError where git fails."""
    rc, _out = read_git(".", "cat-file", "-e", "%s:%s" % (rev, rel))
    if rc:
        return None
    p = subprocess.run(["git", "cat-file", "blob", "%s:%s" % (rev, rel)], capture_output=True, env=read_clean_env())
    if p.returncode:
        raise OSError("git cat-file %s:%s exited %d" % (rev, rel, p.returncode))
    return p.stdout


def read_added_units(sha):
    """The `Unit` of each change record the commit `sha` adds."""
    read_memory_tree("build_records.py")
    from build_records import read_change
    rc, out = read_git(".", "diff-tree", "--no-commit-id", "-r", "--root", "--name-only", "--diff-filter=A", sha)
    if rc:
        raise OSError("git diff-tree %s exited %d" % (sha, rc))
    units = set()
    for rel in (n for n in out.splitlines() if CHANGE_NAME.search(n)):
        units.add(read_change(rel, read_policy_blob(sha, rel).decode("utf-8", "replace")).get("Unit"))
    return units


def check_push_range(base, tip):
    """The push arm over `<base>..<tip>` -> its exit: 0 clean, reported or unarmed, 1 a commit refused, 2 not
    judged. A tree holding no policy kit or no memory-tree kit has no guarded policy file to grade: one
    `unarmed` line, exit 0, as the hook prints one line for no loop kit."""
    try:
        policy, mguard = read_policy_modules()
        read_memory_tree("commit_trailers.py")
    except LookupError as e:
        print("%s: push · unarmed · %s" % (SAY, e))
        return 0
    try:
        floor = read_floor()
        from commit_trailers import read_commits
        commits = read_commits(".", ["--no-merges", "%s..%s" % (base, tip)], [TRAILER_KEY])
        findings, graded = [], 0
        for c in commits:
            sha8 = c["sha"][:8]
            old = read_policy_blob(c["parents"][0], mguard.POLICY) if c["parents"] else None
            new = read_policy_blob(c["sha"], mguard.POLICY)
            if old is None:
                if new is not None:
                    print("%s: push · %s adds %s, not graded" % (SAY, sha8, mguard.POLICY))
                continue
            if old == new:
                continue
            graded += 1
            a, b = parse_policy_bytes(old), parse_policy_bytes(new)
            if a is None or b is None:
                findings.append("commit %s · %s does not parse on one side, so its changed keys are unknown" % (
                    sha8, mguard.POLICY))
                continue
            said, units = set(c["trailers"][TRAILER_KEY]), read_added_units(c["sha"])
            for key, (o, n) in sorted(mguard.derive_leaf_changes(a, b).items()):
                want, tag = render_policy_trailer(policy, key, o, n), derive_row_tag(policy, key)
                if want not in said:
                    findings.append("commit %s · %s · %s changed with no `%s: %s` trailer" % (
                        sha8, mguard.POLICY, policy.render_dotted(key), TRAILER_KEY, want))
                if tag is None or tag not in units:
                    findings.append("commit %s · %s · %s changed and the commit adds no change record naming %s" % (
                        sha8, mguard.POLICY, policy.render_dotted(key), tag or "its row, which no catalogue row is"))
    except (LookupError, LoopError, OSError, ValueError) as e:
        print("%s: cannot judge · %s" % (SAY, e))
        return 2
    if findings and floor["record-changes"] == "off":
        print("floor: record-changes off")
        for f in findings:
            print("%s: push · reported · %s" % (SAY, f))
        return 0
    for f in findings:
        print("%s: push · refused · %s" % (SAY, f))
    print("%s: push · %d commit(s) read · %d changing %s · %d finding(s)" % (
        SAY, len(commits), graded, mguard.POLICY, len(findings)))
    return 1 if findings else 0


# ------------------------------------------------------------------------------------------ the plants
FX_BUILD, FX_UNIT = "tFix", "TOOL-tFix-1"
FX_CAP = "AGENTS.md"
FX_AGENTS = "# AGENTS.md\n\n" + "a fixture charter line, padded to its measure.\n" * 2 + "x" * 10 + "\n"
FX_RUN, FX_DRIVER, FX_BRANCH = "memory/builds/tRun/RUN.md", "drv/unattended.sh", "run/t"
FX_ROW = "- %s · %s cap 100 -> 120: the fixture's file measured 118 bytes\n" % (FX_UNIT, FX_CAP)
FX_REVIEW = "[review]\nmax-rounds = 4\n"
PLANTS = {
    "raise-admitted": "policy_edit.py raise AGENTS.md 120 and its decision row",
    "raise-no-record": "the cap raised by hand with its RAISED line and decision row, no change record",
    "raise-lowered": "the cap set to 90 by hand",
    "floor-off-agent": "floor.no-actor-witness off staged under each guard value on a branch no run names",
    "floor-off-run": "owner-only on a live run's branch: a floor member off and a list line dropped, with and without records",
    "other-write-owner-only": "review.max-rounds set with a change record under owner-only",
    "with-reason-admitted": "agents-with-reason: a key set with its record and a decision row",
    "with-reason-no-row": "agents-with-reason: a key set with its record and no decision row",
    "mandate-live": "agents-within-mandate on a live run's branch",
    "mandate-none": "agents-within-mandate on a branch no run names",
    "owner-only-live": "owner-only on a live run's branch",
    "push-no-trailer": "a commit changing the policy file with no Gov-Policy: line, graded by --push-range",
    "proof-signed-refuse": "policy_edit.py set policy-file.proof signed under refuse",
    "proof-signed-fallback": "policy_edit.py set policy-file.proof signed under fallback-reported",
    "set-run-live": "policy_edit.py set on a live run's branch, a key then a floor member",
    "floor-readers": "an unlisted actor witness and an unrecorded transition, under the floor on, then off",
}


def run_fixture_command(top, argv):
    """A process in the scratch repository: `(exit, stdout and stderr)`, standard error never a terminal."""
    p = subprocess.run(argv, cwd=top, capture_output=True, text=True, encoding="utf-8", errors="replace",
                       env=read_clean_env())
    said = p.stdout + p.stderr
    sys.stdout.write(said)
    return p.returncode, said


def write_guard_plant(top, policy_text=""):
    """The scratch repository at `top`, committed on `main`: `AGENTS.md`, the policy file setting its cap
    beside `policy_text`, the policy kit's list at that kit's own path, and the build `tFix`. -> the list's path."""
    _policy, mguard = read_policy_modules()
    run_fixture_git(top, "init", "-q", "--template=", "-b", "main")
    list_rel = derive_list_rel(mguard)
    kit_list = pathlib.Path(mguard.__file__).absolute().parent / mguard.LIST
    write_fixture_files(top, {
        FX_CAP: FX_AGENTS, mguard.POLICY: '[budgets]\n"%s" = 100\n%s' % (FX_CAP, policy_text),
        list_rel: kit_list.read_text(encoding="utf-8").replace("\r", ""),
        ".memory-tree.conf": 'MEMORY_ROOT=memory\nFAMILIES="tool:TOOL"\n',
        "memory/builds/%s/README.md" % FX_BUILD: "# %s\n" % FX_BUILD,
        mguard.DECISIONS: "# Decisions\n\n- the fixture's first row\n"})
    run_fixture_git(top, "add", "-A")
    run_fixture_git(top, "commit", "-q", "-m", "fixture")
    return list_rel


def write_live_run(top):
    """A live run's branch: `run/t` checked out, its run-state file and a driver declaring the terminal set."""
    run_fixture_git(top, "checkout", "-q", "-b", FX_BRANCH)
    write_fixture_files(top, {FX_RUN: "# tRun\n\n## Run facts\nphase: BUILDING\nrun-branch: refs/heads/%s\n" % FX_BRANCH,
                              FX_DRIVER: 'PHASES_TERMINAL="LANDED ABORTED"\n'})
    run_fixture_git(top, "add", "-A")
    run_fixture_git(top, "commit", "-q", "-m", "the live run")


def write_staged(top, files):
    """Each `{path: edit of its text}` written and staged."""
    for rel, edit in files.items():
        path = pathlib.Path(top, rel)
        write_fixture_files(top, {rel: edit(path.read_text(encoding="utf-8") if path.is_file() else "")})
        run_fixture_git(top, "add", "--", rel)


def write_fixture_record(top, tag):
    """One change record naming `tag`, written through the memory-tree kit's door and staged."""
    read_memory_tree("build_records.py")
    import build_records
    rel = build_records.write_change(str(top), FX_BUILD, FX_UNIT, tag, "edit", "semantic", "none", "none",
                                     "none — fixture")
    run_fixture_git(top, "add", "--", rel)


def run_guard_plant(case, top):
    """The scenarios of `case` over the scratch at `top`: `[(scenario, exit, owed, needle, output)]`."""
    _policy, mguard = read_policy_modules()
    me, out = [sys.executable, str(pathlib.Path(__file__).absolute())], []
    edit = [sys.executable, str(KIT / "policy_edit.py")]
    who = ["--build", FX_BUILD, "--unit", FX_UNIT]

    def run_scenario(name, argv, owed, needle):
        rc, said = run_fixture_command(top, argv)
        out.append((name, rc, owed, needle, said))

    def add_text(extra):
        return lambda t: t + extra

    def run_reset():
        run_fixture_git(top, "reset", "-q", "--hard")
        run_fixture_git(top, "clean", "-qfd")

    guard_value = {"with-reason-admitted": "agents-with-reason", "with-reason-no-row": "agents-with-reason",
                   "mandate-live": "agents-within-mandate", "mandate-none": "agents-within-mandate"}.get(case)
    expansion = 'on-missing-expansion = "fallback-reported"\n' if case == "proof-signed-fallback" else ""
    head = "[policy-file]\n%s%s" % ('guard = "%s"\n' % guard_value if guard_value else "", expansion)
    list_rel = write_guard_plant(top, head if (guard_value or expansion) else "")
    if case in ("floor-off-run", "mandate-live", "owner-only-live", "set-run-live"):
        write_live_run(top)
    raised = (mguard.POLICY, lambda t: t.replace('"%s" = 100\n' % FX_CAP, '# RAISED 100 -> 120, 2026-11-15, %s, '
                                                 'measured 118 bytes\n"%s" = 120\n' % (FX_UNIT, FX_CAP)))
    if case == "raise-admitted":
        run_scenario("the raise written", edit + ["raise", FX_CAP, "120", *who, "--argument", "the fixture"], 0, "Gov-Policy:")
        write_staged(top, {mguard.DECISIONS: add_text(FX_ROW)})
        run_scenario("the raise judged", me + ["--staged"], 0, "loop-guard: admitted")
    elif case in ("raise-no-record", "raise-lowered"):
        lowered = (mguard.POLICY, lambda t: t.replace('"%s" = 100\n' % FX_CAP, '"%s" = 90\n' % FX_CAP))
        write_staged(top, dict([raised if case == "raise-no-record" else lowered, (mguard.DECISIONS, add_text(FX_ROW))]))
        run_scenario("judged", me + ["--staged"], 1, "change record" if case == "raise-no-record" else "a lowering")
    elif case == "floor-off-agent":
        for value in ("owner-only", "agents-with-reason", "agents-within-mandate"):
            write_staged(top, {mguard.POLICY: add_text('\n[policy-file]\nguard = "%s"\n' % value)})
            run_fixture_git(top, "commit", "-q", "-m", "guard %s" % value)
            write_staged(top, {mguard.POLICY: add_text('\n[floor]\nno-actor-witness = "off"\n')})
            write_fixture_record(top, "policy.floor")
            run_scenario(value, me + ["--staged"], 1, "floor.guard-self")
            run_reset()
            run_fixture_git(top, "reset", "-q", "--hard", "HEAD~1")
    elif case == "floor-off-run":
        dropped = {mguard.POLICY: add_text('\n[floor]\nno-actor-witness = "off"\n'),
                   list_rel: lambda t: t.replace(".governance/deploy.toml\n", "")}
        write_staged(top, dropped)
        write_fixture_record(top, "policy.floor")
        write_fixture_record(top, LIST_TAG)
        run_scenario("with their records", me + ["--staged"], 0, "loop-guard: admitted")
        run_reset()
        write_staged(top, dropped)
        run_scenario("without them", me + ["--staged"], 1, "no staged change record names %s" % LIST_TAG)
        out.append(("without them, the floor's record", out[-1][1], 1, "no staged change record names policy.floor",
                    out[-1][4]))
    elif case in ("other-write-owner-only", "with-reason-admitted", "with-reason-no-row", "mandate-live",
                  "mandate-none", "owner-only-live"):
        write_staged(top, {mguard.POLICY: add_text(FX_REVIEW)})
        write_fixture_record(top, "policy.review.max-rounds")
        if case == "with-reason-admitted":
            write_staged(top, {mguard.DECISIONS: add_text("- %s · review.max-rounds 3 -> 4: the fixture\n" % FX_UNIT)})
        owed = 0 if case in ("with-reason-admitted", "mandate-live", "owner-only-live") else 1
        run_scenario("judged", me + ["--staged"], owed, "loop-guard: admitted" if not owed else "policy-file.guard")
    elif case == "push-no-trailer":
        base = run_fixture_git(top, "rev-parse", "HEAD")
        write_staged(top, {mguard.POLICY: add_text(FX_REVIEW)})
        write_fixture_record(top, "policy.review.max-rounds")
        run_fixture_git(top, "commit", "-q", "-m", "review rounds raised, no trailer")
        sha8 = run_fixture_git(top, "rev-parse", "--short=8", "HEAD")
        run_scenario("graded", me + ["--push-range", "%s..HEAD" % base], 1, "commit %s · %s" % (sha8, mguard.POLICY))
    elif case in ("proof-signed-refuse", "proof-signed-fallback"):
        refuse = case == "proof-signed-refuse"
        run_scenario("set signed", edit + ["set", "policy-file.proof", "signed", *who], 2 if refuse else 1,
                     "point.instruction.signed-proof" if refuse else "the catalogue default tty-cli")
    elif case == "set-run-live":
        run_scenario("a key", edit + ["set", "review.max-rounds", "4", *who], 0, "Proof: none — run mandate")
        run_fixture_git(top, "commit", "-q", "-m", "review rounds raised on the run's branch")
        run_scenario("a floor member", edit + ["set", "floor.guard-self", "off", *who], 0, "Proof: none — run mandate")
    elif case == "floor-readers":
        out += run_floor_readers(top)
    return out


def run_floor_readers(top):
    """AC17's four observations: each reader refuses its plant under the floor all on, and reports and
    passes once the landed revision sets its member off. `[(scenario, exit, owed, needle, output)]`."""
    import contextlib
    import io
    import loop_lib
    import loop_transition as lt
    remove_tree(top)
    pathlib.Path(top).mkdir()
    witness = lt.write_transition_plant(pathlib.Path(top), "default")
    with contextlib.redirect_stdout(io.StringIO()):
        lt.main(["record", "--build", lt.FX_BUILD, "--root", str(top), "--from", "planning", "--item", "item.plan.exit",
                 "--outcome", "recorded", "--witness", witness])
    for rec in lt.read_transition_records(lt.FX_BUILD, pathlib.Path(top)):
        pathlib.Path(top, rec["path"]).unlink()
    run_fixture_git(top, "add", "-A")
    run_fixture_git(top, "commit", "-q", "-m", "the move's record deleted")
    listed = [ln.split("\t")[1] for ln in loop_lib.read_actor_rows(KIT) if ln.split("\t")[0] == "DOD_CORE"]
    entries = ["%s:agent" % item for item in listed] + ["fx-floor-witness:agent"]
    out = []
    for member_state in ("on", "off"):
        if member_state == "off":
            write_fixture_files(top, {".governance/policy.toml": '[floor]\nno-actor-witness = "off"\nrecord-changes = "off"\n'})
            run_fixture_git(top, "add", "-A")
            run_fixture_git(top, "commit", "-q", "-m", "the floor's two members off")
        lines, refusals = loop_lib.check_site_witnesses(KIT, "DOD_CORE", entries, root=top)
        said = "\n".join(lines + ["loop: refused · %s" % r for r in refusals]) + "\n"
        sys.stdout.write(said)
        out.append(("actor witness, floor %s" % member_state, 1 if refusals else 0, 1 if member_state == "on" else 0,
                    "fx-floor-witness" if member_state == "on" else "floor: no-actor-witness off", said))
        lines, findings = lt.check_transition_channels(lt.FX_BUILD, pathlib.Path(top))
        said = "\n".join(["%s: transition · %s" % (lt.SAY, f) for f in findings] + lines) + "\n"
        sys.stdout.write(said)
        out.append(("transition, floor %s" % member_state, 1 if findings else 0, 1 if member_state == "on" else 0,
                    "owes a record" if member_state == "on" else "floor: record-changes off", said))
    return out


def run_fixture(case):
    """`case`'s scenarios over one scratch repository, each held or missed: the last exit when all held, else 3."""
    top = pathlib.Path(tempfile.mkdtemp(prefix="loop-guard-")).absolute()
    try:
        print("%s: fixture · plant %s · %s" % (SAY, case, PLANTS[case]))
        try:
            out = run_guard_plant(case, top)
        except (LookupError, LoopError, OSError, subprocess.CalledProcessError) as e:
            print("%s: fixture · plant %s · not run: %s" % (SAY, case, e))
            return 2
        held = 0
        for name, rc, owed, needle, said in out:
            ok = rc == owed and needle in said
            held += ok
            print("%s: fixture · %s · exit %d · owed %d naming %r · %s" % (SAY, name, rc, owed, needle,
                                                                        "held" if ok else "MISSED"))
        print("%s: fixture · plant %s · %d of %d scenario(s) held%s" % (
            SAY, case, held, len(out), " · all held" if out and held == len(out) else ""))
        return out[-1][1] if out and held == len(out) else 3
    finally:
        remove_tree(top)


def run_selftest():
    """Every plant through `run_selftest_cases`: each owes its last scenario's exit and the all-held line."""
    owed = {"raise-no-record": 1, "raise-lowered": 1, "floor-off-agent": 1, "floor-off-run": 1,
            "other-write-owner-only": 1, "with-reason-no-row": 1, "mandate-none": 1, "push-no-trailer": 1,
            "proof-signed-refuse": 2, "proof-signed-fallback": 1}
    cases = [(case, ["--fixture", "--plant", case], owed.get(case, 0), "%s: fixture · plant %s · " % (SAY, case),
              "all held") for case in PLANTS]
    return run_selftest_cases(main, cases, "%s: selftest" % SAY)


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="guard.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("--staged", action="store_true", help="judge the staged change of an agent's commit")
    ap.add_argument("--push-range", help="<base>..<tip>: grade each commit's Gov-Policy trailers and records")
    ap.add_argument("--fixture", action="store_true", help="run one plant's scenarios in a scratch repository")
    ap.add_argument("--plant", choices=list(PLANTS))
    ap.add_argument("--selftest", action="store_true", help="run every plant")
    args = ap.parse_args(argv)
    modes = [args.staged, args.push_range is not None, args.fixture, args.selftest]
    if sum(modes) != 1 or args.fixture != bool(args.plant):
        ap.error("one of --staged, --push-range <base>..<tip>, --fixture --plant <case> or --selftest")
    if args.selftest:
        return run_selftest()
    if args.fixture:
        return run_fixture(args.plant)
    if args.staged:
        return check_staged()
    base, sep, tip = args.push_range.partition("..")
    if not (base and sep and tip) or base.startswith("-") or tip.startswith("-"):
        ap.error("--push-range takes <base>..<tip>")
    return check_push_range(base, tip)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
