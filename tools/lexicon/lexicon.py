#!/usr/bin/env python3
# gov:kit lexicon@1.1
"""lexicon.py — three naming predicates over a DECLARED vocabulary.

    python tools/lexicon/lexicon.py            # assert; non-zero on an unwaived offender
    python tools/lexicon/lexicon.py --list     # print every offender, waived or not (authoring aid)
    python tools/lexicon/lexicon.py --measure  # print the three pins THIS conf produces; decide nothing
    python tools/lexicon/lexicon.py --suggest <name>   # one line for ONE identifier, no corpus pass
    python tools/lexicon/lexicon.py --brief <path>     # how the corpus already spells this file's objects
    python tools/lexicon/lexicon.py --probe            # what the canon would propose here; read-only, exits 0

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
population passes green forever and tells you nothing. Three checks push back, and the third is
narrower than an earlier version of this docstring claimed:

  DEAD PROBE          a parser/probe language whose definition population is empty against a corpus
                      containing that extension — an extractor that has gone inert
  frozen SENTINELS    a fixture per shipped pattern set in `selftest.py`, because the corpus-side
                      arm above is itself defeated by an empty corpus
  UNSELECTIVE RULE    a LAYERS rule whose FROM or TO glob matches no tracked file

WHAT IS NOT CHECKED, said plainly because the previous version of this file claimed it was. There
is no proof that a non-empty, selective rule can actually FIRE. One was attempted and it was a
tautology: every synthetic import target derived from a real file's PATH round-trips through the
resolver's own path-mirroring reading, so the check certified every rule — including, MEASURED,
under the pre-fix resolver whose blindness it had been written to catch. A vacuity check that is
itself vacuous is worse than none, because it gets cited as coverage.

What P3's correctness actually rests on is `resolve_import` plus fixtures written in the PRODUCTION
shape — a hyphenated directory reached by a bare-stem import, which is the case the first
implementation could not see and no path-shaped fixture would have caught. Those live in
`selftest.py`. The general question is `memory/gotchas/armed-but-unreachable-rule.md`, and it is a
REVIEW question: no predicate here can decide reachability for a rule type it has never seen.

HOW IMPORT RESOLUTION WORKS, and why it is shaped this way. Four review rounds each found a blocker
here, so the rules are written down rather than left to be re-derived:

  LANGUAGE FIRST      the importer's extension decides what a dot MEANS. An earlier cut branched on
                      `"." in target`, a Python namespace rule, and applied it to JavaScript.
  RELATIVE            `./` and `../` resolve against the importer's directory; in Python a LEADING
                      DOT is relative-to-package and `node.level` carries the depth. Escaping the
                      repo root yields NOTHING — clamping it back in can fabricate a crossing.
  DOTTED (python)     names its package from the root, so the importer's directory gets no
                      precedence — but a candidate must be PATH-CONSISTENT with the dots, or the
                      stem lookup degenerates into "any file with this basename" and third-party
                      imports red as crossings.
  BARE (python)       the flat `sys.path`-insert shape, and the only one where the importer's own
                      directory legitimately wins.
  EVERY OTHER LANG    a bare specifier is a package PATH; its dots are part of a name.

Candidates are matched at PATH BOUNDARIES throughout. A bare `startswith` was the same defect class
the glob anchoring removed, living on in the sibling helper.

THE CASE TABLES IN `selftest.py` ARE THE INSTRUMENT. Every defect in this file's history lived in
`_glob_match` or `resolve_import` and NONE was visible to an end-to-end fixture — reverting one fix
verbatim once left all 48 fixture arms green while the live gate stayed at exit 0. Each fix is
verified by reverting it and watching a NAMED row red; three rows that did not do so were rewritten
or relabelled, and one row's stated property is documented as weaker than its neighbour's. When
extending either function, add rows FIRST.
"""

import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lexicon_conf import ConfError, langs, load_conf, build_negatives  # noqa: E402
import canon  # noqa: E402
from subtokens import leading_verb, subtokens  # noqa: E402

KIT_LEXICON_VERSION = "1.1"

