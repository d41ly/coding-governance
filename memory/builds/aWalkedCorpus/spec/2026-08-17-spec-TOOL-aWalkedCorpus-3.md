# TOOL-aWalkedCorpus-3 — the recall floor, built against the harness that exists

**Status:** OPEN · rev-2 · 2026-08-17 · node a · Tier-2 · base 3e5c6d43 · streams tooling · ratified 2026-08-17

## 1. Goal

Ship the merge-bar leg `TOOL-aWalkedCorpus-2` could not: a committed question set, a measured floor
naming one cell of the metric matrix, and the gate program that compares them. The deferral was a
measurement, not a preference, and it named four things a successor needs. This unit builds all
four.

## 2. Scope (IN)

- **S1 — the gate program.** `tools/memory-recall/check-recall.py`, the executable
  `TOOL-aWalkedCorpus-2` needed and never named. Its surface, error contract and evaluation order are
  §4's `### Data model`; they are part of this scope item, because round-2 F6 found that a program
  described only as a flow leaves three reachable states unspecified.
- **S2 — the fixture.** `tools/memory-recall/recall-fixture.json`: twelve questions, each carrying the
  record ids that answer it and a `from` field citing the record its answer was taken from. **It is
  committed with this spec** rather than promised by it — round-2 F1 established that a number
  measured against an artifact no reader can reach is exactly the defect that deferred the
  predecessor.
- **S3 — one pin, derived rather than observed.** `.memory-tree.conf` gains
  `RECALL_FLOOR="records:fts5:r@5>=0.81"`. The cell and the value are ONE token so they cannot drift
  apart. The value is **not** today's score: it is the one-retirement worst case computed in §4, and
  §4 shows the derivation. The pin is shrink-only in the sense that matters — the score may rise and
  the floor may follow, but a fall reds, and lowering the floor to accommodate a fall is the move this
  unit exists to make visible.
- **S4 — the per-id resolution assertion.** `check-recall.py` resolves every `expected_ids` entry
  against the graded set itself and exits non-zero naming any id with an empty hit set. This is a
  separate predicate from the floor, not a second pin: round-2 F3 measured that `ceiling` counts
  QUERIES and cannot express per-id resolution, so a question carrying one real and one fictional id
  scores `ceiling 1.00`.
- **S5 — the leg.** A `tools/gate-legs.json` entry running S1, guarded on `tools/memory-recall/`,
  `memory/` and `.memory-tree.conf` — the three things that can move the number.
- **S6 — the arms.** `tools/memory-recall/selftest.py` gains one arm per row of §4's degradation
  table, including the two that must fire SINGLY, plus the empty fixture, the all-miss fixture, the
  absent cell, the absent fixture and the absent or malformed pin.
- **S7 — the dossier.** `memory/map/features/memory-recall.md`, claiming S5's leg key and **every**
  `memory-recall` key currently in `memory/map/baseline.toml` — measured at four, not two (round-2
  F4). The coverage gate reds until a dossier claims a new leg and `baseline.toml`'s own header
  forbids new keys in itself, so the dossier is not optional.
- **S8 — the fixture stays out of adopters' trees.** `tools/memory-recall/kit.toml` gains a
  `[[files]]` exclude for `recall-fixture.json` and `check-recall.py`. Its `include = "**"` otherwise
  ships a question set keyed on gov record ids, plus a program reading pins an adopter's conf does not
  carry, into every adopting tree with no `[[gate_leg]]` to run it (round-2 F5). §8 records what was
  parked instead.

## 3. Non-goals (OUT)

- **Grading `chunks`.** Measured over the committed fixture at the served chunk size,
  `chunks:fts5:r@5` is **0.1667** against `records:fts5:r@5` 0.8333. The gap is the fixture's SHAPE,
  not a retrieval defect: an id is a record-level target, and `expected_by_target` credits a chunk only
  when the chunk's own text carries the id. Grading chunks needs a path- or passage-keyed fixture,
  which is its own unit.
- **Tuning retrieval.** A floor that lands with the change that moves it cannot tell you which did
  what.
- **A fixture that covers the corpus.** Twelve questions is a floor's worth, not coverage.
- **Extending `bench.py` or `union.py`.** Both are byte-pinned in `verbatim.json` and asserted by
  `selftest.py`. S1 wraps them; nothing edits them.
