**Serves:** diff-review TOOL-aPooledSweep-1 TOOL-aPooledSweep-2 TOOL-aPooledSweep-3

# Tier-2 diff review — the pooled sweep mode of `run-selftests.sh`

*Node `a` · 2026-09-07 · reviewed at the integration boundary (the cumulative diff landing on `main`),
per charter §8. Adversarial fan → skeptic refutation → this synthesis.*

Reviewed range: `05fb897c2f1275b49dc1aeb56fb453505e5a9681...HEAD` · ROUND 1

## Verdict: BLOCKED

Three blockers. Two are defects in the new sweep mode that make it unusable on the population it was
written for, and one is a merge-bar leg that is red on this worktree right now, so the diff cannot
land as it stands. Nothing here is stylistic and nothing is speculative: every blocker was reproduced
against the shipped script, not inferred from reading it.

## Review shape

| | |
|---|---|
| Raw findings | 12 |
| Confirmed (survived a skeptic) | 11 |
| Refuted | 1 |
| Unverified | 0 |
| Precision | 0.92 |

**Run integrity.** Lenses 4/4 returned, 0 DIED. Skeptic batches 4/4 returned, 0 DIED. 0 contradictory
verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates. Every lens and every
skeptic batch came back, so this run is complete and a zero count in it is evidence, not a gap.

**The 11 confirmed findings resolve to 6 distinct defects.** The harness discarded no duplicates
because it merges nothing across lenses; four lenses independently reported D1 and three reported D2,
each reaching it by its own reproduction. That convergence is corroboration, and it is the reason
those two are stated with reproduced consequences rather than mechanisms. The table below is the
adjudicated set, and the blocker/high counts are counted over it.

## Severity adjudication

| # | Sev | Site | Defect | Reported by |
|---|-----|------|--------|-------------|
| D1 | BLOCKER | `tools/run-gates/run-selftests.sh:465` | `echo $$` records the runner's pid, so the wall watchdog kills the runner | 1, 4, 8, 11 |
| D2 | BLOCKER | `tools/run-gates/run-selftests.sh:566` | closed-interval peak-concurrency guard reds every honest sweep | 3, 7, 10 |
| D3 | BLOCKER | `tools/install-prefix-carried.txt:106-107` | ratchet not moved for the new literals; the `install-prefix` leg is red | 12 |
| D4 | MEDIUM | `tools/run-gates/run-selftests.sh:395` | the run wall ignores the pool's own worst case, so `OUTER=1` kills a clean run | 5 |
| D5 | MEDIUM | `tools/run-gates/run-selftests.sh:256, :396` | both advertised knobs are discarded silently when non-numeric | 9 |
| D6 | LOW | `tools/run-gates/run-selftests.sh:583` | `FP_AFTER` carries no liveness assertion, unlike `FP_BEFORE` | 6 |

**Blockers 3 · highs 0.** D1 arrived tagged `high` from three lenses and `blocker` from one, and I
promoted it. The reason is reachability plus totality: D4 shows the wall firing on a legitimate,
documented knob setting, and when it fires the runner dies at exit 143 with every verdict lost and the
suites orphaned. A safety control that does the opposite of its stated job, on a path nobody has ever
observed, is charter §7's `a gate you have only ever seen pass` in its worst form. Nothing else was
re-graded; D4, D5 and D6 keep the severities their skeptics adjudicated.

---

## D1 — BLOCKER — the wall watchdog kills the runner, not the suites

`tools/run-gates/run-selftests.sh:465`

```
echo $$ > "$d/pid"
```

`_rs_sweep_one` runs backgrounded (`_rs_sweep_one "$i" &`), and bash does **not** re-set `$$` in a
subshell — that is `$BASHPID`. Verified on this host: a backgrounded function printed `$$`=1305281,
the parent's pid, against `$BASHPID`=1305283. So every `$d/pid` file holds the runner's own pid, and
the watchdog's `kill -TERM "$wp"` at `:487` targets `run-selftests.sh`.

