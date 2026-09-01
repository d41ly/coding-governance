# TOOL-dBriefedPass-1 — `plan_state` grades a spec by heading TITLE, not by ordinal

**Status:** SPECCED · rev-1 · 2026-09-01 · node d · Tier-2 · base 269dacae · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-prompt-TOOL-dBriefedPass-1.md](../prompts/2026-09-01-prompt-TOOL-dBriefedPass-1.md) | research | TOOL-dBriefedPass-2 TOOL-dBriefedPass-3 TOOL-dBriefedPass-4 TOOL-dBriefedPass-5 |

<!-- /gen:spec-records -->

## 1. Goal

Make the M2 classifier read a spec's sections by their HEADING TITLE rather than by their ordinal
number, so a Tier-1 spec — which legitimately omits `## 5. Production-readiness checklist` and
renumbers everything after it — is graded on the sections it actually has.

## 2. Scope (IN)

- **S1** — `plan_state` in `tools/unattended/unattended.sh` selects its four sections by title:
  `Scope`, `Acceptance criteria`, `Gates`, `Open questions`, each anchored as
  `^## [0-9]+\. <Title>`, which is the shape the sibling reader in
  `tools/memory-tree/check-memory-hygiene.sh` already uses at its lines 880, 939 and 1326.
- **S2** — the ordinal is still REQUIRED to be present and numeric; only its VALUE stops being read.
  A heading with no ordinal is not a canonical section and must not become one by this change.
- **S3** — a spec carrying two headings with the same title is a REFUSAL, not a last-one-wins merge.
  The ordinal previously made duplicates impossible to express; keying on the title removes that
  accident, and a silent merge would be a new could-not-fail shape introduced by the fix.
- **S4** — arms in `tools/unattended/unattended.test.sh` covering: a Tier-1 spec with a filled
  §5 Acceptance grading READY, a Tier-1 spec with an EMPTY §5 Acceptance grading THIN, a Tier-1 spec
  whose §7 Open questions carries an unresolved item grading FORKED, and a Tier-1 spec whose §8
  Revision log carries bullets NOT grading FORKED.
- **S5** — `tools/memory-tree/marker-contract.test.sh` and `tools/unattended/unattended.test.sh`
  both slice this function's body out of the shipped bytes; both keep passing.

## 3. Non-goals (OUT)

- The sibling reader in `check-memory-hygiene.sh` is NOT touched. It is already correct, and the
  point of this unit is to make the two agree by moving the wrong one.
- No new section is added to the spec canon, and no Tier-1 spec in the corpus is rewritten. The
  classifier moves to the corpus, never the corpus to the classifier.
- The case table that holds the two readers in agreement is not replaced with shared code. That is
  a larger refactor with its own cost and it is not what this defect needs.
- `--close`'s THIN term keeps its `SPEC_THIN_CUTOFF` date gating exactly as declared. This unit
  changes what THIN MEANS on a Tier-1 spec; it does not change which specs the term grades.

## 4. Design

### Inventory

The four ordinals `plan_state` currently anchors on, and what each actually selects on a Tier-1
spec, measured on `memory/builds/dTieredTribunal/spec/2026-08-26-spec-dTieredTribunal-2.md`:

| anchor | intended section | Tier-2 actual | Tier-1 actual |
|---|---|---|---|
| `^## 2\.` | Scope (IN) | Scope (IN) | Scope (IN) |
| `^## 6\.` | Acceptance criteria | Acceptance criteria | **Gates** |
| `^## 7\.` | Gates | Gates | **Open questions** |
| `^## 8\.` | Open questions | Open questions | **Revision log** |

Two consequences follow and they differ in severity. The FORKED false positive is loud: a revision
log has bullet items and no conforming `RESOLVED (...)` mark, so every Tier-1 spec grades FORKED.
The THIN blindness is silent and is the worse half: the acceptance slot is filled by the Gates
section, so a Tier-1 spec stating no acceptance criterion at all grades READY.

### Migration

None. The change is a predicate, no artifact is committed from it, and no spec's bytes move.

### Alternatives rejected

- **Derive the offset from the tier in the status header.** Rejected: it makes the classifier depend
  on a second field being correct, and a spec whose header tier disagrees with its section count
  would then be graded on a shape it does not have. The titles are already unambiguous.
- **Accept both the ordinal and the title.** Rejected: two accepted spellings is two answers to one
  question, and the ordinal spelling is the one that is wrong.

### Files touched (estimate)

`tools/unattended/unattended.sh` (the `plan_state` awk program), `tools/unattended/unattended.test.sh`.

## 5. Production-readiness checklist

- **Security · data · write surface** — none. The function reads a file and prints a token.
- **Performance** — unchanged shape: one awk pass per graded spec. `TOOL-aCollapsedScan-4` records
  that this call is the `unattended kit gate` leg's dominant per-unit cost and that it is unfoldable;
  this unit must not make it slower, and a title match is the same single regex per heading line.
- **Observability** — the refusal in S3 names the file and the duplicated title.
- **Testing** — S4's four arms, each observed RED against the shipped predicate before the fix.
- **Migration · rollback** — revert is the single function body; nothing is persisted.

## 6. Acceptance criteria

- **AC1** — `bash tools/unattended/unattended.sh --plan dTieredTribunal` prints no `(FORKED)` for
  `TOOL-dTieredTribunal-15` or `TOOL-dTieredTribunal-2`. Both print it today; that is the observation
  that proves this change and it is re-runnable against a tracked build.
- **AC2** — a Tier-1 fixture spec whose `## 5. Acceptance criteria` body is empty grades `THIN`.
  Observed RED first: against the shipped predicate the same fixture grades `READY`, and that arm is
  the one this unit exists for.
- **AC3** — a Tier-1 fixture spec whose `## 8. Revision log` carries bullets and whose
  `## 7. Open questions` reads `none` grades `READY`, not `FORKED`.
- **AC4** — in `tools/unattended/unattended.test.sh`, a Tier-2 fixture spec's grade is UNCHANGED across the fix for all four states, so the
  384 Tier-2-shaped specs in the corpus are not regraded.
- **AC5** — a fixture spec carrying two `Acceptance criteria` headings is REFUSED with a message
  naming the file and the title.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · `unattended driver selftest` · `unattended kit gate` ·
`marker contract (4 readers)` · `memory hygiene`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-01 · authored under the dBriefedPass mandate.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "drive a build's passes through an orchestrated workflow
harness in a fixed order"` returned no seam for a classifier fix; the seam this unit extends was
found by reading source instead and is named by path:
`tools/memory-tree/check-memory-hygiene.sh:880,939,1326`, which already anchors these same sections
as `^## [0-9]+[.] <Title>`. This unit copies that spelling rather than inventing one, which is what
makes the two readers agree by construction instead of by a case table nobody re-runs. The classifier
being changed is `tools/unattended/unattended.sh:1649`.

Recall terms used: unattended mandate pass ordering workflow harness spec before code regrounding
compaction driver orchestration agent-cap fan-out build-method handoff prompt.
