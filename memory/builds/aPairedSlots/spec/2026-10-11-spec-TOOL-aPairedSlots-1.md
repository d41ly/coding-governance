# TOOL-aPairedSlots-1 — a `slots=<n>` key on each profile row, kit default 1, overridable by `GATE_TURNSTILE_SLOTS`

**Status:** CLOSED · rev-2 · 2026-10-11 · node a · Tier-2 · base b6cd02bc · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aPairedSlots-1-1-acceptance-ledger.md](../build/2026-10-11-build-TOOL-aPairedSlots-1-1-acceptance-ledger.md) | journal | TOOL-aPairedSlots-6 TOOL-aPairedSlots-8 |
| [2026-10-11-build-TOOL-aPairedSlots-1-ab-instrument.sh](../build/2026-10-11-build-TOOL-aPairedSlots-1-ab-instrument.sh) | journal | — |
| [2026-10-11-prompt-TOOL-aPairedSlots-1-1-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aPairedSlots-1-1-build-brief.md) | journal | TOOL-aPairedSlots-2 TOOL-aPairedSlots-3 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6 TOOL-aPairedSlots-7 TOOL-aPairedSlots-8 TOOL-aPairedSlots-9 |
| [2026-10-11-prompt-TOOL-aPairedSlots-1.md](../prompts/2026-10-11-prompt-TOOL-aPairedSlots-1.md) | research | TOOL-aPairedSlots-2 TOOL-aPairedSlots-3 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6 |

<!-- /gen:spec-records -->

## 1. Goal

How many bars the turnstile admits at once becomes a declared knob: a `slots=<n>` key on each
`tools/run-gates/gate-profiles.txt` row, 1 where a row omits it, overridden by
`GATE_TURNSTILE_SLOTS`, and printed by `--print-profile`. Which value node a's row carries is
TOOL-aPairedSlots-9's, from the two-bar A/B.

## 2. Scope (IN)

- **S1 — the row key.** `slots` joins `KNOWN_KNOBS` in `tools/run-gates/run-gates.sh` and is
  parsed with the existing row validator, so a non-numeric or over-long value refuses the bar as
  any malformed knob does. A value of 0 refuses too, with its own message, because a turnstile of
  no slots admits nothing. A row that omits the key resolves `PROF_SLOTS=1`, as does the built-in
  branch with no table. Observed by AC1.
- **S2 — the override.** `GATE_TURNSTILE_SLOTS`, when set, replaces the row's value. A value that
  is not a positive integer of at most 15 digits is IGNORED with one NOTE line naming it and the row
  value used, because this knob only schedules bars and can never skip a leg, which is the same
  rule `GATE_JOBS` follows. Observed by AC2.
- **S3 — where it is printed.** `--print-profile` prints `slots<TAB><n>` after `queue`. The
  profile line gains `, slots <n>` after the mempause field ONLY when the effective value is above
  1, so a run at 1 prints the line it prints today. Observed by AC1, AC3.
- **S5 — the knob classes and the pins.** `GATE_TURNSTILE_SLOTS` joins `BAR_INERT_KNOBS` in
  `.githooks/pre-push.test.sh`, because it decides contention and never a verdict. `slots` joins
  `PINNED_KNOBS` in `tools/run-gates/run-gates.test.sh`. Observed by AC5.
- **S6 — the text.** `gate-profiles.txt`'s KNOBS header gains the `slots=<n>` entry, and
  `tools/run-gates/README.md`'s knob table gains the row. NOT OBSERVED — prose, graded by the
  review, not by a check.

## 3. Non-goals (OUT)

- The semaphore that reads the value (TOOL-aPairedSlots-2) and the width it implies
  (TOOL-aPairedSlots-3). This unit resolves and prints the number; with only this unit built, a
  bar still admits exactly one holder whatever the number says.
- Node a's value and the A/B that decides it (TOOL-aPairedSlots-9).
- A per-host or per-repository slot declaration. The row is selected by detected hardware, as
  every knob is; a host running repositories that declare different values is the rollout question
  TOOL-aPairedSlots-2 states.
- Re-deriving the TTL, `TS_MAXWAIT` or the wall from the slot count.

### Edges

- **hands-off** `TOOL-aPairedSlots-2` — `PROF_SLOTS`, the resolved and overridden value, which
  the semaphore reads as its slot count.
- **hands-off** `TOOL-aPairedSlots-9` — the row value the A/B decides, written with this unit's key.

## 4. Design