CONF_NAME = ".lexicon.conf"
WAIVER_FILES = {
    "verb": "lexicon-verb-waivers.txt",
    "suffix": "lexicon-suffix-waivers.txt",
    "layer": "lexicon-layer-waivers.txt",
}
#: The extensions this kit can extract, and the ONE place they are declared. `scaffold_lexicon.py`
#: imports this rather than keeping its own copy: the two had ALREADY diverged on the `py` pattern
#: set (`""` here against `"python-ast"` there) within one build, so a probe against a repo with no
#: declaration graded python through a different code path than the scaffold that would adopt it.
#: Closing review M7.
KNOWN_EXTS = {"py": ("python-ast", "parser"), "js": ("js-regex", "probe")}

PIN_KEYS = {"verb": "VERB_OFFENDER_PIN", "suffix": "SUFFIX_OFFENDER_PIN", "layer": "LAYER_OFFENDER_PIN"}

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
            # crossing spelling in Python invisible to P3. `node.level` carries the leading dots of
            # a relative import and is preserved here rather than silently flattened.
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


def _build_glob_rx(pattern: str) -> str:
    """Glob -> regex source. ONE spelling of the conversion, because there were two and they
    disagreed: the nesting branch below escaped the RAW pattern, so any wildcard EARLIER in it
    became a literal asterisk and nesting silently stopped matching below depth 1. Measured, under
    `apps/*/internal/*`: the identical import red at depth 1 and passed GREEN at depth 2.

    THE DIALECT, stated because it is a choice and not a standard: `*` matches within one segment,
    `**` crosses segments, `?` is exactly one non-separator character. `**` is substituted FIRST —
    left to the single-star rule it collapsed to `[^/]*[^/]*`, so `<dir>/**` selected strictly LESS
    than `<dir>/*`, which is the opposite of what every reader expects.
    """
    out = re.escape(pattern).replace(r"\*\*", "\x00")
    out = out.replace(r"\*", "[^/]*").replace(r"\?", "[^/]")
    return out.replace("\x00", ".*")


def _check_path_suffix(path: str, suffix: str) -> bool:
    """Does `path`, minus its extension, end with `suffix` AT A PATH BOUNDARY?

    This is what makes a dotted import target mean something. Without it, `concurrent.helper` and
    `thirdparty.helper` — imports touching nothing in the repo — resolved onto any file whose stem
    happened to be `helper` and RED as layer crossings. A false positive there is worse than the
    false negative it replaced: the only escape is a waiver, and that waiver then permanently
    silences the genuine violation it is hiding.
    """
    base = path.rsplit("/", 1)[-1]
    stem_path = path[: -(len(base) - base.rfind("."))] if "." in base else path
    return stem_path == suffix or stem_path.endswith("/" + suffix)


def _glob_match(path: str, pattern: str) -> bool:
    """Fully ANCHORED. A `<dir>/*` pattern also matches anything nested under `<dir>/`.

    An earlier cut fell back to an UNANCHORED `re.match(rx, path)`, which accepts any path merely
    STARTING with the pattern's literal prefix — so `tools/codebase-map//codebase-map/conf` matched
    `tools/codebase-map/*`. That is how a since-removed reachability arm certified itself: it fed the
    matcher a mangled synthetic no import could ever spell, and the sloppy prefix accepted it.

    Both defects lived here, and neither was visible to any end-to-end fixture. The arms are a direct
    CASE TABLE in `selftest.py`.
    """
    if re.fullmatch(_build_glob_rx(pattern), path):
        return True
    if pattern.endswith("/*"):
        return re.fullmatch(_build_glob_rx(pattern[:-1]) + ".*", path) is not None
    return False


def build_module_index(files: list[str]) -> dict[str, list[str]]:
    """`{module-stem: [repo paths]}` over the tracked corpus, for P3's resolver.

    A LAYERS glob is spelled as a repo PATH. An import target is a NAMESPACE. Turning one into the
    other by swapping dots for slashes only works when the two happen to coincide, and it silently
    fails whenever they do not — most importantly when a directory name contains a character no
    module name may contain. `tools/codebase-map/` is exactly that case: no Python import can ever
    produce the hyphen, so a rule naming it was unmatchable by construction and P3 reported a clean
    zero over a population it could not select. That is the vacuous-selector class this kit's own
    docstring names as its dominant failure mode.
    """
    index: dict[str, list[str]] = {}
    for rel in files:
        base = rel.rsplit("/", 1)[-1]
        stem = base.rsplit(".", 1)[0] if "." in base else base
        index.setdefault(stem, []).append(rel)
    return index


