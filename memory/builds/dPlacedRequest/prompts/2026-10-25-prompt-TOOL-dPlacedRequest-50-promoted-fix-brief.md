**Serves:** research TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52

# Promoted fix brief — dPlacedRequest, the round-4 promotions' gate hits

The round-4 spec audit's disposal added TOOL-dPlacedRequest-50 to -52, closing the findings of
`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-44-spec-audit.md`, and folded hands-off
edges into the specs they amend. Read the first fix brief,
`memory/builds/dPlacedRequest/prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md`, and the round-2 and
round-3 promoted fix briefs, `memory/builds/dPlacedRequest/prompts/2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md`
and `memory/builds/dPlacedRequest/prompts/2026-10-25-prompt-TOOL-dPlacedRequest-44-promoted-fix-brief.md`: their
rules per hit class bind here. Fix the three hits below by editing the named specs, and nothing else: no product code,
no commit, no index render, no binding line.

- **[path]** on TOOL-dPlacedRequest-52: cite the file TOOL-dPlacedRequest-13 creates by its basename in §6.
- **[size]** on TOOL-dPlacedRequest-34: the round-4 fold pushed it over the 49152-byte ceiling again. Cut it to at
  most 47104 bytes, the target TOOL-dPlacedRequest-43's S22 states, so the next records render cannot push it over,
  by tightening prose and dropping repetition, never by dropping a finding the unit closes, a criterion or a hands-off
  edge any disposal folded in.
- **check 12, failure mode** on TOOL-dPlacedRequest-52's AC22: give it its red case on one line (`Red when:`), as
  its siblings do; check 12 joins a criterion's lines but reads that marker whole.

Bump each edited spec's rev and add its §9 line. Run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25`
(the specs are staged) and return each hit's disposition with spec 34's final byte count.

## The hits

```text
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-52.md [path] `tools/lib/gov-feed.sh` — not tracked by git ls-files
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md [size] `size <- memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md` — 49387 bytes, 235 over the spec ceiling 49152; split the spec or move history out of it
HYGIENE check 12 FAILED — spec files dated >= 2026-07-15 not conforming to memory/TEMPLATE-SPEC.md:
memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-52.md (acceptance bullets naming no failure mode, required at/after SPEC_FAILURE_MODE_CUTOFF 2026-09-08): AC22
```
