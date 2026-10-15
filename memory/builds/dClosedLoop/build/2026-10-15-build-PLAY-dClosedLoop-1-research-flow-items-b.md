# Research: the flow layer's items, Test, Deploy, Maintain, the stage review and the Loop Review

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 21's return, verbatim. Its question is in
`prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-2-researcher.md`, and its use is in
`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md`, under `[audit]`.

---

I couldn't give every item a clean pass: across Test, Deploy, Maintain and both reviews there are 39 findings. Five are about the driver (P25): two where it judges or reasons, and three record disagreements. Three are core items that depend on an expansion with no core fallback (P28). Six are witnesses an agent types itself (P2/P23).

Three of them stand out:
1. The stage-exit recommendation has the driver doing the reasoning (F-X1).
2. Maintain's patch intakes are written by an agent, and with `patch.ratify: auto` that intake becomes the mandate (F-M2).
3. Deploy's landing review "blocks" but runs after the push (F-D4).

All of this is read-only. The one current-code claim I checked is that `GATE_ATTRIBUTE` labels reds OWN, INHERITED, MIXED, CONTENDED or DEAD PROBE and is report-only (`tools/run-gates/run-gates.sh:19-21`). That agrees with research-test:22.

**Sources**, under `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\`:
- **flow.md**, `2026-10-14-build-PLAY-dClosedLoop-1-flow.md`: `[test]` :441-475, `[deploy]` :511-548, `[maintain]` :583-628, `[review]` :644-712.
- **flow-roles**, `2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md`: `[cycle]` :16-32, `[steps]` :82-118.
- **roles**, `2026-10-14-build-PLAY-dClosedLoop-1-roles.md`: `[map]` :162-239, roster :390-412.
- **v2**, `2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`: `[layers]` :121-158, `[principles]` :160-270, `[policies]` :305-402.
- **instr**, `2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md`: `[layers]` kit map :205-226, `[recommendations]` :332-459.
- **coord**, `2026-10-14-build-PLAY-dClosedLoop-1-coordination.md`: `[design]` :76-121.
- **AGENTS.md**, `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\AGENTS.md`, cited for practice lines.

**Conventions in the tables:**
- **Layers:** core is I instruction, F flow, R roles, M memory, RT runtime. Expansions are K knowledge, O observability, X integrations, D distribution. Policy values are I, the level-2 policy values (v2 `[front-door]` ladder).
- **Instruction scope** follows R-C (instr :362-372): policy keys, then practice reach, then views. No practice declares a per-stage reach yet; the catalogue is dOrderedCharter's (v2 `[chain]` :570). So every practice listed is **UNVERIFIED**, a candidate taken from today's charter line.
- **Views** are R-E slices (instr :388-393) of today's whole guides under `memory/guides/`. The tester, deployer and maintainer have no agent file yet: roles roster status is "new" (roles :151-153), and `memory/guides/` holds none.

## 1. Tables

### Test
The whole step runs once per build per tree, and again when the tip moves (flow.md:467-470).

| tag | actor | witness | inputs by layer | instruction scope | routes | fan-out, depends on | flags |
|---|---|---|---|---|---|---|---|
| `test.prepared-merge` | command | Not stated. Proposed: the merge commit SHA and tree hash in Test's worktree | M: Build-to-Test transition, range. RT: worktree. I: `verdict.tree` | `verdict.tree` · [reconcile] AGENTS.md:33, [isolate] :30 · MERGE-BAR (tree) | fixed → `test.selection`; a conflict has no route at this item | once per tree · `build.transition` | F-T5, F-T10 |
| `test.selection` | command | Not stated. Proposed: a selection record of the legs the range claims plus the declared levels | M: range. F: leg manifest, product-test declarations. I: policies | `tests.landing-levels`, `tests.product`, `verdict.held` · [bar] :27, [cost] :28 · MERGE-BAR (selection) | → `test.verdict`; who demands a held leg is unstated | once · prepared-merge | F-T6, F-T10 |
| `test.verdict` | command (the bar, through the hook) | The hook-written verdict per tree hash (flow.md:449; walkthrough :257-258) | F: selection, the engine. RT: hook, backend. X: remote-CI slot | `verdict`, `verdict.blocks`, `verdict.held`, `hooks.bypass` · [bar], [gate] :24, [verify] · MERGE-BAR | green → items 5-6; red → `test.red-attribution`; stale → `test.prepared-merge` | once per tree, each leg inside · selection | — |
| `test.red-attribution` | tester | The tester's return, typed by the actor itself | F: verdict and its labels. M: diff, specs. K: bug classes not stated (UNVERIFIED) | `verdict.red-route`, `verdict.blocks` · [class], [verify], [signal] :48 · tester return template | code misses spec → builder fix pass; spec wrong → new unit at Design; inherited → ask; merge conflict → builder or architect (flow-roles :87) | per red · verdict | F-T3, F-T4, F-T10 |
| `test.flakes` | command | Not stated. Proposed: a flake record from the bar's retry, plus a quarantine entry (store UNVERIFIED) | F: verdict runs. O lists "gate health and flakes" | `verdict.flakes` · [gate] | past the threshold → quarantine and an ask (walkthrough :265-266) | per flaky leg · verdict | F-T8, F-T10 |
| `test.seen-red` | command | A seen-red record per gate added or changed (flow.md:448) | M: range. F: leg manifest, bar records | none · [gate] | missing: no route | per gate · verdict | F-T7 |
| `test.review` | command scores; driver reasons; review roles (gate lens) when owed | Not stated | F: verdict, gates. M: past findings | `review.test`, `review.test.effort`, `review.recommendation`, `review.recommendation.source`, `review.blocks`, `review.findings` · [risk] :40, [bound] :41 · REVIEW-PROTOCOL, gate lens | findings "disposed as in Build" (flow-roles :89) | once · items 4-6 | F-T1, F-X1, F-T10 |
| `test.transition` | command | A transition record over the witnesses of items 1-7 (flow.md:450) | M: witnesses, mailbox (coord :106-107) | `transitions.record`, `mailbox.reads`, `card.follows` · [records] :37 | → Deploy; refused → the failing item; backward steps recorded (flow-roles :272-273) | once · items 1-7 | F-T9 |

### Deploy
The landing runs once per build. Under the default `build.closes: at-landing`, items 6 and 7 move to a release record kept per SHA (flow.md:546-548).

| tag | actor | witness | inputs by layer | instruction scope | routes | fan-out, depends on | flags |
|---|---|---|---|---|---|---|---|
| `deploy.verdict-current` | command | Not stated. Proposed: the verdict's tree equals the prepared merge on the current tip | M: Test transition. F: verdict | `verdict.tree` · [bar] | current → item 2; stale → Test (flow-roles :96) | once · `test.transition` | F-D12 |
| `deploy.authorize` | command | Not stated. Proposed: under `request`, the hook-written intake (flow-roles :186-191). session-model :189 says "the ratification trailer", which predates FR-1 | M: intake log. I: `autonomy` | `autonomy`, `plan.ratification` · [land] :31 · UNATTENDED-PROTOCOL (mandate) | no route when unauthorized | once · item 1 | F-D6, F-D12 |
| `deploy.land` | command (lander, turnstile) | Not stated. Proposed: the pushed `--no-ff` merge plus the reused pre-push verdict | F: lander. RT: turnstile, hook. M: leases (order) | `landing.order`, `deps.landing`, `hooks.bypass`, `verdict` · [land], [post-merge] :32 · UNATTENDED-VERBS (land) | moved tip → Test; the parent-hold and the core re-check are not items | once, serialized per node · item 2 | F-D5, F-D12 |
| `deploy.landing-record` | command | The landing record: SHA, builds, units, verdict (flow.md:516) | M: git, verdict | `transitions.record` · [records], [derive] :20 | none | once · item 3 | — |
| `deploy.kit-versions` | command mints; deployer writes notes | Versions: not stated. Notes: typed by the deployer. flow.md:517 says "generated" | M: landed units' records. D: kit descriptors | `release.cadence` · [contract] :19 · deployer return template | none | per kit moved · item 4 | F-D1, F-D7, F-D9, F-D12 |
| `deploy.promote` | command; deployer "where a verify needs judgment" | Not stated. Proposed: a verify record per environment per SHA | engine (layer unassigned) | `deploy.runs`, `deploy.promotion` · [verify] | none (flow-roles :98) | per environment in promotion order · item 3 | F-D1, F-D2, F-D10, F-D11, F-D12 |
| `deploy.verify-fail` | command; deployer records the disposition (roles :215) | The deployer's record of a policy action | O/engine verify output | `deploy.on-verify-fail` | roll forward plus an ask; after close → Plan's triage (flow.md:628) | per failed verify · item 6 | F-D1, F-D8, F-D11 |
| `deploy.review` | roles :216: command and driver plus review roles. flow-roles :99: review roles only | Not stated | M: landing record | `review.deploy` (and its effort), `review.recommendation*`, `review.blocks`, `review.findings` · [risk], [bound] · REVIEW-PROTOCOL, landing lens | "—" (flow-roles :99) | once · item 4 | F-D1, F-X1, F-D3, F-D4, F-D12 |
| `deploy.lease-release` | command | Not stated. Proposed: lease refs deleted on the remote (coord :83-88) | M/F: lease refs | `leases*` | none | per build and per unit · item 8 | F-D12 |
| `deploy.transition` | command | Items 1-9 (flow.md:522) | M: witnesses, mailbox | `build.closes`, `card.snapshot`, `transitions.record` | the build closes; `landed` posted to dependents; terminal card committed (flow-roles :100) | once · items 1-9 | F-D5 |

### Maintain
Runs once per cadence period or per event (`maintain.events`, flow.md:614-616).

| tag | actor | witness | inputs by layer | instruction scope | routes | fan-out, depends on | flags |
|---|---|---|---|---|---|---|---|
| `maintain.lease` | command | The lease ref `refs/gov/leases/run/maintain/<period>` (coord :78) | M/F: leases | `maintain.host`, `maintain.cadence`, `maintain.events`, `leases*` | lease held elsewhere → skip (session-model :208-209, not in flow.md) | once · cadence tick or event | F-M6, F-M8 |
| `maintain.detect` | command | Not stated. Proposed: one reading per registered detector against its pin and owner | Core: dormant builds, leases and mailbox (M/F); process census (RT, instr :221); gate health and flakes (F verdict records). Expansion: drift-audit and runlog (O); map freshness (K); branch-reconcile (RT expansion, instr :222); adopter currency and outbox (D) | `maintain.events`, `maintain.on-breach` · [derive], [signal] · HYGIENE | a failed detector has no route | per detector · item 1 | F-M3, F-M8, F-M10 |
| `maintain.cadence-tests` | command runs; tester attributes | Not stated | F: the bar on the tip, the levels left out of the landing set, held legs | `tests.landing-levels`, `verdict.held` · [bar], [cost] | → Plan's triage (flow-roles :107) | per red · item 1 | F-M7, F-M10 |
| `maintain.safe-fix` | command (untracked fixes); maintainer (patch intakes) | Not stated. Intakes are typed by the maintainer | M/F: readings; I: `maintain.fixes` | `maintain.fixes`, `patch.ratify` · [small] :29 · UNATTENDED-ASKS | each tracked fix → a patch build at Design | per reading with a fix · item 2 | F-M1, F-M2, F-M7, F-M9, F-M10, F-M11 |
| `maintain.file-breach` | maintainer | Not stated. Filings are typed by the maintainer | M/F/O: readings | `maintain.on-breach` · [signal] · maintainer template, HYGIENE (ids) | → Plan's triage | per breach · item 2 | F-M10 |
| `maintain.release-cut` | command cuts; deployer writes notes | Not stated | D: kit versions, notes | `release.cadence` · [contract] | none | once, when due · item 2 | F-M4, F-M7, F-M10 |
| `maintain.currency` | command | Not stated | D: fleet register, adopter receipts | `deploy.currency` | none | per adopter · item 1 | F-M4, F-M10 |
| `maintain.record` | command | The maintenance record (flow.md:592); store UNVERIFIED | M: items 1-7. O: metrics handed on | `transitions.record` · [records] | metrics → Loop Review | once · items 2-7 | F-M5 |
| `maintain.lease-release` | command | Not stated (lease ref released) | M/F | `leases*` | none | once · item 8 | — |

### Stage review
Runs at a stage's exit when the trigger holds (flow.md:660-661).

| tag | actor | witness | inputs by layer | instruction scope | routes | fan-out, depends on | flags |
|---|---|---|---|---|---|---|---|
| `review.stage-trigger` | command | A trigger record citing the policy value, the recommendation record or the hook-written owner intake | I: `review.<stage>`, `review.recommendation`. M: intake | `review.<stage>`, `review.recommendation`, `review.blocks` | not triggered → the stage advances | once · the stage's recommendation item | F-X1 (inherited) |
| `review.stage-pin` | command | The pinned revision SHAs (flow.md:670) | M | `review.build.when` | none | once · item 1 | — |
| `review.stage-lens` | reviewer | Not stated. Findings are a typed return | M: artifact. K: bug classes (UNVERIFIED) | `review.<stage>.effort` · [risk], [bound] · REVIEW-PROTOCOL, lens view, reviewer template | → skeptic | per lens, within the fan-out bound · item 2 | F-R10 |
| `review.stage-refute` | skeptic | Not stated | M: findings | [verify] · skeptic template | confirmed or refuted; unverified "stays outstanding", with no route | per finding · item 3 | F-R3, F-R10 |
| `review.stage-report` | synthesizer | The report under the build's `reviews/` (flow.md:673) | M | [signal] · synthesizer template | none | once · item 4 | F-R4 |
| `review.stage-dispose` | command by policy; spec writer for new units | Not stated | M: report. K: bug-class catalogue | `review.findings`, `review.left-shift`, `review.follow-up` · [left-shift] :26, [class] | owning stage (new units, asks); a gate earned has no route | per confirmed finding · item 5 | F-R1, F-R2, F-R9, F-R10 |
| `review.stage-cost` | command | Not stated | O: value ledger | `budgets.*` · [cost] | none | once · item 5 | F-R5, F-R10 |

### Loop Review
Runs once per `review.loop.cadence`.

| tag | actor | witness | inputs by layer | instruction scope | routes | fan-out, depends on | flags |
|---|---|---|---|---|---|---|---|
| `review.loop-lease` | command | `refs/gov/leases/run/review/<period>` (coord :78) | M/F | `review.loop.cadence`, `leases*` | held elsewhere: not stated | once · cadence | F-M8 (same shape) |
| `review.loop-metrics` | command | "gathered from the records, never typed" (flow.md:679) | M: transitions, review yield, plan revisions. O: gate cost, flakes, ledger, bypasses | `review.loop.window-days`, `budgets.*` · [derive] | none | once · item 1 | F-R5 |
| `review.loop-propose` | roles :237 says loop reviewer; roster :407, :411-412 and flow-roles :118 say reviewer, skeptic, synthesizer | Not stated | M/O: metrics | `review.loop.retire` · REVIEW-PROTOCOL, loop lens | → item 4 | per proposal · item 2 | F-R6, F-R10 |
| `review.loop-file` | command; owner as `review.loop.retire` says | Owner's ratification witness: not stated | M: proposals | `review.loop.retire` | → Plan | per proposal · item 3 | F-R1, F-R7 |
| `review.loop-record` | command | The Loop Review record (flow.md:682) | M | [records] | none | once · item 4 | F-R4 |

## 2. Extension points per step

- **Test**:
  - verdict backend: `peer-node`, or `remote-ci` (X, P3's designed slot, v2:168-169)
  - leg packs: gate-lint and pytest-parallel-guardrails (instr :216)
  - product-test runner adapters (`tests.product`; layer UNVERIFIED)
  - the bug-class slot in the tester's work order (UNVERIFIED; v2 :572 names only the builder's and the scout's slots)
  - gate health and flake signals to O
- **Deploy**:
  - the deploy engine and its adapters, starting with incms (layer unassigned)
  - optional emitted CI (X, v2 :577)
  - `notify.owner` beyond the turn (X)
  - `run.host` set to `cloud-routine` (X)
  - kit versions and release notes (D)
- **Maintain**:
  - detector slots: O (drift-audit, runlog), K (map freshness), D (currency, outbox), and RT expansion (branch-reconcile)
  - hosts set to `os-scheduler` or `cloud-routine` (X)
  - the release cut (D)
  - the metrics handoff (O)
- **Review**:
  - lens slots per stage
  - the value ledger (O)
  - the bug-class catalogue for left-shift (K)
  - instruction effectiveness, R-J (O, instr :447-450)
  - Loop metrics beyond memory (O)

## 3. Findings

**Shared across steps**
- **F-X1** (P25, `driver.reads: state-reads-only`): the driver reasons out the stage-exit recommendation. Evidence: flow.md:709-712 ("the agent records the score with its reasoning"), flow-roles :56 ("driver reasons") and :89, roles :207, :216, :377-379. This hits `test.review` and `deploy.review`, and `review.stage-trigger` inherits it. Fix: the command renders the reason from the signals that fired. The owner should confirm that reading of FL-R3.

**Test**
- **F-T1** (P24, one actor per item, v2:223-225): item 7 has three actors (flow-roles :89). Fix: split it into `test.recommendation` (command) and `test.gate-review` (review roles).
- **F-T3** (P2, P23): the tester's agent-typed class decides whether a red goes to a fix pass or to Design (flow-roles :87; v2:220-221). Fix: the witness becomes a computed join. Every red leg in the hook-written verdict has one disposition, and the artifact each disposition routes to exists.
- **F-T4** (closed outcome set, flow-roles `[cycle]` :30-32): the routes cover four classes (flow-roles :87). The bar's labels include MIXED, CONTENDED and DEAD PROBE (run-gates.sh:19-21), and none of those has a route. Fix: declare an enum in which those three route to asks.
- **F-T5** (no failure route): a merge conflict arises at item 1, but its route sits on item 4, whose input is a verdict that does not exist yet. Fix: give `test.prepared-merge` the outcomes {fixed, conflict}, with conflict routing to the tester.
- **F-T6** (P24): who demands a held leg under `verdict.held: on-demand` is unstated (flow.md:427-428; session-model :176). Fix: on-demand means a recorded request; with none, the leg is skipped and the skip recorded.
- **F-T7** (no failure route): a missing seen-red record has no route (flow-roles :88). Fix: outcome `missing` sends a builder fix pass to the unit that added the gate.
- **F-T8** (P28): flakes and gate health are listed under O (v2:136; instr :169), yet the core item 5 quarantines them, which changes what blocks. Fix: make the flake record a flow record kind that O reads.
- **F-T9** (P24): the lease's verified tree is the input to landing order (coord :80-81, :174-175), but no Test item writes it. Fix: declare it as an effect of `test.transition`, witnessed by the lease ref's history.
- **F-T10** (witness not stated): items 1, 2, 4, 5 and 7. Fix: name the witnesses proposed in the table.

**Deploy**
- **F-D1** (P24): items 5, 6, 7 and 8 each have two actors (roles :213-216). Fix: split each into one item per actor.
- **F-D2** (P25): it is unstated who decides that "a verify needs judgment" (flow-roles :98). Fix: verify outcomes {pass, fail, inconclusive}, with inconclusive routing to the deployer by table.
- **F-D3** (records disagree): the item 8 actor differs between roles :216 and flow-roles :99, and flow-roles gives no route. Fix: align flow-roles with roles and add the `review.findings` route.
- **F-D4** (`review.blocks` versus order): every review blocks (flow.md:701-703), but item 8 reviews the landing record after item 3 has already pushed. Fix: state that the review blocks `deploy.transition` (the close), and that findings enter through the post-close row of the entry-point table (flow.md:628).
- **F-D5** (P24): four settled behaviours have no item:
  - the parent-landing hold (flow-roles :236-237);
  - the turnstile (flow-roles :233-235);
  - the K1 core re-check on the landed tree (v2:108-111, :577);
  - the `landed` notice and the terminal card snapshot (flow-roles :100).

  Fix: add `deploy.parent-landed` before `deploy.land`, and `deploy.core-recheck` after it. A core red there stops the build closing; where it routes next is UNVERIFIED. Declare the notice and the snapshot as witnessed effects of `deploy.transition`.
- **F-D6** (no failure route; records disagree): under `three-gates` or `every-stage`, landing needs the owner's authorization (v2:563), and nothing says where the item goes without it. session-model :189 also conflicts with FR-1. Fix: an `awaiting-owner` outcome routed to `notify.owner`.
- **F-D7** (P23): notes are "generated" (flow.md:517) but written by the deployer (roles :213). Fix: the witness is one notes entry per minted version, computed; the note text is evidence.
- **F-D8** (P2): the disposition is a policy value, yet the deployer records it (roles :215). Fix: the command records it, and the deployer acts only on `inconclusive`.
- **F-D9** (P28): minting kit versions is Distribution (v2:138; instr :225). Fix: put it at a D extension point, witnessed `not-applicable` when no kit moved.
- **F-D10** (layer unassigned): the deploy engine appears in no layer row (instr :205-226). Fix: add its row. It comes after landing, so the sorting test (v2:124-126) places it outside the core.
- **F-D11** (no lifecycle): under `at-landing`, the release record has no start, lease or end (flow.md:546-548). Fix: give it its own items, with a run lease per SHA on the lease grammar (coord :76-78).
- **F-D12** (witness not stated): items 1, 2, 3, 5, 6, 8 and 9.

**Maintain**
- **F-M1** (the record contradicts itself): item 4 says "applied, verified and landed" (flow.md:588), while the settlement routes tracked fixes to patch builds (flow.md:610-613). Fix: reword item 4 to the settled split.
- **F-M2** (P2, P23): the maintainer's intake becomes the mandate under `patch.ratify: auto` (roles :222; flow.md:625-626). An owner's intake, by contrast, is hook-written (flow-roles :186-191). Fix: the command renders the intake from the keyed detector reading and its `maintain.fixes` entry.
- **F-M3** (P28): "every detector runs" (flow.md:586) mixes core and expansion detectors. Fix: a detector register with each detector's layer, a fixed core set, and expansion detectors attached at a declared point. The witness is a reading from every registered detector.
- **F-M4** (P28): items 6 and 7 are Distribution only. Fix: an extension point, with `not-applicable` when D is absent.
- **F-M5** (no-tracked-content rule, flow.md:612-613): where the maintenance record is stored is unstated (UNVERIFIED). Fix: declare its store as a ref or an untracked file.
- **F-M6** (lease key): event runs have no lease key (coord :78; flow.md:614-616). Fix: key the lease `.../maintain/<period>/<event>`.
- **F-M7** (P24): items 3, 4 and 6 each have two actors. Fix: split them.
- **F-M8** (no failure route): a lease held elsewhere and a failed detector both lack a route. The skip appears only in session-model :208. Fix: declare outcomes for both. The same applies to `review.loop-lease`.
- **F-M9** (one fact in one place, [default] :50): item 4's "anything else is filed" duplicates item 5. Fix: drop the clause.
- **F-M10** (witness not stated): items 2 to 7.
- **F-M11** (the declared set): pruning a closed build's mailbox ref (coord :110) is missing from the `maintain.fixes` default (v2:387), so it fails the contract witness "fixes inside the declared set" (v2:564). Fix: add it to the default.

**Review**
- **F-R1** (P24): stage item 6 and loop item 4 each have two actors. Fix: split them.
- **F-R2** (P23, P28): counting a class's second occurrence needs class identity. A "command" is assigned to judge it (roles :233), and the catalogue it would read is K (v2:135). Fix: the reviewer's return carries a class tag from a registered core set, and the command counts by tag. The K catalogue becomes an optional slot.
- **F-R3** (no failure route): "unverified stays outstanding" (flow.md:672) does not say whether it blocks. Fix: route it to an ask and declare whether it blocks.
- **F-R4** (no home): reports go "under the build's reviews", but a Maintain review and the Loop Review have no build. Fix: declare a home for each.
- **F-R5** (P28): the ledger and the Loop metrics need O (v2:136; instr :165-171). Fix: the core keeps cost in the report and takes its metrics from M, with O as a slot.
- **F-R6** (records disagree; missing item): roles :237 names the "loop reviewer", whom the roster folds into the reviewer (:334, :411-412). The Loop checklist also has no refutation item, though flow-roles :118 has the skeptic act. Fix: update the map row and add `review.loop-refute`.
- **F-R7** (P2): the owner's retirement ratification has no witness (v2:400). Fix: witness it as `plan.ratification` says.
- **F-R9** (no failure route): a class that earns a gate (flow.md:704-707) has no route. Fix: outcome `gate-earned` routes to a patch-build intake (flow.md:625).
- **F-R10** (witness not stated): stage items 3, 4, 6 and 7; loop items 3 and 4.

**One sorting question for the owner** (P28, v2:124-126): the core test is "request to landing", so it cannot classify anything that runs after landing. That covers the release record, all of Maintain and the Loop Review. Smallest fix: record which reading holds, either core shells with expansion bodies or something else. The owner has to confirm this one.
