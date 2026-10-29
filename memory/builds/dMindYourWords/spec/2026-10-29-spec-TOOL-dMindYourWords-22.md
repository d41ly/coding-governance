# TOOL-dMindYourWords-22 — the debt pin compares only the slice of `lexicon-debt` its own run measures

**Status:** OPEN · rev-2 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |
| [2026-10-29-prompt-TOOL-dMindYourWords-22-1-spec-writer.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-22-1-spec-writer.md) | journal | — |
| [2026-10-29-prompt-TOOL-dMindYourWords-22-promoted-fix-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-22-promoted-fix-brief.md) | research | TOOL-dMindYourWords-24 TOOL-dMindYourWords-27 TOOL-dMindYourWords-29 |
| [2026-10-29-review-TOOL-dMindYourWords-22-to-29-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dMindYourWords-22-to-29-spec-audit-round1.md) | spec-audit | TOOL-dMindYourWords-24 TOOL-dMindYourWords-27 TOOL-dMindYourWords-26 TOOL-dMindYourWords-28 TOOL-dMindYourWords-23 TOOL-dMindYourWords-25 TOOL-dMindYourWords-29 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 1 of `reviews/2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md`, HIGH, which
shares item H1 with id 43 (TOOL-dMindYourWords-23). After TOOL-dMindYourWords-13 lands, the
`lexicon-debt` population holds two slices with two producers: the corpus run measures the code rows
and `--tags` measures the tag rows. `check_debt_pin` compares measured keys with the WHOLE ledger both
ways, so the corpus run prints every tag row as an `unmeasured row`, drained, with the line to delete,
and `--tags` prints every corpus row the same way. This unit gives each row one slice and makes each run
compare its own slice only, so neither run advises deleting the other's debt.

## 2. Scope (IN)

- **S1** — The slice predicate. `derive_ledger_slice(row, registry_rel)` in `tools/lexicon/lexicon.py` returns
  `tags` when the row's `path` field equals `registry_rel` and its `rule` field is `verb` or `noun`,
  else `corpus`. `registry_rel` is the repo-relative path of the namespace registry `--tags` reads,
  located by the same `resolve_kit_dir("playbook", "namespaces.toml", ...)` read PLAY-dOrderedCharter-10
  S7 gives `--tags`, or `None` when no registry resolves, under which every row is `corpus`. One
  predicate, one home: TOOL-dMindYourWords-23's writers call it. Observed by AC1 and AC3.
- **S2** — The scoped compare. `check_debt_pin` takes the slice its caller measured, `corpus` from
  `check_pass` and `tags` from the `--tags` verdict (TOOL-dMindYourWords-13 S2), and filters the ledger
  rows, and the base rows, to that slice before `compare_counts` and `compare_to_base`; `carry_renames`
  runs first, on the whole file, so a renamed registry carries its rows. A row of the other slice is
  never a finding of this run. Observed by AC1, AC2 and AC4.
- **S3** — The population line. Each run that judges the pin prints one line naming its slice and both
  counts, `lexicon: debt slice <slice> · <n> row(s) compared · <m> row(s) held for the other slice`, on
  green and red, so a filter that matched nothing reads as a zero beside its population and never as a
  clean pass. Observed by AC1.
- **S4** — The docs. The debt-ledger section of `tools/lexicon/README.md` (TOOL-dMindYourWords-1 S11)
  states the two slices, their producers and that each run judges its own; `KIT_LEXICON_VERSION` moves
  once. NOT OBSERVED as behaviour: prose has no grader beyond the carriers' own legs.

## 3. Non-goals (OUT)

- What the two writers keep when they rewrite the home: TOOL-dMindYourWords-23, which closes id 43 of
  the same report item with this unit's predicate.
- A second ledger population for tags: TOOL-dMindYourWords-13 §8 F3 rejected it as a second pin, and
  this unit keeps the one population.
- The left-shift lint and selftest arm the report names under H1: a gate is its own unit (BUILD-METHOD
  M2), and no clause of this build names it.
