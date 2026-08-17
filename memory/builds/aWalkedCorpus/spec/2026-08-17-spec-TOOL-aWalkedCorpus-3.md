# TOOL-aWalkedCorpus-3 — the recall floor, built against the harness that exists

**Status:** OPEN · rev-1 · 2026-08-17 · node a · Tier-2 · base 3e5c6d43 · streams tooling

## 1. Goal

Ship the merge-bar leg `TOOL-aWalkedCorpus-2` could not: a committed question set, a measured floor
naming one cell of the metric matrix, and the gate program that compares them. The deferral was a
measurement, not a preference, and it named four things a successor needs. This unit builds all
four.

## 2. Scope (IN)

- **S1 — the gate program.** `tools/memory-recall/check-recall.py`, the executable
  `TOOL-aWalkedCorpus-2` needed and never named. It resolves the conf, builds a data dir into a
  `tempfile.mkdtemp()` by running `extract.py`, runs `bench.py --json`, reads the NAMED cell, compares
  it to the declared floor, and exits non-zero below it. `bench.py` is byte-pinned by
  `verbatim.json` and always returns 0; this program is the exit code, and `bench.py` is untouched.
- **S2 — the fixture.** `tools/memory-recall/recall-fixture.json`: twelve questions, each carrying
  the record ids that answer it and a `from` field citing the landed record the question was written
  against.
- **S3 — two pins, both measured, both naming a cell.** `.memory-tree.conf` gains
  `RECALL_FLOOR="records:fts5:r@5>=0.83"` and `RECALL_CEILING_FLOOR="records>=1.00"`. The cell and the
  value are ONE token so they cannot drift apart, and the measuring command sits in the comment above
  them.
- **S4 — the leg.** A `tools/gate-legs.json` entry running S1, guarded on `tools/memory-recall/`,
  `memory/` and `.memory-tree.conf` — the three things that can move the number.
- **S5 — the arms.** `tools/memory-recall/selftest.py` gains, at minimum: the floor FALLS and the
  program exits non-zero when the corpus is degraded; an absent fixture reds by NAME rather than
  skipping; a malformed pin reds rather than defaulting; and the two failure directions print
  distinguishable messages.
- **S6 — the dossier.** `memory/map/features/memory-recall.md`, claiming S4's leg key. The coverage
  gate reds until a dossier claims a new leg, and `memory/map/baseline.toml` forbids new keys in
  itself, so the dossier is not optional. It also claims the two memory-recall keys sitting unclaimed
  in the baseline today, which shrinks it by two.

## 3. Non-goals (OUT)

- **Grading `chunks`.** `TOOL-aWalkedCorpus-2` §3 put `records` and `chunks` in scope. Measured over
  this fixture at the served chunk size, `chunks:fts5:r@5` is **0.08** against `records:fts5:r@5`
  0.83, and the gap is the fixture's SHAPE rather than a retrieval defect: an id is a record-level
  target, and `expected_by_target` credits a chunk only when the chunk's own text carries the id.
  Pinning 0.08 would be a decoration. Grading chunks needs a path-keyed or passage-keyed fixture,
  which is its own unit.
- **Tuning retrieval.** Unchanged from the deferred unit's §3, and for the same reason: a floor that
  lands with the change that moves it cannot tell you which did what.
- **A fixture that covers the corpus.** Twelve questions is a floor's worth, not coverage. §4 states
  what that does and does not buy.
- **Extending `bench.py` or `union.py`.** Both are byte-pinned in `verbatim.json` and asserted by
  `selftest.py`. S1 wraps them; nothing edits them.
- **A `Conf` field for the floor.** `recall_conf.load_conf()` is public and returns the raw mapping,
  so S1 reads the pins through it. Adding a slot to `Conf` would touch `digest()`, the
  `KEY=VALUE` protocol `adopt-memory-recall.sh` parses, and the rendered Skill — three carriers for a
  value only the gate reads.

## 4. Design

### The cell, and why it is that cell

`bench.py` emits `r@k`, `f@k`, `MRR` and `b@k` per substrate per set across whatever `--ks` it is
given, plus a `ceiling` per set. One run over this fixture spans 0.00 to 1.00. A scalar floor over
that matrix names nothing, which is the third finding the deferral records. The pin therefore names
`set:substrate:metric@k` as one token.

The substrate is `fts5`, verified against source rather than chosen: `query.py:655` ranks with
`bm25(d, 1.0, 1.0, B.ALIAS_WEIGHT)`, and `bench.py`'s `fts5` is `run_fts(..., weighted=False)`, which
is the same expression. `fts5w` scores better here (r@10 0.92 against 0.83) and grading it would
flatter a substrate no session is served.

`r@5` because a session reads a handful of hits, and because at twelve questions the metric moves in
steps of 0.083 — one question flipping out of the top five reds the leg.

