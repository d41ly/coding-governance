# Walk return: run C, walker 5, dRankedPlan to dConvergedCharter

**Serves:** research PLAY-dClosedLoop-1

Dispatch 189's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-30-spec-reviewer.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

The chain shipped and failed because one of these clauses names a path, a field or a guard without carrying the rule that settles it. The receipt never gains the release it was installed from, so the currency watch cannot count. The dead-paths gate is folded into an observability detector that is scoped to memory. The playbook gate is retired along with the unattended kit, and nothing relocates it first.

### C5-F1 — The receipt never gains the release tag and source remote that the currency watch reads
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0435
- **Class:** K6, c2
- **Severity:** high
- **Evidence:**
  - layer-expansions [design-distribution], record kinds: "`receipt` (`.governance/install.json`, schema 4: per-kit versions, the release tag, the source remote …)".
  - layer-expansions, `install.from`: "the receipt then names one release, so 'releases behind' is defined".
  - `kits.currency` "joins the receipt's rows to gov's remote tag list: releases behind".
  - The fates row for govkit: "receipt names its release".
  - The schema numbers then moved (folds-reviews-compared `receipt-steps-later`). dSafePassage's cl-0020 makes schema 4 "gaining `steps`". cl-0435 makes schema 5 "gaining `superseded`, `deprecations` and `prior_commit`".
  - No clause carries the release or source fields. `grep -n "gov_source\|install.from\|release tag" rp.txt ss.txt tc.txt others.txt` matched no clause.
  - In code, `tools/govkit/govkit.py:8020` still writes `"gov_source": str(root)`, and `RECEIPT_SCHEMA = 3` (line 49).
- **Consequence:**
  - gap-deploy-12, which dShippedRelease owns, is closed by no unit.
  - cl-0417's currency watch and `kits.currency` have no installed release to count from, so "releases behind" is undefined.
  - In S4 (an adopter two releases behind), the currency record can only read unverified, and `currency.on-behind` never fires.
- **Fix:** Add `release` and `source_remote` to cl-0435's schema-5 field list. Name `kits.currency` as their reader, with a planted receipt that has no release tag seen red.

### C5-F2 — The "memory's dead pointers" detector absorbs a gate whose population is shipped text outside `memory/`
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0448
- **Class:** K10, c3
- **Severity:** high
- **Evidence:**
  - cl-0448: "a detector for the memory's dead pointers, owned by Maintain, absorbing `check-dead-paths.sh` and keeping its merge-bar leg".
  - The script's header (`tools/check-dead-paths.sh:2`): "nothing outside `memory/`, and no map dossier or gotcha page, may name a file this repo DELETED".
  - Its leg in `tools/gate-legs.json`: "dead-path carriers (deleted files still named)", subject `repo`.
  - The other population in the clause is gap-orient-10's: "12 of the 98 paths the auto-memory names no longer exist".
  - layer-expansions [design-observability]: "A signal that decides a position is a core witness … change-caused witnesses … leave drift-audit for gate legs … each owned by the layer whose records it grades".
- **Consequence:**
  - A builder following the clause's wording builds an auto-memory pointer reading and drops the shipped-text population. The kept "merge-bar leg" then certifies a check it no longer runs.
  - Because the leg now sits in observability's pack, every install without observability silently loses the dead-path gate.
- **Fix:**
  - Name both populations: shipped text, dossiers and gotchas from the old gate, plus the auto-memory pointers.
  - Keep the shipped-text leg as a core leg owned by the layer whose records it grades. Only the auto-memory reading moves to Maintain.
  - Plant a deleted-file name in a kit README and see it red on a core-only tree.

### C5-F3 — A post-landing core red "stops that build from closing", but the settled route closes it through the post-close row
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0423
- **Class:** K2
- **Severity:** medium
- **Evidence:**
  - cl-0423: "so a core red the landing merge introduced stops that build from closing (foundations K1)".
  - layer-flow [settled]: "the entry-point table's post-close row, which now covers a landing-review finding and a post-landing core red, each entering as a patch build".
  - flow-steps [deploy] `deploy.core`: "red → a patch build through the entry-point table's post-close row, and the close waits for its filing".
  - `grep -n "close waits"` finds only flow-steps:369.
- **Consequence:** A lander built from the clause holds the build open, with its leases and mailbox, until the red is fixed. A Deploy step built from flow-steps closes it once the patch build is filed. The S6 landing route has two incompatible terminals.
- **Fix:** Reword cl-0423: "… a core red the landing merge introduced files a patch build through the post-close row before the build closes". Plant a red landed tree whose close happens without that filing and see it red.

### C5-F4 — The playbook gate lives in the kit that convergence deletes, and no clause moves it out first
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0486 (and cl-dClosedLoop-0392)
- **Class:** K10
- **Severity:** medium
- **Evidence:**
  - cl-0392 makes "`check-playbook` as Design's pack".
  - cl-0486 retires the unattended kit, with "the gate legs that reference the kit … each re-pointed or retired with it".
  - In `tools/gate-legs.json`, the leg "playbook validity gate" has argv `['bash', '{prefix}/unattended/check-playbook.sh']`. The probe was a python scan of the legs for `unattended/`.
  - The script itself is `tools/unattended/check-playbook.sh`. `--record-piece` and `--record-set` live in `tools/unattended/unattended.sh:29-30`.
  - The fates row reads: "playbook mode (`--record-piece`, `--record-set`, `check-playbook`) … RESHAPED … Design's pack (dIndexedDesign)".
