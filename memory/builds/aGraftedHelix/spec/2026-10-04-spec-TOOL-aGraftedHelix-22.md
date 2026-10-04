# TOOL-aGraftedHelix-22 — the claim write decision refuses a derived claim-read class outside `CLAIM_READS`, observed by a criterion and kept by a standing arm

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-1 · base 5266d22e · streams tooling · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aGraftedHelix-19` rev-1 stated two refusals in its S2, a mode outside `CLAIM_MODES` and a
derived claim-read class outside `CLAIM_READS`, and named one criterion that drove only the mode. A
build that omitted the read-axis refusal passed every criterion. Unit 19's per-cell arm derives its
cells from `CLAIM_READS`, so it never drives a class `check_claim_writable` derives and the constant
lacks: a class added to the function later neither refuses nor appears among the derived cells, and
the arm stays green over an uncovered cell. That is finding 31 of the round-1 audit of units 10 to
15, the finding unit 19 exists to close, reopened on the read axis. This unit builds the read-axis
refusal as a numbered check, drives it with a criterion, and keeps it with a standing arm. It closes
finding 6 (HIGH) of the round-1 spec audit of units 16 to 19.

## 2. Scope (IN)

- **S1** — `check_claim_writable` refuses a claim-read class it derives outside `CLAIM_READS`, as a
  `fail <n>` branch: a new check, numbered one above unit 19's mode check, whose message names the
  class and `CLAIM_READS`. The refusal comes after the class is derived and before any claim write,
  and at `--preflight`, whose claim write precedes every local write, before any local write too.
  Observed by AC1.
- **S2** — `tools/unattended/unattended.test.sh` gains a standing arm for S1. In a scratch copy of
  the driver, `CLAIM_READS` lacks the existing member `foreign-stale`, so the class still has its
  case branch. The arm runs `--preflight` over a seeded foreign stale claim and asserts S1's
  refusal line naming `foreign-stale` and `CLAIM_READS`, an unmoved claim ref and no run-state file.
  Its staged break takes the read-axis membership test out of the copy: the class then reaches its
  `take, announced` cell, the claim ref moves, and the arm reds. This is the arm
  `tools/memory-tree/check-arms.py` requires of S1's branch. Observed by AC1, which makes the arm's
  observation and its staged break directly; the arm itself is the suite's, which the main loop runs
  at VERIFYING.
- **S3** — The unattended kit version moves once after this unit's last move, in every carrier
  `tools/check-kit-versions.sh` pairs. Observed by AC2.

## 3. Non-goals (OUT)

- **A criterion that a constant member with no branch reaches the refusal.** The audit offered it as
  a second criterion. It presumed unit 19 rev-1's clause that such a member reaches the refusal,
  which is false, because a member passes the membership test; unit 19 rev-2 deletes that clause, and
  its S3 derived-set assertion owns that direction.
- **The mode axis.** Its refusal, check number, criterion and arm are unit 19's.
- **Changing a cell.** Every outcome is `TOOL-aGraftedHelix-1`'s table.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-19` — `CLAIM_READS` and `CLAIM_MODES` as driver constants,
  the mode refusal whose check this unit numbers above, and the derived-set arm that owns the
  branchless-member direction; without them there is no constant to refuse outside of.

## 4. Design

### Evidence

- Unit 19 rev-1 S2 named "Observed by AC2", and AC2 drove only a mode outside `CLAIM_MODES` at the
  `--hold` site; its staged break and its arm staged only a phantom MODE.
- `fail()` is defined at `tools/unattended/unattended.sh:637`, so `tools/memory-tree/check-arms.py`
  discovers the driver and keys every `fail <n>` call site by its own failure text. A refusal written
  as a call site is under that gate the moment it lands.
- Unit 1's call-site table puts `--preflight`'s claim write after the write gate and before
  rotation, so a refusal there leaves the tree untouched, the shape unit 1's AC6 observes.
- Unit 1's §4 table answers a foreign `stale` claim at `--preflight` with `take, announced`, a cell
  that writes. Removing that class from the constant therefore turns a write into a refusal, which
  is the difference the arm reads.

