#!/usr/bin/env python3
"""check-spec-tokens.py — a spec's machine-facing tokens resolve against the tree that owns them.

TOOL-dRetiredFork-20. Three spec-audit rounds over one build found the same class by hand every
time: a section 7 gate name that is not a leg (18 of 36 in one set), a section 6 criterion whose
witness path is not tracked, and a `path:line` citation four lines short. Each is a JOIN over two
tracked files, and hand-verifying them is what this replaces.

WHAT IT DOES NOT CHECK, stated here because a structural check reads as a semantic one to everybody
who did not write it. It resolves EXISTENCE and RANGE. It does not read the cited line and does not
know whether it says what the spec claims; a citation naming a real line that argues the opposite
passes. It does not grade prose, scope, acceptance or tier. The bar join reads an INVOCATION as a
spec spells it inside backticks, and nothing else: it cannot see a path built at runtime,
a runner spelled inside a sh -c string,
a suite run written as the body of a fenced block,
or a suite named in prose.
Each of those is the ACT, and the act is refused by the hook of TOOL-aDeferredBar-3, not here.

THE JOINS KEEP THEIR POPULATIONS APART, the correction rev-2 folded from round 3. The fourth join,
`bar`, reads two of the three rather than minting a fourth.

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
  handoff a `**hands-off**` bullet's backticked PAYLOAD, in the `### Edges` block of a LIVE spec
         dated at or after SPEC_HANDOFF_CUTOFF (`.memory-tree.conf`, blank = off) -> the text of
         the sibling spec the bullet names, joined by the uid each spec's own H1 carries, inside
         the one build (TOOL-dDerivedDocket-37). The bullet promises a named sibling a flag, a key,
         a file or a placeholder, and nothing checked that the sibling names it: three spec-audit
         rounds over one build found the class by hand every time, and a probe run after the fold
         found three more. TWO LIMITS, stated here because neither is guessable from a green row.
         It proves the sibling NAMES the token, never that it DOES the work the bullet describes —
         a sibling mentioning it in passing passes. And `**consumes-from**` bullets are NOT graded:
         measured over that build, grading them produced twelve misses and no true one, each an
         argument variant of a command the producer does name or a consumer naming its own file.
         ABSENCE IS NOT DISAGREEMENT, check 12's own rule: a bullet whose target names no live spec
         in its build is handing to a terminal or Tier-1 sibling, both legitimate, so it is SKIPPED
         AND COUNTED like the citation arm's untracked half, and the count rides every run.

REFUSALS, not passes. An empty spec population refuses: a lint that graded nothing reports the same
zero as a clean tree. An unreadable manifest refuses. A waiver row naming a path no spec cites, or
one the tree now tracks, refuses — a stale exception cannot hide a live hit. A cutoff the tree's own
history dates at or after itself refuses, and so does EVERY cutoff key this file reads whose value
is not a real ISO date, SPEC_LEGLINE_CUTOFF included: the comparisons are string comparisons, and a
malformed value would report the join as set while it graded nothing.

  python tools/check-spec-tokens.py            # assert; exit 1 on an unwaived hit
  python tools/check-spec-tokens.py --list     # every hit and near-miss, authoring aid, exit 0
"""
import datetime
import json
import pathlib
import re
import subprocess
import sys

KIT_SPEC_TOKENS_VERSION = "1.0"  # gov:kit spec-tokens@1.0 — the deployer's read

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
# TOOL-dDerivedDocket-37: the hands-off join's key, grammar and refusal. The GRAMMAR IS CHECK 12'S,
# copied rather than called: the hygiene engine is a copy-installed kit, so an arm there would reach
# every memory-tree adopter's bar, a shipped surface this unit did not price. Check 12's own lines,
# cited so a reader can compare them: the uid at
# tools/memory-tree/check-memory-hygiene.sh:1533-1534, Non-goals and Edges by heading text at :1547
# and :1549, the marker at :1553, the verb at :1557 and the backticked-or-bare target at :1564-1565.
HANDOFF_KEY = "SPEC_HANDOFF_CUTOFF"
# ONE rule here is WIDER than check 12's, which reads a bullet's first line only: this reads the
# two-space continuation lines too, the shape the acceptance-bullet loop below already uses. A
# payload wrapped past the house width is still the bullet's promise, and reading only line one
# would leave every wrapped token ungraded and silent.
HANDOFF_BULLET = re.compile(r"^(?:-|\*)[ \t]+\*\*hands-off\*\*[ \t].*(?:\n  .*)*", re.M)
# `## <n>. Non-goals` by HEADING TEXT and never by ordinal, the read GATES_HEAD and AC_HEAD already
# have. No end anchor, because the house heading is `## 3. Non-goals (OUT)`.
NONGOALS_HEAD = re.compile(r"^## [0-9]+[.] Non-goals[^\n]*$", re.M)
# The uid a spec's H1 carries. BOTH halves of a handoff key are read from this and never from a
# filename: a spec may legally be family-less, carry a record tail or sit in a sub-folder of
# `spec/`, and its filename then says nothing about the unit it specs.
SPEC_UID = re.compile(r"^# ([A-Z][A-Za-z0-9-]*) ", re.M)
# A unit id is this join's SUBJECT, not its payload. The target is dropped by identity; every other
# id in the bullet is context — a sibling unit, a prior decision — and grading one would demand that
# every spec a bullet mentions names the unit mentioning it.
UNIT_ID = re.compile(r"^[A-Z][A-Za-z0-9]*-[A-Za-z]+-[0-9]+$")
HANDOFF_WHY = ("this bullet hands the token to that sibling and the sibling's own spec never names "
               "it: name it there, or correct the bullet — the join proves the sibling NAMES the "
               "token, never that it does the work")


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


