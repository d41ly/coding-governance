# PLAY-dOrderedCharter-8 deviation 82 — the charter re-rendered, its map naming the card file at level 1

**Serves:** deviation PLAY-dOrderedCharter-8

- **Departs from:** `PLAY-dOrderedCharter-8@rev-3` [Design]
- **Hand-off:** spec-to-code
- **Before:** the files-touched estimate lists the card engine and its suite, the fixture, the scratch guard and its suite, the handoff, the shell envelope and the parity suite, the document registry and the instruction-units module, and no rendered charter.
- **After:** `AGENTS.md` is re-rendered with its provenance row in `.governance/instructions.lock`: the map section's level-1 line reads `.claude/orientation-card.md` where it read `no registered document`, and nothing else in the charter moved.
- **Cause:** builder discovery
- **Reason:** the card's `doc.orientation-card` registry row lands in the registry the charter's instruction map is rendered from, so the render gate would red a charter left at its old map line.
- **Evidence:** `render_playbook.py --render-scope charter` rewrote one line of `AGENTS.md` and the lock row's blob; `AGENTS.md` measures 23279 bytes against its 23161-byte size row, a warning under the warn posture, the same breach the charter carried before this pass.
- **Risk:** additive
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-8
