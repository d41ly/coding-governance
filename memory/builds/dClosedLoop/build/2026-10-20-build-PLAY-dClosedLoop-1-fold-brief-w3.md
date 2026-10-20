# Fold brief: writer 3

**Serves:** research PLAY-dClosedLoop-1

**Your task is to fold the whole-design audit's findings at the 33 places below into dClosedLoop's design
records, as one fold script.** This brief is your instructions, not a spec to review.

## What you fold, and against what

- **The subject is the working tree's design records** under `memory/builds/dClosedLoop/build/`, at commit `8222099f8a619eef461fe91e84bd9f74173be730`.
  The findings were made on a sealed copy into which twelve past defects were planted. The copy is not your subject;
  read nothing in it. The plants are listed in the round record's `[recall-scored]`
  (`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`). A finding that describes a plant points at a defect
  the working tree never had.
- **Your records:** architecture-v2's `[chain]` rows of every other build, and v2's sections outside `[chain]`. Edit nothing else. When a place needs an edit in another record, list it under
  *Requests* in your return, with the exact change, and leave it out of your script.
- **Read freely** in the working tree: every design record, the gap register, the design map, `tools/`, `skills/` and
  `.githooks/`. Write only in your scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fold/w3/`. Nothing goes into the repository.

## How you fold

1. **For each place,** read its findings below, then read the place in the working tree. Give it exactly one
   disposition:
   - `fold`: the defect is in the working tree, and the fix follows from what the design already settles. Write it.
   - `fork`: the fix chooses between real options, or changes what the design means. Write no fold. Name the
     question, the options and your recommendation, for the owner.
   - `plant`: the finding describes one of the twelve plants, absent from the working tree. Cite the plant.
   - `not a defect`: the working tree already answers it. Quote where.
   - `duplicate`: another place carries the same defect. Name it, and fold it there.
2. **Write the folds as one Python script,** `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fold/w3/fold-3.py`, using the build's fold library:

```python
import pathlib, sys
sys.path.insert(0, "C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/expansions")
from fold_lib import Record
R = Record("memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md")
R.sub("<exact old text, matching once>", "<new text>", "<place # and finding ids>")
R.insert_before("<exact anchor text, matching once>", "<text>", "<place # and finding ids>")
R.save()
```

   `sub` refuses unless its old text matches exactly once, so quote enough to be unique. Keep each record's own
   conventions: a clause keeps its `cl-dClosedLoop-NNNN` id and its build row, a new clause takes the next free id after
   the highest in `[clause-ids]` (never a renumber), and a record that logs revisions gets a line saying "Revised
   2026-10-20 by the whole-design audit's fold" with the finding ids. Write prose in the records' own register: short
   declarative sentences, no new terms where a defined one exists.
3. **Fold the smallest change that closes each defect,** as its finding's *Fix* and its skeptic's reading say. Where
   the skeptic narrowed a finding, fold the narrowed one.

## What you return

Your final message, nothing else:
1. **Dispositions,** one row per place: `| # | place | disposition | findings | evidence or the fold's one-line gist |`.
2. **Fold script:** its path, and how many edits it makes in which records.
3. **Forks,** each: `### FK-3-<k> — <question>`, then the options, your recommendation and the findings it rests on.
4. **Requests,** each naming the record, the exact change and the place it serves, or `none`.
5. **Read outside the list above:** `none`, or what and why.

Write nothing to the repository. Your effort is the one your role definition sets.

## The places

### Place 2: architecture-v2 · P23 · worst high · critical

#### A1-F3 — `cl-dClosedLoop-0093`, P23's only enforcer, is carried by no clause
- **Address:** architecture-v2 [enforcement] `P23`; architecture-v2 [chain] dDeclaredLoop row
- **Class:** K5, c5
- **Severity:** high
- **Scenario:** S1 (A2-F1: S2; A3-F17: S5; A5-F10: S6)
- **What is wrong:** [enforcement] reads "| `P23` | `cl-dClosedLoop-0093` |", and that row (v2:1707) is the id's only occurrence in the copy. A parse of [chain] finds 495 clauses with 0093 the only gap: dDeclaredLoop's row runs from `cl-dClosedLoop-0092` to `cl-dClosedLoop-0094`, and [clause-ids] says "Retired: none".
- **Consequence:** P23 ("Claims are trusted by key and source") has no clause, so no chain spec can carry it, and the carries join reds a ghost id at dDeclaredLoop's Design exit. Claims pulled from another node or harness are acted on with no recompute: S2's witnesses, cards and interface keys, S5's replayed claim and `entry.claim`'s own-key retry.
- **Fix:** Restore dDeclaredLoop's clause `cl-dClosedLoop-0093`: claims trusted by recomputed key and source, refusing a source an agent typed and re-deriving otherwise, seen red on a planted stale key. Otherwise list 0093 as retired and name P23's real enforcing clause in its row. Confirm that Stage 0's K5 arm reds the ghost id.
- **Skeptic:** Confirmed high, c5 (batch 1). Its own parse found 495 ids with only 0093 missing, and only `cl-dClosedLoop-0164` recomputes a key, for interface messages alone.
- **Same as:** A2-F1, A3-F17, A5-F10

#### A3-F17 — `cl-dClosedLoop-0093` is carried by no clause, so P23's only enforcer is a ghost id
- **Address:** architecture-v2 [enforcement] `P23`; architecture-v2 [chain] dDeclaredLoop
- **Same as:** A1-F3
- **Skeptic:** Confirmed high, c5 (batch 1), as the same defect at architecture-v2 [enforcement] `P23`.

