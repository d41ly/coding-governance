#!/usr/bin/env python3
"""check-spec-tokens.py — a spec's machine-facing tokens resolve against the tree that owns them.

TOOL-dRetiredFork-20. Three spec-audit rounds over one build found the same class by hand every
time: a section 7 gate name that is not a leg (18 of 36 in one set), a section 6 criterion whose
witness path is not tracked, and a `path:line` citation four lines short. Each is a JOIN over two
tracked files, and hand-verifying them is what this replaces.

WHAT IT DOES NOT CHECK, stated here because a structural check reads as a semantic one to everybody
who did not write it. It resolves EXISTENCE and RANGE. It does not read the cited line and does not
know whether it says what the spec claims; a citation naming a real line that argues the opposite
passes. It does not grade scope, acceptance or tier, and grades prose only where the claims join
grades a dossier-claim sentence's SHAPE. The bar join reads an INVOCATION as a
spec spells it inside backticks, and nothing else: it cannot see a path built at runtime,
a runner spelled inside a sh -c string,
a suite run written as the body of a fenced block,
or a suite named in prose.
Each of those is the ACT, and the act is refused by the hook of TOOL-aDeferredBar-3, not here.
The claims join (TOOL-dGatedProse-2) grades the SHAPE of a claimed object and resolves nothing, and
six things are invisible to it by construction: (1) an unbackticked dossier subject, because the
look-back window that would read one scored precision 0.00 over this corpus; (2) an unbackticked
claimed object, because every arm grades a run of backticked objects; (3) a claim inside a fenced
block, blanked so a spec may exhibit the refused sentence as a worked example; (4) a key-shaped
object that is not a key, a typo included, which the map's own both-directions ratchet fails once a
dossier claims it; (5) a claim in the wrong dossier, because no dossier's claims table is read; and
(6) a filler run longer than the closed arm admits, such as four words between the subject and the
noun arm's verb where that arm admits three. A zero from it is the corpus's normal state, and
CLAIM_CANARY is what separates that zero from a dead arm.

THE JOINS KEEP THEIR POPULATIONS APART, the correction rev-2 folded from round 3. The fourth join,
`bar`, reads two of the three rather than minting a fourth; the fifth, `guards`, reads the legs
population plus one of its own, the declared write set; the sixth, `claims`, reads none of them,
being a grammar over the spec's own prose outside its fenced blocks.

  legs   backticked tokens on a `## 7. Gates` LINE THAT IS THE LIST -> a `name` in the manifest.
         A section 7 line carrying prose is not graded: measured, that predicate produced 270
         hits of which 271 came from prose in one spec. The arm reports its graded count so a
         green row cannot be read as covering the prose it skipped.
  paths  every backticked PATH-SHAPED token inside an acceptance-criteria bullet -> `git ls-files`.
         The bullet loop finds the acceptance section by heading text (`AC_HEAD`), never by its
         ordinal, so a light-profile spec is graded where its criteria sit (TOOL-aDeferredBar-2).
         Path-shaped is a slash AND an extension, or an exact tracked path
         (TOOL-dRetiredFork-20 F2). A bare word is prose and is not a path.
  cites  every backticked `<path>:<line>` -> that file's line count, SCOPED to citations whose path
         is TRACKED. Measured at b0108f13: 453 specs carry 1721 citations and 854 of them name an
         untracked path, because the house style cites a kit file by basename (`run-gates.sh:407`).
         Redding those is 854 dispositions and this lint never lands; passing them silently is a
         could-not-fail arm over half the corpus. So they are SKIPPED AND COUNTED, and the count is
         printed on every run — a skip that does not announce itself is indistinguishable from
         coverage.
  bar    every backticked token of the legs and paths populations that spells a merge-bar or
         self-test-suite INVOCATION, in a LIVE spec dated at or after SPEC_DIRECT_CUTOFF
         (`.memory-tree.conf`, blank = off) -> a hit (TOOL-aDeferredBar-2). A bar or a suite is
         not an acceptance observation: the pass observes the checker on a staged break, a
         --selftest flag or a fixture, and the bar runs once after the build is complete. The
         test runs FIRST in each loop, on the raw token, because NOT_A_TOKEN and NOT_A_LEG would
         drop the motivating `GATE_SELFTESTS=1 bash ...` token unread. Pre-cutoff carriers are
         COUNTED on the report line and listed by --list as NEAR, so the OFF state and the
         day-one zero cannot hide what they skip. A set key that is not strictly past the day it
         was committed is REFUSED before grading: the register's rule is a relation to the fleet
         working day, and a value carried across a day boundary is stale by construction.
  guards every backticked PATH-SHAPED token under a spec's `### Files touched` sub-head — spelled
         with or without ` (estimate)`, the declared write set — joined to every `guard` list in
         the manifest with git-pathspec semantics (`p == g` or `p` under `g/`, never a bare prefix,
         so an exact-file guard does not trip on `x.sh.bak`): a leg whose guard the write set
         trips must be a name on the section 7 leg line, in a LIVE spec dated at or after
         SPEC_GUARD_LEGS_CUTOFF (blank = off) -> a hit whose token is the composite
         `<leg> <- <path>` (TOOL-aBlindedTrial-8). A DIRECTORY token under the sub-head — one
         ending in `/` and of TWO OR MORE segments, `tools/run-gates/` — is a declared PREFIX and
         trips SYMMETRICALLY: a guard it equals or sits under, and a guard that sits under it
         (closing review round 1, R3; writing the folder instead of the files was a clean pass
         before). A ONE-segment token, `tools/`, is a ROOT and declares nothing: it is how prose
         names a tree ("No file under `tools/` is touched"), and --list names it as NEAR (round
         2, R1). The residual, stated in BOTH directions (round 3, R4): a two-segment directory
         named in prose is still read as declared, and a one-segment directory that is itself a
         joined guard, `.githooks/`, declared wholesale declares nothing - name its files or a
         two-segment child. The join grades only a spec that CARRIES a Gates heading, the legline arm's own
         precondition: a Tier-1 spec under the light profile may omit the section, and one that
         does is COUNTED on the guards line rather than joined or examined, its tripping paths
         listed as NEAR (R4, round 2 R8). BROAD guards are EXCLUDED from the join and listed by
         --list as NEAR, and broad is BREADTH, not depth (R1): a guard carried by MORE than
         BROAD_LEG_FLOOR LEGS (a guard listed twice in one row is one leg), whatever its depth,
         because a guard many legs share adds no information when named and buries the specific
         one. The excluded set is printed WITH its per-guard leg counts on the guards line of every
         run, so the exclusion announces itself and no count of it lives in prose. A leg without a
         `guard` key is not joined; a spec without the sub-head declares nothing and is counted
         apart. The join reads the ESTIMATE as written, not the write set the build actually made;
         it reads no path named in prose outside the sub-head; and it reads a guard as a directory
         or an exact file, never as git pathspec magic. The motivating case: a unit that edited
         `tools/hooks/scratch-guard.js` and omitted `scratch-guard self-test`, found by a closing
         review and not by a gate.
  claims every backticked OBJECT a dossier-claim SENTENCE names, in a LIVE spec, outside fenced
         blocks, with no cutoff key (owner, 2026-09-21) -> a hit when the object is a PATH (a
         `/`), a GLOB (a `*` or `?`) or a CODE SYMBOL (an underscore between two letters or
         digits, either case, or a parenthesis), none of which the map can hold as a key
         (TOOL-dGatedProse-2). A sentence is one of four arms anchored on a backticked dossier
         subject — a features dossier, the foundation dossier or a bare `.md` basename — built
         from CLOSED word lists and named active, passive, noun and fronted. Each yields the
         MAXIMAL run of objects a comma, `and`, `or`, `plus` or the middle dot joins, so a
         conjunction cannot hide its second object. A token carrying a space is never refused:
         every live key carrying punctuation also carries a space, and that clause is what keeps
         the refusal set disjoint from the key set. Every cleared object is listed by --list as
         NEAR, and the join's line prints on every run, because it has no key to branch on.

REFUSALS, not passes. An empty spec population refuses: a lint that graded nothing reports the same
zero as a clean tree. An unreadable manifest refuses. A waiver row naming a path no spec cites, or
one the tree now tracks, refuses — a stale exception cannot hide a live hit. A cutoff the tree's own
history dates at or after itself refuses, and so does EVERY cutoff key this file reads whose value
is not a real ISO date, SPEC_LEGLINE_CUTOFF and SPEC_GUARD_LEGS_CUTOFF included, because all of
them pass through `read_cutoff_key`: the comparisons are string comparisons, and a malformed value
would report the join as set while it graded nothing.

  python tools/check-spec-tokens.py            # assert; exit 1 on an unwaived hit
  python tools/check-spec-tokens.py --list     # every hit and near-miss, authoring aid, exit 0
"""
import datetime
import json
import pathlib
import re
import subprocess
import sys

