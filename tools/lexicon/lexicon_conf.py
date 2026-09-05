"""lexicon_conf.py — the ONE reader of `.lexicon.conf`.

FOUR consumers need this file: the engine (`tools/lexicon/lexicon.py`), the adopter script
(`tools/lexicon/adopt-lexicon.sh`, in bash), this repo's `map_extractors.py`, and `drift-audit`'s
signals. Two hand-written parsers for one file is the two-answers-to-one-question class, so the bash
side calls `--print-verbs` here rather than reimplementing the grammar, and every Python consumer
imports `load_conf`. The count above read "three" and hedged the third with "when its unit unparks"
long after it unparked, while the map dossier said four and listed them correctly — two carriers of
one count, disagreeing, in a file whose whole subject is not having two of something.

THE GRAMMAR, and why it is not exactly the sibling one. `.memory-tree.conf` and
`.codebase-map.conf` are a RESTRICTED line-based `KEY=VALUE` that bash can `source` and Python can
parse line-wise. That grammar cannot carry `VERBS`: a closed verb table is one row per verb with a
prose meaning, and the negative definitions ("`build` not `create`") are the rows that make the
table worth having. So this grammar is the sibling one PLUS block keys:

    KEY="value"            # single-line, sibling grammar: no inline comment after a value
    KEY:                   # block key: rows are the indented lines that follow
      row one
      row two
    NEXT_KEY="..."         # a non-indented line ends the block

A block ends at the first non-indented, non-blank line, or at EOF. Blank lines inside a block are
skipped, not terminators — a table with a blank line between groups is the shape a human writes.
"""

import re
import sys
from pathlib import Path

#: Keys whose value is an indented block rather than a single line. `LAYERS` left with the
#: predicate that read it (TOOL-aSurfacedLexicon-2); `CELLS` and `PINS` arrived with the
#: (language, surface) matrix (TOOL-aSurfacedLexicon-4); `CANON` is the owner's overlay over the
#: frozen shipped clusters (TOOL-aSurfacedLexicon-11). Widening this tuple does NOT make every
#: identifier-shaped header legal: an unlisted header still falls through to the refusal in
#: `load_conf`, which is the regression AC4 stands on.
BLOCK_KEYS = ("VERBS", "CELLS", "PINS", "PATTERNS", "CANON")

#: The closed sets the `CELLS` and `PINS` rows are graded against. A row naming a token outside
#: one of these is a refusal naming the file and the line, never a skip.
SURFACES = ("function", "type", "file", "constant")
CONVENTIONS = ("snake", "screaming", "camel", "pascal", "kebab", "dark")
PIN_PREDICATES = ("debt", "unruled", "suffix", "conv")

#: The extractor parts a `PATTERNS` row may name — the three lists `extract` returns, in its order.
#: A closed set here for the same reason `SURFACES` is one: a typo'd part would arm nothing and
#: report nothing, which is the shape a declaration must never be able to take by accident.
PATTERN_PARTS = ("functions", "types", "imports")

#: A pattern-set id, as `LANGS` spells it. Hyphens are the shipped house style (`js-regex`), which is
#: why the generic row-key parse and not the alphabetic `VERBS` one is what this block runs through.
_PSET_RE = re.compile(r"^[A-Za-z0-9_-]+$")

#: The selector kinds a `CELLS` row key may name (TOOL-aSurfacedLexicon-13). `prefix` is a literal
#: leading-substring test over the NAME; `decorator` names one decorator and is a `parser`-mode
#: capability, refused on any other mode by `check_declaration`. A CLOSED set, for the reason
#: `SURFACES` is one: a typo'd kind would route nothing and report nothing, which is the shape a
#: declaration must never be able to take by accident. There is deliberately no regex kind — a
#: predicate language over names is a second grading language inside a naming gate.
SELECTOR_KINDS = ("prefix", "decorator")

