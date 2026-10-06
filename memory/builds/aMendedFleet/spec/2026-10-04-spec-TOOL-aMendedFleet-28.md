# TOOL-aMendedFleet-28 — the recall floor grades the served path, terms plus fusion

**Status:** CLOSED · rev-2 · 2026-10-04 · node a · Tier-2 · base 7af5f564 · streams tooling · advances TOOL-aProbedToolkit-10 · ratified 2026-10-04 · order 28

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aMendedFleet-28-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aMendedFleet-28-1-acceptance-ledger.md) | journal | — |
| [2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md](../reviews/2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md) | diff-review | KICK-aMendedFleet-1 KICK-aMendedFleet-2 KICK-aMendedFleet-3 KICK-aMendedFleet-4 PLAY-aMendedFleet-1 PLAY-aMendedFleet-2 PLAY-aMendedFleet-3 PLAY-aMendedFleet-4 TOOL-aMendedFleet-1 TOOL-aMendedFleet-2 TOOL-aMendedFleet-3 TOOL-aMendedFleet-4 TOOL-aMendedFleet-5 TOOL-aMendedFleet-6 TOOL-aMendedFleet-7 TOOL-aMendedFleet-8 TOOL-aMendedFleet-9 TOOL-aMendedFleet-10 TOOL-aMendedFleet-11 TOOL-aMendedFleet-12 TOOL-aMendedFleet-13 TOOL-aMendedFleet-14 TOOL-aMendedFleet-15 TOOL-aMendedFleet-16 TOOL-aMendedFleet-17 TOOL-aMendedFleet-18 TOOL-aMendedFleet-19 TOOL-aMendedFleet-20 TOOL-aMendedFleet-21 TOOL-aMendedFleet-22 TOOL-aMendedFleet-23 TOOL-aMendedFleet-24 TOOL-aMendedFleet-25 TOOL-aMendedFleet-26 TOOL-aMendedFleet-27 TOOL-aMendedFleet-29 TOOL-aMendedFleet-30 TOOL-aMendedFleet-31 TOOL-aMendedFleet-32 TOOL-aMendedFleet-33 TOOL-aMendedFleet-34 TOOL-aMendedFleet-35 TOOL-aMendedFleet-36 TOOL-aMendedFleet-37 TOOL-aMendedFleet-38 TOOL-aMendedFleet-39 TOOL-aMendedFleet-40 TOOL-aMendedFleet-41 TOOL-aMendedFleet-42 TOOL-aMendedFleet-43 TOOL-aMendedFleet-44 TOOL-aMendedFleet-45 TOOL-aMendedFleet-46 TOOL-aMendedFleet-47 TOOL-aMendedFleet-48 TOOL-aMendedFleet-49 TOOL-aMendedFleet-50 TOOL-aMendedFleet-51 TOOL-aMendedFleet-52 TOOL-aMendedFleet-53 TOOL-aMendedFleet-54 TOOL-aMendedFleet-55 TOOL-aMendedFleet-56 TOOL-aMendedFleet-57 TOOL-aMendedFleet-58 TOOL-aMendedFleet-59 TOOL-aMendedFleet-60 TOOL-aMendedFleet-61 TOOL-aMendedFleet-62 TOOL-aMendedFleet-63 TOOL-aMendedFleet-64 TOOL-aMendedFleet-65 TOOL-aMendedFleet-66 TOOL-aMendedFleet-67 TOOL-aMendedFleet-68 TOOL-aMendedFleet-69 TOOL-aMendedFleet-70 TOOL-aMendedFleet-71 TOOL-aMendedFleet-72 TOOL-aMendedFleet-73 TOOL-aMendedFleet-74 TOOL-aMendedFleet-75 TOOL-aMendedFleet-81 TOOL-aMendedFleet-82 TOOL-aMendedFleet-83 TOOL-aMendedFleet-84 TOOL-aMendedFleet-85 TOOL-aMendedFleet-86 TOOL-aMendedFleet-87 TOOL-aMendedFleet-88 TOOL-aMendedFleet-89 TOOL-aMendedFleet-90 TOOL-aMendedFleet-91 TOOL-aMendedFleet-92 TOOL-aMendedFleet-93 TOOL-aMendedFleet-94 TOOL-aMendedFleet-97 TOOL-aMendedFleet-98 TOOL-aMendedFleet-99 TOOL-aMendedFleet-100 TOOL-aMendedFleet-101 TOOL-aMendedFleet-102 TOOL-aMendedFleet-103 TOOL-aMendedFleet-104 TOOL-aMendedFleet-105 |

