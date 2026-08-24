# TOOL-aWalkedCorpus-3 — the recall floor, built against the harness that exists

**Status:** CLOSED · rev-5 · 2026-08-17 · node a · Tier-2 · base 3e5c6d43 · streams tooling · ratified 2026-08-17

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-17-review-TOOL-aWalkedCorpus-3-2.md](../reviews/2026-08-17-review-TOOL-aWalkedCorpus-3-2.md) | spec-audit | — |
| [2026-08-17-review-TOOL-aWalkedCorpus-3-3.md](../reviews/2026-08-17-review-TOOL-aWalkedCorpus-3-3.md) | spec-audit | — |
| [2026-08-17-review-TOOL-aWalkedCorpus-3-4.md](../reviews/2026-08-17-review-TOOL-aWalkedCorpus-3-4.md) | diff-review | — |

<!-- /gen:spec-records -->

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
  unit exists to make visible. **A fixture edit that moves `h` or `R` re-derives the pin in the same
  commit**; `--audit-fixture` prints both counts and `(h-1)/(R-1)` beside the declared value so the
  obligation is checkable rather than remembered.
- **S4 — the per-id resolution assertion.** `check-recall.py` computes the SET DIFFERENCE
  `set(q["expected_ids"]) - set(bench.expected_by_target(docs, q, anchors).keys())` and reds naming
  every id in it. It is a separate predicate from the floor, not a second pin: round-2 F3 measured
  that `ceiling` counts QUERIES and cannot express per-id resolution, so a question carrying one real
  and one fictional id scores `ceiling 1.00`. The predicate is a set difference and **not** "an id
  with an empty hit set", because `expected_by_target` DROPS an unresolvable target
  (`if hits: out[tid] = hits`, `bench.py:360-361`) — the empty hit set never occurs, so rev-2's
  wording named a permanently-green assertion.
- **S5 — the leg.** A `tools/gate-legs.json` entry running S1, guarded on `tools/memory-recall/`
  and `memory/`. `.memory-tree.conf` is the third thing that can move the number and is NOT in the
  guard: govkit's `selfcheck` partitions every guard pathspec into four prefix classes — under
  `memory/`, under `.githooks/` or `.claude/`, under `skills/session-kickoff/`, or kit-relative — and
  a repo-root conf falls into none of them, so declaring it reds the bar. The cost is bounded and
  one-sided: a commit touching ONLY the pin skips this leg on a diff-scoped run, while `GATE_FULL=1`
  in the pre-push hook bypasses every guard, so the authoritative run still grades it.
- **S6 — the arms, in a gov-only file.** `tools/memory-recall/test_recall_floor.py`, with its own
  `tools/gate-legs.json` entry beside S5's. It carries one arm per row of §4's degradation table
  including the two that must fire SINGLY, plus the empty fixture, the all-miss fixture, the empty
  graded set, the absent fixture, the absent/malformed/out-of-vocabulary pin, and the
  `--audit-fixture` overlap and `hits`-disagreement reds. **`tools/memory-recall/selftest.py` is NOT touched.** Round-3 F4 measured why: it is
  shipped byte-for-byte by the `**` engine rule AND is itself a declared `[[gate_leg]]`, so an arm
  keyed on `TOOL-aWrittenMethod-4` would run on an adopter's bar against a corpus that has no such
  id, over two files S8 deliberately withholds. Arm names lead with `test`, a declared lexicon verb;
  `selftest.py`'s dominant `t_` prefix is not one, and the verb pin has zero headroom (§4).
- **S7 — the dossier.** `memory/map/features/memory-recall.md`, claiming S5's leg key and **every**
  `memory-recall` key currently in `memory/map/baseline.toml` — measured at four, not two (round-2
  F4). The coverage gate reds until a dossier claims a new leg and `baseline.toml`'s own header
  forbids new keys in itself, so the dossier is not optional.
- **S8 — the fixture stays out of adopters' trees.** `tools/memory-recall/kit.toml` gains a SECOND
  `[[files]]` rule, `include = ["recall-fixture.json", "check-recall.py", "test_recall_floor.py"]`
  with `role = "project-owned"` and no `to`. Its `include = "**"` otherwise ships a question set keyed
  on gov record ids, plus a program reading pins an adopter's conf does not carry, into every adopting
  tree with no `[[gate_leg]]` to run it (round-2 F5). §8 records what was parked instead.

  **The mechanism is claim-by-destination, and rev-2 named one that does not exist.** govkit has no
  `exclude` key: a `**` rule's pool drops only what another rule's DESTINATION claims
  (`govkit.py` `scan_claimed_paths`), and `project-owned` is absent from
  `LANDABLE_ROLES = ("engine", "seed")` so `apply` never writes it. `tools/drift-audit/kit.toml` and
  `tools/lexicon/kit.toml` are the working precedents. Round-3 F1 proved the rev-2 spelling was a
  silent no-op that `selfcheck` passes either way, which is why AC13 asserts the PAYLOAD instead.

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

