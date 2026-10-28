# TOOL-dIndexedDesign-12 — the structured spec's typed edges: `implements=` and `decides=` read through one spec-site adapter, and `design.seams` reading a tag's bundle

**Status:** OPEN · rev-2 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 2 · advances TOOL-dIndexedDesign-17

**Carries:** cl-dClosedLoop-0394@97e00df6 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-fix-return.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-fix-return.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-c.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-c.md) | research | TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-1 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-1-fix-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-fix-brief.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |
| [2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md) | spec-audit | TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-3 |

<!-- /gen:spec-records -->

## 1. Goal

A spec says what it implements and what it decides only in prose: the one typed spec binding at base is
`**Carries:**` (`tools/memory-tree/design_lib.py:115`), so a feature cannot list its units and a
decision cannot name the spec that made it (v2 P12, :900-902; night pass point 4, `[edges]`). This unit
gives a spec `**Edges:** implements=<target>` and `**Edges:** decides=<target>` lines in
PLAY-dOrderedCharter-24's grammar, read through one adapter in the memory-tree kit that calls that
build's parser and adds no grammar, and gives `design.seams` its read of a tag's bundle through
`gov_tag.py bundle`.

## 2. Scope (IN)

Build-run preconditions, each specced and DEFERRED at base, each landed before this build run because
dOrderedCharter is an ancestor through dDeclaredLoop (`memory/builds/dDeclaredLoop/README.md` front
matter, `parents: dOrderedCharter dFairHearing`): `tools/playbook/edge_grammar.py`'s
`parse_edge_lines(text, path)` and `parse_edge_target` (PLAY-dOrderedCharter-24 S2, S3), the
`implements` and `decides` rows of `tools/playbook/edges.toml` (-24 S1, -28 S1), and
`python tools/playbook/gov_tag.py bundle <address>` (-25 S1, S2). From this build:
`read_spec_headings` and `read_spec_section` (`TOOL-dIndexedDesign-9` S1, S2, order 1).

- **S1** — The adapter, shared interface I2: `read_spec_edge_lines(text, path="<spec>")` in
  `tools/memory-tree/design_lib.py`, beside `read_spec_edges` (:543). It hands the whole text to
  `edge_grammar.parse_edge_lines(text, path)`, which walks `tree_lib.unfenced_lines`, and returns one
  dict per edge target: `line`, `type`, `target`, `form` (`parse_edge_target`'s class: `tag`,
  `pinned-tag`, `section`, `id`, `id#tag` or `pinned-id`) and `section`, the tag of the spec section
  the line sits under by `read_spec_headings`, or `header` above the first section. The parser's
  refusal passes through as a `DesignRefusal` naming each `path:line`. The adapter compiles no regex
  for the line or the target. Observed by AC1 and AC3.
- **S2** — The `implements=` targets a spec may write, checked by the adapter after the parse: a unit
  id (`id`), a `feature.<seg>` tag (`tag`), or a pinned clause id `cl-d<Build>-NNNN@<hash8>`
  (`pinned-id` whose id matches `design_lib._CL`, :110, the `CARRY` clause shape, :115). A `pinned-id`
  target whose id is not a clause id, and any other form, is refused naming the `path:line`, the
  target and the three admitted forms. Observed by AC2.
- **S3** — `decides=` on a spec, targets as TOOL-dLinkedLibrary-22 spells them (its S6: any node,
  each target one `parse_edge_target` classifies), the edge's source the spec's unit id. The adapter
  admits every form the registry's `decides` row admits and checks nothing the parser does not.
  Observed by AC1.
- **S4** — The CLI, `python tools/memory-tree/design_lib.py --edges <path>...`: one line per edge
  target, `<path>:<line> · <type> · <target> · <form> · <section>`, then
  `design-lib: <n> file(s) · <m> edge(s) · <k> refused`; exit 1 when any file refused, 2 when the
  playbook kit does not resolve, naming it. Observed by AC1 and AC2.
