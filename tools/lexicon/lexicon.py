#!/usr/bin/env python3
# gov:kit lexicon@1.0
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
population passes green forever and tells you nothing. It is armed THREE ways, and the third was
added after the first two proved insufficient in this file's own first landing:

  DEAD PROBE          a parser/probe language whose definition population is empty against a corpus
                      containing that extension — an extractor that has gone inert
  frozen SENTINELS    a fixture per shipped pattern set in `selftest.py`, because the corpus-side
                      arm above is itself defeated by an empty corpus
  UNMATCHABLE RULE    a LAYERS rule that is NON-EMPTY but cannot fire. `NOT ARMED` tests emptiness
                      and DEAD PROBE tests extractors; neither tests REACHABILITY, and a real rule
                      shipped through that gap reporting an unfalsifiable 0. Reachability is proved
                      by CONSTRUCTION: the rule must flag its own synthetic violation.
"""

import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lexicon_conf import ConfError, langs, load_conf  # noqa: E402
from subtokens import leading_verb, subtokens  # noqa: E402

KIT_LEXICON_VERSION = "1.0"

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
            if node.module:
                imports.append((node.module, node.lineno))
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


def _glob_match(path: str, pattern: str) -> bool:
    rx = re.escape(pattern).replace(r"\*", "[^/]*").replace(r"\?", "[^/]")
    return re.match(rx + "$", path) is not None or re.match(rx, path) is not None


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


def resolve_import(target: str, importer: str, index: dict[str, list[str]]) -> list[str]:
    """Candidate repo paths an import target may denote. Empty means EXTERNAL or unresolvable, which
    is not a violation — a rule can only forbid what it can locate."""
    out: list[str] = []
    here = importer.rsplit("/", 1)[0] if "/" in importer else ""

    # A relative JS/TS specifier resolves against the IMPORTER's directory. Swapping dots for
    # slashes mangles these into `///adapters/db` and matches nothing.
    if target.startswith("."):
        parts = [p for p in (here + "/" + target).split("/") if p not in ("", ".")]
        stack: list[str] = []
        for p in parts:
            if p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        cand = "/".join(stack)
        out.append(cand)
        out.extend(p for p in index.get(cand.rsplit("/", 1)[-1], []) if p.startswith(cand))
        return out

    # A dotted namespace MAY mirror a path; keep that reading, it is right when packages mirror dirs.
    out.append(target.replace(".", "/"))

    # And resolve the LAST segment as a module stem against the corpus. This is what catches the
    # flat `sys.path`-insert import — the commonest shape in this tree and in every kit here — where
    # the target is a bare name that shares no characters with its own directory.
    out.extend(index.get(target.rsplit(".", 1)[-1], []))
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


def scan_unmatchable_rules(layers, files: list[str], index) -> list[tuple[str, str, str]]:
    """LAYERS rules that CANNOT fire, with the reason. The third vacuity defence.

    `NOT ARMED` tests whether LAYERS is empty; `DEAD PROBE` tests whether an extractor selects
    anything. Neither tests whether a NON-EMPTY rule is REACHABLE, and that gap shipped a rule that
    could never match while its offender pin read a confident, unfalsifiable 0.

    Reachability is proved by CONSTRUCTION, not by observation: for each rule, take a real tracked
    file on the `to` side, derive the import target a real importer would write for it, and require
    the matcher to flag it. A rule that survives its own synthetic violation is a rule that will
    never see a real one.
    """
    bad = []
    for frm, to in layers:
        sources = [f for f in files if _glob_match(f, frm)]
        targets = [f for f in files if _glob_match(f, to)]
        if not sources:
            bad.append((frm, to, f"the FROM glob {frm!r} matches no tracked file"))
            continue
        if not targets:
            bad.append((frm, to, f"the TO glob {to!r} matches no tracked file"))
            continue
        probe_src = sources[0]
        reachable = False
        for t in targets:
            base = t.rsplit("/", 1)[-1]
            stem = base.rsplit(".", 1)[0] if "." in base else base
            for synthetic in (stem, t.rsplit(".", 1)[0].replace("/", "."), "./" + t):
                if check_layer_violation(probe_src, synthetic, [(frm, to)], index):
                    reachable = True
                    break
            if reachable:
                break
        if not reachable:
            bad.append((frm, to, f"no import of any file under {to!r} can be matched from {frm!r} — "
                                 f"the rule is non-empty but UNREACHABLE, so its offender count is "
                                 f"an unfalsifiable 0"))
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
        # The THIRD vacuity defence. Emptiness and dead extractors were armed from the start; a
        # non-empty rule that cannot fire was not, and that is the gap a real rule shipped through.
        for frm, to, why in scan_unmatchable_rules(layers, files, module_index):
            problems.append(f"UNMATCHABLE LAYERS RULE `{frm} -> {to}` — {why}. A rule that cannot "
                            f"fire is worse than no rule: it reports a confident 0 that no edit can "
                            f"ever move.")

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
