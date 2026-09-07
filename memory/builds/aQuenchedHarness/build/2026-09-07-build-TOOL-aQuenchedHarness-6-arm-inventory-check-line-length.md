# check-line-length.test.sh — the port, its arm inventory, and its readings

**Serves:** journal TOOL-aQuenchedHarness-6

Node `a`, 2026-09-07. The first suite ported onto `tools/lib/lib-selftest.sh`. Spec §S4/S5 require
the arm inventory to be extracted before and after and DIFFED, because a port that drops an arm is
faster and greener at once — a regression wearing a speed-up's clothes. §S7 requires seconds, spawns
and arm count on both sides. All of it is below.

## The inventory diff — AC1

`bash tools/lib/extract-arms.sh` on each side. The before-inventory was taken at `c63e4177`, from the
suite as it stood; the after-inventory from the ported suite at width 8.

```
before: 18 arm(s)     after: 18 arm(s)     diff: empty
```

Both sides sort to the same 18 labels:

```
a POSITIONAL beats the declaration
a declaration selecting NO subject is cannot-run
a long line INSIDE a fence does not red
a long line inside a TABLE does red
a non-ASCII line is measured in CHARACTERS, not bytes
a non-numeric LINE_MAX is a named failure, not a certified zero
a non-numeric POSITIONAL limit is a named failure, not a certified zero
a row naming an ABSENT path reds as stale
a scanner that dies mid-run is a named failure, not a certified zero
a subject with NO gradeable line is a dead probe, not a clean verdict
an ABSENT declaration is NOT ADOPTED at exit 0, not a red install day
an over-length line reds naming the line and its length
an undeclared subject with no environment falls through to 450
an UNDECLARED subject honours the environment
a NON-NUMERIC limit is a named failure, not a shell error
control · a short subject passes
exactly at the limit passes
the DECLARATION beats the environment
```

## The guard's own failing case — AC2, AC6

A gate nobody has seen fail is an assertion about nothing, so the arm `exactly at the limit passes`
was deleted from a scratch copy and both layers were observed:

- **With the suite's own `SELFTEST_FLOOR=18` intact**, the harness refuses before running an arm, the
  suite prints no per-arm line at all, and `extract-arms` reports `UNEXTRACTABLE` at exit 3 rather
  than handing back an empty inventory that would compare equal to another empty one. That is AC6's
  named state arriving on a real suite rather than on a fixture.
- **With the floor lowered to 17** so the suite runs, the diff is non-empty and names the missing
  arm — `17d16 < exactly at the limit passes` — at exit 1. The port would be refused.

## The readings — AC3, S7

| | before | after, width 1 | after, width 2 | after, width 4 | after, width 8 |
|---|---|---|---|---|---|
| wall | 31.9 s | 23.2 s | 13.6 s | 9.6 s | **7.9 s** |
| factor | — | 1.37x | 2.35x | 3.33x | **4.03x** |
| traced spawns | 74 | — | — | — | **42** |
| arms | 18 | 18 | 18 | 18 | 18 |

**Before** is the median of three consecutive runs — 31.3 / 33.3 / 31.9 s — on node `a`, 2026-09-07,
with nothing else running. **Traced spawns** are `bash -x` lines whose first token is an external
binary, the same expression on both sides; `bash -x` does not follow a child script, so the subject's
own internal spawns are invisible to it in both columns and the figure is comparative, not absolute.

**The condition the declared factor grades is width 8**, which is what `run-selftests.sh` exports on
this node, and the header of `tools/run-gates/selftest-budgets.txt` says so where it declares the
3.0x minimum. That pairing needs its caveat stated rather than buried: **the before-suite had no
width**. It kept ONE scratch repo and mutated it with a `reset` before every arm, so two of its arms
run concurrently only by corrupting each other, and there is no honest "before at width 8" to put in
that column. The comparable pair is the suite as it could actually be run, on either side of the
port, on the same box within the same hour. Both serial columns are printed above so a reader can
apply whichever comparison they think is fair; at width 1 the port clears 1.37x and would NOT clear
the declared factor.

## Where the time went, and where it did not

The spawn column is the part worth keeping. Of the 74 traced spawns before, **31 were `python3`, and
every one of them built a line of repeated characters** — 18 of those inside the `reset` that ran
before each arm. At the 773 ms a python spawn costs on this fleet that is ~24 s of a 31.9 s suite,
spent on strings a shell builds in a builtin. `build_line` in the ported suite is those 31
spawns, and it is named for the lexicon's declared `build` rather than for brevity:

```sh
build_line() { local pad; printf -v pad "%${2}s" ""; printf '%s\n' "${pad// /$1}"; }
```

The remaining 42 spawns are 19 `cp -a`, 18 `timeout`, 3 `git`, and one each of `rm` and `chmod` —
which is to say, three per arm plus the fixture, and nothing else. The subject itself measures
1.12 s per invocation, so **18 x 1.12 = 20 s is this suite's irreducible serial floor**; the width-1
column is that floor plus 3 s of harness. Everything below 20 s is bought by the pool, and the pool
is bought by the per-arm snapshot copy, which costs 136 ms against the 626 ms a `git init` costs.

## Two defects the port surfaced, both fixed here

Neither was visible until a real suite ran on the harness, and both are recorded because the numbers
above are wrong without them.

- **The harness was the cost.** Its first draft wrote five files per arm and read them back with
  `cat`, read the capture with another `cat`, and tested it with `grep` — eleven processes of
  bookkeeping around a subject that costs one. The first port measured **62 s against the 32 s of the
  suite it replaced**. The declarations moved into arrays the arm subshell inherits, the capture is
  read with `read -d ''`, the substring test is a `case`, and setup and subject share one `bash -c`
  under one `timeout`. Three processes per arm.
- **`wait -n || wait` is not a fallback, it is a barrier.** `wait -n` returns the exit status of the
  job that finished, so a red arm was read as "this shell has no `wait -n`" and the pool waited for
  every outstanding job. Measured before the fix: 62 s at width 1 and 46 s at width 2, where width 2
  should have been half of width 1. The capability is now probed once at source time.

A third defect was found in a sibling and fixed in `tools/run-gates/run-selftests.sh`: its composite
bound divided the declared width by an outer pool of 4 that does not exist, because its run loop is
serial on purpose. Every ported suite was being handed a quarter of the width it was entitled to —
13.6 s against 7.9 s, on this suite.

## What this does NOT claim

- Nothing here says the suite is *correct*, only that it grades the same 18 things it used to. The
  gate under it is untouched, per spec §3.
- The `bash -x` spawn counts do not see inside the subject. The subject's own python calls are
  unchanged and are present in both columns.
- One reading per column, except `before`, which is a median of three. A busy box moves these; this
  repo has measured the same leg varying 5.5x median under contention.
