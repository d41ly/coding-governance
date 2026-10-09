# TOOL-aRoutedQuill-2 — build brief

**Serves:** journal TOOL-aRoutedQuill-2

node a · 2026-10-09 · authored by the orchestrator of the unattended run, for the unit agent.

- **Input.** The spec, `spec/2026-10-09-spec-TOOL-aRoutedQuill-2.md`, whole; the build README; the
  run handoff under `prompts/`. Step 3 of 6; TOOL-aRoutedQuill-1 (micro-spec, check 12) and KICK-aRoutedQuill-1 (brief, card `## route`) are built before you. Your F1 is RESOLVED by the probe record under `build/`.
- **Fast diff-scoped gates only, nothing held.** No merge bar, no `*.test.sh` suite, no
  `run-selftests.sh`. Verify each acceptance criterion with its direct check: feed
  `tools/hooks/scratch-guard.js` hand-built PreToolUse payloads (stdin JSON) against fixture cards
  and confs, and observe a staged break red once. A criterion only a suite can observe goes into
  the return summary for the close.
- **Your commit arms the gate on this very session.** A settings edit is live on the next tool
  call, and this run's main loop and every subagent share one session id (the probe record). So
  before you stage `.claude/settings.json` and gov's `ROUTED_PATHS`, the main loop has already put a
  `## route` naming `TOOL-aRoutedQuill-2` on the card, and this spec reads INPROGRESS. Keep it so
  until your commit flips it to CLOSED. If a write of yours is refused after arming, read the
  refusal: it is the gate working, and the remedy it names is the fix, not a bypass.
- **Re-stamp the kickoff manifest** in your commit, because `.memory-tree.conf` is on its
  `watch:` line: `last-audit` (and `last-body-change` if the body changes), with a
  `manifest-audit:` delta line in the commit message, and keep `bash
  skills/session-kickoff/manifest-check.sh` at exit 0.
- **Kit versions are NOT bumped in this pass.** The main loop bumps each kit once, after its last
  unit; `python tools/govkit/govkit.py epoch` reporting this kit as owed is expected.
- **Records.** Write the acceptance ledger as a `build/` record with `**Serves:** journal
  TOOL-aRoutedQuill-2` (grammar: `memory/HYGIENE.md`, "Acceptance ledger"). `git add` a new record
  before running the hygiene gate on it — the gate reads tracked files only. Run
  `python tools/memory-tree/gen_build_index.py --write` after staging, and declare every path it
  rewrites in `--dispatch`.
- **A new shell or python function stales `memory/map/generated/symbols.json`**: run
  `python tools/codebase-map/gen_map.py --write` before committing, and delete any slice script
  first.
- **Commit.** Subject names `TOOL-aRoutedQuill-2`; the trailer block carries `Pass: TOOL-aRoutedQuill-2`
  and `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`; the spec's status reads CLOSED in
  that commit. Stage `memory/builds/aRoutedQuill/RUN.md` in the same commit, because `--brief` and
  `--dispatch` write rows there and a pass commit without them leaves the record one commit late.