- **Consequence:** Under cl-0486's "re-pointed or retired", a builder may retire the playbook gate as a leg of the retired kit. The script then disappears with `tools/unattended/`, and gap-flow-17's recipe half is lost.
- **Fix:**
  - cl-0392 moves `check-playbook.sh` and the piece and set recorders to the loop kit's home in its own unit, with their readers re-pointed.
  - cl-0486 names that leg as re-pointed, never retired, and runs it on the scratch clone with `tools/unattended/` removed.

### C5-F5 — Build drains only "in hunks" and always claims, so `retrofit.drain`'s file and off and `retrofit.claim-on-touch`'s carry and off have no build, and velocity selects `carry`
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0406
- **Class:** K9
- **Severity:** medium
- **Evidence:**
  - cl-0406: "draining the legacy a unit touches, in hunks under `retrofit.drain-cap`, and claiming the baselined map keys".
  - v2 [policies]: `retrofit.drain` takes hunk, file, off; `retrofit.claim-on-touch` takes claim, carry, off. Both are owned by dScopedBuild.
  - v2 [presets] line 1571: `retrofit.claim-on-touch | carry | claim | claim | claim`, so velocity sets carry.
  - retrofit [drain]: "Under `retrofit.drain: file` … owes every baselined site in each touched file … Under `off`, nothing is owed".
  - Stage 0's leads K4: "retrofit.drain … retrofit.claim-on-touch: read by no chain clause and no item (guard-bearing)".
- **Consequence:** A velocity repository still claims and drains, contradicting its preset. The `file` and `off` values validate in the schema and do nothing.
- **Fix:** cl-0406 reads both keys and builds each value's arm, with each value seen on a planted unit.

### C5-F6 — Caps, the rework budget and deadlines are "re-derived" with no route through the owner, though raising a loop bound is a loosening
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0461, cl-dClosedLoop-0473 and cl-dClosedLoop-0474
- **Class:** K10
- **Severity:** medium
- **Evidence:**
  - cl-0461: "caps re-derived from evidence and review cost". cl-0473: "the rework budget, the deadlines and the thresholds re-derived from that evidence once 30 builds have run".
  - P9: "A cap's value is the owner's".
  - v2 `flow.rework-budget`: "raising it is a loosening, the owner's alone".
  - stall-and-loop item 11: "Observability trends, never decides". Item 8: "raising any loop bound … is a loosening: under `flow.adapt` it waits for the owner".
  - layer-expansions `loop.propose` "re-derives the caps", and `loop.file` routes to "the owner's breakpoint, as `review.loop.retire` says".
  - Contrast cl-0463: "through the guarded policy command, the owner's own setting for a role winning".
- **Consequence:** A builder can apply re-derived values directly. That loosens a loop bound unattended, or overwrites an owner's cap. dDeclaredLoop's static check would then refuse the Loop Review's own write.
- **Fix:** Each of these clauses files its re-derived value as a `loop.file` proposal through the guarded policy command, the owner's setting winning and a raise waiting for the owner. Plant a re-derivation that writes the policy directly and see it red.

### C5-F7 — The Loop Review is fixed at "weekly", and `budgets.*` is read by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0460 (and cl-dClosedLoop-0461)
- **Class:** K4
- **Severity:** medium
- **Evidence:**
  - cl-0460: "the weekly Loop Review".
  - v2 [policies]: `review.loop.cadence | weekly, monthly, every-n-landings | weekly | walk R1 | dCalibratedLens`.
  - layer-expansions: "The Loop Review, a cadence program keyed by ISO week".
  - Stage 0's leads K4: "review.loop.cadence: read by no chain clause and no item" and "budgets.*: read by no chain clause and no item".
- **Consequence:** The monthly and every-n-landings values pass the schema and run weekly. The cap-value keys that cl-0461 re-derives have no reader clause.
- **Fix:**
  - cl-0460 reads `review.loop.cadence`, keys the lease by the selected period, and sees each value on a planted case.
  - cl-0461 names `budgets.*` as what it re-derives.

### C5-F8 — Maintain's build delivers the Loop Review, a program its descendant dCalibratedLens owns
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0449
- **Class:** K7
- **Severity:** medium
- **Evidence:**
  - cl-0449 (dTendedCadence): "Maintain and the Loop Review delivered as cadence steps of the observability expansion".
  - layer-expansions: the items `loop.lease` to `loop.record` are owned by dCalibratedLens. cl-0460 builds "the weekly Loop Review".
  - The map gives `record-kind.loop-review` to dCalibratedLens, whose parents are dTendedCadence and dFairHearing.
- **Consequence:** When dTendedCadence is specced and landed, the Loop Review's items and record kind do not exist yet. Its cadence step registers a program with no items, and two builds' clauses carry the Loop Review's registration.
- **Fix:** cl-0449 registers Maintain's cadence step only, and dCalibratedLens's cl-0460 registers the Loop Review's step. Alternatively, cl-0449 names its "not installed" stand-in until dCalibratedLens lands.

