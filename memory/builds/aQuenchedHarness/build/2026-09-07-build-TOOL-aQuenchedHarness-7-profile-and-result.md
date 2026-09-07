# The longest leg on the bar, profiled and cut — and the target it still misses

**Serves:** journal TOOL-aQuenchedHarness-7

Node `a`, 2026-09-07. `unattended kit gate` — `bash tools/unattended/check-unattended.sh` — profiled,
changed, and measured on a frozen clone. The spec declared its targets from the BEFORE profile and
before any after-reading existed, which is why one of them can be, and is, reported as missed.

## What the profile said, and how it refuted the hypothesis

`memory/builds/aQuenchedHarness/build/2026-09-07-build-TOOL-aQuenchedHarness-7-cost-hypothesis.md`
was written first and predicted the cost was the per-record `git log --follow` walk in the two loops
over `RUN*.md`. It named what would refute it. This is that:

```
git log --follow --diff-filter=A   31 calls        the predicted term
git log -1 --format=%s <sha>     1528 calls        61% of every git spawn in the run
```

`pass_commit()` walks its window with `git log --reverse --format=%H`, then spends **one more git
spawn per commit** to read that commit's SUBJECT — and it is called once per (anchor, unit) pair, so
the same commits are re-read once per pair. That is the pass-order defect verbatim, the one
`274aa39b` already fixed elsewhere in this repo, sitting in a second file.

## The three changes

All three are semantics-preserving and the proof is below, not the argument.

1. **`pass_commit` takes the subject out of the walk it already does.** `%H%x09%s` instead of `%H`,
   read line-wise into two fields, and the inner `git log -1` is gone. A heredoc rather than a pipe,
   because the loop `return`s from the function and a piped `while` runs in a subshell.
2. **A loop-invariant hoist in `check-unattended.sh`.** `$dshit` does not change inside the sibling
   loop, so reading its subject once per SIBLING was a git spawn per sibling to answer one question.
3. **`id_in` in native bash.** This one came from measuring the FIRST fix rather than from reading:
   after the git spawn left that loop, the same loop still ran `id_in` per commit, and `id_in` forked
   a subshell and spawned a `grep` — 1528 of them, in the exact place the git spawn had been.

## The result

| | before | after |
|---|---|---|
| external processes, traced | **5420** | **2321** |
| git spawns | 2517 | 1022 |
| `git log -1` | 1528 | 33 |
| `grep` | 2235 | 631 |
| stdout + exit status | 46 lines, rc 1 | **byte-identical, 46 lines, rc 1** |

**57% of every external process the leg starts, removed.** That figure is contention-independent and
is the one to trust.

The seconds are messier, and the mess is stated rather than resolved by picking the flattering pair:

```
controlled A/B, both arms in ONE window   1067.1 s -> 439.9 s   2.43x
quiet standalone, hours apart              625.2 s -> 435.4 s   1.44x
```

The within-window pair is the methodologically sound one — same box, same minute, same remote — but
its BEFORE arm ran while the box was loaded, which is why it is nearly double the quiet BEFORE taken
earlier the same day. The quiet pair is the honest floor. **The truth is between 1.44x and 2.43x**,
and this repo has measured the same leg varying 5.5x median under contention, so a single number here
would be a choice rather than a measurement.

## The targets, and the one that is missed

Declared in the spec's §2 S3 from the before-profile, before any after-reading existed:

- **spawns ≤ 22 per `RUN*.md` record** — **MET.** 1022 git spawns over 49 records = **20.9**, against
  51.3 before. (All external processes: 47.4 per record, against 110.6.)
- **wall ≤ 400 s**, quiet standalone — **MISSED, at 435 s.** By 9%.
- **`BUDGET_kit_gate` lower than 240** — **NOT MET, and it is not meetable.** That budget records
  *"measured 187 s IDLE on node `a` 2026-08-26"*. Between that date and this one the population it
  walks went from **25 `RUN*.md` records to 49** and from **71 builds to 102** — records ×1.96, and
  the leg's cost ×3.34 over the same span. It grows FASTER than the repo does, because both the
  number of (anchor, unit) pairs and the window each one walks grow together. A budget set against a
  tree half this size cannot be met by making the leg faster; it can only be met by lying about it.
  The row is re-declared at the measured figure with this reading beside it.

**Declaring the target before the reading is what made the miss visible**, and it is the second time
in this build that the practice paid: the first attempt at this unit "met" its target by counting only
GIT spawns, which turned out to be 46% of the processes. The 400 s was derived from that same partial
model, so it was always going to be optimistic. It stays as declared.

## What is left, for whoever takes the next pass

The remaining 2321 processes, in order: **git 1022** (rev-parse 304, cat-file 220, merge-base 179,
show 136, log 111, diff-tree 66), **grep 631**, **awk 296**, **sort 164**. At ~187 ms a process on this
fleet that accounts for essentially the whole 435 s, so the cost model — process count, not
algorithmic work — is intact; it was the DENOMINATOR that was wrong the first time.

The next lever is the per-item `rev-parse` / `cat-file -e` / `merge-base --is-ancestor` trio, which is
703 spawns answering ancestry and existence questions about a small set of shas. One `git cat-file
--batch-check` pass and one `git merge-base --is-ancestor` per PAIR rather than per row would take
most of it. That was not attempted here: it changes what the checker asks git rather than how often,
and this unit's whole safety property is that the stdout does not move.

## What this does NOT claim

- Not that the leg is now cheap. 435 s is still the longest thing on the bar.
- Not that the 2.43x transfers to the merge bar. Every figure here is a frozen clone, standalone. The
  leg's recorded gate-run reading is a different condition and a different number.
- Not that S4's spawn-count regression arm exists. It does not, and the reason is recorded in the
  spec: its only home is `check-unattended.test.sh`, which measured 9067 s and is RED — putting a new
  pin into a suite nobody can afford to run and that nobody has seen pass is the shape this whole
  build exists to argue against. It is named in the wrap-up instead.
