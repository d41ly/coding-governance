#!/usr/bin/env python3
"""Check 20 — the row documents' grammar, and the id collisions inside one file.

WHY THIS EXISTS, and why it is NOT a keyability check. The obvious assertion — "every row in every
row document parses" — is a check that CANNOT FAIL on this corpus: measured, 137 of 137 rows key,
and the merge driver already guarantees the property at merge time, where it can actually be
violated. A second answer to a question another gate already answers is this repo's
`two-answers-to-one-question` class, and a check with no reachable failure is
`fixture-passes-by-finding-nothing`. So keyability is kept only as the CHEAP PRECONDITION that makes
the real assertion meaningful (an id the grammar stopped recognising drops silently out of both), and
the assertion this check exists for is UNIQUENESS WITHIN A FILE.

That half has measured live violations and nothing else on the bar can see them: hygiene check 13's
collision scan is scoped to build folders, check 8 does not cover the decision index, and the merge
driver's duplicate guard is merge-time only — both live collisions arrived by ordinary
single-parent commits, so no merge ever inspected them.

SCOPE IS PER FILE, DELIBERATELY. Corpus-wide uniqueness would red 19 ids on day one, every one of
them the designed backlog-row-plus-decision-row pair, and would need a 19-row waiver — the exact
shape `corpus_ids.py` refused in writing for the same reason. Per-file has two violations, both in
the live decision index. NAMED GAP: the live index and its rotated archive are two files by design,
so a row that rotates out and is re-minted is not caught here; the all-time collision grep the
decision index's own header prescribes is what covers that.

THE PIN IS A COUNT, NOT A REGISTRY. A membership list would put the offending ids in a second place
and let a deletion there pass unnoticed; a shrink-only count keeps the names single-sourced in the
document and still reds when the number grows. An UNDECLARED pin is its own refusal, because
omitting the key is the quietest way to disarm a gate.

CLI: --check (gate), --report (human), --emit-pin (the current count, for re-pinning), --selftest.
"""
import os
import re
import subprocess
import sys

CHECK = 20
PIN_KEY = "ROW_DUPLICATE_PIN"


class Problem(Exception):
    """A named, user-facing failure. Never a traceback."""


def run(*argv, cwd=None):
    p = subprocess.run(argv, cwd=cwd, capture_output=True, text=True)
    if p.returncode != 0:
        raise Problem(f"row-grammar: `{' '.join(argv)}` failed: {p.stderr.strip()}")
    return p.stdout


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def resolve_root(start=None):
    """Walk up for the conf, bounded by .git — the kit must work at any install prefix."""
    here = os.path.abspath(start or os.path.dirname(__file__))
    while True:
        if os.path.isfile(os.path.join(here, ".memory-tree.conf")):
            return here
        parent = os.path.dirname(here)
        if parent == here or os.path.exists(os.path.join(here, ".git")):
            raise Problem("row-grammar: no .memory-tree.conf found walking up from the kit")
        here = parent


def load_conf(root):
    conf = {}
    for line in read(os.path.join(root, ".memory-tree.conf")).split("\n"):
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        conf[k.strip()] = v.strip().strip('"').strip("'")
    return conf


def id_pattern(conf):
    """Built from the DECLARED families, so this module and the index generator read one source.

    The recall kit's grammar is deliberately NOT imported: it is an optional sibling, and reaching it
    would make it a hard prerequisite of every hygiene run — the coupling unit 1 removed for exactly
    this reason. The family alternation is declared in this kit's own conf, so both consumers derive
    from one declaration rather than one copying the other.
    """
    fams = [p.split(":")[1] for p in conf.get("FAMILIES", "").split() if ":" in p]
    if not fams:
        raise Problem("row-grammar: FAMILIES is empty, so no row could be recognised and this check "
                      "would pass by finding nothing")
    # The sequence admits a REVISION SUFFIX (`-9b`), because a revision row is a row: it occupies a
    # line, carries a key and must survive a key-merge. This is deliberately WIDER than the roster
    # derivation in the index generator, which excludes the same shape — a roster answers "which ids
    # belong to this build", where an amendment is not a member, and this answers "what is on this
    # line", where it is. Two questions, two predicates, stated here so the difference is not read as
    # drift. Without the suffix the numeric prefix matches inside a revision id and 42 real archive
    # rows report as unkeyable.
    return re.compile(r"(?:" + "|".join(sorted(re.escape(f) for f in fams)) + r")-[A-Za-z0-9]+-\d+[a-z]*")


def row_docs(root, m):
    """Every row-shaped document: the live index, the backlog shards, and the rotated archives."""
    tracked = [p for p in run("git", "ls-files", "--", m + "/", cwd=root).split("\n") if p]
    keep = []
    for p in tracked:
        base = os.path.basename(p)
        if p == f"{m}/DECISIONS.md" or p.startswith(f"{m}/backlog/"):
            keep.append(p)
        elif p.startswith(f"{m}/archive/") and base.startswith("DECISIONS.") and base.endswith(".md"):
            keep.append(p)
    return sorted(keep)