**Reproduced, four times independently.** A fixture whose run exceeds the wall prints the three
header lines and then `Terminated`, exit 143. Consequences, all of them on the only path the wall
exists for:

- No verdict row is rendered for any suite. The `WALL` rows at `:527-530`, the `walled` summary at
  `:556`, the peak-concurrency line, the fingerprint verdict, the withheld count and the `sweep RED`
  summary are all unreachable. The operator gets a silent death instead of a verdict.
- The suites are never signalled. They are reparented and keep running, so the run wall bounds
  nothing at all while `:444` advertises `run wall ${SWEEP_WALL}s`.
- The EXIT trap does run under the untrapped SIGTERM, so `rm -rf "$SWEEP_ROOT"` at `:409` deletes the
  scratch root out from under suites whose `TMPDIR` points inside it. One reproduction surfaced the
  resulting `.../2/v: No such file or directory`.
- `wall-breached`, `WALL_BREACHED` and the `walled` accumulator are written and never read. The
  comment at `:474` states their purpose — telling `killed by the wall` from `never wrote a verdict` —
  and that purpose can never be served.

**Fix.** Record the pid of the process that actually needs signalling. `$BASHPID` alone kills the
wrapper subshell and orphans the `timeout` grandchild, so prefer recording the `timeout` child, whose
death propagates to the suite:

```sh
TMPDIR="$d/tmp" "$SWEEP_TIMEOUT" -k 5 "$bound" bash -c "${SW_ARGV[$((k - 1))]}" > "$d/out" 2>&1 &
echo $! > "$d/pid"
wait $!; rc=$?
```

Guard the read at `:487` with a numeric check (`case $wp in ''|*[!0-9]*) continue;; esac`) so a
truncated or recycled pid file cannot signal an unrelated process.

**Left-shift gate.** An arm that stages an actual breach: a fixture population whose serialized
runtime exceeds a legal `SELFTEST_WALL` (one at or above the largest derived per-suite bound, so the
pre-flight refusal at `:400` does not fire instead), asserting exit 1, a `WALL` row and the `sweep RED`
summary in the output. The existing wall arm at `run-selftests.test.sh:212` exercises only the
pre-flight refusal, which returns 2 before a watchdog exists — the breach path has never been observed
firing at all.

## D2 — BLOCKER — the peak-concurrency guard reds a correctly bounded pool

`tools/run-gates/run-selftests.sh:566`

```awk
for (j=1; j<=NR; j++) if (s[j] <= s[i] && e[j] >= s[i]) c++
```

Closed intervals over `date +%s` stamps, which are 1-second granular (`:463`, `:469`). A pool slot
handoff — suite ends, subshell writes `v`, the parent's `wait -n` returns, the replacement stamps its
start — completes in milliseconds, so `e_prev == s_next` is the **ordinary** case. At that second the
guard counts the finished predecessor, the newcomer and every still-running sibling: `OUTER+1`. The
test at `:572` is a bare `-gt "$OUTER"` with no tolerance, so one collision reds the run.

**Reproduced repeatedly.** Three green 1s suites at `SELFTEST_OUTER_WIDTH=1` (strictly serial) printed
`peak concurrency 2 of outer 1`, `THE POOL RAN WIDER THAN ITS BOUND`, `sweep RED`, exit 1. Four green
2s suites at outer 2 printed peak 4 and RED. At outer 2 the same fixture reds on roughly two runs in
three — flaky, because the only variable is whether a ~10ms handoff straddles a second boundary.

The real population is 59 rows against an outer width of 8 on node `a`, i.e. about 51 handoffs per
sweep, so a clean reading is essentially unreachable and `sweep GREEN` — the mode's only product —
essentially cannot be produced. Worse, the RED text tells the operator the box was oversubscribed and
`every reading above is suspect`, which is the exact `an instrument that reds on innocent runs is
ignored within two sightings` failure this same file warns about at `:427`.

**Fix.** Half-open intervals, keeping the suite counted against itself:

```awk
for (j=1; j<=NR; j++) if (s[j] <= s[i] && (e[j] > s[i] || j == i)) c++
```

