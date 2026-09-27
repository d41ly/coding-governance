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
    The hash is of WORKING-TREE bytes on the machine that installed, so a clone whose end-of-line
    filters differ from that machine's reds here for any path no line-ending pin covers. That is a
    true reading rather than a defect in this file, and it is why the summary line names the
    receipt's schema: the reading is then available at the point of failure.

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
    them apart.
    """
    findings, graded = [], 0
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
        got = hashlib.sha256(found.read_bytes()).hexdigest()
        if got != want:
            findings.append(f"DRIFTED   {path} — receipt {want[:12]}, disk {got[:12]}")
    return findings, graded


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
    """The six built-in arms, over receipts written into a temporary directory.

    They run on EVERY invocation and not only under the selftest flag. In a tree that holds no
    receipt the only other behaviour of this file is an announced skip, and a leg whose sole live
    behaviour is "nothing to do here" is the could-not-fail shape — gov's own tree is permanently in
    exactly that state, so without these arms the leg would grade nothing on the bar that ships it.
    """
    results = []
    with tempfile.TemporaryDirectory() as td:
        base = pathlib.Path(td)

        tree = write_fixture(base, "clean", [{"path": "a.txt", "role": "engine", "sha256": None}])
        findings, graded = check_engine_rows(tree, json.loads((tree / RECEIPT).read_text(encoding="utf-8"))["files"])
        results.append(("an intact engine row grades clean", not findings and graded == 1))

        tree = write_fixture(base, "drifted", [{"path": "a.txt", "sha256": None}])
        rows = json.loads((tree / RECEIPT).read_text(encoding="utf-8"))["files"]
        rows[0]["sha256"] = "0" + rows[0]["sha256"][1:]
        findings, graded = check_engine_rows(tree, rows)
        results.append(("a drifted sha256 is reported, on a row with no role key",
                        graded == 1 and len(findings) == 1 and findings[0].startswith("DRIFTED")
                        and "a.txt" in findings[0]))

        tree = write_fixture(base, "absent", [{"path": "a.txt", "role": "engine",
                                               "sha256": "0" * 64}], drop_file=True)
        findings, graded = check_engine_rows(tree, json.loads((tree / RECEIPT).read_text(encoding="utf-8"))["files"])
        results.append(("a missing file is reported as missing and not as drift",
                        graded == 1 and len(findings) == 1 and findings[0].startswith("MISSING")))

        tree = write_fixture(base, "norows", [{"path": "a.txt", "role": "seed", "sha256": "0" * 64},
                                              {"path": "b.txt", "role": "merged"}])
        findings, graded = check_engine_rows(tree, json.loads((tree / RECEIPT).read_text(encoding="utf-8"))["files"])
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

    for label, ok in results:
        print(f"ARM {'ok  ' if ok else 'FAIL'}  {label}")
    bad = [label for label, ok in results if not ok]
    print(f"fixtures: {len(results) - len(bad)}/{len(results)} arm(s) ok")
    return len(bad)


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
    findings, graded = check_engine_rows(tree, rows)
    print(f"receipt: schema {receipt.get('schema')} · {len(rows)} row(s) read · "
          f"{graded} engine row(s) graded")

    if not graded:
        print("DEAD PROBE  the receipt parsed and yielded ZERO gradeable engine rows, so a clean "
              "report here would describe nothing that was looked at. Refusing to call this tree "
              "verified.")
        return 1

    for line in findings:
        print(line)
    print_unattributed(rows)
    if findings:
        print(f"FAIL  {len(findings)} of {graded} graded engine row(s) no longer match the receipt")
        return 1
    print(f"ok  {graded} engine row(s) match the receipt")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
