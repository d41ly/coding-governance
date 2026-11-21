# dPlacedRequest - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gates-run: unattended-17952593412338706263-496420 bfa5f311
parked-surfaced: yes
keepalive-reaped: yes
asks-at-landing: TOOL-dPlacedRequest-22=OPEN TOOL-dPlacedRequest-65=CLOSED TOOL-dPlacedRequest-66=CLOSED TOOL-dPlacedRequest-67=CLOSED TOOL-dPlacedRequest-68=CLOSED TOOL-dPlacedRequest-69=CLOSED TOOL-dPlacedRequest-70=CLOSED TOOL-dPlacedRequest-71=CLOSED TOOL-dPlacedRequest-73=CLOSED TOOL-dPlacedRequest-74=OPEN TOOL-dPlacedRequest-75=OPEN TOOL-dPlacedRequest-76=OPEN TOOL-dPlacedRequest-77=OPEN TOOL-dPlacedRequest-78=OPEN TOOL-dPlacedRequest-79=OPEN TOOL-dPlacedRequest-80=OPEN TOOL-dPlacedRequest-81=OPEN TOOL-dPlacedRequest-82=OPEN TOOL-dPlacedRequest-83=OPEN TOOL-dPlacedRequest-84=WONTDO TOOL-dPlacedRequest-85=WONTDO TOOL-dPlacedRequest-86=WONTDO TOOL-dPlacedRequest-87=OPEN TOOL-dPlacedRequest-88=WONTDO TOOL-dPlacedRequest-89=WONTDO TOOL-dPlacedRequest-90=OPEN TOOL-dPlacedRequest-91=WONTDO TOOL-dPlacedRequest-92=WONTDO TOOL-dPlacedRequest-93=WONTDO TOOL-dPlacedRequest-94=WONTDO TOOL-dPlacedRequest-101=WONTDO TOOL-dPlacedRequest-102=OPEN TOOL-dPlacedRequest-103=OPEN TOOL-dPlacedRequest-104=WONTDO TOOL-dPlacedRequest-105=OPEN TOOL-dPlacedRequest-106=WONTDO TOOL-dPlacedRequest-107=WONTDO TOOL-dPlacedRequest-108=WONTDO TOOL-dPlacedRequest-109=OPEN TOOL-dPlacedRequest-110=OPEN
units-at-landing: TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 TOOL-dPlacedRequest-95 TOOL-dPlacedRequest-96 TOOL-dPlacedRequest-97 TOOL-dPlacedRequest-98 TOOL-dPlacedRequest-99 TOOL-dPlacedRequest-100
hold-run: 
hold-streak: 1 · at da3dc3ea
resume-owed: none · owner
held-at: 2026-11-21T09:12:26Z
hold-reason: the landing's pre-push routed-commits range refuses six earlier Red-fix commits outside the inline lane's limits (parked: routed-commits-lane-limits); every other red the run caused is fixed and 21 inherited reds remain, each held red on main's daily job with an open ask
hold-until: owner
hold-code: owner-decision
held-from: VERIFYING
refreshed-at: 4a7fff390790a4d5debec6bf77fd27661ba9a2da · handoff · 0 touching
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 6b3ebc8308414624d538f94e36d218eb9771af48
phase: VERIFYING
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dplacedrequest-42a7be
anchor-kind: default-branch
cli-version: 2.1.326
lease-utc: 2026-11-21T11:07:06Z
pid-image: claude.exe
host: compeeto
pid: 27268
session: dec54915-9f6d-416a-abf5-d4658b7ca977
keepalive: 2439436f
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

2026-11-19T08:04:18Z dispatch · item b34330ca TOOL-dPlacedRequest-1 · reason tools/unattended/unattended.sh tools/unattended/lib-unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt tools/playbook/render_playbook.py skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh help/loop.md memory/map/generated tools/govkit/subject-pins.tsv memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-1.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-1-1-acceptance-ledger.md

2026-11-19T08:07:38Z brief · item TOOL-dPlacedRequest-1 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T08:55:29Z dispatch · item 45d59991 TOOL-dPlacedRequest-27 · reason tools/lib/gov-feed.sh tools/unattended/unattended.sh tools/run-gates/post-merge.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-27.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-27-1-acceptance-ledger.md

2026-11-19T08:57:08Z brief · item TOOL-dPlacedRequest-27 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T09:06:17Z dispatch · item 6edaf99b TOOL-dPlacedRequest-17 · reason tools/lib/gov-feed.sh tools/unattended/unattended.sh tools/run-gates/post-merge.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md tools/govkit/subject-pins.tsv memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-17.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-17-1-acceptance-ledger.md

2026-11-19T09:17:21Z brief · item TOOL-dPlacedRequest-17 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T09:41:29Z dispatch · item 7a5d1987 TOOL-dPlacedRequest-23 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-23.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-23-1-acceptance-ledger.md

2026-11-19T09:43:47Z brief · item TOOL-dPlacedRequest-23 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T09:53:15Z dispatch · item d1ef94ba TOOL-dPlacedRequest-24 · reason tools/lib/gov-feed.sh tools/unattended/unattended.sh tools/run-gates/post-merge.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md tools/unattended/README.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-24.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-24-1-acceptance-ledger.md

2026-11-19T10:21:17Z brief · item TOOL-dPlacedRequest-24 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T10:31:09Z dispatch · item fb6691ef TOOL-dPlacedRequest-25 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-25.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-25-1-acceptance-ledger.md

2026-11-19T10:33:59Z brief · item TOOL-dPlacedRequest-25 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T10:45:59Z dispatch · item 917222bb TOOL-dPlacedRequest-16 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh help/loop.md memory/map/generated tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md tools/loop/budget.py tools/govkit/subject-pins.tsv memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-16.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-16-1-acceptance-ledger.md

2026-11-19T11:15:25Z brief · item TOOL-dPlacedRequest-16 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-19T11:16:19Z draw · re-dispatch · TOOL-dPlacedRequest-16 · 5/130 · 20261119T111619Z-280c9d

2026-11-19T11:16:19Z dispatch · item 675237ee TOOL-dPlacedRequest-16 · reason skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh memory/guides/SESSION-KICKOFF.md
2026-11-19T11:49:25Z draw · re-dispatch · TOOL-dPlacedRequest-16 · 6/130 · 20261119T114925Z-f7c57c

2026-11-19T11:49:25Z dispatch · item 675237ee TOOL-dPlacedRequest-16 · reason skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh memory/guides/SESSION-KICKOFF.md help/loop.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-16-1-acceptance-ledger.md memory/guides/UNATTENDED-STOPS.md tools/unattended/STOPS.template.md tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/map/generated tools/govkit/subject-pins.tsv
2026-11-19T11:56:24Z draw · fix-pass · TOOL-dPlacedRequest-16 · 7/130 · 20261119T115624Z-480c57

2026-11-19T11:56:24Z dispatch · item c29e05fc TOOL-dPlacedRequest-16 · reason tools/unattended/unattended.test.sh memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-16-1-acceptance-ledger.md memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-16.md

2026-11-19T12:03:00Z dispatch · item 1f3742a0 TOOL-dPlacedRequest-26 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-26.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-26-1-acceptance-ledger.md

2026-11-19T12:04:51Z brief · item TOOL-dPlacedRequest-26 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T12:15:33Z dispatch · item 34ceebb9 TOOL-dPlacedRequest-36 · reason tools/lib/gov-feed.sh tools/unattended/unattended.sh tools/run-gates/post-merge.sh tools/unattended/unattended.test.sh memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-36.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-36-1-acceptance-ledger.md

2026-11-19T12:17:28Z brief · item TOOL-dPlacedRequest-36 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T12:28:23Z dispatch · item 56b2f9af TOOL-dPlacedRequest-37 · reason tools/lib/gov-feed.sh tools/unattended/unattended.sh tools/run-gates/post-merge.sh tools/unattended/unattended.test.sh memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-37.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-37-1-acceptance-ledger.md

2026-11-19T12:30:43Z brief · item TOOL-dPlacedRequest-37 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T12:40:14Z dispatch · item 3a060d14 TOOL-dPlacedRequest-38 · reason tools/lib/resolve-python.test.sh memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-38.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-38-1-acceptance-ledger.md

2026-11-19T12:43:06Z brief · item TOOL-dPlacedRequest-38 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T12:58:57Z dispatch · item 1121a9d9 TOOL-dPlacedRequest-39 · reason tools/lib/gov-feed.sh tools/unattended/unattended.sh tools/run-gates/post-merge.sh tools/unattended/unattended.test.sh memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-39.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-39-1-acceptance-ledger.md

2026-11-19T13:03:26Z brief · item TOOL-dPlacedRequest-39 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-19T13:04:39Z draw · re-dispatch · TOOL-dPlacedRequest-39 · 8/130 · 20261119T130439Z-0d8786

2026-11-19T13:04:39Z dispatch · item 7af14438 TOOL-dPlacedRequest-39 · reason tools/lib/resolve-python.test.sh
2026-11-19T13:12:10Z draw · re-dispatch · TOOL-dPlacedRequest-39 · 9/130 · 20261119T131210Z-d01894

2026-11-19T13:12:10Z dispatch · item 7af14438 TOOL-dPlacedRequest-39 · reason tools/lib/resolve-python.test.sh memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-39-1-acceptance-ledger.md tools/lib/gov-feed.sh tools/run-gates/post-merge.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-39.md

2026-11-19T13:21:14Z dispatch · item 615abc9e TOOL-dPlacedRequest-41 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-41.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-41-1-acceptance-ledger.md

2026-11-19T13:23:22Z brief · item TOOL-dPlacedRequest-41 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T13:47:10Z dispatch · item 03c82f55 TOOL-dPlacedRequest-20 · reason tools/unattended/unattended.sh tools/unattended/STOPS.template.md tools/unattended/VERBS.template.md tools/unattended/unattended.test.sh help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-20.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-20-1-acceptance-ledger.md

2026-11-19T13:48:59Z brief · item TOOL-dPlacedRequest-20 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-19T14:11:12Z draw · re-dispatch · TOOL-dPlacedRequest-20 · 10/130 · 20261119T141112Z-d0d1b8

