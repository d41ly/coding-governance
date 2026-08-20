# TOOL-dUnstalledConvoy-8 — M6's default inverts to parallel-on-proof, and the directive stops naming the opposite of its own handle

**Status:** SPECCED · rev-1 · 2026-08-20 · node d · Tier-2 · base 2dc9df35 · streams tooling

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
  builds rather than describing it, per M1's rule.
- **S5** — the Skill's directive table cell for `parallel-when-disjoint` is re-read after the change
  to confirm it still NAMES the rule rather than restating it. If the cell became accurate only by
  accident, it is corrected in the same commit.
- **S6** — **CONDITIONAL.** If `TOOL-dUnstalledConvoy-7` records E3 or E4 as FAILED, this unit does
  not ship the inversion. It ships the recorded loss instead, and its own status goes `WONTDO` with a
  pointer to the record, which is an amendment under `TOOL-dUnstalledConvoy-4` and owes a `rescope`
  row.
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

M6 today reads, in order: a framing sentence declaring sequence the default; three numbered
conditions; a closing sentence on unwritable path lists; a paragraph recording that condition 3 was
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
- **AC2** — M6's three conditions are byte-identical to their text at BASE, verified by
  `git diff 2dc9df35 -- memory/guides/BUILD-METHOD.md` showing no change inside the numbered list.
- **AC3** — `bash tools/memory-tree/check-method-carriers.sh` stays green, and the template and its
  render agree.
- **AC4** — `wc -l` on `memory/guides/BUILD-METHOD.md` is at or under M1's stated line budget after
  this unit AND `TOOL-dUnstalledConvoy-4` have both landed, with the figure in the commit message.
- **AC5** — The Skill's `parallel-when-disjoint` cell names the rule and does not restate it, read
  after the change.
- **AC6** — If unit 7 recorded a FAILED criterion, this unit's spec status is `WONTDO` with the
  record as its tail pointer, and a `rescope` row exists. AC1 through AC5 are then vacuous by
  construction and the build says so rather than reporting them green.

## 7. Gates

`method carriers` · `kit version markers` · `memory-tree hygiene` · `unattended kit gate` · the full
bar at the push boundary.

## 8. Open questions

- **F1 — does the inversion bind an ATTENDED build too?** M6 is binding for any build of more than
  one pass, attended or not, and its first line says so. Inverting it therefore changes what an
  attended session must do, which is a wider blast radius than the owner's report asked for. Options:
  invert M6 for all builds; or scope the obligation to runs under a mandate, leaving attended builds
  on the current default. **Recommendation: invert for all builds.** The proof requirement is the
  same work either way, an attended session that writes two path lists has earned the same
  concurrency, and a rule that behaves differently by run mode is two rules. This is a scope
  question the owner may want; it is raised here rather than resolved silently.

## 9. Revision log

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
