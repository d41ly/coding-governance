# TOOL-dWitnessedBar-13 — retrofit's baseline ledger factory in `tools/lib`

**Status:** OPEN · rev-1 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 3 · advances TOOL-dWitnessedBar-31

**Carries:** cl-dClosedLoop-0351@d6eaa553 whole
**Carries:** node:system.retrofit

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-c.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-c.md) | research | TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-fix-return.md) | research | TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-28 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-fix-brief.md) | research | TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 |

<!-- /gen:spec-records -->

## 1. Goal

Give every population a check tolerates one primitive: a ledger file per population, registered with
its key kind, drain, direction and home, read and compared by one factory, carried across a rename
and merged by row. Today gov holds 28 registries in at least six grammars and writes the count
ratchet twice, in `sh_hygiene.py` and `encoding_posture.py` (gap-test-14).

## 2. Scope (IN)

- **S1** — The canonical factory block `# >>> legacy_ledger_py` in `tools/lib/legacy_ledger.py`,
  holding the registration record, the row grammar and reader, the atomic writer, the four
  directions, the both-ways compare and the base compare of §4. Observed by AC1, AC2, AC3 and AC4.
- **S2** — The registration: a `[[ledger]]` table in the owning kit's `kit.toml`, declaring
  `population`, `seed`, `key`, `fields`, `drain`, `direction`, `home` and `leg`, and optionally
  `verbatim` (S11), read by `read_registrations(root)`. A population no kit descriptor owns, one a
  repository-root tool reads or the step rows, registers as a `[[ledger]]` table in
  `tools/govkit/registry.toml`, which `read_registrations` reads beside the descriptors (the reads
  TOOL-dWitnessedBar-16 §8 F3 and TOOL-dWitnessedBar-18 §8 F2 make). The derived index of populations
  is that function's output, never a typed list. Observed by AC1 and AC9.
- **S3** — Each ledger file opens with a header line rendered from its registration, which the
  reader compares with the registration both ways. Observed by AC1.
- **S4** — The both-ways arm calls `compute_coverage` and the base is `resolve_compare_base`, both
  imported from PLAY-dOrderedCharter-19 S9's `coverage_join` module (D3). The factory adds the count
  compare and the direction predicates around them. Observed by AC2 and AC3.
- **S5** — Rename carry: `carry_renames(root, reg, base)` re-keys every `site` row whose path
  `git diff -M --name-status <base>..HEAD` renamed, keeping count, SHA and disposition; a rename
  alone is neither a gain nor a drain. Observed by AC4.
- **S6** — The ledger merge class in `tools/memory-tree/merge-rows.py`: `check_ledger` beside
  `check_build_backlog`, a per-path row predicate and the factory's row key, the merge rule
  "drained beats carried, the lower count wins", and the postconditions `no_new_duplicates`,
  `no_misfiled_rows`, `no_row_loss` and `structure_identity` extended to it. Driven through
  `merge-rows.sh` and the existing `merge=rows` attribute. Observed by AC5 and AC6.
- **S7** — `merge-rows.test.sh` runs its append-collision case, "disjoint appends", on a planted
  ledger conflict, and a concurrent-drain case beside it. Observed by AC5 and AC6.
- **S8** — The copy-install route: inline module copies `tools/memory-tree/legacy_ledger.py` and
  `tools/gate-lint/legacy_ledger.py`, plus `tools/gate-lint/coverage_join.py` carrying PLAY-dOrderedCharter-19 S9's block,
  each held by a `PARITY_ROWS` row of `tools/lib/resolve-python.test.sh`, which also gains a
  behaviour section `2l` for the factory. Observed by AC7.
- **S9** — The count ratchet's second instance: `check_registry` and `read_registry` in
  `tools/gate-lint/sh_hygiene.py` and `tools/gate-lint/encoding_posture.py` become thin adapters over
  the factory's `read_rows` and `compare_counts`, each keeping its messages and its four-field
  `reason` grammar until TOOL-dWitnessedBar-16 converts its registry. Observed by AC8.
