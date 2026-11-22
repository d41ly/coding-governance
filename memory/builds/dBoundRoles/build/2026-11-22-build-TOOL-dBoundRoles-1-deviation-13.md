# TOOL-dBoundRoles-1 deviation 13 — the role factory's usage row declares the two new flags

**Serves:** deviation TOOL-dBoundRoles-1

- **Departs from:** `TOOL-dBoundRoles-1@rev-8 [§4 Files touched]`
- **Hand-off:** spec-to-code
- **Before:** §4 Files touched names `help/loop.md` for the role factory's usage line and no `tools/govkit/usage.toml`, whose `[[usage]]` row `script:{prefix}/loop/factories.py#role` declares that verb's flags.
- **After:** that row's `flags` gains `--layer=` and `--acts-as=`, and the `help/loop.md` anchor `script:tools/loop/factories.py#role` is re-pinned from `8825562a` to `50224b14`, the fingerprint `python tools/govkit/docs_leg.py --fingerprints` prints for the row after the edit; nothing else in either file moved.
- **Cause:** builder discovery
- **Reason:** the docs leg tests each inline `python` command a page under `help/` shows against the declared flags of its verb (`tools/govkit/docs_leg.py#ANCHOR_RE` and its THE COMMANDS paragraph), so the `help/loop.md` line §5 says gains `--layer` and `--acts-as` would name two flags the row does not declare, and the charter's `[docs]` rule holds the page current.
- **Evidence:** `tools/govkit/usage.toml` at the pass's base `85a3e2b4` declared the role verb's flags as `--workflow=` to `--ceiling=`, eight entries (DERIVED from the builder's read).
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** none
- **Caused-by:** TOOL-dBoundRoles-1
