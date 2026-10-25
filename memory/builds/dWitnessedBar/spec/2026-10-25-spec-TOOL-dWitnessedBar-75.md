# TOOL-dWitnessedBar-75 — the CR-reach canary's failure line names the check that failed, so a red at its line count cannot pass for a red at its byte check

**Status:** DEFERRED · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 40 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-75-deviation-751.md](../build/2026-10-25-build-TOOL-dWitnessedBar-75-deviation-751.md) | deviation | — |
| [2026-10-25-review-TOOL-dWitnessedBar-74-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-74-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 68 to 73
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-68-spec-audit-round1.md`)
confirmed finding **id 24 at HIGH**, report item **H1**. Id 10 shares that item and takes
`TOOL-dWitnessedBar-74`.

`TOOL-dWitnessedBar-70` S2 prints one fixed line for every way the canary fails, and its AC2 demands
that same line for both of its staged breaks. A break that trips the one-line count and a break that
reaches the 41-byte comparison therefore print the same bytes. AC2 passes whichever check fired, and
no record shows the comparison went red.

This unit gives the line a slot naming the check that failed, keeps unit 70 AC2's prefix, and records
each of unit 70 AC2's breaks with the line it printed. It repairs `TOOL-dWitnessedBar-70` and builds
one step after it (order 40), after `TOOL-dWitnessedBar-74` within that order.

## 2. Scope (IN)

- **S1** — The slot. Unit 70 S2's line reads
  `gov-canary: the planted CR never reached read_green_file on <uname -s> for <what>; the CR-strip assertion is not counted`.
  `<what>` is `count <n>` when the mutant changed `<n>` lines and `<n>` is not 1. It is the variable's
  name, `rec_sha`, when the count held and `TOOL-dWitnessedBar-74`'s `check_cr_reached` returned non-zero
  for it. The text up to and including `on <uname -s>` is unit 70 AC2's prefix, unchanged. Observed
  by AC1 and AC2.
- **S2** — One emission site, one check per failure. The suite prints the line from one statement,
  with `<what>` passed as a value, so the line has one spelling. When the count fails, the byte
  comparison is not run, and only the `count <n>` line prints. Observed by AC1 and AC2.
- **S3** — Unit 70 AC2's staged reds are recorded with the line each printed. At the close, on a
  Windows node, the main loop stages two breaks in a scratch clone: a `.githooks/pre-push` whose
  `read_green_file` holds no `%$'\r'`, and one carrying `TOOL-dWitnessedBar-74` S2's `sha` variant.
  Unit 70's acceptance ledger records each beside AC2 with its printed line, `for count 0` and
  `for rec_sha` respectively, and the `uname -s` it ran under. Observed by AC3.

## 3. Non-goals (OUT)

- The slot's `rec_fp` value, and unit 72's break recorded with its line. Both are
  `TOOL-dWitnessedBar-77`'s.
- The liveness variant and `check_cr_reached`, which are `TOOL-dWitnessedBar-74`'s.
- Whether unit 66 S2's own assertion still runs and prints after the canary fails, which
  `TOOL-dWitnessedBar-78` S1 states for id 1.
- The report's left-shift text, a checklist entry that a criterion requiring a printed line to name a
  value cites a line with a slot for it. No clause of this build names it. S2's one emission site is
  the regression this unit builds.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-70` — S2's failure line and AC2's two breaks, which S1 gives a slot and S3 records with their printed lines (id 24)
- **consumes-from** `TOOL-dWitnessedBar-74` — `check_cr_reached`, whose return decides the `rec_sha` value, and S2's `sha` variant, which S3 stages as the byte-arm break (ids 24 and 10)
- **hands-off** `TOOL-dWitnessedBar-77` — the slot's `rec_fp` value and the record of unit 72 AC1's break with the line it printed (ids 24 and 25)
- **hands-off** `TOOL-dWitnessedBar-78` — the strip-less break's ledger lines for unit 70 AC3 and unit 72 AC3, which quote this line beside the compare's own, and unit 72's Inventory answered with the slot (ids 1 and 17)
- **hands-off** `TOOL-dWitnessedBar-84` — the slot's `unread` value for a read failure, and the ledger lines for AC2 and AC3 kept on one physical line and cited by section label (ids 11, 16, 19 of the round-1 spec audit of units 74 to 78)

## 4. Design

### Evidence

- `spec/2026-10-25-spec-TOOL-dWitnessedBar-70.md:43-47` fixes S2's line with no slot, and AC2
  (`:143-148`) expects that line for both of its plants.
- A function holding no `%$'\r'` leaves the canary's `sed` nothing to change: the report's verdict on
  id 1 records a probe printing 0 changed lines, so that break trips the count.
- On this node, a prototype carrying `TOOL-dWitnessedBar-74` S2's `sha` variant passed the canary's
  count with one changed line, and its mutant gave `rec_sha` 40 bytes (that spec's §4 Evidence). So
  the two breaks of S3 reach different checks.
- The suite prints each failure with `echo "gov-canary: ..."` and sets `fail=1`
  (`tools/run-gates/run-gates.gov.test.sh:212`).

### Inventory

Minted: the `for <what>` slot of unit 70 S2's line, with the values `count <n>` and `rec_sha`. No
function, constant, plant, flag or file. Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 40, after `TOOL-dWitnessedBar-70` (39). Order 40 is shared with
`TOOL-dWitnessedBar-71`, `TOOL-dWitnessedBar-72` and `TOOL-dWitnessedBar-74`. Dispatch is strictly
sequential and sorts a tie by id string (`tools/workflows/unattended-build.js:608-613`), so this unit
builds last of the four, after unit 74, whose function and variant it reads.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`

### Alternatives rejected

- **A count-failure line with its own prefix.** Unit 70 AC2 grades the prefix
  `...read_green_file on ` followed by the `uname -s` value for both of its breaks, so a second prefix
  leaves AC2 unmet on the count break.
- **Keep one line and record which check fired in the ledger alone.** The ledger would then carry a
  distinction the arm never printed, so the record could not be checked against the run.

## 5. Production-readiness checklist

- security — no new write path.
- perf / scale — none: the slot is a value in an existing line.
- error / empty / loading states — S1 names both failure modes, and S2 keeps a count failure from
  also reporting a byte failure it never measured.
- observability — the slot names the check, so a red record says which assertion fired.
- risks — a reader of the old line's exact text would miss the slot; AC1's grep finds the one site.
- testing — AC1 by grep, AC2 by scratch clone at the close, AC3 by ledger at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When `grep -c 'the planted CR never reached read_green_file on' tools/run-gates/run-gates.gov.test.sh`
  runs on the built tree, it prints 1, and that line passes `<what>` as a variable.
  Red when: two statements print the line, so it can be spelled two ways.
- **AC2** — In a scratch clone whose `.githooks/pre-push` has a `read_green_file` holding no
  `%$'\r'`, the arm prints `gov-canary: the planted CR never reached read_green_file on ` followed by
  the `uname -s` value and ` for count 0;`, and no line holding `for rec_sha`. In a clone carrying
  `TOOL-dWitnessedBar-74` S2's `sha` variant in the hook, it prints the same prefix with
  ` for rec_sha;`, and no line holding `for count`.
  Red when: the two breaks print the same line.
  fixture: scratch clones under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.
- **AC3** — When `grep -n 'AC2' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-70*acceptance-ledger*`
  runs at the close, it prints one red record quoting `for count 0` and one quoting `for rec_sha`, each
  with a `uname -s` value beginning `MINGW` or `MSYS`, and each naming `TOOL-dWitnessedBar-75`.
  Red when: a staged break is recorded with no printed line, or both records quote the same line.
  permission: the arm's run is the main loop's, at the close.

## 7. Gates

`run-gates gov canary` · `memory hygiene`

`run-gates gov canary` is held unless the main loop sets GATE_SELFTESTS at the close
(`tools/run-gates/run-gates.sh:3129-3131`), which `SELFTESTS_OWED_PATHS="tools/"` does
(`.unattended.conf:40`).

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 AC2 · the slotted failure line, staged red by a hook whose `read_green_file` holds no strip (reaches `for count 0`) and by `TOOL-dWitnessedBar-74`'s `sha` variant in the hook (reaches `for rec_sha`) · none, the floor is stated by `TOOL-dWitnessedBar-73` S15

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 70 is itself derived
  and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — What form does the slot take (id 24)?** Options: (a) ` for <what>` after the `uname -s` value,
  `<what>` a count or a variable name, the report's corrected fix for item H2; (b) a parenthesised
  `(<var>|no strip line to mutate)`, the corrected fix for item M2; (c) a separate count-failure line.
  (c) fails unit 70 AC2's shared prefix (§4 Alternatives rejected); veto 1 discards it. (b) cannot
  report a count of two, the shape the report's probes found. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the most feature-rich survivor, since it names every count.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 68 to 73, id 24
  (HIGH, item H1, shared with id 10).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-84, promoted by the round-1 spec audit of units 74 to 78; nothing else
  moved.

## 10. Reuse audit

The seam is unit 70 S2's failure line in `tools/run-gates/run-gates.gov.test.sh`, extended by a slot
in place, and the suite's `echo "gov-canary: ..."` plus `fail=1` idiom (`:212`).
`python tools/codebase-map/reuse_lookup.py "prove a byte comparison can fail by running it on a variant that loses the byte"`
ranked `fail`, `stage_or_fail`, `print_fail` and `no_row_loss`, none a failure line naming the check
that fired, so no existing seam fits beyond the line named above.

Recall terms used: `python tools/memory-recall/query.py "how is a canary assertion proven able to fail on every run rather than once at the close" --terms "canary liveness variant mutant staged red byte check rec_sha rec_fp CR strip seen red failure line"`
