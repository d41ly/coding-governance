# DEPL-dShippedRelease-9 — a derived runbook: the operator order for install and update, rendered from the kit descriptors, a hand edit red at render parity

**Status:** OPEN · rev-2 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 31 · closes DEPL-dShippedRelease-32

**Carries:** cl-dClosedLoop-0419@c78ef1a4 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |
| [2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-9-deviation-91.md](../build/2026-10-30-build-DEPL-dShippedRelease-9-deviation-91.md) | deviation | — |
| [2026-10-30-build-DEPL-dShippedRelease-9-reuse-scout-e.md](../build/2026-10-30-build-DEPL-dShippedRelease-9-reuse-scout-e.md) | research | DEPL-dShippedRelease-10 DEPL-dShippedRelease-21 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 |
| [2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md](../prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md](../reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-10 DEPL-dShippedRelease-21 DEPL-dShippedRelease-23 DEPL-dShippedRelease-31 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-13 DEPL-dShippedRelease-4 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-6 DEPL-dShippedRelease-27 DEPL-dShippedRelease-5 DEPL-dShippedRelease-30 DEPL-dShippedRelease-3 DEPL-dShippedRelease-25 DEPL-dShippedRelease-7 DEPL-dShippedRelease-16 DEPL-dShippedRelease-20 DEPL-dShippedRelease-17 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-18 DEPL-dShippedRelease-24 DEPL-dShippedRelease-8 DEPL-dShippedRelease-26 DEPL-dShippedRelease-19 DEPL-dShippedRelease-22 |

<!-- /gen:spec-records -->

## 1. Goal

`WIRE-INTO-PROJECT.md` is 164,498 bytes of hand-written prose (PINNED, measured at `f4597719`), and the
only check on it, `tools/govkit/check_runbook_parity.py`, asks whether an anchor exists and says it
does not grade prose (`:14-17`), so the order an operator installs and updates kits in is stated
nowhere a machine grades (`gap-deploy-08`). This unit renders that order from the kit descriptors into
one region of the runbook, through dOrderedCharter's renderer as a new scope, so a hand edit to the
region is red at render parity, and it lets the rendered rows answer the population check, whose
ratchet of 18 entries with no section falls to 0. It is the last unit in build order, so its header
closes DEPL-dShippedRelease-32.

## 2. Scope (IN)

This unit owns no node. The order it renders is the one `item.kits.install` and `item.kits.update`
(DEPL-dShippedRelease-17) walk, both reading `read_kit_rows`.

Build-run preconditions, each specced and unbuilt at this base: PLAY-dOrderedCharter-20 S4, S5 and S8
(`tools/playbook/renderers.toml`, `--render-scope`, `--check-render`, the
`instruction render (one renderer of record)` leg), and through it dOrderedCharter's units 7, 9, 12
and 16; TOOL-dLinkedLibrary-18 S2 (`region_py`, `read_region`, `splice_region`) with
TOOL-dLinkedLibrary-52's refusal of a body holding its own marker; TOOL-dDeclaredLoop-12 S5
(`order_by_needs`); PLAY-dOrderedCharter-36 S1 (`read_kind_schema`); and units 10 and 21 of this build.
dPlacedRequest, dKeptSession, dFairHearing and dSafePassage reach this unit only through those.

- **S1** — The region. One pair of marker lines, `<!-- gov:runbook-order -->` and
  `<!-- /gov:runbook-order -->`, in `WIRE-INTO-PROJECT.md`, under a new hand-written heading
  `## The operator order — install and update`, placed before `## 0`. Every byte outside the pair stays
  hand-written; the two markers stay byte for byte. Observed by AC1 and AC2.
- **S2** — The scope. `runbook` joins the scopes of `tools/playbook/render_playbook.py`:
  `--render-scope runbook --target <tree>` writes the region through `splice_region`, and
  `--check-render --scope runbook --target <tree>` compares it. `--check-render` with no scope includes
  it, as PLAY-dOrderedCharter-20 S8 states of every scope. A `[[target]]` row of `renderers.toml` claims
  it, `paths = ["WIRE-INTO-PROJECT.md"]`, `renderer = "playbook:runbook"`,
  `region = "gov:runbook-order"`, and `read_runbook_target` reads the path and the marker from that row,
  so neither is typed in the scope. Observed by AC1 and AC9.
- **S3** — The rows. `render_runbook_order(rows)` is pure: it takes `read_kit_rows(root)`
  (DEPL-dShippedRelease-10 S6) and returns the table §4 "The table" states, one row per kit in that
  order, each column read from one descriptor key. Each key is checked against the `[[field]]` rows of
  `kit-schema.toml` through `read_kind_schema` before the first row renders, so a renamed field refuses
  rather than blanking a column. A row whose `installable` is `false` stays out of the order: it
  carries `—` for its number, `not installable: <why_not_installable>` as its Install cell, and sorts
  after every numbered row. An argv token
  renders as §4 states; a token the render does not know refuses naming the kit and the token. No cell
  reads a kit version. Observed by AC1, AC4 and AC8.
- **S4** — Render parity, defined here because no record defines it: the bytes between the pair of
  `WIRE-INTO-PROJECT.md` equal `render_runbook_order`'s output over the tree's own descriptors.
  `check_runbook_order` makes that compare, and a difference exits 1 with one line naming the file, the
  region, the first differing line and the remedy, the `--render-scope runbook` command. Bytes outside
  the pair are not compared. Observed by AC2 and AC3.
- **S5** — The refusals. Each exits non-zero with the file unchanged and names its cause: no pair, two
  pairs, a body holding the marker, an empty `read_kit_rows`, a `requires` cycle, a `[[target]]` row
  absent. A tree holding no `WIRE-INTO-PROJECT.md`, every adopter since the file does not ship, prints
  one `runbook: no target in this tree` line and exits 0 before any descriptor is read. That skip is no
  coverage in gov: `check_runbook_parity.py:76-78` reds the absent file there. Observed by AC5.
- **S6** — The population check. `tools/govkit/check_runbook_parity.py` reads the region through an
  inline `region_py` block and credits each kit id in a rendered row as that entry's section, beside the
  anchors, with the two-way arm and a missing pair red. `PROBLEM_PIN` moves from 18 to 0 in the same
  commit, and the docstring's "WHAT IT DOES NOT DO" paragraph says where render parity lives. The
  anchors of the twelve hand-written sections stay. Observed by AC6.
- **S7** — The hand-written sentences. The runbook's opening paragraph (lines 3-5) gains a sentence
  holding the words "the rendered order", which wins where a section's position disagrees with it, and
  the new heading gains one saying `govkit apply` orders a selection by the same rule and `govkit
  update` walks the receipt's `kits` in the order `apply` wrote them, any kit the default set gained
  after them (`tools/govkit/govkit.py:7982`, `:9234`, `:9273`). Observed by AC9.
- **S8** — The leg. Render parity runs in the `instruction render (one renderer of record)` leg, and that
  leg must declare no `doc_reads`, or declare `WIRE-INTO-PROJECT.md`, because a doc-only push
  skips a leg that declares `doc_reads` and none of whose paths moved (`.githooks/gate-env.sh:105-108`),
  and the runbook is in `GATE_DOC_PATHS`. No new leg. Observed by AC7.
- **S9** — The plants. `python tools/playbook/instruction_units.py fixture --plant <case>`, the seam
  PLAY-dOrderedCharter-20 S10 builds, gains `runbook-order`, `runbook-hand-edit`, `runbook-stale`,
  `runbook-not-installable`, `runbook-refusals` and `runbook-tokens`, each a throwaway tree of three
  descriptors, a `kit-schema.toml`, a `renderers.toml` and a runbook. Observed by AC1, AC2, AC3, AC4, AC5
  and AC8.

## 3. Non-goals (OUT)

- Rendering the rest of the runbook. The per-kit sections, the migrations and the harness-migration
  blocks `tools/govkit/selftest.py:14872` cuts out stay hand-written.
- Rendering the `govkit` verbs: §8 F7.
- `kit-schema.toml`, `read_kit_rows`, `purpose`, `installable` and `why_not_installable`: units 10 and
  21. This unit reads them.
- Retiring `skills/deploy-governance/SKILL.md`. `layer-expansions.md:440` says it retires, and no clause
  of this build carries that (`gap-tool-05` has no spec).
- The `[isolate]` ports and the emitted `up —` line: §8 F8.
- TOOL-aHonedRuleset-15's install-path defects and the runbook's other open asks.
- Regenerating the region at the lander or at an adopter's update: §4 "Alternatives rejected".

### Edges

- **consumes-from** `DEPL-dShippedRelease-10` — `kit-schema.toml`, the `[[field]]` rows each column is checked against, and `read_kit_rows`, the rows and their order; without them there is nothing to render
- **consumes-from** `DEPL-dShippedRelease-21` — `installable`, `why_not_installable` and `purpose`, the fields the not-installable rows and the Purpose column render
- **consumes-from** external — PLAY-dOrderedCharter-20 S4, S5, S8 and S10 (the renderer table, the scopes, the render gate, the fixture verb), TOOL-dLinkedLibrary-18 S2 and TOOL-dLinkedLibrary-52 (the region factory), PLAY-dOrderedCharter-36 S1 (`read_kind_schema`), each specced and unbuilt at this base, so each is a build-run precondition
- **hands-off** `DEPL-dShippedRelease-78` — parity's line ending and its figure, which the minors batch repairs (review ids 19, 37, 59)

## 4. Design

### The table

The region holds one table and nothing else.

```markdown
<!-- gov:runbook-order -->
| # | Kit | Purpose | Requires | Install | Update | Verify |
|---|---|---|---|---|---|---|
| 1 | `playbook` | <purpose> | — | — | — | — |
| 2 | `memory-tree` | <purpose> | — | `bash <prefix>/memory-tree/adopt-memory-tree.sh --scaffold` | `…` | — |
| 3 | `memory-recall` | <purpose> | `memory-tree` | `…` | `…` | `…` |
| — | `lib` | <purpose> | — | not installable: <why_not_installable> | — | — |
<!-- /gov:runbook-order -->
```

| Column | Descriptor key | Rendered as |
|---|---|---|
| # | `installable` | the row's position among installable rows, `—` when `false` |
| Kit | `id` | backticked |
| Purpose | `purpose` | whitespace squeezed, each pipe escaped |
| Requires | `requires` | each id backticked, comma-joined, `—` when empty |
| Install | `adopt`, `selectable`, `why_not_installable` | the `[adopt]` argv, `conditional` when `selectable` says so and it has none, `—` otherwise |
| Update | `regenerate` | each `[[regenerate]]` argv, joined by ` ; `, `—` when none |
| Verify | `check` | the `[check]` argv, `—` when none |

`{prefix}` renders `<prefix>`, `{kit}` renders `<prefix>/<home>` from the descriptor's `home`,
`{memory_root}` and `{map_root}` render `<memory_root>` and `<map_root>`: the four of `TOKENS`
(`tools/run-gates/regen.py:48`). The literal prefix never appears, because
`tools/check-install-prefix.sh:241` bans it in this file. At this base the descriptors' argvs use
`{prefix}` and `{kit}` only (PINNED, 2026-10-30).

One region serves both orders because they are one order: `apply` writes `kits` in selection order
(`tools/govkit/govkit.py:7982`) and `update` walks that list (`:9234`), appending what the default set
gained (`:9273`). `read_kit_rows` orders through `order_by_needs`, which is `derive_install_order`'s
loop (TOOL-dDeclaredLoop-12 §4), so the rendered order and `govkit`'s are one computation.

### The flow

```python
def read_runbook_target(root):          # the `playbook:runbook` row, or a Refusal
def render_runbook_order(rows):         # rows -> the region's body, pure
def write_runbook_order(root):          # splice_region, then one write with newline='\n'
def check_runbook_order(root):          # read_region against render_runbook_order
```

`--check-render` with no scope reaches the last. Its leg, not `govkit runbook parity`, carries the
byte compare (§8 F2); `check_runbook_parity.py` keeps its population. `RENDERED_ROW` is its one new
pattern, anchored at a line opening `| <n> | ` or `| — | ` followed by a backticked id, and read only
inside the pair.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `render_runbook_order`, `read_runbook_target`, `write_runbook_order`, `check_runbook_order` | functions | `py.function`, each OK by `--suggest` at `5d1c82ac` |
| `RENDERED_ROW`, `RUNBOOK_REGION` | constants of `check_runbook_parity.py` | `py.constant` is undeclared, so no cell grades them |
| `runbook`, `playbook:runbook` | a render scope and its renderer id | none |
| `region` | a key of a `[[target]]` row | none |
| `gov:runbook-order` | a marker pair, the `gov:` family of `gov:playbook` | none |
| the six plants of S9 | fixture cases | none |

### Migration

None. `WIRE-INTO-PROJECT.md` is no registry entry's file, so no adopter holds it and no upgrade step is
owed. The build pass adds the pair and the heading by hand, then runs the render once.

### Rollout

Live at landing, at order 31, after every unit that moves a descriptor key this table reads. A branch
that changes a descriptor column after this lands owes one re-render, which the leg's remedy line names.

### Files touched (estimate)

- `WIRE-INTO-PROJECT.md`
- `tools/playbook/render_playbook.py`
- `tools/playbook/instruction_units.py`
- `tools/playbook/renderers.toml`
- `tools/govkit/check_runbook_parity.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **The whole file rendered.** Rejected by reading it: 2,200 lines, from which `selftest.py:14872` cuts
  four bash blocks by their markers, and no descriptor holds the derive-or-ask judgement the rest
  carries. A template holding them all would be the same prose in a second file.
- **A `gen:` marker pair.** `GEN_REGION_AWK` strips that family for the memory tree's readers, and this
  file is no memory record; `gov:` is the family of `AGENTS.md:1` and of TOOL-dWellOiledMachine-21 S4's
  `gov:harness-prompts`.
- **A version column.** `cmd_mint` moves versions at every landing whose shipped bytes moved
  (`tools/govkit/govkit.py:13497`), after the branch's render, so the region would stale on its own
  landing.
- **A `[[regenerate]]` row.** A row on `tools/playbook/kit.toml` runs at every adopter's update and its
  `writes` is what a rollback restores (`:50-55`), for a file no adopter holds. The leg's remedy line
  costs one command on the rare commit that needs it.
- **A byte compare inside `check_runbook_parity.py`.** A second comparator of one render, reached from
  an expansion kit, for a gate PLAY-dOrderedCharter-20 S8 already runs over every scope.
- **`WIRE-INTO-PROJECT.md` in `INSTRUCTION_PATHSPECS`.** §8 F4.

## 5. Production-readiness checklist

- security — no new secret, egress or automation surface; the scope writes one file, between one pair
  of markers the table names, under `splice_region`'s refusal of a body holding its marker.
- perf / scale — one descriptor read per run, and the compare costs milliseconds; 30 rows at this base.
- error / empty / loading states — every refusal of S5 leaves the file unchanged; an empty population
  refuses, so a table of no rows never reads as parity.
- observability — one line on green naming the row count, one on red naming the file, region, line and
  remedy; the no-target skip prints.
- risks — two branches that each move a descriptor column conflict inside the region, and re-rendering
  resolves it (the class of PLAY-dClosedLoop-35). A file of this exact name in an adopter's own tree
  with no pair would refuse, which no registry row can cause, since none ships it.
- testing — the plants of S9, both ways, and the `govkit selftest` arm of §7.
- migration — none: §4 "Migration".
- user docs — N/A for `help/`: no adopter-facing command or file changes, and the runbook is its own
  reader's page. `tools/playbook/README.md` is untouched, since a scope adds no adopter step.

## 6. Acceptance criteria

- **AC1** — When `python instruction_units.py fixture --plant runbook-order` renders a tree whose kit `a`
  requires `c`, `--check-render --scope runbook` exits 0, the rows read `c`, `a`, `b`, and a second
  render leaves `git hash-object` of the file unchanged; on the tree, the numbered rows of
  `WIRE-INTO-PROJECT.md` keep the relative order of the ids `python kit_factory.py --list` prints.
  Red when: rows sort alphabetically, a second order exists, or a render moves a byte twice.
- **AC2** — When `python instruction_units.py fixture --plant runbook-hand-edit` changes one byte of a
  rendered row, `python tools/playbook/render_playbook.py --check-render --scope runbook --target <tree>`
  exits 1 naming `WIRE-INTO-PROJECT.md`, `gov:runbook-order`, the line and the re-render command, and
  exits 0 once restored; a byte changed outside the pair exits 0.
  Red when: a hand edit to the rendered section passes, or an edit to the narrative reds.
- **AC3** — When `python instruction_units.py fixture --plant runbook-stale` adds a `requires` edge to one
  descriptor with no re-render, the check exits 1, and after `--render-scope runbook` it exits 0 and the
  order has moved.
  Red when: a row survives the descriptor it was read from.
- **AC4** — When `python instruction_units.py fixture --plant runbook-not-installable` holds a descriptor
  carrying `installable = false` and `why_not_installable`, that kit's row carries `—` for its number and
  the reason in Install, and sorts last; with the key absent the row is numbered.
  Red when: a not-installable kit gets a place in the order.
- **AC5** — When `python instruction_units.py fixture --plant runbook-refusals` runs its cases, no pair, two
  pairs, a `purpose` holding the marker, an empty population, a `requires` cycle, no `[[target]]` row and a
  column key absent from `kit-schema.toml` each exit non-zero naming the cause with the file's
  `git hash-object` unchanged; a tree with no runbook prints `runbook: no target in this tree` and exits 0.
  Red when: an empty or malformed region reads as parity, or a refused render writes.
- **AC6** — When `python tools/govkit/check_runbook_parity.py` runs on the tree it prints
  `0 problem(s) · pin 0`; in a fixture repository holding a copy of it, a registry of two entries, one
  anchored and one rendered, it exits 0; with the rendered row deleted it exits 1 naming that entry; with a
  row naming no entry it exits 1 naming the row; with the pair gone it exits 1.
  Red when: a section-less entry passes, or the check credits a row outside the pair.
  fixture: a scratch repository under `%TEMP%/<short-name>`; the checker finds its root by `.git`.
  figure: 0 is the PINNED equality; 18 was PINNED at `f4597719` from 30 entries and 12 anchors, and
  the 32 entries of DEPL-dShippedRelease-21 S3 are all rendered, `lib` and `govkit` unnumbered.
- **AC7** — When `python -c "import json, sys; print([(l['argv'], l.get('doc_reads')) for l in json.load(open(sys.argv[1], encoding='utf-8')) if l['name'] == 'instruction render (one renderer of record)'])" tools/gate-legs.json`
  runs, it prints one row whose argv runs `--check-render` with no `--scope`, its `doc_reads` `None` or
  naming `WIRE-INTO-PROJECT.md`.
  Red when: a doc-only push of a hand edit to the region skips the compare.
- **AC8** — When `python instruction_units.py fixture --plant runbook-tokens` renders argvs using `{prefix}`
  and `{kit}`, the rows spell `<prefix>/<home>/…` and no literal prefix or brace, a pipe in a `purpose`
  stays in one cell, and an argv carrying `{nosuch}` refuses naming the kit and the token.
  Red when: a literal prefix reaches the runbook, or an unknown token renders.
- **AC9** — When `git grep -n -F "playbook:runbook" -- '*renderers.toml'` and `git grep -n -F "the rendered
  order" -- WIRE-INTO-PROJECT.md` run, each prints at least one line, and `python
  tools/playbook/render_playbook.py --check-render --scope runbook --target .` exits 0 on the tree.
  Red when: the row or a sentence is missing, or the landed region is stale.

## 7. Gates

`govkit runbook parity` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `playbook render selftest` · `policy fixtures` · `playbook parity` · `install-prefix (shipped surface)` · `dead-path carriers (deleted files still named)` · `python resolver (behaviour + inline parity + idiom ban)` · `spec tokens (a spec's own names resolve)`

The close also reads the `instruction render (one renderer of record)` leg, which PLAY-dOrderedCharter-20
S10 adds and no manifest holds at this base, so it sits in this sentence and not on the line above.

New arm: tools/playbook/instruction_units.py · covers AC1 AC2 AC3 AC4 AC5 AC8 · the `runbook-*` fixture cases of S9, each failing case staged by its plant · none
New arm: tools/govkit/selftest.py · covers AC6 · a scratch repository holding a copy of `check_runbook_parity.py`, its failing case a rendered row deleted · none

## 8. Open questions

- **F1 — Does the runbook render whole, or by region?** Scout E's F5. Options: (a) the whole file from a
  template; (b) one region. The clause says "a hand edit to a rendered section", and its subject is
  "the operator order", not the runbook.
  RESOLVED (agent, 2026-10-30, delegated): (b), rung 1. widens: none · relaxes: none · grants: PLAY-dClosedLoop-3 `WIRE-INTO-PROJECT.md`, a governance carrier the clause names, gains one rendered region, its heading and two hand-written sentences
- **F2 — What is "render parity"?** Scout E's F6 and disagreement 8: it appears only in v2's chain rows.
  Options: (a) PLAY-dOrderedCharter-20's gate with a new scope; (b) a stronger `govkit runbook parity`
  keeping the leg's name. The clause says "dOrderedCharter's renderer", and that spec's S8 grades every
  scope's bytes, so (b) adds a second comparator. The `govkit runbook parity` leg keeps its name and
  its population, as fates:180 has it stay, and S4 states the definition.
  RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, the most feature-rich survivor. widens: none · relaxes: none
- **F3 — How does a core renderer reach the install order, which sits in
  `tools/govkit/govkit.py:911`?** Scout E's F4. Options: (a) an `optional` row under
  PLAY-dOrderedCharter-16 S2 with a named fallback; (b) a reader in the core.
  `layer-expansions.md:443` makes the descriptor schema a core point, and DEPL-dShippedRelease-10 S6
  puts `read_kit_rows` in `tools/playbook/kit_factory.py`, carrying `order_by_needs` inline "so a core
  reader reaches the order with no govkit". The scope calls `read_kit_rows` and imports nothing from
  `tools/govkit/`, so `check_layers.py` finds no edge.
  RESOLVED (agent, 2026-10-30, delegated): (b), rung 1. widens: none · relaxes: none
- **F4 — Does the runbook join `INSTRUCTION_PATHSPECS`?** Scout E's disagreement 8. Options: (a) add it;
  (b) a `[[target]]` row only. PLAY-dOrderedCharter-3 S6 reads that list as the load-bearing population,
  which a 164 KB document no agent loads whole does not belong to, and PLAY-dOrderedCharter-20 S8 would
  grow its shrink-only legacy list by one. TOOL-dWellOiledMachine-21 S4 is the precedent: its
  `messages` scope's row claims paths outside the list.
  RESOLVED (agent, 2026-10-30, delegated): (b), rung 3. widens: none · relaxes: none
- **F5 — PLAY-dOrderedCharter-20 S5 says every write records the target's lock row, and `lock --check`
  (PLAY-dOrderedCharter-12 AC4) reds any byte of the file changing, so a narrative edit here would red
  it.** Options: (a) a row carrying `region` writes no lock row; (b) a lock row hashing the region's
  bytes alone, which moves `lock --check`'s meaning. This region's parity is already
  `check_runbook_order`, and it renders no unit, so the lock would carry nothing else. Ask for
  dOrderedCharter: PLAY-dOrderedCharter-20 S5 exempts a `[[target]]` row carrying `region` from the
  lock · accept `render_playbook.py --render-scope runbook` writes no row to
  `.governance/instructions.lock`, and `lock --check` stays green after a narrative edit of
  `WIRE-INTO-PROJECT.md`, seen on a fixture.
  RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, the smaller change to a parent's contract. widens: none · relaxes: none
- **F6 — Do rendered rows answer the population check, or does its pin stay at 18?** Options: (a) credit
  a rendered row as a section, the pin at 0; (b) leave the check alone, 18 entries still reported
  section-less. The gap names the check as existence-only, and each rendered row states the kit's order,
  purpose, adopter, update and check, which is more than an anchor proves. TOOL-cMendedVintage-18 left
  the eighteen to "a separate build", and this is the build that derives them. The liveness half
  stands, since a row renders from required fields.
  RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, the most feature-rich survivor. widens: none · relaxes: none
- **F7 — Do the `govkit` verbs render too?** Options: (a) a new `[[operator_step]]` descriptor table; (b)
  typed in the renderer; (c) the kit table rendered, the verbs left in hand-written prose. The clause
  says "rendered from the kit descriptors", and no descriptor at this base holds a verb, so (b) is a
  typed fact in the renderer and (a) is a second statement of the steps `kits.install` and
  `kits.update` walk (DEPL-dShippedRelease-17), which `[one-fact]` refuses.
  RESOLVED (agent, 2026-10-30, delegated): (c), rung 3, the survivor with fewer open questions. widens: none · relaxes: none
- **F8 — Who carries `gap-deploy-08`'s `[isolate]` ports and `up —` half?** Scout E's F13: no clause
  does, and `layer-expansions.md:125` closes the gap "in part". Options: (a) leave that half open with
  an ask, recorded as a departure; (b) build an allocator and a checker here. (b) fails veto 1: it adds
  a second mechanism to a one-mechanism unit, and it grades an empty population, since
  TOOL-dWellOiledMachine-11 §3 states only an adopter's isolation pack declares services and none
  exists, which `[gate]` refuses as coverage. Deviation 91 records the departure, and
  PLAY-dOrderedCharter-2 S5 takes the credential field. Ask for dWellOiledMachine: the workspace
  allocator takes ports from an isolation pack, and an emitted `up —` line is graded · accept a planted
  pack's services get ports `allocate_workspace` records, and a planted `up —` line naming a port
  outside them is red.
  RESOLVED (agent, 2026-10-30, delegated): (a), rung 5, the most capable option failing only the goal bound, the standing ruling ER:240. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, from the packet's Items 9, `gap-deploy-08`, the spec brief's unit row
  and shared interfaces, scout E's row and its disagreements 8 and 9.
- rev-2 · 2026-10-30 · §3 · the Edges gain the mirror of each edge the round-1 spec audit's promoted units declare toward this unit (units 78); no scope, design or criterion moved.

## 10. Reuse audit

The seams extended are `render` and the scope flags of `tools/playbook/render_playbook.py` (`:1024`,
PLAY-dOrderedCharter-20 S5), `splice_region` and `read_region` (TOOL-dLinkedLibrary-18 S2),
`read_kit_rows` (DEPL-dShippedRelease-10 S6), `read_kind_schema` (PLAY-dOrderedCharter-36 S1), and the
ratchet of `tools/govkit/check_runbook_parity.py:42`, `:60`. `python tools/codebase-map/reuse_lookup.py
"render a section of a hand written document from declared rows and red a hand edit to it"` ranked
`render` and name-stem hits; `"compare a generated region of a document with a fresh render and refuse
a difference"` ranked `render` and the shell `region`, the factory's own population; `"order kits by
their declared dependencies for an install"` ranked `resolve_kit_dir` and name-stem hits and missed
`derive_install_order`, which source shows at `tools/govkit/govkit.py:911`. Each lookup confirms no
renderer takes a section inside a hand-written document at this base.

Where records and source disagree: PLAY-dOrderedCharter-20 §10 cites `render` at `:979`, and it is at
`:1024`. The gap register says 163 KB, and the file is 164,498 bytes. The ratchet's comment measures 8
anchors over 26 entries, and the tree holds 12 over 30, the same 18. The scout's order source is right
at `:911`, and `read_kit_rows` now carries it. The scout's fork F4 assumed the order stayed in an
expansion; DEPL-dShippedRelease-10 S6 settles that.

Recall terms used: `python tools/memory-recall/query.py "how is the install runbook derived from kit descriptors and how is a hand edit to a rendered section refused" --terms "runbook render parity kit descriptors operator order install update region WIRE-INTO-PROJECT govkit anchor"`, and `python tools/memory-recall/query.py "what closes the runbook half of gap-deploy-08 and what stays stated only" --terms "gap-deploy-08 isolate ports up line stated only runbook narrative parity allocator checker"`
