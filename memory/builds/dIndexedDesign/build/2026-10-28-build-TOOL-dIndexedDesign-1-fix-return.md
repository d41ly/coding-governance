**Serves:** research TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20

# Fix pass return — dIndexedDesign

The fix-pass spec writer's final return, extracted from its transcript by script, never retyped.

All nine findings are fixed and `TOOL-dIndexedDesign-20` is written. `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25`, run against a private copy of the git index with all 17 specs staged, exits 0 and reports nothing against these specs. Its one line naming them is an informational check 25 notice about unit 5, which I did not touch. I committed nothing, did not touch the real index, wrote nothing outside `spec/`, and did not run the build-index generator. I did not run `check-spec-tokens.py` or the carries join over the set either (my role doesn't allow it), so the main loop's run is the first check of findings 2 to 7.

## The findings, by number

1. **Unit 15.** In S4 the template placeholder `<YYYY-MM-DD>` in `stream-plan: <YYYY-MM-DD>` became `stream-plan: <date>`, "an ISO date". That is the shape the spec's own §8 already uses.
2. **Unit 11.** In AC1 the path is now followed by a space before the semicolon: `. tools/unattended/lib-unattended.sh ; derive_set_identity …`. The command can't close its backticks mid-way, so I separated the semicolon from the path instead; the path is now its own tracked word.
3. **Unit 2.** In AC1 to AC5, `src/x.sh` became `<root>/<path-a>`, `src/y/z.sh` became `<root>/<dir>/<path-b>`, `src/y/` became `<root>/<dir>/` and `src/` became `<root>/`. AC1 now has one sentence defining the placeholders, so the one-segment-root case keeps its meaning.
4. **Suites named in acceptance criteria.**
   - Unit 9, AC5: the `plan_state` slice is now described by its line span (its `plan_state()` line to the first column-0 `}`), not by the suite.
   - Unit 9, AC11: now runs each reader of S11's case table directly. The existing `New arm:` line still covers AC5 and AC11.
   - Unit 16, AC6: now compares `plan_state` at HEAD and at base with a `sed -n` over the function's span.
   - Unit 16, AC9: now evaluates `tier2-review.js` and `unattended-build.js` under `node` with a stub `Workflow`. I added `New arm: tools/workflows/unattended-build.test.sh · covers AC9`.
5. **§7 leg lines.**
   - Unit 9 gained `routed-commits selftest`, `pre-push run-log line`, `run-gates run-log line`, `verifier fan-out self-test`, `review-join self-test`, `codebase-map gate coverage`, `codebase-map adopter e2e` and `policy fixtures`.
   - Unit 12 gained `policy fixtures`.
   - Unit 16 gained `verifier fan-out self-test` and `review-join self-test`.
   - I checked every name against `tools/gate-legs.json`.
6. **Hand-off tokens.**
   - Unit 13 names `derive_tag_bundles` in S9 and in its `consumes-from` bullet for unit 12.
   - Unit 1 names `coverage-lens` in S3 ("a `coverage-lens` record … is no audit for `ready-plus-audit`") and in its `consumes-from` bullet for unit 16.
   - Unit 3 names `with-spec-audit` in S1 (the opt-in it re-points is the declaration that test reads) and in its `consumes-from` bullet for unit 16.
   - Unit 8 names `### Interfaces` in its `consumes-from` bullet for unit 7 and in S5's arm (e), which now also joins a `### Interfaces` row. AC3 gained the plant `undeclared-interface-row` to observe it.
7. **Unit 20 authored** (below).
8. **Edges between units 8, 9, 16 and 20.**
   - Unit 8: the external part-2 bullet is now `hands-off TOOL-dIndexedDesign-20 — read_feature_designs …`, and §1, S2 and §3 name unit 20.
   - Unit 9: added `hands-off TOOL-dIndexedDesign-20 — read_spec_section`.
   - Unit 16: added `hands-off TOOL-dIndexedDesign-20 — read_design_policy … design.reentry`.
   - Unit 16 (beyond the brief): I narrowed its bullet to unit 8 to `design.forks` only, because unit 8 no longer reads `design.reentry`.
9. **The shared `tools/loop/loop.toml`.** Units 8, 13 and 20 each name it in §2, in order 8 then 9, with who writes which row. Units 8 and 20 also name the shared `design_lib.py` and `BUILD-METHOD.template.md` M2.

## Unit 20

`C:\projects\coding-governance\.claude\worktrees\unattended-dindexeddesign-516d37\memory\builds\dIndexedDesign\spec\2026-10-28-spec-TOOL-dIndexedDesign-20.md`

It carries `cl-dClosedLoop-0390@a096f77c part 2/2` and the six nodes. The status header is as given, at order 9, and both `design.forks` and `design.reentry` appear in backticks. It is 30914 bytes.

**Scope items:**
- **S1:** `read_feature_designs` gains a `rev` argument. Both the working-tree read and the read at a revision go through one parser, `parse_feature_design`.
- **S2:** `derive_interface_changes` compares two revisions using §4's direction table. Adding an interface or a consumer is additive; removing either, or changing the producer or contract, is breaking.
- **S3:** `derive_reentry_level` decides unit or feature level. It reads the policy through the literal call `read_design_policy("design.reentry", root)`, and the trigger table covers all four values.
- **S4:** the `diff` record kind.
- **S5:** the `--reentry` command.
- **S6:** `--input`, whose kinds and routes come from the `item.design.input` row in `tools/loop/loop.toml`, so there is no second list.
- **S7:** the `inventory` record kind.
- **S8:** `gen_build_index.py --inventory`, which checks the inventory against every unit marked CLOSED at each `Of` revision.
- **S9:** the `design.reentry` catalogue row gains its summary and usage line.
- **S10:** the three items go live and their stand-in rows leave `loop.toml`.
- **S11:** new plants on unit 8's `--decompose-fixture`.
- **S12:** a sentence in M2.

**Forks** (all settled at rung 3, except F5, settled by a probe):
- **F1:** `interface-change` is read as the breaking-change trigger, so removing it from the set keeps a breaking change at the unit level.
- **F2:** the input's kind is passed by the caller with `--kind` and checked against the item row's outcomes.
- **F3:** the classifier is unit 20's own table in `design_lib.py`, because PLAY-dOrderedCharter-36's classifier is unbuilt and its build is not an ancestor.
- **F4:** `two-plus-units` counts the units the diff touches, and the two judgment triggers hold only when the caller passes `--flag`.
- **F5 (FACT-QUESTION):** the inventory join lives in `gen_build_index.py`, because that file already imports `design_lib` (its lines 548-549) and the reverse import would be a cycle.

## Edges and asks still owed

No edge is left one-sided. Two asks from unit 20 need filing by the main loop:
- **To dDeclaredLoop, target TOOL-dDeclaredLoop-13 (from F1).** Accept: row F6's outcome reads the feature-level outcome of `item.design.reentry` (a breaking change or a held `design.reentry` trigger), seen on a planted additive change under `two-plus-units` moving its feature to `decomposed`.
- **To dOrderedCharter, target PLAY-dOrderedCharter-36 (from F3).** Accept: S5's classifier and unit 20's direction table read one declared-direction function, extracted by whichever lands second.

Two notes:
- The README's `ids:` list and roster table do not yet name TOOL-dIndexedDesign-20.
- Unit 9's AC7 still runs `review_replay.py --selftest`. The fix brief allows a `--selftest` flag, but the spec brief forbids naming one in a criterion, so I left it unchanged.
