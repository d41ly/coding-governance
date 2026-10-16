# Revision — dRedressedBar: TOOL-dRedressedBar-20 rev-2 and TOOL-dRedressedBar-7, F1 resolved as (b)

**Serves:** research TOOL-dRedressedBar-20 TOOL-dRedressedBar-7

## The brief

### Goal
The owner resolved unit 20's §8 F1 as option (b), 2026-10-14. The carrier-writer defect already rewrote a second fixture, `tools/playbook/render_playbook.py:1397`, from `v3.5` to `v1.28` over three earlier landings (`166bfcd78` wrote it as v3.5; landing merges and the mint in `ed1e9db3c` moved it). Restore it to `v3.5` in this build, and mint playbook-render to 1.29 for the bytes that restore moves. Revise both affected specs, each with a rev bump and a §9 line:
1. **Spec 20** to rev-2: mark F1 `RESOLVED (owner, 2026-10-14): (b)` in place. Add a scope item restoring `render_playbook.py:1397` to `v3.5`, with an AC that observes it and a "Red when" for a fixture still reading v1.28. State that this moves playbook-render's shipped bytes and that unit 7's mint bumps it, so unit 20 itself bumps nothing. Its §3 Edges hand that bump to unit 7. Restoring v3.5 must keep the line's test passing (any major below 4 is an older template); say so and observe it.
2. **Spec 7** to rev-4: the mint now moves exactly FIVE kits: agent-cap, branch-reconcile, roles, unattended, and playbook-render 1.28 → 1.29. Playbook-render's render re-renders `AGENTS.md`, so the step's allowed-writes set includes it and whatever else that render writes. Name which kickoff-manifest watch or verify path that re-render touches, and whether AC6's re-stamp is then owed. Add the `consumes-from` detail that unit 20's restore is what moves playbook-render. The "stop if the mint moves another kit or writes another file" rule stands with the five-kit set.

### Items
1. The two revisions above. No other spec moves.

### Acceptance
`bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades units 20 and 7 READY. Spec 20's F1 carries the owner's mark, and spec 7's mint table lists five kits.

### Gates
`kit epoch` · `kit version markers` · `playbook parity` · `kickoff-manifest ratchet` · `memory hygiene`

### Non-goals
- No code.
- No merge to local main and no push without the owner's ask.