KIT_SPEC_TOKENS_VERSION = "1.1"  # gov:kit spec-tokens@1.1 — the deployer's read

WAIVERS = "memory/project/spec-token-waivers.txt"
SPEC_GLOB = "memory/builds/*/spec/*.md"
LEGS = "tools/gate-legs.json"

SEC = r"^## %s\.[^\n]*\n(.*?)(?=\n## |\Z)"
TICK = re.compile(r"`([^`\n]+)`")
CITE = re.compile(r"`([^`\s]+\.[A-Za-z0-9]+):(\d+)(?:-\d+)?`")
CITE_TAIL = re.compile(r":\d+(-\d+)?$")
# A deploy-time token or an env assignment is never a path or a leg.
NOT_A_TOKEN = re.compile(r"^(GATE_|\{\{|\$|~|'|\"|<)")
# A section 7 list carries more than leg names: commands to run, conf keys, and the files a leg
# grades. The pre-wiring run over 453 specs surfaced all three and they are not defects, so the leg
# join excludes them by SHAPE rather than by waiver. A leg name is prose: no slash, no leading dot,
# not a bare SHOUTED_KEY, and not a command line.
NOT_A_LEG = re.compile(r"^(bash |sh |python3? |node |git )|/|^\.|^[A-Z][A-Z0-9_]+$")
# Terminal specs are FROZEN records. This repo cites a landed decision verbatim and never rewrites
# it, so grading a CLOSED spec would demand editing one to clear a hit. The population is the specs
# a build can still change.
LIVE = re.compile(r"^\*\*Status:\*\*\s*(OPEN|SPECCED|INPROGRESS|BLOCKED)", re.M)
# Section 7 is a LIST in the house style — backticked leg names joined by the middle dot — but many
# specs carry prose there too. Measured over the live corpus: treating every backticked token in
# section 7 as a leg name produced 270 hits, 271 of them from prose in a single spec. So the join
# reads only lines that ARE the list: nothing outside the backticks but separators and punctuation.
# A prose line naming a leg is therefore NOT graded, which is the honest limit of this arm and is
# reported as such rather than implied away.
LEG_LINE = re.compile(r"^[\s]*(`[^`\n]+`[\s]*[·,]?[\s]*)+\.?[\s]*$")
# TOOL-aJoinedCanon-7: the Gates section is located by HEADING TEXT and never by ordinal.
GATES_HEAD = re.compile(r"^## [0-9]+[.] Gates[ \t]*$", re.M)
# The dated demand, the owner's ruling on this unit's fork. From this date a LIVE spec that CARRIES a
# Gates heading must contribute at least one graded leg name from it. The heading precondition is the
# whole of the Tier-1 accommodation: under the light profile a spec may legally omit the section, and
# one that omits it stays silent rather than red. Blank or absent turns the arm off.
LEGLINE_KEY = "SPEC_LEGLINE_CUTOFF"
SPEC_DATE = re.compile(r"/([0-9]{4}-[0-9]{2}-[0-9]{2})-spec-")
# TOOL-aDeferredBar-2: the bar join's key, heading pattern and predicate. Blank or absent is OFF.
DIRECT_KEY = "SPEC_DIRECT_CUTOFF"
# TOOL-aBlindedTrial-8: the guards join's key and the sub-head it reads. The corpus spells the
# sub-head both ways (437 with the parenthetical, 21 without at 987c5bec), so the suffix is optional.
# The section body ends at the NEXT heading of any depth, because the sub-head has siblings.
GUARDS_KEY = "SPEC_GUARD_LEGS_CUTOFF"
FILES_HEAD = re.compile(r"^### Files touched( \(estimate\))?[ \t]*$", re.M)
# A guard carried by MORE than this many legs is BROAD and leaves the guards join (closing review
# round 1, R1). Measured on the manifest at 144cd1fb: 5 keeps `tools/hooks/` (5 legs, the motivating
# case) and `.githooks/` (5) joined and drops `tools/lib/` (30), `tools/` (11), `tools/memory-tree/`
# (9) and `tools/run-gates/` (6). The figures live here as the reason for the floor, dated; the set
# the floor excludes TODAY is derived and printed on every run, never typed.
BROAD_LEG_FLOOR = 5
# The acceptance section by HEADING TEXT, the shape GATES_HEAD already has and for the same reason:
# a light-profile spec drops `## 5.` and the ordinal read grades whatever sits sixth.
AC_HEAD = re.compile(r"^## [0-9]+[.] Acceptance criteria[ \t]*$", re.M)
# A merge-bar or suite INVOCATION: the runner or a suite at command position — the token's start
# or a chain separator, past optional VAR=value prefixes, `timeout` with its options and duration,
# and a bash/sh/python/py launcher with one option — a short one, `py`'s version selector
# (`-3`, `-3.12`) or `-X` with its value glued or as the next word (closing round 3 T6) — never
# `-n`, the no-exec syntax check the hook of TOOL-aDeferredBar-3 admits, nor `-c`/`-m`, whose
# argument is code; closing round 2 R12 gave this reader the slots that hook grew, so
# `python -u <suite>`, `py <suite>` and `timeout -k 5 120 bash <suite>` read alike in both, and
# the duration slot already took any word, so `timeout "$GATE_BOUND" bash <suite>` was a hit here
# before round 3 T5 made it one in the hook — or a
# GATE_FULL= / GATE_SELFTESTS= assignment with a NON-EMPTY value anywhere in the
# token. A suite is a `.test.sh` file OR a whole-suite `selftest.py` file (closing review F2: six
# manifest legs are the latter and both readers had spelled "suite" as the shell convention); a
# `--selftest` FLAG on some other file is the seconds-long direct check and is not a run. A
# `path:line` citation fails the trailing lookahead and stays the cites join's; a grep over a suite
# FILE has grep at command position and is not a run; the empty assignment is the OFF spelling, and
# so is the QUOTED empty one, `GATE_FULL=""` — the quote is not a value (closing review F9, where
# `\S` read it as one while the hook of TOOL-aDeferredBar-3 unquoted it to OFF).
BAR = re.compile(
    r"(?:^|&&|[;|(])\s*(?:\w+=\S*\s+)*(?:timeout\s+(?:(?:-[ks]|--kill-after|--signal)\s+\S+\s+|-\S+\s+)*\S+\s+)?"
    r"(?:(?:bash|sh|python3?(?:\.\d+)?|py)\s+(?:(?!-[ncm]\s)(?:-X\S*(?:\s+\S+)?|-[A-Za-z]+|-\d+(?:\.\d+)?)\s+)?)?(?:\S*/)?"
    r"(?:(?:run-gates|run-selftests|run-unattended-gates|[^\s/*?]+\.test)\.sh|selftest\.py)(?=\s|$)"
    r"|(?:^|\s)GATE_(?:FULL|SELFTESTS)=[\"']?[^\s\"']")
