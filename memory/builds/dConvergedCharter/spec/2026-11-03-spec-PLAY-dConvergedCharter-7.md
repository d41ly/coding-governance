# PLAY-dConvergedCharter-7 — protocols and templates as tag-sliced views, the guides retired, their rationale in units' `help` and the `help/why/` tree under `help.explanation`

**Status:** OPEN · rev-2 · 2026-11-04 · node d · Tier-2 · base 0d1c1dda · streams playbook · order 17 · advances PLAY-dConvergedCharter-24

**Carries:** cl-dClosedLoop-0481@a6574329 whole
**Carries:** node:policy-key.help.explanation

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md](../build/2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-03-build-PLAY-dConvergedCharter-6-reuse-scout-b.md](../build/2026-11-03-build-PLAY-dConvergedCharter-6-reuse-scout-b.md) | research | PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-15 |
| [2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md](../build/2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md) | journal | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-39 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-fix-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-fix-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-21 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md](../reviews/2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md) | spec-audit | PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-18 |

<!-- /gen:spec-records -->

## 1. Goal

The guides under `memory/guides/` and the two templates `memory/HYGIENE.md` and `memory/TEMPLATE-SPEC.md`
are 409 KB of hand-written prose that restate the flow's steps (gap-found-12), and once they go nothing
explains the product to a human (gap-found-36). This unit makes an agent's protocol a tag slice over the
loop's checklists, the roles, the record schemas and the policies, renders the two templates from units
and the record schema, and retires the hand-written guides. Each guide section's rationale moves into a
unit's `help` field, never into `help/`'s feature pages, and renders into its own tree under `help/` as
`help.explanation` says. No agent loads that tree. A guide whose section maps to no unit's rationale
cannot be retired, which the arm of S6 proves on a planted retirement (the owner's FQ-6).

## 2. Scope (IN)

- **S1** — The policy key's row. `help.explanation` keeps its catalogue row at
  `tools/policy/catalogue.toml:998-1001` (allowed `rendered` and `registry-only`, default `rendered`,
  owner dConvergedCharter), and gains `summary` and `usage = 'help.explanation = "registry-only"'`. Then
  `python tools/policy/policy.py lists --write` drains its name from
  `tools/policy/unsummarised-keys.txt:72`. No second row is added. Observed by AC1.
- **S2** — The literal reader. `tools/playbook/render_playbook.py` reads the key once per run by the
  literal call `read_policy_value("help.explanation", root)`, through the playbook kit's reader in
  `tools/playbook/policy_value.py` (PLAY-dOrderedCharter-19 S8, the kit's first key read), `root` the
  tree under render. A refused read, or a value outside the two, reds the scope naming the key and the
  value. This call is the reader the policy kit's reader-coverage arm counts
  (`check_reader_coverage`, `tools/policy/check_policy.py:520`, `READER_SHAPES` at `:425`). Observed by
  AC2 and AC4.
- **S3** — The `explanation` scope (I18, I21). `python tools/playbook/render_playbook.py --render-scope
  explanation` renders, under `rendered`, `help/why/README.md` and one page `help/why/<kit>.md` per kit
  manifest holding at least one unit with a `help` field. `render_explanation(units)` is pure: it takes
  `read_units(root)` (PLAY-dOrderedCharter-9 S2) and writes one `## <unit tag>` section per unit in read
  order, its `help` text, then one `Explains: <address>` line per `explains=` edge it declares. The index
  lists each page once. Under `registry-only` the scope writes nothing and leaves no file under
  `help/why/`. `--check-render --scope explanation` compares the bytes, and under `registry-only` reds any
  file left under `help/why/`. One `[[target]]` row in `tools/playbook/renderers.toml` claims the tree,
  `paths = ["help/why/*.md"]`, `renderer = "playbook:explanation"`. Observed by AC2, AC3 and AC4.
- **S4** — Apart from every agent load. `help/why/` is outside `help/reference/`
  (PLAY-dOrderedCharter-37 S3), holds no `[[document]]` row of `tools/playbook/documents.toml`
  (PLAY-dOrderedCharter-3 S1), and is no member of any load set `derive_load_set` derives
  (PLAY-dOrderedCharter-11 S1). So `rationale-apart` (PLAY-dOrderedCharter-29 S6) stays green with the
  tree rendered. A page carries no `<!-- usage: … -->` anchor, so the docs leg walks it
  (`tools/govkit/docs_leg.py:413`) for links only. Observed by AC5.
- **S5** — The `explains` edge type. One `[[edge]]` row in `tools/playbook/edges.toml`
  (PLAY-dOrderedCharter-24 S1): `type = "explains"`, `inverse = "explained-by"`, `from = ["unit"]`,
  `to = ["doc"]`, `pin = "none"`, `status = "declared"`. A unit row writes it in its `edges` list as
  `explains=doc.<name>#<seg>`, the section address of PLAY-dOrderedCharter-19 S3. The closed set and the
  target-resolves check are dOrderedCharter's, so §8 F2 files the ask they owe. Observed by AC6.
- **S6** — The no-lost-rationale arm, `check_rationale_kept(root)`, run by
  `--check-render --scope explanation` under either value. Its population is
  `derive_retired_sections(root)`: every `<memory_root>/guides/*.md` that a first-parent commit of
  `HEAD` takes out of the tree, plus one absent from the index or the working tree, each read at that
  commit's parent. The walk carries NO pathspec, `git log --first-parent --diff-merges=first-parent
  --diff-filter=D -M --name-status`, and keeps the `D` entries under `<memory_root>/guides/` after it
  reads them: with a pathspec git cannot pair a rename whose destination lies outside it and reports
  the move as `D`, measured on a scratch repository by finding 27 of
  `2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1`. A file renamed out of `memory/guides/`, as S8
  moves `SESSION-KICKOFF.md`, keeps its sections at its new path, so rename detection stays on and only
  a `D` entry joins the population. Its sections are cut by unit 19's `extract_section` rule (I12), each
  giving one address `doc.<name>#<seg>`. The arm reds each address no unit row's `explains=` edge
  targets, naming the guide, the section heading and the address. A guide still present is not graded. An empty population prints `rationale kept: graded 0 guide(s) taken out`, never a
  bare green. Observed by AC7 and AC8.
- **S7** — The rationale moved. Every `##` section of each guide this unit takes out has its rationale
  written as a unit's `help` field with an `explains=` edge to its address; unit 12 writes the edges of
  the four UNATTENDED guides it takes out, and S6 grades all of them. Each move runs through unit 13's
  guide caller, `python tools/playbook/guide_move.py plan --rationale` then `apply` (unit 13 S3,
  over the factory `tools/lib/prose_move.py`'s `derive_moves` and `write_moves`, I16), a second route
  this unit adds beside unit 13's feature route: one move per `##` section of a guide this unit takes
  out, its destination the `help` field of a unit in the kit manifest §4 "The guides" names and its
  edge `explains=doc.<name>#<seg>` in place of the feature route's `promoted-from=`. A section whose
  directive text is already a unit (unit 1) gains the `help` and the edge on that unit. Each row is
  written by `apply`'s own write route (unit 13 S4, its §8 F2): the pass's kit edit, its change record
  through `python tools/memory-tree/build_records.py new change`, and the whole plan refused, writing
  nothing, unless `instructions_edit.py check` passes over the would-be tree. No row goes through
  `instructions.edit`'s door, which under its default `owner-command-agents-propose`
  (`tools/policy/catalogue.toml:647-649`) prints a proposal for an agent and writes nothing, so the
  guides would leave with their rationale unwritten. Observed by AC8, AC9 and AC12.
- **S8** — The guides retired. Once S7 holds, this unit removes `memory/guides/ANNOTATION-STYLE.md`,
  `memory/guides/BUILD-METHOD.md`, `memory/guides/MERGE-BAR.md`, `memory/guides/REVIEW-PROTOCOL.md` and
  `memory/guides/PLAYBOOK-TEMPLATE.md`, the last a render whose `[[files]]` and `[[lf_pin]]` rows unit 12
  moved to the runtime descriptor with `check-playbook.sh` and its template; this unit removes those two
  rows with the render, and the template stays as the checker's input,
  and moves the kickoff manifest `memory/guides/SESSION-KICKOFF.md` to `memory/project/SESSION-KICKOFF.md`,
  its `manifest_path` (`.governance/deploy.toml:54`) and readers re-pointed (§8 F5). It removes the kit
  sources `tools/memory-tree/ANNOTATION-STYLE.template.md`,
  `tools/memory-tree/BUILD-METHOD.template.md` and `tools/workflows/REVIEW-PROTOCOL.template.md`. Their
  pairs leave `PAIRS` in `tools/memory-tree/kit-dogfood-parity.test.sh:61` and
  `tools/workflows/check-protocol-parity.test.sh:94`, and their rows leave
  `tools/playbook/instructions-legacy.txt`. Each reader below is re-pointed to the tag slice of S9 or to
  `help/why/`. Observed by AC7, AC9 and AC10.
  **Readers:** by name: `coding-governance-agents.template.md` (rendered to `AGENTS.md`), the nine role
  sources under `tools/roles/agents/` (rendered to `.claude/agents/*.md`), `tools/roles/SKILL.template.md`,
  `skills/session-kickoff/SKILL.md`, `README.md`, `WIRE-INTO-PROJECT.md`, `help/spec-audit.md`,
  `.governance/deploy.toml:68`, `.memory-tree.conf:531`, `tools/memory-tree/kit.toml`,
  `tools/memory-tree/adopt-memory-tree.sh`, `tools/memory-tree/README.md`,
  `tools/memory-tree/HYGIENE.template.md`, `tools/memory-tree/check-memory-hygiene.test.sh`,
  `tools/memory-tree/check-method-carriers.test.sh`, `tools/workflows/kit.toml`,
  `tools/workflows/README.md`, `tools/workflows/unattended-build.template.js`,
  `tools/hooks/agent-cap.js:431`, `tools/drift-audit/drift_signals.py:44`, `tools/lib/render-doc.sh`,
  `tools/govkit/selftest.py:9758`, `tools/run-gates/run-gates.gov.test.sh`, `tools/check-template-size.test.sh`,
  and for the manifest `.governance/install.json`, `skills/session-kickoff/manifest-check.sh`,
  `tools/drift-audit/drift_signals.py:35`, `tools/policy/check_policy.py:3175` and
  `tools/govkit/fixtures/release-0/deploy.toml`;
  the rows of `tools/gate-legs.json` are rendered from the kits' `[[gate_leg]]` rows, the edit ·
  by value: `tools/template-size-limits.txt:129` and `tools/template-size-highwater.txt`, which cap
  `BUILD-METHOD.md`'s bytes; `tools/policy/caps.toml:63-67`, the same cap's policy row;
  `memory/project/method-carriers.txt`, which `tools/memory-tree/check-method-carriers.sh` compares with
  every file pointing at `BUILD-METHOD.md`; `tools/policy/check_policy.py:3492` and `:3761`, whose
  template-size plants name `BUILD-METHOD.md`. The build re-derives both halves by `git grep` at its
  first pass, by path and by value.
- **S9** — The views. An agent's protocol is the tag slice `python tools/playbook/gov_tag.py bundle <tag>`
  (PLAY-dOrderedCharter-25 S1), whose rows gather the units and the four sources through their namespaces:
  `item` (the loop's checklists, TOOL-dDeclaredLoop-11 and -12), `role` (`tools/roles/workflows.toml`,
  `load_roles` at `tools/roles/roles_lib.py:355`), `record` (the record schemas, `record_kinds.py --template`,
  TOOL-dTotalRecall-1 S5) and `policy` (the catalogue). Each namespace is its build's row
  (PLAY-dOrderedCharter-10 S5). The charter's protocol lines (`coding-governance-agents.template.md`,
  "Protocols — read the one whose trigger holds") name the slice command for each trigger in place of the
  guide path, and the tag for each is read from the registries at the build pass (§4 "The guides").
  Observed by AC10.
- **S10** — The templates rendered. `memory/TEMPLATE-SPEC.md` and `memory/HYGIENE.md` become targets of
  unit 10's `protocols` scope, their sources `tools/memory-tree/SPEC-TEMPLATE.template.md` and
  `tools/memory-tree/HYGIENE.template.md` reduced to slot lines: `<!-- units: <selector> -->`
  (PLAY-dOrderedCharter-20 S7) and one new slot `<!-- record-template: <kind> -->`, which expands to the
  output of `record_kinds.py --template <kind>` (TOOL-dTotalRecall-1 S5, unit 6). TEMPLATE-SPEC's
  skeleton is `<!-- record-template: spec -->`. Each `[[target]]` row moves from `renderer = "render-doc"`
  (PLAY-dOrderedCharter-20 §4) to `renderer = "playbook:protocols"`, and both paths leave the legacy list.
  Their pairs leave `PAIRS` in `tools/memory-tree/kit-dogfood-parity.test.sh:61`, their `rendered` rows
  in `tools/memory-tree/kit.toml` (`:56-65`) regenerate through `--render-scope protocols`, and
  `tools/memory-tree/adopt-memory-tree.sh` renders them by calling the one renderer, through the
  playbook-render edge its `requires_if` already declares. Their rationale moves as S7's does, the edge
  targeting `doc.hygiene#<seg>` or `doc.template-spec#<seg>`. Observed by AC11.

## 3. Non-goals (OUT)

- The protocol slices of the guides' directive text and the `protocols` and `skills` scopes: unit 10's.
  This unit adds the `explanation` scope and two `protocols` targets on that scope.
- Protocol text derived to facts, each document in its envelope: unit 1's. This unit moves rationale,
  never directive text.
- The four UNATTENDED guides and their rationale edges: unit 12 takes them out with the unattended kit.
  S6 grades that removal with this unit's own. `SESSION-KICKOFF.md`'s ratchet and its gate: unit 16
  moves `manifest-check.sh`; this unit moves only the manifest file out of `memory/guides/`.
- Retiring the parity tests, `render-doc.sh` and the legs that run them: unit 8's, each with its last
  document. This unit takes its own documents' pairs out of `PAIRS`, and nothing more.
- The help pages, the kit READMEs and the runbook, and the link from `help/README.md` into `help/why/`:
  unit 15's.
- The feature pages under `help/`: rationale never goes there (the clause).
- Any edit to v2, a parent spec or another build's record: each needed change is an ask in §8.

### Edges

- **consumes-from** `PLAY-dConvergedCharter-12` — `explains=`, the edges from units' `help` to the four UNATTENDED guides' sections, which S6 grades with this unit's own
- **consumes-from** `PLAY-dConvergedCharter-6` — `record_kinds.py`, every record kind registered, so `record_kinds.py --template spec` renders S10's skeleton and the `record` namespace of S9 is whole
- **consumes-from** `PLAY-dConvergedCharter-19` — `extract_section`, the heading-to-section rule S6 cuts a retired guide by, so an address S6 derives equals the address a unit's edge spells
- **consumes-from** `PLAY-dConvergedCharter-13` — `guide_move.py`, the guide caller of the factory `prose_move.py` and its write route, to which S7 adds the `--rationale` route it moves each section's rationale through; without it the rationale would land through `dossier_move.py`'s proposal and record route, or a third mover
- **consumes-from** `PLAY-dConvergedCharter-1` — `instructions-legacy.txt`, drained of the guides' directive text, so S8 removes files whose directive units already exist
- **consumes-from** `PLAY-dConvergedCharter-10` — `renderers.toml`, with the `protocols` scope S10 targets and the scope grammar S3's `[[target]]` row follows
- **hands-off** `PLAY-dConvergedCharter-15` — `help/why/`, the tree and its index page `help/why/README.md`, which that unit links from `help/README.md` only while `help.explanation` reads `rendered`
- **hands-off** `PLAY-dConvergedCharter-8` — `help.explanation`'s `explanation` scope, and the guide and template documents moved off `render-doc` and out of both parity tests' `PAIRS`, so that unit retires `kit-dogfood-parity.test.sh`, the review-protocol document pair and `render-doc.sh` with their last documents
- **consumes-from** external — PLAY-dOrderedCharter-9, -11, -15, -19, -20, -24, -25, -29 and -37, TOOL-dDeclaredLoop-11 and -12, TOOL-dTotalRecall-1 and -10: each DEFERRED at base and built before this unit's build pass

## 4. Design

### Evidence

Read at `d8a12f046`; no product file differs from base `0d1c1dda`.

- `help.explanation`'s row at `tools/policy/catalogue.toml:998-1001` carries `allowed`, `default` and
  `owner` and no `summary` or `usage`; its name is `tools/policy/unsummarised-keys.txt:72`.
- The reader-coverage arm counts a call whose first argument is the key as a string literal
  (`READER_SHAPES` row 1, `tools/policy/check_policy.py:425-429`) in tracked code outside the memory root
  and `help/` (`scan_reader_keys`, `:481`). `govkit.read_policy_value` is at `tools/govkit/govkit.py:274`,
  and the docs leg reads `help.enforce` through it at `tools/govkit/docs_leg.py:727`.
- `memory/guides/` holds ten files at base, 317,842 bytes (PINNED, `cat memory/guides/*.md | wc -c` at
  `d8a12f046`), the figure unit 13 §4 sums with the two templates. Their carriers:
  `BUILD-METHOD.md` and `ANNOTATION-STYLE.md` under kit/dogfood parity
  (`tools/memory-tree/kit-dogfood-parity.test.sh:61`, beside `HYGIENE.md` and `TEMPLATE-SPEC.md`);
  `REVIEW-PROTOCOL.md` under the protocol pair (`tools/workflows/check-protocol-parity.test.sh:94`); the
  four UNATTENDED guides and `PLAYBOOK-TEMPLATE.md` copied by `tools/unattended/adopt-unattended.sh:761-787`;
  `SESSION-KICKOFF.md` and `MERGE-BAR.md` hand-written, with no kit header.
- `git log --diff-filter=D -- 'memory/guides/*'` prints nothing at `d8a12f046`, so S6's population is
  empty until this build removes a guide, and no historic removal can red it. S6 itself walks without
  the pathspec, so a move out of the guides path never reads as a removal.
- `scout B` row 7 and its interfaces hold against source at `d8a12f046`, line numbers included.

### The guides

| Guide | Removed by | Rationale rows land in |
|---|---|---|
| `ANNOTATION-STYLE.md`, `BUILD-METHOD.md` | this unit | `tools/memory-tree/instructions.toml` |
| `REVIEW-PROTOCOL.md` | this unit | `tools/workflows/instructions.toml` |
| `MERGE-BAR.md` | this unit | `tools/run-gates/instructions.toml` |
| `PLAYBOOK-TEMPLATE.md` | this unit | the loop kit's manifest (TOOL-dDeclaredLoop-11) |
| the four UNATTENDED guides | unit 12 | the loop or runtime kit's manifest, unit 12's S1 |
| `SESSION-KICKOFF.md` | moved by this unit, not graded | none: a manifest, not a guide in substance |

The slice tag for each protocol line of S9 is the stage or item tag its trigger names, read from the
loop and roles registries at the build pass: DERIVED, never typed here.

### The explanation page

```markdown
# Why — <kit>

## unit.reuse-first

A spec set that skips the probes rebuilds what exists.

Explains: doc.build-method#m5-recall-and-reuse
```

### Inventory

Minted: `render_explanation`, `check_rationale_kept`, `derive_retired_sections`, the scope
`explanation`, the slot `<!-- record-template: <kind> -->`, the edge type `explains` with its inverse
`explained-by`, and the plant cases `explanation-rendered`, `explanation-registry-only`,
`rationale-unmapped`, `rationale-mapped` and `rationale-moved-out` on PLAY-dOrderedCharter-20 S10's
fixture verb; the route `--rationale` of `guide_move.py plan` and its plant `rationale-route` on
`guide_move.py --fixture`. Each function
name was asked of `python tools/lexicon/lexicon.py --suggest <name> --as py.function` at `d8a12f046`: all
three OK. No leg is added: the arm runs in `instruction render (one renderer of record)`.

### Migration

The rationale moves in one pass per guide, its `plan` read before its `apply`. The guides are removed in
the last commit of the unit, after S6 reads green over a scratch commit that removes them.

### Files touched (estimate)

- `tools/playbook/render_playbook.py`
- `tools/playbook/guide_move.py` (the `--rationale` route and its plant)
- `tools/runtime/kit.toml` (the `PLAYBOOK-TEMPLATE.md` render's `[[files]]` and `[[lf_pin]]` rows)
- `tools/playbook/renderers.toml`
- `tools/playbook/edges.toml`
- `tools/playbook/instructions-legacy.txt`
- `tools/memory-tree/instructions.toml`
- `tools/workflows/instructions.toml`
- `tools/run-gates/instructions.toml`
- `tools/policy/catalogue.toml`
- `tools/policy/unsummarised-keys.txt`
- `help/why/` (rendered)
- `memory/guides/ANNOTATION-STYLE.md`, `memory/guides/BUILD-METHOD.md`, `memory/guides/MERGE-BAR.md`,
  `memory/guides/REVIEW-PROTOCOL.md`, `memory/guides/PLAYBOOK-TEMPLATE.md` (removed)
- `memory/guides/SESSION-KICKOFF.md` moved to `memory/project/SESSION-KICKOFF.md`; its readers
  `.governance/install.json`, `skills/session-kickoff/manifest-check.sh`,
  `tools/govkit/fixtures/release-0/deploy.toml`
- `tools/memory-tree/ANNOTATION-STYLE.template.md`, `tools/memory-tree/BUILD-METHOD.template.md`,
  `tools/workflows/REVIEW-PROTOCOL.template.md` (removed)
- `tools/memory-tree/HYGIENE.template.md`, `tools/memory-tree/SPEC-TEMPLATE.template.md` (slot templates);
  `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md` (their renders)
- `tools/memory-tree/kit-dogfood-parity.test.sh`, `tools/workflows/check-protocol-parity.test.sh` (pairs)
- `coding-governance-agents.template.md`, `tools/roles/agents/`, `tools/memory-tree/kit.toml`,
  `tools/memory-tree/adopt-memory-tree.sh`, `tools/memory-tree/README.md`, `tools/workflows/kit.toml`,
  `tools/workflows/README.md`, `tools/template-size-limits.txt`, `tools/policy/caps.toml`,
  `memory/project/method-carriers.txt`, `.memory-tree.conf`, `tools/hooks/agent-cap.js`,
  `tools/drift-audit/drift_signals.py`, `tools/policy/check_policy.py`, `.governance/deploy.toml`,
  `README.md`, `WIRE-INTO-PROJECT.md`, `help/spec-audit.md` (the readers of S8)

### Alternatives rejected

- **A rendered view file per retired guide**, at a new path such as `memory/protocols/<name>.md`. Rejected
  by R-E's own test: "an agent reads its slice and never a whole guide" (layer-instruction `:508-509`).
  A file per guide is a whole guide again, and unit 14's exit check reds a surviving guide path.
- **The no-lost-rationale arm keyed by the compare base.** Rejected by a measurement: units 12 and 16
  remove six guides before this unit lands, and after the build lands the compare base no longer holds
  any of them, so the arm would grade nothing from then on. History read once per run grades every
  removal for good, and `git log --diff-filter=D` over `memory/guides/` costs one call.
- **`explains=<guide path>#<seg>`, the path spelling of the brief's I21.** Rejected because
  PLAY-dOrderedCharter-24 S4 reds a target outside its row's `to` namespaces, and a section target is
  written `<doc>#<seg>` in the `doc` namespace (PLAY-dOrderedCharter-19 S3). I21 is refined to
  `explains=doc.<name>#<seg>`.
- **Reading the key through `govkit.read_policy_value` directly**, as I21 states. Rejected because
  the playbook kit already holds its own reader (PLAY-dOrderedCharter-19 creates
  `tools/playbook/policy_value.py`), and a second path to the policy reader in one kit is a copy.

## 5. Production-readiness checklist

- security — no new write surface: the scope writes only the paths its `[[target]]` row claims, and the
  arm only reads git history and blobs.
- perf / scale — one `git log` per run plus one blob read per removed guide; the page render is linear in
  the units.
- error / empty / loading states — an empty population announces `graded 0`; a refused policy read reds
  naming the key; `registry-only` with no tree is green.
- observability — the arm names guide, heading and address per red; the scope prints the value it read.
- risks — a section heading renamed between base and removal changes its address; S6 reads the removing
  commit's parent, so the address graded is the one last seen.
- testing — the plant cases of the Inventory, through the fixture verb, each in a throwaway tree.
- migration — the rationale moves once per guide, plan before apply; the removal commit is last.
- user docs — `help/why/README.md` itself, and `help/policy.md`'s key table gains the `help.explanation`
  row.

## 6. Acceptance criteria

- **AC1** — When `python tools/policy/policy.py lists --write` has run, `grep -c help.explanation
  tools/policy/unsummarised-keys.txt` prints 0 and the catalogue row carries `summary` and `usage`.
  Red when: the row lacks either field, or a second `help.explanation` row exists.
- **AC2** — When `python instruction_units.py fixture --plant explanation-rendered` runs, its tree holds
  one page per kit with a `help` unit plus the index, each section naming its unit tag and its `Explains:`
  lines, and `render_playbook.py --check-render --scope explanation` exits 0 there.
  Red when: a unit with `help` has no section, or a page is written for a kit with none.
- **AC3** — When the same plant then hand-edits one page and `render_playbook.py --check-render --scope
  explanation` runs, it exits 1 naming the page.
  Red when: a hand edit passes render parity.
- **AC4** — When `python instruction_units.py fixture --plant explanation-registry-only` commits
  `.governance/policy.toml` setting `help.explanation = "registry-only"`, `--render-scope explanation`
  leaves no file under the tree's `why` directory, and a planted page there reds `--check-render --scope
  explanation`; a committed value `inline` reds naming the key.
  Red when: a page renders under `registry-only`, or an unknown value is read as a known one.
  fixture: the policy file is committed, because the reader reads the landed revision.
- **AC5** — When `grep -c why documents.toml` runs after the unit lands it prints 0, and the
  `rationale-apart` arm passes on the tree with the explanation pages rendered.
  Red when: a `help` text appears in a registered document, or the tree is a registered document.
- **AC6** — When `python edge_grammar.py --list` runs, it prints `explains` with inverse
  `explained-by`, from `unit` to `doc`, and a unit row declaring `explained-by=` is red.
  Red when: the type is missing, or its inverse may be declared.
- **AC7** — When `python instruction_units.py fixture --plant rationale-unmapped` commits the removal of a
  planted guide holding sections `## Why` and `## How`, with a unit explaining only `## How`,
  `render_playbook.py --check-render --scope explanation` exits 1 naming the guide, `## Why` and its
  `doc.<name>#why` address.
  Red when: the retirement passes, or the red names no section.
- **AC8** — When the plant `rationale-mapped` adds the second `explains=` edge and the check runs again,
  it exits 0, and with no guide removed it prints `graded 0 guide(s) taken out`; the plant
  `rationale-moved-out`, a commit moving a planted guide to `memory/project/` with no edge, also prints
  `graded 0 guide(s) taken out`.
  Red when: a fully mapped retirement reds, the empty population prints a bare green, or a guide moved
  out of the guides path is graded as removed.
- **AC9** — When `python tools/playbook/render_playbook.py --check-render --scope explanation` runs on this
  tree after the unit lands, it exits 0 with a population of nine guides, this unit's five and unit 12's
  four, and `git ls-files memory/guides` prints nothing.
  Red when: a section of any of the nine is graded unmapped, or a file survives under the guides path.
  figure: nine is PINNED at `d8a12f046` (ten guides less the moved manifest); the section count is
  DERIVED by the run.
- **AC10** — When `git grep -n -E "guides/(BUILD-METHOD|SESSION-KICKOFF)\.md" -- . ':!memory/builds'` runs
  after the unit lands, it prints no reader outside the frozen records, the charter's protocol lines each
  name a `gov_tag.py bundle` command, and `bash manifest-check.sh` reads the manifest at its new path.
  Red when: a reader still names a removed or moved guide.
- **AC11** — When `render_playbook.py --check-render --scope protocols` runs after the unit lands, it
  exits 0 over `memory/TEMPLATE-SPEC.md` and `memory/HYGIENE.md`, the skeleton block of the first equal
  to `record_kinds.py --template spec`, and `grep -c TEMPLATE-SPEC instructions-legacy.txt` prints 0.
  Red when: either template is still on the legacy list, or its skeleton is typed beside the schema.
- **AC12** — When `python guide_move.py --fixture --plant rationale-route` runs, `plan
  --rationale` writes one entry per `##` section of the planted guide, `apply` appends one unit
  row per entry carrying its `help` and its `explains=doc.<name>#<seg>` edge with one change record each,
  and the same apply over a tree whose `instructions_edit.py check` fails leaves the manifest and the
  guide byte-identical.
  Red when: a section moves with no edge, a row is written past a failing check, or a row goes through
  `instructions.edit`'s door and is read as written.
## 7. Gates

`policy fixtures` · `playbook render selftest` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `manifest-check self-test` · `lexicon naming predicates` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `transition-audit arms` · `straggler-guard arms` · `agent-cap self-test` · `scratch-guard self-test` · `hook destinations self-test` · `drift-audit selftest` · `policy check` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The parents' legs `instruction render (one renderer of record)` and `writing practice (records and
units)` run this unit's arm and AC5 once they land; neither is in the manifest at base.

New arm: tools/playbook/render_playbook.py · covers AC2 AC3 AC4 AC7 AC8 · the five plant cases of the Inventory, its failing cases a committed guide removal with one unmapped section and a move out of the guides path walked with a pathspec · none
New arm: tools/playbook/guide_move.py · covers AC12 · the `rationale-route` plant, staged red with `apply` writing past a failing `instructions_edit.py check` · none

## 8. Open questions

- **F1 — Where is an agent's view of a retired guide?** Options: (a) a rendered file per guide; (b) the
  tag slice `gov_tag.py bundle <tag>`, no file. RESOLVED (agent, 2026-11-03, delegated): (b), rung 1:
  R-E says the guides become "views sliced by tag, so an agent reads its slice and never a whole guide"
  (layer-instruction `:508-509`), and the fates record retires the guides (fates `:210`). widens: none · relaxes: none
- **F2 — How do the closed edge set and the retirement rule admit `explains`?** Options: (a) this unit
  adds the `edges.toml` row and asks dOrderedCharter to name it; (b) the arm reads a side map with no edge.
  (b) is a second inventory beside the unit rows. RESOLVED (agent, 2026-11-03, delegated): (a), rung 3.
  The ask, target build dOrderedCharter: PLAY-dOrderedCharter-24 S1's closed set names `explains`
  (`unit` to `doc`, inverse `explained-by`, `pin = "none"`), and PLAY-dOrderedCharter-25 S6 and -29 S8
  read a `doc.<name>#<seg>` address that `derive_retired_sections` returns as resolved and retired with
  a successor when an `explains=` edge targets it; accept: a fixture unit whose `explains=` edge targets a
  section of a guide removed in an earlier commit passes `gov_tag.py check`, and the same address with no
  edge reds the retirement rule. widens: none · relaxes: none
- **F3 — Which population does the arm grade?** Options: (a) guides present at the compare base and gone
  at the tip; (b) every guide removed on the first-parent history. (a) grades nothing after landing and
  misses units 12 and 16 once they land (§4 "Alternatives rejected"). RESOLVED (agent, 2026-11-03,
  delegated): (b), rung 2, decided by the probe `git log --diff-filter=D -- 'memory/guides/*'`, which
  prints nothing at base, so (b) cannot red on history; its liveness is AC7's planted removal. widens: none · relaxes: none
- **F4 — Are the templates graded by the arm?** Options: (a) only removed guides, as the clause says;
  (b) also a template section that vanishes at render. (b) adds a bound beyond the clause that every later
  edit to a rendered template would meet. RESOLVED (agent, 2026-11-03, delegated): (a), rung 3, with the
  limit stated in §7's arm line and S10 moving the templates' rationale as S7 does. widens: none · relaxes: none
- **F5 — `SESSION-KICKOFF.md`, a manifest under `memory/guides/`.** Options: (a) take it out as a guide;
  (b) move it to `memory/project/SESSION-KICKOFF.md` with `manifest_path` re-pointed; (c) leave it for
  unit 16. (a) strands the ratchet gate unit 16 keeps, whose input it is; (c) leaves a file unit 14's exit
  check reds as a surviving guide, and unit 16's spec re-points readers of it without moving it. RESOLVED
  (agent, 2026-11-03, delegated): (b), rung 3: the fates record reshapes the ratchet into "the guarded
  instruction manifest" (fates `:201`) rather than retiring it. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, from the packet's Item 7, v2:1295 `[policies]`, layer-instruction
  R-E (`:506-512`), final-questions FQ-6 (`:241`, `:346`, `:356`, `:376`, `:380`), the fates rows
  `:108` and `:210`, scout B row 7 and its interfaces, and the spec brief's I17, I18 and I21.
- rev-2 · 2026-11-04 · S6 S7 S8 §3 §4 AC8 AC12 §7 §10 · folded
  `2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1` findings 33 (S7 writes rows by `apply`'s kit
  edit and change-record route, never `instructions.edit`'s door), 34 (S7 moves rationale through
  `guide_move.py --rationale` over `prose_move.py`, the edge to PLAY-dConvergedCharter-13 renamed),
  27 (S6 walks without a pathspec, the `rationale-moved-out` plant), 31 (the guides' bytes restated as
  317,842) and 3 (the `PLAYBOOK-TEMPLATE.md` render's rows sit in the runtime descriptor, where unit 12
  moved them, and leave with the render).

## 10. Reuse audit

The seams extended are `render_playbook.py`'s scopes (PLAY-dOrderedCharter-20 S5) and its fixture verb
(S10), `read_units` and the `help` field (PLAY-dOrderedCharter-9 S1-S2), the edge registry
(PLAY-dOrderedCharter-24 S1), the tag slice (PLAY-dOrderedCharter-25 S1), the prose mover (I16): the
factory `tools/lib/prose_move.py` through its guide caller `tools/playbook/guide_move.py plan|apply`
(unit 13 S1, S3, S4), never the dossier caller `dossier_move.py`, whose route sends sections to
proposals and records,
`extract_section` (I12), `record_kinds.py --template` (TOOL-dTotalRecall-1 S5) and the catalogue's
`lists --write` drain (`tools/policy/policy.py`). `python tools/codebase-map/reuse_lookup.py "render each
unit's rationale into a help tree no agent loads"` ranked name-stem hits only (`tree`, `load`,
`load_conf`, `render`); `"refuse removing a guide while one of its sections maps to no unit"` ranked
`units`, `map_root` and `render_map_md`. None renders rationale or grades a retirement, so
`render_explanation` and `check_rationale_kept` are new, each on the renderer's existing scope seam.
Scout B's row 7 holds against source at `d8a12f046`; the brief's I21 disagrees with
PLAY-dOrderedCharter-24 on the edge target's spelling and with PLAY-dOrderedCharter-19 on the reader,
both refined in §4 "Alternatives rejected".

Recall terms used: `python tools/memory-recall/query.py "where does a retired guide's rationale go once guides become rendered views" --terms "help.explanation rationale help field explanation tree guides retired rendered views unit FQ-6 no agent loads"`
