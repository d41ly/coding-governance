**Serves:** research TOOL-dPlacedRequest-46

# Brief — dPlacedRequest: TOOL-dPlacedRequest-46's divergence, resolved

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

TOOL-dPlacedRequest-46's builder returned a DIVERGENCE (run `wf_5cc8df6e-de1`) and committed nothing: the defect §1 and
§4 describe does not happen on the tree. The walk in `tools/unattended/unattended.sh#read_claims` stops a row at a
`renews: -` commit as its beat and records that flag, and the verdict pass reads the flag as `live` before any bound
compare (TOOL-dPlacedRequest-17 S3's never-stale rule), so under `leases.renewal none` alone every row reads live and
AC1 to AC3's red copy reads the same as the pass. The one real difference the builder measured: a `renews: -`
commit ABOVE an older, sighted `renews: no` commit of the same tenure (a chain written partly under another renewal
policy) reads `stale` without the new stop and `live` with it. Revise the spec to the main loop's ruling.

### Items

1. F-scope: add to §8, resolved: "What does the `renews: -` stop repair, when the verdict pass already reads a `-` beat live?" (a) the mixed chain: a `-` commit above an older sighted `renews: no` commit of the same tenure, which reads stale today; (b) keep the ACs and name a red copy that also drops the verdict pass's never-stale read; (c) retire the unit as WONTDO. Mark `RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; it is the one input the stop changes, a renewal-policy change mid-tenure makes it real, and its red fires on the unit-35-order copy. widens: none · relaxes: none`.
2. Rewrite §1 Goal and §4 Evidence to the mixed-chain defect, with the builder's measured probe (a `-` tip sighted 60 s ago, PINNED, over a `renews: no` commit sighted 3600000 s ago, PINNED, reads `stale` on the unit-35-order copy and `live` with the stop), and drop the claim that every held lease goes stale under `none`.
3. Rewrite AC1 and AC2 to plant a `-` commit above an older sighted `renews: no` commit of the same epoch, red on the unit-35-order copy; AC3 plants each class above an old `renews: no` commit so the `-` class reads stale on the copy and live with the stop; add the unsighted `-` commit over an old commit (reads `unknown` with the stop, `stale` without) if it keeps the arm honest. Amend §7's `New arm:` line to the same red.
4. Cite code as `path#symbol`; the builder's blob-pinned lines may stay as blob pins.

### Acceptance

Spec 46 at its next rev carries the resolved fork, §1, §4, AC1 to AC3 and §7 rewritten to the mixed chain, and one §9
line naming this brief and the divergence; `check-memory-hygiene.sh --only 12,25 --spec`, the spec-token checker and
`bash tools/unattended/unattended.sh --check-specs dPlacedRequest TOOL-dPlacedRequest-46` report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker and the driver's `--check-specs`; no other.

### Non-goals

No product code, no commit, no index render, no status flip (it stays INPROGRESS), no spec other than
TOOL-dPlacedRequest-46, and no fork left open. Pin every figure you write with DERIVED or PINNED, and never quote a
check's hit literally in prose.
