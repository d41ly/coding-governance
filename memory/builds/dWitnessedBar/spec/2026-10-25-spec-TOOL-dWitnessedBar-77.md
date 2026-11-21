# TOOL-dWitnessedBar-77 — the canary prints its failure line once per variable whose CR did not arrive, and unit 72's red is recorded with the `for rec_fp` line

**Status:** CLOSED · rev-4 · 2026-11-21 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 41 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-77-deviation-771.md](../build/2026-10-25-build-TOOL-dWitnessedBar-77-deviation-771.md) | deviation | — |
| [2026-10-25-build-TOOL-dWitnessedBar-77-deviation-772.md](../build/2026-10-25-build-TOOL-dWitnessedBar-77-deviation-772.md) | deviation | — |
| [2026-11-19-build-TOOL-dWitnessedBar-77-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-77-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-77-1-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-77-1-builder-return.md) | journal | — |
| [2026-11-21-build-TOOL-dWitnessedBar-77-widen-19.md](../build/2026-11-21-build-TOOL-dWitnessedBar-77-widen-19.md) | widen | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-77-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-77-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-77-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-77-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-77-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-77-reground-spec-writer.md) | journal | — |
| [2026-10-25-review-TOOL-dWitnessedBar-74-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-74-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-78 |
| [2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md](../reviews/2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md) | diff-review | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 68 to 73
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-68-spec-audit-round1.md`)
confirmed finding **id 25 at HIGH**, report item **H2**. Id 9 shares that item and took
`TOOL-dWitnessedBar-76`. Report items M2 and L2, ids 1 and 17, describe the failure line's two
spellings at MEDIUM and LOW, and `TOOL-dWitnessedBar-78` takes them.

`TOOL-dWitnessedBar-72` S1, §5 observability and AC1 said the canary's failure line names `rec_fp`.
Unit 70 S2 fixed that line as text with no variable, and unit 72's §4 Inventory minted nothing, so
a canary that never checks `rec_fp` could pass AC1. `TOOL-dWitnessedBar-75` gave the line a slot,
and its §8 F3 took the slot's `rec_fp` value from this unit. `TOOL-dWitnessedBar-76` made the byte
checks one `check_canary_keys` call, and its §8 F3 left the slot reading only the first variable that
call prints.

What remains is this unit's: the canary prints its line once for every variable whose CR did not
arrive, so a break losing both keys' CRs names both, and unit 72 AC1's staged red is recorded with
the `for rec_fp` line it prints. It builds after `TOOL-dWitnessedBar-76` at order 41.

## 2. Scope (IN)

- **S1** — One line per failing variable. In `tools/run-gates/run-gates.gov.test.sh`, the canary
  collects its slot values, in order, in one array, `rgf_whats`. It holds `count <n>` alone when the
  mutant changed `<n>` lines and `<n>` is not 1. Otherwise it holds each word `check_canary_keys`
  prints on `$rgf_t/cut-mut.sh`, in the order printed, split as the liveness loop splits `rgf_got`.
  `rgf_ok` is 1 only when `rgf_whats` is empty, and stays the flag both compares' counts read. One
  loop over `rgf_whats` sets `rgf_what` and runs unit 75 S2's one statement, which prints unit 75
  S1's line with `$rgf_what` in the slot and sets `fail=1`. The cut to the first printed variable,
  `rgf_what=${rgf_miss%%$'\n'*}`, goes. A count failure still runs no byte check and prints no
  variable. A `fingerprint` CR that did not arrive alone still prints
  `gov-canary: the planted CR never reached read_green_file on <uname -s> for rec_fp; the CR-strip assertion is not counted`
  once. Observed by AC1.
- **S2** — Unit 72 AC1's staged red is recorded with its line. At the close, on a Windows node, the
  main loop stages in a scratch clone's `.githooks/pre-push` the `fingerprint` edit
  `TOOL-dWitnessedBar-76` S3's loop writes at `648a4d5d5`, `fingerprint) rec_fp=${_rg_v%?} ;;`.
  Unit 72's acceptance ledger records it as a second line opening `- AC1 — ` under its
  `**Evidences:** TOOL-dWitnessedBar-72` block. The line quotes the printed `for rec_fp` line, states
  that no line holding `for rec_sha` or `for count` printed, and names the `uname -s` it ran under
  and `TOOL-dWitnessedBar-77`. Observed by AC2.

## 3. Non-goals (OUT)

- The slot and its `count <n>`, `rec_sha` and `rec_fp` values, which are `TOOL-dWitnessedBar-75`'s,
  CLOSED at `1b3295a52`.
- `CANARY_KEYS`, `check_canary_keys` and the per-key liveness loop, which are
  `TOOL-dWitnessedBar-76`'s, CLOSED at `bdc10a4df`. Its liveness lines are unchanged.
- The slot's `unread` value for a read failure, `TOOL-dWitnessedBar-84` S13's.
- The `for count 2` record of unit 72 AC1's `$(awk ...)`-plus-strip break, `TOOL-dWitnessedBar-84`
  S5's.
- Unit 72's §4 Inventory and §5 observability line answered in its ledger, and the strip-less
  break's two printed lines recorded for unit 72 AC3, which are `TOOL-dWitnessedBar-78`'s for ids 17
  and 1.
- The report's left-shift text, a checklist entry that a criterion requiring a printed line to name a
  value cites a line with a slot for it. No clause of this build names it.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-72` — S1's claim that the canary's failure line names `rec_fp`, and AC1's red, which S1 makes true and S2 records (id 25)