2026-11-19T14:11:13Z dispatch · item 8ce867dc TOOL-dPlacedRequest-20 · reason tools/unattended/unattended.sh tools/unattended/STOPS.template.md tools/unattended/VERBS.template.md tools/unattended/unattended.test.sh help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-20.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-20-1-acceptance-ledger.md memory/guides/UNATTENDED-STOPS.md memory/guides/UNATTENDED-VERBS.md

2026-11-19T14:26:42Z dispatch · item 62e752c5 TOOL-dPlacedRequest-18 · reason tools/unattended/unattended.sh tools/unattended/STOPS.template.md tools/unattended/unattended.test.sh memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-18.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-18-1-acceptance-ledger.md

2026-11-19T14:28:49Z brief · item TOOL-dPlacedRequest-18 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-19T14:31:01Z draw · re-dispatch · TOOL-dPlacedRequest-18 · 11/130 · 20261119T143101Z-eb06c6

2026-11-19T14:31:01Z dispatch · item b3c3f715 TOOL-dPlacedRequest-18 · reason tools/unattended/unattended.sh tools/unattended/STOPS.template.md tools/unattended/unattended.test.sh memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-18.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-18-1-acceptance-ledger.md memory/guides/UNATTENDED-STOPS.md

2026-11-19T15:09:06Z dispatch · item 4cfcf56b TOOL-dPlacedRequest-28 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-28.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-28-1-acceptance-ledger.md

2026-11-19T15:27:58Z brief · item TOOL-dPlacedRequest-28 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T15:49:43Z dispatch · item 51f85852 TOOL-dPlacedRequest-12 · reason tools/unattended/unattended.sh tools/unattended/VERBS.template.md tools/unattended/unattended.test.sh help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-12.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-12-1-acceptance-ledger.md memory/guides/UNATTENDED-VERBS.md

2026-11-19T15:55:02Z brief · item TOOL-dPlacedRequest-12 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-19T15:55:55Z draw · re-dispatch · TOOL-dPlacedRequest-12 · 12/130 · 20261119T155555Z-adcad6

2026-11-19T15:55:55Z dispatch · item 0e62fd84 TOOL-dPlacedRequest-12 · reason tools/unattended/unattended.sh tools/unattended/VERBS.template.md tools/unattended/unattended.test.sh help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-12.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-12-1-acceptance-ledger.md memory/guides/UNATTENDED-VERBS.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt

2026-11-19T16:08:32Z dispatch · item 02b9dc08 TOOL-dPlacedRequest-42 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-42.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-42-1-acceptance-ledger.md

2026-11-19T16:10:09Z brief · item TOOL-dPlacedRequest-42 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T16:20:08Z dispatch · item c3ffe872 TOOL-dPlacedRequest-15 · reason tools/push-main.sh tools/push-main.test.sh tools/unattended/unattended.sh tools/unattended/VERBS.template.md tools/unattended/unattended.test.sh memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-15.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-15-1-acceptance-ledger.md memory/guides/UNATTENDED-VERBS.md

2026-11-19T16:26:51Z brief · item TOOL-dPlacedRequest-15 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T16:54:39Z dispatch · item 60df6910 TOOL-dPlacedRequest-19 · reason tools/loop/request.py tools/loop/kit.toml tools/loop/selftest.py tools/unattended/unattended.sh tools/unattended/VERBS.template.md tools/unattended/STOPS.template.md tools/unattended/unattended.test.sh help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-19.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-19-1-acceptance-ledger.md memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-STOPS.md
2026-11-19T17:10:11Z draw · re-dispatch · TOOL-dPlacedRequest-19 · 13/130 · 20261119T171011Z-e045ea

2026-11-19T17:10:11Z dispatch · item 7ac71f3f TOOL-dPlacedRequest-19 · reason tools/loop/request.py tools/loop/kit.toml tools/loop/README.md tools/unattended/unattended.sh tools/unattended/VERBS.template.md tools/unattended/STOPS.template.md tools/unattended/unattended.test.sh tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv memory/map/features/loop.md tools/run-gates/selftest-budgets.txt help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-19.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-19-1-acceptance-ledger.md memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-STOPS.md

2026-11-19T17:11:23Z brief · item TOOL-dPlacedRequest-19 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-19T17:16:06Z draw · re-dispatch · TOOL-dPlacedRequest-19 · 14/130 · 20261119T171606Z-49b335

2026-11-19T17:16:06Z dispatch · item 0dd2d5fc TOOL-dPlacedRequest-19 · reason tools/loop/request.py tools/loop/kit.toml tools/loop/README.md tools/unattended/unattended.sh tools/unattended/VERBS.template.md tools/unattended/STOPS.template.md tools/unattended/unattended.test.sh tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv memory/map/features/loop.md tools/run-gates/selftest-budgets.txt help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-19.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-19-1-acceptance-ledger.md memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-STOPS.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt
2026-11-19T17:26:27Z draw · re-dispatch · TOOL-dPlacedRequest-19 · 15/130 · 20261119T172627Z-595f6d

2026-11-19T17:26:27Z dispatch · item 0dd2d5fc TOOL-dPlacedRequest-19 · reason tools/loop/request.py tools/loop/kit.toml tools/loop/README.md tools/unattended/unattended.sh tools/unattended/VERBS.template.md tools/unattended/STOPS.template.md tools/unattended/unattended.test.sh tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv memory/map/features/loop.md tools/run-gates/selftest-budgets.txt help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-19.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-19-1-acceptance-ledger.md memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-STOPS.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt memory/guides/SESSION-KICKOFF.md

2026-11-19T17:36:21Z dispatch · item d3e7f8e1 TOOL-dPlacedRequest-29 · reason tools/push-main.sh tools/push-main.test.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-29.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-29-1-acceptance-ledger.md

2026-11-19T17:38:02Z brief · item TOOL-dPlacedRequest-29 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T17:59:55Z dispatch · item 08987e05 TOOL-dPlacedRequest-30 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-30.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-30-1-acceptance-ledger.md help/loop.md

2026-11-19T18:01:37Z brief · item TOOL-dPlacedRequest-30 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T18:15:01Z dispatch · item 23ac1488 TOOL-dPlacedRequest-31 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-31.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-31-1-acceptance-ledger.md help/loop.md

2026-11-19T18:17:44Z brief · item TOOL-dPlacedRequest-31 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T18:28:32Z dispatch · item 0572d812 TOOL-dPlacedRequest-32 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-32.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-32-1-acceptance-ledger.md help/loop.md

2026-11-19T18:33:20Z brief · item TOOL-dPlacedRequest-32 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-19T18:45:22Z draw · fix-pass · TOOL-dPlacedRequest-32 · 16/130 · 20261119T184522Z-e3dd15

2026-11-19T18:45:22Z dispatch · item b822de43 TOOL-dPlacedRequest-32 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-32.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-32-1-acceptance-ledger.md help/loop.md tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md

2026-11-19T18:53:08Z dispatch · item a201620e TOOL-dPlacedRequest-9 · reason tools/playbook/instruction_units.py tools/playbook/readers.toml tools/govkit/entries/kickoff-manifest.kit.toml tools/govkit/steps/kickoff_facts_to_overlay.py skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh skills/session-kickoff/MANIFEST-TEMPLATE.md skills/session-kickoff/SKILL.md memory/guides/SESSION-KICKOFF.md .governance/instructions.toml .governance/policy.json help/orientation-card.md help/README.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-9.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-9-1-acceptance-ledger.md

2026-11-19T18:59:14Z brief · item TOOL-dPlacedRequest-9 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-19T19:15:54Z draw · re-dispatch · TOOL-dPlacedRequest-9 · 17/130 · 20261119T191554Z-8c2a50

2026-11-19T19:15:54Z dispatch · item 355b2418 TOOL-dPlacedRequest-9 · reason tools/playbook/instruction_units.py tools/playbook/readers.toml tools/govkit/entries/kickoff-manifest.kit.toml tools/govkit/steps/kickoff_facts_to_overlay.py tools/govkit/selftest.py skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh skills/session-kickoff/MANIFEST-TEMPLATE.md skills/session-kickoff/SKILL.md help/upgrade-steps.md memory/guides/SESSION-KICKOFF.md .governance/instructions.toml .governance/policy.json help/orientation-card.md help/README.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-9.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-9-1-acceptance-ledger.md
2026-11-19T19:53:52Z draw · re-dispatch · TOOL-dPlacedRequest-9 · 18/130 · 20261119T195352Z-17766a

2026-11-19T19:53:53Z dispatch · item 5ab86530 TOOL-dPlacedRequest-9 · reason tools/playbook/instruction_units.py tools/playbook/readers.toml tools/govkit/entries/kickoff-manifest.kit.toml tools/govkit/steps/kickoff_facts_to_overlay.py tools/govkit/selftest.py skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh AGH8 K2 skills/session-kickoff/MANIFEST-TEMPLATE.md skills/session-kickoff/SKILL.md help/upgrade-steps.md memory/guides/SESSION-KICKOFF.md .governance/instructions.toml .governance/steps/kickoff-manifest/facts-to-overlay.before.json .governance/policy.json help/orientation-card.md help/README.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-9.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-9-1-acceptance-ledger.md
2026-11-19T19:55:01Z draw · re-dispatch · TOOL-dPlacedRequest-9 · 19/130 · 20261119T195501Z-5542f5

2026-11-19T19:55:01Z dispatch · item 5ab86530 TOOL-dPlacedRequest-9 · reason tools/playbook/instruction_units.py tools/playbook/readers.toml tools/govkit/entries/kickoff-manifest.kit.toml tools/govkit/steps/kickoff_facts_to_overlay.py tools/govkit/selftest.py skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh skills/session-kickoff/MANIFEST-TEMPLATE.md skills/session-kickoff/SKILL.md help/upgrade-steps.md memory/guides/SESSION-KICKOFF.md .governance/instructions.toml .governance/steps/kickoff-manifest/facts-to-overlay.before.json .governance/policy.json help/orientation-card.md help/README.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-9.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-9-1-acceptance-ledger.md
2026-11-19T20:27:58Z draw · fix-pass · TOOL-dPlacedRequest-9 · 20/130 · 20261119T202758Z-a25862

