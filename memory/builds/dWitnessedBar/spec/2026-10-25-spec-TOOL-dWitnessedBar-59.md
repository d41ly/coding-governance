# TOOL-dWitnessedBar-59 — the inherited-red upgrade step splits a policy file's lines on LF alone, as the readers do, held by a lone-CR parity row

**Status:** CLOSED · rev-4 · 2026-11-20 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 23 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 TOOL-dWitnessedBar-106 TOOL-dWitnessedBar-107 TOOL-dWitnessedBar-108 TOOL-dWitnessedBar-109 TOOL-dWitnessedBar-110 |
| [2026-10-25-build-TOOL-dWitnessedBar-59-deviation-591.md](../build/2026-10-25-build-TOOL-dWitnessedBar-59-deviation-591.md) | deviation | — |
| [2026-11-19-build-TOOL-dWitnessedBar-59-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-59-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-59-1-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-59-1-builder-return.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-59-2-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-59-2-builder-return.md) | journal | — |
| [2026-11-20-build-TOOL-dWitnessedBar-59-red-fix-103.md](../build/2026-11-20-build-TOOL-dWitnessedBar-59-red-fix-103.md) | red-fix | — |
| [2026-11-21-build-TOOL-dWitnessedBar-1-runlog-5a748574.md](../build/2026-11-21-build-TOOL-dWitnessedBar-1-runlog-5a748574.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 TOOL-dWitnessedBar-106 TOOL-dWitnessedBar-107 TOOL-dWitnessedBar-108 TOOL-dWitnessedBar-109 TOOL-dWitnessedBar-110 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-1-spec-tokens-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-1-spec-tokens-brief.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-28 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-59-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-59-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-59-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-59-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-59-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-59-reground-spec-writer.md) | journal | — |
| [2026-10-25-review-TOOL-dWitnessedBar-58-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-58-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-62 |
| [2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md](../reviews/2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md) | diff-review | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 52 to 57
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-52-spec-audit-round1.md`)
confirmed finding **id 13 at HIGH**, its item **H2**, alone in that item. `TOOL-dWitnessedBar-55` S1 has
the step read "per line, one trailing CR cut" and never names the line separator. The pre-step
readers' `read_policy_key` (`.githooks/pre-push@1ecf9aa6:1306-1321`, the same bytes live at
`.githooks/pre-push#read_policy_key`) splits on LF alone: a here-string read with `read -r`, then
`${line%$'\r'}` cuts one trailing CR. Python's text mode and `str.splitlines()` also split on a lone CR.
Over `INHERITED_RED=park<CR>INHERITED_RED=land<LF>` the hook read one line, value
`park<CR>INHERITED_RED=land`, which its `*` arm mapped to park (`.githooks/pre-push@1ecf9aa6:1343`); a
text-mode step reads two lines and takes `land`, writing `own-mixed-contended`, so MIXED and CONTENDED
reds that blocked yesterday land. Unit 55 landed at `dff3ca0d6` with the step splitting on LF alone
(`tools/govkit/steps/inherited_red.py#read_value`), so the step meets S1 at HEAD, but nothing holds it
there. None of the rows of unit 55's parity arm holds a lone CR, and the arm's comment names a lone CR as
what it does not check (`tools/govkit/selftest.py#check_inherited_red_step`). This unit takes the
report's fix. It repairs `TOOL-dWitnessedBar-55`.

## 2. Scope (IN)

- **S1** — LF alone separates lines. `tools/govkit/steps/inherited_red.py` reads each file it reads,
  the policy file and `.unattended.conf` alike, as bytes, decodes them as UTF-8, and splits the text with
  `.split('\n')` alone. It never calls `splitlines()`, never opens a file in universal-newline text mode,
  and never iterates a file object for lines, since iterating a file opened with `newline=''` still
  splits on a lone CR. A CR inside a line stays in that line; unit 55 S1's trailing-CR cut is unchanged.
  The landed step holds this at HEAD, so this unit edits no step code (§4 Evidence).
  Observed by AC1 and AC2.
- **S2** — One split for every verb. `up` deletes, and `witness` counts, the lines S1's split yields, so
  a physical line holding a lone CR is one line to all three: read, deleted and counted whole.
  Observed by AC2.
- **S3** — The parity row. Unit 55 S4's fixture set gains a row named `lone-cr` holding
  `INHERITED_RED=park<CR>INHERITED_RED=land<LF>`, whose agreed value is the hook's,
  `park<CR>INHERITED_RED=land`, which unit 44's table maps to `every-red`. The arm's row-count check
  counts it, and the arm's comment stops naming a lone CR as unchecked. Its staged break is a step reader
  that splits on a lone CR. Observed by AC3.

## 3. Non-goals (OUT)

- The line-selection rule, the cleaning and the rows unit 55 landed: `TOOL-dWitnessedBar-55`'s.
- The value table, `every-red` for a value outside `park` and `land` included: `TOOL-dWitnessedBar-44`'s.
- Any edit of `tools/govkit/steps/inherited_red.py`: the landed step meets S1 and S2 at HEAD.
- How `up` keeps the bytes of the lines it does not delete: the round-1 minors' id 18 item
  (`TOOL-dWitnessedBar-57` S14).
- Moving unit 55's parity arm onto `check_conf_reader_parity`: the minors batch's id 26 item
  (`TOOL-dWitnessedBar-62`), which carries this unit's `lone-cr` row with it.
- The report's left-shift text, a bug-class checklist entry: the class is already recorded as
  `memory/gotchas/text-mode-read-eats-a-bare-cr.md`. A parity-fixture rule for every bash/Python reader
  pair is a gate no clause of this build names; S3 holds this pair.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-55` — the step's LF-only reader, landed at `dff3ca0d6`, and S4's parity fixture set, whose line separator S1 states and to which S3 adds the lone-CR row
- **hands-off** `TOOL-dWitnessedBar-62` — the lone-CR parity row, which the minors batch's id 26 item carries onto `check_conf_reader_parity` with the rows unit 55 landed
- **hands-off** `TOOL-dWitnessedBar-63` — AC2's byte half, answered by unit 57's AC12, AC3's bytes capture of bash's stdout, and S1's split observed on `.unattended.conf` too (ids 3, 8, 33)

## 4. Design

### Evidence

- `while IFS= read -r line || [ -n "$line" ]; do line=${line%$'\r'}; … done <<< "$1"`
  (`.githooks/pre-push#read_policy_key`, the same bytes at `.githooks/pre-push@1ecf9aa6:1306-1312` when
  it read `INHERITED_RED`): one line per LF, a CR only cut when it ends the line. Probed 2026-11-20 at
  HEAD `e22cdce08`, the function cut from the hook prints `park<CR>INHERITED_RED=land` for S3's bytes.
