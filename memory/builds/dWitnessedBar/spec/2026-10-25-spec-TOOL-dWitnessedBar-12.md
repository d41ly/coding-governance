# TOOL-dWitnessedBar-12 — the `leg`, `check` and `pack` tag namespaces, and a `tag` on every leg

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 5 · advances TOOL-dWitnessedBar-31

**Carries:** cl-dClosedLoop-0350@37beff65 whole
**Carries:** node:tag-namespace.leg
**Carries:** node:tag-namespace.check
**Carries:** node:tag-namespace.pack

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-b.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-b.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-28 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-fix-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 |
| [2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-28 |

<!-- /gen:spec-records -->

## 1. Goal

Give every gate leg a `tag` in the `leg` namespace beside its free-text `name`, which stays the join
key of every file keyed by leg, and register the `leg`, `check` and `pack` namespaces with their
extractors, so a leg, a check and a pack can be addressed, selected and shape-checked like every
other tagged thing. 139 of 140 leg names failed the tag shape when the systems record measured them
(systems.md:270), and no leg carries a tag today.

## 2. Scope (IN)

- **S1** — A `tag` on each of the 142 rows of `tools/gate-legs.json` and on each of the 68
  `[[gate_leg]]` rows in the kit descriptors, by the rule of §4 "The tag rule". Observed by AC1.
- **S2** — Three `[[namespace]]` rows in `tools/playbook/namespaces.toml`, in
  PLAY-dOrderedCharter-19 S2's row shape, per §4 "The three rows". Observed by AC2.
- **S3** — Three extractors in `tools/playbook/tag_index.py`: `extract_leg` (one member per
  manifest row's `tag`), `extract_pack` (one member `pack.<word>` per distinct `pack` value on the
  manifest's rows) and `extract_check` (one member `check.<kit>.<id>` per `[[check]]` row of a kit
  descriptor). Observed by AC3 and AC4.
- **S4** — The leg row key set, today a literal spelled twice in `tools/run-gates/run-gates.test.sh`
  (`:244` and `:580`), becomes one constant `LEG_KEYS` that both arms read, and `tag` joins it.
  Every later unit adding a row key adds it there once. Observed by AC5.
- **S5** — `LEG_KEY_FLOORS` in `tools/govkit/govkit.py`, beside the three `*_FLOOR_RUN_GATES`
  constants: one table from row key to the run-gates version whose canary admits it, `tag` its first
  entry. The emitter carries a descriptor's `tag` into a target's row only at or above that floor,
  through `check_target_reads_subject`'s `floor` argument. Observed by AC6.
- **S6** — govkit selfcheck 7h's both-ways join gains `tag`: a descriptor row and its manifest row
  carry the same tag. Observed by AC7.
- **S7** — The gov canary `tools/run-gates/run-gates.gov.test.sh` asserts every row of gov's own
  manifest carries a `tag` in the `leg` namespace and no two rows share one. Observed by AC1.
- **S8** — The fixture plants, on PLAY-dOrderedCharter-19 S13's
  `gov_tag.py --fixture --plant <case>`: `leg-rows`, `leg-dup`, `pack-rows` and `check-rows`. Observed by AC3 and AC4.

## 3. Non-goals (OUT)

- The tag grammar, `namespaces.toml`, the index, the shape check and the join factory:
  PLAY-dOrderedCharter-19's and -10's, called here and never re-specced.
- The `pack` row key itself: PLAY-dOrderedCharter-19 S12's, which this unit's extractor reads.
- Moving any file keyed by leg name onto the tag. `ceiling-evidence.txt`, `selftest-budgets.txt`,
  `windows-only-legs.txt`, `silenced_legs` and `tools/roles/house/policy.toml`'s `[gates]` stay keyed
  by `name` (systems.md:265-271).
- Declaring `[[check]]` rows for any kit's numbered checks. The namespace reads `unarmed` until a kit
  declares one (§8 F2); the two checks numbered 23 (final-questions.md:312) are its first candidates.
- The leg factory that generates the manifest: TOOL-dWitnessedBar-11. Until it lands, the tag is
  written in the manifest and the descriptors, and 7h joins the two.
- A repository's own legs' `leg.adopter.<name>` rows: TOOL-dWitnessedBar-28's.
- A rename or retirement of a leg tag through a change record: PLAY-dOrderedCharter-15's write path.

### Edges

- **hands-off** `TOOL-dWitnessedBar-22` — `tag`, the `leg.<owner>.<name>` member a `tests` edge's
  target and an `enforces` row's leg are addressed by
- **hands-off** `TOOL-dWitnessedBar-19` — `tag`, the row key `purpose` is added beside in `LEG_KEYS`
  and `LEG_KEY_FLOORS`
- **hands-off** `TOOL-dWitnessedBar-11` — `tag`, which the leg factory emits from each pack's
  declaration and its conformance gate grades
- **hands-off** `TOOL-dWitnessedBar-14` — `tag`, the `pack.ratchet` member its legs' `pack` value
  yields
- **hands-off** `TOOL-dWitnessedBar-24` — `tag`, the `pack.portability` member its legs' `pack`
  value yields
- **hands-off** `TOOL-dWitnessedBar-28` — `tag`, the `leg` namespace a repository's
  `leg.adopter.<name>` rows join and the `pack.adopter` member
- **consumes-from** external — PLAY-dOrderedCharter-19 S1, S2, S4, S12 and S13 and
  PLAY-dOrderedCharter-10 S3: the grammar, the registry, the index, the `pack` key, the fixture and
  the shape check this unit registers into
- **hands-off** `TOOL-dWitnessedBar-51` — the round-1 minors ids 15, 16 and 41: `LEG_KEYS`' readers through the `level` and `precommit` keys, the tag rule re-derived for units 24 and 9, and the row hash dropping declarative keys, each a scope item of that unit

## 4. Design

### The tag rule

`tag = "leg.<owner>.<name>"`, where `<owner>` is the `id` of the kit descriptor whose
`[[gate_leg]]` row declares the leg, or `gov` for a leg `tools/govkit/registry.toml` exempts, and
`<name>` is the leg's `name` lower-cased, each run of characters outside `[a-z0-9]` folded to one
hyphen and the ends trimmed. A tag over 64 bytes is cut at its last hyphen within 64. Applied at
`cdfbd1cf` the rule yields 142 tags, 68 under a descriptor's id and 74 under `gov`, 3 cut, no two
equal, every one matching `seg := [a-z0-9][a-z0-9-]*`, and no `<owner>` a namespace word (PINNED,
measured 2026-10-25 by a probe over the manifest, the descriptors and the registry).

The rule runs once, at the pass, to write the tags. After that a tag is the leg's declared identity
and is not re-derived when its `name` changes; a rename of the tag is a change record's
(PLAY-dOrderedCharter-15). A new leg is given its tag by the same rule, which the gov canary's
shape and uniqueness arm and 7h hold it to.

### The three rows

```toml
# tools/playbook/namespaces.toml, beside PLAY-dOrderedCharter-10's eight and TOOL-dDeclaredLoop-18's four
[[namespace]]
ns = "leg"
owner = "dWitnessedBar"
layer = "layer.flow"
source = "tools/gate-legs.json, the tag of each row"
extractor = "tag_index:extract_leg"
role = "selects"
purpose-source = "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md#design-tags"
join-armed-by = "dWitnessedBar"
```

| `ns` | `source` | `extractor` | `role` | Members at landing |
|---|---|---|---|---|
| `leg` | `tools/gate-legs.json`, each row's `tag` | `tag_index:extract_leg` | `selects` | 142, DERIVED from the manifest |
| `pack` | `tools/gate-legs.json`, each distinct `pack` value | `tag_index:extract_pack` | `selects` | `pack.tags` once PLAY-dOrderedCharter-19 S12 lands; `ratchet`, `portability`, `adopter` join as their units land |
| `check` | `tools/*/kit.toml`, each `[[check]]` row | `tag_index:extract_check` | `describes` | `unarmed` |

`leg` and `pack` select: a later instruction unit's or a test selection's scope names them. A
`[[check]]` row holds `id` (one segment) and `leg` (the name of the leg that runs it), so
`check.memory-tree.23` and `check.unattended.23` can be told apart once each kit declares them.

### The one key set

```bash
# tools/run-gates/run-gates.test.sh, once, near the top
LEG_KEYS="name argv guard impure reads chunk subject ceiling signature doc_reads tag"
```

Both Python programs that read the key set today (the arm at `:244` and `keyset_probe` at `:580`)
take it from `LEG_KEYS` as an argument, so a key cannot be admitted by one and refused by the
other. The value at the build run is whatever keys the parents added before it (`pack` from
PLAY-dOrderedCharter-19 S12, `enforces` from PLAY-dOrderedCharter-50 S1) plus `tag`.
PLAY-dOrderedCharter-50 S2's `owed_rows.py` reads "each `KNOWN` copy"; where it has landed, it
reads `LEG_KEYS` instead, its two-copies refusal then unreachable.

The run-gates kit's version moves at this pass, and `LEG_KEY_FLOORS["tag"]` is that version
(DERIVED at the pass from `KIT_RUN_GATES_VERSION`, `tools/run-gates/run-gates.sh:36`, 1.43 at
`cdfbd1cf`), so an adopter whose installed canary predates `tag` never meets the key.

### Inventory

Minted: 142 leg tags, the `[[namespace]]` rows `leg`, `check` and `pack`, `extract_leg`,
`extract_pack`, `extract_check`, the `[[check]]` descriptor table, `LEG_KEYS`, `LEG_KEY_FLOORS`, the
gov canary's tag arm, the four plants. Naming cells: each function is asked of the lexicon's
`--suggest` under `--as py.function`, and `LEG_KEY_FLOORS` under `--as py.constant`, at the pass.

### Migration

Additive. Every row gains a key; no name moves; an adopter's manifest gains `tag` on gov rows only
through `apply` or `update` above the floor.

### Files touched (estimate)

- `tools/gate-legs.json`
- `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/run-gates.gov.test.sh`
- `tools/run-gates/run-gates.sh` (the kit version)
- `tools/run-gates/owed_rows.py` (where PLAY-dOrderedCharter-50 landed it)
- `tools/playbook/namespaces.toml`
- `tools/playbook/tag_index.py`
- `tools/playbook/gov_tag.py`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- the 26 descriptors carrying `[[gate_leg]]` rows: `tools/agent-instructions/kit.toml`,
  `tools/branch-reconcile/kit.toml`, `tools/codebase-map/kit.toml`, `tools/drift-audit/kit.toml`,
  `tools/gate-lint/kit.toml`, `tools/lexicon/kit.toml`, `tools/memory-recall/kit.toml`,
  `tools/memory-tree/kit.toml`, `tools/playbook/kit.toml`, `tools/process-monitor/kit.toml`,
  `tools/roles/kit.toml`, `tools/run-gates/kit.toml`, `tools/runlog/kit.toml`,
  `tools/unattended/kit.toml`, `tools/workflows/kit.toml`,
  `tools/govkit/entries/check-agent-cap-restatement.kit.toml`,
  `tools/govkit/entries/check-install-prefix.kit.toml`,
  `tools/govkit/entries/check-kit-versions.kit.toml`,
  `tools/govkit/entries/check-line-length.kit.toml`,
  `tools/govkit/entries/check-microformats.kit.toml`,
  `tools/govkit/entries/check-placeholders.kit.toml`,
  `tools/govkit/entries/check-testsuite-counts.kit.toml`,
  `tools/govkit/entries/check-wiring.kit.toml`, `tools/govkit/entries/kickoff-manifest.kit.toml`,
  `tools/govkit/entries/push-main.kit.toml`, `tools/govkit/entries/settings-merge.kit.toml`

### Alternatives rejected

- **The tag in place of the name.** Every name-keyed file and the run-log history join on `name`
  (systems.md:265-271); moving them is a migration the clause does not ask for.
- **A per-key floor constant.** The fourth hand-copied constant is what I1 forbids; one table keyed
  by row key is read the same way by every later key.
- **Tags hand-written per leg.** 142 hand choices are not derived and cannot be re-checked; the rule
  is stated and its output measured.

## 5. Production-readiness checklist

- security — no new write path; descriptor and manifest edits through the existing govkit paths.
- perf / scale — three extractors over one JSON and the descriptors; the index re-parses only
  changed blobs.
- error / empty / loading states — `check` prints `unarmed` while no `[[check]]` row exists, never
  green; a duplicate or malformed tag reds the gov canary naming both rows.
- observability — `gov_tag.py check` prints each namespace's member count.
- risks — the `check` namespace is empty at landing; an adopter below the floor carries no tags,
  so a selection by `leg.*` there selects nothing until it updates.
- testing — AC1 to AC7 by a pass; the arms of §7 at the close.
- migration — additive, as §4 says.
- user docs — none under `help/`: no page describes the manifest's keys; `tools/run-gates/README.md`
  names `tag` beside `name` at the pass.

## 6. Acceptance criteria

- **AC1** — When a probe reads `tools/gate-legs.json` after the pass, every row carries a `tag`
  matching `leg.<seg>.<seg>`, at most 64 bytes, no two equal, and each descriptor-backed row's tag
  opens with its descriptor's `id`; the gov canary's tag arm, given a copy with one tag duplicated,
  names both rows.
  Red when: a row lacks a tag, or two legs share one.
  figure: the row count is DERIVED from the manifest at observation; 142 is PINNED at `cdfbd1cf`.
- **AC2** — When `grep -cE '^ns = "(leg|check|pack)"' namespaces.toml` runs in `tools/playbook/`,
  it prints 3.
  Red when: a row is missing, so a `leg.*` tag reads `namespace not registered`.
- **AC3** — When `python gov_tag.py --fixture --plant leg-rows` runs, the index holds the fixture's
  `leg.gate-lint.shell-hygiene` member; under `--plant leg-dup`, two rows with one tag, `check`
  exits 1 naming the tag.
  Red when: `extract_leg` reads the `name` instead of the `tag`, or a duplicate passes.
- **AC4** — When `python gov_tag.py --fixture --plant pack-rows` runs, a fixture manifest whose rows
  carry `"pack": "tags"` twice and `"pack": "ratchet"` once yields exactly `pack.tags` and
  `pack.ratchet`; under `--plant check-rows`, two kits each declaring `[[check]] id = "23"` yield
  `check.memory-tree.23` and `check.unattended.23`, and with no `[[check]]` row the namespace prints
  `unarmed`.
  Red when: a pack word is counted once per row, or an empty `check` namespace reads green.
- **AC5** — When the canary's key-set arm and its `keyset_probe` are run over a fixture manifest
  with a row carrying `tag`, both pass; with `LEG_KEYS` edited to drop `tag`, both fail; and
  `grep -c '^KNOWN = ' run-gates.test.sh` in `tools/run-gates/` prints 0.
  Red when: either arm keeps its own literal, so the two can disagree.
- **AC6** — When a probe calls govkit's emitter over a fixture target whose installed runner reads
  one minor version below `LEG_KEY_FLOORS["tag"]`, the written row carries no `tag`; at the floor
  it carries the descriptor's tag.
  Red when: a target below the floor receives a key its canary refuses.
- **AC7** — When `govkit.py selfcheck` runs over a fixture whose descriptor row's `tag` differs
  from its manifest row's, check 7h names the leg and both tags.
  Red when: the two spellings drift unseen.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `govkit selftest` · `govkit selfcheck` · `govkit acceptance matrix` · `govkit refusal join` · `recall floor arms` · `playbook render selftest` · `measure-legs selftest` · `agent-instructions self-test` · `branch-reconcile selftest` · `codebase-map adopter e2e` · `codebase-map gate coverage` · `codebase-map kit selftest` · `drift-audit selftest` · `lexicon selftest` · `pre-push run-log line` · `review-join self-test` · `run-gates run-log line` · `runlog selftest` · `shell-hygiene selftest` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `memory hygiene`

New arm: tools/run-gates/run-gates.test.sh · covers AC5 · both key-set arms reading `LEG_KEYS`, staged by `tag` cut from it · that suite's arm count
New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 · the tag presence and uniqueness arm, staged by one duplicated tag · that suite's arm count
New arm: tools/playbook/adopt-playbook.sh · covers AC3 AC4 · the playbook-render selftest runs `gov_tag.py --fixture` under the four plants, staged by `leg-dup` · none
New arm: tools/govkit/selftest.py · covers AC6 AC7 · the `tag` floor pair and 7h's tag join, staged by the floor table entry removed · none

## 8. Open questions

- **F1 — What is a gov-exempt leg's owner segment?** Options: (a) `gov`; (b) `adopter`, as a
  repository's own leg; (c) the kit whose file the argv names. (b) collides with the form a real
  adopter's overlay rows take (TOOL-dWitnessedBar-28), so gov's and an adopter's own legs would be
  one population; (c) names a kit as owner of a leg its descriptor refused to declare.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — What declares the `check` namespace's members?** Options: (a) `[[check]]` rows in kit
  descriptors, read by `extract_check`, `unarmed` until a kit declares one; (b) parse each checker's
  numbered comment headers; (c) defer the row. (b) reads two comment styles that are conventions,
  not grammar (`# <n> — ` in `check-memory-hygiene.sh:614`, `# ---- <n>: ` in
  `check-unattended.sh:1172`); (c) leaves the clause's namespace unregistered. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the declared-table precedent TOOL-dDeclaredLoop-18 F2 set for
  `command`. widens: none · relaxes: none
- **F3 — Where does the one key set live?** Options: (a) `LEG_KEYS` in `run-gates.test.sh`, the
  suite whose two arms read it; (b) a constant in `run-gates.sh` read by the canary, as
  `KNOWN_KNOBS` (`run-gates.sh:479`) is. (b) puts in the runner a set the runner
  never reads, so the constant would describe nothing it governs. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3. widens: none · relaxes: none
- **FACT-QUESTION · F4 — Does the stated rule give 142 unique, shape-valid tags within 64 bytes?**
  Probe: the rule of §4 applied to `tools/gate-legs.json`, the descriptors and
  `tools/govkit/registry.toml` at `cdfbd1cf`. Observation, 2026-10-25: 142 tags, 3 cut at 64 bytes,
  no collision, every segment valid. Liveness: before the cut, 3 tags exceeded 64 bytes, so the probe
  reports a negative when the cut is removed. RESOLVED (agent, 2026-10-25, delegated): the rule as
  stated, rung 2. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 12, the brief's shared interfaces I1
  and I2 and owned-node table, scout B's row for cl-0350, systems.md `[design-tags]`, and the
  manifest, descriptors and canary read at base `cdfbd1cf`.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-51, written by the round-1 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seams extended are PLAY-dOrderedCharter-19's registry, index and fixture and
PLAY-dOrderedCharter-10's extractor module and shape check, all specced and DEFERRED to that build's
run; and, in today's code, the canary's two key-set literals (`tools/run-gates/run-gates.test.sh:244`
and `:580`), govkit's floor constants (`tools/govkit/govkit.py:6010-6017`) and their reader
`check_target_reads_subject` (`:6063`), the emitter's row builder (`:4422-4455`) and selfcheck 7h
(`:2785`). The lookup
`python tools/codebase-map/reuse_lookup.py "give each gate leg a tag beside its free-text name"`
ranked only generic `leg`, `legs` and `read_text` stems and named no seam,
which is the expected answer: no tag field exists. One disagreement with scout B: it counts 70
descriptor rows; at `cdfbd1cf` 68 `[[gate_leg]]` rows sit in 26 descriptors, which with 74
`[[exempt_leg]]` rows covers all 142 legs. The recall probe returned scout B's row, the
systems-retrofit review that introduced the `tag` field, and PLAY-dOrderedCharter-19 S12; none
disagreed with source otherwise.

Recall terms used: `python tools/memory-recall/query.py "how does a leg get a tag in the leg namespace while its name stays the join key" --terms "leg tag namespace name join key gate-legs.json KNOWN canary key set floor run-gates check pack"`
