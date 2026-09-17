# cMendedVintage - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 1f42235793aedbff4ab821b4dd777e404d345abb
phase: BUILDING
branch-sha: 859daa67e728ae273d5278536fb462c04077f16f
branch-ref: refs/heads/branch/govkit-update-rollbacks-0502c4
mode: prompt
run-branch: refs/heads/branch/govkit-update-rollbacks-0502c4
anchor-kind: run-branch
keepalive: 84ee75f8
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 4cf0944dbdce94714870f26760936bc5edabc64e
anchor-ref: refs/heads/main
base: 859daa67e728ae273d5278536fb462c04077f16f

## Parked

2026-09-16T12:43:39Z decision · item The charter's §16 R1 requires an emitted micro-format to be a markdown list item ('- ' at column 0), but skills/session-kickoff/manifest-check.sh:478 counts READY lines with grep -c '^READY — ', anchored at column 0 with no list marker. A card body that follows the charter is read as carrying NO ready line: the append reports success, leaves the 'READY — none yet' sentinel in place, skips the tree-cell re-render, and the scratch-guard then blocks the session's next commit. · reason Two options and both change a governance carrier, which M3 veto 2 reserves to the owner. Either §16 R1 gains an explicit carve-out for a machine-read on-disk record, or manifest-check.sh accepts an optional leading '- ' on the lines it anchors. I will not pick: the charter is the carrier this repo is most careful about, and the fix is one line either way. Observed live this run — it cost 71 minutes and a refused commit.

2026-09-16T12:43:51Z rescope · item add TOOL-cMendedVintage-9 · reason Building uncovered it: manifest-check.sh:128 resolves the session id by reading stdin for the SessionStart hook's JSON, guarded only by '[ -t 0 ]'. That covers the hook (pipe then EOF) and a human at a terminal, but not stdin being an open pipe that never sends EOF — which is what every tool-invoked shell has. --card --write then blocks in sed forever: measured 71 minutes at 4.4s CPU with no children, cleared instantly with '< /dev/null'. Passing --session does not avoid it, because the stdin read runs first and CARD_SID is only the fallback. The skill's own Step 5 prescribes this exact invocation as the card repair, so the documented remedy hangs. Strictly beneficial, no veto tripped (a kit engine, not a governance carrier), and it is a blocker between this run and its own landing.

2026-09-16T16:08:37Z review · item cMendedVintage-spec-set-r1 · reason verdict BLOCKED · blockers 1 · BOUNDED · disposition promote

2026-09-16T16:12:01Z rescope · item add DEPL-cMendedVintage-15 · reason promoted from review record 2026-09-16-review-cMendedVintage-spec-set-spec-audit-round1 finding B1 at severity blocker, disposed by BUILD-METHOD M4 which admits no other route for a blocker or a high

2026-09-16T16:12:03Z rescope · item add DEPL-cMendedVintage-16 · reason promoted from review record 2026-09-16-review-cMendedVintage-spec-set-spec-audit-round1 finding H1 at severity high, disposed by BUILD-METHOD M4 which admits no other route for a blocker or a high

2026-09-16T16:12:06Z rescope · item add DEPL-cMendedVintage-17 · reason promoted from review record 2026-09-16-review-cMendedVintage-spec-set-spec-audit-round1 finding H2 at severity high, disposed by BUILD-METHOD M4 which admits no other route for a blocker or a high

2026-09-16T16:12:09Z rescope · item add DEPL-cMendedVintage-18 · reason promoted from review record 2026-09-16-review-cMendedVintage-spec-set-spec-audit-round1 finding H3 at severity high, disposed by BUILD-METHOD M4 which admits no other route for a blocker or a high

2026-09-16T16:12:11Z rescope · item add DEPL-cMendedVintage-19 · reason promoted from review record 2026-09-16-review-cMendedVintage-spec-set-spec-audit-round1 finding H4 at severity high, disposed by BUILD-METHOD M4 which admits no other route for a blocker or a high

