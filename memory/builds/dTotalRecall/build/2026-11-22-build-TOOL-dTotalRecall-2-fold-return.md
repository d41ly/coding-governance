**Serves:** research TOOL-dTotalRecall-2

# TOOL-dTotalRecall-2 fold against unit 3 as built — the spec writer's return

The gov-spec-writer return for [2026-11-22-prompt-TOOL-dTotalRecall-2-fold-spec-writer](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-2-fold-spec-writer.md), in substance.

- Folded to rev-12; `--check-specs`, `check-spec-tokens.py --spec`, pinned-facts and hygiene check 12 read green; the spec sits under its size ceiling again, no criterion dropped.
- F6 RESOLVED (agent, delegated): the landed `placement.py#read_build_lease` returns None both for a free lease and for one this session holds, so the door splits its body into a new `read_lease_class` answering `free`, `mine` or the failing fact; the fleet-tag and session comparison lives once; AC5 adds a lease holder not refused over another session's claim.
- A clone with no remote: unit 3 as built answers `local <ref> · no remote` with exit 0 and no id, so the door passes a slug and takes an ask's sequence from the driver's existing `derive_ask_seq` through `breakpoints.py#run_sourced`; unit 7's no-remote fixture gets `<FAMILY>-<slug>-1`, or exit 2 `unarmed — no unattended kit` where its clone lacks the unattended kit (AC6 gains the case).
- The claim's session is read from this node's cache ref through a new `read_claim_lines` shared with `read_own_claim`; §5 states that a claim this node never fetched reads as no claim.
- `placement.py` and `gen_build_index.py` join Files touched; the gates line gains `tier2-review self-test`.