**Two PRECONDITIONS stop the run; three PREDICATES all evaluate and all report.** Rev-2 wrote one
five-step short-circuit, and round-3 F2 measured what that cost: the two levers that prove the floor
and the per-id check are independent both red at per-id, so under a short-circuit the floor verdict
they assert is never computed. Separating evaluation from reporting is what makes both observable in
one run — the same split `run-gates.sh` already makes between scheduling order and reporting order.

Preconditions, in order, each redding by NAME and stopping — without either, nothing can be evaluated:

1. **The fixture** — absent, unparseable, or carrying an empty `queries` list reds naming the path.
   It does not skip. The empty list is a precondition rather than a downstream symptom because a
   question set with no questions makes the per-id predicate vacuously green.
2. **The pin** — `RECALL_FLOOR` absent, empty, or not matching
   `<set>:<sub>:<metric>@<k>>=<float>` reds naming the key. There is no default. `<set>` and `<sub>`
   are constrained to the enumerated vocabularies — `spine|records|chunks` and `bench.py`'s substrate
   names — so a one-character typo reds HERE naming the key rather than raising `FileNotFoundError`
   inside `bench.load` (round-3, med).

3. **The graded set** — `<set>.jsonl` present under the data dir and NON-EMPTY, or red naming the
   set and the dir. A floor over an empty document set is satisfied by any corpus.

Predicates. Each is evaluated, each prints its own `ok` / `RED` line, and the process exits non-zero
if ANY of them failed. Reporting order is fixed so the leading message is determinate:

4. **Per-id resolution (S4)** — the set difference above, redding with every unresolved id named. It
   REPORTS FIRST so a retired record is reported as a retired record, and it does not stop the run.
5. **The floor** — `r@k / ceiling` against the pin. **When `ceiling` is 0 the floor prints
   `not evaluated` and is not a red of its own.** That is an explicit rule, not a side effect of
   stopping early: it is what keeps the normalisation free of a 0/0 branch now that step 4 no longer
   halts the run. An all-miss fixture therefore exits non-zero on step 4 with the floor reported as
   not evaluated, which is AC5.

**Step 3 replaced a branch that could not fail, and the BUILD found that, not a review.** Rev-3 wrote
it as a predicate asking whether the pinned `<metric>@<k>` appeared in the report. Measured while
implementing: `bench.score()` emits `r@k` and `f@k` for whatever `k` it is handed, and step 2's
grammar admits only those two metrics — so the branch was green for every pin it could ever see. That
is `memory/gotchas/fixture-passes-by-finding-nothing.md` shipped inside the gate written to close it,
and it survived two adversarial spec reviews because a spec cannot be executed. The reachable state
is an absent or empty document set, which a `--data-dir` arm can produce and which `spine` — zero
docs in this repo today — produces live.

`--audit-fixture` is a separate mode over the same loaded corpus. Per question it prints the measured
`homes`, the measured `hits`, and the content-term overlap defined below; it reds when any overlap
exceeds `OVERLAP_MAX` or when a fixture's declared `hits` disagrees with the measurement. In
aggregate it prints `h`, `R` and `(h-1)/(R-1)` beside the declared `RECALL_FLOOR`, so the pin's own
derivation is re-checkable rather than living only in this section (round-3, med).

### The seam is bench's SCORING FUNCTIONS, imported — not its JSON report

`check-recall.py` imports `bench` for `load`, `build_index`, `rank_with`, `score`,
`expected_by_target` and `terms`, and `query` for `CHUNK_MAX` only. Both imports were measured
side-effect-free: `import query` costs 0.085 s and writes nothing into the kit directory.
`sys.dont_write_bytecode = True` goes ABOVE both, as `extract.py` already does — that one line is the
whole of the kit's "a query writes nothing in your tree" property.

