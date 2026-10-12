---
slug: aPairedSlots
node: a
opened: 2026-10-11
streams: tooling
roster: TOOL
ids: TOOL-aPairedSlots-1 TOOL-aPairedSlots-2 TOOL-aPairedSlots-3 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6 TOOL-aPairedSlots-7 TOOL-aPairedSlots-8 TOOL-aPairedSlots-9 TOOL-aPairedSlots-10 TOOL-aPairedSlots-11 TOOL-aPairedSlots-12 TOOL-aPairedSlots-13 TOOL-aPairedSlots-14 TOOL-aPairedSlots-15 TOOL-aPairedSlots-16 TOOL-aPairedSlots-17 TOOL-aPairedSlots-18 TOOL-aPairedSlots-19 TOOL-aPairedSlots-20
authorized-by: prompt
---

# aPairedSlots — two non-doc gate bars at once, and doc-only bars never queue

## The problem this build exists to solve

The run-gates turnstile admits one bar and queues every other. On 2026-10-11 a doc-only landing bar
waited over 30 minutes behind an unrelated full bar, with a third bar queued behind it, so the
queue and not the legs is now the main cost of a landing. The owner asked for two non-doc bars at
once, and for doc-only bars to be admitted freely under a key of their own. The turnstile's header
records a measurement saying two concurrent bars are slower than two serial ones, so this build
re-measures that before any code and lets the numbers set node a's slot count. The owner's prose is
the mandate, recorded under [prompts/](prompts/2026-10-11-prompt-TOOL-aPairedSlots-1.md).

## Expected improvements

- A doc-only bar never waits behind another worktree's bar.
- Where the A/B shows it pays, two non-doc bars run at once and the queue halves.
- The slot count is a declared knob with a recorded measurement behind its value.
- Two concurrent bars on one repository lose no ledger row, run-log line or run record.

## Detriments if this is not built

- Every landing keeps queueing behind any unrelated full bar on the host.
- Doc-only landings keep paying a full bar's wait for a run of seconds.
- The serialization rule rests on a three-bar measurement nobody has repeated for two bars.

## Build-level rules

- **Classification (M2)**: six units at open; eight after the shared-path audit split unit 5, nine after the owner cut the A/B to one repetition (2026-10-11); all authored this run, one mechanism each.
- Built on aFrugalTurnstile's host-wide turnstile (TOOL-aFrugalTurnstile-5), never on the one it
  replaced; this run's code passes start only once that build has landed on the default branch.
- Units 1, 2, 3, 4, 5 and 7 write `tools/run-gates/run-gates.sh` and run in that order; unit 9 runs
  last, since it sets that file's share rule, and the A/B left the value it already had. Unit 6
  writes the unattended kit and unit 8 the process-monitor self-test; each is disjoint from the rest.
- Out of scope, owned by aFrugalTurnstile: the scoped and full staleness rules, lineage reuse,
  `post-merge.sh` and the push boundary.
- One kit-version bump per touched kit, after the last unit.

## Parked decisions

- **Node a lands at one slot, dark.** The two-bar A/B (TOOL-aPairedSlots-9) measured A1, two bars
  one after the other, at 8440 s. B1, both at once at half width, ran past 11162 s, and C1, both at
  once at full width, ran past 8945 s; both were stopped past A1's makespan, so neither meets the
  rule. All three arm-runs ran beside other sessions' bars, on a host whose kernel pool had leaked to
  26 GB. To turn two slots on, add `slots=2` to the `capable` row of `tools/run-gates/gate-profiles.txt`,
  or set `GATE_TURNSTILE_SLOTS=2`; re-measure on a freshly booted host first. The numbers are in
  [the results record](build/2026-10-11-build-TOOL-aPairedSlots-9-ab-results.md).

