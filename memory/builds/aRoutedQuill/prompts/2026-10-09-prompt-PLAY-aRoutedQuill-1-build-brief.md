# PLAY-aRoutedQuill-1 — build brief

**Serves:** journal PLAY-aRoutedQuill-1

node a · 2026-10-09 · authored by the orchestrator of the unattended run, for the unit agent.

- **Input.** The spec, `spec/2026-10-09-spec-PLAY-aRoutedQuill-1.md`, whole; the build README; the
  run handoff under `prompts/`. Step 5 of 6, sequenced before TOOL-aRoutedQuill-5 (both re-render the generated index). Units 1 to 4 of the roster and TOOL-aRoutedQuill-3/-4 are built before you; the write gate is ARMED on this session.
- **Fast diff-scoped gates only, nothing held.** No merge bar, no `*.test.sh` suite, no
  `run-selftests.sh`. Verify each acceptance criterion with its direct check: render the charter
  with `tools/playbook/` into `AGENTS.md`, run `bash tools/check-template-size.sh` (read the margin
  from it, never from prose; a ceiling raise is an owner decision, not an edit), and
  `bash tools/playbook/check-playbook-parity.sh` if the spec's gates name it. Observe a staged
  break red once. A criterion only a suite can observe goes into the return summary for the close.
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
  PLAY-aRoutedQuill-1` (grammar: `memory/HYGIENE.md`, "Acceptance ledger"). `git add` a new record
  before running the hygiene gate on it — the gate reads tracked files only. Run
  `python tools/memory-tree/gen_build_index.py --write` after staging, and declare every path it
  rewrites in `--dispatch`.
- **A new shell or python function stales `memory/map/generated/symbols.json`**: run
  `python tools/codebase-map/gen_map.py --write` before committing, and delete any slice script
  first.
- **Commit.** Subject names `PLAY-aRoutedQuill-1`; the trailer block carries `Pass: PLAY-aRoutedQuill-1`
  and `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`; the spec's status reads CLOSED in
  that commit. Stage `memory/builds/aRoutedQuill/RUN.md` in the same commit, because `--brief` and
  `--dispatch` write rows there and a pass commit without them leaves the record one commit late.
