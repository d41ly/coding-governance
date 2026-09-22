# TOOL-dBriefedPass-1 — `plan_state` grades a spec by heading TITLE, not by ordinal

**Status:** CLOSED · rev-3 · 2026-09-01 · node d · Tier-2 · base 269dacae · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-build-TOOL-dBriefedPass-1-1-classifier-pass.md](../build/2026-09-01-build-TOOL-dBriefedPass-1-1-classifier-pass.md) | journal | — |
| [2026-09-01-prompt-TOOL-dBriefedPass-1.md](../prompts/2026-09-01-prompt-TOOL-dBriefedPass-1.md) | research | TOOL-dBriefedPass-2 TOOL-dBriefedPass-3 TOOL-dBriefedPass-4 TOOL-dBriefedPass-5 |
| [2026-09-01-review-TOOL-dBriefedPass-1-2-3-4-5-closing-diff-round1.md](../reviews/2026-09-01-review-TOOL-dBriefedPass-1-2-3-4-5-closing-diff-round1.md) | diff-review | TOOL-dBriefedPass-2 TOOL-dBriefedPass-3 TOOL-dBriefedPass-4 TOOL-dBriefedPass-5 |
| [2026-09-01-review-TOOL-dBriefedPass-1-2-3-4-5-closing-diff-round2.md](../reviews/2026-09-01-review-TOOL-dBriefedPass-1-2-3-4-5-closing-diff-round2.md) | diff-review | TOOL-dBriefedPass-2 TOOL-dBriefedPass-3 TOOL-dBriefedPass-4 TOOL-dBriefedPass-5 |
| [2026-09-01-review-TOOL-dBriefedPass-1-spec-audit-round1.md](../reviews/2026-09-01-review-TOOL-dBriefedPass-1-spec-audit-round1.md) | spec-audit | TOOL-dBriefedPass-2 TOOL-dBriefedPass-3 TOOL-dBriefedPass-4 TOOL-dBriefedPass-5 |
| [2026-09-01-review-TOOL-dBriefedPass-1-spec-audit-round2.md](../reviews/2026-09-01-review-TOOL-dBriefedPass-1-spec-audit-round2.md) | spec-audit | TOOL-dBriefedPass-2 TOOL-dBriefedPass-3 TOOL-dBriefedPass-4 TOOL-dBriefedPass-5 |
| [2026-09-01-review-TOOL-dBriefedPass-1-spec-audit-round3.md](../reviews/2026-09-01-review-TOOL-dBriefedPass-1-spec-audit-round3.md) | spec-audit | TOOL-dBriefedPass-2 TOOL-dBriefedPass-3 TOOL-dBriefedPass-4 TOOL-dBriefedPass-5 |

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
- **S3** — a spec carrying two headings with the same title binds the FIRST occurrence, and the
  awk does so DETERMINISTICALLY rather than by fallthrough. The ordinal previously made duplicates
  impossible to express and keying on the title removes that accident, so the behaviour is pinned by
  an arm instead of being left to whichever branch happens to run last.
- **S4** — arms in `tools/unattended/unattended.test.sh` covering: a Tier-1 spec with a filled
  §5 Acceptance grading READY, a Tier-1 spec with an EMPTY §5 Acceptance grading THIN, a Tier-1 spec
  whose §7 Open questions carries an unresolved item grading FORKED, and a Tier-1 spec whose §8
  Revision log carries bullets NOT grading FORKED.
- **S5** — `tools/memory-tree/marker-contract.test.sh` and `tools/unattended/unattended.test.sh`
  both slice this function's body out of the shipped bytes; both keep passing.
- **S6** — `memory/guides/BUILD-METHOD.md` M2's THIN and FORKED sentences are restated in section
  TITLES, and so is its template half `tools/memory-tree/BUILD-METHOD.template.md`, which
  `kit/dogfood doc parity` byte-compares against the render. The prose and the classifier move in ONE
  commit: today both are ordinal-keyed and both are wrong for Tier-1 in the same way, so a run
  following M2 and the machine reach the same answer, and after this unit they would disagree on
  exactly the Tier-1-shaped specs that `TOOL-dBriefedPass-3` turns into a hard refusal.
- **S7** — S6 is paid for INSIDE the declared budget. `memory/guides/BUILD-METHOD.md` is 24560 bytes
  against M1's 24576, and the template is 24571, so the edit is byte-neutral or byte-negative or it
  does not land: M3 reserves M1's own budget from this run's delegated authority, so a budget bump is
  PARKED as an owner decision and S6 is then dropped rather than forced.

## 3. Non-goals (OUT)

- The sibling reader in `check-memory-hygiene.sh` is NOT touched. It is already correct, and the
  point of this unit is to make the two agree by moving the wrong one.
- No new section is added to the spec canon, and no Tier-1 spec in the corpus is rewritten. The
  classifier moves to the corpus, never the corpus to the classifier.
- The case table that holds the two readers in agreement is not replaced with shared code. That is
  a larger refactor with its own cost and it is not what this defect needs.
