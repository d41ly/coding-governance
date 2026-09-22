# TOOL-dUnstalledConvoy-29 — a leg's subject cannot be flipped silently, because value correctness is not machine-decidable

**Status:** CLOSED · rev-2 · 2026-08-24 · node d · Tier-2 · base b164a296 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-24-build-TOOL-dUnstalledConvoy-26-2-acceptance-ledger.md](../build/2026-08-24-build-TOOL-dUnstalledConvoy-26-2-acceptance-ledger.md) | journal | TOOL-dUnstalledConvoy-26 TOOL-dUnstalledConvoy-27 TOOL-dUnstalledConvoy-28 TOOL-dUnstalledConvoy-30 TOOL-dUnstalledConvoy-31 TOOL-dUnstalledConvoy-32 |
| [2026-08-24-build-TOOL-dUnstalledConvoy-29-1-red-first.md](../build/2026-08-24-build-TOOL-dUnstalledConvoy-29-1-red-first.md) | journal | — |
| [2026-08-24-review-TOOL-dUnstalledConvoy-26-closing-diff.md](../reviews/2026-08-24-review-TOOL-dUnstalledConvoy-26-closing-diff.md) | journal | TOOL-dUnstalledConvoy-26 TOOL-dUnstalledConvoy-27 TOOL-dUnstalledConvoy-28 TOOL-dUnstalledConvoy-30 TOOL-dUnstalledConvoy-31 TOOL-dUnstalledConvoy-32 TOOL-dUnstalledConvoy-33 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-dUnstalledConvoy-26`'s cross-check grades that `subject` is PRESENT and that the descriptor and
the manifest AGREE. Both hold when every leg says `repo` and when every leg says `kit`, so a wrong
population passes every acceptance criterion that spec has.

Whether a given leg's subject is the RIGHT one is a judgement about what the leg reads. No predicate
decides it. What a machine can do is make CHANGING it deliberate.

## 2. Scope (IN)

- **S1 — a leg's `subject` is ratcheted.** A committed pin records the subject of every known leg; a
  value that differs from its pin reds until the pin moves in the same commit.
- **S2 — the pin is DERIVED into the check, not hand-listed.** It is generated from the descriptors,
  so adding a leg adds a pin row and nothing goes stale by omission.
  **AMENDED rev-2: generated from `tools/gate-legs.json`, not from the descriptors.** Section 7h
  already asserts the two agree in both directions, so pinning the manifest pins every descriptor
  leg transitively — and it also covers the `[[exempt_leg]]` rows, which no descriptor claims and a
  descriptor-derived pin would have left free to move. The narrower population was the weaker one.
- **S3 — the refusal names the leg, both values, and what moving the pin means** — that a leg moving
  from `repo` to `kit` leaves the automatic bar.
- **S4 — the check states what it does NOT decide**, in its own header: it grades CHANGE, never
  correctness, and a green row is not evidence any subject is right.
- **S5 — every change lands with its arm, observed failing first.**

## 3. Non-goals (OUT)

- Deciding correctness. It is a review judgement and S4 says so rather than implying otherwise.
- The presence and agreement checks — `TOOL-dUnstalledConvoy-26` owns those and they stay.
- Any assignment. `TOOL-dUnstalledConvoy-30` owns the one assignment known to be wrong.

## 4. Design

This is the same shape as the repo's other ratchets: a value nobody can verify automatically is at
least prevented from moving unobserved. The parent unit's checks answer "is there a subject, and do
the two spellings agree"; this one answers "did somebody change one without saying so".

S2 matters because the alternative — a hand-kept pin — is a second list of the legs, and this build
has already paid twice for deriving a population one way while its consumer derived it another.

S4 is not decoration. A check named for subjects, sitting green on a bar, reads to everyone who did
not write it as evidence the subjects are right. It is not, and the header is where that gets said.

## 5. Production-readiness checklist

- **security** — a leg cannot leave the automatic bar without a recorded, reviewed change.
- **perf/scale** — one derivation and one comparison per leg.
- **a11y / i18n** — N/A.
- **error/empty/loading states** — a leg with no pin is a NEW leg and reds until pinned; that is the
  intended reading, and an unpinned leg passing would be the hole.
- **observability** — S3.
- **testing/gates** — govkit's selftest, plus the full bar.
- **migration/rollback** — the first pin is generated from the tree as it stands.
- **help/ docs** — the check's own header, per S4.

## 6. Acceptance criteria

- **AC1** — flipping one leg's `subject` without moving its pin REDS, naming the leg and both values,
  observed in `tools/govkit/selftest.py`.
- **AC2** — moving the pin in the same commit passes, observed in `tools/govkit/selftest.py`.
- **AC3** — a NEW leg with no pin reds rather than passing, observed in `tools/govkit/selftest.py`.
- **AC4** — the pin is derived from the descriptors, asserted by regenerating it and comparing,
  observed in `tools/govkit/selftest.py`.
- **AC5** — the check's header states it grades change and not correctness, observed by `grep`.
- **AC6** — every arm was observed RED before its fix, observed in
  `2026-08-24-build-TOOL-dUnstalledConvoy-29-1-red-first.md`.
- **AC7** — the full bar is green, observed by `bash tools/run-gates/run-gates.sh`.

## 7. Gates

`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`.

## 8. Open questions

- **F1 — ratchet, or try to decide correctness?** RESOLVED (agent, 2026-08-24): ratchet. Correctness
  needs to know what a leg reads when it fails, which no predicate over a descriptor can see. This
  build has twice written a predicate over a population and discarded it on measurement; a third is
  not the answer.

## 9. Revision log

- rev-1 · 2026-08-24 · promoted from round 2's NON-CONVERGENT spec audit, which found that all-`repo`
  and all-`kit` both satisfy every acceptance criterion the parent spec carries.
- rev-2 · 2026-08-24 · S2 amended at build time: the pin derives from the leg MANIFEST rather than
  from the descriptors, because the manifest is the superset and the exempt legs are exactly the
  rows the narrower derivation would have missed. Built and CLOSED.

  Two arms were sharpened after the red-first run rather than before it, and the reason is worth
  keeping. `AC4: and the generated pin is exactly the derived population` and `AC2: and the moved
  pin records the new value` both PASSED against a build with no ratchet in it: the fixture's
  hand-written pin already held the bytes they asserted, so regeneration was never the thing being
  measured. Corrupting the pin first, and planting a stale row the regeneration must drop, made both
  discriminating. One arm remains non-discriminating BY CONSTRUCTION and is labelled `CONTROL`: an
  assertion that a correct tree is green cannot fail when the mechanism is absent, and it is kept
  because a ratchet that reds on a correct tree is the other way this fails.

## 10. Reuse audit

The repo already ratchets values nobody can verify — floors, cutoffs, pins — with the same
derive-then-compare shape. This adds a row to that family, not a new mechanism.
