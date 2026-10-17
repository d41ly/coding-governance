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

## [probes-final] The closing review's probes, and their runs at `0e7c41abb`

Each runs from the worktree root. The folds' closing review (`reviews/2026-10-17-review-PLAY-dClosedLoop-1-debt-folds.md`)
asked for each.

### The table-shape probe (L2)

```python
"""Find markdown table rows that do not match their table's shape: a row indented differently from its
header, so the renderer ends the table there, or a row whose cell count differs from the header's, so a
pipe split it or a cell went missing.

Usage: python table_shape.py <file-or-dir> ...   (exit 1 on any finding)
A table opens on a header row followed by a separator row, each indented up to three spaces past the
enclosing list's indent, and runs until a line that is blank or not a pipe row. A row is any line in that
run that holds a pipe once its indent is stripped. Cells are counted on unescaped pipes outside nothing:
a pipe inside backticks still splits a cell, as the renderer splits it. Fenced code blocks are skipped.
Prints each finding, then the tables and rows read, so a zero is a zero over a named population.
"""
import pathlib
import re
import sys

SEP = re.compile(r"^\|?(\s*:?-+:?\s*\|)+(\s*:?-+:?\s*)?$")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")


def cells(row):
    body = row.strip()
    if body.startswith("|"):
        body = body[1:]
    if body.endswith("|") and not body.endswith("\\|"):
        body = body[:-1]
    return len(re.split(r"(?<!\\)\|", body))


def scan(path):
    lines = path.read_text(encoding="utf-8").split("\n")
    findings, tables, rows = [], 0, 0
    fenced = False
    n = 0
    while n < len(lines):
        line = lines[n]
        if FENCE.match(line):
            fenced = not fenced
            n += 1
            continue
        if fenced:
            n += 1
            continue
        nxt = lines[n + 1] if n + 1 < len(lines) else ""
        if "|" in line and SEP.match(nxt.strip()):
            tables += 1
            indent = len(line) - len(line.lstrip(" "))
            width = cells(line)
            m = n + 2
            while m < len(lines):
                row = lines[m]
                if not row.strip() or "|" not in row or FENCE.match(row):
                    break
                rows += 1
                ind = len(row) - len(row.lstrip(" "))
                if ind != indent:
                    findings.append(f"{path}:{m + 1}: indented {ind}, its table's header {indent}: {row.strip()[:60]}")
                elif cells(row) != width:
                    findings.append(f"{path}:{m + 1}: {cells(row)} cells, its header {width}: {row.strip()[:60]}")
                m += 1
            n = m
            continue
        n += 1
    return findings, tables, rows


paths = []
for arg in sys.argv[1:]:
    p = pathlib.Path(arg)
    paths += sorted(p.rglob("*.md")) if p.is_dir() else [p]
all_f, t_all, r_all = [], 0, 0
for p in paths:
    f, t, r = scan(p)
    all_f += f
    t_all += t
    r_all += r
print("\n".join(all_f))
print(f"files {len(paths)}; tables {t_all}; rows {r_all}; findings {len(all_f)}")
sys.exit(1 if all_f else 0)
```

Over the build's records and the bug classes, before the fold:

```text
$ python table_shape.py memory/builds/dClosedLoop/build memory/gotchas
memory\builds\dClosedLoop\build\2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:331: indented 0, its table's header 2: | `blocked` | each blocked item, with what blocks it | raise
memory\builds\dClosedLoop\build\2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:581: indented 0, its table's header 2: | the dispatcher's permission entry, new | PermissionRequest
memory\builds\dClosedLoop\build\2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-hooks.md:41: 7 cells, its header 5: | `commit-msg` | Merge transition audit, plus unattended `--
files 235; tables 545; rows 5724; findings 3
```

After it, the one row left is a verbatim research return's, which a filed return keeps as it came:

```text
$ python table_shape.py memory/builds/dClosedLoop/build memory/gotchas
memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-hooks.md:41: 7 cells, its header 5: | `commit-msg` | Merge transition audit, plus unattended `--
files 235; tables 545; rows 5724; findings 1
```

### The target-spawn probe, revised (M7, M10)