def _resolve_relative(spec: str, here: str, index, ext: str) -> list[str]:
    """A `./`-or-`../` specifier against the importer's directory. `[]` means it escapes the repo.

    ESCAPING IS EXTERNAL, NOT CLAMPED. The first cut silently ignored a `..` with nothing left to
    pop, so `../../../outside/thing.js` landed back inside the tree and could FABRICATE a crossing
    against a path the import never names.
    """
    stack: list[str] = [p for p in here.split("/") if p]
    for part in [p for p in spec.split("/") if p not in ("", ".")]:
        if part == "..":
            if not stack:
                return []
            stack.pop()
        else:
            stack.append(part)
    cand = "/".join(stack)
    out = [cand]
    # BOUNDARY, not prefix: a bare `startswith` is the same defect the glob anchoring removed, and
    # it let `../shared/thing` resolve onto `web/shared/thingamajig.js`.
    out.extend(p for p in index.get(cand.rsplit("/", 1)[-1], [])
               if ext_of(p) == ext and _check_path_suffix(p, cand))
    return out


def resolve_import(target: str, importer: str, index: dict[str, list[str]]) -> list[str]:
    """Candidate repo paths an import target may denote. Empty means EXTERNAL or unresolvable, which
    is not a violation — a rule can only forbid what it can locate.

    LANGUAGE-AWARE, and that is the correction. An earlier cut branched on `"." in target`, which is
    a PYTHON namespace rule: it treated the JS package specifier `lodash.debounce` as a dotted module
    path and stripped its importer-local precedence. A dot means different things in different
    languages and the importer's extension is what says which.
    """
    here = importer.rsplit("/", 1)[0] if "/" in importer else ""
    ext = ext_of(importer)

    if target.startswith("./") or target.startswith("../"):
        return _resolve_relative(target, here, index, ext)

    if ext == "py":
        # A leading dot is a RELATIVE package import: one dot is this package, each extra dot walks
        # up one. `node.level` is preserved by the extractor precisely so this is decidable.
        if target.startswith("."):
            level = len(target) - len(target.lstrip("."))
            rest = target[level:].replace(".", "/")
            up = "../" * (level - 1)
            return _resolve_relative("./" + up + rest, here, index, ext)

        if "." in target:
            # A dotted target names its own package FROM THE ROOT, so the importer's directory gets
            # no precedence — but the candidate must be PATH-CONSISTENT with the dots, or the stem
            # lookup degenerates into "any file with this basename".
            dotted = target.replace(".", "/")
            out = [dotted]
            out.extend(p for p in index.get(target.rsplit(".", 1)[-1], [])
                       if ext_of(p) == ext and _check_path_suffix(p, dotted))
            return out

        # A BARE name is the flat `sys.path`-insert shape — the commonest one in this tree, and the
        # only one where the importer's own directory legitimately wins.
        hits = [p for p in index.get(target, []) if ext_of(p) == ext]
        local = [p for p in hits if (p.rsplit("/", 1)[0] if "/" in p else "") == here]
        return local or hits

    # Every other language: a bare specifier is a PACKAGE PATH, and its dots are part of a name
    # rather than separators. Resolve it as a path and by its final segment's stem; anything that
    # denotes nothing tracked is external, which is not a violation.
    out = [target]
    tail = target.rsplit("/", 1)[-1]
    stem = tail.rsplit(".", 1)[0] if "." in tail else tail
    out.extend(p for p in index.get(stem, []) if ext_of(p) == ext and _check_path_suffix(p, target))
    return out


def check_layer_violation(rel: str, target: str, layers, index) -> tuple[str, str] | None:
    """The `(from, to)` rule this import breaks, or None."""
    for frm, to in layers:
        if not _glob_match(rel, frm):
            continue
        for cand in resolve_import(target, rel, index):
            if _glob_match(cand, to):
                return (frm, to)
    return None


