# TOOL-dTrueNorth-12 — the routed-commits self-test reaches the strip through a resolver and builds its own design in the fixture

**Status:** CLOSED · rev-4 · 2026-10-22 · node d · Tier-2 · base 271aa59d · streams tooling · order 4

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-21-build-TOOL-dTrueNorth-12-deviation-11.md](../build/2026-10-21-build-TOOL-dTrueNorth-12-deviation-11.md) | deviation | — |
| [2026-10-21-build-TOOL-dTrueNorth-12-ledger.md](../build/2026-10-21-build-TOOL-dTrueNorth-12-ledger.md) | journal | — |
| [2026-10-22-build-TOOL-dTrueNorth-12-deviation-21.md](../build/2026-10-22-build-TOOL-dTrueNorth-12-deviation-21.md) | deviation | — |
| [2026-10-21-prompt-TOOL-dTrueNorth-12-build-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-12-build-brief.md) | journal | — |
| [2026-10-22-prompt-TOOL-dTrueNorth-12-1-spec-writer.md](../prompts/2026-10-22-prompt-TOOL-dTrueNorth-12-1-spec-writer.md) | journal | — |
| [2026-10-22-prompt-TOOL-dTrueNorth-12-divergence-brief.md](../prompts/2026-10-22-prompt-TOOL-dTrueNorth-12-divergence-brief.md) | research | — |
| [2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md](../reviews/2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md) | spec-audit | TOOL-dTrueNorth-8 TOOL-dTrueNorth-9 TOOL-dTrueNorth-10 TOOL-dTrueNorth-11 TOOL-dTrueNorth-13 TOOL-dTrueNorth-14 TOOL-dTrueNorth-15 TOOL-dTrueNorth-16 |
| [2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md](../reviews/2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md) | diff-review | TOOL-dTrueNorth-1 TOOL-dTrueNorth-2 TOOL-dTrueNorth-3 TOOL-dTrueNorth-4 TOOL-dTrueNorth-5 TOOL-dTrueNorth-6 TOOL-dTrueNorth-7 TOOL-dTrueNorth-8 TOOL-dTrueNorth-9 TOOL-dTrueNorth-10 TOOL-dTrueNorth-11 TOOL-dTrueNorth-13 TOOL-dTrueNorth-14 TOOL-dTrueNorth-15 TOOL-dTrueNorth-16 TOOL-dTrueNorth-17 TOOL-dTrueNorth-18 TOOL-dTrueNorth-19 TOOL-dTrueNorth-20 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dTrueNorth/reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md`)
confirmed finding **id 30 at HIGH**, its item **H5**. Through `deviation_join.py`,
`routed_commits.py --selftest` reads three things outside the leg's guard and outside an adopter's
tree: `GEN_REGION_AWK` from `tools/unattended/lib-unattended.sh`, the live tree's `DESIGN_RECORD`
`[chain]` section, and its `DESIGN_VIEW`. The leg is guarded on `{prefix}/lib/` and
`{prefix}/memory-tree/` only and ships to adopters, and `TOOL-dTrueNorth-7` edits the library in this
same build. An edit to the library alone skips the leg or reuses its earlier green, and an adopter
without the unattended kit or gov's records runs a shipped self-test that cannot build its fixture.
This unit takes the skeptic's corrected fix: the strip is reached through a resolver a test can
replace, a missing kit is a named skip of the plants that read the strip, the fixture builds a small
design of its own, and the leg's guard names the library. It repairs `TOOL-dTrueNorth-4`. The second
self-test that copies gov's live design, `TOOL-dTrueNorth-6`'s, is the same class at MEDIUM, id 42
(item M16), batched into `TOOL-dTrueNorth-16`.

## 2. Scope (IN)

- **S1** — `read_gen_region_awk(resolve=None)` in `tools/memory-tree/deviation_join.py` returns the
  value of the `GEN_REGION_AWK=` assignment in the unattended kit's `lib-unattended.sh`, the kit found
  by `backlog.resolve_kit_dir("unattended", "lib-unattended.sh", <this kit's directory>)` or by the
  `resolve` callable a caller injects, the shape `read_landed_unclosed` takes. The value is read from
  the file, never copied into the module. `read_gen_strip`, which today resolves the kit itself with
  no resolver a caller can inject (`tools/memory-tree/deviation_join.py:314`), reads the value
  through it. This supersedes `TOOL-dTrueNorth-4` S4's fixed path to
  `tools/unattended/lib-unattended.sh`. Observed by AC2.
- **S2** — The unresolved kit, two readings, and one strip in force per process. In the live join
  with the `DESIGN_*` keys declared, a kit that does not resolve is a refusal naming it, exit 2,
  because a population read without the strip would count status-only revisions as members. The
  resolution moves up front: today `read_gen_strip` runs only from `extract_authored`
  (`tools/memory-tree/deviation_join.py:334`), so only once a revision is graded; it moves to the
  first act of `read_population`, before `DESIGN_VIEW` is read (`:407`). The CLI's armed join and the
  host's `read_host_lines` both enter there, so each refuses on an unresolved kit whatever the
  history holds: the CLI exits 2, the host raises its `Refusal`, exit 2. Under `--fixture` and in
  the host's self-test, it is one line, `deviation: SKIP — the unattended kit does not resolve, so
  the plants that read the generated-region strip are not run: <reason> · <plants>`, and every other
  plant runs under the strip stubbed to the identity. The plants named are those whose verdict reads
  the strip: `status-only`, `header-rev`, `gen`, `status-gen` and `gen-text` (`TOOL-dTrueNorth-4`
  AC5), and any further plant whose verdict changes when the strip is stubbed to the identity, which
  the pass finds by running every plant so stubbed.
  The identity is installed on the module, as the strip `read_gen_strip` returns, by the fixture's
  two entry points, `run_fixture` and `run_plant_arms`, for the length of their call, and restored,
  its cache cleared, in their `finally`; it is never an argument to `measure_fixture`. The
  `record-late` arm (`tools/memory-tree/deviation_join.py:1196-1199`) reaches the join through the
  host, `routed_commits.check_routed_commits`, whose `check_deviation_join` imports this same module
  (`tools/memory-tree/routed_commits.py:346`, the module aliasing itself at
  `tools/memory-tree/deviation_join.py:660` when run as a script), enters `read_population` through
  `read_host_lines`, and turns its `Unmeasured` into the host's `Refusal` (`routed_commits.py:352-353`).
  So that live host path reads the identity the skip installed, as `--fixture --host routed-commits`
  does (`deviation_join.py:1097`), and once the entry point returns, a live join in the same process
  refuses again. Observed by AC1 and AC7.
- **S3** — The fixture's design is its own. `build_design_fixture(repo)` writes, in the fixture's pin
  commit, a design record whose `[chain]` section holds two fixture builds, `dFixA` and `dFixB`, with
  one clause per clause-moving role, eleven at HEAD, so that each role moves its own clause and no
  other role's, as `TOOL-dTrueNorth-4` §4 "The fixture" requires for plants to compose; and the view
  of it in the as-built row grammar, one row per clause. Both come from constants in the module, each
  clause id written once in the role map §4 "The fixture design" tables; the second commit and the
  clause-move plants edit those. Nothing reads the live tree's `DESIGN_RECORD` or `DESIGN_VIEW`.
  The join's chain builds are the view's Build column (`deviation_join.py:407`), so a spec outside
  them is no chain-build spec: the fixture's units, `RUN.md` and records move from
  `memory/builds/dTrueNorth/` to the fixture build folder `memory/builds/dFixA/`, as §4 states. The
  self-test gains one arm over the composed run, every plant but `unmeasured`: its member count is
  the fixture's own count, the base's `BASE_MEMBERS` plus each plant's own increment read from the
  single-plant builds `run_plant_arms` already measures, and its only late member is the
  `record-late` plant's. This supersedes `TOOL-dTrueNorth-4` §4 "The fixture"'s "the tree's
  `DESIGN_RECORD` `[chain]` section and its `DESIGN_VIEW` file copied in whole, never a synthetic
  chain". Observed by AC3 and AC6.
- **S4** — In `tools/gate-legs.json`, the `routed-commits selftest` guard gains
  `{prefix}/unattended/lib-unattended.sh`. Observed by AC4.
- **S5** — The dependency S2 refuses on is declared where the kit declares its conditional siblings:
  one `requires_if` row in `tools/memory-tree/kit.toml` naming the kit `unattended` when any of
  `DESIGN_RECORD`, `DESIGN_BASELINE` or `DESIGN_VIEW` is set, its `why` naming the strip the live join
  reads and the fixture's named skip. Like the rows beside it, it selects no kit and installs nothing.
  Observed by AC5.

## 3. Non-goals (OUT)

- `TOOL-dTrueNorth-6`'s fixture, which copies the live design the same way: `TOOL-dTrueNorth-16`'s
  item for id 42, which reuses S3's builder.
- The plants' verdicts. Every plant `TOOL-dTrueNorth-4` AC6 tables exits as that table states over
  the fixture design; only where the design comes from, and the build folder the fixture writes
  under, move.
- An install-prefix concern the finder raised and the skeptic did not establish: with S1 the module
  spells no path under the unattended kit, so there is nothing for that leg to read.
- This unit's own departure record: the close writes one for each member recorded by nobody
  (README build-level rule 4).

### Edges

- **consumes-from** `TOOL-dTrueNorth-4` — `deviation_join.py`, its fixture, its plants and the host call from `routed_commits.py`'s self-test; without them there is no strip read and no fixture to make hermetic
- **hands-off** `TOOL-dTrueNorth-16` — `build_design_fixture`, the second instance of which its item for id 42 extracts into a shared factory
- **hands-off** `TOOL-dTrueNorth-20` — the four `DESIGN_*` keys in `kit.toml`'s `conditional_keys` beside S5's row, which names all four, AC5 observed by a TOML read, `read_gen_region_awk` refusing a missing or empty strip, and the guards-join hit S4 makes on `TOOL-dTrueNorth-7` (the round-2 spec audit's ids 11, 26, 10, 15, 36 and 24)

## 4. Design

### Evidence

- `GEN_REGION_AWK` is assigned at `tools/unattended/lib-unattended.sh:1045`.
- `backlog.resolve_kit_dir(home, anchor, here)` (`tools/memory-tree/backlog.py:1749`) resolves a
  kit through the install receipt, then a probe beside the caller, and raises `LookupError` naming
  the places it looked.
- `read_landed_unclosed(root, conf, resolve=None)` (`tools/memory-tree/gen_build_index.py:1678` at
  base 271aa59d, `tools/memory-tree/gen_build_index.py:2055` at HEAD) is the precedent for an
  injectable resolver over a sibling kit, refusing by name when it does not resolve.
- The leg ships as a `subject = "kit"` row with `guard = ["{kit}/"]`
  (`tools/memory-tree/kit.toml:337-341`), and gov's manifest guards it on `{prefix}/lib/` and
  `{prefix}/memory-tree/`.
- The memory-tree kit's descriptor requires no kit (`tools/memory-tree/kit.toml:7`) and declares its
  conditional siblings as `requires_if` rows (`:8`), so an adopter may lack the unattended kit.
- `read_gen_strip` (`tools/memory-tree/deviation_join.py:314-329`) resolves the kit through
  `backlog.resolve_kit_dir` with no injection, and its one caller, `extract_authored` (`:334`), runs
  only on a revision `read_population` grades, as the import's own comment says (`:317`).
- The chain builds are `read_design_view`'s Build column (`deviation_join.py:407`), and the spec,
  record and `RUN.md` scans walk only those builds' folders (`:427`, `:509`). The fixture writes
  every path under `TN`, `memory/builds/dTrueNorth/` (`:694`), a chain build only of gov's live view.
- At HEAD eleven fixture roles each move a clause of the copied live `[chain]`, each its own: the
  base's owner amendment of `cl-dClosedLoop-0004` (`:918-922`), the `baseline` plant's
  `cl-dClosedLoop-0119` (`:931-935`), the `clause` plant's `cl-dClosedLoop-0008` (`:936-938`), the
  six `APPROVER_PLANTS` (`:704-709`) and the two `RISK_PLANTS` (`:711-712`). The `quote` plant reads
  the base's clause and moves none (`:993`); `malformed-follow` names a clause at no hash and moves
  none (`:1016`).
- The base plants `BASE_MEMBERS`, six (`:1127`). The builder's hand-back measured the composed run
  at 29 members over HEAD's design and at 22, with a late line no plant planted, under rev-3's four
  clauses, where eight roles share a clause.

### The fixture design

Two builds, `dFixA` and `dFixB`, holding eleven clauses, `cl-dFix-0001` to `cl-dFix-0011`, one per
clause-moving role, their texts plain sentences holding one backticked name each. A clause-moving
role is the base's owner amendment or a plant whose `add_plant` arm calls `set_moved_clause`: the
three named arms (`deviation_join.py:919`, `:932`, `:937`) and the one branch serving every entry of
`APPROVER_PLANTS` and `RISK_PLANTS` (`:939-948`). That count is the code's, eleven at HEAD, and the
table below follows it:

| Clause | Build | The role that moves it | HEAD's clause |
|---|---|---|---|
| `cl-dFix-0001` | `dFixA` | the base's owner amendment, approved by decision row `FIX-dClosedLoop-4`; `quote` reads it and moves none | `cl-dClosedLoop-0004` |
| `cl-dFix-0002` | `dFixA` | `baseline`, the clause it loosens before re-pointing the `Baseline:` line | `cl-dClosedLoop-0119` |
| `cl-dFix-0003` | `dFixA` | `clause`, edited with no record | `cl-dClosedLoop-0008` |
| `cl-dFix-0004` | `dFixA` | `owner-bare` | `cl-dClosedLoop-0001` |
| `cl-dFix-0005` | `dFixA` | `owner-er` | `cl-dClosedLoop-0002` |
| `cl-dFix-0006` | `dFixA` | `owner-row5` | `cl-dClosedLoop-0003` |
| `cl-dFix-0007` | `dFixB` | `owner-unknown-id` | `cl-dClosedLoop-0005` |
| `cl-dFix-0008` | `dFixB` | `approver-none` | `cl-dClosedLoop-0006` |
| `cl-dFix-0009` | `dFixB` | `approver` | `cl-dClosedLoop-0007` |
| `cl-dFix-0010` | `dFixB` | `below-risk` | `cl-dClosedLoop-0010` |
| `cl-dFix-0011` | `dFixB` | `owner-cause` | `cl-dClosedLoop-0011` |

The role map is held once. `APPROVER_PLANTS` and `RISK_PLANTS` keep their shape and carry the ids
above; `CLAUSE_ROLES` beside them maps the base, `baseline` and `clause` to theirs; and
`build_design_fixture` writes one `[chain]` clause and one view row per id those three hold, so a role
added to the map gets its own clause with no second edit. The plants' needles that name a moved
clause, `clause`'s and `owner-row5`'s (`:1134`, `:1141`), read their id from the map. The decision
rows name fixture clauses: `FIX-dClosedLoop-4`'s row names `cl-dFix-0001`, so the base's owner
approval holds, and no row names `cl-dFix-0006`, so `owner-row5` still reds.

The record carries the `[chain]` table and a `[clause-ids]` section reading `No baseline.`, committed
first; the pin is that commit, and the second commit writes the `Baseline:` line naming it, as
`build_fixture` does today (`:1042-1051`). The view is the eleven rows, each `since` `baseline`, in
the row grammar `design_lib.VIEW_ROW` reads.

The fixture build folder is `memory/builds/dFixA/`: `TN` names it, so every spec, deviation record,
acceptance ledger, prompt record, audit record and the `RUN.md` the base and the plants write move
there from `memory/builds/dTrueNorth/`, and the two `add` records depart from `dFixA [chain]`, not
`dTrueNorth [chain]`. `dFixB` holds clauses and no folder, which the scans skip (`:427-429`). The unit
ids `FIX-dTrueNorth-<n>` and the commit subjects keep their spelling: no join reads a build from
them, since `parse_spec_h1` admits any slug (`tools/memory-tree/tree_lib.py:219`) and a record's
build is its folder (`RECORD_NAME`, `deviation_join.py:125`).

The composed run, every plant but `unmeasured` over the base, holds `BASE_MEMBERS` plus each
plant's own increment, the member count of the base and that plant alone less `BASE_MEMBERS`. That
sum is the fixture's own count, derived from its single-plant builds and never typed, and the
composed run's only late member is the `record-late` plant's.

### Inventory

| Identifier | Kind | Lexicon cell |
|---|---|---|
| `read_gen_region_awk` | function, `deviation_join.py` | `py.function`, OK |
| `build_design_fixture` | function, `deviation_join.py` | `py.function`, OK |
| `CLAUSE_ROLES` | constant, `deviation_join.py` | `py.constant`, undeclared in the lexicon's cells, so ungoverned |

### Files touched (estimate)

- `tools/memory-tree/deviation_join.py`
- `tools/memory-tree/routed_commits.py` (its self-test's call into the fixture only)
- `tools/gate-legs.json`
- `tools/memory-tree/kit.toml` (one `requires_if` row)

### Alternatives rejected

- **A named refusal when the kit is absent, the finder's first fix.** The skeptic judged it unsound:
  inside a shipped self-test of a kit that does not require the unattended kit, a refusal reds that
  self-test in every such adopter.
- **A copy of the awk in the module.** `TOOL-dTrueNorth-4` S4 refuses one, and two copies of the
  strip drift.

## 5. Production-readiness checklist

- security — no new surface; the resolver reads a receipt row and a probe path inside the tree, and
  skips a receipt path that escapes it.
- perf / scale — one file read for the awk, now once per process at the join's entry; the design
  fixture writes two short files, the record and its eleven-row view; the compose arm adds one
  fixture build to the self-test.
- error / empty / loading states — an unresolved kit is a refusal live and a named skip under the
  fixture; neither reads as green over the plants it did not run.
- observability — the SKIP line names the reason and every plant it held back.
- risks — an adopter's self-test no longer observes the strip plants; the SKIP line says so on every
  run, and gov, where the kit resolves, runs them all.
- testing — AC1 to AC7 as probes; the arm under §7.
- migration — none.
- user docs — the module docstring; no page under `help/` covers the self-test.

## 6. Acceptance criteria

- **AC1** — When a probe copies `tools/lib/` and `tools/memory-tree/` into a scratch git repository
  under `%TEMP%` that holds no unattended kit and runs
  `python3 <scratch>/"tools/memory-tree/deviation_join.py" --fixture --plant status-only --policy refuse`,
  it prints the `deviation: SKIP` line naming the unattended kit and the held plants and exits 0;
  `--fixture --plant pass-revision --policy refuse` there still exits 1; and
  `--fixture --plant record-late --host routed-commits` there prints the SKIP line, then the host's
  RANGE line naming the planted revision as recorded after its departure, and exits 0, printing no
  `REFUSED` line.
  Red when: the fixture raises, or reds, when the kit is absent, or the identity strip reaches the
  fixture's own call and not the host's, so the host path through `check_routed_commits` refuses.
  fixture: a scratch repository under a short `%TEMP%` path; the tree holds none.
- **AC2** — When a probe loads the module and calls `read_gen_region_awk()` on the tree, it returns
  the bytes `sed -n "s/^GEN_REGION_AWK='\(.*\)'$/\1/p" tools/unattended/lib-unattended.sh` prints, and
  with `resolve` a stub raising `LookupError` it raises `LookupError` naming the kit.
  Red when: the value comes from a literal in the module.
- **AC3** — When `python3 "tools/memory-tree/deviation_join.py" --fixture --plant <case> --policy refuse`
  runs for each plant of `TOOL-dTrueNorth-4` AC6 in a scratch clone whose `.memory-tree.conf` blanks
  every `DESIGN_*` key and which holds no `DESIGN_RECORD` file, each exits as that table states.
  Red when: the fixture reads the live tree's design record or view, or writes its units outside its
  own chain builds, so the base's members are not read.
  fixture: a scratch clone under a short `%TEMP%` path.
- **AC4** — When `python3 -c "import json; print([l['guard'] for l in json.load(open( 'tools/gate-legs.json' )) if l['name'] == 'routed-commits selftest'])"`
  runs, the list holds the library's pathspec, the `{prefix}` token resolving so that it names
  `tools/unattended/lib-unattended.sh`.
  Red when: a commit touching only the library would skip the leg.
- **AC5** — When `grep -n 'kit = "unattended"' tools/memory-tree/kit.toml` runs, it prints one
  `requires_if` row whose `when_any_key_set` names the three `DESIGN_*` keys of S5.
  Red when: the live join's sibling dependency is undeclared, so `govkit selfcheck` grades nothing.
- **AC6** — When `python3 "tools/memory-tree/deviation_join.py" --fixture` runs in the AC3 clone under
  its default `--policy report`, the composed run exits 0, its summary prints `members N` with N the
  fixture's own count, and its summary's `recorded late` count is 1, its one
  `recorded after its departure` line naming the `record-late` plant's unit. A probe there derives N: it loads the module and, for each plant of
  `PLANTS` but `unmeasured`, reads the member count `measure_fixture` returns over `build_fixture` of
  the base and that plant; N is `BASE_MEMBERS` plus the sum of each count less `BASE_MEMBERS`.
  Red when: two clause-moving roles share a clause, so the composed run holds fewer members than its
  plants planted and the shared clause's later record reads late.
  figure: N is DERIVED at observation from the single-plant builds; the builder's hand-back measured
  29 over HEAD's plants and 22 under rev-3's four clauses, on 2026-10-22.
  fixture: the AC3 clone.
  cost: one fixture build per plant, as the self-test's arms already make.
- **AC7** — When `python3 <scratch>/"tools/memory-tree/deviation_join.py" --policy report` runs in
  AC1's scratch repository, one commit there holding a `.memory-tree.conf` that declares
  `DESIGN_RECORD`, `DESIGN_BASELINE` and `DESIGN_VIEW` with `DESIGN_VIEW` naming no file, it exits 2
  with a `nothing measured` line naming the unattended kit, not the view.
  Red when: the strip is resolved only once a revision is graded, so the view's refusal comes first
  and a history grading no revision never asks for the kit.
  fixture: AC1's scratch repository, with that conf committed.

## 7. Gates

`routed-commits selftest` · `routed commits name a specced unit` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `govkit selfcheck` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/routed_commits.py (its selftest) · covers AC1 AC3 AC6 · the deviation fixture run under a resolver stub raising LookupError, its record-late arm through the host included, and over a tree with every DESIGN_* key blank, red against the base module that reads the live records and a fixed library path; the composed run held to the sum of its plants' members and to the one late member, red against a role map that puts two roles on one clause · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join of
  `TOOL-dTrueNorth-2` reds a chain spec carrying nothing and derived from nothing. (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, the owner's ruling that a run carries the units it adds (ER:320).
  (b) None. (c) A `part k/n` carry of the repaired unit's clause. (b) reds `unbound` and (c) reds
  `parts` against the repaired unit's whole carrier; veto 1 discards both. Recommendation (a).
  Rung 3. RESOLVED (agent, 2026-10-21, delegated): (a). widens: none · relaxes: none
- **F2 — Does the build's grant lift veto 2 for the kit and manifest edits?** All three are governance
  carriers by `PLAY-dClosedLoop-10`'s list. `cl-dClosedLoop-0004` names the join at the commit
  through the routed-commit attribution, which this leg hosts; S4 guards that leg and S5 declares the
  sibling the join reads. RESOLVED
  (agent, 2026-10-21, delegated): lifted by `PLAY-dClosedLoop-3`, rung 3. grants: PLAY-dClosedLoop-3
  the deviation join's strip resolver, its fixture design, its requires_if row and the
  routed-commits self-test guard cl-dClosedLoop-0004's join runs in · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-21 · initial draft, promoted from the round-1 spec audit's id 30 (HIGH, item H5).
- rev-2 · 2026-10-21 · §3 · the Edges block gains a hands-off to TOOL-dTrueNorth-20, promoted by the
  round-2 spec audit, the mirror of its consumes-from; no other section moves.
- rev-3 · 2026-10-21 · §6 · the acceptance criteria name the modules this build creates (`deviation_join.py`, `asbuilt_view.py`, `design_lib.py`) quoted or bare, and a `git show`/`json.load` argument quoted, so the spec-tokens paths join, which reads the live tree at every `--dispatch`, stops refusing every unit before those modules exist. No criterion's observation moves.
- rev-4 · 2026-10-22 · S1 S2 S3 §3 §4 §5 AC1 AC3 AC6 AC7 §7 · the builder's DIVERGENCE hand-back: S3 and
  §4 gave the fixture design four clauses, while `TOOL-dTrueNorth-4` §4 "The fixture", which this
  unit leaves in force, makes every plant its own unit, clause or row so plants compose; eleven roles
  move a clause at HEAD, and on four clauses the composed run fell from 29 members to 22 and printed
  a late line no plant planted. The run's ruling (a), recorded in
  `memory/builds/dTrueNorth/prompts/2026-10-22-prompt-TOOL-dTrueNorth-12-divergence-brief.md`: one
  clause per clause-moving role, eleven, mapped role to clause in §4 "The fixture design"; the
  fixture's units, `RUN.md` and records move to `memory/builds/dFixA/`; S2's strip resolves at
  `read_population`'s entry, and its skip's identity strip reaches the host's
  `check_routed_commits` path the `record-late` arm takes; AC3 reads plants singly, AC6 holds the
  composed run to its derived count and its one late line, AC7 observes the up-front refusal. §4
  Evidence's `gen_build_index.py` citation names its HEAD line beside its base line.

## 10. Reuse audit

Probe: `python tools/codebase-map/reuse_lookup.py "resolve a sibling kit directory with an
injectable resolver"` ranked `resolve_kit_dir` (`tools/memory-tree/backlog.py`,
`tools/lib/resolve_kit_dir.py`) as a seam with 71 installs, and `kit_rel`. The seam this unit extends
is `backlog.resolve_kit_dir`, the resolver the kit's engines already import, with
`read_landed_unclosed`'s `resolve=` as the injection precedent; the fixture design follows
`TOOL-dTrueNorth-2`'s arm, which builds a two-build fixture view, record and deriver in its scratch
repositories, and its role map extends the plants' own `APPROVER_PLANTS` and `RISK_PLANTS`, which
already name each approver and risk plant's clause. No hit disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit and its generated view kept fresh" --terms "spec-audit promoted unit repairs order
as-built view deviation record re-render guard selftest pin"`