BAR_WHY = ("a bar or suite is not an acceptance observation: observe the checker on a staged break, "
           "a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites "
           "run once, after the build is complete")

# TOOL-dGatedProse-2: THE CLAIMS JOIN. A codebase-map dossier claims EXACT inventory keys and nothing
# else, so a spec sentence saying a dossier claims a path, a glob or a code symbol books a grader that
# does not exist. It is a GRAMMAR over the spec's prose plus a closed refusal set over the object it
# names; nothing resolves, so nothing goes stale and nothing resolves by coincidence. Every filler is a
# CLOSED word list: an open `\w+` filler is what walked the dry run's broad predicate out of one clause
# and into the next. The fragments are named once here and composed into the four arms below.
CLAIM_PARTS = {
    # A backticked dossier SUBJECT: a features dossier, the foundation dossier, or a bare basename.
    "subj": r"`(?:memory/map/features/[A-Za-z0-9._-]+|memory/map/FOUNDATION|[A-Za-z0-9._-]+)\.md`",
    # A backticked OBJECT. A full dossier path is never one: it is the next clause's subject, and
    # reading it as claimed would red it as a PATH.
    "obj": r"`(?!(?:memory/map/features/[A-Za-z0-9._-]+|memory/map/FOUNDATION)\.md`)[^`\n]+`",
    # The one dash or colon a subject may carry before its verb, the way a list row writes it.
    "gap": r"(?:\s*[\u2014\u2013:-])?",
    # No negation is a modal, so "does not claim" is no claim; `to` is one, so "to claim" is.
    "modal": r"(?:will|would|shall|should|must|may|might|can|could|does|do|did|to|now|also|still"
             r"|then|thus|already|only|newly|explicitly|deliberately|therefore)",
    "verb": r"claim(?:s|ed|ing)?",
    # `that` is no determiner, so a that-clause after the verb reaches nothing.
    "det": r"(?:the|a|an|its|their|this|these|those|both|each|every|all|one|two|three|new|same"
           r"|exact|existing)",
    "copula": r"(?:is|are|was|were|be|been|being|gets?|got|stays?|remains?)",
    "rel": r"(?:which|that)",
    "word": r"[A-Za-z][\w'\u2019-]*",
}
# The run: a MAXIMAL chain of objects joined by nothing but a comma, `and`, `or`, `plus` or the middle
# dot, so a conjunction cannot hide its second object.
CLAIM_PARTS["run"] = (r"(?P<run>{obj}(?:(?:\s*[,\u00b7]\s*(?:(?:and|or|plus)\s+)?|\s+(?:and|or|plus)\s+)"
                      r"{obj})*)").format(**CLAIM_PARTS)
