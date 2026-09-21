#!/usr/bin/env python3
"""backlog.py — a build's BACKLOG.md grammar, the two status-header verbs, and the status fold.

    python backlog.py --selftest      # run from this kit's own directory

WHAT THIS IS. Backlog status is the one work-state fact this repo still types by hand, and a typed
status drifts from the records that decide it. This module is the model that replaces it: one
grammar for a build's own `BACKLOG.md`, the two spec-header verbs `closes` and `advances`, and an
ORDER-FREE fold that derives every ask's status from SETS of records.

THE MODULE SHIPS DARK. Nothing here reads the tree, runs a command or is wired into a check.
`BACKLOG_MODE` defaults to `shards`, no spec header in this corpus carries either verb, and a
header that carries neither parses byte-identically to how it parsed before.

THE FAMILY VIEW LIVES HERE TOO (TOOL-dDerivedDocket-7): the renderer, the predicate that
RECOGNISES a view, and the relocation recipe every banner and message quotes. All three are
pure text functions — the generator hands them records and hands them its own install prefix,
and the row driver and the relocation engine read the same three rather than holding copies.
One constant, three renderings, and no second spelling to drift.

THE FILE GRAMMAR, in one place and nowhere else:

    file       := H1 BLANK* QUOTE* [ "## Asks" (BLANK | ask)* ] [ "## Dispositions" (BLANK | verbrow)* ]
    ask        := "- " ID " . filed " DATE [ " . unit" ] " . " TEXT CLAUSE* [ " -> " POINTER ]
    verbrow    := status | sev | scope | provenance
    scope      := "- SCOPE . " ID CLAUSE+
    CLAUSE     := " . " LABEL " " VALUE
    LABEL      := "seen" | "accept" | "out" | "may" | "verify" | "data"
    seen       := LOCATOR [ " run `" COMMAND "`" ]
    LOCATOR    := "`" PATH "`@" SHA7+ [ ":" LINE ] | "`" PATH "` matching `" PATTERN "`"
                | REPO ":" PATH "@" SHA7+
    may        := "none" | GRANT ( " " GRANT )*      ; GRANT := "`" PATH "`" | decision ID
    status     := "- CLOSED . "   ID " . by "    (ID | SHA)        " . " WHY
                | "- WONTDO . "   ID                               " . " WHY
                | "- BLOCKED . "  ID " . on "    ID                " . " WHY
                | "- DEFERRED . " ID " . until " ID                " . " WHY
                | "- KEEP . "     ID                               " . " WHY
                | "- REOPEN . "   ID " . of "    (ID | SHA | SLUG) " . " WHY
    sev        := "- SEV . " ID " . " ("BLOCKER" | "HIGH" | "MED" | "LOW") " . " WHY
    provenance := "- RELOCATED . " ID " . by " SHA " . " ("kept"|"dropped"|"amended") ": " WHY

The separator written `.` above is the middot `SEP` below; it is spelled out here because a
docstring that carried the real glyph twenty times would be the one place a reader copies a row
from, and a copy of the grammar is the thing that rots. The renderers at the foot of this file are
the copyable form, and the parser reads exactly what they write — that pairing is what AC2 grades.

WHAT THIS MODULE DOES NOT CHECK, said out loud because a structural reader reads as a semantic one
to everybody who did not write it. It never touches the filesystem, git, the clock or a network: a
caller hands it text and hands it a spec index. It does not decide whether a WHY is true, or whether a `closes` verb is honest — an over-claiming `closes` closes its
ask silently, and the only thing that shows it is the Decided-by value the fold returns beside the
status. It does not read a wrapped legacy row: `read_legacy_row` reads ONE physical line and says so.

THE CLAUSE TAIL, `SCOPE` ROWS AND THE READY PREDICATE LIVE HERE TOO (TOOL-dDerivedDocket-15), and
they change none of the above. Whether a locator's PATH exists is still not this module's question:
`build_grader` takes the tree probe as a CALLABLE, exactly as `read_header_verbs` takes its id
expander, so a caller hands in the tree it means and this file still touches no filesystem. A clause
is CONTENT, so a malformed one is verdict V13 and never an exception; V14 is forward-only, read off
the MERGED clauses, and disarmed by the same two conf verdicts V9 and V12 are.

CONTENT NEVER RAISES. Every unparseable line is a V2 verdict naming the file and the line, because
one bad row in one build must not refuse every artifact this kit renders. The two things that DO
raise are configuration, not content: an unknown `BACKLOG_MODE` value and a malformed header verb.
"""
from __future__ import annotations

import collections
import itertools
import os
import pathlib
import re
import sys

# ------------------------------------------------------------------------------------- the grammar
# THE FIVE GLYPHS ARE STRUCTURE. `SEP` is U+00B7 and `ARROW` is U+2192; both are spelled once, here,
# so the parser and the renderers below cannot disagree about a byte.
SEP = " · "
ARROW = " → "
H_ASKS = "## Asks"
H_DISPOSITIONS = "## Dispositions"

STATUS_VERBS = ("CLOSED", "WONTDO", "BLOCKED", "DEFERRED", "KEEP", "REOPEN")
SEV_VERB = "SEV"
PROVENANCE_VERB = "RELOCATED"
SEVERITIES = ("BLOCKER", "HIGH", "MED", "LOW")
DISPOSALS = ("kept", "dropped", "amended")
# A DERIVED token is never a verb. Somebody will write `- SPECCED . <id> . why`, because that is what
# the shard rows they are migrating from look like; V5 names the mistake instead of letting the line
# read as prose. `WITHDRAWN` is in the same list for the same reason, and its remedy names WONTDO.
NON_VERBS = ("SPECCED", "INPROGRESS", "OPEN", "WITHDRAWN")

# TOOL-dDerivedDocket-15 — THE CLAUSE TAIL. Six labels, closed, and spelled once here so the ask
# reader, the SCOPE reader, the merge and every verdict below read the same set. The order is the
# grammar's own and carries no meaning: a tail is read RIGHT TO LEFT, so the written order of two
# clauses never decides anything.
CLAUSE_LABELS = ("seen", "accept", "out", "may", "verify", "data")
# The disposition-file verb that adds clauses to somebody else's ask WITHOUT touching its home
# folder. Upper case, as every verb in that section is. It derives no status, which is why it is a
# row class of its own rather than a seventh `STATUS_VERBS` member — a reader that folds statuses
# must not have to remember to skip it.
SCOPE_VERB = "SCOPE"
# THE `may` VALUE THAT IS NOT A GRANT. Spelled once because the merge ABSORBS it: a row saying
# `may none` beside a row naming a path merges to the path, and two spellings of this token would
# make one of those rows a grant nobody wrote.
GRANT_NONE = "none"

MODES = ("shards", "builds")
MODE_KEY = "BACKLOG_MODE"
CUTOFF_KEY = "ASK_CUTOFF"
# The view's summary column, in characters. A CAP and not a target: every other cell is a
# bounded token, so this key alone decides whether a view row fits the entry budget the hygiene
# engine grades. It is read with `read_excerpt_chars`, which REFUSES an unusable value rather
# than falling back — a silent fallback re-cuts every summary in the tree and says nothing.
EXCERPT_KEY = "BACKLOG_EXCERPT_CHARS"
EXCERPT_DEFAULT = 72

TERMINAL = ("CLOSED", "WONTDO")
UNRESOLVED = "UNRESOLVED"
UNLABELLED = "unlabelled"
LEGACY_TOKENS = ("OPEN", "SPECCED", "INPROGRESS", "BLOCKED", "DEFERRED", "CLOSED", "WONTDO",
                 "WITHDRAWN")

# A zero-padded DATE, so a plain string comparison IS a date comparison. `2026-9-30` is refused by
# V16 rather than accepted, because `"2026-10-01" < "2026-9-30"` is true and an October ask would
# then sort before a September cutoff and silently disarm V9 and V12.
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SHA_RE = re.compile(r"^[0-9a-f]{7,40}$")
# A build folder slug. Disjoint from a SHA by construction: every slug in this corpus carries an
# upper-case letter (the node tag plus a CamelCase adjective-noun) and a SHA carries none.
SLUG_RE = re.compile(r"^(?=.*[A-Z])[A-Za-z0-9]+$")

# THE THREE LOCATOR FORMS OF §4, and the one shape fix F6 forbids, each anchored at BOTH ends. A
# locator is the whole value or it is not a locator: an unanchored form would read the first legal
# prefix of a typo as a pinned path and report the ask located, which is the exact state F6 exists
# to refuse.
SEEN_PINNED_RE = re.compile(r"^`(?P<path>[^`]+)`@(?P<sha>[0-9a-f]{7,40})(?::(?P<line>\d+))?$")
SEEN_MATCHING_RE = re.compile(r"^`(?P<path>[^`]+)` matching `(?P<pattern>[^`]+)`$")
SEEN_EXTERNAL_RE = re.compile(
    r"^(?P<repo>[A-Za-z0-9][A-Za-z0-9._-]*):(?P<path>[^`@\s]+)@(?P<sha>[0-9a-f]{7,40})$")
#: FIX F6's whole subject: a path and a line with no pinned commit. Matched SEPARATELY so the
#: verdict can say WHICH mistake was made — "not a locator" sends a reader looking for a typo, and
#: the mistake is that a line number moves and the ask then points at nothing while still reading
#: located.
SEEN_BARE_LINE_RE = re.compile(r"^`(?P<path>[^`]+)`:(?P<line>\d+)$")
#: The optional command tail. NON-GREEDY on the locator and anchored on the closing backtick, so a
#: locator whose own path carries the word `run` keeps it.
SEEN_RUN_RE = re.compile(r"^(?P<locator>.*\S) run `(?P<command>[^`]+)`$")

Grammar = collections.namedtuple("Grammar", "families id_re")
Row = collections.namedtuple("Row", "cls code verb target value why extra path slug line raw")
#: `clauses` is the tuple of (label, value) pairs a row carried, in WRITTEN order, duplicates
#: included — a duplicate is V13's finding and dropping it here would answer the verdict before it
#: was asked. It defaults to empty, so every construction site that predates the tail is unchanged.
Ask = collections.namedtuple("Ask", "id path slug filed unit text pointer line clauses",
                             defaults=((),))
#: One parsed `seen` value. `kind` is `pinned`, `matching` or `external`, or "" with `why` set —
#: never an exception, because a `seen` is CONTENT and content never raises in this module.
Seen = collections.namedtuple("Seen", "kind path sha line pattern command why")
#: One ask's READY answer. `missing` is the failing rules in rule order; `closers` carries a foreign
#: live spec R2 admitted under a `stale:` prefix, which is how a stale claim is named without a
#: fourth grade (§8 F2).
Ready = collections.namedtuple("Ready", "grade missing holds grant closers")
Verdict = collections.namedtuple("Verdict", "code text files")
Conf = collections.namedtuple("Conf", "mode cutoff verdicts")
Legacy = collections.namedtuple("Legacy", "id status withdrawn body why")
Parsed = collections.namedtuple("Parsed", "path slug asks rows verdicts")
Spec = collections.namedtuple("Spec", "id path status closes advances")
Corpus = collections.namedtuple("Corpus", "files specs builds")
Fold = collections.namedtuple("Fold", "statuses decided severities counts")


class Problem(Exception):
    """A named, user-facing failure. Never a traceback, and never raised by CONTENT."""


FAMILY_SHAPE = re.compile(r"^[A-Za-z][A-Za-z0-9]*$")


def build_grammar(families) -> Grammar:
    """The id grammar bound to ONE families list.

    Bound to the CALLER's list and never to this repo's. A grammar built from the wrong tree
    recognises nothing, an empty classification is what a clean corpus yields, and the failure then
    looks exactly like success — the defect `corpus_ids.py` measured on its own first run. An empty
    list therefore compiles to `(?!)`, which matches nothing and says so at every call site rather
    than quietly admitting everything.

    EVERY FAMILY IS VALIDATED, NOT ESCAPED. These tokens are spliced into a regex, and a conf value
    reaching `re.compile` is a class this repo has measured: escaping it makes a quoted value match
    nothing, and passing it through lets a `|` swallow a subtree — both silently, both looking like
    a clean corpus. A family is `[A-Za-z][A-Za-z0-9]*` and anything else REFUSES by name, which is
    the one outcome a reader can act on.
    """
    fams = [f for f in families if f]
    bad = [f for f in fams if not FAMILY_SHAPE.match(f)]
    if bad:
        raise Problem(f"family name(s) {' '.join(sorted(bad))} are not [A-Za-z][A-Za-z0-9]*, and "
                      f"these go into a regex, where a stray metacharacter silently re-scopes the "
                      f"id grammar instead of failing")
    alt = "|".join(sorted(set(fams))) or "(?!)"
    return Grammar(tuple(sorted(set(fams))),
                   re.compile(r"^(?:" + alt + r")-[A-Za-z0-9]+-\d+$"))


def check_id(token: str, grammar: Grammar) -> bool:
    """Is this token a well-formed id under that grammar? One predicate, used by every shape."""
    return bool(token) and bool(grammar.id_re.match(token))


# ------------------------------------------------------------------------------------ the conf keys
def read_conf(conf: dict) -> Conf:
    """`BACKLOG_MODE` and `ASK_CUTOFF`, with the two conf verdicts they can raise.

    THE MODE KEY'S SPELLING IS FROZEN FOREVER (design A1): the transition audit classifies a commit
    by it, so renaming it would make every commit before the rename unclassifiable.

    An unrecognised mode RAISES rather than reading as `shards`. Defaulting it would mean a typo
    silently keeps the old renderer alive after a tree has migrated to the new one, and a migration
    that half-happened is worse than one that refused.
    """
    raw = (conf.get(MODE_KEY) or "").strip()
    mode = raw or MODES[0]
    if mode not in MODES:
        raise Problem(f"{MODE_KEY}='{raw}' is not one of: {' '.join(MODES)}")
    cutoff = (conf.get(CUTOFF_KEY) or "").strip()
    verdicts = []
    # UNDER `shards` THE CUTOFF IS NOT READ. Nothing this module arms with it is live in that mode,
    # so grading it would red a tree for a key it does not yet use.
    if mode == "builds":
        if not cutoff:
            verdicts.append(Verdict(15, f"{CUTOFF_KEY} is blank while {MODE_KEY} is `builds`, so "
                                        f"the forward-only verdicts V9 and V12 are disarmed", ()))
        elif not DATE_RE.match(cutoff):
            verdicts.append(Verdict(16, f"{CUTOFF_KEY}='{cutoff}' is not a zero-padded YYYY-MM-DD "
                                        f"date, so a string comparison against it is not a date "
                                        f"comparison and V9 and V12 are disarmed", ()))
    return Conf(mode, cutoff, tuple(verdicts))


def check_cutoff_armed(conf: Conf) -> bool:
    """Are the forward-only verdicts live? False whenever V15 or V16 fired, or the mode is shards."""
    return conf.mode == "builds" and not conf.verdicts


