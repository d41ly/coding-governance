# TOOL-aPairedSlots-3 — a bar dispatched while another slot is held takes the shared width its rule names

**Status:** CLOSED · rev-3 · 2026-10-11 · node a · Tier-2 · base b6cd02bc · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aPairedSlots-3-1-acceptance-ledger.md](../build/2026-10-11-build-TOOL-aPairedSlots-3-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-prompt-TOOL-aPairedSlots-1-1-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aPairedSlots-1-1-build-brief.md) | journal | TOOL-aPairedSlots-1 TOOL-aPairedSlots-2 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6 TOOL-aPairedSlots-7 TOOL-aPairedSlots-8 TOOL-aPairedSlots-9 |
| [2026-10-11-prompt-TOOL-aPairedSlots-1.md](../prompts/2026-10-11-prompt-TOOL-aPairedSlots-1.md) | research | TOOL-aPairedSlots-1 TOOL-aPairedSlots-2 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6 |

<!-- /gen:spec-records -->

## 1. Goal

When a bar acquires a slot while another slot is already held, its worker-pool width follows the
rule the two-bar A/B chose, resolved once right after the acquire and printed as a profile line, so
two bars sharing the host run at the width that was measured to pay rather than at a width nobody
measured. The memory pause is confirmed host-wide and is not duplicated.

## 2. Scope (IN)

- **S1 — the held count, once.** Immediately after the `gate queue: acquired` line, a run that
  HOLDS a slot (`QUEUED_FROM` reads `held`) at a `TS_SLOTS` above 1 reads `measure_held_slots`,
  the number of slot paths that exist, its own included. It is read once and never again in the
  run. A nested, expired, unticketed, docs or disabled run reads nothing and keeps its width.
  Observed by AC1, AC3.