# The four arms, in the order the report names them, each MATCHED at a token start and never searched.
CLAIM_ARMS = [(name, re.compile(shape.format(**CLAIM_PARTS), re.I)) for name, shape in (
    ("active", r"{subj}{gap}(?:\s+{modal}){{0,2}}\s+{verb}(?:\s+{det}){{0,3}}\s+{run}"),
    ("passive", r"{run}(?:\s+{modal}){{0,2}}\s+{copula}(?:\s+{modal})?\s+claimed\s+by(?:\s+{det})?\s+{subj}"),
    ("noun", r"{subj}(?:['\u2019]s)?{gap}(?:\s+{word}){{0,3}}?\s+claims?\s+(?:on|over|to|under|as)"
             r"(?:\s+{det}){{0,3}}\s+{run}"),
    ("fronted", r"{run}(?:\s*,\s*{rel}|\s+{rel})?\s+{subj}(?:\s+dossier)?(?:\s+{modal}){{0,2}}\s+{verb}\b"),
)]
# The refusal set, one row per class, and the FIRST ROW TO MATCH DECIDES. The first row is the shared
# SPACE CLAUSE, which clears: every live key carrying punctuation also carries a space, so this row is
# what keeps the three classes disjoint from the key set, and the self-test re-derives that on every
# run. GLOB is tested before PATH so `tools/*/kit.toml` reports its real shape; both rest on the same
# sentence of the map's contract, so the order moves a label and never a verdict.
CLAIM_REFUSALS = (
    ("", re.compile(r"\s"), "cleared by the space clause: a token carrying a space is never refused"),
    ("GLOB", re.compile(r"[*?]"), "the map README rules that path globs are digest-only, never gated "
     "(memory/map/README.md, rendered by tools/codebase-map/gen_map.py)"),
    ("PATH", re.compile(r"/"), "the map README rules that path globs are digest-only, never gated "
     "(memory/map/README.md, rendered by tools/codebase-map/gen_map.py)"),
    ("CODE SYMBOL", re.compile(r"[A-Za-z0-9]_[A-Za-z0-9]|[()]"), "the symbol tier feeds "
     "generated/symbols.json only and never the ratchet (tools/codebase-map/map_extractors.py)"),
)
CLAIMS_WHY = ("a codebase-map dossier claims EXACT inventory keys and no key is a {cls}: {cite}; name "
              "the key the dossier will claim, or describe the thing in prose")
# THE LIVENESS ASSERTION (charter §7). A zero from this join is the corpus's measured normal state, so a
# dead arm would report exactly what a clean corpus reports. One refused claim per arm, each verb in
# UPPERCASE so the case fold is load-bearing on every arm, between them covering all three classes,
# plus one claim on a real parenthesised leg name that must CLEAR, which is what pins the space clause.
# `check_claim_canary` tests the entries STRUCTURALLY and never against a typed total.
CLAIM_CANARY = [
    ("`memory/map/features/runlog.md` CLAIMS `derive_window_closer`.", "active", "CODE SYMBOL"),
    ("`tools/runlog/*.py` is CLAIMED BY `runlog.md`.", "passive", "GLOB"),
    ("`runlog.md`'s CLAIM on `tools/runlog/runlog.py` stands.", "noun", "PATH"),
    ("`read_window()`, which `memory/map/features/runlog.md` CLAIMS, stays.", "fronted", "CODE SYMBOL"),
    ("`memory/map/features/spec-tokens.md` CLAIMS `spec tokens (a spec's own names resolve)`.",
     "active", ""),
]


def run(*args):
    return subprocess.run(args, capture_output=True, text=True).stdout


def read_tracked(root):
    return set(run("git", "-C", str(root), "ls-files").split())


def extract_section(text, num):
    m = re.search(SEC % num, text, re.S | re.M)
    return m.group(1) if m else ""


def extract_gates(text):
    """Section 7 by its HEADING TEXT, never by its ordinal.

    TOOL-aJoinedCanon-7. A Tier-1 spec under the light profile may legally drop
    `## 5. Production-readiness checklist`, which slides every later section up one — so the ordinal
    read grades whatever happens to sit seventh, and once the S7 arm below turns a silent read into a
    VERDICT that becomes a red on a spec the format permits. The pattern is check 12's
    acceptance-witness regex with one word changed: bracketed dot, tab class and end anchor intact.

    Returns None when the spec carries NO Gates heading at all. That is a different fact from an
    empty section and the report keeps the two apart, because they have different remedies.
    """
    m = GATES_HEAD.search(text)
    if not m:
        return None
    rest = text[m.end():]
    nxt = re.search(r"^## ", rest, re.M)
    return rest[:nxt.start()] if nxt else rest


def extract_acceptance(text):
    """The acceptance section by its HEADING TEXT — `extract_gates` with `AC_HEAD` in its place.

    TOOL-aDeferredBar-2. Both bullet-loop joins read it: the ordinal read graded whatever sat sixth,
    which under the light profile is the Gates section. None when the spec carries no such heading,
    which the bullet loop reads as an empty population.
    """
    m = AC_HEAD.search(text)
    if not m:
        return None
    rest = text[m.end():]
    nxt = re.search(r"^## ", rest, re.M)
    return rest[:nxt.start()] if nxt else rest


def extract_files_touched(text, files):
    """The declared write set and the roots it mentions, as `(paths, roots)`. `paths` is every
    path-shaped word inside backticks under the `### Files touched` sub-head, in order and without
    repeats, PLUS every directory-shaped one kept with its trailing `/` so the join can read it as a
    prefix (closing review round 1, R3 — the trailing-slash rule of `check_path_shaped` is right for
    the paths and cites joins and wrong here, where `tools/x/` declares everything under it). `roots`
    is every ONE-segment directory token — `tools/`, `memory/` — which declares NOTHING (round 2,
    R1, measured at 315201b0: a one-segment `tools/` token appeared 14 times over every spec, every
    one prose such as "No file under `tools/` is touched", and reading it as declared owed 34 legs);
    they are returned so `--list` can name the skip. None when the spec carries no such sub-head, which the report counts apart from a
    sub-head declaring nothing (TOOL-aBlindedTrial-8). The body closes at the next heading of ANY
    depth, unlike the section readers above, because the sub-head has siblings inside section 4.
    """
    m = FILES_HEAD.search(text)
    if not m:
        return None
    rest = text[m.end():]
    nxt = re.search(r"^##+ ", rest, re.M)
    body = rest[:nxt.start()] if nxt else rest
    paths, roots = [], []
    for tok in TICK.findall(body):
        for word in tok.split():
            if len(derive_dir_segments(word)) == 1:
                if word not in roots:
                    roots.append(word)
            elif (check_path_shaped(word, files) or check_dir_shaped(word)) and word not in paths:
                paths.append(word)
    return paths, roots


