# TOOL-dTrueNorth-3 — the coverage region in each chain build's README, and the INPROGRESS refusal

**Status:** CLOSED · rev-2 · 2026-10-21 · node d · Tier-2 · base 271aa59d · streams tooling · order 1

**Carries:** cl-dClosedLoop-0003@d2811290 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-21-build-TOOL-dTrueNorth-3-ledger.md](../build/2026-10-21-build-TOOL-dTrueNorth-3-ledger.md) | journal | — |
| [2026-10-21-prompt-TOOL-dTrueNorth-1-spec-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-1-spec-brief.md) | research | TOOL-dTrueNorth-1 TOOL-dTrueNorth-2 TOOL-dTrueNorth-4 TOOL-dTrueNorth-5 TOOL-dTrueNorth-6 TOOL-dTrueNorth-7 |
| [2026-10-21-prompt-TOOL-dTrueNorth-3-build-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-3-build-brief.md) | journal | — |
| [2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md](../reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md) | spec-audit | TOOL-dTrueNorth-1 TOOL-dTrueNorth-2 TOOL-dTrueNorth-4 TOOL-dTrueNorth-5 TOOL-dTrueNorth-6 TOOL-dTrueNorth-7 |
| [2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md](../reviews/2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md) | diff-review | TOOL-dTrueNorth-1 TOOL-dTrueNorth-2 TOOL-dTrueNorth-4 TOOL-dTrueNorth-5 TOOL-dTrueNorth-6 TOOL-dTrueNorth-7 TOOL-dTrueNorth-8 TOOL-dTrueNorth-9 TOOL-dTrueNorth-10 TOOL-dTrueNorth-11 TOOL-dTrueNorth-12 TOOL-dTrueNorth-13 TOOL-dTrueNorth-14 TOOL-dTrueNorth-15 TOOL-dTrueNorth-16 TOOL-dTrueNorth-17 TOOL-dTrueNorth-18 TOOL-dTrueNorth-19 TOOL-dTrueNorth-20 |

<!-- /gen:spec-records -->

## 1. Goal

The owner reads a chain build's coverage at each spec landing, and today it exists only as the
instrument's `carries.py --report <slug>` output pasted into a packet. This unit renders it into
every chain build's README as a generated region beside its unit ids, `<!-- gen:build-coverage -->`,
every field the clause names with an explicit none. It also makes memory hygiene refuse a chain
build's spec at `INPROGRESS`, which is past the build's Design exit, while that build's coverage is
red. Both read one value, `derive_carries_coverage` from `TOOL-dTrueNorth-2`, so the region and the
refusal cannot disagree.

## 2. Scope (IN)

- **S1** — The region pair, `<!-- gen:build-coverage -->` and `<!-- /gen:build-coverage -->`,
  registered in `GEN_REGIONS` (`tools/memory-tree/gen_build_index.py:101-105`) directly after
  `build-index`, whose units table carries the unit ids. `render_order` and `render_edges` find
  their own pairs by name rather than by tuple index (`:1545`, `:1576`). Observed by AC1, AC4.
- **S2** — `read_carries_coverage(root, conf)`, the one read the render and the refusal share. Blank
  `SPEC_CARRIES_CUTOFF` returns the off state without resolving anything. Set, it loads
  `check-spec-tokens.py` from the kit directory's parent by path and calls its
  `derive_carries_coverage`, as `read_landed_unclosed` (`:1678-1713`) reaches a sibling kit only
  under its key. A checker that does not resolve, or a refusal it raises, is a named `Problem`
  before anything is written. Observed by AC5, AC8.
- **S3** — `render_coverage`, the body: one line naming the build, its clause, owned-node and spec
  counts and the cutoff, then one bullet per field the clause lists. The fields are the clauses
  carried whole, the clauses carried in parts with their ids, the clauses a release line names
  with their decisions, the uncarried, stale and ambiguous clauses each as a count with its
  ids, the owned nodes no carrier names, the specs derived from no clause with their decisions, and
  the clauses the token arm cannot see. An empty field reads `none`. Every line stays within
  `IDS_WRAP`, a long list wrapping onto two-space continuation lines through `_render_wrapped_ids`,
  extended with a separator, an indent and an end argument whose defaults keep its present
  callers' output (`gen_build_index.py:1457`, `:1462`, `:3545`). Observed by AC2, AC3.
