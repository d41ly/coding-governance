# Fold brief: writer 5

**Serves:** research PLAY-dClosedLoop-1

**Your task is to fold the whole-design audit's findings at the 21 places below into dClosedLoop's design
records, as one fold script.** This brief is your instructions, not a spec to review.

## What you fold, and against what

- **The subject is the working tree's design records** under `memory/builds/dClosedLoop/build/`, at commit `8222099f8a619eef461fe91e84bd9f74173be730`.
  The findings were made on a sealed copy into which twelve past defects were planted. The copy is not your subject;
  read nothing in it. The plants are listed in the round record's `[recall-scored]`
  (`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`). A finding that describes a plant points at a defect
  the working tree never had.
- **Your records:** the records named by your places other than v2 and flow-steps. Edit nothing else. When a place needs an edit in another record, list it under
  *Requests* in your return, with the exact change, and leave it out of your script.
- **Read freely** in the working tree: every design record, the gap register, the design map, `tools/`, `skills/` and
  `.githooks/`. Write only in your scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fold/w5/`. Nothing goes into the repository.

## How you fold

1. **For each place,** read its findings below, then read the place in the working tree. Give it exactly one
   disposition:
   - `fold`: the defect is in the working tree, and the fix follows from what the design already settles. Write it.
   - `fork`: the fix chooses between real options, or changes what the design means. Write no fold. Name the
     question, the options and your recommendation, for the owner.
   - `plant`: the finding describes one of the twelve plants, absent from the working tree. Cite the plant.
   - `not a defect`: the working tree already answers it. Quote where.
   - `duplicate`: another place carries the same defect. Name it, and fold it there.
2. **Write the folds as one Python script,** `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fold/w5/fold-5.py`, using the build's fold library:

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
3. **Forks,** each: `### FK-5-<k> — <question>`, then the options, your recommendation and the findings it rests on.
4. **Requests,** each naming the record, the exact change and the place it serves, or `none`.
5. **Read outside the list above:** `none`, or what and why.

Write nothing to the repository. Your effort is the one your role definition sets.

## The places

### Place 31: layer-expansions · kits.update · worst high · critical

#### A4-F4 — `kits.install` and `kits.update` have two actors, one route and no outcome for the step walk
- **Address:** layer-expansions [design-distribution] `kits.update`, `kits.install`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S4
- **What is wrong:** layer-expansions:457 gives both items the actor "the owner, or a command", against flow-steps [rules]' "One actor per item, of one kind". The only route is "an adapter that declares no target → its slot renders not installed". dSafePassage's walk outcomes have no route: step k exiting 1 with the receipt at k-1 (`cl-dClosedLoop-0022`), a reclaimed lock (`cl-dClosedLoop-0019`), the downgrade refusal (`cl-dClosedLoop-0021`), a `retired-edited` order (`cl-dClosedLoop-0026`), a step marked attended (`cl-dClosedLoop-0024`) and `instructions.stale: refuse` holding the update.
- **Consequence:** S4's central item cannot reach a terminal with its witness. A killed or failed step has nowhere to route, and its owner is never told.
- **Fix:** Split the row into one item per actor, for example `kits.update` (command) and `kits.update-attended` (owner). Give each a closed, routed outcome set: done; step k failed → receipt at k-1 and an owner item; held → order; attended → outbox order; refused → ask.
- **Skeptic:** Confirmed high (batch 4). The two actors break [rules], and the walk's outcomes have no route.

#### B5-F6 — `kits.install` and `kits.update` share one row with two actor kinds, no Needs and no terminal route
- **Address:** layer-expansions [design-distribution] `kits.update`
- **Class:** K1, c2
- **Severity:** high
- **Scenario:** S4
- **Defect:** One row serves both items, with the actor "the owner, or a command". flow-steps [rules] forbids that: one actor of one kind per item, and one item per policy value. The row has no Needs. Its only route is the case of an adapter with no target: there is no success route, no failed-step route and no handoff to `test.seed` or the `adopt` program.
- **Consequence:** An adopter's update in S4 reaches no declared terminal.
- **Fix:** Split the row into `kits.install` and `kits.update`, one row per actor value, each with Needs and a closed outcome set. Updated → `test.seed` for each new check → `adopt.declarations` and `adopt.instructions`. A step that exits nonzero → the receipt at step k-1 and a rerun. Held → an order.
- **Skeptic:** Confirmed high (c2). The walker's "self-written witness" leg is overstated, since [rules] allows a witness a command writes. That part of the fix is dropped.

