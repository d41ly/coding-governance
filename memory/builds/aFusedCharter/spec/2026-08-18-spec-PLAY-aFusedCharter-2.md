# PLAY-aFusedCharter-2 — every session emits a shaped overview of its own state, and the shapes get one grammar

**Status:** OPEN · rev-1 · 2026-08-18 · node a · Tier-2 · base 497d25d0 · streams playbook

## 1. Goal

Add a BINDING slug-keyed pair of micro-formats so a session's final message always carries a
machine-shaped overview of which build it is in, how far through, and which spec governs it — and
put the existing micro-formats under one stated grammar, so the block is a compilable definition set
rather than seven independently-invented shapes.

## 2. Scope (IN)

**S1 — State the grammar, once, as one paragraph.** A shape is a HEAD, the joiner, and a TAIL. The
head is one keyword from a closed set with fixed case. The joiner appears exactly once. Tail fields
are separated by one separator glyph and nothing else. No parentheses, except markdown-link syntax.
No colon as a joiner or a label — a colon survives only glued to a value, as a port. Placeholders
are lowercase angle-bracket names, alternation written with a pipe. Five glyphs are pinned. The
grammar binds shape SYNTAX and never value BYTES: an opaque field such as a commit subject or a
reason keeps whatever characters it has, so the bans do not reach inside one.

**S2 — State R1: an emitted micro-format is a markdown list item.** A list marker at column zero,
then the shape's bytes. No backticks, no fence, no bold, no heading. Nothing before the marker and
nothing after the last field, one shape per line. Two reasons, neither of them taste. Backticks and
fences defeat the clickable-link rule `PLAY-aFusedCharter-1` S5 folds into this same section, which
breaks every shape carrying a link. And a list item cannot merge with its neighbour, which is what
the two-line pair in S3 depends on. The consequence is that the definition list renders
byte-identically to a correct emission minus its backticks, so the instruction to an agent is: copy
the bullet, fill the angle brackets.

**S3 — Add the two slug-keyed shapes, emitted as an adjacent ordered pair.**

```
- BUILD — <slug> · Tier-<n> · <done>/<total> <step> · left <ids|none|unspecced>
- SPEC — [<unit-id>](<path>) · review <ids|none> · open <ids|none>
```

Five adjacency rules travel with them, and they are the substance of the shape rather than
decoration. The pair is emitted in the state block of **every** final message while a build is in
progress — that is the BINDING half, and it is the one rule in this section with no routine-length
escape. `SPEC` is omitted before a spec exists, and `left` then reads the unspecced token. `SPEC`'s
link label is the unit id and never the filename. `review` and `open` are build-wide over Tier-2
units only, and the whole clause drops for a build holding none. The tier on `BUILD` is the tier of
the unit named by the CURRENT step, not the build's maximum.

**S4 — Rewrite the seven existing shapes to satisfy the grammar.** Every one of them violates it
today, which is the evidence that a grammar was missing rather than unenforced. `committed` puts
two fields ahead of the joiner. `pushed` carries a parenthetical. `skipped` and `READY` use a colon
as a label. `up` separates a credential with a slash. `gates GREEN` splits its keyword across the
head. The rewritten set is in `§4`'s Data model. This is a byte change to shapes this repo's own
records already contain, and `§3` states what that does not license.

**S5 — Bring two governed shapes into the block.** The skipped-leg shape and the
already-delivered-digest shape are defined today inside prose bullets elsewhere in the section,
which means the block is not the definition set it claims to be. Both move in and take the grammar.

**S6 — Extend the pre-send self-check** with one question: is every micro-format a bare list item
with no backticks, fence or bold? The self-check is a documented check and stays one; the machine
half is `TOOL-aFusedCharter-2`'s, and it grades the DEFINITIONS rather than the emission.

**S7 — Name the reuse.** The shapes are deliberately byte-compatible with the ones inCMS ratified,
so one grep serves both repos. That is stated in the section as the reason the names are `BUILD` and
`SPEC` rather than something gov-native, because a future editor who does not know it will
"improve" them apart.

## 3. Non-goals (OUT)

**No emission enforcement.** RESOLVED by the owner at kickoff: the rule is binding in the document
and a gate grades the definition block, but nothing machine-checks that a given final message
carried the pair. A Stop-hook validator is the known mechanism and is named as a follow-up.

**No rewriting of landed records.** S4 changes what a shape must look like from now on. Every
`memory/builds/` record and every archived ledger row carrying an old-shape line stays exactly as
written — they are records of what was emitted, not instances of a current rule.

**No new keyword beyond the two.** The closed set grows by exactly `BUILD` and `SPEC`.

**No `§16` restructure.** The section keeps its rule numbering and its scope clause. This unit edits
the micro-format block and the pre-send check inside it.

**Not the gate.** `TOOL-aFusedCharter-2` owns the parser and the leg.

## 4. Design

### Data model

The closed keyword set after this unit, with each shape's disposition. Every one is a definition
line inside the block.

