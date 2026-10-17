# Research instruments: layers 1 to 4's Tier-2 rounds, compared

**Serves:** research PLAY-dClosedLoop-1

The instruments behind `build/2026-10-16-build-PLAY-dClosedLoop-1-layers-reviews-compared.md`, as fenced
text, since the lexicon gate grades every tracked Python file. They ran from the session scratchpad,
written here as `<the session scratchpad>`.

## [make-args] The args generator

It wrote all eight rounds' args. Run as `python make_args.py <the session scratchpad> <the worktree>`.

```python
"""Write the eight Tier-2 runs' args (layers 1 to 4, rounds A and B), shaped as the runtime runs' were.
Usage: python make_args.py <scratch-dir> <repo>"""
import json
import subprocess
import sys

SP, REPO = sys.argv[1], sys.argv[2]
B = "memory/builds/dClosedLoop/build/"
P = B + "2026-10-15-build-PLAY-dClosedLoop-1-"
V2 = B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"


def blob(path):
    return subprocess.run(["git", "rev-parse", f"HEAD:{path}"], capture_output=True, text=True, check=True).stdout.strip()


def tags(path):
    out = []
    for line in open(path, encoding="utf-8"):
        if line.startswith(("## [", "### [")):
            out.append(line.split("]")[0].split("[")[1])
    return out


LAYERS = [
    ("instruction", 1, "the instruction layer's design record", [P + "layer-instruction.md"],
     [V2, B + "2026-10-14-build-PLAY-dClosedLoop-1-foundations.md", P + "design-overview.md", P + "layer-roles.md",
      P + "layer-memory.md", P + "layer-runtime.md"], ""),
    ("flow", 2, "the flow layer's two design records, its layer review and its steps defined item by item",
     [P + "layer-flow.md", P + "flow-steps.md"],
     [V2, B + "2026-10-14-build-PLAY-dClosedLoop-1-flow.md", B + "2026-10-14-build-PLAY-dClosedLoop-1-flow-interactions.md",
      P + "flow-roles.md", P + "research-flow-items-a.md", P + "research-flow-items-b.md", P + "layer-instruction.md",
      P + "layer-runtime.md"],
     " The owner holds a revisit of this layer's relations to the other layers; a finding about those relations is "
     "still reported, as input to that revisit."),
    ("roles", 3, "the roles layer's design record", [P + "layer-roles.md"],
     [V2, B + "2026-10-14-build-PLAY-dClosedLoop-1-roles.md", P + "flow-roles.md", P + "flow-steps.md",
      B + "2026-10-14-build-PLAY-dClosedLoop-1-research-roles-anatomy.md",
      B + "2026-10-14-build-PLAY-dClosedLoop-1-research-roles-coverage.md",
      B + "2026-10-14-build-PLAY-dClosedLoop-1-research-roles-interactions.md",
      B + "2026-10-14-build-PLAY-dClosedLoop-1-research-roles-priorart.md", P + "layer-runtime.md"],
     " The owner holds a revisit of this layer's mechanical shape (the execution shape of each role item); a finding "
     "about it is still reported, as input to that revisit."),
    ("memory", 4, "the memory layer's design record", [P + "layer-memory.md"],
     [V2, P + "research-memory-builds.md", P + "research-memory-asks-decisions.md", P + "research-memory-map-reuse.md",
      P + "research-memory-annotations.md", P + "research-memory-tooling.md", P + "layer-roles.md", P + "lexicon.md",
      P + "layer-runtime.md"], ""),
]
BY_DESIGN = ("- The build is design-only: no product code and no unit specs; each chain build writes its own specs "
             "later, so unit-level implementation detail is absent by design.\n"
             "- The owner's settled answers, recorded in the record's answer sections, are decisions: a finding may show "
             "that one contradicts another record, the platform or the tree, but does not re-argue the owner's choice.\n"
             "- Records outside memory/builds/dClosedLoop/ are not under review, and the research returns are evidence, "
             "not subjects.")
checklist = open(f"{SP}/l14/cl_instruction.txt", encoding="utf-8").read()

index = []
for key, n, desc, subjects, specs, extra in LAYERS:
    tag_list = []
    for s in subjects:
        tag_list += [t for t in tags(s) if f"[{t}]" not in tag_list and t not in tag_list]
    tag_text = ", ".join(f"[{t}]" for t in tag_list)
    for run in ("A", "B"):
        report = f"memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-{key}-{run.lower()}.md"
        context = (
            f"The subject is {desc} for build dClosedLoop, a design-only build that re-architects gov onto one loop. "
            "The owner framed this layer, and settled its forks in the record's own answer sections. The owner asked "
            "for two independent medium-effort Tier-2 rounds on each of layers 1 to 4, as were run on the runtime layer, "
            f"their results compared to spot gaps; this is run {run} on layer {n}, the {key} layer. Layers settled after "
            "this record was written, the runtime layer last, are among the specs, and a statement here that a later "
            f"layer changed or contradicts is a finding.{extra} Audit the record as an architecture spec, against six "
            "questions: (1) internal consistency: do its components, principles, policies, build units, gaps and "
            "answers agree with each other; (2) consistency with the sibling records in specs: v2's principles, policy "
            "catalogue and chain, and the other layers' records; (3) feasibility against the measured facts in the "
            "research returns and records in specs: a mechanism the platform or the tree cannot support, or a claim the "
            "evidence does not bear out; (4) missing mechanisms: anything this layer must provide to the other layers "
            "that the design omits; (5) claims that are unenforced or untestable as written; (6) extension points that "
            "could not in fact be filled without changing code. Address each finding by the record's section tag, such "
            f"as {tag_text}. Write the report to {report}. Its head carries an H1, then, within its first twelve lines, "
            "the line `**Serves:** spec-audit PLAY-dClosedLoop-1`. It carries exactly one `## Verdict:` line, whose "
            "token is CLEAN, CLEAN WITH FIXES or BLOCKED and nothing else.")
        args = {
            "kind": "spec-audit", "repo": REPO,
            "subjects": [{"path": s, "blob": blob(s)} for s in subjects],
            "scratch": f"{SP}/review-{key}-{run.lower()}", "reviewDir": "memory/builds/dClosedLoop/reviews",
            "round": 1, "intensity": "full",
            "roles": {"specFinder": "gov-spec-reviewer", "skeptic": "gov-skeptic", "synthesis": "gov-synthesizer"},
            "efforts": {"specFinder": "medium", "skeptic": "medium", "synthesis": "medium"},
            "specs": specs, "context": context, "byDesign": BY_DESIGN, "checklist": checklist,
        }
        out = f"{SP}/l14/args-{key}-{run.lower()}.json"
        json.dump(args, open(out, "w", encoding="utf-8"), indent=1)
        index.append(f"{key}-{run.lower()}: {len(json.dumps(args))} chars, {len(specs)} specs, subjects "
                     + ", ".join(f"{s.rsplit('-', 1)[-1]}@{blob(s)[:8]}" for s in subjects))
