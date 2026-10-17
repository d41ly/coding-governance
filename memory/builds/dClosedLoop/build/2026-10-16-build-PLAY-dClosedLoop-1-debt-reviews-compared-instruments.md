# The review debt's runs: the args and the script that wrote them

**Serves:** research PLAY-dClosedLoop-1

The args of dispatches 61 to 72, written by the script below from the tree, the six bug-class checklists
and the three saved workflow runs whose ledgers give the prior sets. The runs and their comparison are in
`build/2026-10-16-build-PLAY-dClosedLoop-1-debt-reviews-compared.md`.

## [builder] The script that writes the args

Each checklist is `gotchas.py --for-paths` over a spec audit's record, or `gotchas.py --for-diff` over a
fold's range, run at `388dfc665`.

```python
"""Write the args of the six unreviewed pieces' reviews, two independent runs each, at medium effort, as the
owner asked on 2026-10-16: "fix everything that's stale, then review all 6 unreviewed pieces - medium
effort, twice each."

- The lexicon and the review system are design records no review read: a spec audit each, round 1, full,
  shaped as the layers' audits (dispatches 39 to 46).
- The four folds are commit ranges: a light diff review each, shaped as the fold reviews before them
  (dispatches 47, 48, 50, 59, 60). A fold that answers an earlier round's findings is that chain's next
  round, handed that round's confirmed set, from its workflow's own ledger, as `priorFindings`.

Runs A and B share every field but the run label, the report path and the spec audit's scratch directory.
Usage: python make_debt_args.py <out-dir>   (from the worktree root)
Refuses unless every prior ledger's confirmed rows equal its run's confirmed count.
"""
import json
import pathlib
import subprocess
import sys

OUT = pathlib.Path(sys.argv[1])
REPO = "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297"
SP = ("C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/"
      "1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad")
WF = ("C:/Users/d41ly/.claude/projects/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/"
      "1799cb98-0882-4ab8-a308-19495d2a487a/workflows/")
B = "memory/builds/dClosedLoop/build/2026-10-1"
RV = "memory/builds/dClosedLoop/reviews/2026-10-1"


def rec(date, name):
    return f"{B}{date}-build-PLAY-dClosedLoop-1-{name}.md"


def rev(date, name):
    return f"{RV}{date}-review-PLAY-dClosedLoop-1-{name}.md"


def git(*a):
    return subprocess.run(["git", "-C", REPO, *a], capture_output=True, text=True, check=True).stdout.strip()


def prior(run):
    """The confirmed set of a saved workflow run, in the harness's own shape, trimmed to what its prompt reads."""
    d = json.load(open(WF + run + ".json", encoding="utf-8"))
    res = d["result"] if isinstance(d["result"], dict) else json.loads(d["result"])
    out = [{"id": x["id"], "lens": x["lens"], "ref": x["ref"], "claim": x["claim"],
            "severity": x.get("skepticSeverity") or x["severity"]}
           for x in res["ledger"] if x["verdict"] == "confirmed"]
    if len(out) != res["confirmed"]:
        sys.exit(f"{run}: {len(out)} confirmed rows where the run reports {res['confirmed']}")
    return out


V2, GAPS = rec("4", "architecture-v2"), rec("4", "gap-register")
STEPS, FLOW = rec("5", "flow-steps"), rec("5", "layer-flow")
ROLES, MEM, RT = rec("5", "layer-roles"), rec("5", "layer-memory"), rec("5", "layer-runtime")
INSTR, LIB, EXP = rec("5", "layer-instruction"), rec("6", "layer-library"), rec("6", "layer-expansions")
OWNER = ("The owner asked for two independent medium-effort Tier-2 rounds on each of six pieces of the design that "
         "no review had read, their results compared; this is run {run}, and the other run's report is not "
         "evidence, so do not open it.")
TAIL = ("Write the report to {report}. Its head carries an H1, then, within its first twelve lines, the line "
        "`**Serves:** {kind} PLAY-dClosedLoop-1`. It carries exactly one `## Verdict:` line, whose token is CLEAN, "
        "CLEAN WITH FIXES or BLOCKED and nothing else.")
AT_HEAD = ("The worktree is at a later HEAD, and later commits changed some of this text: verify each finding against "
           "the file at HEAD, cite HEAD's line, and report a defect only if HEAD still carries it.")
KNOWLEDGE = ("- Records written before 2026-10-16 that say Knowledge mean memory's library side (layer-library "
             "[settled], \"Older records' wording\").")
GENERATED = ("- Generated files (memory/LIVE.md, the build README's generated regions, memory/map/generated/ and "
             "memory/gotchas/INDEX.md) are rendered and not under review.\n"
             "- The atlas page and its generator are an owner-facing view outside this review.")
ANSWERS = ("RH-1, PIN-1, EX-1 to EX-3, DI-1, KN-1, LB-1 to LB-4, L-1 to L-6, the review system's R-1 to R-3, and the "
           "earlier F*, FR-*, FI-*, S-*, LR-* and RT-*")
DIFF_BY_DESIGN = (
    "- The build is design-only: no product code and no unit specs. Unit-level detail is absent by design and owed "
    "to the chain builds.\n"
    f"- The owner's settled answers ({ANSWERS}) are decisions: a finding may show one contradicts a record or the "
    "tree, but does not re-argue the owner's choice.\n"
    "- Dated records keep what held when they were written: research returns, revision notes (the 2026-10-16 stale "
    "sweep's included), [forks], [settled], [review] and the session log's past entries.\n"
    f"{KNOWLEDGE}\n"
    "- A refuted finding stays refuted: the comparison records' none rows carry the skeptic's reason.\n"
    f"{GENERATED}")
SPEC_BY_DESIGN = (
    "- The build is design-only: no product code and no unit specs; each chain build writes its own specs later, so "
    "unit-level implementation detail is absent by design.\n"
    "- The owner's settled answers, recorded in the record's answer sections, are decisions: a finding may show that "
    "one contradicts another record, the platform or the tree, but does not re-argue the owner's choice.\n"
    "- Records outside memory/builds/dClosedLoop/ are not under review, and the research returns are evidence, not "
    "subjects.\n"
    f"{KNOWLEDGE}\n"
    f"{GENERATED}")
SIX = ("Audit the record as an architecture spec, against six questions: (1) internal consistency: do its "
       "components, policies, build units, gaps and answers agree with each other; (2) consistency with the sibling "
       "records in specs: v2's principles, policy catalogue and chain, and the layers' records; (3) feasibility "
       "against the measured facts in the research returns, the records in specs and the tree: a mechanism the "
       "platform or the tree cannot support, or a claim the evidence does not bear out; (4) missing mechanisms: "
       "{missing}; (5) claims that are unenforced or untestable as written; (6) extension points, {ext}, that could "
       "not in fact be filled without changing code. Address each finding by the record's section tag, such as "
       "{tags}.")

PIECES = []

# 1. The lexicon: a design record no review read.
PIECES.append(dict(
    key="lexicon", kind="spec-audit", subject=rec("5", "lexicon"),
    specs=[V2, LIB, MEM, INSTR, STEPS, RT, EXP, GAPS] + [rec("5", f"research-lexicon-{p}") for p in
                                                       ("kit", "population", "instruments", "prior-art")],
    context=("The subject is the lexicon's design record for build dClosedLoop, a design-only build that re-architects "
             "gov onto one loop. The owner asked for a full review of the lexicon kit under the new architecture "
             "([words]), and settled its forks L-1 to L-6 in the record's own answer table. No review has read this "
             "record. " + OWNER + " Records settled after this record was written are among the specs: the library "
             "side (KN-1 folded the Knowledge expansion into the memory layer, and the lexicon is one of memory's "
             "optional components), the expansion round and the runtime layer. A statement here that a later record "
             "changed or contradicts is a finding. " +
             SIX.format(missing="anything the lexicon must provide to the flow, the roles or the other layers that "
                                "the design omits", ext="such as a pack or a definition class",
                        tags="[settled], [current], [fit], [design], [gaps-proposed] and [forks]") + " " + TAIL),
    by_design=SPEC_BY_DESIGN, checklist="cl-lexicon.txt"))

# 2. The review system: a design record no review read.
PIECES.append(dict(
    key="review-system", kind="spec-audit", subject=rec("5", "review-system"),
    specs=[V2, STEPS, FLOW, ROLES, RT, GAPS, rec("6", "layers-reviews-compared"),
           rec("5", "research-review-lenses"), rec("5", "research-review-adjudication")],
    context=("The subject is the review system's design record for build dClosedLoop, a design-only build that "
             "re-architects gov onto one loop. While the layer reviews ran, the owner asked whether gov's rework needs "
             "opt-in review lenses and whether the skeptics' and the synthesizer's instructions need changing "
             "([words]). Two researchers measured gov's review history, and the owner settled the record's forks "
             "R-1 to R-3 in [answers]. No review has read this record. " + OWNER + " Records settled after this "
             "record was written are among the specs: the flow's breakpoint items, the roles and runtime layers, and "
             "the comparison of the layer rounds. A statement here that a later record changed or contradicts is a "
             "finding. " +
             SIX.format(missing="anything review must provide to the flow's breakpoint, the roles or the runtime "
                                "that the design omits", ext="such as an opt-in lens",
                        tags="[current], [design], [stale], [gaps-proposed], [forks] and [answers]") + " " + TAIL),
    by_design=SPEC_BY_DESIGN, checklist="cl-review-system.txt"))

# 3. The runtime round's fold and its two settlements: round 1 of the fold's own review.
RA, RB = rev("5", "runtime-a"), rev("5", "runtime-b")
RCMP = rec("5", "runtime-reviews-compared")
PIECES.append(dict(
    key="runtime-fold", kind="diff-review", base="6cfd21619", head="3611a60e9", round=1, prior=None,
    specs=[RCMP, RT, V2, GAPS, STEPS, ROLES, RA, RB, rec("5", "research-runtime-floor")],
    exclude=[RA, RB, rec("5", "research-runtime-floor-probes"), rec("5", "research-runtime-floor"),
             "memory/builds/dClosedLoop/prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-15-researcher.md",
             "memory/builds/dClosedLoop/README.md"],
    context=("The diff is the runtime layer's fold in build dClosedLoop, a design-only build that re-architects gov "
             "onto one loop, with the two settlements after it. No review has read it: the runtime layer's two Tier-2 "
             f"audits ({RA}, {RB}) read the design before the fold, and the first closing review of a fold came with "
             "the layers round. " + OWNER + " The diff holds three commits. 2dbf8f26f folds the two audits' 59 "
             "defects into layer-runtime (an act session per act, returns that survive any death, binding at the "
             f"call), v2 and the gap register, and compares the rounds in {RCMP}, whose [map] names where each defect "
             "went and whose [neither] lists the main loop's own additions. e30f0acbd settles the runtime forks: "
             "dWellOiledMachine joins the chain with the `next` verb and the owner's controls, and a session starts "
             "fresh at a boundary by default. 3611a60e9 re-verifies RT-2 from a new research return: no CLI floor, "
             "and every version fails closed through ask rules only the dispatcher answers. The two audit reports "
             "and the research returns are handed in as specs and are not under review. Read the diff without them: "
             "git -C {repo} diff {base}...{head} -- . {excl}. " + AT_HEAD + " Review for four things: (1) a confirmed "
             "audit finding the fold left unfixed, fixed only in part, or fixed in a way its own text contradicts, "
             "against [map]'s claim; (2) a defect the fold or a settlement introduced: an item, route, witness, key, "
             "value, record kind or lease with no producer, no arm or no home, or one fact now stated two ways; (3) "
             "a settled answer misapplied, RT-1 to RT-3 among them; (4) text wrong about the tree or the platform. " +
             TAIL),
    by_design=DIFF_BY_DESIGN + "\n- The research returns are evidence, measured when written; RT-2's re-verification "
              "is recorded in research-runtime-floor and its probes.", checklist="cl-runtime-fold.txt"))

# 4. The layers round's follow-up fold: round 3 of that fold's review.
R2L = rev("6", "fold-followup")
LCMP = rec("6", "layers-reviews-compared")
PIECES.append(dict(
    key="fold-round3", kind="diff-review", base="cc4c83ad5", head="1bc4883fe", round=3, prior="wf_e26eda01-523",
    specs=[LCMP, R2L, STEPS, ROLES, MEM, FLOW, rec("5", "flow-roles"), RT, V2, GAPS],
    exclude=[R2L, "memory/gotchas/INDEX.md", "memory/builds/dClosedLoop/README.md"],
    context=("The diff is round 3 of the closing review of the layers round's fold in build dClosedLoop, a "
             "design-only build that re-architects gov onto one loop. Round 1 reviewed the fold of layers 1 to 4. "
             f"Round 2 ({R2L}) reviewed round 1's fixes and returned CLEAN WITH FIXES, 31 of 34 confirmed in 18 items; "
             "its confirmed findings are handed in as priorFindings. No round has read the fold of those 18 items: "
             "the library review's range starts at it. " + OWNER + " The diff is the one commit 1bc4883fe that folds "
             "them: flow-steps, layer-roles, layer-memory, layer-flow, flow-roles, layer-runtime, v2, the gap "
             f"register, three bug classes under memory/gotchas/, and {LCMP} [follow-up], which names where each item "
             "went. Where a fix needed a tool's own enumeration, the design text states the contract and the owning "
             "build's gap carries the enumeration. Read the diff without round 2's report and the generated files: "
             "git -C {repo} diff {base}...{head} -- . {excl}. " + AT_HEAD + " Review for three things: (1) a round-2 "
             "finding the fix leaves standing, fixes in part, or fixes in a way its own text contradicts; (2) a defect "
             "the fix itself introduced: an item, route, witness, key, value, record kind or lease with no producer, "
             "no arm or no home, or one fact now stated two ways; (3) text wrong about the tree, the lander's and the "
             "runner's seams included. " + TAIL),
    by_design=DIFF_BY_DESIGN + "\n- Where a fix needed a tool's own enumeration, the design states the contract and "
              "the owning build's gap carries the enumeration: a missing enumeration in the design is by design, a "
              "contract the gap does not carry is not.", checklist="cl-fold-round3.txt"))

