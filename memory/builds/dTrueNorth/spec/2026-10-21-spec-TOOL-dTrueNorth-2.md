# TOOL-dTrueNorth-2 — the carries join, a further join of the spec tokens leg

**Status:** OPEN · rev-1 · 2026-10-21 · node d · Tier-2 · base 271aa59d · streams tooling · order 1

**Carries:** cl-dClosedLoop-0002@6acd9ea9 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-21-prompt-TOOL-dTrueNorth-1-spec-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-1-spec-brief.md) | research | TOOL-dTrueNorth-1 TOOL-dTrueNorth-3 TOOL-dTrueNorth-4 TOOL-dTrueNorth-5 TOOL-dTrueNorth-6 TOOL-dTrueNorth-7 |

<!-- /gen:spec-records -->

## 1. Goal

No gate joins a design clause to the spec that carries it, so a dropped, stale or doubly carried
clause is found only when a review happens to run (gap-design-13). This unit adds the carries join to
`tools/check-spec-tokens.py`, beside the hands-off join and behind the same kind of cutoff:
`SPEC_CARRIES_CUTOFF`, read through `read_cutoff_key`. It reads each chain build's specs through the
parser in `design_lib.py` and reds a ghost id, an unbound spec, a stale pin, two whole carriers or two
pins, a revision that stops carrying a clause with no decision, and a clause token missing from its
carriers, and a run that measured no spec is never green. Its acceptance is the bootstrap
instrument's thirteen plants (D3), which is stricter than the clause and recorded as deviation 3.

## 2. Scope (IN)

- **S1** — The population. With `SPEC_CARRIES_CUTOFF` set, `read_carries_specs` takes the tracked
  chain-build specs `scan_chain_specs` selects at or after the cutoff, reads each one's status
  header, and sets every `WONTDO` spec apart, counted (§8 F2). It reads each kept spec's working-tree
  text and its text at every commit that touched it, through one `git log` over the chain builds'
  spec folders and one `git cat-file --batch`. Observed by AC14, AC15.
- **S2** — `scan_carries`, the join, a pure function over `(design, specs)` where `specs` is
  `{build: [(path, text, revisions)]}`, the shape `carries.py`'s own `fixture()` builds. Its arms,
  each a finding labelled by arm, as `carries.py:225-290` reads them:
  - per spec: `malformed`, a line the parser refuses; `unbound`, carrying nothing and derived from
    nothing; `withdrawn`, carrying an id `[clause-ids]` withdraws; `ghost`, carrying an id no clause
    has; `crossbuild`, carrying another build's clause with no `**Moved:**` line naming it to the
    spec's own build; `stale`, a pin other than the hash of the clause's text in the view; `stopped`, a clause an
    earlier revision carried that this text does not carry and does not release;
  - per clause: `ambiguous`, two whole carriers or two pinned hashes; `parts`, parts that are not
    1 to n; `token`, a backticked name of the clause found in none of its carriers, read from
    whichever build's folder holds each carrier;
  - at a Design exit only, called with `exit_mode=True`: `uncarried`, a clause no spec carries and
    none releases; `node`, an owned node no spec names.
  Observed by AC1 to AC12.
- **S3** — `derive_carries_coverage`, the one function `TOOL-dTrueNorth-3` calls. It reads the keys,
  the design through `read_design`, the population, and runs `scan_carries` once with `exit_mode=True`.
  It returns, per chain build, the coverage fields `carries.py:293-312` computes, the build's specs
  with their statuses, and the findings with their arm labels. With the cutoff blank it returns an
  `off` state naming the key; any other misconfiguration raises `DesignRefusal`. Observed by AC13,
  AC15.
- **S4** — The leg. `main()` calls `derive_carries_coverage` once, keeps every finding whose arm is
  not `uncarried` or `node`, and folds each into `hits` before the waiver pass, as the hands-off join
  folds its own at `tools/check-spec-tokens.py:1250-1252`. A hit's token is the composite
  `carries <- <arm>:<ref>`, so a waiver row keyed on a bare path never takes one. One report line
  prints on every run, off and armed alike, and carries the literal `live spec(s) ·` so that
  `--dispatch` leaves it out of a refusal's diagnosis (`tools/unattended/unattended.sh:13502`). With
  the cutoff set and no chain spec measured, the leg refuses and exits 1. Observed by AC12, AC14,
  AC16.
