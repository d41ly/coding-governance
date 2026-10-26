# TOOL-dTotalRecall-37 — only the four rendered workflow scripts are `linguist-generated`, held equal to the kits' render rows both ways

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 4 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 |
| [2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md) | research | TOOL-dTotalRecall-36 TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md) | research | TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-36 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-38 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-36 TOOL-dTotalRecall-39 TOOL-dTotalRecall-43 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md`)
confirmed finding **id 16 at HIGH**, its item **H2**, alone in that item. `TOOL-dTotalRecall-8` §4
"Bounds" registers gov's generated code as `tools/workflows/*.js` in `.gitattributes`, and its Bounds
table excludes every `linguist-generated` path from the code record. That glob matches all eleven
tracked `.js` files of the workflows kit (`git ls-files 'tools/workflows/*.js'` at base `462d20f3`).
Four are the `.template.js` sources and three are hand-written: `check-workflow-syntax.js`,
`orient-counterfactual.js` and `unattended-unit.js`. Only four are renders, each declared by a
`role = "rendered"` row of `tools/workflows/kit.toml` (`:62-64`, `:76-78`, `:82-84`, `:88-90`). The code
record would hold no definition, call or edge of the workflow sources, and every reader of it would
answer wrongly about them. This unit names the four renders alone and adds a parity arm that holds the
attribute set equal to the kits' render outputs, both ways. It repairs `TOOL-dTotalRecall-8`.

## 2. Scope (IN)

- **S1** — `.gitattributes` names `linguist-generated` on the four rendered paths, one line each:
  `tools/workflows/tier2-review.js`, `tools/workflows/unattended-build.js`,
  `tools/workflows/drift-audit-code.js` and `tools/workflows/drift-audit-state.js`, in place of the
  `tools/workflows/*.js` registration `TOOL-dTotalRecall-8` wrote. The existing
  `tools/workflows/*.js text eol=lf` pin is a different attribute and stays as it is. Observed by AC1
  and AC2.
- **S2** — The parity arm, `check_generated_attributes(root, descs, r)` in `tools/govkit/govkit.py`, run
  by `selfcheck` (`:1832`) over the descriptors `read_descriptors` (`:13238`) parses. The render set is
  every `[[files]]` row with `role = "rendered"` whose `to`, with `{kit}` resolved to the entry's home
  under the tool root, names a code file of the code record's languages. The attribute set is every
  tracked file under the tool root that `git check-attr --stdin linguist-generated` reports `set`, read
  in one spawn. Each path in one set and not the other is a finding naming its side:
  `rendered but not linguist-generated` or `linguist-generated but rendered by no kit`. Observed by AC3.
- **S3** — The code record holds the workflow sources. At the pass tip, `code_record.py` derives rows
  for the four `.template.js` files and the three hand-written scripts and none for the four renders.
  Observed by AC4.

## 3. Non-goals (OUT)

- The code record, its Bounds table and its attribute read: `TOOL-dTotalRecall-8`'s. This unit changes
  which paths carry the attribute, not how the record reads it.
- Generated files outside the tool root. An adopter marks its own generated code as it likes, and the
  arm grades only paths under the tool root, where the kits' render rows live.
- Rendered Markdown and Skill files. They are not code the record reads, so the arm's render set
  holds code files only.

### Edges

- **consumes-from** `TOOL-dTotalRecall-8` — the Bounds row reading `linguist-generated` and the
  `.gitattributes` registration this unit narrows to the four renders
- **hands-off** `TOOL-dTotalRecall-53` — `check_generated_attributes` and the four renders' attribute, which that unit gives an `eol` row and carries to adopters (the round-1 audit of units 36 to 43, ids 24 and 25)

## 4. Design

### The registration

```gitattributes
tools/workflows/tier2-review.js linguist-generated
tools/workflows/unattended-build.js linguist-generated
tools/workflows/drift-audit-code.js linguist-generated
tools/workflows/drift-audit-state.js linguist-generated
```

Explicit paths rather than a glob, because the render set is four named outputs and a glob over a
kit's directory is the defect. The parity arm is what keeps the list from drifting when a fifth render
lands: its row in `kit.toml` makes the arm red until the line is added.

### The arm's two sets, at base

| Set | Members at base `462d20f3` |
|---|---|
| render outputs that are code | the four `.js` renders above (`tools/workflows/kit.toml` rows) |
| `linguist-generated` under the tool root | none (`grep -c linguist .gitattributes` printed `0`) |

At the pass base `TOOL-dTotalRecall-8` has written its glob, so the arm reads the eleven paths and
names the seven that are not renders, which is the arm's red case on the real tree.

### Inventory

Minted: `check_generated_attributes` in `tools/govkit/govkit.py`. Naming cell: asked of
`python tools/lexicon/lexicon.py --suggest check_generated_attributes --as py.function` at the pass.

### Files touched (estimate)

- `.gitattributes`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **Derive the attribute lines from the render rows with a generator.** A third generated artifact for
  four lines; the parity arm gives the same guarantee and leaves `.gitattributes` authored.
- **Exclude rendered files by reading the render rows inside `code_record.py`.** The memory-tree kit
  ships to adopters that carry no kit descriptors, and the record's Bounds rule is the attribute an
  adopter can set; the descriptor read belongs to the deployer, which already parses them.

## 5. Production-readiness checklist

- security — no new surface; the arm reads tracked files and one `git check-attr` output.
- perf / scale — one attribute spawn over the tool root's tracked files per selfcheck run.
- error / empty / loading states — an empty render set and an empty attribute set agree and pass,
  which is correct for a tree whose kits render no code; the arm prints both counts so a zero is seen.
- observability — each finding names the path and its side.
- risks — a render whose `to` holds a token the arm cannot resolve; the arm refuses it by name rather
  than dropping it from the set.
- testing — AC1 to AC4 by the pass; the arm of §7 at the close.
- migration — none: the attribute changes no checkout.
- user docs — none under `help/`: no page covers the code record's bounds.

## 6. Acceptance criteria

- **AC1** — When `git check-attr linguist-generated -- tools/workflows/*.template.js
  tools/workflows/check-workflow-syntax.js tools/workflows/orient-counterfactual.js
  tools/workflows/unattended-unit.js` runs at the pass tip, every line reads `unspecified`.
  Red when: a source or a hand-written script carries the attribute.
- **AC2** — When `git check-attr linguist-generated -- tools/workflows/tier2-review.js
  tools/workflows/unattended-build.js tools/workflows/drift-audit-code.js
  tools/workflows/drift-audit-state.js` runs, every line reads `set`.
  Red when: a render loses the attribute and its definitions enter the record twice.
- **AC3** — When `python tools/govkit/govkit.py selfcheck` runs in a scratch copy whose
  `.gitattributes` carries `tools/workflows/*.js linguist-generated` again, it names
  `tools/workflows/unattended-unit.js` as `linguist-generated but rendered by no kit`; with the
  `tier2-review.js` line cut instead, it names that path as `rendered but not linguist-generated`.
  Red when: the arm compares one direction only.
  fixture: a scratch copy under `%TEMP%`; the pass makes it.
- **AC4** — When a `python -c` probe with `sqlite3` reads the index `build_index` writes after
  `python code_record.py --check` at the pass tip, the `code_row` table holds a row
  named `renderShapeLine` from the blob of `tools/workflows/tier2-review.template.js`, and no row from
  the blob of `tools/workflows/tier2-review.js`.
  Red when: the template's definitions are absent, or the render's are counted beside them.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/govkit/selftest.py · covers AC3 · the plants `generated-glob` and `render-unmarked`, staged by comparing the attribute set against the render set in one direction only · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-8`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Where does the parity arm live?** Options: (a) govkit's `selfcheck`, which already parses
  every descriptor; (b) `code_record.py --check`. (b) reads kit descriptors from a kit that adopters
  install without them, so its arm would red an adopter's own generated files. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3, tie-broken by reuse of `read_descriptors`. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's id 16 (HIGH, item H2).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the hands-off mirror of TOOL-dTotalRecall-53, each a consumes-from edge of a unit the round-1 spec audit of units 36 to 43 promoted.

## 10. Reuse audit

The seams extended are govkit's descriptor reader `read_descriptors` (`tools/govkit/govkit.py:13238`)
and its `selfcheck` (`:1832`), which grade every descriptor already, and the batched attribute read of
`tools/check-wiring.sh:1141` that `TOOL-dTotalRecall-8`'s Bounds paragraph cites. No existing seam
compares an attribute set with a render set: `python tools/codebase-map/reuse_lookup.py "mark
generated code paths so an extractor skips them"` ranked name-stem neighbours (`extract`, `skip`,
`resolve_generated_indexes`), the last of which resolves the unattended kit's generated indexes and
reads no attribute.

Recall terms used: `python tools/memory-recall/query.py "how is a confirmed spec audit finding promoted to a repair unit ordered after the unit it repairs" --terms "promoted HIGH repairs order spec-audit disposal batched minors rescope add Derived PLAY-dClosedLoop-2 hands-off"`
