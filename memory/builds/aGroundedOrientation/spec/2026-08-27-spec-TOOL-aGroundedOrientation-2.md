**Status:** CLOSED · rev-5 · 2026-08-27 · node a · Tier-1 · base b4e1d5be · streams tooling · order 3

# TOOL-aGroundedOrientation-2 — a check arm holds the probe step ahead of the build-folder write

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-27-prompt-TOOL-aGroundedOrientation-1.md](../prompts/2026-08-27-prompt-TOOL-aGroundedOrientation-1.md) | research | TOOL-aGroundedOrientation-1 |
| [2026-08-27-review-TOOL-aGroundedOrientation-1-diff-review-round1.md](../reviews/2026-08-27-review-TOOL-aGroundedOrientation-1-diff-review-round1.md) | diff-review | TOOL-aGroundedOrientation-1 TOOL-aGroundedOrientation-3 |
| [2026-08-27-review-TOOL-aGroundedOrientation-1-spec-audit-round1.md](../reviews/2026-08-27-review-TOOL-aGroundedOrientation-1-spec-audit-round1.md) | spec-audit | TOOL-aGroundedOrientation-1 TOOL-aGroundedOrientation-3 |

<!-- /gen:spec-records -->

## 1. Goal
Left-shift TOOL-aGroundedOrientation-1 into a gate: an arm inside `check-unattended.sh` asserting the
prompt path's probe step is present and precedes its build-folder write, so a later edit cannot
silently restore the state this build fixed.

## 2. Scope (IN)
- **S1.** `tools/unattended/check-unattended.sh`, inside check 20's existing prompt-section slice
  (`$psec`): locate `RUN the orientation probes` and `Write the build folder`, and refuse when the
  probe step is absent or does not precede the write.
- **S2.** Arms in `tools/unattended/check-unattended.test.sh` for BOTH branches — the ordering
  violation and the vacuity case — each asserting this arm's own failure text.
- **S3.** Bump `ARMS_FLOORS` in `.memory-tree.conf` for
  `tools/unattended/check-unattended.sh`, which is `<path>:<branches>:<armed>` and moves 99:98 to
  101:100 for the two new armed branches.

## 3. Non-goals (OUT)
- **N1.** A NEW check number. This reuses `fail 20`, whose subject is already "the prompt path
  ordered inside its OWN section". A new number costs a number and buys a second name for one
  question.
- **N2.** Asserting anything about WHICH probes run. That is unit 1's N1 and the same
  `two-answers-to-one-question` class: a gate enumerating the probe list becomes a third carrier of
  it, and the one that reds when the kickoff engine legitimately changes.
- **N3.** Ordering against check 18. That check grades the FIRST `--preflight` against the FIRST
  `/session-kickoff` across the whole file and is deliberately blind to the second start path — the
  reason check 20 exists at all. This arm lives inside the section slice, like its siblings.

## 4. Design
Check 20 already slices the prompt section heading-to-heading into `$psec` with awk, emitting
`<line-within-section>\t<text>`, then locates three ordered steps by first occurrence and compares
line numbers. This arm is a fourth locator and one more comparison in that same block — no new slice,
no new traversal.

The vacuity guard is not optional and is the half that matters. Check 20's existing third arm exists
because two comparisons against an empty string are green: if the locator disappears, an ordering
check silently passes over nothing. So an absent `RUN the orientation probes` is its own refusal,
distinct in text from the ordering refusal, and the test arm asserts the ordering message is NOT
emitted in that case.

### Alternatives rejected
- **A whole-file grep for the literal.** Green whether or not the line sits in the prompt section, and
  green if a second start path later carries it instead. The section slice is the point.
- **Asserting the probe step precedes `**Preflight**` instead of the write.** True but weaker: the
  defect is orientation landing after the ROSTER is authored, and step 3 is where that happens.

## 6. Acceptance criteria
- **AC1.** With `RUN the orientation probes` moved after step 3 in a scratch copy, the leg REDS with
  the ordering message naming both line numbers. Observed by staging the break, not asserted.
- **AC2.** With the literal removed entirely, the leg REDS with the VACUITY message, and the ordering
  message is absent from that output. Both halves asserted — `hit` on the first, `miss` on the second.
- **AC3.** On the unmodified tree `bash tools/unattended/check-unattended.sh` exits 0, and check 20's
  three pre-existing arms in `tools/unattended/check-unattended.test.sh` still pass.
- **AC4.** `python3 tools/memory-tree/check-arms.py --check` exits 0 with the bumped floor, so both
  new branches are armed rather than pinned as unarmed.
