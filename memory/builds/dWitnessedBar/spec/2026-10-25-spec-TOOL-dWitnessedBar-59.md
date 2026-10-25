# TOOL-dWitnessedBar-59 — the inherited-red upgrade step splits a policy file's lines on LF alone, as the readers do, held by a lone-CR parity row

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 23 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 |
| [2026-10-25-review-TOOL-dWitnessedBar-58-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-58-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-62 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 52 to 57
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-52-spec-audit-round1.md`)
confirmed finding **id 13 at HIGH**, its item **H2**, alone in that item. `TOOL-dWitnessedBar-55` S1 has
the step read "per line, one trailing CR cut" and never names the line separator. `read_policy_key`
(`.githooks/pre-push:1306-1320`) splits on LF alone: a here-string read with `read -r`, then
`${line%$'\r'}` cuts one trailing CR. Python's text mode and `str.splitlines()` also split on a lone CR.
Over `INHERITED_RED=park<CR>INHERITED_RED=land<LF>` the hook reads one line, value
`park<CR>INHERITED_RED=land`, which its `*` arm maps to park (`:1339-1343`); a text-mode step reads two
lines and takes `land`, writing `own-mixed-contended`, so MIXED and CONTENDED reds that blocked
yesterday land. None of unit 55's eight parity fixtures holds a lone CR. This unit takes the report's
fix. It repairs `TOOL-dWitnessedBar-55`.

## 2. Scope (IN)

- **S1** — LF alone separates lines. `tools/govkit/steps/inherited_red.py` reads each file it reads,
  the policy file and `.unattended.conf` alike, as bytes, decodes them as UTF-8, and splits the text with
  `.split('\n')` alone. It never calls `splitlines()`, never opens a file in universal-newline text mode,
  and never iterates a file object for lines, since iterating a file opened with `newline=''` still
  splits on a lone CR. A CR inside a line stays in that line; unit 55 S1's trailing-CR cut is unchanged.
  Observed by AC1 and AC2.
- **S2** — One split for every verb. `up` deletes, and `witness` counts, the lines S1's split yields, so
  a physical line holding a lone CR is one line to all three: read, deleted and counted whole.
  Observed by AC2.
- **S3** — The parity row. Unit 55 S4's fixture set gains a ninth fixture holding
  `INHERITED_RED=park<CR>INHERITED_RED=land<LF>`, whose agreed value is the hook's,
  `park<CR>INHERITED_RED=land`, which unit 44's table maps to `every-red`. Its staged break is a step
  reader that opens the file in text mode. Observed by AC3.

## 3. Non-goals (OUT)

- The line-selection rule, the cleaning and the eight fixtures: `TOOL-dWitnessedBar-55`'s.
- The value table, `every-red` for a value outside `park` and `land` included: `TOOL-dWitnessedBar-44`'s.
- How `up` keeps the bytes of the lines it does not delete: the round-1 minors' id 18 item
  (`TOOL-dWitnessedBar-57` S14).
- Moving unit 55's parity arm onto `check_conf_reader_parity`: the minors batch's id 26 item
  (`TOOL-dWitnessedBar-62`), which carries this unit's ninth row with it.
- The report's left-shift text, a bug-class checklist entry: the class is already recorded as
  `memory/gotchas/text-mode-read-eats-a-bare-cr.md`. A parity-fixture rule for every bash/Python reader
  pair is a gate no clause of this build names; S3 holds this pair.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-55` — the step's reader rule and S4's parity fixture set, whose line separator S1 states and to which S3 adds the lone-CR row
- **hands-off** `TOOL-dWitnessedBar-62` — the lone-CR parity row, which the minors batch's id 26 item carries onto `check_conf_reader_parity` with the other eight
- **hands-off** `TOOL-dWitnessedBar-63` — AC2's byte half, answered by unit 57's AC12, AC3's bytes capture of bash's stdout, and S1's split observed on `.unattended.conf` too (ids 3, 8, 33)

## 4. Design

### Evidence

- `while IFS= read -r line || [ -n "$line" ]; do line=${line%$'\r'}; … done <<< "$1"`
  (`.githooks/pre-push:1306-1311`): one line per LF, a CR only cut when it ends the line.
- `case "$pol" in land) … park) … '') … *) PP_WHY="… outside 'park land', which reads park"`
  (`.githooks/pre-push:1339-1344`).
- Unit 44's table maps any other non-blank value to `every-red` (`TOOL-dWitnessedBar-44` §4).

### The split, on the shapes that differ

| Bytes | Hook's lines | A text-mode step's lines | S1's lines |
|---|---|---|---|
| `A=1\nB=2\n` | 2 | 2 | 2 |
| `A=1\r\nB=2\r\n` | 2, CR cut | 2 | 2, CR cut |
| `A=1\rB=2\n` | 1 | 2 | 1 |

### Inventory

Minted: the fixture `lone-cr` in unit 55's set. Nothing else.

### Migration

None: the step has not run at any adopter.

### Rollout

Live at landing, one step after `TOOL-dWitnessedBar-55`, in the same kit version as the step.

### Files touched (estimate)

- `tools/govkit/steps/inherited_red.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **Refuse a file holding a lone CR.** The readers already decided what such a file means; an update
  that refuses leaves the adopter on the retired key.
- **Normalise CR to LF before reading.** It changes the value the hook enforces into a milder one,
  the loosening this unit exists to prevent.

## 5. Production-readiness checklist

- security — the step now maps the value the hook enforced, never a milder one a second line yielded.
- perf / scale — one bytes read per file, as before.
- error / empty / loading states — a file that does not decode as UTF-8 is unit 44's refusal path,
  unchanged.
- observability — none new.
- risks — a reader whose split changes later diverges until S3's row reds, which is its purpose.
- testing — AC1 to AC3 by fixture; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `python inherited_red.py up <target>` runs over a fixture whose `.githooks/gate-env.sh`
  holds `INHERITED_RED=park<CR>INHERITED_RED=land<LF>`, the target's `policy.toml` holds
  `blocks = "every-red"` under `[verdict]`.
  Red when: the step splits on the lone CR and writes `own-mixed-contended`.
  fixture: scratch targets under the run's scratch path, built by the suite.
- **AC2** — When `up` runs over that fixture, the whole physical line is gone and every other byte of the
  file is unchanged; `python inherited_red.py witness <target>` before `up` counts one assignment.
  Red when: `up` or `witness` splits the line in two.
- **AC3** — When unit 55's parity arm reads the `lone-cr` fixture through the step's reader and through
  `read_policy_key` extracted from `.githooks/pre-push`, both yield `park<CR>INHERITED_RED=land`; with the
  step's reader switched to a text-mode open, the arm fails naming `lone-cr`.
  Red when: the arm stays green over a reader that splits on CR.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `memory hygiene`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 · the `lone-cr` fixture read by both readers and the lone-CR target, staged red by opening the policy file in text mode · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of `TOOL-dWitnessedBar-55`'s clause. Unit 55 carries none,
  being itself derived, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 52 to 57, id 13
  (HIGH, item H2).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring TOOL-dWitnessedBar-63's
  consumes-from edge, promoted by the round-1 spec audit of units 58 to 62; nothing else moved.

## 10. Reuse audit

The seam is `read_policy_key` itself (`.githooks/pre-push:1306-1320`), whose LF-only here-string read the
step now follows, and unit 55 S4's parity arm, which gains a row rather than a second harness.
`python tools/codebase-map/reuse_lookup.py "split policy file lines on LF only like the bash reader"`
ranked `read`, `read_text`, `lf` (`tools/codebase-map/map_lib.py`) and `read_conf`; none splits a file on
LF alone for a policy key, so no existing seam fits beyond the hook's function. The recall query below
returned the class's record, `TOOL-dUnstalledConvoy-18` and its gotcha
`memory/gotchas/text-mode-read-eats-a-bare-cr.md`, whose rule ("the damage happens on the READ") S1
follows.

Recall terms used: `python tools/memory-recall/query.py "which INHERITED_RED line do the policy readers take" --terms "read_policy_key INHERITED_RED lone CR splitlines universal newlines LF here-string gate-env.sh parity fixture"`
