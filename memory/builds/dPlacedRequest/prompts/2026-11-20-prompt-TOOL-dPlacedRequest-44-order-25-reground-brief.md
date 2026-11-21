**Serves:** research TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50

# Brief — dPlacedRequest: the order-25 units re-grounded before their builds

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

Units 44, 45, 48 and 50 (order 25, all DEFERRED) each repair a unit this run has since built and CLOSED:
`TOOL-dPlacedRequest-43` (rev-11, CLOSED at c96319ad2) and `TOOL-dPlacedRequest-47` (rev-7, CLOSED at c0c7531b8).
Unit 43's re-ground already folded unit 44's S3 and unit 48's S4 into spec 43 (its F6), and spec 47 rev-7 already
carries the mixed-tenure criterion unit 50 asks for. The charter's P19 keeps built work out of in-place rewrites, so
no item of these four may edit spec 43 or spec 47. Re-ground all four specs so a builder can build each as written,
each ruling a fork in that spec's §8 marked
`RESOLVED (agent, 2026-11-20, delegated): <option>, rung 3; <reason>. widens: none · relaxes: none`.

### Items

1. Spec 44: S3 and AC4 are satisfied by spec 43 rev-11's F6 (AC24 runs this unit's oracle, and spec 43 holds no first-parent walk); reduce them to an observation of spec 43's text. Probe where the oracle of S1 and S2 is to live and run (the close's version-bump check), and amend S1, S2 and §4 to the tree's names.
2. Spec 45: its motivation cites spec 43 S24 walking the first parent, which rev-11 no longer does; restate §1 against the class record alone (the defect stays real for any check run on a prepared merge). Probe the class record under `memory/gotchas/` and the lander's merge construction by `path#symbol`, and amend S1, S2 and the criteria to the tree.
3. Spec 48: unit 43 built the request lock, and `tools/unattended/unattended.sh#write_request_record` now copies into a temporary sibling (the key's file name with a process-id suffix) and then moves it with `mv -n`, so a stub matching a copy whose destination is the stored `.md` never fires. Amend S1's placement seam to the copy the tree makes, re-check S2's expected outcomes against the lock (a busy lock answers exit 2 naming `requests.lock`), and reduce S4 and AC4 to an observation of spec 43's AC30 (already folded).
4. Spec 50: no edit to spec 47. Rule whether spec 47 rev-7's AC1 (the mixed tenure, built as an arm in `tools/unattended/unattended.test.sh`) already reaches the guard past every earlier stop; if it does, reduce S1 and S2 to observations of that arm and build nothing, else narrow the unit to the one extra arm row it still owes (the variant spec 47 does not plant), placed beside unit 47's block. Probe the arm's block and the driver's `read_claims` walk before ruling, and pin each measured figure.
5. In every one of the four specs: replace each line citation with a `path#symbol` citation or a blob pin, each bare file-stem section reference with its alias tag, and each claim the tree contradicts with the tree's reading; leave no fork open.

### Acceptance

Specs 44, 45, 48 and 50 each at a new rev carry their resolved forks and amendments, `path#symbol` citations and one
§9 line naming this brief; `check-memory-hygiene.sh --only 12,25 --spec`, the spec-token checker and
`bash tools/unattended/unattended.sh --check-specs dPlacedRequest <id>` report nothing for each.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the driver's `--check-specs` and the naming
lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip (all four stay DEFERRED), no spec other than these four
(specs 43 and 47 are CLOSED and stay untouched). Pin every figure you write with DERIVED or PINNED on its own line,
never let a section sign or a section number stand before a unit word, and never quote a check's hit literally in
prose.
