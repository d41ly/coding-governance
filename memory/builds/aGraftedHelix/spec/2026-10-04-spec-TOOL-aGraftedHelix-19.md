# TOOL-aGraftedHelix-19 — the claim write table's rows and modes are driver constants the decision refuses outside of, and the per-cell arm derives its cells from them

**Status:** SPECCED · rev-2 · 2026-10-04 · node a · Tier-1 · base 5266d22e · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-review-TOOL-aGraftedHelix-16-spec-audit-round1.md](../reviews/2026-10-04-review-TOOL-aGraftedHelix-16-spec-audit-round1.md) | spec-audit | TOOL-aGraftedHelix-16 TOOL-aGraftedHelix-17 TOOL-aGraftedHelix-18 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aGraftedHelix-12`'s table-driven arm holds one typed row per cell of the claim write table
`check_claim_writable` implements, and checks its own completeness only by counting its own rows. That
catches a row dropped from the arm. It cannot see a claim-read class or a mode added to the function
later, so the arm stays green over an uncovered cell. Unit 12 rev-2 declares its arm an instance check
on that account and hands the derivation to this unit. The round-1 audit admitted the arm as a gate
only if it derived its cells rather than keeping a second typed copy. This unit gives the table's two
axes one declaration in the driver, makes the decision refuse a mode outside it, and has the arm
derive its cells from that declaration. It closes finding 31 (HIGH) of the round-1 spec audit of
units 10 to 15.

## 2. Scope (IN)

- **S1** — `tools/unattended/unattended.sh` declares the table's axes as two constants beside
  `check_claim_writable`, each on one assignment line of the `NAME="…"` form `VERBS_SLUG` uses:
  `CLAIM_READS`, the eight claim-read classes in the §4 table's row order, and `CLAIM_MODES`, the four
  modes in its column order. Observed by AC1.
- **S2** — `check_claim_writable` refuses a mode outside `CLAIM_MODES` before any claim write, as a
  `fail <n>` branch: a new check, numbered one above the highest `fail <n>` in the driver at the
  pass's parent, whose message names the mode and `CLAIM_MODES`. A mode passed by a call site
  without its constant member therefore fails on its first use. A member added to the constant
  without a case branch passes this test; S3's derived-set assertion catches that direction, through
  the cells it has no typed outcome for. The refusal of a claim-read class outside `CLAIM_READS` is
  `TOOL-aGraftedHelix-22`'s. Observed by AC2.
- **S3** — Unit 12's arm reads both constants from the driver's own assignment lines, the way
  `tools/unattended/unattended.test.sh` already reads `VERBS_SLUG`, and derives its cell set as
  their product. Before it drives a cell it asserts that its typed outcomes cover exactly that set,
  naming every cell present on one side only. NOT OBSERVED by a criterion here: the suite is the main
  loop's to run at VERIFYING, and the arm's red on a staged break is observed there (§7).
- **S4** — The unattended kit version moves once after this unit's last move, in every carrier
  `tools/check-kit-versions.sh` pairs. Observed by AC3.
- **S5** — `tools/unattended/unattended.test.sh` gains a standing arm for S2's refusal. In a scratch
  copy of the driver, `CLAIM_MODES` lacks the existing member `status-write`, so the value still has
  its branch. The arm drives `--hold` over a claim this run holds and asserts S2's refusal line
  naming `status-write` and `CLAIM_MODES`, and an unmoved claim ref. Its staged break takes the
  membership test out of the copy: the value then reaches its branch, the claim is written, and the arm
  reds. This is the arm `tools/memory-tree/check-arms.py` requires of S2's `fail <n>` branch.
  Observed by AC2, which makes the arm's observation and its staged break directly; the arm itself
  is the suite's, which the main loop runs at VERIFYING.

## 3. Non-goals (OUT)

- **Changing a cell.** Every outcome is unit 1's table, and every reacher is unit 12's.
- **Parsing `check_claim_writable`'s case labels.** The audit offered it as the other derivation. A
  shell `case` reader is a second parser of the driver. S2's refusal and `TOOL-aGraftedHelix-22`'s
  make the constants load-bearing for the values the function meets, and S3's derived-set assertion
  catches a member with no branch.
- **A spec lint joining a decision table's rows to criteria.** Unit 12's §3 declines it, and this
  unit leaves that decline as it stands.
- **The read axis.** Refusing a derived claim-read class outside `CLAIM_READS`, its criterion and
  its standing arm are `TOOL-aGraftedHelix-22`'s (§3 Edges).

### Edges

- **consumes-from** `TOOL-aGraftedHelix-1` — `check_claim_writable` and its §4 table of eight
  claim-read rows and four modes; without them there is no decision to declare the axes of.
- **consumes-from** `TOOL-aGraftedHelix-12` — the table-driven arm and its reachers; without it
  there is no arm to derive.
- **hands-off** `TOOL-aGraftedHelix-22` — the refusal of a claim-read class outside `CLAIM_READS`,
  numbered one above S2's check, with a criterion that drives it and a standing arm that keeps it
  (finding 6 of the round-1 audit of units 16 to 19).

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
before it drives a cell, naming one phantom cell per `CLAIM_READS` member, each a cell it has no
outcome for. The arm prints the count; this spec does not type it. That is the observation a
row-count assertion could not make.

### The refusal's stimulus

S5's arm and AC2 REMOVE an existing member rather than pass a phantom value. A removed member keeps
its case branch, so the break that deletes the membership test lets the value reach that branch and
write, and the arm reds. A phantom value has no branch, and a default branch refusing with the same
text would keep the arm green with the membership test gone (finding 12's skeptic).

### Inventory

New constants `CLAIM_READS` and `CLAIM_MODES` in `tools/unattended/unattended.sh`. One new check,
S2's, numbered at build time as S2 states, with its message and its standing arm. No new function,
conf key or file. A constant is not a lexicon cell here, and no codebase-map key is minted.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- every other carrier of the unattended version marker, which `tools/check-kit-versions.sh`
  enumerates

## 5. Production-readiness checklist

- security — No new surface. The refusal only narrows what the decision accepts.
- perf / scale — Two membership tests per decision, in-process.
- error / empty / loading states — An undeclared mode is a named refusal with no claim write.
- observability — The refusal names the value and the constant it is missing from.
- risks — A caller passing a mode the function used to accept silently now refuses. Unit 1 declares
  exactly four call-site modes, so every caller passes a member.
- testing — S3's derived-set assertion, observed RED with a phantom mode, and S5's arm, observed RED
  with the membership test removed.
- migration — None: the table lands with unit 1 in this build.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `grep -E '^CLAIM_(READS|MODES)=' tools/unattended/unattended.sh` runs at the
  pass's commit, it prints two lines. The quoted value of `CLAIM_READS` holds eight words, and that
  of `CLAIM_MODES` four.
  Red when: an axis is missing, or holds a count other than unit 1's table.
- **AC2** — When a scratch copy of the driver with `status-write` removed from `CLAIM_MODES` runs
  `--hold <slug> --code <a declared hold code> --until owner --reason <text> --reaped <the recorded
  keepalive>` over unit 1's fixture, whose branch tip is pushed and whose claim this run holds, it
  prints `UNATTENDED check <n> FAILED` naming `status-write` and `CLAIM_MODES`, and
  `git ls-remote <bare> refs/gov/runs/<slug>` prints the same sha before and after. With the
  membership test also removed from the copy, the same call moves that sha.
  Red when: an undeclared mode reaches a cell.
- **AC3** — When `bash tools/check-kit-versions.sh` runs at the pass's commit it exits 0, and
  `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` names no unattended carrier
  left behind.
  Red when: the driver's bytes moved and the unattended version did not.

## 7. Gates

`unattended kit gate` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `harness arms (fail branches armed or pinned)` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · the per-cell arm's derived-set assertion over CLAIM_READS and CLAIM_MODES; stage a phantom member appended to CLAIM_MODES · the suite's floor rises by its new arm count

New arm: tools/unattended/unattended.test.sh · S2's refusal, driven at --hold over a scratch driver with status-write removed from CLAIM_MODES; stage the membership test removed · the suite's floor rises by its new arm count

The unattended suites are not on the bar (`tools/unattended/README.md`). A pass runs the arm as a
slice, and the main loop runs the suite once at VERIFYING.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, promoted from finding 31 of the round-1 spec audit of units 10
  to 15.
- rev-2 · 2026-10-04 · §1 §2 §3 §4 §5 §6 §7 · S2 S5 · AC2 · folded the round-1 spec audit of units 16
  to 19 on this unit. Findings 12 and 20: S2 drops the false clause that a branchless constant member
  reaches the refusal, pins the refusal as a numbered `fail <n>` check, and S5 adds its standing arm,
  stimulated by a removed member. Finding 8: AC2 spells `--hold`'s required arguments. Finding 13:
  the staged break names one phantom cell per `CLAIM_READS` member and types no count. Finding 14:
  §1 cites unit 12 rev-2. Finding 6 is promoted to `TOOL-aGraftedHelix-22`, which takes the read
  axis's refusal; §3 gains its hands-off and a non-goal.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a test arm derives its decision table cells from the
implementation's declared enumerations"` ranked name-stem neighbours only, with
`unscanned layers: .sh`. The seam extended is the suite's existing read of a driver constant, the
`VERBS_SLUG` line at `tools/unattended/unattended.test.sh:2456`. The recall probe returned the
round-1 audit's finding 46, which set the derivation as the arm's condition, and
`TOOL-aKeyedAnnotation-10`, a derive-over-author ruling for a pair list, and no record of a decision
table declared as constants.

Recall terms used: derive enumeration constant case labels table arm cells verdict mode second copy class gate drift