### Place 32: layer-expansions · maintain.patch · worst high · critical

#### A3-F4 — `maintain.patch` opens a patch build at Design and skips placement, claim and lease
- **Address:** layer-expansions [Maintain items] `maintain.patch`
- **Class:** K2
- **Severity:** medium (the walker graded it high, c2)
- **Scenario:** S3
- **What is wrong:** layer-expansions:225 has `maintain.patch` open "a patch build at Design", routing "Design, as `patch.ratify` says", which skips `entry.place` and `entry.claim`. flow-steps [entry] (108-110) already says a cadence filer's prompt "is recorded as intake … and placed by `entry.place` the same way", and [transitions] requires the claim ref and the lease record for `patch`.
- **Consequence:** The expansion row contradicts the declared path. Built as written, a Maintain patch has no slug claim, no lease and no transition witness.
- **Fix:** Route `maintain.patch` to the filer's intake and then `entry.place`, so it reaches `entry.claim` the way every other patch does.
- **Skeptic:** Confirmed medium (batch 4), graded down from high. The design declares the right path in flow-steps [entry], so this is a contradiction a spec writer trips over, not a scenario that fails as designed.

#### A3-F8 — `maintain.patch`'s key has no period or SHA, so a recurrence after the patch lands counts as done
- **Address:** layer-expansions [Maintain items] `maintain.patch`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S3
- **What is wrong:** layer-expansions:225 keys the witness by "(reading, offender key)" only. `maintain.file` keys its `seen` rows by period, or event and SHA, and `cl-dClosedLoop-0092` makes items idempotent by witness.
- **Consequence:** When a patched offender regresses under the same key, the existing intake reads the re-patch as done. The regression is neither patched nor filed.
- **Fix:** Key the intake by (reading, offender key, base SHA). With a patch still open, a recurrence adds a `seen` row. With the patch landed, it opens a new patch on the shared budget.
- **Skeptic:** Confirmed medium (batch 4).

#### B5-F1 — Maintain's patch build skips entry, its claim and lease, and FI-4's light five
- **Address:** layer-expansions [design-observability] `maintain.patch`
- **Class:** K10, c3
- **Severity:** high (the entry-skip part: medium)
- **Scenario:** S3
- **Defect:** `maintain.patch` "opens a patch build at Design". [transitions] and `design.input` admit a patch only with its slug claimed and its lease taken by `entry.claim`. flow-steps [entry] and retrofit [cadence] route a cadence filer through `entry.place` instead, so the design states two entry routes for one patch. On either route, no item reads `patch.ratify`, and the patch path (`entry.claim` → `design.input` → `design.unit-spec`) runs no duplicate check. Two of FI-4's "light five" go unenforced.
- **Consequence:** A strict `patch.ratify: owner` silently loosens, because no item holds the patch for the owner. With no dedupe, `deploy.core`'s post-close patch and Maintain's `default-branch-red` patch for the same red both run.
- **Fix:** Route `maintain.patch`, and `deploy.core`'s post-close row, to "files a patch intake → `entry.place`", with `entry.claim` taking the slug and the lease. Give the patch path one item that runs `plan.dedupe` and one owner gate that reads `patch.ratify`, and add both to [transitions].
- **Skeptic:** Confirmed high (c3) on `patch.ratify` and the dedupe. `patch.ratify` has 0 hits in flow-steps, layer-flow and flow-roles, and appears in v2 only as catalogue rows. The entry-skip part stands at medium, as under B1-F4.
- **Same as:** B1-F4

