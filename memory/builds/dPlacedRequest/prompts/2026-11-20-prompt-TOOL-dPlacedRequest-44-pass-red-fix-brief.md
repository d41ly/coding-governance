**Serves:** research TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50

# Brief — dPlacedRequest: the order-25 re-ground's figures pinned on their lines

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

TOOL-dPlacedRequest-44's pass legs are red on writing practice: the pinned-facts check reads four figures the
order-25 re-ground wrote without a PINNED or DERIVED mark on their own line. Spec 44 (CLOSED) carries the commit count
of the oracle's walk on this branch; spec 48 (DEFERRED) carries the request lock's wait; spec 50 (DEFERRED) carries the
fresh sighting's age and the old opener's age. Pin each on its own line; change nothing else.

### Items

1. In `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-44.md`, the line carrying the oracle's walked-commit count gets `(PINNED)` after the figure on that same line, or is reflowed so the figure and its mark share a line. Spec 44 is CLOSED, so this is an editorial correction for an inline red fix: no rev bump, no status change, one §9 line naming this brief.
2. In the specs of `TOOL-dPlacedRequest-48` and `TOOL-dPlacedRequest-50`, every line carrying one of the flagged figures (the lock wait in 48; the two sighting ages in 50) gets its mark on the same line. Both are DEFERRED: bump the rev and add one §9 line naming this brief.

### Acceptance

`python tools/playbook/writing_practice.py check pinned-facts` reports no red for the three specs, and
`check-memory-hygiene.sh --only 12,25 --spec` and the spec-token checker over each report nothing.

### Gates

The pinned-facts check, the memory hygiene gate (`--only 12,25 --spec`) and the spec-token checker; no other.

### Non-goals

No product code, no commit, no index render, no status flip, no other line and no other spec. Never quote a check's
hit literally in prose.
