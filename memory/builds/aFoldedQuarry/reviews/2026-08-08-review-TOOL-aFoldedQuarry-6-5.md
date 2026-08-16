# Review 5 — adversarial pass over the U4 gotchas sub-spec

**Serves:** spec-audit TOOL-aFoldedQuarry-6  <!-- inferred: U4, the gotchas sub-spec, per the build README's unit table -->

**Scope:** `spec/units/2026-08-08-spec-aFoldedQuarry-6-u4-gotchas.md` at rev-1, before any code.
**Method:** the catalogue's whole subject is gates that look green and are not, so the question is
what makes THIS unit look green and not be.

| # | Severity | Where | Finding |
|---|---|---|---|
| J1 | blocker | §2 S4, §6 AC6 | three "documented defects" with no arm are three silent bugs |
| J2 | high | §2 S3, §6 AC4 | the anchor harvest will select the record's OWN file and every sibling |
| J3 | high | §2 S7 | a budget with no measured number is a number somebody guesses later |
| J4 | medium | §2 S5 | check 19 needs a tree where the append-only area is non-empty, or it is vacuous |
| J5 | low | §4 | `gotchas/` must join check 3's sanctioned set in the same commit |

## J1 — a carried defect without an arm is just a defect (blocker)

S4 says three harvest defects are "carried as documented behaviour". Documented behaviour that no
test pins is indistinguishable from a bug nobody has noticed yet, and the whole point of copying
them forward is that a future reader will otherwise re-derive them the expensive way. Each of the
three gets its own arm asserting the OBSERVED result — `::` inside backticks harvests to nothing, a
trailing slash harvests to nothing, a bare basename selects tree-wide — so a future change that
"fixes" one of them fails loudly and its author has to decide deliberately. AC6 already gestures at
this; S4 now says the arms are part of the deliverable, not a nice-to-have.

## J2 — a record's anchors select the record itself (high)

Anchors are backtick-quoted path-like tokens in the body, and every record in this corpus will cite
paths under `memory/gotchas/` when it describes its own class — plus the selection rule matches on
basename, so a record naming `INDEX.md` selects every `INDEX.md` in the tree. The consequence is that
`--for-diff` over a diff that touches the catalogue emits most of the catalogue.

The fix is small and belongs in the spec rather than in a comment: a record's anchors NEVER select
inside `<MEMORY_ROOT>/gotchas/` — the catalogue is not a subject of review, and a record firing
because someone edited the catalogue is noise that trains reviewers to skip the checklist.

## J3 — a budget nobody measured is not a budget (high)

S7 introduces `UNIVERSAL_BUDGET` and cites upstream's designed-10-measured-40. It does not say what
THIS corpus's number is or how it is arrived at. Following U3's convention: `--report` prints the
count, the conf carries the measured value, and the build journal records it — so the first raise is
an argument against a recorded figure. A blank value turns the check off, matching every other pin
in this kit.

## J4 — check 19 is vacuous unless the append-only area is populated (medium)

The inert-anchor arm fires when EVERY path a record's anchors reach is append-only. On a tree whose
append-only area is empty, no anchor can reach one, so the arm can never fire and the rule ships
green forever. The selftest fixture therefore has to contain a real append-only file and a record
whose only anchor points at it — and the arm must assert the specific inert message, not merely a
non-zero exit, or the fixture proves nothing.

## J5 — the new directory must be sanctioned in the same commit (low)

`<MEMORY_ROOT>/gotchas/` is a new root child, and check 3 rejects an unexpected root entry. Cheap,
but a red bar in the middle of a commit is exactly what the one-commit rollout is meant to avoid.

## Disposition

All five folded into rev-2 before any code. J1 makes the three arms deliverables; J2 excludes the
catalogue from its own selection; J3 measures the budget; J4 populates check 19's fixture; J5 joins
the doc sweep.
