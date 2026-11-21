# TOOL-dWitnessedBar-86 — a suite run with either liveness variant missing is seen below the floor, and the floor claims of units 79, 80 and 82 are recorded against that red

**Status:** DEFERRED · rev-3 · 2026-11-21 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 44 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-86-deviation-861.md](../build/2026-10-25-build-TOOL-dWitnessedBar-86-deviation-861.md) | deviation | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-86-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-86-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-86-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-86-reground-spec-writer.md) | journal | — |
| [2026-10-25-review-TOOL-dWitnessedBar-85-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-85-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-88 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 79 to 84
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-79-spec-audit-round1.md`)
confirmed finding **id 17 at HIGH**, report item **H1**. Id 1 shares that item and takes
`TOOL-dWitnessedBar-85`.

`TOOL-dWitnessedBar-82` S2, AC2 and its New-arm line say the restated floor sees unit 79's length
variant deleted: a suite copy lacking it prints `below the pinned floor`. The New-arm lines of units 79
and 80 say their variants are covered by the floor 82 S1 restates after them. No spec had observed
what `a` does when a variant is missing, and the report's skeptics found that it does not move, so
those claims certified coverage nobody had seen.

Unit 85 makes each variant count. This unit runs the observation the report asks for: at the close,
a suite with the length variant missing and one with the tail variant missing are each seen below
the floor, by exactly the count unit 85 adds, and the same copy at unit 82's own pass is recorded
passing. The claims of units 79, 80 and 82 are answered in their ledgers against those lines. It
repairs `TOOL-dWitnessedBar-82` and builds after `TOOL-dWitnessedBar-85`, the last unit of order 44.

## 2. Scope (IN)

- **S1** — Two staged absences at the close. The main loop runs the arm in two scratch clones of the
  built tree. In the first, the suite copy's liveness loop runs no length variant: its
  `check_key_variant` call with the replacement `${_rg_v:1}`, that line and its continuation line, is
  absent. In the second, the call with the replacement `${_rg_v%?}x` is absent in the same way. Each
  prints `gov-canary: executed <n> assertions, below the pinned floor <floor>` and exits non-zero,
  with `<floor>` minus `<n>` equal to the number of words in `${CANARY_KEYS[*]}`. Neither prints a
  `length variant` or `tail variant` reason line, so the floor line is the red that sees the absence.
  Observed by AC1.
- **S2** — The same absence before unit 85. In a scratch clone checked out at unit 82's pass commit,
  which `build_commit` answers, the suite copy with no length variant prints `PASS (<n> assertions)`
  with the `<n>` the unedited copy prints there. That records the report's finding as observed and
  shows that the coverage rests on unit 85 S1. Observed by AC2.
- **S3** — Unit 82's claims answered. Unit 82's acceptance ledger beside AC2 records S1's two printed
  floor lines, each naming the variant its copy lacked and `<floor>` minus `<n>`, and S2's `PASS`
  line at unit 82's pass commit with that commit's sha. The record states that the floor's coverage
  of the variants, which 82 S2, AC2 and its New-arm line claim, holds through `TOOL-dWitnessedBar-85`
  S1. It names this unit. Observed by AC3.
- **S4** — The New-arm claims of units 79 and 80 answered. The acceptance ledgers of
  `TOOL-dWitnessedBar-79` and `TOOL-dWitnessedBar-80` beside AC2, the criterion each New-arm line
  covers, each carry a line quoting S1's floor line for the copy that lacked that unit's variant and
  naming `TOOL-dWitnessedBar-85` and this unit, in answer to the New-arm clause that the floor is
  restated after them by 82 S1. Observed by AC4.

## 3. Non-goals (OUT)

- The per-variant count and the floor restated over it, which are `TOOL-dWitnessedBar-85`'s for id 1.
- Rewording the spec text of units 79, 80 and 82. Their claims are answered in their ledgers by
  name, as `TOOL-dWitnessedBar-78` §3 answers units 68 to 73.
- The staged reds of each condition, which are `TOOL-dWitnessedBar-81`'s, and 82 AC2's first clone,
  which lacks unit 78's fourth-record arm and is unit 82's own.
- The floors `TOOL-dWitnessedBar-88`, `-89` and `-90` restate after this unit, and unit 89 S7's line
  beside AC1 in this unit's ledger. S1's clones read the floor the built tree holds at the close.
- The report's left-shift text, a checklist entry that an arm a floor protects adds to the floor's
  counter, and its promotion into the spec template. The template is a governance carrier, which
  BUILD-METHOD M3's veto 2 withholds from this run. S1 is that statement, made for this arm.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-79` — the length variant and its New-arm claim, which S1 stages absent and S4 answers in its ledger (id 17)
- **consumes-from** `TOOL-dWitnessedBar-80` — the tail variant and its New-arm claim, which S1 stages absent and S4 answers in its ledger (id 17)
- **consumes-from** `TOOL-dWitnessedBar-82` — §1, AC2 and the New-arm claim that the floor protects the variants, which S2 observes at its pass and S3 answers in its ledger (id 17)
- **consumes-from** `TOOL-dWitnessedBar-85` — the per-variant count, without which S1's copies print `PASS` and the claims stay unanswered (ids 17 and 1)
- **hands-off** `TOOL-dWitnessedBar-89` — AC1's exact difference, which unit 89 makes hold by placing the visited increments outside `check_canary_keys` (id 16 of the round-1 spec audit of units 85 to 88)

## 4. Design

### Evidence

Read at `e62583e7b` on 2026-11-21; the suite is unchanged there since unit 85's `0a5a198f6`.

- `spec/2026-10-25-spec-TOOL-dWitnessedBar-82.md` S2 and AC2 stage a copy lacking the `_rg_v:1}`
  variant and expect `below the pinned floor`; S2 says that copy reds at the close through unit 85 S1
  and prints `PASS` at unit 82's own pass, which this unit's S2 records. Its New-arm line repeats the
  claim. Its ledger's AC2 line (`2026-11-19-build-TOOL-dWitnessedBar-82-1-acceptance-ledger`) holds a
  counting probe over that copy and leaves the clone runs OWED to the close.
- The New-arm lines of `spec/2026-10-25-spec-TOOL-dWitnessedBar-79.md` and
  `spec/2026-10-25-spec-TOOL-dWitnessedBar-80.md` each cover AC2 and close "the floor is restated after
  this unit by `TOOL-dWitnessedBar-82` S1, which builds at order 43".
- `tools/run-gates/run-gates.gov.test.sh@e62583e7b:246` holds `FLOOR_ASSERTIONS=80` (PINNED
  2026-11-21), and `:1320` fails only when `a` is below the floor, printing S1's line; the suite then
  prints `FAIL` and exits 1 (`:1325-1326`).
- The liveness loop (`@e62583e7b:981-994`) calls `check_key_variant` per pair, the tail variant at
  `:985-986` and the length variant at `:987-988`, each `&& a=$((a+1)) ||` on its continuation line,
  unit 85 S1's increment. A key joins `rgf_seen` when no call left a reason (`:992`), and the gated
  compares are `:997` and `:1000`. A copy lacking one call's two lines leaves the other call alone to
  decide `rgf_seen`, so `a` falls by that call's increments only, one per pair. A stub probe of the
  loop, `check_key_variant` returning 0, read `a` as 7 as built and 5 with either call removed, both
  keys in `rgf_seen` each time (DERIVED 2026-11-21 by this re-ground's probe).
- The visited increments sit outside `check_canary_keys`, as unit 84 landed them:
  `awk '/^check_canary_keys\(\)/,/^}/' tools/run-gates/run-gates.gov.test.sh | grep -c 'a=\$((a'`
  prints 0 (DERIVED 2026-11-21), the probe of 89 AC7, and the loop's own is `@e62583e7b:994`.
- At unit 82's pass the length call (`tools/run-gates/run-gates.gov.test.sh@47ab62ebf:957-958`) adds
  nothing to `a`, under `FLOOR_ASSERTIONS=74` at `:246` (PINNED 2026-11-21), so a copy lacking it
  executes the unedited count.
- The hook's `sha)` arm reads `rec_sha=$_rg_v` bare (`.githooks/pre-push#read_green_file`).
  `#check_key_variant`'s `sed` given an empty replacement changes that line once, and its mutant reads
  `rec_sha` empty, which `#check_cr_reached` fails, so the call returns 0, seen red. Given `$_rg_v` it
  changes no line and prints `length variant changed 0 lines` (§8 F2).
- `tools/unattended/lib-unattended.sh#build_commit` answers which commit is a unit's pass, as
  `TOOL-dWitnessedBar-62` S16 rules. Sourced beside `tools/lib/resolve-python.sh`, it names
  `47ab62ebf` for unit 82 (DERIVED 2026-11-21); without the resolver, `#read_attribution_tokens`
  finds no launcher and the call returns 1.
- `memory/gotchas/ledger-token-wrapped-across-a-line-joins-nothing.md` records that a ledger grep
  reads one physical line.

### Inventory

Minted: nothing in code. The ledger records of S3 and S4. No function, constant, plant, flag or
file. Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

Units 79, 80, 82 and 85 are CLOSED (`08f226f3d`, `a967359a8`, `47ab62ebf`, `0a5a198f6`). Dispatch is
strictly sequential and sorts a tie by id string
(`tools/workflows/unattended-build.js@e62583e7b:78-82`, `:692-697`), so this unit builds alone after
unit 85, the last of order 44. At its pass it writes its own acceptance ledger, each criterion OWED to
the close, as units 81 and 87 did at theirs (`d2a1d891d`). At the close, after every unit is
terminal, the main loop runs S1's and S2's clones and writes S3's and S4's lines and its observations.

### Files touched (estimate)

- `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-82-1-acceptance-ledger.md`:
  S3's records and statement, beside AC2.
- `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-79-1-acceptance-ledger.md`:
  S4's record, beside AC2.
- `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-80-1-acceptance-ledger.md`:
  S4's record, beside AC2.
- This unit's own acceptance ledger, a new record in the same build directory, named by the pass's
  date as every builder's ledger is.

No code file and no other record.

### Alternatives rejected

- **Stage only the length variant's absence, as 82 AC2 does.** The tail variant's absence would stay
  unobserved, and unit 80's New-arm claim would rest on a red nobody saw.
- **Record the absence at the close alone, with no run at unit 82's pass.** The record would not show
  that the coverage came from unit 85, so a later change that undoes the count could not be told from
  a floor that never held it.

## 5. Production-readiness checklist

- security — no new write path. The scratch clones sit under `%TEMP%`.
- perf / scale — three scratch clones and three arm runs, once, at the close.
- error / empty / loading states — S1 names the floor line each copy prints and the reason lines it
  must not print.
- observability — each record quotes the printed line and the difference, so a reader can check it
  against a rerun.
- risks — a builder who stages an absence by keeping the call with an empty replacement runs a
  variant still seen red, and the copy prints `PASS`; S1's floor line catches it. One who keeps the
  call with `$_rg_v` prints its `changed 0 lines` reason and loses the key's compare too; S1's second
  clause and its exact difference catch that copy (§4 Evidence).
- testing — AC1 and AC2 by scratch clone, AC3 and AC4 by ledger, all at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — In a scratch clone of the built tree whose suite copy's liveness loop lacks the length
  variant's `check_key_variant` call, both its lines, the arm prints a line holding
  `below the pinned floor`, exits non-zero, and prints no line holding `length variant` or
  `tail variant`; the floor minus the executed count it prints equals the number of words in
  `${CANARY_KEYS[*]}`. A copy lacking the tail variant's call does the same.
  Red when: a variant can go missing with the canary green, or its absence reads only through its own
  reason line.
  fixture: scratch clones under `%TEMP%/<short-name>`.
  figure: the counts are DERIVED at observation time; the word count reads 2 today.
  permission: the arm's run is the main loop's, at the close.
- **AC2** — With `tools/lib/resolve-python.sh` and `tools/unattended/lib-unattended.sh` sourced,
  `build_commit cdfbd1cf..HEAD TOOL-dWitnessedBar-82 memory/builds/dWitnessedBar "$GENERATED_INDEXES" "$SHARED_RECORDS"`
  names unit 82's pass commit, the two values read from `.unattended.conf`. In a scratch clone
  checked out there, the suite copy with no length variant prints `PASS (<n> assertions)` with the
  same `<n>` as the unedited copy.
  Red when: the record claims the floor saw a missing variant before the count that makes it see one.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
  permission: the arm's run is the main loop's, at the close.
- **AC3** — When `grep -n 'below the pinned floor' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-82*acceptance-ledger*`
  runs at the close, it prints one line naming `length variant` and one naming `tail variant`, each
  with the difference and `TOOL-dWitnessedBar-86`, and
  `grep -n 'TOOL-dWitnessedBar-85' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-82*acceptance-ledger*`
  prints a line holding `PASS` and a sha.
  Red when: unit 82's coverage claim stands with no printed line beside it.
  permission: the ledger is written at the close.
- **AC4** — When `grep -n 'below the pinned floor' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-79*acceptance-ledger*`
  and the same grep over unit 80's ledger run at the close, each prints a line naming
  `TOOL-dWitnessedBar-85` and `TOOL-dWitnessedBar-86`, on the line grep prints.
  Red when: a New-arm line's floor clause is recorded against unit 82's restatement alone.
  permission: the ledgers are written at the close.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

`recall floor` and `recall floor arms` are owed for the ledgers under `memory/`. S1 and S2 run the
`run-gates gov canary` arm in scratch clones at the close; this unit adds no arm and moves none, so
it declares no `New arm:` line.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 82 is itself derived
  and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — How is a missing variant staged (id 17)?** Options: (a) the variant's `check_key_variant`
  call absent from the loop, so the copy runs the other variant alone; (b) the call kept with an
  inert replacement. As landed (§4 Evidence), an empty replacement is still seen red and adds its
  count, and `$_rg_v` prints its `changed 0 lines` reason, which reds through the variant's own check
  rather than the floor. Neither shows what the floor sees, and each fails a clause of S1; veto 1
  discards (b). RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the one survivor; its reasoning
  re-grounded 2026-11-21.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 79 to 84, id 17
  (HIGH, item H1, shared with id 1).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-89, the minors batch of the round-1 spec audit of units 85 to 88;
  nothing else moved.
- rev-3 · 2026-11-21 · §1 · S1 · S3 · §3 · §4 · §5 · AC1 · AC2 · §8 F2 · §10 · re-grounded at
  `e62583e7b` per 2026-11-19-prompt-TOOL-dWitnessedBar-86-reground-brief: units 79, 80, 82 and 85 as
  landed, 82's claim read from its S2, an absence staged as a whole `check_key_variant` call, AC2's
  resolver sourced, F2's reasoning over the landed replacement, Rollout and Files touched listed
  exactly, and blob-pinned citations; intent unchanged.

## 10. Reuse audit

The seam is the acceptance ledger of `memory/HYGIENE.md` "Acceptance ledger", as
`TOOL-dWitnessedBar-81` uses it to record each staged break with its printed line, and the suite's own
floor line at `tools/run-gates/run-gates.gov.test.sh@e62583e7b:1320`; the pass commit is
`build_commit`'s answer.
`python tools/codebase-map/reuse_lookup.py "assert a pinned count of executed assertions against a floor"`
ranked `counts`, `compare_counts`, `measure_typed_counts` and `read_count` (PINNED 2026-11-21), none
a record of a staged absence, so no existing seam fits beyond the ledger and floor named above.

Recall terms used: `python tools/memory-recall/query.py "how does a gate's assertion floor see a liveness variant that is no longer there" --terms "canary liveness variant counted FLOOR_ASSERTIONS restated floor owner deleted arm seen red increment"`