2026-09-16T16:12:14Z rescope · item add DEPL-cMendedVintage-20 · reason promoted from review record 2026-09-16-review-cMendedVintage-spec-set-spec-audit-round1 finding H5 at severity high, disposed by BUILD-METHOD M4 which admits no other route for a blocker or a high

2026-09-16T16:12:16Z rescope · item add DEPL-cMendedVintage-21 · reason promoted from review record 2026-09-16-review-cMendedVintage-spec-set-spec-audit-round1 finding H6 at severity high, disposed by BUILD-METHOD M4 which admits no other route for a blocker or a high

2026-09-16T17:15:48Z decision · item unattended-build.js's disposal reconciliation compares disposed ROWS against raw CONFIRMED findings, so a legitimate synthesis-time merge of two raw findings into one row reports DEGRADED and withholds the roster. Hit live this run: 14 confirmed collapsed to 13 rows because raw 14 and raw 25 were the same defect on the same two sentences of DEPL-cMendedVintage-10, reached from two directions. Every finding WAS disposed - 7 promoted with specs and rescope rows on disk, 6 folded as rev-2 bumps with section 9 lines - and I verified both halves by hand before proceeding. · reason The obvious fix, relaxing the equality, is NOT strictly beneficial: that arithmetic is the only thing standing between a dropped finding and a roster handed out as if nothing were missing, and relaxing it makes a real drop invisible. The correct fix is for the synthesis stage to emit an explicit merge map the reconciliation can consume, which is a design change in another kit and outside this build's goal. So this is neither an adoption nor a backlog row I may mint: a cMendedVintage id for work this build will not do would put a specless unit in its own roster and block build-complete. Owner decides.

2026-09-16T17:20:45Z dispatch · item 09c9415a TOOL-cMendedVintage-9 · reason skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh

2026-09-16T17:21:24Z brief · item TOOL-cMendedVintage-9 · reason 3b5378a72ff0 memory/builds/cMendedVintage/prompts/2026-09-16-prompt-TOOL-cMendedVintage-9-2-build-brief.md

2026-09-16T17:22:15Z dispatch · item 09c9415a TOOL-cMendedVintage-9 · reason skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh memory/builds/cMendedVintage/spec/2026-09-16-spec-TOOL-cMendedVintage-9.md

2026-09-16T17:29:04Z dispatch · item 09c9415a TOOL-cMendedVintage-9 · reason skills/session-kickoff/manifest-check.sh skills/session-kickoff/manifest-check.test.sh memory/builds/cMendedVintage/spec/2026-09-16-spec-TOOL-cMendedVintage-9.md memory/builds/cMendedVintage/README.md memory/builds/cMendedVintage/build/2026-09-16-build-TOOL-cMendedVintage-9-acceptance-ledger.md memory/guides/SESSION-KICKOFF.md

2026-09-16T17:36:36Z dispatch · item 1900b591 DEPL-cMendedVintage-1 · reason tools/govkit/govkit.py tools/govkit/selftest.py

2026-09-16T17:36:37Z brief · item DEPL-cMendedVintage-1 · reason aa8c0a836794 memory/builds/cMendedVintage/prompts/2026-09-16-prompt-DEPL-cMendedVintage-1-2-build-brief.md

2026-09-16T17:39:29Z dispatch · item 1900b591 DEPL-cMendedVintage-1 · reason tools/govkit/govkit.py tools/govkit/selftest.py WIRE-INTO-PROJECT.md memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-1.md

2026-09-16T17:48:17Z dispatch · item 56055917 DEPL-cMendedVintage-1 · reason tools/govkit/govkit.py tools/govkit/selftest.py WIRE-INTO-PROJECT.md tools/workflows/README.md memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-1.md

2026-09-16T17:51:24Z dispatch · item 03ba97f1 DEPL-cMendedVintage-2 · reason tools/govkit/govkit.py tools/govkit/selftest.py

2026-09-16T17:51:25Z brief · item DEPL-cMendedVintage-2 · reason d4e603c689f7 memory/builds/cMendedVintage/prompts/2026-09-16-prompt-DEPL-cMendedVintage-2-2-build-brief.md

