# DEPL-dShippedRelease-14 deviation 141 — the landing review runs the diff kind's default lenses, because `review.pin` has no landing preset to pass

**Serves:** deviation DEPL-dShippedRelease-14

- **Departs from:** `cl-dClosedLoop-0424@efed0e2f` [review.pin]
- **Hand-off:** design-to-spec
- **Before:** run until dCalibratedLens's Deploy lenses land with the lenses of the preset `review.pin` passes from dFairHearing's catalogue
- **After:** the landing review blocking the build's close rather than the push, run until dCalibratedLens's Deploy lenses land with the lenses `review.pin`'s landing pin selects from dFairHearing's catalogue, the diff kind's default lenses, no `preset` argument passed since `preset` is refused on a `diff-review`, seen on a tree that holds no Deploy lens
- **Cause:** design defect
- **Reason:** The clause assumes a preset exists for a landing. TOOL-dFairHearing-3 S8 maps spec and design subjects only, TOOL-dFairHearing-2 refuses `preset` on `diff-review`, and the landing's subject is a diff, because `KINDS` holds two kinds and a landing is no spec. So there is no preset to pass. The clause's intent, that the landing review runs on the catalogue's lenses before the Deploy lenses exist, is kept: `DIFF_LENSES` are that catalogue's rows (TOOL-dFairHearing-13), and the pin prints `diff defaults · no Deploy lens`. Adding a `landing` literal to `PRESETS` would be a parent's surface with no lens to hold. Also follows through as: gap gap-deploy-06.
- **Evidence:** `tools/workflows/tier2-review.template.js:190`; `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-3.md` S8; `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-2.md` S1 and AC1; scout A disagreement 12, `memory/builds/dShippedRelease/build/2026-10-30-build-DEPL-dShippedRelease-1-reuse-scout-a.md:109-113`; DEPL-dShippedRelease-14 §8 F2
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer role of dShippedRelease's spec run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); carried for the owner's walk unless it rules otherwise
- **Follow-through:** amends cl-dClosedLoop-0424@efed0e2f
- **Caused-by:** DEPL-dShippedRelease-14
