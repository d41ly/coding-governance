---
slug: aEvidencedLens
node: a
opened: 2026-10-05
streams: tooling
roster: TOOL
authorized-by: prompt
spec-audit: 2026-10-05
ids: TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 TOOL-aEvidencedLens-12 TOOL-aEvidencedLens-13 TOOL-aEvidencedLens-14
---

# aEvidencedLens — a spec audit the owner opts into gathers evidence, and every finding becomes a unit

## The problem this build exists to solve

A spec audit an owner opts into runs four lenses that may not read outside the spec set. Its only
automated caller hands those lenses no context, and nothing records which lens earned its cost. In
the 13 audited builds sampled, about two in five of the defects that got past the audit needed
evidence no lens was allowed to gather. The owner's prompt and the one answered question are in
`prompts/`.

## Expected improvements

- Lenses probe the tree read-only, and every spec finding carries its evidence.
- Five lenses aim at the classes the corpus measured, prior art among them.
- The caller hands every lens its context, siblings, checklist and fold diff.
- Every confirmed spec-audit finding becomes a unit, the minors batched.
- Each lens is scored on the unique defects it found.

## Detriments if this is not built

- Opted-in audits keep costing about 12x with no measured gain in the built code.
- Defects that need a probe keep reaching the closing review or the owner.
- Spec-audit mediums and lows keep landing as fold text no later round reads.
- Nobody can tell which lens to keep, because none is scored.

## Build-level rules

- Spec-audit kind only; the diff-review kind's prompts and lenses do not move.
- The audit stays opt-in and `REVIEW_ROUNDS` stays owner-set; neither default moves.
- Lens probes are READ-ONLY: no write to the tree, scratch only, every command bounded.
- Reuse first: the diff kind's evidence shape, the batched-minors seams, review_replay.py.
- Every new refusal or gate clause is observed RED on a staged break before it lands.
- Harness units build first, so the audit of promoted units uses the improved harness.
- Classified at kickoff (M2): all eleven MISSING.

## Parked decisions

