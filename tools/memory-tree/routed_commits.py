#!/usr/bin/env python3
"""routed_commits.py — every commit touching a product path names a unit specced before it.

TOOL-aRoutedQuill-3. The write gate (`scratch-guard.js`) sees Edit and Write calls only, so a product
file changed through a shell, a hook-less run or an unwired install reaches a commit with no unit
behind it. This leg grades the COMMITS: every non-merge commit touching a path under `ROUTED_PATHS`
must name a unit id whose spec existed at that commit's first parent.

    python routed_commits.py                          # grade the range, print the summary
    python routed_commits.py --newest-unit <range> [<path>]  # the newest unit id <range>'s commits
                                                      # attribute, those touching <path> alone if named
    python routed_commits.py --red-fix-limits <rev>   # one `Red-fix:` commit against the lane's limits
    python routed_commits.py --selftest               # the arms, over scratch repositories

THE RANGE. `$GATE_PUSH_BASE..HEAD` (RANGE) when that variable is set, not all zeros, and names a
commit in this clone — the pushed commits, at the pre-push hook. Otherwise all of HEAD's history
(WHOLE), and the summary says why. An unresolvable value WIDENS and never narrows. At a resolvable
base the WHOLE history is graded BESIDE the range (TOOL-aRoutedQuill-10), because remote CI grades
WHOLE and a red only CI sees must not land: a second summary line, `WHOLE beside RANGE`, and a
`FAILED in WHOLE` list naming only shas the RANGE half did not. The RANGE half reads no waiver, so
nothing excuses a pushed commit; `ROUTED_COMMIT_WAIVED` is read wherever WHOLE is graded, the push
boundary's WHOLE half included, and a listed sha that is not a violation there reds as stale.

ATTRIBUTION is the UNION of the ids among the subject's whole tokens and the ids a `Pass:` trailer
names; `Pass: none` adds none and keeps the subject's. It is the `union` view of the kit's one trailer
reader, `commit_trailers.py` (TOOL-dDeclaredLoop-23), and deliberately not its `replace` view, which
`read_attribution_tokens` in the unattended kit names, where a trailer REPLACES the subject: that reader
decides which commit is a unit's pass, this leg only whether a commit is attributed to any unit.
Which spec defines an id is `tree_lib.parse_spec_h1` over every spec at HEAD.

THE RED-FIX LANE (TOOL-aNimbleMend-8). A graded commit that names no unit is admitted when it carries
at least one `Red-fix: <leg name>` trailer, one leg per trailer line, and every value is a leg name
of the `LEG_MANIFEST` file in that commit's own tree; the summary line counts them as `<n> red-fix`.
A blank `LEG_MANIFEST` reads as `gate-legs.json` beside the run-gates kit found beside this one
(`resolve_leg_manifest`, TOOL-aNimbleMend-15). A value that names no leg, a blank `LEG_MANIFEST`
with no such kit inside the repository, and a commit holding no manifest are violations that say so. A commit that names a unit is graded as ever and its trailer is not read. The policy
key `bar.inline-red-fixes` gates the pushed RANGE and never the history: off, a `Red-fix:` commit in
RANGE is `names no unit`, and WHOLE still admits it, so turning the key off reds nothing that
landed. The key is read once, by `read_lane_state`, and only when a RANGE commit is a candidate; a
history with no trailer costs no spawn it did not cost before.

THE LANE'S LIMITS (TOOL-aNimbleMend-10). Every non-merge commit of each population carrying a
`Red-fix:` trailer, whether or not it names a unit, is graded against four limits, and a finding
moves the exit to 1. L1 size: at most RED_FIX_MAX_PATHS paths under `ROUTED_PATHS` and at most
RED_FIX_MAX_LINES lines over them, added plus deleted, a binary path over the bound. L2: no path the
policy kit's `guarded-paths.txt` lists in the tree of the commit's first parent, at the path the list
has in the working tree (TOOL-aTemperedLane-2); the working tree's list where that parent holds none,
the commit has no parent, or the list lies outside the repository; where the working tree's list does
not resolve, no path under `.governance/`. L3: no path under any build's `spec/` folder, less a plain
modification, its mode unchanged, confined to the spec's one `gen:spec-records` region: each side
holds exactly one marker pair in order and every byte outside it, both marker lines included, is
unchanged (TOOL-aTemperedLane-1). L4: no path added under `ROUTED_PATHS`, a rename read as a deletion
and an addition. `ROUTED_COMMIT_WAIVED` excuses a finding in WHOLE and never in RANGE, and the stale
rule counts a finding as a violation. One `red-fix limits` line per population says how many were
graded. A population holding no fix commit costs no git call. Any other costs one log, plus one read
of the parents' lists where a fix commit has a parent and the list lies inside the repository, plus
one read of spec blobs where a fix commit plainly modifies a spec: three calls at most, whatever the
count of fix commits. `--red-fix-limits <rev>` grades the one commit `<rev>` names,
merge or not, with no waiver: exit 0 inside the limits, 1 over one, 2 when the rev names no commit
or the commit carries no trailer. NOT checked: whether the change is a fix, a new surface made
inside an existing file, a deleted path, and any record outside `spec/`. L2 does not check a path the
list gained after the commit or in it, whenever the commit lands; nor a path an earlier commit took
off the list, so a path unlisted in one commit, fixed in the next and relisted later passes; nor an
edit of the list alone, since the list does not name itself; nor a list that has moved, a parent
holding none at its present path being graded by the working tree's, which the graded run controls;
nor the list's file mode, a symbolic link there read as its target text. A guarded list
absent from the working tree, deleted by the fix commit or by any later one, leaves only the
`.governance/` prefix, whatever the first parent's list holds (TOOL-aTemperedLane-3).
L3 no longer checks what a fix commit writes between two unchanged marker lines: whether it is the generator's row is `gen_build_index.py --check`'s answer, at the graded tip
and never per commit, so a hand-written line there that a later commit removes is seen by nothing.
Nor where the pair sits: the region's extent is the parent's, so a pair an earlier commit widened
widens what a fix commit may write.

Exit 0 clean · 1 a violation or a stale waiver · 2 REFUSED, the leg cannot give an answer worth
reading (an unarmed conf, a shallow clone, an empty id map, a truncated log stream).

WHAT THIS DOES NOT CHECK, stated because a structural check reads as a semantic one to everybody who
did not write it. ANY named id with a spec at the first parent passes (F1): whether that unit's
scope covers the change is not read, nor the spec's quality, tier or status. A merge's own content
is not graded, so a conflict resolution that adds product code passes; its non-merge parents are
graded. Commits committed before `ROUTED_COMMIT_CUTOFF` are counted and not graded, and the cutoff
is a date the committer sets. The graded run controls the conf, so it can narrow `ROUTED_PATHS`,
move the cutoff or list a waiver: the summary prints all three as a trace, not a guard. A spec
moved since the commit is looked for at its HEAD path and reads as absent, and so is a leg manifest
moved since a `Red-fix:` commit: it is looked for at the path HEAD's conf names. The lane checks
neither that the commit fixes the red nor that the named leg was ever red: the gate ledger is per
clone and untracked, so this leg reads none, and a trailer naming a real leg passes. Pass-order history
(the unattended kit) answers "spec at the first parent" from a header window and lets a trailer
replace the subject; this file reads the H1 and the union, and NOTHING machine-joins the two files.

Every git call is pinned (`--no-replace-objects`, `tree_lib.build_git_env`) and counted: the
self-test holds the number of spawns constant whatever the range holds.

THE DEVIATION JOIN (TOOL-dTrueNorth-4) is hosted here, its core `deviation_join.py`, over the two
populations this leg already reads: the RANGE half asks whether each design or spec departure in
the pushed range had its deviation record in its departing commit's tree, the WHOLE half joins every
departure at HEAD and grades every approver. Its lines follow this leg's under `routed-commits:
deviation`, and it runs the chain's `report` value, so it never moves the exit. Off unless the conf
declares all four DESIGN_* keys, in one line and with no git call, so the
constant spawn count holds there; armed, its spawns grow with the chain-build specs' revisions. A
declared design it cannot measure is REFUSED, exit 2.

THE HISTORY VERDICT STORE (TOOL-dQuietDisk-4). A commit's log record never changes once its id exists,
so the leg keeps the parsed records in TOOL-dQuietDisk-1's history verdict store, through this kit's
copy of `history_store.py`, under the leg name `routed-commits`. An item is one bucket: the records of
every commit of HEAD's history whose id opens with the same RECORD_BUCKET_HEX hex digits, a JSON array
sorted by id, keyed by the prefix and a digest of its member ids, and by the working bytes of this
file, the trailer reader, `tree_lib.py` and the trailer key table, so an edit to any of them misses
every bucket. A run reads each bucket, recovers a moved bucket's old members through this worktree's
last filled tip, and logs only the commits no bucket holds: by id, or over `HEAD` past
LOG_BATCH_BOUND. Each population's order is one `git rev-list`, so a warm run with no new commit runs
no `log --name-only` and still pays the store's resolve, the switch's policy read and one `rev-parse`,
which are not in the counted spawns above. A torn, foreign or misshapen bucket is logged again, and a
fill that leaves a commit unread writes nothing. The policy key `tests.history-verdicts` is the switch:
at `regraded`, or where the store cannot resolve, each population is read by its one log pass and
nothing is written. No verdict is stored: every commit is graded on every run, against HEAD's id map.
"""
from __future__ import annotations

import contextlib
import datetime
import hashlib
import io
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

# CPython writes bytecode beside the SOURCE, inside the tree a hook may be committing.
sys.dont_write_bytecode = True

KIT = pathlib.Path(__file__).resolve().parent
if str(KIT) not in sys.path:
    sys.path.append(str(KIT))
from tree_lib import (GIT_ENV_LEAKS, RED_FIX_TRAILER, SPEC_RECORDS_CLOSE, SPEC_RECORDS_OPEN,  # noqa: E402
                      build_git_env, build_spec_path_re, check_marker_line, parse_conf, parse_leg_names,
                      parse_spec_h1, read_policy_value)
from commit_trailers import derive_attribution, read_commits, read_key_table  # noqa: E402  the kit's one trailer reader
from history_store import HistoryStore, resolve_store  # noqa: E402  the kit's copy of the history verdict store

SAY = "routed-commits"
#: TOOL-dQuietDisk-4: the most commit ids one log reads by id; past it the fill logs `HEAD` whole.
#: 500 ids at 41 bytes hold the argv near 21 KB, under the 32,767-character command line of Windows.
LOG_BATCH_BOUND = 500
#: TOOL-dQuietDisk-4: the hex digits of a commit id that name its bucket, so 256 buckets.
RECORD_BUCKET_HEX = 2
#: TOOL-aNimbleMend-10 F1: the most paths under ROUTED_PATHS one `Red-fix:` commit may change.
RED_FIX_MAX_PATHS = 3
#: TOOL-aNimbleMend-10 F1: the most lines, added plus deleted, it may change over those paths.
RED_FIX_MAX_LINES = 60
ZERO_SHA_RE = re.compile(r"^0+$")
SHA_RE = re.compile(r"^[0-9a-f]{7,40}$")
#: Every git process this module starts, counted so the self-test can hold it constant (AC6).
GIT_SPAWNS = [0]


class Refusal(Exception):
    """S7: the leg cannot give an answer worth reading. Exit 2, never a reassuring zero."""


def run_git(repo, *args, stdin: bytes | None = None, may_fail: bool = False):
    """One pinned git call in `repo`, its stdout as bytes; None on failure when `may_fail`.

    Its env is `build_git_env` less `tree_lib.GIT_ENV_LEAKS`, the kit's one list, `GIT_NAMESPACE`
    included (TOOL-dTrueNorth-26 S1): every call here names its repository explicitly, so dropping the
    variables a hook exports is always correct, and it is what keeps a self-test fixture from reading
    the real repository when the bar runs inside a hook."""
    GIT_SPAWNS[0] += 1
    env = {k: v for k, v in build_git_env().items() if k not in GIT_ENV_LEAKS}
    argv = ["git", "--no-replace-objects", "-c", "log.showSignature=false", "-C", str(repo), *args]
    proc = subprocess.run(argv, input=stdin, capture_output=True, env=env)
    if proc.returncode != 0:
        if may_fail:
            return None
        detail = proc.stderr.decode("utf-8", "replace").strip()
        refusal = Refusal(f"`git {' '.join(args)}` failed: {detail}")
        # TOOL-dDeclaredLoop-37 S5: a caller whose verb answers through its status reads it here.
        refusal.status, refusal.out = proc.returncode, proc.stdout
        raise refusal
    return proc.stdout


def load_conf(repo: pathlib.Path) -> dict:
    """The tree's `.memory-tree.conf`, through the kit's one parser."""
    path = repo / ".memory-tree.conf"
    if not path.is_file():
        raise Refusal(f"no .memory-tree.conf at {repo.as_posix()}, so there is no ROUTED_PATHS to grade against")
    return parse_conf(path.read_bytes().decode("utf-8", "replace").replace("\r\n", "\n"), {})


def build_id_re(families):
    """A unit id as a whole token, over the declared family prefixes."""
    alt = "|".join(sorted(set(families))) or "(?!)"
    return re.compile(r"(?<![A-Za-z0-9-])(?:" + alt + r")-[A-Za-z0-9]+-\d+(?![A-Za-z0-9-])")


def extract_unit_ids(text: str, id_re) -> list:
    """Every id `text` names, in order, once each."""
    seen: list = []
    for m in id_re.finditer(text):
        if m.group(0) not in seen:
            seen.append(m.group(0))
    return seen


def extract_families(conf: dict) -> list:
    """The prefixes of `FAMILIES` (`TOOL`, not `tooling:TOOL`), each VALIDATED as letters: a prefix is
    spliced into the id pattern, and an escaped one would match nothing while a `|` would match all."""
    families = [p.split(":", 1)[-1] for p in (conf.get("FAMILIES") or "").split() if p.split(":", 1)[-1]]
    for fam in families:
        if not re.fullmatch(r"[A-Za-z]+", fam):
            raise Refusal(f"FAMILIES prefix '{fam}' is not letters only, so it cannot name an id family")
    return families


def check_conf(conf: dict, tracked: list) -> tuple:
    """`(entries, cutoff, families, memory_root, waived)`, or a Refusal naming the key or entry (S7)."""
    memory_root = (conf.get("MEMORY_ROOT") or "memory").strip().strip("/")
    routed = (conf.get("ROUTED_PATHS") or "").strip()
    if not routed:
        raise Refusal("ROUTED_PATHS is blank or absent in .memory-tree.conf, so the leg has no product set to grade")
    cutoff = (conf.get("ROUTED_COMMIT_CUTOFF") or "").strip()
    if not cutoff:
        raise Refusal("ROUTED_COMMIT_CUTOFF is blank or absent in .memory-tree.conf; declare the date the leg arms from")
    try:
        datetime.date.fromisoformat(cutoff)
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", cutoff):
            raise ValueError(cutoff)
    except ValueError:
        raise Refusal(f"ROUTED_COMMIT_CUTOFF '{cutoff}' is not an ISO date (YYYY-MM-DD)") from None
    entries = []
    for raw in routed.split():
        entry = raw.replace("\\", "/")
        while entry.startswith("./"):
            entry = entry[2:]
        bare = entry.rstrip("/")
        if re.match(r"^([A-Za-z]:|/|~)", entry):
            raise Refusal(f"ROUTED_PATHS entry {raw} is absolute; entries are repo-root-relative")
        if ".." in entry.split("/"):
            raise Refusal(f"ROUTED_PATHS entry {raw} climbs through ..")
        # Two-way (TOOL-aRoutedQuill-12 S6): an entry under MEMORY_ROOT covers it as surely as one above it.
        if (bare in ("", ".") or memory_root == bare or memory_root.startswith(bare + "/")
                or bare.startswith(memory_root + "/")):
            raise Refusal(f"ROUTED_PATHS entry {raw} covers MEMORY_ROOT ({memory_root}), so a spec commit "
                          f"would need a spec before itself")
        if not any(test_routed_path(p, [entry]) for p in tracked):
            raise Refusal(f"ROUTED_PATHS entry {raw} names nothing tracked at HEAD; a directory entry ends in /")
        entries.append(entry)
    families = extract_families(conf)
    if not families:
        raise Refusal("the id map is empty: FAMILIES is blank in .memory-tree.conf, so no commit could name a unit")
    waived = (conf.get("ROUTED_COMMIT_WAIVED") or "").split()
    for sha in waived:
        if not SHA_RE.match(sha):
            raise Refusal(f"ROUTED_COMMIT_WAIVED entry '{sha}' is not a commit sha (7 to 40 lowercase hex)")
    return entries, cutoff, families, memory_root, waived


