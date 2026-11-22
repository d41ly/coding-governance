# TOOL-dBoundRoles-2 deviation 23 — help/roles.md names the never list, the return template and the rendered sections

**Serves:** deviation TOOL-dBoundRoles-2

- **Departs from:** `TOOL-dBoundRoles-2@rev-5 [§5]`
- **Hand-off:** spec-to-code
- **Before:** §5's user-docs line says no page under `help/` documents the role file grammar, and §4 Files touched names no `help/roles.md`.
- **After:** `help/roles.md` "How a task reaches an agent" step 2 names the `never` and `return` keys beside `mandatory` and `output`, and says the role text closes with `## Never`, `## Ceiling` and `## Return`; nothing else on the page moved.
- **Cause:** builder discovery
- **Reason:** that step already lists a role file's keys, `rules`, `mandatory` and `output`, so with the two new required keys and the three rendered sections it would describe a role file and an agent type short of what this unit ships, and the charter's `[docs]` rule holds a user-facing change undone until its page under `help/` is current.
- **Evidence:** `help/roles.md` step 2 of "How a task reaches an agent" at the pass's base `85a3f6e4` named `rules`, `mandatory` and `output` and no limit or return key. (DERIVED from the builder's read)
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** none
- **Caused-by:** TOOL-dBoundRoles-2
