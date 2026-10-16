# Revision — dRedressedBar: TOOL-dRedressedBar-19 rev-2 and the spec 10 H1, for two hygiene refusals

**Serves:** research TOOL-dRedressedBar-19 TOOL-dRedressedBar-10

## The brief

### Goal
The pre-commit gate refused the commit holding round 4's promotion on two checks. Fix both in spec
text, with nothing else moving.
- **HYGIENE check 12** on `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-19.md`:
  "acceptance bullets naming no failure mode, required at/after SPEC_FAILURE_MODE_CUTOFF 2026-09-08:
  AC10". Give AC10 its failure mode in the form `memory/TEMPLATE-SPEC.md` states, the `Red when:`
  line its siblings carry. Bump spec 19 to rev-2 with a §9 line.
- **HYGIENE check 7** on `memory/builds/dRedressedBar/README.md:134` (370 chars > 350): the index row
  the generator renders from spec 10's H1 is over the cap. Shorten spec 10's H1 title so the rendered
  row fits, keeping its meaning. Bump spec 10's rev with a §9 line naming the shortened title.

### Items
1. The two revisions above. Edit no other spec, and leave the README, which is generated.

### Acceptance
With both specs staged and `python -B tools/memory-tree/gen_build_index.py --write` re-run,
`bash tools/memory-tree/check-memory-hygiene.sh --staged` prints no check 7 and no check 12 line.

### Gates
`memory hygiene`

### Non-goals
- No code. No edit to any other spec.
