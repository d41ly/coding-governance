# TOOL-aMendedFleet-43 — the map renders a card of at most 1 KB per feature from its dossier's toml fence

**Status:** SPECCED · rev-2 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 43

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

A reader who needs one feature's moving parts today opens its dossier, and the dossiers nearest the
20,480-byte `DOSSIER_CAP_BYTES` cap cost that reader 20 KB to learn a title, a status and a claim
list. This unit renders, from each dossier's toml fence alone, a card of at most 1024 bytes into one
generated file beside `MAP.md`, kept fresh by the same `gen_map.py --check` and gate compare that
keep `MAP.md` fresh. The review's second half of the point, moving measured history out of the
dossiers near the cap, is a separate mechanism with a disjoint write set, and §8 F1 splits it.

## 2. Scope (IN)

- **S1** — `render_cards_md(tree, inventory_ids)` in `tools/codebase-map/map_lib.py` returns the
  cards file's text: the same one-line generated banner `render_map_md` writes, a `# Feature cards`
  heading and one sentence saying the cards derive from the fences alone, then one `## <feature>`
  section per entry of `tree.dossiers`, sorted by feature. `FOUNDATION.md` gets no card: it is
  substrate, not a feature. The output is deterministic: sorted inputs, LF, no timestamp.
  Observed by AC1 and AC2.
- **S2** — A card holds, in this order: the heading; the dossier's title, cut to at most 160 bytes
  at a character boundary with `...` appended when cut; one line naming status, streams and the
  dossier's repo-relative path; then one list line each for decisions, for every non-empty claims
  inventory in `inventory_ids` order, and for the path globs, each line naming its full item count
  before its items. Items are added one at a time while the card stays within
  `FEATURE_CARD_CAP_BYTES`, 1024, counted in UTF-8 bytes from the heading through the card's last line, with room reserved
  for the cut line. Every item that did not fit is counted, and the card ends with one line,
  `cut <n> item(s) to fit 1024 bytes; the dossier's toml fence lists them all`, when n is above
  zero. Observed by AC1 and AC2.
- **S3** — Nothing outside the toml fence enters a card, so a prose-only edit to a dossier never
  stales the cards file, and a fence edit stales it exactly when it already stales `MAP.md`.
  Observed by AC3.
- **S4** — `_artifacts()` in `tools/codebase-map/gen_map.py` gains the cards file, spelled as a
  `gen_dir`-rooted literal so `check_gate_coverage.py` reads it, and so do the `fresh` mappings in
  `tools/codebase-map/test_codebase_map.py` and `tools/codebase-map/test_codebase_map.template.py`.
  `--write` writes it, `--check` reports it STALE, and `--scaffold` writes it on a tree with no
  dossiers as a banner and heading only. Observed by AC1, AC3 and AC4.
- **S5** — The cards file is named, with what it holds, in the layout list of `_README` in
  `gen_map.py`, in its dogfood rendering `memory/map/README.md`, and in the generated-artifacts
  rows of `tools/codebase-map/README.md`. Observed by AC5.
- **S6** — The cards file and `memory/map/generated/symbols.json` are regenerated in the unit's
  commit, and the prose of `memory/map/features/codebase-map.md` is refreshed in the same commit,
  since this unit touches its paths. Observed by AC1.
- **S7** — A selftest arm renders cards for a fixture tree: one ordinary dossier, one whose title
  and globs overflow the cap, and an empty tree. NOT OBSERVED by a criterion here: the suite runs
  once at the close, and the arm is declared under `New arm:` in §7.

## 3. Non-goals (OUT)

- Moving measured history out of the dossiers near the cap. §8 F1 splits it into
  `TOOL-aMendedFleet-89`; it edits dossier prose, which this unit never reads.
- Any reader of the cards. No unit of this build points a session step at a card: the orientation
  units, 77 and 78, add the overlaps cell and Step 4's context-command pointer and neither names the
  cards, and a pointer to a file that does not exist yet cannot be written first.
- Card content from dossier prose: constraints, gaps, seams or the reuse affordance. Prose has no
  fixed shape a 1 KB budget can cut fairly, and reading it would couple the cards to every prose edit.
- A card for `FOUNDATION.md`, or a byte size or last-commit field on a card. The size moves with
  every prose edit and the commit is unit 37's derivation.
- Bumping the codebase-map kit version. Many units of this build move the kit, and the bump is owed
  once, after the last move, at the close.

### Edges

- **consumes-from** `TOOL-aMendedFleet-37` — AC1 reads `map_diff.py --stale-dossiers`, which that
  unit builds, to observe that this unit refreshed the dossier whose paths it touched.
- **hands-off** `TOOL-aMendedFleet-89` — the measured-history move, which F1 assigns there; it edits
  prose below the fences and leaves the cards file byte-identical.
- **hands-off** external — pointing a session step at the cards, which no unit of this build owns
  and is not built here.
- **hands-off** external — the codebase-map kit version bump, owed once at the close.

## 4. Design

### Evidence

Read at base `7af5f564`, whose bytes for every file below equal HEAD's at `fee9f62b`.

