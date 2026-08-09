#!/usr/bin/env python3
# RAW docstring, and not a style choice: the text below quotes regex fragments, and in a cooked
# string `\b` is the BACKSPACE escape (it reached `main()`'s usage output as a control character) and
# `\s` is an invalid escape that CPython warns about on every single merge — a driver that prints a
# SyntaxWarning to stderr during `git merge` reads as a broken driver.
r"""A row-keyed three-way merge driver for the id-anchored index files (upstream ARCH-dQuarriedLedger-1 U9).

    git config merge.rows.driver 'bash tools/lib/pyrun.sh tools/memory-tree/merge-rows.py %O %A %B %P'

Auto-resolves the index conflicts that are pure append-collisions — two nodes each appending a row to
`memory/DECISIONS.md` or `memory/backlog/<FAMILY>.md` — without duplicating a record, ENFORCED by a
postcondition rather than assumed from the keying (see below). Upstream replayed 765 merges: a
row-keyed merge auto-resolved 133 of 312 historical index conflicts with zero dropped ids.

WHY NOT `merge=union`, which is one line of config and no code. Tested with git's own driver over
every historical conflict upstream: union never LOSES an id (0 of 441) but INTRODUCES a duplicate in
147 of 151 `DECISIONS.md` conflicts and 118 of 121 backlog conflicts. Those files hold zero duplicate
ids at HEAD, so every one of those is real damage. A design that measured only LOSS concluded union
was safe. It is not, and measuring the other direction is the whole reason this file exists.

WHY THIS IS NOT THE WITHDRAWN `regenerate` DRIVER. That one was withdrawn for a STRUCTURAL reason:
`ort` checks the merge result out only AFTER the per-path merges run, so a generator invoked from
inside a driver renders from the PRE-merge tree and commits a stale artifact.

This driver is a pure function of `%O %A %B` **plus the anchor grammar it reads from the worktree's
memory-recall kit** — it is NOT worktree-free, and claiming otherwise is what the next author would
have reasoned from. The exposure is real but bounded, and different in kind from regenerate's:
regenerate wrote a whole artifact from the stale tree, whereas a merge that CHANGES the anchor
grammar keys its index merge on the pre-merge grammar. A row is still never INVENTED; at worst a row
whose anchor only the NEW grammar recognises is treated as unkeyed content — and unkeyed content is
precisely the population the postcondition below exists for, because it is the population the keying
cannot speak for. The grammar is deliberately not vendored — a second copy of a regex is this repo's
catalogued drift class, and a stale-but-single grammar beats two that disagree.

The import is DEFERRED into `anchors()` rather than run at module scope, so an unreadable or broken
`extract.py`, a missing kit directory or a missing `.memory-tree.conf` all raise inside `merge()` and
are caught by `main()`'s fail-closed handler. At module scope they produce the silent-take-ours
shape: the driver exits non-zero without writing `%A`, and git leaves the path holding OURS-only
content with no markers and the incoming rows simply absent.

THREE REGIONS, and the split is the difference between working and not. A file is a preamble
(everything before the first anchored row), the row block, and a trailer. Every governed index here
opens with unkeyable prose — `memory/DECISIONS.md` is a title, two blockquote routing lines and a
section heading before its first anchored row; `memory/backlog/TOOL.md` is a title and a mutability
note — so an unconditional "a line the grammar cannot key -> CONFLICT" rule conflicts on EVERY merge
and the auto-resolve is unreachable. Preamble and trailer take an ordinary three-way text merge; only
the row block is keyed. THE REGION RULE WINS AT THE BLOCK BOUNDARY: the block is
`lines[first_anchor:last_anchor+1]`, so a section heading that sits BEFORE the first anchor is
preamble, and one INSIDE the block attaches to the following anchor (see `rows`).

Row ORDER comes from `%A`, with each `%B`-only row SPLICED IN after the last key that precedes it in
`%B` and is itself emitted, AND after the `%A`-only keys that already follow that key — before all
of them when there is none. The first cut appended those rows past the whole row block instead,
which files an incoming decision under whatever `## FAMILY` heading happens to be last:
`memory/DECISIONS.md` says of itself "Grouped by family for reading". That is not a design trade, it
is a REGRESSION — measured against the merge this driver replaces, git's own three-way merge places
the same row correctly. Order among siblings is not semantic (ids are labels, not ranks); SECTION
MEMBERSHIP is, and splicing is what keeps it.

THE `%A`-ONLY SKIP IS NOT A TIE-BREAK, it is the second half of the same defect. Seating the cursor
on the shared predecessor alone put ours' newly appended `## PLAY` row UNDER theirs' newly opened
`## KICK` heading, at exit 0, through a real `git merge` on the real index — because theirs' row was
the first of its section and so carried that heading as its lead-in. Git's own merge files both rows
correctly on the same two commits. Ours' own new rows belong where ours put them, so the incoming row
splices in after them.

A splice cannot be right in every shape, and the ones it cannot decide MUST NOT be guessed. So
placement is also a POSTCONDITION (`no_misfiled_rows`): every id in the written file must sit under
the same `#`-heading it sat under in an input that carries it. That is what catches the residue —
e.g. a row ours RELOCATED across a heading, which drags the row theirs filed behind it into the
section ours moved to (reproduced: `- TOOL-…` committed under `## closed`, rc 0, `clean`).

WHY A KEYED ROW CANNOT DUPLICATE — AND WHY THAT IS NOT THE WHOLE FILE. Union duplicates because it
is a LINE merge, and a row edited on both sides is two different lines. Keying by id removes that
for every line the grammar KEYS: such a row is emitted from exactly one branch of the case analysis
in `merge()`, so two rows with one id can only come from an explicit conflict, which is loud.

The grammar does not key every line, and this paragraph used to be written as though it did.
Measured on this repo's own `memory/DECISIONS.md`: 73 `- ` rows, 35 anchored, 38 UNKEYED. The shared
session-era pattern is bounded by `\b`, so the ratified correction-id form — a trailing letter, as
in `…-1b` — does not key at all. To this driver those 38 lines are CONTENT: they travel as a row's
lead-in or as trailer, and content is exactly what a line merge can copy. Two nodes minting the same
unkeyable row in different regions emitted it TWICE at exit 0 before this was written down.

So the no-duplicate property is ENFORCED, not asserted. Three mechanisms, and none is the grammar:

  * LEAD-IN DEDUP (`merge`'s `lead`). A row is its lead-in plus its anchor (see `rows`), so when two
    nodes each land the FIRST row of the same currently-empty section, the same base furniture — the
    `## FAMILY` heading, the `*(none yet)*` placeholder — rides in on two different new ids and is
    emitted twice. Furniture is not a record. The dedup is ADJACENCY-scoped, not file-wide: it
    suppresses a repeated lead-in only when the previous emitted row was itself new to the merge and
    carried the identical lead-in. File-wide it deleted furniture that legitimately repeats — two
    nodes each opening a `### 2026-08` sub-heading in DIFFERENT sections lost theirs entirely, at
    exit 0, where `git merge-file` produces the fully correct file.
  * A LINE POSTCONDITION (`no_new_duplicates`, line half): no ROW-SHAPED line — `^\s*[-*]\s` — may be
    written more times than the most any ONE input carried it. Row-shaped and not "any non-blank
    line", because the two shapes are indistinguishable at the line level and their correct answers
    are OPPOSITE: a record written twice is corruption, a heading written twice in two sections is
    the merge git itself performs. A record is a row; furniture is governed by the dedup above and
    by `no_misfiled_rows`.
  * AN ID POSTCONDITION (`no_new_duplicates`, id half). The line half compares EXACT text, so the
    same unkeyable correction id minted on two nodes with different WORDING is two different lines
    and lands twice at exit 0 — measured. So each row-shaped line is also keyed on the FIRST id it
    carries, under a grammar deliberately WIDER than the driver's own (`…-9b` keys here and does not
    key there), and the same cap applies. First id, not every id: rows cite other records constantly,
    and counting citations makes two nodes each citing one base row look like a duplicate. Measured
    over this corpus: 73 rows, 73 distinct leading ids, zero repeats — a live invariant, not a hope.

All three postconditions run on EVERY verdict, over the merged lines with conflict regions excised.
Scoping them to rc 0 was wrong: an author resolves the marked hunks and reads everything outside them
as settled, so a duplicate emitted OUTSIDE the markers of an unrelated conflict is exactly as
invisible at rc 1 as at rc 0 — reproduced. Excising the regions is what keeps that honest, since a
conflict hunk repeats content from both sides by construction. A violation raises, and `main()`'s
fail-closed handler turns it into a real conflict, because a driver that cannot answer must say so.

Every claim above is falsifiable and `merge-rows.test.sh` falsifies each: the shape that broke union,
two nodes opening the same empty section, an unkeyable row minted on both nodes, the same id minted
on both with different wording, a repeated lead-in in two sections, a duplicate hiding beside an
unrelated conflict, and both directions of a delete against adjacent incoming content.

Exit 0 = merged clean. Exit 1 = conflict markers written to %A; git leaves the path unmerged.
Exit 2 = called with fewer than the three input paths (usage).
"""
# Annotations as strings, the same house rule `extract.py` and `map_lib.py` follow. `resolve_python`
# imposes NO version floor — every candidate is accepted on `-c "import sys"` alone — so the
# interpreter a node hands this driver is whatever it has, and a `str | None` in a signature is
# evaluated at def time without this line.
from __future__ import annotations

