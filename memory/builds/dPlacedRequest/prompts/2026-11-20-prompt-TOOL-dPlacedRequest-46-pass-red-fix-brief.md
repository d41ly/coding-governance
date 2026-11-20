**Serves:** research TOOL-dPlacedRequest-46

# Brief — dPlacedRequest: TOOL-dPlacedRequest-46's spec pins its figures on their lines

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

TOOL-dPlacedRequest-46 is CLOSED and its pass legs are red on writing practice: the pinned-facts check reads each
duration in the spec on its own line, and rev-6's §4 Evidence and AC1 to AC4 carry the probe's ages on lines whose
PINNED mark sits on a later `figure:` line. Pin each one on its own line; change nothing else.

### Items

1. In `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-46.md`, every line of §4 Evidence and of AC1 to AC4 that carries one of the probe's ages (the sightings of 60, 120 and 3600000 seconds) gets `(PINNED)` after each figure on that same line, or is reflowed so the figure and its PINNED mark share a line. This is an editorial correction to a CLOSED spec made for an inline red fix (protocol section 12): no rev bump, no status change, and one §9 line naming this brief.

### Acceptance

`python tools/playbook/writing_practice.py check pinned-facts` reports no red for the spec, and
`check-memory-hygiene.sh --only 12,25 --spec` and the spec-token checker over it report nothing.

### Gates

The pinned-facts check, the memory hygiene gate (`--only 12,25 --spec`) and the spec-token checker; no other.

### Non-goals

No product code, no commit, no index render, no status flip (it stays CLOSED), no other line and no other spec.
