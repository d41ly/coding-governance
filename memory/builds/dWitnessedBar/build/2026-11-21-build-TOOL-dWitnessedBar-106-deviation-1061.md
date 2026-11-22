# TOOL-dWitnessedBar-106 deviation 1061 — the IR AC11 arm's cut of the hook's R-scoped read gains the floor's functions and orders

**Serves:** deviation TOOL-dWitnessedBar-106

- **Departs from:** `TOOL-dWitnessedBar-106@rev-1 [S6]`
- **Hand-off:** spec-to-code
- **Before:** S6 and §4 "The arms" name the new arms and their floor harness, which cuts `read_policy_key`, `scan_policy_bytes`, `derive_strictest` and `read_policy_at` by awk range and takes the column-0 orders and `PP_POLICY_REL` by grep; they say nothing of TOOL-dWitnessedBar-3's IR AC11 arm, whose `_ir_fns` cut `resolve_python`, `resolve_kit_dir`, `read_policy_key` and `read_policy_at` alone.
- **After:** the suite cuts the R-scoped read once, as `_pp_read_fns` (the four functions by awk range and the orders and path by grep), beside the IR AC11 arm; that arm's `_ir_fns` is its `resolve_python` and `resolve_kit_dir` cut followed by `_pp_read_fns`, and the floor harness's `run_floor_read` evals the same `_pp_read_fns`. No expected value of the IR AC11 arm moves.
- **Cause:** builder discovery
- **Reason:** after S3, `read_policy_at` calls `derive_strictest` and `scan_policy_bytes` and reads the orders, so the unchanged `_ir_fns` cut would define neither and the IR AC11 arm would read an empty `PP_POLICY`; one shared cut, rather than a second copy of the four ranges, is the charter's `[reuse]` at the kind's second instance.
- **Evidence:** a probe evaluating the composed `_ir_fns` in a subshell over this repository at `8e5bf6088` printed `own-mixed-contended 10`, the value `python tools/policy/policy.py get verdict.blocks --rev HEAD` printed and the bound `.githooks/gate-env.sh` declares (DERIVED from the builder's probe, 2026-11-21).
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** none
- **Caused-by:** TOOL-dWitnessedBar-106