# -------------------------------------------------------------------------------- the row classifier
def extract_row(line: str, grammar: Grammar) -> Row | None:
    """The ONE classifier: any physical line's row class and target, or None when it is not a row.

    Every other reader in this kit — the duplicate census, the transition audit, the relocation
    engine, the planner — asks this function rather than spelling the grammar a second time. A
    second spelling is two answers to one question, and the copy is always the one that rots.

    `cls` is one of `ask`, `status`, `severity`, `provenance` or `unknown`. An `unknown` row carries
    the verdict `code` it owes (2, or 5 for a derived token used as a verb) and the reason in `why`,
    so the file walk can report it without re-deciding anything.
    """
    if not line.startswith("- "):
        return None
    body = line[2:]
    head = body.split(SEP, 1)[0]
    blank = Row("unknown", 2, head, "", "", "", {}, "", "", 0, line)
    if head in NON_VERBS:
        remedy = ("write the disposition as a `WONTDO` row" if head == "WITHDRAWN"
                  else "a derived status is never written down; it is folded from the records")
        return blank._replace(code=5, why=f"`{head}` is a DERIVED status token, not a verb — {remedy}")
    if check_id(head, grammar):
        return _extract_ask(body, head, line)
    if head in STATUS_VERBS:
        return _extract_status(body, head, line, grammar)
    if head == SEV_VERB:
        return _extract_sev(body, line, grammar)
    if head == SCOPE_VERB:
        return _extract_scope(body, line, grammar)
    if head == PROVENANCE_VERB:
        return _extract_provenance(body, line, grammar)
    return blank._replace(why=f"leads with `{head}`, which is neither an id nor a declared verb")


def _extract_ask(body: str, ask_id: str, line: str) -> Row:
    blank = Row("unknown", 2, "", ask_id, "", "", {}, "", "", 0, line)
    parts = body.split(SEP, 2)
    if len(parts) < 3:
        return blank._replace(why="an ask row is `<id> . filed <date> [. unit] . <text>`")
    if not parts[1].startswith("filed "):
        return blank._replace(why=f"the field after the id is `{parts[1]}`, not `filed <date>`")
    filed = parts[1][len("filed "):]
    if not DATE_RE.match(filed):
        return blank._replace(why=f"`filed {filed}` is not a zero-padded YYYY-MM-DD date")
    rest, unit = parts[2], False
    # `unit` IS RECOGNISED ONLY AS THE WHOLE FIELD after `filed`. A TEXT that happens to be exactly
    # the word `unit` is therefore read as the marker and refused for carrying no text, which is the
    # stated risk rather than a silent misread.
    if rest == "unit":
        unit, rest = True, ""
    elif rest.startswith("unit" + SEP):
        unit, rest = True, rest[len("unit" + SEP):]
    text, arrow, pointer = rest.rpartition(ARROW)
    if not arrow:
        text, pointer = rest, ""
    # THE TAIL IS READ BEFORE THE TEXT IS GRADED, and off the pointer-stripped remainder, because
    # the grammar puts the pointer LAST: `TEXT CLAUSE* [" → " POINTER]`.
    text, clauses = extract_clauses(text)
    if not text.strip():
        return blank._replace(why="the ask text is empty")
    if arrow and not pointer.strip():
        return blank._replace(why="the pointer after the arrow is empty")
    return Row("ask", 0, "", ask_id, filed, text,
               {"unit": unit, "pointer": pointer, "clauses": clauses}, "", "", 0, line)


def extract_clauses(rest: str) -> tuple:
    """`(text, clauses)` — the clause tail of a row body, read RIGHT TO LEFT.

    RIGHT TO LEFT IS THE WHOLE RULE, and it is not a preference. Left to right, an ask TEXT that
    happens to contain ` · out ` would swallow every real clause after it into one free-text value
    and the row would grade as carrying no acceptance at all — silently, which is the one outcome
    this grammar may not have. Read from the right, that TEXT costs the writer exactly the one
    clause it collides with, and the misread lands as a clause whose value then fails its grammar
    and is named by V13.

    THE LAST SEGMENT IS ALWAYS TEXT. `TEXT` is mandatory in the grammar, so the walk stops with one
    segment left however many of them look like labels — a row that is nothing but clauses keeps
    its first as the text rather than parsing to an ask with no subject.

    A SEGMENT WHOSE FIRST TOKEN IS A LABEL IS A CLAUSE EVEN WITH NO VALUE. `· out ·` is read as an
    `out` clause carrying nothing, which V13 names; read as prose instead it would be TEXT, and the
    two clauses beyond it would be swallowed exactly as the left-to-right reading swallows them.

    DUPLICATES SURVIVE. The pairs come back in written order with nothing deduplicated, because
    "this label is written twice" is a verdict somebody must be told about and a reader that folded
    them here would answer it before it was asked.
    """
    parts = rest.split(SEP)
    found: list = []
    while len(parts) > 1:
        head = parts[-1].split(" ", 1)
        if head[0] not in CLAUSE_LABELS:
            break
        found.append((head[0], head[1].strip() if len(head) > 1 else ""))
        parts.pop()
    found.reverse()
    return SEP.join(parts), tuple(found)


def _extract_scope(body: str, line: str, grammar: Grammar) -> Row:
    """`- SCOPE · <id> · <clause>+` — clauses added to an ask from OUTSIDE its home folder.

    EVERY FIELD AFTER THE ID IS A CLAUSE, and one that is not REFUSES the row rather than being
    read as prose: a SCOPE row has no TEXT slot for prose to land in, so admitting it would file an
    unreadable field under a label nobody wrote.
    """
    parts = body.split(SEP)
    blank = Row("unknown", 2, SCOPE_VERB, "", "", "", {}, "", "", 0, line)
    if len(parts) < 3:
        return blank._replace(why=f"a {SCOPE_VERB} row is `{SCOPE_VERB} . <id> . <label> <value>` "
                                  f"and carries at least one clause")
    if not check_id(parts[1], grammar):
        return blank._replace(why=f"`{parts[1]}` is not a well-formed id")
    blank = blank._replace(target=parts[1])
    pairs = []
    for field in parts[2:]:
        head = field.split(" ", 1)
        if head[0] not in CLAUSE_LABELS:
            return blank._replace(why=f"the field `{field}` does not lead with a clause label; the "
                                      f"labels are {' '.join(CLAUSE_LABELS)}")
        pairs.append((head[0], head[1].strip() if len(head) > 1 else ""))
    return Row("scope", 0, SCOPE_VERB, parts[1], "", "", {"clauses": tuple(pairs)}, "", "", 0, line)


# ------------------------------------------------------------------- the clause VALUE grammars
def read_clause_values(pairs, label: str) -> list:
    """Every value written under one label, in order. The ONE accessor over a clause tuple."""
    return [v for lab, v in pairs if lab == label]


def parse_seen(value: str) -> Seen:
    """One `seen` value as `Seen`. NEVER raises: an unreadable value comes back with `why` set.

    THE COMMAND TAIL IS STRIPPED FIRST, because the locator forms are anchored at both ends and a
    value carrying a command would otherwise match none of them and report as a malformed locator
    when the locator was fine.

    FIX F6 IS A NAMED CASE, not a fall-through. `` `path`:23 `` is recognised and refused with the
    reason — a line number moves, and the ask then points at nothing while still reading located.
    """
    locator, command = value.strip(), ""
    run = SEEN_RUN_RE.match(locator)
    if run:
        locator, command = run.group("locator"), run.group("command")
    if not locator:
        return Seen("", "", "", "", "", command, "carries no locator")
    pin = SEEN_PINNED_RE.match(locator)
    if pin:
        return Seen("pinned", pin.group("path"), pin.group("sha"), pin.group("line") or "", "",
                    command, "")
    match = SEEN_MATCHING_RE.match(locator)
    if match:
        return Seen("matching", match.group("path"), "", "", match.group("pattern"), command, "")
    ext = SEEN_EXTERNAL_RE.match(locator)
    if ext:
        return Seen("external", ext.group("path"), ext.group("sha"), "", "", command, "")
    bare = SEEN_BARE_LINE_RE.match(locator)
    if bare:
        return Seen("", bare.group("path"), "", bare.group("line"), "", command,
                    f"{locator} pins a line and no commit; a line MOVES, and the ask would then "
                    f"point at nothing while still reading located — write "
                    f"`` `path`@<sha>[:line] `` or `` `path` matching `pattern` ``")
    return Seen("", "", "", "", "", command,
                f"{locator} is none of the three locator forms: `` `path`@<sha>[:line] ``, "
                f"`` `path` matching `pattern` ``, or `<repo>:<path>@<sha>`")


def extract_grants(value: str) -> tuple:
    """`(grants, why)` for one `may` value. `('none',)` is the absorbed token, never a grant.

    TOKENISED RATHER THAN SPLIT, because a granted PATH is backticked and a backticked path may
    carry a space. A bare `.split()` would shred one grant into two, and each half would then fail
    the id test and report as two mistakes where the writer made none.
    """
    raw = value.strip()
    if raw == GRANT_NONE:
        return (GRANT_NONE,), ""
    out, i = [], 0
    while i < len(raw):
        if raw[i] == " ":
            i += 1
            continue
        if raw[i] == "`":
            end = raw.find("`", i + 1)
            if end < 0:
                return (), f"`{raw}` carries a grant whose opening backtick is never closed"
            out.append(raw[i:end + 1])
            i = end + 1
            if i < len(raw) and raw[i] != " ":
                return (), f"`{raw}` runs a backticked grant straight into the next token"
            continue
        end = raw.find(" ", i)
        end = len(raw) if end < 0 else end
        out.append(raw[i:end])
        i = end
    if not out:
        return (), "carries no grant"
    if GRANT_NONE in out:
        return (), (f"`{raw}` writes `{GRANT_NONE}` beside a grant; `{GRANT_NONE}` is the value "
                    f"that grants NOTHING, and a row cannot say both")
    return tuple(out), ""


#: A GRANT's id half, graded by SHAPE and deliberately NOT against the declared family allowlist. A
#: `may` names a DECISION id, and a decision family is not necessarily one of the families a
#: build's asks are filed under — grading it against the backlog allowlist would refuse a
#: legitimate grant on any tree whose two sets differ. Whether the id RESOLVES is the question the
#: unit that HONOURS a grant asks, at the moment it honours one.
GRANT_ID_RE = re.compile(r"^[A-Za-z][A-Za-z0-9]*-[A-Za-z0-9]+-\d+$")


def check_grant(grant: str) -> bool:
    """Is this token a GRANT? A backticked path, or an id-shaped token. See `GRANT_ID_RE`."""
    return bool(grant.startswith("`") and grant.endswith("`") and len(grant) > 2) \
        or bool(GRANT_ID_RE.match(grant))


def derive_grants(values) -> tuple:
    """Every `may` value merged: a UNION of grants in which `none` is ABSORBED.

    `()` when no clause was written at all, `('none',)` when every clause said `none`, and the
    sorted union otherwise. Absorbed rather than conflicting, because `none` is the value a writer
    puts on a row to say THEIR row grants nothing — it was never a claim about anybody else's.
    """
    if not values:
        return ()
    grants: set = set()
    for value in values:
        got, _why = extract_grants(value)
        grants.update(g for g in got if g != GRANT_NONE)
    return tuple(sorted(grants)) if grants else (GRANT_NONE,)


def _read_slot(field: str, keyword: str):
    """`by <value>` -> `<value>`, or None when the slot is absent or empty. One reader, four slots."""
    lead = keyword + " "
    if not field.startswith(lead):
        return None
    return field[len(lead):].strip() or None


def _extract_status(body: str, verb: str, line: str, grammar: Grammar) -> Row:
    slots = {"CLOSED": "by", "BLOCKED": "on", "DEFERRED": "until", "REOPEN": "of"}
    want = 4 if verb in slots else 3
    parts = body.split(SEP, want - 1)
    blank = Row("unknown", 2, verb, "", "", "", {}, "", "", 0, line)
    if len(parts) < want:
        shape = (f"`{verb} . <id> . {slots[verb]} <value> . <why>`" if verb in slots
                 else f"`{verb} . <id> . <why>`")
        return blank._replace(why=f"a {verb} row is {shape}")
    target = parts[1]
    if not check_id(target, grammar):
        return blank._replace(why=f"`{target}` is not a well-formed id")
    blank = blank._replace(target=target)
    value = ""
    if verb in slots:
        value = _read_slot(parts[2], slots[verb])
        if value is None:
            return blank._replace(why=f"the third field is `{parts[2]}`, not `{slots[verb]} <value>`")
        if verb == "CLOSED" and not (check_id(value, grammar) or SHA_RE.match(value)):
            return blank._replace(why=f"`by {value}` is neither an id nor a 7-to-40 hex sha")
        if verb in ("BLOCKED", "DEFERRED") and not check_id(value, grammar):
            return blank._replace(why=f"`{slots[verb]} {value}` is not a well-formed id")
        if verb == "REOPEN" and not (check_id(value, grammar) or SHA_RE.match(value)
                                     or SLUG_RE.match(value)):
            return blank._replace(why=f"`of {value}` is neither an id, a sha nor a build slug")
    why = parts[want - 1]
    if not why.strip():
        return blank._replace(why=f"a {verb} row's why is empty")
    return Row("status", 0, verb, target, value, why, {}, "", "", 0, line)


def _extract_sev(body: str, line: str, grammar: Grammar) -> Row:
    parts = body.split(SEP, 3)
    blank = Row("unknown", 2, SEV_VERB, "", "", "", {}, "", "", 0, line)
    if len(parts) < 4:
        return blank._replace(why="a SEV row is `SEV . <id> . <BLOCKER|HIGH|MED|LOW> . <why>`")
    if not check_id(parts[1], grammar):
        return blank._replace(why=f"`{parts[1]}` is not a well-formed id")
    blank = blank._replace(target=parts[1])
    if parts[2] not in SEVERITIES:
        return blank._replace(why=f"`{parts[2]}` is not one of: {' '.join(SEVERITIES)}")
    if not parts[3].strip():
        return blank._replace(why="a SEV row's why is empty")
    return Row("severity", 0, SEV_VERB, parts[1], parts[2], parts[3], {}, "", "", 0, line)


def _extract_provenance(body: str, line: str, grammar: Grammar) -> Row:
    parts = body.split(SEP, 3)
    blank = Row("unknown", 2, PROVENANCE_VERB, "", "", "", {}, "", "", 0, line)
    if len(parts) < 4:
        return blank._replace(why="a RELOCATED row is `RELOCATED . <id> . by <sha> . "
                                  "<kept|dropped|amended>: <why>`")
    if not check_id(parts[1], grammar):
        return blank._replace(why=f"`{parts[1]}` is not a well-formed id")
    blank = blank._replace(target=parts[1])
    sha = _read_slot(parts[2], "by")
    if sha is None or not SHA_RE.match(sha):
        return blank._replace(why=f"the third field is `{parts[2]}`, not `by <7-to-40 hex sha>`")
    disposal, colon, why = parts[3].partition(": ")
    if not colon or disposal not in DISPOSALS:
        return blank._replace(why=f"the fourth field does not lead with one of "
                                  f"{'/'.join(DISPOSALS)} followed by `: `")
    if not why.strip():
        return blank._replace(why="a RELOCATED row's why is empty")
    return Row("provenance", 0, PROVENANCE_VERB, parts[1], sha, why, {"disposal": disposal},
               "", "", 0, line)


