# TOOL-aPacedTurnstile-6 — reuse a proven green, and scope a worktree to its own branch point

**Status:** OPEN · rev-2 · 2026-08-18 · node a · Tier-2 · base 6517579f · streams tooling

## 1. Goal

`TOOL-aPacedTurnstile-5` records what each leg proved and against which inputs. Consume it: skip a
leg whose inputs are byte-identical to a recorded green, which makes resume-from-a-failed-leg a
special case rather than a second mechanism, and fix the base a worktree scopes against so a branch
is graded on what it actually changed.

## 2. Scope (IN)

- **S1** — `GATE_REUSE`, default OFF. When set, a leg is skipped if it is not declared impure, its
  ledger row says ok, and the row's input key equals the one computed this run.
- **S2** — the per-leg input key: for a guarded leg, a digest over the joined argv, the resolved
  base, and the path-and-blob-hash list across its guard pathspecs; for an unguarded leg, the same
  but over the whole-tree fingerprint, because an unguarded leg declares that it reads everything.
- **S3** — a fourth report verb for a reused leg, padded to the same column as the existing three and
  following `TOOL-aPacedTurnstile-1`'s two-space tail contract.
- **S4** — a leg declaring `impure` never gets an input key and can never be reused. The key is
  DECLARED by `TOOL-aPacedTurnstile-5`, which owns the manifest's key set; this unit owns its VALUES,
  measured rather than guessed, and the structural arm in S8. Two units touching one key with no
  stated authority is how a manifest ends up with two provenances for one field.
- **S5** — the base becomes `git merge-base HEAD "origin/$DEFBR"`, replacing the origin tip, where
  the default branch is OBSERVED from the remote and never taken from a local ref. `GATE_BASE` still
  outranks everything; an unresolvable base still fails safe to running every leg; and a base that
  resolves EQUAL TO HEAD is refused and falls back to running everything, because on the default
  branch itself the merge-base is degenerate and would otherwise scope every leg away. That last
  clause is the `TOOL-cFinalBerth-2` class, and taking the merge-base against a local branch is how
  the form this unit adopts reaches it.
- **S6** — a canary arm for the case that actually distinguishes the two base semantics: a guard-
  unchanged leg on a DIVERGED branch skips against the merge-base where it would have run against
  the tip.
- **S7** — reuse arms in `tools/run-gates/run-gates.evidence.test.sh`: a reused leg prints the reuse
  verb, a changed input defeats reuse, an impure leg is never reused, a red leg is never reused, and
  reuse is off unless asked.
- **S8** — a structural canary arm: a leg whose own script directly calls out to the network must
  carry an `impure` declaration, with the gate's header stating plainly that it sees a direct call
  and not a call through a driver. The matcher is WRAPPER-AWARE, because the motivating files route
  their remote calls through a shell function rather than the bare command, and a matcher that only
  sees the bare spelling finds nothing in exactly the files that motivated it. It carries the
  anti-vacuity assertion the lexicon and playbook-parity gates already use: the scan over the real
  manifest must resolve the known network-calling legs BY NAME, and print `DEAD PROBE` and red when
  its match set is empty.

## 3. Non-goals (OUT)

- Writing the record. That is `TOOL-aPacedTurnstile-5`.
- The push boundary. `TOOL-aPacedTurnstile-7` owns it, and it reads the full-green file rather than
  the ledger.
- Turning reuse on by default. See the boundary rule; it is opt-in and this unit keeps it that way.
- A resume flag, a failed-leg list, or a state machine. Reuse subsumes them, which is the argument
  for this shape.
- Sharing the ledger across the eleven worktrees on this node. Sound and tempting, but it converts a
  single-writer file into a contended one exactly as `TOOL-aPacedTurnstile-4` is designing the lock.
  Revisit after that lands, with a measurement of how often a cross-worktree key matches.
- Widening or narrowing any leg's `guard`.

## 4. Design

### Soundness, stated exactly