def test_routed_path(path: str, entries: list):
    """The entry `path` lies under — equal to a file entry, or under a directory entry — or None."""
    for entry in entries:
        if (entry.endswith("/") and path.startswith(entry)) or path == entry:
            return entry
    return None


def read_blob_batch(repo, names: list) -> dict:
    """`{name: the blob's bytes, or None}` for every object name of `names`, in ONE `git cat-file --batch`
    and no call for an empty list. None where the answer is not a blob with a size, a body of another
    type skipped so the next header is read where it starts. A stream that ends early is a Refusal
    (TOOL-aTemperedLane-1 S3)."""
    names = list(dict.fromkeys(names))
    if not names:
        return {}
    raw = run_git(repo, "cat-file", "--batch", stdin="".join(f"{n}\n" for n in names).encode("utf-8"))
    got, pos = {}, 0
    for name in names:
        end = raw.find(b"\n", pos)
        if end < 0:
            raise Refusal(f"`git cat-file --batch` ended before it answered {name}")
        head, pos = raw[pos:end].split(), end + 1
        got[name] = None
        if len(head) != 3 or not head[2].isdigit():
            continue                            # `missing`, `ambiguous`: no body follows
        size = int(head[2])
        if pos + size >= len(raw):              # the body and the LF that closes it
            raise Refusal(f"`git cat-file --batch` ended inside {name}")
        if head[1] == b"blob":
            got[name] = raw[pos:pos + size]
        pos += size + 1
    return got


def load_spec_paths(repo, tracked: list, memory_root: str, families: list) -> tuple:
    """`({id: [spec paths]}, specs tracked)`: which spec defines each id at HEAD, in ONE read."""
    spec_re = build_spec_path_re(memory_root)
    specs = [p for p in tracked if spec_re.match(p) and p.endswith(".md")]
    id_map: dict = {}
    if not specs:
        return id_map, 0
    bodies = read_blob_batch(repo, [f"HEAD:{p}" for p in specs])
    for path in specs:
        body = bodies[f"HEAD:{path}"]
        if body is None:
            continue
        hit = parse_spec_h1(path, body.decode("utf-8", "replace").replace("\r\n", "\n"), memory_root, families)
        if hit:
            id_map.setdefault(hit[1], []).append(path)
    return id_map, len(specs)


def derive_commit_range(repo, env) -> tuple:
    """`(mode, rev args, label)`: RANGE over `$GATE_PUSH_BASE..HEAD`, else WHOLE with its reason (S4)."""
    head = run_git(repo, "rev-parse", "--verify", "HEAD").decode("utf-8").strip()
    base = (env.get("GATE_PUSH_BASE") or "").strip()
    if not base:
        return "WHOLE", ["HEAD"], "WHOLE (GATE_PUSH_BASE is unset)"
    if ZERO_SHA_RE.match(base):
        return "WHOLE", ["HEAD"], "WHOLE (GATE_PUSH_BASE is all zeros: a push creating the branch)"
    got = run_git(repo, "rev-parse", "--verify", "--quiet", base + "^{commit}", may_fail=True)
    if not got:
        return "WHOLE", ["HEAD"], f"WHOLE (GATE_PUSH_BASE {base[:12]} names no commit in this clone)"
    sha = got.decode("utf-8").strip()
    return "RANGE", [f"{sha}..{head}"], f"RANGE {sha[:8]}..{head[:8]}"


def read_routed_commits(repo, rev_args: list, held: dict | None = None) -> list:
    """Every commit in the range, newest first, from ONE log pass (S6): sha, parents, committer date,
    subject, `Pass:` trailer and the paths it touches, renames read as a deletion plus an addition.
    `red_fix` is the list of its `Red-fix:` trailer values (TOOL-aNimbleMend-8 S5), one leg name per
    trailer line: a leg name holds spaces, commas and parentheses, so a value is its whole line.
    The pass is the one trailer reader's, run through this module's pinned, counted runner
    (TOOL-dDeclaredLoop-23 S5); a key the trailer table does not register and a stream that ends
    mid-record are each a Refusal. Where no playbook kit resolves, or its table holds no row, the
    reader reads its floor keys, which hold both keys read here (TOOL-dDeclaredLoop-40).

    `held` is the leg's one dict per run (TOOL-dQuietDisk-4 S1). Given, the first call fills it from
    the history verdict store over `git rev-list HEAD`, and each population's order is one `rev-list`
    over its revision arguments, `HEAD` reusing the fill's, its records taken from the fill's map. A
    commit no record holds is skipped, so a short log yields a short list. With the store off, and
    with `held` absent, the read is the one log pass above."""
    def read_logged_commits(revs) -> list:
        try:
            return read_commits(repo, revs, ("Pass", RED_FIX_TRAILER), files=True,
                                run=lambda at, argv: run_git(at, *argv))
        except (LookupError, ValueError) as exc:
            raise Refusal(f"the commit log cannot be read: {exc}") from None

    def derive_routed_record(c) -> dict:
        c["trailer"] = " ".join(c["trailers"]["Pass"]).strip()
        c["red_fix"] = [v for v in c["trailers"][RED_FIX_TRAILER] if v]
        return c

    def derive_bucket_fields(prefix, members) -> list:
        return [prefix, hashlib.sha256("\n".join(sorted(members)).encode("ascii")).hexdigest()]

    def parse_bucket(body, members) -> dict:
        """`{sha: record}` from a bucket's body; ValueError on a body that does not parse, a record
        of another shape, or a set of ids other than `members` (S4)."""
        rows = json.loads(body)
        strs = (lambda v: isinstance(v, list) and all(isinstance(x, str) for x in v))
        got = {}
        for row in rows if isinstance(rows, list) else [None]:
            if not (isinstance(row, dict)
                    and set(row) == {"sha", "parents", "date", "subject", "trailers", "paths"}
                    and isinstance(row["sha"], str) and isinstance(row["date"], str)
                    and isinstance(row["subject"], str) and strs(row["parents"]) and strs(row["paths"])
                    and isinstance(row["trailers"], dict) and set(row["trailers"]) == {"Pass", RED_FIX_TRAILER}
                    and all(strs(v) for v in row["trailers"].values())):
                raise ValueError("a bucket record is not the reader's shape")
            got[row["sha"]] = row
        if len(got) != len(rows) or set(got) != set(members):
            raise ValueError("a bucket holds ids other than its members")
        return got

    def render_bucket(members, records) -> str:
        keys = ("sha", "parents", "date", "subject", "trailers", "paths")
        rows = [{k: records[sha][k] for k in keys} for sha in sorted(members)]
        return json.dumps(rows, sort_keys=True, separators=(",", ":"))

    def read_bucket(store, prefix, members):
        body = store.read(derive_bucket_fields(prefix, members))
        try:
            return None if body is None else parse_bucket(body, members)
        except ValueError:
            return None

    def load_record_map() -> None:
        """S2, S3: open the store once, then fill `held` over HEAD's whole order, logging only the
        commits no bucket holds, and write only when every commit of the order has its record."""
        try:
            _keys, table = read_key_table()
        except (LookupError, ValueError) as exc:
            raise Refusal(f"the commit log cannot be read: {exc}") from None
        code = [KIT / name for name in ("routed_commits.py", "commit_trailers.py", "tree_lib.py")]
        store = held["store"] = resolve_store(repo, SAY, code + ([pathlib.Path(table).resolve()] if table else []))
        if not store.stored:
            return
        order = held["order"] = run_git(repo, "rev-list", "HEAD").decode("ascii").split()
        buckets: dict = {}
        for sha in order:
            buckets.setdefault(sha[:RECORD_BUCKET_HEX], []).append(sha)
        records, missed = {}, []
        for prefix, members in buckets.items():
            got = read_bucket(store, prefix, members)
            if got is None:
                missed.append(prefix)
            else:
                records.update(got)
        tip = store.read_tip()
        if missed and tip and tip != order[0]:
            # A moved bucket's old members, through the last filled tip; a tip naming no commit gives none.
            old: dict = {}
            moved = set(missed)
            for sha in (run_git(repo, "rev-list", tip, may_fail=True) or b"").decode("ascii", "replace").split():
                if sha[:RECORD_BUCKET_HEX] in moved:
                    old.setdefault(sha[:RECORD_BUCKET_HEX], []).append(sha)
            for prefix, members in old.items():
                records.update(read_bucket(store, prefix, members) or {})
        lack = [sha for sha in order if sha not in records]
        if len(lack) > LOG_BATCH_BOUND:
            records.update((c["sha"], c) for c in read_logged_commits(["HEAD"]))
        elif lack:
            records.update((c["sha"], c) for c in read_logged_commits(["--no-walk=unsorted", *lack]))
        held["records"] = records
        if all(sha in records for sha in order):     # S5: a short log writes nothing
            for prefix in missed:
                store.write(derive_bucket_fields(prefix, buckets[prefix]), render_bucket(buckets[prefix], records))
            if tip != order[0]:
                store.write_tip(order[0])
            store.remove_aged()

    if held is None:
        return [derive_routed_record(c) for c in read_logged_commits(rev_args)]
    if not held:
        load_record_map()
    if not held["store"].stored:
        return [derive_routed_record(c) for c in read_logged_commits(rev_args)]
    order = held["order"] if rev_args == ["HEAD"] else run_git(repo, "rev-list", *rev_args).decode("ascii").split()
    return [derive_routed_record(dict(held["records"][sha])) for sha in order if sha in held["records"]]


def read_lane_state(repo) -> tuple:
    """`(on, why)`: the red-fix lane's key, `bar.inline-red-fixes`, by the ask contract's five outcomes
    (TOOL-aNimbleMend-8 S7). On for the answer `on`, and for a repository with no policy kit, where
    `why` is the NOTE the contract asks for; off for `off`, for a refused read, where `why` is the
    reader's own line, and for any other value, where `why` names the key and the value."""
    try:
        value = read_policy_value("bar.inline-red-fixes", repo)
    except LookupError:
        return True, "NOTE — no policy kit resolves beside this kit, so bar.inline-red-fixes reads on"
    except ValueError as exc:
        return False, str(exc)
    if value == "on":
        return True, ""
    if value == "off":
        return False, ""
    return False, f"bar.inline-red-fixes reads {value}, neither on nor off, so the red-fix lane is closed"


def resolve_leg_manifest(repo, conf: dict) -> str:
    """The leg manifest a `Red-fix:` value is checked against, as a path relative to `repo`: the conf's
    `LEG_MANIFEST` where it is not blank, else `gate-legs.json` beside the run-gates kit found beside
    this one (TOOL-aNimbleMend-15 S7), so a default install grades the lane with the key left blank.
    The empty string where no run-gates kit resolves or that file sits outside `repo`."""
    named = (conf.get("LEG_MANIFEST") or "").strip()
    if named:
        return named
    from backlog import resolve_kit_dir   # noqa: E402  the kit's inline copy of the sibling resolver
    try:
        beside = resolve_kit_dir("run-gates", "run-gates.sh", KIT).parent / "gate-legs.json"
        return beside.resolve().relative_to(pathlib.Path(repo).resolve()).as_posix()
    except (LookupError, OSError, ValueError):
        return ""


def read_guarded_paths():
    """The lines of the policy kit's `guarded-paths.txt` as the working tree holds it, the kit found
    beside this one; None where no policy kit resolves or the list does not read, which limit L2
    answers by refusing every path under `.governance/` (TOOL-aNimbleMend-10 S3)."""
    from backlog import resolve_kit_dir   # noqa: E402  the kit's inline copy of the sibling resolver
    try:
        text = (resolve_kit_dir("policy", "guarded-paths.txt", KIT) / "guarded-paths.txt").read_text(encoding="utf-8")
    except (LookupError, OSError, ValueError):
        return None
    return parse_guarded_paths(text)


def parse_guarded_paths(text: str) -> list:
    """The paths a guarded list's text names: its lines, less `#` comments and blank ones."""
    return [ln.strip() for ln in text.splitlines() if ln.strip() and not ln.strip().startswith("#")]


def resolve_guarded_path(repo) -> str:
    """The policy kit's `guarded-paths.txt` as a path relative to `repo`, the kit found as
    `read_guarded_paths` finds it; the empty string where it does not resolve or lies outside `repo`
    (TOOL-aTemperedLane-2 S1)."""
    from backlog import resolve_kit_dir   # noqa: E402  the kit's inline copy of the sibling resolver
    try:
        listed = resolve_kit_dir("policy", "guarded-paths.txt", KIT) / "guarded-paths.txt"
        return listed.resolve().relative_to(pathlib.Path(repo).resolve()).as_posix()
    except (LookupError, OSError, ValueError):
        return ""


def read_parent_lists(repo, fixes: list) -> dict:
    """`{sha: the paths its first parent's guarded list names}`, in ONE batched read, holding only the
    commits of `fixes` whose first parent holds a UTF-8 list at the path it has in the working tree.
    No git call where that path is not inside `repo`, or no commit has a parent (TOOL-aTemperedLane-2
    S3)."""
    path = resolve_guarded_path(repo)
    if not path:
        return {}
    names = {c["sha"]: f"{c['parents'][0]}:{path}" for c in fixes if c["parents"]}
    bodies = read_blob_batch(repo, list(names.values()))
    got = {}
    for sha, name in names.items():
        if bodies[name] is None:
            continue
        try:
            got[sha] = parse_guarded_paths(bodies[name].decode("utf-8"))
        except UnicodeDecodeError:
            pass                                # no list reads there: the caller's fallback answers
    return got


def extract_outside_records(body):
    """A spec blob's text outside its one `gen:spec-records` region, both marker lines kept; None where
    `body` is None or does not hold exactly one open and one close marker line, the open first.

    latin-1 is lossless over any bytes and the split is on LF alone, so nothing is folded: a line ending
    that moved outside the region, a marker line's included, is a difference (TOOL-aTemperedLane-1)."""
    if body is None:
        return None
    lines = body.decode("latin-1").split("\n")
    opens = [n for n, ln in enumerate(lines) if check_marker_line(ln, SPEC_RECORDS_OPEN)]
    closes = [n for n, ln in enumerate(lines) if check_marker_line(ln, SPEC_RECORDS_CLOSE)]
    if len(opens) != 1 or len(closes) != 1 or opens[0] > closes[0]:
        return None
    return "\n".join(lines[:opens[0] + 1] + lines[closes[-1]:])