**Left-shift gate.** The existing arm at `run-selftests.test.sh:312` cannot catch this: its fixture
declares 2 runnable rows and `OUTER` is always >= 2 there (the fixture has no `run-gates.sh`, so the
width falls back to 2), both suites start together, no handoff ever occurs, and the arm passes on a
population smaller than the bound it tests. That is a gate that cannot fail. Replace it with one that
stages the class: a fixture of three short suites at `SELFTEST_OUTER_WIDTH=1`, asserting exit 0 and
`peak concurrency 1 of outer 1`. That arm reds today, which is the failing case §7 requires before the
guard counts as landed.

## D3 — BLOCKER — the diff cannot land: the `install-prefix` leg is red

`tools/install-prefix-carried.txt:106-107`

Confirmed by running the gate on this worktree — exit status read from the command itself, not through
a pipe:

```
ROSE  tools/run-gates/run-selftests.test.sh  5 -> 7
ROSE  tools/run-gates/run-selftests.sh       5 -> 9
REAL_EXIT=1
```

The diff adds root-install kit-path literals to both files (more `tools/run-gates/run-selftests.sh`
spellings in the header, usage and the two runtime `echo` lines at `:598` and `:610`, plus new
`tools/lib/lib-selftest.sh` references) and leaves `tools/install-prefix-carried.txt` untouched — its
rows still declare 5 and 5. The leg `install-prefix (shipped surface)` in `tools/gate-legs.json`
carries `"subject": "repo"` and **no** `guard`, so it runs on every bar including the pre-push full
run.

One correction to the incoming finding: the gate emitted two `ROSE` rows and **no** `SWAPPED` row.
`SWAPPED` is a distinct verdict for a held count with a changed kit set, and it did not fire.

**Fix.** Either derive the paths in the new strings — the two runtime `echo` lines can spell the
invocation from `$0`/`$HERE` the way the rest of the file derives `ROOT` — or, if the literals are
deliberate because this script *is* the gov-side invocation (which is exactly what the existing
fourth-column reasons on rows 106-107 already argue), hand-write the new counts with an updated reason
column. The gate's own output says `ROSE` is a BAN, so `--write-ratchet` is not the remedy here. Then
re-run `bash tools/check-install-prefix.sh` and confirm exit 0.

**Left-shift gate.** None needed — the gate exists and works; this is the gate doing its job and being
ignored. The process fix is that a branch bar was not run before the fold. Worth noting for the DoD:
this leg is unguarded, so it would have caught the omission on any full local bar.

## D4 — MEDIUM — the run wall ignores the pool's own worst case

`tools/run-gates/run-selftests.sh:395`

`SWEEP_WALL=$SWEEP_LARGEST`, and the only refusal (`:400-406`) rejects a wall *below* the largest
per-suite bound. Nothing bounds it from above against the run's own shape, which is roughly the sum of
the bounds divided by `OUTER`. The comment reasons only about the lower bound.

The arithmetic: `selftest-budgets.txt` declares `sweep-ceiling-factor: 2` and a largest budget of
13600 (`unattended gate selftest`), so the derived wall is 27200s, while the 59 rows sum to 55280s
declared and 36146s measured serially. `SELFTEST_OUTER_WIDTH` is clamped only to `>=1` and `<=W`
(`:256-262`), so `OUTER=1` is accepted silently and the run is serial — and a run in which every suite
finishes inside its own bound is still killed by the wall. Same shape at the `W=2` fallback used when
`run-gates.sh --print-profile` fails on a slow box. Today the operator gets an unexplained SIGTERM;
once D1 is fixed they get `WALL`/`sweep RED` on a clean run, with no diagnosis of why.

**Fix.** Derive the wall as the max of the largest per-suite bound and the pool's own worst case —
accumulate `SUM_BOUNDS` in the loop that already computes `SWEEP_LARGEST`, then
`SWEEP_WALL = max(SWEEP_LARGEST, (SUM_BOUNDS + OUTER - 1) / OUTER)` — and keep the existing refusal as
the floor for an explicit `SELFTEST_WALL`.