def derive_dir_segments(tok):
    """The REAL segments of a `/`-terminated token this join could read, or `[]` for anything else:
    a token that is not `/`-terminated, opens like a deploy-time token, carries a glob or a space, or
    has a segment that is empty, `.` or `..` — so `./`, `../` and `tools/./` are nothing, not a path
    (round 2, R8). `tools/` -> `['tools']`; `tools/run-gates/` -> `['tools', 'run-gates']`."""
    if NOT_A_TOKEN.match(tok) or " " in tok or "*" in tok or "?" in tok or not tok.endswith("/"):
        return []
    parts = tok.rstrip("/").split("/")
    return [] if any(x in ("", ".", "..") for x in parts) else parts


def check_dir_shaped(tok):
    """A declared PREFIX: a directory token of TWO OR MORE real segments. A one-segment token is a
    ROOT (`tools/`), which is how prose names a tree and declares nothing (round 2, R1); round 1's
    fold kept it and owed every non-broad leg under it. The residual, both directions (round 3,
    R4): a two-segment directory named in prose is still read as declared, and a one-segment
    directory that is itself a joined guard (`.githooks/`) declared wholesale declares nothing -
    its files, or a two-segment child, must be named."""
    return len(derive_dir_segments(tok)) >= 2


def check_guard_trips(path, guard):
    """Git-pathspec semantics for a manifest guard: the exact path, or anything under it as a
    directory. Never a bare prefix, so `tools/x.sh` does not trip on `tools/x.sh.bak`. A declared
    DIRECTORY (its trailing `/` kept by `extract_files_touched`, two or more segments — a root never
    reaches here) trips symmetrically: it also trips a guard that sits under it, an exact-file guard
    included, because `tools/x/` declares `tools/x/y.sh` (R3)."""
    p, g = path.rstrip("/"), guard.rstrip("/")
    if p == g or p.startswith(g + "/"):
        return True
    return path.endswith("/") and g.startswith(p + "/")


def derive_guarded_legs(rows):
    """The manifest's guarded legs, split by guard BREADTH. Returns `(joined, broad)`: `broad` is
    `{guard: legs}` for every guard carried by MORE than BROAD_LEG_FLOOR legs over the whole
    manifest, whatever its depth, which the join excludes, prints with its counts and --list reports
    as NEAR; `joined` is `(name, [guards])` for every leg carrying at least one guard that is not
    broad, with the broad ones dropped from its list. A leg with no `guard` key is absent from both
    (fixture manifests omit it). rev-1 split on DEPTH — one segment or more — and on the real
    manifest that joined `tools/lib/` (30 legs) and excluded `.githooks/` (5); the count is the
    property the exclusion was written for (closing review round 1, R1)."""
    count = {}
    for r in rows:
        for g in set(r.get("guard") or []):   # LEGS, not entries: a guard listed twice in one row is one leg (round 2, R7)
            count[g] = count.get(g, 0) + 1
    broad = {g: n for g, n in count.items() if n > BROAD_LEG_FLOOR}
    joined = []
    for r in rows:
        keep = [g for g in (r.get("guard") or []) if g not in broad]
        if keep:
            joined.append((r["name"], keep))
    return joined, broad


def render_broad(broad):
    """The excluded set as the report prints it, count-descending then by name; `none` when empty."""
    return " ".join(f"{g} ({n})" for g, n in sorted(broad.items(), key=lambda kv: (-kv[1], kv[0]))) or "none"


def check_cutoff_relation(root, key, value):
    """THE RELATION, ASSERTED (TOOL-aDeferredBar-2, Date gate; one helper for every cutoff key that
    carries it since TOOL-aBlindedTrial-8). The register's rule puts a new cutoff strictly past the
    day it is set, so a value the tree's own history dates at or after itself was carried across a
    day boundary instead of re-derived. It is compared to the SETTING COMMIT's date and not to the
    newest spec date on the tree: from the day after landing, that comparison refuses exactly the
    population the join exists to grade. A value not yet in history cannot be checked and is
    announced, never refused or passed. Returns the report-line suffix, or None after printing the
    refusal.

    PICKAXE `-S`, NOT `-G` (closing review F4): `-G` matches any hunk that adds OR removes the line,
    so a block move, a requote or a whitespace cleanup re-dated the "setting commit" to that later
    day and the gate refused a value nobody re-set. `-S` matches a change in the line's OCCURRENCE
    COUNT, which a move or a requote leaves at one.
    """
    q = subprocess.run(["git", "-C", str(root), "log", "-1", "--format=%cs", "--pickaxe-regex",
                        f'-S^{key}="?{value}"?$', "--", ".memory-tree.conf"],
                       capture_output=True, text=True)
    if q.returncode:
        # A delegate whose status is discarded reads a query that never ran as "not yet committed"
        # — the announced skip with the wrong reason, which the next reader trusts.
        print(f"spec-tokens: REFUSING — the history query for {key} {value} failed, so the "
              f"relation cannot be asserted: {q.stderr.strip() or 'git exited ' + str(q.returncode)}")
        return None
    set_on = q.stdout.strip()
    if not set_on:
        return " · relation unchecked: value not yet committed"
    if value <= set_on:
        print(f"spec-tokens: REFUSING — {key} {value} is not strictly past {set_on}, the day the "
              "value was committed; the register's rule is the day AFTER the later of the newest "
              "spec filename date on any ref and the setting commit's own date")
        return None
    return ""


def read_conf_key(root, key):
    """One key out of `.memory-tree.conf`, by plain assignment. Absent or blank means OFF."""
    p = root / ".memory-tree.conf"
    if not p.exists():
        return ""
    m = re.search(r'^%s="?([^"\n]*)"?\s*$' % re.escape(key),
                  p.read_bytes().decode("utf-8", "replace"), re.M)
    return m.group(1).strip() if m else ""


def read_cutoff_key(root, key):
    """`read_conf_key` for a DATE key. A set value that is not a real ISO date is a REFUSAL, never OFF
    and never armed (closing review F10; round 2 R7 and R11): every cutoff this file reads is armed
    by a string comparison, so `2026-9-8` reports the join as set while grading nothing, and
    `2026-13-45` has the shape and no day. ONE helper for EVERY cutoff key, because F10 gated the
    instance and left SPEC_LEGLINE_CUTOFF standing. Returns None on the refusal, after printing it.
    """
    value = read_conf_key(root, key)
    if not value:
        return value
    try:
        if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value):
            raise ValueError(value)
        datetime.date.fromisoformat(value)
    except ValueError:
        print(f"spec-tokens: REFUSING — {key} {value} is not an ISO date (YYYY-MM-DD), so "
              "neither the relation nor the arming comparison can read it and the join would report "
              "as set while grading nothing")
        return None
    return value