#: A selector literal carries NO DOT, and that is load-bearing rather than fussy: a `PINS` row key is
#: `<cell>.<predicate>` split on the dot, so a dotted literal would make the pin row of the very cell
#: the selector creates unparseable — and S4's whole point is that a selector'd cell ratchets on a
#: pin of its own. A dotted decorator (`@app.route`) is recorded and matched by its LAST segment,
#: which is why the restriction costs an adopter nothing.
_SEL_LIT_RE = re.compile(r"^[A-Za-z0-9_]+$")

#: Per-cell flags. `vocab` grades the row's names against the verb table; `notail` bans a trailing
#: type suffix. Both are declared here rather than accepted freely so a typo reds instead of
#: silently arming nothing.
_CELL_FLAGS = ("vocab", "notail")

_SCALAR_RE = re.compile(r'^([A-Za-z_][A-Za-z0-9_]*)=(.*)$')
_BLOCK_RE = re.compile(r'^([A-Za-z_][A-Za-z0-9_]*):[ \t]*$')


class ConfError(Exception):
    """A refusal naming the file and line. Never a silent default: an unreadable declaration must
    not degrade into an empty one, because every predicate here reads green over an empty set."""


def load_conf(path: str | Path) -> dict:
    """Parse `.lexicon.conf` into `{scalars..., "VERBS": …, "CELLS": …, "PINS": …}`.

    Raises ConfError on an unreadable file or a malformed line. It does NOT validate that any
    particular key is present — arming is the engine's question, and a reader that refuses an
    absent key cannot be used by the scaffolder that is about to write it. An ABSENT block resolves
    to its empty container, which is what keeps a declaration written before `CELLS` and `PINS`
    existed parsing exactly as it did.
    """
    p = Path(path)
    try:
        raw = p.read_text(encoding="utf-8")
    except OSError as e:
        raise ConfError(f"{p}: cannot read: {e}") from e

    out: dict = {k: {} for k in BLOCK_KEYS}
    # `{block: {rowkey: lineno}}`, kept beside the parsed blocks because the CROSS-BLOCK refusals at
    # the tail run after every value shape has already dropped its line number. Derived by re-running
    # `_parse_rows` rather than by re-splitting the row here: the split IS the grammar, and a second
    # copy of it is how a row key an owner typed stops matching the line the refusal prints.
    rowlines: dict = {k: {} for k in BLOCK_KEYS}
    lines = raw.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            i += 1
            continue

        mb = _BLOCK_RE.match(line)
        if mb and mb.group(1) in BLOCK_KEYS:
            key = mb.group(1)
            i += 1
            rows = []
            while i < len(lines):
                nxt = lines[i]
                if not nxt.strip():
                    i += 1
                    continue
                if not nxt[:1].isspace():
                    break
                body = nxt.strip()
                if not body.startswith("#"):
                    rows.append((i + 1, body))
                i += 1
            out[key] = _parse_block(key, rows, p)
            rowlines[key] = {k: ln for k, (ln, _rest) in _parse_rows(rows, p).items()}
            continue

        ms = _SCALAR_RE.match(line)
        if ms:
            val = ms.group(2).strip()
            if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
                val = val[1:-1]
            out[ms.group(1)] = val
            i += 1
            continue

        raise ConfError(f"{p}:{i + 1}: not a KEY=VALUE line, a KEY: block header, or a comment: {stripped!r}")

    check_declaration(out, p, rowlines)
    return out


def _parse_rows(rows: list[tuple[int, str]], p: Path) -> dict[str, tuple[int, str]]:
    """The GENERIC block shape: `<row-key> <rest>`, split on the first run of whitespace.

    Insertion-ordered, and the line number rides along because every caller's refusal has to name
    it. No `.isalpha()` test — that one lives in the `VERBS` arm, and it is the whole reason a
    dotted row key such as `py.function` could not be written down before this.
    """
    table: dict[str, tuple[int, str]] = {}
    for lineno, body in rows:
        parts = body.split(None, 1)
        rowkey = parts[0]
        if rowkey in table:
            raise ConfError(f"{p}:{lineno}: duplicate row key {rowkey!r}, first seen at "
                            f"line {table[rowkey][0]}")
        table[rowkey] = (lineno, parts[1].strip() if len(parts) > 1 else "")
    return table


