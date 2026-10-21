# TOOL-dTrueNorth-10 — deviation records 2 and 3, written verbatim at kind `deviation`, the view re-rendered in their commit

**Status:** OPEN · rev-3 · 2026-10-21 · node d · Tier-2 · base 271aa59d · streams tooling · order 4

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-21-build-TOOL-dTrueNorth-10-deviation-9.md](../build/2026-10-21-build-TOOL-dTrueNorth-10-deviation-9.md) | deviation | — |
| [2026-10-21-prompt-TOOL-dTrueNorth-10-build-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-10-build-brief.md) | journal | — |
| [2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md](../reviews/2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md) | spec-audit | TOOL-dTrueNorth-8 TOOL-dTrueNorth-9 TOOL-dTrueNorth-11 TOOL-dTrueNorth-12 TOOL-dTrueNorth-13 TOOL-dTrueNorth-14 TOOL-dTrueNorth-15 TOOL-dTrueNorth-16 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dTrueNorth/reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md`)
confirmed finding **id 12 at HIGH**, its item **H3**: deviation records 2 and 3 exist nowhere, and no
spec writes them. The spec commit `7bf32c437` deferred both to `TOOL-dTrueNorth-4`'s pass, but that
unit's S10 writes only deviation-1 and deviation-4, its Migration upgrades the kind of a deviation-2
file that is not in the tree, and `TOOL-dTrueNorth-7` §4 Rollout step 4 says deviation-2 "was written
with this spec". No spec carries either record's text. Without them the departure from
`cl-dClosedLoop-0002` (D3) and the new-unit departure for `TOOL-dTrueNorth-7` go unrecorded, the view's
`cl-dClosedLoop-0002` row cites no record, and the close's departures join lists both with no record
behind them. This unit carries both records' text, writes them at kind `deviation` from their first
commit, and re-renders the view in the same commit. It repairs `TOOL-dTrueNorth-4`. The same defect
at MEDIUM, id 2 (item M1), is batched into `TOOL-dTrueNorth-16`.

## 2. Scope (IN)

- **S1** — Deviation-2, byte for byte the text under §4 "The records", at
  `memory/builds/dTrueNorth/build/2026-10-21-build-TOOL-dTrueNorth-7-deviation-2.md`, its binding
  `**Serves:** deviation TOOL-dTrueNorth-7` from its first commit. Observed by AC1 and AC2.
- **S2** — Deviation-3, byte for byte, at
  `memory/builds/dTrueNorth/build/2026-10-21-build-TOOL-dTrueNorth-2-deviation-3.md`, its binding
  `**Serves:** deviation TOOL-dTrueNorth-2`. Its `**After:**` is the clause's text unchanged, the
  reading `TOOL-dTrueNorth-2` §8 F3 resolved to (c), so the view cites the record on the clause's row
  and the hash stays `6acd9ea9`. Observed by AC1, AC2, AC3 and AC4.
- **S3** — The same commit re-renders `DESIGN_VIEW` with `gen_build_index.py --write` and stages it,
  the rule `TOOL-dTrueNorth-8` S1 states and hygiene check 9 enforces at the commit. Observed by AC3.
- **S4** — The two sentences these records falsify are superseded, not edited: `TOOL-dTrueNorth-4`
  §4 Migration's upgrade step finds no file of another kind, because both records carry `deviation`
  from their first commit, and `TOOL-dTrueNorth-7` §4 Rollout step 4's "was written with this spec"
  reads "is written by `TOOL-dTrueNorth-10`". Observed by AC2.

## 3. Non-goals (OUT)

- Deviation-1 and deviation-4: `TOOL-dTrueNorth-4` S10 writes them.
- Any field outside the grammar `TOOL-dTrueNorth-4` S1 states; this unit adds no field.
- Editing the frozen specs of units 4 and 7; S4 records the superseded readings here.
- Records for the units this build's spec audit promoted. Each `rescope · item add` row is a
  population member the close records, by README build-level rule 4.

### Edges

- **consumes-from** `TOOL-dTrueNorth-4` — the record grammar `read_record` grades and the kind `deviation` in `RECORD_KIND_TOKENS`; without them check 21 reads both records as malformed
- **consumes-from** `TOOL-dTrueNorth-6` — the generator whose `--write` re-renders `DESIGN_VIEW` over the new records; without it the instrument would be the view's writer
- **hands-off** `TOOL-dTrueNorth-16` — the four records in the tree, which its item for id 2 observes and its item for id 33 reads on the view's `cl-dClosedLoop-0002` row
- **hands-off** `TOOL-dTrueNorth-20` — the decline route for deviation-3's approval carried for the owner's walk (the round-2 spec audit's id 45)

## 4. Design

### Evidence

- The execution plan's `[deviations]` table states both departures: the extra unit's record 2,
  hand-off design-to-spec, follow-through "new unit <its id>", approver owner citing ER:232, ER:320
  and P0.8's row 1 (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:1279`);
  and the D3 departure "carried, not asked, for the owner's walk", recorded with its author as
  approver under `author-recorded` (`:1289-1294`).
