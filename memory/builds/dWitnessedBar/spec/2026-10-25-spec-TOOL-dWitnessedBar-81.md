# TOOL-dWitnessedBar-81 — the byte check's staged reds are one break per condition, each recorded with the line it printed, so units 74 and 76 close on a red that happened

**Status:** OPEN · rev-3 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 41 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-review-TOOL-dWitnessedBar-79-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-79-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 74 to 78
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-74-spec-audit-round1.md`)
confirmed finding **id 1 at HIGH**, report item **H1**. Ids 7 and 18 share that item and take
`TOOL-dWitnessedBar-79` and `TOOL-dWitnessedBar-80`.

`TOOL-dWitnessedBar-74` AC2 stages one break, a `check_cr_reached` whose count reads `-ge 0`, and
expects the line `(it passed a value that lost its CR)`. Its liveness variant fails both conditions,
so that break leaves the variant rejected by the tail test and the line never prints. AC2 is red on a
correct build, and a builder who chases it would take out the tail test. Unit 74's §7 New-arm line
claims the same break reaches that line, and unit 76 AC2 and its New-arm line repeat the claim for
`rec_fp`. Without a record of what each break printed, the ledger would show a seen-red that never
happened.

This unit restates those criteria as one staged break per condition, runs each at the close in a
scratch clone, and records the line each printed in the ledgers of units 74 and 76. The `-ge 0`
break defeats the length condition and must reach `TOOL-dWitnessedBar-79`'s line. A break with no
last-byte test defeats the tail condition and must reach `TOOL-dWitnessedBar-80`'s. It repairs
`TOOL-dWitnessedBar-74` and builds one step after it (order 41).

## 2. Scope (IN)

- **S1** — Two staged breaks, one per condition. At the close, on a Windows node, the main loop runs
  the arm in two scratch clones. In the first, the suite's `check_cr_reached` compares the byte count
  with `-ge 0`, its tail test kept. In the second, it keeps the count at forty-one and holds no
  last-byte test. Observed by AC1.
- **S2** — Each break reaches its own variant and only it. The first break prints
  `TOOL-dWitnessedBar-79`'s line, `(the length variant passed a value one byte short)`, for `rec_sha`
  and for `rec_fp`, and no `tail variant` line. The second prints `TOOL-dWitnessedBar-80`'s line,
  `(the tail variant passed a value whose last byte is not CR)`, for both, and no `length variant`
  line. Observed by AC1.
- **S3** — Unit 74's acceptance ledger beside AC2 records both breaks, each with its printed `rec_sha`
  line, the line it did not print, and the `uname -s` it ran under. The record states that unit 74
  AC2's quoted reason, `it passed a value that lost its CR`, is the one `TOOL-dWitnessedBar-80` S3
  restates as the tail reason, and that its `-ge 0` break reaches the length reason. It names this
  unit. Observed by AC2.
- **S4** — Unit 76's acceptance ledger beside AC2 records the same two breaks with their printed
  `rec_fp` lines, so unit 76's New-arm claim rests on a red each condition showed for `rec_fp`. It
  names this unit. Observed by AC3.

## 3. Non-goals (OUT)

- The variants themselves, which are `TOOL-dWitnessedBar-79`'s and `TOOL-dWitnessedBar-80`'s.
- Rewording the spec text of units 74 and 76. Their AC2 and New-arm claims are answered in their
  ledgers by name, as `TOOL-dWitnessedBar-78` §3 answers units 68 to 73.
- The ledger's physical-line rule for the other units' records, which is `TOOL-dWitnessedBar-84`'s
  for id 16. This unit's own criteria already require it.
- The report's left-shift text, that a staged break states which condition it defeats and its
  expected printed line. No clause of this build names it. S1 and S2 are that statement, made for
  this arm.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-74` — AC2 and the §7 New-arm claim, which S1 restates as one break per condition and S3 answers in that unit's ledger (id 1)
- **consumes-from** `TOOL-dWitnessedBar-76` — AC2 and the §7 New-arm claim for `rec_fp`, which S4 answers in that unit's ledger (id 1)
- **consumes-from** `TOOL-dWitnessedBar-79` — the length variant and its reason, which the first break must reach (ids 1 and 7)
- **consumes-from** `TOOL-dWitnessedBar-80` — the tail variant and its reason, which the second break must reach (ids 1 and 18)
- **hands-off** `TOOL-dWitnessedBar-87` — §1, §4 Evidence and S4's reading of 76 AC2, which unit 87 corrects in this unit's ledger (id 7 of the round-1 spec audit of units 79 to 84)
- **hands-off** `TOOL-dWitnessedBar-88` — S1, AC2, AC3 and S4's records, which unit 88 holds to one platform rule (id 23 of the same audit)
- **hands-off** `TOOL-dWitnessedBar-89` — S3 and S4's break records, which unit 89 marks with `break:` so 88 S19's platform rule selects them alone (id 1 of the round-1 spec audit of units 85 to 88)

## 4. Design

### Evidence

- `spec/2026-10-25-spec-TOOL-dWitnessedBar-74.md` §6 AC2 stages the `-ge 0` break and quotes
  `(it passed a value that lost its CR)`. Its §7 New-arm line claims the same, and `TOOL-dWitnessedBar-76`
  §6 AC2 quotes that reason for `rec_fp`.