def _parse_verbs(rows: list[tuple[int, str]], p: Path) -> dict[str, str]:
    """`{verb: gloss}`. The one arm with an alphabetic row key, and the reason it is an arm."""
    table: dict[str, str] = {}
    for lineno, body in rows:
        parts = body.split(None, 1)
        verb = parts[0].rstrip(":")
        if not verb.isalpha():
            raise ConfError(f"{p}:{lineno}: a verb must be alphabetic, got {verb!r}")
        table[verb.lower()] = parts[1].strip() if len(parts) > 1 else ""
    return table


def parse_cell_key(rowkey: str, where: str = "") -> tuple[str, str, str | None, str | None]:
    """`<ext>.<surface>[+<kind>:<literal>]` -> `(ext, surface, kind, literal)`; kind is None for a
    plain cell.

    ONE READER for the row key, because three callers ask the same question of it — the `CELLS`
    parser, the cross-block check below, and the engine's routing — and a second copy of the split is
    how a key an owner typed stops matching the row a refusal prints. `where` is the caller's
    `"<file>:<line>: "` prefix; it is a prefix rather than a pair of arguments so a caller with no
    position (the engine, reading an ALREADY-parsed block) passes nothing and still gets the message.

    THE SELECTOR RIDES ON THE KEY rather than in a block of its own, and that buys three things a
    second block does not: the `PINS` block is keyed on the cell string, so a selector'd key gets its
    own pin row for free; the report is keyed on the same string, so a selector'd row prints with no
    second lookup; and one cell's declaration stays in one place, which matters because the parent
    and the selector PARTITION a population — reading only one of them tells a reader the wrong
    denominator.
    """
    head, sep, sel = rowkey.partition("+")
    parts = head.split(".")
    if len(parts) != 2 or not all(parts):
        raise ConfError(f"{where}a CELLS row key is `<ext>.<surface>`, optionally followed by one "
                        f"`+<kind>:<literal>` selector, got {rowkey!r}")
    if parts[1] not in SURFACES:
        raise ConfError(f"{where}unknown surface {parts[1]!r} in {rowkey!r}; "
                        f"the closed set is {' '.join(SURFACES)}")
    if not sep:
        return parts[0], parts[1], None, None
    kind, ksep, lit = sel.partition(":")
    if not ksep or kind not in SELECTOR_KINDS:
        raise ConfError(f"{where}a CELLS selector is `+<kind>:<literal>` with a kind in "
                        f"{' '.join(SELECTOR_KINDS)}, got {'+' + sel!r} in {rowkey!r}")
    if not _SEL_LIT_RE.match(lit):
        raise ConfError(f"{where}selector literal {lit!r} in {rowkey!r} is not `[A-Za-z0-9_]+`; a "
                        f"dot there would make this cell's own PINS row key unparseable")
    return parts[0], parts[1], kind, lit


