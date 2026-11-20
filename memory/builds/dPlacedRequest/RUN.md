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
lease-utc: 2026-11-19T15:04:39Z
pid-image: claude.exe
host: compeeto
pid: 27268
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

2026-11-19T13:21:14Z dispatch · item 5f8b8dea TOOL-dPlacedRequest-41 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-41.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-41-1-acceptance-ledger.md

2026-11-19T13:23:22Z brief · item TOOL-dPlacedRequest-41 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T13:47:10Z dispatch · item 8f3cf456 TOOL-dPlacedRequest-20 · reason tools/unattended/unattended.sh tools/unattended/STOPS.template.md tools/unattended/VERBS.template.md tools/unattended/unattended.test.sh help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-20.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-20-1-acceptance-ledger.md

2026-11-19T13:48:59Z brief · item TOOL-dPlacedRequest-20 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-19T14:11:12Z draw · re-dispatch · TOOL-dPlacedRequest-20 · 10/130 · 20261119T141112Z-d0d1b8

2026-11-19T14:11:13Z dispatch · item cfc89088 TOOL-dPlacedRequest-20 · reason tools/unattended/unattended.sh tools/unattended/STOPS.template.md tools/unattended/VERBS.template.md tools/unattended/unattended.test.sh help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-20.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-20-1-acceptance-ledger.md memory/guides/UNATTENDED-STOPS.md memory/guides/UNATTENDED-VERBS.md

2026-11-19T14:26:42Z dispatch · item dcc88977 TOOL-dPlacedRequest-18 · reason tools/unattended/unattended.sh tools/unattended/STOPS.template.md tools/unattended/unattended.test.sh memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-18.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-18-1-acceptance-ledger.md

2026-11-19T14:28:49Z brief · item TOOL-dPlacedRequest-18 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-19T14:31:01Z draw · re-dispatch · TOOL-dPlacedRequest-18 · 11/130 · 20261119T143101Z-eb06c6

2026-11-19T14:31:01Z dispatch · item a7703198 TOOL-dPlacedRequest-18 · reason tools/unattended/unattended.sh tools/unattended/STOPS.template.md tools/unattended/unattended.test.sh memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-18.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-18-1-acceptance-ledger.md memory/guides/UNATTENDED-STOPS.md

2026-11-19T15:09:06Z dispatch · item 2a39cb16 TOOL-dPlacedRequest-28 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-28.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-28-1-acceptance-ledger.md

2026-11-19T15:27:58Z brief · item TOOL-dPlacedRequest-28 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T15:49:43Z dispatch · item 1150143f TOOL-dPlacedRequest-12 · reason tools/unattended/unattended.sh tools/unattended/VERBS.template.md tools/unattended/unattended.test.sh help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-12.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-12-1-acceptance-ledger.md memory/guides/UNATTENDED-VERBS.md

2026-11-19T15:55:02Z brief · item TOOL-dPlacedRequest-12 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-19T15:55:55Z draw · re-dispatch · TOOL-dPlacedRequest-12 · 12/130 · 20261119T155555Z-adcad6

2026-11-19T15:55:55Z dispatch · item 2125460b TOOL-dPlacedRequest-12 · reason tools/unattended/unattended.sh tools/unattended/VERBS.template.md tools/unattended/unattended.test.sh help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-12.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-12-1-acceptance-ledger.md memory/guides/UNATTENDED-VERBS.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt

2026-11-19T16:08:32Z dispatch · item 9047d651 TOOL-dPlacedRequest-42 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-42.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-42-1-acceptance-ledger.md

2026-11-19T16:10:09Z brief · item TOOL-dPlacedRequest-42 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T16:20:08Z dispatch · item 3ae0c204 TOOL-dPlacedRequest-15 · reason tools/push-main.sh tools/push-main.test.sh tools/unattended/unattended.sh tools/unattended/VERBS.template.md tools/unattended/unattended.test.sh memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-15.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-15-1-acceptance-ledger.md memory/guides/UNATTENDED-VERBS.md

2026-11-19T16:26:51Z brief · item TOOL-dPlacedRequest-15 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T16:54:39Z dispatch · item 1226835f TOOL-dPlacedRequest-19 · reason tools/loop/request.py tools/loop/kit.toml tools/loop/selftest.py tools/unattended/unattended.sh tools/unattended/VERBS.template.md tools/unattended/STOPS.template.md tools/unattended/unattended.test.sh help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-19.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-19-1-acceptance-ledger.md memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-STOPS.md
2026-11-19T17:10:11Z draw · re-dispatch · TOOL-dPlacedRequest-19 · 13/130 · 20261119T171011Z-e045ea

2026-11-19T17:10:11Z dispatch · item 4fc71184 TOOL-dPlacedRequest-19 · reason tools/loop/request.py tools/loop/kit.toml tools/loop/README.md tools/unattended/unattended.sh tools/unattended/VERBS.template.md tools/unattended/STOPS.template.md tools/unattended/unattended.test.sh tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv memory/map/features/loop.md tools/run-gates/selftest-budgets.txt help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-19.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-19-1-acceptance-ledger.md memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-STOPS.md