- **S5** — `design.seams` reading a tag's bundle, the hand-off `bundle`:
  `derive_tag_bundles(tags, root)` in `design_lib.py` runs
  `<sys.executable> <playbook kit>/gov_tag.py bundle <tag>` per tag, in manifest mode, with `root` as
  its working directory, the kit found by the inline `resolve_kit_dir` copy, and returns
  `{tag: [manifest line, …]}` in the order given. An exit 2 is a `DesignRefusal` naming the tag and
  `gov_tag.py`'s stderr line. The fold and the row budget are `gov_tag.py`'s own (`tags.bundle-rows`,
  -25 S2); this function reads no policy key. CLI: `design_lib.py --bundle <tag>...`. Observed by AC4.
- **S6** — The kit edge: memory-tree's reach into the playbook kit is declared once, in the
  `requires_if` row for `playbook` that TOOL-dTotalRecall-43 S10 adds to `tools/memory-tree/kit.toml`,
  whose `why` gains `design_lib.py` and its two calls; where the kit does not resolve, both functions
  refuse naming it, and `read_spec_edges` and every other `design_lib` reader stay importable.
  Observed by AC5.
- **S7** — The format document: `tools/memory-tree/SPEC-TEMPLATE.template.md` gains a section
  `**Edges:** — a spec's typed edges`, stating the placement (column 0, under the binding lines, one
  line per type), the types a spec writes, S2's three `implements=` forms, that `**Carries:**` stays the
  clause binding a chain spec writes and `implements=<clause>@<hash8>` joins as a whole carrier
  (§8 F1), that §3's `### Edges` bullets stay the hand-off grammar, and `edge_grammar.py` as the one
  parser; `memory/TEMPLATE-SPEC.md` is its render. Observed by AC6.

## 3. Non-goals (OUT)

- The coverage join reading `implements=` with a clause target: `TOOL-dIndexedDesign-16`'s.
- Feature membership, the feature design record and the interface diff: `TOOL-dIndexedDesign-8`'s.
- `item.design.seams`, `record-kind.seams` and the scout's use of the bundle:
  `TOOL-dIndexedDesign-13`'s. This unit owns no node.
- The edge registry, the closed set, the inverses and the site-wide type check
  (PLAY-dOrderedCharter-24 S1, S4, S5; -25 S5): read, never re-specced. Its spec-site gap is an ask
  (§8 F3).
- §3's `consumes-from` and `hands-off` bullets and check 12's verb list: unchanged.
- A spec-tokens arm grading every spec's edge lines: the site-wide grade is dOrderedCharter's
  type-registered check (§8 F3).

### Edges

- **consumes-from** `TOOL-dIndexedDesign-9` — `read_spec_section`, with `read_spec_headings`, which name the section each edge line sits under; without it a tagged section reads as `header`
- **hands-off** `TOOL-dIndexedDesign-16` — `read_spec_edge_lines`, whose `implements=` pinned clause targets the coverage join counts as whole carriers
- **hands-off** `TOOL-dIndexedDesign-8` — `read_spec_edge_lines`, the one reader of `implements=feature.<seg>`, the feature membership it joins on
- **hands-off** `TOOL-dIndexedDesign-13` — `bundle`, `derive_tag_bundles`, the bundle `design.seams` reads for a tag the request names
- **consumes-from** external — dOrderedCharter's `edge_grammar.py`, `edges.toml` and `gov_tag.py bundle` (PLAY-dOrderedCharter-24 S1-S3, -25 S1-S2, -28 S1), DEFERRED at base, built before this build run; dTotalRecall's `requires_if` row (TOOL-dTotalRecall-43 S10)
- **hands-off** `TOOL-dIndexedDesign-38` — the round-1 spec audit's minors that land on this spec, report ids 11 and 43, each a scope item of that batch unit

## 4. Design

### A spec header with edges

```markdown
# TOOL-dFix-3 — the fixture unit

**Status:** OPEN · rev-1 · 2026-11-02 · node d · Tier-2 · base 57bc3b91 · streams tooling

**Carries:** cl-dFix-0001@1a2b3c4d whole
**Edges:** implements=feature.record-door,cl-dFix-0002@9f8e7d6c
**Edges:** decides=policy-key.design.overlap
```

