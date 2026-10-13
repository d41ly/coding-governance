**Serves:** research TOOL-aOrientedCast-27

# The owner's sixth addendum — every workflow run says what it is and what it is doing

Sent by the owner in this build's session on 2026-10-13, while TOOL-aOrientedCast-24 was building.
Verbatim:

```text
another addition to the build - 'unattended-unit' workflows carry only their generic workflow names and description (Builds exactly ONE unit...) with no pointers to the build slug or unit id. More information needs to be included with each started agent/workflow to clearly indicate what they're and what they're doing to the owner. In addition, these workflows launch just a single agent - wouldn't it be better to launch these agents separately, outside the workflow? Or is there an advantage running them as a workflow?
```

## How the run reads it

- **What the tool allows.** A `Workflow` run's title and description are its script's `meta` block,
  which must be a pure literal; the tool ignores a `title` or `description` passed at call time. A
  run cannot be renamed per call. It can announce itself: its first log line, which `/workflows`
  shows, its agents' labels, and the first line of its return.
- **The addition joins TOOL-aOrientedCast-27** as a fold: each harness logs
  `<slug> · <unit-or-scope> · <action>` as its first line and leads its return with the same, beside
  the agent labels that unit already gives, and the roles README and help page say where the owner
  reads a run's identity.
- **The question was answered in the session, not asked back.** Keep the single-agent harness. It
  sets per-stage effort, which the `Agent` tool cannot; its agents do not count against the
  per-prompt-turn direct-spawn budget an unattended run cannot reset; its journal is what
  `handoff.py agents --run` derives the agent lines and ledger from; it validates the builder's
  return against a schema; and a run resumes by id with cached results.

## The follow-up, the same day, verbatim

```text
In light of what you've just claimed, shouldn't spec writer agents run in a workflow as well? They've been running as individual agents this session.
```

Yes. The harness spec stage authored this build's new specs twice, but every fold and several new
specs ran as direct spawns: the spec stage authors only MISSING specs, so a rev bump has no harness
route, and the main loop stopped routing new specs through the harness after its commit stage
refused once on the main loop's own uncommitted ledger line. Those spawns ran at the agent type's
effort rather than the owner's new level, counted against the direct-spawn budget, and returned free
text. Adopted as TOOL-aOrientedCast-28: the build harness gains a FOLD stage that rev-bumps an
existing spec as a typed, effort-set, journalled spec-writer agent, and the spawn guard then refuses
a direct `gov-spec-writer` spawn from a session holding a live run's lease.