import pathlib
import re
import subprocess
import sys

# Same rationale as `tools/memory-recall/extract.py`: CPython writes a module's bytecode next to its
# SOURCE, which is inside the worktree being merged. A merge driver that reads three blobs and writes
# one should write nothing else, and this is the whole of that property on the deferred import below.
sys.dont_write_bytecode = True

_ANCHOR_AT = None
_GRAMMAR = None


def _anchor_root() -> pathlib.Path:
    """The nearest ancestor of THIS FILE holding `.memory-tree.conf`.

    Not `git rev-parse --show-toplevel`: in a linked worktree the WSL bash resolves ahead of MSYS and
    cannot read a `gitdir:` pointer, so rev-parse dies for a reason that has nothing to do with the
    merge. Not a fixed `parents[2]` either — that is correct only at this repo's `tools/` install
    prefix, while the walk-up is correct at both the `tools/` and the adopter `<root>/memory-tree/`
    prefix with no env var and no second declaration.
    """
    here = pathlib.Path(__file__).resolve()
    for parent in here.parents:
        if (parent / ".memory-tree.conf").is_file():
            return parent
    raise RuntimeError(
        f"no .memory-tree.conf above {here.as_posix()} — the anchor grammar is read from the "
        f"memory-tree conf, so there is no grammar to key rows with"
    )


