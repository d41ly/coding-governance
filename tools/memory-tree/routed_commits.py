#!/usr/bin/env python3
"""routed_commits.py — every commit touching a product path names a unit specced before it.

TOOL-aRoutedQuill-3. The write gate (`scratch-guard.js`) sees Edit and Write calls only, so a product
file changed through a shell, a hook-less run or an unwired install reaches a commit with no unit
behind it. This leg grades the COMMITS: every non-merge commit touching a path under `ROUTED_PATHS`
must name a unit id whose spec existed at that commit's first parent.

    python routed_commits.py                          # grade the range, print the summary
    python routed_commits.py --newest-unit <range>    # the newest unit id <range>'s commits attribute
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
policy kit's `guarded-paths.txt` lists, read as the working tree holds it; where no policy kit
resolves, no path under `.governance/`. L3: no path under any build's `spec/` folder. L4: no path
added under `ROUTED_PATHS`, a rename read as a deletion and an addition. `ROUTED_COMMIT_WAIVED`
excuses a finding in WHOLE and never in RANGE, and the stale rule counts a finding as a violation.
One `red-fix limits` line per population says how many were graded; a population holding no fix
commit costs no git call, any other exactly one. `--red-fix-limits <rev>` grades the one commit
`<rev>` names, merge or not, with no waiver: exit 0 inside the limits, 1 over one, 2 when the rev
names no commit or the commit carries no trailer. NOT checked: whether the change is a fix, a new
surface made inside an existing file, a deleted path, any record outside `spec/`, and a guarded
list the fix commit itself shortened.

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
"""
from __future__ import annotations

import contextlib
import datetime
import io
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
from tree_lib import (GIT_ENV_LEAKS, RED_FIX_TRAILER, build_git_env, build_spec_path_re, parse_conf,  # noqa: E402
                      parse_leg_names, parse_spec_h1, read_policy_value)
from commit_trailers import derive_attribution, read_commits  # noqa: E402  the kit's one trailer reader

SAY = "routed-commits"
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


def load_spec_paths(repo, tracked: list, memory_root: str, families: list) -> tuple:
    """`({id: [spec paths]}, specs tracked)`: which spec defines each id at HEAD, in ONE read."""
    spec_re = build_spec_path_re(memory_root)
    specs = [p for p in tracked if spec_re.match(p) and p.endswith(".md")]
    id_map: dict = {}
    if not specs:
        return id_map, 0
    raw = run_git(repo, "cat-file", "--batch", stdin="".join(f"HEAD:{p}\n" for p in specs).encode("utf-8"))
    pos = 0
    for path in specs:
        end = raw.index(b"\n", pos)
        head = raw[pos:end].split()
        pos = end + 1
        if len(head) != 3 or head[-1] == b"missing":
            continue
        size = int(head[2])
        text = raw[pos:pos + size].decode("utf-8", "replace").replace("\r\n", "\n")
        pos += size + 1
        hit = parse_spec_h1(path, text, memory_root, families)
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


def read_routed_commits(repo, rev_args: list) -> list:
    """Every commit in the range, newest first, from ONE log pass (S6): sha, parents, committer date,
    subject, `Pass:` trailer and the paths it touches, renames read as a deletion plus an addition.
    `red_fix` is the list of its `Red-fix:` trailer values (TOOL-aNimbleMend-8 S5), one leg name per
    trailer line: a leg name holds spaces, commas and parentheses, so a value is its whole line.
    The pass is the one trailer reader's, run through this module's pinned, counted runner
    (TOOL-dDeclaredLoop-23 S5); a key the trailer table does not register, a kit that does not resolve
    and a stream that ends mid-record are each a Refusal."""
    try:
        commits = read_commits(repo, rev_args, ("Pass", RED_FIX_TRAILER), files=True,
                               run=lambda at, argv: run_git(at, *argv))
    except (LookupError, ValueError) as exc:
        raise Refusal(f"the commit log cannot be read: {exc}") from None
    for c in commits:
        c["trailer"] = " ".join(c["trailers"]["Pass"]).strip()
        c["red_fix"] = [v for v in c["trailers"][RED_FIX_TRAILER] if v]
    return commits


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
    return [ln.strip() for ln in text.splitlines() if ln.strip() and not ln.strip().startswith("#")]


