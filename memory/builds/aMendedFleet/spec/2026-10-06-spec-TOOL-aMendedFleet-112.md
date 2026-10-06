# TOOL-aMendedFleet-112 — four suites' assertion floors cover the arms this build added, unit 75's AC1 names the plain-run form, and the kickoff units are graded Tier-2

**Status:** SPECCED · rev-1 · 2026-10-06 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-06 · order 109

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of this build, round 1, confirmed seven minor findings whose fixes write
records and suite floors only: findings 12, 14, 15, 16 and 17 leave arms this build added outside
the executed-assertion floor of the suite they sit in, finding 20 is an acceptance criterion that
quotes output its own command never prints, and finding 21 is three kickoff units graded Tier-1
that the tier rule grades Tier-2. This unit is the records half of the review's promoted minors.
Its write set is disjoint from `TOOL-aMendedFleet-111`, which takes the code half, so the two build
concurrently. Every finding was re-verified at `e83b29b6`, the reviewed tip, and none is fixed there.

## 2. Scope (IN)

- **S1** — FINDING 12, THE UNATTENDED SUITE'S FLOORS. In `tools/unattended/unattended.test.sh`,
  `FLOOR_SHARD_1` rises by the region-one assertions of `TOOL-aMendedFleet-61` and
  `TOOL-aMendedFleet-63`, `FLOOR_SHARD_2` by the region-two assertions of `TOOL-aMendedFleet-66`,
  `TOOL-aMendedFleet-83`, `TOOL-aMendedFleet-49` S8 and `TOOL-aMendedFleet-9`, and
  `FLOOR_ASSERTIONS` by their sum, each counted off its block as §4's table records. One `RAISED`
  comment line per unit is added above each constant it moves, in the shape the `TOOL-aMendedFleet-60`
  line already has. The S8 block's SKIP branch gains `n=$((n+2))` beside its announce line, so its
  two assertions are COUNTED EITHER WAY, the convention the `TOOL-dMendedRecall-2` SKIP already
  follows, and the floor holds in a tree where no drift-audit kit resolves. Observed by AC1.
  **Readers:** by name: the floor `case` on `SH_I` near the end of the suite, which selects one of
  the three constants, and `tools/check-testsuite-counts.sh`, which reads that a non-zero
  `FLOOR_ASSERTIONS` pin exists. by value: the suite's `[ "$n" -ge "$FLOOR" ]` comparison, the only
  reader that compares the number.
- **S2** — FINDING 14, THE KICK-2 MISCOUNT. The `KICK-aMendedFleet-2` block executes 9 assertions,
  not the 10 both floor comments state. The `RAISED 1892 -> 1902` line under `FLOOR_ASSERTIONS`
  becomes `RAISED 1892 -> 1901` naming 9 lines, and the `RAISED 224 -> 234` line under
  `FLOOR_SHARD_1` becomes `RAISED 224 -> 233` naming 9 assertions. S1's raises chain from the
  corrected figures. Observed by AC2.
  **Readers:** by name: no code reads a `RAISED` comment in this suite; the comment is read by the
  next author who raises the floor. by value: the suite's `[ "$n" -ge "$FLOOR" ]` comparison,
  through the constants the corrected chain sets.
- **S3** — FINDING 15, THE TIER2-REVIEW FLOOR. `FLOOR_ASSERTIONS` in
  `tools/workflows/tier2-review.test.sh` rises from 183 to 195, with one `RAISED 183 -> 195 by
  TOOL-aMendedFleet-67:` comment naming the 12 `ck()` calls of the `workerType` block, whose
  absent-type half `TOOL-aMendedFleet-93` rewrote. Observed by AC3.
  **Readers:** by name: the suite's own floor compare after the runner's summary line, and
  `tools/check-testsuite-counts.sh` for the pin's presence. by value: the
  `[ "$executed" -lt "$FLOOR_ASSERTIONS" ]` compare, which reds when the executed count falls below
  the pin.