def check_path_shaped(tok, files):
    """A path this join can resolve. The pre-wiring run over the live corpus produced every one of
    these exclusions as a near-miss, and each would otherwise red an innocent spec.

    A GLOB is a population, not a path — `tools/*/kit.toml` names a set and `git ls-files` will never
    hold it. A `path:line` token belongs to the citation join, which grades the line number too;
    grading it here reports the whole token as an untracked path, which is both wrong and confusing.
    A trailing `/` or `.` is prose about path normalisation, not a path.
    """
    if NOT_A_TOKEN.match(tok) or " " in tok:
        return False
    if "*" in tok or "?" in tok:
        return False
    if CITE_TAIL.search(tok):
        return False
    if tok.rstrip("/.") != tok:
        return False
    return ("/" in tok and "." in tok.rsplit("/", 1)[1]) or tok in files


def scan_claims(text):
    """The claims join over one spec's text (TOOL-dGatedProse-2). Returns `(runs, hits, clears)`:
    `runs` counts the distinct matched runs, each hit is `(line, object, class, arms, cite)` and each
    clear is `(line, object, arms, why)`, where `arms` names every arm that reached the object's run,
    so a run two arms reach is ONE run carrying both. Fenced blocks are blanked line for line first,
    by the same line-level toggle the hygiene engine reads a spec with, so a spec may exhibit the
    refused sentence as a worked example and every line number still holds.
    """
    lines, inside = [], False
    for ln in text.split("\n"):
        fence = ln.lstrip().startswith("```")
        lines.append("" if inside or fence else ln)
        inside = inside != fence
    body = "\n".join(lines)
    starts = [m.start() for m in TICK.finditer(body)]
    found = {}
    for name, arm in CLAIM_ARMS:
        for s in starts:
            m = arm.match(body, s)
            if m:
                found.setdefault(m.span("run"), set()).add(name)
    # A passive or fronted arm matched at a token INSIDE a chain yields a tail of the run it already
    # matched from the chain's head; the tail's arms fold into the run that contains it.
    runs = {}
    for span in sorted(found, key=lambda sp: (sp[0], -sp[1])):
        outer = next((o for o in runs if o[0] <= span[0] and span[1] <= o[1]), None)
        runs.setdefault(outer or span, set()).update(found[span])
    hits, clears = [], []
    for (a, b), names in sorted(runs.items()):
        arms = tuple(n for n, _ in CLAIM_ARMS if n in names)
        for om in TICK.finditer(body, a, b):
            obj, line = om.group(1), body.count("\n", 0, om.start()) + 1
            row = next((r for r in CLAIM_REFUSALS if r[1].search(obj)), None)
            if row and row[0]:
                hits.append((line, obj, row[0], arms, row[2]))
            else:
                clears.append((line, obj, arms, row[2] if row else "cleared: no path, glob or "
                               "code-symbol shape"))
    return len(runs), hits, clears


def check_claim_canary():
    """Assert `CLAIM_CANARY` STRUCTURALLY (TOOL-dGatedProse-2, S3). Returns None when it holds, else
    the first failure as a sentence: every arm is the designated arm of a refused entry, every class
    appears, a clearing entry exists, no entry spells its verb in lowercase, and each entry's scan
    carries its designated arm and its expected verdict. An arm added without an entry refuses here,
    at startup, and so does a dead arm, a lost case fold or a lost space clause.
    """
    arms = [n for n, _ in CLAIM_ARMS]
    refused = [e for e in CLAIM_CANARY if e[2]]
    for n in arms:
        if not any(e[1] == n for e in refused):
            return f"arm {n!r} is the designated arm of no refused entry"
    for cls in (r[0] for r in CLAIM_REFUSALS if r[0]):
        if not any(e[2] == cls for e in refused):
            return f"class {cls!r} appears in no refused entry"
    if len(refused) == len(CLAIM_CANARY):
        return "no entry must clear, so nothing pins the space clause"
    for sentence, arm, cls in CLAIM_CANARY:
        if arm not in arms:
            return f"entry {sentence!r} names {arm!r}, which is not an arm"
        if re.search(r"claim", sentence):
            return f"entry {sentence!r} spells its verb in lowercase, so the case fold is not load-bearing"
        _, hits, clears = scan_claims(sentence)
        if cls:
            if len(hits) != 1 or hits[0][2] != cls or arm not in hits[0][3]:
                return (f"entry {sentence!r} expected one {cls} hit through arm {arm!r}, got "
                        f"{[(h[1], h[2], h[3]) for h in hits]}")
        elif hits or not any(arm in c[2] for c in clears):
            return (f"entry {sentence!r} expected to clear through arm {arm!r}, got hits "
                    f"{[(h[1], h[2]) for h in hits]} and clears {[(c[1], c[2]) for c in clears]}")
    return None


