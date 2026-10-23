# PLAY-dOrderedCharter-41 — the `cross-os` block stays live, so every v4 template renders after the practice catalogue lands

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ce13efbe · streams playbook · order 18 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-PLAY-dOrderedCharter-39-promoted-fix-return.md](../build/2026-10-24-build-PLAY-dOrderedCharter-39-promoted-fix-return.md) | research | PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 |
| [2026-10-24-build-PLAY-dOrderedCharter-41-deviation-411.md](../build/2026-10-24-build-PLAY-dOrderedCharter-41-deviation-411.md) | deviation | — |
| [2026-10-24-prompt-PLAY-dOrderedCharter-39-promoted-fix-brief.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-39-promoted-fix-brief.md) | research | PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 |
| [2026-10-24-review-PLAY-dOrderedCharter-39-spec-audit.md](../reviews/2026-10-24-review-PLAY-dOrderedCharter-39-spec-audit.md) | spec-audit | PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-49 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dOrderedCharter/reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md`)
confirmed **finding 30 at HIGH**, its item **H3**. `PLAY-dOrderedCharter-1` S6 marks the `cross-os`
`[[block]]` row `legacy` and moves the template marker only to v4.5. `render()` refuses any template
at or above `TEMPLATE_MAJOR` (4) whose `when` fence names a legacy block
(`tools/playbook/render_playbook.py:1004-1012`), and gov's template still carries
`<!-- when:cross-os -->` at line 198, around the Toolchain section, as every seeded v4.x adopter
template carries the section-1 fence. Gov's re-render (unit 1 AC4) and every adopter's render would
refuse. Unit 1's Migration line is also wrong: the reseed note fires only when the major is behind
(`:1026-1029`), never for v4.4 against v4.5. This unit keeps `cross-os` a live block, keeps S6's
mapping of `drop_blocks` onto the practice set, states the major-only rule, and arms a render probe
over gov's template and a seeded previous-minor template. It repairs unit 1 and is built right after
it.

## 2. Scope (IN)

- **S1** — The row stays live. The `cross-os` `[[block]]` row in
  `tools/govkit/entries/playbook.kit.toml:285-287` carries no `legacy` key at this unit's close. This
  supersedes unit 1 S6's "the `cross-os` `[[block]]` row ... gains `legacy`". Where unit 1 landed the
  key, this unit takes it off the row.
  **Readers:** by name: `tools/govkit/entries/playbook.kit.toml`, the row, and
  `tools/playbook/render_playbook.py`, which reads the `legacy` key of every block row · by value:
  `render()`'s legacy set and its refusal (`tools/playbook/render_playbook.py:1008-1012`), which this
  item keeps `cross-os` out of. Observed by AC1 and AC2.
- **S2** — The mapping, without the legacy path. A `drop_blocks` member `cross-os` still cuts the
  fenced text the template carries (the Toolchain section at `coding-governance-agents.template.md:198-200`,
  and on a seeded v4.4 template the section-1 line at `:42-44` too) and leaves `practice.cross-os` out of
  the active set unit 1's reader resolves. The render prints one note,
  `practices drop_blocks cross-os also leaves practice.cross-os out of the active set; charter.practices names the set directly`,
  in place of unit 1 S6's note, because the member still cuts a live block. Observed by AC2 and
  AC3.
- **S3** — The rule restated. `render_playbook.py`'s comment above `TEMPLATE_MAJOR`
  (`tools/playbook/render_playbook.py:336-342`) and unit 1's catalogue docs in `help/charter.md` say
  what the code does: a template whose marker major is below `TEMPLATE_MAJOR` gets the reseed note and
  may carry a legacy fence; one at or above it may not carry a legacy fence and gets no note, a minor
  behind included. This supersedes unit 1 §4 Migration's sentence that a template older than v4.5 gets
  the `legacy` note. Observed by AC4.
- **S4** — The render probe, armed. `render_playbook.py --selftest` gains an arm that, after the
  descriptor's block rows are read, renders gov's own template and a seeded copy of the previous minor
  template (v4.4, its literal section-1 lines and both `cross-os` fences) against a scratch target,
  each with and without `drop_blocks = ["cross-os"]`, and asserts each render exits 0. Observed by AC5.

## 3. Non-goals (OUT)

- The practice catalogue, its reader and the `{{PRACTICES}}` line: unit 1's.
- Retiring `practice.cross-os` into the portable practice: `PLAY-dOrderedCharter-30`, whose §3 already
  keeps the `when:cross-os` fence and its row for the Toolchain section.
- The v5.0 marker and any `TEMPLATE_MAJOR` move: `PLAY-dOrderedCharter-2`'s; its constant pair is a
  minor of the same review, batched in `PLAY-dOrderedCharter-49`.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-1` — the catalogue, `resolve_active_practices` and S6's mapping of a dropped block onto the active set, which S2 keeps and S1 takes off the legacy path
- **hands-off** `PLAY-dOrderedCharter-55` — round-2 ids 3, 9 and 17: unit 1 lands no `legacy` key, AC4 asserted on the line, and the selftest guard widened to the arm's inputs

## 4. Design

### Evidence