#### A5-F10 — P23's only enforcing clause id is a ghost
- **Address:** architecture-v2 [enforcement] `P23`
- **Same as:** A1-F3
- **Skeptic:** Confirmed high, c5 (batch 1), as the same defect, observed the same way.

### Place 14: architecture-v2 · cl-dClosedLoop-0435 · worst high · critical

#### A4-F6 — No clause makes the receipt name its release and remote, or cuts a release
- **Address:** architecture-v2 [chain] dShippedRelease row (`cl-dClosedLoop-0435`); layer-expansions [design-distribution]
- **Class:** K6
- **Severity:** medium (the walker graded it high, c2)
- **Scenario:** S4
- **What is wrong:** layer-expansions:438 defines receipt schema 4 as "per-kit versions, the release tag, the source remote". `cl-dClosedLoop-0020` defines schema 4 as gaining `steps`, and `cl-dClosedLoop-0435` defines schema 5 without those fields. No clause builds the release tag or the source remote, and `govkit.py:8020` still writes `"gov_source": str(root)`. `kits.cut` has an item row (layer-expansions:453) but no clause builds it.
- **Consequence:** "Two releases behind" cannot be computed, so `kits.currency` and `install.from: release-tag` read a field nothing builds. Two schema-4 definitions collide. Currency fails, and it blocks landings only under strict's `currency.on-behind: red`.
- **Fix:** Add dShippedRelease clauses for `kits.cut` (the annotated `gov/v<date>.<n>` tag) and for a receipt schema step that adds the release tag and source remote and drops the local path. Restate distribution's receipt schema to match `cl-dClosedLoop-0020` and `cl-dClosedLoop-0435`.
- **Skeptic:** Confirmed medium (batch 1), graded down from high. The S4 update walk itself does not fail, and the "cuts a release" half is weaker because `kits.cut` exists as an item row.

#### C5-F1 — The receipt never gains the release tag and source remote that the currency watch reads
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0435
- **Class:** K6, c2
- **Severity:** high
- **Evidence:** layer-expansions:438 put "the release tag, the source remote" in receipt schema 4, and `kits.currency` (layer-expansions:454) joins the receipt to gov's remote tag list, with "unreachable → unverified, never green". After the schema renumbering, cl-0020 gives schema 4 only `steps`, and cl-0435 gives schema 5 only `superseded`, `deprecations` and `prior_commit`. No clause carries a release or source field. Today `tools/govkit/govkit.py:49` is `RECEIPT_SCHEMA = 3`, and line 8020 writes `"gov_source": str(root)`, a local path.
- **Consequence:** gap-deploy-12, which dShippedRelease owns, is closed by no unit. cl-0417's currency watch has no installed release to count from. In S4 (an adopter two releases behind) the currency record reads unverified, and `currency.on-behind` never fires.
- **Fix:** Add `release` and `source_remote` to cl-0435's schema-5 fields, and name `kits.currency` as their reader. Plant a receipt with no release tag and see it red.
- **Skeptic:** confirmed high.

### Place 42: architecture-v2 · P14 · worst medium · includes an unverified finding

#### A1-F9 — P14's "review lenses read the active practices' reach" has no enforcing clause
- **Address:** architecture-v2 [enforcement] `P14`; architecture-v2 [principles] P14
- **Claimed:** no clause makes a review lens load the active practices' reach.
- **Skeptic:** Refuted (batch 1). Every work order loads "the step's practice reach" (flow-steps:47-51), each step lists reviewers at a breakpoint among its roles, and `review.lens` is an item. `cl-dClosedLoop-0168` renders a work order per item, and `cl-dClosedLoop-0051` hands each practice's reach per step in work orders, so a lens reads the active reach through its work order.
- **Second skeptic:** Confirmed medium. I rebuilt the [chain] clauses from v2 into the scratch file `clauses.txt`. No clause ties a lens to practice reach. The P14 row (v2 :1698) names `cl-dClosedLoop-0031`, which is only the catalogue. It also names `cl-dClosedLoop-0051`, which hands step-scoped reach to role work orders. The lens clauses (0070, 0080, 0458, 0470) fill the harness's lens slots from catalogue data and never mention reach. The Review-stage reach that foundations :71-76 describe has no step to be scoped under.

### Place 43: architecture-v2 · P29 · worst medium

#### B4-F14 — P29's row leaves out the clauses that carry most of P29
- **Address:** architecture-v2 [enforcement] `P29`
- **Class:** K5
- **Severity:** medium
- **Scenario:** S7
- **Defect:** P29's row names only `cl-dClosedLoop-0178`, which covers its first two rules. The verifier-context, answered-calls and false-facts rules sit in `cl-dClosedLoop-0196`, `0197` and `0198`, outside the row.
- **Consequence:** dOrderedCharter's meta-check never joins three of P29's rules to the principle.
- **Fix:** Add 0196, 0197 and 0198 to P29's row.
- **Skeptic:** Confirmed medium.

#### C3-F28 — P29's enforcement row names one clause, though P29 has several rules
- **Address:** architecture-v2 [enforcement] P29
- **Class:** K5
- **Severity:** medium
- **Evidence:** v2:1713 names only cl-0178 for P29. P29 (v2:866-881) also covers verifiers alone and cold (`roles.verifier-context`), answered calls (`roles.answered-calls`), false facts (`roles.on-contradiction`), acting on keyed facts (`roles.trust`), and "Recall: recall is re-verified once, by the orientation scout at entry". cl-0196, cl-0197, cl-0198 and cl-0205 carry those keys but sit in no row. No clause carries the recall re-verification; cl-0192 and cl-0204 only compose the card.
- **Consequence:** The principle registry certifies P29 from a clause that carries one of its rules, and the recall boundary is never built.
- **Fix:** Add cl-0196, cl-0197, cl-0198 and cl-0205 to P29's row, and add the recall re-verification to cl-0192.
- **Skeptic:** confirmed medium.