- `case "$pol" in land) … park) … '') … *) PP_WHY="… outside 'park land', which reads park"`
  (`.githooks/pre-push@1ecf9aa6:1338-1344`). The hook reads no `INHERITED_RED` at HEAD:
  `TOOL-dWitnessedBar-3` retired it onto `verdict.blocks`.
- Unit 44's table maps any other non-blank value to `every-red`
  (`tools/govkit/steps/inherited_red.py#parse_gate`, over its `OTHER`).
- The landed step reads each file with `read_bytes()` and splits with `.split("\n")`, in
  `tools/govkit/steps/inherited_red.py#read_value`, `#render_gate_rest`, `#cmd_up` and `#cmd_witness`;
  `#derive_reads` reads `.unattended.conf` through `read_value`. Probed 2026-11-20 at HEAD `e22cdce08`
  over a scratch target holding `A=1<LF>INHERITED_RED=park<CR>INHERITED_RED=land<LF>B=2<LF>`: `up`
  wrote `blocks = "every-red"` and left `A=1<LF>B=2<LF>`. Over S2's target of AC2, `witness` before
  `up` printed `assigns` once and `not an assignment` nowhere, and `up` left `A=1<LF>B=2<LF>`.
- The parity arm, `tools/govkit/selftest.py#check_inherited_red_step`, cuts `read_policy_key` from the
  live hook, captures bash's stdout as bytes and decodes it itself, so a CR in bash's value reaches the
  compare. It checks the step's `read_value` against the hook over a tuple of byte rows, labels each
  check by the row's `repr`, and asserts the count of rows graded. Its comment "WHAT IT DOES NOT CHECK"
  names a lone CR. Its `run_step` captures the step's stdout in text mode, which turns a CR into a line
  break, so a witness observation counts substrings, never lines.
