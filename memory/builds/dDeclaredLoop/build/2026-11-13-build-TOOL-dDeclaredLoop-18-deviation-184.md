# TOOL-dDeclaredLoop-18 deviation 184 — the namespace-word rule narrowed to names of two or more segments

**Serves:** deviation TOOL-dDeclaredLoop-18

- **Departs from:** `TOOL-dDeclaredLoop-18@rev-4`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-18`'s spec as the revision at `TOOL-dDeclaredLoop-18@rev-4` reads it, under the rule that a first segment may not be a namespace word.
- **After:** the spec at rev-5: §8 F8 resolved to (b), the rule narrowed in both twins to names of two or more segments, so `kind.command`, `kind.item` and `kit.policy` stay legal once `command`, `item` and `policy` are registered.
- **Cause:** builder divergence
- **Reason:** the third dispatch built rev-4 whole and found the three tags red on the live tree; a rename of the policy kit's id is an adopter-facing migration no unit of this build holds, and the clause names the four words.
- **Surface:** the tag grammar's namespace-word rule, in `tools/playbook/tag_index.py` and its twin in `tools/lexicon/lexicon.py`
- **Bound:** the systems record's sentence that a first segment may not be a namespace word, for one-segment names
- **Tier:** strongest, a rule the owner answered in person on 2026-10-19
- **Evidence:** the builder return `memory/builds/dDeclaredLoop/build/2026-11-13-build-TOOL-dDeclaredLoop-18-3-builder-return.md`, and the rev-5 line in this spec's §9.
- **Risk:** loosening
- **Approver:** the run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`) and the standing ruling ER:388; the owner reads it first in the departures report at the landing
- **Follow-through:** none
- **Caused-by:** 2026-11-13-build-TOOL-dDeclaredLoop-18-3-builder-return