<!-- /gen:spec-records -->

## 1. Goal

The one merge-bar leg that asks whether orientation returns the right thing grades a configuration
no session is served. `tools/memory-recall/check-recall.py` ranks the bare fixture question over the
`records` set alone through `bench.rank_with`, while `tools/memory-recall/query.py` refuses a query
without `--terms` and serves `run_fusion`: the records arm and the rolled-up chunk arm, fused by
`rrf`. This unit makes the floor rank every graded question through the CLI's own `query_expr` and
`run_fusion`, with the terms a session would supply, and gives the fixture the headroom the owner's
no-saturation ruling demands before any pin over it means anything. It advances
`TOOL-aProbedToolkit-10`, whose second half, family coverage of the fixture's ids, it does not do.

## 2. Scope (IN)

- **S1** — the `RECALL_FLOOR` grammar admits a `served` head: `served:<metric>@<k>>=<value>`. The
  single-pair head `<set>:<substrate>` still parses, so the shipped shape and any adopter conf
  carrying it are untouched. A malformed `served` pin refuses naming the field, as the single-pair
  branch of `parse_pin` already does. Observed by AC1 and AC6.
- **S2** — under a `served` pin, `build_served_dir` builds the CLI's two sqlite sets in a scratch dir
  with `query.build_cache`, over `extract.corpus_inputs` of the root. `measure_served` ranks every
  graded row with `query.run_fusion(dir, query.query_expr(question, terms), k)`. Nothing about
  ranking, rollup or fusion is restated in `check-recall.py`; it imports the served functions, so a
  change to any of them moves the floor. Observed by AC1 and AC2.
- **S3** — a fused hit satisfies an expected id under `bench.expected_by_target`'s two rules: its
  `id` equals the expected id, or its `id` is empty, its path is one where the id is anchored and its
  text carries the id. The anchor map is read from the served `records.db` `meta` table, and a hit
  whose `id` column is empty is handed to `expected_by_target` without an `id` key, so the anchor
  rule is the one that judges it. Predicate 4 resolves an expected id against that same map.
  Observed by AC1 and AC2.
- **S4** — every fixture question carries two term lists: `terms`, the strong rewrite a session
  writes after reading the corpus, and `naive_terms`, written from the question alone by an author
  who has not read the record that answers it. Each list's length sits inside `query.TERM_BAND`,
  imported rather than restated. Under a `served` pin, `read_fixture` refuses a question missing
  either list, or carrying one outside the band, and names the question. Observed by AC3.
- **S5** — a graded ROW is one (question, slice) pair, the slices being `terms` and `naive_terms`.
  `h`, `R` and the ceiling count rows. The leg prints `h` and `R` per slice beside the floor verdict,
  and `--audit-fixture` prints the same per slice plus `(h-1)/(R-1)` over every row. Each question's
  declared `hits` becomes an object keyed by slice name, re-derived from the served measurement,
  because the audit reds on a declared value the measurement disagrees with. Observed by AC4 and AC5.
- **S6** — `.memory-tree.conf` pins `RECALL_FLOOR` to a `served` cell whose value is DERIVED by the
  existing rule, the floor below the one-retirement worst case `(h-1)/(R-1)`, measured at build. The
  comment block above the key is restated with the per-slice `h` and `R`, the worst case and the
  fixture size the derivation rests on. That file is on the kickoff manifest's `watch:` line, so the
  manifest's `last-audit` and `last-body-change` are re-stamped in the same commit with a delta line.
  Observed by AC5 and AC9.
- **S7** — the arm in `tools/memory-recall/test_recall_floor.py` that asserts the literal `h=10
  R=12` becomes a not-below arm against the `h` and `R` the conf comment records. Its docstring says
  what that arm stops seeing: a pin left merely conservative after a fixture edit. Arms that pass a
  single-pair pin keep that pin, so the old grammar stays exercised. Observed by AC7.
- **S8** — `tools/memory-recall/README.md`'s floor section shows the `served` head and says why it
  is the default, and the fixture's `_README` states the two term lists and the provenance of each.
  The docstring of `check-recall.py` states what a `served` run still does not check: untracked files
  the CLI also indexes, the `--budget` byte cut `emit` applies to the fused list, and the CLI's
  default `k` of 20 against the pin's `k`. Observed by AC8.
- **S9** — `memory/map/generated/symbols.json` is regenerated for the new
  definitions. NOT OBSERVED by a criterion here: `python tools/codebase-map/gen_map.py --check` at
  the close is its check, and §7 names the leg that reads it.