print("\n".join(index))
```

## [args] Round B's args, layer by layer

The fields every round shares, with the scratch path and the checklist abbreviated:

```json
{
 "kind": "spec-audit",
 "repo": "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297",
 "reviewDir": "memory/builds/dClosedLoop/reviews",
 "round": 1,
 "intensity": "full",
 "roles": {
  "specFinder": "gov-spec-reviewer",
  "skeptic": "gov-skeptic",
  "synthesis": "gov-synthesizer"
 },
 "efforts": {
  "specFinder": "medium",
  "skeptic": "medium",
  "synthesis": "medium"
 },
 "byDesign": "- The build is design-only: no product code and no unit specs; each chain build writes its own specs later, so unit-level implementation detail is absent by design.\n- The owner's settled answers, recorded in the record's answer sections, are decisions: a finding may show that one contradicts another record, the platform or the tree, but does not re-argue the owner's choice.\n- Records outside memory/builds/dClosedLoop/ are not under review, and the research returns are evidence, not subjects.",
 "scratch": "<the session scratchpad>/review-<layer>-<run>",
 "checklist": "<the text in [checklist]>"
}
```

Each layer's own fields, verbatim. Round A's differ only in the context's run label and report path.

### [args-instruction]

```json
{
 "subjects": [
  {
   "path": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md",
   "blob": "3cfd547af6f355c5df687331f71a945f56a2e140"
  }
 ],
 "specs": [
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md",
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-foundations.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-design-overview.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md"
 ],
 "context": "The subject is the instruction layer's design record for build dClosedLoop, a design-only build that re-architects gov onto one loop. The owner framed this layer, and settled its forks in the record's own answer sections. The owner asked for two independent medium-effort Tier-2 rounds on each of layers 1 to 4, as were run on the runtime layer, their results compared to spot gaps; this is run B on layer 1, the instruction layer. Layers settled after this record was written, the runtime layer last, are among the specs, and a statement here that a later layer changed or contradicts is a finding. Audit the record as an architecture spec, against six questions: (1) internal consistency: do its components, principles, policies, build units, gaps and answers agree with each other; (2) consistency with the sibling records in specs: v2's principles, policy catalogue and chain, and the other layers' records; (3) feasibility against the measured facts in the research returns and records in specs: a mechanism the platform or the tree cannot support, or a claim the evidence does not bear out; (4) missing mechanisms: anything this layer must provide to the other layers that the design omits; (5) claims that are unenforced or untestable as written; (6) extension points that could not in fact be filled without changing code. Address each finding by the record's section tag, such as [words], [layers], [current], [fit], [uncovered], [charter-today], [recommendations], [forks], [settled]. Write the report to memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-instruction-b.md. Its head carries an H1, then, within its first twelve lines, the line `**Serves:** spec-audit PLAY-dClosedLoop-1`. It carries exactly one `## Verdict:` line, whose token is CLEAN, CLEAN WITH FIXES or BLOCKED and nothing else."
}
```

### [args-flow]

```json
{
 "subjects": [
  {
   "path": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md",
   "blob": "7031c90f195ce746943196d2dc570b84dd753b63"
  },
  {
   "path": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md",
   "blob": "43e9cf4b27292b535aa24a2680a73cd663a62e34"
  }
 ],
 "specs": [
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md",
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-flow.md",
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-flow-interactions.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-flow-items-a.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-flow-items-b.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md"
 ],
 "context": "The subject is the flow layer's two design records, its layer review and its steps defined item by item for build dClosedLoop, a design-only build that re-architects gov onto one loop. The owner framed this layer, and settled its forks in the record's own answer sections. The owner asked for two independent medium-effort Tier-2 rounds on each of layers 1 to 4, as were run on the runtime layer, their results compared to spot gaps; this is run B on layer 2, the flow layer. Layers settled after this record was written, the runtime layer last, are among the specs, and a statement here that a later layer changed or contradicts is a finding. The owner holds a revisit of this layer's relations to the other layers; a finding about those relations is still reported, as input to that revisit. Audit the record as an architecture spec, against six questions: (1) internal consistency: do its components, principles, policies, build units, gaps and answers agree with each other; (2) consistency with the sibling records in specs: v2's principles, policy catalogue and chain, and the other layers' records; (3) feasibility against the measured facts in the research returns and records in specs: a mechanism the platform or the tree cannot support, or a claim the evidence does not bear out; (4) missing mechanisms: anything this layer must provide to the other layers that the design omits; (5) claims that are unenforced or untestable as written; (6) extension points that could not in fact be filled without changing code. Address each finding by the record's section tag, such as [words], [how], [shape], [fit], [uncovered], [recommendations], [audit], [forks], [settled], [rules], [entry], [plan], [design], [build], [test], [deploy], [breakpoint], [expansions], [consequences], [open]. Write the report to memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-flow-b.md. Its head carries an H1, then, within its first twelve lines, the line `**Serves:** spec-audit PLAY-dClosedLoop-1`. It carries exactly one `## Verdict:` line, whose token is CLEAN, CLEAN WITH FIXES or BLOCKED and nothing else."
}
```

### [args-roles]

```json
{
 "subjects": [
  {
   "path": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md",
   "blob": "081ef3c1a150617101b948c3f276900abd0a2dd5"
  }
 ],
 "specs": [
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md",
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-roles.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md",
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-research-roles-anatomy.md",
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-research-roles-coverage.md",
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-research-roles-interactions.md",
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-research-roles-priorart.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md"
 ],
 "context": "The subject is the roles layer's design record for build dClosedLoop, a design-only build that re-architects gov onto one loop. The owner framed this layer, and settled its forks in the record's own answer sections. The owner asked for two independent medium-effort Tier-2 rounds on each of layers 1 to 4, as were run on the runtime layer, their results compared to spot gaps; this is run B on layer 3, the roles layer. Layers settled after this record was written, the runtime layer last, are among the specs, and a statement here that a later layer changed or contradicts is a finding. The owner holds a revisit of this layer's mechanical shape (the execution shape of each role item); a finding about it is still reported, as input to that revisit. Audit the record as an architecture spec, against six questions: (1) internal consistency: do its components, principles, policies, build units, gaps and answers agree with each other; (2) consistency with the sibling records in specs: v2's principles, policy catalogue and chain, and the other layers' records; (3) feasibility against the measured facts in the research returns and records in specs: a mechanism the platform or the tree cannot support, or a claim the evidence does not bear out; (4) missing mechanisms: anything this layer must provide to the other layers that the design omits; (5) claims that are unenforced or untestable as written; (6) extension points that could not in fact be filled without changing code. Address each finding by the record's section tag, such as [words], [settled], [current], [fit], [trust], [tags], [matrix], [roster], [more], [gaps], [forks], [owner-notes], [instrument]. Write the report to memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-roles-b.md. Its head carries an H1, then, within its first twelve lines, the line `**Serves:** spec-audit PLAY-dClosedLoop-1`. It carries exactly one `## Verdict:` line, whose token is CLEAN, CLEAN WITH FIXES or BLOCKED and nothing else."
}
```

### [args-memory]

```json
{
 "subjects": [
  {
   "path": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md",
   "blob": "bb5dd4e2d648746f6656f7e766261aaea8964b96"
  }
 ],
 "specs": [
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-builds.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-asks-decisions.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-map-reuse.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-annotations.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-tooling.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md"
 ],
 "context": "The subject is the memory layer's design record for build dClosedLoop, a design-only build that re-architects gov onto one loop. The owner framed this layer, and settled its forks in the record's own answer sections. The owner asked for two independent medium-effort Tier-2 rounds on each of layers 1 to 4, as were run on the runtime layer, their results compared to spot gaps; this is run B on layer 4, the memory layer. Layers settled after this record was written, the runtime layer last, are among the specs, and a statement here that a later layer changed or contradicts is a finding. Audit the record as an architecture spec, against six questions: (1) internal consistency: do its components, principles, policies, build units, gaps and answers agree with each other; (2) consistency with the sibling records in specs: v2's principles, policy catalogue and chain, and the other layers' records; (3) feasibility against the measured facts in the research returns and records in specs: a mechanism the platform or the tree cannot support, or a claim the evidence does not bear out; (4) missing mechanisms: anything this layer must provide to the other layers that the design omits; (5) claims that are unenforced or untestable as written; (6) extension points that could not in fact be filled without changing code. Address each finding by the record's section tag, such as [words], [settled], [research], [current], [fit], [design], [contract], [build], [names], [relations], [asks], [decisions], [reuse], [map], [annotations], [knowledge], [views], [determinism], [tools], [gaps-proposed], [forks], [instrument]. Write the report to memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-memory-b.md. Its head carries an H1, then, within its first twelve lines, the line `**Serves:** spec-audit PLAY-dClosedLoop-1`. It carries exactly one `## Verdict:` line, whose token is CLEAN, CLEAN WITH FIXES or BLOCKED and nothing else."
}
```

## [checklist] The checklist every round was handed

`gotchas.py`'s output over the subject, the same for all four layers:

```text
# recurring-bug-class checklist for 1 path(s) (1 file(s))
# 5 class(es) selected by an anchor + 6 universal
# by anchor specificity: 0 path · 4 directory · 1 basename; a cut tier prints one line per class
# invariants are read from the working tree; with no --base, a record this subject adds or edits can stand as by design

- [ ] fixture-passes-by-finding-nothing (universal)
      a test arm whose fixture never triggers the rule passes, and proves nothing
      memory/gotchas/fixture-passes-by-finding-nothing.md

- [ ] guard-above-a-fold-makes-its-fallback-dead (universal)
      a guard added above a fold settles the predicate the fold's own fallback re-tests, leaving a dead arm that reads as coverage
      memory/gotchas/guard-above-a-fold-makes-its-fallback-dead.md

- [ ] heredoc-escape-reaches-the-regex (universal)
      source written through a shell heredoc into a non-raw string turns an escape into a control byte, and the symptom never looks like a quoting problem
      memory/gotchas/heredoc-escape-reaches-the-regex.md

- [ ] inline-fence-swallows-the-rest-of-the-file (universal)
      a triple-backtick written inline in prose opens a fence the reader never closes, so every section after it silently disappears from the checker's view
      memory/gotchas/inline-fence-swallows-the-rest-of-the-file.md

- [ ] staged-break-substitutes-a-synthetic-value (universal)
      an arm that proves a mechanism by replacing the shipped value with a simpler one proves the mechanism for the simpler value
      memory/gotchas/staged-break-substitutes-a-synthetic-value.md

- [ ] two-answers-to-one-question (universal)
      a fact stated in two places drifts, and the copies need not disagree loudly to be wrong
      memory/gotchas/two-answers-to-one-question.md

- [ ] a-merge-of-the-default-branch-read-as-additions (directory)
      a check that lists the files a range or a commit ADDS reads a merge of the default branch into a feature branch as adding every file the default branch gained, unless its git invocation is one of the shapes that cannot
      memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md

- [ ] amendment-leaves-its-other-half-standing (directory)
      a criterion is amended and the clause, scope item or log line that only made sense under the old wording is left behind, so one rule now returns two verdicts
      memory/gotchas/amendment-leaves-its-other-half-standing.md

- [ ] ledger-token-wrapped-across-a-line-joins-nothing (directory)
      hygiene check 23 extracts a ledger line's backticked tokens PER LINE, so a token the writer wrapped across a line break belongs to no line and the criterion it answers reads as unanswered
      memory/gotchas/ledger-token-wrapped-across-a-line-joins-nothing.md

- [ ] retirement-inventory-misses-readers-by-value (directory)
      an inventory of what reads a retired thing, built by searching for its name, misses every assertion on a count or a value that thing carries, because those name nothing
      memory/gotchas/retirement-inventory-misses-readers-by-value.md

- [ ] record-without-serves-or-with-a-round-counter (basename)
      a new build record owes a Serves line and a filename that projects it, and a round counter in that filename mints an id nothing defines
      memory/gotchas/record-without-serves-or-with-a-round-counter.md

# by design — 0 invariant(s) this selection touches
```

## [compare] The comparison script

The runtime comparison's script, with one change: a seventh argument names the map's section tag.

```python
"""Compare two Tier-2 rounds on one subject, defect by defect.

Inputs, all tracked: the two review reports (their appendix tables), the comparison record
(its [map] table, one row per defect naming each round's finding ids), and the session log
(the agent ledger's returned lines for the two runs).

Refuses, exit 1: a finding id the map does not place, a map id the report lacks, a run with no
returned lines. Prints every number the comparison record states.

Usage: python compare_rounds.py <report-a> <report-b> <compare-record> <session-log> <run-a> <run-b> [<map-tag>]
  <map-tag> names the record's map section, `## [<map-tag>]`; it defaults to `map`.
"""
import re
import sys

SEV = {"low": 1, "medium": 2, "high": 3, "blocker": 4}


