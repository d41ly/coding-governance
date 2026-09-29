# aRepatriatedFork - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 2b36619cf1aafadc63fa235e63fde849a5400efc
phase: BUILDING
mode: slug
run-branch: refs/heads/branch/arepatriated-fork-build-e42158
anchor-kind: default-branch
lease-utc: 2026-09-29T13:57:52Z
pid-image: claude.exe
host: compeeto-agent
pid: 17728
session: 3b534792-4ade-4a9d-8dfa-4cb264c0af0d
keepalive: 953a4b2c
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: d6e1749c0542218004260928f1399174daafb789
anchor-ref: refs/heads/main
base: d6e1749c0542218004260928f1399174daafb789

## Parked

2026-09-29T11:05:21Z brief · item TOOL-aRepatriatedFork-23 · reason 07d15bb623a8 memory/builds/aRepatriatedFork/prompts/2026-09-29-prompt-TOOL-aRepatriatedFork-23-build-brief.md

2026-09-29T11:05:23Z brief · item TOOL-aRepatriatedFork-24 · reason 0b9d262bef72 memory/builds/aRepatriatedFork/prompts/2026-09-29-prompt-TOOL-aRepatriatedFork-24-build-brief.md

2026-09-29T11:05:24Z brief · item TOOL-aRepatriatedFork-25 · reason 7e6a0af28dec memory/builds/aRepatriatedFork/prompts/2026-09-29-prompt-TOOL-aRepatriatedFork-25-build-brief.md

2026-09-29T11:05:25Z brief · item TOOL-aRepatriatedFork-26 · reason 34dc1149aa68 memory/builds/aRepatriatedFork/prompts/2026-09-29-prompt-TOOL-aRepatriatedFork-26-build-brief.md

2026-09-29T11:05:27Z brief · item TOOL-aRepatriatedFork-27 · reason 7ab34a4719ce memory/builds/aRepatriatedFork/prompts/2026-09-29-prompt-TOOL-aRepatriatedFork-27-build-brief.md

2026-09-29T11:05:28Z brief · item TOOL-aRepatriatedFork-29 · reason ef5fbd0b3c19 memory/builds/aRepatriatedFork/prompts/2026-09-29-prompt-TOOL-aRepatriatedFork-29-build-brief.md

2026-09-29T11:05:29Z brief · item TOOL-aRepatriatedFork-28 · reason 6ace46627006 memory/builds/aRepatriatedFork/prompts/2026-09-29-prompt-TOOL-aRepatriatedFork-28-build-brief.md

2026-09-29T11:05:31Z brief · item TOOL-aRepatriatedFork-30 · reason 5f43f647b722 memory/builds/aRepatriatedFork/prompts/2026-09-29-prompt-TOOL-aRepatriatedFork-30-build-brief.md

2026-09-29T11:09:07Z dispatch · item c88a328b TOOL-aRepatriatedFork-23 · reason tools/check-install-prefix.sh tools/check-install-prefix.test.sh tools/install-prefix-carried.txt tools/govkit/entries/check-install-prefix.kit.toml memory/builds/aRepatriatedFork/spec/2026-09-25-spec-TOOL-aRepatriatedFork-23.md memory/builds/aRepatriatedFork/build/2026-09-29-build-TOOL-aRepatriatedFork-23-1-acceptance-ledger.md

2026-09-29T11:22:58Z dispatch · item c88a328b TOOL-aRepatriatedFork-23 · reason tools/check-install-prefix.sh tools/check-install-prefix.test.sh tools/install-prefix-carried.txt tools/govkit/entries/check-install-prefix.kit.toml memory/builds/aRepatriatedFork/spec/2026-09-25-spec-TOOL-aRepatriatedFork-23.md memory/builds/aRepatriatedFork/build/2026-09-29-build-TOOL-aRepatriatedFork-23-1-acceptance-ledger.md memory/builds/aRepatriatedFork/README.md

2026-09-29T12:11:52Z rescope · item add TOOL-aRepatriatedFork-44 · reason TOOL-23's widened ledger names the fixture incms-2cff5855.receipt.json; its filename carries an adopter name TOOL-35's scrub missed, which govkit selfcheck arm 10 refuses

2026-09-29T12:17:26Z dispatch · item 1b3c6fac TOOL-aRepatriatedFork-44 · reason tools/govkit/fixtures/incms-2cff5855.receipt.json tools/govkit/fixtures/adopter-ic-2cff5855.receipt.json tools/govkit/fixtures/make_adopter_receipt.py tools/govkit/selftest.py tools/dead-path-waivers.txt memory/builds/aRepatriatedFork/spec/2026-09-29-spec-TOOL-aRepatriatedFork-44.md memory/builds/aRepatriatedFork/build/2026-09-29-build-TOOL-aRepatriatedFork-44-1-acceptance-ledger.md memory/builds/aRepatriatedFork/README.md

2026-09-29T13:06:56Z rescope · item add TOOL-aRepatriatedFork-45 · reason TOOL-44's rename showed check-dead-paths.sh builds its dead-name needles from deleted files only, so a git mv leaves the old name ungated; a planted citation of the renamed-away fixture exited 0. Built after the drain.

