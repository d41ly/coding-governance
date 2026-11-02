# TOOL-dCalibratedLens-9 — probe cost priced in the value ledger, and compactions counted per item kind

**Status:** OPEN · rev-2 · 2026-11-02 · node a · Tier-2 · base 8bec4cef · streams tooling · order 4 · advances TOOL-dCalibratedLens-18

**Carries:** cl-dClosedLoop-0466@f36d2aed whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 |
| [2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md](../reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) | spec-audit | TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-14 |

<!-- /gen:spec-records -->

## 1. Goal

The probe program (night pass, point 2) spends agent acts on verifications, reproductions and
experiments, and nothing prices them, so a placed probe that never decides anything is never seen to
cost. A compaction is journaled with the item in flight (night pass, point 5, item 3), and nothing
counts it, though "an item that compacts mid-flight is sized wrong". This unit gives the value ledger
its `probe` rows, one per probe origin, priced from the token fields of the acts that worked the probe,
and gives the Loop Review's gather one `compactions` metric, the count per item kind over the window.

## 2. Scope (IN)

Build-run preconditions, each specced and unbuilt at base `8bec4cef`, each re-grounded by the build
run, which stops this unit when one is absent: TOOL-dCalibratedLens-2 (the module
`tools/loop/loop_review.py`, `PROVIDERS`, the row grammar, `derive_ledger_rows` and `price`) and
TOOL-dCalibratedLens-3 (`METRICS`, `measure_loop_metrics` and the record's Metrics lines); the probe
program and its `probe` and `probe-trigger` record kinds (TOOL-dPlacedRequest-7 S4 to S6); the act
record and its token fields (TOOL-dWellOiledMachine-32 S7, S8); `read_act_records`
(TOOL-dWellOiledMachine-53 S4); the `Gov-Act:` commit trailer (TOOL-dWellOiledMachine-33 S1); the
`runtime` producer and the `compaction` class of the journal (TOOL-dWellOiledMachine-16 S3) and its
writer at a compaction (TOOL-dWellOiledMachine-12 S8); and the record door's `find` and `show`
(TOOL-dTotalRecall-9 S3, S5).

- **S1** — (amended, id 51) The act read across kits. `tools/runtime/ledgers.py` gains the verb `python ledgers.py acts
  [--build <slug>]`, which calls `read_act_records(repo, build)` once and prints one JSON object per
  act record on stdout: `key`, `act`, `item`, `tokens-in`, `tokens-out` and `wall`, each as the record
  spells it, `withheld` kept as written and an absent field as `null`. The loop kit runs it as a
  bounded subprocess (60 s) through the inline `resolve_kit_dir` block the module already carries
  (TOOL-dCalibratedLens-2 S1), since a kit imports no sibling kit. A failed run, a timeout or no
  runtime kit found is a refused read: the provider prints one `ledger — probe · acts unread · <why>`
  line and returns no rows, never a zero cost. Observed by AC1 and AC6.
- **S2** — One act's cost. `derive_act_tokens(act)` in `tools/loop/loop_review.py` returns
  `tokens-in` plus `tokens-out` as an integer, or `None` when either is `withheld`, absent or not a
  non-negative integer. It is the one place the loop kit computes an act's token cost;
  TOOL-dCalibratedLens-12 calls it. Observed by AC2.
- **S3** — The probe's acts. `read_commit_acts(root, start)` runs ONE `git log --since=<start>
  --format=<NUL><%(trailers:key=Gov-Act,valueonly,separator=%x2C)> --name-only` over the pathspec
  `<MEMORY_ROOT>/builds/*/build/*-probe-[0-9]*.md` and returns, per probe record path, the set of act
  ids whose commits touched it inside the window. A commit with no `Gov-Act:` trailer, the owner's or
  a command's, adds nothing. Observed by AC3.
- **S4** — (amended, id 50) The provider, `PROVIDERS`' `probe` entry. `derive_probe_rows(root, window)` reads every
  `probe` record through `gov_record.py find --kind probe` and `show`, each record's `Trigger` through
  `show` of its `probe-trigger` record, the acts through S1 and the commits through S3, and hands the
  parsed lists to `derive_probe_costs(probes, acts, commits, window)`. That pure function returns
  `(rows, events)` in TOOL-dCalibratedLens-2's provider shape, as §4 "The rows" states: one row per
  probe origin, and one own catch event per probe record whose verdict decided. An act counts toward a
  probe only when its record's `item` is an `item.probe.*` tag, so an asker's act that ran `probe.py
  trigger` is never priced as the probe. Observed by AC3, AC4 and AC5.
- **S5** — Unrecorded cost said, never zeroed. An act joined by S3 whose cost S2 answers `None`, or
  whose id names no act record, is counted per row and printed as one `ledger — probe · <id> · <n>
  act(s) unrecorded` line on stderr; a row whose every act is unrecorded renders `cost` as `-`.
  Observed by AC5.
- **S6** — (amended, id 31) The compaction count. `read_journal_compactions(root)` runs `python <runlog kit>/runlog.py
  journal --producer runtime` (the existing verb, `tools/runlog/runlog.py:151`, its producer choices
  read from `PRODUCER_FILES`, `:499`) as a bounded subprocess (60 s) found through `resolve_kit_dir`,
  and keeps the JSON objects whose `class` is `compaction`. `measure_compactions(lines, window)`, a
  pure function, counts the lines whose `t` lies in the window per `item` value, `item=none` and an
  absent `item` counted together as `unattributed`. Observed by AC6 and AC7.
- **S7** — (amended, id 11) The metric. `METRICS` (TOOL-dCalibratedLens-3 S5) gains the entry `compactions`, whose
  reader answers `(value, source)` per §4 "The metric": the counts in one value, the source the
  journal read and the node it was read on, `none` over an empty count, and `searched-none` with the
  journal path when the journal is absent or the read refused. The record writes it as its Metrics
  line, `compactions: <value> · <source>`. Observed by AC7 and AC8.
- **S8** — The docs. `tools/loop/README.md` states the `probe` row, its origin, its cost source, what
  counts as a catch, and the `compactions` metric with its one-node reach; `help/loop-review.md`
  (TOOL-dCalibratedLens-2 S12) gains the same in its value-ledger section and its Loop Review section.
  NOT OBSERVED by a criterion: prose, read by the closing review.

## 3. Non-goals (OUT)

- The view, its row grammar, `price`, `derive_ledger_rows`, and the `window` and `state` columns:
  TOOL-dCalibratedLens-2's. This unit adds one `PROVIDERS` entry and codes no second writer of the view.
- The walk, the lease, the period, the window and the record: TOOL-dCalibratedLens-3's. This unit
  adds one `METRICS` entry and reads the window it is handed rather than the key.
- Proposing a probe origin's retirement: TOOL-dCalibratedLens-5's `propose`, which reads this row like
  any other.
- Cost per item kind over every act: TOOL-dCalibratedLens-12's `item` rows. The acts of `item.probe.*`
  items are priced in both views; neither view is a sum of the other, and the ledger carries no total.
- Compactions on another node. The journal is node-local (`<git common dir>/runlog/`,
  TOOL-dWellOiledMachine-16 S3), so the metric counts the lease holder's node, the reach v2:1345 states
  for `review.loop.catch-source`; a cross-node count needs a committed compaction record no build owns.
- Wall time as probe cost. The `cost` unit is `tok`; an act's `Wall` is TOOL-dWellOiledMachine-53's
  estimate and TOOL-dCalibratedLens-17's trend.
- A `Cost` field on the probe record: the cost is derived from the act records the probe's commits
  name, so a second copy would be one fact twice (§8 F1).

### Edges

- **consumes-from** `TOOL-dCalibratedLens-2` — `PROVIDERS`, which gains the `probe` entry, the provider shape and the `-` and event rules of the row grammar; without them the rows have no view to land in
- **consumes-from** `TOOL-dCalibratedLens-3` — `METRICS`, which gains the `compactions` entry, and the window the walk hands every reading
- **hands-off** `TOOL-dCalibratedLens-12` — `derive_act_tokens` and `ledgers.py acts`, the act read and the one cost computation the `item` rows reuse
- **consumes-from** external — TOOL-dPlacedRequest-7 (the `probe` and `probe-trigger` records), TOOL-dWellOiledMachine-12, -16, -32, -33 and -53 (the compaction line, the journal, the act record, the `Gov-Act:` trailer and `read_act_records`) and TOOL-dTotalRecall-9 (`find`, `show`), all DEFERRED at base and of ancestor builds
- **hands-off** `TOOL-dCalibratedLens-28` — `derive_probe_rows` and `derive_probe_costs`, which that unit's `probes-41` plant prices (id 50)
- **hands-off** `TOOL-dCalibratedLens-16` — `ledgers.py acts --build` and `read_runtime_journal`, the act read and the journal read its S4 and S3 share (ids 50, 31)
- **hands-off** `TOOL-dCalibratedLens-30` — the `compactions` reading's dead-source line, which the minors batch's `dead-sources` arm reads (id 11)

## 4. Design

### The rows

```
probe record  --Trigger-->  probe-trigger record  ->  origin = <Cause>@<At, else Asker>
probe record path  <-- commits in the window carrying Gov-Act: <act> --  act ids
act ids  ->  ledgers.py acts  ->  act rows whose item starts item.probe.  ->  derive_act_tokens
```

| Column | Value for one origin |
|---|---|
| `kind` | `probe` |
| `id` | `<cause>@<item tag>`: the trigger's `Cause`, and its `At` where set, else its `Asker`; `point@item.entry.place`, say |
| `since` | the earliest `<date>` of that origin's probe record file names, over every probe record and not only the window's |
| `cost` | `<tokens>tok/<acts>`: the sum of `derive_act_tokens` over the distinct acts S3 joins to that origin's probe records inside the window, and their count; `-` per S5 |
| `catches`, `false-reds`, `last-catch` | joined by `derive_ledger_rows` from this provider's events |

The events are `(probe, <origin>, <date>, own)`, one per probe record of the origin whose `Verdict`
decided, at any age, `<date>` its file name's: `confirmed` or `refuted` for a verification or a
reproduction, `measured` for an experiment. No probe verdict is a false red, so this provider returns
no `false` event and the row's `false-reds` reads `0`.

An origin is the retirable thing. A `point` origin is a placement in `probe.points`
(`tools/policy/catalogue.toml:679`), which the owner removes; a `raised` or `owner` origin names the
asking item. A probe that ends `inconclusive`, `unrunnable`, `within-noise` or `aborted` decided
nothing, so an origin whose probes only ever end that way catches nothing and is what
TOOL-dCalibratedLens-5 proposes. An act is counted once per origin however many commits it made.

### The metric

```
compactions: item.build.unit 4, item.review.synth 1, unattributed 2 · runtime journal on <node>
compactions: none · runtime journal on <node>
compactions: searched-none · <journal path>
```

One Metrics line, the shape TOOL-dCalibratedLens-3 §4 "The record" gives: each item kind and its count,
highest first and then by tag, `unattributed` last, comma-joined. `<node>` is the node name the walk
runs on. The count is a sizing signal and decides nothing: no item routes on it.

### Inventory

Minted: the functions `derive_act_tokens`, `read_commit_acts`, `derive_probe_rows`,
`derive_probe_costs`, `read_journal_compactions` and `measure_compactions` in
`tools/loop/loop_review.py`, each answered OK by `python tools/lexicon/lexicon.py --suggest <name> --as
py.function` at this base (`count_compactions` was refused for `measure`); the `acts` verb of
`ledgers.py`; the `PROVIDERS` key `probe`; the `METRICS` entry `compactions`; the output lines `ledger —
probe · …`.

### Migration

None: no probe, act record or compaction line exists at base, and a review over an empty population
writes no `probe` row and `compactions: none`.

### Amendments (round-1 spec audit)

The round-1 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md`) confirmed the
findings below on this spec, and its disposal amended this text. Each bullet supersedes the text it
names; the unit it names owns the finding and its proof.

- **id 50 · S4 (H10, `TOOL-dCalibratedLens-28`)** — The probe records are listed with one
  `git ls-files` over S3's pathspec `<MEMORY_ROOT>/builds/*/build/*-probe-[0-9]*.md`, each read
  through `gov_record.py show`, and each `probe-trigger` record the same way; never
  `gov_record.py find`, which stops at 40 rows.
- **id 31 · S6 (M15, `TOOL-dCalibratedLens-30`)** — The runtime journal read is one helper,
  `read_runtime_journal(root)`, the bounded `runlog.py journal --producer runtime` subprocess
  returning the parsed lines; `read_journal_compactions` filters it, and TOOL-dCalibratedLens-16 S3
  calls it and filters by the walk's window.
- **id 51 · S1, AC1 (M26, `TOOL-dCalibratedLens-30`)** — `ledgers.py acts` gains `--since <date>`,
  filtering by the act record's file-name date before any record is read, and reads the tracked act
  records in one process (one `git ls-files`, one `git cat-file --batch`), never one
  `gov_record.py show` per act; `estimate` (TOOL-dCalibratedLens-17) stays all-time. The 60 s bound
  is sized for the population a window holds, and AC1 also times `acts --since` over 500 planted act
  records under it.
- **id 11 · S7, AC8 (L1, `TOOL-dCalibratedLens-30`)** — An absent runtime journal file reads
  `searched-none` (nothing written yet); a refused or timed-out read, or no runlog kit, reads
  `compactions: unread · <reason>`, and AC8's refused-read case expects `unread`.
- **id 39 · Files touched (M19, `TOOL-dCalibratedLens-30`)** — Every `loop_review.py` verb or flag
  this unit adds to `help/loop-review.md` gets its `[[usage]]` row in `tools/govkit/usage.toml`, and
  the page's `<!-- usage: … -->` anchor is re-fingerprinted, so
  `python tools/govkit/docs_leg.py --list` names it and the `docs` leg reads no `UNROWED` line.

### Files touched (estimate)

- `tools/loop/loop_review.py` (S2 to S7, and the `--fixture` cases of §7)
- `tools/loop/README.md` (S8)
- `tools/runtime/ledgers.py` (S1, and its `fixture` case of §7)
- `help/loop-review.md` (S8, TOOL-dCalibratedLens-2's page)
- `tools/govkit/usage.toml` — the `[[usage]]` row of each verb or flag added (id 39)

### Alternatives rejected

- **A `Cost` field written on the probe record at `probe.return`.** It still needs this unit's join to
  fill, and then holds a figure the act records already hold.
- **Rows per probe item tag.** They duplicate TOOL-dCalibratedLens-12's `item` rows for `item.probe.*`
  and name nothing the owner can retire.
- **An inline copy of `read_act_records` and of the journal grammar in the loop kit.** Both readers
  already exist behind a CLI or can, and a subprocess keeps one reader of each source (§8 F2).

## 5. Production-readiness checklist

- security — no new write path: the provider reads committed records, one `git log` and two kit CLIs,
  and its output lands through `price` and `record`, units 2 and 3's. The `acts` verb prints fields the
  committed act records already carry.
- perf / scale — one `git log`, one `ledgers.py acts`, one `find --kind probe` and one `show` per probe
  and trigger record; `read_act_records` costs one `show` per act, its own spec's ceiling.
- error / empty / loading states — a refused read prints its reason and yields no row rather than a
  zero; an unrecorded act is counted and named; an absent journal renders `searched-none`.
- observability — every `ledger — probe` line names the origin and the count it could not price.
- risks — an act of a probe item that commits nothing to the probe record is not joined, so cost
  under-reads (`ponytail:` ceiling: trailer join only; a probe field on the act record is the upgrade
  if a measured probe shows acts missing); the compaction count is one node's.
- testing — each criterion is a probe of this unit's functions over planted inputs; the arms in §7 are
  observed RED then GREEN by the main loop at the close.
- migration — none, §4 "Migration".
- user docs — S8, `help/loop-review.md` and the loop kit README.

## 6. Acceptance criteria

- **AC1** — (amended, id 51) When `python ledgers.py acts` runs from the runtime kit directory in a scratch repository
  holding two act records, one with `Tokens-In: withheld`, it prints two JSON objects whose `key`,
  `item`, `tokens-in` and `tokens-out` match the records, the withheld one as `"withheld"`.
  Red when: a withheld field is printed as `0` or the record is dropped.
  fixture: a scratch repository under `%TEMP%`; the act record kind is TOOL-dWellOiledMachine-32's,
  absent at `8bec4cef`.
- **AC2** — When a probe calls `derive_act_tokens` from `loop_review.py` on `{"tokens-in": "120",
  "tokens-out": "30"}`, `{"tokens-in": "withheld", "tokens-out": "30"}` and `{"tokens-in": "-4",
  "tokens-out": "1"}`, it returns `150`, `None` and `None`.
  Red when: a withheld or negative field is summed as a number.
- **AC3** — When a probe commits, in a scratch repository, one probe record under a commit carrying
  `Gov-Act: act-aaaaaaaaaaaa` and a second commit to it carrying no trailer, `read_commit_acts` from
  `loop_review.py` returns that record's path mapped to `{"act-aaaaaaaaaaaa"}` alone.
  Red when: the trailer-less commit adds an act, or a commit outside the window is read.
  fixture: a scratch repository under `%TEMP%`, built by the probe.
- **AC4** — When a probe calls `derive_probe_costs` from `loop_review.py` with two probes of trigger
  `point@item.entry.place`, verdicts `refuted` and `inconclusive`, joined to acts of items
  `item.probe.design` (100 tokens) and `item.entry.place` (900 tokens), it returns one row with
  `kind` `probe`, `id` `point@item.entry.place` and `cost` `100tok/1`, and one own event for the
  `refuted` probe alone.
  Red when: the asker's `item.entry.place` act is priced as the probe, or `inconclusive` yields an
  event.
- **AC5** — When the same probe joins one more act whose `tokens-out` is `withheld`, the row's `cost`
  stays `100tok/1` and stderr carries one `ledger — probe · point@item.entry.place · 1 act(s)
  unrecorded` line; with only that act joined, `cost` is `-`.
  Red when: an unrecorded act is summed as zero with no line, or a row of unrecorded acts reads `0tok`.
- **AC6** — When `derive_probe_rows` runs in a scratch repository with no runtime kit on the resolve
  path, it returns no row and prints one `ledger — probe · acts unread ·` line naming the missing kit.
  Red when: a refused act read yields rows priced at zero.
- **AC7** — When a probe calls `measure_compactions` from `loop_review.py` over planted journal
  objects, three `class=compaction` lines with `item=item.build.unit`, one with `item=none`, one
  outside the window and one `class=stall` line, it returns `item.build.unit` 3 and `unattributed` 1.
  Red when: an out-of-window or non-compaction line is counted, or `item=none` is dropped.
- **AC8** — (amended, id 11) When `python loop_review.py --fixture --plant compactions` runs from the loop kit directory,
  a scratch repository with no runtime journal answers the `compactions` metric `searched-none` with the
  journal path, and one holding the AC7 lines answers `item.build.unit 3, unattributed 1`.
  Red when: an absent journal reads as `none`, or the entry is missing from `METRICS`.
  fixture: the `--fixture` frame is TOOL-dCalibratedLens-2's, absent at `8bec4cef`.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `docs` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix`

The leg `loop-review selftest` (TOOL-dCalibratedLens-2 S11, argv `loop_review.py --fixture`) and the
runtime kit's fixture leg (TOOL-dWellOiledMachine-53) are not in the manifest at base, so they are
named here in prose; each grades its arm below once its unit lands.

New arm: tools/loop/loop_review.py · covers AC2 AC3 AC4 AC5 AC6 AC7 AC8 · `--fixture` cases planting probe, trigger and act records with one trailer-less commit, an unrecorded act, a missing runtime kit, and journal lines in and out of the window; the failing case staged by dropping the `item.probe.` filter from `derive_probe_costs` · none
New arm: tools/runtime/ledgers.py · covers AC1 · a `fixture --case acts-withheld` case reading two act records, one withheld; the failing case staged by printing a withheld field as 0 · none

## 8. Open questions

- **F1 — The probe record carries no cost field (the brief's PRIMITIVE GAP); how is a probe's cost
  joined to it?** Options: (a) the commits that touched the probe record carry `Gov-Act:` trailers
  (TOOL-dWellOiledMachine-33 S1), each naming an act record whose `Tokens-*` S2 sums, kept only for
  `item.probe.*` acts; (b) a `Cost` field the probe program writes at `probe.return`, which still
  needs a join to fill; (c) act records whose `item` is `item.probe.*`, matched to a probe by build,
  unit and time span, which mis-assigns two probes of one unit; (d) an ask on dPlacedRequest for a
  probe id on the act record. (b) is a fact twice; (c) fails when one unit runs two probes; (d) leaves
  this clause unbuilt until another build moves. RESOLVED (agent, 2026-11-02, delegated): (a), rung 3,
  the most feature-rich survivor, built inside this unit's scope from primitives two ancestor builds
  spec. widens: none · relaxes: none
- **F2 — How does the loop kit read act records and the runtime journal, since a kit imports no
  sibling kit?** Options: (a) a subprocess of each owning kit's CLI, `ledgers.py acts` (new, S1) and
  the existing `runlog.py journal --producer runtime`; (b) inline copies of `read_act_records` and of
  the `journal_grammar_py` block under parity rows of `tools/lib/resolve-python.test.sh`; (c) an
  import of the runtime kit. (c) breaks the kit rule; (b) carries two blocks of another kit's code
  into a third kit to save two spawns. RESOLVED (agent, 2026-11-02, delegated): (a), rung 3, a reuse of
  the seam `cmd_journal` (`tools/runlog/runlog.py:151`), the route TOOL-dCalibratedLens-2 S4 already
  takes for its `node-journal` source. widens: none · relaxes: none
- **F3 — Who fills the catch columns of a `probe` row?** RESOLVED (agent, 2026-11-02, delegated): the
  provider returns its own catch events and `derive_ledger_rows` joins them, rung 1 of the records:
  TOOL-dCalibratedLens-2 §4 "The row" gives a provider whose kind carries its own catches exactly that
  route, and the catch source's verdict records name legs and never a probe origin. A decided verdict
  is the catch, rung 3, since an undecided probe is the one bearing no load. widens: none · relaxes:
  none
- **F4 — The brief joins `class=compaction` lines to the act record's `Item`; is the join needed?**
  RESOLVED (agent, 2026-11-02, delegated): no, rung 1 of the records: the line already carries
  `item=<item tag|none>`, the act record's `item` for an act session (TOOL-dWellOiledMachine-12 S8), so
  the count reads the line alone and an act-less session counts as `unattributed`. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, from the packet's Items 9 (`cl-dClosedLoop-0466@f36d2aed`), the
  brief's row for this unit and S1, S3 and S4, night pass points 2 and 5, layer-expansions:258-263,
  the sibling specs TOOL-dCalibratedLens-2 and -3 as written this run, and the parent and ancestor
  specs named in §2 at base `8bec4cef`. The status token is `OPEN`, the drafting token of
  TEMPLATE-SPEC; the brief's `DRAFT` is no member of `STATUS_TOKENS`
  (`tools/memory-tree/tree_lib.py:28`).
- rev-2 · 2026-11-02 · §3 §4 §7 S1 S4 S6 S7 AC1 AC8 · amended at the disposal of the round-1 spec
  audit `2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit`, §4 "Amendments (round-1
  spec audit)": ids 50 (`TOOL-dCalibratedLens-28`), and 31, 51, 11 and 39
  (`TOOL-dCalibratedLens-30`); §3 gains the hands-offs to units 28, 16 and 30.

## 10. Reuse audit

The seams extended are TOOL-dCalibratedLens-2's `PROVIDERS` and provider shape and
TOOL-dCalibratedLens-3's `METRICS`; the runlog kit's journal verb `cmd_journal`
(`tools/runlog/runlog.py:151`, its `--producer` choices at `:499`), called as it is rather than copied;
the runtime kit's `read_act_records` (TOOL-dWellOiledMachine-53 S4), given a CLI verb beside that
spec's `checks` and `status`; and the `Gov-Act:` trailer (TOOL-dWellOiledMachine-33 S1) as the join
key. `python tools/codebase-map/reuse_lookup.py "price the cost of each probe and count compactions per
item kind"` ranked name stems (`probe`, `counts`, `measure_typed_counts`) and record helpers in
`tools/runlog/record.py`, none a cost or compaction reader; no existing seam fits the pricing itself,
which no landed code does, and the loop kit and runtime kit are absent at base. Where record and
source disagree: the brief joins compaction lines to the act record's `Item`, and
TOOL-dWellOiledMachine-12 S8 shows the line carries the item itself (§8 F4); the brief says the probe
record carries no cost field, and TOOL-dPlacedRequest-7 S6's field list agrees. The recall hit
TOOL-dTotalRecall-11 names `probe.run` among the shape-run writers, an experiment's review shape and no
token cost, which is TOOL-dCalibratedLens-7's row kind.

Recall terms used: `python tools/memory-recall/query.py "how is probe cost priced and how are compactions counted per item kind" --terms "probe record act record Tokens-In compaction journal item kind value ledger Loop Review sizing"`
