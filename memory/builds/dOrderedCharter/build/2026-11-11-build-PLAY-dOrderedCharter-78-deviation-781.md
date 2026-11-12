# PLAY-dOrderedCharter-78 deviation 781 — the scratch install's template arm reads the template beside the engine

**Serves:** deviation PLAY-dOrderedCharter-78

- **Departs from:** `PLAY-dOrderedCharter-78@rev-1` [Scope]
- **Hand-off:** spec-to-code
- **Before:** S2 changes shape 5 of `tools/govkit/matrix.py` at its install selection alone, and AC2 expects no line opening `FAIL scratch install:`.
- **After:** the shape's arm that asserted the charter template lands at the operator's `playbook_path` answer now asserts it lands beside the renderer's engine, at `<prefix>/playbook/coding-governance-agents.template.md`.
- **Cause:** builder discovery
- **Reason:** PLAY-dOrderedCharter-31 retired the `playbook` entry's seeded copy, so that entry lands no file and the `[[retired]]` row `playbook/seeded-template` carries an adopter's old copy; the arm would print `FAIL scratch install:` on every run once apply renders, and AC2 could not hold. The arm's claim, that the install lands the template the render reads, is unchanged.
- **Evidence:** `tools/govkit/entries/playbook.kit.toml` declares no `[[files]]` rule and `[adopt] argv = []`, and `tools/playbook/kit.toml` lands the template at `{prefix}/playbook/coding-governance-agents.template.md` (PINNED, read at 5403142e4).
- **Risk:** editorial
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-31