### Place 44: architecture-v2 · P3 · worst medium

#### A4-F13 — No clause builds P3's remote-CI verdict slot or the verdict-backend registry
- **Address:** architecture-v2 [enforcement] `P3`
- **Class:** K5
- **Severity:** medium
- **Scenario:** S7
- **What is wrong:** P3's row names only `cl-dClosedLoop-0342` and `cl-dClosedLoop-0344`. The clauses touch remote CI only in `cl-dClosedLoop-0029` (the floor in CI) and `cl-dClosedLoop-0279` (the headless spike). layer-expansions:179 makes the verdict-backend registry a Test core point that dWitnessedBar builds, and no clause builds it.
- **Consequence:** The `verdict` key's `remote-ci` value and integrations' backend have no core point to register at, so part of P3 is enforced by nothing.
- **Fix:** Add a dWitnessedBar clause for the verdict-backend registry and its `remote-ci` slot, seen red on a planted unregistered backend, and list it in P3's row.
- **Skeptic:** Confirmed medium (batch 1). whole-audit [stage0] already lists this as a K5 lead.

#### B3-F6 — dWitnessedBar owns the remote verdict, but no unit builds it
- **Address:** architecture-v2 [chain] dWitnessedBar row; architecture-v2 [enforcement] `P3`
- **Class:** K5
- **Severity:** medium
- **Scenario:** S2
- **Defect:** gap-test-02 (HIGH) gives dWitnessedBar the verdict-backend registry and the remote verdict under `verdict: remote-ci`. No clause in 0339 to 0368, or in any other row, builds the registry, the `remote-ci` read, or `verdict.remote.trust`, `.pin-scope` and `.pin`. The integrations clauses (0425, 0429, 0432) do not build them either.
- **Consequence:** A node that selects `remote-ci` is judged by a workflow in the tree it judges, with no pin or trust guard. `cl-dClosedLoop-0014`'s no-reader arm reds the three keys once dWitnessedBar lands.
- **Fix:** Give dWitnessedBar a clause for the backend registry and the pinned-workflow trust arm, seen red on a build that edits its own pinned workflow. Or move gap-test-02 and the three keys to an integrations row and record the move.
- **Skeptic:** Confirmed medium.

### Place 45: architecture-v2 · [chain] · worst medium

#### C3-F15 — dTotalRecall owns gap-mem-23 (touch-drop wired to nothing), but no clause of it carries the gap
- **Address:** architecture-v2 [chain] dTotalRecall row, Gaps owned (`gap-mem-23`)
- **Class:** K8
- **Severity:** medium
- **Evidence:** gap-mem-23: "`--drop-affordance-exempt` has no caller in `tools/`". In the working tree the flag appears only in `tools/codebase-map/map_diff.py` and its README. The touch-drop is wired by cl-0407 (dScopedBuild, a descendant), which calls `drop_touched_exemptions`. None of cl-0212 to cl-0237 mentions it.
- **Consequence:** The gap's owner lands without closing it, and its actual closer does not own it.
- **Fix:** Move gap-mem-23 to dScopedBuild, which completes the closure and descends from dTotalRecall, by the register's own rule. Alternatively, add a dTotalRecall clause wiring the drop.
- **Skeptic:** confirmed medium.

#### C3-F23 — dLinkedLibrary owns gap-mem-11 and gap-mem-12, but no clause of it carries either
- **Address:** architecture-v2 [chain] dLinkedLibrary row, Gaps owned (`gap-mem-11`, `gap-mem-12`)
- **Class:** K8
- **Severity:** low
- **Evidence:** gap-mem-11 covers records that contradict code: the map README path, `backlog.py`'s claim, the DEPL rows, `ANNOTATION-STYLE` saying no gate reads comment citations, and `HYGIENE.md`'s unused `note` kind. gap-mem-12: "the annotation follow-through test decides nothing: it has no threshold, sample size or window". No clause of cl-0238 to cl-0261 mentions either; a search of all clauses for follow-through, ANNOTATION-STYLE or `note` finds only cl-0241's grammar.
- **Consequence:** Both gaps survive their owner's landing, and the pushed-at-read fallback has no deciding test.
- **Fix:** Add a clause correcting gap-mem-11's records, including the ANNOTATION-STYLE guide and template pair. Set gap-mem-12's threshold, sample and window in cl-0244.
- **Skeptic:** confirmed low. layer-memory:1226 also gives gap-mem-12's threshold to dTotalRecall, not to the owner dLinkedLibrary.

### Place 92: architecture-v2 · cl-dClosedLoop-0374 · worst medium

#### C5-F14 — Plan Review and the landing review run before the build that supplies their lenses, with no stand-in
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0374 and cl-dClosedLoop-0424 (with cl-dClosedLoop-0458)
- **Class:** K7
- **Severity:** medium
- **Evidence:** cl-0374 (dRankedPlan) builds "Plan Review", and cl-0424 (dShippedRelease) "the landing review blocking the build's close". cl-0458 (dCalibratedLens) supplies "lenses for Plan, Test, Deploy and Maintain". dCalibratedLens descends from dRankedPlan, and it and dShippedRelease do not descend from each other. `review.plan` is opt-in, and neither clause names a stand-in lens from dFairHearing's catalogue.
- **Consequence:** From dRankedPlan's landing until dCalibratedLens's, the Plan breakpoint has no lens, and the landing review is in the same position.
- **Fix:** cl-0374 and cl-0424 each name a stand-in lens from dFairHearing's catalogue until dCalibratedLens lands.
- **Skeptic:** confirmed medium, narrowed. The split-rule half does not hold: gap-plan-04, gap-deploy-06 and gap-review-01 are three gaps, each with one owner.

