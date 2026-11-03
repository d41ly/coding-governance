# PLAY-dOrderedCharter-22 deviation 222 — the tag resolver's `schema` arm row stops spelling the index schema

**Serves:** deviation PLAY-dOrderedCharter-22

- **Departs from:** `PLAY-dOrderedCharter-22@rev-3 [§4 Files touched]`
- **Hand-off:** spec-to-code
- **Before:** the `schema` row of the tag resolver's arms in `tools/playbook/adopt-playbook.sh`, landed by PLAY-dOrderedCharter-44, asserts `tag-index — rebuilt: schema 0 to 1`, a second copy of `tag_index.INDEX_SCHEMA`; this unit's §4 names the file for its own plants' rows only.
- **After:** the row asserts `tag-index — rebuilt: schema 0 to` and nothing after, so the plant's own `stamp == ti.INDEX_SCHEMA` comparison is the one reading of the schema number; the plant printed the line with exit 0 at this pass.
- **Cause:** builder discovery
- **Reason:** a fact stated in two places drifts (class two-answers-to-one-question); unit 44's builder return names the row as owed and the write gate refused its edit after that unit's CLOSED flip, so this unit's brief owes it in the pass that next writes the file.
- **Evidence:** `memory/builds/dOrderedCharter/build/2026-11-03-build-PLAY-dOrderedCharter-44-1-builder-return.md:15`; `tools/playbook/tag_index.py`'s `INDEX_SCHEMA = 1`; `tools/playbook/gov_tag.py`'s `schema` plant returns 0 only on `stamp == ti.INDEX_SCHEMA`.
- **Risk:** editorial
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `report` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-44