- `Dossier` in `tools/codebase-map/map_lib.py` already carries feature, title, status, streams,
  decisions, claims by inventory and globs, parsed from the fence by `parse_dossier`; `load_map_tree`
  returns them as `tree.dossiers`. A card needs no parser of its own.
- `_artifacts()` in `gen_map.py` and `test_generated_artifacts_are_fresh` in the gate each spell the
  artifact set as `gen_dir / "<name>"` literals, and `check_gate_coverage.py` compares the two sets
  with one regex. Adding a literal to both is the whole wiring.
- Measured at `fee9f62b` on node a, PINNED: the longest dossier title is 500 bytes (`runlog`), the
  largest claim list is 33 keys (`lexicon`), and 7 dossiers sit within 10% of the cap, as the review
  said. A card that printed every field uncut would pass 1024 bytes for several dossiers, which is
  why S2 cuts by item and states the count.
- `memory/map/generated/` is outside hygiene check 6's index set
  (`check-memory-hygiene.sh --print-index-set` lists no path under it), so the cards file carries no
  size cap but its own per-card one.

### Data model

```text
## <feature>

<title, at most 160 bytes>

- status `<status>` · streams `<stream>`[, `<stream>`] · dossier `<map-root>/features/<feature>.md`
- decisions <n>: `<id>`, `<id>`, ...          (or `decisions 0`)
- <inventory-id> <n>: `<key>`, `<key>`, ...   (one line per non-empty inventory)
- globs <n>: `<glob>`, ...
- cut <c> item(s) to fit 1024 bytes; the dossier's toml fence lists them all
```

A list line whose first item does not fit is left out whole and its items join the cut count; a line
already started keeps its header count, so a reader always learns how many items exist.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `render_cards_md` | function, `map_lib.py` | `py.function`, verb `render`; `--suggest render_cards_md --as py.function` answered OK |
| `FEATURE_CARD_CAP_BYTES` | module constant, `map_lib.py` | none |
| `CARDS.md` | generated artifact under the map root's `generated/` | none |

### Rollout

The gate template is copied into an adopter only when absent, so an upgraded adopter's frozen gate
names no cards file and `check_gate_coverage.py` reds naming it. That is the check's purpose; the
kit README's row says which line to add. Units 35 to 42 move the same kit first, sequentially.

### Files touched (estimate)

- `tools/codebase-map/map_lib.py`
- `tools/codebase-map/gen_map.py`
- `tools/codebase-map/test_codebase_map.py`
- `tools/codebase-map/test_codebase_map.template.py`
- `tools/codebase-map/selftest.py`
- `tools/codebase-map/README.md`
- `memory/map/README.md`
- `memory/map/generated/CARDS.md`
- `memory/map/generated/symbols.json`
- `memory/map/features/codebase-map.md`

### Alternatives rejected

- **One generated file per feature.** It is the literal reading of "a card per feature", but a
  deleted dossier would leave an orphan file that neither `--check` nor the gate enumerates, and
  both would need a directory sweep; one file is one more literal in two lists.
- **A print mode and no committed file.** Nothing to keep fresh, but nothing to read without running
  python either, and it would be a second reader of the fence beside the generator.
- **Appending cards to `MAP.md`.** That file is an inventory-to-claimant table; one feature's card
  would sit 15 KB into it, and every fence edit already re-renders both anyway.

## 5. Production-readiness checklist

- security — N/A: a local generator writes one more file from data it already parses.
- perf / scale — one pass over the parsed tree that `gen_map.py` already loads; output grows by at
  most 1 KB per dossier.
- error / empty / loading states — an empty tree renders the banner and heading only; a title past
  160 bytes and a list past the cap are cut and counted, never refused.
- observability — every cut card says how many items it dropped and where they are.
- risks — the cards file enters the recall corpus like `MAP.md` does, so recall can return a card
  chunk; it carries the same facts as the fence, so the answer is not wrong, only shorter. An
  upgraded adopter's gate-coverage leg reds until they add one line, which is that check's design.
- testing — AC1 to AC4 run directly; the selftest arm is S7's.
- migration — N/A: a new generated file, written by `--write`.
- user docs — S5's three README rows.

## 6. Acceptance criteria

- **AC1** — When `python tools/codebase-map/gen_map.py --check` runs at the unit's tip, it exits 0;
  and a `python -c` reader that splits `CARDS.md` under the map's `generated/` directory on its
  `## ` headings prints one section per dossier `git ls-files memory/map/features` lists, each at
  most 1024 bytes when encoded as UTF-8, and `python tools/codebase-map/map_diff.py
  --stale-dossiers` does not list `codebase-map`.
  Red when: a dossier has no card, a card passes 1024 bytes, or the unit leaves its own dossier
  older than its paths.
  figure: the card count is DERIVED from `git ls-files` at observation time.
- **AC2** — When, in a scratch clone of the unit's tip under a short `%TEMP%` path, the title of
  `memory/map/features/runlog.md` is lengthened to 600 bytes and its `globs` list gains 60 entries,
  and `python tools/codebase-map/gen_map.py --write` runs, the `runlog` card is still at most 1024
  bytes and valid UTF-8, its title line ends `...` within 160 bytes, its `globs` line states the
  full count, and its last line reads `cut <n> item(s)` with n equal to the items the card omits.
  Red when: the card grows past the cap, the cut line is missing, or n miscounts.