def check_red_fix_limits(repo, fixes: list, entries: list, memory_root: str, guarded: list) -> dict:
    """`{sha: [finding]}` over `fixes`, the `Red-fix:` commits of one population: the inline lane's four
    limits (TOOL-aNimbleMend-10), one finding per limit a commit is over, and no key for a commit
    inside all four.

    L1 size: more than RED_FIX_MAX_PATHS paths under ROUTED_PATHS, more than RED_FIX_MAX_LINES lines
    added plus deleted over them, or a binary one. L2 guarded policy file: a path the policy kit's
    list names in the tree of the commit's first parent, else in the working tree, else any path under
    `.governance/` (TOOL-aTemperedLane-2 S1 S2). L3 spec edit: a path under any build's `spec/` folder, less a plain modification, its
    status `M` and its mode unchanged, whose two blobs are byte-identical outside their one
    `gen:spec-records` region (TOOL-aTemperedLane-1 S1). L4 new surface: a path added under
    ROUTED_PATHS, a rename read as a deletion and an addition.

    No git call where `fixes` is empty, else THREE at most, whatever the commit count: `read_parent_lists`'s
    batched read where one is owed, a `git log` over those commits alone, the shas on stdin, carrying
    the numeric and the raw status form, then, where a fix commit plainly modifies a spec, one batched
    read of those specs' blobs by the ids its raw lines carry. A merge is read against its first parent.
    `guarded` is the caller's one-slot cache of `read_guarded_paths`, filled here on the first fix
    commit of the run and never before."""
    if not fixes:
        return {}
    if not guarded:
        guarded.append(read_guarded_paths())
    parent_lists = read_parent_lists(repo, fixes)
    spec_re = build_spec_path_re(memory_root)
    raw = run_git(repo, "log", "--no-walk=unsorted", "--stdin", "--root", "--no-renames", "--raw", "--numstat",
                  "-z", "--no-abbrev", "--no-color", "--diff-merges=first-parent", "--format=%x1e%H%x1f",
                  stdin="".join(c["sha"] + "\n" for c in fixes).encode("utf-8")).decode("utf-8", "replace")
    graded = []
    for rec in raw.split("\x1e")[1:]:
        sha, rest = rec.split("\x1f", 1)
        tokens = iter(rest.split("\0"))
        paths, added, moved, lines, binary = [], [], {}, 0, False
        for tok in tokens:
            tok = tok.lstrip("\n")
            stat = re.match(r"(\d+|-)\t(\d+|-)\t(.+)$", tok, re.S)
            if tok.startswith(":"):                 # the raw form: `:modes shas STATUS`, then its path
                path = next(tokens, "")
                paths.append(path)
                old_mode, new_mode, old_id, new_id, status = tok[1:].split()
                if status.startswith("A") and test_routed_path(path, entries):
                    added.append(path)
                if status == "M" and old_mode == new_mode and spec_re.match(path):
                    moved[path] = (old_id, new_id)
            elif stat and test_routed_path(stat.group(3), entries):
                if stat.group(1) == "-":
                    binary = True
                else:
                    lines += int(stat.group(1)) + int(stat.group(2))
        graded.append((sha, paths, added, moved, lines, binary))
    bodies = read_blob_batch(repo, [i for _s, _p, _a, moved, _l, _b in graded for pair in moved.values() for i in pair])
    found = {}
    for sha, paths, added, moved, lines, binary in graded:
        kept = {}                                   # the spec paths whose change is inside the records region
        for path, pair in moved.items():
            old, new = (extract_outside_records(bodies[i]) for i in pair)
            kept[path] = old is not None and old == new
        routed_n = sum(1 for p in paths if test_routed_path(p, entries))
        listed = parent_lists.get(sha, guarded[0])
        held = [p for p in paths if (p.startswith(".governance/") if listed is None else p in listed)]
        specs = [p for p in paths if spec_re.match(p) and not kept.get(p)]
        out = []
        if routed_n > RED_FIX_MAX_PATHS or lines > RED_FIX_MAX_LINES or binary:
            out.append(f"L1 size: {routed_n} path(s), {lines} line(s){', a binary one' if binary else ''}; "
                       f"the bound is {RED_FIX_MAX_PATHS} and {RED_FIX_MAX_LINES}")
        if held:
            out.append(f"L2 guarded policy file: {', '.join(held)}")
        if specs:
            out.append(f"L3 spec edit: {', '.join(specs)}")
        if added:
            out.append(f"L4 new surface: {', '.join(added)}")
        if out:
            found[sha] = out
    return found


def check_routed_commits(repo, env) -> tuple:
    """`(exit code, lines)`: grade the range, and WHOLE beside a RANGE (S1, S4, S5, S8, S9). Raises Refusal on S7."""
    repo = pathlib.Path(repo)
    conf = load_conf(repo)
    if run_git(repo, "rev-parse", "--is-shallow-repository").decode("utf-8").strip() == "true":
        raise Refusal("this clone is shallow, so the history the leg grades is cut short; fetch full history "
                      "(`fetch-depth: 0` on actions/checkout)")
    tracked = [p for p in run_git(repo, "ls-tree", "-r", "-z", "--name-only", "HEAD").decode("utf-8", "replace").split("\0") if p]
    entries, cutoff, families, memory_root, waived = check_conf(conf, tracked)
    id_map, spec_count = load_spec_paths(repo, tracked, memory_root, families)
    if spec_count and not id_map:
        raise Refusal(f"the id map is empty: {spec_count} spec file(s) are tracked under {memory_root}/builds/*/spec/ "
                      f"and no H1 defines an id over FAMILIES {' '.join(families)}")
    mode, rev_args, label = derive_commit_range(repo, env)
    # TOOL-aRoutedQuill-10: at a resolvable base the WHOLE history is graded BESIDE the pushed range,
    # because remote CI grades WHOLE and a red only it sees must not land. The RANGE half reads no waiver.
    populations = [(mode, rev_args, label, "")]
    if mode == "RANGE":
        populations.append(("WHOLE", ["HEAD"], "WHOLE beside RANGE (the history remote CI grades)", " WHOLE"))
    id_re = build_id_re(families)
    routed = " ".join(entries)
    lines, failed, range_shas, read = [], False, set(), []
    # TOOL-aNimbleMend-8 S7: the lane key, read ONCE and only when a RANGE commit carries the trailer and
    # names no unit. It gates the pushed range, never the history: WHOLE admits whatever the key says.
    lane = []
    manifest = resolve_leg_manifest(repo, conf)
    # TOOL-aNimbleMend-10: the limits pass's lines, its listed shas, and its one-slot guarded-list cache.
    limit_lines, limit_shas, guarded = [], set(), []
    # TOOL-dQuietDisk-4 S1: the store, the WHOLE order and the record map, filled once for both populations.
    held: dict = {}
    for mode, rev_args, label, tag in populations:
        commits = read_routed_commits(repo, rev_args, held)
        read.append((mode, label.split(" (")[0], commits))
        total = int(run_git(repo, "rev-list", "--count", *rev_args).decode("utf-8").strip())
        if total != len(commits):
            raise Refusal(f"the log pass parsed {len(commits)} commit(s) and `git rev-list --count` reports {total} "
                          f"over the same range; a truncated stream is not a clean one")
        merges = exempt = not_routed = graded = 0
        violations, pending, candidates, red_fix_n = [], [], [], 0
        for c in commits:
            if len(c["parents"]) >= 2:
                merges += 1
            elif c["date"][:10] < cutoff:
                exempt += 1
            elif not any(test_routed_path(p, entries) for p in c["paths"]):
                not_routed += 1
            else:
                graded += 1
                ids = derive_attribution(c, "union", id_re)
                pairs = [(i, p) for i in ids for p in id_map.get(i, [])]
                if not ids and c["red_fix"] and mode == "RANGE" and not lane:
                    lane.append(read_lane_state(repo))
                if not ids and c["red_fix"] and (mode == "WHOLE" or lane[0][0]):
                    candidates.append(c)        # a lane candidate: its trailer is graded below
                elif not ids:
                    violations.append((c, ids, "names no unit"))
                elif not c["parents"]:
                    violations.append((c, ids, "no first parent"))
                elif not pairs:
                    violations.append((c, ids, "no spec defines it at HEAD"))
                else:
                    pending.append((c, ids, pairs))
        if pending:
            query = "".join(f"{c['parents'][0]}:{p}\n" for c, _, pairs in pending for _, p in pairs)
            answers = iter(run_git(repo, "cat-file", "--batch-check", stdin=query.encode("utf-8")).decode("utf-8", "replace").split("\n"))
            for c, ids, pairs in pending:
                present = [not next(answers).endswith(" missing") for _ in pairs]
                if not any(present):
                    paths = ", ".join(sorted({p for _, p in pairs}))
                    violations.append((c, ids, f"no spec at its first parent {c['parents'][0][:8]}: {paths}"))
        if candidates:
            # TOOL-aNimbleMend-8 S6: each candidate's manifest, in ONE batched read made only when a
            # candidate exists. Every value a leg name at its own commit admits; anything else says so.
            legs = {}
            if manifest:
                bodies = read_blob_batch(repo, [f"{c['sha']}:{manifest}" for c in candidates])
                for c in candidates:
                    body = bodies[f"{c['sha']}:{manifest}"]
                    if body is None:
                        continue                # `missing`: no manifest at that commit
                    try:
                        legs[c["sha"]] = parse_leg_names(body.decode("utf-8", "replace"))
                    except ValueError:
                        pass                    # not a leg manifest: read as absent
            for c in candidates:
                names = legs.get(c["sha"])
                strays = [v for v in c["red_fix"] if names is not None and v not in names]
                if names is None:
                    violations.append((c, [], f"its `{RED_FIX_TRAILER}:` trailer cannot be checked: " + (
                        f"no leg manifest reads at {manifest} in that commit" if manifest else "LEG_MANIFEST is blank")))
                elif strays:
                    violations.append((c, [], f"`{RED_FIX_TRAILER}: {strays[0]}` names no leg of {manifest} at that commit"))
                else:
                    red_fix_n += 1
        # TOOL-aNimbleMend-10 S1: every non-merge `Red-fix:` commit of the population against the lane's
        # four limits, whether or not it names a unit. No git call where the population holds none.
        fixes = [c for c in commits if c["red_fix"] and len(c["parents"]) < 2]
        over = check_red_fix_limits(repo, fixes, entries, memory_root, guarded)
        waived_n, limit_waived, stale = 0, 0, []
        if mode == "WHOLE" and waived:
            kept = []
            for v in violations:
                if any(v[0]["sha"].startswith(w) for w in waived):
                    waived_n += 1
                else:
                    kept.append(v)
            # S6: a limits finding is a violation to the stale rule, and the one waiver excuses it.
            stale = [w for w in waived if not any(sha.startswith(w) for sha in [v[0]["sha"] for v in violations] + list(over))]
            violations = kept
            limit_waived = sum(1 for sha in over if any(sha.startswith(w) for w in waived))
            over = {sha: found for sha, found in over.items() if not any(sha.startswith(w) for w in waived)}
        failed = failed or bool(violations or stale or over)
        limit_lines.append(f"{SAY}: red-fix limits · graded {len(fixes)} · bound {RED_FIX_MAX_PATHS} path(s), "
                           f"{RED_FIX_MAX_LINES} line(s) · {limit_waived} waived")
        # A commit over a limit is listed once: the WHOLE half names only what the RANGE half did not.
        listed = [c for c in fixes if c["sha"] in over and c["sha"] not in limit_shas]
        if listed:
            limit_lines.append(f"{SAY} FAILED — a Red-fix commit is outside the inline lane's limits:")
        limit_lines.extend(f"  {c['sha'][:8]} {c['subject']} — {found}" for c in listed for found in over[c["sha"]])
        limit_shas.update(c["sha"] for c in listed)
        lines.append(f"{SAY}: {label} · graded {graded} · {exempt} exempt by the {cutoff} cutoff · {merges} merge(s) · "
                     f"{not_routed} not routed · {waived_n} waived{f' · {red_fix_n} red-fix' if red_fix_n else ''} · "
                     f"{len(id_map)} spec id(s) at HEAD · ROUTED_PATHS {routed}")
        if mode == "RANGE" and lane and lane[0][1]:
            lines.append(f"{SAY}: {lane[0][1]}")
        if graded == 0:
            lines.append(f"{SAY}:{tag} graded 0 — the range holds {total} commit(s) and none of its non-merge commits "
                         f"on or after the {cutoff} cutoff touches ROUTED_PATHS {routed}")
        # S3: a violation is listed once; the WHOLE half names only what the RANGE half did not.
        violations = [v for v in violations if v[0]["sha"] not in range_shas]
        if violations and not tag:
            lines.append(f"{SAY} FAILED — a commit touching ROUTED_PATHS names no unit specced before it:")
        elif violations:
            lines.append(f"{SAY} FAILED in WHOLE — a commit outside the pushed range names no unit specced before "
                         f"it, and remote CI grades it:")
        for c, ids, why in violations:
            lines.append(f"  {c['sha'][:8]} {c['subject']} — {' '.join(ids) or 'no unit id'} — {why}")
        range_shas.update(v[0]["sha"] for v in violations)
        for w in stale:
            lines.append(f"{SAY} FAILED — ROUTED_COMMIT_WAIVED lists {w}, which is not a violation in the graded "
                         f"population: a stale waiver widens nothing, remove it")
    # TOOL-dTrueNorth-4 S7: the deviation join over the populations just read. It lists and never moves
    # the exit, which stays this leg's own verdict.
    return (1 if failed else 0), lines + limit_lines + check_deviation_join(repo, conf, read)


def check_deviation_join(repo, conf, read) -> list:
    """The deviation join's lines (TOOL-dTrueNorth-4 S7), hosted over the populations this leg read:
    `read` is `[(mode, label, commits)]`, its WHOLE list among them, so the join reads history once.

    Its RANGE half asks whether each member departing in the pushed range has its record in that
    commit's tree; its WHOLE half joins every member at HEAD and grades every approver. It runs the
    chain's values, `report` and `author-recorded`, so it lists and never moves the exit. Its states are
    the key rule's, `design_lib.read_design_keys` (TOOL-dTrueNorth-16 S5): OFF when all four DESIGN_*
    keys are blank, one line and no git call, so a tree declaring no design keeps this leg's constant
    spawn count. ARMED, its spawns grow with the chain-build specs' revisions. A partial key set, and a
    declared design it cannot measure, its pin unreadable among them, is a Refusal, exit 2, as an
    unarmed conf is here.
    """
    import deviation_join  # noqa: E402  the join's core, a sibling loaded only here
    try:
        armed, why = deviation_join.read_join_state(repo, conf)
        if not armed:
            return [f"{SAY}: deviation join off — {why}"]
        return [f"{SAY}: {ln}" for ln in deviation_join.read_host_lines(repo, conf, read)]
    except deviation_join.Unmeasured as exc:
        raise Refusal(f"the deviation join is armed and measures nothing: {exc}") from None


def read_newest_unit(repo, rev_range: str, path: str | None = None) -> str:
    """The first id, walking the non-merge commits of `rev_range` newest first, that a spec at HEAD
    defines, by the union reading; '' when none does. The attended lander's mint names this unit (S11),
    so an unspecced id or a merge's id would name one the leg cannot grade (TOOL-aRoutedQuill-12 S2).
    `path` limits the walk to the commits touching it, `git log ... <range> -- <path>`, read as a
    literal pathspec: the runner's size-warning attribution (TOOL-dWitnessedBar-29 S4, S5)."""
    repo = pathlib.Path(repo)
    conf = load_conf(repo)
    families = extract_families(conf)
    if not families:
        return ""
    memory_root = (conf.get("MEMORY_ROOT") or "memory").strip().strip("/")
    tracked = [p for p in run_git(repo, "ls-tree", "-r", "-z", "--name-only", "HEAD").decode("utf-8", "replace").split("\0") if p]
    id_map, _ = load_spec_paths(repo, tracked, memory_root, families)
    id_re = build_id_re(families)
    try:
        # The path rides after its own `--`; the reader's trailing `--` is then one more literal
        # pathspec, `--`, which names no file.
        revs = ["--no-merges", rev_range] + (["--", f":(literal){path}"] if path else [])
        commits = read_commits(repo, revs, ("Pass",), run=lambda at, argv: run_git(at, *argv))
    except (LookupError, ValueError) as exc:
        raise Refusal(f"the commit log cannot be read: {exc}") from None
    for c in commits:
        for uid in derive_attribution(c, "union", id_re):
            if uid in id_map:
                return uid
    return ""


#: TOOL-dDeclaredLoop-37 S5: the two spellings of a consumer's own trailer parse, each a case-insensitive
#: extended pattern (TOOL-dDeclaredLoop-67 S54) split inside its literal, so the probe never reads this line
#: as a hit. S19 cuts the REGION of the reader's inline block, from its opening marker line to its closing
#: one, never the carrier file: the same spelling below the closing marker, or in a carrier holding no
#: block, is graded like any other line. A comment line is cut wherever it sits.
TRAILER_PARSE_NEEDLES = ("trailers:[^)]*key=" "pass", "interpret-trailers " "--parse")
#: The inline block whose region the scan cuts, by its marker lines.
TRAILER_BLOCK = "commit_trailers_py"


def read_marker_ranges(text: str, block: str = TRAILER_BLOCK) -> list:
    """`[(first, last)]`, the 1-based line numbers of each `# >>> <block>` line and the `# <<< <block>`
    line closing it in `text`, both included; a region left open runs to the last line."""
    ranges, start = [], None
    lines = text.split("\n")
    for n, line in enumerate(lines, 1):
        bare = line.strip()
        if start is None and bare.startswith("# >>> " + block):
            start = n
        elif start is not None and bare.startswith("# <<< " + block):
            ranges.append((start, n))
            start = None
    if start is not None:
        ranges.append((start, len(lines)))
    return ranges