2026-09-16T17:54:56Z dispatch · item 03ba97f1 DEPL-cMendedVintage-2 · reason tools/govkit/govkit.py tools/govkit/selftest.py WIRE-INTO-PROJECT.md memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-2.md memory/LIVE.md

2026-09-16T18:05:59Z dispatch · item 03ba97f1 DEPL-cMendedVintage-2 · reason tools/govkit/govkit.py tools/govkit/selftest.py WIRE-INTO-PROJECT.md memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-2.md memory/builds/cMendedVintage/README.md memory/LIVE.md

2026-09-16T18:12:31Z dispatch · item 96cab2de DEPL-cMendedVintage-3 · reason tools/govkit/govkit.py tools/govkit/selftest.py

2026-09-16T18:12:32Z brief · item DEPL-cMendedVintage-3 · reason 0b97a85037a7 memory/builds/cMendedVintage/prompts/2026-09-16-prompt-DEPL-cMendedVintage-3-2-build-brief.md

2026-09-16T18:15:05Z dispatch · item 96cab2de DEPL-cMendedVintage-3 · reason tools/govkit/govkit.py tools/govkit/selftest.py memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-3.md

2026-09-16T18:25:59Z dispatch · item 30352c6a DEPL-cMendedVintage-4 · reason tools/govkit/govkit.py tools/govkit/selftest.py WIRE-INTO-PROJECT.md

2026-09-16T18:26:00Z brief · item DEPL-cMendedVintage-4 · reason 8c9d217fb319 memory/builds/cMendedVintage/prompts/2026-09-16-prompt-DEPL-cMendedVintage-4-2-build-brief.md

2026-09-16T18:28:57Z dispatch · item 30352c6a DEPL-cMendedVintage-4 · reason tools/govkit/govkit.py tools/govkit/selftest.py WIRE-INTO-PROJECT.md memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-4.md memory/LIVE.md

2026-09-16T18:46:26Z dispatch · item 7941c2dd DEPL-cMendedVintage-5 · reason tools/lexicon/kit.toml tools/drift-audit/kit.toml tools/memory-recall/kit.toml

2026-09-16T18:46:27Z brief · item DEPL-cMendedVintage-5 · reason 4300ebe58773 memory/builds/cMendedVintage/prompts/2026-09-16-prompt-DEPL-cMendedVintage-5-2-build-brief.md

2026-09-16T18:50:15Z dispatch · item 7941c2dd DEPL-cMendedVintage-5 · reason tools/lexicon/kit.toml tools/lexicon/lexicon.py tools/lexicon/canon.py tools/lexicon/LEXICON.md tools/lexicon/README.md .claude/skills/lexicon/SKILL.md tools/drift-audit/kit.toml tools/drift-audit/drift_report.py tools/drift-audit/adopt-drift-audit.sh tools/drift-audit/drift_signals.py tools/drift-audit/drift_signals.template.py tools/drift-audit/README.md tools/drift-audit/selftest.py tools/workflows/drift-audit-code.js tools/workflows/drift-audit-state.js tools/memory-recall/kit.toml tools/memory-recall/recall_conf.py tools/memory-recall/README.md memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-5.md

2026-09-16T19:10:19Z dispatch · item 9597176f DEPL-cMendedVintage-16 · reason tools/govkit/govkit.py tools/lexicon/kit.toml tools/govkit/matrix.py

2026-09-16T19:10:21Z brief · item DEPL-cMendedVintage-16 · reason c0f4066d3aa6 memory/builds/cMendedVintage/prompts/2026-09-16-prompt-DEPL-cMendedVintage-16-2-build-brief.md

2026-09-16T19:18:43Z dispatch · item 9597176f DEPL-cMendedVintage-16 · reason tools/lexicon/kit.toml tools/govkit/matrix.py tools/lexicon/README.md memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-16.md memory/LIVE.md

2026-09-16T19:24:45Z dispatch · item 9597176f DEPL-cMendedVintage-16 · reason tools/lexicon/kit.toml tools/govkit/matrix.py tools/lexicon/README.md memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-16.md memory/builds/cMendedVintage/README.md

