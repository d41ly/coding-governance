#!/usr/bin/env python3
"""deviation_join.py — every departure from the frozen design joined to a typed deviation record.

TOOL-dTrueNorth-4. A spec and its code could move together with no reason or approver any check
read (`gap-build-07`). This module computes the departures from history, never from a declaration,
and joins each to a deviation record: at the commit, through the routed-commit attribution, and at
the close. It is the product successor of the bootstrap instrument `deviations.py`'s population and
join (the dClosedLoop build's records, blob `93e7a492`), and of no other part of it: the departures
report stays the instrument's.

THE RECORD is one file, `<MEMORY_ROOT>/builds/<build>/build/<date>-build-<unit id>-deviation-<n>.md`,
in the departing build's `build/` folder, `<n>` unique within its build, its id the file's stem, its
`**Serves:**` kind `deviation`. Its fields are bold-key bullets read with the instrument's field
regex, so the two read one value: Departs from, Hand-off, Before, After, Cause, Reason, Evidence,
Risk, Approver, Follow-through and Caused-by, with Bound, Tier, Surface and Supersedes optional.
`**Supersedes:**` holds one record id, the stem `<date>-build-<unit id>-deviation-<n>` of another
record, which the newer of two amends of one clause names to order them (TOOL-dTrueNorth-18): the
as-built view's head rule reads it. `read_record` grades one against the closed sets below and names
each malformed field; it returns the fields whatever it found, so a reader of `**After:**` reads a
malformed record as the instrument does. An `**After:**` holding a `|` is malformed, because the view
renders it as its clause row's Text cell and the pipe would split that cell in two (TOOL-dTrueNorth-16
S22); the view renders that clause from the baseline and reports the record.

THE POPULATION, six arms over the chain builds' specs, the chain builds being the Build column of
`DESIGN_VIEW`, their specs and records the TRACKED files `design_lib.read_tracked_builds` lists, as
the records tables read them, and a spec a file `design_lib.build_spec_file_re` names, the predicate
the revision reader refuses by (TOOL-dTrueNorth-26 S5, S7); each member carries an address, its
hand-off and its departing commit:
  - a spec revision that is not an ancestor of its unit's FIRST PASS, `<unit>@rev-N`, N the header
    revision the commit changed;
  - a spec revision that is not an ancestor of the commit adding the newest `spec-audit` record whose
    `**Serves:**` pins `<unit>@rev-N`, read from `tree_lib.read_bindings`' `pins`;
  - an `amended rev-N` ledger line under an `**Evidences:** <unit>` block of a `journal` record,
    `<unit>@rev-<N-1>`;
  - a divergence hand-back, a `prompts/` record whose `### Goal` opens `DIVERGENCE:`;
  - a rescope row of a chain build's `RUN.md` or rotated `RUN.*.md`, but a `defer` row, dated by the
    oldest commit changing its count anywhere in its build folder, so a row dates alike from the live
    file and from an archive (TOOL-dTrueNorth-24);
  - a clause of `DESIGN_RECORD`'s `[chain]` whose hash at HEAD differs from its hash at
    `DESIGN_BASELINE`, or that is new or absent at HEAD; and the record's `Baseline:` line differing
    from `DESIGN_BASELINE`, listed first and joined by no record.
Both revision arms exempt a revision whose text is unchanged once its `**Status:**` line and every
generated region are stripped, the strip being the unattended kit's `GEN_REGION_AWK`, read from
`lib-unattended.sh` and never copied, the kit found by `backlog.resolve_kit_dir` or by a resolver a
caller injects (`read_gen_region_awk`, TOOL-dTrueNorth-12). The strip resolves as the population's
first act, once per process, so a kit that does not resolve is nothing measured whatever the history
holds: a population read without it would count a status-only revision as a member.

THE FIRST PASS is the oldest commit, by committer date, among those `routed_commits.read_routed_commits`
returns for HEAD that carry a `Pass:` trailer naming the unit (`Pass: none` names none), or carry no
`Pass:` trailer, name the unit as a whole token of the subject and write a path under `ROUTED_PATHS`.
That is the trailer-replaces-subject reading, the instrument's `read_first_pass` and THE UNATTENDED
DRIVER'S PASS RULE, the one `read_attribution_tokens` and `pass_commit` in its kit apply: a commit whose
subject names X and whose trailer names Y is Y's pass and no pass of X. It deliberately differs from the
union `routed_commits.py` attributes by (its docstring's ATTRIBUTION paragraph), because that leg answers
whether a commit names any unit, not which unit's pass it is (TOOL-dTrueNorth-16 S13).

THE JOIN. A member joins the record departing from its address, an `add` member the record whose
`**Follow-through:**` is `new unit <id>`. Each record's approver is graded under one approval value:
`author-recorded`, the chain's (decision `PLAY-dClosedLoop-4`), or `by-risk`, the table final-questions
`[deviation]` sets. Both refuse an approver opening with no role the grammar names, and an owner
approver citing no decision id whose row `<MEMORY_ROOT>/DECISIONS.md` holds on the mainline the remote
ladder resolves (`read_decision_ref`) and names the record's departed clause or its new unit, so a run
cannot approve itself with a row it minted on its own branch. `by-risk` also refuses a role below its
risk class, the risk read from the record.

AT THE COMMIT AND AT THE CLOSE, hosted in `routed_commits.py` over the two populations it already
grades: its RANGE half asks, for each member departing in `$GATE_PUSH_BASE..HEAD`, whether its joining
record is present in that commit's tree, in ONE `git cat-file --batch-check`; its WHOLE half joins
every member at HEAD, grades every approver, and runs the commit join over every sha. The host runs
the chain's values, `report` and `author-recorded`: it lists and never moves the leg's exit.

Usage (from the worktree root):
  python deviation_join.py [--policy report|refuse] [--approval author-recorded|by-risk] [--range A..B]
  python deviation_join.py --fixture [--plant <case>] [--policy ...] [--approval ...]
  python deviation_join.py [--fixture [--plant <case>]] --host routed-commits
  python deviation_join.py --selftest
With no `--range` the commit join reads every commit. `--host routed-commits` calls
`routed_commits.check_routed_commits` in-process and prints the host's lines, over the fixture with
`GATE_PUSH_BASE` set to its base, over the tree with the process environment. `--fixture` builds a
temporary repository with every plant, or the base and one plant; `--selftest` runs every plant
against the exit it must take, then every plant but `unmeasured` composed, the arms
`routed_commits.py --selftest` also runs. The fixture's design is its own (TOOL-dTrueNorth-12 S3),
written by `design_lib.write_design_fixture`, the builder the as-built view's fixture writes its design
with too (TOOL-dTrueNorth-16 S19): two builds, `dFixA` holding every folder the fixture writes, and one
`[chain]` clause per clause-moving role, so plants compose; nothing reads this tree's design. The two
`unmeasured-*` plants stand alone and are left out of every-plant runs. Where the unattended kit
does not resolve, `--fixture` and the arms print one `deviation: SKIP` line naming why and the plants
that read the strip, `STRIP_PLANTS`, and run every other plant under the strip stubbed to the
identity, set for that call alone; the host's path in that call reads it too.
Exit 0 green or `report` · 1 on any finding under `refuse` · 2 nothing measured.

ITS STATES ARE THE KEY RULE's, `design_lib.read_design_keys` (TOOL-dTrueNorth-16 S5): OFF when all
four `DESIGN_*` keys are blank or absent, one line and no history read; a partial set, or a
`DESIGN_BASELINE` naming no commit, is nothing measured, exit 2, naming the key. The keys are gov's,
declared blank in the kit's example conf, which is off, so an adopter's join reads them as off.
NOTHING MEASURED, exit 2,
on each cause alone (S23): the unattended kit does not resolve; the baseline names no commit, or no
commit holding the record, whatever the specs; or the pin reads and no chain-build spec exists.
COST, armed: one read of the kit's library, the two git spawns of `design_lib.read_spec_revisions`
over every chain-build spec, the one revision reader the carries join reads too (S12), one strip per
revision past a pass or a pin, one blob batch for the rescope and hand-back rows, and one pickaxe log
per ledger line and rescope row; it grows with the chain-build specs' revisions, where the host's own
leg is constant.

What it does not read: whether a record's reason is true or its risk class honest, which the
approver and the closing review judge; a departure in code that changes no spec; a hand edit inside a
generated region, which the strip cannot tell from a render; and the departures report, which stays
the instrument's.
"""
from __future__ import annotations

import argparse
import datetime
import functools
import hashlib
import os
import pathlib
import re
import shutil
import stat
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True

KIT = pathlib.Path(__file__).resolve().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
import row_grammar  # noqa: E402  the kit's decision-row grammar
import routed_commits  # noqa: E402  the host: its log pass, its routed-path test and its pinned git runner
from design_lib import (  # noqa: E402  the one parser of the design, and its clause-id grammar
    _CL, DESIGN_KEYS, DesignRefusal, read_chain_clauses, read_design_keys, read_design_view, read_spec_revisions,
    read_tracked_builds, scan_chain_specs, write_design_fixture)
from tree_lib import HDR_RE, parse_conf, parse_spec_h1, read_adding_commits, read_bindings, read_blobs_at  # noqa: E402

SAY = "deviation"
POLICIES = ("report", "refuse")
APPROVALS = ("author-recorded", "by-risk")
HOST_POLICY, HOST_APPROVAL = "report", "author-recorded"   # the chain's values, PLAY-dClosedLoop-4
FIELD = re.compile(r"^- \*\*([A-Z][a-z-]+(?: [a-z]+)?):\*\* (.+)$")     # deviations.py:123
REQUIRED = ("Departs from", "Hand-off", "Before", "After", "Cause", "Reason", "Evidence", "Risk", "Approver",
            "Follow-through", "Caused-by")
HANDS = ("design-to-spec", "design-revised", "spec-revised", "spec-to-code", "code-to-record")
CAUSES = ("design defect", "owner ruling", "builder discovery", "review finding", "external")
RISKS = ("editorial", "additive", "stricter", "loosening", "breaking")
ROLES = ("spec writer", "author", "owner")      # the record grammar's approver roles, the longest first
RANK = {"author": 0, "spec writer": 1, "owner": 2}
LEAST = {"editorial": "author", "additive": "spec writer", "stricter": "spec writer", "loosening": "owner",
         "breaking": "owner"}                   # final-questions `[deviation]`, the by-risk table
_ID =r"[A-Za-z]+-[A-Za-z0-9]+-\d+"
DEPARTS = re.compile(r"^(`?)(?:" + _CL + r"@[0-9a-f]{8}|" + _ID + r"@rev-\d+|d[A-Z]\w+)\1(?: \[[^\]]+\])?$")
FOLLOW = re.compile(r"^(?:amends " + _CL + r"@[0-9a-f]{8}|supersedes " + _CL + r"@[0-9a-f]{8} by " + _CL
                    + r"|new unit " + _ID + r"|(?:gap|ask|usage) \S+)$")
_STEM = r"\d{4}-\d{2}-\d{2}-build-" + _ID + r"-deviation-"      # a record's stem, its <n> following
RECORD_NAME = re.compile(r"(?:^|/)builds/(?P<build>[^/]+)/build/" + _STEM + r"(?P<n>\d+)\.md$")
SUPERSEDES = re.compile(r"(`?)(" + _STEM + r"\d+)\1")           # one record id, quoted or bare
RESCOPE = re.compile(r"^\S+ rescope · item (add|retire|supersede|defer) (\S+)(?: -> (\S+))? · reason (.*)$", re.M)
LEDGER = re.compile(r"^- (\S+) — amended rev-(\d+)\b")
RUN_FILE = re.compile(r"^RUN(?:\.[^/]+)?\.md$")
DIVERGENCE = re.compile(r"^### Goal[ \t]*\n(?:[ \t]*\n)*DIVERGENCE:", re.M)


class Unmeasured(Exception):
    """Nothing measured: exit 2 on the CLI, the host's Refusal in the leg."""


def run_git(root, *args, stdin=None):
    """One pinned git call through the host's counted runner: stdout bytes, or None on a non-zero exit."""
    return routed_commits.run_git(root, *args, stdin=stdin, may_fail=True)


def read_join_state(root, conf):
    """`(armed, why)` by the key rule, `design_lib.read_design_keys` (TOOL-dTrueNorth-16 S5): off, with no
    git call, when all four `DESIGN_*` keys are blank; armed when all four are set and the pin names a
    commit. A partial set, or a pin naming no commit, is Unmeasured naming the key."""
    try:
        values = read_design_keys(root, conf)
    except DesignRefusal as exc:
        raise Unmeasured(str(exc)) from None
    if values is None:
        return False, f"{', '.join(DESIGN_KEYS)} are blank in .memory-tree.conf, so the join reads no history"
    return True, ""


