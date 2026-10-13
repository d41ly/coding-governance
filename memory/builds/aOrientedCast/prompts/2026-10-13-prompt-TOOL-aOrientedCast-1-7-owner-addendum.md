**Serves:** research TOOL-aOrientedCast-23 TOOL-aOrientedCast-25

# The owner's fourth addendum — term 4 reworded, and two effort levels changed

Two rulings sent by the owner in this build's session on 2026-10-13, after TOOL-aOrientedCast-23 was
ratified and while it was building. Verbatim, in order:

```text
(a) Reword term 4 so the run records the row "before or with the raise".
```

```text
let's bring another small change into this build. Change efforts: spec-writers should write at HIGH effort, gov-builders should write code at xhigh effort.
```

## How the run reads them

- **The first** answers the decision parked in `RUN.md`: term 4 of the size-limits rule that
  TOOL-aOrientedCast-23 writes said the raising unit's "same commit adds that unit's row to
  memory/DECISIONS.md", which a pass may not do. It becomes: the run records that unit's row in
  `memory/DECISIONS.md` before or with the raise. TOOL-aOrientedCast-23's spec takes it as a fold,
  and a second pass of that unit changes the one line.
- **The second** moves two values of the seeded policy file `tools/roles/house/policy.toml`:
  `gov-spec-writer` from `xhigh` to `high`, and `gov-builder` from `high` to `xhigh`. The file is
  under `tools/`, so the change is a builder's, folded into TOOL-aOrientedCast-25, the build's last
  roles unit. Its second pass re-renders the agent types. Until it lands, the main loop passes these
  two levels explicitly in every harness call's `efforts`, which wins over an agent type's level.