- **S10** — A CLI on the canonical file, `python legacy_ledger.py read|compare|carry <population>`,
  run in the repository it is invoked from, printing one finding per line and exiting 1 on any
  finding, 0 on none, 2 on a refusal. It is how a pass and section `2l` observe the factory.
  Observed by AC1, AC2, AC3 and AC4.
- **S11** — The line-number refusal's declared exception: a registration's `verbatim = [<field>]`
  names key fields whose text is the tracked subject, such as a `file:line` positional reference, so
  `read_rows` stores them as written and refuses a line-number shape in every other field and every
  other population (the read TOOL-dWitnessedBar-18 §8 F1 makes). Observed by AC10.

## 3. Non-goals (OUT)

- Converting any of gov's 28 registries, the pins or the cutoffs, and the readers those conversions
  owe: TOOL-dWitnessedBar-16, -17, -18 and -20.
- `test.seed`, the seed verb and unarmed reporting: TOOL-dWitnessedBar-15.
- The `ratchet` pack's legs, the widen records and `retrofit.widen`: TOOL-dWitnessedBar-14. This
  unit names what a direction refuses; the pack decides what a refusal costs.
- The touch join and a hunk drain: `build.scope`'s, dScopedBuild's.
- Moving `compute_coverage` and `resolve_compare_base`: PLAY-dOrderedCharter-19 S9's (D3).
- A second merge driver, or a new `.gitattributes` line: no ledger exists at landing; each converting
  unit adds its file's `merge=rows` line.
- The `ledger` record kind and the census kinds: dTotalRecall's.

### Edges

- **hands-off** `TOOL-dWitnessedBar-15` — `legacy_ledger.py`, the factory whose registration and
  atomic writer `test.seed` seeds through
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
- **consumes-from** external — PLAY-dOrderedCharter-19 S9's `coverage_join` module with
  `compute_coverage` and `resolve_compare_base`; without it the both-ways arm and the base have no
  shared engine

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

`read_registrations(root)` reads every tracked `kit.toml` under the tool root, and the `[[ledger]]`
tables of `<tool root>/govkit/registry.toml` where that file is tracked, and returns one
`Registration` per table, refusing a table missing a field, a value outside its closed set, a
`verbatim` entry not in its `fields`, or two tables with one `home` wherever each sits. The govkit
registry is the home for a population no descriptor owns: govkit carries no `kit.toml`, and
`load_registry` (`tools/govkit/govkit.py:247`) reads only its own tables, so a `[[ledger]]` table
beside them changes nothing it reads. A repository with no tracked govkit registry, which is every
copy-installed adopter, registers through its descriptors alone. `seed` may be `[]`, a check with no seed, which TOOL-dWitnessedBar-15 reports
unarmed; whether a `home` is one the target's hygiene check admits is that unit's seed-time test.
The derived index of populations is this list. A registration keyed to a leg by `leg` is how
`test.seed` (unit 15) finds the check to seed at a leg's row.

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
| `read_rows(path, arity, tail=("sha", "disposition"), verbatim=())` | `(rows, malformed)`; `tail=("reason",)` reads today's four-field registries for this unit's S9 adapters; `verbatim` holds the field positions the line-number refusal skips |
| `write_rows(path, reg, rows)` | writes header and rows through a sibling temp file and `os.replace`, so a run that dies leaves the old file or the new one, never half of either |
| `compare_counts(measured, declared, direction)` | one finding per key: `unmeasured row`, `undeclared site`, `count rose`, `count fell`; the both-ways key sets come from `compute_coverage` with no owners, its `unclaimed` and `stale_baseline` fields |
| `compare_to_base(root, reg)` | the rows at `resolve_compare_base(root)`'s SHA beside the working rows, judged by the direction, or `None` and the base's own reason |
| `carry_renames(root, reg, base)` | the rows with each renamed path re-keyed, and the `(old, new)` pairs it applied |

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
(`retrofit.md:440-442`).

