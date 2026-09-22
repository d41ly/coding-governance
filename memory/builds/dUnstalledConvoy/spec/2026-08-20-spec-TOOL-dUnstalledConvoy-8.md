# TOOL-dUnstalledConvoy-8 — M6's default inverts to parallel-on-proof, and the directive stops naming the opposite of its own handle

**Status:** CLOSED · rev-3 · 2026-08-21 · node d · Tier-2 · base 2dc9df35 · streams tooling · ratified 2026-08-20

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-22-review-TOOL-aBoundedVerdict-1-merge.md](../../aBoundedVerdict/reviews/2026-08-22-review-TOOL-aBoundedVerdict-1-merge.md) | diff-review | TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-2 TOOL-aBoundedVerdict-13 TOOL-aBoundedVerdict-19 TOOL-aBoundedVerdict-22 PLAY-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-3 TOOL-dUnstalledConvoy-4 TOOL-dUnstalledConvoy-5 TOOL-dUnstalledConvoy-6 TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-9 TOOL-dUnstalledConvoy-10 TOOL-dUnstalledConvoy-11 TOOL-dUnstalledConvoy-12 TOOL-aShardedFloor-4 |
| [2026-08-21-build-TOOL-dUnstalledConvoy-11-1-acceptance-ledger.md](../build/2026-08-21-build-TOOL-dUnstalledConvoy-11-1-acceptance-ledger.md) | journal | TOOL-dUnstalledConvoy-11 PLAY-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-3 TOOL-dUnstalledConvoy-4 TOOL-dUnstalledConvoy-5 TOOL-dUnstalledConvoy-6 TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-9 TOOL-dUnstalledConvoy-10 |
| [2026-08-21-build-TOOL-dUnstalledConvoy-7-1-parallelism-criteria.md](../build/2026-08-21-build-TOOL-dUnstalledConvoy-7-1-parallelism-criteria.md) | journal | TOOL-dUnstalledConvoy-7 |
| [2026-08-20-review-TOOL-dUnstalledConvoy-1-1.md](../reviews/2026-08-20-review-TOOL-dUnstalledConvoy-1-1.md) | spec-audit | PLAY-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-3 TOOL-dUnstalledConvoy-4 TOOL-dUnstalledConvoy-5 TOOL-dUnstalledConvoy-6 TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-9 TOOL-dUnstalledConvoy-10 TOOL-dUnstalledConvoy-11 TOOL-dUnstalledConvoy-12 |
| [2026-08-21-review-TOOL-dUnstalledConvoy-1-12-cumulative.md](../reviews/2026-08-21-review-TOOL-dUnstalledConvoy-1-12-cumulative.md) | diff-review | PLAY-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-3 TOOL-dUnstalledConvoy-4 TOOL-dUnstalledConvoy-5 TOOL-dUnstalledConvoy-6 TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-9 TOOL-dUnstalledConvoy-10 TOOL-dUnstalledConvoy-11 TOOL-dUnstalledConvoy-12 |
| [2026-08-21-review-TOOL-dUnstalledConvoy-1-12-fix.md](../reviews/2026-08-21-review-TOOL-dUnstalledConvoy-1-12-fix.md) | diff-review | PLAY-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-3 TOOL-dUnstalledConvoy-4 TOOL-dUnstalledConvoy-5 TOOL-dUnstalledConvoy-6 TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-9 TOOL-dUnstalledConvoy-10 TOOL-dUnstalledConvoy-11 TOOL-dUnstalledConvoy-12 |
| [2026-08-21-review-TOOL-dUnstalledConvoy-1-12-lib-fix.md](../reviews/2026-08-21-review-TOOL-dUnstalledConvoy-1-12-lib-fix.md) | diff-review | PLAY-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-3 TOOL-dUnstalledConvoy-4 TOOL-dUnstalledConvoy-5 TOOL-dUnstalledConvoy-6 TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-9 TOOL-dUnstalledConvoy-10 TOOL-dUnstalledConvoy-11 TOOL-dUnstalledConvoy-12 |
| [2026-08-21-review-TOOL-dUnstalledConvoy-1-12-round3-fix.md](../reviews/2026-08-21-review-TOOL-dUnstalledConvoy-1-12-round3-fix.md) | diff-review | PLAY-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-3 TOOL-dUnstalledConvoy-4 TOOL-dUnstalledConvoy-5 TOOL-dUnstalledConvoy-6 TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-9 TOOL-dUnstalledConvoy-10 TOOL-dUnstalledConvoy-11 TOOL-dUnstalledConvoy-12 |