- Changing the row grammar or the key `render_offender_keys` gives a tag finding.

### Edges

- **consumes-from** `TOOL-dMindYourWords-1` — `check_debt_pin`, its call to `compare_counts` and `compare_to_base` after `carry_renames`, and the `lexicon-debt` registration; without it there is no comparison to scope
- **consumes-from** `TOOL-dMindYourWords-13` — the `--tags` verdict that calls `check_debt_pin` and the tag row's key, path the registry and rule `verb` or `noun`; without it there is no second slice
- **hands-off** `TOOL-dMindYourWords-23` — `derive_ledger_slice`, the one predicate by which the `--measure` and `--rebaseline` writers keep the slice they do not measure
- **hands-off** `TOOL-dMindYourWords-37` — `derive_ledger_slice`, `registry_rel`, the held count and AC4's base case, which the minors batch spells POSIX, bounds to the root, keys on the path alone and fixtures with a remote (review ids 9, 14, 15, 31, 32 and 37)

## 4. Design

### Evidence

- Unit 1 makes `check_debt_pin` compare measured keys with the ledger both ways and print an
  `unmeasured row` as drained with the row to delete (`spec/2026-10-29-spec-TOOL-dMindYourWords-1.md`
  §4 "The verdict table"). Unit 13 keys a tag finding `<registry path>\t<verb|noun>\t<tag>` and judges it
  through the same `check_debt_pin` (`spec/2026-10-29-spec-TOOL-dMindYourWords-13.md` S2, §8 F5).
  Neither limits the comparison by slice (review ids 1 and 43, confirmed).
- The registry `tools/playbook/namespaces.toml` is a `.toml` file and `toml` is a `dark` extension of
  this repository's `LANGS` (`.lexicon.conf:24`), so the corpus walk extracts no definition from it and
  no corpus offender carries its path. The rule test is kept anyway, because an adopter may arm an
  extension gov leaves dark.
- `resolve_kit_dir` takes `here` logically and never calls `resolve()` (`tools/lib/resolve_kit_dir.py`,
  the canonical block), so the registry path the corpus run computes equals the one `--tags` reads.

### The flow

```
rows      = read_rows(home)                       # whole file
rows      = carry_renames(root, reg, base)        # whole file, before any filter
reg_rel   = registry path, or None
mine      = [r for r in rows if derive_ledger_slice(r, reg_rel) == slice]
base_mine = [r for r in base_rows if derive_ledger_slice(r, reg_rel) == slice]
findings  = compare_counts(measured, mine) + compare_to_base(mine, base_mine)
print(f"lexicon: debt slice {slice} · {len(mine)} row(s) compared · {len(rows) - len(mine)} row(s) held for the other slice")
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_ledger_slice` | function, `tools/lexicon/lexicon.py` | `py.function`; `lexicon.py --suggest derive_ledger_slice --as py.function` answered `OK` at writing |
| `corpus`, `tags` | slice values | none |

### Migration

None. The ledger's bytes do not change; only which rows each run reads as its own.

### Rollout

Live at landing. Before it, the defect is live only between TOOL-dMindYourWords-13's landing and this
unit's, the two builds of one order apart; the build lands both together.

### Files touched (estimate)

- `tools/lexicon/lexicon.py`: S1, S2, S3, `KIT_LEXICON_VERSION`
- `tools/lexicon/selftest.py`: the arm of §7
- `tools/lexicon/README.md`: S4

### Alternatives rejected

- **A slice marker in the row**, a rule `tag.verb`: it changes the key unit 13 §8 F5 settled and the I4
  rule values, and would migrate every seeded tag row; the registry path already marks the slice.
- **Folding the tag findings into the corpus run**, so one run measures every row (the report's third
  route): the tags reach `--tags` on stdin from the core's one call per run (PLAY-dOrderedCharter-10
  S6), and the corpus run has no tag set to measure.
