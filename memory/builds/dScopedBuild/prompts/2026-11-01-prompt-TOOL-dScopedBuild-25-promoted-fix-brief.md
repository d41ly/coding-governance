**Serves:** research TOOL-dScopedBuild-25 TOOL-dScopedBuild-28 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-35

# Fix brief — dScopedBuild, the round-1 promotions' token reds

The round-1 spec audit's disposal promoted TOOL-dScopedBuild-25 to -35 and folded their hands-off edges into units 1
to 15 at rev-2, all uncommitted. `tools/check-spec-tokens.py` reds the six hits below, each in exactly the spec it
names. Fix each in place with its observation unchanged, and nothing else: no design change, no edit to a spec this
list does not name. The promoted specs have never been committed, so a fix there stays at `rev-1` and owes no §9
line; a fix in TOOL-dScopedBuild-3, committed and audited at rev-1 and folded to rev-2 by the disposal, rides that
rev-2 and extends its §9 line. Read the spec brief
`memory/builds/dScopedBuild/prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md`, section "What the last
spec runs had to fix after their writers returned", before the first edit.

- TOOL-dScopedBuild-28: a criterion cites `memory/note.md`, not tracked; spell it as the planted fixture's relative
  path in words or pass it as an argument. A criterion also names `.githooks/pre-commit.test.sh`, a suite, which is
  not an acceptance observation: observe the checker on a staged break or a fixture, and move the suite to a
  `New arm:` line in §7.
- TOOL-dScopedBuild-31: a criterion cites `tools/memory-tree/record-kinds.toml`, which a parent creates and HEAD does
  not track: cite it by basename in §6 and keep the full path in §2, §4 and Files touched.
- TOOL-dScopedBuild-32: a criterion names `GATE_FULL=1`, a bar prefix: observe the unit's own function on a fixture
  instead, and leave the bar to §7.
- TOOL-dScopedBuild-35: a criterion cites `tools/codebase-map/reuse_check.py`, which unit 12 creates: cite it by
  basename in §6, full path kept elsewhere.
- TOOL-dScopedBuild-33 hands `deviation_join.read_first_passes` to TOOL-dScopedBuild-3, whose spec never names that
  token. Unit 33 supersedes unit 1's move of `read_first_passes` (the readers stay in `deviation_join.py`): name the
  token in unit 3 where it reads the base, in its §3 `consumes-from` line from unit 33, or correct unit 33's bullet
  to the token unit 3 already carries.

Return each change by spec and section, then rerun `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25`
and report its verdict on these files. Write nothing outside `memory/builds/dScopedBuild/spec/`, commit nothing, run
no generator.