- **A `Conf` field for the floor.** `recall_conf.load_conf()` is public and returns the raw mapping,
  so S1 reads the pin through it. A `Conf` slot would touch `digest()`, the `KEY=VALUE` protocol
  `adopt-memory-recall.sh` parses, and the rendered Skill — three carriers for a value only the gate
  reads.
- **A graded floor for adopters.** S8 excludes the fixture and the program from the kit payload. An
  adopter's floor would have to be measured against their corpus, from a fixture they author; shipping
  gov's is `memory/gotchas/pin-copied-from-another-corpus.md`. The alternative is parked in §8.

## 4. Design

### The cell, and why it is that cell

`bench.py` emits `r@k`, `f@k`, `MRR` and `b@k` per substrate per set, plus a `ceiling` per set. One
run over this fixture spans 0.17 to 0.83. A scalar floor over that matrix names nothing, which is the
third finding the deferral records. The pin therefore names `set:substrate:metric@k` as one token, and
S1 DERIVES its `--sets`, `--subs` and `--ks` from that token, so re-aiming the pin re-aims the run.

The substrate is `fts5`, and the justification is the SOURCE, not a score. `query.py:655` ranks with
`bm25(d, 1.0, 1.0, B.ALIAS_WEIGHT)`; `bench.py`'s `fts5` is `run_fts(..., weighted=False)`, the same
expression. Over the committed fixture `fts5w` measures r@10 **0.8333 — equal to `fts5`, not better**,
so there is no comparative argument here in either direction and rev-1's claim of one was a fixture
artifact (round-2 F1). Grading `fts5` is right because it is what a session is served.

`r@5` because a session reads a handful of hits, and because at twelve questions the metric moves in
steps of 0.083.

### Data model — the program's surface, error contract and order

```
python tools/memory-recall/check-recall.py [--data-dir DIR] [--repo ROOT] [--audit-fixture]
```

`--data-dir` grades an already-extracted set instead of extracting, which is the seam every arm in S6
needs and which rev-1 left the builder to invent. With no `--data-dir` the program extracts the repo's
own corpus into a `tempfile.mkdtemp()` at `query.CHUNK_MAX`, imported rather than restated so the
graded corpus is the served one.

Evaluation order is fixed, and it is fixed because the message a red prints must be determinate:

1. **The fixture** — absent or unparseable reds naming the path. It does not skip.
2. **The pin** — `RECALL_FLOOR` absent, empty, or not matching `<set>:<sub>:<metric>@<k>>=<float>`
   reds naming the key. There is no default.
3. **Per-id resolution (S4)** — every `expected_ids` entry resolves in the graded set, or red naming
   the id. This runs BEFORE the floor so a retired record is reported as a retired record.
4. **The cell** — `sets.<set>.substrates.<sub>[<metric>@<k>]` present in the report, or red naming the
   cell as unmeasured. An empty fixture makes `substrates` `{}` and this is the branch that catches
   it, rather than a `KeyError`.
5. **The floor** — `ceiling` of 0 reds at step 3 and never reaches the division, so the normalisation
   has no 0/0 branch. Otherwise compare `r@k / ceiling` against the pin.

`--audit-fixture` prints each question's content-term overlap with its target's own text and reds
above `OVERLAP_MAX`. It exists because the anti-tautology property below is otherwise a sentence.

### The pin is DERIVED from the worst case, not read off today's score

`r@k` is `h/Q` and `ceiling` is `R/Q` over one query list, so the normalised score is exactly `h/R` —
`h` questions that hit, `R` whose targets resolve at all. Retiring a record that a HITTING question
targets removes it from numerator and denominator both, so the normalised score FALLS. Rev-1 claimed
normalisation made a ceiling movement red exactly one pin; that is arithmetically false, and round-2
F2 measured it.

The fix is to price one retirement into the pin instead of pretending it costs nothing. Measured on
the committed fixture: `h=10`, `R=12`. The one-retirement worst case is `(h-1)/(R-1) = 9/11 = 0.8182`,
so the pin is **0.81**, and the property it buys is stated rather than assumed: *the floor carries
exactly one legitimate retirement's headroom by construction.* A second retirement (`8/10 = 0.80`) or
any genuine regression (`9/12 = 0.75`) reds, which is correct — the first demands fixture
maintenance, the second demands investigation, and step 3 above tells them apart before the floor is
ever evaluated.