2026-09-16T19:32:00Z dispatch · item 52f1612f TOOL-cMendedVintage-1 · reason tools/memory-tree/adopt-memory-tree.sh tools/memory-tree/kit.toml

2026-09-16T19:32:02Z brief · item TOOL-cMendedVintage-1 · reason d54944afbe21 memory/builds/cMendedVintage/prompts/2026-09-16-prompt-TOOL-cMendedVintage-1-2-build-brief.md

2026-09-16T19:36:13Z dispatch · item 52f1612f TOOL-cMendedVintage-1 · reason tools/memory-tree/adopt-memory-tree.sh tools/memory-tree/kit.toml tools/memory-tree/check-memory-hygiene.sh tools/memory-tree/README.md tools/memory-tree/HYGIENE.template.md tools/memory-tree/SPEC-TEMPLATE.template.md tools/memory-tree/BUILD-METHOD.template.md tools/memory-tree/ANNOTATION-STYLE.template.md memory/HYGIENE.md memory/TEMPLATE-SPEC.md memory/guides/BUILD-METHOD.md memory/guides/ANNOTATION-STYLE.md memory/builds/cMendedVintage/spec/2026-09-16-spec-TOOL-cMendedVintage-1.md memory/LIVE.md

2026-09-16T19:48:13Z decision · item A dispatched pass can commit files outside its declared --writes set and nothing refuses it. TOOL-cMendedVintage-1 declared two paths and committed seventeen: a kit version bump rippled to four templates, a README and check-memory-hygiene.sh, and a pre-commit manifest re-stamp added memory/guides/SESSION-KICKOFF.md. The builder reported this honestly; no verb, hook or gate raised it. · reason BUILD-METHOD M6 condition 1 proves two concurrent passes disjoint from their DECLARED write sets, and the skill tells a pass to re-declare WIDER before committing. But the declaration is taken at dispatch time and never compared against the commit, so the proof rests on a promise rather than an observation. It cost nothing here because no sibling pass was open — the verb said so explicitly, 'condition 1 is a proof over an empty set' — but under real concurrency two passes could overlap with both declarations still looking disjoint. Out of this build's scope, and the fix is a design question for the unattended kit rather than a predicate I should invent mid-run: comparing a commit against its declaration needs a rule for the legitimate ripples, which a version bump and a hook re-stamp both are.

2026-09-16T19:49:27Z dispatch · item 8a8529b1 DEPL-cMendedVintage-6 · reason tools/unattended/kit.toml tools/unattended/adopt-unattended.sh tools/unattended/fixture-records/tools~unattended~fixture-pieces~one~piece.md.md tools/unattended/fixture-records/tools~unattended~fixture-pieces~two~piece.md.md

2026-09-16T19:49:29Z brief · item DEPL-cMendedVintage-6 · reason 1ba412f3082a memory/builds/cMendedVintage/prompts/2026-09-16-prompt-DEPL-cMendedVintage-6-2-build-brief.md

2026-09-16T19:55:42Z dispatch · item 8a8529b1 DEPL-cMendedVintage-6 · reason tools/unattended/kit.toml tools/unattended/adopt-unattended.sh tools/unattended/fixture-record-one.template.md tools/unattended/fixture-record-two.template.md tools/unattended/unattended.sh tools/unattended/check-unattended.sh tools/unattended/check-pass-order.sh tools/unattended/check-brief-recorded.sh tools/unattended/README.md memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-6.md memory/LIVE.md

