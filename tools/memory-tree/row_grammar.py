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
# Check 24 rides this module for the same reason 13-20 do: it walks ROW DOCUMENTS, and the row
# grammar lives here. TOOL-cSpliceWarden-6.
ROTATION_CHECK = 24
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


def derive_families(conf):
    """The DECLARED family tokens. One derivation, read by `id_pattern` and by `row_docs`.

    Lifted out when `row_docs` grew its second consumer: two copies of one split is the
    two-answers-to-one-question class, and this one would have drifted silently — a family added to
    the conf would have joined the id grammar and NOT the document set, so its rotated archive would
    have gone unscanned while every row in it still keyed.
    """
    fams = []
    for p in conf.get("FAMILIES", "").split():
        # REFUSED, never dropped, and the shell refuses the same token for the same reason. The two
        # derivations are different expressions over one declaration, so a malformed token is where
        # they diverge: `nocolon` is dropped by both, but `spare:` is dropped by the shell's `*:?*`
        # case and kept HERE as an empty string, which renders an empty alternation branch that
        # matches `.2026-01-01.md`. Refusing is what makes the two agree by construction.
        head, sep, tail = p.partition(":")
        if not sep or not tail:
            raise Problem(f"row-grammar: FAMILIES token '{p}' is not <discipline>:<FAMILY> with a "
                          f"non-empty family; this module and check 10 derive the family set by "
                          f"different expressions and would select different archives from it")
        fams.append(tail)
    if not fams:
        raise Problem("row-grammar: FAMILIES is empty, so no row could be recognised and this check "
                      "would pass by finding nothing")
    return fams


def id_pattern(conf):
    """Built from the DECLARED families, so this module and the index generator read one source.

    The recall kit's grammar is deliberately NOT imported: it is an optional sibling, and reaching it
    would make it a hard prerequisite of every hygiene run — the coupling unit 1 removed for exactly
    this reason. The family alternation is declared in this kit's own conf, so both consumers derive
    from one declaration rather than one copying the other.
    """
    fams = derive_families(conf)
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


# A rotated archive, by the name of the document it ROTATED: `<STEM>.<iso-date><suffix?>.md`, flat.
# The date half and the STEM half are a conjunction and each carries the other's weight — the date
# keeps a family-named file that is not a rotation out, the stem keeps a dated file that is not a row
# document out. The optional trailing `[a-z0-9]*` is a same-day DISAMBIGUATOR: two builds rotated to
# one date on 2026-08-17 and the second is `TOOL.2026-08-17b.md`.
#
# ONE FULLMATCH, not startswith-plus-search. The first cut tested the stem with `startswith` and the
# date with `search`, which admits a date ANYWHERE after the stem: `TOOL.notes.2026-01-01.md` passed
# here and was refused by check 10, whose ERE anchors the date immediately after the stem's dot. Two
# readers of one rule that disagree on a real filename is the defect the cross-reader arm exists to
# catch, and it missed this one because its fixture held no such name — so the fixture now does.
# Built from the declared stems so it is the same conjunction the shell spells, in the same order.
def build_rotated_re(conf):
    stems = "|".join(re.escape(x) for x in ["DECISIONS"] + derive_families(conf))
    return re.compile(r"(?:" + stems + r")\.[0-9]{4}-[0-9]{2}-[0-9]{2}[a-z0-9]*\.md\Z")


def row_docs(root, m, conf):
    """Every row-shaped document: the live index, the backlog shards, and the rotated archives.

    An archive is a ROTATION of one of those documents, so it is recognised by the name of the
    document it rotated — `DECISIONS` or a DECLARED family. The first cut kept only the `DECISIONS.`
    prefix, which left every rotated BACKLOG shard unscanned: measured at the widening, three files
    and 161 rows, carrying two duplicated ids that had been invisible to the bar since the day the
    archive holding them was written.

    NOT "every .md under archive/". That sweeps in the frozen charter snapshots and the retired
    ledger shards, which are prose. They contribute no keyed rows today, so the naive widening looks
    harmless — measured, it moves the row count by nothing and the `loose` count by seven — but a
    quoted example row inside one would red the `unkeyed` branch on a file nobody is permitted to
    edit, and the only remedy would be to edit it.

    The family set is DECLARED rather than derived from the tree, deliberately: resolving an
    archive's stem against a live index would mean that deleting a shard silently removes its
    archives from the scan, which is the vacuity class this module exists to avoid. Check 10 DOES
    resolve, because its question is "which index should name this"; this one's question is "is this
    a row document", and a declared answer cannot narrow behind your back.
    """
    tracked = [p for p in run("git", "ls-files", "--", m + "/", cwd=root).split("\n") if p]
    rot = build_rotated_re(conf)
    keep = []
    for p in tracked:
        base = os.path.basename(p)
        if p == f"{m}/DECISIONS.md" or p.startswith(f"{m}/backlog/"):
            keep.append(p)
        elif p.startswith(f"{m}/archive/") and "/" not in p[len(f"{m}/archive/"):]:
            if rot.match(base):
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
    for p in row_docs(root, m, conf):
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