# 5. The library round's fold: round 2 of the library review.
R1LIB = rev("6", "library")
PIECES.append(dict(
    key="library-followup", kind="diff-review", base="d4fc4bb51", head="0dd962724", round=2, prior="wf_9d4cc07b-2f2",
    specs=[LIB, R1LIB, STEPS, MEM, INSTR, ROLES, V2, GAPS],
    exclude=[R1LIB, rec("6", "atlas"), "memory/map/generated", "memory/gotchas/INDEX.md",
             "memory/builds/dClosedLoop/README.md"],
    context=("The diff is round 2 of the library round's review in build dClosedLoop, a design-only build that "
             f"re-architects gov onto one loop. Round 1 ({R1LIB}) reviewed KN-1's fold, the library design and its "
             "settlement, and returned CLEAN WITH FIXES, 25 of 31 confirmed in 19 items; its confirmed findings are "
             "handed in as priorFindings. The owner deferred this follow-up on 2026-10-16 and now asks for it. " +
             OWNER + " The diff is the one commit 0dd962724 that folds them: layer-library's [review-fold] names where "
             "each item went; flow-steps (build.distill writes the major decisions' rows before Test), layer-memory, "
             "layer-instruction, layer-roles, v2, the gap register, and four bug classes filed under memory/gotchas/ "
             "and claimed in memory/map/features/. Read the diff without round 1's report, the atlas and the generated "
             "files: git -C {repo} diff {base}...{head} -- . {excl}. " + AT_HEAD + " Review for three things: (1) a "
             "round-1 finding the fix leaves standing, fixes in part, or fixes in a way its own text contradicts; (2) "
             "a defect the fix itself introduced: an item, route, witness, key, value, record kind or lease with no "
             "producer, no arm or no home, or one fact now stated two ways; (3) text wrong about the tree. " + TAIL),
    by_design=DIFF_BY_DESIGN, checklist="cl-library-followup.txt"))

# 6. The expansion round's follow-up fold: round 3 of the expansion fold's review.
R2X = rev("6", "expansions-fold-followup")
XCMP = rec("6", "expansions-reviews-compared")
PIECES.append(dict(
    key="expansions-fold-round3", kind="diff-review", base="67c79f7cc", head="5e139d377", round=3,
    prior="wf_c69ed990-543",
    specs=[XCMP, R2X, EXP, STEPS, RT, MEM, V2, GAPS],
    exclude=[R2X, "memory/gotchas/INDEX.md", "memory/builds/dClosedLoop/README.md"],
    context=("The diff is round 3 of the closing review of the expansion fold in build dClosedLoop, a design-only "
             f"build that re-architects gov onto one loop. Round 2 ({R2X}) reviewed round 1's fixes and returned "
             "CLEAN WITH FIXES, 24 of 35 confirmed in 14 items; its confirmed findings are handed in as "
             "priorFindings. " + OWNER + " The diff is the one commit 5e139d377 that folds them, and "
             f"{XCMP} [follow-up] names where each item went: the both-runs probe rewritten and every row it flagged "
             "cited; layer-expansions' kits.offer naming and refusing all five govkit target-side sites; "
             "build.release-ceiling with the supervisor's sweep; the event wait fanned out per build; deploy.close "
             "minted under the claim ref; the exit record naming its environment; the keep record. layer-runtime, "
             "flow-steps, layer-memory, v2, the gap register and five bug classes under memory/gotchas/ change with "
             "it. Read the diff without round 2's report and the generated files: git -C {repo} diff "
             "{base}...{head} -- . {excl}. " + AT_HEAD + " Review for three things: (1) a round-2 finding the fix "
             "leaves standing, fixes in part, or fixes in a way its own text contradicts; (2) a defect the fix itself "
             "introduced: an item, route, witness, key, value, record kind or lease with no producer, no arm or no "
             "home, or one fact now stated two ways; (3) text wrong about the tree, govkit's execution sites "
             "included. " + TAIL),
    by_design=DIFF_BY_DESIGN + "\n- For an earlier round's H1 the fold chose the fix that denies by default: the "
              "unattended offer runs nothing from the adopter's tree. For round 2's M8 it chose a new key, "
              "build.release-ceiling, over a second reader for runtime.hold-ceiling. A finding may show either choice "
              "contradicted elsewhere, not re-argue it.", checklist="cl-expansions-fold-round3.txt"))

