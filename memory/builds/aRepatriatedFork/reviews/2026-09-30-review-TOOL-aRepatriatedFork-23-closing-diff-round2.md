**Serves:** diff-review TOOL-aRepatriatedFork-23 TOOL-aRepatriatedFork-24 TOOL-aRepatriatedFork-29 TOOL-aRepatriatedFork-30 TOOL-aRepatriatedFork-46

# aRepatriatedFork: Tier-2 review of the cumulative diff landing on main, round 2

*Node `a`, 2026-09-30. This is round 2 of the integration-boundary review (§8). It covers the round-1
fold: 13 commits on `branch/arepatriated-fork-build-e42158` since `7de665e5`. Four primed finder
lenses fanned out, and every finding went to an adversarial skeptic prompted to refute it. The unit
ids on the binding line are the ones the range's commit messages carry.*

**Range reviewed: `7de665e56d2f0e9ae9b7cd9596cfedb0e35c6b4a...HEAD`** (HEAD = `c7fa802e` when this report was written).

**Round: 2.**

## Verdict: CLEAN WITH FIXES

Nothing in this round blocks the landing, but three items are open and none is fixed in this range.
The HIGH item matters most. The round-1 B1 fix checks the default bar's receipt and its runner, but
the runner still takes its leg manifest from the `GATE_LEGS` environment variable, and its python
from `GOV_PYTHON`. Setting either one lets a RED tracked bar land with a clean `git status`. That
gap existed before this diff. It is still HIGH, because it defeats the guarantee B1's fix states.
The two LOW items are a false red when `GIT_DIR` is inherited, and a gotcha page that still describes
the deleted install-prefix registries as live.

## Review shape and run integrity

- **Raw 8, confirmed 4, refuted 4, unverified 0. Precision 0.50** (4 / 8).
- **Adjudicated tally, by item:** 3 items. 0 BLOCKER, 1 HIGH, 0 MEDIUM, 2 LOW.
- **Adjudicated tally, by raw confirmed finding:** 4. 0 BLOCKER, 2 HIGH, 0 MEDIUM, 2 LOW. The two
  counts differ because findings 1 and 4 are one defect. Two lenses reported it, one as MEDIUM and one
  as HIGH, and it is merged into item H1 at HIGH.
- **Run integrity:** lenses 4/4 returned, 0 DIED. Skeptic batches 4/4 returned, 0 DIED. 0
  contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates. The run
  is complete: no lens or batch died, so the finding set was not cut short by the harness.
- The four refuted findings are the raw ids missing from the table below. They were dropped on the
  skeptic's refutation and are not carried as open items.
- Precision at 0.50 is on the §8 threshold. The next round should narrow lens scope and priming
  before it adds any agents.
- The cited lines were spot-checked against HEAD while this report was written:
  `.githooks/pre-push:817-820` (the two `check_reviewed_file` calls), `:363` (`unset GOV_KITROOT`),
  `:531` (`GOV_PYTHON` in the resolver), `:1069` (`$gate </dev/null`), `run-gates.sh:147`,
  `check-verifier-fanout.sh:138`, `check-review-join.sh:177`, `check-dead-paths.sh:193` (the
  `memory/map/features/*` haystack), and the gotcha's line 34. `tools/install-prefix-*.txt` no
  longer exists.

| Item | Severity | Finding ids | Where | One line |
|------|----------|-------------|-------|----------|
| H1 | HIGH | 1, 4 | `.githooks/pre-push:819` | `GATE_LEGS` or `GOV_PYTHON` from the environment lets the vetted runner certify a planted manifest |
| L1 | LOW | 7 | `tools/workflows/check-verifier-fanout.sh:138` | An inherited `GIT_DIR` makes both fan-out gates resolve the hook under `tools/workflows/` and go red |
| L2 | LOW | 8 | `tools/check-dead-paths.sh:166` | A live gotcha still describes the deleted install-prefix registries, and the dead-paths gate cannot see it |