- **consumes-from** `TOOL-dWitnessedBar-75` — the `for <what>` slot, its `rec_fp` value and its one emission statement, which S1 runs once per failing variable (ids 25 and 24)
- **consumes-from** `TOOL-dWitnessedBar-76` — `check_canary_keys`, whose output S1 prints one line per variable, and the `fingerprint` variant S2 stages (ids 25 and 9)
- **hands-off** `TOOL-dWitnessedBar-78` — unit 72's Inventory and observability line answered with the slot's `rec_fp` value, which unit 75 landed and S1 prints once per failing variable, and the strip-less break's printed lines recorded for unit 72 AC3 (ids 1 and 17)
- **hands-off** `TOOL-dWitnessedBar-82` — the New-arm claim, which unit 82's restated floor answers in this unit's ledger (id 2 of the round-1 spec audit of units 74 to 78, item H2)
- **hands-off** `TOOL-dWitnessedBar-84` — S1's count line and the ledger lines for AC1 and AC2, kept on one physical line and cited by section label (ids 4, 11, 16 of the round-1 spec audit of units 74 to 78)
- **hands-off** `TOOL-dWitnessedBar-88` — S2's staged `fingerprint` variant, which unit 88 names by its current text in unit 72's ledger (id 13 of the round-1 spec audit of units 79 to 84)

## 4. Design

### Evidence

Probed at `648a4d5d5` (PINNED 2026-11-21) under `uname -s` `MINGW64_NT-10.0-22621`,
GNU bash 5.3.9 `x86_64-pc-cygwin` and GNU sed 4.9 (PINNED 2026-11-21). The probe sourced the suite's
`check_cr_reached`, `CANARY_KEYS` and `check_canary_keys`, cut the hook's `read_green_file`, and
read a hand-built record laid out as the AC12 arm's record, which `TOOL-dWitnessedBar-68` S1 and
`TOOL-dWitnessedBar-67` S2 build: two `sha` lines the second CR-ended, a CR-ended `fingerprint`. It ran
the canary's chain as HEAD has it and a prototype of S1 under `set -u`, and the liveness loop as HEAD
has it. The arm's own record, from `run_local_plant`, is the main loop's at the close:

| Hook copy | Count | HEAD prints `for` | S1 prints `for` | Liveness reasons | Pin |
|---|---|---|---|---|---|
| HEAD's hook | 1 | nothing | nothing | none | PINNED 2026-11-21 |
| `fingerprint) rec_fp=${_rg_v%?} ;;` | 1 | `rec_fp` | `rec_fp` | `it named rec_fp whose CR arrived`, `variant changed 0 lines` | PINNED 2026-11-21 |
| unit 72 AC1's bare `$(awk ...)` `fingerprint` read | 1 | `rec_fp` | `rec_fp` | not probed | PINNED 2026-11-21 |
| both `sha) rec_sha=${_rg_v%?} ;;` and the `fingerprint` edit | 1 | `rec_sha` | `rec_sha`, then `rec_fp` | `variant changed 0 lines`, twice | PINNED 2026-11-21 |
| no `    _rg_v=${_rg_v%$'\r'}` line | 0 | `count 0` | `count 0` | `mutant changed 0 lines`, twice | PINNED 2026-11-21 |

Only the both-keys copy tells S1 from HEAD, so it is AC1's break and the New arm's red. No liveness
line holds ` for `, so AC1's absence tests read the canary's lines alone.

