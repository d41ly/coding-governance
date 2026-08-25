# build README surface — the slot contract, the heading canon and the three generated regions

```toml
feature = "build-readme-surface"
title = "A build README is mostly generated, and its authored slots are positional and named"
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

**The `gen:build-units` pair is NESTED inside `build-index`, and is the units table's address.**
`TOOL-aBoundedVerdict-11` added it because the unattended driver selected unit rows out of the
enclosing region by ROW SHAPE (`^| \[`) while this generator renders a records table into that same
region — so every review and journal record counted as an unfinished unit. Nested rather than a fifth
`GEN_REGIONS` entry: that tuple drives region CREATION and the canonical-order check, and registering
it there would move the units table outside the region three legs and two dossiers bracket. So the
enclosing region's extent is byte-unchanged and the driver gets a name to read instead of a shape to
guess. Consumers address it with `region()` like any other pair; it is not in `GEN_REGIONS` and must
not be added there.

**The `roster:units` pair is authored, this generator never writes into it, and it is NARROWED — not
retired.** `check_authorization` byte-compared that slice across a run's pinned BASE, so a renderer
touching it would have invalidated every run authorized against the file, which is why it appears in
the module only so the slot walk can find it. `TOOL-aBoundedVerdict-11` moves the frozen
authorization scope to the GENERATED region's unit-ID SET (BASE ⊆ HEAD, never row bytes, because
those carry status and rev and would refuse every run that built anything), and it moved FOUR of the
pair's five readers. **The fifth is live and deliberate**: `roster_ids` in the unattended driver
still reads the authored pair, because it answers a question the generated region cannot — which
units are PLANNED but unspecced — and pointing it at the generated region was tried inside that same
unit and reverted as a tautology. That spec was corrected at rev-8 to say so. Eleven build READMEs
carry the pair, measured with `git ls-files 'memory/builds/*/README.md' | xargs grep -lF`; whether it
becomes mandatory or its readers are deleted together is an open owner decision.

**The roster is wrapped, never counted.** `TOOL-aMouldedFolio-2` renders the full roster here and only
its count in `LIVE.md` and the ledger, and `render_region`'s own comment states that `unit(s)` and
`ids` answer different questions. The wrap width is one tier below the line cap because the
entry-budget check refuses to pin its locale, so a render sitting exactly at the cap would pass on one
node and red on another.

**Edges are build SLUGS, and only `parents:` is authored.** A slug joins no roster, so the edge region
leaves `LIVE.md` and both ledger shards byte-neutral. The child set is derived by inverting the parent
declaration: authoring both directions would be two answers to one question, which is the shape
`TOOL-aMouldedFolio-1` refused when it declined a front-matter schema.

**The authored half is a CLOSED HEADING CANON, and it is OPT-IN per file.** `SLOT_CANON` declares
five slots in order — the immutable description (which IS the goal bound M3's rescope rule reads),
expected improvements, detriments if not built, build-level rules, parked decisions — with per-slot
`empty_ok` and `bullets` flags. `slot_violations` grades the canon only when its caller passes
`canon=True`, which `cmd_check_format` does for a path
`memory/project/readme-contract.txt` declares BOUND. That registry is asserted in BOTH directions and
its exempt pin is an EQUALITY, so a pin left high after a drain reds rather than going slack. One
README is bound today and the leg names its own reach on every run; `--survey` grades every README
regardless, and `--report` prints each slot's bytes against its declared ceiling and its recorded
high-water. Ceilings live in `build-readme-slot-limits.txt` and high-waters in a separate file,
because `--bump` writes the second and must never touch the first. Adopters receive the rows with no
ceiling values, which is the announced UNARMED state; a MISSING row is a refusal.

**Position is still the mechanism.** No slot has a marker pair. `TOOL-aRuledFrontispiece-1` refused
per-slot markers for a reason that still holds — two more lines per README to solve what position
already solves — and refused heading-DETECTION for a second reason that expired at
`TOOL-aBoundedVerdict-11`. Reading those two refusals as one is how the live rule gets deleted with
its dead neighbour.

**The no-markers hole.** `slot_violations` returned `[]` unconditionally when it found no generated
pair, so a README with no markers passed every trigger however much prose it held — measured on a
45,185-byte fixture that reported clean. It is now a violation. No live file reaches it, which is why
it went unseen.

**Order is authored on the SPECS and computed here.** `· order <n>` in a status header is a positive
integer, at most once; ties are the parallel group, gaps are permitted so a retired unit needs no
renumber, and a malformed value REFUSES rather than rendering a plausible step. The roster carries
Order and Tier and sorts by build order; the link cell stays first and status stays a whole delimited
cell, because the unattended driver selects on both.

**Records render in the SPEC they serve.** A `gen:spec-records` pair sits between the status header
and `## 1. Goal` — the one place check 12 does not look, so no eleventh section and no cutoff. The
build README's document inventory and its records table are GONE; the two coverage joins survive
there and now render UNCONDITIONALLY, because each used to hide behind its own non-empty test and a
fully-covered build rendered nothing at all.

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

- The roster-wrapping half of the corpus surgery never fired, and it is now MOOT rather than pending:
  `--check-format` cannot identify an authored plan that is not already wrapped, an unwrapped plan is
  legal, and twelve build READMEs carrying a roster table have no `roster:units` pair — but
  `TOOL-aBoundedVerdict-11` moved four of that pair's five readers instead of wrapping the corpus,
  and the population still matters to the fifth. **The deferral this bullet used to carry was stale**: it named
  `TOOL-cBriefedPilot-18` as the owner of making the pair mandatory, and that unit is CLOSED with its
  own AC9 asserting a grep returns zero where it returns two — the requirement was never established.
  `TOOL-aPacedTurnstile-14` then hit the same gap from another node's live run and is closed by
  `TOOL-aBoundedVerdict-11` S8.
- The `order` verb is PERMITTED and not required, so the build-order region is empty for every build
  that has not adopted it. Requiring it needs a dated cutoff, which the owner deferred to a follow-up.
- Two build READMEs sit in `curation-debt.txt` above the byte tier they entered. Both belong to other
  builds, and each row drains when that build's owner curates it.
