# PLAY-dConvergedCharter-15 — the hand-written `help/` pages, the kit READMEs, root `README.md` and the runbook migrated: a generated reference half, a how-to half under the docs leg, render parity on both

**Status:** OPEN · rev-1 · 2026-11-03 · node d · Tier-2 · base 0d1c1dda · streams playbook · order 20 · advances PLAY-dConvergedCharter-24

**Carries:** cl-dClosedLoop-0489@74c9a546 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md](../build/2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-03-build-PLAY-dConvergedCharter-6-reuse-scout-b.md](../build/2026-11-03-build-PLAY-dConvergedCharter-6-reuse-scout-b.md) | research | PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 |
| [2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md](../build/2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md) | journal | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-39 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md](../reviews/2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md) | spec-audit | PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-18 |

<!-- /gen:spec-records -->

## 1. Goal

The charter's `[docs]` rule binds every user-facing change to its page under `help/`, and the pages,
the kit READMEs, root `README.md` and the agent runbook `WIRE-INTO-PROJECT.md` restate their registries
by hand (gap-found-27). This unit migrates each: a fates row; a reference half generated from its
registry by dOrderedCharter's renderer, the runbook's taken as dShippedRelease derives it; and a
how-to half written as a page the docs leg grades. A hand edit to a rendered page is red at render
parity (SA-5, the owner's FQ-5).

## 2. Scope (IN)

- **S1** — The fates rows. Each migrated population has a fates row: `help/` pages is the fates
  record's `[table]` row (top-level, `help/` pages, RESHAPED, fates `:198`); kit READMEs, root
  `README.md` and the agent runbook have none (final-questions `:243` asks for them). Unit 14
  materializes `tools/govkit/fates.toml` (I22) after this unit, so the four rows this unit needs are
  handed to it, each `[[part]]` with `kit = "top-level"`, its function, `fate = "RESHAPED"`, `where`
  naming this unit's halves, and `paths`: `["help/**"]`, `["tools/*/README.md"]`, `["README.md"]` and
  `["WIRE-INTO-PROJECT.md"]`. Observed by AC1.
- **S2** — The help pages' reference half. In each of the twelve hand-written pages under `help/`, a
  section whose `<!-- usage: <id> <fp8> -->` anchor is a member of a class a `[[reference]]` row renders
  (PLAY-dOrderedCharter-37 S1: the policy catalogue and the drive table) moves to the rendered page that
  row declares, `help/reference/<page>.md`. The hand page keeps its how-to text and links the member's
  section there. At `d8a12f046` that is thirteen `policy:` anchors over eight pages and one `command:`
  anchor (§4 "The pages"). `script:` and `verb:` anchors are how-to and stay. Observed by AC2 and AC3.
  **Readers:** by name: `tools/govkit/docs_leg.py` (`read_page_anchors`, `:247`), which reads each
  anchor where it sits, and `memory/project/docs-undocumented.txt`, which lists members no page anchors
  · by value: `docs_leg.py`'s stale-page arm, which compares each anchor's `fp8` with the member's
  fingerprint, and PLAY-dOrderedCharter-37 S4's `--fingerprints`, which the render reads.
- **S3** — The `readme` scope (I18). `python tools/playbook/render_playbook.py --render-scope readme`
  writes three kinds of region through `splice_region`, as DEPL-dShippedRelease-9 S2 writes the
  runbook's, each claimed by a `[[target]]` row of `tools/playbook/renderers.toml` with `renderer =
  "playbook:readme"` and its `region`:
  - `gov:kit-reference` in each `tools/<kit>/README.md`, `render_kit_reference(row)` over that kit's
    `read_kit_rows(root)` row (DEPL-dShippedRelease-10 S6): its id, `summary`, `requires`, the files it
    installs (`to` rows), its legs and its commands;
  - `gov:kit-index` in root `README.md`, `render_kit_index(rows)`: one line per kit in install order,
    its home and `summary`, in place of the hand-written `## Contents` list;
  - `gov:help-index` in `help/README.md`: every page under `help/` by directory, so `help/why/README.md`
    (unit 7) is linked exactly while `help.explanation` renders that tree.
  `--check-render --scope readme` compares each region's bytes; bytes outside a region stay hand-written.
  Observed by AC4 and AC5.
- **S4** — A one-line `summary` on every kit descriptor. `read_kit_rows` returns no human sentence today
  (gap-found-36: 0 of 29 descriptors). One `[[field]]` row in `tools/playbook/kit-schema.toml`
  (DEPL-dShippedRelease-10 S1), `summary`, `type = "text"`, `required = "every"`, and the key on every
  descriptor, so the unknown-key and required arms of that unit's gate grade it. Observed by AC4.
- **S5** — The runbook. Its reference half is DEPL-dShippedRelease-9's `gov:runbook-order` region,
  taken as that unit derives it, with no second render here. Observed by AC6.
- **S6** — The how-to halves under the docs leg. The docs leg's page walk (`tools/govkit/docs_leg.py:413`,
  `help/**/*.md` today) also walks each path a `[[target]]` row of the `readme` or `runbook` scope
  claims, read from `tools/playbook/renderers.toml`, so one declaration names both the rendered region
  and the graded page. A command a README or the runbook shows outside a region is then anchored, its
  links checked and its staleness graded like a page under `help/`, under `help.enforce`. A member a
  newly walked page anchors leaves `memory/project/docs-undocumented.txt` by its shrink-only rule.
  Observed by AC6 and AC7.