### Place 93: architecture-v2 · cl-dClosedLoop-0378 · worst medium

#### CS1-F1 — The ratification fallback ends when "that hook" lands, but cl-0283 keeps it per harness, and the two builds are unordered
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0378, read against cl-dClosedLoop-0283
- **Class:** K7
- **Severity:** medium
- **Evidence:** cl-0378: "until that hook and the intake kind land, `plan.exit` … falls back to dDeclaredLoop's owner gate". cl-0283 (dWellOiledMachine) drains "RC-9's fallback … per harness, only where an adapter's capability table declares the prompt-submit event and kept in force for any other, seen on a planted Codex-shaped adapter that still reaches Plan's exit". dRankedPlan's parents (dDeclaredLoop, dTotalRecall, dBoundRoles) do not include dWellOiledMachine, nor the reverse, so either may land first.
- **Consequence:** If dWellOiledMachine lands first, cl-0283's acceptance needs a Plan exit that does not exist yet. dRankedPlan's spec, reading cl-0378, then finds the hook landed and builds no fallback, so a Codex-shaped harness has no ratification path.
- **Fix:** Make cl-0378's condition per harness ("until the harness's adapter declares the prompt-submit event"). Order the two builds, or move cl-0283's planted case to whichever lands second.
- **Skeptic:** raised by skeptic batch 1 on re-walking cl-0378, which walker 5 had passed as holding. No second skeptic judged it.

### Place 94: architecture-v2 · cl-dClosedLoop-0382 · worst medium

#### C5-F13 — gap-flow-04's closure spans two builds that do not descend from each other, and gap-flow-03 has no closing clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0382 (dRankedPlan, Gaps owned)
- **Class:** K8
- **Severity:** medium
- **Evidence:** gap-flow-04 ("no recorded plan revision and no re-design inventory of completed work") is dRankedPlan's, but its inventory half is `design.inventory` (dIndexedDesign, flow-steps:183). Neither build descends from the other, which the register's split rule (gap-register:12) forbids. cl-0382 only mentions "a plan revision" without building its record. No dRankedPlan clause matches gap-flow-03 (the card, plan and brief levels).
- **Consequence:** The gap join reads dRankedPlan as closing a gap whose inventory half lands elsewhere. No unit builds the plan-revision record, and the three-times-written plan stays.
- **Fix:** Split gap-flow-04 into a dRankedPlan key (the plan-revision record, built by a clause) and a dIndexedDesign key (the inventory). Add a dRankedPlan clause declaring the card, plan and brief levels, for gap-flow-03.
- **Skeptic:** confirmed medium.

### Place 95: architecture-v2 · cl-dClosedLoop-0383 · worst medium

#### C5-F16 — The Design hand-off and overlap keys are read by no clause, so the overlap refusal is unbuilt
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0383 and cl-dClosedLoop-0384
- **Class:** K4
- **Severity:** medium
- **Evidence:** `design.handoff` (derived-ready, ready-plus-audit, status-and-tier) and `design.overlap` (warn, refuse, index-only) are dIndexedDesign's (v2:1158-1159), and no clause names either; stage0-leads:155-156 agree. cl-0383 says only "the derived-READY hand-off" and cl-0384 "the design index". flow-steps:200 lists both among Design's policies.
- **Consequence:** The `refuse` value of the guard-bearing `design.overlap` passes the schema and only warns, and `ready-plus-audit` is never built.
- **Fix:** cl-0383 reads `design.handoff` and cl-0384 reads `design.overlap`, each value seen on a planted overlapping roster.
- **Skeptic:** confirmed medium.

### Place 96: architecture-v2 · cl-dClosedLoop-0400 · worst medium