```python
"""List every place govkit's update can run code the target repository authored, and fail when the design
does not name each one.

Usage: python target_spawns.py tools/govkit/govkit.py <named.json> [entry]   (entry defaults to _cmd_update)
<named.json> maps each function the design names to the number of its target-side sites, for example
{"run_kit_check": 1, "_cmd_update": 2}. Exit 1 when a reached function holds sites the list does not name,
or a different count, or when a named function no longer holds a reached site.

Two populations, each printed with its count:
- spawns: a subprocess call (`run`, `Popen`, `check_output`, `call`) whose `cwd=` names the target or the
  root. Its program is the target's own code, or runs in the target's tree;
- git in the target: a subprocess call whose argv opens `git -C <target>`. Git itself is not the target's
  code, but git runs the target's hooks: `hook run` names one, an index write fires post-index-change, a
  ref update fires reference-transaction, a checkout fires post-checkout, and a commit fires pre-commit,
  prepare-commit-msg, commit-msg and post-commit. Each such call is a site, named by its function, unless
  it reads only (`version`, `rev-parse`, `ls-files`, `cat-file`, `check-attr`, `hash-object`, `show`,
  `ls-tree`, `merge-base`, `for-each-ref`, `diff`, `status`, `log`).
The call graph is by name, and a guard on the path is not evaluated: reached means reachable on some path.
Spawn calls that match neither population are counted, so the narrowing is visible.
"""
import ast
import collections
import json
import sys

path, named_path = sys.argv[1], sys.argv[2]
entry = sys.argv[3] if len(sys.argv) > 3 else "_cmd_update"
NAMED = json.load(open(named_path, encoding="utf-8"))
tree = ast.parse(open(path, encoding="utf-8").read())
READ_ONLY = {"version", "rev-parse", "ls-files", "cat-file", "check-attr", "hash-object", "show", "ls-tree",
             "merge-base", "for-each-ref", "diff", "status", "log", "ls-remote", "config"}
# A helper whose verb arrives as an argument: `_names(*args)` in dirty_claimed_paths, whose callers pass
# only `ls-files`, `ls-tree` and `diff` (govkit.py, the four calls after its definition).
READ_ONLY_HELPERS = {"_names"}

defs = {}


def walk(node):
    for child in ast.iter_child_nodes(node):
        if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
            defs.setdefault(child.name, []).append(child)
        walk(child)


walk(tree)
calls = collections.defaultdict(set)
for name, nodes in defs.items():
    for fn in nodes:
        for sub in ast.walk(fn):
            if isinstance(sub, ast.Call):
                f = sub.func
                callee = f.id if isinstance(f, ast.Name) else f.attr if isinstance(f, ast.Attribute) else None
                if callee in defs:
                    calls[name].add(callee)
seen, stack = set(), [entry]
while stack:
    n = stack.pop()
    if n not in seen:
        seen.add(n)
        stack.extend(calls.get(n, ()))


def enclosing(lineno):
    best = None
    for name, nodes in defs.items():
        for fn in nodes:
            if fn.lineno <= lineno <= (fn.end_lineno or fn.lineno) and (best is None or fn.lineno > best[1]):
                best = (name, fn.lineno)
    return best[0] if best else "<module>"


def git_verb(call):
    """The git subcommand of a call whose first argument is a list literal opening `git -C <target>`."""
    if not call.args or not isinstance(call.args[0], (ast.List, ast.BinOp)):
        return None
    lst = call.args[0].left if isinstance(call.args[0], ast.BinOp) else call.args[0]
    if not isinstance(lst, ast.List) or len(lst.elts) < 3:
        return None
    src = [ast.unparse(e) for e in lst.elts]
    if src[0] != "'git'" or src[1] != "'-C'" or "target" not in src[2]:
        return None
    rest = [e.value for e in lst.elts[3:] if isinstance(e, ast.Constant) and isinstance(e.value, str)]
    verb = next((a for a in rest if not a.startswith("-")), "?")
    if verb == "?" and isinstance(call.args[0], ast.BinOp):
        verb = "<argv>"
    return verb


spawns, gits, other = [], [], 0
for node in ast.walk(tree):
    if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
            and node.func.attr in ("run", "Popen", "check_output", "call")):
        continue
    fn = enclosing(node.lineno)
    cwd = next((ast.unparse(k.value) for k in node.keywords if k.arg == "cwd"), None)
    verb = git_verb(node)
    if cwd and ("target" in cwd or cwd in ("str(root)", "root")):
        spawns.append((node.lineno, fn, f"cwd={cwd}"))
    elif verb is not None:
        gits.append((node.lineno, fn, verb))
    else:
        other += 1

sites = collections.Counter()
print(f"entry: {entry}; functions it reaches: {len(seen)}")
print("spawns with the target as cwd:")
for ln, fn, what in sorted(spawns):
    r = fn in seen
    print(f"{ln:>6}  {'REACHED' if r else 'not    '}  {fn}  {what}")
    if r:
        sites[fn] += 1
print("git in the target:")
for ln, fn, verb in sorted(gits):
    r = fn in seen
    hooks = verb not in READ_ONLY and fn not in READ_ONLY_HELPERS
    print(f"{ln:>6}  {'REACHED' if r else 'not    '}  {fn}  git {verb}{'  runs hooks' if hooks else ''}")
    if r and hooks:
        sites[fn] += 1
print(f"spawn calls in neither population: {other}")
findings = []
for fn, n in sorted(sites.items()):
    if fn not in NAMED:
        findings.append(f"{fn}: {n} reached target-side site(s) the design does not name")
    elif NAMED[fn] != n:
        findings.append(f"{fn}: the design names {NAMED[fn]} site(s), and {n} are reached")
for fn in sorted(set(NAMED) - set(sites)):
    findings.append(f"{fn}: the design names it, and no reached site holds it")
print(f"reached sites: {sum(sites.values())} in {len(sites)} functions; named: {sum(NAMED.values())} in {len(NAMED)}")
for f in findings:
    print("FINDING", f)
sys.exit(1 if findings else 0)
```

