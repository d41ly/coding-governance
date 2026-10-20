# Fold brief: writer 2

**Serves:** research PLAY-dClosedLoop-1

**Your task is to fold the whole-design audit's findings at the 37 places below into dClosedLoop's design
records, as one fold script.** This brief is your instructions, not a spec to review.

## What you fold, and against what

- **The subject is the working tree's design records** under `memory/builds/dClosedLoop/build/`, at commit `8222099f8a619eef461fe91e84bd9f74173be730`.
  The findings were made on a sealed copy into which twelve past defects were planted. The copy is not your subject;
  read nothing in it. The plants are listed in the round record's `[recall-scored]`
  (`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`). A finding that describes a plant points at a defect
  the working tree never had.
- **Your records:** architecture-v2's `[chain]` rows of dBoundRoles, dFurnishedOrders, dTotalRecall, dLinkedLibrary, dMindYourWords, dWellOiledMachine, dWitnessedBar. Edit nothing else. When a place needs an edit in another record, list it under
  *Requests* in your return, with the exact change, and leave it out of your script.
- **Read freely** in the working tree: every design record, the gap register, the design map, `tools/`, `skills/` and
  `.githooks/`. Write only in your scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fold/w2/`. Nothing goes into the repository.

## How you fold

1. **For each place,** read its findings below, then read the place in the working tree. Give it exactly one
   disposition:
   - `fold`: the defect is in the working tree, and the fix follows from what the design already settles. Write it.
   - `fork`: the fix chooses between real options, or changes what the design means. Write no fold. Name the
     question, the options and your recommendation, for the owner.
   - `plant`: the finding describes one of the twelve plants, absent from the working tree. Cite the plant.
   - `not a defect`: the working tree already answers it. Quote where.
   - `duplicate`: another place carries the same defect. Name it, and fold it there.
2. **Write the folds as one Python script,** `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fold/w2/fold-2.py`, using the build's fold library:

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
3. **Forks,** each: `### FK-2-<k> — <question>`, then the options, your recommendation and the findings it rests on.
4. **Requests,** each naming the record, the exact change and the place it serves, or `none`.
5. **Read outside the list above:** `none`, or what and why.

Write nothing to the repository. Your effort is the one your role definition sets.

## The places

### Place 9: architecture-v2 · cl-dClosedLoop-0228 · worst high · critical

#### C3-F13 — The map's losing replay has no loss conditions
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0228
- **Class:** K10, c3
- **Severity:** high
- **Evidence:** project-map [test] (pm:699-702): "The map loses, and is not built, if any of these holds: the recall of the known set rises by less than the twin runs' difference plus 5 items; the median of existence searches per lens falls by less than one; the bytes read before the first act rise by more than the map's own bytes". cl-0228 says only "the replay with the map and without at its first unit … so a losing map is never built". cl-0253 extends the same undefined test to code.
- **Consequence:** "Losing" is undefined, so the replay certifies the map whatever it scores, and the routed loss path never runs.
- **Fix:** Carry the three loss conditions, and the twin runs they compare against, in cl-0228 and in cl-0253's extension.
- **Skeptic:** confirmed high.

### Place 10: architecture-v2 · cl-dClosedLoop-0239 · worst high · critical

#### C3-F17 — The reuse scout's acceptance re-runs the benchmark with no threshold
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0239
- **Class:** K10, c3
- **Severity:** high
- **Evidence:** layer-memory [reuse] (lm:717-718): the acceptance "re-runs aScoutedSeam's 24-case benchmark against the built index and entries, and must meet M1c's 16". research-scoutedseam-apply measured m1c at 8/12 on the held-out set. cl-0239 re-runs the benchmark and its twelve held-out cases with no bar.
- **Consequence:** The acceptance passes at any score, so a house index that loses to today's 13/24 checklist scout ships.
- **Fix:** Put the pass bar in cl-0239, on the tuning set and on the 12 held-out cases.
- **Skeptic:** confirmed high.

### Place 11: architecture-v2 · cl-dClosedLoop-0306 · worst high · critical

#### C4-F1 — The unattended-kit dissolve retires the supervisor's own seam and removes the tick that hosts it
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0306
- **Class:** K10 (a migration across a drain), c2
- **Severity:** high
- **Evidence:** cl-0306 retires "`resume-tick.sh` and the `RESUME_SCHEDULE_*` task … with an adopter's hand-registered resume task removed". cl-0284 says the opposite: "the supervisor: `resume-tick.sh` grown, started and restarted by the node tick". layer-runtime [supervise] (357-371) keeps the OS-scheduled `gov-resume-tick` registration as what starts the supervisor, refuses a run host without it at preflight, and retires only `RESUME_SCHEDULE_*`. Fates rows 145-146 mark `resume-tick.sh` RESHAPED into the supervisor and `RESUME_SCHEDULE_*` RETIRED. `tools/unattended/README.md:211,218` shows that `gov-resume-tick` is the hand-registered resume task.
- **Consequence:** The upgrade step deletes the supervisor's script and the node tick that starts and restarts it. Every run host then fails preflight, and the `host` fixture cannot pass. A crashed or rebooted supervisor never comes back, so unattended builds stop short of a terminal.
- **Fix:** In cl-0306, retire only `RESUME_SCHEDULE_*` and resume-tick's `--dangerously-skip-permissions` launch. Keep `resume-tick.sh` as the supervisor's seam (cl-0284), and keep the `gov-resume-tick` registration as the node tick, re-pointed rather than removed.
- **Skeptic:** confirmed high. cl-0306 contradicts cl-0284 and layer-runtime [supervise].