Read at `ce13efbe`. `TEMPLATE_MAJOR = 4` (`tools/playbook/render_playbook.py:343`); `current` is
`int(marker.group(1)) >= TEMPLATE_MAJOR` (`:1004`); the legacy set is the descriptor's rows carrying
`legacy` (`:1008`); a current template carrying a legacy block's fence raises `Refusal`
(`:1009-1012`); a legacy `drop_blocks` member whose fence is absent is noted as `retired` (`:1015`,
the note at `:1025`); the reseed note fires only on `marker and not current` (`:1026-1029`). The template carries `<!-- governance-template: v4.4 -->` at line 9 and `when:cross-os`
fences at lines 42-44 and 198-200. The block row is at `tools/govkit/entries/playbook.kit.toml:285-287`
with no `legacy` key today. Gov's `.governance/deploy.toml` sets no `drop_blocks`, and says why in its
comment.

### Flow

`render()` keeps its order. Unit 1's catalogue step resolves the active set; S2's step, beside it,
removes `practice.cross-os` when `drop_blocks` names `cross-os` and appends the note. The existing
`drop_names` loop and drop set (`:1017-1023`) drop the fence as they always did, because `cross-os` is declared and
not legacy.

### Inventory

Minted: the note prefix `practices drop_blocks` and the selftest arm's label. No identifier.

### Files touched (estimate)

- `tools/govkit/entries/playbook.kit.toml`
- `tools/playbook/render_playbook.py`
- `help/charter.md`

### Rollout

Live at landing, order 18, after unit 1 at order 17, beside unit 3, which shares order 18 and also
writes `tools/playbook/render_playbook.py`, so the dispatch's write sets intersect and the two are
sequenced rather than run together (M6), and before unit 2 at order 20, which moves the marker to v5.0.

### Alternatives rejected

- **Bumping `TEMPLATE_MAJOR` and the marker to v5.0 in this unit and moving the Toolchain fence**, the
  review's second fix. Unit 2 owns the v5.0 move; doing it here moves every v4.x adopter to the
  reseed path two units early and splits one major bump across two units.
- **Keeping `legacy` and exempting `cross-os` from the refusal.** A named exemption to a rule that
  exists to stop a retired block coming back.

## 5. Production-readiness checklist

- security: no new surface.
- perf / scale: none; one set difference per render.
- error / empty / loading states: unchanged; a `drop_blocks` member naming an undeclared block is
  still refused (`:988-992`).
- observability: S2's note names both the dropped block and the practice.
- risks: an adopter reading unit 1's earlier `retired` wording is told to keep the member, which still
  drops the Toolchain section.
- testing: AC1 to AC5; S4 is a selftest arm (§7).
- migration: none for adopters; a v4.4 template renders as it did.
- user docs: `help/charter.md` (S3).

## 6. Acceptance criteria

- **AC1** — When `python -c "import sys, tomllib; print([b for b in tomllib.load(open(sys.argv[1],'rb'))['block'] if b['name']=='cross-os'])" tools/govkit/entries/playbook.kit.toml`
  runs at the unit's commit, the one row printed has no `legacy` key.
  Red when: the row carries `legacy`.
- **AC2** — When `python tools/playbook/render_playbook.py --target . --check` runs on gov, it exits 0.
  Red when: the render refuses naming `when:cross-os`, as it does with the row marked legacy.
- **AC3** — When the render runs against a scratch target with `drop_blocks = ["cross-os"]` and gov's
  template, the output carries no Toolchain section and no `[cross-os]` line, and prints the
  `practices drop_blocks cross-os` note; without the member it carries both.
  Red when: the member drops only one of the two, or prints the `retired` note.
- **AC4** — When `git grep -n -e "minor behind" -- tools/playbook/render_playbook.py help/`
  runs, `render_playbook.py` and the page `charter.md` each state the major-only rule.
  Red when: either still says a minor-older template gets the reseed note.
- **AC5** — When `python tools/playbook/render_playbook.py --selftest` runs, the S4 arm renders gov's
  template and the seeded v4.4 copy with and without the member and reports four exits of 0.
  Red when: a block row's state change makes either template refuse.

## 7. Gates

`playbook render selftest` · `playbook render wiring` · `playbook parity` · `govkit acceptance matrix` · `govkit selftest` · `govkit refusal join` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/render_playbook.py · covers AC5 · the selftest renders gov's template and a seeded v4.4 template after the block rows are read, its failing case staged by marking the `cross-os` row `legacy` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, as the tree's promoted specs do; (b) none; (c) a part of unit 1's
  clause. (b) reds unbound and (c) splits a clause this unit does not carry. RESOLVED (agent,
  2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — Keep the block live, or bump the major here.** Options: (a) keep `cross-os` live and keep
  S6's mapping; (b) bump `TEMPLATE_MAJOR` and the marker to v5.0 now and move the Toolchain fence; (c)
  keep `legacy` with an exemption. (b) takes unit 2's major bump two units early and (c) adds an
  exemption to a refusal. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3, the option that keeps
  every v4 template rendering with no new surface. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's finding 30 (HIGH, item H3).
- rev-2 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-2 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-55.

## 10. Reuse audit

The seam is `render()`'s block handling in `tools/playbook/render_playbook.py:979-1051`, the legacy set
and refusal at `:1008-1012` and the `drop_names` loop and drop set at `:1017-1023`, which this unit leaves as it is
and keeps `cross-os` outside of. The recall query returned `TOOL-dRedressedBar-20` §4, which describes
the same three rules at an earlier line set (`:1000-1001`, `:1006-1009`, `:1023-1026`) and agrees with
source on their meaning. `python tools/codebase-map/reuse_lookup.py "render a template whose when
fence names a block a deploy file drops"` ranked `render` (SEAM) first, which is the function above.

Recall terms used: `python tools/memory-recall/query.py "why does a legacy block fence refuse a current major template" --terms "legacy block when fence TEMPLATE_MAJOR marker reseed drop_blocks cross-os refusal current major"`