def _parse_cells(rows: list[tuple[int, str]], p: Path) -> dict[str, tuple[str, frozenset]]:
    """`{"py.function": ("snake", frozenset({"vocab"}))}` from `<ext>.<surface>  <conv> [flags]`.

    The row key is kept VERBATIM as the dict key rather than exploded into a tuple: a string key is
    what lets `--print-rows` emit the block for bash without a second grammar, and what lets a row
    be grepped by the exact text an owner typed. Callers split at the dot themselves.
    """
    out: dict[str, tuple[str, frozenset]] = {}
    for rowkey, (lineno, rest) in _parse_rows(rows, p).items():
        parse_cell_key(rowkey, f"{p}:{lineno}: ")
        toks = rest.split()
        if not toks:
            raise ConfError(f"{p}:{lineno}: CELLS row {rowkey!r} declares no convention")
        conv, flags = toks[0], toks[1:]
        if conv not in CONVENTIONS:
            # `dot` is a CLASSIFIER form and deliberately not declarable: no language convention is
            # "identifiers contain dots", so a `dot` cell would be one nothing could be written for.
            extra = (" — `dot` is a classifier form the report uses, not a declarable convention"
                     if conv == "dot" else "")
            raise ConfError(f"{p}:{lineno}: unknown convention {conv!r} in {rowkey!r}; "
                            f"the closed set is {' '.join(CONVENTIONS)}{extra}")
        for f in flags:
            if f not in _CELL_FLAGS:
                raise ConfError(f"{p}:{lineno}: unknown cell flag {f!r} in {rowkey!r}; "
                                f"the closed set is {' '.join(_CELL_FLAGS)}")
        out[rowkey] = (conv, frozenset(flags))
    return out


def _parse_pins(rows: list[tuple[int, str]], p: Path) -> dict[str, int]:
    """`{"py.file.conv": 7}` from `<ext>.<surface>.<predicate>  <count>`.

    ROW SEPARATION IS A REFUSAL HERE, not a convention a fixture remembers (fork F1, option (c)).
    Two pin rows on consecutive lines merge badly: two branches each draining a neighbouring cell
    conflict, which is the likeliest concurrent pair because related cells sit together. One blank
    line between rows gives git the context line that makes those merges clean, so the reader
    REQUIRES it — over the tracked declaration, on a leg with no guard, rather than over a fixture
    the selftest wrote for itself. A comment line between two rows satisfies it too: the block
    scanner drops `#` rows while still advancing the counter.
    """
    out: dict[str, int] = {}
    prev: tuple[str, int] | None = None
    for rowkey, (lineno, rest) in _parse_rows(rows, p).items():
        if prev is not None and lineno == prev[1] + 1:
            raise ConfError(f"{p}:{lineno}: PINS rows {prev[0]!r} (line {prev[1]}) and {rowkey!r} "
                            f"(line {lineno}) are adjacent; separate every pin row with one blank "
                            f"line so two branches draining neighbouring cells merge clean")
        prev = (rowkey, lineno)
        parts = rowkey.split(".")
        if len(parts) != 3 or not all(parts):
            raise ConfError(f"{p}:{lineno}: a PINS row key is `<ext>.<surface>.<predicate>`, "
                            f"got {rowkey!r}")
        if parts[2] not in PIN_PREDICATES:
            raise ConfError(f"{p}:{lineno}: unknown pin predicate {parts[2]!r} in {rowkey!r}; "
                            f"the closed set is {' '.join(PIN_PREDICATES)}")
        if not rest.isdigit():
            raise ConfError(f"{p}:{lineno}: a PINS count must be a non-negative integer, "
                            f"got {rest!r} for {rowkey!r}")
        out[rowkey] = int(rest)
    return out