#### B2-F16 — P19's one clause names no refusing check, and a deviation record admits a revision after a pass
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0400`
- **Class:** K5
- **Severity:** medium
- **Scenario:** S3
- **Defect:** 0400, "built specs frozen", has no check and no seen-red. `cl-dClosedLoop-0004`'s population, each spec revision after the unit's first attributed pass commit, includes a landed unit's spec. `cl-dClosedLoop-0412` passes such a revision once it has a deviation record.
- **Consequence:** A patch build can revise a built unit's spec in place under an approved deviation. P19 requires a new unit.
- **Fix:** Add to 0400 a refusal of any revision of a unit whose spec is in a landed range, its deviation population included, seen red on a planted in-place edit of a landed unit's spec.
- **Skeptic:** Confirmed medium. No freeze check appears in v2 or flow-steps. final-questions' rule that a change after landing is a new unit is enforced by nothing.

### Place 97: architecture-v2 · cl-dClosedLoop-0406 · worst medium

#### C5-F5 — Build drains only "in hunks" and always claims, so `retrofit.drain` and `retrofit.claim-on-touch` have unbuilt values, and velocity selects `carry`
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0406
- **Class:** K9
- **Severity:** medium
- **Evidence:** cl-0406 hard-codes "in hunks under `retrofit.drain-cap`" and "claiming … under `retrofit.claim-cap`". v2 gives dScopedBuild `retrofit.drain` (hunk, file, off) and `retrofit.claim-on-touch` (claim, carry, off), and no clause names either. The preset row at v2:1571 gives velocity `carry`. retrofit:404-406 defines the `file` and `off` arms.
- **Consequence:** A velocity repository still claims and drains, contradicting its preset. The `file` and `off` values validate in the schema and do nothing.
- **Fix:** Have cl-0406 read both keys and build each value's arm, each value seen on a planted unit.
- **Skeptic:** confirmed medium.

### Place 98: architecture-v2 · cl-dClosedLoop-0415 · worst medium

#### CS4-F2 — `deploy.unlease` is built without its mailbox close, and no clause carries copy-before-prune
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0415
- **Class:** K1
- **Severity:** medium
- **Evidence:** cl-0415 builds `deploy.unlease` "closing each of a build's leases with a terminal tombstone" and says nothing of the mailbox. flow-steps:376's item "closes its mailbox". flow-steps:55-59: "every message still on its mailbox ref, disposed or not, is copied into the build folder, and the undisposed ones are marked … Only then is the ref pruned". No clause pairs mail with prune, copy or unlease; cl-0143 says only "kept in the build's transition log".
- **Consequence:** A builder of the clause may never close the mailbox, or may prune the ref without copying and lose undisposed messages. `life.unlease` has the same gap.
- **Fix:** Add the mailbox close to cl-0415, with copy-before-prune and undisposed messages marked. Plant a build with an undisposed message, unlease it, and see the copy in the folder and the ref pruned only after it.
- **Skeptic:** raised by skeptic batch 4 on re-walking cl-0415, which walker 5 had passed as holding. No second skeptic judged it.

### Place 99: architecture-v2 · cl-dClosedLoop-0419 · worst medium

#### C5-F12 — The derived runbook and release notes have no losing test, and the runbook is derived again at convergence
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0419 (and cl-dClosedLoop-0414, cl-dClosedLoop-0489)
- **Class:** K10
- **Severity:** medium
- **Evidence:** cl-0419 is only "a derived runbook" and cl-0414 only "kit release notes", with no red case. final-questions [help] (220, 225) and research-final-help:129 record that the derived runbook and release notes have no losing test, and final-questions [folded] (382-404) does not fold it. cl-0489 (dConvergedCharter) then migrates "the agent runbook … its reference half generated".
- **Consequence:** The first derivation's acceptance cannot fail, and two builds derive the same document under different rules.
- **Fix:** cl-0419 states its render-parity red on a hand-edited runbook section, and cl-0414 a red on notes missing a landing. cl-0489 either cites cl-0419's derivation, or cl-0419 moves into cl-0489.
- **Skeptic:** confirmed medium.

### Place 100: architecture-v2 · cl-dClosedLoop-0422 · worst medium

#### C5-F11 — The landing queue has no ordering rule, and Deploy and distribution keys are read by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0422 (and cl-dClosedLoop-0417, cl-dClosedLoop-0437)
- **Class:** K4
- **Severity:** medium
- **Evidence:** P21: "landings go in plan priority, then first verified", and `landing.order` offers plan-priority-then-first-verified, first-verified and owner-orders. None of `landing.order`, `deploy.runs`, `deploy.currency`, `kits.cadence`, `kits.host`, `kits.watch-cadence` or `commits.squash` appears in any clause. cl-0422 says only "landings ordered through the landing queue it builds", and P21's row (v2:1705) relies on it. flow-steps:407 says "ordered by `landing.order`", but no clause carries it. cl-0437 builds `commits.squash`'s three values without naming the key.
- **Consequence:** P21's ordering half has no enforcing clause, and `owner-orders` is unbuilt. The cadence and host keys that `kits.currency` runs on have no clause reading them.
- **Fix:** cl-0422 orders the queue "as `landing.order` says", each value planted. cl-0417 reads `kits.watch-cadence`, `kits.host` and `deploy.currency`. cl-0437 names `commits.squash`.
- **Skeptic:** confirmed medium.

### Place 101: architecture-v2 · cl-dClosedLoop-0423 · worst medium

#### C5-F3 — A post-landing core red "stops that build from closing", but the settled route closes it through the post-close row
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0423
- **Class:** K2
- **Severity:** medium
- **Evidence:** cl-0423: "so a core red the landing merge introduced stops that build from closing (foundations K1)", which foundations:369-377 reads as no exit "until the red is fixed or excepted". flow-steps:369 (`deploy.core`): "red → a patch build through the entry-point table's post-close row, and the close waits for its filing". layer-flow:326-328 routes the same red through the post-close row.
- **Consequence:** A lander built from the clause holds the build open, with its leases and mailbox, until the red is fixed. A Deploy step built from flow-steps closes it once the patch build is filed. The S6 landing route has two incompatible terminals.
- **Fix:** Reword cl-0423: "… a core red the landing merge introduced files a patch build through the post-close row before the build closes". Plant a red landed tree whose close happens without that filing, and see it red.
- **Skeptic:** confirmed medium.

### Place 102: architecture-v2 · cl-dClosedLoop-0438 · worst medium

#### A4-F5 — `adopt.declarations` and `adopt.instructions` are named by clauses but have no item row
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0438`
- **Class:** K1
- **Severity:** medium (the walker graded it high, c2)
- **Scenario:** S4
- **What is wrong:** `cl-dClosedLoop-0438` defines `adopt.declarations`, and adopter-instructions:183 says the program "gains `adopt.instructions`". flow-steps [adopt] (611-615) holds rows only for `adopt.census`, `test.seed`, `adopt.practices`, `adopt.decisions` and `adopt.reconstruct`, and layer-expansions has none.
- **Consequence:** S4's "declarations proposed as overlay rows" has no declared actor, needs, witness or route, and it escapes the item join over repository-level items. `cl-dClosedLoop-0438` carries the behaviour and a fixture, so S4's update still runs.
- **Fix:** Add a row for `adopt.declarations`: the command proposes, then an owner ruling item witnessed by the ruling records, then the overlay write. Add a row for `adopt.instructions`. Give each its Owner.
- **Skeptic:** Confirmed medium (batch 1), graded down from high. It is a missing declaration a spec writer trips over, not a failing scenario.

