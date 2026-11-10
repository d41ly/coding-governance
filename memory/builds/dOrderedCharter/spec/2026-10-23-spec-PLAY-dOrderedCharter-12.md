# PLAY-dOrderedCharter-12 — the statement grammar, its check, and render provenance in a sidecar lock

**Status:** CLOSED · rev-5 · 2026-11-04 · node d · Tier-2 · base ce13efbe · streams playbook · order 13 · advances PLAY-dOrderedCharter-38

**Carries:** cl-dClosedLoop-0042@9958d12b whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return-2.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return-2.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-a.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-a.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-27 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-24-build-PLAY-dOrderedCharter-12-deviation-121.md](../build/2026-10-24-build-PLAY-dOrderedCharter-12-deviation-121.md) | deviation | — |
| [2026-10-24-build-PLAY-dOrderedCharter-12-deviation-122.md](../build/2026-10-24-build-PLAY-dOrderedCharter-12-deviation-122.md) | deviation | — |
| [2026-10-24-build-PLAY-dOrderedCharter-12-deviation-123.md](../build/2026-10-24-build-PLAY-dOrderedCharter-12-deviation-123.md) | deviation | — |
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-73 PLAY-dOrderedCharter-74 PLAY-dOrderedCharter-75 PLAY-dOrderedCharter-76 PLAY-dOrderedCharter-77 |
| [2026-11-02-build-PLAY-dOrderedCharter-12-ledger.md](../build/2026-11-02-build-PLAY-dOrderedCharter-12-ledger.md) | journal | — |
| [2026-11-04-build-PLAY-dOrderedCharter-12-1-builder-return.md](../build/2026-11-04-build-PLAY-dOrderedCharter-12-1-builder-return.md) | journal | — |
| [2026-11-10-build-PLAY-dOrderedCharter-1-runlog-8d3cc031.md](../build/2026-11-10-build-PLAY-dOrderedCharter-1-runlog-8d3cc031.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-73 PLAY-dOrderedCharter-74 PLAY-dOrderedCharter-75 PLAY-dOrderedCharter-76 PLAY-dOrderedCharter-77 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-edge-fix-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-edge-fix-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-11-02-prompt-PLAY-dOrderedCharter-12-build-brief.md](../prompts/2026-11-02-prompt-PLAY-dOrderedCharter-12-build-brief.md) | journal | — |
| [2026-11-03-prompt-PLAY-dOrderedCharter-19-latent-hits-brief.md](../prompts/2026-11-03-prompt-PLAY-dOrderedCharter-19-latent-hits-brief.md) | research | PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-55 |
| [2026-11-03-prompt-PLAY-dOrderedCharter-53-drift-sweep-brief.md](../prompts/2026-11-03-prompt-PLAY-dOrderedCharter-53-drift-sweep-brief.md) | research | PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-42 |
| [2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md](../reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md) | spec-audit | PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-37 |
| [2026-11-05-review-PLAY-dOrderedCharter-1-closing-diff-review-round1.md](../reviews/2026-11-05-review-PLAY-dOrderedCharter-1-closing-diff-review-round1.md) | diff-review | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 |

<!-- /gen:spec-records -->

## 1. Goal

Loaded text is unshaped (gap-found-11): nothing checks that a loaded line gives direction, the charter's
headings name a number, it points at "the marker below", which an agent reading the rendered text never sees
as an instruction, its render provenance loads in every session, and a typed fact goes stale where it loads
("Worktrees: none yet" beside thirteen worktrees). P11 says every loaded unit is one of six statement types
and render provenance never loads. This unit lands the closed set of types (S9), the check that grades a
unit's text against its type and a rendered document against the four shapes R-D names, and the sidecar lock
`.governance/instructions.lock` that carries render provenance instead of the loaded text.

## 2. Scope (IN)

- **S1** — The closed set. `STATEMENT_TYPES = ("directive", "constraint", "definition", "pointer",
  "policy-value", "fact")` and `MODALS = ("MUST", "NEVER", "ALWAYS")` in
  `tools/playbook/instruction_units.py`; no other file types either list. Observed by AC1.