2026-09-16T20:07:19Z dispatch · item 8a8529b1 DEPL-cMendedVintage-6 · reason tools/unattended/kit.toml tools/unattended/adopt-unattended.sh tools/unattended/fixture-record-one.template.md tools/unattended/fixture-record-two.template.md tools/unattended/fixture-records/tools~unattended~fixture-pieces~one~piece.md.md tools/unattended/fixture-records/tools~unattended~fixture-pieces~two~piece.md.md tools/unattended/unattended.sh tools/unattended/check-unattended.sh tools/unattended/check-pass-order.sh tools/unattended/check-brief-recorded.sh tools/unattended/README.md tools/unattended/PLAYBOOK-TEMPLATE.template.md tools/unattended/PROTOCOL.template.md tools/unattended/SKILL.template.md tools/unattended/VERBS.template.md tools/unattended/playbook.fixture.template.md tools/unattended/playbook.fixture.md tools/unattended/gate-guard.js .claude/skills/unattended/SKILL.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/PLAYBOOK-TEMPLATE.md memory/guides/UNATTENDED-VERBS.md memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-6.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-16T20:09:24Z dispatch · item 8a8529b1 DEPL-cMendedVintage-6 · reason tools/unattended/kit.toml tools/unattended/adopt-unattended.sh tools/unattended/fixture-record-one.template.md tools/unattended/fixture-record-two.template.md tools/unattended/fixture-records/tools~unattended~fixture-pieces~one~piece.md.md tools/unattended/fixture-records/tools~unattended~fixture-pieces~two~piece.md.md tools/unattended/unattended.sh tools/unattended/check-unattended.sh tools/unattended/check-pass-order.sh tools/unattended/check-brief-recorded.sh tools/unattended/README.md tools/unattended/PLAYBOOK-TEMPLATE.template.md tools/unattended/PROTOCOL.template.md tools/unattended/SKILL.template.md tools/unattended/VERBS.template.md tools/unattended/playbook.fixture.template.md tools/unattended/playbook.fixture.md tools/unattended/gate-guard.js .claude/skills/unattended/SKILL.md memory/guides/UNATTENDED-PROTOCOL.md memory/guides/PLAYBOOK-TEMPLATE.md memory/guides/UNATTENDED-VERBS.md memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-6.md memory/builds/cMendedVintage/README.md

2026-09-16T20:15:06Z dispatch · item 0ddee337 DEPL-cMendedVintage-7 · reason tools/govkit/govkit.py tools/govkit/selftest.py tools/unattended/kit.toml tools/workflows/kit.toml tools/workflows/README.md

2026-09-16T20:15:07Z brief · item DEPL-cMendedVintage-7 · reason 3f486e666da1 memory/builds/cMendedVintage/prompts/2026-09-16-prompt-DEPL-cMendedVintage-7-2-build-brief.md

2026-09-16T20:20:15Z dispatch · item 0ddee337 DEPL-cMendedVintage-7 · reason tools/govkit/govkit.py,tools/govkit/selftest.py,tools/drift-audit/kit.toml,tools/lexicon/kit.toml,tools/memory-recall/kit.toml,tools/memory-tree/kit.toml,tools/unattended/kit.toml,tools/workflows/kit.toml,tools/workflows/README.md,tools/workflows/check-protocol-parity.test.sh,tools/workflows/unattended-build.test.sh,WIRE-INTO-PROJECT.md,memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-7.md,memory/builds/cMendedVintage/RUN.md,memory/LIVE.md

2026-09-16T20:32:09Z dispatch · item e6612579 DEPL-cMendedVintage-8 · reason tools/govkit/govkit.py tools/govkit/selftest.py

2026-09-16T20:32:10Z brief · item DEPL-cMendedVintage-8 · reason 9107164ffeb8 memory/builds/cMendedVintage/prompts/2026-09-16-prompt-DEPL-cMendedVintage-8-2-build-brief.md

2026-09-16T20:35:38Z dispatch · item e6612579 DEPL-cMendedVintage-8 · reason tools/govkit/govkit.py tools/govkit/selftest.py memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-8.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-16T20:42:30Z dispatch · item e6612579 DEPL-cMendedVintage-8 · reason tools/govkit/govkit.py tools/govkit/selftest.py memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-8.md memory/builds/cMendedVintage/README.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-16T20:49:26Z dispatch · item 8295fb18 TOOL-cMendedVintage-2 · reason tools/gate-lint/sh_hygiene.py tools/gate-lint/kit.toml tools/gate-lint/README.md tools/gate-lint/substitution-fed-loops.template.txt

