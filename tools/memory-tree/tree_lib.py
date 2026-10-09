#!/usr/bin/env python3
"""tree_lib.py — the helpers two or more memory-tree engines share, and nothing else.

TOOL-aRepatriatedFork-9. `check-arms.py`, `row_grammar.py` and `gotchas.py` used to import these from
`corpus_ids.py` and `gen_build_index.py`, which made those two files a hard prerequisite of every
engine beside them. At an adopter whose copies of those two are its own programs — adopter ic, measured —
both gov engines died on import with an `ImportError`, so a fork of one file forced a fork of three.
The helpers live here now, and the two modules that defined them re-import them, so every caller
that reaches them through the old name keeps working.

WHAT BELONGS HERE: a name at least two engines in this directory read. A name one engine owns stays
in that engine; this is a seam, not a utility drawer. `row_grammar.py --selftest` carries the arm
that refuses a sibling engine importing from `corpus_ids` or `gen_build_index` again.

The module name follows the codebase-map kit's `map_lib.py` and the runlog kit's `runlog_lib.py`.
"""
from __future__ import annotations

import os
import pathlib
import re

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

# A gotcha record's front-matter block: `---` at line 1, the column-0 `key: value` lines, `---`.
# Read by `gotchas.py` (checks 17-19, which grade the keys) and by `row_grammar.py`'s record
# enumeration (check 27, which ranks a record by its `description`). TOOL-aGraftedHelix-9 moved it
# here so the kit holds one copy: two engines spelling one block are free to disagree on where a
# record's front matter ends.
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)


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
    # TOOL-aRepatriatedFork-38 rev-3 (the closing review's C4): the WORD rule, decided on the text
    # right after `=`. Whitespace there ends the assignment, so `K= x` and `K=   # note` are empty in
    # bash; a `#` begins a comment only AFTER whitespace, so `K=#x` keeps `#x`.
    if v[:1].isspace():
        return k, ""
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
    # UNQUOTED: a `#` that FOLLOWS whitespace starts a comment. Position 0 is not one: the
    # leading-whitespace case returned above, so a `#` there is the first character of the word.
    cut = -1
    for i, ch in enumerate(v):
        if ch == "#" and i > 0 and v[i - 1].isspace():
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


#: The declared-gap citation form (TOOL-aMendedFleet-26): this prefix written immediately before an
#: id says "this id has no record", so check 14 does not count it as an orphan and the roster
#: derivation does not file it on its slug's build. Spelled here and nowhere else.
MISSING_PREFIX = "missing:"


def scan_missing_citations(text: str, id_re) -> tuple[list, str]:
    """`(ids, blanked)`: every id written in the `missing:` form, and `text` with each form and its
    id overwritten by spaces of the same length, so offsets and line numbers still hold.

    `id_re` is the CALLER's own compiled id regex, so the form needs no second id grammar: each
    reader recognises a marked id by exactly the predicate it already uses for a cited one. A plain
    regex cannot tell the two apart on its own, because the colon is a word boundary.
    """
    pat = re.compile(re.escape(MISSING_PREFIX) + "(?:" + id_re.pattern + ")", id_re.flags)
    ids = [mm.group(0)[len(MISSING_PREFIX):] for mm in pat.finditer(text)]
    if not ids:
        return ids, text
    return ids, pat.sub(lambda mm: " " * len(mm.group(0)), text)


def build_spec_path_re(memory_root: str):
    """The path half of `parse_spec_h1`: a build's `spec/` folder, at any depth. Exposed so a caller
    walking a whole tree can skip reading a file the predicate would refuse on its path alone."""
    return re.compile(r"^" + re.escape(memory_root) + r"/builds/[^/]+/spec/")


def parse_spec_h1(rel: str, text: str, memory_root: str, families) -> tuple[int, str] | None:
    """`(lineno, id)` of the H1 that DEFINES a unit id in a spec file, or None.

    THE one predicate for "which id does this spec define" (TOOL-aRepatriatedFork-40). Two kits read
    it: `gen_build_index.spec_ids`, the index generator's resolution set, and the memory-recall
    kit's `extract_records`, which anchors a record on the same line. The recall kit reaches it
    through the sibling-kit resolver because it `requires` this kit; a copy of the regex there is
    the two-answers-to-one-question class.

    `rel` is repo-relative and must sit under `<memory_root>/builds/<slug>/spec/`, at any depth. The
    first UNFENCED H1 whose first token is `<FAMILY>-<slug>-<seq>` wins, one per file. `families`
    is the prefixes alone (`TOOL`, not `tooling:TOOL`).
    """
    if not build_spec_path_re(memory_root).match(rel):
        return None
    alt = "|".join(sorted(set(families))) or "(?!)"
    pat = re.compile(r"^#\s+[`*]*(?P<id>(?:" + alt + r")-[A-Za-z0-9]+-\d+)\b")
    for n, line in unfenced_lines(text):
        if line is None:
            continue
        m = pat.match(line)
        if m:
            return n, m.group("id")
    return None


def build_git_env() -> dict:
    """The environment every pinned git call in this kit runs under — the kit's ONE pin policy.

    `GIT_GRAFT_FILE=/dev/null` is the spelling the unattended kit's history leg uses and it works
    under Git for Windows, whose MSYS layer maps the name. A graft file re-parents commits, so
    without this pin every ancestry answer could be honest about a sha and wrong about what that sha
    means. Callers add `--no-replace-objects` to the argv. Read by `transition_audit.py` and
    `routed_commits.py`; it moved here from the first when the second arrived (TOOL-aRoutedQuill-3).
    """
    env = dict(os.environ)
    env["GIT_GRAFT_FILE"] = "/dev/null"
    return env
