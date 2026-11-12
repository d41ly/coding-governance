**Serves:** research PLAY-dOrderedCharter-74

# Brief: unit 74 — the two code reds the second bar left

## The prompt

> merge this branch to remote as well

— owner, 2026-11-05. The second full bar at VERIFYING left two reds in this build's own code.

## The brief

### Goal

Write unit 74's micro-spec, so the remote-literal and leg-ceiling legs go green over this tree.

### Items

1. **Remote literals.** `tools/playbook/instruction_units.py#DERIVED_UNIT_KEYS` is `("status", "origin")`. The ban's third shape reads a
   quoted remote name as the last element of a tuple opened after `(`, and `origin` is a unit-row field name here. Reorder the tuple so the
   name is not its last element, after checking that no reader depends on its order. Do not touch the checker.
2. **Leg ceilings.** `tools/gate-legs.json`'s `layer dependencies (the core never depends on an expansion)` row has a ceiling of 120s. The
   evidence check requires it to clear the 3.6s evidenced maximum by max(120s, 1.0x), so it is 4s short. Raise it to the smallest value the
   check accepts, read from `tools/run-gates/derive-ceilings.py`'s own rule, and say the figure.
3. **The watch list.** `tools/gate-legs.json` is on the kickoff manifest's watch list, so `memory/guides/SESSION-KICKOFF.md` joins Files
   touched for its stamp.

In the spec:

- A Tier-1 micro-spec by `memory/TEMPLATE-SPEC.md`, at `memory/builds/dOrderedCharter/spec/2026-11-08-spec-PLAY-dOrderedCharter-74.md`.
- Status `DEFERRED`, rev-1, dated 2026-11-08, base `fc2572d5d`, streams playbook, `order 17`, advancing PLAY-dOrderedCharter-38, and
  `**Derived:** PLAY-dClosedLoop-2` after the status header.
- New text cites code as `path#symbol`, outside the acceptance bullets, which spell plain tracked paths. New text names a section in words.
- Stage it, then run the hygiene spec checks (`--only 12,25`).

### Acceptance

- The micro-spec exists, names both fixes and their files, and an acceptance line per leg.

### Gates

Memory hygiene, as your role runs it.

### Non-goals

- No code. No edit to another spec. No change to either checker.