# ------------------------------------------------------------------------------------- the record
def read_record(path, text):
    """One record: its fields, keyed for the join, and `malformed`, `[(field, why)]` naming each field
    the grammar refuses. The fields are returned whatever that list holds."""
    lines = text.replace("\r\n", "\n").split("\n")
    fields, bad, seen = {}, [], {}
    for n, ln in enumerate(lines):
        m = FIELD.match(ln)
        if not m:
            continue
        key, value = m.group(1), m.group(2).strip()
        if key in seen:
            bad.append((key, f"is given twice, at lines {seen[key]} and {n + 1}"))
            continue
        seen[key] = n + 1
        fields[key] = value
        nxt = lines[n + 1] if n + 1 < len(lines) else ""
        if key in ("Before", "After") and nxt.strip() and not nxt.startswith(("- **", "#")):
            bad.append((key, "runs past its one line"))
        if key == "After" and "|" in value:
            bad.append((key, "holds a `|`: the as-built view renders **After:** as the Text cell of its "
                             "clause's row, and the pipe would split that cell in two"))
    name = RECORD_NAME.search(path)
    if not name:
        bad.append(("file name", "is not <date>-build-<unit id>-deviation-<n>.md in a build's build/ folder"))
    bad += [(k, "is missing") for k in REQUIRED if k not in fields]
    for key, allowed in (("Hand-off", HANDS), ("Cause", CAUSES), ("Risk", RISKS)):
        if key in fields and fields[key] not in allowed:
            bad.append((key, f"{fields[key]} is outside {' · '.join(allowed)}"))
    if "Departs from" in fields and not DEPARTS.match(fields["Departs from"]):
        bad.append(("Departs from", f"{fields['Departs from']} is no <clause id>@<hash8>, <unit>@rev-N or build slug"))
    follow = fields.get("Follow-through", "")
    if follow and not FOLLOW.match(follow):
        why = ("names no clause at an eight-hex hash" if re.match(r"(amends|supersedes)\b", follow) else
               "is outside amends · supersedes · new unit · gap · ask · usage, written unquoted")
        bad.append(("Follow-through", f"{follow} {why}"))
    if "Caused-by" in fields and not re.fullmatch(r"`?[^\s`]+`?", fields["Caused-by"]):
        bad.append(("Caused-by", f"{fields['Caused-by']} is not one id"))
    supersedes = fields.get("Supersedes")
    named = SUPERSEDES.fullmatch(supersedes or "")
    if supersedes is not None and not named:
        bad.append(("Supersedes", f"{supersedes} is not one record id: **Supersedes:** names the stem "
                                  "<date>-build-<unit id>-deviation-<n> of another record"))
    elif named and named.group(2) == pathlib.PurePosixPath(path).stem:
        bad.append(("Supersedes", f"{supersedes} names the record itself: **Supersedes:** names another record"))
    return {"id": pathlib.PurePosixPath(path).stem, "path": path,
            "build": name.group("build") if name else None, "n": int(name.group("n")) if name else None,
            "departs": fields.get("Departs from", ""),
            "address": fields.get("Departs from", "").split(" [")[0].strip("` "),
            "hand": fields.get("Hand-off", ""), "before": fields.get("Before"), "after": fields.get("After"),
            "cause": fields.get("Cause", ""), "reason": fields.get("Reason"), "evidence": fields.get("Evidence"),
            "risk": fields.get("Risk", ""), "approver": fields.get("Approver"),
            "follow": fields.get("Follow-through", ""), "caused_by": fields.get("Caused-by"),
            "bound": fields.get("Bound"), "tier": fields.get("Tier"), "surface": fields.get("Surface"),
            "supersedes": named.group(2) if named else supersedes, "malformed": bad}


def read_records(root, conf):
    """Every TRACKED path the instrument's glob names, `<MEMORY_ROOT>/builds/*/build/*-deviation-*.md`,
    sorted by path and each read by `read_record` from its working copy; two files of one build at one
    `<n>` are each malformed, naming the other.

    The population is `design_lib.read_tracked_builds`', the one the records tables read through
    `gen_build_index.plan()`, so an untracked draft moves neither the view nor the join, and a record
    staged and not committed is read (TOOL-dTrueNorth-26 S7). A tracked path absent from the working
    tree is read as absent. A failed `ls-files` is its `DesignRefusal`, which each caller maps."""
    memory_root = (conf.get("MEMORY_ROOT") or "memory").strip().strip("/")
    glob = re.compile(re.escape(memory_root) + r"/builds/[^/]+/build/[^/]*-deviation-[^/]*\.md")
    records = []
    for rel in sorted(p for p in read_tracked_builds(root, memory_root) if glob.fullmatch(p)):
        p = pathlib.Path(root, rel)
        if p.is_file():
            records.append(read_record(rel, p.read_bytes().decode("utf-8", "replace")))
    shared = {}
    for r in records:
        if r["n"] is not None:
            shared.setdefault((r["build"], r["n"]), []).append(r)
    for (_b, n), group in shared.items():
        for r in group if len(group) > 1 else ():
            others = ", ".join(o["path"] for o in group if o is not r)
            r["malformed"].append(("file name", f"shares deviation-{n} with {others}"))
    return records


# ------------------------------------------------------------------------------------ the history
def read_blobs(root, requests):
    """`{(rev, path): text, or None}` for every `(rev, path)` pair, through `tree_lib.read_blobs_at`, the
    kit's one blob-batch parser (TOOL-dTrueNorth-26 S17): None for an object the rev does not hold, one
    that is not a blob and one that is not UTF-8, the absence each caller already reads as a legal
    answer. Only the reader's `OSError`, a failed call or a stream short of a request, is Unmeasured."""
    try:
        return read_blobs_at(root, requests)
    except OSError as exc:
        raise Unmeasured(f"the blobs of {len(requests)} revision(s) could not be read: {exc}") from None


def read_commit_times(commits):
    """`{sha: aware datetime}` of each commit's committer date."""
    return {c["sha"]: datetime.datetime.fromisoformat(c["date"].replace("Z", "+00:00")) for c in commits}


def read_ancestors(parents, sha, cache):
    """`sha` and every commit reachable from it, walked over the parent map the log pass read."""
    if sha not in cache:
        seen, todo = set(), [sha]
        while todo:
            s = todo.pop()
            if s not in seen:
                seen.add(s)
                todo.extend(parents.get(s, ()))
        cache[sha] = seen
    return cache[sha]


def read_first_passes(commits, units, entries, when):
    """`{unit: sha}`, each unit's first pass (S5): the oldest commit, by committer date, carrying a
    `Pass:` trailer naming it, or carrying none, naming it in its subject and writing a routed path."""
    first = {}
    for c in commits:
        if c["trailer"]:
            names = re.sub(r"[^A-Za-z0-9-]", " ", c["trailer"]).split()
            named = set() if "none" in names else units.intersection(names)
        elif any(routed_commits.test_routed_path(p, entries) for p in c["paths"]):
            named = units.intersection(re.sub(r"[^A-Za-z0-9-]", " ", c["subject"]).split())
        else:
            named = set()
        for u in named:
            if u not in first or when[c["sha"]] <= when[first[u]]:
                first[u] = c["sha"]
    return first


def read_row_commit(root, row, path):
    """The oldest commit whose diff changes the count of `row` under `path`, `git log --reverse -S` as
    `deviations.py:378-380` finds it. THE PATH IS EACH CALLER'S (TOOL-dTrueNorth-24 S1). The rescope arm
    passes the row's build folder, `<MEMORY_ROOT>/builds/<build>`, as the instrument's
    `scan_rescope_members` does: the oldest commit changing the row's count anywhere in that folder is the
    one that wrote it into `RUN.md`, so a row dates alike from the live file and from a rotated
    `RUN.<phase>.<blob8>.md`, where a pickaxe over the archive alone answers the commit that rotated it.
    The ledger arm passes the one journal record the line sits in: a journal record is never rotated, and
    two ledgers of one build folder can hold one ledger line's text, so a folder pickaxe there would date
    the line by the other record's commit."""
    out = (run_git(root, "log", "--reverse", "--format=%H", f"-S{row}", "HEAD", "--", path) or b"").split()
    return out[0].decode("ascii") if out else None


def read_gen_region_awk(resolve=None):
    """The value of the `GEN_REGION_AWK=` assignment in the unattended kit's `lib-unattended.sh`, read from
    the file and never copied into this module, so check 23 and this join strip one way (P0.1 row 8a). The
    kit is the one `backlog.resolve_kit_dir` finds, or `resolve`'s, a stand-in a caller injects taking the
    same three arguments, as `gen_build_index.read_landed_unclosed` takes one (TOOL-dTrueNorth-12 S1). A kit
    that does not resolve, or whose library cannot be read, raises `LookupError` naming the kit.

    A RESOLVED KIT THAT CANNOT STRIP IS THE UNRESOLVED KIT (TOOL-dTrueNorth-20 S16): a library holding no
    single-line `GEN_REGION_AWK='…'`, or more than one, an empty value, and a PATH with no `awk` to run it
    each raise the same `LookupError`, naming the file and the variable, so the live join exits 2 and the
    fixture prints its named SKIP. An empty program prints nothing, so every revision would read as
    status-only and the population would be empty while the join reported green over it."""
    import backlog       # the sibling-kit resolver, loaded only where the strip is asked for
    try:
        lib = pathlib.Path((resolve or backlog.resolve_kit_dir)("unattended", "lib-unattended.sh", str(KIT)),
                           "lib-unattended.sh")
        text = lib.read_text(encoding="utf-8")
    except (LookupError, OSError) as exc:
        raise LookupError(f"the unattended kit's lib-unattended.sh, which holds GEN_REGION_AWK, does not "
                          f"resolve: {exc}") from None
    found = re.findall(r"^GEN_REGION_AWK='([^']*)'$", text, flags=re.M)
    if len(found) != 1:
        raise LookupError(f"{lib.as_posix()} holds {len(found)} single-line GEN_REGION_AWK='…' assignments, not "
                          "one, so the generated-region strip cannot be read")
    if not found[0].strip():
        raise LookupError(f"{lib.as_posix()} holds an empty GEN_REGION_AWK, and an empty strip prints nothing, so "
                          "every revision would read as status-only")
    if not shutil.which("awk"):
        raise LookupError(f"no awk is on PATH to run {lib.as_posix()}'s GEN_REGION_AWK, so the generated-region "
                          "strip cannot run")
    return found[0]


GEN_STRIP = None                 # the strip a fixture entry point set for its call alone; None reads the kit's
IDENTITY_STRIP = (None, None)    # the strip stubbed to the identity, under the fixture's named skip (S2)


@functools.lru_cache(maxsize=None)
def read_gen_strip():
    """`(awk, program)`, the one strip in force for this process: the one `set_gen_strip` set, else the
    unattended kit's `GEN_REGION_AWK` and the awk that runs it. A kit that does not resolve is Unmeasured
    naming it (TOOL-dTrueNorth-12 S2)."""
    if GEN_STRIP is not None:
        return GEN_STRIP
    try:
        prog = read_gen_region_awk()
    except LookupError as exc:
        raise Unmeasured(f"the generated-region strip cannot be read, and a population read without it would "
                         f"count a status-only revision as a member: {exc}") from None
    awk = shutil.which("awk")
    if not awk:
        raise Unmeasured("the generated-region strip needs an awk to run it, and none is on PATH")
    return awk, prog


def set_gen_strip(strip):
    """Set `strip` as the one `read_gen_strip` returns, None restoring the kit's own, and clear the caches
    holding either, so a strip a fixture set for its call never outlives that call (S2)."""
    global GEN_STRIP
    GEN_STRIP = strip
    read_gen_strip.cache_clear()
    extract_authored.cache_clear()


@functools.lru_cache(maxsize=None)
def extract_authored(text):
    """A spec's text less its `**Status:**` line and every generated region (P0.1 row 8a); under the
    identity strip, less its `**Status:**` line alone."""
    awk, prog = read_gen_strip()
    body = re.sub(r"(?m)^\*\*Status:\*\*.*$", "", text)
    if awk is None:
        return body.encode("utf-8")
    done = subprocess.run([awk, prog], input=body.encode("utf-8"), capture_output=True)
    if done.returncode:
        raise Unmeasured(f"the generated-region strip exited {done.returncode}: "
                         f"{done.stderr.decode('utf-8', 'replace').strip()}")
    return done.stdout


def check_material(before, after):
    """True when a revision changes text outside its `**Status:**` line and every generated region."""
    return extract_authored(before) != extract_authored(after)


def read_header_rev(text, hdr):
    """The `rev-N` of a spec's `**Status:**` header, as the units table reads it, or None."""
    for ln in (text or "").split("\n"):
        m = hdr.match(ln)
        if m:
            return int(m.group("rev"))
    return None


def read_baseline_line(text):
    """The sha the record's `[clause-ids]` section records as `Baseline:`, or None."""
    section = text.split("\n## [clause-ids]", 1)[1].split("\n## ", 1)[0] if "\n## [clause-ids]" in text else ""
    m = re.search(r"^Baseline: `([0-9a-f]{7,40})`", section, flags=re.M)
    return m.group(1) if m else None


