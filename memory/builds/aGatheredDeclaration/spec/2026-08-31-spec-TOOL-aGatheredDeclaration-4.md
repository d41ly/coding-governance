# TOOL-aGatheredDeclaration-4 — ceiling enforcement becomes owner opt-in, default OFF

**Status:** OPEN · rev-1 · 2026-08-31 · node a · Tier-2 · base 44734f15 · streams tooling · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Make per-leg ceiling ENFORCEMENT an owner opt-in that ships OFF, in this repo and in everything the
kit ships, while leaving ceiling DECLARATION mandatory. A ceiling kills a leg before it can answer,
and killed legs have cost this fleet reds and re-runs that produced no evidence at all.

## 2. Scope (IN)

- **S1** — `[bar].enforce_ceilings`, declared in `gate-legs.toml`, shipping `false`.
- **S2** — `GATE_CEILINGS=0|1` as the per-machine override, whose absence takes the declared value.
- **S3** — the ANNOUNCEMENT, twice and durably: a banner on stderr before the first leg dispatches
  when enforcement is OFF, and a line in the summary and in `gate-last-summary.txt`. A green earned
  unbounded must never be mistakable for one earned bounded.
- **S4** — the run record gains an `enforce_ceilings` key and its source, so a later reader can tell
  which kind of green a recorded run was.
- **S5** — `gate-full-green` records the enforcement state, and `.githooks/pre-push` treats a stamp
  earned with enforcement OFF as COVERING a push that needs it off, never the reverse. Same
  coverage-not-equality shape the self-test key already has.
- **S6** — `.unattended.conf`'s `GATE_BOUND` — the whole-bar bound the unattended `--close` runs
  under — comes under the same rule: it ships absent, the kit's default applies only when
  enforcement is on, and the driver says on stderr which it used.
- **S7** — the kit's adopter seed declares `enforce_ceilings = false`, so no adopter inherits
  enforcement by arriving.

## 3. Non-goals (OUT)

- Removing ceilings. Declaration stays required; unit 2 keeps `default_ceiling` and every per-leg
  value, and every one of them keeps its comment.
- Changing what a fired ceiling DOES. It still produces `GATE FAIL <leg> (timed out after Ns)` —
  never a skip, never a green. That rule is correct and is not touched.
- The turnstile's TTL, which is derived from the profile row's `timeout=` and not from a leg
  ceiling. `TOOL-aGatheredDeclaration-5` owns the turnstile.
- Auditing the 86 declared ceiling values. With enforcement off they cost nothing; re-deriving them
  is a follow-up worth doing from `<git-dir>/gate-ledger.tsv` once the bar is cheap to shard.

## 4. Design

### Data model

Two inputs, one resolution, printed:

| source | value |
|---|---|
| `GATE_CEILINGS` env | `0` or `1`, outranks everything |
| `[bar].enforce_ceilings` | the declared default, shipping `false` |
| neither | `false` — and the runner says the default was taken |

The existing per-leg bound code is not deleted. It is guarded: when enforcement is off, the leg is
dispatched without its `timeout -k` prefix and its declared ceiling is reported in `--manifest` as
`declared, not enforced`.

### Migration

`.unattended.conf` currently declares `GATE_BOUND="3600"` with a stated derivation. S6 comments it
out rather than deleting it, keeping the derivation and the `TOOL-aBoundedCeiling-6` incident that
motivated it, so re-enabling is uncommenting one line.

**The incident that argued FOR a bound is still true, and this unit is not pretending otherwise.**
An adopter `--close` ran 3h19m with its launching session dead and its inner child at zero CPU, and
nothing in that chain had a deadline. Turning the bound off restores that exposure. The trade is
stated rather than hidden: an unbounded run that hangs costs an operator's attention, while a bound
that fires costs a landing and produces no evidence. The owner has ruled which cost they prefer and
S3's announcement is what keeps the choice visible on every run.

### Rollout

One commit. Rollback is `GATE_CEILINGS=1`, which needs no code change and is why the override exists
ahead of any request for it.

### Files touched (estimate)

`tools/run-gates/run-gates.sh` · `tools/gate-legs.toml` · `.unattended.conf` ·
`tools/unattended/unattended.sh` (the `GATE_BOUND` read) · `.githooks/pre-push` (S5) ·
`tools/run-gates/run-gates.test.sh` · `tools/run-gates/README.md`.

### Alternatives rejected

**Keep enforcement on and raise every ceiling.** This is what the adopter did, twice, and it is what
produced a leg killed at 2041 s against a 2040 s ceiling — a bound raised from a measurement that
was itself 3.07x low. A number derived from one box on one day cannot survive another box under
load, and the failure lands on the run that did everything right.

**A per-leg `enforce` key.** More expressive and unasked for. One switch is what was requested, and
a per-leg opt-out is a follow-up that costs nothing to add later.

## 5. Production-readiness checklist

