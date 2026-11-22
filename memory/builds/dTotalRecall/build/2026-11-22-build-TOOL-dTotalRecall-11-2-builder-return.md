**Serves:** journal TOOL-dTotalRecall-11

# TOOL-dTotalRecall-11 build pass 2 — the builder's return

The gov-builder return for the pass dispatched at `f711a9567` from [2026-11-22-prompt-TOOL-dTotalRecall-11-build-brief-2](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-11-build-brief-2.md), recorded whole; the pass tip is `71ce746a0`.

## Why

Every claim the rev-7 spec makes about current code still holds, and the AC4 fixture's lease reads free (`lease — none · aBatchedPacket/build`). The unit is built as the spec states and closed in one pass commit.

## Summary

TOOL-dTotalRecall-11 is built and committed as 71ce746a0 on base f711a9567. The commit carries `Pass: TOOL-dTotalRecall-11`, and in the same commit the spec header moved to CLOSED, rev-7, 2026-11-22. No gate leg, suite or bar ran in this pass.

**How it was built.** Pass 1's saved draft (C:/Users/d41ly/AppData/Local/Temp/claude/7ca5dd954c018619/16f4ad58-6904-4a66-bc18-9482a47ce656/scratchpad/TOOL-dTotalRecall-11-draft.patch) applied cleanly on f711a9567. I then re-ran both factories from section 4's exact flags over the restored declarations:
- `leg_factory.py new` reproduced the kit.toml row and tools/gate-legs.json byte for byte.
- `record_kinds.py new` reproduced the record-kinds.toml row. I then appended the `caused-by` cardinality cell, which `derive_cardinality_cell` derives.
- `leg_factory --write`, `record_kinds --write` and `adopt-memory-tree.sh --render` all stood at a fixed point.
- The ceiling-evidence row was re-taken with `derive-ceilings.py --write --observed` at 1.3 s on node d, so the ceiling stays 125.
- `gen_map.py --write` and `gen_build_index.py --write` ran, and the kickoff manifest's `last-audit` was re-stamped, because tools/gate-legs.json is on its watch list.
- The ledger is memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-11-2-acceptance-ledger.md.

**Checks that ran** (probes of this unit's own code; each stands in for the gate named):
- **AC1** (record-kinds / tier2-review): `--parse-line` prints `blocker=0` and `out_tokens=97922` with no `merged`; the `merged=0` and `trigger=owed` forms parse; `blocker=zero` exits 2 naming `blocker`. `SHAPE_RE.pattern` is byte-equal to section 4's literal.
- **AC2** (memory hygiene): the census of 318 lines gives `318 parsed · 0 refused`.
- **AC3**: prints `True True Caused-by`.
- **AC4, AC5, AC6**: run in a `git clone --depth 1` of the committed tip under %TEMP%, and before the commit in a clone with the pass applied.
  - AC4: the door wrote `...TOOL-aBatchedPacket-1-shape-run-1.md key ea6dec1f793c` with Blocker 0, Out-tokens 90630, Merged 0 and Caused-by the review's stem. A second run printed `exists` with the same key, and status did not change.
  - AC5: all four cases exit 2 printing `refused shape-run:` and write no file.
  - AC6: the check returns 0 green; with Blocker edited to 3 it returns 1 with `Blocker · record 3 · line 0`; with a missing Caused-by it names the stem.
- **AC7** (record-kinds): `check_row` gives `[]`; with an empty writer it gives one red opening `row shape-run`.
- **AC8** (tier2-review self-test): `grep -c "SHAPE_RE = "` gives 0, and the guard on the gate-legs row ends `shape_run.py`. The suite's parse block, sliced out and run by hand on the six `renderShapeLine` lines, finds none wrong. With `agents=x` all six are wrong (`refused · agents`), and with no python it says `no python was resolved`.
- **AC9** (measure-legs and the canaries): `enforces` is `practice.one-fact` and the argv names `shape_run.py --check`. `leg_factory --list` names tools/memory-tree/kit.toml. `owed_rows.py --base f711a9567` reports 0 owed both before and after the commit.
- **AC10** (kit/dogfood doc parity): the bullet names `shape-run`, reads "eighteen after `research`", and is byte-equal in the template and in memory/HYGIENE.md.
- **AC11** (edge cardinality): `check_cardinality_mirror` gives `[]`, and reds with the cell removed.
- **Naming**: every new function returned OK from `lexicon --suggest`. `lexicon --measure` leaves VERB_OFFENDER_PIN at 1448, so .lexicon.conf is untouched.

**Owed to the close:**
- Every leg in the spec's section 7 gate list.
- Two `New arm:` RED-first observations:
  - the tier2-review.test.sh shape arm, staged by `renderShapeLine` printing `agents=x`;
  - `shape_run.py --check`, staged by a planted record whose Blocker differs from its review line.
- The tier2-review suite's budget row may need re-measuring, because its shape arm now spawns python six times.

**Checklist acted on** (`gotchas --for-diff HEAD~1..HEAD`): the held-suite guard is added; the new leg's meta-gate rows read 0 owed (unit 43 owns the rest); the regex reached no heredoc; the parser runs with `dont_write_bytecode` and the suite spawns it with `-B`.

**Notes:**
- The commit hook printed a warn-only dossier-bytes notice: memory/map/features/memory-tree-hygiene.md is 21344 bytes against a 20480 budget. It was already 21286 bytes at base.
- MAP.md, CARDS.md and inventories.json are committed as generated outputs without being declared, following the unit-22 precedent.
- Unit 61's spec and its row in the build README belong to another session's work and are left unstaged.
- Both temp clones were removed.