## 3. Non-goals (OUT)

- Building aTunedCompass's discriminating fixture, `TOOL-aTunedCompass-9`. It samples passage
  questions over unanchored files to price the chunk half against `bench` ensembles, a second
  mechanism with its own audit, kit claim and runbook line. This unit's headroom comes from the naive
  slice instead, per §8 F1.
- The ensemble pin grammar and byte reporting of `TOOL-aTunedCompass-3`. A `+`-joined head describes
  `bench`'s model of a merged pool, not `run_fusion`'s order, rollup or expression; §8 F2.
- Retiring or rescoping `TOOL-aTunedCompass-2` or `TOOL-aTunedCompass-3`. Their disposition is that
  build's own act; §8 F3.
- Family coverage of the fixture's expected ids, the second half of `TOOL-aProbedToolkit-10`.
- A fixture question for unit 27's live-line property. That unit adds none: its gold arm lives in
  `tools/memory-recall/selftest.py` over its own fixture corpus, so this unit writes both term lists
  for exactly the questions the fixture holds when its pass runs.
- Any change to `query.py`, `bench.py` or `union.py`. The floor reads the served functions and
  edits none of them.

### Edges

- **hands-off** `TOOL-aMendedFleet-29` — `build_served_dir` and `measure_served`, which that unit's
  probe-harvest report grades its questions through at `k` 10.
- **hands-off** external — aTunedCompass's units 2, 3 and 9 stay in that build; whether this unit
  supersedes 2 and 3 is recorded there, and the run's wrap-up names the overlap for the owner.
- **consumes-from** external — aGraftedHelix's unit 4, live on its own branch, adds a supersession
  reorder INSIDE `run_fusion`. Whichever of the two lands second re-measures the pin, because the
  floor grades that order once this unit lands.

## 4. Design

### Evidence

Read at base `7af5f564` on 2026-10-04; nothing under `tools/memory-recall/` or in `.memory-tree.conf`
has moved between that base and this spec.

- `measure_run` in `check-recall.py` calls `bench.load(data, pin["set"])` and
  `bench.rank_with(pin["sub"], docs, db, dfreq, q["query"], pin["k"])`: one set, one substrate, the
  bare question. The shipped pin is `records:fts5:r@5>=0.81`.
- `tools/memory-recall/recall-fixture.json` holds 12 questions and 0 carry a `terms` key, measured
  2026-10-04.
- `query.main` composes `query_expr(question, terms)` and calls `run_fusion(dirp, expr, k)` on both
  its healthy path and its rebuild path. `run_fusion` is `rrf` over `search(dirp, "records", ...)`
  and `run_rollup(search(dirp, "chunks", ...), k)`.
- `query._write_set` writes `meta.id` as `d.get("id") or d.get("rec") or ""`, so a chunk hit with
  no parent record arrives from `search` with an EMPTY `id`, not an absent one. Handed to
  `bench.expected_by_target` as-is, the `"id" in r` branch would compare an empty string and the
  anchor branch would never run; S3's key removal is what keeps `bench`'s chunk semantics.
- Saturation, PINNED from the 2026-10-04 review at `ac65de998`, not re-measured: with strong terms
  the served path scored hit@5 1.000 at n=16, against 0.938 for records alone; with weak terms its
  MRR was 0.422, close to the no-terms 0.397. Node d's dTracedLattice measurement, committed in that
  build's `build/` folder, moved a harvested set from r@5 0.325 to 0.398 by feeding the recorded
  rewrite through `query_expr`. Strong terms saturate; naive ones leave headroom.
- `check-recall.py`, `recall-fixture.json` and `test_recall_floor.py` are claimed `project-owned` in
  `tools/memory-recall/kit.toml`, so none of them ships to an adopter.

### Data model

```json
{"query": "<question>", "terms": ["<8-14 words>"], "naive_terms": ["<8-14 words>"],
 "expected_ids": ["<id>"], "from": "<provenance>", "hits": {"terms": true, "naive_terms": false}}
```

### Inventory

- `build_served_dir(root)` and `measure_served(dirp, queries, pin)` in `check-recall.py`, and the
  `SLICES` tuple naming the two term-list keys. The lexicon's `--suggest` answered `measure_served`
  OK for cell `py.function`; `build_served_dir` leads with `build`, a declared verb. A name the
  lexicon leg refuses at build time is replaced with its `--suggest` answer and this list amended.

### Files touched (estimate)

