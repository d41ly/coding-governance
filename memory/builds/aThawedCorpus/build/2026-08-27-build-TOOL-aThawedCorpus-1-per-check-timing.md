# Per-check timing of the memory hygiene gate — node `a`, 2026-08-27

**Serves:** research TOOL-aThawedCorpus-1

The owner's prompt asserts that the memory tooling walks the whole corpus on every call and that this
is where the time goes. The first half is true. The second is what this record measures, because the
remedy differs completely depending on the answer, and no figure in this tree attributed the leg's
cost to anything smaller than the leg.

## Method

`tools/memory-tree/check-memory-hygiene.sh` was copied to `tools/memory-tree/_hyg_timed.sh` with a
`date +%s%N` emission inserted before every top-level `# <n> — ` check comment, and — in the second
pass — before check 23's `alcut=` line and each `if [ "$STAGED" = 0 ]` delegating block, neither of
which carries a numbered comment of its own. Nothing else was changed and the copy was deleted after.
A tick measures the span from one emission to the next in SOURCE order, which is not numeric order:
the file runs 22 before 21, and 21 before 10.

The corpus: 71 build folders, 823 tracked files under `memory/`, 1.95 MB, 310 records under
`memory/builds/*/{build,prompts,reviews}/`, roughly 250 specs.

## The first pass was contaminated, and the manifest said it would be

`memory/guides/SESSION-KICKOFF.md` front-loads the trap verbatim: several sessions share this node,
the bar has no admission control, and a latency claim taken under load must be re-run on a quiet box
before it is believed (`TOOL-aPacedTurnstile-2`). Forty to forty-one `python.exe` processes belonging
to another project's virtualenv and a second Claude session were resident throughout the first pass.

That trap was read AFTER the first measurement rather than before it, because the unattended prompt
path preflights before it hands back to `/session-kickoff`, and preflight needs a pushed build folder.
The ordering is correct for authorization and wrong for measurement; the cost was one contaminated
pass and two figures that had to be withdrawn.

**Withdrawn: the pre-commit hook at 913 s, and `--staged` at 593 s of it.** Re-measured on a quiet
box the same hook is **29 s**. `--staged` never runs checks 21 or 23 at all, so the commit path was
never carrying this defect — it was carrying contention. Any claim that the memory gate dominates
every commit is wrong and is not repeated below.

## What the quiet box measured

Zero foreign python processes at start and at end, on the pass these figures come from. Full run,
no arguments: **1398 s**, exit 1. A second complete pass with coarser ticks read 1265 s; the two
agree on the shape and the finer one is quoted throughout, because it is the one whose spans are
measured rather than inferred.

| segment | span | share |
|---|---|---|
| checks 1-9 and 22, ten checks | 32.4 s | 2.3% |
| **check 21**, record-to-spec binding | **338.9 s** | **24.2%** |
| checks 10, 11, 12 | 7.0 s | 0.5% |
| checks 13-19 and 20, the python delegates | 47.4 s | 3.4% |
| **check 23**, the acceptance ledger | **962.0 s** | **68.8%** |

Every span is a tick-to-tick measurement. Check 21's is its comment to its own
`if [ "$STAGED" = 0 ]` guard; check 23's is its `alcut=` line to process end, since it is the last
thing the script does. Neither is a remainder.

**Check 21's span is the LOOP, not the parse it contains.** `gen_build_index.py --print-bindings`
alone measures **1.416 s** and yields 301 `S` rows — 0.4% of the 338.9 s. On the contaminated pass the
same command measured 10.1 s, so this probe could have come back the other way and did not.

**Two checks are 1300.9 s of 1398 s — 93.1% — and they carry the same defect.**

## The defect, which is not the walk

Neither check is slow because it reads 823 files. Both are slow because they spawn a process per
corpus item for work that is string manipulation.

**Check 21**, `proj21`: per record, a command substitution plus a `grep -oE` for `claimed`, and a
pipeline subshell plus `tr` and `grep -qxF` for the membership test. Four to six process creations,
310 times.

**Check 23**, twice over: `for r in $(git ls-files …); do awk … "$r"; done` is one `awk` per record
across 310 of them; and the per-spec loop pays two `basename` spawns, a `cut`, a `sort -C`, a `sed`
piped to a `grep`, another `grep`, a `sed` piped to a `head`, and an `awk` piped to a `sort -u` —
roughly eleven per spec over ~250 specs, before an inner loop that runs one more `grep` per
acceptance criterion. Several thousand process creations for one verdict.