- The report's skeptics probed the break on a unit-69-shaped loop: with `-ge 0` and the tail test kept,
  the `${_rg_v%?}` variant's mutant returned 1, so no line printed (ids 1, 7 and 18).
- `TOOL-dWitnessedBar-79` §4 Evidence and `TOOL-dWitnessedBar-80` §4 Evidence record, on this node, a
  length variant ending in `\r` at 40 bytes and a tail variant ending in `x` at 41 bytes, each failing
  one condition. A break that defeats one condition therefore lets exactly one variant pass.
- `memory/gotchas/ledger-token-wrapped-across-a-line-joins-nothing.md` records that a ledger grep
  reads one physical line.

### Inventory

Minted: nothing in code. The ledger records of S3 and S4. No function, constant, plant, flag or
file. Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

At the close, after every unit is terminal. The unit takes order 41 so that it sits beside the
variants it observes. Dispatch sorts a tie by id string (`tools/workflows/unattended-build.js:608-613`),
so units 79 and 80 build before it. Its records are written at the close, when the arm runs.

### Files touched (estimate)

- `memory/builds/dWitnessedBar/build/`

### Alternatives rejected

- **One combined break, `-ge 0` with the tail test taken out, the report's smaller alternative.** It
  shows the arm can red, but not that each condition can, so a vacuous count with the tail test kept
  would still land green.
- **A break that makes `check_cr_reached` return 0 on every value.** Both variants pass it, so the
  record could not say which condition the arm would have caught.

## 5. Production-readiness checklist

- security — no new write path. The scratch clones sit under `%TEMP%`.
- perf / scale — two scratch clones and two arm runs, once, at the close.
- error / empty / loading states — S2 names the line each break must print and the line it must not.
- observability — each record quotes the printed line, so a reader can check it against a rerun.
- risks — a break staged on the wrong condition prints the other variant's line, which S2's second
  clause catches.
- testing — AC1 by scratch clone, AC2 and AC3 by ledger, all at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — In a scratch clone whose suite copy has `check_cr_reached` compare the count with `-ge 0`,
  the arm prints a line holding `(the length variant passed a value one byte short)` for `rec_sha` and
  one for `rec_fp`, and no line holding `tail variant`. In a clone whose `check_cr_reached` holds no
  last-byte test, it prints a line holding
  `(the tail variant passed a value whose last byte is not CR)` for each, and no line holding
  `length variant`.
  Red when: a break reaches the other condition's variant, or reaches none, so its red names no
  condition.
  fixture: scratch clones under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.
- **AC2** — When `grep -n 'AC2' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-74*acceptance-ledger*`
  runs at the close, it prints one line quoting `the length variant passed a value one byte short`
  and one quoting `the tail variant passed a value whose last byte is not CR`, each with `rec_sha`, a
  `uname -s` value beginning `MINGW` or `MSYS`, and `TOOL-dWitnessedBar-81`, all on the line grep
  prints.
  Red when: unit 74 AC2 is recorded red from one break, or from a line no break printed.
  permission: the ledger is written at the close.
- **AC3** — When `grep -n 'AC2' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-76*acceptance-ledger*`
  runs at the close, it prints the same two lines for `rec_fp`, each with a `uname -s` value and
  `TOOL-dWitnessedBar-81` on the line grep prints.
  Red when: unit 76's New-arm claim for `rec_fp` is recorded with no printed line.
  permission: the ledger is written at the close.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

`recall floor` and `recall floor arms` are owed for the ledgers under `memory/`. The two staged
breaks run the `run-gates gov canary` arm in scratch clones at the close; this unit adds no arm and
moves none, so it declares no `New arm:` line.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 74 is itself derived
  and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — How is unit 74 AC2 answered (id 1)?** Options: (a) two breaks, one per condition, each
  recorded with its line, the report's fix; (b) one combined break that defeats both conditions,
  the report's smaller alternative; (c) one break making `check_cr_reached` return 0 regardless.
  (b) and (c) leave a vacuous count with the tail test kept unobserved, which fails unit 74 AC2's
  Red-when, "a vacuous comparison passes with the arm green"; veto 1 discards both. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the one survivor.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 74 to 78, id 1
  (HIGH, item H1, shared with ids 7 and 18).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-87 and TOOL-dWitnessedBar-88, promoted by the round-1 spec audit of
  units 79 to 84; nothing else moved.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-89, the minors batch of the round-1 spec audit of units 85 to 88;
  nothing else moved.

## 10. Reuse audit

The seam is the acceptance ledger of `memory/HYGIENE.md` "Acceptance ledger", as
`TOOL-dWitnessedBar-75` S3 uses it to record unit 70's staged reds with their printed lines; this
unit records two more against the variants of units 79 and 80.
`python tools/codebase-map/reuse_lookup.py "prove each condition of a two-condition check can fail on its own variant"`
ranked `check`, `fail`, `checks` and `check_line`, none a record of a staged break, so no existing
seam fits beyond the ledger named above.

Recall terms used: `python tools/memory-recall/query.py "how is each condition of a canary byte check seen red, and who restates the assertion floor" --terms "canary liveness variant length tail CR byte check FLOOR_ASSERTIONS restated floor owner seen red"`
