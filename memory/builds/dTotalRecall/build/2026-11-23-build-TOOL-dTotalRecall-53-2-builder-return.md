**Serves:** journal TOOL-dTotalRecall-53
**Caused-by:** TOOL-dTotalRecall-53

# TOOL-dTotalRecall-53 build pass 2 — the builder's return

The gov-builder return for the pass dispatched at `6ab7625a1` from [2026-11-23-prompt-TOOL-dTotalRecall-53-build-2-brief](../prompts/2026-11-23-prompt-TOOL-dTotalRecall-53-build-2-brief.md), recorded whole; the pass tip is `6db81d070`.

## Why

Spec rev-6 holds as written at 6ab7625a1, so TOOL-dTotalRecall-53 is built in one pass commit. Every item except S20, S32 and S36 is built or re-observed (§3 and §8 parked those three). The commit carries the `Pass: TOOL-dTotalRecall-53` trailer, and the spec header is set to CLOSED in that same commit.

## Summary

I built TOOL-dTotalRecall-53 and committed it as 6db81d070 on base 6ab7625a1, with the spec header set to CLOSED. I ran no gate, suite or bar; every criterion was checked with python -c probes, the unit's own commands over scratch fixtures, or scratch clones under %TEMP% (now removed). Results are in memory/builds/dTotalRecall/build/2026-11-23-build-TOOL-dTotalRecall-53-2-acceptance-ledger.md.

**What changed**
- **One keep marker (S34).** The three code censuses now read `# census: kept <census> <reason>` (`//` in JavaScript) through `id_grammar.read_kept_reason`. The two file-keyed constants keep only their build-folder rows (9 in all).
- **Marked or re-pointed lines.** I marked 31 split lines, 16 alias hits and 108 Serves literals across 42 files (DERIVED 2026-11-23, the builder's count over its pass), then re-rendered the `gen_build_index.py` forwarders with `shims.py --write`. Three splits were re-pointed onto `parse_id_parts` instead: `record_causes.derive_reached`, `gov_record.run_spec` and the record_causes fixture's slug.
- **Item-level changes:**
  - S9: the writer census grades each Serves literal, not each file.
  - §8 F5: the four docstrings say `Serves:` unbolded, and `LEGACY` is unchanged byte for byte.
  - S19, S22, S39: the alias census also reads a regex alternation, a bare `case` pattern, a module constant's alias key, and the build folders' scripts.
  - S23: the homeless check reads every file outside builds, with a new `not-records` list in `record-kinds.toml`.
  - S21, S1, S16: `derive_record_kind` takes a `written_kind` argument, and the flip probe has two new census cases.
  - Also built: S4, S10, S12, S14, S24, S27 (all 140 build READMEs re-rendered), S31 (a new gotcha class), S33, S35, S37, S40 and S41.
  - S22: ask PLAY-dClosedLoop-1003 was filed through the ask door.
- The kickoff manifest is re-stamped, and the map and index are regenerated.

**Checks run, and the gate each stands in for**
- Observed: AC1, AC2, AC4–AC10, AC12–AC19, AC21–AC31, AC33–AC35 and AC37–AC41.
- The census and check functions called over the tree stand in for the `record-kinds`, `record causes`, `edge cardinality` and `corpus-ids` legs. All three censuses list 0 red.
- `check_record_kinds` is red only on two pockets in this machine's `.git` (`dHomedResolver`, `history-verdicts`). HEAD's code reds them too, so they are inherited.
- AC11 was re-observed over the unit 19 fixture.
- AC3 was only partly observed: all 209 old-style ids fall back in every re-pointed reader, and none collides with a build folder or an ask. Full reader-output parity against a worktree at base is owed.
- The naming lexicon gave OK for all 13 new names, and `VERB_OFFENDER_PIN` stays at 1435.
- `py_compile`, `bash -n` and `node --check` passed on every changed file except the `.test.sh` suites: the gate-guard hook refused `bash -n` on those, so their syntax check is owed.
- The commit hook first failed on check 23 (ledger line labels) and an unclaimed gotcha class in the codebase map; both were fixed before the commit landed.

**Owed to the close**
- The legs on the spec's gates section.
- RED-first runs for the five `New arm:` lines:
  - record_causes plants `literal-without-cause`, `duplicate-cause`, `unmarked-writer`
  - record_kinds plants `unarmed-on-disallowed-form`, `awk-regex-alias`, `alias-constant`, `homeless-empty`
  - id_grammar cases `i-named-reader`, `unmarked-split`
  - edge_grammar plant `cardinality-refused`
  - runlog `test_memory_dtr53_paths`
- No suite in the declared write set runs the record_causes or edge_grammar plants. Each grades itself PASS or FAIL, but wiring them into `check-memory-hygiene.test.sh` or `adopt-playbook.sh` is still open.
- The `memory hygiene --only 9` run, and the AC3 reader parity.

**Risks**
- The homeless check now reds any unhomed file an adopter has under `memory/` outside builds. The `not-records` globs spell `memory/` literally, which is an adopter contract change.
- The comment-only edits to `tier2-review.js` and `unattended-build.js` may need a kit version bump if a version leg requires one.
- The `Decided:` trailers record the choices, among them: the module-constant alias form reads the tool root only; `derive_path_key` folds MSYS paths on every platform; the homeless check reds only an empty population; and a census case with nothing to plant prints `unarmed`.

**Gotchas checklist**
`gotchas.py --for-diff HEAD~1..HEAD` ran and listed 117 classes. I acted on the relevant ones: renamed outputs have no stranded readers, the new fixtures cannot pass by finding nothing, no new local collides, and ledger tokens sit on one line each.