### The merge class

`check_ledger(path, lines)` is true when the first line of each of `%O`, `%A` and `%B` is a ledger
header for one population; headers that disagree raise `StructureDrift`. A ledger's home is
declared, not path-shaped, so the class reads the header the factory wrote rather than a path
pattern (§8 F3). Under the class:

- the row predicate is every line that is neither blank nor `#`, replacing `_ROW_RE`'s bullet test
  for that file;
- the row key is the line's first `arity` TAB fields, `arity` read from the header;
- `resolve_rows` takes the ledger rule: a key one side removed and the other left as at `%O` is
  removed (drained beats carried); a key both sides changed takes the lower count with that side's
  SHA and disposition; equal counts with different SHA or disposition are a conflict region;
- `no_new_duplicates` keys by the ledger key, and the other three postconditions run unchanged over
  the written bytes.

A ledger's `.gitattributes` line is `<home> merge=rows`, the attribute the authored indexes already
carry, so `merge-rows.sh` and check-wiring's `check_merge_rows` (`tools/check-wiring.sh:1221`) need
no second driver.

### The copy-install route

`tools/lib/` ships nothing, so two kits carry the block as a sibling module: memory-tree, whose
`merge-rows.py` reads the header and key, and which codebase-map, drift-audit and the later
converting kits already `require`; and gate-lint, which requires nothing (`tools/gate-lint/kit.toml:7`),
for this unit's S9 adapters. gate-lint also carries PLAY-dOrderedCharter-19 S9's `coverage_join` block as a sibling module under that
block's own parity row, rather than requiring memory-tree (§8 F2). Both kits' `include = "**"` file
rules already install new files.

### Inventory

Minted: `tools/lib/legacy_ledger.py`, its two inline copies, `tools/gate-lint/coverage_join.py`, the
block `legacy_ledger_py`, the `[[ledger]]` descriptor table and its govkit registry home, the
`verbatim` registration key, the header grammar, `Registration`,
`read_registrations`, `read_rows`, `write_rows`, `compare_counts`, `compare_to_base`,
`carry_renames`, `check_ledger`, the `PARITY_ROWS` rows `legacy_ledger_py` and the gate-lint row of
`coverage_join`, and section `2l`. Naming cells: each function is asked of the lexicon's
`--suggest` under `--as py.function` at the pass.

### Migration

None at landing: no population is converted here. The S9 adapters keep their registries' grammar and
messages byte for byte, which their own self-test arms observe.

### Files touched (estimate)

