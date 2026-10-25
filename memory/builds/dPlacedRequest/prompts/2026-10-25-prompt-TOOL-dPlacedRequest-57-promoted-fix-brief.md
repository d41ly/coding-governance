**Serves:** research TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59

# Promoted fix brief — dPlacedRequest, the round-6 promotions' gate hit

The round-6 spec audit's disposal added TOOL-dPlacedRequest-57 to -59, closing the findings of
`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-53-spec-audit.md`. Read the first fix
brief, `memory/builds/dPlacedRequest/prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md`: its **check 25**
rule binds here. Fix the one hit below by editing TOOL-dPlacedRequest-58, and nothing else: no product code, no
commit, no index render, no binding line.

- **check 25**: a §2 item that truly retires a named thing gains a `**Readers:**` clause, `by name:` the readers
  that spell it and `by value:` its value readers or `NO VALUE READERS` and a reason, each found by `git grep`, each
  marker on one line; an item that retires nothing named is reworded so no retirement word sits beside a backticked
  token.

Bump the spec's rev and add its §9 line. Run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` (the
specs are staged) and return the hit's disposition.

## The hit

```text
HYGIENE check 25 FAILED — §2 scope items of LIVE specs that retire a named thing, and every **Readers:** clause, must answer by name: with names a reader spells and by value: with a reader or NO VALUE READERS and a reason:
memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-58.md (§2 items that retire a named thing carry no **Readers:** clause; write **Readers:** then by name: and the readers that spell the name, then by value: and the readers of its value, or NO VALUE READERS and a reason): S1
```
