# KICK-dKeptSession-33 — the preset store's rule for the derived-default rows: unassigned where v2 restates the default, literal where a preset differs

**Status:** OPEN · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 2 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-33-deviation-331.md](../build/2026-10-26-build-KICK-dKeptSession-33-deviation-331.md) | deviation | — |
| [2026-10-26-review-KICK-dKeptSession-30-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md) | spec-audit | KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-32 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-41 KICK-dKeptSession-44 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build's spec set
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md`)
confirmed finding **id 17 at HIGH**, report item **H2**. Id 2 is the same defect, found by the
coherence lens, and shares the item; it is promoted as `KICK-dKeptSession-34`. The two units split
the item's one fix: this unit is the store's rule, and unit 34 is the reader's answer for a row the
store leaves unassigned.

`KICK-dKeptSession-1` S1 and S2 require every shipped preset to assign every row `never` does not
name, and `standard` to equal each row's literal catalogue default. Eight presettable rows have a
derived default, and v2's preset table spells their cells as prose such as "the role's effort",
which `check_value` refuses. Neither rule can hold for them, and strict's real override of
`maintain.fixes` has no specified spelling. This unit names the eight rows and gives the store one
rule for them. It repairs `KICK-dKeptSession-1` and builds one step after it (order 2).

## 2. Scope (IN)

- **S1** — id 17. The eight rows, named: `roles.effort.<role>`, `roles.effort.<workflow>.<stage>`,
  `roles.effort.default`, `roles.model.<role>.<harness>`, `maintain.fixes`, `review.<stage>`,
  `review.<stage>.effort` and `budgets.*`, each a catalogue row whose `default` is a
  `{derived = …}` table and which v2's never list does not name. The class is computed, never typed:
  `derive_derived_rows(rows, never)` in `tools/policy/presets.py` returns them. Observed by AC1.
- **S2** — id 17. Unassigned where v2 restates the default. A row whose v2 cell is the same prose in
  all four presets, restating its derived default, is assigned in no preset: `roles.effort.<role>`,
  `roles.effort.<workflow>.<stage>`, `roles.effort.default`, `roles.model.<role>.<harness>`,
  `review.<stage>.effort` and `budgets.*` (v2:1512-1515, 1657, 1668). `review.<stage>` is a pattern
  row whose concrete keys `review.design` and `review.build` carry literal cells, so the store assigns
  those keys and never the pattern. Observed by AC1, AC2.
- **S3** — id 17. Literal where a preset differs. `maintain.fixes` is the one derived row whose
  presets differ (v2:1638): each preset assigns a literal set `check_value` admits, the full safe set
  as the catalogue default's six named fixes, split on `, `, for `velocity`, `standard` and
  `guarded`, and `["reap", "regenerate stale"]` for `strict`. Observed by AC3.
- **S4** — id 17. The check. `check_presets` excludes S2's rows from the completeness rule and from
  the standard-equals-default rule, and judges an S3 row's `standard` value against its default's
  named members. It refuses a value spelling a derived default's prose, and any S2 row a preset
  assigns. AC1's count is derived from that rule. Observed by AC1, AC2, AC3.
- **S5** — id 17. `KICK-dKeptSession-1` S1's "assigning every presettable key", S2's two rules and
  AC1's figure of 246 are superseded by name here, and answered in that unit's acceptance ledger with
  AC1's output. Observed by AC1.

## 3. Non-goals (OUT)

- What `policy.py get` answers for an unassigned row: `KICK-dKeptSession-34`, the id 2 half.
- The derived values themselves: their owner builds' readers, dBoundRoles' role efforts and
  dGroundRules' caps among them.
- The report's left-shift arm, every preset value passing `check_value` and no derived row carrying
  its default's prose: S4 is that arm, inside `arm_presets`.

### Edges

- **consumes-from** `KICK-dKeptSession-1` — `presets.toml`, `check_presets` and `arm_presets`, whose completeness and standard-equals-default rules this unit makes hold over the derived-default rows (id 17)
- **hands-off** `KICK-dKeptSession-34` — the unassigned rows of S2, for which the reader's preset step answers None so the derived default reads with source `default`
- **hands-off** `KICK-dKeptSession-32` — the rule for which rows a preset assigns, which decides the rows the scaffold leaves out
- **hands-off** `KICK-dKeptSession-56` — `check_presets`, `derive_derived_rows` and §7's legs, the batch's S7, S31, S41 and S25 (ids 7, 47, 33, 34)

## 4. Design

### Evidence

- At `3c8c4718a` the catalogue holds a `{derived = …}` default on `roles.effort.<role>`,
  `roles.effort.<workflow>.<stage>`, `roles.effort.default`, `roles.model.<role>.<harness>`,
  `maintain.fixes`, `review.<stage>`, `review.<stage>.effort` and `budgets.*`, beside
  `charter.practices`, `floor`, `roles.harness.<role>`, `roles.auth.<role>` and `verdict.remote.pin`,
  which v2's never list names (catalogue read with `tomllib`, 2026-10-26; v2:1430-1437).
- v2's table: "the role's effort" in every column (v2:1512-1513, 1657), "unset" (v2:1514), "the
  role's model on that harness" (v2:1515), "each cap's evidence-derived value" (v2:1668), and
  `maintain.fixes` "the full safe set" except strict's "reap, regenerate stale" (v2:1638).
- `maintain.fixes` is a `set` row with item `.+` and `empty = "allowed"`, so a two-member set passes
  `check_value`; its default names six fixes.
- `review.design` and `review.build` carry literal cells in all four presets (v2's table).

### The store, for S2 and S3

```toml
[preset.strict]
"maintain.fixes" = ["reap", "regenerate stale"]
# no roles.effort.*, roles.model.*, review.<stage>.effort or budgets.* key: S2

