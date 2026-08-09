#!/usr/bin/env python3
# RAW docstring, and not a style choice: the text below quotes regex fragments, and in a cooked
# string `\b` is the BACKSPACE escape (it reached `main()`'s usage output as a control character) and
# `\s` is an invalid escape that CPython warns about on every single merge — a driver that prints a
# SyntaxWarning to stderr during `git merge` reads as a broken driver.
r"""A row-keyed three-way merge driver for the id-anchored index files (aMendedLedger U9).

    git config merge.rows.driver 'bash tools/lib/pyrun.sh tools/memory-tree/merge-rows.py %O %A %B %P'

Auto-resolves the index conflicts that are pure append-collisions — two nodes each appending a row to
`memory/DECISIONS.md` or `memory/backlog/<FAMILY>.md` — without duplicating a record, ENFORCED by
postconditions on the written bytes rather than assumed from the keying.

WHY NOT `merge=union`, which is one line of config and no code. Tested with git's own driver over
every historical conflict upstream: union never LOSES an id (0 of 441) but INTRODUCES a duplicate in
147 of 151 `DECISIONS.md` conflicts and 118 of 121 backlog conflicts. Those files hold zero duplicate
ids at HEAD, so every one of those is real damage. A design that measured only LOSS concluded union
was safe. It is not, and measuring the other direction is the whole reason this file exists.

WHY THIS IS NOT THE WITHDRAWN `regenerate` DRIVER. That one was withdrawn for a STRUCTURAL reason:
`ort` checks the merge result out only AFTER the per-path merges run, so a generator invoked from
inside a driver renders from the PRE-merge tree and commits a stale artifact.

TWO PLANES, AND THE PARTITION IS THE ROW SHAPE. Every line is classified by ONE stateless predicate
applied to that line alone — `_ROW_RE`, `^\s*[-*]\s` — into ROW or STRUCTURE. Structure is merged by
`git merge-file`, positionally, byte for byte. Only the row set is key-merged here. The partition is
the SHAPE and never the anchor grammar: measured, `git merge-file` is correct on every class of
non-row content this corpus produced (a heading, a placeholder, a repeated lead-in note, a
sub-heading in two sections) and its ONE observed corruption is a row line duplicated at rc 0 —
which is exactly the population keying owns. Partitioning by the grammar would hand git the row
lines it duplicates and rebuild the defect on the other side of the split.

THE SKELETON is how the two planes recombine in ORDER rather than by guess. Each of `%O %A %B` is
projected to a line list of the same length in which every ROW line becomes a single token line and
every STRUCTURE line passes through unchanged. The token is the row's id when the grammar keys it
(`\x01row:<id>\x01`) and a digest of its STRIPPED text when it does not (`\x01raw:<hex>\x01`).
Hashing the stripped text is what stops line form smuggling a duplicate: a final copy with no
newline and an interior copy with one produce the same token. The three skeletons are merged by
`git merge-file`, the row set is key-merged separately, and the merged skeleton is then walked and
its tokens substituted.

Keying a row's token on its ID and not its text is what keeps a row EDIT invisible to the structure
plane. Otherwise every row edit is a structural change and git starts arbitrating record text, which
is where duplication comes from — measured: a heading renamed on theirs against the row under it
edited on ours is rc 1 through raw `git merge-file` and rc 0 here, because ours' skeleton is
byte-identical to base's.

THE ROW PLANE IS `key -> LIST`, NEVER `key -> line`. A markdown file may legitimately carry the same
row-shaped line twice (two identical `  - notes` sub-bullets under two different rows is ordinary),
and collapsing those to one made a file FAIL ITS OWN IDENTITY MERGE — a permanent whole-file
conflict no author can clear. So a key resolves to a list of row lines, and `no_row_loss` below is a
CONSERVATION check and explicitly not a uniqueness check.

RECONCILIATION IS FOUR RULES, in order, over the merged skeleton:

  1. A structure line outside a conflict region is emitted byte for byte.
  2. A token outside a region is replaced by the NEXT UNCONSUMED entry of `resolved[key]` — one
     line, or nothing when a delete was honoured, or a marker block. Each occurrence consumes one
     entry; a token that occurs more often than the row plane resolved it is a conservation failure
     and refused by name.
  3. A region whose ours-side and theirs-side consist ENTIRELY of tokens is resolved by POSITIONAL
     CONCATENATION: ours' tokens in order, then theirs'. A theirs-side token is suppressed only when
     the same key also occurs on OURS' side. DEDUP HAPPENS ACROSS SIDES AND NEVER WITHIN A SIDE —
     the within-side form deletes a legitimately repeated note out of an append-only record at rc 0,
     measured, and it is a REGRESSION against the driver this replaces. An empty side counts as
     token-only.
  4. Any other region is emitted as a conflict, and each token inside it is replaced by the row line
     from the SIDE OF THE REGION IT APPEARS ON — never by `resolved[key]`, whose value can itself be
     a marker block. Nested markers close the outer region early and leak unresolved lines into the
     view all four postconditions read; per side, they cannot.

Rule 3 is the whole design. Both sides of a diff hunk sit between the same context lines, so when
every disputed line is a row, section membership is not in dispute — only order among siblings,
which is not semantic, because ids are labels and not ranks. Rule 4 is its converse. Held as one
sentence: THE DRIVER MAY AUTO-RESOLVE WHERE GIT CONFLICTS ONLY WHEN EVERY DISPUTED LINE IS A ROW
TOKEN; A DISPUTED STRUCTURE LINE IS ALWAYS A CONFLICT.

THE CONFLICT STYLE IS PINNED AT THE CALL SITE and that is load-bearing, not tidiness. `git
merge-file` honours the invoking repo's `merge.conflictStyle`, and git runs a merge driver from the
top of the worktree, so a node-local `diff3`/`zdiff3` reaches this process. Under three sections
rules 3 and 4 are undefined: the region stops being token-only, rule 3 evaporates, and the same
driver returns different verdicts per node on identical blobs. `-c merge.conflictStyle=merge`
overrides a configured style — measured on git 2.54 — and buys determinism at the cost of the base
section in the driver's own conflict output. The three-section shape is still handled defensively
below, and it falls to rule 4.

FOUR POSTCONDITIONS, all over the WRITTEN BYTES and on EVERY verdict, over `settled()` — the merged
lines with conflict regions excised. Bytes and not the in-memory emit list: a terminator defect is
invisible in a list where two glued records are still two elements.

  * `no_new_duplicates` line half — no row-shaped line written more often than the most any ONE
    input carried it. This is what refuses the one shape `git merge-file` itself corrupts.
  * `no_new_duplicates` id half — no id leading more rows than in any one input, under a grammar
    deliberately INDEPENDENT of the driver's own. This is what refuses a re-worded duplicate of an
    unkeyable row, and the redesign makes it MORE load-bearing: with the partition on the row shape,
    an inert anchor grammar no longer conflicts loudly, it quietly hashes.
  * `no_misfiled_rows` — no keyed row under a heading no input filed it under. Rule 3 makes
    misfiling structurally unreachable, so this is a backstop; it stays because it is the one
    postcondition that has already caught real damage and it costs a single pass.
  * `no_row_loss` — CONSERVATION. For every key, the count of that key's row lines in the settled
    output equals the number of entries the row plane resolved it to. Keys resolved to a conflict
    block, and keys inside a rule-4 region, are excluded because `settled()` excises their lines by
    design. "That row appears exactly once" is the BANNED wording: it is false for a file carrying a
    legitimately repeated row line, and stating it that way turns an identity merge into a permanent
    whole-file conflict.
  * `structure_identity` — the output's non-row, NON-MARKER lines equal the merged skeleton's
    non-token, NON-MARKER lines, in order, byte for byte. Markers are excluded on BOTH sides and
    that word is load-bearing: the skeleton carries git's markers and the output does not carry the
    same ones, so an asymmetric form is unequal by construction on every conflicted merge AND on
    every rule-3 auto-resolve — it would break the headline case this unit exists for.

THE NEWLINE CONTRACT, seven sites. `read`'s `newline=""`; `text_merge`'s `newline=""` write, its
byte capture and manual decode; `main`'s `write_bytes`. Then: (5) a token carries the terminator of
the row it replaces, so the skeleton is not a mixed-terminator file; (6) every marker line the
DRIVER synthesizes carries the file's dominant terminator, computed over `%A`; (7) a row line
substituted for a token carries the terminator of the TOKEN's position in the merged skeleton, never
the one it carried in its source blob. Site 7 is not a refinement. Measured: ours appending an
unterminated final row while theirs appends a terminated one made rule 3 emit ours' token first, the
empty terminator rode along, and `"".join` FUSED TWO RECORDS ONTO ONE LINE at rc 0 with no markers
and a `clean` audit line, where the `git merge-file` control returns rc 1 with both rows intact.

Exit 0 = merged clean. Exit 1 = conflict markers written to %A; git leaves the path unmerged.
Exit 2 = called with fewer than the three input paths (usage).
"""
# Annotations as strings, the same house rule `extract.py` and `map_lib.py` follow. `resolve_python`
# imposes NO version floor — every candidate is accepted on `-c "import sys"` alone — so the
# interpreter a node hands this driver is whatever it has, and a `str | None` in a signature is
# evaluated at def time without this line.
from __future__ import annotations