### Place 12: architecture-v2 · cl-dClosedLoop-0337 · worst high · critical

#### A2-F3 — The landing push releases the build's lease, so the Deploy items after the push run unfenced and no node can take them over
- **Address:** architecture-v2 [chain] dWellOiledMachine `cl-dClosedLoop-0337`; flow-steps [deploy] `deploy.unlease`, `deploy.close`
- **Class:** K10, c2
- **Severity:** high
- **Scenario:** S2
- **What is wrong:** `cl-dClosedLoop-0337` carries "the build's release" in the landing push, and `cl-dClosedLoop-0134` makes a landed build's release terminal, refusing every acquisition. flow-steps (369-376) runs `deploy.core` through `deploy.snapshot` after `deploy.land` and only then `deploy.unlease`. `cl-dClosedLoop-0133` requires every effect push to carry a lease beat, and `build.release-hold: whole-close` keeps the leases until `deploy.released`.
- **Consequence:** After X's landing push, the snapshot and close pushes have no lease to fence them. If d's session limit hits now, `cl-dClosedLoop-0325`'s hand-over has nothing to hand over, and `cl-dClosedLoop-0332`'s pick never offers a terminal tombstone. X lands but never reaches `deploy.close`.
- **Fix:** Make the landing push carry the lease beat only, and leave the release to `deploy.unlease` as flow-steps orders it. Otherwise state that the post-push Deploy items run under a close lease any node may take after a hand-over. See it red on a supervisor killed between `deploy.land` and `deploy.snapshot`, whose build a second node closes.
- **Skeptic:** Confirmed high, c2 (batch 1). `cl-dClosedLoop-0325`'s hand-over and `cl-dClosedLoop-0332`'s pick ("never a terminal tombstone") cannot recover a build that dies between land and close.

### Place 13: architecture-v2 · cl-dClosedLoop-0364 · worst high · critical

#### C4-F2 — The shared bash resolver accepts only MINGW or MSYS, which refuses every bash on Linux
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0364
- **Class:** K10 (a trust boundary and portability), c1
- **Severity:** high
- **Evidence:** cl-0364 accepts a candidate "only once it runs and answers `uname -s` as MINGW or MSYS … and a refusal in place of any fall-back", with no Windows scope, while claiming to keep the existing resolvers' contracts. away-pass [p4-compat] (line 174) puts Windows with Git-Bash and Linux at tier 1, and cl-0315 plans for Linux nodes. The existing resolvers accept by run probe, not by MINGW: `tools/govkit/govkit.py:1138` runs `-c :`, and `tools/run-gates/profile_bar.py:282` runs `test -f`.
- **Consequence:** On any Linux node `uname -s` prints `Linux`, so every gov launch site refuses. The bar, the hooks and the lander cannot run there, so builds cannot land from a tier-1 platform.
- **Fix:** Scope the MINGW/MSYS acceptance to a Windows host (`os.name == 'nt'`). Elsewhere, accept a candidate that runs and meets the bash floor, and add a Linux arm to the staged-break fixture.
- **Skeptic:** confirmed high.

### Place 35: architecture-v2 · cl-dClosedLoop-0231 · worst high

#### C3-F14 — Renaming the Serves kind `journal` to `log` ships with no adopter alias step
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0231 (with cl-dClosedLoop-0229)
- **Class:** K10
- **Severity:** high
- **Evidence:** memory-plan [integration] and [migration] (memory-plan:293, 297, 331) require dTotalRecall's adopter upgrade steps to include "the `journal` alias", and read the `journal` kind through it. cl-0229 renames the kind. cl-0231's steps list the scaffold verbs, the README front-matter grading and the retag step, but no alias.
- **Consequence:** After an update, an adopter's records carrying `**Serves:** journal` fail the Serves grading or lose their kind, against P38. gov itself holds 1,443 such records (memory-plan:125).
- **Fix:** Add the `journal` alias upgrade step to cl-0231, seen on a planted adopter record with `Serves: journal`.
- **Skeptic:** confirmed high. The count is 1,443, not the walker's 1,436, which does not change the finding.

### Place 36: architecture-v2 · cl-dClosedLoop-0301 · worst high

#### C4-F3 — The default load is replayed through a hook channel smaller than the map, and no clause carries the owed cap measurement
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0301 (also cl-dClosedLoop-0290)
- **Class:** K10
- **Severity:** high
- **Evidence:** cl-0301 has the session-start hook load "the card and the map by default … at a compaction", and `memory.map-budget` defaults to 32k. night-pass-two (line 401) says the harness keeps 10,000 characters of hook context and "past them text is silently lost". v2 [owed] gives the level-0 map as 31,203 of 32,768 B, and owes the compact and resume hooks' output cap "measured with a 32 KiB map" (night-pass [p5-compaction] item 4). layer-runtime (line 1022) lists "the card's size check". Neither cl-0290 nor cl-0301 carries the measurement or the size check.
- **Consequence:** After a compaction the map is cut to about a third of its size, and nothing reports it. gap-orient-18's fix ships without restoring the map, and the session works from a partial map it does not know is partial.
- **Fix:** Add to cl-0301 the owed measurement of the hook channel's cap against a 32 KiB map, and a size check that routes the over-cap remainder through an instruction-file channel or fails red. Add the card's size check to cl-0290.
- **Skeptic:** confirmed high.

### Place 40: architecture-v2 · cl-dClosedLoop-0217 · worst medium · critical