- **S4** — Where the region lives. `--write` creates the pair in a chain build's README, a build
  `read_design_view`'s Build column names, and in no other README. `--check` byte-compares it
  wherever it stands, and names as a `Problem` a chain README that lacks the pair and a non-chain
  README that holds one (§8 F2). With the cutoff blank, no README gains a pair, and one that holds
  a pair renders a single line saying coverage is not read and which key is blank. Observed by AC1,
  AC4, AC5.
- **S5** — The refusal. `cmd_check_coverage`, a new `--check-coverage` verb, reads the same value
  and, for each chain build with a spec at `INPROGRESS` whose findings, read at the Design exit, are
  not empty, prints that spec and each finding's arm and reference, and exits 1. Off, it prints one
  line naming the blank key and exits 0; a `Problem` exits 2. Hygiene check 29 in
  `tools/memory-tree/check-memory-hygiene.sh` delegates to it as checks 24 and 26 delegate, and
  fails on 1 or 2. Under `--staged` it runs when a staged path sits under a build's `spec/` folder or
  is the conf, and otherwise prints one held line. Observed by AC6, AC7, AC8.
- **S6** — The readers of the region set. Check 6's authored-byte pricing awk
  (`check-memory-hygiene.sh:1023-1025`) counts the new pair as generated. `check_index_input`
  (`gen_build_index.py:831-857`) treats a staged `check-spec-tokens.py` as a build-index input
  while the cutoff is set, because the region renders from its join. Observed by AC9, AC11.
- **S7** — The prose homes: item 29 in `tools/memory-tree/HYGIENE.template.md`'s check catalogue,
  items 6 and 9 naming four regions, all rendered into `memory/HYGIENE.md`; and the
  `--check-coverage` verb in `tools/memory-tree/README.md` beside the generator's other verbs.
  Observed by AC10.

## 3. Non-goals (OUT)

- The join and the coverage fields' computation: `TOOL-dTrueNorth-2`'s `derive_carries_coverage`.
  This unit renders and refuses; it computes no field.
- The parser and the chain-build list: `TOOL-dTrueNorth-1`'s.
- A verdict line in the region. The refusal prints the findings it reads; the region carries the
  clause's fields and nothing beyond them.
- Refusing a spec at any other status. `OPEN`, `SPECCED` and `BLOCKED` precede the Design exit, and
  a terminal or `DEFERRED` spec is not building.
- The packet's Coverage section. It stays `carries.py --report`'s output until the report-switch step
  the execution plan schedules at this build's landing, which is dClosedLoop's to make.
- Splitting this clause into two units. One writer cannot mint ids, and the README's roster places
  one unit per clause (§8 F3).

### Edges

- **consumes-from** `TOOL-dTrueNorth-1` — `read_design_view`'s Build column, which names the chain builds whose README carries the region
- **consumes-from** `TOOL-dTrueNorth-2` — `derive_carries_coverage`, the fields this region renders and the findings check 29 reads
- **hands-off** `TOOL-dTrueNorth-11` — the guards of the two self-test legs this unit's arms run in, which must name `check-spec-tokens.py` (the round-1 spec audit's id 28)
- **hands-off** `TOOL-dTrueNorth-15` — `cmd_check_coverage`'s graded count on every run (the round-1 spec audit's id 41)
- **hands-off** `TOOL-dTrueNorth-16` — `read_carries_coverage` and check 29, which that unit amends for the round-1 spec audit's ids 6, 10, 18, 29, 37, 44 and 45

## 4. Design

### Evidence

- `GEN_REGIONS` declares three regions in canonical order (`gen_build_index.py:101-105`).
  `insert_region` places a missing pair after the nearest earlier registered region's close
  (`:2224-2244`), and `plan()` creates a missing pair for every registered region under
  `create_missing` (`:2372-2376`) and renders each region a README holds (`:2377-2391`).
