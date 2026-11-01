# TOOL-dTotalRecall-23 deviation 231 — the row read adopted by the memory legs' per-record walks, not by the hygiene leg's bash checks

**Serves:** deviation TOOL-dTotalRecall-23

- **Departs from:** `cl-dClosedLoop-0234@eb7b1784`
- **Hand-off:** design-to-spec
- **Before:** the clause has "the memory legs reading the index's rows for unchanged blobs and re-parsing only changed ones", and the night pass two gives the cause as the memory legs re-reading the whole tree on every run, 83 s at 54 MB (night-pass-two.md:228-230).
- **After:** the memory legs' per-record walks in Python reading the index's rows for unchanged blobs and re-parsing only changed ones, through the `leg_row` table, its readers and `read_rows_at`: they are `corpus_ids.walk` (run twice per hygiene run, in `corpus_ids.py --check` and in `gotchas.py --check`), `read_bindings`, `gen_build_index.py`'s spec-header read and the recall leg's served build, while the hygiene leg's own bash checks, and the path matching in `gotchas.py`'s `selectable`, keep reading text, each able to join later by adding a reader to `LEG_READERS`, an index read and a full read agreeing on a planted tree (the night pass two, point 3, the owner's NT-15)
- **Cause:** design defect
- **Reason:** the design assumed the legs' cost was per-file parsing. A timing probe at the spec run shows otherwise. Of the hygiene leg's 174.8 s, about 113 s is in its bash checks, which grep and scan text with no parse product a row can hold. The slowest Python engine, `gotchas.py`, spends most of its time outside the shared walk in path matching, which is CPU work and not a parse. Turning the bash checks into row readers would rewrite a 3,376-line leg, which is a separate adopter unit by BUILD-METHOD M2. The two `corpus_ids.walk` runs, 15.7 s and 17.9 s, are the per-blob parse the clause describes, and they are adopted.
- **Evidence:** TOOL-dTotalRecall-23 §8 F4, the probe and its observation (node d, 2026-10-26, a clone of the run branch at `fb872a37e`); `tools/memory-tree/check-memory-hygiene.sh` (3,376 lines, delegating to Python at `:1268`, `:1674`, `:2912`, `:2932`, `:2949`); `tools/memory-tree/corpus_ids.py:494`; TOOL-dTotalRecall-23 §3.
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer role of this spec run's writer group 4, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** amends cl-dClosedLoop-0234@eb7b1784
- **Caused-by:** PLAY-dClosedLoop-2