2026-09-16T20:49:27Z brief · item TOOL-cMendedVintage-2 · reason 60f0e1284b9a memory/builds/cMendedVintage/prompts/2026-09-16-prompt-TOOL-cMendedVintage-2-2-build-brief.md

2026-09-16T20:53:38Z dispatch · item 8295fb18 TOOL-cMendedVintage-2 · reason tools/gate-lint/sh_hygiene.py tools/gate-lint/kit.toml tools/gate-lint/README.md tools/gate-lint/substitution-fed-loops.template.txt memory/map/features/gate-lint.md memory/builds/cMendedVintage/spec/2026-09-16-spec-TOOL-cMendedVintage-2.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-16T21:02:04Z dispatch · item 8295fb18 TOOL-cMendedVintage-2 · reason tools/gate-lint/sh_hygiene.py tools/gate-lint/kit.toml tools/gate-lint/README.md tools/gate-lint/substitution-fed-loops.template.txt memory/map/features/gate-lint.md memory/builds/cMendedVintage/spec/2026-09-16-spec-TOOL-cMendedVintage-2.md memory/builds/cMendedVintage/build/2026-09-16-build-TOOL-cMendedVintage-2-acceptance-ledger.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-16T21:05:43Z dispatch · item 8295fb18 TOOL-cMendedVintage-2 · reason tools/gate-lint/sh_hygiene.py tools/gate-lint/kit.toml tools/gate-lint/README.md tools/gate-lint/substitution-fed-loops.template.txt memory/map/features/gate-lint.md memory/builds/cMendedVintage/spec/2026-09-16-spec-TOOL-cMendedVintage-2.md memory/builds/cMendedVintage/build/2026-09-16-build-TOOL-cMendedVintage-2-acceptance-ledger.md memory/builds/cMendedVintage/README.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-16T22:26:30Z brief · item DEPL-cMendedVintage-9 · reason 6a49b1430acc memory/builds/cMendedVintage/prompts/2026-09-16-prompt-DEPL-cMendedVintage-9-2-build-brief.md

2026-09-16T22:37:03Z dispatch · item 3ca2f144 DEPL-cMendedVintage-9 · reason tools/govkit/govkit.py tools/govkit/selftest.py tools/govkit/refusal_join.py WIRE-INTO-PROJECT.md

2026-09-16T22:44:13Z dispatch · item 3ca2f144 DEPL-cMendedVintage-9 · reason tools/govkit/govkit.py tools/govkit/selftest.py tools/govkit/refusal_join.py WIRE-INTO-PROJECT.md memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-9.md memory/LIVE.md memory/ledger

2026-09-16T23:01:34Z dispatch · item 3ca2f144 DEPL-cMendedVintage-9 · reason tools/govkit/govkit.py tools/govkit/selftest.py tools/govkit/refusal_join.py WIRE-INTO-PROJECT.md memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-9.md memory/builds/cMendedVintage/build/2026-09-17-build-DEPL-cMendedVintage-9-acceptance-ledger.md memory/builds/cMendedVintage/README.md memory/LIVE.md memory/ledger

2026-09-16T23:56:56Z dispatch · item f777a580 TOOL-cMendedVintage-3 · reason tools/check-wiring.sh

2026-09-16T23:56:57Z brief · item TOOL-cMendedVintage-3 · reason 1d8b7f4949ae memory/builds/cMendedVintage/prompts/2026-09-16-prompt-TOOL-cMendedVintage-3-2-build-brief.md

2026-09-16T23:59:34Z dispatch · item f777a580 TOOL-cMendedVintage-3 · reason tools/check-wiring.sh tools/check-wiring.test.sh memory/builds/cMendedVintage/spec/2026-09-16-spec-TOOL-cMendedVintage-3.md memory/builds/cMendedVintage/build/2026-09-17-build-TOOL-cMendedVintage-3-acceptance-ledger.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-17T00:08:53Z dispatch · item f777a580 TOOL-cMendedVintage-3 · reason tools/check-wiring.sh tools/check-wiring.test.sh memory/builds/cMendedVintage/spec/2026-09-16-spec-TOOL-cMendedVintage-3.md memory/builds/cMendedVintage/build/2026-09-17-build-TOOL-cMendedVintage-3-acceptance-ledger.md memory/builds/cMendedVintage/README.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-17T00:16:47Z dispatch · item d019bf9c TOOL-cMendedVintage-4 · reason tools/check-wiring.sh tools/process-monitor/adopt-process-monitor.sh tools/memory-recall/adopt-memory-recall.sh tools/install-prefix-carried.txt