# Module scope, unlike `extract` and `tempfile` below: this import runs BEFORE `anchors()` appends
# the memory-recall kit to `sys.path`, so the shadowing the deferred imports guard against cannot
# reach it.
import hashlib
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

    THERE IS NO DEGRADED MODE. Falling back to hashing every row would still beat `git merge-file`,
    and that is exactly the trap: the file would merge under a different rule than the one
    configured, silently, on the path where the kit is already broken.
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


class DuplicatedContent(RuntimeError):
    """A duplicate postcondition refused the result. Raised, never printed-and-continued."""


class Misfiled(RuntimeError):
    """The placement postcondition refused the result. Raised, never printed-and-continued."""


class RowLoss(RuntimeError):
    """The CONSERVATION postcondition refused the result: a key's row count does not match.

    Not a uniqueness failure. The question is whether the number of lines written for a key equals
    the number the row plane resolved it to — in BOTH directions, so a loss and a duplication are
    the same refusal seen from two sides.
    """


class StructureDrift(RuntimeError):
    """The structure plane and the written file disagree, or the reconstruction is unsound.

    Every member is a should-never-fire invariant on the driver's own construction — a sentinel that
    survived into the output, an unterminated interior line, a region shape git cannot have written.
    Raising lands in `main()`'s fail-closed handler, which is the right direction: a whole-file
    conflict the author resolves by hand beats a file whose bytes the driver cannot account for.
    """


