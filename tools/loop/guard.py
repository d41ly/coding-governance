#!/usr/bin/env python3
"""guard.py — the policy file's guard: its commit verdict, its push arm and the expansion rule (TOOL-dDeclaredLoop-2).

    python guard.py --staged                      # the pre-commit block's verdict, from the top level
    python guard.py --push-range <base>..<tip>    # the pre-push arm over a default-branch update
    python guard.py --expansion                   # the expansion rule over <key>=<toml value> lines on stdin
    python guard.py --fixture --plant <case>
    python guard.py --selftest

THE VERDICT, `check_staged`. The pre-commit block runs it only when a path the policy kit's
`guarded-paths.txt` lists at HEAD is staged and standard error is no terminal, so every call is an
agent's commit. It wraps dGroundRules-6's minimal guard, the policy kit's `guard.py`, found through
`read_policy_kit`, and copies none of it. In order:

1. The touch set, the minimal guard's `read_guarded_paths` met with the staged names, less a merge's
   parent sides. Empty: exit 0.
2. Owner-only, under every value of `floor.guard-self` and of `policy-file.guard`: a staged change of a
   leaf `OWNER_ONLY_KEYS` holds, `verdict.remote.pin` or `verdict.peer.signers`, is refused naming the key unless the minimal
   guard's `check_run_mandate` admits the branch, the owner's 2026-11-12 ruling (TOOL-dWitnessedBar-6).
   Then guard-self, at `floor.guard-self` `on`: a staged change of the list file, or of a leaf of
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

THE PUSH ARM, `check_push_range` (TOOL-dDeclaredLoop-44). Every commit of the range, merges included,
read through the memory-tree kit's `read_commits` with the key `Gov-Policy`. A non-merge commit whose
parent holds the policy file and whose own blob of it differs is graded leaf by leaf: each changed
leaf owes one trailer line `Gov-Policy: policy.<key> <old> -> <new>`, the key spelled by
`render_dotted` and each value compact JSON, `none` for a leaf the file did not set; and the commit
adds a change record naming the leaf's row tag. A two-parent merge whose clean re-merge git computes,
`merge-tree --write-tree` of its parents read by `read_remerge_policy`, is graded against that
re-merge alone (TOOL-dDeclaredLoop-69): it owes for each key its result sets to a value other than
that re-merge's, a key set back to one side's old value included, the same trailer, its old value the
re-merge's, and a change record among those git's combined diff, `diff-tree --cc`, lists at the
merge. A merge equal to its re-merge owes nothing, its sides' commits being graded in the range. That
re-merge is in one of five states (TOOL-dDeclaredLoop-78, TOOL-dDeclaredLoop-81): `absent`, its tree
lacking the file, read as the empty table; `present`, its tree holding it; `uncomputable`, an octopus
merge or a git without `merge-tree --write-tree`, which `resolve_write_tree_support` probes once from
`git merge-tree -h`, the re-merge never run; `conflicted`, an exit 1 whose conflicts hold the policy
path, or that prints no tree id; and `failed`, every other outcome. An exit 1 whose `--name-only`
conflicted paths, the lines after its tree id up to the first blank line, miss the policy path reads
`absent` or `present` from that tree, as an exit 0 does (TOOL-dDeclaredLoop-75 S27). The usage probe runs under `LC_ALL=C`, so a translated git prints its usage header untranslated
(TOOL-dDeclaredLoop-88 S16). A git whose usage probe fails, cannot start or prints no usage text is graded as a failed
re-merge, `probe failed: <detail>`, and only a usage text lacking `--write-tree` reads as a git without
it (TOOL-dDeclaredLoop-85); a probe exiting other than 0 or 129, or printing no `usage: git merge-tree`
line, is a failed probe, whatever its text names (TOOL-dDeclaredLoop-86 S2). A `present` re-merge whose file does not parse is refused, `merge <sha8> · <policy
path> does not parse at C`, as is a merge whose own file does not parse, `at M`, or a parent's on the
parents' grade, `at parent <sha8>`; a non-merge commit's reads `on one side`. Every
`uncomputable` or `conflicted` merge is graded against its parents (TOOL-dDeclaredLoop-59), and only where the
combined diff lists the file with a blob differing from its first parent's: it owes for a key its result
sets to a value no parent holds, the trailer's old value the first parent's. A `failed` merge prints
`<sha8> graded against every parent — the clean re-merge failed: <detail>`, its exit code and git's
first standard error line, a start that fails spelled `start failed: <the first non-blank line of its text>`,
stripped, or its class name where it has none (TOOL-dDeclaredLoop-92 S17, TOOL-dDeclaredLoop-94 S20), a negative code
`signal <n>` and an empty standard error `(no stderr)` (TOOL-dDeclaredLoop-86 S22), and owes, with no exemption and whatever the combined diff lists, the
trailer and record for each key its result sets apart from some parent, the old value the first such
parent's. A commit or merge no parent of which holds the file, a root commit included, is printed where
it adds the file and is not graded; a merge any parent of which holds it is graded as above, a parent
lacking it, the first included, read as the empty table (TOOL-dDeclaredLoop-115). An all-zero
base, a new ref, reads as the policy kit's `derive_landed_revision`; where that refuses, a first push to
an empty remote among the causes, the arm prints `push · no landed revision (<why>), graded over every
commit touching <policy path>` and grades each commit `git log --full-history <tip> -- <policy path>`
names, merges by the same key grade, exit 0 where none changes a key (TOOL-dDeclaredLoop-67 S33). Exit 1
names the commit or merge and the key; at `floor.record-changes` `off` each finding is reported after
`floor: record-changes off`, exit 0.

THE EXPANSION RULE, `check_expansion_value(key, value, points)`. A `[[selects]]` row of this kit's
`loop.toml` names a key, a value and the layer point that value needs; where `points`, those the core
rows of the playbook kit's `layers.toml` declare, lack it, `policy-file.on-missing-expansion` decides:
`refuse` raises LoopError naming the key, the value and the point, `fallback-reported` prints one
`loop-guard: fallback` line and returns the catalogue default. A row missing a string `key`, `value`
or `point` is a LoopError naming it.

THE EXPANSION VERB, `--expansion` (KICK-dKeptSession-1 S8, TOOL-dDeclaredLoop-2 S8): each non-blank
`<key>=<toml value>` line on stdin judged by `check_expansion_value(key, value, read_core_points(), top)`,
`top` the working directory's repository, so the policy kit's `presets.py` loads a preset by the one
rule and copies none of it. A refused pair, or a line that is no such pair, prints `loop-guard: refused
· stdin:<n> · <why>`, the refusal naming the key, the value and the point; the rule's `fallback` line
passes through as no refusal. Exit 2 on any refusal or unreadable line, else 0.

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
`git push --no-verify`; that a change record's argument is true; and a commit or merge adding the
policy file that no parent holds, which the push arm skips (§8 F11) and the verdict refuses off a live
run's branch. Only an octopus merge, a re-merge conflicting on the policy file or a git without
`merge-tree --write-tree` is graded against its parents
alone, one line naming it and why: a key set back to one parent's value passes there unowed, and a
value git's clean merge would have produced, a multi-line one both sides edited, is owed there. A
merge whose clean re-merge fails is graded against every parent and owes a trailer and a record for
each key that differs from one.
"""
import argparse
import functools
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
#: a new ref's old sha, SHA-1 or SHA-256 width, which git reads as no revision at all
ZERO_SHA = re.compile(r"0{40}|0{64}")
#: the leaves the guard's own switch holds, each a key path prefix
SELF_KEYS = (("policy-file", "guard"), ("policy-file", "proof"), ("floor",))
#: the leaves only the owner, or a live run on its own branch, may change (TOOL-dWitnessedBar-6 S9): the
#: off-node backends' pin, which decides the files a remote or peer verdict may stand on, and the peer
#: signer list, whose keys alone may sign a peer verdict (TOOL-dWitnessedBar-43 S2); a set is one leaf
OWNER_ONLY_KEYS = (("verdict", "remote", "pin"), ("verdict", "peer", "signers"))
#: a change record's name, the change kind's grammar under any memory root
read_memory_tree("id_grammar.py")
from id_grammar import SlugPattern  # noqa: E402  the slug grammar, bound at first use (TOOL-dTotalRecall-5 S7)
CHANGE_NAME = SlugPattern(lambda g: r"(?:^|/)builds/[^/]+/build/\d{4}-\d{2}-\d{2}-build-[A-Za-z]+-(?:" + g.slug_class
                          + r")-\d+-change-\d+\.md$")
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


#: an `--expansion` line's key: dotted segments, as the catalogue spells a key
EXPANSION_KEY = re.compile(r"[A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*")