def scan_unselective_rules(layers, files: list[str], index) -> list[tuple[str, str, str]]:
    """LAYERS rules whose globs SELECT NOTHING. States exactly that and no more.

    WHAT THIS IS NOT, stated first because the previous version claimed it. This does NOT prove a
    rule is reachable. It cannot: any synthetic import target derived from the target's own PATH
    round-trips through the resolver's path-mirroring reading, so a construction-based proof
    certifies every rule — MEASURED, by restoring the pre-fix resolver, which this arm still
    declared REACHABLE. The construction branch was a tautology dressed as a defence, and a
    vacuity check that is itself vacuous is worse than none, because it is cited as coverage.

    What a rule's reachability actually rests on is the RESOLVER, and the only honest evidence for
    that is an OBSERVED failing case plus fixtures in `selftest.py` written in the PRODUCTION shape
    — a hyphenated directory reached by a bare-stem import. Those exist and are what this kit
    stands on; see the `armed-but-unreachable-rule` class for the general question, which no
    predicate here can answer for a rule type it has not seen.

    What IS checkable is emptiness at both ends, and it does fire: it caught five of this kit's own
    fixtures declaring a rule they had no files to express.
    """
    bad = []
    for frm, to in layers:
        if not any(_glob_match(f, frm) for f in files):
            bad.append((frm, to, f"the FROM glob {frm!r} matches no tracked file"))
        elif not any(_glob_match(f, to) for f in files):
            bad.append((frm, to, f"the TO glob {to!r} matches no tracked file"))
    return bad