**SOUND — the hash-keyed reuse.** A leg is skipped only because a run already executed this argv
against this exact worktree content at this base and recorded ok. Nothing is inferred about what the
leg reads. Contrast the `guard`, whose premise is that a human listed the leg's inputs correctly.
Two holes in that premise, both verified rather than asserted:

- **Untracked files are invisible to a guard.** `git diff --quiet BASE -- <path>` does not see
  untracked files. Verified in this worktree: the diff reported no change for a directory that held
  two untracked files at the time. A brand-new leg script or fixture, added but not yet staged, does
  not trip its own guard. The fingerprint closes this, because the porcelain status sees it.
- **Under-declaration is unchecked.** The canary checks only that a guard RESOLVES to a tracked
  path. Nothing checks that it names every input, and
  `memory/builds/cBriefedPilot/spec/2026-08-14-spec-cBriefedPilot-15.md` records a live instance.

The claim is not unconditional, and overclaiming it would repeat an error this repo has already
caught twice. NOT in the key: environment variables, git config, the wall clock, the machine, and
other processes on it. So the precise claim is **sound modulo declared purity and a stable
environment**, and the `impure` declaration is where that assumption is made visible instead of
silent.

**ADVISORY — the guard pathspecs, the impure list, and the timing-based dispatch order.** All three
are hand-written and all three stay.

**The boundary rule, which is this unit's actual contribution:** an advisory input may cause MORE
work on any path, and may cause LESS work only on an opt-in, non-authoritative run. That is why
reuse defaults off, and why the full-green file demands nothing was reused as well as nothing
skipped. A mis-declared impure leg can therefore cost a stale green on a developer's opt-in re-run;
it can never contaminate the one recorded fact the push boundary consumes.

**And the ceiling, so nobody sells this as a speedup it is not.** Whole-tree-keyed reuse buys resume
and a free repeat run. It buys approximately nothing at the push boundary, because a merge moves the
tree and every key with it. Diff-scoping still needs the guard, which is why
`TOOL-aPacedTurnstile-7` exists and why this unit does not pretend to replace it. What the guarded
key does add is a strictly better guard for the legs that have one: hashing the path-and-blob set
the guard names is exactly as sound as the guard while closing the untracked-file hole and getting
reverts and rebases right — a diff calls a file that changed and changed back "changed"; a hash
calls it the same.

### Resume is not a second mechanism

Re-run after a red with reuse on and nothing else. Every leg whose inputs still match its ok row is
reused; the failed leg has no reusable row; anything the fix touched has a new key. What runs is the
failed leg plus what changed. One rule, two behaviours — which is the reason to prefer this shape
over a purpose-built resume file.

### The base

Today the base is the origin TIP and the guard diffs it against the working tree. For a worktree
branch the right base is the branch point, for three independent reasons.

The guard's premise requires a GREEN base: "unchanged since BASE, so BASE's verdict carries" is only
an argument if BASE was proven green. Both candidates qualify, but the merge-base is the tree this
worktree actually descends from, so the carried verdict is about content this worktree holds. After
the default branch advances, files it changed and the worktree did not show as "changed", and the
legs run for a difference that is not the worktree's.

It makes reuse keys stable: a merge-base does not move when origin advances, only when HEAD merges
or rebases. Keying on the tip would invalidate every ledger row on every fetch.

And the bar already disagrees with itself — `tools/memory-tree/check-verdict-epoch.sh` derives its
own base as a merge-base. One bar, two notions of base; this is a one-line change that removes the
inconsistency.

Today's canary arm passes under EITHER semantics, because its fixture points the remote ref at HEAD
so the merge-base is the tip. The change would land untested, which is why S6 adds the diverged
case.

### Recursion and concurrency

Both harnesses spawn nested runners — one through scratch repos with their own git dir, the other
through an explicit git dir and manifest. Every record read is derived from the resolved git dir, so
a nested run reads the fixture's. No lock is introduced, so there is nothing to deadlock on.