def appendix(path):
    text = open(path, encoding="utf-8", newline="").read()
    tail = text.split("## Appendix", 1)[1]
    rows = {}
    for line in tail.splitlines():
        if not re.match(r"^\| \d+ \|", line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
        fid, lens, _ref, sev, skep, verdict = cells[:6]
        if verdict not in ("confirmed", "refuted", "unverified", "uncertain"):
            sys.exit(f"{path}: id {fid}: unparseable verdict {verdict!r}")
        rows[int(fid)] = {"lens": lens, "sev": (skep or sev), "verdict": verdict}
    if not rows:
        sys.exit(f"{path}: no appendix rows")
    return rows


def ids(cell):
    cell = cell.strip()
    return [] if cell in ("—", "-", "") else [int(x) for x in re.split(r"[,\s]+", cell) if x]


def defect_map(path, tag="map"):
    text = open(path, encoding="utf-8", newline="").read()
    head = f"\n## [{tag}]"
    if head not in text:
        sys.exit(f"{path}: no section {head.strip()}")
    block = text.split(head, 1)[1].split("\n## ", 1)[0]
    out = []
    for line in block.splitlines():
        if not line.startswith("| `"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
        out.append({"tag": cells[0].strip("`"), "A": ids(cells[2]), "B": ids(cells[3]), "disp": cells[4]})
    if not out:
        sys.exit(f"{path}: no [map] rows")
    return out


def returned_out(path, run):
    text = open(path, encoding="utf-8", newline="").read()
    outs = [float(m.group(1)) * (1000 if m.group(2) else 1) for m in re.finditer(
        r"^- returned — .*? · ([0-9.]+)(k?) out · run " + re.escape(run) + r"/", text, re.M)]
    if not outs:
        sys.exit(f"{path}: no returned lines for run {run}")
    return len(outs), sum(outs) / 1000


def main():
    rep = {"A": appendix(sys.argv[1]), "B": appendix(sys.argv[2])}
    dmap = defect_map(sys.argv[3], sys.argv[7] if len(sys.argv) > 7 else "map")
    runs = {"A": returned_out(sys.argv[4], sys.argv[5]), "B": returned_out(sys.argv[4], sys.argv[6])}

    placed = {"A": set(), "B": set()}
    for d in dmap:
        for r in "AB":
            for i in d[r]:
                if i not in rep[r]:
                    sys.exit(f"map row {d['tag']}: {r}{i} is not in report {r}")
                placed[r].add(i)
    for r in "AB":
        missing = sorted(set(rep[r]) - placed[r])
        if missing:
            sys.exit(f"report {r}: ids the map does not place: {missing}")

    def state(d, r):
        vs = [rep[r][i]["verdict"] for i in d[r]]
        if "confirmed" in vs:
            return "confirmed"
        return "raised-refuted" if vs else "absent"

    def sev(d, r):
        s = [SEV[rep[r][i]["sev"]] for i in d[r] if rep[r][i]["verdict"] == "confirmed"]
        return max(s) if s else 0

    real = [d for d in dmap if "confirmed" in (state(d, "A"), state(d, "B"))]
    both = [d for d in real if state(d, "A") == state(d, "B") == "confirmed"]
    only = {r: [d for d in real if state(d, r) == "confirmed" and state(d, "AB"[r == "A"]) != "confirmed"] for r in "AB"}
    n = {r: len(both) + len(only[r]) for r in "AB"}

    print("== runs")
    for r in "AB":
        conf = sum(1 for v in rep[r].values() if v["verdict"] == "confirmed")
        highs = sum(1 for v in rep[r].values() if v["verdict"] == "confirmed" and SEV[v["sev"]] >= 3)
        agents, out = runs[r]
        print(f"{r}: raw {len(rep[r])}, confirmed {conf}, refuted {len(rep[r]) - conf}, "
              f"precision {conf / len(rep[r]):.2f}, high findings {highs}, "
              f"agents {agents}, out {out:.1f}k (sum of returned lines)")
    print("== defects")
    print(f"map rows {len(dmap)}, confirmed defects {len(real)}, refuted-only {len(dmap) - len(real)}")
    print(f"both {len(both)}, A only {len(only['A'])}, B only {len(only['B'])}")
    for r in "AB":
        print(f"{r} alone covers {n[r]} of {len(real)} ({n[r] / len(real):.0%})")
    print(f"overlap (Jaccard) {len(both) / len(real):.2f}")
    chap = (n["A"] + 1) * (n["B"] + 1) / (len(both) + 1) - 1
    print(f"Chapman estimate of the population: {chap:.1f}, so about {chap - len(real):.0f} found by neither")
    for r in "AB":
        print(f"{r} only: {', '.join(d['tag'] for d in only[r])}")
    print("== severity (a defect takes its highest confirmed grade per round)")
    hi = [d for d in real if max(sev(d, 'A'), sev(d, 'B')) >= 3]
    print(f"high defects {len(hi)}: {', '.join(d['tag'] for d in hi)}")
    for d in hi:
        print(f"  {d['tag']}: A {sev(d, 'A')} B {sev(d, 'B')}")
    agree = sum(1 for d in both if sev(d, "A") == sev(d, "B"))
    print(f"shared defects graded alike {agree} of {len(both)}")
    print("== lenses behind the defects one round alone found")
    for r in "AB":
        tally = {}
        for d in only[r]:
            for lens in sorted({rep[r][i]["lens"] for i in d[r] if rep[r][i]["verdict"] == "confirmed"}):
                tally[lens] = tally.get(lens, 0) + 1
        print(f"{r}: " + ", ".join(f"{k} {v}" for k, v in sorted(tally.items(), key=lambda kv: -kv[1])))
    print("== refuted findings and their twins")
    for r in "AB":
        for i, v in sorted(rep[r].items()):
            if v["verdict"] == "confirmed":
                continue
            d = next(d for d in dmap if i in d[r])
            twin = [f"{q}{j}" for q in "AB" for j in d[q] if rep[q][j]["verdict"] == "confirmed"]
            print(f"{r}{i} ({d['tag']}): confirmed twin {', '.join(twin) if twin else 'none'}")


if __name__ == "__main__":
    main()
```

## [summarize] The summary script

```python
"""Run the round comparison over each layer's map and derive the cross-layer table.

Usage: python summarize_layers.py <compare_rounds.py> <layers-record> <runtime-record> <session-log>

Runs compare_rounds.py once per layer, the runtime layer on its own record's `[map]` and layers 1 to 4
on the layers record's `[map-<layer>]`. Refuses, exit 1, when any run refuses or prints a line this
parser does not recognise. Prints the summary table, then every run's full output.
"""
import re
import subprocess
import sys

REPORT = "memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-{}-{}.md"
LAYERS = [  # name, which record holds the map, the map's tag, run A, run B
    ("runtime", "runtime", "map", "wf_6508cb22-7d6", "wf_3c895b43-8da"),
    ("instruction", "layers", "map-instruction", "wf_261507e4-5ca", "wf_c5538013-6cc"),
    ("flow", "layers", "map-flow", "wf_1532dea2-2f7", "wf_782666f6-e98"),
    ("roles", "layers", "map-roles", "wf_478254d1-ce0", "wf_08c634a0-1b4"),
    ("memory", "layers", "map-memory", "wf_b6756400-d03", "wf_ec731bfc-925"),
]


def grab(pattern, text, name):
    m = re.search(pattern, text, re.M)
    if not m:
        sys.exit(f"{name}: no line matches {pattern!r}")
    return m.groups()


def run(script, record, log, name, tag, run_a, run_b):
    out = subprocess.run([sys.executable, script, REPORT.format(name, "a"), REPORT.format(name, "b"),
                          record, log, run_a, run_b, tag], capture_output=True, text=True)
    if out.returncode != 0:
        sys.exit(f"{name}: compare_rounds refused: {(out.stdout + out.stderr).strip()}")
    t = out.stdout
    r = {"name": name, "text": t}
    for side in "AB":
        raw, conf, prec, spent = grab(rf"^{side}: raw (\d+), confirmed (\d+), refuted \d+, precision ([0-9.]+), "
                                      rf"high findings \d+, agents \d+, out ([0-9.]+)k ", t, name)
        r[side] = (int(raw), int(conf), prec, float(spent))
    r["defects"], r["refuted_only"] = map(int, grab(r"^map rows \d+, confirmed defects (\d+), refuted-only (\d+)$", t, name))
    r["both"], r["a_only"], r["b_only"] = map(int, grab(r"^both (\d+), A only (\d+), B only (\d+)$", t, name))
    r["chapman"] = float(grab(r"^Chapman estimate of the population: ([0-9.]+),", t, name)[0])
    highs = re.findall(r"^  (\S+): A (\d) B (\d)$", t, re.M)
    r["high"] = len(highs)
    r["high_one"] = [tag for tag, a, b in highs if a == "0" or b == "0"]
    r["alike"] = tuple(map(int, grab(r"^shared defects graded alike (\d+) of (\d+)$", t, name)))
    refuted = re.findall(r"^[AB]\d+ \(\S+\): confirmed twin (.+)$", t, re.M)
    r["refuted"] = len(refuted)
    r["twinned"] = sum(1 for v in refuted if v != "none")
    if len(highs) != int(grab(r"^high defects (\d+)", t, name)[0]):
        sys.exit(f"{name}: the high-defect lines do not match their count")
    return r


def pct(n, d):
    return f"{n / d:.0%}"


def main():
    script, layers_rec, runtime_rec, log = sys.argv[1:5]
    rows = [run(script, runtime_rec if which == "runtime" else layers_rec, log, name, tag, a, b)
            for name, which, tag, a, b in LAYERS]
    print("| Layer | Findings A / B | Confirmed A / B | Precision A / B | Out A / B |")
    print("|---|---|---|---|---|")
    oa = ob = 0.0
    for r in rows:
        print(f"| {r['name']} | {r['A'][0]} / {r['B'][0]} | {r['A'][1]} / {r['B'][1]} "
              f"| {r['A'][2]} / {r['B'][2]} | {r['A'][3]:.1f}k / {r['B'][3]:.1f}k |")
        oa, ob = oa + r["A"][3], ob + r["B"][3]
    fa, fb = sum(r["A"][0] for r in rows), sum(r["B"][0] for r in rows)
    ca, cb = sum(r["A"][1] for r in rows), sum(r["B"][1] for r in rows)
    print(f"| all five | {fa} / {fb} | {ca} / {cb} | {ca / fa:.2f} / {cb / fb:.2f} | {oa:.1f}k / {ob:.1f}k |")
    print()
    print("| Layer | Defects | Both | A only | B only | A alone covers | B alone covers | Overlap "
          "| Chapman: found by neither | High defects | High, one round only | Shared, graded alike "
          "| Refuted, with a confirmed twin |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    tot = {k: 0 for k in ("d", "both", "ao", "bo", "high", "ho", "al", "sh", "rf", "tw")}
    chap = 0.0
    for r in rows:
        d, both = r["defects"], r["both"]
        print(f"| {r['name']} | {d} | {both} "
              f"| {r['a_only']} | {r['b_only']} | {pct(both + r['a_only'], d)} | {pct(both + r['b_only'], d)} "
              f"| {both / d:.2f} | {r['chapman'] - d:.0f} | {r['high']} | {len(r['high_one'])} "
              f"| {r['alike'][0]} of {r['alike'][1]} | {r['twinned']} of {r['refuted']} |")
        for k, v in (("d", d), ("both", both), ("ao", r["a_only"]), ("bo", r["b_only"]), ("high", r["high"]),
                     ("ho", len(r["high_one"])), ("al", r["alike"][0]), ("sh", r["alike"][1]),
                     ("rf", r["refuted"]), ("tw", r["twinned"])):
            tot[k] += v
        chap += r["chapman"] - d
    t = tot
    print(f"| all five | {t['d']} | {t['both']} | {t['ao']} "
          f"| {t['bo']} | {pct(t['both'] + t['ao'], t['d'])} | {pct(t['both'] + t['bo'], t['d'])} "
          f"| {t['both'] / t['d']:.2f} | {chap:.0f} | {t['high']} | {t['ho']} | {t['al']} of {t['sh']} "
          f"| {t['tw']} of {t['rf']} |")
    print()
    print("high defects one round alone found: " + "; ".join(
        f"{r['name']}: {', '.join(r['high_one'])}" for r in rows if r["high_one"]))
    print(f"layers 1 to 4: defects {sum(r['defects'] for r in rows[1:])}, both {sum(r['both'] for r in rows[1:])}, "
          f"A only {sum(r['a_only'] for r in rows[1:])}, B only {sum(r['b_only'] for r in rows[1:])}, "
          f"high {sum(r['high'] for r in rows[1:])}, high one round only {sum(len(r['high_one']) for r in rows[1:])}, "
          f"found by neither {sum(r['chapman'] - r['defects'] for r in rows[1:]):.0f}, "
          f"refuted with a confirmed twin {sum(r['twinned'] for r in rows[1:])} of {sum(r['refuted'] for r in rows[1:])}, "
          f"out {sum(r['A'][3] + r['B'][3] for r in rows[1:]):.1f}k")
    for r in rows:
        print(f"\n=== {r['name']}\n{r['text'].rstrip()}")


if __name__ == "__main__":
    main()
```

## [assemble] The record's assembly

It filled the record's template with `[summary]`'s tables and the four maps, so the record carries
what was measured. The summary script was then run again over the written record, and its output
matched the draft's byte for byte.

```python
"""Fill the layers record's template: the two summary tables and the four maps, verbatim.

Usage: python assemble_record.py <scratch-l14> <out-record>
"""
import sys

L14, OUT = sys.argv[1], sys.argv[2]
t = open(f"{L14}/record-template.md", encoding="utf-8").read()
summary = open(f"{L14}/summary.out", encoding="utf-8").read()
tables = summary.split("\nhigh defects one round alone found:", 1)[0].rstrip("\n")
if tables.count("| Layer |") != 2:
    sys.exit("summary.out does not open with the two tables")
t = t.replace("<<SUMMARY>>", tables)
for layer in ("instruction", "flow", "roles", "memory"):
    m = open(f"{L14}/map-{layer}.md", encoding="utf-8").read().rstrip("\n")
    key = f"<<MAP:{layer}>>"
    if t.count(key) != 1:
        sys.exit(f"template lacks {key}")
    t = t.replace(key, m)
if "<<" in t:
    sys.exit("an unfilled placeholder remains")
open(OUT, "w", encoding="utf-8", newline="\n").write(t)
print(f"wrote {OUT}: {len(t.encode('utf-8'))} bytes")
```

## [output] What the summary script printed

Run as `python summarize_layers.py compare_rounds.py <the layers record> <the runtime record> <the session
log>`, exit 0. The runtime section reproduces the runtime record's `[numbers]` verbatim, so the
map-tag change left the old output as it was.

```text
| Layer | Findings A / B | Confirmed A / B | Precision A / B | Out A / B |
|---|---|---|---|---|
| runtime | 60 / 61 | 56 / 57 | 0.93 / 0.93 | 212.2k / 218.0k |
| instruction | 48 / 47 | 44 / 36 | 0.92 / 0.77 | 220.2k / 230.3k |
| flow | 69 / 46 | 60 / 45 | 0.87 / 0.98 | 258.4k / 222.8k |
| roles | 47 / 54 | 37 / 43 | 0.79 / 0.80 | 196.8k / 240.8k |
| memory | 61 / 58 | 52 / 51 | 0.85 / 0.88 | 300.7k / 282.0k |
| all five | 285 / 266 | 249 / 232 | 0.87 / 0.87 | 1188.3k / 1193.9k |

| Layer | Defects | Both | A only | B only | A alone covers | B alone covers | Overlap | Chapman: found by neither | High defects | High, one round only | Shared, graded alike | Refuted, with a confirmed twin |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| runtime | 59 | 32 | 14 | 13 | 78% | 76% | 0.54 | 6 | 8 | 2 | 28 of 32 | 6 of 8 |
| instruction | 48 | 19 | 15 | 14 | 71% | 69% | 0.40 | 10 | 5 | 0 | 14 of 19 | 7 of 15 |
| flow | 57 | 28 | 15 | 14 | 75% | 74% | 0.49 | 7 | 8 | 2 | 18 of 28 | 6 of 10 |
| roles | 33 | 17 | 6 | 10 | 70% | 82% | 0.52 | 3 | 2 | 1 | 15 of 17 | 11 of 21 |
| memory | 68 | 34 | 15 | 19 | 72% | 78% | 0.50 | 8 | 6 | 1 | 22 of 34 | 10 of 16 |
| all five | 265 | 130 | 65 | 70 | 74% | 75% | 0.49 | 35 | 29 | 6 | 97 of 130 | 40 of 70 |

high defects one round alone found: runtime: cycle-spawns, structured-output; flow: bar-attribution-unjoined, lander-exit-classes; roles: repair-staleness; memory: v14-refusal-exists
layers 1 to 4: defects 206, both 98, A only 51, B only 57, high 21, high one round only 4, found by neither 29, refuted with a confirmed twin 34 of 62, out 1952.0k

=== runtime
== runs
A: raw 60, confirmed 56, refuted 4, precision 0.93, high findings 6, agents 12, out 212.2k (sum of returned lines)
B: raw 61, confirmed 57, refuted 4, precision 0.93, high findings 9, agents 12, out 218.0k (sum of returned lines)
== defects
map rows 61, confirmed defects 59, refuted-only 2
both 32, A only 14, B only 13
A alone covers 46 of 59 (78%)
B alone covers 45 of 59 (76%)
overlap (Jaccard) 0.54
Chapman estimate of the population: 64.5, so about 6 found by neither
A only: driver-cwd, binding-events, compaction-checks, cli-floor-decision, permission-mode, parallel-cleared, core-sweep, journal-owner, next-readers, gap-keys, command-idempotence, reap-predicate, deferral-fixtures, cadence-period
B only: invariant-coverage, cycle-spawns, instance-witness, structured-output, headless-workflow, compact-target, user-guards, stopfailure-packs, deferral-seam, owner-rulings, git-witness-readers, return-write-path, limit-hold
== severity (a defect takes its highest confirmed grade per round)
high defects 8: relaunch-replay, merge-back, chain-overlap, fixture-2-population, catalogue-duplicates, fencing, cycle-spawns, structured-output
  relaunch-replay: A 3 B 3
  merge-back: A 3 B 2
  chain-overlap: A 3 B 3
  fixture-2-population: A 3 B 3
  catalogue-duplicates: A 2 B 3
  fencing: A 3 B 3
  cycle-spawns: A 0 B 3
  structured-output: A 0 B 3
shared defects graded alike 28 of 32
== lenses behind the defects one round alone found
A: reuse 5, failure-envelope 4, grounding 2, coherence 2, blast-radius 2
B: failure-envelope 5, grounding 4, coherence 3, blast-radius 3, reuse 3
== refuted findings and their twins
A14 (journal-owner): confirmed twin A35
A45 (prose-ceilings): confirmed twin none
A46 (slug-shape): confirmed twin none
A59 (resume-tick-consumers): confirmed twin A38, B43
B14 (calls-per-act): confirmed twin A21, B23
B38 (hook-fragments): confirmed twin A36, A41, B33
B47 (next-readers): confirmed twin A39
B61 (resume-tick-consumers): confirmed twin A38, B43

=== instruction
== runs
A: raw 48, confirmed 44, refuted 4, precision 0.92, high findings 4, agents 12, out 220.2k (sum of returned lines)
B: raw 47, confirmed 36, refuted 11, precision 0.77, high findings 4, agents 12, out 230.3k (sum of returned lines)
== defects
map rows 54, confirmed defects 48, refuted-only 6
both 19, A only 15, B only 14
A alone covers 34 of 48 (71%)
B alone covers 33 of 48 (69%)
overlap (Jaccard) 0.40
Chapman estimate of the population: 58.5, so about 10 found by neither
A only: tag-spelling, act-session-load-point, agent-instructions-seam, join-population, knowledge-in-core-render, heading-grammar, gap-count-mismatch, hook-injected-loads, trigger-read-bytes, crlf-byte-counts, retired-summed-budget, tag-registry-seams, one-source-roles-list, governing-document-rename, gap-found-17-stale
B only: example-item-names, charter-before-policy, grammar-red-case, reuse-entries-units, command-items-units, principle-check-switchable, layer-conformance-gate, policy-level, help-move-owner, node-registry-card, worktrees-placeholder, instruction-paths, tag-lifecycle, handed-content-grammar
== severity (a defect takes its highest confirmed grade per round)
high defects 5: codex-override, existing-budgets, roles-tag-join, section-number-readers, owner-proof
  codex-override: A 3 B 2
  existing-budgets: A 2 B 3
  roles-tag-join: A 3 B 3
  section-number-readers: A 3 B 2
  owner-proof: A 3 B 3
shared defects graded alike 14 of 19
== lenses behind the defects one round alone found
A: coherence 6, reuse 4, blast-radius 3, grounding 3, failure-envelope 2
B: coherence 8, failure-envelope 4, grounding 1, reuse 1, blast-radius 1
== refuted findings and their twins
A30 (provenance-marker-readers): confirmed twin none
A45 (grammar-red-case): confirmed twin B41
A46 (grammar-template-type): confirmed twin none
A47 (section-number-readers): confirmed twin A29, B20
B11 (existing-budgets): confirmed twin A22, A31, B18
B15 (card-rank-or5): confirmed twin none
B21 (provenance-marker-readers): confirmed twin none
B23 (effectiveness-seam): confirmed twin none
B24 (agent-instructions-seam): confirmed twin A26
B25 (instruction-command-seams): confirmed twin none
B29 (act-session-load-point): confirmed twin A5, A38
B31 (codex-override): confirmed twin A6, A14, A39, B40
B32 (harness-injected-loads): confirmed twin A4, A44, B39
B35 (microformats-fence): confirmed twin none
B37 (provenance-marker-readers): confirmed twin none

=== flow
== runs
A: raw 69, confirmed 60, refuted 9, precision 0.87, high findings 6, agents 12, out 258.4k (sum of returned lines)
B: raw 46, confirmed 45, refuted 1, precision 0.98, high findings 3, agents 12, out 222.8k (sum of returned lines)
== defects
map rows 61, confirmed defects 57, refuted-only 4
both 28, A only 15, B only 14
A alone covers 43 of 57 (75%)
B alone covers 42 of 57 (74%)
overlap (Jaccard) 0.49
Chapman estimate of the population: 64.2, so about 7 found by neither
A only: self-typed-review-witnesses, exit-witness-all-items, parents-test-decides, ask-acceptance, first-unwitnessed-item, bar-attribution-unjoined, verdict-tree-build-tip, lease-ref-history, merge-read-as-additions, design-rounds-carrier, lander-seams, lander-exit-classes, owner-disposition-witness, item-count-readers, mailbox-prune-orphan
B only: pause-leases, review-findings-entry, scope-refusal-stuck, review-harness-seam, tests-without-cadence-semantics, tag-policy-collision, turnstile-not-queue, reasoning-field-timing, tier-preset-guarded, flakes-quarantine-seam, placement-policy-routes, disposition-set-gaps, deployer-expansion-mismatch, instruction-tag-examples
== severity (a defect takes its highest confirmed grade per round)
high defects 8: owner-gate-vs-question, withdraw-program-missing, red-routes-ignore-policy, bar-attribution-unjoined, design-audit-no-fold, intake-owner-scope, intake-secrets, lander-exit-classes
  owner-gate-vs-question: A 3 B 3
  withdraw-program-missing: A 3 B 2
  red-routes-ignore-policy: A 2 B 3
  bar-attribution-unjoined: A 3 B 0
  design-audit-no-fold: A 2 B 3
  intake-owner-scope: A 3 B 2
  intake-secrets: A 3 B 2
  lander-exit-classes: A 3 B 0
shared defects graded alike 18 of 28
== lenses behind the defects one round alone found
A: failure-envelope 5, coherence 4, grounding 4, reuse 3, blast-radius 2
B: blast-radius 4, failure-envelope 3, coherence 3, reuse 2, grounding 2
== refuted findings and their twins
A9 (review-findings-entry): confirmed twin B8
A15 (maintain-superseded-text): confirmed twin none
A28 (audit-b-count): confirmed twin none
A33 (review-harness-seam): confirmed twin B21
A37 (class-set-undefined): confirmed twin A26, B24
A40 (tests-without-cadence-dup): confirmed twin none
A44 (tag-policy-collision): confirmed twin B5
A47 (deploy-close-reconcile): confirmed twin A65, B44
A51 (recommendation-source-mismatch): confirmed twin none
B18 (merge-read-as-additions): confirmed twin A25

=== roles
== runs
A: raw 47, confirmed 37, refuted 10, precision 0.79, high findings 0, agents 12, out 196.8k (sum of returned lines)
B: raw 54, confirmed 43, refuted 11, precision 0.80, high findings 1, agents 12, out 240.8k (sum of returned lines)
== defects
map rows 39, confirmed defects 33, refuted-only 6
both 17, A only 6, B only 10
A alone covers 23 of 33 (70%)
B alone covers 27 of 33 (82%)
overlap (Jaccard) 0.52
Chapman estimate of the population: 36.3, so about 3 found by neither
A only: gaps-count-stale, settled-rule-attribution, cycle-amendment, claimed-fact-staleness, read-class-undefined, cli-version-measurement
B only: effort-carrier, rules-key-binding, handoff-seam, repair-staleness, p29-vs-p23, flow-roles-steps-stale, verifier-set-spelling, cached-prefix-claim, roster-fold-item, adopter-role-overlays
== severity (a defect takes its highest confirmed grade per round)
high defects 2: repair-lifecycle, repair-staleness
  repair-lifecycle: A 2 B 3
  repair-staleness: A 0 B 3
shared defects graded alike 15 of 17
== lenses behind the defects one round alone found
A: grounding 2, failure-envelope 2, coherence 1, reuse 1
B: coherence 5, blast-radius 2, reuse 2, grounding 2, failure-envelope 1
== refuted findings and their twins
A9 (recall-once-per-session): confirmed twin none
A19 (blob-sha-crlf): confirmed twin none
A22 (effort-carrier): confirmed twin B38
A24 (metrics-extractor-seam): confirmed twin none
A25 (role-step-join-exists): confirmed twin none
A26 (rules-key-binding): confirmed twin B30
A27 (handoff-seam): confirmed twin B28
A30 (protocol-pointer-machinery): confirmed twin A47, B37
A34 (keys-agent-typed): confirmed twin none
A42 (answered-state-calls): confirmed twin A11, B46
B11 (dboundroles-order): confirmed twin none
B19 (blob-sha-crlf): confirmed twin none
B20 (cut-at-launch): confirmed twin A7, A11, A41, B12, B40
B23 (sod-agent-id-check): confirmed twin A3, A36, B7, B53
B26 (role-step-join-exists): confirmed twin none
B27 (metrics-extractor-seam): confirmed twin none
B29 (effort-carrier): confirmed twin B38
B34 (cut-at-launch): confirmed twin A7, A11, A41, B12, B40
B35 (matrix-prompt-writer): confirmed twin A2, A14, A35, B2, B16, B36, B50
B43 (role-step-join-exists): confirmed twin none
B54 (protocol-pointer-machinery): confirmed twin A47, B37

=== memory
== runs
A: raw 61, confirmed 52, refuted 9, precision 0.85, high findings 1, agents 12, out 300.7k (sum of returned lines)
B: raw 58, confirmed 51, refuted 7, precision 0.88, high findings 5, agents 12, out 282.0k (sum of returned lines)
== defects
map rows 73, confirmed defects 68, refuted-only 5
both 34, A only 15, B only 19
A alone covers 49 of 68 (72%)
B alone covers 53 of 68 (78%)
overlap (Jaccard) 0.50
Chapman estimate of the population: 76.1, so about 8 found by neither
A only: stale-map-tokenizers, slug-date-text-stale, frozen-refs-resolve, relation-target-unlanded, flip-acceptance-unfailable, grammar-change-existing-ids, decisions-layer-placement, decisions-append-only, reuse-entry-proposal-path, reuse-field-seam, foundation-home, dossier-anchor-seam, feature-anchor-cases, pushed-at-read-no-hook, gap-owner-order
B only: ref-homed-kinds, generated-kinds-door, hygiene-checks-not-schema, check-numbers-stable, derived-keys-front-matter, id-grammar-seam, v14-refusal-exists, refused-ask-fate, amends-vs-frozen-spec, reuse-entry-should, core-needs-knowledge, reuse-benchmark-rerun, ratchets-seam, map-cost-untimed, callers-restale, inventory-counts, dangling-ids-exist, annotation-style-overturned, follow-through-test
== severity (a defect takes its highest confirmed grade per round)
high defects 6: record-idempotence, record-concurrent-mint, kind-list-incomplete, v14-refusal-exists, spec10-token, reuse-probed-readers
  record-idempotence: A 3 B 3
  record-concurrent-mint: A 2 B 3
  kind-list-incomplete: A 2 B 3
  v14-refusal-exists: A 0 B 3
  spec10-token: A 2 B 3
  reuse-probed-readers: A 2 B 3
shared defects graded alike 22 of 34
== lenses behind the defects one round alone found
A: coherence 6, reuse 5, failure-envelope 4, blast-radius 1
B: coherence 7, failure-envelope 4, reuse 4, blast-radius 3, grounding 3
== refuted findings and their twins
A5 (reuse-entry-level): confirmed twin none
A6 (core-needs-knowledge): confirmed twin B55
A16 (lookup-name-inventory): confirmed twin A17, A32, B38
A23 (map-cost-untimed): confirmed twin B26
A29 (id-grammar-seam): confirmed twin B31
A38 (lookup-name-inventory): confirmed twin A17, A32, B38
A39 (authority-keys-via-record): confirmed twin none
A58 (annotation-grammar-inputs): confirmed twin none
A59 (annotation-green-vacuous): confirmed twin A10, A30, B24, B52
B6 (reuse-field-seam): confirmed twin A26
B7 (recall-boundroles-order): confirmed twin none
B9 (annotation-green-vacuous): confirmed twin A10, A30, B24, B52
B13 (kappa-below-threshold): confirmed twin A15, B57
B19 (reuse-obligation-witness): confirmed twin none
B47 (stale-lexicon-owner): confirmed twin A8, A20, A44, B5, B37, B58
B56 (annotation-grammar-inputs): confirmed twin none
```

## [seen-red] Each script, seen red

Each planted copy differs from the record only in the lines named. Every run exited 1, for the
reason it was planted for.

```text
$ compare_rounds.py ... map-knowledge   (the record holds no [map-knowledge])
memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layers-reviews-compared.md: no section ## [map-knowledge]
exit 1

$ planted: B49 taken off both its rows in [map-memory]
report B: ids the map does not place: [49]
exit 1

$ planted: B59, which report B lacks, added to follow-through-test
map row follow-through-test: B59 is not in report B
exit 1

$ planted: summarize_layers.py over a copy whose [map-roles] heading is renamed
roles: compare_rounds refused: <the session scratchpad>/l14/red-nomap.md: no section ## [map-roles]
exit 1
```

## [fold] The fold's instruments

`set_dispositions.py` fills each layer map's `disposition` cells from the layer record's `[revised]`
table, and refuses unless the two hold the same defects, each once. It writes nothing when it refuses.

```python
"""Fill a layer's map dispositions in the comparison record from the layer record's [revised] table.

Usage: python set_dispositions.py <layer> <layer-record> [<more layer records>...]
Refuses, exit 1, unless the map's defects and the [revised] tables' defects are the same set, each
once. Writes only the comparison record's `disposition` cells for that layer's map.
"""
import re
import sys

COMPARE = "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layers-reviews-compared.md"
layer, records = sys.argv[1], sys.argv[2:]

revised = {}
for rec in records:
    text = open(rec, encoding="utf-8", newline="").read()
    if "\n## [revised]" not in text:
        sys.exit(f"{rec}: no [revised] section")
    block = text.split("\n## [revised]", 1)[1].split("\n## ", 1)[0]
    short = re.sub(r"^.*PLAY-dClosedLoop-1-", "", rec).removesuffix(".md")
    for line in block.splitlines():
        m = re.match(r"^\| `([a-z0-9-]+)` \| ([^|]+?) \| ", line)
        if m:
            if m.group(1) in revised:
                sys.exit(f"{m.group(1)}: placed twice across the [revised] tables")
            revised[m.group(1)] = f"{m.group(2)}; `{short}` `[revised]`"

text = open(COMPARE, encoding="utf-8", newline="").read()
head = f"\n## [map-{layer}]"
before, rest = text.split(head, 1)
section, after = rest.split("\n## ", 1)
lines, seen = [], set()
for line in section.split("\n"):
    m = re.match(r"^(\| `([a-z0-9-]+)` \|.*\| )([^|]*)( \|)$", line)
    if m:
        tag = m.group(2)
        if tag not in revised:
            sys.exit(f"map row {tag}: no disposition in any [revised] table")
        seen.add(tag)
        line = m.group(1) + revised[tag] + m.group(4)
    lines.append(line)
extra = sorted(set(revised) - seen)
if extra:
    sys.exit(f"[revised] rows the map lacks: {extra}")
open(COMPARE, "w", encoding="utf-8", newline="").write(before + head + "\n".join(lines) + "\n## " + after)
kinds = {}
for tag in seen:
    k = revised[tag].split(";")[0]
    kinds[k] = kinds.get(k, 0) + 1
print(f"{layer}: {len(seen)} dispositions set · " + ", ".join(f"{k} {v}" for k, v in sorted(kinds.items())))
```

Run once per layer as each fold landed, it printed:

```text
instruction: 54 dispositions set · amend 43, amend, gap 3, fork, amend 1, none 6, owed 1
flow: 61 dispositions set · amend 51, amend, gap 2, fork, amend 4, none 4
roles: 39 dispositions set · amend 32, fork, amend 1, none 6
memory: 73 dispositions set · amend 63, amend, gap 1, fork, amend 3, none 5, owed 1
```

Seen red both ways on planted copies of the roles record. The comparison record was byte-identical
after both runs:

```text
$ planted: the `blob-sha-crlf` row removed from the roles record's [revised] (1 line)
map row blob-sha-crlf: no disposition in any [revised] table
exit 1

$ planted: a [revised] row for a defect the map lacks, `ghost-defect`, appended (1 line)
[revised] rows the map lacks: ['ghost-defect']
exit 1
```

`tally_folded.py` counts the dispositions and writes `[folded]` in the comparison record. After the fold's
closing review (L6) it takes `--record`, so its refusal can be seen red on a copy:

```python
"""Tally each layer map's dispositions in the comparison record, and write its [folded] section.

Usage: python tally_folded.py [--record <path>] [--write]
Reads the four `[map-<layer>]` tables; each row's last cell opens with its disposition, before `;`.
"""
import re
import sys

C = "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layers-reviews-compared.md"
if "--record" in sys.argv:
    C = sys.argv[sys.argv.index("--record") + 1]
KINDS = ["amend", "amend, gap", "fork, amend", "owed", "none"]
text = open(C, encoding="utf-8", newline="").read()
rows, tot = [], {k: 0 for k in KINDS}
for layer in ("instruction", "flow", "roles", "memory"):
    block = text.split(f"\n## [map-{layer}]", 1)[1].split("\n## ", 1)[0]
    counts = {k: 0 for k in KINDS}
    for line in block.splitlines():
        if line.startswith("| `"):
            disp = line.rstrip(" |").rsplit(" | ", 1)[1].split(";")[0].strip()
            if disp not in counts:
                sys.exit(f"{layer}: unknown disposition {disp!r}")
            counts[disp] += 1
    rows.append((layer, counts))
    for k in KINDS:
        tot[k] += counts[k]
table = ["| Layer | " + " | ".join(KINDS) + " | Rows |", "|---|" + "---|" * (len(KINDS) + 1)]
for layer, c in rows + [("all four", tot)]:
    table.append(f"| {layer} | " + " | ".join(str(c[k]) for k in KINDS) + f" | {sum(c.values())} |")
section = """## [folded] Where every map row went, 2026-10-16

Each layer record's `[revised]` names where every defect's fix sits, and the maps' `disposition` cells
point there. `tally_folded.py` (the instruments record) counts the cells:

""" + "\n".join(table) + """

- **owed** is the fifth disposition the fold needed: a fix that turns on the chain's order goes to v2's
  `[owed]`, for the re-cut.
- **The gaps registered:** `gap-rt-11` to `gap-rt-14`, `gap-flow-15` and `gap-mem-12`; after the
  follow-up round, `gap-deploy-09`, `gap-mem-13` and `gap-mem-14`, with `gap-test-04` and
  `gap-deploy-02` extended. Revised 2026-10-17: this line once left out `gap-mem-14`.
- **The keys added to v2:** `instructions.proof`, `flow.route-backs`, and `policy.on-missing-expansion`
  from LR-4.
"""
print("\n".join(table))
if "--write" in sys.argv:
    if "\n## [folded]" in text:
        a, rest = text.split("\n## [folded]", 1)
        b = rest.split("\n## ", 1)[1]
        text = a + "\n" + section + "\n## " + b
    else:
        text = text.replace("\n## [map-instruction]", "\n" + section + "\n## [map-instruction]", 1)
    open(C, "w", encoding="utf-8", newline="").write(text)
    print("[folded] written")
```

Its run, then its refusal on a planted copy, which left the record untouched:

```text
$ python tally_folded.py
| Layer | amend | amend, gap | fork, amend | owed | none | Rows |
|---|---|---|---|---|---|---|
| instruction | 43 | 3 | 1 | 1 | 6 | 54 |
| flow | 51 | 2 | 4 | 0 | 4 | 61 |
| roles | 32 | 0 | 1 | 0 | 6 | 39 |
| memory | 63 | 1 | 3 | 1 | 5 | 73 |
| all four | 189 | 6 | 9 | 2 | 21 | 227 |
exit 0

$ planted: one instruction row's disposition misspelled `ammend` (1 line changed)
instruction: unknown disposition 'ammend'
exit 1
```

After the follow-up round, four rows moved to `amend, gap`: the comparison record's `[follow-up]`
names them. The tally's text gained the gaps they carry, and the same scripts then printed:

```text
$ python set_dispositions.py flow <the flow layer record> <the step definitions>
flow: 61 dispositions set · amend 48, amend, gap 5, fork, amend 4, none 4
exit 0

$ python set_dispositions.py memory <the memory layer record>
memory: 73 dispositions set · amend 62, amend, gap 2, fork, amend 3, none 5, owed 1
exit 0

$ python tally_folded.py --write
| Layer | amend | amend, gap | fork, amend | owed | none | Rows |
|---|---|---|---|---|---|---|
| instruction | 43 | 3 | 1 | 1 | 6 | 54 |
| flow | 48 | 5 | 4 | 0 | 4 | 61 |
| roles | 32 | 0 | 1 | 0 | 6 | 39 |
| memory | 62 | 2 | 3 | 1 | 5 | 73 |
| all four | 185 | 10 | 9 | 2 | 21 | 227 |
[folded] written
exit 0
```

## [fold-review] The fold's closing review

The fold's own diff review, dispatch 47, run as `wf_9349d401-2da`: light, three lenses, at the
closing-review roles' declared effort (`handoff.py stage-efforts closing-review`). Its args,
verbatim:

```json
{
 "kind": "diff-review",
 "base": "e7839224cff1b7553fb9567109155e805289f0d1",
 "head": "9e0e43aef628987c5a63ec8e0b2ad1fba438b5c7",
 "repo": "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297",
 "intensity": "light",
 "reviewDir": "memory/builds/dClosedLoop/reviews",
 "roles": {
  "diffFinder": "gov-diff-reviewer",
  "skeptic": "gov-skeptic",
  "synthesis": "gov-synthesizer"
 },
 "efforts": {
  "diffFinder": "high",
  "skeptic": "high",
  "synthesis": "high"
 },
 "specs": [
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layers-reviews-compared.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md"
 ],
 "context": "The diff folds two Tier-2 rounds' findings into the four layer design records of build dClosedLoop, a design-only build that re-architects gov onto one loop: the instruction layer (layer-instruction.md), the flow layer (layer-flow.md and flow-steps.md), the roles layer (layer-roles.md) and the memory layer (layer-memory.md). It also moves the sibling records they touch: foundations.md, architecture-v2.md, the gap register, flow-roles.md and the session log, and fills the comparison record's map dispositions. Each layer record's new [revised] table names, per defect tag, where its fix sits. The comparison record's [map-<layer>] tables list each defect with the finding ids behind it, and the eight reports memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-{instruction,flow,roles,memory}-{a,b}.md hold each finding. The owner's answers LR-1 to LR-6 are in the comparison record's [answers]. Review the fold for three things: (1) a [revised] row whose named fix is absent from the section it names, or does not fix the defect its findings describe; (2) fold text that contradicts another statement in the same or a sibling record, including an owner answer misapplied or a later layer's change not carried; (3) new design text that is wrong about the tree, such as a seam, file, line, key or value that does not exist or says otherwise, or a check said to be seen red with no recorded run. Write the report to memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold.md. Its head carries an H1, then, within its first twelve lines, the line `**Serves:** diff-review PLAY-dClosedLoop-1`. It carries exactly one `## Verdict:` line, whose token is CLEAN, CLEAN WITH FIXES or BLOCKED and nothing else.",
 "byDesign": "- The build is design-only: no product code and no unit specs. Unit-level detail is absent by design and owed to the chain builds.\n- The owner's settled answers (F*, R-*, RT-*, LR-*) are decisions: a finding may show that one contradicts a record or the tree, but does not re-argue the owner's choice.\n- A defect whose [revised] disposition is `none` was refuted by the rounds' skeptics; re-reporting it is out of scope unless the fold made it true.\n- Dated records keep what held when they were written: research returns, snapshots, revision notes and the session log's past entries.\n- Generated files (memory/LIVE.md and the build README's generated regions) are rendered and not under review.",
 "checklist": "# recurring-bug-class checklist for e7839224c..9e0e43aef (12 changed file(s))\n- two-answers-to-one-question (universal)\n  a fact stated in two places drifts, and the copies need not disagree loudly to be wrong\n- amendment-leaves-its-other-half-standing (directory)\n  a criterion is amended and the clause, scope item or log line that only made sense under the old wording is left behind, so one rule now returns two verdicts\n- fixture-passes-by-finding-nothing (universal)\n  a test arm whose fixture never triggers the rule passes, and proves nothing\n- retirement-inventory-misses-readers-by-value (directory)\n  an inventory of what reads a retired thing, built by searching for its name, misses every assertion on a count or a value that thing carries, because those name nothing\n- staged-break-substitutes-a-synthetic-value (universal)\n  an arm that proves a mechanism by replacing the shipped value with a simpler one proves the mechanism for the simpler value\n- inline-fence-swallows-the-rest-of-the-file (universal)\n  a triple-backtick written inline in prose opens a fence the reader never closes, so every section after it silently disappears from the checker's view"
}
```

### The follow-up round's args

Dispatch 48, run as `wf_e26eda01-523`: round 2 over the fixes, handed round 1's confirmed set in the harness's own shape, trimmed to the fields its prompt reads. Verbatim:

```json
{
 "kind": "diff-review",
 "base": "9e0e43aef628987c5a63ec8e0b2ad1fba438b5c7",
 "head": "2e6f9aa1b100aa190d2099fcc990a0a2292f98b2",
 "repo": "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297",
 "round": 2,
 "priorFindings": [
  {
   "id": 1,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:250",
   "claim": "The fix for `flakes-quarantine-seam` puts `test.flakes` on the wrong branch. It is reached only from `test.verdict`'s green outcome, but the bar prints `nondeterministic · <leg>` only on a run it has already turned red.",
   "severity": "high"
  },
  {
   "id": 2,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:297",
   "claim": "`deploy.core` is called 'the lander's post-merge bar', with 'clean → deploy.record'. The lander starts that bar only on its exit-0 path, starts it detached, and records no result. This tree also declares no `GATE_POST_MERGE`.",
   "severity": "high"
  },
  {
   "id": 3,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:296",
   "claim": "`deploy.land` claims to push 'the prepared merge and nothing else, reusing its verdict', with 'the tip moved → Test' as its own outcome. On a push race, though, `--land` re-prepares onto the new tip and pushes that new merge itself, and it never returns a 'tip moved' class.",
   "severity": "medium"
  },
  {
   "id": 4,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:405",
   "claim": "The build's transition table lacks transitions that the folded items route. The engine 'refuses any transition the table lacks', so those routes cannot be taken.",
   "severity": "medium"
  },
  {
   "id": 5,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:294",
   "claim": "C1: the owner's landing gate is placed in two incompatible spots. `deploy.mandate` checks 'the owner's landing gate before it' and is proven by 'the gate's witness'. Lines 319 and 348 put that gate 'before `deploy.parents`', which is after `deploy.mandate`.",
   "severity": "medium"
  },
  {
   "id": 6,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:340",
   "claim": "C1, LR-3 misapplied: 'An owner breakpoint is an owner item. It parks the build, and resolves as `run.on-owner-question` says.' Under the default `best-effort-recorded` no build parks, and `park-build` is only one of four values.",
   "severity": "medium"
  },
  {
   "id": 7,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:389",
   "claim": "C1: there are two copies of the mailbox-prune rule, and they disagree. `deploy.release` prunes the mailbox ref 'once the build folder holds every disposed message'. `life.release` 'deletes the leases and the mailbox ref' with no such condition.",
   "severity": "medium"
  },
  {
   "id": 8,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:804",
   "claim": "C1: v2's dDeclaredLoop row was edited by the fold, which added `gap-flow-15`, but it still specifies 'a default failure route (the refusal recorded, `next` naming the first unwitnessed item)'. That is the wording the `first-unwitnessed-item` defect retired.",
   "severity": "low"
  },
  {
   "id": 9,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:35",
   "claim": "Under LR-5, every ask a core item files must use one of four mechanical acceptance forms: a red, an unverified finding, a stray or a repair. But several core items here file asks that fit none of the four.",
   "severity": "medium"
  },
  {
   "id": 10,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:38",
   "claim": "C1: flow-steps' copy of the mechanical acceptance forms has drifted from memory [asks]:441-444, its source. Here a red is 'the leg green on the default branch' (memory: 'a later green of the same leg'), and a stray is 'the stray claimed' (memory: 'the path claimed or reverted').",
   "severity": "low"
  },
  {
   "id": 11,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:314",
   "claim": "The fix for `record-concurrent-mint` mints every id 'under the build's lease'. But the flow writes the first records of a build before any build lease exists, and the slug that the lease is keyed by is itself minted by `record`.",
   "severity": "medium"
  },
  {
   "id": 12,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:622",
   "claim": "Under LR-6, a build lands its `gov:feature` anchor while its reuse entry is only 'proposed or accepted', and the check runs both ways. No rule covers the owner rejecting the proposal after the build has landed.",
   "severity": "medium"
  },
  {
   "id": 15,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-session-log.md:801",
   "claim": "C1: 'All four layers are folded: 206 defects placed, and every map row's disposition set' gives a different total from the per-layer entries above it and from the comparison record. Those count 54 + 61 + 39 + 73 = 227 placed defects, and [folded] tallies 227 rows.",
   "severity": "low"
  },
  {
   "id": 16,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:221",
   "claim": "The `policy-lists-incomplete` fix is still incomplete for `flow.route-backs`. [rules]:32-34 says every route back counts against it, yet only the breakpoint's policy list (line 374) names it.",
   "severity": "low"
  },
  {
   "id": 17,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:296",
   "claim": "deploy.land's exit routes misread the lander. On exit 4 the route goes to deploy.core and then deploy.record, but the lander exits 4 before it writes the marker or starts the post-merge bar. And exit 1 also covers a push that landed but could not be recorded, yet it is routed back to Test to prepare again.",
   "severity": "high"
  },
  {
   "id": 18,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:297",
   "claim": "deploy.core's actor is 'the lander's post-merge bar (GATE_POST_MERGE)', but that bar is optional and fire-and-forget, and it is not declared on this tree at all. The item's witness has no producer to read and no route for the case where no result ever arrives.",
   "severity": "medium"
  },
  {
   "id": 19,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:253",
   "claim": "test.flakes never reads `verdict.flakes`. It always turns a leg past the threshold into a held leg, and it uses `verdict.held` as the quarantine carrier, although that key only sets when held legs run.",
   "severity": "medium"
  },
  {
   "id": 20,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:405",
   "claim": "The new [transitions] table does not cover routes the Plan program declares. Triage's defer, retire and refuse, `plan.dedupe`'s duplicate route back to `entry.place`, and a triage-selected ask entering Plan have no row, and none of them has a terminal state.",
   "severity": "medium"
  },
  {
   "id": 21,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:35",
   "claim": "[rules] closes every ask a core item files to the four mechanical acceptances (LR-5), but the programs' own items file asks that fit none of the four.",
   "severity": "medium"
  },
  {
   "id": 22,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:804",
   "claim": "C2: the fold edited dDeclaredLoop's row (adding gap-flow-15) but left its default failure route as '`next` naming the first unwitnessed item'. flow-steps [rules] was amended (`first-unwitnessed-item`) so that `next` returns the frontier.",
   "severity": "medium"
  },
  {
   "id": 23,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md:36",
   "claim": "C2: the fold made `test.verdict` runner-written ('the runner writes the verdict record for the tree, which the pre-push hook reads', `hook-actor-kind`). It left four carriers of the hook-written verdict standing: layer-flow's Test row ('the declared backend's hook-written verdict'), v2 [contracts]' Test row (v2:788), dWitnessedBar's planned unit 'the hook-written verdict' (v2:809), and flow-roles:95.",
   "severity": "medium"
  },
  {
   "id": 24,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md:242",
   "claim": "C2: the fold concluded that no landing queue exists, because the turnstile is a host-wide bar semaphore that push-main.sh never takes (gap-flow-08; flow-steps [deploy]). flow-roles still settles that 'Landings on a node pass through the turnstile landing queue that already exists', and its [closed] H7 row repeats 'the existing turnstile landing queue'. layer-runtime:892 also still gives dShippedRelease 'the turnstile queue'.",
   "severity": "medium"
  },
  {
   "id": 25,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md:54",
   "claim": "C2: the fold amended flow-roles [cycle] step 2 so that the prompt writer receives the resolved work order with inputs as keyed content (`cycle-amendment`). The roles record's own summary of that cycle still says 'The driver hands the prompt writer the item's details, with references to its input records', although the fold edited the bullet just above it (line 47).",
   "severity": "low"
  },
  {
   "id": 26,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md:446",
   "claim": "Two carriers are named for the same load-point budget. Instruction R-C says the budgets extend `tools/template-size-limits.txt` and 'a new load point joins that table'. The roles fold says a role's static block's budget is `check_roles.py`'s `BODY_CEILINGS`, 'one carrier' (layer-roles:376, R3-A).",
   "severity": "medium"
  },
  {
   "id": 28,
   "lens": "verification",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:628",
   "claim": "C3: The `[annotations]` resolve check is built on a drift-audit signal that cannot fail. `source_cited_ids_resolving_to_no_record` is report-only (`gateable: False`), and its RATCHETS row only guards raising the pin. The signal counts record ids matched by the id grammar, so it never reads a `refs=<path>` or a `gov:feature` tag. The fold's own fix for `annotation-green-vacuous` (row 1043), 'seen red on a planted reference', therefore has no red to observe.",
   "severity": "medium"
  },
  {
   "id": 29,
   "lens": "verification",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md:1159",
   "claim": "C3: The revised `role_matrix.py` drops every item row under a heading outside its hard-coded STEPS list without any message. It asserts no item population, so all three arms pass by not reading the rows.",
   "severity": "medium"
  },
  {
   "id": 30,
   "lens": "verification",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:415",
   "claim": "The new `[transitions]` table says 'the engine refuses any transition the table lacks', yet it lacks routes that the folded items declare. No check joins the items' `Then` cells to the table.",
   "severity": "medium"
  },
  {
   "id": 31,
   "lens": "verification",
   "ref": "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layers-reviews-compared-instruments.md:950",
   "claim": "`tally_folded.py`'s only refusal, an unknown disposition, was never seen red, and none of its runs is recorded. `set_dispositions.py` beside it has both reds recorded.",
   "severity": "low"
  }
 ],
 "intensity": "light",
 "reviewDir": "memory/builds/dClosedLoop/reviews",
 "roles": {
  "diffFinder": "gov-diff-reviewer",
  "skeptic": "gov-skeptic",
  "synthesis": "gov-synthesizer"
 },
 "efforts": {
  "diffFinder": "high",
  "skeptic": "high",
  "synthesis": "high"
 },
 "specs": [
  "memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layers-reviews-compared.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md"
 ],
 "context": "The follow-up round of the closing review of build dClosedLoop's fold, a design-only build that re-architects gov onto one loop. Round 1 (memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold.md) reviewed the fold of two Tier-2 rounds into the four layer records and found 28 confirmed findings in 24 items, handed here as priorFindings. This diff is the fix of those items, plus the owner's LR-7 answer, plus the dispatch record: flow-steps.md (the Test and Deploy items, the transition table, the breakpoint, the mailbox rule), the memory, instruction and roles records, layer-flow, flow-roles, the runtime record, v2, the gap register, the session log, the comparison record's [closing-review] table, the instruments record, role_matrix.py's arm 0 inside the roles record, and three new bug-class records under memory/gotchas/. Review it for three things: (1) a prior finding whose fix is absent, partial, or not what the [closing-review] table says it is; (2) fix text that introduces a new defect: a route, outcome, witness or carrier the named actor never produces, a statement that contradicts another record, or an owner answer misapplied; (3) a check said to be seen red with no recorded run, or a new gotcha record whose anchors or resolution do not hold. Write the report to memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold-followup.md. Its head carries an H1, then, within its first twelve lines, the line `**Serves:** diff-review PLAY-dClosedLoop-1`. It carries exactly one `## Verdict:` line, whose token is CLEAN, CLEAN WITH FIXES or BLOCKED and nothing else.",
 "byDesign": "- The build is design-only: no product code and no unit specs. Unit-level detail is absent by design and owed to the chain builds.\n- The owner's settled answers (F*, R-*, RT-*, LR-1 to LR-7) are decisions: a finding may show that one contradicts a record or the tree, but does not re-argue the owner's choice.\n- Round 1's refuted findings (ids 13, 14 and 27) are out of scope unless the fix made them true.\n- Dated records keep what held when they were written: research returns, snapshots, revision notes and the session log's past entries.\n- Generated files (memory/LIVE.md, the build README's generated regions and memory/gotchas/INDEX.md) are rendered and not under review.",
 "checklist": "# recurring-bug-class checklist for 9e0e43aef..2e6f9aa1b (18 changed file(s))\n# 10 class(es) selected by an anchor + 6 universal\n# by anchor specificity: 3 path · 4 directory · 3 basename; a cut tier prints one line per class\n# invariants are read at 9e0e43aef628; 0 that this subject adds, edits or takes out are listed as items, never by design\n\n- [ ] fixture-passes-by-finding-nothing (universal)\n      a test arm whose fixture never triggers the rule passes, and proves nothing\n      memory/gotchas/fixture-passes-by-finding-nothing.md\n\n- [ ] guard-above-a-fold-makes-its-fallback-dead (universal)\n      a guard added above a fold settles the predicate the fold's own fallback re-tests, leaving a dead arm that reads as coverage\n      memory/gotchas/guard-above-a-fold-makes-its-fallback-dead.md\n\n- [ ] heredoc-escape-reaches-the-regex (universal)\n      source written through a shell heredoc into a non-raw string turns an escape into a control byte, and the symptom never looks like a quoting problem\n      memory/gotchas/heredoc-escape-reaches-the-regex.md\n\n- [ ] inline-fence-swallows-the-rest-of-the-file (universal)\n      a triple-backtick written inline in prose opens a fence the reader never closes, so every section after it silently disappears from the checker's view\n      memory/gotchas/inline-fence-swallows-the-rest-of-the-file.md\n\n- [ ] staged-break-substitutes-a-synthetic-value (universal)\n      an arm that proves a mechanism by replacing the shipped value with a simpler one proves the mechanism for the simpler value\n      memory/gotchas/staged-break-substitutes-a-synthetic-value.md\n\n- [ ] two-answers-to-one-question (universal)\n      a fact stated in two places drifts, and the copies need not disagree loudly to be wrong\n      memory/gotchas/two-answers-to-one-question.md\n\n- [ ] parser-drops-rows-it-cannot-place (path)\n      a record-parsing instrument skips rows under a heading or key it does not know and still prints a clean run, so its population shrinks without a word\n      memory/gotchas/parser-drops-rows-it-cannot-place.md\n\n- [ ] owner-item-without-its-reject-outcome (path)\n      a design hands a decision to the owner and routes only the yes, so a no leaves landed work with no route and a check that turns red on the default branch\n      memory/gotchas/owner-item-without-its-reject-outcome.md\n\n- [ ] route-names-an-output-its-actor-never-emits (path)\n      a designed route or witness names an output, exit class or record that its actor never produces on that path, so the route is dead or waits forever\n      memory/gotchas/route-names-an-output-its-actor-never-emits.md\n\n- [ ] a-merge-of-the-default-branch-read-as-additions (directory)\n      a check that lists the files a range or a commit ADDS reads a merge of the default branch into a feature branch as adding every file the default branch gained, unless its git invocation is one of the shapes that cannot\n      memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md\n\n- [ ] amendment-leaves-its-other-half-standing (directory)\n      a criterion is amended and the clause, scope item or log line that only made sense under the old wording is left behind, so one rule now returns two verdicts\n      memory/gotchas/amendment-leaves-its-other-half-standing.md\n\n- [ ] ledger-token-wrapped-across-a-line-joins-nothing (directory)\n      hygiene check 23 extracts a ledger line's backticked tokens PER LINE, so a token the writer wrapped across a line break belongs to no line and the criterion it answers reads as unanswered\n      memory/gotchas/ledger-token-wrapped-across-a-line-joins-nothing.md\n\n- [ ] retirement-inventory-misses-readers-by-value (directory)\n      an inventory of what reads a retired thing, built by searching for its name, misses every assertion on a count or a value that thing carries, because those name nothing\n      memory/gotchas/retirement-inventory-misses-readers-by-value.md\n\n- [ ] record-without-serves-or-with-a-round-counter (basename)\n      a new build record owes a Serves line and a filename that projects it, and a round counter in that filename mints an id nothing defines\n      memory/gotchas/record-without-serves-or-with-a-round-counter.md\n\n- [ ] a-folded-field-leaves-its-row-shape-docs-behind (basename)\n      a review fold adds a key to a declared row shape in the code and its gate, and the spec body and the README that describe that shape keep the old key set\n      memory/gotchas/a-folded-field-leaves-its-row-shape-docs-behind.md\n\n- [ ] git-rm-cached-refuses-a-diverged-index-blob (basename)\n      `git rm --cached` refuses a path whose index blob differs from both HEAD and the worktree, so a fixture cleanup without `-f` silently leaves the file staged and the next arm measures the wrong fixture\n      memory/gotchas/git-rm-cached-refuses-a-diverged-index-blob.md\n\n# by design — 0 invariant(s) this selection touches"
}
```