The `--json` report is NOT the seam, and rev-2's §10 said it was. Two reasons, both measured: it is
aggregate-only and carries no target-level data, so step 3 is not computable from it at all; and it
rounds every value to four decimals (`bench.py:456`, `:475-477`), so a normalisation built on it
returns 0.9090 where the unrounded inputs give 0.9091 — a spec literal that fails against the seam
the spec names. One in-process path removes both problems and keeps `bench.py` byte-pinned, since
importing a module edits nothing.

### The pin is DERIVED from the worst case, not read off today's score

`r@k` is `h/Q` and `ceiling` is `R/Q` over one query list, so the normalised score is exactly `h/R` —
`h` questions that hit, `R` whose targets resolve at all. Retiring a record that a HITTING question
targets removes it from numerator and denominator both, so the normalised score FALLS. Rev-1 claimed
normalisation made a ceiling movement red exactly one pin; that is arithmetically false, and round-2
F2 measured it.

The fix is to price one retirement into the pin instead of pretending it costs nothing. Measured on
the committed fixture: `h=10`, `R=12`. The one-retirement worst case is `(h-1)/(R-1) = 9/11 = 0.8182`,
so the pin is **0.81**. All twelve single retirements were enumerated rather than argued: ten hitting
targets land on exactly 0.8182 and the two missing targets on 0.9091, with no collateral rank
movement, so the headroom generalises and is not a property of the one row the table shows.

**Stated precisely, because rev-2 over-stated it in the permissive direction.** The floor carries one
retirement of a **hitting** target. Retiring a NON-hitting target costs the floor nothing at all — it
drops `R` without dropping `h`, so the score RISES, which is exactly what row 3 below shows. A second
retirement reds only when both were hits: swept over all 66 two-retirement pairs, 21 stay green and
every one of them includes a currently-missing target. Rev-2's sentence "a second retirement
(`8/10 = 0.80`) reds" is therefore true of the hit-plus-hit case and false of the other 21, and the
honest version is this paragraph. A genuine regression with no retirement (`9/12 = 0.75`) reds in
every case, which is the direction that matters.

Nothing recomputes the pin from the run it grades — that is the circular-ceiling class
`aQuarriedLantern-1:568` refused. What `--audit-fixture` does instead is PRINT `h`, `R` and
`(h-1)/(R-1)` beside the declared value, so a fixture edit that moves either is visible in the same
commit rather than silently widening or narrowing the floor's slack. S3 states that obligation.

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
`records:fts5:r@5` today; `overlap` is the metric defined below. Ten hit, twelve resolve, and every
column here is MEASURED by `--audit-fixture` rather than kept by hand.

| # | expected id | homes | hits | overlap | provenance |
|---|---|---|---|---|---|
| 1 | `TOOL-aUnmannedHelm-5` | 3 | yes | 0.444 | `aWrittenMethod-2` §10 probe |
| 2 | `TOOL-aUnmannedHelm-6` | 3 | yes | 0.500 | `aWrittenMethod-2` §10 probe |
| 3 | `TOOL-aStandingWrit-2` | 2 | yes | 0.500 | `DECISIONS.md` row |
| 4 | `TOOL-aStandingWrit-4` | 2 | yes | 0.375 | `DECISIONS.md` row |
| 5 | `TOOL-cSteadyMetronome-1` | 1 | yes | 0.375 | `DECISIONS.md` row |
| 6 | `TOOL-aWidenedGuide-1` | 2 | yes | 0.429 | `DECISIONS.md` row |
| 7 | `TOOL-aWrittenMethod-4` | 3 | yes | 0.333 | `DECISIONS.md` row |
| 8 | `TOOL-aWrittenMethod-6` | 3 | yes | 0.167 | `DECISIONS.md` row |
| 9 | `TOOL-aUnmannedHelm-10` | 2 | **no** | 0.125 | `DECISIONS.md` row |
| 10 | `TOOL-aMouldedFolio-1` | 1 | **no** | 0.167 | `DECISIONS.md` row |
| 11 | `TOOL-aUnmannedHelm-9` | 2 | yes | 0.500 | `DECISIONS.md` row |
| 12 | `TOOL-cFinalBerth-1` | 2 | yes | 0.429 | `DECISIONS.md` row |

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

### The overlap metric and OVERLAP_MAX, both declared

Rev-2 converted the anti-tautology property from a prose number into a gate and then named a
threshold it never defined, which round-3 F3 filed as a knob a builder sets after seeing the result.
All three parts are declared here:

- **Tokenizer** — `bench.terms`, IMPORTED rather than reimplemented, so the audit and the index agree
  on what a content word is.
- **Formula** — `|terms(question) ∩ terms(target)| / |terms(question)|`. The denominator is the
  QUESTION's distinct content terms. The target text is the **UNION of every record carrying any of
  the question's `expected_ids`**; the Inventory table's `homes` column reaches 3, and the reduction
  has to be named because the readings disagree materially — union gives 9 of 12 strictly under half,
  first-home 11 of 12, and last-home reports 0.000 on four questions, which would hide a genuinely
  tautological question rather than catch it.
- **`OVERLAP_MAX = 0.60`**, a module constant in `check-recall.py` with its justification beside it,
  not a conf key: nothing but this gate reads it, and S3's argument for the conf was that a person
  edits the floor between releases, which is not true of this.

The value is DERIVED from the measured distribution, the same way the floor is. Over the committed
fixture: **min 0.125, mean 0.362, max 0.500**, three questions at 0.500 and **none at or above
0.60**. A query-is-the-record fixture scores ~1.0. So 0.60 sits one step above the observed maximum —
tight enough that copied text cannot pass, loose enough that today's set is not on the boundary.

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
| `tools/gate-legs.json` | S5's leg, and S6's beside it |
| `tools/memory-recall/test_recall_floor.py` | new — S6, gov-only, non-landable |
| `tools/memory-recall/kit.toml` | S8, the second `[[files]]` rule at `role = "project-owned"` |
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
- error / empty / loading states — §4's `### Data model`: two PRECONDITIONS that red by name and stop
  (absent/unparseable/empty fixture; absent, malformed or out-of-vocabulary pin) and three PREDICATES
  that each red by name without stopping (unresolved expected id, absent cell, the floor). A grading
  leg that skips when its question set is missing is the vacuity class this unit exists to close.
- observability — every predicate prints its own verdict line in one run, so a red says which half
  moved before anyone opens a file. The floor's line reads `not evaluated` when `ceiling` is 0 or the
  cell is absent, which is a REPORTED state rather than a silent skip.
- risks — **the fixture going stale as records are legitimately removed.** S4's per-id assertion names
  the unresolved id, and the pin's derived headroom absorbs the first retirement so the red arrives as
  fixture maintenance rather than as a false regression. Second risk: `pin-copied-from-another-corpus`,
  addressed by S8 and recorded in §8.
- testing + left-shift gates — S6, and the two single-direction arms are the unit's centre.
- migration / rollback — revert; the program, the fixture, the pin and the leg land together.
- user docs — `tools/memory-recall/README.md` gains the fixture, the pin and the re-measure command.

## 6. Acceptance criteria

Every criterion below observes a PRINTED verdict line rather than the absence of a string, because
round-3 F2 found that rev-2's phrasing ("the floor stays green") asserted a state the short-circuiting
program never reached.

- **AC1** — When `python tools/memory-recall/check-recall.py` runs on a clean tree it exits 0 and
  prints one line per predicate: the cell `records:fts5:r@5`, the raw score, the ceiling, the
  normalised score, and `per-id: ok`.
- **AC2a** — **The floor reds ALONE.** With only the `memory/DECISIONS.md` record for
  `TOOL-aWrittenMethod-4` removed from an extracted dir, `check-recall.py --data-dir` exits non-zero,
  prints `RECALL_FLOOR` RED at a normalised 0.7500 against the 0.81 pin, and prints `per-id: ok` in
  the same run.
- **AC2b** — **The per-id assertion reds ALONE.** With every record for `TOOL-aMouldedFolio-1`
  removed, `check-recall.py --data-dir` exits non-zero, names that id on its per-id line, and prints
  the floor line as `ok` at a normalised 0.9091 — both verdicts in one run.
- **AC2c** — **One retirement of a hitting target is free.** With every record for
  `TOOL-aStandingWrit-2` removed, the printed normalised score is 0.8182, the floor line reads `ok`,
  and only the per-id line reds.
- **AC3** — With `tools/memory-recall/recall-fixture.json` absent, unparseable, or carrying an empty
  `queries` list, `check-recall.py` exits non-zero naming that path. It does not skip and does not
  exit 0.
- **AC4** — With `RECALL_FLOOR` absent, empty, not matching the pin grammar, or naming a set or
  substrate outside the enumerated vocabularies, `check-recall.py` exits non-zero naming the key. A
  pin reading `record:fts5:r@5>=0.81` reds here rather than raising inside `bench.load`.