### Place 103: architecture-v2 · cl-dClosedLoop-0443 · worst medium

#### C5-F9 — Maintain's host, cadence, events, reading admission and run record are built by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0443, cl-dClosedLoop-0445 and cl-dClosedLoop-0447
- **Class:** K4
- **Severity:** medium
- **Evidence:** `maintain.host`, `maintain.cadence`, `maintain.events`, `maintain.reading-admission` and `observability.run-record` are named by no clause. Stage 0's K4 lists all five as unread, three guard-bearing, and its K3 shows the run record with no writer and no reader (stage0-leads:129-130). layer-expansions admits a reading with no derivable owner only "under `maintain.reading-admission: report-unowned`", and has the journal reader write a run's record "as `observability.run-record` says". cl-0443, cl-0445 and cl-0447 say only "the cadence, on Runtime's hosts", "detectors with owners" and "the maintenance record". The default `maintain.events` includes `release-verify-failed`, whose producer kind is dShippedRelease's, not an ancestor.
- **Consequence:** The admission guard's refuse and report arms, the run record (gap-maint-14) and the event subset are unbuilt or unspecified.
- **Fix:** cl-0443 reads `maintain.host`, `maintain.cadence` and `maintain.events`, with `release-verify-failed` rendering "not installed" until dShippedRelease lands. cl-0445 builds both admission values. cl-0447 adds the run record under `observability.run-record`. Each is seen on a planted case.
- **Skeptic:** confirmed medium, narrowed. layer-expansions:232 already limits `release-verify-failed` to "when integrations is installed", so the missing stand-in is a partial gap only.

### Place 104: architecture-v2 · cl-dClosedLoop-0445 · worst medium

#### C5-F10 — Three gaps Maintain owns are closed by no clause
- **Address:** architecture-v2 [chain] dTendedCadence row, Gaps owned (cl-dClosedLoop-0445)
- **Class:** K8
- **Severity:** medium
- **Evidence:** dTendedCadence owns gap-maint-09 (five drift signals become core legs: ledger_rows, non_terminal_specs, closed_specs, handkept, cutoff_keys_armed), gap-maint-10 (a reading varies with its tree, answered by `maintain.reading-tree`) and gap-maint-11 (the remote-CI drift signal is dead) (gap-register:427-429). A search of every clause for those signals, `reading-tree` or the remote-CI signal finds only cl-0277, the lexicon's two signals.
- **Consequence:** The five drift signals stay report-only in drift-audit, with the merge bar reaching them through an optional kit. The tree-variance and dead-probe gaps close in name only.
- **Fix:** Add a dTendedCadence clause carrying all three: the five legs moved to their owning layers' packs, readings taken under `maintain.reading-tree`, and the dead remote-CI signal fixed or retired. Alternatively, move gap-maint-09 to the builds that own those legs.
- **Skeptic:** confirmed medium.

### Place 105: architecture-v2 · cl-dClosedLoop-0449 · worst medium

#### C5-F8 — Maintain's build delivers the Loop Review, a program its descendant dCalibratedLens owns
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0449
- **Class:** K7
- **Severity:** medium
- **Evidence:** cl-0449 (dTendedCadence) delivers "Maintain and the Loop Review … as cadence steps of the observability expansion". The items `loop.lease` to `loop.record` (layer-expansions:253-262) and `record-kind.loop-review` (design-map:290) belong to dCalibratedLens, a descendant, and cl-0460 builds the Loop Review again.
- **Consequence:** When dTendedCadence lands, its cadence step registers a program with no items, and two builds' clauses carry the Loop Review's registration.
- **Fix:** cl-0449 registers Maintain's cadence step only, and cl-0460 registers the Loop Review's. Alternatively, cl-0449 names a "not installed" stand-in until dCalibratedLens lands.
- **Skeptic:** confirmed medium.

### Place 106: architecture-v2 · cl-dClosedLoop-0460 · worst medium

#### C5-F7 — The Loop Review is fixed at "weekly", and `budgets.*` is read by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0460 (and cl-dClosedLoop-0461)
- **Class:** K4
- **Severity:** medium
- **Evidence:** cl-0460 fixes "the weekly Loop Review". v2:1213 gives dCalibratedLens `review.loop.cadence` (weekly, monthly, every-n-landings), which no clause names, and layer-expansions keys the Loop Review by ISO week. Stage 0's K4 lists `review.loop.cadence` and `budgets.*` as unread.
- **Consequence:** The monthly and every-n-landings values pass the schema and run weekly. The cap keys cl-0461 re-derives have no clause naming them.
- **Fix:** cl-0460 reads `review.loop.cadence`, keys the lease by the selected period, and sees each value on a planted case. cl-0461 names `budgets.*` as what it re-derives.
- **Same as:** C1-F13, for the `budgets.*` half only.
- **Skeptic:** confirmed medium, narrowed on the `budgets.*` half. cl-0015, cl-0041 and cl-0064 read `budgets.enforce` and `budgets.pinned`, and cl-0461's "caps re-derived" is in substance the `budgets.*` row's default.

### Place 107: architecture-v2 · cl-dClosedLoop-0495 · worst medium