# The lifecycle vocabulary is the index generator's, imported rather than retyped: it is the single
# source check 8 already reads, and a second copy here would be the two-answers class inside the
# module that exists to stop it. Retyping it is also what let the first cut read the prose words
# `ONE`, `S`, `W` and `CORRECTS` as status tokens in a decision archive.
from gen_build_index import STATUS_TOKENS, TERMINAL as TERMINAL_STATUS


def check_rotation(root, conf):
    """-> (findings, graded, mode). Does this tree HONOUR its declared ROTATION_MODE?

    Under `cut` an id sits in exactly ONE file, so a rotated archive owes two things: every row in it
    is terminal, and none of its ids is also in the live index it was cut from. Those two together
    are what `cut` means.

    Under `snapshot` the overlap is legal by construction and the assertion inverts to "an archived
    row is never edited after the rotation" — a git-history property whose baseline is the commit
    that ADDED the archive. That baseline is NOT resolvable here and the measurement is recorded
    rather than assumed: `git log --diff-filter=A` returns EMPTY for two of this repo's four
    archives, because a rotation lands inside a MERGE and only `git log -m` sees it; the plain,
    `--full-history` and `-m` spellings disagree on a third; and `git log ""..HEAD -- <path>` exits 0
    printing nothing, so an unresolved baseline reports a clean archive. An arm that cannot find its
    own starting point and says so by staying silent is the reassuring zero this kit refuses. The
    mode is ANNOUNCED as ungraded instead, on every run.
    """
    m = conf["MEMORY_ROOT"]
    mode = conf.get("ROTATION_MODE", "").strip()
    idre = id_pattern(conf)
    rowre = re.compile(r"^\s*[-*]\s+[`*]*(" + idre.pattern + r")\b")
    statusre = re.compile(r"^\s*[-*]\s+[`*]*" + idre.pattern + r"[`*]*\s*·\s*("
                          + "|".join(STATUS_TOKENS) + r")\b")
    docs = row_docs(root, m, conf)
    archives = [p for p in docs if p.startswith(f"{m}/archive/")]
    live = [p for p in docs if not p.startswith(f"{m}/archive/")]
    if mode not in ("cut", "snapshot"):
        return ([f"check {ROTATION_CHECK}: ROTATION_MODE is UNDECLARED, so nothing grades what a "
                 f"rotation means in this tree. {len(archives)} rotated archive(s) are ungraded. "
                 f"Declare `cut` or `snapshot` in .memory-tree.conf to turn this check on."], 0, mode)
    if mode == "snapshot":
        return ([f"check {ROTATION_CHECK}: ROTATION_MODE is `snapshot`, which this engine does NOT "
                 f"grade — see check_rotation's docstring for the measurement. {len(archives)} "
                 f"rotated archive(s) are ungraded, and nothing here says your archives are "
                 f"faithful."], 0, mode)

    bad = []
    for a in archives:
        stem = os.path.basename(a).split(".")[0]
        idx = [p for p in live if os.path.basename(p) == f"{stem}.md"]
        # A shard under backlog/ carries a lifecycle token per row; the decision index does not.
        status_bearing = bool(idx) and idx[0].startswith(f"{m}/backlog/")
        rows, ids = [], set()
        for n, line in unfenced_lines(read(os.path.join(root, a))):
            if line is None:
                continue                      # check 20 owns the unterminated-fence refusal
            mm = rowre.match(line)
            if not mm:
                continue
            ids.add(mm.group(1))
            st = statusre.match(line)
            rows.append((n, mm.group(1), st.group(1) if st else None))
        # (a) TERMINAL ONLY. A row whose status this cannot READ is NOT counted terminal — it is a
        # row the check could not grade, and a skip that looks like a pass is not coverage.
        nonterm = [r for r in rows if r[2] is not None and r[2] not in TERMINAL_STATUS]
        ungraded = [r for r in rows if r[2] is None] if status_bearing else []
        if not status_bearing:
            # A decision row carries no lifecycle token, so "terminal only" is vacuously true here
            # and asserting it is a category error — this build's forensics record says so. The
            # EXCLUSIVITY half below still applies, and is where a decision id duplicated between
            # the index and its archive would surface.
            nonterm = []
        if nonterm:
            bad.append(f"    {a}: {len(nonterm)} non-terminal row(s) in a `cut` archive — under cut a "
                       f"non-terminal row stays in the live index and never rotates: "
                       + ", ".join(f"{r[1]} ({r[2]}) at line {r[0]}" for r in nonterm[:6]))
        if ungraded:
            bad.append(f"    {a}: {len(ungraded)} row(s) carry no readable status token, so this check "
                       f"could not grade them either way: "
                       + ", ".join(f"{r[1]} at line {r[0]}" for r in ungraded[:6]))
        # (b) EXCLUSIVITY. One id, one file.
        if len(idx) != 1:
            bad.append(f"    {a}: stem '{stem}' resolves to {len(idx)} live index(es), so the "
                       f"exclusivity half was NOT graded for it (check 10 reports the resolution)")
            continue
        live_ids = {mm.group(1) for _n, line in unfenced_lines(read(os.path.join(root, idx[0])))
                    if line is not None and (mm := rowre.match(line))}
        both = sorted(ids & live_ids)
        if both:
            bad.append(f"    {a}: {len(both)} id(s) also live in {idx[0]}, so the pair does not "
                       f"partition the family: " + " ".join(both[:8]))
    return (bad, len(archives), mode)