The key rides the existing row validator, which already refuses an unknown key, a non-numeric value
and an over-long one, so `slots` needs only its name added and a zero check beside the `mempause`
percent check. The override follows `GATE_JOBS`: it replaces the value and never the row, and a
malformed value falls back rather than refusing, because a knob that only schedules bars can never
turn a leg into a pass or a skip.

The profile line is the one place a slot count could change what a bar prints at the kit default,
so the field appears only above 1.

### Inventory

New names: `PROF_SLOTS` (a shell variable, the resolved count), `slots` (a profile knob and a
`--print-profile` key), `GATE_TURNSTILE_SLOTS` (an environment knob). No function is minted.

### Rollout

A row without the key reads 1, so every adopter table keeps today's behaviour after a kit update.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/gate-profiles.txt`
- `tools/run-gates/README.md`
- `tools/run-gates/run-gates.test.sh`
- `.githooks/pre-push.test.sh`

### Alternatives rejected

- **A count derived from cores or RAM.** The earlier measurement found the contended resource is
  per-op latency that does not parallelise, so no hardware figure predicts the answer; only a
  measurement on the host does, and a declared row is where this tree keeps a measured number.
- **Refusing a malformed `GATE_TURNSTILE_SLOTS`.** The row value is the safe fallback and a knob
  that only schedules bars follows `GATE_JOBS`, which clamps rather than refuses.

## 5. Production-readiness checklist

- security — N/A — a count read from a tracked table and an environment knob; no new input surface.
- perf / scale — N/A here; the value and its measurement are TOOL-aPairedSlots-9's.
- error / empty / loading states — an absent key reads 1; a malformed row value refuses the bar; a
  malformed override is ignored with a NOTE.
- observability — `--print-profile` and, above 1, the profile line.
- risks — none beyond the row validator's; the shipped value is TOOL-aPairedSlots-9's risk.
- testing — AC1 to AC3 and AC5 in scratch fixtures; the canary's pinned set moves with the knob.
- migration — none; a missing key is the old behaviour.
- user docs — the README knob table and the profile table's header.

## 6. Acceptance criteria

The fixtures are scratch repos under the session scratch, built the way the canary builds one,
with a `gate-profiles.txt` row the arm writes.

- **AC1** — When a fixture row declares `slots=3`, the runner's profile verb prints a
  `slots` line reading 3, and with the key omitted one reading 1.
  Red when: the key is absent from `KNOWN_KNOBS`, and the row refuses as an unknown knob.
- **AC2** — When `GATE_TURNSTILE_SLOTS=2` is set over a row declaring none, `--print-profile`
  prints a `slots` line reading 2; when it is `abc`, it prints the row's value and stderr carries the NOTE.
  Red when: the override is not read, and the value stays 1.
- **AC3** — When a fixture bar runs at the effective value 1, its `gate profile:` line is
  byte-identical to the base runner's on the same fixture, and at 2 it carries `, slots 2`.
  Red when: the field is printed unconditionally, and the value-1 line differs from base.
- **AC5** — When `check_knob_classes`, sliced out of the pre-push hook's self-test, runs over the
  changed runner, it prints nothing, and before the classification it names
  `GATE_TURNSTILE_SLOTS`.
  Red when: the knob is left unclassified.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `memory hygiene`

New arm: tools/run-gates/run-gates.test.sh · covers AC1 AC2 AC3 · a fixture row without the key, then with it, then the override · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.
- rev-2 · 2026-10-11 · §1 · S4 · AC4 · §4 · §8 · the A/B, node a's value and F1 move to
  TOOL-aPairedSlots-9 on the owner's ruling of 2026-10-11 (one repetition per arm, build now), so
  this unit is the knob alone and builds while the A/B runs.

## 10. Reuse audit

`reuse_lookup.py "admit more than one gate bar at once with a counting semaphore of beacon slots"`
named no counting-semaphore seam; the knob extends the existing profile-row parse in
`tools/run-gates/run-gates.sh` (`KNOWN_KNOBS` and its validator) and the `--print-profile` verb,
whose reader is `parse_gate_profile` in `tools/unattended/lib-unattended.sh`. Recall qid 921
returned TOOL-aMeteredTurnstile-6 and TOOL-aUnblockedFleet-6, the three-bar measurement
TOOL-aPairedSlots-9 re-runs for two bars.

Recall terms used: `python tools/memory-recall/query.py "why does the gate turnstile serialize bars and admit only one at a time" --terms "turnstile beacon queue ticket serialize concurrent bars width contended CPU host-wide nonce heartbeat reap slots"`