def run_expansion(lines):
    """`--expansion` over `lines`: each `<key>=<toml value>` judged by `check_expansion_value`, one
    `refused` line per refused pair or unreadable line, numbered from 1 -> 2 on any, else 0."""
    rc, out = read_git(".", "rev-parse", "--show-toplevel")
    top = out if rc == 0 and out else "."
    points, refused = read_core_points(), 0
    for n, raw in enumerate(lines, 1):
        line = raw.strip()
        if not line:
            continue
        key, eq, rhs = line.partition("=")
        try:
            if not (eq and EXPANSION_KEY.fullmatch(key.strip())):
                raise ValueError(line)
            value = tomllib.loads("v = " + rhs.strip())["v"]  # tomllib.TOMLDecodeError is a ValueError
        except ValueError:
            print("%s: refused · stdin:%d · %s is not <key>=<toml value>" % (SAY, n, json.dumps(line, ensure_ascii=False)))
            refused += 1
            continue
        try:
            check_expansion_value(key.strip(), value, points, top)
        except (LoopError, LookupError) as e:
            print("%s: refused · stdin:%d · %s" % (SAY, n, e))
            refused += 1
    return 2 if refused else 0


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
    # Step 2, owner-only: under every floor and guard value, the run admission before it.
    owners = [policy.render_dotted(k) for k in sorted(changes or {}) if k in OWNER_ONLY_KEYS]
    if owners:
        admission, _whys = mguard.check_run_mandate()
        if admission is None:
            refused += [(mguard.POLICY, "%s: owner-only, refused for every agent commit off a live run's branch, "
                                        "whatever policy-file.guard and floor.guard-self read" % n) for n in owners]
        else:
            print("%s: admitted · owner-only · %s · the run-branch of %s" % (SAY, ", ".join(owners), admission))
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


def read_added_units(sha, rels=None):
    """The `Unit` of each change record the commit `sha` adds, or, for a merge, of each one among `rels`,
    the paths its combined diff lists, that the merge holds: `--diff-filter=A` prints nothing for a merge."""
    read_memory_tree("build_records.py")
    from build_records import read_change
    if rels is None:
        rc, out = read_git(".", "diff-tree", "--no-commit-id", "-r", "--root", "--name-only", "--diff-filter=A", sha)
        if rc:
            raise OSError("git diff-tree %s exited %d" % (sha, rc))
        rels = out.splitlines()
    units = set()
    for rel in (n for n in rels if CHANGE_NAME.search(n)):
        blob = read_policy_blob(sha, rel)
        if blob is not None:
            units.add(read_change(rel, blob.decode("utf-8", "replace")).get("Unit"))
    return units


def build_failure_detail(outcome, text):
    """The one spelling of a detail under `the clean re-merge failed:` (TOOL-dDeclaredLoop-85): an OSError
    reads `start failed: <the first non-blank line of its text>`, stripped, or `start failed: <its class name>`
    where that text has none (TOOL-dDeclaredLoop-92 S17, TOOL-dDeclaredLoop-94 S20); an exit code reads
    `<rc>`, a negative one `signal <n>`, followed by the first non-blank line of `text`, or `(no stderr)`
    where it has none (TOOL-dDeclaredLoop-86 S22)."""
    if isinstance(outcome, OSError):
        detail = next((ln.strip() for ln in str(outcome).splitlines() if ln.strip()), type(outcome).__name__)
        return "start failed: %s" % detail
    line = next((ln.strip() for ln in text.splitlines() if ln.strip()), "(no stderr)")
    return "%s %s" % ("signal %d" % -outcome if outcome < 0 else outcome, line)


def run_merge_tree_usage():
    """`git merge-tree -h` -> `(exit, stdout, stderr)`, both decoded with replacement; OSError where git
    cannot start (TOOL-dDeclaredLoop-85). Run under `LC_ALL=C` and an empty `LANGUAGE`, set in that call's
    environment alone, so a git shipping translations prints its usage header untranslated
    (TOOL-dDeclaredLoop-88 S16)."""
    p = subprocess.run(["git", "merge-tree", "-h"], capture_output=True, text=True, encoding="utf-8",
                       errors="replace", env=read_clean_env(LC_ALL="C", LANGUAGE=""))
    return p.returncode, p.stdout, p.stderr


def check_write_tree_usage(rc, text):
    """The usage probe's answer from its exit `rc` and its joined `text` (TOOL-dDeclaredLoop-85): where `rc`
    is 0 or 129 and a line opens `usage: git merge-tree`, `supported` if the text names `--write-tree`,
    else `unsupported`, the form a git before it prints; `probe failed` for anything else, a text naming
    the option with no usage line or under another exit included (TOOL-dDeclaredLoop-86 S2)."""
    if rc not in (0, 129) or not any(ln.startswith("usage: git merge-tree") for ln in text.splitlines()):
        return "probe failed"
    return "supported" if "--write-tree" in text else "unsupported"


@functools.cache
def resolve_write_tree_support():
    """Whether this git carries `merge-tree --write-tree` -> `(answer, detail)`, probed once per process
    from its usage text, never from a real re-merge's exit (TOOL-dDeclaredLoop-81); a probe that cannot
    start answers `probe failed` (TOOL-dDeclaredLoop-85)."""
    try:
        rc, out, err = run_merge_tree_usage()
    except OSError as e:
        return "probe failed", build_failure_detail(e, "")
    text = out + "\n" + err
    return check_write_tree_usage(rc, text), build_failure_detail(rc, text)


