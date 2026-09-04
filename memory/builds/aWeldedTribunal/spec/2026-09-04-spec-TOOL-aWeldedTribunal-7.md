# TOOL-aWeldedTribunal-7 — the wiring check names the hooks that will actually run

**Status:** CLOSED · rev-3 · 2026-09-04 · node a · Tier-2 · base 9b5ae688 · streams tooling · order 7 · ratified 2026-09-04

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-review-TOOL-aWeldedTribunal-1-8-diff-round1.md](../reviews/2026-09-04-review-TOOL-aWeldedTribunal-1-8-diff-round1.md) | diff-review | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-8 |
| [2026-09-04-review-TOOL-aWeldedTribunal-1-8-diff-round2.md](../reviews/2026-09-04-review-TOOL-aWeldedTribunal-1-8-diff-round2.md) | diff-review | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-8 |
| [2026-09-04-review-TOOL-aWeldedTribunal-1-8-round1.md](../reviews/2026-09-04-review-TOOL-aWeldedTribunal-1-8-round1.md) | spec-audit | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-8 |
| [2026-09-04-review-TOOL-aWeldedTribunal-1-8-round2.md](../reviews/2026-09-04-review-TOOL-aWeldedTribunal-1-8-round2.md) | spec-audit | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-8 |
| [2026-09-05-review-TOOL-aWeldedTribunal-1-8-diff-round3.md](../reviews/2026-09-05-review-TOOL-aWeldedTribunal-1-8-diff-round3.md) | diff-review | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-8 |
| [2026-09-05-review-TOOL-aWeldedTribunal-1-8-diff-round4.md](../reviews/2026-09-05-review-TOOL-aWeldedTribunal-1-8-diff-round4.md) | diff-review | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-8 |

<!-- /gen:spec-records -->

## 1. Goal

`core.hooksPath` is repo-global and absolute, so in this multi-worktree layout the hooks that gate a
commit and a push come from whatever the PRIMARY tree has checked out — not from the tree being
worked in. Check H of `tools/check-wiring.sh` already resolves that path and asserts only that a
`pre-commit` file exists there. Make it also compare the resolved `pre-commit` AND `pre-push`
against the blobs the current tree tracks, and REPORT — without gating — when they differ.

## 2. Scope (IN)

- **S1** — Check H hashes the resolved `<hooksPath>/<hook>` and compares it against
  `HEAD:.githooks/<hook>` in the CURRENT tree, for each hook in a declared list. The list is
  `pre-commit` and `pre-push` today and the comparison is written OVER the list, so a third hook is
  one row rather than a third copy.
- **S2** — **A divergence prints a `note`-severity line and does NOT increment `unwired`.** This is
  the half rev-1 got wrong and it is load-bearing: `tools/check-wiring.sh:809` is
  `[ "$unwired" = 0 ] && exit 0 || exit 1`, so an `UNWIRED`-class line IS the exit code. The line
  names both hashes, the resolved path, and the branch the hook's own checkout is on.
- **S3** — A hook the current tree does not TRACK is a `skip` line naming it, never a comparison and
  never a count. Check H's entry guard is tracked `.githooks/pre-commit` alone, so an adopter that
  owns its own pre-commit and ships no pre-push must not acquire a permanent unclearable finding.
- **S4** — `.githooks/pre-push`'s header comment is corrected. It currently reads that the active
  hook is the tracked dir "so tracked == active by construction — no staleness class for THIS
  repo", which §4's measurement falsifies for exactly this layout.
- **S5** — `memory/gotchas/hookspath-resolves-into-another-checkout.md` is refreshed in the same
  commit, **written over the record's CARRIERS and not over one heading**: after the refresh, no
  paragraph of that file may assert the comparison is unwritten or unopened. Two sections say it
  today. "Its gate" says the check "is opened as a backlog item rather than written here, because a
  check whose subject is the operator's environment needs a decision about whether it reds or
  reports" — the decision §8 takes and the check S1 writes. And `:59-62`, under "What to do", says
  "**A gate on this is possible and is not written.** `check-wiring.sh` already resolves
  `core.hooksPath`; it could compare the resolved directory's blob against the tracked one at HEAD
  and report a mismatch" — a description of exactly what S1 builds, in the conditional. Rev-2 scoped
  only the first, which would leave the cited class record still asserting that the thing just built
  does not exist: verbatim the defect S5 exists to remove, one paragraph up.
- **S6** — Arms in the `check-wiring self-test` suite, derived from S1's hook list rather than
  hand-written per hook: a planted divergence prints the line for that hook, a matching pair does
  not, an untracked hook prints `skip`, and **`--check` exits 0 in every one of those states.**

