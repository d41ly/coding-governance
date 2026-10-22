# TOOL-dSafePassage-7 deviation 21 — the release-0 half of the needs-target check is observed by the upgrade-walk leg

**Serves:** deviation TOOL-dSafePassage-7

- **Departs from:** `cl-dClosedLoop-0024@7817c7d0` [acceptance]
- **Hand-off:** design-to-spec
- **Before:** the step kind's isolation contract, which every caller inherits: each step run from a declared working directory with a scrubbed environment, Python's `-I`, `core.hooksPath` pointed at an empty directory through `GIT_CONFIG_COUNT` and no ambient credential, and its field for the target's code checked by running each release-0 step under that contract beside a planted target hook and a planted target module, each seen not to run, so a step that needs target code fails there and is marked attended (the shape audit)
- **After:** the step kind's isolation contract, which every caller inherits: each step run from a declared working directory with a scrubbed environment, Python's `-I`, `core.hooksPath` pointed at an empty directory through `GIT_CONFIG_COUNT` and no ambient credential, and its field for the target's code checked by running each release-0 step under that contract beside a planted target hook and a planted target module, each seen not to run, so a step that needs target code fails there and is marked attended (the shape audit)
- **Cause:** builder discovery
- **Reason:** The clause checks the needs-target field by running each release-0 step under the contract. The release-0 tree is TOOL-dSafePassage-5's, built at order 5, and one of the steps it walks is TOOL-dSafePassage-11's, at order 3, while this unit builds at order 2. So TOOL-dSafePassage-7 ships the contract, the plants and the check, and observes all of them on its own fixture steps; the upgrade-walk leg of TOOL-dSafePassage-5 runs the same check over the release-0 tree for every declared step. A second release-0 generator inside this unit would be two answers to one fixture. The clause's text stands, and the build observes it whole; what moves is which unit's acceptance observes its release-0 half.
- **Evidence:** TOOL-dSafePassage-7 §8 F2 and its §3 Edges hands-off to TOOL-dSafePassage-5; the spec brief's writer-group table (`memory/builds/dSafePassage/prompts/2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md:119-125`) and its S8 (`:100-102`)
- **Risk:** editorial
- **Approver:** author, the gov-spec-writer role of dSafePassage's spec run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** amends cl-dClosedLoop-0024@7817c7d0
- **Caused-by:** TOOL-dSafePassage-5