The design's list after the fold, `named-design.json`:

```json
{"_cmd_update": 15, "run_kit_check": 1, "measure_contract_parity": 1, "run_hole_probes": 1, "run_fragment_merges": 4, "remove_wired_fragments": 1, "decline_findings": 1, "land_through_index": 2, "write_gate_legs": 1}
```

Against the six kinds the records named before the fold (`named-six.json`, the same list less the git
writes), it fails:

```text
$ python target_spawns.py tools/govkit/govkit.py named-six.json
entry: _cmd_update; functions it reaches: 134
spawns with the target as cwd:
  4757  REACHED  decline_findings  cwd=str(target)
  5012  REACHED  run_hole_probes  cwd=str(target)
  5051  REACHED  run_kit_check  cwd=str(target)
  5888  REACHED  run_fragment_merges  cwd=str(target)
  5897  REACHED  run_fragment_merges  cwd=str(target)
  5909  REACHED  run_fragment_merges  cwd=str(target)
  5912  REACHED  run_fragment_merges  cwd=str(target)
  5933  REACHED  remove_wired_fragments  cwd=str(target)
  5958  not      read_gate_verdicts  cwd=str(target)
  6065  REACHED  measure_contract_parity  cwd=str(target)
  6189  not      exempt_leg  cwd=str(target)
  7744  not      _cmd_apply  cwd=str(target)
 10986  REACHED  _cmd_update  cwd=str(target)
 11119  REACHED  _cmd_update  cwd=str(target)
 13198  not      cmd_mint  cwd=str(root)
git in the target:
  4294  REACHED  write_gate_legs  git add  runs hooks
  5237  not      cmd_check  git hash-object
  5615  REACHED  eol_population  git ls-files
  5620  REACHED  eol_population  git check-attr
  6206  not      hook_probe  git version
  6210  not      hook_probe  git rev-parse
  6215  not      hook_probe  git hook  runs hooks
  6572  REACHED  index_read  git ls-files
  6622  REACHED  index_blob  git cat-file
  6771  REACHED  git_path  git rev-parse
  6800  REACHED  demand_index_resolved  git ls-files
  6886  REACHED  _names  git ?
  6906  REACHED  dirty_claimed_paths  git rev-parse
  7422  not      _cmd_apply  git add  runs hooks
  7847  not      _cmd_apply  git diff
  7871  not      _cmd_apply  git ls-files
  8609  REACHED  land_through_index  git hash-object
  8617  REACHED  land_through_index  git update-index  runs hooks
  8622  REACHED  land_through_index  git checkout-index  runs hooks
  8658  REACHED  read_worktree_status  git status
  8730  REACHED  measure_rendered_rows  git hash-object
  8893  REACHED  _cmd_update  git add  runs hooks
  9914  REACHED  _cmd_update  git rm  runs hooks
 10048  REACHED  _cmd_update  git add  runs hooks
 10090  REACHED  _cmd_update  git add  runs hooks
 10158  REACHED  _cmd_update  git update-index  runs hooks
 10320  REACHED  _cmd_update  git mv  runs hooks
 10774  REACHED  _cmd_update  git ls-files
 11361  REACHED  _cmd_update  git rm  runs hooks
 11376  REACHED  _cmd_update  git update-index  runs hooks
 11386  REACHED  _cmd_update  git checkout-index  runs hooks
 11517  REACHED  _cmd_update  git rm  runs hooks
 11520  REACHED  _cmd_update  git update-index  runs hooks
 11712  REACHED  _cmd_update  git rm  runs hooks
 11719  REACHED  _cmd_update  git rm  runs hooks
 11767  REACHED  _cmd_update  git diff
 12205  not      demand_adopt_index_clean  git rev-parse
 12209  not      demand_adopt_index_clean  git diff
 12213  not      demand_adopt_index_clean  git diff
 12701  not      _cmd_adopt  git add  runs hooks
spawn calls in neither population: 30
reached sites: 27 in 9 functions; named: 11 in 7
FINDING _cmd_update: the design names 2 site(s), and 15 are reached
FINDING land_through_index: 2 reached target-side site(s) the design does not name
FINDING write_gate_legs: 1 reached target-side site(s) the design does not name
exit 1
```