### The stimulus

The arm and AC1 REMOVE an existing member rather than derive a phantom class. A removed member keeps
its case branch, so the break that deletes the membership test lets the class reach that branch and
write, and the arm reds. A phantom class has no branch, and a default branch refusing with the same
text would keep the arm green with the membership test gone. Unit 19 states the same rule for the
mode axis.

### Inventory

One new check, S1's, numbered at build time as S1 states, with its message and its standing arm. No
new function, constant, conf key or file. No codebase-map key is minted.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- every other carrier of the unattended version marker, which `tools/check-kit-versions.sh`
  enumerates

## 5. Production-readiness checklist

- security — No new surface. The refusal only narrows what the decision accepts.
- perf / scale — One membership test per decision, in-process.
- error / empty / loading states — An undeclared class is a named refusal with no claim write.
- observability — The refusal names the class and the constant it is missing from.
- risks — A class `check_claim_writable` derives today and the constant lacks would refuse on first
  use. Unit 19's constant lists every class unit 1's table names, so none does.
- testing — S2's arm, observed RED with the read-axis membership test removed.
- migration — None: the table lands with unit 1 in this build.
- user docs — N/A.

## 6. Acceptance criteria

The fixture is unit 1's driver fixture: a `git clone --local` of this repository under `%TEMP%`, its
one remote re-pointed at a bare repository, `RUN_CLAIMS` on.

- **AC1** — When a scratch copy of the driver with `foreign-stale` removed from `CLAIM_READS` runs
  `--preflight <slug> --keepalive-id k2` over the fixture, whose bare remote holds a claim for
  `<slug>` written by another session under another keepalive with `status: live` and a `beat-utc`
  older than `RESUME_STALE_BOUND`, it prints `UNATTENDED check <n> FAILED` naming `foreign-stale`
  and `CLAIM_READS`, `git ls-remote <bare> refs/gov/runs/<slug>` prints the same sha before and
  after, and the run-state file does not exist. With the read-axis membership test also removed from
  the copy, the same call takes the claim and that sha moves.
  Red when: an undeclared claim-read class reaches its cell.
- **AC2** — When `bash tools/check-kit-versions.sh` runs at the pass's commit it exits 0, and
  `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` names no unattended carrier
  left behind.
  Red when: the driver's bytes moved and the unattended version did not.

## 7. Gates

`unattended kit gate` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `harness arms (fail branches armed or pinned)` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · S1's refusal, driven at --preflight over a scratch driver with foreign-stale removed from CLAIM_READS and a seeded foreign stale claim; stage the read-axis membership test removed · the suite's floor rises by its new arm count

The unattended suites are not on the bar (`tools/unattended/README.md`). A pass runs AC1 directly,
and the main loop runs the suite once at VERIFYING.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, promoted from finding 6 of the round-1 spec audit of units 16
  to 19, grounded against unit 19 rev-2, unit 1's call-site table and `check-arms.py` at base
  `5266d22e`.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "refuse a derived class outside a declared constant and
arm the refusal"` ranked name-stem neighbours only, `armed` in `tools/memory-tree/corpus_ids.py` and
`refusal` in `tools/memory-recall/recall_conf.py`, and printed `unscanned layers: .sh`, so its miss is
no evidence. The seams extended were read from source: unit 19's constants and mode refusal, and the
`fail <n>` discovery of `tools/memory-tree/check-arms.py`, which already gates every numbered
refusal. No existing seam fits beyond them. The recall probe returned the audit's own M3 and H4
rows, `TOOL-aFoldedQuarry-7`, the ruling that made every `fail` branch armed or pinned, and
`DEPL-aHoistedPass-6`, an armed branch with no behavioural reader, and no record of a refusal
outside a declared constant.

Recall terms used: refusal constant membership fail branch armed pinned check-arms standing arm scratch copy driver

The question passed with them: "how is a refusal outside a declared constant set kept by a standing
arm".