#### B1-F4 — Maintain's patch skips entry.place and entry.claim and goes straight to Design
- **Address:** layer-expansions [design-observability] `maintain.patch`
- **Class:** K2
- **Severity:** medium (the walker graded it high)
- **Scenario:** S3
- **Skeptic:** Confirmed medium. flow-steps [entry] and retrofit [cadence] route a cadence filer's intake through `entry.place`, so a path to the claim and the lease exists. What remains is a contradiction a spec writer trips over, not a failing scenario. The item is under B5-F1.
- **Same as:** B5-F1

#### B5-F2 — A Maintain patch's key has no period, so a failed fix is swallowed
- **Address:** layer-expansions [design-observability] `maintain.patch`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S3
- **Defect:** The patch intake is keyed by (reading, offender key), with no period. Every command item in [design] is idempotent on its witness key. `maintain.read` routes every later over-pin reading of the same offender back to `maintain.patch`.
- **Consequence:** A patch lands, and the next period's reading of the same offender is still over its pin. The re-filing is a no-op on the existing key, so the breach is never filed again and never reaches the owner. `maintain.file`'s per-period `seen` rows do not have this hole.
- **Fix:** Key the intake by (reading, offender key, period). Route a recurrence on a closed patch to `maintain.file` as a `seen` row on an owner ask.
- **Skeptic:** Confirmed high (c3) on the swallowed recurrence. The walker's budget leg is wrong: a Maintain patch is a build with its own `flow.rework-budget` (v2: "one budget per build"). That part of the fix is dropped.

### Place 33: layer-expansions · maintain.record · worst high · critical

#### A3-F9 — Neither cadence program reaches its closing item, so the lease release and the record go unwitnessed
- **Address:** layer-expansions [Maintain items] `maintain.record`, `maintain.levels`; layer-expansions [Loop Review items] `loop.record`
- **Class:** K2
- **Severity:** medium
- **Scenario:** S3
- **What is wrong:** The Maintain and Loop Review tables (layer-expansions:220-262) have no Needs column. No route reaches `maintain.levels`, `maintain.record` or `loop.record`: `maintain.patch` routes to Design, `maintain.file` to Plan's triage and `loop.file` to the owner's breakpoint. Only `maintain.record` releases the lease. Stage 0 lists all three items as reached from no entry.
- **Consequence:** A Maintain run that patches or files never writes its maintenance record and never releases its lease. The Loop Review's record goes unwritten the same way.
- **Fix:** Add Needs columns, and route every outcome of `maintain.read`, `maintain.direct`, `maintain.patch`, `maintain.file` and `loop.file` to the program's record item.
- **Skeptic:** Confirmed medium (batch 4).

#### B5-F3 — The expansion tables declare no Needs, and `maintain.record`, `maintain.levels` and `loop.record` are never reached
- **Address:** layer-expansions [design-observability] `maintain.record` (the Maintain and Loop Review tables)
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S3
- **Defect:** The Maintain and Loop Review tables have no Needs column. No route reaches `maintain.levels`, `maintain.record` or `loop.record`: read goes to direct, patch or file; direct to file; patch to Design; file to triage; `loop.file` to the owner's breakpoint.
- **Consequence:** `maintain.record` is the only item that releases the period lease and writes the record that EX-3's default `every-period` owes. Neither happens, so a run never closes and the slower levels never run.
- **Fix:** Add a Needs column to every expansion table, for example `maintain.record` needing every reached item of the run and `maintain.levels` needing `maintain.lease`. End each program's terminal routes at its record item.
- **Skeptic:** Confirmed high (c2). No route anywhere reaches the three items.

### Place 34: layer-memory · test.seen-red · worst high · critical