**Left-shift gate.** An arm asserting the derived wall scales with the width: the same fixture run at
`SELFTEST_OUTER_WIDTH=1` and at the resolved width must print a strictly larger `run wall` for the
narrower pool. Non-default knob, hence MEDIUM rather than higher.

## D5 — MEDIUM — both advertised knobs skip themselves silently

`tools/run-gates/run-selftests.sh:256-257` and `:396-397`

Both are `''|*[!0-9]*) : ;;` — a non-numeric value is discarded with no announcement. Verified:
`SELFTEST_OUTER_WIDTH=two SELFTEST_WALL=30m ... --sweep` printed `width 2 (outer 2, inner 1)` and
`run wall 120s`, byte-identical to passing nothing, with nothing on stdout or stderr. The digit test
also swallows `-1` and a trailing space, and `:258`'s `-ge 1` swallows `0`.

Both knobs are advertised in the mode's own usage text at `:52-55`, so an operator narrowing the pool
on a busy box gets the full resolved width instead and never learns. This is the same shape the block
two screens up (`:365-372`) refuses loudly and by name for `sweep-ceiling-factor` — *a factor nobody
wrote is not a factor* — in a file whose whole thesis is refusing what it cannot resolve. §7's *a skip
must announce itself* covers a knob that skipped itself.

**Fix.** Keep `''` as the no-override path; make any other non-numeric value print
`run-selftests: SELFTEST_WALL='<v>' is not a number of seconds` and `exit 2`.

**Left-shift gate.** Two arms, one per knob, asserting exit 2 and the offending spelling echoed back.

## D6 — LOW — the after-fingerprint has no liveness assertion

`tools/run-gates/run-selftests.sh:583`

`FP_AFTER=$(_rs_fingerprint)` is unguarded, while the before-reading at `:431` refuses when the
command fails and its comment at `:428-430` states exactly why. The file sets `set -u` only (`:24`),
never `set -e`, so there is no backstop: a failing git yields the empty string, and `:584` compares it
to `FP_BEFORE`. On the ordinary clean-tree start that prints `tree fingerprint MATCHED before and
after — no suite wrote outside its scratch`, a false green on the sweep's entire pool-safety claim,
from a probe that never ran. On a dirty tree it inverts into a false `THE SWEEP IS UNSOUND` naming no
culprit.

One correction to the incoming finding: the `tools/git-nostatus.sh` fixture it cites shims git for the
whole run, so it refuses at `:431` and never reaches `:583`. It proves the author treats a status-less
git as reachable, not that this path is reachable that way. The live route is a transient failure after
the pool drains — fork/EAGAIN or disk pressure behind a wide pool, a left-behind `index.lock`. Thin
but nonzero, and the charter's rule is that a signal without a liveness assertion is itself the defect.
LOW is right.

**Fix.**

```sh
if ! FP_AFTER=$(_rs_fingerprint); then
  st=1
  echo "run-selftests: the after fingerprint could not be TAKEN — this sweep is UNGRADED for pool safety"
elif [ "$FP_BEFORE" != "$FP_AFTER" ]; then
  ...
fi
```

**Left-shift gate.** An arm placing the existing `git-nostatus.sh` shim on `PATH` for the second
reading only, asserting the `UNGRADED` line and a non-zero status.

---

## What this diff needs before it lands

1. Fix D3 or the bar stays red and the push is blocked at the boundary. Cheapest of the three.
2. Fix D2 or `--sweep` reds on every honest run of the real population.
3. Fix D1, and only then D4, or the wall stays a control that kills the wrong process.
4. D5 and D6 are small and both are the file's own stated principles applied to itself.

Two of the three blockers share one root shape, and it is the one §7 names: **a new guard is not
landed until its failing case has been observed.** Neither the wall nor the peak-concurrency guard has
ever been seen firing — the wall's only arm tests the pre-flight refusal, and the peak arm runs a
population smaller than the bound it tests. Staging one real breach and one real handoff would have
caught both before this review existed.