- At HEAD the canary sets `rgf_what` to `count <n>` or to the first line of `check_canary_keys`'s
  output, `${rgf_miss%%$'\n'*}`, and prints the line from one statement
  (`tools/run-gates/run-gates.gov.test.sh@648a4d5d5:904-910`).
  `grep -n 'the planted CR never reached read_green_file on' tools/run-gates/run-gates.gov.test.sh`
  prints one line holding ` for $rgf_what;` (PINNED 2026-11-21).
- `check_canary_keys` prints each failing variable on its own line, in `CANARY_KEYS` order
  (`tools/run-gates/run-gates.gov.test.sh#check_canary_keys`). The liveness loop splits that output
  as `for rgf_g in $rgf_got` (`tools/run-gates/run-gates.gov.test.sh@648a4d5d5:922`), the split S1
  reuses; the words are variable names and hold no space.
- The suite runs under `set -u` (`tools/run-gates/run-gates.gov.test.sh@648a4d5d5:31`); an empty
  array's `"${rgf_whats[@]}"` expands to nothing there from bash 4.4 on (PINNED 2026-11-21, the probe).
- Unit 70 S2 fixed the line with no slot. Unit 72 S1, §5 observability and AC1 said it names
  `rec_fp`, and unit 72 §4 Inventory reads "Minted: nothing". Unit 75 S1 and §8 F3 give the slot its
  `rec_fp` value; unit 76 S2 and §8 F3 feed it the first variable `check_canary_keys` prints.
- Unit 72's ledger beside AC1 quotes the slotless line for the bare `$(awk ...)` copy and names no
  unit 77 (`memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-72-1-acceptance-ledger.md`),
  so S2's line is a second one.

### Inventory

Minted: the arm array `rgf_whats`. No function, constant, plant, flag or file; the `rec_fp` value is
unit 75's. Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 41, after `TOOL-dWitnessedBar-72` and `TOOL-dWitnessedBar-75` (order 40,
CLOSED at `e0cf5fa91` and `1b3295a52`). Order 41's `TOOL-dWitnessedBar-73` and `-76` are CLOSED at
`71f212ad1` and `bdc10a4df`. Dispatch is strictly sequential and sorts a tie by id string
(`tools/workflows/unattended-build.js@648a4d5d5:78-82`, `:692-697`), so this unit builds next, before
`TOOL-dWitnessedBar-79`, `-80` and `-81`. Units 79 and 80 also edit
`tools/run-gates/run-gates.gov.test.sh`, and unit 81 writes under `memory/builds/dWitnessedBar/build/`,
where S2's ledger sits, so none of them builds beside this unit.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`: S1's array and loop around the one emission statement.
- `memory/project/shell-role.txt`: the suite's row reads 784 (PINNED 2026-11-21 at `648a4d5d5`),
  and `sh_hygiene.py`'s `measure_code_lines` measures it at 784 (PINNED 2026-11-21). When S1 grows
  the suite past the row, the pass widens it with
  `python tools/memory-tree/ratchet.py widen shell-role --key tools/run-gates/run-gates.gov.test.sh --reason "TOOL-dWitnessedBar-77 S1" --unit TOOL-dWitnessedBar-77`,
  which adds one to the row and writes its widen record under `memory/builds/dWitnessedBar/build/`,
  declared through `--dispatch`; the pass then sets the row to the measured count, as units 75 and
  76 did.
- `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-72-1-acceptance-ledger.md`:
  S2's line, the main loop's at the close.

### Alternatives rejected

- **Give `rec_fp` its own line, outside unit 75's slot.** It would be a second emission site for one
  failure, the shape unit 75 S2 rules out.
- **Print one line naming every failing variable.** A record could then not show that the
  `fingerprint` break named `rec_fp` alone, which S2 records.
- **Split `check_canary_keys`'s output with a `while read` loop.** Fed from a here-string of a
  `$(...)` value, it is the shape this node's bash mishandles; the word split needs no input stream.

## 5. Production-readiness checklist

- security — no new write path.
- perf / scale — none: one line per failing variable, at most one per `CANARY_KEYS` pair.
- error / empty / loading states — S1 keeps a count failure from naming a variable it never read.
- observability — the canary names every variable whose CR did not arrive.
- risks — none beyond unit 75's.
- testing — AC1 by probe and scratch clone, AC2 by ledger at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When the arm runs over the built tree, it prints no line holding
  `never reached read_green_file`. In a scratch clone whose `.githooks/pre-push` reads both
  `sha) rec_sha=${_rg_v%?} ;;` and `fingerprint) rec_fp=${_rg_v%?} ;;`, the arm prints
  `gov-canary: the planted CR never reached read_green_file on ` followed by the `uname -s` value and
  ` for rec_sha;`, then the same prefix with ` for rec_fp;`, and no line holding `for count`. In a
  clone whose `read_green_file` lacks the line `    _rg_v=${_rg_v%$'\r'}`, it prints the
  ` for count 0;` line once and no line holding `for rec_sha` or `for rec_fp`.
  `grep -n 'the planted CR never reached read_green_file on' tools/run-gates/run-gates.gov.test.sh`
  still prints one line, holding ` for $rgf_what;`.
  Red when: the both-keys clone prints `for rec_sha` alone, a count failure prints a variable, or a
  second statement spells the line.
  fixture: scratch clones under `%TEMP%/<short-name>`.
  figure: the two lines and `count 0` are PINNED 2026-11-21 by §4 Evidence.
  permission: the arm's run is the main loop's, at the close.
