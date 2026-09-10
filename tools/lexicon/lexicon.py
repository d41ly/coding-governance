#!/usr/bin/env python3
# gov:kit lexicon@1.2
"""lexicon.py — two naming predicates over a DECLARED vocabulary, plus one self-containment refusal.

THE INVOCATIONS ARE NOT LISTED HERE. Run the file with no recognised mode and it prints them, with
its own path DERIVED rather than spelled — because this kit installs at whatever prefix an adopter
chose and `apply` writes gov's bytes VERBATIM, so a literal path in this docstring arrives unchanged
in a tree where it resolves to nothing. A usage block in a docstring is also the second spelling of
what the program already prints, and it is the copy nobody re-renders. DEPL-dCarriedReceipt-15 S5.

WHAT THIS IS FOR, since it is not typo-catching. A closed verb table makes "which verb is this"
answerable only when a function has ONE responsibility, so a name that will not fit the table is
reporting an unclear responsibility or a seam in the wrong place. The rows that matter are the ones
pinned by what they are NOT — `build` not `create`, `load` not `fetch`. A table without negative
definitions is decoration.

COVERAGE MODES, and the law behind them. `map_extractors.py` refuses to ship a regex extractor for
shell and declares that language recall-dark instead, because a regex over shell definitions would
look like coverage while silently skipping what it forgot. That law binds here, so every extension
in the corpus carries a DECLARED mode and an undeclared one is a named refusal:

    parser  a real parse                  complete over its extension
    probe   a regex pattern set           incomplete BY CONSTRUCTION, reported as such every run
    dark    none, declared explicitly     named every run, never silently absent

TWO PARSERS SHIP, and which one runs is the `LANGS` row's pattern-set id, not a second mode token:
`python-ast` is `ast`, `shell-tokens` is the tokenizer in `parse_shell_defs`. That law above is why
the shell one is a tokenizer: the naive same-line regex over this corpus over-counts a JavaScript
function sitting inside a bash heredoc, AND a heredoc-aware refinement of that same regex loses
real definitions to a quoted run of `<` characters it mistakes for an opener. Two regex readings of
one population, each wrong where the other is not, which is the whole argument for tokenizing.
NO FIGURE IS QUOTED HERE and the omission is deliberate: this header and the kit README each
carried a number for that loss and they disagreed with each other, which is one fact with two
carriers and no gate between them. The reason this used to give — that the refinement "was never
committed, so no reader could re-derive either" — is FALSE about the commit that carried it: the
refinement ships as a runnable snippet in `memory/builds/aSurfacedLexicon/spec/`'s unit-14 spec,
tracked in the same build. Corrected at the closing review (M5), which is worth its own sentence
because a comment justifying an omission by asserting a record does not exist is a claim about the
tree, and this kit's own `KNOWN_EXTS` comment states the rule it broke: a fix comment is read as
provenance, so an overstated one is worse than none. Both counts are re-derivable from that
snippet; the reproducible one for a reader in a hurry is the naive count, in the build record with
its command. TOOL-aSurfacedLexicon-14.

VACUITY IS THE DOMINANT FAILURE MODE, not false positives — a predicate that selects an empty
population passes green forever and tells you nothing. Three checks push back:

  DEAD PROBE          a parser/probe language whose definition population is empty against a corpus
                      containing that extension — an extractor that has gone inert; and, in
                      `check_self_containment`, a self-containment walk that judged NO imports
  frozen SENTINELS    a fixture per shipped pattern set in `selftest.py`, because the corpus-side
                      arm above is itself defeated by an empty corpus

THE THIRD PREDICATE IS GONE, and this paragraph is its epitaph rather than its documentation.
`P3 layer` graded a DECLARED, glob-shaped, repo-relative import direction out of a `LAYERS` block,
and it cost a glob dialect, a module index and an import resolver — 164 lines and 29 self-test arms
— to enforce ONE declared rule whose pin never left `"0"` in its whole history, over a population it
reported as 557 imports and could actually reach 44 of. Four review rounds each found a blocker in
`_glob_match` or `resolve_import`, none of them visible to an end-to-end fixture. The rule the repo
actually relied on survives, in `check_self_containment` below: this kit ships SELF-CONTAINED, which
is why `subtokens.py` is a port of a `codebase-map` function rather than an import of it. That
refusal resolves nothing and globs nothing, so the two helpers that carried every P3 defect have no
successor. TOOL-aSurfacedLexicon-2.
"""

import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import canon  # noqa: E402
from lexicon_conf import (ConfError, CONVENTIONS, PATTERN_PARTS, SURFACES, langs,  # noqa: E402
                          load_conf, build_negatives, parse_cell_key)
from subtokens import (check_convention, classify, leading_verb, read_stem,  # noqa: E402
                       render_convention, subtokens)

KIT_LEXICON_VERSION = "1.2"

CONF_NAME = ".lexicon.conf"
WAIVER_FILES = {
    "verb": "lexicon-verb-waivers.txt",
    "suffix": "lexicon-suffix-waivers.txt",
}
#: The extensions this kit can extract, and the ONE place they are declared. `scaffold_lexicon.py`
#: imports this rather than keeping its own copy: the two had ALREADY diverged on the `py` pattern
#: set (`""` here against `"python-ast"` there) within one build. The divergence was real; the
#: CONSEQUENCE this comment first claimed was not. It said the two graded python through different
#: code paths, and they do not — `extract_text` dispatches on `mode` alone and reads `pset` only
#: under `probe`, so nothing anywhere compares a pattern-set id against `""`. A fix comment is read
#: as provenance, so an overstated one is worse than none. Closing review M7, trimmed by round 2.
KNOWN_EXTS = {"py": ("python-ast", "parser"), "js": ("js-regex", "probe"),
              "sh": ("shell-tokens", "parser")}

PIN_KEYS = {"verb": "VERB_OFFENDER_PIN", "suffix": "SUFFIX_OFFENDER_PIN"}

#: The predicate keys, in report order. ONE spelling, because there were four literal `("verb",
#: "suffix", "layer")` tuples in `run()` and a fifth in the tally loop — deleting a predicate meant
#: finding all of them.
KINDS = ("verb", "suffix")

#: The S7 guard's predicate: a string literal in `scaffold_lexicon.py` that BEGINS `CANON:`, which
#: is what an emitted block header looks like. Deliberately not the bare token — that matches the
#: file's own `# PROPOSED from the SHIPPED CANON` comment, and a guard whose pass condition is a
#: comment's wording is the gate-satisfied-by-its-own-prose class. TOOL-aSurfacedLexicon-11.
_CANON_HEADER_RE = re.compile(r"""["']\s*CANON:""")

#: The shipped `probe` pattern sets. Each one MUST have a frozen sentinel fixture in `selftest.py`
#: that yields a non-zero definition count, so a set going inert fails there rather than here.
#:
#: SHIPPED, NOT RESOLVED, and the two names are kept apart on purpose. This kit installs under
#: `role = "engine"`, so an upgrade overwrites this file: an adopter arming TypeScript, Go or C# by
#: editing the dict below would lose it on the next `apply`, which is why the extractor set is
#: DECLARABLE in `.lexicon.conf` and merged over this one by `resolve_pattern_sets`. Nothing
#: mutates this constant. TOOL-aSurfacedLexicon-9.
PATTERN_SETS = {
    "js-regex": {
        "functions": [
            re.compile(r"^\s*(?:export\s+)?(?:async\s+)?function\s+([A-Za-z_$][\w$]*)", re.M),
            re.compile(r"^\s*(?:export\s+)?(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*(?:async\s*)?\([^)]*\)\s*=>", re.M),
        ],
        "types": [re.compile(r"^\s*(?:export\s+)?class\s+([A-Za-z_$][\w$]*)", re.M)],
        "imports": [
            re.compile(r"""^\s*import\s+(?:[^'"]*\s+from\s+)?['"]([^'"]+)['"]""", re.M),
            re.compile(r"""require\(\s*['"]([^'"]+)['"]\s*\)""", re.M),
        ],
    },
}


#: S2 — the COVERAGE SNIFFER. A deliberately BROAD, deliberately INCOMPLETE probe for "does this file
#: define anything at all", run over every tracked text file regardless of its `LANGS` declaration.
#:
#: WHY IT CANNOT REUSE THE ARMED EXTRACTORS: they only run on declared-armed extensions, so a
#: denominator built from them is the numerator. Measuring coverage needs a reading of the files the
#: kit does NOT grade, which is exactly the population no armed extractor may touch.
#:
#: WHAT STOPS IT BECOMING A SECOND VOCABULARY: it answers ONE boolean per file and feeds ONE consumer,
#: a printed fraction. It names nothing, grades nothing, and no predicate reads it. A regex here that
#: is wrong costs an inaccurate percentage; a regex in `PATTERN_SETS` that is wrong costs a verdict.
#: That asymmetry is the whole containment and it is structural rather than promised.
#:
#: It is a HEURISTIC and the README says so. It is not a lexer and it is not a step toward one.
#:
#: WIDENED FOR TYPESCRIPT BY TOOL-aGradedDialect-3 S8, and the reason is a REFUSAL rather than a
#: coverage number. `DEAD SNIFFER` reds when an ARMED extractor finds a definition in a file this
#: sniffer reads as empty, and six of `parse_ts_defs`'s definition forms sniffed NEGATIVE against
#: the rows above — measured 2026-09-10: `export interface Props`, `export type Id =`,
#: `export enum`, `export const Card: React.FC = () =>`, `const pick = <T,>(x) =>` and
#: `export default function App()`. A `types.ts` carrying only an interface and a type alias is a
#: near-universal shape in a real TypeScript tree, so the FIRST adopter file arming this feature
#: would have redded their gate on the run right after `--scaffold`. Being wrong the OTHER way
#: costs an inaccurate percentage, which is why the new rows are deliberately loose.
DEFINITION_SNIFF = re.compile(
    r"""^[ \t]*(?:
          (?:async[ \t]+)?def[ \t]+\w                     # python, ruby
        | (?:export[ \t]+(?:default[ \t]+)?)?(?:async[ \t]+)?function[ \t]+\w  # js, ts, php, shell
        | (?:export[ \t]+)?(?:abstract[ \t]+)?class[ \t]+\w   # js, ts, php, java, kotlin
        | (?:export[ \t]+)?(?:declare[ \t]+)?(?:interface|enum)[ \t]+\w  # ts, java, kotlin, c#
        | (?:export[ \t]+)?type[ \t]+\w[\w$]*[ \t]*[<=]   # ts type alias
        | (?:export[ \t]+)?(?:const|let|var)[ \t]+\w[\w$]*(?:[ \t]*:[^=\n]+)?[ \t]*=[ \t]*(?:async[ \t]*)?[(<]
        | func[ \t]+\w                                    # go, swift
        | fn[ \t]+\w                                      # rust
        | (?:public|private|protected)[ \t]+[\w<>\[\]]+[ \t]+\w+[ \t]*\(   # java, c#
        | \w[\w-]*[ \t]*\([ \t]*\)[ \t]*\{                # shell `f() {`
        )""",
    re.M | re.X,
)

#: Extensions the sniffer never opens. Not a vocabulary — a read-cost bound. A binary or a lockfile
#: cannot carry a definition and reading it is wasted I/O; being wrong here can only UNDERCOUNT the
#: denominator, which reports coverage as better than it is, so the list is kept short deliberately.
SNIFF_SKIP = {
    # Binary or generated: cannot carry a definition, and reading one is wasted I/O.
    "png", "jpg", "jpeg", "gif", "ico", "pdf", "zip", "gz", "wasm", "lock", "svg",
    # PROSE AND DATA, and this half is a judgement rather than a fact about bytes, so it is argued.
    # A fenced code block inside documentation is an EXAMPLE, not a definition this kit could grade
    # even if the extension were armed. Measured on this repo: including `.md` put 82 documentation
    # files into the denominator and reported coverage as 25.7% against 42.9% — a number that moves
    # when somebody writes a tutorial is not measuring coverage. Data formats are here for the same
    # reason one step simpler: they declare no functions at all.
    "md", "rst", "txt", "json", "toml", "yaml", "yml", "tsv", "csv", "ini", "cfg",
}


def scan_definition_carriers(root: Path, files: list[str]) -> set[str]:
    """Tracked files the sniffer believes define something. S2."""
    out = set()
    for rel in files:
        if ext_of(rel) in SNIFF_SKIP:
            continue
        try:
            src = (root / rel).read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if DEFINITION_SNIFF.search(src):
            out.add(rel)
    return out


class Offender:
    """One finding. `text` is the WAIVER KEY, and it is the matched text rather than
    `<path>:<line>` on purpose: `install-prefix-waivers.txt` keys on position and any edit ABOVE a
    waived line unpins it, which reds a merge that touched nothing the waiver guards.

    `verb` and `cls` carry TOOL-aSurfacedLexicon-7's P1 split and are `None` for every other
    predicate. `cls` is `"debt"` when the canon holds a cluster for the leading token — the kit can
    name the rename — and `"unruled"` when it does not. It is stored rather than re-derived because
    the report, the per-cell pins and the site census all read the same classification, and three
    readers each asking `canon.build_form_index()` again is three chances to answer differently.
    """

    __slots__ = ("kind", "path", "line", "text", "detail", "verb", "cls")

    def __init__(self, kind, path, line, text, detail, verb=None, cls=None):
        self.kind, self.path, self.line, self.text, self.detail = kind, path, line, text, detail
        self.verb, self.cls = verb, cls

    def __str__(self):
        return f"{self.path}:{self.line}: {self.kind}: {self.text} — {self.detail}"


def print_canon_posture(conf: dict) -> None:
    """The UNFREEZE, on EVERY run and above everything else this file prints. S4.

    A run that prints nothing here means the canon is frozen, and there is no state in which it is
    quietly overridden. Green output is where a reader stops looking, so that is where the fact
    sits — a posture visible only on a red run is the quiet unfreeze with an extra step, which is
    the mirror defect this door was designed not to become. TOOL-aSurfacedLexicon-11.
    """
    rows = conf.get("CANON") or {}
    if not rows:
        return
    print(f"lexicon: CANON UNFROZEN — {len(rows)} owner row(s) merged over the shipped clusters; "
          f"stamp {(conf.get('canon_unfrozen') or '').strip()!r}")


def read_debt_gloss(verb: str, forms: dict | None = None,
                    clusters=None) -> tuple[str, str]:
    """`(representative, gloss)` for a token the shipped canon holds a cluster for; `("", "")` else.

    THE SPLIT'S WHOLE CLASSIFIER, and it is one dict lookup on purpose. A P1 offender whose leading
    token is a key of `canon.build_form_index()` is DEBT — the kit can name the rename it owes — and
    one that is not is UNRULED, which is a scoping question no vocabulary can answer for the author.

    THE CANON DECIDES THE SPELLING, NEVER THE STANDARD. `canon.py` is prescriptive, frozen in the
    kit under `role = "engine"`, and was written without reading any adopter's corpus, so consulting
    it here cannot turn what this repo already does into what it should do. The corpus is evidence
    for exactly ONE thing on this path: which spellings become debt. TOOL-aSurfacedLexicon-7.

    `forms` is the resolved index, passed by the corpus walk so 968 offenders do not rebuild it 968
    times; `--suggest` grades one name and lets it default.

    `clusters` is the MERGED tuple where an owner declared a `CANON:` overlay, and BOTH arguments
    have to travel together: `forms` decides the representative and `clusters` is what the gloss is
    read out of, so passing a merged index with the shipped tuple resolves an owner's form and then
    prints the shipped gloss for it, or the empty string. That pairing is the defect two revisions
    of this unit's spec carried. TOOL-aSurfacedLexicon-11.
    """
    clusters = canon.CLUSTERS if clusters is None else clusters
    forms = canon.build_form_index(clusters) if forms is None else forms
    rep = forms.get(verb, "")
    return (rep, canon.read_gloss(rep, clusters)) if rep else ("", "")


def render_swapped_name(name: str, want: str) -> str:
    """`name` with its leading subtoken replaced by `want`, in the CALLER's own spelling.

    ONE HOME FOR THE SWAP, because there are now two readers of it — the P1 offender line and
    `--suggest` — and two implementations of "what should this be called instead" is the same defect
    this kit exists to gate, one level up. TOOL-aSurfacedLexicon-7.

    THE TAIL IS THE ORIGINAL SURFACE, SLICED. It is never re-derived, and two review rounds were
    needed to land on that. Round 1 sliced by `len(verb)` while `leading_verb` had stripped the
    leading underscores first, so the two disagreed about where the verb ended and `_fetch_conf`
    suggested `_load_h_conf`. Round 2 found that rebuilding the tail out of `subtokens()` — the
    round-1 fix — traded that for worse: the splitter lowercases, breaks acronym runs, splits digit
    boundaries and drops anything outside its character class, so `getUserURLs` came back as
    `readUserUrLs`, `fetch_v2_data` as `load_v_2_data` and `create$data` as `build_data` with the
    `$` silently gone. Three of those had been CORRECT before the fix.

    Slicing at the end of the FIRST SUBTOKEN's own surface is what both rounds were reaching for.
    The splitter decides where the verb ends, which is the half round 1 had right; nothing
    downstream re-spells a character the caller wrote, which is the half round 2 had right.
    Separator style, case, acronym runs, digit suffixes, trailing underscores and characters the
    splitter cannot even see all survive, because not one of them is ever regenerated.

    THE VERB INHERITS THE CASE OF THE TOKEN IT REPLACES, so a SCREAMING_SNAKE name is not answered
    in lower snake and a PascalCase one is not answered in camelCase. Round 1 answered every shape
    in the declaration's own lowercase, which is a second way of handing back a name whose only
    remaining defect is that the author must edit it before typing it.
    """
    lead = name[:len(name) - len(name.lstrip("_"))]
    body = name[len(lead):]
    toks = subtokens(name)
    first = toks[0] if toks else ""
    if not first or body[:len(first)].lower() != first:
        # The splitter and the surface disagree. `leading_verb`'s contract allows that for a name
        # with no word characters; answer with the bare verb rather than invent a tail for it.
        surface, rest = "", ""
    else:
        surface, rest = body[:len(first)], body[len(first):]
    if len(surface) > 1 and surface.isupper():
        cased = want.upper()
    elif surface[:1].isupper():
        cased = want[:1].upper() + want[1:]
    else:
        cased = want
    return lead + cased + rest


def measure_vocab_cells(unwaived: list, cells: dict) -> tuple[dict, list]:
    """`{cell: (debt, unruled)}` over every `CELLS` row carrying the `vocab` flag, plus refusals.

    SCOPED TO THE CELLS THAT EXIST (S4). A pair with no `CELLS` row gets no pin row, so on a tree
    whose declaration arms no `vocab` cell this returns `{}` and the scalar `VERB_OFFENDER_PIN` is
    the only verb ratchet — which is the state this unit lands in, deliberately, because a `PINS`
    row naming an undeclared cell is a `load_conf` refusal on the unguarded wiring leg.

    THE TWO REFUSALS BELOW ARE WHY THIS IS NOT THREE INLINE LINES. A `vocab` flag on a surface P1
    does not grade, or on a routed subset whose partition this census does not read, would count the
    WHOLE extension's offenders under that row's name — a pin that ratchets a population it does not
    describe. Both are named where they are written rather than reported as a plausible number.
    """
    rows: dict[str, tuple[int, int]] = {}
    problems: list[str] = []
    per: dict[str, list] = {}
    for o in unwaived:
        per.setdefault(f"{ext_of(o.path)}.{PREDICATE_SURFACES['verb']}", []).append(o)
    for cell, (_conv, flags) in cells.items():
        if "vocab" not in flags:
            continue
        _ext, surface, kind, _lit = parse_cell_key(cell)
        if surface != PREDICATE_SURFACES["verb"]:
            problems.append(
                f"VOCAB ON THE WRONG SURFACE — the cell `{cell}` carries the `vocab` flag, but P1 "
                f"grades the `{PREDICATE_SURFACES['verb']}` surface and this row names "
                f"`{surface}`. Its debt/unruled pair would count a population the row does not "
                f"describe, so it is refused rather than reported.")
            continue
        if kind:
            problems.append(
                f"VOCAB ON A ROUTED SUBSET — the cell `{cell}` carries the `vocab` flag on a "
                f"`{kind}` selector. P1's offenders are censused per extension and not through the "
                f"cell partition, so this row's pair would be its PARENT's count under a selector's "
                f"name. Declare `vocab` on the parent row, or extend the census to the partition.")
            continue
        got = per.get(cell, [])
        rows[cell] = (sum(1 for o in got if o.cls == "debt"),
                      sum(1 for o in got if o.cls == "unruled"))
    return rows, problems