OUT.mkdir(parents=True, exist_ok=True)
index = []
for p in PIECES:
    cl = (OUT / p["checklist"]).read_bytes().decode("utf-8").replace("\r\n", "\n")
    for run in ("A", "B"):
        report = rev("6", f"{p['key']}-{run.lower()}")
        common = {"repo": REPO, "reviewDir": "memory/builds/dClosedLoop/reviews", "specs": p["specs"],
                  "byDesign": p["by_design"], "checklist": cl}
        if p["kind"] == "spec-audit":
            args = {"kind": "spec-audit", **common,
                    "subjects": [{"path": p["subject"], "blob": git("rev-parse", "HEAD:" + p["subject"])}],
                    "scratch": f"{SP}/review-{p['key']}-{run.lower()}", "round": 1, "intensity": "full",
                    "roles": {"specFinder": "gov-spec-reviewer", "skeptic": "gov-skeptic", "synthesis": "gov-synthesizer"},
                    "efforts": {"specFinder": "medium", "skeptic": "medium", "synthesis": "medium"},
                    "context": p["context"].format(run=run, report=report, kind="spec-audit")}
        else:
            base, head = git("rev-parse", p["base"]), git("rev-parse", p["head"])
            excl = " ".join(f"':(exclude){x}'" for x in p["exclude"])
            args = {"kind": "diff-review", "base": base, "head": head, **common, "round": p["round"],
                    "intensity": "light",
                    "roles": {"diffFinder": "gov-diff-reviewer", "skeptic": "gov-skeptic", "synthesis": "gov-synthesizer"},
                    "efforts": {"diffFinder": "medium", "skeptic": "medium", "synthesis": "medium"},
                    "context": p["context"].format(run=run, report=report, kind="diff-review", repo=REPO, base=base,
                                                   head=head, excl=excl)}
            if p["prior"]:
                args["priorFindings"] = prior(p["prior"])
        missing = [s for s in p["specs"] if not (pathlib.Path(REPO) / s).exists()]
        if missing:
            sys.exit(f"{p['key']}: specs that do not exist: {missing}")
        name = f"args-{p['key']}-{run.lower()}.json"
        with open(OUT / name, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(args, fh, indent=1, ensure_ascii=False)
        index.append(f"{name}: {len(json.dumps(args))} chars, {len(p['specs'])} specs, "
                     f"{len(args.get('priorFindings', []))} prior, round {args['round']}, {args['intensity']}, "
                     f"report {report.rsplit('/', 1)[-1]}")
print("\n".join(index))
```

Its run:

```text
args-lexicon-a.json: 9399 chars, 12 specs, 0 prior, round 1, full, report 2026-10-16-review-PLAY-dClosedLoop-1-lexicon-a.md
args-lexicon-b.json: 9399 chars, 12 specs, 0 prior, round 1, full, report 2026-10-16-review-PLAY-dClosedLoop-1-lexicon-b.md
args-review-system-a.json: 9180 chars, 9 specs, 0 prior, round 1, full, report 2026-10-16-review-PLAY-dClosedLoop-1-review-system-a.md
args-review-system-b.json: 9180 chars, 9 specs, 0 prior, round 1, full, report 2026-10-16-review-PLAY-dClosedLoop-1-review-system-b.md
args-runtime-fold-a.json: 10819 chars, 9 specs, 0 prior, round 1, light, report 2026-10-16-review-PLAY-dClosedLoop-1-runtime-fold-a.md
args-runtime-fold-b.json: 10819 chars, 9 specs, 0 prior, round 1, light, report 2026-10-16-review-PLAY-dClosedLoop-1-runtime-fold-b.md
args-fold-round3-a.json: 28653 chars, 10 specs, 31 prior, round 3, light, report 2026-10-16-review-PLAY-dClosedLoop-1-fold-round3-a.md
args-fold-round3-b.json: 28653 chars, 10 specs, 31 prior, round 3, light, report 2026-10-16-review-PLAY-dClosedLoop-1-fold-round3-b.md
args-library-followup-a.json: 22738 chars, 8 specs, 25 prior, round 2, light, report 2026-10-16-review-PLAY-dClosedLoop-1-library-followup-a.md
args-library-followup-b.json: 22738 chars, 8 specs, 25 prior, round 2, light, report 2026-10-16-review-PLAY-dClosedLoop-1-library-followup-b.md
args-expansions-fold-round3-a.json: 22795 chars, 8 specs, 24 prior, round 3, light, report 2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold-round3-a.md
args-expansions-fold-round3-b.json: 22795 chars, 8 specs, 24 prior, round 3, light, report 2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold-round3-b.md
```

## [pairs] Runs A and B differ only in their labels

```python
"""Runs A and B of each piece share every field but the run label, the report path and a spec audit's
scratch directory.

Usage: python pair_check.py <args-dir>
"""
import json
import sys

D = sys.argv[1].rstrip("/") + "/"
bad = 0
for k in ("lexicon", "review-system", "runtime-fold", "fold-round3", "library-followup", "expansions-fold-round3"):
    a, b = (json.load(open(f"{D}args-{k}-{r}.json", encoding="utf-8")) for r in "ab")
    fields = sorted(x for x in set(a) | set(b) if a.get(x) != b.get(x))
    same = (a["context"].replace(f"{k}-a.md", "@").replace("run A,", "run @,")
            == b["context"].replace(f"{k}-b.md", "@").replace("run B,", "run @,"))
    ok = same and set(fields) <= {"context", "scratch"}
    bad += not ok
    print(f"{k}: fields that differ {fields}; the contexts differ only in the labels: {same}")
sys.exit(1 if bad else 0)
```

Its run:

```text
lexicon: fields that differ ['context', 'scratch']; the contexts differ only in the labels: True
review-system: fields that differ ['context', 'scratch']; the contexts differ only in the labels: True
runtime-fold: fields that differ ['context']; the contexts differ only in the labels: True
fold-round3: fields that differ ['context']; the contexts differ only in the labels: True
library-followup: fields that differ ['context']; the contexts differ only in the labels: True
expansions-fold-round3: fields that differ ['context']; the contexts differ only in the labels: True
```

## [args-lexicon] Run A's args for the lexicon, verbatim

Run B's differ only as `[pairs]` shows.

```json
{
 "kind": "spec-audit",
 "repo": "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297",
 "reviewDir": "memory/builds/dClosedLoop/reviews",
 "specs": [
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md",
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-lexicon-kit.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-lexicon-population.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-lexicon-instruments.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-lexicon-prior-art.md"
 ],
 "byDesign": "- The build is design-only: no product code and no unit specs; each chain build writes its own specs later, so unit-level implementation detail is absent by design.\n- The owner's settled answers, recorded in the record's answer sections, are decisions: a finding may show that one contradicts another record, the platform or the tree, but does not re-argue the owner's choice.\n- Records outside memory/builds/dClosedLoop/ are not under review, and the research returns are evidence, not subjects.\n- Records written before 2026-10-16 that say Knowledge mean memory's library side (layer-library [settled], \"Older records' wording\").\n- Generated files (memory/LIVE.md, the build README's generated regions, memory/map/generated/ and memory/gotchas/INDEX.md) are rendered and not under review.\n- The atlas page and its generator are an owner-facing view outside this review.",
 "checklist": "# recurring-bug-class checklist for 1 path(s) (1 file(s))\n# 9 class(es) selected by an anchor + 6 universal\n# by anchor specificity: 0 path · 5 directory · 4 basename; a cut tier prints one line per class\n# invariants are read from the working tree; with no --base, a record this subject adds or edits can stand as by design\n\n- [ ] fixture-passes-by-finding-nothing (universal)\n      a test arm whose fixture never triggers the rule passes, and proves nothing\n      memory/gotchas/fixture-passes-by-finding-nothing.md\n\n- [ ] guard-above-a-fold-makes-its-fallback-dead (universal)\n      a guard added above a fold settles the predicate the fold's own fallback re-tests, leaving a dead arm that reads as coverage\n      memory/gotchas/guard-above-a-fold-makes-its-fallback-dead.md\n\n- [ ] heredoc-escape-reaches-the-regex (universal)\n      source written through a shell heredoc into a non-raw string turns an escape into a control byte, and the symptom never looks like a quoting problem\n      memory/gotchas/heredoc-escape-reaches-the-regex.md\n\n- [ ] inline-fence-swallows-the-rest-of-the-file (universal)\n      a triple-backtick written inline in prose opens a fence the reader never closes, so every section after it silently disappears from the checker's view\n      memory/gotchas/inline-fence-swallows-the-rest-of-the-file.md\n\n- [ ] staged-break-substitutes-a-synthetic-value (universal)\n      an arm that proves a mechanism by replacing the shipped value with a simpler one proves the mechanism for the simpler value\n      memory/gotchas/staged-break-substitutes-a-synthetic-value.md\n\n- [ ] two-answers-to-one-question (universal)\n      a fact stated in two places drifts, and the copies need not disagree loudly to be wrong\n      memory/gotchas/two-answers-to-one-question.md\n\n- [ ] a-merge-of-the-default-branch-read-as-additions (directory)\n      a check that lists the files a range or a commit ADDS reads a merge of the default branch into a feature branch as adding every file the default branch gained, unless its git invocation is one of the shapes that cannot\n      memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md\n\n- [ ] amendment-leaves-its-other-half-standing (directory)\n      a criterion is amended and the clause, scope item or log line that only made sense under the old wording is left behind, so one rule now returns two verdicts\n      memory/gotchas/amendment-leaves-its-other-half-standing.md\n\n- [ ] insert-after-a-key-that-occurs-twice (directory)\n      a record edit inserts a row after the first match of a cell value that occurs in two tables, so the row lands in the wrong table and the right one never gains it\n      memory/gotchas/insert-after-a-key-that-occurs-twice.md\n\n- [ ] ledger-token-wrapped-across-a-line-joins-nothing (directory)\n      hygiene check 23 extracts a ledger line's backticked tokens PER LINE, so a token the writer wrapped across a line break belongs to no line and the criterion it answers reads as unanswered\n      memory/gotchas/ledger-token-wrapped-across-a-line-joins-nothing.md\n\n- [ ] retirement-inventory-misses-readers-by-value (directory)\n      an inventory of what reads a retired thing, built by searching for its name, misses every assertion on a count or a value that thing carries, because those name nothing\n      memory/gotchas/retirement-inventory-misses-readers-by-value.md\n\n- [ ] owner-item-without-its-reject-outcome (basename)\n      a design hands a decision to the owner and routes only the yes, so a no leaves landed work with no route and a check that turns red on the default branch\n      memory/gotchas/owner-item-without-its-reject-outcome.md\n\n- [ ] policy-value-with-no-route (basename)\n      a policy key catalogues a value that no item reading the key routes or witnesses, so a preset that selects the value cannot run\n      memory/gotchas/policy-value-with-no-route.md\n\n- [ ] rate-quoted-without-its-denominator (basename)\n      a rate put to the owner in a fork divides by the wrong population, so the option's own cost reads several times off\n      memory/gotchas/rate-quoted-without-its-denominator.md\n\n- [ ] record-without-serves-or-with-a-round-counter (basename)\n      a new build record owes a Serves line and a filename that projects it, and a round counter in that filename mints an id nothing defines\n      memory/gotchas/record-without-serves-or-with-a-round-counter.md\n\n# by design — 0 invariant(s) this selection touches\n",
 "subjects": [
  {
   "path": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md",
   "blob": "424d2a7dee1d47bf5cc11b8702333bb075795fd3"
  }
 ],
 "scratch": "C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/review-lexicon-a",
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
 "context": "The subject is the lexicon's design record for build dClosedLoop, a design-only build that re-architects gov onto one loop. The owner asked for a full review of the lexicon kit under the new architecture ([words]), and settled its forks L-1 to L-6 in the record's own answer table. No review has read this record. The owner asked for two independent medium-effort Tier-2 rounds on each of six pieces of the design that no review had read, their results compared; this is run A, and the other run's report is not evidence, so do not open it. Records settled after this record was written are among the specs: the library side (KN-1 folded the Knowledge expansion into the memory layer, and the lexicon is one of memory's optional components), the expansion round and the runtime layer. A statement here that a later record changed or contradicts is a finding. Audit the record as an architecture spec, against six questions: (1) internal consistency: do its components, policies, build units, gaps and answers agree with each other; (2) consistency with the sibling records in specs: v2's principles, policy catalogue and chain, and the layers' records; (3) feasibility against the measured facts in the research returns, the records in specs and the tree: a mechanism the platform or the tree cannot support, or a claim the evidence does not bear out; (4) missing mechanisms: anything the lexicon must provide to the flow, the roles or the other layers that the design omits; (5) claims that are unenforced or untestable as written; (6) extension points, such as a pack or a definition class, that could not in fact be filled without changing code. Address each finding by the record's section tag, such as [settled], [current], [fit], [design], [gaps-proposed] and [forks]. Write the report to memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-lexicon-a.md. Its head carries an H1, then, within its first twelve lines, the line `**Serves:** spec-audit PLAY-dClosedLoop-1`. It carries exactly one `## Verdict:` line, whose token is CLEAN, CLEAN WITH FIXES or BLOCKED and nothing else."
}
```

## [args-review-system] Run A's args for the review system, verbatim

Run B's differ only as `[pairs]` shows.

```json
{
 "kind": "spec-audit",
 "repo": "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297",
 "reviewDir": "memory/builds/dClosedLoop/reviews",
 "specs": [
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md",
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layers-reviews-compared.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-review-lenses.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-review-adjudication.md"
 ],
 "byDesign": "- The build is design-only: no product code and no unit specs; each chain build writes its own specs later, so unit-level implementation detail is absent by design.\n- The owner's settled answers, recorded in the record's answer sections, are decisions: a finding may show that one contradicts another record, the platform or the tree, but does not re-argue the owner's choice.\n- Records outside memory/builds/dClosedLoop/ are not under review, and the research returns are evidence, not subjects.\n- Records written before 2026-10-16 that say Knowledge mean memory's library side (layer-library [settled], \"Older records' wording\").\n- Generated files (memory/LIVE.md, the build README's generated regions, memory/map/generated/ and memory/gotchas/INDEX.md) are rendered and not under review.\n- The atlas page and its generator are an owner-facing view outside this review.",
 "checklist": "# recurring-bug-class checklist for 1 path(s) (1 file(s))\n# 9 class(es) selected by an anchor + 6 universal\n# by anchor specificity: 0 path · 5 directory · 4 basename; a cut tier prints one line per class\n# invariants are read from the working tree; with no --base, a record this subject adds or edits can stand as by design\n\n- [ ] fixture-passes-by-finding-nothing (universal)\n      a test arm whose fixture never triggers the rule passes, and proves nothing\n      memory/gotchas/fixture-passes-by-finding-nothing.md\n\n- [ ] guard-above-a-fold-makes-its-fallback-dead (universal)\n      a guard added above a fold settles the predicate the fold's own fallback re-tests, leaving a dead arm that reads as coverage\n      memory/gotchas/guard-above-a-fold-makes-its-fallback-dead.md\n\n- [ ] heredoc-escape-reaches-the-regex (universal)\n      source written through a shell heredoc into a non-raw string turns an escape into a control byte, and the symptom never looks like a quoting problem\n      memory/gotchas/heredoc-escape-reaches-the-regex.md\n\n- [ ] inline-fence-swallows-the-rest-of-the-file (universal)\n      a triple-backtick written inline in prose opens a fence the reader never closes, so every section after it silently disappears from the checker's view\n      memory/gotchas/inline-fence-swallows-the-rest-of-the-file.md\n\n- [ ] staged-break-substitutes-a-synthetic-value (universal)\n      an arm that proves a mechanism by replacing the shipped value with a simpler one proves the mechanism for the simpler value\n      memory/gotchas/staged-break-substitutes-a-synthetic-value.md\n\n- [ ] two-answers-to-one-question (universal)\n      a fact stated in two places drifts, and the copies need not disagree loudly to be wrong\n      memory/gotchas/two-answers-to-one-question.md\n\n- [ ] a-merge-of-the-default-branch-read-as-additions (directory)\n      a check that lists the files a range or a commit ADDS reads a merge of the default branch into a feature branch as adding every file the default branch gained, unless its git invocation is one of the shapes that cannot\n      memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md\n\n- [ ] amendment-leaves-its-other-half-standing (directory)\n      a criterion is amended and the clause, scope item or log line that only made sense under the old wording is left behind, so one rule now returns two verdicts\n      memory/gotchas/amendment-leaves-its-other-half-standing.md\n\n- [ ] insert-after-a-key-that-occurs-twice (directory)\n      a record edit inserts a row after the first match of a cell value that occurs in two tables, so the row lands in the wrong table and the right one never gains it\n      memory/gotchas/insert-after-a-key-that-occurs-twice.md\n\n- [ ] ledger-token-wrapped-across-a-line-joins-nothing (directory)\n      hygiene check 23 extracts a ledger line's backticked tokens PER LINE, so a token the writer wrapped across a line break belongs to no line and the criterion it answers reads as unanswered\n      memory/gotchas/ledger-token-wrapped-across-a-line-joins-nothing.md\n\n- [ ] retirement-inventory-misses-readers-by-value (directory)\n      an inventory of what reads a retired thing, built by searching for its name, misses every assertion on a count or a value that thing carries, because those name nothing\n      memory/gotchas/retirement-inventory-misses-readers-by-value.md\n\n- [ ] owner-item-without-its-reject-outcome (basename)\n      a design hands a decision to the owner and routes only the yes, so a no leaves landed work with no route and a check that turns red on the default branch\n      memory/gotchas/owner-item-without-its-reject-outcome.md\n\n- [ ] policy-value-with-no-route (basename)\n      a policy key catalogues a value that no item reading the key routes or witnesses, so a preset that selects the value cannot run\n      memory/gotchas/policy-value-with-no-route.md\n\n- [ ] rate-quoted-without-its-denominator (basename)\n      a rate put to the owner in a fork divides by the wrong population, so the option's own cost reads several times off\n      memory/gotchas/rate-quoted-without-its-denominator.md\n\n- [ ] record-without-serves-or-with-a-round-counter (basename)\n      a new build record owes a Serves line and a filename that projects it, and a round counter in that filename mints an id nothing defines\n      memory/gotchas/record-without-serves-or-with-a-round-counter.md\n\n# by design — 0 invariant(s) this selection touches\n",
 "subjects": [
  {
   "path": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-review-system.md",
   "blob": "40738693d35d605329c16244e3bb5af9aaeaef2f"
  }
 ],
 "scratch": "C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/review-review-system-a",
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
 "context": "The subject is the review system's design record for build dClosedLoop, a design-only build that re-architects gov onto one loop. While the layer reviews ran, the owner asked whether gov's rework needs opt-in review lenses and whether the skeptics' and the synthesizer's instructions need changing ([words]). Two researchers measured gov's review history, and the owner settled the record's forks R-1 to R-3 in [answers]. No review has read this record. The owner asked for two independent medium-effort Tier-2 rounds on each of six pieces of the design that no review had read, their results compared; this is run A, and the other run's report is not evidence, so do not open it. Records settled after this record was written are among the specs: the flow's breakpoint items, the roles and runtime layers, and the comparison of the layer rounds. A statement here that a later record changed or contradicts is a finding. Audit the record as an architecture spec, against six questions: (1) internal consistency: do its components, policies, build units, gaps and answers agree with each other; (2) consistency with the sibling records in specs: v2's principles, policy catalogue and chain, and the layers' records; (3) feasibility against the measured facts in the research returns, the records in specs and the tree: a mechanism the platform or the tree cannot support, or a claim the evidence does not bear out; (4) missing mechanisms: anything review must provide to the flow's breakpoint, the roles or the runtime that the design omits; (5) claims that are unenforced or untestable as written; (6) extension points, such as an opt-in lens, that could not in fact be filled without changing code. Address each finding by the record's section tag, such as [current], [design], [stale], [gaps-proposed], [forks] and [answers]. Write the report to memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-review-system-a.md. Its head carries an H1, then, within its first twelve lines, the line `**Serves:** spec-audit PLAY-dClosedLoop-1`. It carries exactly one `## Verdict:` line, whose token is CLEAN, CLEAN WITH FIXES or BLOCKED and nothing else."
}
```

## [args-runtime-fold] Run A's args for the runtime fold, verbatim

Run B's differ only as `[pairs]` shows.

```json
{
 "kind": "diff-review",
 "base": "6cfd21619e9cbe6084dd9d38982194750aa908b2",
 "head": "3611a60e92117c77f111a9ab7d73c56fd060fe9a",
 "repo": "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297",
 "reviewDir": "memory/builds/dClosedLoop/reviews",
 "specs": [
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-runtime-reviews-compared.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md",
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md",
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md",
  "memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-a.md",
  "memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-b.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-floor.md"
 ],
 "byDesign": "- The build is design-only: no product code and no unit specs. Unit-level detail is absent by design and owed to the chain builds.\n- The owner's settled answers (RH-1, PIN-1, EX-1 to EX-3, DI-1, KN-1, LB-1 to LB-4, L-1 to L-6, the review system's R-1 to R-3, and the earlier F*, FR-*, FI-*, S-*, LR-* and RT-*) are decisions: a finding may show one contradicts a record or the tree, but does not re-argue the owner's choice.\n- Dated records keep what held when they were written: research returns, revision notes (the 2026-10-16 stale sweep's included), [forks], [settled], [review] and the session log's past entries.\n- Records written before 2026-10-16 that say Knowledge mean memory's library side (layer-library [settled], \"Older records' wording\").\n- A refuted finding stays refuted: the comparison records' none rows carry the skeptic's reason.\n- Generated files (memory/LIVE.md, the build README's generated regions, memory/map/generated/ and memory/gotchas/INDEX.md) are rendered and not under review.\n- The atlas page and its generator are an owner-facing view outside this review.\n- The research returns are evidence, measured when written; RT-2's re-verification is recorded in research-runtime-floor and its probes.",
 "checklist": "# recurring-bug-class checklist for 6cfd21619..3611a60e9 (11 changed file(s))\n# 13 class(es) selected by an anchor + 6 universal\n# by anchor specificity: 4 path · 4 directory · 5 basename; a cut tier prints one line per class\n# invariants are read at 6cfd21619e9c; 0 that this subject adds, edits or takes out are listed as items, never by design\n\n- [ ] fixture-passes-by-finding-nothing (universal)\n      a test arm whose fixture never triggers the rule passes, and proves nothing\n      memory/gotchas/fixture-passes-by-finding-nothing.md\n\n- [ ] guard-above-a-fold-makes-its-fallback-dead (universal)\n      a guard added above a fold settles the predicate the fold's own fallback re-tests, leaving a dead arm that reads as coverage\n      memory/gotchas/guard-above-a-fold-makes-its-fallback-dead.md\n\n- [ ] heredoc-escape-reaches-the-regex (universal)\n      source written through a shell heredoc into a non-raw string turns an escape into a control byte, and the symptom never looks like a quoting problem\n      memory/gotchas/heredoc-escape-reaches-the-regex.md\n\n- [ ] inline-fence-swallows-the-rest-of-the-file (universal)\n      a triple-backtick written inline in prose opens a fence the reader never closes, so every section after it silently disappears from the checker's view\n      memory/gotchas/inline-fence-swallows-the-rest-of-the-file.md\n\n- [ ] staged-break-substitutes-a-synthetic-value (universal)\n      an arm that proves a mechanism by replacing the shipped value with a simpler one proves the mechanism for the simpler value\n      memory/gotchas/staged-break-substitutes-a-synthetic-value.md\n\n- [ ] two-answers-to-one-question (universal)\n      a fact stated in two places drifts, and the copies need not disagree loudly to be wrong\n      memory/gotchas/two-answers-to-one-question.md\n\n- [ ] insert-after-a-key-that-occurs-twice (path)\n      a record edit inserts a row after the first match of a cell value that occurs in two tables, so the row lands in the wrong table and the right one never gains it\n      memory/gotchas/insert-after-a-key-that-occurs-twice.md\n\n- [ ] policy-value-with-no-route (path)\n      a policy key catalogues a value that no item reading the key routes or witnesses, so a preset that selects the value cannot run\n      memory/gotchas/policy-value-with-no-route.md\n\n- [ ] rule-stated-with-no-check-that-fails (path)\n      a principle, a constraint between two keys or another rule is added in prose with no check that can fail on its breach, so it binds nothing and nobody can see that it does not\n      memory/gotchas/rule-stated-with-no-check-that-fails.md\n\n- [ ] zero-witness-over-an-unnamed-population (path)\n      a scan whose zero is the witness names no population, so a skipped scan and a scan over less than the guarded boundary publishes both read as clean\n      memory/gotchas/zero-witness-over-an-unnamed-population.md\n\n- [ ] a-merge-of-the-default-branch-read-as-additions (directory)\n      a check that lists the files a range or a commit ADDS reads a merge of the default branch into a feature branch as adding every file the default branch gained, unless its git invocation is one of the shapes that cannot\n      memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md\n\n- [ ] amendment-leaves-its-other-half-standing (directory)\n      a criterion is amended and the clause, scope item or log line that only made sense under the old wording is left behind, so one rule now returns two verdicts\n      memory/gotchas/amendment-leaves-its-other-half-standing.md\n\n- [ ] ledger-token-wrapped-across-a-line-joins-nothing (directory)\n      hygiene check 23 extracts a ledger line's backticked tokens PER LINE, so a token the writer wrapped across a line break belongs to no line and the criterion it answers reads as unanswered\n      memory/gotchas/ledger-token-wrapped-across-a-line-joins-nothing.md\n\n- [ ] retirement-inventory-misses-readers-by-value (directory)\n      an inventory of what reads a retired thing, built by searching for its name, misses every assertion on a count or a value that thing carries, because those name nothing\n      memory/gotchas/retirement-inventory-misses-readers-by-value.md\n\n- [ ] record-without-serves-or-with-a-round-counter (basename) · memory/gotchas/record-without-serves-or-with-a-round-counter.md\n\n- [ ] owner-item-without-its-reject-outcome (basename) · memory/gotchas/owner-item-without-its-reject-outcome.md\n\n- [ ] rate-quoted-without-its-denominator (basename) · memory/gotchas/rate-quoted-without-its-denominator.md\n\n- [ ] a-folded-field-leaves-its-row-shape-docs-behind (basename) · memory/gotchas/a-folded-field-leaves-its-row-shape-docs-behind.md\n\n- [ ] git-rm-cached-refuses-a-diverged-index-blob (basename) · memory/gotchas/git-rm-cached-refuses-a-diverged-index-blob.md\n\n# by design — 0 invariant(s) this selection touches\n",
 "round": 1,
 "intensity": "light",
 "roles": {
  "diffFinder": "gov-diff-reviewer",
  "skeptic": "gov-skeptic",
  "synthesis": "gov-synthesizer"
 },
 "efforts": {
  "diffFinder": "medium",
  "skeptic": "medium",
  "synthesis": "medium"
 },
 "context": "The diff is the runtime layer's fold in build dClosedLoop, a design-only build that re-architects gov onto one loop, with the two settlements after it. No review has read it: the runtime layer's two Tier-2 audits (memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-a.md, memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-b.md) read the design before the fold, and the first closing review of a fold came with the layers round. The owner asked for two independent medium-effort Tier-2 rounds on each of six pieces of the design that no review had read, their results compared; this is run A, and the other run's report is not evidence, so do not open it. The diff holds three commits. 2dbf8f26f folds the two audits' 59 defects into layer-runtime (an act session per act, returns that survive any death, binding at the call), v2 and the gap register, and compares the rounds in memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-runtime-reviews-compared.md, whose [map] names where each defect went and whose [neither] lists the main loop's own additions. e30f0acbd settles the runtime forks: dWellOiledMachine joins the chain with the `next` verb and the owner's controls, and a session starts fresh at a boundary by default. 3611a60e9 re-verifies RT-2 from a new research return: no CLI floor, and every version fails closed through ask rules only the dispatcher answers. The two audit reports and the research returns are handed in as specs and are not under review. Read the diff without them: git -C C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 diff 6cfd21619e9cbe6084dd9d38982194750aa908b2...3611a60e92117c77f111a9ab7d73c56fd060fe9a -- . ':(exclude)memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-a.md' ':(exclude)memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-b.md' ':(exclude)memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-floor-probes.md' ':(exclude)memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-floor.md' ':(exclude)memory/builds/dClosedLoop/prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-15-researcher.md' ':(exclude)memory/builds/dClosedLoop/README.md'. The worktree is at a later HEAD, and later commits changed some of this text: verify each finding against the file at HEAD, cite HEAD's line, and report a defect only if HEAD still carries it. Review for four things: (1) a confirmed audit finding the fold left unfixed, fixed only in part, or fixed in a way its own text contradicts, against [map]'s claim; (2) a defect the fold or a settlement introduced: an item, route, witness, key, value, record kind or lease with no producer, no arm or no home, or one fact now stated two ways; (3) a settled answer misapplied, RT-1 to RT-3 among them; (4) text wrong about the tree or the platform. Write the report to memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-runtime-fold-a.md. Its head carries an H1, then, within its first twelve lines, the line `**Serves:** diff-review PLAY-dClosedLoop-1`. It carries exactly one `## Verdict:` line, whose token is CLEAN, CLEAN WITH FIXES or BLOCKED and nothing else."
}
```

## [args-fold-round3] Run A's args for the layers round's follow-up fold, verbatim

Run B's differ only as `[pairs]` shows.

```json
{
 "kind": "diff-review",
 "base": "cc4c83ad57806d987fcc2318d7e596ea8676407b",
 "head": "1bc4883fec8a8d55147b586645f2709c3b023a3d",
 "repo": "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297",
 "reviewDir": "memory/builds/dClosedLoop/reviews",
 "specs": [
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layers-reviews-compared.md",
  "memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold-followup.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md",
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md",
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md"
 ],
 "byDesign": "- The build is design-only: no product code and no unit specs. Unit-level detail is absent by design and owed to the chain builds.\n- The owner's settled answers (RH-1, PIN-1, EX-1 to EX-3, DI-1, KN-1, LB-1 to LB-4, L-1 to L-6, the review system's R-1 to R-3, and the earlier F*, FR-*, FI-*, S-*, LR-* and RT-*) are decisions: a finding may show one contradicts a record or the tree, but does not re-argue the owner's choice.\n- Dated records keep what held when they were written: research returns, revision notes (the 2026-10-16 stale sweep's included), [forks], [settled], [review] and the session log's past entries.\n- Records written before 2026-10-16 that say Knowledge mean memory's library side (layer-library [settled], \"Older records' wording\").\n- A refuted finding stays refuted: the comparison records' none rows carry the skeptic's reason.\n- Generated files (memory/LIVE.md, the build README's generated regions, memory/map/generated/ and memory/gotchas/INDEX.md) are rendered and not under review.\n- The atlas page and its generator are an owner-facing view outside this review.\n- Where a fix needed a tool's own enumeration, the design states the contract and the owning build's gap carries the enumeration: a missing enumeration in the design is by design, a contract the gap does not carry is not.",
 "checklist": "# recurring-bug-class checklist for cc4c83ad5..1bc4883fe (17 changed file(s))\n# 16 class(es) selected by an anchor + 6 universal\n# by anchor specificity: 8 path · 4 directory · 4 basename; a cut tier prints one line per class\n# invariants are read at cc4c83ad5780; 0 that this subject adds, edits or takes out are listed as items, never by design\n\n- [ ] fixture-passes-by-finding-nothing (universal)\n      a test arm whose fixture never triggers the rule passes, and proves nothing\n      memory/gotchas/fixture-passes-by-finding-nothing.md\n\n- [ ] guard-above-a-fold-makes-its-fallback-dead (universal)\n      a guard added above a fold settles the predicate the fold's own fallback re-tests, leaving a dead arm that reads as coverage\n      memory/gotchas/guard-above-a-fold-makes-its-fallback-dead.md\n\n- [ ] heredoc-escape-reaches-the-regex (universal)\n      source written through a shell heredoc into a non-raw string turns an escape into a control byte, and the symptom never looks like a quoting problem\n      memory/gotchas/heredoc-escape-reaches-the-regex.md\n\n- [ ] inline-fence-swallows-the-rest-of-the-file (universal)\n      a triple-backtick written inline in prose opens a fence the reader never closes, so every section after it silently disappears from the checker's view\n      memory/gotchas/inline-fence-swallows-the-rest-of-the-file.md\n\n- [ ] staged-break-substitutes-a-synthetic-value (universal)\n      an arm that proves a mechanism by replacing the shipped value with a simpler one proves the mechanism for the simpler value\n      memory/gotchas/staged-break-substitutes-a-synthetic-value.md\n\n- [ ] two-answers-to-one-question (universal)\n      a fact stated in two places drifts, and the copies need not disagree loudly to be wrong\n      memory/gotchas/two-answers-to-one-question.md\n\n- [ ] parser-drops-rows-it-cannot-place (path)\n      a record-parsing instrument skips rows under a heading it does not know, or rows its pattern cannot read, and still prints a clean run, so its population shrinks without a word\n      memory/gotchas/parser-drops-rows-it-cannot-place.md\n\n- [ ] owner-item-without-its-reject-outcome (path)\n      a design hands a decision to the owner and routes only the yes, so a no leaves landed work with no route and a check that turns red on the default branch\n      memory/gotchas/owner-item-without-its-reject-outcome.md\n\n- [ ] policy-value-with-no-route (path)\n      a policy key catalogues a value that no item reading the key routes or witnesses, so a preset that selects the value cannot run\n      memory/gotchas/policy-value-with-no-route.md\n\n- [ ] route-names-an-output-its-actor-never-emits (path)\n      a designed route or witness names an output, exit class or record that its actor never produces on that path, so the route is dead or waits forever\n      memory/gotchas/route-names-an-output-its-actor-never-emits.md\n\n- [ ] append-without-an-idempotence-key (path)\n      a command that appends to an append-only record declares no key, so a retried run writes the same row twice and a set-join witness stays green\n      memory/gotchas/append-without-an-idempotence-key.md\n\n- [ ] insert-after-a-key-that-occurs-twice (path)\n      a record edit inserts a row after the first match of a cell value that occurs in two tables, so the row lands in the wrong table and the right one never gains it\n      memory/gotchas/insert-after-a-key-that-occurs-twice.md\n\n- [ ] rule-stated-with-no-check-that-fails (path)\n      a principle, a constraint between two keys or another rule is added in prose with no check that can fail on its breach, so it binds nothing and nobody can see that it does not\n      memory/gotchas/rule-stated-with-no-check-that-fails.md\n\n- [ ] zero-witness-over-an-unnamed-population (path)\n      a scan whose zero is the witness names no population, so a skipped scan and a scan over less than the guarded boundary publishes both read as clean\n      memory/gotchas/zero-witness-over-an-unnamed-population.md\n\n- [ ] a-merge-of-the-default-branch-read-as-additions (directory)\n      a check that lists the files a range or a commit ADDS reads a merge of the default branch into a feature branch as adding every file the default branch gained, unless its git invocation is one of the shapes that cannot\n      memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md\n\n- [ ] amendment-leaves-its-other-half-standing (directory)\n      a criterion is amended and the clause, scope item or log line that only made sense under the old wording is left behind, so one rule now returns two verdicts\n      memory/gotchas/amendment-leaves-its-other-half-standing.md\n\n- [ ] ledger-token-wrapped-across-a-line-joins-nothing (directory)\n      hygiene check 23 extracts a ledger line's backticked tokens PER LINE, so a token the writer wrapped across a line break belongs to no line and the criterion it answers reads as unanswered\n      memory/gotchas/ledger-token-wrapped-across-a-line-joins-nothing.md\n\n- [ ] retirement-inventory-misses-readers-by-value (directory)\n      an inventory of what reads a retired thing, built by searching for its name, misses every assertion on a count or a value that thing carries, because those name nothing\n      memory/gotchas/retirement-inventory-misses-readers-by-value.md\n\n- [ ] record-without-serves-or-with-a-round-counter (basename) · memory/gotchas/record-without-serves-or-with-a-round-counter.md\n\n- [ ] rate-quoted-without-its-denominator (basename) · memory/gotchas/rate-quoted-without-its-denominator.md\n\n- [ ] a-folded-field-leaves-its-row-shape-docs-behind (basename) · memory/gotchas/a-folded-field-leaves-its-row-shape-docs-behind.md\n\n- [ ] git-rm-cached-refuses-a-diverged-index-blob (basename) · memory/gotchas/git-rm-cached-refuses-a-diverged-index-blob.md\n\n# by design — 0 invariant(s) this selection touches\n",
 "round": 3,
 "intensity": "light",
 "roles": {
  "diffFinder": "gov-diff-reviewer",
  "skeptic": "gov-skeptic",
  "synthesis": "gov-synthesizer"
 },
 "efforts": {
  "diffFinder": "medium",
  "skeptic": "medium",
  "synthesis": "medium"
 },
 "context": "The diff is round 3 of the closing review of the layers round's fold in build dClosedLoop, a design-only build that re-architects gov onto one loop. Round 1 reviewed the fold of layers 1 to 4. Round 2 (memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold-followup.md) reviewed round 1's fixes and returned CLEAN WITH FIXES, 31 of 34 confirmed in 18 items; its confirmed findings are handed in as priorFindings. No round has read the fold of those 18 items: the library review's range starts at it. The owner asked for two independent medium-effort Tier-2 rounds on each of six pieces of the design that no review had read, their results compared; this is run A, and the other run's report is not evidence, so do not open it. The diff is the one commit 1bc4883fe that folds them: flow-steps, layer-roles, layer-memory, layer-flow, flow-roles, layer-runtime, v2, the gap register, three bug classes under memory/gotchas/, and memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layers-reviews-compared.md [follow-up], which names where each item went. Where a fix needed a tool's own enumeration, the design text states the contract and the owning build's gap carries the enumeration. Read the diff without round 2's report and the generated files: git -C C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 diff cc4c83ad57806d987fcc2318d7e596ea8676407b...1bc4883fec8a8d55147b586645f2709c3b023a3d -- . ':(exclude)memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold-followup.md' ':(exclude)memory/gotchas/INDEX.md' ':(exclude)memory/builds/dClosedLoop/README.md'. The worktree is at a later HEAD, and later commits changed some of this text: verify each finding against the file at HEAD, cite HEAD's line, and report a defect only if HEAD still carries it. Review for three things: (1) a round-2 finding the fix leaves standing, fixes in part, or fixes in a way its own text contradicts; (2) a defect the fix itself introduced: an item, route, witness, key, value, record kind or lease with no producer, no arm or no home, or one fact now stated two ways; (3) text wrong about the tree, the lander's and the runner's seams included. Write the report to memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold-round3-a.md. Its head carries an H1, then, within its first twelve lines, the line `**Serves:** diff-review PLAY-dClosedLoop-1`. It carries exactly one `## Verdict:` line, whose token is CLEAN, CLEAN WITH FIXES or BLOCKED and nothing else.",
 "priorFindings": [
  {
   "id": 1,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:300",
   "claim": "The H2/M9 fix to deploy.core still names a witness that its producers do not write on three reachable paths. (1) On exit 1 after the push, `write_lander_marker || exit 1` (push-main.sh:979) runs before `run_post_merge` (:980), so no bar is started. But the witness bullets (:309-329) have deploy.core start the bar itself only when the key is undeclared or after exit 4. (2) Under `local`, `run_post_merge` can decline to start the bar and still return 0 (push-main.sh:440-452: no python launcher, no kit, no common dir). deploy.core then waits for a verdict that never comes. (3) post-merge.sh writes a third verdict, `REFUSED` (post-merge.sh:64-68, :310, :366), which matches none of green, red or still running. `<common-dir>/gate-post-merge` keeps only the last landing's verdict, so a second landing on the node can overwrite this one before deploy.core reads it.",
   "severity": "medium"
  },
  {
   "id": 2,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:299",
   "claim": "deploy.land's 'exit 0, landed and marked' and its witness 'the lander's marker on exit 0' do not match the lander. `write_lander_marker` returns 0 with no marker in four cases: no `.unattended.conf`; an empty `LANDER_MARKER`; a hook that vetted a STUB bar; and a hook that recorded no vetted bar (push-main.sh:356, :369-376). That last case includes the `pushed == was` no-op push, which `check_push_allow` accepts at :344-346.",
   "severity": "medium"
  },
  {
   "id": 3,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:320",
   "claim": "'Exit 1 has two meanings' leaves out a third. `derive_push_failure` returns `unreachable` when the remote cannot be probed after a failed push (push-main.sh:282-284), and `cmd_land` maps it to `exit 1` (:1000-1002), not 3. The adapter's test, whether the remote's default branch holds the pushed SHA, cannot be answered against an unreachable remote. Gate-red, head-moved, signalled and hook-precondition refusals also exit 1 at this point, and the listed causes omit them.",
   "severity": "medium"
  },
  {
   "id": 4,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:253",
   "claim": "In the H1/M10 fix, test.flakes' only witness is 'the flake record', but under `verdict.flakes: retry-only` its Then cell says 'nothing is recorded'. Also, under `quarantine` the run re-enters `test.verdict`, not `test.select`, although `test.select` is the item that applies `verdict.held` to the selection (:249).",
   "severity": "medium"
  },
  {
   "id": 5,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:452",
   "claim": "The LR-7 form 'a held flaky leg: `verdict.held` releases it' names an output that its actor never produces. In v2:568, `verdict.held` takes the values peer-or-cadence, push-selected and on-demand, which decide when a held leg runs. Nothing in it releases a leg. Round 1's finding 17 already rejected `verdict.held` as the quarantine carrier. Also, after the fix test.flakes no longer files an ask (flow-steps:253), so this core ask kind has no filer.",
   "severity": "medium"
  },
  {
   "id": 6,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:315",
   "claim": "The M7 fix for `record-concurrent-mint` is partial and miscites its seam. `check_slug_claimed` (gen_build_index.py:3478-3504) runs three local, read-only git probes and writes no claim. It is not a 'compare-and-swap against the remote's claims', and the build's own coordination.md:68 and research-plan.md:104 say it reads local history only. The intake record is written at `entry.intake`, before `plan.input`. A patch build enters at `designing` straight from placement (transitions :426), so it never passes `plan.input` or `plan.lease`.",
   "severity": "medium"
  },
  {
   "id": 7,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:496",
   "claim": "The M8 fix's 'reject and remove' disposition leaves the red it was written to prevent. The both-ways check (:636-637) accepts a `gov:feature` tag only when its entry is 'proposed, accepted, or rejected and kept'. Between the owner's reject-and-remove and the landing of the patch build that removes the anchor, the anchor sits on the default branch with an entry in none of those states.",
   "severity": "medium"
  },
  {
   "id": 8,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:429",
   "claim": "The new row 'planning | `plan.dedupe`: a duplicate, placed onto the build it matches | merged' disagrees with plan.dedupe's own Then cell (:104), which is 'a duplicate or an overlap → `entry.place`, with the finding'. plan.dedupe places nothing. It sends the request back to placement, and placement's outcomes from a build in `planning` (new, ask, none, amend, continue) have no row. An overlap has no row either.",
   "severity": "medium"
  },
  {
   "id": 9,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:45",
   "claim": "The single mailbox rule (M5) says the undisposed messages 'are marked so in the terminal snapshot', and that only then is the ref pruned. But the rule is run by `deploy.release` and `life.release`, which come after `deploy.snapshot` and `life.snapshot` have already committed the terminal snapshot (:304-305, :407-408). The snapshot item is also a no-op on an equal snapshot.",
   "severity": "medium"
  },
  {
   "id": 10,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md:1169",
   "claim": "C7: role_matrix.py's arm 0 does not close the class it was added for. A table row whose tag does not match `^\\| `([a-z]+\\.[a-z0-9-]+)` \\|` is skipped silently, and nothing counts it: an uppercase letter, an underscore, or a three-part tag such as `item.build.scope`, the full spelling [rules] names. Probe: I extracted the script from the record and ran it on copies of flow-steps. With `test.reason` changed to `test.Reason` it printed 'items 70; ... findings 0' and exited 0. With `test.attribute` changed to `test.attribute.own` it printed the same, exit 0. The unmodified record printed 'items 71 ... findings 0'.",
   "severity": "medium"
  },
  {
   "id": 12,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layers-reviews-compared.md:330",
   "claim": "The [closing-review] row M13 says the runtime record's two rows were fixed 'under dated notes'. The diff edits layer-runtime:54 and :892 in place, with no dated note. Only flow-roles' FR-6 and H7 carry 'Revised: 2026-10-16'.",
   "severity": "low"
  },
  {
   "id": 13,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:452",
   "claim": "The LR-7 form 'a held flaky leg: `verdict.held` releases it' has no filer and no releasing actor. The M10 fix removed 'with an ask' from `test.flakes` (flow-steps:253, which now files no ask). `verdict.held` is a run schedule (peer-or-cadence, push-selected or on-demand; v2:568, flow-steps:263) and has no release value.",
   "severity": "medium"
  },
  {
   "id": 15,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:314",
   "claim": "The M7 fix rests on a lock that does not exist. It says the slug is 'claimed first, by compare-and-swap against the remote's claims (`check_slug_claimed`)'. But gen_build_index.py:3478 `check_slug_claimed` is a read-only local probe: `rev-list --all`, `git grep` and `log --all` over the clone, as its docstring says. It writes nothing, takes no lock and reads no remote. No 'family's claim ref' exists for asks either: tools/ uses only refs/gov/runs/* and refs/gov/bar-red.",
   "severity": "high"
  },
  {
   "id": 16,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:316",
   "claim": "Memory says the intake record mints under the slug claim taken at `plan.input`. But flow-steps' `entry.intake` hook (line 67) writes the intake record before any step runs. Flow-steps' `plan.input` (line 103) only pins the input, and neither its Does nor its witness claims a slug.",
   "severity": "medium"
  },
  {
   "id": 18,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:429",
   "claim": "The new transition row sends `plan.dedupe`'s duplicate to the terminal state `merged`. The item's own Then (line 104) sends 'a duplicate or an overlap' back to `entry.place` with the finding, and layer-flow [settled]:331-332 says 'a duplicate maps to continue'. The overlap outcome has no row.",
   "severity": "medium"
  },
  {
   "id": 19,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:811",
   "claim": "C11: the diff edited dDeclaredLoop's row (the frontier wording) but left 'terminal states landed, withdrawn and superseded'. flow-steps:446 now declares seven terminal states: landed, withdrawn, superseded, deferred, retired, refused and merged.",
   "severity": "medium"
  },
  {
   "id": 20,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:45",
   "claim": "The new mailbox rule marks undisposed messages 'in the terminal snapshot', but that snapshot is committed one item earlier by `deploy.snapshot` (line 304) or `life.snapshot` (line 407). `deploy.release` and `life.release` declare only 'the deleted refs, and the mailbox's messages in the folder' as their writes.",
   "severity": "medium"
  },
  {
   "id": 21,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:300",
   "claim": "deploy.core routes green, red, still running and no verdict, but post-merge.sh also records `verdict REFUSED` (exit 2, write_refusal at post-merge.sh:64-67). Examples: the sha is not on the remote branch as this clone last fetched it (line 164), no remote, or a runner absent at the sha. The witness is the single-slot `<common-dir>/gate-post-merge`, which the next landing's bar on the same node overwrites.",
   "severity": "medium"
  },
  {
   "id": 22,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:299",
   "claim": "deploy.land's witness is 'the lander's marker on exit 0' and its class is 'exit 0, landed and marked'. But push-main.sh's write_lander_marker (lines 354-376) returns 0 without writing a marker in four cases: no .unattended.conf, no LANDER_MARKER, a STUB-gated bar, and no vetted bar recorded. cmd_land then exits 0 ('landed').",
   "severity": "medium"
  },
  {
   "id": 23,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md:1169",
   "claim": "C5/parser class: arm 0 refuses rows under unknown headings, but an item row whose tag the row regex cannot parse is still skipped silently. Probe: on a scratch copy of flow-steps at 2e6f9aa1b, with `test.flakes` rewritten as `test.Flakes`, role_matrix.py printed 'items 70; ... findings 0' with no FINDING line. The planted red uses only a lowercase heading rename, a shape the heading regex reads.",
   "severity": "medium"
  },
  {
   "id": 24,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:456",
   "claim": "[asks] calls the ten forms 'the core filers' whole set (LR-7)'. But flow-steps [open]:538 has Test, under `tests.without-cadence: wait-for-expansion`, file an ask whose acceptance is 'the level green once observability's Maintain runs it'. That is none of the ten: an unrun level is not a red.",
   "severity": "medium"
  },
  {
   "id": 25,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md:95",
   "claim": "The M12 fix is partial. Prior id 23 named four carriers of the hook-written verdict, flow-roles:95 among them. flow-roles' Test row still returns 'the hook-written verdict', and both [closing-review] M12 and flow-steps' `hook-actor-kind` row list only layer-flow, v2's contracts and dWitnessedBar's row.",
   "severity": "low"
  },
  {
   "id": 26,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md:330",
   "claim": "C11: the M10 fix made test.flakes hold a leg only under `verdict.flakes: quarantine`, and record or retry under the other values. layer-flow [settled]'s flake bullet still says, unconditionally, 'a flaky leg past the threshold is held (`verdict.held`)'.",
   "severity": "low"
  },
  {
   "id": 27,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:892",
   "claim": "[closing-review] M13 says the runtime record's two rows were fixed 'under dated notes'. Lines 54 and 892 were rewritten in place with no revision note, unlike flow-roles, which gained 'Revised: 2026-10-16'.",
   "severity": "low"
  },
  {
   "id": 28,
   "lens": "verification",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:251",
   "claim": "C9: The H1 fix sends `nondeterministic · <leg>` reds to `test.flakes`. But `test.verdict` (:250) is declared as the runner with `GATE_ATTRIBUTE` only, and on that invocation the bar never prints the line. run-gates.sh prints it only for a leg it drew from a cached ok (`$WORK/$i.sampled`, :3609 and :5162-5172), and it draws legs only when REUSE_MODE is `env` or `push` (:3570). With no `GATE_REUSE` set and no push naming HEAD, REUSE_MODE stays `off` (:3305-3323). The evidence test the new gotcha cites asserts the line only under `GATE_REUSE=1 GATE_REUSE_SAMPLE=1` (run-gates.evidence.test.sh:1266-1267).",
   "severity": "high"
  },
  {
   "id": 29,
   "lens": "verification",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:253",
   "claim": "Under `quarantine`, `test.flakes` holds the leg and then re-enters `test.verdict`. That skips `test.select` (:249), the only item that applies `verdict.held` to the selection record. So the 'fresh verdict on the same tree' runs the old selection, with the just-held leg still in it as an ordinary leg.",
   "severity": "medium"
  },
  {
   "id": 30,
   "lens": "verification",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:318",
   "claim": "C9: The core re-check's witness bullets cover exit 0 under `local`, `ci`, undeclared and exit 4. They do not cover exit 1 after the push. push-main.sh:978-980 calls `write_lander_marker || exit 1` before `run_post_merge`, so a landing whose marker failed starts no bar. Under `GATE_POST_MERGE=local`, `deploy.core` (:300) 'reads' `<common-dir>/gate-post-merge` for a SHA no bar was started on.",
   "severity": "medium"
  },
  {
   "id": 31,
   "lens": "verification",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:452",
   "claim": "C9: LR-7's form 'a held flaky leg: `verdict.held` releases it' names an event no actor emits. `verdict.held`'s values (v2:568: peer-or-cadence, push-selected, on-demand) schedule when a held leg runs, and none of them releases one. The same diff also dropped 'with an ask' from `test.flakes` (flow-steps:253), so no core item files this ask kind at all.",
   "severity": "medium"
  },
  {
   "id": 32,
   "lens": "verification",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:314",
   "claim": "C6/C9: The M7 fix says a slug is 'claimed first, by compare-and-swap against the remote's claims (`check_slug_claimed`), at `plan.input`', and that intake records mint under that claim. That fails in three ways. First, `check_slug_claimed` (gen_build_index.py:3478) is a read-only probe of local refs, tracked files and commit messages: it writes no claim and does no compare-and-swap. Second, flow-steps' `plan.input` (:103) only pins the intake record, proven by its SHA, and takes no claim. Third, the intake record is written by `entry.intake` (:67) before `plan.input` exists.",
   "severity": "medium"
  },
  {
   "id": 33,
   "lens": "verification",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md:1170",
   "claim": "The M16 fix is partial. Arm 0 asserts only that each step holds at least one item. A step-table row that the item regex cannot read is still skipped with no message. Probes on the step definitions at 2e6f9aa1b: with the backticks dropped from `deploy.notify`'s row, the run printed 'items 70; ... findings 0' and exited 0. With a double space after `` `test.attribute` ``, it printed 'items 70; ... items with a role 18; findings 0' and exited 0. The recorded rename red does reproduce: 'items 65 ... findings 7', exit 1.",
   "severity": "medium"
  },
  {
   "id": 34,
   "lens": "verification",
   "ref": "memory/gotchas/parser-drops-rows-it-cannot-place.md:33",
   "claim": "Two new class records anchor on files that do not cover the class. In this record, the anchor `role_matrix.py` resolves to no tracked path (probed with gotchas.py's ANCHOR_RE and selection predicate at 2e6f9aa1b: 0 hits). Its other anchors are this build's dated records. `owner-item-without-its-reject-outcome.md` anchors only layer-memory.md and the fold review.",
   "severity": "low"
  }
 ]
}
```

## [args-library-followup] Run A's args for the library round's fold, verbatim

Run B's differ only as `[pairs]` shows.

```json
{
 "kind": "diff-review",
 "base": "d4fc4bb51d56c315afea4f3fdf18ea86f947c020",
 "head": "0dd96272468fb2487d51f362266f0ef46185859b",
 "repo": "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297",
 "reviewDir": "memory/builds/dClosedLoop/reviews",
 "specs": [
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md",
  "memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-library.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md",
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md",
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md"
 ],
 "byDesign": "- The build is design-only: no product code and no unit specs. Unit-level detail is absent by design and owed to the chain builds.\n- The owner's settled answers (RH-1, PIN-1, EX-1 to EX-3, DI-1, KN-1, LB-1 to LB-4, L-1 to L-6, the review system's R-1 to R-3, and the earlier F*, FR-*, FI-*, S-*, LR-* and RT-*) are decisions: a finding may show one contradicts a record or the tree, but does not re-argue the owner's choice.\n- Dated records keep what held when they were written: research returns, revision notes (the 2026-10-16 stale sweep's included), [forks], [settled], [review] and the session log's past entries.\n- Records written before 2026-10-16 that say Knowledge mean memory's library side (layer-library [settled], \"Older records' wording\").\n- A refuted finding stays refuted: the comparison records' none rows carry the skeptic's reason.\n- Generated files (memory/LIVE.md, the build README's generated regions, memory/map/generated/ and memory/gotchas/INDEX.md) are rendered and not under review.\n- The atlas page and its generator are an owner-facing view outside this review.",
 "checklist": "# recurring-bug-class checklist for d4fc4bb51..0dd962724 (24 changed file(s))\n# 15 class(es) selected by an anchor + 6 universal\n# by anchor specificity: 8 path · 4 directory · 3 basename; a cut tier prints one line per class\n# invariants are read at d4fc4bb51d56; 0 that this subject adds, edits or takes out are listed as items, never by design\n\n- [ ] fixture-passes-by-finding-nothing (universal)\n      a test arm whose fixture never triggers the rule passes, and proves nothing\n      memory/gotchas/fixture-passes-by-finding-nothing.md\n\n- [ ] guard-above-a-fold-makes-its-fallback-dead (universal)\n      a guard added above a fold settles the predicate the fold's own fallback re-tests, leaving a dead arm that reads as coverage\n      memory/gotchas/guard-above-a-fold-makes-its-fallback-dead.md\n\n- [ ] heredoc-escape-reaches-the-regex (universal)\n      source written through a shell heredoc into a non-raw string turns an escape into a control byte, and the symptom never looks like a quoting problem\n      memory/gotchas/heredoc-escape-reaches-the-regex.md\n\n- [ ] inline-fence-swallows-the-rest-of-the-file (universal)\n      a triple-backtick written inline in prose opens a fence the reader never closes, so every section after it silently disappears from the checker's view\n      memory/gotchas/inline-fence-swallows-the-rest-of-the-file.md\n\n- [ ] staged-break-substitutes-a-synthetic-value (universal)\n      an arm that proves a mechanism by replacing the shipped value with a simpler one proves the mechanism for the simpler value\n      memory/gotchas/staged-break-substitutes-a-synthetic-value.md\n\n- [ ] two-answers-to-one-question (universal)\n      a fact stated in two places drifts, and the copies need not disagree loudly to be wrong\n      memory/gotchas/two-answers-to-one-question.md\n\n- [ ] policy-value-with-no-route (path)\n      a policy key catalogues a value that no item reading the key routes or witnesses, so a preset that selects the value cannot run\n      memory/gotchas/policy-value-with-no-route.md\n\n- [ ] append-without-an-idempotence-key (path)\n      a command that appends to an append-only record declares no key, so a retried run writes the same row twice and a set-join witness stays green\n      memory/gotchas/append-without-an-idempotence-key.md\n\n- [ ] insert-after-a-key-that-occurs-twice (path)\n      a record edit inserts a row after the first match of a cell value that occurs in two tables, so the row lands in the wrong table and the right one never gains it\n      memory/gotchas/insert-after-a-key-that-occurs-twice.md\n\n- [ ] parser-drops-rows-it-cannot-place (path)\n      a record-parsing instrument skips rows under a heading it does not know, or rows its pattern cannot read, and still prints a clean run, so its population shrinks without a word\n      memory/gotchas/parser-drops-rows-it-cannot-place.md\n\n- [ ] rate-quoted-without-its-denominator (path)\n      a rate put to the owner in a fork divides by the wrong population, so the option's own cost reads several times off\n      memory/gotchas/rate-quoted-without-its-denominator.md\n\n- [ ] owner-item-without-its-reject-outcome (path)\n      a design hands a decision to the owner and routes only the yes, so a no leaves landed work with no route and a check that turns red on the default branch\n      memory/gotchas/owner-item-without-its-reject-outcome.md\n\n- [ ] route-names-an-output-its-actor-never-emits (path)\n      a designed route or witness names an output, exit class or record that its actor never produces on that path, so the route is dead or waits forever\n      memory/gotchas/route-names-an-output-its-actor-never-emits.md\n\n- [ ] rule-stated-with-no-check-that-fails (path)\n      a principle, a constraint between two keys or another rule is added in prose with no check that can fail on its breach, so it binds nothing and nobody can see that it does not\n      memory/gotchas/rule-stated-with-no-check-that-fails.md\n\n- [ ] a-merge-of-the-default-branch-read-as-additions (directory)\n      a check that lists the files a range or a commit ADDS reads a merge of the default branch into a feature branch as adding every file the default branch gained, unless its git invocation is one of the shapes that cannot\n      memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md\n\n- [ ] amendment-leaves-its-other-half-standing (directory)\n      a criterion is amended and the clause, scope item or log line that only made sense under the old wording is left behind, so one rule now returns two verdicts\n      memory/gotchas/amendment-leaves-its-other-half-standing.md\n\n- [ ] ledger-token-wrapped-across-a-line-joins-nothing (directory)\n      hygiene check 23 extracts a ledger line's backticked tokens PER LINE, so a token the writer wrapped across a line break belongs to no line and the criterion it answers reads as unanswered\n      memory/gotchas/ledger-token-wrapped-across-a-line-joins-nothing.md\n\n- [ ] retirement-inventory-misses-readers-by-value (directory)\n      an inventory of what reads a retired thing, built by searching for its name, misses every assertion on a count or a value that thing carries, because those name nothing\n      memory/gotchas/retirement-inventory-misses-readers-by-value.md\n\n- [ ] record-without-serves-or-with-a-round-counter (basename) · memory/gotchas/record-without-serves-or-with-a-round-counter.md\n\n- [ ] a-folded-field-leaves-its-row-shape-docs-behind (basename) · memory/gotchas/a-folded-field-leaves-its-row-shape-docs-behind.md\n\n- [ ] git-rm-cached-refuses-a-diverged-index-blob (basename) · memory/gotchas/git-rm-cached-refuses-a-diverged-index-blob.md\n\n# by design — 0 invariant(s) this selection touches\n",
 "round": 2,
 "intensity": "light",
 "roles": {
  "diffFinder": "gov-diff-reviewer",
  "skeptic": "gov-skeptic",
  "synthesis": "gov-synthesizer"
 },
 "efforts": {
  "diffFinder": "medium",
  "skeptic": "medium",
  "synthesis": "medium"
 },
 "context": "The diff is round 2 of the library round's review in build dClosedLoop, a design-only build that re-architects gov onto one loop. Round 1 (memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-library.md) reviewed KN-1's fold, the library design and its settlement, and returned CLEAN WITH FIXES, 25 of 31 confirmed in 19 items; its confirmed findings are handed in as priorFindings. The owner deferred this follow-up on 2026-10-16 and now asks for it. The owner asked for two independent medium-effort Tier-2 rounds on each of six pieces of the design that no review had read, their results compared; this is run A, and the other run's report is not evidence, so do not open it. The diff is the one commit 0dd962724 that folds them: layer-library's [review-fold] names where each item went; flow-steps (build.distill writes the major decisions' rows before Test), layer-memory, layer-instruction, layer-roles, v2, the gap register, and four bug classes filed under memory/gotchas/ and claimed in memory/map/features/. Read the diff without round 1's report, the atlas and the generated files: git -C C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 diff d4fc4bb51d56c315afea4f3fdf18ea86f947c020...0dd96272468fb2487d51f362266f0ef46185859b -- . ':(exclude)memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-library.md' ':(exclude)memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.md' ':(exclude)memory/map/generated' ':(exclude)memory/gotchas/INDEX.md' ':(exclude)memory/builds/dClosedLoop/README.md'. The worktree is at a later HEAD, and later commits changed some of this text: verify each finding against the file at HEAD, cite HEAD's line, and report a defect only if HEAD still carries it. Review for three things: (1) a round-1 finding the fix leaves standing, fixes in part, or fixes in a way its own text contradicts; (2) a defect the fix itself introduced: an item, route, witness, key, value, record kind or lease with no producer, no arm or no home, or one fact now stated two ways; (3) text wrong about the tree. Write the report to memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-library-followup-a.md. Its head carries an H1, then, within its first twelve lines, the line `**Serves:** diff-review PLAY-dClosedLoop-1`. It carries exactly one `## Verdict:` line, whose token is CLEAN, CLEAN WITH FIXES or BLOCKED and nothing else.",
 "priorFindings": [
  {
   "id": 1,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:395",
   "claim": "`review.report` allows only `class:`, `new:` and `gate:` dispositions, and its witness and routes have no arm for `none`. But v2 makes `review.unclassed: reason` the velocity preset's value (v2:753) and also catalogues `owner-rules`. layer-library [left-shift] (:181) lists `none` with its reason as a fourth disposition.",
   "severity": "medium"
  },
  {
   "id": 2,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:396",
   "claim": "On built work, `review.dispose` assigns the `new:` class record to 'the fix unit's builder'. But under the default `review.findings: blocker-high-own` (v2:625), a lower-graded confirmed finding becomes an ask, and an ask has no fix unit and no builder. The witness ('each `new:` class to its record once written') and the route ('built → released') also let the breakpoint release before any class exists. On the unbuilt path, `review.fold`'s witness (:397) joins only the spec fold, never the class record.",
   "severity": "medium"
  },
  {
   "id": 3,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:313",
   "claim": "`deploy.distill` is a plain command whose only route is `deploy.recommend`. But v2 sets `decisions.major: author-owner-ratifies` in the strict preset (v2:719), and LB-3 defines that value as 'each major row waits for the owner's ratification at `deploy.distill`'. Deploy declares no owner breakpoint or owner item there, and no outcome for a rejected row.",
   "severity": "medium"
  },
  {
   "id": 4,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:204",
   "claim": "`build.unit-pass`'s witness hard-codes the `new-seam` condition: the reuse line is owed 'for a unit whose spec's reuse audit says \"no existing seam fits\"', and only then adds 'as `reuse.propose` says'. Strict sets `reuse.propose: every-unit` and velocity sets `owner-asks` (v2:715).",
   "severity": "medium"
  },
  {
   "id": 5,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:313",
   "claim": "`deploy.distill` appends rows to the shared append-only log, but declares neither 'idempotent' nor 'reconciles'. `[rules]` (:58) requires every command item to declare one, and its Deploy neighbours `deploy.notify`/`snapshot`/`release` spell out their no-op. Its witness, 'a join both ways' between the major decisions and the rows naming the build, is a set join that a duplicated row still satisfies.",
   "severity": "medium"
  },
  {
   "id": 6,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:346",
   "claim": "The library flow points were added to the item tables, but not to their steps' Memory clauses:\n- Deploy's Memory clause (:346) lists the landing record, transition, snapshot and messages, not the decision-log rows `deploy.distill` writes.\n- Build's (:227) omits the `new:` class records the fix unit's builder writes and the reuse proposals.\n- Plan's (:123) reads neither the research view nor the decision log, though layer-library [research-view] calls the research view 'the planner's core source' and [consult] names both as the planner's fallback without recall.",
   "severity": "low"
  },
  {
   "id": 7,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:842",
   "claim": "dBoundRoles' planned units still read 'work-order fields an expansion fills (bug classes, the map's dossiers) declared as optional slots'. KN-1 made bug classes core: they ride the builder's and reviewers' work orders on every install (layer-library [settled]; layer-instruction's KN-1 note: 'the first and the third are no longer breaks').",
   "severity": "medium"
  },
  {
   "id": 8,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:309",
   "claim": "v2's amended rule says an optional slot is 'rendered empty where it is not installed'. layer-library [consult] (:281-283) says every optional slot renders filled, searched-with-nothing, or not-installed with the core's fallback named, and 'Absence never renders as an empty result, which would read as a clean search'. Two copies of one rule disagree, and the v2 copy was edited in this diff.",
   "severity": "medium"
  },
  {
   "id": 9,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:839",
   "claim": "dOrderedCharter's planned units still say 'the check that the core never depends on an expansion'. P28 as amended (v2:433) extends that rule to a core layer's optional components ('the core never depends on it either'), and the map, recall and lexicon are no longer expansions.",
   "severity": "low"
  },
  {
   "id": 10,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md:82",
   "claim": "LB-2's recommended option told the owner 'today 256 specs in 67 builds, about 1.6 proposals per such build'. 256/67 is 3.8. The 1.6 is 256/163, the rate over all builds, not over 'such' builds (research P2-A has the same slip).",
   "severity": "medium"
  },
  {
   "id": 11,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:238",
   "claim": "`gap-review-10` and `gap-mem-15` were added without a re-measure block. The register says its counts 'are derived, never typed', and each fold appends the instrument's output. Run now, the instrument prints Review=10 Memory=15 Deploy=9, LOW=22 MED=70 HIGH=79, while the last recorded block shows Review=9 Memory=12 Deploy=8, LOW=21 MED=67 HIGH=78.",
   "severity": "low"
  },
  {
   "id": 12,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:313",
   "claim": "deploy.distill reads 'the build's decisions declared major', but no item in any step writes a decision record with a declared class. The two-way join that is its witness therefore runs over an empty population and passes on every build.",
   "severity": "high"
  },
  {
   "id": 13,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:313",
   "claim": "C8 owner-item-without-its-reject-outcome: under decisions.major=author-owner-ratifies, deploy.distill has no owner-item wait and no route for a rejected ratification. That value is the strict preset's.",
   "severity": "medium"
  },
  {
   "id": 14,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:346",
   "claim": "deploy.distill appends rows to memory/DECISIONS.md after deploy.land has pushed the landed SHA, and no later Deploy item lands that write. Deploy's Memory field does not even list the decision-log write.",
   "severity": "medium"
  },
  {
   "id": 15,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md:285",
   "claim": "The [consult] table, which lists every place the core reads an optional component, misses two core paths that import memory-recall. Check 27 ranks added decision rows and gotchas with recall's bench.build_index, and the decision log's 'holds now' view is rendered from recall's derive_supersession_map.",
   "severity": "medium"
  },
  {
   "id": 17,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:362",
   "claim": "C11 amendment-leaves-its-other-half-standing: review.report's disposition set and witness hold only class:, new: and gate:. The `none` disposition, which layer-library [left-shift] line 181 defines and review.unclassed=reason or owner-rules admits, has neither a witness arm nor a route.",
   "severity": "medium"
  },
  {
   "id": 18,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md:219",
   "claim": "The research view and its counts key on the `**Serves:** research` binding, but HYGIENE defines that kind as 'a report that precedes the specs', and it binds design records, session logs and gap registers. The view therefore indexes far more than research, and the '202 research records' figure overcounts.",
   "severity": "medium"
  },
  {
   "id": 21,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:370",
   "claim": "C11 amendment-leaves-its-other-half-standing: the kinds list still says whether the annotation index is core or the map's 'is the library round's (`[open]` in its record)', although LB-4 settled it and layer-library's [open] now holds only the review.",
   "severity": "low"
  },
  {
   "id": 22,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-session-log.md:114",
   "claim": "Five two-column Records-index rows (research-library-paths, layer-library, atlas.html, atlas.py, the 18-researcher prompt) were appended inside the seven-column Dispatches table, and the Records index at line 1287 never gained them.",
   "severity": "medium"
  },
  {
   "id": 24,
   "lens": "verification",
   "ref": "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md:224",
   "claim": "C6: the research view and its witness select 'research' by the `**Serves:** research` binding, which design records, gap registers and session logs also carry. Check 21 only checks that a Serves line is present, so this witness cannot fail on a record bound to the wrong kind.",
   "severity": "medium"
  },
  {
   "id": 25,
   "lens": "verification",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:396",
   "claim": "C9: `review.dispose` is a command, but its witness ('each `new:` class to its record once written') waits for a record that no actor writes at or before dispose. On unbuilt specs the writer is `review.fold`, which runs after dispose (dispose → fold). On built work it is 'the fix unit's builder', and no such builder exists when `review.findings` turns the finding into an ask.",
   "severity": "medium"
  },
  {
   "id": 26,
   "lens": "verification",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:395",
   "claim": "`review.report`'s computed witness requires that '`new:` names a slug no record holds'. That predicate turns false as soon as the flow's next steps file that class under memory/gotchas/, so a witnessed report later re-derives as unwitnessed.",
   "severity": "medium"
  },
  {
   "id": 28,
   "lens": "verification",
   "ref": "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:719",
   "claim": "C9: the strict preset sets `decisions.major: author-owner-ratifies`, so each major row 'waits for the owner's ratification at `deploy.distill`' (layer-library :89-90). `deploy.distill`'s only actor is a command, and its only route is → `deploy.recommend`. The owner's ratification is an output this actor never emits, and no route handles a refusal. The same holds for `review.unclassed: owner-rules` against `review.report`, whose actor is the synthesizer.",
   "severity": "medium"
  },
  {
   "id": 29,
   "lens": "verification",
   "ref": "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:753",
   "claim": "The velocity preset sets `review.unclassed: reason`, but `review.report`'s Does and witness (flow-steps :395) list only `class:`, `new:` and `gate:` and resolve only those. No arm accepts or checks a `none` disposition with a reason.",
   "severity": "medium"
  },
  {
   "id": 30,
   "lens": "verification",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:204",
   "claim": "`build.unit-pass`'s witness now includes the builder's own typed reuse line. That breaks [rules] (:24, 'No witness is typed by the acting agent'), and the `none` arm cannot fail. The trigger is also the exact prose phrase \"no existing seam fits\", while the hygiene §10 check that admits specs also accepts 'no seam fits', 'no existing seam' and a 'reuse-first' waiver.",
   "severity": "medium"
  }
 ]
}
```

## [args-expansions-fold-round3] Run A's args for the expansion round's follow-up fold, verbatim

Run B's differ only as `[pairs]` shows.

```json
{
 "kind": "diff-review",
 "base": "67c79f7cc466ae2d077eca7cc99111e897dd46db",
 "head": "5e139d3775c2b8b5c80879d6cb13a29b1b83b420",
 "repo": "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297",
 "reviewDir": "memory/builds/dClosedLoop/reviews",
 "specs": [
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-expansions-reviews-compared.md",
  "memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold-followup.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md",
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md",
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md"
 ],
 "byDesign": "- The build is design-only: no product code and no unit specs. Unit-level detail is absent by design and owed to the chain builds.\n- The owner's settled answers (RH-1, PIN-1, EX-1 to EX-3, DI-1, KN-1, LB-1 to LB-4, L-1 to L-6, the review system's R-1 to R-3, and the earlier F*, FR-*, FI-*, S-*, LR-* and RT-*) are decisions: a finding may show one contradicts a record or the tree, but does not re-argue the owner's choice.\n- Dated records keep what held when they were written: research returns, revision notes (the 2026-10-16 stale sweep's included), [forks], [settled], [review] and the session log's past entries.\n- Records written before 2026-10-16 that say Knowledge mean memory's library side (layer-library [settled], \"Older records' wording\").\n- A refuted finding stays refuted: the comparison records' none rows carry the skeptic's reason.\n- Generated files (memory/LIVE.md, the build README's generated regions, memory/map/generated/ and memory/gotchas/INDEX.md) are rendered and not under review.\n- The atlas page and its generator are an owner-facing view outside this review.\n- For an earlier round's H1 the fold chose the fix that denies by default: the unattended offer runs nothing from the adopter's tree. For round 2's M8 it chose a new key, build.release-ceiling, over a second reader for runtime.hold-ceiling. A finding may show either choice contradicted elsewhere, not re-argue it.",
 "checklist": "# recurring-bug-class checklist for 67c79f7cc..5e139d377 (16 changed file(s))\n# 19 class(es) selected by an anchor + 6 universal\n# by anchor specificity: 11 path · 4 directory · 4 basename; a cut tier prints one line per class\n# invariants are read at 67c79f7cc466; 0 that this subject adds, edits or takes out are listed as items, never by design\n\n- [ ] fixture-passes-by-finding-nothing (universal)\n      a test arm whose fixture never triggers the rule passes, and proves nothing\n      memory/gotchas/fixture-passes-by-finding-nothing.md\n\n- [ ] guard-above-a-fold-makes-its-fallback-dead (universal)\n      a guard added above a fold settles the predicate the fold's own fallback re-tests, leaving a dead arm that reads as coverage\n      memory/gotchas/guard-above-a-fold-makes-its-fallback-dead.md\n\n- [ ] heredoc-escape-reaches-the-regex (universal)\n      source written through a shell heredoc into a non-raw string turns an escape into a control byte, and the symptom never looks like a quoting problem\n      memory/gotchas/heredoc-escape-reaches-the-regex.md\n\n- [ ] inline-fence-swallows-the-rest-of-the-file (universal)\n      a triple-backtick written inline in prose opens a fence the reader never closes, so every section after it silently disappears from the checker's view\n      memory/gotchas/inline-fence-swallows-the-rest-of-the-file.md\n\n- [ ] staged-break-substitutes-a-synthetic-value (universal)\n      an arm that proves a mechanism by replacing the shipped value with a simpler one proves the mechanism for the simpler value\n      memory/gotchas/staged-break-substitutes-a-synthetic-value.md\n\n- [ ] two-answers-to-one-question (universal)\n      a fact stated in two places drifts, and the copies need not disagree loudly to be wrong\n      memory/gotchas/two-answers-to-one-question.md\n\n- [ ] policy-value-with-no-route (path)\n      a policy key catalogues a value that no item reading the key routes or witnesses, so a preset that selects the value cannot run\n      memory/gotchas/policy-value-with-no-route.md\n\n- [ ] foreign-code-runs-on-the-ambient-credential (path)\n      an unattended item runs code another repository authored, on the node's whole environment and ambient credential, so that repository's committers gain the node's rights\n      memory/gotchas/foreign-code-runs-on-the-ambient-credential.md\n\n- [ ] route-names-an-output-its-actor-never-emits (path)\n      a designed route or witness names an output, exit class or record that its actor never produces on that path, so the route is dead or waits forever\n      memory/gotchas/route-names-an-output-its-actor-never-emits.md\n\n- [ ] zero-witness-over-an-unnamed-population (path)\n      a scan whose zero is the witness names no population, so a skipped scan and a scan over less than the guarded boundary publishes both read as clean\n      memory/gotchas/zero-witness-over-an-unnamed-population.md\n\n- [ ] append-without-an-idempotence-key (path)\n      a command that appends to an append-only record declares no key, so a retried run writes the same row twice and a set-join witness stays green\n      memory/gotchas/append-without-an-idempotence-key.md\n\n- [ ] core-depends-on-an-optional-part (path)\n      a core item, leg, field or preset cannot run, or cannot be enforced, without an expansion or an optional component, and the dependency hides behind the guard or Absent clause that seems to degrade it\n      memory/gotchas/core-depends-on-an-optional-part.md\n\n- [ ] insert-after-a-key-that-occurs-twice (path)\n      a record edit inserts a row after the first match of a cell value that occurs in two tables, so the row lands in the wrong table and the right one never gains it\n      memory/gotchas/insert-after-a-key-that-occurs-twice.md\n\n- [ ] one-run-claim-recorded-as-agreed (path)\n      a comparison of two independent runs records a claim only one run made as what both found, so a single measurement carries the weight of agreement\n      memory/gotchas/one-run-claim-recorded-as-agreed.md\n\n- [ ] owner-item-without-its-reject-outcome (path)\n      a design hands a decision to the owner and routes only the yes, so a no leaves landed work with no route and a check that turns red on the default branch\n      memory/gotchas/owner-item-without-its-reject-outcome.md\n\n- [ ] parser-drops-rows-it-cannot-place (path)\n      a record-parsing instrument skips rows under a heading it does not know, or rows its pattern cannot read, and still prints a clean run, so its population shrinks without a word\n      memory/gotchas/parser-drops-rows-it-cannot-place.md\n\n- [ ] rule-stated-with-no-check-that-fails (path)\n      a principle, a constraint between two keys or another rule is added in prose with no check that can fail on its breach, so it binds nothing and nobody can see that it does not\n      memory/gotchas/rule-stated-with-no-check-that-fails.md\n\n- [ ] a-merge-of-the-default-branch-read-as-additions (directory) · memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md\n\n- [ ] amendment-leaves-its-other-half-standing (directory) · memory/gotchas/amendment-leaves-its-other-half-standing.md\n\n- [ ] ledger-token-wrapped-across-a-line-joins-nothing (directory) · memory/gotchas/ledger-token-wrapped-across-a-line-joins-nothing.md\n\n- [ ] retirement-inventory-misses-readers-by-value (directory) · memory/gotchas/retirement-inventory-misses-readers-by-value.md\n\n- [ ] record-without-serves-or-with-a-round-counter (basename) · memory/gotchas/record-without-serves-or-with-a-round-counter.md\n\n- [ ] rate-quoted-without-its-denominator (basename) · memory/gotchas/rate-quoted-without-its-denominator.md\n\n- [ ] a-folded-field-leaves-its-row-shape-docs-behind (basename) · memory/gotchas/a-folded-field-leaves-its-row-shape-docs-behind.md\n\n- [ ] git-rm-cached-refuses-a-diverged-index-blob (basename) · memory/gotchas/git-rm-cached-refuses-a-diverged-index-blob.md\n\n# by design — 0 invariant(s) this selection touches\n",
 "round": 3,
 "intensity": "light",
 "roles": {
  "diffFinder": "gov-diff-reviewer",
  "skeptic": "gov-skeptic",
  "synthesis": "gov-synthesizer"
 },
 "efforts": {
  "diffFinder": "medium",
  "skeptic": "medium",
  "synthesis": "medium"
 },
 "context": "The diff is round 3 of the closing review of the expansion fold in build dClosedLoop, a design-only build that re-architects gov onto one loop. Round 2 (memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold-followup.md) reviewed round 1's fixes and returned CLEAN WITH FIXES, 24 of 35 confirmed in 14 items; its confirmed findings are handed in as priorFindings. The owner asked for two independent medium-effort Tier-2 rounds on each of six pieces of the design that no review had read, their results compared; this is run A, and the other run's report is not evidence, so do not open it. The diff is the one commit 5e139d377 that folds them, and memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-expansions-reviews-compared.md [follow-up] names where each item went: the both-runs probe rewritten and every row it flagged cited; layer-expansions' kits.offer naming and refusing all five govkit target-side sites; build.release-ceiling with the supervisor's sweep; the event wait fanned out per build; deploy.close minted under the claim ref; the exit record naming its environment; the keep record. layer-runtime, flow-steps, layer-memory, v2, the gap register and five bug classes under memory/gotchas/ change with it. Read the diff without round 2's report and the generated files: git -C C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 diff 67c79f7cc466ae2d077eca7cc99111e897dd46db...5e139d3775c2b8b5c80879d6cb13a29b1b83b420 -- . ':(exclude)memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold-followup.md' ':(exclude)memory/gotchas/INDEX.md' ':(exclude)memory/builds/dClosedLoop/README.md'. The worktree is at a later HEAD, and later commits changed some of this text: verify each finding against the file at HEAD, cite HEAD's line, and report a defect only if HEAD still carries it. Review for three things: (1) a round-2 finding the fix leaves standing, fixes in part, or fixes in a way its own text contradicts; (2) a defect the fix itself introduced: an item, route, witness, key, value, record kind or lease with no producer, no arm or no home, or one fact now stated two ways; (3) text wrong about the tree, govkit's execution sites included. Write the report to memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold-round3-a.md. Its head carries an H1, then, within its first twelve lines, the line `**Serves:** diff-review PLAY-dClosedLoop-1`. It carries exactly one `## Verdict:` line, whose token is CLEAN, CLEAN WITH FIXES or BLOCKED and nothing else.",
 "priorFindings": [
  {
   "id": 1,
   "lens": "correctness",
   "ref": "memory/gotchas/one-run-claim-recorded-as-agreed.md:42",
   "claim": "C1 fixture-passes-by-finding-nothing: the new text says the class's probe was run over [agreement] and [cross] and went green. The committed probe (the comparison record's [closing-review]) only checks rows that spell '<layer> A and B'. No [agreement] row uses that spelling, because there both runs are named by the 'Both runs' column, so the probe reads every [agreement] row and checks none of them.",
   "severity": "high"
  },
  {
   "id": 2,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:240",
   "claim": "Text wrong about the tree: gap-deploy-13 says GOVKIT_RERENDER=0 'declines only the last two' sites (the [[regenerate]] argvs and gained kits' adopters). The switch also declines hook-fragment wiring, which runs the target's own settings-merge.py: run_fragment_merges at tools/govkit/govkit.py:5888 runs it with cwd=target, gated by _rerender_on at :11093-11099. kits.offer's 'runs nothing' mode (layer-expansions:445) lists three exclusions and omits this site. The gotcha's fixture (foreign-code-runs-on-the-ambient-credential.md:44) plants no settings-merge payload.",
   "severity": "high"
  },
  {
   "id": 4,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:336",
   "claim": "deploy.close is now 'minted under the build's claim ref, or under the wake's run lease once the build's lease is gone'. Its Needs include deploy.unlease, which deletes the build's lease refs, so the 'lease gone' condition holds on every path. Under at-landing and at-landing-maintain-owns, deploy.released passes at once and no wake lease exists. layer-memory:321-323 still says every record after the lease mints 'under the build's lease'.",
   "severity": "medium"
  },
  {
   "id": 5,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:149",
   "claim": "C10: life.quiesce hands a waiting landed build's withdraw to 'that item's owner item'. deploy.released raises that owner item only on a non-verified exit record or past runtime.hold-ceiling (flow-steps:333). While the wait is running normally, no owner item exists to receive the request.",
   "severity": "medium"
  },
  {
   "id": 6,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md:241",
   "claim": "Two copies of one rule disagree. The new paragraph keys Maintain's release-verify-failed ask by (SHA, environment) 'the key release.route files its own ask under'. maintain.file (:225) keys every Maintain ask by (reading, offender key). The event that fires the run, the slot's exit record, is keyed by SHA only (flow-steps:381, layer-expansions:378) and carries no environment.",
   "severity": "medium"
  },
  {
   "id": 7,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md:257",
   "claim": "C22, fixed in a way its own record contradicts. loop.file writes a kept row's disposition 'to its ledger state, with its date, through record'. The value ledger is 'a generated library view' (:211), its gate is 'the value ledger derived, never typed' (:215), and loop.price regenerates every column, state included, each week (:255).",
   "severity": "medium"
  },
  {
   "id": 9,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:1026",
   "claim": "C1: the journal-retention fixture checks only that an entry older than runtime.journal is pruned and that nothing is pruned under 'all'. No case keeps an entry younger than the limit.",
   "severity": "medium"
  },
  {
   "id": 10,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md:442",
   "claim": "Two copies of one fact disagree. kits.cut under owner-cut now fires 'each kits.watch-cadence period'. kits.watch-cadence's own row (:461) and v2's catalogue (:670) say it is 'the period of the currency probe and the fleet reading; the cut's is kits.cadence'.",
   "severity": "low"
  },
  {
   "id": 13,
   "lens": "correctness",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:711",
   "claim": "The event wait is 'keyed by (event, SHA) as a cadence instance is'. One exit record for a later SHA wakes every build whose landed SHA it contains (flow-steps:333), yet the key names no build. A cadence instance whose witness already shows is skipped.",
   "severity": "low"
  },
  {
   "id": 14,
   "lens": "seams",
   "ref": "memory/gotchas/one-run-claim-recorded-as-agreed.md:42",
   "claim": "C14/C8: the probe recorded as 'green once each row cited each run's line' cannot fail on any [agreement] row. Its predicate (compared record :313, CREDIT = '<layer> A and B') matches only that phrase, but [agreement] credits both runs through its 'Both runs' column. Its 'rows read: 52' are 46 [agreement] rows and 6 [cross] rows.",
   "severity": "high"
  },
  {
   "id": 15,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:786",
   "claim": "C8: the fold split the scan's populations across boundaries (:778 the prepare covers commits, tracked files and memory/; :780 the ref-push path covers mailbox, card, leases and claims, one object per push). It kept the rule that 'an empty population is a dead probe, never green' for every population the witness names.",
   "severity": "medium"
  },
  {
   "id": 16,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:711",
   "claim": "C11: deploy.released's event wait is 'keyed by (event, SHA) as a cadence instance is', and the supervisor skips an instance whose key already has a witness (:704-706). The key leaves out the build, but one exit record answers several builds.",
   "severity": "medium"
  },
  {
   "id": 17,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:333",
   "claim": "The new arm 'no exit record within runtime.hold-ceiling → the same owner item' has no driver. The item runs only when the exit record's event wakes it, under that wake's lease (layer-runtime :710-713), so with no record there is no wake, no lease and no supervisor. The arm also reuses runtime.hold-ceiling (6 hours), whose rows at v2:609 and layer-runtime:836 define it as the usage-limit hold of [supervise].",
   "severity": "medium"
  },
  {
   "id": 18,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md:257",
   "claim": "The M6 fix writes 'a kept row's disposition ... to its ledger state, with its date, through record'. Yet the value ledger is 'a generated view, never typed' (:80), a 'generated library view' (:211), gated as 'the value ledger derived, never typed' (:215), and regenerated in full each week by loop.price (:255).",
   "severity": "medium"
  },
  {
   "id": 19,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md:241",
   "claim": "C11: Maintain's release-verify-failed ask is keyed by (SHA, environment), but the run fires from the release slot's exit record, which is 'keyed by SHA with an outcome' (flow-steps:380; [core-points]) and carries no environment. maintain.file also keys its asks by (reading, offender key) (:225), a second key for the same ask.",
   "severity": "medium"
  },
  {
   "id": 20,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:452",
   "claim": "life.quiesce now hands a landed build's request 'to that item's owner item'. deploy.released raises that owner item only on a non-verified outcome or a ceiling breach (:333), so while the wait is pending there is no owner item to receive the request, and under close-only no lease-holding executor runs life.quiesce either.",
   "severity": "medium"
  },
  {
   "id": 21,
   "lens": "seams",
   "ref": "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md:461",
   "claim": "kits.cut under owner-cut now fires 'each kits.watch-cadence period' (:442), but kits.watch-cadence's own rows still say it serves 'the currency probe and the fleet reading ... the cut's is kits.cadence' (here and v2:670).",
   "severity": "low"
  },
  {
   "id": 25,
   "lens": "verification",
   "ref": "memory/gotchas/one-run-claim-recorded-as-agreed.md:42",
   "claim": "C15: the both-runs probe recorded as green over [agreement] and [cross] reads 52 rows but its predicate matches none of the [agreement] rows. It matches only the literal '<layer> A and B', so 39 [agreement] rows whose 'Both runs' cell credits both runs, and [cross]'s 'observability B, distribution A' row, can never fail it.",
   "severity": "high"
  },
  {
   "id": 26,
   "lens": "verification",
   "ref": "memory/gotchas/foreign-code-runs-on-the-ambient-credential.md:44",
   "claim": "C9: the new fixture plants a payload in three kinds of target-side code (a regenerate argv, an adopt script run by [check], a workspace hook). govkit's update runs two more kinds from the target tree: the [[hole]] discharge probes (run_hole_probes at govkit.py:10953 and :11800, cwd=target, at :5012) and the target's own settings-merge.py during fragment wiring (run_fragment_merges at :11094, run with cwd=target at :5888/:5897/:5912).",
   "severity": "high"
  },
  {
   "id": 27,
   "lens": "verification",
   "ref": "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md:257",
   "claim": "The kept-row fix writes the owner's 'kept' disposition 'to its ledger state ... through record'. But the value ledger is 'a generated view, never typed' (:80, :211), gated 'the value ledger derived, never typed' (:215), and loop.price regenerates it, state included (:255).",
   "severity": "medium"
  },
  {
   "id": 28,
   "lens": "verification",
   "ref": "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:933",
   "claim": "C12: dDeclaredLoop's new core-only preset load is 'refused only for a value on a core key that selects an absent expansion, seen red on a planted Absent clause that refuses by key'. That seen-red covers only over-refusal.",
   "severity": "medium"
  },
  {
   "id": 30,
   "lens": "verification",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:1026",
   "claim": "The journal-retention fixture asserts only that entries older than runtime.journal days are pruned, and that none are pruned under all. No entry inside the window is planted.",
   "severity": "medium"
  },
  {
   "id": 33,
   "lens": "verification",
   "ref": "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:710",
   "claim": "The new event wait (deploy.released woken by the exit record, keyed by (event, SHA), run under the wake's own run lease, with a runtime.hold-ceiling owner item) has no fixture in [tests]. `cadence` covers only periods, and `limits` covers the ceiling only for a StopFailure hold.",
   "severity": "medium"
  },
  {
   "id": 34,
   "lens": "verification",
   "ref": "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md:241",
   "claim": "Maintain files the release-verify-failed ask 'keyed by (SHA, environment)', but its event is produced by the slot's exit record, which is keyed by SHA with an outcome and carries no environment (flow-steps:380, layer-expansions:179, :637).",
   "severity": "medium"
  }
 ]
}
```

## [compare-lexicon] The lexicon pair's comparison, run over the record

```text
$ python compare_rounds.py reviews/2026-10-16-review-PLAY-dClosedLoop-1-lexicon-a.md \
    reviews/2026-10-16-review-PLAY-dClosedLoop-1-lexicon-b.md \
    build/2026-10-16-build-PLAY-dClosedLoop-1-debt-reviews-compared.md \
    build/2026-10-14-build-PLAY-dClosedLoop-1-session-log.md wf_14950dae-859 wf_b52591b3-8f4 map-lexicon
== runs
A: raw 53, confirmed 47, refuted 6, precision 0.89, high findings 3, agents 12, out 231.1k (sum of returned lines)
B: raw 56, confirmed 49, refuted 7, precision 0.88, high findings 3, agents 12, out 230.8k (sum of returned lines)
== defects
map rows 52, confirmed defects 49, refuted-only 3
both 23, A only 13, B only 13
A alone covers 36 of 49 (73%)
B alone covers 36 of 49 (73%)
overlap (Jaccard) 0.47
Chapman estimate of the population: 56.0, so about 7 found by neither
A only: drift-vs-classes, replay-threshold, pack-fixture, prototype-live-import, forced-by-name-route, suggest-forced-aware, no-pack-owner-route, nouns-table, drain-count, pins-plain-edit, gaps-cite-asks, raise-misread, fixture-undefined
B only: drift-enforcement-site, pack-selection-inputs, pack-row-validation, vocabulary-proposal-route, init-row-inventory, leg-placement, chain-order, doc-reads-stale, three-pins, gap2-example, foreign-ask, main-red-stale, tag-check-point
== severity (a defect takes its highest confirmed grade per round)
high defects 4: ratified-readers, acquire-family, map-extraction-states, declaration-home
  ratified-readers: A 3 B 2
  acquire-family: A 3 B 3
  map-extraction-states: A 3 B 2
  declaration-home: A 2 B 3
shared defects graded alike 14 of 23
== lenses behind the defects one round alone found
A: coherence 4, grounding 4, reuse 3, failure-envelope 1, blast-radius 1
B: coherence 6, blast-radius 3, failure-envelope 2, grounding 2, reuse 1
== refuted findings and their twins
A27 (bar-comparison-seam): confirmed twin A12, B15
A33 (declaration-second-carrier): confirmed twin none
A41 (ratified-readers): confirmed twin A3, A30, A37, B2, B30, B38
A45 (commit-check-seam): confirmed twin A29, B8, B33
A50 (pack-selection-inputs): confirmed twin B50
A52 (declaration-home): confirmed twin A19, B23, B35, B48
B21 (import-census): confirmed twin none
B25 (map-dependency-undeclared): confirmed twin A18, A28, A36, A40, B5, B28, B42, B52
B32 (replay-threshold): confirmed twin A8
B36 (forced-by-name-route): confirmed twin A32
B43 (later-records): confirmed twin A9, A20, A51, B27, B56
B51 (commit-check-seam): confirmed twin A29, B8, B33
B53 (keys-absent): confirmed twin none
```

## [compare-review-system] The review-system pair's comparison, run over the record

```text
$ python compare_rounds.py reviews/2026-10-16-review-PLAY-dClosedLoop-1-review-system-a.md \
    reviews/2026-10-16-review-PLAY-dClosedLoop-1-review-system-b.md \
    build/2026-10-16-build-PLAY-dClosedLoop-1-debt-reviews-compared.md \
    build/2026-10-14-build-PLAY-dClosedLoop-1-session-log.md wf_84ae201a-775 wf_dd2730e2-e29 map-review-system
== runs
A: raw 47, confirmed 41, refuted 6, precision 0.87, high findings 1, agents 12, out 224.7k (sum of returned lines)
B: raw 45, confirmed 39, refuted 6, precision 0.87, high findings 0, agents 12, out 207.6k (sum of returned lines)
== defects
map rows 38, confirmed defects 35, refuted-only 3
both 19, A only 10, B only 6
A alone covers 29 of 35 (83%)
B alone covers 25 of 35 (71%)
overlap (Jaccard) 0.54
Chapman estimate of the population: 38.0, so about 3 found by neither
A only: stale-gap-review-03, preset-two-names, fix-verdict-test, grade-test-synthetic, batch-test-weak, opt-in-tests, replay-blindness, opt-in-depends-on-later-build, orphan-check-wrong-half, leg-manifest-dependency
B only: twins-test-positive-only, replay-scorer, opt-in-preset-meaning, universal-budget, grade-per-id-f2, review-driver-nonexistent
== severity (a defect takes its highest confirmed grade per round)
high defects 2: replay-blindness, replay-threshold
  replay-blindness: A 3 B 0
  replay-threshold: A 3 B 2
shared defects graded alike 15 of 19
== lenses behind the defects one round alone found
A: coherence 6, grounding 2, failure-envelope 2, reuse 1, blast-radius 1
B: reuse 3, coherence 2, failure-envelope 1, blast-radius 1, grounding 1
== refuted findings and their twins
A14 (replay-threshold): confirmed twin A4, A44, B11, B43
A21 (replay-rule0): confirmed twin none
A24 (replay-scorer): confirmed twin B43
A29 (twins-input): confirmed twin none
A34 (replay-scorer): confirmed twin B43
A47 (leg-manifest-dependency): confirmed twin A36
B10 (ordering-unenforced): confirmed twin A2, B16
B19 (batch-contiguity): confirmed twin A16, B36
B25 (design-audit-selection): confirmed twin A1, A13, A30, B8, B12
B35 (opt-in-extension): confirmed twin A7, A19, A26, A37, B9, B26, B45
B37 (restatement-gate): confirmed twin none
B42 (batch-sort-key): confirmed twin A42, B15
```
