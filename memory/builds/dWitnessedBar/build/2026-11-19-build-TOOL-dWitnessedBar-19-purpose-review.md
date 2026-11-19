**Serves:** research TOOL-dWitnessedBar-19

# TOOL-dWitnessedBar-19 — every leg's purpose, and where it came from

One row per leg of `tools/gate-legs.json` at the build run's base, 198 legs (DERIVED from the
manifest at this pass), each with the `purpose` the pass wrote on its manifest row and on its
descriptor row where a descriptor claims it, the step of the spec's rule (§4 "The rule") that
produced it, and the `path:line` of the source read. Step 1 cites the leg's own `name` line in the
manifest, whose parenthetical it paraphrases; step 2 the comment block directly above the leg's
`[[gate_leg]]` row; step 3 the gate script's header, qualified by the leg's `argv` where several legs
run one script (the argv word is on the leg's manifest row). Step 4 reached no leg first: step 3
reached every leg the first two did not.

A step-2 comment reached a leg only where it says what the leg does; a block about the leg's
subject, guard or hold says nothing about this leg it does not say about its siblings, so step 3
decided those. What no probe sees: whether each 60 characters say what the cited line says. The
closing review reads these rows against their cites.

| Leg | Purpose | Step | Source |
|---|---|---|---|
| kickoff-manifest ratchet | verifies the kickoff manifest against mechanical signals | 3 | skills/session-kickoff/manifest-check.sh@d704bfff:3 |
| template size <=48KiB | caps the charter template's bytes at its declared ceiling | 3 | tools/check-template-size.sh@c76defce:2 |
| charter size | caps the charter's bytes at its declared ceiling | 3 | tools/check-template-size.sh@c76defce:2 |
| micro-format definitions | grades the charter's micro-format definitions by grammar | 3 | tools/check-microformats.sh@b2f9e51b:2 |
| micro-format gate selftest | observes the micro-format gate's failing case per predicate | 3 | tools/check-microformats.test.sh@b21ec1c0:2 |
| line length | holds agent-instruction prose to a declared line length | 3 | tools/check-line-length.sh@bdfb62bf:2 |
| line-length gate selftest | observes the line-length gate's failing case per branch | 3 | tools/check-line-length.test.sh@9e8acd12:2 |
| playbook parity | runs the charter's parity gate over its stated values | 3 | tools/playbook/render_playbook.py@cbd3d672:73 |
| playbook parity selftest | self-tests the playbook parity check | 3 | tools/check-playbook-parity.test.sh@10dcd3dd:2 |
| template size gate selftest | self-tests the template size gate | 3 | tools/check-template-size.test.sh@0f222700:2 |
| build-method size | caps the build method's bytes at its declared ceiling | 3 | tools/check-template-size.sh@c76defce:2 |
| unattended protocol size | caps the unattended protocol's bytes at its declared ceiling | 3 | tools/check-template-size.sh@c76defce:2 |
| unattended skill size | caps the unattended skill's bytes at its declared ceiling | 3 | tools/check-template-size.sh@c76defce:2 |
| kickoff engine size <=18KiB | caps the kickoff engine's bytes at its declared ceiling | 3 | tools/check-template-size.sh@c76defce:2 |
| shell hygiene (a loop fed by a command substitution) | catches a loop fed by a command substitution in a shell file | 1 | tools/gate-legs.json@e63bd4e0:237 |
| shell hygiene (a location probe asked from a moved directory) | catches a location probe asked from a moved directory | 1 | tools/gate-legs.json@e63bd4e0:254 |
| shell hygiene (a fork spent on builtin work) | catches a fork spent on builtin work in a shell file | 1 | tools/gate-legs.json@e63bd4e0:274 |
| shell hygiene (a fixed-name temp renamed into place) | catches a fixed-name temp renamed into place in a shell file | 1 | tools/gate-legs.json@e63bd4e0:294 |
| spawn budget (forks per hot entrypoint) | caps the forks per hot entrypoint at a shrink-only ceiling | 1 | tools/gate-legs.json@e63bd4e0:315 |
| shell-hygiene selftest | stages breaks into a copy of the shell-hygiene scanner | 2 | tools/gate-lint/kit.toml@d0a711f4:124 |
| encoding posture (text IO names its encoding) | catches Python text IO that does not name its encoding | 1 | tools/gate-legs.json@e63bd4e0:351 |
| kit version markers | checks every kit carries a well-formed version constant | 3 | tools/check-kit-versions.sh@4681e380:2 |
| verdict epoch (kit version dates the engine) | requires the version that dates the engine to move with it | 1 | tools/gate-legs.json@e63bd4e0:388 |
| verdict-epoch self-test | self-tests the verdict-epoch check in throwaway repos | 3 | tools/memory-tree/check-verdict-epoch.test.sh@d2ebac08:2 |
| agent-instructions wiring | compares the rendered CLAUDE.md entry file with its render | 3 | tools/playbook/render_playbook.py@cbd3d672:71 |
| manifest-check self-test | runs the kickoff manifest check's scenario suite | 3 | skills/session-kickoff/manifest-check.test.sh@9211eea4:2 |
| python resolver (behaviour + inline parity + idiom ban) | tests the python resolver's behaviour, inline parity and ban | 1 | tools/gate-legs.json@e63bd4e0:462 |
| agent-cap self-test | tests the agent-cap guard on Workflow and Agent tool calls | 3 | tools/hooks/agent-cap.test.sh@97439f99:2 |
| scratch-guard self-test | tests the guard that keeps agent scratch out of home | 3 | tools/hooks/scratch-guard.test.sh@b8bb1ed3:2 |
| format-guard self-test | tests the hook refusing a final message without its format | 3 | tools/hooks/format-guard.test.sh@a256c80c:2 |
| memory-hygiene self-test | fixture-tests the memory hygiene checks and empty guard | 3 | tools/memory-tree/check-memory-hygiene.test.sh@f740dd4c:2 |
| row-driver view refusal | asserts governed paths resolve merge=rows and views refuse | 3 | tools/memory-tree/merge-rows.py@cd441001:171 |
| row-keyed merge driver replay | replays fixtures through the row-keyed merge driver | 3 | tools/memory-tree/merge-rows.test.sh@4e5e5b05:2 |
| kit/dogfood doc parity | holds the memory-tree kit's shipped docs equal to live ones | 3 | tools/memory-tree/kit-dogfood-parity.test.sh@ddb1994d:2 |
| method carriers (every pointer declared) | requires every pointer at the build method to be declared | 1 | tools/gate-legs.json@e63bd4e0:628 |
| method-carriers self-test | self-tests the method-carrier gate in a scratch repo | 3 | tools/memory-tree/check-method-carriers.test.sh@a45c89ff:2 |
| build-index selftest | self-tests the generated build index | 3 | tools/memory-tree/gen_build_index.py@a1bfa9b9:2 |
| build README slot contract | grades each build README's slot contract and heading canon | 3 | tools/memory-tree/gen_build_index.py@a1bfa9b9:9 |
| corpus-ids selftest | self-tests the corpus's id and path classifier | 3 | tools/memory-tree/corpus_ids.py@a5809fac:2 |
| gotchas selftest | self-tests the bug-class index and its per-diff checklist | 3 | tools/memory-tree/gotchas.py@f85b1351:2 |
| routed-commits selftest | self-tests the check that routed commits name a unit | 3 | tools/memory-tree/routed_commits.py@d48d1dc8:2 |
| row-grammar selftest | self-tests the row-document grammar and id-collision check | 3 | tools/memory-tree/row_grammar.py@923ce49a:2 |
| backlog migration selftest | runs the backlog migration planner's suite | 2 | tools/memory-tree/kit.toml@2bb01a7d:342 |
| harness arms (fail branches armed or pinned) | requires each harness fail branch to be armed or pinned | 1 | tools/gate-legs.json@e63bd4e0:800 |
| check-arms selftest | self-tests the harness arms meta-gate | 3 | tools/memory-tree/check-arms.py@36e38fb2:2 |
| branch-guard self-test | tests the pre-commit branch guard in a throwaway repo | 3 | .githooks/pre-commit.test.sh@fe6b214e:2 |
| pre-push self-test | drives a real push through the pre-push hook | 3 | .githooks/pre-push.test.sh@972e3a7d:2 |
| pre-push run-log line | observes the pre-push hook's run-log lines from outside | 3 | .githooks/pre-push.runlog.test.sh@0b4811de:2 |
| pre-push bar self-test | re-disables pre-push bar arms in a copy, sees evasions land | 2 | tools/govkit/entries/push-main.kit.toml@8f3de785:99 |
| push-main self-test | proves the lander and the pre-push marker gate | 3 | tools/push-main.test.sh@ffb7749f:2 |
| check-wiring self-test | tests the wiring checker's wired and unwired detection | 3 | tools/check-wiring.test.sh@8d0af8c9:2 |
| verifier fan-out self-test | self-tests the verifier fan-out gate and its rule | 3 | tools/workflows/check-verifier-fanout.test.sh@6fc495dc:2 |
| review-protocol parity (kit vs dogfood) | holds each review kit render equal to its dogfood copy | 1 | tools/gate-legs.json@e63bd4e0:970 |
| review-join ban (no ref-keyed join) | bans a ref-keyed verdict join in a workflow script | 1 | tools/gate-legs.json@e63bd4e0:986 |
| workflow script syntax | parses every workflow script in its runtime's dialect | 3 | tools/workflows/check-workflow-syntax.js@77a13020:2 |
| tier2-review self-test | tests the review harness's argument and durability contracts | 3 | tools/workflows/tier2-review.test.sh@5295143f:2 |
| unattended-build self-test | arms the unattended build harness | 3 | tools/workflows/unattended-build.test.sh@7d95ece0:2 |
| review-join self-test | self-tests the review-join ban and workflow syntax gates | 3 | tools/workflows/check-review-join.test.sh@6bff782d:2 |
| spec-audit opt-in pack self-test | tests the review kit's spec-audit opt-in pack | 3 | tools/workflows/spec-audit-optin.test.sh@fd149d71:2 |
| review-replay selftest | self-tests the review replay tool | 2 | tools/workflows/kit.toml@e27ef6a0:180 |
| pytest-guardrails self-test | statically checks the pytest parallel guardrails kit | 3 | tools/pytest-parallel-guardrails/pytest-parallel-guardrails.test.sh@ac1a47f4:2 |
| codebase-map kit selftest | exercises the codebase-map engine with fixtures | 3 | tools/codebase-map/selftest.py@1562a974:1 |
| codebase-map gate coverage | checks the installed map gate compares every artifact | 3 | tools/codebase-map/check_gate_coverage.py@7706dca1:2 |
| codebase-map coverage + freshness | grades the codebase map's coverage and freshness | 3 | tools/codebase-map/test_codebase_map.py@15ab8d82:1 |
| codebase-map adopter e2e | tests the codebase-map adopter end to end | 3 | tools/codebase-map/adopt-codebase-map.test.sh@276d83bc:2 |
| settings-merge selftest | self-tests wiring a hook into a target's settings.json | 3 | tools/settings-merge.py@548b594f:2 |
| memory-recall kit selftest | tests the memory-recall kit's own contract | 3 | tools/memory-recall/selftest.py@6474907c:2 |
| recall floor | grades the committed question set against the recall floor | 3 | tools/memory-recall/check-recall.py@7977d175:2 |
| recall floor arms | arms the recall floor check per degradation row | 3 | tools/memory-recall/test_recall_floor.py@c2de6ea5:2 |
| memory-recall skill wiring | checks the memory-recall Skill has not drifted | 3 | tools/memory-recall/adopt-memory-recall.sh@48d9ddb1:5 |
| drift-audit selftest | tests that the drift-audit kit can fail | 3 | tools/drift-audit/selftest.py@7a0392f1:2 |
| drift-audit wiring | checks the drift-audit kit's wiring has not drifted | 3 | tools/drift-audit/adopt-drift-audit.sh@fdc1b2b3:2 |
| process-monitor wiring | checks the process-monitor kit's wiring has not drifted | 3 | tools/process-monitor/adopt-process-monitor.sh@23cf4868:2 |
| process-monitor census selftest | arms the process-monitor engine's parsing and liveness | 3 | tools/process-monitor/selftest.py@ef4b52e9:2 |
| process-monitor adopter selftest | observes each process-monitor adopter refusal red | 3 | tools/process-monitor/adopt-process-monitor.test.sh@b7131f45:2 |
| runlog selftest | arms the runlog kit over fixtures and scratch trees | 3 | tools/runlog/selftest.py@6c19574d:2 |
| runlog record schema | checks committed run records and run-state history | 2 | tools/runlog/kit.toml@724215b0:89 |
| runlog skill wiring | checks the rendered runlog Skill has not gone stale | 2 | tools/runlog/kit.toml@724215b0:105 |
| cleanup skill wiring | checks the rendered cleanup Skill has not gone stale | 2 | tools/branch-reconcile/kit.toml@080fceb6:55 |
| branch-reconcile selftest | tests the branch-reconcile kit in fixture repositories | 3 | tools/branch-reconcile/selftest.py@464766d2:2 |
| drift-audit records | checks the repo's record of its state still matches reality | 3 | tools/drift-audit/drift_report.py@57d928be:2 |
| unattended kit gate | grades the repository against the unattended-run kit | 3 | tools/unattended/check-unattended.sh@287ccb81:2 |
| pass-order history | refuses a unit built before it was specced | 3 | tools/unattended/check-pass-order.sh@f708d377:2 |
| routed commits name a specced unit | requires each routed commit to name a unit specced before it | 2 | tools/memory-tree/kit.toml@2bb01a7d:385 |
| brief-recorded | refuses a closed unit whose build commit records no brief | 3 | tools/unattended/check-brief-recorded.sh@8649c1b2:2 |
| playbook validity gate | grades the validity of every playbook and the kit fixture | 2 | tools/unattended/kit.toml@b1b81c9d:290 |
| unattended skill wiring | verifies the unattended Skill still matches kit and conf | 3 | tools/unattended/adopt-unattended.sh@c3cd27dc:5 |
| run-gates canary | checks the manifest is well-formed and sources every leg | 3 | tools/run-gates/run-gates.test.sh@59f72ea6:2 |
| run-gates evidence | checks a red leg's own output survives on disk | 3 | tools/run-gates/run-gates.evidence.test.sh@d9200d98:2 |
| run-gates turnstile | arms the turnstile that serialises bars on one repository | 3 | tools/run-gates/run-gates.turnstile.test.sh@340ddcac:2 |
| run-gates gov canary | runs the run-gates canary arms keyed on this repository | 3 | tools/run-gates/run-gates.gov.test.sh@d660e8c8:2 |
| foreign-prefix parity (every self-test at three prefixes) | runs every declared self-test at three tool-root prefixes | 1 | tools/gate-legs.json@e63bd4e0:1690 |
| run-gates run-log line | observes the gate runner's run-log line from outside | 3 | tools/run-gates/run-gates.runlog.test.sh@67da5494:2 |
| run-gates adopter e2e | grades the run-gates adopter on its effects | 3 | tools/run-gates/adopt-run-gates.test.sh@5f09fc69:2 |
| run-gates wiring | checks the run-gates kit's adopted declaration for drift | 3 | tools/run-gates/adopt-run-gates.sh@7dcd91ec:2 |
| profile-bar selftest | self-tests the bar profiler | 3 | tools/run-gates/profile_bar.test.sh@5ad0d75b:2 |
| held-halves selftest | self-tests the split-tier held self-test combiner | 2 | tools/run-gates/kit.toml@8af77800:213 |
| measure-legs selftest | self-tests the profiler that runs each leg clean | 3 | tools/run-gates/measure_legs.py@d888b331:2 |
| install-prefix (shipped surface) | bans a kit path spelled in the shipped surface | 1 | tools/gate-legs.json@e63bd4e0:1821 |
| hook destinations (every declared hook path ships) | requires every declared hook path to ship | 1 | tools/gate-legs.json@e63bd4e0:1842 |
| hook destinations self-test | arms the hook-destinations gate | 3 | tools/check-hook-destinations.test.sh@d561078e:2 |
| agent-cap restatement | bans live prose stating a fan-out bound as a bare number | 3 | tools/check-agent-cap-restatement.sh@902fe65e:2 |
| agent-cap restatement self-test | self-tests the agent-cap restatement gate | 3 | tools/check-agent-cap-restatement.test.sh@5392780e:2 |
| install-prefix self-test | arms the install-prefix ban red and green | 3 | tools/check-install-prefix.test.sh@f9b2fd1f:2 |
| dead-path carriers (deleted files still named) | catches a deleted file still named outside the memory tree | 1 | tools/gate-legs.json@e63bd4e0:1932 |
| dead-path carriers self-test | self-tests the dead-path carriers gate | 3 | tools/check-dead-paths.test.sh@43a92998:2 |
| remote literals (kit code names no remote) | bans kit code naming a remote by literal | 1 | tools/gate-legs.json@e63bd4e0:1967 |
| remote literals self-test | self-tests the remote-literals ban | 3 | tools/check-remote-literals.test.sh@bbefdccc:2 |
| govkit selfcheck | self-checks the deployer's own declarations | 3 | tools/govkit/govkit.py@60b8fa09:2 |
| kit epoch (shipped bytes move, the version moves) | requires a kit's version to move when its shipped bytes do | 1 | tools/gate-legs.json@e63bd4e0:2019 |
| step-rows-frozen | refuses an edit to a frozen upgrade step row | 3 | tools/govkit/upgrade_steps.py@98cf21fb:3 |
| step-gate | diffs the adopter-visible surface between base and tip | 3 | tools/govkit/step_gate.py@11b2aceb:2 |
| docs | fingerprints each member's usage against its help page | 3 | tools/govkit/docs_leg.py@259afa60:2 |
| help reference pages | compares each help reference page with its render | 3 | tools/playbook/render_playbook.py@cbd3d672:118 |
| help page commands | runs every command a help page shows in a scratch adopter | 3 | tools/govkit/docs_leg.py@259afa60:34 |
| upgrade-walk | walks every declared upgrade step over release-0 | 3 | tools/govkit/upgrade_walk.py@aea8e1c7:2 |
| govkit selftest | exercises every deployer refusal in throwaway repos | 3 | tools/govkit/selftest.py@45513099:2 |
| lexicon naming predicates | grades names against the declared lexicon vocabulary | 3 | tools/lexicon/lexicon.py@a4787e4f:3 |
| lexicon selftest | runs red and green fixtures for every lexicon predicate | 3 | tools/lexicon/selftest.py@7363ebed:2 |
| lexicon wiring | verifies the repository's naming-lexicon declaration | 3 | tools/lexicon/adopt-lexicon.sh@53869d18:2 |
| playbook placeholder catalogue | holds the playbook's version markers in lockstep | 3 | tools/check-placeholders.sh@db7d14ad:2 |
| placeholder-catalogue self-test | arms the placeholder gate, each arm asserting its message | 3 | tools/check-placeholders.test.sh@66386d6e:2 |
| memory hygiene | runs the memory tree's mechanized hygiene checks | 3 | tools/memory-tree/check-memory-hygiene.sh@2c0cb6f2:2 |
| memory hygiene (the pass checks) | runs the memory hygiene checks a pass owes | 1 | tools/gate-legs.json@e63bd4e0:2285 |
| transition-audit arms | arms hygiene check 26 and its commit-time carrier | 3 | tools/memory-tree/transition-audit.test.sh@f9d213b9:2 |
| straggler-guard arms | arms the shards-to-builds straggler layer | 3 | .githooks/straggler-guard.test.sh@267fa8ba:2 |
| marker contracts | holds live readers to contracts shared code cannot express | 3 | tools/memory-tree/marker-contract.test.sh@e147acb7:2 |
| verifier fan-out | holds workflow harnesses to the verify-stage total | 3 | tools/workflows/check-verifier-fanout.sh@153f0600:2 |
| govkit refusal join | requires every deployer refusal to be reached by an arm | 3 | tools/govkit/refusal_join.py@59ae80a7:2 |
| govkit runbook parity | holds the prose runbook and the registry to one population | 3 | tools/govkit/check_runbook_parity.py@0ed63820:2 |
| govkit acceptance matrix | drives the deployer against repository shapes | 3 | tools/govkit/matrix.py@8bb81dbe:2 |
| testsuite counts (every bar self-test prints one) | requires every bar self-test to print an assertion count | 1 | tools/gate-legs.json@e63bd4e0:2441 |
| testsuite counts self-test | arms each testsuite-counts refusal with a green control | 3 | tools/check-testsuite-counts.test.sh@eea2b8d9:2 |
| playbook render wiring | asserts the rendered charter region still matches | 3 | tools/playbook/adopt-playbook.sh@ff84b4d8:5 |
| playbook render selftest | arms the charter render engine's own predicates | 2 | tools/playbook/kit.toml@52ce0d75:175 |
| spec tokens (a spec's own names resolve) | requires a spec's own names to resolve in the tree | 1 | tools/gate-legs.json@e63bd4e0:2520 |
| spec tokens (the pass's own spec) | resolves the tokens of the pass's own spec | 1 | tools/gate-legs.json@e63bd4e0:2536 |
| kit placeholders (a declared token its adopter substitutes) | requires a kit's adopter to substitute each declared token | 1 | tools/gate-legs.json@e63bd4e0:2555 |
| roles catalogue | grades role files against the governing doc and overlays | 2 | tools/roles/kit.toml@d2cf3868:97 |
| roles render wiring | grades the agent types, role index and Skill renders | 2 | tools/roles/kit.toml@d2cf3868:112 |
| roles render selftest | self-tests rendering roles into Claude Code agent types | 3 | tools/roles/render_agents.py@0d96af1a:2 |
| roles adopter self-test | tests the roles adopter in fresh fixture repositories | 3 | tools/roles/adopt-roles.test.sh@c23a4909:2 |
| policy check | checks the repository's own policy file | 2 | tools/policy/kit.toml@39a8aeb9:80 |
| loop definition | checks the loop definition every reader in the target reads | 2 | tools/loop/kit.toml@a479e408:173 |
| loop definition fixtures | plants each break in the loop definition's reader | 3 | tools/loop/loop_lib.py@7d5c58fe:7 |
| loop computed witness | self-tests witnesses computed rather than typed | 3 | tools/loop/loop_witness.py@2538582a:2 |
| loop checklist tags | maps each core checklist handle onto its declared item | 3 | tools/loop/loop_checklist.py@708f9e9a:2 |
| loop item kind | checks the item kind's factory and the composed items | 3 | tools/loop/loop_items.py@ac1029cb:2 |
| loop splice check | checks a repository's own stages spliced into the loop | 3 | tools/loop/splice.py@119677da:2 |
| loop parent routes | tests a dependent build's route when its parent withdraws | 3 | tools/loop/loop_parents.py@13072a1e:2 |
| loop transition record | checks a build's stage transition recorded three ways | 3 | tools/loop/loop_transition.py@8b78cbc0:2 |
| loop guard fixtures | plants breaks in the policy guard's commit and push arms | 3 | tools/loop/guard.py@3b9aa3a9:2 |
| loop claims fixtures | tests stored claims keyed and trusted over their sources | 3 | tools/loop/claims.py@029b5cc9:2 |
| loop position fixtures | tests deriving a build's position from witnesses alone | 3 | tools/loop/position.py@710b2d07:2 |
| loop upstream fixtures | tests an item's upstream commitments and their returns | 3 | tools/loop/upstream.py@d7c8e6ac:2 |
| loop review bounds fixtures | tests each review loop's round bound from the policy file | 3 | tools/loop/review_bounds.py@510228a0:2 |
| loop composition fixtures | tests a build's composition pinned and moved per step | 3 | tools/loop/composition.py@43684e14:2 |
| loop adapt fixtures | tests a build's own flow changes proposed and applied | 3 | tools/loop/adapt.py@b496531b:2 |
| loop budget fixtures | tests a build's rework budget and what draws on it | 3 | tools/loop/budget.py@bfef8c85:2 |
| loop termination | checks every composition a build can run terminates | 3 | tools/loop/termination.py@c8525e2c:2 |
| loop breakpoint fixtures | tests a build's breakpoints at its item boundaries | 3 | tools/loop/breakpoints.py@52627944:2 |
| loop scenario fixtures | checks the scenario kind's rows and their conflicts | 3 | tools/loop/scenario.py@842a953a:2 |
| loop transition tables | checks the transition tables every mover in the target reads | 2 | tools/loop/kit.toml@a479e408:188 |
| loop stage coverage | joins every product part both ways to its stage | 3 | tools/loop/stage_coverage.py@5a7404bf:2 |
| loop command conformance | gates the command kind's rows | 3 | tools/loop/factories.py@835d45ef:2 |
| loop factories fixtures | self-tests the factories of six registered kinds | 3 | tools/loop/factories.py@835d45ef:2 |
| layer dependencies (the core never depends on an expansion) | refuses a core dependency on an expansion | 1 | tools/gate-legs.json@e63bd4e0:3050 |
| core meta-check | joins every principle both ways to what enforces it | 3 | tools/playbook/core.py@854477bd:4 |
| core kinds | checks the core kinds' conformance-gate contract | 3 | tools/playbook/core.py@854477bd:5 |
| core skills conformance | gates the skill kind's population | 3 | tools/playbook/core.py@854477bd:5 |
| core practices conformance | gates the practice kind's population | 3 | tools/playbook/core.py@854477bd:5 |
| core selftest | plants each core check's break in a throwaway repository | 3 | tools/playbook/core.py@854477bd:8 |
| instruction ladder (level is the one term) | requires level to be the one term for a ladder place | 1 | tools/gate-legs.json@e63bd4e0:3153 |
| instruction grammar (statement types, provenance lock) | checks instruction statement types and the provenance lock | 1 | tools/gate-legs.json@e63bd4e0:3170 |
| instruction units (schema, one fact) | checks the instruction unit schema and one fact per unit | 1 | tools/gate-legs.json@e63bd4e0:3187 |
| instruction render (one renderer of record) | requires one renderer of record per instruction file | 1 | tools/gate-legs.json@e63bd4e0:3205 |
| instruction envelopes | checks every instruction document against its envelope | 3 | tools/playbook/instruction_units.py@844b899b:21 |
| instruction units selftest | plants each instruction-unit break in a throwaway tree | 3 | tools/playbook/instruction_units.py@844b899b:15 |
| instruction edits (manifest checks) | runs the instruction edit path's manifest checks | 1 | tools/gate-legs.json@e63bd4e0:3257 |
| instruction edits selftest | self-tests the one write path for instruction units | 3 | tools/playbook/instructions_edit.py@4d0923c2:2 |
| tags (the resolver's checks) | runs the tag resolver's checks | 1 | tools/gate-legs.json@e63bd4e0:3291 |
| positional (the citation check alone) | runs the positional file:line citation check alone | 1 | tools/gate-legs.json@e63bd4e0:3309 |
| tags positional selftest | self-tests the positional citation population | 3 | tools/playbook/positional.py@35ec5e22:1 |
| tags bundle selftest | self-tests bundling a tag's node and its inbound edges | 3 | tools/playbook/tag_bundle.py@773a5b42:1 |
| edges (every declared edge parses, is registered and resolves) | requires every declared edge to parse, register and resolve | 1 | tools/gate-legs.json@e63bd4e0:3362 |
| writing practice (records and units) | runs the writing practice's checks on records and units | 1 | tools/gate-legs.json@e63bd4e0:3380 |
| one-owner | requires each namespace, kind and kit unit to name one owner | 3 | tools/playbook/writing_practice.py@c129baaa:25 |
| policy fixtures | proves on a fixture that each policy arm can red | 3 | tools/policy/check_policy.py@db1db6e9:1 |
| leg ceilings clear their evidenced maximum | checks each leg's ceiling against its recorded evidence | 3 | tools/run-gates/derive-ceilings.py@7d58ebdb:2 |
| every held leg is budgeted, every budget row resolves | checks each held self-test's on-demand cost declaration | 3 | tools/run-gates/run-selftests.sh@f6685fa0:2 |
| python reads (a name never bound, an import outside its guard) | catches a Python name never bound or an unguarded import | 1 | tools/gate-legs.json@e63bd4e0:3559 |
| receipt sync (installed files match the receipt) | checks the installed files match the deployer's receipt | 1 | tools/gate-legs.json@e63bd4e0:3575 |
| spec-tokens self-test | arms the spec-tokens check red and green | 3 | tools/check-spec-tokens.test.sh@8c5495e6:2 |
| chain-packet self-test | arms the chain-packet door red and green | 3 | tools/chain-packet.test.sh@396018d9:2 |
| kit-placeholders self-test | arms the kit-placeholders check red and green | 3 | tools/check-kit-placeholders.test.sh@009ed435:2 |
| selftest harness self-test | arms the shared self-test harness from outside it | 3 | tools/lib/lib-selftest.test.sh@e5bf94d6:2 |
| extract-arms self-test | arms the four states the arm extractor can report | 3 | tools/lib/extract-arms.test.sh@b179a5b6:2 |
| run-selftests self-test | observes every refusal of the on-demand self-test runner | 3 | tools/run-gates/run-selftests.test.sh@d6a07964:2 |

## Put to the owner

none. The rule reached every leg, so no pending population, no `purpose-pending.txt` and no ask
row exist (S6, S7).
