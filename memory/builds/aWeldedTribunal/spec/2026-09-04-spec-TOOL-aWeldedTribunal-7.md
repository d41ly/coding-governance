# TOOL-aWeldedTribunal-7 — the wiring check names the pre-push that will actually run

**Status:** OPEN · rev-1 · 2026-09-04 · node a · Tier-2 · base 9b5ae688 · streams tooling · order 7 · ratified 2026-09-04

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`core.hooksPath` is repo-global and absolute, so in this multi-worktree layout the hook that gates a
push comes from whatever the PRIMARY tree has checked out — not from the tree being pushed. Check H
of `tools/check-wiring.sh` already resolves that path and asserts only that a `pre-commit` file
exists there. Make it also compare the resolved `pre-push` against the blob the pushed tree tracks,
and say so when they differ.

## 2. Scope (IN)

- **S1** — Check H additionally hashes the resolved `<hooksPath>/pre-push` and compares it against
  `HEAD:.githooks/pre-push` in the CURRENT tree.
- **S2** — A divergence prints an `UNWIRED`-class line naming both hashes, the resolved path, and
  the branch the hook's own checkout is on, so the operator can tell WHICH other checkout supplied
  it. A line saying only "mismatch" sends the reader to derive the rest.
- **S3** — The same comparison for `pre-commit`, because check H already resolves that file and the
  branch guard lives in it. One arm covering one of two hooks certifies coverage it does not have.
- **S4** — `.githooks/pre-push`'s header comment is corrected. It currently reads that the active
  hook is the tracked dir "so tracked == active by construction — no staleness class for THIS
  repo", which the measurement in §4 falsifies for exactly this layout. A stale claim beside the
  mechanism it describes is the `two-answers-to-one-question` class.
- **S5** — Arms in the `check-wiring self-test` leg in both directions: a planted divergence must
  produce the line, and a matching pair must not.

## 3. Non-goals (OUT)

- **REDDING on a divergence.** Resolved in §8; the reasoning is there and the short form is that the
  divergence is a STRUCTURAL and legitimate state of this layout, so a red would be bypassed rather
  than fixed.
- **A refusal in `.githooks/pre-push` itself.** That is where the check would actually BIND, and it
  is the right follow-up: the boundary that runs is the boundary that should assert it is the right
  one. It is out of scope here because it changes what the push boundary REFUSES, which is a wider
  decision than the row asked for, and because a hook can only assert this once the version carrying
  the assertion is the one the primary tree has checked out. Backlog row, filed at fold time.
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

That measurement is why the check is worth having and why it must not red: the two hashes agreeing
today is luck about which branch another checkout is parked on.

### Data model

Check H gains, after its existing `pre-commit` existence arm:

| Value | How |
|---|---|
| resolved blob | `git hash-object "$curdir/pre-push"` |
| tracked blob | `git rev-parse HEAD:.githooks/pre-push` |
| the other checkout's branch | `git -C "$(dirname "$curdir")" rev-parse --abbrev-ref HEAD` |

The third is best-effort: the hooks dir's parent is not guaranteed to be a work tree, so an empty
answer prints as unknown rather than aborting the arm. A probe that cannot answer says so.

### Liveness

Both `git hash-object` and `git rev-parse HEAD:<path>` can fail — an absent file, a tree with no
such path. Neither failure may print `ok`. An unreadable side is reported as UNKNOWN and counted the
same as a divergence, because a comparison that could not run is not a comparison that passed.
`MSYS mangles rev:dotpath` is a recorded trap on this node: `git rev-parse "<rev>:.githooks/x"` can
report ABSENT under a POSIX-emulation shell. `git ls-tree <rev> -- <path>` is the spelling that
works, and the build pass verifies which of the two this environment answers correctly before
trusting either.

### Files touched (estimate)

- `tools/check-wiring.sh` — check H.
- `.githooks/pre-push` — the header comment of S4.
- The `check-wiring self-test` suite — the arms of S5.

### Alternatives rejected

Recorded in §8, which is where the fork and its vetoes are.

