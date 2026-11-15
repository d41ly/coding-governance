# TOOL-aMeasuredDrag-8 — brief-recorded's date cutoff compared in the shell, with no process per README

**Status:** SPECCED · rev-2 · 2026-11-15 · node a · Tier-1 · base aebbb4a7 · streams tooling · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief.md) | research | TOOL-aMeasuredDrag-1 TOOL-aMeasuredDrag-2 TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-4 TOOL-aMeasuredDrag-5 TOOL-aMeasuredDrag-6 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-9 TOOL-aMeasuredDrag-10 TOOL-aMeasuredDrag-11 |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-ruling-brief.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-ruling-brief.md) | research | TOOL-aMeasuredDrag-1 TOOL-aMeasuredDrag-2 TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-7 |

<!-- /gen:spec-records -->

## 1. Goal

The `brief-recorded` leg decides each build README's date cutoff with `printf | sort -C`, a pipeline
of processes per README, over every README at HEAD (finding spawns-4). This unit makes that one test
a bash string compare, which spawns nothing. Its twin in the `pass-order history` leg moves too,
as F1 resolved. Which builds are graded does not change.

## 2. Scope (IN)

- **S1** — `tools/unattended/check-brief-recorded.sh:368` tests
  `[[ "$opened" < "$BRIEF_RECORDED_CUTOFF" ]]` in place of the `printf | sort -C` pipeline, and
  skips the same builds. The comment at `:366-367` says why the compare is a date order and why it
  is in the shell. Observed by AC1, AC2 and AC3.
- **S2** — Under F1 (b), `tools/unattended/check-pass-order.sh:330` makes the same change against
  `PASS_ORDER_CUTOFF`, with its comment at `:328-329` reworded the same way. Observed by AC1, AC2
  and AC3.

## 3. Non-goals (OUT)

- The other `sort -C` cutoffs in `tools/unattended/unattended.sh`, `check-unattended.sh` and
  `lib-unattended.sh`. The review measured a per-README cost only in the two legs above (finding
  spawns-4 and the legs-2 overlap). Unlanded branches edit all three of those files.
- The `GIT show | sed | head` read of `opened:` at `:364` and `:326`, and the single
  `git cat-file --batch` read the review proposes for legs-2. That is a structural change, out of
  this build.
- RANGE-mode scoping of either leg.
- The cutoff keys, their values in `.unattended.conf`, and the shape checks at `:285-287`, `:365`,
  `:181-183` and `:327`.
- Any suite arm. The change preserves every decision, and the held suites already grade the cutoff
  in both directions (§6).
- Any page under `help/`. No page names either comparison.

## 4. Design

### Evidence

Read at `6d98c39ca`. Every file cited here has the same blob at the base `aebbb4a7`.

- `tools/unattended/check-brief-recorded.sh@626764eedaed:361-370` loops over every
  `memory/builds/*/README.md` at HEAD. It reads `opened:` (`:364`), skips a value that is not
  `NNNN-NN-NN` (`:365`), and skips a build opened before the cutoff with
  `printf '%s\n%s\n' "$BRIEF_RECORDED_CUTOFF" "$opened" | sort -C` (`:368`).
- The cutoff is refused unless it is an ISO date (`:285-287`), so both operands of `:368` are the
  same ten-character shape, with digits in the same places.
- `tools/unattended/check-pass-order.sh@023376a09f78:319-332` is the same loop with the same reads,
  the same shape check (`:327`) and the same pipeline against `PASS_ORDER_CUTOFF` (`:330`). That
  cutoff is refused unless it is an ISO date (`:181-183`).
- `sort -C` exits 0 when its input is already sorted, equal lines included. So `:368` skips exactly
  when `opened` sorts strictly before the cutoff, which is what `[[ "$opened" < "$cutoff" ]]` asks.
  Both use the locale's collation, and over two strings of one shape that is their date order.
- The repo already compares dates this way: `tools/unattended/lib-unattended.sh@a3e03db6b9f0:1809`
  and `:1812`, and `tools/unattended/check-unattended.sh@434b64be9904:2547`.
  `tools/memory-tree/check-memory-hygiene.sh@d9ce57108339:3528` notes the same `sort -C` retired
  there, inlined into awk.
- Both scripts run under `#!/usr/bin/env bash` (line 1 of each).
- Over the 212 READMEs at `6d98c39ca`, plus one opened on the cutoff itself, the two forms skip the
  same builds. Against `2026-09-06` (`.unattended.conf@dca9e08e9e22:514`) both skip 103. Against
  `2026-09-01` (`:461`) both skip 84. No README differs. All PINNED at `6d98c39ca`, by the AC1 block.
