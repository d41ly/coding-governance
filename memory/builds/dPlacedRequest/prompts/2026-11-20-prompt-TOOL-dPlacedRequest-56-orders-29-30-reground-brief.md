**Serves:** research TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60

# Brief — dPlacedRequest: the order-29 and order-30 units re-grounded before their builds

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

Units 56 and 57 (order 29) and 58 and 60 (order 30), all DEFERRED, repair units this run has since built and
CLOSED, 52 to 55 among them. Spec 52 rev-10 moved its AC11 to AC14, AC17 and AC29 into spec 55, and spec 54 rev-6
dropped its AC3; these four specs still cite some of those labels. The charter's P19 keeps built work out of
in-place rewrites, and a builder writes no spec. The facts the tree now fixes:

- The version-bump oracle the close runs is the block in CLOSED spec 55's section 4 (exit 0 on a clean walk, 1 when a
  version line moved, 2 on a refusal); spec 44's block is superseded there. It is not product code.
- The placed request race is unit 48's region-eight block in `tools/unattended/unattended.test.sh` as unit 52
  rebuilt it: up to three attempts, each clearing its own handshake files, an overrun or a broken lock discarded.
- The base an observing run passes the oracle is the run's pinned BASE as RUN.md records it.

Re-ground all four specs so a builder can build each as written, each ruling a fork in that spec's §8 marked
`RESOLVED (agent, 2026-11-20, delegated): <option>, rung 3; <reason>. widens: none · relaxes: none`.

### Items

1. F-fold: an amendment one of these four orders to another of the four (for example 58 and 60 on 56 or 57) is made once, now, in the target spec, and the ordering unit reduces to an observation of that text.
2. F-oracle: an item that corrects the oracle cannot edit CLOSED spec 55. Rule the home so the close still runs exactly one oracle: the recommended answer is that the last of these units to correct it carries the whole corrected block in its own section 4, names spec 55's block superseded there (never edited), and every earlier text names the new block. If an item's correction is already true of spec 55's block, mark the item satisfied and reduce it to its observation.
3. F-closed-specs: every item that edits, bumps or rewrites a CLOSED spec in place is re-scoped: a product change still needed is built and observed; a text-only finding on a closed spec is resolved in this spec's own §4, naming the closing mechanism, and the closed spec is untouched.
4. Probe every item against the tree and cite where it stands by `path#symbol`; replace every cite of a moved or dropped criterion with the criterion that now holds it (spec 55's AC labels for the oracle, unit 52's rebuilt race block for the race); an item a landed unit satisfies is marked so and reduced to its observation or dropped. Narrow each unit to what is left, and say what was narrowed.
5. Replace every line citation with a `path#symbol` citation or a blob pin and every bare file-stem section reference with its alias tag; keep each spec within the live-spec size cap; leave no fork open.

### Acceptance

Specs 56, 57, 58 and 60 each at a new rev carry their resolved forks, every amendment the re-grounding found,
`path#symbol` citations and one §9 line naming this brief; `check-memory-hygiene.sh --only 12,25 --spec`, the
spec-token checker, a PLAIN `python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dPlacedRequest <id>` report nothing for each.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the pinned-facts check, the driver's
`--check-specs` and the naming lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip (all four stay DEFERRED), no spec other than these four.
Pin every figure you write with DERIVED or PINNED on its own line (the pinned-facts check's `--shrink` mode reads
green over reds, so read its plain run), never let a section sign or a section number stand before a unit word, and
never quote a check's hit literally in prose.
