# TOOL-aRoutedQuill-1 — build brief

**Serves:** journal TOOL-aRoutedQuill-1

node a · 2026-10-09 · authored by the orchestrator of the unattended run, for the unit agent.

- **Input.** The spec, `spec/2026-10-09-spec-TOOL-aRoutedQuill-1.md`, whole; the build README; the
  run handoff under `prompts/`. Step 1 of 6; nothing in this build is built yet.
- **Fast diff-scoped gates only, nothing held.** No merge bar, no `*.test.sh` suite, no
  `run-selftests.sh`. Verify each acceptance criterion with its direct check: run
  `check-memory-hygiene.sh` on a staged fixture or the real tree, and observe a staged break red
  once. A criterion only a suite can observe goes into the return summary for the close.
- **Kit versions are NOT bumped in this pass.** The main loop bumps each kit once, after its last
  unit; `python tools/govkit/govkit.py epoch` reporting this kit as owed is expected.
- **Records.** Write the acceptance ledger as a `build/` record with `**Serves:** journal
  TOOL-aRoutedQuill-1` (grammar: `memory/HYGIENE.md`, "Acceptance ledger"). `git add` a new record
  before running the hygiene gate on it — the gate reads tracked files only. Run
  `python tools/memory-tree/gen_build_index.py --write` after staging, and declare every path it
  rewrites in `--dispatch`.
- **A new shell or python function stales `memory/map/generated/symbols.json`**: run
  `python tools/codebase-map/gen_map.py --write` before committing, and delete any slice script
  first.
- **Commit.** Subject names `TOOL-aRoutedQuill-1`; the trailer block carries `Pass: TOOL-aRoutedQuill-1`
  and `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`; the spec's status reads CLOSED in
  that commit. Stage `memory/builds/aRoutedQuill/RUN.md` in the same commit, because `--brief` and
  `--dispatch` write rows there and a pass commit without them leaves the record one commit late.