#### B3-F1 — The seen-red check writes the record it checks for
- **Address:** layer-memory [design], kind `seen-red`; flow-steps [test] `test.seen-red`
- **Class:** K3, c3
- **Severity:** high
- **Scenario:** S1
- **Defect:** layer-memory's kind table names `test.seen-red` as the writer of the seen-red record. That item only checks that every gate the build added or changed has one. No item is the recorder that gap-test-06 owes, which dWitnessedBar's row carries.
- **Consequence:** The record's only declared writer is its checker. `test.seen-red` can pass for a gate nobody ever saw red, and P30's single declaration names the checker as the writer.
- **Fix:** Make the writer the run that observed the planted red: the leg factory's seen-red arm, run inside the unit's pass, keyed by the leg and the red SHA. Keep `test.seen-red` a reader. Seed a gate with no observed red that must make `test.seen-red` red.
- **Skeptic:** Confirmed high. The kind table's row and `test.seen-red`'s Does cell say exactly this.

### Place 39: layer-runtime · build.unit-pass · worst high · includes an unverified finding

#### B2-F7 — A cross-node unit has no workspace or integration rule under the default `build.worktree: shared`
- **Address:** layer-runtime [isolate]; flow-steps [build] `build.unit-pass`
- **Skeptic:** Refuted. `cl-dClosedLoop-0319` and night-pass-two say a unit taken by a session that does not hold the build is driven "only that unit's passes on its own branch", reaching the build's driver through the branch. layer-runtime [isolate] merges each unit branch into the build branch before the unit's lease is released.
- **Second skeptic:** Confirmed high. layer-runtime [isolate]: under the default `build.worktree: shared`, the build has "the build's one worktree" and a commit queue on the holding node. "Integration before release" covers unit branches only. Meanwhile cloud-and-scale [design] 8 has any node pick "ready, unleased units" across builds, and `design.streams` hands one build's units to several node units. Nothing says where node x commits or how its pass joins the build branch. Its fenced push to an advanced branch has no declared route, so S2 has no path to integration (c2).

### Place 111: coordination · cl-dClosedLoop-0143 · worst medium

#### A2-F10 — Coordination refs trust a writer's self-declared identity (STRIDE: spoofing, tampering, denial)
- **Address:** coordination [6]; architecture-v2 [chain] dKeptSession `cl-dClosedLoop-0143`; dWellOiledMachine `cl-dClosedLoop-0335`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S2
- **What is wrong:** The message's sender (fleet tag, session, build) is a field the writer types, and `cl-dClosedLoop-0143` names the ref by `<fleet tag>/<session>`. `cl-dClosedLoop-0335` refuses only an agent-forged request record, and `cl-dClosedLoop-0160` derives a message id from the session without checking identity. Under Codex the invariants "hold only at the git boundary" (layer-runtime:830). No clause binds the writer of a mail, lease or tombstone ref to the identity it names.
- **Consequence:** An act session on node x can write an `ack` or `answer` in X's name, which unblocks X's transitions. It can also write a terminal tombstone on X's lease, which refuses every take-over.
- **Fix:** Bind each coordination write to its writer, through the act's binding record or a signing key in the node profile. Refuse at the record door a ref whose path names another writer. See it red on a planted cross-session mail write and a forged tombstone.
- **Skeptic:** Confirmed medium (batch 2).

### Place 112: coordination · cl-dClosedLoop-0162 · worst medium

#### A2-F5 — No item or actor answers a mailbox `question`, while it blocks the recipient's transitions for 72h, past its 24h lease
- **Address:** coordination [6] "The mailbox"; architecture-v2 [chain] dKeptSession `cl-dClosedLoop-0162`; flow-steps [rules]
- **Class:** K1
- **Severity:** medium (the walker graded it high)
- **Scenario:** S2
- **What is wrong:** coordination [6] refuses every transition while a message addressed to the build is "neither answered nor acknowledged", until `flow.wait-ceiling` (72h) passes and the asker's default answers. No flow-steps item or actor answers or acknowledges a `question`, and `next` only lists them. `leases.renewal: progress` renews only on witnessed progress or declared waits, and `leases.expiry-hours` is 24.
- **Consequence:** Y asks through X's mailbox, X runs unattended and nothing answers. X's next step transition is refused for up to 72h, and its build lease can lapse at 24h. X still reaches its terminal when the default answers, so this is a stall with lease churn.
- **Fix:** Declare the answering item: the role that owns the asked interface, dispatched by `next` when a `question` arrives. Declare the recipient's refused transition a wait inside the asker's deadline, so it renews. See it red on a planted question to an unattended build.
- **Skeptic:** Confirmed medium (batch 2), graded down from high. The block falls only on step transitions and the default answers at 72h, so no scenario fails.

