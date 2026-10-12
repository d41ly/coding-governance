# aHeardState - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
hold-run: 
hold-streak: 1 · at 12cb2e1b
resume-owed: none · owner
held-at: 2026-10-12T19:59:59Z
hold-reason: the owner paused the run to reboot node a: about 26 GB of leaked kernel pool after 7 days up made each spawn cost 260-740 ms and pushed the claim push past its bound; unit 1 is built and amended, unit 2 is SPECCED with its code drafted but not placed
hold-until: owner
hold-code: host-owner-action
held-from: BUILDING
refreshed-at: 6e8f8b1da4dc036b7fce23555b78fb4b5db0e60c · park · 13 touching
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 9ea947136
phase: VERIFYING
may: none
mode: prompt
run-branch: refs/heads/branch/aHeardState
anchor-kind: local
cli-version: 2.1.293
lease-utc: 2026-10-12T21:27:33Z
pid-image: claude.exe
host: compeeto-agent
pid: 12396
session: 7ecabc14-b395-43a9-8f32-9e036af87174
keepalive: 4fa4ef2e
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 13fe6a04dfac854847b87419641b5c546a0385e9
anchor-ref: refs/heads/main
base: 6b32af422bc2c02d067c2fc0887627f95404de0f

## Parked

2026-10-12T16:33:00Z brief · item TOOL-aHeardState-1 · reason b9d32e7b75fa memory/builds/aHeardState/prompts/2026-10-11-prompt-TOOL-aHeardState-1-1-brief.md

2026-10-12T16:33:44Z brief · item TOOL-aHeardState-2 · reason b9d32e7b75fa memory/builds/aHeardState/prompts/2026-10-11-prompt-TOOL-aHeardState-1-1-brief.md

2026-10-12T16:46:25Z dispatch · item 2d0dd234 TOOL-aHeardState-1 · reason tools/hooks/format-guard.js tools/hooks/format-guard.fragment.json tools/hooks/format-guard.test.sh tools/hooks/scratch-guard.js tools/hooks/kit.toml tools/hooks/README.md .claude/settings.json tools/gate-legs.json tools/govkit/registry.toml memory/map/features/agent-cap.md memory/map/generated/inventories.json memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md

2026-10-12T17:06:38Z dispatch · item 2d0dd234 TOOL-aHeardState-1 · reason tools/hooks/format-guard.js tools/hooks/format-guard.fragment.json tools/hooks/format-guard.test.sh tools/hooks/scratch-guard.js tools/hooks/kit.toml tools/hooks/README.md .claude/settings.json tools/gate-legs.json tools/govkit/registry.toml memory/map/features/agent-cap.md memory/map/generated/inventories.json memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/guides/SESSION-KICKOFF.md

2026-10-12T19:45:28Z dispatch · item 0a2162b9 TOOL-aHeardState-1 · reason memory/builds/aHeardState/spec/2026-10-11-spec-TOOL-aHeardState-1.md memory/builds/aHeardState/build/2026-10-12-build-TOOL-aHeardState-1-1-live-witness.md

2026-10-12T19:47:28Z decision · item stop-guard is dark for a run whose session was launched in another worktree and moved to the run's tree: this run's session drew no run-open block at a BUILDING turn end · reason options: (a) the unattended kit's preflight refuses a session whose CLAUDE_PROJECT_DIR is not the run's tree; (b) the protocol tells the prompt path to relaunch the session in the new worktree; (c) record it as a gotcha only. Refused here: it changes the unattended kit, outside this build's mandate, and rests on an inference from two silent hooks (build record 2026-10-12-build-TOOL-aHeardState-1-1-live-witness.md)

2026-10-12T20:00:34Z hold · item host-owner-action · reason until owner · reaped 81987d49 · resume none(owner)

2026-10-12T21:27:39Z resume · item aHeardState · reason held · keepalive 4fa4ef2e · manual

2026-10-12T21:28:24Z dispatch · item 4110a669 TOOL-aHeardState-2 · reason memory/builds/aHeardState/spec/2026-10-11-spec-TOOL-aHeardState-2.md

2026-10-12T21:30:08Z dispatch · item b8c9b136 TOOL-aHeardState-2 · reason tools/runlog/prose.py tools/runlog/runlog.py tools/runlog/selftest.py tools/runlog/kit.toml tools/runlog/fixtures/prose.json tools/runlog/README.md tools/hooks/format-guard.test.sh memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/inventories.json

2026-10-12T21:34:52Z dispatch · item 50e2420f TOOL-aHeardState-2 · reason tools/hooks/agent-cap.js tools/hooks/scratch-guard.js tools/hooks/format-guard.js tools/runlog/runlog_lib.py tools/runlog/README.md tools/runlog/adopt-runlog.sh tools/runlog/extract.py tools/runlog/model.py tools/runlog/record.py tools/runlog/runlog.py tools/runlog/selftest.py tools/runlog/prose.py tools/playbook/render_playbook.py

2026-10-12T21:49:01Z review · item aHeardState · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · highs 5 · minors 18 · disposition promote

2026-10-12T21:49:43Z rescope · item add TOOL-aHeardState-3 · reason closing review round 1 id 8 (HIGH): the format-guard self-test leg has no subject pin and no budget row

