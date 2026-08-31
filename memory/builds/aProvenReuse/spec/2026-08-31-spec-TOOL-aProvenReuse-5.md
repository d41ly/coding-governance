# TOOL-aProvenReuse-5 — the example-conf parity arm reaches bare presets

**Status:** CLOSED · rev-1 · 2026-08-31 · node a · Tier-1 · base 3bfc5e87 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-review-TOOL-aGradedMandate-1-closing-diff-review-round2.md](../../aGradedMandate/reviews/2026-08-31-review-TOOL-aGradedMandate-1-closing-diff-review-round2.md) | diff-review | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 TOOL-aGradedMandate-10 TOOL-aGradedMandate-11 TOOL-aProvenReuse-1 TOOL-aProvenReuse-2 |
| [2026-08-31-review-TOOL-aProvenReuse-1-diff-review-round2.md](../reviews/2026-08-31-review-TOOL-aProvenReuse-1-diff-review-round2.md) | diff-review | TOOL-aProvenReuse-1 TOOL-aProvenReuse-2 |
| [2026-08-31-review-TOOL-aProvenReuse-1-diff-review-round3.md](../reviews/2026-08-31-review-TOOL-aProvenReuse-1-diff-review-round3.md) | diff-review | TOOL-aProvenReuse-1 TOOL-aProvenReuse-2 |

<!-- /gen:spec-records -->

## 1. Goal

Make the shipped-example parity arm in `tools/memory-tree/check-memory-hygiene.test.sh` see every
adopter key the engine actually reads, not only the ones spelled `${NAME:-}`. Two live keys were
already through the hole, and `TOOL-aProvenReuse-1` added a third by the same route.

## 2. Scope (IN)

- **S1** — the arm's population becomes the UNION of its existing `${NAME:-}` derivation and a new
  one over bare presets matching `^[A-Z][A-Z0-9_]*_CUTOFF=` in the engine.
- **S2** — the new derivation carries its own non-empty assertion, on the same footing as the
  existing one, so a regex that stops matching cannot restore the blind spot silently.
- **S3** — `FORK_MARK_CUTOFF` and `REVIEW_VERDICT_CUTOFF` are declared in
  `tools/memory-tree/.memory-tree.conf.example`, each with what it gates and its grandfathering rule.

## 3. Non-goals (OUT)

- **N1** — widening the preset derivation past `_CUTOFF`. A bare `^[A-Z0-9_]+=` would sweep in every
  engine internal — the cap constants, `SPEC_CANON`, the shipped-version captures — and demand an
  adopter declare things the kit owns. `_CUTOFF` is the convention every date ratchet here follows.
- **N2** — changing what any cutoff DOES, or what its blank value means. This unit only makes two of
  them discoverable and the arm honest about its own population.
- **N3** — the same widening in sibling kits. `tools/unattended/` has its own conf-parity checks with
  their own shapes; whether they share this blind spot is a separate question nobody has measured.

## 4. Design

### Inventory

| Path | Change |
|---|---|
| `tools/memory-tree/check-memory-hygiene.test.sh` | S1, S2 — the second derivation and its assertion |
| `tools/memory-tree/.memory-tree.conf.example` | S3 — the two undeclared keys |

The union is built in one subshell so both streams reach a single `sort -u`, and the existing
exemption list keeps working against the merged population unchanged.

### Alternatives rejected

- **Declaring the two keys and stopping.** That is the instance, not the class. The arm would still
  be blind to the next bare preset, and the next one is how these two got in.
- **Rewriting the arm to parse the conf instead of the engine.** The arm's direction is deliberate:
  it asks what the ENGINE reads and demands the example declare it. Reversing that would let a key
  the engine dropped sit in the example forever.

### Rollout

One commit, with the two declarations, because the widened arm reds without them.

## 5. Production-readiness checklist

- **Security** — N/A. A self-test derivation over tracked files.
- **Performance** — one extra `grep -oE` over a file the arm already reads twice.
- **Error states** — S2's assertion covers the derivation returning nothing.
- **Observability** — the existing per-key failure message already names the missing key.
- **Testing** — the arm IS the test; AC1 and AC2 are its two directions.
- **Migration/rollback** — an adopter who re-pulls the example gains two documented keys, both
  blank, both meaning "off". No behaviour changes.

## 6. Acceptance criteria

- **AC1** — with the two keys absent from the example, `bash tools/memory-tree/check-memory-hygiene.test.sh`
  FAILS naming `FORK_MARK_CUTOFF` and `REVIEW_VERDICT_CUTOFF`. Observed before the declarations were
  written, which is the whole evidence that the widening reaches anything.
- **AC2** — with them declared, `bash tools/memory-tree/check-memory-hygiene.test.sh` exits 0 and
  reports a higher assertion count than before this unit, since the population grew.
- **AC3** — every `^[A-Z][A-Z0-9_]*_CUTOFF=` preset in `tools/memory-tree/check-memory-hygiene.sh`
  appears in the shipped example, checked by that same run rather than by eye.

## 7. Gates

`bash tools/memory-tree/check-memory-hygiene.test.sh` is the whole bar for this unit; it is the
`memory-hygiene self-test` leg, guarded on `tools/memory-tree/`, which this unit touches.
What no gate here checks: whether a future adopter key arrives under neither derivation — a third
spelling would be invisible again, and N1 records why the population is not simply widened to
everything.

## 8. Open questions

- **Q1 — is this Tier-1 or Tier-2?** The manifest assigns Tier-2 to a changed kit contract, and the
  shipped example is adopter-facing. **RESOLVED (agent, 2026-08-31, delegated):** Tier-1. Both keys
  are ALREADY live engine keys with live behaviour; the example was incomplete documentation of a
  contract that did not change. Nothing here adds a rule, moves a cutoff, or alters what a blank
  value means. The tier rule is about contract CHANGES, and this is a contract DISCLOSURE.

## 9. Revision log

- rev-1 · 2026-08-31 · authored after the code, and that order is a defect rather than a shortcut.
  M2's hard floor says never build a MISSING unit and that "I will spec it afterwards" is the same
  act with the record written last. What happened: the closing diff review surfaced the blind spot as
  finding F9, protocol §11 made it a strictly-beneficial discovery to ADOPT rather than park, and the
  fix went in during the same fold pass before this file existed. Recorded here rather than
  backdated, because a spec that claims to have preceded its code is worth less than one that says
  it did not.

## 10. Reuse audit

The seam is the parity arm that already exists at
`tools/memory-tree/check-memory-hygiene.test.sh:1483` — it already derives a population from the
engine, already holds a declared exemption list asserted in both directions, and already emits the
per-key failure message this unit needs. Nothing new is built: one additional derivation is unioned
into the population it already computes.

`python tools/codebase-map/reuse_lookup.py "checking that a shipped example config declares every
key the engine reads"` returned the `memory-tree-hygiene` affordance seam and `check_read_path` in
`corpus_ids.py`; the latter was inspected and REJECTED, since it classifies id and path corpora and
holds no conf-key reader.

Recall terms used: `reuse-first reuse audit spec section 10 seam recall probe terms directive waiver
silent unchecked machine-checked prose` — the set this build composed for its own question, reused
per M5's rule that the obligation is satisfied once for the SET rather than per spec.

Where a hit was STALE: none. The arm's current derivation and its exemption list were read at
`tools/memory-tree/check-memory-hygiene.test.sh:1476-1500` at writing time rather than taken from
the review's description of them.