### Place 113: flow · flow [Entry points, settled 2026-10-14] · worst medium

#### A3-F2 — The post-close row still sends a post-landing red to triage as an ask
- **Address:** flow [Entry points, settled 2026-10-14]
- **Class:** K2
- **Severity:** medium
- **Scenario:** S3
- **What is wrong:** The table's last row still reads "A failed verify after its build closed at landing | Plan's triage | filed as an ask, then a patch build or a planned build by its size". layer-flow:326-328 says the row "now covers a landing-review finding and a post-landing core red, each entering as a patch build", but the table was never changed. `deploy.core`, `deploy.distill` and the landing review all route through that row.
- **Consequence:** A spec writer for `deploy.core` reads two contradictory entry paths: an ask through triage, or a patch at Design.
- **Fix:** Revise the row: a post-landing core red or a landing-review finding enters at Design as a patch build, and a post-close failed verify enters at triage.
- **Skeptic:** Confirmed medium (batch 2).

### Place 142: layer-expansions · kits.adopters · worst medium

#### A4-F18 — `kits.adopters` routes on `deploy.currency`'s values without naming the key
- **Address:** layer-expansions [design-distribution] `kits.adopters`
- **Class:** K4
- **Severity:** low
- **Scenario:** S4
- **What is wrong:** layer-expansions:455 routes on `pull-and-watch`, `push-branches` and `pull-only` without naming `deploy.currency`. v2:1177 is the key's only appearance in v2, and no clause reads it.
- **Consequence:** The key-read join reds, or a rename of the key drops the routes unseen.
- **Fix:** Write "as `deploy.currency` says" in the routes.
- **Skeptic:** Confirmed low (batch 4). The finding's other half is wrong: `kits.cut` and `kits.currency` already name `kits.host`, `kits.cadence` and `kits.watch-cadence` in their actor cells (layer-expansions:453-454).

#### BS4-F1 — `kits.adopters` has no outcome for an unreachable remote or an unreadable receipt
- **Address:** layer-expansions [design-distribution] `kits.adopters`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S4
- **Defect:** The row reads each adopter's committed receipt at its remote tip and routes only by `deploy.currency`'s value. [agree-distribution] settles that an unreachable remote is unverified, never green, and the sibling `kits.currency` carries that outcome. `kits.adopters` does not.
- **Consequence:** If an adopter's remote or receipt cannot be read during S4's migration, the reading has no outcome. It may show as "0 behind" or be dropped, and under `push-branches` an offer may go out against a receipt nobody read.
- **Fix:** Add "unreachable or unreadable → the adopter record unverified, never green, reported as `pull-and-watch` reports, and no `kits.offer`". Seed a planted unreachable remote.
- **Skeptic:** Raised by skeptic batch 4 at `kits.adopters` S4, where walker 5 gave `holds`. No second skeptic tested it.

### Place 143: layer-expansions · kits.cut · worst medium

#### B5-F5 — Concurrent `kits.cut` instances race for one tag number
- **Address:** layer-expansions [design-distribution] `kits.cut`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S2
- **Defect:** Under `every-landing` each cut instance is keyed by its landed SHA and takes its own lease. Nothing serialises the choice of `<n>` in `gov/v<date>.<n>`.
- **Consequence:** Two near-simultaneous landings pick the same tag number. The refused push becomes an owner item, its only route.
- **Fix:** Serialise cuts under one lease for the tag series. On a refused tag push, refetch and renumber within `flow.route-backs`, and raise an owner item only past that bound.
- **Skeptic:** Confirmed medium.

### Place 144: layer-expansions · kits.offer · worst medium