## 3. Non-goals (OUT)

- The reference renderer, `references.toml` and the `help/reference/` pages: PLAY-dOrderedCharter-37's.
  This unit moves hand sections onto them and adds no `[[reference]]` row.
- The runbook's region and its parity: DEPL-dShippedRelease-9's.
- `help/why/` and its scope: unit 7's. This unit only links its index.
- Materializing the fates table and its exit check: unit 14's.
- New concept, task or tutorial pages: PLAY-dOrderedCharter-37 S6's three; this unit writes no page.
- Kit README prose beyond its region and the how-to sentences the docs leg grades.

### Edges

- **consumes-from** `PLAY-dConvergedCharter-7` — `help/why/`, the explanation tree and its index page, which S3's help index links while it exists
- **consumes-from** `PLAY-dConvergedCharter-10` — `renderers.toml`, the scope grammar S3's `readme` rows follow and S6 reads the claimed paths from
- **hands-off** `PLAY-dConvergedCharter-14` — `fates.toml`, the four `[[part]]` rows of S1 (`help/` pages, kit READMEs, root `README.md`, the agent runbook), which that unit materializes with the record's `[table]`
- **consumes-from** external — PLAY-dOrderedCharter-20 and -37, DEPL-dShippedRelease-9 and -10, TOOL-dLinkedLibrary-18 (`splice_region`), each DEFERRED at base and built before this unit's build pass

## 4. Design

### Evidence

Read at `d8a12f046`; no product file differs from base `0d1c1dda`.

- `help/` holds `README.md` and twelve hand-written pages (PINNED, `ls help/`), not the two
  PLAY-dOrderedCharter-37 §1 counts (scout B finding 2).
- `tools/` holds 18 kit READMEs; `tools/govkit/` and `tools/lib/` have none. Root `README.md` is 119
  lines, its `## Contents` a hand list of kits from `:9`. `WIRE-INTO-PROJECT.md` is 2,200 lines.
- The docs leg walks `help/**/*.md` only (`tools/govkit/docs_leg.py:413`), reads anchors at `:247` and
  links at `:354`, and reads `help.enforce` at `:727`. Its leg is `docs`.
- `tools/govkit/check_runbook_parity.py:60` pins `PROBLEM_PIN = 18`; DEPL-dShippedRelease-9 S6 re-reads
  it over the region.