def run_merge_tree(p1, p2):
    """git's clean re-merge of `p1` and `p2` -> `(exit, stdout, stderr)`, its conflicted file info as names
    alone (`--name-only`, TOOL-dDeclaredLoop-75 S27); OSError where git cannot start."""
    p = subprocess.run(["git", "merge-tree", "--write-tree", "--name-only", p1, p2], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", env=read_clean_env())
    return p.returncode, p.stdout, p.stderr


def read_remerge_policy(parents):
    """The state of git's clean re-merge of the two `parents`, `merge-tree --write-tree`, with its policy
    table or why it is not read (TOOL-dDeclaredLoop-78, TOOL-dDeclaredLoop-81) -> `(state, table, why)`:
    `uncomputable`, table None, for an octopus merge or a git without `merge-tree --write-tree`, the
    re-merge never run; `conflicted` for an exit 1 whose conflicts hold the policy path, or whose first
    line is no tree id; `failed`, `why` its detail, for every other outcome:
    an exit 0 with no tree id, any other exit, a start that fails or a usage probe that failed, the
    re-merge then never run (TOOL-dDeclaredLoop-85); `absent`, table {}, where it exits 0, or exits 1 with
    conflicts elsewhere (TOOL-dDeclaredLoop-75 S27), and its tree lacks the file; `present` where its
    tree holds the file, table the file parsed, None where it does not parse. A missing path is never
    `uncomputable`."""
    _policy, mguard = read_policy_modules()
    if len(parents) != 2:
        return "uncomputable", None, "an octopus merge of %d parents" % len(parents)
    support, detail = resolve_write_tree_support()
    if support == "unsupported":
        return "uncomputable", None, "this git has no merge-tree --write-tree"
    if support == "probe failed":
        # TOOL-dDeclaredLoop-85: only a probed absence takes the parents' exemption.
        return "failed", None, "probe failed: %s" % detail
    try:
        rc, out, err = run_merge_tree(*parents)
    except OSError as e:
        return "failed", None, build_failure_detail(e, "")
    lines = out.strip().split("\n")
    tree = lines[0].strip()
    if rc == 1:
        # TOOL-dDeclaredLoop-75 S27: the conflicted paths are the lines after the tree id up to the first blank
        # line, so a conflict elsewhere leaves the policy file's clean merge in that tree to read.
        blank = next((i for i, ln in enumerate(lines) if i and not ln.strip()), len(lines))
        if not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", tree):
            return "conflicted", None, "its re-merge conflicts, merge-tree exit 1 printing no tree id"
        if mguard.POLICY in [ln.strip() for ln in lines[1:blank]]:
            return "conflicted", None, "its re-merge conflicts on %s, merge-tree exit 1" % mguard.POLICY
    if rc not in (0, 1) or not tree:
        return "failed", None, build_failure_detail(rc, err if rc else "no tree id")
    blob = read_policy_blob(tree, mguard.POLICY)
    return ("absent", {}, None) if blob is None else ("present", parse_policy_bytes(blob), None)


def check_push_range(base, tip):
    """The push arm over `<base>..<tip>` -> its exit: 0 clean, reported or unarmed, 1 a commit refused, 2 not
    judged. A tree holding no policy kit or no memory-tree kit has no guarded policy file to grade: one
    `unarmed` line, exit 0, as the hook prints one line for no loop kit. Its cost past the commit walk is
    one `git merge-tree --write-tree` per two-parent merge whose policy blob differs from some parent's,
    a merge equal to every parent skipped before it (TOOL-dDeclaredLoop-79): 23 ms PINNED each, the
    median of ten runs over a two-file scratch, measured 2026-11-17 on node d (win32, git 2.54)."""
    try:
        policy, mguard = read_policy_modules()
        read_memory_tree("commit_trailers.py")
    except LookupError as e:
        print("%s: push · unarmed · %s" % (SAY, e))
        return 0
    try:
        floor = read_floor()
        revs = ["%s..%s" % (base, tip)]
        if ZERO_SHA.fullmatch(base):
            try:
                base, how = policy.derive_landed_revision(".")
                revs = ["%s..%s" % (base, tip)]
                print("%s: push · a new ref, graded past %s" % (SAY, how))
            except policy.Refusal as e:
                # TOOL-dDeclaredLoop-67 S33: no landed revision, so every commit of the tip's history that
                # touches the policy file is graded, never the arm left unjudged
                revs = ["--full-history", tip, "--", mguard.POLICY]
                print("%s: push · no landed revision (%s), graded over every commit touching %s" % (
                    SAY, e, mguard.POLICY))
        from commit_trailers import read_commits
        commits = read_commits(".", revs, [TRAILER_KEY])
        findings, graded = [], 0
        for c in commits:
            sha8, listed, state, clean, why = c["sha"][:8], None, None, None, None
            kind, own = ("merge", ", the merge's own change") if len(c["parents"]) > 1 else ("commit", "")
            if kind == "merge":
                rc, out = read_git(".", "diff-tree", "--cc", "-r", "--name-only", "--no-commit-id", c["sha"])
                if rc:
                    raise OSError("git diff-tree --cc %s exited %d" % (sha8, rc))
                listed = out.splitlines()
            blobs = [read_policy_blob(p, mguard.POLICY) for p in c["parents"]]
            old, new = (blobs[0] if blobs else None), read_policy_blob(c["sha"], mguard.POLICY)
            if all(blob is None for blob in blobs):
                # TOOL-dDeclaredLoop-115: an add is a commit or merge no parent of which holds the file, a root
                # commit included; any other merge is graded below, a lacking parent read as {}
                if new is not None and (listed is None or mguard.POLICY in listed):
                    print("%s: push · %s %s adds %s, not graded" % (SAY, kind, sha8, mguard.POLICY))
                continue
            if kind == "merge":
                # TOOL-dDeclaredLoop-79 S23: a merge whose blob equals EVERY parent's, an absent one equal only
                # to an absent one, is skipped before any re-merge, since git's clean re-merge equals it too.
                if all(blob == new for blob in blobs):
                    continue
                # TOOL-dDeclaredLoop-69: where git's clean re-merge is computable it is the whole reference,
                # so neither the combined list nor ONE parent's equal blob skips the merge.
                # TOOL-dDeclaredLoop-81: a failed re-merge never takes that skip either.
                state, clean, why = read_remerge_policy(c["parents"])
                if state in ("uncomputable", "conflicted") and (mguard.POLICY not in listed or old == new):
                    continue
            elif old == new:
                continue
            a, b = parse_policy_bytes(old), parse_policy_bytes(new)
            unknown = "%s %s · %s does not parse %%s, so its changed keys are unknown" % (kind, sha8, mguard.POLICY)
            if state in ("present", "absent"):
                # TOOL-dDeclaredLoop-78: a present re-merge that does not parse is refused naming it, never
                # a fall to the parents, whose equal blob would exempt the merge.
                side = "at C" if clean is None else "at M" if b is None else None
                changes = None if side else mguard.derive_leaf_changes(clean, b)
                if changes == {}:
                    continue
                graded += 1
                if side:
                    findings.append(unknown % side)
                    continue
            elif state == "failed":
                # TOOL-dDeclaredLoop-81: a re-merge that failed is graded against every parent, no exemption:
                # each leaf M sets apart from some parent is owed, its old value the first such parent's.
                print("%s: push · %s graded against every parent — the clean re-merge failed: %s" % (SAY, sha8, why))
                refs = [parse_policy_bytes(blob) for blob in blobs]
                side = "at M" if b is None else "at parent %s" % c["parents"][refs.index(None)][:8] if None in refs else None
                changes = {}
                for r in [] if side else refs:
                    for k, v in mguard.derive_leaf_changes(r, b).items():
                        changes.setdefault(k, v)
                if not (side or changes):
                    continue
                graded += 1
                if side:
                    findings.append(unknown % side)
                    continue
            else:
                graded += 1
                # TOOL-dDeclaredLoop-59: with no clean re-merge a merge owes only a leaf its result sets to a
                # value no parent holds; a parent lacking the file, the first included, reads as {}.
                refs = [parse_policy_bytes(blob) for blob in blobs]
                if b is None or None in refs:
                    findings.append(unknown % ("on one side" if kind == "commit" else "at M" if b is None else
                                               "at parent %s" % c["parents"][refs.index(None)][:8]))
                    continue
                if why:
                    print("%s: push · %s graded against its parents only — %s" % (SAY, sha8, why))
                owed = set.intersection(*(set(mguard.derive_leaf_changes(r, b)) for r in refs))
                changes = {k: v for k, v in mguard.derive_leaf_changes(a, b).items() if k in owed}
            said, units = set(c["trailers"][TRAILER_KEY]), read_added_units(c["sha"], listed)
            for key, (o, n) in sorted(changes.items()):
                want, tag = render_policy_trailer(policy, key, o, n), derive_row_tag(policy, key)
                if want not in said:
                    findings.append("%s %s · %s · %s changed with no `%s: %s` trailer%s" % (
                        kind, sha8, mguard.POLICY, policy.render_dotted(key), TRAILER_KEY, want, own))
                if tag is None or tag not in units:
                    findings.append("%s %s · %s · %s changed and the %s adds no change record naming %s%s" % (
                        kind, sha8, mguard.POLICY, policy.render_dotted(key), kind,
                        tag or "its row, which no catalogue row is", own))
    except (LookupError, LoopError, OSError, ValueError, policy.Refusal) as e:
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
FX_PIN = '[verdict.remote]\npin = "%s"\n' % ("a" * 40)
FX_SIGNERS = '[verdict.peer]\nsigners = ["b ssh-ed25519 %s"]\n' % ("A" * 68)
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
    "pin-owner-only": "verdict.remote.pin under agents-with-reason, recorded with its decision row, on a branch no run names",
    "signers-owner-only": "verdict.peer.signers under agents-with-reason, recorded with its decision row, on a branch no "
                          "run names",
    "owner-only-live": "owner-only on a live run's branch",
    "push-no-trailer": "a commit changing the policy file with no Gov-Policy: line, graded by --push-range",
    "push-merge-carries-trailered": "a --no-ff merge taking a side's trailered, recorded policy change whole",
    "push-merge-resolution-edit": "a merge resolution setting review.max-rounds, with trailer and record, then neither",
    "push-merge-both-sides-clean": "a clean --no-ff merge of side's cap raise and main's review.max-rounds",
    "push-merge-equal-to-every-parent": "a --no-ff merge of a side and a main each committing a non-policy file, "
                                        "graded in process",
    "push-merge-conflict-pick": "a conflicting review.max-rounds resolved to side's value, the merge untrailered",
    "push-merge-octopus": "an octopus merge of b1 and b2, each branch and main setting a different key",
    "push-merge-revert-to-unchanged-side": "a run branch merging main and setting main's review.max-rounds back "
                                           "to the base's, with trailer and record, then neither",
    "push-merge-conflict-elsewhere": "push-merge-revert-to-unchanged-side with a file both sides add apart, so the "
                                     "re-merge exits 1 on that file alone, with trailer and record, then neither",
    "push-merge-resurrect-deleted-policy": "a run branch merging main, which deleted the policy file, and "
                                           "keeping its own file, untrailered",
    "push-merge-resurrect-deleted-policy-conflict-elsewhere": "push-merge-resurrect-deleted-policy with main also "
                                                              "adding fx-run.txt apart from the run's, so the merge "
                                                              "stops on that file alone, the run keeping both its "
                                                              "own files, untrailered",
    "push-merge-unparseable-parent": "an octopus merge of b1, setting review.max-rounds, and b2, declaring [review] "
                                     "twice, into main, which raises the cap, written by commit-tree, graded past b2",
    "push-merge-resurrect-emptied-policy": "a run branch merging main, which emptied the policy file, and "
                                           "keeping its own file, untrailered",
    "push-merge-both-absent": "a run branch merging main, which deleted the policy file, taking the deletion",
    "push-merge-unparseable-c": "main and a run branch each declaring [leases] apart, git's clean merge "
                                "declaring it twice, the run keeping its own file, untrailered",
    "push-merge-unrelated-histories": "an orphan run branch keeping the base's policy file, merged into main with "
                                      "--allow-unrelated-histories, with trailer and record, then neither",
    "push-merge-first-parent-lacks-policy": "an orphan branch lacking the policy file as a merge's first parent, "
                                            "main's file with review.max-rounds set as its result, then main "
                                            "deleting the policy file and merging a run branch that keeps it, each "
                                            "untrailered",
    "push-merge-tree-fatal": "a run branch merging main and keeping its own policy file, graded in process with "
                             "the clean re-merge exiting 128, then failing to start, failing to start with no "
                             "message and with an errno alone, killed by signal 9 and exiting 128 with no stderr, "
                             "then failing to start with a two-line message, graded on its first line alone",
    "push-merge-tree-fatal-unparseable-parent": "push-merge-tree-fatal with main declaring [review] twice, graded "
                                                "in process with the clean re-merge exiting 128",
    "push-merge-no-write-tree": "push-merge-both-sides-clean's history graded in process by a git with no "
                                "merge-tree --write-tree",
    "push-merge-probe-failed": "push-merge-tree-fatal's history graded in process by a git whose usage probe "
                               "cannot start",
    "push-merge-probe-silent": "push-merge-tree-fatal's history graded in process by a git whose usage probe "
                               "exits 129 with no usage text",
    "push-merge-probe-failed-trailered": "push-merge-probe-failed with the merge carrying review.max-rounds' "
                                         "trailer from 4 to none and its change record",
    "push-merge-probe-failed-unparseable-parent": "push-merge-tree-fatal-unparseable-parent's history graded in "
                                                  "process by a git whose usage probe cannot start",
    "push-merge-conflicted-unparseable-parent": "push-merge-tree-fatal-unparseable-parent's history, the merge "
                                                "keeping the run's policy file plus one comment line, graded in "
                                                "process with the clean re-merge conflicting on that file",
    "push-merge-probe-signal": "push-merge-tree-fatal's history graded in process by a git whose usage probe is "
                               "killed by signal 9",
    "push-merge-old-git-usage": "push-merge-both-sides-clean's history graded in process by a git whose usage "
                                "probe prints only the trivial form on standard error",
    "push-new-branch": "an all-zero base read as origin's default tip, then that tracking ref deleted and every "
                       "commit touching the policy file graded",
    "push-first-to-empty-remote": "a first push to a remote holding no ref: the policy file's add and one trailered, "
                                  "recorded change, then a merge resolution editing it with neither",
    "proof-signed-refuse": "policy_edit.py set policy-file.proof signed under refuse",
    "proof-signed-fallback": "policy_edit.py set policy-file.proof signed under fallback-reported",
    "set-run-live": "policy_edit.py set on a live run's branch, a key then a floor member",
    "floor-readers": "an unlisted actor witness and an unrecorded transition, under the floor on, then off",
    "write-guarded-rollback": "policy_edit.py's write_guarded, in process, its os.replace spied: a record refused, "
                              "a rename interrupted, a callable over its prior bytes",
}


