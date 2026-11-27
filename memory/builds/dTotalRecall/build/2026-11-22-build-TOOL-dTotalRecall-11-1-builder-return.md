**Serves:** journal TOOL-dTotalRecall-11

# TOOL-dTotalRecall-11 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `4993aec72` from [2026-11-22-prompt-TOOL-dTotalRecall-11-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-11-build-brief.md), recorded whole: a divergence, nothing committed.

## Why

DIVERGENCE: the spec's §6 AC4 cannot hold as written, and AC5 and AC6 inherit the problem because they run over AC4's record and clone. AC4 names memory/builds/aBriskPreflight/reviews/2026-10-12-review-TOOL-aBriskPreflight-1-2-3-4-5-6-7-10-diff-review-round1.md and expects `gov_record.py new shape-run --review` to exit 0 printing `wrote`. But S4 has the handler call `build_records.write_new_record`. That function's landed authority read, `check_mint_authority`, calls `placement.read_lease_class`, which refuses a build whose lease is held by another session (TOOL-dTotalRecall-2 S6). In a `git clone --depth 1` of the tree, memory/builds/aBriskPreflight/RUN.md is still `phase: HELD`, holding session 653ff713-97af-487f-8f4e-2f4c9c73a605. `unattended.sh --lease status build aBriskPreflight` prints `aBriskPreflight/build daily-agent 653ff713-… held held 0`. So the door exits 2 with `refused shape-run: the build lease of aBriskPreflight reads held, held by daily-agent session 653ff713-97af-487f-8f4e-2f4c9c73a605`, and it does this on every node. The code follows S4. The fixture AC4 names does not. To change it, AC4 (and AC5 and AC6, which say "that review record" and "the AC4 clone") would have to name a review record in a build whose lease reads free. For example, memory/builds/aBatchedPacket/reviews/2026-11-13-review-TOOL-aBatchedPacket-1-diff-review-round1.md: its build has no RUN.md and its Serves line is `diff-review TOOL-aBatchedPacket-1`. Its expected values would then be `-build-TOOL-aBatchedPacket-1-shape-run-1.md`, `Blocker` 0, `Out-tokens` 90630, `Merged` 0. The other option is for AC4 to say how the fixture frees the lease. I found no other divergence: every other path, symbol, flag and figure the spec cites matched the tree (`tier2-review.test.sh#SHAPE_RE`, argv[4] as bd_mtd and argv[5] as lens_py, record_kinds.py `new` writing the typed source and id-rule, `LATER_COLUMNS`, the derived caused-by cardinality cell, leg_factory `new`, the census of 318 lines, the "seventeen after research" bullet). memory/HYGIENE.md, memory/map/features/memory-tree-hygiene.md and tools/run-gates/ceiling-evidence.txt are missing from the dispatched write set; I declared them with `--dispatch --writes` and the driver accepted them.

## Summary

Nothing is committed for TOOL-dTotalRecall-11: AC4's named fixture is refused by the record door's lease check, so this returns as a divergence. Base is 4993aec724ec91248c3dfa0837c952fb5bad2dd3. The builder hook allowed every probe below; I ran no gate leg, suite or bar.

**Draft saved, worktree restored.** The full build is saved as one patch at C:/Users/d41ly/AppData/Local/Temp/claude/7ca5dd954c018619/16f4ad58-6904-4a66-bc18-9482a47ce656/scratchpad/TOOL-dTotalRecall-11-draft.patch (710 lines; reverse-apply-checked against the worktree before the restore, so it applies forward on HEAD), with a copy of the new module beside it as shape_run.py. I put every product path back with `git checkout`, deleted the new file and removed the %TEMP%/sr11 clone. Still in the tree:
- memory/builds/dTotalRecall/RUN.md: the rows the driver staged for `--brief` and `--dispatch`. I left them because the main loop's own dispatch rows are staged there too.
- Spec files for units 48 to 51, help/reference/*.md, and the untracked prompt and reground files: another writer's work, untouched.

**What the draft contains:**
- **The parser.** tools/memory-tree/shape_run.py holds `SHAPE_RE`, compiled from one field table; its pattern string is byte-identical to the spec's literal (checked). It also has `parse_shape_line`, `read_shape_line`, `check_shape_runs` and the `--parse-line`, `--parse-file` and `--check` modes.
- **The kind.** `shape-run` joins `TYPED_RECORD_KINDS` and `build_records.KINDS`. The closed sets are `SHAPE_KINDS`, `SHAPE_INTENSITIES` and `SHAPE_STAGES` in build_records.py, which the regex reads, so each word is spelled once.
- **The door.** gov_record.py gains `write_shape_run(root, review)` and the `run_shape_run` handler. The unit id comes from `tree_lib.read_bindings`. I also extracted `print_written`, now shared by the handler and `main`.
- **The leg.** Declared by `leg_factory.py new` as §4 spells it, then the registry row by `record_kinds.py new` as §4 spells it, plus the derived cardinality cell.
- **Docs and owed rows.** HYGIENE.template.md bullet ("eighteen after `research`") and its `--render` into memory/HYGIENE.md. The guard on the tier2-review self-test leg, rendered by `--write`. Rows in subject-pins.tsv and the memory-tree-hygiene dossier. A ceiling-evidence row: 1.0 s, node d, written by `derive-ceilings.py --observed`. The suite's shape arm re-pointed to spawn `shape_run.py --parse-line`. Both READMEs updated.

**Checks that ran on the draft.** Each is a probe of this unit's own code, and each stands in for the gate named:
- **AC1**, via `--parse-line` (stands in for `record-kinds`): `blocker=0` and `out_tokens=97922` printed with no `merged`; the `merged=0` and `trigger=owed` forms parse; `blocker=zero` exits 2 naming `blocker`.
- **AC2** (stands in for `memory hygiene`): the git grep census, 318 lines (DERIVED by `wc -l`), gives `318 parsed · 0 refused`.
- **AC3** prints `True True Caused-by`.
- **AC7**: `check_row` gives `[]`; with an empty writer it gives one red opening `row shape-run`.
- **AC9**: `leg_factory.py --list` names tools/memory-tree/kit.toml, and `owed_rows.py --base 4993aec72` reports 0 owed.
- **AC10**: the bullet is byte-equal between the template and memory/HYGIENE.md (stands in for `kit/dogfood doc parity`).
- **AC11** (stands in for `edge cardinality`): `check_cardinality_mirror` gives `[]`, and reds without the cell.
- **AC8**, by hand: the arm's own parse block, sliced from the suite, ran on six lines from the template's `renderShapeLine`. All six pass; with `agents=x` all six are reported wrong with `refused · agents`; with no python all six name it.
- **AC4 to AC6** were observed only on the substitute record from aBatchedPacket, in a clone with the pass applied:
  - The door wrote, then returned `exists` with the same key, and git status was unchanged.
  - All four AC5 refusals printed `refused shape-run:` and wrote nothing.
  - `check_shape_runs` returned 0 green. Changing Blocker to 3 gave 1 with `Blocker · record 3 · line 0`. A missing `Caused-by` named the stem.
  - On the named aBriskPreflight record the door refused on the lease.

**Owed to the close, after the redispatch:** the tier2-review self-test, record-kinds, memory hygiene, edge cardinality and the rest of §7, plus both `New arm:` RED-first observations (the shape arm staged by `agents=x`, and the leg staged by a planted record whose Blocker differs). Not done: no ledger was written, no `gotchas --for-diff` ran (nothing was committed), and `lexicon --measure` was not run.