- P0.8's row 1 is `PLAY-dClosedLoop-2`, which names `TOOL-dTrueNorth-7` (`memory/DECISIONS.md:230`),
  so the owner citation passes P0.1 row 6.
- The clause text of `cl-dClosedLoop-0002` is the view's row text
  (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md:10`), and v2's
  dTrueNorth row plans six units (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1764`).
- The instrument finds no row owed for a record whose `**Departs from:**` is not a clause
  (`asbuilt.py:58-62`), so deviation-2, departing from a build slug, renders no row and moves only
  the head's count.

### The records

`memory/builds/dTrueNorth/build/2026-10-21-build-TOOL-dTrueNorth-7-deviation-2.md`:

```markdown
# TOOL-dTrueNorth-7 deviation 2 — the extra unit, the carry-forward of a unit a spec run adds

**Serves:** deviation TOOL-dTrueNorth-7

- **Departs from:** `dTrueNorth` [roster]
- **Hand-off:** design-to-spec
- **Before:** dTrueNorth's row of v2's `[chain]` plans six units, one for each of `cl-dClosedLoop-0001` to `cl-dClosedLoop-0006`, and no unit for the carry-forward of a unit a spec run adds
- **After:** dTrueNorth's roster carries seven units, the six and `TOOL-dTrueNorth-7`, the carry-forward condition for every unit a spec run adds, once, and the starting-roster reading it rests on, derived from `PLAY-dClosedLoop-2`
- **Cause:** owner ruling
- **Reason:** Every chain build after dTrueNorth runs twice, a spec run and a build run, and today's carry-forward term cannot close the spec run: its starting roster is read from a generated region that names no unit before a build has a spec, and it refuses every unit a run added (plan review H1). The owner approved an extra unit that makes both work, after calling the gap a bug, and widened it to the units a spec run adds from a review or a discovery.
- **Evidence:** the owner's "dTrueNorth's extra unit (Recommended)" (ER:232), after "that sounds like a bug" (ER:196-197), widened by "Carry it too (Recommended)" (ER:320); the decision row `PLAY-dClosedLoop-2` (`memory/DECISIONS.md:230`); the execution plan's `[deviations]` table, deviation record 2 (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:1279`); TOOL-dTrueNorth-7 §1
- **Risk:** additive
- **Approver:** owner, `PLAY-dClosedLoop-2`, the decision row recording ER:232 and ER:320 that names TOOL-dTrueNorth-7, as P0.1 row 6 requires
- **Follow-through:** new unit TOOL-dTrueNorth-7
- **Caused-by:** PLAY-dClosedLoop-2
```

`memory/builds/dTrueNorth/build/2026-10-21-build-TOOL-dTrueNorth-2-deviation-3.md`:

```markdown
# TOOL-dTrueNorth-2 deviation 3 — the product join takes the instrument's plant suite as its acceptance