### C5-F9 — Maintain's host, cadence, events, reading admission and run record are built by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0443, cl-dClosedLoop-0445 and cl-dClosedLoop-0447
- **Class:** K4
- **Severity:** medium
- **Evidence:**
  - Stage 0's leads K4: `maintain.host`, `maintain.cadence`, `maintain.events` (guard-bearing), `maintain.reading-admission` (guard-bearing) and `observability.run-record` (guard-bearing) are all "read by no chain clause and no item".
  - Stage 0's leads K3: "run-record: no writer item … no reader".
  - layer-expansions: "A reading with no derivable owner, or no pin, is refused at registration. Under `maintain.reading-admission: report-unowned` it is admitted". Also: "Observability's journal reader writes a run's record … as `observability.run-record` says".
  - The `release-verify-failed` event reads the release slot's exit record (`release-exit`, dShippedRelease's). dShippedRelease is not an ancestor of dTendedCadence.
  - The clauses say only "the cadence, on Runtime's hosts", "detectors with owners" and "the maintenance record".
- **Consequence:**
  - The admission guard's refuse and report arms, the run record (gap-maint-14) and the event subset are unbuilt or unspecified.
  - The default `maintain.events` names an event whose producer kind lands in a non-ancestor, with no stand-in.
- **Fix:**
  - cl-0443 reads `maintain.host`, `maintain.cadence` and `maintain.events`, with `release-verify-failed` rendering "not installed" until dShippedRelease lands.
  - cl-0445 builds both admission values.
  - cl-0447 adds the run record under `observability.run-record`.
  - Each is seen on a planted case.

### C5-F10 — Three gaps Maintain owns are closed by no clause
- **Address:** architecture-v2 [chain] dTendedCadence row, Gaps owned (cl-dClosedLoop-0445)
- **Class:** K8
- **Severity:** medium
- **Evidence:**
  - gap-maint-09: "Five become core legs" (ledger_rows, non_terminal_specs, closed_specs, handkept, cutoff_keys_armed).
  - gap-maint-10: a reading varies with its tree, which `maintain.reading-tree` answers.
  - gap-maint-11: "The remote-CI drift signal is dead".
  - `grep "ledger_rows\|non_terminal_specs\|handkept\|cutoff_keys_armed\|reading-tree\|remote-CI drift"` over all chain clauses matches only cl-0277, the lexicon's two signals.
- **Consequence:**
  - The five drift signals stay report-only in drift-audit, and the merge bar keeps reaching them through an optional kit.
  - The tree-variance and dead-probe gaps close in name only.
- **Fix:** Add a dTendedCadence clause carrying all three: the five legs moved to their owning layers' packs, readings taken under `maintain.reading-tree`, and the dead remote-CI signal fixed or retired. Alternatively, move gap-maint-09 to the builds that own those legs.

### C5-F11 — The landing queue has no ordering rule, and six Deploy and distribution keys are read by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0422 (and cl-dClosedLoop-0417, cl-dClosedLoop-0437)
- **Class:** K4
- **Severity:** medium
- **Evidence:**
  - cl-0422: "landings ordered through the landing queue it builds (`gap-flow-08`)".
  - P21: "landings go in plan priority, then first verified".
  - v2: `landing.order | plan-priority-then-first-verified, first-verified, owner-orders`.
  - Stage 0's leads K4 list `landing.order`, `deploy.runs`, `deploy.currency`, `kits.cadence`, `kits.host`, `kits.watch-cadence` and `commits.squash` as "read by no chain clause and no item".
  - cl-0437 builds `commits.squash`'s values without naming the key.
- **Consequence:**
  - P21's ordering half has no enforcing clause, and `owner-orders` is unbuilt.
  - The distribution cadence and host keys that `kits.currency` runs on have no clause reading them.
- **Fix:**
  - cl-0422 orders the queue "as `landing.order` says", with each value planted.
  - cl-0417 reads `kits.watch-cadence`, `kits.host` and `deploy.currency`.
  - cl-0437 names `commits.squash`.

### C5-F12 — The derived runbook and release notes have no losing test, and the runbook is rebuilt again at convergence
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0419 (and cl-dClosedLoop-0414, cl-dClosedLoop-0489)
- **Class:** K10
- **Severity:** medium
- **Evidence:**
  - cl-0419: "a derived runbook". cl-0414: "kit release notes".
  - final-questions [help]: "the derived runbook and release notes have no losing test".
  - research-final-help: "dShippedRelease (#18) | A losing test for the derived runbook and release notes". This is not among final-questions [folded].
  - cl-0489 (dConvergedCharter) migrates "the agent runbook … its reference half generated … its how-to half written".
- **Consequence:** Two builds derive the same document under different rules, and the first derivation's acceptance cannot fail.
- **Fix:**
  - cl-0419 states its render-parity red on a hand-edited runbook section, and cl-0414 a red on notes missing a landing.
  - cl-0489 either cites cl-0419's derivation, or cl-0419 moves to cl-0489.

### C5-F13 — gap-flow-04's closure spans two builds that do not descend from each other, and gap-flow-03 has no closing clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0382 (dRankedPlan, Gaps owned)
- **Class:** K8
- **Severity:** medium
- **Evidence:**
  - gap-flow-04: "no recorded plan revision and no re-design inventory of completed work".
  - The inventory kind is dIndexedDesign's (map `record-kind.inventory — owner=dIndexedDesign`; ownership-population P15, "refuted: owner dIndexedDesign"), and `design.inventory` is dIndexedDesign's item.
  - The gap register's rule: "a gap whose closers do not descend one from the other is split, one key per build".
  - dIndexedDesign's parents do not include dRankedPlan, and dRankedPlan's do not include dIndexedDesign.
  - cl-0382 only names "a plan revision". No clause builds the plan-revision record. gap-flow-03 (card, plan and brief levels) is matched by no clause.
