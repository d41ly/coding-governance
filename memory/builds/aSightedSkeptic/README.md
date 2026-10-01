---
slug: aSightedSkeptic
node: a
opened: 2026-10-01
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-aSightedSkeptic-1 TOOL-aSightedSkeptic-2 TOOL-aSightedSkeptic-3 TOOL-aSightedSkeptic-4 TOOL-aSightedSkeptic-5 TOOL-aSightedSkeptic-6 TOOL-aSightedSkeptic-7 TOOL-aSightedSkeptic-8 TOOL-aSightedSkeptic-9
---

# aSightedSkeptic — the Tier-2 review harness, briefed, calibrated and measured

## The problem this build exists to solve

`tools/workflows/tier2-review.js` closes every build here and ships to every adopter, and its own
record says it does not converge. Of 194 closing diff reviews, none came back `CLEAN`. Long builds
plateau: one ran nine rounds, every one BLOCKED. In later rounds, half the confirmed findings are
defects the previous round's fix introduced.

Seven causes were found in its prompts and arguments, plus a measurement gap. Skeptics get no repo,
range or by-design list. Proposed fixes are never judged. Finders get no intent and no checklist. The
lens set misses the repo's signature defect. Severity is undefined. Intensity is fixed. And recall is
never measured. The owner's prompt and the list are in `prompts/`.

## Expected improvements

- Fold rounds stop finding defects in fixes nobody judged.
- A skeptic reads the right tree and the right range.
- Lenses judge the diff against stated intent and the project's own bug classes.
- BLOCKER means one thing across finders, skeptics and synthesis.
- Small diffs can be reviewed light.
- Per-lens yield and recall become measurable.

## Detriments if this is not built

- Closing reviews keep plateauing, and each round re-spends a full fan on defects in the last fix.
- A skeptic in the wrong checkout keeps confirming or refuting against code nobody asked about.
- Whether a lens earns its tokens stays unanswerable, so the lens set keeps being chosen by feel.

## Build-level rules

- Every harness change lands in `tools/workflows/tier2-review.template.js` and its render, and assumes nothing about an adopter beyond what the harness requires today.
- A project-specific input arrives as an `args` field; its absence is ANNOUNCED in the log and the report, never defaulted silently.
- Fan-out stays inside `tools/hooks/agent-cap.js`: the lens array stays a literal of at most five, and a skipped lens is skipped inside its thunk.
- No governance carrier is edited. Five lenses sit inside the review protocol's stated three to six.
- Each unit's arms go into `tools/workflows/tier2-review.test.sh` and are observed RED first; the suite runs once, at `VERIFYING`.
- No spec audit (owner, 2026-10-01): the closing diff review is the specs' first review.
- Classified at kickoff (M2): all nine units MISSING; specced by the build harness, built one at a time in spec order.

## Parked decisions