**Serves:** deviation TOOL-dTrueNorth-2

- **Departs from:** `cl-dClosedLoop-0002@6acd9ea9` [acceptance]
- **Hand-off:** design-to-spec
- **Before:** the carries join, a further join of the spec tokens leg behind that cutoff as the handoff join is: a ghost id, an unbound spec, a stale pin, two specs carrying one clause whole, or pinning it to two hashes, and a revision that stops carrying a clause with no decision each red, a token of a clause missing from its carriers red, and a run that measured no spec never green, each seen on its planted case over a fixture spec set (the owner's FQ-2, P41)
- **After:** the carries join, a further join of the spec tokens leg behind that cutoff as the handoff join is: a ghost id, an unbound spec, a stale pin, two specs carrying one clause whole, or pinning it to two hashes, and a revision that stops carrying a clause with no decision each red, a token of a clause missing from its carriers red, and a run that measured no spec never green, each seen on its planted case over a fixture spec set (the owner's FQ-2, P41)
- **Cause:** review finding
- **Reason:** The product join takes the bootstrap instrument `carries.py`'s thirteen plants as its acceptance (D3), each with the verdict the instrument gives it, which is stricter than the clause's red cases: a `crossbuild` plant, a `moved` green control and a `moved-token` plant are among them, and the clause names none of the three. The clause's text stands, so the view cites this record on the clause's row and the clause's hash stays `6acd9ea9`, the pin both the instrument and the product join read.
- **Evidence:** the execution plan's `[deviations]`, "Carried, not asked, for the owner's walk" (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:1289-1294`); the instrument's plants (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-carries.py`, `PLANTS`); TOOL-dTrueNorth-2 §1 and §8 F3
- **Risk:** stricter
- **Approver:** spec writer, the gov-spec-writer role of dTrueNorth's whole run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); carried for the owner's walk unless it rules otherwise
- **Follow-through:** amends cl-dClosedLoop-0002@6acd9ea9
- **Caused-by:** PLAY-dClosedLoop-1
```

### Files touched (estimate)

- `memory/builds/dTrueNorth/build/2026-10-21-build-TOOL-dTrueNorth-7-deviation-2.md` (new)
- `memory/builds/dTrueNorth/build/2026-10-21-build-TOOL-dTrueNorth-2-deviation-3.md` (new)
- `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md` (re-rendered by `--write`, never edited)

### Alternatives rejected

- **The records beside their units' specs, written by the spec writers of units 2 and 7.** Those
  specs are frozen at their audited revision; carrying the text there would be a fold the method's
  M4 refuses for a promoted finding.
- **A risk of `loosening` on deviation-2.** The extra unit adds a mechanism and relaxes no bound
  the clauses state, which is the grammar's `additive`; the owner's approval meets every class.

## 5. Production-readiness checklist

- security — no new write path; two records under this build's own `build/` folder.
- perf / scale — two files and one render.
- error / empty / loading states — a field outside its closed set is a malformed line under
  `TOOL-dTrueNorth-4`'s `read_record`, which AC2 reads.
- observability — the view cites deviation-3 on `cl-dClosedLoop-0002`'s row and counts every record
  in its head.
- risks — a byte of drift in deviation-3's `**After:**` moves the clause's hash in the view, which
  reds every carrier's pin; AC4 reads the hash.
- testing — AC1 to AC4 as probes of the tree after the pass.
- migration — none: both records carry the kind from their first commit.
- user docs — none; the records are this build's own.

## 6. Acceptance criteria

- **AC1** — When `git ls-files 'memory/builds/dTrueNorth/build/*-deviation-*.md'` runs after the pass,
  it lists deviation-1, deviation-2, deviation-3 and deviation-4.
  Red when: either record of S1 or S2 is absent from the pass's commit.
  figure: four is DERIVED from `TOOL-dTrueNorth-4` S10 and this unit.
- **AC2** — When `python3 "tools/memory-tree/deviation_join.py" --approval by-risk` runs on the tree,
  no `refused:` or malformed line names `2026-10-21-build-TOOL-dTrueNorth-7-deviation-2` or
  `2026-10-21-build-TOOL-dTrueNorth-2-deviation-3`, and `python3 tools/memory-tree/gen_build_index.py --print-bindings`
  prints no `A` row for either.
  Red when: a field falls outside its closed set, the owner citation names a row that does not name
  `TOOL-dTrueNorth-7`, or a record's kind is not `deviation`.
- **AC3** — When `grep -n 'cl-dClosedLoop-0002' memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`
  runs after the pass, the row's last cell cites `2026-10-21-build-TOOL-dTrueNorth-2-deviation-3`, and
  `python3 "tools/memory-tree/asbuilt_view.py" --check` exits 0.
  Red when: the commit lands the records without re-rendering the view, so the row reads `baseline`.
- **AC4** — When `python3 "tools/memory-tree/design_lib.py" --design --build dTrueNorth` runs after the
  pass, `cl-dClosedLoop-0002` reads hash `6acd9ea9` with its since cell citing deviation-3.
  Red when: deviation-3's `**After:**` differs by one byte from the clause's text, so the view moves
  the hash and every carrier's pin reads stale.

## 7. Gates

`memory hygiene` · `routed commits name a specced unit` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

No suite arm lands with this unit: the records are data, read by the arms `TOOL-dTrueNorth-4` and
`TOOL-dTrueNorth-6` declare. AC1 to AC4 are the probes the close reads for this unit.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join of
  `TOOL-dTrueNorth-2` reds a chain spec carrying nothing and derived from nothing. (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, the owner's ruling that a run carries the units it adds (ER:320).
  (b) None. (c) A `part k/n` carry of the repaired unit's clause. (b) reds `unbound` and (c) reds
  `parts` against the repaired unit's whole carrier; veto 1 discards both. Recommendation (a).
  Rung 3. RESOLVED (agent, 2026-10-21, delegated): (a). widens: none · relaxes: none
- **F2 — Which filenames do the records take?** (a) The names the spec brief, `TOOL-dTrueNorth-4`'s
  Files touched and the execution plan already spell, dated 2026-10-21. (b) The pass's own date.
  (b) strands the path `TOOL-dTrueNorth-4` §4 Migration names. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-21, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-21 · initial draft, promoted from the round-1 spec audit's id 12 (HIGH, item H3).
- rev-2 · 2026-10-21 · §3 · the Edges block gains a hands-off to TOOL-dTrueNorth-20, promoted by the
  round-2 spec audit, the mirror of its consumes-from; no other section moves.
- rev-3 · 2026-10-21 · §6 · the acceptance criteria name the modules this build creates (`deviation_join.py`, `asbuilt_view.py`, `design_lib.py`) quoted or bare, and a `git show`/`json.load` argument quoted, so the spec-tokens paths join, which reads the live tree at every `--dispatch`, stops refusing every unit before those modules exist. No criterion's observation moves.

## 10. Reuse audit

Probe: no existing seam fits, and none is needed: the unit writes two records in the grammar
`TOOL-dTrueNorth-4` S1 owns and reuses `TOOL-dTrueNorth-6`'s `--write` for the render. The texts are
taken from the execution plan's `[deviations]` table and from deviation-1 and deviation-4's shape in
`TOOL-dTrueNorth-4` §4, so the four records read one grammar. `python tools/codebase-map/reuse_lookup.py
"re-render a generated view in the commit that changes its inputs"` ranked `render_family_view`, the
same render-in-the-commit precedent `TOOL-dTrueNorth-8` cites; the map does not scan `memory/`, so no
record was visible to it, the one place the probe and the tree disagree.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit and its generated view kept fresh" --terms "spec-audit promoted unit repairs order
as-built view deviation record re-render guard selftest pin"`
