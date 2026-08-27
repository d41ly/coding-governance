# TOOL-aPrimedKeepalive-4 — leg check 7 stops counting a LANDING record whose work is already on the remote

**Status:** INPROGRESS · rev-3 · 2026-08-27 · node a · Tier-2 · base b4e1d5be · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-27-build-TOOL-aPrimedKeepalive-1-7-acceptance-ledger.md](../build/2026-08-27-build-TOOL-aPrimedKeepalive-1-7-acceptance-ledger.md) | journal | TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-5 TOOL-aPrimedKeepalive-6 TOOL-aPrimedKeepalive-7 |
| [2026-08-27-prompt-TOOL-aPrimedKeepalive-1-1.md](../prompts/2026-08-27-prompt-TOOL-aPrimedKeepalive-1-1.md) | research | TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-5 |
| [2026-08-27-review-TOOL-aPrimedKeepalive-1-6-spec-audit-round1.md](../reviews/2026-08-27-review-TOOL-aPrimedKeepalive-1-6-spec-audit-round1.md) | spec-audit | TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-5 TOOL-aPrimedKeepalive-6 |

<!-- /gen:spec-records -->

## 1. Goal

A run that reaches `LANDING`, merges, pushes, and then cannot stamp its own record holds the entire
fleet's bar hostage: check 7 counts it as a live run forever, so the next run's bar reds and the next
run cannot land either. `memory/builds/dTieredTribunal/RUN.md` is in that state at BASE and blocks
this build. Stop counting a record whose work is provably on the remote's default branch, and report
it instead.

## 2. Scope (IN)

- **S1** — `tools/unattended/check-unattended.sh`'s `nlive` accumulation excludes a record whose
  phase is exactly `LANDING` and whose `witness` is sha-shaped, resolves in this clone, and is an
  ancestor of the tip the remote advertises for the default branch.
- **S2** — every excluded record is REPORTED by path, with the witness and the anchor it was judged
  against. An exclusion nobody can see is a check quietly deleted.
- **S3** — the exclusion FAILS CLOSED. If the remote did not answer, **if the advertised tip names a
  commit this clone has not fetched**, if the witness does not resolve, or if the phase is anything
  other than `LANDING`, the record counts exactly as it does today, and the reason is reported. The
  fetched-tip cause is the one the first draft omitted, and the code it borrows from documents it two
  lines from the idiom S1 copies: `check-unattended.sh:816-817` blanks its anchor under the comment
  "PROVED PRESENT, not merely non-empty ... which red three honest LANDED records".
- **S4** — the failing case is OBSERVED before the change lands: a record in `LANDING` whose witness
  is NOT an ancestor of the advertised tip must still red check 7 when a second run is live.

## 3. Non-goals (OUT)

- Any change to `--landed`, its check 34, or the lander marker. `TOOL-dUnstalledConvoy-38` owns that
  predicate and is not this unit; the record this build is blocked by cannot be stamped from node
  `a` under any predicate, because this node's marker predates the work.
- Any change to `PHASES_TERMINAL`. `LANDING` stays non-terminal, because it means the Definition of
  Done was evaluated and the landing not yet observed, and that is true of the excluded records too.
- Excluding any phase other than `LANDING`. A `BUILDING` record whose witness happens to be on the
  remote is a genuinely live run and must keep counting.
- Marking `dTieredTribunal` terminal by hand. Its record stays exactly as its own run left it; this
  unit changes what the leg CONCLUDES from it, not what it says.
- The driver's own `check_single_live`. It is `TOOL-aPrimedKeepalive-7`, adopted mid-build after
  this section's first draft was DISPROVED: it claimed the driver "already admits the ordinary second
  run", and `--preflight` was then observed refusing at exactly two live records. The claim was
  reasoning about the code rather than an observation of it.

## 4. Design

### Why the exclusion is honest and not a relaxation

Check 7's stated purpose is in its own header: more than one non-terminal record means *"the run" is
not well-defined for anything keyed on it*. A record at `LANDING` whose witness is an ancestor of the
tip the remote advertises is not a competing run — it is a finished one missing a stamp. Nothing
keyed on "the run" would ever resolve to it, because its work is already on the branch every later
run measures against.

The check keeps its full strength everywhere else. A `LANDING` record whose work is NOT on the remote
is exactly the dangerous case — a run that closed and never landed — and it keeps counting.

### The predicate, and where it actually goes

Check 15 performs the same ancestry test at `:909` — `GIT merge-base --is-ancestor "$w" "$b"` — but
**`$b` is NOT in scope at the accumulation point**, and an earlier draft of this section said it was.
`nlive` increments at `:695`; `b="$ADV_HEAD"` is assigned at `:816` inside a conditional, so at the
accumulation point it is unset on the first record and holds the PREVIOUS record's value on every
later one. Written literally, that is a loop-carried stale anchor.

So the exclusion is a SECOND pass over `$live`, after the walk, reading `ADV_HEAD` directly and
never `$b`, re-deriving `phase_of` and `fact_of` per record. That re-derivation is deliberate and is
not the two-answers-to-one-question class: it reads the same two accessors the walk reads, from the
same file, at the same commit — one grammar evaluated twice, not two grammars.

### Liveness, which is the part that must not be skipped

The leg's remote observation can fail: `ADV_NREM_RC` already carries "no remote" and "more than one
remote" as distinct causes, and the advertisement itself can time out. On any of those, no exclusion
is computable, so every record counts and the leg SAYS the exclusion was unavailable. A check that
silently stops excluding is indistinguishable from one that found nothing to exclude — this repo's
own named class.