def _kit_dir(root: pathlib.Path) -> pathlib.Path:
    """The memory-recall kit directory, in either install layout.

    Tools-first, the same order `tools/check-wiring.sh` uses when it resolves `settings-merge.py`
    across the two layouts: `<root>/tools/memory-recall/` in this repo, `<root>/memory-recall/` in a
    repo that copy-installed the kit at the canonical prefix.
    """
    for cand in (root / "tools" / "memory-recall", root / "memory-recall"):
        if cand.is_dir():
            return cand
    raise RuntimeError(
        f"no memory-recall kit under {root.as_posix()} (looked at tools/memory-recall and "
        f"memory-recall) — the anchor grammar lives there and is never vendored here"
    )


def anchors() -> tuple:
    """The ONE anchor grammar, imported lazily and never re-typed.

    Lazy on purpose. At module scope an import failure kills the driver BEFORE `main()` can write
    anything, which is the silent-take-ours shape; raised from in here it lands in the fail-closed
    handler and the author gets conflict markers instead of a quietly truncated file.

    `grammar_for(root)` re-resolves `.memory-tree.conf` at an EXPLICIT root and returns the id
    alternation plus the four anchor regexes built from THAT repo's `FAMILIES`, so an adopting repo
    with different families keys on its own ids. `anchor_at(line, g)` is the "which id does this line
    DEFINE" predicate, as opposed to one that merely cites it.
    """
    global _ANCHOR_AT, _GRAMMAR
    if _ANCHOR_AT is None:
        root = _anchor_root()
        # APPEND, never `insert(0, …)`: prepending puts the kit dir ahead of the stdlib, so any
        # module name it ever gains shadows the real one — a `tempfile.py` there would silently
        # replace the stdlib module `text_merge` imports below.
        sys.path.append(str(_kit_dir(root)))
        import extract as EX  # noqa: PLC0415 — deliberately deferred; see above
        _GRAMMAR = EX.grammar_for(str(root))
        _ANCHOR_AT = EX.anchor_at
    return _ANCHOR_AT, _GRAMMAR


def key(line: str) -> str | None:
    """The record id this line anchors, or None if it anchors none."""
    anchor_at, grammar = anchors()
    return anchor_at(line, grammar)


def split_regions(lines: list[str]) -> tuple[list[str], list[str], list[str]]:
    """(preamble, row block, trailer) — the row block spans first..last anchored line inclusive."""
    idx = [i for i, ln in enumerate(lines) if key(ln)]
    if not idx:
        return lines, [], []
    return lines[:idx[0]], lines[idx[0]:idx[-1] + 1], lines[idx[-1] + 1:]


