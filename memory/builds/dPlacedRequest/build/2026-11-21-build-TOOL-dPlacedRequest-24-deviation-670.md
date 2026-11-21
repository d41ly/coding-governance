# TOOL-dPlacedRequest-24 deviation 670 — TOOL-dPlacedRequest-24@rev-8 revised after its first pass or its audited revision

**Serves:** deviation TOOL-dPlacedRequest-24

- **Departs from:** `TOOL-dPlacedRequest-24@rev-8`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dPlacedRequest-24`'s spec as its first pass or its newest spec audit read it.
- **After:** the spec as `3e87e4ccb` left it, the revision the report addresses as `TOOL-dPlacedRequest-24@rev-8`.
- **Cause:** builder discovery
- **Reason:** the revision's commit reads: fix(dPlacedRequest): the stops guide pins the queue lock's wait, and spec 24's revision line stops reading as a figure. The departures report places it not an ancestor of its first pass 527d68430.
- **Evidence:** commit `3e87e4ccb`; the spec, `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-24.md`; the departures report of this close.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role whose handoff the revision's commit carries, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage spec-revised
- **Caused-by:** PLAY-dClosedLoop-2