- `render_order` and `render_edges` address their own pairs as `GEN_REGIONS[1]` and
  `GEN_REGIONS[2]` (`:1545`, `:1576`), so an insertion at index 1 moves them unless they look up
  by name.
- `slot_violations` reads every `GEN_REGIONS` pair as generated (`:2144-2161`), so a registered
  region is never authored content after the first generated marker.
- Check 6 prices a build README by its authored bytes, excluding the three named pairs
  (`check-memory-hygiene.sh:1004-1025`); a pair it does not name is priced as authored.
- Check 7 caps a build README line at 350 characters (`memory/HYGIENE.md` item 7), and generated
  lines are graded too, which is why `_render_wrapped_ids` (`gen_build_index.py:1507-1526`) wraps
  at `IDS_WRAP`, 300.
- `read_landed_unclosed` (`:1678-1713`) is the precedent for reaching code outside this kit only
  under a set key, refusing by name when it does not resolve.
- Checks 24 and 26 delegate to a sibling Python module and print its capture
  (`check-memory-hygiene.sh:1580-1634`). Check numbers 1 to 28 are taken
  (`memory/HYGIENE.md` items 1 to 28), so the next free number is 29.
- The 22 chain builds each hold a README with the `gen:build-index` pair and an authored
  `roster:units` pair (measured this pass, 2026-10-21, at `271aa59d`). The roster reader skips a
  README for its own slug only (`gen_build_index.py:767-803`); every id the region renders is a
  decision id already in a spec's own text, so no roster moves.

### Data model

The region, as it renders for a build with one derived spec and no other finding:

```markdown
Coverage of dTrueNorth's 6 clause(s) and 1 owned node(s), over 7 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 6
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 0 (none)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: none
- specs derived from no clause: `spec/2026-10-21-spec-TOOL-dTrueNorth-7.md` (PLAY-dClosedLoop-2)
- clauses the token arm cannot see: cl-dClosedLoop-0002
```

The body sits between the two markers, a blank line after the open marker as the order and edges
regions render theirs; the example leaves the markers out so this spec carries no column-0 marker
a region reader could take for a real one.

Each field is `carries.py --report`'s, one bullet each where the instrument joins three on a line,
and the uncarried, stale and ambiguous fields carry their count, as the clause asks. A released
clause renders `<id> <moved|retired|deferred> by <decision>`; a derived spec renders its path
relative to the build folder, in backticks, with its decision. The off form is the pair around
`*Coverage is not read: SPEC_CARRIES_CUTOFF is blank.*`.

`cmd_check_coverage`'s refusal, one line per refused spec:

```text
build-index: coverage — <spec path> is INPROGRESS while dTrueNorth's coverage is red: uncarried cl-dClosedLoop-0599; stale cl-…
```

