# Skeptic return: run B, batch 4

**Serves:** research PLAY-dClosedLoop-1

Dispatch 182's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-23-skeptic.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

- B3-F7: confirmed medium
  Verified at flow-steps [test] `test.route` (line 296). The arm "an OWN or MIXED red → `test.attribute`" has no blocking condition, while "a red that does not block → an ask" also applies. Under v2's default `verdict.blocks: own-only` (line 1144; walkthrough line 303: "MIXED and CONTENDED are reported and filed, not blocking"), a MIXED red matches both arms, which is what layer-flow [settled] line 329 describes.

- B4-F2: confirmed high
  flow-steps [transitions] (lines 623-650) has no row for closing incomplete and no parked state. Its only hold is `paused`, and line 596 says a paused build keeps its leases. v2 `cl-dClosedLoop-0116` (close incomplete) and `cl-dClosedLoop-0326` (park, lease released) both need such a row. The default `run.on-owner-silence: apply-recommendation` (v2 line 1103) parks a build whose ratification goes unanswered, so S6 reaches a transition the table lacks. `life.quiesce` also routes "pause → parked", a state the table does not have. One detail of the evidence is off: the `incomplete` grep does print lines, but only unrelated ones.

- B5-F13: refuted
  The premise "with no commit" is false. `kits.currency` itself counts tags "after the installed commit". Today's receipt records `gov_commit` (tools/govkit/govkit.py:8020), and each row records `commit`, `gov_oid` and `sha256`. Schema 4 (`cl-dClosedLoop-0020`) and schema 5 (`cl-dClosedLoop-0435`, which adds `prior_commit`) extend that receipt. A moved tag therefore installs under a receipt naming a different commit and different blob ids, not "the same receipt". The tag-date skew point is negligible: gov's one cutter dates every tag, and releases are days apart while the skew is seconds.

- B5-F5: confirmed medium
  layer-expansions [design-distribution] `kits.cut` (line 453): under `every-landing` each instance is keyed by its landed SHA, and layer-runtime [schedule] (line 793) gives each instance its own lease. Nothing serialises the choice of `<n>`, so two near-simultaneous landings pick the same `gov/v<date>.<n>`. The only route for the refused push is "an owner item".

- B5-F10: confirmed low
  The `kits.offer` row (line 456) still reads "adds an eighth; the mode refuses all eight", and the contract row (line 438) still says "schema 4". v2 `cl-dClosedLoop-0435` adds a ninth spawn kind and receipt schema 5, and it sits in dShippedRelease's row (v2 line 1651), the same build that owns these items.

- B5-F7: refuted
  The `kits.offer` row (line 456) itself names dShippedRelease's update hook running `test.seed` and `adopt` as target-side code "which the offer leaves to the adopter's own run". It routes "an update that needs target-side execution … → an outbox order". So an update that brings a new check does get the order, as `cl-dClosedLoop-0430` and retrofit [seed] (lines 373-376) say. There is no "ordinary pushed path" that skips it. Also, under `unarmed` an unseeded check reads unarmed and is never green, and under `refuse` the adopter's lander refuses the update.

- B5-F6: confirmed high
  layer-expansions `kits.install`, `kits.update` (line 457) is one row for two items, with the actor "the owner, or a command". flow-steps [rules] lines 21-23 forbid exactly that. The row has no Needs, and its only route is the no-target adapter case, so there is no success route, no failed-step route and no handoff to `test.seed`/`adopt`. S4 therefore reaches no terminal (c2). The "self-written witness" part is overstated: [rules] line 24 allows a witness written by a command.

- B5-F4: confirmed medium
  `loop.lease` (line 257) routes only to `loop.gather`, while `maintain.lease` (line 222) declares "held elsewhere → skip; done → nothing". `release.pick` (line 384) takes "E's promotion lease" and routes only to `release.approve`. Neither `release.record` (line 389) nor any v2 dShippedRelease clause releases that lease. "promotion lease" appears nowhere else in the design.

- B5-F14: confirmed medium
  The ancestor walk over v2's Parents column shows neither dTendedCadence nor dShippedRelease as the other's ancestor. dTendedCadence's `maintain.events` defaults to all three events (v2 line 1194). The producer of `release-verify-failed` is the release slot (`gap-deploy-01`, dShippedRelease), and the shared-key fixture (layer-expansions lines 242-247) needs `release.route`. Only dConvergedCharter descends from both builds.

- B1-F4: confirmed medium (walker said high)
  The `maintain.patch` row (line 225) routes straight to "Design", against [transitions] line 627 and [design] line 170. But flow-steps [entry] (lines 108-110) has a cadence filer's intake "placed by `entry.place` the same way", and retrofit [cadence] (line 496) routes the sweep "through `entry.place`'s `patch` disposition". So the design has a path that reaches the claim and the lease. What remains is a contradiction a spec writer trips over, not a scenario that fails.

- B5-F1: confirmed high
  Even on the route through `entry.place`, `patch.ratify` is read by no item: 0 hits in flow-steps, layer-flow and flow-roles, and it appears in v2 only as catalogue rows (lines 1204, 1519). The patch path (`entry.claim` → `design.input` → `design.unit-spec`) has no duplicate check. That leaves two of FI-4's "light five" (flow-interactions lines 103-105) unenforced, so a strict `patch.ratify: owner` silently loosens (c3). The entry-skip part of this finding stands at medium, as under B1-F4.

