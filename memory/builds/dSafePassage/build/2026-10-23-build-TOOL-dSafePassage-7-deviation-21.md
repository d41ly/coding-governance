# TOOL-dSafePassage-7 deviation 21 — the release-0 half of the needs-target check is observed by the upgrade-walk leg

**Serves:** deviation TOOL-dSafePassage-7

- **Departs from:** `dSafePassage` [roster]
- **Hand-off:** design-to-spec
- **Before:** the roster's row 7, TOOL-dSafePassage-7 carrying `cl-dClosedLoop-0024@7817c7d0` whole, its own acceptance observing the whole clause, the needs-target check run over each release-0 step among it
- **After:** TOOL-dSafePassage-7 carrying `cl-dClosedLoop-0024@7817c7d0` whole and observing the contract, both plants and the needs-target check on its own fixture steps, and TOOL-dSafePassage-5's `upgrade-walk` leg running that check over a scratch copy of the release-0 tree for every declared step (its S10, observed by its AC10)
- **Cause:** builder discovery
- **Reason:** The clause checks the needs-target field by running each release-0 step under the contract. The release-0 tree is TOOL-dSafePassage-5's, built at order 5, and one of the steps it walks is TOOL-dSafePassage-11's, at order 3, while this unit builds at order 2. So TOOL-dSafePassage-7 ships the contract, the plants and the check, and observes all of them on its own fixture steps; the upgrade-walk leg of TOOL-dSafePassage-5 runs the same check over the release-0 tree for every declared step. A second release-0 generator inside this unit would be two answers to one fixture. The clause's text stands, and the build observes it whole; what moves is which unit's acceptance observes its release-0 half. So this record departs from the build's roster, never from the clause, and is addressed to `dSafePassage` [roster] as dTrueNorth's roster records are, so the as-built view does not read it as amending `cl-dClosedLoop-0024`. Its follow-through is the ask under which the build run builds TOOL-dSafePassage-5 and its leg, `TOOL-dSafePassage-14`: no `new unit`, `gap` or `usage` names that follow-up (rung 3).
- **Evidence:** TOOL-dSafePassage-7 §8 F2 and its §3 Edges hands-off to TOOL-dSafePassage-5; TOOL-dSafePassage-5 S10; the spec brief's writer-group table (`memory/builds/dSafePassage/prompts/2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md:119-125`) and its S8 (`:100-102`)
- **Risk:** editorial
- **Approver:** author, the gov-spec-writer role of dSafePassage's spec run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-14
- **Caused-by:** TOOL-dSafePassage-5
