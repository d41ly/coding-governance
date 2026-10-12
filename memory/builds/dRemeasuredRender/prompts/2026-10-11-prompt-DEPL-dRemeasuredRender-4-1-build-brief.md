# Build brief — DEPL-dRemeasuredRender-4

**Serves:** journal DEPL-dRemeasuredRender-4

Built INLINE by the main loop, promoted from the closing diff review's round 1 and sequenced
DEPL-dRemeasuredRender-3 then DEPL-dRemeasuredRender-4, because both write `tools/govkit/govkit.py`
and `tools/govkit/selftest.py`. The main loop holds the review record and the code it names.

Build exactly what the unit's spec states. Each new behaviour arm is observed RED against
`bac1a4fb`'s `govkit.py` through the scratch runner the earlier govkit units used. No merge bar
and no full self-test inside the pass. Temporary files go to the session scratchpad.