- **Consequence:**
  - The gap join reads dRankedPlan as closing a gap whose inventory half lands elsewhere.
  - No unit builds the plan-revision record, and the three-times-written plan stays.
- **Fix:**
  - Split gap-flow-04 into a dRankedPlan key (the plan-revision record, built by a clause) and a dIndexedDesign key (the inventory).
  - Add a dRankedPlan clause that declares the card, plan and brief levels, for gap-flow-03.

### C5-F14 — Plan Review and the landing review run before or beside the build that supplies their lenses
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0374 and cl-dClosedLoop-0424 (with cl-dClosedLoop-0458)
- **Class:** K7
- **Severity:** medium
- **Evidence:**
  - cl-0374 (dRankedPlan): "Plan Review". cl-0424 (dShippedRelease): "the landing review blocking the build's close".
  - cl-0458 (dCalibratedLens): "lenses for Plan, Test, Deploy and Maintain".
  - gap-review-01 ("Plan, Test, Deploy and Maintain have none") is dCalibratedLens's. gap-plan-04 is dRankedPlan's, and gap-deploy-06 is dShippedRelease's.
  - dCalibratedLens descends from dRankedPlan. dShippedRelease and dCalibratedLens do not descend from each other.
- **Consequence:**
  - From dRankedPlan's landing until dCalibratedLens's, the Plan breakpoint has no lens, and no stand-in is named.
  - The landing review's gap and its lens's gap are owned by two builds that do not descend from each other, which the gap register's split rule forbids.
- **Fix:**
  - cl-0374 and cl-0424 each name their stand-in lens from dFairHearing's catalogue until dCalibratedLens lands.
  - Re-key gap-plan-04 and gap-deploy-06 to the build that completes them, or split them.

### C5-F15 — The deviation and coverage gaps are owned by the bootstrap build, not the build whose gate closes them
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0412 (and cl-dClosedLoop-0398)
- **Class:** K8
- **Severity:** low
- **Evidence:**
  - gap-build-07: "A deviation is recorded but never gated", owned by dTrueNorth (final-questions [gaps]). gap-design-13 is likewise dTrueNorth's.
  - The gap register's rule (the folds' closing review, 2026-10-19): "owned by the one whose landing completes the closure, which descends from the other".
  - The gate is cl-0412 (dScopedBuild) and the Design exit read is cl-0398 (dIndexedDesign). Both descend from dTrueNorth.
- **Consequence:** The gap join reads "never gated" as closed when dTrueNorth lands, before any gate exists.
- **Fix:** Move gap-build-07 to dScopedBuild and gap-design-13 to dIndexedDesign, or split each gap into the instrument key and the gate key.

### C5-F16 — The Design hand-off and overlap keys are read by no clause, so the overlap refusal is unbuilt
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0383 and cl-dClosedLoop-0384
- **Class:** K4
- **Severity:** medium
- **Evidence:**
  - v2: `design.handoff | derived-ready, ready-plus-audit, status-and-tier` and `design.overlap | warn, refuse, index-only`, both dIndexedDesign's.
  - flow-steps [design] lists both among Design's policies.
  - Stage 0's leads K4: "design.handoff: read by no chain clause"; "design.overlap … (guard-bearing)".
  - The clauses say only "the derived-READY hand-off" and "the design index".
- **Consequence:** The `refuse` value of a guard-bearing key passes the schema and only warns. `ready-plus-audit` is never built.
- **Fix:** cl-0383 reads `design.handoff` and cl-0384 reads `design.overlap`, with each value seen on a planted overlapping roster.

### C5-F17 — The reuse check's re-entries omit the rework budget and the non-converging end that flow-steps settled
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0410
- **Class:** K2
- **Severity:** medium
- **Evidence:**
  - cl-0410: "re-entries bounded by `flow.route-backs`".
  - flow-steps [build] `build.reuse-check`: "re-entries past `flow.route-backs` → that item's loop ends non-converging and its open rows go to asks, each re-entry drawing on `flow.rework-budget` (revised 2026-10-19 by the owner's SL-1 and SL-2)".
- **Consequence:** A reuse-check loop built from the clause neither draws on the build's budget nor files its open rows as asks, which breaks P39's single budget per build.
- **Fix:** Append to cl-0410: "each re-entry drawing on `flow.rework-budget`, and past `flow.route-backs` ending non-converging with its open rows filed as asks". Seen on a planted fourth re-entry.

### C5-F18 — When the closing review runs is a dScopedBuild key no clause reads
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0402
- **Class:** K4
- **Severity:** low
- **Evidence:**
  - v2: `review.build.when | per-build, per-unit, per-landing | per-build | walk B3 | dScopedBuild`.
  - Stage 0's leads K4: "review.build.when: read by no chain clause and no item".
  - cl-0402: "the closing review recorded".
- **Consequence:** Per-unit and per-landing pass the schema and run per build.
- **Fix:** cl-0402: "the closing review recorded, run as `review.build.when` says", with each value planted.

