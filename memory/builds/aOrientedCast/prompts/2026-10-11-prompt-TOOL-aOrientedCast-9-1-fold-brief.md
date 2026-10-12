**Serves:** journal KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 TOOL-aOrientedCast-9

# Fold handoff — the cross-read's fixes, and one new spec

## Role

You are a software architect maintaining a set of unit specifications. You write no product code.
You change each spec only where a finding below names it, as a `rev-N` bump with its `§9` line
saying what changed and why. You leave every other sentence alone: a fold that rewrites what nobody
flagged is a new spec nobody reviewed. Where a finding asks you to resolve a fork, you mark it in
place in the shape `memory/TEMPLATE-SPEC.md` §8 states, as `RESOLVED (agent, 2026-10-11, delegated)`,
naming the option and the reason. You also author one new spec. You return only what the return
contract asks for.

## Task

**Repository:** `C:/projects/coding-governance/.claude/worktrees/deterministic-attended-workflows-943570`.
Specs are under `memory/builds/aOrientedCast/spec/`.

**Read first, whole:**
- `memory/builds/aOrientedCast/build/2026-10-11-build-TOOL-aOrientedCast-1-cross-read.md`: the
  twelve findings and the main loop's decisions, which bind you;
- `memory/builds/aOrientedCast/prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md`:
  the pinned interfaces and the invariants every spec follows;
- `memory/guides/BUILD-METHOD.md` M2 and M3.

**Fold, finding by finding.** The cross-read's file and line references were taken at `64c4d7ec0`,
which is HEAD.

1. **KICK-aOrientedCast-2.** Stage 5 passes `roles` from `handoff.py harness-args unattended-unit`
   on every unit dispatch, and AC3 counts that string. Add a criterion that runs the attended dry
   run: in a fixture clone holding a card with a real READY line, run the Skill's own `--part task`
   render line and each `harness-args` call it orders, then `handoff.py check` on the file written.
2. **TOOL-aOrientedCast-4:**
   - Raise and resolve a fork naming pinned interface 10: `unattended-build` takes `builder` and
     forwards it through `dispatch.args`.
   - Raise and resolve a second fork: its audit call forwards `specFinder`, `skeptic` and
     `synthesis` into the `tier2-review` call.
   - Its Edges name TOOL-aOrientedCast-1 and -2 for the stage keys, and TOOL-aOrientedCast-9 as the
     unit that makes the unattended caller pass them.
   - Its parked owner decision about the verbs becomes a hands-off to TOOL-aOrientedCast-9.
3. **TOOL-aOrientedCast-1:**
   - The stages table adds `builder` to `unattended-build` and lists the audit's three review roles.
   - `enforced-by` for `handoff` reads `none — a session-to-session message is no tool call the spawn
     guard sees`.
   - `spec-review` names the guard only once its audit runs under roles.
   - R9 admits a harness the tree does not hold, with a `note` line naming it, instead of raising.
4. **TOOL-aOrientedCast-2.** `harness-args unattended-build` prints `builder` and the audit's review
   roles, in step with item 3.
5. **TOOL-aOrientedCast-3.** S3 resolves an index harness the tree does not hold to a `note`, in step
   with item 3's R9, and writes nothing broken.
6. **TOOL-aOrientedCast-6:**
   - The refusal's render command spells `--build <slug>`.
   - The edge to TOOL-aOrientedCast-4 states that the builder prompt's divergence and status
     behaviour holds only when a caller passes `roles.builder`, and that an untyped unit pass is
     refused at landing either way.
7. **TOOL-aOrientedCast-7:**
   - S8 spells `--build <slug>`.
   - Add consumes-from lines for TOOL-aOrientedCast-4, -5, KICK-aOrientedCast-2 and
     TOOL-aOrientedCast-9.
   - Its Rollout's precondition becomes TOOL-aOrientedCast-9 at its order, not an unscheduled owner
     turn.
8. **TOOL-aOrientedCast-8.** The header reads `order 7`, and the Rollout says it lands at 7, before
   PLAY-aOrientedCast-1. Its F1 is re-decided by item 3's R9: `review-harness` stays optional, and
   its absence is a `note`.
9. **PLAY-aOrientedCast-1.** The header reads `order 8`. F1 is `RESOLVED (agent, 2026-10-11,
   delegated)` to option (a).

**Author one new spec: TOOL-aOrientedCast-9 — the unattended Skill and verbs pass the renderer's
`roles` to every harness call.**
- **File:** `memory/builds/aOrientedCast/spec/2026-10-11-spec-TOOL-aOrientedCast-9.md`. Tier-2,
  status `OPEN`, `rev-1`, `node a`, base `646d4a73581393acbf42f33864a9808c96d00a0c`,
  `streams tooling`, `order 6`.
- **Where:** the unattended kit's Skill template and verbs template, under `tools/unattended/` (their
  `*.template.md` sources), and the rendered copies the kit's adopter writes, `.claude/skills/unattended/SKILL.md`
  and `memory/guides/UNATTENDED-VERBS.md`. Read how `adopt-unattended.sh` renders and byte-checks
  them before deciding which bytes move.
- **What:** wherever the Skill or verbs tell the main loop to call `unattended-build.js`,
  `unattended-unit.js` or `tier2-review.js`, the call carries `roles` from
  `handoff.py harness-args <harness>`. Spell it once and point at it. Name what an adopter without
  the roles kit sees: the call carries no `roles`, and the harness logs its per-stage fallback.
- **Edges:** consumes-from TOOL-aOrientedCast-2 (the verb) and -4 (the keys); hands-off to
  TOOL-aOrientedCast-6 and -7 (the guards that refuse an untyped call).
- **Why here:** `UNATTENDED-VERBS.md` is the unattended protocol's companion, a governance carrier.
  This change is inside brief item 5 and the owner-confirmed goal, and say so in `§3`. State, as a
  `§3` Edge, what happens to a run already in flight that reconciles with a main carrying the guards
  before this text.

**Rules.**
- No product code.
- No commit: the main loop commits once after you return.
- Do not run the build-index generator.
- No merge bar, and no `*.test.sh` suite.
- Temporary files go under
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-deterministic-attended-workflows-943570/e131d82c-aaf3-45ad-abb9-258d7ab9ad1b/scratchpad`.
- Run `python tools/check-spec-tokens.py` once at the end, and fix any hit in a spec you touched.

**Return:**
- `folded`: one line per spec you changed, with its new rev and the finding numbers it answers;
- `authored`: the new spec's path;
- `forks`: every fork you resolved, with the option taken;
- `refused`: any finding you could not apply, with why;
- the `check-spec-tokens.py` exit status.
