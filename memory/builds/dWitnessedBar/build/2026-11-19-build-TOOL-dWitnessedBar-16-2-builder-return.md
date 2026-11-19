**Serves:** journal TOOL-dWitnessedBar-16

# TOOL-dWitnessedBar-16 — builder return 2 (run `wf_9c94951a-c3f`), a divergence, nothing committed

## Why

DIVERGENCE: before writing anything I checked spec rev-10 (memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-16.md) against the landed factory, the ratchet pack and the readers. Three things cannot be built as written.

(1) S3, with §4 "The populations" and §4 "Inventory", says every registration carries "a `seed` argv" but does not name one for any of the 29 populations. It also gives no reader a measuring mode for that argv to call, and the landed code depends on it in four places:
- `tools/lib/legacy_ledger.py#seed_population` returns `unarmed <pop> no seed` for `seed = []`. S3 requires `present <population>`, so S3 itself rules out an empty seed.
- `tools/memory-tree/ratchet.py#run_unarmed` fails `ratchet (unarmed)` for a `seed = []` registration whose home holds rows.
- `ratchet.py#run_seed_laundering` (line 407, `if removed and reg.seed`) runs the seed whenever a row leaves its base. A seed that measures nothing therefore fails every later drain as `unresolved`, or passes it wrongly.
- A fresh `seed` in an adopter writes whatever the seed prints, which makes S10's migration depend on the argv too.

The precedent is `conf-scalar-pins`, whose seed is the leg's own measurement (`ratchet.py keys-not-scalar --measure`, printing `<fields> TAB <count>` rows). No reader §4 names has an equivalent: `sh_hygiene.py`, `encoding_posture.py`, `check-brief-recorded.sh`, `check-pass-order.sh`, `check-dead-paths.sh`, `check-testsuite-counts.sh`, `check-spec-tokens.py`, `docs_leg.py`, `fork-count.sh`, `check-method-carriers.sh`, `check-playbook-parity.sh`, `check-agent-cap-restatement.sh` and `transition_audit.py` have no measure flag. The flags that do exist print conf pins, not keyed rows: `corpus_ids.py --measure`, `lexicon.py --measure`, `check-arms.py --emit-pin`. The spec needs to name each population's seed argv and put the measure mode it adds to each reader into Scope, Files touched and Acceptance (a new mechanism per reader), or state another rule that satisfies `run_unarmed`, `run_seed_laundering` and S3's `present`.

(2) §5's empty-states line says "an empty population keeps its header and reads `unarmed`". The landed `ratchet.py#run_populated` fails `ratchet (populated)`, a manifest leg in `tools/gate-legs.json`, for any armed home with a seed and no rows. Seven of the converted homes hold no row today: `corpus-path-unresolved.txt`, `id-orphan-waiver.txt`, `location-probe-waivers.txt`, `stale-header-waiver.txt`, `transition-audit.txt`, `lexicon-suffix-waivers.txt` and `lexicon-verb-waivers.txt`. That leg therefore exits 1 on the landed tree, while §7 says the ratchet legs grade every converted population and the bar must pass. The brief admits this failure "until unit 7 lands", but the spec's §5 sentence and §7 cannot both hold. The spec has to say what those seven homes are at this pass.

(3) S7 and AC6 convert `readme-contract.txt`. §3 Edges and TOOL-dWitnessedBar-51 S22 leave that file to a main-loop commit, and the brief requires every reader I change to "accept both the old and the converted file until then". Doing that means `gen_build_index.py#read_contract_rows` keeps a parser for the old grammar. S4 forbids that ("no reader keeps a parser of the old grammar"), AC3's Red-when fails on it, and no unit's spec removes that transitional read afterwards. The spec needs to name the transitional dual read and the unit and acceptance that remove it.

Also noted, not blocking: after S6's rename, `tools/codebase-map/test_codebase_map.py:169` (unit 51 S5's) still passes `baseline.toml` to `derive_baseline_additions`. The F8 adapter then finds no registration, so the baseline's never-gains check reports UNGRADED rather than failing from this pass until unit 51 lands. §3 or §5 should state that gap.

No path was changed and nothing was committed.

## Summary

I stopped before writing any code, because the TOOL-dWitnessedBar-16 spec (rev-10) can't be built as written. Nothing is committed, and the tree is clean at 6f80e4e8e29393486a144eefe114ae20c5f94c17.

**What I checked (reading only, no code written):**
- **Population:** `git ls-files` matches §4: 29 homes to convert, plus unit 14's `conf-scalar-pins.txt` and the three lists §3 leaves to unit 18.
- **Code I read:** the ledger factory (`tools/lib/legacy_ledger.py`), the ratchet legs in `tools/memory-tree/ratchet.py`, `check-arms.py#check_retirements`, the drift dictionaries in `drift_signals.py`, `owed_rows.py`, the `coverage_join` copies and `test_codebase_map.py`.
- **Flags:** I searched every reader §4 names for a measure, seed or emit flag.

**The three problems, all detailed in `why`:**
1. **Seed commands:** every registration must carry a `seed` command that measures its population. The landed ratchet legs fail without one. Neither the spec nor any reader supplies such a command for any of the 29 populations.
2. **Empty homes:** §5 says an empty population reads `unarmed`. In fact the landed `ratchet (populated)` leg fails it, and seven converted homes are empty, so that leg fails on the landed tree.
3. **`readme-contract.txt`:** the brief requires readers to accept both the old and the new grammar. S4 and AC3 forbid keeping an old-grammar reader, and no unit removes it later.

I also noted, without treating it as blocking, that `test_codebase_map.py` will report the baseline check as UNGRADED from this pass until unit 51 lands.

**Commands run:**
- `bash tools/unattended/unattended.sh --brief dWitnessedBar --unit TOOL-dWitnessedBar-16 --path memory/builds/dWitnessedBar/prompts/2026-11-19-prompt-TOOL-dWitnessedBar-16-build-brief.md` said the brief was already recorded, unchanged at 25468d36ee60, and wrote nothing.
- Nothing timed out and nothing was skipped.

**Not done:**
- No gate, suite or bar ran, and none of these reads stands in for one.
- Every §7 leg and both `New arm:` red-first checks (`tools/drift-audit/selftest.py` for AC7/AC8, `tools/memory-tree/ratchet.py` for AC12) are still owed at the close once the unit is rebuilt.
- `gotchas.py --for-diff` didn't run, because there is no commit.
- I didn't write the converted `readme-contract.txt` to the scratchpad, since the conversion never started.

The spec writer needs to revise the spec before this unit is dispatched again.