#### C3-F9 — Typed relations drop the `depends-on` cycle check and the pending-target rule
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0217
- **Class:** K10, c3
- **Severity:** medium
- **Evidence:** layer-memory [relations] (lm:547-550): "every relation's target must exist, and `depends-on` must form no cycle … A target found nowhere is pending, not red, until its build lands". cl-0217 says only "typed relations (…), inverted, checked both ways and rendered as the relation graph". dTotalRecall owns gap-mem-07 (gap-register:189, "no cycle check").
- **Consequence:** A `depends-on` cycle passes the check, leaving gap-mem-07 open. Otherwise, a target on another node's unlanded branch reds and refuses legitimate work.
- **Fix:** Add both rules to cl-0217: red on a planted two-build cycle, and pending on a planted target on another node's branch.
- **Skeptic:** confirmed medium.

### Place 68: architecture-v2 · cl-dClosedLoop-0176 · worst medium · includes an unverified finding

#### B2-F15 — No clause enforces P18's ranking of a fork's options
- **Address:** architecture-v2 [enforcement] `P18` / [chain] `cl-dClosedLoop-0176`, `cl-dClosedLoop-0390`
- **Skeptic:** Refuted. 0390 carries "fork resolution by `design.forks`", whose default `agents-feature-rich-expandable` is the ranking rule, and the charter renders it at level 0. 0176 and the fork record carry "with a full record". A ranked-list field is an addition the fix proposes, not a gap in the clauses.
- **Second skeptic:** Confirmed medium. architecture-v2 [enforcement] P18: the row cites only cl-0176 ("resolved by the role that meets it and recorded") and cl-0390 ("fork resolution by `design.forks`"). The fork record carries only "its id, its resolver and its declared class" (flow-steps `design.decompose` / `design.unit-spec`). No clause or check requires the options ranked by feature-richness and then expandability. The ranking appears only in the charter render (v2:973) and the default value's name.

#### C3-F1 — No clause carries P18's admitted-options rule or checks a fork's pick against the ranking
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0176
- **Class:** K5
- **Severity:** medium (the walker said high, c5)
- **Evidence:** P18: "Agents resolve forks by the most feature-rich option, then the most expandable, with a full record … only options the core admits are options". cl-0176 says only "every fork resolved by the role that meets it and recorded, or held as `run.on-owner-question` says". cl-0390, P18's other enforcing clause, says "fork resolution by `design.forks`".
- **Consequence:** An unattended role's pick is never checked against the admitted set or the ranking, so a pick outside them passes.
- **Fix:** Add the core-admitted option set and the full record to cl-0176. Plant a fork whose recorded pick is not the top-ranked admitted option, and see it red.
- **Skeptic:** confirmed medium, not c5. cl-0390 names `design.forks`, whose default `agents-feature-rich-expandable` (v2:1019) carries the ranking, and P18 has two enforcing clauses (v2:1702). The part with no clause is "only options the core admits are options", and the check that a pick is the top admitted option.

### Place 69: architecture-v2 · cl-dClosedLoop-0180 · worst medium

#### C3-F2 — `instructions.task-charter` is read by no clause, though dBoundRoles owns it
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0180
- **Class:** K4
- **Severity:** medium
- **Evidence:** v2 [policies] (v2:1231) gives `instructions.task-charter` (when-not-static, always) to dBoundRoles, and its single-carry check "refuses `always` on a backend that loads the static block". systems (410-413) has the single-carry check read the key and the harness kind. cl-0180 says only "the role static block carried once per spawn", and no [chain] row names the key.
- **Consequence:** The single-carry check is built without its key. Either `always` is accepted where the charter loads twice, or the key's value never routes.
- **Fix:** Have cl-0180 name `instructions.task-charter` and its refusal of `always` on a static-block backend, seen red on a planted `always`.
- **Skeptic:** confirmed medium.

#### C3-F3 — gap-roles-20, the static block's budget covering only its base body, is carried by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0180
- **Class:** K8
- **Severity:** low
- **Evidence:** gap-roles-20 (gap-register:171, "The static block's budget covers its base body only") is dBoundRoles's (v2:1641). layer-instruction:458 makes `BODY_CEILINGS` the role block's only budget carrier, research-instruction-writing-b N3 puts the 2,487–4,220 B charter blocks per role outside it, and `tools/roles/check_roles.py:84` reads "Bytes of each slot's BASE body". No clause of cl-0166 to cl-0191 budgets the whole rendered block.
- **Consequence:** The gap stays open after its owner lands, and the rendered charter blocks stay unbudgeted.
- **Fix:** Extend cl-0180: the budget covers the whole rendered static block, seen red on a planted charter block that pushes a role over its ceiling.
- **Skeptic:** confirmed low.

### Place 70: architecture-v2 · cl-dClosedLoop-0197 · worst medium

#### C3-F8 — The answered-call hook omits the verifier exemption, so the default `refuse` blocks a verifier reading its subject
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0197
- **Class:** K10
- **Severity:** medium
- **Evidence:** layer-roles [trust] item 10 (lr:331-336): "A verifier's read of its subject is never an answered call, and neither is a read the packet does not cover". It adds that below CLI 2.1.295 a rule on an ungated tool stays open when its hook fails, and the failure is recorded. cl-0197 says only "the answered-call hook (`roles.answered-calls`)", whose default is `refuse` (v2:1057). cl-0205 defers its details to unit specs.
- **Consequence:** A reviewer's or tester's read of its handed subject is refused, and verification stalls. The fail-open window also goes unrecorded.
- **Fix:** Carry both rules in cl-0197. See it green on a planted verifier read of its subject, and see a recorded failure on a planted hook crash.
- **Skeptic:** confirmed medium. P29 (v2:875-878) implies the exemption but does not carry it.

### Place 71: architecture-v2 · cl-dClosedLoop-0199 · worst medium