# A RECORD is a row. Every governed index writes one record per `- `/`* ` line, and this predicate is
# the whole reason the duplicate postconditions can be strict without redding a legitimate merge: a
# repeated ROW is corruption, a repeated HEADING is two sections that happen to share a name. Both are
# "a line written twice" and nothing at the line level tells them apart, so the population is named
# here instead of guessed there. It is also the ONLY partition predicate — stateless, one line at a
# time, no parser state, because state is where all three rounds of defects lived.
_ROW_RE = re.compile(r"^\s*[-*]\s")
# Deliberately INDEPENDENT of the driver's own anchor grammar, and not imported from it. The keyed
# path already guarantees uniqueness for what `key()` keys; this exists for the population it does
# NOT key. Keying the postcondition on the same regex as the merge would make it self-consistent and
# blind: an id the grammar stopped recognising would drop out of BOTH the merge and the check on the
# merge.
#
# THE POPULATION IS RE-GROUNDED, because the one this comment used to name is gone. It said "the
# ratified `…-9b` correction form, which the shared session era's trailing `\b` rejects" — true until
# memory-recall kit 1.1 widened that era to `\d+[a-z]*`, after which `- TOOL-zFix-9b · text` keys
# like any other row. It was also wrong in the other direction the whole time: this pattern demands
# `<FAMILY>-<slug>-<digits>` and so is NARROWER than the anchor grammar for both flat eras
# (`ARCH-001`, `ABL-d119` match there and not here). Neither error emptied it. Measured under the
# widened grammar, the live population is a ROW-SHAPED LINE CARRYING AN ID AND NO ANCHOR SEPARATOR:
# every anchor pattern requires `[-—:·]` or `[·|]` after the id, this pattern requires nothing, so
# `- TOOL-zFix-9b carries an id but no anchor separator` is invisible to `key()` and visible here.
# That difference is structural rather than lexical, which is why it is the one worth standing on: an
# era can widen again, and a separator cannot be granted by widening one. `merge-rows.test.sh` case
# 0d asserts both halves live before any arm leans on them.
_ID_RE = re.compile(r"\b[A-Z]+-[A-Za-z0-9]+-[0-9]+[a-z]*\b")
# A marker line is INVENTED by the merge, so it has no input count to be measured against, and the
# same three markers legitimately repeat once per conflicting region. `|||||||` is written under
# diff3 style, which `text_merge` now overrides at the call site — it is still recognised here
# because recognising a shape the driver refuses to request costs nothing and mis-reading one is how
# a base section leaks into the ours side.
_OPEN, _CLOSE, _SEP, _BASE = "<<<<<<<", ">>>>>>>", "=======", "|||||||"
_MARKER_RE = re.compile(r"^(?:<<<<<<<|>>>>>>>|=======|\|\|\|\|\|\|\|)")
_HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s")
# The token delimiter. Fail-closed in both directions: no INPUT line may contain it (so tokenization
# is unambiguous) and no OUTPUT line may (so a reconstruction bug is caught before it reaches the
# worktree).
_SENT = "\x01"


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

    The backstop for everything the anchor grammar cannot key. The row plane guarantees conservation
    for every key; this is the check that the KEYS themselves did not launder a duplicate — two
    nodes minting the same unkeyable row in different regions produce two distinct `raw:` keys with
    identical text, and nothing in the row plane can see that they are the same record.

    TWO HALVES, because the line half alone is blind to a re-worded duplicate. Two nodes each minting
    the same unkeyable id with different prose produce two DIFFERENT lines, so the line census sees
    each once, the cap holds, and the id lands twice in an append-only record at exit 0 — measured.
    So the same rule is lifted from line to record. The population is named at `_ID_RE`: a row-shaped
    line carrying an id and no anchor separator.
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
    row, so a scan scoped to the rows would report `None` for every PLAY row and see no misfiling
    when one moved out.
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


