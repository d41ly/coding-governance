#!/usr/bin/env python3
"""tree_lib.py — the helpers two or more memory-tree engines share, and nothing else.

TOOL-aRepatriatedFork-9. `check-arms.py`, `row_grammar.py` and `gotchas.py` used to import these from
`corpus_ids.py` and `gen_build_index.py`, which made those two files a hard prerequisite of every
engine beside them. At an adopter whose copies of those two are its own programs — inCMS, measured —
both gov engines died on import with an `ImportError`, so a fork of one file forced a fork of three.
The helpers live here now, and the two modules that defined them re-import them, so every caller
that reaches them through the old name keeps working.

WHAT BELONGS HERE: a name at least two engines in this directory read. A name one engine owns stays
in that engine; this is a seam, not a utility drawer. `row_grammar.py --selftest` carries the arm
that refuses a sibling engine importing from `corpus_ids` or `gen_build_index` again.

The module name follows the codebase-map kit's `map_lib.py` and the runlog kit's `runlog_lib.py`.
"""
from __future__ import annotations

import pathlib

# The lifecycle vocabulary, one declaration for the index generator's front-matter check, check 24's
# rotation grading and the backlog-row census.
STATUS_TOKENS = ("OPEN", "SPECCED", "INPROGRESS", "BLOCKED", "DEFERRED", "CLOSED", "WONTDO")
# What the INDEX generator and check 24 call terminal: a `DEFERRED` build or row stays in the live
# index, because parked work is still work somebody owes.
TERMINAL = ("CLOSED", "WONTDO")
# What the backlog-row CENSUS calls terminal, and it is DELIBERATELY WIDER (the unit's section 8 F1,
# owner-resolved). `memory/TEMPLATE-SPEC.md` names CLOSED / DEFERRED / WONTDO as the terminal set a
# spec header flips to, and a report-only census counting a deferred row as outstanding work would
# overstate the debt. The index answers "what must stay visible", the census "what is still owed";
# two questions, two tuples, and both are declared HERE so the difference is one decision in one place
# rather than two modules that happen to disagree.
CENSUS_TERMINAL = ("CLOSED", "WONTDO", "DEFERRED")


def kit_rel() -> str:
    """This kit's directory relative to the enclosing checkout, DERIVED and never spelled.

    Written into generated artifacts and into remedy strings an operator copies, so a hardcoded
    prefix lands a dead path in an adopter's tree. Falls back to the bare kit name when the module
    sits outside any checkout (a test fixture, an odd install); the result is a pointer, never a gate
    input.
    """
    here = pathlib.Path(__file__).resolve().parent
    for anc in [here] + list(here.parents):
        if (anc / ".git").exists():
            try:
                return here.relative_to(anc).as_posix()
            except ValueError:
                break
    return here.name


def parse_conf_line(line: str):
    """One `.memory-tree.conf` line -> `(key, value)`, or `None` for a line that declares nothing.

    TOOL-aScouredKit-19. SIX readers in this kit held this body and the shell gate SOURCES the same
    file in bash, so any spelling bash accepts and the python half mis-reads REMOVES coverage while
    the gate stays green. Reproduced: `MEMORY_ROOT=memory   # note` took `gotchas.py --check` from
    rc=1 to rc=0 over an identical planted violation, because the python half then walked a directory
    that does not exist. Coverage removed, not failed closed.

    TWO SPELLINGS BASH ACCEPTS THAT THE OLD BODY DID NOT, both measured against `set -a; . conf`:

        MEMORY_ROOT=memory   # note   ->  memory        (an unquoted inline comment is stripped)
        export FAMILIES="TOOL DEPL"   ->  TOOL DEPL     (the export prefix is not part of the key)

    AND ONE IT MUST NOT BREAK, which is why the comment strip is not unconditional:

        QUOTED="a # b"                ->  a # b         (a `#` inside quotes is DATA)

    Stripping `#` unconditionally would turn that into `a`, a silent wrong value where today's bug is
    at least a loud directory miss. So the strip runs BEFORE the quote peel and only on an unquoted
    `#` that begins a word, which is bash's own rule.

    NOT a general shell grammar, and deliberately: command substitution, parameter expansion, line
    continuations and quoted whitespace are all legal bash and none is in scope. These two are the
    spellings an adopter actually writes and the ones the kit's own example neither shows nor forbids.
    """
    line = line.strip()
    if not line or line.startswith("#") or "=" not in line:
        return None
    k, _, v = line.partition("=")
    k = k.strip()
    if k.startswith("export ") or k.startswith("export\t"):
        k = k[len("export"):].strip()
    if not k:
        return None
    v = v.strip()
    # A QUOTED VALUE AND AN UNQUOTED ONE NEED DIFFERENT SCANS, and the first cut of this function
    # had only the second — so `KEY="v"  # note` kept both the comment AND a stray quote, which is
    # live on five lines of this kit's own shipped `.memory-tree.conf.example`. Found by the closing
    # diff review, reproduced against `set -a; . conf`.
    #
    # QUOTED: take the text between the opening quote and its MATCH, then treat only the remainder
    # as comment territory. That is what makes `Q="a # b"` keep its `#` while `Q="a"  # note` loses
    # its trailing one — the two directions this parser has to get right at once.
    if v[:1] in ("'", '"'):
        q = v[0]
        end = v.find(q, 1)
        if end >= 0:
            return k, v[1:end]
        # An UNTERMINATED quote is not something to guess at. Fall through to the unquoted scan,
        # which is what the old body did for every value, so this is no worse than before for a
        # spelling bash itself would reject.
    # UNQUOTED: a `#` that begins a word starts a comment, including at position 0 — `X=   # note`
    # is an empty value in bash, not the literal `# note`.
    cut = -1
    for i, ch in enumerate(v):
        if ch == "#" and (i == 0 or v[i - 1].isspace()):
            cut = i
            break
    if cut >= 0:
        v = v[:cut].strip()
    return k, v.strip('"').strip("'")


def parse_conf(text: str, conf: dict) -> dict:
    """Merge every declaration in `text` into `conf`, which carries the caller's OWN defaults.

    The defaults stay per-reader on purpose: they differ (`CHARTER` and the pins for corpus_ids, the
    universal budget for gotchas, the arms floors for check-arms), and one merged dict would give
    every reader keys it has no use for and hide which reader depends on which.
    """
    for line in text.split("\n"):
        kv = parse_conf_line(line)
        if kv is not None:
            conf[kv[0]] = kv[1]
    return conf


def unfenced_lines(text: str):
    """Yield (lineno, line) for every line OUTSIDE a fenced block, then the open fence's line.

    The final yield is `(opened_at, None)` when the document ends inside a fence, and nothing when it
    does not. A caller that only wants the text ignores it; a caller that must REFUSE a document it
    could not fully read needs it, and no reader in either kit had it — the shell `_unfenced` and the
    index generator both ended silently with the fence still open, dropping every later line at
    exit 0. That is invisible by construction: a fence opened near the top of a row document hides
    every duplicate below it, and hiding duplicates is what the check that reads this exists to stop.
    """
    fence = ""
    opened_at = 0
    for n, line in enumerate(text.split("\n"), 1):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            mark = "```" if stripped.startswith("```") else "~~~"
            if not fence:
                fence, opened_at = mark, n
                continue
            # Only the marker that OPENED the fence closes it: a ``` line inside a ~~~ block is
            # content, not a toggle.
            if mark == fence:
                fence = ""
                continue
        if not fence:
            yield n, line
    if fence:
        yield opened_at, None