- security — N/A. No new input reaches an execution sink; `GATE_CEILINGS` is compared as a string
  against `0` and `1` and refused otherwise, never expanded.
- perf / scale — removes the kill-and-rerun cost. A hung leg now costs wall clock instead of a
  landing, which is the trade §4 states.
- a11y, i18n — N/A.
- error / empty / loading states — a `GATE_CEILINGS` value that is not `0` or `1` is exit 2 naming
  it, rather than being read as falsy.
- observability — S3 and S4 are the whole answer. The state is on stderr, in the summary, in
  `gate-last-summary.txt` and in the run record.
- risks — an unbounded hang. Named, accepted, announced. The secondary risk is a stamp confusion,
  which S5 answers with coverage rather than equality.
- testing + left-shift gates — arms below, each observed RED first.
- migration / rollback — one env var, no code change.
- user docs — `tools/run-gates/README.md`'s ceiling section is rewritten; the charter's merge-bar
  section names the switch.

## 6. Acceptance criteria

- **AC1** — When neither `GATE_CEILINGS` nor `[bar].enforce_ceilings` is set, a leg that sleeps past
  its declared ceiling COMPLETES and its row is a pass, asserted in
  `tools/run-gates/run-gates.test.sh` with a scratch leg whose ceiling is 1 s and whose sleep is
  longer, graded on elapsed time against an untimed control rather than on a literal.
- **AC2** — When `GATE_CEILINGS=1`, that same leg is killed and its row is
  `GATE FAIL <leg> (timed out after Ns)`, never a skip and never a pass.
- **AC3** — When enforcement is OFF, a banner naming the state appears on stderr before the first
  leg's verdict, asserted by ordering against the first `GATE ` line in captured output.
- **AC4** — When a run finishes with enforcement OFF, `gate-last-summary.txt` carries a line saying
  so, asserted by grepping the file rather than the stream.
- **AC5** — When `GATE_CEILINGS` holds anything but `0` or `1`, the runner exits 2 naming the value,
  observed RED before the arm is written.
- **AC6** — When a `gate-full-green` stamp was earned with enforcement OFF and a later push needs it
  off, `.githooks/pre-push` accepts it; when the push needs it ON, the hook forces a full run,
  asserted in `.githooks/pre-push.test.sh` in both directions.
- **AC7** — When `.unattended.conf` declares no `GATE_BOUND`, `bash tools/unattended/unattended.sh
  --close <slug>` runs the bar unbounded and says on stderr that no bound was declared, asserted in
  the unattended kit's own suite.
- **AC8** — When `bash tools/run-gates/run-gates.sh --manifest` runs with enforcement off, every
  leg's ceiling column reads `declared, not enforced`, asserted by grepping the output.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `run-gates evidence` · `unattended kit gate` ·
`pre-push hook selftest`. No new leg.

## 8. Open questions

- **F1 — does `enforce_ceilings = false` make the `bounded-through-a-pipe-is-unbounded` gotcha
  class dead?** That class says a wall-clock timeout captured through a command substitution bounds
  the verdict rather than the clock. With enforcement off there is no timeout to mis-capture, so the
  class is unreachable through this path — but it is still reachable through the turnstile TTL and
  through any adopter that turns enforcement on. Recommendation: keep the class, and add a line to
  its record naming this unit as the reason the default path no longer exercises it.
  RESOLVED (agent, 2026-08-31, delegated): keep the class and annotate it. Deleting a gotcha because
  one caller stopped reaching it is the same shape as deleting a gate because nothing currently
  fails it.

## 9. Revision log

- rev-1 · 2026-08-31 · initial draft.

## 10. Reuse audit

**The seam is an adopter's, and it is a whole design rather than a function.**
`C:/projects/incms/main/scripts/gate.sh:53-72` implements exactly this switch: `INCMS_GATE_UNBOUNDED`,
default `0`, validated to `0|1`, with a five-line banner and a summary line. Its header carries the
argument this unit reuses verbatim — a ceiling KILLS a leg before it can answer, so enforcement off
produces strictly more evidence than a ceiling that fired. **The one change on adoption is the
DEFAULT**: inCMS ships bounded with an opt-out, and the owner has ruled this ships unbounded with an
opt-in. That inversion is the only difference and it is stated here so a reader comparing the two
trees does not read it as drift.

`_ceiling()` at `scripts/gate.sh:134-138` is the second half and is adopted as-is in spirit:
declaration stays MANDATORY. gov's runner today COUNTS undeclared ceilings and carries on
(`tools/run-gates/README.md`, "A leg that declares no ceiling runs UNBOUNDED, and is COUNTED rather
than refused") — verified against source. Unit 2's `default_ceiling` is what lets declaration be
mandatory without every leg carrying a number.

`python tools/memory-recall/query.py` with the terms recorded in
`TOOL-aGatheredDeclaration-2` §10 surfaced `TOOL-aBoundedCeiling-6` as the record that ARGUED for
`GATE_BOUND`, and §4 above answers it rather than ignoring it.