- **S4** — FINDING 16, THE RUNLOG FLOOR. `ASSERTION_FLOOR` in `tools/runlog/selftest.py` rises
  from 1554 to 1561. The new `RAISED 1554 -> 1561 by TOOL-aMendedFleet-70:` block is the newest
  move in the file, names `test_extract_ready`'s 4 checks and the 3 decoy checks `main` runs after
  every arm, and ends with the arithmetic line `4 + 3 = 7`. Observed by AC4.
  **Readers:** by name: `main`'s floor compare and `parse_floor_raise`, which the record AC2 arm of
  `test_record_placement_windows` calls on the suite's own source. by value: that arm, which
  requires the newest move to reach `ASSERTION_FLOOR`, to name the unit that made it, and to carry
  arithmetic summing to the move.
- **S5** — FINDING 17, THE MANIFEST-CHECK FLOOR. `FLOOR_ASSERTIONS` in
  `skills/session-kickoff/manifest-check.test.sh` rises from 207 to 216, with a `+9` comment line
  naming the `drift —` cell's five `run_card` and four `check_eq` calls of `KICK-aMendedFleet-1`,
  below the `+8` and `+19` lines. Observed by AC5.
  **Readers:** by name: the suite's `[ "$pass" -ge "$FLOOR_ASSERTIONS" ]` line and
  `tools/check-testsuite-counts.sh`. by value: the `[ "$pass" -ge "$FLOOR_ASSERTIONS" ]` line,
  the only reader that compares the number.
- **S6** — FINDING 20, UNIT 75'S AC1 WORDING. `TOOL-aMendedFleet-75` takes a rev-4 bump whose AC1
  asks the plain run for what it prints: a line carrying `[covers]` and the composite token
  `covers <- <fixture spec> AC9`, and none naming `AC1`. The `HIT` wording leaves AC1. The bump
  adds its §9 line with the scope token `AC1`, and the header date moves to the bump's date; the
  status stays CLOSED. Observed by AC6.
  **Readers:** by name: `tools/check-spec-tokens.py`, whose covers join reads the `AC1` label and
  not its prose; the spec is Tier-1 and owes no acceptance ledger. by value: NO VALUE READERS —
  the criterion's prose is read by a person re-running it, and no tool compares it.
- **S7** — FINDING 21, THE KICKOFF UNITS' TIER. `KICK-aMendedFleet-1`, `KICK-aMendedFleet-2` and
  `KICK-aMendedFleet-4` are re-graded Tier-2, each by a rev bump that changes the header's tier,
  moves its date and adds one sentence to its §4 `### Evidence` naming the tier rule's clause that
  grades it: KICK-2 adds the `--overlaps` flag to the unattended driver and a card cell in the same
  commit, a cross-kit change; KICK-1's cell reads the drift-audit kit's `drift-history.tsv` header
  contract; KICK-4's cell spells the unattended driver's `AI_AGENT` version rule a second time. Each
  bump's §9 line carries the scope token `§4`. One acceptance-ledger journal record per unit is
  added under the build's `build/` folder, answering every criterion in the OBSERVED form from the
  observations its commit message records: `6f2c55785` for KICK-1, `481eb9f39` and `b2762c788` for
  KICK-2, `f3e9f93d7` for KICK-4. The build README is re-rendered. Observed by AC7.
  **Readers:** by name: `tools/memory-tree/check-memory-hygiene.sh`, whose status-header read skips
  a `Tier-1` header before the section canon and check 23's ledger join, and
  `tools/memory-tree/gen_build_index.py`, which renders each spec's tier into the README roster.
  by value: check 23 of `tools/memory-tree/check-memory-hygiene.sh`, which now demands a ledger
  line per criterion of the three CLOSED units; the tier column and the "Ids no record names" list
  that `tools/memory-tree/gen_build_index.py` renders into `memory/builds/aMendedFleet/README.md`,
  the second of which the three ledgers drain of the three ids.

## 3. Non-goals (OUT)

- The code findings of the same review: 3, 4, 5, 6, 7, 9, 10, 18 and 19 are
  `TOOL-aMendedFleet-111`'s, and finding 1 is `TOOL-aMendedFleet-110`'s.
- The class gates the review proposes as left-shifts for findings 12 to 17 and 21. §8 F1 and F2
  split each to a unit the run adds.
- Any arm. This unit adds no assertion and moves none; it re-prices the floors over arms that exist.
- Raising a floor for an arm `TOOL-aMendedFleet-111` adds. That unit raises the floor of any suite
  it adds arms to, by its own count, in its own commit.