### Two pins, because there are two failure directions

| pin | falls when | the operator's next move |
|---|---|---|
| `RECALL_FLOOR` | retrieval got worse | investigate the change that moved it |
| `RECALL_CEILING_FLOOR` | an expected id no longer resolves anywhere in the set | retarget the fixture |

`bench.py`'s `score()` returns 0.0 for a query whose targets do not resolve, so `r@k <= ceiling` by
construction — a legitimately removed record drags the retrieval number down with it. That is the
fifth finding the deferral records, and one scalar cannot express both halves. Splitting them makes
each red name its own remedy. `RECALL_FLOOR` is compared against the ceiling-NORMALISED score
(`r@k / ceiling`) so a ceiling movement reds exactly one pin; `RECALL_CEILING_FLOOR` is what stops
the normalisation from turning a shrinking corpus into a rising quotient.

### The red proof, measured before this spec was written

The deferred unit's arm removed a declared corpus source and moved the chosen metric by nothing —
`records` was byte-identical at every k, and chunk MRR moved the wrong way. The replacement drops
`memory/DECISIONS.md` from the extracted sets and re-benches the same fixture:

| | `records` docs | ceiling | `fts5:r@5` | normalised |
|---|---|---|---|---|
| baseline | 256 | 1.00 | 0.83 | 0.83 |
| degraded | 225 | 0.83 | 0.17 | 0.20 |

Both pins move, in the directions the table above assigns them. This is a PLUMBING arm — it proves
the score responds to the corpus, not that retrieval is good — and S5 says so where it is written.

### The fixture's provenance rule

`TOOL-aWalkedCorpus-2` §4 required every question to come from a landed spec's §10 recall probe. That
pool was re-measured here and is 8 specs, 3 naming ids, 2 of those 3 citing the id as a recorded
MISS — one usable spec. The rule widens to: **a question whose answer was determined by a person
writing a record that states it**, which admits `memory/DECISIONS.md` rows, backlog rows and closing
review rows. Every question carries `from` naming that record.

The tautology this rule has to avoid is a question written by reading what the index returns.
Measured against it: eleven of the twelve questions share under half their content terms with the
record they target, and the two that rank worst (16th and 13th) are in the fixture precisely because
they fail today. The fixture is not a description of the current ranking.

### What this does not prove

A floor over twelve questions measures that these questions still find these records. A change that
improves them while degrading a hundred others passes. §3 scopes coverage out rather than letting the
number stand for quality.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/memory-recall/check-recall.py` | new — S1 |
| `tools/memory-recall/recall-fixture.json` | new — S2 |
| `.memory-tree.conf` | S3, both pins plus the measuring command |
| `tools/gate-legs.json` | S4 |
| `tools/memory-recall/selftest.py` | S5 |
| `memory/map/features/memory-recall.md` | new — S6 |
| `memory/map/baseline.toml` | the two claimed keys deleted |
| `tools/memory-recall/README.md` | the fixture, the pins and how to re-measure |
| `AGENTS.md` | the gate-suite citation, or the charter signal reds |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamp: two watched pathspecs move |
| `memory/builds/aWalkedCorpus/README.md` | the roster gains this unit |
| `memory/backlog/TOOL.md` · `memory/DECISIONS.md` | the row and the decisions this unit takes |

`tools/memory-recall/recall_conf.py` is NOT in the table. Its `KIT_MEMORY_RECALL_VERSION` feeds
`Conf.digest()`, which every warm cache keys on; this unit changes no extraction or schema behaviour,
so bumping it would evict every cache on the fleet for a file none of them reads.

### Alternatives rejected

- **Grade through `union.py`.** Its `records:fts5+chunks:fts5` ensemble is closer to what `query.py`
  actually serves, and it measured 0.833 here. Rejected because it reports no `ceiling` and one `k`,
  so the two-pin split above is not expressible against it.
- **One scalar floor.** The deferral's third finding, and rejected on it.
- **Re-derive the floor from the run being graded.** `aQuarriedLantern-1:568` refused the upstream
  port on exactly this ground — "a gate that recomputes its threshold from the run it is grading can
  never fail". The floor is declared in a file a person edits.

## 5. Production-readiness checklist

- security — N/A. The program reads tracked files and writes only inside `mkdtemp()`.
- perf / scale — MEASURED on this tree: extract 0.43 s, bench over 12 questions 0.61 s. The leg is
  guarded, but `memory/` is one of its guards, so it runs on most commits; ~1 s is the price.
- a11y / i18n — N/A.
- error / empty / loading states — an absent fixture, an absent pin and a malformed pin each red by
  NAME. A grading leg that skips when its question set is missing is the vacuity class this unit
  exists to close.
- observability — the leg prints the cell, the raw score, the ceiling and the normalised value, so a
  red says which half moved before anyone opens a file.
- risks — the fixture going stale as records are legitimately removed. `RECALL_CEILING_FLOOR` is the
  signal that separates that from a regression, and its red names the unresolved id.
- testing + left-shift gates — S5, and the degradation arm is the unit's centre.
- migration / rollback — revert; the program, the fixture, the pins and the leg land together.
- user docs — `tools/memory-recall/README.md` gains the fixture, the pins and the re-measure command.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-recall/check-recall.py` runs on a clean tree it exits 0 and
  prints the cell `records:fts5:r@5`, the raw score, the ceiling and the normalised score.
