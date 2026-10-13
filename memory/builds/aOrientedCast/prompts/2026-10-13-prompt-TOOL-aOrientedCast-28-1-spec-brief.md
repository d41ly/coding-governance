**Serves:** journal TOOL-aOrientedCast-28

# Spec handoff — spec folds run through the build harness

## Role

You are a code architect writing the specification for one unit. You write no code. A builder builds
from your spec alone. Verify every claim about current code by reading it, and cite path and line.
A choice you cannot derive is a fork, resolved by M3 of the build method and marked
`RESOLVED (agent, 2026-10-13, delegated)`. You run no gate and no self-test; the only checks you may
run are memory hygiene and the lexicon. You write only this unit's spec file. You do not commit, and
you do not regenerate any index.

## Task

**Repository:** `C:/projects/coding-governance/.claude/worktrees/deterministic-attended-workflows-943570`.

**Why:** the owner's sixth addendum, `memory/builds/aOrientedCast/prompts/2026-10-13-prompt-TOOL-aOrientedCast-1-8-owner-addendum.md`,
"The follow-up". In this build every spec FOLD ran as a direct `gov-spec-writer` spawn, because the
spec stage of `tools/workflows/unattended-build.js` authors only MISSING specs and leaves a present
one alone. A direct spawn cannot set its effort (the `Agent` tool has no effort parameter), counts
against the per-prompt-turn direct-spawn budget an unattended run cannot reset, leaves no harness
journal, and returns free text.

**The spec:** `memory/builds/aOrientedCast/spec/2026-10-13-spec-TOOL-aOrientedCast-28.md`, status
`OPEN`, `rev-1`, `node a`, base `646d4a73581393acbf42f33864a9808c96d00a0c`, Tier-2, `streams tooling`,
order 29. Full ten sections.

**Scope to design:**
1. **A fold route in the build harness.** A caller hands `unattended-build.js` units to FOLD: each a
   present spec, a fold brief, and the rev it must reach. The stage spawns them as the `specWriter`
   role, at `efforts.specWriter`, with a schema'd return naming the new rev and what moved, and does
   not author, audit or hand out a roster for them. Decide whether this is a new mode, a new `units`
   field, or a sibling harness; reuse the spec stage's existing role, effort, label and commit
   handling rather than copying it. Its commit stage refuses on a foreign tree change exactly as the
   spec stage's does.
2. **The spawn guard closes the direct route.** Once the fold route exists, rule 6 of
   `tools/hooks/agent-cap.js` refuses an `Agent` call whose `subagent_type` is the spec-writer role
   from a session holding a non-terminal run's lease, naming the harness route. Read the lease the
   way `tools/unattended/gate-guard.js` and `run-lease.js` already do; one reader, not a copy.
   Outside a live lease, a direct spec-writer spawn stays legal, so attended work is unchanged.
3. **The docs that route a fold:** the unattended verbs template and the `/build` Skill template name
   the fold route where they now say how a spec is revised.

**Read first:** `memory/guides/BUILD-METHOD.md`; the "Invariants for every unit" of
`memory/builds/aOrientedCast/prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md`; and the
specs of TOOL-aOrientedCast-4 (the build harness's roles), -7 (the spawn guard), -22 and -24 (the
lease readers) and -27, which is OPEN and edits rule 6 and the three harnesses' labels. This unit
builds after TOOL-aOrientedCast-27: share its files only in that order, and say so in §3.

**Kit versions:** bump each kit this unit moves, once, after TOOL-aOrientedCast-27's steps. Read the
carriers from `tools/check-kit-versions.sh` without running it.

Each new refusal gets a `New arm:` line naming its staged break; its red-first observation is the
main loop's at the close. Every §6 criterion is a direct check a builder may run.

**Return:** `authored`, `forks` with the option taken, `refused` with why, and the memory hygiene exit
status over your file if you ran it.