- KICK-aMendedFleet-3. The review names KICK-1, -2 and -4 only.
- Any other unit's tier. The finding names these three, and a corpus-wide tier audit is F2's unit.
- Bumping the kit versions of the four suites' kits. Many units of this build move those kits; the
  bump is owed once, at the close.

### Edges

- **hands-off** external — the floor-delta class gate, built by the unit §8 F1 splits out.
- **hands-off** external — the Tier-1 cross-kit class gate, built by the unit §8 F2 splits out.
- **hands-off** external — the kit version bumps, owed once at the build's close.

## 4. Design

### Evidence

Read at `e83b29b6`, the reviewed tip and this worktree's HEAD, on 2026-10-06.

- Base `7af5f564` pins `FLOOR_SHARD_1=209`, `FLOOR_SHARD_2=1680` and `FLOOR_ASSERTIONS=1877` in
  the unattended suite, 180 in the tier2-review suite, 180 in the manifest-check suite and 1543 in
  the runlog selftest. HEAD pins 234, 1680, 1902, 183, 207 and 1554. PINNED, read with
  `git show 7af5f564:<path>` and a grep of each constant.
- `git diff 7af5f564 HEAD` over the unattended suite adds 72 lines carrying `hit`, `miss`, `same`,
  `mutate` or an `n=$((n+1))` guard and removes none; the review's figure, re-measured.
- The KICK-2 block executes `same`, `hit`, `hit`, `hit`, `miss`, `hit`, `same`, `hit`, `miss`: 9.
- The `workerType` block of the tier2-review suite executes 12 `ck()` calls on its green path: one
  unconditional, one in the absent-type run, seven in the explicit-Plan run and three in the
  refusal loop. `checkNoThrow` counts a failure only.
- `test_extract_ready` carries 4 `check()` calls, and `git show` of the other three commits that
  touched the runlog selftest in this range adds 8 for `TOOL-aMendedFleet-58`, already priced, and
  none for `TOOL-aMendedFleet-97`.
- The manifest-check diff adds 8 assertions for KICK-2, 19 for KICK-4 and 9 for KICK-1, and the
  floor comment prices only the first two.
- `check-spec-tokens.py` prints the `HIT` prefix only under `--list`; a plain run prints
  `spec-tokens: <spec> [covers] ` then the backticked token, the form the covers arm of
  `tools/check-spec-tokens.test.sh` asserts.
- A scratch clone of HEAD under `%TEMP%` with the three KICK headers flipped to Tier-2 and
  `check-memory-hygiene.sh` run over it reported two findings and no other: check 23 naming all 16
  criteria of the three units, and check 9 naming the README's stale roster tier column. No
  section-canon, Edges, §8 or §10 finding fired: the three specs already carry the Tier-2 shape. The
  run took 77 s on node a. PINNED, measured 2026-10-06.

### Inventory — the unattended suite's blocks

Executed assertions per block, counted off each block's own lines with its loop and branches
expanded. PINNED at `e83b29b6` on 2026-10-06; the build re-derives them by the same count.

| Unit | Block line | Region | Executed | Floor today |
|---|---|---|---|---|
| `TOOL-aMendedFleet-60` | 728 | one | 15 | priced |
| `KICK-aMendedFleet-2` | 783 | one | 9 | priced as 10, S2 |
| `TOOL-aMendedFleet-61` | 1308 | one | 19 | unpriced |
| `TOOL-aMendedFleet-63` | 1595 | one | 11, a loop of 7 with the runlog kit present and 4 without | unpriced |
| `TOOL-aMendedFleet-66` | 9349 | two | 2 | unpriced |
| `TOOL-aMendedFleet-83` | 9369 | two | 2 | unpriced |
| `TOOL-aMendedFleet-49` S8 | 9783 | two | 2, behind a SKIP that S1 makes count 2 | unpriced |
| `TOOL-aMendedFleet-9` | 11719 | two | 16 | unpriced |

