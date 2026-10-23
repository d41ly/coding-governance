# PLAY-dOrderedCharter-24 — the edge-type registry and the edge grammar: one closed set of typed edges, inverses derived, selectors open

**Status:** OPEN · rev-2 · 2026-10-24 · node d · Tier-2 · base ce13efbe · streams playbook · order 7 · advances PLAY-dOrderedCharter-38

**Carries:** cl-dClosedLoop-0054@1e793db7 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-b.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-b.md) | research | PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-28 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md](../reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md) | spec-audit | PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-37 |

<!-- /gen:spec-records -->

## 1. Goal

Two relation vocabularies exist and no closed edge set: the map's layer, owner, after and implements,
and memory's depends-on, patches, amends, supersedes and implements, with no tests, decides or
instructs edge (`gap-found-25`), so the cycle the owner asked for cannot be walked by key
(`gap-mem-35`). This unit lands the edge-type registry, one row per type of one closed set, each edge
declared once at the site that owns its fact and its inverse derived, never declared; the `edge`
grammar `type=target[,target]` and its one parser; the instruction selectors open to a namespace a
later build registers; and the pin hash factored into one shared function (night pass, point 4; P33).

## 2. Scope (IN)

- **S1** — The registry, `tools/playbook/edges.toml` (shared interface S6): one `[[edge]]` row per
  type with `type`, `inverse`, `from`, `to`, `pin` (`none`, `tag` or `clause`), `status` (`declared`
  or `derived`) and `declared-at`. This unit writes P33's twelve declared types and the derived
  `cites`, from memory-plan `[edges]`; PLAY-dOrderedCharter-28 adds the twelve new types and widens
  `decides` and `after`. Observed by AC1.
- **S2** — The grammar. At a markdown site an edge is one line at column 0, `**Edges:**
  type=target[,target]`, one line per type, so a block of two types is two lines. In a TOML row it is
  one string per type in the row's `edges` list, the same `type=target[,target]`. A target holds no
  space, comma or bracket; a section target is written `<doc>#<seg>`; a pinned target is
  `<address>@<hash8>`. Observed by AC2 and AC3.
- **S3** — The parser, `tools/playbook/edge_grammar.py`: `parse_edge_lines(text, path)` walks
  `tree_lib.unfenced_lines`, so a fenced line is never an edge, returns one record per edge with its
  line, type and targets, and collects every malformed line into one refusal naming each `path:line`,
  the line and the grammar, the discipline of `design_lib.parse_binding_lines`
  (`tools/memory-tree/design_lib.py:348`). `parse_edge_target` classifies a target by address form:
  `tag`, `pinned-tag`, `section`, `id`, `id#tag`, `pinned-id`. Observed by AC2 and AC3.
- **S4** — The closed set. An edge whose type no row holds is red; a declared edge whose type is an
  `inverse` of a row is red, since an inverse is derived; a declared `cites` is red, since `cites` is
  derived from text; a target whose namespace is outside its row's `to`, or a pin on a type whose row
  says `pin = "none"`, is red. Observed by AC4 and AC5.
- **S5** — Inverses derived: `derive_inverse_edges(edges)` returns, for every declared edge, the
  `(target, inverse, source)` triple its row names, and nothing is ever read from a site for an
  inverse. Observed by AC4.
- **S6** — The selectors open: a row's `to` may name the class `selects`, meaning every namespace
  whose registry row has `role = "selects"` (shared interface S4); `instructs` names it, so a
  namespace a later build registers as a selector, `feature` by dTotalRecall, is a legal `instructs`
  target with no change to `edges.toml`. Observed by AC6.
- **S7** — The pin hash (shared interface S7): `derive_clause_hash`'s normaliser factored into
  `derive_pin_hash(text)` in `tools/memory-tree/design_lib.py`, the first eight hex digits of the
  SHA-256 of the UTF-8 text with each whitespace run folded to one space and the ends stripped;
  `derive_clause_hash(text)` becomes `derive_pin_hash` of the text with its trailing `cl-` id cut,
  its values unchanged. Every later pin calls `derive_pin_hash`. Observed by AC7.
