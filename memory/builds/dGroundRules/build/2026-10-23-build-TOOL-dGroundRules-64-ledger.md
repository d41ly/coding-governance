# TOOL-dGroundRules-64 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-64

The unit writes no code: each criterion runs a literal of its spec's §4 whole, on the built units 5,
21, 33 and 34 at `0a08a6904`, from the repository root. No merge bar, gate leg or self-test suite ran
in this pass. `COPY` was `git clone -q . %TEMP%/p64`, removed after; each staged break in it was
restored with `git -C <copy> checkout` before the next. The install-day target of AC4 was built in
process by `build_install_target` and the deployer's `apply`, as unit 34's AC20 probe built it, and
removed after. This unit declares no `New arm:` line, so the close owes no red-first observation for it.

**Evidences:** TOOL-dGroundRules-64
- AC1 — `MIRROR_CHECK` — printed `policy: mirror fresh`, exit 0; `POLICY_BLOB_WHOLE` exited 0 printing `43fa1bb1dbe35b80a185cc5c1c452285b74086c0`, and `MIRROR_POLICY_BLOB` printed the same id. Red case: `POLICY_BLOB_CUT` exited 128, git answering `path 'policy.toml' does not exist in 'HEAD'`.
- AC2 — `POLICY_SHOW_WHOLE` — exited 0, and `cmp` of its bytes against what `SCAFFOLD_BYTES` printed found them equal; `MIRROR_ATTR_WHOLE` printed `.governance/policy.json: eol: lf`. Red case: `POLICY_SHOW_CUT` exited 128 and `MIRROR_ATTR_CUT` printed `policy.json: eol: unspecified`.
- AC3 — `FRESH_TARGET` — with nothing staged in the copy it exited 0, printing `211 assertion(s) executed · 0 wrong` and no `WRONG` line. With `GUARD_OUT_SELFTEST` staged it exited 1, printing `TRACE_WRONG` (`policy-fixture: guard-trace · WRONG tools/govkit/selftest.py · not under the policy fixtures guard`) and `210 assertion(s) executed · 1 wrong`. Red case: with `GUARD_OUT_OTHER` staged instead, its one `WRONG` line named `tools/govkit/registry.toml` and nothing of the deployer's selftest. This is the observation unit 33's ledger left owed for AC4 under `--fixture`: the case opens the deployer's selftest in process through `read_deploy_answers`, with no staged `open()`.
- AC4 — `SCAFFOLD_TARGET` — with `POLICY_BEFORE_SCAFFOLD` planted over the install's own policy file (the scaffold's text with `budgets.enforce = "bogus"` and `[policy-file] on-invalid = "refuse"`) and the install staged, it exited 2, printing `... is invalid, so the mirror is not deferred; fix it, then re-run --scaffold`, then `policy-check: arm_schema · 1 finding(s)` and `budgets.enforce: "bogus" is not one of ["warn", "refuse"]`, and no `mirror deferred`. Red case: with `POLICY_TOP_PLANT` instead it exited 0 printing `adopt-policy: mirror deferred · .governance/policy.toml has uncommitted changes`; the valid file it deferred on was the one the install had written, which the scaffold printed as `kept`, so the criterion's red holds while its clause "writes its own valid file" reads the install's file as the scaffold's.
- AC5 — `ANSWERS_PROBE` — with nothing staged after `COPY` it exited 0 printing `['manifest_path', 'memory_root', 'playbook_dir', 'playbook_path', 'user_skills']`. With `DEPLOY_FULL_OUT` staged (one line renamed) it exited 1, its last stderr line `ANSWERS_ERROR`: `RuntimeError: no [answers] table of DEPLOY_FULL to install with in <%TEMP%>/p64/tools/govkit/selftest.py`, `<%TEMP%>` the host's temp directory spelled with forward slashes. Red case: `DEPLOY_FULL_OUT_OTHER` renamed no line of the runlog kit's selftest.py, and the probe exited 0 printing the same five keys.
- AC6 — `EVIDENCE_README` — printed two lines, `165:<!-- gen:build-order -->` and `179:<!-- /gen:build-order -->`. Red case: `EVIDENCE_ROOT_CUT` printed `0`.