# ------------------------------------------------------------------------------------- the file walk
def parse_file(path: str, text: str, grammar: Grammar) -> Parsed:
    """One file's asks, verb rows and per-file verdicts. NEVER raises on content.

    The slug is the file's own parent folder, derived here so no caller has to pass it twice.

    THE WALK REPORTS EVERY LINE IT DID NOT UNDERSTAND. A parser that skips an unrecognised line
    makes a mis-segmented file read exactly like a clean one, which is the shape that lets a whole
    section fall out of a corpus at exit 0.

    THE CALLER OPENS THE FILE WITH `newline=""`, and nothing here depends on its doing so. A CRLF
    file splits on `\\n` and each line's ONE trailing CR is dropped, so a CRLF and an LF copy of one
    file parse identically. A BARE CR mid-line stays inside the field it landed in; every shape test
    is anchored at both ends, so that field fails its test and the line is REPORTED. Under a
    universal-newlines read the same CR arrives as a line break and the row is reported too. Both
    readings are loud, which is the property this note exists to pin — the kit has a gotcha for the
    text-mode read that silently rewrites a bare CR, and this grammar must not be its next victim.
    """
    slug = os.path.basename(os.path.dirname(path.replace("\\", "/").rstrip("/"))) or ""
    asks: list = []
    rows: list = []
    verdicts: list = []

    def add_v2(lineno: int, why: str) -> None:
        verdicts.append(Verdict(2, f"{path}:{lineno}: {why}", (path,)))

    state = "pre"
    seen = set()
    for n, raw in enumerate(text.split("\n"), 1):
        line = raw[:-1] if raw.endswith("\r") else raw
        if not line.strip():
            continue
        if line[0] in " \t":
            add_v2(n, "a continuation line; every row is one physical line")
            continue
        if state == "pre":
            if line.startswith("# ") and not line.startswith("## "):
                state = "head"
            else:
                add_v2(n, "sits above the H1, and a file's first content line is its H1")
            continue
        if line in (H_ASKS, H_DISPOSITIONS):
            if line in seen:
                add_v2(n, f"a second `{line}` heading; each section appears once")
                continue
            seen.add(line)
            state = "asks" if line == H_ASKS else "disp"
            continue
        if line.startswith("#"):
            add_v2(n, f"`{line.split(' ')[0]}` heading; the only headings are "
                      f"`{H_ASKS}` and `{H_DISPOSITIONS}`")
            continue
        if line.startswith(">"):
            if state != "head":
                add_v2(n, "a blockquote below a section heading; the quote belongs under the H1")
            continue
        row = extract_row(line, grammar)
        if row is None:
            add_v2(n, "matches no declared row shape")
            continue
        row = row._replace(path=path, slug=slug, line=n)
        if row.cls == "unknown":
            verdicts.append(Verdict(row.code, f"{path}:{n}: {row.why}", (path,)))
            continue
        if state == "head":
            add_v2(n, f"a row above both section headings; every row sits under `{H_ASKS}` or "
                      f"`{H_DISPOSITIONS}`")
            continue
        if state == "asks" and row.cls != "ask":
            add_v2(n, f"a `{row.verb}` verb row under `{H_ASKS}`; verb rows sit under "
                      f"`{H_DISPOSITIONS}`")
            continue
        if state == "disp" and row.cls == "ask":
            add_v2(n, f"an ask row under `{H_DISPOSITIONS}`; ask rows sit under `{H_ASKS}`")
            continue
        if row.cls == "ask":
            asks.append(Ask(row.target, path, slug, row.value, row.extra["unit"], row.why,
                            row.extra["pointer"], n, row.extra["clauses"]))
        else:
            rows.append(row)

    # V4 IS PER FILE AND PER CLASS. A triage sweep writes a status row AND a SEV row for one ask in
    # one file, and the relocation engine writes a status row AND a RELOCATED row; one rule over
    # every verb row would refuse both designed pairs. Provenance rows are excluded entirely — a
    # relocation may touch one id several times, once per sha.
    for cls in ("status", "severity"):
        first: dict = {}
        for row in rows:
            if row.cls != cls:
                continue
            if row.target in first:
                verdicts.append(Verdict(
                    4, f"{path}: two {cls} rows for {row.target}, at lines {first[row.target]} and "
                       f"{row.line}; one file states one {cls} per target, and a disposer changes "
                       f"its mind by editing its own row", (path,)))
            else:
                first[row.target] = row.line
    if not asks and not rows:
        verdicts.append(Verdict(2, f"{path}: parses to nothing — no ask row and no verb row, which "
                                   f"is indistinguishable from a file the walk mis-segmented",
                                (path,)))
    return Parsed(path, slug, tuple(asks), tuple(rows), tuple(verdicts))


# ------------------------------------------------------------------------------ the legacy row reader
def read_legacy_row(line: str, grammar: Grammar) -> Legacy:
    """ONE physical line of a pre-flip shard or archive, as (id, status, withdrawn, body).

    PERMANENT, and that is why it lives here rather than in the migration that first needed it. The
    transition audit, the relocation tools, the planner and the switch-over all read legacy rows,
    and this reader outlives every other shards-mode path.

    IT NEVER GUESSES. Anything it cannot key returns `id=None` with the reason in `why`, because an
    unreadable line returned as OPEN is a guess that a migration then WRITES DOWN.

    ONE LINE PER CALL. A legacy row wrapped across physical lines is joined by the planner's
    permissive parser, which calls this once per logical row; joining here would need a lookahead
    this signature does not have.
    """
    if not line.startswith("- "):
        return Legacy(None, None, False, "", "not a list row")
    fields = [f.strip() for f in _extract_legacy_fields(line[2:])]
    if len(fields) < 2:
        return Legacy(None, None, False, "", "fewer than two fields, so it carries no status slot")
    head, second = fields[0], fields[1]
    if check_id(head, grammar):
        ident, token, body = head, second, fields[2:]
    elif check_id(second, grammar):
        # STATUS-FIRST. The old shards were authored both ways and both are in the archive.
        ident, token, body = second, head, fields[2:]
    else:
        return Legacy(None, None, False, "", "neither of the first two fields is a well-formed id")
    # THE `CLOSED by <evidence>` SLOT. The token field is `CLOSED by deletion (…)` in 5 live rows,
    # so the token is the FIRST word and the rest of the field is evidence prose that belongs to the
    # body — dropping it would lose the only record of what closed the row.
    lead = token.split(" ", 1)[0]
    if lead not in LEGACY_TOKENS:
        return Legacy(None, None, False, "", f"`{lead}` is not a legacy status token")
    if token != lead:
        body = [token.split(" ", 1)[1]] + body
    withdrawn = lead == "WITHDRAWN"
    return Legacy(ident, "WONTDO" if withdrawn else lead, withdrawn, SEP.join(body).strip(), "")


def _extract_legacy_fields(body: str) -> list:
    """The two legacy separators, tried in the order the corpus uses them.

    Middot first: the ASCII ` - ` form also occurs INSIDE middot-separated prose (a dashed clause),
    so trying ASCII first would shred a well-formed row into fragments. Tried the other way round,
    a genuinely ASCII row simply has no middot and falls through.
    """
    if SEP in body:
        return body.split(SEP)
    return body.split(" - ")


# --------------------------------------------------------------------------- the status-header verbs
_VERBS = ("closes", "advances")
_VERB_LOOSE = {v: re.compile(r"·\s*" + v + r"\b") for v in _VERBS}
_VERB_VALUE = {v: re.compile(r"·\s*" + v + r"\s+([^·]*?)\s*(?=·|$)") for v in _VERBS}


def read_header_verbs(header: str, path: str, expand) -> dict:
    """`closes <ids>` and `advances <ids>` off a spec's status header, expanded.

    Each verb is PERMITTED and never required, exactly as `order` is, so no landed spec goes
    retroactively red and a header carrying neither parses as it always did.

    A malformed value REFUSES rather than being dropped. Dropped, the spec would simply render with
    no link and its ask would never close — a plausible, silent, wrong answer, which is the failure
    mode the `order` verb's own anchoring was rewritten to remove.

    `expand` is the generator's `_expand_ids` bound to this repo's family alternation, passed in
    rather than imported: this module owns no id alternation of its own and must not grow a second
    one.
    """
    out: dict = {}
    for verb in _VERBS:
        hits = _VERB_LOOSE[verb].findall(header)
        if len(hits) > 1:
            raise Problem(f"{path}: status header carries the `{verb}` verb {len(hits)} times, so "
                          f"which asks this spec {verb} has more than one answer")
        if not hits:
            out[verb] = []
            continue
        found = _VERB_VALUE[verb].search(header)
        value = found.group(1) if found else ""
        if not value:
            raise Problem(f"{path}: status header carries `{verb}` with no value, and a verb naming "
                          f"no ask is not a link")
        ids, bad = expand(value)
        if bad:
            raise Problem(f"{path}: status header carries `{verb} {value}`, and "
                          f"{' '.join(bad)} is not an id or an id range")
        out[verb] = ids
    both = sorted(set(out["closes"]) & set(out["advances"]))
    if both:
        raise Problem(f"{path}: status header names {' '.join(both)} under BOTH `closes` and "
                      f"`advances`, and one spec cannot both finish an ask and merely move it")
    return out


# -------------------------------------------------------------------------------------- the corpus
def build_corpus(files, specs=None, builds=None) -> Corpus:
    """The fold's one input: parsed files, a spec index by id, and the caller's build statuses.

    `builds` is the CALLER's map of build slug to derived status. This module never derives one —
    that is `gen_build_index.derive_status`'s job, and re-deriving it here would be a second answer
    to a question the generator already answers.
    """
    specs = dict(specs or {})
    return Corpus(tuple(files), specs, dict(builds or {}))


def _read_asks(corpus: Corpus) -> dict:
    out: dict = {}
    for parsed in corpus.files:
        for ask in parsed.asks:
            out.setdefault(ask.id, ask)
    return out


def _read_rows(corpus: Corpus, cls: str) -> dict:
    out: dict = {}
    for parsed in corpus.files:
        for row in parsed.rows:
            if row.cls == cls:
                out.setdefault(row.target, []).append(row)
    return out


def _read_links(corpus: Corpus, asks: dict) -> tuple:
    """C(A) and P(A), as dicts of ask id -> sorted spec ids.

    C(A) is every spec whose header `closes` A, PLUS A's same-id spec when A carries `unit`. The
    same-id pairing is DECLARED, never inferred: four id pairs in this corpus are a backlog row and
    a spec about different subjects, so inferring the link from equal ids would have closed asks
    nobody closed.
    """
    closing: dict = {a: set() for a in asks}
    advancing: dict = {a: set() for a in asks}
    for spec in corpus.specs.values():
        for ask_id in spec.closes:
            closing.setdefault(ask_id, set()).add(spec.id)
        for ask_id in spec.advances:
            advancing.setdefault(ask_id, set()).add(spec.id)
    for ask_id, ask in asks.items():
        if ask.unit and ask_id in corpus.specs:
            closing.setdefault(ask_id, set()).add(ask_id)
    return ({k: sorted(v) for k, v in closing.items()},
            {k: sorted(v) for k, v in advancing.items()})


# ---------------------------------------------------------------------------------------- the fold
def derive_evidence(corpus: Corpus) -> dict:
    """Per ask: what closes it, what declines it, what it is held on, and which live specs link it.

    ONE computation with TWO readers. Stratum 1 of the fold reads `closing` and `declining` to
    decide terminality; the view unit's `--asks --json` projection publishes all four, and the
    switch-over's drift signals read `closing`, `declining` and `live_specs` by name. Deriving them
    twice would be two answers to one question, and the second copy is the one that rots.

    A NON-`unit` CLOSING SPEC READING WONTDO CONTRIBUTES NOTHING to `declining`. That spec was one
    ATTEMPT at the ask; abandoning the attempt does not decline the ask, and treating it as a
    decline is how a live ask silently disappears.

    Nothing here reads a date, a file order or a row order: every value is the sorted form of a set,
    so a permutation of the corpus returns identical bytes.
    """
    asks = _read_asks(corpus)
    drows = _read_rows(corpus, "status")
    closing_specs, advancing_specs = _read_links(corpus, asks)
    out: dict = {}
    for ask_id, ask in asks.items():
        cancelled = {r.value for r in drows.get(ask_id, []) if r.verb == "REOPEN"}
        closing = sorted(s for s in closing_specs.get(ask_id, [])
                         if s in corpus.specs and corpus.specs[s].status == "CLOSED"
                         and s not in cancelled)
        closing += sorted(r.value for r in drows.get(ask_id, [])
                          if r.verb == "CLOSED" and r.value not in cancelled)
        declining = sorted(r.slug for r in drows.get(ask_id, [])
                           if r.verb == "WONTDO" and r.slug not in cancelled)
        if (ask.unit and ask_id in corpus.specs and corpus.specs[ask_id].status == "WONTDO"
                and ask_id not in cancelled):
            declining.append(ask_id)
        linked = sorted(set(closing_specs.get(ask_id, [])) | set(advancing_specs.get(ask_id, [])))
        out[ask_id] = {
            "closing": closing,
            "declining": declining,
            "holds": sorted({r.value for r in drows.get(ask_id, [])
                             if r.verb in ("BLOCKED", "DEFERRED")}),
            "live_specs": [s for s in linked
                           if s in corpus.specs and corpus.specs[s].status not in TERMINAL],
        }
    return out


def _check_live(asks: dict, specs: dict, statuses: dict, target: str):
    """Is this hold target live? None when it resolves to neither a filed ask nor a spec H1.

    AN ASK WINS A TIE. A target that is both a filed ask and a spec H1 resolves to the ask, because
    the ask is the thing a disposer was holding on when they wrote the row.

    ONE IMPLEMENTATION, TWO BINDINGS. The fold calls it with the statuses stratum 1 has decided so
    far; READY's R3 and the decided-by set call it with the finished fold. A second copy for the
    later readers would be two answers to "is this hold released", and the copy is the one that
    would keep an ask held after its target closed.
    """
    if target in asks:
        return statuses.get(target) not in TERMINAL
    if target in specs:
        return specs[target].status not in TERMINAL
    return None


def check_hold_live(corpus: Corpus, fold: Fold, target: str):
    """`_check_live` bound to a FINISHED fold — the binding every reader outside the fold uses."""
    return _check_live(_read_asks(corpus), corpus.specs, fold.statuses, target)


def derive_clauses(corpus: Corpus) -> dict:
    """Per ask: `{label: (value, …)}`, merged over its ask row and every SCOPE row naming it.

    ONE MERGE, READ BY THREE. V14 asks whether the merged clauses carry an acceptance, READY's R5
    and R6 ask the same question, and `--probe` takes its command from here. A second merge
    anywhere would let a non-filer cure an ask for one reader and not for another (§8 F6).

    FIVE LABELS CONJOIN and `may` is a UNION with `none` absorbed, which is why `may` comes back
    RAW here too: the absorbing fold is `derive_grants`, called by whoever prints or honours a
    grant, so this function stays the one that merely collects.

    ORDER IS THE ASK ROW FIRST, then the SCOPE rows by (path, line). Nothing below reads the order
    — every consumer either asks "is there one" or iterates all of them — but a stable one means a
    printed detail view returns identical bytes for a permuted corpus.
    """
    asks = _read_asks(corpus)
    out: dict = {a: {} for a in asks}
    rows = sorted((r for p in corpus.files for r in p.rows if r.cls == "scope"),
                  key=lambda r: (r.path, r.line))
    pairs: dict = {a: list(asks[a].clauses) for a in asks}
    for row in rows:
        if row.target in pairs:
            pairs[row.target].extend(row.extra["clauses"])
    for ask_id, got in pairs.items():
        out[ask_id] = {lab: tuple(read_clause_values(got, lab)) for lab in CLAUSE_LABELS
                       if read_clause_values(got, lab)}
    return out


