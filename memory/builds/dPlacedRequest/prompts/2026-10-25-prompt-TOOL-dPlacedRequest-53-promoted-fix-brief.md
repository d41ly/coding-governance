**Serves:** research TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56

# Promoted fix brief — dPlacedRequest, the round-5 promotions' gate hit

The round-5 spec audit's disposal added TOOL-dPlacedRequest-53 to -56, closing the findings of
`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-50-spec-audit.md`. Read the round-1
promoted fix brief, `memory/builds/dPlacedRequest/prompts/2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md`:
its **[bar]** rule binds here. Fix the one hit below by editing TOOL-dPlacedRequest-56, and nothing else: no product
code, no commit, no index render, no binding line.

- **[bar]**: the criterion names a suite as its observation. Observe the function or the checker the criterion is
  about directly, on a fixture or a staged break, and keep the suite on its §7 `New arm:` line.

Bump the spec's rev and add its §9 line. Run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` (the
specs are staged) and return the hit's disposition.

## The hit

```text
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-56.md [bar] `tools/unattended/unattended.test.sh` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
```