def run(root: Path, list_mode: bool = False, measure_mode: bool = False) -> int:
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

    verbs = conf.get("VERBS") or {}
    banned = tuple(t for t in (conf.get("BANNED_SUFFIXES") or "").split() if t)
    layers = conf.get("LAYERS") or []
    files = tracked_files(root)

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
    present = sorted({ext_of(f) for f in files})
    missing = [e for e in present if e not in declared]
    if missing:
        problems.append("UNDECLARED EXTENSIONS (declare each in LANGS, `dark` if nothing extracts it): "
                        + ", ".join(missing))

    module_index = build_module_index(files)

    if not layers:
        problems.append("P3 NOT ARMED — LAYERS is empty. An unarmed predicate is a refusal, never a "
                        "green run: declare a forbidden import direction, or remove the conf to "
                        "un-adopt the kit entirely.")
    else:
        # EMPTINESS ONLY. This does NOT establish that a selective rule can fire — see the module
        # docstring for the tautology that claim rode on, and the KNOWN DEFECTS note there.
        for frm, to, why in scan_unselective_rules(layers, files, module_index):
            problems.append(f"UNSELECTIVE LAYERS RULE `{frm} -> {to}` — {why}. A rule whose globs "
                            f"select nothing cannot fire, so its offender count is a 0 no edit "
                            f"can move.")

    # --- extraction, with the vacuity arm ----------------------------------------------------
    offenders: dict[str, list[Offender]] = {"verb": [], "suffix": [], "layer": []}
    # S1 — keyed on (extension, PREDICATE), never on extension alone. The fold this replaces
    # summed functions and types into one number, so `.js` reported a healthy 89 while P2 graded
    # ZERO JavaScript classes and nothing could say so. A population is per-predicate or it is
    # not a population — the predicate is what decides which definitions were even eligible.
    graded: dict[tuple[str, str], int] = {}
    extractor_carriers: set[str] = set()   # files an ARMED extractor found a definition in

    for rel in files:
        ext = ext_of(rel)
        if ext not in declared:
            continue
        pset, mode = declared[ext]
        if mode == "dark":
            continue
        if mode == "probe" and pset not in PATTERN_SETS:
            problems.append(f"LANGS declares pattern set {pset!r} for .{ext}, which this kit does not ship")
            continue
        try:
            got = extract(root / rel, mode, pset)
        except SyntaxError as e:
            problems.append(f"{rel}: declared `{mode}` but does not parse: {e}")
            continue
        if got is None:
            continue
        funcs, types_, imports = got
        graded[(ext, "verb")] = graded.get((ext, "verb"), 0) + len(funcs)
        graded[(ext, "suffix")] = graded.get((ext, "suffix"), 0) + len(types_)
        graded[(ext, "layer")] = graded.get((ext, "layer"), 0) + len(imports)
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

        for target, lineno in imports:
            hit = check_layer_violation(rel, target, layers, module_index)
            if hit:
                offenders["layer"].append(Offender(
                    "P3 layer", rel, lineno, f"{rel}->{target}",
                    f"forbidden import direction {hit[0]} -> {hit[1]}"))

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
        if any(ext_of(f) == ext for f in files) and not ext_total:
            problems.append(f"DEAD PROBE — .{ext} is declared `{mode}`"
                            + (f" ({pset})" if pset else "")
                            + " and the corpus contains it, but the extractor found NO definitions. "
                              "An extractor that selects an empty population passes green forever.")

    # `--measure` — print the three counts THIS conf produces and decide nothing.
    #
    # `--scaffold` measures against the DERIVED seed, and the whole point of the seed is that a human
    # then rewrites it. Every pin it wrote was therefore a pre-curation number, and without this verb
    # the only way to re-measure after curating was to read the failure output of a red gate. That is
    # how a pin ends up asserted rather than measured — and two of these three shipped as a hardcoded
    # `"0"` under a comment that called them MEASURED.
    # HOISTED ABOVE `--measure`, and H1 of the closing review is why. The waiver load, the STALE
    # detection and the pin parse used to live BELOW the `measure_mode` return, so two of the four
    # conditions the comment there names could never reach `problems` on that path: `--measure`
    # printed three pins and exited 0 over a tree carrying dead waivers, while `--check` on the same
    # tree exited 1 naming them. An operator re-measuring after curation pasted a pin derived from a
    # corpus whose silencers no longer matched anything. Same armed-but-unreachable shape as the
    # DEAD SNIFFER defect, in the commit whose own comment claimed the opposite.
    waived_by: dict[str, dict] = {}
    unwaived_by: dict[str, list] = {}
    for kind in ("verb", "suffix", "layer"):
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
            int(pin_raw) if str(pin_raw).strip() else 0
        except ValueError:
            problems.append(f"{PIN_KEYS[kind]}={pin_raw!r} is not an integer")

    if measure_mode:
        for kind in ("verb", "suffix", "layer"):
            print(f'{PIN_KEYS[kind]}="{len(unwaived_by[kind])}"')
        if problems:
            print("# NOTE: the run also reported problems that are not pin-counted:")
            for p in problems:
                print(f"#   {p}")
        # S4 — the exit code these four conditions always described. UNDECLARED EXTENSIONS, DEAD
        # PROBE, UNSELECTIVE LAYERS RULE and STALE WAIVERS rode as `# NOTE:` comments under an
        # unconditional 0, so `--measure` could not fail. Three later units use it as a discharge
        # probe, and a probe that cannot fail discharges nothing.
        return 1 if problems else 0

    # --- waivers, pins, verdict ---------------------------------------------------------------
    exit_code = 0
    tally: dict[str, tuple[int, int, int]] = {}
    for kind in ("verb", "suffix", "layer"):
        waivers = waived_by[kind]
        found = offenders[kind]
        unwaived = unwaived_by[kind]

        if list_mode:
            for o in found:
                print(("  waived " if o.text in waivers else "  ") + str(o))

        tally[kind] = (sum(v for (_e, k), v in graded.items() if k == kind),
                       len(unwaived), len(found) - len(unwaived))
        pin_raw = conf.get(PIN_KEYS[kind], "")
        try:
            pin = int(pin_raw) if str(pin_raw).strip() else 0
        except ValueError:
            pin = 0
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
    label = {"verb": "P1 verb  ", "suffix": "P2 suffix", "layer": "P3 layer "}
    for kind in ("verb", "suffix", "layer"):
        g, off, wv = tally[kind]
        print(f"lexicon: {label[kind]} graded={g} offenders={off} waived={wv}")

    # S2 — a REPORT, not a refusal. An armed pair that grades nothing is NAMED so the zero is
    # legible; it does not red. `.js` here is armed and has no classes at all, which is a repo
    # that does not write JavaScript classes rather than an extractor that went inert — and the
    # inert case is owned by the frozen SENTINELS fixture in this kit's own selftest, which can
    # tell the two apart where a single tree cannot. See the spec's section 4.
    # S1/S2 — the coverage fraction, on every run. The armed share of the files that actually
    # carry a definition, which is the number a `LANGS` edit moves and nothing else reported.
    carriers = scan_definition_carriers(root, files)
    armed_exts = {e for e, (ps, m) in declared.items()
                  if m == "parser" or (m == "probe" and ps in PATTERN_SETS)}
    armed_carriers = {f for f in carriers if ext_of(f) in armed_exts}
    pct = (100.0 * len(armed_carriers) / len(carriers)) if carriers else 0.0
    print(f"lexicon: coverage — armed {len(armed_carriers)} of {len(carriers)} "
          f"definition-carrying file(s) ({pct:.1f}%)")

    # S6 — the sniffer's liveness, and rev-3 corrects rev-1 on WHAT it asserts. rev-1 wanted "some
    # dark extension carries a definition", which reds an honest adopter whose dark extensions are
    # all data files — the same defect `TOOL-dScaffoldedMirror-2` had to fix in DEAD PREDICATE.
    # What is falsifiable without that flaw is AGREEMENT: every file an ARMED extractor found a
    # definition in must also sniff positive. Two independent readings of one population, and a
    # sniffer that has gone blind contradicts the extractors rather than merely reporting zero.
    # PRINTS AND SETS THE CODE HERE, not via `problems`. The first cut appended to that list, which
    # is already printed and already folded into `exit_code` forty lines above — so this refusal could
    # never fire and a staged break proved it: blinding the sniffer left the run at exit 0. A refusal
    # registered after its own reader has run is the armed-but-unreachable class, and the only thing
    # that caught it was observing the break rather than reasoning about it.
    blind = sorted(extractor_carriers - carriers)
    if blind:
        exit_code = 1
        print(f"lexicon: DEAD SNIFFER — the coverage sniffer found no definition in {len(blind)} "
              f"file(s) where an ARMED extractor did (e.g. {blind[0]}). The denominator is "
              f"undercounting, which reports coverage as BETTER than it is.")

    empty = [f".{e} {k}=0" for (e, k), v in sorted(graded.items()) if v == 0]
    if empty:
        print("lexicon: armed but grading nothing (reported, not a refusal): " + ", ".join(empty))

    if exit_code == 0:
        modes = ", ".join(f".{e}={m}" for e, (_, m) in sorted(declared.items()))
        print(f"lexicon OK — {len(files)} tracked file(s); coverage: {modes}")
    return exit_code