- **S8** — The parser's own CLI: `edge_grammar.py --list` prints every type with its inverse, `from`,
  `to` and `pin`; `--parse <file>` prints each edge or the refusal; `--fixture --plant <case>` runs the
  plants of §4. Observed by AC1 to AC6.

## 3. Non-goals (OUT)

- The twelve new types, the widened `decides` and `after`, the native-id classes and the edges
  applied at every memory-plan site, with their resolution and the pin reds: PLAY-dOrderedCharter-28's.
- Resolving a target to a node: PLAY-dOrderedCharter-19's resolver, which PLAY-dOrderedCharter-28 calls.
- `gov tag bundle`'s type-registered and target-resolves checks: PLAY-dOrderedCharter-25's.
- A leg: the edge checks join the `tags` leg pack with PLAY-dOrderedCharter-28.
- Migrating today's prose relations into edges: the sites' own builds.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-19` — `read_namespaces` and each row's `role`, which S6 reads; and `TAG_RE`, which classifies a tag target
- **hands-off** `PLAY-dOrderedCharter-28` — the twelve new edge types, `carries-clause` among them, and the parser applied at every site with `derive_pin_hash` for the pinned forms
- **hands-off** `PLAY-dOrderedCharter-9` — the edge parser a unit row's `edges` field is read through
- **hands-off** `PLAY-dOrderedCharter-12` — S7's shared normaliser, the hash of each units entry
- **hands-off** `PLAY-dOrderedCharter-20` — S7's shared normaliser, the one-fact key's hash
- **hands-off** `PLAY-dOrderedCharter-25` — `tools/playbook/edges.toml`, its parser and the registry order bundles group by
- **hands-off** `PLAY-dOrderedCharter-32` — `derive_pin_hash` and the edge grammar the overlay's `amends` and `supersedes` targets are written in
- **hands-off** `PLAY-dOrderedCharter-33` — `derive_pin_hash`, the normaliser the pins share
- **hands-off** `PLAY-dOrderedCharter-35` — the edge grammar and S7's shared pin normaliser
- **hands-off** `PLAY-dOrderedCharter-15` — S7's shared normaliser for a change record's before and after texts
- **hands-off** `PLAY-dOrderedCharter-49` — the round-1 spec audit's minors on this spec, findings 51 and 52, which that batch unit corrects after this unit lands, each by the item its report id names

## 4. Design

### Data model

```toml
# tools/playbook/edges.toml
[[edge]]
type = "instructs"
inverse = "instructed-by"
from = ["unit"]
to = ["selects"]
pin = "none"
status = "declared"
declared-at = "the unit's select"

[[edge]]
type = "amends"
inverse = "amended-by"
from = ["any"]
to = ["any"]
pin = "tag"
status = "declared"
declared-at = "the amending node"

[[edge]]
type = "cites"
inverse = "cited-by"
from = ["any"]
to = ["any"]
pin = "none"
status = "derived"
declared-at = "derived from the text"
```

The twelve declared rows and their `from` and `to`, from memory-plan `[edges]`: `part-of` (any to
any tag), `implements` (any to `feature` or a spec id), `tests` (any to any), `decides` (a decision
id to any), `instructs` (`unit` to `selects`), `enforces` (any to `unit` or `practice`), `after` (a
build to a build), `supersedes` and `amends` (any to any, `pin = "tag"`), `patches` (a build to a
build or `item`), `owner` (any to a build or `layer`), `layer` (`kit` to `layer`). `any` admits every
registered namespace and every native-id class; a namespace word not yet registered, `feature` or
`item`, may stand in `to` and admits nothing until its build registers it.

### Address forms

| Form | Shape |
|---|---|
| `tag` | `TAG_RE` |
| `pinned-tag` | `<tag>@[0-9a-f]{8}` |
| `section` | `<tag>#<seg>` |
| `id` | a native id, its classes registered by PLAY-dOrderedCharter-28 |
| `id#tag` | `<id>#<tag>`, a record's section |
| `pinned-id` | `<id>@[0-9a-f]{8}` |

