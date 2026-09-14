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

REFUSALS, not passes. An empty spec population refuses: a lint that graded nothing reports the same
zero as a clean tree. An unreadable manifest refuses. A waiver row naming a path no spec cites, or
one the tree now tracks, refuses — a stale exception cannot hide a live hit. A cutoff the tree's own
history dates at or after itself refuses.

  python tools/check-spec-tokens.py            # assert; exit 1 on an unwaived hit
  python tools/check-spec-tokens.py --list     # every hit and near-miss, authoring aid, exit 0
"""
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
# or a chain separator, past optional VAR=value prefixes, `timeout N` and a bash/sh launcher — or a
# GATE_FULL= / GATE_SELFTESTS= assignment with a NON-EMPTY value anywhere in the token. A
# `path:line` citation fails the trailing lookahead and stays the cites join's; a grep over a suite
# FILE has grep at command position and is not a run; the empty assignment is the OFF spelling.
BAR = re.compile(
    r"(?:^|&&|[;|(])\s*(?:\w+=\S*\s+)*(?:timeout\s+\S+\s+)?(?:bash\s+|sh\s+)?(?:\S*/)?"
    r"(?:run-gates|run-selftests|run-unattended-gates|[^\s/*?]+\.test)\.sh(?=\s|$)"
    r"|(?:^|\s)GATE_(?:FULL|SELFTESTS)=\S")
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


def read_conf_key(root, key):
    """One key out of `.memory-tree.conf`, by plain assignment. Absent or blank means OFF."""
    p = root / ".memory-tree.conf"
    if not p.exists():
        return ""
    m = re.search(r'^%s="?([^"\n]*)"?\s*$' % re.escape(key),
                  p.read_bytes().decode("utf-8", "replace"), re.M)
    return m.group(1).strip() if m else ""


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

    legline_cut = read_conf_key(root, LEGLINE_KEY)
    direct_cut = read_conf_key(root, DIRECT_KEY)
    relation = ""
    if direct_cut:
        # THE RELATION, ASSERTED (TOOL-aDeferredBar-2, Date gate). The register's rule puts a new
        # cutoff strictly past the day it is set, so a value the tree's own history dates at or after
        # itself was carried across a day boundary instead of re-derived. It is compared to the
        # SETTING COMMIT's date and not to the newest spec date on the tree: from the day after
        # landing, that comparison refuses exactly the population the join exists to grade. A value
        # not yet in history cannot be checked and is announced, never refused or passed.
        set_on = run("git", "-C", str(root), "log", "-1", "--format=%cs",
                     f'-G^{DIRECT_KEY}="?{direct_cut}"?$', "--", ".memory-tree.conf").strip()
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