# ============================================================================================
# TOOL-dScaffoldedMirror-10 — SUPPLY. The half of this kit with a measured record.
#
# Since the declaration landed, this repo added 136 definitions and zero offenders over a window in
# which the gate refused NOTHING. That half works by delivering context, and it was delivered by a
# session happening to open the conf. These two verbs hand the table to the author instead.
#
# THE GUARDS ARE STRUCTURAL, NOT STATED (S6). Section 12 of the charter bans a GATE whose vocabulary
# is a mirror of the code it grades. Neither verb below is a gate: neither can exit 1, neither prints
# a pin, and nothing in `scaffold_lexicon.py` imports either — so what the corpus DOES can never
# become what the corpus SHOULD do by a path anyone can take. A promise would not survive a refactor;
# the absence of a return path does.
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
    # THE TAIL COMES FROM THE SAME SPLITTER THE VERB DID. Slicing the raw name by `len(verb)` is
    # wrong whenever the two disagree about where the verb starts: `leading_verb` strips leading
    # underscores first, so `_fetch_conf` sliced to `h_conf` and the suggestion dropped the object
    # entirely. And the rejoin followed no convention: `getUserData` came back as `read_UserData`,
    # gluing a camelCase tail after an underscore. Closing review M4 and M5.
    lead = name[:len(name) - len(name.lstrip("_"))]
    tail_tokens = subtokens(name)[1:]
    body = name.lstrip("_")
    camel = "_" not in body and body != body.lower()
    if not tail_tokens:
        rest = ""
    elif camel:
        rest = "".join(t[:1].upper() + t[1:] for t in tail_tokens)
    else:
        rest = "_".join(tail_tokens)
    if verb in banned:
        want = banned[verb]
        gloss = (verbs.get(want) or "").strip()
        swap = (lead + want + rest) if camel and rest else (
            f"{lead}{want}_{rest}" if rest else lead + want)
        print(f"use `{swap}` — the declaration says `{want}`, NOT `{verb}`: {gloss}")
    else:
        print(f"`{verb}` is not in the declared table, and no row bans it by name. "
              f"Declared verbs: {' '.join(sorted(verbs))}")
    return 0


def read_object(name: str) -> str:
    """The OBJECT of an identifier: its subtokens after the leading one, rejoined.

    `build_index` and `render_index` share the object `index`, which is what makes two spellings of
    one concept comparable. A single-token name has no object and is not comparable to anything.
    """
    parts = subtokens(name)
    return "_".join(parts[1:]) if len(parts) > 1 else ""