## HIGH

### H1: the default bar's manifest and python are still chosen by the environment (findings 1, 4)

**Where:** `.githooks/pre-push:819` is where the fix vets the runner. `.githooks/pre-push:1069` runs
`$gate </dev/null` with the inherited environment. `tools/run-gates/run-gates.sh:147` reads
`LEGS_FILE="${GATE_LEGS:-$(dirname "$KITREL")/gate-legs.json}"`.

**Defect.** B1's fix vets `.governance/install.json` and the runner file with `check_reviewed_file`.
It does not vet the manifest that runner reads. The hook never unsets or checks `GATE_LEGS`: outside
the tests, nothing mentions it. The hook passes `GOV_PYTHON` to its own `resolve_python` (line 531),
and the runner does the same at its line 53. Predicates 6 and 7 hash the in-tree
`${KP}gate-legs.json`, never the `LEGS_FILE` the runner actually reads.

**Repro.** Run `GATE_LEGS=/tmp/one-green-leg.json bash tools/push-main.sh` on a tree whose tracked bar
is RED. The receipt and runner are tracked and unmodified, so both `check_reviewed_file` calls pass.
The planted manifest sits outside the tree, so `git status` stays empty and the dirty-tree refusal
never fires. The runner runs one always-green leg, returns 0, and the push lands. A `GOV_PYTHON`
pointing at a planted interpreter has the same effect, because both the resolver and the runner's
manifest parser run whatever it names. A second route skips the environment: in a repo that tracks
no manifest at `${KP}gate-legs.json`, an ignored file at that path is hashed by predicate 7 and read
by the runner, and neither goes through the new check.

**Why HIGH and not BLOCKER.** The environment variable is set by whoever runs the push, and an
attended caller could equally pass `--no-verify`. The gap also predates this range. But the hook
treats the environment as hostile everywhere else. It unsets `GOV_KITROOT` at line 363. It holds
`GOV_GATE_CMD` to `check_bar_command`, with `GOV_GATE_CMD_TEST` as a labelled stub escape. An
unattended run cannot type `--no-verify` into an owner's turn, but it can export a variable. B1's fix
says the default bar is one the repository reviews, and this is a reachable way around that.

**Fix.**

1. On the default-bar path (`GOV_GATE_CMD` empty and `GOV_GATE_CMD_TEST` unset), `unset GATE_LEGS`
   next to `unset GOV_KITROOT`, or refuse it as `bar-refused` when it is set. If fixtures need it
   (`pre-push.runlog.test.sh:526` drives the hook with it set), keep it only under the
   `GOV_GATE_CMD_TEST` stub label, the way that escape already works.
2. Add `check_reviewed_file "${KP}gate-legs.json" "$main_local" "is the leg manifest the default bar runs"`
   next to the runner check, which closes the ignored-manifest route.
3. Run the default bar with a python the resolver itself vetted, or refuse a set `GOV_PYTHON` on a
   default-branch push.

**Left-shift gate.** Add an arm to `.githooks/pre-push.test.sh` in the B1 shape: a RED tracked bar,
`GATE_LEGS` pointing at an untracked always-green manifest, and the real tracked `run-gates.sh`.
Expect `gate-red` or `bar-refused`. Add a sibling arm for `GOV_PYTHON` and one for an ignored
`${KP}gate-legs.json`. Stage the fix out first and watch each arm go RED (§7). The class is "an
environment knob that selects what the vetted bar runs". A structural check can find every
`${VAR:-` default in `run-gates.sh` and assert that each one is unset, vetted or test-labelled in
the hook, so the next knob added to the runner cannot slip past.

## LOW

### L1: both fan-out gates ask git for the root again, and an inherited GIT_DIR breaks them (finding 7)