def check_red_fix_limits(repo, fixes: list, entries: list, memory_root: str, guarded: list) -> dict:
    """`{sha: [finding]}` over `fixes`, the `Red-fix:` commits of one population: the inline lane's four
    limits (TOOL-aNimbleMend-10), one finding per limit a commit is over, and no key for a commit
    inside all four.

    L1 size: more than RED_FIX_MAX_PATHS paths under ROUTED_PATHS, more than RED_FIX_MAX_LINES lines
    added plus deleted over them, or a binary one. L2 guarded policy file: a path the policy kit's
    list names. L3 spec edit: a path under any build's `spec/` folder. L4 new surface: a path added
    under ROUTED_PATHS, a rename read as a deletion and an addition.

    No git call where `fixes` is empty, and ONE otherwise whatever its length (S9): a `git log` over
    those commits alone, the shas on stdin, carrying the numeric and the raw status form. A merge is
    read against its first parent. `guarded` is the caller's one-slot cache of `read_guarded_paths`,
    filled here on the first fix commit of the run and never before."""
    if not fixes:
        return {}
    if not guarded:
        guarded.append(read_guarded_paths())
    spec_re = build_spec_path_re(memory_root)
    raw = run_git(repo, "log", "--no-walk=unsorted", "--stdin", "--root", "--no-renames", "--raw", "--numstat",
                  "-z", "--no-color", "--diff-merges=first-parent", "--format=%x1e%H%x1f",
                  stdin="".join(c["sha"] + "\n" for c in fixes).encode("utf-8")).decode("utf-8", "replace")
    found = {}
    for rec in raw.split("\x1e")[1:]:
        sha, rest = rec.split("\x1f", 1)
        tokens = iter(rest.split("\0"))
        paths, added, lines, binary = [], [], 0, False
        for tok in tokens:
            tok = tok.lstrip("\n")
            stat = re.match(r"(\d+|-)\t(\d+|-)\t(.+)$", tok, re.S)
            if tok.startswith(":"):                 # the raw form: `:modes shas STATUS`, then its path
                path = next(tokens, "")
                paths.append(path)
                if tok.split()[-1].startswith("A") and test_routed_path(path, entries):
                    added.append(path)
            elif stat and test_routed_path(stat.group(3), entries):
                if stat.group(1) == "-":
                    binary = True
                else:
                    lines += int(stat.group(1)) + int(stat.group(2))
        routed_n = sum(1 for p in paths if test_routed_path(p, entries))
        held = [p for p in paths if (p.startswith(".governance/") if guarded[0] is None else p in guarded[0])]
        specs = [p for p in paths if spec_re.match(p)]
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
    for mode, rev_args, label, tag in populations:
        commits = read_routed_commits(repo, rev_args)
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
                raw = run_git(repo, "cat-file", "--batch",
                              stdin="".join(f"{c['sha']}:{manifest}\n" for c in candidates).encode("utf-8"))
                pos = 0
                for c in candidates:
                    end = raw.index(b"\n", pos)
                    head = raw[pos:end].split()
                    pos = end + 1
                    if len(head) != 3 or not head[2].isdigit():
                        continue                # `missing`: no manifest at that commit
                    body, pos = raw[pos:pos + int(head[2])], pos + int(head[2]) + 1
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


def read_newest_unit(repo, rev_range: str) -> str:
    """The first id, walking the non-merge commits of `rev_range` newest first, that a spec at HEAD
    defines, by the union reading; '' when none does. The attended lander's mint names this unit (S11),
    so an unspecced id or a merge's id would name one the leg cannot grade (TOOL-aRoutedQuill-12 S2)."""
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
        commits = read_commits(repo, ["--no-merges", rev_range], ("Pass",), run=lambda at, argv: run_git(at, *argv))
    except (LookupError, ValueError) as exc:
        raise Refusal(f"the commit log cannot be read: {exc}") from None
    for c in commits:
        for uid in derive_attribution(c, "union", id_re):
            if uid in id_map:
                return uid
    return ""


#: TOOL-dDeclaredLoop-37 S5: the two spellings of a consumer's own trailer parse. Each literal is split
#: inside its needle, so the probe never reads this line as a hit.
TRAILER_PARSE_NEEDLES = ("trailers:key=" "Pass,", "interpret-trailers " "--parse")


def check_trailer_parses(root, rev=None) -> list:
    """Every line under `root` that spells its own trailer parse, as `<path>:<line>` relative to
    `root`: ONE `git grep -n -F` for the two needles, run in `root`, over its tracked files, or
    over the tree of `rev` when given, less `*.test.sh` and any `commit_trailers.py`.
    [] where git greps and finds none; Refusal where git cannot grep `root`.

    It does not read a parse spelled another way, a key other than `Pass`, or an untracked file."""
    argv = ["grep", "-n", "-z", "-F"]
    for needle in TRAILER_PARSE_NEEDLES:
        argv += ["-e", needle]
    argv += ([rev] if rev else []) + ["--", ".", ":!*.test.sh", ":!*commit_trailers.py"]
    try:
        out = run_git(root, *argv)
    except Refusal as exc:
        # git grep exits 1 for no match; any other failure is git unable to grep, never an empty answer.
        if exc.status == 1 and not exc.out.strip():
            return []
        raise
    hits = []
    for line in out.decode("utf-8", "replace").split("\n"):
        if line:
            path, num = line.split("\0")[:2]
            hits.append(f"{path[len(rev) + 1:] if rev else path}:{num}")
    return hits