Against the design's list, it passes:

```text
$ python target_spawns.py tools/govkit/govkit.py named-design.json
entry: _cmd_update; functions it reaches: 134
spawns with the target as cwd:
  4757  REACHED  decline_findings  cwd=str(target)
  5012  REACHED  run_hole_probes  cwd=str(target)
  5051  REACHED  run_kit_check  cwd=str(target)
  5888  REACHED  run_fragment_merges  cwd=str(target)
  5897  REACHED  run_fragment_merges  cwd=str(target)
  5909  REACHED  run_fragment_merges  cwd=str(target)
  5912  REACHED  run_fragment_merges  cwd=str(target)
  5933  REACHED  remove_wired_fragments  cwd=str(target)
  5958  not      read_gate_verdicts  cwd=str(target)
  6065  REACHED  measure_contract_parity  cwd=str(target)
  6189  not      exempt_leg  cwd=str(target)
  7744  not      _cmd_apply  cwd=str(target)
 10986  REACHED  _cmd_update  cwd=str(target)
 11119  REACHED  _cmd_update  cwd=str(target)
 13198  not      cmd_mint  cwd=str(root)
git in the target:
  4294  REACHED  write_gate_legs  git add  runs hooks
  5237  not      cmd_check  git hash-object
  5615  REACHED  eol_population  git ls-files
  5620  REACHED  eol_population  git check-attr
  6206  not      hook_probe  git version
  6210  not      hook_probe  git rev-parse
  6215  not      hook_probe  git hook  runs hooks
  6572  REACHED  index_read  git ls-files
  6622  REACHED  index_blob  git cat-file
  6771  REACHED  git_path  git rev-parse
  6800  REACHED  demand_index_resolved  git ls-files
  6886  REACHED  _names  git ?
  6906  REACHED  dirty_claimed_paths  git rev-parse
  7422  not      _cmd_apply  git add  runs hooks
  7847  not      _cmd_apply  git diff
  7871  not      _cmd_apply  git ls-files
  8609  REACHED  land_through_index  git hash-object
  8617  REACHED  land_through_index  git update-index  runs hooks
  8622  REACHED  land_through_index  git checkout-index  runs hooks
  8658  REACHED  read_worktree_status  git status
  8730  REACHED  measure_rendered_rows  git hash-object
  8893  REACHED  _cmd_update  git add  runs hooks
  9914  REACHED  _cmd_update  git rm  runs hooks
 10048  REACHED  _cmd_update  git add  runs hooks
 10090  REACHED  _cmd_update  git add  runs hooks
 10158  REACHED  _cmd_update  git update-index  runs hooks
 10320  REACHED  _cmd_update  git mv  runs hooks
 10774  REACHED  _cmd_update  git ls-files
 11361  REACHED  _cmd_update  git rm  runs hooks
 11376  REACHED  _cmd_update  git update-index  runs hooks
 11386  REACHED  _cmd_update  git checkout-index  runs hooks
 11517  REACHED  _cmd_update  git rm  runs hooks
 11520  REACHED  _cmd_update  git update-index  runs hooks
 11712  REACHED  _cmd_update  git rm  runs hooks
 11719  REACHED  _cmd_update  git rm  runs hooks
 11767  REACHED  _cmd_update  git diff
 12205  not      demand_adopt_index_clean  git rev-parse
 12209  not      demand_adopt_index_clean  git diff
 12213  not      demand_adopt_index_clean  git diff
 12701  not      _cmd_adopt  git add  runs hooks
spawn calls in neither population: 30
reached sites: 27 in 9 functions; named: 27 in 9
exit 0
```

