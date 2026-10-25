# TOOL-dWitnessedBar-77 — the canary's failure line names `rec_fp` when the `fingerprint` CR did not arrive, and unit 72's red is recorded with that line

**Status:** OPEN · rev-3 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 41 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 |
| [2026-10-25-review-TOOL-dWitnessedBar-74-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-74-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-78 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 68 to 73
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-68-spec-audit-round1.md`)
confirmed finding **id 25 at HIGH**, report item **H2**. Id 9 shares that item and takes
`TOOL-dWitnessedBar-76`. Report items M2 and L2, ids 1 and 17, describe the failure line's two
spellings at MEDIUM and LOW, and `TOOL-dWitnessedBar-78` takes them.

`TOOL-dWitnessedBar-72` S1, §5 and AC1 say unit 70 S2's failure line names `rec_fp`. Unit 70 S2 fixes
that line as text with no variable, and unit 72's Inventory mints nothing. So AC1 either fails on a
correct build, or a builder makes every count failure name `rec_fp`, which grades nothing about
`rec_fp`. Either way a canary that never checks `rec_fp` can pass AC1.

`TOOL-dWitnessedBar-75` gives the line a slot naming the check that failed. This unit gives the slot
its `rec_fp` value, prints one line per variable whose CR did not arrive, and records unit 72 AC1's
staged red with the line it printed. It repairs `TOOL-dWitnessedBar-72` and builds one step after it
(order 41), after `TOOL-dWitnessedBar-76` within that order.

## 2. Scope (IN)

- **S1** — The slot's `rec_fp` value. When the canary's count holds, the arm prints unit 75 S1's line
  once for each variable `TOOL-dWitnessedBar-76`'s `check_canary_keys` names on the canary's mutant,
  with that variable in `<what>`. A `fingerprint` CR that did not arrive prints
  `gov-canary: the planted CR never reached read_green_file on <uname -s> for rec_fp; the CR-strip assertion is not counted`,
  and unit 67 S2's assertion is not counted. A count failure prints only unit 75's `count <n>` line,
  never a variable. Observed by AC1.
- **S2** — Unit 72 AC1's staged red is recorded with its line. At the close, on a Windows node, the
  main loop stages `TOOL-dWitnessedBar-76` S3's `fingerprint` variant in a scratch clone's
  `.githooks/pre-push`. Unit 72's acceptance ledger records it beside AC1 with the printed line, which
  holds `for rec_fp`, the absence of any line holding `for rec_sha` or `for count`, and the `uname -s`
  it ran under. Observed by AC2.

## 3. Non-goals (OUT)

- The slot itself and its `count <n>` and `rec_sha` values, which are `TOOL-dWitnessedBar-75`'s.
- The per-key liveness check and `check_canary_keys`, which are `TOOL-dWitnessedBar-76`'s.
- Unit 72's §4 Inventory and §5 observability line answered in its ledger, and the strip-less
  break's two printed lines recorded for unit 72 AC3, which are `TOOL-dWitnessedBar-78`'s for ids 17
  and 1.
- The report's left-shift text, a checklist entry that a criterion requiring a printed line to name a
  value cites a line with a slot for it. No clause of this build names it.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-72` — S1's claim that the canary's failure line names `rec_fp`, and AC1's red, which S1 makes true and S2 records (id 25)
- **consumes-from** `TOOL-dWitnessedBar-75` — the `for <what>` slot and its one emission site, to which S1 adds the `rec_fp` value (ids 25 and 24)
- **consumes-from** `TOOL-dWitnessedBar-76` — `check_canary_keys`, whose output S1 prints one line per variable, and the `fingerprint` variant S2 stages (ids 25 and 9)
- **hands-off** `TOOL-dWitnessedBar-78` — unit 72's Inventory and observability line answered with the `rec_fp` value, and the strip-less break's printed lines recorded for unit 72 AC3 (ids 1 and 17)
- **hands-off** `TOOL-dWitnessedBar-82` — the New-arm claim, which unit 82's restated floor answers in this unit's ledger (id 2 of the round-1 spec audit of units 74 to 78, item H2)
- **hands-off** `TOOL-dWitnessedBar-84` — S1's count line and the ledger lines for AC1 and AC2, kept on one physical line and cited by section label (ids 4, 11, 16 of the round-1 spec audit of units 74 to 78)
- **hands-off** `TOOL-dWitnessedBar-88` — S2's staged `fingerprint` variant, which unit 88 names by its current text in unit 72's ledger (id 13 of the round-1 spec audit of units 79 to 84)

## 4. Design

### Evidence

- `spec/2026-10-25-spec-TOOL-dWitnessedBar-70.md:43-47` fixes S2's line with no slot.
  `spec/2026-10-25-spec-TOOL-dWitnessedBar-72.md:37-40`, `:103` and `:111-115` say that line names
  `rec_fp`, and `:75` reads "Minted: nothing".
- `TOOL-dWitnessedBar-76` §4 Evidence: the `fingerprint` variant's mutant gives `rec_sha` 41 bytes and
  `rec_fp` 40, so `check_canary_keys` names `rec_fp` alone on it.
- The report's corrected fix for id 25 keeps unit 70 AC2's prefix and puts the variable after the
  `uname -s` value, which unit 75 S1's slot does.

### Inventory

Minted: the `rec_fp` value of `TOOL-dWitnessedBar-75`'s `for <what>` slot. No function, constant,
plant, flag or file. Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 41, after `TOOL-dWitnessedBar-72` (40) and `TOOL-dWitnessedBar-75` (40).
Order 41 is shared with `TOOL-dWitnessedBar-73` and `TOOL-dWitnessedBar-76`. Dispatch is strictly
sequential and sorts a tie by id string (`tools/workflows/unattended-build.js:608-613`), so this unit
builds last of the three, after unit 76, whose function and variant it reads.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`

### Alternatives rejected

- **Give `rec_fp` its own line, outside unit 75's slot.** It would be a second emission site for one
  failure, the shape unit 75 S2 rules out.
- **Print one line naming every failing variable.** A record could then not show that the
  `fingerprint` break named `rec_fp` alone, which S2 records.

## 5. Production-readiness checklist

- security — no new write path.
- perf / scale — none: one line per failing variable, at most two.
- error / empty / loading states — S1 keeps a count failure from naming a variable it never read.
- observability — the line names `rec_fp` when its CR did not arrive.
- risks — none beyond unit 75's.
- testing — AC1 by scratch clone at the close, AC2 by ledger at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — In a scratch clone whose `.githooks/pre-push` carries `TOOL-dWitnessedBar-76` S3's
  `fingerprint` variant, the arm prints `gov-canary: the planted CR never reached read_green_file on `
  followed by the `uname -s` value and ` for rec_fp;`, and no line holding `for rec_sha` or
  `for count`. In a clone whose `read_green_file` holds no `%$'\r'`, it prints the `for count 0` line
  and no line holding `for rec_fp`.
  Red when: the canary checks `rec_sha` alone, or a count failure is printed naming `rec_fp`.
  fixture: scratch clones under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.
- **AC2** — When `grep -n 'AC1' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-72*acceptance-ledger*`
  runs at the close, a red record quotes a line holding `for rec_fp` and a `uname -s` value beginning
  `MINGW` or `MSYS`, states that no `for rec_sha` or `for count` line printed, and names
  `TOOL-dWitnessedBar-77`.
  Red when: unit 72 AC1's red is recorded with no printed line, or on a line that names no variable.
  permission: the arm's run is the main loop's, at the close.

## 7. Gates

`run-gates gov canary` · `memory hygiene`

`run-gates gov canary` is held unless the main loop sets GATE_SELFTESTS at the close
(`tools/run-gates/run-gates.sh:3129-3131`), which `SELFTESTS_OWED_PATHS="tools/"` does
(`.unattended.conf:40`).

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 · the slot's `rec_fp` value, one line per failing variable, staged red by `TOOL-dWitnessedBar-76`'s `fingerprint` variant in the hook (reaches `for rec_fp`) and by a hook whose `read_green_file` holds no strip (reaches `for count 0` with no `rec_fp` line) · none, the floor is stated by `TOOL-dWitnessedBar-73` S15

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 72 is itself derived
  and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 68 to 73, id 25
  (HIGH, item H2, shared with id 9).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-82 and TOOL-dWitnessedBar-84, promoted by the round-1 spec audit of
  units 74 to 78; nothing else moved.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-88, promoted by the round-1 spec audit of units 79 to 84; nothing else
  moved.

## 10. Reuse audit

The seam is `TOOL-dWitnessedBar-75`'s slotted failure line and its one emission site in
`tools/run-gates/run-gates.gov.test.sh`, given one more value, fed by `TOOL-dWitnessedBar-76`'s
`check_canary_keys`.
`python tools/codebase-map/reuse_lookup.py "prove a byte comparison can fail by running it on a variant that loses the byte"`
ranked `fail`, `stage_or_fail`, `print_fail` and `no_row_loss`, none a failure line naming a
variable, so no existing seam fits beyond the line named above.

Recall terms used: `python tools/memory-recall/query.py "how is a canary assertion proven able to fail on every run rather than once at the close" --terms "canary liveness variant mutant staged red byte check rec_sha rec_fp CR strip seen red failure line"`