Other parked entries live in `RUN.md` and are surfaced in the wrap-up.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aPairedSlots-1` | a `slots=<n>` key on each profile row, kit default 1 and overridable by `GATE_TURNSTILE_SLOTS` |
| 2 | `TOOL-aPairedSlots-2` | the turnstile is a counting semaphore of `slots` beacons, each reaped and released on its own |
| 3 | `TOOL-aPairedSlots-3` | a bar dispatched while another slot is held takes the shared width its rule names |
| 4 | `TOOL-aPairedSlots-4` | a doc-only bar takes its own key and never queues |
| 5 | `TOOL-aPairedSlots-5` | a worktree holds at most one slot, so every path under its git dir stays one bar's; the shared-path audit and the two-real-bar check |
| 6 | `TOOL-aPairedSlots-6` | the unattended driver's gate backstop stays correct with two holders |
| 7 | `TOOL-aPairedSlots-7` | the common dir's run log, shared full green and drift history header take a second concurrent writer safely |
| 8 | `TOOL-aPairedSlots-8` | the process-monitor adopter self-test stamps a fixture's common dir, not the real one |
| 9 | `TOOL-aPairedSlots-9` | node a's slot count and the shared-width rule, set by the two-bar A/B at one repetition per arm (owner, 2026-10-11) |
| 11 | `TOOL-aPairedSlots-11` | the drift history is created with its header already in it (closing review H1) |
| 12 | `TOOL-aPairedSlots-12` | the A/B instrument reads the run record's verdict by key, and the rule check proves an arm from its bar rows (closing review H2) |
| 13 | `TOOL-aPairedSlots-13` | the two-bar check reads the verdict by key and grades its rows at their declared width (closing review H3) |
| 14 | `TOOL-aPairedSlots-14` | the two-bar check's overlap guard reads the slots the bars were admitted to (closing review H4) |
| 15 | `TOOL-aPairedSlots-15` | the closing review's mediums and lows, batched |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 14 unit(s) · node a · opened 2026-10-11 · streams tooling
ids TOOL-aPairedSlots-1 TOOL-aPairedSlots-2 TOOL-aPairedSlots-3 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6 TOOL-aPairedSlots-7 TOOL-aPairedSlots-8 TOOL-aPairedSlots-9 TOOL-aPairedSlots-10 TOOL-aPairedSlots-11 TOOL-aPairedSlots-12 TOOL-aPairedSlots-13 TOOL-aPairedSlots-14
ids TOOL-aPairedSlots-15 TOOL-aPairedSlots-16 TOOL-aPairedSlots-17 TOOL-aPairedSlots-18 TOOL-aPairedSlots-19 TOOL-aPairedSlots-20

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aPairedSlots-1 — a `slots=<n>` key on each profile row, kit default 1, overridable by `GATE_TURNSTILE_SLOTS`](spec/2026-10-11-spec-TOOL-aPairedSlots-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-10-11 |
| [TOOL-aPairedSlots-6 — the unattended driver's gate backstop stays correct with two holders](spec/2026-10-11-spec-TOOL-aPairedSlots-6.md) | 1 | 1 | CLOSED | rev-1 | 2026-10-11 |
| [TOOL-aPairedSlots-8 — the process-monitor adopter self-test stamps a fixture's common dir, not the real one](spec/2026-10-11-spec-TOOL-aPairedSlots-8.md) | 1 | 1 | CLOSED | rev-2 | 2026-10-11 |
| [TOOL-aPairedSlots-2 — the turnstile is a counting semaphore of `slots` beacons, each reaped and released on its own](spec/2026-10-11-spec-TOOL-aPairedSlots-2.md) | 2 | 2 | CLOSED | rev-3 | 2026-10-12 |
| [TOOL-aPairedSlots-3 — a bar dispatched while another slot is held takes the shared width its rule names](spec/2026-10-11-spec-TOOL-aPairedSlots-3.md) | 3 | 2 | CLOSED | rev-3 | 2026-10-11 |
| [TOOL-aPairedSlots-4 — a doc-only bar takes its own key and never queues](spec/2026-10-11-spec-TOOL-aPairedSlots-4.md) | 4 | 2 | CLOSED | rev-1 | 2026-10-11 |
| [TOOL-aPairedSlots-5 — a worktree holds at most one slot, so every path under its git dir stays one bar's](spec/2026-10-11-spec-TOOL-aPairedSlots-5.md) | 5 | 2 | CLOSED | rev-2 | 2026-10-11 |
| [TOOL-aPairedSlots-7 — the common dir's shared files take a second concurrent writer safely](spec/2026-10-11-spec-TOOL-aPairedSlots-7.md) | 6 | 2 | CLOSED | rev-4 | 2026-10-12 |
| [TOOL-aPairedSlots-9 — node a's slot count and the shared-width rule, set by the two-bar A/B](spec/2026-10-11-spec-TOOL-aPairedSlots-9.md) | 7 | 2 | CLOSED | rev-2 | 2026-10-12 |
| [TOOL-aPairedSlots-12 — the A/B instrument reads the run record's verdict by key, and the rule check proves an arm from its bar rows](spec/2026-10-12-spec-TOOL-aPairedSlots-12.md) | 8 | 1 | CLOSED | rev-1 | 2026-10-12 |
| [TOOL-aPairedSlots-13 — the two-bar check reads the verdict by key and grades its rows at their declared width](spec/2026-10-12-spec-TOOL-aPairedSlots-13.md) | 8 | 1 | CLOSED | rev-1 | 2026-10-12 |
| [TOOL-aPairedSlots-11 — the drift history is created with its header already in it](spec/2026-10-12-spec-TOOL-aPairedSlots-11.md) | 9 | 2 | CLOSED | rev-1 | 2026-10-12 |
| [TOOL-aPairedSlots-14 — the two-bar check's overlap guard reads the slots the bars were admitted to](spec/2026-10-12-spec-TOOL-aPairedSlots-14.md) | 9 | 1 | CLOSED | rev-1 | 2026-10-12 |
| [TOOL-aPairedSlots-15 — the closing review's mediums and lows, batched](spec/2026-10-12-spec-TOOL-aPairedSlots-15.md) | 9 | 2 | CLOSED | rev-2 | 2026-10-12 |
<!-- /gen:build-units -->

Records: 25 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aPairedSlots-1 TOOL-aPairedSlots-2 TOOL-aPairedSlots-3 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6 TOOL-aPairedSlots-7 TOOL-aPairedSlots-8 TOOL-aPairedSlots-9 TOOL-aPairedSlots-11 TOOL-aPairedSlots-12 TOOL-aPairedSlots-13
TOOL-aPairedSlots-14 TOOL-aPairedSlots-15.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aPairedSlots-1`, `TOOL-aPairedSlots-6`, `TOOL-aPairedSlots-8` | yes |
| 2 | `TOOL-aPairedSlots-2` | no |
| 3 | `TOOL-aPairedSlots-3` | no |
| 4 | `TOOL-aPairedSlots-4` | no |
| 5 | `TOOL-aPairedSlots-5` | no |
| 6 | `TOOL-aPairedSlots-7` | no |
| 7 | `TOOL-aPairedSlots-9` | no |
| 8 | `TOOL-aPairedSlots-12`, `TOOL-aPairedSlots-13` | yes |
| 9 | `TOOL-aPairedSlots-11`, `TOOL-aPairedSlots-14`, `TOOL-aPairedSlots-15` | yes |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