def render_pin_rows(rows: dict) -> list[str]:
    """The `PINS:` rows for `measure_vocab_cells`'s census, BLANK-SEPARATED (S5).

    The blank line is not formatting. `_parse_pins` REFUSES two rows whose line numbers differ by
    one — TOOL-aSurfacedLexicon-4's S10, so that two branches draining neighbouring cells merge
    clean — and this is the emitter that reader grades. A dense emission would produce bytes
    `adopt-lexicon.sh --check` rejects on an unguarded leg, which is a `--measure` output nobody can
    paste. Returned as a list of lines rather than one string so the caller decides the surround.
    """
    out: list[str] = []
    for cell, (debt, unruled) in rows.items():
        if out:
            out.append("")
        out.append(f"  {cell}.debt  {debt}")
        out.append("")
        out.append(f"  {cell}.unruled  {unruled}")
    return out


def tracked_files(root: Path) -> list[str]:
    out = subprocess.run(["git", "ls-files"], cwd=root, capture_output=True, text=True)
    if out.returncode != 0:
        raise SystemExit("lexicon: not a git repo, or `git ls-files` failed")
    return [ln for ln in out.stdout.splitlines() if ln.strip()]


def ext_of(path: str) -> str:
    """The extension used for a LANGS lookup. A file with no dot in its BASENAME reports `<none>`,
    which must be declared like any other: two such files are tracked here, and letting them fall
    through unnamed is exactly the silent skip the fail-closed law refuses."""
    base = path.rsplit("/", 1)[-1]
    return base.rsplit(".", 1)[-1] if "." in base else "<none>"


def _python_defs(src: str):
    """Definitions and imports from a real parse. A SyntaxError RAISES rather than degrading to an
    empty result: an unparseable file under a `parser` declaration is a broken corpus, and
    returning `[]` would launder it into a clean run."""
    import ast

    tree = ast.parse(src)
    funcs, types_, imports = [], [], []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            funcs.append((node.name, node.lineno))
        elif isinstance(node, ast.ClassDef):
            types_.append((node.name, node.lineno))
        elif isinstance(node, ast.Import):
            imports.extend((a.name, node.lineno) for a in node.names)
        elif isinstance(node, ast.ImportFrom):
            # `from a.b import c` touches BOTH `a.b` and `a.b.c`, and `c` may itself be a module.
            # Keeping only `node.module` discarded the imported NAME, which made the commonest
            # crossing spelling in Python invisible to the deleted P3, and the same discard would
            # blind `check_self_containment` to `from map_lib import _STOPWORDS`. `node.level`
            # carries the leading dots of a relative import and is preserved here rather than
            # silently flattened — that is how the self-containment walk tells relative from bare.
            dots = "." * (node.level or 0)
            mod = node.module or ""
            if dots or mod:
                imports.append((dots + mod, node.lineno))
            for a in node.names:
                if a.name == "*":
                    continue
                sep = "." if mod else ""
                imports.append((dots + mod + sep + a.name, node.lineno))
    return funcs, types_, imports


#: A shell function name, as this parser will accept one. Deliberately the SAME character class the
#: naive same-line regex used, so the two populations are comparable name-for-name and the only
#: difference between them is what the tokenizer could see that a line match could not.
_SH_NAME = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")

#: Characters that end a heredoc DELIMITER word. Not a general operator set — the tokenizer below
#: dispatches on characters directly and this is the one place it needs a class.
_SH_BREAK = " \t;&|<>\n"


def scan_shell_tokens(src: str) -> list:
    """`[(kind, text, line)]` for shell source: every CODE token, and nothing that is not code.

    `kind` is `word` or `op`; `op` is one of `( ) { }`. Everything else the shell reads as syntax —
    redirections, separators, pipes — is consumed as a word break and emitted as nothing, because
    the four definition forms `parse_shell_defs` recognises need no other operator.

    WHAT IT TRACKS, which is the whole reason this is not a regex: single quotes, double quotes as a
    STATE rather than a span, `$'…'`, backslash escapes and line continuations, `#` comments at a
    word boundary, `${…}` and `$((…))` as opaque expansions, backticks as an opaque span, command
    substitution `$(…)` as suspended-string-state CODE with its own nesting, heredocs with quoted
    and unquoted delimiters in both the plain and `<<-` tab-stripped forms, and here-strings `<<<`.

    THE HERE-STRING IS WHY THE STATE MACHINE EXISTS. `<<<` and a literal run of `<` inside a quoted
    grep pattern are indistinguishable to a line regex and trivially distinguishable here: a
    heredoc-aware REFINEMENT of the naive pattern reads `'^<<<<<<< ours$'` in
    the memory-tree kit's `merge-rows.test.sh` as an opener whose terminator never arrives and blanks
    the thousand lines below it, losing ten real definitions. A tokenizer never enters that branch,
    because the run is inside single quotes.

    RAISES `SyntaxError` on a source it cannot tokenize — an unterminated quote, heredoc or `${`,
    naming the construct and the line it opened on. Never a partial list and never an empty one:
    `scan_corpus` turns that into a named refusal, and returning `[]` would launder a broken file
    into a clean run exactly as it would for `_python_defs`.
    """
    toks: list = []
    word: list = []
    wline = 1
    i, n, line = 0, len(src), 1
    parens: list = []
    heredocs: list = []
    at_word_start = True
    dq = False
    dq_line = 0

    def add_word():
        """Close the word being accumulated, if any, and emit it."""
        nonlocal word
        if word:
            toks.append(("word", "".join(word), wline))
            word = []

    def add_char(s: str):
        """Append source text to the word being accumulated, opening one if none is."""
        nonlocal wline
        if not word:
            wline = line
        word.append(s)

    def read_quoted(j: int, q: str, escapes: bool) -> int:
        """The index just past the `q` that closes a span opened before `j`."""
        while j < n:
            c2 = src[j]
            if escapes and c2 == "\\" and j + 1 < n:
                j += 2
                continue
            if c2 == q:
                return j + 1
            j += 1
        raise SyntaxError(f"unterminated {q} quote opened at line {line}")

    def read_braced(j: int) -> int:
        """The index just past the `}` closing a `${` opened before `j`, counting nesting."""
        depth = 1
        while j < n and depth:
            if src[j] == "\\":
                j += 2
                continue
            if src[j] == "{":
                depth += 1
            elif src[j] == "}":
                depth -= 1
            j += 1
        if depth:
            raise SyntaxError(f"unterminated ${{ opened at line {line}")
        return j

    while i < n:
        c = src[i]

        # --- the expansions a double-quoted string and bare code read the same way ------------
        if c == "\\" and i + 1 < n:
            if src[i + 1] == "\n":
                i += 2
                line += 1
                continue
            add_char(src[i:i + 2])
            i += 2
            at_word_start = False
            continue

        if c == "`":
            j = read_quoted(i + 1, "`", True)
            seg = src[i:j]
            add_char(seg)
            line += seg.count("\n")
            i = j
            at_word_start = False
            continue

        if src.startswith("$((", i):
            j = src.find("))", i + 3)
            if j < 0:
                raise SyntaxError(f"unterminated $(( opened at line {line}")
            seg = src[i:j + 2]
            add_char(seg)
            line += seg.count("\n")
            i = j + 2
            at_word_start = False
            continue

        if src.startswith("${", i):
            j = read_braced(i + 2)
            seg = src[i:j]
            add_char(seg)
            line += seg.count("\n")
            i = j
            at_word_start = False
            continue

        if src.startswith("$(", i):
            # A command substitution's body is CODE, including inside a double-quoted string, so
            # the string state is SUSPENDED here and restored by the `)` that closes it. Handling
            # this by counting parentheses inside the string instead was wrong in both directions
            # and measured so: without the count, `"$(sed "1s/^x*()/y()/")"` closed the string on
            # its inner quote and lost four later definitions; with a bare count, the `(` inside
            # `"$(sed 's/FAILED (\(.*\)/x/')"` closed it one paren early and cost twenty.
            add_word()
            parens.append(("$(", dq))
            dq = False
            i += 2
            at_word_start = True
            continue

        # --- inside a double-quoted string: everything not handled above is literal -----------
        if dq:
            if c == '"':
                add_char('"')
                dq = False
                i += 1
                at_word_start = False
                continue
            if c == "\n":
                line += 1
            add_char(c)
            i += 1
            continue

        # --- code state ------------------------------------------------------------------------
        if c == "\n":
            add_word()
            line += 1
            i += 1
            # A heredoc BODY is not code and is never tokenized. The queue is drained here rather
            # than at the `<<` because a line may open several, and their bodies follow the line.
            while heredocs:
                delim, strip, hline = heredocs.pop(0)
                while True:
                    j = src.find("\n", i)
                    raw = (src[i:] if j < 0 else src[i:j]).rstrip("\r")
                    if (raw.lstrip("\t") if strip else raw) == delim:
                        i = n if j < 0 else j + 1
                        line += 1
                        break
                    if j < 0:
                        raise SyntaxError(
                            f"unterminated heredoc <<{delim} opened at line {hline}")
                    i = j + 1
                    line += 1
            at_word_start = True
            continue

        if c in " \t":
            add_word()
            i += 1
            at_word_start = True
            continue

        if c == "#" and at_word_start:
            j = src.find("\n", i)
            i = n if j < 0 else j
            continue

        if c == "'":
            j = read_quoted(i + 1, "'", False)
            seg = src[i:j]
            add_char(seg)
            line += seg.count("\n")
            i = j
            at_word_start = False
            continue

        if c == '"':
            add_char('"')
            dq, dq_line = True, line
            i += 1
            at_word_start = False
            continue

        if c == "(":
            add_word()
            parens.append(("(", dq))
            toks.append(("op", "(", line))
            i += 1
            at_word_start = True
            continue

        if c == ")":
            add_word()
            marker, was_dq = parens.pop() if parens else ("(", False)
            if marker == "$(":
                dq = was_dq
            else:
                # An UNBALANCED `)` is legal shell — every `case` arm ends with one — so it is
                # emitted rather than refused. Only quote and heredoc states can fail to close.
                toks.append(("op", ")", line))
            i += 1
            at_word_start = True
            continue

        if c in "{}":
            add_word()
            toks.append(("op", c, line))
            i += 1
            at_word_start = True
            continue

        if src.startswith("<<", i):
            add_word()
            strip = src.startswith("<<-", i)
            j = i + (3 if strip else 2)
            while j < n and src[j] in " \t":
                j += 1
            delim: list = []
            while j < n and src[j] not in _SH_BREAK:
                ch = src[j]
                if ch in "'\"":
                    k = read_quoted(j + 1, ch, False)
                    delim.append(src[j + 1:k - 1])
                    j = k
                elif ch == "\\" and j + 1 < n:
                    delim.append(src[j + 1])
                    j += 2
                else:
                    delim.append(ch)
                    j += 1
            i = j
            # A HERE-STRING LANDS HERE WITH AN EMPTY DELIMITER and queues nothing, which is
            # right: `<<<` is `<<` followed by a `<`, and `<` is a word break, so the
            # delimiter scan stops immediately. There WAS an explicit `<<<` arm above this
            # one and it is deleted: reverting it changed not one token anywhere in this
            # corpus, because this path already produced the same result for every
            # here-string in it. A branch whose removal reds nothing is an assertion about
            # nothing, which is the rule this kit's own gate legs are held to.
            if delim:
                heredocs.append(("".join(delim), strip, line))
            at_word_start = True
            continue

        if c in ";&|<>":
            add_word()
            i += 1
            at_word_start = True
            continue

        add_char(c)
        i += 1
        at_word_start = False

    add_word()
    if dq:
        raise SyntaxError(f'unterminated " quote opened at line {dq_line}')
    if heredocs:
        raise SyntaxError(
            f"unterminated heredoc <<{heredocs[0][0]} opened at line {heredocs[0][2]}")
    return toks


def parse_shell_defs(src: str):
    """Shell function definitions as `(functions, types, imports)`, from a TOKENIZER not a regex.

    FOUR RECOGNISED FORMS, and no fifth: the POSIX `name() { … }`, the bash `function name { … }`,
    the combined `function name() { … }`, and the subshell body `name() ( … )`. The body may open on
    a later line than the name. A name is `[A-Za-z_][A-Za-z0-9_]*`, which is the same class the
    naive same-line regex accepted, so the two readings are comparable name-for-name. Each hit is
    `(name, line)` — the line the NAME is on.

    TYPES AND IMPORTS ARE EMPTY LISTS, and that is a refusal rather than an omission: shell has
    neither in any sense this kit grades, so the declaration carries no `sh` type cell and P2 grades
    nothing here. The three-list shape is `extract`'s contract and is unchanged.

    THREE REFUSALS, each of which this header owes you because two of them have no runtime behaviour
    to observe:

    1. A file it CANNOT TOKENIZE raises `SyntaxError` naming the construct and the line it opened
       on — an unterminated quote, heredoc or `${`. It never returns an empty or partial list for
       such a file. `scan_corpus` catches that and yields a named refusal, exactly as it does for an
       unparseable Python file, because an unreadable file under an armed declaration is a broken
       corpus and `[]` would launder it into a clean run.
    2. A definition constructed by `eval`, or arriving by `source`/`.` of another file, is NOT
       found. There is no definition SITE to grade: the name exists only after a runtime expansion.
       A sourced file's own definitions are extracted where they are written, which is the right
       answer; this repo carries thirty such constructions and every one of them is out of reach of
       any static extractor, so pretending otherwise would be the green-by-absence claim this parser
       exists to refuse.
    3. A definition inside a HEREDOC BODY is not a definition and is not returned. This is the one
       refusal with a confirmed live instance: the hooks kit's `agent-cap.test.sh` embeds a JavaScript
       `function f() { … }` inside a `<<'EOF'` body, which the naive same-line pattern reports as a
       shell function.

    NOT AN INTERPRETER. It tokenizes and locates; it never evaluates, never expands and never runs
    what it reads. TOOL-aSurfacedLexicon-14.
    """
    toks = scan_shell_tokens(src)
    out, k, m = [], 0, len(toks)
    while k < m:
        kind, text, ln = toks[k]
        if kind == "word" and text == "function" and k + 1 < m and toks[k + 1][0] == "word" \
                and _SH_NAME.match(toks[k + 1][1]):
            j = k + 2
            if j + 1 < m and toks[j][1] == "(" and toks[j + 1][1] == ")":
                j += 2
            if j < m and toks[j][0] == "op" and toks[j][1] in "{(":
                out.append((toks[k + 1][1], toks[k + 1][2]))
                k = j + 1
                continue
        elif kind == "word" and _SH_NAME.match(text) and k + 2 < m \
                and toks[k + 1][1] == "(" and toks[k + 2][1] == ")":
            j = k + 3
            if j < m and toks[j][0] == "op" and toks[j][1] in "{(":
                out.append((text, ln))
                k = j + 1
                continue
        k += 1
    return out, [], []


# ---- TOOL-aGradedDialect-3: the TypeScript reader -----------------------------------------

#: A TypeScript identifier, as this locator will accept one. Deliberately the SAME character class
#: the shipped `js-regex` set accepts, so the two readings of one population are comparable
#: name-for-name and the only difference between them is what the tokenizer could see.
_TS_NAME = re.compile(r"^[A-Za-z_$][A-Za-z0-9_$]*$")

#: Words after which a `/` opens a REGEX and a `<` opens a JSX element, because each of them ENDS a
#: statement or an operator rather than an expression. Every other word ends an expression, so the
#: slash divides and the angle compares. This is the ported shape of `scan_shell_tokens`'s
#: `at_word_start`: a state the lexer already knows, never a lookahead over the text.
_TS_EXPR_WORDS = frozenset(
    "return typeof instanceof in of new delete void yield await throw case do else extends".split())

#: The bracket openers `read_ts_type_end` counts. Not a general operator table — the tokenizer
#: dispatches on characters directly and this is the one place a depth walk needs the set.
_TS_OPENERS = ("(", "[", "{", "<")


def check_ts_generic(src: str, i: int) -> bool:
    """A `<` at expression position in a `.tsx` source: a GENERIC parameter list, not a JSX element?

    TypeScript's own tie-break, and the only lookahead in this tokenizer: in a `.tsx` file `<T>` is
    an element and `<T,>` and `<T extends X>` are type parameters, so the construct is decided by
    what follows the NAME and by nothing else. Written down rather than left to the `.ts` reader
    because a `.tsx` file carrying `const pick = <T,>(x) => x` would otherwise scan as an element
    whose closing tag never arrives, and REFUSE the whole file.
    """
    n = len(src)
    j = i + 1
    while j < n and src[j] in " \t\n":
        j += 1
    k = j
    while k < n and (src[k].isalnum() or src[k] in "_$"):
        k += 1
    if k == j:
        return False
    while k < n and src[k] in " \t\n":
        k += 1
    return src[k:k + 1] == "," or src[k:k + 8] == "extends "


def scan_ts_tokens(src: str, jsx: bool = False) -> list:
    """`[(kind, text, line)]` for TypeScript source: every CODE token, and nothing that is not code.

    `kind` is `word` or `op`. `op` is one of `( ) { } [ ] = : ; , < > =>` and `@` — the punctuation
    `parse_ts_defs` needs. Every other operator the language reads as syntax is consumed as a word
    break and emitted as nothing, because no definition form below needs it.

    WHAT IT CONSUMES WITHOUT EMITTING, which is the whole reason this is not a regex: single- and
    double-quoted strings, a template literal's TEXT, `//` and `/* */` comments, a regex literal,
    and JSX text children. A `function` keyword inside a template literal or a JSX text child is
    DATA, and no same-line pattern can tell it from code — this corpus carries one such file, a
    Facebook pixel snippet embedded in a `.tsx` template literal.

    THE STATE IS A STACK, not a set of flags, because the constructs nest: a template literal holds
    a `${}` substitution which may hold another template literal. `/` and `<` are decided by the
    previously LEXED token, never by a lookahead pattern — with the single exception
    `check_ts_generic` names and argues.

    TWO SPANS ARE TOKENIZED AND SUPPRESSED: a template `${…}` substitution and a JSX `{…}`
    expression container. They are lexed so the state machine stays honest about nesting and
    terminators, and no token from inside them is emitted, so `parse_ts_defs` returns no definition
    from either. Spec §8 F2 prices that refusal against the conformance floor rather than arguing
    it away.

    RAISES `SyntaxError` on a source it cannot tokenize, naming the construct and the line it opened
    on. Never a partial list and never an empty one: `scan_corpus` turns that into a named refusal,
    and returning `[]` would launder a broken file into a clean run exactly as it would for
    `_python_defs`.
    """
    toks: list = []
    stack = ["code"]
    opens: list = []
    suppress = 0
    expr_end = False
    i, n, line = 0, len(src), 1

    def add_token(kind: str, text: str) -> None:
        """Emit one token, unless we are inside a suppressed span."""
        if not suppress:
            toks.append((kind, text, line))

    def read_string(j: int, q: str) -> int:
        """The index just past the `q` that closes a string opened before `j`."""
        while j < n:
            c2 = src[j]
            if c2 == "\\":
                j += 2
                continue
            if c2 == "\n":
                break
            if c2 == q:
                return j + 1
            j += 1
        raise SyntaxError(f"unterminated {q} string opened at line {line}")

    def read_regex(j: int) -> int:
        """The index just past the flags of a regex literal opened before `j`."""
        cls = False
        while j < n:
            c2 = src[j]
            if c2 == "\\":
                j += 2
                continue
            if c2 == "\n":
                break
            if c2 == "[":
                cls = True
            elif c2 == "]":
                cls = False
            elif c2 == "/" and not cls:
                j += 1
                while j < n and src[j].isalpha():
                    j += 1
                return j
            j += 1
        raise SyntaxError(f"unterminated regex literal opened at line {line}")

    while i < n:
        top = stack[-1]
        c = src[i]

        # --- a template literal's TEXT ---------------------------------------------------------
        if top == "tmpl":
            if c == "\\":
                line += src.count("\n", i, min(i + 2, n))
                i += 2
                continue
            if c == "`":
                stack.pop()
                opens.pop()
                expr_end = True
                i += 1
                continue
            if src.startswith("${", i):
                stack.append("tmplcode")
                opens.append(("${ substitution", line))
                suppress += 1
                expr_end = False
                i += 2
                continue
            if c == "\n":
                line += 1
            i += 1
            continue

        # --- JSX text children ------------------------------------------------------------------
        if top == "jsxchildren":
            if src.startswith("</", i):
                j = src.find(">", i)
                if j < 0:
                    raise SyntaxError(
                        f"unterminated JSX element opened at line {opens[-1][1]}")
                line += src.count("\n", i, j)
                i = j + 1
                stack.pop()
                opens.pop()
                expr_end = True
                continue
            if c == "<":
                stack.append("jsxtag")
                opens.append(("JSX element", line))
                i += 1
                continue
            if c == "{":
                stack.append("jsxexpr")
                opens.append(("JSX expression", line))
                suppress += 1
                expr_end = False
                i += 1
                continue
            if c == "\n":
                line += 1
            i += 1
            continue

        # --- inside a JSX opening tag, where the attributes live --------------------------------
        if top == "jsxtag":
            if src.startswith("/>", i):
                stack.pop()
                opens.pop()
                expr_end = True
                i += 2
                continue
            if c == ">":
                stack[-1] = "jsxchildren"
                i += 1
                continue
            if c in "\"'":
                j = read_string(i + 1, c)
                line += src.count("\n", i, j)
                i = j
                continue
            if c == "{":
                stack.append("jsxexpr")
                opens.append(("JSX expression", line))
                suppress += 1
                expr_end = False
                i += 1
                continue
            if c == "\n":
                line += 1
            i += 1
            continue

        # --- code -------------------------------------------------------------------------------
        if c == "\n":
            line += 1
            i += 1
            continue
        if c in " \t\r":
            i += 1
            continue
        if src.startswith("//", i):
            j = src.find("\n", i)
            i = n if j < 0 else j
            continue
        if src.startswith("/*", i):
            j = src.find("*/", i + 2)
            if j < 0:
                raise SyntaxError(f"unterminated /* comment opened at line {line}")
            line += src.count("\n", i, j)
            i = j + 2
            continue
        if c in "\"'":
            j = read_string(i + 1, c)
            line += src.count("\n", i, j)
            i = j
            expr_end = True
            continue
        if c == "`":
            stack.append("tmpl")
            opens.append(("template literal", line))
            i += 1
            continue
        if c == "/":
            if not expr_end:
                j = read_regex(i + 1)
                line += src.count("\n", i, j)
                i = j
                expr_end = True
                continue
            i += 1
            expr_end = False
            continue
        if c == "<":
            if jsx and not expr_end and not check_ts_generic(src, i):
                stack.append("jsxtag")
                opens.append(("JSX element", line))
                i += 1
                continue
            add_token("op", "<")
            i += 1
            expr_end = False
            continue
        if c == "{":
            stack.append("brace")
            opens.append(("{ block", line))
            add_token("op", "{")
            i += 1
            expr_end = False
            continue
        if c == "}":
            if top == "tmplcode" or top == "jsxexpr":
                stack.pop()
                opens.pop()
                suppress -= 1
            else:
                # An unbalanced `}` at the base of the stack is EMITTED rather than refused; only a
                # frame that failed to close is a refusal, and it is raised after the loop.
                if top == "brace":
                    stack.pop()
                    opens.pop()
                add_token("op", "}")
                expr_end = True
            i += 1
            continue
        if src.startswith("=>", i):
            add_token("op", "=>")
            i += 2
            expr_end = False
            continue
        if c in "()[]=:;,>@":
            add_token("op", c)
            i += 1
            expr_end = c in ")]"
            continue
        if c.isalnum() or c in "_$":
            j = i
            while j < n and (src[j].isalnum() or src[j] in "_$"):
                j += 1
            text = src[i:j]
            add_token("word", text)
            expr_end = text not in _TS_EXPR_WORDS
            i = j
            continue
        i += 1
        expr_end = False

    if len(stack) > 1:
        construct, ln = opens[-1]
        raise SyntaxError(f"unterminated {construct} opened at line {ln}")
    return toks