- The step's row `govkit/inherited-red-to-verdict-blocks` is not on `main`
  (`git show refs/heads/main:tools/govkit/steps.toml`, PINNED 2026-11-20 at `a0ae4dcac`), so no edit
  here meets `step-rows-frozen`; this unit makes none.

### The split, on the shapes that differ

Each count is DERIVED from the bytes on its row by the split its column names.

| Bytes | Hook's lines | A text-mode step's lines | S1's lines |
|---|---|---|---|
| `A=1\nB=2\n` | two | two | two |
| `A=1\r\nB=2\r\n` | two, CR cut | two | two, CR cut |
| `A=1\rB=2\n` | one | two | one |

### The change, in the suite

In `check_inherited_red_step`, after unit 55's AC3 block:

- The AC1 target: `.githooks/gate-env.sh` holding `A=1<LF>INHERITED_RED=park<CR>INHERITED_RED=land<LF>B=2<LF>`.
- The AC2 target: `.githooks/gate-env.sh` holding `A=1<LF>INHERITED_RED=park<CR> INHERITED_RED=land<LF>B=2<LF>`.
  The text after its lone CR spells the key indented, so an `up` that splits there keeps it and a
  `witness` that splits there names it as not an assignment (§8 F2).
- In the parity rows, the `lone-cr` row, its check label carrying the name `lone-cr`, the row-count
  check counting it, and the comment's "a lone CR" taken out of what the arm does not check.

### Inventory

Minted: the parity row name `lone-cr` in unit 55's set. Nothing else.

### Migration

None: no step code moves, and the step has not run at any adopter.

### Rollout

Live at landing, one order after `TOOL-dWitnessedBar-55`, as suite rows over the step it landed.

### Files touched (estimate)

- `tools/govkit/selftest.py`

### Alternatives rejected

- **Refuse a file holding a lone CR.** The readers already decided what such a file means; an update
  that refuses leaves the adopter on the retired key.
- **Normalise CR to LF before reading.** It changes the value the hook enforces into a milder one,
  the loosening this unit exists to prevent.
- **Re-edit the step to restate S1.** The landed step meets it; an edit with no behaviour to change is
  scaffolding, and it would move a program `step-rows-frozen` freezes once the row lands on `main`.

## 5. Production-readiness checklist

- security — the step maps the value the hook enforced, never a milder one a second line yielded, and
  the `lone-cr` row reds a reader that stops doing so.
- perf / scale — two scratch targets and one bash run more in the govkit suite.
- error / empty / loading states — a file that does not decode as UTF-8 is unit 44's refusal path,
  unchanged.