#### A4-F8 — `kits.offer`'s push grant "scoped to `gov/update-*`" is a scope the grant probe cannot see
- **Address:** layer-expansions [design-distribution] `kits.offer`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S4
- **What is wrong:** layer-expansions:456 scopes the grant "to `gov/update-*` on its one remote". The grant field (layer-runtime:869-871) is a list of scopes that registration probes, and the `grant` fixture (layer-runtime:1188) only checks granted against declared scopes. No record says how a ref-prefix scope is granted or probed, and a repository token's write scope is not per-ref.
- **Consequence:** Gov's node holds write grants to every adopter's remote. The probe either refuses every real token or certifies a repository-wide write grant as prefix-scoped.
- **Fix:** Declare the enforcement, such as a remote-side ruleset restricting the grant's identity to `gov/update-*`. Make the registration probe a refused push to a non-prefixed ref, seen red on a token that can push outside the prefix.
- **Skeptic:** Confirmed medium (batch 4). It could read as high, but a refused push already routes to an outbox order.

#### A4-F17 — `kits.offer` refuses "all eight" spawn kinds while cl-0435 adds a ninth
- **Address:** layer-expansions [design-distribution] `kits.offer`
- **Class:** K6
- **Severity:** low
- **Scenario:** S4
- **What is wrong:** layer-expansions:456 says "the design adds an eighth; the mode refuses all eight". `cl-dClosedLoop-0435` adds step processes as a ninth spawn kind, refused unless they run under the step kind's isolation contract, and has `kits.offer` run the steps that need no target code.
- **Consequence:** A spec writer working from the item omits the step-process kind and its isolation exception.
- **Fix:** Name the ninth kind and its exception in the item.
- **Skeptic:** Confirmed low (batch 4).

#### B5-F10 — `kits.offer`'s counts and the receipt schema are stale against v2
- **Address:** layer-expansions [design-distribution] `kits.offer`
- **Class:** K1
- **Severity:** low
- **Scenario:** S4
- **Defect:** The row says "adds an eighth; the mode refuses all eight", and the contract row says "schema 4". `cl-dClosedLoop-0435`, on the same build's row, adds a ninth spawn kind and moves the receipt to schema 5.
- **Consequence:** A spec writer building the offer mode from the row misses the ninth kind and the schema-5 fields S4's migration needs.
- **Fix:** Bring the row's count and the receipt line up to 0435.
- **Skeptic:** Confirmed low.

### Place 145: layer-expansions · loop.file · worst medium

#### BS3-F2 — `loop.file` files asks with no acceptance, which the default refuses
- **Address:** layer-expansions [design-observability] `loop.file`; layer-memory [asks]
- **Class:** K10
- **Severity:** medium
- **Scenario:** S2
- **Defect:** layer-memory [asks] refuses a filing that states no `accept` line, and `asks.acceptance` defaults to `refuse`. `loop.file` states none, unlike `maintain.file`.
- **Consequence:** Every Loop Review proposal's filing is refused. A cadence run has no build budget, so the run re-files every beat and never reaches the owner's breakpoint.
- **Fix:** State `loop.file`'s acceptance, either the owner's `review.loop.retire` breakpoint disposing the row or a keep record. Plant an ask that is refused without it.
- **Skeptic:** Raised by skeptic batch 3 at `loop.file` S2, where walker 5 gave `holds`. No second skeptic tested it.

### Place 146: layer-expansions · loop.lease · worst medium

#### B5-F4 — `loop.lease` and `release.pick` leave a lease held elsewhere unrouted, and E's promotion lease is never released
- **Address:** layer-expansions [design-observability] `loop.lease`; [design-integrations] `release.pick`, `release.record`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S2
- **Defect:** `loop.lease` routes only to `loop.gather`, and `release.pick` only to `release.approve`. Neither has the "held elsewhere" or "done" outcome `maintain.lease` declares. Neither `release.record` nor any dShippedRelease clause releases E's promotion lease.
- **Consequence:** Node x's instance has no outcome while node d holds the week's lease or E's. A finished pass leaves E's lease held, so the next landed SHA's pick blocks until expiry.
- **Fix:** Give `loop.lease` and `release.pick` the outcomes `maintain.lease` has: held elsewhere → skip; done → nothing. Make `release.record` release E's promotion lease.
- **Skeptic:** Confirmed medium. "Promotion lease" appears nowhere else in the design.

