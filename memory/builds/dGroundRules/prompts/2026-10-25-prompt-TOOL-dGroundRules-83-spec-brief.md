**Serves:** research TOOL-dGroundRules-83

# Spec brief — TOOL-dGroundRules-83, the review-harness regenerate in an adopter target is denied by the agent-cap hook

## The prompt

At the close the main loop ran `python tools/govkit/selftest.py` in scratch clones at the run's base `3c2b69be4` and at `59f02fde9`. At the base it fails 6 distinct arms (inherited: the playbook seed preview, OC8 AC4 and OC13 AC4 in the roles adopter, and `[-5] D1` SHELL_EXEC_SITES). At `59f02fde9` it fails those and 47 more, every one in the `[-PV]` family. The first and causal one is:

> FAIL [-PV] F2 the introducing update runs the regenerate and it exits 0 in the same run — e-render/regenerate argv exited 2 and no declared outcome accepts that, so the receipt is not re-stamped. Its stderr ended: protocol-parity: the agent-cap hook does not admit the writer split: the agent-cap hook exited 2 with no reason. Update it: govkit update --kits agent-cap.

Every later `[-PV]` block (R2-*, R3-*, PIN, W3, W4, F1) then reds because block 1 did not finish clean. The logs are in the run's scratchpad as `govkit-head-59f02fde9.log` and `govkit-base-3c2b69be4.log`. This build changed the writer-split probe (TOOL-dGroundRules-18, -30, -34, -74), rule 7 (TOOL-dGroundRules-10, -21, -61, -73) and the hooks kit's settings expectations, so the regenerate's probe of the hook in a fresh adopter target is now denied.

## The brief

### Goal
Author `memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-83.md`, a Tier-1 micro-spec at order 30, status `DEFERRED`, in the shape `2026-10-25-spec-TOOL-dGroundRules-79.md` follows, that makes the review-harness regenerate succeed in the govkit selftest's `[-PV]` adopter target again. Author only: no product code, no commit, no gate beyond memory hygiene.

### Items
1. Diagnose first, by reading and by probes (never the selftest suite itself): build the `[-PV]` target the way `tools/govkit/selftest.py` builds it (copy its setup into a scratch script under the scratchpad), run the review-harness regenerate argv in it, and run the agent-cap hook on the writer-split probe payload the protocol-parity render sends. Name which agent-cap rule denies it and why its reason is empty, and which commit of this build introduced the denial (bisect over the build's commits that touch `tools/hooks/agent-cap.js`, `tools/workflows/check-protocol-parity.test.sh`'s render path and the render script).
2. Decide, with the evidence, whether the defect is in the product (an adopter's regenerate is denied, which every adopter would hit) or in the fixture (the target lacks something a real adopter install always has). Spec the fix on the side the evidence names; if both, spec the product fix and say why the fixture needs nothing. The empty denial reason is a defect on its own (a hook denial always names its rule): spec it too if it is this build's.
3. Each acceptance criterion is a probe the pass may run (the scratch `[-PV]` target and the regenerate argv, a direct hook call), never the govkit selftest or the bar, and carries `Red when:` with a staged break that reds it by name. The close's main loop runs the govkit selftest and confirms the 47 `[-PV]` arms go green while the 6 inherited ones stay as they were.
4. §6 names the legs the touched files owe through `derive_guarded_legs`, plus any unguarded leg that reads them; adjust a floor or a pinned count only where the change moves it, and say which.
5. §7 "Open questions" reads exactly `none`, with no bullet under it; any follow-up goes in the §8 revision log as prose. No line anywhere in §5 starts at column 0 with `AC<n>` other than the bullets themselves; every AC bullet carries `Red when:`; keep every acceptance code span on one line and free of a `|` the bar pattern reads as a pipe; no retirement word in §2; an untracked path sits in a fenced block; never write a probe copy of a spec inside the spec folder.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); hygiene check 12 names nothing in this spec.

### Gates
Memory hygiene only.

### Non-goals
Any other spec; the six inherited govkit failures; units already built except where the diagnosis names their code as the cause.

### Limitations
Measured by the main loop; the selftest takes about an hour, so the spec's criteria must not need it.

### Reuse
The selftest's own `[-PV]` target builder, and the hook's existing denial-reason paths.