- **AC5** — With an all-miss fixture, `check-recall.py` exits non-zero on the per-id line and prints
  the floor line as `not evaluated`, never dividing by a zero `ceiling`.
- **AC5b** — With the pinned set absent from the data dir, or present and empty, `check-recall.py`
  refuses naming the set and the dir. A pin of `spine:fts5:r@5>=0.81` reproduces it live, because
  `spine` extracts to zero docs in this repo.
- **AC6** — When `bash tools/run-gates.sh` runs, both new legs appear by name and are green.
- **AC7** — When `python tools/memory-recall/test_recall_floor.py` runs it exits 0, and inverting any
  one arm — including the `--audit-fixture` overlap arm — reds it naming that arm.
- **AC8** — When `python tools/codebase-map/test_codebase_map.py` runs after
  `python tools/codebase-map/gen_map.py --write`, coverage and freshness are green, and every
  `memory-recall` key is claimed by `memory/map/features/memory-recall.md` and absent from
  `memory/map/baseline.toml`.
- **AC9** — When `python tools/memory-recall/check-recall.py --audit-fixture` runs, it prints each
  question's measured `homes`, `hits` and overlap; every overlap is at or below `OVERLAP_MAX` of
  0.60; and a fixture whose questions are copied from their targets' text reds naming the offending
  question index and its measured overlap.
- **AC10** — When `--audit-fixture` runs it prints `h`, `R` and `(h-1)/(R-1)` beside the declared
  `RECALL_FLOOR`, and reds when any question's declared `hits` disagrees with the measurement.
- **AC11** — When `python tools/drift-audit/drift_report.py --check` runs,
  `handkept_inventories_disagreeing_with_source` still reports 0 at pin 0.
- **AC12** — When `python tools/memory-recall/bench.py` and `tools/memory-recall/union.py` are
  compared against `tools/memory-recall/verbatim.json`, both digests are unchanged.
- **AC13** — When the `**` rule's pool is resolved through govkit's own `resolve_rule_pool`, it
  contains none of `recall-fixture.json`, `check-recall.py` or `test_recall_floor.py`, and still
  contains `selftest.py`. The assertion is over the PAYLOAD, not over `selfcheck`'s exit code, which
  round-3 F1 measured green against a key govkit never reads. It is an ARM in
  `test_recall_floor.py` rather than a manual `plan` invocation, because `plan` refuses without a
  target descriptor `intake` writes — so a one-time command could not have been a standing check.
- **AC14** — When `python tools/lexicon/lexicon.py` runs it exits 0, with every new definition's name
  leading with a declared verb.

## 7. Gates

- `python tools/memory-recall/selftest.py` — the verbatim pins and the kit contract, UNCHANGED by
  this unit and green as the proof it stayed adopter-safe.
- `python tools/memory-recall/test_recall_floor.py` — S6's arms.
- `python tools/memory-recall/check-recall.py` — the new leg itself.
- `python tools/govkit/govkit.py selfcheck` and `... plan --kits memory-recall <target>` — the kit
  payload changes, and only `plan` can observe it.
- `bash tools/run-gates.test.sh` — the canary over the changed manifest.
- `python tools/codebase-map/test_codebase_map.py` — the new leg key and the new dossier.
- `python tools/lexicon/lexicon.py` — zero headroom on the verb pin; see §4.
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

- rev-5 · 2026-08-17 · **folded the round-4 closing review of the BUILT unit: SHIP WITH FIXES, 0
  blockers, 2 high, 3 medium, 6 low — all 11 applied, each with an arm.** F2 (high) is the sharp one
  and it is this unit's own subject class for the third time: `measure_overlap` re-implemented target
  resolution records-only, so a question the run could not resolve scored `overlap 0.000` — a PASS,
  and under a `chunks:` pin EVERY row read 0.000 with the guard fully vacuous. It now reuses the
  run's own targets, reports NOT MEASURED as a red, and excludes unmeasured rows from the summary;
  the chunks pin measures 12/12 through the anchor map. F1 (high): every arm leaked an ~8 MB corpus
  copy, 15 per run, ~2 GB accumulated on one node — tracked and removed, with a leak-delta assertion
  in `main()`. F3: `build_data_dir`'s refusal escaped as a traceback at exit 1, the one branch no arm
  reached because all of them pass `--data-dir`; one handler now covers both preconditions and the
  refusal carries extract's last stderr line rather than its whole trace. F4: `read_fixture`
  validated the container, not the questions. The six lows: the derivation guard is one-directional
  and three records said otherwise (narrowed to what the code does), the withholding binds
  `govkit apply` only so `WIRE-INTO-PROJECT.md` gains its own delete step, the arms leg guard gains
  `tools/govkit/`, the fixture header contradicted its own armed gate, `sys.path.insert` sat after
  the import it enabled (15 of 16 arms died under `-P`), `gate-legs.json` had been rewritten
  wholesale into 639/617 lines with three non-ASCII bytes and is now a 23-line ASCII addition, and
  `measure_run` returned a dead `anchors` key that made F2's gap look covered. Arms 16 -> 20; the
  bar is 65/65.
