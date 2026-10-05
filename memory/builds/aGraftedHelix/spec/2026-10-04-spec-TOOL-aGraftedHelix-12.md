# TOOL-aGraftedHelix-12 — every cell of the claim write table, and every write `--beat` declines, is observed

**Status:** SPECCED · rev-4 · 2026-10-05 · node a · Tier-1 · base 5266d22e · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md](../prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md) | journal | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9 TOOL-aGraftedHelix-10 TOOL-aGraftedHelix-11 TOOL-aGraftedHelix-13 TOOL-aGraftedHelix-14 TOOL-aGraftedHelix-15 |
| [2026-10-04-review-TOOL-aGraftedHelix-10-spec-audit-round1.md](../reviews/2026-10-04-review-TOOL-aGraftedHelix-10-spec-audit-round1.md) | spec-audit | TOOL-aGraftedHelix-10 TOOL-aGraftedHelix-11 TOOL-aGraftedHelix-13 TOOL-aGraftedHelix-14 TOOL-aGraftedHelix-15 |

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
  sha moved, whether the run-state file changed and the line the call printed (`taken` for `claim
  taken over`, `announced` for the announce row's `claim not written`, `lost` for a write whose
  push lost), or `unreached` with the reason no path reaches the cell. The line field is what tells
  a `take, announced` cell from a `take` one, an `announce` cell from a refusal that wrote nothing,
  and the table's own check 90 or announcement from a race lost by a row misread as `none`, whose
  exit, check, ref and record coincide with them. The arm seeds each claim state with real
  `gov-claim` messages over a bare remote. It
  asserts that its own table holds rows × columns cells before it drives one, so a missing row reds
  rather than shrinking the arm. That count reads only the arm's own rows; deriving the cell set from
  the driver, so a class or mode added later reds too, is `TOOL-aGraftedHelix-19`'s. NOT OBSERVED by a criterion here: the suite is the main loop's to
  run at VERIFYING, and each cell's red on a staged break is observed there (§7).
- **S4** — The unattended kit version moves once after this unit's last move if its shipped bytes
  moved, in every carrier `tools/check-kit-versions.sh` pairs. Observed by AC3.

## 3. Non-goals (OUT)

- **Changing a cell.** The table is unit 1's. This unit observes the table as unit 1's latest rev
  states it, including that rev's holder-column `stale` cell.
- **A spec lint joining a decision table's rows to criteria.** The audit offered it as a class
  gate. It would be a new reader of spec prose. This arm becomes the class gate for this table only
  once `TOOL-aGraftedHelix-19` derives its cells from the driver; built alone, it is an instance
  check over today's thirty-two cells.
- **The resume matrix.** `TOOL-dDerivedDocket-40` records the same class for the resume matrix of
  `TOOL-dDerivedDocket-4`; this arm moves neither its guide nor its leg.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-1` — `check_claim_writable`, its §4 table and its four
  call-site modes, and `--beat`; without them there is no cell to drive.
- **hands-off** `TOOL-aGraftedHelix-19` — the arm's cell set: that unit declares the table's rows
  and modes as driver constants the decision refuses outside of, and has this arm derive its cells
  from them in place of its own row count (round-1 audit of units 10 to 15, finding 31).

## 4. Design

### The reachers

| mode | reacher |
|---|---|
| preflight | `--preflight tFresh` under a new session and keepalive, in the suite's armed fixture, where the slug has no run-state file |
| take-over | a different session's `--resume` reaching `run_takeover` on a presumed-stopped record |
| holder | `--resume <slug> --keepalive-id <recorded id>`, and `--beat <slug>` for S2 |
| status write | `--hold <slug>`, on a fixture reset per cell |

Each cell starts from a fresh fixture state, so no cell's write is the next cell's input. The ref's
sha is read with `git ls-remote <bare> refs/gov/runs/<slug>` before and after, and the run-state
file is compared byte for byte. The preflight reacher needs no clone: each cell resets the tree to
its mode's committed base and clears every claim, so the tree holds no run-state file for the slug,
which is all a fresh clone bought. The `mine` row's claim is aged a third of `RESUME_STALE_BOUND`, so
the holder cell `renew when due` is observed through its due half; the not-due half is unit 1's AC7
and AC18 arms and this unit's AC2. All thirty-two cells are reached, so the arm carries no
`unreached` row today; the form stays, so a cell a later change makes unreachable announces itself.

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

The fixture is the driver suite's claim fixture, unit 1's: a scratch repository under `%TEMP%`, its
one remote a bare repository, claims seeded with `git commit-tree` over the empty tree.

- **AC1** — When `bash tools/unattended/unattended.sh --preflight <slug> --keepalive-id k2` runs
  from a new session over a foreign `held` claim, and again over an `unknown` claim, each exits with
  `UNATTENDED check 89 FAILED` and the tree holds no run-state file for the slug. When a different
  session's `--resume` reaches `run_takeover` over a foreign `landed` claim, and again over an
  `unknown` claim, each exits with check 89 and the run-state file is byte-unchanged.
  Red when: any of the four cells takes the claim.
- **AC2** — When `bash tools/unattended/unattended.sh --beat <slug>` runs over the claim fixture,
  whose run `--liveness` reads `LIVE` on this host as unit 1's `--beat` arm relies on, with the
  claim rewritten to another session `live`, it prints `unattended: beat — <slug> · skipped:` naming a claim not this run's,
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
- rev-2 · 2026-10-04 · §2 §3 · S3 · the round-1 spec audit of units 10 to 15 promoted its finding
  31 on this unit to `TOOL-aGraftedHelix-19`. S3 and §3 stop calling the arm the class gate on its
  own row count, and §3 gains the hands-off to that unit.
- rev-3 · 2026-10-05 · §2 §4 §6 · S3 AC1 AC2 · the build pass's divergences, before the code. S3's
  outcome gains the printed line, which alone tells `take, announced` from `take` and `announce`
  from a refusal. The preflight reacher runs in the suite's armed fixture rather than a fresh clone,
  since a per-cell reset leaves the slug no run-state file, and AC1 says "tree" for "clone". The
  `mine` seed is aged so the holder cell is observed due. AC2 runs in the driver suite's claim
  fixture, the file §4 names, rather than the tick suite's.
- rev-4 · 2026-10-05 · §2 · S3 · the line field gains `lost`. A staged break making every claim
  read as `none` left eight cells green: the five foreign holder cells and the three status
  announce cells, because a create pushed against the empty lease loses, and that is check 90 or a
  `claim not written` line with the ref unmoved, the same tuple the table's own refusal gives.

## 10. Reuse audit

No existing seam fits a per-cell arm: the driver suite's claim blocks are unit 1's and observe eleven
cells. The arm extends the suite's fixture builder and unit 1's seeding of real `gov-claim`
messages. The recall probe run for this set returned the hook and lease rulings and no per-cell
arm. The round-1 audit record names the open ask `TOOL-dDerivedDocket-40`, the same class for the
resume matrix, cited as prior art in §3 and given no header verb.

Recall terms used: pre-push default-branch GOV_DEFAULT_BRANCH remote name URL refusal resolve_remote_name tick session keepalive lease
