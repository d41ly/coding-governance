**Serves:** research TOOL-dDeclaredLoop-28

# Brief: revise spec TOOL-dDeclaredLoop-28 onto unit 27's composition input

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. TOOL-dDeclaredLoop-28's re-ground (rev-5, parked by the run, not yet committed) adds a `--layer` flag to
`overlay_rows.py compose` so a build's applied rows reach its composition, and says it reuses unit 27's flag if 27 lands one
first. Unit 27's committed rev-4 adds `compose --kind <kind> --rows -` for the same job (its section 8 F8). One input per
job: the run's reuse practice holds that a kind's second instance reuses the first.

## The brief

### Goal

Write `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-28.md` as rev-6, with one revision-log line, so the
build's applied rows reach the composition through unit 27's `--rows -` input and no second compose input is added.

### Items

1. Your worktree may be cut from main. Start from the run's parked rev-5, copied whole from
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/b120d4a7f8b5be2e/7c85732c-fa0c-43e9-83f2-238d293195e0/scratchpad/pending/spec-28.md`
   into your copy of the spec's path. Read unit 27's committed rev-4 and every code claim from
   branch/unattended-declared-loop-d56bf0 through `git show`.
2. Replace the `--layer` flag in S6, F6, §4 and §5 with unit 27's `--rows -` input, passed by `read_composition`,
   `read_composition_at` and `position.py` as 27 defines it; name 27 as consumes-from with a matching edge where 27 hands
   it off, and say in §5 that 27 builds first (order 24).
3. Keep F7 and F8 as rev-5 resolved them, and keep the decision row text §5 spells out for the `REFUSAL_CEILINGS` raise.
4. Keep the unit one mechanism, its carries, its order and its DEFERRED status. Write only that spec file. Do not commit and do
   not regenerate any index. Run the spec-token checker with its spec flag over the spec and fix every hit. Do not run the
   whole-tree memory hygiene gate, and do not ask any checker for its help text. Each Readers half sits on one line.
5. Never kill a process you did not start, never match processes by a script's name to stop them, and never run
   check-memory-hygiene.sh, not even with --help.

### Acceptance

- The revised spec adds no compose input beyond unit 27's, and the spec-token checker reports no unwaived hit.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.