With `measure_contract_parity` struck from that list, its site listing as above, it fails on the one name:

```text
$ python target_spawns.py tools/govkit/govkit.py named-planted.json
reached sites: 27 in 9 functions; named: 26 in 8
FINDING measure_contract_parity: 1 reached target-side site(s) the design does not name
exit 1
```

### The both-runs probe, revised again (M9)

```python
"""The probe one-run-claim-recorded-as-agreed prescribes, run over a design record's [agreement] and [cross].

Usage: python both_runs_probe.py <record.md>

A row credits a research run in one of two forms, and each credited run must be cited by a line of its
own return, `research-<layer>-<a|b>.md:<line>`, unless the crediting cell itself says "re-measured
here" (a phrase in another cell re-measures that cell's claim, not the credit):
- in [agreement], a table under `### [agree-<layer>]` whose "Both runs" cell is not empty or a dash
  credits both runs of that layer;
- in [cross], the "Found by" cell credits each run it names: "<layer> A and B" names both, and
  "<layer> A" or "<layer> B" names one. A row naming two or more runs must cite each.

Every table body row under the two sections is read. A row the probe cannot place, an [agreement] table
outside a known layer's subsection, or a [cross] row whose "Found by" names no run, is a finding, so a
predicate that matches nothing cannot pass silently. The probe prints how many rows it read and how many
its predicate matched. Exit 1 on any finding.

The revision of 2026-10-17, after the folds' closing review, reads each table by the renderer's grammar:
a header row and its separator open it, either indented up to three spaces and with its edge pipes
optional, and it runs to the first blank line or block start. An indented or pipe-less body row is read
and checked like any other, where the version before it skipped any line not opening with a pipe.

The revision of 2026-10-17 (the debt round) reads the exemption from the crediting cell, where the
version before it exempted a row whose phrase sat in any cell, and counted it as checked. Exempt rows
print apart from checked ones.

