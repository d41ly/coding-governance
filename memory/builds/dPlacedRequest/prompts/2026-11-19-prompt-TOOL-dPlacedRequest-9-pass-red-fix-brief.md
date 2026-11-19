**Serves:** research TOOL-dPlacedRequest-9

# Brief — dPlacedRequest: TOOL-dPlacedRequest-9's spec, one citation re-cited for the positional leg

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

TOOL-dPlacedRequest-9 is CLOSED and its pass legs are red on the positional leg: the spec's §4 quotes gov's moved
§B bullet with a bare reference to the build method's spec-set section, which the positional check reads as an unlisted section citation
and asks to be cited by the alias row's tag. Re-cite that one reference; change nothing else.

### Items

1. In `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-9.md`, the bullet that opens "A build may amend its own roster", replace that bare reference with the tag citation `doc.build-method#m2-the-spec-set-decompose-detect-classify-act`, leaving the rest of the line as it is. This is an editorial correction to a CLOSED spec made for an inline red fix (protocol section 12): no rev bump, no status change, and one §9 line naming this brief.

### Acceptance

`python tools/playbook/positional.py check` reports no unlisted row for the spec, and `check-memory-hygiene.sh --only
12,25 --spec` and the spec-token checker over it report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker and the positional check; no other.

### Non-goals

No product code, no commit, no index render, no status flip (it stays CLOSED), no other line and no other spec.
