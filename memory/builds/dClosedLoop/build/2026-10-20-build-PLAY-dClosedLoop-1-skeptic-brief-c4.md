# Skeptic brief: run C, batch 4

**Serves:** research PLAY-dClosedLoop-1

**Your task is to refute each finding below, and then to break each clean cell after them.** This brief is your
instructions, not the subject of your review: do not review it, the audit's seal or its instruments. A defect you see
in them goes in one line at the end of your return, and nowhere else.

You are one of four skeptics in run C of the whole-design audit (`C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`, whose `[rubric]` grades
what you confirm). Each finding below was returned by a walker reading the sealed copy of the design at
`C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/`. Try to refute each one: re-read its address in the copy, and confirm it
only when the defect is there and does what the finding says. Then try to break each clean cell listed after them, a
cell a walker judged to hold.

## What you may read, and nothing else

1. **The sealed copy's design records,** under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/`, but not its
   `*-compared.md`, `*-instruments.md` or session-log records, and nothing in the copy's `reviews/` or `prompts/`.
2. **The design map,** `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/design-map.txt`, as your index, and **Stage 0's leads,** `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/stage0-leads.md`,
   which some findings cite.
3. **Code** under the working tree's `tools/`, `skills/` and `.githooks/`, to test a claim the design makes about
   today, and the protocol files your charter names: `memory/guides/`, `memory/HYGIENE.md` and `memory/TEMPLATE-SPEC.md`.
