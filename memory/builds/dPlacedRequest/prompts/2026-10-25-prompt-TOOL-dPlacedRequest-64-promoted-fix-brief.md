**Serves:** research TOOL-dPlacedRequest-64

# Promoted fix brief — dPlacedRequest, the round-9 batch unit's gate hit

The round-9 spec audit's disposal added TOOL-dPlacedRequest-64, the batch unit closing the minors of
`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-62-spec-audit.md`. It is the chain's
last unit and is carried forward unaudited under the owner's ruling. Read the round-6 promoted fix brief,
`memory/builds/dPlacedRequest/prompts/2026-10-25-prompt-TOOL-dPlacedRequest-57-promoted-fix-brief.md`: its
**check 25** rule binds here. Fix the one hit below by editing TOOL-dPlacedRequest-64, and nothing else: no product
code, no commit, no index render, no binding line.

Bump the spec's rev and add its §9 line. Run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` (the
specs are staged) and return the hit's disposition.

## The hit

```text
HYGIENE check 25 FAILED — §2 scope items of LIVE specs that retire a named thing, and every **Readers:** clause, must answer by name: with names a reader spells and by value: with a reader or NO VALUE READERS and a reason:
memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-64.md (§2 items that retire a named thing carry no **Readers:** clause; write **Readers:** then by name: and the readers that spell the name, then by value: and the readers of its value, or NO VALUE READERS and a reason): S14
```