2026-11-19T20:27:58Z dispatch · item 7901e7c9 TOOL-dPlacedRequest-9 · reason tools/playbook/instruction_units.py tools/playbook/readers.toml tools/govkit/entries/kickoff-manifest.kit.toml tools/govkit/steps/kickoff_facts_to_overlay.py tools/govkit/selftest.py skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh skills/session-kickoff/MANIFEST-TEMPLATE.md skills/session-kickoff/SKILL.md help/upgrade-steps.md memory/guides/SESSION-KICKOFF.md .governance/instructions.toml .governance/steps/kickoff-manifest/facts-to-overlay.before.json .governance/policy.json help/orientation-card.md help/README.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-9.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-9-1-acceptance-ledger.md
2026-11-19T20:30:01Z draw · fix-pass · TOOL-dPlacedRequest-9 · 21/130 · 20261119T203001Z-e492d2

2026-11-19T20:30:01Z dispatch · item 47c47f11 TOOL-dPlacedRequest-9 · reason tools/playbook/instruction_units.py tools/playbook/readers.toml tools/govkit/entries/kickoff-manifest.kit.toml tools/govkit/steps/kickoff_facts_to_overlay.py tools/govkit/selftest.py skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh skills/session-kickoff/MANIFEST-TEMPLATE.md skills/session-kickoff/SKILL.md help/upgrade-steps.md memory/guides/SESSION-KICKOFF.md .governance/instructions.toml .governance/steps/kickoff-manifest/facts-to-overlay.before.json .governance/policy.json help/orientation-card.md help/README.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-9.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-9-1-acceptance-ledger.md

2026-11-19T20:48:59Z dispatch · item 65d23356 TOOL-dPlacedRequest-2 · reason skills/session-kickoff/manifest-check.sh tools/lib/resolve-python.test.sh skills/session-kickoff/manifest-check.test.sh skills/session-kickoff/card-store.fixture.sh skills/session-kickoff/SKILL.md tools/hooks/scratch-guard.js tools/loop/loop_transition.py tools/memory-tree/build_records.py tools/memory-tree/tree_lib.py tools/memory-tree/HYGIENE.template.md tools/policy/catalogue.toml .governance/policy.json help/orientation-card.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-2.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-2-1-acceptance-ledger.md memory/HYGIENE.md

2026-11-19T20:56:10Z brief · item TOOL-dPlacedRequest-2 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-19T21:03:25Z draw · re-dispatch · TOOL-dPlacedRequest-2 · 22/130 · 20261119T210325Z-e63ffb

2026-11-19T21:03:25Z dispatch · item e3952ab6 TOOL-dPlacedRequest-2 · reason skills/session-kickoff/manifest-check.sh tools/lib/resolve-python.test.sh skills/session-kickoff/manifest-check.test.sh skills/session-kickoff/card-store.fixture.sh skills/session-kickoff/SKILL.md tools/hooks/scratch-guard.js tools/loop/loop_transition.py tools/memory-tree/build_records.py tools/memory-tree/tree_lib.py tools/memory-tree/HYGIENE.template.md tools/policy/catalogue.toml .governance/policy.json help/orientation-card.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-2.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-2-1-acceptance-ledger.md memory/HYGIENE.md tools/hooks/scratch-guard.test.sh memory/guides/SESSION-KICKOFF.md
2026-11-19T21:22:33Z draw · re-dispatch · TOOL-dPlacedRequest-2 · 23/130 · 20261119T212233Z-892b8b

2026-11-19T21:22:33Z dispatch · item e3952ab6 TOOL-dPlacedRequest-2 · reason skills/session-kickoff/manifest-check.sh tools/lib/resolve-python.test.sh skills/session-kickoff/manifest-check.test.sh skills/session-kickoff/card-store.fixture.sh skills/session-kickoff/SKILL.md tools/hooks/scratch-guard.js tools/loop/loop_transition.py tools/memory-tree/build_records.py tools/memory-tree/tree_lib.py tools/memory-tree/HYGIENE.template.md tools/policy/catalogue.toml .governance/policy.json help/orientation-card.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-2.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-2-1-acceptance-ledger.md memory/HYGIENE.md tools/hooks/scratch-guard.test.sh memory/guides/SESSION-KICKOFF.md tools/govkit/registry.toml
2026-11-19T21:42:28Z draw · fix-pass · TOOL-dPlacedRequest-2 · 24/130 · 20261119T214228Z-8745ab

2026-11-19T21:42:28Z dispatch · item aa358454 TOOL-dPlacedRequest-2 · reason skills/session-kickoff/manifest-check.sh tools/lib/resolve-python.test.sh skills/session-kickoff/manifest-check.test.sh skills/session-kickoff/card-store.fixture.sh skills/session-kickoff/SKILL.md tools/hooks/scratch-guard.js tools/loop/loop_transition.py tools/memory-tree/build_records.py tools/memory-tree/tree_lib.py tools/memory-tree/HYGIENE.template.md tools/policy/catalogue.toml .governance/policy.json help/orientation-card.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-2.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-2-1-acceptance-ledger.md memory/HYGIENE.md tools/hooks/scratch-guard.test.sh memory/guides/SESSION-KICKOFF.md tools/govkit/registry.toml

2026-11-19T21:46:09Z dispatch · item f8a692f0 TOOL-dPlacedRequest-40 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-40.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-40-1-acceptance-ledger.md help/loop.md tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md

2026-11-19T21:49:07Z brief · item TOOL-dPlacedRequest-40 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T21:59:24Z dispatch · item 86fbcf6e TOOL-dPlacedRequest-33 · reason skills/session-kickoff/manifest-check.sh skills/session-kickoff/card-store.fixture.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-33.md memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-33-1-acceptance-ledger.md
2026-11-19T22:15:11Z draw · re-dispatch · TOOL-dPlacedRequest-33 · 25/130 · 20261119T221511Z-f73f8f

2026-11-19T22:15:11Z dispatch · item f4c3094a TOOL-dPlacedRequest-33 · reason skills/session-kickoff/manifest-check.sh skills/session-kickoff/card-store.fixture.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-33.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-33-1-acceptance-ledger.md

2026-11-19T22:18:22Z brief · item TOOL-dPlacedRequest-33 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-19T22:21:05Z draw · re-dispatch · TOOL-dPlacedRequest-33 · 26/130 · 20261119T222105Z-59f87f

2026-11-19T22:21:05Z dispatch · item d7e28e91 TOOL-dPlacedRequest-33 · reason skills/session-kickoff/manifest-check.sh skills/session-kickoff/card-store.fixture.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-33.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-33-1-acceptance-ledger.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt
2026-11-19T22:35:36Z draw · re-dispatch · TOOL-dPlacedRequest-33 · 27/130 · 20261119T223536Z-41eadf

2026-11-19T22:35:36Z dispatch · item d7e28e91 TOOL-dPlacedRequest-33 · reason skills/session-kickoff/manifest-check.sh skills/session-kickoff/card-store.fixture.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-33.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-33-1-acceptance-ledger.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt skills/session-kickoff/manifest-check.test.sh tools/govkit/registry.toml
2026-11-19T22:39:20Z draw · re-dispatch · TOOL-dPlacedRequest-33 · 28/130 · 20261119T223920Z-24f365

2026-11-19T22:39:20Z dispatch · item d7e28e91 TOOL-dPlacedRequest-33 · reason skills/session-kickoff/manifest-check.sh skills/session-kickoff/card-store.fixture.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-33.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-33-1-acceptance-ledger.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt skills/session-kickoff/manifest-check.test.sh tools/govkit/registry.toml memory/guides/SESSION-KICKOFF.md
2026-11-19T22:41:40Z draw · fix-pass · TOOL-dPlacedRequest-33 · 29/130 · 20261119T224140Z-fc0645

2026-11-19T22:41:40Z dispatch · item 3a285847 TOOL-dPlacedRequest-33 · reason skills/session-kickoff/manifest-check.sh skills/session-kickoff/card-store.fixture.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-33.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-33-1-acceptance-ledger.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt skills/session-kickoff/manifest-check.test.sh tools/govkit/registry.toml memory/guides/SESSION-KICKOFF.md help/orientation-card.md

2026-11-19T22:48:49Z dispatch · item cb1a8a1e TOOL-dPlacedRequest-8 · reason memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-8.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-8-1-acceptance-ledger.md tools/loop/item-schema.toml tools/loop/loop.toml tools/loop/loop_lib.py tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md help/loop.md memory/map/generated
2026-11-19T23:02:25Z draw · re-dispatch · TOOL-dPlacedRequest-8 · 30/130 · 20261119T230225Z-b8bae8

2026-11-19T23:02:25Z dispatch · item f25386d0 TOOL-dPlacedRequest-8 · reason .claude/skills/unattended/SKILL.md help/loop.md memory/guides/UNATTENDED-VERBS.md memory/map/generated tools/loop/item-schema.toml tools/loop/kit.toml tools/loop/loop.toml tools/loop/loop_lib.py tools/template-size-limits.txt tools/unattended/SKILL.template.md tools/unattended/VERBS.template.md tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-8.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-8-1-acceptance-ledger.md

2026-11-19T23:03:19Z brief · item TOOL-dPlacedRequest-8 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T23:26:51Z dispatch · item fac8a6a2 TOOL-dPlacedRequest-6 · reason tools/loop/loop.toml tools/loop/loop_lib.py help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-6.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-6-1-acceptance-ledger.md help/loop.md memory/map/generated tools/loop/loop.toml tools/loop/loop_lib.py tools/loop/item-schema.toml

2026-11-19T23:29:39Z brief · item TOOL-dPlacedRequest-6 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-19T23:44:58Z dispatch · item 109bea63 TOOL-dPlacedRequest-7 · reason .governance/policy.json help/loop.md memory/HYGIENE.md memory/map/features/loop.md memory/map/generated tools/gate-legs.json tools/govkit/subject-pins.tsv tools/govkit/registry.toml tools/loop/kit.toml tools/loop/loop.toml tools/loop/loop_lib.py tools/loop/probe.py tools/memory-tree/HYGIENE.template.md tools/memory-tree/build_records.py tools/memory-tree/tree_lib.py tools/playbook/core-pending.txt tools/policy/catalogue.toml tools/run-gates/ceiling-evidence.txt tools/run-gates/selftest-budgets.txt memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-7.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-7-1-acceptance-ledger.md

2026-11-19T23:46:05Z brief · item TOOL-dPlacedRequest-7 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T00:01:25Z draw · re-dispatch · TOOL-dPlacedRequest-7 · 31/130 · 20261120T000125Z-2a6a16

