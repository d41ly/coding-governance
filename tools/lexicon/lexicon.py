#!/usr/bin/env python3
# gov:kit lexicon@1.1
"""lexicon.py — three naming predicates over a DECLARED vocabulary.

    python tools/lexicon/lexicon.py            # assert; non-zero on an unwaived offender
    python tools/lexicon/lexicon.py --list     # print every offender, waived or not (authoring aid)
    python tools/lexicon/lexicon.py --measure  # print the three pins THIS conf produces; decide nothing

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

from lexicon_conf import ConfError, langs, load_conf  # noqa: E402
from subtokens import leading_verb, subtokens  # noqa: E402

KIT_LEXICON_VERSION = "1.1"

CONF_NAME = ".lexicon.conf"
WAIVER_FILES = {
    "verb": "lexicon-verb-waivers.txt",
    "suffix": "lexicon-suffix-waivers.txt",
    "layer": "lexicon-layer-waivers.txt",
}
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


def extract(path: Path, mode: str, pset: str):
    """`(functions, types, imports)` for one file, or `None` when the mode declares no extractor."""
    if mode == "dark":
        return None
    src = path.read_text(encoding="utf-8", errors="replace")
    if mode == "parser":
        return _python_defs(src)
    return _probe_defs(src, pset)


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
    populations: dict[str, int] = {}

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
        populations[ext] = populations.get(ext, 0) + len(funcs) + len(types_)

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
        if any(ext_of(f) == ext for f in files) and not populations.get(ext):
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
    if measure_mode:
        for kind in ("verb", "suffix", "layer"):
            waivers = load_waivers(kit, kind)
            unwaived = [o for o in offenders[kind] if o.text not in waivers]
            print(f'{PIN_KEYS[kind]}="{len(unwaived)}"')
        if problems:
            print("# NOTE: the run also reported problems that are not pin-counted:")
            for p in problems:
                print(f"#   {p}")
        return 0

    # --- waivers, pins, verdict ---------------------------------------------------------------
    exit_code = 0
    for kind in ("verb", "suffix", "layer"):
        waivers = load_waivers(kit, kind)
        found = offenders[kind]
        seen_texts = {o.text for o in found}
        unwaived = [o for o in found if o.text not in waivers]
        stale = [w for w in waivers if w not in seen_texts]

        if list_mode:
            for o in found:
                print(("  waived " if o.text in waivers else "  ") + str(o))

        if stale:
            problems.append(f"STALE WAIVERS in {WAIVER_FILES[kind]} (the matched text is gone; "
                            f"delete the row): {', '.join(sorted(stale))}")

        pin_raw = conf.get(PIN_KEYS[kind], "")
        try:
            pin = int(pin_raw) if str(pin_raw).strip() else 0
        except ValueError:
            problems.append(f"{PIN_KEYS[kind]}={pin_raw!r} is not an integer")
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

    if exit_code == 0:
        modes = ", ".join(f".{e}={m}" for e, (_, m) in sorted(declared.items()))
        print(f"lexicon OK — {len(files)} tracked file(s); coverage: {modes}")
    return exit_code


def main(argv: list[str]) -> int:
    mode = argv[1] if len(argv) > 1 else "--check"
    if mode not in ("--check", "--list", "--measure"):
        sys.stderr.write("usage: python tools/lexicon/lexicon.py [--check|--list|--measure]\n")
        return 2
    out = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    if out.returncode != 0:
        sys.stderr.write("lexicon: not a git repo\n")
        return 2
    return run(Path(out.stdout.strip()), list_mode=(mode == "--list"), measure_mode=(mode == "--measure"))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