The revision of 2026-10-16 replaced a first version whose only predicate was the "<layer> A and B"
spelling, which no [agreement] row uses (the follow-up round's H1).
"""
import re
import sys

LAYERS = ("observability", "integrations", "distribution")
SEP = re.compile(r"^\|?(\s*:?-+:?\s*\|)+(\s*:?-+:?\s*)?$")
INDENT = re.compile(r"^ {1,3}")
BLOCK = re.compile(r"^ {0,3}(#|`{3}|~{3}|>|[-*+] |\d+[.)] )")
text = open(sys.argv[1], encoding="utf-8").read()
findings, read, matched, exempt = [], 0, 0, 0


def cells(ln):
    return [c.strip() for c in ln.strip().strip("|").split(" | ")]


def check(tag, ln, runs, cell):
    global matched, exempt
    if "re-measured here" in cell:
        exempt += 1
        return
    matched += 1
    missing = [f"{layer} {run.upper()}" for layer, run in sorted(runs)
               if not re.search(rf"research-{layer}-{run}\.md:\d+", ln)]
    if missing:
        findings.append(f"[{tag}] {cells(ln)[0][:60]}: credits {', '.join(sorted(f'{l} {r.upper()}' for l, r in runs))}; "
                        f"no line cited for {', '.join(missing)}")


for tag in ("agreement", "cross"):
    head = f"\n## [{tag}]"
    if head not in text:
        sys.exit(f"no section {head.strip()}")
    block = text.split(head, 1)[1].split("\n## ", 1)[0]
    layer, header, in_table = None, None, False
    lines = block.split("\n")
    for n, ln in enumerate(lines):
        m = re.match(r"^### \[agree-([a-z]+)\]", ln)
        if m:
            layer, header, in_table = m.group(1), None, False
            continue
        flat = INDENT.sub("", ln)
        if not in_table:
            nxt = INDENT.sub("", lines[n + 1]) if n + 1 < len(lines) else ""
            if "|" in flat and SEP.match(nxt.strip()):
                in_table, header = True, cells(flat)
            continue
        if not ln.strip() or BLOCK.match(ln):
            in_table = False
            continue
        if SEP.match(flat.strip()):
            continue
        read += 1
        ln = flat
        row = cells(ln)
        if tag == "agreement":
            if layer not in LAYERS or "Both runs" not in header:
                findings.append(f"[agreement] a row the probe cannot place: {ln[:80]}")
                continue
            both = row[header.index("Both runs")]
            if both not in ("", "—", "-"):
                check(tag, ln, {(layer, "a"), (layer, "b")}, both)
        else:
            if "Found by" not in header:
                findings.append(f"[cross] a row the probe cannot place: {ln[:80]}")
                continue
            found = row[header.index("Found by")]
            runs = set()
            for lay, a, b in re.findall(r"\b(" + "|".join(LAYERS) + r") (A)(?: and (B))?\b", found):
                runs.add((lay, "a"))
                if b:
                    runs.add((lay, "b"))
            for lay in re.findall(r"\b(" + "|".join(LAYERS) + r") B\b", found):
                runs.add((lay, "b"))
            if not runs:
                findings.append(f"[cross] a row whose Found by names no run: {ln[:80]}")
            elif len(runs) >= 2:
                check(tag, ln, runs, found)
    header = None

print(f"rows read: {read}; rows the predicate matched and checked: {matched}; exempt, their crediting cell re-measured: {exempt}")
for f in findings:
    print(f)
print(f"findings: {len(findings)}")
sys.exit(1 if findings else 0)
```

Its systems variant changes two lines, as `build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`
`[instrument-agreement]` says. Over the records at `0e7c41abb`, both pass: layer-expansions reads 52 rows, 44
checked, and the systems record 51 rows, 48 checked, each with no finding. On planted copies of
layer-expansions, the version before this one misses both rows, and this one catches each:

```text
$ planted: the first [agree-observability] row, its citations struck and indented one space; the probe before its revision
rows read: 51; rows the predicate matched and checked: 43; exempt, their crediting cell re-measured: 0
findings: 0
exit 0

$ planted: the first [agree-observability] row, its citations struck and indented one space; the probe after its revision
rows read: 52; rows the predicate matched and checked: 44; exempt, their crediting cell re-measured: 0
[agreement] The line: credits observability A, observability B; no line cited for observability A, observability B
findings: 1
exit 1

$ planted: the same row, its citations struck and its leading pipe dropped; the probe before its revision
rows read: 51; rows the predicate matched and checked: 43; exempt, their crediting cell re-measured: 0
findings: 0
exit 0

$ planted: the same row, its citations struck and its leading pipe dropped; the probe after its revision
rows read: 52; rows the predicate matched and checked: 44; exempt, their crediting cell re-measured: 0
[agreement] The line: credits observability A, observability B; no line cited for observability A, observability B
findings: 1
exit 1
```

### The reuse-token probe, gated as hygiene gates it (L3)

```python
"""Size gap-design-05's one-token migration: the specs whose reuse audit records a new seam, under each
predicate that reads it today.

Usage: python reuse_token_count.py <rev>   (from the worktree root)
Population: tracked memory/builds/*/spec/*.md at <rev>. Every match is case-insensitive.
- the trigger: the exact phrase "no existing seam fits", which `reuse.propose: new-seam` reads;
- one of two: that phrase or "no seam fits";
- section 10, any date: the substrings "no existing seam" or "no seam fits", or "reuse-first", inside
  the spec's `## 10. Reuse audit` section before its "recall terms" or `--terms`; and, beside it, the
  same substrings over the whole file;
- hygiene, as it reads: section 10's tokens, in a spec whose file name's first date is on or after
  `.memory-tree.conf`'s `SPEC10_EVIDENCE_CUTOFF` at <rev>, the only specs check-memory-hygiene.sh grades
  there (revised 2026-10-17, after the folds' closing review: the first version left the cutoff out);
- the unions of the trigger with each section-10 reading.
"""
import collections
import re
import subprocess
import sys

rev = sys.argv[1]


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, encoding="utf-8", check=True).stdout


conf = git("show", f"{rev}:.memory-tree.conf")
cut = re.search(r'^SPEC10_EVIDENCE_CUTOFF="([0-9-]+)"', conf, re.M)
if not cut:
    sys.exit("no SPEC10_EVIDENCE_CUTOFF in .memory-tree.conf at " + rev)
CUT = cut.group(1)
specs = [p for p in git("ls-tree", "-r", "--name-only", rev, "memory/builds/").splitlines()
         if re.match(r"^memory/builds/[^/]+/spec/[^/]+\.md$", p)]


def section10(text):
    out, inside = [], False
    for line in text.split("\n"):
        if line.startswith("## "):
            inside = bool(re.match(r"^## 10\. Reuse audit", line))
            continue
        if inside:
            out.append(line.lower())
    s = " " + " ".join(out)
    cuts = [i for i in (s.find("recall terms"), s.find("--terms")) if i >= 0]
    return s[:min(cuts)] if cuts else s


pops = collections.defaultdict(set)
for p in specs:
    t = git("show", f"{rev}:{p}")
    low, s10 = t.lower(), section10(t)
    if "no existing seam fits" in low:
        pops["the trigger: \"no existing seam fits\""].add(p)
    if "no existing seam fits" in low or "no seam fits" in low:
        pops["one of two: that phrase or \"no seam fits\""].add(p)
    if "no existing seam" in low or "no seam fits" in low:
        pops["whole file: \"no existing seam\" or \"no seam fits\""].add(p)
    if any(k in s10 for k in ("no existing seam", "no seam fits", "reuse-first")):
        pops["section 10, any date: those or \"reuse-first\""].add(p)
        d = re.search(r"\d{4}-\d{2}-\d{2}", p.rsplit("/", 1)[-1])
        if d and d.group(0) >= CUT:
            pops[f"hygiene, as it reads: those, in specs dated {CUT} or later"].add(p)
TRIG = pops["the trigger: \"no existing seam fits\""]
pops["the union of the trigger and section 10, any date"] = TRIG | pops["section 10, any date: those or \"reuse-first\""]
pops["the union of the trigger and hygiene's reading"] = TRIG | pops[f"hygiene, as it reads: those, in specs dated {CUT} or later"]
print(f"specs read: {len(specs)} in {len({p.split('/')[2] for p in specs})} builds")
for label, pop in pops.items():
    print(f"{label}: {len(pop)} specs in {len({p.split('/')[2] for p in pop})} builds")
```

```text
$ python reuse_token_count.py HEAD
specs read: 1301 in 163 builds
one of two: that phrase or "no seam fits": 251 specs in 67 builds
whole file: "no existing seam" or "no seam fits": 323 specs in 77 builds
section 10, any date: those or "reuse-first": 333 specs in 75 builds
hygiene, as it reads: those, in specs dated 2026-09-01 or later: 302 specs in 55 builds
the trigger: "no existing seam fits": 236 specs in 60 builds
the union of the trigger and section 10, any date: 339 specs in 76 builds
the union of the trigger and hygiene's reading: 323 specs in 66 builds
```

### The chain's two joins

After the fold, the gap-ownership join and the preset check, run as extracted from the session log, exit 0:
219 gap keys over 15 builds, none unowned, and 185 catalogue keys, 175 presettable, 175 preset rows.
