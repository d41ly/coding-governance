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
document and still reds when the number grows. An UNDECLARED pin means ZERO — the strictest value,
never a refusal and never off: a default that can only tighten needs no ceremony, and refusing one
cost every hygiene fixture and every freshly scaffolded adopter a red bar.

CLI: --check (gate), --report (human), --emit-pin (the current count, for re-pinning), --selftest.
"""
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corpus_ids import parse_conf  # the kit's ONE conf parser
from gen_build_index import unfenced_lines  # the kit's ONE fence reader; see scan()

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


def tree_root():
    """The tree being AUDITED, not the tree this file lives in.

    Every sibling delegate resolves it this way (gen_build_index, corpus_ids, gotchas), and the
    first cut of this module did not: it walked up from __file__, so the kit graded ITS OWN repo
    whichever tree it was pointed at — reporting this repo's row count and this repo's pinned
    duplicates, at exit 0, about somebody else's corpus. That is grammar-bound-to-the-wrong-root
    verbatim. No arm caught it because every arm passed an explicit root, so the resolver was never
    executed by the selftest at all; the arm at the bottom now shells out with a foreign cwd.
    """
    return run("git", "rev-parse", "--show-toplevel").strip()


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
    """This reader carries NO defaults and REFUSES an absent conf, unlike its four siblings.

    TOOL-aWeldedTribunal-5. The difference is deliberate and is preserved rather than smoothed away:
    the other four open with a populated defaults dict AND an `os.path.isfile` guard, so an absent
    conf yields their defaults. This one reads the file unconditionally, so an absent conf RAISES.
    Routing it through the shared parser with a guard bolted on would have converted a hard failure
    into a quiet empty-dict success -- coverage removed rather than failed closed, which is the exact
    class this unit exists to close, reintroduced by the unit closing it.

    Only the PARSE is shared. The disposition on a missing file stays this module's own.
    """
    conf = {}
    parse_conf(read(os.path.join(root, ".memory-tree.conf")), conf)
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


# Family-INDEPENDENT id shape, used only as the vacuity precondition. Deriving that precondition
# from the declared FAMILIES would assert one value against another the same call derives — the
# tautology this repo records as assertion-between-two-derived-values, and it made the
# wrong-families arm pass by finding nothing twice over.
# Written with a real string builder, never a shell heredoc: the first cut of this line carried a
# word-boundary escape that reached the file as a literal BACKSPACE byte, so the pattern compiled,
# printed correctly, and matched nothing. Only repr() showed it.
GENERIC_ID = re.compile(r"[A-Z][A-Z0-9]{1,9}-[A-Za-z0-9]+-[0-9]+[a-z]*")


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
    """-> (rows, unkeyed, dupes, loose, open_fences).

    `unkeyed` is [(path, line)] and `open_fences` is [(path, line)] — both carry LOCATIONS, because a
    bare count tells an operator a rule was broken and not where, and the duplicate branch beside them
    has always printed path and line.

    Fence handling is DELEGATED to the index generator's reader, which already strips one trailing CR,
    recognises `~~~`, and closes a fence only with the marker that opened it. This module shipped a
    private boolean toggle that did none of the three; a second fence machine in one kit is the
    two-answers class, and this one was the weaker copy.
    """
    m = conf["MEMORY_ROOT"]
    idre = id_pattern(conf)
    # A ROW leads with a dash and then an id, optionally emphasised. Anything else on the line is
    # prose and is not this check's business.
    rowre = re.compile(r"^\s*[-*]\s+[`*]*(" + idre.pattern + r")\b")
    rows = loose = 0
    unkeyed, dupes, open_fences = [], [], []
    for p in row_docs(root, m):
        seen = {}
        for n, line in unfenced_lines(read(os.path.join(root, p))):
            if line is None:          # the document ended inside a fence; n is where it opened
                open_fences.append((p, n))
                continue
            if GENERIC_ID.search(line):
                loose += 1
            mm = rowre.match(line)
            if not mm:
                # A dash-led line that carries no id at all is prose, not an unkeyed row. A line that
                # leads with a dash AND holds an id somewhere later is the shape that would silently
                # drop out of a key-merge, so it is counted.
                if re.match(r"^\s*[-*]\s+", line) and idre.search(line):
                    unkeyed.append((p, n))
                continue
            rows += 1
            seen.setdefault(mm.group(1), []).append(n)
        for i, lines in sorted(seen.items()):
            if len(lines) > 1:
                dupes.append((p, i, lines))
    return rows, unkeyed, dupes, loose, open_fences


def pin_of(conf):
    """Undeclared means ZERO — the STRICTEST value, never a refusal and never off.

    The first cut refused an undeclared pin, reasoning that omitting a key is the quietest way to
    disarm a gate. That reasoning is sound for a pin whose absence RELAXES the check and wrong for
    this one, because 0 is the strict end: a tree that never declares the key can never tolerate a
    duplicate. The refusal bought nothing and cost two real trees — every fixture in the hygiene
    self-test, and every repo scaffolded from the shipped conf example, which is the adopter breakage
    the closing review caught as a blocker. A default that can only tighten needs no ceremony.
    """
    raw = conf.get(PIN_KEY, "").strip()
    if raw == "":
        return 0
    if not raw.isdigit():
        raise Problem(f"row-grammar: {PIN_KEY} must be a non-negative integer, got '{raw}'")
    return int(raw)


def cmd_check(root, conf):
    rows, unkeyed, dupes, loose, open_fences = scan(root, conf)
    pin = pin_of(conf)
    bad = []
    if rows == 0 and loose:
        bad.append(f"check {CHECK}: {loose} line(s) under the row documents carry id-shaped text but "
                   f"NOT ONE keyed as a row — the grammar is mis-segmented. (A tree with no ids at "
                   f"all is young, not broken, and stays silent.)")
    # An open fence is checked BEFORE anything derived from the scan, because a document the reader
    # could not finish is a document whose row set is unknown — reporting "0 duplicates" over it would
    # be the silent skip this branch exists to replace.
    if open_fences:
        bad.append(f"check {CHECK}: {len(open_fences)} row document(s) end inside a fenced block that "
                   f"is never closed, so every line after it was unreadable and any duplicate below "
                   f"it is invisible:")
        for p, n in open_fences:
            bad.append(f"    {p}: fence opened at line {n} and never closed")
        # TERMINAL. The counts below are derived from a read that stopped early, so comparing
        # them against the pin would turn a partial scan into a pin instruction — "lower it to
        # N" where N omits everything the fence hid. Refuse first, count later.
        print(chr(10).join(bad))
        return 1
    if unkeyed:
        bad.append(f"check {CHECK}: {len(unkeyed)} dash-led line(s) carry an id the row grammar "
                   f"cannot key, so a key-merge would drop or duplicate them:")
        for p, n in unkeyed:
            bad.append(f"    {p}:{n}")
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


def cmd_report(root, conf):
    rows, unkeyed, dupes, loose, open_fences = scan(root, conf)
    print(f"rows keyed   : {rows}")
    print(f"unkeyed rows : {len(unkeyed)}")
    for p, n in unkeyed:
        print(f"  {p}:{n}")
    print(f"open fences  : {len(open_fences)}")
    for p, n in open_fences:
        print(f"  {p}: opened at line {n}")
    print(f"duplicates   : {len(dupes)}")
    for p, i, lines in dupes:
        print(f"  {p}: {i} at lines {', '.join(str(x) for x in lines)}")
    return 0


def cmd_emit_pin(root, conf):
    _rows, _unkeyed, dupes, _loose, open_fences = scan(root, conf)
    # A pin emitted from a partial read is worse than no pin: it is a NUMBER an operator will
    # paste into the conf, derived from a corpus the scanner could not finish reading.
    if open_fences:
        for p, n in open_fences:
            print(f"row-grammar: {p} ends inside a fence opened at line {n}; no pin is emitted "
                  f"from a partial read")
        return 1
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


def cmd_selftest():
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

    def cap(root, conf, fn=cmd_check):
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
        c5 = _tree(t5, "\n".join(["- ARCH-tOne-1 · one",
                                  "- ARCH-tOne-1 · the same id twice", ""]))
        del c5[PIN_KEY]
        # An undeclared pin is the STRICTEST value, not a refusal and not off: this fixture holds one
        # duplicate and no pin, so it must RED on the duplicate rather than on the missing key.
        arm("an undeclared pin reds on a duplicate rather than on the missing key",
            "two answers to one question", lambda: cap(t5, c5))
        # VACUITY: the wrong-grammar case must red, not pass by finding nothing.
        t6 = os.path.join(base, "wrongfam"); os.makedirs(t6)
        c6 = _tree(t6, "- ARCH-tOne-1 · one\n", families="other:OTHER")
        arm("a families list that recognises nothing reds instead of passing",
            "the grammar is mis-segmented", lambda: cap(t6, c6))
        # An id inside a fenced block is an example, not a row.
        t7 = os.path.join(base, "fenced"); os.makedirs(t7)
        c7 = _tree(t7, "- ARCH-tOne-1 · one\n\n```\n- ARCH-tOne-1 · an example in a fence\n```\n")
        arm("an id inside a fenced block is not a row", "row-grammar: clean (1 row(s)",
            lambda: cap(t7, c7))
        # ---- the delegated fence reader. The private toggle this replaced recognised neither of the
        # ---- first two shapes, and no reader in either kit had the third.
        t7b = os.path.join(base, "tildefence"); os.makedirs(t7b)
        c7b = _tree(t7b, "\n".join(["- ARCH-tOne-1 · one", "", "~~~",
                                    "- ARCH-tOne-1 · an example inside a tilde fence", "~~~", ""]))
        arm("a ~~~ fence is a fence", "row-grammar: clean (1 row(s)", lambda: cap(t7b, c7b))
        t7c = os.path.join(base, "nested"); os.makedirs(t7c)
        c7c = _tree(t7c, "\n".join(["- ARCH-tOne-1 · one", "", "~~~", "```",
                                    "- ARCH-tOne-1 · content, not a toggle", "```", "~~~", ""]))
        arm("a ``` marker inside a ~~~ block is content, not a toggle",
            "row-grammar: clean (1 row(s)", lambda: cap(t7c, c7c))
        # AC3: the fixture MUST hide a duplicate after the opener. A fixture whose unterminated fence
        # conceals nothing cannot tell "refused" from "silently skipped" — both print clean.
        t7d = os.path.join(base, "openfence"); os.makedirs(t7d)
        c7d = _tree(t7d, "\n".join(["- ARCH-tOne-1 · one", "", "```",
                                    "- ARCH-tOne-1 · a duplicate the open fence would hide", ""]))
        arm("an unterminated fence REDS instead of silently hiding the rest",
            "never closed", lambda: cap(t7d, c7d))
        arm("the unterminated fence names the line it opened on", "fence opened at line 3",
            lambda: cap(t7d, c7d))
        # [14]/[15]: the refusal must be TERMINAL in both modes — a count or a pin derived from a
        # read that stopped at an unclosed fence is a number an operator would act on.
        t7e = os.path.join(base, "openfencepin"); os.makedirs(t7e)
        c7e = _tree(t7e, chr(10).join(["- ARCH-tOne-1 . one", "", "```",
                                       "- ARCH-tOne-1 . the duplicate the pin exists for", ""]),
                    pin="1")
        arm("an open fence stops --check before any pin comparison", "TERMINAL",
            lambda: "LEAKED" if "lower it to" in cap(t7e, c7e) else "TERMINAL")
        arm("--emit-pin refuses on a partial read instead of printing a number",
            "no pin is emitted", lambda: cap(t7d, c7d, cmd_emit_pin))
        # A dash-led line holding an id the grammar cannot KEY is counted, not ignored.
        t8 = os.path.join(base, "unkeyed"); os.makedirs(t8)
        c8 = _tree(t8, "- ARCH-tOne-1 · one\n- see ARCH-tOne-9 for the rationale\n")
        arm("a dash-led line whose id is not in key position is counted unkeyed",
            "the row grammar cannot key", lambda: cap(t8, c8))
        arm("an unkeyed line is reported with its path and line, not a bare count",
            "memory/DECISIONS.md:2", lambda: cap(t8, c8))
        # AC5: --report and --emit-pin unpack scan() too; rev-1 named neither as a consumer.
        arm("--report survives the return-shape change", "open fences  : 0",
            lambda: cap(t, c, cmd_report))
        arm("--emit-pin survives the return-shape change", f'{PIN_KEY}="0"',
            lambda: cap(t, c, cmd_emit_pin))

        # THE ARM THE FIRST CUT DID NOT HAVE. Every arm above passes an explicit root, so none of
        # them executes the resolver — which is exactly how this module shipped a review blocker:
        # it walked up from __file__ and graded the KIT's repo whichever tree it was pointed at,
        # reporting this repo's counts at exit 0 about a foreign corpus. An arm that cannot reach
        # the resolver cannot see that, so this one SHELLS OUT with a foreign cwd.
        t9 = os.path.join(base, "foreign"); os.makedirs(t9)
        _tree(t9, "\n".join(["- ARCH-tOne-1 · one",
                             "- ARCH-tOne-1 · the same id twice", ""]), pin="0")
        def _foreign():
            r = subprocess.run([sys.executable, os.path.abspath(__file__), "--check"],
                               cwd=t9, capture_output=True, text=True)
            return f"rc={r.returncode} {r.stdout}{r.stderr}"
        arm("--check grades the tree it is RUN IN, not the tree the kit lives in",
            "two answers to one question", _foreign)

    if fails:
        print(f"FAIL — {len(fails)} arm(s) failed")
        return 1
    print("PASS — row_grammar: all arms held")
    return 0


def main(argv):
    mode = argv[1] if len(argv) > 1 else "--check"
    if mode == "--selftest":
        return cmd_selftest()
    try:
        root = tree_root()
    except Problem:
        print("row-grammar: not a git repo")
        return 2
    conf = load_conf(root)
    if mode == "--check":
        return cmd_check(root, conf)
    if mode == "--report":
        return cmd_report(root, conf)
    if mode == "--emit-pin":
        return cmd_emit_pin(root, conf)
    print(f"row-grammar: unknown argument '{mode}'; the modes are --check, --report, --emit-pin "
          f"and --selftest")
    return 2


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except Problem as exc:
        print(str(exc))
        sys.exit(1)
