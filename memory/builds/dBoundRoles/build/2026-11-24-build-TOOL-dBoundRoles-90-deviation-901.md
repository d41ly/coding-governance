# TOOL-dBoundRoles-90 deviation 901 — a writing stage is spawned once, where TOOL-dBoundRoles-5 re-ran it

**Serves:** deviation TOOL-dBoundRoles-90

- **Departs from:** `TOOL-dBoundRoles-5@rev-6` [S6, S7, AC6, AC7]
- **Hand-off:** spec-to-code
- **Before:** S6 re-runs every single-call stage returning nothing, through `runWithRetries` in the two templates and inline around the unit harness's builder; S7 has the Skill and the verbs guide pass `retries` to each harness; AC6 has the builder's null re-run; AC7 refuses a malformed `retries` in the three harnesses. Deviation 53 of `TOOL-dBoundRoles-5` lists the wrapped stages as the build harness's spec commit, subject resolver, round record and disposal, and the review harness's checklist agent, resume probe and synthesis. And `TOOL-dBoundRoles-90@rev-1` S2 has `tools/workflows/unattended-build.js` written by the protocol parity script's `--render`.
- **After:** (1) In the build harness the subject resolver alone is wrapped; the spec commit, the round record and the disposal are each one `agent()` call, and a null meets the stop each already has. The review harness's wrapped stages are unchanged. (2) `tools/workflows/unattended-unit.js` spawns its builder once and reads no `retries`; a key passed to it is undeclared and ignored, so the malformed-count refusal of AC7 stands in the build and the review harness only. (3) `dispatch.args` carries no `retries`; the audit's review call still does. (4) The verbs guide, the build Skill, `tools/workflows/README.md` and `help/roles.md` give `retries` to the build and the review harness only. (5) The suite's builder rows of AC6 and the unit harness's refusal rows of AC7 are replaced by the `DBR90` group, and the declared stage set it holds is the list that stands in place of deviation 53's. (6) The render was written by a scratch program that fills the template's tokens, first shown to reproduce the committed render from the committed template, since the renderer is a mode of a suite file this pass may not run.
- **Cause:** review finding
- **Reason:** an agent that wrote and then died returns nothing, and a second spawn repeats its write; the closing diff review's H4, resolved by F1 and F2 of this unit's spec. The CLOSED spec and deviation 53 stay as they are, under the main loop's decision `memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-58-1-main-loop-decision.md`.
- **Evidence:** the acceptance ledger `memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-90-1-acceptance-ledger.md`.
- **Risk:** stricter
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value; reported by the `report` value
- **Follow-through:** none
- **Caused-by:** TOOL-dBoundRoles-5
