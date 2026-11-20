**Serves:** research TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55

# Brief — dPlacedRequest: the order-27 and order-28 units re-grounded before their builds

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

Units 52 (order 27) and 53, 54 and 55 (order 28), all DEFERRED, repair units this run has since built and CLOSED
(among them 43, 44, 45, 47, 48, 49, 50 and 51), and two of them repair unit 52 itself. The charter's P19 keeps built
work out of in-place rewrites, and a builder writes no spec. Three facts the tree now fixes:

- The version-bump oracle is not product code: it is the command block in CLOSED spec 44's section 4, run once at the
  close on the prepared merge, and on a clean build its last `grep` exits 1, the same code as its refusal of an empty
  walk.
- The placed request race is unit 48's region-eight block in `tools/unattended/unattended.test.sh`, holding the copy
  onto the temporary `<key>.md.<pid>` sibling, with the lock's 5 s wait (PINNED) and the second call refused with exit 2.
- Unit 43 rev-11 no longer carries the 48128 figure; its size item reads the spec-token checker's cap.

Re-ground all four specs so a builder can build each as written, each ruling a fork in that spec's §8 marked
`RESOLVED (agent, 2026-11-20, delegated): <option>, rung 3; <reason>. widens: none · relaxes: none`.

### Items

1. F-fold (52, 53): spec 52 is still DEFERRED, so the in-place rewrite of spec 52's AC1, AC6 and AC9 that spec 53 orders is a spec act done here once, now, in spec 52; spec 53 reduces to an observation of spec 52's text. Apply the same rule to any other amendment one of these four orders to another of the four.
2. F-oracle-home (52, 54, 55): spec 44 is CLOSED, so a correction to the oracle cannot land in its section 4. Rule where the corrected oracle lives so the close runs exactly one oracle: the recommended answer is that the last of these units to correct it carries the whole corrected block in its own section 4, every earlier oracle text names that block as the one the close runs, and spec 44's block is named superseded there (never edited). Fold the corrections of 52's oracle item, 54 (the walk only this build's own prepared merge) and 55 (the verdict from the walk's own exit status, not grep's) into that one block, and name it in each spec.
3. F-closed-specs (all four): every item that edits, bumps or rewrites a CLOSED spec in place is re-scoped: a product change still needed is built and observed; a text-only finding on a closed spec is resolved in this spec's own §4, naming the closing mechanism, and the closed spec is untouched.
4. Probe every item of the four against the tree and cite where it stands by `path#symbol`: an item a landed unit satisfies is marked so and reduced to its observation or dropped; an item whose symbol, verb, file, field, flag, bound or figure moved is amended (spec 52's AC9 and AC10 to the checker's cap, its race items to unit 48's block as built, its references to spec 49's items by the S-ids spec 49 rev-7 kept). Narrow each unit to what is left, and say what was narrowed.
5. Replace every line citation with a `path#symbol` citation or a blob pin and every bare file-stem section reference with its alias tag; keep each spec within the live-spec size cap; leave no fork open.

### Acceptance

Specs 52, 53, 54 and 55 each at a new rev carry their resolved forks, every amendment the re-grounding found,
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
