**Serves:** spec-audit TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28

# dDerivedDocket — spec audit of topic group G1, kit self-protection, round 1

*Node `d`, 2026-09-14. A Tier-2 adversarial pass over the eight specs of topic group G1: the suite
baseline, the in-place landing, the landing path, HELD, auto-resume, the derived terminal, the gate
wall and the process ledger. Four primed finder lenses ran, then a skeptic stage prompted to REFUTE
each finding in five batches, then this synthesis. The sources were the ratified design record
`memory/builds/dDerivedDocket/build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md`, the owner
mandate `memory/builds/dDerivedDocket/prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-owner-mandate.md`,
and the spec brief's roster and edge tables. Sibling specs outside G1 were read wherever an edge or
an interface named them, because contradiction between specs is in scope. Every blocker and every
high below was re-checked against source at `abac6d59` before it was written down here, and the
sites read are named in each entry.*

**Round: 1.** Range at base `abac6d59`, each subject pinned at the blob it was read at: `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-1.md@eff3044870892efe6953e21e98db9bf5d204cce3`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-2.md@28376741b92b11bfc88e26141773215f75b51573`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-3.md@080db7e6f87aae1a5bdbb49995de08a25c3f760e`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-4.md@abb0f753a3c2b6dd7a2b1aa19c19743b3ab35a45`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-5.md@59edbe034c6420f9062144921f757ee0ff3f1a0f`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-22.md@8ed493ea095269fc5a339cfc4fdf27778175a320`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-27.md@79fade4ed7a56e65143d9be4261a403e978586a2`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-28.md@bed7c3443091d36757a662a15a7ba68f71186283`

## Verdict: BLOCKED

Two blockers stand, and both sit in unit 22 at the seam where the LANDED derivation plugs into
readers that unit 4 routes through `derived_phase()`. Four confirmed findings carry them: 57 and 38
are one defect, and 77 and 58 are the other. So the blocker count is 4 by finding id and 2 by
defect. B1: `--landed` is refused by its own terminal guard after every successful push, in both
lander modes. B2: rotating a derived-LANDED record archives a file whose phase is LANDING, and the
repository's own `unattended kit gate` leg reds on it permanently.

Seven confirmed findings are HIGH, which is six defects because 2 and 39 describe one. The lease
goes stale under a live bar once unit 27 lands (H1). Unit 4 reverses KF7's ratified acceptance
without a revision line (H2). `--phase` can enter HELD with no hold facts (H3). The fact-set arm's
date idiom re-dates rotated records (H4). Unit 1 specs a fix its base already carries (H5). Unit 22's
AC10 cannot pass (H6).

Every blocker and high is a defect in a document this round read, so the disposition
`memory/guides/BUILD-METHOD.md` M4 prescribes is FOLD for all of them. Two folds change a ratified design point and should be decided rather than folded
silently: H2, which either restores KF7 or takes the reversal to the owner, and M1, whose fix
relaxes design section 21.7's push-before-HELD rule. The folded text is unreviewed surface
(`memory/gotchas/fold-text-is-unreviewed-surface.md`), so round 2 re-reviews the fold, and unit 22's
readers table and unit 4's lease section most of all.

## Run integrity

- Lenses: 4 of 4 returned, 0 DIED.
- Skeptic batches: 5 of 5 returned, 0 DIED.
- Contradictory verdicts demoted to unverified: 0. Spurious verdicts discarded: 0. Duplicates: 0.

Every counter that could make this run incomplete is zero, so the finding set is complete for what
the four lenses were primed to hunt. That is not a claim that G1 holds no other defect; it is a
claim that nothing was lost between the lenses and this page. The pipeline's duplicate count of 0 is
its own exact-match dedupe. On reading, six pairs of confirmed findings describe one defect each from
two lenses (57/38, 77/58, 2/39, 42/67, 43/68, 46/84). They are folded into one entry each below, and
every count on this page stays per finding id.

## Review shape

Raw 88, confirmed 49, refuted 39, unverified 0, precision 0.56. The 49 confirmed ids collapse to 43
distinct defects.

| Severity | Finding ids | Distinct defects |
|---|---:|---:|
| BLOCKER | 4 | 2 |
| HIGH | 7 | 6 |
| MEDIUM | 33 | 30 |
| LOW | 5 | 5 |

Precision at 0.56 sits just above the ~0.5 floor `AGENTS.md` section 8 sets. The confirmed set has
one dominant class, `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`: an
acceptance criterion that cannot fail, most often because an S-item's "Observed by" list names
criteria that stay green with the S-item deleted. Ids 1, 5, 6, 9, 14, 16, 20 to 24, 29, 32, 33, 35
and 71 are that class, which is 16 of the 49. The four
remaining topic groups should prime their lenses with that gotcha's skip test (for each S-item, name
the mutation that deletes it and the AC that reds) and require a `file:line` from the tree for every
claim about BASE.

## Findings index

| Id | Severity | Entry | Spec | Address |
|---:|---|---|---|---|
| 57 | BLOCKER | B1 | 22 | §2 S7, S8; §4 The readers |
| 38 | BLOCKER | B1 | 22 | §2 S2, S7, S8; §4 The readers |
| 77 | BLOCKER | B2 | 22 | §2 S4; §4 The readers; §6 AC6 |
| 58 | BLOCKER | B2 | 22 | §2 S4; §4 The readers |
| 2 | HIGH | H1 | 27 | §2 S4; §3 Non-goals |
| 39 | HIGH | H1 | 27 | §3 Non-goals against §2 S4 |
| 79 | HIGH | H2 | 4 | §4 The lease; §6 AC6; §8 F3; §10 |
| 60 | HIGH | H3 | 4 | §2 S9, S1 |
| 59 | HIGH | H4 | 22 | §2 S10; §4 The fact-set arm |
| 78 | HIGH | H5 | 1 | §2 S7; §4 The `$1` fix; §6 AC3 |
| 1 | HIGH | H6 | 22 | §6 AC10 |
| 40 | MEDIUM | M1 | 3 | §4 What an incomplete landing does |
| 41 | MEDIUM | M2 | 27 | §2 S7 |
| 42 | MEDIUM | M3 | 28 | §2 S3; §4 Pruning and concurrency |
| 67 | MEDIUM | M3 | 28 | §2 S3; §4 Pruning and concurrency |
| 43 | MEDIUM | M4 | 22 | §2 S2; §4 Where the tip comes from |
| 68 | MEDIUM | M4 | 22 | §4 Where the tip comes from |
| 46 | MEDIUM | M5 | 22 | §2 S10 |
| 84 | MEDIUM | M5 | 22 | §2 S10; §4 The readers; §6 AC9; §9 |
| 80 | MEDIUM | M6 | 4 | §2 S9; §4 Preflight on a live record; §6 AC10 |
| 83 | MEDIUM | M7 | 4 | §4 The lease; §6 AC7; §10 |
| 70 | MEDIUM | M8 | 4 | §4 The lease; §2 S3 |
| 69 | MEDIUM | M9 | 4 | §4 `derived_phase()`; §2 S8; §6 AC8 |
| 85 | MEDIUM | M10 | 4 | §2 S2; §4 Codes and conditions; §7 |
| 47 | MEDIUM | M11 | 1 | §2 S9 |
| 50 | MEDIUM | M12 | 1 | §2 S3 |
| 61 | MEDIUM | M13 | 3 | §4 The sequence under in-place; step 1 |
| 63 | MEDIUM | M14 | 5 | §2 S11; §4 Rollout |
| 15 | MEDIUM | M15 | 3 | §2 S3 |
| 29 | MEDIUM | M16 | 22 | §2 S6; §6 AC3 |
| 5 | MEDIUM | M17 | 1 | §2 S5 |
| 6 | MEDIUM | M18 | 1 | §2 S5 against §4 Cost |
| 71 | MEDIUM | M19 | 1 | §6 AC3 |
| 9 | MEDIUM | M20 | 2 | §2 S4, S9 |
| 14 | MEDIUM | M21 | 3 | §2 S3 |
| 16 | MEDIUM | M22 | 3 | §2 S1; §4 gates-green |
| 20 | MEDIUM | M23 | 4 | §2 S5 |
| 21 | MEDIUM | M24 | 4 | §2 S3 |
| 22 | MEDIUM | M25 | 4 | §2 S2 |
| 23 | MEDIUM | M26 | 4 | §2 S6 |
| 24 | MEDIUM | M27 | 4 | §2 S9 |
| 32 | MEDIUM | M28 | 27 | §2 S5 |
| 33 | MEDIUM | M29 | 27 | §2 S1 |
| 35 | MEDIUM | M30 | 28 | §2 S3 |
| 52 | LOW | L1 | 22 | §2 S7 |
| 72 | LOW | L2 | 22 | §4 The readers |
| 73 | LOW | L3 | 3 | §2 S2; §4 step 2 |
| 87 | LOW | L4 | 3 | §2 S5; §4 step 4 |
| 53 | LOW | L5 | 1 | §3 Edges; §9 |

Every spec path below is `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-<n>.md`,
named by its unit number.

## Blockers

### B1 — `--landed` is refused by its own terminal guard after every successful push (57, 38)

**Where.** Unit 22 §2 S7 and S8, and §4 "The readers", the row routing `refuse_if_terminal` through
the derivation; against unit 4 §2 S8.

**Defect.** At BASE `verb_landed` calls `refuse_if_terminal "$rel" --landed` before any other test
(`tools/unattended/unattended.sh:2269`). Unit 4 S8 routes that guard through `derived_phase()`, and
unit 22 S2 makes it return LANDED once the LANDING record's commit is an ancestor of the advertised
tip. That is the state after every successful landing in both modes. Under in-place, `--close`
commits the record on the prepared merge and `--land` pushes it. Under primary, the record is
committed before the lander pushes, as `--close`'s own message instructs (`unattended.sh:3046`,
"COMMIT the run-state file, then land"). So `--landed` fails check 26, "the run is already
finished", before S7's observation or S8's ancestry test can run.

**Impact.** AC4 and AC7 cannot pass as written. AC7's fixture passes only because its record was
never pushed, which is the TOOL-aBoundedCeiling-9 shape this unit exists to remove. Under primary,
which every adopter keeps, no run ever again writes LANDED, `landed-anchor`, `units-at-landing` or
`unpushed-at-landing`. The Skill's four-step sequence ends on a numbered refusal after a good landing.

**Fix.** `verb_landed` tests the RECORDED phase for terminality, through a recorded-only mode of
`refuse_if_terminal` or a test of its own. It then handles a derived LANDED explicitly: under
in-place it prints the derivation and exits 0, and under primary it proceeds to check 34's ancestry
test and writes the facts. The readers table says so, and M9's call-site list carries the row.

**Left-shift.** Two arms in `tools/unattended/unattended.test.sh`, one per mode, where the record
commit is already on the advertised tip when `--landed` runs. Stage each RED by routing the guard
back through `derived_phase()`. The class-level gate is item 1 of "Left-shift, by class".

### B2 — derived-LANDED rotation archives a non-terminal record, and the leg reds forever (77, 58)

**Where.** Unit 22 §2 S4, §4 "The readers" and §6 AC6.

**Defect.** S4 retires the record as `RUN.LANDED.<blob8>.md` while keeping its `phase: LANDING`
line. At BASE the leg's check 4 fails every archived record whose content phase is outside
PHASES_TERMINAL (`tools/unattended/check-unattended.sh:1086-1089`), and since TOOL-aUnblockedFleet-2
it is the only phase refusal left on the leg. `archive_name_of` builds the name from the recorded
phase (`unattended.sh:1602-1607`), so the file would in fact be named `RUN.LANDING.<blob8>.md`.
Protocol §2's rotation paragraph says rotation never edits a retired record and that "an archived
record carrying a non-terminal phase reds", while S4 writes `landed-derived` into it first. The
readers table names neither check 4 nor `archive_name_of`.

**Impact.** Four LANDING records sit at BASE: aCollapsedScan, dRatifiedSeam, dRetiredFork and
dSealedTally. The migration note expects each to rotate on its slug's next preflight, and under
in-place every future gov landing stays LANDING too. The first such preflight reds the `unattended
kit gate` leg, which is a repository-subject leg on every default bar, and it stays red because
retired records are frozen. AC6 is a driver arm that never runs the leg over the rotated file, and
the post-build bar performs no rotation, so nothing in this unit can see the break.

**Fix.** Choose one and state it in S4. Either rotation writes `phase: LANDED` beside the verified
`landed-derived` evidence, which is a verb that evaluates what it claims (TOOL-cFinalBerth-1). Or
check 4, check 7's live count and check 15 accept an archived LANDING record whose `landed-derived`
commit is an ancestor of the advertised tip. Either way, fix `archive_name_of`, add check 4 to the
readers table, and amend protocol §2's rotation paragraph in the same unit.

**Left-shift.** A `tools/unattended/check-unattended.test.sh` arm that rotates a derived-LANDED
fixture through `--preflight` and then runs the leg over the result. Stage it RED by reverting the
chosen fix. The class-level gate is item 2 below.

## High

### H1 — the lease goes stale under a live bar once unit 27 lands (2, 39)

**Where.** Unit 27 §3 Non-goals, the "`GATE_BOUND`'s other consumers" bullet, against its own §2 S4;
and unit 4 §4 "The lease".

**Defect.** Unit 4 sets the stale bound at `max(GATE_BOUND, LEASE_STALE_AFTER)`, with the second term
defaulting to 7200 s. The lease is refreshed only on writing verbs and at the start of
`run_bounded`, and the first term exists "because a live bar can hold a session silent for the whole
bar". Unit 27 moves the bar's bound off GATE_BOUND onto the pinned backstop, which is 21600 + 7200 +
600 = 29400 s in gov, while gov's GATE_BOUND stays 3600. Its non-goal keeps GATE_BOUND for the wiring
check, the lander probes and the asks witness, and never names the lease. The lease bound therefore
becomes 7200 s without anyone deciding it. KF7 (design §21) specified `max(backstop, declared bound)`,
and no spec in the set carries that term.

**Impact.** A bar that queues and runs past 7200 s is the i97 case unit 27 exists for. In that case
a live session's lease goes stale, `--status` prints `presumed-stopped`, and unit 4's matrix lets
`--resume --keepalive-id C` from a second session take the run over mid-bar. Two sessions then drive
one slug, which is what the lease exists to prevent.

**Fix.** Unit 4 is built before unit 27, so unit 27 takes the lease bound into its scope: the first
term becomes the pinned `gate-backstop` fact, with GATE_BOUND as the announced fallback when a record
carries no fact. Declare the edge in both specs, and add an AC where a stub bar outlives GATE_BOUND
and LEASE_STALE_AFTER but stays inside the backstop.

**Left-shift.** That AC's arm asserts no `presumed-stopped` and a refused foreign take-over. Stage it
RED by restoring the GATE_BOUND term. The class is
`memory/gotchas/amendment-leaves-its-other-half-standing.md`: a bound moved for one consumer left
its other consumer's formula standing.

### H2 — unit 4 reverses KF7's ratified acceptance without a revision line (79)

**Where.** Unit 4 §4 "The lease", the resume-matrix row "working phase · fresh, no id passed"; §6
AC6's third clause; §8 F3; §9 and §10.

**Defect.** KF7 (design lines 2329-2333) says "`--resume` refuses a fresh lease with a numbered code,
so no two sessions can drive one slug", with the acceptance "a resume while this slug's bar is
running is refused", and it names the keepalive tick as a refresh source. §22.1's D12-i9 consequence
repeats the rule (design line 2387). Unit 4 instead exits 0 with an orientation for a no-id resume
over a fresh working-phase lease, drops the tick refresh, and re-decides the point as a delegated
fork (F3). §9 records no divergence, and §10 says the spec follows KF7. The build README's rule is
that a spec diverging from the design takes a rev and a §9 line, and this one has neither.

**Impact.** The Skill's Resume step is `--resume <slug>` with no id (`SKILL.template.md:664`), so
any second session that follows it is admitted to a slug whose bar is still running. Unit 5's
refusal rule 1 concedes as much. KF7's own acceptance criterion cannot pass under AC6.

**Fix.** Restore KF7. A no-id `--resume` over a fresh lease refuses with a numbered code naming
`--keepalive-id`. The Skill's Resume step and BUILD-METHOD's regrounding line pass the session's own
keepalive id, which the session can list. State whether the keepalive tick refreshes the lease. If
the reversal is kept instead, it is an owner question and not a delegated fork, and it takes a §9
line.

**Left-shift.** Invert AC6's third clause so a no-id resume over a fresh lease refuses, and stage it
RED with the current exit-0 row. The class-level check is item 4 below.

### H3 — `--phase <slug> HELD` enters HELD with none of the hold facts (60)

**Where.** Unit 4 §2 S9 and S1.

**Defect.** `verb_phase` refuses only terminal phases and LANDING (`unattended.sh:2218-2231`). Once
S1 adds HELD to PHASES_CORE, `--phase <slug> HELD --witness <sha>` writes it. The record then has no
`held-at`, `hold-until`, `hold-code` or `held-from`, and it can sit over a dirty or unpublished tree
with the keepalive unreaped. S9 blocks `--phase` out of HELD but not into it, and no AC covers the
entry path. `--resume`'s condition test, unit 5's fire rule and refusals, and the checkpoint all
read absent facts afterwards. This is the class the LANDING refusal's own comment names and
TOOL-cFinalBerth-1 records: a precondition satisfiable by one phase move.

**Fix.** Make HELD producer-only in `verb_phase`, written by `--hold` alone, beside LANDING's
refusal.

**Left-shift.** An arm running `--phase <slug> HELD --witness <sha>` that expects a numbered refusal
and an unchanged record, staged RED by deleting the branch. The class generalises: a structural arm
in `tools/unattended/check-unattended.sh` could assert that every phase some verb other than
`verb_phase` writes is refused by `verb_phase`, which a scan of `set_fact ... phase` sites derives.

### H4 — the fact-set arm's date idiom re-dates rotated records (59)

**Where.** Unit 22 §2 S10, §4 "The fact-set arm" and §6 AC9.

**Defect.** S10 dates a record by its first commit using "the idiom `LANDED_ANCHOR_CUTOFF` already
uses", which is `git log --diff-filter=A --format=%cs -- "$f" | tail -1` with no `--follow`
(`check-unattended.sh:1276`). The DISPOSITION_CUTOFF site records why that breaks on rotated
records (`check-unattended.sh:487-491`): rotation creates a new path whose first add is the rotation
commit. Measured at BASE, aPacedTurnstile's archive `RUN.LANDED.a1fd98d8.md` reads 2026-08-20
without `--follow` and 2026-08-18 with it. Many LANDED records lack `units-at-landing` or
`unpushed-at-landing`, dCarriedReceipt, aSealedCaravan and aDeclaredBound among them. Once one is
rotated after the cutoff it is graded and fails forever. That includes dCarriedReceipt, which AC9
exempts only at its `RUN.md` path, and it is exactly the outcome F4 chose a new key to avoid.

**Fix.** Date with `git log --follow --diff-filter=A`, as DISPOSITION_CUTOFF does. Add an AC9 arm
over a pre-cutoff LANDED record after it has been rotated. Fix the shared idiom once, at both sites:
see the observation under "Outside the confirmed set".

**Left-shift.** That arm, staged RED by dropping `--follow`. The class-level gate is item 3 below.

### H5 — unit 1 specs a fix its base already carries (78)

**Where.** Unit 1 §2 S7, §4 "The `$1` fix", §6 AC3, and §3's second bullet.

**Defect.** Commit 8b29f0b9 (2026-09-08) is an ancestor of `abac6d59`. It replaced the bare `$1` in
the case pattern at `tools/unattended/unattended.test.sh:4107` with a path-agnostic pattern, and its
message says the unsharded suite "could not run unsharded at all" before it and that the arm still
fails at check 49. That is why the spec's own grep "found no candidate", and the spec marks the
claim UNVERIFIED and ships it anyway. AC3 is green at BASE, and its Red-when stages a revert of
someone else's commit, so it grades nothing this unit does. The builder is told to reproduce
`$1: unbound variable`, which cannot happen at BASE. TOOL-aTracedSpawn-1 and TOOL-aHoistedPass-36
cause 1 stay OPEN although fixed, and §3's "roughly thirty arms S7 makes reachable" misstates what
the unit changes. This is `memory/gotchas/spec-names-code-its-base-lacks.md` run backwards: a spec
naming a defect its base already fixed.

**Fix.** Drop S7 and the "`$1` fix" subsection, and cite 8b29f0b9 in §10. Delete AC3 or turn it into
a BASE measurement. Dispose the two backlog rows as fixed by 8b29f0b9, with evidence, the way
TOOL-dScaffoldedMirror-22 was closed. M19 becomes moot with this fold.

**Left-shift.** A `tools/check-spec-tokens.py` arm refusing a spec at SPECCED that self-marks a BASE
claim `(UNVERIFIED)`. Run over this build today, the bare token hits units 1, 21, 26 and 29, and
unit 29's hits are the review harness's own output literal. The predicate therefore needs the
parenthesised self-mark and a printed near-miss list before it is wired, per charter §7.

### H6 — unit 22's AC10 cannot pass (1)

**Where.** Unit 22 §6 AC10, against §2 S11.

**Defect.** AC10 requires `git diff abac6d59 -- tools/memory-tree/gen_build_index.py` to be empty at
unit 22's build commit. Units 6, 7 and 15 are ordered before 22 on the same run branch, and each
lists that file in its Files touched: unit 6 adds `parse_spec` keys, unit 7 the family view's render
path, and unit 15 V13 and `--new-build`. The diff is therefore non-empty whatever unit 22 does, and
the criterion cannot tell the break it names from sibling units' legitimate edits. This is the
second form of `criterion-asserts-what-its-own-command-cannot-show`.

**Fix.** Diff against unit 22's own starting commit, the parent of its first commit, or replace the
criterion with a grep asserting that `gen_build_index.py` never calls `landing_commit_of` or
`derived_phase`.

**Left-shift.** A `tools/check-spec-tokens.py` join: an AC that diffs a path against the build's
BASE reds when an earlier-ordered sibling's Files touched lists the same path. Both inputs are
already parsed in this tree, the order values by the build-order renderer and the Files-touched
lines by the spec reader.

## Medium

The first sixteen entries are contradictions between specs, or between a spec and BASE. The last
fourteen are gaps in what the acceptance criteria can observe, and most of them are an S-item whose
"Observed by" list names criteria that stay green when the S-item is deleted.

### M1 — a real remote outage leaves the run neither landable nor holdable (40)

**Where.** Unit 3 §4 "What an incomplete landing does", against unit 4 §2 S3.

**Defect.** On the lander's `unreachable` outcome the run pushes its branch and then runs `--hold
--code platform-unavailable`. Gov declares `ANCHOR_SCOPE="published"` (`.unattended.conf:110`), unit
4 S3 refuses `--hold` unless the branch tip is on its remote, and design §21.7 requires the branch
pushed before HELD. In a sustained outage the branch push fails too, the hold refuses, and neither
spec gives a next step. Only ABORTED or a prose ending remain, which are the two endings HELD exists
to replace. AC8 grades only the Skill text. M4 compounds this: even with the precondition fixed,
`--hold` from LANDING in an offline clone exits 1.

**Fix.** Define the unpushed hold. For example, unit 4 S3 accepts a recorded unpushed-tip fact for
`platform-unavailable` only, re-checked at resume, where unit 5's rule 4 already refuses a scheduled
resume while the remote does not answer. Unit 3 then names that route. This relaxes a design rule,
so both specs take a §9 line.

**Left-shift.** An arm where the branch push also fails and the hold is taken with the unpushed-tip
fact, staged RED by restoring the unconditional published-scope test.

### M2 — the host-degraded route omits the branch push (41)

**Where.** Unit 27 §2 S7 and §6 AC8, against unit 4 §2 S3 and unit 3 §4.

**Defect.** S7's route for a `gates-green` hold line is "reap the keepalive and run `--hold`". Under
in-place, HEAD at a failed `--close` is the prepared merge that `--prepare` built locally and nobody
pushed, so under gov's published scope unit 4 S3 refuses the hold. Unit 3's own incomplete-landing
route includes the push, and unit 27's omits it. AC8 checks only that the line routes to `--hold`.

**Fix.** S7's route becomes: push the branch, reap the keepalive, then `--hold` with `--reaped <id>`.

**Left-shift.** AC8's arm asserts that the push step precedes `--hold` in the rendered Close section.

### M3 — the `--resume` reap runs without the lease, and on rows that write nothing (42, 67)

**Where.** Unit 28 §2 S3 and §4 "Pruning and concurrency", against unit 4 §2 S5 and §4 "The lease".

**Defect.** Unit 28 rests prune safety on all four reaping verbs running "under the slug's lease".
Unit 4's matrix has `--resume` run without holding it in three rows: the no-id orientation over a
fresh lease, which is the regrounding spelling; the refusal over a foreign lease; and "still held",
which writes nothing. Unit 4 S5's ordered take-over steps carry no reap step, although DR U26
placed one second, and its hand-off gives unit 28 only the `--hold` seam. The reaper is a
project-declared command, so it runs through `run_bounded`, which unit 4 S6 has refresh the lease
and unit 28 S1 has append to the ledger.

**Impact.** An orienting session can rewrite the ledger by tmp-then-rename while the holder's
`run_bounded` appends, losing that record and leaving an orphan nothing reaps. A later `--hold` then
passes S7 over a live bar. A refused or still-held resume would write the lease and the ledger,
which breaks unit 4 AC1 and unit 5 AC7.

**Fix.** Unit 4 S5 names a reap step after the condition test and after the lease is held, and hands
it to unit 28. Unit 28 S3 reaps and prunes in `--resume` only on take-over rows, only counts orphans
on the orientation and refusal rows, and makes its reaper call without the lease refresh.

**Left-shift.** An arm where a no-id `--resume` over a fresh foreign lease leaves the ledger and the
lease byte-unchanged, staged RED by reaping on that row.

### M4 — the remote observation's refusal leaks into every `derived_phase()` caller (43, 68)

**Where.** Unit 22 §4 "Where the tip comes from" and §2 S2, against §4 "The readers".

**Defect.** `derived_phase()` calls `observe_anchor` for a LANDING record. That function reports
through `fail()`, which prints to stdout and sets the global `status` with no reset
(`unattended.sh:331`), and the script exits with `$status`. It also refuses with check 30 when this
clone lacks the advertised tip. §4 contains the refusal only inside `--status`, but the readers table
routes `refuse_if_terminal`, preflight's rotation test and `--resume` through the same derivation,
and `refuse_if_terminal` guards fourteen writing verbs at BASE, with `--hold` to come.

**Impact.** Called directly, the status leaks. `--abort` on a LANDING record with the remote down
writes ABORTED and exits 1. `--hold` from LANDING after the lander's `unreachable`, which is unit 3
§4's prescribed route, prints a spurious check-27 failure and exits 1. Called as a command
substitution, the refusal text lands inside the phase value instead, the class
`memory/gotchas/status-set-in-a-subshell.md` records. On an unfetched clone LANDED never derives, so
the migration note holds only after a fetch.

**Fix.** Observe through a silent helper that returns a code, as `branch_tip_quiet` does
(`unattended.sh:821`), never through `fail()`. Specify `derived_phase()`'s output convention, return
LANDING plus the reason to every caller, and state the fetch precondition in the migration note.

**Left-shift.** Extend AC5 to `--hold` and `--abort` on a LANDING record with an unanswered remote,
asserting the exit status and that stdout carries no `UNATTENDED check` line. Stage it RED by calling
`observe_anchor` directly.

### M5 — the fact-set arm grades an empty population in gov's own mode (46, 84)

**Where.** Unit 22 §2 S10, §4 "The readers" (the check-15-and-S10 row), §6 AC9 and §9.

**Defect.** S10 grades records that SAY LANDED. Gov lands in-place from the cutoff on (unit 3 S1),
in-place `--landed` writes nothing (S7), and rotation keeps `phase: LANDING` (S4). So no gov record
after the cutoff ever says LANDED, and the arm grades an empty set from the day it arms, with no
liveness line. That is charter §7's probe that cannot move. It also narrows DR U20's "the leg checks
each terminal record's fact set" without a §9 line, so TOOL-aBoundedCeiling-11's hand-reached
terminal stays ungated here: a hand-committed, pushed `phase: LANDING` derives LANDED with none of
`--close`'s facts. Keying on the `RUN.LANDED.` archive name instead would red every in-place
rotation for facts no in-place verb writes.

**Fix.** State the in-place fact set: `units-at-landing` and, where it applies, `asks-at-landing` at
close, and `landed-derived` at rotation. Grade the records the leg derives LANDED, which S9 already
computes for check 7, and derived-LANDED archives, against that set by mode. Print the graded count
as the arm's liveness line. Otherwise record the narrowing in §9.

**Left-shift.** A staged-RED fixture of a hand-committed LANDING record lacking `units-at-landing`
after the cutoff, plus an assertion that a zero graded count announces itself. The class is
`memory/gotchas/vacuous-selector-empty-population.md`.

### M6 — refusing every live re-preflight reverses a sanctioned flow and leaves the texts behind (80)

**Where.** Unit 4 §2 S9, §4 "Preflight on a live record" and §6 AC10.

**Defect.** The kit records a re-preflight after a compaction as sanctioned in five places: the
protocol (`PROTOCOL.template.md:572`, "re-issues the recorded set rather than opening a new turn"),
`SKILL.template.md:169`, the driver comment at `unattended.sh:1286`, the pin-once code for the base
and anchor triple (owner fork 2026-08-16, `unattended.sh:2692-2713`), and TOOL-cBriefedPilot-3's
requested-equals-recorded branch. §4's BASE premise, "re-pinning the anchor", is stale: at BASE only
`keepalive` and `witness` are rewritten. TOOL-aBranchedMandate-8's hand-off asked the fixer to
refuse or rotate, decide which and say why, with a gate asserting that the keepalive survives two
preflights. After S9, the protocol and the Skill tell an agent to re-preflight, the driver refuses
it, and the pin-once branches become dead code.

**Fix.** Decide it in §8 with the records cited. Either keep own-slug re-preflight idempotent and
make it preserve the recorded keepalive, or keep the refusal and in the same unit rewrite the
protocol's waiver paragraph and Skill line 169, remove the dead branches, correct §4's BASE claim
and log the reversal in §9.

**Left-shift.** The hand-off's own arm, the keepalive surviving two preflights, or its inverse if
the refusal is kept; the skill-wiring check then grades the rewritten texts.

### M7 — the backlog row the design closes with this unit goes unnamed, and its population has no matrix row (83)

**Where.** Unit 4 §4 "The lease" (the resume matrix), §6 AC7, §1 and §10.

**Defect.** The design lists TOOL-aReapedTicket-5 among U26's closes (design line 2081), and unit 4
never names it. That row is about non-terminal records abandoned by dead sessions. Two exist at BASE,
`memory/builds/aClosedDocket/RUN.md` and `memory/builds/aUnblockedFleet/RUN.md`, both BUILDING and
both without a lease. The matrix covers an absent lease only for HELD, §5 says an absent lease "reads
as released" with no working-phase row to apply it to, and S7 derives `presumed-stopped` only from a
lease older than the bound. So the population is never surfaced, `--resume` on it hits an undefined
cell, and AC7 names the row's candidate signal, last-commit age, as a break without citing the row.

**Fix.** Cite TOOL-aReapedTicket-5 in §1 and §10, and add a matrix row for a working phase with an
absent lease. One candidate is `presumed-stopped` once the record's last commit is older than the
bound, announced and never a refusal, per TOOL-aUnblockedFleet-1. Otherwise say the row stays OPEN
and why, and reconcile AC7 with the choice.

**Left-shift.** An arm over a leaseless BUILDING fixture asserting the chosen `--status` and
`--resume` outputs.

### M8 — the lease's identity goes stale after the first in-session resume (70)

**Where.** Unit 4 §4 "The lease" and §2 S3.

**Defect.** The lease's identity is the keepalive id. The kept resume rule
(`PROTOCOL.template.md:400-406`, `SKILL.template.md:670-686`) reaps the recorded job and schedules
a replacement on every resume, and at BASE `--keepalive-id` is accepted by `--preflight` alone. Unit
4 lets only the take-over record the new id. On the working-phase, fresh-lease rows, passing the
replacement is refused as "a different id". After the first in-session resume, the lease and the
`keepalive` fact both name a reaped job, so the premise that "a resume that passes an id its own
scheduler lists is the session that holds the lease" stops holding. S3's `--reaped` precondition
can then be met with the stale id while the live replacement keeps firing into the HELD run.

**Fix.** Let the holder record a replacement, for example `--resume --keepalive-id <new> --replaces
<old>`, accepted when `<old>` equals the lease's id. Key S3's `--reaped` on the current id.

**Left-shift.** An arm that resumes in-session with a replacement id and then holds, asserting that
`--reaped <old>` refuses and `--reaped <new>` is accepted.

### M9 — "four callers" undercounts BASE's phase reads (69)

**Where.** Unit 4 §4 "`derived_phase()`", §2 S8 and §6 AC8.

**Defect.** Besides the four callers §4 names, BASE reads the `phase` fact in `check_single_live`
(`unattended.sh:1283`, `1324`), `archive_name_of` (`1604`), `verb_landed` (`2270`, and `2282` over
other worktrees' copies) and `verb_preflight` (`2749`). AC8's structural arm, "outside the writers
only `derived_phase()` reads the phase fact", reds on BASE's own code unless each site is routed or
classed as a writer, and the spec decides none of them. The routing of `verb_landed` and
`archive_name_of` is exactly what decides whether unit 22's S4, S7 and S8 can work, which is how B1,
B2 and L2 arise.

**Fix.** List every read site with its classification, recorded or derived, and define "writer" for
the structural arm.

**Left-shift.** AC8's arm takes that table as its exemption list and refuses a row naming a site
that no longer exists. This is item 1 below.

### M10 — the hold-code vocabulary has no floor (85)

**Where.** Unit 4 §2 S2, §4 "Codes and conditions" and §7.

**Defect.** Every conf-extendable core set in the kit carries a required, shrink-only count floor.
HALT_FLOOR sits beside HALT_CODES_EXTRA (`.unattended.conf:165`, "a pin that quietly defaults is a
pin nobody set"), with DIRECTIVES_FLOOR (TOOL-cBriefedPilot-2) and CORE_FLOOR (TOOL-aUnmannedHelm-6)
beside it. Unit 4 copies the pattern as HOLD_CODES_CORE plus HOLD_CODES_EXTRA and claims the reuse in
§10, but specifies no floor. A driver edit dropping `inherited-red`, where unit 24's park policy
ends, or `host-degraded`, which unit 27's two hold lines name, passes the kit gate silently.

**Fix.** Add HOLD_FLOOR, shrink-only and required, declared in gov's conf and the kit example and
validated by the leg. Otherwise state in §8 why this vocabulary alone needs none.

**Left-shift.** A staged-RED arm deleting a core hold code from a driver copy, mirroring AC9's
CORE_FLOOR arm.

### M11 — kit-version ownership conflicts across the build (47)

**Where.** Unit 1 §2 S9, against unit 25 S6 and AC7, units 22 S13, 24 S11, 27 S9 and 28 S9, unit 23
S9 and unit 5 §3.

**Defect.** Unit 1 moves the run-gates and unattended markers at order 1. Unit 25 pins run-gates
"from 1.6 to 1.7" and "agree at 1.7" at order 25, which is false once unit 1 has landed; at BASE
`KIT_RUN_GATES_VERSION` is 1.6 and `KIT_UNATTENDED_VERSION` is 1.19. Units 24 and 27 each move
run-gates "once for this build", units 22 and 28 each move unattended "once for this build", unit 23
S9 attributes the run-gates move to unit 25 alone, and unit 5 §3 says the unattended constant moves
"once per landing range, not per unit". Either a constant moves several times in one landing range,
or later S-items and ACs grade a move they did not make and cannot red on their own break.

**Fix.** Adopt one rule for the set, for example unit 5's per-landing-range rule with a single named
owner per kit. Turn every other version S-item into a NOT OBSERVED pointer to that owner, and unpin
unit 25's figures.

**Left-shift.** A cross-spec join in `tools/check-spec-tokens.py` refusing two specs in one build
that each claim to move the same kit constant.

### M12 — unit 1's DEAD PROBE is narrower than KF14 and than unit 23's (50)

**Where.** Unit 1 §2 S3, against unit 23 §4 item 4 and design §21 KF14.

**Defect.** S3 makes a side a DEAD PROBE only when it exits non-zero with no count line AND no FAIL
line. A suite that prints its count line, prints nothing matching `^(FAIL|nope|.*FAILED)` and exits
non-zero yields an empty set, no NEW failure, and exit 0 under S5. That is green by absence. KF14
says "an empty S(L) with a non-zero exit is a DEAD PROBE", unit 1's own normaliser section cites
KF14, and unit 23 lifts this unit's runner and applies KF14's definition. One piece of machinery
therefore carries two definitions. Most suites print their count line only on a pass, which narrows
the window, but this rule is the instrument every later self-test unit's Definition of Done reads.

**Fix.** A side is a DEAD PROBE whenever its exit is non-zero and its FAIL set is empty, with or
without a count line. Add an AC for a suite that prints its count line and then exits non-zero.

**Left-shift.** That AC's fixture, staged RED by restoring the count-line clause.

### M13 — the stamp precondition is asserted, not enforced, before the in-place bar (61)

**Where.** Unit 3 §4 "The sequence under in-place", and step 1 of "`--close` under in-place".

**Defect.** The design relies on `gates-green` writing the full-green stamp, so the push does not pay
a second full bar (KF2). run-gates writes the stamp only when `git status --porcelain`, untracked
files included, was empty at start (`run-gates.sh:1114-1119`, `1855-1857`). `--attest` stages
RUN.md (`unattended.sh:3955-3956`), and the sequence's only cleanliness test, `--prepare`'s
dirty-tree check, uses `-uno` (`push-main.sh:71`). Step 1's "with the tree clean" is not a listed
refusal. An attestation between `--prepare` and `--close`, or any untracked file, leaves the bar
GREEN with no stamp and says nothing. `--land` then scopes against an older stamp or forces a FULL
bar inside `git push`, which is the guard-scoped grading this unit rejects and the second bar KF2
rules out. AC3's clean fixture cannot see it.

**Fix.** Under in-place, `gates-green` refuses, numbered and before running, when `git status
--porcelain` is non-empty, and names the stamp precondition. The Skill orders attest, commit,
`--prepare`, `--close`.

**Left-shift.** An arm running `--close` over a prepared merge with one untracked file, asserting the
numbered refusal and that no bar ran.

### M14 — the resume-schedule placeholders pass every check (63)

**Where.** Unit 5 §2 S11 and §4 "Rollout".

**Defect.** `tools/unattended/kit.toml` records a hole: the shipped conf example copied verbatim
renders its angle-bracket placeholder text as literal prose and passes every check. Its discharge
probe covers only `^KEEPALIVE_(CREATE|DELETE|INTERVAL)="<.*>"` (`kit.toml:196`). S11 ships the
example with the switch on and angle-bracket carrier names, and kit.toml is not in the files touched.
A fresh adopter who copies the example gets a non-empty `<...>` value that `adopt-unattended.sh`
substitutes, so no `{{...}}` placeholder survives and the red that AC9 and the Rollout rely on never
fires. The rendered Skill then tells the agent to file restarts with a tool literally named `<...>`.
The Rollout argument holds only for upgraders whose key is absent.

**Fix.** Extend the discharge predicate to `RESUME_SCHEDULE_(CREATE|DELETE)` and add kit.toml to the
files touched; or ship those two keys absent from the example, so the placeholder survives.

**Left-shift.** The extended discharge probe, plus an arm that adopts the example verbatim and
expects the red.

### M15 — the driver re-derives the prepared-merge predicate the lander owns (15)

**Where.** Unit 3 §2 S3 and §4 "gates-green", against unit 2 §2 S9.

**Defect.** `gates-green` tests the prepared merge "by the three facts the lander defines", but unit
2 exposes only `--carry` as a single-spelling query and hands the prepared-merge shape to unit 3 to
grade itself. The driver must re-implement the predicate, and no AC compares its verdict with
`--land`'s. Unit 3's own Alternatives reject exactly this for the carry predicate: "Two spellings of
one predicate disagree". The two can disagree on a single-parent tail or a stale `T^1`, and the run
then commits LANDING on a HEAD that `--land` refuses.

**Fix.** Unit 2 adds a read-only lander query, for example `--prepared --slug`, and `gates-green`
asks it. Otherwise an AC runs AC10's tail fixtures through both and requires one verdict.

**Left-shift.** A parity arm over the tail fixtures, driver verdict against lander verdict. The class
is `memory/gotchas/two-answers-to-one-question.md`.

### M16 — the in-place move of `asks-at-landing` is observed nowhere (29)

**Where.** Unit 22 §2 S6 and §6 AC3, against unit 17 §3 and its hands-off.

**Defect.** S6 moves both `units-at-landing` and `asks-at-landing` to `--close` under in-place, and
unit 17 delegates exactly that move to this unit. AC3 checks only `units-at-landing`. Under in-place
`--landed` writes nothing (S7), unit 17 AC8 exercises `--landed` only, and unit 18 S4 and AC7 grade
only records at LANDED, which in-place records never are. If the move is skipped, `asks-at-landing`
is never written in gov's mode and no criterion in any unit reds.

**Fix.** Extend AC3: a mandated fixture's in-place close commits `asks-at-landing` on the line after
`units-at-landing`, and a failing ASKS_CMD witness refuses `--close` before any write.

**Left-shift.** That extension, staged RED by leaving the write at `--landed`.

### M17 — unit 1: no criterion runs an inherited-only fixture (5)

**Where.** Unit 1 §2 S5.

**Defect.** S5 says INHERITED is "reported and not failing", but AC1 exits 1 because of NEW and AC5
exercises FIXED. S1 tells the L side to run "exactly as the no-flag mode does", and that loop sets
`st=1` on any non-zero exit. An implementation that exits 1 whenever S(L) is non-empty passes AC1 to
AC8 and defeats the one property units 2 to 5, 22, 27 and 28 rely on.

**Fix.** Add an AC: the fixture fails arm A at both R and L, prints `INHERITED 1` and `NEW 0`, and
exits 0.

**Left-shift.** That arm, red when the exit derives from S(L) being non-empty.

### M18 — unit 1: whether an L-side budget breach fails under `--attribute` is undecided (6)

**Where.** Unit 1 §2 S5 against §4 "Cost" and §8 F3.

**Defect.** S5 gives the full exit rule under `--attribute`: 1 on NEW or DEAD PROBE, "else 0". §4
Cost and F3 say the L side keeps "the budget verdict", and in the no-flag mode that verdict sets
`st=1` on OVER BUDGET. Read literally, S5 drops the charter's "a runner REDS on breach" in attribute
mode, while §4 implies the breach still reds. Six units cite "cost: the declared budgets" for their
`--attribute` run, and no AC decides between the two readings.

**Fix.** State whether an L-side OVER BUDGET exits 1 under `--attribute`, and add an AC with a
fixture suite whose budget row is below its runtime.

**Left-shift.** That arm.

### M19 — unit 1: AC3 measures a green suite, not a fixed abort (71)

**Where.** Unit 1 §6 AC3.

**Defect.** `unattended.test.sh` prints its count line only when every arm passes
(`unattended.test.sh:5463`, `[ "$st" = 0 ] && echo "PASS ($n assertions)"`), the conditional shape
`check-testsuite-counts.sh` requires. §3 says the arms S7 makes reachable may fail. So AC3 is unmet
whenever any arm fails, and a red but complete run is not the DEAD PROBE its Red-when names.

**Fix.** Moot once H5's fold deletes AC3. If AC3 survives, observe the absence of `unbound variable`
and a completed floor comparison instead of the `PASS` line.

**Left-shift.** None beyond the rewritten criterion.

### M20 — unit 2: an own-build carry set is never observed being accepted (9)

**Where.** Unit 2 §2 S4 and S9.

**Defect.** S4's attribution has three branches: unit id, build folder, and unknown counted as
foreign. S9 promises exit 0 on a non-foreign set. AC2 and AC10 observe only a foreign-by-unit-id
refusal, and AC1's carry set is empty. An implementation that marks a commit foreign only when it
names another build's id treats unknown commits, such as reconcile merges and ad-hoc commits, as
own. That fails open on the unit's core purpose and passes every AC. An implementation that refuses
every non-empty set also passes, and blocks every landing whose branch merged this build's own
attended commits.

**Fix.** Add an arm where local `<def>` carries a commit touching `memory/builds/<slug>/`, B merges
it, `--carry` exits 0 and `--land` pushes. Add a second arm where a subject-less, folder-less commit
reads `unknown` and refuses.

**Left-shift.** Those two arms.

### M21 — unit 3: the `GATE_FULL=1` export is unobserved (14)

**Where.** Unit 3 §2 S3.

**Defect.** AC10's environment-printing GATE_CMD asserts only `GATE_SELFTESTS`, and AC3's two-leg
manifest does not say it has a guarded leg, so the stamp's `skips=0` precondition
(`run-gates.sh:1855`) cannot tell a scoped run from a full one. Dropping the export passes every AC,
and in gov's guarded manifest the landing bar is then guard-scoped, which is the i28 and i29 shape §4
Alternatives rejects.

**Fix.** AC10 also asserts `GATE_FULL=1` in the printed environment, or AC3's fixture carries a
guarded leg the landing range does not touch.

**Left-shift.** The AC10 extension.

### M22 — unit 3: gov's own declarations are never read by a criterion (16)

**Where.** Unit 3 §2 S1 and §4 "gates-green", the "Gov declares its kit roots" sentence.

**Defect.** S1 says gov's conf sets `in-place`, and §4 says gov declares its kit roots, but AC5, AC9
and AC10 all run on fixtures, and a blank value only announces a default. The in-place path can ship
inert in the one repository that dogfoods it, and unit 22's in-place behaviour with it, while every
AC stays green. Units 5 (AC13) and 27 (AC5) carry real-tree criteria for their own gov keys, so the
build's own precedent shows the omission.

**Fix.** Add an AC: `check-unattended.sh` on the real tree reports LANDER_MODE `in-place` as
declared, and SELFTESTS_OWED_PATHS resolving to the `tools/` kit roots.

**Left-shift.** That AC is the liveness half of the in-place path in this repository.

### M23 — unit 4: authorization re-verification at a take-over is unobserved (20)

**Where.** Unit 4 §2 S5.

**Defect.** At BASE `verb_resume` (`unattended.sh:2881`) never calls `trusted_base` or
`check_authorization`, so re-verifying authorization at a take-over is new behaviour at a new call
site. AC1, AC4, AC6 and AC7 exercise only paths where authorization passes, and unit 5 AC8 runs the
take-over unchanged. A take-over that skips the step passes every criterion, and with auto-resume on
a revoked mandate keeps being driven by unwatched scheduled sessions until `--close`. The harm is
bounded by `--close`'s non-overridable `authorization-reachable` item, but S5's coverage claim is
false for a security-relevant step.

**Fix.** Add an AC: a HELD fixture whose mandate no longer verifies at the pinned BASE makes
`--resume` refuse with a number, with the run-state file and the lease byte-unchanged.

**Left-shift.** That arm, staged RED by skipping the call.

### M24 — unit 4: three of `--hold`'s four preconditions have no criterion (21)

**Where.** Unit 4 §2 S3.

**Defect.** S3 cites AC2 and AC4. AC2 covers only the dirty-tree refusal, and AC4 runs `--resume`,
not `--hold`, so the citation is wrong. Nothing feeds `--hold` an already-HELD record, an unpushed
tip under `ANCHOR_SCOPE=published`, or a keepalive neither reaped nor recorded unreachable. A
`--hold` on a HELD record would overwrite `held-from` with HELD, and unit 5 §4 rule 3 assumes the
published-scope push was required.

**Fix.** Add three `--hold` arms for those inputs, each refusing with a number and leaving the
run-state file unchanged.

**Left-shift.** Those arms.

### M25 — unit 4: the closed code set and condition grammar are never seen refusing (22)

**Where.** Unit 4 §2 S2.

**Defect.** AC1 uses a valid `after`, AC2 refuses on a dirty tree, and AC11 checks only that the
verb is declared, carried and invoked. Across the whole spec set every `--hold` invocation uses a
valid code and condition. Unit 5's fire rule parses `hold-until` as `after <instant>`, so
unvalidated text reaches a durable schedule computation, and a pause can be recorded under an
ending's code, which §4 says the separate vocabulary exists to prevent.

**Fix.** Add an AC: `--code bogus` and `--until 'after tomorrow'` each refuse with a number and no
write, and a code declared in HOLD_CODES_EXTRA is accepted.

**Left-shift.** That arm.

### M26 — unit 4: the lease lifecycle is observed only through hand-built lease files (23)

**Where.** Unit 4 §2 S6.

**Defect.** AC6 and AC7 use hand-built lease fixtures. No criterion runs `--preflight` and observes
a lease taken, a writing verb or `run_bounded` refreshing it, `--hold` writing `released`, or a
terminal removing it. A driver that never takes a lease leaves every live working-phase record
takeable, because an absent lease reads as released and a stale one reads `presumed-stopped`.

**Fix.** Add arms: `--preflight` creates `taken`, a writing verb advances `refreshed`, `--hold`
writes `released … held`, and `--abort` removes the file.

**Left-shift.** Those arms.

### M27 — unit 4: `--phase` out of HELD is unobserved (24)

**Where.** Unit 4 §2 S9.

**Defect.** At BASE `verb_phase` guards only with `refuse_if_terminal` (`unattended.sh:2210`), which
a non-terminal HELD passes. AC5 names this exact `is_terminal`-only class for `--landed` but observes
only `--landed` and `--close`. An implementation adding HELD checks to those two verbs alone leaves
`--phase` out of HELD open, skipping S5's condition test and authorization step. H3 is the same
verb's entry path.

**Fix.** Extend AC5: `--phase <working>` on a HELD fixture refuses with a number and writes nothing.

**Left-shift.** The AC5 extension.

### M28 — unit 27: the kill-after-acquired discriminator is unobserved (32)

**Where.** Unit 27 §2 S5.

**Defect.** S5 keeps today's never-returned text for a kill after the `gate queue: acquired` line.
AC1 prints acquired and exits 0, AC2 hangs without printing it, and §7's arm list has no stub that
prints acquired and then hangs past the backstop. An implementation mapping every backstop kill to
`host-degraded` and `probe gate` passes every AC, and with auto-resume on a wedged leg then gets up
to RESUME_SCHEDULE_LIMIT retries instead of the never-returned verdict.

**Fix.** Add an AC: the stub prints `gate queue: acquired` and then hangs past the backstop; the item
is UNMET with the never-returned text and no `hold` line.

**Left-shift.** That arm.

### M29 — unit 27: the `GATE_WALL` export is unobserved (33)

**Where.** Unit 27 §2 S1.

**Defect.** The runner reads `WALL=${GATE_WALL:-$PROF_WALL}` (`run-gates.sh:422`), and the driver
does not reference GATE_WALL at BASE, so the export is new. AC1's stub never shows its environment,
unlike unit 3 AC10's. AC5 reads gov's conf, where GATE_WALL and every profile wall are both 21600, so
a driver that never exports looks identical. A GATE_WALL below the profile wall gives a backstop that
fires while the runner is still legitimately inside its own wall.

**Fix.** Add an AC: with `GATE_WALL="7"` an environment-printing stub shows `GATE_WALL=7`, and with it
blank the variable is unset and the default is announced.

**Left-shift.** That arm.

### M30 — unit 28: only `--resume` is observed reaping (35)

**Where.** Unit 28 §2 S3.

**Defect.** AC1, AC4 and AC8 reap only at `--resume`. AC6 tests `--hold`'s refusal under a live
driver, where nothing is reaped, and AC2 and AC5 test non-reaping. Reaping at `--preflight`, at
`gates-green` before the bar, and at `--hold`, and pruning dead records, have no criterion. The goal
cites i26, where the driver died mid-bar and the session lived on; that run reaches `gates-green`
again without passing through `--resume`, so the one call site that fixes i26 is the unobserved one.

**Fix.** Add arms: an orphan from a killed driver is reaped by `gates-green` before the stub bar
starts, and by `--preflight`; a record whose process has exited is gone from the ledger after the
verb.

**Left-shift.** Those arms. Mind M3 when writing them: the `--resume` arm must run on a take-over
row.

## Low

### L1 — no verb removes the lease or the ledger after an in-place landing (52)

**Where.** Unit 22 §2 S7, against unit 4 §2 S6 and unit 28 §4 "Pruning and concurrency".

**Defect.** Unit 4 removes the lease "at a terminal", and unit 28 removes the ledger at a terminal
write. Under in-place `--landed` writes nothing and rotation waits for the slug's next preflight,
which may never come, so neither file is ever removed. Whenever the remote does not answer,
`derived_phase` falls back to LANDING, a working phase, so `--status` prints `presumed-stopped` for a
landed run and unit 4's matrix offers a take-over.

**Fix.** Name the in-place removal point, for example `--landed`'s successful observation; both files
live under the git common dir, so AC4's clean porcelain still holds. Otherwise exempt a LANDING
record that has a landing commit from the stale-lease rule.

**Left-shift.** An arm asserting the lease file is gone after an in-place `--landed`.

### L2 — the driver's twin of check 7's exclusion keeps the witness reading (72)

**Where.** Unit 22 §4 "The readers".

**Defect.** The readers table leaves out `check_single_live` (`unattended.sh:1260-1306`,
TOOL-aPrimedKeepalive-7), the driver's copy of check 7's LANDING exclusion, which reads the witness.
After S9, for AC8's record, with the witness pushed and the record not, preflight still announces it
excluded as finished while the leg counts it live. That is the disagreement AC8 exists to remove,
moved into the driver.

**Fix.** Route `check_single_live`'s exclusion through `landing_commit_of`, add it to the readers
table, and add an arm.

**Left-shift.** AC8 extended to preflight's live-run announcement. The class is
`memory/gotchas/two-guards-one-question-two-answers.md`.

### L3 — a lander exit of 2 is read as a mode misdeclaration (73)

**Where.** Unit 3 §2 S2 and §4 "`--close` under in-place" step 2.

**Defect.** Unit 3 reads `--carry` exiting 2 as "a lander that does not implement the mode".
`push-main.sh` already exits 2 for not-a-repo, an undeterminable default branch and a failed fetch
(`push-main.sh:15`, `23-25`, `78`), and unit 2 pins no distinct code for `--carry`'s observation
failure. A network fault or an unset `origin/HEAD` is then reported as a LANDER_MODE misdeclaration.
The refusal is right and the diagnosis is wrong.

**Fix.** Unit 2 reserves exit 2 for argument refusal under the new flags and gives "could not
observe" its own code, and unit 3 maps each.

**Left-shift.** An arm with `origin/HEAD` unset expecting the observation code, not the LANDER_MODE
message.

### L4 — a committing `--close` falsifies the rotation paragraph's premise (87)

**Where.** Unit 3 §2 S5 and §4 "`--close` under in-place" step 4.

**Defect.** Protocol §2's rotation paragraph says the archive name derives "from the BYTES rather
than the witness because no verb here commits", and TOOL-dClosedLexicon-11's DECISIONS row carries
the same clause, as does the driver comment at `unattended.sh:1590-1591`. Under in-place `--close`
now commits, and unit 3 rewrites only protocol §6. The shipped protocol will then state a reason
that is false in gov's mode, and the test comment at `unattended.test.sh:2477` goes stale with it.

**Fix.** Restate the paragraph's reason as "two runs can honestly share a witness", which still
holds, update the test comment, and note in §10 that TOOL-dClosedLexicon-11's clause is superseded.

**Left-shift.** A documented check for the fold: any change to what a verb writes greps the protocol
and the driver comments for "no verb" premises. The class is
`memory/gotchas/amendment-leaves-its-other-half-standing.md`.

### L5 — unit 1's edge record is incomplete (53)

**Where.** Unit 1 §3 Edges and §9.

**Defect.** §9 says three edges beyond the brief were added, to units 3, 4 and 5, but §3 also hands
off to unit 30, which the brief's table does not list. §3 hands off to none of 22, 27 or 28, although
each runs `run-unattended-gates.sh --attribute <BASE>` in its final AC exactly as 3, 4, 5 and 30 do,
and none of the three declares consumes-from unit 1. A change to the attribution interface, M12's
fix for one, would not be traced into three of the six subject units that use it.

**Fix.** Add hands-off lines for units 22, 27 and 28 with matching consumes-from lines there, and make
§9 list every added edge, the one to unit 30 included.

**Left-shift.** A join over the edge lines the build-edge renderer already parses: a spec whose AC
invokes `--attribute` must declare consumes-from `TOOL-dDerivedDocket-1`, and the producer must
list the matching hands-off.

## Left-shift, by class

1. **A reader routed through a new derivation without enumerating its call sites** (B1, M4, M9, L2).
   Unit 4's AC8 structural arm should take a classification table, site against recorded or derived,
   as its input. It then refuses a `phase` read absent from the table and a table row whose site is
   gone. A verb whose own postcondition is a terminal, `--landed` first, is classed recorded. B1 is
   the `two-guards-one-question-two-answers` class: the terminal guard and the verb's own purpose are
   jointly unsatisfiable after a good landing, and the gotcha should gain this build as an anchor.
2. **A rotation that changes an archived-record invariant with no leg arm over its output** (B2).
   Every driver arm that produces an archive should run the leg over the result, through one helper
   in `tools/unattended/check-unattended.test.sh`.
3. **First-commit dating without `--follow`** (H4, and the observation below). A lint arm in the
   unattended leg's self-scan flags `--diff-filter=A` first-commit dating without `--follow` under
   `tools/unattended/` and `tools/memory-tree/`. Run it over the tree first and print hits and
   near-misses: `check-unattended.sh:1276` is a live hit at BASE.
4. **A spec claiming to follow a design fix whose acceptance it contradicts** (H2, H1, M5). This is
   not mechanically gateable. The documented check for the next four groups: for every KF or D12 id a
   spec cites, the lens quotes that id's acceptance line and names the AC that meets it.
5. **An S-item whose "Observed by" criteria survive its deletion** (M17 to M30, M16, H6). Documented
   check by construction, per `criterion-asserts-what-its-own-command-cannot-show`. A partial
   mechanical half fits `tools/check-spec-tokens.py`: an S-item citing an AC whose text shares none
   of the S-item's backticked tokens is printed as a near-miss for the auditor, never as a red.

## Outside the confirmed set

One observation came out of re-checking H4 and was not put to a skeptic, so it is not counted above.
It was measured at `abac6d59`. Check 15's own grandfathering (`check-unattended.sh:1276`) uses the
same `--diff-filter=A` idiom without `--follow`. Nine LANDED `RUN.md` records carry no
`landed-anchor`: aBranchedMandate, aDeclaredBound, aDeclaredCeiling, aFusedCharter, aPacedTurnstile,
aPromptedMandate, aSealedCaravan, aSiftedPlaybook and dUnstalledConvoy. All nine were first committed
before `LANDED_ANCHOR_CUTOFF="2026-08-21"`, so they are graded clean at their `RUN.md` path today.
Rotating any of them re-dates the archive to the rotation commit, which is after the cutoff. For a
record whose witness resolves against an answering remote, check 15 would then red "names no anchor
kind" on a frozen record. The only such rotation so far,
aPacedTurnstile's on 2026-08-20, escaped by one day. H4's fix should correct the idiom at both sites
in one change, with an arm over a rotated, anchorless, pre-cutoff record.

## What this round did not cover

- Units outside G1 were read only where an edge or an interface named them. Nothing here clears
  units 6 to 21, 23 to 26 or 29 to 36, PLAY-dDerivedDocket-1 or DEPL-dDerivedDocket-1. Several
  entries (H6, M11, M12, M16, L5) name defects that also live in those siblings, and their own group
  audits should pick them up.
- The design record's measured figures were not independently re-derived. The profile walls,
  TS_MAXWAIT and the largest leg ceiling are taken as unit 27 and the design report them.
- The 39 refuted findings are not reproduced here. They were refuted, not lost, as the run-integrity
  counters show.
