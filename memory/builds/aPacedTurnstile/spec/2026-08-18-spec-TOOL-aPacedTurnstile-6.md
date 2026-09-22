# TOOL-aPacedTurnstile-6 — reuse a proven green, and scope a worktree to its own branch point

**Status:** CLOSED · rev-6 · 2026-08-20 · node a · Tier-2 · base 43a6c13e · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-18-review-TOOL-aPacedTurnstile-1-round2.md](../reviews/2026-08-18-review-TOOL-aPacedTurnstile-1-round2.md) | spec-audit | TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-7 |
| [2026-08-18-review-TOOL-aPacedTurnstile-1-round3.md](../reviews/2026-08-18-review-TOOL-aPacedTurnstile-1-round3.md) | spec-audit | TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-7 |
| [2026-08-18-review-TOOL-aPacedTurnstile-1-round4.md](../reviews/2026-08-18-review-TOOL-aPacedTurnstile-1-round4.md) | spec-audit | TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-7 |
| [2026-08-18-review-TOOL-aPacedTurnstile-1-run-cumulative.md](../reviews/2026-08-18-review-TOOL-aPacedTurnstile-1-run-cumulative.md) | diff-review | TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-7 |
| [2026-08-18-review-TOOL-aPacedTurnstile-1.md](../reviews/2026-08-18-review-TOOL-aPacedTurnstile-1.md) | spec-audit | TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-7 |

<!-- /gen:spec-records -->

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
  following `TOOL-aPacedTurnstile-1`'s two-space tail contract, TOGETHER with every consumer of that
  verb set. Three consumers exist and all three are obligations of this scope item, because a verb
  added to the runner alone is a leg that vanishes from two records without saying so.
  - `tools/run-gates/run-gates.sh` — `report_one`'s branch set, under the tail contract stated in
    that function's own header.
  - `tools/run-gates/profile_bar.py` — the `VERDICT` regex pins `^GATE (ok|skip|FAIL)\s\s+(.*)$`, so
    an unrecognised verb drops the leg from `rec["legs"]`, from the executed set and from the leg
    count in the refusal message, SILENTLY. The verb joins that alternation, and a reused leg is
    classified the way `skip` already is — no duration this run, so it must not reach the
    missing-duration list that makes the profiler refuse to publish a regime.
  - `tools/run-gates/kit.toml` — `[gate_runner_seed]` declares the deployer's whole verdict
    vocabulary as `observed_ran` / `observed_failed` / `observed_skipped`, and gains a fourth row.
    The comment beside `observed_skipped` records what a missing row costs: the deployer's state for
    that verb becomes unreachable and its DEAD-PROBE refusal structurally dead.
- **S4** — a leg declaring `impure` never gets an input key and can never be reused. The key is
  DECLARED by `TOOL-aPacedTurnstile-5`, which owns the manifest's key set; this unit owns its VALUES,
  measured rather than guessed. Two units touching one key with no stated authority is how a manifest
  ends up with two provenances for one field. The measurement is now taken and §4 records it: gov's
  corpus holds no impure leg today, so the value set this unit writes is EMPTY and the rule is graded
  by fixture rather than by a live declaration.
- **S5** — the base becomes the merge-base against the default branch WHERE THAT IS A PROPER
  ANCESTOR OF HEAD, and the origin tip otherwise. The default branch is OBSERVED from the remote and
  never taken from a local ref. `GATE_BASE` still outranks everything, and an unresolvable base still
  fails safe to running every leg. The proper-ancestor test is what keeps the
  `TOOL-cFinalBerth-2` class out: a degenerate merge-base equal to HEAD would otherwise scope the
  entire bar away, and refusing the base outright would instead scope NOTHING away on the commonest
  scoped-run state in this repo. §4 works the four cases and shows the change is inert everywhere
  except a diverged branch.
- **S6** — a canary arm for the case that actually distinguishes the two base semantics: a guard-
  unchanged leg on a DIVERGED branch skips against the merge-base where it would have run against
  the tip.
- **S7** — reuse arms in `tools/run-gates/run-gates.evidence.test.sh`: a reused leg prints the reuse
  verb, a changed input defeats reuse, an impure leg is never reused, a red leg is never reused, and
  reuse is off unless asked.

## 3. Non-goals (OUT)

- Writing the record. That is `TOOL-aPacedTurnstile-5`.
- The push boundary. `TOOL-aPacedTurnstile-7` owns it, and it reads the full-green file rather than
  the ledger.
