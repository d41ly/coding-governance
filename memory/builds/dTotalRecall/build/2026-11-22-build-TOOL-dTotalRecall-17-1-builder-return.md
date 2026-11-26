**Serves:** journal TOOL-dTotalRecall-17
**Caused-by:** TOOL-dTotalRecall-17

# TOOL-dTotalRecall-17 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `479d7256a` from [2026-11-22-prompt-TOOL-dTotalRecall-17-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-17-build-brief.md), recorded whole; the pass tip is `30c21c834`.

## Why

S1 to S3 of TOOL-dTotalRecall-17 are built and committed as one pass commit with the `Pass: TOOL-dTotalRecall-17` trailer. The spec status is still INPROGRESS. The build brief (memory/builds/dTotalRecall/prompts/2026-11-22-prompt-TOOL-dTotalRecall-17-build-brief.md) says S4 to S7 and AC4/AC5 belong to the main loop at this unit's second pass commit, and tells the builder not to flip CLOSED. The task's generic order to set CLOSED conflicts with that. I followed the brief because closing now would claim AC4/AC5 are done when they have not run. Until the main loop does S4 to S7 and closes the spec, the driver's --plan will keep naming this unit.

## Summary

TOOL-dTotalRecall-17 is committed as 30c21c834 on base 479d7256a. S1 to S3 are built and checked against scratch fixtures. S4 to S7 (the runs, the map, the verdict record, any routing) are still owed to the main loop, and the spec stays INPROGRESS for that reason.

**What was built** (all in C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e):
- **tools/workflows/replay_scorer.py**
  - A third instance, `map-replay`, is added to `INSTANCES` and `INSTANCE_KEYS`.
  - New functions: `measure_map_experiment`, `extract_item_findings`, `read_map_known`, `derive_map_verdict`, `measure_existence_searches`, `measure_bytes_before_act`, `read_transcript_calls` and `measure_call_searches`.
  - An inline, byte-identical copy of `resolve_kit_dir` lets it find the runlog kit. If no runlog kit is found it refuses with exit 2 `unarmed`.
  - The run-report reading was moved out of `measure_replay_experiment` into a shared `read_run_reports`, which both experiments now use.
  - `--instance map-replay` now gives a usage error, because this instance only runs through `--experiment`.
  - Three new arms (`map-known`, `map-verdict`, `map-transcript`) raise `ARMS_DECLARED` from 29 to 32.
- **tools/workflows/kit.toml**: a `requires_if` row for `runlog`.
- **tools/workflows/README.md**: the factory and experiment paragraphs now describe the third instance.
- **Records**: the acceptance ledger memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-17-1-acceptance-ledger.md, and a deviation record, memory/builds/dTotalRecall/build/2026-11-23-build-TOOL-dTotalRecall-17-deviation-1009.md. The deviation covers what the spec did not name: five helper functions, the module constants and the CLI refusal.
- **Regenerated files**: symbols.json (from `gen_map.py --write`), and the build README, LIVE.md and dClosedLoop's as-built view (from `gen_build_index.py --write`).

**Write set.** I widened it twice with `--dispatch`: once for the deviation record's exact path (the commit hook does not accept a `<n>` placeholder) and once for the regenerated dClosedLoop as-built view.

**Commands that timed out.** The first `--dispatch` call hit my own 110 s bound and recorded nothing. Because the write could not happen without it, I re-ran it once with a 580 s bound and it succeeded. (DERIVED 2026-11-23 by the builder)

**Checks that ran.** None of these is a gate:
- **Scratch probe.** A script (C:/Users/d41ly/AppData/Local/Temp/claude/7ca5dd954c018619/16f4ad58-6904-4a66-bc18-9482a47ce656/scratchpad/u17/probe_ac.py) imported the module and ran its CLI over scratch fixtures. It stands in for the `review-replay selftest` leg on AC1 to AC3.
  - AC1: an item with no heading gives exit 2 naming M9; a heading naming a finding id no confirmed row holds gives exit 2 naming L1 and 7; with both removed it gives exit 0 and prints `known r1: 2 item(s) over 3 finding(s)`.
  - On the three real audits, the known sets came out as the spec says: 37 items over 45 findings, 14 over 19, and 16 over 18.
  - AC2: each planted figure set loses on its own term only, and the set sitting on every boundary wins.
  - AC3: the fixture transcript gives 2 searches and 911 bytes (900 + 9 + 2). A torn line is refused, and a lone copy of the file with no runlog kit beside it is refused `unarmed`. (DERIVED 2026-11-23 by the builder)
  - The `review-replay` experiment path still scores correctly after `read_run_reports` was moved out.
- **Naming lexicon.** `--suggest` approved every new name, and `--measure` left `VERB_OFFENDER_PIN` unchanged at 1435.
- **Commit hooks.** The pre-commit hooks (memory hygiene, codebase-map freshness, kickoff ratchet, unattended checks) passed on the second attempt. The first attempt was refused only because the deviation path had not been declared.
- **Bug-class checklist.** `gotchas.py --for-diff HEAD~1..HEAD` ran over the commit. I went through the classes it selected and found nothing to change: each arm's fixture triggers its rule, each ledger token is on one line and spelled by its criterion, and every manifest key the README names is one the code reads.

**Owed to the main loop at the close:**
- The RED-first observation of each new arm:
  - `map-known`: `extract_item_findings` keeping an item that has no heading.
  - `map-verdict`: `derive_map_verdict` ignoring the `searches` term.
  - `map-transcript`: `measure_bytes_before_act` counting past the first act.
- The legs on the spec's gates section: `review-replay selftest`, `python resolver (behaviour + inline parity + idiom ban)` (for the new inline `resolve_kit_dir` copy), `memory hygiene`, and the rest of section 7.
- AC4 and AC5: the twelve harness runs, the map derived at `01dcdd1ae`, the verdict record and manifest, and on a `lose` verdict the three asks. After that, flipping the spec to CLOSED.