def scan_clause_members(root, record, pin, now, old):
    """The clause-move arm: the moved `Baseline:` line first, then each clause whose hash differs from the
    pin's, departing at the oldest commit since the pin touching the record where its hash differs. `old`,
    the record at the pin, is always read: an unreadable pin is nothing measured before this is reached
    (TOOL-dTrueNorth-16 S23)."""
    members = []
    line = read_baseline_line(now)
    if not (line and pin.startswith(line)):
        members.append({"kind": "baseline", "build": None, "address": "DESIGN_RECORD's Baseline: line",
                        "hand": "design-revised", "sha": None,
                        "what": f"the Baseline: line moved from {pin[:9]} to {line[:9] if line else 'none'}"})
    o = {cid: (b, h) for b, cid, _t, h in read_chain_clauses(old, f"{record} at {pin[:9]}")}
    n = {cid: (b, h) for b, cid, _t, h in read_chain_clauses(now, record)}
    moved = [cid for cid in sorted(set(o) | set(n)) if cid not in n or cid not in o or o[cid][1] != n[cid][1]]
    departed = {}
    if moved:
        shas = (run_git(root, "log", "--reverse", "--format=%H", f"{pin}..HEAD", "--", record) or b"").decode().split()
        blobs = read_blobs(root, [(s, record) for s in shas])
        for s in shas:
            try:
                at = {cid: h for _b, cid, _t, h in read_chain_clauses(blobs[(s, record)] or "", record)}
            except DesignRefusal:
                at = {}
            for cid in moved:
                if cid not in departed and at.get(cid) != (o[cid][1] if cid in o else None):
                    departed[cid] = s
    for cid in moved:
        b, h = o.get(cid) or n[cid]
        what = (f"{cid} absent at HEAD since the baseline" if cid not in n else f"{cid} new since the baseline"
                if cid not in o else f"{cid} moved from {o[cid][1]} to {n[cid][1]} since the baseline")
        members.append({"kind": "clause", "build": b, "address": f"{cid}@{h}", "hand": "design-revised",
                        "sha": departed.get(cid), "what": what})
    return members


def read_population(root, conf, commits):
    """`(members, facts)` of the tree at `root` (S4): `commits` is the WHOLE list `read_routed_commits`
    already read, so the host reads history once. Raises Unmeasured when nothing can be measured. Its
    first act resolves the strip, before the view is read, so the CLI's armed join and the host's
    `read_host_lines` each refuse an unresolved kit whatever the history holds (TOOL-dTrueNorth-12 S2)."""
    read_gen_strip()
    root = pathlib.Path(root)
    memory_root = (conf.get("MEMORY_ROOT") or "memory").strip().strip("/")
    # The key rule first (TOOL-dTrueNorth-16 S5, S23): a partial set, or a pin naming no commit, is
    # nothing measured on its own, whatever the specs hold.
    try:
        values = read_design_keys(root, conf)
    except DesignRefusal as exc:
        raise Unmeasured(str(exc)) from None
    if values is None:
        raise Unmeasured(f"every DESIGN_* key ({', '.join(DESIGN_KEYS)}) is blank, so there is no design to measure")
    record, pin, view = (values[k] for k in ("DESIGN_RECORD", "DESIGN_BASELINE", "DESIGN_VIEW"))
    try:
        builds = list(dict.fromkeys(r[0] for r in read_design_view(view, root)))
        now = (root / record).read_bytes().decode("utf-8", "replace").replace("\r\n", "\n")
        families = routed_commits.extract_families(conf)
    except (DesignRefusal, routed_commits.Refusal) as exc:
        raise Unmeasured(str(exc)) from None
    except OSError as exc:
        raise Unmeasured(f"DESIGN_RECORD names {record}, which cannot be read: {exc}") from None
    old = read_blobs(root, [(pin, record)])[(pin, record)]
    if old is None:
        raise Unmeasured(f"DESIGN_BASELINE {pin} names no commit holding DESIGN_RECORD {record}, so the clause "
                         "population has no pin and nothing is measured, whatever the specs hold")
    when = read_commit_times(commits)
    parents = {c["sha"]: c["parents"] for c in commits}
    reach = {}
    entries = []
    for raw in (conf.get("ROUTED_PATHS") or "").split():
        entry = raw.replace("\\", "/")
        while entry.startswith("./"):
            entry = entry[2:]
        entries.append(entry)
    # The TRACKED `.md` under each chain build (TOOL-dTrueNorth-26 S7), the population the records
    # tables read, so a draft never staged is no spec and no record of the join.
    try:
        tracked = read_tracked_builds(root, memory_root)
    except DesignRefusal as exc:
        raise Unmeasured(str(exc)) from None
    found = [p for b in builds for p in sorted(t for t in tracked if t.startswith(f"{memory_root}/builds/{b}/")
                                                and t.endswith(".md") and (root / t).is_file())]
    kept, _skipped = scan_chain_specs(found, builds, "", memory_root)
    specs = []
    for b, rel in kept:
        hit = parse_spec_h1(rel, (root / rel).read_bytes().decode("utf-8", "replace"), memory_root, families)
        specs.append((b, rel, hit[1] if hit else None))
    if not specs:
        raise Unmeasured(f"DESIGN_BASELINE {pin[:9]} reads, and no chain build of {view} holds a spec, so nothing "
                         "is measured and the run is never green")
    spec_of = {u: p for _b, p, u in specs if u}
    members = scan_clause_members(root, record, pin, now, old)
    # The records a chain build holds, classified once by the kit's binding reader, `tree_lib.read_bindings`.
    rels = [p for p in found if re.match(re.escape(memory_root) + r"/builds/[^/]+/(?:build|reviews|prompts)/", p)]
    binds = read_bindings(str(root), rels, conf)
    texts = {}

    def derive_slug(rel):
        return rel[len(memory_root) + len("/builds/"):].split("/", 1)[0]

    def read_text(rel):
        if rel not in texts:
            texts[rel] = (root / rel).read_bytes().decode("utf-8", "replace").replace("\r\n", "\n")
        return texts[rel]

    audits = [r for r in rels if "/reviews/" in r and binds.get(r, {}).get("state") == "bound"
              and binds[r]["kind"] == "spec-audit" and binds[r]["pins"]]
    handbacks = [r for r in rels if "/prompts/" in r and DIVERGENCE.search(read_text(r))]
    # THE ONE ADDING-COMMIT READER (TOOL-dTrueNorth-20 S32), the audit-writer test's too: the oldest add
    # of each record, one glob pathspec per folder and the records never on argv.
    try:
        adding = {**read_adding_commits(root, f":(glob){memory_root}/builds/*/reviews/**", audits),
                  **read_adding_commits(root, f":(glob){memory_root}/builds/*/prompts/**", handbacks)}
    except OSError as exc:
        raise Unmeasured(f"the records' adding commits cannot be read: {exc}") from None
    candidates = {}
    for rel in audits:
        if adding.get(rel) in when:
            for unit, n in binds[rel]["pins"].items():
                candidates.setdefault(unit, []).append((n, adding[rel]))
    pins = {u: max(c, key=lambda x: when[x[1]]) for u, c in candidates.items()}
    units = set(spec_of)
    first = read_first_passes(commits, units, entries, when)
    # THE ONE REVISION READER (TOOL-dTrueNorth-16 S12), the carries join's too: each revision with its
    # text at its first parent and at the commit, in two spawns whatever the count.
    try:
        revisions = read_spec_revisions(root, list(spec_of.values()), memory_root)
    except DesignRefusal as exc:
        raise Unmeasured(str(exc)) from None
    graded = []
    for b, path, unit in specs:
        if not unit:
            continue
        for sha, before, after in revisions.get(path, []):
            after_pass = unit in first and sha not in read_ancestors(parents, first[unit], reach)
            after_audit = unit in pins and sha not in read_ancestors(parents, pins[unit][1], reach)
            if after_pass or after_audit:
                graded.append((b, path, unit, sha, before, after, after_pass, after_audit))
    for b, path, unit, sha, before, after, after_pass, after_audit in graded:
        if before is None or not check_material(before, after or ""):
            continue                                    # its creation, or no material change
        rev = read_header_rev(before, HDR_RE)
        address = f"{unit}@rev-{rev if rev is not None else '?'}"
        if after_pass:
            members.append({"kind": "revision", "build": b, "address": address, "hand": "spec-revised", "sha": sha,
                            "what": f"{unit}'s spec changed at {sha[:9]}, not an ancestor of its first pass "
                                    f"{first[unit][:9]}"})
        pin_n, pin_sha = pins.get(unit, (None, None))
        if after_audit and (not after_pass or f"{unit}@rev-{pin_n}" != address):
            members.append({"kind": "audit", "build": b, "address": f"{unit}@rev-{pin_n}", "hand": "spec-revised",
                            "sha": sha, "what": f"{unit}'s spec changed at {sha[:9]}, past its audited revision "
                                                f"rev-{pin_n} ({pin_sha[:9]})"})
    # The ledger arm: an `amended rev-N` line under an `**Evidences:** <unit>` block of a journal record.
    for rel in rels:
        if binds.get(rel, {}).get("kind") != "journal":
            continue
        unit = None
        for n, ln in enumerate(read_text(rel).split("\n"), 1):
            ev = re.match(r"^\*\*Evidences:\*\* `?([^`\s]+)`?", ln)
            if ev or ln.startswith("#"):
                unit = ev.group(1) if ev else None
                continue
            a = LEDGER.match(ln)
            if a and unit:
                k = int(a.group(2))
                members.append({"kind": "ledger", "build": derive_slug(rel), "address": f"{unit}@rev-{k - 1}",
                                "hand": "spec-revised", "sha": read_row_commit(root, ln, rel),
                                "what": f"{unit}'s ledger line {a.group(1)} amended rev-{k}, in {rel}:{n}"})
    # The rescope arm and the hand-back arm, each addressed at its unit's header revision at its commit.
    rows, backs = [], []
    for b in builds:
        folder = root / memory_root / "builds" / b
        scope = folder.relative_to(root).as_posix()     # a row's pickaxe reads its folder, never its file (S1)
        for p in sorted(folder.glob("RUN*.md")) if folder.is_dir() else ():
            if RUN_FILE.match(p.name):
                rel = p.relative_to(root).as_posix()
                for m in RESCOPE.finditer(p.read_bytes().decode("utf-8", "replace").replace("\r\n", "\n")):
                    if m.group(1) != "defer":
                        rows.append((b, rel, m.group(1), m.group(2), m.group(0), read_row_commit(root, m.group(0), scope)))
    for rel in handbacks:
        ids = binds.get(rel, {}).get("ids") or []
        backs.append((derive_slug(rel), rel, ids[0] if ids else None, adding.get(rel)))
    at = read_blobs(root, [(sha, spec_of[item]) for _b, _r, act, item, _row, sha in rows
                           if sha and act != "add" and item in spec_of]
                    + [(sha, spec_of[unit]) for _b, _r, unit, sha in backs if sha and unit in spec_of])

    def read_rev_at(unit, sha):
        rev = read_header_rev(at.get((sha, spec_of[unit])), HDR_RE) if sha and unit in spec_of else None
        return f"{unit}@rev-{rev if rev is not None else '?'}"

    for b, rel, act, item, _row, sha in rows:
        if act == "add":
            members.append({"kind": "add", "build": b, "address": f"new unit {item}", "hand": "design-to-spec",
                            "sha": sha, "what": f"the rescope add of {item}, in {rel}"})
        else:
            members.append({"kind": "rescope", "build": b, "address": read_rev_at(item, sha), "hand": "spec-revised",
                            "sha": sha, "what": f"the rescope {act} of {item}, in {rel}"})
    for b, rel, unit, sha in backs:
        members.append({"kind": "handback", "build": b, "address": read_rev_at(unit, sha), "hand": "spec-to-code",
                        "sha": sha, "what": f"{unit}'s divergence hand-back in {rel}"})
    return members, {"pin": pin, "baseline": old is not None, "specs": len(specs), "memory_root": memory_root,
                     "nopin": [u for _b, _p, u in specs if u and u not in pins]}


# --------------------------------------------------------------------------------------- the join
def derive_joins(members, records):
    """`[(member, its joining record, or None)]`: the record departing from the member's address, or for an
    add the record whose follow-through is `new unit <item>`; the moved Baseline: line joins none."""
    out = []
    for mb in members:
        if mb["kind"] == "baseline":
            rec = None
        elif mb["kind"] == "add":
            rec = next((r for r in records if r["follow"].replace("`", "").strip() == mb["address"]), None)
        else:
            rec = next((r for r in records if r["address"] == mb["address"]), None)
        out.append((mb, rec))
    return out