- Turning reuse on by default. See the boundary rule; it is opt-in and this unit keeps it that way.
- A resume flag, a failed-leg list, or a state machine. Reuse subsumes them, which is the argument
  for this shape.
- Sharing the ledger across this node's worktrees, whose count is derived from `git worktree list`
  and is well into double figures. Sound and tempting, but it converts a single-writer file into a
  contended one, and the contention design is `TOOL-aPacedTurnstile-4`'s. Under the re-derived order
  `-4` lands BEFORE this unit, so the lock will exist — the cut stands anyway, because what is still
  missing is a measurement of how often a cross-worktree key actually matches. Revisit with that
  number, not with the lock.
- Widening or narrowing any leg's `guard`.
- **The structural network-call gate — CUT at rev-5, not deferred.** This was S8, with AC10, AC12
  and AC12b. Two independent findings killed it, both of them measurements this spec should have
  taken before wiring a predicate, per the charter's §7 rule that a candidate gate predicate is run
  over the real tree first. (1) The predicate run over `tools/gate-legs.json` at `43a6c13` matches
  six legs and every one of them is hermetic: `tools/unattended/unattended.test.sh` builds its origin
  under `mktemp -d`, and `.githooks/pre-push.test.sh` says in its own header that it drives a real
  push into a throwaway scratch repo. The gate would red six innocent legs. (2) `impure` cannot
  travel to an adopter: `tools/govkit/govkit.py` emits `name`, `argv` and `guard` and nothing else, so
  a shipped arm demanding the declaration reds on arrival in every target — the same
  `pin-copied-from-another-corpus` class rev-4 diagnosed for the NAME half while leaving the
  DECLARATION half shipped. Making the key travel needs a descriptor field and an emitter change,
  which belong with the key's owner and not here. The ids `S8`, `AC10`, `AC12` and `AC12b` are
  RETIRED and are not reused by a later rev, so a review citing them still resolves.
- Making `impure` travel through the deployer. That is the key owner's problem
  (`TOOL-aPacedTurnstile-5`), and this unit no longer has a shipped arm that depends on it.

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
tree and every key with it. The ceiling is DERIVED, not pinned: on a floor-bound bar, reusing every
pure leg leaves the binding leg to run, so the saving is the observed wall clock minus that leg's own
duration, both read from a `python tools/run-gates/profile_bar.py` record. At the re-scope
measurement — quiet node `a`, `43a6c13`, 2026-08-20, `GATE_FULL=1` — that is 1033.2 s of wall against
a binding `unattended driver selftest` of 836.5 s, so under 200 s, on an opt-in run only. Both terms
move with every commit; re-run the instrument rather than quoting these. Diff-scoping still needs the
guard, which is why `TOOL-aPacedTurnstile-7` exists and why this unit does not pretend to replace it.
What the guarded key does add is a strictly better guard for the legs that have one: hashing the
path-and-blob set the guard names is exactly as sound as the guard while closing the untracked-file
hole and getting reverts and rebases right — a diff calls a file that changed and changed back
"changed"; a hash calls it the same.

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
own base as a merge-base, with the origin-prefixed ref first and a local fallback. One bar, two
notions of base; this change removes the inconsistency.

**Why the rule is proper-ancestor-or-tip, and not a refusal.** Rev-2 wrote the degenerate case as a
REFUSAL: a base equal to HEAD is thrown away and every leg runs. That is wrong in the expensive
direction, and the re-scope caught it by working the four cases the runner actually meets.

| case | merge-base | rev-2 refusal | rev-5 rule | today's origin tip |
|---|---|---|---|---|
| diverged branch | proper ancestor | merge-base | merge-base | tip — the case this unit fixes |
| fresh branch off a fast-forwarded `main` | HEAD | refused, whole bar runs | tip, which equals HEAD | tip |
| on `main`, working tree dirty | HEAD | refused, whole bar runs | tip, which equals HEAD | tip |
| on `main`, local commits ahead | origin tip | origin tip | origin tip | tip |

The middle two rows are the commonest scoped-run state in this repo, and the refusal turns each of
them into a full bar. `changed()` diffs BASE against the WORKING TREE rather than against a commit,
so an equal-to-HEAD base still scopes correctly on uncommitted edits — that is why the tip fallback
is not merely safe but is the behaviour the tree already relies on. The `TOOL-cFinalBerth-2` class is
still refused, since no case scopes the whole bar away; it is refused by falling back rather than by
running everything.