#### C3-F4 — Replacing the protocol pointers omits the same-unit re-point of the machinery that asserts them
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0199
- **Class:** K10
- **Severity:** medium
- **Evidence:** layer-roles [tags] (lr:376-380) requires the slicing unit to re-point, in the same unit, `CARRIED_SECTIONS`, `check_roles.py` R0, R5 and R10, and `render_agents.py`'s self-test arm 4. cl-0199 says only "the role files' re-verification orders and protocol pointers replaced by rendered slices". In code, `tools/roles/roles_lib.py:67` is `CARRIED_SECTIONS = ("Protocols", "Facts")`, `check_roles.py:169` reads the carried Protocols body, and `render_agents.py:335-338`'s arm 4 asserts the carried text.
- **Consequence:** Built from the clause, the slicing unit leaves R5, R10 and the self-test asserting the Protocols carry. The roles catalogue goes red, or the whole-document carry survives beside the slices.
- **Fix:** Name the four consumers in cl-0199 and require them re-pointed in the same unit.
- **Skeptic:** confirmed medium.

### Place 72: architecture-v2 · cl-dClosedLoop-0201 · worst medium

#### C3-F6 — Role metrics are written into the value ledger, which a later build registers, with no stand-in
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0201
- **Class:** K6
- **Severity:** medium
- **Evidence:** cl-0201 writes "role metrics per role and item into the value ledger". The design map gives `record-kind.value-ledger` to dCalibratedLens, built by cl-0459. dCalibratedLens is not an ancestor of dFurnishedOrders, whose only parent is dBoundRoles (v2:1642), and no stand-in is named.
- **Consequence:** dFurnishedOrders cannot be specced or landed in order, because its writer has no registered kind to write.
- **Fix:** Have cl-0201 write a metrics record dFurnishedOrders owns, which dCalibratedLens's ledger reads later, or add a stand-in until cl-0459 lands.
- **Skeptic:** confirmed medium.

### Place 73: architecture-v2 · cl-dClosedLoop-0202 · worst medium

#### C3-F5 — Five keys dFurnishedOrders owns are read by none of its clauses
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0202
- **Class:** K4
- **Severity:** medium
- **Evidence:** v2 [policies] gives dFurnishedOrders `annotations.delivery`, `roles.orientation.house-index`, `instructions.slices`, `retrofit.slot-bytes` and `memory.map-unfold` (v2:1228, 1229, 1234, 1247, 1261). None appears in any [chain] row, and Stage 0's K4 lists all five as unread, three of them guard-bearing. cl-0202 says "legacy slot in its four states" with no cap key, and cl-0203 says "the unfolds each item declares (PM-6)" with no key.
- **Consequence:** Each key's non-default value never routes. The legacy slot's 1 KB cap and the code-notes delivery have no switch.
- **Fix:** Name each key in the clause that builds its slot: `retrofit.slot-bytes` in cl-0202, `annotations.delivery` in cl-0209, `instructions.slices` in cl-0199, `memory.map-unfold` in cl-0203, and `roles.orientation.house-index` in a slot clause. Each value is routed and seen.
- **Skeptic:** confirmed medium.

#### C3-F7 — The memory slices read a sibling build's index and keys with no stand-in
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0202
- **Class:** K6
- **Severity:** medium
- **Evidence:** cl-0202 delivers "the work order's memory slices … each under its own budget and its own answer". systems [cross] (systems:214-215) prices them by `memory.item-budget` and answers them by `memory.over-budget`, both dTotalRecall's, and sections resolve through dTotalRecall's `record show` (cl-0220). dTotalRecall is not an ancestor of dFurnishedOrders. cl-0203 and cl-0208 carry "not installed until dTotalRecall's renderer lands"; cl-0202 does not. cl-0195's three-state rule covers only optional components and expansions, and memory is core.
- **Consequence:** The slot cannot be built in order, or it is built against a section index that does not exist yet.
- **Fix:** Add a stand-in to cl-0202: the memory slot renders "not installed" until dTotalRecall's section extractors land, as cl-0203 and cl-0208 do.
- **Skeptic:** confirmed medium.

### Place 74: architecture-v2 · cl-dClosedLoop-0216 · worst medium

#### C3-F10 — The slug grammar omits "binds new mints only", `BUILD_SLUG_RE`'s derivation and the named flips
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0216
- **Class:** K10
- **Severity:** medium
- **Evidence:** layer-memory [names] (lm:518-528): "A changed grammar binds new mints only. Existing slugs and ids keep their form, every reader accepts both, and the grammar in force at minting is recorded with each slug". It also derives `BUILD_SLUG_RE` from the `builds.slug-*` keys and names the flips. cl-0216 says only "proven by flipping the grammar in a scratch clone".
- **Consequence:** A grammar flip makes every reader reject existing slugs and ids across the tree, and the flip test can pass on one flip.
- **Fix:** Carry the new-mints-only rule, the recorded grammar per slug, the derived `BUILD_SLUG_RE` and the named flip set in cl-0216.
- **Skeptic:** confirmed medium.

### Place 75: architecture-v2 · cl-dClosedLoop-0219 · worst medium

#### C3-F11 — The code record's re-timing has no losing bound
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0219
- **Class:** K10
- **Severity:** medium
- **Evidence:** v2 [owed] (v2:1894-1896): the code record's cold derivation re-timed at dTotalRecall's first unit, "over 30 s or over 1 MB loses, on gov's tree and on a planted adopter-scale fixture". cl-0219 has only "re-timed on a planted adopter-scale fixture": no bound, and no gov tree.
- **Consequence:** The re-timing cannot fail, so an over-budget derivation ships.
- **Fix:** Put the 30 s and 1 MB loss bound, on both trees, into cl-0219.
- **Skeptic:** confirmed medium.

