# TOOL-aGraftedHelix-12 — every cell of the claim write table, and every write `--beat` declines, is observed

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-1 · base 5266d22e · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md](../prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md) | journal | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9 TOOL-aGraftedHelix-10 TOOL-aGraftedHelix-11 TOOL-aGraftedHelix-13 TOOL-aGraftedHelix-14 TOOL-aGraftedHelix-15 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aGraftedHelix-1` §4 "Who may write a claim" decides every claim write by an eight-row,
four-column table, and its criteria observe eleven of the thirty-two cells. No criterion observes
the refusing cells that stop a double drive: a foreign `held` or `unknown` claim at `--preflight`,
and a foreign `terminal` or `unknown` claim at a take-over. No criterion observes `--beat` declining
to write either, so a `--beat` that skips its `mine` test overwrites a claim another node took over.
This unit observes those cells directly and adds a table-driven suite arm over every cell. It closes
findings 2 and 3 (HIGH) of the round-1 spec audit.

## 2. Scope (IN)

- **S1** — The four refusing cells finding 2 names are observed in a fixture: `--preflight` over a
  foreign `held` claim and over an `unknown` claim, and a take-over over a foreign `terminal` claim
  and over an `unknown` claim. Each refuses with check 89 and writes nothing local. Observed by AC1.
- **S2** — `--beat` declining to write is observed in a fixture: over a claim another session holds
  `live`, and over this run's claim with a beat younger than a quarter of `RESUME_STALE_BOUND`.
  Each prints a `skipped:` line and moves no ref. Observed by AC2.
- **S3** — A table-driven arm in `tools/unattended/unattended.test.sh` holds one row per cell of
  the table `check_claim_writable` implements: the claim-read row, the mode, the reacher that drives
  that mode, and the outcome. The outcome is the exit, the check number, whether the claim ref's
  sha moved and whether the run-state file changed, or `unreached` with the reason no path reaches
  the cell. The arm seeds each claim state with real `gov-claim` messages over a bare remote. It
  asserts that its own table holds rows × columns cells before it drives one, so a missing row reds
  rather than shrinking the arm. NOT OBSERVED by a criterion here: the suite is the main loop's to
  run at VERIFYING, and each cell's red on a staged break is observed there (§7).
- **S4** — The unattended kit version moves once after this unit's last move if its shipped bytes
  moved, in every carrier `tools/check-kit-versions.sh` pairs. Observed by AC3.

## 3. Non-goals (OUT)

- **Changing a cell.** The table is unit 1's. This unit observes the table as unit 1's latest rev
  states it, including that rev's holder-column `stale` cell.
- **A spec lint joining a decision table's rows to criteria.** The audit offered it as a class
  gate. It would be a new reader of spec prose, and this arm is the class gate for this table.
- **The resume matrix.** `TOOL-dDerivedDocket-40` records the same class for the resume matrix of
  `TOOL-dDerivedDocket-4`; this arm moves neither its guide nor its leg.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-1` — `check_claim_writable`, its §4 table and its four
  call-site modes, and `--beat`; without them there is no cell to drive.

## 4. Design

### The reachers

| mode | reacher |
|---|---|
| preflight | `--preflight <slug>` from a fresh clone under a new session and keepalive |
| take-over | a different session's `--resume` reaching `run_takeover` on a presumed-stopped record |
| holder | `--resume <slug> --keepalive-id <recorded id>`, and `--beat <slug>` for S2 |
| status write | `--hold <slug>`, on a fixture reset per cell |

Each cell starts from a fresh fixture state, so no cell's write is the next cell's input. The ref's
sha is read with `git ls-remote <bare> refs/gov/runs/<slug>` before and after, and the run-state
file is compared byte for byte.

### Files touched (estimate)

- `tools/unattended/unattended.test.sh`
- every other carrier of the unattended version marker, which `tools/check-kit-versions.sh`
  enumerates

## 5. Production-readiness checklist

- security — N/A: test arms only.
- perf / scale — Thirty-two fixture states, each a seeded ref and one driver call. The arm runs
  inside the unattended suites, which are off the bar.
- error / empty / loading states — An `unreached` cell carries its reason, so a skip announces
  itself.
- observability — Each cell's failure names its row and column.
- risks — A cell no reacher reaches stays unobserved; its `unreached` mark is the record of that.
- testing — S3's arm, each cell observed RED once with its branch of `check_claim_writable`
  reverted.
- migration — None.
- user docs — N/A.

## 6. Acceptance criteria

The fixture is unit 1's: a `git clone --local` of this repository under `%TEMP%`, its one remote
re-pointed at a bare repository, claims seeded with `git commit-tree` over the empty tree.

- **AC1** — When `bash tools/unattended/unattended.sh --preflight <slug> --keepalive-id k2` runs
  from a new session over a foreign `held` claim, and again over an `unknown` claim, each exits with
  `UNATTENDED check 89 FAILED` and the clone holds no run-state file for the slug. When a different
  session's `--resume` reaches `run_takeover` over a foreign `landed` claim, and again over an
  `unknown` claim, each exits with check 89 and the run-state file is byte-unchanged.
  Red when: any of the four cells takes the claim.
- **AC2** — When `bash tools/unattended/unattended.sh --beat <slug>` runs over unit 1's tick
  fixture, whose run `--liveness` reads `LIVE` on this host, with the claim rewritten to another
  session `live`, it prints `unattended: beat — <slug> · skipped:` naming a claim not this run's,
  and `git ls-remote <bare> refs/gov/runs/<slug>` prints the same sha before and after. With this
  run's own claim at a beat younger than a quarter of `RESUME_STALE_BOUND`, it prints the skipped
  line naming a beat not yet due, and the sha is unchanged.
  Red when: `--beat` writes over another session's live claim or a beat not yet due, or the
  skipped line names the verdict, which means the fixture never reached the claim test.
- **AC3** — When `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` runs at the
  pass's commit, it names no unattended carrier left behind.
  Red when: the suite's bytes moved and the unattended version did not.

## 7. Gates

`unattended kit gate` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · the cell table over every row and column of check_claim_writable's table; stage each branch of check_claim_writable reverted in turn · the suite's floor rises by its new arm count

The unattended suites are not on the bar (`tools/unattended/README.md`). A pass runs the arm as a
slice, and the main loop runs the suite once at VERIFYING.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, promoted from the round-1 spec audit's findings 2 and 3.

## 10. Reuse audit

No existing seam fits a per-cell arm: the driver suite's claim blocks are unit 1's and observe eleven
cells. The arm extends the suite's fixture builder and unit 1's seeding of real `gov-claim`
messages. The recall probe run for this set returned the hook and lease rulings and no per-cell
arm. The round-1 audit record names the open ask `TOOL-dDerivedDocket-40`, the same class for the
resume matrix, cited as prior art in §3 and given no header verb.

Recall terms used: pre-push default-branch GOV_DEFAULT_BRANCH remote name URL refusal resolve_remote_name tick session keepalive lease