- In that run the pipeline form took 13.2 s and 12.5 s for the 213 compares, PINNED at `6d98c39ca`.
  The shell form took 24 ms for each, and ten `/usr/bin/true` took 0.55 s to 0.62 s, PINNED at
  `6d98c39ca` too.
- The live run's branch inserts 156 lines at `check-brief-recorded.sh:129` and at
  `check-pass-order.sh:57`. Neither insert touches the lines this unit edits.

### The change

In `tools/unattended/check-brief-recorded.sh`, lines 366-368 become:

```bash
  # Both values passed an ISO-date shape check, so a bash string compare is their date order and
  # spawns nothing per README (TOOL-aMeasuredDrag-8); a build opened BEFORE the cutoff is skipped.
  if [[ "$opened" < "$BRIEF_RECORDED_CUTOFF" ]]; then
```

In `tools/unattended/check-pass-order.sh`, lines 328-330 become the same three lines, with
`PASS_ORDER_CUTOFF` in place of `BRIEF_RECORDED_CUTOFF`. The `skipped_cutoff` line and the `fi`
below each stay. Each file keeps its line count, so every line number cited elsewhere stays true.

### What this does not check

- A locale whose collation orders digits out of their numeric order. `sort -C` used the same
  collation, so no build this unit grades would differ. Neither the old form nor the new one guards
  against such a locale.
- The other spawns per README, the `opened:` read and the `RUN.md` read. Those are legs-2's.

### Alternatives rejected

- A shared `date_before` function in `lib-unattended.sh`. It would wrap one bash test, and that file
  is edited on the live run's branch.
- Dropping the shape check and comparing raw. A malformed `opened:` must stay counted as skipped,
  never compared.

### Files touched (estimate)

- `tools/unattended/check-brief-recorded.sh`
- `tools/unattended/check-pass-order.sh`

## 5. Acceptance criteria

All commands run from the worktree root in Git Bash. AC1 and AC3 are the builder's, before the
commit. AC2 is read from the commit.

- **AC1** — When the block below runs with each cutoff, `bash -s 2026-09-06` and `bash -s 2026-09-01`,
  it prints `mismatches=0`, and `skipped_old` equals `skipped_new`. It also prints both timings
  beside the ten-`true` baseline, which go in the acceptance ledger as the before and after.
  Red when: the new form is written as `>` or `<=`, so the README opened on the cutoff, appended as
  the last date, prints a `MISMATCH` line.
  figure: DERIVED at observation time. The counts and timings in §4 are PINNED at `6d98c39ca`.

  ```bash
  bash -s 2026-09-06 <<'EOF'
  cut=$1; dates=(); mism=0; old=0; new=0
  for r in $(git ls-tree -r --name-only HEAD -- memory/builds | grep -E "/README\.md$"); do
    o=$(git show "HEAD:$r" | sed -n 's/^opened:[[:space:]]*//p' | head -1)
    case "$o" in [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]) dates+=("$o") ;; esac
  done
  dates+=("$cut")
  t0=$(date +%s%N); for o in "${dates[@]}"; do printf '%s\n%s\n' "$cut" "$o" | sort -C || old=$((old+1)); done
  t1=$(date +%s%N); for o in "${dates[@]}"; do [[ "$o" < "$cut" ]] && new=$((new+1)); done
  t2=$(date +%s%N)
  for o in "${dates[@]}"; do a=0; b=0; printf '%s\n%s\n' "$cut" "$o" | sort -C || a=1
    [[ "$o" < "$cut" ]] && b=1; [ $a = $b ] || { mism=$((mism+1)); echo "MISMATCH $o"; }; done
  t3=$(date +%s%N); for i in 1 2 3 4 5 6 7 8 9 10; do /usr/bin/true; done; t4=$(date +%s%N)
  echo "dates=${#dates[@]} skipped_old=$old skipped_new=$new mismatches=$mism" \
    "sortC_ms=$(( (t1-t0)/1000000 )) shell_ms=$(( (t2-t1)/1000000 )) true10_ms=$(( (t4-t3)/1000000 ))"
  EOF
  ```

