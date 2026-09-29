# aRepatriatedFork - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 860a824149ecec9b026a21097f2e2b7a181c7c0f
phase: BUILDING
mode: slug
run-branch: refs/heads/branch/arepatriated-fork-build-e42158
anchor-kind: default-branch
lease-utc: 2026-09-29T11:02:51Z
pid-image: claude.exe
host: compeeto-agent
pid: 11996
session: 3b534792-4ade-4a9d-8dfa-4cb264c0af0d
keepalive: b1bc1d24
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
