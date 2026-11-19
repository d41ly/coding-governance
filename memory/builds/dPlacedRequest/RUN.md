# dPlacedRequest - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 88f3b4132f3cd79b01fbe745acd962b9edc18895
phase: BUILDING
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dplacedrequest-42a7be
anchor-kind: default-branch
cli-version: 2.1.326
lease-utc: 2026-11-19T02:58:11Z
pid-image: claude.exe
host: compeeto
pid: 17280
session: dec54915-9f6d-416a-abf5-d4658b7ca977
keepalive: 447082a8
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: 9e21ac760dc0a43d6ed007396922722ccee98d57
anchor-ref: refs/heads/main
base: 9e21ac760dc0a43d6ed007396922722ccee98d57

## Parked

2026-11-19T04:43:32Z review · item dPlacedRequest-spec-set-r1 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 9 · minors 25 · folded 34 · promoted 0 · disposition fold
2026-11-19T05:52:49Z budget · frozen · 63 unit(s) · 130
2026-11-19T05:52:49Z draw · review-round · dPlacedRequest-spec-set-r2 · 1/130 · 20261119T055249Z-5f4e9a

2026-11-19T05:52:49Z review · item dPlacedRequest-spec-set-r2 · reason verdict CLEAN · blockers 0 · round-highs 4 · round-minors 25 · CONVERGED · highs 4 · minors 25 · folded 29 · promoted 0 · disposition fold
2026-11-19T06:46:56Z draw · review-round · dPlacedRequest-spec-set-r3 · 2/130 · 20261119T064656Z-50cda6

2026-11-19T06:46:56Z review · item dPlacedRequest-spec-set-r3 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 2 · minors 18 · folded 20 · promoted 0 · disposition fold

2026-11-19T06:50:21Z dispatch · item 88f3b413 TOOL-dPlacedRequest-11 · reason tools/lib/gov-ref.sh tools/lib/resolve-python.test.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md tools/unattended/README.md tools/run-gates/post-merge.sh tools/push-main.sh tools/push-main.test.sh tools/loop/README.md help/loop.md .githooks/pre-push .githooks/pre-push.test.sh tools/govkit/subject-pins.tsv memory/map/generated

2026-11-19T06:52:34Z brief · item TOOL-dPlacedRequest-11 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-19T07:10:11Z draw · re-dispatch · TOOL-dPlacedRequest-11 · 3/130 · 20261119T071011Z-12b13f

2026-11-19T07:10:11Z dispatch · item 9fdc501a TOOL-dPlacedRequest-11 · reason memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-11-1-acceptance-ledger.md memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-11.md
2026-11-19T07:11:48Z draw · re-dispatch · TOOL-dPlacedRequest-11 · 4/130 · 20261119T071148Z-067a23

2026-11-19T07:11:48Z dispatch · item 9fdc501a TOOL-dPlacedRequest-11 · reason memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-11-1-acceptance-ledger.md memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-11.md .githooks/pre-push .githooks/pre-push.test.sh help/loop.md memory/guides/UNATTENDED-STOPS.md tools/lib/gov-ref.sh tools/lib/resolve-python.test.sh tools/loop/README.md tools/push-main.sh tools/push-main.test.sh tools/run-gates/post-merge.sh tools/unattended/README.md tools/unattended/STOPS.template.md tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/govkit/subject-pins.tsv memory/map/generated

2026-11-19T07:32:56Z dispatch · item dc9f0c27 TOOL-dPlacedRequest-13 · reason tools/lib/gov-feed.sh tools/lib/gov-ref.sh tools/lib/resolve-python.test.sh tools/unattended/unattended.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt tools/unattended/unattended.test.sh tools/run-gates/post-merge.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md tools/govkit/subject-pins.tsv help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-13.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-13-1-acceptance-ledger.md

2026-11-19T07:39:45Z brief · item TOOL-dPlacedRequest-13 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T08:04:18Z dispatch · item 4b9a1d04 TOOL-dPlacedRequest-1 · reason tools/unattended/unattended.sh tools/unattended/lib-unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt tools/playbook/render_playbook.py skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh help/loop.md memory/map/generated tools/govkit/subject-pins.tsv memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-1.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-1-1-acceptance-ledger.md

2026-11-19T08:07:38Z brief · item TOOL-dPlacedRequest-1 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T08:55:29Z dispatch · item ac04253f TOOL-dPlacedRequest-27 · reason tools/lib/gov-feed.sh tools/unattended/unattended.sh tools/run-gates/post-merge.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-27.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-27-1-acceptance-ledger.md

2026-11-19T08:57:08Z brief · item TOOL-dPlacedRequest-27 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T09:06:17Z dispatch · item e2e10388 TOOL-dPlacedRequest-17 · reason tools/lib/gov-feed.sh tools/unattended/unattended.sh tools/run-gates/post-merge.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md tools/govkit/subject-pins.tsv memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-17.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-17-1-acceptance-ledger.md

