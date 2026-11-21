**Serves:** research TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51

# Brief — dPlacedRequest: the order-26 units re-grounded before their builds

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

Units 49 and 51 (order 26, both DEFERRED) repair units this run has since built and CLOSED. Unit 49 batches 34 minor
findings of the round-2 promotions' audit landing on twelve units (among them 34, 36, 37, 38, 43, 44, 45, 47 and 48,
all CLOSED); unit 51 repairs the merge-class record unit 45 just extended, and cites unit 50, which closed as an
observation-only unit. The charter's P19 keeps built work out of in-place rewrites: no item of these two may edit a
CLOSED spec, and a builder may write no spec at all. Re-ground both specs so a builder can build each as written,
each ruling a fork in that spec's §8 marked
`RESOLVED (agent, 2026-11-20, delegated): <option>, rung 3; <reason>. widens: none · relaxes: none`.

### Items

1. F-closed-specs (both specs): every item that edits, bumps or rewrites a CLOSED spec in place is re-scoped. Where the finding still needs a product change, the item builds that change and observes it; where the finding is about the closed spec's text only, the item is recorded here as resolved by naming the closing mechanism in this spec's own §4, and the closed spec is not touched. Say which items moved and why.
2. Probe every item of both specs against the tree. For each, cite where it now stands by `path#symbol`: an item a landed unit already satisfies is marked so (naming the unit) and reduced to its observation or dropped; an item whose cited symbol, verb, file, field, flag or bound moved is amended to the tree's name; a reader marked as not in tree is replaced with the reader as built. Spec 49's items on the version oracle, the request lock and the card bounds must agree with what units 43, 44 and 48 built (the oracle in spec 44's section-4 block, the lock answering exit 2, and the separate card publish bound). Narrow each unit to what is left, and say what was narrowed.
3. Spec 51: check the merge-class record's rows as unit 45 left them and amend the split, its criterion and any cite of unit 50 to the tree; unit 50 built nothing and observes unit 47's arm.
4. Replace every line citation with a `path#symbol` citation or a blob pin, and every bare file-stem section reference with its alias tag. Keep each spec within the live-spec size cap the spec-token checker reads.
5. If an amendment leaves a real choice the tree cannot settle, decide it by the same rung and record it resolved; leave no fork open.

### Acceptance

Specs 49 and 51 each at a new rev carry their resolved forks, every amendment the re-grounding found, `path#symbol`
citations and one §9 line naming this brief; `check-memory-hygiene.sh --only 12,25 --spec`, the spec-token checker,
a PLAIN `python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dPlacedRequest <id>` report nothing for each.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the pinned-facts check, the driver's
`--check-specs` and the naming lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip (both stay DEFERRED), no spec other than these two.
Pin every figure you write with DERIVED or PINNED on its own line (the pinned-facts check's `--shrink` mode reads
green over reds, so read its plain run), never let a section sign or a section number stand before a unit word, and
never quote a check's hit literally in prose.