# ------------------------------------------------------------------------------------- self-test
BASE_EPOCH = 1767225600      # 2026-01-01, after every fixture cutoff
OLD_EPOCH = 959817600        # 2000-06-01, before the fixture cutoff 2001-01-01
SPEC1 = "memory/builds/tFix/spec/2026-01-01-spec-TOOL-tFix-1.md"
SPEC2 = "memory/builds/tFix/spec/2026-01-01-spec-TOOL-tFix-2.md"


def build_fixture(root: pathlib.Path, name: str, commits: list) -> tuple:
    """A scratch repository from ONE `git fast-import`: `(repo, [sha per commit])`.

    Each commit is `{msg, files: {path: text | None}, date?, parent?, merge?}`, parents named by their
    1-based position; a commit's first parent defaults to the one before it."""
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
                body = text.encode("utf-8")
                out += b"M 100644 inline %s\ndata %d\n%s\n" % (path.encode("utf-8"), len(body), body)
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
            "kit/commit_trailers.py": planted}}])
        hits = check_trailer_parses(repo, s[0])
        try:
            seen = f"returned {check_trailer_parses(repo, '0' * 40)!r}"
        except Refusal as exc:
            seen = f"Refusal {exc}"
        print_arm(hits == ["kit/consumer.sh" + ":" + "2"] and seen.startswith("Refusal "),
            "TOOL-dDeclaredLoop-37 AC3 a planted consumer's trailer parse is named by path and line, the suite "
            "and the reader beside it are not, and a revision git cannot grep is a Refusal",
            f"hits {hits!r}\nan unreadable revision: {seen}")

        # ---- TOOL-dDeclaredLoop-38 AC1: the trailer CLI's stdout holds no CR over the planted fixture.
        # Live on win32 only: where the default newline is LF the arm cannot turn red, and says which ran.
        # It counts no lines: TOOL-dDeclaredLoop-58's.
        import commit_trailers  # noqa: E402  already imported above; build_fixture is the reader's own
        fix38 = commit_trailers.build_fixture(root / "lf38")
        out38 = subprocess.run([sys.executable, str(KIT / "commit_trailers.py"), "tokens", "HEAD"], cwd=fix38,
                               capture_output=True,
                               env={k: v for k, v in build_git_env().items() if k not in GIT_ENV_LEAKS}).stdout
        print_arm(b"\r" not in out38,
            f"TOOL-dDeclaredLoop-38 AC1 `tokens HEAD` over the planted fixture writes LF only, on {sys.platform}"
            + ("" if sys.platform == "win32" else " (not live here: the default newline is LF)"), repr(out38))

        # ---- TOOL-dDeclaredLoop-39 AC4: this kit's copy of the reader drops tree_lib's leak list, the
        # canonical's copy compared with the kit's own tuple, member for member and in order.
        import tree_lib  # noqa: E402
        print_arm(pathlib.Path(commit_trailers.__file__).resolve().parent == KIT
                  and commit_trailers.GIT_ENV_LEAKS == tree_lib.GIT_ENV_LEAKS,
            "TOOL-dDeclaredLoop-39 AC4 this kit's commit_trailers.GIT_ENV_LEAKS equals tree_lib.GIT_ENV_LEAKS",
            f"reader {commit_trailers.__file__}: {commit_trailers.GIT_ENV_LEAKS!r}\ntree_lib: {tree_lib.GIT_ENV_LEAKS!r}")
    finally:
        shutil.rmtree(root, ignore_errors=True)
    print(f"{SAY} selftest: {'all arms held' if not failed else f'{len(failed)} arm(s) FAILED'}")
    return 1 if failed else 0


def main(argv: list) -> int:
    args = argv[1:]
    if args == ["--selftest"]:
        return run_selftest()
    try:
        repo = pathlib.Path(run_git(os.getcwd(), "rev-parse", "--show-toplevel").decode("utf-8").strip())
        if len(args) == 2 and args[0] == "--newest-unit":
            unit = read_newest_unit(repo, args[1])
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
            print(f"{SAY}: unknown arguments {' '.join(args)}; the verbs are none, --newest-unit <range>, "
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