- **S5** — The checker's header names the ninth join, its population and its two limits, beside
  the hands-off join's entry. Observed by AC17.

## 3. Non-goals (OUT)

- The parser, the view reader, the withdrawn-id reader, the owned-node reader and the population
  selector: `TOOL-dTrueNorth-1`'s `design_lib.py`. This unit parses nothing itself.
- Rendering coverage, and refusing a spec at `INPROGRESS` while its build's coverage is red:
  `TOOL-dTrueNorth-3`'s. The `uncarried` and `node` arms red the bar nowhere; clause 0002 names
  neither, and clause 0003 puts the Design-exit refusal in memory hygiene.
- Whether a carrier means what its clause means. The semantic lens reads that at a Design exit
  (`design.coverage.semantic`), and a carrier keeping every token while contradicting its clause
  passes here, as it passes the instrument.
- A clause amended after its carrier is `CLOSED`. The `stale` arm reds the frozen carrier, which
  fails closed; the remedy is dIndexedDesign's `design.coverage` (`cl-dClosedLoop-0398`), and the
  deviation record that moves the hash is `TOOL-dTrueNorth-4`'s population.
- History across a rename. `git log` is read per path without `--follow`, so a clause carried before
  a spec file was renamed is not read as carried.
- Editing `carries.py` or any instrument; the instrument keeps running at the Design exit beside
  this join (the packet's Gates).

### Edges

- **consumes-from** `TOOL-dTrueNorth-1` — the parser, the readers and `scan_chain_specs` in `design_lib.py`; without them this join has no clause and no binding to read
- **hands-off** `TOOL-dTrueNorth-3` — `derive_carries_coverage`, the coverage fields and findings its region renders and its hygiene check reads

## 4. Design

### Evidence

- The hands-off join is the seventh join and the precedent: its key `SPEC_HANDOFF_CUTOFF`, read
  through `read_cutoff_key` at `tools/check-spec-tokens.py:1068`, its hits folded into `hits`
  before the waiver pass at `:1250-1252`, and its report line printed on every run at `:1331`.
- `main()` already holds the whole tracked spec set as `allspecs` at `:1014`, before it narrows to
  live specs. The carries join reads its own population, so the live narrowing does not reach it.
- `--dispatch` runs this checker over the live tree before every unit and refuses on exit 1
  (`tools/unattended/unattended.sh:13493-13506`). It filters report lines out of its diagnosis by
  `live spec\(s\) ·`, `bar join ·` and `Gates heading` (`:13502`).
- The instrument's thirteen plants run today as `carries.py --fixture --plant <case>`: eleven exit
  1, `unmeasured` exits 2, `moved` exits 0 by design, and the clean set exits 0 (observed this
  pass, 2026-10-21, at `271aa59d`). `moved` is the green control, its carrier holding every token.
- Under this harness each unit's spec goes `CLOSED` in its own build commit
  (`tools/unattended/unattended.sh:13482-13483`), so a join reading only live specs would lose each
  carrier as its unit closed.

### Data model

A finding is `(where, arm, ref, why)`: `where` is the spec path for a per-spec arm and the build slug
for a per-clause or exit arm; `ref` is the clause id, the node, or the spec path.

`derive_carries_coverage(root, files=None)` returns:

```python
{"state": "armed", "cutoff": "2026-10-21", "measured": 7,
 "skipped": {"other-build": 0, "pre-cutoff": 0, "undated": 0, "wontdo": 0},
 "builds": {"dTrueNorth": {
     "clauses": ["cl-dClosedLoop-0001", ...], "nodes": ["record-kind.deviation"],
     "specs": [("memory/builds/dTrueNorth/spec/…-1.md", "OPEN"), ...],
     "whole": [...], "split": [...], "released": [(cid, "moved"|"retired"|"deferred", decision)],
     "uncarried": [...], "stale": [...], "ambiguous": [...], "unnamed": [...],
     "derived": [(path, decision)], "blind": [...],
     "findings": [(where, arm, ref, why), ...]}}}
```

Every chain build of the view gets an entry, a build with no spec included, so the region can say
"over 0 specs" rather than be absent. The off state is `{"state": "off", "why": "SPEC_CARRIES_CUTOFF
blank"}`. The fields are `carries.py:293-312`'s, computed the same way: `whole` is a clause with a
whole carrier, `split` one carried only in parts, `released` the `**Moved:**`, `**Retired:**` and
`**Deferred:**` lines of the build's own specs, `uncarried` a clause neither carried nor released
there, `stale` a clause one of whose carriers pins another hash, `ambiguous` a clause with two whole
carriers, `unnamed` an owned node no spec names, `derived` each `**Derived:**` line with its spec,
and `blind` a clause with no backticked name.

### Behaviour

- **Keys.** The cutoff through `read_cutoff_key`; a `None` from it, a refusal it has printed, raises
  `DesignRefusal`. The four `DESIGN_*` keys through `read_conf_key`, handed to `read_design`, which
  refuses a blank one by name. No relation check runs on the cutoff, as none runs on
  `SPEC_HANDOFF_CUTOFF`: the key is set on the day it grades.
- **Statuses.** The status token is the word after `**Status:**` in the spec's first five unfenced
  lines. `WONTDO` is set apart before any arm runs, so a superseded unit's binding lines neither carry
  nor collide with its successor's. Every other status carries, `CLOSED` and `DEFERRED` included,
  since a landed carrier is what carries a landed clause.
- **Revisions.** `git log --format=%H --name-only` over every chain build's `spec/` folder gives each
  path its commits; one `git cat-file --batch` request of `<sha>:<path>` lines reads them. A commit
  where the path is absent is skipped. Each revision is parsed with `strict=False`, so a malformed
  line a later commit corrected is no finding now; the working-tree text is parsed strictly.
- **A spec refused by the parser** contributes its `malformed` finding and no binding, so it is not
  also reported `unbound`.
- **The join** is `carries.py:225-290` arm for arm, with two changes, each named: the `withdrawn` arm
  reads `read_retired_ids` at the baseline as the instrument reads `[clause-ids]` in the working tree;
  and the clause population is the view's, through `read_design`, where the instrument reads v2. The
  two agree on every clause until a deviation's `amends` row moves one, and `TOOL-dTrueNorth-1`'s
  evidence measured that agreement on all 509 clauses.
- **The leg's report line**, one shape on every run:
  `spec-tokens: carries join · <n> chain spec(s) measured in <b> build(s), every status but WONTDO, not only live spec(s) · <c> clause(s) · <w> withdrawn · <o> owned node(s) · <k> finding(s), <x> at the Design exit only · SPEC_CARRIES_CUTOFF <date>`.
  Off, the tail reads `SPEC_CARRIES_CUTOFF blank (arm off)` and the counts read 0.
- **Never green on nothing.** Armed, `measured` zero prints `spec-tokens: REFUSING — the carries join
  measured no chain spec at/after SPEC_CARRIES_CUTOFF <date>, so it read nothing and is never green`
  and returns 1, before the waiver pass.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `CARRIES_KEY` | constant, `"SPEC_CARRIES_CUTOFF"` | `tools/check-spec-tokens.py` |
| `CARRIES_EXIT_ARMS` | constant, `("uncarried", "node")` | check-spec-tokens |
| `read_carries_specs` | function | check-spec-tokens |
| `scan_carries` | function | check-spec-tokens |
| `derive_carries_coverage` | function | check-spec-tokens |
| the `carries` hit kind and its `carries <- <arm>:<ref>` token | join output | check-spec-tokens |

Each name leads with a verb the naming lexicon declares. `design_lib` is imported by path from the
memory-tree kit beside this file, the module's own directory joined to `memory-tree`.

### Fixtures

The parity probe is a scratch script the pass writes. It loads `tools/check-spec-tokens.py` and
`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-carries.py` by path, builds the
design with `read_design` over the tree's keys, and for each plant of the instrument's `PLANTS`, and
for none, hands `carries.py`'s `fixture(builds, nodes, "dTrueNorth", plant)` to `scan_carries(...,
exit_mode=True)`. Using the instrument's own fixture builder is what makes the plant suite the
instrument's and not a copy. The further cases, two hashes, a parts gap, a malformed line, a
withdrawn id and a `WONTDO` carrier, are edits the probe makes to the clean fixture's texts.

### Rollout

Lands armed: `TOOL-dTrueNorth-1` set the cutoff. From this unit's commit, every `--dispatch` of the
later units runs the join over this build's own specs, so a sibling spec that drops a token or a pin
refuses the next dispatch rather than surfacing at the close.

### Files touched (estimate)

- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`

