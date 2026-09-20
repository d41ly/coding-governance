# TOOL-aBlindedTrial-1 — spec-first versus build-first, measured on a blinded trial

**Status:** INPROGRESS · rev-2 · 2026-09-20 · node a · Tier-1 · base d46d3ccb · streams tooling+playbook · order 1 · ratified 2026-09-20

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Answer, with numbers derived by command, whether writing and adversarially auditing a spec before
code produces better code than building from the brief directly, and what that costs in tokens.
Two halves: a retrospective over this repo's own 610 specs, and a prospective trial in which the
same briefs are built under three regimes and graded blind.

## 2. Scope (IN)

- S1 — Retrospective ordering: for every spec under `memory/builds/*/spec/`, the order of first
  spec commit, first `spec-audit` record and first product commit naming the unit, by committer
  timestamp. Observed by AC1.
- S2 — Retrospective adherence read: twenty CLOSED Tier-2 spec-first units sampled deterministically,
  each graded by an agent for criterion concreteness, criterion satisfaction in the product diff,
  code the spec never mentions, and whether the audit's fold is visible in what was built. Observed
  by AC2.
- S3 — Three briefs for standalone Python stdlib tools shaped like this repo's work — a
  declared-population checker, a row-keyed three-way merge driver, a gate-ledger reporter with a
  liveness assertion — each with example fixtures and deliberate open points. Observed by AC3.
- S4 — A hidden acceptance suite per brief, authored and adversarially verified from the brief
  alone, every test tagged `stated`, `implied` or `ambiguous`, frozen by sha256 before any arm runs.
  Observed by AC3, AC4.
- S5 — Three arms, three replicates each, per brief, in isolated scratch cells: **B** builds from
  the brief; **P** writes an unreviewed plan of at most 40 lines then builds; **S** authors a full
  `TEMPLATE-SPEC.md` spec, has it audited by `tools/workflows/tier2-review.js` in its `spec-audit`
  kind, folds the confirmed findings to rev-2, and a separate agent builds from the spec. Observed
  by AC5, AC6.
- S6 — Grading: hidden-suite pass rate split by certainty tag; blind find→refute review per script
  with confirmed defects by severity; adherence judges over the S specs and P plans; non-blank lines
  of code; output tokens per arm attributed from the agent transcripts. Observed by AC7, AC8, AC9.
- S7 — One build record carrying the tables, the derivation of every figure, and the verdict.
  Observed by AC10.

## 3. Non-goals (OUT)

- No change to the template, `BUILD-METHOD.md`, the kickoff engine or any kit. A rule change is a
  follow-up unit.
- No fourth arm (spec without audit), no fourth task, no more than three replicates — unless §8's
  menu is ratified otherwise. Each is priced there.
- No grading of the trial's own build records by any of the trial's agents.
- No claim about tasks larger than one agent context: the trial's units are one-file tools, and the
  record says so.

### Edges

- **consumes-from** external — `tools/workflows/tier2-review.js` at its tracked version is the
  audit; a change to it mid-trial invalidates the S arm.
- **hands-off** external — any template or method change the verdict motivates.

## 4. Design

### Inventory

Everything the trial writes lives under `C:/Users/daily-agent/AppData/Local/Temp/xp/` (`XP`), the
sanctioned scratch root, and is not tracked. What lands in this tree is the build record.

| path under `XP` | what |
|---|---|
| `briefs/{A,B,C}.md` | the three briefs, verbatim in the build record |
| `fixtures/<T>/` | example inputs each cell receives |
| `hidden/<T>/test_<T>.py` + `AMBIGUITIES.md` | the frozen acceptance suite and its readings |
| `cells/<T>/<arm>/<rep>/` | one git repository per cell; brief, fixtures, the tool, S adds `spec/` and `reviews/` |
| `eval/<T>/<code>/` | blinded copies, code = first 6 hex of a salted sha1 of the cell path |
| `wf/*.js`, `wf/gen_wf.py`, `wf/harness.py` | the harnesses; the per-task scripts are generated so the three tasks cannot drift |
| `results/*.json` | every derived figure |