## 3. Non-goals (OUT)

- **REDDING on a divergence.** Resolved in §8. The short form: the divergence is a STRUCTURAL and
  legitimate state of this layout, so a red would be bypassed rather than fixed — and
  `.unattended.conf:38` makes `bash tools/check-wiring.sh --check` an unattended run's precondition,
  so a red here refuses every unattended run whenever a sibling checkout moved.
- **A refusal in `.githooks/pre-push` itself.** That is where the check would actually BIND, and it
  is the right follow-up: the boundary that runs is the boundary that should assert it is the right
  one. Out of scope here because it changes what the push boundary REFUSES, and because a hook can
  only assert this once the version carrying the assertion is the one the primary tree holds.
  Backlog row, filed at fold time.
- **Changing `core.hooksPath` to a per-worktree value.** git offers no such thing;
  `core.hooksPath` is repo-global by design. This is the constraint, not a bug to route around.
- **Auto-fixing.** `--fix` sets an UNSET `core.hooksPath` and never clobbers a set one, deliberately.
  A divergence is not something to fix by rewriting another worktree's checkout.

## 4. Design

### The measurement this unit is grounded on

Taken on node `a`, 2026-09-04, in this worktree:

```
core.hooksPath            C:\projects\coding-governance\.githooks
resolved pre-push blob    ebf290c815c76ba1c710f32709218b05da4735c3
HEAD:.githooks/pre-push   ebf290c815c76ba1c710f32709218b05da4735c3
primary tree branch       main
```

They MATCH right now, because the primary tree happens to be on `main` and this branch has not
touched `.githooks/`. That is the condition, and it is not stable: `TOOL-dUnstalledConvoy-26`'s
landing ran with the primary tree on `contrib/incms-memory-recall`, so the push used that branch's
`pre-push` — no gate-env sourcing, no predicate 8, and the boundary's new coverage check simply
absent. Nothing wrong shipped, because a separate full bar had verified the pushed tree; the
BOUNDARY was not the one that shipped.

That measurement is why the check is worth having and why it must not gate: the two hashes agreeing
today is luck about which branch another checkout is parked on.

### The severity vocabulary, and why it decides this unit

`tools/check-wiring.sh` already has three severities and only one of them gates. `ok` and `note`
print and pass; `UNWIRED` increments `unwired`, which line 809 turns into the exit code. The script
already uses `note` for a condition that is TRUE, worth printing, and not dormant wiring — the EOL
notes are the shipped example. A hooks divergence is exactly that shape, so this unit reaches for
`note` and the rest of §8's reasoning follows.

### Data model

| Value | How |
|---|---|
| tracked? | `git ls-files --error-unmatch .githooks/<hook>` |
| resolved blob | `git hash-object "$curdir/<hook>"` |
| tracked blob | `git rev-parse HEAD:.githooks/<hook>` |
| the other checkout's branch | `git -C "$(dirname "$curdir")" rev-parse --abbrev-ref HEAD` |

The last is best-effort: the hooks dir's parent is not guaranteed to be a work tree, so an empty
answer prints as unknown rather than aborting the arm. A probe that cannot answer says so.

### Liveness, bounded by S3

An UNREADABLE side is reported and is never printed as `ok`. But "unreadable" is bounded to a hook
the tree TRACKS: an untracked hook is S3's `skip`, which is a different fact and gets a different
word. Rev-1 conflated them and would have given any adopter with no tracked pre-push a permanent
finding with no action available to clear it. Under S2 that is no longer a red either way, but a
permanent unclearable NOTE is still noise, and noise is how a report stops being read.

`MSYS mangles rev:dotpath` is a recorded trap on this node: `git rev-parse "<rev>:.githooks/x"` can
report ABSENT under a POSIX-emulation shell. `git ls-tree <rev> -- <path>` is the spelling that
works, and the build pass verifies which of the two this environment answers correctly before
trusting either.

### Files touched (estimate)

- `tools/check-wiring.sh` — check H.
- `.githooks/pre-push` — the header comment of S4.
- `memory/gotchas/hookspath-resolves-into-another-checkout.md` — S5.
- The `check-wiring self-test` suite — the arms of S6.

### Alternatives rejected

Recorded in §8, which is where the fork and its vetoes are.

## 5. Production-readiness checklist

- security — the subject IS a security-adjacent control: which gate runs at the boundary. The change
  reads and reports; it writes nothing and refuses nothing.
