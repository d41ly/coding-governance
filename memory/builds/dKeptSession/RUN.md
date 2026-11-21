# dKeptSession - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: a4dd146d6773f436a4527d2a9740a7beec69e405
phase: BUILDING
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dkeptsession-a0567a
anchor-kind: default-branch
cli-version: 2.1.326
lease-utc: 2026-11-21T12:17:07Z
pid-image: claude.exe
host: compeeto
pid: 29104
session: d5b6d4ab-72df-4e61-9a7c-05dde93b7f5b
keepalive: f586eb4e
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: c2a407b0390f3d57a118b58e376c326aeb207c13
anchor-ref: refs/heads/main
base: c2a407b0390f3d57a118b58e376c326aeb207c13

## Parked

2026-11-21T13:26:22Z brief · item KICK-dKeptSession-1 · reason b9a738e8e603 memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md

2026-11-21T13:27:22Z dispatch · item a4dd146d KICK-dKeptSession-1 · reason tools/policy/presets.toml tools/policy/presets.py tools/policy/policy.py tools/policy/check_policy.py tools/policy/README.md tools/loop/guard.py tools/loop/loop.toml tools/loop/factories.py tools/loop/README.md tools/playbook/kinds.toml tools/playbook/core-pending.txt help/reference/kinds.md help/policy.md
2026-11-21T14:01:58Z budget · frozen · 64 unit(s) · 132
2026-11-21T14:01:58Z draw · re-dispatch · KICK-dKeptSession-1 · 1/132 · 20261121T140158Z-b911aa

2026-11-21T14:01:58Z dispatch · item a186ba16 KICK-dKeptSession-1 · reason tools/policy/presets.toml tools/policy/presets.py tools/policy/policy.py tools/policy/check_policy.py tools/policy/README.md tools/loop/guard.py tools/loop/loop.toml tools/loop/factories.py tools/loop/README.md tools/playbook/kinds.toml tools/playbook/core-pending.txt tools/gate-legs.json help/reference/kinds.md help/policy.md memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-1-1-acceptance-ledger.md
