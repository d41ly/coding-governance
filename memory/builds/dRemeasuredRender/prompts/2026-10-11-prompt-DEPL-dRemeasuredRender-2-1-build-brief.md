# Build brief — DEPL-dRemeasuredRender-2

**Serves:** journal DEPL-dRemeasuredRender-2

Built INLINE by the main loop, after `DEPL-dRemeasuredRender-1`, because both write
`tools/govkit/govkit.py` and `tools/govkit/selftest.py`. The main loop has already read
`run_hole_probes`, the regenerate loop's early probe and the `[aHI-1 S3]` arm that asserts its line.

Build exactly what the unit's spec states. Write the two self-test arms first and observe each RED
against base `17472e21`'s `govkit.py` through the same scratch runner unit 2 used. No merge bar and
no full self-test inside the pass. Temporary files go to the session scratchpad.
