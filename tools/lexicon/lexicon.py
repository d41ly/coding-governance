#!/usr/bin/env python3
# gov:kit lexicon@1.1
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

    parser  a real parse (Python `ast`)   complete over its extension
    probe   a regex pattern set           incomplete BY CONSTRUCTION, reported as such every run
    dark    none, declared explicitly     named every run, never silently absent

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

from lexicon_conf import ConfError, langs, load_conf, build_negatives  # noqa: E402
from subtokens import leading_verb, subtokens  # noqa: E402

KIT_LEXICON_VERSION = "1.1"

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
KNOWN_EXTS = {"py": ("python-ast", "parser"), "js": ("js-regex", "probe")}

PIN_KEYS = {"verb": "VERB_OFFENDER_PIN", "suffix": "SUFFIX_OFFENDER_PIN"}

#: The predicate keys, in report order. ONE spelling, because there were four literal `("verb",
#: "suffix", "layer")` tuples in `run()` and a fifth in the tally loop — deleting a predicate meant
#: finding all of them.
KINDS = ("verb", "suffix")

#: The shipped `probe` pattern sets. Each one MUST have a frozen sentinel fixture in `selftest.py`
#: that yields a non-zero definition count, so a set going inert fails there rather than here.
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
#: It is a HEURISTIC and the README says so. It is not a lexer, it is not a step toward one, and
#: `TOOL-dScaffoldedMirror-13` still owns the `.ts`/`.tsx` question.
DEFINITION_SNIFF = re.compile(
    r"""^[ \t]*(?:
          (?:async[ \t]+)?def[ \t]+\w                     # python, ruby
        | (?:export[ \t]+)?(?:async[ \t]+)?function[ \t]+\w   # js, ts, php, shell `function f`
        | (?:export[ \t]+)?(?:abstract[ \t]+)?class[ \t]+\w   # js, ts, php, java, kotlin
        | (?:export[ \t]+)?(?:const|let|var)[ \t]+\w[\w$]*[ \t]*=[ \t]*(?:async[ \t]*)?\(  # js arrow
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
    waived line unpins it, which reds a merge that touched nothing the waiver guards."""

    __slots__ = ("kind", "path", "line", "text", "detail")

    def __init__(self, kind, path, line, text, detail):
        self.kind, self.path, self.line, self.text, self.detail = kind, path, line, text, detail

    def __str__(self):
        return f"{self.path}:{self.line}: {self.kind}: {self.text} — {self.detail}"


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


def _probe_defs(src: str, pset: str):
    spec = PATTERN_SETS[pset]

    def hits(key):
        out = []
        for rx in spec[key]:
            for m in rx.finditer(src):
                out.append((m.group(1), src.count("\n", 0, m.start()) + 1))
        return out

    return hits("functions"), hits("types"), hits("imports")


def extract_text(src: str, mode: str, pset: str):
    """`(functions, types, imports)` for SOURCE TEXT, or `None` when the mode declares no extractor.

    Split out of `extract` so a caller holding BYTES rather than a path uses the SAME extractor.
    `drift-audit`'s marginal-offense-rate signal derives its two operands from git blobs at two shas
    and never writes a tree; a second implementation there would be the
    `second-implementation-is-not-a-second-opinion` class inside the one instrument whose entire
    value is that both of its operands come from one extractor. TOOL-dScaffoldedMirror-7 S4.
    """
    if mode == "dark":
        return None
    if mode == "parser":
        return _python_defs(src)
    return _probe_defs(src, pset)


def extract(path: Path, mode: str, pset: str):
    """`(functions, types, imports)` for one file, or `None` when the mode declares no extractor."""
    if mode == "dark":
        return None
    return extract_text(path.read_text(encoding="utf-8", errors="replace"), mode, pset)


def scan_corpus(root: Path, declared: dict):
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
    for rel in tracked_files(root):
        ext = ext_of(rel)
        pset, mode = declared.get(ext, ("", "dark"))
        if mode == "dark":
            yield rel, ext, None, None
            continue
        if mode == "probe" and pset not in PATTERN_SETS:
            yield rel, ext, None, (f"LANGS declares pattern set {pset!r} for .{ext}, which this kit "
                                   f"does not ship")
            continue
        try:
            defs = extract(root / rel, mode, pset)
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
    siblings = {p.stem for p in mods}
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


def measure_pass(root: Path, kit: Path, conf: dict, declared: dict) -> dict:
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
    banned = tuple(t for t in (conf.get("BANNED_SUFFIXES") or "").split() if t)

    # THE ONE WALK, materialised because the population is read four times below — for the declared
    # surface, for the DEAD PROBE corpus test, for the coverage denominator and for the OK line.
    scanned = list(scan_corpus(root, declared))
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
                offenders["verb"].append(Offender(
                    "P1 verb", rel, lineno, name,
                    f"leading token {verb!r} is not in the declared VERBS table"))

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

    return {
        "problems": problems,
        "graded": graded,
        "offenders": offenders,
        "waivers": waived_by,
        "unwaived": unwaived_by,
        "pins": pins_by_kind,
        "declared": declared,
        "files": files,
        "carriers": carriers,
        "self_mods": self_mods,
        "self_imports": self_imports,
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
        pin = measured["pins"][kind]
        if len(unwaived) > pin:
            exit_code = 1
            print(f"lexicon: {kind} offenders {len(unwaived)} over pin {pin}:")
            for o in unwaived[:40]:
                print(f"  {o}")
            if len(unwaived) > 40:
                print(f"  … and {len(unwaived) - 40} more")

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
        print(f"lexicon: {label[kind]} graded={g} offenders={off} waived={wv}")

    # THE SELF-CONTAINMENT POPULATION, on green as well as on red, and deliberately NOT shaped like
    # the two rows above: this is a refusal with a measured reach, not a third declared predicate.
    # Printing it is what makes the absence of a refusal a measurement rather than a mood — and
    # printing alone is not enough, which is why a zero here is a `DEAD PROBE` refusal above.
    print(f"lexicon: self-contained — judged {measured['self_imports']} import(s) over "
          f"{measured['self_mods']} module(s) beside the engine")

    # S2 — a REPORT, not a refusal. An armed pair that grades nothing is NAMED so the zero is
    # legible; it does not red. `.js` here is armed and has no classes at all, which is a repo
    # that does not write JavaScript classes rather than an extractor that went inert — and the
    # inert case is owned by the frozen SENTINELS fixture in this kit's own selftest, which can
    # tell the two apart where a single tree cannot. See the spec's section 4.
    # S1/S2 — the coverage fraction, on every run. The armed share of the files that actually
    # carry a definition, which is the number a `LANGS` edit moves and nothing else reported.
    carriers = measured["carriers"]
    armed_exts = {e for e, (ps, m) in declared.items()
                  if m == "parser" or (m == "probe" and ps in PATTERN_SETS)}
    armed_carriers = {f for f in carriers if ext_of(f) in armed_exts}
    pct = (100.0 * len(armed_carriers) / len(carriers)) if carriers else 0.0
    print(f"lexicon: coverage — armed {len(armed_carriers)} of {len(carriers)} "
          f"definition-carrying file(s) ({pct:.1f}%)")

    empty = [f".{e} {k}=0" for (e, k), v in sorted(graded.items()) if v == 0]
    if empty:
        print("lexicon: armed but grading nothing (reported, not a refusal): " + ", ".join(empty))

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
    except ConfError as e:
        print(f"lexicon: {e}")
        return 1

    measured = measure_pass(root, kit, conf, declared)
    problems = measured["problems"]

    if measure_mode:
        # `--measure` prints the counts THIS conf produces and decides nothing beyond its own
        # refusals. S4 — the exit code these conditions always described. UNDECLARED EXTENSIONS,
        # DEAD PROBE and STALE WAIVERS rode as `# NOTE:` comments under an unconditional 0, so
        # `--measure` could not fail. Three later units use it as a discharge probe, and a probe
        # that cannot fail discharges nothing. NOT SELF-CONTAINED and its own DEAD PROBE join them.
        for kind in KINDS:
            print(f'{PIN_KEYS[kind]}="{len(measured["unwaived"][kind])}"')
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


def run_suggest(root: Path, name: str) -> int:
    """S1 — one deterministic line for ONE identifier. Reads the declaration and nothing else.

    NO CORPUS PASS, deliberately and measurably: the whole value is that an author can ask before
    writing, and a verb that walks 900 files to answer one question is a verb nobody waits for.
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

    verb = leading_verb(name)
    if not verb:
        print(f"lexicon: {name} has no word characters, so it is ungradeable rather than wrong")
        return 0
    if verb in verbs:
        print(f"OK — {name} leads with `{verb}`, which the declaration carries")
        return 0

    banned = build_banned_index(conf)
    # THE TAIL IS THE ORIGINAL SURFACE, SLICED. It is never re-derived, and two review rounds were
    # needed to land on that. Round 1 found the tail sliced by `len(verb)` while `leading_verb` had
    # stripped the leading underscores first, so the two disagreed about where the verb ended and
    # `_fetch_conf` suggested `_load_h_conf`. Round 2 found that rebuilding the tail out of
    # `subtokens()` -- the round-1 fix -- traded that for worse: the splitter lowercases, breaks
    # acronym runs, splits digit boundaries and drops anything outside its character class, so
    # `getUserURLs` came back as `readUserUrLs`, `fetch_v2_data` as `load_v_2_data` and `create$data`
    # as `build_data` with the `$` silently gone. Three of those had been CORRECT before the fix.
    #
    # Slicing at the end of the FIRST SUBTOKEN's own surface is what both rounds were reaching for.
    # The splitter decides where the verb ends, which is the half round 1 had right; nothing
    # downstream re-spells a character the caller wrote, which is the half round 2 had right.
    # Separator style, case, acronym runs, digit suffixes, trailing underscores and characters the
    # splitter cannot even see all survive, because not one of them is ever regenerated.
    lead = name[:len(name) - len(name.lstrip("_"))]
    body = name[len(lead):]
    _toks = subtokens(name)
    _first = _toks[0] if _toks else ""
    if not _first or body[:len(_first)].lower() != _first:
        # The splitter and the surface disagree. `leading_verb`'s contract allows that for a name
        # with no word characters; suggest the bare verb rather than invent a tail for it.
        surface, rest = "", ""
    else:
        surface, rest = body[:len(_first)], body[len(_first):]
    if verb in banned:
        want = banned[verb]
        gloss = (verbs.get(want) or "").strip()
        # THE VERB INHERITS THE CASE OF THE TOKEN IT REPLACES, so a SCREAMING_SNAKE name is not
        # answered in lower snake and a PascalCase one is not answered in camelCase. Round 1 answered
        # every shape in the declaration's own lowercase, which is a second way of handing back a
        # name whose only remaining defect is that the author must edit it before typing it.
        if len(surface) > 1 and surface.isupper():
            want_cased = want.upper()
        elif surface[:1].isupper():
            want_cased = want[:1].upper() + want[1:]
        else:
            want_cased = want
        swap = lead + want_cased + rest
        print(f"use `{swap}` — the declaration says `{want}`, NOT `{verb}`: {gloss}")
    else:
        print(f"`{verb}` is not in the declared table, and no row bans it by name. "
              f"Declared verbs: {' '.join(sorted(verbs))}")
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
    if mode not in ("--check", "--list", "--measure", "--suggest"):
        # THE USAGE BLOCK LIVES HERE AND NOWHERE ELSE. It moved out of the module docstring, whose
        # copy spelled the install prefix six times and reached every adopter unchanged.
        sys.stderr.write(
            f"usage: python {me} "
            "[--check|--list|--measure|--suggest <name>]\n"
            "  --check            assert; non-zero on an unwaived offender\n"
            "  --list             print every offender, waived or not (authoring aid)\n"
            "  --measure          print the pins THIS conf produces; decide nothing\n"
            "  --suggest <name>   one line for ONE identifier, no corpus pass\n")
        return 2
    if mode == "--suggest" and len(argv) < 3:
        sys.stderr.write(f"usage: python {me} --suggest <identifier>\n")
        return 2
    out = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    if out.returncode != 0:
        sys.stderr.write("lexicon: not a git repo\n")
        return 2
    root = Path(out.stdout.strip())
    # The SUPPLY verb returns before `run()`, which is what keeps it off the gate path: it cannot
    # reach a pin, a waiver or an exit code of 1 even by accident.
    if mode == "--suggest":
        return run_suggest(root, argv[2])
    return run(root, list_mode=(mode == "--list"), measure_mode=(mode == "--measure"))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