def rows(block: list[str]) -> tuple[dict[str, str], dict[str, list[str]], list[str], list[str]]:
    """(id -> its anchor LINE, id -> the lines leading it, id order, unkeyed lines after the last).

    A ROW IS ITS LEAD-IN PLUS ITS ANCHOR LINE, and that is a measurement, not a preference. The naive
    model is "a row is one line, unkeyed lines are carried separately". Measured on this corpus's
    `memory/DECISIONS.md`, the section headings `## KICK — kickoff` and `## TOOL — tooling` and the
    `*(none yet)*` placeholder under KICK sit INSIDE the row block, interleaved between anchored
    rows. Carrying those in a side list and re-emitting them at the end would move every section
    heading to the bottom of the file — a driver that corrupts the thing it merges, exiting 0.

    So unkeyed lines attach to the FOLLOWING anchor, not the preceding one. A section heading belongs
    with the first row of its section, so when a `%B`-only row arrives it brings its heading with it.

    THE LEAD-IN IS RETURNED SEPARATELY FROM THE ANCHOR, not glued to it, and that split is the whole
    of two defects. Glued, the lead-in is picked wholesale by whichever branch of the case analysis
    wins the ANCHOR, so (i) an edit to the heading on one side and to the row on the other could not
    both survive, and (ii) two ids that are each new to the merge each carried their own copy of the
    same base heading, which is how a section heading got emitted twice at exit 0. Split, the lead-in
    gets its own three-way merge against `%O` and its own dedup — see `merge`.
    """
    anchor, lead_of, order, lead = {}, {}, [], []
    for ln in block:
        k = key(ln)
        if k is None or k in anchor:
            # `k in anchor` is a duplicate id within ONE input: pre-existing damage this driver must
            # not launder into a merge. Kept as ordinary content attached to the next anchor.
            lead.append(ln)
            continue
        anchor[k] = ln
        lead_of[k] = lead
        order.append(k)
        lead = []
    return anchor, lead_of, order, lead


class DuplicatedContent(RuntimeError):
    """A duplicate postcondition refused the result. Raised, never printed-and-continued."""


class Misfiled(RuntimeError):
    """The placement postcondition refused the result. Raised, never printed-and-continued."""


# A RECORD is a row. Every governed index writes one record per `- `/`* ` line, and this predicate is
# the whole reason the duplicate postconditions can be strict without redding a legitimate merge: a
# repeated ROW is corruption, a repeated HEADING is two sections that happen to share a name. Both are
# "a line written twice" and nothing at the line level tells them apart, so the population is named
# here instead of guessed there.
_ROW_RE = re.compile(r"^\s*[-*]\s")
# Deliberately WIDER than the driver's own anchor grammar, and not imported from it. The keyed path
# already guarantees uniqueness for what `key()` keys; this exists for the population it does NOT key
# — the ratified `…-9b` correction form, which the shared session era's trailing `\b` rejects. Keying
# the postcondition on the same regex as the merge would make it self-consistent and blind: an id the
# grammar stopped recognising would drop out of BOTH the merge and the check on the merge.
_ID_RE = re.compile(r"\b[A-Z]+-[A-Za-z0-9]+-[0-9]+[a-z]*\b")
# A marker line is INVENTED by the merge, so it has no input count to be measured against, and the
# same three markers legitimately repeat once per conflicting region. `|||||||` is here because
# `git merge-file` writes it under `diff3` style, which is a per-node config this driver does not set.
# One pair, not three tokens: `settled` drops everything BETWEEN them, which covers `=======` and the
# `|||||||` base section `git merge-file` writes under diff3 style without naming either.
_OPEN, _CLOSE = "<<<<<<<", ">>>>>>>"
_HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s")


def settled(lines: list[str]) -> list[str]:
    """`lines` with every conflict region dropped — the part of the file an author reads as decided.

    The postconditions below run on THIS, never on the raw output, and they run on every verdict. The
    first cut ran them only when the verdict was clean, reasoning that a conflict hunk repeats context
    from both sides by construction. True, and it argues for excising the REGIONS, not for switching
    the check off: one unrelated both-sides row edit anywhere in the file turned the detector off for
    the whole file, and the duplicate was then written OUTSIDE the markers — reproduced. An author
    resolves the marked hunks and commits everything else unread, so rc 1 hides a duplicate exactly as
    well as rc 0 does.
    """
    out, inside = [], False
    for ln in lines:
        s = ln.lstrip()
        if not inside and s.startswith(_OPEN):
            inside = True
            continue
        if inside:
            if s.startswith(_CLOSE):
                inside = False
            continue
        out.append(ln)
    return out


def census(lines: list[str]) -> dict[str, int]:
    """How many times each ROW-SHAPED line occurs, keyed on the stripped text.

    Stripped because the question is about content, not endings: this driver's whole newline contract
    exists so a CRLF region survives as CRLF, and a census that compared raw bytes would answer "not
    a duplicate" for the same line arriving from a CRLF side and an LF side — or for one side's copy
    of a row landing as the file's final line with no terminator, which is the reachable shape.
    """
    out: dict[str, int] = {}
    for ln in lines:
        if not _ROW_RE.match(ln):
            continue
        s = ln.strip()
        if s:
            out[s] = out.get(s, 0) + 1
    return out


def row_ids(lines: list[str]) -> dict[str, int]:
    """How many rows LEAD with each id — the record-level census the line-level one cannot do."""
    out: dict[str, int] = {}
    for ln in lines:
        if not _ROW_RE.match(ln):
            continue
        m = _ID_RE.search(ln)
        if m:
            out[m.group(0)] = out.get(m.group(0), 0) + 1
    return out


