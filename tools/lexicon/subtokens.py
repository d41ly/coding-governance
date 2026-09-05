"""subtokens.py — the leading-token splitter, LEXICON-OWNED.

Ported from `map_lib.subtokens()`, not imported from it. The direction of truth is stated in the
unit spec (S5) and it is deliberately the opposite of what the first draft proposed: the lexicon
owns its copy and ships SELF-CONTAINED, so an adopter who takes this kit WITHOUT `codebase-map`
gets a working kit rather than an ImportError. A parity leg asserts the two copies agree, but that
leg is gov-internal and is never shipped — the shipped-parity version of it would compare against a
file the adopter does not have, so it would red forever or be silently skipped, and a silently
skipped parity leg is the drift the gate exists to catch.

Keep this file byte-comparable to its source in SUBSTANCE: the regex and the lowercasing are the
contract. If `map_lib` changes the split, the gov-internal parity leg is what notices.

TWO PREDICATES LIVE HERE AND NEITHER CALLS THE OTHER (TOOL-aSurfacedLexicon-5 S7). `subtokens()`
LOWERCASES, so `BuildIndex` and `build_index` are indistinguishable after it and no case question
can be answered from its output. The convention classifier below therefore reads the RAW name and is
`subtokens()`'s SIBLING, not its consumer. The two also disagree about what "no word characters"
MEANS, and a reader hitting either one deserves to be told: `leading_verb` strips LEADING
underscores and runs ASCII subtoken classes, so a non-ASCII name returns `""` there; `read_core`
strips underscores at BOTH ends and nothing else, so the same name survives it whole and reds as
AMBIGUOUS. Ungradeable there, AMBIGUOUS here, deliberately, because one rule across both was never
available to be chosen (fork F1).
"""

import re

#: camelCase / snake / kebab / path / digit boundary splitter — `getUserID` -> [get,user,id],
#: `api/x/route.ts` -> [api,x,route,ts], `slugify` -> [slugify]. `[A-Z]+(?![a-z])` keeps an
#: acronym run (`HTTPServer` -> [http, server]) instead of shredding it.
_SUBTOKEN_RE = re.compile(r"[A-Z]+(?![a-z])|[A-Z][a-z]*|[a-z]+|[0-9]+")


def subtokens(text: str) -> list[str]:
    """Lowercase word pieces of an identifier, split on camelCase, snake_case, kebab, path
    (`/` `.`) and digit boundaries."""
    return [t.lower() for t in _SUBTOKEN_RE.findall(text)]


def leading_verb(identifier: str) -> str:
    """The first subtoken of an identifier — the token P1 grades against the declared table.

    Returns `""` for an identifier with no word characters at all (`__`, `_`, `1`), which the
    caller must treat as UNGRADEABLE rather than as a violation: a name with no leading token is
    not a name that chose the wrong verb. Dunder and single-underscore prefixes are stripped first,
    so `_build_index` and `__init__` grade on `build` and `init` rather than on nothing.
    """
    toks = subtokens(identifier.lstrip("_"))
    return toks[0] if toks else ""


# ---- the convention classifier: read_core -> classify -> check_convention ------------------------
#
# NOT DERIVED FROM THE POPULATION IT GRADES, and that is the load-bearing property rather than an
# aside. The six forms below are the ordinary prescriptive spellings of snake, SCREAMING, camelCase,
# PascalCase, kebab-case and dot.case; not one of them was read off this corpus, and none may ever be
# widened because the tree failed it. The corpus is evidence for exactly one thing here — which
# spellings become debt — and for nothing whatever about what a convention IS.

#: Leading and trailing underscores are PRIVACY MARKERS, not case, and stripping them before
#: classification is the largest single source of false positives the prototype found: without it
#: `__init__` and `_build_index` are reported as snake violations. Anchored and DOTALL, so it strips
#: underscores at both ends and NOTHING else — a non-ASCII core survives it whole.
_AFFIX = re.compile(r"^(_*)(.*?)(_*)$", re.DOTALL)