<!-- /gen:spec-records -->

## 1. Goal

The directive `parallel-when-disjoint` points at M6, whose first sentence is "Sequence is the default;
parallelism is a claim you substantiate". A run obeying the directive and a run obeying the section
it points at do opposite things, and every observed unattended run has done the sequential one. This
unit inverts the default so the handle and the rule agree, conditional on
`TOOL-dUnstalledConvoy-7`'s verdict.

## 2. Scope (IN)

- **S1** — M6's framing sentence inverts. Concurrent dispatch becomes REQUIRED for a pair whose
  disjointness is proven, and sequence becomes the fallback for everything else.
- **S2** — M6's three conditions are kept VERBATIM. They were corrected once already, when condition
  3's build-README clause was found vacuous, and this unit changes the obligation attached to them,
  never the conditions themselves.
- **S3** — the written-path-lists requirement stays as the precondition and keeps its current closing
  sentence: work whose two path lists cannot be written down is not known to be disjoint and is
  sequenced. This is what stops the inversion becoming "parallelise by default and hope".
- **S4** — M6 states that the proof is RECORDED, pointing at the verb `TOOL-dUnstalledConvoy-9`
  builds rather than describing it, per M1's rule. **That verb now lands BEFORE this unit** in the
  2026-08-20 reorder, so the pointer is live on arrival. Review fold: M6. In the first draft the verb
  landed seven passes later, and M7 makes a run re-read the method WHOLE at every pass boundary, so
  the run itself would have read a rule pointing at a flag no reader could invoke.
- **S5** — the Skill's directive table cell for `parallel-when-disjoint` is re-read after the change
  to confirm it still NAMES the rule rather than restating it. If the cell became accurate only by
  accident, it is corrected in the same commit.
- **S6** — **CONDITIONAL.** If `TOOL-dUnstalledConvoy-7` records E3 or E4 as anything other than
  `cleared` — `failed` AND `not-observed` both — this unit does not ship the inversion. It ships the
  recorded loss instead, and its own status goes `WONTDO` with a pointer to the record, which is an
  amendment under `TOOL-dUnstalledConvoy-4` and owes a `rescope` row. Review fold: M1, because the
  measurement's vocabulary is three-valued and a two-valued predicate lets an UNMEASURED criterion
  ship the inversion — the exact thing the owner's fork-B answer refused. Review fold: H14 for the
  other half: the authority and the verb now land at positions 2 and 3 against this unit's 7, so the
  amendment row is writable when this branch needs it. In the first draft they landed at 7 and 8
  against this unit's 3, and the run's only legal moves were to park — the recorded stall — or to flip
  a status with no record, which the roster check then redded for the rest of the build.
- **S7** — the result is measured against M1's stated budget before commit. Three lines of the seven
  available are this unit's share.

## 3. Non-goals (OUT)

- Changing M6's three conditions. S2 is explicit, and the conditions are the part that was already
  measured and corrected.
- Changing the fan-out or concurrency CEILINGS. M6 closes by saying it governs WHICH work is parallel
  and never HOW MUCH, and the ceilings belong to the review protocol. That division is preserved.
- Making a pass kind other than the five M6 names dispatchable. The pass set is closed and stays
  closed.
- The recording verb and its check. Those are units 10 and 11.
- Shipping an inversion the measurement did not support. S6 is the whole of this non-goal.

## 4. Design

### The change is a framing sentence and an obligation, not a rule set