One inherited-environment hazard is real and is handled by the default: the canary's scratch dir
persists across arms, so a ledger accumulates there. If reuse were on by default, the existing
width-1 against width-4 equivalence arm would compare a fresh run against a fully-reused one and
break. That is concrete evidence for the opt-in default rather than a hypothetical.

### Which legs are impure

Measured, then declared. The remote calls are verified in `tools/unattended/check-unattended.sh` and
`tools/unattended/unattended.sh`. Whether the three self-tests reach those paths or stub the remote
in their fixtures is NOT yet verified, so the build measures before declaring. Until measured,
declare all four — over-declaring costs nothing but reuse on legs that are most of the wall clock
anyway, and under-declaring is a wrong skip.

### Rollout

One commit after `TOOL-aPacedTurnstile-5`. Rollback is unsetting the feature, which is the default,
so the rollback state is the shipped state and every arm runs against it.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/run-gates/run-gates.sh` | the reuse decision in the existing serial pre-pass, the key, the verb, the base |
| `tools/run-gates/run-gates.test.sh` | S6's diverged-base arm, S8's structural arm |
| `tools/run-gates/run-gates.evidence.test.sh` | S7's reuse arms |
| `tools/gate-legs.json` | the measured `impure` values |

### Alternatives rejected

- **Reuse on by default.** Rejected: it would break the canary's equivalence arm, and it inverts the
  boundary rule by letting an advisory declaration reduce work on an authoritative run.
- **A dedicated resume file listing failed legs.** Rejected: a second mechanism for a case the key
  already covers, and it would need its own staleness rule.
- **Keying reuse on the guard's diff rather than a hash.** Rejected: inherits the untracked-file hole
  and mis-handles reverts.

## 5. Production-readiness checklist

- security — reuse reads only the record in the git dir; a hostile ledger can cause a wrong skip on
  an opt-in run, which is why the authoritative fact demands nothing was reused.
- perf / scale — one digest per leg over its guard paths, plus the one whole-tree fingerprint the
  record already computes.
- a11y — N/A: no user interface.
- i18n — N/A: operator-facing English in shell.
- error / empty / loading states — an absent or corrupt ledger yields no reuse, the safe direction,
  and carries an arm.
- observability — the reuse verb names every leg that was skipped for this reason, and the record
  counts them, so a reused run is never mistaken for a full one.
- risks (concurrency, data-loss, rollback hazards) — the real risk is a mis-declared impure leg
  yielding a stale green on an opt-in run. Bounded by the boundary rule and by S8's structural arm.
- testing + left-shift gates — S8 left-shifts the under-declaration class one hop deep, and says so
  in its own header rather than implying more.
- migration / rollback — the shipped default is the rollback.
- user docs — the charter's gate-suite paragraph gains the reuse knob and its default.

## 6. Acceptance criteria

- **AC1** — When a green run is repeated with `GATE_REUSE=1` on an unchanged tree, every pure leg
  prints the reuse verb and the verdict names a non-zero reused count.
- **AC2** — When a leg fails, is fixed, and the bar is re-run with `GATE_REUSE=1`, only that leg and
  the legs whose inputs the fix moved execute — asserted in
  `tools/run-gates/run-gates.evidence.test.sh` by comparing the executed set against the changed set.
- **AC3** — When one file inside a guarded leg's guard changes, that leg is NOT reused on the next
  run with `GATE_REUSE=1`.
- **AC4** — When a leg is declared `impure`, it is never reused even on a byte-identical tree.
- **AC5** — When a leg's previous row records a failure, it is never reused, asserted in
  `tools/run-gates/run-gates.evidence.test.sh`.
- **AC6** — When `GATE_REUSE` is unset, no leg is reused and stdout is byte-identical to a run
  against a manifest carrying no reuse state.
- **AC7** — When the branch has DIVERGED from the default branch, a leg whose guard paths are
  unchanged since the branch point skips, where the same leg against the origin tip would run —
  asserted in `tools/run-gates/run-gates.test.sh`.
- **AC8** — When `GATE_BASE` is set explicitly, it still outranks the merge-base derivation.
- **AC9** — When the base cannot be resolved at all, every leg runs, asserted in
  `tools/run-gates/run-gates.test.sh`.
- **AC9b** — When the run is ON the default branch, so the merge-base against it is HEAD itself, the
  base is refused and every leg runs — asserted in `tools/run-gates/run-gates.test.sh`. Without this
  the adopted merge-base form scopes the entire bar away on the one branch that matters most.
- **AC12** — When the structural network matcher is run over `tools/gate-legs.json`, it resolves the
  known network-calling legs by name, and when its match set is emptied it prints `DEAD PROBE` and
  exits non-zero — the anti-vacuity control, without which S8 passes by finding nothing.
- **AC10** — When a leg's own script directly calls out to the network and carries no `impure`
  declaration, `bash tools/run-gates/run-gates.test.sh` exits non-zero naming that leg.
- **AC11** — When a run reuses any leg, `<git-dir>/gate-full-green` is not written, so the fact
  `TOOL-aPacedTurnstile-7` consumes can never rest on a reused verdict.

## 7. Gates

`bash tools/run-gates/run-gates.test.sh` · `bash tools/run-gates/run-gates.evidence.test.sh` ·
`bash tools/check-testsuite-counts.sh` · `bash tools/memory-tree/check-verdict-epoch.sh` ·
`python tools/memory-tree/check-arms.py --check` · `bash tools/memory-tree/check-memory-hygiene.sh`.

## 8. Open questions

- **Whether this unit and `TOOL-aPacedTurnstile-5` should be one spec.** The design research
  recommended one, on the argument that the consumers are the reason the record's fields exist, and
  that specifying an emitter without them produces fields nobody has had to read. RESOLVED (agent,
  2026-08-18, delegated by the owner's kickoff scope approval): keep them split, and cut at the
  write/read seam rather than at the base change. The reason is review risk, not scheduling —
  `TOOL-aPacedTurnstile-5` changes no verdict and this unit changes verdicts, so the split isolates
  the half a reviewer must be hostile toward. The research's concern is answered at the build level:
  every field the record carries is read by this unit or by `TOOL-aPacedTurnstile-7`, both specced
  in this same set, and the reconcile pass checks that join in both directions.
- **Whether the structural network-call arm should walk two hops.** Recommendation: no. A graph
  walker does not earn itself for a three-leg population, and the gate states its own one-hop
  ceiling in its header the way `check-method-carriers.sh` already does.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.
- rev-2 · 2026-08-18 · folded the spec audit: S5 names the ref it takes the merge-base against and
  refuses a degenerate base equal to HEAD, the `TOOL-cFinalBerth-2` class the adopted form otherwise
  inherits (F22, F23); S8's matcher becomes wrapper-aware and carries a `DEAD PROBE` anti-vacuity
  control, having found zero sites in the very files that motivated it (F24); S4 states which unit
  owns the `impure` key against which owns its values (F41).

## 10. Reuse audit

The seam this extends is the runner's existing serial guard pre-pass, which already materialises a
skip decision before any worker starts. Reuse joins it there rather than adding a second decision
point, so neither decision depends on scheduling — the same reason that pass is already serial. The
report verb extends `report_one`'s existing branch set under the column contract
`TOOL-aPacedTurnstile-1` owns. The base derivation adopts the merge-base form already used by
`tools/memory-tree/check-verdict-epoch.sh`, which is why this is a convergence rather than a new
notion. The record it reads is `TOOL-aPacedTurnstile-5`'s.

Recall terms used: gate, leg, verdict, reuse, cache, lock, beacon, queue, concurrent, session,
worktree, scoped, diff, GATE_FULL, guard, skip. The probe returned `cBriefedPilot-15` (the verified
live guard hole this unit's key closes for guarded legs) and the aTimedTurnstile review's F6 (the
cache carry-forward whose semantics the ledger preserves).