### The degradation table — every row measured, two of them isolating

`RECALL_CEILING_FLOOR` is gone. Round-2 F3 showed the aggregate it pinned cannot see what §5 charged
it with naming, and S4's per-id assertion can. What is left is one pin and one predicate, and the two
single-direction levers below are what prove they are independent.

| lever | ceiling | `r@5` | normalised | floor | per-id |
|---|---|---|---|---|---|
| baseline | 1.0000 | 0.8333 | 0.8333 | green | green |
| drop only the `memory/DECISIONS.md` home of `TOOL-aWrittenMethod-4` | 1.0000 | 0.7500 | 0.7500 | **RED** | green |
| retire `TOOL-aMouldedFolio-1` entirely | 0.9167 | 0.8333 | 0.9091 | green | **RED**, names the id |
| retire `TOOL-aStandingWrit-2` (a hitting target) | 0.9167 | 0.7500 | 0.8182 | green | **RED**, names the id |
| drop `memory/DECISIONS.md` wholesale | 0.8333 | 0.1667 | 0.2000 | **RED** | **RED** |

Row 2 is the floor-only red: three records carry `TOOL-aWrittenMethod-4`, so removing its
`DECISIONS.md` home leaves the id resolvable and drops the question out of the top five. Row 3 is the
per-id-only red. Row 4 is the one-retirement case the pin is derived from, and it is GREEN by
construction. Row 5 is a plumbing arm — it proves the score responds to the corpus, not that
retrieval is good — and S6 labels it as one.

### Reproducing every number above

```
python tools/memory-recall/extract.py . <tmpdir> --chunk-max 600
python tools/memory-recall/bench.py <tmpdir> tools/memory-recall/recall-fixture.json \
       --sets records,chunks --subs fts5,fts5w --ks 1,5,10
```

Measured at `records 257 docs`. The corpus MOVES — it was 256 before this build's own round-2 review
record landed under `memory/` — so a re-measurement that differs by a document is the corpus, not a
regression. This is why the pin is derived from `h` and `R` rather than copied from a run.

### Inventory — the fixture, and the h and R the pin rests on

`homes` is the number of records carrying the id; `hits` is whether the question is answered at
`records:fts5:r@5` today. Ten hit, twelve resolve.

| # | expected id | homes | hits | provenance |
|---|---|---|---|---|
| 1 | `TOOL-aUnmannedHelm-5` | 3 | yes | `aWrittenMethod-2` §10 probe |
| 2 | `TOOL-aUnmannedHelm-6` | 3 | yes | `aWrittenMethod-2` §10 probe |
| 3 | `TOOL-aStandingWrit-2` | 2 | yes | `DECISIONS.md` row |
| 4 | `TOOL-aStandingWrit-4` | 2 | yes | `DECISIONS.md` row |
| 5 | `TOOL-cSteadyMetronome-1` | 1 | yes | `DECISIONS.md` row |
| 6 | `TOOL-aWidenedGuide-1` | 2 | yes | `DECISIONS.md` row |
| 7 | `TOOL-aWrittenMethod-4` | 3 | yes | `DECISIONS.md` row |
| 8 | `TOOL-aWrittenMethod-6` | 3 | yes | `DECISIONS.md` row |
| 9 | `TOOL-aUnmannedHelm-10` | 2 | **no** | `DECISIONS.md` row |
| 10 | `TOOL-aMouldedFolio-1` | 1 | **no** | `DECISIONS.md` row |
| 11 | `TOOL-aUnmannedHelm-9` | 2 | yes | `DECISIONS.md` row |
| 12 | `TOOL-cFinalBerth-1` | 2 | yes | `DECISIONS.md` row |

### The fixture's provenance rule, and the tautology it has to avoid

`TOOL-aWalkedCorpus-2` §4 required every question to come from a landed spec's §10 recall probe. That
pool was re-measured here: 8 specs carry such a probe, 3 name ids, and 2 of those 3 cite the id as a
recorded MISS — one usable spec. The rule widens to **a question whose answer was determined by a
person writing a record that states it**, which admits `DECISIONS.md` rows, backlog rows and closing
review rows. Every question carries `from` naming that record.

