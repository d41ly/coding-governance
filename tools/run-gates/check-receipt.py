#!/usr/bin/env python3
"""check-receipt.py — the files the deployer installed here, against the hashes its receipt records.

WHAT THIS CHECKS. `.governance/install.json` lists every file a deployment wrote into this tree,
each with the sha256 of the bytes that landed. This reads that list and reds when an engine row's
file is missing, or is present and no longer hashes to its recorded value. That is the INTEGRITY
half of the deployer's own `check` verb, and the half is the whole point: `check` needs a gov
checkout beside this tree and is invoked automatically by nothing, so an adopter's own merge bar has
had no way at all to learn that an installed file drifted.

WHAT IT DOES NOT CHECK, said out loud because a structural check reads as a semantic one to
everyone who did not write it.

  - No DESCRIPTOR half and no PROVENANCE half. A row's `source`, `commit` and `gov_oid` resolve only
    against a gov checkout, which is exactly the thing an adopter does not have.
  - No `seed` row. That role's contract is that this tree OWNS the file after one copy, so hashing
    one would red every target that did what the role exists to permit.
  - No `merged`, `attributes` or `forked` row. A merged row's `sha256` covers the whole merged file
    while its real contract is only the marked block, which needs the extractor and the marker table.
  - No `.governance/install.sums`. The sidecar is written from EVERY row carrying `sha256`, seed rows
    included, so verifying it reds the population the bullet above deliberately exempts.
  - No VERDICT on the `evidence` state, though it is now READ. Rows carrying `unattributed` are
    counted and printed as a NOTE, and that count never moves the exit status: the remedy the note
    prints only began working in this same release, so redding on it here would hand an adopter a
    failure they have had no release in which to clear. The follow-up that turns the note into a
    leg failure is the release AFTER adopters have had one. Until then this arm only reports, and
    the integrity arm above is the only one that decides.
  - And it does not know whether a recorded hash is RIGHT, only whether the bytes still match it.
    A row whose raw bytes miss its `sha256` is graded once more, through the TARGET'S OWN clean
    filter: when `git hash-object` over the working file yields the row's `oid` and the raw bytes'
    blob does not, the only difference is one the target's filters remove, so the row counts as
    `eol-only` and clean — the rule `govkit check` applies. What still reds: a row with no `oid`
    (a receipt below schema 3), a real content edit, a CRLF copy no filter normalizes, a tampered
    `sha256` over bytes that ARE the blob, a tree with no `.git`, and any row when git refuses. A
    receipt written on a CRLF box and graded on an LF clone reds too, because there the raw bytes are
    the blob; that is what the receipt records, and the summary line names its schema for it.

NO RECEIPT IS A SKIP, AND IT SAYS SO. A tree that never adopted anything has nothing to verify, and
a skip that looks like a pass is indistinguishable from coverage. gov's own tree holds no receipt, so
that is the path this takes on gov's bar, and the fixture arms below are what give the leg a verdict
here rather than a permanent silence.
"""
import contextlib
import hashlib
import io
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile

RECEIPT = ".governance/install.json"