def _unmarked(lines: list[str]) -> list[str]:
    """`lines` with the MARKER lines dropped and every content line kept.

    The placement view, and deliberately not `settled()`. Excision is right for the duplicate
    question — a conflict hunk repeats content from both sides by construction — and WRONG for the
    section question, because a hunk's headings still bound the sections around it. Measured: two
    nodes renaming the same heading differently puts that heading inside a region, `settled()` drops
    both versions, and every row below it reads as having moved to whatever heading precedes the
    region. `no_misfiled_rows` then refuses a correct, scoped, one-hunk conflict and `main()`'s
    fail-closed handler converts it into a whole-file marker sandwich — the ergonomics complaint,
    manufactured by the check rather than found by it.
    """
    return [ln for ln in lines if not _MARKER_RE.match(ln.lstrip())]


def no_misfiled_rows(merged: list[str], *inputs: list[str]) -> None:
    """Refuse to file a row under a heading no input filed it under.

    A BACKSTOP now rather than the primary mechanism. Placement no longer comes from a splice this
    driver computes; it comes from git's own diff of the skeleton, and rule 3 only ever concatenates
    within a region whose context lines both sides share. So misfiling is structurally unreachable —
    which is an argument for keeping the check cheap, not for deleting it. It is the one
    postcondition that has already caught real damage (a `PLAY` decision auto-committed under
    `## KICK`; a row filed under `## closed` because ours relocated the neighbour it arrived behind)
    and it costs a single pass.

    "An input that carries it", not "%A", deliberately: a row whose section is unchanged on both
    sides has one answer, and a row only one side carries has exactly one input to answer for it.
    """
    clean = sections(_unmarked(merged))
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
    """Ordinary three-way text merge, via `git merge-file`. The single call site, for the skeleton.

    THE CONFLICT STYLE IS PINNED, and that is the one contract change this redesign makes to a
    retained function. `git merge-file` honours the invoking repo's `merge.conflictStyle`, and git
    runs a merge driver from the top of the worktree, so a node that set `diff3` or `zdiff3` gets a
    third `||||||| base` section here. Reconciliation rules 3 and 4 are defined over an ours side and
    a theirs side; under three sections rule 3 evaporates and every auto-resolve this unit exists for
    vanishes on that node only — the same driver answering two ways on identical blobs. `-c` wins
    over a configured value (measured, git 2.54), so the region shape reaching the rules cannot be
    changed by an adopter's config. The cost is that the driver's own conflict output carries no base
    section even where the adopter asked for one.
    """
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
        r = subprocess.run(["git", "-c", "merge.conflictStyle=merge",
                            "merge-file", "-p", "-L", "ours", "-L", "base", "-L", "theirs",
                            str(p / "a"), str(p / "o"), str(p / "b")],
                           capture_output=True)
        # SITE 3 of the newline contract, and the one upstream does not solve: it passes
        # `text=True`, which is universal-newline mode, so a CRLF region comes back as LF and the
        # careful `newline=""` two lines up is undone. Capture BYTES and decode by hand instead —
        # this repo's nodes run `core.autocrlf=true` and the governed indexes are CRLF in the
        # worktree, which is exactly the format git hands a merge driver.
        return r.stdout.decode("utf-8", "replace").splitlines(keepends=True), r.returncode != 0


# --------------------------------------------------------------------------------------------
# The skeleton
# --------------------------------------------------------------------------------------------

def _split_term(line: str) -> tuple[str, str]:
    """(body, terminator). The empty terminator of an unterminated final line is a real answer."""
    for t in ("\r\n", "\n", "\r"):
        if line.endswith(t):
            return line[:-len(t)], t
    return line, ""


def _dominant(lines: list[str]) -> str:
    """The file's dominant line terminator — site 6, computed over `%A`, LF when empty or tied."""
    n = {"\r\n": 0, "\n": 0, "\r": 0}
    for ln in lines:
        t = _split_term(ln)[1]
        if t:
            n[t] += 1
    top = max(n.values())
    winners = [t for t, c in n.items() if c == top]
    return "\n" if top == 0 or len(winners) != 1 else winners[0]


def _row_key(line: str) -> str:
    """The row plane's key for a row-shaped line: its id when the grammar keys it, else a digest.

    The digest is over the STRIPPED text, which is what makes line form unable to smuggle a
    duplicate past the plane: a final copy with no newline and an interior copy with one hash the
    same. `row:`/`raw:` prefixes keep the two namespaces from colliding and make the audit line's
    keyed/hashed split derivable from the keys themselves.
    """
    k = key(line)
    if k is not None:
        return "row:" + k
    return "raw:" + hashlib.sha1(line.strip().encode("utf-8", "replace")).hexdigest()[:16]


def _token_of(body: str) -> str | None:
    """The key a token line names, or None when the line is structure."""
    if len(body) > 2 and body.startswith(_SENT) and body.endswith(_SENT):
        return body[1:-1]
    return None