def cmd_check_rotation(root, conf):
    findings, graded, mode = check_rotation(root, conf)
    if mode not in ("cut",):
        print(findings[0])
        return 0
    if findings:
        print(f"check {ROTATION_CHECK}: the declared ROTATION_MODE is `cut` and this tree does not "
              f"honour it — an id must sit in exactly ONE file:")
        print("\n".join(findings))
        return 1
    # ANTI-VACUITY. A clean verdict over zero archives is the reassuring zero this kit refuses, in
    # the check whose whole subject is a population that may legitimately be empty.
    if graded == 0:
        print(f"rotation-mode: `cut` declared and NO rotated archive exists yet — this check graded "
              f"NOTHING, and a green verdict here is coverage of nothing.")
        return 0
    print(f"rotation-mode: clean (`cut`, {graded} rotated archive(s): terminal-only and disjoint "
          f"from their live indexes)")
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
def _tree(tmp, decisions, *, families="arch:ARCH", pin="0", archives=None, shards=None):
    run("git", "init", "-q", ".", cwd=tmp)
    run("git", "config", "user.email", "t@t.test", cwd=tmp)
    run("git", "config", "user.name", "t", cwd=tmp)
    with open(os.path.join(tmp, ".memory-tree.conf"), "w", encoding="utf-8") as fh:
        fh.write(f'MEMORY_ROOT=memory\nFAMILIES="{families}"\n{PIN_KEY}="{pin}"\n')
    os.makedirs(os.path.join(tmp, "memory", "backlog"), exist_ok=True)
    with open(os.path.join(tmp, "memory", "DECISIONS.md"), "w", encoding="utf-8") as fh:
        fh.write(decisions)
    # A live shard, so an archive has an index to be resolved against and to be DISJOINT from.
    for name, body in (shards or {}).items():
        with open(os.path.join(tmp, "memory", "backlog", name), "w", encoding="utf-8") as fh:
            fh.write(body)
    # ARCHIVES ARE WRITTEN BEFORE `git add -A`, and that ordering is load-bearing rather than tidy:
    # `row_docs` enumerates through `git ls-files`, so a fixture staged afterwards is invisible and
    # every arm over it would pass by finding nothing — this module's own vacuity class.
    for name, body in (archives or {}).items():
        dest = os.path.join(tmp, "memory", "archive", name)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as fh:
            fh.write(body)
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

        # THE WIDENING (TOOL-cSpliceWarden-3). The archive branch admitted a file only when its
        # basename began `DECISIONS.`, so every rotated BACKLOG shard went unscanned — three of them
        # in this kit's own dogfood repo, one carrying two duplicated ids past a green bar for a
        # month. The duplicate below uses an id the live index does NOT carry, so a red can only have
        # come from the archive file itself.
        t10 = os.path.join(base, "archivedupe"); os.makedirs(t10)
        c10 = _tree(t10, "- ARCH-tOne-1 · one\n",
                    archives={"ARCH.2026-01-01.md": "- ARCH-tTwo-1 · a rotated row\n"
                                                    "- ARCH-tTwo-1 · the same id again\n"})
        arm("a duplicate inside a rotated BACKLOG archive is found, not skipped",
            "two answers to one question", lambda: cap(t10, c10))
        arm("the rotated backlog archive is named with its lines",
            "memory/archive/ARCH.2026-01-01.md: ARCH-tTwo-1 at lines 1, 2", lambda: cap(t10, c10))

        # THE SCOPE NEGATIVE, which is what pins the narrow predicate against the naive one. "Every
        # .md under archive/" would sweep in frozen snapshots and retired shards; a quoted example
        # row inside one would then red the unkeyed branch on a file nobody is permitted to edit, and
        # the only remedy would be to edit it. Three shapes are refused here: a name with no date, a
        # date whose stem is not a declared family, and a file nested below archive/.
        t11 = os.path.join(base, "archivescope"); os.makedirs(t11)
        c11 = _tree(t11, "- ARCH-tOne-1 · one\n",
                    archives={"playbook-v-2-0.md": "- ARCH-tNope-1 · quoted in a frozen snapshot\n"
                                                   "- ARCH-tNope-1 · and quoted twice\n",
                              "NOTAFAMILY.2026-01-01.md": "- ARCH-tNope-2 · dated, wrong stem\n"
                                                          "- ARCH-tNope-2 · twice\n",
                              # The date must sit IMMEDIATELY after the stem's dot. This name has the
                              # right stem and a date further along, and the two readers split on it
                              # until the Python side became one anchored fullmatch.
                              "ARCH.notes.2026-01-01.md": "- ARCH-tNope-4 · a date, but not a rotation\n"
                                                          "- ARCH-tNope-4 · twice\n",
                              os.path.join("ledger", "a.md"): "- ARCH-tNope-3 · a retired shard\n"
                                                              "- ARCH-tNope-3 · twice\n",
                              # THE POSITIVE. Without one that MUST be selected, both readers
                              # returning nothing is "agreement", and the arm passes over a predicate
                              # that selects nothing at all.
                              "ARCH.2026-02-02.md": "- ARCH-tYes-1 · a real rotation, selected\n",
                              # THE SAME-DAY DISAMBIGUATOR, which nothing else exercises: delete
                              # `[a-z0-9]*` from either reader and every other arm stays green.
                              # `TOOL.2026-08-17b.md` in the dogfood repo is why it exists.
                              "ARCH.2026-02-02b.md": "- ARCH-tYes-2 · the second rotation of one day\n"})
        arm("a frozen non-row file under archive/ is NOT scanned, and a same-day disambiguated one IS",
            "row-grammar: clean (3 row(s)", lambda: cap(t11, c11))

        # THE TWO READERS OF ONE RULE. check 10 in check-memory-hygiene.sh enumerates the same set in
        # shell; this module does it in Python. Neither can import the other, so the rule would be
        # two copies free to drift — and the drift is silent in the worst direction, since a narrower
        # Python side simply scans less and still prints a clean count. The shell PRINTS its ERE and
        # this arm asserts the two agree over a tree holding one of every shape.
        def resolve_shell_ere(sh, cwd):
            """The shell's own ERE, or None. Every candidate is RUN — being on PATH is not evidence.

            On Windows `bash` resolves to the WSL launcher, which tries to boot a VM and returns
            UTF-16 "the timeout period expired" at rc=1. That is the MS-Store-python3 shape one
            interpreter over, and it is why this probes rather than assuming.
            """
            cands = [os.environ.get("GOV_BASH", ""), "bash",
                     "C:/Program Files/Git/bin/bash.exe", "/bin/bash", "sh"]
            for c in cands:
                if not c:
                    continue
                try:
                    r = subprocess.run([c, sh, "--print-rotated-archive-ere"], cwd=cwd,
                                       capture_output=True, text=True, timeout=60)
                except (OSError, subprocess.TimeoutExpired):
                    continue
                if r.returncode != 0:
                    continue
                out = [l for l in (r.stdout or "").strip().split("\n") if l.strip()]
                # The print modes sit below an observability echo, so the ERE is the LAST line.
                if out and out[-1].startswith("^"):
                    return out[-1]
            return None

        def check_readers_agree():
            sh = os.path.join(os.path.dirname(os.path.abspath(__file__)), "check-memory-hygiene.sh")
            if not os.path.isfile(sh):
                return ("JOIN-OK SKIPPED — check-memory-hygiene.sh is not installed beside this "
                        "module, so the two readers were NOT compared and nothing here asserts they "
                        "agree")
            ere = resolve_shell_ere(sh, t11)
            if ere is None:
                # PRINTED, not merely returned. `arm()` prints the label alone on success, so a skip
                # returned as a passing value is indistinguishable from a verified one — which is the
                # whole objection to a silent skip.
                print("arm SKIP  the cross-reader join did NOT run: no candidate shell executed "
                      "`--print-rotated-archive-ere` on this node. The two readers were NOT compared. "
                      "Set GOV_BASH to a usable bash to exercise it.")
                return ("JOIN-OK SKIPPED — announced above; this arm verified nothing")
            rx = re.compile(ere.replace("$M", "memory"))
            tracked = [x for x in run("git", "ls-files", "--", "memory/", cwd=t11).split("\n") if x]
            shell_set = sorted(x for x in tracked if rx.search(x))
            py_set = sorted(x for x in row_docs(t11, "memory", c11) if x.startswith("memory/archive/"))
            if shell_set != py_set:
                return f"DISAGREE shell={shell_set} python={py_set}"
            # ANTI-VACUITY, and it is the whole value of this arm. Two readers that both select
            # NOTHING agree, and so do two that are both broken. The fixture holds names that must be
            # selected and names that must not, so the comparison is checked against a tree whose
            # answer is known rather than merely equal on both sides.
            if not py_set:
                return ("VACUOUS — both readers selected NOTHING, so the agreement says only that two "
                        "predicates are equally silent; the fixture must hold a selectable archive")
            if len(py_set) == len(tracked):
                return ("VACUOUS — both readers selected EVERY tracked file, so nothing was "
                        "discriminated")
            return f"JOIN-OK AGREE (both selected {sorted(py_set)} of {len(tracked)} tracked files)"
        arm("check 10's shell enumeration and row_docs() select the same archives",
            "JOIN-OK", check_readers_agree)

        # CHECK 24 — the declared ROTATION_MODE, every branch. TOOL-cSpliceWarden-6.
        # The clean case first, so the reds below are known to be reds and not a broken fixture.
        t24 = os.path.join(base, "rotcut"); os.makedirs(t24)
        c24 = _tree(t24, "- ARCH-tOne-1 · one\n", pin="0",
                    shards={"ARCH.md": "- ARCH-tLive-1 · OPEN · the live row\n"},
                    archives={"ARCH.2026-01-01.md": "- ARCH-tGone-1 · CLOSED · a terminal row, cut-legal\n"})
        _conf24 = dict(c24); _conf24["ROTATION_MODE"] = "cut"
        arm("a `cut` tree whose archive is terminal-only and disjoint passes, and says what it graded",
            "rotation-mode: clean (`cut`, 1 rotated archive(s)",
            lambda: cap(t24, _conf24, cmd_check_rotation))

        # (a) a non-terminal row in a cut archive.
        t24b = os.path.join(base, "rotnonterm"); os.makedirs(t24b)
        c24b = _tree(t24b, "- ARCH-tOne-1 · one\n", pin="0",
                     shards={"ARCH.md": "- ARCH-tLive-1 · OPEN · the live row\n"},
                     archives={"ARCH.2026-01-01.md": "- ARCH-tGone-1 · CLOSED · terminal\n"
                                                     "- ARCH-tStay-1 · OPEN · under cut this never rotates\n"})
        _c24b = dict(c24b); _c24b["ROTATION_MODE"] = "cut"
        arm("a non-terminal row in a `cut` archive is named with its id, status and line",
            "ARCH-tStay-1 (OPEN) at line 2", lambda: cap(t24b, _c24b, cmd_check_rotation))

        # (a2) THE BOLD-ID EVASION. The first cut of this check spelled its own row predicate in
        # shell and a bold-wrapped id passed it silently — and `memory/DECISIONS.md` carries fifteen
        # such rows. Delegating to this module's grammar is what closes it, so the arm pins it.
        t24c = os.path.join(base, "rotbold"); os.makedirs(t24c)
        c24c = _tree(t24c, "- ARCH-tOne-1 · one\n", pin="0",
                     shards={"ARCH.md": "- ARCH-tLive-1 · OPEN · the live row\n"},
                     archives={"ARCH.2026-01-01.md": "- **ARCH-tBold-1** · SPECCED · bold-wrapped\n"})
        _c24c = dict(c24c); _c24c["ROTATION_MODE"] = "cut"
        arm("a BOLD-WRAPPED id in a cut archive is still a row, and is still graded",
            "ARCH-tBold-1 (SPECCED)", lambda: cap(t24c, _c24c, cmd_check_rotation))

        # (b) exclusivity: one id, two files.
        t24d = os.path.join(base, "rotboth"); os.makedirs(t24d)
        c24d = _tree(t24d, "- ARCH-tOne-1 · one\n", pin="0",
                     shards={"ARCH.md": "- ARCH-tBoth-1 · OPEN · the id the archive also carries\n"},
                     archives={"ARCH.2026-01-01.md": "- ARCH-tBoth-1 · CLOSED · also live in the shard\n"})
        _c24d = dict(c24d); _c24d["ROTATION_MODE"] = "cut"
        arm("an id in BOTH an archive and its live index breaks the partition and is named",
            "does not partition the family: ARCH-tBoth-1",
            lambda: cap(t24d, _c24d, cmd_check_rotation))

        # A DECISIONS archive has no lifecycle token per row, so the terminal half is a category
        # error there and is deliberately not asserted. Without this arm, scoping it out is
        # indistinguishable from forgetting it.
        t24e = os.path.join(base, "rotdecisions"); os.makedirs(t24e)
        c24e = _tree(t24e, "- ARCH-tOne-1 · one\n", pin="0",
                     archives={"DECISIONS.2026-01-01.md": "- ARCH-tDec-1 · CORRECTS an earlier row, and this is prose\n"})
        _c24e = dict(c24e); _c24e["ROTATION_MODE"] = "cut"
        arm("a DECISIONS archive is not graded terminal-only — a decision row carries no status",
            "rotation-mode: clean", lambda: cap(t24e, _c24e, cmd_check_rotation))

        # The two modes this engine does NOT grade must ANNOUNCE, never pass quietly.
        _c24s = dict(c24); _c24s["ROTATION_MODE"] = "snapshot"
        arm("`snapshot` announces that it is NOT graded, and says how many archives that leaves",
            "does NOT grade", lambda: cap(t24, _c24s, cmd_check_rotation))
        _c24u = dict(c24); _c24u["ROTATION_MODE"] = ""
        arm("an UNDECLARED mode announces rather than passing quietly",
            "UNDECLARED", lambda: cap(t24, _c24u, cmd_check_rotation))

        # ANTI-VACUITY: `cut` over a tree with no rotated archive must SAY it graded nothing.
        t24f = os.path.join(base, "rotempty"); os.makedirs(t24f)
        c24f = _tree(t24f, "- ARCH-tOne-1 · one\n", pin="0")
        _c24f = dict(c24f); _c24f["ROTATION_MODE"] = "cut"
        arm("`cut` with NO rotated archive says it graded nothing rather than reporting clean",
            "graded NOTHING", lambda: cap(t24f, _c24f, cmd_check_rotation))

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
    if mode == "--check-rotation":
        return cmd_check_rotation(root, conf)
    print(f"row-grammar: unknown argument '{mode}'; the modes are --check, --check-rotation, "
          f"--report, --emit-pin and --selftest")
    return 2


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except Problem as exc:
        print(str(exc))
        sys.exit(1)
