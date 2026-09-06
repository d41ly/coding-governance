# annotation style — the rendered convention for a comment that cites a record

```toml
feature = "annotation-style"
title = "Annotation style: what a code comment citing a governance record must carry"
status = "shipped"
streams = ["tooling"]
decisions = ["TOOL-aKeyedAnnotation-1"]

[claims]
gate-legs = []
kits = []
git-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = ["ANNOTATION-STYLE.md"]
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "tools/memory-tree/ANNOTATION-STYLE.template.md",
  "memory/guides/ANNOTATION-STYLE.md",
]
```

## Constraints & why

**An annotation layer already existed and nobody had declared it.** Product source cites unit ids
densely, and the drift-audit shipped-evidence oracle consumes those citations as evidence a unit
shipped — so the layer is load-bearing. Nothing graded it, nothing wrote it down, and one of its
pointers had resolved to no record for its entire life.

**Every mechanism the obvious remedy wanted was refused on measurement.** A grammar, a marker kind,
a source-side gate, a recall-corpus entry, a tokenizer change: each was designed and rejected in the
design pass this feature came from, and the strongest of them — a marked annotation in the existing
`gov:` namespace — was rejected while being acknowledged as genuinely fixing three rot paths. It is
a second id grammar in a repo whose own catalogue names that class, and it buys correctness for a
mandate the pass says must not exist. So this feature ships PROSE and nothing else.

**Annotation stays VOLUNTARY, and the whole design rests on it.** The shipped-evidence oracle
discriminates only because citation is sparse and late. Make citation mandatory and every unit is
cited the moment it is written, so the signal answers "was this specced" instead of "did this ship".
A mandate would then need the marker, the marker a grammar, and the grammar a gate — the three
things measurement had already refused.

**The evidence is the required half and the id is the optional pointer.** Measured over comment
blocks under `tools/`, carrying an id and carrying a measurement are two largely disjoint practices,
and the id-only population is the one whose content is nearest zero. Both real dangling pointers sat
in exactly that shape. Hence the one-line test the guide is built around: delete the id and the
block must still be worth reading.

## Shared seams

- **The kit's `render_doc` seam in `tools/memory-tree/adopt-memory-tree.sh`** — one conditional line
  per rendered guide, shared with the hygiene rules, the spec format and the build method. This
  feature adds a fourth caller and no mechanism.
- **`kit-dogfood-parity.test.sh`'s `PAIRS` string** — the hand-kept population every rendered
  document pair joins. Four carriers must agree for one rendered guide: that literal, the
  `[[files]] role = "rendered"` stanza in `tools/memory-tree/kit.toml`, that leg's `guard` inside the
  same descriptor, and its `guard` row in `tools/gate-legs.json`. The descriptor guard is the one
  that SHIPS, so patching this repo's manifest alone exports the hole rather than closing it.
- **The exclusion lists over the build method's filename** — kept in two hand-written copies, in the
  adopter script's seeder block and in `tools/memory-tree/check-method-carriers.sh`. This feature
  avoids both by not spelling that literal in its template at all.

## Gaps

- **Deriving the parity carriers from the descriptor is not done.** Four hand-kept carriers per
  rendered guide is the standing cost, and a miss prints green. Filed as a backlog row rather than
  built here, because deriving kit parity sits outside the goal of the build that produced this
  feature.
- **Nothing grades the convention, deliberately.** A style rule a machine could grade would be a
  rule, and every rule this design pass considered was refused on measurement. The compensating
  check is that the guide is short, rendered into adopters with the kit, and reachable from the
  document a session already loads.
- **The `gov:` marker vocabulary is still unclosed** — ten kinds in use with their own consumers and
  nothing grading the vocabulary, so a misspelled marker is silence from every reader. Adjacent
  rather than blocking: this feature adds no kind.

## Reuse affordance

seam: the `render_doc` line in `tools/memory-tree/adopt-memory-tree.sh` — add a rendered guide by
adding one conditional line, one descriptor stanza, one pair row and two guard rows.
seam: the one-line test — delete the id and read what is left — as the review question for any
comment that cites a record.
