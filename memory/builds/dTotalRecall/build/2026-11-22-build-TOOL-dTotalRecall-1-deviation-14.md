# TOOL-dTotalRecall-1 deviation 14 — `record_kinds.py new` re-renders the HYGIENE view beside the row it appends

**Serves:** deviation TOOL-dTotalRecall-1

- **Departs from:** `TOOL-dTotalRecall-1@rev-7` [§5]
- **Hand-off:** spec-to-code
- **Before:** §5's security line says `new` writes one tracked file, the registry.
- **After:** `new` appends the row and re-renders the `gen:record-kinds` region of `tools/memory-tree/HYGIENE.template.md`, two tracked files, so AC10's `--check` exits 0 after `new` alone.
- **Cause:** builder discovery
- **Reason:** AC10 requires a green `--check` after `new` alone, and `--check` compares the region byte for byte with the registry, so a `new` writing the registry alone reds AC10; the builder resolved the tension in favour of the criterion.
- **Evidence:** pass commit `360b653fd27b7fefa4839bfb44884207230a66c6` and its `Decided:` trailer; the builder return `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-1-2-builder-return.md`.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of `wf_2c520d14-677` under the build's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-1
