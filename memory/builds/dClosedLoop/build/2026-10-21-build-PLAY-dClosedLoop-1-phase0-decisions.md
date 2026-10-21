# Phase 0 decisions: the nine rows P0.8 mints, in full

**Serves:** research PLAY-dClosedLoop-1

The nine `memory/DECISIONS.md` rows `PLAY-dClosedLoop-2` to `PLAY-dClosedLoop-10`, minted under dClosedLoop's slug by
P0.8 of `build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` and landed with the opening. A row is capped at
300 characters (`memory/HYGIENE.md`, check 7), so each row carries its decision and its source lines, and this record
carries each in full. ER is `build/2026-10-20-build-PLAY-dClosedLoop-1-execution.md`; every quote below is verbatim
from it.

## [row-1]

**PLAY-dClosedLoop-2 — a chain spec run closes by carry-forward, and dTrueNorth's extra unit `TOOL-dTrueNorth-7`
lets it carry every unit it adds.**
- Sources: "Split phases (Recommended)" (ER:84), "dTrueNorth's extra unit (Recommended)" (ER:232) and "Carry it too
  (Recommended)" (ER:320).
- The extra unit is `**Derived:**` from this row. The row records the owner's approval of that unit as a departure
  from v2 (the plan's `[deviations]`), the starting-roster reading `[phase-1]` specifies included.
- It lets a spec run carry any unit it adds, from a review or an adopted discovery, forward to its own build run,
  once. The build run builds it and never defers it again.
- The row names the unit's id so the deviation instrument's approver arm can look the cited id up here, holding no
  decision id itself: "Rows name the ids (Recommended)" (ER `[phase0-answers]`).

## [row-2]

**PLAY-dClosedLoop-3 — the chain's `may:` grant.**
- Source: "One decision row (Recommended)" (ER:181), held in the walk: "Hold, on to Phase 1 (Recommended)" (ER:461).
- Each chain build may make the governance-carrier and public-surface changes its own `[chain]` clauses name. All 22
  chain READMEs' `may:` lines cite this row; dTrueNorth's also cites `PLAY-dClosedLoop-2`, since the carry-forward
  condition changes a carrier no `[chain]` clause names.
- A governance carrier is a path on `PLAY-dClosedLoop-10`'s list. A run's M3 judges whether a change is covered
  (`tools/unattended/lib-unattended.sh:1455-1458`). The grant lifts veto 2 only.

## [row-3]

**PLAY-dClosedLoop-4 — the chain's deviation values, and the departure from `cl-dClosedLoop-0004`.**
- Sources: "departures are recorded and explained at the end, nothing is parked or blocked - the build must go
  through to completion." (ER:103-104); "A deviation, your values (Recommended)" (ER:189); "Report, as read
  (Recommended)" (ER:255); "The adding build (Recommended)" (ER:396).
- The chain runs with `deviation.gate = report` and `deviation.approval = author-recorded`, applied to every run and
  to the bootstrap instruments. The owner approves the departure from `cl-dClosedLoop-0004`.
- The build that adds each key sets the chain's value in its own landing: dDeclaredLoop's spec carries
  `deviation.approval = author-recorded` and dScopedBuild's carries `deviation.gate = report`, each recorded as a
  departure citing this row. Nothing waits on the owner.

## [row-4]

**PLAY-dClosedLoop-5 — node b is offered chain spec runs only.**
- Source: "Spec runs only" (ER:219).
- The schedule script declares it as `SPEC_ONLY`, citing the answer, because no file it reads holds it.

## [row-5]

**PLAY-dClosedLoop-6 — the standing ruling for residual forks, and the weakest bound relaxed.**
- Sources: "Standing ruling" (ER:240); "Standing ruling takes it (Recommended)" (ER:388); "Relax the weakest bound"
  (ER:328).
- Where every surviving option passes veto 1 and fails only veto 3 or the goal bound, the run takes "the most capable
  option that fails only the security veto or the goal bound" (ER:237-238). The same rung takes a fork whose only
  options trip veto 2 outside the grant, marked `widens: <change>`.
- A fork with no option left has its weakest failing bound dropped, and the run builds.
- Each choice is a departure, marked as README rule 6 says. Every non-`none` `widens:` or `relaxes:` and every
  `grants:` choice is listed first in the build's departures report (ER:284-285, :347-348, :383-384).

## [row-6]

**PLAY-dClosedLoop-7 — the driver-rewriting builds, and the self-test waiver.**
- Sources: "Land through new code (Recommended)" (ER:248); "Test in its spec (Recommended)" (ER:264); "You type it
  (Recommended)" (ER:270); "Waive in each README" (ER:476), at the scope the walk's correction states (ER:544-557).
- The driver-rewriting builds land through their own new code. dPlacedRequest's claim migration,
  `cl-dClosedLoop-0120`, carries its test; the row names that clause so the approver arm can look it up: "Rows name
  the ids (Recommended)" (ER `[phase0-answers]`). The owner types every start.
- Each driver-changing build waives the unattended kit's own on-demand suites for its landing in its README, in
  dAlignedCarrier's form, proving its driver changes by targeted probes and its own planted tests. Its close still
  runs the flagged bar, `GATE_FULL=1 GATE_SELFTESTS=1`.

## [row-7]

**PLAY-dClosedLoop-8 — the coordination rules.**
- Source: the owner walked the plan's handoffs and coordination and changed nothing: "On to the schedule
  (Recommended)" (ER:502).
- Push the run branch after every pass; never preflight over a claim; re-run the schedule script at every landing;
  reconcile at a prepare conflict (the plan's `[coordination]`).

## [row-8]

**PLAY-dClosedLoop-9 — the unit family follows the main stream.**
- Source: "Family by stream" (ER:438), over the recommended "TOOL for all".
- PLAY for charter and playbook builds, KICK for session and kickoff, DEPL for deploy, TOOL otherwise, matched on each
  build's Stage and slug noun, whole words. `open.py --families` prints the table: two PLAY, one KICK, one DEPL and
  eighteen TOOL builds.

## [row-9]

**PLAY-dClosedLoop-10 — the governance carrier.**
- Source: "Define it in Phase 0 (Recommended)" (ER:525).
- A governance carrier is a tracked path on the list `open.py --carriers` derives from the tree at the opening commit,
  quoted whole in `[carriers]` below. The grant, `PLAY-dClosedLoop-3`, reads against it.
- Nothing else is a carrier: the build records, `memory/DECISIONS.md`, the backlogs and the root `README.md` are
  records, not rules a run is held to. `open.py --carriers --check` reds a tracked path under a selector the list
  omits.

## [carriers]

The list `open.py --carriers` printed at the opening commit's parent, `8d19dd714`, whole:

````text
Governance carriers at HEAD `8d19dd7149b1`, P0.8 row 9's six selectors: 112 entries over 451 tracked paths.

1. routed product paths (`.memory-tree.conf` `ROUTED_PATHS`: tools/ skills/ coding-governance-agents.template.md WIRE-INTO-PROJECT.md): 63 entries, 17 kits with a `kit.toml`, 4 other directories, 42 files
   - `WIRE-INTO-PROJECT.md`
   - `coding-governance-agents.template.md`
   - `skills/deploy-governance/` · 1 tracked files
   - `skills/session-kickoff/` · 6 tracked files
   - `tools/agent-cap-restatement-waivers.txt`
   - `tools/agent-instructions/` · kit · 4 tracked files
   - `tools/branch-reconcile/` · kit · 6 tracked files
   - `tools/check-agent-cap-restatement.sh`
   - `tools/check-agent-cap-restatement.test.sh`
   - `tools/check-dead-paths.sh`
   - `tools/check-dead-paths.test.sh`
   - `tools/check-hook-destinations.sh`
   - `tools/check-hook-destinations.test.sh`
   - `tools/check-install-prefix.sh`
   - `tools/check-install-prefix.test.sh`
   - `tools/check-kit-placeholders.py`
   - `tools/check-kit-placeholders.test.sh`
   - `tools/check-kit-versions.sh`
   - `tools/check-line-length.sh`
   - `tools/check-line-length.test.sh`
   - `tools/check-microformats.sh`
   - `tools/check-microformats.test.sh`
   - `tools/check-placeholders.sh`
   - `tools/check-placeholders.test.sh`
   - `tools/check-playbook-parity.sh`
   - `tools/check-playbook-parity.test.sh`
   - `tools/check-remote-literals.sh`
   - `tools/check-remote-literals.test.sh`
   - `tools/check-spec-tokens.py`
   - `tools/check-spec-tokens.test.sh`
   - `tools/check-template-size.sh`
   - `tools/check-template-size.test.sh`
   - `tools/check-testsuite-counts.sh`
   - `tools/check-testsuite-counts.test.sh`
   - `tools/check-wiring.fragment.json`
   - `tools/check-wiring.sh`
   - `tools/check-wiring.test.sh`
   - `tools/codebase-map/` · kit · 20 tracked files
   - `tools/dead-path-waivers.txt`
   - `tools/drift-audit/` · kit · 8 tracked files
   - `tools/gate-legs.json`
   - `tools/gate-lint/` · kit · 6 tracked files
   - `tools/govkit/` · 24 tracked files
   - `tools/hooks/` · kit · 11 tracked files
   - `tools/lexicon/` · kit · 14 tracked files
   - `tools/lib/` · 15 tracked files
   - `tools/line-length-limits.txt`
   - `tools/memory-recall/` · kit · 17 tracked files
   - `tools/memory-tree/` · kit · 33 tracked files
   - `tools/playbook-kit-waivers.txt`
   - `tools/playbook/` · kit · 5 tracked files
   - `tools/process-monitor/` · kit · 13 tracked files
   - `tools/push-main.sh`
   - `tools/push-main.test.sh`
   - `tools/pytest-parallel-guardrails/` · kit · 7 tracked files
   - `tools/roles/` · kit · 31 tracked files
   - `tools/run-gates/` · kit · 45 tracked files
   - `tools/runlog/` · kit · 20 tracked files
   - `tools/settings-merge.py`
   - `tools/template-size-highwater.txt`
   - `tools/template-size-limits.txt`
   - `tools/unattended/` · kit · 50 tracked files
   - `tools/workflows/` · kit · 24 tracked files

2. git hooks (every tracked file under `.githooks/`, which `core.hooksPath` wires): 11 entries, 0 kits with a `kit.toml`, 0 other directories, 11 files
   - `.githooks/commit-msg`
   - `.githooks/gate-env.sh`
   - `.githooks/pre-commit`
   - `.githooks/pre-commit.test.sh`
   - `.githooks/pre-push`
   - `.githooks/pre-push.runlog.test.sh`
   - `.githooks/pre-push.test.sh`
   - `.githooks/pre-rebase`
   - `.githooks/pre_push_bar_selftest.py`
   - `.githooks/straggler-guard.sh`
   - `.githooks/straggler-guard.test.sh`

3. agent and role files (every tracked path under `.claude/`, a skill as its directory): 19 entries, 0 kits with a `kit.toml`, 7 other directories, 12 files
   - `.claude/agents/gov-builder.md`
   - `.claude/agents/gov-diff-reviewer.md`
   - `.claude/agents/gov-orienter.md`
   - `.claude/agents/gov-researcher.md`
   - `.claude/agents/gov-reuse-scout.md`
   - `.claude/agents/gov-skeptic.md`
   - `.claude/agents/gov-spec-reviewer.md`
   - `.claude/agents/gov-spec-writer.md`
   - `.claude/agents/gov-synthesizer.md`
   - `.claude/roles.json`
   - `.claude/rules/product.md`
   - `.claude/settings.json`
   - `.claude/skills/build/` · 1 tracked files
   - `.claude/skills/cleanup/` · 1 tracked files
   - `.claude/skills/drift-audit/` · 1 tracked files
   - `.claude/skills/lexicon/` · 1 tracked files
   - `.claude/skills/memory-recall/` · 1 tracked files
   - `.claude/skills/runlog/` · 1 tracked files
   - `.claude/skills/unattended/` · 1 tracked files

4. the charter (the template and its renders): 3 entries, 0 kits with a `kit.toml`, 0 other directories, 3 files
   - `AGENTS.md`
   - `CLAUDE.md`
   - `coding-governance-agents.template.md`

5. the method's guides (every tracked file under `memory/guides/`): 10 entries, 0 kits with a `kit.toml`, 0 other directories, 10 files
   - `memory/guides/ANNOTATION-STYLE.md`
   - `memory/guides/BUILD-METHOD.md`
   - `memory/guides/MERGE-BAR.md`
   - `memory/guides/PLAYBOOK-TEMPLATE.md`
   - `memory/guides/REVIEW-PROTOCOL.md`
   - `memory/guides/SESSION-KICKOFF.md`
   - `memory/guides/UNATTENDED-ASKS.md`
   - `memory/guides/UNATTENDED-PROTOCOL.md`
   - `memory/guides/UNATTENDED-STOPS.md`
   - `memory/guides/UNATTENDED-VERBS.md`

6. the root confs (a root `.<name>.conf`, `.gitattributes`, and every tracked file under `.governance/`): 7 entries, 0 kits with a `kit.toml`, 0 other directories, 7 files
   - `.codebase-map.conf`
   - `.gitattributes`
   - `.governance/deploy.toml`
   - `.lexicon.conf`
   - `.memory-tree.conf`
   - `.process-monitor.conf`
   - `.unattended.conf`
````