- **S2** — The unit check. `check_statement(row) -> list[str]` grades one unit row, in S10's field names,
  against its `type`, as R-D and the systems record's "Per type" bullet state:
  - a `directive`'s text opens with a modal of `MODALS`, its condition in `trigger`;
  - a `constraint` carries a value in its text and names its enforcer in `enforced-by`;
  - a `definition`'s text holds a term and its meaning, `<term> — <meaning>`;
  - a `pointer`'s text names a trigger and a target, a tag the resolver resolves to a unit or slice, or a
    command, never a whole document;
  - a `policy-value` carries `source = "policy:<key>"` and no typed text;
  - a `fact` carries a `source` and no typed text, so "Worktrees: none yet" typed as a fact is red;
  - a `type` outside `STATEMENT_TYPES` is red, naming the six.
  Each red names the unit's tag, the rule and the remedy. Observed by AC2.
- **S3** — The document check. `check_document(text) -> list[str]` grades a rendered document's lines for
  the four shapes R-D lists, each seen red on today's charter:
  - a provenance paragraph, one holding `Rendered from`, `re-render` or `never edit the rendered`, read
    case-insensitively, and the template version marker `<!-- governance-template: v<n>.<n> -->`;
  - a numbered heading, `^#{1,6} +\d+[.)]? `;
  - a pointer to text never loaded, one of the closed phrases `the marker below`, `the marker above`,
    `the comment below` and `the comment above`;
  - a typed fact, a bold-key bullet under a heading named `Facts` that no `fact` unit with a `source`
    produced, as the lock row's `units` attributes lines (S4).
  `python tools/playbook/instruction_units.py grammar --doc <path>` runs it on demand. Observed by AC3.
- **S4** — The lock. `.governance/instructions.lock` holds one `[[target]]` row per rendered target:
  `path`, `blob` (the git blob id of the rendered bytes), `units` (each `<tag>@<hash8>`, the hash unit
  24's `derive_pin_hash` (`tools/memory-tree/design_lib.py:173`) gives the unit's text, empty for a
  document no unit renders yet), `renderer`
  (`<kit id>@<kit version>`) and `template` (the source template's path and its version marker, `v4.4`
  today). `write_lock_row` and `read_lock` in `instruction_units.py` are its one writer and one reader.
  Observed by AC4.
- **S5** — Provenance out of the charter. `render()` in `tools/playbook/render_playbook.py` writes the
  charter's lock row on every render and no longer copies the version marker into the rendered text; the
  source template keeps its marker, which `check-placeholders.sh`, `check-playbook-parity.sh` and the
  `playbook` entry's `version_from` read from the source. The rendered marker is retired.
  **Readers:**
  by name: `skills/session-kickoff/SKILL.md` (its Step 2 fallback greps a governance doc for
  `governance-template:`) and `WIRE-INTO-PROJECT.md` (its marker paragraphs), each re-pointed to the
  lock's charter row;
  by value: `skills/session-kickoff/SKILL.md`, whose fallback reads the marker's presence as "an
  instantiated governance doc" and now reads a lock row whose `template` is set.
  Observed by AC5.
- **S6** — The lock check. `python tools/playbook/instruction_units.py lock --check` reds a row whose path
  is not tracked, whose `blob` differs from the working tree's bytes, or whose fields break S4, and a
  rendered charter carrying a version marker. Observed by AC4 and AC5.
