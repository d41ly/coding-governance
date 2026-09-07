# TOOL-aPooledSweep-3 — pool safety is observed, not assumed

**Status:** OPEN · rev-1 · 2026-09-07 · node a · Tier-2 · base 05fb897c · streams tooling · order 3

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Running 59 suites together is sound only if each confines its writes to its own scratch. Give every
pooled suite a private scratch root, and OBSERVE that the sweep left the repository unchanged —
rather than asserting that suites are hermetic because they call `mktemp -d`.

## 2. Scope (IN)

- **S1** — each pooled suite runs with its own `TMPDIR`, so every `mktemp -d` inside it lands in a
  tree no sibling can reach. Observed by AC1.
- **S2** — the sweep FINGERPRINTS the repository before and after the whole run and REDS on a
  difference, naming what changed. The fingerprint covers the tracked working tree and the git
  common dir, which are the two places a suite writing outside its scratch would land. Observed by
  AC2.
- **S3** — the fingerprint has a LIVENESS assertion: a fingerprint that could not be taken REFUSES,
  and says the sweep is ungraded rather than reporting a clean tree. Observed by AC3.
- **S4** — the refusal names the sweep as UNSOUND rather than naming a suite. A whole-run
  fingerprint cannot attribute, and it says so instead of guessing. Observed by AC2.

## 3. Non-goals (OUT)

- Not attributing a dirty tree to the suite that dirtied it. A per-suite fingerprint under a pool is
  a read racing 58 writers. The serial mode is the attribution tool, and the refusal names it as the
  next step.
- Not declaring a per-suite pool-safety column in `tools/run-gates/selftest-budgets.txt`. Nothing has
  been observed to need one, and adding a middle column to a tab-read file is the
  `empty-field-collapses-unless-it-is-last` class the checklist selects for this exact path.
- Not sandboxing a suite. A private `TMPDIR` is a redirection, not a jail, and this spec claims no
  more than that.
- Not fingerprinting untracked files. A suite legitimately leaving an untracked artifact in the tree
  is not the failure this observes, and `.gitignore`d build output would red every run.

### Edges

- **consumes-from** `TOOL-aPooledSweep-1` — the pooled mode. Without it there is nothing to make
  safe, and the fingerprint would grade a serial run that was never in doubt.
- **hands-off** external — attribution of a dirty tree to one suite, which needs a serial re-run and
  is the remedy the refusal names.

## 4. Design

### The private scratch

One `mktemp -d` for the sweep, one subdirectory per pool slot, `TMPDIR` exported into each suite
process. Every suite in this population creates its own scratch with `mktemp -d` or a Python
equivalent, and both honour `TMPDIR`, so the redirection reaches them without any suite being edited.
Five suites in the population create no scratch of their own; four of those run on
`tools/lib/lib-selftest.sh`, which calls `mktemp -d` itself and is therefore redirected identically.

### The fingerprint

Two reads, before and after the whole sweep:

- `git status --porcelain` over TRACKED paths — a suite that wrote into the checkout.
- a listing of `git rev-parse --git-common-dir` at one level, names and sizes — a suite that wrote
  into the repository's own metadata, which is where the runner's ledger, its logs and the lander
  marker live.

Equal before and after is the pass. Different is a RED naming the differing entries.

**The liveness assertion is the load-bearing half.** A fingerprint that returns an empty string
because the command failed is indistinguishable from a clean tree, which is the exact
green-by-absence shape this repo gates in a dozen places. So the BEFORE fingerprint must be
non-empty in at least its git-common-dir arm — a git dir with no entries is not a state that exists
— and an empty one REFUSES before a single suite starts.

### Why a whole-run fingerprint and not a per-suite one

Per-suite is what a reader wants and it cannot be had here. Under a pool, reading the tree after
suite `k` observes whatever suites `k+1..n` have done by then, so a per-suite verdict would be
attributed at random. The honest instrument is the one that answers a question it can answer: did
this sweep dirty the repository. The answer is actionable — a red sends the operator to the serial
mode, which CAN attribute — and it is never wrong about the thing it claims.

### Inventory

- `_rs_fingerprint` — the function taking one reading. One implementation, two call sites, because
  a before-reader and an after-reader written separately are two answers to one question.
- `SWEEP_TMPROOT` — the sweep's scratch root, removed on exit.

### Files touched (estimate)