### Place 147: layer-expansions · maintain.file · worst medium

#### B5-F14 — dTendedCadence's release-verify-failed join depends on dShippedRelease, which is not its ancestor
- **Address:** layer-expansions [design-observability] `maintain.file`
- **Class:** K7
- **Severity:** medium
- **Scenario:** S7
- **Defect:** `maintain.file`'s ask for `release-verify-failed` joins `release.route`'s, and its fixture needs `release.route`. `release.route` is dShippedRelease's, and neither build is the other's ancestor. `maintain.events` defaults to all three events.
- **Consequence:** If dTendedCadence lands first, the join and its fixture have nothing to run against, so the arm lands unseen red or is skipped.
- **Fix:** Put the fixture and the join on dShippedRelease's row, or on a build descended from both (only dConvergedCharter is). Record dTendedCadence's event arm as a stand-in until then.
- **Skeptic:** Confirmed medium.

### Place 148: layer-expansions · maintain.read · worst medium

#### B5-F11 — `maintain.read` routes neither `maintain.tiers` nor `maintain.on-breach`
- **Address:** layer-expansions [design-observability] `maintain.read`
- **Class:** K4
- **Severity:** medium
- **Scenario:** S3
- **Defect:** `maintain.read` routes only in pin, over pin and dead, with no arm per band of the default `maintain.tiers: bands`. `maintain.file` always files an ask, so `maintain.on-breach`'s `red-leg` and `report` values have no arm. flow-steps [rules] requires routes declared per policy value.
- **Consequence:** A reading in the log or diagnose band has no route, and two of `maintain.on-breach`'s three values do nothing.
- **Fix:** Give `maintain.read` one route per tier band, and `maintain.file` one arm per `maintain.on-breach` value, each with its own witness.
- **Skeptic:** Confirmed medium.

### Place 149: layer-expansions · release.approve · worst medium

#### BS2-F2 — `release.approve` has two actors of two kinds, chosen by a policy value
- **Address:** layer-expansions [design-integrations] `release.approve`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S7
- **Defect:** The actor is "the owner, or a command", chosen by `deploy.promotion`. flow-steps [rules] makes an item whose actor a policy value chooses one item per value.
- **Consequence:** dDeclaredLoop's item factory cannot declare the item as written. `owner-approves-prod` and `auto-on-green` share one tag and one outcome table.
- **Fix:** Split it into `release.approve-owner` (the owner, under `owner-approves-*`) and `release.approve-auto` (a command, under `auto-on-green`), routed from `release.pick` by `deploy.promotion`'s value.
- **Skeptic:** Raised by skeptic batch 2 at `release.approve` S7, where walker 5 gave `holds`. No second skeptic tested it.

### Place 150: layer-expansions · release.route · worst medium

#### BS1-F2 — The release program's promotion lease is no lease the grammar declares, and its rollback is not fenced
- **Address:** layer-expansions `release.route` and `release.pick`; layer-runtime [Fencing]
- **Class:** K10
- **Severity:** medium
- **Scenario:** S2
- **Defect:** `release.pick` takes "E's promotion lease", which `cl-dClosedLoop-0120`'s lease grammar (builds, units and cadence runs) does not declare. The fence travels only with pushes by the commit queue and the lander, and `release.route` rolls E back through an engine adapter.
- **Consequence:** Where `release.environments` is set, a stale holder's in-flight rollback can reach E after another node has taken E's lease and promoted a newer SHA. E silently runs the older release, and its records disagree with what it runs.
- **Fix:** Add the promotion lease, with its epoch, to dPlacedRequest's lease grammar. Require every engine adapter's promote and rollback to check that epoch, or to compare-and-swap on E's current deployment id. Seen red on a planted stale holder's rollback after a take-over.
- **Skeptic:** Raised by skeptic batch 1 at `release.route` S2, where walker 5 gave `holds`. No second skeptic tested it.

