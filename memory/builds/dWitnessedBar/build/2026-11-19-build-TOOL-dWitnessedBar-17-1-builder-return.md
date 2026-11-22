**Serves:** journal TOOL-dWitnessedBar-17

# TOOL-dWitnessedBar-17 — builder return 1 (run `wf_f8585f39-a29`), a divergence, nothing committed

## Why

DIVERGENCE: the spec (rev-6) cannot be built as written for the two zero pins. I found two problems by probing the tree at 4cc97d97b before any write.

(1) S1, S4, §4 "The pins" and §4 Files touched disagree with §3 Edges over `corpus-path-unresolved`. The §3 Edges consumes-from line on TOOL-dWitnessedBar-16 (unit 16) says this unit converts and registers `memory/project/corpus-path-unresolved.txt` before folding DEAD_PATH_PIN into it. The tree agrees: the file still has its old comment header and grammar, and no `[[ledger]]` table in any kit.toml names `corpus-path-unresolved`. But S1 calls it one of "the populations unit 16 converted". The §4 table gives its seed argv and leg as "unit 16's", and neither exists. Its key-kind cell reads "site · citing path, cited path", but `tools/lib/legacy_ledger.py#_check_table` refuses a `site` key without a `path` field. Files touched lists neither `memory/project/corpus-path-unresolved.txt` nor an `[[upgrade]]` conversion step for it. Nowhere does the spec say how `corpus_ids.py` keeps grading the `<occurrences>` and `absent|moved:DEST` columns once the file is in ledger grammar. The rev-6 log line itself says S1 and S4 "are restated over it at this unit's re-ground", and that restatement never landed. The spec needs to state this population's full registration: key kind and fields, seed argv, leg, direction and drain. It also needs the conversion step at adopters, the reader change in `corpus_ids.py`, and the home added to Files touched.

(2) S4 and §8 F2(a) cannot hold together with AC4 on the landed tree. S4 arms checks 13 to 15 only when `id-orphan-waiver` and `corpus-path-unresolved` are "seeded rather than `unarmed`". In gov, `memory/project/id-orphan-waiver.txt` already holds only its ledger header and `# unarmed · dead probe · ef4d5554…` (written by unit 16 at 3a7a51471). Its registered seed is `convert_registry.py read-back id-orphan-waiver`. Run now, that seed prints `dead probe: memory/project/id-orphan-waiver.txt holds no row` and exits 0. A waiver bounded at 0 offenders (ORPHAN_ID_PIN=0, DEAD_PATH_PIN=0) therefore can never read armed through a read-back seed, and `corpus-path-unresolved`, also empty, would end up the same way. So S4 disarms checks 13 to 15 in gov itself. That contradicts AC4's first clause ("arms checks 13 to 15 with no pin in the conf"), and AC4's second clause describes exactly the tree's current state as the disarmed case. The spec has to say what arms an empty zero-bound population: a live offender measurement as the seed in place of read-back, an arming signal other than the home's armed state, or something else. It also has to say whether this unit changes unit 16's `id-orphan-waiver` registration or home, and if so add those paths to Files touched.

Every other claim I probed holds. The symbols the spec cites exist in corpus_ids.py, row_grammar.py, ratchet.py, legacy_ledger.py and upgrade_steps.py. The conf assignments of the seven keys are where S3 puts them, and drift_signals.py's RATCHETS holds the four pin rows S5 removes. The `.gitattributes` ledger block and the descriptor's `conditional_keys` and `measured-pins` entries exist.

## Summary

Not built. I stopped at the pre-build check and wrote no product or record path; the tree is clean at base 4cc97d97b9c9e7638d4ebd226d18fd830228d377.

The `--brief` recording ran and reported "brief already recorded, unchanged". The two documents were /C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-17.md and /C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/prompts/2026-11-19-prompt-TOOL-dWitnessedBar-17-build-brief.md.

Checks that ran (read-only probes; none stands in for a gate):
- `git grep` for the seven pin keys and every file that reads them.
- A grep of the cited symbols in corpus_ids.py, row_grammar.py, ratchet.py, legacy_ledger.py, upgrade_steps.py, conf_to_policy.py and test_codebase_map.py.
- An inspection of the `[[ledger]]` tables in tools/memory-tree/kit.toml.
- `python tools/memory-tree/convert_registry.py read-back id-orphan-waiver`, which printed the dead-probe line.
- Probes of `.gitattributes`, check 3's named list, the descriptor's `conditional_keys` and `measured-pins` entries, and the RATCHETS rows.

No gate, suite or bar ran, and no gotchas checklist ran because nothing was committed. Nothing timed out. The two `New arm:` lines in spec §7 and the AC1 to AC10 observations are still owed once the spec is revised and the unit rebuilt.

The orientation card handed to this agent says the unit is Tier-2 at DEFERRED. The spec header reads INPROGRESS, so that card is stale.