#### C5-F21 — Convergence folds the house file over the owner's earlier rulings on the same values
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0495 (against cl-dClosedLoop-0438)
- **Class:** K10
- **Severity:** medium
- **Evidence:** cl-0438 (dShippedRelease) proposes "the house file's efforts as `roles.effort.*` values … for the owner to rule once" (flow-roles-adoption:264). cl-0495 later folds "a repository's efforts … into the `roles.effort.*` policy keys … with an upgrade step", and reads no prior ruling or declined row. P8: "an update never overwrites or silently drops a repository's change".
- **Consequence:** An owner who declined a proposed effort has it written into the policy file by convergence's upgrade step, which overrides the ruling (P8, P38).
- **Fix:** cl-0495's step folds only values with no ruling from cl-0438, and reads a declined row as a drop. Plant a declined proposal and see it survive the fold.
- **Skeptic:** confirmed medium.

### Place 108: architecture-v2 · install.retired-edits · worst medium

#### A4-F9 — `install.on-shim-call: refuse` and `install.retired-edits: delete` break P38 and P8, and two values have no arm
- **Address:** architecture-v2 [policies] `install.retired-edits`, `install.on-shim-call`
- **Class:** K9
- **Severity:** medium
- **Scenario:** S4
- **What is wrong:** `install.retired-edits` allows "order, keep, delete" (v2:1277), and `install.on-shim-call` allows "warn, journal, refuse" (v2:1276). `cl-dClosedLoop-0026` plants only the `order` grading, so `keep` and `delete` are never seen red, while `cl-dClosedLoop-0023` sees each shim value. No preset selects either loosening value.
- **Consequence:** An owner override can delete an adopter-edited retired file, against P8's "never overwrites or silently drops". It can also make a shimmed hook path fail inside its window, against P38's "keeps working, or warns".
- **Fix:** Drop `delete` and `refuse`, or keep them with a recoverable copy and an order, declared as loosenings. Add planted arms for `keep` and `delete`.
- **Skeptic:** Confirmed medium (batch 1).

### Place 109: architecture-v2 · plan.triage · worst medium

#### B1-F10 — Plan's owner values switch nothing
- **Address:** architecture-v2 [policies] `plan.triage`, `plan.authority`
- **Class:** K4
- **Severity:** medium
- **Scenario:** S1
- **Defect:** The strict values `plan.triage: owner-batches` and `plan.authority: owner-orders` appear in no item. `plan.triage-rule` is a command and `plan.triage-judge` is the planner, so the owner never acts.
- **Consequence:** Owner switches that switch nothing, against P10. `cl-dClosedLoop-0014`'s no-reader arm reds such keys once their owner build lands.
- **Fix:** Give each owner value an item and a clause, for example a `plan.triage-owner` item under `owner-batches`, or retire the value with a decision.
- **Skeptic:** Confirmed medium, narrowed. `plan.kickoff` is read by `cl-dClosedLoop-0375`, and `planner-drafts-owner-ratifies` does not contradict `plan.ratification: request`. The finding's Stage 0 K4 lead list could not be checked.

### Place 110: architecture-v2 · roles.model.<role> · worst medium

#### A2-F11 — `roles.model.<role>` holds one model while `roles.harness.<role>` admits several harnesses
- **Address:** architecture-v2 [policies] `roles.model.<role>`, `roles.harness.<role>`
- **Class:** K9
- **Severity:** medium
- **Scenario:** S2
- **What is wrong:** v2:1063 takes one model, defaulting to the role's single declared model (layer-roles:476). v2:1064 lets a role run on "one or more" harnesses. `cl-dClosedLoop-0332` drops work whose model the node lacks.
- **Consequence:** Node x, on another harness, lacks the role's model, so the pick never offers it X's unit. S2's cross-harness take fails even with the key unset.
- **Fix:** Key the model per harness (`roles.model.<role>.<harness>`), or make the value a map from harness to model. The preset check reds a role whose harness set has no model for one of its members.
- **Skeptic:** Confirmed medium (batch 1). The default is the role's single declared model, which makes the defect stronger than the finding says.

### Place 152: architecture-v2 · [clause-ids] · worst low

#### B2-F12 — v2 never defines the text a clause hash is taken over
- **Address:** architecture-v2 [clause-ids]
- **Class:** K6
- **Severity:** low
- **Scenario:** S7
- **Defect:** [clause-ids] says only "its text's hash being its revision". The normalisation (SHA-256, the first eight hex digits, the id cut off, whitespace folded) is defined only in carries.py, which neither v2 nor final-questions cites.
- **Consequence:** A dTrueNorth spec writer working from v2 can choose another normalisation, and every pin the instrument wrote then reads stale under the product join.
- **Fix:** State the hash rule in [clause-ids], and have `cl-dClosedLoop-0001` cite it.
- **Skeptic:** Confirmed low.

### Place 163: architecture-v2 · cl-dClosedLoop-0371 · worst low

#### C5-F19 — Plan's triage, kickoff and authority keys are built only at their defaults
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0371, cl-dClosedLoop-0375 and cl-dClosedLoop-0370
- **Class:** K4
- **Severity:** low
- **Evidence:** v2 offers `plan.triage` (owner-batches, rules, archive-legacy), `plan.kickoff` (offer-next, binding, advisory) and `plan.authority` (planner-drafts-owner-ratifies, planner-within-themes, owner-orders), and Stage 0's K4 lists all three as unread. cl-0371 carries "rule-based triage", cl-0375 "kickoff offering the next item", and cl-0370 names no `plan.authority`. The presets select `owner-batches`, `binding` and `owner-orders` (v2:1469-1472), which no clause builds.
- **Consequence:** The other values, including those the presets select, are accepted by the schema and never take effect.
- **Fix:** Name each key in its clause, with each value's arm planted.
- **Skeptic:** confirmed low.

