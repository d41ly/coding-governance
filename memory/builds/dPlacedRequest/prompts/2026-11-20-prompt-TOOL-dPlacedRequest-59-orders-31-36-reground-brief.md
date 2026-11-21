**Serves:** research TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64

# Brief — dPlacedRequest: the last five units re-grounded before their builds

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

Units 59 (order 31), 61 (33), 62 (34), 63 (35) and 64 (36), all DEFERRED, are the build's last. They repair units this
run has since built and CLOSED (52 to 58 and 60 among them), and several of them edit other specs in place: 61 and 63
list the build's spec folder as a file they touch, and 62 edits specs 59 and 61. The charter's P19 keeps built work
out of in-place rewrites, and a builder writes no spec. The facts the tree now fixes:

- The version-bump oracle the close runs is the block in CLOSED spec 56's section 4 (spec 55's block is superseded
  there); the close passes it the run's pinned BASE as spec 57 reads it through the library's `extract_run_facts`.
  It is not product code.
- The placed request race is unit 52's rebuilt block in region eight of `tools/unattended/unattended.test.sh`, with
  unit 58's absence check before call A.
- Spec 56 now hands off to spec 57 (57 consumes from 56). Spec 61's S7 (moving 56's order and editing its edge), S10
  (the run-facts read 57 already uses) and S14 (34's AC59, frozen) and spec 59's cite of 56's per-attempt sketch
  (gone) all predate that.

Re-ground all five specs so a builder can build each as written, each ruling a fork in that spec's §8 marked
`RESOLVED (agent, 2026-11-20, delegated): <option>, rung 3; <reason>. widens: none · relaxes: none`.

### Items

1. F-fold: an amendment one of these five orders to another of the five (62 on 59 and 61, and any other) is made once, now, in the target spec, and the ordering unit reduces to an observation of that text.
2. F-closed-specs: every item that edits, bumps, re-orders or rewrites a CLOSED spec in place is re-scoped: a product change still needed is built and observed; a text-only finding on a closed spec is resolved in this spec's own §4, naming the closing mechanism, and the closed spec is untouched. No unit's Files touched may name the spec folder or another spec after this pass.
3. F-oracle: an item that corrects the oracle cannot edit CLOSED spec 56. If an item's correction is already true of spec 56's block, mark it satisfied and reduce it to its observation; otherwise the last of these units to correct it carries the whole corrected block in its own section 4, names spec 56's block superseded there (never edited), and every earlier text names the new block, so the close runs exactly one oracle.
4. Probe every item against the tree and cite where it stands by `path#symbol`; replace every cite of a moved, dropped or superseded criterion, sketch or block with what now holds it; an item a landed unit satisfies is marked so and reduced to its observation or dropped. Narrow each unit to what is left, and say what was narrowed.
5. Replace every line citation with a `path#symbol` citation or a blob pin and every bare file-stem section reference with its alias tag; keep each spec within the live-spec size cap; leave no fork open.

### Acceptance

Specs 59, 61, 62, 63 and 64 each at a new rev carry their resolved forks, every amendment the re-grounding found,
`path#symbol` citations and one §9 line naming this brief; `check-memory-hygiene.sh --only 12,25 --spec`, the
spec-token checker, a PLAIN `python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dPlacedRequest <id>` report nothing for each.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the pinned-facts check, the driver's
`--check-specs` and the naming lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip (all five stay DEFERRED), no spec other than these five.
Pin every figure you write with DERIVED or PINNED on its own line (the pinned-facts check's `--shrink` mode reads
green over reds, so read its plain run), never let a section sign or a section number stand before a unit word, and
never quote a check's hit literally in prose.
