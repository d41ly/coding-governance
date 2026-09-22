# S3 — where a `check-unattended.sh` invocation's time actually goes

**Serves:** journal TOOL-aGradedDoorway-7

**The spec refused to design past this number and this is the number.** `TOOL-aGradedDoorway-7` §4
inferred the split from a division (15270 s over 265 runs) and said so in the text: *"S3 exists
because this paragraph is arithmetic on two measured numbers rather than a third measured number,
and the whole ranking below rests on it."* AC3 forbids citing that inference once this file exists.

## Method

The suite's own fixture, reused rather than reproduced: `head -n 272 check-unattended.test.sh` is
everything up to `if in_shard 1; then`, which is exactly the prologue that builds the tree, the bare
origin, the anchor commit and the conforming `.unattended.conf`. Run from `tools/unattended/` so the
suite's `HERE=$(cd "$(dirname "$0")" && pwd)` resolves to the real kit — the first cut ran it from a
scratch directory, every `cp "$HERE/…"` failed, and the resulting 122 ms "invocation" was a shell
exiting 127. That number is recorded here because it looked exactly like a finding.

Node `a`, 16 logical cores, Windows/MSYS, 2026-08-29. Gov at `1344f4bc`, kit `unattended@1.12`.

## The measurement

One `bash tools/unattended/check-unattended.sh` against that fixture:

```
real    2m8.014s
user    0m12.138s
sys     0m43.904s
```

| term | seconds | share of wall |
|---|---|---|
| check bodies (user CPU) | 12.1 | **9.5 %** |
| kernel — process creation, git plumbing, file I/O (sys CPU) | 43.9 | 34.3 % |
| not on CPU at all — scheduler, I/O and on-access scanning | 72.0 | 56.2 % |

`sys / (user + sys)` is **78.4 %**, which is the same ratio the sibling session measured on the real
inCMS corpus (485.2 s real / 79.3 s user / 287.4 s sys). Two different trees, two different corpora,
the same shape — so this is a property of the workload, not of either fixture.

Per-spawn cost on this node, measured directly over 100 iterations each:

| operation | cost |
|---|---|
| shell builtin (`:`) | 0.053 ms |
| `grep` spawn | 181 ms |
| `bash -c` spawn | 251 ms |
| `git rev-parse` spawn | 371 ms |

**A spawn costs 3 400 to 7 000 times a builtin here.** At ~250 ms and a 128 s invocation, the
checker is making on the order of 500 process creations per run — which agrees with the census
`TOOL-dNarrowedAnchor-1` took on node `d` (469 before its cut, 220 after), so the count is stable
across nodes and only the unit price moves.

## What this settles

**1. The §4 inference holds, and by a wider margin than it claimed.** It estimated ~53 s of a 57 s
run was fixed overhead. Measured, the check bodies are 9.5 % of wall. Decomposing checks 1-27 so
`--only <n>` accepts any n targets that 9.5 %: a perfect 30-way split that eliminated every check
body entirely would return one tenth of the cost, for the largest and riskiest refactor on the list.
It stays rejected, now on a measurement rather than a division.

**2. The ranking inside §4 is wrong in one place, and S4 should move up.** Sharding splits
invocations across workers and lowers the FLOOR; it removes no spawns. S4 — batching arms that share
a tree state into one `run()` — removes invocations outright, and invocations are 90.5 % of the
cost. On the ordering the owner ratified (S1, then S3, then S4 and S2 on its answer) this is S3's
answer: **S4 before S2.**

**3. The largest single factor is the node, and it is not a code change.** Gov's own ceiling comment
records 19-39 ms per spawn on node `d`; node `a` measures 251 ms. That is 6.4 to 13 times, and it is
most of the gap between this suite costing 3 565 s there and 15 270 s in the inCMS adopter here. An
on-access scanner in front of every `exec` is the documented cause. **The remedy is an exclusion for
the repo and temp trees on the affected node, which is an operator action on system security
settings — this record names it and does not perform it.** No amount of sharding recovers a 10x unit
price.

## What is NOT measured here, said plainly

- The 128 s is ONE invocation on a COLD tree, against gov's `check-unattended.sh` at 1.12, which
  does not carry the adopter's check-30 memo. inCMS's own average is 57 s per run over 265 runs of
  its patched copy on a 302-build corpus. These are different programs on different corpora and the
  two wall figures must not be compared; the three-way SPLIT is what transfers, and it transfers
  because the sibling measurement on the real corpus reproduces the same 78.4 %.
- The spawn count is inferred from wall ÷ unit price and corroborated by gov's own census. It was
  not counted directly in this run: an `xtrace` census over the same invocation returned 2 lines,
  because `set -x` in the parent does not follow into the child the suite actually runs.