The rule's blast radius is therefore exactly ONE row: the change is byte-inert on every case except a
diverged branch, which is the case S6 and AC7 grade and the only case where nothing grades it today.

The claim rev-4 carried here — that today's canary arm passes under either semantics, so the change
lands untested — was half right and its second half was false in the direction that reds on landing.
The 3h fixture in `tools/run-gates/run-gates.test.sh` does `git init -q -b main`, commits, then points
`refs/remotes/origin/main` and `origin/HEAD` at HEAD, so merge-base equals HEAD: under rev-2's refusal
that arm loses its `GATE skip  guarded  (unchanged vs main)` line, its `2/2 legs passed (1 skipped)`
tally and the manifest-position assertion built on both. Under rev-5's rule the fallback returns the
tip and the arm is untouched. The first half stands — the arm cannot distinguish the semantics, which
is still why S6 exists.

### Recursion and concurrency

The kit holds five harnesses. Two execute a nested runner and their isolation differs:
`tools/run-gates/run-gates.test.sh` drives it inside scratch repos that each have their own git dir,
and `tools/run-gates/run-gates.evidence.test.sh` drives it through an explicit `GIT_DIR` and
`GATE_LEGS`, as its own header states. Three do not execute it:
`tools/run-gates/run-gates.gov.test.sh` parses the manifest and greps the runner,
`tools/run-gates/adopt-run-gates.test.sh` exercises the adopter, and
`tools/run-gates/profile_bar.test.sh` injects a stub in place of the subprocess call. Outside the
harnesses, `tools/run-gates/profile_bar.py` spawns the real runner itself, which is why S3 treats it
as a first-class consumer rather than as a reader. Every record read is derived from the resolved git
dir, so a nested run reads the fixture's. No lock is introduced, so there is nothing to deadlock on.

That git dir already holds a SECOND per-leg run record: `profile_bar.py` appends per-run, per-leg
verdicts to `<git-dir>/gate-profile.jsonl`. It is not a substitute for the ledger — it carries no
input key and exists only when the profiling verb is run — and this unit reads only
`TOOL-aPacedTurnstile-5`'s ledger. Whether one git dir should hold two per-leg records is the
record owner's question, not this unit's.

One inherited-environment hazard is real and is handled by the default: the canary's scratch dir
persists across arms, so a ledger accumulates there. If reuse were on by default, the existing
width-1 against width-4 equivalence arm would compare a fresh run against a fully-reused one and
break. That is concrete evidence for the opt-in default rather than a hypothetical.

### Which legs are impure

Measured at `43a6c13` on 2026-08-20, and the answer is NONE. The legs are the harnesses, not the
product files. Every leg whose own script contains a direct network verb — derived by running that
predicate over `tools/gate-legs.json`, six legs at that sha and a number that moves — builds its
remote locally: `tools/unattended/unattended.test.sh` constructs `ORIGIN` under `mktemp -d` and
pushes and fetches there, and `.githooks/pre-push.test.sh` states in its header that it drives a real
push into a throwaway scratch repo. Two of the six are outside the unattended kit entirely, which is
why the earlier three-or-four-leg framing was drawn from the wrong population as well as being wrong
about it.

Rev-4 said "until measured, declare all four — over-declaring costs nothing". That was false on both
halves. The population was never four, and over-declaring costs precisely the leg reuse most wants:
the binding leg is inside the set the old predicate matched, and it is the majority of the wall clock
under the measurement §4 cites above. So the value set this unit writes is empty,
`tools/gate-legs.json` leaves the files-touched table, and the S1 purity clause plus AC4 are graded
by a FIXTURE manifest in the evidence harness rather than by a live declaration. That is a
deliberately fixture-only path and is named here so a reader does not mistake a green AC4 for
evidence about gov's real corpus.

### Rollout