2026-11-19T17:11:23Z brief · item TOOL-dPlacedRequest-19 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-19T17:16:06Z draw · re-dispatch · TOOL-dPlacedRequest-19 · 14/130 · 20261119T171606Z-49b335

2026-11-19T17:16:06Z dispatch · item 689ef038 TOOL-dPlacedRequest-19 · reason tools/loop/request.py tools/loop/kit.toml tools/loop/README.md tools/unattended/unattended.sh tools/unattended/VERBS.template.md tools/unattended/STOPS.template.md tools/unattended/unattended.test.sh tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv memory/map/features/loop.md tools/run-gates/selftest-budgets.txt help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-19.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-19-1-acceptance-ledger.md memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-STOPS.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt
2026-11-19T17:26:27Z draw · re-dispatch · TOOL-dPlacedRequest-19 · 15/130 · 20261119T172627Z-595f6d

2026-11-19T17:26:27Z dispatch · item 689ef038 TOOL-dPlacedRequest-19 · reason tools/loop/request.py tools/loop/kit.toml tools/loop/README.md tools/unattended/unattended.sh tools/unattended/VERBS.template.md tools/unattended/STOPS.template.md tools/unattended/unattended.test.sh tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv memory/map/features/loop.md tools/run-gates/selftest-budgets.txt help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-19.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-19-1-acceptance-ledger.md memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-STOPS.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt memory/guides/SESSION-KICKOFF.md

2026-11-19T17:36:21Z dispatch · item 1e53c343 TOOL-dPlacedRequest-29 · reason tools/push-main.sh tools/push-main.test.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-29.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-29-1-acceptance-ledger.md

2026-11-19T17:38:02Z brief · item TOOL-dPlacedRequest-29 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T17:59:55Z dispatch · item d490d15f TOOL-dPlacedRequest-30 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-30.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-30-1-acceptance-ledger.md help/loop.md

2026-11-19T18:01:37Z brief · item TOOL-dPlacedRequest-30 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T18:15:01Z dispatch · item b6255b62 TOOL-dPlacedRequest-31 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-31.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-31-1-acceptance-ledger.md help/loop.md

2026-11-19T18:17:44Z brief · item TOOL-dPlacedRequest-31 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T18:28:32Z dispatch · item ae49ec18 TOOL-dPlacedRequest-32 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-32.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-32-1-acceptance-ledger.md help/loop.md

2026-11-19T18:33:20Z brief · item TOOL-dPlacedRequest-32 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-19T18:45:22Z draw · fix-pass · TOOL-dPlacedRequest-32 · 16/130 · 20261119T184522Z-e3dd15

2026-11-19T18:45:22Z dispatch · item cf01fc77 TOOL-dPlacedRequest-32 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-32.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-32-1-acceptance-ledger.md help/loop.md tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md

2026-11-19T18:53:08Z dispatch · item 5fdfe467 TOOL-dPlacedRequest-9 · reason tools/playbook/instruction_units.py tools/playbook/readers.toml tools/govkit/entries/kickoff-manifest.kit.toml tools/govkit/steps/kickoff_facts_to_overlay.py skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh skills/session-kickoff/MANIFEST-TEMPLATE.md skills/session-kickoff/SKILL.md memory/guides/SESSION-KICKOFF.md .governance/instructions.toml .governance/policy.json help/orientation-card.md help/README.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-9.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-9-1-acceptance-ledger.md

2026-11-19T18:59:14Z brief · item TOOL-dPlacedRequest-9 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-19T19:15:54Z draw · re-dispatch · TOOL-dPlacedRequest-9 · 17/130 · 20261119T191554Z-8c2a50

2026-11-19T19:15:54Z dispatch · item 100c1045 TOOL-dPlacedRequest-9 · reason tools/playbook/instruction_units.py tools/playbook/readers.toml tools/govkit/entries/kickoff-manifest.kit.toml tools/govkit/steps/kickoff_facts_to_overlay.py tools/govkit/selftest.py skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh skills/session-kickoff/MANIFEST-TEMPLATE.md skills/session-kickoff/SKILL.md help/upgrade-steps.md memory/guides/SESSION-KICKOFF.md .governance/instructions.toml .governance/policy.json help/orientation-card.md help/README.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-9.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-9-1-acceptance-ledger.md
2026-11-19T19:53:52Z draw · re-dispatch · TOOL-dPlacedRequest-9 · 18/130 · 20261119T195352Z-17766a

2026-11-19T19:53:53Z dispatch · item 0834babf TOOL-dPlacedRequest-9 · reason tools/playbook/instruction_units.py tools/playbook/readers.toml tools/govkit/entries/kickoff-manifest.kit.toml tools/govkit/steps/kickoff_facts_to_overlay.py tools/govkit/selftest.py skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh AGH8 K2 skills/session-kickoff/MANIFEST-TEMPLATE.md skills/session-kickoff/SKILL.md help/upgrade-steps.md memory/guides/SESSION-KICKOFF.md .governance/instructions.toml .governance/steps/kickoff-manifest/facts-to-overlay.before.json .governance/policy.json help/orientation-card.md help/README.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-9.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-9-1-acceptance-ledger.md
2026-11-19T19:55:01Z draw · re-dispatch · TOOL-dPlacedRequest-9 · 19/130 · 20261119T195501Z-5542f5