def skeleton(lines: list[str]) -> tuple[list[str], dict[str, list[str]]]:
    """(the line list with every ROW replaced by its token, key -> the BODIES of its row lines).

    Bodies and not lines: the terminator a row carried in its source blob is used HERE, on the
    token, and nowhere else. On the way back a substituted row takes the terminator of the TOKEN's
    position in the merged skeleton (site 7), so carrying the source terminator any further is what
    fuses two records onto one line when the merge relocates a formerly-final row.
    """
    skel: list[str] = []
    rows: dict[str, list[str]] = {}
    for ln in lines:
        body, term = _split_term(ln)
        if not _ROW_RE.match(ln):
            skel.append(ln)
            continue
        k = _row_key(ln)
        rows.setdefault(k, []).append(body)
        skel.append(_SENT + k + _SENT + term)
    return skel, rows


# --------------------------------------------------------------------------------------------
# The row plane
# --------------------------------------------------------------------------------------------

def _quote(entries: list[tuple]) -> str:
    """The row TEXT behind a key, for a refusal message.

    A `raw:` key is a digest, so a refusal that names only the key tells an author nothing about
    which line the driver refused over — and every one of these refusals lands in front of a human
    resolving a merge by hand. The keyed half is legible on its own and quoted the same way, because
    two message shapes for one failure is a worse cost than one redundant id.
    """
    for kind, payload in entries:
        if kind == "row":
            return repr(payload.strip()[:72])
    return "a conflict block"


def _conflict(ours: list[str] | None, theirs: list[str] | None) -> tuple:
    """A marker block, as BODIES. Site 6 attaches the dominant terminator at emit time."""
    open_ln = _OPEN + " ours" + ("" if ours is not None else " (deleted)")
    close_ln = _CLOSE + " theirs" + ("" if theirs is not None else " (deleted)")
    return ("conflict", [open_ln] + list(ours or []) + [_SEP] + list(theirs or []) + [close_ln])


def resolve_rows(O: dict, A: dict, B: dict) -> dict[str, list[tuple]]:
    """key -> the LIST of entries it resolves to. An entry is one row body, or one marker block.

    A pure per-key decision with NO ordering — ordering is the skeleton's job. `key -> LIST` and
    never `key -> line`: a file may legitimately carry the same row-shaped line twice, and collapsing
    those made it fail its own identity merge.

    The resolved list is the branch's own list, which on every branch where both sides keep the
    content is `max(len(A[k]), len(B[k]))`. It is deliberately NOT forced to that maximum on the
    branch where one side is unchanged and the other REMOVED a copy of a repeated row: forcing the
    max there resurrects a deletion the author made.

    THE DELETE COMPARISON IS THE ROW LINE ALONE, and that is correct rather than a relapse. The
    defect that forced a lead-in-plus-anchor comparison was that a side which filed content ABOVE a
    deleted row read as untouched and its content was discarded. In this design there is no lead-in:
    adjacent structure lines are on the other plane and merged by git, and an adjacent ROW is a
    separate key with its own decision. The concept the repair repaired no longer exists.

    A `raw:` key cannot be "in both sides with different text", because different text is a different
    key. Editing an unkeyable row therefore reads as a delete of the old key plus an add of the new
    one — right in the one-sided case, and keeping BOTH wordings in the both-sides case. That last
    outcome is deliberate and guarded: if the row carries an id, `no_new_duplicates`' id half refuses
    it; if it carries none, it is a note and not a record, and keeping both is what an append-only
    record does.
    """
    resolved: dict[str, list[tuple]] = {}
    order = list(O) + [k for k in A if k not in O] + [k for k in B if k not in O and k not in A]
    rows = lambda bodies: [("row", b) for b in bodies]  # noqa: E731 — one expression, used thrice
    for k in order:
        in_o, in_a, in_b = k in O, k in A, k in B
        if in_a and in_b:
            if A[k] == B[k]:
                entries = rows(A[k])
            elif not in_o:
                entries = [_conflict(A[k], B[k])]     # both minted it, differently
            elif O[k] == A[k]:
                entries = rows(B[k])                  # only theirs changed it
            elif O[k] == B[k]:
                entries = rows(A[k])                  # only ours changed it
            else:
                entries = [_conflict(A[k], B[k])]     # all three differ
        elif in_a:
            if not in_o:
                entries = rows(A[k])                  # ours added it; theirs never saw it
            elif O[k] == A[k]:
                entries = []                          # theirs deleted what ours left alone — honour
            else:
                # DELETE/MODIFY: ours edited it, theirs deleted it. Silently keeping ours would
                # discard a deliberate delete; silently dropping ours would discard a deliberate
                # edit. Neither is ours to choose.
                entries = [_conflict(A[k], None)]
        elif in_b:
            if not in_o:
                entries = rows(B[k])                  # theirs added it
            elif O[k] == B[k]:
                entries = []                          # ours deleted what theirs left alone — honour
            else:
                entries = [_conflict(None, B[k])]     # the mirror, and the one that lost data
        else:
            entries = []                              # in %O only — both deleted it
        resolved[k] = entries
    return resolved