def run_brief(root: Path, target: str) -> int:
    """S2/S3 — for the objects THIS file names, which leading tokens are live across the corpus.

    NOT A DIRECTORY HISTOGRAM, and the difference is not stylistic. A histogram of a directory's
    off-table leading tokens is bounded by that directory's vocabulary: measured on one adopter test
    directory, 750 distinct tokens and a 7,996-byte full list, so a top-nine line shows 1.2% of it and
    the truncation that bounds the cost voids the signal. Keying on the objects the author's OWN file
    already names is bounded by construction and surfaces the only drift class actually measured here
    — one concept spelled two ways in two kits.

    IT PRINTS WHAT THE CORPUS DOES, NEVER WHAT IT SHOULD DO. No verdict, no pin, no exit 1.
    """
    rel = target.replace("\\", "/")
    p = root / rel
    if not p.is_file():
        print(f"lexicon: {rel} is not a file in this tree")
        return 2

    try:
        conf = load_conf(root / CONF_NAME)
    except (ConfError, OSError) as exc:
        print(f"lexicon: cannot read the declaration: {exc}")
        return 2
    declared = {e: (ps, m) for e, ps, m in langs(conf)}
    ext = ext_of(rel)
    if ext not in declared:
        print(f"COVERAGE: undeclared — .{ext} has no LANGS entry, so nothing is extracted for it")
        return 2
    pset, mode = declared[ext]
    if mode == "dark" or (mode == "probe" and pset not in PATTERN_SETS):
        print(f"COVERAGE: dark — .{ext} declares no extractor, so this file's definitions are not "
              f"read at all. An empty section here would be indistinguishable from 'nothing is "
              f"established, invent freely', which is why this refuses instead.")
        return 2
    print(f"COVERAGE: {mode} — .{ext}" + (f" ({pset})" if pset else "")
          + ("; a probe is incomplete BY CONSTRUCTION" if mode == "probe" else ""))

    # An unparseable target is a NAMED refusal. The corpus loop below already catches this and
    # skips; the target could not, so `--brief` on a file mid-edit died with a traceback rather
    # than saying which file and why. Exit 2, keeping 1 reserved for verdicts. Closing review M3.
    try:
        got = extract(p, mode, pset)
    except (SyntaxError, ValueError) as exc:
        print(f"lexicon: {rel} does not parse, so its objects cannot be read: {exc}")
        return 2
    here = sorted({read_object(n) for n, _ln in (got[0] if got else []) if read_object(n)})
    if not here:
        print("this file names no multi-token definition, so there is no object to compare")
        return 0

    live: dict = {}
    for f in tracked_files(root):
        e = ext_of(f)
        if e not in declared:
            continue
        ps, md = declared[e]
        if md == "dark" or (md == "probe" and ps not in PATTERN_SETS):
            continue
        try:
            g = extract(root / f, md, ps)
        except (SyntaxError, OSError):
            continue
        if not g:
            continue
        for n, _ln in g[0]:
            obj = read_object(n)
            if obj:
                live.setdefault(obj, {}).setdefault(leading_verb(n) or "?", 0)
                live[obj][leading_verb(n) or "?"] += 1

    verbs = conf.get("VERBS") or {}
    print("this prints what the corpus DOES, never what it should do — it decides nothing")
    for obj in here:
        seen = live.get(obj) or {}
        shown = ", ".join(f"{v} x{c}" + ("" if v in verbs else " (off-table)")
                          for v, c in sorted(seen.items(), key=lambda kv: (-kv[1], kv[0])))
        flag = "  <-- SPELLED MORE THAN ONE WAY" if len(seen) > 1 else ""
        print(f"  {obj}: {shown or 'no other definition names this object'}{flag}")
    return 0