2026-09-17T00:16:48Z brief · item TOOL-cMendedVintage-4 · reason a925a5aa2977 memory/builds/cMendedVintage/prompts/2026-09-16-prompt-TOOL-cMendedVintage-4-2-build-brief.md

2026-09-17T00:22:07Z dispatch · item 961fc402 TOOL-cMendedVintage-4 · reason tools/check-wiring.sh tools/check-wiring.test.sh tools/process-monitor/adopt-process-monitor.sh tools/memory-recall/adopt-memory-recall.sh tools/install-prefix-carried.txt tools/install-prefix-waivers.txt memory/builds/cMendedVintage/spec/2026-09-16-spec-TOOL-cMendedVintage-4.md memory/builds/cMendedVintage/build/2026-09-17-build-TOOL-cMendedVintage-4-acceptance-ledger.md memory/LIVE.md

2026-09-17T00:34:18Z dispatch · item 961fc402 TOOL-cMendedVintage-4 · reason tools/check-wiring.sh tools/check-wiring.test.sh tools/process-monitor/adopt-process-monitor.sh tools/memory-recall/adopt-memory-recall.sh tools/install-prefix-carried.txt tools/install-prefix-waivers.txt memory/builds/cMendedVintage/spec/2026-09-16-spec-TOOL-cMendedVintage-4.md memory/builds/cMendedVintage/build/2026-09-17-build-TOOL-cMendedVintage-4-acceptance-ledger.md memory/builds/cMendedVintage/README.md memory/LIVE.md

2026-09-17T00:44:35Z dispatch · item 2ec1d1d0 TOOL-cMendedVintage-5 · reason tools/check-install-prefix.sh tools/install-prefix-carried.txt tools/check-install-prefix.test.sh

2026-09-17T00:44:37Z brief · item TOOL-cMendedVintage-5 · reason 07881ac501cf memory/builds/cMendedVintage/prompts/2026-09-16-prompt-TOOL-cMendedVintage-5-2-build-brief.md

2026-09-17T00:48:50Z dispatch · item 2ec1d1d0 TOOL-cMendedVintage-5 · reason tools/check-install-prefix.sh tools/install-prefix-carried.txt tools/check-install-prefix.test.sh memory/builds/cMendedVintage/spec/2026-09-16-spec-TOOL-cMendedVintage-5.md memory/builds/cMendedVintage/build/2026-09-17-build-TOOL-cMendedVintage-5-acceptance-ledger.md memory/LIVE.md

2026-09-17T00:59:20Z dispatch · item 2ec1d1d0 TOOL-cMendedVintage-5 · reason tools/check-install-prefix.sh tools/install-prefix-carried.txt tools/check-install-prefix.test.sh memory/builds/cMendedVintage/spec/2026-09-16-spec-TOOL-cMendedVintage-5.md memory/builds/cMendedVintage/build/2026-09-17-build-TOOL-cMendedVintage-5-acceptance-ledger.md memory/builds/cMendedVintage/README.md memory/LIVE.md

2026-09-17T01:07:51Z dispatch · item 8df90a64 DEPL-cMendedVintage-10 · reason tools/govkit/govkit.py tools/govkit/selftest.py

2026-09-17T01:07:52Z brief · item DEPL-cMendedVintage-10 · reason cd5d20be687b memory/builds/cMendedVintage/prompts/2026-09-16-prompt-DEPL-cMendedVintage-10-2-build-brief.md

