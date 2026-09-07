# TOOL-aPooledSweep-3 — pool safety is observed, not assumed

**Status:** CLOSED · rev-3 · 2026-09-07 · node a · Tier-2 · base 05fb897c · streams tooling · order 3 · ratified 2026-09-07

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-07-build-TOOL-aPooledSweep-1-acceptance-ledger-and-the-measured-ab.md](../build/2026-09-07-build-TOOL-aPooledSweep-1-acceptance-ledger-and-the-measured-ab.md) | journal | TOOL-aPooledSweep-1 TOOL-aPooledSweep-2 |
| [2026-09-07-review-TOOL-aPooledSweep-1-2-3-spec-audit-round1.md](../reviews/2026-09-07-review-TOOL-aPooledSweep-1-2-3-spec-audit-round1.md) | spec-audit | TOOL-aPooledSweep-1 TOOL-aPooledSweep-2 |
| [2026-09-07-review-TOOL-aPooledSweep-1-2-3-spec-audit-round2.md](../reviews/2026-09-07-review-TOOL-aPooledSweep-1-2-3-spec-audit-round2.md) | spec-audit | TOOL-aPooledSweep-1 TOOL-aPooledSweep-2 |

<!-- /gen:spec-records -->

## 1. Goal

Running 59 suites together is sound only if each confines its writes to its own scratch. Give every
pooled suite a private scratch root, and OBSERVE that the sweep left the repository unchanged —
rather than asserting that suites are hermetic because they call `mktemp -d`.

## 2. Scope (IN)

- **S1** — each pooled suite runs with its own `TMPDIR`, so every `mktemp -d` inside it lands in a
  tree no sibling can reach. Observed by AC1.
- **S2** — the sweep FINGERPRINTS THE TRACKED WORKING TREE before and after the whole run and REDS
  on a difference, naming the paths that changed. One place, not two: §4 records why the git common
  dir was dropped. The BEFORE reading is taken before any suite starts, observed by AC7; the
  comparison is observed by AC2.
- **S3** — the fingerprint has a LIVENESS assertion: a fingerprint that could not be taken REFUSES,
  and says the sweep is ungraded rather than reporting a clean tree. Observed by AC3.
- **S4** — the refusal names the sweep as UNSOUND rather than naming a suite. A whole-run
  fingerprint cannot attribute, and it says so instead of guessing. Observed by AC2.
- **S5** — A POOLED RED NAMES ITS OWN DISAMBIGUATION. `TOOL-dSpentCeiling-8` measured two rows of
  this population — `run-gates turnstile` and `row-keyed merge driver replay` — redding under the
  bar's own concurrency and green standalone, with no tree change between runs. A sweep that reds
  therefore prints the serial re-run as the step that separates a broken mechanism from a busy box.
  Observed by AC5.

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
  is not the failure this observes. This is a FLAG and not a property of the command: plain
  `git status --porcelain` lists untracked paths with `??` and hides ignored ones, so the reading
  passes `--untracked-files=no` explicitly. Rev-2 resolved F1 against a default the command does not
  have.
- Not fingerprinting the git common dir. §4 records the reading that removed it; the residual gap —
  a suite writing into repository metadata — is observed by nothing here and is named rather than
  implied away.
- Not resolving a load-sensitive red. S5 makes the ambiguity actionable by naming the serial re-run;
  distinguishing a broken mechanism from a busy box is `TOOL-dSpentCeiling-8` and stays there.

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
The suites that create no scratch of their own run on `tools/lib/lib-selftest.sh`, which calls
`mktemp -d` itself and is therefore redirected identically. Derived over the tracked tree, THREE
suites source that harness at top level: `tools/check-line-length.test.sh`,
`tools/lib/extract-arms.test.sh` and `tools/run-gates/run-selftests.test.sh`. A grep for the
harness's filename returns five, because `tools/lib/lib-selftest.test.sh` tests it as a SUBJECT and
`tools/check-testsuite-counts.test.sh` only writes the spelling inside fixture strings.

### The fingerprint, and the arm that was dropped

One read, before and after the whole sweep: `git status --porcelain --untracked-files=no`. Equal is
the pass. Different is a RED naming the differing paths.

**The flag is load-bearing.** `--porcelain` alone reports untracked paths as `??` rows, so without
it every ordinary build artifact, editor swap file and freshly written record in the tree would flip
the reading between the two takes — and this build's own sweep would red on the review report it had
just written. `--untracked-files=no` is what makes the non-goal above true rather than assumed.

**Rev-1 had a second arm and it is DELETED rather than narrowed.** It listed the git common dir at
one level, on the reasoning that repository metadata is where an escaping suite would most likely
write. Listing that directory on this checkout says why it cannot be an instrument: it holds
`gate-bar-queue`, `gate-ledger.tsv`, `gate-logs`, `gate-run`, `gate-timings.tsv`,
`unattended-landed`, `index`, `logs`, `refs` and `ORIG_HEAD`, every one of them written by ordinary
tooling. `run-gates.sh` places `gate-bar-beacon` and `gate-bar-queue` there when a bar claims the
turnstile, the directory is SHARED by every worktree of the repository, and this repo's own
conventions assume concurrent sessions in sibling worktrees. The sweep's floor is the longest suite,
so the window between the two readings is tens of minutes wide: any sibling session running the bar
flips the listing, and S4 then forbids the refusal from naming a culprit. An operator would get an
unattributable RED for something the sweep did not do, and an instrument that reds on innocent runs
is ignored within two sightings.

