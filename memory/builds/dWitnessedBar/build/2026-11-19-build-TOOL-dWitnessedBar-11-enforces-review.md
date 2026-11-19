**Serves:** research TOOL-dWitnessedBar-11

# TOOL-dWitnessedBar-11 — every leg's `enforces`, and where each tag came from

The pass applied §4 "The enforces rule" to the 147 legs that carried no `enforces` and held a
`leg` row of `tools/playbook/core-pending.txt` at the pass's start (DERIVED at this pass). Step 1 read the unit
whose commit introduced the leg (the first commit whose diff of `tools/gate-legs.json` adds its name, `git log -S`),
that unit's spec's `**Carries:**` lines, and the design record's `[enforcement]` row naming a carried clause. Step 2
read the leg's `purpose` and named a practice of `tools/playbook/practices.toml` only where that practice's line
states the rule a red of the leg reports broken: a self-test of a gate, guard or check reports a failing case not
observed (`practice.gate`); a render or index checked against its source reports a generated artifact gone stale
(`practice.derive`); a gate comparing two copies of one value reports them apart (`practice.one-fact`). A leg
testing a feature rather than enforcing a rule was not given a guessed tag.

Step 1 reached 6 legs and step 2 73; 77 legs gained
`enforces` and left the pending list, and 70 stay pending, put to the owner below. Tagging a leg
with a pending principle or practice made that row stale, so the pass deleted it: `principle.p33`, whose arming build
is dOrderedCharter, now enforced by `tags bundle selftest` through step 1, and the ten practice rows step 2 reached.
What no probe sees: whether a tag names the rule the leg actually enforces. The closing review reads each row against
its cites.

