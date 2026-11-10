# PLAY-dOrderedCharter-77 deviation 772 — check 23 closes a span by a run as long as its opener

**Serves:** deviation PLAY-dOrderedCharter-77

- **Departs from:** `PLAY-dOrderedCharter-77@rev-2` [Design]
- **Hand-off:** spec-to-code
- **Before:** the sketch under "The tokenizer, sketched" joins a criterion bullet's lines and hands the joined text to check 23's `altoks` unchanged, which pairs single backticks.
- **After:** the spec side's `altoks` in `tools/memory-tree/check-memory-hygiene.sh` reads a span as Markdown does: it opens on a run of backticks and closes on the next run of the same length, an unclosed run is literal text, and a backtick inside a span becomes a space. The ledger side's extractor is unchanged.
- **Cause:** builder discovery
- **Reason:** read per line, a double-backtick span paired wrong only until the line ended; joined, the same mispairing shifts every later pair of the bullet, so the join alone would change verdicts AC16 says must hold. Pairing runs by length keeps each span one token over the joined text.
- **Evidence:** a Python replay of check 23's token join over every tracked CLOSED Tier-2 spec past `LEDGER_TOKEN_CUTOFF`, with the ledger map as the checker builds it, named `PLAY-dOrderedCharter-13/AC5` as the only verdict that moves between the per-line tokens and this pass's joined ones. The checker's own run, AC16, is the close's.
- **Risk:** loosening
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-77
