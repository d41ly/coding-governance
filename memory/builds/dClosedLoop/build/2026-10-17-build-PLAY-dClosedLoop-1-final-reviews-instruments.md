# The final reviews' instruments: the args and the script that wrote them

**Serves:** research PLAY-dClosedLoop-1

The args of dispatches 85 and 86, written by the script below from the tree and the two bug-class
checklists. The runs are in `build/2026-10-17-build-PLAY-dClosedLoop-1-final-reviews.md`.

## [builder] The script that writes the args

The closing review's checklist is `gotchas.py --for-diff 9b188202a..cdcea2c9b`, and the audit's is
`gotchas.py --for-paths` over its two records, both run at `cdcea2c9b`.

```python
"""Write the args of the two reviews the owner asked for on 2026-10-17: "delete the duplicate artifact first,
then do both the closing review of the folds and a tier-2 review of the systems and retrofit rounds."

- The closing review of the folds is a diff review over every fold commit since the debt round's twelve
  reviews returned, `9b188202a..cdcea2c9b`, round 1, full: no review has read the folds, and the folds
  touch the dispatcher's binding, the release hold and the adopter sandbox, so the security and intent
  lenses run too. It runs at the closing-review workflow's declared efforts.
- The systems and retrofit rounds are two design records no review has read: one spec audit over both,
  round 1, full, at the spec-review workflow's declared efforts, with the records their answers were folded
  into, and every research return behind them, as specs.

Each run's efforts are what `handoff.py stage-efforts <workflow>` prints for its workflow.
Usage: python make_final_args.py <out-dir>   (from the worktree root)
Refuses unless every spec exists, both ranges resolve, and both checklists are present.
"""
import json
import pathlib
import subprocess
import sys

OUT = pathlib.Path(sys.argv[1])
REPO = "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297"
SP = ("C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/"
      "1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad")
B = "memory/builds/dClosedLoop/build/2026-10-1"
RV = "memory/builds/dClosedLoop/reviews/2026-10-1"


def rec(date, name):
    return f"{B}{date}-build-PLAY-dClosedLoop-1-{name}.md"


def rev(date, name):
    return f"{RV}{date}-review-PLAY-dClosedLoop-1-{name}.md"


def git(*a):
    return subprocess.run(["git", "-C", REPO, *a], capture_output=True, text=True, check=True).stdout.strip()


def efforts(workflow):
    out = subprocess.run([sys.executable, "tools/roles/handoff.py", "stage-efforts", workflow], cwd=REPO,
                         capture_output=True, text=True, check=True).stdout.strip()
    return json.loads(out)


V2, GAPS = rec("4", "architecture-v2"), rec("4", "gap-register")
STEPS, FLOW = rec("5", "flow-steps"), rec("5", "layer-flow")
ROLES, MEM, RT = rec("5", "layer-roles"), rec("5", "layer-memory"), rec("5", "layer-runtime")
INSTR, LIB, EXP = rec("5", "layer-instruction"), rec("6", "layer-library"), rec("6", "layer-expansions")
LEX, RSYS = rec("5", "lexicon"), rec("5", "review-system")
CMP, INS = rec("6", "debt-reviews-compared"), rec("6", "debt-reviews-compared-instruments")
SYS, RET = rec("6", "systems"), rec("7", "retrofit")
SESSION = rec("4", "session-log")

ANSWERS = ("LX-1 to LX-3, RV-1, AN-1, AN-2, IW-1, IW-2, RS-1, RS-2, MS-1 to MS-3, RF-1 to RF-6, RH-1, PIN-1, EX-1 "
           "to EX-3, DI-1, KN-1, LB-1 to LB-4, L-1 to L-6, the review system's R-1 to R-3, and the earlier F*, FR-*, "
           "FI-*, S-*, LR-* and RT-*")
KNOWLEDGE = ("- Records written before 2026-10-16 that say Knowledge mean memory's library side (layer-library "
             "[settled], \"Older records' wording\").")
GENERATED = ("- Generated files (memory/LIVE.md, the build README's generated regions, memory/map/generated/ and "
             "memory/gotchas/INDEX.md) are rendered and not under review.\n"
             "- The atlas page and its generator are an owner-facing view outside this review.")
TAIL = ("Write the report to {report}. Its head carries an H1, then, within its first twelve lines, the line "
        "`**Serves:** {kind} PLAY-dClosedLoop-1`. It carries exactly one `## Verdict:` line, whose token is CLEAN, "
        "CLEAN WITH FIXES or BLOCKED and nothing else.")