def check_trailer_parses(root, rev=None) -> list:
    """Every code line under `root` that spells its own trailer parse, as `<path>:<line>` relative to
    `root`: ONE `git grep -n -z -i -E` for the two patterns, run in `root`, over its tracked files, or
    over the tree of `rev` when given, less `*.test.sh`. A hit inside a reader block's marker region,
    or on a line whose first non-blank characters are `#` or `//`, is cut, each hit's file read once
    at the same revision, or from the working tree. [] where git greps and finds none; Refusal where
    git cannot grep `root` or read a hit's file at `rev`.

    It does not read a parse spelled another way, a key other than `Pass`, or an untracked file."""
    argv = ["grep", "-n", "-z", "-i", "-E"]
    for needle in TRAILER_PARSE_NEEDLES:
        argv += ["-e", needle]
    argv += ([rev] if rev else []) + ["--", ".", ":!*.test.sh"]
    try:
        out = run_git(root, *argv)
    except Refusal as exc:
        # git grep exits 1 for no match; any other failure is git unable to grep, never an empty answer.
        if exc.status == 1 and not exc.out.strip():
            return []
        raise
    hits, texts = [], {}
    for line in out.decode("utf-8", "replace").split("\n"):
        if not line:
            continue
        path, num = line.split("\0")[:2]
        path = path[len(rev) + 1:] if rev else path
        if path not in texts:
            raw = run_git(root, "show", f"{rev}:{path}") if rev else (pathlib.Path(root) / path).read_bytes()
            text = raw.decode("utf-8", "replace").replace("\r\n", "\n")
            texts[path] = (text.split("\n"), read_marker_ranges(text))
        lines, ranges = texts[path]
        n = int(num)
        code = lines[n - 1].lstrip() if n <= len(lines) else ""
        if code.startswith(("#", "//")) or any(a <= n <= b for a, b in ranges):
            continue
        hits.append(f"{path}:{num}")
    return hits


def check_lf_lines(out: bytes, shas: list) -> list:
    """TOOL-dDeclaredLoop-58 S2: the findings of a `tokens` run's bytes `out` against `shas`, the
    commits git lists for the same revisions; [] when clean. Each non-empty line must open with the
    next sha and a space, none missing or extra, before a CR is looked for, so an empty or short
    output is named as such and never passes on nothing. An empty `shas` is a finding of its own.

    It splits on LF alone, so a CR stays on its line and is named by the CR read, not the match."""
    if not shas:
        return ["no commit to compare against: git listed no sha"]
    lines = [line for line in out.split(b"\n") if line]
    if ([line[:40].decode("ascii", "replace") for line in lines] != list(shas)
            or any(line[40:41] != b" " for line in lines)):
        return [f"{len(lines)} sha-led lines read, {len(shas)} expected: "
                f"read {[line[:41].decode('ascii', 'replace') for line in lines]!r}, git lists {list(shas)!r}"]
    return ["a CR reached the output"] if b"\r" in out else []


# ------------------------------------------------------------------------------------- self-test
BASE_EPOCH = 1767225600      # 2026-01-01, after every fixture cutoff
OLD_EPOCH = 959817600        # 2000-06-01, before the fixture cutoff 2001-01-01
SPEC1 = "memory/builds/tFix/spec/2026-01-01-spec-TOOL-tFix-1.md"
SPEC2 = "memory/builds/tFix/spec/2026-01-01-spec-TOOL-tFix-2.md"


def build_fixture(root: pathlib.Path, name: str, commits: list) -> tuple:
    """A scratch repository from ONE `git fast-import`: `(repo, [sha per commit])`.

    Each commit is `{msg, files: {path: text | bytes | None}, date?, parent?, merge?, exec?}`, parents
    named by their 1-based position; a commit's first parent defaults to the one before it. A path
    `exec` lists is written at mode 100755, every other at 100644."""
    repo = root / name
    repo.mkdir()
    run_git(repo, "init", "-q", "--template=")      # no template seeds node state (TOOL-dTrueNorth-32 S7)
    (repo / ".git" / "HEAD").write_bytes(b"ref: refs/heads/main\n")
    out = bytearray()
    for n, c in enumerate(commits, 1):
        when = c.get("date", BASE_EPOCH + n * 60)
        msg = c["msg"].encode("utf-8")
        out += b"commit refs/heads/main\nmark :%d\n" % n
        out += b"author T <t@e> %d +0000\ncommitter T <t@e> %d +0000\n" % (when, when)
        out += b"data %d\n%s\n" % (len(msg), msg)
        parent = c.get("parent", n - 1)
        if parent:
            out += b"from :%d\n" % parent
        for m in c.get("merge", []):
            out += b"merge :%d\n" % m
        for path, text in c.get("files", {}).items():
            if text is None:
                out += b"D %s\n" % path.encode("utf-8")
            else:
                body = text if isinstance(text, bytes) else text.encode("utf-8")
                mode = b"100755" if path in c.get("exec", []) else b"100644"
                out += b"M %s inline %s\ndata %d\n%s\n" % (mode, path.encode("utf-8"), len(body), body)
    marks = repo / ".git" / "fixture-marks"
    run_git(repo, "fast-import", "--quiet", f"--export-marks={marks.as_posix()}", stdin=bytes(out))
    by_mark = dict(line.split(" ", 1) for line in marks.read_text(encoding="utf-8").split("\n") if line)
    return repo, [by_mark[f":{n}"].strip() for n in range(1, len(commits) + 1)]


def set_fixture_conf(repo: pathlib.Path, **keys) -> None:
    """Write the fixture's conf: the defaults, overridden by `keys`."""
    conf = {"MEMORY_ROOT": "memory", "ROUTED_PATHS": "src/", "ROUTED_COMMIT_CUTOFF": "2001-01-01",
            "FAMILIES": "tooling:TOOL", "ROUTED_COMMIT_WAIVED": ""}
    conf.update(keys)
    (repo / ".memory-tree.conf").write_bytes("".join(f'{k}="{v}"\n' for k, v in conf.items()).encode("utf-8"))