One commit, after `TOOL-aPacedTurnstile-4` under the re-derived build order `-5 → -4 → -6 → -7 → -3`.
`-5` supplies the ledger and the key set this unit reads; `-4` lands first because it settles
contention before this unit changes the base every guard diffs against, keeping the two failure
surfaces apart. `TOOL-aPacedTurnstile-7` follows, consuming the base this unit sets. Rollback is
unsetting the feature, which is the default, so the rollback state is the shipped state and every arm
runs against it. The base change has no flag and is not rollback-protected that way; its blast radius
is the single diverged-branch row of the case table above, which is what makes that acceptable.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/run-gates/run-gates.sh` | the reuse decision in the existing serial pre-pass, the key, the verb, the base |
| `tools/run-gates/profile_bar.py` | the `VERDICT` alternation and the reused-leg classification (S3) |
| `tools/run-gates/kit.toml` | the fourth `[gate_runner_seed]` verdict row (S3) |
| `tools/run-gates/run-gates.test.sh` | S6's diverged-base arm |
| `tools/run-gates/run-gates.evidence.test.sh` | S7's reuse arms, and AC13's profile-bar arm |
| `tools/run-gates/README.md` | the reuse knob in the per-file knob table |
| `tools/run-gates/gate-profiles.txt` | the reuse knob in the OVERRIDES paragraph |
| `AGENTS.md` | the merge-bar section's knob line |

`tools/gate-legs.json` and `tools/run-gates/run-gates.gov.test.sh` were in this table at rev-4 and
are OUT at rev-5: the first because the measured `impure` value set is empty, the second because the
gov-corpus arm it held was cut with S8.

### Alternatives rejected

- **Reuse on by default.** Rejected: it would break the canary's equivalence arm, and it inverts the
  boundary rule by letting an advisory declaration reduce work on an authoritative run.
- **A dedicated resume file listing failed legs.** Rejected: a second mechanism for a case the key
  already covers, and it would need its own staleness rule.
- **Keying reuse on the guard's diff rather than a hash.** Rejected: inherits the untracked-file hole
  and mis-handles reverts.
- **Refusing a base equal to HEAD, as rev-2 specified.** Rejected at rev-5: it cannot distinguish a
  degenerate merge-base from a fresh branch off a fast-forwarded default, turns the two commonest
  scoped-run states into full bars, and reds the shipped canary's own skip arm. See the case table.
- **Moving the structural network-call gate to another unit rather than cutting it.** Rejected: the
  predicate is wrong over the real tree in any unit, so relocating it would relocate a defect. If the
  under-declaration class is worth gating, it needs a new predicate and its own measurement first.

## 5. Production-readiness checklist

- security — reuse reads only the record in the git dir; a hostile ledger can cause a wrong skip on
  an opt-in run, which is why the authoritative fact demands nothing was reused.
- perf / scale — one digest per leg over its guard paths, plus the one whole-tree fingerprint the
  record already computes.
- a11y — N/A: no user interface.
- i18n — N/A: operator-facing English in shell.
- error / empty / loading states — an absent or corrupt ledger yields no reuse, the safe direction,
  and carries an arm.
- observability — the reuse verb names every leg that was skipped for this reason, the record counts
  them, and the profile-bar record keeps them countable, so a reused run is never mistaken for a full
  one in either record.
- risks (concurrency, data-loss, rollback hazards) — the residual risk is a mis-declared impure leg
  yielding a stale green on an opt-in run, bounded by the boundary rule. It is no longer bounded by a
  structural gate: S8 was cut, so this class is an ACCEPTED residual for this unit rather than a
  left-shifted one, and §3 records why.
- testing + left-shift gates — S6 covers the base change's one distinguishing case; S7 covers reuse;
  AC13 keeps the profiler honest about a verb it does not otherwise see. The under-declaration class
  is NOT left-shifted here — see the risks line.
- migration / rollback — the shipped default is the rollback.
- user docs — three carriers, not one, because a knob documented in one of them is the recurring
  defect this build's README names: the merge-bar section of `AGENTS.md`, the per-file knob table in
  `tools/run-gates/README.md`, and the OVERRIDES paragraph in `tools/run-gates/gate-profiles.txt`.

## 6. Acceptance criteria

- **AC1** — When a green run is repeated with `GATE_REUSE=1` on an unchanged tree, every pure leg
  prints the reuse verb and the verdict names a non-zero reused count.
- **AC2** — When a leg fails, is fixed, and the bar is re-run with `GATE_REUSE=1`, only that leg and
  the legs whose inputs the fix moved execute — asserted in
  `tools/run-gates/run-gates.evidence.test.sh` by comparing the executed set against the changed set.
- **AC3** — When one file inside a guarded leg's guard changes, that leg is NOT reused on the next
  run with `GATE_REUSE=1`.
- **AC4** — When a leg is declared `impure` in the harness's fixture manifest, it is never reused
  even on a byte-identical tree, asserted in `tools/run-gates/run-gates.evidence.test.sh`. Fixture
  only: §4 records that gov's own corpus declares no impure leg.
- **AC5** — When a leg's previous row records a failure, it is never reused, asserted in
  `tools/run-gates/run-gates.evidence.test.sh`.
- **AC6** — When `GATE_REUSE` is unset AND an immediately preceding green run left ledger rows that
  WOULD match this run's keys — the precondition AC1 already states and this one did not — no leg is
  reused and stdout is byte-identical to the control, which is that same tree run with the ledger
  removed. Without the precondition both clauses pass by finding nothing on a cold ledger, which is
  this repo's `memory/gotchas/fixture-passes-by-finding-nothing.md` class in the ONE criterion
  guarding the opt-in default — and that default is §4's boundary rule, that an advisory input may
  cause less work only on an opt-in, non-authoritative run. Stated this way, a leaked default shows
  up as reuse verbs on the subject run's stdout (round 2's R28).
- **AC7** — When the branch has DIVERGED from the default branch, a leg whose guard paths are
  unchanged since the branch point skips, where the same leg against the origin tip would run —
  asserted in `tools/run-gates/run-gates.test.sh`.
- **AC8** — When `GATE_BASE` is set explicitly, it still outranks the merge-base derivation.
- **AC9** — When the base cannot be resolved at all, every leg runs, asserted in
  `tools/run-gates/run-gates.test.sh`.
- **AC9b** — When the run sits where the merge-base resolves to HEAD itself — the existing 3h fixture
  in `tools/run-gates/run-gates.test.sh`, whose remote ref points at HEAD — the base falls back to the
  origin tip and the guarded leg still prints `GATE skip  guarded  (unchanged vs main)` with its
  `2/2 legs passed (1 skipped)` tally. The arm is unchanged by this unit and must stay green: that is
  the observation that the rule scopes nothing away on the branch states that matter most, which
  rev-2's refusal would have broken.
- **AC11** — When a run reuses any leg, `<git-dir>/gate-full-green` is not written, so the fact
  `TOOL-aPacedTurnstile-7` consumes can never rest on a reused verdict.
- **AC13** — When a run that reused at least one leg is profiled with
  `python tools/run-gates/profile_bar.py`, the reused legs appear in the emitted record with their
  verb, the reported leg count equals the number of legs the runner reported, and the profiler does
  not refuse for a missing duration — asserted in `tools/run-gates/run-gates.evidence.test.sh`.
  Without this the new verb is dropped by the `VERDICT` regex and the profiler under-counts the bar
  in silence.
- **AC14** — When `tools/run-gates/kit.toml` is read, `[gate_runner_seed]` declares a template for
  the reuse verb alongside `observed_ran`, `observed_failed` and `observed_skipped`, so the
  deployer's state for a reused leg is reachable rather than structurally dead.

## 7. Gates

`bash tools/run-gates/run-gates.test.sh` · `bash tools/run-gates/run-gates.gov.test.sh` ·
`bash tools/run-gates/run-gates.evidence.test.sh` · `bash tools/run-gates/profile_bar.test.sh` ·
`bash tools/run-gates/adopt-run-gates.test.sh` ·
`bash tools/check-testsuite-counts.sh` · `bash tools/memory-tree/check-verdict-epoch.sh` ·
`python tools/memory-tree/check-arms.py --check` · `bash tools/memory-tree/check-memory-hygiene.sh`.

## 8. Open questions

none open — one fork was raised at rev-5 and RESOLVED in the same pass; the two below it are
RESOLVED or MOOT, marked in place.

- **Who removes the stale sentence S8's cut leaves in `tools/run-gates/run-gates.gov.test.sh`.** That
  file's header named three sibling arms as its reason to exist, and one of them was "the reuse unit's
  network-calling leg names" — an arm that no longer exists after §3's cut. Leaving it is a false
  claim in a shipped file's own header, which is the class §7 of the charter calls worse than the
  gap. Options seen: (a) this unit makes the one-line header correction, which is small but widens a
  unit the re-scope narrowed; (b) `TOOL-aPacedTurnstile-1` owns the file and folds it when the
  build's records close; (c) leave it and record the staleness in the build README.
  RESOLVED (2026-08-20): **none of the three — the RE-SCOPE made the correction, in the commit that
  cut the arm.** The reservation and its removal are one edit, not two, and splitting them is how a
  file ends up describing an arm nobody will ever write. The header now records that the arm was cut,
  and why, so a reader who finds the old reservation quoted in a review can still resolve it. The
  gov canary was re-run after the edit and is unchanged at 9 assertions.
- **Whether this unit and `TOOL-aPacedTurnstile-5` should be one spec.** The design research
  recommended one, on the argument that the consumers are the reason the record's fields exist, and
  that specifying an emitter without them produces fields nobody has had to read. RESOLVED (agent,
  2026-08-18, delegated by the owner's kickoff scope approval): keep them split, and cut at the
  write/read seam rather than at the base change. The reason is review risk, not scheduling —
  `TOOL-aPacedTurnstile-5` changes no verdict and this unit changes verdicts, so the split isolates
  the half a reviewer must be hostile toward. The research's concern is answered at the build level:
  every field the record carries is read by this unit or by `TOOL-aPacedTurnstile-7`, both specced
  in this same set, and the reconcile pass checks that join in both directions.
- **Whether the structural network-call arm should walk two hops.** RESOLVED (agent, 2026-08-18,
  delegated): no. MOOT at rev-5 — the arm itself is cut per §3, so the one-hop ceiling has nothing to
  bound. The resolution is kept rather than deleted because its stated ground was a three-leg
  population, and that figure was wrong twice over: the real predicate matches six legs at `43a6c13`
  and two of them are outside the kit the argument was drawn from. A ceiling argument resting on a
  miscounted population is worth keeping visible.

## 9. Revision log

- rev-6 · 2026-08-20 · BUILT and CLOSED. Both halves landed as re-scoped, and the base repair is
  the one worth reading twice.

  **The base is the branch point, and the fallback is what makes that safe.** The merge-base is
  used only where it is a PROPER ANCESTOR of HEAD; otherwise the origin tip stands. Demonstrated
  both directions on one fixture before the arm was written: on a diverged branch the leg whose
  guard the branch never touched SKIPS under the new rule and RUNS under the old one, so the arm
  has a real failing case rather than a hoped-for one. The canary builds that fixture itself,
  because the harness's existing base fixture points its remote ref at HEAD — merge-base == HEAD
  there, both rules agree, and an arm using it would grade a distinction it cannot see.

  **Reuse is opt-in, and every positive arm carries its control.** "Nothing was reused" is the
  state a cold ledger, a broken key and a correct refusal all produce, so each refusal arm also
  proves that reuse WOULD have fired on the same run: the impure leg does not reuse while its pure
  sibling does, the red leg runs again while the green sibling reuses, the changed guard defeats
  reuse for that leg only. The opt-in arm states its precondition first — that the rows WOULD
  match — then proves stdout is byte-identical to the same tree with the ledger removed.

  **A cost this unit paid for and then gave back.** The record unit left three separate
  `git status --porcelain` walks in the startup path: one for the clean test, one for the per-leg
  input keys, one inside the fingerprint helper. Measured at 2136 ms from process start to the
  header being on disk in a two-file scratch repo, and paid on every run of an 86-leg bar. Folded
  to one walk in the runner plus the helper's own, which it keeps because a git hook calls that
  executable directly and it has to be self-contained.

  The measurement surfaced through an arm rather than through a profile: the evidence harness
  killed a run at 2 s and asserted the header had been written, so it started reporting the crash
  case as unreadable. That arm was grading the runner's STARTUP BUDGET, which is not its subject.
  The kill now lands at 5 s against a 6 s leg — mid-run with room on both sides — and the startup
  cost is a separate, real finding rather than a confusing red.

  **The verb reaches its two consumers, which is the half a new verb usually loses.**
  `profile_bar.py`'s verdict grammar required two spaces after the verb, which is an accident of
  the three short verbs rather than a property of the contract — `reuse` is padded with one, so
  every reused leg was being dropped silently and the bar under-counted. And `kit.toml`'s
  `[gate_runner_seed]` now declares `observed_reused`, without which a target's reused leg has no
  deployer state and that outcome is structurally unreachable.
- rev-1 · 2026-08-18 · initial draft.
- rev-2 · 2026-08-18 · folded the spec audit. BLOCKER F4 — this unit had no position in the build
  order — is fixed in the build README, which now sequences it `-5 → -6 → -3` with its forcing edges.
  In this file: S5 names the ref it takes the merge-base against and
  refuses a degenerate base equal to HEAD, the `TOOL-cFinalBerth-2` class the adopted form otherwise
  inherits (F22, F23); S8's matcher becomes wrapper-aware and carries a `DEAD PROBE` anti-vacuity
  control, having found zero sites in the very files that motivated it (F24); S4 states which unit
  owns the `impure` key against which owns its values (F41).
- rev-3 · 2026-08-18 · swept section 8 under the standing mandate: every fork RESOLVED in
  place per M3, and the section's first non-blank line made machine-legal so the classifier
  reads this unit as READY instead of FORKED.
- rev-4 · 2026-08-18 · folded the round-2 spec audit. R10: S8's anti-vacuity control demands gov's
  network-calling legs BY NAME and reads an empty match set as `DEAD PROBE`, which reds on arrival
  in any adopter tree once `TOOL-aPacedTurnstile-1` makes the canary shippable; the gov-corpus
  expectations move to that unit's gov-only harness and AC12b keeps the wrapper-aware MATCHER graded
  in any tree, since wrapper-awareness is a property of the matcher and not of gov's corpus. R28:
  AC6 gains the precondition AC1 already states — a preceding green whose rows would match — because
  on a cold ledger both of its clauses passed by finding nothing, in the one criterion guarding the
  opt-in default that §4's boundary rule rests on.
- rev-5 · 2026-08-20 · folded the owner's re-scope and the reground against the tree at `43a6c13`,
  221 commits past the rev-4 base. The unit loses its gate and repairs its rule, and both moves come
  from the same omission: rev-2 and rev-4 argued about a predicate and a base rule without ever
  running either against the real tree, which is exactly what the charter's §7 forbids. Run now, the
  network predicate matches six legs and all six are hermetic — `tools/unattended/unattended.test.sh`
  builds its origin under `mktemp -d`, `.githooks/pre-push.test.sh` says so in its header — so the
  gate would have red six innocent legs, and `tools/govkit/govkit.py` copies only `name`, `argv` and
  `guard`, so its shipped half could never have travelled. S8, AC10, AC12 and AC12b are cut and the
  ids retired, with the under-declaration class recorded in §5 as an accepted residual rather than
  quietly dropped. The base rule's refusal-on-degenerate clause is replaced by proper-ancestor-or-tip
  after working the four real cases: the refusal could not tell a degenerate merge-base from a fresh
  branch off a fast-forwarded default, turned the two commonest scoped-run states into full bars, and
  reds the shipped canary's own 3h skip arm, whose fixture points the remote ref at HEAD — the
  opposite of what rev-4's §4 claimed about that arm. Three consumers of the report verb are named in
  S3 where rev-4 named one: `profile_bar.py` pins `ok|skip|FAIL` and drops an unknown verb silently,
  and `kit.toml`'s `[gate_runner_seed]` records in its own comment what a missing verdict row costs.
  Every pinned figure is replaced by a derivation or by a figure carrying `43a6c13` and its date, per
  the re-scope's D1: the wall-clock ceiling, the impure population, the harness count and the
  worktree count were all quoted from a 70-leg bar that no longer exists. The build order is
  re-derived to `-5 → -4 → -6 → -7 → -3`, which moves this unit behind `-4` rather than directly
  behind `-5`.

## 10. Reuse audit

The seam this extends is the runner's existing serial guard pre-pass, which already materialises a
skip decision before any worker starts. Reuse joins it there rather than adding a second decision
point, so neither decision depends on scheduling — the same reason that pass is already serial. The
report verb extends `report_one`'s existing branch set under the column contract
`TOOL-aPacedTurnstile-1` owns, and reaches the two records that read that set rather than stopping at
the runner. The base derivation adopts the merge-base form already used by
`tools/memory-tree/check-verdict-epoch.sh`, which is why this is a convergence rather than a new
notion. The record it reads is `TOOL-aPacedTurnstile-5`'s, and the separate
`<git-dir>/gate-profile.jsonl` that `profile_bar.py` writes is deliberately not reused as a
substitute, for the reason §4 gives.

Recall terms used: gate, leg, verdict, reuse, cache, lock, beacon, queue, concurrent, session,
worktree, scoped, diff, GATE_FULL, guard, skip. The probe returned `cBriefedPilot-15` (the verified
live guard hole this unit's key closes for guarded legs) and the aTimedTurnstile review's F6 (the
cache carry-forward whose semantics the ledger preserves).