[preset.standard]
"maintain.fixes" = ["reap", "prune landed", "regenerate stale", "defer dormant",
                    "records-only fixes", "close finished run records"]
```

### Inventory

| Identifier | Kind | Home |
|---|---|---|
| `derive_derived_rows` | function | `tools/policy/presets.py` |
| `presets-derived` | fixture case | `tools/policy/check_policy.py` |

### Migration

None. No preset store exists before `KICK-dKeptSession-1`.

### Files touched (estimate)

- `tools/policy/presets.toml`: S2 and S3
- `tools/policy/presets.py`: `derive_derived_rows` and S4
- `tools/policy/check_policy.py`: the `presets-derived` case
- `help/policy.md`: one sentence on unassigned rows in the presets section

### Alternatives rejected

- **A literal value per derived row in every preset.** It overrides the evidence-derived caps and
  role efforts in every repository that names a preset, `standard` included.
- **A `{derived = …}` table in the store.** The store would carry prose `check_value` refuses, the
  defect itself.

## 5. Production-readiness checklist

- security — none: the store is read-only data shipped in the kit.
- perf / scale — one pass over the catalogue rows per check.
- error / empty / loading states — a preset assigning an S2 row is a finding naming the preset and
  the key.
- observability — `presets.py check` prints the unassigned count beside the assigned one.
- risks — a derived row added later is classed by S1 automatically and reads unassigned until its
  owner gives the presets literal cells.
- testing — the case of §6 and the arm in §7.
- migration — none.
- user docs — `help/policy.md`.

## 6. Acceptance criteria

- **AC1** — When `python presets.py check` runs in the policy kit, it exits 0 and prints, per preset,
  an assigned count and an unassigned count naming each S2 row and `review.<stage>`.
  Red when: a preset assigns no value to an S2 row and the check reds it as incomplete.
  figure: both counts are DERIVED from the catalogue, `never` and S1's class at each run.
- **AC2** — When the `presets-derived` case plants the value `"each cap's evidence-derived value"`
  on one `budgets.*` key of the census in `strict`, `arm_presets` reds naming `strict` and the key.
  Red when: a derived row carrying its default's prose loads.
- **AC3** — When `python presets.py load strict` runs, `maintain.fixes` reads `reap` and
  `regenerate stale`; for `standard` it reads the six fixes, and the standard-equals-default rule is
  green.
  Red when: strict's override has no literal, or `standard` differs from the default's members.

## 7. Gates

`lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/policy/check_policy.py · covers AC2 · the `presets-derived` case, staged by a planted prose value on a derived row · none

## 8. Open questions

- **F1 — What does the store hold for a row whose default is derived?** Options: (a) nothing where
  v2 restates the default, a literal for every preset where one differs; (b) a literal for every
  preset on every such row; (c) prose. (b) overrides evidence-derived values in every repository.
  (c) fails `check_value`. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the skeptic's
  corrected fix. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's H2 (id 17).
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-56` mirrored, the other ends of
  the edges the round-1 promotions' audit's disposal declared

## 10. Reuse audit

The seam extended is `KICK-dKeptSession-1`'s store and `check_presets`, with dGroundRules'
`check_value` and `read_catalogue_row` (`tools/policy/policy.py` at `3c8c4718a`) for every value.
`python tools/codebase-map/reuse_lookup.py "named policy presets completeness check pair rules"`,
unit 1's probe, ranked name stems only, and the policy kit is not at this base, so no existing seam
in the tree fits; the class is derived from the catalogue's own `derived` default shape.

Recall terms used: `python tools/memory-recall/query.py "how does a preset assign a key whose
default is derived" --terms "preset presets derived default maintain.fixes budgets roles.effort
check_value completeness standard unassigned"`