def _over(merged: dict[str, int], inputs: list[dict[str, int]]) -> list[tuple]:
    """Everything written more often than the most any ONE input carried it.

    The cap is a MAXIMUM over the inputs rather than a sum: an index that legitimately repeats a
    placeholder twice at base must still be allowed to carry it twice, while two sides that each
    carry a line once may not become two. (A sum would pass the exact shape this exists to refuse.)
    """
    cap: dict[str, int] = {}
    for side in inputs:
        for s, n in side.items():
            if n > cap.get(s, 0):
                cap[s] = n
    return sorted((s, n, cap.get(s, 0)) for s, n in merged.items() if n > 1 and n > cap.get(s, 0))


def no_new_duplicates(merged: list[str], *inputs: list[str]) -> None:
    """Refuse to write a row, or an id, more times than the most any ONE input carried it.

    The backstop for everything the anchor grammar cannot key. `merge()` guarantees uniqueness for
    KEYED rows by construction; unkeyed lines are content and reach the output through two
    independent paths (a row's lead-in, and the preamble/trailer text merges), so nothing structural
    stops the same line arriving down both. Measured on the real index: the same unkeyable row minted
    on two nodes and filed in different regions was written twice, exit 0, audit line "clean".

    TWO HALVES, because the line half alone is blind to the corpus's own correction form. Two nodes
    each minting `…-9b` with different prose produce two DIFFERENT lines, so the line census sees each
    once, the cap holds, and the id lands twice in an append-only record at exit 0 — measured, and the
    suite's own oracle sees it. So the same rule is lifted from line to record.
    """
    clean = settled(merged)
    sides = [settled(side) for side in inputs]
    over = _over(census(clean), [census(s) for s in sides])
    if over:
        s, n, was = over[0]
        raise DuplicatedContent(
            f"{len(over)} row line(s) would be written more often than any single input carries "
            f"them, e.g. {s[:72]!r} x{n} against x{was}"
        )
    over = _over(row_ids(clean), [row_ids(s) for s in sides])
    if over:
        s, n, was = over[0]
        raise DuplicatedContent(
            f"{len(over)} id(s) would lead more rows than in any single input, e.g. {s!r} x{n} "
            f"against x{was} — the same id minted on two nodes with different wording"
        )


def sections(lines: list[str]) -> dict[str, str]:
    """id -> the `#` heading it sits under, over a WHOLE file (preamble included).

    Whole file on purpose: `memory/DECISIONS.md` opens `## PLAY — playbook` BEFORE its first anchored
    row, so that heading is preamble by the region rule and a block-scoped walk would report `None`
    for every PLAY row and see no misfiling when one moved out.
    """
    out: dict[str, str] = {}
    cur = ""
    for ln in lines:
        if _HEADING_RE.match(ln):
            cur = ln.strip()
            continue
        k = key(ln)
        if k is not None and k not in out:
            out[k] = cur
    return out


def no_misfiled_rows(merged: list[str], *inputs: list[str]) -> None:
    """Refuse to file a row under a heading no input filed it under.

    The splice places a `%B`-only row after the neighbour it arrived behind; that is right for the
    shapes it was measured on and cannot be right for all of them. Where it is wrong the damage is
    silent — a `PLAY` decision auto-committed under `## KICK`, a row filed under `## closed` because
    ours relocated the neighbour it arrived behind — so placement gets a postcondition rather than a
    cleverer heuristic. `git merge-file` REFUSES the relocation input; being quietly worse than the
    merge this replaces is the bar this driver has to clear.

    "An input that carries it", not "%A", deliberately: a row whose section is unchanged on both
    sides has one answer, and a row only one side carries has exactly one input to answer for it.
    """
    clean = sections(settled(merged))
    per_side = [sections(side) for side in inputs]
    bad = []
    for k, sect in sorted(clean.items()):
        was = [s[k] for s in per_side if k in s]
        if was and sect not in was:
            bad.append((k, sect, sorted(set(was))))
    if not bad:
        return
    k, sect, was = bad[0]
    raise Misfiled(
        f"{len(bad)} row(s) would be filed under a heading no input filed them under, e.g. {k!r} "
        f"under {sect[:48]!r} against {[w[:48] for w in was]}"
    )