- **S2 — the rule.** At a held count of 2 or more, and with `GATE_JOBS` unset, the width follows
  `TS_SHARE_RULE`, a constant beside the turnstile block: `half` (arm B's rule) makes `JOBS` into
  `JOBS / held`, never below 1, and `full` (arm C's) leaves it. It ships as `full`, which changes
  no width, until TOOL-aPairedSlots-9 sets it from the A/B. `GATE_JOBS`, when set, is the operator's
  width and is never divided. Observed by AC1, AC2.
- **S3 — printed and recorded.** At a held count of 2 or more the run prints one line,
  `gate profile: width <w> at dispatch — <k> of <n> bar slots held (<rule>)`, rebuilds `PROF_LINE`
  with that width so the summary file and the durable copies carry it, and the header's `width`
  key records it, because the header is written after this point. At a held count of 1 nothing is
  printed and nothing changes. Observed by AC1, AC3.
- **S4 — the memory pause is the host's.** `read_mem_used` reads `/proc/meminfo` or the cgroup
  pair, both host-wide, so two bars pausing on one reading is already the shared pause; this unit
  adds none, and the turnstile block's header comment says so beside the width rule. Observed by
  AC4.
- **S5 — the text.** The run-gates README's turnstile section states the rule, the arm it came
  from and its record. NOT OBSERVED — prose, graded by the review.

## 3. Non-goals (OUT)

- Re-widening a running bar when the other holder leaves, or narrowing it when one arrives after
  this bar's acquire. The width is resolved once; the A/B measured two bars started together, and
  a bar that started alone at full width keeps it.
- A width rule for the doc-only key (TOOL-aPairedSlots-4), whose bars hold no slot.
- A second memory pause, or any change to `mempause`.

### Edges

- **consumes-from** `TOOL-aPairedSlots-2` — `measure_held_slots` and the slot paths it counts.
- **hands-off** `TOOL-aPairedSlots-9` — the value of `TS_SHARE_RULE`, which the A/B decides.

## 4. Design

The profile line is printed before the queue on purpose: a wait folded into it would delay it by
the whole wait. So the width resolved after the acquire is a SECOND `gate profile:` line, printed
only when it can differ from the first, and `PROF_LINE` is rebuilt so every later copy of it agrees
with what dispatched. The rule divides by the held count rather than by two, so a host declaring
three slots gets a third of the width under arm B's rule, which is the same rule at a larger count.

### Inventory

One function is minted, `render_prof_line`, in the `sh.function` cell: the profile line's one
template, called where the line is first built and again after a dispatch width moves it, so the
two copies cannot drift. `TS_HELD_N` is TOOL-aPairedSlots-2's; this unit adds the variable
`TS_SHARE_RULE` (the constant naming the rule, `half` or `full`). No new
header key: `width` already records the effective width.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.turnstile.test.sh`
- `tools/run-gates/README.md`

### Alternatives rejected

- **A row knob for the shared width.** It would be a second number the same A/B decides, beside
  `slots`, on a table whose every knob the canary pins; a rule that follows from the measurement
  belongs in the code that the measurement's record is cited from.
- **Resolving the width per dispatch.** A width that moves mid-run is one no record can report, and
  the A/B measured a fixed width per bar.

## 5. Production-readiness checklist

- security — N/A — a width computed from a count this runner already reads.
- perf / scale — the rule is the A/B's; the record is the evidence.
- error / empty / loading states — a held count that cannot be read counts this run's own slot
  only, which is the full width.
- observability — the dispatch line and the header's `width`.
- risks — a bar that acquires beside a bar started alone runs at the shared width while its
  neighbour runs full; the A/B did not measure that mix, and the README says so.
- testing — AC1 to AC4 in the turnstile suite's fixtures.
- migration — none.
- user docs — the README's turnstile section.

## 6. Acceptance criteria

- **AC1** — When a fixture bar acquires slot 2 while slot 1 is held, at a profile width of 4 and
  `GATE_TURNSTILE_SLOTS=2`, its output carries `width 2 at dispatch — 2 of 2 bar slots held` from a
  runner copy whose `TS_SHARE_RULE` is `half`, and `width 4 at dispatch` from one whose rule is
  `full`, and its header's `width` matches each.
  Red when: the held count is not read, and the width is the profile's under either rule.
- **AC2** — When the same bar runs with `GATE_JOBS=3`, its header's `width` is 3.
  Red when: the operator's width is divided.
- **AC3** — When a fixture bar acquires slot 1 with no other slot held, no `at dispatch` line is
  printed and its header's `width` is the profile's.
  Red when: the line is printed at a held count of 1.
- **AC4** — When two fixture bars share one `GATE_MEMINFO` file reading 95 percent used under
  `mempause=90`, both run records carry a non-empty `pauses` file.
  Red when: either bar reads a private source, and dispatches without pausing.

## 7. Gates

`run-gates turnstile` · `run-gates canary`

New arm: tools/run-gates/run-gates.turnstile.test.sh · covers AC1 AC2 AC3 AC4 · a runner copy with the held-count read removed · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.
- rev-2 · 2026-10-11 · S2 · AC1 · §8 · the rule becomes the constant `TS_SHARE_RULE`, shipped as
  `full`; F1 and setting the constant move to TOOL-aPairedSlots-9 on the owner's ruling of
  2026-10-11 (one repetition per arm, build now).
- rev-3 · 2026-10-11 · §4 · the profile line's template moves into `render_prof_line`, called at
  both sites, rather than a second inline copy of it after the dispatch width.

## 10. Reuse audit

The seam is the width resolution in `tools/run-gates/run-gates.sh` (`JOBS` from `PROF_WIDTH` and
`GATE_JOBS`, and `PROF_LINE`), extended after the acquire rather than duplicated, and
`read_mem_used`, confirmed host-wide and not extended. `reuse_lookup.py` named no seam for a
contention-scaled width. Recall returned TOOL-aMeteredTurnstile-6, the measurement that found width
24 slower than width 8.

Recall terms used: `python tools/memory-recall/query.py "why does the gate turnstile serialize bars and admit only one at a time" --terms "turnstile beacon queue ticket serialize concurrent bars width contended CPU host-wide nonce heartbeat reap slots"`