### Alternatives rejected

- **The join inside `design_lib.py`.** The spec brief's S4 places it in the spec tokens leg beside
  the hands-off join, and the clause names that leg.
- **Live specs only, the checker's other joins' population.** Every carrier would leave the
  population at its unit's close, and every landed build would read as uncarried.
- **The exit arms in the bar.** Twenty-one chain builds have no spec today, so the bar would red on
  every clause they own from this unit's landing.

## 5. Production-readiness checklist

- security — read-only. No new write path; the new execution is the deriver `TOOL-dTrueNorth-1`
  loads, refused unless tracked.
- perf / scale — one `git log` and one `cat-file --batch` for every chain spec's history, and the
  deriver's 0.5 s (PINNED, 2026-10-21), against the leg's 180 s ceiling in `tools/gate-legs.json`.
- error / empty / loading states — blank cutoff: an announced off line. Set with a blank or
  unreadable design key: a refusal naming it. Set with no spec measured: a refusal. None reads green.
- observability — the report line on every run, the counts it measured, and each hit naming its
  arm, its spec or build and its clause.
- risks — the join reads this build's own specs at every dispatch from its landing, so a sibling
  unit's spec that breaks a pin refuses that dispatch. That is the intent, and it is the first time
  a spec defect stops a dispatch rather than a review.
