# aGroundedOrientation - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: e62f6f32ddc0d102f3dba5dfdae64f763cbf90cf
phase: RUNNING
branch-sha: e62f6f32ddc0d102f3dba5dfdae64f763cbf90cf
branch-ref: refs/heads/branch/unattended-prompt-cg-toolkits-831d35
mode: prompt
anchor-kind: run-branch
keepalive: c25e22fa
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: b4e1d5be879bc8868529fb57c15657e271c39113
anchor-ref: refs/heads/main
base: e62f6f32ddc0d102f3dba5dfdae64f763cbf90cf

## Parked

2026-08-27T11:30:07Z review · item 2026-08-27-review-TOOL-aGroundedOrientation-1-spec-audit-round1 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-08-27T12:00:49Z rescope · item add TOOL-aGroundedOrientation-1 · reason The generated units region at the pinned BASE e62f6f32 held only TOOL-aGroundedOrientation-3, because units 1 and 2 had no spec yet and that region is RENDERED from specs. The authored roster table named all three from the first commit. Their specs were authored after preflight, so the region caught up and the driver correctly saw the executed roster grow. This is the defect this build exists to fix, occurring to the build itself: had orientation run its probes before step 3, all three specs would have existed at BASE.

2026-08-27T12:00:56Z rescope · item add TOOL-aGroundedOrientation-2 · reason The generated units region at the pinned BASE e62f6f32 held only TOOL-aGroundedOrientation-3, because units 1 and 2 had no spec yet and that region is RENDERED from specs. The authored roster table named all three from the first commit. Their specs were authored after preflight, so the region caught up and the driver correctly saw the executed roster grow. This is the defect this build exists to fix, occurring to the build itself: had orientation run its probes before step 3, all three specs would have existed at BASE.
