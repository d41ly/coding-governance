#!/usr/bin/env python3
"""routed_commits.py — every commit touching a product path names a unit specced before it.

TOOL-aRoutedQuill-3. The write gate (`scratch-guard.js`) sees Edit and Write calls only, so a product
file changed through a shell, a hook-less run or an unwired install reaches a commit with no unit
behind it. This leg grades the COMMITS: every non-merge commit touching a path under `ROUTED_PATHS`
must name a unit id whose spec existed at that commit's first parent.

    python routed_commits.py                          # grade the range, print the summary
    python routed_commits.py --newest-unit <range>    # the newest unit id <range>'s commits attribute
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
names; `Pass: none` adds none and keeps the subject's. That deliberately differs from
`read_attribution_tokens` in the unattended kit, where a trailer REPLACES the subject: that reader
decides which commit is a unit's pass, this leg only whether a commit is attributed to any unit.
Which spec defines an id is `tree_lib.parse_spec_h1` over every spec at HEAD.

Exit 0 clean · 1 a violation or a stale waiver · 2 REFUSED, the leg cannot give an answer worth
reading (an unarmed conf, a shallow clone, an empty id map, a truncated log stream).

WHAT THIS DOES NOT CHECK, stated because a structural check reads as a semantic one to everybody who
did not write it. ANY named id with a spec at the first parent passes (F1): whether that unit's
scope covers the change is not read, nor the spec's quality, tier or status. A merge's own content
is not graded, so a conflict resolution that adds product code passes; its non-merge parents are
graded. Commits committed before `ROUTED_COMMIT_CUTOFF` are counted and not graded, and the cutoff
is a date the committer sets. The graded run controls the conf, so it can narrow `ROUTED_PATHS`,
move the cutoff or list a waiver: the summary prints all three as a trace, not a guard. A spec
moved since the commit is looked for at its HEAD path and reads as absent. Pass-order history
(the unattended kit) answers "spec at the first parent" from a header window and lets a trailer
replace the subject; this file reads the H1 and the union, and NOTHING machine-joins the two files.

Every git call is pinned (`--no-replace-objects`, `tree_lib.build_git_env`) and counted: the
self-test holds the number of spawns constant whatever the range holds.
"""
from __future__ import annotations

import datetime
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
from tree_lib import build_git_env, build_spec_path_re, parse_conf, parse_spec_h1  # noqa: E402

SAY = "routed-commits"
ZERO_SHA_RE = re.compile(r"^0+$")
SHA_RE = re.compile(r"^[0-9a-f]{7,40}$")
# The variables a hook exports that would point a `-C <repo>` call at ANOTHER repository. Every call
# here names its repository explicitly, so dropping them is always correct, and it is what keeps a
# self-test fixture from reading the real repository when the bar runs inside a hook.
GIT_LOCATION_VARS = ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_COMMON_DIR",
                     "GIT_OBJECT_DIRECTORY", "GIT_ALTERNATE_OBJECT_DIRECTORIES", "GIT_PREFIX")
#: Every git process this module starts, counted so the self-test can hold it constant (AC6).
GIT_SPAWNS = [0]


class Refusal(Exception):
    """S7: the leg cannot give an answer worth reading. Exit 2, never a reassuring zero."""