2026-11-19T19:55:01Z dispatch · item 0834babf TOOL-dPlacedRequest-9 · reason tools/playbook/instruction_units.py tools/playbook/readers.toml tools/govkit/entries/kickoff-manifest.kit.toml tools/govkit/steps/kickoff_facts_to_overlay.py tools/govkit/selftest.py skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh skills/session-kickoff/MANIFEST-TEMPLATE.md skills/session-kickoff/SKILL.md help/upgrade-steps.md memory/guides/SESSION-KICKOFF.md .governance/instructions.toml .governance/steps/kickoff-manifest/facts-to-overlay.before.json .governance/policy.json help/orientation-card.md help/README.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-9.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-9-1-acceptance-ledger.md
2026-11-19T20:27:58Z draw · fix-pass · TOOL-dPlacedRequest-9 · 20/130 · 20261119T202758Z-a25862

2026-11-19T20:27:58Z dispatch · item f96b1a0f TOOL-dPlacedRequest-9 · reason tools/playbook/instruction_units.py tools/playbook/readers.toml tools/govkit/entries/kickoff-manifest.kit.toml tools/govkit/steps/kickoff_facts_to_overlay.py tools/govkit/selftest.py skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh skills/session-kickoff/MANIFEST-TEMPLATE.md skills/session-kickoff/SKILL.md help/upgrade-steps.md memory/guides/SESSION-KICKOFF.md .governance/instructions.toml .governance/steps/kickoff-manifest/facts-to-overlay.before.json .governance/policy.json help/orientation-card.md help/README.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-9.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-9-1-acceptance-ledger.md
2026-11-19T20:30:01Z draw · fix-pass · TOOL-dPlacedRequest-9 · 21/130 · 20261119T203001Z-e492d2

2026-11-19T20:30:01Z dispatch · item cdabc971 TOOL-dPlacedRequest-9 · reason tools/playbook/instruction_units.py tools/playbook/readers.toml tools/govkit/entries/kickoff-manifest.kit.toml tools/govkit/steps/kickoff_facts_to_overlay.py tools/govkit/selftest.py skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh skills/session-kickoff/MANIFEST-TEMPLATE.md skills/session-kickoff/SKILL.md help/upgrade-steps.md memory/guides/SESSION-KICKOFF.md .governance/instructions.toml .governance/steps/kickoff-manifest/facts-to-overlay.before.json .governance/policy.json help/orientation-card.md help/README.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-9.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-9-1-acceptance-ledger.md

2026-11-19T20:48:59Z dispatch · item 91ce2580 TOOL-dPlacedRequest-2 · reason skills/session-kickoff/manifest-check.sh tools/lib/resolve-python.test.sh skills/session-kickoff/manifest-check.test.sh skills/session-kickoff/card-store.fixture.sh skills/session-kickoff/SKILL.md tools/hooks/scratch-guard.js tools/loop/loop_transition.py tools/memory-tree/build_records.py tools/memory-tree/tree_lib.py tools/memory-tree/HYGIENE.template.md tools/policy/catalogue.toml .governance/policy.json help/orientation-card.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-2.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-2-1-acceptance-ledger.md memory/HYGIENE.md

2026-11-19T20:56:10Z brief · item TOOL-dPlacedRequest-2 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-19T21:03:25Z draw · re-dispatch · TOOL-dPlacedRequest-2 · 22/130 · 20261119T210325Z-e63ffb

2026-11-19T21:03:25Z dispatch · item 4f6532a7 TOOL-dPlacedRequest-2 · reason skills/session-kickoff/manifest-check.sh tools/lib/resolve-python.test.sh skills/session-kickoff/manifest-check.test.sh skills/session-kickoff/card-store.fixture.sh skills/session-kickoff/SKILL.md tools/hooks/scratch-guard.js tools/loop/loop_transition.py tools/memory-tree/build_records.py tools/memory-tree/tree_lib.py tools/memory-tree/HYGIENE.template.md tools/policy/catalogue.toml .governance/policy.json help/orientation-card.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-2.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-2-1-acceptance-ledger.md memory/HYGIENE.md tools/hooks/scratch-guard.test.sh memory/guides/SESSION-KICKOFF.md
2026-11-19T21:22:33Z draw · re-dispatch · TOOL-dPlacedRequest-2 · 23/130 · 20261119T212233Z-892b8b

2026-11-19T21:22:33Z dispatch · item 4f6532a7 TOOL-dPlacedRequest-2 · reason skills/session-kickoff/manifest-check.sh tools/lib/resolve-python.test.sh skills/session-kickoff/manifest-check.test.sh skills/session-kickoff/card-store.fixture.sh skills/session-kickoff/SKILL.md tools/hooks/scratch-guard.js tools/loop/loop_transition.py tools/memory-tree/build_records.py tools/memory-tree/tree_lib.py tools/memory-tree/HYGIENE.template.md tools/policy/catalogue.toml .governance/policy.json help/orientation-card.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-2.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-2-1-acceptance-ledger.md memory/HYGIENE.md tools/hooks/scratch-guard.test.sh memory/guides/SESSION-KICKOFF.md tools/govkit/registry.toml
2026-11-19T21:42:28Z draw · fix-pass · TOOL-dPlacedRequest-2 · 24/130 · 20261119T214228Z-8745ab

