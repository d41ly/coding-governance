# TOOL-aRatifiedRulings-2 — acceptance ledger

**Serves:** journal TOOL-aRatifiedRulings-2

Every observation below was made on node `a` on 2026-09-13 over the working tree this unit commits.
The suite runs were made over FROZEN COPIES of `tools/unattended/` under a short root in the user
temp directory (the scratchpad path length is a recorded trap on this node), one copy per run, so
seven runs could go concurrently and no edit to the worktree existed to revert afterwards; spec
rev-4 logs that substitution for the in-place `sed` / `git checkout` the criteria spell. Each copy
differs from the landed kit by the ONE delta named beside it. The output files are not committed;
the figures below are what they hold, and a reader re-deriving them re-runs the named copy.

| Run | Copy | Delta from the landed kit | Invocation |
|---|---|---|---|
| R0 | `base` | suite AND checker at base, no arm; `FLOOR_SHARD_2=99999` | `--shard 2/2` |
| R1 | `arm_base` | checker at base (`git show HEAD:tools/unattended/check-unattended.sh`), suite landed | `--shard 2/2` |
| R2 | `tip` | none | `--shard 2/2` |
| R3 | `tip99` | `FLOOR_SHARD_2=99999` | `--shard 2/2` |
| R4 | `brkC` | `dsrun=$(GIT show "$dshit:$f" 2>/dev/null \|\| true)` → `dsrun=$(cat "$f" 2>/dev/null \|\| true)` | `--shard 2/2` |
| R5 | `brkD` | the exact `case "$dsbrief" in *"$dsnl$dsq$dsnl"*)` → `dsx=0; for dsrow in $dsbrief; do covers "$dsrow" "$dsq" && { dsx=1; break; }; done` and `case "$dsx" in 1)` | `--shard 2/2` |
| R6 | `tip` | none | unsharded |

Every run is `bash <copy>/check-unattended.test.sh [--shard 2/2] > <file> 2>&1`, and every figure
is read from the file with `grep`, never through `&&` or `tail`. All seven exit 1, before and after,
for the causes `TOOL-aHoistedPass-38` records and the spec's section 4 names; the exit status is not
an observation here and the ledger reads FAIL lines.

**Evidences:** TOOL-aRatifiedRulings-2
- AC1 — `bash tools/unattended/check-unattended.test.sh --shard 2/2` — R1, the arm against the checker at base, holds `FAIL unexpected: unattended: check 23 —` and `FAIL missing: check 23 excluded memory/builds/tRun/prompts/2026-08-21-prompt-ARCH-tRun-1-1-build-brief.md for ARCH-tRun-1 in memory/builds/tRun/RUN.md`; R2, the landed kit, holds neither. Whole-file `^FAIL` counts are @@R1FAIL@@ and @@R2FAIL@@, and the sorted set difference R1 minus R2 is exactly the five arm lines quoted under AC1, AC2 and AC5 — the residual @@R2FAIL@@ lines are identical on both sides and are the pre-existing population. The `hit` on the report line is the positive artifact that the exclusion branch ran on that path. Before the full runs, a harness of the suite's prologue plus only the new arm printed exactly those five lines with `n=7 st=1` against the base checker and nothing with `n=7 st=0` against the landed one, 11 m 44 s and 5 m 54 s, which is how the arm's line set was known before three hours were spent on it. Wall clocks: R1 @@R1WALL@@ s, R2 @@R2WALL@@ s, concurrent with the other five and with three sibling sessions' work on the box
- AC2 — `build-brief.md` — R1 holds `FAIL missing: wrote work/stray.txt in memory/builds/tRun/RUN.md` and `FAIL unexpected: build-brief.md`, because the base line reads the brief first and the stray second in `diff-tree` order; R2 holds neither, so at the landed tip the `wrote` list names the stray file alone and the brief appears nowhere in the output
- AC3 — `cat "$f"` — R4, the landed checker with the exclusion set read from the working-tree run-state file instead of `GIT show "$dshit:$f"`, holds `FAIL missing: wrote memory/builds/tRun/prompts/2026-08-21-prompt-ARCH-tRun-1-1-build-brief.md`, and its sorted FAIL set minus R2's is exactly that one line, so the break redded C and nothing else in the shard. C printed no FAIL line in R1 or R2: the base checker already reports the post-hoc brief, which is what makes C a control and the break its only red. The copy was discarded rather than checked out; no worktree byte moved
- AC4 — `covers "$row" "$dsq"` — R5, the landed checker with the exact `case` membership replaced by a `covers` walk over the rows, holds `FAIL missing: memory/builds/tRun/prompts/other.md`, and its sorted FAIL set minus R2's is exactly that one line: the directory row covered both files, the `wrote` list emptied, and A, B, C and E stayed silent — E because `covers` normalises both sides. D printed no FAIL line in R1 or R2. Discarded copy, as for AC3
- AC5 — `./` — R1 holds the line `FAIL unexpected: unattended: check 23 —` exactly twice, A's and E's, where R0 — the base suite with no arm — holds it 0 times and R2 holds it 0 times; so the dot-spelled row excluded nothing against the base checker and excludes the brief once `normpath` is applied
- AC6 — `FAIL executed` — neither R2 (shard 2/2, `FLOOR_SHARD_2=316`) nor R6 (unsharded, `FLOOR_ASSERTIONS=399`) prints a `FAIL executed` line. R3 prints `FAIL executed @@R3N@@ assertions in shard 2/2 against a floor of 99999` and R0 prints `FAIL executed 377 assertions in shard 2/2 against a floor of 99999`, so the arm executed @@DELTA@@ assertions, which is its `hit` and `miss` call count: A 2, B 2, C 1, D 1, E 1. `FLOOR_SHARD_2` 309 → 316 and `FLOOR_ASSERTIONS` 392 → 399 at `check-unattended.test.sh`, `FLOOR_SHARD_1=83` untouched; the measurement line above the floors records the raise. R0 wall 7071 s over 24 FAIL lines, the pre-existing population; R6 wall @@R6WALL@@ s over @@R6FAIL@@ FAIL lines
- AC7 — `bash tools/unattended/check-unattended.sh` — run twice over this worktree at the staged tree, once with the checker at base from the `base` copy (2067 s, exit 0, 39 lines) and once with the landed checker (2037 s, exit 0, 34 lines), both under the seven concurrent suite runs, against the 220 s the spec records idle. Outside check 23 the two outputs are byte-identical. Base: 30 check-23 lines, 29 of the `committed a path outside` class and 1 `moved inside its window`. The derivation loop below, run over the base output, finds 28 brief paths whose unit's row is in the pass commit's tree and 1 whose is not, plus 154 other paths that must still print, and reports 0 violations against the tip output. Tip: 25 check-23 lines, 24 of the class and the same window line; 5 lines left because the brief was their only path — `DEPL-dRetiredFork-8` at `e8dd66dc`, `TOOL-dRetiredFork-1` at `3fca9b7b`, `-2` at `5a713a55`, `-5` at `137aff98` and `-9` at `68310b27` — 23 keep printing without the brief, and exactly 1 tip line names a `-build-brief.md`: `TOOL-dRetiredFork-6` at `ffdaa82b`, whose row reached the tree in the run-state commit after its pass commit, the residual section 4 derives. The corpus now also holds `aClosedDocket`, `aRatifiedRulings` and `aUnblockedFleet` in phase BUILDING, none of which contributes a line of the class