- `tools/lib/legacy_ledger.py` (new)
- `tools/memory-tree/legacy_ledger.py` (new, inline copy)
- `tools/gate-lint/legacy_ledger.py` (new, inline copy)
- `tools/gate-lint/coverage_join.py` (new, inline copy of PLAY-dOrderedCharter-19 S9's block)
- `tools/lib/resolve-python.test.sh`
- `tools/memory-tree/merge-rows.py`
- `tools/memory-tree/merge-rows.test.sh`
- `tools/gate-lint/sh_hygiene.py`
- `tools/gate-lint/encoding_posture.py`

### Alternatives rejected

- **A central registration list.** It is the hand-typed index retrofit retires; a `[[ledger]]` table
  sits beside the kit's `[[gate_leg]]` rows, where the check that owns the population is declared.
- **The registration in the ledger file alone.** `test.seed` must find a population that is absent,
  so the registration cannot live only inside the file it seeds.
- **A sibling merge driver.** The shape audit's finding (`2026-10-18 shape-audit-b:570`): the
  row-keyed driver and its postconditions already exist, and a second driver duplicates them.

## 5. Production-readiness checklist

- security — one new write path, `write_rows`, which writes only a registration's declared `home`
  after the hygiene admission test, atomically.
- perf / scale — the reader is linear in rows; `compare_to_base` runs one `git show` per population.
- error / empty / loading states — a malformed row, a bad header and a bad registration are each
  named; no base is unresolved, never green.
- observability — every finding names population, key and direction.
- risks — the TSV class must never catch a markdown index: `check_ledger` requires the header on all
  three blobs, and the backlog class keeps its precedence.
- testing — AC1 to AC10 by a pass; the arms of §7 at the close.
- migration — none, as §4 says.
- user docs — none under `help/`: no page describes registries; `tools/memory-tree/README.md`'s merge
  driver section names the ledger class at the pass.

## 6. Acceptance criteria

- **AC1** — When `python legacy_ledger.py read <fixture>` runs from `tools/lib/` over a fixture repo
  under `%TEMP%` holding a `[[ledger]]` table and its ledger file, it prints each row and exits 0;
  with the header's direction changed, a key field `42`, or a disposition `done`, it exits 1 naming
  the line.
  Red when: a header that disagrees with its registration, or a line-number key, reads clean.
- **AC2** — When `python legacy_ledger.py compare <population>` runs in the fixture repo with a site
  measured that no row declares and a row no measurement finds, it prints `undeclared site` and
  `unmeasured row`, one each.
  Red when: the compare reads one direction only, so a stale row stays green.
- **AC3** — When the fixture's `shrink-only` ledger gains a key on a branch whose merge-base is the
  fixture's `main`, `compare` prints `gained` for it; the same key with disposition
  `widened:<record>` is not printed; the same gain under `declared-set` is not printed; with the
  fixture's remote ref deleted, it prints `unresolved` and the base's reason.
  Red when: a direction other than `shrink-only` refuses a gain, or no base reads green.
- **AC4** — When a baselined file is `git mv`-ed in the fixture and
  `python legacy_ledger.py carry <population>` runs, its rows move to the new path with their counts, SHAs and dispositions, and
  `compare` prints no gain and no drain.
  Red when: the rename reads as a drained old key and a gained new one.
- **AC5** — When `merge-rows.sh` merges a planted ledger conflict in which `%A` and `%B` each append
  a different row, the result holds both rows, the header once, and the audit line reads `clean`.
  Red when: the TSV rows fall to the structure plane and the append conflicts.
- **AC6** — When `merge-rows.sh` merges `%A` lowering a key's count to 2 and `%B` to 3, the result
  holds count 2; when `%A` removes the key and `%B` leaves it as at `%O`, the key is absent.
  Red when: the higher count or the carried row survives the merge.
- **AC7** — When the `legacy_ledger_py` block is cut from `legacy_ledger.py` and from
  `tools/memory-tree/` and `tools/gate-lint/` copies with the parity arm's `blk` awk range, the
  cuts are identical; with one byte changed in the gate-lint copy, they differ.
  Red when: a copy-installed kit's copy drifts unseen.
- **AC8** — When `python tools/gate-lint/sh_hygiene.py memory/project/substitution-fed-loops.txt`
  and `python tools/gate-lint/encoding_posture.py memory/project/encoding-posture-sites.txt` run at
  the pass tip, their stdout and exit codes equal those at the base `cdfbd1cf`.
  Red when: an adapter changes a message, a verdict or the grammar it reads.
- **AC9** — When `python legacy_ledger.py read <population>` runs in a fixture repo under `%TEMP%`
  whose only `[[ledger]]` table for that population sits in the fixture's govkit `registry.toml`,
  no kit descriptor declaring it, it prints each row and exits 0; with a kit's table declaring the
  same `home` beside it, it exits 2 naming both tables.
  Red when: `read_registrations` reads only `kit.toml` files, so the population reads as
  unregistered.
- **AC10** — When the fixture's registration declares `fields = ["ref"]` and `verbatim = ["ref"]`
  and its ledger holds a row whose reference is `x.py:120`, `read` prints the row and exits 0; a
  second population in the same fixture with no `verbatim`, holding a `site` key field `120`, exits 1
  naming the line; and a `verbatim` naming a field outside `fields` exits 2 naming the table.
  Red when: `verbatim` is read as a population-wide waiver of the refusal, or a `verbatim` entry the
  registration's `fields` lack is accepted.

## 7. Gates

`shell-hygiene selftest` · `shell hygiene (a loop fed by a command substitution)` · `encoding posture (text IO names its encoding)` · `python resolver (behaviour + inline parity + idiom ban)` · `row-keyed merge driver replay` · `row-driver view refusal` · `check-wiring self-test` · `memory hygiene`

New arm: tools/lib/resolve-python.test.sh · covers AC1 AC2 AC3 AC4 AC7 AC9 AC10 · the `legacy_ledger_py` parity row and section `2l` over a fixture registration, one in a govkit registry and one declaring `verbatim`, staged by one byte changed in the gate-lint copy, by the `shrink-only` predicate cut and by the `verbatim` skip widened to every field · that suite's assertion count, raised by the rows
New arm: tools/memory-tree/merge-rows.test.sh · covers AC5 AC6 · the disjoint-appends case on a planted ledger and the concurrent-drain case, staged by `check_ledger` returning false so the TSV rows reach the structure plane · that suite's case count

## 8. Open questions

- **F1 — Where does a population's registration live?** Options: (a) a `[[ledger]]` table in the
  owning kit's `kit.toml`, beside its `[[gate_leg]]` rows; (b) one central list; (c) the ledger
  file's header alone. (b) is the hand-typed index retrofit retires (`retrofit.md:267-269`); (c)
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
  `tools/codebase-map/map_lib.py:1404`, with `resolve_compare_base` at `:1502`; PLAY-dOrderedCharter-19
  S9's move is DEFERRED to that build's run, which the chain runs before this build's build run.
  Liveness: the probe names `tools/lib/coverage_join.py` once S9 lands. RESOLVED (agent, 2026-10-25,
  delegated): cite S9 as the import, rung 2; the build run re-grounds on the landed module and, if S9
  is still absent there, stops this unit rather than copying `map_lib`'s functions. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 13, the brief's shared interface I4,
  scout C's row for cl-0351, `retrofit.md:187-283`, and the sources read at base `cdfbd1cf`.

## 10. Reuse audit

The seams extended are the ones the clause and scout C name, each verified at `cdfbd1cf`: the count
ratchet `read_registry` and `check_registry` at `tools/gate-lint/sh_hygiene.py:402` and `:462`, and
their twin at `tools/gate-lint/encoding_posture.py:165` and `:205`; the both-ways engine
`compute_coverage` (`tools/codebase-map/map_lib.py:1404`) and the base `resolve_compare_base`
(`:1502`), through PLAY-dOrderedCharter-19 S9's move; the row-keyed driver
`tools/memory-tree/merge-rows.py`, its class dispatch `check_build_backlog` (`:498`), its keyed
census `measure_row_classes` (`:508`), its row predicate `_ROW_RE` (`:402`) and its wiring in `merge`
(`:1283-1288`); and the inline-block gate `PARITY_ROWS` (`tools/lib/resolve-python.test.sh:168`).
The lookup `python tools/codebase-map/reuse_lookup.py "a shrink-only keyed baseline of counted sites"`
with the words `compared both ways` appended ranked `derive_baseline_additions` and `resolve_compare_base` as seams and otherwise
generic `key` and `count` stems; it did not rank `read_registry`, which scout C and the clause found.
One disagreement with scout C: it places `merge()`'s wiring at `:1279-1281`; at `cdfbd1cf` the
class test and the postcondition calls are at `merge-rows.py:1283-1288`. The recall probe returned scout C's row, the
systems-retrofit review naming `compute_coverage` as the engine, and the shape audit's finding that
the driver exists; none disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "where is the count ratchet for a keyed registry and how are TSV rows merged" --terms "legacy ledger factory shrink-only registry count ratchet read_registry check_registry merge-rows row-keyed driver compute_coverage"`
