# PLAY-dConvergedCharter-8 — the remaining renderers absorbed, each retired with its last document, and the arm that refuses one retired early

**Status:** DEFERRED · rev-1 · 2026-11-03 · node d · Tier-2 · base 0d1c1dda · streams playbook · order 19 · advances PLAY-dConvergedCharter-24

**Carries:** cl-dClosedLoop-0482@c53ca182 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md](../build/2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-03-build-PLAY-dConvergedCharter-6-reuse-scout-b.md](../build/2026-11-03-build-PLAY-dConvergedCharter-6-reuse-scout-b.md) | research | PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-15 |
| [2026-11-03-build-PLAY-dConvergedCharter-8-deviation-81.md](../build/2026-11-03-build-PLAY-dConvergedCharter-8-deviation-81.md) | deviation | — |
| [2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md](../build/2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md) | journal | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-39 PLAY-dConvergedCharter-40 PLAY-dConvergedCharter-41 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-fix-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-fix-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-21 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md](../reviews/2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md) | spec-audit | PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-18 |

<!-- /gen:spec-records -->

## 1. Goal

dOrderedCharter's one renderer absorbs the charter's and the agent files' renderers, and leaves four
others beside its legacy list until their documents migrate (systems `:403-405`): kit/dogfood doc
parity, review-protocol parity, each kit's skill wiring `--check`, and govkit's placeholder render in
adopters. Units 7, 9 and 10 move those documents to the one renderer. This unit retires each remaining
renderer with its last document, and adds the arm that refuses retiring a renderer while a document it
renders is still on the legacy list. One renderer of record then holds every instruction file.

## 2. Scope (IN)

- **S1** — The renderer's leg on its row. A `[[target]]` row of `tools/playbook/renderers.toml`
  (PLAY-dOrderedCharter-20 S4) whose `renderer` is not a scope of the one renderer, `playbook:<scope>`,
  carries `leg = "<leg name>"`, naming the gate leg that holds its bytes: the leg that runs a renderer
  is the renderer's live presence in the bar. The key is optional and additive, as DEPL-dShippedRelease-9
  S2's `region` is. Observed by AC1.
- **S2** — The live-renderer arm, `check_renderer_live(root)`, run by `python
  tools/playbook/render_playbook.py --check-render`. For each path on
  `tools/playbook/instructions-legacy.txt` (I17), the row claiming it must name a `playbook:<scope>`
  the renderer declares, or carry a `leg` that `tools/gate-legs.json` holds. A row naming neither reds,
  naming the row's renderer, the listed path and the missing leg. A row claiming no listed path is not
  graded. Observed by AC1 and AC2.