AT_HEAD = ("The worktree may be at a later HEAD: verify each finding against the file at HEAD, cite HEAD's line, and "
           "report a defect only if HEAD still carries it.")

FOLDS_BY_DESIGN = (
    "- The build is design-only: no product code and no unit specs. Unit-level detail is absent by design and owed "
    "to the chain builds.\n"
    f"- The owner's settled answers ({ANSWERS}) are decisions: a finding may show one contradicts a record or the "
    "tree, but does not re-argue the owner's choice.\n"
    "- Dated records keep what held when they were written: research returns, review reports, revision notes, "
    "[forks], [settled], [review] and the session log's past entries.\n"
    f"{KNOWLEDGE}\n"
    "- A refuted finding stays refuted: the comparison record's none rows carry the skeptic's reason. Two refuted "
    "rows the skeptics found real but older than the diff read `amend: refuted only as older than the diff`, and "
    "their fixes were taken anyway.\n"
    "- The non-default preset values of the thirty-one keys the systems and retrofit fold added were assigned by "
    "analogy, as v2's dated note says: a finding may show one inconsistent with its preset or with an owner's "
    "answer, not that it is unasked.\n"
    "- Each fold section's classes column copies the confirmed findings' classes from the two runs' ledgers.\n"
    f"{GENERATED}")
SPEC_BY_DESIGN = (
    "- The build is design-only: no product code and no unit specs; each chain build writes its own specs later, so "
    "unit-level implementation detail is absent by design.\n"
    "- The owner's settled answers, recorded in each record's [answers], are decisions: a finding may show that one "
    "contradicts another record, the platform or the tree, but does not re-argue the owner's choice.\n"
    "- Records outside memory/builds/dClosedLoop/ are not under review, and the research returns are evidence, not "
    "subjects.\n"
    "- The non-default preset values of the keys these rounds added were assigned by analogy, as v2's dated note "
    "says: a finding may show one inconsistent with its preset or with an owner's answer, not that it is unasked.\n"
    f"{KNOWLEDGE}\n"
    f"{GENERATED}")
SIX = ("Audit each record as an architecture spec, against six questions: (1) internal consistency: do its "
       "components, policies, build units, gaps and answers agree with each other; (2) consistency with the sibling "
       "records in specs: v2's principles, policy catalogue and chain, the gap register and the layers' records, the "
       "two subjects with each other included; (3) feasibility against the measured facts in the research returns, "
       "the records in specs and the tree: a mechanism the platform or the tree cannot support, or a claim the "
       "evidence does not bear out; (4) missing mechanisms: {missing}; (5) claims that are unenforced or untestable "
       "as written; (6) extension points, {ext}, that could not in fact be filled without changing code. Address each "
       "finding by the record's file and section tag, such as {tags}.")

REPORT_A, REPORT_B = rev("7", "debt-folds"), rev("7", "systems-retrofit")
BASE, HEAD = git("rev-parse", "9b188202a"), git("rev-parse", "cdcea2c9b")
EXCL_A = [SESSION, "memory/builds/dClosedLoop/reviews", "memory/gotchas/INDEX.md", "memory/builds/dClosedLoop/README.md",
          "memory/LIVE.md", "memory/map/generated"]
excl = " ".join(f"':(exclude){x}'" for x in EXCL_A)

