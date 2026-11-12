# aLiftedCeiling - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 768014ca37d52bef329959838d97957c97f541e9
phase: RUNNING
may: none
mode: prompt
run-branch: refs/heads/branch/unattended-aliftedceiling
anchor-kind: local
cli-version: 2.1.321
lease-utc: 2026-11-12T18:26:10Z
pid-image: claude.exe
host: compeeto-agent
pid: 5716
session: 0394fa33-012c-408f-a840-e6e4cfaac23f
keepalive: 6506ac7a
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: aa8f0800087a4d4cde9854bdbfb18a4932857726
anchor-ref: refs/heads/main
base: 768014ca37d52bef329959838d97957c97f541e9

## Parked

2026-11-12T19:00:53Z brief · item TOOL-aLiftedCeiling-1 · reason 45342159f129 memory/builds/aLiftedCeiling/prompts/2026-11-12-prompt-TOOL-aLiftedCeiling-1-build-brief.md

2026-11-12T19:02:01Z dispatch · item 1eeed758 TOOL-aLiftedCeiling-1 · reason tools/gate-legs.json tools/run-gates/ceiling-evidence.txt memory/guides/SESSION-KICKOFF.md memory/builds/aLiftedCeiling/spec/2026-11-12-spec-TOOL-aLiftedCeiling-1.md memory/builds/aLiftedCeiling/build/2026-11-12-build-TOOL-aLiftedCeiling-1-ledger.md memory/builds/aLiftedCeiling/README.md memory/LIVE.md

2026-11-12T19:18:32Z review · item aLiftedCeiling · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · highs 0 · minors 1 · disposition promote

2026-11-12T19:18:35Z rescope · item add TOOL-aLiftedCeiling-2 · reason the closing review's round-1 minor, promoted: the instruction-edits evidence row's how text names no host load and a clone sha other than the spec's
