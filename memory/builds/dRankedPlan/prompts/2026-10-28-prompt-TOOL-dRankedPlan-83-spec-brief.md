**Serves:** research TOOL-dRankedPlan-83

# Spec brief — TOOL-dRankedPlan-83, the routed commits leg's ceiling covers this run's close

## The prompt

The owner answered the run's second hand-off `owner-decision` at `5232949ca`: "Raise the routed-commits leg's ceiling
the same way as TOOL-dRankedPlan-82, then re-prepare onto origin/main, re-close and land dRankedPlan." The answer is
recorded in `memory/builds/dRankedPlan/prompts/2026-10-27-prompt-TOOL-dRankedPlan-1-owner-review-until-no-high.md`.

With the spec tokens leg green at its new 830 s ceiling, the close's bar at `9c135e17d` redded only
`routed commits name a specced unit`: timed out at its 300 s ceiling in the pool and on its serial retry, attributed
CONTENDED. The main loop then ran it alone in 354 s, exit 0, with another session's two staged hygiene checks
running as it started, so that reading is not R. dWellOiledMachine's close measured the same leg at 358 s alone.

## The brief

### Goal
Author `memory/builds/dRankedPlan/spec/2026-10-28-spec-TOOL-dRankedPlan-83.md`, a Tier-1 micro-spec, status
`DEFERRED`, carrying no `order` verb, in the shape of
`memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-82.md` at rev-2, which it follows section for
section. Like unit 82 it is built in this run, not carried forward. Author only: no product code, no commit.

### Items
1. R is the main loop's, the larger of its two readings of the leg alone, each by `time` over this leg's argv
   (`tools/gate-legs.json:1096-1099`) with `GATE_PUSH_BASE=1a61f21a2`, the prepared merge's first parent, on node a:
   354.0 s (exit 0) after the close at `9c135e17d`, another session's two staged hygiene checks running as it
   started; and 295.5 s (`real 4m55.499s`, exit 0) at `922d6b94d`, 39 commits past that base, 03:44:56 to 03:49:52,
   another worktree's `--dispatch` running its `tools/check-spec-tokens.py` across part of it. The evidence row is a
   maximum, so R is 354.0 and C is 10 x ceil(354.0 / 5) = 710. State both readings, their census and the idle
   orphan `run-gates.sh` (pid 10907, Oct 23) in the spec and in the `--how` text. The builder takes no reading and
   runs no gate leg: the role gate refuses both legs to `gov-builder` (unit 82's §4).
2. S1 is this leg's ceiling in `tools/gate-legs.json` (`:1104`, 300 today) and its evidence row in
   `tools/run-gates/ceiling-evidence.txt`, which today holds no row for this leg: read `derive-ceilings.py` for
   what `--write --observed` does for a leg with no row and what its summary then prints, and spec that. C is the
   least multiple of 10 at or above 2R. No other row of either file moves. S2 is the `last-audit` re-stamp of
   `memory/guides/SESSION-KICKOFF.md`, as in unit 82. Read every cited line from the tree at this unit's base.
3. Name what the raise does not check: where the leg's time goes, read from `tools/memory-tree/routed_commits.py`
   (its deviation arm joins every chain build's records), and when the ceiling comes back down.
4. AC1 (the main loop's: red against the parent's manifest through `GATE_LEGS`, green at the pass commit), AC2 (the
   main loop's reading, and its red at a base where the range holds few commits, if one exists — say which), AC3 and
   AC4 (the builder's, on its staged change), each with `Red when:`, as unit 82 rev-2 states them.
5. §6 names the legs the three touched files owe through `python tools/check-spec-tokens.py --legs-for`.
6. §7 "Open questions" reads exactly `none`; any follow-up goes in §8 as prose. Keep every acceptance code span on one
   line and free of a `|`; no retirement word in §2; an untracked path sits in a fenced block; never write a probe
   copy of a spec inside the spec folder.

### Acceptance
`python tools/check-spec-tokens.py` names nothing in this spec and hygiene check 12 names nothing in it; the main loop
runs both on a quiet host, so run neither yourself.

### Gates
None of your own.

### Non-goals
`routed_commits.py` and every other checker; any other leg's ceiling; the run-gates runner;
`tools/run-gates/ceiling-margin.txt`.

### Reuse
`TOOL-dRankedPlan-82` rev-2 and its pass `026bc5055`; `tools/run-gates/derive-ceilings.py`.