- **A second `[[ledger]]` population for tags**: a second pin, refused by unit 13 §8 F3.

## 5. Production-readiness checklist

- security — read-only over the committed ledger; no new write path.
- perf / scale — one pass over about 1,200 rows per run, one extra resolver call for the registry path.
- error / empty / loading states — no registry resolves: every row is `corpus` and `--tags` is not
  installed, the parent's slot line; an empty slice prints `0 row(s) compared` beside its held count.
- observability — S3's line on every judging run, green and red.
- risks — a tag row whose registry moved without `git mv` reads as `corpus` in the old path; the
  corpus run then prints it drained, which is true, since no tag run can measure it there.
- testing — AC1 to AC4 and the arm of §7.
- migration — none.
- user docs — `tools/lexicon/README.md` (S4).

## 6. Acceptance criteria

- **AC1** — When `python tools/lexicon/lexicon.py` runs in a fixture repository whose ledger holds one
  live corpus row and one live tag row, it exits 0, prints `lexicon: debt slice corpus · 1 row(s)
  compared · 1 row(s) held for the other slice`, and prints no `drained` line naming the tag row.
  Red when: the corpus run reads the tag row as an `unmeasured row`, or the held count is absent.
  fixture: a scratch repository under `%TEMP%`, a planted `namespaces.toml` and ledger.
- **AC2** — When the same fixture runs `printf '<the tag>\n' | python tools/lexicon/lexicon.py --tags`,
  it exits 0 and prints no `drained` line naming the corpus row.
  Red when: the tags run reads a corpus row as drained.
- **AC3** — When the fixture's tag is renamed so `--tags` no longer measures it, the `--tags` run prints
  that tag row drained with the line to delete, and the corpus run still names it nowhere.
  Red when: the slice filter hides the tag slice from its own run, so a real drain goes unseen.
- **AC4** — When the fixture's branch adds a tag row to the ledger over its base, the corpus run names
  no `gained` finding for it, and the `--tags` run judges it.
  Red when: the base half compares across slices.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `codebase-map kit selftest` · `kit version markers`

New arm: tools/lexicon/selftest.py · covers AC1 AC2 AC3 AC4 · a fixture ledger holding one corpus row and one tag row, its failing case `check_debt_pin` called with the slice filter cut out, under which AC1's run prints the tag row drained · none

## 8. Open questions

- **F1 — Which producer owns each row of the shared population?** Options: (a) a slice per row, decided
  by the registry path and the rule, each run comparing its own; (b) a second population for tags;
  (c) the corpus run measuring every row. (b) is the second pin unit 13 §8 F3 refused, and (c) has no
  tag set to measure. RESOLVED (agent, 2026-10-29, delegated): (a), rung 3, the report's first route
  and the only survivor of veto 1. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 1 (HIGH, item H1) of the round-1 spec
  audit; the writer half of the item is TOOL-dMindYourWords-23.
- rev-2 · 2026-10-29 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 audit of units 22 to 29
  declare toward this unit (TOOL-dMindYourWords-37); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is TOOL-dMindYourWords-1's `check_debt_pin`, which already wraps the factory's
`compare_counts` and `compare_to_base`; the slice is a filter in front of them, not a second compare.
`python tools/codebase-map/reuse_lookup.py "keep the rows another producer owns when rewriting a shared
ledger file"` ranked name-stem helpers (`rows`, `row`, `extract_row`, `owners_of`) and no function that
partitions a ledger by producer, so no existing seam fits the partition itself; the registry path comes
from the `resolve_kit_dir` read PLAY-dOrderedCharter-10 S7 adds to the same engine. The recall probe
surfaced the round-1 report item H1 and unit 13's Migration, which agree with this reading.

Recall terms used: `python tools/memory-recall/query.py "how does the lexicon debt ledger keep its rows when tag findings and corpus findings share one population" --terms "lexicon-debt ledger drain measure rebaseline tags slice check_debt_pin widened shallow provenance"`