The alternative was an exclusion list. Rejected below, and the residual gap is a declared non-goal
rather than a silence.

**The liveness assertion is the load-bearing half.** A fingerprint that returns an empty string
because the command failed is indistinguishable from a clean tree, which is the exact
green-by-absence shape this repo gates in a dozen places. `git status --porcelain` is EMPTY on a
clean tree, so emptiness cannot be the liveness test here: the assertion is that the command
SUCCEEDED, and a non-zero exit or an unresolvable repository REFUSES before a single suite starts.

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

**Keeping the git-common-dir arm behind an exclusion list.** Rejected: the list would have to name
eleven entries today, and it grows every time any kit writes a new file there — a list nobody
re-derives, guarding a signal that reds on innocent concurrent bars in the meantime. Deleting the
arm and declaring the gap is the honest half of the same trade.

## 5. Production-readiness checklist

- security — N/A: the fingerprint reads, it does not write, and the private `TMPDIR` narrows rather
  than widens what a suite can reach.
- perf / scale — two `git status` reads per sweep, not per suite. Rev-2 deleted the two directory
  listings this row used to price alongside them.
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
- **AC5** — When a fixture suite writes a file into the git common dir during a sweep, `--sweep`
  does NOT red. Red when: a git-dir write reds the sweep, which is the false positive §4 deleted
  that arm to avoid.
- **AC6** — When any suite in a sweep reds, the summary NAMES the serial re-run — the no-flag
  `bash tools/run-gates/run-selftests.sh` — as the disambiguation step. Red when: a red summary omits the re-run instruction, leaving an operator
  with a verdict that cannot separate a broken mechanism from a busy box.
- **AC7** — When the fingerprint's BEFORE reading is taken, `git status --porcelain
  --untracked-files=no` has run before the first suite starts: a fixture suite that dirties a
  tracked file is still reported, rather than being baked into the baseline. Red when: the before-reading is taken after the pool starts, which makes every
  suite's own writes invisible to the comparison and the whole check vacuous.

## 7. Gates

`run-selftests self-test` · `memory hygiene` · `lexicon naming predicates`

New arm: `tools/run-gates/run-selftests.test.sh` · a fixture suite that writes into a tracked path,
and a stubbed `git` that makes the fingerprint fail · the suite's assertion floor moves by the
number of arms added.
New arm: `tools/run-gates/run-selftests.test.sh` · a fixture suite that writes into the git common
dir, asserted NOT to red, paired with the tracked-path arm so the two pin both edges of the
predicate · same floor move.
New arm: `tools/run-gates/run-selftests.test.sh` · an untracked file created in the fixture tree
during a sweep, asserted NOT to red, and a suite whose write is ordered before the baseline would
be taken · same floor move.

## 8. Open questions

- **F1 — does the fingerprint cover untracked files in the checkout?** RESOLVED (agent, 2026-09-07,
  delegated): no, and it takes a FLAG to mean it. `git status --porcelain --untracked-files=no`.
  Rev-2 resolved this against a property `--porcelain` does not have: it lists untracked paths as
  `??` by default and hides ignored ones, so the unflagged form would have redded every sweep on
  ordinary build output — M3's veto 1, since it would fail this unit's own AC4.

## 9. Revision log

- rev-1 · 2026-09-07 · initial draft.
- rev-2 · 2026-09-07 · §2 S2, S5 · §3 · §4 · §6 AC5 · §7 · folded round-1 spec audit H2, H3, H4, H7.
  H2: the git-common-dir arm reds on any sibling session running the bar, so it is deleted and the
  gap declared, with AC5's negative arm pinning that it does not red. H4 dissolves with it — a
  one-armed predicate owes one staged break, which AC2 already is. H3: `TOOL-dSpentCeiling-8`
  measured two rows of this population redding under concurrency, so S5 makes a pooled red name its
  own serial re-run. H7: the inner-harness suite count was four and is three.
- rev-3 · 2026-09-07 · §2 S2 · §3 · §4 · §5 · §6 AC5, AC6, AC7 · §7 · §8 F1 · folded round-2 spec
  audit H5, H7, M3, M4. The loop exited NON-CONVERGENT at round 2, so every finding was disposed by
  FOLD. H5: S2 promised a before-and-after comparison and every criterion observed only the after,
  so AC7 pins when the baseline is taken. H7: `git status --porcelain` reports untracked paths, so
  the reading takes `--untracked-files=no` and F1 says so. M3: rev-2's AC5 conjoined a must-not-red
  fixture with an observation that only exists when something reds, so it splits into AC5 and AC6.
  M4: the readiness row still priced the two directory listings rev-2 deleted.

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