- B5-F2: confirmed high
  The `maintain.patch` witness is "the intake, keyed by (reading, offender key)" (line 225), and [design] line 166 makes a repeat on that key a no-op. `maintain.read` routes every later over-pin reading of the same offender back to `maintain.patch`, so the recurrence is swallowed, unlike `maintain.file`'s per-period `seen` rows (c3). The budget part is wrong: a Maintain patch is a build with its own `flow.rework-budget` (v2 line 1134: "one budget per build").

- B5-F11: confirmed medium
  `maintain.read` (line 223) has only "in pin / over pin / dead" routes, with no arm per band for v2's default `maintain.tiers: bands` (line 1201). `maintain.file` (line 226) always "files an ask", with "the ask" as its witness, so `maintain.on-breach`'s `red-leg` and `report` values (line 1193) have no arm. flow-steps [rules] line 32 requires routes declared per policy value.

- B5-F3: confirmed high
  The Maintain and Loop Review tables (lines 220, 255) have no Needs column. No route anywhere reaches `maintain.levels`, `maintain.record` or `loop.record`: read → direct/patch/file, direct → file, patch → Design, file → triage, `loop.file` → the breakpoint. `maintain.record` is the only item that "releases the lease", so a run never closes (c2).

- B4-F15: confirmed low
  layer-memory [contract]'s kind table (lines 397-477) has rows for `attendance override`, `probe`, `workspace` and `review`. Nothing registers "the trigger record" (`probe.trigger`, flow-steps line 536), "the command's record" (`life.request`, line 587, and the witness of [transitions] lines 645-646) or "the executor's record of the acts it let finish" (`life.quiesce`, line 588).

- B3-F1: confirmed high
  The layer-memory kind table reads "| seen-red | dWitnessedBar | its writer is `test.seen-red` |". That item's Does is only "checks that every gate … has a seen-red record" (flow-steps line 299). The recorder `gap-test-06` owes ("has no recorder", carried in v2 dWitnessedBar's row) has no item. The single declaration P30 relies on names the checker as the record's writer.

- B2-F7: refuted
  v2 `cl-dClosedLoop-0319` and night-pass-two (lines 327-330) say a unit taken by a session that does not hold the build is driven "only that unit's passes on its own branch, pushed the same way, its returns' rows … reaching the build's driver through the branch". layer-runtime [isolate] (lines 731-735) merges each unit branch into the build branch before the unit's lease is released. Where node x commits, and how its pass reaches the build branch, is therefore declared.

- B5-F12: refuted
  layer-runtime [schedule] (lines 793-797) checks the witness for each period key before and after taking the lease, and says "A missed period runs at the next wake". A node whose clock is a few seconds slow either finds the earlier period's witness and skips, or runs a period that genuinely never ran. No key runs twice. The "two records" are two different periods, both owed.

Clean cells:

- `build.unit-pass` S6: holds
  An acceptance red → fix pass, which draws on the budget under [rules] lines 38-44. An unreachable remote is covered by `stale-remote` in layer-runtime [decide] (line 335). Exhausting the budget is B4-F2's defect, not this cell's.

- `plan.triage-judge` S7: holds
  The planner role (dBoundRoles) and the schema factory (dDeclaredLoop) are both ancestors of dRankedPlan.

- `plan.triage-judge` S5: holds
  Withdrawal and supersession do not change its closed set of outcomes: select, defer, retire, refuse.

- `design.research` S5: holds
  `life.quiesce` lets the act in flight finish and dispatches nothing new. The research-return kind has its writer.

- `test.route` S7: holds
  Today's `GATE_ATTRIBUTE` (tools/run-gates/run-gates.sh lines 19-21, 4340-4348) already produces the five classes, and `gap-test-04` is owned by its own build.

- `maintain.read` S7: holds
  Its adapters, journal and memory-contract owner come from ancestors. The release-event hole is B5-F14's.

- `kits.adopters` S4: defect

### BS4-F1 — `kits.adopters` has no outcome for an unreachable remote or an unreadable receipt
- **Address:** layer-expansions [design-distribution] `kits.adopters`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S4
- **Evidence:** The row (line 455) "reads each register row's committed receipt at its remote tip" and routes only by `deploy.currency` value: "`pull-and-watch` → reported; `push-branches` → `kits.offer`; `pull-only` → recorded". [agree-distribution] (line 115) settles that "gov reads each adopter's committed receipt for the adopter view; an unreachable remote is unverified, never green". The sibling `kits.currency` (line 454) carries "unreachable → unverified, never green", and `kits.adopters` does not. flow-steps [rules] (line 28) says "Every item's outcome set is closed, and every outcome routes".
- **Consequence:** In S4, if the adopter's remote cannot be read, or its receipt cannot be read during the schema migration, the reading has no declared outcome. A spec writer can record it as "0 behind", drop it, or under `push-branches` offer an update against a receipt it never read. The adopter view shows nothing instead of "unverified".
- **Fix:** Add "unreachable or unreadable → the adopter record unverified, never green, reported as `pull-and-watch` reports, and no `kits.offer`" to the row, and seed a planted unreachable remote.

- `review.fold` S2: holds
  It is the driver's design-time item. `new:` slugs are claimed by compare-and-swap at `review.report`, and a unit-lease holder drives only its own unit's passes (`cl-dClosedLoop-0319`).

- **Read outside the list above:** I listed the names in `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/` once, to make sure my own scratch folder existed. That showed the other skeptics' and walkers' folder names, but I opened none of them. The listing of the copy's root also showed `stage0-leads.md` by name, and I did not open it. Every other read was the copy's design records, the design map, this brief, and code under the working tree's `tools/` (`tools/govkit/govkit.py`, `tools/run-gates/run-gates.sh`, plus a grep of `tools/`, `skills/` and `.githooks/`).