def text_merge(o: list[str], a: list[str], b: list[str]) -> tuple[list[str], bool]:
    """Ordinary three-way text merge for the prose regions, via `git merge-file`."""
    if a == b:
        return a, False
    if o == a:
        return b, False
    if o == b:
        return a, False
    import tempfile  # noqa: PLC0415 — deferred with the sys.path.append above in mind
    with tempfile.TemporaryDirectory() as td:
        p = pathlib.Path(td)
        for name, data in (("o", o), ("a", a), ("b", b)):
            # `newline=""` — site 2 of the newline contract. Without it Python translates every "\n"
            # in the joined text to the platform separator on write, and a CRLF region round-trips as
            # CRCRLF.
            (p / name).write_text("".join(data), encoding="utf-8", newline="")
        # -L labels the markers `ours`/`base`/`theirs`. Without them git labels a conflict with the
        # temp FILENAMES, so a real conflict reads `<<<<<<< C:\\Users\\…\\tmpqm5j4r78\\a` — an
        # absolute scratch path in the file the author now has to resolve by hand.
        r = subprocess.run(["git", "merge-file", "-p", "-L", "ours", "-L", "base", "-L", "theirs",
                            str(p / "a"), str(p / "o"), str(p / "b")],
                           capture_output=True)
        # SITE 3 of the newline contract, and the one upstream does not solve: it passes
        # `text=True`, which is universal-newline mode, so a CRLF preamble comes back as LF and the
        # careful `newline=""` two lines up is undone. Capture BYTES and decode by hand instead —
        # this repo's nodes run `core.autocrlf=true` and the governed indexes are CRLF in the
        # worktree, which is exactly the format git hands a merge driver.
        return r.stdout.decode("utf-8", "replace").splitlines(keepends=True), r.returncode != 0