def read_receipt(tree):
    """The parsed receipt, or None when this tree holds none.

    Only ABSENCE returns None. A receipt that is present and does not parse raises, because the
    caller reds on it: folding a corrupt receipt into the absent case would announce a SKIP over a
    target whose record of itself is unreadable, which is the one tree that most needs a verdict.
    """
    path = tree / RECEIPT
    if not path.is_file():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def check_engine_rows(tree, rows):
    """The findings over the rows this reader owns, and the count of rows it actually graded.

    A row with NO `role` key is an engine row. That is the receipt writer's own default and the
    existing integrity reader's; taking an absent key to mean some other role would silently drop
    the entire population of any receipt that omits it, and report the result as clean.

    The count comes back so the caller can assert its own liveness. A loop that graded nothing and a
    tree that is genuinely intact produce the same empty finding list, and only this number tells
    them apart. The third value is the eol-only count: rows whose raw bytes missed and whose bytes
    through the target's clean filter are the row's `oid` (the module docstring states the rule).
    Every such candidate goes to ONE `hash-object --stdin-paths` spawn after the loop, because a
    git spawn costs ~0.75 s on a Windows node and a per-row spawn over 65 rows is most of a minute.
    """
    findings, graded = [], 0
    candidates = []  # (path, raw bytes, the receipt's sha256, the row's oid)
    for row in rows:
        if (row.get("role") or "engine") != "engine":
            continue
        path = row.get("path")
        if not path:
            findings.append("MALFORMED  an engine row carries no `path`")
            continue
        graded += 1
        found = tree / path
        if not found.is_file():
            findings.append(f"MISSING   {path} — in the receipt and not on disk")
            continue
        want = row.get("sha256")
        if not want:
            continue
        data = found.read_bytes()
        if hashlib.sha256(data).hexdigest() != want:
            candidates.append((path, data, want, row.get("oid")))

    clean, why = {}, None
    asked = [c[0] for c in candidates if c[3] and "\n" not in c[0] and "\r" not in c[0]]
    if asked:
        clean, why = resolve_clean_oids(tree, asked)
    if why:
        findings.append(f"GIT       {why} — {len(asked)} mismatched row(s) graded on raw bytes alone")
    eol_only = 0
    for path, data, want, oid in candidates:
        # `derive_blob_oid(data) != oid` IS THE TAMPER GUARD: where the filter changes nothing the
        # raw bytes ARE the blob, so a clean oid that matches means the receipt's sha256 is wrong.
        if oid and clean.get(path) == oid and derive_blob_oid(data) != oid:
            eol_only += 1
            continue
        got = hashlib.sha256(data).hexdigest()
        note = " (a path carrying a line break cannot be normalized)" if oid and path not in asked else ""
        findings.append(f"DRIFTED   {path} — receipt {want[:12]}, disk {got[:12]}{note}")
    return findings, graded, eol_only


def derive_blob_oid(data):
    """Git's SHA-1 object name for these bytes, as `git hash-object --stdin --no-filters` prints it.

    Computed, not spawned: the header is `blob <length>` and a NUL, the same rule `govkit`'s
    `blob_oid` uses. A SHA-256 repository therefore keeps the raw-bytes reading (spec §3).
    """
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def resolve_clean_oids(tree, paths):
    """`({path: oid}, None)` for each path through the tree's own clean filter, or `({}, why)`.

    ONE spawn for the whole list: `--stdin-paths` applies each path's own attributes and filters and
    prints one oid per input line, in order. No `-w`, so it writes no object. Bytes on stdin, never
    text mode: Windows text mode would turn each newline into CRLF and every path would gain a CR.

    A tree with no `.git` is refused BEFORE spawning. Outside a repository `hash-object` does not
    fail — it hashes through the HOST's global and system config, which is not the target's filter,
    and on a `core.autocrlf=true` host it would call any CRLF copy clean.
    """
    if not (tree / ".git").exists():
        return {}, f"hash-object --stdin-paths not consulted: {tree.as_posix()} holds no .git, so there is no target clean filter"
    try:
        out = subprocess.run(["git", "-C", str(tree), "hash-object", "--stdin-paths"],
                             input="".join(p + "\n" for p in paths).encode("utf-8"), capture_output=True)
    except OSError as exc:
        return {}, f"hash-object --stdin-paths could not start git: {exc}"
    oids = out.stdout.decode("utf-8", "replace").split()
    if out.returncode != 0 or len(oids) != len(paths):
        err = out.stderr.decode("utf-8", "replace").strip().splitlines()
        return {}, f"hash-object --stdin-paths refused (exit {out.returncode}): {err[-1] if err else 'no message'}"
    return dict(zip(paths, oids)), None


