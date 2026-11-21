**Serves:** research TOOL-dPlacedRequest-100

# Brief — dPlacedRequest: spec 100's cost estimate pinned

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

Spec `TOOL-dPlacedRequest-100` carries one duration with no mark on its own line, and the plain pinned-facts check
reds it at unit 95's pass legs: the cost estimate under its new arm cites a budget row's figure. Pin it; change
nothing else.

### Items

1. In spec `TOOL-dPlacedRequest-100`, the one line `python tools/playbook/writing_practice.py check pinned-facts` names
   gets PINNED or DERIVED on that same line (DERIVED where the figure is computed from others in the spec), or is
   reflowed so the figure and its mark share a line.
2. This is an editorial correction: keep the spec at rev-1 and add no revision-log line beyond one naming this brief.

### Acceptance

A plain `python tools/playbook/writing_practice.py check pinned-facts` reports no red for the spec, and
`check-memory-hygiene.sh --only 12,25 --spec` and the spec-token checker over it report nothing.

### Gates

The pinned-facts check, the memory hygiene gate (`--only 12,25 --spec`) and the spec-token checker; no other.

### Non-goals

No product code, no commit, no index render, no status flip, no other line and no other spec. Never quote a check's
hit literally in prose.