M6 today reads, in order: a framing sentence declaring sequence the default, which shares its LINE
with the opening of the first condition; three conditions hard-wrapped as one continuing paragraph
rather than a numbered list; a closing sentence on unwritable path lists; a paragraph recording that condition 3 was
once vacuous; and a pointer to where the ceilings live.

The inversion rewrites the first of those five and adds the recording pointer. Everything else is
kept. This matters for the line budget in §4's last sub-head and it matters for correctness: the
conditions are the measured part of the section, and a unit that rewrote them would be discarding
the only part of M6 that has already survived a review.

### Why the obligation must be REQUIRED and not ENCOURAGED

An encouraged parallelism is what the tree has today. The directive already exists, already binds
every unattended run, and has never produced a concurrent dispatch. A rule that a run may follow and
has never followed is indistinguishable from no rule, and the owner's report is precisely that
observation.

So S1's obligation is mandatory where the proof exists. The proof is what bounds it: a pair whose
path lists cannot be written down is sequenced, and writing them down is work, so the rule cannot
be satisfied by asserting disjointness.

### Line budget

`memory/guides/BUILD-METHOD.md` has seven lines of headroom against M1's stated 290, shared with
`TOOL-dUnstalledConvoy-4`, which budgets four. This unit's share is three.

The inversion itself is close to neutral — one framing sentence replaced by another of similar
length. S4's pointer is the addition. If the pair overruns, the disposition is a fork to the owner,
because M1's budget is a stated constraint of a governance carrier and raising it is an owner turn.
This unit does not get to raise the budget of the file that states its own limits.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/memory-tree/BUILD-METHOD.template.md` | M6's framing sentence and S4's pointer |
| `memory/guides/BUILD-METHOD.md` | the render of the same |
| `tools/unattended/SKILL.template.md` and its render | S5, only if the cell needs it |

### Alternatives rejected

- **Inverting now and measuring alongside.** Offered to the owner and declined. The original refusal
  refused to ship on argument, and shipping on argument now would discard the thing that refusal
  bought.
- **Leaving M6 alone and making the directive binding on proof.** Offered and declined. It leaves the
  handle pointing at a section whose first sentence says the opposite, which is the drift that
  produced the observation.
- **Deleting the directive.** Rejected: the owner's report asks for parallelism to be required, not
  abandoned.

## 5. Production-readiness checklist

- security — N/A — documentation. The write-set proof is the safety mechanism and unit 10 owns it.
- perf / scale — this unit is the one whose whole subject is wall-clock, and it buys nothing by
  itself. Units 10 and 11 make the obligation checkable; unit 7 decides whether it is sound.
- a11y — N/A — documentation.
- i18n — N/A — documentation.
- error / empty / loading states — N/A — documentation.
- observability — S4's pointer is what makes a parallel dispatch leave a trace.
- risks (concurrency, data-loss, rollback hazards) — the live risk is a run parallelising a pair
  whose disjointness it asserted rather than proved. S3 is the bound; unit 11 is the detector.
- testing + left-shift gates — the method carriers check and the kit-version marker check read this
  file. An open row records that the marker remedy names too few carriers, so the marker population
  is derived from the markers rather than from that message.
- migration / rollback — none. A run reading the old text sequences, which is what runs already do.
- user docs — the Skill's directive table, S5.

## 6. Acceptance criteria

- **AC1** — M6's framing sentence requires concurrent dispatch for a proven-disjoint pair, verified by
  `grep` finding the new sentence and not the old one in `memory/guides/BUILD-METHOD.md`.
- **AC2** — M6's three conditions are unchanged, verified as a CONTENT assertion rather than a diff:
  extract the paragraph from `memory/guides/BUILD-METHOD.md`, strip newlines, and assert the substring
  from the conditions' opening through their closing sentence is byte-identical to the same substring
  at BASE. Review fold: M16. There is no numbered list to diff — the framing sentence this unit
  REPLACES shares one hard-wrapped line with the opening of condition 1, and conditions 2 and 3 are
  continuation lines of that same paragraph, so any correct implementation changes that line and a
  diff assertion would fail on every valid edit.
- **AC3** — `bash tools/memory-tree/check-method-carriers.sh` stays green, and the template and its
  render agree.
- **AC4** — `wc -l` on `memory/guides/BUILD-METHOD.md` shows this unit's own edit within the
  three-line share S7 states, measured at THIS unit's commit. Review fold: M15. The joint file-wide
  assertion moved to `TOOL-dUnstalledConvoy-4` AC9, which is the later of the two method-editing units
  in the reordered plan and can therefore actually take the observation; a criterion naming a joint
  state that does not exist at its own pass is not an observation that proves this change.
- **AC5** — The Skill's `parallel-when-disjoint` cell names the rule and does not restate it, read
  after the change.
- **AC6** — If unit 7 recorded a FAILED criterion, this unit's spec status is `WONTDO` with the
  record as its tail pointer, and a `rescope` row exists. AC1 through AC5 are then vacuous by
  construction and the build says so rather than reporting them green.

## 7. Gates

`method carriers` · `kit version markers` · `memory-tree hygiene` · `unattended kit gate` · the full
bar at the push boundary.

## 8. Open questions

- **F1 — RESOLVED (agent, 2026-08-20, delegated): the inversion binds EVERY build, attended or not. M6's first line already says it is binding for any build of more than one pass, the disjointness proof is the same work either way, and an attended session that writes two path lists has earned the same concurrency. A rule that behaves differently by run mode is two rules. Recorded as the wider blast radius it is, and surfaced in the wrap-up because the owner may want the narrower reading.**

  The question this settles: does the inversion bind an ATTENDED build too? M6 is binding for any build of more than
  one pass, attended or not, and its first line says so. Inverting it therefore changes what an
  attended session must do, which is a wider blast radius than the owner's report asked for. Options:
  invert M6 for all builds; or scope the obligation to runs under a mandate, leaving attended builds
  on the current default. **Recommendation: invert for all builds.** The proof requirement is the
  same work either way, an attended session that writes two path lists has earned the same
  concurrency, and a rule that behaves differently by run mode is two rules. This is a scope
  question the owner may want; it is raised here rather than resolved silently.

## 9. Revision log

- rev-3 · 2026-08-21 · SHIPPED, on the measurement rather than instead of it: the verdict token reads
  `cleared`, so S6's condition never fired. The three conditions survive BYTE-IDENTICAL to BASE,
  asserted as AC2's content comparison rather than a diff — the framing sentence shares its line with
  the opening of condition 1, so any correct edit changes that line and a diff assertion would fail on
  every valid one. ONE line of the two available, 288 to 289 of M1's 290. S5 found the directive cell
  inaccurate rather than accidentally right: it called M6 a `default` and M6 no longer has one, so the
  cell now names the obligation.
- rev-2 · 2026-08-20 · folded the spec audit: M6 (the pointer target now lands earlier, per the reorder),
  M1 and H14 (S6 treats an unmeasured criterion as non-shipping, and the amendment row is writable at
  this unit's new position), M16 (AC2 becomes a content assertion, because the conditions are not a
  numbered list), M15 (the joint budget observation moves to the later method-editing unit).
- rev-1 · 2026-08-20 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "the build method's parallelism rule and the directive
that points at it"` returns the `build-method` dossier and the `unattended` affordance seam. The seam
extended is M6 itself, together with the directive registry constant that already names it — no new
carrier and no new pointer type.

`python tools/memory-recall/query.py "why is sequence the default for build passes and what would
have to be true to invert it" --terms "M6 parallelism sequence default disjoint write set condition
three shared mutable record directive handle pointer inversion"` returns the record correcting M6's
condition 3 as vacuous, the parallelism verdict, and the method-ownership record placing M6 in the
memory-tree kit. The first of those is why S2 keeps the conditions verbatim: they are the part of
this section that has already been measured and fixed.

Recall terms used: M6 parallelism sequence default disjoint write set condition three shared mutable
record directive handle pointer inversion.