- **S7** — The leg and plants. One leg `instruction grammar (statement types, provenance lock)` in
  `tools/gate-legs.json`, with `"subject": "repo"` and `"chunk": "product"` as `line length` carries for
  a check of shipped text, carrying `"enforces": ["principle.p11"]`, runs `grammar`, which grades every unit
  row through unit 9's reader and every lock row whose `units` is non-empty through S3, and `lock --check`;
  until unit 9's reader lands in the module, the unit half prints `unarmed: no unit reader
  (PLAY-dOrderedCharter-9)`, never green. `python tools/playbook/instruction_units.py fixture --plant
  <case>` runs each case in a throwaway tree in the system temp directory. Observed by AC1 to AC5.
- **S8** — The leg's own rows, written in this pass. The claiming row is an `[[exempt_leg]]` row in
  `tools/govkit/registry.toml` naming the leg, with a `why` in the shape of unit 19's at `:711` (§8 F4);
  `python tools/govkit/govkit.py selfcheck --write` adds its `tools/govkit/subject-pins.tsv` row; the
  `gate-legs` claim of `memory/map/features/playbook.md` gains the leg; and `python
  tools/codebase-map/gen_map.py --write` rewrites `memory/map/generated/`. The commit hook refuses an
  unclaimed leg once a `.py` path is staged (`.githooks/pre-commit:280-292`). Observed by AC6.

## 3. Non-goals (OUT)

- Rewriting the charter's provenance paragraph, its numbered headings and its Facts section: unit 2
  re-founds the charter, and the document check grades it once units render it.
- The unit row schema (I1) and the one-fact check (I4): unit 20. The row reader: unit 9.
- Positional references (`§n`, `Mn`): unit 19 and unit 26.
- Lock rows for the roles, guide and agent-instructions renders: unit 20's one renderer writes them once it
  absorbs those renderers.
- The region markers `<!-- gov:playbook -->` and `<!-- one-line -->`: render plumbing, not provenance;
  the envelope (unit 3) is what identifies a document.
- Handed content in work orders, which is data and never graded (dBoundRoles' render).

### Edges

- **consumes-from** `PLAY-dOrderedCharter-13` — the module `tools/playbook/instruction_units.py` S1 adds to
- **consumes-from** `PLAY-dOrderedCharter-24` — its S7's shared normaliser `derive_pin_hash`, the `<hash8>` of each `units` entry
- **consumes-from** `PLAY-dOrderedCharter-19` — the resolver a pointer's target resolves through
- **consumes-from** `PLAY-dOrderedCharter-7` — the `enforces` key S7's leg carries, and `principle` in the `enforces` row's `to` in `tools/playbook/edges.toml`, which unit 7's pass adds at order 11 (`:67` reads `["unit", "practice"]` at HEAD), so S7's `principle.p11` is a registered target
- **hands-off** `PLAY-dOrderedCharter-9` — the row reader the unit half of S7's leg grades through
- **hands-off** `PLAY-dOrderedCharter-20` — lock rows written by the one renderer for every target it absorbs, and the schema check beside S2
- **hands-off** `PLAY-dOrderedCharter-2` — the re-founded charter, which S3 grades once units render it
- **hands-off** `PLAY-dOrderedCharter-15` — the grammar check the write command's S6 runs before every write
- **hands-off** `PLAY-dOrderedCharter-49` — the round-1 spec audit's minors on this spec, findings 5, 27, 39, 67, 74 and 83, which that batch unit corrects after this unit lands, each by the item its report id names
- **consumes-from** `PLAY-dOrderedCharter-50` — the owed-rows probe: this pass runs `python tools/run-gates/owed_rows.py --base HEAD` before its commit and writes every row it names in that commit (round-2 id 23)
- **hands-off** `PLAY-dOrderedCharter-55` — AC1 and AC5, which unit 49 S60 and S71 correct, are observed at `PLAY-dOrderedCharter-49`'s pass and recorded from that observation; this pass changes no code to satisfy it (round-2 id 2)

## 4. Design

### Data model

```toml
# .governance/instructions.lock
[[target]]
path = "AGENTS.md"
blob = "<40-hex git blob id of the rendered bytes>"
units = []                                   # <tag>@<hash8> each, once units render it
renderer = "playbook-render@1.33"                 # KIT_PLAYBOOK_RENDER_VERSION at render time
template = "coding-governance-agents.template.md@v4.4"
```

The lock is written whole and sorted by `path`, so two renders of one tree write identical bytes. `blob`
is `git hash-object` of the bytes the renderer wrote. `renderer`'s version is read from
`KIT_PLAYBOOK_RENDER_VERSION` (`tools/playbook/render_playbook.py:1887`), never typed.

### Inventory

Minted: `STATEMENT_TYPES`, `MODALS`, `check_statement`, `check_document`, `write_lock_row`, `read_lock`,
the verbs `grammar` (with `--doc`) and `lock --check`, the file `.governance/instructions.lock`, and the leg
`instruction grammar (statement types, provenance lock)` and its rows (S8).

### Migration

The first render after this unit writes the lock and drops the marker line from `AGENTS.md`; both commit
with the code.

### Rollout

Live at landing, at order 13: after unit 13 (order 12) creates the module and unit 24 (order 7) the
normaliser, and before unit 9 (order 14), whose reader arms the unit half of S7.

### Files touched (estimate)

- `tools/playbook/instruction_units.py`
- `tools/playbook/render_playbook.py`
- `.governance/instructions.lock`
- `AGENTS.md`
- `skills/session-kickoff/SKILL.md`
- `WIRE-INTO-PROJECT.md`
- `tools/gate-legs.json`
- `tools/govkit/registry.toml`, the leg's `[[exempt_leg]]` row
- `tools/govkit/subject-pins.tsv`, regenerated by `govkit.py selfcheck --write`
- `memory/map/features/playbook.md`, the leg's claim
- `memory/map/generated/`, the files `python tools/codebase-map/gen_map.py --write` rewrites

### Alternatives rejected

- **Provenance kept in the rendered text as a comment.** An HTML comment loads with the file; R-D puts it
  in a sidecar.
- **The install receipt's `rendered` rows as the lock.** The receipt records an install and lives only in
  adopters; the lock records every render, gov's own included.
- **Grading every document now, today's charter included.** The leg would land red until unit 2; a legacy
  document is graded on demand, by `--doc`, until units render it.

## 5. Production-readiness checklist

- security: the lock holds paths, blob ids and versions, no secret; the writer writes only
  `.governance/instructions.lock`.
- perf / scale: one `git hash-object` per rendered target; the checks are per-line regexes.
- error / empty / loading states: an absent lock after a render is red; the unit half reads `unarmed`
  until unit 9 lands, never green.
- observability: each red names the tag or the path and line, the shape and the remedy.
- risks: an adopter's kickoff that greps the rendered marker misses it after update; S5 re-points the
  engine's own fallback and the runbook in the same unit.
- testing: S7's plants both ways; `grammar --doc AGENTS.md` on today's charter.
- migration: §4 Migration.
- user docs: `WIRE-INTO-PROJECT.md`'s marker paragraphs name the lock (S5).

## 6. Acceptance criteria

- **AC1** — When `git grep -n -E "\"policy-value\"" -- tools` runs, it prints one definition, in
  `instruction_units.py`'s `STATEMENT_TYPES`.
  Red when: a second module types the set.
- **AC2** — When `python instruction_units.py fixture --plant statements` runs, a directive
  with no modal, a constraint with no `enforced-by`, a `fact` row with `text = "Worktrees: none yet"` and no
  `source`, a pointer to `doc.nosuch`, a `policy-value` with typed text and a row typed `prose` each red
  `check_statement`, and one well-formed row of each type passes.
  Red when: a malformed unit passes, or a well-formed one reds.
- **AC3** — When `python instruction_units.py grammar --doc AGENTS.md` runs on today's
  charter, it exits 1 naming the provenance paragraph at lines 4 to 8, the heading `## 1. Governing
  practices`, the phrase `the marker below` and the `**Worktrees:**` fact; on the fixture's re-founded
  charter, carrying none of the four, it exits 0.
  figure: the line numbers are PINNED to `AGENTS.md` at `4e8f80cdf`.
  Red when: any of the four shapes passes on today's charter.
- **AC4** — When `python instruction_units.py fixture --plant lock` renders a fixture charter
  twice, the lock's bytes are identical both times, its row's `blob` equals `git hash-object` of the
  rendered file, and a hand edit of the rendered file reds `lock --check` naming the path.
  Red when: the lock drifts between renders or misses an edited target.
- **AC5** — When a probe renders the charter into a scratch clone of this repository with `python
  tools/playbook/render_playbook.py --target <clone>`, `git -C <clone> grep -n "governance-template:" --
  AGENTS.md` prints nothing and the clone's `.governance/instructions.lock` charter row, read through
  `read_lock`, holds `template = "coding-governance-agents.template.md@v4.4"`; and after the pass `git
  grep -n "instructions.lock" -- skills/session-kickoff/SKILL.md WIRE-INTO-PROJECT.md` prints the
  re-pointed lines.
  Red when: provenance loads with the charter, or a reader still looks for the rendered marker.
- **AC6** — When `git grep -n -F 'name = "instruction grammar (statement types, provenance lock)"' --
  tools/govkit/registry.toml` runs after the pass, it prints one line under an `[[exempt_leg]]`
  header; `git grep -n -F "instruction grammar (statement types, provenance lock)" --
  tools/govkit/subject-pins.tsv memory/map/generated/MAP.md` prints the pins row and the map's row,
  `playbook` its claimant; and `git grep -n -F '"instruction grammar (statement types, provenance
  lock)"' -- memory/map/features/playbook.md` prints one line, the dossier's `gate-legs = [` claim.
  Red when: the leg lands without its claiming row, its pins row, its dossier claim, or the rewritten map.