| Leg | Tags | Step | Source |
|---|---|---|---|
| cleanup skill wiring | `practice.derive` | 2 | step 2: `practice.derive` at tools/playbook/practices.toml@04da1dc4:92, read against the purpose at tools/branch-reconcile/kit.toml@2d549d70:62: a rendered Skill checked against its render |
| codebase-map coverage + freshness | `practice.derive` | 2 | step 2: `practice.derive` at tools/playbook/practices.toml@04da1dc4:92, read against the purpose at tools/codebase-map/kit.toml@4091c847:107: the generated codebase map checked fresh |
| codebase-map gate coverage | `practice.derive` | 2 | step 2: `practice.derive` at tools/playbook/practices.toml@04da1dc4:92, read against the purpose at tools/codebase-map/kit.toml@4091c847:152: the installed map gate compares every generated artifact |
| agent-cap restatement | `practice.one-fact` | 2 | step 2: `practice.one-fact` at tools/playbook/practices.toml@04da1dc4:100, read against the purpose at tools/govkit/entries/check-agent-cap-restatement.kit.toml@d689252d:49: bans a fan-out bound restated as a bare number |
| agent-cap restatement self-test | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/entries/check-agent-cap-restatement.kit.toml@d689252d:66: self-tests the restatement gate |
| install-prefix self-test | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/entries/check-install-prefix.kit.toml@707d1164:35: arms the install-prefix ban red and green |
| micro-format definitions | `practice.formats` | 2 | step 2: `practice.formats` at tools/playbook/practices.toml@04da1dc4:301, read against the purpose at tools/govkit/entries/check-microformats.kit.toml@8863a649:51: grades the micro-format definitions the formats practice makes non-negotiable |
| micro-format gate selftest | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/entries/check-microformats.kit.toml@8863a649:65: observes the micro-format gate's failing case |
| playbook placeholder catalogue | `practice.one-fact` | 2 | step 2: `practice.one-fact` at tools/playbook/practices.toml@04da1dc4:100, read against the purpose at tools/govkit/entries/check-placeholders.kit.toml@ed07150e:39: holds the version markers in lockstep with their source |
| placeholder-catalogue self-test | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/entries/check-placeholders.kit.toml@ed07150e:55: arms the placeholder gate |
| testsuite counts (every bar self-test prints one) | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/entries/check-testsuite-counts.kit.toml@0deb21be:30: a self-test printing no count reads an empty population as coverage |
| testsuite counts self-test | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/entries/check-testsuite-counts.kit.toml@0deb21be:46: arms each testsuite-counts refusal |
| check-wiring self-test | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/entries/check-wiring.kit.toml@7960125a:40: observes the wiring checker's unwired detection |
| push-main self-test | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/entries/push-main.kit.toml@a1fe6558:74: proves the lander's marker gate |
| pre-push self-test | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/entries/push-main.kit.toml@a1fe6558:97: drives a real push through the pre-push gate |
| pre-push bar self-test | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/entries/push-main.kit.toml@a1fe6558:119: re-disables the pre-push bar's arms and sees the evasions land |
| lexicon naming predicates | `practice.consistency` | 2 | step 2: `practice.consistency` at tools/playbook/practices.toml@04da1dc4:68, read against the purpose at tools/lexicon/kit.toml@4440af33:169: a naming convention gated |
| memory-recall skill wiring | `practice.derive` | 2 | step 2: `practice.derive` at tools/playbook/practices.toml@04da1dc4:92, read against the purpose at tools/memory-recall/kit.toml@9aa10121:111: a rendered Skill checked against its render |
| kit/dogfood doc parity | `practice.one-fact` | 2 | step 2: `practice.one-fact` at tools/playbook/practices.toml@04da1dc4:100, read against the purpose at tools/memory-tree/kit.toml@2dd59ca5:281: a gate comparing the shipped docs with the live ones |
| method carriers (every pointer declared) | `practice.one-fact` | 2 | step 2: `practice.one-fact` at tools/playbook/practices.toml@04da1dc4:100, read against the purpose at tools/memory-tree/kit.toml@2dd59ca5:317: every pointer at the method's source declared |
| build-index selftest | `practice.derive` | 2 | step 2: `practice.derive` at tools/playbook/practices.toml@04da1dc4:92, read against the purpose at tools/memory-tree/kit.toml@2dd59ca5:347: self-tests the generated build index |
| row-grammar selftest | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/memory-tree/kit.toml@2dd59ca5:402: self-tests the row grammar and id-collision check |
| harness arms (fail branches armed or pinned) | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/memory-tree/kit.toml@2dd59ca5:452: a fail branch never armed is a gate never seen red |
| check-arms selftest | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/memory-tree/kit.toml@2dd59ca5:467: self-tests the harness-arms meta-gate |
| routed commits name a specced unit | `practice.spec` | 2 | step 2: `practice.spec` at tools/playbook/practices.toml@04da1dc4:108, read against the purpose at tools/memory-tree/kit.toml@2dd59ca5:487: each routed commit names a unit specced before it |
| routed-commits selftest | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/memory-tree/kit.toml@2dd59ca5:504: self-tests the routed-commits check's failing case |
| playbook render wiring | `practice.derive` | 2 | step 2: `practice.derive` at tools/playbook/practices.toml@04da1dc4:92, read against the purpose at tools/playbook/kit.toml@f12fac67:171: the rendered charter region checked against its render |
| playbook render selftest | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/playbook/kit.toml@f12fac67:190: arms the render engine's predicates |
| roles render wiring | `practice.derive` | 2 | step 2: `practice.derive` at tools/playbook/practices.toml@04da1dc4:92, read against the purpose at tools/roles/kit.toml@4fcf55c4:124: the agent types, role index and Skill renders checked |
| runlog skill wiring | `practice.derive` | 2 | step 2: `practice.derive` at tools/playbook/practices.toml@04da1dc4:92, read against the purpose at tools/runlog/kit.toml@8b357f71:118: a rendered Skill checked against its render |
| pass-order history | `practice.spec` | 2 | step 2: `practice.spec` at tools/playbook/practices.toml@04da1dc4:108, read against the purpose at tools/unattended/kit.toml@1bf92e87:319: refuses a unit built before it was specced |
| unattended skill wiring | `practice.derive` | 2 | step 2: `practice.derive` at tools/playbook/practices.toml@04da1dc4:92, read against the purpose at tools/unattended/kit.toml@1bf92e87:361: a rendered Skill checked against its kit and conf |
| verifier fan-out | `practice.bound` | 2 | step 2: `practice.bound` at tools/playbook/practices.toml@04da1dc4:248, read against the purpose at tools/workflows/kit.toml@0e164a5f:133: holds workflow harnesses to the verify-stage total |
| review-protocol parity (kit vs dogfood) | `practice.one-fact` | 2 | step 2: `practice.one-fact` at tools/playbook/practices.toml@04da1dc4:100, read against the purpose at tools/workflows/kit.toml@0e164a5f:149: a gate comparing each review kit render with its dogfood copy |
| hook destinations self-test | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:426: arms the hook-destinations gate |
| branch-guard self-test | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:508: observes the pre-commit branch guard's refusal |
| straggler-guard arms | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:524: arms the straggler layer |
| recall floor arms | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:573: arms the recall floor check per degradation row |
| spec-tokens self-test | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:667: arms the spec-tokens check red and green |
| chain-packet self-test | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:684: arms the chain-packet door red and green |
| dead-path carriers self-test | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:715: self-tests the dead-path carriers gate |
| remote literals self-test | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:745: self-tests the remote-literals ban |
| govkit selftest | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:791: exercises every deployer refusal |
| govkit runbook parity | `practice.one-fact` | 2 | step 2: `practice.one-fact` at tools/playbook/practices.toml@04da1dc4:100, read against the purpose at tools/govkit/registry.toml@519f118f:870: the prose runbook and the registry held to one population |
| govkit refusal join | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:885: every deployer refusal reached by an arm |
| template size gate selftest | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:938: observes the size gate's failing case |
| playbook parity | `practice.one-fact` | 2 | step 2: `practice.one-fact` at tools/playbook/practices.toml@04da1dc4:100, read against the purpose at tools/govkit/registry.toml@519f118f:953: a gate comparing the charter's stated values with their sources |
| playbook parity selftest | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:974: self-tests the parity gate's failing case |
| kit-placeholders self-test | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:1001: arms the kit-placeholders check red and green |
| agent-instructions wiring | `practice.derive` | 2 | step 2: `practice.derive` at tools/playbook/practices.toml@04da1dc4:92, read against the purpose at tools/govkit/registry.toml@519f118f:1028: a rendered entry file checked against its render |
| process-monitor adopter selftest | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:1099: observes each adopter refusal red |
| drift-audit selftest | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:1115: tests that the drift-audit kit can fail |
| line-length gate selftest | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:1140: observes the line-length gate's failing case |
| run-selftests self-test | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:1154: observes every refusal of the self-test runner |
| scratch-guard self-test | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:1168: observes the scratch guard's refusals |
| format-guard self-test | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:1188: observes the format guard's refusal |
| agent-cap self-test | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:1210: observes the agent-cap guard's refusals |
| lexicon selftest | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:1224: red and green fixtures for every lexicon predicate |
| verdict-epoch self-test | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:1285: self-tests the verdict-epoch check's failing case |
| memory-hygiene self-test | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:1299: fixture-tests the hygiene checks and their empty guard |
| transition-audit arms | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:1313: arms hygiene check 26 and its carrier |
| row-driver view refusal | `practice.reconcile` | 2 | step 2: `practice.reconcile` at tools/playbook/practices.toml@04da1dc4:189, read against the purpose at tools/govkit/registry.toml@519f118f:1335: the row-keyed merge of shared records, a view refused |
| row-keyed merge driver replay | `practice.reconcile` | 2 | step 2: `practice.reconcile` at tools/playbook/practices.toml@04da1dc4:189, read against the purpose at tools/govkit/registry.toml@519f118f:1348: replays the additive row-keyed merge of shared records |
| method-carriers self-test | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:1362: self-tests the method-carrier gate's failing case |
| verifier fan-out self-test | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:1497: self-tests the verifier fan-out gate |
| review-join self-test | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:1553: self-tests the review-join ban and syntax gates |
| leg ceilings clear their evidenced maximum | `practice.cost` | 2 | step 2: `practice.cost` at tools/playbook/practices.toml@04da1dc4:154, read against the purpose at tools/govkit/registry.toml@519f118f:1567: each leg's declared ceiling against its evidence |
| every held leg is budgeted, every budget row resolves | `practice.cost` | 2 | step 2: `practice.cost` at tools/playbook/practices.toml@04da1dc4:154, read against the purpose at tools/govkit/registry.toml@519f118f:1581: every held self-test declares its cost |
| extract-arms self-test | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:1595: arms the four states the arm extractor reports |
| selftest harness self-test | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:1613: arms the shared self-test harness |
| policy fixtures | `principle.p10`, `principle.p42`, `practice.gate` | 1, 2 | step 1: TOOL-dGroundRules-1's memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-1.md@c511ba3f:5 carries `cl-dClosedLoop-0007`, in memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c9:1832; step 1: TOOL-dGroundRules-1's memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-1.md@c511ba3f:5 carries `cl-dClosedLoop-0007`, in memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c9:1864; step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:1659: TOOL-dGroundRules-1 carries cl-dClosedLoop-0007, in P10's and P42's rows; its purpose observes each policy arm red |
| tags positional selftest | `practice.gate` | 2 | step 2: `practice.gate` at tools/playbook/practices.toml@04da1dc4:123, read against the purpose at tools/govkit/registry.toml@519f118f:2228: self-tests the positional citation population |
| tags bundle selftest | `principle.p33` | 1 | step 1: PLAY-dOrderedCharter-25's memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-25.md@a6c5f47c:5 carries `cl-dClosedLoop-0055`, in memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c9:1855 |
| step-rows-frozen | `principle.p38` | 1 | step 1: TOOL-dSafePassage-1's memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-1.md@262b484c:5 carries `cl-dClosedLoop-0018`, in memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c9:1860 |
| step-gate | `principle.p38` | 1 | step 1: TOOL-dSafePassage-10's memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-10.md@b33a99af:5 carries `cl-dClosedLoop-0027`, in memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c9:1860 |
| docs | `principle.p42`, `practice.docs` | 1, 2 | step 1: TOOL-dSafePassage-13's memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-13.md@b40f40a6:5 carries `cl-dClosedLoop-0030`, in memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c9:1864; step 2: `practice.docs` at tools/playbook/practices.toml@04da1dc4:226, read against the purpose at tools/govkit/registry.toml@519f118f:2336: TOOL-dSafePassage-13 carries cl-dClosedLoop-0030, in P42's row; its purpose reds a member whose help page is not current |
| upgrade-walk | `principle.p38` | 1 | step 1: TOOL-dSafePassage-5's memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-5.md@5e2449c9:5 carries `cl-dClosedLoop-0022`, in memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c9:1860 |

