**Serves:** research KICK-dKeptSession-69

# Brief — dKeptSession: the run branch reconciled with origin/main, and the run's own full-bar reds cleared

## The prompt

> /unattended dKeptSession

## The brief

### Goal

`origin/main` has moved 634 commits (DERIVED, `git rev-list --count c2a407b0..8b8b1374`) past this run's BASE `c2a407b0`. dWitnessedBar landed at `8b8b1374`. Since then the
pre-commit leg set has refused every commit that stages a kickoff-engine or policy-kit path. Seven of its 100 legs (DERIVED, the hook's `gates RED — 7/100` line) are
red on the run head:

- Tied to `origin/main`:
  - `drift-audit records`: RATCHET WEAKENED against origin/main's pins.
  - `policy check`: `arm_reader_coverage` finds 20 keys dWitnessedBar landed with no reader in this tree.
- Left by this run's own units:
  - `shell hygiene (a location probe asked from a moved directory)`, at three sites in `skills/session-kickoff/card-store.fixture.sh`.
  - `shell hygiene (a stage committed with no staged-diff test)`, at one site in the same file.
  - `shell hygiene (a fork spent on builtin work)`: `pure-fn-subst` in `skills/session-kickoff/manifest-check.sh` measures 5 against a registry
    of 2, and `cat-file` in `tools/hooks/scratch-guard.test.sh` measures 20 against 11.
  - `python reads`: the build-index selftest, gotchas selftest, memory-recall kit selftest and recall floor legs import
    `tools/policy/presets.py` and `tools/memory-tree/design_lib.py` outside their guards.
  - `step-rows-frozen`: KICK-dKeptSession-4 changed `tools/govkit/steps/kickoff_facts_to_overlay.py`, the program a landed
    step's argv names. The leg says to ship the correction as a new step.

A trial `git merge --no-commit --no-ff origin/main` on the run branch conflicts in 13 files (DERIVED, `git diff --name-only --diff-filter=U`):

- Product code:
  - `tools/policy/policy.py` (6 hunks), `tools/policy/check_policy.py` (2), `tools/policy/kit.toml` (2), `tools/policy/README.md` (4).
- Generated:
  - `.governance/policy.json`, `help/reference/policy.md`, `memory/map/generated/symbols.json`.
- Row registries:
  - `memory/project/positional-refs.txt`, `memory/project/unpinned-facts.txt`, `memory/project/docs-undocumented.txt`,
    `tools/playbook/core-pending.txt`, `tools/run-gates/selftest-budgets.txt`.
- The kickoff manifest stamp: `memory/guides/SESSION-KICKOFF.md`.

The product conflicts are one design collision. TOOL-dWitnessedBar-20 moved the legacy-homes list into a ledger population
at `memory/project/legacy-homes.txt`, graded and written by the baseline ledger factory and registered in govkit's registry.
KICK-dKeptSession-19 built a shrink-list factory (`read_shrink_base`, `write_shrink_file`) over that same list. It also put
the unscanned-readers list, KICK-dKeptSession-19's unnamed-keys list and KICK-dKeptSession-16's unpurposed-namespaces list
through it. `[reuse]` allows one factory per kind.

Write the spec of KICK-dKeptSession-69 as a new file, `memory/builds/dKeptSession/spec/2026-11-22-spec-KICK-dKeptSession-69.md`,
to `memory/TEMPLATE-SPEC.md`:

- Header: `INPROGRESS`, rev-1, 2026-11-22, node d, Tier-2, base the run head, streams tooling, order 9, advances
  KICK-dKeptSession-29.
- Second line: `**Derived:** PLAY-dClosedLoop-2`, the binding KICK-dKeptSession-67 carries.

### Items

1. F-merge: every commit in this worktree runs the PRIMARY tree's hooks (`core.hooksPath` names
   `C:\projects\coding-governance\.githooks`), and the primary tree now sits at `origin/main` `8b8b1374`. So every commit,
   a records-only one included, now meets main's hooks over this branch's pre-main tree, and is refused. No dispatch row,
   brief or spec can be committed first, and a pass worktree is not reachable. The reconcile is therefore ONE commit on the
   run branch, made the way `push-main.sh`'s conflict refusal says: the main loop runs `git merge --no-ff --no-commit
   origin/main` in the run worktree, the unit's builder resolves the conflicts and makes this unit's fixes in that
   worktree, and the main loop commits the merge, with this spec, its records and `Pass: KICK-dKeptSession-69`, once
   main's hooks pass over it. State the resolution for each of the 13 files (DERIVED, as above):
   - Generated outputs are re-rendered, never hand-merged.
   - Row registries are unioned, then shrunk or re-derived by their own verbs.
   - The kickoff manifest is re-stamped.
   - Each product hunk follows F-factory.
2. F-factory: decide how the two factories meet, with the alternatives in §4's rejected list. The default is the
   feature-rich, single-factory one: legacy-homes is the ledger population as main has it, and this run's other lists move
   onto main's baseline ledger factory, with the shrink-list factory deleted. If you keep the shrink-list factory, give the
   reason main's factory cannot carry those lists. Name every caller that changes (KICK-dKeptSession-19's and -16's arms and
   cases, `cmd_lists`, `check_policy.py`'s fixtures), and every CLOSED unit's spec text this supersedes. That superseded
   text is answered in this unit's own acceptance ledger, as KICK-dKeptSession-49 rev-6 ruled.
3. F-own-reds: name the fix for each of the five red legs this run left, and the criterion that observes each leg green:
   - Shell hygiene: scrub the three location probes; test the stage before the fixture's commit; bring each `$(f …)` and
     `$(cat …)` count back to its registry row through the no-fork forms.
   - `python reads`: widen each named leg's guard in `tools/gate-legs.json` to the module it imports.
   - `step-rows-frozen`: restore the landed step program's bytes, and ship KICK-dKeptSession-4's scaffold change as a new
     step row, as the leg's remedy says.
   Read `tools/govkit/upgrade_steps.py#check_frozen` and the step registry for how a new step is declared.
4. F-inherited: check whether the two legs tied to `origin/main` go green on the merged tree. Where one stays red, find
   whether it is red on `origin/main` itself, then either attribute it with `GATE_ATTRIBUTE` or fix it, and say which.
5. F-behaviour: every criterion names its command and the exit and output it observes. The pass legs
   (`bash tools/run-gates/pass-legs.sh`) and the policy fixtures are named in §7. No suite runs in the pass.
6. Hook paths, citations and size, as the build's other specs keep them:
   - Files touched names every path the merge and the fixes move, including `symbols.json`, `selftest-budgets.txt` where a
     `plants=` token moves, and the kickoff manifest re-stamp.
   - Cite code as `path#symbol`; leave no `path:number` token unless it is a blob pin.
   - Pin every figure, keep within the live-spec size cap, and leave no fork open except one that would change a
     governance carrier.

### Acceptance

The new spec exists. `bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, `--only 29`,
`python tools/check-spec-tokens.py --spec <path>`, a PLAIN `python tools/playbook/writing_practice.py check pinned-facts`
and `bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-69` report nothing for it.

### Gates

The memory hygiene gate, the spec-token checker, the pinned-facts check, the driver's `--check-specs` and the naming
lexicon; no other.

### Non-goals

No product code, no commit, no index render, and no spec other than the new one. Do not start the merge in the run
worktree. Read `origin/main` with `git show origin/main:<path>` and `git diff HEAD...origin/main -- <path>`.
