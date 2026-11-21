**Serves:** research TOOL-dPlacedRequest-96

# Brief — dPlacedRequest: TOOL-dPlacedRequest-96, a foreign stale lease can be taken over again, and its hint prints

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

The closing diff review of this build exited NON-CONVERGENT at round 2 (`--review` recorded `disposition promote`). This unit is one HIGH finding, promoted to a unit of its own. Write its spec so a builder can close each finding below with the mechanism the record's fix names (the skeptic judged most fixes SOUND; where the record gives the skeptic's class-level fix, take that), and so each criterion is observed RED-first against the tree as it stands at 2b4cc0bd4.

### Items

1. `memory/builds/dPlacedRequest/reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md`, item H2 — `check_claim_writable` lost its `lease:foreign-stale` row, so stale leases cannot be taken over (id 3). Read the item whole: its Where, What is wrong, Fix and Left-shift gate lines are the design input; a left-shift gate the record names is part of this unit's scope where it fits one write set, and otherwise a bug-class checklist entry.

### Acceptance

Spec `TOOL-dPlacedRequest-96` exists at rev-1, DEFERRED, order 37, with one scope item and one criterion per finding, each criterion naming its `New arm:` and its RED-first reading against the tree at 2b4cc0bd4; `check-memory-hygiene.sh --only 12,25 --spec`, the spec-token checker, a PLAIN `python tools/playbook/writing_practice.py check pinned-facts` and `bash tools/unattended/unattended.sh --check-specs dPlacedRequest TOOL-dPlacedRequest-96` report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the pinned-facts check, the driver's `--check-specs` and the naming lexicon; no other.

### Non-goals

No product code, no commit, no index render, no spec other than TOOL-dPlacedRequest-96; CLOSED specs stay frozen (P19). The unattended kit's self-test suites stay waived (README rule 8): a criterion they would observe is observed by a probe and cites that rule. Pin every figure on its own line with DERIVED or PINNED, cite code as `path#symbol` or a blob pin, and never quote a check's hit literally in prose.