`design_lib.py --edges` prints, for that file:

```
x.md:6 · implements · feature.record-door · tag · header
x.md:6 · implements · cl-dFix-0002@9f8e7d6c · pinned-id · header
x.md:7 · decides · policy-key.design.overlap · tag · header
design-lib: 1 file(s) · 3 edge(s) · 0 refused
```

An edge line under `## [section.design] Design`, the section edge line TOOL-dTotalRecall-19 §4 writes
for a record, reads with `section.design`, so a reader can tell a unit-level edge from a section-level
one without a second grammar.

### What the adapter checks, and what it leaves

| Check | Owner |
|---|---|
| the line grammar, a target's address form, a malformed line | `edge_grammar.parse_edge_lines` |
| an unregistered type, a type's `to`, a pin on a type that takes none | `edges.toml` through -24 S4, at every site the index reads |
| `implements=` takes a unit id, a feature tag or a pinned clause id | this adapter, S2 |
| the section an edge sits under | this adapter, through `read_spec_headings` |

### The clause binding, beside `implements=`

`**Carries:** <cl>@<h> whole` and `**Edges:** implements=<cl>@<h>` state one fact. A spec may write
either; the coverage join reads each spec's clause carriers once whichever line names them, so one
clause named by both lines at one hash is one carrier, and at two hashes is two pins, which the join's
existing `ambiguous` arm reds (`tools/check-spec-tokens.py:1013-1018`). Parts stay `**Carries:**`'s
alone: an edge has no `part k/n` form. This build's own specs keep `**Carries:**`, because the
in-service instrument `carries.py` reads only that line.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_spec_edge_lines` | Python function, `design_lib.py` | `py.function` |
| `derive_tag_bundles` | Python function, `design_lib.py` | `py.function` |
| `--edges`, `--bundle` | flags of `design_lib.py` | none |

### Migration

None: no landed spec carries a `**Edges:**` line outside a fence but TOOL-dTotalRecall-19 (:188-189,
inside a fenced example), and the adapter only reads.

### Rollout

One pass after its preconditions land: the adapter and its CLI, the bundle read, the kit row, then the
format document.

### Files touched (estimate)

- `tools/memory-tree/design_lib.py`: S1-S5
- `tools/memory-tree/kit.toml`: S6
- `tools/check-spec-tokens.test.sh`: the arm of §7
- `tools/memory-tree/SPEC-TEMPLATE.template.md`, and `memory/TEMPLATE-SPEC.md` its render: S7
- `tools/memory-tree/check-memory-hygiene.sh`: `KIT_MEMORY_TREE_VERSION`

### Alternatives rejected

- **`implements` as a §3 `### Edges` bullet verb.** Lost to the closed set: a bullet verb is check 12's
  two-verb grammar (`check-memory-hygiene.sh:2559-2600`), which no registry row types, so a feature's
  units would be read by a second grammar the tag index never sees.
- **A regex for `**Edges:**` in `design_lib`.** Lost to -24 S3, which makes `parse_edge_lines` the one
  parser; AC3's stub observes that the adapter parses nothing itself.
- **Reading only the header block.** Lost to TOOL-dTotalRecall-19 §4, whose section edge line sits under
  a heading: refusing it in a spec would make one grammar legal in a record and red in a spec.

## 5. Production-readiness checklist

- security — no write path; one subprocess per bundled tag, its argv a list with the tag as one
  argument, never a shell string.
- perf / scale — one parse per spec read; `derive_tag_bundles` runs once per tag the caller names, and
  `gov_tag.py`'s own fold bounds each manifest.
- error / empty / loading states — a spec with no edge line returns `[]`; every refusal names the
  `path:line` or the tag; an absent playbook kit refuses by name and leaves the other readers loaded.