2026-11-19T21:42:28Z dispatch · item f4fd1fc3 TOOL-dPlacedRequest-2 · reason skills/session-kickoff/manifest-check.sh tools/lib/resolve-python.test.sh skills/session-kickoff/manifest-check.test.sh skills/session-kickoff/card-store.fixture.sh skills/session-kickoff/SKILL.md tools/hooks/scratch-guard.js tools/loop/loop_transition.py tools/memory-tree/build_records.py tools/memory-tree/tree_lib.py tools/memory-tree/HYGIENE.template.md tools/policy/catalogue.toml .governance/policy.json help/orientation-card.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-2.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-2-1-acceptance-ledger.md memory/HYGIENE.md tools/hooks/scratch-guard.test.sh memory/guides/SESSION-KICKOFF.md tools/govkit/registry.toml

2026-11-19T21:46:09Z dispatch · item 989635a6 TOOL-dPlacedRequest-40 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-40.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-40-1-acceptance-ledger.md help/loop.md tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md

2026-11-19T21:49:07Z brief · item TOOL-dPlacedRequest-40 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T21:59:24Z dispatch · item cae9cb2d TOOL-dPlacedRequest-33 · reason skills/session-kickoff/manifest-check.sh skills/session-kickoff/card-store.fixture.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-33.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-33-1-acceptance-ledger.md
2026-11-19T22:15:11Z draw · re-dispatch · TOOL-dPlacedRequest-33 · 25/130 · 20261119T221511Z-f73f8f

2026-11-19T22:15:11Z dispatch · item f4012d32 TOOL-dPlacedRequest-33 · reason skills/session-kickoff/manifest-check.sh skills/session-kickoff/card-store.fixture.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-33.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-33-1-acceptance-ledger.md

2026-11-19T22:18:22Z brief · item TOOL-dPlacedRequest-33 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-19T22:21:05Z draw · re-dispatch · TOOL-dPlacedRequest-33 · 26/130 · 20261119T222105Z-59f87f

2026-11-19T22:21:05Z dispatch · item 64a6f71e TOOL-dPlacedRequest-33 · reason skills/session-kickoff/manifest-check.sh skills/session-kickoff/card-store.fixture.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-33.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-33-1-acceptance-ledger.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt
2026-11-19T22:35:36Z draw · re-dispatch · TOOL-dPlacedRequest-33 · 27/130 · 20261119T223536Z-41eadf

2026-11-19T22:35:36Z dispatch · item 64a6f71e TOOL-dPlacedRequest-33 · reason skills/session-kickoff/manifest-check.sh skills/session-kickoff/card-store.fixture.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-33.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-33-1-acceptance-ledger.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt skills/session-kickoff/manifest-check.test.sh tools/govkit/registry.toml
2026-11-19T22:39:20Z draw · re-dispatch · TOOL-dPlacedRequest-33 · 28/130 · 20261119T223920Z-24f365

2026-11-19T22:39:20Z dispatch · item 64a6f71e TOOL-dPlacedRequest-33 · reason skills/session-kickoff/manifest-check.sh skills/session-kickoff/card-store.fixture.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-33.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-33-1-acceptance-ledger.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt skills/session-kickoff/manifest-check.test.sh tools/govkit/registry.toml memory/guides/SESSION-KICKOFF.md
2026-11-19T22:41:40Z draw · fix-pass · TOOL-dPlacedRequest-33 · 29/130 · 20261119T224140Z-fc0645

2026-11-19T22:41:40Z dispatch · item be32c500 TOOL-dPlacedRequest-33 · reason skills/session-kickoff/manifest-check.sh skills/session-kickoff/card-store.fixture.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-33.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-33-1-acceptance-ledger.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt skills/session-kickoff/manifest-check.test.sh tools/govkit/registry.toml memory/guides/SESSION-KICKOFF.md help/orientation-card.md

2026-11-19T22:48:49Z dispatch · item 6c48fcb3 TOOL-dPlacedRequest-8 · reason memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-8.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-8-1-acceptance-ledger.md tools/loop/item-schema.toml tools/loop/loop.toml tools/loop/loop_lib.py tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md help/loop.md memory/map/generated
2026-11-19T23:02:25Z draw · re-dispatch · TOOL-dPlacedRequest-8 · 30/130 · 20261119T230225Z-b8bae8

2026-11-19T23:02:25Z dispatch · item d0206276 TOOL-dPlacedRequest-8 · reason .claude/skills/unattended/SKILL.md help/loop.md memory/guides/UNATTENDED-VERBS.md memory/map/generated tools/loop/item-schema.toml tools/loop/kit.toml tools/loop/loop.toml tools/loop/loop_lib.py tools/template-size-limits.txt tools/unattended/SKILL.template.md tools/unattended/VERBS.template.md tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-8.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-8-1-acceptance-ledger.md

2026-11-19T23:03:19Z brief · item TOOL-dPlacedRequest-8 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T23:26:51Z dispatch · item bceeb875 TOOL-dPlacedRequest-6 · reason tools/loop/loop.toml tools/loop/loop_lib.py help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-6.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-6-1-acceptance-ledger.md help/loop.md memory/map/generated tools/loop/loop.toml tools/loop/loop_lib.py tools/loop/item-schema.toml

