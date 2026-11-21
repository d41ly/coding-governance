# TOOL-dPlacedRequest-99 deviation 734 — the closing review's NON-CONVERGENT exit or the spec audit after it promoted a unit

**Serves:** deviation TOOL-dPlacedRequest-99

- **Departs from:** dPlacedRequest [roster]
- **Hand-off:** design-to-spec
- **Before:** dPlacedRequest's roster carries the units the build run started with and those its earlier reviews promoted.
- **After:** the roster also carries `TOOL-dPlacedRequest-99`, specced at `memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md` and built by this run.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit to a unit whose mechanism closes it; this run is the build run, so it built the unit rather than carrying it forward.
- **Evidence:** the rescope add row for `TOOL-dPlacedRequest-99` in `memory/builds/dPlacedRequest/RUN.md`; the unit's spec, `memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dPlacedRequest-99
- **Caused-by:** PLAY-dClosedLoop-2