- No kit descriptor carries a human sentence: `grep -c '^summary' tools/*/kit.toml` prints 0 for each.
- The fates `[table]` holds a `help/` pages row (`:198`) and no row for kit READMEs, root `README.md` or
  the runbook; the runbook appears only as govkit's "runbook parity … STAYS" (`:180`).

### The pages

| Page | Anchors moving to a reference page |
|---|---|
| `help/agent-limit.md` | `policy:runtime.agents-in-flight` |
| `help/docs-leg.md` | `policy:help.enforce` |
| `help/policy.md` | `policy:policy-file.on-invalid` |
| `help/python-floor.md` | `policy:platforms.provision` |
| `help/shims.md` | `policy:install.deprecation-window`, `policy:install.on-shim-call` |
| `help/size-caps.md` | `policy:budgets.*`, `policy:budgets.enforce`, `policy:budgets.pinned` |
| `help/spec-audit.md` | the three `policy:review.spec-audit.*` keys |
| `help/update-edits.md` | `policy:install.retired-edits` |
| `help/roles.md` | `command:build`, which unit 17 retires first; the anchor goes with it |

`help/measure-legs.md`, `help/step-gate.md` and `help/upgrade-steps.md` anchor `script:` and `verb:`
members only, so they move nothing. The set is PINNED at `d8a12f046` and DERIVED again at the build
pass from each anchor's class.

### Data model

```markdown
<!-- gov:kit-reference -->
**lexicon** · Answers what to call a name from the repository's declared vocabulary.
- requires: none
- installs: `.lexicon.conf`, `.claude/skills/gov-lexicon/SKILL.md`
- legs: `lexicon selftest`, `lexicon naming predicates`
- commands: `lexicon.py --suggest`, `lexicon.py --check`
<!-- /gov:kit-reference -->
```

### Inventory

Minted: the scope `readme`, its regions `gov:kit-reference`, `gov:kit-index` and `gov:help-index`,
`render_kit_reference` and `render_kit_index` (each asked of `python tools/lexicon/lexicon.py --suggest
<name> --as py.function` at `d8a12f046`: OK), the descriptor key `summary`, and the plant cases
`readme-hand-edit` and `readme-page-command` on PLAY-dOrderedCharter-20 S10's fixture verb.

### Files touched (estimate)

- `tools/playbook/render_playbook.py`, `tools/playbook/renderers.toml`, `tools/playbook/kit-schema.toml`
- `tools/govkit/docs_leg.py`, `memory/project/docs-undocumented.txt`
- `help/README.md`, `help/agent-limit.md`, `help/docs-leg.md`, `help/policy.md`, `help/python-floor.md`,
  `help/shims.md`, `help/size-caps.md`, `help/spec-audit.md`, `help/update-edits.md`, `help/roles.md`
