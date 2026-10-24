# TOOL-dSafePassage-28 — every refusal of the prepared landing after the walk leaves a clean tree, gated as a class

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 5 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-28-deviation-74.md](../build/2026-10-23-build-TOOL-dSafePassage-28-deviation-74.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-23-review-TOOL-dSafePassage-27-28-29-30-31-32-33-34-35-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-27-28-29-30-31-32-33-34-35-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-32 TOOL-dSafePassage-27 TOOL-dSafePassage-33 TOOL-dSafePassage-31 TOOL-dSafePassage-34 TOOL-dSafePassage-35 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 15 to 26
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md`)
confirmed finding **id 35** at HIGH, merged with id 1 into its item **D-1**. Its skeptic traced the
leak to the regeneration refusal, which `TOOL-dSafePassage-27` closes, and argued that the later
refusals of `cmd_prepare` are safe because they run on files `git add -A` already staged or committed.
No arm observes that argument, and the report's left-shift asks for one: a fixture that iterates
every refusing stage after `run_gov_first`, with the walk passing, and asserts a clean
`git status --porcelain` after each. This unit is id 35's promotion: that arm, gating the class, so
a refusal branch added to `cmd_prepare` later either joins it or reds it.

## 2. Scope (IN)

- **S1** — The population, derived. The arm reads `cmd_prepare` in `tools/push-main.sh`, from the
  line calling `run_gov_first` to the function's end, and counts its refusal branches, each a
  `return 1` line. It holds a table of one row per branch, in source order, and reds when the derived
  count and the table's row count differ, naming both. The count at the base, after
  TOOL-dSafePassage-25 and `TOOL-dSafePassage-27` land, is derived by the build and never typed here.
  Observed by AC1.
- **S2** — One case per row. Each row names how the fixture plants that refusal with the walk
  passing, or carries `unplantable:` and its reason. The plantable rows at writing are the gov-first
  refusal itself (TOOL-dSafePassage-25's planted failing witness, the one row whose walk does not
  pass), the regeneration refusal (a committed `regen.py` exiting 1, as arm 30 plants one,
  `tools/push-main.test.sh:993-1009`), the merge-loss refusal (a branch whose merge loses a
  definition, as the suite's merge-loss arms plant one) and the compare-and-swap refusal (the branch
  moved by a second commit between the plant's `run_regen` and the swap, made by the planted
  `regen.py` itself). Observed by AC2.
- **S3** — The assertion. After each planted refusal, the fixture asserts exit 1, the branch at its
  old sha and checked out, `git status --porcelain` printing nothing, and no path under
  `.governance/steps` or `.governance/outbox` left in the working tree. Observed by AC2 and AC3.
- **S4** — The unplantable rows. A row marked `unplantable:` is printed by the arm on every run as a
  `skip` line naming the branch and its reason, so a skipped case is never read as coverage. Two
  rows are expected there: the commit-tree refusal (`git commit-tree` or `git update-ref` failing at
  `tools/push-main.sh:921-925`) and the final checkout failure (`:943-945`), which no fixture makes
  fail without a lander switch, and this unit ships none. Observed by AC4.

## 3. Non-goals (OUT)

- The regeneration refusal's own fix: `TOOL-dSafePassage-27`.
- A lander switch that makes `git commit-tree` fail on demand. The skip line names the gap instead.
- The attended landing, whose gov-first walk is its own commit (TOOL-dSafePassage-8 S4); its
  behavioural arm is finding 18, carried by the minors batch.

### Edges

- **consumes-from** `TOOL-dSafePassage-27` — the one snapshot the prepared path cleans against; without it the regeneration row of this arm is red over the shipped lander
- **hands-off** `TOOL-dSafePassage-42` — findings 1, 10 and 31 of the spec audit of units 27 to 35, the compare-and-swap row's `moved` branch in `PREPARE_REFUSALS`' `expect` column; findings 18 and 32, the derived count read through `scan_shell_lines` and anchored on the `if ! run_gov_first` call; and finding 26, the pricing of the added landings

## 4. Design

### The arm

```
for each row of PREPARE_REFUSALS (stage, plant, expect):
  build TOOL-dSafePassage-8's --prepare fixture, the walk passing unless the row plants its refusal
  apply the row's plant, commit it on the branch; an unplantable row prints its skip line instead
  run push-main.sh --prepare --slug fx; assert rc 1, branch unmoved and checked out
  assert `git status --porcelain` empty and no .governance/steps or outbox path present
derived = count of `return 1` lines in cmd_prepare after the run_gov_first call
assert derived == rows of PREPARE_REFUSALS
```

The table lives in `tools/push-main.test.sh` beside the arm, one row per branch in source order, so
a reader comparing the two sees which row answers which branch.

### Inventory

Minted in `tools/push-main.test.sh`: the table `PREPARE_REFUSALS` and the arm's case labels. No
function in a shipped file, no conf key, gate leg or policy key.

### Migration

None.

### Rollout

Live at landing as a self-test arm. It builds at order 5 with `TOOL-dSafePassage-27`, after it within
the order, because both write `tools/push-main.test.sh` and this arm's regeneration row needs that
unit's fix.

### Files touched (estimate)

- `tools/push-main.test.sh`

### Alternatives rejected

- **One case per refusal, typed with no derived count.** A refusal added to `cmd_prepare` later would
  join no case and the arm would stay green over it, the instance-gating the charter's class rule
  forbids.
- **A lander switch to fail `commit-tree`.** It ships a knob into the lander for one arm; the skip line
  states the gap at no cost.

## 5. Production-readiness checklist

- security: N/A — a self-test arm; it writes only its scratch fixtures under `%TEMP%`.
- perf / scale: one fixture landing per plantable row, four at writing, each the cost of the suite's existing
  `--prepare` arms.
- error / empty / loading states: a derived count of zero reds the arm, so an anchor that matches
  nothing is never read as an empty class.
- observability: each case prints its stage; each unplantable row prints its skip line.
- risks: the derived count reads `return 1` lines by shape; a refusal spelled another way is not
  counted, which the arm's comment states.
- testing: this unit is the arm.
- migration: none.
- user docs: N/A — a self-test arm.

## 6. Acceptance criteria

- **AC1** — When `awk '/^cmd_prepare\(\)/,/^}/' tools/push-main.sh | sed -n '/run_gov_first/,$p' | grep -c 'return 1'`
  runs after the pass, it prints the count the arm's table carries rows for, and
  `git grep -n "PREPARE_REFUSALS" -- tools/push-main.test.sh` shows that table.
  Red when: a refusal branch of `cmd_prepare` after the walk has no row.
  figure: the count is DERIVED by this command at the pass.
- **AC2** — When the arm's gov-first, regeneration, merge-loss and compare-and-swap cases run the fixture
  landing `bash tools/push-main.sh --prepare --slug fx`, the walk passing in all but the first, each
  exits 1 with the
  branch unmoved, and `git status --porcelain` in the fixture prints nothing after each.
  Red when: any refusal after the walk leaves an untracked file the walk or a later stage made.
  fixture: scratch clones under `%TEMP%`, built as `build_regen_fixture` builds one
  (`tools/push-main.test.sh:934`), with TOOL-dSafePassage-8's step plant.
- **AC3** — When `git -C <fixture> ls-files --others --exclude-standard -- .governance` runs after
  each planted refusal, it prints nothing.
  Red when: a before-image, an order or a receipt the walk made survives a refusal.
- **AC4** — When the arm runs, its output carries one `skip` line per `unplantable:` row, naming the
  commit-tree refusal and the final checkout failure, each with its reason.
  Red when: an unplantable branch is counted as covered with no line saying so.

## 7. Gates

`push-main self-test` · `spec tokens (a spec's own names resolve)`

New arm: tools/push-main.test.sh · covers AC1 AC2 AC3 AC4 · one fixture landing per plantable refusal of `cmd_prepare` after the walk, plus the derived-count check, its failing case staged by a lander copy carrying one extra refusal branch with no row, and by one whose regeneration refusal cleans against a snapshot taken after the walk · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the round-1 spec audit of units 15 to 26's
  id 35 (HIGH, item D-1, shared with id 1).
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the spec audit of units 27 to 35, written by the disposal stage: `TOOL-dSafePassage-42`; no other section moved.

## 10. Reuse audit

The seam extended is `tools/push-main.test.sh`'s regeneration arms (`build_regen_fixture`, `:934`,
and arm 30, `:993-1009`), whose plant this arm reuses as its first row, and its merge-loss arms.
`python tools/codebase-map/reuse_lookup.py "clean the untracked files a refused lander stage made
after an earlier stage passed"` ranked `CensusRefused`, `ScopeRefused` and `corpus_files`, name-token
matches, so no existing seam fits beyond the suite's own fixtures.

Recall terms used: `python tools/memory-recall/query.py "how were spec audit findings promoted into repair units placed beside the unit they repair" --terms "spec audit promoted unit repair blocker high minors batch disposal order edges rescope"`