def run_git(repo, *args, stdin: bytes | None = None, may_fail: bool = False):
    """One pinned git call in `repo`, its stdout as bytes; None on failure when `may_fail`."""
    GIT_SPAWNS[0] += 1
    env = build_git_env()
    for key in GIT_LOCATION_VARS:
        env.pop(key, None)
    argv = ["git", "--no-replace-objects", "-c", "log.showSignature=false", "-C", str(repo), *args]
    proc = subprocess.run(argv, input=stdin, capture_output=True, env=env)
    if proc.returncode != 0:
        if may_fail:
            return None
        detail = proc.stderr.decode("utf-8", "replace").strip()
        raise Refusal(f"`git {' '.join(args)}` failed: {detail}")
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
        if bare in ("", ".") or memory_root == bare or memory_root.startswith(bare + "/"):
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
    subject, `Pass:` trailer and the paths it touches, renames read as a deletion plus an addition."""
    fmt = "%x1e%H%x1f%P%x1f%cI%x1f%s%x1f%(trailers:key=Pass,valueonly,separator=%x20)%x1f"
    raw = run_git(repo, "log", "-z", "--root", "--no-renames", "--name-only", "--no-color",
                  f"--format={fmt}", *rev_args, "--").decode("utf-8", "replace")
    commits = []
    for rec in raw.split("\x1e")[1:]:
        sha, parents, date, subject, trailer, rest = rec.split("\x1f", 5)
        commits.append({"sha": sha, "parents": parents.split(), "date": date, "subject": subject,
                        "trailer": trailer.strip(), "paths": [p for p in re.split(r"[\0\n]", rest) if p]})
    return commits


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
    lines, failed, range_shas = [], False, set()
    for mode, rev_args, label, tag in populations:
        commits = read_routed_commits(repo, rev_args)
        total = int(run_git(repo, "rev-list", "--count", *rev_args).decode("utf-8").strip())
        if total != len(commits):
            raise Refusal(f"the log pass parsed {len(commits)} commit(s) and `git rev-list --count` reports {total} "
                          f"over the same range; a truncated stream is not a clean one")
        merges = exempt = not_routed = graded = 0
        violations, pending = [], []
        for c in commits:
            if len(c["parents"]) >= 2:
                merges += 1
            elif c["date"][:10] < cutoff:
                exempt += 1
            elif not any(test_routed_path(p, entries) for p in c["paths"]):
                not_routed += 1
            else:
                graded += 1
                ids = extract_unit_ids(c["subject"] + " " + c["trailer"], id_re)
                pairs = [(i, p) for i in ids for p in id_map.get(i, [])]
                if not ids:
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
        waived_n, stale = 0, []
        if mode == "WHOLE" and waived:
            kept = []
            for v in violations:
                if any(v[0]["sha"].startswith(w) for w in waived):
                    waived_n += 1
                else:
                    kept.append(v)
            stale = [w for w in waived if not any(v[0]["sha"].startswith(w) for v in violations)]
            violations = kept
        failed = failed or bool(violations or stale)
        lines.append(f"{SAY}: {label} · graded {graded} · {exempt} exempt by the {cutoff} cutoff · {merges} merge(s) · "
                     f"{not_routed} not routed · {waived_n} waived · {len(id_map)} spec id(s) at HEAD · ROUTED_PATHS {routed}")
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
    return (1 if failed else 0), lines


def read_newest_unit(repo, rev_range: str) -> str:
    """The first id the newest attributed commit in `rev_range` names, by the union reading; '' when
    none does. The attended lander's mint names this unit (S11)."""
    repo = pathlib.Path(repo)
    families = extract_families(load_conf(repo))
    if not families:
        return ""
    id_re = build_id_re(families)
    raw = run_git(repo, "log", "--no-color", "--format=%s%x1f%(trailers:key=Pass,valueonly,separator=%x20)%x1e",
                  rev_range, "--").decode("utf-8", "replace")
    for rec in raw.split("\x1e"):
        ids = extract_unit_ids(rec.replace("\x1f", " "), id_re)
        if ids:
            return ids[0]
    return ""


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
    run_git(repo, "init", "-q")
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
        mint = "mint: kit versions onto origin/main at 1234abcd"
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
        if args:
            print(f"{SAY}: unknown arguments {' '.join(args)}; the verbs are none, --newest-unit <range> and --selftest")
            return 2
        rc, lines = check_routed_commits(repo, os.environ)
    except Refusal as exc:
        print(f"{SAY} REFUSED — {exc}")
        return 2
    print("\n".join(lines))
    return rc


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv))