### C5-F19 — Plan's triage, kickoff and authority keys are built only at their defaults
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0371, cl-dClosedLoop-0375 and cl-dClosedLoop-0370
- **Class:** K4
- **Severity:** low
- **Evidence:**
  - v2: `plan.triage | owner-batches, rules, archive-legacy`; `plan.kickoff | offer-next, binding, advisory`; `plan.authority | planner-drafts-owner-ratifies, planner-within-themes, owner-orders`.
  - Stage 0's leads K4 lists all three as unread.
  - The clauses read "rule-based triage" and "kickoff offering the next item".
- **Consequence:** The other values are accepted by the schema and never take effect.
- **Fix:** Name each key in its clause, with each value's arm planted.

### C5-F20 — "Runs neither … both" in cl-0430 has no antecedent inside the clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0430
- **Class:** K1
- **Severity:** low
- **Evidence:** cl-0430: "an update `kits.offer` offers runs neither in the adopter's tree, and its outbox order names the adopter's own run of both". The referent, `adopt` and `test.seed`, is in cl-0427.
- **Consequence:** A spec carrying cl-0430 whole cannot tell which runs are withheld, and the carries join pins this text.
- **Fix:** Reword: "… runs neither `adopt` nor `test.seed` in the adopter's tree, and its outbox order names the adopter's own run of each".

### C5-F21 — Convergence folds the house file over the owner's earlier rulings on the same values
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0495 (against cl-dClosedLoop-0438)
- **Class:** K10
- **Severity:** medium
- **Evidence:**
  - cl-0438 (dShippedRelease): "the house file's efforts as `roles.effort.*` values … proposed as overlay rows for the owner to rule once".
  - cl-0495: "a repository's efforts folded into the `roles.effort.*` policy keys … with an upgrade step".
  - P8: "an update never overwrites or silently drops a repository's change".
- **Consequence:** An owner who declined a proposed effort at install has it written into the policy file by convergence's upgrade step, which overrides the ruling (P8 and P38).
- **Fix:** cl-0495's step folds only values with no ruling from cl-0438, and reads a declined row as a drop. Plant a declined proposal and see it survive the fold.

### C5-F22 — The fates join's population leaves out rows the table holds
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0488
- **Class:** K10
- **Severity:** low
- **Evidence:**
  - cl-0488's population is "`git ls-files` across `tools`, `skills`, `.githooks`, `.claude`, `.github`, `help`, the runbook and the template".
  - The fates table has a `guides` row ("hand-written guides | RETIRED", under `memory/guides/`) and the unattended row "`.unattended.conf` extension vocabularies", whose file is at the repository root.
- **Consequence:** A guide or a root kit conf that remains after convergence is outside the exit check.
- **Fix:** Derive the population from every fates row's path glob, plus the listed directories, and plant a surviving `memory/guides/` file to see it red.

### C5-F23 — `design.streams` names both an item and a key, and the planner item's Needs loops onto itself
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0397
- **Class:** K1
- **Severity:** low
- **Evidence:**
  - Stage 0's leads K1: "design.streams: a cycle among Needs: design.streams > design.streams".
  - flow-steps' Needs cell: "`design.overlaps`, where `design.streams` holds".
  - The precedent: layer-expansions renamed "the key `maintain.record` to `maintain.record-when` … so the item `maintain.record` keeps its name".
- **Consequence:** The needs graph and the tag index cannot tell the item from the key.
- **Fix:** Rename the key, for example `design.streams-when`, in v2 [policies], flow-steps and cl-0397.

