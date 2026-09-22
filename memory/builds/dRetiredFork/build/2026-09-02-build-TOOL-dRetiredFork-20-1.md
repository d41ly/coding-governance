# Build — TOOL-dRetiredFork-20, the spec lint

**Serves:** journal TOOL-dRetiredFork-20

Built on node `d` under session slug `dRetiredFork`. `tools/check-spec-tokens.py` plus its twelve-arm
suite, wired as two legs, with a shrink-only waiver registry.

## What the pre-wiring run actually did

`AGENTS.md` §7 says to run a candidate predicate over the real tree and print hits AND near-misses
before wiring it. That is not ceremony here — it took **four passes** and each one caught the
predicate redding innocent files:

| pass | hits | what the near-misses showed |
|---|---|---|
| 1 | many | grading FROZEN closed specs, whose records this repo never rewrites |
| 2 | 304 | globs and `path:line` tokens graded by the path join |
| 3 | 38 | §7 prose graded as leg names — 271 of 304 hits came from ONE spec's prose |
| 4 | 31 | `~/…`, `$HOME/…` and quoted shell words graded as repo paths |

The final population is 48 live specs, 405 terminal specs deliberately not graded, 759 tokens
graded, and 275 citations skipped because their path is untracked — a figure the run PRINTS, because
half the corpus cites kit files by basename and a silent skip there would be a could-not-fail arm
over half the subject.

## What it found that the reviews found by hand

The one unwaived hit in this build was `TOOL-dRetiredFork-14` AC3's `.claude/hooks/agent-cap.test.sh`
— round 3's blocker 4, found independently by a join rather than by a reviewer. That is the whole
argument for the unit. Of the remaining 31 hits, none is in dRetiredFork: 22 distinct tokens across
four other builds' live specs, each waived with a reason naming whose they are. Two are real stale
paths (`tools/run-gates.sh`, which moved under `tools/run-gates/`) and are recorded as that build's.

## Two refusals on landing, both correct

`govkit selfcheck` red until both new legs had a row in `tools/govkit/subject-pins.tsv`, and
`check-testsuite-counts` red until the suite pinned `FLOOR_ASSERTIONS` and COMPARED it to its printed
count. Neither was anticipated by rev-1; S8 anticipated the first class and the second is its
sibling. Both are the house pattern working: a new moving part reds until a declaration claims it.

## Not done, and said plainly

The leg join grades only §7 lines that ARE the list. A §7 line carrying prose is not graded, which is
stated in the program header rather than implied — the alternative was 271 hits from one spec's
prose. The citation join resolves existence and range and never reads the cited line, so a citation
naming a real line that argues the opposite passes.

**Evidences:** TOOL-dRetiredFork-20
- AC1 — `python tools/check-spec-tokens.py` — staged `TOOL-dRetiredFork-14` AC3's original untracked path, observed exit 1 naming file, kind and token; restored, exit 0
- AC2 — `bash tools/check-spec-tokens.test.sh` — arm 3, a §7 name absent from the manifest reds
- AC3 — `bash tools/check-spec-tokens.test.sh` — arm 4, a citation past end of file reds
- AC4 — `bash tools/check-spec-tokens.test.sh` — arm 6, a waived hit with a reason passes and the count prints
- AC5 — `bash tools/check-spec-tokens.test.sh` — arms 7 and 8, a stale waiver and a reasonless one both red
- AC6 — `bash tools/check-spec-tokens.test.sh` — arms 9 and 11, an empty spec population and an absent registry both REFUSE
- AC7 — `memory/builds/dRetiredFork/build/2026-09-02-build-TOOL-dRetiredFork-20-1.md` — the four-pass run is recorded above with its hits and near-misses; both S1 clauses landed, AC3 corrected and the rev-2 log line no longer overstates the fold
- AC7b — `python tools/check-spec-tokens.py` — the run reports `275 citation(s) skipped (untracked path)` on every invocation
- AC7c — `python tools/govkit/govkit.py selfcheck` — exits 0 with both files declared as registry exemptions and both legs pinned
- AC8 — `bash tools/check-testsuite-counts.sh` — exits 0; the leg declares a ceiling and the suite pins a floor of 12
