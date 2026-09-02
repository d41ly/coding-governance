#!/usr/bin/env python3
"""check-spec-tokens.py — a spec's machine-facing tokens resolve against the tree that owns them.

TOOL-dRetiredFork-20. Three spec-audit rounds over one build found the same class by hand every
time: a section 7 gate name that is not a leg (18 of 36 in one set), a section 6 criterion whose
witness path is not tracked, and a `path:line` citation four lines short. Each is a JOIN over two
tracked files, and hand-verifying them is what this replaces.

WHAT IT DOES NOT CHECK, stated here because a structural check reads as a semantic one to everybody
who did not write it. It resolves EXISTENCE and RANGE. It does not read the cited line and does not
know whether it says what the spec claims; a citation naming a real line that argues the opposite
passes. It does not grade prose, scope, acceptance or tier.

THE THREE JOINS HAVE THREE POPULATIONS, and that is the correction rev-2 folded from round 3.

  legs   backticked tokens on a `## 7. Gates` LINE THAT IS THE LIST -> a `name` in the manifest.
         A section 7 line carrying prose is not graded: measured, that predicate produced 270
         hits of which 271 came from prose in one spec. The arm reports its graded count so a
         green row cannot be read as covering the prose it skipped.
  paths  every backticked PATH-SHAPED token inside a `## 6. Acceptance criteria` bullet ->
         `git ls-files`. Path-shaped is a slash AND an extension, or an exact tracked path
         (TOOL-dRetiredFork-20 F2). A bare word is prose and is not a path.
  cites  every backticked `<path>:<line>` -> that file's line count, SCOPED to citations whose path
         is TRACKED. Measured at b0108f13: 453 specs carry 1721 citations and 854 of them name an
         untracked path, because the house style cites a kit file by basename (`run-gates.sh:407`).
         Redding those is 854 dispositions and this lint never lands; passing them silently is a
         could-not-fail arm over half the corpus. So they are SKIPPED AND COUNTED, and the count is
         printed on every run — a skip that does not announce itself is indistinguishable from
         coverage.

REFUSALS, not passes. An empty spec population refuses: a lint that graded nothing reports the same
zero as a clean tree. An unreadable manifest refuses. A waiver row naming a path no spec cites, or
one the tree now tracks, refuses — a stale exception cannot hide a live hit.

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


def run(*args):
    return subprocess.run(args, capture_output=True, text=True).stdout


def tracked(root):
    return set(run("git", "-C", str(root), "ls-files").split())


def section(text, num):
    m = re.search(SEC % num, text, re.S | re.M)
    return m.group(1) if m else ""


def path_shaped(tok, files):
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

    files = tracked(root)
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

    hits, skipped, graded, seen_waived = [], 0, 0, set()
    for f in specs:
        text = (root / f).read_bytes().decode("utf-8", "replace")
        for line in section(text, 7).splitlines():
            if not LEG_LINE.match(line):
                continue
            for tok in TICK.findall(line):
                if NOT_A_TOKEN.match(tok) or NOT_A_LEG.search(tok):
                    continue
                graded += 1
                if tok not in legs:
                    hits.append((f, "leg", tok, f"not a name in {LEGS}"))
        for bullet in re.findall(r"^- .*(?:\n  .*)*", section(text, 6), re.M):
            for tok in TICK.findall(bullet):
                for word in tok.split():
                    if not path_shaped(word, files):
                        continue
                    graded += 1
                    if word not in files:
                        hits.append((f, "path", word, "not tracked by git ls-files"))
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

    print(f"spec-tokens: {len(specs)} live spec(s) · {frozen} terminal spec(s) not graded · "
          f"{graded} token(s) graded · {skipped} citation(s) skipped (untracked path) · "
          f"{len(waivers)} waiver(s)")

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
