**Serves:** research TOOL-dRankedPlan-1 TOOL-dRankedPlan-9 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-31

# Brief: the owner's picks on the re-ground's open forks

## The prompt

> take the recommendations on the forks

— owner, 2026-10-29, on the forks the re-ground left open, as the cross-check record's "After the
re-ground" section lists them
(`memory/builds/dRankedPlan/build/2026-10-28-build-TOOL-dRankedPlan-1-parents-crosscheck.md`).

## The brief

### Goal

Mark each of the three forks below resolved by the owner to the option its own spec recommends, and
make each spec read as its fork now decides. No spec's design changes beyond what the pick settles.

### Items

- rp9 F6 (a): the ask to TOOL-dRankedPlan-16 for `plan_record.py path <slug>`. Both units are this
  build's, so the pick is a step of unit 16, not an ask across builds: state it in rp16 as a verb it
  adds, with the acceptance line rp9 F6 gives, and in rp9 S5 and rp15 as the route they take.
- rp15 F8 (a): the `enforces` tag option (a) names, written into the leg's `[[gate_leg]]` declaration
  and any criterion that reads `enforces`.
- rp31 F1 (a): the same, for the `session-predicate callers` leg.

One writer revises specs 9, 15, 16 and 31; rp16 is touched only for the verb rp9 F6 picks. The spec
files are `memory/builds/dRankedPlan/spec/2026-10-2?-spec-TOOL-dRankedPlan-<n>.md`. Write probe copies
only under
`C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-elastic-lalande-a8b091/bd0d7692-8d65-44a9-bf88-d3f42e06b8de/scratchpad/rp-f/`,
and delete nothing else there. Return, per spec: the rev it now reads; each fork resolved and its
pick; the sections moved; and its byte count.

In every spec you revise:

- Bump the **Status:** line's `rev-N` to `rev-N+1`, dated 2026-10-29, the status kept `DEFERRED`.
- Mark each fork in place: `RESOLVED (owner, 2026-10-29): (<letter>) <the pick in a few words>.` Drop
  "Open for the owner".
- Replace each sentence that points at the fork as open with the picked route, where it stands.
- Add one §9 line naming the forks resolved, this brief, and the sections moved.
- Stay under the class cap of 49152 bytes.

### Acceptance

- `wc -c <spec>` is under 49152.
- The **Status:** line reads `rev-<N+1>` dated 2026-10-29, and §9 holds the new line.
- `grep -n "Open for the owner" <spec>` prints no line of a fork this brief names.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only
  your specs staged into it through `GIT_INDEX_FILE`, names none of your specs. Findings that only a
  `gen_build_index.py --write` render cures belong to the main loop.

### Gates

Only the memory hygiene gate and the naming lexicon, as the role allows.

### Non-goals

- No file outside specs 9, 15, 16 and 31. No commit, no stage into the real index, no deviation
  record, no `BACKLOG.md` row.
- No fork other than those named, and no other build's spec.