The resulting pins, from base: `FLOOR_SHARD_1` 209 + 15 + 9 + 19 + 11 = 263; `FLOOR_SHARD_2`
1680 + 2 + 2 + 2 + 16 = 1702; `FLOOR_ASSERTIONS` 1877 + 54 + 22 = 1953. The raise chain under
`FLOOR_ASSERTIONS` reads 1892 -> 1901 for KICK-2, then 1901 -> 1920, 1931, 1933, 1935, 1937 and
1953 for units 61, 63, 66, 83, 49 and 9 in suite order. The other three pins: 195, 1561, 216.

No identifier is minted. The three ledger records are new files.

### Rollout

The four suite edits are comment lines, one SKIP-branch counter and four constants. No suite runs
in the pass; each figure is the static count above, and the suites' executed counts are owed once,
after the build, as the `New arm:` lines in §7 declare. If `TOOL-aMendedFleet-111` lands first and
raises a floor in one of these suites, this unit's raise stacks on that value and its `RAISED`
lines chain from it; the per-unit deltas in §4 do not change.

The KICK rev bumps, the three ledgers and the README re-render land in one commit, because check 23
reds the moment a header reads Tier-2 without its ledger, and check 9 reds until the roster's tier
column is re-rendered. The ledgers are tracked before `gen_build_index.py --write` runs, since the
generator sees tracked files only.

### Files touched (estimate)

- `tools/unattended/unattended.test.sh`
- `tools/workflows/tier2-review.test.sh`
- `tools/runlog/selftest.py`
- `skills/session-kickoff/manifest-check.test.sh`
- `memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-75.md`
- `memory/builds/aMendedFleet/spec/2026-10-04-spec-KICK-aMendedFleet-1.md`
- `memory/builds/aMendedFleet/spec/2026-10-04-spec-KICK-aMendedFleet-2.md`
- `memory/builds/aMendedFleet/spec/2026-10-04-spec-KICK-aMendedFleet-4.md`
- three new ledger records, `2026-10-06-build-KICK-aMendedFleet-<n>-1-acceptance-ledger.md` for
  n of 1, 2 and 4, under the build's own build folder
- `memory/builds/aMendedFleet/README.md`, re-rendered

### Alternatives rejected

- **Leave the S8 SKIP branch uncounted and price only this repo's run.** This repo resolves the
  drift-audit kit, so the arm executes here, but an adopter without that kit would red the floor on
  an arm that announces its own skip. The suite's two existing SKIP conventions both count.
- **Lower the floors by the phantom KICK-2 assertion with a new LOWERED line.** The miscount is in
  the raise itself; correcting the raise keeps one line per unit and a chain that adds up.
- **Reword unit 75's AC1 to name `--list`.** The covers arm in the spec-tokens suite asserts the
  plain form, so naming that form keeps the criterion and the suite observing one output.
- **Record in each KICK spec why the card cell falls outside the tier rule.** The rule names a
  cross-kit change and a changed kit contract, and KICK-2 adds a driver flag in the same commit as
  a card cell; a waiver argued against the rule's own text is a second answer to one question.

## 5. Production-readiness checklist

- security — N/A: comments, four integers, one counter in a SKIP branch and records; no input,
  write path or surface moves.
- perf / scale — N/A: no arm is added, so no suite gets slower.
- error / empty / loading states — the S8 SKIP branch now counts what it skips, as the suite's two
  existing SKIP conventions do; every other path is unchanged.
- observability — each raise is a `RAISED` line naming its unit and its count, so the next author
  can re-derive the pin from the comments.
- risks — a floor priced above what the suite executes reds the close's suite runs. The counts are
  static, so a branch the table misreads shows there first; §4 expands every loop and branch.
- testing — AC1 to AC7 here, and the four suites' executed counts at the close per §7.
- migration — N/A: nothing stored changes shape.
- user docs — N/A: no user-facing behaviour moves.

## 6. Acceptance criteria

- **AC1** — When the unattended suite's three constants are read at base by `git show` of
  `7af5f564` and in the working file by `grep -n "^FLOOR_" tools/unattended/unattended.test.sh`,
  `FLOOR_SHARD_1` has risen by at least 54, `FLOOR_SHARD_2` by at least 22 and
  `FLOOR_ASSERTIONS` by at least 76, every unit row of §4's table is named by one `RAISED` line
  under each constant its region moves, and the S8 SKIP branch carries `n=$((n+2))`.
  Red when: a block in §4's table can be deleted and the executed count still meets the floor its
  region reads, which is the case whenever a pin is below base plus the table's sum.
  figure: DERIVED from the per-block count at observation time; 263, 1702 and 1953 at writing.
