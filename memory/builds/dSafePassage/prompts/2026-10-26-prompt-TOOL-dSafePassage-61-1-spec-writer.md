**Serves:** research TOOL-dSafePassage-61 TOOL-dSafePassage-1

# Brief: TOOL-dSafePassage-1's F8 stop fired — split the gov migration of the size-limits file into TOOL-dSafePassage-61

## The prompt

No owner prompt: the build run's own divergence, under the run's delegated M2 AMEND authority.

## The brief

### Goal

TOOL-dSafePassage-1 builds as far as the landed policy guard allows, and the gov migration of the size-limits file waits in TOOL-dSafePassage-61 for TOOL-dGroundRules-13, every sibling spec agreeing with the split.

**Why.** The build run dispatched TOOL-dSafePassage-1 first. Its builder stopped before writing code and returned a
DIVERGENCE at §8 F8, whose resolution ends "The build run's first pass reads whether the landed guard grants
it, and stops S8 if not." The landed guard does not grant it:

- `tools/policy/guard.py` (TOOL-dGroundRules-6, CLOSED, landed on main at `60d90cb7`) admits one agent shape:
  a single measured-file cap raised. A probe of its own `check_raise_shape` over S8's write (the seven rows of
  `tools/template-size-limits.txt` moved into `[budgets]` of `.governance/policy.toml`, values unchanged)
  printed `refused=True · why: 7 keys changed; one cap raised is the one agent shape`; one cap raised with a
  `RAISED` comment printed `refused=False`.
- `.githooks/pre-commit:199-213` runs that guard with `--staged` on any commit made without a terminal that
  stages the policy file, so the pass commit is refused. Going around it (`--no-verify`, a pty wrapper) routes
  around a tool's refusal and is not an option.
- `TOOL-dGroundRules-13`, the ask that would admit a value-preserving step write, is OPEN and DEFERRED in
  `memory/builds/dGroundRules/BACKLOG.md`.

The run recorded the amendment: `--rescope dSafePassage --act add --item TOOL-dSafePassage-61` (RUN.md).

**The constraint every revision must hold.** Nothing this build lands may write `.governance/policy.toml` in a shape the landed guard refuses — not
TOOL-dSafePassage-1's pass commit, and not a later unit's. That includes the gov-first walk: TOOL-dSafePassage-8's
lander runs each declared step's up on gov's own tree in the prepared merge, so a step DECLARED in this landing
whose up on gov writes the policy file in a refused shape meets the same refusal at the landing. Decide from the
specs and the code whether that forces S7's step row itself (`govkit/template-size-limits-to-budgets`) out of
this landing along with S8, or whether S8 alone moves. Check S6 (`agent-cap/fanout-cap-to-agents-in-flight`)
the same way: does its up on gov write the policy file, and would the guard refuse it? State what you found.

### Items

1. **Author `memory/builds/dSafePassage/spec/2026-10-26-spec-TOOL-dSafePassage-61.md`**, Tier-2, status
   `DEFERRED`, `advances TOOL-dSafePassage-14`, with an `order` after every unit it needs, carrying the items
   the constraint forces out of TOOL-dSafePassage-1 (S8 at least; S7 if the constraint forces it) and the
   criteria that observe them (AC15, AC19, the S8 half of AC13, and AC13/AC14 whole if S7 moves). Its
   DEFERRED reason names `TOOL-dGroundRules-13`. Its **Carries:** follows the carried clause
   (`cl-dClosedLoop-0018`) exactly as TOOL-dSafePassage-1's does. Keep the design text as spec 1 has it; this
   is a move, not a redesign.
2. **Revise TOOL-dSafePassage-1** as a rev-11 bump dated 2026-10-26, still `DEFERRED`: remove what moved,
   point at TOOL-dSafePassage-61 where a reader needs it, mark §8 F8 with what the build run's first pass
   found (`F8's stop fired, 2026-10-26: the landed guard refuses; S8 [and S7] moved to TOOL-dSafePassage-61`),
   and add one §9 line naming this brief. Every remaining AC must be observable without the moved items,
   including the selftest `New arm:` line's `covers` list.
3. **Cross-read every sibling spec** that names the moved items, the size-limits file, `template-size-limits`
   or the step id — at least TOOL-dSafePassage-5, -8 and -26 do — on M2's four axes (scope, interface,
   ordering, acceptance). Fix a disagreement in exactly the one document that is wrong, as a rev bump with a
   §9 line naming this brief. A sibling criterion that can only be observed once the moved item lands moves to
   TOOL-dSafePassage-61 too.
4. **Add TOOL-dSafePassage-61's row** to the README's authored `roster:units` table (`**Derived:**` the
   build-run divergence, its clause one line), and run `python tools/memory-tree/gen_build_index.py --write`
   once the new spec is `git add`ed.
5. **Commit nothing.** Return the list of files you wrote; the main loop commits them.

### Acceptance

- `git grep -n 'template-size-limits' -- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-1.md`
  names no item, criterion or file the unit's own pass would write.
- `python tools/check-spec-tokens.py` reports nothing about the specs you touched, and
  `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your
  files staged through `GIT_INDEX_FILE`, names no finding in them.
- `bash tools/unattended/unattended.sh --plan dSafePassage --paths` lists TOOL-dSafePassage-61 READY and
  TOOL-dSafePassage-1 READY.

### Gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### Non-goals

- No product code, and no change to `tools/policy/guard.py` or to any dGroundRules file: widening the guard is TOOL-dGroundRules-13's, an owner-risk surface.
- No commit, no stage into the real index, no deviation record: the main loop writes those.
- No redesign of S7 or S8: the moved text keeps its design.

### Reuse

The round-1 to round-7 promotions in this build (for example `memory/builds/dSafePassage/prompts/2026-10-23-prompt-TOOL-dSafePassage-26-1-spec-writer.md`) for how a unit is added to the roster and its spec authored.