A target matching no form is a malformed line.

### The plants

`good-block` (a two-line block, exit 0), `space-target`, `comma-in-pair`, `bracket-target`,
`two-types-one-line`, `no-equals`, `unregistered-type`, `declared-inverse`, `declared-cites`,
`outside-to`, `pin-on-none`, `selector-registered`, `selector-describes`, `fenced-edge` (exit 0, not
read).

### Inventory

Minted: `tools/playbook/edges.toml` with keys `type`, `inverse`, `from`, `to`, `pin`, `status`,
`declared-at` and the class words `any` and `selects`; `tools/playbook/edge_grammar.py` with
`read_edge_types`, `parse_edge_lines`, `parse_edge_target`, `derive_inverse_edges`, `check_edges`,
`build_edges_fixture`; `derive_pin_hash` in `tools/memory-tree/design_lib.py`; the flags `--list`,
`--parse`, `--fixture`, `--plant`; the prefix `edges:`. Naming cells: checked with
`python tools/lexicon/lexicon.py --suggest <name> --as py.function` at the pass.

### Migration

Additive; no site declares an edge yet, and `derive_clause_hash`'s values do not move.

### Files touched (estimate)

- `tools/playbook/edges.toml` (new)
- `tools/playbook/edge_grammar.py` (new)
- `tools/memory-tree/design_lib.py`
- `tools/playbook/README.md`

### Alternatives rejected

- **Front matter or a sidecar list for edges**: each lost a measured test (memory-plan `[sites]`:
  7.3% fit, 43 of 45 stranded, 12 of 31 drifted).
- **Inverses declared at both ends**: two facts for one relation.
- **`instructs` with a closed target list**: every later selector would edit the registry, and the
  night pass opened the selectors to a later build's namespace.

## 5. Production-readiness checklist

- security: a parser and a data file; no write path.
- perf / scale: a line scan per file, linear.
- error / empty / loading states: every malformed line is named in one refusal; an unreadable registry exits 2.
- observability: `--list` prints the whole closed set.
- risks: a site's prose that happens to open `**Edges:**`; the parser reads it as an edge line and reds it if malformed, which is the intended pressure.
- testing: AC1 to AC7 and §7's arm.
- migration: §4 "### Migration".
- user docs: `help/tags.md` gains the edge grammar and the closed set's table, rendered from `--list`.

## 6. Acceptance criteria

- **AC1** — When `python edge_grammar.py --list` runs, it prints thirteen types, the
  twelve declared and `cites`, each with its inverse, and `cites` marked derived.
  Red when: a type lacks an inverse, or `cites` is declarable.
  figure: thirteen is PINNED for this unit; PLAY-dOrderedCharter-28 raises it.
- **AC2** — When `python edge_grammar.py --fixture --plant good-block` runs, a heading
  followed by `**Edges:** implements=feature.x` and `**Edges:** tests=kit.y,kit.z` parses to two
  edges, the second with two targets, and exits 0; `--plant fenced-edge` exits 0 with no edge read.
  Red when: a two-type block reads as one edge, or a fenced line is read.
- **AC3** — When `--plant space-target`, `--plant bracket-target`, `--plant comma-in-pair`,
  `--plant two-types-one-line` and `--plant no-equals` run, each exits 1 and one refusal names every
  bad `path:line` with the grammar.
  Red when: a malformed edge line is passed over, or only the first is named.
- **AC4** — When `--plant unregistered-type`, `--plant declared-inverse` and `--plant declared-cites`
  run, each exits 1 naming the type; and `derive_inverse_edges` over the good block returns
  `implemented-by` and `tested-by` triples.
  Red when: an unregistered or inverse type is declarable, or an inverse is read from a site.