- **AC3** — When, in that clone, a sentence is appended under `## Gaps` in
  `memory/map/features/runlog.md`, `python tools/codebase-map/gen_map.py --check` exits 0; when
  instead the fence's `status` is edited to another legal value without a regen, which leaves
  `MAP.md` unchanged, it exits 1 printing `STALE` for
  `CARDS.md`, and `python tools/codebase-map/test_codebase_map.py` prints `FAIL
  test_generated_artifacts_are_fresh`.
  Red when: a prose edit stales the cards, or a fence edit goes unnoticed by either reader.
- **AC4** — When `python tools/codebase-map/check_gate_coverage.py --list` runs at the tip, both the
  engine's set and the installed gate's set name `CARDS.md`; when the cards literal is deleted
  from the gate's `fresh` mapping in the working tree, `python tools/codebase-map/check_gate_coverage.py`
  exits 1 naming it, and restoring the line returns it to exit 0.
  Red when: the gate can omit the cards file silently.
- **AC5** — When `git grep -n "CARDS.md" -- tools/codebase-map/README.md memory/map/README.md tools/codebase-map/gen_map.py`
  runs, it hits each of the three files.
  Red when: the layout docs do not name the new artifact.

## 7. Gates

`codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/codebase-map/selftest.py` · a fixture tree with an ordinary dossier, one whose title and globs overflow the cap, and an empty tree, rendered by `render_cards_md`; staged red by removing the per-item budget check · none

## 8. Open questions

- **F1** — Is moving measured history out of the dossiers near the cap part of this mechanism?
  RESOLVED (agent, 2026-10-04, delegated): split — the history move goes to a new unit the run
  adds, `TOOL-aMendedFleet-89`. It edits the prose of the seven dossiers near the cap and decides where measured history
  lives instead, while this unit renders from the fences and never reads prose: two mechanisms with
  disjoint write sets, and the build's rule is one mechanism per spec.
- **F2** — One cards file, one file per feature, or a print mode?
  RESOLVED (agent, 2026-10-04, delegated): one generated file, per §4's rejected alternatives. It is
  the only shape the existing freshness compare and the gate-coverage check read with one literal
  each, and it is readable without running anything.
- **F3** — What may a card carry?
  RESOLVED (agent, 2026-10-04, delegated): the fence only, S2's fields in S2's order. Anything from
  prose would stale the cards on prose edits that change no claim.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the synthesis's item [#47], `parse_dossier`,
  `_artifacts()`, the gate's `fresh` mapping and `check_gate_coverage.py`, re-measured at `fee9f62b`.
- rev-2 · 2026-10-04 · S2 §3 §4 §8 · the M2 cross-read: the history move named `external` and "a unit
  the run adds" while `TOOL-aMendedFleet-89` exists in this build, so the Non-goal, Edges and F1 name
  it; the Non-goal gave the card pointer to units 77 and 78, whose specs add an overlaps cell and a
  Step 4 pointer and never name the cards, so it now says no unit owns it; and the cap constant was
  spelled `CARD_CAP_BYTES`, the name the session card's 8,192-byte cap already carries in
  `skills/session-kickoff/manifest-check.sh` and units 76, 77 and 96 cite, so S2 and the Inventory
  spell it `FEATURE_CARD_CAP_BYTES`.

## 10. Reuse audit

The seams extended are `render_map_md` in `tools/codebase-map/map_lib.py`, whose banner and
determinism rules the cards copy, `load_map_tree` and `Dossier` for the parsed fences, `_artifacts()`
in `tools/codebase-map/gen_map.py`, and the `fresh` mapping of `test_generated_artifacts_are_fresh`
in the gate, which `check_gate_coverage.py` already joins. `python tools/codebase-map/reuse_lookup.py
"render a short generated summary card per feature from the dossier toml fence"` ranked
`render_inventories_json`, `render_map_md` and `render_affordance_exempt` first, all in the map kit,
then `load_dossier_texts` and `parse_dossier`; nothing renders a per-feature summary, so the cards
are a new renderer beside `render_map_md` rather than an extension of one. The probe printed
`unscanned layers: .sh`, and no shell file renders map artifacts. Recall returned the map README's
layout list, `MAP.md`'s header and `TOOL-aRelaxedShard-1`, which declared the dossier cap, and
`TOOL-dFoldedVerdict-7`, which records that capped documents fill up; no record proposes a card.
Where the report and the tree disagree: they do not; the seven dossiers within 10% of the cap
re-measured as seven at `fee9f62b`.

Recall terms used: `python tools/memory-recall/query.py "is there a short generated per-feature
card from the codebase-map dossier toml claims, and where should measured history live when a
dossier nears its byte cap" --terms "codebase-map dossier toml fence card generated MAP.md gen_map
byte cap DOSSIER_CAP_BYTES split measured history"`
