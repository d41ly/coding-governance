# TOOL-dTotalRecall-38 deviation 1013 — the hand-off of parse_id_parts to unit 46 was not taken: unit 54 built the body and unit 46 observed it

**Serves:** deviation TOOL-dTotalRecall-38

- **Departs from:** `TOOL-dTotalRecall-38@rev-6` [§3 Edges, the hands-off to TOOL-dTotalRecall-46]
- **Hand-off:** spec-to-code
- **Before:** unit 38 hands `parse_id_parts` to TOOL-dTotalRecall-46, "whose body that unit rebuilds on `tree_lib.build_id_token_re`".
- **After:** TOOL-dTotalRecall-54 built the body at pass 74af3faa4, and TOOL-dTotalRecall-46 at pass 63f283ddd built no body and observed that one, as TOOL-dTotalRecall-64 amended its spec to do at 86360f071; unit 38 spec, CLOSED at pass 2f59e5acb, keeps the hand-off line.
- **Cause:** review finding
- **Reason:** two units designed one function body, and TOOL-dTotalRecall-64 settled it by having unit 46 observe the body of unit 54, where a build by the stale hand-off would have overwritten the cited-family body; a CLOSED spec is frozen, so the line stands as history and this record names the departure (the round-1 spec audit of units 61 to 66, id 5; TOOL-dTotalRecall-70 S14).
- **Evidence:** 86360f071, the pass of TOOL-dTotalRecall-64 that settled it, which touches no line of the unit 38 spec; the parse_id_parts and SUFFIX_RE segments of `tools/memory-tree/id_grammar.py` equal at 74af3faa4 and 63f283ddd; `memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-61-spec-audit-round1.md`.
- **Risk:** editorial
- **Approver:** author, under the value `author-recorded` of the build
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** 2026-10-26-review-TOOL-dTotalRecall-61-spec-audit-round1
- **Made-by:** lease-dTotalRecall
