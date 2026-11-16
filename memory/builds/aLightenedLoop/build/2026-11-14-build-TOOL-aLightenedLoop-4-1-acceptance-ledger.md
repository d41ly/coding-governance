# TOOL-aLightenedLoop-4 — acceptance ledger

**Serves:** journal TOOL-aLightenedLoop-4

No merge bar, no self-test suite and no gate ran in this pass. Every criterion below was observed
with the spec's own commands from the worktree root in Git Bash, before the pass commit, with their
outputs saved under the session scratchpad.

One reading the close should know. AC2's handoff command, as the spec spells it, exits 1 on this
tree: since the spec was grounded, units 3 and 5 added fork-fold records under the build's
`prompts/` folder, so the render now asks which brief to use. Both renders, before and after, ran
with `--input prompt=memory/builds/aLightenedLoop/prompts/2026-11-14-prompt-TOOL-aLightenedLoop-1-brief.md`
added. The criterion's observation, a diff of the two renders, is unchanged by it. AC3's Python
check opened both files with `encoding='utf-8'` added; it compares the same text either way.

Owner parity: this unit changes prose only, so no check's exit code, refusal text or rendered
byte moves outside the rendered prose itself. The typed builder prompt is byte-identical (AC3), and
of the nine role renders and four memory-tree documents only the three sources' copies moved
(AC1, AC4). The spec's §3 exempts this unit from a timing figure, as the brief does.

**Evidences:** TOOL-aLightenedLoop-4
- AC1 — `python tools/roles/render_agents.py --write` — wrote two files; `git status --porcelain .claude/agents/`
  listed exactly ` M .claude/agents/gov-builder.md` and ` M .claude/agents/gov-spec-writer.md`, and
  `grep -c 'check that the spec can be built as written' .claude/agents/gov-builder.md` printed 1.
- AC2 — `tools/roles/handoff.py` — the render before the edit and after it, then `diff`: the marker
  line with `role-sha` moving from `8fbf0460794b` to `174639c91458`, and the S1 paragraph's six lines
  with one blank line as added lines, nothing else. Diff aligns that blank line before the paragraph
  rather than after it, which is the same added text. The stderr load-set note read
  2257 bytes of 4096 before and 2823 bytes of 4096 after. <!-- PINNED 2026-11-14 -->
- AC3 — `cmp "$S/t0.txt" "$S/t1.txt" && echo typed-identical` — printed `typed-identical`; the
  Python check over the untyped prompts printed `True`. The probe ran over `tools/workflows/unattended-unit.js`
  as HEAD `c5006c53c` holds it and as edited. The suite arms on `tools/workflows/unattended-build.test.sh`
  (the two untyped `has` and the typed `hasnt_`) were written, not run: their RED and GREEN are the close's.
- AC4 — `bash tools/memory-tree/adopt-memory-tree.sh --render` — re-rendered only
  `memory/TEMPLATE-SPEC.md`; the porcelain listing over the four documents named it alone. `grep -c`
  printed 1 for `A watched path brings its manifest` and 1 for `the blob-pinned line` over both
  `memory/TEMPLATE-SPEC.md` and `tools/memory-tree/SPEC-TEMPLATE.template.md`.
- AC5 — `grep -c 'TEMPLATE-SPEC' tools/roles/agents/gov-spec-writer.agent.md` — printed 0; the
  `<path>@<oid>:<n>` count printed 0 for the source and for `.claude/agents/gov-spec-writer.md`, and
  `grep -c "form the spec format's writing rules give"` printed 1 for both.
- AC6 — `git grep -n -i -E 'file:line|path and line|<path>:<line>' -- tools/roles/agents/gov-builder.agent.md tools/roles/agents/gov-spec-writer.agent.md tools/workflows/unattended-unit.js tools/memory-tree/SPEC-TEMPLATE.template.md`
  — printed nothing and exited 1, both before the edits and after them.