The tautology to avoid is a question written by reading what the index returns. Round-2 F1 built one
— twelve questions whose text IS the target record's text — and it scored `r@5 1.00` while proving
nothing, satisfying rev-1's AC9 outright. Prose cannot exclude that, so `--audit-fixture` measures it
and AC9 observes the measurement. Two of the twelve questions are in the set precisely because they
FAIL today, which a fixture written from a result list would never contain.

### What this does not prove

A floor over twelve questions measures that these questions still find these records. A change that
improves them while degrading a hundred others passes. §3 scopes coverage out rather than letting the
number stand for quality.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/memory-recall/check-recall.py` | new — S1, S4 |
| `tools/memory-recall/recall-fixture.json` | new — S2, committed with this spec |
| `.memory-tree.conf` | S3, the pin plus its derivation and the measuring argv |
| `tools/gate-legs.json` | S5 |
| `tools/memory-recall/selftest.py` | S6 |
| `tools/memory-recall/kit.toml` | S8, the `[[files]]` exclude |
| `memory/map/features/memory-recall.md` | new — S7 |
| `memory/map/baseline.toml` | all four `memory-recall` keys deleted |
| `memory/map/generated/inventories.json` | GENERATED — `python tools/codebase-map/gen_map.py --write` |
| `memory/map/generated/MAP.md` | GENERATED — same command |
| `memory/map/generated/symbols.json` | GENERATED — same command; `_live_py` walks the filesystem, so S1 and S6 both stale it |
| `tools/memory-recall/README.md` | the fixture, the pin and how to re-measure |
| `AGENTS.md` | the gate-suite citation, or the charter signal reds |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamp: watched pathspecs move |
| `memory/builds/aWalkedCorpus/README.md` | the roster |
| `memory/backlog/TOOL.md` · `memory/DECISIONS.md` | the row and the decisions this unit takes |

`tools/memory-recall/recall_conf.py` is NOT in the table. Its `KIT_MEMORY_RECALL_VERSION` feeds
`Conf.digest()`, which every warm cache keys on; this unit changes no extraction or schema behaviour,
so bumping it would evict every cache on the fleet for a file none of them reads.

**Naming convention, called out because the leg has zero headroom.** `.lexicon.conf` pins
`VERB_OFFENDER_PIN` at exactly today's count and `lexicon.py` compares one-sided, so ONE new
definition whose name does not lead with a declared verb reds `python tools/lexicon/lexicon.py` —
which is guarded on `tools/` and therefore runs on every commit in this unit. S6's arms follow
`selftest.py`'s dominant `t_` convention; `t` is not a declared verb. Either add `t` to the conf's
verb table in the same commit or name the arms with a declared verb. Round-2 verified this by adding
one probe file and watching the leg go red.

### Alternatives rejected

- **Keep `RECALL_CEILING_FLOOR` as a second pin.** It cannot see per-id resolution (F3) and it
  duplicates what S4 asserts better. Dropped; `ceiling` is still REPORTED so a reader sees which half
  moved.
- **Pin the raw `r@k` rather than the normalised score.** Then every retirement reds the floor and the
  remedy is always ambiguous. The normalisation plus the derived headroom is what makes one
  retirement free and the second one loud.
- **Grade through `union.py`.** Its `records:fts5+chunks:fts5` ensemble is closer to what `query.py`
  serves, but it reports no `ceiling` and one `k`, so neither S4 nor the derivation above is
  expressible against it.
- **Re-derive the floor from the run being graded.** `aQuarriedLantern-1:568` refused the upstream
  port on exactly this ground — "a gate that recomputes its threshold from the run it is grading can
  never fail".

## 5. Production-readiness checklist

- security — N/A. The program reads tracked files and writes only inside `mkdtemp()`.
- perf / scale — MEASURED: extract 0.43 s; bench 0.07 s at the narrow argv the pin derives, 0.50 s at
  `records,chunks`. The leg is guarded, but `memory/` is one of its guards, so it runs on most
  commits.
- a11y / i18n — N/A.
- error / empty / loading states — the five ordered branches in §4's `### Data model`, each redding by
  NAME: absent fixture, absent or malformed pin, unresolved expected id, absent cell (the empty-fixture
  case), and the floor itself. A grading leg that skips when its question set is missing is the
  vacuity class this unit exists to close.