def read_ts_angle_end(toks: list, k: int):
    """The index just past the `>` closing a `<` at `k`, or `None` when that `<` compares.

    Brackets inside the run are counted so a heritage clause's type literals — `extends
    Component<{ a: X }, { b: Y }>` — do not end it, and an unbalanced closer or a `;` at angle
    depth ends the attempt rather than swallowing the rest of the file.
    """
    angle, inner, m, j = 0, 0, len(toks), k
    while j < m and j - k < 400:
        kind, text, _ln = toks[j]
        if kind == "op":
            if text in ("(", "[", "{"):
                inner += 1
            elif text in (")", "]", "}"):
                inner -= 1
                if inner < 0:
                    return None
            elif inner == 0:
                if text == "<":
                    angle += 1
                elif text == ">":
                    angle -= 1
                    if angle == 0:
                        return j + 1
                elif text == ";":
                    return None
        j += 1
    return None


def read_ts_paren_end(toks: list, k: int):
    """The index just past the `)` closing the `(` at `k`, or `None`."""
    depth, m, j = 0, len(toks), k
    while j < m:
        kind, text, _ln = toks[j]
        if kind == "op":
            if text == "(":
                depth += 1
            elif text == ")":
                depth -= 1
                if depth == 0:
                    return j + 1
        j += 1
    return None


def read_ts_brace_end(toks: list, k: int) -> int:
    """The index just past the `}` closing the `{` at `k`; the end of the list when none does."""
    depth, m, j = 0, len(toks), k
    while j < m:
        kind, text, _ln = toks[j]
        if kind == "op":
            if text == "{":
                depth += 1
            elif text == "}":
                depth -= 1
                if depth == 0:
                    return j + 1
        j += 1
    return m


def read_ts_type_end(toks: list, k: int, stop: str):
    """The index of the first `stop` op at bracket depth 0 from `k`, or `None`.

    This is how a TYPE ANNOTATION is stepped over without parsing type grammar: the annotation ends
    at the token the caller names — `=` for a variable declaration, `=>` for an arrow's return type
    — and a `,`, `;` or unbalanced closer before it means there was no such annotation.

    A `=>` AT DEPTH 0 IS NOT AN END, and that is the one rule here worth writing down: a function
    TYPE is spelled `(t: Tone) => boolean`, so `let f: (t: Tone) => boolean = function (t) {…}`
    carries a fat arrow inside the annotation that precedes the `=` this walk is looking for.
    """
    depth, m, j = 0, len(toks), k
    while j < m:
        kind, text, _ln = toks[j]
        if kind == "op":
            if depth == 0 and text == stop:
                return j
            if text in _TS_OPENERS:
                depth += 1
            elif text in (")", "]", "}", ">"):
                depth -= 1
                if depth < 0:
                    return None
            elif depth == 0 and text in (";", ","):
                return None
        j += 1
    return None


def check_ts_arrow(toks: list, k: int) -> bool:
    """Does an arrow function or a function expression START at `k`?

    The four heads: `function`, `async` before any of these, `x =>`, `(params) =>` with an optional
    return-type annotation, and `<T,>(params) =>`.
    """
    m = len(toks)
    if k >= m:
        return False
    kind, text, _ln = toks[k]
    if kind == "word":
        if text == "async":
            return check_ts_arrow(toks, k + 1)
        if text == "function":
            return True
        return k + 1 < m and toks[k + 1][0] == "op" and toks[k + 1][1] == "=>"
    if text == "<":
        j = read_ts_angle_end(toks, k)
        return j is not None and check_ts_arrow(toks, j)
    if text == "(":
        j = read_ts_paren_end(toks, k)
        if j is None:
            return False
        if j < m and toks[j][0] == "op" and toks[j][1] == ":":
            e = read_ts_type_end(toks, j + 1, "=>")
            if e is None:
                return False
            j = e
        return j < m and toks[j][0] == "op" and toks[j][1] == "=>"
    return False


def check_ts_body(toks: list, k: int) -> bool:
    """Does the callable whose parameter list opens at `k` carry a BODY?

    An OVERLOAD SIGNATURE is a declaration terminated by `;` with no body, and TypeScript reports
    the implementation rather than the signatures — so returning one would be a definition site the
    oracle does not count. The scan steps over a return-type annotation on the way, including one
    that is itself a type literal: `function f(): { a: string } {` reaches its body brace because
    the type literal's own `{` is the first at depth 0 either way, and the `;` inside it is not.
    """
    j = read_ts_paren_end(toks, k)
    if j is None:
        return False
    depth, m = 0, len(toks)
    while j < m:
        kind, text, _ln = toks[j]
        if kind == "op":
            if depth == 0 and text == "{":
                return True
            if depth == 0 and text in (";", ")", "}", ","):
                return False
            if text in ("(", "[", "<"):
                depth += 1
            elif text in (")", "]", ">"):
                depth -= 1
        j += 1
    return False


def read_ts_block_kind(prev, cur: str, pend) -> str:
    """Which KIND of block a `{` opens: `statement`, `class`, `object` or `type`.

    THE WHOLE REASON A REGEX CANNOT DO THIS. A property signature in an interface and a property
    assignment in an object literal are spelled identically — `render: (el: HTMLElement) => string`
    is a function TYPE in one and a function DEFINITION in the other — and only the enclosing block
    tells them apart. This corpus carries the case: `interface Window` declares two such properties
    and the oracle counts ZERO functions in it.

    `pend` is the kind a `class`, `interface`, `enum` or `type` header already decided; `cur` is the
    enclosing block, which is what routes a `:` to a nested type literal inside a type and to a
    nested object literal inside an object.
    """
    if pend:
        return pend
    if prev is None:
        return "statement"
    pk, pt, _ln = prev
    if pk == "op":
        if pt == ":":
            return "object" if cur == "object" else "type"
        if pt in ("=", "(", ",", "[", "<"):
            return "type" if cur == "type" else "object"
        return "statement"
    if pt in ("as", "satisfies", "extends", "implements"):
        return "type"
    if pt in ("return", "case"):
        return "object"
    return "statement"


def parse_ts_defs(src: str, jsx: bool = False):
    """TypeScript definitions as `(functions, types, imports)`, from a TOKENIZER not a regex.

    THE RECOGNISED FORMS, mirroring the oracle's set so recall and precision are comparable form for
    form: `function <name>` including `export`, `export default`, `async` and generator forms; a
    class or object-literal METHOD and a `get` or `set` accessor, under the name the oracle records;
    `constructor`; a `const`, `let` or `var` bound to an arrow or a function expression; a property
    assignment or class property initialised to one. `class`, `interface`, `type` and `enum` are
    types. Each hit is `(name, line)` — the line the NAME is on, never its body's.

    `jsx` picks the LEXER, and the two extensions take two `PARSERS` ids for that reason: `.ts`
    lexes `<T>(x) => x` as a generic arrow and `.tsx` lexes `<T>` as an element, so one lexer mode
    necessarily mis-reads one of the two populations.

    SIX REFUSALS, and this header owes you every one of them because three have no runtime failure
    to stage:

    1. A source it CANNOT TOKENIZE raises `SyntaxError` naming the construct and the line it opened
       on: an unterminated string, template literal, `${ substitution`, `/* comment`, regex literal,
       `{ block` or JSX element. It never returns an empty or partial list for such a file.
       `scan_corpus` turns that into a named refusal, because an unreadable file under an armed
       declaration is a broken corpus and `[]` would launder it into a clean run.
    2. A definition written inside a template `${…}` substitution or a JSX `{…}` expression
       container is NOT returned. Those spans are tokenized and SUPPRESSED — the ported shape of
       `scan_shell_tokens`, which treats `${…}` and `$((…))` as opaque — and the cost is priced
       against the conformance floor rather than argued away. Spec §8 F2.
    3. An OVERLOAD SIGNATURE — a `function` declaration terminated by `;` with no body — is not a
       definition. TypeScript reports the implementation, and so does this.
    4. A definition constructed by `eval`, by a decorator, or arriving through an `import` is NOT
       found. There is no definition SITE to grade: the name exists only after a runtime step.
    5. A COMPUTED or string-literal property key — `[k]: () => …`, `"on-change": () => …` — is not
       returned. The locator names a definition by its identifier and there is none to name; the
       oracle drops computed keys before they reach a record for the same reason.
    6. IMPORTS ARE AN EMPTY LIST, and that is a refusal rather than an omission: the corpus walk
       discards the third element, the only import consumer reads this kit's own Python directly,
       and a populated list would be an ungraded population with a fixture obligation. The
       three-list shape is `extract`'s contract and is unchanged. `parse_shell_defs` set the
       precedent for types.

    NOT AN INTERPRETER. It tokenizes and locates; it never resolves a type, walks a module graph,
    evaluates or runs what it reads. TOOL-aGradedDialect-3.
    """
    toks = scan_ts_tokens(src, jsx)
    funcs: list = []
    types_: list = []
    blocks = ["statement"]
    pend = None
    k, m = 0, len(toks)
    while k < m:
        kind, text, ln = toks[k]
        cur = blocks[-1]

        if kind == "op":
            if text == "<":
                # A balanced generic run is SKIPPED whole, so a type argument's own braces cannot
                # be read as a block. `read_ts_angle_end` returns None where the `<` compares.
                j = read_ts_angle_end(toks, k)
                k = j if j is not None else k + 1
                continue
            if text == "{":
                want = read_ts_block_kind(toks[k - 1] if k else None, cur, pend)
                pend = None
                if want == "type":
                    # A type carries no definition site, so it is stepped over whole rather than
                    # walked. That is what keeps an interface's property SIGNATURES out of `funcs`.
                    k = read_ts_brace_end(toks, k)
                    continue
                blocks.append(want)
                k += 1
                continue
            if text == "}":
                if len(blocks) > 1:
                    blocks.pop()
                k += 1
                continue
            if text == ";":
                pend = None
            k += 1
            continue

        nxt = toks[k + 1] if k + 1 < m else None
        nt = nxt[1] if nxt else ""

        if text == "function" and nxt and nxt[0] == "word" and _TS_NAME.match(nt):
            j = k + 2
            if j < m and toks[j][0] == "op" and toks[j][1] == "<":
                a = read_ts_angle_end(toks, j)
                j = a if a is not None else j
            if j < m and toks[j][0] == "op" and toks[j][1] == "(" and check_ts_body(toks, j):
                funcs.append((nt, nxt[2]))
            k += 1
            continue

        if text in ("class", "interface", "enum") and nxt and nxt[0] == "word" \
                and _TS_NAME.match(nt):
            types_.append((nt, nxt[2]))
            pend = "class" if text == "class" else "type"
            k += 2
            continue

        if text == "type" and nxt and nxt[0] == "word" and _TS_NAME.match(nt) \
                and k + 2 < m and toks[k + 2][0] == "op" and toks[k + 2][1] in ("=", "<"):
            types_.append((nt, nxt[2]))
            pend = "type"
            k += 2
            continue

        if cur == "statement" and text in ("const", "let", "var") and nxt \
                and nxt[0] == "word" and _TS_NAME.match(nt):
            j = k + 2
            if j < m and toks[j][0] == "op" and toks[j][1] == ":":
                e = read_ts_type_end(toks, j + 1, "=")
                j = e if e is not None else m
            if j < m and toks[j][0] == "op" and toks[j][1] == "=" \
                    and check_ts_arrow(toks, j + 1):
                funcs.append((nt, nxt[2]))
            k += 1
            continue

        if cur in ("object", "class") and _TS_NAME.match(text):
            if nt == "(" and nxt[0] == "op" and check_ts_body(toks, k + 1):
                funcs.append((text, ln))
            elif cur == "object" and nt == ":" and nxt[0] == "op" \
                    and check_ts_arrow(toks, k + 2):
                funcs.append((text, ln))
            elif cur == "class" and nt == "=" and nxt[0] == "op" \
                    and check_ts_arrow(toks, k + 2):
                funcs.append((text, ln))
        k += 1
    return funcs, types_, []


def parse_tsx_defs(src: str):
    """`parse_ts_defs` with JSX lexing on — the `.tsx` half of the pair. Its header is that one."""
    return parse_ts_defs(src, jsx=True)


#: The `parser`-mode extractors, keyed by the pattern-set id its `LANGS` row names — the third
#: extractor arm, beside `python-ast` and the `probe` sets. Keyed rather than branched on the
#: extension because `extract_text` is handed source TEXT and a mode, never a path: `drift-audit`
#: calls it against git blobs at two shas and has no file to look at. A `parser` row naming an id
#: that is not here is a REFUSAL in `scan_corpus`, never a silent fallthrough to Python.
#:
#: TWO IDS FOR ONE READER, and not one reader handed the extension: `extract_text` is given source
#: TEXT and a mode and never a path, and the two `.ts`/`.tsx` populations need two different lexer
#: modes — `<T>(x) => x` is a generic arrow in one and an element in the other, so one mode
#: necessarily mis-reads one of them. TOOL-aGradedDialect-3 §4.
PARSERS = {"python-ast": _python_defs, "shell-tokens": parse_shell_defs,
           "ts-tokens": parse_ts_defs, "tsx-tokens": parse_tsx_defs}


def resolve_pattern_sets(conf: dict) -> dict:
    """The SHIPPED sets with every declared `PATTERNS` row merged over them. A NEW mapping, always.

    NOTHING MUTATES `PATTERN_SETS`, and that is a contract rather than tidiness: `selftest.py`
    compares its frozen SENTINELS against that constant to prove every SHIPPED set has a fixture
    yielding a non-zero count, so a declared set folded into it would red the kit's own vacuity arm
    on any repo whose conf declares one. Shipped and resolved are two questions with two answers.

    THE MERGE IS PER KEY, not per set. A declared `js-regex.types` row replaces the shipped `types`
    list for `js-regex` and leaves its `functions` and `imports` standing. Replacement rather than
    append is what lets an adopter FIX a shipped regex, which is the case that motivates the block at
    all — and per-key rather than per-set is what stops fixing one part silently disarming the other
    two. The distinction is invisible on a declaration that only ever adds a NEW set, so the arm that
    guards it declares over the shipped one; every run also PRINTS the replaced keys, because a set
    weakened rather than emptied is otherwise inferred rather than seen.

    A row naming an UNSHIPPED set builds that set from empty parts, so a declaration arming only
    `functions` still answers the three-list contract `_probe_defs` reads.
    """
    out = {pid: dict(spec) for pid, spec in PATTERN_SETS.items()}
    for rowkey, rx in (conf.get("PATTERNS") or {}).items():
        pid, part = rowkey.split(".")
        out.setdefault(pid, {k: [] for k in PATTERN_PARTS})[part] = [rx]
    return out


def _probe_defs(src: str, pset: str, sets: dict | None = None):
    spec = (sets if sets is not None else PATTERN_SETS)[pset]

    def hits(key):
        out = []
        for rx in spec[key]:
            for m in rx.finditer(src):
                out.append((m.group(1), src.count("\n", 0, m.start()) + 1))
        return out

    return hits("functions"), hits("types"), hits("imports")


def resolve_extractor(mode: str, pset: str, sets: dict | None = None):
    """THE ARMEDNESS PREDICATE: the extractor a `(mode, pattern-set id)` pair reaches, or `None`.

    ONE HOME, because this question is asked at FOUR sites and an earlier revision of the spec named
    only the two that DISPATCH — `extract_text` and the refusal in `scan_corpus`. The other two
    REPORT: the coverage fraction and `--expand`'s armed-extension tally each decided armedness for
    themselves, so a `probe` row whose id names a parser would have been extracted by one half of a
    run and counted UNARMED by the other. The fraction and the extraction disagreeing about the same
    file is two answers to one question inside one run. TOOL-aGradedDialect-3 §8 F1.

    THE PATTERN-SET ID SELECTS THE READER AND THE MODE TOKEN CARRIES ONLY THE STANDING, which is
    what makes a tokenizer-shaped reader reachable under `probe` at all. Before this, `probe`
    reached `PATTERN_SETS` alone, so a reader that MISSED its conformance floor — the honest `probe`
    outcome — had nowhere to run, and the rule that whatever ships declares `parser` or `probe` was
    mechanically false for half of its own vocabulary. A new mode TOKEN was the other shape and the
    engine's own comment refuses it: `LANG_MODE_RANK` reads an unknown mode as absent, so a
    strengthening edit would fire a weakening finding.

    `dark` reaches nothing by declaration, and a `parser` row naming an unshipped id reaches nothing
    by fact; `scan_corpus` tells those two apart in its message and this predicate does not need to.
    """
    if mode not in ("parser", "probe"):
        return None
    if pset in PARSERS:
        return PARSERS[pset]
    if mode == "probe" and pset in (PATTERN_SETS if sets is None else sets):
        return _probe_defs
    return None