### Method

1. `retro.py` (scratchpad) walks `git log` once and classifies every spec: SPEC-FIRST, SAME-COMMIT,
   BUILD-FIRST or NO-PRODUCT; audit BEFORE-CODE, AFTER-CODE or NEVER. Attribution is by unit id in
   the product commit subject, falling back to the build slug and flagged.
2. `wf/retro-quali.js` fans five readers over the twenty-unit sample, four units each.
3. `wf/hidden.js`: per brief, an author writes the suite and a verifier re-tags, loosens, adds and
   re-runs it against an exit-0 stub, which every test must fail. `harness.py freeze-hidden` records
   the sha256; `run-hidden` refuses a suite whose hash moved.
4. `harness.py prep` builds the 27 cells. `wf/arms-<T>.js`, one Workflow call per task, runs B as a
   fan of three, then P as a fan of three, then the three S chains sequentially; each S chain is
   author → nested `tier2-review.js` (`kind: 'spec-audit'`, subject pinned by blob) → fold → build.
   Every prompt carries a `[cell:T/arm/rep:step]` tag for token attribution.
5. `harness.py blind` copies scripts under code names; `wf/eval-<T>.js` runs finder → skeptic per
   script (skeptic defaults to refuted) and adherence judges over the S specs and P plans.
6. `harness.py run-hidden`, `tokens <transcript dirs>`, `report` derive the tables.

### What discriminates

Arm P exists so the result can separate "thinking before coding" from "the ceremony": if P ≈ S on
quality, the spec format and the audit are the cost with no return; if S > P, the audit or the
separation of author from builder is doing work; if B ≈ P ≈ S, upfront design does not move
one-file tools and the record says exactly that.

### Alternatives rejected

- Grading in this tree, with the repo's gates: contaminates every arm with prior art and makes
  "reuse the existing checker" the winning move in all three.
- One agent grading its own output: the arm that wrote the spec would also grade adherence to it.
- Token cost from `budget.spent()` deltas: fans run concurrently, so the delta cannot be attributed;
  the transcripts carry per-agent usage and a prompt tag joins them to a cell.

## 5. Production-readiness checklist

- security — N/A, scratch cells, no network, no credentials
- perf / scale — the S arm is roughly eight agents per replicate against one for B; wall clock is
  bounded by running one task at a time
- error / empty / loading states — a dead agent returns null and the cell is recorded as missing,
  never as a zero
- observability — every agent result lands in `results/*.json`; the workflow journal is the audit
  trail
- risks — the hidden suite's author interprets the brief too; the certainty tags and the verifier
  bound that, and pass rates are reported per tag
- testing — the hidden suites are run against an exit-0 stub before freezing; a test the stub passes
  is deleted
- migration — N/A
- user docs — N/A, records-only

## 6. Acceptance criteria

- **AC1** — When `retro.py` runs over the tree, it prints the order and audit distributions for all
  specs and for CLOSED specs separately, split by attribution quality, and writes `retro.json`.
  Red when: a spec with a status header is missing from the count, or a figure appears in the record
  that the JSON does not carry.
- **AC2** — When `retro-quali.js` runs, every one of the twenty sampled units has a graded row in
  its return, or is named as ungraded with the batch that died.
  Red when: a batch dies and the record reports the survivors as the sample.
- **AC3** — When `harness.py freeze-hidden` runs, each of the three suites has a recorded sha256 and
  at least 25 tagged tests, and `run-hidden` refuses to run when a suite's bytes differ from the
  freeze.
  Red when: a suite under 25 tests is frozen, or a changed suite is graded.
- **AC4** — When each frozen suite is run with `SUT` pointing at a stub that exits 0 and prints
  nothing, every test fails.
  Red when: any test passes against the stub.
- **AC5** — When `arms-<T>.js` completes for a task, nine `[cell:T/arm/rep] build` commits exist
  across the nine cells, and every S cell holds a spec at rev-2 whose `reviews/` directory carries a
  `tier2-review.js` report.
  Red when: an S build ran against a spec that was never audited, or a cell is missing and reported
  as a pass.