2026-10-12T21:49:52Z rescope · item add TOOL-aHeardState-4 · reason closing review round 1 id 9 (HIGH): the new {prefix}/hooks/ guard tips hooks/ past BROAD_LEG_FLOOR and out of the spec-tokens join

2026-10-12T21:49:53Z rescope · item add TOOL-aHeardState-5 · reason closing review round 1 id 10 (HIGH): the format-guard self-test guard omits the runlog files its parity arm reads

2026-10-12T21:49:55Z rescope · item add TOOL-aHeardState-6 · reason closing review round 1 id 14 (HIGH): the same narrow-guard defect from the intent lens; its unit records the class in the bug-class checklist

2026-10-12T21:49:56Z rescope · item add TOOL-aHeardState-7 · reason closing review round 1 id 3 (HIGH): the format-guard header says continuation commits are absorbed, and the code demands them

2026-10-12T21:49:57Z rescope · item add TOOL-aHeardState-8 · reason closing review round 1: the 18 MEDIUM and LOW findings, batched into one unit

2026-10-12T21:53:05Z brief · item TOOL-aHeardState-3 · reason b9d32e7b75fa memory/builds/aHeardState/prompts/2026-10-11-prompt-TOOL-aHeardState-1-1-brief.md

2026-10-12T21:53:07Z brief · item TOOL-aHeardState-4 · reason b9d32e7b75fa memory/builds/aHeardState/prompts/2026-10-11-prompt-TOOL-aHeardState-1-1-brief.md

2026-10-12T21:53:09Z brief · item TOOL-aHeardState-5 · reason b9d32e7b75fa memory/builds/aHeardState/prompts/2026-10-11-prompt-TOOL-aHeardState-1-1-brief.md

2026-10-12T21:53:11Z brief · item TOOL-aHeardState-6 · reason b9d32e7b75fa memory/builds/aHeardState/prompts/2026-10-11-prompt-TOOL-aHeardState-1-1-brief.md

2026-10-12T21:53:12Z brief · item TOOL-aHeardState-7 · reason b9d32e7b75fa memory/builds/aHeardState/prompts/2026-10-11-prompt-TOOL-aHeardState-1-1-brief.md

2026-10-12T21:53:13Z brief · item TOOL-aHeardState-8 · reason b9d32e7b75fa memory/builds/aHeardState/prompts/2026-10-11-prompt-TOOL-aHeardState-1-1-brief.md

2026-10-12T21:54:30Z dispatch · item 7267f93e TOOL-aHeardState-3 · reason tools/govkit/subject-pins.tsv tools/run-gates/selftest-budgets.txt

2026-10-12T21:56:37Z dispatch · item 42a3992d TOOL-aHeardState-4 · reason memory/builds/aHeardState/spec/2026-10-13-spec-TOOL-aHeardState-4.md tools/gate-legs.json memory/guides/SESSION-KICKOFF.md

2026-10-12T21:58:04Z dispatch · item bb3654ac TOOL-aHeardState-4 · reason tools/gate-legs.json memory/guides/SESSION-KICKOFF.md

2026-10-12T22:01:08Z dispatch · item 588fb282 TOOL-aHeardState-5 · reason tools/gate-legs.json memory/guides/SESSION-KICKOFF.md

2026-10-12T22:02:01Z dispatch · item b357641e TOOL-aHeardState-6 · reason memory/gotchas/held-suite-guard-misses-a-sibling-kit.md memory/map/features/agent-cap.md

2026-10-12T22:02:20Z dispatch · item b357641e TOOL-aHeardState-6 · reason memory/gotchas/held-suite-guard-misses-a-sibling-kit.md memory/gotchas/INDEX.md memory/map/features/agent-cap.md

2026-10-12T22:03:10Z dispatch · item f1d88c60 TOOL-aHeardState-7 · reason tools/hooks/format-guard.js tools/hooks/format-guard.test.sh

2026-10-12T22:05:16Z dispatch · item f1d88c60 TOOL-aHeardState-7 · reason tools/hooks/format-guard.js tools/hooks/format-guard.test.sh memory/map/generated/inventories.json memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md

2026-10-12T22:06:35Z dispatch · item 0604ee9f TOOL-aHeardState-8 · reason tools/hooks/format-guard.js tools/hooks/format-guard.test.sh tools/runlog/prose.py tools/runlog/selftest.py tools/runlog/kit.toml tools/runlog/fixtures/prose.json tools/runlog/fixtures/prose-charter.md memory/map/generated/inventories.json memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md

2026-10-12T22:11:56Z dispatch · item 53d686b2 TOOL-aHeardState-8 · reason tools/hooks/agent-cap.js tools/hooks/scratch-guard.js tools/hooks/format-guard.js tools/runlog/runlog_lib.py tools/runlog/README.md tools/runlog/adopt-runlog.sh tools/runlog/extract.py tools/runlog/model.py tools/runlog/record.py tools/runlog/runlog.py tools/runlog/selftest.py tools/runlog/prose.py

2026-10-12T22:14:46Z dispatch · item 5742dae9 TOOL-aHeardState-3 · reason tools/run-gates/selftest-budgets.txt