- **AC5.** THE SECTION SLICE IS OBSERVABLE. With `RUN the orientation probes` deleted from the prompt
  section and re-added under a DIFFERENT `## ` heading of
  `tools/unattended/SKILL.template.md`, the leg still REDS with the vacuity message. AC1–AC4 are all
  satisfied by the whole-file grep §4 rejects, so without this criterion the design decision §4 calls
  "the point" is untested — a gate whose stated rationale nothing observes is the could-not-fail shape
  one level up. This is the criterion that distinguishes the two implementations.

## 7. Gates
`bash tools/unattended/check-unattended.sh` · `bash tools/unattended/check-unattended.test.sh` ·
`python3 tools/memory-tree/check-arms.py --check` · `bash tools/run-gates/run-gates.sh` at the push
boundary.

## 8. Open questions
None.

## 9. Revision log
- rev-1 · 2026-08-27 · authored during the run, unreviewed by definition (M4).
- rev-2 · 2026-08-27 · AC3 named no backticked witness and hygiene check 12 refused it at the
  pre-commit boundary. Rewritten to name `check-unattended.sh` and its sibling `.test.sh` explicitly.
  The gate caught a spec defect this run wrote, which is the acceptance-witness rule doing its job.
- rev-3 · 2026-08-27 · round-1 spec-audit fold, F1 (high). AC1-AC4 were ALL satisfied by the
  whole-file grep §4 explicitly rejects, so the section-slice decision §4 calls "the point" was
  unobservable — the gate's own rationale went untested. AC5 added as the discriminating case: the
  literal moved to another `## ` section must still RED.
- rev-4 · 2026-08-27 · built and landed on main at ded17252 with its ARMS 1-OF-3 OBSERVED, which is
  a real gap and is recorded rather than rounded up. AC1 OBSERVED: with the probe step moved below
  the write, the leg emitted the ordering refusal. AC2 and AC5 UNOBSERVED — the run was landing
  when they were still executing. AC5 is the costly one: it is the only criterion separating this
  section-scoped gate from the whole-file grep 4 rejects, so the design decision remains untested.
  AC4 OBSERVED: `check-arms.py --check` exit 0 at the bumped 101:100 floor, after it REFUSED the
  first attempt for asserting a PREFIX of the failure text rather than the text itself.
  A prior observation attempt ran 45 minutes against a clone of HEAD where this unit was
  uncommitted, so the arm under test did not exist and all three reported hit=0 — indistinguishable
  from a broken arm. The probe now asserts the locator is PRESENT in the checker under test,
  because the liveness check could not: 'the clean tree emits neither message' is true both when
  the arm is correctly silent and when it is absent.
- rev-5 · 2026-08-27 · ALL THREE ARMS NOW OBSERVED. rev-4's claim that AC2 and AC5 were unobserved
  was PREMATURE and is corrected here rather than left standing. AC5 PASSED: the literal moved to
  another `## ` heading still produced the vacuity refusal, so the section slice is observable and
  the design decision 4 calls "the point" is tested. AC2 initially reported FAIL, and that was my
  interference, not the arm: its output was 313 bytes ending mid-run at check 9 against 2835 for a
  completed arm, because an orphan-reap I ran excluded PIDs and the string `u2arms` while that
  checker appears as a bare relative path containing neither. Re-run alone and uninterrupted it
  emitted the vacuity refusal, 2835 bytes, one hit. The lesson is already written down and was not
  applied: match a reap on the script PATH, never on a keyword the checking command itself carries.

## 10. Reuse audit
**The seam extended.** Check 20's own `$psec` slice in `tools/unattended/check-unattended.sh`, and
its three existing arms in the sibling `.test.sh` — including the vacuity arm this unit copies the
shape of. Nothing new is built; a fourth locator joins three.

**Recall probe.** Terms: `unattended check twenty prompt path section slice ordering vacuity guard
arms floor fail call site test arm`. It returned the `TOOL-aPromptedMandate-5` review thread that
created check 20 and recorded WHY it is section-scoped rather than file-scoped — which is N3.

**Map probe.** `reuse_lookup.py "assert one documented step precedes another inside a section slice"`
returned no symbol-level seam; the seam is an awk block in one shell script, below the granularity
the map indexes.

**Staleness.** `ARMS_FLOORS` was read from `.memory-tree.conf` at writing time and stands at
`tools/unattended/check-unattended.sh:99:98`. Verify before bumping — another node landing a `fail`
call site moves it, and this build already merged ten such commits.