- `README.md`, `WIRE-INTO-PROJECT.md` (outside DEPL-dShippedRelease-9's region)
- `tools/govkit/entries/` (the `summary` key)
- `tools/agent-instructions/README.md`, `tools/agent-instructions/kit.toml`,
  `tools/branch-reconcile/README.md`, `tools/branch-reconcile/kit.toml`, `tools/codebase-map/README.md`,
  `tools/codebase-map/kit.toml`, `tools/drift-audit/README.md`, `tools/drift-audit/kit.toml`,
  `tools/gate-lint/README.md`, `tools/gate-lint/kit.toml`, `tools/hooks/README.md`, `tools/hooks/kit.toml`,
  `tools/lexicon/README.md`, `tools/lexicon/kit.toml`, `tools/memory-recall/README.md`,
  `tools/memory-recall/kit.toml`, `tools/memory-tree/README.md`, `tools/memory-tree/kit.toml`,
  `tools/playbook/README.md`, `tools/playbook/kit.toml`, `tools/policy/README.md`, `tools/policy/kit.toml`,
  `tools/process-monitor/README.md`, `tools/process-monitor/kit.toml`,
  `tools/pytest-parallel-guardrails/README.md`, `tools/pytest-parallel-guardrails/kit.toml`,
  `tools/roles/README.md`, `tools/roles/kit.toml`, `tools/run-gates/README.md`, `tools/run-gates/kit.toml`,
  `tools/runlog/README.md`, `tools/runlog/kit.toml`, `tools/workflows/README.md`, `tools/workflows/kit.toml`

### Alternatives rejected

- **The how-to halves moved into new pages under `help/`.** Rejected because every reader of the
  runbook's path and of a kit's README (the charter's Facts, the kickoff engine, the adopters) would
  follow the text to a second home, which is one fact in two places; widening the docs leg's walk to the
  claimed paths grades the same text where it is.
- **The kit README's reference half as a `[[reference]]` row of PLAY-dOrderedCharter-37.** Rejected
  because that renderer writes whole pages under `help/reference/` and refuses one outside it (S3), and a
  kit README's reference sits inside a hand-written file, which is the region form
  DEPL-dShippedRelease-9 already uses.
- **A `summary` field on the kit index alone, typed in the renderer.** Rejected by the derive rule: the
  sentence is a fact of the kit and belongs on its descriptor, where `read_kit_rows` returns it.

## 5. Production-readiness checklist

- security — the scope writes only between the markers its rows claim; a missing or doubled marker
  refuses with the file unchanged, as DEPL-dShippedRelease-9 S5 states.
- perf / scale — one `read_kit_rows` call per render, linear in the kits.
- error / empty / loading states — a descriptor with no `summary` reds the kit gate before any render;
  a README with no markers refuses naming it.
- observability — the scope prints each region written; the docs leg prints its widened page count.
- risks — widening the docs leg's walk may surface links and commands in the READMEs that are stale
  today; they are fixed in this unit, never listed away.
- testing — the plant cases of the Inventory, each in a throwaway tree.
- migration — the markers are inserted once per README; adopters receive the regions with the kits.
- user docs — this unit is the user docs: `help/README.md`'s index and each kit README's region.

## 6. Acceptance criteria

- **AC1** — When `grep -n -E "README.md|WIRE-INTO-PROJECT.md|help/" fates.toml` runs once unit 14 has
  materialized the table, it prints the four `[[part]]` rows of S1, each `fate = "RESHAPED"`.
  Red when: a migrated population has no fates row.
  fixture: the table is unit 14's, built after this unit, so the observation waits on it.
- **AC2** — When `python tools/govkit/docs_leg.py` runs after the unit lands, no hand-written page under
  `help/` anchors a `policy:` or `command:` member, and every such member's anchor is
  on a rendered reference page.
  Red when: a hand page still states a key a reference page renders.
- **AC3** — When `render_playbook.py --reference --check` runs after the unit lands, it exits 0, and a
  planted edit inside the rendered policy reference page makes it exit 1 naming the page.
  Red when: a hand edit to a rendered reference page passes.
- **AC4** — When `python instruction_units.py fixture --plant readme-hand-edit` renders the `readme`
  scope over a two-kit tree and then edits a line inside one `gov:kit-reference` region,
  `render_playbook.py --check-render --scope readme` exits 1 naming the README and the region; the
  same tree unedited exits 0, and a descriptor with no `summary` reds the kit gate.
  Red when: a hand edit inside a region passes, or a kit renders with no summary.
- **AC5** — When `render_playbook.py --render-scope readme` runs with `help.explanation` reading
  `registry-only`, `help/README.md`'s index names no page of the `why` tree, and with `rendered` it
  names that tree's index.
  Red when: the index links a tree that is absent, or omits one that is present.
- **AC6** — When `python tools/govkit/docs_leg.py` runs after the unit lands, its page count includes
  `WIRE-INTO-PROJECT.md`, `README.md` and the 18 kit READMEs, and `render_playbook.py --check-render
  --scope runbook` exits 0.
  Red when: a claimed path is not walked, or the runbook region is rendered twice.
  figure: 18 is PINNED at `d8a12f046`; the walked count is DERIVED by the run.
- **AC7** — When `python instruction_units.py fixture --plant readme-page-command` plants a README whose
  how-to half shows a command with a flag its verb does not declare, `docs_leg.py` reds it naming the
  README, as it reds the same on a page under `help/`.
  Red when: a README's command is ungraded.

## 7. Gates

`docs` · `govkit runbook parity` · `govkit acceptance matrix` · `playbook render selftest` · `policy fixtures` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `recall floor` · `agent-instructions self-test` · `branch-reconcile selftest` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `drift-audit selftest` · `shell-hygiene selftest` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `lexicon selftest` · `pytest-guardrails self-test` · `pre-push run-log line` · `runlog selftest` · `run-gates run-log line` · `tier2-review self-test` · `unattended-build self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The parent leg `instruction render (one renderer of record)` runs S3's parity once it lands; it is not
in the manifest at base.

New arm: tools/playbook/render_playbook.py · covers AC4 AC5 · the plants `readme-hand-edit` and the help index under each `help.explanation` value, the failing case an edit inside a `gov:kit-reference` region · none
New arm: tools/govkit/docs_leg.py · covers AC7 · the plant `readme-page-command`, the failing case an undeclared flag shown in a README's how-to half · none

## 8. Open questions

- **F1 — Where does a README's or the runbook's how-to half live?** Options: (a) in place, the docs
  leg's walk widened to the paths the `readme` and `runbook` scopes claim; (b) moved to new pages under
  `help/`. (b) splits one document across two homes and moves every reader of the runbook path.
  RESOLVED (agent, 2026-11-03, delegated): (a), rung 3, "a page under the docs leg" read as a page the
  docs leg grades. widens: none · relaxes: none
- **F2 — Where do the four missing fates rows go before unit 14?** Options: (a) handed to unit 14 as
  rows of `tools/govkit/fates.toml`; (b) written into the fates record. (b) edits another build's frozen
  record. RESOLVED (agent, 2026-11-03, delegated): (a), rung 3. widens: none · relaxes: none
- **F3 — The kit sentence's source.** Options: (a) a `summary` key on every descriptor with its
  `[[field]]` row; (b) the README's first paragraph read as the summary. (b) derives a registry fact from
  prose, the inverse of the clause. RESOLVED (agent, 2026-11-03, delegated): (a), rung 3, additive with a
  required field, and it closes the kit-descriptor third of gap-found-36. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, from the packet's Item 15, final-questions `:228-244`, `:345`,
  `:375`, the fates rows `:180` and `:198`, scout B row 15 and finding 2, and the spec brief's I18, I21
  and I22.

## 10. Reuse audit

The seams extended are `render_playbook.py`'s scopes (PLAY-dOrderedCharter-20 S5) with the region form
`splice_region` and the `runbook` scope (DEPL-dShippedRelease-9 S1-S2), `read_kit_rows`
(DEPL-dShippedRelease-10 S6) and `kit-schema.toml`'s `[[field]]` rows, the reference renderer
(PLAY-dOrderedCharter-37 S1-S2), and the docs leg's page walk (`tools/govkit/docs_leg.py:413`). `python
tools/codebase-map/reuse_lookup.py "render a help reference page from a registry and check render
parity"` ranked `check`, `render`, `checks`, `build_reference_index` (`tools/codebase-map/map_lib.py`),
`check_line` and `render_cards_md`; `build_reference_index` indexes symbol references for the map, not
pages. `render_kit_reference` and `render_kit_index` are new, on the `runbook` scope's region seam. Scout
B row 15 holds against source at `d8a12f046`, and its finding 2 (thirteen files under `help/`, not two)
is confirmed.

Recall terms used: `python tools/memory-recall/query.py "how do help pages, kit READMEs and the runbook get generated reference halves" --terms "help pages kit README runbook reference rendered registry how-to docs leg fates render parity"`