## 5. Production-readiness checklist

- security — the subject IS a security-adjacent control: which gate runs at the push boundary. The
  change reads and reports; it writes nothing and refuses nothing.
- perf / scale — two hash reads per session-start invocation.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — the UNKNOWN arm above is the empty state and it is loud.
- observability — this unit IS the observability fix, and §4's liveness paragraph is what stops it
  becoming a reassuring zero.
- risks — the honest limit, and the gate's own header will carry it per the charter's rule that a
  gate states what it does NOT check: this reports a divergence, it does not prevent one, and a
  push made in the window between the report and the push still runs the other checkout's hook.
- testing + left-shift gates — S5's arms. The class is
  `memory/gotchas/hookspath-resolves-into-another-checkout.md`, which the checklist selects for this
  file and which this row is the live instance of.
- migration / rollback — none.
- user docs — the `AGENTS.md` merge-bar section describes the push boundary and states the active
  hooks are the tracked dir "so there is no staleness-drift class here". That sentence is the same
  claim S4 corrects in the hook's own header, and it is checked and corrected at fold time if it
  still reads that way.

## 6. Acceptance criteria

- **AC1** — When `core.hooksPath` resolves to a checkout whose `pre-push` differs from
  `HEAD:.githooks/pre-push`, `bash tools/check-wiring.sh` prints an `UNWIRED` line naming both
  hashes and the resolved path.
- **AC2** — When the two agree, `bash tools/check-wiring.sh` prints the existing `ok hooks` line and
  no divergence line. The negative arm; without it the check could print on every run.
- **AC3** — When the resolved `pre-push` is absent or the tracked blob cannot be read, the output
  says UNKNOWN and is counted as unwired, never as `ok`.
- **AC4** — When `bash tools/check-wiring.sh --session` runs in this worktree today, it exits with
  the same status it does now, because the two blobs currently match. The change is a no-op on a
  clean tree, which is what makes AC1's planted divergence the real evidence.
- **AC5** — When `.githooks/pre-push` is read, its header no longer claims there is no staleness
  class for this repo, and names the multi-worktree condition instead.
- **AC6** — When the `check-wiring self-test` leg runs under `bash tools/run-gates/run-gates.sh`,
  it is green and its new arms are counted.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — the `check-wiring self-test` leg named in
`tools/gate-legs.json`. It is guarded on this kit, so it runs on this diff.

## 8. Open questions

- **F1 · Does a divergence RED, or report?** The row that opens this unit states the decision is
  needed first and does not make it. Three options were considered.

  **Option A, report.** A line in check H, counted as unwired, no exit-code change beyond the
  existing unwired tally.

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
  fails M3's veto 1 in spirit: it would red a tree whose only fault is that a SIBLING checkout moved,
  which no action in this tree can fix. Option C is strictly more feature-rich than A and is not
  vetoed, but it is a change to what the push boundary REFUSES, which is scope the row did not open;
  it is recorded as the follow-up in §3 rather than taken silently here.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, with F1 resolved before any code per the build method's fork
  rule. The two blob hashes in §4 were measured in this worktree at authoring time.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "wiring check resolves the git hooks path and grades what
it finds"` was run and did NOT name the seam — it ranked `resolve` in `recall_conf.py` and `check`
in `test_recall_floor.py`, which match on name stem rather than on behaviour. The miss is recorded
rather than retried with softer words: a probe exits 0 on a miss and that is an answer.

The seam is check H of `tools/check-wiring.sh` at line 188, which already resolves `core.hooksPath`
through its own `abspath` helper and already owns the `ok` / `UNWIRED` / `FIXED` line vocabulary and
the `unwired` tally. This unit extends that arm; no new check, no new output format, no new file.
The class record `memory/gotchas/hookspath-resolves-into-another-checkout.md` already exists and is
what the row points at. It was found by grepping `hooksPath` across `tools/` after the recall probe
returned the row.

Recall terms used: `--terms "agent-cap blankLiterals capFindings fanoutFindings landed phase check34
lander marker unrepairable govkit renormalize memory-tree conf"`