2026-11-20T00:01:25Z dispatch · item a57c059c TOOL-dPlacedRequest-7 · reason .governance/policy.json help/loop.md memory/HYGIENE.md memory/map/features/loop.md memory/map/generated tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/loop/kit.toml tools/loop/loop.toml tools/loop/loop_lib.py tools/loop/probe.py tools/memory-tree/HYGIENE.template.md tools/memory-tree/build_records.py tools/memory-tree/tree_lib.py tools/playbook/core-pending.txt tools/policy/catalogue.toml tools/run-gates/ceiling-evidence.txt tools/run-gates/selftest-budgets.txt memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-7.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-7-1-acceptance-ledger.md
2026-11-20T00:17:05Z draw · re-dispatch · TOOL-dPlacedRequest-7 · 32/130 · 20261120T001705Z-5ad0f4

2026-11-20T00:17:05Z dispatch · item 5d186f0f TOOL-dPlacedRequest-7 · reason .governance/policy.json help/loop.md memory/HYGIENE.md memory/map/features/loop.md memory/map/generated tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/loop/kit.toml tools/loop/loop.toml tools/loop/loop_lib.py tools/loop/probe.py tools/memory-tree/HYGIENE.template.md tools/memory-tree/build_records.py tools/memory-tree/tree_lib.py tools/playbook/core-pending.txt tools/policy/catalogue.toml tools/run-gates/selftest-budgets.txt memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-7.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-7-1-acceptance-ledger.md
2026-11-20T00:40:16Z draw · re-dispatch · TOOL-dPlacedRequest-7 · 33/130 · 20261120T004016Z-683759

2026-11-20T00:40:16Z dispatch · item 222f05e8 TOOL-dPlacedRequest-7 · reason .governance/policy.json help/loop.md memory/HYGIENE.md memory/map/features/loop.md memory/map/generated tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/loop/kit.toml tools/loop/loop.toml tools/loop/loop_lib.py tools/loop/probe.py tools/memory-tree/HYGIENE.template.md tools/memory-tree/build_records.py tools/memory-tree/tree_lib.py tools/playbook/core-pending.txt tools/policy/catalogue.toml tools/run-gates/selftest-budgets.txt memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-7.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-7-1-acceptance-ledger.md tools/loop/README.md
2026-11-20T00:43:04Z draw · re-dispatch · TOOL-dPlacedRequest-7 · 34/130 · 20261120T004304Z-ed5638

2026-11-20T00:43:04Z dispatch · item 222f05e8 TOOL-dPlacedRequest-7 · reason .governance/policy.json help/loop.md memory/HYGIENE.md memory/map/features/loop.md memory/map/generated tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/loop/kit.toml tools/loop/loop.toml tools/loop/loop_lib.py tools/loop/probe.py tools/memory-tree/HYGIENE.template.md tools/memory-tree/build_records.py tools/memory-tree/tree_lib.py tools/playbook/core-pending.txt tools/policy/catalogue.toml tools/run-gates/selftest-budgets.txt memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-7.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-7-1-acceptance-ledger.md tools/loop/README.md memory/guides/SESSION-KICKOFF.md memory/LIVE.md memory/builds/dPlacedRequest/README.md
2026-11-20T00:55:29Z draw · fix-pass · TOOL-dPlacedRequest-7 · 35/130 · 20261120T005529Z-394fe9

2026-11-20T00:55:29Z dispatch · item b1f8f916 TOOL-dPlacedRequest-7 · reason .governance/policy.json help/loop.md memory/HYGIENE.md memory/map/features/loop.md memory/map/generated tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/loop/kit.toml tools/loop/loop.toml tools/loop/loop_lib.py tools/loop/probe.py tools/memory-tree/HYGIENE.template.md tools/memory-tree/build_records.py tools/memory-tree/tree_lib.py tools/playbook/core-pending.txt tools/policy/catalogue.toml tools/run-gates/selftest-budgets.txt memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-7.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-7-1-acceptance-ledger.md tools/loop/README.md memory/guides/SESSION-KICKOFF.md memory/LIVE.md memory/builds/dPlacedRequest/README.md memory/backlog/TOOL.md

2026-11-20T01:01:11Z dispatch · item 5a751503 TOOL-dPlacedRequest-4 · reason .claude/agents/gov-orienter.md help/loop.md memory/guides/UNATTENDED-VERBS.md memory/map/generated tools/gate-legs.json tools/loop/kit.toml tools/loop/placement.py tools/playbook/core-pending.txt tools/roles/README.md tools/roles/agents/gov-orienter.agent.md tools/unattended/VERBS.template.md tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/run-gates/selftest-budgets.txt memory/map/features/loop.md memory/guides/SESSION-KICKOFF.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-4.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-4-1-acceptance-ledger.md

2026-11-20T01:20:58Z brief · item TOOL-dPlacedRequest-4 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-20T01:41:24Z dispatch · item 01b3c970 TOOL-dPlacedRequest-10 · reason tools/loop/placement.py tools/roles/agents/gov-orienter.agent.md .claude/agents/gov-orienter.md tools/roles/README.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-10.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-10-1-acceptance-ledger.md

2026-11-20T01:45:16Z brief · item TOOL-dPlacedRequest-10 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-20T01:58:30Z dispatch · item 26301edd TOOL-dPlacedRequest-14 · reason tools/loop/budget.py tools/loop/placement.py tools/unattended/unattended.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-14.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-14-1-acceptance-ledger.md tools/unattended/unattended.test.sh

2026-11-20T02:04:36Z brief · item TOOL-dPlacedRequest-14 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T02:05:44Z draw · re-dispatch · TOOL-dPlacedRequest-14 · 36/130 · 20261120T020544Z-d65a8d

2026-11-20T02:05:44Z dispatch · item 1e2a4b18 TOOL-dPlacedRequest-14 · reason tools/loop/budget.py tools/loop/placement.py tools/unattended/unattended.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-14.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-14-1-acceptance-ledger.md tools/unattended/unattended.test.sh tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt
2026-11-20T02:30:53Z draw · fix-pass · TOOL-dPlacedRequest-14 · 37/130 · 20261120T023053Z-f7aed5

2026-11-20T02:30:53Z dispatch · item ade7a0d1 TOOL-dPlacedRequest-14 · reason tools/loop/budget.py tools/loop/placement.py tools/unattended/unattended.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-14.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-14-1-acceptance-ledger.md tools/unattended/unattended.test.sh tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt

2026-11-20T02:35:25Z dispatch · item 694e83fc TOOL-dPlacedRequest-5 · reason tools/loop/placement.py tools/loop/breakpoints.py tools/unattended/unattended.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-5.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-5-1-acceptance-ledger.md tools/unattended/unattended.test.sh

2026-11-20T02:39:40Z brief · item TOOL-dPlacedRequest-5 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T02:40:42Z draw · re-dispatch · TOOL-dPlacedRequest-5 · 38/130 · 20261120T024042Z-504d22

2026-11-20T02:40:43Z dispatch · item 8c3d875c TOOL-dPlacedRequest-5 · reason tools/loop/placement.py tools/loop/breakpoints.py tools/unattended/unattended.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-5.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-5-1-acceptance-ledger.md tools/unattended/unattended.test.sh tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt
2026-11-20T02:55:05Z draw · re-dispatch · TOOL-dPlacedRequest-5 · 39/130 · 20261120T025505Z-41d564

2026-11-20T02:55:05Z dispatch · item 8c3d875c TOOL-dPlacedRequest-5 · reason tools/loop/placement.py tools/loop/breakpoints.py tools/unattended/unattended.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-5.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-5-1-acceptance-ledger.md tools/unattended/unattended.test.sh tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt help/spec-audit.md
2026-11-20T03:03:50Z draw · fix-pass · TOOL-dPlacedRequest-5 · 40/130 · 20261120T030350Z-d2920b

2026-11-20T03:03:50Z dispatch · item ed4c66e4 TOOL-dPlacedRequest-5 · reason tools/loop/placement.py tools/loop/breakpoints.py tools/unattended/unattended.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-5.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-5-1-acceptance-ledger.md tools/unattended/unattended.test.sh tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt help/spec-audit.md

2026-11-20T03:10:40Z dispatch · item 25785c2d TOOL-dPlacedRequest-21 · reason tools/loop/claim.py tools/loop/loop_transition.py tools/loop/kit.toml tools/gate-legs.json tools/playbook/core-pending.txt tools/unattended/unattended.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md tools/memory-tree/gen_build_index.py help/loop.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-21.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-21-1-acceptance-ledger.md tools/unattended/unattended.test.sh tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/run-gates/selftest-budgets.txt memory/map/features/loop.md memory/guides/SESSION-KICKOFF.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt

2026-11-20T03:14:22Z brief · item TOOL-dPlacedRequest-21 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T03:25:13Z draw · re-dispatch · TOOL-dPlacedRequest-21 · 41/130 · 20261120T032513Z-49a62c

2026-11-20T03:25:13Z dispatch · item e8a9a1e7 TOOL-dPlacedRequest-21 · reason tools/loop/claim.py tools/loop/loop_transition.py tools/loop/kit.toml tools/gate-legs.json tools/playbook/core-pending.txt tools/unattended/unattended.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md tools/memory-tree/gen_build_index.py help/loop.md memory/map/generated tools/unattended/unattended.test.sh tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/run-gates/selftest-budgets.txt memory/map/features/loop.md memory/guides/SESSION-KICKOFF.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-21.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-21-1-acceptance-ledger.md

2026-11-20T04:24:50Z dispatch · item 3a5e4bc1 TOOL-dPlacedRequest-3 · reason tools/loop/loop.toml tools/loop/loop_lib.py skills/session-kickoff/SKILL.md memory/guides/SESSION-KICKOFF.md help/loop.md memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-3.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-3-1-acceptance-ledger.md

2026-11-20T04:26:48Z brief · item TOOL-dPlacedRequest-3 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T04:36:28Z draw · fix-pass · TOOL-dPlacedRequest-3 · 42/130 · 20261120T043628Z-acc1de

2026-11-20T04:36:28Z dispatch · item 4680bf19 TOOL-dPlacedRequest-3 · reason tools/loop/loop.toml tools/loop/loop_lib.py skills/session-kickoff/SKILL.md memory/guides/SESSION-KICKOFF.md help/loop.md memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-3.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-3-1-acceptance-ledger.md tools/loop/README.md

