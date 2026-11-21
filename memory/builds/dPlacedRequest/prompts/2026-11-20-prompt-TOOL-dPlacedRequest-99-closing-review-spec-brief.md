**Serves:** research TOOL-dPlacedRequest-99

# Brief — dPlacedRequest: TOOL-dPlacedRequest-99, the closing review's minors: every plant on a gate, a resolver arm, honest re-fence and card outcomes, a re-priced row and three loose ends

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

The closing diff review of this build exited NON-CONVERGENT at round 2 (`--review` recorded `disposition promote`). This unit is the MEDIUM and LOW findings, batched into one unit as the severity rule orders. Write its spec so a builder can close each finding below with the mechanism the record's fix names (the skeptic judged most fixes SOUND; where the record gives the skeptic's class-level fix, take that), and so each criterion is observed RED-first against the tree as it stands at 95c3103ad.

### Items

1. `memory/builds/dPlacedRequest/reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md`, item M1 — the suite runs 8 of card-store.fixture.sh's plants, and the rest are on no gate (id 4). Read the item whole: its Where, What is wrong, Fix and Left-shift gate lines are the design input; a left-shift gate the record names is part of this unit's scope where it fits one write set, and otherwise a bug-class checklist entry.
2. `memory/builds/dPlacedRequest/reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md`, item M2 — no arm tells the S20 exact-match node resolver from the substring rule it replaced (id 5). Read the item whole: its Where, What is wrong, Fix and Left-shift gate lines are the design input; a left-shift gate the record names is part of this unit's scope where it fits one write set, and otherwise a bug-class checklist entry.
3. `memory/builds/dPlacedRequest/reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md`, item M1 — the lander reads a local re-fence failure as `claim-lost` (id 2). Read the item whole: its Where, What is wrong, Fix and Left-shift gate lines are the design input; a left-shift gate the record names is part of this unit's scope where it fits one write set, and otherwise a bug-class checklist entry.
4. `memory/builds/dPlacedRequest/reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md`, item M2 — a build-card follow prefers a stale cache ref over a newer unpublished card (id 3). Read the item whole: its Where, What is wrong, Fix and Left-shift gate lines are the design input; a left-shift gate the record names is part of this unit's scope where it fits one write set, and otherwise a bug-class checklist entry.
5. `memory/builds/dPlacedRequest/reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md`, item M3 — the placement suite's budget row prices fifteen plants; the suite now has 29 (id 1). Read the item whole: its Where, What is wrong, Fix and Left-shift gate lines are the design input; a left-shift gate the record names is part of this unit's scope where it fits one write set, and otherwise a bug-class checklist entry.
6. `memory/builds/dPlacedRequest/reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md`, item L1 — `CARD_STORED_FROM` is set and never read (id 4). Read the item whole: its Where, What is wrong, Fix and Left-shift gate lines are the design input; a left-shift gate the record names is part of this unit's scope where it fits one write set, and otherwise a bug-class checklist entry.
7. `memory/builds/dPlacedRequest/reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md`, item L2 — scratch-guard's assertion floor leaves out AC28's two rows (id 6). Read the item whole: its Where, What is wrong, Fix and Left-shift gate lines are the design input; a left-shift gate the record names is part of this unit's scope where it fits one write set, and otherwise a bug-class checklist entry.
8. `memory/builds/dPlacedRequest/reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md`, item L3 — the `--entry-claim` usage line omits exits 2 and 3 (id 8). Read the item whole: its Where, What is wrong, Fix and Left-shift gate lines are the design input; a left-shift gate the record names is part of this unit's scope where it fits one write set, and otherwise a bug-class checklist entry.

### Acceptance

Spec `TOOL-dPlacedRequest-99` exists at rev-1, DEFERRED, order 37, with one scope item and one criterion per finding, each criterion naming its `New arm:` and its RED-first reading against the tree at 95c3103ad; `check-memory-hygiene.sh --only 12,25 --spec`, the spec-token checker, a PLAIN `python tools/playbook/writing_practice.py check pinned-facts` and `bash tools/unattended/unattended.sh --check-specs dPlacedRequest TOOL-dPlacedRequest-99` report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the pinned-facts check, the driver's `--check-specs` and the naming lexicon; no other.

### Non-goals

No product code, no commit, no index render, no spec other than TOOL-dPlacedRequest-99; CLOSED specs stay frozen (P19). The unattended kit's self-test suites stay waived (README rule 8): a criterion they would observe is observed by a probe and cites that rule. Pin every figure on its own line with DERIVED or PINNED, cite code as `path#symbol` or a blob pin, and never quote a check's hit literally in prose.
