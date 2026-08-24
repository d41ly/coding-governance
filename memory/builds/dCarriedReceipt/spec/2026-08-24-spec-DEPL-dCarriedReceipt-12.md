# DEPL-dCarriedReceipt-12 — write preconditions and a lock, on both writing verbs

**Status:** SPECCED · rev-1 · 2026-08-24 · node d · Tier-2 · base 9ddcc5c9 · streams deployer · ratified 2026-08-24

## 1. Goal

`cmd_update` has no in-progress-operation guard of any kind, and `cmd_apply`'s guard is dead in the
worktree layout adopters are told to use. `update --write` against a path carrying a live `UU`
collapses three index stages to zero through its own `git add` (`:3103`), and both sides of the
operator's merge become unrecoverable. Nothing else in this build may gain a write path until a
write refuses to run on a tree that is mid-operation.

## 2. Scope (IN)

- **S1** — replace the `target/.git/<marker>` path stat at `:2334` with `git rev-parse --git-path
  <marker>`, the form already used at `:2019`, so the probe resolves in a linked worktree where
  `.git` is a file.
- **S2** — apply that probe **unconditionally** in both `cmd_apply` and `cmd_update`. Today it sits
  inside `if pins:`, so a target declaring no `lf_pin` is unguarded even where the path form works.
- **S3** — refuse on `git ls-files -u` returning any row (an unresolved merge in the index).
- **S4** — refuse when any path the receipt claims is dirty in the target's worktree or index,
  naming the paths. A dirty file outside the receipt's population does not block.
- **S5** — an `O_EXCL` lock at `.governance/outbox/.update.lock`, taken by both writing verbs,
  released on every exit path including refusal, and carrying the pid and start time so a stale lock
  is diagnosable rather than mysterious.
- **S6** — every refusal names the condition, the marker or path that tripped it, and what to do.

## 3. Non-goals (OUT)

- **Not** auto-resolving, stashing, or aborting anything in the target. A deployer that tidies the
  operator's tree is a deployer that loses work; refuse and say why.
- **Not** a `--force` escape. Deliberate: the whole point is that the muscle-memory invocation must
  not be the destructive one, and a flag reachable in a hurry is not a guard.
- **Not** journal/resume for a crash mid-write; that is parked on the build's cut list and reuses
  `apply --resume`'s existing mechanism when it lands.

## 4. Design

### Data model

No receipt change. The lock is a file, not a field.

### Migration

None. Both verbs gain refusals only; a clean target behaves exactly as today.

### Alternatives rejected

- *Keep the path stat and special-case a worktree.* A second way to answer "where is the git dir"
  is a second answer that drifts. `--git-path` already exists in this file and is correct for every
  layout, including submodules — which matters, because NicoCares is one.
- *Guard only `update`.* `apply` writes `.gitattributes` and lands bytes; it has the same exposure
  and already ships a guard that merely does not work.
- *Advisory warning instead of refusal.* A warning printed above a successful-looking write is what
  the operator will not read.

### Files touched (estimate)

`tools/govkit/govkit.py` (~45 lines), `tools/govkit/selftest.py` (5 arms), one fixture that builds
a linked worktree.

## 5. Production-readiness checklist

- security — the dirty-path refusal closes a real exposure: a write onto an unstaged local edit is
  indistinguishable afterwards from an edit the operator made.
- perf / scale — one `rev-parse` and one `ls-files -u` per run; negligible against the blob reads
  already performed.
- a11y — N/A: CLI.
- i18n — N/A.
- error / empty / loading states — a stale lock prints its recorded pid and age and the command to
  clear it, rather than an unexplained refusal.
- observability — every refusal names its condition; the lock file records who holds it.
- risks — the residual risk is a target mutated by another process between the precondition check
  and the write. The lock covers govkit-vs-govkit; it does not cover govkit-vs-human, and this spec
  does not claim otherwise.
- testing + left-shift gates — five arms, each observed RED before the fix. The linked-worktree arm
  is the one that matters and is the one no existing fixture covers, which is why the defect shipped.
- migration / rollback — none; revertible as a pure addition of refusals.
- user docs — `WIRE-INTO-PROJECT.md` gains the precondition list beside the update step.

## 6. Acceptance criteria

- **AC1** — With `MERGE_HEAD` present in a **linked worktree** target, both `govkit.py apply` and
  `govkit.py update --write` refuse by name. Observe RED first: at `9ddcc5c9` both proceed, because
  `.git` is a file there and the path stat cannot fire.
- **AC2** — With `MERGE_HEAD` present in a normal (non-linked) target that declares **no** `lf_pin`,
  `apply` refuses. Observe RED first: today the probe sits inside `if pins:`.
- **AC3** — With an unresolved path in the index (`git ls-files -u` non-empty), `update --write`
  refuses and the index still shows three stages afterwards (`git ls-files -u | wc -l` unchanged).
- **AC4** — With one receipt-claimed path dirty, `update --write` refuses and names that path; with
  a dirty path **outside** the receipt population, it proceeds.
- **AC5** — Two concurrent `update --write` runs against one target: the second refuses on the lock
  and the first completes; after both, `.governance/outbox/.update.lock` is absent.
- **AC6** — A refusal path also releases the lock: after AC3's refusal, `.update.lock` is absent.

## 7. Gates

`bash tools/run-gates/run-gates.sh` full bar; specifically the `govkit selftest` leg, plus
`tools/govkit/refusal_join.py` — this unit adds six refusal branches and every one needs an arm
asserting it, which is the join's declared contract.

## 8. Open questions

- **F1 — should the dirty-path refusal cover the whole target or only receipt-claimed paths?**
  Receipt-claimed only. A deployer refusing over an unrelated edit in a repo it does not own is a
  deployer people learn to work around.
  RESOLVED (agent, 2026-08-24, delegated): receipt-claimed only, under the full-scope approval.
- **F2 — lock scope: per target, or per (target, verb)?** Per target. `apply` and `update` both
  write the receipt, so letting them interleave is the case the lock exists for.
  RESOLVED (agent, 2026-08-24, delegated): per target.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, from the kit-sync design pass (5 lenses + fold); the dead-guard
  mechanism verified in source against `9ddcc5c9` and reproduced in a live linked worktree.

## 10. Reuse audit

Reuses the `git rev-parse --git-path` form already present at `govkit.py:2019` rather than adding a
second git-dir resolver — the duplicate-answer defect this file's own comments name elsewhere. The
refusal shape reuses the existing `Refusal` class and its message discipline, and the new branches
are counted by the existing `refusal_join.py` contract rather than a new counter. No new seam: both
verbs already have a preamble where preconditions belong, and `cmd_apply` already demands
cleanliness in one place — this unit generalises that call site instead of adding one.