`tools/run-gates/run-selftests.sh` · `tools/run-gates/run-selftests.test.sh` · one build record.

### Alternatives rejected

**Declaring pool safety per suite in the budgets file.** Rejected on two counts. It is a survey of 59
suites to produce a claim nobody can falsify without running them anyway, and it adds a middle column
to a `IFS=$'\t' read -r` reader where an empty field collapses and silently shifts every field after
it — a defect this repo has already recorded as a gotcha class and which the checklist selected for
this path.

**Comparing each suite's own scratch usage.** Rejected: a suite confined to `TMPDIR` is the case that
needs no observation, and one escaping it does not do so through its scratch.

## 5. Production-readiness checklist

- security — N/A: the fingerprint reads, it does not write, and the private `TMPDIR` narrows rather
  than widens what a suite can reach.
- perf / scale — two `git status` reads and two directory listings per sweep, not per suite.
- error / empty / loading states — an unreadable fingerprint is the refusal S3 names, not an empty
  one.
- observability — the differing entries are printed. A clean sweep says the fingerprint matched,
  rather than saying nothing.
- risks — the recorded risk is that the after-fingerprint runs while a suite's own cleanup is still
  in flight, reporting a difference that resolves a moment later. The pool is drained before the
  reading is taken, which is what makes it a whole-run instrument rather than a sampling one.
- testing — arms staging a suite that writes into the checkout, and one staging an unreadable
  fingerprint.
- migration — additive and confined to the new mode.
- user docs — `print_usage` names the fingerprint as part of what `--sweep` asserts.

## 6. Acceptance criteria

- **AC1** — When a pooled fixture suite calls `mktemp -d`, the directory it receives is under the
  sweep's own scratch root and not under the ambient `TMPDIR`. Red when: a suite's scratch lands
  outside the sweep root, so two suites could collide on a shared parent.
- **AC2** — When a fixture suite deliberately writes into a tracked file in the checkout, `--sweep`
  REDS after the pool drains, names that path, and states that the sweep is unsound without naming
  a culprit suite. Red when: the sweep exits 0 over a dirtied tree, or names a suite it cannot have
  attributed.
- **AC3** — When the fingerprint command is made to fail, `--sweep` REFUSES before running any suite
  and says the sweep is ungraded. Red when: a failed fingerprint reads as a clean one and the sweep
  proceeds.
  fixture: the arm forces the failure through a stubbed `git` on `PATH`, not by deleting the git dir.
- **AC4** — When `--sweep` completes over an undirtied tree, it states that the fingerprint matched.
  Red when: a clean sweep is silent about the fingerprint, so a run where the check never fired is
  indistinguishable from one where it passed.

## 7. Gates

`run-selftests self-test` · `memory hygiene` · `lexicon naming predicates`

New arm: `tools/run-gates/run-selftests.test.sh` · a fixture suite that writes into a tracked path,
and a stubbed `git` that makes the fingerprint fail · the suite's assertion floor moves by the
number of arms added.

## 8. Open questions

- **F1 — does the fingerprint cover untracked files in the checkout?** RESOLVED (agent, 2026-09-07,
  delegated): no. `git status --porcelain` over tracked paths only. A suite legitimately leaving an
  untracked artifact is not the failure this observes, and including untracked paths would red every
  sweep on ordinary build output — M3's veto 1, since it would fail this unit's own AC4.

## 9. Revision log

- rev-1 · 2026-09-07 · initial draft.

## 10. Reuse audit

No existing seam fits: nothing in `tools/run-gates/` fingerprints the repository around a run.
`tools/run-gates/gate-fingerprint.sh` is the nearest name and was read at source — it fingerprints
the TREE THAT A RECORDED GREEN NAMES, so the pre-push hook can tell whether a stamp still reproduces
at the sha it claims. That is a different question from "did this run dirty anything", it takes no
before-and-after pair, and reusing it would mean bending a push-boundary instrument into a
concurrency instrument. The private-`TMPDIR` half extends the scratch discipline
`tools/lib/lib-selftest.sh` already applies one level down, at the arm rather than at the suite.

Recall terms used: `python tools/memory-recall/query.py "why could the costly self-test suites not be
ported onto the parallel harness, and what would make them portable" --terms "selftest harness port
arm inventory extract negative assertion substring snapshot shard parallel budget majority share
spawn"`.