def scan(root, conf):
    """-> (rows, unkeyed, dupes) where dupes is [(path, id, [line numbers])]."""
    m = conf["MEMORY_ROOT"]
    idre = id_pattern(conf)
    # A ROW leads with a dash and then an id, optionally emphasised. Anything else on the line is
    # prose and is not this check's business.
    rowre = re.compile(r"^\s*[-*]\s+[`*]*(" + idre.pattern + r")\b")
    rows = unkeyed = 0
    dupes = []
    for p in row_docs(root, m):
        seen = {}
        in_fence = False
        for n, line in enumerate(read(os.path.join(root, p)).split("\n"), 1):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            mm = rowre.match(line)
            if not mm:
                # A dash-led line that carries no id at all is prose, not an unkeyed row. A line that
                # leads with a dash AND holds an id somewhere later is the shape that would silently
                # drop out of a key-merge, so it is counted.
                if re.match(r"^\s*[-*]\s+", line) and idre.search(line):
                    unkeyed += 1
                continue
            rows += 1
            seen.setdefault(mm.group(1), []).append(n)
        for i, lines in sorted(seen.items()):
            if len(lines) > 1:
                dupes.append((p, i, lines))
    return rows, unkeyed, dupes


def pin_of(conf):
    raw = conf.get(PIN_KEY, "").strip()
    if raw == "":
        raise Problem(
            f"row-grammar: {PIN_KEY} is not declared in .memory-tree.conf. An undeclared pin is not "
            f"a disabled check — omitting the key is the quietest way to disarm a gate, so it is a "
            f"refusal. Set it to the count `--emit-pin` reports."
        )
    if not raw.isdigit():
        raise Problem(f"row-grammar: {PIN_KEY} must be a non-negative integer, got '{raw}'")
    return int(raw)


def do_check(root, conf):
    rows, unkeyed, dupes = scan(root, conf)
    pin = pin_of(conf)
    bad = []
    if rows == 0:
        bad.append(f"check {CHECK}: no row parsed in any row document — the grammar recognises "
                   f"nothing, and recognising nothing is what a CLEAN corpus also looks like")
    if unkeyed:
        bad.append(f"check {CHECK}: {unkeyed} dash-led line(s) carry an id the row grammar cannot "
                   f"key, so a key-merge would drop or duplicate them")
    if len(dupes) > pin:
        bad.append(f"check {CHECK}: {len(dupes)} id(s) appear more than once within one row document "
                   f"(pin {pin}, shrink-only) — an index that answers to one id twice has two "
                   f"answers to one question:")
        for p, i, lines in dupes:
            bad.append(f"    {p}: {i} at lines {', '.join(str(x) for x in lines)}")
    elif len(dupes) < pin:
        bad.append(f"check {CHECK}: {PIN_KEY} is {pin} but only {len(dupes)} duplicate(s) remain — "
                   f"the pin is shrink-only, so lower it to {len(dupes)} to lock the repair in")
    if bad:
        print("\n".join(bad))
        return 1
    print(f"row-grammar: clean ({rows} row(s) across the row documents, {len(dupes)} pinned duplicate(s))")
    return 0


def do_report(root, conf):
    rows, unkeyed, dupes = scan(root, conf)
    print(f"rows keyed   : {rows}")
    print(f"unkeyed rows : {unkeyed}")
    print(f"duplicates   : {len(dupes)}")
    for p, i, lines in dupes:
        print(f"  {p}: {i} at lines {', '.join(str(x) for x in lines)}")
    return 0


def do_emit_pin(root, conf):
    _rows, _unkeyed, dupes = scan(root, conf)
    print(f'{PIN_KEY}="{len(dupes)}"')
    return 0


# ----------------------------------------------------------------------------------------- selftest
def _tree(tmp, decisions, *, families="arch:ARCH", pin="0"):
    run("git", "init", "-q", ".", cwd=tmp)
    run("git", "config", "user.email", "t@t.test", cwd=tmp)
    run("git", "config", "user.name", "t", cwd=tmp)
    with open(os.path.join(tmp, ".memory-tree.conf"), "w", encoding="utf-8") as fh:
        fh.write(f'MEMORY_ROOT=memory\nFAMILIES="{families}"\n{PIN_KEY}="{pin}"\n')
    os.makedirs(os.path.join(tmp, "memory", "backlog"), exist_ok=True)
    with open(os.path.join(tmp, "memory", "DECISIONS.md"), "w", encoding="utf-8") as fh:
        fh.write(decisions)
    run("git", "add", "-A", cwd=tmp)
    run("git", "commit", "-q", "-m", "f", "--no-verify", cwd=tmp)
    return load_conf(tmp)


