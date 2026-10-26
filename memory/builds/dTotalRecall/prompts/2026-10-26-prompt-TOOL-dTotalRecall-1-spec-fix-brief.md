**Serves:** research TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-14 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-23 TOOL-dTotalRecall-26

# Spec fix brief — dTotalRecall, the cross-writer fixes before the first spec commit

The five spec writers of `unattended-build.js` run `wf_a94908c7-6d6` wrote all twenty-six specs under
`memory/builds/dTotalRecall/spec/`; their returns are
`memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md`. Nothing is committed
yet, so every edit below is made IN PLACE at `rev-1` with no rev bump and no §9 line: the spec commit after this pass
is each spec's first. The spec brief `memory/builds/dTotalRecall/prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md`
still binds; where a fix below respells one of its interfaces, the fix wins. Make exactly these fixes, and no other
change to any spec's design.

## F1 · §3 edges one side declared

Hygiene check 12 and the writers' returns name these. Add each missing side, naming the token in backticks in both
specs, in the §3 bullet shape the spec already uses:

- unit 1 `hands-off TOOL-dTotalRecall-9 — record-kinds.toml` (unit 9 adds the `sections` column; unit 9 already
  declares the `consumes-from`).
- unit 2 `hands-off` to units 24 and 20 naming `gov_record.py`, wherever 24 and 20 already declare the
  `consumes-from`; add whichever side is missing.
- unit 9 `hands-off TOOL-dTotalRecall-23 — record find`, with unit 23's `consumes-from` back if it is missing.
- `policy_value.py`: unit 8 (order 3) is the ONE creator of `tools/memory-tree/policy_value.py`, the memory-tree
  adapter over `read_policy_value`. Units 2, 3, 4, 5, 7, 9 and 19 read it and no longer create it "where absent":
  each drops it from its own Files touched and creation steps, declares `consumes-from TOOL-dTotalRecall-8 —
  policy_value.py`, and unit 8 declares the matching `hands-off` to each (it already hands it to unit 16).

## F2 · hand-off tokens the receiving spec never names

`tools/check-spec-tokens.py` reds these: a §3 bullet hands a token to a sibling whose spec never names it. Name the
token, in backticks, where the receiving spec reads it:

- unit 26 names `derive_nodes` (from unit 14).
- unit 19 names `canonical_kind` (from unit 18).
- unit 4 names `slug-grammar:` (from unit 5; it is the front-matter key unit 4's `FRONT_MATTER_KEYS` admits).
- unit 6 names `slug_class` (from unit 5).
- unit 23 names `section` (from unit 9).

## F3 · interface agreements

- **I5 edge line.** Unit 19 settled it (its §8 F1, F2): a section's edge line is PLAY-dOrderedCharter-24 S2's
  `**Edges:** type=target[,target]`, one line per type, and header lines also accept the typed factory's
  `- **Key:**` form. Unit 2's door writes exactly that spelling; unit 22 reads through the parent's parser. Fix any
  spec that still spells I5's ` · `-joined pairs.
- **Unit 1's conformance gate** accepts the two columns other units add: `root` (unit 19, true on the build-readme
  and claim rows) and `sections` (unit 9). Its S3 two-way schema comparison reads unit 4's `FRONT_MATTER_KEYS` dict
  literal by its keys.
- **Unit 18's `RECORD_KIND_TOKENS`** keeps PLAY-dOrderedCharter-42's `+ TYPED_RECORD_KINDS` concatenation rather than
  a fixed tuple, because unit 11 adds `shape-run` through it.
- **Unit 2's `new build-readme` and `new spec`** accept every flag `--new-build` and `--new-spec` take today, since
  unit 20's forward passes them through unchanged; the door does not append to the feed itself (unit 24's lander
  hook does).

## F4 · acceptance criteria and gates

- Unit 21: §6 names `gov/index.db` and `tools/lib/common_dir.py` as paths that do not exist at HEAD; cite them by
  basename (`index.db`, `common_dir.py`) in §6 and keep the full paths in §2, §4 and Files touched.
- Units 21 and 8: a criterion names `selftest.py` as its observation. A suite is not an acceptance observation:
  observe the checker on a staged break or a fixture of the unit's own code, and move the suite to a `New arm:` line
  in §7.
- Unit 7: its §4 Files touched names `tools/memory-tree/gen_build_index.py`, whose guard trips the leg
  `tier2-review self-test`; add that leg to its §7 leg line.
- Unit 9: its Files touched names `skills/session-kickoff/manifest-check.sh`, whose guard trips `manifest-check
  self-test`, `scratch-guard self-test` and `lexicon naming predicates`; add the three to its §7 leg line.

## How to check, and what to return

Run `python tools/check-spec-tokens.py memory/builds/dTotalRecall/spec/*.md` from the repository root; it reads the
working tree and must end `0 unwaived hit(s)` for this build's specs. Run `bash tools/memory-tree/check-memory-hygiene.sh
--only 2,12,25`: the specs and deviation records are STAGED in this worktree, so the gate sees them here; it must
print no FAILED line naming a dTotalRecall file. Do not commit and do not run the index generator. Return the list of
specs you edited, one line each on what changed, and the last line of each check.