def read_decision_ref(root):
    """`(ref, why)`: the mainline an owner approval's decision row must already be held on, read from
    `row_grammar.resolve_remote` as `row_grammar.derive_relation_base` reads its base: `<remote>/<branch>`,
    the branch `main` where the ladder names none, the bare branch where there is no remote. A ladder
    refusal is no ref and its text, so every owner citation is refused, as an unread DECISIONS.md is."""
    remote, branch, _observed, refusal = row_grammar.resolve_remote(root)
    if refusal:
        return None, refusal
    branch = branch.strip() or "main"
    return (f"{remote}/{branch}" if remote else branch), ""


def read_decision_rows(root, conf, ref):
    """`{decision id: its row}` of `<MEMORY_ROOT>/DECISIONS.md` at `ref`, read with the kit's row regex, or None."""
    memory_root = (conf.get("MEMORY_ROOT") or "memory").strip().strip("/")
    raw = run_git(root, "show", f"{ref}:{memory_root}/DECISIONS.md")
    if raw is None:
        return None
    try:
        rowre = row_grammar.derive_row_re(conf)
    except row_grammar.Problem:
        return None
    return {m.group(1): ln for ln in raw.decode("utf-8", "replace").split("\n") for m in [rowre.match(ln)] if m}


def check_approver(rec, rows, approval, at=""):
    """Why `approval` refuses the record's approver, or None (S6, P0.1 row 6); `at` says where the rows
    were read, ` at <ref>`, or that the remote ladder resolved no ref."""
    a = (rec["approver"] or "").strip()
    role = next((r for r in ROLES if a.lower().startswith(r)), None)
    if role is None:
        return f"its approver '{a}' names no role the record grammar names" if a else "it records no approver"
    if approval == "by-risk":
        owner_cause = rec["cause"] == "owner ruling"
        need = "owner" if owner_cause else LEAST.get(rec["risk"])
        if need and RANK[role] < RANK[need]:
            what = f"cause {rec['cause']}" if owner_cause else f"risk {rec['risk']}"
            return f"its approver {role} is below {need}, the least approver its {what} requires under by-risk"
    if role != "owner":
        return None
    cited = list(dict.fromkeys(m.group(0) for m in row_grammar.GENERIC_ID.finditer(a)))
    if not cited:
        return f"its approver '{a}' names the owner and cites no decision id"
    clause = re.match(r"`?(" + _CL + r")@", rec["departs"])
    unit = re.match(r"new unit `?([^`\s]+)", rec["follow"].strip())
    names = [x.group(1) for x in (clause, unit) if x]
    held = [c for c in cited if c in (rows or {})]
    for c in held:
        if any(re.search(r"(?<![A-Za-z0-9-])" + re.escape(x) + r"(?![A-Za-z0-9-])", rows[c]) for x in names):
            return None
    if not held:
        return f"its approver cites {', '.join(cited)}, which no row of DECISIONS.md holds{at}"
    return (f"its approver cites {', '.join(held)}, whose row does not name "
            + (" or ".join(names) if names else "a departed clause or a new unit, and the record names neither"))


def check_approvers(records, rows, approval, at=""):
    """`[(record id, why)]` for each record whose approver `approval` refuses."""
    return [(r["id"], why) for r in records for why in [check_approver(r, rows, approval, at)] if why]


def check_commit_join(root, members, records, range_shas):
    """`[(member, record or None, verdict)]` for each member departing in `range_shas`: `joined` where its
    joining record is in that commit's tree, `late` where it is not, `nobody` where no record joins it.
    Every tree is asked in ONE `git cat-file --batch-check`, as the host batches its own lookups."""
    todo = [(m, r) for m, r in derive_joins(members, records) if m.get("sha") and m["sha"] in range_shas]
    asked = [(m, r) for m, r in todo if r is not None]
    answers = []
    if asked:
        raw = run_git(root, "cat-file", "--batch-check",
                      stdin="".join(f"{m['sha']}:{r['path']}\n" for m, r in asked).encode("utf-8"))
        if raw is None:
            raise Unmeasured("`git cat-file --batch-check` failed, so no departing commit's tree could be read")
        answers = raw.decode("utf-8", "replace").split("\n")
    present = {id(m): not answers[i].endswith(" missing") for i, (m, _r) in enumerate(asked)}
    return [(m, r, "nobody" if r is None else "joined" if present[id(m)] else "late") for m, r in todo]


def measure_join(root, conf, commits):
    """Everything the join renders, read once: the members, their facts, the records, the joins and the
    decision rows on the mainline `read_decision_ref` resolves, with that ref or the ladder's refusal."""
    members, facts = read_population(root, conf, commits)
    try:
        records = read_records(root, conf)
    except DesignRefusal as exc:
        raise Unmeasured(str(exc)) from None
    ref, why = read_decision_ref(root)
    return {"members": members, "facts": facts, "records": records, "joins": derive_joins(members, records),
            "rows": read_decision_rows(root, conf, ref) if ref else None, "ref": ref, "ref_why": why}


def render_member(m, tail):
    return f"{SAY}:   {m['what']}, at {m['address']} ({m['hand']}): {tail}"


def render_lines(result, policy, approval, label="", commit=None, close=True):
    """`(lines, findings)`: the summary line and one line per member, refused record and malformed file,
    every line prefixed `deviation:`. `close=False` renders the commit join alone, the RANGE half's."""
    late = [x for x in commit or [] if x[2] == "late"]
    if not close:
        nobody = [x for x in commit or [] if x[2] == "nobody"]
        lines = [f"{SAY}: {label}commit join · {len(commit or [])} member(s) departing in the range · "
                 f"{len(commit or []) - len(late) - len(nobody)} recorded at their departure · {len(late)} recorded "
                 f"late · {len(nobody)} recorded by nobody · policy {policy}"]
        for m, r, verdict in commit or []:
            lines.append(render_member(m, f"recorded at its departure {m['sha'][:8]} by {r['id']}" if verdict == "joined"
                                       else f"recorded after its departure at {m['sha'][:8]}, by {r['id']}"
                                       if verdict == "late" else "recorded by nobody"))
        return lines, len(late) + len(nobody)
    facts, joins, records = result["facts"], result["joins"], result["records"]
    at = f" at {result['ref']}" if result["ref"] else ", the remote ladder resolving no ref"
    refused = check_approvers(records, result["rows"], approval, at)
    malformed = [(r, field, why) for r in records for field, why in r["malformed"]]
    unjoined = sum(1 for _m, r in joins if r is None)
    lines = [f"{SAY}: {label}baseline {facts['pin'][:9]} {'read' if facts['baseline'] else 'unread'}, chain-build "
             f"specs {facts['specs']}, members {len(joins)} ({unjoined} unjoined), records {len(records)} "
             f"({len({r['id'] for r, _f, _w in malformed})} malformed) · refused {len(refused)}"
             + (f" · commit join {len(commit)} departing, {len(late)} recorded late" if commit is not None else "")
             + f" · policy {policy} · approval {approval}"]
    lines += [render_member(m, f"joins {r['id']}" if r else "recorded by nobody") for m, r in joins]
    lines += [f"{SAY}:   refused: {rid}: {why}" for rid, why in refused]
    lines += [f"{SAY}:   malformed: {r['path']}: {field} {why}" for r, field, why in malformed]
    lines += [render_member(m, f"recorded after its departure at {m['sha'][:8]}, by {r['id']}") for m, r, _v in late]
    if result["rows"] is None:
        lines.append(f"{SAY}:   {facts['memory_root']}/DECISIONS.md is unread{at}, so every owner citation "
                     "is refused" + (f": {result['ref_why']}" if result["ref_why"] else ""))
    if facts["nopin"]:
        lines.append(f"{SAY}:   no audit pin: {', '.join(facts['nopin'])}")
    return lines, unjoined + len(refused) + len(malformed) + len(late)


def read_host_lines(repo, conf, populations):
    """The host's lines (S7): `populations` is `[(mode, label, commits)]` as `check_routed_commits` read
    them, its WHOLE list among them. The RANGE half runs the commit join over the range's shas; the
    WHOLE half runs the close join and the commit join over every sha. A baseline that cannot be read
    is Unmeasured, which the host raises as its Refusal."""
    whole = next(c for mode, _label, c in populations if mode == "WHOLE")
    result = measure_join(repo, conf, whole)
    lines = []
    for mode, label, commits in populations:
        shas = {c["sha"] for c in commits}
        commit = check_commit_join(repo, result["members"], result["records"], shas)
        if mode == "RANGE":
            lines += render_lines(result, HOST_POLICY, HOST_APPROVAL, f"{label} · ", commit, close=False)[0]
        else:
            lines += render_lines(result, HOST_POLICY, HOST_APPROVAL, "WHOLE · ", commit)[0]
    return lines


# ------------------------------------------------------------------------------------ the fixture
FIXTURE_FAMILY = "FIX"     # declared only in the fixture repository's own conf
FIXTURE_BUILDS = ("dFixA", "dFixB")     # the fixture design's chain builds; the first holds every folder
TN = f"memory/builds/{FIXTURE_BUILDS[0]}/"
FIXTURE_ROUTED = "src/"     # the fixture's one routed directory, as routed_commits.py routes its own fixture
EPOCH = 1792576800         # 2026-10-21T10:00Z, after the fixture's ROUTED_COMMIT_CUTOFF
UNMEASURED_PIN = "0123456789abcdef0123456789abcdef01234567"
# TOOL-dTrueNorth-16 S23: each "nothing measured" cause on its own, superseding TOOL-dTrueNorth-4 S8's
# conjunction — a pin naming no commit over the base's specs, and a readable pin with no chain spec.
UNMEASURED_PLANTS = ("unmeasured-pin", "unmeasured-specs")
PLANTS = ("baseline", "clause", "subject-pass", "pass-none", "status-flip", "two-branch", "header-rev", "gen",
          "status-gen", "gen-text", "quote", "amended", "amended-joined", "approver-none", "owner-bare", "owner-er",
          "owner-row5", "owner-row1-added", "owner-unknown-id", "approver", "add", "handback", "audit-pin", "defer",
          "fix-record", "audit-nopin",                       # the instrument's 26, deviations.py:851-854
          "pass-revision", "below-risk", "owner-cause", "status-only", "malformed-field", "malformed-risk",
          "malformed-follow", "malformed-supersedes", "duplicate-n", "record-late",
          "subject-trailer", "pipe-after",                   # with UNMEASURED_PLANTS, TOOL-dTrueNorth-16's four
          "rotated",                                         # TOOL-dTrueNorth-24's
          "spec-notes") + UNMEASURED_PLANTS                  # TOOL-dTrueNorth-26's
# The subject-trailer plant's second unit, Y, whose `Pass:` trailer rides a commit whose subject names X.
SUBJECT_TRAILER_Y = "FIX-dTrueNorth-97"
# The successor the rotated plant's supersede row names; no spec carries it, as none carries the base's.
ROTATED_SUCCESSOR = "FIX-dTrueNorth-96"
# The role map (TOOL-dTrueNorth-12 §4): every clause-moving role moves its own clause of the fixture design,
# so plants compose. The base's owner amendment, which `quote` reads, and the `baseline` and `clause` plants:
CLAUSE_ROLES = {"base": "cl-dFix-0001", "baseline": "cl-dFix-0002", "clause": "cl-dFix-0003"}
# Each approver plant: the clause it moves, and the approver of the record departing from it (P0.1 row 6).
APPROVER_PLANTS = {"owner-bare": ("cl-dFix-0004", "owner"),
                   "owner-er": ("cl-dFix-0005", "owner, quoted at ER:189"),
                   "owner-row5": ("cl-dFix-0006", "owner, FIX-dClosedLoop-6"),
                   "owner-unknown-id": ("cl-dFix-0007", "owner, FIX-dClosedLoop-99"),
                   "approver-none": ("cl-dFix-0008", None),
                   "approver": ("cl-dFix-0009", "author")}
# The by-risk plants: the clause each moves, and its record's risk, cause and approver.
RISK_PLANTS = {"below-risk": ("cl-dFix-0010", "loosening", "builder discovery", "author"),
               "owner-cause": ("cl-dFix-0011", "additive", "owner ruling", "spec writer")}
# The plants whose verdict reads the generated-region strip (TOOL-dTrueNorth-4 AC5), held back by the
# fixture's named skip where the unattended kit does not resolve (TOOL-dTrueNorth-12 S2). Every plant run
# under the identity strip moved gen's and status-gen's verdicts and no other's, so none is added.
STRIP_PLANTS = ("status-only", "header-rev", "gen", "status-gen", "gen-text")
# The unit each plant writes; the base writes FIX-dTrueNorth-1, -2 and -99.
PLANT_UNITS = {p: f"FIX-dTrueNorth-{n}" for n, p in enumerate(
    ("subject-pass", "pass-none", "status-flip", "two-branch", "header-rev", "gen", "status-gen", "gen-text",
     "quote", "amended", "amended-joined", "owner-row1-added", "add", "handback", "audit-pin", "defer",
     "fix-record", "audit-nopin", "record-late", "pass-revision", "status-only", "malformed-field",
     "malformed-risk", "malformed-follow", "duplicate-n", "malformed-supersedes", "subject-trailer",
     "pipe-after", "rotated", "spec-notes"), 10)}