2026-09-17T01:15:03Z dispatch · item 8df90a64 DEPL-cMendedVintage-10 · reason tools/govkit/govkit.py tools/govkit/selftest.py tools/govkit/refusal_join.py memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-10.md memory/builds/cMendedVintage/build/2026-09-17-build-DEPL-cMendedVintage-10-acceptance-ledger.md

2026-09-17T01:41:05Z dispatch · item 3f73181f DEPL-cMendedVintage-15 · reason tools/govkit/govkit.py tools/govkit/matrix.py

2026-09-17T01:41:06Z brief · item DEPL-cMendedVintage-15 · reason df7e5b169b53 memory/builds/cMendedVintage/prompts/2026-09-16-prompt-DEPL-cMendedVintage-15-2-build-brief.md

2026-09-17T01:45:23Z dispatch · item 3f73181f DEPL-cMendedVintage-15 · reason tools/govkit/govkit.py tools/govkit/selftest.py tools/govkit/matrix.py memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-15.md memory/builds/cMendedVintage/build/2026-09-17-build-DEPL-cMendedVintage-15-acceptance-ledger.md WIRE-INTO-PROJECT.md

2026-09-17T01:57:44Z dispatch · item 3f73181f DEPL-cMendedVintage-15 · reason tools/govkit/selftest.py memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-15.md memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-10.md memory/builds/cMendedVintage/build/2026-09-17-build-DEPL-cMendedVintage-15-acceptance-ledger.md WIRE-INTO-PROJECT.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-17T02:01:10Z dispatch · item 3f73181f DEPL-cMendedVintage-15 · reason tools/govkit/selftest.py memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-15.md memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-10.md memory/builds/cMendedVintage/build/2026-09-17-build-DEPL-cMendedVintage-15-acceptance-ledger.md memory/builds/cMendedVintage/README.md WIRE-INTO-PROJECT.md

2026-09-17T02:08:25Z brief · item DEPL-cMendedVintage-17 · reason f0ef307af59a memory/builds/cMendedVintage/prompts/2026-09-16-prompt-DEPL-cMendedVintage-17-2-build-brief.md

2026-09-17T02:10:20Z decision · item A SUPERSEDED --dispatch declaration row holds its pass open forever, and blocks every later unit that declares the same path. check_pass_open closes a row only when a commit naming that unit WROTE inside that row's declared set. DEPL-cMendedVintage-15 declared four times, narrowing as it learned it needed no engine change at all, and its FIRST row named tools/govkit/govkit.py. It correctly wrote nothing there, so that row can never close, and check 49 now refuses DEPL-cMendedVintage-17's declaration of the same file. Most remaining units touch govkit.py, so this blocks the build. · reason Adopted rather than parked for decision, because it is a blocker between this run and its own landing and the protocol names that a discovery. Recording it here as well because the CAUSE is worth an owner's attention independently of the fix: the predicate rewards a pass that writes everything it declared and punishes one that discovers it needs less. DEPL-cMendedVintage-15 did the right thing — it found its blocker already closed in another spelling and wrote no engine code — and that correctness is precisely what wedged the driver. A unit is also permitted to narrow a declaration, which the skill's own text says is refused, so the two halves disagree about whether narrowing is legal at all.

2026-09-17T02:10:58Z rescope · item add TOOL-cMendedVintage-10 · reason Building uncovered it and it blocks the build: a --dispatch declaration row SUPERSEDED by a later row for the same unit is never closed, because check_pass_open closes a row only when a commit naming that unit wrote inside THAT row's declared set. DEPL-cMendedVintage-15 narrowed its declaration four times as it discovered it needed no engine change, so its first row names tools/govkit/govkit.py and can never close; check 49 now refuses every later unit declaring that file, which is most of the remaining roster. Two further halves belong to the same defect: --audit reports no unit dispatched and open while check 49 treats that same row as open, so the driver holds two answers to one question; and the verb permits narrowing a declaration while the skill's text says narrowing is refused. Adopted rather than parked because the protocol names a blocker between a run and its own landing a discovery, and because the only alternative — manufacturing a govkit.py write attributable to a closed unit purely to satisfy the checker — is the could-not-fail shape this build exists to close.