2026-11-19T23:29:39Z brief · item TOOL-dPlacedRequest-6 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T23:44:58Z dispatch · item 22437921 TOOL-dPlacedRequest-7 · reason .governance/policy.json help/loop.md memory/HYGIENE.md memory/map/features/loop.md memory/map/generated tools/gate-legs.json tools/govkit/subject-pins.tsv tools/govkit/registry.toml tools/loop/kit.toml tools/loop/loop.toml tools/loop/loop_lib.py tools/loop/probe.py tools/memory-tree/HYGIENE.template.md tools/memory-tree/build_records.py tools/memory-tree/tree_lib.py tools/playbook/core-pending.txt tools/policy/catalogue.toml tools/run-gates/ceiling-evidence.txt tools/run-gates/selftest-budgets.txt memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-7.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-7-1-acceptance-ledger.md

2026-11-19T23:46:05Z brief · item TOOL-dPlacedRequest-7 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T00:01:25Z draw · re-dispatch · TOOL-dPlacedRequest-7 · 31/130 · 20261120T000125Z-2a6a16

2026-11-20T00:01:25Z dispatch · item 9dc27839 TOOL-dPlacedRequest-7 · reason .governance/policy.json help/loop.md memory/HYGIENE.md memory/map/features/loop.md memory/map/generated tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/loop/kit.toml tools/loop/loop.toml tools/loop/loop_lib.py tools/loop/probe.py tools/memory-tree/HYGIENE.template.md tools/memory-tree/build_records.py tools/memory-tree/tree_lib.py tools/playbook/core-pending.txt tools/policy/catalogue.toml tools/run-gates/ceiling-evidence.txt tools/run-gates/selftest-budgets.txt memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-7.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-7-1-acceptance-ledger.md
2026-11-20T00:17:05Z draw · re-dispatch · TOOL-dPlacedRequest-7 · 32/130 · 20261120T001705Z-5ad0f4

2026-11-20T00:17:05Z dispatch · item 2a0af97a TOOL-dPlacedRequest-7 · reason .governance/policy.json help/loop.md memory/HYGIENE.md memory/map/features/loop.md memory/map/generated tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/loop/kit.toml tools/loop/loop.toml tools/loop/loop_lib.py tools/loop/probe.py tools/memory-tree/HYGIENE.template.md tools/memory-tree/build_records.py tools/memory-tree/tree_lib.py tools/playbook/core-pending.txt tools/policy/catalogue.toml tools/run-gates/selftest-budgets.txt memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-7.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-7-1-acceptance-ledger.md
2026-11-20T00:40:16Z draw · re-dispatch · TOOL-dPlacedRequest-7 · 33/130 · 20261120T004016Z-683759

2026-11-20T00:40:16Z dispatch · item d78f9957 TOOL-dPlacedRequest-7 · reason .governance/policy.json help/loop.md memory/HYGIENE.md memory/map/features/loop.md memory/map/generated tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/loop/kit.toml tools/loop/loop.toml tools/loop/loop_lib.py tools/loop/probe.py tools/memory-tree/HYGIENE.template.md tools/memory-tree/build_records.py tools/memory-tree/tree_lib.py tools/playbook/core-pending.txt tools/policy/catalogue.toml tools/run-gates/selftest-budgets.txt memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-7.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-7-1-acceptance-ledger.md tools/loop/README.md
2026-11-20T00:43:04Z draw · re-dispatch · TOOL-dPlacedRequest-7 · 34/130 · 20261120T004304Z-ed5638

2026-11-20T00:43:04Z dispatch · item d78f9957 TOOL-dPlacedRequest-7 · reason .governance/policy.json help/loop.md memory/HYGIENE.md memory/map/features/loop.md memory/map/generated tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/loop/kit.toml tools/loop/loop.toml tools/loop/loop_lib.py tools/loop/probe.py tools/memory-tree/HYGIENE.template.md tools/memory-tree/build_records.py tools/memory-tree/tree_lib.py tools/playbook/core-pending.txt tools/policy/catalogue.toml tools/run-gates/selftest-budgets.txt memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-7.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-7-1-acceptance-ledger.md tools/loop/README.md memory/guides/SESSION-KICKOFF.md memory/LIVE.md memory/builds/dPlacedRequest/README.md
2026-11-20T00:55:29Z draw · fix-pass · TOOL-dPlacedRequest-7 · 35/130 · 20261120T005529Z-394fe9

2026-11-20T00:55:29Z dispatch · item 67814212 TOOL-dPlacedRequest-7 · reason .governance/policy.json help/loop.md memory/HYGIENE.md memory/map/features/loop.md memory/map/generated tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/loop/kit.toml tools/loop/loop.toml tools/loop/loop_lib.py tools/loop/probe.py tools/memory-tree/HYGIENE.template.md tools/memory-tree/build_records.py tools/memory-tree/tree_lib.py tools/playbook/core-pending.txt tools/policy/catalogue.toml tools/run-gates/selftest-budgets.txt memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-7.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-7-1-acceptance-ledger.md tools/loop/README.md memory/guides/SESSION-KICKOFF.md memory/LIVE.md memory/builds/dPlacedRequest/README.md memory/backlog/TOOL.md

