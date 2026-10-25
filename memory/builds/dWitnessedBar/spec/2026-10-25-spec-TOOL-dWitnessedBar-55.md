# TOOL-dWitnessedBar-55 — the inherited-red upgrade step takes the line today's readers take: the last column-0 assignment, cleaned as they clean it

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 22 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 |
| [2026-10-25-build-TOOL-dWitnessedBar-52-round2-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-52-round2-fix-return.md) | research | TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-52-round2-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-52-round2-fix-brief.md) | research | TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 |
| [2026-10-25-review-TOOL-dWitnessedBar-52-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-52-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 40 to 51
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md`)
confirmed finding **id 43 at HIGH**, its item **H3**, alone in that item. `TOOL-dWitnessedBar-44` maps
the readers' value table onto `verdict.blocks` but never states their line-selection rule.
`read_policy_key` (`.githooks/pre-push:1306-1320`, byte-identical at `tools/unattended/unattended.sh:9517`)
takes the LAST line beginning exactly `INHERITED_RED=` at column 0. For a file holding
`INHERITED_RED=land` and then `INHERITED_RED=park`, both readers park today; a step taking the first
assignment writes `own-mixed-contended`, so MIXED and CONTENDED reds that blocked yesterday land
silently, the loosening unit 44 exists to prevent. An `export INHERITED_RED=` line is invisible to both
readers, so a step honouring it diverges from what was enforced. This unit takes the report's fix. It
repairs `TOOL-dWitnessedBar-44`.

## 2. Scope (IN)

- **S1** — The reader rule. The step reads a file's `INHERITED_RED` as `read_policy_key` does: per line,
  one trailing CR cut; an assignment is a line beginning exactly `INHERITED_RED=`; the LAST
  assignment wins; its value is cut at the first whitespace character followed by `#`, stripped of
  trailing spaces and tabs and of leading spaces, and stripped of one surrounding pair of double or of
  single quotes. A line in any other spelling, `export INHERITED_RED=`, an indented line or a commented
  one, is not an assignment. The same rule reads `GATE_POLICY_FILE` from `.unattended.conf`.
  Observed by AC1 and AC2.
- **S2** — Empty means undeclared. A last assignment that cleans to empty reads as undeclared, as both
  readers read it (`'')` arms, `.githooks/pre-push:1341-1342`, `unattended.sh:9590-9591`), so it takes
  unit 44's undeclared row, whatever an earlier line assigned. Observed by AC2.
- **S3** — What `up` deletes and `witness` counts. `up` deletes every assignment by S1's rule from each
  file it read, and no other line; `witness` counts every assignment remaining by the same rule. A line
  spelling the key that S1 does not read as an assignment is left as it is and named on the witness
  output as `not an assignment <file>:<line>`, which does not fail it. Observed by AC3.
- **S4** — The rule is held to the readers'. A `tools/govkit/selftest.py` arm runs the step's reader and
  the hook's `read_policy_key`, extracted from `.githooks/pre-push` from its `read_policy_key() {` line
  to the first column-0 `}` and run under the resolved bash, over one fixture set: two assignments, an
  `export` line, a commented line, an indented line, a quoted value, a trailing comment, CRLF line ends,
  and an empty last assignment. Each pair of values is equal. Observed by AC4.

## 3. Non-goals (OUT)

- The two files read, the value table and the two-file rule: `TOOL-dWitnessedBar-44`'s.
- The undeclared path's witness line: the round-1 minors batch's id 19 item (`TOOL-dWitnessedBar-51`).
- How `up` writes the bytes of the lines it keeps: the minors batch's id 18 item
  (`TOOL-dWitnessedBar-57`).
- A bug-class checklist entry "a record file read by line position": S4 gates the class for this key.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-44` — the step's two-file read and its mapping table, whose line-selection rule this unit states
- **hands-off** `TOOL-dWitnessedBar-57` — the set of lines S3 deletes, over which the minors batch's id 18 item keeps every other byte
- **hands-off** `TOOL-dWitnessedBar-59` — the reader rule and S4's parity set, whose line separator id 13's unit states as LF alone and to which it adds the lone-CR row
- **hands-off** `TOOL-dWitnessedBar-62` — the parity arm and `witness`, which the minors batch moves onto `check_conf_reader_parity`'s pattern and gives a defined predicate (ids 26, 41)

## 4. Design

### Evidence

- `read_policy_key() { # file text · key -> the LAST <key>= line's value, cleaned; nothing when none
  assigns it`: `line=${line%$'\r'}`; `case "$line" in "$2="*) v=${line#"$2="}; hit=1`; then
  `v=${v%%[[:space:]]#*}`, trailing space and tab stripped, leading space stripped, one pair of `"` or
  `'` removed (`.githooks/pre-push:1306-1320`).
- The driver's copy carries the comment "TWO COPIES OF THIS PARSER, BYTE-IDENTICAL, and the second is
  the pre-push hook's" (`tools/unattended/unattended.sh:9513-9516`), and `read_gate_policy` reads
  `GATE_POLICY_FILE` with it (`:9556`).
- Both readers map an empty value to `land` and anything outside `park land` to `park`
  (`.githooks/pre-push:1339-1343`, `unattended.sh:9583-9592`).

### The rule, on the shapes the readers meet

| File holds | Readers read | Step writes |
|---|---|---|
| `INHERITED_RED=land` then `INHERITED_RED=park` | park | `every-red` |
| `INHERITED_RED=park` then `INHERITED_RED=` | undeclared, land | nothing (undeclared) |
| `export INHERITED_RED=park` alone | undeclared, land | nothing; witness names the line |
| `INHERITED_RED="land" # note` with CRLF | land | `own-mixed-contended` |
| `  INHERITED_RED=park` alone | undeclared, land | nothing; witness names the line |

### Inventory

Minted: the witness line `not an assignment <file>:<line>`. Nothing else.

### Migration

None: the step has not run at any adopter; gov's file holds one plain assignment.

### Rollout

Live at landing, one step after `TOOL-dWitnessedBar-44`, in the same kit version as the step.

### Files touched (estimate)

- `tools/govkit/steps/inherited_red.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **Refuse a file holding two assignments.** The readers already decided what such a file means; an
  update that refuses leaves the adopter on the retired key.
- **Honour `export` lines.** Neither reader does, so the step would map a value nothing enforced.

## 5. Production-readiness checklist

- security — the step now writes what was enforced, never a milder value read from a line nothing read.
- perf / scale — one pass over each file's lines.
- error / empty / loading states — an empty last assignment is undeclared; a non-assignment spelling is
  named, never silently mapped.
- observability — the witness names each line it did not read as an assignment.
- risks — a reader whose rule changes later diverges until S4's arm reds, which is its purpose.
- testing — AC1 to AC4 by fixture and probe; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `python inherited_red.py up <target>` runs over a fixture whose `.githooks/gate-env.sh`
  holds `INHERITED_RED=land` and then `INHERITED_RED=park`, the target's `policy.toml` holds
  `blocks = "every-red"` under `[verdict]` and neither line remains.
  Red when: the step takes the first assignment and writes `own-mixed-contended`.
  fixture: scratch targets under the run's scratch path, built by the suite.
- **AC2** — When the same verb runs over a fixture holding `export INHERITED_RED=park` alone, and over
  one holding `INHERITED_RED=park` then `INHERITED_RED=`, each writes no `blocks` value.
  Red when: the step maps a line neither reader reads, or a value an empty last assignment overrode.
- **AC3** — When `up` runs over a file holding `INHERITED_RED=land`, an `export INHERITED_RED=park` line
  and `INHERITED_RED=park`, both assignments are gone, the `export` line is byte-identical, and
  `python inherited_red.py witness <target>` exits 0 printing `not an assignment` with that line.
  Red when: `up` deletes the `export` line, or `witness` fails on it.
- **AC4** — When the S4 fixture set is read by the step's reader and by `read_policy_key` extracted from
  `.githooks/pre-push`, every fixture yields the same value from both, the CRLF and quoted cases
  included.
  Red when: the step's reader keeps a CR, a quote or a trailing comment the hook strips.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `memory hygiene`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 AC4 · the eight-case fixture set read by both readers and the two-assignment target, staged red by taking the first assignment · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of `TOOL-dWitnessedBar-44`'s clause. Unit 44 carries
  none, being itself derived, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 40 to 51, id 43
  (HIGH, item H3).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring TOOL-dWitnessedBar-59's
  consumes-from edge and the hands-off bullet mirroring TOOL-dWitnessedBar-62's consumes-from edge,
  promoted by the round-1 spec audit of units 52 to 57; nothing else moved.

## 10. Reuse audit

The seam is `read_policy_key` itself, the one parse both readers share byte-identically; the step
follows it and S4 compares against a live extraction of it rather than a typed copy, the [contract]
parity a second reader owes. `python tools/codebase-map/reuse_lookup.py "read the last assignment line
of a policy key"` ranked `read`, `read_text`, `key` and `keys`, generic stems none of which is this
parser, so no existing seam fits beyond the hook's function.

Recall terms used: `python tools/memory-recall/query.py "which INHERITED_RED line do the policy readers take" --terms "read_policy_key INHERITED_RED last assignment column gate-env.sh GATE_POLICY_FILE export comment quotes CRLF"`
