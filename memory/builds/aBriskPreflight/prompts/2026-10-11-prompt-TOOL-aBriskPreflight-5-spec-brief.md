# Spec brief — TOOL-aBriskPreflight-5: the live-run count reads every record's phase in one pass and derives each record once

**Serves:** research TOOL-aBriskPreflight-5

Read first: the build README, the prompt record and the baseline record
(`build/2026-10-11-build-TOOL-aBriskPreflight-1-baseline.md`).

## What the trace shows

`check_single_live` in `tools/unattended/unattended.sh` walks every tracked `RUN.md` and
`RUN.*.md` (109 at BASE; most are retired archives, terminal by construction) and calls
`read_derived_phase` on each. That function reads the phase through `$(fact "$1" phase)` — `fact` is
a builtin `while read` loop, so the cost is the fork plus a byte-wise read of the file — and, for a
LANDING record (19 at BASE, because under `LANDER_MODE="in-place"` a landed record stays LANDING
until the next preflight of its slug), runs `read_landing_commit` in `tools/unattended/lib-unattended.sh`
(`check_lease_only_diff`, a `GIT show HEAD:<f> | extract_run_facts | sed | head | tr` pipeline, a
`GIT log -1 -- <f>`), `read_advertised_tip` and a `GIT merge-base --is-ancestor`. For each record it
then counts live, the announcement loop calls `read_derived_phase` AGAIN and `fact … witness`. The
peer's trace charges about 306 s to this walk.

## The mechanism, one

The live-run count asks each question once for the whole population instead of once per record: the
phase of every record in one read, the LANDING records' landing commits and committed phases in
one pass over git, the ancestry of all of them against the one advertised tip together, and the
announcement reuses what the count derived instead of deriving it again.

## What may not move

- The answer. `read_derived_phase` is "the leg's reading too, so preflight and the bar agree about
  one record": the batched reading must give, for every record, the same phase, the same
  `DP_LANDING`, `DP_AREF`, `DP_TIP` and `DP_REASON` the per-record function gives, and the spec must
  say how that is observed over the real population (every record in the tree at BASE), not argued.
- Every `EXCLUDED …` line, the `N concurrent unattended run(s)` block, the `UNAVAILABLE` line and the
  claims block, byte for byte and in the same order.
- FAILS CLOSED, as the function's comment says: no observation, an uncommitted record, or a landing
  commit off the tip leaves the record LANDING.
- `read_derived_phase`'s other twelve callers keep calling it as they do.

## Out of scope

- Converting `fact`, `runmd_of` or `readme_of` to fork-free readers: aSparedSpawn-8 S1. A batched
  read for this one walk is not that conversion; the spec says why the two do not collide.
- The gate leg's own copy of this walk in `check-unattended.sh`.

## Acceptance shape

- An equivalence probe over every tracked record at BASE: per-record function against the batched
  reading, field by field, zero differences, printed with the population size so a probe that read
  nothing cannot pass (a zero-guard does not catch "some").
- The spawn count of the walk before and after, with the build's `trace-spawns` instrument.
- RED on a staged break: a LANDING record whose landing commit is NOT on the tip must still count
  live; a record with no committed copy must still count live.
- Witnesses in §6 by basename.

## Conventions

- Tier-1 if the reading is proven equal; the spec decides.
- Lexicon verbs; `gen_map.py --write`; the unattended kit bumped once at the end of the build.
- Order: 1, with units 1 and 6 (disjoint write sets).