2026-11-19T09:17:21Z brief · item TOOL-dPlacedRequest-17 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T09:41:29Z dispatch · item 35a1e4a5 TOOL-dPlacedRequest-23 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-23.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-23-1-acceptance-ledger.md

2026-11-19T09:43:47Z brief · item TOOL-dPlacedRequest-23 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T09:53:15Z dispatch · item 6cee25d0 TOOL-dPlacedRequest-24 · reason tools/lib/gov-feed.sh tools/unattended/unattended.sh tools/run-gates/post-merge.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md tools/unattended/README.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-24.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-24-1-acceptance-ledger.md

2026-11-19T10:21:17Z brief · item TOOL-dPlacedRequest-24 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T10:31:09Z dispatch · item 26fcb0c4 TOOL-dPlacedRequest-25 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-25.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-25-1-acceptance-ledger.md

2026-11-19T10:33:59Z brief · item TOOL-dPlacedRequest-25 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T10:45:59Z dispatch · item 6e909d5f TOOL-dPlacedRequest-16 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh help/loop.md memory/map/generated tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md tools/loop/budget.py tools/govkit/subject-pins.tsv memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-16.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-16-1-acceptance-ledger.md

2026-11-19T11:15:25Z brief · item TOOL-dPlacedRequest-16 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-19T11:16:19Z draw · re-dispatch · TOOL-dPlacedRequest-16 · 5/130 · 20261119T111619Z-280c9d

2026-11-19T11:16:19Z dispatch · item 5f71c060 TOOL-dPlacedRequest-16 · reason skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh memory/guides/SESSION-KICKOFF.md
2026-11-19T11:49:25Z draw · re-dispatch · TOOL-dPlacedRequest-16 · 6/130 · 20261119T114925Z-f7c57c

2026-11-19T11:49:25Z dispatch · item 5f71c060 TOOL-dPlacedRequest-16 · reason skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh memory/guides/SESSION-KICKOFF.md help/loop.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-16-1-acceptance-ledger.md memory/guides/UNATTENDED-STOPS.md tools/unattended/STOPS.template.md tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/map/generated tools/govkit/subject-pins.tsv
2026-11-19T11:56:24Z draw · fix-pass · TOOL-dPlacedRequest-16 · 7/130 · 20261119T115624Z-480c57

2026-11-19T11:56:24Z dispatch · item b7e369ee TOOL-dPlacedRequest-16 · reason tools/unattended/unattended.test.sh memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-16-1-acceptance-ledger.md memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-16.md

2026-11-19T12:03:00Z dispatch · item 7018a3a1 TOOL-dPlacedRequest-26 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-26.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-26-1-acceptance-ledger.md

2026-11-19T12:04:51Z brief · item TOOL-dPlacedRequest-26 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T12:15:33Z dispatch · item 6d5207db TOOL-dPlacedRequest-36 · reason tools/lib/gov-feed.sh tools/unattended/unattended.sh tools/run-gates/post-merge.sh tools/unattended/unattended.test.sh memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-36.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-36-1-acceptance-ledger.md

2026-11-19T12:17:28Z brief · item TOOL-dPlacedRequest-36 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T12:28:23Z dispatch · item 1bd813d2 TOOL-dPlacedRequest-37 · reason tools/lib/gov-feed.sh tools/unattended/unattended.sh tools/run-gates/post-merge.sh tools/unattended/unattended.test.sh memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-37.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-37-1-acceptance-ledger.md

2026-11-19T12:30:43Z brief · item TOOL-dPlacedRequest-37 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T12:40:14Z dispatch · item a8ef2cf1 TOOL-dPlacedRequest-38 · reason tools/lib/resolve-python.test.sh memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-38.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-38-1-acceptance-ledger.md

2026-11-19T12:43:06Z brief · item TOOL-dPlacedRequest-38 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T12:58:57Z dispatch · item fe17c278 TOOL-dPlacedRequest-39 · reason tools/lib/gov-feed.sh tools/unattended/unattended.sh tools/run-gates/post-merge.sh tools/unattended/unattended.test.sh memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-39.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-39-1-acceptance-ledger.md

2026-11-19T13:03:26Z brief · item TOOL-dPlacedRequest-39 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-19T13:04:39Z draw · re-dispatch · TOOL-dPlacedRequest-39 · 8/130 · 20261119T130439Z-0d8786

2026-11-19T13:04:39Z dispatch · item 728cd444 TOOL-dPlacedRequest-39 · reason tools/lib/resolve-python.test.sh
2026-11-19T13:12:10Z draw · re-dispatch · TOOL-dPlacedRequest-39 · 9/130 · 20261119T131210Z-d01894

2026-11-19T13:12:10Z dispatch · item 728cd444 TOOL-dPlacedRequest-39 · reason tools/lib/resolve-python.test.sh memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-39-1-acceptance-ledger.md tools/lib/gov-feed.sh tools/run-gates/post-merge.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-39.md
