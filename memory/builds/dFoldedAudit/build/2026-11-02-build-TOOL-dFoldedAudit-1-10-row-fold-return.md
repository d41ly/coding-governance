# dFoldedAudit — unit 1's decision-row fold return

**Serves:** journal TOOL-dFoldedAudit-1

`TOOL-dFoldedAudit-1` is authored at rev-6, with its status still INPROGRESS. I changed only the spec and committed nothing.

**Brief items**
1. **The ceiling:** term 4 (`tools/template-size-limits.txt:23`) is now met by "before". The row landed in its own `Pass: none` commit, written by the main loop. I confirmed that `memory/DECISIONS.md:243` matches §4's fence byte for byte, at 295 characters, and that `10b5814cf` carries it.
2. **Files touched:** `memory/DECISIONS.md` is marked as its own `Pass: none` records commit, already landed, and out of this pass's write set.
3. **Who writes the row:** S10 and §4 "The decision row" say the main loop wrote it and the builder writes nothing to that file.
4. **AC10:** unchanged, and the builder still observes it.
5. **AC7 and AC12:** each `--check` clause is marked "owed to the close". Each also carries a `permission:` line, the format's own field for an observation this run may not make. No other AC clause matches a leg's argv.

There is also a §9 entry for rev-6.

**Edits beyond the brief**
- **§7 leg line:** it gains `unattended skill wiring`. It was missing, and AC7's clause is now owed to that leg.
- **§5:** the security bullet no longer says the file takes a row in this pass, and the testing bullet names the two owed clauses.

**The write set is a marking, not a parser change:** `read_spec_writes` and `read_files_touched` still read the `memory/DECISIONS.md` token as declared, as they do for TOOL-dTrueNorth-27. The builder has to leave it out of `--writes` by hand, and the marking tells them to.

**Gates I ran**
- **Memory hygiene exits 1:** check 9 is the only failed check, because `memory/builds/dFoldedAudit/README.md` differs from a fresh render. I didn't regenerate it, since that's the main loop's job: run `python tools/memory-tree/gen_build_index.py --write` before committing. The cause is probably this rev bump or the uncommitted prompt file, but I didn't isolate which.
- **Naming lexicon exits 1:** the hits are in `.sh` files this pass didn't touch, and its output never mentions this build. I didn't run it against the base commit, so "already failing" is an inference.
- **`tools/check-spec-tokens.py`:** not run; it stays with the main loop.

Spec: `C:\projects\coding-governance\.claude\worktrees\gov-build-m4-spec-audit-694e7b\memory\builds\dFoldedAudit\spec\2026-11-01-spec-TOOL-dFoldedAudit-1.md`