DECISIONS_TEXT = "\n".join([
    "# Decisions", "",
    "- FIX-dClosedLoop-2 · the spec-run close by carry-forward, and dTrueNorth's extra unit FIX-dTrueNorth-99 approved "
    "as a departure (ER:84, ER:232, ER:320)",
    "- FIX-dClosedLoop-3 · the grant every chain build's may: line cites (ER:181)",
    "- FIX-dClosedLoop-4 · the chain's deviation values, report and author-recorded, and the departure from "
    f"{CLAUSE_ROLES['base']} (ER:103-104, ER:189)",
    "- FIX-dClosedLoop-6 · the standing ruling for residual forks (ER:240, ER:388, ER:328)",
    "- FIX-dClosedLoop-7 · the driver-rewriting builds land through their own code, and dPlacedRequest's migration of "
    "cl-dClosedLoop-0120 (ER:248, ER:264)", ""])


class Fixture:
    """A temporary git repository written through `git fast-import`: the fixture's own design and its view,
    the fixture family, and the plants' histories. Every commit is streamed; a sha is resolved only when a
    plant needs one, by importing what is pending."""

    def __init__(self, root, record, view):
        self.root, self.record, self.view = pathlib.Path(root), record, view
        self.tick = self.mark = self.n = 0
        self.rows, self.stream, self.shas, self.marked = [], bytearray(), {}, {}
        self.branches, self.forks, self.branch = {}, {}, "main"
        self.marks = self.root / ".git" / "fixture-marks"
        self.v2 = self.base = None
        self.hashes = {}
        # What `design_lib.write_design_fixture` reads: one clause per id the role maps hold, so each
        # clause-moving role moves its own clause and a role added to a map gets its clause with no
        # second edit, and the fixture's two chain builds.
        self.clause_ids = sorted({*CLAUSE_ROLES.values(), *(v[0] for v in APPROVER_PLANTS.values()),
                                  *(v[0] for v in RISK_PLANTS.values())})
        self.builds = FIXTURE_BUILDS

    def write_commit(self, files, subject, trailers=(), merge=None):
        """One commit on the current branch, `files` mapping a path to its text, or None to delete it; a
        merge also takes every path the merged branch changed since it forked. Returns its mark."""
        cur = self.branches.setdefault(self.branch, {"tip": None, "files": {}})
        changes = {}
        if merge:
            other, fork = self.branches[merge], self.forks[merge]
            changes.update({p: other["files"].get(p) for p in set(other["files"]) | set(fork)
                            if fork.get(p) != other["files"].get(p)})
        changes.update({p: None if v is None else v if isinstance(v, bytes) else v.encode("utf-8")
                        for p, v in files.items()})
        self.tick += 1
        self.mark += 1
        when = EPOCH + self.tick
        msg = (subject + ("\n\n" + "\n".join(trailers) if trailers else "") + "\n").encode("utf-8")
        out, new = self.stream, dict(cur["files"])
        out += b"commit refs/heads/%s\nmark :%d\n" % (self.branch.encode(), self.mark)
        out += b"author fixture <fixture@example.invalid> %d +0000\n" % when
        out += b"committer fixture <fixture@example.invalid> %d +0000\n" % when
        out += b"data %d\n%s\n" % (len(msg), msg)
        if cur["tip"] is not None:
            out += b"from :%d\n" % cur["tip"]
        if merge:
            out += b"merge :%d\n" % self.branches[merge]["tip"]
        for rel in sorted(changes):
            body = changes[rel]
            if body is None and rel in new:
                out += b"D %s\n" % rel.encode("utf-8")
                del new[rel]
            elif body is not None and new.get(rel) != body:
                out += b"M 100644 inline %s\ndata %d\n%s\n" % (rel.encode("utf-8"), len(body), body)
                new[rel] = body
        out += b"\n"
        cur["tip"], cur["files"] = self.mark, new
        return self.mark

    def set_branch(self, name, new=False):
        if new:
            cur = self.branches[self.branch]
            self.branches[name] = {"tip": cur["tip"], "files": dict(cur["files"])}
            self.forks[name] = dict(cur["files"])
            self.stream += b"reset refs/heads/%s\nfrom :%d\n\n" % (name.encode("utf-8"), cur["tip"])
        self.branch = name

    def write_stream(self):
        """Import what is pending, keeping the marks across imports, and read every mark's sha."""
        if self.stream:
            got = run_git(self.root, "fast-import", "--quiet", f"--import-marks-if-exists={self.marks.as_posix()}",
                          f"--export-marks={self.marks.as_posix()}", stdin=bytes(self.stream))
            if got is None:
                raise RuntimeError(f"fixture: git fast-import failed in {self.root}")
            self.stream = bytearray()
            self.shas = dict(ln.split(" ", 1) for ln in self.marks.read_text(encoding="utf-8").split("\n") if ln)
        return self.shas

    def read_sha(self, mark):
        return (self.shas.get(f":{mark}") or self.write_stream()[f":{mark}"]).strip()

    def write_tree(self):
        """Import everything, point HEAD at the run's branch, read that branch's tree into the index, and
        write it to the work tree, so the fixture's records and specs are TRACKED, the population the
        join reads (TOOL-dTrueNorth-26 S7)."""
        self.write_stream()
        (self.root / ".git" / "HEAD").write_bytes(f"ref: refs/heads/{self.branch}\n".encode("utf-8"))
        if run_git(self.root, "read-tree", f"refs/heads/{self.branch}") is None:
            raise RuntimeError(f"fixture: git read-tree {self.branch} failed in {self.root}")
        for rel, body in self.branches[self.branch]["files"].items():
            p = self.root / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(body)

    def render_spec(self, unit, rev, status="OPEN", line="the fixture line holds", records="", extra=""):
        return "\n".join([f"# {unit} — fixture unit", "",
                          f"**Status:** {status} · rev-{rev} · 2026-10-21 · node d · Tier-2 · base 0123abcd · streams "
                          "playbook", "", "## 6. Acceptance criteria", "", f"- AC1: {line}"]
                         + ([extra] if extra else []) + ["", "<!-- gen:spec-records -->", "| Record | Kind |",
                                                         "|---|---|"] + ([records] if records else [])
                         + ["<!-- /gen:spec-records -->", ""])

    def derive_spec_path(self, unit):
        return f"{TN}spec/2026-10-21-spec-{unit}.md"

    def write_spec(self, unit, rev, files=None, **kw):
        return self.write_commit({self.derive_spec_path(unit): self.render_spec(unit, rev, **kw), **(files or {})},
                                 f"spec(dTrueNorth): {unit} rev-{rev}", ["Pass: none"])

    def write_pass(self, unit, trailer=True):
        """The unit's `--dispatch --writes` row, then its product commit under ROUTED_PATHS."""
        out = f"{FIXTURE_ROUTED}fix-{unit.rsplit('-', 1)[1]}.txt"
        self.add_run_row(f"dispatch · item 0a1b2c3d {unit} · reason {out} {self.derive_spec_path(unit)}")
        return self.write_commit({out: "built\n"}, f"build {unit} from its spec", [f"Pass: {unit}"] if trailer else ())

    def render_record(self, unit, departs, approver, risk="additive", cause="builder discovery", hand="spec-revised",
                      follow="gap gap-build-07", caused="", n=None, after="the text that replaced it", **extra):
        """A record in the S1 grammar, `(path, text)`; `caused=None` omits **Caused-by:**."""
        if n is None:
            self.n += 1
            n = self.n
        fields = [("Departs from", departs), ("Hand-off", hand), ("Before", "the text departed from"),
                  ("After", after), ("Cause", cause), ("Reason", "the fixture's departure"),
                  ("Evidence", "the fixture"), ("Risk", risk), ("Approver", approver), ("Follow-through", follow),
                  ("Caused-by", unit if caused == "" else caused)]
        fields += [(k.capitalize(), v) for k, v in extra.items()]
        text = "\n".join([f"# {unit} deviation {n}", "", f"**Serves:** deviation {unit}", ""]
                         + [f"- **{k}:** {v}" for k, v in fields if v is not None]) + "\n"
        return f"{TN}build/2026-10-21-build-{unit}-deviation-{n}.md", text

    def add_run_row(self, row, files=None):
        self.rows.append(f"2026-10-21T10:{len(self.rows) // 60:02d}:{len(self.rows) % 60:02d}Z {row}")
        return self.write_commit({TN + "RUN.md": self.render_run(), **(files or {})},
                                 f"unattended(dTrueNorth): {row.split(' · ')[0]}")

    def render_run(self):
        return "\n".join(["# dTrueNorth - run state", "", "## Run facts", "phase: BUILDING", "", "## Parked", ""]
                         + [r + "\n" for r in self.rows])

    def set_moved_clause(self, cid, words="and a planted amendment "):
        i = self.v2.index(f"`{cid}`")
        self.v2 = self.v2[:i] + words + self.v2[i:]

    def render_prompt(self, unit, divergence):
        goal = ("DIVERGENCE: the spec's §6 cannot be built as written" if divergence
                else "Fix the wording of the spec's fixture line.")
        return "\n".join([f"# Revision — dTrueNorth: {unit}", "", f"**Serves:** research {unit}", "", "## The brief",
                          "", "### Goal", goal, "", "### Items", "1. revise it", ""])

    def render_audit(self, unit, pin):
        return "\n".join([f"# M4 spec audit — {unit}", "", f"**Serves:** spec-audit {unit}"
                          + (f"@rev-{pin}" if pin else ""), "", "**Verdict:** CLEAN", ""])

    def render_ledger(self, unit, rev):
        return "\n".join([f"# {unit} acceptance ledger", "", f"**Serves:** journal {unit}", "",
                          f"**Evidences:** {unit}", f"- AC1 — amended rev-{rev} — the fixture line narrowed, logged in §9",
                          "- AC2 — `fixture` — observed", ""])


def build_fixture_conf(record, view, pin):
    """The fixture's conf: its family and routed paths, and all four DESIGN_* keys, the key rule's armed
    state (TOOL-dTrueNorth-16 S5); the join reads no owned node, so DESIGN_NODES names a path no file holds."""
    return "".join(f'{k}="{v}"\n' for k, v in (
        ("MEMORY_ROOT", "memory"), ("FAMILIES", f"fixture:{FIXTURE_FAMILY}"), ("ROUTED_PATHS", FIXTURE_ROUTED),
        ("ROUTED_COMMIT_CUTOFF", "2026-01-01"), ("DESIGN_RECORD", record), ("DESIGN_BASELINE", pin),
        ("DESIGN_VIEW", view), ("DESIGN_NODES", "memory/design/nodes.py")))


def add_base(fx):
    """The base history, every member joined by a record written in its departing commit, every record's
    approver meeting its risk under both approval values: a revision, a hand-back and a ledger line on one
    record; a supersede; a clause moved by the owner's row; and an extra unit added by the owner's row."""
    u1, u2 = "FIX-dTrueNorth-1", "FIX-dTrueNorth-2"
    fx.write_commit({TN + "RUN.md": fx.render_run()}, "unattended(dTrueNorth): preflight", ["Pass: none"])
    fx.write_spec(u1, 1)
    path, text = fx.render_record(u1, f"{u1}@rev-1 [acceptance]", "spec writer, re-audited at rev-2")
    fx.write_commit({f"{TN}prompts/2026-10-21-prompt-{u1}-1-revision.md": fx.render_prompt(u1, True), path: text},
                    f"records(dTrueNorth): {u1}'s divergence hand-back and its deviation", ["Pass: none"])
    fx.write_pass(u1)
    fx.write_spec(u1, 2, line="the fixture line holds, narrowed")
    fx.write_commit({f"{TN}build/2026-10-21-build-{u1}-1-acceptance-ledger.md": fx.render_ledger(u1, 2)},
                    f"records(dTrueNorth): {u1}'s ledger", ["Pass: none"])
    fx.write_spec(u2, 1)
    fx.add_run_row(f"rescope · item supersede {u2} -> FIX-dTrueNorth-3 · reason building found it two units",
                   dict([fx.render_record(u2, f"{u2}@rev-1 [scope]", "spec writer", follow="new unit FIX-dTrueNorth-3")]))
    cid = CLAUSE_ROLES["base"]
    h = fx.hashes[cid]
    fx.set_moved_clause(cid)
    path, text = fx.render_record(u1, f"`{cid}@{h}` [chain]", "owner, FIX-dClosedLoop-4", risk="stricter",
                                  cause="owner ruling", hand="design-revised", follow=f"amends {cid}@{h}")
    fx.write_commit({fx.record: fx.v2, path: text}, f"records(dTrueNorth): {cid} amended by the owner's row")
    fx.add_run_row("rescope · item add FIX-dTrueNorth-99 · reason dTrueNorth's extra unit, the owner's row 1",
                   dict([fx.render_record("FIX-dTrueNorth-99", f"{FIXTURE_BUILDS[0]} [chain]", "owner, FIX-dClosedLoop-2",
                                          hand="design-to-spec", follow="new unit FIX-dTrueNorth-99")]))