- `tools/memory-recall/check-recall.py`
- `tools/memory-recall/recall-fixture.json`
- `tools/memory-recall/test_recall_floor.py`
- `tools/memory-recall/README.md`
- `.memory-tree.conf`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/map/features/memory-recall.md`
- `memory/map/generated/symbols.json`

The dossier's floor bullet is refreshed on touch. The memory-recall kit's version bump, owed by the
README edit, is taken once at this build's close, after the last move.

### Alternatives rejected

- **Grade the floor with `union.py`.** It scores (set, substrate) ensembles with byte accounting,
  and it too models a merged pool rather than calling `run_fusion`.
- **Compose terms into the `query` string, as `TOOL-aTunedCompass-2` proposed.** `query_expr` quotes
  each term whole and ORs it, while a composed string is tokenised by `bench.terms`; the two differ,
  and the served path takes the lists separately.
- **Grade the CLI as a subprocess.** It would grade the emitted byte-budgeted text, which has to be
  parsed back into ids, and it writes to the shared cache and query log.

## 5. Production-readiness checklist

- security — N/A — reads tracked files and writes only a scratch dir it removes.
- perf / scale — one `query.build_cache` over the tracked corpus replaces one `extract.py`
  subprocess, measured by the review at 6.5 to 15.5 s; 24 fused queries cost milliseconds.
- error / empty / loading states — an empty served set refuses as precondition 3 does today; a
  question resolving no target is a DEAD PROBE row, never a 0.000 averaged in.
- observability — the leg prints `h` and `R` per slice, so a saturated slice is visible on every run.
- risks — the naive slice's authorship is a claim, not a check: the fixture's `_README` records who
  wrote each list and from what. aGraftedHelix's reorder moves the graded order once both land.
- testing — the arms in `test_recall_floor.py` keep the single-pair grammar exercised; new refusals
  are observed RED on staged breaks per §6.
- migration — the pin moves in one commit with its re-derived value; reverting the commit restores
  the single-pair pin, which the parser still reads.
- user docs — the kit README's floor section and the fixture's `_README`, S8.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-recall/check-recall.py` runs on the tree after this unit, it
  prints the cell `served:r@5`, an `h` and `R` line for each of `terms` and `naive_terms`, and the
  floor verdict, and exits 0.
  Red when: the printed cell is `records:fts5:r@5`, a slice line is missing, or the exit is non-zero.
  cost: one served-cache build, about 15 s.
- **AC2** — When, in a throwaway clone, the body of `run_fusion` in `tools/memory-recall/query.py` is
  replaced with `return []` and `python tools/memory-recall/check-recall.py` runs there, it reds the
  floor with `h` 0 in both slices; restoring the body greens it.
  Red when: the staged break leaves the floor green, which means the floor still ranks through
  `bench` and not the served function.
  fixture: a `git clone --local` under a short `%TEMP%` root; the tree holds none today.
- **AC3** — When `python tools/memory-recall/check-recall.py --fixture <copy>` runs against a staged
  copy of `tools/memory-recall/recall-fixture.json` with one question's `naive_terms` deleted, and
  again with one `terms` list cut to 3 words, it exits 2 with `REFUSED` naming that question each
  time.
  Red when: either copy is graded rather than refused.
- **AC4** — When `python tools/memory-recall/check-recall.py --audit-fixture` runs, the `naive_terms`
  slice reports `h` strictly below `R`.
  Red when: every slice reports `h` equal to `R`, which is the saturated fixture the owner refused to
  pin against.
  figure: `h` and `R` DERIVED at observation time.
- **AC5** — When `python tools/memory-recall/check-recall.py --audit-fixture` runs, it prints
  `(h-1)/(R-1)` over every row and the declared pin in `.memory-tree.conf` is at or below it; with
  the pin raised above that value in a staged copy of the conf, the audit reds naming the pin.
  Red when: the raised pin passes the audit.
- **AC6** — When a throwaway clone's `.memory-tree.conf` pins `records:fts5:r@5>=0.81` and
  `python tools/memory-recall/check-recall.py` runs there, it prints the cell `records:fts5:r@5`
  and grades as it does at base; a pin of `served:x@5>=0.5` refuses naming the metric.
  Red when: the single-pair pin no longer parses, or the bad `served` pin is graded.
- **AC7** — When `grep -n "h=10 R=12" tools/memory-recall/test_recall_floor.py` runs, it prints
  nothing, and `grep -n "not below" tools/memory-recall/test_recall_floor.py` hits the arm that
  replaced the literal.
  Red when: the literal-equality assertion survives.