def _parse_patterns(rows: list[tuple[int, str]], p: Path) -> dict[str, "re.Pattern"]:
    r"""`{"ts-regex.functions": <compiled>}` from `<pattern-set-id>.<part>  <one Python regex>`.

    THE REST OF THE ROW IS THE REGEX, verbatim to end of line and compiled with `re.M` exactly as the
    shipped sets in `lexicon.py` are. No quoting and no escaping layer: a pattern is already a
    hand-tuned string of punctuation, and a second level of it is how an adopter ends up debugging
    the declaration grammar instead of their extractor.

    EXACTLY ONE CAPTURING GROUP, refused at parse time rather than at extraction time. `_probe_defs`
    reads `m.group(1)` and nothing else, so a zero-group row raises `IndexError` mid-walk and a
    two-group row silently grades the wrong half of every name it matches. The first is a crash with
    no line number; the second is a predicate reporting confidently on the wrong population. Both
    become one refusal naming the file and the line, which is what the rest of this reader promises.
    A row that fails is never a SKIPPED row: this reader does not degrade a declaration into a
    smaller one.
    """
    out: dict[str, "re.Pattern"] = {}
    for rowkey, (lineno, rest) in _parse_rows(rows, p).items():
        parts = rowkey.split(".")
        if len(parts) != 2 or not all(parts):
            raise ConfError(f"{p}:{lineno}: a PATTERNS row key is `<pattern-set-id>.<part>`, "
                            f"got {rowkey!r}")
        if not _PSET_RE.match(parts[0]):
            raise ConfError(f"{p}:{lineno}: pattern-set id {parts[0]!r} in {rowkey!r} is not "
                            f"`[A-Za-z0-9_-]+`, so no LANGS row could ever name it")
        if parts[1] not in PATTERN_PARTS:
            raise ConfError(f"{p}:{lineno}: unknown extractor part {parts[1]!r} in {rowkey!r}; "
                            f"the closed set is {' '.join(PATTERN_PARTS)}")
        if not rest:
            raise ConfError(f"{p}:{lineno}: PATTERNS row {rowkey!r} declares no regex")
        try:
            rx = re.compile(rest, re.M)
        except re.error as e:
            raise ConfError(f"{p}:{lineno}: PATTERNS row {rowkey!r} is not a Python regex: {e}") from e
        if rx.groups != 1:
            raise ConfError(f"{p}:{lineno}: PATTERNS row {rowkey!r} has {rx.groups} capturing "
                            f"group(s); the extractor reads group 1 and nothing else, so a row "
                            f"declares exactly one — wrap the NAME and make every other group "
                            f"non-capturing with `(?:...)`")
        out[rowkey] = rx
    return out


def _parse_canon(rows: list[tuple[int, str]], p: Path) -> dict[str, tuple]:
    """`{"build": ("create", "make")}` from `<representative> <alternative>...`, whitespace split.

    THE OWNER'S DOOR ONTO A FROZEN TABLE (TOOL-aSurfacedLexicon-11), and the shape is deliberately
    the one `canon.CLUSTERS` already has. A leading minus on the row key deletes a shipped cluster
    and takes no alternatives. What each direction MEANS, and every refusal, lives in
    `canon.build_clusters` — this arm parses and validates nothing beyond the token shape, because
    a second copy of the merge's rules here is the two-answers-to-one-question class.

    A row key is checked for shape and nothing else: the block is an overlay over a table of ASCII
    verbs, so a key carrying punctuation could only ever name a cluster that does not exist, and
    saying so at the line beats a `KeyError` from the merge with no file in it.
    """
    out: dict[str, tuple] = {}
    for rowkey, (lineno, rest) in _parse_rows(rows, p).items():
        head = rowkey[1:] if rowkey.startswith("-") else rowkey
        if not head.isalpha():
            raise ConfError(f"{p}:{lineno}: a CANON representative is alphabetic, optionally "
                            f"preceded by one `-` to delete a shipped cluster, got {rowkey!r}")
        forms = rest.split()
        bad = [f for f in forms if not f.isalpha()]
        if bad:
            raise ConfError(f"{p}:{lineno}: CANON row {rowkey!r} names non-alphabetic "
                            f"alternative(s) {' '.join(bad)!r}")
        out[rowkey] = tuple(forms)
    return out


#: The dispatch, and it is also the GUARD. A new block key costs ONE row here plus its row parser.
#: There is no default: `_BLOCK_PARSERS.get(key, _parse_rows)` sat under a membership test against
#: `BLOCK_KEYS` that had already raised for every key outside it, so the fallback could not be taken
#: by any input — dead code reading as a safety net. Worse, had it ever been reachable it would have
#: parsed an unvalidated block SILENTLY, which is the degrade-into-a-smaller-declaration this reader
#: exists to refuse. Guarding on THIS dict rather than on `BLOCK_KEYS` is what keeps the refusal
#: live: a key added to `BLOCK_KEYS` with no parser written is now a named ConfError instead of a
#: `KeyError` with no file in it.
_BLOCK_PARSERS = {"VERBS": _parse_verbs, "CELLS": _parse_cells, "PINS": _parse_pins,
                  "PATTERNS": _parse_patterns, "CANON": _parse_canon}