def derive_statuses(corpus: Corpus, verdicts=None) -> Fold:
    """Every ask's status, its Decided-by, and its severity — a function of SETS and nothing else.

    TWO STRATA, AND THAT IS THE WHOLE DESIGN. Stratum 1 decides terminality reading no hold at all;
    stratum 2 reads stratum 1. So a hold's release needs only its target's terminality, every
    status is decidable in two passes with no recursion, and a hold CYCLE is a deadlock the verdicts
    name rather than a status nobody can compute.

    NOTHING HERE READS A DATE, A FILE ORDER OR A ROW ORDER. A date-ordered fold was the rejected
    alternative: a rev bump re-dates a spec and would change a status, same-day ties have no honest
    rule, and merge order would end up deciding. Every rule below is a set test, and every value it
    NAMES is the minimum of a sorted set, so a permutation of the corpus returns identical bytes.
    """
    asks = _read_asks(corpus)
    drows = _read_rows(corpus, "status")
    sevrows = _read_rows(corpus, "severity")
    closing_specs, advancing_specs = _read_links(corpus, asks)
    evidence = derive_evidence(corpus)

    statuses: dict = {}
    decided: dict = {}

    # ---- stratum 1: terminality, reading no holds. The two SETS are `derive_evidence`'s, which the
    # view unit's print modes also read. Computing them a second time here would be two answers to
    # the one question "what closed this ask", and the copy is always the one that rots.
    for ask_id in asks:
        closers = evidence[ask_id]["closing"]
        if closers:
            statuses[ask_id] = "CLOSED"
            decided[ask_id] = sorted(closers)[0]
            continue
        decliners = evidence[ask_id]["declining"]
        if decliners:
            statuses[ask_id] = "WONTDO"
            decided[ask_id] = sorted(decliners)[0]

    def check_live(target: str):
        """This fold's own binding of `_check_live`, over the statuses stratum 1 has decided."""
        return _check_live(asks, corpus.specs, statuses, target)

    # ---- stratum 2: live asks only
    for ask_id in asks:
        if ask_id in statuses:
            continue
        linked = sorted(set(closing_specs.get(ask_id, [])) | set(advancing_specs.get(ask_id, [])))
        linked = [s for s in linked if s in corpus.specs]
        for token, rule in (("INPROGRESS", ("INPROGRESS",)), ("SPECCED", ("OPEN", "SPECCED"))):
            hit = [s for s in linked if corpus.specs[s].status in rule]
            if hit:
                statuses[ask_id], decided[ask_id] = token, hit[0]
                break
        if ask_id in statuses:
            continue
        undecidable = ""
        for token, verb in (("BLOCKED", "BLOCKED"), ("DEFERRED", "DEFERRED")):
            hit = [s for s in linked if corpus.specs[s].status == token]
            held = []
            for row in sorted((r for r in drows.get(ask_id, []) if r.verb == verb),
                              key=lambda r: (r.value, r.path, r.line)):
                live = check_live(row.value)
                if live is None:
                    undecidable = undecidable or row.value
                elif live:
                    held.append(row.value)
            if hit or held:
                statuses[ask_id] = token
                decided[ask_id] = sorted(hit + held)[0]
                break
        if ask_id in statuses:
            continue
        if undecidable:
            # THE PLACEHOLDER IS FOR A TARGET THAT NAMES NOTHING, never for a cycle. A cycle's
            # members are all decidable — terminality reads no hold — so they render their TRUE
            # token and V6 names the cycle beside them.
            statuses[ask_id] = UNRESOLVED
            decided[ask_id] = undecidable
            continue
        statuses[ask_id] = "OPEN"
        decided[ask_id] = ""

    severities = {}
    for ask_id in asks:
        levels = [r.value for r in sevrows.get(ask_id, [])]
        severities[ask_id] = (min(levels, key=SEVERITIES.index) if levels else UNLABELLED)

    counts = {
        "files": len(corpus.files),
        "asks": len(asks),
        "rows": sum(len(p.rows) for p in corpus.files),
        "links": sum(len(v) for v in closing_specs.values())
        + sum(len(v) for v in advancing_specs.values()),
        "live": sum(1 for s in statuses.values() if s not in TERMINAL),
        # NOT MEASURED HERE WHEN NOTHING IS PASSED, and `None` says so. The cross-file verdicts are
        # `derive_verdicts`' to compute, and a 0 standing for "nobody asked" is exactly the
        # reassuring zero a liveness line must never print.
        "verdicts": None if verdicts is None else len(verdicts),
    }
    return Fold(statuses, decided, severities, counts)


# ------------------------------------------------------------------------------------- the verdicts
# EVERY CODE THIS MODULE CAN PRODUCE, DECLARED AS DATA. A consumer reports verdicts by
# ITERATING this tuple, never by retyping the list into a chain of branches: a code added below
# with no reporting arm then reds the view unit's selftest instead of vanishing from a check
# that looks green. V13 and V14 ARRIVED with the envelope unit (TOOL-dDerivedDocket-15) and join
# this tuple rather than opening a list of their own; the two conf-reader codes are present,
# because `derive_verdicts` returns them with the rest.
VERDICT_CODES = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)


def derive_verdicts(corpus: Corpus, conf: Conf) -> list:
    """V1 to V12, V15 and V16, as DATA. None of them raises and none of them is a status.

    Every cross-file verdict names the records on BOTH sides, because a verdict can be green on each
    branch and red only after their merge — and the lander who meets it then has to find the other
    half before they can fix either.
    """
    out: list = list(conf.verdicts)
    for parsed in corpus.files:
        out.extend(parsed.verdicts)

    asks = _read_asks(corpus)
    drows = _read_rows(corpus, "status")
    sevrows = _read_rows(corpus, "severity")
    closing_specs, advancing_specs = _read_links(corpus, asks)
    fold = derive_statuses(corpus)

    # V1 — the ask's id slug against the folder it is filed in.
    for parsed in corpus.files:
        for ask in parsed.asks:
            slug = ask.id.split("-")[1] if ask.id.count("-") >= 2 else ""
            if parsed.slug and slug and slug != parsed.slug:
                out.append(Verdict(1, f"{ask.path}:{ask.line}: ask {ask.id} carries slug `{slug}` "
                                      f"and is filed in build folder `{parsed.slug}`", (ask.path,)))

    # V3 — two ask rows for one id, anywhere. Named from both sides: on one branch each file is
    # clean, and the pair only exists after the merge.
    seen: dict = {}
    for parsed in corpus.files:
        for ask in parsed.asks:
            if ask.id in seen:
                first = seen[ask.id]
                out.append(Verdict(3, f"ask {ask.id} has two ask rows: {first.path}:{first.line} "
                                      f"(build `{first.slug}`) and {ask.path}:{ask.line} "
                                      f"(build `{ask.slug}`)", (first.path, ask.path)))
            else:
                seen[ask.id] = ask

    # V7 — a verb-row target, or a `closes`/`advances` id, that is no filed ask.
    # A SCOPE ROW IS EXCLUDED, and V13 owns that case instead. Both verdicts would name the same
    # unfiled target with the same remedy, and one finding reported under two codes is two answers
    # to one question — the reader then has to work out whether they are looking at one mistake or
    # two before they can fix either.
    for parsed in corpus.files:
        for row in parsed.rows:
            if row.cls == "scope":
                continue
            if row.target not in asks:
                out.append(Verdict(7, f"{row.path}:{row.line}: the {row.verb} row targets "
                                      f"{row.target}, which no ask row in any of the "
                                      f"{len(corpus.files)} file(s) read files", (row.path,)))
    for spec in sorted(corpus.specs.values()):
        for verb, ids in (("closes", spec.closes), ("advances", spec.advances)):
            for ask_id in ids:
                if ask_id not in asks:
                    out.append(Verdict(7, f"{spec.path}: the status header `{verb}` names "
                                          f"{ask_id}, which no ask row in any file files",
                                       (spec.path,)))

    # V8 — a CLOSED row's evidence. A SHA is SHAPE-CHECKED ONLY: resolving one would need git, and
    # this module reads no history by design.
    for parsed in corpus.files:
        for row in parsed.rows:
            if row.verb != "CLOSED" or SHA_RE.match(row.value):
                continue
            if row.value not in asks and row.value not in corpus.specs:
                where = corpus.specs[row.target].path if row.target in corpus.specs else "no spec"
                out.append(Verdict(8, f"{row.path}:{row.line}: CLOSED by {row.value}, which is "
                                      f"neither a filed ask nor a spec H1 ({where})", (row.path,)))

    # V6 — hold targets: unresolvable, self-held, and cycles among live asks.
    edges: dict = {}
    for ask_id, rows in drows.items():
        for row in rows:
            if row.verb not in ("BLOCKED", "DEFERRED"):
                continue
            if row.target == row.value:
                out.append(Verdict(6, f"{row.path}:{row.line}: {row.verb} on itself; an ask cannot "
                                      f"release its own hold", (row.path,)))
                continue
            if row.value not in asks and row.value not in corpus.specs:
                out.append(Verdict(6, f"{row.path}:{row.line}: {row.verb} on {row.value}, which is "
                                      f"neither a filed ask nor a spec H1, so this ask's status is "
                                      f"{UNRESOLVED}", (row.path,)))
                continue
            if row.value in asks and fold.statuses.get(ask_id) not in TERMINAL:
                edges.setdefault(ask_id, set()).add(row.value)
    for cycle in _scan_cycles(edges, fold):
        files = tuple(dict.fromkeys(asks[i].path for i in cycle))
        out.append(Verdict(6, "a hold cycle among live asks: "
                              + " -> ".join(list(cycle) + [cycle[0]])
                              + "; the files are " + ", ".join(files)
                              + " and the builds are "
                              + ", ".join(dict.fromkeys(asks[i].slug for i in cycle)), files))

    # V11 — a REOPEN naming no record that currently closes or declines its target.
    for ask_id, rows in drows.items():
        for row in rows:
            if row.verb != "REOPEN":
                continue
            spec = corpus.specs.get(row.value)
            named = bool(spec and spec.status == "CLOSED" and row.value in closing_specs.get(ask_id, []))
            named = named or any(r.verb == "CLOSED" and r.value == row.value
                                 for r in drows.get(ask_id, []))
            named = named or any(r.verb == "WONTDO" and r.slug == row.value
                                 for r in drows.get(ask_id, []))
            if not named:
                where = spec.path if spec else "no such spec"
                out.append(Verdict(11, f"{row.path}:{row.line}: REOPEN of {row.value} ({where}), "
                                       f"which closes or declines nothing for {ask_id} today",
                                   (row.path,)))

    # V10 — the closeout join, RETROACTIVE over every finished build. A REOPEN counts as that ask's
    # KEEP: the row exists, somebody looked, and the question this verdict asks is whether anybody
    # did.
    for parsed in corpus.files:
        if corpus.builds.get(parsed.slug) not in TERMINAL:
            continue
        for ask in parsed.asks:
            if fold.statuses.get(ask.id) == "OPEN" and not drows.get(ask.id):
                out.append(Verdict(10, f"{ask.path}:{ask.line}: build `{parsed.slug}` is "
                                       f"{corpus.builds.get(parsed.slug)} and {ask.id} derives OPEN "
                                       f"with no status row in any of the {len(corpus.files)} "
                                       f"file(s) read", (ask.path,)))

    # V13 — the clause tail's own grammar, over BOTH row kinds. Not forward-only: a malformed
    # clause is a value nobody can read at any date, and a legacy row carries no clause at all, so
    # arming this retroactively reds nothing that was written before the tail existed.
    out.extend(_scan_clause_grammar(corpus, asks))

    # V14 — owner ruling D12-d, FORWARD-ONLY and read off the MERGED clauses (§8 F6), so a SCOPE
    # row written by a non-filer cures an ask exactly as READY's R5 says it does. Disarmed by
    # either conf verdict, like V9 and V12, and for the same reason.
    if check_cutoff_armed(conf):
        merged = derive_clauses(corpus)
        for parsed in corpus.files:
            for ask in parsed.asks:
                if ask.filed < conf.cutoff:
                    continue
                clauses = merged.get(ask.id, {})
                if clauses.get("accept"):
                    continue
                if any(parse_seen(v).command for v in clauses.get("seen", ())):
                    continue
                out.append(Verdict(14, f"{ask.path}:{ask.line}: {ask.id} is filed on or after "
                                       f"{conf.cutoff} and its merged clauses carry neither "
                                       f"`accept` nor a `seen … run`, so nothing states what done "
                                       f"MEANS for it and no run could execute it unasked",
                                   (ask.path,)))

    # V9 and V12 — forward-only, and DISARMED by either conf verdict. They are reported as absent
    # rather than silently skipped: V15 or V16 is already in `out` saying why.
    if check_cutoff_armed(conf):
        for parsed in corpus.files:
            for ask in parsed.asks:
                if ask.filed < conf.cutoff:
                    continue
                if not ask.unit and ask.id in corpus.specs:
                    out.append(Verdict(9, f"{ask.path}:{ask.line}: {ask.id} is filed on or after "
                                          f"{conf.cutoff} without the `unit` marker, and a spec H1 "
                                          f"carries the same id at {corpus.specs[ask.id].path}",
                                       (ask.path, corpus.specs[ask.id].path)))
                if not sevrows.get(ask.id):
                    out.append(Verdict(12, f"{ask.path}:{ask.line}: {ask.id} is filed on or after "
                                           f"{conf.cutoff} with no SEV row in any of the "
                                           f"{len(corpus.files)} file(s) read", (ask.path,)))
    return sorted(out, key=lambda v: (v.code, v.text))


def _scan_clause_grammar(corpus: Corpus, asks: dict) -> list:
    """V13, over every clause-carrying row of both kinds. Five findings, each naming file and row.

    THE ROW KINDS SHARE ONE VALUE WALK. An ask row and a SCOPE row disagree about everything except
    what a clause MEANS, so grading them twice would be the second spelling this module's own
    grammar docstring forbids — and the copy is always the one that stops matching.

    `out`, `accept`, `verify` and `data` are FREE TEXT and the only way they fail is by being
    empty. That is not a formality: an empty value is exactly what a TEXT colliding with a label
    produces, so it is the finding that makes the collision loud instead of silent.

    A `SCOPE` ROW MAY NOT CARRY `may` AT ALL (TOOL-dDerivedDocket-19 S5, owner ruling D12-j). A grant
    is honoured only from an owner-committed build README; a SCOPE row's writer is a triager adding
    clauses to somebody else's ask, so the LABEL is the finding, whatever the value says - `none`
    included - and its grammar is not graded on top of it, because a clause that may not exist has
    no shape worth reporting. An ASK row's `may` stays a PROPOSAL an owner may copy by hand, graded
    below exactly as before.
    """
    out: list = []

    def add(path: str, lineno: int, why: str) -> None:
        out.append(Verdict(13, f"{path}:{lineno}: {why}", (path,)))

    carriers = [(a.path, a.line, f"ask {a.id}", a.clauses, False)
                for p in corpus.files for a in p.asks]
    carriers += [(r.path, r.line, f"{SCOPE_VERB} row for {r.target}", r.extra["clauses"], True)
                 for p in corpus.files for r in p.rows if r.cls == "scope"]
    for path, lineno, who, pairs, scoped in sorted(carriers):
        for label in CLAUSE_LABELS:
            if len(read_clause_values(pairs, label)) > 1:
                add(path, lineno, f"{who} writes the `{label}` clause more than once on one row, so "
                                  f"which value it carries has two answers; a second value belongs "
                                  f"on a {SCOPE_VERB} row, where the merge conjoins it")
        for label, value in pairs:
            if not value:
                add(path, lineno, f"{who} carries a `{label}` clause with no value — a label with "
                                  f"nothing after it is prose that collided with the tail, not a "
                                  f"clause")
                continue
            if label == "seen":
                seen = parse_seen(value)
                if seen.why:
                    add(path, lineno, f"{who} carries `seen {value}`, and {seen.why}")
            elif label == "may" and scoped:
                add(path, lineno, f"{who} carries a `may` clause, and a {SCOPE_VERB} row honours no "
                                  f"grant: authority comes only from a build README the owner "
                                  f"committed, and a {SCOPE_VERB} row is written about somebody "
                                  f"else's ask")
            elif label == "may":
                grants, why = extract_grants(value)
                if why:
                    add(path, lineno, f"{who} carries `may {value}`, and {why}")
                    continue
                for grant in grants:
                    if grant != GRANT_NONE and not check_grant(grant):
                        add(path, lineno, f"{who} carries the grant `{grant}` under `may`, which is "
                                          f"neither a backticked path nor an id")

    # A SCOPE ROW WHOSE TARGET NOBODY FILED, and two of them for one target in one file. Both are
    # per-file, and the second is per-file BY DESIGN: the merge conjoins across files, so two
    # writers may each scope one ask — what nobody may do is state one label twice inside one file
    # and leave a reader to guess which of their own two rows they meant.
    for parsed in corpus.files:
        first: dict = {}
        for row in parsed.rows:
            if row.cls != "scope":
                continue
            if row.target not in asks:
                add(row.path, row.line, f"{SCOPE_VERB} row targets {row.target}, which no ask row "
                                        f"in any of the {len(corpus.files)} file(s) read files")
            if row.target in first:
                add(row.path, row.line, f"a second {SCOPE_VERB} row for {row.target} in this file, "
                                        f"the first at line {first[row.target]}; one file scopes "
                                        f"one target once, and a writer adds a clause by editing "
                                        f"their own row")
            else:
                first[row.target] = row.line
    return out


