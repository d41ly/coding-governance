**Serves:** research TOOL-dPlacedRequest-4

# Brief — dPlacedRequest: TOOL-dPlacedRequest-4's spec follows a function renamed for the lexicon

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

TOOL-dPlacedRequest-4 is CLOSED and its pass legs were red on the naming lexicon: the function the spec named for
appending a placement block leads with a verb the lexicon's declared table does not hold, and the main loop renamed it
`add_placement` in `tools/loop/placement.py` as an inline red fix. The spec still cites the old name in four places.
Re-cite them; change nothing else.

### Items

1. In `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-4.md`, replace every citation of the old function name with `add_placement` (the `tools/loop/placement.py#add_placement` symbol), in its scope paragraph, its edge line, its Inventory row and AC12. This is an editorial correction to a CLOSED spec made for an inline red fix (protocol section 12): no rev bump, no status change, and one §9 line naming this brief and saying the function was renamed for the naming lexicon.

### Acceptance

The spec names the old function nowhere, and `check-memory-hygiene.sh --only 12,25 --spec` and the spec-token checker
over it report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec`) and the spec-token checker; no other.

### Non-goals

No product code, no commit, no index render, no status flip (it stays CLOSED), no other spec. Never quote a check's
hit literally in prose.