def run_probe(root: Path) -> int:
    """S3 — what the canon would propose here, and what the corpus spells otherwise.

    READ-ONLY, NO ARGUMENTS, NO STATE, EXITS 0 UNCONDITIONALLY, and legal against a repo with no
    declaration at all. Those are properties, not manners: an adopter deciding whether to take this
    kit needs to see what it would say BEFORE anything is written, and a probe that can fail or
    write is one nobody runs on a repo they care about.

    IT DECIDES NOTHING. The canon fixes the representative; the corpus only reports which concepts
    are present and which spellings are debt. Reading this output cannot change what a proposal
    would name, which is exactly the property a frequency ranking did not have.
    """
    forms = canon.build_form_index()
    conf = None
    try:
        if (root / CONF_NAME).is_file():
            conf = load_conf(root / CONF_NAME)
    except ConfError:
        conf = None
    declared = {e: (ps, m) for e, ps, m in langs(conf)} if conf else dict(KNOWN_EXTS)

    counts: dict = {}
    files = tracked_files(root)
    for rel in files:
        ext = ext_of(rel)
        if ext not in declared:
            continue
        pset, mode = declared[ext]
        if mode == "dark" or (mode == "probe" and pset not in PATTERN_SETS):
            continue
        try:
            got = extract(root / rel, mode, pset)
        except (SyntaxError, OSError):
            continue
        if not got:
            continue
        for name, _ln in got[0]:
            v = leading_verb(name)
            if v:
                counts[v] = counts.get(v, 0) + 1

    total = sum(counts.values())
    print(f"lexicon --probe — {total} definition(s) over {len(files)} tracked file(s)"
          + ("" if conf else "; NO .lexicon.conf here, so this is what adoption would find"))
    print("the canon decides what each concept is CALLED; this corpus only decides which appear")
    print()

    proposed, debt_rows, off = [], [], {}
    for rep, _gloss, others in canon.CLUSTERS:
        live = [(f, counts.get(f, 0)) for f in (rep,) + tuple(others) if counts.get(f)]
        if not live:
            continue
        proposed.append(rep)
        shown = ", ".join(f"{f} x{n}" + ("" if f == rep else " -> debt") for f, n in live)
        print(f"  {rep:<9} {shown}")
        debt_rows += [(f, n, rep) for f, n in live if f != rep]
    for v, n in counts.items():
        if v not in forms:
            off[v] = n

    print()
    print(f"  would propose {len(proposed)} of {len(canon.CLUSTERS)} cluster(s): {' '.join(proposed)}")
    if debt_rows:
        cost = sum(n for _f, n, _r in debt_rows)
        print(f"  convergence would cost {cost} rename(s) across {len(debt_rows)} spelling(s): "
              + ", ".join(f"{f}->{r} x{n}" for f, n, r in sorted(debt_rows, key=lambda x: -x[1])[:8]))
    else:
        print("  no debt: every live site already uses its cluster's representative")
    # A token in no cluster is not automatically debt. The canon bounds what a MACHINE may propose;
    # it does not bound what an owner may RATIFY, and this repo's own table carries `seed`, `arm` and
    # `cmd`, which no cluster holds. Reporting a ratified row as unnominatable would read as a
    # finding against a decision somebody made deliberately.
    ratified = set((conf or {}).get("VERBS") or {})
    beyond = {v: n for v, n in off.items() if v in ratified}
    unnamed = {v: n for v, n in off.items() if v not in ratified}
    if beyond:
        top = ", ".join(f"{v} x{n}" for v, n in sorted(beyond.items(), key=lambda kv: -kv[1])[:8])
        print(f"  {sum(beyond.values())} definition(s) lead with a RATIFIED row outside the canon: {top}")
        print("  legal: the canon bounds what a proposal may name, never what an owner may declare")
    if unnamed:
        top = ", ".join(f"{v} x{n}" for v, n in sorted(unnamed.items(), key=lambda kv: -kv[1])[:8])
        print(f"  {sum(unnamed.values())} definition(s) lead with a token in NO cluster and NO row: {top}")
        print("  unnominatable by absence — no proposal can ever name them")
    return 0


def main(argv: list[str]) -> int:
    mode = argv[1] if len(argv) > 1 else "--check"
    if mode not in ("--check", "--list", "--measure", "--suggest", "--brief", "--probe"):
        sys.stderr.write("usage: python tools/lexicon/lexicon.py "
                         "[--check|--list|--measure|--suggest <name>|--brief <path>|--probe]\n")
        return 2
    if mode in ("--suggest", "--brief") and len(argv) < 3:
        sys.stderr.write(f"usage: python tools/lexicon/lexicon.py {mode} "
                         + ("<identifier>\n" if mode == "--suggest" else "<path>\n"))
        return 2
    out = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    if out.returncode != 0:
        sys.stderr.write("lexicon: not a git repo\n")
        return 2
    root = Path(out.stdout.strip())
    # The two SUPPLY verbs return before `run()`, which is what keeps them off the gate path: they
    # cannot reach a pin, a waiver or an exit code of 1 even by accident.
    if mode == "--suggest":
        return run_suggest(root, argv[2])
    if mode == "--brief":
        return run_brief(root, argv[2])
    if mode == "--probe":
        return run_probe(root)
    return run(root, list_mode=(mode == "--list"), measure_mode=(mode == "--measure"))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