def run_selftest() -> int:
    """The arms, each over a scratch repository. Exit 0 all held, 1 any failed."""
    failed = []

    def print_arm(ok: bool, what: str, detail: str = "") -> None:
        print(f"  {'ok  ' if ok else 'FAIL'} — {what}" + ("" if ok else f"\n{detail}"))
        if not ok:
            failed.append(what)

    def run_check(repo, env=None) -> tuple:
        try:
            rc, lines = check_routed_commits(repo, env or {})
        except Refusal as exc:
            return 2, f"{SAY} REFUSED — {exc}"
        return rc, "\n".join(lines)

    root = pathlib.Path(tempfile.mkdtemp(prefix="rc-"))
    # TOOL-dQuietDisk-4 S7: every arm runs the store off, so each keeps the one log pass and its spawn
    # count; the record-store arm alone restores the real resolver.
    real_store = globals()["resolve_store"]
    globals()["resolve_store"] = lambda _repo, leg, _paths: HistoryStore(None, leg, "", "", False)
    try:
        # ---- AC1 AC2 AC3 AC8: one history, graded whole, by range and with waivers
        repo, s = build_fixture(root, "main", [
            {"msg": "init", "files": {"README.md": "x\n"}},
            {"msg": "spec TOOL-tFix-1", "files": {SPEC1: "# TOOL-tFix-1 — one\n"}},
            {"msg": "TOOL-tFix-1: code", "files": {"src/a.txt": "a\n"}},
            {"msg": "TOOL-tFix-2: code with its spec", "files": {SPEC2: "# TOOL-tFix-2 — two\n", "src/b.txt": "b\n"}},
            {"msg": "chore: no id", "files": {"src/c.txt": "c\n"}},
            {"msg": "chore: trailer none\n\nPass: none", "files": {"src/d.txt": "d\n"}},
            {"msg": "chore: trailer names it\n\nPass: TOOL-tFix-1", "files": {"src/e.txt": "e\n"}},
            {"msg": "TOOL-tFix-1: subject, trailer none\n\nPass: none", "files": {"src/f.txt": "f\n"}},
            {"msg": "docs only", "files": {"README.md": "y\n"}},
        ])
        set_fixture_conf(repo)
        rc, out = run_check(repo)
        red = {sha[:8] for sha in s if f"  {sha[:8]} " in out}
        print_arm(rc == 1 and s[3][:8] in red and SPEC2 in out and f"first parent {s[2][:8]}" in out and s[2][:8] not in red,
            "AC1 a spec landed with its code reds naming the commit, the spec and the parent; one landed earlier passes", out)
        print_arm(red == {s[3][:8], s[4][:8], s[5][:8]} and out.count("no unit id") == 2,
            "AC2 no id and `Pass: none` alone red `no unit id`; a trailer id passes; `Pass: none` keeps the subject's id", out)
        beside = "WHOLE beside RANGE"
        print_arm("WHOLE (GATE_PUSH_BASE is unset)" in out and "graded 6" in out and "3 not routed" in out
            and beside not in out,
            "AC3 unset reads WHOLE with its reason and grades the whole history", out)
        rc, out = run_check(repo, {"GATE_PUSH_BASE": s[4]})
        rng = out.split(f"{SAY} FAILED in WHOLE")[0]
        print_arm(rc == 1 and f"RANGE {s[4][:8]}" in rng and f"  {s[5][:8]} " in rng
            and f"  {s[3][:8]} " not in rng and f"  {s[4][:8]} " not in rng,
            "AC3 a resolvable base reads RANGE: a violation after it reds, one before it does not", out)
        set_fixture_conf(repo, ROUTED_COMMIT_WAIVED=s[5])
        rc, out = run_check(repo, {"GATE_PUSH_BASE": s[4]})
        rng = out.split(f"{SAY} FAILED in WHOLE")[0]
        print_arm(rc == 1 and f"  {s[5][:8]} " in rng and "0 waived" in out.split("\n")[0]
            and f"{SAY} FAILED — a commit touching" in rng,
            "AC3 RANGE reads no waiver: a listed pushed commit still reds under the RANGE heading", out)
        rc, out = run_check(repo, {"GATE_PUSH_BASE": "0" * 40})
        print_arm(rc == 1 and "all zeros" in out and f"  {s[3][:8]} " in out and beside not in out,
            "AC3 an all-zeros base reads WHOLE", out)
        rc, out = run_check(repo, {"GATE_PUSH_BASE": "0123456789abcdef0123456789abcdef01234567"})
        print_arm(rc == 1 and "names no commit" in out and f"  {s[3][:8]} " in out and beside not in out,
            "AC3 a base naming no commit widens to WHOLE and never narrows", out)
        set_fixture_conf(repo, ROUTED_COMMIT_WAIVED=" ".join(x[:12] for x in s[3:6]))
        rc, out = run_check(repo)
        print_arm(rc == 0 and "3 waived" in out, "AC8 waived violations in WHOLE mode pass and are counted", out)
        set_fixture_conf(repo, ROUTED_COMMIT_WAIVED=" ".join([x[:12] for x in s[3:6]] + [s[2][:12]]))
        rc, out = run_check(repo)
        print_arm(rc == 1 and f"lists {s[2][:12]}" in out and "stale" in out, "AC8 a waiver naming no violation reds as stale", out)

        # ---- TOOL-aRoutedQuill-10: WHOLE graded beside RANGE at a resolvable base
        repo, s = build_fixture(root, "beside", [
            {"msg": "init", "files": {"README.md": "x\n"}},
            {"msg": "spec TOOL-tFix-1", "files": {SPEC1: "# TOOL-tFix-1 — one\n"}},
            {"msg": "TOOL-tFix-1: local code", "files": {"src/a.txt": "a\n"}},
            {"msg": "remote: no id", "files": {"src/r.txt": "r\n"}, "parent": 2},
            {"msg": "Merge remote", "files": {"src/r.txt": "r\n"}, "parent": 3, "merge": [4]},
        ])
        set_fixture_conf(repo)
        rc, out = run_check(repo, {"GATE_PUSH_BASE": s[3]})
        whole = out.split(f"{SAY} FAILED in WHOLE")[-1]
        print_arm(rc == 1 and out.startswith(f"{SAY}: RANGE {s[3][:8]}..{s[4][:8]} · graded 1 ") and beside in out
            and f"{SAY} FAILED in WHOLE" in out and f"  {s[3][:8]} " in whole
            and f"{SAY} FAILED — a commit touching" not in out,
            "AC1 a remote-side violation merged into HEAD reds in WHOLE beside a green RANGE", out)
        repo, s = build_fixture(root, "linear", [
            {"msg": "init", "files": {"README.md": "x\n"}},
            {"msg": "spec TOOL-tFix-1", "files": {SPEC1: "# TOOL-tFix-1 — one\n"}},
            {"msg": "chore: no id", "files": {"src/x.txt": "x\n"}},
            {"msg": "TOOL-tFix-1: code", "files": {"src/y.txt": "y\n"}},
        ])
        set_fixture_conf(repo)
        rc, out = run_check(repo, {"GATE_PUSH_BASE": s[2]})
        print_arm(rc == 1 and "0 merge(s)" in out.split("\n")[0] and f"  {s[2][:8]} " in out.split(f"{SAY} FAILED in WHOLE")[-1],
            "AC2 a linear range with no merge still grades WHOLE beside it and reds an unwaived sha", out)
        set_fixture_conf(repo, ROUTED_COMMIT_WAIVED=s[2][:12])
        rc, out = run_check(repo, {"GATE_PUSH_BASE": s[2]})
        line2 = (out.split("\n") + [""])[1]
        print_arm(rc == 0 and line2.startswith(f"{SAY}: {beside}") and "1 waived" in line2,
            "AC2 the sha waived, WHOLE beside RANGE passes and counts it", out)
        set_fixture_conf(repo, ROUTED_COMMIT_WAIVED=f"{s[2][:12]} {s[3][:12]}")
        rc, out = run_check(repo, {"GATE_PUSH_BASE": s[2]})
        print_arm(rc == 1 and f"lists {s[3][:12]}" in out and "stale" in out,
            "AC3 a stale waiver reds at a resolvable base as it does in WHOLE", out)

        # ---- AC4 AC9: refusals
        repo, s = build_fixture(root, "refuse", [
            {"msg": "init", "files": {"README.md": "x\n"}},
            {"msg": "spec TOOL-tFix-1", "files": {SPEC1: "# TOOL-tFix-1 — one\n"}},
            {"msg": "TOOL-tFix-1: code", "files": {"src/a.txt": "a\n"}},
        ])
        for keys, needle, what in (
                ({"ROUTED_PATHS": ""}, "ROUTED_PATHS is blank", "ROUTED_PATHS blank"),
                ({"ROUTED_COMMIT_CUTOFF": ""}, "ROUTED_COMMIT_CUTOFF is blank", "the cutoff blank"),
                ({"ROUTED_COMMIT_CUTOFF": "yesterday"}, "'yesterday' is not an ISO date", "a cutoff that is not a date"),
                ({"ROUTED_PATHS": "nothing/"}, "nothing/ names nothing tracked", "an entry naming nothing tracked"),
                ({"ROUTED_PATHS": "../src/"}, "../src/ climbs", "an entry climbing through .."),
                ({"ROUTED_PATHS": "/src/"}, "/src/ is absolute", "an absolute entry"),
                ({"ROUTED_PATHS": "memory/"}, "covers MEMORY_ROOT", "an entry covering MEMORY_ROOT"),
                ({"ROUTED_PATHS": "src/ memory/builds/"}, "memory/builds/ covers MEMORY_ROOT", "an entry under MEMORY_ROOT"),
                ({"FAMILIES": ""}, "the id map is empty: FAMILIES is blank", "AC9 FAMILIES blank"),
                ({"FAMILIES": "tooling:T|X"}, "'T|X' is not letters only", "AC9 a FAMILIES prefix that is not letters")):
            set_fixture_conf(repo, **keys)
            rc, out = run_check(repo)
            print_arm(rc == 2 and needle in out, ("" if what.startswith("AC9") else "AC4 ") + what + " refuses at exit 2", out)
        set_fixture_conf(repo)
        orig = globals()["read_routed_commits"]
        globals()["read_routed_commits"] = lambda *a: orig(*a)[1:]
        try:
            rc, out = run_check(repo)
        finally:
            globals()["read_routed_commits"] = orig
        print_arm(rc == 2 and "parsed 2 commit(s)" in out and "reports 3" in out,
            "AC9 a log stream shorter than rev-list refuses naming both counts", out)
        (repo / ".git" / "shallow").write_bytes(s[0].encode("utf-8") + b"\n")
        rc, out = run_check(repo)
        print_arm(rc == 2 and "fetch-depth: 0" in out, "AC4 a shallow clone refuses naming fetch-depth: 0", out)

        repo, s = build_fixture(root, "deadmap", [
            {"msg": "init", "files": {"README.md": "x\n", "memory/builds/tFix/spec/x.md": "# Not an id\n"}},
            {"msg": "TOOL-tFix-1: code", "files": {"src/a.txt": "a\n"}},
        ])
        set_fixture_conf(repo)
        rc, out = run_check(repo)
        print_arm(rc == 2 and "the id map is empty: 1 spec file(s)" in out, "AC9 spec files defining no id refuse", out)

        # ---- AC5: nothing graded still says what it saw
        repo, s = build_fixture(root, "zero", [
            {"msg": "old", "files": {"src/a.txt": "a\n"}, "date": OLD_EPOCH},
            {"msg": "docs", "files": {"README.md": "x\n"}},
            {"msg": "docs again", "files": {"README.md": "y\n"}},
        ])
        set_fixture_conf(repo)
        rc, out = run_check(repo)
        print_arm(rc == 0 and "graded 0 — the range holds 3 commit(s)" in out and "ROUTED_PATHS src/" in out,
            "AC5 a range with no graded commit prints graded 0, its commit count and ROUTED_PATHS", out)
        # TOOL-dTrueNorth-4 AC12: a conf declaring no design key prints ONE join-off line naming the keys,
        # and the exit is the leg's own; the spawn arm below holds that it reads no history.
        print_arm(rc == 0 and out.count(f"{SAY}: deviation join off — ") == 1
            and "DESIGN_RECORD, DESIGN_BASELINE, DESIGN_VIEW, DESIGN_NODES are blank" in out,
            "TOOL-dTrueNorth-4 AC12 the deviation join is off with the design keys blank, in one line", out)

        # ---- AC6: the spawn count does not grow with the commits
        counts = []
        for n in (3, 30):
            repo, s = build_fixture(root, f"spawn{n}", [{"msg": "spec TOOL-tFix-1", "files": {SPEC1: "# TOOL-tFix-1 — one\n"}}]
                                    + [{"msg": f"TOOL-tFix-1: step {k}", "files": {f"src/{k}.txt": f"{k}\n"}} for k in range(n)])
            set_fixture_conf(repo)
            before = GIT_SPAWNS[0]
            rc, out = run_check(repo)
            counts.append((GIT_SPAWNS[0] - before, rc, f"graded {n}" in out))
            before = GIT_SPAWNS[0]
            rc, out = run_check(repo, {"GATE_PUSH_BASE": s[0]})
            counts.append((GIT_SPAWNS[0] - before, rc, f"graded {n}" in out and beside in out))
        print_arm(counts[0][0] == counts[2][0] and counts[1][0] == counts[3][0] and all(c[1] == 0 and c[2] for c in counts),
            f"AC6 3 and 30 routed commits cost the same git spawns, WHOLE and beside RANGE ({counts})", repr(counts))

        # ---- AC7: exempt, merge, and a move out of ROUTED_PATHS
        repo, s = build_fixture(root, "edges", [
            {"msg": "init", "files": {"README.md": "x\n", "src/keep.txt": "k\n"}, "date": OLD_EPOCH},
            {"msg": "old: no id", "files": {"src/old.txt": "o\n"}, "date": OLD_EPOCH + 60},
            {"msg": "spec TOOL-tFix-1", "files": {SPEC1: "# TOOL-tFix-1 — one\n"}},
            {"msg": "side: docs", "files": {"README.md": "side\n"}},
            {"msg": "TOOL-tFix-1: main step", "files": {"src/m.txt": "m\n"}, "parent": 3},
            {"msg": "Merge side", "files": {"README.md": "side\n"}, "parent": 5, "merge": [4]},
            {"msg": "move it out", "files": {"src/m.txt": None, "docs/m.txt": "m\n"}},
        ])
        set_fixture_conf(repo)
        rc, out = run_check(repo)
        red = {sha[:8] for sha in s if f"  {sha[:8]} " in out}
        print_arm(rc == 1 and red == {s[6][:8]} and "2 exempt" in out and "1 merge(s)" in out,
            "AC7 a pre-cutoff commit is exempt, a merge is counted, a move out of ROUTED_PATHS reds", out)

        # ---- AC11: the lander's mint names the range's unit, with `Pass: none`
        mint = "mint: kit versions onto upstream/main at 1234abcd"
        for name, subject, want in (("mint", f"{mint} for TOOL-tFix-1", 0), ("bare", mint, 1)):
            repo, s = build_fixture(root, name, [
                {"msg": "init", "files": {"README.md": "x\n"}},
                {"msg": "spec TOOL-tFix-1", "files": {SPEC1: "# TOOL-tFix-1 — one\n"}},
                {"msg": "TOOL-tFix-1: code", "files": {"src/a.txt": "a\n"}},
                {"msg": f"{subject}\n\nPass: none", "files": {"src/VERSION": "2\n"}},
            ])
            set_fixture_conf(repo)
            rc, out = run_check(repo, {"GATE_PUSH_BASE": s[1]})
            if want == 0:
                print_arm(rc == 0 and "RANGE" in out, "AC11 a mint naming the range's unit with `Pass: none` passes in RANGE", out)
            else:
                print_arm(rc == 1 and f"  {s[3][:8]} " in out and "no unit id" in out, "AC11 an id-less mint reds `no unit id`", out)
                newest = read_newest_unit(repo, f"{s[1]}..HEAD")
                print_arm(newest == "TOOL-tFix-1", f"AC11 --newest-unit reads past an id-less commit to the unit (got '{newest}')")
        # TOOL-aRoutedQuill-12 AC2: an unspecced id and a merge's id are walked past to a specced unit.
        repo, s = build_fixture(root, "newest", [
            {"msg": "init", "files": {"README.md": "x\n"}},
            {"msg": "spec TOOL-tFix-1", "files": {SPEC1: "# TOOL-tFix-1 — one\n"}},
            {"msg": "TOOL-tFix-1: code", "files": {"src/a.txt": "a\n"}},
            {"msg": "TOOL-tFix-9: unspecced, newest", "files": {"src/b.txt": "b\n"}},
        ])
        set_fixture_conf(repo)
        newest = read_newest_unit(repo, f"{s[1]}..HEAD")
        print_arm(newest == "TOOL-tFix-1", f"AC11 --newest-unit walks past an id no spec defines to a specced unit (got '{newest}')")
        repo, s = build_fixture(root, "newestmerge", [
            {"msg": "init", "files": {"README.md": "x\n"}},
            {"msg": "spec TOOL-tFix-1 and TOOL-tFix-2", "files": {SPEC1: "# TOOL-tFix-1 — one\n", SPEC2: "# TOOL-tFix-2 — two\n"}},
            {"msg": "TOOL-tFix-1: code", "files": {"src/a.txt": "a\n"}},
            {"msg": "side: docs", "files": {"README.md": "side\n"}, "parent": 2},
            {"msg": "Merge TOOL-tFix-2 side", "files": {"README.md": "side\n"}, "parent": 3, "merge": [4]},
        ])
        set_fixture_conf(repo)
        newest = read_newest_unit(repo, f"{s[1]}..HEAD")
        print_arm(newest == "TOOL-tFix-1", f"AC11 --newest-unit skips a newest merge commit's id (got '{newest}')")
        # TOOL-dWitnessedBar-29 AC5: a path walks only the commits touching it, so the newest unit, which
        # never touched it, is passed over for the one that did; with no path the newest is named.
        repo, s = build_fixture(root, "newestpath", [
            {"msg": "init", "files": {"README.md": "x\n"}},
            {"msg": "spec TOOL-tFix-1 and TOOL-tFix-2", "files": {SPEC1: "# TOOL-tFix-1 — one\n", SPEC2: "# TOOL-tFix-2 — two\n"}},
            {"msg": "TOOL-tFix-1: grows the guide", "files": {"src/guide.md": "grown\n"}},
            {"msg": "TOOL-tFix-2: elsewhere, newest", "files": {"src/other.txt": "o\n"}},
        ])
        set_fixture_conf(repo)
        newest = read_newest_unit(repo, "HEAD", "src/guide.md")
        print_arm(newest == "TOOL-tFix-1", f"dWB29 AC5 --newest-unit with a path names the unit that touched it (got '{newest}')")
        newest = read_newest_unit(repo, "HEAD")
        print_arm(newest == "TOOL-tFix-2", f"dWB29 AC5 --newest-unit with no path names the newest unit (got '{newest}')")

        # ---- TOOL-aWrappedRoster-1 AC1: the manifest parser reads both shapes an adopter commits, a
        # bare list of rows and an object holding them under `legs`, and still refuses an object without.
        def read_shape(text):
            try:
                return parse_leg_names(text)
            except ValueError:
                return None

        print_arm(read_shape('[{"name": "leg one"}]') == {"leg one"}
            and read_shape('{"_doc": "x", "legs": [{"name": "leg one"}]}') == {"leg one"}
            and read_shape('{"_doc": "x"}') is None and read_shape('"legs"') is None,
            "TOOL-aWrappedRoster-1 AC1 parse_leg_names reads a bare row list and an object's `legs` list, "
            "and refuses an object with no `legs` list and a scalar")

        # ---- TOOL-aNimbleMend-8 AC4 AC5 AC6: the red-fix lane. Four commits, graded WHOLE and RANGE with
        # the lane key stubbed on and then off, then a trailer-free twin for the spawn count. Against a
        # grader that reads no `Red-fix:` trailer every arm but the last two reads RED.
        # TOOL-aNimbleMend-10: the two fix commits CHANGE a file the pre-cutoff init holds, since a fix
        # commit adding a path is over limit L4, and these arms grade the lane's admission alone.
        lane_files = [{"README.md": "x\n", "legs.json": '[{"name": "leg one"}]\n', "src/a.txt": "0\n", "src/b.txt": "0\n"},
                      {"src/a.txt": "a\n"}, {"src/b.txt": "b\n"}, {"src/c.txt": "c\n"}]
        lane_msgs = ["init", "fix: clear leg one\n\nRed-fix: leg one\nPass: none", "fix: names no leg\n\nRed-fix: leg nine",
                     "chore: no id"]
        lane_dates = [{"date": OLD_EPOCH}, {}, {}, {}]
        repo, s = build_fixture(root, "lane", [{"msg": m, "files": f, **d} for m, f, d in zip(lane_msgs, lane_files, lane_dates)])
        free, _s = build_fixture(root, "lanefree", [{"msg": m.split("\n")[0], "files": f, **d}
                                                    for m, f, d in zip(lane_msgs, lane_files, lane_dates)])
        set_fixture_conf(repo, LEG_MANIFEST="legs.json")
        set_fixture_conf(free, LEG_MANIFEST="legs.json")
        c2, c3, c4 = (f"  {x[:8]} " for x in s[1:])
        asked, spawns = [], {}
        orig_lane = globals()["read_lane_state"]
        try:
            for on in (True, False):
                globals()["read_lane_state"] = lambda _repo, on=on: (asked.append(on) or on, "")
                before = GIT_SPAWNS[0]
                rc_w, whole = run_check(repo)
                spawns["lane"] = GIT_SPAWNS[0] - before
                rc_r, both = run_check(repo, {"GATE_PUSH_BASE": s[0]})
                rng, beside_line = both.split("\n")[0], next((ln for ln in both.split("\n") if beside in ln), "")
                listed = both.split(f"{SAY}: {beside}")[0]
                if on:
                    print_arm(rc_w == 1 and c2 not in whole and "1 red-fix" in whole.split("\n")[0]
                        and any(c3 in ln and "leg nine" in ln and "legs.json" in ln for ln in whole.split("\n"))
                        and any(c4 in ln and ln.endswith("names no unit") for ln in whole.split("\n")),
                        "TOOL-aNimbleMend-8 AC4 WHOLE admits a commit whose `Red-fix:` value is a leg at its own "
                        "commit and counts it, reds a value that is no leg naming it and the manifest, and "
                        "still reds a trailer-free commit `names no unit`", whole)
                    print_arm(rc_r == 1 and c2 not in both and "1 red-fix" in rng and "1 red-fix" in beside_line
                        and any(c3 in ln and "leg nine" in ln and "legs.json" in ln for ln in listed.split("\n"))
                        and any(c4 in ln and ln.endswith("names no unit") for ln in listed.split("\n")),
                        "TOOL-aNimbleMend-8 AC4 RANGE with the key on does the same, and both summary lines "
                        "hold `1 red-fix`", both)
                else:
                    print_arm(rc_r == 1 and "red-fix" not in rng and "1 red-fix" in beside_line
                        and all(any(c in ln and ln.endswith("no unit id — names no unit") for ln in listed.split("\n"))
                                for c in (c2, c3, c4)),
                        "TOOL-aNimbleMend-8 AC5 the key off, RANGE reds all three `no unit id — names no "
                        "unit`, and the WHOLE half beside it still admits the lane commit", both)
                    print_arm(rc_w == 1 and c2 not in whole and "1 red-fix" in whole.split("\n")[0],
                        "TOOL-aNimbleMend-8 AC5 the key off reds no lane commit graded WHOLE", whole)
            print_arm(asked == [True, False],
                f"TOOL-aNimbleMend-8 S7 the lane key is read once per RANGE grading and never for WHOLE alone (asked {asked})")
            set_fixture_conf(repo)
            rc, out = run_check(repo)
            print_arm(rc == 1 and any(c2 in ln and "cannot be checked" in ln and "LEG_MANIFEST is blank" in ln for ln in out.split("\n")),
                "TOOL-aNimbleMend-8 S6 a blank LEG_MANIFEST reds a lane commit saying its trailer cannot be checked", out)
            set_fixture_conf(repo, LEG_MANIFEST="absent.json")
            rc, out = run_check(repo)
            print_arm(rc == 1 and any(c2 in ln and "cannot be checked" in ln and "absent.json" in ln for ln in out.split("\n")),
                "TOOL-aNimbleMend-8 S6 a commit holding no manifest reds saying its trailer cannot be checked", out)

            def check_lane_unread(_repo):
                raise AssertionError("the lane key was read for a trailer-free history")

            globals()["read_lane_state"] = check_lane_unread
            before = GIT_SPAWNS[0]
            try:
                rc, out = run_check(free)
                rc2, out2 = run_check(free, {"GATE_PUSH_BASE": _s[0]})
            except AssertionError as exc:
                rc, out, rc2, out2 = -1, str(exc), -1, ""
            spawns["free"] = GIT_SPAWNS[0] - before
        finally:
            globals()["read_lane_state"] = orig_lane
        before = GIT_SPAWNS[0]
        run_check(free)
        spawns["free whole"] = GIT_SPAWNS[0] - before
        print_arm(rc == 1 and rc2 == 1 and " red-fix ·" not in out + out2 and spawns["lane"] == spawns["free whole"] + 2
            and out.count("red-fix limits · graded 0") == 1 and out2.count("red-fix limits · graded 0") == 2,
            "TOOL-aNimbleMend-8 AC5 a trailer-free history reads no lane key, prints no red-fix count and costs "
            "two git spawns fewer than its lane twin, the batched manifest read and the limits read; "
            f"TOOL-aNimbleMend-10 AC6 it prints `red-fix limits · graded 0` once per population ({spawns})", out + "\n" + out2)

        # ---- TOOL-aNimbleMend-15 S9: the REAL `read_lane_state`, reached through a stub of the one
        # policy read it makes. Every arm above replaces the function itself, so its three other
        # outcomes ran nowhere: a refused read and an unknown value close the lane under the reader's
        # line, and no policy kit opens it under the NOTE. Staged by stubbing `read_lane_state` in
        # place of the reader, which leaves each `why` line unprinted.
        def check_reader_refused(_key, _root):
            raise ValueError("policy: refused · the fixture's reader said no")

        def check_reader_absent(_key, _root):
            raise LookupError("no policy kit in this fixture")

        set_fixture_conf(repo, LEG_MANIFEST="legs.json")
        orig_reader = globals()["read_policy_value"]
        try:
            for stub, why in ((check_reader_refused, "policy: refused · the fixture's reader said no"),
                              (lambda _key, _root: "maybe",
                               "bar.inline-red-fixes reads maybe, neither on nor off, so the red-fix lane is closed")):
                globals()["read_policy_value"] = stub
                rc, both = run_check(repo, {"GATE_PUSH_BASE": s[0]})
                listed = both.split(f"{SAY}: {beside}")[0].split("\n")
                print_arm(rc == 1 and "red-fix" not in listed[0] and f"{SAY}: {why}" in listed
                    and any(c2 in ln and ln.endswith("no unit id — names no unit") for ln in listed),
                    f"TOOL-aNimbleMend-15 S9 through the real read_lane_state, a reader answering `{why}` closes the "
                    "lane: RANGE lists the fix commit `names no unit` under that line", both)
            globals()["read_policy_value"] = check_reader_absent
            rc, both = run_check(repo, {"GATE_PUSH_BASE": s[0]})
            listed = both.split(f"{SAY}: {beside}")[0].split("\n")
            print_arm("1 red-fix" in listed[0] and not any(c2 in ln for ln in listed)
                and f"{SAY}: NOTE — no policy kit resolves beside this kit, so bar.inline-red-fixes reads on" in listed,
                "TOOL-aNimbleMend-15 S9 through the real read_lane_state, no policy kit opens the lane: RANGE "
                "counts `1 red-fix` under the NOTE line", both)
        finally:
            globals()["read_policy_value"] = orig_reader

        # ---- TOOL-aNimbleMend-15 S7: a blank LEG_MANIFEST falls back to the manifest beside the
        # run-gates kit found beside this one. The fixture holds such a kit on disk and the manifest
        # in its commits, and this module's own location is stubbed to sit beside it. Staged by
        # taking the fallback out of `resolve_leg_manifest`: the commit reds `LEG_MANIFEST is blank`,
        # as the arm above shows it does where the kit beside this module is outside the repository.
        home, anchor = "run-gates", "run-gates.sh"      # the resolver's own two arguments, as the function passes them
        repo, s = build_fixture(root, "lanebeside", [
            {"msg": "init", "date": OLD_EPOCH,
             "files": {"README.md": "x\n", "kits/gate-legs.json": '[{"name": "leg one"}]\n', "src/a.txt": "0\n"}},
            {"msg": "fix: clear leg one\n\nRed-fix: leg one\nPass: none", "files": {"src/a.txt": "a\n"}}])
        set_fixture_conf(repo)
        kits = repo / "kits"
        (kits / home).mkdir(parents=True)
        (kits / home / anchor).write_bytes(b"#!/usr/bin/env bash\n")
        const = "KIT"       # the module constant's name, held apart: the hygiene suite reads a quoted
        orig_kit = globals()[const]      # capital name in a subscript as a conf key, and this is none
        try:
            globals()[const] = kits / orig_kit.name
            found = resolve_leg_manifest(repo, {})
            rc, out = run_check(repo)
        finally:
            globals()[const] = orig_kit
        print_arm(found == "kits/gate-legs.json" and rc == 0 and "1 red-fix" in out.split("\n")[0]
            and "LEG_MANIFEST is blank" not in out,
            f"TOOL-aNimbleMend-15 S7 a blank LEG_MANIFEST beside a run-gates kit reads that kit's manifest "
            f"(got '{found}') and admits the lane commit", out)
        policy_get = "policy" + ".py"       # spelled apart: AC6 counts that name in this file as zero
        import build_records  # noqa: E402  a sibling, for the one policy read's second caller
        import inspect
        import tree_lib  # noqa: E402
        print_arm(callable(getattr(tree_lib, "read_policy_value", None))
            and "read_policy_value" in inspect.getsource(build_records.read_override_value)
            and policy_get not in pathlib.Path(__file__).read_text(encoding="utf-8"),
            "TOOL-aNimbleMend-8 AC6 the policy read lives once, in tree_lib, the override door calls it, and "
            "this file spells no policy reader of its own")

        # ---- TOOL-aNimbleMend-10 AC1-AC5 AC7: the inline lane's limits. One history, c1 before the cutoff
        # and trailer-free, c2 inside every limit, c3 to c7 one commit per limit; each fix names the unit,
        # so the routing half is green and every red below is the limits pass's. Graded through the verb,
        # then by the leg with the waiver blank, full and one sha too long. Against a grader with no
        # limits pass every arm here reads RED.
        def run_limits_verb(repo, rev: str) -> tuple:
            here, said = os.getcwd(), io.StringIO()
            os.chdir(repo)
            try:
                with contextlib.redirect_stdout(said):
                    rc = main(["routed_commits.py", "--red-fix-limits", rev])
            finally:
                os.chdir(here)
            return rc, said.getvalue()

        fix_msg = "TOOL-tFix-1: fix {}\n\nRed-fix: leg one"
        rows = [f"a{k}\n" for k in range(40)]
        big = ["A0\n"] + [f"B{k}\n" for k in range(1, 31)] + rows[31:] + ["c2\n", "c3\n", "c4\n"]
        policy_toml = ".governance/policy.toml"
        repo, s = build_fixture(root, "limits", [
            {"msg": "init", "date": OLD_EPOCH, "files": {
                "src/a.txt": "".join(rows), "src/b.txt": "b\n", "src/c.txt": "c\n", "src/d.txt": "d\n",
                SPEC1: "# TOOL-tFix-1 — one\n", policy_toml: "x = 1\n"}},
            {"msg": fix_msg.format("c2"), "files": {"src/a.txt": "".join(["A0\n"] + rows[1:] + ["c2\n"])}},
            {"msg": fix_msg.format("c3"), "files": {"src/a.txt": "".join(["A0\n"] + rows[1:] + ["c2\n", "c3\n"]),
                                                    "src/b.txt": "b\nc3\n", "src/c.txt": "c\nc3\n", "src/d.txt": "d\nc3\n"}},
            {"msg": fix_msg.format("c4"), "files": {"src/a.txt": "".join(big)}},
            {"msg": fix_msg.format("c5"), "files": {"src/a.txt": "".join(big + ["c5\n"]), policy_toml: "x = 1\ny = 2\n"}},
            {"msg": fix_msg.format("c6"), "files": {"src/a.txt": "".join(big + ["c5\n", "c6\n"]),
                                                    SPEC1: "# TOOL-tFix-1 — one\nrevised\n"}},
            {"msg": fix_msg.format("c7"), "files": {"src/e.txt": "e\n"}},
        ])
        set_fixture_conf(repo)
        got = [run_limits_verb(repo, sha) for sha in s]
        bound = f"; the bound is {RED_FIX_MAX_PATHS} and {RED_FIX_MAX_LINES}"
        print_arm(got[1][0] == 0 and "is inside all four" in got[1][1]
            and got[2][0] == 1 and f"L1 size: 4 path(s), 4 line(s){bound}" in got[2][1]
            and got[3][0] == 1 and f"L1 size: 1 path(s), 61 line(s){bound}" in got[3][1]
            and "L1" not in got[4][1] + got[5][1] + got[6][1],
            "TOOL-aNimbleMend-10 AC1 the verb exits 0 for a 3-line fix, and 1 naming L1, both counts and the bound "
            "for four routed paths and for 30 lines deleted with 31 added; a path outside ROUTED_PATHS counts "
            "toward neither", "\n".join(out for _rc, out in got))
        orig_guarded = globals()["read_guarded_paths"]
        try:
            globals()["read_guarded_paths"] = lambda: None
            bare = run_limits_verb(repo, s[4])
            globals()["read_guarded_paths"] = lambda: [".governance/other.toml"]
            other = run_limits_verb(repo, s[4])
        finally:
            globals()["read_guarded_paths"] = orig_guarded
        print_arm(got[4][0] == 1 and f"L2 guarded policy file: {policy_toml}" in got[4][1]
            and bare[0] == 1 and f"L2 guarded policy file: {policy_toml}" in bare[1] and other[0] == 0,
            "TOOL-aNimbleMend-10 AC2 the verb exits 1 naming L2 and the guarded path, still does with no policy "
            "kit resolving, and reads a resolved list by its lines, not the directory", got[4][1] + bare[1] + other[1])
        print_arm(got[5][0] == 1 and f"L3 spec edit: {SPEC1}" in got[5][1] and "L2" not in got[5][1],
            "TOOL-aNimbleMend-10 AC3 the verb exits 1 naming L3 and the spec's path", got[5][1])
        print_arm(got[6][0] == 1 and "L4 new surface: src/e.txt" in got[6][1] and "L4" not in got[2][1] + got[3][1],
            "TOOL-aNimbleMend-10 AC4 the verb exits 1 naming L4 and the added path, and a changed path is no addition",
            got[6][1])
        none = run_limits_verb(repo, "0123456789abcdef0123456789abcdef01234567")
        print_arm(none[0] == 2 and f"{SAY} REFUSED — " in none[1] and "names no commit in this clone" in none[1]
            and got[0][0] == 2 and f"{SAY} REFUSED — commit {s[0][:8]} carries no `{RED_FIX_TRAILER}:` trailer" in got[0][1],
            "TOOL-aNimbleMend-10 AC7 the verb refuses at exit 2 a rev naming no commit and a commit carrying no "
            "trailer, saying which", none[1] + got[0][1])
        limits_head = f"{SAY} FAILED — a Red-fix commit is outside the inline lane's limits:"
        rc, out = run_check(repo)
        under = out.split(limits_head)[-1]
        print_arm(rc == 1 and out.count(limits_head) == 1 and all(f"  {x[:8]} " in under for x in s[2:])
            and f"  {s[1][:8]} " not in out and "red-fix limits · graded 6 · bound 3 path(s), 60 line(s) · 0 waived" in out
            and f"{SAY} FAILED — a commit touching" not in out,
            "TOOL-aNimbleMend-10 AC5 the leg exits 1 listing c3 to c7 under the limits header and not c2, the "
            "routing half green", out)
        set_fixture_conf(repo, ROUTED_COMMIT_WAIVED=" ".join(x[:12] for x in s[2:]))
        rc, out = run_check(repo)
        print_arm(rc == 0 and "red-fix limits · graded 6 · bound 3 path(s), 60 line(s) · 5 waived" in out
            and limits_head not in out and "stale" not in out,
            "TOOL-aNimbleMend-10 AC5 the five shas waived, the leg exits 0, counts them, and reads none as stale", out)
        rc, out = run_check(repo, {"GATE_PUSH_BASE": s[0]})
        print_arm(rc == 1 and out.count(limits_head) == 1 and out.count(f"  {s[2][:8]} ") == 1
            and "· 0 waived\n" in out + "\n" and "· 5 waived" in out,
            "TOOL-aNimbleMend-10 S6 the RANGE half reads no waiver: the waived commits still red there, listed once", out)
        set_fixture_conf(repo, ROUTED_COMMIT_WAIVED=" ".join(x[:12] for x in s[1:]))
        rc, out = run_check(repo)
        print_arm(rc == 1 and f"lists {s[1][:12]}" in out and out.count("stale") == 1,
            "TOOL-aNimbleMend-10 AC5 the sha of a fix inside every limit added, the leg reds it alone as stale", out)
        sixty = "".join(f"n{k}\n" for k in range(20))
        repo, s = build_fixture(root, "limit60", [
            {"msg": "init", "date": OLD_EPOCH, "files": {"src/a.txt": "a\n", "src/b.txt": "b\n", "src/c.txt": "c\n",
                                                         SPEC1: "# TOOL-tFix-1 — one\n"}},
            {"msg": fix_msg.format("at the bound"), "files": {"src/a.txt": "a\n" + sixty, "src/b.txt": "b\n" + sixty,
                                                              "src/c.txt": "c\n" + sixty, "README.md": "x\n"}},
        ])
        set_fixture_conf(repo)
        rc, out = run_limits_verb(repo, s[1])
        print_arm(rc == 0 and "is inside all four" in out,
            "TOOL-aNimbleMend-10 AC1 three routed paths and 60 changed lines are at the bound and not over it, a "
            "fourth path outside ROUTED_PATHS beside them", out)

        # ---- TOOL-aTemperedLane-1 AC2-AC7: the L3 exemption. Each r commit is one child of one pre-cutoff
        # commit holding two specs. r1 is the one exempt change; every other stands on one test of S1.
        head, rows, tail = "# TOOL-tFix-{} — spec\n\nintro\n\n", "\n| row 0 |\n\n", "\n## 1. Goal\n\nbody\n"
        more = rows + "| row 1 |\n"
        m_open, m_close = SPEC_RECORDS_OPEN + "\n", SPEC_RECORDS_CLOSE + "\n"
        one, two = head.format(1), head.format(2)
        index = "\n<!-- gen:build-index -->\nunits\n<!-- /gen:build-index -->\n"
        spec_one = one + m_open + rows + m_close + tail
        spec_two = two + m_open + rows + m_close + tail + index
        grown = one + m_open + more + m_close + tail
        moved_to = SPEC1.replace("tFix-1.md", "tFix-9.md")
        cases = [
            ({"files": {SPEC1: grown, "src/a.txt": "a\nr1\n"}}, None),
            ({"files": {SPEC1: grown.replace("body", "edited")}}, SPEC1),
            ({"files": {SPEC1: grown.replace("intro", "edited")}}, SPEC1),
            ({"files": {SPEC1: one.replace("\n", "\r\n") + m_open + rows + m_close + tail.replace("\n", "\r\n")}}, SPEC1),
            ({"files": {SPEC1: one + tail + m_open + rows + m_close}}, SPEC1),
            ({"files": {SPEC1: one + tail}}, SPEC1),
            ({"files": {SPEC1: one + m_open + rows + m_close + m_open + rows + m_close + tail}}, SPEC1),
            ({"files": {SPEC1: spec_one.replace(m_close, SPEC_RECORDS_CLOSE + " \n")}}, SPEC1),
            ({"files": {SPEC1: spec_one.replace(m_open, SPEC_RECORDS_OPEN + "\r\n")
                        .replace(m_close, SPEC_RECORDS_CLOSE + "\r\n")}}, SPEC1),
            ({"files": {moved_to: spec_one}}, moved_to),
            ({"files": {SPEC1: None}}, SPEC1),
            ({"files": {SPEC1: None, moved_to: spec_one}}, f"{SPEC1}, {moved_to}"),
            ({"files": {SPEC1: grown}, "exec": [SPEC1]}, SPEC1),
            ({"files": {SPEC1: grown, SPEC2: spec_two.replace("body", "edited")}}, SPEC2),
            ({"files": {SPEC2: spec_two.replace("units", "edited")}}, SPEC2),
        ]
        repo, s = build_fixture(root, "region", [
            {"msg": "init", "date": OLD_EPOCH, "files": {"src/a.txt": "a\n", SPEC1: spec_one, SPEC2: spec_two}},
            *({"msg": fix_msg.format(f"r{n}"), "parent": 1, **c} for n, (c, _named) in enumerate(cases, 1))])
        set_fixture_conf(repo)
        got = [run_limits_verb(repo, sha) for sha in s[1:]]
        wrong = [f"r{n}: {rc} {out}" for n, ((rc, out), (_c, named)) in enumerate(zip(got, cases), 1)
                 if (rc, "L3" in out) != ((0, False) if named is None else (1, True))
                 or (named and f"L3 spec edit: {named}\n" not in out)]
        print_arm(len(got) == 15 and not [w for w in wrong if w.startswith("r1:")],
            "TOOL-aTemperedLane-1 AC2 the verb exits 0 for a row added inside the records region", "".join(wrong))
        for ac, names, what in (
                ("AC3", (2, 3, 4, 15), "an edit outside the region, a line ending's and another generated region's included"),
                ("AC4", (5, 6, 7, 8, 9), "a marker pair moved, removed, doubled or altered"),
                ("AC5", (10, 11, 12, 13), "a spec added, deleted, renamed or given another mode"),
                ("AC6", (14,), "the edited spec alone where a second one holds only a row")):
            print_arm(not [w for w in wrong if w.startswith(tuple(f"r{n}:" for n in names))],
                f"TOOL-aTemperedLane-1 {ac} the verb exits 1 naming L3 and exactly the path for {what}", "".join(wrong))
        rooted, r = build_fixture(root, "regionroot", [
            {"msg": fix_msg.format("root"), "files": {"src/a.txt": "a\n", SPEC1: spec_one}}])
        set_fixture_conf(rooted)
        rc, out = run_limits_verb(rooted, r[0])
        print_arm(rc == 1 and f"L3 spec edit: {SPEC1}\n" in out,
            "TOOL-aTemperedLane-1 AC5 a parentless fix commit that adds a spec is an L3 finding", out)
        cost = []
        for shas in ([], s[11:14], s[1:2], s[1:]):
            before = GIT_SPAWNS[0]
            check_red_fix_limits(repo, [{"sha": sha} for sha in shas], ["src/"], "memory", [[]])
            cost.append(GIT_SPAWNS[0] - before)
        print_arm(cost == [0, 1, 2, 2],
            f"TOOL-aTemperedLane-1 AC7 the limits cost 0, 1, 2 and 2 git calls over no fix commit, commits that "
            f"plainly modify no spec, r1, and r1 to r15 ({cost})")

        # ---- TOOL-aTemperedLane-2 AC2-AC8: L2 reads the first parent's list. One line of history beside a
        # policy kit inside the fixture, this module's location stubbed as the `lanebeside` arm stubs it.
        # The disk copy of the list names src/a.txt alone, so every verdict says which list was read.
        home, anchor = "policy", "guarded-paths.txt"
        list_path, agent = f"kits/{home}/{anchor}", ".claude/agents/gov-x.md"
        long_list, short_list = f"# a note\nsrc/b.txt\n\n{agent}\n", f"{agent}\n"
        repo, s = build_fixture(root, "parentlist", [
            {"msg": "init", "date": OLD_EPOCH, "files": {"src/a.txt": "a\n", "src/b.txt": "b\n", agent: "x\n",
                                                         policy_toml: "x = 1\n", SPEC1: "# TOOL-tFix-1 — one\n"}},
            {"msg": fix_msg.format("g2"), "files": {"src/a.txt": "a\ng2\n"}},
            {"msg": "chore: the list", "files": {list_path: long_list}},
            {"msg": fix_msg.format("g4"), "files": {"src/a.txt": "a\ng4\n"}},
            {"msg": fix_msg.format("g5"), "files": {"src/b.txt": "b\ng5\n"}},
            {"msg": fix_msg.format("g6"), "files": {agent: "x\nby hand\n"}},
            {"msg": fix_msg.format("g7"), "files": {list_path: short_list, "src/b.txt": "b\ng7\n"}},
            {"msg": fix_msg.format("g8"), "files": {"src/b.txt": "b\ng8\n"}},
            {"msg": fix_msg.format("g9"), "files": {list_path: short_list + "src/a.txt\n", "src/a.txt": "a\ng9\n"}},
            {"msg": fix_msg.format("g10"), "files": {policy_toml: "x = 2\n"}},
        ])
        rooted, r = build_fixture(root, "parentroot", [
            {"msg": fix_msg.format("root"), "files": {"src/a.txt": "a\n", SPEC1: "# TOOL-tFix-1 — one\n"}},
            *({"msg": fix_msg.format(n), "files": {"src/a.txt": f"a\n{n}\n"}} for n in range(30))])
        # TOOL-aTemperedLane-3: a list that is not UTF-8, a directory at its path, and the list deleted by
        # the fix commit itself; then a trailered merge whose two parents hold different lists.
        started = {"msg": "init", "date": OLD_EPOCH, "files": {"src/a.txt": "a\n", "src/b.txt": "b\n",
                                                               SPEC1: "# TOOL-tFix-1 — one\n"}}
        odd, h = build_fixture(root, "parentodd", [
            started,
            {"msg": "chore: the list, not UTF-8", "files": {list_path: b"src/b.txt\n\xff\n"}},
            {"msg": fix_msg.format("h3"), "files": {"src/a.txt": "a\nh3\n"}},
            {"msg": "chore: a directory there", "files": {list_path: None, f"{list_path}/x": "x\n"}},
            {"msg": fix_msg.format("h5"), "files": {"src/a.txt": "a\nh5\n"}},
            {"msg": "chore: the list again", "files": {f"{list_path}/x": None, list_path: "src/b.txt\n"}},
            {"msg": fix_msg.format("h7"), "files": {list_path: None, "src/b.txt": "b\nh7\n"}},
        ])
        joined, m = build_fixture(root, "parentmerge", [
            started,
            {"msg": "side: the list", "files": {list_path: "src/a.txt\n"}},
            {"msg": "chore: the list", "files": {list_path: "src/b.txt\n"}, "parent": 1},
            {"msg": fix_msg.format("m4"), "files": {"src/b.txt": "b\nm4\n"}, "parent": 3, "merge": [2]},
        ])
        for at in (repo, rooted, odd, joined):
            set_fixture_conf(at)
            (at / list_path).parent.mkdir(parents=True)
            (at / list_path).write_bytes(b"src/a.txt\n")
        try:
            globals()[const] = repo / "kits" / orig_kit.name
            got = dict(enumerate((run_limits_verb(repo, sha) for sha in s), 1))
            whole = run_check(repo)
            # AC7: the leg reads newest first, so g2's absent answer is its last and shifts nothing after
            # it. Oldest first it is the first, and an answer paired with its commit by position shows.
            first_up = [c for c in reversed(read_routed_commits(repo, ["HEAD"])) if c["red_fix"]]
            oldest = check_red_fix_limits(repo, first_up, ["src/"], "memory", [])
            # AC8: g5's parent list replaced in this clone by a blob with no lines.
            listed = run_git(repo, "rev-parse", f"{s[3]}:{list_path}").decode("ascii").strip()
            blank = run_git(repo, "hash-object", "-w", "--stdin", stdin=b"# none\n").decode("ascii").strip()
            run_git(repo, "replace", listed, blank)
            swapped = run_limits_verb(repo, s[4])
            (repo / list_path).unlink()
            bare = run_limits_verb(repo, s[9])
            globals()[const] = rooted / "kits" / orig_kit.name
            parentless = run_limits_verb(rooted, r[0])
            population, cost = read_routed_commits(rooted, ["HEAD"]), []
            for inside, fixes in ((True, []), (True, population[-1:]), (True, population[:1]), (True, population[:30]),
                                  (False, population[:30])):
                globals()[const] = rooted / "kits" / orig_kit.name if inside else orig_kit
                before = GIT_SPAWNS[0]
                check_red_fix_limits(rooted, fixes, ["src/"], "memory", [])
                cost.append(GIT_SPAWNS[0] - before)
            globals()[const] = odd / "kits" / orig_kit.name
            torn, dirred, deleted = (run_limits_verb(odd, h[n - 1]) for n in (3, 5, 7))
            (odd / list_path).unlink()
            unlisted = run_limits_verb(odd, h[6])
            globals()[const] = joined / "kits" / orig_kit.name
            merged = run_limits_verb(joined, m[3])
        finally:
            globals()[const] = orig_kit
        l2 ="L2 guarded policy file: {}\n".format
        detail = "".join(f"g{n}: {rc} {out}" for n, (rc, out) in got.items())
        print_arm(all(got[n][0] == 1 and l2(p) in got[n][1] for n, p in ((5, "src/b.txt"), (6, agent))),
            "TOOL-aTemperedLane-2 AC2 the verb exits 1 naming L2 and the path the first parent's list names and the "
            "working list does not, a rendered agent file edited by hand included", detail)
        print_arm(all(got[n][0] == 0 for n in (4, 8, 9)),
            "TOOL-aTemperedLane-2 AC3 the verb exits 0 where only the working list names the path, where an earlier "
            "commit took it off the list, and where the commit itself adds it", detail)
        print_arm(got[7][0] == 1 and l2("src/b.txt") in got[7][1],
            "TOOL-aTemperedLane-2 AC4 the verb exits 1 naming L2 and the path whose line the commit removed", detail)
        print_arm(got[2][0] == 1 and l2("src/a.txt") in got[2][1]
            and parentless[0] == 1 and l2("src/a.txt") in parentless[1],
            "TOOL-aTemperedLane-2 AC5 a parent with no list, and no parent, are graded by the working tree's list",
            got[2][1] + parentless[1])
        print_arm(got[10][0] == 0 and bare[0] == 1 and l2(policy_toml) in bare[1],
            "TOOL-aTemperedLane-2 AC6 the verb exits 0 for the policy file while the list resolves, and 1 naming L2 "
            "and that file once it does not", got[10][1] + bare[1])
        red = {sha[:8] for sha in s if any(f"  {sha[:8]} " in ln and "L2 " in ln for ln in whole[1].split("\n"))}
        early = {sha[:8] for sha, found in oldest.items() if any(f.startswith("L2 ") for f in found)}
        print_arm(whole[0] == 1 and len(first_up) == 8 and red == early == {s[n - 1][:8] for n in (2, 5, 6, 7)},
            "TOOL-aTemperedLane-2 AC7 the history graded whole, newest first and oldest first, names L2 for g2, g5, "
            "g6 and g7 alone", f"{whole[1]}\n{early}")
        print_arm(len(population) == 31 and cost == [0, 1, 2, 2, 1],
            f"TOOL-aTemperedLane-2 AC7 the limits cost 0, 1, 2, 2 and 1 git calls over no fix commit, a parentless "
            f"one, one, 30, and 30 with the list outside the repository ({cost})")
        print_arm(listed != blank and swapped[0] == 1 and l2("src/b.txt") in swapped[1],
            "TOOL-aTemperedLane-2 AC8 a replace ref over the parent's list blob is not read", swapped[1])

        # ---- TOOL-aTemperedLane-3 AC3-AC6, over the two fixtures graded above.
        print_arm(deleted[0] == 1 and l2("src/b.txt") in deleted[1] and unlisted[0] == 0 and "L2" not in unlisted[1],
            "TOOL-aTemperedLane-3 AC3 a fix commit that deletes the list is graded by its parent's while the working "
            "tree holds one, and by the .governance/ prefix alone once it holds none", deleted[1] + unlisted[1])
        for ac, (rc, out), what in (("AC4", torn, "a first parent's list that is not UTF-8"),
                                    ("AC5", dirred, "a directory at the first parent's list path")):
            print_arm(rc == 1 and l2("src/a.txt") in out,
                f"TOOL-aTemperedLane-3 {ac} {what} leaves the working tree's list to grade", out)
        print_arm(merged[0] == 1 and l2("src/b.txt") in merged[1],
            "TOOL-aTemperedLane-3 AC6 a merge is graded by its first parent's list and not the side lineage's", merged[1])

        # ---- TOOL-aTemperedLane-3 AC7: `read_blob_batch` over a stubbed stream cut before a header, one cut
        # inside a body, and one whose tree body holds an LF before the blob asked for next.
        run_name, answers = "run_git", []
        real_git = globals()[run_name]
        for stream in (b"n1 blob 2\nok\n", b"n1 blob 2\nok\nn2 blob 3\nxy", b"n1 tree 3\nx\ny\nn2 blob 2\nok\n"):
            globals()[run_name] = lambda *_a, stream=stream, **_k: stream
            try:
                answers.append(read_blob_batch(root, ["n1", "n2"]))
            except Refusal as exc:
                answers.append(str(exc))
            finally:
                globals()[run_name] = real_git
        print_arm(answers == ["`git cat-file --batch` ended before it answered n2",
                              "`git cat-file --batch` ended inside n2", {"n1": None, "n2": b"ok"}],
            "TOOL-aTemperedLane-3 AC7 a stream cut before a header and one cut inside a body are refused, and a body "
            "that is not a blob is skipped whole", repr(answers))

        # ---- TOOL-dTrueNorth-4 AC1-AC7 AC10 AC13: the deviation join's fixture over every plant, each
        # plant's failing case staged by the plant itself, and the record-late plant through this host.
        # TOOL-dTrueNorth-12 AC1 AC3 AC6: run from a tree whose conf declares no DESIGN_* key, so a fixture
        # reading this tree's design cannot build, the composed run last; then again under a resolver
        # stub raising LookupError, so the kit's absence is one named SKIP and every other plant, the
        # record-late arm through this host included, runs under the identity strip.
        import deviation_join  # noqa: E402  the join's core, a sibling
        repo, _s = build_fixture(root, "nodesign", [{"msg": "init", "files": {"README.md": "x\n"}}])
        set_fixture_conf(repo)

        def resolve_no_kit(*_args):
            raise LookupError("the self-test's stub resolves no kit")

        here, skipped = os.getcwd(), io.StringIO()
        os.chdir(repo)
        try:
            for ok, what, detail in deviation_join.run_plant_arms():
                print_arm(ok, what, detail)
            with contextlib.redirect_stdout(skipped):
                stubbed = deviation_join.run_plant_arms(resolve=resolve_no_kit)
        finally:
            os.chdir(here)
        held = deviation_join.STRIP_PLANTS
        out = skipped.getvalue()
        print_arm(out.count("deviation: SKIP — the unattended kit does not resolve") == 1
            and "the self-test's stub resolves no kit" in out and f"· {' '.join(held)}" in out
            and not any(f" plant {p} " in what for _ok, what, _d in stubbed for p in held)
            and any(" AC10 " in what for _ok, what, _d in stubbed) and any(" AC6 " in what for _ok, what, _d in stubbed),
            "TOOL-dTrueNorth-12 AC1 a resolver stub raising LookupError is one SKIP line naming why and the "
            f"plants it holds back, {' '.join(held)}, which run no arm, and the record-late host arm and the "
            "composed run still run", out)
        for ok, what, detail in stubbed:
            print_arm(ok, f"under the resolver stub: {what}", detail)

        # ---- TOOL-dTrueNorth-20 AC15 (S16): a RESOLVED kit that cannot strip is the unresolved kit. A
        # scratch kit whose lib-unattended.sh holds no single-line assignment, then an empty one, then a
        # good one with no awk on PATH: each raises LookupError naming the file and GEN_REGION_AWK.
        # Against the base reader the first raised Unmeasured, the second returned '', and every
        # revision then read as status-only, and the third passed the strip to a run that cannot start.
        kit20 = root / "kit20"
        kit20.mkdir()
        lib20 = kit20 / "lib-unattended.sh"
        real_which = shutil.which
        for case, text, which in (("no single-line assignment", "#!/usr/bin/env bash\nOTHER='x'\n", real_which),
                                  ("an empty value", "GEN_REGION_AWK=''\n", real_which),
                                  ("no awk on PATH", "GEN_REGION_AWK='{ print }'\n", lambda *_a, **_k: None)):
            lib20.write_bytes(text.encode("utf-8"))
            shutil.which = which
            try:
                got = f"returned {deviation_join.read_gen_region_awk(lambda *_a: kit20)!r}"
            except LookupError as exc:
                got = f"LookupError {exc}"
            finally:
                shutil.which = real_which
            print_arm(got.startswith("LookupError ") and lib20.as_posix() in got and "GEN_REGION_AWK" in got,
                f"TOOL-dTrueNorth-20 AC15 a resolved kit with {case} raises LookupError naming the file and "
                "GEN_REGION_AWK", got)

        # ---- TOOL-dTrueNorth-20 AC17 (S18): the revision reader over 601 spec paths, every one at least 98
        # bytes, returns one revision each through ONE glob pathspec, where the paths on argv raise
        # [WinError 206]; and a revision log exiting 128 is the named refusal, never an empty history.
        import design_lib  # noqa: E402  the one revision reader, a sibling
        specs20 = {f"memory/builds/dAlpha/spec/2026-10-21-spec-TOOL-dAlpha-{n}-a-padded-name-past-ninety-eight-"
                   f"bytes-{n:03d}.md": f"# TOOL-dAlpha-{n} — one\n" for n in range(1, 602)}
        repo, _s = build_fixture(root, "revs601", [{"msg": "601 specs", "files": specs20}])
        try:
            got = design_lib.read_spec_revisions(repo, list(specs20))
            seen = f"read {sum(len(v) == 1 for v in got.values())} of {len(got)}"
        except (OSError, design_lib.DesignRefusal) as exc:
            seen = f"{type(exc).__name__} {exc}"
        print_arm(min(len(p.encode("utf-8")) for p in specs20) >= 98 and seen == "read 601 of 601",
            "TOOL-dTrueNorth-20 AC17 read_spec_revisions over 601 spec paths of at least 98 bytes reads one "
            "revision each, raising no OSError", seen)
        stub20 = root / "git_log_stub20.py"
        stub20.write_bytes(b"import sys\nsys.stderr.write('fatal: the stub refuses git log\\n')\nsys.exit(128)\n")
        real_run = subprocess.run

        def run_log_stub(argv, *a, **kw):
            if "log" in tuple(argv[:3]) and tuple(argv[:1]) == ("git",):
                return real_run((sys.executable, str(stub20)), *a, **kw)
            return real_run(argv, *a, **kw)

        subprocess.run = run_log_stub
        try:
            design_lib.read_spec_revisions(repo, list(specs20))
            seen = "no refusal"
        except design_lib.DesignRefusal as exc:
            seen = str(exc)
        finally:
            subprocess.run = real_run
        print_arm("the spec revision log failed" in seen and "fatal: the stub refuses git log" in seen,
            "TOOL-dTrueNorth-20 AC17 a revision log exiting 128 raises the named refusal, its stderr line in it", seen)

        # ---- TOOL-dDeclaredLoop-37 AC3 (S5): no consumer spells its own trailer parse. The live arm
        # reads the tracked files of the tool root this kit sits in; the planted arm a scratch
        # repository, by revision, since the fixture checks nothing out. Both sit outside every
        # counted GIT_SPAWNS window.
        try:
            hits = check_trailer_parses(KIT.parent)
            print_arm(not hits, "TOOL-dDeclaredLoop-37 AC3 no tracked file under the tool root spells its own "
                "trailer parse", "\n".join(hits))
        except Refusal:
            print("  ok   — TOOL-dDeclaredLoop-37 AC3 NOT GRADED: the tool root is not in a git work tree, so no "
                  "file was read for a trailer parse")
        planted = "fmt = '" "%(trailers:key=" "Pass,valueonly)'\n"
        repo, s = build_fixture(root, "parses", [{"msg": "plant", "files": {
            "kit/consumer.sh": "# a consumer\n" + planted, "kit/consumer.test.sh": planted,
            # TOOL-dDeclaredLoop-67 S19: the reader's own spelling sits inside its block, which is cut
            "kit/commit_trailers.py": "# >>> commit_trailers_py\n" + planted + "# <<< commit_trailers_py\n"}}])
        hits = check_trailer_parses(repo, s[0])
        try:
            seen = f"returned {check_trailer_parses(repo, '0' * 40)!r}"
        except Refusal as exc:
            seen = f"Refusal {exc}"
        print_arm(hits == ["kit/consumer.sh" + ":" + "2"] and seen.startswith("Refusal "),
            "TOOL-dDeclaredLoop-37 AC3 a planted consumer's trailer parse is named by path and line, the suite "
            "and the reader beside it are not, and a revision git cannot grep is a Refusal",
            f"hits {hits!r}\nan unreadable revision: {seen}")

        # ---- TOOL-dDeclaredLoop-67 AC13 (S19, S20, S40, S41, S54): five plants, one scratch commit. The
        # reordered lowercase spelling on a code line is a hit; on a comment line it is not; inside a
        # carrier's block it is cut and below the block's closing marker it is graded; a file named for
        # the reader that carries no block is graded like any other.
        spelt = "fmt = '%(trailers:valueonly,key=" "pass)'\n"
        block = "# >>> commit_trailers_py\n" + spelt + "# <<< commit_trailers_py\n"
        repo, s = build_fixture(root, "parses67", [{"msg": "plant", "files": {
            "kit/code.py": spelt, "kit/comment.py": "# " + spelt, "kit/carrier.py": block + spelt,
            "kit/commit_trailers.py": spelt}}])
        hits = check_trailer_parses(repo, s[0])
        owed = ["kit/carrier.py" + ":" + "4", "kit/code.py" + ":" + "1", "kit/commit_trailers.py" + ":" + "1"]
        print_arm(sorted(hits) == owed,
            "TOOL-dDeclaredLoop-67 AC13 a lowercase reordered spelling on a code line, the line below a carrier's "
            "block and a blockless reader file are named; the comment line and the in-block literal are not",
            f"hits {hits!r}, owed {owed!r}")

        # ---- TOOL-dDeclaredLoop-67 AC9 (S52): the reader's `tokens` verb over a trailer key table that does
        # not parse, then one whose [[trailer]] row has no key: each refused naming the table, exit 2,
        # never the floor. The reader is copied beside a scratch table its resolver finds as a sibling kit,
        # the table's folder named as the tree's own table's is.
        import commit_trailers  # noqa: E402  the kit's one trailer reader
        table_home = commit_trailers.read_key_table()[1].parent.name
        fix52 = commit_trailers.build_fixture(root / "keys52")
        (fix52 / "kit" / "reader").mkdir(parents=True)
        (fix52 / "kit" / table_home).mkdir()
        shutil.copyfile(KIT / "commit_trailers.py", fix52 / "kit" / "reader" / "commit_trailers.py")
        seen52 = []
        for label, table, needle in (("does not parse", "[[trailer]\nkey = 1\n", "does not parse"),
                                     ("a keyless row", '[[trailer]]\nkey = "Pass"\n[[trailer]]\ntype = "x"\n',
                                      "holds a [[trailer]] row 2 with no key")):
            (fix52 / "kit" / table_home / "edges.toml").write_text(table, encoding="utf-8")
            p52 = subprocess.run([sys.executable, str(fix52 / "kit" / "reader" / "commit_trailers.py"), "tokens",
                                  "HEAD"], cwd=fix52, capture_output=True, text=True, encoding="utf-8",
                                 errors="replace",
                                 env={k: v for k, v in build_git_env().items() if k not in GIT_ENV_LEAKS})
            said = p52.stdout + p52.stderr
            seen52.append(f"{label}: exit {p52.returncode} · {said.strip()[:300]}")
            print_arm(p52.returncode == 2 and "commit_trailers: refused · the trailer key table " in said
                      and needle in said and "edges.toml" in said,
                "TOOL-dDeclaredLoop-67 AC9 a trailer key table that " + label.replace("a keyless row", "holds a "
                "keyless row") + " is refused naming the table, exit 2", seen52[-1])

        # ---- TOOL-dDeclaredLoop-38 AC1, TOOL-dDeclaredLoop-58 AC1: the trailer CLI's stdout over the
        # planted fixture holds one sha-led line per commit `git rev-list HEAD` lists, then no CR.
        # The CR half is live on win32 only: where the default newline is LF it cannot turn red.
        import commit_trailers  # noqa: E402  already imported above; build_fixture is the reader's own
        fix38 = commit_trailers.build_fixture(root / "lf38")
        out38 = subprocess.run([sys.executable, str(KIT / "commit_trailers.py"), "tokens", "HEAD"], cwd=fix38,
                               capture_output=True,
                               env={k: v for k, v in build_git_env().items() if k not in GIT_ENV_LEAKS}).stdout
        shas38 = run_git(fix38, "rev-list", "HEAD").decode("ascii").split()
        lf38 = check_lf_lines(out38, shas38)
        print_arm(not lf38,
            "TOOL-dDeclaredLoop-38 AC1 TOOL-dDeclaredLoop-58 AC1 `tokens HEAD` over the planted fixture writes "
            f"one line per listed commit, LF only, on {sys.platform}"
            + ("" if sys.platform == "win32" else " (the CR half is not live here: the default newline is LF;"
               " the count half is)"), "\n".join(lf38) + f"\n{out38!r}")

        # ---- TOOL-dDeclaredLoop-39 AC4: this kit's copy of the reader drops tree_lib's leak list, the
        # canonical's copy compared with the kit's own tuple, member for member and in order.
        import tree_lib  # noqa: E402
        print_arm(pathlib.Path(commit_trailers.__file__).resolve().parent == KIT
                  and commit_trailers.GIT_ENV_LEAKS == tree_lib.GIT_ENV_LEAKS,
            "TOOL-dDeclaredLoop-39 AC4 this kit's commit_trailers.GIT_ENV_LEAKS equals tree_lib.GIT_ENV_LEAKS",
            f"reader {commit_trailers.__file__}: {commit_trailers.GIT_ENV_LEAKS!r}\ntree_lib: {tree_lib.GIT_ENV_LEAKS!r}")

        # ---- TOOL-dDeclaredLoop-40 AC2 AC3 AC5 AC6: this kit's copy of the reader in a scratch tree with
        # no trailer key table, then with a table of no rows, reads the floor keys, refuses any other by
        # name, and notes the skipped check once per process on stderr, never on stdout.
        top40 = root / "floor40"
        (top40 / "kit").mkdir(parents=True)
        shutil.copy(KIT / "commit_trailers.py", top40 / "kit")
        fix40 = commit_trailers.build_fixture(top40)
        env40 = {k: v for k, v in build_git_env().items() if k not in GIT_ENV_LEAKS}
        read40 = ("import sys; sys.path.insert(0, sys.argv[1]); import commit_trailers as ct\n"
                  "for keys, files in ((('Pass',), 0), (('Pass',), 0), (('Pass', 'Red-fix'), 1), (('Gov-Nope',), 0)):\n"
                  "    try: print([c['trailers'] for c in ct.read_commits('.', ['-1', 'HEAD'], keys, files)])\n"
                  "    except ValueError as exc: print('ValueError', exc)\n")

        def run40(*argv):
            return subprocess.run([sys.executable, *argv], cwd=fix40, capture_output=True, text=True, encoding="utf-8", env=env40)

        note40 = "unregistered-key check skipped: no edges.toml"
        want40 = ["[{'Pass': ['TOOL-tFix-2']}]"] * 2 + ["[{'Pass': ['TOOL-tFix-2'], 'Red-fix': []}]"]
        got = run40("-c", read40, str(top40 / "kit"))
        lines = got.stdout.splitlines()
        print_arm(lines[:3] == want40 and len(lines) > 3 and "'Gov-Nope'" in lines[3] and lines[3].startswith("ValueError")
                  and got.stderr.count(note40) == 1,
            "TOOL-dDeclaredLoop-40 AC2 AC3 AC6 with no trailer key table the reader reads Pass and Red-fix, "
            "refuses Gov-Nope by name, and notes the skipped check once", f"{got.stdout}\n{got.stderr}")
        tok = run40(str(top40 / "kit" / "commit_trailers.py"), "tokens", "-1", "HEAD")
        print_arm(tok.returncode == 0 and "PASSTRAILER TOOL-tFix-2" in tok.stdout and note40 not in tok.stdout
                  and note40 in tok.stderr,
            "TOOL-dDeclaredLoop-40 AC3 `tokens` with no trailer key table exits 0, its note on stderr only",
            f"exit {tok.returncode}\n{tok.stdout}\n{tok.stderr}")
        edge_kit = "playbook"   # the trailer key table's kit folder, named once, never joined as a literal
        (top40 / edge_kit).mkdir()
        (top40 / edge_kit / "edges.toml").write_text("# no [[trailer]] row\n", encoding="utf-8")
        got = run40("-c", read40, str(top40 / "kit"))
        print_arm(got.stdout.splitlines()[:1] == want40[:1] and note40 in got.stderr,
            "TOOL-dDeclaredLoop-40 AC5 a trailer key table of no rows reads the floor keys, with the note",
            f"{got.stdout}\n{got.stderr}")

        # ---- TOOL-dQuietDisk-4 AC4 AC5: the record store against this module's own store-off read, over
        # one history holding a lane commit, a merge and an unattributed routed commit: cold, warm, after
        # one added commit and after one torn bucket. The bound is patched to 2, so the cold fill logs
        # HEAD and the later ones log by id. Staged by a fill that reads the buckets and logs no lack:
        # the added commit and the torn bucket's members then go unread, and the leg refuses at exit 2.
        repo, s = build_fixture(root, "stored", [
            {"msg": "init", "date": OLD_EPOCH,
             "files": {"README.md": "x\n", "legs.json": '[{"name": "leg one"}]\n', "src/a.txt": "0\n"}},
            {"msg": "spec TOOL-tFix-1", "files": {SPEC1: "# TOOL-tFix-1 — one\n"}},
            {"msg": "fix: clear leg one\n\nRed-fix: leg one\nPass: none", "files": {"src/a.txt": "a\n"}},
            {"msg": "side: docs", "files": {"README.md": "side\n"}},
            {"msg": "TOOL-tFix-1: main step", "files": {"src/m.txt": "m\n"}, "parent": 3},
            {"msg": "Merge side", "files": {"README.md": "side\n"}, "parent": 5, "merge": [4]},
            {"msg": "chore: no id", "files": {"src/c.txt": "c\n"}},
        ])
        set_fixture_conf(repo, LEG_MANIFEST="legs.json")
        items = repo / ".git" / "history-verdicts" / "v1" / SAY / "items"
        bound_name, logged, seen4 = "LOG_BATCH_BOUND", [], []
        off_store, real_read, real_bound = globals()["resolve_store"], globals()["read_commits"], globals()[bound_name]

        def read_spied_commits(at, revs, *a, **kw):
            logged.append(list(revs))
            return real_read(at, revs, *a, **kw)

        def check_stored_read(what, owed_logs) -> None:
            globals()["resolve_store"] = off_store
            want = run_check(repo)
            globals()["resolve_store"] = real_store
            logged.clear()
            got = run_check(repo)
            files = sorted(p for p in items.rglob("*") if p.is_file()) if items.is_dir() else []
            seen4.append(f"{what}: logs {logged} · {len(files)} item(s)")
            print_arm(got == want and logged == owed_logs and bool(files),
                f"TOOL-dQuietDisk-4 AC4 AC5 {what}: the store-on read prints the store-off read's bytes and exit, "
                f"logging {owed_logs}", f"{seen4[-1]}\nwant {want!r}\ngot  {got!r}")

        def add_fixture_commit(msg, path) -> str:
            head = run_git(repo, "rev-parse", "HEAD").decode("ascii").strip()
            data, when = msg.encode("utf-8"), BASE_EPOCH + 3600
            run_git(repo, "fast-import", "--quiet", stdin=b"commit refs/heads/main\ncommitter T <t@e> %d +0000\n"
                    b"data %d\n%s\nfrom %s\nM 100644 inline %s\ndata 2\nn\n\n"
                    % (when, len(data), data, head.encode("ascii"), path.encode("utf-8")))
            return run_git(repo, "rev-parse", "HEAD").decode("ascii").strip()

        globals()["read_commits"], globals()[bound_name] = read_spied_commits, 2
        try:
            check_stored_read("cold", [["HEAD"]])
            check_stored_read("warm at an unmoved HEAD", [])
            added = add_fixture_commit("chore: added, no id", "src/n.txt")
            check_stored_read("after one added commit", [["--no-walk=unsorted", added]])
            # A LIVE bucket: one whose members are every commit under its prefix, never the item the added
            # commit's bucket left behind, which no run reads again.
            order = run_git(repo, "rev-list", "HEAD").decode("ascii").split()
            for torn in sorted(p for p in items.rglob("*") if p.is_file()):
                data = torn.read_bytes()
                members = [row["sha"] for row in json.loads(data.partition(b"\n")[2].decode("utf-8"))]
                if sorted(members) == sorted(x for x in order if x[:RECORD_BUCKET_HEX] == members[0][:RECORD_BUCKET_HEX]):
                    break
            torn.write_bytes(data[: len(data) // 2])
            lack = [x for x in order if x in members]
            check_stored_read("after one torn bucket", [["HEAD"] if len(lack) > 2 else ["--no-walk=unsorted", *lack]])
        finally:
            globals()["read_commits"], globals()[bound_name] = real_read, real_bound
            globals()["resolve_store"] = off_store
    finally:
        globals()["resolve_store"] = real_store
        import deviation_join  # noqa: E402  its remover: git's objects are read-only on Windows
        deviation_join.remove_tree(root)
    print(f"{SAY} selftest: {'all arms held' if not failed else f'{len(failed)} arm(s) FAILED'}")
    return 1 if failed else 0


def main(argv: list) -> int:
    args = argv[1:]
    if args == ["--selftest"]:
        return run_selftest()
    try:
        repo = pathlib.Path(run_git(os.getcwd(), "rev-parse", "--show-toplevel").decode("utf-8").strip())
        if len(args) in (2, 3) and args[0] == "--newest-unit":
            unit = read_newest_unit(repo, args[1], args[2] if len(args) == 3 else None)
            if unit:
                print(unit)
            return 0
        if len(args) == 2 and args[0] == "--red-fix-limits":
            # TOOL-aNimbleMend-10 S8: the one commit the rev names, merge or not, against the same
            # predicate the leg runs. It reads no waiver.
            conf = load_conf(repo)
            tracked = [p for p in run_git(repo, "ls-tree", "-r", "-z", "--name-only", "HEAD").decode("utf-8", "replace").split("\0") if p]
            entries, _cutoff, _families, memory_root, _waived = check_conf(conf, tracked)
            got = run_git(repo, "rev-parse", "--verify", "--quiet", "--end-of-options", args[1] + "^{commit}", may_fail=True)
            if not got:
                raise Refusal(f"--red-fix-limits {args[1]} names no commit in this clone")
            fix = read_routed_commits(repo, ["-1", got.decode("utf-8").strip()])[0]
            if not fix["red_fix"]:
                raise Refusal(f"commit {fix['sha'][:8]} carries no `{RED_FIX_TRAILER}:` trailer, so the inline "
                              f"lane's limits do not grade it")
            over = check_red_fix_limits(repo, [fix], entries, memory_root, []).get(fix["sha"], [])
            if not over:
                print(f"{SAY}: red-fix limits · {fix['sha'][:8]} is inside all four · bound {RED_FIX_MAX_PATHS} "
                      f"path(s), {RED_FIX_MAX_LINES} line(s)")
                return 0
            print(f"{SAY} FAILED — a Red-fix commit is outside the inline lane's limits:")
            for found in over:
                print(f"  {fix['sha'][:8]} {fix['subject']} — {found}")
            return 1
        if args:
            print(f"{SAY}: unknown arguments {' '.join(args)}; the verbs are none, --newest-unit <range> [<path>], "
                  f"--red-fix-limits <rev> and --selftest")
            return 2
        rc, lines = check_routed_commits(repo, os.environ)
    except Refusal as exc:
        print(f"{SAY} REFUSED — {exc}")
        return 2
    print("\n".join(lines))
    return rc


if __name__ == "__main__":
    # The deviation join imports this module by name; one copy keeps one Refusal class and one counter.
    sys.modules.setdefault("routed_commits", sys.modules[__name__])
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv))
