# TOOL-dQuietDisk-5 deviation 1 — the new arm builds its own guarded fixture beside section 3h's

**Serves:** deviation TOOL-dQuietDisk-5

- **Departs from:** `TOOL-dQuietDisk-5@rev-3` [Gates]
- **Hand-off:** spec-to-code
- **Before:** the `New arm:` line of section 7 says section 3h's guarded fixture gains a plain directory guard, a near-miss path, a glob guard, a planted failing diff and a last-run record whose sha equals the base.
- **After:** `tools/run-gates/run-gates.test.sh` arm 3h1 builds a second guarded fixture, `$SCRATCH/guarded-moved`, laid out as 3h's `$SCRATCH/guarded` is, right after 3h's own cases. It holds a `ga/` leg, a `fx/*.sh` leg and a kit-subject `hk/` leg. It runs the near-miss path `xga/f`, the moved `ga/f` and `fx/a.sh`, a blob named as `GATE_BASE` for the failing diff, and a held record seeded at the HEAD that `GATE_BASE=HEAD` then names. 3h's own fixture keeps its three legs.
- **Cause:** builder discovery
- **Reason:** arm 3i runs 3h's fixture under `GATE_FULL=1` and expects `3/3 legs passed`, so adding legs to that fixture would red 3i without changing anything 3i is meant to check. The cases and the breaks they catch are the ones the `New arm:` line names.
- **Evidence:** `grep -n '"\$G' tools/run-gates/run-gates.test.sh` at this pass shows arm 3i's run over `$G` with the `3/3 legs passed` pattern (PINNED, this pass, 2026-11-22).
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value
- **Follow-through:** ask TOOL-dQuietDisk-5
- **Caused-by:** TOOL-dQuietDisk-5