- observability — none new; the witness prints the value with its CR raw, as the hook held it.
- risks — a reader whose split changes later diverges until S3's row reds, which is its purpose.
- testing — AC1 to AC3 by fixture; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`: no behaviour a user meets changes.

## 6. Acceptance criteria

- **AC1** — When `python inherited_red.py up <target>` runs over a fixture whose `.githooks/gate-env.sh`
  holds `A=1<LF>INHERITED_RED=park<CR>INHERITED_RED=land<LF>B=2<LF>`, the target's `policy.toml` holds
  `blocks = "every-red"` under `[verdict]`.
  Red when: the step splits on the lone CR and writes `own-mixed-contended`.
  fixture: scratch targets under the run's scratch path, built by the suite.
- **AC2** — When `python inherited_red.py witness <target>` runs over a fixture whose
  `.githooks/gate-env.sh` holds `A=1<LF>INHERITED_RED=park<CR> INHERITED_RED=land<LF>B=2<LF>`, it exits 1
  with `assigns` once in its stdout and `not an assignment` nowhere; `up` then leaves the file holding
  exactly `A=1<LF>B=2<LF>`.
  Red when: `up` splits the line in two and keeps ` INHERITED_RED=land`, or `witness` splits it and
  names that text as not an assignment.
- **AC3** — When unit 55's parity arm reads the `lone-cr` row through the step's `read_value` and through
  `read_policy_key` extracted from `.githooks/pre-push`, both yield `park<CR>INHERITED_RED=land` and the
  row-count check counts the row; with the step's `read_value` splitting its text by `str.splitlines()`,
  the arm fails naming `lone-cr`.
  Red when: the arm stays green over a reader that splits on CR.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `memory hygiene`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 · the `lone-cr` row read by both readers and the two lone-CR targets, staged red by the step splitting its text with `str.splitlines()` in `read_value`, `render_gate_rest` and `cmd_witness` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of `TOOL-dWitnessedBar-55`'s clause. Unit 55 carries none,
  being itself derived, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Which bytes does AC2 run over?** Over AC1's line, both halves either side of the lone CR are
  assignments, so a CR-splitting `up` deletes both and a CR-splitting `witness` names neither: AC2's
  red-when could not be observed there. Options: (a) keep AC1's bytes for AC2; (b) a second target
  whose text after the lone CR spells the key indented, which a CR-splitting `up` keeps and a
  CR-splitting `witness` names; (c) mark S2 NOT OBSERVED. (a) fails AC2's red-when, so veto 1 discards
  it; (c) satisfies fewer criteria than (b). RESOLVED (agent, 2026-11-20, delegated): (b), the
  feature-rich option, probed green over the landed step at HEAD `e22cdce08`.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 52 to 57, id 13
  (HIGH, item H2).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring TOOL-dWitnessedBar-63's
  consumes-from edge, promoted by the round-1 spec audit of units 58 to 62; nothing else moved.
- rev-3 · 2026-11-19 · §7 · the leg line gains the leg `policy fixtures`, whose guard §4's
  `tools/govkit/selftest.py` trips, as the spec-token checker's guards join named it at `c6df3e901`,
  by the brief `2026-11-19-prompt-TOOL-dWitnessedBar-1-spec-tokens-brief`; §4 is unchanged, as the
  unit writes that path; nothing else moved.
- rev-4 · 2026-11-20 · §1 · §2 · §3 · §4 · §5 · §6 · §7 · §8 · §10 · re-grounded over HEAD `e22cdce08`
  by the brief `2026-11-19-prompt-TOOL-dWitnessedBar-59-reground-brief`: the pre-step readers cited
  blob-pinned at the base and the live ones by symbol; unit 55, landed at `dff3ca0d6`, already splits on
  LF alone, so S1 and S2 are observed rather than built and `inherited_red.py` leaves Files touched;
  the parity row is named `lone-cr` beside the rows unit 55 landed rather than as a ninth; AC2 runs over
  its own target (F2); the New arm line's staged break and §10's probe ranks restated.

## 10. Reuse audit

The seam is the landed step's reader, `tools/govkit/steps/inherited_red.py#read_value`, whose LF-only
split follows `.githooks/pre-push#read_policy_key`, and unit 55 S4's parity arm,
`tools/govkit/selftest.py#check_inherited_red_step`, which gains a row and two targets rather than a
second harness. `python tools/codebase-map/reuse_lookup.py "split policy file lines on LF only like the bash reader"`
ranked `read_text`, `read`, `read_bytes` and `lf` (`tools/codebase-map/map_lib.py`) at HEAD on
2026-11-20; none splits a file on LF alone for a policy key, so no existing seam fits beyond those two.
The recall query below returned the class's record, `TOOL-dUnstalledConvoy-18` and its gotcha
`memory/gotchas/text-mode-read-eats-a-bare-cr.md`, whose rule ("the damage happens on the READ") S1
follows.

Recall terms used: `python tools/memory-recall/query.py "which INHERITED_RED line do the policy readers take" --terms "read_policy_key INHERITED_RED lone CR splitlines universal newlines LF here-string gate-env.sh parity fixture"`