def extract_text(src: str, mode: str, pset: str, *, sets: dict | None = None):
    """`(functions, types, imports)` for SOURCE TEXT, or `None` when the mode declares no extractor.

    Split out of `extract` so a caller holding BYTES rather than a path uses the SAME extractor.
    `drift-audit`'s marginal-offense-rate signal derives its two operands from git blobs at two shas
    and never writes a tree; a second implementation there would be the
    `second-implementation-is-not-a-second-opinion` class inside the one instrument whose entire
    value is that both of its operands come from one extractor. TOOL-dScaffoldedMirror-7 S4.

    `sets` IS KEYWORD-ONLY AND DEFAULTS TO THE SHIPPED CONSTANT, which is the whole shape of the
    change TOOL-aSurfacedLexicon-9 was allowed to make here. The positional contract is frozen —
    `drift_report.py` calls both of these positionally against git blobs — so the resolution arrives
    beside it rather than inside it, and an adopter who never passes one is on exactly the previous
    behaviour by the default.
    """
    if mode == "dark":
        return None
    # THE ONE DISPATCH, through the ONE armedness predicate. It is keyed on the pattern-set id
    # rather than branched a second time on `mode`: `parser` already means "a real parse", and
    # which parse is what the set id has always said. TOOL-aSurfacedLexicon-14, widened to reach
    # the same readers under `probe` by TOOL-aGradedDialect-3 §8 F1.
    reader = resolve_extractor(mode, pset, sets)
    if reader is None:
        # UNCHANGED FAILURE SHAPE. `scan_corpus` refuses this pair by name one line before it could
        # ever get here, so reaching this is a direct caller passing a pair no reader answers —
        # which used to raise `KeyError(pset)` out of `PARSERS[pset]` or out of `_probe_defs`, and
        # still does. Returning an empty triple would launder an unshipped id into a clean run.
        raise KeyError(pset)
    if reader is _probe_defs:
        return _probe_defs(src, pset, sets)
    return reader(src)


def extract(path: Path, mode: str, pset: str, *, sets: dict | None = None):
    """`(functions, types, imports)` for one file, or `None` when the mode declares no extractor."""
    if mode == "dark":
        return None
    return extract_text(path.read_text(encoding="utf-8", errors="replace"), mode, pset, sets=sets)


def scan_corpus(root: Path, declared: dict, sets: dict | None = None):
    """THE corpus walk. Yields `(rel, ext, defs, problem)` for every TRACKED file, in `git ls-files`
    order. `defs` is `extract`'s `(functions, types, imports)` and is set only for an ARMED file;
    `problem` is a refusal text; an unarmed file carries neither.

    THERE WERE FIVE OF THESE, and they re-derived the same four decisions separately: which
    extensions are armed, whether a declared pattern set actually ships, what `extract` returns, and
    what an extraction FAILURE means. The last one is the divergence that mattered — `run()` turned a
    `SyntaxError` into a named refusal while `run_probe` and both `scaffold_lexicon.py` walks
    swallowed it, so one unparseable file was a gate failure in one reader and invisible in three.
    Decided here, once, and decided `run()`'s way: a refusal, never a silent skip.

    IT YIELDS THE UNARMED FILES TOO, and that is not generosity. Every caller needs the whole tracked
    population for something the armed subset cannot answer — the UNDECLARED EXTENSIONS refusal, the
    DEAD PROBE "the corpus contains this extension" test, the coverage denominator, the scaffold's
    `LANGS` seed. A generator that yielded only armed files would leave each of them calling
    `tracked_files` beside it, which is the second walk this function exists to delete.

    ONE-SHOT, like any generator. A caller that reads the population more than once materialises it
    with `list(...)`; that is still one walk, and it is the only shape in which `tracked_files` and
    `extract` have exactly one call site each in this kit.
    """
    # THE RESOLVED SETS, not the shipped constant — and the refusal below is why every caller has to
    # pass them. A set an adopter declared through `PATTERNS:` was refused HERE, one line before the
    # DEAD PROBE arm and the coverage fraction could see the extension at all, so a declared language
    # could never be graded and never be reported inert either. TOOL-aSurfacedLexicon-9.
    sets = sets if sets is not None else PATTERN_SETS
    for rel in tracked_files(root):
        ext = ext_of(rel)
        pset, mode = declared.get(ext, ("", "dark"))
        if mode == "dark":
            yield rel, ext, None, None
            continue
        # THE ARMEDNESS PREDICATE, asked ONCE and asked of `resolve_extractor` like the other three
        # sites. The two refusal MESSAGES stay apart because they name different repairs: a
        # `PATTERNS:` row cannot declare a parser, so an unshipped parser id is answered with the
        # shipped list rather than with a row an adopter could write. `parser` used to ignore its
        # set id entirely and always run the Python one, which was harmless while one parser shipped
        # and is a silent mis-extraction now that four do.
        if resolve_extractor(mode, pset, sets) is None:
            if mode == "parser":
                yield rel, ext, None, (f"LANGS declares parser {pset!r} for .{ext}, which this kit "
                                       f"does not ship; the parsers are "
                                       f"{' '.join(sorted(PARSERS))}")
            else:
                yield rel, ext, None, (f"LANGS declares pattern set {pset!r} for .{ext}, which this "
                                       f"kit does not ship and no PATTERNS: row declares")
            continue
        try:
            defs = extract(root / rel, mode, pset, sets=sets)
        except SyntaxError as exc:
            yield rel, ext, None, f"{rel}: declared `{mode}` but does not parse: {exc}"
            continue
        except OSError as exc:
            # SEPARATE FROM THE PARSE FAILURE, and named separately. `run_brief` caught the pair and
            # reported both as "does not parse", which is a true refusal under a false reason for
            # half of them. An unreadable file is not an unparseable one.
            yield rel, ext, None, f"{rel}: declared `{mode}` but cannot be read as source: {exc}"
            continue
        yield rel, ext, defs, None


def load_waivers(kit: Path, kind: str) -> dict[str, str]:
    """`{matched-text: reason}`. Absent file means no waivers, which is a legal state and not a
    refusal — a kit that demanded a waiver file could not be adopted into a clean tree."""
    f = kit / WAIVER_FILES[kind]
    out: dict[str, str] = {}
    if not f.exists():
        return out
    for raw in f.read_text(encoding="utf-8").splitlines():
        s = raw.strip()
        if not s or s.startswith("#"):
            continue
        parts = s.split(None, 1)
        out[parts[0]] = parts[1].strip() if len(parts) > 1 else ""
    return out


#: Siblings this engine may name in an import and must nevertheless survive WITHOUT. Exactly one,
#: and it is named rather than inferred: an import outside this tuple is still a hard refusal, so
#: this is a DECLARED exception and not a hole in the rule.
#:
#: WHY IT EXISTS. `--expand` reads the anti-mirror closure out of `scaffold_lexicon.py` rather than
#: copying it, which is the whole point of the mode; but the kit deliberately supports an adopter who
#: took the engine without the scaffolder, and the scaffold guard's absent-file branch REPORTS for
#: exactly that reason. Without this line the same adopter's `--check` reds on a dependency they
#: cannot satisfy, which is the red-nobody-can-fix that branch was written to avoid.
#:
#: WHAT IT DOES NOT BUY, and this is the load-bearing half: it says nothing about HOW the import is
#: written. A module-level `import scaffold_lexicon` would pass this list and then break the engine
#: at import time for that same adopter. The property that actually holds is armed at RUNTIME rather
#: than asserted here — one arm runs `--check` against a kit copy with the file deleted and requires
#: green, another runs `--expand` there and requires a named report rather than a traceback. Adding a
#: name here without arming both is how this tuple becomes the hole it is written not to be.
OPTIONAL_SIBLINGS = ("scaffold_lexicon",)


def check_self_containment(kit_dir: Path = Path(__file__).resolve().parent):
    """`(problems, modules walked, imports judged)` — the ONE constraint the deleted P3 really held.

    THE RULE, in full: every non-relative import in a `.py` file sitting beside this one names either
    a stdlib top-level module or another `.py` file in that same directory. It is STRONGER than the
    declared direction it replaces, which forbade one named neighbour, and it carries no hand-kept
    list, so there is nothing in it to rot. The constraint is real rather than decorative: this kit
    must install without its neighbours, which is why `subtokens.py` PORTS a `codebase-map` function
    instead of importing it.

    IT JUDGES IMPORT STATEMENTS, never file text. A whole-file text search for the neighbour's name
    is the `absence-assertion-over-whole-file-text` class and would fire on its own documentation:
    this docstring has to spell `codebase-map` to be readable at all.

    THE WALK ROOT IS A PARAMETER, and that is the one thing the design fixes about the code shape. A
    predicate that can only ever read its own installed directory has a liveness arm nobody can
    stage, which is the unfalsifiable shape one level up. It DEFAULTS to this file's own directory,
    derived rather than spelled, so it is independent of the prefix an adopter installed at — the
    property `resolve_self_path` already exists to buy.

    A ZERO-IMPORT WALK REDS, in the `DEAD PROBE` token this engine already spells and its neighbours
    already read. Zero offenders over zero imports is exactly the clean green a broken probe prints,
    and telling a satisfied predicate from one that was never asked is what the deleted `P3 NOT
    ARMED` refusal was bought to buy.

    `sys.stdlib_module_names` IS 3.10+, and that costs this kit nothing it had not already spent:
    `lexicon_conf.load_conf(path: str | Path)` is a PEP-604 annotation evaluated at definition time,
    so an adopter on 3.9 cannot import this engine at all today. No fallback is written here because
    a fallback would be code for a version that already cannot run the file it sits in.
    """
    kit = Path(kit_dir)
    mods = sorted(kit.glob("*.py"))
    siblings = {p.stem for p in mods} | set(OPTIONAL_SIBLINGS)
    problems: list[str] = []
    judged = 0
    for path in mods:
        try:
            _funcs, _types, imports = _python_defs(
                path.read_text(encoding="utf-8", errors="replace"))
        except (SyntaxError, OSError) as exc:
            problems.append(f"{path.name} sits beside this engine but its imports cannot be read, "
                            f"so self-containment is UNJUDGED for it: {exc}")
            continue
        judged += len(imports)
        # DEDUPED ON THE TOP-LEVEL NAME. `_python_defs` emits BOTH `map_lib` and `map_lib._STOPWORDS`
        # for `from map_lib import _STOPWORDS`, so an undeduped refusal names one offending statement
        # twice. The COUNT above is deliberately not deduped: it is the population the extractor
        # produced, and shrinking it here would report a smaller reach than was actually judged.
        seen: set[tuple[str, int]] = set()
        for target, lineno in imports:
            top = target.split(".", 1)[0]
            # An empty head is a LEADING DOT — a relative import, which cannot leave this directory
            # by construction and so needs no verdict.
            if not top or (top, lineno) in seen:
                continue
            seen.add((top, lineno))
            if top in siblings or top in sys.stdlib_module_names:
                continue
            problems.append(
                f"NOT SELF-CONTAINED — {path.name}:{lineno} imports `{top}`, which is neither a "
                f"stdlib module nor a `.py` file beside this engine. This kit must work in a tree "
                f"that took it alone: port what you need, as `subtokens.py` does, or drop the "
                f"dependency.")
    if not judged:
        problems.append(
            f"DEAD PROBE — the self-containment walk judged NO imports over {len(mods)} module(s) "
            f"in {kit}. Zero offenders over an empty population is what a broken probe prints, not "
            f"a predicate that is satisfied.")
    return problems, len(mods), judged


#: The conventions a CELLS row may declare and this walk may grade against. `dark` is a declared
#: refusal to grade and never a form; `dot` is a classifier form the messages use and is not
#: declarable, so neither belongs in a teeth figure.
GRADED_CONVENTIONS = tuple(c for c in CONVENTIONS if c != "dark")

def scan_function_names(scanned: list, root: Path, declared: dict, ext: str):
    """Every function definition the armed extractor produced for `ext`. Narrows nothing."""
    names = [(rel, line, name) for rel, e, got, _p in scanned if e == ext and got is not None
             for name, line in got[0]]
    return names, len(names)


def scan_type_names(scanned: list, root: Path, declared: dict, ext: str):
    """Every type definition the armed extractor produced for `ext`. Narrows nothing."""
    names = [(rel, line, name) for rel, e, got, _p in scanned if e == ext and got is not None
             for name, line in got[1]]
    return names, len(names)


def scan_file_stems(scanned: list, root: Path, declared: dict, ext: str):
    """The basename stem of every TRACKED file of `ext`, armed or not. Narrows nothing."""
    names = [(rel, 0, read_stem(rel.rsplit("/", 1)[-1])) for rel, e, _g, _p in scanned if e == ext]
    return names, len(names)


def extract_bound_names(target):
    """The `ast.Name` nodes an assignment TARGET binds, through `Tuple`, `List` and `Starred` only.

    A subscript or attribute target binds no module constant — `d[k] = v` names nothing this kit
    can grade — and counting the `d` underneath it inflates the denominator by exactly those
    targets. That gap is 13 names on this repo's own corpus and it is the entire difference between
    two readings a reader would both describe as "every module-body target", which is why the rule
    is written down here rather than left to whoever next edits the walk.
    """
    import ast

    if isinstance(target, ast.Name):
        yield target
    elif isinstance(target, (ast.Tuple, ast.List)):
        for elt in target.elts:
            yield from extract_bound_names(elt)
    elif isinstance(target, ast.Starred):
        yield from extract_bound_names(target.value)


def scan_module_constants(scanned: list, root: Path, declared: dict, ext: str):
    """PUBLIC SIMPLE module-body assignments, narrowed from every module-body target.

    THE COUNTING RULE LIVES HERE AND NOWHERE ELSE, because three readings of "a module constant" are
    all defensible — every module-body target, simple single-`Name` targets, public ones — and only
    the third yields a clean zero. NO COUNT IS STATED HERE. All three move with every unit that
    binds a module-body name, and the three that were stated here were wrong within two units. The
    `py.constant` comment in `.lexicon.conf` records them, under a selftest arm that reds when they
    drift from what `--check` prints. Module BODY
    statements only, with no descent into a class or function body. Both `ast.Assign` and
    `ast.AnnAssign` count; dropping the annotated form moves all three readings by roughly a tenth.
    A bound name is whatever `extract_bound_names` binds. The DENOMINATOR is every name that rule
    binds, and the GRADED population narrows it to single-`Name` targets with no leading underscore,
    which is the reading this repo arms and the leading underscore is what correlates with mutable
    module state in this corpus.

    IT RE-READS THE FILES OF THIS ONE EXTENSION, which is the only second read in this engine and is
    a deliberate trade: the corpus walk keeps definitions rather than source, and holding fifteen
    hundred files of text in memory to serve one declared cell is the worse half of that bargain.
    It runs only for a `constant` cell a `CELLS` row declares.

    A NON-PYTHON EXTENSION RETURNS AN EMPTY POPULATION rather than guessing, because `ast` cannot
    read one. That empty population is a `DEAD CELL` refusal one caller up, which is the honest
    outcome: a `constant` cell declared for a language this rule cannot select in REDS instead of
    reporting a clean zero at it forever.
    """
    import ast

    if (declared.get(ext) or ("", "dark"))[0] != "python-ast":
        return [], 0
    names: list[tuple[str, int, str]] = []
    targets = 0
    for rel, e, got, _p in scanned:
        if e != ext or got is None:
            continue
        tree = ast.parse((root / rel).read_text(encoding="utf-8", errors="replace"))
        for stmt in tree.body:
            if isinstance(stmt, ast.Assign):
                bound = [n for t in stmt.targets for n in extract_bound_names(t)]
                simple = stmt.targets
            elif isinstance(stmt, ast.AnnAssign):
                bound = list(extract_bound_names(stmt.target))
                simple = [stmt.target]
            else:
                continue
            targets += len(bound)
            if len(simple) == 1 and isinstance(simple[0], ast.Name) \
                    and not simple[0].id.startswith("_"):
                names.append((rel, stmt.lineno, simple[0].id))
    return names, targets


def extract_decorators(scanned: list, root: Path, declared: dict, ext: str) -> dict:
    """`{(path, lineno): {decorator-name, …}}` for a `python-ast` extension, `{}` for every other.

    THE ADDITIVE ACCESSOR (TOOL-aSurfacedLexicon-13 S3), and it is a separate walk rather than a
    third element on each function entry ON PURPOSE. `extract` and `extract_text` return
    `(functions, types, imports)` with each function entry a `(name, lineno)` PAIR, and two call
    sites in ANOTHER kit unpack that pair positionally — `for nm, _ln in got[0]` in
    the drift-audit kit's `drift_report.py`, both of them OUTSIDE any catch naming `ValueError`.
    Widening the pair therefore raises uncaught on `drift-audit records`, a leg carrying no guard,
    which means it reds every bar rather than degrading quietly. The shape is frozen; this accessor
    is how a decorator arrives without touching it, and this kit's own selftest asserts the arity so
    the break is caught here first.

    A DOTTED DECORATOR IS RECORDED BY ITS LAST SEGMENT, so `@app.route` is selectable as `route`. A
    selector literal carries no dot (`lexicon_conf._SEL_LIT_RE`) because a dotted literal would make
    the selector'd cell's own `PINS` row key unparseable.

    WHAT IT DOES NOT DO: a `parser` extension whose pattern set is not `python-ast` — `sh` under
    `shell-tokens` — returns `{}` here, because shell has no decorators to read. A decorator selector
    declared on one selects nothing and reds as a `DEAD CELL`, which is the honest outcome; the
    NON-parser modes are refused earlier and by name, in `lexicon_conf.check_declaration`.
    """
    import ast

    if (declared.get(ext) or ("", "dark"))[0] != "python-ast":
        return {}
    out: dict[tuple[str, int], set] = {}
    for rel, e, got, _p in scanned:
        if e != ext or got is None:
            continue
        # A SyntaxError cannot reach here: `scan_corpus` already ran the same parse over this file
        # and recorded a problem instead of yielding defs, so `got is None` is the unparseable case.
        tree = ast.parse((root / rel).read_text(encoding="utf-8", errors="replace"))
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                continue
            for dec in node.decorator_list:
                target = dec.func if isinstance(dec, ast.Call) else dec
                name = getattr(target, "attr", None) or getattr(target, "id", None)
                if name:
                    # `node.lineno` is the `def`/`class` line on every Python this kit runs on, which
                    # is the line `_python_defs` records — so these keys align with that population
                    # by construction rather than by an offset nobody re-checks.
                    out.setdefault((rel, node.lineno), set()).add(name)
    return out


def scan_routes(names: list, selectors: list, decorators: dict):
    """Route each name to at most ONE selector. Returns `(complement, {cell: names}, ambiguous)`.

    `selectors` is `[(cell, kind, literal)]` for ONE parent cell and `names` is that parent's whole
    population as `[(path, line, name)]`.

    A ROUTED NAME IS GRADED ONCE, against the selector's convention, and LEAVES the parent's
    population. The alternative — grading it against both — makes every routed name a guaranteed
    violation of one of the two cells, which is the failure mode the whole mechanism exists to avoid.

    A NAME MATCHING TWO SELECTORS IS REFUSED, not resolved by declaration order, and is graded by
    NEITHER: a naming gate whose verdict depends on which row the reader saw first is not a
    declaration. That refusal plus the `DEAD CELL` arm covers the overlapping-prefix pair completely
    — two selectors that CAN both match either do both match some name here, or one of them selected
    nothing and reds as a dead cell one layer up.
    """
    routed: dict[str, list] = {cell: [] for cell, _k, _l in selectors}
    complement: list = []
    ambiguous: list = []
    for entry in names:
        path, line, name = entry
        hit = [(cell, kind, lit) for cell, kind, lit in selectors
               if (name.startswith(lit) if kind == "prefix"
                   else lit in decorators.get((path, line), ()))]
        if len(hit) > 1:
            ambiguous.append((entry, [f"+{k}:{l}" for _c, k, l in hit]))
        elif hit:
            routed[hit[0][0]].append(entry)
        else:
            complement.append(entry)
    return complement, routed, ambiguous


#: `<surface>` -> `(selector, POPULATION RULE)`. The rule is a DECLARED string beside the selector
#: and is never derived from the selector's docstring: that would be a second carrier of one fact
#: with no gate comparing the two, which is the class this build exists to close. Every report row
#: prints its rule (TOOL-aSurfacedLexicon-6 S4), because a count with no rule beside it reads as
#: coverage when it is only a scope.
#:
#: A selector takes `(scanned, root, declared, ext)` and returns `(names, denominator)`, where
#: `names` is `[(path, line, graded string)]` and the DENOMINATOR is the wider population the rule
#: narrowed. Equal figures are legal and common — `py.function` grades every function it extracted —
#: and printing both is the only way a reader can see that `py.constant` does not.
#:
#: A surface in `lexicon_conf.SURFACES` with no row here is a REFUSAL in `measure_pass`, never a
#: silent skip: the cell would grade nothing while reporting a clean zero, which is the whole shape
#: this report exists to abolish.
CELL_POPULATION_RULES = {
    "function": (scan_function_names, "every extracted function definition"),
    "type": (scan_type_names, "every extracted type definition"),
    "file": (scan_file_stems, "every tracked file's basename stem"),
    "constant": (scan_module_constants, "public simple module-body assignments"),
}