- **AC2** — When `grep -n "KICK-aMendedFleet-2" tools/unattended/unattended.test.sh` runs, both
  floor comments read 9 and the raises read `1892 -> 1901` and `224 -> 233`, and the block's own
  `hit`, `miss` and `same` lines number 9.
  Red when: a comment still prices the block at 10, so one pinned assertion exists nowhere.
- **AC3** — When `grep -n "FLOOR_ASSERTIONS=" tools/workflows/tier2-review.test.sh` runs, it prints
  195, and the `RAISED 183 -> 195` line above it names `TOOL-aMendedFleet-67` and 12 assertions;
  and the `ck(` calls between the `TOOL-aMendedFleet-67` S5 header and the next block, with the
  refusal loop's one call counted three times, number 12.
  Red when: the pin is below 195, so the `workerType` block can be stranded behind an early exit
  with the suite still at its floor.
  figure: PINNED, 12 counted at `e83b29b6`.
- **AC4** — When `grep -n "^ASSERTION_FLOOR = " tools/runlog/selftest.py` runs, it prints 1561, and
  the last `RAISED` line in the file reads `RAISED 1554 -> 1561 by TOOL-aMendedFleet-70:` with
  `4 + 3 = 7` as the last arithmetic line of its block.
  Red when: the pin is below 1561, so `test_extract_ready` can be renamed out of the `test_`
  discovery with the total still at the floor; or the block's arithmetic misses the move, which the
  suite's own record AC2 arm reads.
- **AC5** — When `grep -n "FLOOR_ASSERTIONS=" skills/session-kickoff/manifest-check.test.sh` runs,
  it prints 216, a `+9` comment line above it names `KICK-aMendedFleet-1`, and the `run_card` and
  `check_eq` calls between the KICK-1 header and the KICK-2 header number 9.
  Red when: the pin is below 216, so the `drift —` cell's arms can be deleted with no red.
- **AC6** — When `memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-75.md` is read,
  its header reads `rev-4`, its AC1 asks a run without `--list` for a line carrying `[covers]` and
  `covers <- ` with the fixture and `AC9`, and none naming `AC1`, it no longer asks for a `HIT`
  line, and §9 carries a rev-4 line with the scope token `AC1`; and
  `grep -n "covers <- " tools/check-spec-tokens.test.sh` hits the covers arm asserting the same
  plain form.
  Red when: AC1 still asks a plain run for output only `--list` prints.
- **AC7** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs at the unit's commit, no
  check 23 finding names `KICK-aMendedFleet-1`, `KICK-aMendedFleet-2` or `KICK-aMendedFleet-4`, the
  three headers read `Tier-2`, and `python tools/memory-tree/gen_build_index.py --check` reports
  clean with the README roster's tier column reading 2 for the three; and when, in a scratch clone of
  that commit under a short `%TEMP%` path, one ledger line of KICK-2 is deleted and the gate re-runs,
  check 23 names exactly that criterion.
  Red when: a header still reads Tier-1 and the ledger join never runs, or a criterion of the three
  has no ledger line.
  cost: about 80 s per hygiene run on node a, measured 77 s on 2026-10-06.

No new refusal or gate clause is added. The floors are existing comparisons at new values, and the
staged break AC7 names is check 23's existing branch observed over the new records.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `testsuite counts (every bar self-test prints one)` · `manifest-check self-test` · `scratch-guard self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `unattended-build self-test` · `review-join self-test` · `runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `line length` · `kit epoch (shipped bytes move, the version moves)`

New arm: `tools/unattended/unattended.test.sh` · covers AC1 AC2 · the existing floor compare, red when a §4 block is deleted or stranded past an exit · `FLOOR_SHARD_1` 263, `FLOOR_SHARD_2` 1702, `FLOOR_ASSERTIONS` 1953

New arm: `tools/workflows/tier2-review.test.sh` · covers AC3 · the existing floor compare, red when the `workerType` block is stranded behind a `die()` · `FLOOR_ASSERTIONS` 195