## Put to the owner

Neither step reached these 70 legs: no carried clause sits in an `[enforcement]` row, and no practice's
line states the rule their red reports broken, most because they test a feature, measure a size or run an engine's
suite rather than enforce a practice. Each keeps its `leg` row of `tools/playbook/core-pending.txt`, and the ask
TOOL-dWitnessedBar-98 in this build's `BACKLOG.md` puts them to the owner as one question.

| Leg | Purpose | Source |
|---|---|---|
| kickoff-manifest ratchet | verifies the kickoff manifest against mechanical signals | tools/govkit/entries/kickoff-manifest.kit.toml@75f9604e:72 |
| template size <=48KiB | caps the charter template's bytes at its declared ceiling | tools/govkit/registry.toml@519f118f:856 |
| charter size | caps the charter's bytes at its declared ceiling | tools/govkit/registry.toml@519f118f:495 |
| line length | holds agent-instruction prose to a declared line length | tools/govkit/entries/check-line-length.kit.toml@56435ecf:61 |
| build-method size | caps the build method's bytes at its declared ceiling | tools/govkit/registry.toml@519f118f:459 |
| unattended protocol size | caps the unattended protocol's bytes at its declared ceiling | tools/govkit/registry.toml@519f118f:471 |
| unattended skill size | caps the unattended skill's bytes at its declared ceiling | tools/govkit/registry.toml@519f118f:483 |
| kickoff engine size <=18KiB | caps the kickoff engine's bytes at its declared ceiling | tools/govkit/registry.toml@519f118f:447 |
| shell hygiene (a loop fed by a command substitution) | catches a loop fed by a command substitution in a shell file | tools/gate-lint/kit.toml@50c959ac:67 |
| shell hygiene (a fork spent on builtin work) | catches a fork spent on builtin work in a shell file | tools/gate-lint/kit.toml@50c959ac:121 |
| spawn budget (forks per hot entrypoint) | caps the forks per hot entrypoint at a shrink-only ceiling | tools/govkit/registry.toml@519f118f:414 |
| shell-hygiene selftest | stages breaks into a copy of the shell-hygiene scanner | tools/gate-lint/kit.toml@50c959ac:180 |
| kit version markers | checks every kit carries a well-formed version constant | tools/govkit/entries/check-kit-versions.kit.toml@384ee387:50 |
| verdict epoch (kit version dates the engine) | requires the version that dates the engine to move with it | tools/memory-tree/kit.toml@2dd59ca5:265 |
| manifest-check self-test | runs the kickoff manifest check's scenario suite | tools/govkit/registry.toml@519f118f:812 |
| build README slot contract | grades each build README's slot contract and heading canon | tools/memory-tree/kit.toml@2dd59ca5:333 |
| corpus-ids selftest | self-tests the corpus's id and path classifier | tools/memory-tree/kit.toml@2dd59ca5:368 |
| gotchas selftest | self-tests the bug-class index and its per-diff checklist | tools/memory-tree/kit.toml@2dd59ca5:382 |
| backlog migration selftest | runs the backlog migration planner's suite | tools/memory-tree/kit.toml@2dd59ca5:422 |
| pre-push run-log line | observes the pre-push hook's run-log lines from outside | tools/govkit/registry.toml@519f118f:1484 |
| review-join ban (no ref-keyed join) | bans a ref-keyed verdict join in a workflow script | tools/workflows/kit.toml@0e164a5f:177 |
| workflow script syntax | parses every workflow script in its runtime's dialect | tools/workflows/kit.toml@0e164a5f:192 |
| tier2-review self-test | tests the review harness's argument and durability contracts | tools/govkit/registry.toml@519f118f:1523 |
| unattended-build self-test | arms the unattended build harness | tools/govkit/registry.toml@519f118f:1540 |
| spec-audit opt-in pack self-test | tests the review kit's spec-audit opt-in pack | tools/govkit/registry.toml@519f118f:1511 |
| review-replay selftest | self-tests the review replay tool | tools/workflows/kit.toml@0e164a5f:213 |
| pytest-guardrails self-test | statically checks the pytest parallel guardrails kit | tools/govkit/registry.toml@519f118f:1374 |
| codebase-map kit selftest | exercises the codebase-map engine with fixtures | tools/govkit/registry.toml@519f118f:1049 |
| codebase-map adopter e2e | tests the codebase-map adopter end to end | tools/govkit/registry.toml@519f118f:1067 |
| settings-merge selftest | self-tests wiring a hook into a target's settings.json | tools/govkit/entries/settings-merge.kit.toml@61bd2196:70 |
| memory-recall kit selftest | tests the memory-recall kit's own contract | tools/govkit/registry.toml@519f118f:1264 |
| recall floor | grades the committed question set against the recall floor | tools/govkit/registry.toml@519f118f:549 |
| drift-audit wiring | checks the drift-audit kit's wiring has not drifted | tools/drift-audit/kit.toml@fb256c7c:156 |
| process-monitor wiring | checks the process-monitor kit's wiring has not drifted | tools/process-monitor/kit.toml@db9baff3:85 |
| process-monitor census selftest | arms the process-monitor engine's parsing and liveness | tools/govkit/registry.toml@519f118f:1080 |
| runlog selftest | arms the runlog kit over fixtures and scratch trees | tools/govkit/registry.toml@519f118f:1251 |
| runlog record schema | checks committed run records and run-state history | tools/runlog/kit.toml@8b357f71:99 |
| branch-reconcile selftest | tests the branch-reconcile kit in fixture repositories | tools/govkit/registry.toml@519f118f:1238 |
| drift-audit records | checks the repo's record of its state still matches reality | tools/drift-audit/kit.toml@fb256c7c:100 |
| unattended kit gate | grades the repository against the unattended-run kit | tools/unattended/kit.toml@1bf92e87:282 |
| brief-recorded | refuses a closed unit whose build commit records no brief | tools/unattended/kit.toml@1bf92e87:344 |
| playbook validity gate | grades the validity of every playbook and the kit fixture | tools/unattended/kit.toml@1bf92e87:303 |
| run-gates canary | checks the manifest is well-formed and sources every leg | tools/govkit/registry.toml@519f118f:1433 |
| run-gates evidence | checks a red leg's own output survives on disk | tools/govkit/registry.toml@519f118f:1445 |
| run-gates turnstile | arms the turnstile that serialises bars on one repository | tools/govkit/registry.toml@519f118f:1421 |
| run-gates gov canary | runs the run-gates canary arms keyed on this repository | tools/govkit/registry.toml@519f118f:842 |
| foreign-prefix parity (every self-test at three prefixes) | runs every declared self-test at three tool-root prefixes | tools/govkit/registry.toml@519f118f:1015 |
| run-gates run-log line | observes the gate runner's run-log line from outside | tools/govkit/registry.toml@519f118f:1471 |
| run-gates adopter e2e | grades the run-gates adopter on its effects | tools/govkit/registry.toml@519f118f:1458 |
| run-gates wiring | checks the run-gates kit's adopted declaration for drift | tools/run-gates/kit.toml@6d7e66a8:202 |
| profile-bar selftest | self-tests the bar profiler | tools/govkit/registry.toml@519f118f:1387 |
| held-halves selftest | self-tests the split-tier held self-test combiner | tools/run-gates/kit.toml@6d7e66a8:248 |
| measure-legs selftest | self-tests the profiler that runs each leg clean | tools/govkit/registry.toml@519f118f:1400 |
| install-prefix (shipped surface) | bans a kit path spelled in the shipped surface | tools/govkit/entries/check-install-prefix.kit.toml@707d1164:58 |
| dead-path carriers (deleted files still named) | catches a deleted file still named outside the memory tree | tools/govkit/registry.toml@519f118f:700 |
| remote literals (kit code names no remote) | bans kit code naming a remote by literal | tools/govkit/registry.toml@519f118f:731 |
| govkit selfcheck | self-checks the deployer's own declarations | tools/govkit/registry.toml@519f118f:761 |
| kit epoch (shipped bytes move, the version moves) | requires a kit's version to move when its shipped bytes do | tools/govkit/registry.toml@519f118f:776 |
| lexicon wiring | verifies the repository's naming-lexicon declaration | tools/lexicon/kit.toml@4440af33:187 |
| memory hygiene | runs the memory tree's mechanized hygiene checks | tools/memory-tree/kit.toml@2dd59ca5:194 |
| memory hygiene (the pass checks) | runs the memory hygiene checks a pass owes | tools/govkit/registry.toml@519f118f:634 |
| marker contracts | holds live readers to contracts shared code cannot express | tools/memory-tree/kit.toml@2dd59ca5:437 |
| govkit acceptance matrix | drives the deployer against repository shapes | tools/govkit/registry.toml@519f118f:917 |
| spec tokens (a spec's own names resolve) | requires a spec's own names to resolve in the tree | tools/govkit/registry.toml@519f118f:599 |
| spec tokens (the pass's own spec) | resolves the tokens of the pass's own spec | tools/govkit/registry.toml@519f118f:615 |
| kit placeholders (a declared token its adopter substitutes) | requires a kit's adopter to substitute each declared token | tools/govkit/registry.toml@519f118f:989 |
| roles render selftest | self-tests rendering roles into Claude Code agent types | tools/roles/kit.toml@4fcf55c4:140 |
| roles adopter self-test | tests the roles adopter in fresh fixture repositories | tools/govkit/registry.toml@519f118f:1627 |
| positional (the citation check alone) | runs the positional file:line citation check alone | tools/govkit/registry.toml@519f118f:653 |
| receipt sync (installed files match the receipt) | checks the installed files match the deployer's receipt | tools/run-gates/kit.toml@6d7e66a8:228 |
