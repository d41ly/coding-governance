# TOOL-dDeclaredLoop-66 deviation 663 — the sweep's positional count, read at this pass's base

**Serves:** deviation TOOL-dDeclaredLoop-66

- **Departs from:** `TOOL-dDeclaredLoop-66@rev-4` [§5]
- **Hand-off:** spec-to-code
- **Before:** the sweep's probe of `memory/project/positional-refs.txt`, read at the tip `adbc3ecf5`, counts 9 PINNED rows naming this spec.
- **After:** at this pass's base `74a6bc30f` the same probe counts 0 PINNED rows: the commit landing rev-4, `68dfc729b`, ran the positional shrink the sweep's row names, since rev-4 cites symbols and paths only.
- **Cause:** builder discovery
- **Reason:** the figure was read before the shrink the sweep itself owes; no design claim moved, and every other sweep figure held at the base.
- **Evidence:** `git log -S'spec-TOOL-dDeclaredLoop-66.md' -- memory/project/positional-refs.txt` names `68dfc729b` as the last commit to change that count.
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** PLAY-dClosedLoop-2