- **S3** — kit/dogfood doc parity retired. Once unit 7 takes its four documents to the one renderer,
  this unit removes `tools/memory-tree/kit-dogfood-parity.test.sh`, its `[[gate_leg]]` row
  `kit/dogfood doc parity` (`tools/memory-tree/kit.toml:247-250`), and the inline `render_doc` block in
  `tools/memory-tree/adopt-memory-tree.sh:510` with its caller at `:590`. Observed by AC3.
  **Readers:** by name: `tools/gate-legs.json:437` (rendered from the kit's row), `tools/govkit/subject-pins.tsv:63`,
  `tools/run-gates/ceiling-evidence.txt:74`, `tools/memory-tree/README.md`, `.gitattributes`,
  `.governance/install.json`, `skills/session-kickoff/manifest-check.sh`, `tools/check-playbook-parity.sh`,
  `tools/memory-tree/check-verdict-epoch.sh`, `tools/memory-tree/check-verdict-epoch.test.sh`,
  `tools/memory-tree/hygiene-parity.test.sh`, `tools/unattended/gate-guard.test.sh` and
  `tools/govkit/selftest.py` · by value: `tools/run-gates/ceiling-evidence.txt:74`, whose measured
  seconds the runner's ceiling reads, and `tools/govkit/subject-pins.tsv:63`, whose subject the
  acceptance matrix compares.
- **S4** — Review-protocol parity narrowed to its harness pairs. Its document pair
  (`tools/workflows/check-protocol-parity.test.sh:94`) leaves with `REVIEW-PROTOCOL.md` (unit 7). The leg
  `review-protocol parity (kit vs dogfood)` (`tools/workflows/kit.toml:130`) keeps its four `.js` pairs,
  which render no instruction file and which the fates record keeps (scout B finding 6). This departs from
  the clause's word for that leg: deviation 81. Observed by AC4.
- **S5** — `render_doc` retired from the lib. With S3 its last inline copy is gone, so the `render_doc`
  block leaves `tools/lib/render-doc.sh` and its parity row leaves `PARITY_ROWS`
  (`tools/lib/resolve-python.test.sh:354`). The file keeps `derive_kit_paths`, `render_kit_cites` and
  `check_kit_cites`, whose inline copies the `.js` pairs of S4 still read. Observed by AC5.
  **Readers:** by name: `tools/lib/resolve-python.test.sh:354`, `tools/memory-tree/adopt-memory-tree.sh:510`
  and `:590`, `tools/memory-tree/kit-dogfood-parity.test.sh` (removed by S3) ·
  by value: NO VALUE READERS, the parity table compares the block's bytes by name, which the by-name
  half lists.
- **S6** — Each kit's Skill wiring `--check`. Once unit 9 makes each kit adopter's Skill arm a caller of
  `--check-render --scope skills`, that call leaves the `--check` of `tools/lexicon/adopt-lexicon.sh`,
  `tools/drift-audit/adopt-drift-audit.sh` and `tools/branch-reconcile/adopt-branch-reconcile.sh`, so the
  kit's `[check]` argv grades its own conf and wiring only, and the one renderer's check in
  `instruction render (one renderer of record)` grades the entry. The legs that ran those `--check`
  argvs are already folded into `kit wiring (every descriptor's check)` by DEPL-dShippedRelease-10 S10.
  Observed by AC6.
- **S7** — Govkit's placeholder render in adopters, for instruction files. Every `rendered` `[[files]]`
  row whose `to` is an instruction file (`INSTRUCTION_PATHSPECS`, PLAY-dOrderedCharter-20 S4) leaves its
  `placeholders` list, its `[[regenerate]]` argv the one renderer's scope, so no adopter substitutes a
  token in an instruction file. At base those rows are `tools/memory-tree/kit.toml:59`, `:65`, `:71` and
  `:77`, `tools/roles/kit.toml:58`, `tools/workflows/kit.toml:43` and the five kits' Skill rows; those
  units 7, 9, 12 and 17 have not removed are re-derived at the first pass. `check-kit-placeholders.py`
  then joins no instruction-file row. Observed by AC7.
  **Readers:** by name: each row's adopter script, whose literal `{{TOKEN}}` substitution for that file
  goes with it · by value: `tools/check-kit-placeholders.py`, which joins each declared token with its
  adopter's substitution and so counts fewer rows.

## 3. Non-goals (OUT)

- Moving any document: units 7 (guides and templates), 9 (Skills) and 10 (the scopes) move them; this
  unit retires what they leave behind.
- The `playbook-placeholders` hole and `check-placeholders.sh --check`: DEPL-dShippedRelease-10 S9
  keeps the survival mode, and the charter's renderers were absorbed at dOrderedCharter.
- The four `.js` harness pairs and the three cite blocks of `render-doc.sh`: kept (S4, S5).
- Folding wiring legs into one: DEPL-dShippedRelease-10 S10's, which §8 F2 settles against
  PLAY-dOrderedCharter-20 S6.
- `/build`'s and `/unattended`'s renderers: units 17 and 12 retire those Skills and their adopters' arms.

### Edges

- **consumes-from** `PLAY-dConvergedCharter-10` — `renderers.toml`, the `protocols` and `skills` scopes' `[[target]]` rows S2 joins the legacy list against
- **consumes-from** `PLAY-dConvergedCharter-7` — `help.explanation`'s `explanation` scope, and the guides and templates moved off `render-doc` and out of both parity tests' `PAIRS`, without which S3 and S4 would retire a renderer with documents left
- **consumes-from** external — PLAY-dOrderedCharter-20 S4, S5, S8 and S10, DEPL-dShippedRelease-9 S2 and DEPL-dShippedRelease-10 S10, each DEFERRED at base and built before this unit's build pass

## 4. Design

### Evidence

Read at `d8a12f046`; no product file differs from base `0d1c1dda`.

- `PAIRS` of `tools/memory-tree/kit-dogfood-parity.test.sh:61` holds four document pairs: `HYGIENE.md`,
  `TEMPLATE-SPEC.md`, `guides/BUILD-METHOD.md` and `guides/ANNOTATION-STYLE.md`.
- `PAIRS` of `tools/workflows/check-protocol-parity.test.sh:94-98` holds `guides/REVIEW-PROTOCOL.md` and
  four `.js` pairs: `unattended-build`, `tier2-review`, `drift-audit-code` and `drift-audit-state`. The
  `.js` renders go through `derive_kit_paths`, `render_kit_cites` and `check_kit_cites` (`:315-530`).
- `tools/lib/render-doc.sh` holds four canonical blocks: `render_doc` (`:38-78`), `derive_kit_paths`,
  `render_kit_cites` and `check_kit_cites`. `render_doc` has inline copies in
  `tools/memory-tree/adopt-memory-tree.sh:510` and the kit/dogfood test; the cite blocks also sit in
  `tools/workflows/check-protocol-parity.test.sh` and `tools/unattended/adopt-unattended.sh:441`.
- PLAY-dOrderedCharter-20 §4 seeds the guides and the two templates on one row `renderer = "render-doc"`.
- The wiring legs at base include `memory-recall skill wiring`, `runlog skill wiring`, `cleanup skill
  wiring`, `drift-audit wiring` and `lexicon wiring`, each running its adopter's `--check`.
- Scout B row 8 and findings 5 and 6 hold against source at `d8a12f046`.

### Data model

```toml
# tools/playbook/renderers.toml, a row still beside the legacy list
[[target]]
paths = ["{memory_root}/guides/*.md"]
renderer = "render-doc"
leg = "kit/dogfood doc parity"
```

### Inventory

Minted: the row key `leg`, `check_renderer_live` (asked of `python tools/lexicon/lexicon.py --suggest
check_renderer_live --as py.function` at `d8a12f046`: OK), and the plant cases `renderer-retired-early`
and `renderer-retired-last` on PLAY-dOrderedCharter-20 S10's fixture verb.

### Files touched (estimate)

- `tools/playbook/render_playbook.py`, `tools/playbook/renderers.toml`
- `tools/memory-tree/kit-dogfood-parity.test.sh` (removed), `tools/memory-tree/kit.toml`,
  `tools/memory-tree/adopt-memory-tree.sh`, `tools/memory-tree/README.md`
- `tools/lib/render-doc.sh`, `tools/lib/resolve-python.test.sh`
- `tools/govkit/subject-pins.tsv`, `tools/run-gates/ceiling-evidence.txt`, `tools/govkit/selftest.py`
- `tools/workflows/check-protocol-parity.test.sh`
- `tools/lexicon/adopt-lexicon.sh`, `tools/drift-audit/adopt-drift-audit.sh`,
  `tools/branch-reconcile/adopt-branch-reconcile.sh`
- `tools/lexicon/kit.toml`, `tools/drift-audit/kit.toml`, `tools/branch-reconcile/kit.toml`,
  `tools/runtime/kit.toml`
- `tools/check-kit-placeholders.py`
- `.gitattributes`, `tools/check-playbook-parity.sh`, `tools/memory-tree/check-verdict-epoch.sh`,
  `tools/memory-tree/hygiene-parity.test.sh` (readers of S3)

### Alternatives rejected

- **A `[[retired]]` row in `tools/govkit/registry.toml` per renderer, joined by the arm.** Rejected by
  reading `read_retired` (`tools/govkit/upgrade_steps.py:890-930`): its id is "an entry id or an
  upgrade-step id", and `update` acts on a retired entry, so a renderer id there is misread as a kit.
- **The arm keyed by compare base: a leg removed between base and tip.** Rejected because the static
  join of S2 reds the same plant with no history read, and stays true on a tree with no base.
- **Retiring `render-doc.sh` whole, as the spec brief's unit row reads.** Rejected by the four `.js`
  pairs: their renders read the three cite blocks, and the fates record keeps that check (S4).

## 5. Production-readiness checklist

- security — no new write surface; the arm reads two declared files.
- perf / scale — one pass over the legacy list and the manifest.
- error / empty / loading states — an empty legacy list grades nothing and prints `renderer live:
  graded 0 listed path(s)`.
- observability — each red names renderer, path and leg.
- risks — a renderer whose leg stays while its code goes: its own leg then reds, which is the bar's
  signal and outside this arm.
- testing — the two plant cases, each in a throwaway tree.
- migration — none for adopters beyond units 7 and 9's: their rows already regenerate through the one
  renderer.
- user docs — `tools/memory-tree/README.md` loses the parity test's section; `tools/playbook/README.md`
  names the `leg` key.

## 6. Acceptance criteria

- **AC1** — When `python instruction_units.py fixture --plant renderer-retired-early` lists
  `memory/HYGIENE.md` on the legacy list under a row `leg = "kit/dogfood doc parity"` and removes that
  leg from the fixture's manifest, `render_playbook.py --check-render` exits 1 naming `render-doc`,
  `memory/HYGIENE.md` and the leg.
  Red when: a renderer's leg is gone while a document it renders stays listed, and the check passes.
- **AC2** — When the plant `renderer-retired-last` takes the path off the legacy list in the same tree,
  `render_playbook.py --check-render` exits 0, and with an empty list it prints `graded 0`.
  Red when: a renderer retired with its last document reds, or an empty population prints a bare green.
- **AC3** — When `git ls-files tools/memory-tree/kit-dogfood-parity.test.sh` and `git grep -n -F
  "kit/dogfood doc parity" -- . ':!memory'` run after the unit lands, both print nothing.
  Red when: the test file or a reader of its leg name survives.
- **AC4** — When `grep -n -A4 "^PAIRS=" check-protocol-parity.test.sh` runs in `tools/workflows/` after the
  unit lands, the `PAIRS` declaration it prints holds four pairs, each a `.js` live copy and its
  `.template.js`, and no `.md` document.
  Red when: a document pair remains, or a `.js` pair is dropped.
- **AC5** — When `grep -c ">>> render_doc" tools/lib/render-doc.sh` runs after the unit lands it prints
  0, and `grep -c "^render_doc|" tools/lib/resolve-python.test.sh` prints 0.
  Red when: the block or its parity row survives its last copy.
- **AC6** — When `bash tools/lexicon/adopt-lexicon.sh --check` runs after the unit lands, it names no
  Skill path and exits 0.
  Red when: an adopter's `--check` still renders or compares a Skill.
- **AC7** — When `python tools/check-kit-placeholders.py --list` runs after the unit lands, it lists no
  row whose `to` is an instruction file.
  Red when: an instruction file is still filled by an adopter's placeholder substitution.

## 7. Gates

`playbook render selftest` · `govkit acceptance matrix` · `policy fixtures` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `codebase-map kit selftest` · `lexicon selftest` · `drift-audit selftest` · `branch-reconcile selftest` · `playbook parity selftest` · `review-protocol parity (kit vs dogfood)` · `kit placeholders (a declared token its adopter substitutes)` · `python resolver (behaviour + inline parity + idiom ban)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The parent leg `instruction render (one renderer of record)` runs S2 once it lands; it is not in the
manifest at base. `kit/dogfood doc parity` is removed by S3, so it is not on the line.

New arm: tools/playbook/render_playbook.py · covers AC1 AC2 · the plants `renderer-retired-early` and `renderer-retired-last`, the failing case a legacy-listed document whose renderer's leg is gone · none
New arm: tools/workflows/check-protocol-parity.test.sh · covers AC4 · `PAIRS` narrowed to its four `.js` pairs, staged red by the `REVIEW-PROTOCOL.md` pair restored to `PAIRS` once its live copy is gone · none

## 8. Open questions

- **F1 — How does the arm know a renderer is retired?** Options: (a) a `leg` key on the row, the leg's
  absence from the manifest being the retirement; (b) a `[[retired]]` registry row per renderer; (c) a
  compare-base diff of the manifest. (b) is misread by `update` (§4 "Alternatives rejected"). RESOLVED
  (agent, 2026-11-03, delegated): (a), rung 3, a key additive like `region`. The ask, target build
  dOrderedCharter: PLAY-dOrderedCharter-20 S4 names the optional `leg` key of a `[[target]]` row, so its
  reader admits it; accept: a `renderers.toml` row carrying `leg` passes `--check-render`'s table arm.
  widens: none · relaxes: none
- **F2 — Which leg runs a kit's `--check` once the renderers fold (scout B finding 5)?** Options: (a)
  DEPL-dShippedRelease-10 S10's one leg `kit wiring (every descriptor's check)`, which retires
  `playbook render wiring` and `roles render wiring` with nine others; (b) PLAY-dOrderedCharter-20 S6,
  which keeps those two names as scopes of its gate. (b) leaves the eleven-leg gap DEPL-dShippedRelease-10
  §8 F6 closes. RESOLVED (agent, 2026-11-03, delegated): (a), rung 3. The ask, target build
  dOrderedCharter: PLAY-dOrderedCharter-20 S6 names `kit wiring (every descriptor's check)` as the leg
  that runs the `charter` and `agents` scopes' wiring check, in place of `playbook render wiring` and
  `roles render wiring`; accept: neither name appears in PLAY-dOrderedCharter-20 outside a retirement
  clause. widens: none · relaxes: none
- **F3 — Review-protocol parity with no document left (scout B finding 6).** Options: (a) retire the
  leg, losing the four `.js` pairs' check; (b) narrow the leg to the `.js` pairs and record the
  departure; (c) split the leg in two. (a) fails the fates record's "STAYS" for the workflows kit's
  parity (research-tool-fates `:68`), the owner's table, and (b) and (c) each fail the clause's "each
  retired with its last document" for this leg, so no option survives veto 1. (c) adds a leg for nothing
  (b) lacks, and the clause's bound is the one that names a renderer of documents, which this leg no
  longer is once S4 lands. Deviation 81 records the relaxed bound.
  RESOLVED (agent, 2026-11-03, delegated): (b), rung 6, ER:328 · widens: none · relaxes: the clause's "each retired with its last document" for `review-protocol parity (kit vs dogfood)`

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, from the packet's Item 8, systems `[design-instruction-writing]`
  (`:398-406`), research-tool-fates `:50`, `:63`, `:68`, scout B row 8 and findings 5 and 6, and the spec
  brief's I17 and I18.

## 10. Reuse audit

The seams extended are `render_playbook.py --check-render` and `renderers.toml` (PLAY-dOrderedCharter-20
S4, S8), the legacy list (S8), the leg manifest `tools/gate-legs.json` read as the renderers' presence,
and the inline-copy parity table `PARITY_ROWS` (`tools/lib/resolve-python.test.sh:351-365`), from which
one row leaves. `python tools/codebase-map/reuse_lookup.py "retire a renderer once its last document leaves
the legacy list"` ranked `read_id_list`, `read_retired` (`tools/govkit/upgrade_steps.py:890`),
`check_legacy_graded` and `check_legacy_homes` (`tools/policy/policy.py`); `read_retired` was tried as
the join and rejected in §4, and the two policy checks grade conf legacy homes, not renderers. The arm
is new, on the renderer's own check. Scout B row 8 holds against source at `d8a12f046`, except that
`render-doc.sh` cannot leave whole: three of its four blocks stay (S5).

Recall terms used: `python tools/memory-recall/query.py "which renderers retire once their last document migrates to the one renderer" --terms "kit/dogfood parity review-protocol parity render-doc renderer retired legacy list skill wiring placeholder"`