2026-09-29T14:15:33Z dispatch · item 1de8126a TOOL-aRepatriatedFork-24 · reason .githooks/pre-commit .githooks/pre-commit.test.sh .githooks/pre-push .githooks/pre-push.test.sh .githooks/pre_push_bar_selftest.py .githooks/gate-env.sh tools/unattended/adopt-unattended.sh tools/unattended/.unattended.conf.example tools/unattended/unattended.sh tools/check-microformats.test.sh tools/check-placeholders.test.sh tools/check-wiring.test.sh tools/check-wiring.sh tools/codebase-map/selftest.py tools/govkit/govkit.py tools/govkit/selftest.py skills/session-kickoff/manifest-check.sh tools/install-prefix-waivers.txt tools/install-prefix-carried.txt tools/agent-instructions/kit.toml tools/gate-lint/kit.toml tools/govkit/entries/check-agent-cap-restatement.kit.toml tools/govkit/entries/check-install-prefix.kit.toml tools/govkit/entries/check-kit-versions.kit.toml tools/govkit/entries/check-placeholders.kit.toml tools/govkit/entries/push-main.kit.toml memory/builds/aRepatriatedFork/spec/2026-09-25-spec-TOOL-aRepatriatedFork-24.md memory/builds/aRepatriatedFork/build/2026-09-29-build-TOOL-aRepatriatedFork-24-1-acceptance-ledger.md memory/builds/aRepatriatedFork/README.md memory/guides/SESSION-KICKOFF.md memory/LIVE.md memory/ledger

2026-09-29T14:18:17Z dispatch · item 1de8126a TOOL-aRepatriatedFork-24 · reason .githooks/pre-commit .githooks/pre-commit.test.sh .githooks/pre-push .githooks/pre-push.test.sh .githooks/pre-push.runlog.test.sh .githooks/pre_push_bar_selftest.py .githooks/gate-env.sh tools/unattended/adopt-unattended.sh tools/unattended/adopt-unattended.test.sh tools/unattended/.unattended.conf.example tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/check-microformats.test.sh tools/check-placeholders.test.sh tools/check-wiring.test.sh tools/check-wiring.sh tools/codebase-map/selftest.py tools/govkit/govkit.py tools/govkit/selftest.py skills/session-kickoff/manifest-check.sh tools/install-prefix-waivers.txt tools/install-prefix-carried.txt tools/agent-instructions/kit.toml tools/gate-lint/kit.toml tools/govkit/entries/check-agent-cap-restatement.kit.toml tools/govkit/entries/check-install-prefix.kit.toml tools/govkit/entries/check-kit-versions.kit.toml tools/govkit/entries/check-placeholders.kit.toml tools/govkit/entries/push-main.kit.toml memory/builds/aRepatriatedFork/spec/2026-09-25-spec-TOOL-aRepatriatedFork-24.md memory/builds/aRepatriatedFork/build/2026-09-29-build-TOOL-aRepatriatedFork-24-1-acceptance-ledger.md memory/builds/aRepatriatedFork/README.md memory/guides/SESSION-KICKOFF.md memory/LIVE.md memory/ledger

2026-09-29T15:03:01Z dispatch · item 2702b4bf TOOL-aRepatriatedFork-24 · reason .githooks/pre-commit .githooks/pre-commit.test.sh .githooks/pre-push .githooks/pre-push.test.sh .githooks/pre-push.runlog.test.sh .githooks/pre_push_bar_selftest.py .githooks/gate-env.sh tools/unattended/adopt-unattended.sh tools/unattended/adopt-unattended.test.sh tools/unattended/.unattended.conf.example tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/check-microformats.test.sh tools/check-placeholders.test.sh tools/check-wiring.test.sh tools/check-wiring.sh tools/codebase-map/selftest.py tools/govkit/govkit.py tools/govkit/selftest.py skills/session-kickoff/manifest-check.sh tools/install-prefix-waivers.txt tools/install-prefix-carried.txt tools/agent-instructions/kit.toml tools/gate-lint/kit.toml tools/govkit/entries/check-agent-cap-restatement.kit.toml tools/govkit/entries/check-install-prefix.kit.toml tools/govkit/entries/check-kit-versions.kit.toml tools/govkit/entries/check-placeholders.kit.toml tools/govkit/entries/push-main.kit.toml memory/builds/aRepatriatedFork/spec/2026-09-25-spec-TOOL-aRepatriatedFork-24.md memory/builds/aRepatriatedFork/build/2026-09-29-build-TOOL-aRepatriatedFork-24-1-acceptance-ledger.md memory/builds/aRepatriatedFork/README.md memory/guides/SESSION-KICKOFF.md memory/LIVE.md memory/ledger .claude/skills/unattended/SKILL.md memory/guides/PLAYBOOK-TEMPLATE.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/UNATTENDED-VERBS.md tools/unattended/PLAYBOOK-TEMPLATE.template.md tools/unattended/PROTOCOL.template.md tools/unattended/README.md tools/unattended/SKILL.template.md tools/unattended/VERBS.template.md tools/unattended/check-brief-recorded.sh tools/unattended/check-pass-order.sh tools/unattended/check-unattended.sh tools/unattended/fixture-record-one.template.md tools/unattended/fixture-record-two.template.md tools/unattended/fixture-records/tools~unattended~fixture-pieces~one~piece.md.md tools/unattended/fixture-records/tools~unattended~fixture-pieces~two~piece.md.md tools/unattended/gate-guard.js tools/unattended/playbook.fixture.md tools/unattended/playbook.fixture.template.md tools/unattended/run-lease.js tools/unattended/stall-recorder.js tools/unattended/stop-guard.js tools/unattended/unattended.sh