#: The surface each PREDICATE's population is the population OF. `graded` is keyed on the predicate
#: because that is what P1 and P2 are; the cell matrix is keyed on the surface. This is the one
#: mapping between them, and it is what lets `UNDECLARED CELL` be DERIVED from the extracted
#: population rather than asserted beside it.
PREDICATE_SURFACES = {"verb": "function", "suffix": "type"}

#: ARMED by TOOL-aSurfacedLexicon-12, in the SAME commit as the full `CELLS` matrix in
#: `.lexicon.conf`, which is the only commit where both halves are true at once. It landed
#: REPORT-ONLY under TOOL-aSurfacedLexicon-6 because arming it at that build order would have fired
#: refusals against a declaration whose matrix did not exist yet — computed on every run, printed on
#: every run, refusing nothing. A matrix that lands with this left `False` ships an arm that reports
#: and can never refuse, which is the failure that whole unit was written against, so the two edits
#: are one change and this comment is where that is recorded.
#:
#: IT IS A KIT DEFAULT AND IT GRADES THE ADOPTER'S DECLARATION, not this repo's, so arming it here
#: reds every adopter that arms a language in `LANGS=` and then declares no cell for the surfaces
#: that language extracted. That is the state it exists to refuse and the refusal names each pair;
#: an adopter arming nothing extracts nothing and still passes. The cost is real and is paid on
#: purpose: the alternative is a report every run that no tree is ever obliged to act on.
UNDECLARED_CELL_ARMED = True


def measure_conventions(scanned: list, conf: dict, root: Path, declared: dict) -> dict:
    """Per declared CELLS row: the population, its RULE, the verdicts and the alternate-convention teeth.

    NO VERDICT AND NO PRINT, like everything else in the measurement half. It returns
    `(rows, problems)` — one dict per cell plus the refusals only the ROUTING can raise — and
    `check_pass` decides what any of it means. The problems come back rather than being appended to
    a list passed in, so this function still reads its inputs and returns its outputs, which is what
    lets the selftest call it directly.

    THE TEETH ARE NOT A NICETY. A cell that prints `0 violations` and nothing else is
    indistinguishable from a cell that CANNOT fail, which is the green-by-absence class one level up
    from the predicate itself. So every armed cell also reports how many of the SAME names each other
    convention would have failed — a figure that is zero everywhere only if the population really is
    ungradeable, and which no implementation can produce by accident.
    """
    cells = conf.get("CELLS") or {}
    pins = conf.get("PINS") or {}
    problems: list[str] = []
    parsed = {cell: parse_cell_key(cell) for cell in cells}

    # The selectors on each PARENT cell string, whether or not that parent has a row of its own. A
    # selector with no parent row is legal — its complement is then simply ungraded, and the
    # `UNDECLARED CELL` report is what names that — so this is keyed on the derived parent rather
    # than on the declared rows.
    selectors: dict[str, list] = {}
    for cell, (ext, surface, kind, lit) in parsed.items():
        if kind:
            selectors.setdefault(f"{ext}.{surface}", []).append((cell, kind, lit))

    # THE POPULATION RULE RUNS ONCE PER `(ext, surface)`, not once per row. `scan_module_constants`
    # re-reads every file of its extension, so a parent and three selectors would otherwise pay for
    # four walks of one population — and the four could not disagree only by accident.
    pops: dict[tuple[str, str], tuple] = {}
    for _cell, (ext, surface, _k, _l) in parsed.items():
        if (ext, surface) in pops:
            continue
        rule = CELL_POPULATION_RULES.get(surface)
        pops[(ext, surface)] = ((None, [], 0) if rule is None
                                else (rule, *rule[0](scanned, root, declared, ext)))

    # THE PARTITION. Every graded list below comes from here, so the parent's names and its
    # selectors' names cannot overlap by construction rather than by two call sites agreeing.
    graded_names: dict[str, list] = {}
    for (ext, surface), (_rule, names, _denominator) in pops.items():
        parent = f"{ext}.{surface}"
        sels = selectors.get(parent, [])
        if not sels:
            graded_names[parent] = names
            continue
        decorators = (extract_decorators(scanned, root, declared, ext)
                      if any(k == "decorator" for _c, k, _l in sels) else {})
        complement, routed, ambiguous = scan_routes(names, sels, decorators)
        graded_names[parent] = complement
        graded_names.update(routed)
        for (path, line, name), lits in ambiguous:
            problems.append(
                f"AMBIGUOUS SELECTOR — the name `{name}` at {path}:{line} matches "
                f"{len(lits)} selectors on cell `{parent}`: {' '.join(lits)}. Which convention it "
                f"is graded against would depend on which row the reader saw first, so it is graded "
                f"by NEITHER and the overlap is refused where it is written.")

    # THE ROW ORDER: each parent, then its own selectors beneath it, then any selector whose parent
    # declares no row. S5 — a routed subset printed anywhere else reads as a separate cell rather
    # than as a subtraction from the row above it, and the denominators only make sense as a pair.
    order: list[str] = []
    for cell, (ext, surface, kind, _l) in parsed.items():
        if kind:
            continue
        order.append(cell)
        order += [c for c, _k, _l2 in selectors.get(f"{ext}.{surface}", []) if c in cells]
    order += [c for c in cells if c not in order]

    out: dict[str, dict] = {}
    for cell in order:
        conv, _flags = cells[cell]
        ext, surface, _kind, _lit = parsed[cell]
        rule, _all_names, denominator = pops[(ext, surface)]
        names = graded_names.get(cell, [])
        row = {
            "convention": conv,
            # THE POPULATION ITSELF, not only its size. The cross-surface arm (closing review, the
            # one left-shift worth more than the seventeen fixes) asks `--suggest` about every name
            # this cell grades and asserts the two verbs agree; over VIOLATIONS alone it goes blind
            # on a clean cell, which is the population where a routing bug hides best.
            "names": names,
            "population": len(names),
            "denominator": denominator,
            "rule": rule[1] if rule is not None else None,
            "graded": rule is not None,
            "pin": pins.get(f"{cell}.conv", 0),
            "verdicts": [],
            "teeth": {},
        }
        if conv != "dark" and row["graded"]:
            for path, line, name in names:
                verdict, message = check_convention(name, conv)
                if verdict != "SATISFIED":
                    # THE NAME RIDES ALONG, and it is not decoration. The closing review's one
                    # cross-surface arm feeds every graded offence back through `--suggest` and
                    # asserts the two surfaces agree; without the name here that arm can only be
                    # written over P1/P2 offenders, which is the half of the population where the
                    # cell partition — the thing most likely to disagree — does not exist.
                    row["verdicts"].append((path, line, name, verdict, message))
            row["teeth"] = {
                alt: sum(1 for _p, _l, n in names if check_convention(n, alt)[0] != "SATISFIED")
                for alt in GRADED_CONVENTIONS if alt != conv
            }
        out[cell] = row
    return out, problems


def measure_pass(root: Path, kit: Path, conf: dict, declared: dict, clusters=None) -> dict:
    """THE MEASUREMENT HALF: one corpus walk, every refusal, and NO verdict.

    IT IS A SEPARATE FUNCTION SO THAT NO RETURN CAN SIT INSIDE IT. The file this replaces confessed
    three times to the same defect — a refusal appended BELOW the `measure_mode` return, therefore
    reachable from `--check` and not from `--measure`, therefore a mode that could not fail while its
    sibling redded the same tree by name. Each was repaired by hoisting one `.append` above the
    return, which fixes an instance and leaves the next author one `return` away from re-earning it.
    Here the mode branch cannot be written inside the measurement at all: `run()` gets this whole
    dict before it knows which mode it is in, so both modes read one refusal list by construction.

    Everything the two printers need is in the returned dict. Nothing here prints and nothing here
    decides.
    """
    verbs = conf.get("VERBS") or {}
    clusters = canon.CLUSTERS if clusters is None else clusters
    banned = tuple(t for t in (conf.get("BANNED_SUFFIXES") or "").split() if t)

    # RESOLVED ONCE, HERE, and handed down. Every reader below asks the same question of the same
    # mapping, which is what stops a language being armed for the extractor and unarmed for the
    # coverage fraction — two answers to one question, in the two halves of one run.
    sets = resolve_pattern_sets(conf)

    # THE ONE WALK, materialised because the population is read four times below — for the declared
    # surface, for the DEAD PROBE corpus test, for the coverage denominator and for the OK line.
    scanned = list(scan_corpus(root, declared, sets))
    files = [rel for rel, _e, _d, _p in scanned]
    scan_problems = [p for _r, _e, _d, p in scanned if p]

    problems: list[str] = []

    # --- S6 of TOOL-dScaffoldedMirror-8: the table's own shape --------------------------------
    #
    # These two run against the DECLARATION, not the corpus, and they are the only checks here that
    # do. A row with no negative cannot tell two verbs apart — `build` alone says nothing that
    # `create` does not — so the gate's whole message degrades to "not in the table", which names no
    # replacement and teaches nothing. The kit's own README calls a table without negative
    # definitions decoration, and this is that sentence made checkable.
    neg = build_negatives(conf)
    bare = sorted(v for v in verbs if not neg.get(v))
    if bare:
        problems.append(
            "VERBS rows carrying no negative definition (write `NOT \\`<token>\\`` into the gloss): "
            + ", ".join(bare) + ". A row that only says what it IS cannot draw a boundary, and the "
            "boundary is the whole product.")

    # A declared negative that is ALSO a row bans and permits one token at once. Satisfied today,
    # and it earns its place forward: it is what stops a later unit admitting a verb some other row
    # already banned — which is exactly how a closed table becomes a synonym list.
    contradicted = sorted({t for ts in neg.values() for t in ts} & set(verbs))
    if contradicted:
        problems.append(
            "VERBS declares as BANNED a token that is itself a row: " + ", ".join(contradicted)
            + ". One token cannot be both the verb to use and the verb not to use.")

    # --- the declaration surface -------------------------------------------------------------
    present = sorted({ext for _r, ext, _d, _p in scanned})
    missing = [e for e in present if e not in declared]
    if missing:
        problems.append("UNDECLARED EXTENSIONS (declare each in LANGS, `dark` if nothing extracts it): "
                        + ", ".join(missing))

    # --- the kit's own self-containment ------------------------------------------------------
    #
    # BELOW the NOT ADOPTED return, which keeps the inert-without-a-declaration contract intact, and
    # inside the measurement pass, which is where the second half of that sentence now lives: this
    # function holds no mode branch, so there is no return for an `.append` to land on the wrong side
    # of. Three refusals in this file's history did exactly that, one round apart.
    #
    # NOT A THIRD `P<n> … graded=` ROW. It is a refusal plus a population line: the kit ships two
    # DECLARED predicates, and a third row would say otherwise.
    self_problems, self_mods, self_imports = check_self_containment()
    problems.extend(self_problems)

    # --- S7 of TOOL-aSurfacedLexicon-11: the mirror may not return through the proposal path -----
    #
    # `scaffold_lexicon.py` proposes a table from the corpus. It may propose which CONCEPTS are
    # live; it may never propose the CANON those concepts are spelled from — a scaffold emitting a
    # `CANON:` block would hand an adopter an owner-declared overlay derived from their own code,
    # which is the mirror this whole file exists to keep out, arriving through the one door built
    # for a human.
    #
    # THE PREDICATE IS NARROWED, AND THE NEAR-MISS IS NAMED HERE RATHER THAN LEFT TO BE REDISCOVERED.
    # The obvious form — any occurrence of `CANON` in that file — matches its own explanatory comment
    # `# PROPOSED from the SHIPPED CANON`, so a guard asserting zero would red the tree it shipped
    # against and the fix would be degrading a sentence to dodge a substring. What is matched is an
    # emitted BLOCK HEADER: a string literal that BEGINS `CANON:`. That comment is not one, because
    # what it appends begins with `#` and carries no colon.
    #
    # WHAT THIS DOES NOT CHECK: it reads the scaffold's SOURCE, not its output. A header assembled
    # from pieces at runtime would pass this and is out of its reach; the arm that would catch that
    # is a scaffold run, which costs a corpus walk on every bar.
    #
    # AND THE SKIP ANNOUNCES ITSELF. This `if` carried no `else`, so renaming or deleting the file
    # it reads turned the guard into a pass with nothing said — a skip wearing a pass's clothes,
    # which is the one shape the charter names by hand. It is REPORTED rather than refused: this
    # kit's own `check_self_containment` reds on an empty population because the population is its
    # subject, whereas the scaffolder is a sibling command an adopter may not have installed, and a
    # red nobody can fix in their own tree is a red they learn to bypass.
    _scaffold = kit / "scaffold_lexicon.py"
    scaffold_skip = "" if _scaffold.is_file() else _scaffold.name
    if _scaffold.is_file():
        hits = [i + 1 for i, ln in enumerate(
            _scaffold.read_text(encoding="utf-8", errors="replace").splitlines())
            if _CANON_HEADER_RE.search(ln)]
        if hits:
            problems.append(
                "THE SCAFFOLD EMITS A `CANON:` BLOCK HEADER, at "
                + ", ".join(f"{_scaffold.name}:{n}" for n in hits)
                + ". The canon overlay is an OWNER declaration and the scaffold derives from the "
                  "corpus, so a proposed overlay is the mirror this kit exists to keep out arriving "
                  "through the one door built for a human. Remove the emission.")

    # --- extraction, with the vacuity arm ----------------------------------------------------
    offenders: dict[str, list[Offender]] = {k: [] for k in KINDS}
    # S1 — keyed on (extension, PREDICATE), never on extension alone. The fold this replaces
    # summed functions and types into one number, so `.js` reported a healthy 89 while P2 graded
    # ZERO JavaScript classes and nothing could say so. A population is per-predicate or it is
    # not a population — the predicate is what decides which definitions were even eligible.
    graded: dict[tuple[str, str], int] = {}
    extractor_carriers: set[str] = set()   # files an ARMED extractor found a definition in

    # THE WALK'S OWN REFUSALS, joining the list here so their position in the output is what it was
    # when this loop did the extracting itself.
    problems.extend(scan_problems)

    # RESOLVED ONCE, like `sets` above and for the same reason: the P1 split asks this index one
    # membership question per offending definition, and rebuilding a 120-key dict per question is a
    # second answer waiting to disagree with the first.
    #
    # THE MERGED TUPLE, and it travels with the index rather than beside it. `clusters` is the
    # SHIPPED tuple on a frozen tree, in which case every line below is byte-identical. It is merged
    # by the caller rather than here so its four refusals land where `run()` already names a
    # declaration refusal, above the corpus walk. TOOL-aSurfacedLexicon-11.
    forms = canon.build_form_index(clusters)

    for rel, ext, got, _problem in scanned:
        if got is None:
            continue
        funcs, types_, _imports = got
        graded[(ext, "verb")] = graded.get((ext, "verb"), 0) + len(funcs)
        graded[(ext, "suffix")] = graded.get((ext, "suffix"), 0) + len(types_)
        if funcs or types_:
            extractor_carriers.add(rel)

        for name, lineno in funcs:
            verb = leading_verb(name)
            if not verb:
                continue
            if verb not in verbs:
                # S1/S2 — CLASSIFIED HERE, once, in the one walk. The kit used to refuse and stop
                # there, and a gate that says no and nothing else gets waived rather than obeyed:
                # 79 of this tree's 968 offenders have a canon cluster naming the rename they owe,
                # and the message named none of them.
                rep, gloss = read_debt_gloss(verb, forms, clusters)
                detail = f"leading token {verb!r} is not in the declared VERBS table"
                if rep:
                    # THE REPLACEMENT IDENTIFIER, not just the representative. A refusal naming
                    # `check` leaves the author to re-spell their own name against it; one naming
                    # `check_thing` is a rename they can apply. Same helper `--suggest` uses, so the
                    # two surfaces cannot answer one question differently.
                    detail += (f" — DEBT: rename to `{render_swapped_name(name, rep)}`; it is a "
                               f"spelling of `{rep}`: "
                               + ((verbs.get(rep) or gloss).strip() or "no gloss declared")
                               + ("" if rep in verbs else
                                  f" (and `{rep}` needs a VERBS row of its own before the gate "
                                  f"accepts it)"))
                offenders["verb"].append(Offender(
                    "P1 verb", rel, lineno, name, detail,
                    verb=verb, cls="debt" if rep else "unruled"))

        for name, lineno in types_:
            for suf in banned:
                # No `name != suf` exemption. A type named exactly `Manager` is the PUREST instance
                # of "a type nobody scoped", and exempting it made the predicate weakest precisely
                # where the offence is strongest.
                if name.endswith(suf):
                    offenders["suffix"].append(Offender(
                        "P2 suffix", rel, lineno, name,
                        f"type name ends with the banned suffix {suf!r}"))
                    break

    # S2 — THE UNRULED HALF'S SITE CENSUS, and it can only be written after the walk because it is a
    # count over the whole corpus. MOST distinct unruled tokens on this tree occur exactly ONCE, so
    # `1 site` and `18 sites` are two different findings wearing one message: the first is a name to
    # fix, the second is a house idiom that either joins the table or gets renamed everywhere. The
    # proportion is deliberately not stated. It was, as 339 of 491, and the denominator was already
    # 751 by the time the line shipped -- both operands move with every unit that adds a definition,
    # and this build corrected that class seven times before deleting it instead. Read it from
    # `--list` when you need it.
    #
    # CORPUS-WIDE, not per-cell, and fork F3 of the spec is why the choice is written down. A reader
    # renaming a token wants to know how many definitions move; a per-cell count answers a question
    # about the row instead. The number is LABELLED corpus-wide on the line, because an unlabelled
    # count under a per-cell report reads as that cell's.
    sites: dict[str, int] = {}
    for o in offenders["verb"]:
        if o.cls == "unruled":
            sites[o.verb] = sites.get(o.verb, 0) + 1
    for o in offenders["verb"]:
        if o.cls == "unruled":
            o.detail += (f" — UNRULED: no canon cluster holds {o.verb!r}, so this is a scoping "
                         f"question and not a rename; {sites[o.verb]} definition(s) corpus-wide "
                         f"lead with it")

    # S6 — the live non-empty assertion. HYGIENE rule 5 applied to this gate: a check must not
    # select an empty population. A declared parser/probe language with NO definitions, against a
    # corpus that CONTAINS that extension, is an extractor that has gone inert.
    for ext, (pset, mode) in sorted(declared.items()):
        if mode == "dark":
            continue
        # UNCHANGED SEMANTICS, deliberately. This sums the VERB and SUFFIX populations because
        # that is what the folded number was, and section 3 forbids this unit moving a verdict.
        # Imports are excluded for the same reason: they were never in the fold.
        ext_total = graded.get((ext, "verb"), 0) + graded.get((ext, "suffix"), 0)
        if any(e == ext for _r, e, _d, _p in scanned) and not ext_total:
            problems.append(f"DEAD PROBE — .{ext} is declared `{mode}`"
                            + (f" ({pset})" if pset else "")
                            + " and the corpus contains it, but the extractor found NO definitions. "
                              "An extractor that selects an empty population passes green forever.")

    # S7 — THE OTHER ZERO POPULATION, and it is reported differently on purpose. DEAD PROBE's guard
    # requires the corpus to CONTAIN the extension, which is correct — an empty population cannot
    # prove an extractor inert — but it means a `LANGS` row arming a language this repo does not
    # carry falls through SILENTLY and is indistinguishable from one that grades. A REPORT and not a
    # refusal: declaring a language before the first file of it is written is a legal state, and one
    # a scaffolded adopter passes through. What is not legal is nobody being able to tell.
    present_exts = {e for _r, e, _d, _p in scanned}
    inert = [f".{ext}={mode}" + (f" ({pset})" if pset else "")
             for ext, (pset, mode) in sorted(declared.items()) if ext not in present_exts]

    # THE WAIVERS, THE STALE DETECTION AND THE PIN PARSE, and H1 of the closing review is why they
    # sit in the measurement rather than beside the verdict. They used to live BELOW the
    # `measure_mode` return, so `--measure` printed its pins and exited 0 over a tree carrying dead
    # waivers while `--check` on the same tree exited 1 naming them. An operator re-measuring after
    # curation pasted a pin derived from a corpus whose silencers no longer matched anything.
    #
    # `--scaffold` measures against the DERIVED seed, and the whole point of the seed is that a human
    # then rewrites it. Every pin it wrote was therefore a pre-curation number, and without `--measure`
    # the only way to re-measure after curating was to read the failure output of a red gate. That is
    # how a pin ends up asserted rather than measured — and two of these shipped as a hardcoded
    # `"0"` under a comment that called them MEASURED.
    waived_by: dict[str, dict] = {}
    unwaived_by: dict[str, list] = {}
    # PARSED ONCE. The round-1 H1 hoist copied the `int(pin_raw)` parse up here for its exception
    # side-effect and left the original below, so one fact had two readers that were identical that
    # day and free to diverge on any edit after it -- the class three of round 1's own findings were
    # about. The value is kept here and read below. Found by the round-2 review.
    pins_by_kind: dict[str, int] = {}
    for kind in KINDS:
        waivers = load_waivers(kit, kind)
        found = offenders[kind]
        waived_by[kind] = waivers
        unwaived_by[kind] = [o for o in found if o.text not in waivers]
        stale = [w for w in waivers if w not in {o.text for o in found}]
        if stale:
            problems.append(f"STALE WAIVERS in {WAIVER_FILES[kind]} (the matched text is gone; "
                            f"delete the row): {', '.join(sorted(stale))}")
        pin_raw = conf.get(PIN_KEYS[kind], "")
        try:
            pins_by_kind[kind] = int(pin_raw) if str(pin_raw).strip() else 0
        except ValueError:
            pins_by_kind[kind] = 0
            problems.append(f"{PIN_KEYS[kind]}={pin_raw!r} is not an integer")

    # DEAD SNIFFER IS A REFUSAL LIKE THE OTHERS, and getting it here took two moves. The first cut
    # appended to `problems` after that list had already been printed and folded into the exit code,
    # so it could never fire; the second printed and set `exit_code` directly, seventy-nine lines
    # below the measure-mode return, which fixed `--check` and left `--measure` exiting 0 with clean
    # pins over a tree `--check` redded by name. Both were armed-but-unreachable, one round apart,
    # and both were found by staging a break rather than by reading the code. `--measure` pays for
    # one definition-carrier scan it did not before, which is the honest price of the two modes
    # answering the same question.
    #
    # WHAT IT ASSERTS IS AGREEMENT, not "some dark extension carries a definition" — that wording
    # reds an honest adopter whose dark extensions are all data files. Every file an ARMED extractor
    # found a definition in must also sniff positive: two independent readings of one population, so
    # a sniffer that has gone blind CONTRADICTS the extractors rather than merely reporting zero.
    carriers = scan_definition_carriers(root, files)
    blind = sorted(extractor_carriers - carriers)
    if blind:
        problems.append(f"DEAD SNIFFER (the coverage sniffer found no definition in {len(blind)} "
                        f"file(s) where an ARMED extractor did, e.g. {blind[0]}; the denominator is "
                        f"undercounting, which reports coverage as BETTER than it is)")

    # --- TOOL-aSurfacedLexicon-6: the cell matrix's own three populations ---------------------
    #
    # THEY ARE DELIBERATELY DIFFERENT POPULATIONS. Two of them can legally be empty in a healthy
    # tree — nothing may be undeclared, and no armed cell need be dead — and the third cannot,
    # which is why only the third carries a liveness assertion.
    declared_cells = conf.get("CELLS") or {}
    cells, cell_problems = measure_conventions(scanned, conf, root, declared)
    problems.extend(cell_problems)

    # --- TOOL-aSurfacedLexicon-7: the P1 split, censused per DECLARED vocab cell ---------------
    #
    # OVER THE UNWAIVED OFFENDERS, so the pair reconciles with the scalar that grades the same list.
    # A waived offender is one the declaration already accounted for, and counting it into a debt
    # row would make the two ratchets disagree about the same corpus.
    vocab_cells, vocab_problems = measure_vocab_cells(unwaived_by["verb"], declared_cells)
    problems.extend(vocab_problems)

    # --- UNREAD PIN: a declared row no verdict path consumes -----------------------------------
    #
    # Closing review M2. Three well-formed `PINS` shapes parsed, passed `check_declaration`, and
    # were graded by NOTHING: `<cell>.suffix` on any cell (no reader anywhere — the predicate has
    # since left `PIN_PREDICATES`), `<cell>.debt`/`<cell>.unruled` on a cell lacking `vocab` (the
    # census only populates `vocab` cells), and `<cell>.conv` on a `dark` cell (the comparison sits
    # below the `dark` branch's `continue`). Observed: a declaration carrying all three produced no
    # line at all about any of them, while the same `conv` pin on a non-dark cell redded. A pin that
    # cannot fire reads as a ratchet and is a decoration.
    #
    # THE SET IS DERIVED, NOT ENUMERATED, which is why this is one arm and not three. It is the
    # declared keys minus the keys a verdict path actually consumes, so the next predicate somebody
    # adds to the closed set reds by this arm until something reads it — no shape list to keep in
    # step. There is a `STALE WAIVERS` arm here and there was no `STALE PIN` one.
    #
    # THE TWO CONDITIONS BELOW ARE `check_pass`'s TWO `continue`s, and that coupling is the one cost:
    # the conv row is consumed exactly where that loop does NOT skip (graded, and not `dark`), and
    # the debt/unruled pair exactly where `measure_vocab_cells` emitted a row. A selftest arm holds
    # them in step by staging each shape and asserting the refusal names it.
    read_pins = set()
    for _cell, _row in cells.items():
        if _row["graded"] and _row["convention"] != "dark":
            read_pins.add(f"{_cell}.conv")
    for _cell in vocab_cells:
        read_pins.update((f"{_cell}.debt", f"{_cell}.unruled"))
    unread_pins = sorted(k for k in (conf.get("PINS") or {}) if k not in read_pins)
    if unread_pins:
        problems.append(
            "UNREAD PIN (the row parses and is graded by nothing, so it can never fire; wire the "
            "predicate or delete the row): " + ", ".join(unread_pins)
            + ". A `.conv` row on a `dark` cell, or a `.debt`/`.unruled` row on a cell without the "
              "`vocab` flag, is declared past the point its verdict path returns.")

    # S7 — THE REPORT'S LIVENESS, asserted as PARITY against the parsed block rather than as
    # `> 0`, so it catches the single row that goes missing as well as the table that empties.
    # A declared row that never reaches the printer is a reporting bug, and an empty table under a
    # green line is exactly what a cell matrix exists to abolish.
    #
    # WHAT IT DOES NOT CHECK: a declaration carrying NO `CELLS` block at all. That is a legal inert
    # state — the kit is opt-in and every adopter passes through it — and refusing it would red
    # every tree that installed this kit before the block existed. The population nobody declared
    # is what `UNDECLARED CELL` below reports on instead.
    if len(cells) != len(declared_cells):
        problems.append(
            f"DEAD CELL REPORT — the declaration carries {len(declared_cells)} CELLS row(s) and "
            f"the report built {len(cells)}. A report that drops rows prints a table nobody can "
            f"tell from a clean matrix.")

    for cell, row in cells.items():
        if row["rule"] is None:
            problems.append(
                f"UNRULED SURFACE — the cell `{cell}` names surface "
                f"`{parse_cell_key(cell)[1]}`, which "
                f"is declarable but carries no row in CELL_POPULATION_RULES, so the cell would "
                f"grade nothing while reporting a clean zero. Declare its population rule, or drop "
                f"the surface from the closed set in lexicon_conf.py.")
            continue
        # S2 — DEAD CELL. This REPLACES a report — the tree printed `armed but grading nothing
        # (reported, not a refusal)` for the whole life of the declaration and nothing ever changed,
        # which is the green-by-absence class wearing a different label.
        #
        # TWO EXEMPTIONS, and both are the same argument: an empty population is only evidence of a
        # dead cell where a non-empty one was POSSIBLE. `dark` is a declared refusal to grade, so
        # its zero is the declaration working. And an extension the corpus carries no file of is an
        # INERT DECLARATION, which this engine already reports rather than refuses one arm over —
        # declaring a language before its first file is written is a legal state a scaffolded
        # adopter passes through, and redding a cell for it would make this refusal disagree with
        # its own sibling about the same tree.
        if (row["convention"] != "dark" and not row["population"]
                and parse_cell_key(cell)[0] in present_exts):
            problems.append(
                f"DEAD CELL — `{cell}` is armed at `{row['convention']}` and its population rule "
                f"({row['rule']}) selected NOTHING. A cell grading an empty population passes green "
                f"forever, so the declaration is wrong or the selector is.")

    # S1 — UNDECLARED CELL, over the EXTRACTED populations and NOTHING else. `graded` is what
    # `extract` produced without being asked, which is functions and types; a `file` or `constant`
    # population exists only for a cell a `CELLS` row declares, so an undeclared one of THOSE has
    # no population to be non-empty and this arm cannot see it. That hole is real, it is stated on
    # the run beside the list, and closing it needs a declaration-independent selector per surface.
    # DERIVED from the walk rather than asserted beside it: this list moves if and only if the
    # extracted population moves.
    undeclared_cells = [f"{ext}.{PREDICATE_SURFACES[kind]} at {n}"
                        for (ext, kind), n in sorted(graded.items())
                        if n and f"{ext}.{PREDICATE_SURFACES[kind]}" not in declared_cells]
    #
    # THE REFUSAL IS GATED ON `declared_cells` BEING NON-EMPTY, which is the SAME boundary the
    # `DEAD CELL REPORT` arm forty lines up already draws and states: a declaration carrying no
    # `CELLS` block at all is a legal inert state, every adopter passes through it, and refusing it
    # would red every tree that installed this kit before the block existed. Two arms in one
    # function disagreeing about that would be the two-answers-to-one-question class inside a
    # single predicate. What the gate buys once an owner declares their FIRST cell is completeness:
    # a partial matrix reds, naming each pair. The boundary is measured rather than reasoned: armed
    # without this clause, the fixtures that red are the ones declaring `LANGS` and no cells, which
    # is exactly the adopter state it describes. No count is written here — it moves with every
    # fixture this kit's selftest adds, and the one that was written here did not reproduce.
    if undeclared_cells and UNDECLARED_CELL_ARMED and declared_cells:
        problems.append(
            "UNDECLARED CELL (an extracted population with no CELLS row grades nothing and is "
            "invisible to every cell verdict; declare each, `dark` if it should not be graded): "
            + ", ".join(undeclared_cells))

    return {
        "problems": problems,
        "cells": cells,
        "vocab_cells": vocab_cells,
        "pin_rows": conf.get("PINS") or {},
        "undeclared_cells": undeclared_cells,
        "graded": graded,
        "offenders": offenders,
        "waivers": waived_by,
        "unwaived": unwaived_by,
        "pins": pins_by_kind,
        "declared": declared,
        # THE WALK ITSELF, so a caller that needs the population rather than a verdict does not pay
        # for a second one. `--expand` derives its proposal set from this list; without it that mode
        # would walk the corpus again, and two walks over one tree is two chances to disagree about
        # which files are armed. TOOL-aSurfacedLexicon-10.
        "scanned": scanned,
        "sets": sets,
        "patterns": conf.get("PATTERNS") or {},
        "canon_overlay": conf.get("CANON") or {},
        "inert": inert,
        "files": files,
        "carriers": carriers,
        "self_mods": self_mods,
        "self_imports": self_imports,
        "scaffold_skip": scaffold_skip,
    }