### Place 164: architecture-v2 · cl-dClosedLoop-0390 · worst low

#### B2-F14 — P17's classifier is marked "(proposed)" in its one enforcing clause
- **Address:** architecture-v2 [enforcement] `P17` / [chain] `cl-dClosedLoop-0390`
- **Class:** K5
- **Severity:** low (the walker graded it medium, c5)
- **Scenario:** S1
- **Defect:** 0390 reads "additive-versus-breaking interface classification (proposed)". It is the only such marker in v2, and it is stale: flow records FL-B4 as answered.
- **Consequence:** A spec writer can read P17's classifier as not yet committed.
- **Fix:** Drop "(proposed)" from 0390.
- **Skeptic:** Confirmed low, not c5. The classifier is carried in the same clause ("two-level re-entry by `design.reentry`"), and flow-steps makes `design.reentry` a dIndexedDesign command that classifies an amendment by a structural diff.

### Place 165: architecture-v2 · cl-dClosedLoop-0397 · worst low · includes an unverified finding

#### C5-F23 — `design.streams` names both an item and a key, and the planner item's Needs loops onto itself
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0397
- **Claim:** The needs graph and the tag index cannot tell the item from the key.
- **Skeptic:** refuted. flow-steps:188's Needs cell is "`design.overlaps`, where `design.streams` holds for the build". The only edge is to `design.overlaps`, the second name is a policy condition, and Stage 0's "cycle" is a parser artifact. The design map keeps items and policy keys in separate namespaces, as with `build.scope`, which cl-0407 grades by value without ambiguity.
- **Second skeptic:** Confirmed low. `design.streams` is both the planner item (flow-steps:188) and a key (v2:1160). The item's Needs cell reads "`design.overlaps`, where `design.streams` holds for the build", which is the self-cycle Stage 0's K1 reports (stage0-leads:13). The design's own precedent renamed `maintain.record-when` "so the item `maintain.record` keeps its name" (v2:1199). The impact is a naming collision only.

### Place 166: architecture-v2 · cl-dClosedLoop-0402 · worst low

#### C5-F18 — When the closing review runs is a dScopedBuild key no clause reads
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0402
- **Class:** K4
- **Severity:** low
- **Evidence:** `review.build.when` (per-build, per-unit, per-landing; v2:1208, dScopedBuild) is named by no clause, and no flow-steps item reads it. cl-0402 reads only "the closing review recorded".
- **Consequence:** The per-unit and per-landing values pass the schema and run per build.
- **Fix:** cl-0402: "the closing review recorded, run as `review.build.when` says", each value planted.
- **Skeptic:** confirmed low.

### Place 167: architecture-v2 · cl-dClosedLoop-0430 · worst low

#### C5-F20 — "Runs neither … both" in cl-0430 has no antecedent inside the clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0430
- **Class:** K1
- **Severity:** low
- **Evidence:** cl-0430: "an update `kits.offer` offers runs neither in the adopter's tree, and its outbox order names the adopter's own run of both". The referents, `adopt` and `test.seed`, are named only in cl-0427, and the carries hash pins the clause text alone.
- **Consequence:** A spec carrying cl-0430 whole cannot tell which runs are withheld.
- **Fix:** Reword: "… runs neither `adopt` nor `test.seed` in the adopter's tree, and its outbox order names the adopter's own run of each".
- **Skeptic:** confirmed low.

### Place 168: architecture-v2 · cl-dClosedLoop-0448 · worst low

#### C5-F2 — "The memory's dead pointers" misnames the gate cl-0448 absorbs, whose population lies outside `memory/`
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0448
- **Class:** K10
- **Severity:** low (the walker said high, c3)
- **Evidence:** cl-0448: "a detector for the memory's dead pointers, owned by Maintain, absorbing `check-dead-paths.sh` and keeping its merge-bar leg". `tools/check-dead-paths.sh:2` covers "nothing outside `memory/`, and no map dossier or gotcha page" naming a deleted file, and its leg is "dead-path carriers (deleted files still named)".
- **Consequence:** The wording points a builder at memory pointers rather than the shipped-text population the absorbed gate checks.
- **Fix:** Name both populations in cl-0448: the old gate's shipped text, dossiers and gotchas, plus the auto-memory pointers.
- **Skeptic:** confirmed low (wording). The clause keeps the script's merge-bar leg (NP-22, night-pass:755: "so a dead path still blocks a merge"). The script is an `[[exempt]]` row at `tools/govkit/registry.toml:242`, so no adopter install ever carried it and no core-only install loses it.

### Place 169: architecture-v2 · cl-dClosedLoop-0488 · worst low

#### C5-F22 — The fates join's population leaves out rows the table holds
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0488
- **Class:** K10
- **Severity:** low
- **Evidence:** cl-0488's population is "`git ls-files` across `tools`, `skills`, `.githooks`, `.claude`, `.github`, `help`, the runbook and the template". The fates table has "hand-written guides | RETIRED" (fates:210, under `memory/guides/`) and `.unattended.conf` (fates:158) at the repository root.
- **Consequence:** A guide or a root kit conf that survives convergence matches no file in the population and escapes the exit check.
- **Fix:** Derive the population from every fates row's path glob plus the listed directories, and plant a surviving `memory/guides/` file to see it red.
- **Skeptic:** confirmed low.