- **AC2** — **The floor can FALL.** With `memory/DECISIONS.md` dropped from the extracted sets,
  `check-recall.py` exits non-zero and its message names `RECALL_FLOOR`. Observed in
  `tools/memory-recall/selftest.py`, not argued.
- **AC3** — With `tools/memory-recall/recall-fixture.json` absent, `check-recall.py` exits non-zero
  and its output names that path. It does not skip and does not exit 0.
- **AC4** — With `RECALL_FLOOR` absent from `.memory-tree.conf`, or present and unparseable,
  `check-recall.py` exits non-zero naming the key rather than assuming a default.
- **AC5** — When `bash tools/run-gates.sh` runs, the new leg appears by name and is green.
- **AC6** — When `python tools/memory-recall/selftest.py` runs it exits 0, and inverting the S5
  degradation arm reds it naming that arm.
- **AC7** — When `python tools/codebase-map/test_codebase_map.py` runs, coverage and freshness are
  green with the new leg key claimed in `memory/map/features/memory-recall.md`, and
  `memory/map/baseline.toml` is two keys shorter.
- **AC8** — When `python tools/drift-audit/drift_report.py --check` runs,
  `handkept_inventories_disagreeing_with_source` still reports 0 at pin 0.
- **AC9** — When `tools/memory-recall/recall-fixture.json` is read, every question carries a `from`
  field naming the landed record its answer was taken from, and every `expected_ids` entry resolves
  in the `records` set — the `ceiling` of 1.00 is that assertion in measured form.
- **AC10** — When `python tools/memory-recall/bench.py` and `tools/memory-recall/union.py` are
  compared against `tools/memory-recall/verbatim.json`, both digests are unchanged.

## 7. Gates

- `python tools/memory-recall/selftest.py` — S5's arms, and the verbatim pins.
- `python tools/memory-recall/check-recall.py` — the new leg itself.
- `bash tools/run-gates.test.sh` — the canary over the changed manifest.
- `python tools/codebase-map/test_codebase_map.py` — the new leg key and the new dossier.
- `python tools/drift-audit/drift_report.py --check` — the zero-tolerance charter signal.
- `bash skills/session-kickoff/manifest-check.sh` — watched pathspecs move.
- `bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

none.

## 9. Revision log

- rev-1 · 2026-08-17 · initial draft, authored under the `aWalkedCorpus` standing mandate. It is the
  successor `TOOL-aWalkedCorpus-2` deferred to, and its four §1 requirements are S1/S2, S3, the red
  proof in §4, and the widened provenance rule in §4. Every number in §4 was measured against this
  tree before the section was written, because the deferral exists precisely because the previous
  spec's were not.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "compare a measured retrieval score against a declared
floor and fail the merge bar"` — ranked `score` in `tools/memory-recall/bench.py` and
`check-template-size.sh` (the repo's other declared-pin gate). The seam this unit extends is
`bench.py`'s `--json` report, which already carries every value both pins need; the shape it copies
is `check-template-size.sh`'s, a declared number in a file a person edits with its justification
beside it.

`python tools/memory-recall/query.py "what makes a gate that measures a number honest rather than a
decoration" --terms "vacuous pin floor shrink-only arm red-proof fixture decoration ceiling measured
provenance tautology degradation cell"` — surfaced `TOOL-aUnmannedHelm-6` (assert against something
declared INDEPENDENTLY), `TOOL-cSteadyMetronome-1` (a gate asserts what the SUBJECT does) and
`cSightedPlumb-1:85` (a permanently-red probe is a decoration, not a signal). The two-pin split in §4
is the first of those applied: the floor is declared in the conf, never recomputed from the run.

**Read rather than assumed, and where they disagreed:** `TOOL-aWalkedCorpus-2` §3 states that
`check_recall.py` "already treats" `records` and `chunks` as the graded pair. That file does not
exist in this repo — `extract.py:128` and `query.py:302` are FORKED comments describing upstream, and
`aQuarriedLantern-1:85` lists the upstream gate among the things that port did not take. The pair is
therefore a claim about a file nobody here can run, and §3 above replaces it with a measurement.