### Place 76: architecture-v2 · cl-dClosedLoop-0220 · worst medium

#### C3-F16 — Memory keys dTotalRecall owns are read by no clause, one of them guard-bearing
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0220 (also cl-dClosedLoop-0225)
- **Class:** K4
- **Severity:** medium
- **Evidence:** `memory.over-budget` (refuse, report, off; exempt from `budgets.enforce`), `memory.superseded-slices` (refuse, mark) and `memory.map-overflow` (degrade, refuse) are dTotalRecall's (v2:1242, 1250, 1246), and none appears in any [chain] row. cl-0220 says "reported when exceeded" and cl-0225 "degraded in a fixed order", neither naming its key. No clause carries the superseded-slices check. Stage 0's K4 lists all three.
- **Consequence:** `refuse` and `off` never route, the superseded-slice check is never built, and the exemption from `budgets.enforce` is lost.
- **Fix:** Name the three keys with their values and checks in cl-0220 and cl-0225.
- **Skeptic:** confirmed medium.

### Place 77: architecture-v2 · cl-dClosedLoop-0223 · worst medium

#### C3-F12 — The acceptance re-measure has no target or window
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0223
- **Class:** K10
- **Severity:** medium
- **Evidence:** systems [design-memory-structure] (systems:550-559): "Thirty days after landing, the median memory bytes per agent that reads memory are below 33 KB", with a note on why the first measure could not fail. cl-0223 says only "the acceptance re-measure counted over every read channel".
- **Consequence:** The measure has no pass bar, which repeats the could-not-fail defect the record already corrected.
- **Fix:** Add "median below 33 KB, 30 days after landing" to cl-0223.
- **Skeptic:** confirmed medium.

### Place 78: architecture-v2 · cl-dClosedLoop-0240 · worst medium

#### C3-F18 — `reuse_lookup.py` is retired without naming its by-value readers
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0240
- **Class:** K10
- **Severity:** medium (the walker said high, c3)
- **Evidence:** layer-memory [reuse] (lm:719-731) lists the by-value readers: hygiene check 12's §10 arm, which accepts the token `reuse_lookup` as reuse evidence (`tools/memory-tree/check-memory-hygiene.sh:2474`); `MAP_CLI` (`tools/unattended/kit.toml:174`); and the `reuse-probed` DoD item (`tools/unattended/PROTOCOL.template.md:356`). cl-0240 says only "retired with their readers rewritten".
- **Consequence:** A spec writer who skips the layer record leaves check 12 certifying a spec's reuse audit on a citation of a retired tool.
- **Fix:** Name the by-value readers in cl-0240. See red a planted spec citing `reuse_lookup` after the new cutoff.
- **Skeptic:** confirmed medium, below the walker's high. The design names these readers, so check 12 loosens only if a spec writer skips the layer record.

### Place 79: architecture-v2 · cl-dClosedLoop-0242 · worst medium

#### C3-F20 — README routing and the relation graph are each built by two builds
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0242
- **Class:** K8
- **Severity:** medium
- **Evidence:** cl-0242 (dLinkedLibrary) builds "the generated views: README routing, the relation graph, …". cl-0215 (dTotalRecall) already builds "a generated routing region by purpose", and cl-0217 has relations "rendered as the relation graph". memory-plan [practice]: "every node gov ships names one owning build".
- **Consequence:** Two specs build one view. The one-owner check reds, or two renderers diverge.
- **Fix:** Drop the two views from cl-0242, or have it say it consumes dTotalRecall's renders.
- **Skeptic:** confirmed medium. The class is a view built twice, not a gap owned twice: gap-mem-05 is dTotalRecall's alone. The walk record listed all three as units 4, 6 and 14 of one build before the split moved unit 14.

### Place 80: architecture-v2 · cl-dClosedLoop-0263 · worst medium

#### C3-F24 — The forced-name packs contradict the rule that namespaced closed sets apply by name
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0263
- **Class:** K10
- **Severity:** medium
- **Evidence:** lexicon [forced] item 1 (lines 245-253): "A namespaced closed set applies by name, and its rows carry a namespace pattern … (`pytest_*`, `__*__`)", with three outcome cases (unresolved base, in-repo parent, marker). cl-0263 applies all three pack kinds, host namespace included, "only where the site resolves statically through its imports to that base", and omits the three cases.
- **Consequence:** Module-level pytest hooks, and dunders on classes with no outside base, stay debt and are refused at commit under `lexicon.at-commit: refuse`, which leaves gap-lex-01 open.
- **Fix:** Split the rule in cl-0263: member and prefix rows resolve statically, and namespace closed sets apply by name. Add the three cases, each with its fixture.
- **Skeptic:** confirmed medium. cl-0265 covers marker verification only partly.

### Place 81: architecture-v2 · cl-dClosedLoop-0271 · worst medium

#### C3-F25 — The noun canon's source contradicts the amended design
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0271
- **Class:** K10
- **Severity:** medium
- **Evidence:** lexicon [drift] (lines 371-373), amended by the debt fold's `nouns-table` row: noun clusters are "written exogenously, such as `sha` against `oid` … The corpus decides only which clusters are live". cl-0271 reads "a noun canon seeded from the corpus and frozen", which is L-3's pre-fold offer wording (lexicon line 539).
- **Consequence:** A corpus-seeded canon makes today's variants canonical, the opposite of the fix.
- **Fix:** Reword cl-0271: clusters written exogenously, with liveness from the corpus.
- **Skeptic:** confirmed medium.