def add_plant(fx, plant):
    """One plant's history, on its own unit, clause or row, so every plant composes with every other."""
    u, u1 = PLANT_UNITS.get(plant), "FIX-dTrueNorth-1"
    if plant == "baseline":
        fx.set_moved_clause(CLAUSE_ROLES[plant], "loosened, so the owner is never asked, ")
        loose = fx.read_sha(fx.write_commit({fx.record: fx.v2}, f"records(dClosedLoop): {CLAUSE_ROLES[plant]} loosened"))
        fx.v2 = re.sub(r"(?m)^Baseline: `[0-9a-f]+`", f"Baseline: `{loose}`", fx.v2)
        fx.write_commit({fx.record: fx.v2}, "records(dClosedLoop): the baseline re-pointed past the loosening")
    elif plant == "clause":
        fx.set_moved_clause(CLAUSE_ROLES[plant])
        fx.write_commit({fx.record: fx.v2}, f"records(dClosedLoop): {CLAUSE_ROLES[plant]} edited, and no record")
    elif plant in APPROVER_PLANTS or plant in RISK_PLANTS:
        if plant in APPROVER_PLANTS:
            (cid, approver), risk, cause = APPROVER_PLANTS[plant], "stricter", "review finding"
        else:
            cid, risk, cause, approver = RISK_PLANTS[plant]
        h = fx.hashes[cid]
        fx.set_moved_clause(cid)
        path, text = fx.render_record(u1, f"`{cid}@{h}` [chain]", approver, risk=risk, cause=cause,
                                      hand="design-revised", follow=f"amends {cid}@{h}")
        fx.write_commit({fx.record: fx.v2, path: text}, f"records(dTrueNorth): {cid} amended, approver {approver}")
    elif plant == "owner-row1-added":
        fx.add_run_row(f"rescope · item add {u} · reason the spec audit promoted it",
                       dict([fx.render_record(u, f"{FIXTURE_BUILDS[0]} [chain]", "owner, FIX-dClosedLoop-2",
                                              hand="design-to-spec", follow=f"new unit {u}")]))
    elif plant in ("subject-pass", "pass-revision"):
        fx.write_spec(u, 1)
        fx.write_pass(u, trailer=plant == "pass-revision")
        fx.write_spec(u, 2, line="the fixture line, revised after the pass")
    elif plant == "pass-none":
        fx.write_spec(u, 1)
        fx.write_commit({f"{FIXTURE_ROUTED}fix-11.txt": "built\n"}, f"build {u}, attributed to no pass", ["Pass: none"])
        fx.write_spec(u, 2, line="the fixture line, revised")
    elif plant == "status-flip":
        fx.write_spec(u, 1)
        fx.write_commit({fx.derive_spec_path(u): fx.render_spec(u, 1, status="INPROGRESS")}, f"{u} goes INPROGRESS")
        fx.write_spec(u, 2, status="INPROGRESS", line="the fixture line, revised")
    elif plant == "status-only":
        fx.write_spec(u, 1)
        fx.write_pass(u)
        fx.write_commit({fx.derive_spec_path(u): fx.render_spec(u, 1, status="INPROGRESS")},
                        f"spec(dTrueNorth): {u} goes INPROGRESS after its pass", ["Pass: none"])
    elif plant == "two-branch":
        fx.write_spec(u, 1)
        fx.set_branch("node-b", new=True)
        fx.write_pass(u)
        fx.set_branch("run")
        fx.write_spec(u, 2, line="the fixture line, revised on node a while node b's pass was in flight")
        fx.write_commit({}, f"merge: node b's pass of {u}", merge="node-b")
    elif plant == "header-rev":
        fx.write_spec(u, 1)
        fx.write_pass(u)
        fx.write_commit({fx.derive_spec_path(u): fx.render_spec(u, 1, status="INPROGRESS")},
                        f"spec(dTrueNorth): {u} INPROGRESS", ["Pass: none"])
        fx.write_spec(u, 2, files=dict([fx.render_record(u, f"{u}@rev-1 [acceptance]", "spec writer")]),
                      status="INPROGRESS", line="the fixture line, revised")
    elif plant in ("gen", "status-gen", "gen-text"):
        fx.write_spec(u, 1)
        fx.write_pass(u)
        fx.write_commit({fx.derive_spec_path(u): fx.render_spec(
            u, 2 if plant == "gen-text" else 1, status="INPROGRESS" if plant == "status-gen" else "OPEN",
            records="| 2026-10-21-review-fixture | spec-audit |",
            line="the fixture line, changed with the render" if plant == "gen-text" else "the fixture line holds")},
            f"records(dTrueNorth): {u}'s spec-records region rendered again", ["Pass: none"])
    elif plant == "quote":
        quoted = next(t for _b, c, t, _h in read_chain_clauses(fx.v2) if c == CLAUSE_ROLES["base"])
        fx.write_spec(u, 1, extra=f"- AC2: quotes its clause, {quoted}")
    elif plant in ("amended", "amended-joined"):
        files = {f"{TN}build/2026-10-21-build-{u}-1-acceptance-ledger.md": fx.render_ledger(u, 3)}
        if plant == "amended-joined":
            files.update([fx.render_record(u, f"{u}@rev-2 [acceptance]", "spec writer")])
        fx.write_commit(files, f"records(dTrueNorth): {u}'s ledger")
    elif plant == "add":
        fx.add_run_row(f"rescope · item add {u} · reason a discovery adopted")
    elif plant in ("handback", "fix-record"):
        fx.write_spec(u, 1)
        fx.write_commit({f"{TN}prompts/2026-10-21-prompt-{u}-1-revision.md": fx.render_prompt(u, plant == "handback")},
                        f"records(dTrueNorth): {u}'s revision record", ["Pass: none"])
    elif plant in ("audit-pin", "audit-nopin"):
        fx.write_spec(u, 1)
        fx.write_commit({f"{TN}reviews/2026-10-21-review-{u}.md": fx.render_audit(u, 1 if plant == "audit-pin" else None)},
                        f"review(dTrueNorth): {u}'s spec audit", ["Pass: none"])
        fx.write_spec(u, 2, line="the fixture line, revised after its audit")
    elif plant == "defer":
        fx.write_spec(u, 1)
        fx.add_run_row(f"rescope · item defer {u} · reason specced; built by this build's build run")
    elif plant in ("malformed-field", "malformed-risk", "malformed-follow", "malformed-supersedes"):
        kw = {"malformed-field": {"caused": None}, "malformed-risk": {"risk": "moderate"},
              "malformed-follow": {"follow": "amends cl-dClosedLoop-0012"},
              "malformed-supersedes": {"supersedes": "deviation-9"}}[plant]   # a short form, no record's stem
        fx.write_commit(dict([fx.render_record(u, f"{u}@rev-1 [scope]", "spec writer", **kw)]),
                        f"records(dTrueNorth): {u}'s deviation, {plant}")
    elif plant == "duplicate-n":
        fx.n += 1
        fx.write_commit(dict([fx.render_record(u, f"{u}@rev-1 [scope]", "spec writer", n=fx.n),
                              fx.render_record("FIX-dTrueNorth-98", "FIX-dTrueNorth-98@rev-1 [scope]", "spec writer",
                                               n=fx.n)]),
                        "records(dTrueNorth): two deviations at one number")
    elif plant == "record-late":
        fx.write_spec(u, 1)
        fx.write_pass(u)
        fx.marked[plant] = fx.write_spec(u, 2, line="the fixture line, revised after its pass")
        fx.write_commit(dict([fx.render_record(u, f"{u}@rev-1 [acceptance]", "spec writer")]),
                        f"records(dTrueNorth): {u}'s deviation, written after its departure", ["Pass: none"])
    elif plant == "subject-trailer":
        # TOOL-dTrueNorth-16 S13: one product commit whose subject names X and whose trailer names Y. By
        # the driver's pass rule it is Y's pass and no pass of X, so X's later revision is no member and
        # Y's is, joined by its record; the union rule would credit X and leave its revision unjoined.
        y = SUBJECT_TRAILER_Y
        fx.write_spec(u, 1)
        fx.write_spec(y, 1)
        fx.add_run_row(f"dispatch · item 0a1b2c3d {y} · reason {FIXTURE_ROUTED}fix-97.txt {fx.derive_spec_path(y)}")
        fx.write_commit({f"{FIXTURE_ROUTED}fix-97.txt": "built\n"}, f"build {u} from its spec", [f"Pass: {y}"])
        fx.write_spec(u, 2, line="the fixture line, revised after a commit naming it in its subject alone")
        fx.write_spec(y, 2, files=dict([fx.render_record(y, f"{y}@rev-1 [acceptance]", "spec writer")]),
                      line="the fixture line, revised after its pass")
    elif plant == "pipe-after":
        # TOOL-dTrueNorth-16 S22: an `**After:**` holding a pipe, which the view would split into two cells.
        fx.write_commit(dict([fx.render_record(u, f"{u}@rev-1 [scope]", "spec writer",
                                               after="the text | that replaced it")]),
                        f"records(dTrueNorth): {u}'s deviation, a pipe in its After")
    elif plant == "rotated":
        # TOOL-dTrueNorth-24 S2: a supersede row written beside its record, the spec revised past it, then
        # the driver's rotation: RUN.md's bytes move to `RUN.LANDED.<blob8>.md`, named by their blob as
        # `archive_name_of` names it, beside a fresh RUN.md holding none of the old rows. A pickaxe over the
        # archive alone dates every row it holds by the rotation; one over the folder, by the row's writer.
        fx.write_spec(u, 1)
        row = fx.add_run_row(f"rescope · item supersede {u} -> {ROTATED_SUCCESSOR} · reason the spec run found it "
                             "two units", dict([fx.render_record(u, f"{u}@rev-1 [scope]", "spec writer",
                                                                 follow=f"new unit {ROTATED_SUCCESSOR}")]))
        fx.write_spec(u, 2, line="the fixture line, revised after its supersede row")
        body = fx.branches[fx.branch]["files"][TN + "RUN.md"]
        blob = hashlib.sha1(b"blob %d\0" % len(body) + body).hexdigest()[:8]
        fx.rows = []
        fx.marked[plant] = (row, fx.write_commit({f"{TN}RUN.LANDED.{blob}.md": body, TN + "RUN.md": fx.render_run()},
                                                 "unattended(dTrueNorth): landed, the run state rotated"))
    elif plant == "spec-notes":
        # TOOL-dTrueNorth-26 S5: a notes file in a chain build's spec folder whose H1 defines a unit and
        # whose name holds no `-spec-`. The selector counts it `unnamed`, so the revision reader, which
        # refuses any path outside its pathspec, is never handed it and the join stays measured.
        fx.write_commit({f"{TN}spec/notes.md": f"# {u} — notes beside the specs, named as no spec is\n\nA note.\n"},
                        "records(dTrueNorth): notes in the spec folder", ["Pass: none"])


def build_fixture(root, plants):
    """The fixture repository at `root`: the fixture family and the decisions, the pin holding the fixture's
    own design (`design_lib.write_design_fixture`), a commit declaring the design keys at it, and the run's
    branch with the base and each plant. Each `unmeasured-*` plant stands alone (TOOL-dTrueNorth-16 S23):
    `unmeasured-pin` declares a pin naming no commit over the base's specs, and `unmeasured-specs` the
    readable pin with no base, so no chain-build spec."""
    fx = Fixture(root, "memory/design/record.md", "memory/design/view.md")
    if run_git(".", "init", "-q", str(root)) is None:
        raise RuntimeError(f"fixture: git init failed at {root}")
    fx.write_commit({".memory-tree.conf": f'MEMORY_ROOT="memory"\nFAMILIES="fixture:{FIXTURE_FAMILY}"\n',
                     "memory/DECISIONS.md": DECISIONS_TEXT}, "fixture: the fixture family and the decisions")
    pin = write_design_fixture(fx)
    fx.hashes = {cid: h for _b, cid, _t, h in read_chain_clauses(fx.v2)}
    fx.v2 = fx.v2.replace("No baseline.", f"Baseline: `{pin}`, the fixture's own.")
    fx.base = fx.write_commit({".memory-tree.conf": build_fixture_conf(fx.record, fx.view,
                                                                       UNMEASURED_PIN if "unmeasured-pin" in plants
                                                                       else pin),
                               fx.record: fx.v2}, "fixture: the baseline taken, and the design keys declared")
    fx.set_branch("run", new=True)
    if "unmeasured-specs" not in plants:
        add_base(fx)
        for p in plants:
            if p not in UNMEASURED_PLANTS:
                add_plant(fx, p)
    fx.write_tree()
    return fx


def remove_tree(root):
    """Delete a fixture repository. git writes its loose objects read-only, which Windows refuses to
    delete, so a refused path is made writable and deleted again rather than left in the temp folder."""
    def remove_read_only(func, path, _exc):
        os.chmod(path, stat.S_IWRITE)
        func(path)
    try:
        shutil.rmtree(root, **({"onexc": remove_read_only} if sys.version_info >= (3, 12)
                               else {"onerror": remove_read_only}))
    except OSError:
        pass