- `--close`'s THIN term keeps its `SPEC_THIN_CUTOFF` date gating exactly as declared, and the
  GRADED POPULATION is unchanged: this unit changes what THIN MEANS on a Tier-1 spec, and it adds no
  third outcome to `plan_state`, so the set of specs the term walks is the same before and after.
  That is what S3's first-occurrence rule buys — a refusal token would have been a new outcome, it
  would have fallen through `verb_plan`'s `case` at `unattended.sh:2074` with no branch, and
  `build-complete`'s bare `[ "$(plan_state …)" = THIN ]` at `:3271` discards the exit status, so a
  refusing spec would have graded silently non-THIN at the one call site where the grade decides a
  landing.
- `plan_state`'s OUTPUT CONTRACT is not widened. It stays one bare token on stdout, which the driver
  records at `:3231-3237` as a deliberate decision because two harnesses slice the function body.
  Nothing here exposes the per-section map, which is why `TOOL-dBriefedPass-3` cannot name the empty
  section in its refusal and says so.

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
- **Observability** — the duplicate-title path emits NOTHING; S3 binds the first occurrence and
  prints the ordinary grade, so its only witness is AC5's two arms. The rev-2 wording named a
  refusal message that the same fold had just removed.
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
- **AC5** — in `tools/unattended/unattended.test.sh`, a fixture spec carrying two
  `Acceptance criteria` headings grades on the FIRST one: the arm fills the first and empties the
  second and asserts `READY`, then swaps them and asserts `THIN`. Two arms, because one alone is
  satisfied by a reader that always takes the last.
- **AC6** — `wc -c memory/guides/BUILD-METHOD.md` and `wc -c
  tools/memory-tree/BUILD-METHOD.template.md` are both at most their pre-edit values, 24560 and
  24571. Measured after S6, not argued: M1's byte half binds first and this unit may not raise it.
- **AC7** — `bash tools/memory-tree/kit-dogfood-parity.test.sh` is green, which is the leg that
  byte-compares the two halves S6 edits. Named because S6 touches a render pair and editing one half
  alone reds a leg no other criterion here observes.
- **AC8** — the POSITIVE observation of S6, without which S6 has no criterion that can fail. In BOTH
  `memory/guides/BUILD-METHOD.md` and `tools/memory-tree/BUILD-METHOD.template.md`, M2's THIN line
  names `Scope`, `Acceptance criteria` and `Gates` and its FORKED line names `Open questions`, and
  neither line carries a `§`-prefixed ordinal. Asserted over those two lines specifically and not
  over the file, whose 27 other `§` references are unrelated and would make a whole-file count
  unfalsifiable. Observed RED against the shipped bytes first, the way AC2 already is: today both
  lines read `§2 Scope, §6 Acceptance or §7 Gates` and `§8 Open questions`. AC6 and AC7 are a byte
  bound and an unchanged-leg assertion, and an empty diff satisfies both.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · `unattended kit gate` · `marker contracts` ·
`kit/dogfood doc parity` · `method carriers (every pointer declared)` · `memory hygiene`.

Every name above resolves against `tools/gate-legs.json`. `unattended driver selftest` and
`marker contract (4 readers)` were listed at rev-2 and resolve to nothing; the driver suite is
`tools/unattended/unattended.test.sh`, which is NOT on the bar by the owner's 2026-08-23 ruling, so
the arms S4 and S5 add are witnessed by running that file directly and the verdict is owed in the
landing report.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-01 · authored under the dBriefedPass mandate.
- rev-2 · 2026-09-01 · round-1 spec-audit fold. H1 and H2 (findings 36 and 22, one defect reached by
  two lenses): S3's REFUSAL had no channel — `plan_state`'s contract is one bare token by a decision
  the driver records, a refusal token has no branch at `verb_plan`'s case and `build-complete`
  discards the exit status, so a duplicate-title spec would have graded silently non-THIN at the one
  site where the grade decides a landing. S3 becomes a deterministic FIRST-occurrence rule, AC5
  becomes two arms, and §3 gains the two non-goals that state the unchanged output contract and the
  unchanged graded population. M2 (finding 61): BUILD-METHOD M2 states the classification in the
  ordinals this unit abandons, and after this build the method and the machine would disagree on
  exactly the Tier-1 specs `TOOL-dBriefedPass-3` refuses on — S6 brings that correction and its
  byte-compared template half into THIS unit so prose and code move in one commit, and S7 states that
  it is paid for inside a budget M3 reserves from this run.
- rev-3 · 2026-09-01 · round-2 spec-audit fold. H4 (finding 1): S6's only criteria were a byte bound
  and an unchanged-leg assertion, both satisfied by an empty diff, so the fold's headline scope item
  had no witness — AC8 observes the content, scoped to M2's two classification lines because a
  whole-file `§` count is 27 in both halves and cannot fail. M2 (finding 16): the §5 Observability
  bullet still described the rev-1 refusal that the rev-2 fold removed, instructing a builder to
  re-introduce exactly what round 1 blocked on. M1 (finding 17): §7 named two legs that resolve
  against nothing in `tools/gate-legs.json`.

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
