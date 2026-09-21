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
`bar`, reads two of the three rather than minting a fourth; the fifth, `guards`, reads the legs
population plus one of its own, the declared write set.

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
         `<leg> <- <path>` (TOOL-aBlindedTrial-8). ONE-SEGMENT guards (`tools/`, `memory/`) are
         EXCLUDED from the join and listed by --list as NEAR: eleven legs guard bare `tools/`, so
         naming them adds no information and buries the specific one. A leg without a `guard` key
         is not joined; a spec without the sub-head declares nothing and is counted apart. The
         join reads the ESTIMATE as written, not the write set the build actually made; it reads
         no path named in prose outside the sub-head; and it reads a guard as a directory or an
         exact file, never as git pathspec magic. The motivating case: a unit that edited
         `tools/hooks/scratch-guard.js` and omitted `scratch-guard self-test`, found by a closing
         review and not by a gate.

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
    """The declared write set: every path-shaped word inside backticks under the `### Files touched`
    sub-head, in order and without repeats. None when the spec carries no such sub-head, which the
    report counts apart from a sub-head declaring nothing (TOOL-aBlindedTrial-8). The body closes at
    the next heading of ANY depth, unlike the section readers above, because the sub-head has
    siblings inside section 4.
    """
    m = FILES_HEAD.search(text)
    if not m:
        return None
    rest = text[m.end():]
    nxt = re.search(r"^##+ ", rest, re.M)
    body = rest[:nxt.start()] if nxt else rest
    paths = []
    for tok in TICK.findall(body):
        for word in tok.split():
            if check_path_shaped(word, files) and word not in paths:
                paths.append(word)
    return paths


def check_guard_trips(path, guard):
    """Git-pathspec semantics for a manifest guard: the exact path, or anything under it as a
    directory. Never a bare prefix, so `tools/x.sh` does not trip on `tools/x.sh.bak`."""
    return path == guard or path.startswith(guard.rstrip("/") + "/")


def derive_guarded_legs(rows):
    """The manifest's guarded legs, split by guard depth. Returns `(joined, broad)`: `joined` is
    `(name, [guards])` for every leg carrying at least one guard deeper than one segment, with the
    one-segment guards dropped from its list; `broad` is the sorted set of one-segment guards over
    the whole manifest, which the join excludes and --list reports as NEAR. A leg with no `guard`
    key is absent from both (fixture manifests omit it)."""
    joined, broad = [], set()
    for r in rows:
        deep = []
        for g in r.get("guard") or []:
            if g.rstrip("/").count("/") == 0:
                broad.add(g)
            else:
                deep.append(g)
        if deep:
            joined.append((r["name"], deep))
    return joined, sorted(broad)


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
    hits, skipped, graded, seen_waived = [], 0, 0, set()
    ungraded, noheading = 0, 0
    bar_examined, bar_specs, bar_carriers, near = 0, 0, 0, []
    g_examined, g_specs, g_carriers, g_nosubhead = 0, 0, 0, 0
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
        declared = extract_files_touched(text, files)
        if declared is None:
            g_nosubhead += 1
            declared = []
        missing = []
        for leg, gs in guarded:
            if leg in named:
                continue
            path = next((p for p in declared if any(check_guard_trips(p, g) for g in gs)), None)
            if path is not None:
                missing.append((leg, path))
        if g_armed:
            g_specs += 1
            g_examined += len(declared)
            hits += [(f, "guards", f"{leg} <- {path}",
                      f"§4 files-touched names {path}, which trips the guard of leg {leg!r}, "
                      "absent from the §7 leg line") for leg, path in missing]
        elif missing:
            g_carriers += 1
            where = f"predates {GUARDS_KEY} {guards_cut}" if guards_cut else f"{GUARDS_KEY} blank (arm off)"
            near += [(f, "guards", f"{leg} <- {path}", where) for leg, path in missing]
        # A path whose only guard matches are one-segment is EXCLUDED, and says so under --list.
        for p in declared:
            if any(check_guard_trips(p, g) for _, gs in guarded for g in gs):
                continue
            hit = [g for g in broad if check_guard_trips(p, g)]
            if hit:
                near.append((f, "guards", p, "matches only the one-segment guard(s) "
                             + " ".join(hit) + ", excluded from the join"))
        for path, line in CITE.findall(text):
            if path not in files:
                skipped += 1
                continue
            graded += 1
            n = len((root / path).read_bytes().decode("utf-8", "replace").splitlines())
            if int(line) > n:
                hits.append((f, "cite", f"{path}:{line}", f"file has {n} lines"))

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
    # and skipped, and how many specs declared nothing it could read.
    if guards_cut:
        print(f"spec-tokens: guards join · {g_examined} declared path(s) examined in {g_specs} live "
              f"spec(s) at/after {GUARDS_KEY} {guards_cut} · {g_carriers} pre-cutoff live spec(s) carry "
              f"a missing guarded leg and are not graded · {g_nosubhead} carry no Files touched "
              f"sub-head{grelation}")
    else:
        print(f"spec-tokens: guards join · {GUARDS_KEY} blank (arm off) · {g_carriers} live spec(s) "
              f"carry a missing guarded leg · {g_nosubhead} carry no Files touched sub-head")
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
