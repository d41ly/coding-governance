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
