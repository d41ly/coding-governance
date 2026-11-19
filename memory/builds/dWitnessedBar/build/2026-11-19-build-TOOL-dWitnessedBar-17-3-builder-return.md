**Serves:** journal TOOL-dWitnessedBar-17

# TOOL-dWitnessedBar-17 — builder return 3 (run `wf_abaf325d-859`), committed 384e6761d

## Why

TOOL-dWitnessedBar-17 is built from its rev-9 spec. The pass commit is dbbd8caba (`Pass: TOOL-dWitnessedBar-17`, spec header set to CLOSED). The bug-class checklist then found one doc reader still describing the old pins, fixed in 384e6761d (`Pass: none`). I started from the second builder's saved patch, which applied cleanly at a3e1779c7. Every spec claim I checked matched the tree: blobs aacff5d2425c, fbbf1499d9a4, 8dfb2a659a2e, c6d425b34ac1 and aca25b09b5ce, and 39 cutoffs (28 + 11). No divergence.

## Summary

The unit is committed on branch/unattended-dwitnessedbar-2ed3b3: dbbd8caba is the pass commit and 384e6761d the checklist fix. No merge bar, suite or gate leg ran. The role hook refused `ratchet.py both-ways`, so the remaining `ratchet` legs, `check-memory-hygiene.sh` and every self-test were not run. Each criterion only those can observe is owed to the close.

**What changed on top of the saved patch (rev-8 and rev-9 of the spec)**
- `tools/codebase-map/map_diff.py` has a new `--list-empty-decisions` flag. It is refused with a range, `--stale-dossiers`, `--tree` or `--drop-affordance-exempt`, writes no file, and has a docstring usage line.
- The `dossier-decisions-empty` registration now seeds through `map_diff.py --list-empty-decisions` and names `ratchet (both ways)` as its leg.
- `test_dossier_decisions_are_declining` is deleted from `test_codebase_map.py` and its template.
- `adopt-memory-tree.sh --scaffold` no longer writes either waiver home, its `project/` comment says why, and its step-8 instructions now point at the population.
- `check-memory-hygiene.test.sh`:
  - every fixture section 4 lists is re-pointed;
  - the check-21 arms key `unbound-records`, and the old "pin undeclared" arm is now a stale-row arm;
  - the project-key cutoff arms use an untracked home that is removed after its last arm;
  - the scaffold arm now asserts that neither home is written;
  - the NOT MEASURED text is updated, and a new check-20 fixture plants a duplicate.
- `resolve-python.test.sh` gains the `{prefix}` seed arm.
- The `gotchas.py` fixture conf, the `govkit/selftest.py` comment, `README.md`, `HYGIENE.template.md` (re-rendered to `memory/HYGIENE.md`), `WIRE-INTO-PROJECT.md`, `.lexicon.conf`, `LEXICON.md`, the row-grammar dossier and the `reuse_lookup.py` docstring are re-worded.
- I re-seeded all four homes and re-converted `corpus-path-unresolved.txt` at a3e1779c7: 3, 16, 14 and 39 rows. (DERIVED from the builder's probe)
- The kickoff manifest is re-stamped, and the map (`symbols.json`) and build index are regenerated.
- The acceptance ledger is at `C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-17-1-acceptance-ledger.md`.

**Checks that ran, all probes over scratch clones under %TEMP% (since removed), and the gate each stands in for**
- **AC1:** the spec's grep printed nothing, and `keys-not-scalar --measure` / `keys-not-scalar` showed only the two `.lexicon.conf` rows, exit 0. Stands in for `ratchet (keys, not a scalar)`.
- **AC4:**
  - `map_diff.py --list-empty-decisions` printed the emptied `loop` dossier and left `memory/map/generated` clean;
  - `corpus_ids.py` exited 1 naming check 15 and the dead path when both homes held only header and unarmed lines, and exited 0 naming none of 13 to 15 with both homes removed;
  - the scaffold wrote neither home.

  Stands in for `memory hygiene` and `corpus-ids selftest`.
- **AC5:** both unseeded populations printed `unarmed <population> no seed` at exit 0 with no home written, and `ratchet.py unarmed` exited 0. Stands in for `ratchet (unarmed)`.
- **AC8:** `measure-cutoffs` printed 39 lines, matching the conf census and the home. Stands in for `ratchet (both ways)`. (DERIVED from the builder's probe)
- **AC9:** `git check-attr` printed `merge: rows`.
- **AC10:**
  - `upgrade_steps.py list` showed all 8 new rows;
  - the `RECORD_UNBOUND_PIN` step's up, witness and down ran, and down restored the original bytes;
  - the blank `ORPHAN_ID_PIN` step removed the key and its home, and down restored both;
  - the `DOSSIER_DECISIONS_EMPTY_PIN` step seeded 14 rows. (DERIVED from the builder's probe)

  Stands in for `govkit selftest`.
- **AC11:** the grep printed only the `conf-scalar-pins` line, and the `row-duplicates` seed armed 3 rows. Running the new arm's steps by hand gave `armed fx-pfx 1` with this pass's code and `unarmed fx-pfx exit 2` with HEAD's code. Stands in for the `python resolver` leg. (DERIVED from the builder's probe)
- **Check 20:** `row_grammar.py --check` gave the key, stale and net-to-zero results the new arm expects. Stands in for `row-grammar selftest`.
- Also: `bash -n` on every edited shell file, `py_compile` on the edited Python, `tomllib` on both kit descriptors, block parity across the three factory copies, `owed_rows.py --base HEAD` (0 rows owed), and the lexicon `--suggest` for every new name. (DERIVED from the builder's probe)

**Owed at the close**
- AC2, AC3, and the leg halves of AC4 (`both-ways`), AC6 (`never-gains`), AC7, AC8 (`both-ways`) and AC9 (`--only 3`).
- The hygiene run on the fresh scaffold.
- Every leg on section 7's line.
- RED-first observation of the four `New arm:` lines:
  - `corpus_ids.py` homes arms;
  - `resolve-python.test.sh` `{prefix}` seed arm;
  - `check-memory-hygiene.test.sh` check-20 and check-21 population arms;
  - `ratchet.py` `cutoff-later` and `cutoff-blank` plants.
- The brief's known reds still stand: install-prefix, and checks 13 and 15 at base. The probes showed the same check-13 and check-15 base reds.

**For the main loop**
- **F10 may not hold at adopters:** spec §8 F10 picks `ratchet (both ways)` so that `dossier-decisions-empty` is graded at adopters. But the memory-tree README's "What an adopter receives" table (unit 46) says `ratchet (both ways)` does not ship to adopters. I built it as the spec says. That table suggests no adopter-side leg grades the population, so the spec-writer may want to revisit F10.
- **`memory/HYGIENE.md` grew** by about 35 lines; its size cap was not checked. (DERIVED from the builder's probe)
- **Bounded commands:** no command timed out and none was skipped.