New arm: `tools/runlog/selftest.py` · covers AC4 · the existing floor compare and the record AC2 arm, red when `test_extract_ready` leaves `test_` discovery or the raise block's arithmetic misses the move · `ASSERTION_FLOOR` 1561

New arm: `skills/session-kickoff/manifest-check.test.sh` · covers AC5 · the existing floor compare, red when the `drift —` cell's block is deleted · `FLOOR_ASSERTIONS` 216

## 8. Open questions

- **F1** — Does this unit build the floor-delta check the review proposes as the class gate for
  findings 12 to 17?
  Options: build it here; split it out; record a checklist class instead. The check diffs each
  floored suite against a base, counts the assertion calls added in each suite's own spelling, and
  reds when the floor moved by less without a recorded reason. It is gateable, so a checklist entry
  is not the left-shift §7 of the charter asks for; and it is a new refusal on the bar with its own
  base-ref and per-suite spelling questions, a second mechanism under M2, while this unit is records
  and constants. `tools/check-testsuite-counts.sh` is the seam it would extend, since it already
  reads every floored suite without running one.
  RESOLVED (main loop, 2026-10-06): split and filed — the floor-delta check is the ask
  TOOL-aMendedFleet-113, extending `tools/check-testsuite-counts.sh`. M4 batches the closing
  review's minors into this one unit, so a second mechanism is filed rather than added to the run.
- **F2** — Does this unit build the gate the review proposes for finding 21, a hygiene check that
  reds a Tier-1 spec whose commits touch two kit directories or add a CLI usage line, unless the
  spec records a tier waiver?
  Options: build it here; split it out. It reads commit history from a spec, adds a waiver grammar
  to the status header, and is a new hygiene check, a mechanism of its own.
  RESOLVED (main loop, 2026-10-06): split and filed — the Tier-1 cross-kit check is the ask
  TOOL-aMendedFleet-114, filed beside TOOL-aMendedFleet-113 for the same reason.
- **F3** — Finding 20's left-shift: the review asks for a checklist line, "an AC quoting a
  checker's output names the flags that produce it". The class
  `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md` already records "the
  command does not print that" as its first form.
  RESOLVED (agent, 2026-10-06, delegated): no new line — the existing class covers it, and
  `gotchas.py --for-diff` hands it to the next review of any spec diff.

## 9. Revision log

- rev-1 · 2026-10-06 · initial draft, from the closing diff review's findings 12, 14, 15, 16, 17,
  20 and 21, a static count of every block this build added to the four suites at `e83b29b6`, and a
  scratch-clone hygiene run with the three KICK headers flipped to Tier-2.

## 10. Reuse audit

The seams extended are each suite's own floor constant and its `RAISED` comment convention, the
COUNTED EITHER WAY SKIP convention of the unattended suite, the runlog selftest's
`parse_floor_raise` grammar, and the acceptance-ledger journal form in `memory/HYGIENE.md`, with
the build's existing ledgers such as the `TOOL-aMendedFleet-60` one as the shape.
`python tools/codebase-map/reuse_lookup.py "raise a self-test's executed assertion floor by the
arms a build added"` returned name-stem neighbours, `arm`, `run_arms` in `tools/lib/lib-selftest.sh`
and a family of `build_*` helpers, none of which prices a floor; it reported every present layer
scanned. No existing seam fits beyond the conventions above, and none is needed: the unit writes
constants and records. Recall returned `TOOL-aWokenSentinel-21` and `TOOL-aWokenSentinel-19`, units
that declared a shrink-only `FLOOR_ASSERTIONS` counted off the block; `TOOL-dUnstalledConvoy-19`, a
floor slack that hid stranded arms exactly, which is why each raise here is exact; and the
`TOOL-dDerivedDocket-49` ledger, the counted-not-run practice §4 follows. Where the review and the
tree disagree: none; every figure in findings 12 to 17 re-measured identically at `e83b29b6`.

Recall terms used: `python tools/memory-recall/query.py "how is a self-test's assertion floor raised
when arms are added, and when must a spec be graded Tier-2" --terms "FLOOR_ASSERTIONS assertion
floor RAISED executed count stranded block testsuite-counts shrink-only Tier-2 acceptance ledger
kit contract"`
