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

CLI: --check (gate), --report (human), --emit-pin (the current counts, for re-pinning), --ages (row
age DERIVED from git rather than stored), --check-rotation (check 24), --selftest.

PROVENANCE. The backlog-row grammar, the two shard pins and `--ages` were written in NicoCares'
fork of this file and taken upstream by TOOL-aRepatriatedFork-9, with two grammar corrections that
corpus could not surface (a frozen legacy id, a parenthesised `CLOSED by` clause) and the third pin
added to `--emit-pin`. Measurements quoted below against `memory/backlog/PKG.md` are that repo's.
"""
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# TOOL-aRepatriatedFork-9 -- the conf parser, the fence reader and the lifecycle vocabulary come from
# `tree_lib.py`, never from a sibling ENGINE. Importing them from `corpus_ids` and `gen_build_index`
# made both a hard prerequisite of this module, and at an adopter whose copies of those two are its
# own programs this check died on import. `scan_engine_imports` below keeps it that way.
from tree_lib import (  # noqa: E402  the kit's shared helpers
    CENSUS_TERMINAL, STATUS_TOKENS, TERMINAL as TERMINAL_STATUS, parse_conf, unfenced_lines,
)

CHECK = 20
# Check 24 rides this module for the same reason 13-20 do: it walks ROW DOCUMENTS, and the row
# grammar lives here. TOOL-cSpliceWarden-6.
ROTATION_CHECK = 24
PIN_KEY = "ROW_DUPLICATE_PIN"
# PKG-dCandidLodestar-61 S5. Spelled as that unit's spec spells it; see `parse_unranked_pins`.
UNRANKED_PIN_KEY = "SEVERITY_UNLABELLED_PIN"
# PKG-dCandidLodestar-61 found this key DECLARED and unread: `.memory-tree.conf` carried it from
# `-59` S5 while no file in the repo compared anything to it. A pin whose value can never be wrong
# is not a pin. It is read here now, through the same `<shard>:<count>` reader, so the live-row
# floor the drain established actually holds.
LIVE_ROW_PIN_KEY = "LIVE_ROW_PIN"


class Problem(Exception):
    """A named, user-facing failure. Never a traceback."""


def run(*argv, cwd=None):
    p = subprocess.run(argv, cwd=cwd, capture_output=True, text=True, encoding="utf-8")
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
        try:
            text = read(os.path.join(root, p))
        except OSError:
            # Tracked but absent from the worktree. Before this branch the open() raised
            # FileNotFoundError straight out of a gate leg, so a deleted-but-tracked row document
            # ended check 20 in a traceback rather than in the named failure this module's own
            # Problem docstring promises. Named, and TERMINAL for the same reason the open-fence
            # branch is: a duplicate hiding in a file nobody could read is invisible either way.
            raise Problem(f"row-grammar: {p} is tracked but is not on disk, so its rows could not "
                          f"be read — a document nobody can open is not a drained one")
        for n, line in unfenced_lines(text):
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


def parse_unranked_pins(conf):
    """-> {shard-path: ceiling} from `SEVERITY_UNLABELLED_PIN`, or {} when it is undeclared.

    POLARITY, and why the default here is the OPPOSITE of `pin_of`'s. That pin's strictest value is
    0 and a young tree can honestly carry it, so an undeclared key can safely mean "tolerate
    nothing". This one is a ceiling over a population of 200 inherited rows: the strict value is
    unreachable, and any default this function could invent would either red the tree on adoption
    or invent a number nobody measured. So undeclared means UNARMED — and `cmd_check` says so out
    loud on every run rather than passing quietly, because a ratchet nobody armed and nobody
    mentions is indistinguishable from one that is holding.

    That is not a hypothetical. `LIVE_ROW_PIN` was declared in `.memory-tree.conf` by
    `PKG-dCandidLodestar-59` S5 and, measured at 32bf8c15, is read by no file in this repo — a pin
    whose value can never be wrong because nothing compares anything to it. The announcement below
    is what stops this key becoming the second one.

    Format is `LIVE_ROW_PIN`'s, deliberately: space-separated `<shard-path>:<count>` tokens, so the
    two pins over the same shards are read the same way and an operator learns one spelling.
    """
    return _parse_shard_pins(conf, UNRANKED_PIN_KEY)


def parse_live_row_pins(conf):
    """-> {shard-path: ceiling} from `LIVE_ROW_PIN`, or {} when it is undeclared.

    Same polarity and same announcement as `parse_unranked_pins`: undeclared means UNARMED and says so in
    the green output. This key spent one wave declared and unread, which is the state that arm
    exists to make impossible.
    """
    return _parse_shard_pins(conf, LIVE_ROW_PIN_KEY)


def _parse_shard_pins(conf, key):
    """The one `<shard-path>:<count>` parse, shared so the two pins cannot drift in spelling."""
    raw = conf.get(key, "").strip()
    if raw == "":
        return {}
    pins = {}
    for tok in raw.split():
        shard, sep, count = tok.rpartition(":")
        if not sep or not shard or not count.isdigit():
            raise Problem(f"row-grammar: {key} takes `<shard-path>:<count>` tokens, got '{tok}'")
        pins[shard] = int(count)
    return pins


# =========================================================================== THE EXPORTED GRAMMAR
# PKG-dCandidLodestar-59 S3/S4. One parse of a backlog row, so `PKG-dCandidLodestar-61` (severity
# backfill) and `PKG-dCandidLodestar-65` (`opened:` backfill) build their fields on ONE shape rather
# than inventing a fourth predicate. `scan()` above is DELIBERATELY not folded into this: it answers
# "is this line keyable and unique in its file", a per-file uniqueness question over every row
# document; this answers "what are this row's fields", and only the backlog shards carry status.
#
# WHY THIS IS A PARSE AND NOT A REGEX EVERY CALLER RE-SPELLS. Three predicates in this tree answered
# "how many live rows does memory/backlog/PKG.md carry" and returned three numbers. Measured at
# 8c8661a2:
#
#   plain `^- <ID> · <LIVE> · `                       260   misses the bolded id AND the 7 qualified
#   the same, tolerant of `**`                        261   misses the 7 comma-qualified statuses
#   drift_report.build_live_backlog_rows              271   counts DEFERRED and both `CLOSED by` rows
#
# The truth under this grammar is 268, and none of the three printed it. That is the repo's own
# `two-answers-to-one-question` class with a third answer bolted on. (NicoCares' corpus throughout
# this block; see the module docstring.)
#
# THE FOUR DIVERGENCES, each a deliberate ruling rather than an accident:
#
#  1. `DEFERRED` IS TERMINAL. `memory/TEMPLATE-SPEC.md` and the charter's DoD both name CLOSED /
#     DEFERRED / WONTDO as the terminal set a spec header flips to, and this unit's own §6 AC1
#     spells live as OPEN|SPECCED|INPROGRESS|BLOCKED. `drift_report.py`'s `_TERMINAL_STATUSES` is
#     `("CLOSED", "WONTDO")` only, so it reads the one DEFERRED row live. That is the difference; it
#     is named here rather than silently reconciled, because a report-only signal counting a
#     deferred row as outstanding work is defensible and a GATE doing it is not. BOTH sets are
#     declared in `tree_lib.py` (`TERMINAL` for the index and check 24, `CENSUS_TERMINAL` here), so
#     the difference is one decision in one place — TOOL-aRepatriatedFork-9's section 8 F1.
#  2. A COMMA-QUALIFIED STATUS KEYS ON ITS FIRST TOKEN. Seven live rows read `OPEN, BACKEND`,
#     `OPEN, OPERATOR` or `BLOCKED, BACKEND`. Both `· <STATUS> · ` predicates drop all seven, so the
#     rows most likely to carry a security finding are the ones the count cannot see.
#  3. `CLOSED by <id>` KEYS AS CLOSED, with the id returned. `memory/backlog/PKG.md` documents this
#     form and three shipped rows use it, yet `drift_report`'s substring test looks for `· CLOSED ·`
#     and reads every one of them LIVE, while `check_core_ask_closures.ASK_ID` needs `([A-Z]+) ·`
#     and cannot see them at all. A closure form the file prescribes and no reader parses is worse
#     than one nobody uses.
#  4. AN ID-LESS ROW IS CLASSIFIED, NOT DROPPED. `memory/backlog/BRAND.md` carries nine rows in a
#     pre-dash `STATUS BRAND — text` form and two dash rows whose id is the bare family. Hygiene
#     check 8 needs a leading `-` or `|` AND an id-shaped token on one line, so all eleven are
#     invisible to it: eleven live rows nothing measures. They parse here as `legacy` and `unkeyed`
#     and they COUNT, which is the whole point of measuring a live set.
#
# WHAT IS DEFINED BUT NOT POPULATED. `severity` is returned raw and is NOT validated against a
# vocabulary: 24 rows carry one and the tokens observed run MED / LOW / HIGH / CORE ASK / GATE GAP /
# LEFT-SHIFT OWED and a dozen more, so a closed enum here would red the corpus on day one and hand
# `-61` a fight it has not chosen yet. `opened` has its PLACE fixed (immediately after severity,
# `opened: YYYY-MM-DD`) and zero rows carry it; `-65` populates it. Fixing the slot now is what
# stops `-65` from having to move every severity token to make room.

# DERIVED from the one vocabulary rather than retyped, so `STATUS_VOCAB` equals
# `tree_lib.STATUS_TOKENS` as a set by construction and a token added there is classified here.
TERMINAL_STATUSES = CENSUS_TERMINAL
LIVE_STATUSES = tuple(s for s in STATUS_TOKENS if s not in CENSUS_TERMINAL)
STATUS_VOCAB = LIVE_STATUSES + TERMINAL_STATUSES

# Longest-first, so `INPROGRESS` cannot be shadowed and `CLOSED` cannot swallow a longer neighbour.
_STATUS_ALT = "|".join(sorted(STATUS_VOCAB, key=len, reverse=True))
# An id, or the BARE FAMILY a row may carry instead. Written family-independently on purpose: the
# family alternation is `id_pattern`'s job and a row whose family is not declared is still a row
# whose status a census must count. Refusing it here would delete eleven BRAND rows from the answer.
#
# ANY NUMBER OF DASH SEGMENTS, not "bare family or family-slug-seq" (TOOL-aRepatriatedFork-9). The
# two-shape pattern the fork shipped had nothing between them, and inCMS carries FROZEN legacy-era
# ids exactly there — `ABL-015`, `DPL-a012`, `PBL-011` — so 58 of its 796 dash-led backlog rows read
# as prose, 54 of them live: the under-count this grammar exists to end, moved to the next corpus.
# Measured 2026-09-23 on node a under this pattern: gov 629 of 629 rows, inCMS 796 of 796, and
# NicoCares' live count unchanged at 196. `keyed` still means "carries at least one dash".
_ROW_ID = r"[A-Z][A-Za-z0-9]{1,9}(?:-[A-Za-z0-9]+)*"
_MIDDOT = "·"

_DASH_ROW = re.compile(
    r"^\s*[-*]\s+"
    r"(?P<wrap>\*\*|`|)(?P<id>" + _ROW_ID + r")(?P=wrap)"
    r"\s*" + _MIDDOT + r"\s*(?P<status>" + _STATUS_ALT + r")\b"
    r"(?P<qual>(?:\s*,\s*[A-Z][A-Z0-9/-]*)*)"
    # The `by` token may be followed by ONE parenthetical before the separator: gov's own
    # `memory/backlog/TOOL.md` closes a row `CLOSED by deletion (<id>)`, and a `by` group admitting
    # one token and then demanding the middot read that row as prose (TOOL-aRepatriatedFork-9).
    r"(?:\s+by\s+(?P<by>[`*]{0,2}[A-Za-z0-9._-]+[`*]{0,2})(?:\s*\([^)]*\))?)?"
    r"\s*" + _MIDDOT + r"\s*(?P<body>.*)$"
)
# The pre-dash form nine BRAND rows still carry: `STATUS <ID or FAMILY> — text`.
_LEGACY_ROW = re.compile(
    r"^(?P<status>" + _STATUS_ALT + r")\b"
    r"(?P<qual>(?:\s*,\s*[A-Z][A-Z0-9/-]*)*)"
    r"\s+(?P<id>" + _ROW_ID + r")\s*[—-]\s+(?P<body>.*)$"
)
# A severity token heads the body and ends at the first `:` or `,`. Bounded to three words and 24
# characters so a body that merely OPENS in capitals ("NOT REAL. ...") is not mistaken for one.
_SEVERITY = re.compile(r"^(?P<sev>[A-Z][A-Z0-9]*(?:[ /-][A-Z0-9]+){0,2})\s*[:,]\s+(?P<rest>.*)$")
_OPENED = re.compile(r"^opened:\s*(?P<opened>\d{4}-\d{2}-\d{2})\s*[.,;]?\s*(?P<rest>.*)$")
_ARROW = "→"

# ---------------------------------------------------- PKG-dCandidLodestar-61: the DECLARED slot
# `-61` asked for severity to become a declared slot, and the shape it assumed — a vocabulary GROWN
# from whatever ships — is refused by the measurement rather than by preference. Over the 245 live
# rows of `memory/backlog/PKG.md` at 32bf8c15 the raw prefix above takes 46 DISTINCT values, and
# they are not 46 severities. Five different kinds of thing share that one position:
#
#   an urgency            BLOCKER 1 · HIGH 6 · MED 29 · LOW 17          53 rows
#   a kind of work        CORE ASK 11 · GATE GAP 5 · LEFT-SHIFT OWED 5 · …
#   a review-finding id   A5 · C8 · C10 · C17                            4 rows
#   an evidence state     CONFIRMED · MEASURED · RESEARCHED · UNVERIFIED 4 rows
#   a capitalised opener  `SIX, not five. …` at PKG-bLucidCadence-21     1 row
#
# A vocabulary grown from what ships would therefore DECLARE `SIX` and `C10` severities, and a
# triage sorting on it would rank a sentence opener against a blocker. That is not a stricter
# version of the raw field; it is the same field with a certificate stapled to it.
#
# So the slot is declared by SPLITTING the question, never by validating the answer. `severity`
# keeps `-59`'s contract byte for byte — raw, unvalidated, whatever the row put there, so every
# caller reading it sees what it always saw. `rank` is the DECLARED severity, populated only from
# the closed set below; any other prefix leaves it None with the raw token still readable beside it.
# Nothing is lost, no live row is reddened, and `rank` can never return `SIX`.
#
# THE SET IS CLOSED AT FOUR AND STAYS CLOSED. Those four are the only urgency-shaped tokens this
# corpus has ever run — checked over both live shards, their terminal rows, and all seven rotated
# `memory/archive/BACKLOG.*.md` snapshots. THE RULE FOR ADDING A FIFTH is a diff to this tuple plus
# an arm in the selftest: a code change a reviewer reads, never a config knob a session turns. That
# is the difference between a vocabulary and a registry, and the registry is what `corpus_ids.py`
# refused in writing.
#
# ORDER IS SEVERITY ORDER, most severe first, so `SEVERITY_VOCAB.index(row.rank)` is the triage
# sort key and no second table anywhere has to agree with this one.
SEVERITY_VOCAB = ("BLOCKER", "HIGH", "MED", "LOW")


class ParsedRow:
    """One backlog row's fields. Attribute access, so a later field is additive for every caller.

    `form` is 'dash' | 'legacy'; `keyed` is False when the id is a bare family with no slug and no
    sequence, which is a ROW without an id rather than a line that is not a row — the distinction
    hygiene check 8 cannot make and the reason eleven BRAND rows go uncounted today.
    """

    __slots__ = ("raw", "form", "id", "keyed", "status", "qualifiers", "closed_by",
                 "live", "severity", "rank", "opened", "body", "pointer")

    def __init__(self, **kw):
        for s in self.__slots__:
            setattr(self, s, kw.get(s))


def parse_row(line):
    """-> ParsedRow, or None when the line is prose rather than a row.

    Returning None for prose and a ParsedRow for an id-less row is the whole contract: a caller that
    conflates the two re-invents the bug in divergence 4 above.
    """
    line = line.rstrip("\n").rstrip("\r")
    m = _DASH_ROW.match(line)
    form = "dash"
    if not m:
        m = _LEGACY_ROW.match(line)
        form = "legacy"
    if not m:
        return None
    body = m.group("body").strip()
    pointer = None
    if _ARROW in body:
        body, _, pointer = body.rpartition(_ARROW)
        body, pointer = body.strip(), pointer.strip() or None
    severity = opened = None
    sm = _SEVERITY.match(body)
    if sm:
        severity, body = sm.group("sev"), sm.group("rest").strip()
    om = _OPENED.match(body)
    if om:
        opened, body = om.group("opened"), om.group("rest").strip()
    rid = m.group("id")
    qual = tuple(q.strip() for q in m.group("qual").split(",") if q.strip())
    by = m.groupdict().get("by")
    return ParsedRow(raw=line, form=form, id=rid, keyed=("-" in rid),
                     status=m.group("status"), qualifiers=qual,
                     closed_by=(by.strip("`*") if by else None),
                     live=(m.group("status") in LIVE_STATUSES),
                     severity=severity,
                     # The declared slot. Membership, not normalisation: a prefix the vocabulary
                     # does not hold leaves this None rather than being coerced into the nearest
                     # value, because a guess here is exactly the "labelled by guess" the unit's
                     # own §3 puts out of scope.
                     rank=(severity if severity in SEVERITY_VOCAB else None),
                     opened=opened, body=body, pointer=pointer)


def scan_backlog_shards(root, conf):
    """The shards a live-row census reads: every tracked `.md` under <memory>/backlog/."""
    m = conf["MEMORY_ROOT"]
    return sorted(p for p in run("git", "ls-files", "--", f"{m}/backlog/", cwd=root).split("\n")
                  if p.endswith(".md"))


def measure_census(root, conf):
    """-> [{shard, live, terminal, unkeyed, rows, dashes, note}], one entry per tracked shard.

    A shard tracked but absent from the worktree reports `note` and None counts rather than 0 — a
    missing file is a different fact from a drained one, and reporting it as 0 is how a deleted
    shard reads as a successful drain (`drift_report.py:1103` is the model).
    """
    out = []
    for rel in scan_backlog_shards(root, conf):
        try:
            text = read(os.path.join(root, rel))
        except OSError:
            out.append({"shard": rel, "live": None, "terminal": None, "unkeyed": None,
                        "rows": None, "dashes": None, "unranked": None,
                        "note": "tracked but not on disk"})
            continue
        live = term = unkeyed = rows = dashes = unranked = 0
        for _n, line in unfenced_lines(text):
            if line is None:
                continue
            if re.match(r"^\s*[-*]\s+", line):
                dashes += 1
            r = parse_row(line)
            if r is None:
                continue
            rows += 1
            if not r.keyed:
                unkeyed += 1
            if r.live:
                live += 1
                # Counted over LIVE rows only. A terminal row nobody will ever rank again is not
                # debt, and counting it would make the ratchet move when a row CLOSES — a pin that
                # falls for the right reason and rises for the wrong one measures neither.
                if r.rank is None:
                    unranked += 1
            else:
                term += 1
        out.append({"shard": rel, "live": live, "terminal": term, "unkeyed": unkeyed,
                    "rows": rows, "dashes": dashes, "unranked": unranked, "note": None})
    return out


def check_census_floor(rows):
    """The NON-VACUITY floor for the census, as a list of messages.

    Without it a grammar that stopped matching prints `live=0` for every shard and reads as the
    drain this unit exists to perform — a gate whose success state and whose total failure state are
    the same bytes. The floor is a RATIO, not a count: a shard that legitimately drains to zero rows
    has no dash-led lines either, so `dashes > 0 and rows == 0` selects only the broken case.
    """
    bad = []
    for r in rows:
        if r["note"]:
            bad.append(f"{r['shard']}: {r['note']} — a tracked shard nobody can read is not a "
                       f"drained one, and counting it as 0 live rows would say it is")
        elif r["dashes"] and not r["rows"]:
            bad.append(f"{r['shard']}: {r['dashes']} dash-led line(s) and NOT ONE parsed as a row — "
                       f"the row grammar has stopped matching, and every count below it is 0 for "
                       f"the wrong reason")
    return bad



# The names NicoCares' two importers already call (`check_closed_build_rows.py` and the census floor
# it reads). The definitions above lead with a declared verb, per the unit's section 8 F4; these are
# ALIASES, not definitions, so that fork's callers run against gov's bytes unchanged until they follow.
backlog_shards = scan_backlog_shards
census = measure_census
census_problems = check_census_floor

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
    # The census floor (S3). This arm asserts nothing about HOW MANY live rows there should be —
    # that pin is `PKG-dCandidLodestar-59` S5's and lives in `.memory-tree.conf` — only that the
    # grammar still resolves the population at all. Without it, `--report`'s numbers and every
    # consumer built on `parse_row` degrade to zero silently.
    shards = measure_census(root, conf)
    floor = check_census_floor(shards)
    bad.extend(f"check {CHECK}: {msg}" for msg in floor)
    # The severity ratchet (PKG-dCandidLodestar-61 S5). Shrink-only per shard, over LIVE rows whose
    # `rank` is None.
    #
    # SUPPRESSED ENTIRELY WHEN THE FLOOR FIRES, for the open-fence branch's reason one level down: a
    # shard whose rows have stopped parsing reports 0 unranked, and this arm would then print "lower
    # it to 0" — a pin instruction, in a gate's own voice, derived from a read that matched nothing.
    # Ordering the messages would not have been enough; the arm has to not run.
    pins = {} if floor else parse_unranked_pins(conf)
    for s in shards:
        if s["note"] or s["shard"] not in pins:
            continue
        pin, now = pins[s["shard"]], s["unranked"]
        if now > pin:
            bad.append(f"check {CHECK}: {s['shard']} carries {now} live row(s) with no declared "
                       f"severity against a pin of {pin} — the pin is shrink-only, so a row added "
                       f"without one of {'/'.join(SEVERITY_VOCAB)} is what moved it")
        elif now < pin:
            bad.append(f"check {CHECK}: {UNRANKED_PIN_KEY} for {s['shard']} is {pin} but only "
                       f"{now} live row(s) are unranked — lower it to {now} to lock the drain in")
    # THE LIVE-ROW FLOOR, armed for the first time. Same shrink-only polarity as the rank pin
    # above, and suppressed by the same grammar floor for the same reason: a shard whose rows
    # stopped parsing reports 0 live, and an unsuppressed arm would print "lower it to 0" in a
    # gate's own voice, derived from a read that matched nothing.
    lpins = {} if floor else parse_live_row_pins(conf)
    for s in shards:
        if s["note"] or s["shard"] not in lpins:
            continue
        pin, now = lpins[s["shard"]], s["live"]
        if now > pin:
            bad.append(f"check {CHECK}: {s['shard']} carries {now} live row(s) against a pin of "
                       f"{pin} — the shard has stopped draining, and rotation cannot help because "
                       f"rotation carries every non-terminal row forward")
        elif now < pin:
            bad.append(f"check {CHECK}: {LIVE_ROW_PIN_KEY} for {s['shard']} is {pin} but only "
                       f"{now} live row(s) remain — lower it to {now} to lock the drain in")
    if bad:
        print("\n".join(bad))
        return 1
    live = sum(s["live"] for s in shards)
    print(f"row-grammar: clean ({rows} row(s) across the row documents, {len(dupes)} pinned "
          f"duplicate(s), {live} live backlog row(s) across {len(shards)} shard(s))")
    # A skip announces itself, INSIDE the green output, because that is the only place the operator
    # who could arm it is looking. Silence here is how `LIVE_ROW_PIN` became a declared pin nothing
    # reads: nothing in a green run ever said it was not being compared to anything.
    for s in shards:
        if s["note"] is None and s["shard"] not in pins:
            print(f"row-grammar: NOT MEASURED — {s['shard']} has no {UNRANKED_PIN_KEY} entry, so "
                  f"its {s['unranked']} unranked live row(s) are counted and NOT gated; "
                  f"`--emit-pin` prints the token to declare")
        if s["note"] is None and s["shard"] not in lpins:
            print(f"row-grammar: NOT MEASURED — {s['shard']} has no {LIVE_ROW_PIN_KEY} entry, so "
                  f"its {s['live']} live row(s) are counted and NOT gated; "
                  f"`--emit-pin` prints the token to declare")
    return 0


# The lifecycle vocabulary is `tree_lib`'s, imported at the top rather than retyped: it is the single
# source check 8 already reads, and a second copy here would be the two-answers class inside the
# module that exists to stop it. Retyping it is also what let the first cut read the prose words
# `ONE`, `S`, `W` and `CORRECTS` as status tokens in a decision archive.


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
    # The per-shard census (S3 AC2). Printed on EVERY run, green or red, and printed as counts
    # beside the population they came out of: `live=208` alone is a number to trust blindly, and
    # `live=208 terminal=112 rows=320 dashes=320` is a number a reader can falsify in one glance.
    shards = measure_census(root, conf)
    print(f"backlog shards: {len(shards)}")
    for s in shards:
        if s["note"]:
            print(f"  {s['shard']}: {s['note']}")
            continue
        print(f"  {s['shard']}: live={s['live']} terminal={s['terminal']} "
              f"unkeyed={s['unkeyed']} rows={s['rows']} dash-led={s['dashes']} "
              f"unranked={s['unranked']}")
    print(f"live rows    : {sum(s['live'] for s in shards if s['live'] is not None)}")
    # The rank census (PKG-dCandidLodestar-61). Printed as the declared values BESIDE the raw
    # prefixes they were drawn from, because the whole finding of that unit is that the two are
    # different populations: a reader who sees only `unranked=192` cannot tell an unlabelled row
    # from a row whose prefix is `CORE ASK`.
    ranks = {v: 0 for v in SEVERITY_VOCAB}
    raw_only = {}
    for rel in scan_backlog_shards(root, conf):
        try:
            text = read(os.path.join(root, rel))
        except OSError:
            continue
        for _n, line in unfenced_lines(text):
            if line is None:
                continue
            r = parse_row(line)
            if r is None or not r.live:
                continue
            if r.rank:
                ranks[r.rank] += 1
            elif r.severity:
                raw_only[r.severity] = raw_only.get(r.severity, 0) + 1
    print("declared rank (live): " + " ".join(f"{v}={ranks[v]}" for v in SEVERITY_VOCAB))
    print(f"raw prefixes that are NOT a declared rank: {len(raw_only)} distinct, "
          f"{sum(raw_only.values())} row(s)")
    for k, v in sorted(raw_only.items(), key=lambda kv: (-kv[1], kv[0]))[:12]:
        print(f"  {v:4d}  {k}")
    for msg in check_census_floor(shards):
        print(f"  FLOOR: {msg}")
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
    # All three pins, so re-pinning is one paste. Emitted even when a key is already declared: an
    # operator lowering a ratchet needs the measurement, not a reminder of the value they are
    # replacing. The fork this came from printed two and its own NOT MEASURED line told the operator
    # `--emit-pin` prints the `LIVE_ROW_PIN` token — an instruction naming output that never arrived.
    shards = measure_census(root, conf)
    toks = " ".join(f"{s['shard']}:{s['unranked']}" for s in shards if s["note"] is None)
    print(f'{UNRANKED_PIN_KEY}="{toks}"')
    toks = " ".join(f"{s['shard']}:{s['live']}" for s in shards if s["note"] is None)
    print(f'{LIVE_ROW_PIN_KEY}="{toks}"')
    return 0


# ============================================== PKG-dCandidLodestar-65: ROW AGE, DERIVED NOT STORED
# `-65` was specced to add an authored `opened: YYYY-MM-DD` field to every row, backfilled from the
# archive snapshots, because `git blame` over `memory/backlog/PKG.md` reports NO row older than 60
# days against a backlog holding rows from six rotations back. Its premise — "rotation rewrites the
# file, so every carried-forward row gets a fresh timestamp" — is REFUTED by measurement, twice, and
# the field is not built:
#
#  1. ROTATION DOES NOT REWRITE CARRIED ROWS. The 2026-08-13 rotation `c31f1027` is +4/-80 on the
#     live shard: it DELETES the terminal rows and adds the archive snapshot beside them. A carried
#     row's bytes are never touched, so its blame survives — which is why blame's oldest line is
#     47.3d, older than the FIRST rotation at 2026-07-25.
#  2. THE 60-DAY CEILING IS THE REPO'S OWN AGE. The first backlog row was committed 2026-07-05, 64
#     days before this was measured. No row in this repo is 60 days old, by any instrument, so
#     `-65`'s AC3 ("reports rows older than 60 days") asks for evidence that cannot exist and an
#     authored field would not have produced it either.
#
# WHAT WAS ACTUALLY WRONG IS THE INSTRUMENT, NOT THE DATA. `git blame` answers "who last TOUCHED
# this line", so a row edited in place — a status flip, a body correction — reads as new. Blame's
# median age is 6.5d against this derivation's 15d over the same file: the gap is editing, not
# rotation. Asking git the other question instead — "in which commit did this id FIRST appear on an
# added line under the backlog paths" — is immune to both, because an edit changes a line that was
# already counted and a rotation adds a snapshot of ids already counted.
#
# MEASURED, at 32bf8c15: 247 of 247 live keyed rows dated, zero misses, in 0.27 s. Validated
# against a 3-minute independent walk that reconstructs the row set at all 1298 commits touching
# `memory/`: 484 ids, ZERO date disagreements. It also beats `-65` S2's own proposed backfill
# source — the archive snapshots cover only 101 of the 247 live rows, and on 82 of those 101 they
# report a date LATER than the truth, because a snapshot is a lower bound and this is a measurement.
#
# So the authored field is a second copy of a fact git already holds, at worse precision, which is
# the charter's single-source rule and its "memory holds only the non-derivable" rule in one. The
# field's PLACE stays fixed in the grammar above (`-59` fixed it, zero rows use it, and a row that
# genuinely predates its own file's history can still carry one); nothing populates it.
_DIFF_ROW_TAIL = r"\s*[-*]\s+[`*]*("


def _build_backlog_pathspecs(conf):
    """Glob pathspecs covering the backlog shards AND every path they have ever lived at.

    Written as globs rather than as the three literal paths this repo happens to have, because the
    live shard has already moved once (`memory/package/BACKLOG.md` -> `memory/backlog/PKG.md`,
    R097) and a literal list is a fact that goes stale the next time it moves. `--follow` is not an
    option: it takes exactly one path, and the rotated archives are a second one.
    """
    m = conf["MEMORY_ROOT"]
    return [f":(glob){m}/backlog/*.md", f":(glob){m}/**/*BACKLOG*.md"]


def derive_first_seen(root, conf):
    """-> {row-id: 'YYYY-MM-DD'}, the commit date a row id first appeared on an added backlog line.

    `-m` IS LOAD-BEARING. Without it `git log -p` shows no diff for a merge commit, and five rows
    of this corpus were introduced by a conflict resolution rather than by either parent — measured,
    they are the exact five ids the walk misses when `-m` is dropped. With it, a merge's diff is
    taken against EACH parent, so a row already present in one parent reads as added against the
    other; that is harmless here and only here, because the walk is `--reverse` and keeps the FIRST
    date it sees, so a genuine earlier introduction always wins.

    THE ID SHAPE IS THE CENSUS'S, behind the DECLARED families (TOOL-aRepatriatedFork-9). A declared
    family followed by ONE OR MORE dash segments, so a frozen legacy id such as `ABL-015` — keyed and
    live under `parse_row` — is dated like any other. With `id_pattern`'s family-slug-seq shape the
    walk never matched one, and inCMS, which declares `ABL` and its siblings as families, would have
    had every live legacy row reported undated at exit 1. The families stay the gate on purpose: a
    families list that recognises nothing still dates nothing, which is the vacuity `cmd_ages` refuses.
    """
    fams = "|".join(sorted(re.escape(f) for f in derive_families(conf)))
    rowre = re.compile(r"^\+" + _DIFF_ROW_TAIL + r"(?:" + fams + r")(?:-[A-Za-z0-9]+)+)\b")
    out = subprocess.run(
        ["git", "log", "--reverse", "--date=short", "--format=__C__ %H %ad", "-p", "-m",
         "--no-color", "--"] + _build_backlog_pathspecs(conf),
        cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if out.returncode != 0:
        raise Problem(f"row-grammar: the age walk's `git log` failed: {out.stderr.strip()}")
    first, date = {}, None
    for line in out.stdout.split("\n"):
        if line.startswith("__C__ "):
            parts = line.split()
            date = parts[2] if len(parts) > 2 else None
            continue
        mm = rowre.match(line)
        if mm and mm.group(1) not in first:
            first[mm.group(1)] = date
    return first


def cmd_ages(root, conf):
    """Row age over the live set, DERIVED. Refuses rather than printing an empty distribution."""
    import datetime
    first = derive_first_seen(root, conf)
    live = []
    for rel in scan_backlog_shards(root, conf):
        try:
            text = read(os.path.join(root, rel))
        except OSError:
            continue
        for n, line in unfenced_lines(text):
            if line is None:
                continue
            r = parse_row(line)
            if r is not None and r.live and r.keyed:
                live.append((rel, n, r))
    # The non-vacuity floor, and it is the same shape as the census floor above: an empty
    # derivation and a corpus with no rows print the same distribution, so the case where the walk
    # silently stopped matching has to be separated from the case where there is nothing to date.
    if live and not first:
        raise Problem("row-grammar: the age walk dated ZERO ids while the shards hold "
                      f"{len(live)} live keyed row(s) — the diff-line grammar has stopped "
                      f"matching, and every age below it would be 'undated' for the wrong reason")
    today = datetime.date.today()
    dated, undated = [], []
    for rel, n, r in live:
        d = first.get(r.id)
        if d is None:
            undated.append((rel, n, r.id))
            continue
        y, mo, dy = (int(x) for x in d.split("-"))
        dated.append(((today - datetime.date(y, mo, dy)).days, r.id, d))
    dated.sort()
    print(f"live keyed rows : {len(live)}")
    print(f"dated from git  : {len(dated)}")
    print(f"undated         : {len(undated)}")
    for rel, n, rid in undated:
        print(f"  {rel}:{n} {rid}")
    if dated:
        bands = [(0, 7), (7, 14), (14, 30), (30, 60), (60, 10 ** 6)]
        print(f"oldest          : {dated[-1][0]}d  {dated[-1][1]} opened {dated[-1][2]}")
        print(f"median          : {dated[len(dated) // 2][0]}d")
        for lo, hi in bands:
            label = f"{lo}-{hi}d" if hi < 10 ** 6 else f"{lo}d+"
            print(f"  {label:>8}: {sum(1 for a, _i, _d in dated if lo <= a < hi)}")
    # An undated live row is the one failure this mode can have that is not vacuity: git holds no
    # record of the id ever being added, which means the row arrived by a path the walk cannot see.
    return 1 if undated else 0


ENGINE_OWNERS = ("corpus_ids", "gen_build_index")


def scan_engine_imports(kit_dir):
    """-> (hits, graded): every import of `corpus_ids` or `gen_build_index` by ANOTHER module here.

    TOOL-aRepatriatedFork-9. The shared helpers live in `tree_lib.py` so that an adopter's own copy
    of either engine cannot kill its siblings on import; a later edit re-adding `from corpus_ids
    import ...` to a sibling would reopen that silently, because in THIS tree the import resolves.
    The two owners' use of each other is exempt, as the spec states. Parsed with `ast`, so a
    comment or a docstring naming the module is not an import.

    NOT CHECKED: a load by path (`importlib.util.spec_from_file_location`), which `gotchas.py` uses
    to ASK `corpus_ids` a question at run time and which degrades to a named failure rather than an
    import error. `graded` is the number of modules parsed, so an empty directory cannot pass.
    """
    import ast
    hits, graded = [], 0
    for name in sorted(os.listdir(kit_dir)):
        if not name.endswith(".py"):
            continue
        stem = name[:-3]
        with open(os.path.join(kit_dir, name), encoding="utf-8") as fh:
            tree = ast.parse(fh.read(), name)
        graded += 1
        if stem in ENGINE_OWNERS:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.level == 0:
                mods = [node.module or ""]
            elif isinstance(node, ast.Import):
                mods = [a.name for a in node.names]
            else:
                continue
            hits.extend((name, node.lineno, m) for m in mods if m.split(".")[0] in ENGINE_OWNERS)
    return hits, graded


# ----------------------------------------------------------------------------------------- selftest
def _tree(tmp, decisions, *, families="arch:ARCH", pin="0", archives=None, shards=None):
    """`shards` is {basename: text} written under <memory>/backlog/ and TRACKED, so the census arms
    below exercise `scan_backlog_shards`'s `git ls-files` walk rather than a directory listing."""
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
                                       capture_output=True, text=True, encoding="utf-8", timeout=60)
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
                               cwd=t9, capture_output=True, text=True, encoding="utf-8")
            return f"rc={r.returncode} {r.stdout}{r.stderr}"
        arm("--check grades the tree it is RUN IN, not the tree the kit lives in",
            "two answers to one question", _foreign)

        # ------------------------------------------------- the exported grammar (S3) and its floor
        # Every arm below states the FIELD it is about, because the three fields `-61` and `-65`
        # build on are exactly the ones no existing predicate returns.
        def read_field(line, attr):
            r = parse_row(line)
            return "None" if r is None else repr(getattr(r, attr))

        arm("a plain dash row returns its id", "'ARCH-tOne-1'",
            lambda: read_field("- ARCH-tOne-1 · OPEN · a body", "id"))
        arm("a plain dash row returns its status", "'OPEN'",
            lambda: read_field("- ARCH-tOne-1 · OPEN · a body", "status"))
        arm("a plain dash row returns its pointer", "'scripts/x.py'",
            lambda: read_field("- ARCH-tOne-1 · OPEN · a body → scripts/x.py", "pointer"))
        arm("the pointer is stripped OFF the body rather than left in it", "'a body'",
            lambda: read_field("- ARCH-tOne-1 · OPEN · a body → scripts/x.py", "body"))
        # The single bolded id at memory/backlog/PKG.md is why the naive predicate under-counts by 1.
        arm("a BOLDED id parses, which is the row the naive predicate misses", "'ARCH-tOne-1'",
            lambda: read_field("- **ARCH-tOne-1** · OPEN · a body", "id"))
        arm("a BACKTICKED id parses too", "'ARCH-tOne-1'",
            lambda: read_field("- `ARCH-tOne-1` · OPEN · a body", "id"))
        # Divergence 2: seven live rows carry this and BOTH `· <STATUS> · ` predicates drop them.
        arm("a comma-qualified status keys on its FIRST token", "'OPEN'",
            lambda: read_field("- ARCH-tOne-1 · OPEN, BACKEND · a body", "status"))
        arm("a comma-qualified row is still LIVE", "True",
            lambda: read_field("- ARCH-tOne-1 · OPEN, BACKEND · a body", "live"))
        arm("the qualifier is returned rather than discarded", "('BACKEND',)",
            lambda: read_field("- ARCH-tOne-1 · OPEN, BACKEND · a body", "qualifiers"))
        # Divergence 3: drift_report reads this row LIVE and check_core_ask_closures cannot see it.
        arm("`CLOSED by <id>` is TERMINAL, not live", "False",
            lambda: read_field("- ARCH-tOne-1 · CLOSED by ARCH-tTwo-9 · a body", "live"))
        arm("`CLOSED by <id>` returns the superseding id", "'ARCH-tTwo-9'",
            lambda: read_field("- ARCH-tOne-1 · CLOSED by ARCH-tTwo-9 · a body", "closed_by"))
        arm("a backticked `CLOSED by` pointer is unwrapped", "'-7'",
            lambda: read_field("- ARCH-tOne-1 · CLOSED by `-7` · a body", "closed_by"))
        # Divergence 1, stated as an arm so a later reconcile cannot flip it by accident.
        arm("DEFERRED is TERMINAL here, unlike drift_report's two-token set", "False",
            lambda: read_field("- ARCH-tOne-1 · DEFERRED · a body", "live"))
        # Divergence 4: the eleven BRAND rows hygiene check 8 cannot see.
        arm("a pre-dash legacy row parses instead of being dropped", "'legacy'",
            lambda: read_field("CLOSED ARCH-tOne-1 — a body", "form"))
        arm("a row whose id is a BARE FAMILY is classified, not dropped", "'ARCH'",
            lambda: read_field("OPEN ARCH — a body", "id"))
        arm("a bare-family row is marked unkeyed rather than keyed", "False",
            lambda: read_field("OPEN ARCH — a body", "keyed"))
        arm("a bare-family row still carries its status, so it COUNTS", "True",
            lambda: read_field("- ARCH · OPEN · a body", "live"))
        # The two fields -61 and -65 build on. `opened` is empty on every real row today; its SLOT
        # is what this unit fixes, so the arm is what stops -65 from having to move severity.
        arm("severity is lifted off the head of the body", "'MED'",
            lambda: read_field("- ARCH-tOne-1 · OPEN · MED: a body", "severity"))
        arm("a multi-word severity is lifted whole", "'CORE ASK'",
            lambda: read_field("- ARCH-tOne-1 · OPEN · CORE ASK: a body", "severity"))
        arm("a body with no severity returns None rather than eating its first clause", "None",
            lambda: read_field("- ARCH-tOne-1 · OPEN · the walk stopped matching, so nothing fired",
                      "severity"))
        arm("`opened:` is lifted from its slot after severity", "'2026-09-05'",
            lambda: read_field("- ARCH-tOne-1 · OPEN · MED: opened: 2026-09-05 a body", "opened"))
        arm("prose is None, which is NOT the same answer as an id-less row", "None",
            lambda: read_field("> Mutable — each row leads with one status token.", "id"))
        arm("a dash-led line with no id and no status is prose", "None",
            lambda: read_field("- just a bullet", "id"))

        # THE CENSUS AND ITS FLOOR. AC4's failing case is observed here rather than only in the
        # tree: a fixture whose rows stop parsing must RED, because `live=0` is byte-identical to a
        # successful drain and a check whose pass and total-failure states print the same thing is
        # not a check.
        _live = "\n".join(["# backlog", "- ARCH-tOne-1 · OPEN · one",
                           "- ARCH-tOne-2 · CLOSED · two", "- ARCH-tOne-3 · OPEN, BACKEND · three",
                           "- ARCH-tOne-4 · DEFERRED · four", ""])
        t10 = os.path.join(base, "census"); os.makedirs(t10)
        c10 = _tree(t10, "- ARCH-tOne-1 · one\n", shards={"ARCH.md": _live})
        arm("the census counts a qualified row live and a DEFERRED row terminal",
            "live=2 terminal=2", lambda: cap(t10, c10, cmd_report))
        arm("--check prints the live population beside the row population",
            "2 live backlog row(s) across 1 shard(s)", lambda: cap(t10, c10))
        # OBSERVED RED [1]: dash-led lines that no longer parse.
        _broken = "\n".join(["# backlog", "- ARCH-tOne-1 : OPEN : one", "- ARCH-tOne-2 : OPEN : two",
                             ""])
        t11 = os.path.join(base, "brokengrammar"); os.makedirs(t11)
        c11 = _tree(t11, "- ARCH-tOne-1 · one\n", shards={"ARCH.md": _broken})
        arm("a shard whose rows ALL stop parsing REDS instead of reporting a drain to zero",
            "the row grammar has stopped matching", lambda: cap(t11, c11))
        arm("the floor names the shard and how many lines it could not read",
            "2 dash-led line(s) and NOT ONE parsed", lambda: cap(t11, c11))
        # An EMPTY shard is young, not broken: no dash-led lines, so the floor must stay silent.
        t12 = os.path.join(base, "emptyshard"); os.makedirs(t12)
        c12 = _tree(t12, "- ARCH-tOne-1 · one\n", shards={"ARCH.md": "# backlog\n\n> Mutable.\n"})
        arm("an EMPTY shard reads as 0 live rows and passes", "row-grammar: clean",
            lambda: cap(t12, c12))
        # OBSERVED RED [2]: tracked but absent. Distinguished from a drain on purpose.
        t13 = os.path.join(base, "missingshard"); os.makedirs(t13)
        c13 = _tree(t13, "- ARCH-tOne-1 · one\n", shards={"ARCH.md": _live})
        os.remove(os.path.join(t13, "memory", "backlog", "ARCH.md"))
        arm("the census reports a tracked-but-absent shard rather than counting it 0 live",
            "tracked but not on disk",
            lambda: "; ".join(check_census_floor(measure_census(t13, c13))))
        arm("--check on a tracked-but-absent row document fails NAMED, never in a traceback",
            "is tracked but is not on disk", lambda: cap(t13, c13))

        # ------------------------------------------- PKG-dCandidLodestar-61: the declared rank slot
        # Every arm states which of the TWO fields it is about. The unit's whole finding is that
        # `severity` and `rank` are different populations, so an arm that does not say which one it
        # asserts over is an arm that cannot detect them being merged back together.
        arm("a declared severity populates rank", "'MED'",
            lambda: read_field("- ARCH-tOne-1 · OPEN · MED: a body", "rank"))
        arm("rank is populated for every member of the declared vocabulary", "[]",
            lambda: repr([v for v in SEVERITY_VOCAB
                          if parse_row(f"- ARCH-tOne-1 · OPEN · {v}: a body").rank != v]))
        # THE FINDING, as an arm. `SIX, not five.` is a live row at memory/backlog/PKG.md, and a
        # vocabulary grown from what ships would have declared it a severity.
        arm("a capitalised sentence opener is raw severity but NOT a rank", "None",
            lambda: read_field("- ARCH-tOne-1 · OPEN · SIX, not five. The asides are orphaned", "rank"))
        arm("that same row still returns its raw prefix, so nothing is lost", "'SIX'",
            lambda: read_field("- ARCH-tOne-1 · OPEN · SIX, not five. The asides are orphaned", "severity"))
        arm("a kind-of-work prefix is raw severity but NOT a rank", "None",
            lambda: read_field("- ARCH-tOne-1 · OPEN · CORE ASK: a body", "rank"))
        arm("a review-finding id is raw severity but NOT a rank", "None",
            lambda: read_field("- ARCH-tOne-1 · OPEN · C10: manifest check 11 caps traps bullets", "rank"))
        # The comma-tailed shape S3 normalised out of the tree, kept as an arm so the parse is
        # asserted rather than remembered: the file no longer carries an instance to fail on.
        arm("a comma-tailed severity still ranks, which is why S3's rewrite was byte-neutral",
            "'LOW'", lambda: read_field("- ARCH-tOne-1 · OPEN · LOW, core: a hydration warning", "rank"))
        arm("the vocabulary is ordered most-severe-first, so index() is the triage sort key",
            "[0, 1, 2, 3]",
            lambda: repr([SEVERITY_VOCAB.index(v) for v in ("BLOCKER", "HIGH", "MED", "LOW")]))
        # ---- the ratchet. Both directions, plus the two ways it could fail to be a check at all.
        _sev = "\n".join(["# backlog", "- ARCH-tOne-1 · OPEN · HIGH: ranked",
                          "- ARCH-tOne-2 · OPEN · CORE ASK: not a rank",
                          "- ARCH-tOne-3 · OPEN · plain prose, no prefix at all",
                          "- ARCH-tOne-4 · CLOSED · terminal and unranked, must NOT count", ""])
        t14 = os.path.join(base, "sevpin"); os.makedirs(t14)
        c14 = _tree(t14, "- ARCH-tOne-1 · one\n", shards={"ARCH.md": _sev})
        c14[UNRANKED_PIN_KEY] = "memory/backlog/ARCH.md:2"
        arm("a shard at its unranked pin passes, and TERMINAL unranked rows do not count",
            "row-grammar: clean", lambda: cap(t14, c14))
        # OBSERVED RED [61-1]: a new unranked row lands and the ceiling bites.
        c14b = dict(c14); c14b[UNRANKED_PIN_KEY] = "memory/backlog/ARCH.md:1"
        arm("an unranked live row above the pin REDS and names the vocabulary it wanted",
            "against a pin of 1", lambda: cap(t14, c14b))
        arm("the red names BLOCKER/HIGH/MED/LOW rather than a bare count", "BLOCKER/HIGH/MED/LOW",
            lambda: cap(t14, c14b))
        # OBSERVED RED [61-2]: shrink-only bites in the other direction, so a drain must be locked in.
        c14c = dict(c14); c14c[UNRANKED_PIN_KEY] = "memory/backlog/ARCH.md:3"
        arm("a stale-high unranked pin REDS, so a drain has to lower it",
            "lower it to 2 to lock the drain in", lambda: cap(t14, c14c))
        # An UNDECLARED pin must ANNOUNCE. This is the arm that stops this key becoming LIVE_ROW_PIN,
        # which is declared in .memory-tree.conf and read by nothing.
        c14d = dict(c14); c14d.pop(UNRANKED_PIN_KEY, None)
        arm("an undeclared unranked pin announces the skip inside the GREEN output",
            "NOT MEASURED", lambda: cap(t14, c14d))
        arm("the announcement names the shard and its unmeasured count",
            "memory/backlog/ARCH.md has no SEVERITY_UNLABELLED_PIN", lambda: cap(t14, c14d))
        arm("a malformed pin token fails NAMED rather than silently pinning nothing",
            "takes `<shard-path>:<count>` tokens", lambda: cap(t14, dict(c14, **{UNRANKED_PIN_KEY: "ARCH.md"})))
        # The ordering hazard: a shard whose grammar broke reports 0 unranked, and an unsuppressed
        # ratchet would answer with "lower it to 0" — a pin instruction from a read that matched
        # nothing. The floor must fire and the ratchet must NOT speak.
        c11b = dict(c11); c11b[UNRANKED_PIN_KEY] = "memory/backlog/ARCH.md:5"
        arm("a broken-grammar shard reds on the FLOOR, not on a bogus pin instruction",
            "FLOOR-ONLY",
            lambda: "LEAKED" if "lower it to 0" in cap(t11, c11b) else
                    ("FLOOR-ONLY" if "stopped matching" in cap(t11, c11b) else "NEITHER"))
        arm("--emit-pin emits the unranked pin beside the duplicate pin",
            'SEVERITY_UNLABELLED_PIN="memory/backlog/ARCH.md:2"',
            lambda: cap(t14, c14, cmd_emit_pin))
        arm("--report prints the declared rank census, not just a raw prefix list",
            "declared rank (live): BLOCKER=0 HIGH=1 MED=0 LOW=0",
            lambda: cap(t14, c14, cmd_report))
        arm("--report separates raw prefixes that are NOT a declared rank", "CORE ASK",
            lambda: cap(t14, c14, cmd_report))

        # -------------------------------------------- PKG-dCandidLodestar-65: row age, DERIVED
        # These arms encode the two REFUTATIONS, not the specced field. An arm that only asserted
        # "the walk returns a date" would pass under `git blame` too, which is the instrument that
        # produced the wrong answer in the first place.
        def _write_commit(tmp, date, files, msg="c"):
            env = dict(os.environ, GIT_AUTHOR_DATE=f"{date}T12:00:00", GIT_AUTHOR_NAME="t",
                       GIT_AUTHOR_EMAIL="t@t.test", GIT_COMMITTER_DATE=f"{date}T12:00:00",
                       GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t.test")
            for rel, text in files.items():
                p = os.path.join(tmp, rel)
                os.makedirs(os.path.dirname(p), exist_ok=True)
                if text is None:
                    os.remove(p)
                    continue
                with open(p, "w", encoding="utf-8") as fh:
                    fh.write(text)
            subprocess.run(["git", "add", "-A"], cwd=tmp, capture_output=True, text=True, encoding="utf-8")
            subprocess.run(["git", "commit", "-q", "-m", msg, "--no-verify"], cwd=tmp,
                           capture_output=True, text=True, encoding="utf-8", env=env)

        t15 = os.path.join(base, "ages"); os.makedirs(t15)
        c15 = _tree(t15, "- ARCH-tOne-1 · one\n", shards={"ARCH.md": "# backlog\n"})
        _write_commit(t15, "2026-01-01", {"memory/backlog/ARCH.md":
                                "# backlog\n- ARCH-tOld-1 · OPEN · minted first\n"})
        _write_commit(t15, "2026-02-01", {"memory/backlog/ARCH.md":
                                "# backlog\n- ARCH-tOld-1 · OPEN · minted first\n"
                                "- ARCH-tNew-1 · OPEN · minted second\n"})
        # THE BLAME REFUTATION. Edit the old row in place on a much later commit: `git blame` would
        # report that later date, and this walk must still report the mint.
        _write_commit(t15, "2026-03-01", {"memory/backlog/ARCH.md":
                                "# backlog\n- ARCH-tOld-1 · OPEN · minted first, EDITED in place\n"
                                "- ARCH-tNew-1 · OPEN · minted second\n"})
        # THE ROTATION REFUTATION. Rotate exactly as this repo does it — snapshot the whole file into
        # memory/archive/BACKLOG.<date>.md and drop the terminal rows from the live shard.
        _write_commit(t15, "2026-04-01", {
            "memory/archive/BACKLOG.2026-04-01.md":
                "# rotated\n- ARCH-tOld-1 · OPEN · minted first, EDITED in place\n"
                "- ARCH-tNew-1 · OPEN · minted second\n",
            "memory/backlog/ARCH.md":
                "# backlog\n- ARCH-tOld-1 · OPEN · minted first, EDITED in place\n"
                "- ARCH-tNew-1 · OPEN · minted second\n"})
        arm("an EDITED row keeps its mint date, which is the answer git blame gets wrong",
            "'2026-01-01'", lambda: repr(derive_first_seen(t15, c15).get("ARCH-tOld-1")))
        arm("a row CARRIED through a rotation keeps its mint date, refuting the specced premise",
            "'2026-02-01'", lambda: repr(derive_first_seen(t15, c15).get("ARCH-tNew-1")))
        arm("--ages dates every live keyed row and exits 0", "rc=0 ",
            lambda: cap(t15, c15, cmd_ages))
        arm("--ages reports the oldest row by its MINT date, not the rotation's",
            "opened 2026-01-01", lambda: cap(t15, c15, cmd_ages))
        # THE `-m` ARM. Five real rows in this corpus were introduced by a conflict resolution and
        # by neither parent; without `-m` the walk misses exactly those five.
        t16 = os.path.join(base, "agesmerge"); os.makedirs(t16)
        c16 = _tree(t16, "- ARCH-tOne-1 · one\n", shards={"ARCH.md": "# backlog\n"})
        _write_commit(t16, "2026-01-01", {"memory/backlog/ARCH.md": "# backlog\n- ARCH-tBase-1 · OPEN · base\n"})
        subprocess.run(["git", "checkout", "-q", "-b", "side"], cwd=t16, capture_output=True, text=True, encoding="utf-8")
        _write_commit(t16, "2026-01-02", {"memory/backlog/ARCH.md":
                                "# backlog\n- ARCH-tBase-1 · OPEN · base\n- ARCH-tSide-1 · OPEN · side\n"})
        subprocess.run(["git", "checkout", "-q", "-"], cwd=t16, capture_output=True, text=True, encoding="utf-8")
        _write_commit(t16, "2026-01-03", {"memory/backlog/ARCH.md":
                                "# backlog\n- ARCH-tBase-1 · OPEN · base\n- ARCH-tMain-1 · OPEN · main\n"})
        subprocess.run(["git", "merge", "-q", "--no-commit", "side"], cwd=t16,
                       capture_output=True, text=True, encoding="utf-8")
        _write_commit(t16, "2026-01-04", {"memory/backlog/ARCH.md":
                                "# backlog\n- ARCH-tBase-1 · OPEN · base\n- ARCH-tMain-1 · OPEN · main\n"
                                "- ARCH-tSide-1 · OPEN · side\n- ARCH-tMerge-1 · OPEN · born in the merge\n"},
            msg="merge")
        arm("a row introduced ONLY by a conflict resolution is dated, which needs `-m`",
            "'2026-01-04'", lambda: repr(derive_first_seen(t16, c16).get("ARCH-tMerge-1")))
        arm("the merge walk still dates the pre-merge rows at their own commits", "'2026-01-01'",
            lambda: repr(derive_first_seen(t16, c16).get("ARCH-tBase-1")))
        # OBSERVED RED [65-1]: the vacuity floor. A families list that recognises nothing makes the
        # diff-line grammar match nothing, and an ungated --ages would print "undated: N" as though
        # the rows were merely young.
        c15v = dict(c15); c15v["FAMILIES"] = "other:OTHER"
        arm("--ages REFUSES when the walk dates zero ids against a populated shard",
            "has stopped matching", lambda: cap(t15, c15v, cmd_ages))
        # OBSERVED RED [65-2]: a live row git has no record of is NAMED and exits 1.
        t17 = os.path.join(base, "agesundated"); os.makedirs(t17)
        c17 = _tree(t17, "- ARCH-tOne-1 · one\n", shards={"ARCH.md": "# backlog\n"})
        _write_commit(t17, "2026-01-01", {"memory/backlog/ARCH.md": "# backlog\n- ARCH-tOld-1 · OPEN · committed\n"})
        with open(os.path.join(t17, "memory", "backlog", "ARCH.md"), "a", encoding="utf-8") as fh:
            fh.write("- ARCH-tGhost-1 · OPEN · never committed, so git cannot date it\n")
        arm("--ages names an undated live row and exits non-zero", "rc=1 ",
            lambda: cap(t17, c17, cmd_ages))
        arm("the undated row is reported with its shard, line and id", "ARCH-tGhost-1",
            lambda: cap(t17, c17, cmd_ages))

        # --------------------------------------------- TOOL-aRepatriatedFork-9: the two corrections
        # AC2. A FROZEN legacy id — family, one dash, a number — sits between the bare family and the
        # family-slug-seq shape. The fork's pattern had nothing there and read the row as prose.
        arm("a frozen legacy id parses as a row", "'ABL-015'",
            lambda: read_field("- ABL-015 · OPEN · body", "id"))
        arm("a legacy id with a node-tagged sequence parses too", "'DPL-a012'",
            lambda: read_field("- DPL-a012 · CLOSED · body", "id"))
        arm("a frozen legacy id is KEYED, not a bare family", "True",
            lambda: read_field("- ABL-015 · OPEN · body", "keyed"))
        t18 = os.path.join(base, "legacyid"); os.makedirs(t18)
        c18 = _tree(t18, "- ARCH-tOne-1 · one\n",
                    shards={"ABL.md": "# backlog\n- ABL-015 · OPEN · body\n"})
        arm("the census counts a legacy-id row live and keyed",
            "memory/backlog/ABL.md: live=1 terminal=0 unkeyed=0 rows=1", lambda: cap(t18, c18, cmd_report))
        # AC3. A `CLOSED by` clause carrying a parenthetical before its separator, the shape gov's
        # own TOOL shard uses. The fork's `by` group took one token and demanded the middot.
        arm("`CLOSED by <token> (<id>)` is CLOSED", "'CLOSED'",
            lambda: read_field("- ARCH-tOne-1 · CLOSED by deletion (ARCH-tTwo-1) · a body", "status"))
        arm("...and TERMINAL", "False",
            lambda: read_field("- ARCH-tOne-1 · CLOSED by deletion (ARCH-tTwo-1) · a body", "live"))
        arm("...and its `by` token is returned without the parenthetical", "'deletion'",
            lambda: read_field("- ARCH-tOne-1 · CLOSED by deletion (ARCH-tTwo-1) · a body", "closed_by"))
        # AC4. The live-row pin: undeclared announces inside the GREEN output, and --emit-pin prints
        # its token beside the other two, measured.
        arm("an undeclared live-row pin announces the skip inside the GREEN output",
            "memory/backlog/ARCH.md has no LIVE_ROW_PIN entry", lambda: cap(t14, c14d))
        arm("--emit-pin prints the live-row pin as the third declaration",
            'LIVE_ROW_PIN="memory/backlog/ARCH.md:3"', lambda: cap(t14, c14, cmd_emit_pin))
        c14e = dict(c14); c14e[LIVE_ROW_PIN_KEY] = "memory/backlog/ARCH.md:2"
        arm("a live row above the live-row pin REDS", "3 live row(s) against a pin of 2",
            lambda: cap(t14, c14e))
        # The age walk dates what the census keys. A frozen legacy id under a DECLARED family is live
        # and keyed, so a walk still spelled in family-slug-seq would report it undated at exit 1.
        t19 = os.path.join(base, "ageslegacy"); os.makedirs(t19)
        c19 = _tree(t19, "- ARCH-tOne-1 · one\n", shards={"ARCH.md": "# backlog\n"})
        _write_commit(t19, "2026-01-05", {"memory/backlog/ARCH.md": "# backlog\n- ARCH-015 · OPEN · a frozen legacy id\n"})
        arm("the age walk dates a frozen legacy id under a declared family", "'2026-01-05'",
            lambda: repr(derive_first_seen(t19, c19).get("ARCH-015")))
        arm("...so --ages over it exits 0 with nothing undated", "undated         : 0",
            lambda: cap(t19, c19, cmd_ages))
        arm("the names NicoCares' importers call are the verb-led definitions, not copies", "True",
            lambda: repr(census is measure_census and census_problems is check_census_floor
                         and backlog_shards is scan_backlog_shards))
        # The split is DERIVED from tree_lib's tuples, so it is asserted against the spec's LITERAL
        # contract rather than against the tuples it came from, which could not disagree.
        arm("the census's live and terminal sets are the contract's four and three", "True",
            lambda: repr(LIVE_STATUSES == ("OPEN", "SPECCED", "INPROGRESS", "BLOCKED")
                         and TERMINAL_STATUSES == ("CLOSED", "WONTDO", "DEFERRED")))

        # AC8. The import graph. GREEN over this kit's own directory, and observed RED on a staged
        # re-import, so the arm is not passing because it matched nothing.
        kit = os.path.dirname(os.path.abspath(__file__))
        arm("no sibling engine in this kit imports corpus_ids or gen_build_index", "hits=[]",
            lambda: "hits={0} graded={1}".format(*scan_engine_imports(kit)))
        arm("...and the scan graded this module itself, so the green is not an empty walk",
            "graded-self=True",
            lambda: f"graded-self={scan_engine_imports(kit)[1] >= 2 and os.path.isfile(__file__)}")
        staged = os.path.join(base, "stagedimport"); os.makedirs(staged)
        with open(os.path.join(staged, "row_grammar.py"), "w", encoding="utf-8") as fh:
            fh.write("# a docstring naming corpus_ids is not an import\nimport os\n")
        with open(os.path.join(staged, "check-arms.py"), "w", encoding="utf-8") as fh:
            fh.write("from corpus_ids import parse_conf\n")
        with open(os.path.join(staged, "gen_build_index.py"), "w", encoding="utf-8") as fh:
            fh.write("from corpus_ids import parse_conf\n")
        arm("a staged sibling re-import is named with its file, line and module",
            "('check-arms.py', 1, 'corpus_ids')",
            lambda: repr(scan_engine_imports(staged)[0]))
        arm("...and the two owners' own mutual use is exempt", "owner-exempt",
            lambda: "owner-exempt" if not [h for h in scan_engine_imports(staged)[0]
                                           if h[0] == "gen_build_index.py"] else "FLAGGED")

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
    if mode == "--ages":
        return cmd_ages(root, conf)
    if mode == "--check-rotation":
        return cmd_check_rotation(root, conf)
    print(f"row-grammar: unknown argument '{mode}'; the modes are --check, --check-rotation, "
          f"--report, --emit-pin, --ages and --selftest")
    return 2


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except Problem as exc:
        print(str(exc))
        sys.exit(1)
