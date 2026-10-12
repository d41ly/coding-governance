# Spec brief — TOOL-aBriskPreflight-7: preflight and the wiring check each declare a wall-clock ceiling and name a breach

**Serves:** research TOOL-aBriskPreflight-7

Read first: the build README, the prompt record (its `## Owner confirmation` carries the ruling
below) and the baseline record, and the specs of units 3 and 4, which are built before this one.

## The owner's item and ruling

Prompt: "Cost becomes a verdict. Preflight and the wiring check each declare a wall-clock ceiling,
and a run over it says so by name instead of waiting silently on a 3600 s bound."

The owner's answer at the one opening turn, chosen from three options: **"Name it, refuse only
wiring"** — the wiring check is killed at its own declared ceiling and preflight refuses check 4
naming that ceiling; preflight's own total over its ceiling prints a named breach line but still
writes the record, because a refused preflight costs a whole re-run.

## What exists

- `check_wiring` runs `$WIRING_CHECK` through `run_bounded` at `GATE_BOUND` (3600 s, the bar's
  bound), and on a kill refuses check 4 with "did not answer within the declared ${GATE_BOUND}s
  bound". `RB_BOUND` is the per-call override `run_bounded` already takes.
- Precedent for a bound that is a FILE CONSTANT, not a conf key: `REMOTE_BOUND="60"` and the
  `RB_TAIL_*` literals, whose comment says why — a new key owes a protocol key-table row, and the
  protocol is a governance carrier this build may not edit.
- The charter's §7: "COST IS A VERDICT: every suite declares a wall-clock ceiling, a runner REDS on
  breach".

## The mechanism, one

Two declared ceilings and what a breach does: the wiring check's is a kill bound on that one child
with a named refusal; preflight's is a measurement of the verb's own wall, compared once, with a
named breach line. The spec settles:

- WHERE each ceiling is declared and who reads it: "its own declared ceiling" for the wiring check
  can mean a constant in `check-wiring.sh` that the driver cannot read for an arbitrary
  `WIRING_CHECK`, or a driver constant applied to whatever `WIRING_CHECK` names. Pick by M3's rule
  and record the loser; a kit file names nothing outside itself by literal.
- The VALUES, from the build's own A/B measurement after units 1 to 6, on a stated host state —
  never from the 60 s target, which is the goal and not a bound, and never by raising a value to
  make a slow run pass. A ceiling a healthy run on a loaded node breaches every time is noise;
  say what margin over the measured wall the value carries and why.
- The exact wording of the refusal and of the breach line, each naming the ceiling, the measured
  wall and, for the wiring check, that the 3600 s bound is no longer its only kill.
- That preflight's breach line prints whether or not preflight refuses, and never changes its exit.

## Acceptance shape

- A stub `WIRING_CHECK` that sleeps past the ceiling, through a sliced `unattended.test.sh` arm or a
  hermetic probe from that suite's setup: refusal 4 naming the ceiling, the record not written. One
  under the ceiling: no refusal.
- A preflight forced over its own ceiling (a stub that sleeps under the wiring ceiling but past the
  preflight one, or a test seam): the named breach line, `preflight OK`, the record written.
- Witnesses in §6 by basename.

## Conventions

- Tier-2: a new refusal.
- No new `.unattended.conf` key. Lexicon verbs; `gen_map.py --write`; kit versions bumped once at
  the end of the build.
- Order: 4, last.