CONTEXT_A = (
    "The diff is the debt round's folds in build dClosedLoop, a design-only build that re-architects gov onto one "
    "loop. The owner asked for the six pieces of the design that no review had read to be reviewed twice each at "
    f"medium effort. The twelve reports were compared defect by defect in {CMP}: each [map-<pair>] section places "
    "every finding of a pair on a defect, and [summary] and [patterns] set the six pairs side by side. Each pair was "
    "then folded. The lexicon pair (02919e4f4, whose broken table rows 402753c0c repaired) and the review-system "
    f"pair (2d61e9e45) each have a [debt-fold] section in their own record ({LEX}, {RSYS}). The runtime-fold pair "
    "(446117047), the layers round's round-3 fold pair (1b759b620), the library pair (e56925e3d) and the expansion "
    f"pair (e2e899e42, with 43f5d1710) each have a [fold-<pair>] section in {CMP}. The lexicon and review-system "
    "folds' owed fixes landed in cc96e0217, and the systems and retrofit rounds' answers were folded into v2, the gap "
    "register and their own records in 36fc6d572. Each fold section names, for every map row, its disposition, where "
    f"its fix sits and its classes. The folds' probes and their runs are in {INS}: [summarize], [contamination], "
    "[probes-library] and [probes-expansions]. No review has read any of the folds, and this is their closing "
    "review, round 1. Read the diff without the review reports, the session log and the generated files: "
    f"git -C {REPO} diff {BASE}...{HEAD} -- . {excl}. " + AT_HEAD + " Review for four things: (1) a map row whose "
    "fix, at the place its fold section names, is missing, partial, or contradicted by its own text or another "
    "record; (2) a defect a fold introduced: an item, route, witness, key, value, record kind, lease, fixture or gap "
    "with no producer, no arm, no owner or no home, or one fact now stated two ways; (3) a settled answer "
    "misapplied, or a probe whose predicate or population does not bear the figure the records quote; (4) text wrong "
    "about the tree, the hooks', govkit's and the lander's code included. " + TAIL)

CONTEXT_B = (
    "The subjects are two design records of build dClosedLoop, a design-only build that re-architects gov onto one "
    f"loop. {SYS} designs five systems that cross the layers: tags, code annotations, instruction writing, role "
    f"workflow shapes and memory structure. {RET} designs how gov retrofits its practices into a repository that "
    "already has a codebase and practices of its own, a sixth system across the layers. The owner asked for both "
    "(each record's [words]). Two researchers measured each system and the retrofit; their returns are among the "
    "specs. The owner answered every fork: AN-1, AN-2, IW-1, IW-2, RS-1, RS-2 and MS-1 to MS-3 in the systems "
    "record's [answers], and RF-1 to RF-6 in the retrofit record's. Their keys, gaps and chain units were folded "
    "into v2 and the gap register in 36fc6d572. No review has read either record. A statement in v2, the register "
    "or a layer record that contradicts these records, or that the fold carried wrongly, is a finding. " +
    SIX.format(missing="anything a system or the retrofit must provide to the flow, the roles, the layers or each "
                       "other that the design omits",
               ext="such as a tag namespace, a role shape, a record kind's sections or a ledger population",
               tags="[agreement], [cross], [design-tags], [design-role-shapes], [answers] and [gaps-proposed] in the "
                    "systems record, and [ledger], [seed], [drain], [owners], [keys] and [answers] in the retrofit "
                    "record") + " " + TAIL)

SPECS_A = [CMP, INS, LEX, RSYS, RT, STEPS, MEM, ROLES, LIB, EXP, V2, GAPS, SYS, RET, rec("5", "runtime-reviews-compared"),
           rec("6", "layers-reviews-compared"), rec("6", "expansions-reviews-compared")]
RESEARCH = [rec("6", f"research-{s}-{r}") for s in ("tags", "annotations", "instruction-writing", "role-shapes",
                                                       "memory-structure") for r in "ab"]
RESEARCH += [rec("7", "research-retrofit-a"), rec("7", "research-retrofit-b"), rec("7", "research-retrofit-instruments")]
SPECS_B = [V2, GAPS, INSTR, MEM, ROLES, RT, STEPS, LIB, EXP] + RESEARCH

OUT.mkdir(parents=True, exist_ok=True)
cl_a = (OUT / "cl-debt-folds.txt").read_bytes().decode("utf-8").replace("\r\n", "\n")
cl_b = (OUT / "cl-systems-retrofit.txt").read_bytes().decode("utf-8").replace("\r\n", "\n")
for specs in (SPECS_A, SPECS_B):
    missing = [s for s in specs if not (pathlib.Path(REPO) / s).exists()]
    if missing:
        sys.exit(f"specs that do not exist: {missing}")
args_a = {"kind": "diff-review", "base": BASE, "head": HEAD, "repo": REPO, "reviewDir": "memory/builds/dClosedLoop/reviews",
          "specs": SPECS_A, "byDesign": FOLDS_BY_DESIGN, "checklist": cl_a, "round": 1, "intensity": "full",
          "roles": {"diffFinder": "gov-diff-reviewer", "skeptic": "gov-skeptic", "synthesis": "gov-synthesizer"},
          "efforts": efforts("closing-review"),
          "context": CONTEXT_A.format(report=REPORT_A, kind="diff-review")}