- observability — `--edges` and `--bundle` print what a reader sees.
- risks — a parent's grammar moving under the adapter; AC3 pins that the adapter holds none of it.
- testing — AC1 to AC6 by a pass, and the arm of §7 at the close.
- migration — none.
- user docs — the spec format's document is S7; no page under `help/` covers the spec format.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/design_lib.py --edges` runs over the §4 example written to
  a scratch file, with a fourth edge line under `## [section.design] Design` and a fifth inside a fenced
  block, it prints the three header edges with forms `tag`, `pinned-id` and `tag`, the fourth with
  section `section.design`, nothing for the fifth, and `4 edge(s) · 0 refused`, exit 0.
  Red when: a fenced line is read, a section edge reads as `header`, or a target's form is wrong.
- **AC2** — When `design_lib.py --edges` runs over scratch specs holding
  `**Edges:** implements=TOOL-dFix-2@1a2b3c4d`, `**Edges:** implements=section.goal` and a malformed
  `**Edges:** implements`, it exits 1 naming each `path:line`, the first two with the three admitted
  `implements=` forms and the third with the parser's grammar.
  Red when: a pinned unit id, a section target or a malformed line is admitted.
- **AC3** — When `read_spec_edge_lines` runs with `edge_grammar.parse_edge_lines` replaced by a stub
  returning no edge, over the AC1 file, it returns `[]`; with the stub raising, the refusal passes
  through with its text.
  Red when: the adapter finds an edge the parser did not return, which means it parses lines itself.
- **AC4** — When `python tools/memory-tree/design_lib.py --bundle <tag>` runs at the pass tip for a
  tag the tag index holds, its lines equal `gov_tag.py bundle <tag>`'s
  manifest; for `feature.nope-not-a-tag` it exits 1 naming the tag and the bundle verb's refusal.
  Red when: the manifest is re-derived or cut, or a refused tag is passed over silently.
- **AC5** — When `read_spec_edge_lines` and `derive_tag_bundles` run in a scratch install prefix that
  holds the memory-tree kit and no playbook kit, each refuses naming the playbook kit, and
  `python -c "import design_lib; design_lib.read_spec_edges"` still imports; `python -c` over
  `tools/memory-tree/kit.toml` with `tomllib` prints the `playbook` `requires_if` row naming
  `design_lib.py`.
  Red when: the absent kit is an `ImportError` at module load, or the edge is undeclared.
- **AC6** — When `grep -n "implements=" tools/memory-tree/SPEC-TEMPLATE.template.md
  memory/TEMPLATE-SPEC.md` runs, both carry the `**Edges:**` section with the three forms and the
  `**Carries:**` rule, and the render matches its template.
  Red when: the format document omits the line or its forms, or the render drifts.

## 7. Gates

`spec-tokens self-test` · `spec tokens (a spec's own names resolve)` · `memory hygiene` · `memory-hygiene self-test` · `build-index selftest` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `policy fixtures`

New arm: tools/check-spec-tokens.test.sh · covers AC1 AC2 AC3 AC5 · a scratch spec with header, section, fenced and malformed edge lines and the parser stubbed, staged by the adapter admitting a pinned unit id or reading a fenced line · none

## 8. Open questions

- **F1 — Does `**Carries:**` stay the clause binding beside `implements=`, and how does the coverage
  join avoid counting one clause twice?** Options: (a) `**Carries:**` stays the only clause binding and
  `implements=` takes unit and feature targets only; (b) both are legal, the join reads each spec's
  clause carriers once whichever line names them, parts staying `**Carries:**`'s; (c) `implements=`
  replaces `**Carries:**` everywhere. (a) fails clause 16's "`implements=` edges taking a clause target"
  (Items 16), a sibling clause of this build; (c) strands `carries.py`, the instrument in service at
  this build's Design exit (the packet's Gates), and PLAY-dOrderedCharter-28 S4's `carries-clause`
  edge, which reads `**Carries:**`. (b) satisfies both clauses and moves no landed spec. Rung 3, the
  most feature-rich survivor. RESOLVED (agent, 2026-10-28, delegated): (b). widens: none · relaxes:
  none
- **F2 — The format document is a governance carrier (BUILD-METHOD M11).** Options: (a) S7 under the
  README's grant, the clause naming the structured spec's edges; (b) the grammar in `design_lib.py`'s
  docstring only, the defect ask PLAY-dClosedLoop-22 files for the binding lines. Rung 3 with veto 2
  lifted by the grant. RESOLVED (agent, 2026-10-28, delegated): (a). grants: PLAY-dClosedLoop-3 the
  spec template's `**Edges:**` section and its render. widens: none · relaxes: none
