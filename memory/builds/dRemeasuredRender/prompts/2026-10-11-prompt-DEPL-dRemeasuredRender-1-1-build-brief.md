# Build brief — DEPL-dRemeasuredRender-1

**Serves:** journal DEPL-dRemeasuredRender-1

Built INLINE by the main loop, sequenced after `TOOL-dRemeasuredRender-1` and before
`DEPL-dRemeasuredRender-2`, because both govkit units write `tools/govkit/govkit.py` and
`tools/govkit/selftest.py`. The main loop has already read `_cmd_update`'s regenerate loop, its
verify pass and both receipt writers.

Build exactly what the unit's spec states. Write the self-test arms first and observe each RED
against base `17472e21`'s `govkit.py`, through a scratch runner that loads the self-test module
and points it at that copy. No merge bar and no full self-test inside the pass; the `govkit
selftest` leg runs once, at the close. Temporary files go to the session scratchpad.