def _parse_block(key: str, rows: list[tuple[int, str]], p: Path):
    """Keyed dispatch. A key with no parser REFUSES rather than falling through to a generic one or
    off the end returning `None`: this reader never degrades a declaration into an empty one."""
    if key not in _BLOCK_PARSERS:
        raise ConfError(f"{p}: no block parser for {key!r}")
    return _BLOCK_PARSERS[key](rows, p)


def check_declaration(conf: dict, p: Path, rowlines: dict) -> None:
    """The two CROSS-BLOCK refusals, run after the whole file is parsed.

    After, because `LANGS` may be declared BELOW `CELLS` and a reader that refuses on line order
    refuses a legal file. Called from the TAIL of `load_conf` rather than from a verdict path in
    `lexicon.py`, so every one of this module's four consumers refuses identically — including
    `adopt-lexicon.sh`, which shells out here and sets `fail=1` on a non-zero rc. That placement is
    what puts these refusals on a gate leg with an empty guard, where a conf-only commit reaches
    them.

    `rowlines` is `{block: {rowkey: lineno}}` and is REQUIRED, not defaulted. These two refusals
    named the FILE and not the line, and they were the only row-level ones here that did — an owner
    reading "CELLS row 'ts.function' names extension 'ts'" had to grep for the row the reader had
    just been looking straight at. The two that legitimately stay file-only are `load_conf`'s
    unreadable-file case, which has no line to name, and `_parse_block`'s missing-parser case, which
    is about a KEY rather than a position; `grep -n 'raise ConfError(f"{p}:' ` shows the split. A
    default here would let a caller silently re-earn the file-only message, which is the omission
    itself rather than a guard against it.
    """
    cells = conf.get("CELLS") or {}
    if cells:
        declared = {ext: mode for ext, _pset, mode in langs(conf)}
        for rowkey in cells:
            ext, _surface, kind, _lit = parse_cell_key(rowkey)
            if ext not in declared:
                raise ConfError(f"{p}:{rowlines['CELLS'][rowkey]}: CELLS row {rowkey!r} names "
                                f"extension {ext!r}, which LANGS does not declare")
            # A DECORATOR SELECTOR IS A `parser` CAPABILITY, and this is the third cross-block
            # refusal for the same reason as the two beside it: a `probe` set is a regex over text
            # and knows nothing about decorators, so the subset would be EMPTY and the cell would
            # report a clean zero at it forever. A named refusal here, at the line it is written on,
            # beats a `DEAD CELL` two layers down that names the population and not the cause.
            if kind == "decorator" and declared[ext] != "parser":
                raise ConfError(f"{p}:{rowlines['CELLS'][rowkey]}: CELLS row {rowkey!r} declares a "
                                f"`decorator` selector on extension {ext!r}, which LANGS declares "
                                f"{declared[ext]!r}; decorators come from a real parse, so a "
                                f"{declared[ext]!r} language would route an EMPTY subset and grade "
                                f"nothing")
    for rowkey in conf.get("PINS") or {}:
        cell = ".".join(rowkey.split(".")[:2])
        if cell not in cells:
            raise ConfError(f"{p}:{rowlines['PINS'][rowkey]}: PINS row {rowkey!r} names cell "
                            f"{cell!r}, which has no CELLS row")