def do_selftest():
    import tempfile
    fails = []

    def arm(label, want, fn):
        try:
            got = fn()
        except Problem as exc:
            got = str(exc)
        except Exception as exc:  # noqa: BLE001 — a traceback here IS the finding
            got = f"UNEXPECTED {type(exc).__name__}: {exc}"
        if want in str(got):
            print(f"arm ok    {label}")
        else:
            fails.append(label)
            print(f"arm FAIL  {label} — expected to see: {want}\n      got: {got}")

    def cap(root, conf, fn=do_check):
        import io
        from contextlib import redirect_stdout
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = fn(root, conf)
        return f"rc={rc} " + buf.getvalue()

    with tempfile.TemporaryDirectory() as base:
        # POSITIVE: a clean corpus passes and says how much it looked at.
        t = os.path.join(base, "clean"); os.makedirs(t)
        c = _tree(t, "- ARCH-tOne-1 · one\n- ARCH-tOne-2 · two\n")
        arm("a clean corpus passes and reports its population", "row-grammar: clean (2 row(s)",
            lambda: cap(t, c))
        # NEGATIVE: the assertion this check exists for.
        t2 = os.path.join(base, "dupe"); os.makedirs(t2)
        c2 = _tree(t2, "- ARCH-tOne-1 · one\n- ARCH-tOne-1 · one again, different text\n")
        arm("a duplicate id within one file is named, with both line numbers",
            "two answers to one question", lambda: cap(t2, c2))
        arm("the duplicate's id and lines are printed", "ARCH-tOne-1 at lines 1, 2",
            lambda: cap(t2, c2))
        # The pin admits a known duplicate, and shrink-only bites in the other direction too.
        t3 = os.path.join(base, "pinned"); os.makedirs(t3)
        c3 = _tree(t3, "- ARCH-tOne-1 · one\n- ARCH-tOne-1 · again\n", pin="1")
        arm("a pinned duplicate passes", "row-grammar: clean", lambda: cap(t3, c3))
        t4 = os.path.join(base, "stale"); os.makedirs(t4)
        c4 = _tree(t4, "- ARCH-tOne-1 · one\n", pin="1")
        arm("a pin above the real count reds, so a repair must lower it",
            "the pin is shrink-only", lambda: cap(t4, c4))
        # An UNDECLARED pin is a refusal, not a disabled check.
        t5 = os.path.join(base, "nopin"); os.makedirs(t5)
        c5 = _tree(t5, "- ARCH-tOne-1 · one\n")
        del c5[PIN_KEY]
        arm("an undeclared pin is a refusal", "is not declared in .memory-tree.conf",
            lambda: cap(t5, c5))
        # VACUITY: the wrong-grammar case must red, not pass by finding nothing.
        t6 = os.path.join(base, "wrongfam"); os.makedirs(t6)
        c6 = _tree(t6, "- ARCH-tOne-1 · one\n", families="other:OTHER")
        arm("a families list that recognises nothing reds instead of passing",
            "recognising nothing is what a CLEAN corpus also looks like", lambda: cap(t6, c6))
        # An id inside a fenced block is an example, not a row.
        t7 = os.path.join(base, "fenced"); os.makedirs(t7)
        c7 = _tree(t7, "- ARCH-tOne-1 · one\n\n```\n- ARCH-tOne-1 · an example in a fence\n```\n")
        arm("an id inside a fenced block is not a row", "row-grammar: clean (1 row(s)",
            lambda: cap(t7, c7))
        # A dash-led line holding an id the grammar cannot KEY is counted, not ignored.
        t8 = os.path.join(base, "unkeyed"); os.makedirs(t8)
        c8 = _tree(t8, "- ARCH-tOne-1 · one\n- see ARCH-tOne-9 for the rationale\n")
        arm("a dash-led line whose id is not in key position is counted unkeyed",
            "the row grammar cannot key", lambda: cap(t8, c8))

    if fails:
        print(f"FAIL — {len(fails)} arm(s) failed")
        return 1
    print("PASS — row_grammar: all arms held")
    return 0


def main(argv):
    mode = argv[1] if len(argv) > 1 else "--check"
    if mode == "--selftest":
        return do_selftest()
    root = resolve_root()
    conf = load_conf(root)
    if mode == "--check":
        return do_check(root, conf)
    if mode == "--report":
        return do_report(root, conf)
    if mode == "--emit-pin":
        return do_emit_pin(root, conf)
    print(f"row-grammar: unknown argument '{mode}'; the modes are --check, --report, --emit-pin "
          f"and --selftest")
    return 2


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except Problem as exc:
        print(str(exc))
        sys.exit(1)