args_b = {"kind": "spec-audit", "repo": REPO, "reviewDir": "memory/builds/dClosedLoop/reviews", "specs": SPECS_B,
          "byDesign": SPEC_BY_DESIGN, "checklist": cl_b,
          "subjects": [{"path": SYS, "blob": git("rev-parse", "HEAD:" + SYS)},
                       {"path": RET, "blob": git("rev-parse", "HEAD:" + RET)}],
          "scratch": f"{SP}/review-systems-retrofit", "round": 1, "intensity": "full",
          "roles": {"specFinder": "gov-spec-reviewer", "skeptic": "gov-skeptic", "synthesis": "gov-synthesizer"},
          "efforts": efforts("spec-review"),
          "context": CONTEXT_B.format(report=REPORT_B, kind="spec-audit")}
for name, args in (("args-debt-folds.json", args_a), ("args-systems-retrofit.json", args_b)):
    with open(OUT / name, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(args, fh, indent=1, ensure_ascii=False)
    print(f"{name}: {len(json.dumps(args))} chars, {len(args['specs'])} specs, round {args['round']}, "
          f"{args['intensity']}, efforts {args['efforts']}")
```

## [args-debt-folds] Dispatch 85's args, verbatim

```json
{
 "kind": "diff-review",
 "base": "9b188202a34ad9de662e9317d9433f1304228dd5",
 "head": "cdcea2c9beee2f506df266b08ae7a45a18df3593",
 "repo": "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297",
 "reviewDir": "memory/builds/dClosedLoop/reviews",
 "specs": [
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-debt-reviews-compared.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-debt-reviews-compared-instruments.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-review-system.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md",
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md",
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md",
  "memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-runtime-reviews-compared.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layers-reviews-compared.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-expansions-reviews-compared.md"
 ],
 "byDesign": "- The build is design-only: no product code and no unit specs. Unit-level detail is absent by design and owed to the chain builds.\n- The owner's settled answers (LX-1 to LX-3, RV-1, AN-1, AN-2, IW-1, IW-2, RS-1, RS-2, MS-1 to MS-3, RF-1 to RF-6, RH-1, PIN-1, EX-1 to EX-3, DI-1, KN-1, LB-1 to LB-4, L-1 to L-6, the review system's R-1 to R-3, and the earlier F*, FR-*, FI-*, S-*, LR-* and RT-*) are decisions: a finding may show one contradicts a record or the tree, but does not re-argue the owner's choice.\n- Dated records keep what held when they were written: research returns, review reports, revision notes, [forks], [settled], [review] and the session log's past entries.\n- Records written before 2026-10-16 that say Knowledge mean memory's library side (layer-library [settled], \"Older records' wording\").\n- A refuted finding stays refuted: the comparison record's none rows carry the skeptic's reason. Two refuted rows the skeptics found real but older than the diff read `amend: refuted only as older than the diff`, and their fixes were taken anyway.\n- The non-default preset values of the thirty-one keys the systems and retrofit fold added were assigned by analogy, as v2's dated note says: a finding may show one inconsistent with its preset or with an owner's answer, not that it is unasked.\n- Each fold section's classes column copies the confirmed findings' classes from the two runs' ledgers.\n- Generated files (memory/LIVE.md, the build README's generated regions, memory/map/generated/ and memory/gotchas/INDEX.md) are rendered and not under review.\n- The atlas page and its generator are an owner-facing view outside this review.",
 "checklist": "# recurring-bug-class checklist for 9b188202a..cdcea2c9b (31 changed file(s))\n# 20 class(es) selected by an anchor + 6 universal\n# by anchor specificity: 13 path · 4 directory · 3 basename; a cut tier prints one line per class\n# invariants are read at 9b188202a34a; 0 that this subject adds, edits or takes out are listed as items, never by design\n\n- [ ] fixture-passes-by-finding-nothing (universal)\n      a test arm whose fixture never triggers the rule passes, and proves nothing\n      memory/gotchas/fixture-passes-by-finding-nothing.md\n\n- [ ] guard-above-a-fold-makes-its-fallback-dead (universal)\n      a guard added above a fold settles the predicate the fold's own fallback re-tests, leaving a dead arm that reads as coverage\n      memory/gotchas/guard-above-a-fold-makes-its-fallback-dead.md\n\n- [ ] heredoc-escape-reaches-the-regex (universal)\n      source written through a shell heredoc into a non-raw string turns an escape into a control byte, and the symptom never looks like a quoting problem\n      memory/gotchas/heredoc-escape-reaches-the-regex.md\n\n- [ ] inline-fence-swallows-the-rest-of-the-file (universal)\n      a triple-backtick written inline in prose opens a fence the reader never closes, so every section after it silently disappears from the checker's view\n      memory/gotchas/inline-fence-swallows-the-rest-of-the-file.md\n\n- [ ] staged-break-substitutes-a-synthetic-value (universal)\n      an arm that proves a mechanism by replacing the shipped value with a simpler one proves the mechanism for the simpler value\n      memory/gotchas/staged-break-substitutes-a-synthetic-value.md\n\n- [ ] two-answers-to-one-question (universal)\n      a fact stated in two places drifts, and the copies need not disagree loudly to be wrong\n      memory/gotchas/two-answers-to-one-question.md\n\n- [ ] policy-value-with-no-route (path)\n      a policy key catalogues a value that no item reading the key routes or witnesses, so a preset that selects the value cannot run\n      memory/gotchas/policy-value-with-no-route.md\n\n- [ ] foreign-code-runs-on-the-ambient-credential (path)\n      an unattended item runs code another repository authored, on the node's whole environment and ambient credential, so that repository's committers gain the node's rights\n      memory/gotchas/foreign-code-runs-on-the-ambient-credential.md\n\n- [ ] one-run-claim-recorded-as-agreed (path)\n      a comparison of two independent runs records a claim only one run made as what both found, so a single measurement carries the weight of agreement\n      memory/gotchas/one-run-claim-recorded-as-agreed.md\n\n- [ ] parser-drops-rows-it-cannot-place (path)\n      a record-parsing instrument skips rows under a heading it does not know, or rows its pattern cannot read, and still prints a clean run, so its population shrinks without a word\n      memory/gotchas/parser-drops-rows-it-cannot-place.md\n\n- [ ] pipe-in-a-code-span-splits-a-table-cell (path)\n      a markdown table cell holding a pipe, even inside backticks, splits into extra cells, so a reader that splits the row on its pipes reads the wrong cell as a column\n      memory/gotchas/pipe-in-a-code-span-splits-a-table-cell.md\n\n- [ ] route-names-an-output-its-actor-never-emits (path)\n      a designed route or witness names an output, exit class or record that its actor never produces on that path, so the route is dead or waits forever\n      memory/gotchas/route-names-an-output-its-actor-never-emits.md\n\n- [ ] zero-witness-over-an-unnamed-population (path)\n      a scan whose zero is the witness names no population, so a skipped scan and a scan over less than the guarded boundary publishes both read as clean\n      memory/gotchas/zero-witness-over-an-unnamed-population.md\n\n- [ ] append-without-an-idempotence-key (path)\n      a command that appends to an append-only record declares no key, so a retried run writes the same row twice and a set-join witness stays green\n      memory/gotchas/append-without-an-idempotence-key.md\n\n- [ ] core-depends-on-an-optional-part (path)\n      a core item, leg, field or preset cannot run, or cannot be enforced, without an expansion or an optional component, and the dependency hides behind the guard or Absent clause that seems to degrade it\n      memory/gotchas/core-depends-on-an-optional-part.md\n\n- [ ] insert-after-a-key-that-occurs-twice (path)\n      a record edit inserts a row after the first match of a cell value that occurs in two tables, so the row lands in the wrong table and the right one never gains it\n      memory/gotchas/insert-after-a-key-that-occurs-twice.md\n\n- [ ] owner-item-without-its-reject-outcome (path)\n      a design hands a decision to the owner and routes only the yes, so a no leaves landed work with no route and a check that turns red on the default branch\n      memory/gotchas/owner-item-without-its-reject-outcome.md\n\n- [ ] rate-quoted-without-its-denominator (path)\n      a rate put to the owner in a fork divides by the wrong population, so the option's own cost reads several times off\n      memory/gotchas/rate-quoted-without-its-denominator.md\n\n- [ ] rule-stated-with-no-check-that-fails (path)\n      a principle, a constraint between two keys or another rule is added in prose with no check that can fail on its breach, so it binds nothing and nobody can see that it does not\n      memory/gotchas/rule-stated-with-no-check-that-fails.md\n\n- [ ] a-merge-of-the-default-branch-read-as-additions (directory) · memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md\n\n- [ ] amendment-leaves-its-other-half-standing (directory) · memory/gotchas/amendment-leaves-its-other-half-standing.md\n\n- [ ] ledger-token-wrapped-across-a-line-joins-nothing (directory) · memory/gotchas/ledger-token-wrapped-across-a-line-joins-nothing.md\n\n- [ ] retirement-inventory-misses-readers-by-value (directory) · memory/gotchas/retirement-inventory-misses-readers-by-value.md\n\n- [ ] record-without-serves-or-with-a-round-counter (basename) · memory/gotchas/record-without-serves-or-with-a-round-counter.md\n\n- [ ] a-folded-field-leaves-its-row-shape-docs-behind (basename) · memory/gotchas/a-folded-field-leaves-its-row-shape-docs-behind.md\n\n- [ ] git-rm-cached-refuses-a-diverged-index-blob (basename) · memory/gotchas/git-rm-cached-refuses-a-diverged-index-blob.md\n\n# by design — 0 invariant(s) this selection touches\n",
 "round": 1,
 "intensity": "full",
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
 "context": "The diff is the debt round's folds in build dClosedLoop, a design-only build that re-architects gov onto one loop. The owner asked for the six pieces of the design that no review had read to be reviewed twice each at medium effort. The twelve reports were compared defect by defect in memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-debt-reviews-compared.md: each [map-<pair>] section places every finding of a pair on a defect, and [summary] and [patterns] set the six pairs side by side. Each pair was then folded. The lexicon pair (02919e4f4, whose broken table rows 402753c0c repaired) and the review-system pair (2d61e9e45) each have a [debt-fold] section in their own record (memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md, memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-review-system.md). The runtime-fold pair (446117047), the layers round's round-3 fold pair (1b759b620), the library pair (e56925e3d) and the expansion pair (e2e899e42, with 43f5d1710) each have a [fold-<pair>] section in memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-debt-reviews-compared.md. The lexicon and review-system folds' owed fixes landed in cc96e0217, and the systems and retrofit rounds' answers were folded into v2, the gap register and their own records in 36fc6d572. Each fold section names, for every map row, its disposition, where its fix sits and its classes. The folds' probes and their runs are in memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-debt-reviews-compared-instruments.md: [summarize], [contamination], [probes-library] and [probes-expansions]. No review has read any of the folds, and this is their closing review, round 1. Read the diff without the review reports, the session log and the generated files: git -C C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 diff 9b188202a34ad9de662e9317d9433f1304228dd5...cdcea2c9beee2f506df266b08ae7a45a18df3593 -- . ':(exclude)memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-session-log.md' ':(exclude)memory/builds/dClosedLoop/reviews' ':(exclude)memory/gotchas/INDEX.md' ':(exclude)memory/builds/dClosedLoop/README.md' ':(exclude)memory/LIVE.md' ':(exclude)memory/map/generated'. The worktree may be at a later HEAD: verify each finding against the file at HEAD, cite HEAD's line, and report a defect only if HEAD still carries it. Review for four things: (1) a map row whose fix, at the place its fold section names, is missing, partial, or contradicted by its own text or another record; (2) a defect a fold introduced: an item, route, witness, key, value, record kind, lease, fixture or gap with no producer, no arm, no owner or no home, or one fact now stated two ways; (3) a settled answer misapplied, or a probe whose predicate or population does not bear the figure the records quote; (4) text wrong about the tree, the hooks', govkit's and the lander's code included. Write the report to memory/builds/dClosedLoop/reviews/2026-10-17-review-PLAY-dClosedLoop-1-debt-folds.md. Its head carries an H1, then, within its first twelve lines, the line `**Serves:** diff-review PLAY-dClosedLoop-1`. It carries exactly one `## Verdict:` line, whose token is CLEAN, CLEAN WITH FIXES or BLOCKED and nothing else."
}
```

## [args-systems-retrofit] Dispatch 86's args, verbatim

```json
{
 "kind": "spec-audit",
 "repo": "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297",
 "reviewDir": "memory/builds/dClosedLoop/reviews",
 "specs": [
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md",
  "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-research-tags-a.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-research-tags-b.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-research-annotations-a.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-research-annotations-b.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-research-instruction-writing-a.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-research-instruction-writing-b.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-research-role-shapes-a.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-research-role-shapes-b.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-research-memory-structure-a.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-research-memory-structure-b.md",
  "memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-research-retrofit-a.md",
  "memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-research-retrofit-b.md",
  "memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-research-retrofit-instruments.md"
 ],
 "byDesign": "- The build is design-only: no product code and no unit specs; each chain build writes its own specs later, so unit-level implementation detail is absent by design.\n- The owner's settled answers, recorded in each record's [answers], are decisions: a finding may show that one contradicts another record, the platform or the tree, but does not re-argue the owner's choice.\n- Records outside memory/builds/dClosedLoop/ are not under review, and the research returns are evidence, not subjects.\n- The non-default preset values of the keys these rounds added were assigned by analogy, as v2's dated note says: a finding may show one inconsistent with its preset or with an owner's answer, not that it is unasked.\n- Records written before 2026-10-16 that say Knowledge mean memory's library side (layer-library [settled], \"Older records' wording\").\n- Generated files (memory/LIVE.md, the build README's generated regions, memory/map/generated/ and memory/gotchas/INDEX.md) are rendered and not under review.\n- The atlas page and its generator are an owner-facing view outside this review.",
 "checklist": "# recurring-bug-class checklist for 2 path(s) (2 file(s))\n# 10 class(es) selected by an anchor + 6 universal\n# by anchor specificity: 0 path · 6 directory · 4 basename; a cut tier prints one line per class\n# invariants are read from the working tree; with no --base, a record this subject adds or edits can stand as by design\n\n- [ ] fixture-passes-by-finding-nothing (universal)\n      a test arm whose fixture never triggers the rule passes, and proves nothing\n      memory/gotchas/fixture-passes-by-finding-nothing.md\n\n- [ ] guard-above-a-fold-makes-its-fallback-dead (universal)\n      a guard added above a fold settles the predicate the fold's own fallback re-tests, leaving a dead arm that reads as coverage\n      memory/gotchas/guard-above-a-fold-makes-its-fallback-dead.md\n\n- [ ] heredoc-escape-reaches-the-regex (universal)\n      source written through a shell heredoc into a non-raw string turns an escape into a control byte, and the symptom never looks like a quoting problem\n      memory/gotchas/heredoc-escape-reaches-the-regex.md\n\n- [ ] inline-fence-swallows-the-rest-of-the-file (universal)\n      a triple-backtick written inline in prose opens a fence the reader never closes, so every section after it silently disappears from the checker's view\n      memory/gotchas/inline-fence-swallows-the-rest-of-the-file.md\n\n- [ ] staged-break-substitutes-a-synthetic-value (universal)\n      an arm that proves a mechanism by replacing the shipped value with a simpler one proves the mechanism for the simpler value\n      memory/gotchas/staged-break-substitutes-a-synthetic-value.md\n\n- [ ] two-answers-to-one-question (universal)\n      a fact stated in two places drifts, and the copies need not disagree loudly to be wrong\n      memory/gotchas/two-answers-to-one-question.md\n\n- [ ] a-merge-of-the-default-branch-read-as-additions (directory)\n      a check that lists the files a range or a commit ADDS reads a merge of the default branch into a feature branch as adding every file the default branch gained, unless its git invocation is one of the shapes that cannot\n      memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md\n\n- [ ] amendment-leaves-its-other-half-standing (directory)\n      a criterion is amended and the clause, scope item or log line that only made sense under the old wording is left behind, so one rule now returns two verdicts\n      memory/gotchas/amendment-leaves-its-other-half-standing.md\n\n- [ ] insert-after-a-key-that-occurs-twice (directory)\n      a record edit inserts a row after the first match of a cell value that occurs in two tables, so the row lands in the wrong table and the right one never gains it\n      memory/gotchas/insert-after-a-key-that-occurs-twice.md\n\n- [ ] ledger-token-wrapped-across-a-line-joins-nothing (directory)\n      hygiene check 23 extracts a ledger line's backticked tokens PER LINE, so a token the writer wrapped across a line break belongs to no line and the criterion it answers reads as unanswered\n      memory/gotchas/ledger-token-wrapped-across-a-line-joins-nothing.md\n\n- [ ] pipe-in-a-code-span-splits-a-table-cell (directory)\n      a markdown table cell holding a pipe, even inside backticks, splits into extra cells, so a reader that splits the row on its pipes reads the wrong cell as a column\n      memory/gotchas/pipe-in-a-code-span-splits-a-table-cell.md\n\n- [ ] retirement-inventory-misses-readers-by-value (directory)\n      an inventory of what reads a retired thing, built by searching for its name, misses every assertion on a count or a value that thing carries, because those name nothing\n      memory/gotchas/retirement-inventory-misses-readers-by-value.md\n\n- [ ] owner-item-without-its-reject-outcome (basename)\n      a design hands a decision to the owner and routes only the yes, so a no leaves landed work with no route and a check that turns red on the default branch\n      memory/gotchas/owner-item-without-its-reject-outcome.md\n\n- [ ] policy-value-with-no-route (basename)\n      a policy key catalogues a value that no item reading the key routes or witnesses, so a preset that selects the value cannot run\n      memory/gotchas/policy-value-with-no-route.md\n\n- [ ] rate-quoted-without-its-denominator (basename)\n      a rate put to the owner in a fork divides by the wrong population, so the option's own cost reads several times off\n      memory/gotchas/rate-quoted-without-its-denominator.md\n\n- [ ] record-without-serves-or-with-a-round-counter (basename)\n      a new build record owes a Serves line and a filename that projects it, and a round counter in that filename mints an id nothing defines\n      memory/gotchas/record-without-serves-or-with-a-round-counter.md\n\n# by design — 0 invariant(s) this selection touches\n",
 "subjects": [
  {
   "path": "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md",
   "blob": "9335a353336ab035011412ed6d6b60c941de4b21"
  },
  {
   "path": "memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md",
   "blob": "cec90968d4159234e132fd1ba5f1a82232102d4f"
  }
 ],
 "scratch": "C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/review-systems-retrofit",
 "round": 1,
 "intensity": "full",
 "roles": {
  "specFinder": "gov-spec-reviewer",
  "skeptic": "gov-skeptic",
  "synthesis": "gov-synthesizer"
 },
 "efforts": {
  "skeptic": "medium",
  "specFinder": "medium",
  "synthesis": "medium"
 },
 "context": "The subjects are two design records of build dClosedLoop, a design-only build that re-architects gov onto one loop. memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md designs five systems that cross the layers: tags, code annotations, instruction writing, role workflow shapes and memory structure. memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md designs how gov retrofits its practices into a repository that already has a codebase and practices of its own, a sixth system across the layers. The owner asked for both (each record's [words]). Two researchers measured each system and the retrofit; their returns are among the specs. The owner answered every fork: AN-1, AN-2, IW-1, IW-2, RS-1, RS-2 and MS-1 to MS-3 in the systems record's [answers], and RF-1 to RF-6 in the retrofit record's. Their keys, gaps and chain units were folded into v2 and the gap register in 36fc6d572. No review has read either record. A statement in v2, the register or a layer record that contradicts these records, or that the fold carried wrongly, is a finding. Audit each record as an architecture spec, against six questions: (1) internal consistency: do its components, policies, build units, gaps and answers agree with each other; (2) consistency with the sibling records in specs: v2's principles, policy catalogue and chain, the gap register and the layers' records, the two subjects with each other included; (3) feasibility against the measured facts in the research returns, the records in specs and the tree: a mechanism the platform or the tree cannot support, or a claim the evidence does not bear out; (4) missing mechanisms: anything a system or the retrofit must provide to the flow, the roles, the layers or each other that the design omits; (5) claims that are unenforced or untestable as written; (6) extension points, such as a tag namespace, a role shape, a record kind's sections or a ledger population, that could not in fact be filled without changing code. Address each finding by the record's file and section tag, such as [agreement], [cross], [design-tags], [design-role-shapes], [answers] and [gaps-proposed] in the systems record, and [ledger], [seed], [drain], [owners], [keys] and [answers] in the retrofit record. Write the report to memory/builds/dClosedLoop/reviews/2026-10-17-review-PLAY-dClosedLoop-1-systems-retrofit.md. Its head carries an H1, then, within its first twelve lines, the line `**Serves:** spec-audit PLAY-dClosedLoop-1`. It carries exactly one `## Verdict:` line, whose token is CLEAN, CLEAN WITH FIXES or BLOCKED and nothing else."
}
```