### Place 82: architecture-v2 · cl-dClosedLoop-0272 · worst medium

#### C3-F26 — `ratified` is retired without its readers by value
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0272
- **Class:** K10
- **Severity:** medium
- **Evidence:** lexicon [vocabulary] (lines 414-417) moves the drift signal, `adopt-lexicon.sh --check`, the kit's `lexicon-pins` hole and the scaffold to the record that replaces `ratified`, with the leg pack's arm seen red on a planted LANGS change newer than the record. The debt fold classes this `retirement-inventory-misses-readers-by-value`. `ratified` is read in `tools/lexicon/{adopt-lexicon.sh,kit.toml,lexicon.py,lexicon_conf.py,scaffold_lexicon.py,selftest.py}` and `tools/drift-audit/{drift_report.py,drift_signals.py}`. cl-0272 says only "with `ratified` replaced by its record".
- **Consequence:** The drift signal and the adopt check keep reading a dead field, and their signal silently stops moving.
- **Fix:** Name the readers in cl-0272, with the planted LANGS red.
- **Skeptic:** confirmed medium.

### Place 83: architecture-v2 · cl-dClosedLoop-0288 · worst medium

#### C4-F8 — Five of dWellOiledMachine's own runtime keys are read by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0288 (also cl-dClosedLoop-0279, cl-dClosedLoop-0284, cl-dClosedLoop-0295)
- **Class:** K4
- **Severity:** medium
- **Evidence:** The catalogue gives `runtime.spawn-backend`, `runtime.relaunch`, `runtime.hook-failure`, `runtime.attended-allowance` and `runtime.secret-scan` to dWellOiledMachine, and no clause names any of them. Stage 0's K4 lists all five, two guard-bearing. cl-0279's spike decides the backend, cl-0284 says "relaunch capped", cl-0288 writes "`onFailure` … on every entry", and cl-0295 builds "the secret value scan", none naming its key.
- **Consequence:** `hook-failure: open`, `relaunch: resume` and `secret-scan`'s `+shape-report` arm are dead values. The `coverage` fixture's "every `runtime.*` key … has a reader" goes red with no clause owning the read.
- **Fix:** Name `runtime.spawn-backend` in cl-0279, `runtime.relaunch` in cl-0284, `runtime.hook-failure` (both values) and `runtime.attended-allowance` in cl-0288, and `runtime.secret-scan` in cl-0295. Give each value an arm.
- **Skeptic:** confirmed medium, narrowed. Both `secret-scan` values include the value gate, so the arm left unbuilt is `+shape-report`, not `value-gate`. cl-0288's "as `runtime.attended-judge` says" implies the allowance read.

### Place 84: architecture-v2 · cl-dClosedLoop-0293 · worst medium