### Files touched (estimate)

`tools/unattended/check-unattended.sh` — the `nlive` accumulation and one report line. No template,
no render, no conf key.

### Alternatives rejected

**Add `LANDING` to `PHASES_TERMINAL`.** It would clear the wedge and destroy the distinction the
phase exists for: `LANDING` records that the Definition of Done was evaluated, and terminality is
supposed to record that the landing was OBSERVED. Rejected — it makes every unlanded close look
landed.

**Let the leg mark the record terminal itself.** A gate leg that writes a record is a gate that
manufactures its own green. Rejected outright.

**Wait for `TOOL-dUnstalledConvoy-38` to fix check 34.** It does not unblock this build: node `a`'s
lander marker names a commit older than `dTieredTribunal`'s witness, so even the corrected predicate
refuses here — correctly. Verified before this line was written.

## 5. Production-readiness checklist

- security — N/A. A read-only ancestry test against an already-observed advertisement.
- perf / scale — no new network round trip; the advertisement is already fetched for other checks.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — S3 IS the error state and each cause is reported separately.
- observability — S2 reports every exclusion with its evidence, so a reader can see what the leg
  decided and why.
- risks — the real risk is over-excluding and hiding a genuinely stuck run. The phase guard plus the
  ancestry test bound it, and S4 observes the failing case rather than assuming it.
- testing + left-shift gates — S4's staged break is the left-shift; the kit's own self-test suite
  covers check 7 and is run on demand per the kit descriptor.
- migration / rollback — one predicate; revert is the rollback. No adopter inherits state.
- user docs — none. The check's own header states what it does and does not do, and is updated.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/check-unattended.sh` runs at BASE with this build's own run
  live, check 7 is GREEN, and its report names `memory/builds/dTieredTribunal/RUN.md` as excluded
  with its witness and the anchor it was judged against.
- **AC2** — When a fixture record is placed in `LANDING` with a witness that is NOT an ancestor of
  the advertised tip and a second run is live, check 7 FAILS — observed, then removed. This is S4.
- **AC3** — When the remote cannot be observed OR its advertised tip does not resolve in this clone,
  the leg reports the exclusion UNAVAILABLE naming that cause and every `LANDING` record counts. The
  line is emitted only when `nlive > 1`, i.e. only when the exclusion could have changed the verdict —
  stated so silence at `nlive <= 1` is a decision rather than an omission.
- **AC6** — When the leg runs with two live records and one excluded, the exclusion line appears on
  STDOUT of a DEFAULT invocation, not behind `REPORT=1`. An exclusion visible only under an opt-in
  flag is the invisible skip S2 forbids.
- **AC4** — When a record in any phase other than `LANDING` carries a witness on the advertised tip,
  it still counts toward `nlive` — the guard is on the phase, verified by reading the predicate.
- **AC5** — When check 7's own header in `tools/unattended/check-unattended.sh` is read, it names the
  exclusion and what the exclusion does NOT claim, per charter §7's rule that a gate states what it
  does not check.

## 7. Gates

`unattended kit gate`, and `bash tools/run-gates/run-gates.sh` at the push boundary. The kit's own
self-tests are not bar legs by owner ruling; `bash tools/unattended/run-unattended-gates.sh` is the
compensating check and its verdict goes in the landing report.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-27 · initial draft. Adopted into this build by owner ruling on 2026-08-27, recorded
  in the build README's owner-decisions section.
- rev-3 · 2026-08-27 · folded spec-audit round 1, findings 25 and 26. S3 omitted the fourth
  fail-closed cause — an advertised tip this clone has not fetched — which the borrowed code documents
  two lines away. §4 claimed the witness and the anchor are in scope in the same walk; `$b` is not, and
  the delivered code is a post-loop second pass, now described as built. AC6 added after the first
  implementation routed both report lines through `report()`, which is gated on `REPORT=1`.
- rev-2 · 2026-08-27 · §3's driver non-goal was FALSE and is replaced by a pointer at
  `TOOL-aPrimedKeepalive-7`. `--preflight` was observed printing `check 5` at two live records while
  verifying another unit's acceptance criterion; the original claim had been reasoned, not observed.
  AC2 and AC5 move to the AMENDED form in the acceptance ledger, because the fixture arm belongs
  with unit 7's — the two units share one predicate and a full leg run costs about fifteen minutes.

## 10. Reuse audit

The seam is check 15's own ancestry idiom, cited by path:
`tools/unattended/check-unattended.sh:909`, `GIT merge-base --is-ancestor "$w" "$b"`, inside the same
per-record walk that computes `nlive`. Both the witness and the anchor are already in scope there, so
this unit adds a phase guard to an existing expression rather than introducing a second way to ask
the same question. `ADV_HEAD`, `ADV_TIPS` and `ADV_NREM_RC` already carry the advertisement and its
distinct failure causes, which is what S3's fail-closed reporting is built from.

Recall terms used: `landing terminal phase check 7 nlive witness ancestor advertised tip deadlock
wedge run-state non-terminal fleet bar`. The query returned `TOOL-aBoundedVerdict-24`
("a run that CLOSES but cannot LAND blocks every later run's bar"), `TOOL-aFusedCharter-4` (the
three-check deadlock, measured 2026-08-19 and resolved only by falsely marking two runs ABORTED) and
`TOOL-dUnstalledConvoy-38`. All three describe this defect; none proposes this remedy, and the
remedy those rows reach for — a change to `--landed` — is verified above not to unblock this node.