2026-11-20T01:01:11Z dispatch · item fc2c79f2 TOOL-dPlacedRequest-4 · reason .claude/agents/gov-orienter.md help/loop.md memory/guides/UNATTENDED-VERBS.md memory/map/generated tools/gate-legs.json tools/loop/kit.toml tools/loop/placement.py tools/playbook/core-pending.txt tools/roles/README.md tools/roles/agents/gov-orienter.agent.md tools/unattended/VERBS.template.md tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/run-gates/selftest-budgets.txt memory/map/features/loop.md memory/guides/SESSION-KICKOFF.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-4.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-4-1-acceptance-ledger.md

2026-11-20T01:20:58Z brief · item TOOL-dPlacedRequest-4 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-20T01:41:24Z dispatch · item 053c89c7 TOOL-dPlacedRequest-10 · reason tools/loop/placement.py tools/roles/agents/gov-orienter.agent.md .claude/agents/gov-orienter.md tools/roles/README.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-10.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-10-1-acceptance-ledger.md

2026-11-20T01:45:16Z brief · item TOOL-dPlacedRequest-10 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-20T01:58:30Z dispatch · item de35faa4 TOOL-dPlacedRequest-14 · reason tools/loop/budget.py tools/loop/placement.py tools/unattended/unattended.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-14.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-14-1-acceptance-ledger.md tools/unattended/unattended.test.sh

2026-11-20T02:04:36Z brief · item TOOL-dPlacedRequest-14 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T02:05:44Z draw · re-dispatch · TOOL-dPlacedRequest-14 · 36/130 · 20261120T020544Z-d65a8d

2026-11-20T02:05:44Z dispatch · item 7dc12c12 TOOL-dPlacedRequest-14 · reason tools/loop/budget.py tools/loop/placement.py tools/unattended/unattended.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-14.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-14-1-acceptance-ledger.md tools/unattended/unattended.test.sh tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt
2026-11-20T02:30:53Z draw · fix-pass · TOOL-dPlacedRequest-14 · 37/130 · 20261120T023053Z-f7aed5

2026-11-20T02:30:53Z dispatch · item 83c1e065 TOOL-dPlacedRequest-14 · reason tools/loop/budget.py tools/loop/placement.py tools/unattended/unattended.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-14.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-14-1-acceptance-ledger.md tools/unattended/unattended.test.sh tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt

2026-11-20T02:35:25Z dispatch · item 8f242b3c TOOL-dPlacedRequest-5 · reason tools/loop/placement.py tools/loop/breakpoints.py tools/unattended/unattended.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-5.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-5-1-acceptance-ledger.md tools/unattended/unattended.test.sh

2026-11-20T02:39:40Z brief · item TOOL-dPlacedRequest-5 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T02:40:42Z draw · re-dispatch · TOOL-dPlacedRequest-5 · 38/130 · 20261120T024042Z-504d22

2026-11-20T02:40:43Z dispatch · item 7775ef41 TOOL-dPlacedRequest-5 · reason tools/loop/placement.py tools/loop/breakpoints.py tools/unattended/unattended.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-5.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-5-1-acceptance-ledger.md tools/unattended/unattended.test.sh tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt
2026-11-20T02:55:05Z draw · re-dispatch · TOOL-dPlacedRequest-5 · 39/130 · 20261120T025505Z-41d564

2026-11-20T02:55:05Z dispatch · item 7775ef41 TOOL-dPlacedRequest-5 · reason tools/loop/placement.py tools/loop/breakpoints.py tools/unattended/unattended.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-5.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-5-1-acceptance-ledger.md tools/unattended/unattended.test.sh tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt help/spec-audit.md
2026-11-20T03:03:50Z draw · fix-pass · TOOL-dPlacedRequest-5 · 40/130 · 20261120T030350Z-d2920b

2026-11-20T03:03:50Z dispatch · item 63b9ab7a TOOL-dPlacedRequest-5 · reason tools/loop/placement.py tools/loop/breakpoints.py tools/unattended/unattended.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-5.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-5-1-acceptance-ledger.md tools/unattended/unattended.test.sh tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt help/spec-audit.md

2026-11-20T03:10:40Z dispatch · item 2490e291 TOOL-dPlacedRequest-21 · reason tools/loop/claim.py tools/loop/loop_transition.py tools/loop/kit.toml tools/gate-legs.json tools/playbook/core-pending.txt tools/unattended/unattended.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md tools/memory-tree/gen_build_index.py help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-21.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-21-1-acceptance-ledger.md tools/unattended/unattended.test.sh tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/run-gates/selftest-budgets.txt memory/map/features/loop.md memory/guides/SESSION-KICKOFF.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt

2026-11-20T03:14:22Z brief · item TOOL-dPlacedRequest-21 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T03:25:13Z draw · re-dispatch · TOOL-dPlacedRequest-21 · 41/130 · 20261120T032513Z-49a62c