def read_fixture_conf(root):
    return parse_conf((pathlib.Path(root) / ".memory-tree.conf").read_text(encoding="utf-8"), {})


def measure_fixture(fx):
    """`(conf, the WHOLE commits, the join's result, the commit join over every sha)` of a built fixture."""
    conf = read_fixture_conf(fx.root)
    commits = routed_commits.read_routed_commits(fx.root, ["HEAD"])
    result = measure_join(fx.root, conf, commits)
    return conf, commits, result, check_commit_join(fx.root, result["members"], result["records"],
                                                    {c["sha"] for c in commits})


def read_fixture_skip(resolve=None):
    """The fixture's named SKIP line where the unattended kit does not resolve, through `resolve` or the
    kit's own resolver, naming why and every plant `STRIP_PLANTS` holds back; '' where it resolves
    (TOOL-dTrueNorth-12 S2). It sets no strip: the entry point that asked does, for its call alone."""
    try:
        read_gen_region_awk(resolve)
    except LookupError as exc:
        return (f"{SAY}: SKIP — the unattended kit does not resolve, so the plants that read the "
                f"generated-region strip are not run: {exc} · {' '.join(STRIP_PLANTS)}")
    return ""


def run_fixture(plants, policy, approval, host=False, resolve=None):
    """Build the fixture, print its lines, and return the exit (S8). Where the unattended kit does not
    resolve, through `resolve` or the kit's own resolver, it prints the named SKIP line first and runs the
    plants `STRIP_PLANTS` does not hold under the strip stubbed to the identity, set for this call alone
    and restored in its `finally`, so the host's path inside the call reads it too (TOOL-dTrueNorth-12 S2);
    a call asking only for held plants runs nothing and exits 0."""
    root = tempfile.mkdtemp(prefix="dj-")
    label = "fixture · " + (f"plant {plants[0]} · " if len(plants) == 1 else "every plant · " if plants
                            else "the base alone · ")
    try:
        skip = read_fixture_skip(resolve)
        if skip:
            set_gen_strip(IDENTITY_STRIP)
            print(skip)
            kept = [p for p in plants if p not in STRIP_PLANTS]
            if plants and not kept:
                return 0
            plants = kept
        fx = build_fixture(root, plants)
        if host:
            try:
                rc, lines = routed_commits.check_routed_commits(fx.root, {"GATE_PUSH_BASE": fx.read_sha(fx.base)})
            except routed_commits.Refusal as exc:
                print(f"{routed_commits.SAY} REFUSED — {exc}")
                return 2
            print("\n".join(lines))
            return rc
        _conf, _commits, result, commit = measure_fixture(fx)
        lines, findings = render_lines(result, policy, approval, label, commit)
        print("\n".join(lines))
        return 1 if policy == "refuse" and findings else 0
    except Unmeasured as exc:
        print(f"{SAY}: {label}nothing measured — {exc}")
        return 2
    finally:
        set_gen_strip(None)
        remove_tree(root)


# -------------------------------------------------------------------------------------- the arms
# The exit each plant takes under `--policy refuse` and the default approval: AC6's table for the
# instrument's 26, and this unit's own; a by-risk plant reds only under `--approval by-risk`.
PLANT_EXITS = dict({p: 1 for p in ("baseline", "clause", "subject-pass", "two-branch", "gen-text", "amended",
                                   "approver-none", "owner-bare", "owner-er", "owner-row5", "owner-row1-added",
                                   "owner-unknown-id", "add", "handback", "audit-pin", "pass-revision",
                                   "malformed-field", "malformed-risk", "malformed-follow",
                                   "malformed-supersedes", "duplicate-n", "record-late", "pipe-after")},
                   **{p: 0 for p in ("pass-none", "status-flip", "header-rev", "gen", "status-gen", "quote",
                                     "amended-joined", "approver", "defer", "fix-record", "audit-nopin",
                                     "below-risk", "owner-cause", "status-only", "subject-trailer", "rotated",
                                     "spec-notes")},
                   **{p: 2 for p in UNMEASURED_PLANTS})


BASE_MEMBERS = 6     # add_base's: a hand-back, a revision, a ledger line, a supersede, a clause, an add


def derive_plant_needle(plant):
    """The text a plant's red line must carry, so an arm reds for its own reason and not another's."""
    u = PLANT_UNITS.get(plant)
    nobody = "recorded by nobody"
    return {"baseline": "the Baseline: line moved", "clause": f"{CLAUSE_ROLES['clause']} moved",
            "subject-pass": f"at {u}@rev-1 (spec-revised): {nobody}", "pass-revision": f"at {u}@rev-1 (spec-revised): {nobody}",
            "two-branch": f"at {u}@rev-1 (spec-revised): {nobody}", "gen-text": f"at {u}@rev-1 (spec-revised): {nobody}",
            "amended": f"at {u}@rev-2 (spec-revised): {nobody}", "add": f"at new unit {u} (design-to-spec): {nobody}",
            "handback": f"at {u}@rev-1 (spec-to-code): {nobody}", "audit-pin": "past its audited revision rev-1",
            "audit-nopin": f"no audit pin: ", "approver-none": "it records no approver",
            "owner-bare": "names the owner and cites no decision id", "owner-er": "names the owner and cites no decision id",
            "owner-row5": f"whose row does not name {APPROVER_PLANTS['owner-row5'][0]}",
            "owner-unknown-id": "cites FIX-dClosedLoop-99, which no row", "owner-row1-added": f"whose row does not name {u}",
            "malformed-field": "Caused-by is missing", "malformed-risk": "Risk moderate is outside",
            "malformed-follow": "names no clause at an eight-hex hash", "duplicate-n": "shares deviation-",
            "malformed-supersedes": "Supersedes deviation-9 is not one record id: **Supersedes:** names the stem",
            "record-late": "recorded after its departure at",
            "unmeasured-pin": f"DESIGN_BASELINE {UNMEASURED_PIN} names no commit",
            "unmeasured-specs": "reads, and no chain build of memory/design/view.md holds a spec",
            "pipe-after": "After holds a `|`: the as-built view renders **After:** as the Text cell",
            "subject-trailer": f"at {SUBJECT_TRAILER_Y}@rev-1 (spec-revised): joins ",
            "rotated": f"at {u}@rev-1 (spec-revised): joins ",
            "below-risk": "below owner, the least approver its risk loosening requires",
            "owner-cause": "below owner, the least approver its cause owner ruling requires"}.get(plant)


def check_rotated_dates(fx, result):
    """`(held, what, detail)` of the rotated plant's own arm (TOOL-dTrueNorth-24 S2): its supersede member
    carries the row commit's sha and the address `<unit>@rev-1`, and no member read from the archive, the
    base's supersede and add among them, carries the rotation commit's. An archive holding no other rescope
    member and no add is no witness of the second half, so it reds too."""
    row, rotation = (fx.read_sha(m) for m in fx.marked["rotated"])
    u = PLANT_UNITS["rotated"]
    archived = [m for m in result["members"] if f", in {TN}RUN.LANDED." in m["what"]]
    own = next((m for m in archived if m["what"].startswith(f"the rescope supersede of {u},")), None)
    others = [m for m in archived if m is not own]
    held = (own is not None and own["sha"] == row and own["address"] == f"{u}@rev-1"
            and any(m["kind"] == "add" for m in others) and any(m["kind"] == "rescope" for m in others)
            and not any(m["sha"] == rotation for m in archived))
    what = (f"TOOL-dTrueNorth-24 AC2 the rotated plant's supersede member dates by its row commit {row[:8]} at "
            f"{u}@rev-1, and no member read from the archive, the base's supersede and add included, by the "
            f"rotation commit {rotation[:8]}")
    return held, what, "\n".join(f"{(m['sha'] or 'none')[:8]} {m['address']}: {m['what']}" for m in archived)


def check_tracked_population():
    """`[(held, what, detail)]`, TOOL-dTrueNorth-26 AC10 and AC9 over one base fixture. AC10: after
    `Fixture.write_tree` the index lists every path of the branch's tree, so the fixture's records and
    specs are tracked. AC9: a record written to the work tree alone moves neither `read_records` nor the
    as-built view's `read_view_inputs`, and once staged both read it. Red against a fixture whose index
    is empty, and against a reader that globs the work tree, which reads the draft."""
    import asbuilt_view     # the view's inputs; it imports this module, so it is loaded here and not above
    root = tempfile.mkdtemp(prefix="dj-")
    arms = []
    try:
        fx = build_fixture(root, [])
        conf = read_fixture_conf(fx.root)
        index = sorted(p for p in (run_git(fx.root, "ls-files", "-z") or b"").decode("utf-8").split("\0") if p)
        tree = sorted(p for p in (run_git(fx.root, "ls-tree", "-r", "-z", "--name-only", "HEAD") or b"")
                      .decode("utf-8").split("\0") if p)
        arms.append((bool(tree) and index == tree, "TOOL-dTrueNorth-26 AC10, the fixture's index lists every path "
                     "of its branch's tree, so its records and specs are tracked",
                     f"index {len(index)} path(s), tree {len(tree)}: {sorted(set(tree) - set(index))[:5]}"))

        def read_ids():
            return ([r["id"] for r in read_records(fx.root, conf)],
                    [r["id"] for r in asbuilt_view.read_view_inputs(fx.root, conf)[2]])

        before = read_ids()
        path, text = fx.render_record("FIX-dTrueNorth-1", "FIX-dTrueNorth-1@rev-1 [scope]", "spec writer", n=77)
        (fx.root / path).write_bytes(text.encode("utf-8"))
        draft = read_ids()
        run_git(fx.root, "add", "--", path)
        staged = read_ids()
        rid = pathlib.PurePosixPath(path).stem
        held = (bool(before[0]) and draft == before
                and all(rid in s and len(s) == len(b) + 1 for s, b in zip(staged, before)))
        arms.append((held, "TOOL-dTrueNorth-26 AC9, an untracked deviation record moves neither the join's records "
                     "nor the view's, and staged it joins both", f"before {before}\ndraft {draft}\nstaged {staged}"))
    except (Unmeasured, DesignRefusal, RuntimeError) as exc:
        arms.append((False, "TOOL-dTrueNorth-26 AC9 and AC10's fixture builds and reads", str(exc)))
    finally:
        remove_tree(root)
    return arms


def check_blob_reader():
    """`(held, what, detail)`, TOOL-dTrueNorth-26 AC20: `read_blobs` answers None for a blob that is not
    UTF-8 and for a path the rev does not hold, the text for one that is, maps the reader's `OSError` to
    Unmeasured, and holds no batch parser of its own, read from its own source. Red against the reader it
    replaced, which decoded with replacement characters and parsed a batch it spawned itself."""
    import ast
    import inspect
    import textwrap
    import tree_lib
    root = tempfile.mkdtemp(prefix="dj-")
    what = ("TOOL-dTrueNorth-26 AC20, read_blobs routes through tree_lib.read_blobs_at: None for a blob that is not "
            "UTF-8, Unmeasured on the reader's OSError, and no batch spawn of its own")
    try:
        fx = Fixture(root, "memory/design/record.md", "memory/design/view.md")
        if run_git(".", "init", "-q", str(root)) is None:
            raise RuntimeError(f"fixture: git init failed at {root}")
        sha = fx.read_sha(fx.write_commit({"memory/ok.md": "ok\n", "memory/bad.md": b"\xff\xfe not UTF-8\n"},
                                          "fixture: a blob that is UTF-8 and one that is not"))
        asks = [(sha, "memory/ok.md"), (sha, "memory/bad.md"), (sha, "memory/absent.md")]
        got = read_blobs(root, asks)
        real, refused = tree_lib.read_git_output, ""

        def read_refused(*_a, **_k):        # the stand-in reader, refusing as a failed spawn does
            raise OSError("the stand-in reader cannot start")

        tree_lib.read_git_output = read_refused
        try:
            read_blobs(root, asks)
        except Unmeasured as exc:
            refused = str(exc)
        finally:
            tree_lib.read_git_output = real
        body = ast.parse(textwrap.dedent(inspect.getsource(read_blobs)))
        calls = {n.func.id for n in ast.walk(body) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)}
        batch = [c.value for c in ast.walk(body) if isinstance(c, ast.Constant) and isinstance(c.value, str)
                 and "--batch" in c.value]
        held = ([got.get(a) for a in asks] == ["ok\n", None, None] and "cannot start" in refused
                and "read_blobs_at" in calls and not batch)
        return held, what, f"answers {[got.get(a) for a in asks]}\nrefused: {refused}\ncalls {sorted(calls)} batch {batch}"
    except (Unmeasured, RuntimeError, OSError) as exc:
        return False, what, str(exc)
    finally:
        remove_tree(root)