- **AC2** — When `grep -n 'AC1' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-72*acceptance-ledger*`
  runs at the close, a red record quotes a line holding `for rec_fp` and a `uname -s` value beginning
  `MINGW` or `MSYS`, states that no `for rec_sha` or `for count` line printed, and names
  `TOOL-dWitnessedBar-77`. The builder's slotless AC1 line already there is not it.
  Red when: unit 72 AC1's red is recorded with no printed line, or on a line that names no variable.
  permission: the arm's run is the main loop's, at the close.

## 7. Gates

`run-gates gov canary` · `portability (shell lines only shrink)` · `recall floor` · `recall floor arms` · `memory hygiene`

`portability (shell lines only shrink)` reads the widened shell-role row and checks a count, never the
arm. The two recall legs are named because their guards name `memory/`, where the row, the widen
record and unit 72's ledger sit. `run-gates gov canary` is held unless the main loop sets
GATE_SELFTESTS at the close (`tools/run-gates/run-gates.sh#derive_hold_source`), which
`SELFTESTS_OWED_PATHS="tools/"` does (`.unattended.conf@648a4d5d5:40`).

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 · one canary line per failing variable, staged red by a hook whose `sha` and `fingerprint` cases both read `${_rg_v%?}` (reaches `for rec_sha` then `for rec_fp`, where HEAD prints `for rec_sha` alone) and by a hook whose `read_green_file` holds no strip (reaches `for count 0` with no variable line) · none, the floor is stated by `TOOL-dWitnessedBar-73` S15

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 72 is itself derived
  and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — What does this unit build once unit 75 §8 F3 landed the `rec_fp` value?** The `fingerprint`
  variant already prints `for rec_fp` at `648a4d5d5` (§4 Evidence), so rev-3's AC1 passes before any
  build. Options: (a) S1 is the one-line-per-variable printing alone, and AC1 and the New arm stage a
  break losing both keys' CRs, which HEAD prints as `for rec_sha` alone; (b) keep rev-3's AC1, an arm
  never seen red against the code it guards; (c) close the unit as built, dropping the printing unit
  75 §3 and unit 76 §8 F3 hand it and S2's record. Veto 1 discards (b) under the charter's gate rule
  and (c) under unit 75's §3. RESOLVED (agent, 2026-11-21, delegated): (a), the one survivor.
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
- rev-4 · 2026-11-21 · §1 to §10 · S1 · S2 · AC1 · AC2 · re-grounded over units 72, 75 and 76 as
  landed, per 2026-11-19-prompt-TOOL-dWitnessedBar-77-reground-brief. S1 narrows to one line per
  failing variable through the array `rgf_whats`, the `rec_fp` value being unit 75's (§8 F2). S2
  spells the staged edit and the ledger line's place. AC1 stages the both-keys break and keeps unit
  75's one-statement grep; AC2 sets aside the builder's slotless line. §4 Evidence re-probes at HEAD;
  the shell-role widen and unit 72's ledger join §4 and §7. Citations move to `path#symbol`,
  blob-pinned lines or section labels.

## 10. Reuse audit

The seam is `TOOL-dWitnessedBar-75`'s slotted failure line and its one emission statement in
`tools/run-gates/run-gates.gov.test.sh`, run once per value, fed by `TOOL-dWitnessedBar-76`'s
`check_canary_keys` and split as that unit's liveness loop splits the same output.
`python tools/codebase-map/reuse_lookup.py "print one failure line for each failing value a check names"`
ranked `check`, `fail`, `read_policy_value`, `checks` and `check_line` first (PINNED 2026-11-21),
none a failure line naming a variable, so no existing seam fits beyond those named above.

Recall terms used: `python tools/memory-recall/query.py "how is a canary failure line made to name every failing variable rather than the first" --terms "canary failure line slot rgf_what rec_sha rec_fp check_canary_keys one line per variable"`