The node's own recorded tax turns that into minutes. `TOOL-aMeteredTurnstile-6` measured `bash -c
true` between 22.5 ms and 581 ms here depending on load; `TOOL-aScannedThrottle-4` records HVCI/VBS
enforcing with synchronous antimalware inspection of exactly this shape.

This is the fifth and sixth instance of one class in this repo. `TOOL-aBatchedLintel-1` collapsed it
in checks 12 and 7, porting `PERF-aSlothfulCapstan-1`; `TOOL-aCollapsedScan-1` collapsed it in
`unattended.sh --plan` on 2026-08-26. `check-method-carriers.sh` carries the shape over a
six-element population and is immaterial. A class fixed three times by hand and never gated is a
class that returns, which is what this build's ceiling unit is for.

## What the measurement rules out

**An mtime-keyed cache.** Every build directory's filesystem mtime reads the worktree's creation
time while the last commit touching it is days older — git records no mtimes, so a clone, checkout
or worktree resets all of them at once. The corpus digest `tools/memory-recall/query.py` already
computes is `st_mtime_ns` plus `st_size`, which is why its index reports `rebuilt` on the first query
in any new worktree. Keyed that way a cache does not merely miss sometimes here; it never hits.

**Keying on `CLOSED`.** Every build's last touching commit is inside seven days, because one
migration — `e6328ce4`, the mandatory roster pair — rewrote 55 build READMEs at once. Status is
authored and can be wrong; content is derived and cannot. Keying on "unchanged" covers the owner's
"fully closed" and also the idle-but-open build, and needs no new authored field.

**A cache as the FIRST purchase.** Collapsing two loops is expected to take the leg from 1398 s to
roughly 120 s with no policy change, no new state and no new failure mode. A skip mechanism bought
before that would be measured against the wrong baseline and would hide the defect rather than
remove it. The owner asked for the systemic half explicitly, so it is built — after, and priced
against what is left.

## What the collapse actually bought

Every row a controlled pair on the same corpus and the same box, stdout AND stderr identical at
every step. The live `bash` process count is reported because this node's cost IS process creation
and an unreported one is how the first round of these figures had to be withdrawn.

| step | full leg | check 23 | check 21 |
|---|---|---|---|
| as shipped | 1398-1420 s | 962.0 s | 338.9 s |
| after `TOOL-aThawedCorpus-4` | 226-360 s | **3.8 s** | 338.9 s |
| after `TOOL-aThawedCorpus-1` | **34 s** | 3.8 s | collapsed |

`TOOL-aThawedCorpus-5` is a separate axis — the pre-commit `--staged` leg, which check 23 walked in
full on every commit for want of the guard its four siblings carry: **683 s to 20 s**, 34x. The
practical reading is the commits in this build's own history: the pre-commit hook cost 913 s at the
start of this run and **23 s** on the commit that landed the last unit.

**A claim this record made, and WITHDRAWS.** It read: the leg was over a live bound, not merely
slow — `memory hygiene` declared at `ceiling: 1270`, `run-gates.sh` killing a leg that outlives its
own, `timeout -k` runnable here, so 1398 s was a breach. Every clause was true when written.

While this build ran, `TOOL-aBoundedCeiling-1` reached rev-5 and re-derived the ceiling RULE from
3x with a 60 s floor to 10x with a 300 s floor, moving `memory hygiene` from 1270 to **12720**. Its
reason is the same lesson this record learned one section above: twelve of forty legs timed out on a
real landing with nothing hung, because a ceiling sized like a COST budget reds on ambient load. A
hang bound and a cost budget are two questions, and 1270 was answering the wrong one.

So 1398 s was never a hang. The collapse is worth what its own controlled pairs say it is worth and
not a byte more, and this record does not get to borrow urgency from a number somebody else has
since corrected.

## What the fixture suite did NOT cover, stated because a green suite looked like evidence

`check-memory-hygiene.test.sh` passes 254 assertions and covers checks 3, 4, 5, 7 and 12. It carries
NOTHING for check 23 and only incidental mentions of 21, so its green says nothing about either
collapse. Both units therefore carry their own SEEDED differential, running the retired
implementation and the new one over crafted inputs that fire outcomes the live corpus never
produces — check 21 and check 23 both emit nothing on this tree, so a byte-diff over it can catch
added output and never a dropped finding. Both came back identical, including check 23's
first-wins ledger lookup, its per-record state reset, its grandfather exclusion, and its label
dedup and collation order.

## An inherited red, found while measuring

`gen_build_index.py --check` exits 1 at `f5dff6ae` with this branch's own build folder moved out of
the tree: `dCarriedReceipt`'s README and fifteen specs are stale, because `f5dff6ae` landed that
build's round-4 diff-review record without re-rendering. Hygiene check 9 therefore reds the merge bar
on `main` for every node. Repaired here by re-rendering, in its own commit, because this run cannot
reach a green bar over it.