def merge(o_lines, a_lines, b_lines) -> tuple[list[str], bool]:
    o_pre, o_blk, o_tr = split_regions(o_lines)
    a_pre, a_blk, a_tr = split_regions(a_lines)
    b_pre, b_blk, b_tr = split_regions(b_lines)

    pre, c1 = text_merge(o_pre, a_pre, b_pre)
    tr, c2 = text_merge(o_tr, a_tr, b_tr)

    O, o_lead, _, o_tail = rows(o_blk)
    A, a_lead, a_order, a_tail = rows(a_blk)
    B, b_lead, b_order, b_tail = rows(b_blk)

    # THE EMIT ORDER: `%A`'s, with each `%B`-only key SPLICED after the last key preceding it in
    # `%B` that survives into the output, and before everything when there is none. Appending them
    # past the block instead put an incoming `## PLAY` row under `## TOOL` — the same two inserts
    # through git's built-in merge land correctly, so the append rule was a regression against the
    # thing being replaced. The cursor is re-seated on every SHARED key, so consecutive `%B`-only
    # rows keep their own relative order behind the neighbour they arrived after.
    #
    # ...AND THEN PAST THE `%A`-ONLY KEYS THAT FOLLOW IT. Seating on the shared predecessor alone put
    # ours' new row UNDER theirs' new `## FAMILY` heading whenever theirs' row opened the next
    # section: theirs' row carries that heading as its lead-in, so anything spliced BEFORE it lands
    # in the wrong section. Reproduced through a real `git merge` on the real `memory/DECISIONS.md`
    # — a PLAY decision auto-committed under `## KICK`, rc 0, `clean`, zero markers, where git's own
    # merge on the same two commits files both rows correctly. Ours' new rows sit where ours put
    # them; the incoming row goes after them. `no_misfiled_rows` judges whatever this cannot.
    a_set = set(a_order)
    a_only = a_set - set(b_order)
    order = list(a_order)
    at = None
    for k in b_order:
        if k in a_set:
            at = order.index(k)
            while at + 1 < len(order) and order[at + 1] in a_only:
                at += 1
            continue
        at = 0 if at is None else at + 1
        order.insert(at, k)

    # AUDIT COUNTERS, incremented at the EMIT sites and never derived from the input lists. Upstream's
    # first cut printed `sum(1 for k in a_order if k in A)`, which `rows()` makes a TAUTOLOGY — it
    # appends to `order` on exactly the branch that assigns `out[k]`, so the sum equals `len(a_order)`
    # no matter what the driver wrote. Reproduced there: base and ours 3 rows, theirs 1, both deletes
    # honoured; the driver wrote a 1-ROW file, exited 0, and the only print in the module announced
    # `3 row(s) from ours, 0 new from theirs, clean`. `dropped` is the term that was missing outright:
    # honouring a delete removes a row and nothing else says so.
    kept = took_b = dropped = 0
    out, conflicted, prev_new_sig = [], False, None

    def lead(k: str) -> list[str]:
        """The lines to emit BEFORE k's anchor.

        Two regimes, because a lead-in has a base counterpart only when its id does.

        k IS IN `%O`: an ordinary three-way merge of the three lead-ins. That is what lets a heading
        edited on one side survive alongside a row edited on the other, and it is also what stops a
        heading being emitted twice when one side MOVED it onto a row it inserted above — the side
        that moved it away contributes an empty lead-in, and `o == a -> b` takes it.

        k IS NEW: there is no base lead-in to merge against, so the side that minted the id supplies
        it (both, merged, when both minted the same id). DEDUP APPLIES HERE AND ONLY HERE. Two nodes
        each landing the first row of the same empty section arrive with the SAME base furniture
        attached to two different new ids; emitting both is how `## DEPL — deployer` appeared twice
        in an append-only file at exit 0.

        THE DEDUP IS ADJACENCY-SCOPED, and that is the second defect in as many cuts. Keyed
        file-wide, it dropped every LATER copy of a lead-in anywhere in the file — so two nodes each
        opening a `### 2026-08` sub-heading in DIFFERENT sections lost theirs outright, at exit 0,
        on an input where `git merge-file` produces the fully correct file. A repeat is furniture
        only when it is the SAME piece of furniture, which is to say when the two new ids land next
        to each other. So the suppression asks about the previous EMITTED row and nothing else: it
        fires when that row was itself new to the merge and carried this exact lead-in.

        Blank-only lead-ins are exempt and do NOT break the adjacency chain: a repeated blank line is
        spacing, not furniture, so suppressing it would run rows together — and a furniture-less row
        landing between two that share furniture has not moved them apart.
        """
        nonlocal conflicted, prev_new_sig
        if k in O:
            got, c = text_merge(o_lead[k], a_lead.get(k, o_lead[k]), b_lead.get(k, o_lead[k]))
            conflicted = conflicted or c
            prev_new_sig = None
            return got
        if k in A and k in B:
            got, c = text_merge([], a_lead[k], b_lead[k])
            conflicted = conflicted or c
        else:
            got = a_lead[k] if k in A else b_lead[k]
        sig = tuple(s for s in (ln.strip() for ln in got) if s)
        if not sig:
            return list(got)
        if sig == prev_new_sig:
            return []
        prev_new_sig = sig
        return list(got)

    # BOTH DELETE TESTS COMPARE THE ROW, WHICH IS THE LEAD-IN PLUS THE ANCHOR — never the anchor
    # alone. Splitting the two apart (the fix for the doubled heading) narrowed these two comparisons
    # to the anchor line, so a side that left the ROW untouched but filed something immediately ABOVE
    # it read as "untouched", and the `continue` past `lead(k)` then DISCARDED what it filed. Measured
    # in both directions: base 3 rows, one side deletes row 2, the other files an unkeyable `…-7b`
    # correction row above row 2 — driver rc 0 `1 dropped … clean`, the incoming row GONE, zero
    # markers; `git merge-file` AND the pre-split driver both rc 1 with the row intact. Losing a row
    # from an append-only record is worse than every other way this can be wrong, and a delete against
    # adjacent new content is a delete/modify by any other name: it falls to the CONFLICT branch
    # below, where the adjacent content is emitted and the disputed row is marked.
    for k in order:
        a_txt, b_txt, o_txt = A.get(k), B.get(k), O.get(k)
        if a_txt is not None:
            if b_txt is None:
                if o_txt is None:
                    out.extend(lead(k))    # ours added it; theirs never saw it
                    out.append(a_txt)
                    kept += 1
                elif o_txt == a_txt and a_lead[k] == o_lead[k]:
                    dropped += 1           # theirs deleted what ours left UNTOUCHED — honour it
                    continue
                else:
                    # DELETE/MODIFY: ours edited it, theirs deleted it. Git conflicts here and so do
                    # we. Silently keeping ours would discard a deliberate delete; silently dropping
                    # ours would discard a deliberate edit. Neither is ours to choose.
                    conflicted = True
                    out.extend(lead(k))
                    out.append("<<<<<<< ours\n")
                    out.append(a_txt)
                    out.append("=======\n")
                    out.append(">>>>>>> theirs (deleted)\n")
                    kept += 1
            elif a_txt == b_txt:
                out.extend(lead(k))
                out.append(a_txt)
                kept += 1
            elif o_txt == a_txt:
                out.extend(lead(k))
                out.append(b_txt)
                kept += 1
            elif o_txt == b_txt:
                out.extend(lead(k))
                out.append(a_txt)
                kept += 1
            else:
                conflicted = True
                out.extend(lead(k))
                out.append("<<<<<<< ours\n")
                out.append(a_txt)
                out.append("=======\n")
                out.append(b_txt)
                out.append(">>>>>>> theirs\n")
                kept += 1
        elif k in O:
            if O[k] == B[k] and b_lead[k] == o_lead[k]:
                dropped += 1               # ours deleted what theirs left UNTOUCHED — honour it
                continue
            # The MIRROR of the case above, and the one that actually lost data upstream: ours
            # deleted it, theirs EDITED it. The first draft dropped theirs' edit here and exited 0
            # "clean" — found by probing delete-vs-edit by hand, because no fixture covered the
            # interaction. A driver that silently discards a modification is the exact failure this
            # unit exists to prevent, and it is unrecoverable once committed.
            conflicted = True
            out.extend(lead(k))
            out.append("<<<<<<< ours (deleted)\n")
            out.append("=======\n")
            out.append(b_txt)
            out.append(">>>>>>> theirs\n")
            took_b += 1
        else:
            out.extend(lead(k))
            out.append(b_txt)
            took_b += 1

    # Unkeyed lines AFTER the last anchor are an ordinary text region, like the trailer.
    tail, c3 = text_merge(o_tail, a_tail, b_tail)
    out = out + tail

    conflicted = conflicted or c3
    # Hoisted, NOT inlined. `f"{"CONFLICT" if … else "clean"}"` — a nested SAME-quote f-string — is
    # PEP 701 and parses only on Python 3.12+; on 3.10/3.11, which `resolve_python` accepts (it
    # imposes no version floor at all), it is a SyntaxError at import. That is not a style point for
    # a merge DRIVER: a driver that fails to start exits non-zero without writing %A, which is the
    # silent-take-ours shape main()'s wrapper below exists to prevent.
    verdict = "CONFLICT" if conflicted or c1 or c2 else "clean"
    merged = pre + out + tr
    # THE POSTCONDITIONS, checked BEFORE the audit line is printed — a run that is about to refuse
    # must not first announce "clean". EVERY verdict, not clean ones only: the region excision inside
    # `settled()` is what handles a conflict hunk's by-construction repetition, and a duplicate
    # written OUTSIDE the markers of an unrelated conflict is invisible at rc 1 exactly as it is at
    # rc 0, because an author resolves the hunks and reads the rest as settled. Reproduced.
    no_new_duplicates(merged, o_lines, a_lines, b_lines)
    no_misfiled_rows(merged, o_lines, a_lines, b_lines)
    # `kept + took_b` is the anchored-row count of the file just written, which is what makes this
    # line auditable: an operator can `grep -c` the result and reconcile. `dropped` is stated even
    # when it is 0, because an omitted term reads as "no deletes" exactly like a zero does.
    print(f"merge-rows: {kept} row(s) from ours, {took_b} new from theirs, "
          f"{dropped} dropped (delete honoured), {verdict}", file=sys.stderr)
    return merged, (conflicted or c1 or c2)