## The AC7 derivation loop

Run from the repo root with the two leg outputs as arguments. It reads the base output only to
find the population and the expectation, and the tip output only to check it.

```bash
base=$1; tip=$2
leave=0; stay=0; other=0; bad=0; lines=0
grep -F 'unattended: check 23 — a dispatched pass committed a path outside' "$base" > "$base.c23" || true
while IFS= read -r line; do
  [ -n "$line" ] || continue
  lines=$((lines+1))
  tail=${line#*declared before dispatch: }
  unit=${tail%% at *}; rest=${tail#* at }
  sha=${rest%% wrote *}; rest=${rest#* wrote }
  paths=${rest% in *}; file=${rest##* in }
  rows=$(git show "$sha:$file" 2>/dev/null | grep -F -- " brief · item $unit · reason " || true)
  bpath=""
  while IFS= read -r r; do [ -n "$r" ] || continue; r=${r#* · reason }; bpath="$bpath ${r#* }"; done <<ROWS
$rows
ROWS
  tline=$(grep -F "declared before dispatch: $unit at $sha wrote" "$tip" || true)
  ttail=""; [ -n "$tline" ] && { ttail=${tline#* wrote }; ttail=${ttail% in *}; }
  for p in $paths; do
    case "$p" in *-build-brief.md) ;; *)
      other=$((other+1))
      case " $ttail " in *" $p "*) ;; *) echo "BAD other path went silent: $unit $p"; bad=$((bad+1)) ;; esac
      continue ;;
    esac
    case " $bpath " in
      *" $p "*) leave=$((leave+1)); case " $ttail " in *" $p "*) echo "BAD expected to leave, survived: $unit $sha $p"; bad=$((bad+1)) ;; esac ;;
      *)        stay=$((stay+1));  case " $ttail " in *" $p "*) ;; *) echo "BAD expected to stay, left: $unit $sha $p"; bad=$((bad+1)) ;; esac ;;
    esac
  done
done < "$base.c23"
printf 'base lines of the class: %s · brief paths expected to LEAVE: %s · to STAY: %s · other paths that must still print: %s · violations: %s\n' "$lines" "$leave" "$stay" "$other" "$bad"
```

Its output on 2026-09-13: `base lines of the class: 29 · brief paths expected to LEAVE: 28 · to
STAY: 1 · other paths that must still print: 154 · violations: 0`.

## What was not observed, and why

- `git checkout -- tools/unattended/check-unattended.sh` after each break, and `sed` on the floor in
  place: replaced by a copy per run, as the header says. The observation each criterion asks for —
  the FAIL-line delta under the named one-line break — is the same observation; the mechanics of
  unstaging it differ and are logged in the spec's rev-4 line.
- A `PASS (<n> assertions)` line, on any run: the suite cannot print one on this tree, per
  `TOOL-aHoistedPass-38`, and section 6's preamble says the exit status is not the observation.
- The section 5 perf line's `git show` count on the live corpus: the 30 s difference between the two
  AC7 runs is inside the noise of seven concurrent suites and is not a measurement of the spawn.