2026-11-20T04:41:09Z dispatch · item 127f4495 TOOL-dPlacedRequest-34 · reason tools/lib/gov-feed.sh tools/lib/gov-ref.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/resume-tick.test.sh tools/unattended/.unattended.conf.example tools/unattended/PROTOCOL.template.md tools/unattended/VERBS.template.md tools/unattended/STOPS.template.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-STOPS.md tools/run-gates/post-merge.sh tools/push-main.sh tools/push-main.test.sh .githooks/pre-push tools/hooks/scratch-guard.js tools/hooks/scratch-guard.test.sh skills/session-kickoff/manifest-check.sh skills/session-kickoff/card-store.fixture.sh skills/session-kickoff/SKILL.md skills/session-kickoff/RESUME.md tools/playbook/render_playbook.py tools/loop/loop_lib.py tools/loop/request.py tools/loop/placement.py tools/loop/budget.py tools/loop/claim.py tools/loop/probe.py tools/loop/loop.toml tools/govkit/steps/kickoff_facts_to_overlay.py .githooks/pre-push.test.sh tools/gate-legs.json tools/run-gates/selftest-budgets.txt tools/govkit/subject-pins.tsv memory/map/features/loop.md memory/map/features/unattended-stops.md memory/gotchas/decision-re-derived-by-a-second-process.md memory/map/generated/symbols.json tools/lib/resolve-python.test.sh help/loop.md memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-34-1-acceptance-ledger.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt tools/govkit/registry.toml memory/guides/SESSION-KICKOFF.md

2026-11-20T04:43:12Z brief · item TOOL-dPlacedRequest-34 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T05:10:54Z draw · re-dispatch · TOOL-dPlacedRequest-34 · 43/130 · 20261120T051054Z-24d423

2026-11-20T05:10:54Z dispatch · item be1af09b TOOL-dPlacedRequest-34 · reason tools/lib/gov-feed.sh tools/lib/gov-ref.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/resume-tick.test.sh tools/unattended/.unattended.conf.example tools/unattended/PROTOCOL.template.md tools/unattended/VERBS.template.md tools/unattended/STOPS.template.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-STOPS.md tools/run-gates/post-merge.sh tools/push-main.sh tools/push-main.test.sh .githooks/pre-push tools/hooks/scratch-guard.js tools/hooks/scratch-guard.test.sh skills/session-kickoff/manifest-check.sh skills/session-kickoff/card-store.fixture.sh skills/session-kickoff/SKILL.md skills/session-kickoff/RESUME.md tools/playbook/render_playbook.py tools/loop/loop_lib.py tools/loop/request.py tools/loop/placement.py tools/loop/budget.py tools/loop/claim.py tools/loop/probe.py tools/loop/loop.toml tools/govkit/steps/kickoff_facts_to_overlay.py .githooks/pre-push.test.sh tools/gate-legs.json tools/run-gates/selftest-budgets.txt tools/govkit/subject-pins.tsv memory/map/features/loop.md memory/map/features/unattended-stops.md memory/gotchas/decision-re-derived-by-a-second-process.md memory/map/generated/symbols.json tools/lib/resolve-python.test.sh help/loop.md memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-34-1-acceptance-ledger.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt tools/govkit/registry.toml memory/guides/SESSION-KICKOFF.md tools/unattended/lib-unattended.sh .unattended.conf tools/loop/README.md
2026-11-20T05:14:37Z draw · re-dispatch · TOOL-dPlacedRequest-34 · 44/130 · 20261120T051437Z-c05755

2026-11-20T05:14:37Z dispatch · item be1af09b TOOL-dPlacedRequest-34 · reason tools/lib/gov-feed.sh tools/lib/gov-ref.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/resume-tick.test.sh tools/unattended/.unattended.conf.example tools/unattended/PROTOCOL.template.md tools/unattended/VERBS.template.md tools/unattended/STOPS.template.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-STOPS.md tools/run-gates/post-merge.sh tools/push-main.sh tools/push-main.test.sh .githooks/pre-push tools/hooks/scratch-guard.js tools/hooks/scratch-guard.test.sh skills/session-kickoff/manifest-check.sh skills/session-kickoff/card-store.fixture.sh skills/session-kickoff/SKILL.md skills/session-kickoff/RESUME.md tools/playbook/render_playbook.py tools/loop/loop_lib.py tools/loop/request.py tools/loop/placement.py tools/loop/budget.py tools/loop/claim.py tools/loop/probe.py tools/loop/loop.toml tools/govkit/steps/kickoff_facts_to_overlay.py .githooks/pre-push.test.sh tools/gate-legs.json tools/run-gates/selftest-budgets.txt tools/govkit/subject-pins.tsv memory/map/features/loop.md memory/map/features/unattended-stops.md memory/gotchas/decision-re-derived-by-a-second-process.md memory/map/generated/symbols.json tools/lib/resolve-python.test.sh help/loop.md memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-34-1-acceptance-ledger.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt tools/govkit/registry.toml memory/guides/SESSION-KICKOFF.md tools/unattended/lib-unattended.sh .unattended.conf tools/loop/README.md tools/loop/loop_items.py
2026-11-20T05:21:10Z draw · fix-pass · TOOL-dPlacedRequest-34 · 45/130 · 20261120T052110Z-8b1acb

2026-11-20T05:21:10Z dispatch · item 75d626b1 TOOL-dPlacedRequest-34 · reason tools/lib/gov-feed.sh tools/lib/gov-ref.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/resume-tick.test.sh tools/unattended/.unattended.conf.example tools/unattended/PROTOCOL.template.md tools/unattended/VERBS.template.md tools/unattended/STOPS.template.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-STOPS.md tools/run-gates/post-merge.sh tools/push-main.sh tools/push-main.test.sh .githooks/pre-push tools/hooks/scratch-guard.js tools/hooks/scratch-guard.test.sh skills/session-kickoff/manifest-check.sh skills/session-kickoff/card-store.fixture.sh skills/session-kickoff/SKILL.md skills/session-kickoff/RESUME.md tools/playbook/render_playbook.py tools/loop/loop_lib.py tools/loop/request.py tools/loop/placement.py tools/loop/budget.py tools/loop/claim.py tools/loop/probe.py tools/loop/loop.toml tools/govkit/steps/kickoff_facts_to_overlay.py .githooks/pre-push.test.sh tools/gate-legs.json tools/run-gates/selftest-budgets.txt tools/govkit/subject-pins.tsv memory/map/features/loop.md memory/map/features/unattended-stops.md memory/gotchas/decision-re-derived-by-a-second-process.md memory/map/generated/symbols.json tools/lib/resolve-python.test.sh help/loop.md memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-34-1-acceptance-ledger.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt tools/govkit/registry.toml memory/guides/SESSION-KICKOFF.md tools/unattended/lib-unattended.sh .unattended.conf tools/loop/README.md tools/loop/loop_items.py help/orientation-card.md
2026-11-20T05:34:10Z draw · fix-pass · TOOL-dPlacedRequest-34 · 46/130 · 20261120T053410Z-997570

2026-11-20T05:34:10Z dispatch · item 1f1b1d62 TOOL-dPlacedRequest-34 · reason tools/lib/gov-feed.sh tools/lib/gov-ref.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/resume-tick.test.sh tools/unattended/.unattended.conf.example tools/unattended/PROTOCOL.template.md tools/unattended/VERBS.template.md tools/unattended/STOPS.template.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-VERBS.md memory/guides/UNATTENDED-STOPS.md tools/run-gates/post-merge.sh tools/push-main.sh tools/push-main.test.sh .githooks/pre-push tools/hooks/scratch-guard.js tools/hooks/scratch-guard.test.sh skills/session-kickoff/manifest-check.sh skills/session-kickoff/card-store.fixture.sh skills/session-kickoff/SKILL.md skills/session-kickoff/RESUME.md tools/playbook/render_playbook.py tools/loop/loop_lib.py tools/loop/request.py tools/loop/placement.py tools/loop/budget.py tools/loop/claim.py tools/loop/probe.py tools/loop/loop.toml tools/govkit/steps/kickoff_facts_to_overlay.py .githooks/pre-push.test.sh tools/gate-legs.json tools/run-gates/selftest-budgets.txt tools/govkit/subject-pins.tsv memory/map/features/loop.md memory/map/features/unattended-stops.md memory/gotchas/decision-re-derived-by-a-second-process.md memory/map/generated/symbols.json tools/lib/resolve-python.test.sh help/loop.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/template-size-limits.txt tools/govkit/registry.toml memory/guides/SESSION-KICKOFF.md tools/hooks/scratch-guard.test.sh memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-34-1-acceptance-ledger.md

2026-11-20T06:04:05Z dispatch · item c8afcf2b TOOL-dPlacedRequest-35 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/map/generated tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-35.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-35-1-acceptance-ledger.md

2026-11-20T06:05:25Z brief · item TOOL-dPlacedRequest-35 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-20T06:14:45Z dispatch · item 1ec16f9c TOOL-dPlacedRequest-46 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-46.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-46-1-acceptance-ledger.md

2026-11-20T06:17:08Z brief · item TOOL-dPlacedRequest-46 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T06:28:08Z draw · re-dispatch · TOOL-dPlacedRequest-46 · 47/130 · 20261120T062808Z-011deb

2026-11-20T06:28:08Z dispatch · item be880efe TOOL-dPlacedRequest-46 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-46.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-46-1-acceptance-ledger.md

2026-11-20T06:43:01Z dispatch · item 7bcd8b1b TOOL-dPlacedRequest-47 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-47.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-47-1-acceptance-ledger.md tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md

2026-11-20T07:01:35Z brief · item TOOL-dPlacedRequest-47 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-20T07:32:43Z dispatch · item 6bd9c2cc TOOL-dPlacedRequest-43 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md tools/unattended/VERBS.template.md help/loop.md skills/session-kickoff/manifest-check.sh skills/session-kickoff/card-store.fixture.sh tools/hooks/scratch-guard.js tools/push-main.sh tools/run-gates/run-selftests.sh tools/loop/placement.py memory/guides/SESSION-KICKOFF.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-43-1-acceptance-ledger.md memory/guides/UNATTENDED-STOPS.md memory/guides/UNATTENDED-VERBS.md tools/unattended/README.md

2026-11-20T07:34:30Z brief · item TOOL-dPlacedRequest-43 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T07:39:02Z draw · re-dispatch · TOOL-dPlacedRequest-43 · 48/130 · 20261120T073902Z-593201