def print_unattributed(rows):
    """A NOTE naming how many rows `govkit update` will never grade, or silence when there are none.

    Keyed on the exact value and NEVER on the key being absent. Absence is the synthesized-row
    state and is a different reading rather than a synonym, so widening this to field-absence would
    report a number the operator's own `update` run disagrees with — and that run's withheld
    re-stamp is the thing this note exists to predict. For the same reason the count is over EVERY
    row rather than over the engine rows this file grades.

    Silent on zero, deliberately, and that silence is not a skipped arm: the loop ran and found
    nothing. A line printed on every run carries no information and trains a reader straight past
    the one run where it says something.
    """
    count = sum(1 for row in rows if row.get("evidence") == "unattributed")
    if not count:
        return
    print(f'check-receipt: NOTE - {count} row(s) carry evidence "unattributed"; '
          "govkit update will not re-stamp")
    print("check-receipt: NOTE - clear them with: "
          "govkit adopt --re-adopt --pin <path>=<rev> --write")


def write_fixture(base, name, rows, body=b"engine bytes\n", drop_file=False):
    """One fixture tree under `base`, with its receipt rows written and its engine file placed.

    The hash in a row spelled `None` is filled in from the bytes actually written, so a clean arm
    cannot pass by comparing a constant against itself.
    """
    tree = base / name
    (tree / ".governance").mkdir(parents=True)
    for row in rows:
        if not row.get("path"):
            continue
        if not drop_file:
            (tree / row["path"]).write_bytes(body)
        if row.get("sha256", "") is None:
            row["sha256"] = hashlib.sha256(body).hexdigest()
    (tree / RECEIPT).write_text(json.dumps({"schema": 3, "files": rows}), encoding="utf-8")
    return tree


def check_fixtures():
    """The built-in arms, over receipts written into a temporary directory and, for the eol-only
    rule, over real git repositories (`check_git_arms`). The `fixtures:` line prints the total.

    They run on EVERY invocation and not only under the selftest flag. In a tree that holds no
    receipt the only other behaviour of this file is an announced skip, and a leg whose sole live
    behaviour is "nothing to do here" is the could-not-fail shape — gov's own tree is permanently in
    exactly that state, so without these arms the leg would grade nothing on the bar that ships it.
    """
    results = []
    with tempfile.TemporaryDirectory() as td:
        base = pathlib.Path(td)

        tree = write_fixture(base, "clean", [{"path": "a.txt", "role": "engine", "sha256": None}])
        findings, graded, _ = check_engine_rows(tree, json.loads((tree / RECEIPT).read_text(encoding="utf-8"))["files"])
        results.append(("an intact engine row grades clean", not findings and graded == 1))

        tree = write_fixture(base, "drifted", [{"path": "a.txt", "sha256": None}])
        rows = json.loads((tree / RECEIPT).read_text(encoding="utf-8"))["files"]
        rows[0]["sha256"] = "0" + rows[0]["sha256"][1:]
        findings, graded, _ = check_engine_rows(tree, rows)
        results.append(("a drifted sha256 is reported, on a row with no role key",
                        graded == 1 and len(findings) == 1 and findings[0].startswith("DRIFTED")
                        and "a.txt" in findings[0]))

        tree = write_fixture(base, "absent", [{"path": "a.txt", "role": "engine",
                                               "sha256": "0" * 64}], drop_file=True)
        findings, graded, _ = check_engine_rows(tree, json.loads((tree / RECEIPT).read_text(encoding="utf-8"))["files"])
        results.append(("a missing file is reported as missing and not as drift",
                        graded == 1 and len(findings) == 1 and findings[0].startswith("MISSING")))

        tree = write_fixture(base, "norows", [{"path": "a.txt", "role": "seed", "sha256": "0" * 64},
                                              {"path": "b.txt", "role": "merged"}])
        findings, graded, _ = check_engine_rows(tree, json.loads((tree / RECEIPT).read_text(encoding="utf-8"))["files"])
        results.append(("a receipt of seed and merged rows alone grades nothing",
                        not findings and graded == 0))

        tree = write_fixture(base, "ungraded", [{"path": "a.txt", "evidence": "unattributed"},
                                                {"path": "b.txt", "evidence": "unattributed"},
                                                {"path": "c.txt", "evidence": "apply"},
                                                {"path": "d.txt"}])
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            print_unattributed(json.loads((tree / RECEIPT).read_text(encoding="utf-8"))["files"])
        out = buf.getvalue()
        results.append(("two `unattributed` rows count 2, with `apply` and an ABSENT field ignored",
                        "NOTE" in out and "2 row(s)" in out and "--pin" in out
                        and "--re-adopt --write" not in out))

        tree = write_fixture(base, "attributed", [{"path": "a.txt", "evidence": "apply"},
                                                  {"path": "b.txt"}])
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            print_unattributed(json.loads((tree / RECEIPT).read_text(encoding="utf-8"))["files"])
        results.append(("no `unattributed` row prints nothing at all", buf.getvalue() == ""))

    results.extend(check_git_arms())
    for label, ok in results:
        print(f"ARM {'ok  ' if ok else 'FAIL'}  {label}")
    bad = [label for label, ok in results if not ok]
    print(f"fixtures: {len(results) - len(bad)}/{len(results)} arm(s) ok")
    return len(bad)