def read(p: str) -> list[str]:
    # SITE 1 of the newline contract. `newline=""` suppresses universal-newline translation, so a
    # CRLF line keeps its "\r\n" and every downstream comparison is over the real bytes.
    with open(p, "r", encoding="utf-8", errors="replace", newline="") as fh:
        return fh.read().splitlines(keepends=True)


def main(argv: list[str]) -> int:
    if len(argv) < 4:
        # The first TWO paragraphs: the summary sentence AND the `git config` line carrying the four
        # `%O %A %B %P` placeholders. Upstream prints `[0]` — the summary alone — so its usage text
        # tells an operator nothing about how to wire the driver it is refusing to run.
        print("\n\n".join((__doc__ or "").split("\n\n")[:2]), file=sys.stderr)
        return 2
    o, a, b = argv[1], argv[2], argv[3]
    # FAIL CLOSED. A merge driver that raises exits non-zero WITHOUT writing %A, and git then leaves
    # the path unmerged holding OURS-only content with no conflict markers in it — the incoming rows
    # are simply absent and nothing says so. That is silent, unrecoverable loss, and it is strictly
    # worse than the crash that caused it. So any exception is converted into a REAL conflict: both
    # sides written out with markers, so the author sees the incoming content and git refuses the
    # commit until it is resolved.
    try:
        merged, conflicted = merge(read(o), read(a), read(b))
    except Exception as exc:  # noqa: BLE001 — deliberately total; see above
        print(f"merge-rows: FAILED ({exc.__class__.__name__}: {exc}) — writing a conflict rather "
              f"than a silent take-ours", file=sys.stderr)
        try:
            ours, theirs = read(a), read(b)
        except Exception:  # noqa: BLE001 — cannot even read the inputs
            return 1  # leave %A untouched and refuse
        body = (["<<<<<<< ours\n"] + ours + ["=======\n"] + theirs
                + [">>>>>>> theirs (merge-rows failed; resolve by hand)\n"])
        pathlib.Path(a).write_bytes("".join(body).encode("utf-8"))
        return 1
    # SITE 4 of the newline contract: written as BYTES, with the newlines already carried by the
    # source lines. `write_text` translates on Windows and would rewrite the whole file's line
    # endings — the governed indexes are CRLF in this repo's worktrees, so that is every line of
    # every file, on a merge that was supposed to add one row.
    pathlib.Path(a).write_bytes("".join(merged).encode("utf-8"))
    return 1 if conflicted else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
