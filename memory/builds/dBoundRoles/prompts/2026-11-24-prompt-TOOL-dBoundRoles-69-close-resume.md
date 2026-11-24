**Serves:** journal TOOL-dBoundRoles-69

# Resume brief — the close of the dBoundRoles build run

Every unit of the roster is CLOSED and the run stands at VERIFYING on `branch/unattended-dboundroles-62c3df`. The
first resume brief, `2026-11-23-prompt-TOOL-dBoundRoles-51-resume-node-a.md`, still holds the close's steps and its owed
list. This one adds what the close has found.

## What stops the run

- **The closing review has no reviewer here.** This build merges the reviewer roles into `gov-reviewer`, and a session
  registers the agent types of the tree it was launched from. The session that built units 56 to 69 was launched from a
  tree at main, so it holds `gov-diff-reviewer` and no `gov-reviewer`, while the role index of the run worktree admits
  only `gov-reviewer`. The review at the landed harness bytes ran its probes and then every lens died with the type not
  found (run `wf_a327c063-5b6`, exit deferred-platform). Launch the resuming session from the run worktree itself, so it
  loads that worktree's `.claude/agents` and its hooks.
- **The flagged bar is the owner's.** The range touches `tools/`, so the VERIFYING notice owes `GATE_FULL=1
  GATE_SELFTESTS=1` on the one `--close`. The owner decides it; it is never set on a session's own account.

## What the resuming session does

1. Take over with `--resume dBoundRoles`, the keepalive first, in a session launched from the run worktree.
2. Run the closing review, round one, from the run BASE to the tip, at the landed bytes of `tools/workflows/tier2-review.js`
   by the README's swap rule. The args of `wf_a327c063-5b6` are the ones to repeat, with the new head.
3. Work the rest of the owed list below, then prepare, authorize, close and land as the first brief says.

## Suite readings at VERIFYING

Each suite was run directly on node a with the session's own variables dropped, as `env -i` with the path, home and temp
variables kept. The base readings are a detached tree at the run BASE.

- `spawn-guard self-test`: red at `b25da7bd`, green at `3eb29b72`, at its floor exactly (red-fix 53).
- `roles adopter self-test`: own reds fixed at `db7b554c` (red-fix 54). Arm 8 stays red and is red at BASE: the roster
  lines of `gov-tester` and, from this build, `gov-prompt-writer` pass 200 characters where no policy kit answers.
- `roles render selftest`, `marker contracts`, `tier2-review self-test`, `scratch-guard self-test`, `playbook render
  selftest` and `loop placement fixtures`: green.
- `unattended-build self-test`: own red fixed at `d1e76e61` (red-fix 55). The D arm over `DISPOSAL_SCHEMA` is red at BASE.
- `memory-recall kit selftest`: the with-hook remedy case and its adopter-layout echo are red at BASE too.
- `loop item kind`: every red names `record-kind.flake`, which no record-version row pins, and is red at BASE. The
  `role-core` case this build adds reds on the same refusal.
- `govkit selftest`: `reviewer-merge-AC9` was own and is fixed at `a97f0aef` (red-fix 56). The other reds, among them the
  `[aHI-5 AC4]`, `[dSP-8] AC3`, `[dSP-49] AC10`, `[aRF-1]`, `[aRF-42]` and `[aHI-3 AC6]` cases, are not attributed: the base
  run was cut short. Run it at BASE before any of them is called inherited.
- `manifest-check self-test`: reds over its card verbs, not attributed. `loop factories fixtures`, `gate-guard selftest`
  and `memory-hygiene self-test` were not run. `check-wiring self-test` and the unattended driver shards were not run.

## Owed still

- RED-first observation of every `New arm:` arm but the ones `seen_red.py --build dBoundRoles` reads back.
- The `resume = "atomic"` key on the reviewers step of `tools/roles/kit.toml` (unit 43 S37). The walker reads it and its
  absence alike, and a step row is frozen once landed, so this landing is the last chance to add it.
- The roster lines of `gov-tester` and `gov-prompt-writer`, and the `budget` of `gov-spec-writer`, whose excess is gov's
  own house text.
- `memory/project/shell-role.txt` drift, the budget rows re-priced from the first readings, unit 43's ledger AC27, and the
  rest of the first brief's list.
- The kickoff-manifest, dead-path and lexicon reds of every pass leg run stay inherited, as the first brief says.

## For the owner at the wrap-up

- The main loop's decision that a CLOSED spec is never edited, `build/2026-11-24-build-TOOL-dBoundRoles-58-1-main-loop-decision.md`.
- Asks 70 to 73 and 75 are deferred on the child units that build them; 74 and 76 are closed; unit 69 closes ask 27.
- The first brief's owner items, PLAY-dOrderedCharter-89 and the defer acts of units 20, 25 and 43.