def _scan_cycles(edges: dict, fold: Fold) -> list:
    """Every hold cycle among live asks, each reported ONCE, rotated to its smallest member.

    Reported once and canonically rotated because AC7 says a permutation of the corpus returns
    identical bytes, and a cycle discovered from three different entry points is one finding.
    """
    found: dict = {}
    live = [a for a in sorted(edges) if fold.statuses.get(a) not in TERMINAL]
    for start in live:
        stack = [(start, (start,))]
        while stack:
            node, path = stack.pop()
            for nxt in sorted(edges.get(node, ())):
                if fold.statuses.get(nxt) in TERMINAL:
                    continue
                if nxt == start:
                    low = path.index(min(path))
                    key = path[low:] + path[:low]
                    found.setdefault(key, key)
                elif nxt not in path:
                    stack.append((nxt, path + (nxt,)))
    return [found[k] for k in sorted(found)]


# ------------------------------------------------------------------- READY, and the decided-by set
#: Everything one grading run holds fixed. Built once per run and handed to `derive_ready` per ask,
#: because every field of it is a property of the RUN and re-deriving any of them per ask would let
#: two asks in one answer be graded against two different trees.
#:
#: `mandate` is the set M. `target` is the build folder R2 admits a live closing spec from.
#: `live_builds` is `None` for "every build is live", which is the CONSERVATIVE default and the
#: reading the ask driver pins: no tree it reads shows every run in flight, so a caller that cannot
#: observe one must not be able to claim a foreign claim is stale by saying nothing.
#: `check_path` is the caller's tree probe, `path -> bool`. A CALLABLE and not a path list, so this
#: module still reads no filesystem and a caller may probe a pinned tree, a working tree or a
#: fixture with the same grader.
Grader = collections.namedtuple(
    "Grader", "corpus fold evidence merged conf mandate target live_builds check_path")

READY_GRADES = ("yes", "legacy", "no")
READY_RULES = ("R1", "R2", "R3", "R4", "R5", "R6")
#: The statuses R2 admits with no question asked. A SPECCED or INPROGRESS ask is admitted only
#: through the closing-spec test below, and a TERMINAL one never is.
READY_LIVE_STATUSES = ("OPEN", "BLOCKED", "DEFERRED")
_POINTER_LINK_RE = re.compile(r"^\[[^\]]*\]\((?P<target>[^)]+)\)$")


def build_grader(corpus: Corpus, fold: Fold, conf: Conf, check_path, mandate=(), target: str = "",
                 live_builds=None) -> Grader:
    """One grading run's fixed inputs. `check_path` is REQUIRED and refusing it is the point.

    A grader with no tree probe would answer R4 the same way for every ask — and the answer it
    would give is `located`, because "no probe said no" and "the path is there" are the same
    boolean. That is the reassuring-zero shape, so this raises instead.
    """
    if not callable(check_path):
        raise Problem("a READY grader needs a tree probe: R4 asks whether a path is PRESENT, and a "
                      "grader with nothing to ask would answer `located` for every ask alive")
    return Grader(corpus, fold, derive_evidence(corpus), derive_clauses(corpus), conf,
                  frozenset(mandate), target, None if live_builds is None else frozenset(live_builds),
                  check_path)


def read_build_slug(path: str) -> str:
    """The build folder a record sits in: `<root>/builds/<slug>/…` -> `<slug>`, or ""."""
    parts = path.replace("\\", "/").split("/")
    return parts[parts.index("builds") + 1] if "builds" in parts[:-1] else ""


def read_pointer_target(pointer: str) -> tuple:
    """`(path, external)` for an ask's POINTER. `path` is "" when nothing path-shaped is in it.

    A pointer is authored prose in three shapes this corpus already writes — a bare path, a
    backticked one, and a markdown link — so it is NORMALISED here rather than grammar-checked.
    R4 is the only reader, and the question it asks is whether the tree holds the thing; a pointer
    that normalises to nothing simply fails that question, which is the honest answer for a pointer
    nobody can follow.
    """
    raw = pointer.strip()
    link = _POINTER_LINK_RE.match(raw)
    if link:
        raw = link.group("target").strip()
    raw = raw.strip("`").strip()
    ext = SEEN_EXTERNAL_RE.match(raw)
    if ext:
        return ext.group("path"), True
    return raw, False


def derive_ready(grader: Grader, ask_id: str) -> Ready:
    """One ask's grade, its failing rules, its live holds, its merged grant and its live closers.

    THE SIX RULES ARE GRADED IN FULL, always, and the grade is read off the failures afterwards.
    Short-circuiting at the first failure would make `missing` a list of one, and a reader who
    fixes that one only learns about the next on the following run — which is how a list of ten
    asks takes ten runs to clear.

    `legacy` IS NOT A THIRD KIND OF PASS. It says: this ask predates the envelope, it is well
    formed in every rule the envelope did not add, and exactly ONE of "somebody can find it" and
    "somebody can tell when it is done" is answered. Both missing is `no` — fix F6's rule, and the
    reason is that an ask nobody can locate AND nobody can grade is not an ask, it is a note.
    """
    rows = [a for p in grader.corpus.files for a in p.asks if a.id == ask_id]
    ask = rows[0] if rows else None
    clauses = grader.merged.get(ask_id, {})
    evidence = grader.evidence.get(ask_id, {})
    status = grader.fold.statuses.get(ask_id, UNRESOLVED)
    missing: list = []

    # R1 — FILED. Exactly one row, in the folder the id's own slug names.
    if len(rows) != 1 or rows[0].slug != (ask_id.split("-")[1] if ask_id.count("-") >= 2 else ""):
        missing.append("R1")

    # R2 — LIVE, and the closers field it produces on the way. A foreign live spec is a LIVE CLAIM
    # unless the caller can say that build is not running, which only a caller observing every run
    # in flight can say — hence `None` meaning "every build is live" rather than "none is".
    closers: list = []
    contested = False
    for spec_id in evidence.get("live_specs", ()):
        slug = read_build_slug(grader.corpus.specs[spec_id].path)
        if slug and slug == grader.target:
            closers.append(spec_id)
        elif grader.live_builds is not None and slug not in grader.live_builds:
            closers.append("stale:" + spec_id)
        else:
            closers.append(spec_id)
            contested = True
    live = status in READY_LIVE_STATUSES or (status in ("SPECCED", "INPROGRESS") and not contested)
    if not live and ask is not None and ask.unit and ask.slug == grader.target \
            and status not in TERMINAL:
        live = True
    if not live:
        missing.append("R2")

    # R3 — UNHELD. A hold on a target INSIDE the mandate is a hold this run will release itself.
    holds = tuple(h for h in evidence.get("holds", ())
                  if check_hold_live(grader.corpus, grader.fold, h) is not False)
    if any(h not in grader.mandate for h in holds):
        missing.append("R3")

    # R4 and R6 — LOCATED and BOUNDED, walked together because both read the same locator set.
    located, external = False, False
    for value in clauses.get("seen", ()):
        seen = parse_seen(value)
        if seen.kind == "external":
            located, external = True, True
        elif seen.kind and grader.check_path(seen.path):
            located = True
    if ask is not None and ask.pointer:
        path, is_external = read_pointer_target(ask.pointer)
        if is_external:
            located, external = True, True
        elif path and grader.check_path(path):
            located = True
    if not located:
        missing.append("R4")

    # R5 — ACCEPTABLE. `accept` says what done looks like; a `seen … run` says a machine can ask.
    if not (clauses.get("accept")
            or any(parse_seen(v).command for v in clauses.get("seen", ()))):
        missing.append("R5")

    if external and not clauses.get("data"):
        missing.append("R6")

    failed = set(missing)
    if not failed:
        grade = "yes"
    elif (not failed - {"R4", "R5"} and len(failed) == 1 and ask is not None
          and check_filed_before_cutoff(grader.conf, ask.filed)):
        grade = "legacy"
    else:
        grade = "no"
    return Ready(grade, tuple(sorted(failed, key=READY_RULES.index)), holds,
                 derive_grants(clauses.get("may", ())), tuple(closers))


def check_filed_before_cutoff(conf: Conf, filed: str) -> bool:
    """Was this ask filed BEFORE the declared cutoff? False whenever no usable cutoff is declared.

    False and not True, because `legacy` is a grandfathering rule and a tree that declares no
    cutoff has grandfathered nothing — it has merely said nothing, and reading silence as "every
    ask is old" would grandfather every ask filed after the envelope shipped.
    """
    return bool(conf.cutoff) and DATE_RE.match(conf.cutoff) is not None and filed < conf.cutoff


def derive_deciders(corpus: Corpus, fold: Fold, evidence: dict) -> dict:
    """Per ask: EVERY member of the set that decided its status, sorted. Never one member picked.

    The fold NAMES one member — the minimum of the set — because a table cell holds one value.
    That is a lossy projection of a mixed outcome, and this repo has a gotcha for exactly it: a
    one-value field recording a mixed outcome reads as a unanimous one. The machine projection
    publishes the whole set, and a selftest arm holds `min(this set) == fold.decided` so the two
    cannot drift into being two answers.

    The rule numbers are UNIT 6's fold rules, not READY's: R1 CLOSED, R2 WONTDO, R3 INPROGRESS,
    R4 SPECCED, R5 BLOCKED, R6 DEFERRED, R7 OPEN — and R7's set is empty by construction, because
    OPEN is what is left when nothing decided anything.
    """
    asks = _read_asks(corpus)
    drows = _read_rows(corpus, "status")
    out: dict = {}
    for ask_id in asks:
        status = fold.statuses.get(ask_id)
        ev = evidence.get(ask_id, {})
        live = [s for s in ev.get("live_specs", ()) if s in corpus.specs]
        if status == "CLOSED":
            members = list(ev.get("closing", ()))
        elif status == "WONTDO":
            members = list(ev.get("declining", ()))
        elif status in ("INPROGRESS", "SPECCED"):
            rule = ("INPROGRESS",) if status == "INPROGRESS" else ("OPEN", "SPECCED")
            members = [s for s in live if corpus.specs[s].status in rule]
        elif status in ("BLOCKED", "DEFERRED"):
            members = [s for s in live if corpus.specs[s].status == status]
            members += [r.value for r in drows.get(ask_id, []) if r.verb == status
                        and check_hold_live(corpus, fold, r.value) is True]
        elif status == UNRESOLVED:
            members = [fold.decided.get(ask_id, "")]
        else:
            members = []
        out[ask_id] = tuple(sorted({m for m in members if m}))
    return out


# ------------------------------------------------------------------------------------- the renderers
# ONE RENDERER PER SHAPE, BESIDE ITS PARSER. Every later writer — the triage sweep, the relocation
# engine, the inherited-red auto-file — spells a row the ONE way `extract_row` reads it, and AC2
# grades the pairing by parsing each renderer's own output back.
def render_ask_row(ask_id: str, filed: str, text: str, unit: bool = False, pointer: str = "",
                   clauses=()) -> str:
    marker = SEP + "unit" if unit else ""
    tail = ARROW + pointer if pointer else ""
    return f"- {ask_id}{SEP}filed {filed}{marker}{SEP}{text}{render_clauses(clauses)}{tail}"


def render_clauses(clauses) -> str:
    """The clause tail alone, for the two renderers that both end with one. `()` renders nothing."""
    return "".join(f"{SEP}{label} {value}" for label, value in clauses)


def render_scope_row(target: str, clauses) -> str:
    return f"- {SCOPE_VERB}{SEP}{target}{render_clauses(clauses)}"


def render_status_row(verb: str, target: str, why: str, value: str = "") -> str:
    slots = {"CLOSED": "by", "BLOCKED": "on", "DEFERRED": "until", "REOPEN": "of"}
    slot = SEP + f"{slots[verb]} {value}" if verb in slots else ""
    return f"- {verb}{SEP}{target}{slot}{SEP}{why}"


def render_sev_row(target: str, level: str, why: str) -> str:
    return f"- {SEV_VERB}{SEP}{target}{SEP}{level}{SEP}{why}"


def render_relocated_row(target: str, sha: str, disposal: str, why: str) -> str:
    return f"- {PROVENANCE_VERB}{SEP}{target}{SEP}by {sha}{SEP}{disposal}: {why}"


# ------------------------------------------------------------------------------------- the view
# THE RECIPE, ONE CONSTANT AND THREE RENDERINGS. The view header quotes it, this unit's data-loss
# guard prints it, the relocation engine's `--recipe` prints it, and the row driver's refusal banner
# prints it. A reader who meets any of the four meets the same bytes, which is the whole point:
# design layer L4 is an instruction an operator reads inside a merge conflict, and an instruction
# that differs between the places it appears is one nobody trusts.
#
# THE KIT PREFIX IS A PARAMETER, never a literal. This file is COPY-INSTALLED into adopting repos at
# whatever path they choose, so a spelled `tools/<kit>/` here lands a dead command in their tree and
# the byte-compare that guards these artifacts happily agrees with it. The caller derives its own
# install location and hands it in; an empty derivation REFUSES below rather than rendering
# `python /migrate_backlog.py`.
RELOCATION_RECIPE = (
    "This branch predates the per-build backlog. Its edits to {m}/backlog/<F>.md must be "
    "relocated, not merged.",
    "  git merge <default>       # MERGE, never rebase or squash: those leave no merge to audit",
    "  python {kit}/migrate_backlog.py --relocate --as <your-slug>",
    "  git add {m}/ && git commit",
    "Already landed without this? Any node:  python {kit}/migrate_backlog.py --repair <merge-sha>",
    "A branch nobody will revisit? From the default branch:  "
    "python {kit}/migrate_backlog.py --ingest <ref>",
)

