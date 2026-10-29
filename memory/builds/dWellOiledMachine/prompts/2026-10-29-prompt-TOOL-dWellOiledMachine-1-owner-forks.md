**Serves:** research TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-54

# Brief: the owner's picks on the re-ground's open forks

## The prompt

> take the recommendations on the forks

— owner, 2026-10-29, on the forks the re-ground left open, as the cross-check record's "After the
re-ground" section lists them
(`memory/builds/dWellOiledMachine/build/2026-10-28-build-TOOL-dWellOiledMachine-1-parents-crosscheck.md`).

## The brief

### Goal

Mark each of the 23 forks below resolved by the owner to the option its own spec recommends, and make
each spec read as its fork now decides. No spec's design changes beyond what the pick settles.

### Items

The forks, by spec, each resolved to the option the fork's own recommendation names (re-read the
fork; the letter here is what it recommends today):

- wm1 F4 (a), wm11 F5 (a), wm12 F5 (a), wm20 F2 (a), wm23 F4 (a), wm33 F4 (a), wm39 F6 (a): the
  `enforces` tag each fork's option (a) names. Write that tag into the leg's `[[gate_leg]]`
  declaration wherever the spec states the row, and into any criterion that reads `enforces`.
- wm2 F4 (a), wm5 F3 (a), wm6 F4 (a), wm7 F5 (a), wm11 F4 (a), wm26 F5 (a), wm30 F3 (b), wm32 F6
  (b), wm43 F4 (a), wm52 F3 (a), and wm4 F3 (b): the ask each fork names. The build run files it in
  the owning build's `BACKLOG.md`; this pass files no row. Where the spec reads "until the pick" or
  "before the pick", state the picked route.
- wm26 F4 (a): the verb it asks dDeclaredLoop for is the one TOOL-dBoundRoles-3 §8 F5 already asks
  (`loop_lib.py declaration`). Say so in the fork: one ask, filed once, serves both, and this build
  files no second row for it.
- wm43 F3 (a), widened: the asked `handoff.py stage-rows <harness>` also prints each workflow entry's
  `driver` and `stage`, because wm54 S2 filters the entries' roles by them. Name wm54 among its
  readers, and state in wm54 S2 that its filter reads those two fields from the same verb.
- wm43 F5 (a), wm48 F4 (a), wm54 F5 (a): this build adds the verb itself (`scope.py --self-chain`,
  `policy.py get --row`, `gen_build_index.py --units`). The file joins Files touched, as the fork
  says, and the step that adds the verb reads as settled.

Not touched:
- wm39 F4, which a writer re-resolved on rung 1; the owner's answer keeps it.
- wm58 F5, which follows TOOL-dTotalRecall-2 §8 F6. That fork is dTotalRecall's, still open, and is not
  this build's to pick.

Groups, one writer each. The spec your handoff's `input:spec` names leads one group. Revise every spec
of that group, and no other:

- **Group A, led by spec 1:** specs 1, 2, 4, 5, 6, 7, 11, 12, 20 and 23.
- **Group B, led by spec 26:** specs 26, 30, 32, 33, 39, 43, 48, 52 and 54.

The spec files are `memory/builds/dWellOiledMachine/spec/2026-10-2?-spec-TOOL-dWellOiledMachine-<n>.md`.
Write probe copies, such as a `GIT_INDEX_FILE` index copy, only under
`C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-elastic-lalande-a8b091/bd0d7692-8d65-44a9-bf88-d3f42e06b8de/scratchpad/wm-f<group letter>/`,
and delete nothing else there. Return, per spec: the rev it now reads; each fork resolved and its
pick; the sections moved; and its byte count.

In every spec you revise:

- Bump the **Status:** line's `rev-N` to `rev-N+1`, dated 2026-10-29, the status kept `DEFERRED`.
- Mark each fork in place, in the closed-paren form `memory/TEMPLATE-SPEC.md` gives:
  `RESOLVED (owner, 2026-10-29): (<letter>) <the pick in a few words>.` Drop "Open for the owner".
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

- No file outside the spec files of your group. No commit, no stage into the real index, no deviation
  record, no `BACKLOG.md` row: the main loop and the build run write those.
- No fork other than those named, and no other build's spec.