2026-11-20T07:39:02Z dispatch · item dac2af17 TOOL-dPlacedRequest-43 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md tools/unattended/VERBS.template.md help/loop.md skills/session-kickoff/manifest-check.sh skills/session-kickoff/card-store.fixture.sh tools/hooks/scratch-guard.js tools/push-main.sh tools/run-gates/run-selftests.sh tools/loop/placement.py memory/guides/SESSION-KICKOFF.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-43-1-acceptance-ledger.md memory/guides/UNATTENDED-STOPS.md memory/guides/UNATTENDED-VERBS.md tools/unattended/README.md help/orientation-card.md tools/hooks/scratch-guard.test.sh tools/push-main.test.sh
2026-11-20T08:12:08Z draw · fix-pass · TOOL-dPlacedRequest-43 · 49/130 · 20261120T081208Z-47b84a

2026-11-20T08:12:08Z dispatch · item afa399f6 TOOL-dPlacedRequest-43 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/STOPS.template.md tools/unattended/VERBS.template.md help/loop.md skills/session-kickoff/manifest-check.sh skills/session-kickoff/card-store.fixture.sh tools/hooks/scratch-guard.js tools/push-main.sh tools/run-gates/run-selftests.sh tools/loop/placement.py memory/guides/SESSION-KICKOFF.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-43-1-acceptance-ledger.md memory/guides/UNATTENDED-STOPS.md memory/guides/UNATTENDED-VERBS.md tools/unattended/README.md help/orientation-card.md tools/hooks/scratch-guard.test.sh tools/push-main.test.sh

2026-11-20T08:39:11Z dispatch · item 4941c2fe TOOL-dPlacedRequest-44 · reason memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-44.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-44-1-acceptance-ledger.md

2026-11-20T08:40:52Z brief · item TOOL-dPlacedRequest-44 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-20T08:47:15Z dispatch · item 3eddba95 TOOL-dPlacedRequest-45 · reason memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md memory/gotchas/INDEX.md memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-45.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-45-1-acceptance-ledger.md

2026-11-20T08:55:55Z brief · item TOOL-dPlacedRequest-45 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-20T09:02:38Z dispatch · item 451a6891 TOOL-dPlacedRequest-48 · reason tools/unattended/unattended.test.sh memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-48.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-48-1-acceptance-ledger.md

2026-11-20T09:04:17Z brief · item TOOL-dPlacedRequest-48 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-20T09:15:12Z dispatch · item 18672c47 TOOL-dPlacedRequest-50 · reason memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-50.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-50-1-acceptance-ledger.md

2026-11-20T09:17:06Z brief · item TOOL-dPlacedRequest-50 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T09:24:07Z draw · fix-pass · TOOL-dPlacedRequest-50 · 50/130 · 20261120T092407Z-febeb5

2026-11-20T09:24:07Z dispatch · item 71587e06 TOOL-dPlacedRequest-50 · reason memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-50.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-50-1-acceptance-ledger.md

2026-11-20T09:58:15Z dispatch · item e69a8d66 TOOL-dPlacedRequest-49 · reason tools/lib/gov-feed.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/lib/resolve-python.test.sh skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh memory/guides/SESSION-KICKOFF.md help/orientation-card.md tools/unattended/README.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-49.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-49-1-acceptance-ledger.md help/loop.md tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md

2026-11-20T09:59:51Z brief · item TOOL-dPlacedRequest-49 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T10:05:34Z draw · re-dispatch · TOOL-dPlacedRequest-49 · 51/130 · 20261120T100534Z-70eb67

2026-11-20T10:05:34Z dispatch · item 05b542ef TOOL-dPlacedRequest-49 · reason tools/lib/gov-feed.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/lib/resolve-python.test.sh skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh memory/guides/SESSION-KICKOFF.md help/orientation-card.md tools/unattended/README.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-49.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-49-1-acceptance-ledger.md help/loop.md tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md tools/push-main.sh tools/run-gates/post-merge.sh
2026-11-20T10:33:20Z draw · fix-pass · TOOL-dPlacedRequest-49 · 52/130 · 20261120T103320Z-efed63

2026-11-20T10:33:20Z dispatch · item c13d3e31 TOOL-dPlacedRequest-49 · reason tools/lib/gov-feed.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/lib/resolve-python.test.sh skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh memory/guides/SESSION-KICKOFF.md help/orientation-card.md tools/unattended/README.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-49.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-49-1-acceptance-ledger.md help/loop.md tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md tools/push-main.sh tools/run-gates/post-merge.sh

2026-11-20T10:38:57Z dispatch · item 04003a2d TOOL-dPlacedRequest-51 · reason memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-51.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-51-1-acceptance-ledger.md

2026-11-20T10:41:21Z brief · item TOOL-dPlacedRequest-51 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T10:48:24Z draw · fix-pass · TOOL-dPlacedRequest-51 · 53/130 · 20261120T104824Z-5d66e8

2026-11-20T10:48:24Z dispatch · item 67bdca25 TOOL-dPlacedRequest-51 · reason memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-51.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-51-1-acceptance-ledger.md

2026-11-20T11:19:10Z dispatch · item 476df731 TOOL-dPlacedRequest-52 · reason tools/unattended/unattended.test.sh tools/lib/gov-feed.sh tools/unattended/unattended.sh tools/lib/resolve-python.test.sh skills/session-kickoff/manifest-check.sh memory/guides/SESSION-KICKOFF.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-52.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-52-1-acceptance-ledger.md

2026-11-20T11:21:01Z brief · item TOOL-dPlacedRequest-52 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T11:25:44Z draw · re-dispatch · TOOL-dPlacedRequest-52 · 54/130 · 20261120T112544Z-3c7062

2026-11-20T11:25:44Z dispatch · item 3b1d2bec TOOL-dPlacedRequest-52 · reason tools/unattended/unattended.test.sh tools/lib/gov-feed.sh tools/unattended/unattended.sh tools/run-gates/post-merge.sh tools/push-main.sh tools/lib/resolve-python.test.sh skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh memory/guides/SESSION-KICKOFF.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-52.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-52-1-acceptance-ledger.md
2026-11-20T11:42:31Z draw · fix-pass · TOOL-dPlacedRequest-52 · 55/130 · 20261120T114231Z-efeb66

2026-11-20T11:42:31Z dispatch · item 498c52a7 TOOL-dPlacedRequest-52 · reason tools/unattended/unattended.test.sh tools/lib/gov-feed.sh tools/unattended/unattended.sh tools/run-gates/post-merge.sh tools/push-main.sh tools/lib/resolve-python.test.sh skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh memory/guides/SESSION-KICKOFF.md memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-52.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-52-1-acceptance-ledger.md

2026-11-20T11:50:58Z dispatch · item 5302d10d TOOL-dPlacedRequest-53 · reason memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-53.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-53-1-acceptance-ledger.md

2026-11-20T11:53:47Z brief · item TOOL-dPlacedRequest-53 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T12:03:06Z draw · fix-pass · TOOL-dPlacedRequest-53 · 56/130 · 20261120T120306Z-97cf01

2026-11-20T12:03:06Z dispatch · item 6b72811a TOOL-dPlacedRequest-53 · reason memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-53.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-53-1-acceptance-ledger.md

2026-11-20T12:07:39Z dispatch · item ad4b0197 TOOL-dPlacedRequest-54 · reason memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-54.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-54-1-acceptance-ledger.md

2026-11-20T12:09:19Z brief · item TOOL-dPlacedRequest-54 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T12:14:44Z draw · fix-pass · TOOL-dPlacedRequest-54 · 57/130 · 20261120T121444Z-3b1acf

2026-11-20T12:14:44Z dispatch · item 225bd968 TOOL-dPlacedRequest-54 · reason memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-54.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-54-1-acceptance-ledger.md

2026-11-20T12:19:45Z dispatch · item 71c3404f TOOL-dPlacedRequest-55 · reason memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-55.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-55-1-acceptance-ledger.md

2026-11-20T12:21:43Z brief · item TOOL-dPlacedRequest-55 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T12:28:17Z draw · fix-pass · TOOL-dPlacedRequest-55 · 58/130 · 20261120T122817Z-05c9a0

2026-11-20T12:28:17Z dispatch · item f973248a TOOL-dPlacedRequest-55 · reason memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-55.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-55-1-acceptance-ledger.md

2026-11-20T13:06:07Z dispatch · item a18ee28e TOOL-dPlacedRequest-56 · reason tools/unattended/unattended.test.sh skills/session-kickoff/manifest-check.test.sh memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-56.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-56-1-acceptance-ledger.md

2026-11-20T13:08:00Z brief · item TOOL-dPlacedRequest-56 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-20T13:22:26Z dispatch · item 68a7dfee TOOL-dPlacedRequest-57 · reason memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-57.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-57-1-acceptance-ledger.md

2026-11-20T13:25:32Z brief · item TOOL-dPlacedRequest-57 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md

2026-11-20T13:34:48Z dispatch · item bf4a4b91 TOOL-dPlacedRequest-58 · reason tools/unattended/unattended.test.sh memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-58.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-58-1-acceptance-ledger.md

2026-11-20T13:37:28Z brief · item TOOL-dPlacedRequest-58 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T13:47:50Z draw · fix-pass · TOOL-dPlacedRequest-58 · 59/130 · 20261120T134750Z-2c4b9e

2026-11-20T13:47:50Z dispatch · item 570fafa1 TOOL-dPlacedRequest-58 · reason tools/unattended/unattended.test.sh memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-58.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-58-1-acceptance-ledger.md

2026-11-20T13:53:53Z dispatch · item f5dd1beb TOOL-dPlacedRequest-60 · reason memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-60.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-60-1-acceptance-ledger.md

2026-11-20T13:55:56Z brief · item TOOL-dPlacedRequest-60 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T14:01:19Z draw · fix-pass · TOOL-dPlacedRequest-60 · 60/130 · 20261120T140119Z-e5f6c4

2026-11-20T14:01:19Z dispatch · item 80fbb019 TOOL-dPlacedRequest-60 · reason memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-60.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-60-1-acceptance-ledger.md

2026-11-20T14:44:20Z dispatch · item 4179a941 TOOL-dPlacedRequest-59 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-59.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-59-1-acceptance-ledger.md