- **AC8** — When `grep -n "served:" tools/memory-recall/README.md` runs, it hits the floor
  section's pin example, and `grep -c "naive_terms" tools/memory-recall/recall-fixture.json` prints
  one more than the fixture's question count, the extra hit being the `_README`'s provenance line.
  Red when: the README still shows only the single-pair example, or the `_README` is silent on the
  naive slice.
  figure: the question count DERIVED from the fixture at observation time.
- **AC9** — When `bash skills/session-kickoff/manifest-check.sh` runs after the landing commit, it
  exits 0 with `last-audit` naming a commit that contains the `.memory-tree.conf` edit.
  Red when: check 5 reports unaudited watch drift.

## 7. Gates

`recall floor` · `recall floor arms` · `memory-recall kit selftest` · `kit/dogfood doc parity` · `transition-audit arms` · `straggler-guard arms` · `kickoff-manifest ratchet` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `codebase-map coverage + freshness` · `kit version markers`

New arm: tools/memory-recall/test_recall_floor.py · a fixture copy missing `naive_terms`, and a `terms` list below the band, against the refusal S4 adds · none

`recall floor arms` and `memory-recall kit selftest` are held self-test legs; the close runs them.

## 8. Open questions

- **F1 — Where does the fixture's headroom come from?**
  Options: a `naive_terms` slice per question, written without reading the answer; build
  aTunedCompass's unit 9 discriminating fixture first and pin against it; pin the strong-terms
  fixture as it stands; or pin against unit 29's harvested probe set. The third is vetoed by the
  owner's ruling recorded in aTunedCompass's README, since strong terms measured hit@5 1.000. The
  second is a second mechanism and stays that build's unit. The fourth rests on labels no person has
  checked and is ordered after this unit. The first is the review's own proposal, keeps one fixture,
  and makes saturation observable per slice.
  RESOLVED (agent, 2026-10-04, delegated): the `naive_terms` slice, S4 and S5.
- **F2 — How is the served configuration named in the pin?**
  Options: an ensemble head, `records:fts5+chunks:fts5`; or a single `served` head. The ensemble head
  names `bench` parts and the floor would still not grade `rrf`, the rollup or `query_expr`.
  RESOLVED (agent, 2026-10-04, delegated): the `served` head, S1.
- **F3 — Does this unit retire aTunedCompass's units 2 and 3?**
  Options: retire both as superseded in this unit's landing commit; or leave them and name the
  overlap. M2 scopes the amend acts to a build's own units, and unit 3 carries byte reporting this
  unit does not build.
  RESOLVED (agent, 2026-10-04, delegated): leave them, with the hands-off edge in §3.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from `check-recall.py`, `query.py` and the fixture at base.
- rev-2 · 2026-10-04 · §2 S9 · §4 · §7 · M2 cross-read: the definitions this unit adds
  move `memory/map/generated/symbols.json`, which `TOOL-aMendedFleet-82` and the build's other
  code units regenerate and declare; this spec named the leg but omitted the write and its Files touched row.
  §3 also corrects the bullet on unit 27, which said that unit adds a fixture question;
  its S5 puts the gold arm in `tools/memory-recall/selftest.py` and its §3 adds none.

## 10. Reuse audit

The seams extended are `parse_pin`, `read_fixture` and the audit in
`tools/memory-recall/check-recall.py`, and the seams imported unchanged are `query_expr`,
`run_fusion`, `build_cache` and `TERM_BAND` in `tools/memory-recall/query.py` plus
`expected_by_target` in `tools/memory-recall/bench.py`. `python tools/codebase-map/reuse_lookup.py
"grade the recall floor on the fused ranking the query CLI serves with rewrite terms"` returned
`rank_with` and `terms` in `bench.py` as seams and `query_expr` as a candidate; `rank_with` is the
call this unit replaces under a `served` pin, and no candidate grades the fused list, so no existing
grader fits. Recall returned `TOOL-aWeighedCompass-16` and `TOOL-aProbedToolkit-10`, the two asks
filing this defect, `TOOL-aWeighedCompass-18` on saturation, and aTunedCompass's units 2, 3 and 9,
whose specs propose the composed-query and ensemble-head shapes §4 rejects. Where the report and the
tree disagree: the brief calls aTunedCompass's unit 9 BLOCKED and the floor fix; at base unit 9 is
SPECCED and is the discriminating fixture, while units 2 and 3 are the BLOCKED floor work.

Recall terms used: `python tools/memory-recall/query.py "how should the recall floor grade the
served fusion path with terms instead of the records set alone" --terms "recall floor pin served
fusion terms run_fusion check-recall saturation fixture ensemble records chunks headroom"`