## 7. Gates

`playbook render selftest` · `govkit acceptance matrix` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `playbook render wiring` · `playbook parity` · `spec tokens (a spec's own names resolve)` · `policy fixtures` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join`

New arm: tools/playbook/instruction_units.py · covers AC2 AC3 AC4 · the leg's `fixture --plant` cases, each failing case staged by its plant · none

New arm: tools/playbook/render_playbook.py · covers AC5 · the render selftest asserts the rendered charter carries no version marker and the lock row carries it, its failing case a renderer copying the marker · none

## 8. Open questions

- **F1** — The brief's S9 spells the lock row as path, blob, unit tag@hash and renderer version. The
  template's version marker is render provenance too, and S5 moves it out of the loaded text, so it needs a
  field. Options: add `template`; fold it into `renderer`; leave the marker in the loaded text.
  RESOLVED (agent, 2026-10-23, delegated): rung 3, the most feature-rich survivor: add `template` (S4).
  Leaving the marker fails P11's "render provenance never loads"; folding two facts into one field breaks
  `renderer`'s one meaning. Units 3 and 20 read the row through `read_lock` and never parse a field.
- **F2** — Does the grammar's leg grade today's hand-written charter? Options: grade it now; grade units
  and unit-rendered documents only, and grade a legacy document on demand.
  RESOLVED (agent, 2026-10-23, delegated): rung 3: the second (S3, S7). The first lands the leg red until
  unit 2 re-founds the charter; the clause's red cases are still observed on today's charter, by AC3.
- **F3** — The rendered marker is read by the kickoff engine's fallback and named by the deployer runbook.
  Options: re-point both in this unit; keep the marker in the render.
  RESOLVED (agent, 2026-10-23, delegated): rung 3: re-point both (S5). grants: PLAY-dClosedLoop-3 the kickoff Skill and the deployer runbook read the provenance lock where they read the rendered marker.
- **F4** — Which row claims S7's leg? Options: (a) an `[[exempt_leg]]` row in `tools/govkit/registry.toml`,
  as units 16, 19 and 28 wrote at `:707`, `:711` and `:715`; (b) a `[[gate_leg]]` row in
  `tools/playbook/kit.toml`, as `playbook render wiring` carries at `:69-72`, since S5's render writes a
  lock row in an adopter too.
  RESOLVED (agent, 2026-11-03, delegated): rung 3: (a). (b) lost on its observation: the leg's `grammar`
  half grades unit rows through unit 9's reader, and the unit rows and their reader are authored in gov,
  so an adopter carrying the leg holds an empty population for that half, which [gate] refuses as
  coverage; and the registry records beside `run-gates.gov.test.sh` that a descriptor row naming a leg the
  target cannot carry reds the deployer. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the spec run's carrier of `cl-dClosedLoop-0042`.
- rev-2 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-1 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-49.
- rev-3 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-2 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-50, PLAY-dOrderedCharter-55.
- rev-4 · 2026-11-03 · §7 · from `2026-11-03-prompt-PLAY-dOrderedCharter-19-latent-hits-brief.md` Item 2: the leg line names `policy fixtures`, whose guard a §4 Files touched path trips, the guards hit the spec-token check reads with DEFERRED as live.
- rev-5 · 2026-11-03 · S4 S7 S8 · §3 · §4 · AC5 AC6 · §7 · §8 F4 · §10 · from `2026-11-03-prompt-PLAY-dOrderedCharter-53-drift-fold-brief.md` (12-1 to 12-6): §10's anchors re-read at HEAD; the example renderer reads 1.33 from `KIT_PLAYBOOK_RENDER_VERSION`; new S8 and AC6 write the leg's exempt, pins, dossier and map rows (F4), and §7 names the legs they trip; the Edges line to unit 7 consumes `principle` in `enforces`' `to`; S4 names `derive_pin_hash`; AC5 renders into a scratch clone, not the wiring leg's check.

## 10. Reuse audit

The seams extended are `render()` in `tools/playbook/render_playbook.py` (line 1024), whose
`TEMPLATE_MARKER_RE` (line 344) already reads the marker S5 moves into the lock, and the closed-grammar
precedents R-D names: `tools/check-microformats.sh`, which grades a fenced definition list against its own
grammar, `check_one_line_regions(text, cap=None) -> list` (`render_playbook.py:698`), and
`tools/check-playbook-parity.sh`'s S4 arm (line 438), which refuses a charter section cited by number. Each grades a different subject, so S2 and S3
are new predicates beside them, not copies. `python tools/codebase-map/reuse_lookup.py "refuse a loaded line
that is not a directive constraint definition pointer policy value or sourced fact"` ranked name-token
matches (`note`, `load`, `fact` in `tools/unattended/unattended.sh`), none a statement grammar, so no existing
seam fits the type check. The install receipt's `rendered` rows were read as the lock's precedent and
rejected (§4).

Recall terms used: `python tools/memory-recall/query.py "how is render provenance kept out of loaded charter text and which statement types may a loaded unit take" --terms "statement grammar directive constraint definition pointer policy-value fact provenance sidecar lock marker R-D"`