2026-11-20T14:47:59Z brief · item TOOL-dPlacedRequest-59 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T15:00:13Z draw · fix-pass · TOOL-dPlacedRequest-59 · 61/130 · 20261120T150013Z-69a0ae

2026-11-20T15:00:13Z dispatch · item eab56e88 TOOL-dPlacedRequest-59 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/map/generated memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-59.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-59-1-acceptance-ledger.md

2026-11-20T15:08:23Z dispatch · item 39ebe377 TOOL-dPlacedRequest-61 · reason memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-61.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-61-1-acceptance-ledger.md

2026-11-20T15:11:32Z brief · item TOOL-dPlacedRequest-61 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T15:18:27Z draw · fix-pass · TOOL-dPlacedRequest-61 · 62/130 · 20261120T151827Z-5d987b

2026-11-20T15:18:27Z dispatch · item 34981ce0 TOOL-dPlacedRequest-61 · reason memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-61.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-61-1-acceptance-ledger.md

2026-11-20T15:24:11Z dispatch · item d2533e23 TOOL-dPlacedRequest-62 · reason memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-62.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-62-1-acceptance-ledger.md

2026-11-20T15:25:55Z brief · item TOOL-dPlacedRequest-62 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T15:33:35Z draw · fix-pass · TOOL-dPlacedRequest-62 · 63/130 · 20261120T153335Z-eb5f9f

2026-11-20T15:33:35Z dispatch · item 8f7a58df TOOL-dPlacedRequest-62 · reason memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-62.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-62-1-acceptance-ledger.md

2026-11-20T15:38:22Z dispatch · item 02daa1f0 TOOL-dPlacedRequest-63 · reason memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-63.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-63-1-acceptance-ledger.md

2026-11-20T15:40:12Z brief · item TOOL-dPlacedRequest-63 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T15:49:33Z draw · fix-pass · TOOL-dPlacedRequest-63 · 64/130 · 20261120T154933Z-41769b

2026-11-20T15:49:34Z dispatch · item 7a0c55f2 TOOL-dPlacedRequest-63 · reason memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-63.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-63-1-acceptance-ledger.md
2026-11-20T15:51:50Z draw · fix-pass · TOOL-dPlacedRequest-63 · 65/130 · 20261120T155150Z-2c25e7

2026-11-20T15:51:50Z dispatch · item 44ac4bed TOOL-dPlacedRequest-63 · reason memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-63.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-63-1-acceptance-ledger.md

2026-11-20T15:55:59Z dispatch · item 1d436a92 TOOL-dPlacedRequest-64 · reason memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-64.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-64-1-acceptance-ledger.md

2026-11-20T15:57:33Z brief · item TOOL-dPlacedRequest-64 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T16:05:19Z draw · fix-pass · TOOL-dPlacedRequest-64 · 66/130 · 20261120T160519Z-9022e8

2026-11-20T16:05:19Z dispatch · item 3a057a50 TOOL-dPlacedRequest-64 · reason memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-64.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-64-1-acceptance-ledger.md
2026-11-20T16:07:18Z draw · fix-pass · TOOL-dPlacedRequest-64 · 67/130 · 20261120T160718Z-d6b5c7

2026-11-20T16:07:18Z dispatch · item ab7501fe TOOL-dPlacedRequest-64 · reason memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-64.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-64-1-acceptance-ledger.md
2026-11-20T16:15:13Z draw · re-dispatch · TOOL-dPlacedRequest-64 · 68/130 · 20261120T161513Z-d7ae07

2026-11-20T16:15:13Z dispatch · item fbf8e094 TOOL-dPlacedRequest-64 · reason memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-64.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-64-1-acceptance-ledger.md

2026-11-20T16:29:18Z review · item dPlacedRequest · reason verdict CLEAN WITH FIXES · blockers 0 · round-highs 2 · round-minors 2
2026-11-20T16:44:59Z draw · review-round · dPlacedRequest · 69/130 · 20261120T164459Z-4c66dc

2026-11-20T16:45:00Z review · item dPlacedRequest · reason verdict CLEAN WITH FIXES · blockers 0 · round-highs 2 · round-minors 6 · NON-CONVERGENT · highs 4 · minors 8 · to units · disposition promote

2026-11-20T16:47:25Z rescope · item add TOOL-dPlacedRequest-95 · reason promoted by the closing diff review's NON-CONVERGENT exit at round 2 (memory/builds/dPlacedRequest/prompts/2026-11-20-prompt-TOOL-dPlacedRequest-95-closing-review-spec-brief.md)

2026-11-20T16:47:26Z rescope · item add TOOL-dPlacedRequest-96 · reason promoted by the closing diff review's NON-CONVERGENT exit at round 2 (memory/builds/dPlacedRequest/prompts/2026-11-20-prompt-TOOL-dPlacedRequest-96-closing-review-spec-brief.md)

2026-11-20T16:47:27Z rescope · item add TOOL-dPlacedRequest-97 · reason promoted by the closing diff review's NON-CONVERGENT exit at round 2 (memory/builds/dPlacedRequest/prompts/2026-11-20-prompt-TOOL-dPlacedRequest-97-closing-review-spec-brief.md)

2026-11-20T16:47:28Z rescope · item add TOOL-dPlacedRequest-98 · reason promoted by the closing diff review's NON-CONVERGENT exit at round 2 (memory/builds/dPlacedRequest/prompts/2026-11-20-prompt-TOOL-dPlacedRequest-98-closing-review-spec-brief.md)

2026-11-20T16:47:29Z rescope · item add TOOL-dPlacedRequest-99 · reason promoted by the closing diff review's NON-CONVERGENT exit at round 2 (memory/builds/dPlacedRequest/prompts/2026-11-20-prompt-TOOL-dPlacedRequest-99-closing-review-spec-brief.md)

2026-11-20T18:07:09Z rescope · item add TOOL-dPlacedRequest-100 · reason finding 29 HIGH of 2026-11-20-review-TOOL-dPlacedRequest-95-99-spec-audit, entry-claim routes a stale build lease as a live holder

2026-11-20T18:34:40Z rescope · item add TOOL-dPlacedRequest-100 · reason promoted by the spec audit of units 95 to 99 (finding 29, a new mechanism on spec 96): memory/builds/dPlacedRequest/reviews/2026-11-20-review-TOOL-dPlacedRequest-95-99-spec-audit.md
2026-11-20T18:35:01Z draw · review-round · dPlacedRequest-spec-set-r4 · 70/130 · 20261120T183501Z-d748b4

2026-11-20T18:35:01Z review · item dPlacedRequest-spec-set-r4 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 5 · minors 27 · folded 31 · promoted 1 · to units · disposition promote

2026-11-20T18:37:02Z decision · item spec-audit-chain-ceiling · reason the spec audit chain stopped at its 4-round ceiling: round 4 audited the closing review's promoted units TOOL-dPlacedRequest-95 to -99 (CONVERGED, 0 blockers, 5 highs, 31 findings folded at rev-2) and promoted finding 29, a new mechanism on spec 96, to TOOL-dPlacedRequest-100, specced at rev-1 and unaudited; options: (a) audit unit 100 as a fifth round past the ceiling, (b) build units 95 to 100 now and close with specs-audited overridden for unit 100 alone, (c) stop the run here

2026-11-20T18:37:42Z handoff · item owner-decision · reason in the run worktree: bash tools/push-main.sh --prepare --slug dPlacedRequest && bash tools/push-main.sh --land --slug dPlacedRequest && bash tools/unattended/unattended.sh --settle dPlacedRequest

2026-11-20T18:37:42Z hold · item owner-decision · reason until owner · reaped 447082a8 · resume none(owner)

2026-11-20T20:52:25Z resume · item dPlacedRequest · reason held · keepalive 65b12df9 · manual

2026-11-20T21:02:47Z dispatch · item 1d91509a TOOL-dPlacedRequest-95 · reason tools/hooks/scratch-guard.js tools/hooks/scratch-guard.test.sh tools/run-gates/selftest-budgets.txt memory/gotchas/foreign-code-runs-on-the-ambient-credential.md memory/gotchas/INDEX.md memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-95.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-95-1-acceptance-ledger.md

2026-11-20T21:03:51Z brief · item TOOL-dPlacedRequest-95 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T21:16:21Z draw · fix-pass · TOOL-dPlacedRequest-95 · 71/130 · 20261120T211621Z-85cabd

2026-11-20T21:16:21Z dispatch · item e98bd44e TOOL-dPlacedRequest-95 · reason tools/hooks/scratch-guard.js tools/hooks/scratch-guard.test.sh tools/run-gates/selftest-budgets.txt memory/gotchas/foreign-code-runs-on-the-ambient-credential.md memory/gotchas/INDEX.md memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-95.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-95-1-acceptance-ledger.md

2026-11-20T21:27:34Z dispatch · item c5109c95 TOOL-dPlacedRequest-96 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-96.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-96-1-acceptance-ledger.md

2026-11-20T21:29:10Z brief · item TOOL-dPlacedRequest-96 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T21:38:41Z draw · fix-pass · TOOL-dPlacedRequest-96 · 72/130 · 20261120T213841Z-9b6774

2026-11-20T21:38:41Z dispatch · item a946e70c TOOL-dPlacedRequest-96 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-96.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-96-1-acceptance-ledger.md

2026-11-20T21:46:37Z dispatch · item bcd76be5 TOOL-dPlacedRequest-97 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-97.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-97-1-acceptance-ledger.md

2026-11-20T21:48:11Z brief · item TOOL-dPlacedRequest-97 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T21:58:49Z draw · fix-pass · TOOL-dPlacedRequest-97 · 73/130 · 20261120T215849Z-383d50

2026-11-20T21:58:49Z dispatch · item 7b78e4c2 TOOL-dPlacedRequest-97 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-97.md memory/builds/dPlacedRequest/build/2026-11-20-build-TOOL-dPlacedRequest-97-1-acceptance-ledger.md

2026-11-20T22:02:39Z dispatch · item ad80dfc6 TOOL-dPlacedRequest-98 · reason tools/push-main.test.sh tools/run-gates/selftest-budgets.txt memory/project/testsuite-count-waivers.txt memory/gotchas/fixture-inherits-ambient-machine-state.md memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-98.md memory/builds/dPlacedRequest/build/2026-11-21-build-TOOL-dPlacedRequest-98-1-acceptance-ledger.md