- observability — the leg prints the cell, the raw score, the ceiling and the normalised value, so a
  red says which half moved before anyone opens a file.
- risks — **the fixture going stale as records are legitimately removed.** S4's per-id assertion names
  the unresolved id, and the pin's derived headroom absorbs the first retirement so the red arrives as
  fixture maintenance rather than as a false regression. Second risk: `pin-copied-from-another-corpus`,
  addressed by S8 and recorded in §8.
- testing + left-shift gates — S6, and the two single-direction arms are the unit's centre.
- migration / rollback — revert; the program, the fixture, the pin and the leg land together.
- user docs — `tools/memory-recall/README.md` gains the fixture, the pin and the re-measure command.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-recall/check-recall.py` runs on a clean tree it exits 0 and
  prints the cell `records:fts5:r@5`, the raw score, the ceiling and the normalised score.
- **AC2a** — **The floor reds ALONE.** With only the `memory/DECISIONS.md` record for
  `TOOL-aWrittenMethod-4` removed from an extracted dir, `check-recall.py --data-dir` exits non-zero,
  its message names `RECALL_FLOOR`, and the per-id assertion stays green. Measured 0.7500 against the
  0.81 pin.
- **AC2b** — **The per-id assertion reds ALONE.** With every record for `TOOL-aMouldedFolio-1` removed,
  `check-recall.py --data-dir` exits non-zero naming that id, and the floor stays green. Measured
  normalised 0.9091.
- **AC2c** — **One retirement is free by construction.** With every record for `TOOL-aStandingWrit-2`
  removed, the normalised score is 0.8182 and does NOT breach `RECALL_FLOOR`; only the per-id
  assertion reds.
- **AC3** — With `tools/memory-recall/recall-fixture.json` absent, `check-recall.py` exits non-zero
  and names that path. It does not skip and does not exit 0.
- **AC4** — With `RECALL_FLOOR` absent, empty, or not matching the pin grammar, `check-recall.py`
  exits non-zero naming the key rather than assuming a default.
- **AC5** — With a fixture whose `queries` is empty, `check-recall.py` reds naming the cell as
  unmeasured rather than raising; with an all-miss fixture it reds at the per-id assertion and never
  divides by a zero `ceiling`.
- **AC6** — When `bash tools/run-gates.sh` runs, the new leg appears by name and is green.
- **AC7** — When `python tools/memory-recall/selftest.py` runs it exits 0, and inverting any one arm
  in §4's degradation table reds it naming that arm.
- **AC8** — When `python tools/codebase-map/test_codebase_map.py` runs after
  `python tools/codebase-map/gen_map.py --write`, coverage and freshness are green, and every
  `memory-recall` key is claimed by `memory/map/features/memory-recall.md` and absent from
  `memory/map/baseline.toml`.
- **AC9** — When `python tools/memory-recall/check-recall.py --audit-fixture` runs, every question
  carries a `from` field and its content-term overlap with its target is at or below `OVERLAP_MAX`;
  a fixture whose questions are copied from their targets' text reds.
- **AC10** — When `python tools/drift-audit/drift_report.py --check` runs,
  `handkept_inventories_disagreeing_with_source` still reports 0 at pin 0.
- **AC11** — When `python tools/memory-recall/bench.py` and `tools/memory-recall/union.py` are
  compared against `tools/memory-recall/verbatim.json`, both digests are unchanged.
- **AC12** — When `python tools/govkit/govkit.py selfcheck` runs it is green, and
  `tools/memory-recall/kit.toml` excludes `recall-fixture.json` and `check-recall.py` from the kit
  payload.

## 7. Gates

- `python tools/memory-recall/selftest.py` — S6's arms, and the verbatim pins.
- `python tools/memory-recall/check-recall.py` — the new leg itself.
- `bash tools/run-gates.test.sh` — the canary over the changed manifest.
- `python tools/codebase-map/test_codebase_map.py` — the new leg key and the new dossier.
- `python tools/lexicon/lexicon.py` — zero headroom on the verb pin; see §4.
- `python tools/govkit/govkit.py selfcheck` — the kit payload changes.
- `python tools/drift-audit/drift_report.py --check` — the zero-tolerance charter signal.
- `bash skills/session-kickoff/manifest-check.sh` — watched pathspecs move.
- `bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