def run_fixture_git(repo, *args):
    """One git call inside a fixture repository; a refusal raises, carrying git's own message."""
    out = subprocess.run(["git", "-C", str(repo), *args], capture_output=True)
    if out.returncode != 0:
        raise RuntimeError(f"git {args[0]} refused: {out.stderr.decode('utf-8', 'replace').strip()}")


def check_git_arms():
    """Four arms over real repositories, for the eol-only rule in the module docstring.

    Each fixture's settings are written into ITS OWN `.git/config`, never passed as `-c`: the graded
    `hash-object` spawn reads the repository's config like any git call, and local config beats a
    host's global and system values, which on a Windows node commonly set `core.autocrlf=true`.
    `safecrlf`, `gpgsign` and `hooksPath` are pinned for the same reason — a host default there
    would fail the setup rather than decide the arm. Each arm asserts it graded exactly one row, so
    an arm whose git call failed cannot pass by grading nothing, and a host where git cannot start
    fails all four with the cause named.
    """
    labels = ("(a) a CRLF copy committed LF under a later eol=lf pin grades clean, eol-only 1",
              "(b) that CRLF copy with one real byte changed is DRIFTED",
              "(c) a hand-written CRLF copy under autocrlf=false and no pin is DRIFTED",
              "(d) LF bytes that ARE the blob under a wrong sha256 are DRIFTED (the tamper half)")
    lf = b"line one\nline two\n"
    base = pathlib.Path(tempfile.mkdtemp())
    try:
        for name, autocrlf in (("pinned", "true"), ("bare", "false")):
            run_fixture_git(base, "init", "-q", name)
            with open(base / name / ".git" / "config", "a", encoding="utf-8") as fh:
                fh.write(f"[core]\n\tautocrlf = {autocrlf}\n\tsafecrlf = false\n\thooksPath = no-hooks\n"
                         "[commit]\n\tgpgsign = false\n"
                         "[user]\n\tname = check-receipt\n\temail = check-receipt@invalid\n")
        pinned, bare = base / "pinned", base / "bare"
        (pinned / "f.txt").write_bytes(lf)
        run_fixture_git(pinned, "add", "f.txt")
        run_fixture_git(pinned, "commit", "-q", "-m", "engine file, committed LF")
        (pinned / "f.txt").unlink()
        run_fixture_git(pinned, "checkout", "--", "f.txt")
        crlf = (pinned / "f.txt").read_bytes()
        if b"\r\n" not in crlf:
            raise RuntimeError("the re-checkout under autocrlf=true wrote no CR byte, so arm (a) would stage nothing")
        (pinned / ".gitattributes").write_bytes(b"f.txt text eol=lf\n")
        run_fixture_git(pinned, "add", ".gitattributes")
        run_fixture_git(pinned, "commit", "-q", "-m", "the eol=lf pin, after the checkout")
        (bare / "f.txt").write_bytes(lf.replace(b"\n", b"\r\n"))
    except (OSError, RuntimeError) as exc:
        shutil.rmtree(base, ignore_errors=True)
        return [(f"{label} — git could not build the fixture: {exc}", False) for label in labels]

    def run_grade(repo, sha=None):
        rows = [{"path": "f.txt", "sha256": sha or hashlib.sha256(lf).hexdigest(), "oid": derive_blob_oid(lf)}]
        return check_engine_rows(repo, rows)

    def check_drifted(got):
        return got[1] == 1 and got[2] == 0 and len(got[0]) == 1 and got[0][0].startswith("DRIFTED")

    got = []
    got.append((run_grade(pinned), lambda g: g == ([], 1, 1)))
    (pinned / "f.txt").write_bytes(crlf.replace(b"one", b"One", 1))
    got.append((run_grade(pinned), check_drifted))
    got.append((run_grade(bare), check_drifted))
    (pinned / "f.txt").write_bytes(lf)
    got.append((run_grade(pinned, sha=hashlib.sha256(b"not these bytes").hexdigest()), check_drifted))
    # ponytail: a leaked directory in the OS temp dir beats a red leg from a held handle on Windows.
    shutil.rmtree(base, ignore_errors=True)
    return [(label if ok(g) else f"{label} — got {g}", ok(g)) for label, (g, ok) in zip(labels, got)]


