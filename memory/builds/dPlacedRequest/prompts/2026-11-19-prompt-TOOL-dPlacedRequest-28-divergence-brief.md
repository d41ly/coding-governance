**Serves:** research TOOL-dPlacedRequest-28

# Brief — dPlacedRequest: TOOL-dPlacedRequest-28's divergence, resolved

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

TOOL-dPlacedRequest-28's builder returned a DIVERGENCE (run `wf_2cdc917a-db6`) and committed nothing: at rev-3 the
spec's AC5 checks a call no code makes, so it can never go red; S2 names the driver's run-claim create without its
refusal shape, the read's home or a criterion; and the §4 refusal line names a holder nothing supplies. Revise the
spec to the main loop's three rulings so it can be built as written.

### Items

1. F2, the read's home. Add to §8, resolved: "Where does the create's feed read live, when every lease commit is built in `tools/unattended/unattended.sh#write_claim`?" (a) in `write_claim`, once, for every create with an empty parent, the `--lease` verbs and the driver's own claims alike; (b) at each caller. Mark `RESOLVED (agent, 2026-11-19, delegated): (a), rung 3; one commit builder, one read, and no caller can skip it. widens: none · relaxes: none`. Amend S1, S4 and §4 so the read sits in `write_claim` and the inline TOOL-dPlacedRequest-16 S5 read in `run_lease_verb` moves into it. Rewrite AC5 as a behaviour probe: `write_claim` with a create over a feed whose newest event names the ref builds no parentless commit (the commit's parent is the feed's commit), red on a staged copy whose `write_claim` skips the read.
2. F3, the driver's create on a feed tombstone. Resolved: `write_claim` returns a code of its own for a tombstone, distinct from rc 1's lost race, and the driver's callers map it exactly as TOOL-dPlacedRequest-16 §4 "The class order" maps a tombstone: the preflight and take-over columns fail check 107, the holder column check 108, each message carrying `tombstone`; the status column announces one line carrying `tombstone`, writes nothing and leaves the exit status unchanged; the `--lease` verbs print `lease refused — tombstone` and exit 1. Mark `RESOLVED (agent, 2026-11-19, delegated): a distinct return code mapped as unit 16's class order maps a tombstone, rung 3; one refusal vocabulary for a tombstone wherever it is met. widens: none · relaxes: none`. Add one acceptance criterion: `--preflight` of a slug whose feed's newest event is a build tombstone (no remote ref) exits 1 with check 107 and `tombstone`, and the remote gains no ref.
3. The refusal line: §4 Design's line keeps the tree's wording, naming the feed commit (this node's feed last saw its tombstone at that commit) and no holder; drop `<holder in the feed's record>`.
4. Cite code as `path#symbol` throughout the revised sections.

### Acceptance

Spec 28 at rev-4 carries F2 and F3 resolved, S1, S2, S4, §4 and AC5 amended to them, the new preflight criterion,
the refusal line corrected, and one §9 line naming this brief and the divergence; `check-memory-hygiene.sh --only
12,25 --spec` and the spec-token checker over it report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker and the naming lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip (it stays INPROGRESS), no spec other than
TOOL-dPlacedRequest-28. Pin every figure you write with DERIVED or PINNED, never let a section sign stand before a
unit word, and never quote a check's hit literally in prose.