- rev-4 · 2026-08-17 · **the BUILD found what two adversarial spec reviews could not.** rev-3's
  predicate 4 asked whether the pinned `<metric>@<k>` appeared in the report; `bench.score()` emits
  `r@k` and `f@k` for any `k`, and the pin grammar admits only those two metrics, so the branch was
  green for every pin reachable through it — the `fixture-passes-by-finding-nothing` class inside the
  gate written to close that class. It becomes precondition 3, the graded set being present and
  NON-EMPTY, which `spine` (zero docs here) fires live. §4 now reads three preconditions and two
  predicates, and AC5b observes the new one. Nothing else moved: the two single-direction levers, the
  derived pin and the overlap declaration are unchanged.
- rev-3 · 2026-08-17 · **folded the round-3 re-review, which returned BLOCKED on two — and BOTH were
  defects rev-2's own fold introduced, which is the finding about this build's method rather than
  about its subject.** F1: S8's `[[files]] exclude` is a key govkit does not implement, so the F5 fold
  was a silent no-op that `selfcheck` passed either way; the mechanism is claim-by-destination with a
  non-landable role, verified here against `scan_claimed_paths` and `LANDABLE_ROLES`, and AC13 now
  asserts the PAYLOAD via `govkit plan`. F2: the five-step evaluation order added to fold round-2's F6
  short-circuited at per-id resolution, so AC2b and AC2c asserted a floor verdict the program never
  computed — §4 now separates two PRECONDITIONS that stop from three PREDICATES that all evaluate and
  all print, with `ceiling == 0` an explicit `not evaluated` rule rather than a side effect of halting.
  F3: `OVERLAP_MAX` was named three times and defined nowhere over a metric whose denominator swings
  the measurement fivefold; §4 declares the tokenizer, the formula, the union-over-homes reduction and
  the value 0.60, derived from a measured distribution (max 0.500, mean 0.362, none at or above 0.60)
  now carried as an Inventory column. F4: S6's arms would have put gov record ids into `selftest.py`,
  which ships to every adopter AND runs on their bar, so they move to a gov-only
  `test_recall_floor.py` under the same non-landable rule and `selftest.py` is untouched. F5: the
  one-retirement headroom claim over-stated — 21 of 66 two-retirement pairs stay green — and §4 now
  states the hitting/non-hitting asymmetry the table already showed. Also: the pin grammar constrains
  set and substrate to their vocabularies so a typo reds at the pin rather than raising inside
  `bench.load`; §10 corrects the seam from the rounded `--json` report to the imported scoring
  functions; and `--audit-fixture` now measures the fixture's own `hits`, `homes`, `h` and `R` so
  three hand-kept claims become observed ones.
  **The next pass is the BUILD, not a fourth review round.** Two rounds of folding produced two
  rounds of fold-introduced blockers, and `memory/guides/REVIEW-PROTOCOL.md` names the exit:
  building is cheaper and stricter than another spec pass. M8's closing diff review is the backstop.
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
`bench.py`'s SCORING FUNCTIONS — `load`, `build_index`, `rank_with`, `score`, `expected_by_target`
and `terms`, imported in-process — and the shape it copies is `check-template-size.sh`'s, a declared
number in a file a person edits with its justification beside it.

**Not the `--json` report, and rev-2 said it was.** That report is aggregate-only, so the per-id
predicate is not computable from it at all: `expected_by_target` drops an unresolvable target before
`ceiling` is ever counted, and no target-level data survives into the JSON. It also rounds to four
decimals, which turns the 0.9091 this spec measures into 0.9090 for anyone who implements against it.
Importing edits nothing, so `verbatim.json`'s byte pin on `bench.py` is untouched either way.

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
