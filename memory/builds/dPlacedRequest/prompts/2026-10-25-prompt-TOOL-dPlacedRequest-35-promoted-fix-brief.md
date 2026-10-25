**Serves:** research TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43

# Promoted fix brief — dPlacedRequest, the round-2 promotions' gate hits

The round-2 spec audit's disposal added TOOL-dPlacedRequest-35 to -43, closing the findings of
`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md`, and folded hands-off
edges into the specs they amend. Read the first fix brief,
`memory/builds/dPlacedRequest/prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md`, and the round-1
promoted fix brief, `memory/builds/dPlacedRequest/prompts/2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md`:
their rules per hit class bind here. Fix the five hits below by editing the named specs, and nothing else: no product
code, no commit, no index render, no `**Carries:**` or `**Derived:**` line.

- **[guards]** on TOOL-dPlacedRequest-43: add each named leg to its §7 leg line.
- **[size]** on TOOL-dPlacedRequest-34: cut it under the 49152-byte ceiling again, leaving room for a later fold, by
  tightening prose and dropping repetition, never by dropping a finding the unit closes or a hands-off edge the
  round-2 disposal folded in.

Bump each edited spec's rev and add its §9 line. Run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25`
(the specs are staged) and return each hit's disposition with spec 34's final byte count.

## The hits

```text
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md [guards] `agent-cap self-test <- tools/hooks/scratch-guard.js` — §4 files-touched names tools/hooks/scratch-guard.js, which trips the guard of leg 'agent-cap self-test', absent from the §7 leg line
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md [guards] `verifier fan-out self-test <- tools/hooks/scratch-guard.js` — §4 files-touched names tools/hooks/scratch-guard.js, which trips the guard of leg 'verifier fan-out self-test', absent from the §7 leg line
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md [guards] `review-join self-test <- tools/hooks/scratch-guard.js` — §4 files-touched names tools/hooks/scratch-guard.js, which trips the guard of leg 'review-join self-test', absent from the §7 leg line
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-43.md [guards] `hook destinations self-test <- tools/hooks/scratch-guard.js` — §4 files-touched names tools/hooks/scratch-guard.js, which trips the guard of leg 'hook destinations self-test', absent from the §7 leg line
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md [size] `size <- memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md` — 50807 bytes, 1655 over the spec ceiling 49152; split the spec or move history out of it
```