- testing — AC1 to AC13 as the parity probe and scratch fixtures; AC14 to AC17 over scratch clones
  and the tree; the `New arm:` line under §7.
- migration — none; no spec outside this build carries a binding line today.
- user docs — the checker's header (S5). No page under `help/` covers the spec tokens leg.

## 6. Acceptance criteria

The plant criteria AC1 to AC11 are each observed by the parity probe §4 Fixtures describes, run
once per plant and once on the clean set.

- **AC1** — When the probe hands `scan_carries` the `ghost` plant, it returns a `ghost` finding
  naming `cl-dClosedLoop-9999`; the clean set returns none.
  Red when: an id no clause has is accepted as carried.
- **AC2** — When the probe hands it the `unbound` plant, it returns an `unbound` finding naming
  `unit-3.md`. Red when: a spec carrying nothing and derived from nothing passes.
- **AC3** — When the probe hands it the `stale` plant, it returns a `stale` finding naming the pin
  `@deadbeef` and the clause's current hash. Red when: a pin is compared with anything but the view.
- **AC4** — When the probe hands it the `ambiguous` plant, it returns an `ambiguous` finding naming
  two whole carriers; when it edits the clean set so a clause's two `part` carriers pin two hashes,
  it returns `ambiguous` naming two hashes.
  Red when: two whole carriers, or two pins of one clause, pass.
- **AC5** — When the probe hands it the `dropped` and `typo` plants, it returns a `stopped` finding
  for each, the `typo` one with the clause last carried two revisions back.
  Red when: only the newest revision is compared, so a later edit hides the earlier one.
- **AC6** — When the probe hands it the `token` plant, it returns a `token` finding naming the
  missing name. Red when: tokens are read from the carrier's binding lines rather than its text.