def check_pass(measured: dict, list_mode: bool = False) -> int:
    """THE VERDICT HALF: prints the counts and the pin verdicts, decides nothing new.

    It reads `measure_pass`'s return and NOTHING else — no corpus, no conf, no waiver file. That is
    what makes the two modes structurally unable to disagree about a refusal: there is one list, it
    is complete before this function is entered, and `--measure` prints the same one.
    """
    declared = measured["declared"]
    graded = measured["graded"]
    problems = measured["problems"]

    exit_code = 0
    tally: dict[str, tuple[int, int, int]] = {}
    for kind in KINDS:
        waivers = measured["waivers"][kind]
        found = measured["offenders"][kind]
        unwaived = measured["unwaived"][kind]

        if list_mode:
            for o in found:
                print(("  waived " if o.text in waivers else "  ") + str(o))

        tally[kind] = (sum(v for (_e, k), v in graded.items() if k == kind),
                       len(unwaived), len(found) - len(unwaived))
        # A TWO-SIDED EQUALITY, and the two directions call for opposite actions, which is why they
        # print different things. A RISE is the ratchet everybody expects: name the offenders. A
        # FALL used to be silent, and that silence is what let the pin sit eleven moves above a
        # corpus that had already drained under it — a number nobody was obliged to re-measure is a
        # number nobody re-measured. A fall now reds too, and prints the exact replacement row, so
        # clearing it is a paste rather than an investigation.
        pin = measured["pins"][kind]
        if len(unwaived) > pin:
            exit_code = 1
            print(f"lexicon: {kind} offenders {len(unwaived)} over pin {pin}:")
            for o in unwaived[:40]:
                print(f"  {o}")
            if len(unwaived) > 40:
                print(f"  … and {len(unwaived) - 40} more")
        elif len(unwaived) < pin:
            exit_code = 1
            print(f"lexicon: {kind} offenders {len(unwaived)} UNDER pin {pin} — the pin is an "
                  f"equality in both directions, so a drain lands in the declaration or it is not "
                  f"landed. Paste this row into .lexicon.conf, naming what left:")
            print(f'  {PIN_KEYS[kind]}="{len(unwaived)}"')

    # --- the convention cells, one block per declared row -------------------------------------
    #
    # THE ROW IS PRINTED ON GREEN TOO, with its population and its teeth, for the same reason the
    # `P1`/`P2` rows below are: a green row is a measurement or it is a mood. A cell reporting `0 of
    # 976` beside `teeth camel=736` has been shown to bite; the same cell with no teeth clause is
    # indistinguishable from one whose predicate never ran.
    for cell, row in measured["cells"].items():
        if not row["graded"]:
            print(f"lexicon: {cell}.conv UNRULED — the `{parse_cell_key(cell)[1]}` surface "
                  f"carries no population rule, so this cell is refused rather than reported at "
                  f"zero")
            continue
        # S4 — THE POPULATION RULE, on every row and beside every count. A count with no rule reads
        # as coverage when it is only a scope, and the denominator is printed with it because a row
        # whose graded count equals its denominator (every `function` cell, by construction) is the
        # only way a reader can see that a narrowed row does NOT.
        pop = (f"population {row['population']} of {row['denominator']} (rule: {row['rule']})")
        if row["convention"] == "dark":
            print(f"lexicon: {cell}.conv dark — declared unGRADED over "
                  f"{row['population']} name(s), which is a refusal and not a skip; {pop}")
            continue
        bad = row["verdicts"]
        n_amb = sum(1 for _p, _l, _n, v, _m in bad if v == "AMBIGUOUS")
        teeth = " ".join(f"{a}={n}" for a, n in sorted(row["teeth"].items()))
        print(f"lexicon: {cell}.conv {len(bad)} of {row['population']} against "
              f"{row['convention']} — violation {len(bad) - n_amb}, ambiguous {n_amb}, "
              f"teeth {teeth}; {pop}")
        for path, line, _n, _v, message in bad[:40]:
            print(f"  {path}:{line}: {message}")
        if len(bad) > 40:
            print(f"  … and {len(bad) - 40} more")
        # THE SAME TWO-SIDED EQUALITY the pins above carry, and for the same reason: a `conv` pin
        # that only ratchets upward lets a cell drain without anybody re-measuring it.
        if len(bad) != row["pin"]:
            exit_code = 1
            print(f"lexicon: {cell}.conv {len(bad)} against declared pin {row['pin']} — the pin is "
                  f"an equality in both directions. Paste this row into .lexicon.conf under PINS:")
            print(f"  {cell}.conv  {len(bad)}")

    # --- TOOL-aSurfacedLexicon-7: the P1 split's own per-cell ratchets -------------------------
    #
    # ADDITIVE TO THE SCALAR, never a replacement for it at this build order. `VERB_OFFENDER_PIN`
    # keeps grading the whole unwaived population above; these rows grade the two halves of each
    # DECLARED vocab cell. Both bind, and that is the point rather than a transition cost: a rename
    # moving a definition from DEBT to UNRULED inside one cell holds the total, so the scalar greens
    # and only these rows can see it. A tree with no vocab cell has exactly the ratchet it had
    # before.
    #
    # TWO-SIDED, like every other pin here. A fall reds as loudly as a rise, because a drain nobody
    # was obliged to re-measure is a drain nobody re-measured.
    pin_rows = measured["pin_rows"]
    for cell, (debt, unruled) in measured["vocab_cells"].items():
        for predicate, got in (("debt", debt), ("unruled", unruled)):
            key = f"{cell}.{predicate}"
            want = pin_rows.get(key, 0)
            print(f"lexicon: {key} {got} against declared pin {want}")
            if got != want:
                exit_code = 1
                print(f"lexicon:   {key} MOVED {want} -> {got} — the pin is an equality in both "
                      f"directions. Paste this row into .lexicon.conf under PINS:, separated from "
                      f"its neighbour by one blank line:")
                print(f"  {key}  {got}")
                # F2, ratified — THE ATTRIBUTION, and it is the difference between a diagnosis and a
                # bug report. An owner who has just unfrozen the canon and is then handed the bare
                # mismatch above reads it as a fault in the ratchet: the overlay moves definitions
                # between the DEBT and UNRULED buckets by construction, and both rows are two-sided
                # pins, so this red is the design working. Printed only where an overlay exists, so
                # the line tells a reader something the mismatch alone does not.
                if measured["canon_overlay"]:
                    print(f"lexicon:   CAUSE — the CANON overlay is unfrozen "
                          f"({len(measured['canon_overlay'])} owner row(s)), which reclassifies "
                          f"leading tokens between DEBT and UNRULED. This movement is that "
                          f"reclassification, not a fault in the ratchet; deleting the CANON: "
                          f"block restores the shipped classification.")

    for p in problems:
        print(f"lexicon: {p}")
    if problems:
        exit_code = 1

    # S3 — the counts, on GREEN as well as on RED. The green line used to print the file count and
    # the coverage modes and NO population and NO offender count, so a reader could not tell this
    # repo from one with nothing to find. A green row is a measurement or it is a mood.
    label = {"verb": "P1 verb  ", "suffix": "P2 suffix"}
    for kind in KINDS:
        g, off, wv = tally[kind]
        # S6 — THE SPLIT ON THE COUNT LINE, on GREEN as well as on RED, and its two halves printed
        # beside the sum they add to so a reader can see that the split moved no verdict. A total
        # with no split is what let one bucket over two populations move eleven times and produce
        # no renames from the second of them.
        split = ""
        if kind == "verb":
            unw = measured["unwaived"][kind]
            debt = sum(1 for o in unw if o.cls == "debt")
            split = f" (debt={debt} + unruled={len(unw) - debt})"
        print(f"lexicon: {label[kind]} graded={g} offenders={off}{split} waived={wv}")

    # THE SELF-CONTAINMENT POPULATION, on green as well as on red, and deliberately NOT shaped like
    # the two rows above: this is a refusal with a measured reach, not a third declared predicate.
    # Printing it is what makes the absence of a refusal a measurement rather than a mood — and
    # printing alone is not enough, which is why a zero here is a `DEAD PROBE` refusal above.
    print(f"lexicon: self-contained — judged {measured['self_imports']} import(s) over "
          f"{measured['self_mods']} module(s) beside the engine")

    # THE STRUCTURAL GUARD THAT READ NOTHING SAYS SO, per the charter's skip-announces-itself rule.
    # Silence here would be indistinguishable from a guard that ran and found nothing.
    if measured["scaffold_skip"]:
        print(f"lexicon: SCAFFOLD GUARD SKIPPED — no `{measured['scaffold_skip']}` beside the "
              f"engine, so the arm refusing a scaffold that emits a `CANON:` block header read no "
              f"file this run and went UNEXERCISED (reported, not a refusal)")

    # S2 — a REPORT, not a refusal. An armed pair that grades nothing is NAMED so the zero is
    # legible; it does not red. `.js` here is armed and has no classes at all, which is a repo
    # that does not write JavaScript classes rather than an extractor that went inert — and the
    # inert case is owned by the frozen SENTINELS fixture in this kit's own selftest, which can
    # tell the two apart where a single tree cannot. See the spec's section 4.
    # S1/S2 — the coverage fraction, on every run. The armed share of the files that actually
    # carry a definition, which is the number a `LANGS` edit moves and nothing else reported.
    #
    # REPORTING SITE ONE of `resolve_extractor`'s four. It read the mode and the pattern sets for
    # itself until TOOL-aGradedDialect-3 §8 F1, which counted a `probe`-declared parser as unarmed
    # while the extractor was reading it — the fraction and the extraction disagreeing about one
    # file, in the two halves of one run.
    carriers = measured["carriers"]
    armed_exts = {e for e, (ps, m) in declared.items()
                  if resolve_extractor(m, ps, measured["sets"]) is not None}
    armed_carriers = {f for f in carriers if ext_of(f) in armed_exts}
    pct = (100.0 * len(armed_carriers) / len(carriers)) if carriers else 0.0
    print(f"lexicon: coverage — armed {len(armed_carriers)} of {len(carriers)} "
          f"definition-carrying file(s) ({pct:.1f}%)")

    # STILL A REPORT, and it now covers the REMAINDER rather than the whole. A zero population on a
    # cell a `CELLS` row DECLARES is a `DEAD CELL` refusal above; what is left here is the pairs
    # nobody declared, where a zero is a repo that writes no JavaScript classes rather than an
    # extractor gone inert, and a single tree cannot tell those two apart.
    empty = [f".{e} {k}=0" for (e, k), v in sorted(graded.items()) if v == 0]
    if empty:
        print("lexicon: armed but grading nothing, UNDECLARED as a cell (reported, not a refusal; "
              "a DECLARED cell at zero is a DEAD CELL refusal above): " + ", ".join(empty))

    # S1 — the UNDECLARED CELL list, printed on EVERY run whether or not it is armed, so the pairs
    # it names stay visible for however long the promotion is outstanding rather than accruing where
    # nobody looks. The second line is the arm's own header, per the charter's rule that a gate
    # states what it does NOT check: a reader who takes this list for the whole undeclared
    # population is reading a scope as a coverage claim.
    print(f"lexicon: UNDECLARED CELL — {len(measured['undeclared_cells'])} extracted population(s) "
          f"with no CELLS row"
          + (": " + ", ".join(measured["undeclared_cells"]) if measured["undeclared_cells"] else "")
          # THE LABEL READS THE SAME CONDITION THE REFUSAL DOES, both halves of it. A run over a
          # declaration with no `CELLS` block is armed and still does not refuse, and printing
          # `[REFUSED above]` there would be a label describing the constant rather than the run.
          + (" [REFUSED above]" if UNDECLARED_CELL_ARMED and measured["cells"]
             else " [reported, not a refusal]"))
    print("lexicon:   NOT CHECKED by that list — the `file` and `constant` surfaces. Their "
          "populations are computed by a declared cell's own selector, so an UNDECLARED one of "
          "those has no population to be non-empty and this arm cannot see it.")

    # S7 — the declaration that arms nothing because the corpus carries none of it. Reported, never
    # a refusal; see the comment beside the measurement.
    if measured["inert"]:
        # THE TWO NAMES ARE KEPT APART IN THE TEXT AS WELL AS IN THE LOGIC. This line used to spell
        # the sibling refusal to explain itself, which put that refusal's name in the output of a run
        # where it had not fired — and the arm asserting the two are distinguishable read it and
        # failed. A report that cannot be told from the thing it is not is the whole defect here.
        print("lexicon: INERT DECLARATION (declared, but the corpus carries no file of that "
              "extension, so nothing is graded and the empty-population refusal cannot judge it "
              "either): " + ", ".join(measured["inert"]))

    # S3 — the declared extractor rows, on every run, and the REPLACED keys named separately. A
    # declared row that lands on a SHIPPED set silently retires the regex it replaces, and a set
    # weakened rather than emptied grades a smaller population while reporting a clean run. Printing
    # the two apart is what makes that a reading rather than an inference.
    patterns = measured["patterns"]
    if patterns:
        print(f"lexicon: PATTERNS — {len(patterns)} declared extractor row(s): "
              + " ".join(patterns))
        over = [k for k in patterns if k.split(".")[0] in PATTERN_SETS]
        if over:
            print("lexicon: PATTERNS REPLACES a SHIPPED extractor key, so the shipped regex for it "
                  "no longer runs: " + " ".join(over))

    if exit_code == 0:
        modes = ", ".join(f".{e}={m}" for e, (_, m) in sorted(declared.items()))
        print(f"lexicon OK — {len(measured['files'])} tracked file(s); coverage: {modes}")
    return exit_code