| Shape | Disposition | What changes |
|---|---|---|
| `committed` | rewritten | fields move behind the joiner |
| `pushed` | rewritten | the parenthetical becomes two separated fields |
| `merged` | rewritten | the trailing gate clause becomes a separated field |
| `gates GREEN` | rewritten | the leg list becomes separated fields |
| `skipped` | moved in, rewritten | the colon label becomes the joiner |
| `up` | rewritten | the slash before a credential becomes a separator |
| `READY` | rewritten | the colon before the gate list becomes a separator |
| `unchanged` | moved in, rewritten | the head becomes a bare keyword |
| `⏳` | rewritten | the estimate parenthetical drops |
| `BUILD` | NEW | S3 |
| `SPEC` | NEW | S3 |

Two shapes carry an optional final field, and the block says which: the merged shape's post-merge
gate clause, present only when the scoped gate actually ran, and the spec shape's open-items clause.
An optional field that is not marked optional is indistinguishable from a missing one, which is what
makes this a data-model fact rather than a note.

### Migration

The shapes appear in this repo's own product prose as well as in its records: the template's `§16`
defines them and `AGENTS.md` will carry them through the render. Nothing else in the tree emits them
programmatically, so there is no code path to migrate — verified by searching the tracked tree for
each shape's leading keyword outside `memory/`.

### Alternatives rejected

**Invent gov-native keywords.** Rejected in S7's terms: two repos already share a fleet, a node
registry convention and half a dozen kits, and a divergent emission vocabulary would make a
cross-repo grep answer half a question.

**Define the pair without a grammar.** Rejected: seven shapes invented independently is precisely
how the block reached a state where five of them cannot be parsed by one rule. A gate over the
definitions is only possible if the definitions have a grammar to be graded against.

**Make the pair conditional on Tier 2.** Rejected: a Tier-1 unit inside a build still has a step and
a remaining scope, and the pair's whole value is that a reader never has to ask which build a
message belongs to.

### Files touched (estimate)

The converged ruleset's `§16` only. `AGENTS.md` receives the same bytes through
`PLAY-aFusedCharter-3`'s render and is not hand-edited here.

## 5. Production-readiness checklist

- security — the credential field in the up shape keeps its existing rule: never a real credential
  in chat, only where it lives. S4 changes that shape's separator and not its rule.
- perf / scale — N/A.
- a11y — N/A.
- i18n — the pinned glyph set is non-ASCII by construction, which is a real constraint on any
  consumer reading the block; the gate in `TOOL-aFusedCharter-2` must read bytes, not a
  locale-dependent decoding.
- error / empty / loading states — N/A.
- observability — the block becomes machine-parseable, which is the point.
- risks — the block costs bytes against a size gate with bounded headroom; `§6` measures it. A
  grammar stated loosely produces a gate that cannot be written, so `§1`'s single paragraph is the
  real deliverable and the shape list is its instances.
- testing + left-shift gates — `TOOL-aFusedCharter-2`.
- migration / rollback — document-only.
- user docs — N/A; the block IS agent-facing instruction.

## 6. Acceptance criteria

- **AC1** — When the block is read, every definition line satisfies the grammar stated above it,
  including the two new ones — the property `TOOL-aFusedCharter-2` will assert mechanically, checked
  here by hand first because a gate is not landed until its failing case has been observed.
- **AC2** — When a session with a build in progress composes a final message, its state block
  carries the `BUILD` line and, once a spec exists, the `SPEC` line immediately after it. Observable
  on this build's own wrap-up message, which is the first instance.
- **AC3** — When the section is searched, no definition line contains a backtick, and each begins at
  column zero with a list marker — `grep -nE '^- [A-Z⏳]' ` over the block returns every shape.
- **AC4** — When `bash tools/check-template-size.sh` runs after this unit, it exits 0 and the
  printed byte count is under `49152`.
- **AC5** — When the pre-send self-check is read, it carries the list-item question added by S6, so
  `grep -c 'bare list item' ` over the converged file returns at least `1`.
- **AC6** — When the two moved shapes are searched for with `grep -n`, neither is still defined in
  a prose bullet outside the block; each appears exactly once, as a definition line.

## 7. Gates

`template size <=48KiB` · `playbook parity` · `memory hygiene` · the full bar at the push boundary.
The new leg arrives with `TOOL-aFusedCharter-2` and is that unit's gate, not this one's.

## 8. Open questions

none — the fork below is RESOLVED and recorded in the build README.

- **F1 — how far does enforcement go?** RESOLVED (owner, 2026-08-18): doc-binding plus a gate over
  the definitions. A Stop-hook emission validator, landed dark at a user-visible channel and
  deriving its matchers from this block rather than from a third copy, is a follow-up and not part
  of this build.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft, written after the owner resolved F1 at kickoff.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "the micro-format shapes a work report emits"` returns no
dossier — the block is product prose inside the playbook and the map covers the machinery over it,
not its contents. The seam this unit reuses is external and is named in S7: inCMS ratified the same
grammar and the same two shapes in its own charter, with a hygiene check over the definitions and a
dark validator over the emission. This unit ports the grammar, R1 and the pair; the validator is
deliberately left behind per F1.

Recall terms used: `micro-format output discipline work report state block session slug build spec
grammar shape emission binding greppable byte-stable`. The binding prior record is
`PLAY-aPrunedCeremony-1`, which established this repo's output-discipline section, and the upstream
one is inCMS's charter-restructure unit, whose scope item four is the direct ancestor of S1 through
S4 and whose measurement — that eleven of fifteen shapes changed bytes to satisfy the grammar — is
what predicted S4's scope here.
