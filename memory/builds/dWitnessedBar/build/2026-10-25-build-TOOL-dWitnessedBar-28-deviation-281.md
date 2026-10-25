# TOOL-dWitnessedBar-28 deviation 281 — a gov leg an adopter hand-edited before conversion stays on the legacy list until the owner drains it into a patch

**Serves:** deviation TOOL-dWitnessedBar-28

- **Departs from:** `cl-dClosedLoop-0366@a7d91105` [today's hand-added rows on the legacy list; a gov leg changed only by a pinned patch]
- **Hand-off:** design-to-spec
- **Before:** the shrink-only legacy list holds "today's hand-added rows", and a gov leg's arguments, guard and ceiling change only by a pinned patch
- **After:** a repository's legs from its overlay's leg rows through the leg factory, registered at Test's leg-pack point as the repository's pack and counted once each has its seen-red record, a manifest row with no source red, every target row no source produces at the first composed update, a hand-edited gov row included, kept on a shrink-only legacy list and landing as the adopter wrote it until the owner converts it into an `amends` patch and drains the entry, a gov leg's arguments, guard and ceiling changed by a pinned patch and dropped only through `instructions.exclude` while every other leg lands, the leg kind's fixed set declared, the canary's key set and the legs that check the composition, its open fields' widening directions declared, a ceiling widening as it rises, and leg tags joined to dSafePassage's step gate, each seen red on a planted unsourced row, a patch on a vanished leg, a dropped fixed leg, a patched fixed leg and a planted leg tag removed with no change record, green on one naming its successor (FA-1, FA-2, FA-5, the flow adoption's review; TOOL-dWitnessedBar-28 §2 S7, §8 F1)
- **Cause:** design defect
- **Reason:** Writing gov's row over a hand-edited one loses the coverage the emitter's drift refusal was written to protect (`tools/govkit/govkit.py:4487-4489`), and converting the edit into a patch would have the emitter write the guarded overlay, past the owner's proof. Holding it on the list keeps the edit, names it on every update, and lets the list only shrink.
- **Evidence:** TOOL-dWitnessedBar-28 §8 F1; gap-test-21; `tools/govkit/govkit.py:4486-4490`
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer role of the harness's spec stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** amends cl-dClosedLoop-0366@a7d91105
- **Caused-by:** TOOL-dWitnessedBar-28