4. **This brief,** and your own scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-c4/`.

Read nothing else: not the working tree's other records, not the walkers' returns, not the session's scratchpad or
temp folders, not other briefs, not git history. The copy is the subject: judge every finding against it alone, since
the working tree may differ from it.

## Findings to refute

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

### C5-F17 — The reuse check's re-entries omit the rework budget and the non-converging end that flow-steps settled
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0410
- **Class:** K2
- **Severity:** medium
- **Evidence:**
  - cl-0410: "re-entries bounded by `flow.route-backs`".
  - flow-steps [build] `build.reuse-check`: "re-entries past `flow.route-backs` → that item's loop ends non-converging and its open rows go to asks, each re-entry drawing on `flow.rework-budget` (revised 2026-10-19 by the owner's SL-1 and SL-2)".
- **Consequence:** A reuse-check loop built from the clause neither draws on the build's budget nor files its open rows as asks, which breaks P39's single budget per build.
- **Fix:** Append to cl-0410: "each re-entry drawing on `flow.rework-budget`, and past `flow.route-backs` ending non-converging with its open rows filed as asks". Seen on a planted fourth re-entry.

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

### C5-F20 — "Runs neither … both" in cl-0430 has no antecedent inside the clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0430
- **Class:** K1
- **Severity:** low
- **Evidence:** cl-0430: "an update `kits.offer` offers runs neither in the adopter's tree, and its outbox order names the adopter's own run of both". The referent, `adopt` and `test.seed`, is in cl-0427.
- **Consequence:** A spec carrying cl-0430 whole cannot tell which runs are withheld, and the carries join pins this text.
- **Fix:** Reword: "… runs neither `adopt` nor `test.seed` in the adopter's tree, and its outbox order names the adopter's own run of each".

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

### C5-F22 — The fates join's population leaves out rows the table holds
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0488
- **Class:** K10
- **Severity:** low
- **Evidence:**
  - cl-0488's population is "`git ls-files` across `tools`, `skills`, `.githooks`, `.claude`, `.github`, `help`, the runbook and the template".
  - The fates table has a `guides` row ("hand-written guides | RETIRED", under `memory/guides/`) and the unattended row "`.unattended.conf` extension vocabularies", whose file is at the repository root.
- **Consequence:** A guide or a root kit conf that remains after convergence is outside the exit check.
- **Fix:** Derive the population from every fates row's path glob, plus the listed directories, and plant a surviving `memory/guides/` file to see it red.

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

### C3-F23 — dLinkedLibrary owns gap-mem-11 and gap-mem-12, but no clause of it carries either
- **Address:** architecture-v2 [chain] dLinkedLibrary row, Gaps owned (`gap-mem-11`, `gap-mem-12`)
- **Class:** K8
- **Severity:** low
- **Evidence:** gap-mem-11 covers records that contradict code: the map README path, `backlog.py`'s claim, the DEPL rows, `ANNOTATION-STYLE` saying no gate reads comment citations, and `HYGIENE.md`'s unused `note` kind. gap-mem-12 says: "the annotation follow-through test decides nothing: it has no threshold, sample size or window". layer-memory [annotations] says: "follow-through after landing, against today's 11.0% … The test's threshold, sample and window are dTotalRecall's to set". No clause of 0238–0261 carries either gap.
- **Consequence:** Both gaps survive their owner's landing, and the pushed-at-read fallback has no deciding test.
- **Fix:** Add a clause correcting gap-mem-11's records, including the ANNOTATION-STYLE guide and template pair. Set gap-mem-12's threshold, sample and window in 0244.

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

### C3-F15 — dTotalRecall owns gap-mem-23 (touch-drop wired to nothing), but no clause of it carries the gap
- **Address:** architecture-v2 [chain] dTotalRecall row, Gaps owned (`gap-mem-23`)
- **Class:** K8
- **Severity:** medium
- **Evidence:** gap-mem-23 says: "`--drop-affordance-exempt` has no caller in `tools/` …". Grepping tools/, skills/ and .githooks/ finds it only inside `tools/codebase-map/map_diff.py` and its README. retrofit's chain table says: "dScopedBuild | … the touch join as `build.scope`'s one check …, calling the map's touch-drop". None of 0212–0237 mentions the touch-drop.
- **Consequence:** The gap's owner lands without closing it, and its actual closer (dScopedBuild) does not own it.
- **Fix:** Move gap-mem-23 to dScopedBuild, which completes the closure and descends from dTotalRecall, by the register's own rule. Alternatively, add a dTotalRecall clause wiring the drop.

### C2-F1 — Clause `cl-dClosedLoop-0093` was deleted, so P23 is enforced by a clause that does not exist and gap-orient-05 is carried by no clause
- **Address:** architecture-v2 [chain], dDeclaredLoop row, between `cl-dClosedLoop-0092` and `cl-dClosedLoop-0094`; architecture-v2 [enforcement], row `P23`.
- **Class:** K5, c5
- **Severity:** blocker
- **Evidence:**
  - v2 [enforcement] (v2:1707) says `| P23 | cl-dClosedLoop-0093 |`.
  - In the copy, `grep -rn cl-dClosedLoop-0093` finds only that row. No clause in [chain] carries the id.
  - Counting the distinct ids in [chain] (v2:1629-1660) gives 495. Stage 0's K5, run on the working tree, read "clauses 496 … findings 0" (stage0-leads).
  - [clause-ids] says "Retired: none", so the id was never legitimately retired.
  - The walk record still lists the clause in dDeclaredLoop's roster: walk:1081 "8. claims keyed and trusted by key and source", and walk:893 "17. claims keyed and trusted by key and source".
  - P23 (v2:806): "A claim is acted on only when its stored key recomputes equal and its weakest source is not typed by an agent".
  - dDeclaredLoop still owns gap-orient-05 (gap-register:135, "Claims carry no freshness keys"), but only 0092's "each claim's key and verdict printed" mentions claim keys. Nothing makes a reader recompute the key or check the source.
- **Consequence:** dTrueNorth's carries join and Stage 0's K5 go red on an id no clause carries. No spec of dDeclaredLoop builds the trust-by-key rule, so the card, the position engine and every claim reader act on stale or agent-typed claims, the failure gap-orient-05 measured (4 of 17 run claims disagreed).
- **Fix:** Restore `cl-dClosedLoop-0093`, "claims keyed and trusted by key and source", in dDeclaredLoop's row between 0092 and 0094. Give it its seen-red arm: a planted claim whose key no longer recomputes, and one whose weakest source is agent-typed, are each re-derived and never acted on.

### C3-F28 — P29's enforcement row names one clause, though P29 has six rules
- **Address:** architecture-v2 [enforcement] P29
- **Class:** K5
- **Severity:** medium
- **Evidence:** P29 has six rules beyond handed and keyed inputs: verifiers alone, cold (`roles.verifier-context`); answered calls (`roles.answered-calls`); false facts (`roles.on-contradiction`); acting on keyed facts (`roles.trust`); "Recall: recall is re-verified once, by the orientation scout at entry". Its row names only `cl-dClosedLoop-0178`. 0196, 0197, 0198 and 0205 carry the keys, but they sit in no row, and no clause carries the orientation scout's one recall re-verification (0192 and 0204 only compose the card).
- **Consequence:** The principle registry certifies P29 from a clause that carries one of its rules. The recall boundary is never built.
- **Fix:** Add 0196, 0197, 0198 and 0205 to P29's row. Add the recall re-verification to 0192.

### C4-F4 — The settling row names an orientation scout as `entry.intake`'s actor, though 0282 builds it as a hook
- **Address:** flow-steps `[entry]` `entry.intake` row, against architecture-v2 [chain] cl-dClosedLoop-0282
- **Class:** K1
- **Severity:** medium
- **Evidence:**
  - The flow-steps `entry.intake` row reads "Actor: orientation scout, in an owner-bound session only … Proven by: the intake entry the scout writes".
  - The same record's amendment row `hook-actor-kind` says "`entry.intake` is a hook". Its own Owner note calls it "`entry.intake`'s hook".
  - layer-roles line 414 lists it as "| hook | `entry.intake` |".
  - 0282 builds "the prompt-submit hook writing each owner prompt verbatim".
- **Consequence:**
  - The item join and the owner check will read a scout, an agent, as the writer of the intake record.
  - That record is "the mandate to land" (gap-rt-14), so the owner's verbatim mandate would be agent-typed.
  - A builder of 0282 or of `entry.orient` meets two contradictory actors.
- **Fix:** set the flow-steps row's actor to "hook: prompt-submit, owner-bound sessions only", and its witness to "the intake entry the hook writes".

## Clean cells to attack

- `cl-dClosedLoop-0265` in dMindYourWords
- `cl-dClosedLoop-0069` in dFairHearing
- `cl-dClosedLoop-0096` in dDeclaredLoop
- `cl-dClosedLoop-0154` in dKeptSession
- `cl-dClosedLoop-0196` in dFurnishedOrders
- `cl-dClosedLoop-0405` in dScopedBuild
- `cl-dClosedLoop-0077` in dFairHearing
- `cl-dClosedLoop-0415` in dShippedRelease

## What you return

Your final message, nothing else:
- for each finding, `- <id>: confirmed <severity>` or `- <id>: refuted`, then one line with the reason you observed,
  quoting its address; a severity the rubric grades otherwise than the walker did, said so;
- for each clean cell, `- <clause> <build>: holds`, or `- <clause> <build>: defect` with the defect written as a new
  finding in the walkers' grammar, its id `CS4-F<n>`;
- last, `- **Read outside the list above:** none`, or each path you read outside it and why.

Write nothing to the repository; any probe you run writes under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-c4/` only. Your effort is the one the owner's
role definition sets.
