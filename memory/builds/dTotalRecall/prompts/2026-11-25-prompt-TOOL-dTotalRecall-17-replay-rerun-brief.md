**Serves:** journal TOOL-dTotalRecall-17 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-26
**Caused-by:** TOOL-dTotalRecall-111

# Brief — dTotalRecall: the map replay run again with more runs per arm

## The prompt

> redesign the record under a bound it can meet, run the replay again with more runs per arm. Why weren't those decisions made under the unattended protocol?

— owner, 2026-11-25, in this run's session on node a, answering asks TOOL-dTotalRecall-109 and TOOL-dTotalRecall-111.

## The brief

### Goal

One new spec, `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-123.md`, Tier-2, that re-runs the map replay
of TOOL-dTotalRecall-17 with more runs per arm and a verdict rule stated before any run. TOOL-dTotalRecall-17 is CLOSED and
frozen; its first verdict record stands as the first experiment.

### Items

1. Read spec 17, its verdict record `2026-11-23-build-TOOL-dTotalRecall-17-map-replay-verdict` and
   `tools/workflows/replay_scorer.py#measure_map_experiment` and `#derive_map_verdict`, with TOOL-dTotalRecall-121 S10's fix of
   the byte term, which read zero in all forty runs of the first experiment (DERIVED 2026-11-23, that record).
2. **The twin difference cannot take more runs as it stands.** It is, summed over the audits, the larger arm's
   max-less-min over its runs, so a range GROWS with the run count and more runs would raise the losing line. State
   the estimator the re-run uses before any run: what noise term replaces it, how the mean of n runs per arm enters, and
   the losing line for recall, with a fixture arm that shows more runs tightening it. Say what that change relaxes and
   join it with the record the build's fork rule asks for.
3. State the run count as a manifest figure the main loop fills, with the effect size a count resolves at the first
   experiment's spread: between-run spread of about eight items per run (DERIVED, the first record's own figures, to be
   re-derived and stated), so five runs per arm resolve a rise near ten and about eighteen resolve five. The main loop takes
   the owner's answer, or five where none came. No run of the first experiment is pooled into the second.
4. The arms, subjects, map and clones are spec 17's, by reference; the clone names take the next free `<n>`. The scorer's
   change, if any, is this unit's code, with its arms.
5. The verdict record, its path and its two routes: on `win` units 14, 15 and 26 are re-opened by the main loop; on
   `lose` they are retired, with their clauses cl-dClosedLoop-0225, -0226 and -0237 re-homed as ask
   TOOL-dTotalRecall-111 names, which no run does by itself. State that the rule is fixed before the first run.
6. Scaffold through `python tools/memory-tree/gov_record.py new spec TOOL-dTotalRecall-123 --tier 2 --order 51`, renamed to the
   path above where the door dates it otherwise; shape and binding line as `2026-10-26-spec-TOOL-dTotalRecall-122.md`.
7. The checks: `--check-specs`, `check-spec-tokens.py --spec`, hygiene check 12 over the spec. Run no gate leg.
8. Your write grant is the spec file of TOOL-dTotalRecall-123 alone, status `OPEN`, rev-1; read this brief's own Limitations at `memory/builds/dTotalRecall/prompts/2026-11-25-prompt-TOOL-dTotalRecall-17-replay-rerun-brief.md` before the first edit.

### Acceptance

The rule, the estimator and the count are stated before any run, the estimator falls with more runs in a fixture arm, and the
commands name no finding.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No replay run here. No edit of spec 17 or of its verdict record. The code record is another brief's.

### Limitations

The write grant is that spec file alone, status `OPEN`, rev-1. Do not commit. A worktree-isolated session refuses an inline
command that embeds git: put it in a script file. Scratch goes under
`C:/Temp/claude/7a8436c9e3b87ce5/9067262b-db21-4497-8ba8-ef2deab46f53/scratchpad/u123/`.

### Reuse

Spec 17's design, and the replay factory's `check_experiment` and its instances.