VIEW_H1 = "# {m}/backlog/{family}.md — live asks, family {family}"
VIEW_PROSE = (
    "Derived, never authored. Each ask is filed once in builds/<slug>/BACKLOG.md; its status is",
    "computed from that file, the specs that close or advance it, and disposition rows. An id NOT",
    "listed here is terminal: `python {kit}/gen_build_index.py --asks <id>` prints what decided it.",
    "Cite ids, never line numbers.",
)
VIEW_BANNER = ("> If your branch edits this file as an authored shard, it predates the per-build "
               "backlog.")
VIEW_COLUMNS = ("Ask", "Status", "Sev", "Decided by", "Filed", "Summary")
VIEW_EMPTY = "*No live ask.*"
VIEW_NONE = "—"

# THE HEADER SHAPE, WITH ANY KIT PREFIX. The generator's own `GEN_HEADER` is bound to THIS install's
# location and cannot answer "is this text a view", because the text in front of the reader may have
# been rendered in an adopter's tree at a different prefix. So the predicate matches the SHAPE. The
# two spellings are held together by a parity arm in the generator's selftest, which is the only
# thing that stops this regex rotting when that constant moves.
VIEW_HEADER_RE = re.compile(
    r"^<!-- generated by \S+/gen_build_index\.py --write — do not hand-edit -->$")
VIEW_H1_RE = re.compile(
    r"^# \S+/backlog/([A-Za-z][A-Za-z0-9]*)\.md — live asks, family \1$")
# A rendered DATA row, recognised by its LINK-WRAPPED first cell. That wrapper is what keeps the
# table-anchor shape off the row, so the row that the anchor grammar refuses to claim is exactly the
# row this pattern accepts — one property, asserted from both sides.
VIEW_ROW_RE = re.compile(
    r"^\| \[[A-Za-z][A-Za-z0-9]*-[A-Za-z0-9]+-\d+\]\(\.\./builds/[A-Za-z0-9]+/BACKLOG\.md\) \|.*\|$")
_LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")


def render_relocation_recipe(kit: str, memory_root: str = "memory") -> list:
    """The recipe's lines, with the caller's install prefix and memory root filled in.

    REFUSES an empty prefix. A recipe is a command an operator will paste, and `python
    /migrate_backlog.py` is worse than no instruction at all: it looks like one.
    """
    if not kit or not memory_root:
        raise Problem("the relocation recipe needs a kit prefix and a memory root, both DERIVED by "
                      "the caller from its own install location; an empty derivation would render "
                      "a command that cannot run and reads as though it can")
    return [line.format(kit=kit, m=memory_root) for line in RELOCATION_RECIPE]


def check_family_view(text: str) -> bool:
    """Is this text a rendered family view? Shape, not bytes, and only the first two lines.

    Two lines and no more, because the row driver calls this on `%A` and `%B` mid-merge, where the
    rest of the file may legitimately be a conflict. The header alone is not enough — every artifact
    this generator writes carries it — so the family H1 is the second half of the test.
    """
    lines = text.split("\n")
    if len(lines) < 2:
        return False
    if not VIEW_HEADER_RE.match(lines[0].rstrip("\r")):
        return False
    return bool(VIEW_H1_RE.match(lines[1].rstrip("\r")))


def render_summary_cell(text: str, cap: int = EXCERPT_DEFAULT) -> str:
    """One ask's TEXT as the view's last cell.

    Four reductions, in this order, each for a stated reason. The pointer tail goes because the
    view cites ids and never paths. A link is reduced to its text and a backtick is dropped so the
    cell carries no path token the hygiene engine's path check could grade — a generated cell that
    reds a path check is a file nobody can land. A `|` becomes `/` because it would otherwise split
    the row into cells that are not there. And the cut is at a space, so the excerpt ends on a word.
    """
    body = text.split(ARROW)[0]
    body = _LINK_RE.sub(r"\1", body).replace("`", "").replace("|", "/").strip()
    if len(body) <= cap:
        return body
    cut = body[:cap]
    space = cut.rfind(" ")
    if space > 0:
        cut = cut[:space]
    return cut.rstrip() + "…"


def build_ask_sort_key(ask: Ask):
    """Slug, then the sequence as a NUMBER, so `-10` sorts after `-2` and a merge stays stable.

    PUBLIC because the view and the print modes must agree on it: a table whose order differs from the
    view it explains is two answers to the question "where is this ask in the list".
    """
    parts = ask.id.split("-")
    slug = parts[1] if len(parts) > 2 else ""
    seq = int(parts[2]) if len(parts) > 2 and parts[2].isdigit() else 0
    return (slug, seq, ask.id)


def render_family_view(family: str, asks, fold: Fold, memory_root: str, kit: str,
                       gen_header: str, excerpt: int = EXCERPT_DEFAULT) -> str:
    """One family's view: every LIVE ask of that family, filed once, cited by id.

    `gen_header` is the generator's own first line, passed IN rather than rebuilt here: it names the
    install prefix and there must be exactly one place that decides what it says.

    NO COUNT, NO TOTAL AND NO PER-STATUS SECTION anywhere in the output (owner ruling D3). Every one
    of those is a value two branches touching one family would both change, so every merge of them
    would conflict on a number neither side authored — and the whole point of a generated view is
    that a merge of it is re-rendered rather than reconciled.
    """
    rows = [a for a in asks
            if a.id.split("-")[0] == family and fold.statuses.get(a.id) not in TERMINAL]
    rows.sort(key=build_ask_sort_key)
    out = [gen_header, VIEW_H1.format(m=memory_root, family=family), ""]
    out += [line.format(kit=kit) for line in VIEW_PROSE]
    out += ["", VIEW_BANNER]
    out += ["> " + line for line in render_relocation_recipe(kit, memory_root)]
    out.append("")
    if rows:
        out.append("| " + " | ".join(VIEW_COLUMNS) + " |")
        out.append("|" + "---|" * len(VIEW_COLUMNS))
        for ask in rows:
            sev = fold.severities.get(ask.id, UNLABELLED)
            out.append(
                f"| [{ask.id}](../builds/{ask.slug}/BACKLOG.md) "
                f"| {fold.statuses.get(ask.id, UNRESOLVED)} "
                f"| {VIEW_NONE if sev == UNLABELLED else sev} "
                f"| {fold.decided.get(ask.id) or VIEW_NONE} "
                f"| {ask.filed} "
                f"| {render_summary_cell(ask.text, excerpt)} |")
    else:
        out.append(VIEW_EMPTY)
    return "\n".join(out) + "\n"


def read_view_grammar_lines(family: str, memory_root: str, kit: str, gen_header: str) -> set:
    """Every FIXED line the view grammar can emit, derived by rendering an empty view.

    Derived rather than listed, so a header line added to the renderer cannot be missing here. The
    two table lines are added because an empty view carries neither.
    """
    empty = render_family_view(family, (), Fold({}, {}, {}, {}), memory_root, kit, gen_header)
    return set(empty.split("\n")) | {
        "| " + " | ".join(VIEW_COLUMNS) + " |",
        "|" + "---|" * len(VIEW_COLUMNS),
    }


def check_view_line(line: str, grammar_lines: set) -> bool:
    """Could the view grammar have emitted this line? Blank, a data row, or one of the fixed lines.

    WHAT THIS DOES NOT DECIDE: whether the line is CURRENT. A data row for an ask nobody files any
    more is still a line the grammar emits, and re-rendering over it is the right answer. The
    question here is only "is this authored content", which is what the data-loss guard asks.
    """
    stripped = line.rstrip("\r")
    if not stripped.strip():
        return True
    if VIEW_ROW_RE.match(stripped):
        return True
    return stripped in grammar_lines


def read_excerpt_chars(conf: dict) -> int:
    """`BACKLOG_EXCERPT_CHARS`, or its default. An unusable value REFUSES and says which.

    A silent fallback here re-cuts every summary in the tree on the next render and reports nothing,
    so a typo would land as a corpus-wide diff nobody asked for and nobody can explain.
    """
    raw = (conf.get(EXCERPT_KEY) or "").strip()
    if not raw:
        return EXCERPT_DEFAULT
    if not raw.isdigit() or int(raw) <= 0:
        raise Problem(f"{EXCERPT_KEY}='{raw}' is not a positive whole number of characters; the "
                      f"view's summary column is cut to it, so an unusable value would silently "
                      f"re-cut every row rather than name itself")
    return int(raw)


# ---------------------------------------------------------------------------------------- selftest
# TEST-ONLY. The real anchor grammar lives in the memory-recall kit and is never vendored here; AC2
# asserts the ANCHOR PROPERTY against that file rather than against a local copy, because an arm
# that grades a copy passes happily when the real grammar moves underneath it. Resolution is the
# same two-layout walk `merge-rows.py` already performs, and it is deliberately NOT at module scope:
# a module that cannot be imported without a sibling kit is a module an adopter cannot install.
def _resolve_anchor_at():
    here = pathlib.Path(__file__).resolve()
    root = next((p for p in here.parents if (p / ".memory-tree.conf").is_file()), None)
    if root is None:
        return None, None, "no .memory-tree.conf above this file"
    kit = next((c for c in (root / "tools" / "memory-recall", root / "memory-recall")
                if c.is_dir()), None)
    if kit is None:
        return None, None, "the memory-recall kit is not installed in this tree"
    sys.path.append(str(kit))
    try:
        import extract as anchor_kit  # noqa: PLC0415 — deliberately deferred; see above
    except Exception as exc:  # noqa: BLE001 — an import failure here is a SKIP, never a red arm
        return None, None, f"the memory-recall kit is present but not importable here ({exc})"
    return anchor_kit.anchor_at, anchor_kit.grammar_for(str(root)), ""


_G = build_grammar(("EXMP", "OTHR"))

#: TOOL-dDerivedDocket-15 — what a POST-CUTOFF fixture ask now owes. V14 grades every ask filed on
#: or after the declared cutoff, so a fixture written to stage ONE verdict must carry an acceptance
#: or it stages two and no arm below can tell which one it was reading. Added to the fixtures whose
#: arms assert an exact verdict-code set, and to no other: the arms that read the fold alone are
#: the control saying the tail changes no status.
_CLAUSE_OK = (("accept", "the fixture ask says what done looks like"),)


def _build_spec(spec_id, status, closes=(), advances=()):
    return Spec(spec_id, f"spec/{spec_id}.md", status, tuple(closes), tuple(advances))


def _build_file(slug, asks=(), rows=()):
    """A fixture file's TEXT, always through the renderers, so no fixture spells a row by hand."""
    body = [f"# {slug} — asks", "", H_ASKS] + list(asks) + ["", H_DISPOSITIONS] + list(rows)
    return f"memory/builds/{slug}/BACKLOG.md", "\n".join(body) + "\n"


def _parse_fixture(slug, asks=(), rows=()):
    path, text = _build_file(slug, asks, rows)
    return parse_file(path, text, _G)


def _read_fold(files, specs=(), builds=None):
    corpus = build_corpus(files, {s.id: s for s in specs}, builds)
    return derive_statuses(corpus), corpus


_CLEAN_CONF = Conf("builds", "2026-01-01", ())


def _read_codes(files, specs=(), builds=None, conf=_CLEAN_CONF):
    corpus = build_corpus(files, {s.id: s for s in specs}, builds)
    return sorted({v.code for v in derive_verdicts(corpus, conf)})


