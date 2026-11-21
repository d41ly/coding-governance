**Serves:** research TOOL-dPlacedRequest-17

# Brief — dPlacedRequest: TOOL-dPlacedRequest-17's divergence, resolved

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

TOOL-dPlacedRequest-17's builder returned a DIVERGENCE (run `wf_47eb729e-d38`) and committed nothing: the spec at
rev-4 leaves the verdict of a lease with no renewing commit undefined, contradicts itself on which commits feed the
renewing beat, says nothing of the existing suite arms the observer clock flips, and cites stale lines. Revise the
spec so it can be built as written, recording the main loop's fork ruling.

### Items

1. New fork in §8, marked resolved: "What anchors the age of a lease whose chain carries no renewing commit?" Options: (a) `unknown`, so it never expires and is never taken over; (b) the current tenure's opening commit counts as a renewing beat whatever its `renews` line says, so its first sighting anchors the age; (c) stale at once. Mark it `RESOLVED (agent, 2026-11-19, delegated): (b), rung 3; (a) fails §5's own take-over risk and §4 Rollout, (c) lets any node take a live run, a second driver (veto 3); TOOL-dPlacedRequest-25 makes the writer stamp the opener `renews: yes`, and this reader rule holds without it. widens: none · relaxes: none`. Amend S3 and §4 "The age pass" so the walk counts the tenure's opening commit as renewing, and add one acceptance criterion observing a chain whose commits all carry `renews: no`: it reads live inside `leases.expiry-hours` of the opener's first sighting and stale after it.
2. The commit set: S2 reads the lease's whole first-parent chain and §4 step 2 groups by the `gov-claim <tail>` header. Make both say the one rule: walk the first-parent chain from the tip and stop at the current tenure's opening commit (TOOL-dPlacedRequest-26 names that bound; cite it as a hands-off), so a migrated lease's legacy commits never feed the renewing beat.
3. The existing suite arms: §5 Files touched and §6 name that this unit re-stages, on planted feed lines, the arms of `tools/unattended/unattended.test.sh` that make a claim stale by planting an old `beat-utc` or seed leases with `renews: no` (the five-verdict AC2 arm, the `foreign-stale` rows of the claim-table arm, AC5, AC8, AC18, AC19, GH36 AC6, DPR1 AC2, and any other the builder's inventory finds), so they keep their verdicts under the observer clock; the inventory is made by `git grep` over the suite at build time, never typed from this list alone.
4. Stale citations: replace `:2172-2186`/`:2180` with `tools/unattended/unattended.sh#read_claims`, `:2269-2275` with `tools/unattended/unattended.sh#check_claim_writable`, and `STOPS.template.md:198-204` with a citation of section 7's `| claim | verdict |` table by heading.

### Acceptance

Spec 17 carries the resolved fork, the amended S2, S3 and §4, the new criterion, the re-staging scope and the four
corrected citations, one rev bump to rev-5 and its §9 line naming this brief and the divergence; the memory hygiene
gate `--only 12,25 --spec` over it and the spec-token checker over it report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec` on the spec), the spec-token checker and the naming lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip (it stays INPROGRESS), no spec other than
TOOL-dPlacedRequest-17. Pin every measured figure you write on its line with DERIVED or PINNED, and cite code as
`path#symbol`, never a bare `path:line`.
