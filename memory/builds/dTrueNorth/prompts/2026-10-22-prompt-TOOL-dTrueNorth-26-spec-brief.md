**Serves:** research TOOL-dTrueNorth-26

# Spec brief — dTrueNorth, the closing review's 19 minors

## The prompt

> The closing diff review of dTrueNorth (round 1, CLEAN WITH FIXES, 0 blockers, 3 high, 19 minors, CONVERGED) batches every confirmed MEDIUM and LOW into one unit (BUILD-METHOD M4). The owner capped spec audits at two rounds, so this spec is built as written, unaudited.

## The brief

### Goal
Author TOOL-dTrueNorth-26, the one unit that closes every confirmed MEDIUM and LOW of `memory/builds/dTrueNorth/reviews/2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md`: items M1 to M9 and L1 to L7, each by its finding id, each its own scope item. Author only: no product code, no commit, no gate.

### Items
1. One scope item per finding id in M1 to M9 and L1 to L7 (19 findings), each with the review's stated fix, the skeptic's where it corrects the finder's (findings 14, 18, 21, 22), and an observation criterion. M7 (finding 20) is discharged by TOOL-dTrueNorth-25, which closes the same defect as H3: name it as a hands-off, not a scope item of this unit.
2. Path `memory/builds/dTrueNorth/spec/2026-10-22-spec-TOOL-dTrueNorth-26.md`, H1 `# TOOL-dTrueNorth-26 — <title>` with an em dash, status `OPEN`, Tier-2, `streams tooling`, `order 10`, a column-0 `**Derived:** PLAY-dClosedLoop-2` line, §3 Edges naming the units whose code it amends and consumes-from TOOL-dTrueNorth-23 to -25 where it touches their files, a `New arm:` line per suite it adds an arm to, §8 forks resolved by README rule 6's rungs, §10's two probes run. Keep it under the 49152-byte spec ceiling (`tools/template-size-limits.txt`), leaving room for its generated records region.
3. Write its deviation record beside the spec: `memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-26-deviation-25.md`, in the `deviation` kind's grammar (read any existing `memory/builds/dTrueNorth/build/*-deviation-*.md`): Departs from `dTrueNorth [roster]`, hand-off design-to-spec, cause review finding, risk additive, approver spec writer under author-recorded (`PLAY-dClosedLoop-4`), follow-through `new unit TOOL-dTrueNorth-26`, Caused-by `PLAY-dClosedLoop-2`.

### Acceptance
`python tools/check-spec-tokens.py` prints no hit on the spec; every acceptance criterion is a probe a pass can run without a gate; the record reads with no malformed field under `python tools/memory-tree/deviation_join.py`.

### Gates
No gate runs in this pass; the spec's §7 lists what the close runs.

### Non-goals
The three highs (TOOL-dTrueNorth-23 to -25); any other unit's spec; product code; inside §6, an untracked file named by full path inside a backticked token; a criterion naming a gate leg, a `*.test.sh` run or the bar.