def main(argv):
    bad = check_fixtures()
    if "--selftest" in argv:
        return 1 if bad else 0

    rest = [a for a in argv if not a.startswith("-")]
    if rest:
        tree = pathlib.Path(rest[0]).resolve()
    else:
        # DERIVED from this file's own location, never spelled. A checker that names its install
        # prefix by literal lands a dead path in every tree that installed it anywhere else, and an
        # EMPTY derivation refuses rather than falling back to the working directory — grading the
        # wrong tree silently is worse than grading none.
        out = subprocess.run(["git", "-C", str(pathlib.Path(__file__).resolve().parent),
                              "rev-parse", "--show-toplevel"], capture_output=True, text=True, encoding="utf-8")
        root = out.stdout.strip()
        if out.returncode != 0 or not root:
            print("FAIL  this file is not inside a git work tree, so the tree to grade cannot be "
                  "derived; pass one as the single positional argument")
            return 2
        tree = pathlib.Path(root)

    try:
        receipt = read_receipt(tree)
    except (ValueError, UnicodeDecodeError) as exc:
        print(f"FAIL  the receipt at {(tree / RECEIPT).as_posix()} does not parse: {exc}")
        return 1

    if receipt is None:
        print(f"SKIP  no receipt at {(tree / RECEIPT).as_posix()} — the deployer installed nothing "
              f"into this tree, so there is nothing here to verify. Written as a skip and not as a "
              f"pass: a clean report over a tree this reader never examined is worth nothing.")
        return 1 if bad else 0

    rows = receipt.get("files") or []
    findings, graded, eol_only = check_engine_rows(tree, rows)
    print(f"receipt: schema {receipt.get('schema')} · {len(rows)} row(s) read · "
          f"{graded} engine row(s) graded · eol-only {eol_only}")

    if not graded:
        print("DEAD PROBE  the receipt parsed and yielded ZERO gradeable engine rows, so a clean "
              "report here would describe nothing that was looked at. Refusing to call this tree "
              "verified.")
        return 1

    for line in findings:
        print(line)
    print_unattributed(rows)
    if findings:
        n = sum(1 for line in findings if not line.startswith("GIT"))
        print(f"FAIL  {n} of {graded} graded engine row(s) no longer match the receipt")
        return 1
    print(f"ok  {graded} engine row(s) match the receipt · eol-only {eol_only}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