def read_spec_uids(root, specs):
    """`(build, uid)` -> the live spec files whose H1 line carries that uid.

    TOOL-dDerivedDocket-37. Both halves of a handoff key are read HERE and never from a filename: a
    spec may legally be family-less, carry a record tail or sit in a sub-folder of `spec/`, so its
    filename says nothing about the unit it specs. Keyed per BUILD, because a uid is unique inside
    its build and nowhere else. One uid may map to several files; measured over 649 tracked specs no
    build had two, and keeping the list is what makes that a measurement rather than an assumption.
    """
    uids = {}
    for f in specs:
        m = SPEC_UID.search((root / f).read_bytes().decode("utf-8", "replace"))
        if m:
            uids.setdefault((f.split("/")[2], m.group(1)), []).append(f)
    return uids


def scan_handoffs(root, specs, uids, cutoff):
    """Every `**hands-off**` bullet's backticked payload -> the text of the sibling it names.

    TOOL-dDerivedDocket-37. Returns `(hits, bullets graded, payload tokens, silent bullets)`. A
    blank cutoff is the OFF spelling and grades nothing, which the report line says out loud.

    THE SILENT COUNT IS THE HONEST HALF. A bullet whose target names no live spec in its own build
    is handing to a terminal or a Tier-1 sibling, and a bullet in a source whose H1 carries no uid
    has no key to report a hit under; both are legitimate, both are skipped, and a skip that does
    not announce its size is indistinguishable from coverage. A bullet naming `external` has no
    sibling to join at all and is not read.
    """
    hits, bullets, tokens, silent = [], 0, 0, 0
    if not cutoff:
        return hits, bullets, tokens, silent
    # One read per file, kept flat rather than behind a nested helper: a nested `def` is a function
    # the naming gate grades and §4 Inventory of TOOL-dDerivedDocket-37 declares exactly two.
    cache = {}
    for f in specs:
        m = SPEC_DATE.search("/" + f)
        if not m or m.group(1) < cutoff:
            continue
        if f not in cache:
            cache[f] = (root / f).read_bytes().decode("utf-8", "replace")
        text = cache[f]
        head = NONGOALS_HEAD.search(text)
        if not head:
            continue
        rest = text[head.end():]
        nxt = re.search(r"^## ", rest, re.M)
        nongoals = rest[:nxt.start()] if nxt else rest
        sub = re.search(r"^### Edges[ \t]*$", nongoals, re.M)
        if not sub:
            continue
        rest = nongoals[sub.end():]
        nxt = re.search(r"^### ", rest, re.M)
        edges = rest[:nxt.start()] if nxt else rest
        uid = SPEC_UID.search(text)
        source = uid.group(1) if uid else ""
        build = f.split("/")[2]
        for bullet in HANDOFF_BULLET.findall(edges):
            # Check 12's target rule, on the payload past the marker and the verb: the first
            # backticked token when the payload opens with one, else its leading word run. Stripping
            # the MARKER here as well as the verb is what keeps a `*`-and-tab bullet readable.
            payload = re.sub(r"^(?:-|\*)[ \t]*\*\*[^*]*\*\*[ \t]*", "", bullet.split("\n", 1)[0])
            if payload.startswith("`"):
                target = payload[1:].partition("`")[0]
            else:
                target = re.match(r"[A-Za-z0-9_-]*", payload).group(0)
            if target == "external":
                continue
            if not source or (build, target) not in uids:
                silent += 1
                continue
            bullets += 1
            parts = []
            for g in uids[(build, target)]:
                if g not in cache:
                    cache[g] = (root / g).read_bytes().decode("utf-8", "replace")
                parts.append(cache[g])
            sibling = "\n".join(parts)
            for tok in TICK.findall(bullet):
                if tok == target or UNIT_ID.match(tok) or NOT_A_TOKEN.match(tok):
                    continue
                tokens += 1
                if tok not in sibling:
                    hits.append((f, "handoff", f"{source}>{target}:{tok}", HANDOFF_WHY))
    return hits, bullets, tokens, silent


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
        legs = {r["name"] for r in json.loads(legs_path.read_bytes().decode("utf-8"))}
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
    handoff_cut = read_cutoff_key(root, HANDOFF_KEY)
    if legline_cut is None or direct_cut is None or handoff_cut is None:
        return 1
    relation = ""
    if direct_cut:
        # THE RELATION, ASSERTED (TOOL-aDeferredBar-2, Date gate). The register's rule puts a new
        # cutoff strictly past the day it is set, so a value the tree's own history dates at or after
        # itself was carried across a day boundary instead of re-derived. It is compared to the
        # SETTING COMMIT's date and not to the newest spec date on the tree: from the day after
        # landing, that comparison refuses exactly the population the join exists to grade. A value
        # not yet in history cannot be checked and is announced, never refused or passed.
        # PICKAXE `-S`, NOT `-G` (closing review F4): `-G` matches any hunk that adds OR removes the
        # line, so a block move, a requote or a whitespace cleanup re-dated the "setting commit" to
        # that later day and the gate refused a value nobody re-set. `-S` matches a change in the
        # line's OCCURRENCE COUNT, which a move or a requote leaves at one.
        q = subprocess.run(["git", "-C", str(root), "log", "-1", "--format=%cs", "--pickaxe-regex",
                            f'-S^{DIRECT_KEY}="?{direct_cut}"?$', "--", ".memory-tree.conf"],
                           capture_output=True, text=True)
        if q.returncode:
            # A delegate whose status is discarded reads a query that never ran as "not yet
            # committed" — the announced skip with the wrong reason, which the next reader trusts.
            print(f"spec-tokens: REFUSING — the history query for {DIRECT_KEY} {direct_cut} failed, "
                  f"so the relation cannot be asserted: {q.stderr.strip() or 'git exited ' + str(q.returncode)}")
            return 1
        set_on = q.stdout.strip()
        if not set_on:
            relation = " · relation unchecked: value not yet committed"
        elif direct_cut <= set_on:
            print(f"spec-tokens: REFUSING — {DIRECT_KEY} {direct_cut} is not strictly past {set_on}, "
                  "the day the value was committed; the register's rule is the day AFTER the later "
                  "of the newest spec filename date on any ref and the setting commit's own date")
            return 1
    hits, skipped, graded, seen_waived = [], 0, 0, set()
    ungraded, noheading = 0, 0
    bar_examined, bar_specs, bar_carriers, near = 0, 0, 0, []
    for f in specs:
        text = (root / f).read_bytes().decode("utf-8", "replace")
        m = SPEC_DATE.search("/" + f)
        armed = bool(direct_cut) and bool(m) and m.group(1) >= direct_cut
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
            near += [(f, tok, where) for tok in bar_toks]
        graded_set = set(pop_toks)
        near += [(f, tok, "outside the graded population")
                 for tok in TICK.findall(text) if BAR.search(tok) and tok not in graded_set]
        for path, line in CITE.findall(text):
            if path not in files:
                skipped += 1
                continue
            graded += 1
            n = len((root / path).read_bytes().decode("utf-8", "replace").splitlines())
            if int(line) > n:
                hits.append((f, "cite", f"{path}:{line}", f"file has {n} lines"))

    # The fifth join, over a population the four above never build: one uid map over the live specs,
    # then one read per graded target. It is folded into `hits` before the waiver pass, so a handoff
    # hit takes a row of the same registry and a stale row naming one reds like any other.
    ho_uids = read_spec_uids(root, specs) if handoff_cut else {}
    ho_hits, ho_bullets, ho_tokens, ho_silent = scan_handoffs(root, specs, ho_uids, handoff_cut)
    hits += ho_hits

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
        for f, tok, where in near:
            print(f"spec-tokens: NEAR   [bar] {f} :: {tok} — {where}")

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
    # THE UNGRADED POPULATION, which the report used to leave out entirely. A leg join that reads N
    # specs and grades a leg name in far fewer of them looks identical to one that graded them all
    # and found nothing wrong. These two numbers are what separate the cases, and they are kept
    # apart because they have different remedies: a section that exists and names no leg is an
    # author writing prose where the list goes, and no section at all is a Tier-1 spec exercising
    # the light profile, which is legal.
    print(f"spec-tokens: {ungraded} live spec(s) carry a Gates heading contributing NO leg name · "
          f"{noheading} carry no Gates heading to grade · "
          + (f"{LEGLINE_KEY} {legline_cut}" if legline_cut else f"{LEGLINE_KEY} blank (arm off)"))
    # The hands-off join's line, ONE shape whether the arm is on or off, because "every run prints
    # it" is what stops a green run over zero bullets passing for a graded one — and the OFF state
    # is exactly when a reader most needs the zero spelled out. Its `live spec(s) ·` is deliberate:
    # `--dispatch` drops the report lines from its refusal diagnosis by that text, so this line
    # cannot crowd a real hit out of the three lines it prints.
    print(f"spec-tokens: hands-off join · {ho_bullets} bullet(s) graded in live spec(s) · "
          f"{ho_tokens} payload token(s) · {ho_silent} silent (no live target in the build, or no "
          f"source uid) · {HANDOFF_KEY} "
          + (handoff_cut if handoff_cut else "blank (arm off)"))

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