- perf / scale — two hash reads per hook per invocation.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — S3's `skip` is the absent state and it announces itself, which is
  the charter's §7 rule rather than a courtesy.
- observability — this unit IS the observability fix, and §4's liveness paragraph is what stops it
  becoming a reassuring zero.
- risks — the honest limit, and the gate's own header will carry it per the charter's rule that a
  gate states what it does NOT check: this reports a divergence, it does not prevent one, and a push
  made in the window between the report and the push still runs the other checkout's hook. That
  window is why `memory/gotchas/hookspath-resolves-into-another-checkout.md` keeps its
  landing-boundary documented check after S5's refresh rather than losing it.
- testing + left-shift gates — S6's arms, derived from the hook list. The class is
  `memory/gotchas/hookspath-resolves-into-another-checkout.md`, and this row is its live instance.
  A second class is left-shifted too: an arm planting one instance of each non-`UNWIRED` severity
  and asserting `--check` exits 0, so any future check reaching for `UNWIRED` when it means `note`
  reds.
- migration / rollback — none.
- user docs — the `AGENTS.md` merge-bar section describes the push boundary and states the active
  hooks are the tracked dir "so there is no staleness-drift class here". That sentence is the same
  claim S4 corrects in the hook's own header, and it is checked and corrected at fold time if it
  still reads that way.

## 6. Acceptance criteria

- **AC1** — When `core.hooksPath` resolves to a checkout whose `pre-push` differs from
  `HEAD:.githooks/pre-push`, `bash tools/check-wiring.sh` prints a `note`-severity line naming both
  hashes and the resolved path.
- **AC2** — When that same planted divergence is present, `bash tools/check-wiring.sh --check`
  **exits 0**. This is B1's criterion and the one that distinguishes the resolved option from the
  vetoed one; without it the unit ships Option B under Option A's name.
- **AC3** — The AC1 pair repeated for `pre-commit`: a planted `<hooksPath>/pre-commit` divergence
  prints its own `note` line naming both hashes, and `--check` still exits 0.
- **AC4** — When the two agree, `bash tools/check-wiring.sh` prints the existing `ok hooks` line and
  no divergence line for that hook. The negative arm; without it the check could print on every run.
- **AC5** — When `.githooks/pre-push` is not tracked in the current tree,
  `bash tools/check-wiring.sh` prints a `skip` line naming it, does not compare, and `--check` exits
  0. This is S3, and the fixture is a repo tracking a `pre-commit` and no `pre-push`.
- **AC6** — When the resolved hook exists but its blob cannot be read for a hook the tree DOES
  track, the output says UNKNOWN and never `ok`.
- **AC7** — When `.githooks/pre-push` is read, its header no longer claims there is no staleness
  class for this repo, and names the multi-worktree condition instead.
- **AC8** — When `memory/gotchas/hookspath-resolves-into-another-checkout.md` is read, NO paragraph
  of it asserts the comparison is unwritten or unopened, and it names the decision taken and the
  check written. The criterion is the WHOLE FILE, not one heading — rev-2 scoped it to "Its gate"
  and left the same false assertion standing under "What to do" at `:59-62`.
- **AC9** — When `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` runs, the
  `check-wiring self-test` leg is green with the new arms counted.

## 7. Gates

`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` for the `check-wiring self-test` leg, which is
`subject = kit` in `tools/gate-legs.json` and is therefore held as `ondemand` by
`tools/run-gates/run-gates.sh:947` on the plain bar — a guard scopes a run, it does not decide
whether a held leg runs at all. `AGENTS.md` records that no boundary sets `GATE_SELFTESTS` (owner,
2026-08-27) and that a DoD owes the full pair for KIT work, which this is. The plain
`bash tools/run-gates/run-gates.sh` still covers the repo-subject legs.


**The FULL PAIR, not half of it.** `AGENTS.md:488` spells the DoD command for KIT work as
`GATE_FULL=1 GATE_SELFTESTS=1`; `GATE_SELFTESTS=1` alone lifts the `ondemand` hold but leaves every
per-leg GUARD in force, so kit legs outside the touched directory stay held with no `skipped` line
saying which. Rev-2 cited the pair and prescribed one half of it.
## 8. Open questions