2026-11-20T22:04:11Z brief · item TOOL-dPlacedRequest-98 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T22:14:42Z draw · re-dispatch · TOOL-dPlacedRequest-98 · 74/130 · 20261120T221442Z-59d479

2026-11-20T22:14:42Z dispatch · item c989f8bc TOOL-dPlacedRequest-98 · reason tools/push-main.test.sh tools/run-gates/selftest-budgets.txt memory/project/testsuite-count-waivers.txt memory/gotchas/fixture-inherits-ambient-machine-state.md memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-98.md memory/builds/dPlacedRequest/build/2026-11-21-build-TOOL-dPlacedRequest-98-1-acceptance-ledger.md memory/gotchas/INDEX.md
2026-11-20T22:21:17Z draw · fix-pass · TOOL-dPlacedRequest-98 · 75/130 · 20261120T222117Z-bf2b20

2026-11-20T22:21:17Z dispatch · item a35f91bb TOOL-dPlacedRequest-98 · reason tools/push-main.test.sh tools/run-gates/selftest-budgets.txt memory/project/testsuite-count-waivers.txt memory/gotchas/fixture-inherits-ambient-machine-state.md memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-98.md memory/builds/dPlacedRequest/build/2026-11-21-build-TOOL-dPlacedRequest-98-1-acceptance-ledger.md memory/gotchas/INDEX.md

2026-11-20T22:27:52Z dispatch · item c498b8f7 TOOL-dPlacedRequest-99 · reason skills/session-kickoff/manifest-check.test.sh skills/session-kickoff/card-store.fixture.sh skills/session-kickoff/manifest-check.sh tools/run-gates/run-selftests.test.sh tools/run-gates/run-selftests.sh tools/run-gates/selftest-budgets.txt tools/gate-legs.json tools/run-gates/ceiling-evidence.txt memory/guides/SESSION-KICKOFF.md tools/push-main.sh tools/push-main.test.sh tools/hooks/scratch-guard.test.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/gotchas/budget-row-not-remeasured-after-added-arms.md memory/gotchas/global-set-and-never-read.md memory/gotchas/floor-left-below-the-arms-it-guards.md memory/gotchas/usage-exit-list-lags-its-function.md memory/gotchas/INDEX.md memory/map/features/session-kickoff.md memory/map/features/unattended.md memory/map/generated/MAP.md memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md memory/builds/dPlacedRequest/build/2026-11-21-build-TOOL-dPlacedRequest-99-1-acceptance-ledger.md

2026-11-20T22:29:24Z brief · item TOOL-dPlacedRequest-99 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T22:56:49Z draw · re-dispatch · TOOL-dPlacedRequest-99 · 76/130 · 20261120T225649Z-3b2649

2026-11-20T22:56:49Z dispatch · item 48144fcb TOOL-dPlacedRequest-99 · reason skills/session-kickoff/manifest-check.test.sh skills/session-kickoff/card-store.fixture.sh skills/session-kickoff/manifest-check.sh tools/run-gates/run-selftests.test.sh tools/run-gates/run-selftests.sh tools/run-gates/selftest-budgets.txt tools/gate-legs.json tools/run-gates/ceiling-evidence.txt memory/guides/SESSION-KICKOFF.md tools/push-main.sh tools/push-main.test.sh tools/hooks/scratch-guard.test.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/gotchas/budget-row-not-remeasured-after-added-arms.md memory/gotchas/global-set-and-never-read.md memory/gotchas/floor-left-below-the-arms-it-guards.md memory/gotchas/usage-exit-list-lags-its-function.md memory/gotchas/INDEX.md memory/map/features/session-kickoff.md memory/map/features/unattended.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json memory/map/generated/CARDS.md memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md memory/builds/dPlacedRequest/build/2026-11-21-build-TOOL-dPlacedRequest-99-1-acceptance-ledger.md
2026-11-20T23:10:25Z draw · fix-pass · TOOL-dPlacedRequest-99 · 77/130 · 20261120T231025Z-a0405d

2026-11-20T23:10:25Z dispatch · item 5d8b869d TOOL-dPlacedRequest-99 · reason skills/session-kickoff/manifest-check.test.sh skills/session-kickoff/card-store.fixture.sh skills/session-kickoff/manifest-check.sh tools/run-gates/run-selftests.test.sh tools/run-gates/run-selftests.sh tools/run-gates/selftest-budgets.txt tools/gate-legs.json tools/run-gates/ceiling-evidence.txt memory/guides/SESSION-KICKOFF.md tools/push-main.sh tools/push-main.test.sh tools/hooks/scratch-guard.test.sh tools/unattended/unattended.sh tools/unattended/unattended.test.sh memory/gotchas/budget-row-not-remeasured-after-added-arms.md memory/gotchas/global-set-and-never-read.md memory/gotchas/floor-left-below-the-arms-it-guards.md memory/gotchas/usage-exit-list-lags-its-function.md memory/gotchas/INDEX.md memory/map/features/session-kickoff.md memory/map/features/unattended.md memory/map/generated/MAP.md memory/map/generated/inventories.json memory/map/generated/symbols.json memory/map/generated/CARDS.md memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md memory/builds/dPlacedRequest/build/2026-11-21-build-TOOL-dPlacedRequest-99-1-acceptance-ledger.md

2026-11-20T23:16:42Z dispatch · item f99ccb12 TOOL-dPlacedRequest-100 · reason tools/unattended/unattended.sh tools/loop/claim.py tools/run-gates/selftest-budgets.txt help/loop.md tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-100.md memory/builds/dPlacedRequest/build/2026-11-21-build-TOOL-dPlacedRequest-100-1-acceptance-ledger.md tools/loop/placement.py

2026-11-20T23:18:57Z brief · item TOOL-dPlacedRequest-100 · reason c73699d13acb memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
2026-11-20T23:29:01Z draw · fix-pass · TOOL-dPlacedRequest-100 · 78/130 · 20261120T232901Z-011e8c

2026-11-20T23:29:01Z dispatch · item 179180dd TOOL-dPlacedRequest-100 · reason tools/unattended/unattended.sh tools/loop/claim.py tools/run-gates/selftest-budgets.txt help/loop.md tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-100.md memory/builds/dPlacedRequest/build/2026-11-21-build-TOOL-dPlacedRequest-100-1-acceptance-ledger.md tools/loop/placement.py memory/builds/dPlacedRequest/build/2026-11-21-build-TOOL-dPlacedRequest-100-red-fix-36.md
2026-11-20T23:32:22Z draw · fix-pass · TOOL-dPlacedRequest-100 · 79/130 · 20261120T233222Z-6f0835

2026-11-20T23:32:22Z dispatch · item 3b4afd7c TOOL-dPlacedRequest-100 · reason tools/unattended/unattended.sh tools/loop/claim.py tools/run-gates/selftest-budgets.txt help/loop.md tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-100.md memory/builds/dPlacedRequest/build/2026-11-21-build-TOOL-dPlacedRequest-100-1-acceptance-ledger.md tools/loop/placement.py memory/builds/dPlacedRequest/build/2026-11-21-build-TOOL-dPlacedRequest-100-red-fix-36.md
2026-11-20T23:34:36Z draw · fix-pass · TOOL-dPlacedRequest-100 · 80/130 · 20261120T233436Z-366cbc

2026-11-20T23:34:36Z dispatch · item 526eb7d1 TOOL-dPlacedRequest-100 · reason tools/unattended/unattended.sh tools/loop/claim.py tools/run-gates/selftest-budgets.txt help/loop.md tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-100.md memory/builds/dPlacedRequest/build/2026-11-21-build-TOOL-dPlacedRequest-100-1-acceptance-ledger.md tools/loop/placement.py memory/builds/dPlacedRequest/build/2026-11-21-build-TOOL-dPlacedRequest-100-red-fix-36.md

2026-11-20T23:39:49Z decision · item landing-merge-protected-skills: the landing must merge origin/main (173 commits past the merge base 9e21ac760, 7 conflicted files), and the merge changes the sandbox-protected .claude/skills/lexicon/SKILL.md and .claude/skills/unattended/SKILL.md; options: (a) the owner confirms the pinned git origin in the app (Help, Troubleshooting, Review Pinned Git Origins) and the run merges, (b) the owner rules a plain git merge acceptable, (c) the owner merges main into the run branch · reason the app takes protected .claude/skills files only from an origin the owner confirmed, and a raw git merge or the lander's --prepare writes the same files, so taking either routes around that guard; no resolver the mandate delegates may confirm an origin

2026-11-21T02:25:49Z handoff · item owner-decision · reason in the run worktree: bash tools/push-main.sh --prepare --slug dPlacedRequest && bash tools/push-main.sh --land --slug dPlacedRequest && bash tools/unattended/unattended.sh --settle dPlacedRequest

2026-11-21T02:25:49Z hold · item owner-decision · reason until owner · reaped 65b12df9 · resume none(owner)

2026-11-21T02:37:16Z resume · item dPlacedRequest · reason held · keepalive c039c97c · manual

2026-11-21T09:11:56Z decision · item routed-commits-lane-limits · reason Six Red-fix commits on the run branch sit outside the inline lane's limits: 52181f51, 0c82930f, ed0cffd2, f6516b55 and 3e87e4cc edit spec paths (L3) and 2ae363bf touches 5 paths and 90 lines (L1). routed_commits.py's RANGE half, which the pre-push hook runs over the landing range, reads no waiver, so push-main.sh --land would be refused. Options: (a) replay the run branch from the first violator's parent, each spec hunk in its own records commit and 2ae363bf in two, then force-push the run branch, as dSkippedRecord repaired the same red on 2026-11-20; (b) a unit that lets the RANGE half honour an owner-recorded waiver for limits findings; (c) the owner lands by hand. The run recommends (a), and refuses it unattended because it rewrites about 350 built commits, two merges among them.

2026-11-21T09:12:29Z handoff · item owner-decision · reason in the run worktree: bash tools/push-main.sh --prepare --slug dPlacedRequest && bash tools/push-main.sh --land --slug dPlacedRequest && bash tools/unattended/unattended.sh --settle dPlacedRequest

2026-11-21T09:12:29Z hold · item owner-decision · reason until owner · reaped c039c97c · resume none(owner)

2026-11-21T11:07:12Z resume · item dPlacedRequest · reason held · keepalive 2439436f · manual
