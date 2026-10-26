**Serves:** research TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-23 TOOL-dTotalRecall-26

# The spec-fix pass — dTotalRecall, its return

The return of the gov-spec-writer dispatched from `memory/builds/dTotalRecall/prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-4-spec-writer.md` over the spec-fix brief, run direct/a8056c0df6728b1ae, extracted from its transcript by script.

Every fix in the brief is applied. I edited 14 specs in place at rev-1, with no rev bump and no §9 line. Nothing is committed and the index was not regenerated. Both checks now come back clean for dTotalRecall.

**Specs edited:**
- **TOOL-dTotalRecall-1:** added the missing `hands-off TOOL-dTotalRecall-9 — record-kinds.toml` bullet. The data model now says the gate accepts the `root` column (unit 19, true on the `build-readme` and `claim` rows) and the `sections` column (unit 9) and grades neither. The two-way schema comparison now reads a dict literal such as unit 4's `FRONT_MATTER_KEYS` by its keys.
- **TOOL-dTotalRecall-2:** `new build-readme` and `new spec` now take every flag `--new-build` and `--new-spec` take today: `<slug> --asks <IDLIST>` and `<id> --tier 1|2 [--order <n>] [--base <sha>]`, citing `gen_build_index.py:3887` and `:8488`. That changed `--asks <file>` to `--asks <IDLIST>` in S7, the command block and AC7. The hand-off to unit 24 now says the lander hook appends to the feed and the door does not. The hand-off to unit 19 spells the edge line `**Edges:** type=target[,target]`, one per type. Dropped `policy_value.py` from its files and added `consumes-from TOOL-dTotalRecall-8`.
- **TOOL-dTotalRecall-3, -4, -5, -7:** each dropped `policy_value.py` from its files and its "create it where absent" wording, and added `consumes-from TOOL-dTotalRecall-8 — policy_value.py`. Unit 7 also rewords its §8 F2 to name unit 8 as the creator.
  - Unit 4 also names `slug-grammar:` in its edge from unit 5.
  - Unit 7 also adds `tier2-review self-test` to its §7 leg line.
- **TOOL-dTotalRecall-6:** the edge from unit 5 now names `slug_class`.
- **TOOL-dTotalRecall-8:** added the seven `hands-off` bullets for `policy_value.py` to units 2, 3, 4, 5, 7, 9 and 19. In AC2, the fixture's test file is now `test_a.py` instead of `selftest.py`. The suite stays on its existing `New arm:` line.
- **TOOL-dTotalRecall-9:** points at unit 8 S10 for the adapter instead of unit 7 §4, adds `consumes-from TOOL-dTotalRecall-8`, and adds `manifest-check self-test`, `scratch-guard self-test` and `lexicon naming predicates` to §7.
- **TOOL-dTotalRecall-18:** `RECORD_KIND_TOKENS` keeps the `+ TYPED_RECORD_KINDS` concatenation, in S7 and in the §4 code block.
- **TOOL-dTotalRecall-19:** points at unit 8 S10 for the adapter, adds `consumes-from TOOL-dTotalRecall-8`, and the edge from unit 18 names `canonical_kind`.
- **TOOL-dTotalRecall-21:**
  - AC2 now reads the question set of the fixture `tools/memory-recall/recall-fixture.json` instead of `selftest.py`, and names `index.db` by basename.
  - AC6 names `common_dir.py` by basename.
  - The suite stays on its `New arm:` line.
- **TOOL-dTotalRecall-23:** the edge from unit 9 names `section`, and says those rows come from the served index's own `build_index`.
- **TOOL-dTotalRecall-26:** the edge from unit 14 names `derive_nodes`.

Two items in the brief needed no edit:
- **Unit 2's hand-offs to 20 and 24:** both sides were already declared.
- **The I5 edge line:** no spec designs with the old ` · `-joined spelling. Units 19 §8 F1 and 22 §8 F3 only quote it as the option they rejected.

**Check results:**
- `python tools/check-spec-tokens.py memory/builds/dTotalRecall/spec/*.md` exits 0, down from 13 hits before the pass. It prints no `0 unwaived hit(s)` line when there are no hits. Its last line is `spec-tokens: carries join · 519 chain spec(s) measured in 9 build(s), every status but WONTDO, not only live spec(s) · 509 clause(s) · 0 withdrawn · 524 owned node(s) · 0 finding(s), 0 at the Design exit only · SPEC_CARRIES_CUTOFF 2026-10-21`.
- `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25`, run again after the last edit, prints no FAILED line, so the earlier check 12 failure on unit 9 is gone. Its last line is `HYGIENE --only 2,12,25 ran checks 2 12 25`.

One gap left for you: if unit 8 is retired on its loss route (its §8 F1), unit 16 creates `policy_value.py` instead (its §8 F3). Unit 16 is order 5, ahead of every reader, so the file still exists in time, but the seven new `consumes-from TOOL-dTotalRecall-8` bullets would then point at a retired unit.

Files are in C:\projects\coding-governance\.claude\worktrees\unattended-dtotalrecall-4bf827\memory\builds\dTotalRecall\spec\:
- 2026-10-26-spec-TOOL-dTotalRecall-1.md
- 2026-10-26-spec-TOOL-dTotalRecall-2.md
- 2026-10-26-spec-TOOL-dTotalRecall-3.md
- 2026-10-26-spec-TOOL-dTotalRecall-4.md
- 2026-10-26-spec-TOOL-dTotalRecall-5.md
- 2026-10-26-spec-TOOL-dTotalRecall-6.md
- 2026-10-26-spec-TOOL-dTotalRecall-7.md
- 2026-10-26-spec-TOOL-dTotalRecall-8.md
- 2026-10-26-spec-TOOL-dTotalRecall-9.md
- 2026-10-26-spec-TOOL-dTotalRecall-18.md
- 2026-10-26-spec-TOOL-dTotalRecall-19.md
- 2026-10-26-spec-TOOL-dTotalRecall-21.md
- 2026-10-26-spec-TOOL-dTotalRecall-23.md
- 2026-10-26-spec-TOOL-dTotalRecall-26.md