def run_arms(report: bool = True) -> list:
    """Every arm. Returns the labels that failed; the generator's own selftest folds these in."""
    fails: list = []

    def arm(label, want, fn):
        try:
            got = fn()
        except Problem as exc:
            got = str(exc)
        except Exception as exc:  # noqa: BLE001 — a traceback here IS the finding
            got = f"UNEXPECTED {type(exc).__name__}: {exc}"
        if want in str(got):
            if report:
                print(f"arm ok    backlog: {label}")
        else:
            fails.append(label)
            print(f"arm FAIL  backlog: {label} — expected to see: {want}\n      got: {got}")

    # ---- AC1: the file grammar, and V2 on everything it does not understand.
    every = _parse_fixture(
        "aFoo",
        asks=[render_ask_row(f"EXMP-aFoo-{n}", "2026-02-01", "a plain ask") for n in range(1, 7)]
        + [render_ask_row("EXMP-aFoo-7", "2026-02-01", "the unit one", unit=True,
                          pointer="docs/x.md")],
        rows=[render_status_row("CLOSED", "EXMP-aFoo-1", "shipped", "EXMP-aFoo-9"),
              render_status_row("WONTDO", "EXMP-aFoo-2", "not worth it"),
              render_status_row("BLOCKED", "EXMP-aFoo-3", "waiting", "EXMP-aFoo-4"),
              render_status_row("DEFERRED", "EXMP-aFoo-4", "later", "EXMP-aFoo-5"),
              render_status_row("KEEP", "EXMP-aFoo-5", "still true"),
              render_status_row("REOPEN", "EXMP-aFoo-6", "came back", "EXMP-aFoo-9"),
              render_sev_row("EXMP-aFoo-1", "HIGH", "it bites"),
              render_relocated_row("EXMP-aFoo-2", "abc1234", "kept", "moved here")])
    arm("one of every row shape parses with no verdict", "7 asks 8 rows []",
        lambda: f"{len(every.asks)} asks {len(every.rows)} rows "
                f"{[v.code for v in every.verdicts]}")
    arm("a continuation line is V2 naming the line", "BACKLOG.md:5: a continuation line",
        lambda: str(parse_file("memory/builds/aFoo/BACKLOG.md",
                               "# t\n\n" + H_ASKS + "\n"
                               + render_ask_row("EXMP-aFoo-1", "2026-02-01", "x") + "\n  and more\n",
                               _G).verdicts[0].text))
    arm("a row above `## Asks` is V2", "a row above both section headings",
        lambda: str(parse_file("memory/builds/aFoo/BACKLOG.md",
                               "# t\n" + render_ask_row("EXMP-aFoo-1", "2026-02-01", "x") + "\n",
                               _G).verdicts[0].text))
    arm("an ask row under `## Dispositions` is V2", "an ask row under `## Dispositions`",
        lambda: str(_parse_fixture("aFoo", rows=[render_ask_row("EXMP-aFoo-1", "2026-02-01",
                                                                "x")]).verdicts[0].text))
    arm("prose inside a section is V2, not skipped", "matches no declared row shape",
        lambda: str(_parse_fixture("aFoo", asks=["a sentence somebody left behind"]).verdicts[0].text))
    arm("a file holding only its H1 is V2, not a clean zero", "parses to nothing",
        lambda: str(parse_file("memory/builds/aFoo/BACKLOG.md", "# only a title\n",
                               _G).verdicts[0].text))
    # THE CONTROL for the four arms above: the same walk over a clean file reports nothing. Without
    # it, a parser that emitted V2 for every line would pass all four.
    arm("the clean fixture reports no verdict at all", "[]",
        lambda: str([v.code for v in every.verdicts]))
    arm("a derived token used as a verb is V5, and WITHDRAWN's remedy names WONTDO",
        "write the disposition as a `WONTDO` row",
        lambda: str(_parse_fixture("aFoo", rows=["- WITHDRAWN" + SEP + "EXMP-aFoo-1" + SEP
                                                 + "gone"]).verdicts[0].text))
    arm("SPECCED used as a verb is V5 too", "5",
        lambda: str(_parse_fixture("aFoo", rows=["- SPECCED" + SEP + "EXMP-aFoo-1" + SEP
                                                 + "x"]).verdicts[0].code))
    arm("an unpadded filed date is refused", "not a zero-padded",
        lambda: str(_parse_fixture("aFoo",
                                   asks=["- EXMP-aFoo-1" + SEP + "filed 2026-2-1" + SEP
                                         + "x"]).verdicts[0].text))
    arm("V4 names both lines of a doubled status row", "two status rows for EXMP-aFoo-1",
        lambda: str([v.text for v in _parse_fixture(
            "aFoo",
            asks=[render_ask_row("EXMP-aFoo-1", "2026-02-01", "x")],
            rows=[render_status_row("KEEP", "EXMP-aFoo-1", "one"),
                  render_status_row("WONTDO", "EXMP-aFoo-1", "two")]).verdicts
            if v.code == 4][0]))
    # THE TWO CLASSES THE BUG-CLASS CHECKLIST NAMED for this diff, armed rather than argued.
    arm("a family carrying a regex metacharacter REFUSES instead of re-scoping the grammar",
        "are not [A-Za-z][A-Za-z0-9]*", lambda: build_grammar(("EXMP|.*", "OTHR")))
    arm("a CRLF copy of a file parses identically to its LF copy", "True",
        lambda: (lambda lf: str(
            parse_file("memory/builds/aFoo/BACKLOG.md", lf.replace("\n", "\r\n"), _G)
            == parse_file("memory/builds/aFoo/BACKLOG.md", lf, _G)))(
            _build_file("aFoo", [render_ask_row("EXMP-aFoo-1", "2026-02-01", "x")])[1]))
    arm("a BARE CR inside a field is REPORTED, never silently re-read", "2",
        lambda: str(_parse_fixture("aFoo", asks=[render_ask_row(
            "EXMP-aFoo-1", "2026-02-01\rmore", "x")]).verdicts[0].code))
    arm("a status row and a SEV row for one ask are NOT V4", "[]",
        lambda: str([v.code for v in _parse_fixture(
            "aFoo",
            asks=[render_ask_row("EXMP-aFoo-1", "2026-02-01", "x")],
            rows=[render_status_row("KEEP", "EXMP-aFoo-1", "one"),
                  render_sev_row("EXMP-aFoo-1", "LOW", "two")]).verdicts]))
    # PROVENANCE IS EXCLUDED FROM V4 ENTIRELY (fork F3): one relocation per sha, so an id moved
    # twice carries two rows. Without this arm, folding provenance back into the per-class rule
    # reds nothing — measured, by staging exactly that.
    arm("two RELOCATED rows for one target in one file are NOT V4", "[]",
        lambda: str([v.code for v in _parse_fixture(
            "aFoo",
            asks=[render_ask_row("EXMP-aFoo-1", "2026-02-01", "x")],
            rows=[render_relocated_row("EXMP-aFoo-1", "abc1234", "kept", "one"),
                  render_relocated_row("EXMP-aFoo-1", "def5678", "amended", "two")]).verdicts]))

    # ---- AC2: the REAL anchor grammar, and the renderer/parser round trip.
    anchor_at, grammar, why = _resolve_anchor_at()
    if anchor_at is None:
        print(f"arm SKIP  backlog: the real `extract.anchor_at` anchor arm did not run — {why}. "
              f"The memory-recall kit owns the one anchor grammar and it is never vendored here, "
              f"so with the kit absent this property is UNEXERCISED rather than passing.")
    else:
        arm("the REAL anchor grammar anchors an ask row on its id", "TOOL-dAnchorProbe-1",
            lambda: str(anchor_at(render_ask_row("TOOL-dAnchorProbe-1", "2026-02-01", "x"),
                                  grammar)))
        arm("and anchors NOTHING on a status, SEV, REOPEN or RELOCATED row", "[None, None, None, None]",
            lambda: str([anchor_at(r, grammar) for r in (
                render_status_row("CLOSED", "TOOL-dAnchorProbe-1", "why", "abc1234"),
                render_sev_row("TOOL-dAnchorProbe-1", "MED", "why"),
                render_status_row("REOPEN", "TOOL-dAnchorProbe-1", "why", "abc1234"),
                render_relocated_row("TOOL-dAnchorProbe-1", "abc1234", "kept", "why"))]))
    arm("every renderer's output parses back to the row it rendered",
        "['ask', 'status', 'status', 'status', 'status', 'status', 'status', 'severity', "
        "'provenance']",
        lambda: str([extract_row(r, _G).cls for r in (
            render_ask_row("EXMP-aFoo-1", "2026-02-01", "t", unit=True, pointer="p/q.py"),
            render_status_row("CLOSED", "EXMP-aFoo-1", "w", "abc1234"),
            render_status_row("WONTDO", "EXMP-aFoo-1", "w"),
            render_status_row("BLOCKED", "EXMP-aFoo-1", "w", "EXMP-aFoo-2"),
            render_status_row("DEFERRED", "EXMP-aFoo-1", "w", "EXMP-aFoo-2"),
            render_status_row("KEEP", "EXMP-aFoo-1", "w"),
            render_status_row("REOPEN", "EXMP-aFoo-1", "w", "aFoo"),
            render_sev_row("EXMP-aFoo-1", "LOW", "w"),
            render_relocated_row("EXMP-aFoo-1", "abc1234", "amended", "w"))]))
    arm("the ask round trip keeps the unit marker and the pointer", "True True p/q.py",
        lambda: (lambda r: f"{r.extra['unit']} {r.why == 't'} {r.extra['pointer']}")(
            extract_row(render_ask_row("EXMP-aFoo-1", "2026-02-01", "t", unit=True,
                                       pointer="p/q.py"), _G)))

    # ---- AC4: one fixture per rule, plus hold release, UNRESOLVED and a cycle.
    def read_rule(asks, rows, specs=(), want="EXMP-aFoo-1"):
        fold, _c = _read_fold([_parse_fixture("aFoo", asks=asks, rows=rows)], specs)
        return f"{fold.statuses[want]} by {fold.decided[want]!r}"

    one = [render_ask_row("EXMP-aFoo-1", "2026-02-01", "x", clauses=_CLAUSE_OK)]
    arm("R1 CLOSED names its closing spec", "CLOSED by 'EXMP-aFoo-7'",
        lambda: read_rule(one, [], [_build_spec("EXMP-aFoo-7", "CLOSED", closes=["EXMP-aFoo-1"])]))
    arm("R2 WONTDO names the declining file's slug", "WONTDO by 'aFoo'",
        lambda: read_rule(one, [render_status_row("WONTDO", "EXMP-aFoo-1", "no")]))
    arm("R3 INPROGRESS", "INPROGRESS by 'EXMP-aFoo-7'",
        lambda: read_rule(one, [], [_build_spec("EXMP-aFoo-7", "INPROGRESS",
                                                advances=["EXMP-aFoo-1"])]))
    arm("R4 SPECCED", "SPECCED by 'EXMP-aFoo-7'",
        lambda: read_rule(one, [], [_build_spec("EXMP-aFoo-7", "SPECCED", closes=["EXMP-aFoo-1"])]))
    arm("R5 BLOCKED names the `on` target", "BLOCKED by 'EXMP-aFoo-2'",
        lambda: read_rule(one + [render_ask_row("EXMP-aFoo-2", "2026-02-01", "y")],
                          [render_status_row("BLOCKED", "EXMP-aFoo-1", "w", "EXMP-aFoo-2")]))
    arm("R6 DEFERRED names the `until` target", "DEFERRED by 'EXMP-aFoo-2'",
        lambda: read_rule(one + [render_ask_row("EXMP-aFoo-2", "2026-02-01", "y")],
                          [render_status_row("DEFERRED", "EXMP-aFoo-1", "w", "EXMP-aFoo-2")]))
    arm("R7 OPEN decides nothing and says so", "OPEN by ''", lambda: read_rule(one, []))
    arm("a KEEP row never changes a status", "OPEN by ''",
        lambda: read_rule(one, [render_status_row("KEEP", "EXMP-aFoo-1", "still true")]))
    # TERMINAL EVIDENCE BEATS LIVE EVIDENCE. Evaluated live-first, a stale SPECCED spec would hide a
    # recorded closure — which is the whole reason stratum 1 reads no hold and runs first.
    arm("a CLOSED row beats a live closing spec", "CLOSED by 'abc1234'",
        lambda: read_rule(one, [render_status_row("CLOSED", "EXMP-aFoo-1", "shipped", "abc1234")],
                          [_build_spec("EXMP-aFoo-7", "SPECCED", closes=["EXMP-aFoo-1"])]))
    arm("CLOSED beats WONTDO", "CLOSED by 'abc1234'",
        lambda: read_rule(one, [render_status_row("CLOSED", "EXMP-aFoo-1", "shipped", "abc1234"),
                                render_status_row("WONTDO", "EXMP-aFoo-1", "no")]))
    # THE HOLD RELEASES ITSELF. Drop `has a live target` from R5 or R6 and a released hold stays
    # BLOCKED or DEFERRED forever, against ruling D5's release-id meaning.
    arm("a BLOCKED hold on a CLOSED target releases to OPEN", "OPEN by ''",
        lambda: read_rule(one + [render_ask_row("EXMP-aFoo-2", "2026-02-01", "y")],
                          [render_status_row("BLOCKED", "EXMP-aFoo-1", "w", "EXMP-aFoo-2"),
                           render_status_row("CLOSED", "EXMP-aFoo-2", "done", "abc1234")]))
    arm("a DEFERRED hold whose `until` target folds CLOSED releases to OPEN", "OPEN by ''",
        lambda: read_rule(one + [render_ask_row("EXMP-aFoo-2", "2026-02-01", "y")],
                          [render_status_row("DEFERRED", "EXMP-aFoo-1", "w", "EXMP-aFoo-2"),
                           render_status_row("CLOSED", "EXMP-aFoo-2", "done", "abc1234")]))
    arm("a hold on a target that is neither an ask nor a spec renders UNRESOLVED",
        f"{UNRESOLVED} by 'EXMP-aFoo-9'",
        lambda: read_rule(one, [render_status_row("BLOCKED", "EXMP-aFoo-1", "w", "EXMP-aFoo-9")]))
    arm("and that ask's V6 names the unresolvable target", "[6]",
        lambda: str(_read_codes([_parse_fixture(
            "aFoo", asks=one,
            rows=[render_sev_row("EXMP-aFoo-1", "LOW", "w"),
                  render_status_row("BLOCKED", "EXMP-aFoo-1", "w", "EXMP-aFoo-9")])])))
    cycle_files = [_parse_fixture(
        "aFoo",
        asks=one + [render_ask_row("EXMP-aFoo-2", "2026-02-01", "y")],
        rows=[render_status_row("BLOCKED", "EXMP-aFoo-1", "w", "EXMP-aFoo-2"),
              render_status_row("BLOCKED", "EXMP-aFoo-2", "w", "EXMP-aFoo-1")])]
    arm("two asks blocked on each other both derive their TRUE token", "BLOCKED BLOCKED",
        lambda: (lambda f: f"{f[0].statuses['EXMP-aFoo-1']} {f[0].statuses['EXMP-aFoo-2']}")(
            _read_fold(cycle_files)))
    arm("and V6 names the cycle", "a hold cycle among live asks: EXMP-aFoo-1 -> EXMP-aFoo-2",
        lambda: str([v.text for v in derive_verdicts(build_corpus(cycle_files), _CLEAN_CONF)
                     if v.code == 6][0]))
    arm("a self-hold is V6", "on itself",
        lambda: str([v.text for v in derive_verdicts(build_corpus([_parse_fixture(
            "aFoo", asks=one,
            rows=[render_status_row("BLOCKED", "EXMP-aFoo-1", "w", "EXMP-aFoo-1")])]),
            _CLEAN_CONF) if v.code == 6][0]))

    # ---- AC5: a WONTDO closing spec declines only the ask it IS.
    arm("a non-`unit` ask whose only closing spec reads WONTDO stays OPEN", "OPEN by ''",
        lambda: read_rule(one, [], [_build_spec("EXMP-aFoo-7", "WONTDO", closes=["EXMP-aFoo-1"])]))
    arm("a `unit` ask whose same-id spec reads WONTDO derives WONTDO", "WONTDO by 'EXMP-aFoo-1'",
        lambda: read_rule([render_ask_row("EXMP-aFoo-1", "2026-02-01", "x", unit=True)], [],
                          [_build_spec("EXMP-aFoo-1", "WONTDO")]))
    arm("a `unit` ask whose same-id spec reads CLOSED derives CLOSED", "CLOSED by 'EXMP-aFoo-1'",
        lambda: read_rule([render_ask_row("EXMP-aFoo-1", "2026-02-01", "x", unit=True)], [],
                          [_build_spec("EXMP-aFoo-1", "CLOSED")]))

    # ---- AC6: REOPEN cancels exactly the record it names.
    spec7 = [_build_spec("EXMP-aFoo-7", "CLOSED", closes=["EXMP-aFoo-1"])]
    arm("a REOPEN naming the closing spec leaves the ask live", "OPEN by ''",
        lambda: read_rule(one, [render_status_row("REOPEN", "EXMP-aFoo-1", "back",
                                                  "EXMP-aFoo-7")], spec7))
    arm("a second CLOSED row citing the SAME evidence stays cancelled", "OPEN by ''",
        lambda: read_rule(one, [render_status_row("REOPEN", "EXMP-aFoo-1", "back", "abc1234"),
                                render_status_row("CLOSED", "EXMP-aFoo-1", "again", "abc1234")]))
    arm("a CLOSED row by a NEW sha re-closes it", "CLOSED by 'def5678'",
        lambda: read_rule(one, [render_status_row("REOPEN", "EXMP-aFoo-1", "back", "abc1234"),
                                render_status_row("CLOSED", "EXMP-aFoo-1", "again", "def5678")]))
    arm("a REOPEN naming a folder slug cancels that folder's WONTDO", "OPEN by ''",
        lambda: (lambda f: f"{f[0].statuses['EXMP-aFoo-1']} by {f[0].decided['EXMP-aFoo-1']!r}")(
            _read_fold([_parse_fixture("aFoo", asks=one,
                                       rows=[render_status_row("WONTDO", "EXMP-aFoo-1", "no")]),
                        _parse_fixture("aBar",
                                       rows=[render_status_row("REOPEN", "EXMP-aFoo-1", "back",
                                                               "aFoo")])])))
    arm("a REOPEN of a record that closes nothing is V11", "which closes or declines nothing",
        lambda: str([v.text for v in derive_verdicts(build_corpus([_parse_fixture(
            "aFoo", asks=one,
            rows=[render_status_row("REOPEN", "EXMP-aFoo-1", "back", "abc1234")])]),
            _CLEAN_CONF) if v.code == 11][0]))

    # ---- AC7: order-freedom, measured over every permutation rather than asserted.
    perm_asks = [render_ask_row("EXMP-aFoo-1", "2026-02-01", "x"),
                 render_ask_row("EXMP-aFoo-2", "2026-02-01", "y"),
                 render_ask_row("EXMP-aFoo-3", "2026-02-01", "z")]
    perm_rows = [render_status_row("BLOCKED", "EXMP-aFoo-1", "w", "EXMP-aFoo-2"),
                 render_status_row("CLOSED", "EXMP-aFoo-3", "done", "abc1234"),
                 render_sev_row("EXMP-aFoo-1", "LOW", "w")]
    # EXMP-aFoo-3 CARRIES TWO CLOSING RECORDS, one per file, and that is the whole point of this
    # corpus. With one closer the Decided-by value is the same whatever order it was found in, so a
    # fold naming `closers[-1]` instead of the sorted minimum permutes identically — measured, by
    # staging exactly that: the permutation arm stayed green over a population of one.
    other_rows = [render_status_row("WONTDO", "EXMP-aFoo-2", "no"),
                  render_status_row("CLOSED", "EXMP-aFoo-3", "also done", "0000111"),
                  render_sev_row("EXMP-aFoo-1", "HIGH", "worse")]
    perm_specs = [_build_spec("EXMP-aFoo-7", "SPECCED", advances=["EXMP-aFoo-1"])]

    def measure_permutations():
        seen_out = set()
        for ao in itertools.permutations(perm_asks):
            for ro in itertools.permutations(perm_rows):
                for oo in itertools.permutations(other_rows):
                    for files in itertools.permutations(
                            [_parse_fixture("aFoo", asks=list(ao), rows=list(ro)),
                             _parse_fixture("aBar", rows=list(oo))]):
                        fold, _c = _read_fold(list(files), perm_specs)
                        seen_out.add(repr(sorted(fold.statuses.items()))
                                     + repr(sorted(fold.decided.items()))
                                     + repr(sorted(fold.severities.items())))
        return f"{len(seen_out)} distinct fold(s)"

    arm("every permutation of file and row order folds identically", "1 distinct fold(s)",
        measure_permutations)
    arm("and the evidence it NAMES is the sorted minimum, not the first record found", "0000111",
        lambda: _read_fold([_parse_fixture("aFoo", asks=perm_asks, rows=perm_rows),
                            _parse_fixture("aBar", rows=other_rows)],
                           perm_specs)[0].decided["EXMP-aFoo-3"])

    # ---- AC8: severity is the most severe row anywhere, never the last one read.
    # HIGH IS READ FIRST ON PURPOSE. Ordered the other way the fixture passes under a last-row-wins
    # severity too, by coincidence of the file order — measured, with `levels[-1]` staged in: the
    # arm stayed green and only the permutation arm caught it. The severest row is now the one a
    # last-wins rule would DISCARD, so this arm can fail on its own.
    sev_files = [_parse_fixture("aFoo", asks=one, rows=[render_sev_row("EXMP-aFoo-1", "HIGH", "w")]),
                 _parse_fixture("aBar", rows=[render_sev_row("EXMP-aFoo-1", "LOW", "w")])]
    arm("HIGH in one file and LOW in another reads HIGH", "HIGH",
        lambda: _read_fold(sev_files)[0].severities["EXMP-aFoo-1"])
    arm("an ask with no SEV row reads unlabelled", UNLABELLED,
        lambda: _read_fold([_parse_fixture("aFoo", asks=one)])[0].severities["EXMP-aFoo-1"])

    # ---- AC9: the legacy row reader.
    def read_legacy(line):
        got = read_legacy_row(line, build_grammar(("TOOL",)))
        return f"{got.id} {got.status} {got.withdrawn} | {got.why}"

    arm("an id-first legacy row", "TOOL-aOld-1 OPEN False |",
        lambda: read_legacy("- TOOL-aOld-1" + SEP + "OPEN" + SEP + "some prose"))
    arm("a status-first legacy row", "TOOL-aOld-1 SPECCED False |",
        lambda: read_legacy("- SPECCED" + SEP + "TOOL-aOld-1" + SEP + "some prose"))
    arm("an ASCII ` - ` separated legacy row", "TOOL-aOld-1 BLOCKED False |",
        lambda: read_legacy("- TOOL-aOld-1 - BLOCKED - some prose"))
    arm("the `CLOSED by` slot keeps its evidence in the body", "TOOL-aOld-1 CLOSED False |",
        lambda: read_legacy("- TOOL-aOld-1" + SEP + "CLOSED by deletion (TOOL-aOld-9)" + SEP + "p"))
    arm("and the evidence prose is not thrown away", "deletion (TOOL-aOld-9)",
        lambda: read_legacy_row("- TOOL-aOld-1" + SEP + "CLOSED by deletion (TOOL-aOld-9)" + SEP
                                + "p", build_grammar(("TOOL",))).body)
    arm("WITHDRAWN folds to WONTDO and raises the flag", "TOOL-aOld-1 WONTDO True |",
        lambda: read_legacy("- TOOL-aOld-1" + SEP + "WITHDRAWN" + SEP + "gone"))
    arm("a prose line returns nothing WITH its reason", "None None False | not a list row",
        lambda: read_legacy("just some prose"))
    arm("an unkeyable list row returns nothing WITH its reason",
        "neither of the first two fields is a well-formed id",
        lambda: read_legacy("- not an id" + SEP + "nor a token" + SEP + "x"))
    arm("a list row whose token is not a legacy status returns nothing",
        "is not a legacy status token",
        lambda: read_legacy("- TOOL-aOld-1" + SEP + "MAYBE" + SEP + "x"))

    # ---- AC10: each verdict staged into an otherwise clean fixture, and the clean control.
    clean_ask = render_ask_row("EXMP-aFoo-1", "2026-02-01", "x", clauses=_CLAUSE_OK)
    clean = [_parse_fixture("aFoo", asks=[clean_ask],
                            rows=[render_sev_row("EXMP-aFoo-1", "LOW", "w")])]
    arm("the clean fixture reports NO verdict", "[]", lambda: str(_read_codes(clean)))
    arm("V1 — the ask's slug is not its folder", "[1]",
        lambda: str(_read_codes([_parse_fixture(
            "aBar", asks=[clean_ask], rows=[render_sev_row("EXMP-aFoo-1", "LOW", "w")])])))
    arm("V1 names the folder AND the slug", "carries slug `aFoo` and is filed in build folder `aBar`",
        lambda: str([v.text for v in derive_verdicts(build_corpus([_parse_fixture(
            "aBar", asks=[clean_ask], rows=[render_sev_row("EXMP-aFoo-1", "LOW", "w")])]),
            _CLEAN_CONF) if v.code == 1][0]))
    # THE MERGE SHAPE, staged as two parsed copies of ONE path. That is what V3 is for: each branch
    # files the ask once and is green, and the pair only exists in the merged tree. Two DIFFERENT
    # build folders would have tripped V1 as well, and a fixture that fires two verdicts cannot say
    # which rule the arm caught.
    dup = clean + [_parse_fixture("aFoo", asks=[clean_ask],
                                  rows=[render_sev_row("EXMP-aFoo-1", "MED", "w")])]
    arm("V3 — two ask rows for one id, and nothing else", "[3]", lambda: str(_read_codes(dup)))
    arm("V3's message names both files and both builds",
        "memory/builds/aFoo/BACKLOG.md:4 (build `aFoo`) and memory/builds/aFoo/BACKLOG.md:4",
        lambda: str([v.text for v in derive_verdicts(build_corpus(dup), _CLEAN_CONF)
                     if v.code == 3][0]))
    arm("V5 — a derived token used as a verb", "[5]",
        lambda: str(_read_codes([_parse_fixture(
            "aFoo", asks=[clean_ask],
            rows=[render_sev_row("EXMP-aFoo-1", "LOW", "w"),
                  "- OPEN" + SEP + "EXMP-aFoo-1" + SEP + "x"])])))
    arm("V7 — a verb row targeting an ask nobody filed", "[7]",
        lambda: str(_read_codes(clean + [_parse_fixture(
            "aBar", rows=[render_status_row("KEEP", "OTHR-aBar-3", "w")])])))
    arm("V7 — a `closes` naming an ask nobody filed", "[7]",
        lambda: str(_read_codes(clean, [_build_spec("EXMP-aFoo-7", "CLOSED",
                                                    closes=["OTHR-aBar-3"])])))
    arm("V8 — a CLOSED row `by` a value that resolves to nothing", "[8]",
        lambda: str(_read_codes([_parse_fixture(
            "aFoo", asks=[clean_ask],
            rows=[render_sev_row("EXMP-aFoo-1", "LOW", "w"),
                  render_status_row("CLOSED", "EXMP-aFoo-1", "w", "EXMP-aFoo-9")])])))
    arm("a CLOSED row `by` a SHA is shape-checked only and is NOT V8", "[]",
        lambda: str(_read_codes([_parse_fixture(
            "aFoo", asks=[clean_ask],
            rows=[render_sev_row("EXMP-aFoo-1", "LOW", "w"),
                  render_status_row("CLOSED", "EXMP-aFoo-1", "w", "abc1234")])])))
    arm("V9 — a post-cutoff ask whose id is a spec H1 without the `unit` marker", "[9]",
        lambda: str(_read_codes([_parse_fixture(
            "aFoo", asks=[render_ask_row("EXMP-aFoo-1", "2026-06-01", "x", clauses=_CLAUSE_OK)],
            rows=[render_sev_row("EXMP-aFoo-1", "LOW", "w")])],
            [_build_spec("EXMP-aFoo-1", "SPECCED")])))
    arm("V9 names the ask's file AND the spec's", "and a spec H1 carries the same id at "
                                                  "spec/EXMP-aFoo-1.md",
        lambda: str([v.text for v in derive_verdicts(build_corpus([_parse_fixture(
            "aFoo", asks=[render_ask_row("EXMP-aFoo-1", "2026-06-01", "x", clauses=_CLAUSE_OK)],
            rows=[render_sev_row("EXMP-aFoo-1", "LOW", "w")])],
            {"EXMP-aFoo-1": _build_spec("EXMP-aFoo-1", "SPECCED")}), _CLEAN_CONF)
            if v.code == 9][0]))
    arm("V10 — a terminal build holding an OPEN ask nobody dispositioned", "[10]",
        lambda: str(_read_codes(
            [_parse_fixture("aFoo", asks=[clean_ask],
                            rows=[render_sev_row("EXMP-aFoo-1", "LOW", "w")])],
            builds={"aFoo": "CLOSED"})))
    arm("a REOPEN counts as that ask's KEEP, so V10 does NOT fire", "[11]",
        lambda: str(_read_codes(
            [_parse_fixture("aFoo", asks=[clean_ask],
                            rows=[render_sev_row("EXMP-aFoo-1", "LOW", "w"),
                                  render_status_row("REOPEN", "EXMP-aFoo-1", "w", "abc1234")])],
            builds={"aFoo": "CLOSED"})))
    arm("V11 — a REOPEN naming no closing record", "[11]",
        lambda: str(_read_codes([_parse_fixture(
            "aFoo", asks=[clean_ask],
            rows=[render_sev_row("EXMP-aFoo-1", "LOW", "w"),
                  render_status_row("REOPEN", "EXMP-aFoo-1", "w", "abc1234")])])))
    arm("V12 — a post-cutoff ask with no SEV row anywhere", "[12]",
        lambda: str(_read_codes([_parse_fixture(
            "aFoo", asks=[render_ask_row("EXMP-aFoo-1", "2026-06-01", "x", clauses=_CLAUSE_OK)])])))
    # TOOL-dDerivedDocket-19 S5 — a SCOPE row's `may` is V13 whatever it says, and the same row with no
    # grant is the control that says the label is the finding and not the row.
    def build_scope_fixture(*clauses):
        return [_parse_fixture("aFoo", asks=[clean_ask],
                               rows=[render_sev_row("EXMP-aFoo-1", "LOW", "w"),
                                     render_scope_row("EXMP-aFoo-1", clauses)])]

    arm("V13 — a SCOPE row carrying a `may` grant", "[13]",
        lambda: str(_read_codes(build_scope_fixture(("may", "`tools/push-main.sh`")))))
    arm("V13 — a SCOPE row carrying `may none` is the same finding", "[13]",
        lambda: str(_read_codes(build_scope_fixture(("may", GRANT_NONE)))))
    arm("V13 names the SCOPE row and the label it may not carry",
        "SCOPE row for EXMP-aFoo-1 carries a `may` clause, and a SCOPE row honours no grant",
        lambda: str([v.text for v in derive_verdicts(build_corpus(
            build_scope_fixture(("may", "`tools/push-main.sh`"))), _CLEAN_CONF) if v.code == 13]))
    arm("a SCOPE row carrying no `may` is not V13", "[]",
        lambda: str(_read_codes(build_scope_fixture(("accept", "cured from outside")))))
    arm("V15 — a blank cutoff under `builds`", "[15]",
        lambda: str(_read_codes(clean, conf=read_conf({MODE_KEY: "builds", CUTOFF_KEY: ""}))))
    arm("V16 — an unpadded cutoff under `builds`", "[16]",
        lambda: str(_read_codes(clean, conf=read_conf({MODE_KEY: "builds",
                                                       CUTOFF_KEY: "2026-9-30"}))))

    # ---- AC11: the two conf keys.
    def read_mode(conf):
        return read_conf(conf).mode

    arm("an absent BACKLOG_MODE reads shards", "shards", lambda: read_mode({}))
    arm("a blank BACKLOG_MODE reads shards", "shards", lambda: read_mode({MODE_KEY: ""}))
    arm("`shards` reads shards", "shards", lambda: read_mode({MODE_KEY: "shards"}))
    arm("`builds` reads builds", "builds", lambda: read_mode({MODE_KEY: "builds"}))
    arm("`shard` is a refusal naming the legal set", "is not one of: shards builds",
        lambda: read_mode({MODE_KEY: "shard"}))
    arm("`builds` with a blank cutoff returns V15", "[15]",
        lambda: str([v.code for v in read_conf({MODE_KEY: "builds", CUTOFF_KEY: ""}).verdicts]))
    arm("`builds` with an unpadded cutoff returns V16 naming the key", "ASK_CUTOFF='2026-9-30'",
        lambda: str(read_conf({MODE_KEY: "builds", CUTOFF_KEY: "2026-9-30"}).verdicts[0].text))
    arm("`builds` with a zero-padded cutoff returns neither", "[]",
        lambda: str([v.code for v in
                     read_conf({MODE_KEY: "builds", CUTOFF_KEY: "2026-09-30"}).verdicts]))
    arm("under `shards` the cutoff is not read at all", "[]",
        lambda: str([v.code for v in
                     read_conf({MODE_KEY: "shards", CUTOFF_KEY: "nonsense"}).verdicts]))
    # AN UNPADDED CUTOFF COMPARED AS A RAW STRING is the defect V16 exists for: `"2026-10-01" <
    # "2026-9-30"` is true, so an October ask would sort BEFORE a September cutoff and V9 and V12
    # would go quiet on exactly the asks they were armed for.
    arm("the disarming is real: V12 does not fire while V16 stands", "[16]",
        lambda: str(_read_codes([_parse_fixture(
            "aFoo", asks=[render_ask_row("EXMP-aFoo-1", "2026-10-01", "x")])],
            conf=read_conf({MODE_KEY: "builds", CUTOFF_KEY: "2026-9-30"}))))

    # ---- the counts the view unit's liveness line prints.
    arm("the fold returns the counts, and `verdicts` is None when nobody asked",
        "{'files': 1, 'asks': 1, 'rows': 1, 'links': 1, 'live': 1, 'verdicts': None}",
        lambda: str(_read_fold(clean, perm_specs)[0].counts))
    return fails


def cmd_selftest() -> int:
    fails = run_arms()
    if fails:
        print(f"FAIL — {len(fails)} arm(s) failed")
        return 1
    print("PASS — backlog: all arms held")
    return 0


def main(argv: list) -> int:
    mode = argv[1] if len(argv) > 1 else "--help"
    if mode == "--selftest":
        return cmd_selftest()
    print("usage: backlog.py --selftest")
    print("  the grammar, the fold and the verdicts are a LIBRARY; the view unit prints them")
    return 0 if mode == "--help" else 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