def read_waivers(root):
    p = root / WAIVERS
    if not p.exists():
        return None
    rows = {}
    for line in p.read_bytes().decode("utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        tok, _, why = line.partition("\t")
        rows[tok.strip()] = why.strip()
    return rows


def main(argv):
    listing = "--list" in argv
    root = pathlib.Path(run("git", "rev-parse", "--show-toplevel").strip())
    if not root.name:
        print("spec-tokens: not a git repo")
        return 2

    files = read_tracked(root)
    allspecs = sorted(f for f in files
                      if re.match(r"memory/builds/[^/]+/spec/.*\.md$", f))
    specs, frozen = [], 0
    for f in allspecs:
        if LIVE.search((root / f).read_bytes().decode("utf-8", "replace")):
            specs.append(f)
        else:
            frozen += 1
    if not specs:
        print("spec-tokens: REFUSING — no tracked spec matched "
              f"{SPEC_GLOB}; a lint that graded nothing reports the same zero as a clean tree")
        return 1

    legs_path = root / LEGS
    if not legs_path.exists():
        print(f"spec-tokens: REFUSING — {LEGS} is missing, so the leg join cannot run")
        return 1
    try:
        rows = json.loads(legs_path.read_bytes().decode("utf-8"))
        legs = {r["name"] for r in rows}
        guarded, broad = derive_guarded_legs(rows)
    except Exception as exc:  # noqa: BLE001 - a malformed manifest is a refusal, not a pass
        print(f"spec-tokens: REFUSING — {LEGS} did not parse: {exc}")
        return 1
    if not legs:
        print(f"spec-tokens: REFUSING — {LEGS} declares no leg")
        return 1

    waivers = read_waivers(root)
    if waivers is None:
        print(f"spec-tokens: REFUSING — {WAIVERS} is absent; a registry nobody created is a "
              "decision nobody made")
        return 1

    legline_cut = read_cutoff_key(root, LEGLINE_KEY)
    direct_cut = read_cutoff_key(root, DIRECT_KEY)
    guards_cut = read_cutoff_key(root, GUARDS_KEY)
    if legline_cut is None or direct_cut is None or guards_cut is None:
        return 1
    relation = check_cutoff_relation(root, DIRECT_KEY, direct_cut) if direct_cut else ""
    grelation = check_cutoff_relation(root, GUARDS_KEY, guards_cut) if guards_cut else ""
    if relation is None or grelation is None:
        return 1
    # The claims join's LIVENESS ASSERTION, before the population loop: an entry that does not hold
    # means an arm, the case fold or the space clause is broken, and the loop's zero would then be
    # indistinguishable from a clean corpus.
    canary = check_claim_canary()
    if canary:
        print(f"spec-tokens: REFUSING — CLAIM_CANARY does not hold: {canary}; the claims join would "
              "report a broken arm as a clean corpus")
        return 1
    hits, skipped, graded, seen_waived = [], 0, 0, set()
    ungraded, noheading = 0, 0
    bar_examined, bar_specs, bar_carriers, near = 0, 0, 0, []
    g_examined, g_specs, g_carriers, g_nosubhead, g_nogates = 0, 0, 0, 0, 0
    c_runs, c_specs, c_cleared = 0, 0, 0
    for f in specs:
        text = (root / f).read_bytes().decode("utf-8", "replace")
        m = SPEC_DATE.search("/" + f)
        armed = bool(direct_cut) and bool(m) and m.group(1) >= direct_cut
        g_armed = bool(guards_cut) and bool(m) and m.group(1) >= guards_cut
        named = set()                 # the manifest names the leg line contributes
        pop_toks, bar_toks = [], []   # every graded-population token · the BAR matches among them
        gates = extract_gates(text)
        if gates is None:
            # No Gates heading at all. Silent by design, and counted apart from the section that
            # exists and contributes nothing: the two silences have different remedies, so a single
            # "ungraded" number would tell a reader to fix the wrong half.
            noheading += 1
            gates = ""
        contributed = 0
        for line in gates.splitlines():
            if not LEG_LINE.match(line):
                continue
            for tok in TICK.findall(line):
                pop_toks.append(tok)
                # The bar test runs FIRST, on the raw token. NOT_A_TOKEN drops a `GATE_` prefix and
                # NOT_A_LEG a `bash ` opener or a slash, and the motivating instruction carries all
                # three; a bar token was never a leg, so it contributes nothing and continues.
                if BAR.search(tok):
                    bar_toks.append(tok)
                    continue
                if NOT_A_TOKEN.match(tok):
                    continue
                # A token that IS a manifest name resolves BEFORE the shape exclusions. Those
                # exclusions exist to drop commands, conf keys and graded files out of the join, and
                # they were written against tokens that are none of them — but a real leg name
                # carrying a `/`, or opening with a command verb, was being discarded UNREAD, so a
                # correct §7 contributed nothing and the spec looked like prose.
                if tok not in legs and NOT_A_LEG.search(tok):
                    continue
                graded += 1
                contributed += 1
                if tok not in legs:
                    hits.append((f, "leg", tok, f"not a name in {LEGS}"))
                else:
                    named.add(tok)
        if not contributed and extract_gates(text) is not None:
            ungraded += 1
            if legline_cut:
                m = SPEC_DATE.search("/" + f)
                if m and m.group(1) >= legline_cut:
                    hits.append((f, "legline", f,
                                 "section 7 carries a Gates heading and contributes no leg name, "
                                 f"required at/after {LEGLINE_KEY} {legline_cut}"))
        for bullet in re.findall(r"^- .*(?:\n  .*)*", extract_acceptance(text) or "", re.M):
            for tok in TICK.findall(bullet):
                pop_toks.append(tok)
                # First here too, and the paths join still runs over the token's words: a tracked
                # runner path resolves either way, and the two joins answer different questions.
                if BAR.search(tok):
                    bar_toks.append(tok)
                for word in tok.split():
                    if not check_path_shaped(word, files):
                        continue
                    graded += 1
                    if word not in files:
                        hits.append((f, "path", word, "not tracked by git ls-files"))
        if armed:
            bar_specs += 1
            bar_examined += len(pop_toks)
            hits += [(f, "bar", tok, BAR_WHY) for tok in bar_toks]
        elif bar_toks:
            # Not graded, but COUNTED and listed: a skip that does not announce its size is
            # indistinguishable from coverage, and the OFF state hides the most.
            bar_carriers += 1
            where = f"predates {DIRECT_KEY} {direct_cut}" if direct_cut else f"{DIRECT_KEY} blank (arm off)"
            near += [(f, "bar", tok, where) for tok in bar_toks]
        graded_set = set(pop_toks)
        near += [(f, "bar", tok, "outside the graded population")
                 for tok in TICK.findall(text) if BAR.search(tok) and tok not in graded_set]
        # THE GUARDS JOIN (TOOL-aBlindedTrial-8): the declared write set against every guarded leg.
        # One hit per MISSING leg, its token naming the first declared path that trips it — the
        # composite keeps a `[leg]` waiver row keyed on the bare leg name from swallowing it.
        touched = extract_files_touched(text, files)
        if touched is None:
            g_nosubhead += 1
            touched = ([], [])
        declared, roots = touched
        # A one-segment ROOT under the sub-head declares nothing (round 2, R1), and says so.
        near += [(f, "guards", p, "a one-segment root declares nothing, not joined - name the files or "
                                  "a directory of two or more segments") for p in roots]
        missing = []
        # The legline arm's precondition, mirrored (R4): a spec with NO Gates heading is the light
        # profile's legal shape and is not joined — counted, NOT examined, and every path it declares
        # that would have tripped a joined guard is named as NEAR, so the skip has a size and a name
        # (round 2, R8).
        if declared and extract_gates(text) is None:
            g_nogates += 1
            near += [(f, "guards", p, "no Gates heading, not joined") for p in declared
                     if any(check_guard_trips(p, g) for _, gs in guarded for g in gs)]
        elif extract_gates(text) is not None:
            if g_armed:
                g_specs += 1
                g_examined += len(declared)
            for leg, gs in guarded:
                if leg in named:
                    continue
                path = next((p for p in declared if any(check_guard_trips(p, g) for g in gs)), None)
                if path is not None:
                    missing.append((leg, path))
        if g_armed:
            hits += [(f, "guards", f"{leg} <- {path}",
                      f"§4 files-touched names {path}, which trips the guard of leg {leg!r}, "
                      "absent from the §7 leg line") for leg, path in missing]
        elif missing:
            g_carriers += 1
            where = f"predates {GUARDS_KEY} {guards_cut}" if guards_cut else f"{GUARDS_KEY} blank (arm off)"
            near += [(f, "guards", f"{leg} <- {path}", where) for leg, path in missing]
        # A path whose only guard matches are BROAD is EXCLUDED, and says so under --list, count and all.
        for p in declared:
            if any(check_guard_trips(p, g) for _, gs in guarded for g in gs):
                continue
            hit = [g for g in broad if check_guard_trips(p, g)]
            if hit:
                near.append((f, "guards", p, "matches only the broad guard(s) "
                             + " ".join(f"{g} ({broad[g]} legs)" for g in hit)
                             + ", excluded from the join"))
        for path, line in CITE.findall(text):
            if path not in files:
                skipped += 1
                continue
            graded += 1
            n = len((root / path).read_bytes().decode("utf-8", "replace").splitlines())
            if int(line) > n:
                hits.append((f, "cite", f"{path}:{line}", f"file has {n} lines"))
        # THE CLAIMS JOIN (TOOL-dGatedProse-2): every live spec, and no cutoff (owner, 2026-09-21).
        runs, c_hits, c_clears = scan_claims(text)
        c_runs += runs
        c_specs += 1 if runs else 0
        c_cleared += len(c_clears)
        hits += [(f, "claims", obj, f"{cls} at line {line}, arm(s) {'+'.join(arms)} — "
                  + CLAIMS_WHY.format(cls=cls, cite=cite)) for line, obj, cls, arms, cite in c_hits]
        near += [(f, "claims", obj, f"line {line}, arm(s) {'+'.join(arms)} — {why}")
                 for line, obj, arms, why in c_clears]

    live = [h for h in hits if h[2] not in waivers]
    for h in hits:
        if h[2] in waivers:
            seen_waived.add(h[2])

    stale = []
    for tok, why in waivers.items():
        if not why:
            stale.append((tok, "carries no reason"))
        elif tok not in seen_waived:
            stale.append((tok, "no spec produces this hit any more"))

    if listing:
        for f, kind, tok, why in hits:
            print(f"spec-tokens: {'WAIVED' if tok in waivers else 'HIT   '} [{kind}] {f} :: {tok} — {why}")
        for f, kind, tok, where in near:
            print(f"spec-tokens: NEAR   [{kind}] {f} :: {tok} — {where}")

    print(f"spec-tokens: {len(specs)} live spec(s) · {frozen} terminal spec(s) not graded · "
          f"{graded} token(s) graded · {skipped} citation(s) skipped (untracked path) · "
          f"{len(waivers)} waiver(s)")
    # The bar join's own line, on every run: what it examined, and what it did NOT — the pre-cutoff
    # carriers it counted and skipped. On the landing day the examined figures read zero by the
    # register's own relation, and this line is what keeps that zero from reading as coverage.
    if direct_cut:
        print(f"spec-tokens: bar join · {bar_examined} token(s) examined in {bar_specs} live spec(s) "
              f"at/after {DIRECT_KEY} {direct_cut} · {bar_carriers} pre-cutoff live spec(s) carry one "
              f"and are not graded{relation}")
    else:
        print(f"spec-tokens: bar join · {DIRECT_KEY} blank (arm off) · {bar_carriers} live spec(s) "
              "carry a bar token")
    # The guards join's line, the same shape for the same reason: what it examined, what it counted
    # and skipped, how many specs declared nothing it could read or carried no Gates heading to join
    # against, and the guards the breadth floor excluded WITH their leg counts — the derived figure
    # that no prose restates (R1, R11).
    g_tail = (f" · {g_nosubhead} carry no Files touched sub-head · {g_nogates} declare a path and carry "
              f"no Gates heading, not joined · excluded as broad (carried by more than {BROAD_LEG_FLOOR} "
              f"legs): {render_broad(broad)}")
    if guards_cut:
        print(f"spec-tokens: guards join · {g_examined} declared path(s) examined in {g_specs} live "
              f"spec(s) at/after {GUARDS_KEY} {guards_cut} · {g_carriers} pre-cutoff live spec(s) carry "
              f"a missing guarded leg and are not graded{g_tail}{grelation}")
    else:
        print(f"spec-tokens: guards join · {GUARDS_KEY} blank (arm off) · {g_carriers} live spec(s) "
              f"carry a missing guarded leg{g_tail}")
    # The claims join's line, on EVERY run and on no branch: it has no key, and a zero is its normal
    # state, so this line is what keeps that zero from reading as coverage.
    print(f"spec-tokens: claims join · {c_runs} dossier-claim sentence(s) examined · {c_specs} live "
          f"spec(s) carry one · {c_cleared} object(s) cleared · canary held over {len(CLAIM_ARMS)} arm(s)")
    # THE UNGRADED POPULATION, which the report used to leave out entirely. A leg join that reads N
    # specs and grades a leg name in far fewer of them looks identical to one that graded them all
    # and found nothing wrong. These two numbers are what separate the cases, and they are kept
    # apart because they have different remedies: a section that exists and names no leg is an
    # author writing prose where the list goes, and no section at all is a Tier-1 spec exercising
    # the light profile, which is legal.
    print(f"spec-tokens: {ungraded} live spec(s) carry a Gates heading contributing NO leg name · "
          f"{noheading} carry no Gates heading to grade · "
          + (f"{LEGLINE_KEY} {legline_cut}" if legline_cut else f"{LEGLINE_KEY} blank (arm off)"))

    if listing:
        return 0
    for f, kind, tok, why in live:
        print(f"spec-tokens: {f} [{kind}] `{tok}` — {why}")
    for tok, why in stale:
        print(f"spec-tokens: STALE WAIVER `{tok}` — {why}")
    if live or stale:
        print(f"spec-tokens: {len(live)} unwaived hit(s), {len(stale)} stale waiver(s)")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