- **F3 — dOrderedCharter's registry, as specced, refuses the clause target, and its site table does not
  name a spec header.** PLAY-dOrderedCharter-28 S3 makes a pinned clause id legal only as a
  `carries-clause` target, and -24 §4 gives `implements` the `to` of `feature` or a spec id; -28 S5's
  sites name a record's header bindings and its section lines. Those specs are another build's and are
  never edited here. Options: (a) one ask in dOrderedCharter's `BACKLOG.md`; (b) a stand-in admitting
  the target in this adapter alone. (b) is a second rule for one edge, which the tag index would then
  red at the site-wide check. Rung 3. RESOLVED (agent, 2026-10-28, delegated): (a). The ask, filed by
  the main loop: target dOrderedCharter, "`implements` admits a pinned clause id, its row's `to`
  naming the `clause-id` native class and its pin `clause`, and the spec header, the lines under a
  spec's H1 above its first section, is a site read through `design_lib.read_spec_edge_lines`" ·
  accept "`edge_grammar.py --parse` over a spec whose header holds
  `**Edges:** implements=cl-dFix-0001@1a2b3c4d` and `**Edges:** decides=feature.x` exits 0, the same
  pin on `tests=` exits 1, and `gov_tag.py bundle feature.x` lists the spec's `decides` edge".
  widens: none · relaxes: none
- **F4 — Where does `design.seams` read a bundle?** Options: (a) `derive_tag_bundles` in `design_lib`,
  handed to `TOOL-dIndexedDesign-13` as `bundle`; (b) the scout's harness calls `gov_tag.py bundle`
  itself. The clause gives the reading to this unit, and (a) gives it an observable criterion (AC4);
  under (b) this clause's `design.seams` half has no code here. Rung 3. RESOLVED (agent, 2026-10-28,
  delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, from the packet's Items 12, the brief's I2 and unit 12 row, scout C
  row 12 and interface 4, PLAY-dOrderedCharter-24, -25 and -28, and TOOL-dLinkedLibrary-22, each
  source re-read at base `57bc3b91`.
- rev-2 · 2026-10-28 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from edge of TOOL-dIndexedDesign-38,
  promoted by the round-1 spec audit of this build; nothing else moved.

## 10. Reuse audit

The seams extended are `design_lib.py`'s spec readers (`read_spec_edges`, `tools/memory-tree/design_lib.py:543`;
`parse_binding_lines`, :348, whose collect-every-malformed-line discipline -24 S3 copies) and, through
them, PLAY-dOrderedCharter-24 S3's `parse_edge_lines` and -25 S1's `gov_tag.py bundle`, each called and
never re-implemented. `python tools/codebase-map/reuse_lookup.py "parse typed edge lines declared in a
spec header"` ranked `parse`, `parse_conf`, `unfenced_lines` (a SEAM, which the parser walks),
`read_spec_edges` and `read_spec_writes`; none parses a typed `**Edges:**` line, because the parser is
specced and unbuilt at base (`tools/playbook/edge_grammar.py` is absent), so no existing seam fits the
line grammar here and the adapter is new beside its siblings. Where records and source disagree: the
brief's I2 places edges "under the binding lines", while TOOL-dTotalRecall-19 §4 places a record's
edge line under a section heading; the adapter reads both and names the section (§4). The scout's note
that dOrderedCharter is outside `parents:` holds, and it is an ancestor through dDeclaredLoop, so its
units are preconditions rather than stand-ins. The recall query returned scout C's row 12, the
relational-syntax research row ("the structured spec declares `implements=` and `decides=`;
`design.seams` reads the bundle") and TOOL-dLinkedLibrary-17 AC3's `decides=feature.alpha` plant.

Recall terms used: `python tools/memory-recall/query.py "how does a spec declare that it implements a feature or a clause and which decision it makes" --terms "Edges implements decides edge_grammar parse_edge_lines Carries carries-clause feature bundle gov_tag"`