Check 29's failure is `HYGIENE check 29 FAILED — a chain build's spec is INPROGRESS while its build's
coverage is red:` followed by those lines.

### Behaviour

- **One read per run.** `plan()` calls `read_carries_coverage` once and attaches each chain build's
  entry to its build record before the region loop, so `--check`, `--write` and `--check-coverage`
  read one value.
- **Creation is chain-only.** The `create_missing` loop skips `build-coverage` for a build the value
  does not name; the render loop then renders it for every README holding the pair, so the
  asymmetry is in creation alone.
- **Demanded where it belongs.** Under `--check`, a chain README with no pair is a `Problem` naming
  it and the `--write` that creates it. A non-chain README with a pair is a `Problem` naming the
  pair, so a region for nothing cannot sit unread.
- **Findings read at the Design exit.** The refusal reads the findings `derive_carries_coverage`
  returns with `exit_mode=True`, all arms, so an uncarried clause and an unnamed node count beside a
  stale pin. The region shows the clause's fields only.
- **Staged.** Check 29 under `--staged` runs when `STAGED_MD` holds a path under
  `<MEMORY_ROOT>/builds/*/spec/` or the staged set holds `.memory-tree.conf`; otherwise it prints
  `memory-hygiene: check 29: held under --staged, no chain spec or conf staged`.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `<!-- gen:build-coverage -->`, `<!-- /gen:build-coverage -->` | region markers | `gen_build_index.py` `GEN_REGIONS` |
| `read_carries_coverage` | function | `gen_build_index.py` |
| `render_coverage` | function, in `REGION_RENDERERS` | `gen_build_index.py` |
| `cmd_check_coverage` | function | `gen_build_index.py` |
| `--check-coverage` | CLI verb | `gen_build_index.py` |
| `sep`, `indent`, `end` | keyword arguments of `_render_wrapped_ids` | `gen_build_index.py` |
| check 29 | hygiene check | `check-memory-hygiene.sh`, `HYGIENE.template.md` |

Each function name leads with a verb the naming lexicon declares.

### Rollout

The unit's commit runs `gen_build_index.py --write`, which renders the region into the 22 chain
READMEs as shared renders (README rule 7). From then, check 9's `--check` keeps them current, and
every spec commit in a chain build re-renders its build's region with the index.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/memory-tree/HYGIENE.template.md`
- `tools/memory-tree/README.md`
- `memory/HYGIENE.md`

The 22 chain READMEs change inside the new pair only, as `--write` renders them.

### Alternatives rejected

- **The pair appended after `build-edges`.** No index-addressed reader moves, but it sits two
  regions from the unit ids, against "beside its unit ids".
- **The pair nested inside `build-index`, as `gen:build-units` is.** The index region's bytes would
  move on every coverage change, and the readers that bracket that region would read coverage as
  part of the index.
- **The refusal inside check 9.** Check 9 grades drift; a red coverage is not drift, and folding it
  there would make a drift message carry a coverage finding.

## 5. Production-readiness checklist

- security — no new write path beyond the README regions `--write` already owns. The checker is
  loaded by path only under a set key and refused by name when absent.
- perf / scale — one `derive_carries_coverage` per generator run, about a second today, which every
  `--check` and `--write` now pays while the key is set.
- error / empty / loading states — a build with no spec renders "over 0 spec(s)" with every clause
  uncarried; a blank key renders the off line; a resolution or join refusal is a named `Problem`.
- observability — the region itself; check 29 names each refused spec and finding; the held line
  under `--staged` announces the skip.
- risks — every chain spec commit now moves its README, so the index renders more often. A chain
  build at `INPROGRESS` with red coverage stops every full hygiene run, which is the clause's intent.
- testing — AC1 to AC11 over a scratch clone and the tree; the arms under §7.
- migration — the first `--write` adds the pair to the 22 chain READMEs; no authored byte moves.
- user docs — `memory/HYGIENE.md` item 29 and `tools/memory-tree/README.md`; no page under `help/`
  covers build READMEs.

## 6. Acceptance criteria

The clone criteria run in a scratch clone of the run branch under `%TEMP%`, short-named, at the
commit carrying this unit and its siblings' specs.

- **AC1** — When `python tools/memory-tree/gen_build_index.py --write` runs in the clone,
  `git diff --stat` lists the 22 chain READMEs and no other README, and every changed line sits between a new
  `<!-- gen:build-coverage -->` pair placed directly after that README's `<!-- /gen:build-index -->`.
  Red when: a non-chain README gains a pair, a roster or `ids:` line moves, or the pair lands
  elsewhere.
  figure: 22 is DERIVED from the view's Build column at observation.
- **AC2** — When the clone's `memory/builds/dTrueNorth/README.md` is read after `--write`, its region
  carries the nine field bullets of §4's data model, and a probe finds each value equal to the same
  field of `carries.py --report dTrueNorth` there, the counts aside.
  Red when: a field is missing, or its value differs from the instrument's.
- **AC3** — When `memory/builds/dConvergedCharter/README.md` is read after `--write`, its region
  reads `over 0 spec(s)`, its uncarried field counts every clause the view gives that build and lists
  them, and `awk 'length > 300'` over the region prints nothing.
  Red when: an empty field is absent rather than `none`, or a long list renders one line past 300.
- **AC4** — When `python tools/memory-tree/gen_build_index.py --check` runs in the clone after
  `--write`, it exits 0; with one byte of dTrueNorth's region hand-edited it exits 1 naming that
  README; with dGroundRules' pair deleted it exits 1 naming that README and `--write`.
  Red when: a hand edit passes, or a chain README without the pair passes.
- **AC5** — When the clone's `.memory-tree.conf` sets `SPEC_CARRIES_CUTOFF=""` and `--write` runs
  on a tree with no pair yet, no README gains one; on a tree holding the pairs, each region renders
  `*Coverage is not read: SPEC_CARRIES_CUTOFF is blank.*`.
  Red when: a blank key still resolves the checker, or a held pair renders a stale body.
- **AC6** — When `bash tools/memory-tree/check-memory-hygiene.sh --only 29` runs in the clone with
  `TOOL-dTrueNorth-1`'s header at `INPROGRESS` and one row planted in the as-built file, in its row
  shape, giving dTrueNorth the clause `cl-dClosedLoop-0599` with the text a planted clause, it fails with `HYGIENE check 29 FAILED` naming that spec and `uncarried cl-dClosedLoop-0599`; with
  the row taken out it passes.
  Red when: the planted uncarried clause does not stop an `INPROGRESS` spec.
  cost: one hygiene run with every producer, about a minute.
  fixture: the green half needs dTrueNorth's coverage otherwise clean; a red there is a sibling
  spec's finding and is reported as one.
- **AC7** — When the same planted row stands and every dTrueNorth spec is `OPEN`, the `--only 29`
  run passes, and the region's uncarried field reads `1 (cl-dClosedLoop-0599)`.
  Red when: a spec before its Design exit is refused.
- **AC8** — When `python tools/memory-tree/gen_build_index.py --check-coverage` runs in the clone, it
  exits 0 on the clean tree, 1 under AC6's plant, 0 with one line naming `SPEC_CARRIES_CUTOFF` when
  the key is blank, and 2 naming `DESIGN_VIEW` when that key names a missing file.
  Red when: a misconfiguration reads as a clean tree.
- **AC9** — When `bash tools/memory-tree/check-memory-hygiene.sh --only 6` runs in the clone over a
  chain README padded so its authored bytes sit under `BUILD_README_CAP_BYTES` and its authored bytes
  plus its coverage region sit over it, it passes.
  Red when: check 6 bills the coverage region to the authored half.
- **AC10** — When `grep -n 'gen:build-coverage' memory/HYGIENE.md tools/memory-tree/HYGIENE.template.md`
  runs, both name the pair in item 6, and `grep -n '^29\. ' memory/HYGIENE.md` prints check 29's
  catalogue entry; `grep -n 'check-coverage' tools/memory-tree/README.md` prints the verb.
  Red when: the check or the region has no prose home, or the rendered copy lags the template.
- **AC11** — When `python tools/memory-tree/gen_build_index.py --check --staged` runs in the clone
  with only `tools/check-spec-tokens.py` staged, it answers that a render is owed and does not print
  its SKIPPED line. Red when: a staged change to the join skips the render it moves.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `build-index selftest` · `build README slot contract` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC6 AC7 AC9 · check 29 over a fixture chain build at INPROGRESS with a planted uncarried clause, green without it and silent at OPEN, and check 6 over a padded README whose region would tip it over the cap · none

New arm: tools/memory-tree/gen_build_index.py (its selftest) · covers AC1 AC3 AC4 AC5 AC8 AC11 · a fixture tree whose conf arms the cutoff over a fixture view, staging a chain README with no pair, a non-chain README holding one, a hand edit, a blank key and a staged checker · none

## 8. Open questions

- **FACT-QUESTION · F1 — Is `DRAFT`, the status the spec brief names, a legal spec status?** Probe:
  `grep -n 'OPEN · SPECCED' memory/HYGIENE.md` prints the seven tokens a spec header reuses
  (HYGIENE.md line 105). Liveness: the line would print `DRAFT` if the vocabulary declared it.
  Observed: it does not. RESOLVED (agent, 2026-10-21, delegated): `OPEN`, which TEMPLATE-SPEC gives
  as "drafting".
- **F2 — Does `--check` demand the pair on a chain README?** The generator's rule for a new region is
  that `--check` never demands one (`gen_build_index.py:2325-2331`), so that registering a region
  forces no corpus-wide render. (a) Demand it on the 22 chain READMEs only. (b) Never demand it, as
  for every other new region. Under (b) a chain README without the pair passes every gate and shows
  the owner no coverage, the absence-reads-as-coverage class the generator's own comments refuse. The
  render (a) forces is 22 files, all shared renders README rule 7 admits. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-21, delegated): (a).
- **F3 — One unit for two mechanisms, the region and the refusal?** BUILD-METHOD M2 asks one
  mechanism per spec. (a) Keep both here, carrying the clause whole. (b) Carry it as `part 1/2` and
  `part 2/2` across this unit and a new one. (b) needs a unit id this writer cannot mint and a roster
  row the README fixes at one unit per clause. Both halves read one function, and the closing diff
  tells them apart by file: the generator's region code and the hygiene engine's check 29.
  Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-21, delegated): (a).
- **F4 — Does check 29 run under `--staged`?** (a) Held, announced, as checks 24 and 26 are. (b) Run
  when a staged path sits under a build's `spec/` folder or is the conf, held otherwise. (b) refuses
  the status flip to `INPROGRESS` at its own commit instead of at the push, for a second of work only
  when a spec is staged. Recommendation (b), the more capable. Rung 3.
  RESOLVED (agent, 2026-10-21, delegated): (b).
- **F5 — May this unit edit `memory/HYGIENE.md`, a governance carrier (BUILD-METHOD M11)?** Veto 2
  discards any option changing a governance carrier unless a grant lifts it. (a) Check 29 with no
  catalogue entry, its prose in the engine alone. (b) The catalogue entry and the region named in
  items 6 and 9, under this build's `may:` grant `PLAY-dClosedLoop-3`, which admits the
  governance-carrier changes a chain build's own clauses name; clause 0003 names memory hygiene's
  refusal. (a) leaves a check with no row in the file that calls itself the catalogue's prose home.
  Recommendation (b). Rung 3, veto 2 lifted by the grant.
  RESOLVED (agent, 2026-10-21, delegated): (b). grants: PLAY-dClosedLoop-3 memory/HYGIENE.md items 6, 9 and 29.

## 9. Revision log

- rev-1 · 2026-10-21 · initial draft.
- rev-2 · 2026-10-21 · §3 · the Edges block gains a hands-off to each unit the round-1 spec audit
  promoted against this one, TOOL-dTrueNorth-11, TOOL-dTrueNorth-15 and TOOL-dTrueNorth-16, the
  mirror of its consumes-from; no other section moves.

## 10. Reuse audit

Probe: `python tools/codebase-map/reuse_lookup.py "render a generated region into each build
README"` ranked general `render` and `region` helpers, and the recall query's hits named
`insert_region` and the `create_missing` splice as the region seam. The seam this unit extends is
`GEN_REGIONS` with its `REGION_RENDERERS` table and `plan()`'s create and render loops in
`tools/memory-tree/gen_build_index.py`, the keyed sibling read `read_landed_unclosed`, the wrapping
helper `_render_wrapped_ids`, and hygiene's delegation pattern of checks 24 and 26. One recall hit, a
2026-08-24 enforcement record, cites `insert_region` at `:1009-1029`; the function now sits at
`:2224-2244`, which §4 cites. No hit named a coverage renderer.

Recall terms used: `python tools/memory-recall/query.py "how does a generated region get rendered
into a build README and refused when absent" --terms "gen region build README render_region
GEN_REGIONS insert_region create_missing check 9 coverage INPROGRESS"`