**Where:** `tools/workflows/check-verifier-fanout.sh:138` and `tools/workflows/check-review-join.sh:177`,
both reading `HOOK="$(git -C "$HERE" rev-parse --show-toplevel)/$_hk_dir/agent-cap.js"`.

**Defect.** The round-1 H1 fix finds the hook's kit dir with a resolver that walks up to `.git`. It
then asks git for the root a second time, instead of using the root the resolver already found. With
`GIT_DIR` exported, `git -C tools/workflows rev-parse --show-toplevel` returns `tools/workflows`
itself. `HOOK` then points at `<root>/tools/workflows/tools/hooks/agent-cap.js`.

**Repro.** This was reproduced in this worktree. Export the linked worktree's absolute `GIT_DIR`, and
both gates exit with `MODULE_NOT_FOUND`. The pre-fix gate at `7de665e5` printed
`verifier-fanout: clean` under the same environment. Git exports an absolute `GIT_DIR` to
`git rebase --exec` and to pre-push in a linked worktree. The tracked pre-push and pre-commit hooks
unset it, so the bar at those two boundaries is not affected. A `rebase --exec` run, a merge-driver
context, or any shell that inherits `GIT_DIR` gets a false red. The `repo_root()` docstring in
`govkit.py` records this exact hazard.

**Fix.** Stop asking git a second time. Have the inline python snippet print the kit directory it
already resolved as an absolute path (`print(d.as_posix())`), and set `HOOK="$_hk_dir/agent-cap.js"`.
If the git call stays, strip the inherited variables first:
`$(cd "$HERE" && env -u GIT_DIR -u GIT_WORK_TREE git rev-parse --show-toplevel)`. Make the same
change in both gates.

**Left-shift gate.** Add an arm to `check-review-join.test.sh` and to the fan-out gate's test that
runs the gate with `GIT_DIR` exported and expects `clean`. The class is "re-deriving a root through
git where an inherited `GIT_DIR` redirects it". A scan for `rev-parse --show-toplevel` in kit
scripts that does not sit behind an `env -u GIT_DIR` would catch the next one.

### L2: a live gotcha still describes the deleted install-prefix registries (finding 8)

**Where:** `memory/gotchas/line-keyed-registry-reds-on-a-file-that-grew.md`, lines 15-39. Line 34
says `tools/check-install-prefix.sh` "has a second arm over `tools/install-prefix-carried.txt`". The
gate side is `tools/check-dead-paths.sh`, whose haystack (line 193) reads `memory/map/features/*` only.

**Defect.** Round-1 L1 was meant to leave nothing describing the deleted ledger and registry as
live. This page still tells the reader to re-key waiver rows and hand-write ledger rows in two files
that no longer exist. `check-install-prefix.sh` now says it has no waiver registry and no list of
carried literals. The page was last changed at `4042505a`, so the L1 fix never touched it.
`gotchas.py --for-paths tools/check-install-prefix.sh` still returns it as a live checklist item. The
dead-paths gate cannot catch it, because it covers only the one instance (the map dossiers) and not
the class.

**Fix.** Rewrite that section in the past tense and point it at the pure ban TOOL-aRepatriatedFork-30
left, or supersede the gotcha now that the files it describes are deleted.

**Left-shift gate.** Decide whether `memory/gotchas/`, which `gotchas.py` serves as a live
checklist, joins `memory/map/features/` in the dead-paths haystack. If it does, add a red arm to
`check-dead-paths.test.sh` in the shape of the 3c dossier arm: a gotcha naming a deleted path must
go RED. The class is "a document served as live guidance that names a deleted path". Every surface
that is served as live belongs in the haystack, not only the one the symptom came from.

## What this round does not claim

- The refuted findings were dropped on the skeptic's word and were not re-checked by hand.
- A zero MEDIUM count is the adjudicated result of a complete run, not a count left short by a
  lens that died.
- No fix in this report has been applied or observed RED/GREEN. Each left-shift arm is a proposal
  until its failing case has been staged and seen.