2026-11-20T03:25:13Z dispatch · item e1e161b3 TOOL-dPlacedRequest-21 · reason tools/loop/claim.py tools/loop/loop_transition.py tools/loop/kit.toml tools/gate-legs.json tools/playbook/core-pending.txt tools/unattended/unattended.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md tools/memory-tree/gen_build_index.py help/loop.md memory/map/generated tools/unattended/unattended.test.sh tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/run-gates/selftest-budgets.txt memory/map/features/loop.md memory/guides/SESSION-KICKOFF.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-21.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-21-1-acceptance-ledger.md

2026-11-20T04:24:50Z dispatch · item f00fddaf TOOL-dPlacedRequest-3 · reason tools/loop/loop.toml tools/loop/loop_lib.py skills/session-kickoff/SKILL.md memory/guides/SESSION-KICKOFF.md help/loop.md memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-3.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-3-1-acceptance-ledger.md

2026-11-20T04:26:48Z brief · item TOOL-dPlacedRequest-3 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T04:36:28Z draw · fix-pass · TOOL-dPlacedRequest-3 · 42/130 · 20261120T043628Z-acc1de

2026-11-20T04:36:28Z dispatch · item f7e1d444 TOOL-dPlacedRequest-3 · reason tools/loop/loop.toml tools/loop/loop_lib.py skills/session-kickoff/SKILL.md memory/guides/SESSION-KICKOFF.md help/loop.md memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-3.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-3-1-acceptance-ledger.md tools/loop/README.md

2026-11-20T04:41:09Z dispatch · item 57e93607 TOOL-dPlacedRequest-34 · reason tools/lib/gov-feed.sh tools/lib/gov-ref.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/resume-tick.test.sh tools/unattended/.unattended.conf.example tools/unattended/PROTOCOL.template.md tools/unattended/VERBS.template.md tools/unattended/STOPS.template.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-STOPS.md tools/run-gates/post-merge.sh tools/push-main.sh tools/push-main.test.sh .githooks/pre-push tools/hooks/scratch-guard.js tools/hooks/scratch-guard.test.sh skills/session-kickoff/manifest-check.sh skills/session-kickoff/card-store.fixture.sh skills/session-kickoff/SKILL.md skills/session-kickoff/RESUME.md tools/playbook/render_playbook.py tools/loop/loop_lib.py tools/loop/request.py tools/loop/placement.py tools/loop/budget.py tools/loop/claim.py tools/loop/probe.py tools/loop/loop.toml tools/govkit/steps/kickoff_facts_to_overlay.py .githooks/pre-push.test.sh tools/gate-legs.json tools/run-gates/selftest-budgets.txt tools/govkit/subject-pins.tsv memory/map/features/loop.md memory/map/features/unattended-stops.md memory/gotchas/decision-re-derived-by-a-second-process.md memory/map/generated/symbols.json tools/lib/resolve-python.test.sh help/loop.md memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-34-1-acceptance-ledger.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt tools/govkit/registry.toml memory/guides/SESSION-KICKOFF.md

2026-11-20T04:43:12Z brief · item TOOL-dPlacedRequest-34 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T05:10:54Z draw · re-dispatch · TOOL-dPlacedRequest-34 · 43/130 · 20261120T051054Z-24d423

2026-11-20T05:10:54Z dispatch · item 52d334e8 TOOL-dPlacedRequest-34 · reason tools/lib/gov-feed.sh tools/lib/gov-ref.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/resume-tick.test.sh tools/unattended/.unattended.conf.example tools/unattended/PROTOCOL.template.md tools/unattended/VERBS.template.md tools/unattended/STOPS.template.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-STOPS.md tools/run-gates/post-merge.sh tools/push-main.sh tools/push-main.test.sh .githooks/pre-push tools/hooks/scratch-guard.js tools/hooks/scratch-guard.test.sh skills/session-kickoff/manifest-check.sh skills/session-kickoff/card-store.fixture.sh skills/session-kickoff/SKILL.md skills/session-kickoff/RESUME.md tools/playbook/render_playbook.py tools/loop/loop_lib.py tools/loop/request.py tools/loop/placement.py tools/loop/budget.py tools/loop/claim.py tools/loop/probe.py tools/loop/loop.toml tools/govkit/steps/kickoff_facts_to_overlay.py .githooks/pre-push.test.sh tools/gate-legs.json tools/run-gates/selftest-budgets.txt tools/govkit/subject-pins.tsv memory/map/features/loop.md memory/map/features/unattended-stops.md memory/gotchas/decision-re-derived-by-a-second-process.md memory/map/generated/symbols.json tools/lib/resolve-python.test.sh help/loop.md memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-34-1-acceptance-ledger.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt tools/govkit/registry.toml memory/guides/SESSION-KICKOFF.md tools/unattended/lib-unattended.sh .unattended.conf tools/loop/README.md
2026-11-20T05:14:37Z draw · re-dispatch · TOOL-dPlacedRequest-34 · 44/130 · 20261120T051437Z-c05755

