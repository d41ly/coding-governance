# dTieredTribunal - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
halt-code: repo-state-out-of-mandate
parked-surfaced: yes
keepalive-reaped: yes
witness: ee0e75471b66991f50f07640651881323b2d702f
phase: ABORTED
mode: slug
anchor-kind: default-branch
keepalive: 7071b8ff
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: cd971285f95e8373a2ce8cd078973f51e1c523db
anchor-ref: refs/heads/main
base: cd971285f95e8373a2ce8cd078973f51e1c523db

## Parked

2026-08-26T10:18:21Z review · item dTieredTribunal-run2-specs · reason verdict BLOCKED · blockers 1

2026-08-26T11:17:18Z review · item dTieredTribunal-run2-specs · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-08-26T11:48:38Z dispatch · item c6f320bd TOOL-dTieredTribunal-15 · reason memory/gotchas memory/map/features memory/map/generated

2026-08-26T12:26:39Z dispatch · item 7b0999a4 TOOL-dTieredTribunal-13 · reason tools/hooks .claude/hooks memory/map/features memory/map/generated

2026-08-26T13:00:50Z dispatch · item 91c5d3ac TOOL-dTieredTribunal-14 · reason tools/hooks .claude/hooks tools/workflows

2026-08-26T13:27:36Z dispatch · item fb2d692e TOOL-dTieredTribunal-11 · reason tools/workflows/tier2-review.js memory/map/features tools/check-agent-cap-restatement.sh memory/builds/dTieredTribunal/README.md

2026-08-26T13:47:59Z dispatch · item f96738b7 TOOL-dTieredTribunal-12 · reason memory/guides/BUILD-METHOD.md tools/memory-tree/BUILD-METHOD.template.md memory/map/features

2026-08-26T17:24:29Z review · item dTieredTribunal-run2-fold · reason verdict BLOCKED · blockers 2

2026-08-26T17:24:56Z review · item dTieredTribunal-run2-fold · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT

2026-08-26T21:16:50Z rescope · item add TOOL-dTieredTribunal-11 · reason the second run's unit set: this build entered BUILDING with the first run's roster and the owner's rulings TOOL-dTieredTribunal-7 through -10 authorized the parked headline goal as units 11-15, so the scope moved and until now nothing on the record said so

2026-08-26T21:17:12Z rescope · item add TOOL-dTieredTribunal-12 · reason the second run's unit set: this build entered BUILDING with the first run's roster and the owner's rulings TOOL-dTieredTribunal-7 through -10 authorized the parked headline goal as units 11-15, so the scope moved and until now nothing on the record said so

2026-08-26T21:17:31Z rescope · item add TOOL-dTieredTribunal-13 · reason the second run's unit set: this build entered BUILDING with the first run's roster and the owner's rulings TOOL-dTieredTribunal-7 through -10 authorized the parked headline goal as units 11-15, so the scope moved and until now nothing on the record said so

2026-08-26T21:17:48Z rescope · item add TOOL-dTieredTribunal-14 · reason the second run's unit set: this build entered BUILDING with the first run's roster and the owner's rulings TOOL-dTieredTribunal-7 through -10 authorized the parked headline goal as units 11-15, so the scope moved and until now nothing on the record said so

2026-08-26T21:18:06Z rescope · item add TOOL-dTieredTribunal-15 · reason the second run's unit set: this build entered BUILDING with the first run's roster and the owner's rulings TOOL-dTieredTribunal-7 through -10 authorized the parked headline goal as units 11-15, so the scope moved and until now nothing on the record said so

2026-08-27T10:14:46Z decision · item landing-marker-not-written · reason The landing HAPPENED and its evidence did not. push-main.sh gated green and pushed main to b4e1d5be on 2026-08-27; the owner countermanded mid-flight and the kill landed AFTER the push completed but BEFORE push-main wrote its lander marker, which still names a9c6d386. --landed refuses at check 34, correctly - a marker naming an earlier landing is the pass-by-finding-anything shape it exists to refuse, and writing it by hand would fabricate the evidence. The owner ruled the push STANDS. Outstanding: re-run bash tools/push-main.sh to write the marker, which forces a full bar because the recorded green sits at a9c6d386 and does not cover the pushed tip

2026-08-27T17:40:53Z abort · item dTieredTribunal · reason probe