# --------------------------------------------------------------------------------------------
# Reconciliation
# --------------------------------------------------------------------------------------------

def _parse_region(block: list[str]) -> dict:
    """Split one conflict region into its sections. Raises when the shape is not one git writes."""
    open_ln, close_ln = block[0], block[-1]
    body = block[1:-1]
    sep = base_mark = None
    for i, ln in enumerate(body):
        s = ln.lstrip()
        if base_mark is None and s.startswith(_BASE):
            base_mark = i
        if s.startswith(_SEP):
            sep = i
            break
    if sep is None:
        raise StructureDrift("a conflict region carries no '=======' separator — "
                             "the merged skeleton is not a shape git merge-file writes")
    if base_mark is None:
        return {"open": open_ln, "ours": body[:sep], "basemark": None, "base": [],
                "sep": body[sep], "theirs": body[sep + 1:], "close": close_ln}
    return {"open": open_ln, "ours": body[:base_mark], "basemark": body[base_mark],
            "base": body[base_mark + 1:sep], "sep": body[sep], "theirs": body[sep + 1:],
            "close": close_ln}


def _region_end(skel: list[str], i: int) -> int:
    for j in range(i + 1, len(skel)):
        if skel[j].lstrip().startswith(_CLOSE):
            return j
    raise StructureDrift("a conflict region in the merged skeleton is never closed")


def _token_only(sec: dict) -> bool:
    """Rule 3's predicate. An empty side counts as token-only; a base section never does."""
    if sec["basemark"] is not None:
        return False
    return all(_token_of(_split_term(ln)[0]) is not None
               for ln in sec["ours"] + sec["theirs"])


def reconcile(skel: list[str], resolved: dict, O: dict, A: dict, B: dict, term: str) -> tuple:
    """Walk the merged skeleton and apply the four rules. Returns (lines, facts)."""
    out: list[str] = []
    cursor: dict[str, int] = {}
    conflict_done: set[str] = set()
    region_keys: set[str] = set()
    n_regions = 0

    def take(k: str, t: str) -> list[str]:
        """Rule 2. One token occurrence consumes one entry of `resolved[k]`."""
        entries = resolved.get(k)
        if entries is None:
            raise RowLoss(f"the merged skeleton carries a token for {k!r} that the row plane never "
                          f"resolved — a row would be written that no input carries")
        if not entries:
            # A DELETE THE ROW PLANE HONOURED. The token survives git's merge of the skeleton
            # whenever the deletion abuts a change on the other side, and dropping it here is what
            # turns that shape from git's refusal into an auto-resolve: the delete is honoured AND
            # whatever the other side filed next to it is kept, because that content is a separate
            # key with its own decision. Refusing instead would red an ordinary honoured delete.
            return []
        i = cursor.get(k, 0)
        if i >= len(entries):
            # A marker block speaks for EVERY occurrence of its key, so a second token for a
            # conflicted key emits nothing rather than refusing.
            if k in conflict_done:
                return []
            raise RowLoss(
                f"key {k!r}: the merged skeleton carries its token {i + 1} time(s) and the row plane "
                f"resolved it to {len(entries)} — {_quote(entries)} would be written twice or "
                f"invented")
        cursor[k] = i + 1
        kind, payload = entries[i]
        if kind == "row":
            return [payload + t]                       # SITE 7: the TOKEN's terminator, not the row's
        conflict_done.add(k)
        return [b + term for b in payload]             # SITE 6: synthesized markers, dominant term

    def per_side(sec_lines: list[str], side: dict, seen: dict) -> list[str]:
        """Rule 4. A token is replaced by the row from the side of the region it appears on."""
        got: list[str] = []
        for ln in sec_lines:
            body, t = _split_term(ln)
            k = _token_of(body)
            if k is None:
                got.append(ln)
                continue
            region_keys.add(k)
            bodies = side.get(k)
            if bodies is None:
                bodies = O.get(k) or A.get(k) or B.get(k)
            i = seen.get(k, 0)
            if not bodies or i >= len(bodies):
                # Unreachable by construction — a region's ours side is a slice of %A's skeleton and
                # its theirs side a slice of %B's, so the bodies are there. Refusing is the
                # fail-closed direction if that ever stops being true.
                raise StructureDrift(f"key {k!r} appears in a conflict region more often than the "
                                     f"side it is on carries it")
            seen[k] = i + 1
            got.append(bodies[i] + t)
        return got

    i = 0
    while i < len(skel):
        ln = skel[i]
        if ln.lstrip().startswith(_OPEN):
            j = _region_end(skel, i)
            sec = _parse_region(skel[i:j + 1])
            if _token_only(sec):
                # RULE 3. Positional concatenation: ours in order, then theirs. A theirs-side token
                # is suppressed only when the same key also occurs on OURS' side — ACROSS sides and
                # never within one. The within-side form is set union wearing a rule's clothes, and
                # it deletes a legitimately repeated note out of an append-only record at rc 0.
                ours_keys = {_token_of(_split_term(x)[0]) for x in sec["ours"]}
                for x in sec["ours"]:
                    body, t = _split_term(x)
                    out.extend(take(_token_of(body), t))
                for x in sec["theirs"]:
                    body, t = _split_term(x)
                    k = _token_of(body)
                    if k in ours_keys:
                        continue
                    out.extend(take(k, t))
            else:
                # RULE 4. The moment a structure line is in dispute, the structure is in dispute —
                # and structure is precisely the class git is right about and this driver has been
                # wrong about three times.
                n_regions += 1
                seen: dict[str, int] = {}
                out.append(sec["open"])
                out.extend(per_side(sec["ours"], A, seen))
                if sec["basemark"] is not None:
                    out.append(sec["basemark"])
                    out.extend(per_side(sec["base"], O, seen))
                out.append(sec["sep"])
                out.extend(per_side(sec["theirs"], B, seen))
                out.append(sec["close"])
            i = j + 1
            continue
        body, t = _split_term(ln)
        k = _token_of(body)
        if k is None:
            out.append(ln)                             # RULE 1
        else:
            out.extend(take(k, t))
        i += 1

    # CONSERVATION AT THE CONSTRUCTION LEVEL, the other direction from `take`'s. Every entry the row
    # plane resolved must have been consumed, unless the key lives inside a rule-4 region where
    # `settled()` excises it by design.
    for k, entries in resolved.items():
        if k in region_keys or k in conflict_done:
            continue
        if cursor.get(k, 0) != len(entries):
            raise RowLoss(
                f"key {k!r}: the row plane resolved {len(entries)} row(s) and the merged skeleton "
                f"carries {cursor.get(k, 0)} token(s) — a row would be lost")
    return out, {"regions": n_regions, "conflicts": conflict_done, "region_keys": region_keys}


