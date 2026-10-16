# TOOL-dRedressedBar-4 — acceptance ledger

**Serves:** journal TOOL-dRedressedBar-4

Written by TOOL-dRedressedBar-27 on 2026-10-15, after the unit closed with no ledger, from what its
builder recorded. Nothing was re-run for it. The unit was built against spec 4 rev-2 in the one
pass commit `305ea9c20`. Spec 4's rev-3 then corrected §3, §5 and §7 as a records fix and moved no
criterion, so the readings answer the criteria as they stand. The readings are the builder's, from
that commit's body and from its return in `2026-10-14-build-TOOL-dRedressedBar-1-2-agent-returns.md`,
under the heading `2026-10-14T14:59:54 · gov-builder · wf_dd507e84-fcf/a9cc4903461cf4d48` at line
4707. No merge bar, no self-test suite and no gate leg ran in the build pass. Every reading is a
direct probe, and the section 7 legs were owed to the close.

**Evidences:** TOOL-dRedressedBar-4
- AC1 — `WORKFLOW_RUNS_DIR` — the quoted-literal search over `tools/hooks/format-guard.js` printed
  one line, the declaration. The constant search printed the declaration and the
  `readJournalAgents` join, and nothing else.
- AC2 — `{"started":["a1"],"ended":["a1"]}` — `readJournalAgents` over a journal planted in the
  scratchpad printed it. On a scratch copy with the constant set to `workflowz`, it printed the
  unreadable-journal error (ENOENT), the red half.
- AC3 — `WORKFLOW_RUNS_DIR = "workflows"` — the same quoted-literal search over
  `tools/roles/adopt-roles.test.sh` printed only that line, and the
  `wf = sub / WORKFLOW_RUNS_DIR /` line was found.
- AC4 — `sess/x/subagents/workflows/wf_00000001-aaa/journal.jsonl` — the A9_WRITE program,
  extracted to a file, carried 0 apostrophes, exited 0 and wrote that journal. On a copy with the
  constant changed, the file was not there, the red half.
