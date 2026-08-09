#!/usr/bin/env python3
"""A row-keyed three-way merge driver for the id-anchored index files (upstream ARCH-dQuarriedLedger-1 U9).

    git config merge.rows.driver 'bash tools/lib/pyrun.sh tools/memory-tree/merge-rows.py %O %A %B %P'

Auto-resolves the index conflicts that are pure append-collisions — two nodes each appending a row to
`memory/DECISIONS.md` or `memory/backlog/<FAMILY>.md` — without ever duplicating or dropping a record
id. Upstream replayed 765 merges: a row-keyed merge auto-resolved 133 of 312 historical index
conflicts with zero silent duplications and zero dropped ids.

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
grammar keys its index merge on the pre-merge grammar. A row is still never invented or duplicated;
at worst a row whose anchor only the NEW grammar recognises is treated as unkeyed content. The
grammar is deliberately not vendored — a second copy of a regex is this repo's catalogued drift
class, and a stale-but-single grammar beats two that disagree.

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

Row ORDER comes from `%A`, with `%B`-only rows appended in `%B` order. Order is not semantic here —
ids are labels, not ranks — so a stable rule beats a clever one.

WHY THIS CANNOT DUPLICATE. Union duplicates because it is a LINE merge, and a row edited on both
sides is two different lines. This merges by KEY, so a row appears at most once by construction and
the only way to get two rows with one id is an explicit conflict, which is loud. The claim is
falsifiable and `merge-rows.test.sh` falsifies it with the exact shape that broke union.

Exit 0 = merged clean. Exit 1 = conflict markers written to %A; git leaves the path unmerged.
Exit 2 = called with fewer than the three input paths (usage).
"""
# Annotations as strings, the same house rule `extract.py` and `map_lib.py` follow. `resolve_python`
# imposes NO version floor — every candidate is accepted on `-c "import sys"` alone — so the
# interpreter a node hands this driver is whatever it has, and a `str | None` in a signature is
# evaluated at def time without this line.
from __future__ import annotations

import pathlib
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


def rows(block: list[str]) -> tuple[dict[str, list[str]], list[str], list[str]]:
    """(id -> the row's lines, id order, unkeyed lines trailing the last anchor).

    A ROW IS ITS LEAD-IN PLUS ITS ANCHOR LINE, and that is a measurement, not a preference. The naive
    model is "a row is one line, unkeyed lines are carried separately". Measured on this corpus's
    `memory/DECISIONS.md`, the section headings `## KICK — kickoff` and `## TOOL — tooling` and the
    `*(none yet)*` placeholder under KICK sit INSIDE the row block, interleaved between anchored
    rows. Carrying those in a side list and re-emitting them at the end would move every section
    heading to the bottom of the file — a driver that corrupts the thing it merges, exiting 0.

    So unkeyed lines attach to the FOLLOWING anchor, not the preceding one. A section heading belongs
    with the first row of its section, so when a `%B`-only row arrives it brings its heading with it,
    and position is preserved by construction rather than by a reordering rule.
    """
    out, order, lead = {}, [], []
    for ln in block:
        k = key(ln)
        if k is None or k in out:
            # `k in out` is a duplicate id within ONE input: pre-existing damage this driver must not
            # launder into a merge. Kept as ordinary content attached to the next anchor.
            lead.append(ln)
            continue
        out[k] = lead + [ln]
        order.append(k)
        lead = []
    return out, order, lead


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

    O, _, o_tail = rows(o_blk)
    A, a_order, a_tail = rows(a_blk)
    B, b_order, b_tail = rows(b_blk)

    # AUDIT COUNTERS, incremented at the EMIT sites and never derived from the input lists. Upstream's
    # first cut printed `sum(1 for k in a_order if k in A)`, which `rows()` makes a TAUTOLOGY — it
    # appends to `order` on exactly the branch that assigns `out[k]`, so the sum equals `len(a_order)`
    # no matter what the driver wrote. Reproduced there: base and ours 3 rows, theirs 1, both deletes
    # honoured; the driver wrote a 1-ROW file, exited 0, and the only print in the module announced
    # `3 row(s) from ours, 0 new from theirs, clean`. `dropped` is the term that was missing outright:
    # honouring a delete removes a row and nothing else says so.
    kept = took_b = dropped = 0
    out, conflicted = [], False
    for k in a_order:
        a_txt, b_txt, o_txt = A[k], B.get(k), O.get(k)
        if b_txt is None:
            if o_txt is None:
                out.extend(a_txt)          # ours added it; theirs never saw it
                kept += 1
            elif o_txt == a_txt:
                dropped += 1               # theirs deleted what ours left untouched — honour it
                continue
            else:
                # DELETE/MODIFY: ours edited it, theirs deleted it. Git conflicts here and so do we.
                # Silently keeping ours would discard a deliberate delete; silently dropping ours
                # would discard a deliberate edit. Neither is ours to choose.
                conflicted = True
                out.append("<<<<<<< ours\n")
                out.extend(a_txt)
                out.append("=======\n")
                out.append(">>>>>>> theirs (deleted)\n")
                kept += 1
        elif a_txt == b_txt:
            out.extend(a_txt)
            kept += 1
        elif o_txt == a_txt:
            out.extend(b_txt)
            kept += 1
        elif o_txt == b_txt:
            out.extend(a_txt)
            kept += 1
        else:
            conflicted = True
            out.append("<<<<<<< ours\n")
            out.extend(a_txt)
            out.append("=======\n")
            out.extend(b_txt)
            out.append(">>>>>>> theirs\n")
            kept += 1
    for k in b_order:
        if k in A:
            continue                       # already emitted above
        if k in O:
            if O[k] == B[k]:
                dropped += 1               # ours deleted what theirs left untouched — honour it
                continue
            # The MIRROR of the case above, and the one that actually lost data upstream: ours
            # deleted it, theirs EDITED it. The first draft dropped theirs' edit here and exited 0
            # "clean" — found by probing delete-vs-edit by hand, because no fixture covered the
            # interaction. A driver that silently discards a modification is the exact failure this
            # unit exists to prevent, and it is unrecoverable once committed.
            conflicted = True
            out.append("<<<<<<< ours (deleted)\n")
            out.append("=======\n")
            out.extend(B[k])
            out.append(">>>>>>> theirs\n")
            took_b += 1
            continue
        out.extend(B[k])
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
    # `kept + took_b` is the anchored-row count of the file just written, which is what makes this
    # line auditable: an operator can `grep -c` the result and reconcile. `dropped` is stated even
    # when it is 0, because an omitted term reads as "no deletes" exactly like a zero does.
    print(f"merge-rows: {kept} row(s) from ours, {took_b} new from theirs, "
          f"{dropped} dropped (delete honoured), {verdict}", file=sys.stderr)
    return pre + out + tr, (conflicted or c1 or c2)


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