# --------------------------------------------------------------------------------------------
# The two new postconditions
# --------------------------------------------------------------------------------------------

def no_row_loss(merged: list[str], resolved: dict, facts: dict) -> None:
    """CONSERVATION, over the written bytes: each key's row count equals what the plane resolved.

    NOT a uniqueness check, and the distinction is the whole point. "That row appears exactly once"
    is false for a file that legitimately carries the same row-shaped line twice, and asserting it
    that way turns an IDENTITY merge of such a file into a permanent whole-file conflict no author
    can clear — measured.

    Keys resolved to a marker block, and keys inside a rule-4 region, are excluded: `settled()`
    excises their lines by design, so their count here is zero for a reason that is not loss.
    """
    excluded = facts["conflicts"] | facts["region_keys"]
    seen: dict[str, int] = {}
    for ln in settled(merged):
        if not _ROW_RE.match(ln):
            continue
        seen[_row_key(ln)] = seen.get(_row_key(ln), 0) + 1
    bad = []
    for k in sorted(set(seen) | set(resolved)):
        if k in excluded:
            continue
        got = seen.get(k, 0)
        want = len(resolved.get(k, []))
        if k not in resolved:
            bad.append((k, got, "no input carries it", "?"))
        elif got != want:
            bad.append((k, got, str(want), _quote(resolved[k])))
    if bad:
        k, got, want, txt = bad[0]
        raise RowLoss(f"{len(bad)} key(s) written a different number of times than the row plane "
                      f"resolved them, e.g. {k!r} ({txt}) written x{got} against {want}")


def structure_identity(merged: list[str], skel: list[str]) -> None:
    """The output's structure is the merged skeleton's structure, byte for byte, in order.

    MARKERS ARE EXCLUDED ON BOTH SIDES and that word is load-bearing. The skeleton carries git's own
    `<<<<<<< ours` / `=======` / `>>>>>>> theirs`; the output carries the driver's, in different
    places and different numbers. Excluding them on the output side only makes the two lists unequal
    BY CONSTRUCTION on every conflicted merge and on every rule-3 auto-resolve — it would refuse the
    headline case this unit exists for.

    Cheap, total, and it is the assertion that says out loud that structure correctness here is a
    property of CONSTRUCTION rather than of a heuristic.
    """
    want = [ln for ln in skel
            if not _MARKER_RE.match(ln.lstrip()) and _token_of(_split_term(ln)[0]) is None]
    got = [ln for ln in merged
           if not _MARKER_RE.match(ln.lstrip()) and not _ROW_RE.match(ln)]
    if want == got:
        return
    for i, (w, g) in enumerate(zip(want, got)):
        if w != g:
            raise StructureDrift(f"structure line {i} of the output is {g!r} where the merged "
                                 f"skeleton has {w!r}")
    raise StructureDrift(f"the output carries {len(got)} structure line(s) where the merged "
                         f"skeleton has {len(want)}")


# --------------------------------------------------------------------------------------------