def run_fixture_command(top, argv, **put):
    """A process in the scratch repository, `put` set in its environment: `(exit, stdout and stderr)`,
    standard error never a terminal."""
    p = subprocess.run(argv, cwd=top, capture_output=True, text=True, encoding="utf-8", errors="replace",
                       env=read_clean_env(**put))
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


def write_fixture_record(top, tag, build=FX_BUILD):
    """One change record naming `tag` under the build `build`, written through the memory-tree kit's door
    and staged."""
    read_memory_tree("build_records.py")
    import build_records
    rel = build_records.write_change(str(top), build, FX_UNIT, tag, "edit", "semantic", "none", "none",
                                     "none — fixture")
    run_fixture_git(top, "add", "--", rel)


def run_guard_plant(case, top):
    """The scenarios of `case` over the scratch at `top`: `[(scenario, exit, owed, needle, output)]`."""
    policy, mguard = read_policy_modules()
    me, out = [sys.executable, str(pathlib.Path(__file__).absolute())], []
    edit = [sys.executable, str(KIT / "policy_edit.py")]
    who = ["--build", FX_BUILD, "--unit", FX_UNIT]

    def run_scenario(name, argv, owed, needle, **put):
        rc, said = run_fixture_command(top, argv, **put)
        out.append((name, rc, owed, needle, said))

    def add_text(extra):
        return lambda t: t + extra

    def run_reset():
        run_fixture_git(top, "reset", "-q", "--hard")
        run_fixture_git(top, "clean", "-qfd")

    def run_grade_in_process(base, swaps, rows):
        """TOOL-dDeclaredLoop-81: `check_push_range(base, "HEAD")` in this process with `swaps` set on this
        module for that grade alone, the re-merge counted; one row per `(scenario, owed, needle)`."""
        import contextlib
        import io
        import unittest.mock
        real, runs, buf = swaps.get("run_merge_tree", run_merge_tree), [], io.StringIO()

        def run_counted_merge_tree(p1, p2):
            runs.append((p1, p2))
            return real(p1, p2)
        # TOOL-dDeclaredLoop-85: the probe's memo is cleared before the swaps and after them, so no grade
        # reads an answer another grade's twin or real probe left.
        resolve_write_tree_support.cache_clear()
        with contextlib.ExitStack() as stack:
            stack.callback(resolve_write_tree_support.cache_clear)
            stack.enter_context(contextlib.chdir(top))
            stack.enter_context(contextlib.redirect_stdout(buf))
            for attr, value in dict(swaps, run_merge_tree=run_counted_merge_tree).items():
                stack.enter_context(unittest.mock.patch.object(sys.modules[__name__], attr, value))
            rc = check_push_range(base, "HEAD")
        said = buf.getvalue() + "merge-tree runs: %d\n" % len(runs)
        sys.stdout.write(said)
        out.extend((name, rc, owed, needle, said) for name, owed, needle in rows)

    guard_value = {"with-reason-admitted": "agents-with-reason", "with-reason-no-row": "agents-with-reason",
                   "mandate-live": "agents-within-mandate", "mandate-none": "agents-within-mandate",
                   "pin-owner-only": "agents-with-reason", "signers-owner-only": "agents-with-reason"}.get(case)
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
    elif case in ("pin-owner-only", "signers-owner-only"):
        key, text = (("verdict.remote.pin", FX_PIN) if case == "pin-owner-only" else
                     ("verdict.peer.signers", FX_SIGNERS))
        write_staged(top, {mguard.POLICY: add_text(text)})
        write_fixture_record(top, "policy." + key)
        write_staged(top, {mguard.DECISIONS: add_text("- %s · %s set: the fixture\n" % (FX_UNIT, key))})
        run_scenario("judged", me + ["--staged"], 1, "%s: owner-only" % key)
    elif case == "push-no-trailer":
        base = run_fixture_git(top, "rev-parse", "HEAD")
        write_staged(top, {mguard.POLICY: add_text(FX_REVIEW)})
        write_fixture_record(top, "policy.review.max-rounds")
        run_fixture_git(top, "commit", "-q", "-m", "review rounds raised, no trailer")
        sha8 = run_fixture_git(top, "rev-parse", "--short=8", "HEAD")
        run_scenario("graded", me + ["--push-range", "%s..HEAD" % base], 1, "commit %s · %s" % (sha8, mguard.POLICY))
    elif case in ("push-merge-carries-trailered", "push-merge-resolution-edit"):
        # TOOL-dDeclaredLoop-44: a merge graded on its combined diff, its record read from that list.
        base = run_fixture_git(top, "rev-parse", "HEAD")
        trailer = ["-m", "%s: policy.review.max-rounds none -> 4" % TRAILER_KEY]
        clean = "1 changing %s · 0 finding(s)" % mguard.POLICY
        run_fixture_git(top, "checkout", "-q", "-b", "side")
        if case == "push-merge-carries-trailered":
            write_staged(top, {mguard.POLICY: add_text(FX_REVIEW)})
            write_fixture_record(top, "policy.review.max-rounds")
            run_fixture_git(top, "commit", "-q", "-m", "review rounds raised", *trailer)
            run_fixture_git(top, "checkout", "-q", "main")
            write_staged(top, {"fx-main.txt": add_text("main's own line\n")})
            run_fixture_git(top, "commit", "-q", "-m", "main's own commit")
            run_fixture_git(top, "merge", "-q", "--no-ff", "-m", "merge side", "side")
            n = run_fixture_git(top, "rev-list", "--count", "%s..HEAD" % base)
            run_scenario("graded", me + ["--push-range", "%s..HEAD" % base], 0, "%s commit(s) read · %s" % (n, clean))
        else:
            write_staged(top, {"fx-side.txt": add_text("side's own line\n")})
            run_fixture_git(top, "commit", "-q", "-m", "side's own commit")
            run_fixture_git(top, "checkout", "-q", "main")
            for name, recorded in (("with its trailer and record", True), ("with neither", False)):
                run_fixture_git(top, "merge", "-q", "--no-ff", "--no-commit", "side")
                write_staged(top, {mguard.POLICY: add_text(FX_REVIEW)})
                if recorded:
                    write_fixture_record(top, "policy.review.max-rounds")
                run_fixture_git(top, "commit", "-q", "-m", "merge side", *(trailer if recorded else []))
                sha8 = run_fixture_git(top, "rev-parse", "--short=8", "HEAD")
                run_scenario(name, me + ["--push-range", "%s..HEAD" % base], 0 if recorded else 1,
                             clean if recorded else "merge %s · %s · review.max-rounds" % (sha8, mguard.POLICY))
                run_fixture_git(top, "reset", "-q", "--hard", "HEAD~1")
    elif case in ("push-merge-both-sides-clean", "push-merge-conflict-pick", "push-merge-octopus",
                  "push-merge-revert-to-unchanged-side", "push-merge-conflict-elsewhere",
                  "push-merge-resurrect-deleted-policy", "push-merge-resurrect-deleted-policy-conflict-elsewhere",
                  "push-merge-resurrect-emptied-policy", "push-merge-both-absent", "push-merge-unparseable-c",
                  "push-merge-no-write-tree", "push-merge-old-git-usage", "push-merge-equal-to-every-parent",
                  "push-merge-unparseable-parent"):
        # TOOL-dDeclaredLoop-59: three keys in separate tables, unchanged lines between, so git merges an
        # edit of each cleanly; every non-merge commit carries its trailer and its change record, each
        # branch's records under a build of its own, since a build numbers its records and two branches
        # adding the same name would conflict.
        pad = "\n# fx: an unchanged line\n# fx: another\n\n"
        write_staged(top, {mguard.POLICY: add_text(pad + '[review]\nmax-rounds = 3\n' + pad +
                                                   '[review.design]\nrounds = "one"\n')})
        write_staged(top, {"memory/builds/%s/README.md" % b: add_text("# %s\n" % b) for b in ("tSide", "tB1", "tB2")})
        run_fixture_git(top, "commit", "-q", "-m", "the three tables")
        base = run_fixture_git(top, "rev-parse", "HEAD")
        cap = (("budgets", FX_CAP), '"%s" = 100\n' % FX_CAP, '"%s" = 120\n' % FX_CAP, 100, 120)
        design = (("review", "design", "rounds"), 'rounds = "one"\n', 'rounds = "until-clean"\n', "one", "until-clean")

        def derive_rounds(value):
            return ("review", "max-rounds"), "max-rounds = 3\n", "max-rounds = %d\n" % value, 3, value

        def write_key_commit(build, key, was_line, now_line, was, now):
            write_staged(top, {mguard.POLICY: lambda t: t.replace(was_line, now_line)})
            write_fixture_record(top, derive_row_tag(policy, key), build)
            run_fixture_git(top, "commit", "-q", "-m", "%s set" % policy.render_dotted(key),
                            "-m", "%s: %s" % (TRAILER_KEY, render_policy_trailer(policy, key, was, now)))

        if case in ("push-merge-both-sides-clean", "push-merge-no-write-tree", "push-merge-old-git-usage"):
            run_fixture_git(top, "checkout", "-q", "-b", "side")
            write_key_commit("tSide", *cap)
            run_fixture_git(top, "checkout", "-q", "main")
            write_key_commit(FX_BUILD, *derive_rounds(5))
            run_fixture_git(top, "merge", "-q", "--no-ff", "-m", "merge side", "side")
            # TOOL-dDeclaredLoop-81: the probe answers absence, so the re-merge never runs; TOOL-dDeclaredLoop-85:
            # the old git's trivial usage line on standard error is the one probe text read as absence.
            swap = {"push-merge-no-write-tree": {"resolve_write_tree_support": lambda: ("unsupported", "")},
                    "push-merge-old-git-usage": {"run_merge_tree_usage": lambda: (
                        129, "", "usage: git merge-tree <base-tree> <branch1> <branch2>\n")}}.get(case)
            if swap:
                run_grade_in_process(base, swap, [
                    ("graded", 0, "graded against its parents only — this git has no merge-tree --write-tree"),
                    ("graded, the re-merge count", 0, "merge-tree runs: 0")])
            else:
                run_scenario("graded", me + ["--push-range", "%s..HEAD" % base], 0,
                             "2 changing %s · 0 finding(s)" % mguard.POLICY)
        elif case == "push-merge-equal-to-every-parent":
            # TOOL-dDeclaredLoop-79 S23: the merge's blob equals both parents', so no re-merge runs
            for branch, rel in (("side", "fx-side.txt"), ("main", "fx-main.txt")):
                run_fixture_git(top, "checkout", "-q", *(["-b", branch] if branch == "side" else [branch]))
                write_staged(top, {rel: add_text("a line\n")})
                run_fixture_git(top, "commit", "-q", "-m", "%s's own file" % branch)
            run_fixture_git(top, "merge", "-q", "--no-ff", "-m", "merge side", "side")
            run_grade_in_process(base, {}, [("graded", 0, "0 finding(s)"),
                                            ("graded, the re-merge count", 0, "merge-tree runs: 0")])
        elif case == "push-merge-revert-to-unchanged-side":
            # TOOL-dDeclaredLoop-69: the merge's blob equals the run branch's, so the combined list never
            # names it; only the clean re-merge, holding main's value, sees the key set back.
            write_key_commit(FX_BUILD, *derive_rounds(5))
            tip = run_fixture_git(top, "rev-parse", "HEAD")
            back = "%s: %s" % (TRAILER_KEY, render_policy_trailer(policy, ("review", "max-rounds"), 5, 3))
            for variant, touched in (("another key", True), ("untouched", False)):
                run_fixture_git(top, "checkout", "-q", "-b", "run-%s" % variant.replace(" ", "-"), base)
                if touched:
                    write_key_commit("tSide", *cap)
                else:
                    write_staged(top, {"fx-run.txt": add_text("the run's own line\n")})
                    run_fixture_git(top, "commit", "-q", "-m", "the run's own commit")
                for name, recorded in (("with its trailer and record", True), ("with neither", False)):
                    run_fixture_git(top, "merge", "-q", "--no-ff", "--no-commit", "main")
                    run_fixture_git(top, "checkout", "HEAD", "--", mguard.POLICY)
                    if recorded:
                        write_fixture_record(top, derive_row_tag(policy, ("review", "max-rounds")), "tSide")
                    run_fixture_git(top, "commit", "-q", "-m", "merge main", *(["-m", back] if recorded else []))
                    sha8 = run_fixture_git(top, "rev-parse", "--short=8", "HEAD")
                    run_scenario("%s, %s" % (variant, name), me + ["--push-range", "%s..HEAD" % tip],
                                 0 if recorded else 1, "0 finding(s)" if recorded else
                                 "merge %s · %s · review.max-rounds" % (sha8, mguard.POLICY))
                    run_fixture_git(top, "reset", "-q", "--hard", "HEAD~1")
        elif case == "push-merge-conflict-elsewhere":
            # TOOL-dDeclaredLoop-75 S27: revert-to-unchanged-side with a file both sides add apart, so the re-merge
            # exits 1 on that file alone and its tree still holds the policy file's clean merge, main's value.
            write_key_commit(FX_BUILD, *derive_rounds(5))
            write_staged(top, {"fx-both.txt": lambda t: "main's line\n"})
            run_fixture_git(top, "commit", "-q", "-m", "main's own line")
            tip = run_fixture_git(top, "rev-parse", "HEAD")
            back = "%s: %s" % (TRAILER_KEY, render_policy_trailer(policy, ("review", "max-rounds"), 5, 3))
            run_fixture_git(top, "checkout", "-q", "-b", "run", base)
            write_staged(top, {"fx-both.txt": lambda t: "the run's line\n"})
            run_fixture_git(top, "commit", "-q", "-m", "the run's own line")
            for name, recorded in (("with its trailer and record", True), ("with neither", False)):
                rc, _said = read_git(top, "merge", "--no-ff", "--no-commit", "main")
                if rc != 1:
                    raise OSError("the conflict-elsewhere merge exited %d, not 1" % rc)
                write_staged(top, {"fx-both.txt": lambda t: "both lines\n"})
                run_fixture_git(top, "checkout", "HEAD", "--", mguard.POLICY)
                if recorded:
                    write_fixture_record(top, derive_row_tag(policy, ("review", "max-rounds")), "tSide")
                run_fixture_git(top, "commit", "-q", "-m", "merge main", *(["-m", back] if recorded else []))
                sha8 = run_fixture_git(top, "rev-parse", "--short=8", "HEAD")
                run_scenario(name, me + ["--push-range", "%s..HEAD" % tip], 0 if recorded else 1,
                             "0 finding(s)" if recorded else "merge %s · %s · review.max-rounds" % (sha8, mguard.POLICY))
                run_fixture_git(top, "reset", "-q", "--hard", "HEAD~1")
        elif case == "push-merge-unparseable-parent":
            # TOOL-dDeclaredLoop-82 S9: b2's policy file declares [review] twice, so it does not parse. An octopus
            # merge of it would not parse at M either, so M's tree is main's file with b1's value, written by
            # hand and joined to its three parents; the range starts at b2, whose own commit is graded elsewhere.
            run_fixture_git(top, "checkout", "-q", "-b", "b1")
            write_key_commit("tB1", *derive_rounds(4))
            run_fixture_git(top, "checkout", "-q", "-b", "b2", "main")
            write_staged(top, {mguard.POLICY: add_text("\n[review]\nmax-rounds = 7\n")})
            run_fixture_git(top, "commit", "-q", "-m", "a second [review] table")
            b2 = run_fixture_git(top, "rev-parse", "HEAD")
            run_fixture_git(top, "checkout", "-q", "main")
            write_key_commit(FX_BUILD, *cap)
            write_staged(top, {mguard.POLICY: lambda t: t.replace("max-rounds = 3\n", "max-rounds = 4\n")})
            merge = run_fixture_git(top, "commit-tree", run_fixture_git(top, "write-tree"), "-p", "HEAD", "-p", "b1",
                                    "-p", b2, "-m", "octopus")
            run_fixture_git(top, "reset", "-q", "--hard", merge)
            run_scenario("graded", me + ["--push-range", "%s..HEAD" % b2], 1, "does not parse at parent %s" % b2[:8])
            out.append(("graded, no Traceback", out[-1][1], 1, "Traceback absent" if "Traceback" in out[-1][4] else "",
                        out[-1][4]))
        elif case not in ("push-merge-conflict-pick", "push-merge-octopus"):
            # TOOL-dDeclaredLoop-78: main deletes, empties or declares a table the run branch also declares
            # apart; the run merges main and, but where both lack the file, keeps its own policy file, so the
            # merge's blob equals its first parent's and only the clean re-merge sees it. The range is the
            # one the run's landing pushes, so main's commit is outside it.
            leases = ("leases", "granularity")
            if case == "push-merge-unparseable-c":
                write_key_commit(FX_BUILD, leases, "[budgets]\n", '[leases]\ngranularity = "build"\n\n[budgets]\n',
                                 None, "build")
            elif case == "push-merge-resurrect-emptied-policy":
                write_staged(top, {mguard.POLICY: lambda t: ""})
                run_fixture_git(top, "commit", "-q", "-m", "the policy file emptied")
            else:
                run_fixture_git(top, "rm", "-q", "--", mguard.POLICY)
                if case == "push-merge-resurrect-deleted-policy-conflict-elsewhere":
                    write_staged(top, {"fx-run.txt": lambda t: "main's line\n"})
                run_fixture_git(top, "commit", "-q", "-m", "the policy file deleted")
            tip = run_fixture_git(top, "rev-parse", "HEAD")
            run_fixture_git(top, "checkout", "-q", "-b", "run", base)
            if case == "push-merge-unparseable-c":
                write_key_commit("tSide", leases, 'rounds = "one"\n', 'rounds = "one"\n\n[leases]\ngranularity = "unit"\n',
                                 None, "unit")
            else:
                write_staged(top, {"fx-run.txt": add_text("the run's own line\n")})
                run_fixture_git(top, "commit", "-q", "-m", "the run's own commit")
            if case == "push-merge-resurrect-deleted-policy-conflict-elsewhere":
                # TOOL-dDeclaredLoop-82 S4: git stops on fx-run.txt alone and the run takes its own side, so the
                # clean re-merge exits 1 with a tree lacking the policy file, read `absent`
                rc, _said = read_git(top, "merge", "--no-ff", "--no-commit", "main")
                if rc != 1:
                    raise OSError("the deleted-policy conflict-elsewhere merge exited %d, not 1" % rc)
                run_fixture_git(top, "checkout", "--ours", "--", "fx-run.txt")
                run_fixture_git(top, "add", "--", "fx-run.txt")
            else:
                run_fixture_git(top, "merge", "-q", "--no-ff", "--no-commit", "main")
            if case != "push-merge-both-absent":
                run_fixture_git(top, "checkout", "HEAD", "--", mguard.POLICY)
            run_fixture_git(top, "commit", "-q", "-m", "merge main")
            sha8 = run_fixture_git(top, "rev-parse", "--short=8", "HEAD")
            owed, needle = {"push-merge-both-absent": (0, "0 finding(s)"), "push-merge-unparseable-c": (
                1, "merge %s · %s does not parse at C" % (sha8, mguard.POLICY))}.get(
                case, (1, "merge %s · %s · review.max-rounds" % (sha8, mguard.POLICY)))
            run_scenario("graded", me + ["--push-range", "%s..HEAD" % tip], owed, needle)
        elif case == "push-merge-conflict-pick":
            run_fixture_git(top, "checkout", "-q", "-b", "side")
            write_key_commit("tSide", *derive_rounds(4))
            run_fixture_git(top, "checkout", "-q", "main")
            write_key_commit(FX_BUILD, *cap)
            write_key_commit(FX_BUILD, *derive_rounds(5))
            mine = run_fixture_git(top, "show", "HEAD:%s" % mguard.POLICY) + "\n"
            rc, _out = read_git(top, "merge", "--no-ff", "--no-commit", "side")
            if rc != 1:
                raise OSError("the conflict pick's merge exited %d, not 1" % rc)
            write_fixture_files(top, {mguard.POLICY: mine.replace("max-rounds = 5\n", "max-rounds = 4\n")})
            run_fixture_git(top, "add", "--", mguard.POLICY)
            run_fixture_git(top, "commit", "-q", "-m", "merge side")
            sha8 = run_fixture_git(top, "rev-parse", "--short=8", "HEAD")
            run_scenario("graded", me + ["--push-range", "%s..HEAD" % base], 0,
                         "%s graded against its parents only" % sha8)
        else:
            run_fixture_git(top, "checkout", "-q", "-b", "b1")
            write_key_commit("tB1", *derive_rounds(4))
            run_fixture_git(top, "checkout", "-q", "-b", "b2", "main")
            write_key_commit("tB2", *design)
            run_fixture_git(top, "checkout", "-q", "main")
            write_key_commit(FX_BUILD, *cap)
            run_fixture_git(top, "merge", "-q", "--no-ff", "-m", "octopus", "b1", "b2")
            sha8 = run_fixture_git(top, "rev-parse", "--short=8", "HEAD")
            run_scenario("graded", me + ["--push-range", "%s..HEAD" % base], 0,
                         "%s graded against its parents only" % sha8)
    elif case in ("push-merge-unrelated-histories", "push-merge-tree-fatal", "push-merge-tree-fatal-unparseable-parent",
                  "push-merge-probe-failed", "push-merge-probe-silent", "push-merge-probe-failed-trailered",
                  "push-merge-probe-failed-unparseable-parent", "push-merge-conflicted-unparseable-parent",
                  "push-merge-probe-signal"):
        # TOOL-dDeclaredLoop-81: main sets review.max-rounds and the run keeps the base's policy file, so the
        # merge's blob equals the run's and the combined list never names it; only the failed re-merge's
        # grade against every parent sees main's key dropped.
        base = run_fixture_git(top, "rev-parse", "HEAD")
        dropped = "merge %%s · %s · review.max-rounds" % mguard.POLICY
        back = "%s: %s" % (TRAILER_KEY, render_policy_trailer(policy, ("review", "max-rounds"), 4, None))
        fatal = case != "push-merge-unrelated-histories"
        if fatal:
            run_fixture_git(top, "checkout", "-q", "-b", "run")
            write_staged(top, {"fx-run.txt": add_text("the run's own line\n")})
            run_fixture_git(top, "commit", "-q", "-m", "the run's own commit")
            run_fixture_git(top, "checkout", "-q", "main")
        # TOOL-dDeclaredLoop-86 S6: main declaring [review] twice, so its policy blob does not parse
        twice = case.endswith("-unparseable-parent")
        trailered = case == "push-merge-probe-failed-trailered"
        write_staged(top, {mguard.POLICY: add_text(FX_REVIEW * (2 if twice else 1))})
        run_fixture_git(top, "commit", "-q", "-m", "review rounds set on main")
        tip = run_fixture_git(top, "rev-parse", "HEAD")
        if fatal:
            run_fixture_git(top, "checkout", "-q", "run")
            run_fixture_git(top, "merge", "-q", "--no-ff", "--no-commit", "main")
            run_fixture_git(top, "checkout", "HEAD", "--", mguard.POLICY)
            if case == "push-merge-conflicted-unparseable-parent":
                # TOOL-dDeclaredLoop-88 S19: the run's bytes plus one comment line, so the merge's file differs
                # from both parents and the combined diff lists it
                write_staged(top, {mguard.POLICY: add_text("# the merge's own line\n")})
            if trailered:   # TOOL-dDeclaredLoop-88 S17: the trailer and record the dropped key owes
                write_fixture_record(top, "policy.review.max-rounds")
            run_fixture_git(top, "commit", "-q", "-m", "merge main", *(["-m", back] if trailered else []))
            sha8 = run_fixture_git(top, "rev-parse", "--short=8", "HEAD")
            merged = run_fixture_git(top, "rev-parse", "HEAD^{tree}")

            def run_unstartable_usage():
                raise OSError("fx stand-in")

            def run_unstartable_lines():
                raise OSError("a\nb")
            # TOOL-dDeclaredLoop-85: a probe that cannot start, or exits 129 with no usage text, is a failed
            # re-merge graded against every parent, the re-merge itself never run.
            fatal_swap = {"run_merge_tree": lambda p1, p2: (128, "", "fatal: fx stand-in\n")}
            unstartable = ({"run_merge_tree_usage": run_unstartable_usage}, "probe failed: start failed: fx stand-in", 0)
            swap, said, n = {
                "push-merge-tree-fatal": (fatal_swap, "128 fatal: fx stand-in", 1),
                "push-merge-tree-fatal-unparseable-parent": (fatal_swap, "128 fatal: fx stand-in", 1),
                "push-merge-probe-failed": unstartable,
                "push-merge-probe-silent": ({"run_merge_tree_usage": lambda: (129, "", "")}, "probe failed: 129", 0),
                # TOOL-dDeclaredLoop-88 S17, S19, S26
                "push-merge-probe-failed-trailered": unstartable,
                "push-merge-probe-failed-unparseable-parent": unstartable,
                "push-merge-conflicted-unparseable-parent": ({"run_merge_tree": lambda p1, p2: (
                    1, "%s\n%s\n" % (merged, mguard.POLICY), "")}, "", 1),
                "push-merge-probe-signal": ({"run_merge_tree_usage": lambda: (-9, "", "")}, "probe failed: signal 9", 0),
            }[case]
            owed = 0 if trailered else 1
            rows = [("graded", owed, "the clean re-merge failed: %s" % said)] if said else []
            if twice:   # TOOL-dDeclaredLoop-86 S6: each branch refuses main's unparseable blob by its parent
                rows.append(("graded, the parent", 1, "merge %s · %s does not parse at parent %s" % (
                    sha8, mguard.POLICY, tip[:8])))
            elif trailered:
                rows.append(("graded, no finding", 0, "0 finding(s)"))
            else:
                rows.append(("graded, the key", 1, dropped % sha8))
            if case != "push-merge-tree-fatal-unparseable-parent":
                rows.append(("graded, the re-merge count", owed, "merge-tree runs: %d" % n))
            run_grade_in_process(tip, swap, rows)
            if case == "push-merge-tree-fatal":
                # TOOL-dDeclaredLoop-86 S22: a start that fails, a signal and an empty stderr, each spelled
                # TOOL-dDeclaredLoop-92 S17: an OSError with no text, and an errno alone, spelled by class or errno
                for name, swapped, spelled in (("start failed", run_unstartable_usage, "start failed: fx stand-in"),
                                               ("start failed, no message", lambda: (_ for _ in ()).throw(OSError()),
                                                "start failed: OSError"),
                                               ("start failed, an errno alone",
                                                lambda: (_ for _ in ()).throw(OSError(5, "")), "start failed: [Errno 5]"),
                                               ("signal", lambda: (-9, "", ""), "signal 9 (no stderr)"),
                                               ("no stderr", lambda: (128, "", ""), "128 (no stderr)")):
                    run_grade_in_process(tip, {"run_merge_tree": lambda p1, p2, f=swapped: f()}, [
                        ("graded, %s" % name, 1, "the clean re-merge failed: %s" % spelled)])
                # TOOL-dDeclaredLoop-94 S20: a two-line OSError is graded on its first line; the needle matches by
                # substring, so a second row, the `graded, no Traceback` idiom, misses where any line is `b`
                run_grade_in_process(tip, {"run_merge_tree": lambda p1, p2: run_unstartable_lines()}, [
                    ("graded, start failed, two lines", 1, "the clean re-merge failed: start failed: a")])
                out.append(("graded, start failed, two lines, the second line", out[-1][1], 1,
                            "no line b" if "b" in out[-1][4].splitlines() else "", out[-1][4]))
        else:
            run_fixture_git(top, "checkout", "-q", "--orphan", "run", base)
            run_fixture_git(top, "commit", "-q", "-m", "the orphan run")
            run_fixture_git(top, "checkout", "-q", "main")
            for name, recorded in (("with its trailer and record", True), ("with neither", False)):
                rc, _out = read_git(top, "merge", "--no-ff", "--no-commit", "--allow-unrelated-histories", "run")
                if rc != 1:
                    raise OSError("the unrelated-history merge exited %d, not 1" % rc)
                run_fixture_git(top, "checkout", "run", "--", mguard.POLICY)
                if recorded:
                    write_fixture_record(top, "policy.review.max-rounds")
                run_fixture_git(top, "commit", "-q", "-m", "merge run", *(["-m", back] if recorded else []))
                sha8 = run_fixture_git(top, "rev-parse", "--short=8", "HEAD")
                run_scenario(name, me + ["--push-range", "%s..HEAD" % tip], 0 if recorded else 1,
                             "0 finding(s)" if recorded else dropped % sha8)
                out.append(("%s, the failed line" % name, out[-1][1], out[-1][2], "the clean re-merge failed: 128",
                            out[-1][4]))
                run_fixture_git(top, "reset", "-q", "--hard", "HEAD~1")
    elif case == "push-merge-first-parent-lacks-policy":
        # TOOL-dDeclaredLoop-115: a merge whose first parent lacks the policy file is graded, never read as an
        # add. An orphan first parent, joined by commit-tree so git's merge cannot reorder it, fails its
        # re-merge on unrelated histories; a first parent that deleted the file re-merges `absent`.
        tip = run_fixture_git(top, "rev-parse", "HEAD")
        run_fixture_git(top, "checkout", "-q", "--orphan", "lacks")
        run_fixture_git(top, "rm", "-q", "-f", "--", mguard.POLICY)   # staged with no HEAD, so git wants -f
        run_fixture_git(top, "commit", "-q", "-m", "the orphan lacking the policy file")
        run_fixture_git(top, "checkout", "-q", "main")
        write_staged(top, {mguard.POLICY: add_text(FX_REVIEW)})
        merge = run_fixture_git(top, "commit-tree", run_fixture_git(top, "write-tree"), "-p", "lacks", "-p", "main",
                                "-m", "merge main onto the orphan")
        run_fixture_git(top, "reset", "-q", "--hard", merge)
        run_scenario("an orphan first parent", me + ["--push-range", "%s..HEAD" % tip], 1,
                     "merge %s · %s · review.max-rounds" % (merge[:8], mguard.POLICY))
        out.append(("an orphan first parent, the failed line", out[-1][1], 1, "the clean re-merge failed: 128",
                    out[-1][4]))
        run_fixture_git(top, "reset", "-q", "--hard", tip)
        run_fixture_git(top, "checkout", "-q", "-b", "run")
        write_staged(top, {"fx-run.txt": add_text("the run's own line\n")})
        run_fixture_git(top, "commit", "-q", "-m", "the run's own commit")
        run_fixture_git(top, "checkout", "-q", "main")
        run_fixture_git(top, "rm", "-q", "--", mguard.POLICY)
        run_fixture_git(top, "commit", "-q", "-m", "the policy file deleted")
        deleted = run_fixture_git(top, "rev-parse", "HEAD")
        run_fixture_git(top, "merge", "-q", "--no-ff", "--no-commit", "run")
        run_fixture_git(top, "checkout", "run", "--", mguard.POLICY)
        run_fixture_git(top, "commit", "-q", "-m", "merge run")
        sha8 = run_fixture_git(top, "rev-parse", "HEAD")[:8]
        run_scenario("a first parent that deleted the file", me + ["--push-range", "%s..HEAD" % deleted], 1,
                     "merge %s · %s · budgets." % (sha8, mguard.POLICY))
    elif case == "push-new-branch":
        write_staged(top, {mguard.POLICY: add_text(FX_REVIEW)})
        run_fixture_git(top, "commit", "-q", "-m", "review rounds raised, no trailer")
        raised8 = run_fixture_git(top, "rev-parse", "--short=8", "HEAD")
        run_fixture_git(top, "remote", "add", "origin", "fx-none.invalid")
        tracking = "refs/remotes/%s/main" % run_fixture_git(top, "remote")   # the name read back, never spelled
        run_fixture_git(top, "update-ref", tracking, "HEAD")
        run_fixture_git(top, "symbolic-ref", tracking.rsplit("/", 1)[0] + "/HEAD", tracking)
        write_staged(top, {"fx-clean.txt": add_text("one clean line\n")})
        run_fixture_git(top, "commit", "-q", "-m", "one clean commit")
        n = run_fixture_git(top, "rev-list", "--count", tracking + "..HEAD")
        zero, unset = ["--push-range", "%s..HEAD" % ("0" * 40)], {"GOV_REMOTE": "", "GOV_DEFAULT_BRANCH": ""}
        run_scenario("the all-zero base", me + zero, 0, "push · %s commit(s) read · 0 changing" % n, **unset)
        run_fixture_git(top, "update-ref", "-d", tracking)
        # TOOL-dDeclaredLoop-67 S33: no landed revision now grades the policy file's history, naming the raise
        run_scenario("the tracking ref deleted", me + zero, 1, "commit %s · %s" % (raised8, mguard.POLICY), **unset)
    elif case == "push-first-to-empty-remote":
        # TOOL-dDeclaredLoop-67 AC23: a remote holding no ref names no landed revision, so the policy file's history
        # is graded: its add is not, a trailered, recorded change is clean, an untrailered merge resolution is not
        run_fixture_git(top, "remote", "add", "origin", "fx-none.invalid")
        write_staged(top, {mguard.POLICY: add_text(FX_REVIEW)})
        write_fixture_record(top, "policy.review.max-rounds")
        run_fixture_git(top, "commit", "-q", "-m", "review rounds raised", "-m",
                        "%s: policy.review.max-rounds none -> 4" % TRAILER_KEY)
        zero, unset = ["--push-range", "%s..HEAD" % ("0" * 40)], {"GOV_REMOTE": "", "GOV_DEFAULT_BRANCH": ""}
        run_scenario("the add and a trailered change", me + zero, 0, "push · no landed revision (", **unset)
        out.append(("the add and a trailered change, the count", out[-1][1], 0,
                    "push · 2 commit(s) read · 1 changing %s · 0 finding(s)" % mguard.POLICY, out[-1][4]))
        run_fixture_git(top, "checkout", "-q", "-b", "side")
        write_staged(top, {"fx-side.txt": add_text("side's own line\n")})
        run_fixture_git(top, "commit", "-q", "-m", "side's own commit")
        run_fixture_git(top, "checkout", "-q", "main")
        run_fixture_git(top, "merge", "-q", "--no-ff", "--no-commit", "side")
        write_staged(top, {mguard.POLICY: lambda text: text.replace("max-rounds = 4", "max-rounds = 5")})
        run_fixture_git(top, "commit", "-q", "-m", "merge side")
        sha8 = run_fixture_git(top, "rev-parse", "--short=8", "HEAD")
        run_scenario("a merge resolution with neither", me + zero, 1,
                     "merge %s · %s · review.max-rounds" % (sha8, mguard.POLICY), **unset)
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
    elif case == "write-guarded-rollback":
        # TOOL-dDeclaredLoop-43: in process over the loop kit's copy of the block, so the spy sees each rename.
        import unittest.mock
        import policy_edit
        target = pathlib.Path(top, mguard.POLICY)
        absent = pathlib.Path(top, "fx-absent", "policy.toml")
        committed, real_replace, handed = target.read_bytes(), policy_edit.os.replace, []

        def run_spy(arm=None):
            renamed = []

            def run_replace(src, dst):
                renamed.append(pathlib.Path(dst))
                if arm is not None and len(renamed) == 1:
                    raise arm
                return real_replace(src, dst)
            return renamed, unittest.mock.patch.object(policy_edit.os, "replace", run_replace)

        def read_temps(folder):
            return sorted(folder.glob("policy.toml.*.tmp"))

        def run_refused_record():
            raise OSError("fx: record refused")

        def write_appended(path):
            handed.append(path)
            path.write_bytes(path.read_bytes() + b"# fx appended\n")

        def check_scenario(name, checks):
            said = "".join("%s: %s · %s\n" % (SAY, label, "held" if ok else "MISSED") for label, ok in checks)
            held = all(ok for _label, ok in checks)
            said += "%s: bytes held\n" % SAY if held else ""
            sys.stdout.write(said)
            out.append((name, 0 if held else 1, 0, "bytes held", said))

        for name, path in (("record refused over a prior file", target), ("record refused, no prior file", absent)):
            renamed, spy = run_spy()
            reached = False
            try:
                with spy:
                    policy_edit.write_guarded(path, committed.decode("utf-8") + "# fx new\n", run_refused_record)
            except OSError as e:
                reached = "fx: record refused" in str(e)
            after = [("the record's error reached the caller", reached),
                     ("no temp sibling remains", not read_temps(path.parent))]
            if path == target:
                after += [("the policy file's bytes equal the committed bytes", target.read_bytes() == committed),
                          ("two renames onto it", renamed == [target, target])]
            else:
                after += [("the path does not exist", not path.exists()), ("one rename onto it", renamed == [path])]
            check_scenario(name, after)
        renamed, spy = run_spy(KeyboardInterrupt())
        reached = False
        try:
            with spy:
                policy_edit.write_guarded(target, "# fx interrupted\n", lambda: "fx-record")
        except KeyboardInterrupt:
            reached = True
        check_scenario("interrupted at the rename", [
            ("the interrupt reached the caller", reached),
            ("the policy file holds the committed bytes", target.read_bytes() == committed),
            ("no temp sibling remains", not read_temps(target.parent))])
        renamed, spy = run_spy()
        with spy:
            got = policy_edit.write_guarded(target, write_appended, lambda: "fx-record")
        check_scenario("a callable over its prior bytes", [
            ("the policy file is the committed bytes plus the line", target.read_bytes() == committed + b"# fx appended\n"),
            ("the handed path is a sibling, not the target",
             len(handed) == 1 and handed[0].parent == target.parent and handed[0] != target),
            ("record()'s value returned", got == "fx-record"),
            ("no temp sibling remains", not read_temps(target.parent))])
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
            "other-write-owner-only": 1, "with-reason-no-row": 1, "mandate-none": 1, "pin-owner-only": 1, "signers-owner-only": 1,
            "push-no-trailer": 1,
            "proof-signed-refuse": 2, "proof-signed-fallback": 1, "push-merge-resolution-edit": 1,
            "push-merge-revert-to-unchanged-side": 1, "push-merge-conflict-elsewhere": 1,
            "push-merge-resurrect-deleted-policy": 1, "push-merge-resurrect-deleted-policy-conflict-elsewhere": 1,
            "push-merge-unparseable-parent": 1, "push-merge-resurrect-emptied-policy": 1,
            "push-merge-unparseable-c": 1, "push-new-branch": 1,
            "push-first-to-empty-remote": 1,
            "push-merge-unrelated-histories": 1, "push-merge-first-parent-lacks-policy": 1, "push-merge-tree-fatal": 1,
            "push-merge-tree-fatal-unparseable-parent": 1, "push-merge-probe-failed": 1,
            "push-merge-probe-silent": 1, "push-merge-probe-failed-unparseable-parent": 1,
            "push-merge-conflicted-unparseable-parent": 1, "push-merge-probe-signal": 1}
    cases = [(case, ["--fixture", "--plant", case], owed.get(case, 0), "%s: fixture · plant %s · " % (SAY, case),
              "all held") for case in PLANTS]
    return run_selftest_cases(main, cases, "%s: selftest" % SAY)


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="guard.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("--staged", action="store_true", help="judge the staged change of an agent's commit")
    ap.add_argument("--push-range", help="<base>..<tip>: grade each commit's Gov-Policy trailers and records")
    ap.add_argument("--expansion", action="store_true", help="judge <key>=<toml value> lines on stdin by the expansion rule")
    ap.add_argument("--fixture", action="store_true", help="run one plant's scenarios in a scratch repository")
    ap.add_argument("--plant", choices=list(PLANTS))
    ap.add_argument("--selftest", action="store_true", help="run every plant")
    args = ap.parse_args(argv)
    modes = [args.staged, args.push_range is not None, args.expansion, args.fixture, args.selftest]
    if sum(modes) != 1 or args.fixture != bool(args.plant):
        ap.error("one of --staged, --push-range <base>..<tip>, --expansion, --fixture --plant <case> or --selftest")
    if args.expansion:
        if hasattr(sys.stdin, "reconfigure"):
            sys.stdin.reconfigure(encoding="utf-8", errors="replace")
        return run_expansion(sys.stdin)
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