- **AC2** — When `git diff --numstat HEAD~1 HEAD -- tools/unattended/check-brief-recorded.sh tools/unattended/check-pass-order.sh`
  runs on the unit's commit, it prints `3	3` for each file. When
  `grep -c "sort -C" tools/unattended/check-brief-recorded.sh tools/unattended/check-pass-order.sh`
  runs, it prints `0` for each file.
  Red when: a line is added or dropped, so later line numbers shift, or the pipeline survives in
  either file.
- **AC3** — When `bash -n tools/unattended/check-brief-recorded.sh && bash -n tools/unattended/check-pass-order.sh`
  runs, it exits 0. When `grep -n '\[\[ "\$opened" < "\$BRIEF_RECORDED_CUTOFF" \]\]' tools/unattended/check-brief-recorded.sh`
  runs, it prints line 368. The same grep against `PASS_ORDER_CUTOFF` in `check-pass-order.sh`
  prints line 330.
  Red when: the test is unbalanced, so `bash -n` names the line and exits 2, or the compare's
  operands are swapped, so the grep prints nothing.

## 6. Gates

`brief-recorded` · `pass-order history`

Both legs are unguarded, so `python tools/check-spec-tokens.py --legs-for` over the two files, run
at `6d98c39ca`, names only legs under the broad `tools/` guard. At the close each leg's summary line
prints its `build(s) skipped by the <cutoff> cutoff` count over the real tree. That count should
match AC1's `skipped_new` for the same HEAD. The held suites `unattended brief-recorded selftest`
(`tools/unattended/check-brief-recorded.test.sh@7f8bc3ca4fd1:512-520`) and
`unattended pass-order selftest` (`tools/unattended/check-pass-order.test.sh@fc3000f8fdc4:482-493`)
already grade the cutoff in both directions, so they re-observe this line at the close. No arm is
added or moved.

## 7. Open questions

- **F1 — Does the twin cutoff in `check-pass-order.sh:330` move with this one?**
  RESOLVED (agent, 2026-11-15, delegated): (b) — both per-README loops lose the same measured cost
  and no verdict moves.
  The brief offers both choices: move the sibling cutoffs the `:366-367` comment names, or state why
  this one differs.
  - (a) Only `check-brief-recorded.sh:368`. The comment at `:366-367` then says the other legs keep
    `sort -C` because the review measured the per-README cost only here. S2 and AC2's and AC3's
    `check-pass-order.sh` halves drop.
  - (b) This line and `check-pass-order.sh:330`. That line is the same per-README loop with the same
    pipeline, at the same cost, PINNED at `6d98c39ca` by AC1's block. The concurrent branches leave
    it untouched. The cutoffs in the driver, `check-unattended.sh` and `lib-unattended.sh` stay
    (§3).
  - (c) Every `sort -C` cutoff in `tools/unattended/`. It edits three files that unlanded branches
    also edit. The finding measured none of those sites.
  Recommendation: (b). It removes the same measured cost from the second leg that pays it. It edits
  one line in a region no concurrent branch touches, and no verdict moves, by AC1. Every AC above is
  written for (b).

## 8. Revision log

- rev-1 · 2026-11-15 · initial draft from the build brief
  `2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief`, item 8, grounded at `6d98c39ca`, whose cited files
  match the base `aebbb4a7`.
- rev-2 · 2026-11-15 · §1 · §7 · F1 resolved as (b) under the run's delegation
  (`2026-11-15-prompt-TOOL-aMeasuredDrag-1-ruling-brief`), so S2 and the `check-pass-order.sh`
  halves of AC1 to AC3 stand. The status moves to SPECCED, as the build's other Tier-1 specs read.

## 9. Reuse audit

The seam is the comparison line itself, edited in place. The repo's existing form for a date
compared against a cutoff is the bash string compare at `tools/unattended/lib-unattended.sh#check_landed_facts_due`
(`:1809`, `:1812`) and `tools/unattended/check-unattended.sh:2547`, and this unit adopts it. No
existing seam fits a shared helper. `python tools/codebase-map/reuse_lookup.py "compare an ISO date against a cutoff in a shell leg"`
ranked cutoff readers (`read_fold_cutoff`, `read_fork_cutoff`) and no comparer. Recall returned
TOOL-aHoistedPass-7, which chose `sort -C` because the sibling cutoffs already used it. It also
returned the findings record's spawns-4 and legs-2.

Recall terms used: `python tools/memory-recall/query.py "why do cutoff comparisons in the unattended legs use sort -C on two dates" --terms "sort -C cutoff opened ISO date compare brief-recorded pass-order grandfathering README spawn"`