- **AC7** — When the probe hands it the `unmeasured` plant, its measured set is empty, and a scratch
  clone whose chain-build specs are deleted makes `python tools/check-spec-tokens.py` exit 1 with
  `REFUSING — the carries join measured no chain spec`.
  Red when: an empty population reports zero findings and exits 0.
  fixture: a scratch clone under `%TEMP%`.
- **AC8** — When the probe hands it the `crossbuild` plant, it returns a `crossbuild` finding naming
  the other build's clause. Red when: a clause of another build counts as carried with no Moved line.
- **AC9** — When the probe hands it the `moved` plant, it returns no finding; the `moved-token`
  plant returns a `token` finding read from the receiving build's carrier.
  Red when: a moved clause's token is read from its owner build's folder.
- **AC10** — When the probe hands it the `uncarried` and `node` plants with `exit_mode=True`, it
  returns an `uncarried` and a `node` finding; with `exit_mode=False` it returns neither.
  Red when: an exit arm fires outside a Design exit, or not at one.
- **AC11** — When the probe edits the clean set to hold a part sequence `part 1/3` and `part 3/3`, a
  carry of a withdrawn id, a malformed `**Carries:**` line and a `WONTDO` second whole carrier, it
  returns `parts`, `withdrawn` and `malformed` findings, and no `ambiguous` finding for the
  `WONTDO` spec. Red when: a `WONTDO` spec still carries, or a malformed line reads as unbound.
  fixture: the withdrawn id needs a design whose withdrawn set is non-empty; the probe passes
  `scan_carries` a copy of the design value with one id added to its `retired` set.
- **AC12** — When the probe hands `scan_carries` the clean set, `fixture(builds, nodes, "dTrueNorth", None)`,
  it returns no finding over two specs measured.
  Red when: a correct spec set reds, so every plant above would pass by a red that is not its own.
- **AC13** — When a probe calls `derive_carries_coverage` over the tree at the observation commit,
  its `dTrueNorth` entry lists, field for field, what `carries.py --report dTrueNorth` prints there:
  carried whole and split, released, uncarried, stale, ambiguous, unnamed nodes, derived and blind.
  Red when: a field is computed differently from `carries.py:293-312`.
  figure: the values are DERIVED at observation.
- **AC14** — When `python tools/check-spec-tokens.py` runs over the tree after this build's seven
  specs are committed, it prints the carries join line with `7 chain spec(s) measured in 1 build(s)`
  and `SPEC_CARRIES_CUTOFF 2026-10-21`, and exits 0 when nothing else is wrong; in a scratch clone
  with one unit's pin changed to `@deadbeef` it exits 1 naming `carries <- stale:` and that clause.
  Red when: the join is not wired into `main()`, or its hits skip the exit decision.
  figure: 7 is DERIVED from the build's roster at observation.
- **AC15** — When the same scratch clone's `.memory-tree.conf` sets `SPEC_CARRIES_CUTOFF=""`, the
  checker prints `SPEC_CARRIES_CUTOFF blank (arm off)` on the carries line and grades no carry; set
  to `2026-10-2`, it exits 1 with `REFUSING — SPEC_CARRIES_CUTOFF 2026-10-2 is not an ISO date`.
  Red when: a blank key grades, or a malformed date reads as off.
- **AC16** — When a waiver row keyed `carries <- stale:<that clause>` is added in that clone, the
  stale hit reads WAIVED under `--list` and the checker exits 0; a row keyed on the bare spec path
  does not waive it. Red when: the hit's token collides with a `[path]` waiver.
- **AC17** — When `grep -n 'carries' tools/check-spec-tokens.py` runs over the module header, it
  finds the ninth join's entry naming its population, `SPEC_CARRIES_CUTOFF`, and the two limits:
  the semantic blind side and the rename.
  Red when: the header's join catalogue does not name the join.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `spec-tokens self-test` · `lexicon naming predicates` · `memory hygiene`

