# TOOL-dWitnessedBar-13 — retrofit's baseline ledger factory in `tools/lib`

**Status:** CLOSED · rev-4 · 2026-11-19 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 3 · advances TOOL-dWitnessedBar-31

**Carries:** cl-dClosedLoop-0351@d6eaa553 whole
**Carries:** node:system.retrofit

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 TOOL-dWitnessedBar-106 TOOL-dWitnessedBar-107 TOOL-dWitnessedBar-108 TOOL-dWitnessedBar-109 TOOL-dWitnessedBar-110 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-c.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-c.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-fix-return.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-28 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-11-19-build-TOOL-dWitnessedBar-13-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-13-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-13-1-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-13-1-builder-return.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-13-red-fix-10.md](../build/2026-11-19-build-TOOL-dWitnessedBar-13-red-fix-10.md) | red-fix | — |
| [2026-11-19-build-TOOL-dWitnessedBar-13-red-fix-11.md](../build/2026-11-19-build-TOOL-dWitnessedBar-13-red-fix-11.md) | red-fix | — |
| [2026-11-19-build-TOOL-dWitnessedBar-13-red-fix-12.md](../build/2026-11-19-build-TOOL-dWitnessedBar-13-red-fix-12.md) | red-fix | — |
| [2026-11-19-build-TOOL-dWitnessedBar-13-red-fix-13.md](../build/2026-11-19-build-TOOL-dWitnessedBar-13-red-fix-13.md) | red-fix | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-84 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-fix-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-13-2-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-13-2-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-13-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-13-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-13-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-13-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-13-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-13-reground-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-13-spec-fix-2-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-13-spec-fix-2-brief.md) | journal | — |
| [2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-28 |
| [2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md](../reviews/2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md) | diff-review | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |

<!-- /gen:spec-records -->

## 1. Goal

Give every population a check tolerates one primitive: a ledger file per population, registered with
its key kind, drain, direction and home, read and compared by one factory, carried across a rename
and merged by row. Gov held 28 registries in at least six grammars (scout C's census, PINNED at
`cdfbd1cf`; unit 16 re-derives its population) and writes the count ratchet twice, in
`sh_hygiene.py` and `encoding_posture.py` (gap-test-14).

## 2. Scope (IN)

- **S1** — The canonical factory block `# >>> legacy_ledger_py` in `tools/lib/legacy_ledger.py`,
  holding the registration record, the row grammar and reader, the atomic writer, the four
  directions, the both-ways compare and the base compare of §4. Observed by AC1, AC2, AC3 and AC4.
- **S2** — The registration: a `[[ledger]]` table in the owning kit's `kit.toml`, declaring
  `population`, `seed`, `key`, `fields`, `drain`, `direction`, `home` and `leg`, and optionally
  `verbatim` (S11), read by `read_registrations(root)` from every tracked descriptor wherever its
  kit is homed (§8 F7). A population no kit descriptor owns, one a
  repository-root tool reads or the step rows, registers as a `[[ledger]]` table in
  `tools/govkit/registry.toml`, which `read_registrations` reads beside the descriptors (the reads
  TOOL-dWitnessedBar-16 §8 F3 and TOOL-dWitnessedBar-18 §8 F2 make). The derived index of populations
  is that function's output, never a typed list. Observed by AC1 and AC9.
- **S3** — Each ledger file opens with a header line rendered from its registration, which the
  reader compares with the registration both ways. Observed by AC1.
- **S4** — The both-ways arm calls `compute_coverage`, PLAY-dOrderedCharter-19 S9's `coverage_join`
  block (`tools/lib/coverage_join.py#compute_coverage`), and the base is `resolve_compare_base`,
  TOOL-dGroundRules-21 S7's `compare_base_py` block (`tools/lib/compare_base.py#resolve_compare_base`),
  each imported and never copied into the factory's block (D3). The factory adds the count compare and
  the direction predicates around them. Observed by AC2 and AC3.
- **S5** — Rename carry: `carry_renames(root, reg, base)` re-keys every `site` row whose path
  `read_renames(root, base)` names renamed between the base and the working tree, keeping count,
  SHA and disposition, and `compare_to_base` re-keys the base rows through the same pairs before it
  judges the direction; a rename alone is neither a gain nor a drain. Observed by AC4.
- **S6** — The ledger merge class in `tools/memory-tree/merge-rows.py`: `check_ledger` beside
  `check_build_backlog`, which selects the ledger row plane, a row predicate and the factory's row
  key, the merge rule "drained beats carried, the lower count wins", and the postconditions
  `no_new_duplicates`, `no_misfiled_rows`, `no_row_loss` and `structure_identity`, each run over the
  plane `merge` selected. Driven through `merge-rows.sh` and the existing `merge=rows` attribute.
  Observed by AC5 and AC6.
- **S7** — `merge-rows.test.sh` runs its append-collision case, "disjoint appends", on a planted
  ledger conflict, and a concurrent-drain case beside it. Observed by AC5 and AC6.
- **S8** — The copy-install route: inline module copies `tools/memory-tree/legacy_ledger.py` and
  `tools/gate-lint/legacy_ledger.py`, plus `tools/gate-lint/coverage_join.py` carrying the
  `coverage_join`, `remote_ladder_py` and `compare_base_py` blocks as `tools/memory-tree/coverage_join.py`
  does, each block held by its `PARITY_ROWS` row of `tools/lib/resolve-python.test.sh`: one new row,
  `legacy_ledger_py`, and the three existing rows, which find the gate-lint copy by its marker. The
  suite also gains a behaviour section `2o` for the factory. Observed by AC7.
- **S9** — The count ratchet's second instance: `check_registry` and `read_registry` in
  `tools/gate-lint/sh_hygiene.py` and `tools/gate-lint/encoding_posture.py` become thin adapters over
  the factory's `read_rows` and `compare_counts`, each keeping its signature, its messages and its
  four-field `reason` grammar until TOOL-dWitnessedBar-16 converts its registry. Observed by AC8.
- **S10** — A CLI on the canonical file, `python legacy_ledger.py read|compare|carry <population>`,
  with `compare` taking `--measured <path>` (§8 F6), run in the repository its working directory
  sits in, printing one finding per line and exiting 1 on any finding, 0 on none, 2 on a refusal
  (§4 "The CLI"). It is how a pass and section `2o` observe the factory. Observed by AC1, AC2, AC3
  and AC4.
- **S11** — The line-number refusal's declared exception: a registration's `verbatim = [<field>]`
  names key fields whose text is the tracked subject, such as a `file:line` positional reference, so
  `read_rows` stores them as written and refuses a line-number shape in every other field and every
  other population (the read TOOL-dWitnessedBar-18 §8 F1 makes). Observed by AC10.

## 3. Non-goals (OUT)

- Converting any of gov's registries, the pins or the cutoffs, and the readers those conversions
  owe: TOOL-dWitnessedBar-16, -17, -18 and -20. The policy kit's shrink-only legacy-homes list,
  landed after `cdfbd1cf`, is unit 20's.
- `test.seed`, the seed verb and unarmed reporting: TOOL-dWitnessedBar-15. That includes running a
  registration's `seed` argv: its bound and its `dead probe:` liveness are that unit's §4 "The
  rule", and its interpreter, tokens and working directory are TOOL-dWitnessedBar-51 S32's. `compare`
  reads measured rows it is handed and runs no argv (§8 F6).
- Whether a home not yet written is one the target's hygiene admits: TOOL-dWitnessedBar-15's
  seed-time home test, which TOOL-dWitnessedBar-47 replaces. This unit's one writer rewrites a home
  already tracked (§4 "The CLI").
- The `ratchet` pack's legs, the widen records and `retrofit.widen`: TOOL-dWitnessedBar-14. This
  unit names what a direction refuses; the pack decides what a refusal costs.
- The touch join and a hunk drain: `build.scope`'s, dScopedBuild's.
- Moving or changing `compute_coverage` and `resolve_compare_base`: landed by PLAY-dOrderedCharter-19
  S9 (`9cb93347d`) and TOOL-dGroundRules-21 S7 (`f6674a6a2`) (D3).
- The merge driver's table class, `check_manifest` and `resolve_tables`, which keeps its precedence
  in `merge` unchanged.
- A second merge driver, or a new `.gitattributes` line: no ledger exists at landing; each converting
  unit adds its file's `merge=rows` line.
- The `ledger` record kind and the census kinds: dTotalRecall's.

### Edges

- **hands-off** `TOOL-dWitnessedBar-15` — `legacy_ledger.py`, the factory whose registration and
  atomic writer `test.seed` seeds through, and `read_rows`, whose `tail=()` form is the one parser of the
  rows a seed argv prints, through which the seed verb reads its argv's stdout
- **hands-off** `TOOL-dWitnessedBar-14` — `legacy_ledger.py`, whose directions, both-ways compare,
  base compare, rename carry and merge class the `ratchet` pack's legs grade
- **hands-off** `TOOL-dWitnessedBar-16` — `legacy_ledger.py`, onto which each registry converts in
  place, adding its `[[ledger]]` row and its `merge=rows` line, and `read_registrations`, which reads
  the kit-less tools' tables in the govkit registry
- **hands-off** `TOOL-dWitnessedBar-17` — `legacy_ledger.py`, its `record`, `key` and `cutoff` key
  kinds for the pins and the date cutoffs
- **hands-off** `TOOL-dWitnessedBar-18` — `legacy_ledger.py`, the registration the keyed lists and
  the step rows join, `read_registrations`, which reads the step rows' table in the govkit registry,
  and `verbatim`, the field the file:line references are stored under
- **hands-off** `TOOL-dWitnessedBar-20` — `legacy_ledger.py`, the population the legacy-homes list
  converts into
- **hands-off** `TOOL-dWitnessedBar-19` — `legacy_ledger.py`, the factory its pending population of
  legs whose purpose the rule cannot derive registers on
- **hands-off** `TOOL-dWitnessedBar-24` — `legacy_ledger.py`, the shell-role ledger and the
  portability arms' registries
- **hands-off** `TOOL-dWitnessedBar-28` — `legacy_ledger.py`, the `shrink-only` list of today's
  hand-added leg rows
- **consumes-from** external — PLAY-dOrderedCharter-19 S9's `coverage_join` block with
  `compute_coverage`, and TOOL-dGroundRules-21 S7's `compare_base_py` block with
  `resolve_compare_base`, both landed; without them the both-ways arm and the base have no shared
  engine
- **hands-off** `TOOL-dWitnessedBar-51` — the round-1 minors ids 4, 52 and 54: `compare_counts`' ceiling rule, `compare_to_base`'s absent and legacy bases, and the ledger merge rule's remaining cases, each a scope item of that unit

## 4. Design

### The registration

```toml
# tools/<kit>/kit.toml, one table per population the kit's check tolerates
[[ledger]]
population = "substitution-fed-loops"
leg = "shell hygiene (a loop fed by a command substitution)"
seed = ["python3", "{prefix}/gate-lint/sh_hygiene.py", "--measure"]
key = "site"                       # site | key | record | cutoff
fields = ["path", "delimiter"]     # the key's fields, in row order
drain = "hunk"                     # hunk | key | none
direction = "shrink-only"          # shrink-only | append-only | declared-set | ceiling
home = "memory/project/substitution-fed-loops.txt"
verbatim = []                      # optional: key fields the line-number refusal skips
```

`read_registrations(root)` derives no tool root (§8 F7). It lists `git ls-files` at `root` and
reads every tracked file whose name is `kit.toml`, at any depth, and every tracked file whose path
ends `govkit/registry.toml`, at any depth, refusing two of the latter. Each kit's descriptor is
read where the kit is homed, so a kit an adopter homed outside the others' parent registers as
theirs do. It returns one `Registration` per table, refusing a table missing a field, a value
outside its closed set, a `verbatim` entry not in its `fields`, a `site` table whose `fields` lack
`path`, a `home` that is absolute or holds a `..` segment, or two tables with one `home` wherever
each sits. A refusal names the file and the table's `population`. The govkit
registry is the home for a population no descriptor owns: govkit carries no `kit.toml`, and
`load_registry` (`tools/govkit/govkit.py#load_registry`) reads only its own tables, so a `[[ledger]]` table
beside them changes nothing it reads. A repository with no tracked govkit registry, which is every
copy-installed adopter, registers through its descriptors alone. `seed` may be `[]`, a check with no seed, which TOOL-dWitnessedBar-15 reports
unarmed; whether a `home` is one the target's hygiene check admits is that unit's seed-time test.
The derived index of populations is this list. A registration keyed to a leg by `leg` is how
`test.seed` (unit 15) finds the check to seed at a leg's row.

What the read does not check: a tracked fixture named `kit.toml` that holds a `[[ledger]]` table
registers as a kit's would. On 2026-11-19 all 18 tracked files named `kit.toml` sit at
`tools/<kit>/kit.toml` (PINNED; `git ls-files | grep -cE '(^|/)kit\.toml$'`), so none is a fixture.

### The ledger file

```
# ledger · <population> · key <kind> <field>,<field> · direction <direction> · drain <drain>
<field> TAB <field> TAB <count> TAB <sha> TAB <disposition>
```

The header is rendered from the registration, and the reader refuses a header that disagrees with
it (the one-fact rule: a rendered copy with a gate comparing it). Rows are TAB-separated: the key's
fields, then a positive integer count, then the 8 to 40 hex SHA the row was seeded or widened at,
then a disposition from the closed set `seeded`, `carried:<unit>`, `deferred:<ask>`, `keep:<ask>`,
`widened:<record>`. A key field that is a bare integer, or ends in `:<digits>`, is refused as a line
number, unless the registration names that field in `verbatim`: there the text is the subject the
population tracks, a positional reference quoted as written, and never the row's position. The
exception is per field and per registration; no other field and no other population is relaxed. A
blank line or a `#` line other than the header is ignored. No key appears twice.

### The factory's functions

| Function | What it returns |
|---|---|
| `read_registrations(root)` | the `Registration` list, or a refusal naming each bad table |
| `read_rows(path, arity, tail=("sha", "disposition"), verbatim=())` | `(rows, malformed)`; `tail=("reason",)` reads today's four-field registries for this unit's S9 adapters; `verbatim` holds the field positions the line-number refusal skips; `tail=()` reads measured rows, the key's fields then the count, TAB-separated, the rows TOOL-dWitnessedBar-15 §4 "The rule" says a seed argv prints, so one parser reads ledger and measurement alike |
| `write_rows(root, reg, rows)` | writes header and rows to `<root>/<reg.home>`, the declared home and no other path, through a sibling temp file and `os.replace`, so a run that dies leaves the old file or the new one, never half of either |
| `compare_counts(measured, declared, direction)` | one finding per key: `unmeasured row`, `undeclared site`, `count rose`, `count fell`; the both-ways key sets come from `compute_coverage` with no owners, its `unclaimed` and `stale_baseline` fields |
| `read_renames(root, base)` | the `(old, new)` pairs `git diff -M -z --name-status <base>` names at `root`, the base against the working tree, so a staged `git mv` counts as a committed one does |
| `compare_to_base(root, reg)` | the rows at `resolve_compare_base(root)`'s SHA, each `site` row re-keyed through `read_renames(root, <sha>)` before any key is compared, beside the working rows, judged by the direction; or `None` and the base's own reason |
| `carry_renames(root, reg, base)` | the working rows with each path `read_renames(root, base)` names re-keyed, and the `(old, new)` pairs it applied |

The direction predicates, each over the base rows and the working rows:

| Direction | Refused |
|---|---|
| `shrink-only` | a key the base lacks, or a count above the base's, unless the row's disposition is `widened:<record>` |
| `append-only` | a base row edited or removed |
| `declared-set` | nothing against the base; both ways against the measurement only |
| `ceiling` | a measured value above the row's count |

`compare_to_base` names each refusal `gained`, `raised`, `edited`, `removed` or `above ceiling`,
with the key. A refusal is a finding the caller prints; the factory never exits. With no base, `compare_to_base`
returns `None` with the reason, which a caller must print as unresolved and never as green
(`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md@5b0cb48caa25:440-442`).

### The CLI

The repository is `git rev-parse --show-toplevel` run in the working directory; outside a work tree
the CLI exits 2. `<population>` names one registration `read_registrations` returns; an unknown
name, or any registration refusal, exits 2.

| Verb | What it does |
|---|---|
| `read <population>` | reads the home through `read_rows`, compares the header both ways, prints each row, and prints each malformed line as a finding naming its line number |
| `compare <population> [--measured <path>]` | prints `compare_to_base`'s findings, or `unresolved` and the base's reason; with `--measured`, also `compare_counts` over `read_rows(<path>, arity, tail=())` and the working rows. Without it the both-ways half is not run, and one stderr line says so |
| `carry <population>` | applies `carry_renames` at `resolve_compare_base(root)`'s SHA and writes the result through `write_rows`, printing each `(old, new)` pair it applied; no base exits 2 with the base's reason |

`carry` writes only a home `git ls-files --error-unmatch` names at the repository. An untracked or
absent home exits 2 naming it and writes nothing, so this unit never creates a home and never runs
TOOL-dWitnessedBar-15's admission test. An `unresolved` line is a finding and exits 1. What the CLI
does not check: whether the `--measured` file came from the registration's own `seed`.

### The merge class

`check_ledger(path, lines)`, with `lines` the three sides' line lists in `%O`, `%A`, `%B` order, is
true when the first line of each is a ledger header for one population; headers that disagree raise
`StructureDrift`. A ledger's home is
declared, not path-shaped, so the class reads the header the factory wrote rather than a path
pattern (§8 F3). In `merge` (`tools/memory-tree/merge-rows.py#merge`) the table class,
`check_manifest`, returns before the row plane and the view/shard refusal runs next; `check_ledger` is
asked after both and before `skeleton` runs, since the plane it selects is what `skeleton` splits
by, and selects the ledger key census as `no_new_duplicates`' `ids` the way `check_build_backlog`
selects `measure_row_classes` for a backlog. A ledger header matches neither
`check_manifest`'s file name nor the two-line shape of `check_family_view`
(`tools/memory-tree/backlog.py#check_family_view`), so neither earlier step takes a ledger.

`merge` selects a row plane, a predicate and a key, once, and passes it to every reader of rows. The
generic plane is today's pair, `_ROW_RE`'s bullet test and `_row_key`
(`tools/memory-tree/merge-rows.py#_row_key`), and is each reader's default, so every non-ledger
merge runs byte for byte as before. Each of these takes the plane where it now splits rows by
`_ROW_RE`: `skeleton`, `census`, `no_new_duplicates`, `no_row_loss`
(`tools/memory-tree/merge-rows.py#no_row_loss`), `structure_identity`
(`tools/memory-tree/merge-rows.py#structure_identity`) and the audit line's row counts. Run on the
generic plane, `no_row_loss` would count no ledger row and `structure_identity` would read every row
as structure, refusing every ledger merge. Under the ledger class:

- the row predicate is every line that is neither blank nor `#`;
- the row key is the line's first `arity` TAB fields, `arity` read from the header;
- `resolve_rows` takes the ledger rule: a key one side removed and the other left as at `%O` is
  removed (drained beats carried); a key both sides changed takes the lower count with that side's
  SHA and disposition; equal counts with different SHA or disposition are a conflict region;
- `no_new_duplicates` takes the ledger key census as `ids`, `no_row_loss` and `structure_identity`
  run over the ledger plane, and `no_misfiled_rows` runs unchanged: its `sections` reads the
  anchor grammar's `key` (`tools/memory-tree/merge-rows.py#key`), which keys a bullet-led line only,
  as a probe of ledger-shaped rows showed on 2026-11-19, so on a ledger it compares nothing.
  That is what it does not check here;
- the audit line counts rows on the ledger plane, reports every ledger row keyed, and its census
  field reads `ledger-keyed`.

A ledger's `.gitattributes` line is `<home> merge=rows`, the attribute the authored indexes already
carry, so `merge-rows.sh` and check-wiring's `check_merge_rows` (`tools/check-wiring.sh#check_merge_rows`)
need no second driver.

### The copy-install route

`tools/lib/` ships nothing, so two kits carry the block as a sibling module: memory-tree, whose
`merge-rows.py` reads the header and key, and which codebase-map, drift-audit and the later
converting kits already `require`; and gate-lint, which requires nothing
(`tools/gate-lint/kit.toml@61946391f2f6:8`), for this unit's S9 adapters. gate-lint also carries a
sibling `coverage_join.py` shaped as memory-tree's is, holding the `coverage_join`,
`remote_ladder_py` and `compare_base_py` blocks under their existing parity rows, rather than
requiring memory-tree (§8 F2); `resolve_compare_base` calls `resolve_remote`, so the ladder block
travels with it. The imports sit outside the `legacy_ledger_py` block, so the block stays
byte-identical: the canonical imports `compute_coverage` from `coverage_join` and
`resolve_compare_base` from `compare_base`, both beside it in `tools/lib/`, and each kit copy imports
both names from its kit's `coverage_join`. Both kits' `include = "**"` file rules already install new
files.

### Inventory

Minted: `tools/lib/legacy_ledger.py`, its two inline copies, `tools/gate-lint/coverage_join.py`, the
block `legacy_ledger_py`, the `[[ledger]]` descriptor table and its govkit registry home, the
`verbatim` registration key, the header grammar, `Registration`,
`read_registrations`, `read_rows`, `write_rows`, `compare_counts`,
`read_renames`, `compare_to_base`, `carry_renames`, the CLI's three verbs and its `--measured` flag,
`check_ledger`, the row-plane parameter of the merge driver's row readers, the audit census value
`ledger-keyed`, the `PARITY_ROWS` row `legacy_ledger_py`, and section `2o`, the first free section of
part 2, unit 27 having landed `2n` in `cc35bb62c`. Naming cells: each function is asked of the
lexicon's `--suggest` under `--as py.function` at the pass.

### Migration

None at landing: no population is converted here. The S9 adapters keep their registries' grammar and
messages byte for byte, which their own self-test arms observe.

### Files touched (estimate)

- `tools/lib/legacy_ledger.py` (new)
- `tools/memory-tree/legacy_ledger.py` (new, inline copy)
- `tools/gate-lint/legacy_ledger.py` (new, inline copy)
- `tools/gate-lint/coverage_join.py` (new, inline copies of the `coverage_join`, `remote_ladder_py`
  and `compare_base_py` blocks)
- `tools/lib/resolve-python.test.sh`
- `tools/memory-tree/merge-rows.py`
- `tools/memory-tree/merge-rows.test.sh`
- `tools/memory-tree/README.md` (the merge driver section, §5's user docs line)
- `tools/gate-lint/sh_hygiene.py`
- `tools/gate-lint/encoding_posture.py`

### Alternatives rejected

- **A central registration list.** It is the hand-typed index retrofit retires; a `[[ledger]]` table
  sits beside the kit's `[[gate_leg]]` rows, where the check that owns the population is declared.
- **The registration in the ledger file alone.** `test.seed` must find a population that is absent,
  so the registration cannot live only inside the file it seeds.
- **A sibling merge driver.** The shape audit's finding
  (`memory/builds/dClosedLoop/reviews/2026-10-18-review-PLAY-dClosedLoop-1-shape-audit-b.md@dbc02df25f04:570`): the
  row-keyed driver and its postconditions already exist, and a second driver duplicates them.
- **The ledger through the table class.** `check_manifest`, `resolve_tables` and `TABLE_ENVELOPE`
  (`tools/memory-tree/merge-rows.py#resolve_tables`, landed after `cdfbd1cf` by
  PLAY-dOrderedCharter-15, -45 and -52) are a whole-file class with its own resolver and its own
  read-back checks. A ledger there is that class's second instance, which owes a factory extracted
  out of `resolve_tables`, and it leaves the four row-plane postconditions S6 extends; the row plane
  with `check_build_backlog`'s `ids` selection serves the ledger as S6 states it.

## 5. Production-readiness checklist

- security — one new write path, `write_rows`, which writes only `<root>/<home>` for a registered
  `home`, atomically. `read_registrations` refuses an absolute home or one holding `..`, the
  validation at the write boundary. This unit's one caller, `carry`, writes only a home already
  tracked, so it creates no file; the admission test for a new home is TOOL-dWitnessedBar-15's,
  run before that unit's first write (§3).
- perf / scale — the reader is linear in rows; `compare_to_base` runs one `git show` and one
  `git diff` per population.
- error / empty / loading states — a malformed row, a bad header and a bad registration are each
  named; no base is unresolved, never green.
- observability — every finding names population, key and direction.
- risks — the TSV class must never catch a markdown index: `check_ledger` requires the header on all
  three blobs, the table class still returns first, and the backlog class keeps its precedence.
- testing — AC1 to AC10 by a pass; the arms of §7 at the close.
- migration — none, as §4 says.
- user docs — none under `help/`: no page describes registries; `tools/memory-tree/README.md`'s merge
  driver section names the ledger class at the pass.

## 6. Acceptance criteria

- **AC1** — When `python legacy_ledger.py read <population>` runs, the canonical file named by its
  absolute path and the working directory a fixture repo under `%TEMP%` holding a `[[ledger]]` table
  and its ledger file, it prints each row and exits 0; with the header's direction changed, a key
  field `42`, or a disposition `done`, it exits 1 naming the line.
  Red when: a header that disagrees with its registration, or a line-number key, reads clean.
- **AC2** — When `python legacy_ledger.py compare <population> --measured <file>` runs in the
  fixture repo, `<file>` measuring a site no row declares and omitting one row's key, it prints
  `undeclared site` and `unmeasured row`, one each; without `--measured` it prints neither, and its
  stderr says the both-ways half was not run.
  Red when: the compare reads one direction only, so a stale row stays green, or a compare given no
  measurement passes silently as if both ways had been read.
- **AC3** — When the fixture's `shrink-only` ledger gains a key on a branch whose merge-base is the
  fixture's `main`, `compare` prints `gained` for it; the same key with disposition
  `widened:<record>` is not printed; the same gain under `declared-set` is not printed; with the
  fixture's remote ref deleted, it prints `unresolved` and the base's reason.
  Red when: a direction other than `shrink-only` refuses a gain, or no base reads green.
  fixture: a bare remote under `%TEMP%` whose `main` the fixture repo has fetched, so
  `resolve_compare_base` resolves; AC4 uses the same one. The tree holds none today; section `2o`
  builds it.
- **AC4** — When a baselined file is `git mv`-ed in the fixture, staged and not committed, and
  `python legacy_ledger.py carry <population>` runs, its rows move to the new path with their
  counts, SHAs and dispositions; then `compare <population> --measured <file>`, `<file>` measuring
  the new path, prints none of `gained`, `unmeasured row` and `undeclared site`. With the home
  untracked, `carry` exits 2 naming the home and leaves the file's bytes unchanged.
  Red when: the rename reads as a drained old key and a gained new one, the base rows are judged on
  their old path, or `carry` writes a home git does not track.
- **AC5** — When `merge-rows.sh` merges a planted ledger conflict in which `%A` and `%B` each append
  a different row, the result holds both rows, the header once, and the audit line's census field
  reads `ledger-keyed` and its verdict `clean`.
  Red when: the TSV rows fall to the structure plane and the append conflicts, or a postcondition
  reading the bullet plane refuses the merge.
- **AC6** — When `merge-rows.sh` merges `%A` lowering a key's count to 2 and `%B` to 3, the result
  holds count 2; when `%A` removes the key and `%B` leaves it as at `%O`, the key is absent.
  Red when: the higher count or the carried row survives the merge.
- **AC7** — When the `legacy_ledger_py` block is cut from `legacy_ledger.py` and from
  `tools/memory-tree/` and `tools/gate-lint/` copies with the parity arm's `blk` awk range, the
  cuts are identical; with one byte changed in the gate-lint copy, they differ.
  Red when: a copy-installed kit's copy drifts unseen.
- **AC8** — When `python tools/gate-lint/sh_hygiene.py memory/project/substitution-fed-loops.txt`
  and `python tools/gate-lint/encoding_posture.py memory/project/encoding-posture-sites.txt` run at
  the pass tip, their stdout and exit codes equal those of the same two commands at the commit the
  pass builds over (the registries and the measured tree have moved since `cdfbd1cf`, so only the
  pass's own parent isolates the adapters).
  Red when: an adapter changes a message, a verdict or the grammar it reads.
- **AC9** — When `python legacy_ledger.py read <population>` runs in a fixture repo under `%TEMP%`
  whose only `[[ledger]]` table for that population sits in the fixture's govkit `registry.toml`,
  no kit descriptor declaring it, it prints each row and exits 0; a second population whose table
  sits in the fixture's scripts/recall/kit.toml, outside the directory holding its other kits, reads
  the same way; with a kit's table declaring the first population's `home` beside it, it exits 2
  naming both tables.
  Red when: `read_registrations` reads only `kit.toml` files, so the population reads as
  unregistered, or reads descriptors under one derived tool root only, so a kit homed elsewhere
  reads as unregistered.
- **AC10** — When the fixture's registration declares `key = "key"`, `fields = ["ref"]` and `verbatim = ["ref"]`
  and its ledger holds a row whose reference is `x.py:120`, `read` prints the row and exits 0; a
  second population in the same fixture with no `verbatim`, holding a `site` key field `120`, exits 1
  naming the line; and a `verbatim` naming a field outside `fields` exits 2 naming the table.
  Red when: `verbatim` is read as a population-wide waiver of the refusal, or a `verbatim` entry the
  registration's `fields` lack is accepted.

## 7. Gates

`shell-hygiene selftest` · `shell hygiene (a loop fed by a command substitution)` · `encoding posture (text IO names its encoding)` · `python resolver (behaviour + inline parity + idiom ban)` · `row-keyed merge driver replay` · `row-driver view refusal` · `check-wiring self-test` · `memory hygiene`

New arm: tools/lib/resolve-python.test.sh · covers AC1 AC2 AC3 AC4 AC7 AC9 AC10 · the `legacy_ledger_py` parity row and section `2o` over a fixture registration, one in a govkit registry and one declaring `verbatim`, staged by one byte changed in the gate-lint copy, by the `shrink-only` predicate cut, by `compare_to_base` judging base rows on their old path, and by the `verbatim` skip widened to every field · that suite's assertion count, raised by the rows
New arm: tools/memory-tree/merge-rows.test.sh · covers AC5 AC6 · the disjoint-appends case on a planted ledger and the concurrent-drain case, staged by `check_ledger` returning false so the TSV rows reach the structure plane, and by `no_row_loss` reading the bullet plane · that suite's case count

## 8. Open questions

- **F1 — Where does a population's registration live?** Options: (a) a `[[ledger]]` table in the
  owning kit's `kit.toml`, beside its `[[gate_leg]]` rows; (b) one central list; (c) the ledger
  file's header alone. (b) is the hand-typed index retrofit retires
  (`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md@5b0cb48caa25:270-272`); (c)
  cannot register an absent population, which `test.seed` seeds. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, with the header a rendered copy the reader compares. widens: none ·
  relaxes: none
- **F2 — How do gate-lint's adapters reach the factory and `compute_coverage`, when gate-lint
  requires no kit?** Options: (a) sibling module copies in gate-lint, each under its parity row;
  (b) `requires = ["memory-tree"]` on gate-lint and imports from memory-tree's copies. (b) changes
  what every gate-lint adopter must install, a public-surface change veto 2 discards. RESOLVED
  (agent, 2026-10-25, delegated): (a), rung 3, the route the clause names ("as every `tools/lib`
  primitive does"). widens: none · relaxes: none
- **F3 — I4 spells the merge class `check_ledger(path)`; how does a path name a ledger whose home is
  declared anywhere?** Options: (a) keep the name, widen the arguments to `(path, lines)` and read
  the rendered header; (b) a path pattern; (c) a second driver attribute. (b) cannot cover homes
  under `tools/` and `memory/project/` alike without matching unrelated files; (c) needs a second
  `merge.<driver>` config that check-wiring would wire. RESOLVED (agent, 2026-10-25, delegated):
  (a), rung 3; the name other units read is kept. widens: none · relaxes: none
- **F4 — How do today's four-field registries ride the factory before TOOL-dWitnessedBar-16
  converts them?** Options: (a) `read_rows` takes a `tail` naming the trailing fields, today's
  `("reason",)` for the adapters; (b) convert the gate-lint registries here. (b) is unit 16's RF-5
  conversion. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the additive form the charter's
  `[core]` rule asks for, its removal unit 16's. widens: none · relaxes: none
- **FACT-QUESTION · F5 — D3: is `compute_coverage` in `tools/lib` at the base?** Probe:
  `git grep -n "def compute_coverage" -- tools`. Observation at `cdfbd1cf`: only
  `tools/codebase-map/map_lib.py@b864fafffc90:1404`, with `resolve_compare_base` at
  `tools/codebase-map/map_lib.py@b864fafffc90:1502`; PLAY-dOrderedCharter-19
  S9's move is DEFERRED to that build's run, which the chain runs before this build's build run.
  Liveness: the probe names `tools/lib/coverage_join.py` once S9 lands. RESOLVED (agent, 2026-10-25,
  delegated): cite S9 as the import, rung 2; the build run re-grounds on the landed module and, if S9
  is still absent there, stops this unit rather than copying `map_lib`'s functions. widens: none ·
  relaxes: none. Re-observed 2026-11-19 at `d08ded6f1`: S9 landed in `9cb93347d`, so the probe names
  `tools/lib/coverage_join.py#compute_coverage` and memory-tree's copy; `resolve_compare_base` sits
  in `tools/lib/compare_base.py#resolve_compare_base` (TOOL-dGroundRules-21 S7), also carried by
  memory-tree's `coverage_join.py` and by `tools/policy/policy.py`. The stop clause does not fire, and
  S4, S8 and §4 import from the two landed modules.
- **F6 — Where does `compare` get the measured counts `compare_counts` takes?** Raised by the first
  builder's return, point 1. Options: (a) `compare --measured <path>`, a file of the rows a seed argv
  prints, read by `read_rows` with `tail=()`, the one parser of that grammar, through which unit
  15's seed verb then reads its argv's stdout; (b) `compare` runs the registration's `seed` through a runner
  built here; (c) no measured half on the CLI, `compare_counts` observed by import only. (b) builds
  the run contract §3 leaves to TOOL-dWitnessedBar-15 §4 and TOOL-dWitnessedBar-51 S32, which veto 1
  discards. (c) leaves AC2 with no command to observe it. RESOLVED (agent, 2026-11-19, delegated):
  (a), the one survivor, a seam unit 15 reuses rather than a runner it re-specifies. widens: none ·
  relaxes: none
- **F7 — How does `read_registrations` find the descriptors at a root that is not gov's checkout?**
  Raised by the first builder's return, point 3. Options: (a) every tracked file named `kit.toml`
  and every tracked `govkit/registry.toml`, at any depth, with no tool root; (b) the one parent of
  every tracked `<dir>/<kit>/kit.toml`, refusing two; (c) govkit's `derive_tool_root`
  (`tools/govkit/govkit.py#derive_tool_root`). (c) keys on a govkit registry, which §4 says no
  copy-installed adopter tracks, and govkit's module travels with neither kit carrying the block,
  so it refuses at every adopter and fails S2. (b) refuses at an adopter that homed one kit
  elsewhere, the case `tools/lib/resolve_kit_dir.py#resolve_kit_dir` names (`scripts/recall/`), and
  fails S2 there. RESOLVED (agent, 2026-11-19, delegated): (a), the one survivor; what it does not
  check is §4's tracked-fixture note. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 13, the brief's shared interface I4,
  scout C's row for cl-0351, `retrofit.md:187-283`, and the sources read at base `cdfbd1cf`.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-51, written by the round-1 spec audit's disposal; nothing else moved.
- rev-3 · 2026-11-19 · §1 §2 §3 §4 §5 §6 §7 §8 §10 · S4 S8 S10 AC8 F5 · re-grounded on the tree at
  `d08ded6f1`: `resolve_compare_base` is imported from `tools/lib/compare_base.py`, and gate-lint's
  `coverage_join.py` carries the three blocks memory-tree's does; the factory's behaviour section is
  `2o`, since `2k` to `2m` are taken and unit 27 takes `2n`; one new parity row, the existing rows
  finding the gate-lint copy by marker; `merge` now dispatches the table class first, named in §4,
  §5 and Alternatives rejected; AC8 compares against the pass's parent, the registries having moved
  since `cdfbd1cf`; citations re-pinned as `path#symbol` or blob-pinned; Files touched gains the
  memory-tree README; per brief 2026-11-19-prompt-TOOL-dWitnessedBar-13-reground-brief.
- rev-4 · 2026-11-19 · §2 §3 §4 §5 §6 §7 §8 §10 · S1 S2 S5 S6 S9 S10 AC1 AC2 AC3 AC4 AC5 AC9 AC10 ·
  the first builder's six points (run `wf_62b9efd5-0fc`) settled at `5e569d9c9`: `compare --measured`
  (F6); AC1 run in the fixture; descriptors read with no tool root (F7); renames span base to
  working tree and re-key the base rows; `carry` writes only a tracked home; the driver's row
  readers take the selected plane. §4 gains "The CLI"; two record citations blob-pinned; per brief
  2026-11-19-prompt-TOOL-dWitnessedBar-13-spec-fix-2-brief.

## 10. Reuse audit

The seams extended are the ones the clause and scout C name, first verified at `cdfbd1cf` and
re-verified at `d08ded6f1`: the count ratchet `tools/gate-lint/sh_hygiene.py#read_registry` and
`tools/gate-lint/sh_hygiene.py#check_registry`, and their twin
`tools/gate-lint/encoding_posture.py#read_registry` and `tools/gate-lint/encoding_posture.py#check_registry`,
both files unchanged since `cdfbd1cf`; the both-ways engine `tools/lib/coverage_join.py#compute_coverage`
and the base `tools/lib/compare_base.py#resolve_compare_base`, which PLAY-dOrderedCharter-19 S9 and
TOOL-dGroundRules-21 S7 landed in `tools/lib/` with memory-tree's `coverage_join.py` carrying both;
the row-keyed driver `tools/memory-tree/merge-rows.py`, its class dispatch
`tools/memory-tree/merge-rows.py#check_build_backlog`, its keyed census
`tools/memory-tree/merge-rows.py#measure_row_classes`, the `ids` parameter of
`tools/memory-tree/merge-rows.py#no_new_duplicates` that selects it, its row predicate
`tools/memory-tree/merge-rows.py#_ROW_RE` and its wiring in `tools/memory-tree/merge-rows.py#merge`;
and the inline-block gate `PARITY_ROWS` in `tools/lib/resolve-python.test.sh`, whose `coverage_join`,
`compare_base_py` and `remote_ladder_py` rows already exist.

Two seams landed after `cdfbd1cf` and are named, not extended. The driver's table class
(`tools/memory-tree/merge-rows.py#check_manifest`, `tools/memory-tree/merge-rows.py#resolve_tables`)
dispatches before the row plane; §4's Alternatives rejected says why the ledger does not ride it. The
policy kit's shrink-only lists (`tools/policy/policy.py#check_list`) read their base through the
same `resolve_compare_base`; the legacy-homes list is TOOL-dWitnessedBar-20's conversion, outside this
unit.

Rev-4 re-verified these at `5e569d9c9` and extends the driver's row readers that split by
`_ROW_RE`, `tools/memory-tree/merge-rows.py#no_row_loss` and
`tools/memory-tree/merge-rows.py#structure_identity` among them. Measured rows reuse `read_rows`.
For finding descriptors no existing seam fits: `tools/govkit/govkit.py#derive_tool_root` needs a
govkit registry and `tools/lib/resolve_kit_dir.py#resolve_kit_dir` finds one named kit (§8 F7);
`reuse_lookup.py "read every tracked kit descriptor kit.toml wherever the kit is homed"` ranks only
generic `read` stems and `resolve_kit_dir`.

The lookup `python tools/codebase-map/reuse_lookup.py "a shrink-only keyed baseline of counted sites compared both ways"`,
re-run at `d08ded6f1`, ranks `resolve_compare_base` (now in `tools/lib/compare_base.py`, memory-tree's
`coverage_join.py` and `tools/policy/policy.py`) and `derive_baseline_additions` as seams and otherwise
generic `key` and `count` stems; it does not rank `read_registry`, which scout C and the clause found.
One disagreement with scout C, kept from rev-1: it places `merge()`'s wiring at
`tools/memory-tree/merge-rows.py@b4a8ac18daa0:1279-1281`, where at `cdfbd1cf` the class test and the
postcondition calls are at `tools/memory-tree/merge-rows.py@b4a8ac18daa0:1283-1288`. The recall probe,
re-run at `d08ded6f1`, returns scout C's row, the systems-retrofit review naming `compute_coverage` as
the engine, and the brief's item for this unit; none disagrees with source beyond the moves above.

Recall terms used: `python tools/memory-recall/query.py "where is the count ratchet for a keyed registry and how are TSV rows merged" --terms "legacy ledger factory shrink-only registry count ratchet read_registry check_registry merge-rows row-keyed driver compute_coverage"`
