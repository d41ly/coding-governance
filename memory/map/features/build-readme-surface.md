# build README surface — the slot contract and the four generated regions

```toml
feature = "build-readme-surface"
title = "A build README is mostly generated, and its authored slots are positional"
status = "shipped"
streams = ["tooling"]
decisions = []

[claims]
gate-legs = ["build README slot contract"]
kits = []
git-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "tools/memory-tree/gen_build_index.py",
]
```

## Constraints & why

**The slot sequence is positional, not delimited.** Front matter, title, ONE authored prose block,
the authored `roster:units` plan, then the generated regions. Bounding the prose with markers instead
was considered and refused by the owner: it would have let authored content sit anywhere and made the
contract a labelling convention rather than a shape.

**`--write` creates a missing region pair; `--check` never demands one.** This asymmetry is the whole
reason a new region can ship without a corpus-wide re-render inside its own commit. Both verbs call
`plan()`, so the flag lives there — `create_missing`, default false, set only on the write path. If a
create-if-missing step ever runs under `--check`, every un-paired README reports stale and the
asymmetry silently inverts; the `--selftest` arm "check is silent about an absent region pair" is the
one that fails when that happens.

**The slot refusal is unreachable from `plan()`, `--write` and `--check`.** The generator must keep
rendering a tree it would refuse to grade, or a corpus that violates the contract cannot be rendered
into compliance. `--check-format` is the only caller, and the gate leg is what makes it binding.

**The `roster:units` pair is authored and this generator never writes into it.** The unattended kit's
`check_authorization` byte-compares that slice across a run's pinned BASE, so a renderer touching it
would invalidate every run authorized against the file. It appears in the module only so the slot
walk can find it.

**The roster is wrapped, never counted.** `TOOL-aMouldedFolio-2` renders the full roster here and only
its count in `LIVE.md` and the ledger, and `render_region`'s own comment states that `unit(s)` and
`ids` answer different questions. The wrap width is one tier below the line cap because the
entry-budget check refuses to pin its locale, so a render sitting exactly at the cap would pass on one
node and red on another.

**Edges are build SLUGS, and only `parents:` is authored.** A slug joins no roster, so the edge region
leaves `LIVE.md` and both ledger shards byte-neutral. The child set is derived by inverting the parent
declaration: authoring both directions would be two answers to one question, which is the shape
`TOOL-aMouldedFolio-1` refused when it declined a front-matter schema.

## Shared seams

`apply_region` takes its marker pair as an argument and DEFAULTS to the build-index constants. The
default is load-bearing rather than convenient: `tools/memory-tree/marker-contract.test.sh` is a
second positional caller, so a bare signature change breaks a gate leg.

`insert_region` anchors on sibling REGIONS, never on prose, because over a README that violates the
slot sequence there is no well-defined "after the prose" point — and that is the branch every corpus
write takes until the corpus is conformed.

The document inventory parses no part of a record's filename. Five files under `legacy-files.txt`
carry grandfathered names, and a renderer that parsed names would have to waive them or degrade them.

## Reuse affordance

seam: `apply_region(text, region, path, mark_open, mark_close)` — splice a marker-delimited region in
any authored markdown file, with three refusals (no pair, more than one pair, inverted order) that
name the pair they were called with.
seam: `slot_violations(text, path)` — the two-trigger slot walk, returning `(line, reason)` pairs.
seam: `GEN_REGIONS` — the canonical region order; appending an entry registers a new region for both
creation and rendering.

## Gaps

- The roster-wrapping half of the corpus surgery never fired. `--check-format` cannot identify an
  authored plan that is not already wrapped, and an unwrapped plan is legal, so twelve build READMEs
  carrying a roster table still have no `roster:units` pair. Making the pair mandatory is
  `TOOL-cBriefedPilot-18` on another node.
- The `order` verb is PERMITTED and not required, so the build-order region is empty for every build
  that has not adopted it. Requiring it needs a dated cutoff, which the owner deferred to a follow-up.
- Two build READMEs sit in `curation-debt.txt` above the byte tier they entered. Both belong to other
  builds, and each row drains when that build's owner curates it.
