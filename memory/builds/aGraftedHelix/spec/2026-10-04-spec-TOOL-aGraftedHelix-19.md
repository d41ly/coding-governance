# TOOL-aGraftedHelix-19 — the claim write table's rows and modes are driver constants the decision refuses outside of, and the per-cell arm derives its cells from them

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-1 · base 5266d22e · streams tooling · order 3

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aGraftedHelix-12`'s table-driven arm holds one typed row per cell of the claim write table
`check_claim_writable` implements, and checks its own completeness only by counting its own rows. That
catches a row dropped from the arm. It cannot see a claim-read class or a mode added to the function
later, so the arm stays green over an uncovered cell while unit 12's §3 calls it the class gate. The
round-1 audit admitted the arm as a gate only if it derived its cells rather than keeping a second
typed copy. This unit gives the table's two axes one declaration in the driver, makes the decision
refuse a value outside it, and has the arm derive its cells from that declaration. It closes finding
31 (HIGH) of the round-1 spec audit of units 10 to 15.

## 2. Scope (IN)

- **S1** — `tools/unattended/unattended.sh` declares the table's axes as two constants beside
  `check_claim_writable`, each on one assignment line of the `NAME="…"` form `VERBS_SLUG` uses:
  `CLAIM_READS`, the eight claim-read classes in the §4 table's row order, and `CLAIM_MODES`, the four
  modes in its column order. Observed by AC1.
- **S2** — `check_claim_writable` refuses a mode outside `CLAIM_MODES` and a claim-read class it
  derives outside `CLAIM_READS`, with a named internal error that writes nothing. A class or mode
  added to the function without its constant therefore fails on its first use, and one added to the
  constant without a branch reaches the refusal too. Observed by AC2.
- **S3** — Unit 12's arm reads both constants from the driver's own assignment lines, the way
  `tools/unattended/unattended.test.sh` already reads `VERBS_SLUG`, and derives its cell set as
  their product. Before it drives a cell it asserts that its typed outcomes cover exactly that set,
  naming every cell present on one side only. NOT OBSERVED by a criterion here: the suite is the main
  loop's to run at VERIFYING, and the arm's red on a staged break is observed there (§7).
- **S4** — The unattended kit version moves once after this unit's last move, in every carrier
  `tools/check-kit-versions.sh` pairs. Observed by AC3.

## 3. Non-goals (OUT)

- **Changing a cell.** Every outcome is unit 1's table, and every reacher is unit 12's.
- **Parsing `check_claim_writable`'s case labels.** The audit offered it as the other derivation. A
  shell `case` reader is a second parser of the driver, and S2's refusal already makes the constants
  load-bearing for the function.
- **A spec lint joining a decision table's rows to criteria.** Unit 12's §3 declines it, and this
  unit leaves that decline as it stands.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-1` — `check_claim_writable` and its §4 table of eight
  claim-read rows and four modes; without them there is no decision to declare the axes of.
- **consumes-from** `TOOL-aGraftedHelix-12` — the table-driven arm and its reachers; without it
  there is no arm to derive.

## 4. Design

### Evidence

- Unit 12 S3 has the arm assert that "its own table holds rows × columns cells", which reads only
  the arm's own rows.
- The round-1 audit's finding 46 made the arm a gate "provided it derives its cell list from the
  section 4 table rather than from a second typed copy".
- `tools/unattended/unattended.test.sh:2456` reads `VERBS_SLUG` from the driver with one `sed -n`
  over its assignment line, so reading a driver constant is an existing suite shape.

### The constants

| constant | members, in order |
|---|---|
| `CLAIM_READS` | `none` `mine` `same-session` `foreign-live` `foreign-held` `foreign-stale` `foreign-terminal` `unknown` |
| `CLAIM_MODES` | `preflight` `take-over` `holder` `status-write` |

The spellings are the classes unit 1 §4 "Who may write a claim" names, hyphenated so each is one
shell word. Where unit 1's build already spelled a class or mode as one word, the constant takes
that spelling instead, so the function and the constant agree.

### The staged break

In a scratch copy of the driver, a phantom member is appended to `CLAIM_MODES`. The arm then reds
before it drives a cell, naming the four phantom cells it has no outcome for. That is the observation
a row-count assertion could not make.

### Inventory

New constants `CLAIM_READS` and `CLAIM_MODES` in `tools/unattended/unattended.sh`. No new function,
check, conf key or file. A constant is not a lexicon cell here, and no codebase-map key is minted.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- every other carrier of the unattended version marker, which `tools/check-kit-versions.sh`
  enumerates

## 5. Production-readiness checklist

- security — No new surface. The refusal only narrows what the decision accepts.
- perf / scale — Two membership tests per decision, in-process.
- error / empty / loading states — An undeclared class or mode is a named refusal with no write.
- observability — The refusal names the value and the constant it is missing from.
- risks — A caller passing a mode the function used to accept silently now refuses. Unit 1 declares
  exactly four call-site modes, so every caller passes a member.
- testing — S3's derived-set assertion, observed RED with a phantom mode.
- migration — None: the table lands with unit 1 in this build.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `grep -E '^CLAIM_(READS|MODES)=' tools/unattended/unattended.sh` runs at the
  pass's commit, it prints two lines. The quoted value of `CLAIM_READS` holds eight words, and that
  of `CLAIM_MODES` four.
  Red when: an axis is missing, or holds a count other than unit 1's table.
- **AC2** — When a scratch copy of the driver whose `--hold` call site passes a mode not in
  `CLAIM_MODES` runs `--hold <slug>` over unit 1's fixture, it prints a line naming that mode and
  `CLAIM_MODES`, and `git ls-remote <bare> refs/gov/runs/<slug>` prints the same sha before and
  after.
  Red when: an undeclared mode reaches a cell.
- **AC3** — When `bash tools/check-kit-versions.sh` runs at the pass's commit it exits 0, and
  `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` names no unattended carrier
  left behind.
  Red when: the driver's bytes moved and the unattended version did not.

## 7. Gates

`unattended kit gate` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `harness arms (fail branches armed or pinned)` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · the per-cell arm's derived-set assertion over CLAIM_READS and CLAIM_MODES; stage a phantom member appended to CLAIM_MODES · the suite's floor rises by its new arm count

The unattended suites are not on the bar (`tools/unattended/README.md`). A pass runs the arm as a
slice, and the main loop runs the suite once at VERIFYING.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, promoted from finding 31 of the round-1 spec audit of units 10
  to 15.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a test arm derives its decision table cells from the
implementation's declared enumerations"` ranked name-stem neighbours only, with
`unscanned layers: .sh`. The seam extended is the suite's existing read of a driver constant, the
`VERBS_SLUG` line at `tools/unattended/unattended.test.sh:2456`. The recall probe returned the
round-1 audit's finding 46, which set the derivation as the arm's condition, and
`TOOL-aKeyedAnnotation-10`, a derive-over-author ruling for a pair list, and no record of a decision
table declared as constants.

Recall terms used: derive enumeration constant case labels table arm cells verdict mode second copy class gate drift
