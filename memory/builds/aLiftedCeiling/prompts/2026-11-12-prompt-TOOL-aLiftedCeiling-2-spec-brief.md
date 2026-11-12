**Serves:** research TOOL-aLiftedCeiling-2

# Brief: spec TOOL-aLiftedCeiling-2 — the closing review's minor: the evidence row names its host load

## The prompt

> Yes, raise it

— owner, 2026-11-12. The closing review's round 1,
`memory/builds/aLiftedCeiling/reviews/2026-11-12-review-TOOL-aLiftedCeiling-1-diff-review-round1.md`, CONVERGED clean with one LOW,
which the kit promotes to a unit; read it whole first.

## The brief

### Goal

Write spec TOOL-aLiftedCeiling-2, a micro-spec for one mechanical unit at order 2: the instruction-edits leg's evidence row in
`tools/run-gates/ceiling-evidence.txt` carries a `--how` text that names the host load during its race and the commit its clone
was taken at, as the file's header and spec TOOL-aLiftedCeiling-1 ask.

### Items

1. **Where you write.** Write the new spec only at
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/foldal2/2026-11-12-spec-TOOL-aLiftedCeiling-2.md`;
   write nothing under the repository. Follow `memory/TEMPLATE-SPEC.md` for a Tier-1 micro-spec; status line `DEFERRED · rev-1 ·
   2026-11-12 · node a · Tier-1 · base <HEAD short sha> · streams tooling · order 2`. Write no open fork: where a choice remains,
   take your recommendation and mark it resolved in its own span.
2. **The row.** The row stands at 110 s, written by `derive-ceilings.py --write --observed` from a race in a fresh clone of
   `33a1a8676`, the unit's own pass commit, where unit 1's spec named its base `123123146`; the race ran with no other gate run on
   the host. Read how the kit rewrites an observed row whose value does not change (the file is monotone and generated, never
   hand-edited), and say how the row's source text is replaced through the kit, whether the clone's commit is named as run or the
   race repeated at the base the spec named, and that the diff stays one row.
3. Criteria observe the row's source naming the host load and the commit, the file's diff against the build's base still one added
   line, and the ceiling check still green. The spec-token check grades a live spec's acceptance bullets word by word: no acceptance
   command whose words include an untracked path, no `path#symbol`, no suite as the observation, each backticked span on one line,
   every tripped leg on the gates line. Every new fact pinned, every new `path:line` blob-pinned.

### Acceptance

- Spec TOOL-aLiftedCeiling-2 builds as written over HEAD, and its row's source states the load it was measured under.

### Gates

None run on the repository: this is a scratch write.

### Non-goals

- No code. No edit outside the scratch copy. No change to the ceiling or the measured value.
