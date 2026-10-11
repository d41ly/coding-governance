---
slug: aPairedSlots
node: a
opened: 2026-10-11
streams: tooling
roster: TOOL
ids: TOOL-aPairedSlots-1 TOOL-aPairedSlots-2 TOOL-aPairedSlots-3 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6
authorized-by: prompt
status: OPEN
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

- A doc-only bar never waits behind a non-doc bar.
- Where the A/B shows it pays, two non-doc bars run at once and the queue halves.
- The slot count is a declared knob with a recorded measurement behind its value.
- Two concurrent bars on one repository lose no ledger row, run-log line or run record.

## Detriments if this is not built

- Every landing keeps queueing behind any unrelated full bar on the host.
- Doc-only landings keep paying a full bar's wait for a run of seconds.
- The serialization rule rests on a three-bar measurement nobody has repeated for two bars.

## Build-level rules

- **Classification (M2)**: six units, MISSING at open, authored this run, one mechanism each.
- Built on aFrugalTurnstile's host-wide turnstile (TOOL-aFrugalTurnstile-5), never on the one it
  replaced; this run's code passes start only once that build has landed on the default branch.
- Units 1 to 4 all write `tools/run-gates/run-gates.sh` and run in roster order. Unit 5 writes the
  shared-path sites in the same file and runs after them. Unit 6 writes the unattended kit and is
  disjoint from the rest.
- Out of scope, owned by aFrugalTurnstile: the scoped and full staleness rules, lineage reuse,
  `post-merge.sh` and the push boundary.
- One kit-version bump per touched kit, after the last unit.

## Parked decisions

None yet. Parked entries live in `RUN.md` and are surfaced in the wrap-up.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aPairedSlots-1` | a `slots=<n>` key on each profile row, kit default 1 and overridable by `GATE_TURNSTILE_SLOTS`, set for node a by the two-bar A/B |
| 2 | `TOOL-aPairedSlots-2` | the turnstile is a counting semaphore of `slots` beacons, each reaped and released on its own |
| 3 | `TOOL-aPairedSlots-3` | a bar dispatched while another slot is held takes the width the A/B chose |
| 4 | `TOOL-aPairedSlots-4` | a doc-only bar takes its own key and never queues |
| 5 | `TOOL-aPairedSlots-5` | every path two concurrent bars on one repository both write is made safe or per-bar |
| 6 | `TOOL-aPairedSlots-6` | the unattended driver's gate backstop stays correct with two holders |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-10-11 · streams tooling
ids TOOL-aPairedSlots-1 TOOL-aPairedSlots-2 TOOL-aPairedSlots-3 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
