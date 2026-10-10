# TOOL-aRoutedQuill-3 — build brief

**Serves:** journal TOOL-aRoutedQuill-3

node a · 2026-10-09 · authored by the orchestrator of the unattended run, for the unit agent.

- **Input.** The spec, `spec/2026-10-09-spec-TOOL-aRoutedQuill-3.md`, whole; the build README; the
  run handoff under `prompts/`. Step 4 of 6, sequenced (unit 3 before unit 4, both write memory/map/generated/). TOOL-aRoutedQuill-1, KICK-aRoutedQuill-1 and TOOL-aRoutedQuill-2 (the write gate, now ARMED on this session) are built before you.
- **Fast diff-scoped gates only, nothing held.** No merge bar, no `*.test.sh` suite, no
  `run-selftests.sh`. Verify each acceptance criterion with its direct check: run
  `python tools/memory-tree/routed_commits.py` (its `--selftest`, and RANGE/STAGED modes against
  scratch-clone fixtures), and drive `tools/push-main.sh`'s mint commit from a scratch-clone
  fixture, never the real remote. Observe a staged break red once. A criterion only a suite can
  observe goes into the return summary for the close.
- **Render `memory/map/generated/` with `python tools/codebase-map/gen_map.py --write`**; unit 4
  re-renders it after you.
- **The write gate is armed on this session.** Your writes to `ROUTED_PATHS` pass only while the
  card's `## route` names this unit and this spec reads INPROGRESS; the main loop set both before
  dispatch. A refusal names its remedy: read it, it is the gate working, never bypass it.
- **Every commit touching `ROUTED_PATHS` names its unit** in the subject or the `Pass:` trailer, from
  the run's first commit (the handoff's Corrections section).
- **Re-stamp the kickoff manifest** in your commit if you stage a file on its `watch:` line
  (`.memory-tree.conf`, `tools/gate-legs.json` among them): `last-audit`, with a `manifest-audit:`
  delta line in the commit message, keeping `bash skills/session-kickoff/manifest-check.sh` at 0.
- **Kit versions are NOT bumped in this pass.** The main loop bumps each kit once, after its last
  unit; `python tools/govkit/govkit.py epoch` reporting this kit as owed is expected.
- **Records.** Write the acceptance ledger as a `build/` record with `**Serves:** journal
  TOOL-aRoutedQuill-3` (grammar: `memory/HYGIENE.md`, "Acceptance ledger"). `git add` a new record
  before running the hygiene gate on it — the gate reads tracked files only. Run
  `python tools/memory-tree/gen_build_index.py --write` after staging, and declare every path it
  rewrites in `--dispatch`.
- **A new shell or python function stales `memory/map/generated/symbols.json`**: run
  `python tools/codebase-map/gen_map.py --write` before committing, and delete any slice script
  first.
- **Commit.** Subject names `TOOL-aRoutedQuill-3`; the trailer block carries `Pass: TOOL-aRoutedQuill-3`
  and `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`; the spec's status reads CLOSED in
  that commit. Stage `memory/builds/aRoutedQuill/RUN.md` in the same commit, because `--brief` and
  `--dispatch` write rows there and a pass commit without them leaves the record one commit late.
