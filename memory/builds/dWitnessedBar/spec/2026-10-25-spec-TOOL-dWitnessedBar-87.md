# TOOL-dWitnessedBar-87 — unit 76 AC2's own break, a canary that skips `rec_fp`, is staged after unit 80 and recorded with the two lines it now prints

**Status:** CLOSED · rev-5 · 2026-11-21 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 42 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 TOOL-dWitnessedBar-106 TOOL-dWitnessedBar-107 TOOL-dWitnessedBar-108 TOOL-dWitnessedBar-109 TOOL-dWitnessedBar-110 |
| [2026-10-25-build-TOOL-dWitnessedBar-87-deviation-871.md](../build/2026-10-25-build-TOOL-dWitnessedBar-87-deviation-871.md) | deviation | — |
| [2026-10-25-build-TOOL-dWitnessedBar-87-deviation-872.md](../build/2026-10-25-build-TOOL-dWitnessedBar-87-deviation-872.md) | deviation | — |
| [2026-11-19-build-TOOL-dWitnessedBar-87-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-87-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-87-1-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-87-1-builder-return.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-87-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-87-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-87-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-87-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-87-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-87-reground-spec-writer.md) | journal | — |
| [2026-10-25-review-TOOL-dWitnessedBar-85-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-85-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-88 |
| [2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md](../reviews/2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md) | diff-review | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 79 to 84
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-79-spec-audit-round1.md`)
confirmed finding **id 7 at HIGH**, report item **H2**. Ids 2 and 12 are the same defect found at a
medium grade, item M1, and `TOOL-dWitnessedBar-88` takes them.

`TOOL-dWitnessedBar-76` S3 prints the reason `it passed a value that lost its CR` when `<var>` is
absent from `check_canary_keys`'s output, and 76 AC2 stages a `check_canary_keys` that skips `rec_fp`
and expects exactly that line; 76's New-arm line repeats it. `TOOL-dWitnessedBar-80` S3 gives the tail
variant its own reason in that place, and units 79 and 80 leave the loop holding only the length and
tail variants. With `rec_fp` skipped, each of them prints its own reason for `rec_fp`, so 76 AC2's
line can no longer print. Unit 76's ledger beside AC2 records that line from a probe made before
units 79 and 80 landed. `TOOL-dWitnessedBar-81` §1 reads 76 AC2 and its New-arm line as repeating
unit 74 AC2's claim, a `check_cr_reached` break, and 81 S4 records only the per-condition breaks
beside it. 81's rev-4 §4 Evidence names the skip, but no scope item of 81 stages it. Nothing answers
the break 76 AC2 actually stages, so 76 AC2 is red on a correct build, and a builder chasing it would bring the
old reason back against unit 80.

This unit stages that break after units 79 and 80 land and records, in unit 76's ledger, the two
lines it prints. It corrects 81's reading of 76 AC2 in 81's ledger. It repairs
`TOOL-dWitnessedBar-81` and builds one step after it (order 42).

## 2. Scope (IN)

- **S1** — Unit 76 AC2's break, staged. At the close the main loop runs the arm in a scratch clone of
  the built tree whose suite copy has `check_canary_keys` skip `rec_fp`, the break 76 AC2 names. The
  arm prints, for `rec_fp`, a line holding `(the length variant passed a value one byte short)` and a
  line holding `(the tail variant passed a value whose last byte is not CR)`, prints no line holding
  `it passed a value that lost its CR` and no `rec_sha byte check was not seen red` line, and exits
  non-zero. Observed by AC1.
- **S2** — Unit 76 answered. Unit 76's acceptance ledger beside AC2, the criterion its New-arm line
  covers, records S1's two printed `rec_fp` lines. It states that `TOOL-dWitnessedBar-80` S3's tail
  reason and `TOOL-dWitnessedBar-79` S3's length reason are what 76 AC2's break reaches once those
  units land, in place of the quoted `it passed a value that lost its CR`, and names this unit.
  Observed by AC2.
- **S3** — Unit 81's reading corrected. Unit 81's acceptance ledger beside AC3 records that 76 AC2
  stages a `check_canary_keys` that skips `rec_fp`, not the `check_cr_reached` break 81 §1 reads it
  as repeating; that 81 S4's records beside 76 AC2 are the per-condition breaks for `rec_fp`; and
  that 76 AC2's own break is answered by this unit's S2. It names this unit. Observed by AC3.

## 3. Non-goals (OUT)

- Whether unit 76 S3's other reason, `it named <other> whose CR arrived`, applies to each new variant,
  and the length variant's reason when another variable is named. Those are ids 12 and 20, which
  `TOOL-dWitnessedBar-88` takes, together with id 2's inventory of every reader of the reason unit 80
  stands in place of.
- Rewording the spec text of units 76 and 81. Their claims are answered in their ledgers by name, as
  `TOOL-dWitnessedBar-78` §3 answers units 68 to 73.
- The variants and their reasons, which are `TOOL-dWitnessedBar-79`'s and `TOOL-dWitnessedBar-80`'s.
- The report's left-shift text, a checklist entry that a unit retiring a printed reason answers every
  reader by name, and a hygiene check for a quoted failure line no live spec defines. No clause of this
  build names them. S1 to S3 are that answer, made for this reason.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-76` — AC2's skip-`rec_fp` break and its New-arm claim, which S1 stages and S2 answers in that unit's ledger (id 7)
- **consumes-from** `TOOL-dWitnessedBar-79` — the length variant's reason, which S1 requires for `rec_fp` (id 7)
- **consumes-from** `TOOL-dWitnessedBar-80` — S3's tail reason, which stands where 76 AC2's quoted reason stood and which S1 requires for `rec_fp` (id 7)
- **consumes-from** `TOOL-dWitnessedBar-81` — §1 and S4's reading of 76 AC2, which S3 corrects in that unit's ledger; its rev-4 §4 Evidence already names the skip (id 7)
- **hands-off** `TOOL-dWitnessedBar-88` — the other-variable reason for the new variants and the inventory of the readers of 76 S3's absent-variable reason, ids 2, 12 and 20 of the same audit
- **hands-off** `TOOL-dWitnessedBar-89` — S1's staged break, §4 Evidence and S2's ledger lines, which unit 89 pins against 84 S14, corrects and grades line by line (ids 2, 5 and 6 of the round-1 spec audit of units 85 to 88)
- **hands-off** `TOOL-dWitnessedBar-90` — S2's statement and two `rec_fp` lines beside 76 AC2, and AC2's token list, which unit 90 keeps outside its selection and supersedes for the length line (ids 1 and 2 of the round-1 spec audit of unit 89)
- **hands-off** `TOOL-dWitnessedBar-92` — its ledger's `- AC2` answer, under which unit 92 places unit 90 S6's note as a labelled continuation line and counts the answer exactly (ids 3 and 11 of the round-1 spec audit of unit 90)

## 4. Design

### Evidence

Read at `6381c364f` on 2026-11-21. Units 76, 79, 80 and 81 are CLOSED.

- `spec/2026-10-25-spec-TOOL-dWitnessedBar-76.md` rev-4 S3 defines `it passed a value that lost its
  CR` for an absent `<var>`, AC2 stages a `check_canary_keys` that skips `rec_fp` and quotes that
  line, and its §7 New-arm line claims the same.
- `spec/2026-10-25-spec-TOOL-dWitnessedBar-80.md` rev-4 S3 gives the tail variant the reason
  `the tail variant passed a value whose last byte is not CR`, and names unit 74 AC2's quote as
  answered by unit 81 and unit 76 AC2's as answered by this unit.
- `spec/2026-10-25-spec-TOOL-dWitnessedBar-79.md` S3 gives the length variant the reason
  `the length variant passed a value one byte short` when its mutant passes `<var>`'s byte check.
- `spec/2026-10-25-spec-TOOL-dWitnessedBar-81.md` rev-4 §1 says unit 76 AC2 and its New-arm line
  "repeat the claim" of unit 74 AC2, whose rev-3 break is a `check_cr_reached` comparing `true`. Its
  §4 Evidence names 76 AC2's skip of `rec_fp`, and its S4 records the `-ge 0` and no-tail breaks
  beside 76 AC2.
- As landed, the per-key loop calls `check_key_variant` with the tail reason, then the length reason
  (`tools/run-gates/run-gates.gov.test.sh@6381c364f:947-951`). A variant whose mutant's
  `check_canary_keys` output lacks `<var>` prints that call's passed reason
  (`tools/run-gates/run-gates.gov.test.sh@6381c364f:895`). With `rec_fp` skipped, `rec_fp` is absent
  for both its variants, and `rec_sha`'s variants are untouched.
  `grep -c 'lost its CR' tools/run-gates/run-gates.gov.test.sh` prints 0 (PINNED 2026-11-21).
- A spec-writer probe at `6381c364f` sourced `check_cr_reached` through `check_key_variant` and the
  liveness loop over a hand-built AC12-shaped record, with `check_canary_keys` skipping `rec_fp` in
  one `diff` line. It printed the `rec_fp` line with the tail reason, then with the length reason, no
  other line, `fail` 1, `rgf_seen` ` rec_sha` (DERIVED from that probe, 2026-11-21). It is not S1's
  clone run.
- `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-76-1-acceptance-ledger.md`
  beside AC2 records the skip printing `it passed a value that lost its CR` over unit 76's slice, and
  owes the clone run to the close. Unit 81's ledger marks its AC3, the 76-ledger records, OWED.
- `memory/gotchas/ledger-token-wrapped-across-a-line-joins-nothing.md` records that a ledger grep
  reads one physical line.

### Inventory

Minted: nothing in code. The ledger records of S2 and S3. No function, constant, plant, flag or
file. Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

At the close, after every unit is terminal. The unit takes order 42, one above unit 81's 41, so it
sits after units 76, 79, 80 and 81, CLOSED at `bdc10a4df`, `08f226f3d`, `a967359a8` and
`dc1205950`, whose reasons and records it reads. Order 42's other unit, `TOOL-dWitnessedBar-78`,
CLOSED at `253e21771`, so this unit closes order 42 and builds alone. Its records are written at the
close, when the arm runs, after unit 81's records beside 76 AC2.

### Files touched (estimate)

- `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-76-1-acceptance-ledger.md`:
  S2's records and statement, beside AC2.
- `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-81-1-acceptance-ledger.md`:
  S3's record, beside AC3.
- This unit's own acceptance ledger, a new record in the same build directory, named by the pass's
  date as every builder's ledger is.

No code file and no other record.

### Alternatives rejected

- **Answer 76 AC2 with unit 81's per-condition breaks.** Those breaks edit `check_cr_reached`, not
  `check_canary_keys`, so they never show what a canary that checks `rec_sha` alone prints, which is
  76 AC2's Red-when.
- **Keep 76 S3's absent-variable reason beside the variants' own reasons.** It would print a reason
  that names no condition next to two that do, which unit 80 S3 exists to stop.

## 5. Production-readiness checklist

- security — no new write path. The scratch clone sits under `%TEMP%`.
- perf / scale — one scratch clone and one arm run, once, at the close.
- error / empty / loading states — S1 names the two lines the break must print and the two it must not.
- observability — each record quotes the printed line, so a reader can check it against a rerun.
- risks — a builder who stages the break on `rec_sha` reads `rec_sha` lines; S1 names `rec_fp` and
  requires no `rec_sha` line.
- testing — AC1 by scratch clone, AC2 and AC3 by ledger, all at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — In a scratch clone of the built tree whose suite copy has `check_canary_keys` skip
  `rec_fp`, the arm prints a `rec_fp` line holding `(the length variant passed a value one byte short)`
  and one holding `(the tail variant passed a value whose last byte is not CR)`, prints no line
  holding `lost its CR` and none holding `rec_sha byte check`, and exits non-zero.
  Red when: the break prints the reason unit 80 stands in place of, or reaches `rec_sha`.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.
- **AC2** — When `grep -n 'AC2' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-76*acceptance-ledger*`
  runs at the close, it prints one line quoting `the length variant passed a value one byte short` and
  one quoting `the tail variant passed a value whose last byte is not CR`, each with `rec_fp`,
  `TOOL-dWitnessedBar-80` and `TOOL-dWitnessedBar-87` on the line grep prints. The records
  `TOOL-dWitnessedBar-81` S4 writes beside the same AC2 carry 81, not 87, and are not these lines.
  Red when: unit 76 AC2 is recorded from a break it does not stage, or against a line no run printed.
  permission: the ledger is written at the close.
- **AC3** — When `grep -n 'skip' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-81*acceptance-ledger*`
  runs at the close, it prints a line naming `check_canary_keys`, `rec_fp`, `TOOL-dWitnessedBar-76` AC2
  and `TOOL-dWitnessedBar-87`.
  Red when: unit 81's ledger certifies its per-condition breaks, the `-ge 0` count among them, as
  76 AC2's with no correction beside it.
  permission: the ledger is written at the close.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

`recall floor` and `recall floor arms` are owed for the ledgers under `memory/`. S1 runs the
`run-gates gov canary` arm in a scratch clone at the close; this unit adds no arm and moves none, so
it declares no `New arm:` line.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 81 is itself derived
  and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Which unit does this promotion repair, and so where does it sit (id 7)?** Options: (a) unit
  81, whose §1 and S4 the finding locates first, order 42; (b) unit 80, whose S3 sets the reason in
  place, order 42 too; (c) unit 76, whose AC2 goes red, order 42 too. All three sit at order 41, so
  the order is the same; the repaired unit decides only which spec the record names. (a) is the spec
  whose reading the fix corrects. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, tie-broken by
  fewer open questions.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 79 to 84, id 7
  (HIGH, item H2; ids 2 and 12 are its medium-graded item M1).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-89, the minors batch of the round-1 spec audit of units 85 to 88;
  nothing else moved.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-90, the minors batch of the round-1 spec audit of unit 89; nothing else
  moved.
- rev-4 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-92, the minors batch of the round-1 spec audit of unit 90; nothing else
  moved.
- rev-5 · 2026-11-21 · §1 · S3 · §3 · §4 · AC2 · AC3 · re-grounded at `6381c364f` under
  `2026-11-19-prompt-TOOL-dWitnessedBar-87-reground-brief`: unit 81's rev-4 §1 reading and §4
  Evidence, unit 80's rev-4 S3 answer, the landed loop and a probe of the skip, Rollout's CLOSED
  shas, Files touched listed exactly, and AC2 told apart from 81 S4's records; intent unchanged.

## 10. Reuse audit

The seam is the acceptance ledger of `memory/HYGIENE.md` "Acceptance ledger", as
`TOOL-dWitnessedBar-81` uses it to record each staged break with its printed line; this unit records
one more break, 76 AC2's own.
`python tools/codebase-map/reuse_lookup.py "record a staged break with the failure line it printed"`
ranked `records`, `check_line`, `render_line` and `extract_records`, none a record of a staged break
with its printed line, so no existing seam fits beyond the ledger named above.

Recall terms used: `python tools/memory-recall/query.py "which reader quotes a canary failure reason that a later unit stands another reason in place of" --terms "canary liveness reason rec_fp check_canary_keys skip staged break ledger answered retired reason reader"`