- **F1 · Does a divergence RED, or report?** The row that opens this unit states the decision is
  needed first and does not make it. Three options were considered.

  **Option A, report.** A `note`-severity line in check H, printed and not counted, so the exit code
  is untouched.

  **Option B, red.** A divergence fails the wiring gate leg, so the bar refuses until the operator
  changes what another checkout has checked out.

  **Option C, report at SessionStart and red at the push boundary.** Needs a refusal inside
  `.githooks/pre-push`, which is a wider change than the row asks for and cannot assert anything
  until the asserting version is the one the primary tree holds.

  RESOLVED (agent, 2026-09-04, delegated): **Option A**. The measurement in §4 is what decides it.
  A primary tree parked on a feature branch is a NORMAL state of this layout — it is the state the
  charter's own §3 spends rules on — and the divergence it produces is therefore structural, not a
  misconfiguration. A gate that reds on a structural condition is a gate that is bypassed, and this
  repo's own charter says a check nobody can afford to run is a check nobody runs. Option B also
  fails M3's veto 1 in spirit: it would red a tree whose only fault is that a SIBLING checkout
  moved, which no action in this tree can fix. Option C is strictly more feature-rich than A and is
  not vetoed, but it is a change to what the push boundary REFUSES, which is scope the row did not
  open; it is recorded as the follow-up in §3 rather than taken silently here.

  **The resolution STANDS at rev-2, and its SCOPING was wrong at rev-1.** The spec-audit's B1 found
  that rev-1 implemented Option A with an `UNWIRED`-class line, and `unwired` is exactly what
  `tools/check-wiring.sh:809` turns into the exit code — so rev-1 shipped Option B's behaviour under
  Option A's name, and would have refused every unattended run through `.unattended.conf:38`'s
  `WIRING_CHECK` whenever a sibling checkout moved. The pick is unchanged; S2 now names the
  non-gating `note` severity and AC2 observes the exit code. This is recorded rather than quietly
  corrected because a fork whose implementation contradicts its resolution is not a resolved fork.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, with F1 resolved before any code per the build method's fork
  rule. The two blob hashes in §4 were measured in this worktree at authoring time.
- rev-2 · 2026-09-04 · folded spec-audit round 1 (B1, H5, H7, H12, M1). **B1, blocker:** rev-1's
  Option A used an `UNWIRED` line, which IS the exit code at `:809`, so it delivered the behaviour
  §8 vetoed Option B for and would have blocked every unattended run via `WIRING_CHECK`. S2 now
  pins the non-gating `note` severity and AC2 observes it. **H5:** rev-1 scoped `pre-commit` in S3
  and observed only `pre-push` in every criterion; S1 is now written over a hook LIST and AC3
  covers the second hook. **H12:** rev-1 counted an absent pre-push as UNKNOWN with no bound,
  giving any adopter with no tracked pre-push a permanent unclearable finding; S3 and AC5 add the
  tracked-ness guard and the announced skip. **H7:** §7 named the plain bar for a `subject = kit`
  leg that `run-gates.sh:947` holds; it now names `GATE_SELFTESTS=1` and drops the guard-based
  reasoning, which was the wrong mechanism. **M1:** S5 adds the gotcha-record refresh, which rev-1
  left asserting that this very check was unwritten.

- rev-3 · 2026-09-04 · folded spec-audit round 2 (M9, M10). The loop exited NON-CONVERGENT at round
  2, so this is the disposing fold and there is no round 3. **M9:** rev-2's S5 and AC8 scoped the
  gotcha refresh to the record's "Its gate" heading, while the same false assertion — that this gate
  "is possible and is not written" — also stands under "What to do" at `:59-62`. A build satisfying
  AC8 whole would have left the cited class record still saying the thing just built does not exist,
  which is the exact defect S5 exists to remove. Both are now written over the file's carriers rather
  than one heading. **M10:** §7 cited `AGENTS.md`'s full pair and prescribed half of it.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "wiring check resolves the git hooks path and grades what
it finds"` was run and did NOT name the seam — it ranked `resolve` in `recall_conf.py` and `check`
in `test_recall_floor.py`, which match on name stem rather than on behaviour. The miss is recorded
rather than retried with softer words: a probe exits 0 on a miss and that is an answer.

The seam is check H of `tools/check-wiring.sh` at line 188, which already resolves `core.hooksPath`
through its own `abspath` helper and already owns the `ok` / `note` / `UNWIRED` / `FIXED` severity
vocabulary and the `unwired` tally. This unit extends that arm and reuses the `note` severity the
script's EOL arms already ship; no new check, no new output format, no new file. The class record
`memory/gotchas/hookspath-resolves-into-another-checkout.md` already exists and is what the row
points at. It was found by grepping `hooksPath` across `tools/` after the recall probe returned the
row.

Recall terms used: `--terms "agent-cap blankLiterals capFindings fanoutFindings landed phase check34
lander marker unrepairable govkit renormalize memory-tree conf"`