- **AC6** — When an S build agent diverges from its spec, the spec carries a rev-3 §9 line and the
  agent's `deviationsFromSpec` count is non-zero; the record reports the count per cell.
  Red when: code and spec disagree and the §9 log does not say so.
- **AC7** — When `harness.py run-hidden` runs over the 27 cells, `hidden-results.json` carries pass
  counts per cell split by `stated`, `implied` and `ambiguous`.
  Red when: a cell with no script is reported as any number other than missing.
- **AC8** — When `eval-<T>.js` completes, every blinded script has a review row carrying raw,
  confirmed and refuted counts, and no reviewer prompt names an arm.
  Red when: a judge's prompt or working directory reveals the arm.
- **AC9** — When `harness.py tokens` runs over the workflow transcript directories, every agent is
  attributed to a `[cell:…]`, `[eval:…]`, `[adherence:…]`, `[hidden:…]` or `[retro-quali:…]` tag, and
  the untagged count is printed.
  Red when: a per-arm token figure is reported while the untagged count is not.
- **AC10** — When the build record is written, every figure in it names the `results/*.json` key or
  the command that derives it, and the verdict states the trial's own token cost beside the arms'.
  Red when: a number in the record has no derivation, or the trial's cost is omitted.

## 7. Gates

The records this unit adds must keep green the legs that grade this tree's own state; the set is
read from `tools/gate-legs.json` at emission time. The leg line:

`memory hygiene` · `build README slot contract` · `spec tokens (a spec's own names resolve)` · `pass-order history` · `brief-recorded`

## 8. Open questions

The scope menu, put to the owner 2026-09-20 and ratified at the recommended shape on every item.

- **F1 — replicates per cell.** Three (recommended; 27 builds, 9 audits) or five (45 builds, 15
  audits, roughly 1.7× the cost). Three cannot detect a small effect; it can detect a large one and
  it measures the cost ratio precisely either way. Recommendation: three, and re-run the surviving
  contrast at five only if the result is close. RESOLVED (owner, 2026-09-20): three.
- **F2 — a fourth arm, spec WITHOUT audit.** Isolates the audit's contribution from the spec's.
  Adds 9 builds and 9 spec authors. Recommendation: no — arm P already separates "thinking first"
  from "the ceremony", and if S beats P the follow-up trial is exactly this arm.
  RESOLVED (owner, 2026-09-20): no fourth arm.
- **F3 — task set.** The three briefs in `XP/briefs/` (recommended) or swap one for an in-repo task
  built inside a scratch clone of this tree with its gates. In-repo tasks measure a different thing
  — reuse of existing seams — and contaminate the arms with prior art. Recommendation: the three
  standalone briefs. RESOLVED (owner, 2026-09-20): the three standalone briefs.
- **F4 — grading weights.** Report the four measures separately (recommended) rather than a composite
  score; a composite hides which measure moved. RESOLVED (owner, 2026-09-20): separate measures.

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft; retrospective S1 already run while drafting (figures in
  `retro.json`), the rest awaits scope approval.
- rev-2 · 2026-09-20 · §8 · scope approved by the owner at the recommended shape on all four forks;
  status INPROGRESS. S2 and S4 completed before approval as preparation: twenty units graded, three
  suites frozen at 43/42/42 tests, each failing 100% against an exit-0 stub.

## 10. Reuse audit

Not required at Tier 1, recorded anyway. No existing seam fits for the trial itself: nothing in the
tree runs one brief under several regimes. The audit inside the S arm IS an existing seam and is
reused as shipped: `tools/workflows/tier2-review.js` in its `spec-audit` kind. The retrospective's
ordering predicate is the same one `tools/unattended/check-pass-order.sh` grades for builds opened
after `PASS_ORDER_CUTOFF`; it was re-derived in Python rather than extended because that leg reads
CLOSED units of one build under a conf, and this needs every spec of every build with attribution
flags. Recall terms used: spec audit pass-order build-first specs-reviewed hard floor unit built
adherence acceptance ledger token cost review harness.
