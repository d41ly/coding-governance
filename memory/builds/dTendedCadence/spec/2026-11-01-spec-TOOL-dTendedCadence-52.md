# TOOL-dTendedCadence-52 — the security review's record lands through the one landing seam, so a `security-` landing is the same four lines a period landing is

**Status:** DEFERRED · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 21 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |
| [2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md) | spec-audit | TOOL-dTendedCadence-56 TOOL-dTendedCadence-55 TOOL-dTendedCadence-57 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 43 of `reviews/2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md`,
HIGH, item H5. Unit 48 S24 defines one landing grammar, key, base and readings digest with
re-derivation (spec-48:107-110), and never names unit 39's security landing, which files the
three-line text `land maintenance-record security-<head12>`, `base:`, `security-head:` with no digest
(spec-39 S2, §4 "The intake", :34-40, :62-71). A patch build built to S24 refuses it, so the review's
head is never committed and every review falls back to the period start. TOOL-dTendedCadence-49 and
-50 replace S24's grammar with one carried payload that names no family. This unit puts the review's
landing on that seam, so the patch build reads one grammar for every record family.

## 2. Scope (IN)

- **S1** — The call. Once unit 13 S6 has written the review's record under `security-<head12>`
  (unit 39 S1), `security_review.py` calls `write_record_landing(root, <written path>,
  "security-<head12>", <head>, "security-review")` (TOOL-dTendedCadence-49 S1), and files no text of
  its own. The three-line text of unit 39 §4 and its function `write_review_landing` are not built.
  A raise prints its line and exits 1, unit 39 S2's hand-over. Observed by AC1.
- **S2** — The landing. The patch build lands the review's intake with `maintenance.py land`
  (TOOL-dTendedCadence-50), as it lands a period record: the payload is the record unit 13 S6 wrote,
  its `**Base:**` the head and its `security-head:` line the head, so nothing is re-derived and no
  family is special-cased. Observed by AC2.
- **S3** — The docs. `help/maintain.md`'s section "The security review" states that the review's
  record lands through the same four lines as Maintain's. Observed by AC3.

## 3. Non-goals (OUT)

- The review's key and its base read: unit 39 S1 and S3, unchanged.
- The landing seam and verb: TOOL-dTendedCadence-49 and -50.
- A landing of every family of `RECORD_KEY_FAMILIES` as one arm: id 24, TOOL-dTendedCadence-59.

### Edges

- **consumes-from** `TOOL-dTendedCadence-48` — S24's single landing grammar, which named no security landing; this unit puts that landing on the grammar that replaces it
- **consumes-from** `TOOL-dTendedCadence-49` — `write_record_landing`, the seam the review's landing calls
- **consumes-from** `TOOL-dTendedCadence-39` — `security_review.py`'s landing (S2) and its `security-<head12>` key, whose filing this unit routes through the seam
- **hands-off** `TOOL-dTendedCadence-71` — S1's security landing through the one seam, to which that unit corrects spec-39 in place (review id 28)
- **hands-off** `TOOL-dTendedCadence-74` — AC2's clones and AC3's section probe, repaired by the minors batch (review ids 11, 20)

## 4. Design

### Evidence

- Spec-39 S2 re-writes the review's record "from the text alone" with stdin `{"read": [0, 0],
  "readings": [], "fields": {"security-head": "<head>"}}` (§4, :69-71).
- Spec-48 S24 consumes unit 39 only for S17 (spec-48:180), so its landing never names a `security-`
  key.
- TOOL-dTendedCadence-50 S3 checks the key with `derive_record_family`, which admits `security-`
  keys once unit 39 S1 adds the family.

### Inventory

Minted: nothing. `security-review` is unit 39's filer value, passed through.

### Files touched (estimate)

- `tools/drift-audit/security_review.py`: S1
- `tools/drift-audit/selftest.py`: the cases of §6
- `help/maintain.md`: S3

### Alternatives rejected

- **Name both grammars in the patch build.** Two answers to one question, the class item M1 of the
  same report names; one carried payload makes the family irrelevant to the landing.

## 5. Production-readiness checklist

- security — the review's record leaves the node by the seam's ref, which the publishing boundary
  scans; its text carries two shas and a digest and no finding text.
- perf / scale — one landing per completed review, `weekly` by default.
- error / empty / loading states — a refused push or filing exits 1 and the next wake re-reviews the
  range, as unit 39 S2 states.
- observability — the seam's line, `maintain — security-<head12> · security-review · landing
  <commit12> · <answer>`.
- risks — a review re-run on a later UTC day writes its record under a new dated path, and so files a
  new landing for one head; the landed records agree on `security-head`.
- testing — the criteria of §6.
- migration — N/A — no review record exists at base.
- user docs — `help/maintain.md`, S3.

## 6. Acceptance criteria

The fixture is unit 39's two-run chain, its filer a recording stub, with a scratch bare remote added
as the fixture's one remote.

- **AC1** — When a completed review runs in the fixture, the recorded text is four lines opening
  `land maintenance-record security-<H12>` and carrying `payload:` and `sha256:`, and `git grep -n
  "write_review_landing" -- tools/drift-audit/` prints nothing.
  Red when: the review files its own grammar, or a second landing filer exists.
- **AC2** — When the fixture lands the first run's text with `python maintenance.py land` in a second
  clone and commits the path, the second run's range line names base `H1`.
  Red when: the security landing is refused, so the second run's base is the period start.
- **AC3** — When `grep -n "four lines\|maintenance.py land" maintain.md` runs in `help/`, the section
  "The security review" matches.
  Red when: the page still describes a three-line landing.

## 7. Gates

`drift-audit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 · unit 39's two-run chain landed through `maintenance.py land` in a second clone, staged against the three-line security text · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 43 (HIGH, item H5) of the round-1 spec
  audit of units 35 to 48.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 spec audit of units 49 to 59 declare toward this unit (units 71, 74); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is TOOL-dTendedCadence-49's `write_record_landing`, called with the review's own
filer, and TOOL-dTendedCadence-50's verb, unchanged. `python tools/codebase-map/reuse_lookup.py
"carry a written record to another node under a git ref and land it"` named no second landing
filer in the tree, so the review takes the one seam rather than keeping its own.

Recall terms used: `python tools/memory-recall/query.py "how does a records-only patch build land a
maintenance record the walk wrote" --terms "records-only patch intake landing maintenance record refs
gov ref parentless commit digest re-derive"`