| clause | build | read against | verdict |
|---|---|---|---|
| cl-dClosedLoop-0369 | dRankedPlan | gap-plan-01; flow-steps [plan] `plan.place` | holds |
| cl-dClosedLoop-0370 | dRankedPlan | v2 [policies] plan.*; ownership.md key rows; cl-0166 roster | C5-F19 |
| cl-dClosedLoop-0371 | dRankedPlan | gap-plan-02, gap-plan-06; flow-steps `plan.triage-rule`; v2 `plan.triage` | C5-F19 |
| cl-dClosedLoop-0372 | dRankedPlan | gap-plan-05; v2 `maintain.fixes` | holds |
| cl-dClosedLoop-0373 | dRankedPlan | v2 [chain] live-build note | holds |
| cl-dClosedLoop-0374 | dRankedPlan | gap-plan-04, gap-review-01; flow-steps [plan] breakpoints; cl-0458 | C5-F14 |
| cl-dClosedLoop-0375 | dRankedPlan | gap-plan-07; v2 `plan.kickoff` | C5-F19 |
| cl-dClosedLoop-0376 | dRankedPlan | v2 `kickoff.runs`; fates skills rows; cl-0490 | holds |
| cl-dClosedLoop-0377 | dRankedPlan | flow-steps [entry] `entry.intake`; recut H2 and RC-9; cl-0282, cl-0283 | holds |
| cl-dClosedLoop-0378 | dRankedPlan | audit-fold H1; recut tolerance row; cl-0123; cl-0283 | holds |
| cl-dClosedLoop-0379 | dRankedPlan | v2 `memory.item-budget`; walk [wave-2] | holds |
| cl-dClosedLoop-0380 | dRankedPlan | night-pass point 2; flow-steps `plan.record` | holds |
| cl-dClosedLoop-0381 | dRankedPlan | gap-plan-08; night-pass point 6 | holds |
| cl-dClosedLoop-0382 | dRankedPlan | gap-flow-03, gap-flow-04; gap-register split rule; ownership-population P15 | C5-F13 |
| cl-dClosedLoop-0383 | dIndexedDesign | gap-design-04; flow-steps `design.ready`; v2 `design.handoff` | C5-F16 |
| cl-dClosedLoop-0384 | dIndexedDesign | gap-design-02; flow-steps `design.overlaps`; v2 `design.overlap` | C5-F16 |
| cl-dClosedLoop-0385 | dIndexedDesign | gap-design-03; audit-fold [af-1]; flow-steps [design] breakpoints | holds |
| cl-dClosedLoop-0386 | dIndexedDesign | gap-design-05, gap-design-06 | holds |
| cl-dClosedLoop-0387 | dIndexedDesign | gap-design-07; walk WK-2 | holds |
| cl-dClosedLoop-0388 | dIndexedDesign | gap-design-09 | holds |
| cl-dClosedLoop-0389 | dIndexedDesign | P12; [enforcement] | holds |
| cl-dClosedLoop-0390 | dIndexedDesign | gap-flow-01; P17, P18; v2 `design.reentry`, `design.forks` | holds |
| cl-dClosedLoop-0391 | dIndexedDesign | gap-design-10; P12 | holds |
| cl-dClosedLoop-0392 | dIndexedDesign | gap-flow-17; fates unattended row; gate-legs.json "playbook validity gate" | C5-F4 |
| cl-dClosedLoop-0393 | dIndexedDesign | Stage 0's leads K3 playbook-set; dWitnessedBar ancestry | holds |
| cl-dClosedLoop-0394 | dIndexedDesign | night-pass point 4; P12 | holds |
| cl-dClosedLoop-0395 | dIndexedDesign | gap-design-11; night-pass-two [p2] item 2; scoutedseam-apply §5c | holds |
| cl-dClosedLoop-0396 | dIndexedDesign | night-pass-two NT-26 | holds |
| cl-dClosedLoop-0397 | dIndexedDesign | gap-design-12; v2 `design.streams`; flow-steps `design.streams`; parked-debt values-no-arm; Stage 0's leads K1 | C5-F23 |
| cl-dClosedLoop-0398 | dIndexedDesign | final-questions [gaps], [folded]; v2 `design.coverage*`; gap-register rule | C5-F15 |
| cl-dClosedLoop-0399 | dScopedBuild | gap-spine-03; flow-steps [build] exits | holds |
| cl-dClosedLoop-0400 | dScopedBuild | P19; gap-flow-05; v2 `review.findings` (dDeclaredLoop) | holds |
| cl-dClosedLoop-0401 | dScopedBuild | gap-build-01; flow-steps `build.scope` | holds |
| cl-dClosedLoop-0402 | dScopedBuild | gap-build-02; v2 `review.build.when` | C5-F18 |
| cl-dClosedLoop-0403 | dScopedBuild | gap-build-03; cl-0172 | holds |
| cl-dClosedLoop-0404 | dScopedBuild | gap-build-04; night-pass-two NT-24; checklist-unowned fold | holds |
| cl-dClosedLoop-0405 | dScopedBuild | flow-steps `build.core` | holds |
| cl-dClosedLoop-0406 | dScopedBuild | gap-build-05; retrofit [drain]; v2 [presets] line 1571 | C5-F5 |
| cl-dClosedLoop-0407 | dScopedBuild | retrofit [drain]; recut H5; cl-0049; map_lib.py:1373 | holds |
| cl-dClosedLoop-0408 | dScopedBuild | P31; night-pass point 2 | holds |
| cl-dClosedLoop-0409 | dScopedBuild | fates playbook-mode row; gap-flow-17 | holds |
| cl-dClosedLoop-0410 | dScopedBuild | gap-build-06; flow-steps `build.reuse-check`; v2 `flow.rework-budget` | C5-F17 |
| cl-dClosedLoop-0411 | dScopedBuild | gap-flow-22; scoutedseam-apply §6 rank 2 | holds |
| cl-dClosedLoop-0412 | dScopedBuild | final-questions [gaps]; v2 `deviation.gate`; gap-register rule | C5-F15 |
| cl-dClosedLoop-0413 | dShippedRelease | flow-steps `deploy.record` | holds |
| cl-dClosedLoop-0414 | dShippedRelease | final-questions [help]; research-final-help #18 | C5-F12 |
| cl-dClosedLoop-0415 | dShippedRelease | flow-steps `deploy.unlease`; P40; parked-debt release-deletes-lease | holds |
| cl-dClosedLoop-0416 | dShippedRelease | walk WK-8 | holds |
| cl-dClosedLoop-0417 | dShippedRelease | gap-deploy-04; layer-expansions `kits.currency`; v2 `kits.*` | C5-F11 |
| cl-dClosedLoop-0418 | dShippedRelease | gap-deploy-03 | holds |
| cl-dClosedLoop-0419 | dShippedRelease | gap-deploy-08; final-questions [help]; cl-0489 | C5-F12 |
| cl-dClosedLoop-0420 | dShippedRelease | gap-tool-07; foundations K3 | holds |
| cl-dClosedLoop-0421 | dShippedRelease | P21; flow-steps `deploy.parents`; v2 `deps.landing` | holds |
| cl-dClosedLoop-0422 | dShippedRelease | P21; gap-flow-08; v2 `landing.order`; stall-and-loop [layers] | C5-F11 |
| cl-dClosedLoop-0423 | dShippedRelease | foundations K1; layer-flow [settled]; flow-steps `deploy.core` | C5-F3 |
| cl-dClosedLoop-0424 | dShippedRelease | gap-deploy-06; layer-flow [settled]; cl-0458 | C5-F14 |
| cl-dClosedLoop-0425 | dShippedRelease | gap-deploy-01; flow-steps [deploy] extension points | holds |
| cl-dClosedLoop-0426 | dShippedRelease | gap-deploy-13; layer-expansions distribution | holds |
| cl-dClosedLoop-0427 | dShippedRelease | gap-deploy-27; retrofit [owners]; adopter-instructions | holds |
| cl-dClosedLoop-0428 | dShippedRelease | P8; folds-reviews self-update-unplaced | holds |
| cl-dClosedLoop-0429 | dShippedRelease | retrofit [practices] CI row | holds |
| cl-dClosedLoop-0430 | dShippedRelease | cl-0427; cl-0426 | C5-F20 |
| cl-dClosedLoop-0431 | dShippedRelease | audit-fold M16; FM10; code consumers of `*/kit.toml` | holds |
| cl-dClosedLoop-0432 | dShippedRelease | v2 `integrations.tracker` | holds |
| cl-dClosedLoop-0433 | dShippedRelease | cl-0166; recut decided rows | holds |
| cl-dClosedLoop-0434 | dShippedRelease | gap-deploy-14; v2 `install.guards` | holds |
| cl-dClosedLoop-0435 | dShippedRelease | gap-deploy-12; layer-expansions receipt row, `install.from`; cl-0020; govkit.py:49, 8020 | C5-F1 |
| cl-dClosedLoop-0436 | dShippedRelease | gap-tool-11; v2 `platforms.*`; run-held-wsl.sh exists | holds |
| cl-dClosedLoop-0437 | dShippedRelease | gap-deploy-21, 22, 23; v2 `commits.squash`; memory-plan | C5-F11 |
| cl-dClosedLoop-0438 | dShippedRelease | flow-adoption FA-1; effort-default-homeless fold | holds |
| cl-dClosedLoop-0439 | dShippedRelease | gap-deploy-28; widening-unchecked fold | holds |
| cl-dClosedLoop-0440 | dShippedRelease | stall-and-loop [chain]; flow-steps `deploy.released`; keep-waiting fold | holds |
| cl-dClosedLoop-0441 | dShippedRelease | gap-deploy-29; cloud-and-scale | holds |
| cl-dClosedLoop-0442 | dTendedCadence | P6; layer-expansions Maintain | holds |
| cl-dClosedLoop-0443 | dTendedCadence | gap-maint-01; v2 `maintain.host`, `maintain.cadence`, `maintain.events` | C5-F9 |
| cl-dClosedLoop-0444 | dTendedCadence | v2 `maintain.fixes`; P6 | holds |
| cl-dClosedLoop-0445 | dTendedCadence | gap-maint-02, 09, 10, 11; layer-expansions admission rule | C5-F9, C5-F10 |
| cl-dClosedLoop-0446 | dTendedCadence | gap-maint-06 | holds |
| cl-dClosedLoop-0447 | dTendedCadence | v2 `maintain.record-when`, `observability.run-record`; gap-maint-14 | C5-F9 |
| cl-dClosedLoop-0448 | dTendedCadence | gap-orient-10; fates check-dead-paths row; tools/check-dead-paths.sh:2; layer-expansions line rule | C5-F2 |
| cl-dClosedLoop-0449 | dTendedCadence | layer-expansions Loop Review owners; map record-kind.loop-review | C5-F8 |
| cl-dClosedLoop-0450 | dTendedCadence | retrofit [cadence], [never]; v2 `retrofit.cadence` | holds |
| cl-dClosedLoop-0451 | dTendedCadence | cl-0166; recut | holds |
| cl-dClosedLoop-0452 | dTendedCadence | flow-steps [entry] repeat; cl-0305 | holds |
| cl-dClosedLoop-0453 | dTendedCadence | night-pass point 4 | holds |
| cl-dClosedLoop-0454 | dTendedCadence | gap-maint-12; v2 `maintain.security-review` | holds |
| cl-dClosedLoop-0455 | dTendedCadence | gap-maint-13; v2 `maintain.tiers` | holds |
| cl-dClosedLoop-0456 | dTendedCadence | P35; shape-reviews legacy-populations | holds |
| cl-dClosedLoop-0457 | dTendedCadence | gap-maint-15; v2 `maintain.interpreter-eol` | holds |
| cl-dClosedLoop-0458 | dCalibratedLens | gap-review-01; audit-fold [af-1]; v2 `review.<stage>.effort` | C5-F14 |
| cl-dClosedLoop-0459 | dCalibratedLens | P9; layer-expansions `loop.price` | holds |
| cl-dClosedLoop-0460 | dCalibratedLens | gap-review-02; v2 `review.loop.cadence`; layer-expansions ISO week | C5-F7 |
| cl-dClosedLoop-0461 | dCalibratedLens | P9; v2 `budgets.*`; layer-expansions `loop.propose` | C5-F6, C5-F7 |
| cl-dClosedLoop-0462 | dCalibratedLens | gap-found-16; P11 | holds |
| cl-dClosedLoop-0463 | dCalibratedLens | v2 `memory.item-budget` | holds |
| cl-dClosedLoop-0464 | dCalibratedLens | gap-review-11; audit-fold `review.cost` | holds |
| cl-dClosedLoop-0465 | dCalibratedLens | project-map losing test (15 points, 38 findings); cl-0228 | holds |
| cl-dClosedLoop-0466 | dCalibratedLens | night-pass points 2 and 5 | holds |
| cl-dClosedLoop-0467 | dCalibratedLens | gap-review-14; shape-reviews replay-scorers | holds |
| cl-dClosedLoop-0468 | dCalibratedLens | gap-review-15, gap-review-16 | holds |
| cl-dClosedLoop-0469 | dCalibratedLens | P35; away-pass point 5 | holds |
| cl-dClosedLoop-0470 | dCalibratedLens | gap-review-17; flow-adoption folds fixed-set, joins, policy-names | holds |
| cl-dClosedLoop-0471 | dCalibratedLens | gap-review-18; v2 `flow.promote`; decline-unrecorded fold | holds |
| cl-dClosedLoop-0472 | dCalibratedLens | gap-review-19; P9 | holds |
| cl-dClosedLoop-0473 | dCalibratedLens | P39, P9; stall-and-loop items 8 and 11; v2 `flow.rework-budget` | C5-F6 |
| cl-dClosedLoop-0474 | dCalibratedLens | P40, P9; cloud-and-scale | C5-F6 |
| cl-dClosedLoop-0475 | dConvergedCharter | gap-found-12 | holds |
| cl-dClosedLoop-0476 | dConvergedCharter | P11 | holds |
| cl-dClosedLoop-0477 | dConvergedCharter | gap-maint-04 | holds |
| cl-dClosedLoop-0478 | dConvergedCharter | gap-tool-05; fates RETIRED rows | holds |
| cl-dClosedLoop-0479 | dConvergedCharter | gap-spine-04; P8 | holds |
| cl-dClosedLoop-0480 | dConvergedCharter | P16; shape-reviews kind-factory-dup; cl-0212 | holds |
| cl-dClosedLoop-0481 | dConvergedCharter | gap-found-36; v2 `help.explanation`; final-questions FQ-6 | holds |
| cl-dClosedLoop-0482 | dConvergedCharter | fates top-level rows | holds |
| cl-dClosedLoop-0483 | dConvergedCharter | gap-found-13, gap-found-28; fates skills row; SKILL.template.md census | holds |
| cl-dClosedLoop-0484 | dConvergedCharter | gap-found-12 | holds |
| cl-dClosedLoop-0485 | dConvergedCharter | audit-fold H5 and M6; v2 [policies]; four `read_policy_key` copies in code; roles_lib.py:363 | holds |
| cl-dClosedLoop-0486 | dConvergedCharter | gap-tool-08; fates unattended rows; gate-legs.json unattended legs | C5-F4 |
| cl-dClosedLoop-0487 | dConvergedCharter | night-pass point 4 | holds |
| cl-dClosedLoop-0488 | dConvergedCharter | gap-tool-09; fates [table] kits; fates check limits | C5-F22 |
| cl-dClosedLoop-0489 | dConvergedCharter | P42; final-questions [help]; cl-0419 | C5-F12 |
| cl-dClosedLoop-0490 | dConvergedCharter | gap-orient-21; shape-reviews SA-9 | holds |
| cl-dClosedLoop-0491 | dConvergedCharter | shape-reviews SK-1 | holds |
| cl-dClosedLoop-0492 | dConvergedCharter | memory-plan [cycle]; shape-reviews cycle-walk | holds |
| cl-dClosedLoop-0493 | dConvergedCharter | P34, P37; memory-plan guides row | holds |
| cl-dClosedLoop-0494 | dConvergedCharter | P38 | holds |
| cl-dClosedLoop-0495 | dConvergedCharter | gap-roles-26; P8; cl-0438; flow-adoption folds | C5-F21 |
| cl-dClosedLoop-0496 | dConvergedCharter | gap-found-32; fates `.unattended.conf` row | holds |

| dRankedPlan | C5-F13, C5-F14, C5-F19 |
|---|---|
| dIndexedDesign | C5-F4, C5-F15, C5-F16, C5-F23 |
| dScopedBuild | C5-F5, C5-F15, C5-F17, C5-F18 |
| dShippedRelease | C5-F1, C5-F3, C5-F11, C5-F12, C5-F14, C5-F20 |
| dTendedCadence | C5-F2, C5-F8, C5-F9, C5-F10 |
| dCalibratedLens | C5-F6, C5-F7, C5-F14 |
| dConvergedCharter | C5-F4, C5-F12, C5-F21, C5-F22 |

**Read outside the list above:** none. I wrote one helper script, `split.py`, and its outputs to `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/walk-c5/`, and nothing to the repository.

One defect in the instruments: Stage 0's K4 arm reads a key as unread when a clause builds its values without naming the key, as cl-0437 does for `commits.squash`. That arm overcounts, and it does not separate a key whose clause fixes it at its default value.
