**Serves:** research TOOL-dTotalRecall-8

# TOOL-dTotalRecall-8 build pass 1 — the builder's return (DIVERGENCE: the re-timing loses)

The gov-builder return of `unattended-unit.js` run `wf_f5357dcb-803`, at base `b4137f489`, saved in substance. Nothing was committed; the draft core is a patch under the session scratchpad.

## why

DIVERGENCE: TOOL-dTotalRecall-8 loses its own re-timing (S1 / AC1), so §8 F1's loss route applies. That route retires the unit WONTDO, and only the spec writer can write WONTDO's tail pointer. I followed S1 in order: before any other code, I wrote the derivation core of §4 "The derivation". That is `extract_ranges` in the `extract_code` block, its fourth copy at tools/playbook/extract_code.py, and tools/playbook/code_record.py with the bounds, the per-tree resolution, `--dump` and `--time`. I timed it cold on gov's tree at the pass base: `python tools/playbook/code_record.py --time --tree b4137f4897595a1911ce59a73ce88b8a61785f6c` printed `seconds 10.80` (DERIVED at observation) and `bytes 10884519` (DERIVED at observation). The bytes are over AC1's 1,000,000 line (PINNED by the clause) by about ten times. The loss holds however the rows are rendered: in a probe over the same derivation, the every-tracked-file `code_file` rows S7 and the §4 Bounds sentence on non-code skipped rows ask for come to 1,255,628 bytes of paths alone (15,118 files, DERIVED). The definitions alone, with key, range and a 12-hex hash, come to 850,731 bytes (11,297 defs, DERIVED). The resolved `calls` edges' src and dst alone come to 2,318,591 bytes (23,382 edges, DERIVED), with 48,015 mention edges on top (DERIVED). Each figure leaves out everything else, so even the smallest faithful dump is over 3 MB. The fixture run was not needed: AC1 reds when either run is over a line. What the spec would have to say: either F1's route as written (WONTDO with the measurement in the deviation it owes, readers keep `git grep`), which §8 F1 already states and only the spec writer may carry out, or a re-scoped AC1/§4 "Record size". The second would redefine `bytes` as something other than every row of the record, for example the neighbourhood an agent reads, and cut `code_file` rows to code-language files (30,449 bytes, DERIVED). It would also have to deal with calls edges at 2.3 MB. I restored every path I changed and committed nothing. The draft core is saved as a patch that applies cleanly at base.

## summary

TOOL-dTotalRecall-8 is not built: it fails its own size test, so nothing was committed and the unit needs the spec writer before it can be dispatched again.

**What failed.** Following S1, I wrote the derivation core first and timed it cold on gov's tree at base b4137f48 with `code_record.py --time`. It printed `seconds 10.80` and `bytes 10884519`. The time is under the 30 s line, but the size is about ten times the 1,000,000-byte line, so AC1 is red. That puts the unit on §8 F1's loss route, which retires it as WONTDO. Only the spec writer can write that, so this comes back as a divergence. (DERIVED, the builder's own run)

**Why no rendering fixes it.** I measured the smallest parts of the record on their own:
- the paths of the `code_file` rows S7 asks for, one per tracked file: 1,255,628 bytes (DERIVED, the builder's own run)
- the definitions with range and a short hash: 850,731 bytes (DERIVED, the builder's own run)
- the resolved call edges' endpoints: 2,318,591 bytes (DERIVED, the builder's own run)

Each alone is near or over the line, and together they are over 3 MB. (DERIVED, the builder's own run)

**What I checked before building.** Every seam the spec cites exists as described: `tag_index.py#load_index`/`derive_index_path`/`read_worktree_trees`/`load_memory_tree`/`build_index`, `tree_lib.py#read_blobs_at`, `policy_value.py#read_policy_value`, runlog `extract_segments`/`_derive_program` and the helpers named alongside them, `resolve_prefix_token`, the `extract_code` parity row, `record_kinds.py` `FORMS`/`add_record_kind`, `map_lib.py#parse_dossier`/`measure_dossier_staleness`, P32's clause, the core-pending row, the docs-ledger row at line 180, the unsummarised key and its catalogue row, and the size of `unattended.test.sh`. No other divergence found. Two loose notes for whoever revises the spec:
- the moved functions in `tools/runlog/extract.py` are scattered, so one contiguous marked region means reordering them;
- the spec doesn't say whether the kit epoch leg needs `kit.toml` version bumps for runlog, playbook, lexicon or codebase-map.

**Checks run.** The cold re-timing above, which is AC1's observation, plus probes of `extract_ranges` over small Python, shell and JavaScript fixtures and over all 496 py/sh/js files (none failed to parse). No gate, suite or bar ran, and none was owed. Nothing went red-first and no `New arm:` was staged, because nothing was built. The `--brief` verb answered "brief already recorded, unchanged". `gotchas.py --for-diff` was not run because there is no commit.

**State of the tree.** The three `extract_code.py` copies are back to base and `tools/playbook/code_record.py` and `tools/playbook/extract_code.py` are deleted. I touched nothing else; the staged `RUN.md` row and another spec writer's unit 25 and unit 5 files are still in the tree. The draft core is saved at C:/Users/d41ly/AppData/Local/Temp/claude/7ca5dd954c018619/16f4ad58-6904-4a66-bc18-9482a47ce656/scratchpad/TOOL-dTotalRecall-8-draft-core.patch, and `git apply --check` passes at base. It holds `extract_ranges` in all four copies plus `code_record.py`. (DERIVED, the builder's own run)