def check_composed_run(counts):
    """`(held, what, detail)` of the composed run (TOOL-dTrueNorth-12 S3): every plant `counts` holds, each
    mapped to the member count of the base and that plant alone, built over one base. Its members must be
    `BASE_MEMBERS` plus each plant's own increment, a sum derived from the single-plant builds and never
    typed, and its one late member the `record-late` plant's, so two roles sharing a unit, clause or row,
    which would lose a member and read the later record late, red."""
    plants = list(counts)
    want = BASE_MEMBERS + sum(n - BASE_MEMBERS for n in counts.values())
    unit = PLANT_UNITS["record-late"]
    what = (f"TOOL-dTrueNorth-12 AC6 the composed run of {len(plants)} plant(s) holds {want} members, the base's "
            f"{BASE_MEMBERS} plus each plant's own, and one member recorded late, {unit}'s")
    root = tempfile.mkdtemp(prefix="dj-")
    try:
        _conf, _commits, result, commit = measure_fixture(build_fixture(root, plants))
        late = [m["address"] for m, _r, verdict in commit if verdict == "late"]
        lines, _f = render_lines(result, "report", "author-recorded", "every plant · ", commit)
        return (len(result["joins"]) == want and len(late) == 1 and late[0].startswith(f"{unit}@"), what,
                f"members {len(result['joins'])}, late {late}\n" + "\n".join(lines))
    except Unmeasured as exc:
        return False, what, str(exc)
    finally:
        remove_tree(root)


def run_plant_arms(resolve=None):
    """Every arm of the join over its fixture: `[(held, what, detail)]`. Each plant is built once with the
    base and measured under both policies, and under by-risk where that is what reds it; the base alone
    is green under both approvals; the host's RANGE and WHOLE halves read the late record (AC10); the
    rotated plant's members date by the commits that wrote their rows (`check_rotated_dates`); a plant
    with no needle has its report arm read the render's findings count, which a planted finding moves
    (TOOL-dTrueNorth-26 S18); the tracked population (`check_tracked_population`) and the one blob reader
    (`check_blob_reader`); and last the composed run of every plant measured here (`check_composed_run`). Where the unattended kit does not
    resolve, through `resolve` or the kit's own resolver, it prints the named SKIP line and runs every plant
    `STRIP_PLANTS` does not hold under the strip stubbed to the identity, set for this call alone and
    restored in its `finally`, the record-late arm's host path included (TOOL-dTrueNorth-12 S2)."""
    arms, counts, bites = [], {}, []
    try:
        skip = read_fixture_skip(resolve)
    except Unmeasured as exc:
        return [(False, "TOOL-dTrueNorth-12 S2 the generated-region strip resolves, or its plants are skipped "
                        "by name", str(exc))]
    if skip:
        set_gen_strip(IDENTITY_STRIP)
        print(skip)
    # The fixtures have no remote, so the ladder's two keys the caller may have exported are held back
    # for the call and restored after it: the rows are read on the fallback whatever the caller's shell.
    ladder_env = {k: os.environ.pop(k) for k in ("GOV_REMOTE", "GOV_DEFAULT_BRANCH") if k in os.environ}
    try:
        for plant in (None,) + tuple(p for p in PLANTS if not (skip and p in STRIP_PLANTS)):
            root = tempfile.mkdtemp(prefix="dj-")
            try:
                fx = build_fixture(root, [plant] if plant else [])
                try:
                    _conf, _commits, result, commit = measure_fixture(fx)
                except Unmeasured as exc:
                    # TOOL-dTrueNorth-16 AC23: each cause alone is nothing measured, naming its own reason.
                    needle = derive_plant_needle(plant) if plant else None
                    arms.append((plant in UNMEASURED_PLANTS and needle in str(exc),
                                 f"TOOL-dTrueNorth-16 AC23 {'plant ' + plant if plant else 'the base'} measures "
                                 f"nothing, exit 2 under both policies, naming `{needle}`", str(exc)))
                    continue
                # Liveness: the base plants six members, each joined, so a population that read nothing, or a
                # join that matched nothing, cannot pass an exit-0 arm by finding nothing.
                live = sum(1 for _m, r in result["joins"] if r is not None) >= BASE_MEMBERS
                if plant is None:
                    for approval in APPROVALS:
                        lines, findings = render_lines(result, "refuse", approval, "base · ", commit)
                        arms.append((findings == 0 and live and len(result["joins"]) == BASE_MEMBERS,
                                     f"TOOL-dTrueNorth-4 AC1 the base alone exits 0 under refuse and {approval}, "
                                     f"its {BASE_MEMBERS} members each joined", "\n".join(lines)))
                    # TOOL-dTrueNorth-27 AC15: the fixture has no remote, so its rows are read on the
                    # ladder's fallback, `main`; a GOV_REMOTE naming no remote of it is the ladder's refusal,
                    # no ref, and the render names that refusal on its unread line.
                    os.environ["GOV_REMOTE"] = "no-such-remote"
                    try:
                        ref, why = read_decision_ref(fx.root)
                        refused_lines = render_lines(measure_fixture(fx)[2], "report", "author-recorded", "base · ",
                                                     commit)[0]
                    finally:
                        os.environ.pop("GOV_REMOTE", None)
                    arms.append((result["ref"] == "main" and ref is None and "GOV_REMOTE names no-such-remote" in why
                                 and any("DECISIONS.md is unread, the remote ladder resolving no ref" in ln
                                         and why in ln for ln in refused_lines),
                                 "TOOL-dTrueNorth-27 AC15 the decision rows are read on the ref the remote ladder "
                                 "resolves, `main` in a fixture with no remote, and a GOV_REMOTE naming no remote "
                                 "of it is no ref and the ladder's refusal, named on the unread line",
                                 f"ref {result['ref']!r}; refused ref {ref!r}: {why}\n" + "\n".join(refused_lines)))
                    continue
                counts[plant] = len(result["joins"])
                needle = derive_plant_needle(plant)
                approval = "by-risk" if plant in RISK_PLANTS else "author-recorded"

                def check_needle(lines):
                    if needle is None:               # a needle-less plant's arms read the findings count
                        raise ValueError(f"plant {plant} has no needle, so no line of it can be checked")
                    if plant == "audit-nopin":       # the base's units carry no pin either, so the unit is the needle
                        return any(ln.startswith(f"{SAY}:   {needle}") and PLANT_UNITS[plant] in ln for ln in lines)
                    return any(needle in ln for ln in lines)

                lines, findings = render_lines(result, "refuse", approval, f"plant {plant} · ", commit)
                want = PLANT_EXITS[plant] if plant not in RISK_PLANTS else 1
                arms.append(((1 if findings else 0) == want and live and (want == 0 or check_needle(lines)),
                             f"TOOL-dTrueNorth-4 plant {plant} exits {want} under refuse and {approval}"
                             + (f", naming `{needle}`" if want else ""), "\n".join(lines)))
                lines, report_findings = render_lines(result, "report", approval, f"plant {plant} · ", commit)
                # TOOL-dTrueNorth-26 S18: a plant with no needle plants no line, so its report arm asserts the
                # report render's own findings count is 0, the value `render_lines` returns whatever the
                # policy; a constant True arm asserted nothing.
                arms.append((check_needle(lines) if needle is not None else report_findings == 0,
                             f"TOOL-dTrueNorth-4 plant {plant} under report, which never refuses, "
                             + ("lists what it plants" if needle is not None else "renders no finding"),
                             "\n".join(lines)))
                if needle is None:
                    # The count that arm reads must move: one malformed record planted beside the
                    # plant's own records is a finding the same report render counts (AC21).
                    planted = dict(result, records=result["records"] + [read_record(
                        f"{TN}build/2026-10-21-build-FIX-dTrueNorth-1-deviation-999.md", "- **Risk:** moderate\n")])
                    bites.append((plant, report_findings,
                                  render_lines(planted, "report", approval, f"plant {plant} · ", commit)[1]))
                if plant == "subject-trailer":
                    x = PLANT_UNITS[plant]
                    arms.append((check_needle(lines) and not any(f"at {x}@rev-" in ln for ln in lines),
                                 f"TOOL-dTrueNorth-16 AC13 the commit naming {x} in its subject and "
                                 f"{SUBJECT_TRAILER_Y} in its trailer is the first pass of {SUBJECT_TRAILER_Y} "
                                 f"and of no {x}", "\n".join(lines)))
                if plant == "rotated":
                    arms.append(check_rotated_dates(fx, result))
                if plant in RISK_PLANTS:
                    lines, findings = render_lines(result, "refuse", "author-recorded", f"plant {plant} · ", commit)
                    arms.append((findings == 0, f"TOOL-dTrueNorth-4 AC4 plant {plant} exits 0 under author-recorded",
                                 "\n".join(lines)))
                if plant == "record-late":
                    late = fx.read_sha(fx.marked[plant])[:8]
                    try:
                        rc, host = routed_commits.check_routed_commits(fx.root,
                                                                       {"GATE_PUSH_BASE": fx.read_sha(fx.base)})
                    except routed_commits.Refusal as exc:
                        rc, host = 2, [str(exc)]
                    out = "\n".join(host)
                    rng, _, whole = out.partition("routed-commits: deviation: WHOLE")
                    u = PLANT_UNITS[plant]
                    arms.append((rc == 0 and f"routed-commits: deviation: RANGE" in rng
                                 and f"at {u}@rev-1 (spec-revised): recorded after its departure at {late}" in rng
                                 and f"at {u}@rev-1 (spec-revised): joins " in whole,
                                 "TOOL-dTrueNorth-4 AC10 the host's RANGE half reads the record as written after its "
                                 "departure, its WHOLE half joins it, and the host exits 0", out))
            except Unmeasured as exc:
                arms.append((False, f"TOOL-dTrueNorth-4 plant {plant} could not build its fixture", str(exc)))
            finally:
                remove_tree(root)
        arms.append((bool(bites) and all(f == 0 and p > 0 for _p, f, p in bites),
                     f"TOOL-dTrueNorth-26 AC21, the report arm of each of the {len(bites)} plant(s) with no needle reads "
                     "the render's findings count: 0 over the plant, above 0 over a planted finding",
                     "\n".join(f"{p}: findings {f}, planted {n}" for p, f, n in bites)))
        arms += check_tracked_population()
        arms.append(check_blob_reader())
        arms.append(check_composed_run(counts))
    finally:
        set_gen_strip(None)
        os.environ.update(ladder_env)
    return arms


def run_selftest():
    held = 0
    arms = run_plant_arms()
    for ok, what, detail in arms:
        held += bool(ok)
        print(f"  {'ok  ' if ok else 'FAIL'} — {what}" + ("" if ok else f"\n{detail}"))
    print(f"{SAY} selftest: {held} of {len(arms)} arm(s) held")
    return 0 if held == len(arms) else 1


def main(argv):
    ap = argparse.ArgumentParser(prog="deviation_join.py")
    ap.add_argument("--policy", choices=POLICIES, default="report")
    ap.add_argument("--approval", choices=APPROVALS, default="author-recorded")
    ap.add_argument("--range", dest="span", metavar="A..B")
    ap.add_argument("--fixture", action="store_true")
    ap.add_argument("--plant", choices=PLANTS)
    ap.add_argument("--host", choices=("routed-commits",))
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return run_selftest()
    if a.plant and not a.fixture:
        ap.error("--plant takes --fixture")
    if a.span and (a.fixture or a.host):
        ap.error("--range reads the tree's history, so it takes neither --fixture nor --host")
    if a.fixture:
        return run_fixture([a.plant] if a.plant else [p for p in PLANTS if p not in UNMEASURED_PLANTS], a.policy,
                           a.approval, host=bool(a.host))
    try:
        root = pathlib.Path(routed_commits.run_git(os.getcwd(), "rev-parse", "--show-toplevel").decode("utf-8").strip())
        if a.host:
            rc, lines = routed_commits.check_routed_commits(root, os.environ)
            print("\n".join(lines))
            return rc
        conf = routed_commits.load_conf(root)
        armed, why = read_join_state(root, conf)
        if not armed:
            print(f"{SAY}: join off — {why}")
            return 0
        commits = routed_commits.read_routed_commits(root, ["HEAD"])
        result = measure_join(root, conf, commits)
        shas = {c["sha"] for c in commits}
        if a.span:
            raw = run_git(root, "rev-list", a.span, "--")
            if raw is None:
                print(f"{SAY}: --range {a.span} names no revision range in this clone")
                return 2
            shas = set(raw.decode("utf-8").split())
        lines, findings = render_lines(result, a.policy, a.approval, "",
                                       check_commit_join(root, result["members"], result["records"], shas))
    except routed_commits.Refusal as exc:
        print(f"{routed_commits.SAY} REFUSED — {exc}")
        return 2
    except Unmeasured as exc:
        print(f"{SAY}: nothing measured — {exc}")
        return 2
    print("\n".join(lines))
    return 1 if a.policy == "refuse" and findings else 0


if __name__ == "__main__":
    sys.modules.setdefault("deviation_join", sys.modules[__name__])
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