#### A2-F7 — The clock offset that corrects a holder's stamp has no declared reference, measurer or writer check
- **Address:** architecture-v2 [chain] dWellOiledMachine `cl-dClosedLoop-0293`; layer-runtime [enforce] "The node registry gains runtime facts"
- **Class:** K10
- **Severity:** medium
- **Scenario:** S2
- **What is wrong:** layer-runtime:837 lists "the clock offset" among the registry's runtime facts with no reference and no measurer. cloud-and-scale:211 joins the two expiry rules with "or", while the v2:1033 row joins them with "and". `cl-dClosedLoop-0293`'s plant only applies a supplied offset.
- **Consequence:** A skewed node cannot measure its own offset, and a self-reported one lets x's stamps look fresh for ever, denying take-over. Which expiry rule decides is undefined. The plant certifies nothing about how the offset is measured.
- **Fix:** Name the reference (for example the remote's push time read through the host API, or an NTP probe), the measuring command, and which rule wins. See it red on a node that misreports its own offset.
- **Skeptic:** Confirmed medium (batch 1).

### Place 85: architecture-v2 · cl-dClosedLoop-0296 · worst medium

#### C4-F13 — The event-wait sweep and the atomic landing rely on dShippedRelease items that no ancestor lands
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0296 (also cl-dClosedLoop-0337)
- **Class:** K6
- **Severity:** medium
- **Evidence:** cl-0296's sweep "raises a wait past `build.release-ceiling` once", and the catalogue defines that key as how long `deploy.released` waits for an exit record. cl-0337 carries "the build's release with its landed notice … in one atomic push". flow-steps gives `deploy.released`, `deploy.notify`, `deploy.unlease` and `deploy.close` to dShippedRelease, which comes after dWellOiledMachine, and Stage 0's K2 shows the lead UNCLASSED. No dWellOiledMachine clause names a stand-in, unlike flow-steps' [probe] stand-ins (lines 569-576).
- **Consequence:** The sweep and layer-runtime's `event-wait` and `lifecycle` fixtures cannot run when dWellOiledMachine lands, so their arms are never seen red or are built against items that do not exist yet.
- **Fix:** Have cl-0296 and cl-0337 name a stand-in release slot and notice, with the same contract and owned by this build, until dShippedRelease lands. Alternatively, move the fixtures' release arms to dShippedRelease.
- **Skeptic:** confirmed medium.

### Place 86: architecture-v2 · cl-dClosedLoop-0316 · worst medium

#### C4-F11 — The card's retirement re-points an incomplete list of readers
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0316
- **Class:** K10 (a retirement by value)
- **Severity:** medium
- **Evidence:** cl-0316 re-points the write gate, `readCard`, `extractRouteUnits`, the route notice and `manifest-check.sh --card --write`, "with `check-wiring.test.sh` and `format-guard.test.sh`". `grep -rn "orientation/"` also finds `skills/session-kickoff/manifest-check.test.sh` (14 lines, such as 861, asserting "the card is at <common-dir>/orientation/<sid>.md") and `tools/hooks/scratch-guard.test.sh:537,539,737`.
- **Consequence:** Those tests still assert the retired card path, so the unit lands red.
- **Fix:** Add `scratch-guard.test.sh` and `manifest-check.test.sh` to cl-0316's inventory, each re-pointed in the same unit.
- **Skeptic:** confirmed medium, narrowed. The two `orientation-*.fragment.json` files the walker also named hold no card path; they wire `manifest-check.sh --card --write`, which cl-0316 already names. The consequence is a red bar, not a silent pass.

### Place 87: architecture-v2 · cl-dClosedLoop-0324 · worst medium · includes an unverified finding

#### C4-F6 — The no-progress and repeat detectors arm as blocking with no false-positive measurement first
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0324
- **Class:** K10
- **Severity:** medium
- **Evidence:** stall-and-loop [owed] (line 414): "The no-progress and repeat detectors' false positives measured on gov's own run logs before either blocks (dWellOiledMachine)". cl-0324 builds both detectors as acting, with no measurement step and no journal-only stage.
- **Consequence:** An untested detector can mark healthy items stuck and route them, spending the build's rework budget, with no check that could show the error.
- **Fix:** Add to cl-0324 the replay over gov's recorded run logs, and keep the detectors journal-only until their false-positive rate is recorded.
- **Skeptic:** confirmed medium.

#### C4-F7 — Lease expiry by "tip unchanged" cannot fire while the fenced pushes keep moving the tip
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0324 (with cl-dClosedLoop-0284 and cl-dClosedLoop-0293)
- **Claim:** A looping holder that commits pushes a new lease beat at every pass, so its lease never expires.
- **Skeptic:** refuted. Under `build.push`'s default `every-pass`, a push and its lease beat (cl-0133) happen only at a pass commit, which is itself a witness. A holder looping without a witness makes no pass push, so its tip stays unchanged and the lease expires, as cl-0324's arm and layer-runtime's `renewal` fixture (line 1246) require. A holder whose commits are witnessed passes is making progress, so renewal there is intended.
- **Second skeptic:** Confirmed medium. cl-dClosedLoop-0133 makes every effect push carry a new lease beat, which moves the lease tip ("a re-push of an unchanged lease ref never counting as the fence"). `build.push` defaults to `every-pass`. cl-dClosedLoop-0135 and the `leases.expiry-hours` row judge expiry by "an observer seeing the tip unchanged". No clause separates a fence beat from a progress renewal. So layer-runtime:1246's `renewal` holder, "whose acts write commits … but never a witness", keeps moving the tip, and cl-dClosedLoop-0324's arm cannot go red under the observer rule.

### Place 88: architecture-v2 · cl-dClosedLoop-0325 · worst medium

#### C4-F5 — The session-limit hold hands the lease over without the owner item the settling records require
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0325
- **Class:** K10
- **Severity:** medium
- **Evidence:** cl-0325 releases "the build's lease as a hand-over at `runtime.hold-ceiling` so a node with quota takes the build over and the wake tick stops". Its red cases are "the lease still held or the tick firing again past the ceiling, a hand-over no second node takes". The catalogue's `runtime.hold-ceiling` row, layer-runtime [supervise] and layer-runtime [tests] `limits` all say an owner item is raised.
- **Consequence:** When no node with quota exists, which is the "hand-over no second node takes" case, the build sits released and nobody is told.
- **Fix:** Add "and raises an owner item" to cl-0325, with a red arm on a ceiling passed and no owner item.
- **Skeptic:** confirmed medium.

### Place 89: architecture-v2 · cl-dClosedLoop-0344 · worst medium

#### C4-F9 — Three remote-verdict gaps and their keys sit on dWitnessedBar with no clause to build them
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0344 (also cl-dClosedLoop-0342, cl-dClosedLoop-0347, cl-dClosedLoop-0352)
- **Class:** K4
- **Severity:** medium
- **Evidence:** dWitnessedBar owns gap-test-11 ("A remote verdict certifies itself"), gap-test-12 and gap-test-13, and the catalogue gives it `verdict`, `verdict.remote.trust`, `verdict.remote.pin`, `verdict.remote.pin-scope`, `tests.product` and `retrofit.widen`. layer-expansions lets a remote verdict stand as a witness "only when … the pinned files at `head_sha` equal the pin". None of cl-0339 to cl-0368 names a verdict-backend registry, a remote pin, the held-CI reader's adapter, `tests.product` or `retrofit.widen`.
- **Consequence:** A remote verdict can be built with no source check, so once `verdict: remote-ci` is selected a pusher's workflow edit certifies itself. `tests.product` and `retrofit.widen` have no reader, and gap-test-12 and gap-test-13 close with nothing built.
- **Fix:** Add a dWitnessedBar clause for the verdict-backend registry under `verdict` and the remote verdict's source check under `verdict.remote.*`, seen red on a swapped workflow. Name the held-CI reader's adapter registration. Name `tests.product` in cl-0347 and `retrofit.widen` in cl-0352.
- **Skeptic:** confirmed medium.

### Place 90: architecture-v2 · cl-dClosedLoop-0346 · worst medium

#### C4-F10 — No clause builds the runner's same-tree re-run, so a flaky leg never reaches `test.flakes`
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0346
- **Class:** K2
- **Severity:** medium
- **Evidence:** flow-steps [test] (line 296) has `test.route` "re-runs each red leg once on the same tree", and line 304 calls that a runner mode dWitnessedBar owes (gap-test-04); today the bar retries only timeouts. cl-0346 says only "flake quarantine", and cl-0368 re-runs only CONTENDED reds on a quiet host.
- **Consequence:** `test.route` cannot tell a nondeterministic red from a real one. Flaky reds route to `test.attribute` as OWN reds, and the quarantine never receives a leg.
- **Fix:** Add to cl-0346 "the runner's mode re-running a red leg once on the same tree under `test.verdict`'s env, seen on a fixture leg that reds then greens reaching `test.flakes`".
- **Skeptic:** confirmed medium.

### Place 91: architecture-v2 · cl-dClosedLoop-0362 · worst medium

#### C4-F12 — The portability pack moves in a "shell-hygiene mode" that `encoding_posture.py` does not have
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0362
- **Class:** K6
- **Severity:** medium
- **Evidence:** cl-0362: "the last moved in from gate-lint's `encoding_posture.py` with its shell-hygiene mode". `encoding_posture.py` has no shell mode; its only modes are text and binary. `tools/gate-legs.json` runs `gate-lint/sh_hygiene.py` as its own script, with three legs plus a selftest. research-compatibility §4 puts P-launch's legs in the shell-hygiene spawn-idioms and loop legs.
- **Consequence:** A builder either looks for a mode that does not exist or leaves `sh_hygiene.py` in gate-lint.
- **Fix:** Read "moved in from gate-lint's `encoding_posture.py`, with `sh_hygiene.py`'s legs beside it".
- **Skeptic:** confirmed medium, narrowed. cl-0362 also names a bare-shell-name arm, so P-launch is not left without a core leg.

### Place 158: architecture-v2 · cl-dClosedLoop-0166 · worst low

#### C3-F29 — The deployer's registration omits distribution's contract
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0166
- **Class:** K10
- **Severity:** low
- **Evidence:** layer-roles [roster] (lr:462, 466) and flow-steps [consequences] ("it registers under both") register the deployer under distribution and integrations: release notes for distribution, verify judgment for integrations. cl-0166 registers it only "through the integrations and observability layer contracts".
- **Consequence:** The release-notes item has a role its expansion never registers, so P28's no-expansion-role-in-core arm may red on it.
- **Fix:** Add distribution's contract to cl-0166.
- **Skeptic:** confirmed low.

### Place 159: architecture-v2 · cl-dClosedLoop-0238 · worst low

#### CS3-F1 — The decision routing's below-kappa outcome is not carried, and the record's re-run loop has no bound
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0238
- **Class:** K10 (a loop with no end, P39)
- **Severity:** low
- **Evidence:** cl-0238 has "today's 200 rows routed by two raters at kappa 0.8 or better", with no outcome below the bar. layer-memory [decisions] (lines 678-682): "Below kappa 0.8 the rubric is revised and the routing re-run, and no row moves until it passes", with no cap. Its debt-fold row `kappa-below-threshold` (line 1193) is the fix the clause leaves out.
- **Consequence:** A spec carrying cl-0238 has no route below the bar. The record's route is revise-and-re-run until the bar passes, which P39 forbids, so the major-decision log can stay unrouted indefinitely.
- **Fix:** Carry the below-kappa route in cl-0238, with a bound: a set number of rubric revisions, then an owner item.
- **Skeptic:** raised by skeptic batch 3 on re-walking cl-0238, which walker 3 had passed as holding. No second skeptic judged it.

### Place 160: architecture-v2 · cl-dClosedLoop-0244 · worst low

#### C3-F22 — `annotations.resolve-scope` and `annotations.lookup` are not named
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0244
- **Class:** K4
- **Severity:** low
- **Evidence:** v2 gives both keys to dLinkedLibrary (systems:363, 365): `annotations.resolve-scope` (notes, every-comment-ref) and `annotations.lookup` (query-and-map, query, map-index). No clause names either; cl-0244 carries AN-1's default behaviour in prose only. Stage 0's K4 lists both as unread.
- **Consequence:** `notes` and `map-index` never route.
- **Fix:** Name both keys in cl-0241 and cl-0244.
- **Skeptic:** confirmed low.

### Place 161: architecture-v2 · cl-dClosedLoop-0254 · worst low

#### C3-F31 — The span rule's owed re-measure is not carried
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0254
- **Class:** K10
- **Severity:** low
- **Evidence:** v2 [owed]: "the span share re-measured with the map's own extractors: the hybrid loses if 80% or more of a feature's outside spans sit in a derivable definition (point 4)". No clause carries "span share" or "80%", and cl-0254 builds the span rule with no losing test.
- **Consequence:** The hybrid span rule is built with no test that could reject it.
- **Fix:** Add the re-measure and its 80% bound to cl-0254.
- **Skeptic:** confirmed low.

### Place 162: architecture-v2 · cl-dClosedLoop-0262 · worst low

#### C3-F27 — The "one pin over three seams" rule is carried by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0262
- **Class:** K10
- **Severity:** low
- **Evidence:** lexicon [classes] (lines 223-234): "`VERB_OFFENDER_PIN` becomes the debt pin. `SUFFIX_OFFENDER_PIN` folds into it … The per-cell `PINS:` block retires", and "Two cells re-arm. `py.file` and `py.constant`". cl-0262 names only "the shrink-only pin", and cl-0276 only "records kept out by the path selector". `tools/lexicon/lexicon.py:121` still holds both pins in `PIN_KEYS`.
- **Consequence:** The suffix pin and the per-cell pins survive as separate waivers beside the debt pin.
- **Fix:** Carry the fold, the `PINS:` retirement and the two cells' re-arming in cl-0262 and cl-0276.
- **Skeptic:** confirmed low.
