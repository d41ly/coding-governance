# The subject cache, and the three fixtures that tested nothing before it tested anything

**Serves:** journal TOOL-aQuenchedHarness-13

Node `a`, 2026-09-08. Evidence for `TOOL-aQuenchedHarness-13` §6 at rev-1.

## What this unit was, and how it was found

Not by looking for it. The push of unit 10 was refused by a red gate, and the red was not this
build's: `brief-recorded` timed out at its 900 s ceiling. Timed at origin/main's own tip, `d499258d`,
with nothing of this build merged, it costs **1760 s**. The leg is not failing — it passes, slowly,
and the runner kills it. The default branch has been un-pushable for every node since `aPooledSweep`
landed, and that landing's own bar did not catch it.

`build_commit` in `lib-unattended.sh` walks the in-range history once per graded unit and needs each
commit's subject. Its own header states the subject cache is "not an optimisation you may drop",
prices the sibling leg at 591 s cached against 3977-5401 s uncached, and records that the cache was
once ORPHANED BY A LIFT: built by its caller, read by nobody, and caught by a 6.7x regression at the
push boundary rather than by anyone reading the code. `check-brief-recorded.sh` referenced `_SUBJ`
zero times. It never had one.

The cost is therefore O(units x commits) in process spawns and grows on both axes at once, which is
why it crossed its ceiling on a LANDING rather than on an edit.

## Evidences

**Evidences:** TOOL-aQuenchedHarness-13

- AC1 — `bash tools/unattended/check-brief-recorded.sh`, timed with `date +%s%3N` — MET. 2165 s to
  **255 s** on this tree, against a 900 s ceiling. The uncached
  reading at origin/main's tip was 1760 s, so the leg was over its ceiling before this build merged
  anything. Timed at observation.
  figure: DERIVED.
- AC2 — `diff` — the leg's stdout is byte-identical to the uncached run on the same tree: 12 closed
  units graded, 101 builds skipped by the cutoff, 0 with no pinned BASE, same excluded record
  surface. The cache changes what the walk COSTS and nothing about what it decides.
- AC3 — `head -n -1` — the size assertion REFUSES a short cache. Staged into a copy of the leg beside
  a copy of the library, because the leg refuses to run without one: exit 2, and the message names
  both counts — *the subject cache holds 5 commit(s) where history has 2352*. Armed in the suite as
  `a truncated subject cache REFUSES` and `... names the shortfall`; suite green at 46 arms, exit 0.
- AC4 — `git rev-list --count` — the arm's fixture guard asserts the break had an EFFECT. This
  criterion exists because the arm failed twice before it tested anything, and neither failure was
  visible by reading it.

## The two fixtures that passed their own guard while testing nothing

Worth the space, because both are the same class and the class is this repo's oldest.

**First: a `sed` that edited the wrong thing.** `s|GIT log ... 2>/dev/null |&head -5 " | "|` used `|`
as the delimiter and `&` in the replacement, so it re-inserted the match and produced
`2>/dev/null head -5 |` — making `head` an ARGUMENT to `git log` rather than a stage after it. The
guard checked that `head -5` appeared in the file. It did. The guard passed.

**Second: a truncation that truncated nothing.** `head -5` against a fixture history SHORTER than
five lines removes nothing at all, so the cache matched history exactly, the leg exited 0, and the
arm asserted a refusal that had no reason to happen. The guard again checked that the text was
present. It was.

The repair is that the guard now asserts the EFFECT rather than the edit: it reads
`git rev-list --count HEAD` in the fixture and refuses if history is under two commits, and the
truncation is `head -n -1`, which drops exactly one line whatever the length. Off-by-one is also the
realistic way a cache reads short, so the sharper break is the more faithful one.

`memory/gotchas/` already carries this class from the other direction. What it did not carry, and
what these two add, is that **a fixture guard which checks the edit rather than the effect is itself
a fixture that tests nothing** — one level up from the arm it protects.

## What this does not answer

Whether any other caller of `build_commit` is also uncached. This unit fixed the one that was
blocking the branch; the question is a grep, not a unit, and §8 records it rather than closing it.