New arm: tools/check-spec-tokens.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 AC11 AC12 AC14 AC15 AC16 · scratch repositories whose conf arms SPEC_CARRIES_CUTOFF over a two-build fixture view, a fixture record at a fixture baseline and a fixture deriver, each arm's plant staged by its own spec edit and observed green once restored · none

The arm reads its own scratch fixtures, never the instrument, so it outlives `carries.py`'s
retirement by dIndexedDesign. AC10, AC13 and AC17 are probes the close reads directly.

## 8. Open questions

- **FACT-QUESTION · F1 — Is `DRAFT`, the status the spec brief names, a legal spec status?** Probe:
  `grep -n 'OPEN · SPECCED' memory/HYGIENE.md` prints the seven tokens a spec header reuses
  (HYGIENE.md line 105). Liveness: the line would print `DRAFT` if the vocabulary declared it.
  Observed: it does not. RESOLVED (agent, 2026-10-21, delegated): `OPEN`, which TEMPLATE-SPEC gives
  as "drafting".
- **F2 — Which statuses carry a clause?** (a) Every status, as the instrument reads. (b) Every status
  but `WONTDO`. (c) Live specs only, the checker's other joins' population. (c) loses every carrier
  at its unit's close, so the build's own landing reads uncarried; veto 1 discards it. (a) makes a
  superseded unit's spec, which M2 retires by a status flip that leaves its text as it was, collide
  with its successor as `ambiguous`, so retiring a carrier would need a text edit the status flip
  exists to avoid. (b) keeps the instrument's thirteen plants, none of which involves a status, and
  lets a supersession read clean; a clause a retired unit carried and nothing else does reads
  `uncarried` at the Design exit. Recommendation (b). Rung 3.
  RESOLVED (agent, 2026-10-21, delegated): (b).
- **F3 — What does deviation 3's `**Follow-through:**` row say?** The record departs from
  `cl-dClosedLoop-0002@6acd9ea9`, and `asbuilt.py:58-62` refuses a record departing from a clause
  with no `amends` or `supersedes` row. (a) `amends` with a new clause text naming the thirteen
  plants: the view's hash moves, so the product join wants a new pin while `carries.py`, which reads
  v2 and not the view, wants `6acd9ea9`, and `carries.py --build dTrueNorth --exit` at the Design
  exit, a packet gate, reds whichever pin is chosen. (b) `gap gap-design-13`: `asbuilt.py --check`
  reds the record as a departure with no row. (c) `amends cl-dClosedLoop-0002@6acd9ea9` with an
  `**After:**` that is the clause's text unchanged, the stricter acceptance stated in its Reason and
  Evidence: the view cites the record on the clause's row, the text and the hash stay, and both
  joins agree on the pin. Veto 1 discards (a) and (b). Recommendation (c), which is also the true
  reading: the clause stands as written, and the spec does more. Rung 3.
  RESOLVED (agent, 2026-10-21, delegated): (c).

## 9. Revision log

- rev-1 · 2026-10-21 · initial draft.

## 10. Reuse audit

Probe: `python tools/codebase-map/reuse_lookup.py "join each spec to the sibling or upstream record
it names behind a dated cutoff"` ranked `tree_lib.parse_spec_h1` and `read_fork_cutoff` among general
helpers, and no join from a spec to a design. The seam this unit extends is the spec tokens leg's
join set in `tools/check-spec-tokens.py`: the hands-off join's key reader `read_cutoff_key`, its fold
into `hits` before the waiver pass, its composite hit token and its every-run report line, all at the
lines §4 Evidence cites. The arms are the instrument's, `carries.py:225-290`, ported, and the plant
suite is the instrument's `fixture()`, called rather than copied. The recall query's hits were the
brief, the packet, v2 and the view; none named a product join, and none disagreed with source on the
lines cited.

Recall terms used: `python tools/memory-recall/query.py "which join of the spec tokens leg reads a
spec against another document behind a cutoff" --terms "spec tokens leg handoff join cutoff carries
ghost stale pin unbound dropped clause plant"`