def build_negatives(conf: dict) -> dict:
    r"""`{verb: {banned-token, ...}}` from the NOT clauses in each VERBS gloss.

    THE BACKTICKS ARE THE GRAMMAR, not decoration. Measured against the table this landed on: the
    pattern ``NOT\s+`([A-Za-z]+)` `` matches exactly the rows a bare `\bNOT\b` word match does, so
    there is no un-backticked `NOT` anywhere in the corpus this must govern — it parses every
    existing row with zero rewrites and zero false positives. A looser pattern would have to guess
    where the token ends, and the prose after the comma is the half a reader actually needs.

    A row may carry SEVERAL build_negatives. The gloss keeps its prose; only the tokens are extracted.
    """
    out = {}
    for verb, gloss in (conf.get("VERBS") or {}).items():
        out[verb] = set(re.findall(r"NOT\s+`([A-Za-z][A-Za-z0-9_]*)`", gloss or ""))
    return out

def langs(conf: dict) -> list[tuple[str, str, str]]:
    """`LANGS` as `(ext, pattern_set_id, mode)` triples. An empty pattern-set id is legal and is
    what a `dark` declaration looks like — it names no extractor on purpose."""
    out = []
    for tok in (conf.get("LANGS") or "").split():
        parts = tok.split(":")
        if len(parts) != 3:
            raise ConfError(f"LANGS entry must be `<ext>:<pattern-set-id>:<mode>`, got {tok!r}")
        ext, pset, mode = parts
        if mode not in ("parser", "probe", "dark"):
            raise ConfError(f"LANGS mode must be parser, probe or dark, got {mode!r} in {tok!r}")
        out.append((ext.lstrip("."), pset, mode))
    return out


def _main(argv: list[str]) -> int:
    """`--print-verbs <conf>` one verb per line, `--print-rows [<block>] <conf>` key+TAB+rest.

    `--print-rows` exists because the Skill render needs the GLOSS, and rendering it any other way
    means a second parser for the block grammar. That was the shape the closing review found (H2):
    the render carried its own inline parser, so the two disagreed on a continuation line and on a
    row whose gloss contained a colon, and the drift gate could not see it — it compared two outputs
    of the SAME renderer. One reader, two output shapes.

    The OPTIONAL block key on `--print-rows` is what lets `adopt-lexicon.sh` read the (language,
    surface) matrix through this one reader too. Omitting it keeps the `VERBS` behaviour byte for
    byte, so no existing caller changes.

    Anything else is a usage
    refusal: this module is a library first and a CLI only for the one consumer that cannot import."""
    block = "VERBS"
    if len(argv) == 4 and argv[1] == "--print-rows":
        block, argv = argv[2], [argv[0], argv[1], argv[3]]
    if len(argv) != 3 or argv[1] not in ("--print-verbs", "--print-rows") or block not in BLOCK_KEYS:
        sys.stderr.write("usage: python tools/lexicon/lexicon_conf.py "
                         "--print-verbs <conf> | --print-rows [" + "|".join(BLOCK_KEYS) + "] <conf>\n")
        return 2
    try:
        conf = load_conf(argv[2])
    except ConfError as e:
        sys.stderr.write(f"lexicon-conf: {e}\n")
        return 1
    if argv[1] == "--print-rows":
        for rowkey, val in (conf.get(block) or {}).items():   # DECLARATION order, which the Skill preserves
            if block == "CELLS":
                val = " ".join([val[0], *sorted(val[1])])
            elif block == "CANON":
                # THE DETECTION ROUTE for `adopt-lexicon.sh`'s stamp refusals, and it is this flag
                # rather than a grep. `--print-rows CANON` prints one overlay row per line and
                # exits 0 with NO output where no block is declared, which is the whole predicate
                # the stamp arm needs. `adopt-lexicon.sh` already rules a second parser out by
                # name; this is the shell-out it rules in. TOOL-aSurfacedLexicon-11.
                val = " ".join(val)
            elif block == "PATTERNS":
                # The COMPILED object is what the block holds, so print the source it was compiled
                # from. `str(re.compile(...))` is a repr, and a repr is not the row an owner typed.
                val = val.pattern
            print(f"{rowkey}	{str(val).strip()}")
        return 0
    for verb in sorted(conf.get("VERBS") or {}):
        print(verb)
    return 0


if __name__ == "__main__":
    raise SystemExit(_main(sys.argv))