def run(root: Path, list_mode: bool = False, measure_mode: bool = False) -> int:
    """The two modes, over ONE measurement. The mode branch is here and nowhere deeper."""
    kit = Path(__file__).resolve().parent
    conf_path = root / CONF_NAME
    if not conf_path.exists():
        print(f"lexicon: NOT ADOPTED — no {CONF_NAME} at the repo root; the kit is opt-in and inert without it")
        return 0

    try:
        conf = load_conf(conf_path)
        declared = {ext: (pset, mode) for ext, pset, mode in langs(conf)}
        # ValueError joins ConfError here and nowhere wider. `build_clusters` is in `canon.py`,
        # which imports nothing on purpose, so it cannot raise the reader's own exception — and its
        # four refusals are declaration refusals, which belong beside the reader's rather than in a
        # traceback out of the corpus walk. TOOL-aSurfacedLexicon-11.
        clusters = canon.build_clusters(conf.get("CANON") or {})
    except (ConfError, ValueError) as e:
        print(f"lexicon: {e}")
        return 1

    # ABOVE THE COUNTS, on every run, red and green alike (S4).
    print_canon_posture(conf)

    measured = measure_pass(root, kit, conf, declared, clusters)
    problems = measured["problems"]

    if measure_mode:
        # `--measure` prints the counts THIS conf produces and decides nothing beyond its own
        # refusals. S4 — the exit code these conditions always described. UNDECLARED EXTENSIONS,
        # DEAD PROBE and STALE WAIVERS rode as `# NOTE:` comments under an unconditional 0, so
        # `--measure` could not fail. Three later units use it as a discharge probe, and a probe
        # that cannot fail discharges nothing. NOT SELF-CONTAINED and its own DEAD PROBE join them.
        for kind in KINDS:
            print(f'{PIN_KEYS[kind]}="{len(measured["unwaived"][kind])}"')
        # S5 — the P1 split's rows, for every DECLARED vocab cell and no others. EMPTY on a tree
        # that arms none, which is this repo at this build order and is the correct result: a pin
        # row naming a cell no `CELLS` row declares is a `load_conf` refusal, so emitting one
        # eagerly would hand the operator bytes the wiring leg rejects.
        rows = render_pin_rows(measured["vocab_cells"])
        if rows:
            print("# PINS: rows — paste them INSIDE the PINS: block, indented, keeping the blank")
            print("# lines; two adjacent pin rows are a refusal in lexicon_conf._parse_pins.")
            for line in rows:
                print(line)
        if problems:
            print("# NOTE: the run also reported problems that are not pin-counted:")
            for p in problems:
                print(f"#   {p}")
        return 1 if problems else 0

    return check_pass(measured, list_mode)



# ============================================================================================
# TOOL-dScaffoldedMirror-10 — SUPPLY. The half of this kit with a measured record.
#
# Since the declaration landed, this repo added 136 definitions and zero offenders over a window in
# which the gate refused NOTHING. That half works by delivering context, and it was delivered by a
# session happening to open the conf. `--suggest` hands the table to the author instead.
#
# IT IS THE ONLY SUPPLY VERB LEFT, and the gap is stated rather than softened.
# TOOL-aSurfacedLexicon-3 deleted the per-FILE reading (one file's objects, measured against the
# corpus) together with the pre-adoption report, and NOTHING in this build restores a per-file
# reading at all: TOOL-aSurfacedLexicon-8 restores the per-NAME one with the canon behind it, at
# build order 6. Until then the Skill runs on the per-identifier route alone. The deleted modes'
# spellings are deliberately not written anywhere in this kit — a flag name that resolves to a usage
# block is a dead string, and the dispatcher below already names every mode that exists.
#
# THE GUARD IS STRUCTURAL, NOT STATED (S6). Section 12 of the charter bans a GATE whose vocabulary is
# a mirror of the code it grades. The verb below is not one: it cannot exit 1, it prints no pin, and
# nothing in `scaffold_lexicon.py` imports it — so what the corpus DOES can never become what the
# corpus SHOULD do by a path anyone can take. A promise would not survive a refactor; the absence of
# a return path does.
# ============================================================================================


def build_banned_index(conf: dict) -> dict:
    """`{banned-token: verb}` — the inverse of the NOT clauses, so a refusal can name the REPLACEMENT.

    Depends on `TOOL-dScaffoldedMirror-8`'s structured grammar and does not re-parse it. A verb may
    ban several tokens; a token banned by two verbs keeps the first, which the two asserts in that
    unit make impossible to reach.
    """
    out = {}
    for verb, banned in build_negatives(conf).items():
        for tok in banned:
            out.setdefault(tok, verb)
    return out


def resolve_cell(cells: dict, spec: str) -> tuple:
    """`(cell, convention, flags)` for one `--as` argument, or a ConfError naming WHICH refusal.

    FOUR REFUSALS, SEPARATELY WORDED, and the wording is the product (TOOL-aSurfacedLexicon-8 S2). A
    caller who typed a cell that does not exist, a cell the owner declared `dark`, a key that is not
    a cell at all, and a BARE SURFACE have four different problems, and one message for all four
    tells none of them what to do next. The bare-surface refusal is a MENU: it lists the declared
    cells carrying that surface, which is fork F2's ratified ruling and the clause that keeps the
    refusal from being a wall.

    Checked in that order because the shapes overlap: `file` is malformed AS A CELL KEY, so the bare
    surface has to be recognised before the generic malformed refusal can claim it.
    """
    if spec in SURFACES:
        carriers = sorted(c for c in cells if parse_cell_key(c)[1] == spec)
        menu = (" ".join(carriers) if carriers else
                "none — this declaration carries no cell for that surface")
        raise ConfError(f"`--as {spec}` names a BARE SURFACE, and a surface is not a cell: this "
                        f"declaration may arm two languages on it and the answer differs by "
                        f"language. Declared `{spec}` cells: {menu}")
    try:
        _ext, _surface, kind, _lit = parse_cell_key(spec)
    except ConfError as exc:
        raise ConfError(f"`--as {spec}` is MALFORMED: {exc}") from exc
    if kind:
        raise ConfError(f"`--as {spec}` is MALFORMED: it carries a selector. `--as` addresses the "
                        f"parent `<ext>.<surface>` cell; a selector is applied FROM THE NAME, the "
                        f"way the grader applies it.")
    if spec not in cells:
        raise ConfError(f"cell `{spec}` is UNDECLARED — no CELLS row names it, so there is no "
                        f"convention to answer in. Declared cells: "
                        + (" ".join(sorted(cells)) or "none"))
    conv, flags = cells[spec]
    if conv == "dark":
        raise ConfError(f"cell `{spec}` is declared `dark`, which is the owner saying this surface "
                        f"is deliberately ungraded here. There is no convention to answer in.")
    return spec, conv, flags


def read_routed_cell(cells: dict, cell: str, name: str) -> tuple:
    """The row `name` is actually graded in — the parent, or a selector'd row that claims the name.

    S9. `--as` takes the plain cell and never a selector'd key, but the grader partitions that cell
    by selector, so answering in the PARENT's convention for a name the grader routes elsewhere is
    the same surface-blindness one level down. A `prefix` selector is resolvable from an identifier
    and is applied here. A `decorator` selector is NOT — `--suggest` sees no decorator — so a cell
    carrying one answers in the parent's convention and the caller is TOLD, rather than left with a
    confident answer the gate may disagree with.

    `name` IS THE GRADED STRING, not the caller's raw argument, and the parameter is named for what
    it is because passing the wrong one is invisible. Closing review M1: this was handed the raw
    `--suggest` argument while the grader's `scan_routes` matches on the STEM, so
    the codebase-map kit's `test_codebase_map.py` missed a `+prefix:test` row here and hit it there —
    one file, two cells, two verdicts.

    EVERY MATCHING SELECTOR IS COLLECTED AND A SECOND ONE IS REFUSED, never resolved by declaration
    order. `scan_routes` calls that resolution disqualifying in its own words — "a naming gate whose
    verdict depends on which row the reader saw first is not a declaration" — and this verb used to
    do exactly it, returning the first dict-order hit while `--check` refused the same name as
    `AMBIGUOUS SELECTOR` and graded it by neither. Closing review M3.
    """
    note = ""
    hits = []
    for key, (conv, flags) in cells.items():
        if not key.startswith(cell + "+"):
            continue
        _e, _s, kind, lit = parse_cell_key(key)
        if kind == "prefix" and name.startswith(lit):
            hits.append((key, conv, flags, lit))
        if kind == "decorator":
            note = (f"cell `{cell}` also declares a `decorator` selector (`{lit}`), which cannot be "
                    f"resolved from an identifier — this answer is the parent cell's")
    if len(hits) > 1:
        raise ConfError(
            f"AMBIGUOUS SELECTOR — the name `{name}` matches {len(hits)} selectors on cell "
            f"`{cell}`: " + " ".join(f"+prefix:{lit}" for _k, _c, _f, lit in hits)
            + ". Which convention it is graded against would depend on which row the reader saw "
              "first, so it is graded by NEITHER and the overlap is refused where it is written — "
              "the same refusal `--check` prints over the corpus.")
    if hits:
        key, conv, flags, _lit = hits[0]
        # THE `decorator` NOTE IS DROPPED WITH THE PARENT, not carried onto the routed row: the note
        # says "this answer is the parent cell's", and once a prefix row claims the name it is not.
        return key, conv, flags, ""
    return cell, cells[cell][0], cells[cell][1], note


def run_suggest(root: Path, name: str, cell_spec: str) -> int:
    """S1 — one deterministic line for ONE identifier, from the declaration and the SHIPPED CANON.

    TWO SOURCES, IN THE FIXED PRECEDENCE the body below states: the declaration's own inverted NOT
    clauses first, then `canon.py` where no row bans the token by name. It read the declaration and
    nothing else until TOOL-aSurfacedLexicon-7 wired the canon in, and this line said so for one
    unit longer than it was true.

    NO CORPUS PASS, deliberately and measurably: the whole value is that an author can ask before
    writing, and a verb that walks 900 files to answer one question is a verb nobody waits for.
    Both sources are tables that ship with the kit, so this stays true wherever it is installed.
    `--as` adds a THIRD table read and no walk at all.

    SURFACE-AWARE (TOOL-aSurfacedLexicon-8). `cell_spec` is the `--as` argument and it is REQUIRED,
    because the surface is the whole question: which predicates are armed and which convention the
    answer is spelled in are both properties of the cell, and a default answers that silently for a
    caller who did not think about it. A surface-blind suggestion is how this verb handed back
    `loadUserData` for a cell declaring snake — a name its own gate reds.

    AT MOST THREE CHECKS, IN THIS ORDER: the banned tail on the surface P2 grades, the leading
    token on the surface P1 grades, and the convention always. The re-casing is applied to whatever
    name the earlier checks produced, so the printed name is legal under every armed predicate of
    that cell at once rather than under the last one to run.

    WHICH SURFACE ARMS WHICH PREDICATE IS READ FROM `PREDICATE_SURFACES`, not from a per-cell flag,
    and closing review B2 is why that sentence is worth its own paragraph. The two checks used to be
    gated on the cell's `vocab` and `notail` flags while the GRADER arms neither — P1 walks every
    extracted function and P2 every extracted type, whatever any `CELLS` row says. So a declaration
    arming no flag (this repo's, and every scaffolded adopter's) got `OK` here for names the merge
    bar reds on, and the installed Skill tells every agent to trust this answer. `vocab` survives as
    what it always graded, the per-cell DEBT/UNRULED ratchet in `measure_vocab_cells`; `notail` had
    no reader but the defect and is gone from the grammar.

    THE TAIL-BEFORE-VERB ORDER IS DEFENSIVE OVER DISJOINT POPULATIONS, which is stated rather than
    implied: `PREDICATE_SURFACES` maps the two predicates onto DIFFERENT surfaces, so no cell can
    reach both branches and nothing here can distinguish this ordering from its reverse. A predicate
    added on a surface another already grades gives the rule a population and owes an arm whose
    input hits both.
    """
    try:
        conf = load_conf(root / CONF_NAME)
    except (ConfError, OSError) as exc:
        print(f"lexicon: cannot read the declaration: {exc}")
        return 2
    verbs = conf.get("VERBS") or {}
    if not verbs:
        print("lexicon: no VERBS declared; nothing to suggest against")
        return 2
    try:
        # `flags` is deliberately DISCARDED. Per-cell arming flags used to gate what this mode
        # checked, which is the B2 defect the closing review found: the grader reads no such flag,
        # so a name the bar reds on came back OK here. The predicate set is now PREDICATE_SURFACES
        # and both surfaces read it, which is why nothing below wants the flags.
        cell, conv, _flags = resolve_cell(conf.get("CELLS") or {}, cell_spec)
    except ConfError as exc:
        print(f"lexicon: {exc}")
        return 2

    # S8 — WHAT A `file` CELL'S ARGUMENT IS. `--suggest` takes an identifier, so a `file` cell takes
    # a BASENAME and grades the stem `read_stem` cuts from it — the grader's own seam, reused rather
    # than re-derived, because a suggester that stems differently from the checker is the
    # surface-blindness this unit exists to remove, one level down. `_SUBTOKEN_RE` shreds `.` and `/`
    # into separate tokens and cannot compute that stem at all.
    #
    # COMPUTED ABOVE THE ROUTING, AND THROUGH `parse_cell_key`. Both halves are closing-review
    # fixes and they are one edit because they are one ordering. M1: `read_routed_cell` was handed
    # the RAW argument while the grader routes on the stem, so a path-shaped argument missed a
    # `+prefix:` row the grader hits. H3: the surface test was `cell.split(".")[1]`, run AFTER
    # routing had reassigned `cell` to `py.file+prefix:test`, so it compared against
    # `file+prefix:test`, never took the stem, and left `graded` carrying the `.py` extension — a
    # name no convention can spell, so the advisor emitted a false refusal on a stem the gate
    # SATISFIES. `parse_cell_key` is the one reader of a cell key in this kit and the `.split(".")`
    # idiom is now gone from this file; a selftest arm holds it gone.
    surface = parse_cell_key(cell)[1]
    graded = (read_stem(name.replace("\\", "/").rsplit("/", 1)[-1])
              if surface == "file" else name)

    try:
        cell, conv, flags, routing = read_routed_cell(conf.get("CELLS") or {}, cell, graded)
    except ConfError as exc:
        print(f"lexicon: {exc}")
        return 2
    try:
        clusters = canon.build_clusters(conf.get("CANON") or {})
    except ValueError as exc:
        print(f"lexicon: {exc}")
        return 2
    # S4 — the posture, ABOVE the answer, on this surface too. `--suggest` is the verb an author
    # reads before writing a name, so an overlay steering that answer with nothing saying so is the
    # quiet unfreeze in the one place it would be least visible.
    print_canon_posture(conf)

    lines = []
    if routing:
        lines.append(f"note — {routing}")

    # WHICH PREDICATES ARE ARMED IS A PROPERTY OF THE SURFACE, NEVER OF A PER-CELL FLAG, and that is
    # closing review B2 — the blocker this whole verb was found guilty of. P1 and P2 grade the
    # corpus UNCONDITIONALLY: every extracted function is checked against `VERBS`, every extracted
    # type against `BANNED_SUFFIXES`, and no `CELLS` row can arm or disarm either. This verb gated
    # the same two checks on the cell's `vocab` and `notail` flags, so on a declaration that armed
    # neither — this repo's, and every scaffolded adopter's — `--suggest fetch_remote --as
    # py.function` answered `OK` for a name `--check` reds on by name. The installed Skill tells
    # every agent here to trust that answer.
    #
    # `PREDICATE_SURFACES` IS THE MAPPING and it is read rather than restated: it already declares
    # which surface each predicate's population IS, which is what stops the tail check firing on a
    # `file` cell P2 never grades. A cell whose surface no predicate grades gets the convention
    # check alone, which is exactly what the grader does to it.
    if surface == PREDICATE_SURFACES["suffix"]:
        for suf in tuple(t for t in (conf.get("BANNED_SUFFIXES") or "").split() if t):
            if graded.endswith(suf):
                print(f"`{graded}` ends with the banned suffix `{suf}`, which P2 bans on the "
                      f"`{surface}` surface cell `{cell}` grades — the question is what this thing "
                      f"IS, and `{suf}` answers that with a role nobody scoped.")
                for line in lines:
                    print(line)
                return 0

    verb = leading_verb(graded)
    if not verb:
        # AC7 — `leading_verb`'s contract, preserved rather than re-spelled around. Its population is
        # the underscore-only and the non-ASCII names; a DIGIT-leading name is graded, because
        # `_SUBTOKEN_RE` carries `[0-9]+` and `leading_verb("1")` returns `"1"`.
        print(f"lexicon: {graded} has no word characters, so it is ungradeable rather than wrong")
        return 0

    banned = build_banned_index(conf)
    # S3 — TWO SOURCES, IN A FIXED PRECEDENCE, and the order is the whole criterion. The
    # declaration's own inverted NOT clauses win: the owner wrote that negative and the canon did
    # not. Only where no row bans the token by name does the shipped canon get asked — which is 36
    # of this repo's 44 python debt definitions, the population that used to get a refusal and
    # nothing else.
    #
    # THE TWO DISAGREE ON THIS TREE, which is what makes the precedence observable rather than
    # asserted: `install` is banned by a row naming `seed`, and `canon.build_form_index()["install"]`
    # is `init`. An arm in `selftest.py` reds if the last such disagreement ever leaves the
    # declaration. TOOL-aSurfacedLexicon-7.
    want, gloss, source = "", "", ""
    graded_by_p1 = surface == PREDICATE_SURFACES["verb"] and bool(verbs)
    if graded_by_p1 and verb not in verbs:
        if verb in banned:
            want = banned[verb]
            gloss = (verbs.get(want) or "").strip()
            source = "the declaration says"
        else:
            rep, canon_gloss = read_debt_gloss(verb, None, clusters)
            if rep:
                want = rep
                gloss = (verbs.get(rep) or canon_gloss).strip()
                # Fork F2 of TOOL-aSurfacedLexicon-7, decided as its recommendation: propose the
                # representative even where this declaration does not carry it, and SAY SO.
                # Suppressing the advice leaves the author with a refusal and nothing else, which is
                # the defect this whole path exists to close; proposing it silently hands them a
                # name the gate reds on the next run.
                source = ("the shipped canon says" if rep in verbs else
                          "the shipped canon says (and this declaration carries NO row for it, so "
                          "it needs one first)")

    answer = render_swapped_name(graded, want) if want else graded
    # THE RENDERER IS REACHED FROM EVERY EXIT, not only from the banned-verb branch. A name whose
    # leading token IS declared used to return here with an `OK` line before any convention check
    # ran, and that quiet everyday path — nothing wrong but the case — is the one this verb answers
    # most often. F1, ratified as option A: a name the round trip cannot carry is NOT re-spelled.
    recased = render_convention(answer, conv)
    if recased and recased != answer:
        lines.append(f"re-cased to {conv} for cell `{cell}`, which `{answer}` does not satisfy"
                     + (f" (it satisfies {', '.join(sorted(classify(answer)))})"
                        if classify(answer) else ""))
        answer = recased
    elif not recased:
        lines.append(f"NOT re-cased: `{answer}` cannot be spelled in {conv} without inventing bytes "
                     f"the caller did not write — a character the splitter cannot see and {conv} "
                     f"does not re-supply, or a core no convention can carry. Fix it by hand.")

    if want:
        print(f"use `{answer}` — {source} `{want}`, NOT `{verb}`: {gloss}")
    elif graded_by_p1 and verb not in verbs:
        print(f"`{verb}` is not in the declared table, no row bans it by name, and the shipped "
              f"canon holds no cluster for it — so this is a SCOPING question, not a spelling one. "
              f"Declared verbs: {' '.join(sorted(verbs))}")
    elif answer != graded:
        print(f"use `{answer}` — cell `{cell}` declares {conv}, and `{graded}` does not satisfy it")
    elif not recased:
        print(f"`{graded}` does not satisfy {conv} for cell `{cell}`, and this verb will not "
              f"re-spell it")
    elif graded_by_p1:
        print(f"OK — {graded} leads with `{verb}`, which the declaration carries, and satisfies "
              f"{conv} for cell `{cell}`")
    else:
        print(f"OK — {graded} satisfies {conv} for cell `{cell}`")
    for line in lines:
        print(line)
    return 0