- None yet.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aEvidencedLens-1` | 2 | the spec-audit lens catalogue: five lenses, the harness the one source, prior art as reuse-and-extend |
| 2 | `TOOL-aEvidencedLens-2` | 2 | spec lenses run bounded read-only probes and every spec finding carries its evidence |
| 3 | `TOOL-aEvidencedLens-3` | 2 | the spec skeptic's verdict test follows the rubric, re-runs evidence, refutes duplicates and by-design |
| 4 | `TOOL-aEvidencedLens-4` | 2 | a fold round reads the diff from the previous blob; a moved subject is graded, never fixed BLOCKER |
| 5 | `TOOL-aEvidencedLens-5` | 2 | the build harness hands the audit its context, sibling specs, checklist and prior findings |
| 6 | `TOOL-aEvidencedLens-6` | 2 | the review returns a per-lens yield over defect clusters, unique defects counted |
| 7 | `TOOL-aEvidencedLens-7` | 2 | `--review` takes highs and minors on a spec subject's exit and requires `promote` when any stood |
| 8 | `TOOL-aEvidencedLens-8` | 2 | the build harness promotes spec-audit minors into one or two batched units instead of folding |
| 9 | `TOOL-aEvidencedLens-9` | 2 | the bar refuses a run commit that changes `REVIEW_ROUNDS` |
| 10 | `TOOL-aEvidencedLens-10` | 1 | `review_replay.py` scores a spec-audit report against a past one by file and section |
| 11 | `TOOL-aEvidencedLens-11` | 1 | the method, the memory-tree README, the Skill and a decision record state what 1 to 9 built |
| 12 | `TOOL-aEvidencedLens-12` | 2 | PROMOTED: the spec skeptic line carries a finding's evidence through a line-break-only fold, so a pipe survives |
| 13 | `TOOL-aEvidencedLens-13` | 2 | PROMOTED: no diff-kind probe, lens or skeptic prompt moved from BASE through unit 6, observed once with the review key masked |
| 14 | `TOOL-aEvidencedLens-14` | 2 | PROMOTED: check 19 walks a terminal record's exclusions when either owner-held scan hits |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 14 unit(s) · node a · opened 2026-10-05 · streams tooling
ids TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 TOOL-aEvidencedLens-12 TOOL-aEvidencedLens-13
ids TOOL-aEvidencedLens-14

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aEvidencedLens-1 — the spec-audit lens catalogue: five lenses aimed at the measured classes, the harness its one source](spec/2026-10-05-spec-TOOL-aEvidencedLens-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-10-05 |
| [TOOL-aEvidencedLens-2 — spec lenses probe read-only, and every spec finding carries its evidence](spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md) | 2 | 2 | CLOSED | rev-2 | 2026-10-05 |
| [TOOL-aEvidencedLens-3 — the spec skeptic confirms by the rubric, re-runs the evidence, and refutes duplicates and by-design](spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md) | 3 | 2 | CLOSED | rev-2 | 2026-10-05 |
| [TOOL-aEvidencedLens-4 — a spec fold round reads its diff, and a moved subject is graded, not fixed at BLOCKER](spec/2026-10-05-spec-TOOL-aEvidencedLens-4.md) | 4 | 2 | CLOSED | rev-2 | 2026-10-05 |
| [TOOL-aEvidencedLens-6 — the review returns a per-lens yield over defect clusters, unique defects counted](spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md) | 5 | 2 | SPECCED | rev-3 | 2026-10-05 |
| [TOOL-aEvidencedLens-10 — `review_replay.py` scores a spec-audit report against a past one by file and section](spec/2026-10-05-spec-TOOL-aEvidencedLens-10.md) | 6 | 1 | SPECCED | rev-2 | 2026-10-05 |
| [TOOL-aEvidencedLens-13 — no diff-kind probe, lens or skeptic prompt moved from BASE through unit 6, observed once with the review key masked](spec/2026-10-05-spec-TOOL-aEvidencedLens-13.md) | 6 | 2 | SPECCED | rev-1 | 2026-10-05 |
| [TOOL-aEvidencedLens-5 — the build harness hands the audit its context, sibling specs, checklist and prior findings](spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md) | 6 | 2 | SPECCED | rev-2 | 2026-10-05 |
| [TOOL-aEvidencedLens-7 — `--review` takes highs and minors on a spec subject's exit and requires `promote` when any stood](spec/2026-10-05-spec-TOOL-aEvidencedLens-7.md) | 6 | 2 | SPECCED | rev-2 | 2026-10-05 |
| [TOOL-aEvidencedLens-9 — the bar refuses a run commit that changes `REVIEW_ROUNDS`](spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md) | 6 | 2 | SPECCED | rev-2 | 2026-10-05 |
| [TOOL-aEvidencedLens-12 — the spec skeptic line carries a finding's evidence through a line-break-only fold, so a pipe survives](spec/2026-10-05-spec-TOOL-aEvidencedLens-12.md) | 7 | 2 | SPECCED | rev-2 | 2026-10-05 |
| [TOOL-aEvidencedLens-14 — check 19 walks a terminal record's exclusions when EITHER owner-held scan hits, so an owner's round raise never reds an archived record](spec/2026-10-05-spec-TOOL-aEvidencedLens-14.md) | 7 | 2 | SPECCED | rev-1 | 2026-10-05 |
| [TOOL-aEvidencedLens-8 — the build harness promotes spec-audit minors, batched, and records the counts](spec/2026-10-05-spec-TOOL-aEvidencedLens-8.md) | 7 | 2 | SPECCED | rev-2 | 2026-10-05 |
| [TOOL-aEvidencedLens-11 — the method, the memory-tree README, the Skill, the verbs entry and a decision record state what units 1 to 9 built](spec/2026-10-05-spec-TOOL-aEvidencedLens-11.md) | 8 | 1 | SPECCED | rev-2 | 2026-10-05 |
<!-- /gen:build-units -->

Records: 14 bound to this build, across 3 record folder(s).

Ids no record names: TOOL-aEvidencedLens-12 TOOL-aEvidencedLens-13 TOOL-aEvidencedLens-14.

Ids no `spec-audit` record has ever named: TOOL-aEvidencedLens-12 TOOL-aEvidencedLens-13 TOOL-aEvidencedLens-14.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aEvidencedLens-1` | no |
| 2 | `TOOL-aEvidencedLens-2` | no |
| 3 | `TOOL-aEvidencedLens-3` | no |
| 4 | `TOOL-aEvidencedLens-4` | no |
| 5 | `TOOL-aEvidencedLens-6` | no |
| 6 | `TOOL-aEvidencedLens-10`, `TOOL-aEvidencedLens-13`, `TOOL-aEvidencedLens-5`, `TOOL-aEvidencedLens-7`, `TOOL-aEvidencedLens-9` | yes |
| 7 | `TOOL-aEvidencedLens-12`, `TOOL-aEvidencedLens-14`, `TOOL-aEvidencedLens-8` | yes |
| 8 | `TOOL-aEvidencedLens-11` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
