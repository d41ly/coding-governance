**Serves:** journal TOOL-aOrientedCast-24 TOOL-aOrientedCast-25

# Build brief — the second closing review's promotions

The build brief for the second addendum's units binds you, and through it the brief every earlier
unit of this build was handed:
`memory/builds/aOrientedCast/prompts/2026-10-13-prompt-TOOL-aOrientedCast-16-2-build-brief.md`. Read
both. This file adds two rules.

- **Never bypass a hook.** No `--no-verify`, no `-n`, no environment variable that disarms a hook,
  for any reason. When a hook refuses your commit, return `committed: false` with the refusal quoted
  in `why`, and the main loop decides. A refusal caused by a second pass the main loop owes, such as
  a rendered copy that still carries the old version, is still a refusal. TOOL-aOrientedCast-22's
  first pass bypassed one and left its commit's checks unrun; this rule is that finding's left-shift.
- **Two passes where a renderer moves.** A unit that changes a generator writes nothing the
  generator renders; the main loop re-renders in a second pass after your commit. If your commit
  cannot pass its hook without the rendered copy, that is the case above: return it uncommitted,
  naming the paths, and the main loop declares both halves together.