- **AC5** — When `--plant outside-to` (`layer=kit.x`) and `--plant pin-on-none`
  (`part-of=kit.x@1a2b3c4d`) run, each exits 1 naming the row's `to` or `pin`.
  Red when: a target outside its row's namespaces, or a pin on a type that admits none, passes.
- **AC6** — When `--plant selector-registered` runs, a fixture registry adding `feature` with
  `role = "selects"`, `instructs=feature.x` exits 0 with `edges.toml` unchanged; under
  `--plant selector-describes`, the same row with `role = "describes"`, it exits 1.
  Red when: a later selector needs an edit to the edge registry, or a descriptor is selectable.
- **AC7** — When `python -c "import sys; sys.path.insert(0,'tools/memory-tree'); import design_lib as d, pathlib; rows=d.read_design_view(d.read_design_conf('.')['DESIGN_VIEW']); print(all(d.derive_clause_hash(t)==h for _,_,t,h,_ in rows))"`
  runs, it prints `True`; and `git grep -n "hashlib.sha256" -- tools/memory-tree/design_lib.py`
  prints one line, inside `derive_pin_hash`.
  Red when: the factoring moves a clause hash, or a second normaliser remains.
  fixture: the read uses the view's text cells, which hold each clause's text as hashed.

## 7. Gates

`memory hygiene` · `playbook render selftest` · `govkit acceptance matrix` · `verdict epoch (kit version dates the engine)` · `lexicon naming predicates`

New arm: tools/playbook/adopt-playbook.sh · covers AC2 AC3 AC4 AC5 AC6 · the playbook-render selftest runs every plant of §4 · none

## 8. Open questions

- **F1 — One `**Edges:**` line per type, or pairs joined by ` · ` on one line.** The brief's shared
  interface S6 spells pairs separated by ` · `; memory-plan `[sites]` and clause
  `cl-dClosedLoop-0058` say "one `**Edges:**` line per type", and that clause's planted "two-type
  block" is two lines. RESOLVED (agent, 2026-10-23, delegated): one line per type, rung 1, v2 answers
  it; a line carrying a second `type=` pair is malformed (`two-types-one-line`). The TOML `edges`
  field holds one string per type for the same reason. widens: none · relaxes: none
- **F2 — Where `derive_pin_hash` lives.** Options: `design_lib.py`, beside `derive_clause_hash`;
  the edge parser. The clause hash's callers (`asbuilt_view.py:131`, `check-spec-tokens.test.sh:1609`)
  already import `design_lib`. RESOLVED (agent, 2026-10-23, delegated): `design_lib.py`, rung 3, one
  normaliser beside its first caller, the edge parser importing it core to core. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-1 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-49.

## 10. Reuse audit

No existing seam fits the registry or the grammar: `**Edges:**`, `carries-clause` and `promoted-from`
have no hit in code (`git grep -n "Edges:\*\*" -- tools` prints nothing), and the only typed relations
parsed today are the as-built view's `amends` and `supersedes` follow rows
(`tools/memory-tree/asbuilt_view.py:143`, `ROW_FOLLOW`). The parse discipline reused is
`design_lib.parse_binding_lines` (`tools/memory-tree/design_lib.py:348`) over `tree_lib.unfenced_lines`
(`tools/memory-tree/tree_lib.py:149`), and the hash is `derive_clause_hash`
(`tools/memory-tree/design_lib.py:169`), factored. `reuse_lookup.py "parse a typed relation line and
check its type against a closed registry"` ranked `parse` (`tools/memory-recall/query.py`), `check`,
`parse_args`, `kit_rel`, `parse_conf`, `checks`, `check_line` and `parse_spec_h1`, and not
`parse_binding_lines`, which the scout's reading named and source confirms as the closer discipline:
the lookup ranks by name tokens and misses it.

Recall terms used: `python tools/memory-recall/query.py "what is the closed set of typed edges and how is an edge line written" --terms "edge type registry closed set inverse derived Edges line target grammar instructs selector P33 cites"`