- None yet.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aSightedSkeptic-1` | 2 | the skeptic is briefed with the repo, the range, the context and the by-design list |
| 2 | `TOOL-aSightedSkeptic-2` | 2 | the skeptic judges each proposed fix as well as the claim |
| 3 | `TOOL-aSightedSkeptic-3` | 2 | finders are handed intent: a `specs` argument, and the range's commit messages by default |
| 4 | `TOOL-aSightedSkeptic-4` | 2 | a `checklist` argument whose classes are split across the lenses |
| 5 | `TOOL-aSightedSkeptic-5` | 2 | five diff lenses, with verification and intent added, and project lens notes |
| 6 | `TOOL-aSightedSkeptic-6` | 2 | one severity rubric; a skeptic may re-grade, or answer uncertain |
| 7 | `TOOL-aSightedSkeptic-7` | 2 | an intensity argument whose light setting announces the lenses it skips |
| 8 | `TOOL-aSightedSkeptic-8` | 2 | every finding keeps its lens, a findings ledger lands beside the report, and the confirmed set is returned |
| 9 | `TOOL-aSightedSkeptic-9` | 2 | the replay benchmark: a ledger scored for recall against a past round's known findings |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 9 unit(s) · node a · opened 2026-10-01 · streams tooling
ids TOOL-aSightedSkeptic-1 TOOL-aSightedSkeptic-2 TOOL-aSightedSkeptic-3 TOOL-aSightedSkeptic-4 TOOL-aSightedSkeptic-5 TOOL-aSightedSkeptic-6 TOOL-aSightedSkeptic-7 TOOL-aSightedSkeptic-8 TOOL-aSightedSkeptic-9

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aSightedSkeptic-5 — five diff lenses, with verification and intent added, project lens notes, and one review-shape bump](spec/2026-10-01-spec-TOOL-aSightedSkeptic-5.md) | 1 | 2 | CLOSED | rev-1 | 2026-10-01 |
| [TOOL-aSightedSkeptic-1 — the skeptic is briefed with the repo, the range, the context and the by-design list](spec/2026-10-01-spec-TOOL-aSightedSkeptic-1.md) | 2 | 2 | CLOSED | rev-1 | 2026-10-01 |
| [TOOL-aSightedSkeptic-3 — finders and skeptics are handed intent: a `specs` argument, and the range's commit messages by default](spec/2026-10-01-spec-TOOL-aSightedSkeptic-3.md) | 3 | 2 | CLOSED | rev-1 | 2026-10-01 |
| [TOOL-aSightedSkeptic-4 — a `checklist` argument whose classes are split across the lenses that run](spec/2026-10-01-spec-TOOL-aSightedSkeptic-4.md) | 4 | 2 | SPECCED | rev-1 | 2026-10-01 |
| [TOOL-aSightedSkeptic-2 — the skeptic judges each finding's proposed fix as well as its claim](spec/2026-10-01-spec-TOOL-aSightedSkeptic-2.md) | 5 | 2 | SPECCED | rev-1 | 2026-10-01 |
| [TOOL-aSightedSkeptic-6 — one severity rubric, a skeptic's binding grade, and an uncertain verdict](spec/2026-10-01-spec-TOOL-aSightedSkeptic-6.md) | 6 | 2 | SPECCED | rev-1 | 2026-10-01 |
| [TOOL-aSightedSkeptic-7 — an intensity argument whose light setting announces the lenses it skips](spec/2026-10-01-spec-TOOL-aSightedSkeptic-7.md) | 7 | 2 | SPECCED | rev-1 | 2026-10-01 |
| [TOOL-aSightedSkeptic-8 — every finding keeps its lens, a findings ledger lands beside the report, and the confirmed set is returned](spec/2026-10-01-spec-TOOL-aSightedSkeptic-8.md) | 8 | 2 | SPECCED | rev-1 | 2026-10-01 |
| [TOOL-aSightedSkeptic-9 — the replay benchmark: a review scored for recall against a past round](spec/2026-10-01-spec-TOOL-aSightedSkeptic-9.md) | 9 | 2 | SPECCED | rev-1 | 2026-10-01 |
<!-- /gen:build-units -->

Records: 11 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aSightedSkeptic-1 TOOL-aSightedSkeptic-2 TOOL-aSightedSkeptic-3 TOOL-aSightedSkeptic-4 TOOL-aSightedSkeptic-5 TOOL-aSightedSkeptic-6 TOOL-aSightedSkeptic-7 TOOL-aSightedSkeptic-8 TOOL-aSightedSkeptic-9.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aSightedSkeptic-5` | no |
| 2 | `TOOL-aSightedSkeptic-1` | no |
| 3 | `TOOL-aSightedSkeptic-3` | no |
| 4 | `TOOL-aSightedSkeptic-4` | no |
| 5 | `TOOL-aSightedSkeptic-2` | no |
| 6 | `TOOL-aSightedSkeptic-6` | no |
| 7 | `TOOL-aSightedSkeptic-7` | no |
| 8 | `TOOL-aSightedSkeptic-8` | no |
| 9 | `TOOL-aSightedSkeptic-9` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