### Place 151: layer-runtime · cl-dClosedLoop-0325 · worst medium

#### A2-F2 — The hand-over at the session-limit ceiling releases the build lease but not the in-flight unit's lease
- **Address:** layer-runtime [supervise] "Session limits"; architecture-v2 [chain] dWellOiledMachine `cl-dClosedLoop-0325`
- **Class:** K10
- **Severity:** medium (the walker graded it high, c2)
- **Scenario:** S2
- **What is wrong:** layer-runtime:405-406 and `cl-dClosedLoop-0325` release only "the build's lease as a hand-over" once the hold passes `runtime.hold-ceiling`. Under the default `leases.granularity: build-and-unit`, no record releases, tombstones or expires d's in-flight unit lease. Under the default `build.worktree: shared`, the partial pass sits only in d's worktree.
- **Consequence:** d hits its limit mid-unit. The build lease passes on, but the unit lease stays with d until `leases.expiry-hours` (24h) passes and `cl-dClosedLoop-0332`'s pick offers it. X's Build step, and Y waiting on X, are delayed by up to a day.
- **Fix:** At `runtime.hold-ceiling`, release every lease the held supervisor holds for the build as hand-overs. Push the in-flight pass's partial commit, or record it as lost so `resume.partial` restarts the item. Probe it with a limit planted mid-unit, followed by a second node claiming that unit within one tick.
- **Skeptic:** Confirmed medium (batch 4), graded down from high. The "no node can ever claim" branch does not hold: under `leases.renewal: progress` the unit lease expires and the pick offers it, so the build is delayed, not stuck.

### Place 170: fates · [table] · worst low

#### A4-F16 — The fates table gives govkit's `update` to dShippedRelease alone and marks govkit optional
- **Address:** fates [table] govkit "install and update, receipt"
- **Class:** K8
- **Severity:** low
- **Scenario:** S4
- **What is wrong:** The row (fates:176 in the copy, not :111) gives the reshape to dShippedRelease and omits dSafePassage, whose `cl-dClosedLoop-0019` and `cl-dClosedLoop-0020` reshape `update` and the receipt.
- **Consequence:** The row is wrong in wording only. `cl-dClosedLoop-0488` joins each path to its fate and grades no owner, and "govkit | optional" agrees with v2's `distribution` layer row.
- **Fix:** Add dSafePassage to the row.
- **Skeptic:** Confirmed low (batch 2). The claimed consequence, a wrong owner graded at dConvergedCharter's exit, does not follow.

### Place 178: layer-memory · [contract] · worst low

#### B4-F15 — Slice items write record kinds that are not registered
- **Address:** layer-memory [contract]
- **Class:** K3
- **Severity:** low
- **Scenario:** S5
- **Defect:** The kind table has no row for "the trigger record" (`probe.trigger`), "the command's record" (`life.request`) or "the executor's record of the acts it let finish" (`life.quiesce`).
- **Consequence:** Stage 0's K3 arm reads registered kinds only, so the three records have no declared reader, home or check.
- **Fix:** Register `probe trigger`, `lifecycle request` and `quiesce` rows, each with its writer item and readers.
- **Skeptic:** Confirmed low.

### Place 179: layer-runtime · [supervise] · worst low

#### A3-F18 — layer-runtime gives dDeclaredLoop the coordination feature that v2 places on dPlacedRequest
- **Address:** layer-runtime [supervise] "What stays where it is"
- **Class:** K8
- **Severity:** low (the walker graded it medium)
- **Scenario:** S5
- **What is wrong:** layer-runtime:1043 says dDeclaredLoop keeps "the coordination feature (`gap-conc-01`, `gap-conc-02`)", while v2:1639 gives dPlacedRequest the coordination feature and both gaps.
- **Consequence:** The line is a stale pointer. The gap join reads only v2's chain table, so the gap is not owned twice there.
- **Fix:** Re-point layer-runtime's line to dPlacedRequest.
- **Skeptic:** Confirmed low (batch 4), graded down from medium.