#: The six forms, each ONE anchored pattern over the stripped core. `dot` is a CLASSIFIER form only
#: and is deliberately not declarable — `lexicon_conf.CONVENTIONS` refuses it by name — because no
#: language convention is "identifiers contain dots"; it earns its place by keeping a dotted name out
#: of AMBIGUOUS and by letting a message say what such a name DOES satisfy. `run` matches four of the
#: six on purpose, which is the whole argument for returning a SET rather than a label.
_FORMS = {
    "snake": re.compile(r"^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$"),
    "screaming": re.compile(r"^[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)*$"),
    "camel": re.compile(r"^[a-z][a-z0-9]*(?:[A-Z][a-z0-9]*)*$"),
    "pascal": re.compile(r"^[A-Z][a-z0-9]*(?:[A-Z][a-z0-9]*)*$"),
    "kebab": re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$"),
    "dot": re.compile(r"^[a-z][a-z0-9]*(?:[.][a-z0-9]+)*$"),
}


def read_core(name: str) -> str:
    """The identifier with its leading and trailing underscores stripped — what `classify` grades.

    Returns `""` for a name that is nothing but underscores, which is a legal Python definition name
    (`def _():`) and NOT a skip: `check_convention` reds it as AMBIGUOUS. See the module docstring
    for why that diverges from `leading_verb` on purpose.
    """
    return _AFFIX.match(name).group(2)


def classify(name: str) -> set:
    """The SET of forms the affix-stripped core satisfies — never a single label.

    SET-VALUED BECAUSE THE POPULATION IS. Hundreds of this repo's Python definitions satisfy two or
    more forms at once, and `run` satisfies four, so a single-label classifier reports a violation
    for every one of them the moment the declared cell is not the label it happened to pick. That is
    a predicate that gets waived in its first week rather than one that ships.

    `classify` is NOT in the declared VERBS table and it STAYS: it is the name the prototype used,
    and the table's value is scoping rather than spelling. The cost is a named, measured raise of
    `VERB_OFFENDER_PIN` rather than a rename that answers no question about what this does.
    """
    core = read_core(name)
    return {k for k, rx in _FORMS.items() if rx.match(core)}


def read_stem(basename: str) -> str:
    """A filename's basename up to its FIRST dot — the string an `<ext>.file` cell grades.

    FIRST and not last, and the difference is a ten-fold swing rather than a nicety: under last-dot
    stemming every `*.test.sh` script keeps an interior dot in its stem and reds as a kebab
    violation, so a compound extension alone would red this repo's whole shell test suite on day one.

    A dot-LEADING basename therefore stems to the EMPTY string, which `check_convention` reds as
    AMBIGUOUS. That is not a defect to route around — it is the classifier saying it was handed
    nothing to classify — and it has a live in-corpus population, so arming one of those cells is a
    decision about dotfiles rather than a formality.
    """
    return basename.split(".", 1)[0]


def check_convention(name: str, convention: str) -> tuple:
    """`(verdict, message)` for ONE name against ONE declared convention. Three verdicts, no fourth.

    SATISFIED when the convention is IN the set, message empty. VIOLATION when the set is non-empty
    and the convention is not in it, message naming what the name DOES satisfy. AMBIGUOUS when the
    set is empty, whether or not the core is, under a message distinct from VIOLATION.

    A VIOLATION is "the declared convention is not IN the set", never "it is not the set's first or
    only member" — the difference is every multi-convention name in the corpus.

    The AMBIGUOUS row deliberately does NOT test the core. Reading it as "non-empty core AND empty
    set" leaves an EMPTY core matching no row at all: not SATISFIED, not VIOLATION because the set is
    empty, not AMBIGUOUS because the core is. The name then falls through all three and the
    classifier prints nothing, which is a skip wearing a pass's clothes.
    """
    forms = classify(name)
    if convention in forms:
        return "SATISFIED", ""
    if not forms:
        return "AMBIGUOUS", (f"AMBIGUOUS  {name}  satisfies no convention this classifier knows, so "
                             f"there is nothing here to grade against {convention}")
    return "VIOLATION", f"VIOLATION  {name}  satisfies {', '.join(sorted(forms))}, not {convention}"
