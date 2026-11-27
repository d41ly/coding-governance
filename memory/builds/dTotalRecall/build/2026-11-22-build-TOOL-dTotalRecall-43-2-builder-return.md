**Serves:** journal TOOL-dTotalRecall-43
**Caused-by:** TOOL-dTotalRecall-43

# TOOL-dTotalRecall-43 build pass 2 — the builder's return

The gov-builder return for the pass dispatched at `e27040824` from [2026-11-23-prompt-TOOL-dTotalRecall-43-build-2-brief](../prompts/2026-11-23-prompt-TOOL-dTotalRecall-43-build-2-brief.md), recorded whole; the pass tip is `b9b6e584a`.

## Why

TOOL-dTotalRecall-43 is built from spec rev-8 and committed as one pass commit. The spec's status header is now CLOSED · rev-8 · 2026-11-23, and the commit carries `Pass: TOOL-dTotalRecall-43`. Before writing any code I checked every claim the spec makes against the code; each one held, so this is not a divergence. Some changes go beyond what the spec states. They are recorded in deviation record 2026-11-23-build-TOOL-dTotalRecall-43-deviation-1011 and on the commit's `Decided:` lines.

## Summary

**Built** (all at C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e):
- **tools/memory-tree/record_kinds.py:**
  - S1: the `homeless records` arm.
  - S23: typed kinds are graded by `deviation_join.read_record` or `build_records.read_record`.
  - S25: the sections parity arm.
  - S41: `GIT_OWN` is now a pattern set.
  - S47: the purpose review refuses to write into a file a kit renders, and drafts an ask instead.
  - S57: `--field` key refusal.
  - S58: three new stream-plan reds (stream named twice, unit not in the README `ids:` or not matching the id grammar, second fence), via `check_plan_units`.
  - New plants: `homeless-record`, `owner-graded`, `bad-field-key`, `stream-name-twice`, `stream-foreign-unit`, `stream-two-fences`.
- **tools/memory-tree/backlog.py#check_line_break** is the one line-break rule (S37). Its callers are `check_row_value`, the factory's two checks, the door's checks, each `--edge`, record_kinds' two purpose checks and ratchet.py.
- **tools/memory-tree/build_records.py#write_record:** a collided `<n>` moves to the next number instead of raising (S43). The door-header plant gains `field-newline`, `edge-newline`, a mint beside an untracked draft, and `mint-collision`.
- **tools/memory-tree/import_walk.py#derive_closure_version** is the one version rule (S21). `tag_index.derive_extractor_versions`, `tree_lib.load_leg_reader` and `query.derive_recall_digest` all call it (S22). `CACHE_VERSION` is removed.
- **tools/memory-recall/query.py:** the index line reports freed rows (S39); with no playbook kit it exits 2 with one line (S26).
- **WIRE-INTO-PROJECT.md:** §0 and §3c now name the playbook kit (S26).
- **README and selftest docstring:** both record the one `union.py` fork (S27).
- **extract_code block** (synced in all three copies): `BUILTIN_ARMED` mirrors `KNOWN_EXTS` (S15). `read_defs_at` reads worktree ids from one `git hash-object --stdin-paths` call, counts missing paths, and reads a symlink as its link text (S36).
- **memory_measure.py:** counts only this clone's memory tree (S16, S17). It now uses `runlog/extract.py#read_result_bytes`, which replay_scorer shares (S53). New plants: `harness-memory`, `msys-path`, `foreign-memory-path`, `bare-root`.
- **Smaller items, one each:**
  - S6: the retag step writes `[section.<anchor>]`.
  - S44: every `derive_anchor` caller now seeds the authored anchors first, via `tag_index.read_authored_anchors`.
  - S52: the class extractor goes through `gotchas.build_record`.
  - S24: `memory.map-purpose` drives the chain purpose arm.
  - S20, S40: there is one grader, `check_front_matter`, and a key given twice is refused.
  - S14: the `# slug-grammar: kept` marker hides a line from `--readers`.
  - S59: the replay reads the whole history.
  - S10: new `requires_if` rows.
  - S34: ADV-05 and ADV-06 point at `record_find.py`.
  - S50: corrected docstring.
  - S28: typed derived keys removed from four fixture READMEs under tools/unattended.
  - S30: the map is regenerated.
  - S54: the kickoff `last-audit` is re-stamped.

**Paths added beyond the main loop's dispatch**, each declared with `--dispatch` before staging: tools/govkit/selftest.py (its retag expectations follow S6), tools/lexicon/selftest.py, tools/runlog/selftest.py, tools/memory-tree/ratchet.py, the deviation record, and WIRE-INTO-PROJECT.md (the commit hook refused until it was declared).

**Checks that ran.** The only gate was `lexicon naming predicates` (lexicon OK), plus `--suggest` for every minted name. Everything else was a fixture or probe of the changed code: record_kinds `--fixture` (green plus every new plant), the build_records door-header and typed-kinds plants, runlog `memory --fixture` (13 plants), and scratch-repo probes. The ledger, memory/builds/dTotalRecall/build/2026-11-23-build-TOOL-dTotalRecall-43-2-acceptance-ledger.md, has one line per criterion. The probes stand in for no gate.

**Deviation from the no-suite rule:** C:/Users/d41ly/AppData/Local/Temp/claude/7ca5dd954c018619/16f4ad58-6904-4a66-bc18-9482a47ce656/scratchpad/probe_recall.py imported tools/memory-recall/selftest.py to reuse its fixture builders. Its `@check` decorators run every arm on import, so the memory-recall suite effectively ran in-process once. Its verdicts were never read. The probe's own observations were for AC22, AC26 and AC39.

**Refused to this role:** `record_kinds.py --check` at the tip (the record-kinds leg) was blocked by the hook. Instead, probes showed 0 homeless records at the tip, 0 owner-reader reds over this tree's typed records, and no sections-parity red.

**Owed at the close:**
- RED-first observation of the five `New arm:` lines:
  - record_kinds.py: plants named above.
  - gov_record.py: door-header plant.
  - lib/extract_code.py: arms in lexicon/selftest.py.
  - runlog/memory_measure.py: `test_memory_dtr43_paths`.
  - memory-recall/selftest.py: `test_conf_change_frees_the_old_copy` and `test_query_without_playbook_kit_refuses`.
- The legs on the spec's gates section, chiefly record-kinds, build-index selftest, govkit selftest/selfcheck, corpus-ids, codebase-map kit selftest, memory-recall kit selftest, runlog selftest, playbook render selftest, the unattended suites (fixture READMEs edited) and kickoff-manifest ratchet.
- The selftest-budget rows for the three suites that gained arms, which need re-measuring.
- AC45 (edge_grammar cardinality in a scratch copy) and AC59 (65-mint counter fixture).
- AC55 and AC56 stay parked with unit 8.

**Bug-class checklist:** `gotchas.py --for-diff HEAD~1..HEAD` named 72 classes. I acted on them before committing: renamed a nested helper the lexicon flagged, made record_extract reuse tag_index's `AUTHORED_SECTION_RE`, and checked the containment and id-substring cases. Remaining items:
- record_causes.py still has its own `AUTHORED_TAG_RE`, a duplicate of the authored-tag regex.
- WIRE-INTO-PROJECT.md near line 2192 still calls union.py byte-identical; F3's grant covers only §0 and §3c.

No command timed out.