2026-11-20T05:14:37Z dispatch · item 52d334e8 TOOL-dPlacedRequest-34 · reason tools/lib/gov-feed.sh tools/lib/gov-ref.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/resume-tick.test.sh tools/unattended/.unattended.conf.example tools/unattended/PROTOCOL.template.md tools/unattended/VERBS.template.md tools/unattended/STOPS.template.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-STOPS.md tools/run-gates/post-merge.sh tools/push-main.sh tools/push-main.test.sh .githooks/pre-push tools/hooks/scratch-guard.js tools/hooks/scratch-guard.test.sh skills/session-kickoff/manifest-check.sh skills/session-kickoff/card-store.fixture.sh skills/session-kickoff/SKILL.md skills/session-kickoff/RESUME.md tools/playbook/render_playbook.py tools/loop/loop_lib.py tools/loop/request.py tools/loop/placement.py tools/loop/budget.py tools/loop/claim.py tools/loop/probe.py tools/loop/loop.toml tools/govkit/steps/kickoff_facts_to_overlay.py .githooks/pre-push.test.sh tools/gate-legs.json tools/run-gates/selftest-budgets.txt tools/govkit/subject-pins.tsv memory/map/features/loop.md memory/map/features/unattended-stops.md memory/gotchas/decision-re-derived-by-a-second-process.md memory/map/generated/symbols.json tools/lib/resolve-python.test.sh help/loop.md memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-34-1-acceptance-ledger.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt tools/govkit/registry.toml memory/guides/SESSION-KICKOFF.md tools/unattended/lib-unattended.sh .unattended.conf tools/loop/README.md tools/loop/loop_items.py
2026-11-20T05:21:10Z draw · fix-pass · TOOL-dPlacedRequest-34 · 45/130 · 20261120T052110Z-8b1acb

2026-11-20T05:21:10Z dispatch · item dbfe3805 TOOL-dPlacedRequest-34 · reason tools/lib/gov-feed.sh tools/lib/gov-ref.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/resume-tick.test.sh tools/unattended/.unattended.conf.example tools/unattended/PROTOCOL.template.md tools/unattended/VERBS.template.md tools/unattended/STOPS.template.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-STOPS.md tools/run-gates/post-merge.sh tools/push-main.sh tools/push-main.test.sh .githooks/pre-push tools/hooks/scratch-guard.js tools/hooks/scratch-guard.test.sh skills/session-kickoff/manifest-check.sh skills/session-kickoff/card-store.fixture.sh skills/session-kickoff/SKILL.md skills/session-kickoff/RESUME.md tools/playbook/render_playbook.py tools/loop/loop_lib.py tools/loop/request.py tools/loop/placement.py tools/loop/budget.py tools/loop/claim.py tools/loop/probe.py tools/loop/loop.toml tools/govkit/steps/kickoff_facts_to_overlay.py .githooks/pre-push.test.sh tools/gate-legs.json tools/run-gates/selftest-budgets.txt tools/govkit/subject-pins.tsv memory/map/features/loop.md memory/map/features/unattended-stops.md memory/gotchas/decision-re-derived-by-a-second-process.md memory/map/generated/symbols.json tools/lib/resolve-python.test.sh help/loop.md memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-34-1-acceptance-ledger.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt tools/govkit/registry.toml memory/guides/SESSION-KICKOFF.md tools/unattended/lib-unattended.sh .unattended.conf tools/loop/README.md tools/loop/loop_items.py help/orientation-card.md
2026-11-20T05:34:10Z draw · fix-pass · TOOL-dPlacedRequest-34 · 46/130 · 20261120T053410Z-997570

2026-11-20T05:34:10Z dispatch · item 75ac39bb TOOL-dPlacedRequest-34 · reason tools/lib/gov-feed.sh tools/lib/gov-ref.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/resume-tick.test.sh tools/unattended/.unattended.conf.example tools/unattended/PROTOCOL.template.md tools/unattended/VERBS.template.md tools/unattended/STOPS.template.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-STOPS.md tools/run-gates/post-merge.sh tools/push-main.sh tools/push-main.test.sh .githooks/pre-push tools/hooks/scratch-guard.js tools/hooks/scratch-guard.test.sh skills/session-kickoff/manifest-check.sh skills/session-kickoff/card-store.fixture.sh skills/session-kickoff/SKILL.md skills/session-kickoff/RESUME.md tools/playbook/render_playbook.py tools/loop/loop_lib.py tools/loop/request.py tools/loop/placement.py tools/loop/budget.py tools/loop/claim.py tools/loop/probe.py tools/loop/loop.toml tools/govkit/steps/kickoff_facts_to_overlay.py .githooks/pre-push.test.sh tools/gate-legs.json tools/run-gates/selftest-budgets.txt tools/govkit/subject-pins.tsv memory/map/features/loop.md memory/map/features/unattended-stops.md memory/gotchas/decision-re-derived-by-a-second-process.md memory/map/generated/symbols.json tools/lib/resolve-python.test.sh help/loop.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt tools/govkit/registry.toml memory/guides/SESSION-KICKOFF.md tools/hooks/scratch-guard.test.sh memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-34-1-acceptance-ledger.md

2026-11-20T06:04:05Z dispatch · item 1141217d TOOL-dPlacedRequest-35 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/map/generated tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-35.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-35-1-acceptance-ledger.md

2026-11-20T06:05:25Z brief · item TOOL-dPlacedRequest-35 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-20T06:14:45Z dispatch · item 36666a1f TOOL-dPlacedRequest-46 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-46.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-46-1-acceptance-ledger.md

2026-11-20T06:17:08Z brief · item TOOL-dPlacedRequest-46 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