def run_expand(root: Path) -> int:
    """`--expand` — the one-time widening of the declared table, bounded by the frozen clusters.

    THE ONLY DIRECTION THIS KIT WILL PROPOSE IN. The corpus decides which concepts are LIVE here and
    decides nothing else; every proposed row is spelled by `canon.py`, element 0, at every frequency.
    A leading token no cluster holds cannot enter a proposal by any path, which is why the tail below
    is printed as EVIDENCE for an owner rather than offered as a candidate list. That closure is the
    whole difference between widening a vocabulary and legalising a habit, and it is what makes the
    guard three paragraphs up — that nothing here can turn what the corpus DOES into what it SHOULD
    do — survive a mode that exists to propose rows.

    READ-ONLY, and it returns before `check_pass` the way `--suggest` does: it prints no pin and
    cannot reach a waiver. Its exit codes are 0 on a tree it measured, 1 on a declaration that does
    not parse, and 2 when it could not measure at all — an absent scaffolder, or a corpus no armed
    extractor produced a definition from. The non-zero matters: the shell wrapper stops before
    `--stamp` on it, so a run that measured nothing cannot spend the one supported widening.

    The `expanded=` stamp and the already-expanded refusal both live in `adopt-lexicon.sh`, so the
    engine keeps NO write path to the file it grades — the risk tier this unit was priced at is
    "writes at most one scalar", and the scalar is not written here. TOOL-aSurfacedLexicon-10.
    """
    # LAZY, AND IT HAS TO BE — two reasons, and the first one is fatal rather than stylistic.
    # `scaffold_lexicon` imports THIS module at its own module scope and then reads `lex.KNOWN_EXTS`
    # in its module BODY, above which lexicon.py's own definition sits; a top-level import here
    # therefore raises `AttributeError` out of the sibling and lexicon.py stops importing at all,
    # reddening every leg that touches the kit. Second, a landed arm runs `--check` against a kit
    # copy with `scaffold_lexicon.py` DELETED and asserts it is green, so the import must not exist
    # on the default path either.
    #
    # AND IT LOADS A SECOND COPY OF THIS MODULE, which is worth knowing before somebody debugs it.
    # Run as a script this file is `__main__`, so the sibling's `import lexicon` finds nothing in
    # `sys.modules` and imports lexicon.py again under its own name. Harmless today — this module's
    # body is assignments and a `sys.path.insert`, with no I/O — but `lex.KNOWN_EXTS` inside the
    # scaffold is then a DIFFERENT object from the one this function holds, so nothing across that
    # boundary may be compared by identity.
    try:
        import scaffold_lexicon
    except ImportError as e:
        # The kit ships without the scaffolder in an adopter who took only the engine, and that is
        # a supported install rather than a defect. REPORTED, never a traceback, and never a silent
        # zero: the same posture `measure_pass` takes for its scaffold guard.
        print(f"lexicon: SCAFFOLDER ABSENT — `--expand` derives its proposal set from the same "
              f"closure the scaffolder uses, and that file is not installed beside this one ({e}). "
              f"Nothing was measured; this is not an empty proposal.")
        return 2

    kit = Path(__file__).resolve().parent
    conf_path = root / CONF_NAME
    if not conf_path.exists():
        # Carried from `run()` rather than inherited: a mode dispatched beside `--suggest` never
        # reaches run()'s NOT ADOPTED branch, and `load_conf` on a missing file raises.
        print(f"lexicon: NOT ADOPTED — no {CONF_NAME} at the repo root, so there is no table to "
              f"widen; the kit is opt-in and inert without one")
        return 0
    try:
        conf = load_conf(conf_path)
        declared = {ext: (pset, mode) for ext, pset, mode in langs(conf)}
        clusters = canon.build_clusters(conf.get("CANON") or {})
    except (ConfError, ValueError) as e:
        print(f"lexicon: {e}")
        return 1

    # ABOVE EVERYTHING, exactly as `run()` does it. A mode whose entire subject is what the frozen
    # clusters permit must not be the one run that stays silent about an owner having opened them.
    print_canon_posture(conf)

    verbs = conf.get("VERBS") or {}
    measured = measure_pass(root, kit, conf, declared, clusters)
    derived = scaffold_lexicon.derive_candidates(measured["scanned"], declared=verbs,
                                                 clusters=clusters)
    candidates, live = derived["candidates"], derived["live"]

    # AN EMPTY `live` HAS THREE CAUSES AND ONLY ONE OF THEM IS BENIGN, so the branch is split three
    # ways rather than two. Round 2 named the reassuring zero and round 3 found HALF its fix landed:
    # the guard gated on definitions EXTRACTED, which is a different population from `live`, so a
    # corpus whose walk read plenty of definitions and whose leading tokens are all off-canon sailed
    # past it into the benign sentence — a vacuously-true universal over an empty set, closing with
    # an explicit denial of the failure mode actually occurring. Two fixture corpora reach it.
    #
    # REFUSED rather than reported, and 2 rather than 0: the wrapper's `|| exit 1` means the non-zero
    # here is the only thing stopping `--stamp` spending the ONE supported widening on a corpus in
    # which nothing is live, which the already-expanded refusal then makes permanent.
    #
    # THE PREDICATE READS FUNCTION DEFINITIONS AND THE WORDS SAY SO. The first cut summed the verb
    # half and then spoke for the whole extraction, so a corpus of nothing but type definitions was
    # told no extractor produced a definition and sent to `--check`, which prints `graded=2` and
    # `lexicon OK` on that same tree. Round-2 F2, round-3 B1 and M1.
    graded_defs = sum(n for key, n in measured["graded"].items() if key[1] == "verb")
    types_seen = sum(n for key, n in measured["graded"].items() if key[1] == "suffix")
    # ARMED means armed, and `declared` is every declared row including the `dark` ones. Printing all
    # of them under that word contradicted the sentence above it in exactly the state the refusal
    # exists for — the first cause it offers is "every language may be declared `dark`", and the
    # evidence line appeared to rule that out. Derived the way `run()` derives its coverage fraction,
    # from the mode rather than from the key. Round-3 M2.
    # REPORTING SITE TWO of `resolve_extractor`'s four — the armed-extension tally. Derived the way
    # `check_pass` derives its coverage fraction, and now through the SAME predicate rather than
    # through a second spelling of it. TOOL-aGradedDialect-3 §8 F1.
    armed = sorted(e for e, (ps, m) in declared.items()
                   if resolve_extractor(m, ps, measured["sets"]) is not None)
    evidence = (f"  armed extension(s): {' '.join(armed) or '(none armed)'}\n"
                f"  extracted: {graded_defs} function definition(s) and {types_seen} type "
                f"definition(s) over {len(measured['files'])} tracked file(s)")
    if not graded_defs:
        print(f"EXPAND — NOTHING MEASURED, so there is nothing to propose FROM. No armed extractor "
              f"produced a FUNCTION definition over this corpus: every language may be declared "
              f"`dark`, an armed extension may have no files, or an extractor may have refused them. "
              f"An empty proposal here is the SYMPTOM, not the normal result — a cluster cannot be "
              f"voted live by a walk that found nothing to vote with.")
        print(evidence)
        return 2
    if not live:
        print(f"EXPAND — NOTHING LIVE, so there is nothing to propose FROM. The walk read "
              f"{graded_defs} function definition(s) and NOT ONE of them leads with a token any "
              f"cluster holds, so no concept is live here and the table cannot be widened from a "
              f"corpus that votes for nothing. The empty proposal is the SYMPTOM, and what this "
              f"corpus owes is renames rather than rows: `--list` prints every one of those "
              f"definitions with its site.")
        print(evidence)
        return 2

    if candidates:
        print(f"EXPAND — {len(candidates)} cluster(s) have a live site in this corpus and no row in "
              f"the declared table. Paste them INSIDE the `VERBS:` block, indented, and SHARPEN "
              f"every negative first: the glosses below are the shipped ones, and a row nobody "
              f"edited is the seed's problem arriving one table later.")
        for v in candidates:
            print(f"  {v:<9} {canon.read_gloss(v, clusters)}{canon.render_negative(v, clusters)}")
    else:
        print(f"EXPAND — nothing to propose. All {len(live)} cluster(s) with a live site in this "
              f"corpus already carry a row, so a widening bounded by the clusters can offer nothing "
              f"this declaration does not hold. That is the NORMAL result on an adopted repo and "
              f"not a run that failed to measure.")

    # THE TAIL, from the ENGINE's own classification and not a second predicate. `unruled` already
    # means "a leading token no cluster holds and no row names" everywhere else in this file, and it
    # is the number `--check` prints on every bar; re-deriving it here would be two answers to one
    # question with the copy nobody grades.
    #
    # OVER THE UNWAIVED SET, which is the same population `--check` splits and the pins ratchet. The
    # first cut read every offender and the comment above it still claimed parity with `--check` — so
    # a repo with one verb waiver got its already-accounted-for exception handed back as an
    # unresolved house idiom, and the divergence the comment names as the only risk arrived from the
    # other side of the function. This repo's waiver registry has no rows, so no corpus here can
    # observe it; a fixture arm pins which population the tail means. Round-2 review F5.
    tail: dict = {}
    for off in measured["unwaived"]["verb"]:
        if off.cls == "unruled" and off.verb:
            tail[off.verb] = tail.get(off.verb, 0) + 1
    rows = sorted(tail.items(), key=lambda kv: (-kv[1], kv[0]))
    # AND THE WAIVED COUNT IS STATED, because moving to the unwaived set aligned these rows with the
    # offender scalar and MISALIGNED them with the corpus-wide site census the engine attaches to
    # every unruled offender — two numbers for one question, printed by one tool. `check_pass` prints
    # `waived=N` on its own line for the same reason; an operator sizing a rename off an unqualified
    # tail undercounts by exactly the waived sites, which are still definitions leading with that
    # token. Round-3 L1.
    # The SAME predicate `measure_pass` splits on, spelled once here rather than a second membership
    # rule: an offender is waived exactly when its matched text is a key of the registry.
    _waived_texts = measured["waivers"]["verb"]
    waived_unruled = sum(1 for off in measured["offenders"]["verb"]
                         if off.cls == "unruled" and off.verb and off.text in _waived_texts)

    print("")
    print(f"NOT PROPOSALS — {len(rows)} leading token(s) across {sum(tail.values())} UNWAIVED "
          f"definition(s), with {waived_unruled} further definition(s) waived and not counted here "
          f"or in the rows below; `--list` counts a token's sites corpus-wide, waivers included, so "
          f"the two differ by exactly that number. They "
          f"lead with a word no cluster holds and no row names. THIS VERB WILL NEVER OFFER THEM, at "
          f"any frequency. A row here would be the corpus voting on its own commonest spellings, "
          f"which is the one shape a naming gate must not have, and it is the defect this kit was "
          f"rebuilt to close. They are printed as EVIDENCE: a token near the top is a house idiom "
          f"that either earns a hand-written row with a hand-written negative, or gets renamed "
          f"everywhere.")
    for v, n in rows[:20]:
        print(f"  {v:<14} {n} definition(s)")
    if len(rows) > 20:
        print(f"  ...and {len(rows) - 20} more; `--list` prints every one with its site.")

    print("")
    # THE COST, named rather than left for the next red bar to teach. NO PIN IS SPELLED HERE: the
    # scalars and the per-cell rows a declaration carries move with the units that add them, and a
    # message enumerating them is wrong on the commit after the one that wrote it. `--measure`
    # prints exactly the rows this conf produces, which is the same reason it exists.
    print(f"COST — every row you paste moves a pin. A newly declared verb stops being an offender, "
          f"so the offender scalars fall and so does every armed vocab cell's row; each pin is a "
          f"TWO-SIDED equality, so a drain nobody records reds the bar exactly as a rise does. "
          f"Re-measure and paste what it prints: python {resolve_self_path()} --measure")
    if measured["problems"]:
        print(f"NOTE — this declaration already reports {len(measured['problems'])} problem(s) that "
              f"`--check` names. The proposal above came off the same walk and is unaffected by "
              f"them, but a table that does not grade is a table to fix before widening.")
    return 0


def resolve_self_path() -> str:
    """This file's path AS THE OPERATOR WOULD TYPE IT, derived from `__file__` (S5).

    THE ONE HOME FOR THE LITERAL, and it is not a literal. This kit installs at whatever prefix an
    adopter chose, and `apply` writes gov's bytes VERBATIM — nothing substitutes into a file body
    anywhere — so a spelled `<prefix>/lexicon/lexicon.py` arrives unchanged in a tree that has no
    such path. Every usage string in this file routes through here, and the docstring's copy of the
    block was DELETED rather than fixed: two spellings of one invocation is the same defect with the
    harder half hidden in a comment.

    Relative to the repo root where that resolves, and to the file's own NAME where it does not — a
    file run from outside a checkout still prints something a reader can act on, rather than an
    absolute path from somebody else's disk.
    """
    here = Path(__file__).resolve()
    try:
        out = subprocess.run(["git", "-C", str(here.parent), "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True)
        if out.returncode == 0:
            return here.relative_to(Path(out.stdout.strip()).resolve()).as_posix()
    except (OSError, ValueError):
        pass
    return here.name


def main(argv: list[str]) -> int:
    me = resolve_self_path()
    mode = argv[1] if len(argv) > 1 else "--check"
    if mode not in ("--check", "--list", "--measure", "--suggest", "--expand"):
        # THE USAGE BLOCK LIVES HERE AND NOWHERE ELSE. It moved out of the module docstring, whose
        # copy spelled the install prefix six times and reached every adopter unchanged.
        sys.stderr.write(
            f"usage: python {me} "
            "[--check|--list|--measure|--suggest <name>|--expand]\n"
            "  --check            assert; non-zero on an unwaived offender\n"
            "  --list             print every offender, waived or not (authoring aid)\n"
            "  --measure          print the pins THIS conf produces; decide nothing\n"
            "  --suggest <name> --as <ext>.<surface>\n"
            "                     one line for ONE identifier, no corpus pass\n"
            "  --expand           propose the live clusters this table does not declare; writes\n"
            "                     nothing. The stamp lives in adopt-lexicon.sh --expand --stamp\n")
        return 2
    if mode == "--expand" and len(argv) > 2:
        # REFUSED RATHER THAN IGNORED. Every other mode here reads `argv[1]` and drops the rest, so
        # `--expand --stamp` would run a full expansion, write nothing, and report success — and
        # `--stamp` is exactly the word an operator will reach for, because the wrapper takes it.
        # A flag that silently does nothing is worse than one that does not exist.
        sys.stderr.write(f"usage: python {me} --expand\n"
                         f"  --expand takes no further arguments and writes nothing. The stamp is "
                         f"the WRAPPER's: adopt-lexicon.sh --expand --stamp, which also holds the "
                         f"refusal on a table that was already expanded.\n"
                         f"  got: {' '.join(argv[2:])!r}\n")
        return 2
    cell_spec = ""
    if mode == "--suggest":
        # `--as` IS REQUIRED AND IS NOT DEFAULTED (S1). The surface decides which predicates are
        # armed and which convention the answer is spelled in, so a default answers the whole
        # question silently for a caller who did not think about it.
        rest = argv[3:]
        if len(argv) > 3 and rest[0] == "--as" and len(rest) > 1:
            cell_spec = rest[1]
        if len(argv) < 3 or argv[2].startswith("--") or not cell_spec:
            sys.stderr.write(f"usage: python {me} --suggest <identifier> --as <ext>.<surface>\n"
                             "  --as is REQUIRED: the surface decides which predicates are armed "
                             "and which convention the answer is spelled in.\n")
            return 2
    out = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    if out.returncode != 0:
        sys.stderr.write("lexicon: not a git repo\n")
        return 2
    root = Path(out.stdout.strip())
    # The SUPPLY verb returns before `run()`, which is what keeps it off the gate path: it cannot
    # reach a pin, a waiver or an exit code of 1 even by accident.
    if mode == "--suggest":
        return run_suggest(root, argv[2], cell_spec)
    # The WIDENING verb returns here for the same reason the supply verb above does: it must not be
    # able to reach a pin or a waiver by any path, however the file is refactored. It is NOT the
    # supply verb's exit-code contract, and the parallel was drawn too wide here at first: `--suggest`
    # returns only 0 and 2, while this one also returns 1 on a declaration that does not parse and 2
    # on an absent scaffolder. The accurate contract lives on `run_expand` itself, which is where an
    # exit-code claim belongs. Round-2 review F8.
    if mode == "--expand":
        return run_expand(root)
    return run(root, list_mode=(mode == "--list"), measure_mode=(mode == "--measure"))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