def merge(o_lines, a_lines, b_lines) -> tuple[list[str], bool]:
    for name, side in (("%O", o_lines), ("%A", a_lines), ("%B", b_lines)):
        for n, ln in enumerate(side, 1):
            if _SENT in ln:
                raise StructureDrift(f"{name} line {n} contains the token sentinel U+0001, so "
                                     f"tokenization cannot be unambiguous")
    term = _dominant(a_lines)
    o_skel, O = skeleton(o_lines)
    a_skel, A = skeleton(a_lines)
    b_skel, B = skeleton(b_lines)
    resolved = resolve_rows(O, A, B)
    # The bool is deliberately discarded: whether the SKELETON conflicted is not the verdict. A
    # token-only region becomes an auto-resolve (rule 3) and any other becomes a conflict (rule 4),
    # and the verdict below is read off the bytes actually written.
    skel, _ = text_merge(o_skel, a_skel, b_skel)
    # Only the line that ends the file may be unterminated. Normalising the SKELETON rather than the
    # output is what makes site 7 total: every token then carries a real terminator, so a substituted
    # row cannot inherit an empty one from a formerly-final position and fuse with its neighbour.
    skel = [ln if ln.endswith(("\n", "\r")) else ln + term for ln in skel[:-1]] + skel[-1:]

    out, facts = reconcile(skel, resolved, O, A, B, term)
    for n, ln in enumerate(out[:-1], 1):
        if not ln.endswith(("\n", "\r")):
            raise StructureDrift(f"output line {n} carries no terminator and is not the last line — "
                                 f"joining would fuse two records onto one line")
    merged = "".join(out).splitlines(keepends=True)
    for n, ln in enumerate(merged, 1):
        if _SENT in ln:
            raise StructureDrift(f"output line {n} still carries a token sentinel — a token was not "
                                 f"substituted")

    # ALL FIVE POSTCONDITIONS, on EVERY verdict, over the WRITTEN BYTES, and BEFORE the audit line is
    # printed — a run about to refuse must not first announce a clean result. Bytes and not the emit
    # list: a terminator defect is invisible in a list where two glued records are still two
    # elements, and both new postconditions passed a list-level reading of the exact corruption they
    # exist to catch.
    no_new_duplicates(merged, o_lines, a_lines, b_lines)
    no_misfiled_rows(merged, o_lines, a_lines, b_lines)
    no_row_loss(merged, resolved, facts)
    structure_identity(merged, skel)

    # THE AUDIT LINE. Every number is derived from the written bytes and the three inputs AFTER the
    # fact — never from a counter incremented at an emit site, which is how the retired line came to
    # print `38 row(s) from ours … clean` on a merge that had just deleted one. `k` and `h` are what
    # make an inert grammar visible during a real merge: on the governed indexes `h` is 0 today, and
    # a FAMILIES drift turns every row hashed without moving any other number.
    clean = settled(merged)
    written = [ln for ln in clean if _ROW_RE.match(ln)]
    keyed = sum(1 for ln in written if key(ln) is not None)
    nrow = lambda side: sum(1 for ln in side if _ROW_RE.match(ln))  # noqa: E731 — used three times
    honoured = sum(1 for k, e in resolved.items() if not e)
    conflicted = any(ln.lstrip().startswith(_OPEN) for ln in merged)
    pairs = sum(1 for ln in merged if ln.lstrip().startswith(_OPEN))
    if pairs != len(facts["conflicts"]) + facts["regions"]:
        raise StructureDrift(
            f"the written file holds {pairs} conflict region(s) against {len(facts['conflicts'])} "
            f"row conflict(s) plus {facts['regions']} structure conflict(s) — the audit line would "
            f"describe a file this is not")
    verdict = "CONFLICT" if conflicted else "clean"
    print(f"merge-rows: rows O/A/B {nrow(o_lines)}/{nrow(a_lines)}/{nrow(b_lines)} -> "
          f"{len(written)} written ({keyed} keyed, {len(written) - keyed} hashed), "
          f"{honoured} deletes honoured, {len(facts['conflicts'])} row conflicts, "
          f"{facts['regions']} structure conflicts, {verdict}", file=sys.stderr)
    return merged, conflicted


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
        # SITE 6 here too: the fail-closed body's markers carry the dominant terminator, so a
        # refusal on a CRLF worktree file does not write three LF lines into it. And ours' own final
        # line is terminated before `=======` follows it — an unterminated last line is the ordinary
        # shape of "one node's editor left no trailing newline", and joining it to a marker is the
        # same record-fusing defect site 7 closes on the merge path.
        t = _dominant(ours)
        cap = lambda side: [ln if ln.endswith(("\n", "\r")) else ln + t for ln in side]  # noqa: E731
        body = ([_OPEN + " ours" + t] + cap(ours) + [_SEP + t] + cap(theirs)
                + [_CLOSE + " theirs (merge-rows failed; resolve by hand)" + t])
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