- **Should an adopter get a graded recall floor at all?** RESOLVED (agent, 2026-08-17, delegated) for
  THIS unit only, by the narrow option: S8 excludes `recall-fixture.json` and `check-recall.py` from
  the kit payload, so no adopter receives gov's question set or a program reading pins their conf does
  not carry. **The wider option is PARKED, not taken.** Options seen: (a) exclude, which is S8;
  (b) declare a third `[[gate_leg]]` in `kit.toml` and build an adoption-time path by which an adopter
  seeds their own fixture and MEASURES their own floor. Refused because (b) differs from (a) in what
  gets BUILT — it needs a seeding mechanism, an adopter-facing measuring verb and a story for a repo
  whose corpus is too small to score — and a standing mandate delegates fork resolution, never scope.
  The parked half is a successor unit's subject, and round-1 F11 asked for this decision without
  getting one.

## 9. Revision log

- rev-2 · 2026-08-17 · **folded the round-2 spec audit, which returned BLOCKED on two.** F1: every
  retrieval number rested on a fixture in no tracked file, and two of those numbers carried design
  arguments that REVERSED on an independently authored set — `chunks:fts5:r@5` is 0.1667 not 0.08,
  and `fts5w` r@10 equals `fts5` rather than beating it, so §4's substrate argument now rests on
  source alone. The fixture is committed with this spec and §4 gains its inventory, the reproduction
  argv and `--audit-fixture` as AC9's mechanical observer. F2: `r@k / ceiling` reduces to `h/R`, so
  retiring a record a HITTING question targets moves both signals and rev-1's "reds exactly one pin"
  was false; the pin is now DERIVED as the one-retirement worst case `(h-1)/(R-1) = 0.8182 -> 0.81`,
  and §4's table carries two measured single-direction levers that rev-1 had no way to produce. F3:
  `ceiling` counts queries, not ids, so `RECALL_CEILING_FLOOR` is replaced by S4's per-id assertion.
  F4: three generated codebase-map artifacts were missing from Files touched, and the baseline holds
  four `memory-recall` keys, not two. F5: `kit.toml`'s `include = "**"` shipped the fixture to every
  adopter — S8 excludes it and §8 records what was parked. F6: S1 had no interface, so §4 gains a
  `### Data model` with the surface, the five-step evaluation order and the degenerate cases. Also
  restored the predecessor's pin-direction sentence to S3, and recorded the lexicon verb-pin headroom
  in §4 because the leg runs on every commit here.
- rev-1 · 2026-08-17 · initial draft, authored under the `aWalkedCorpus` standing mandate. It is the
  successor `TOOL-aWalkedCorpus-2` deferred to, and its four §1 requirements are S1/S2, S3, the red
  proof in §4, and the widened provenance rule in §4.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "compare a measured retrieval score against a declared
floor and fail the merge bar"` — ranked `score` in `tools/memory-recall/bench.py` and
`check-template-size.sh` (the repo's other declared-pin gate). The seam this unit extends is
`bench.py`'s `--json` report, which already carries every value the pin and the per-id assertion need;
the shape it copies is `check-template-size.sh`'s, a declared number in a file a person edits with its
justification beside it.

`python tools/memory-recall/query.py "what makes a gate that measures a number honest rather than a
decoration" --terms "vacuous pin floor shrink-only arm red-proof fixture decoration ceiling measured
provenance tautology degradation cell"` — surfaced `TOOL-aUnmannedHelm-6` (assert against something
declared INDEPENDENTLY), `TOOL-cSteadyMetronome-1` (a gate asserts what the SUBJECT does) and
`cSightedPlumb-1:85` (a permanently-red probe is a decoration, not a signal). The first of those is
why the pin is declared in the conf and derived from `h` and `R` rather than recomputed from the run.

**Read rather than assumed, and where they disagreed:** `TOOL-aWalkedCorpus-2` §3 states that
`check_recall.py` "already treats" `records` and `chunks` as the graded pair. That file does not exist
in this repo — `extract.py:128` and `query.py:302` are FORKED comments describing upstream, and
`aQuarriedLantern-1:85` lists the upstream gate among the things that port did not take. The pair is
therefore a claim about a file nobody here can run, and §3 replaces it with a measurement.
