# aQueuedIndex - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
units-at-landing: TOOL-aQueuedIndex-1 TOOL-aQueuedIndex-2 TOOL-aQueuedIndex-3
gates-run: unattended-179450345232738512245-5856 c739aab7
parked-surfaced: yes
keepalive-reaped: yes
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 8439558dd73588bc753e954376a5288a8d0d5aa1
phase: LANDING
may: none
mode: prompt
run-branch: refs/heads/branch/unattended-aqueuedindex
anchor-kind: local
cli-version: 2.1.321
lease-utc: 2026-11-12T14:02:05Z
pid-image: claude.exe
host: compeeto-agent
pid: 5716
session: 0394fa33-012c-408f-a840-e6e4cfaac23f
keepalive: c2273454
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 97e0841d7d0bdb38df314a1f8d01616a4d431dad
anchor-ref: refs/heads/main
base: d084590b612e1dfe97fb7a55b1ff9c1cedb3482c

## Parked

2026-11-12T14:50:25Z dispatch · item 6f5d27a2 TOOL-aQueuedIndex-1 · reason tools/playbook/tag_index.py tools/playbook/gov_tag.py tools/playbook/adopt-playbook.sh help/tags.md memory/builds/aQueuedIndex/spec/2026-11-12-spec-TOOL-aQueuedIndex-1.md memory/builds/aQueuedIndex/build/2026-11-12-build-TOOL-aQueuedIndex-1-ledger.md memory/builds/aQueuedIndex/build/2026-11-12-build-TOOL-aQueuedIndex-1-deviation-11.md memory/builds/aQueuedIndex/README.md memory/LIVE.md memory/map/generated memory/map/baseline.toml memory/project/positional-refs.txt memory/project/unpinned-facts.txt

2026-11-12T14:50:54Z brief · item TOOL-aQueuedIndex-1 · reason b901a3ad86b9 memory/builds/aQueuedIndex/prompts/2026-11-12-prompt-TOOL-aQueuedIndex-1-build-brief.md

2026-11-12T15:23:30Z dispatch · item eb478868 TOOL-aQueuedIndex-1 · reason tools/playbook/tag_index.py tools/playbook/gov_tag.py tools/playbook/adopt-playbook.sh help/tags.md memory/builds/aQueuedIndex/spec/2026-11-12-spec-TOOL-aQueuedIndex-1.md memory/builds/aQueuedIndex/build/2026-11-12-build-TOOL-aQueuedIndex-1-ledger.md memory/builds/aQueuedIndex/build/2026-11-12-build-TOOL-aQueuedIndex-1-deviation-11.md memory/builds/aQueuedIndex/README.md memory/LIVE.md memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md

2026-11-12T15:38:35Z review · item aQueuedIndex · reason verdict BLOCKED · blockers 2

2026-11-12T15:38:37Z rescope · item add TOOL-aQueuedIndex-2 · reason the closing review's round-1 findings, batched: the queued-writers plant cannot see the under-lock re-read (B1), no arm fails when the overlay or gc block loses its BEGIN IMMEDIATE (M1), and the plant prints green before its checks (L1)

2026-11-12T16:22:30Z brief · item TOOL-aQueuedIndex-2 · reason 4db42f335ccf memory/builds/aQueuedIndex/prompts/2026-11-12-prompt-TOOL-aQueuedIndex-2-build-brief.md

2026-11-12T16:23:39Z dispatch · item 543acfa5 TOOL-aQueuedIndex-2 · reason tools/playbook/gov_tag.py tools/playbook/adopt-playbook.sh memory/builds/aQueuedIndex/spec/2026-11-12-spec-TOOL-aQueuedIndex-2.md memory/builds/aQueuedIndex/build/2026-11-12-build-TOOL-aQueuedIndex-2-ledger.md memory/builds/aQueuedIndex/README.md memory/LIVE.md

2026-11-12T16:38:54Z review · item aQueuedIndex · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · highs 0 · minors 1 · disposition promote

2026-11-12T16:38:56Z rescope · item add TOOL-aQueuedIndex-3 · reason the closing review's round-2 minor, promoted: BUSY_TIMEOUT = 600 has no check that fails if it shrinks; the queued-writers plant prints the timeout and its row requires 600

2026-11-12T16:56:17Z brief · item TOOL-aQueuedIndex-3 · reason 8a49fdf13f7f memory/builds/aQueuedIndex/prompts/2026-11-12-prompt-TOOL-aQueuedIndex-3-build-brief.md

2026-11-12T16:57:27Z dispatch · item d12660e9 TOOL-aQueuedIndex-3 · reason tools/playbook/gov_tag.py memory/builds/aQueuedIndex/spec/2026-11-12-spec-TOOL-aQueuedIndex-3.md memory/builds/aQueuedIndex/build/2026-11-12-build-TOOL-aQueuedIndex-3-ledger.md memory/builds/aQueuedIndex/README.md memory/LIVE.md
