# TOOL-aWalkedCorpus-2 — the corpus gets something that grades it

**Status:** SPECCED · rev-1 · 2026-08-16 · node a · Tier-2 · base b4f0cf1c · streams tooling

## 1. Goal

The recall corpus can widen, narrow or be re-walked and nothing measures whether retrieval got
worse. `aDeclaredCeiling` widened it and said so in its own §5: "unfalsifiable against precision by
construction". `bench.py` already computes the metrics; what is missing is a committed question set
and a pinned merge-bar leg. Ship both.

## 2. Scope (IN)

- **S1 — the fixture.** `tools/memory-recall/recall-fixture.json`: a committed set of questions,
  each with the record ids that ANSWER it. Authored from questions this repo actually asked — the
  `§10` recall probes of landed specs, whose answers are known independently of what the index
  currently returns.
- **S2 — the leg.** A `tools/gate-legs.json` entry running `bench.py` over the fixture and refusing
  a score below a declared floor. Guarded on `tools/memory-recall/` and `MEMORY_ROOT`, because those
  are the two things that can move the number.
- **S3 — the floor is DECLARED and MEASURED.** `.memory-tree.conf` gains `RECALL_FLOOR`, pinned to
  what the tree actually scores at build time, with the measuring run named beside it. Shrink-only
  in the sense that matters: the score may rise and the floor may follow, but a fall reds.
- **S4 — the arms.** `tools/memory-recall/selftest.py` gains: the floor FALLS when the corpus is
  degraded, and the leg reds. This is the whole unit — a floor nobody has watched fail is a
  decoration, and this repo names that anti-pattern in `drift_signals.py`.
- **S5 — the ceiling metric is reported, not gated.** `bench.py` already separates "retrieval missed
  it" from "the data was never there". The leg prints both; only the retrieval half is pinned,
  because a fixture naming a record that has been legitimately archived should tell a reader why it
  dropped rather than red the bar for the wrong reason.

## 3. Non-goals (OUT)

- **Tuning retrieval.** This unit measures; it does not change ranking, weighting or the index
  shape. A floor that lands together with the change that moves it cannot tell you which did what.
- **A fixture that covers the corpus.** Coverage is a different and much larger unit. This one ships
  a small, honest set whose answers were determined independently, and says so.
- **Grading `spine`.** `bench.py` takes `--sets`; this leg grades `records` and `chunks`, the two
  sets `check_recall.py` already treats as the graded pair.

## 4. Design

### The vacuity risk is the whole design problem

A fixture authored by reading what the index currently returns is a tautology: it would pass on the
day it lands and could never fall for a real reason. Two properties keep it honest:

1. **Provenance.** Every question comes from a `§10` recall probe a landed spec already ran, and its
   expected ids are the records that spec cited as the answer. Those were determined by a human
   reading records, before this fixture existed.
2. **A red proof.** S4 degrades the corpus — remove a declared source, or narrow `MEMORY_ROOT` —
   and asserts the score falls through the floor. A floor that has only been seen to pass is an
   assertion about nothing, which is the rule this repo applies to every other gate it ships.

### Why the floor is declared rather than hardcoded

`TOOL-aDeclaredCeiling-1` established the pattern one build ago and its reasoning transfers exactly:
a number with its justification beside it, in a file a person edits, separate from anything a tool
rewrites. The measuring run is named next to the value so a later reader can reproduce it.

### What this does NOT prove, stated rather than implied

A floor over a small fixture measures that these questions still find these records. It does not
measure precision over the corpus as a whole, and a change that improves these queries while
degrading a hundred others passes. That is a real limit of a small question set and the reason §3
scopes coverage out rather than pretending the floor is a quality guarantee.

### Files touched

| File | Change |
|---|---|
| `tools/memory-recall/recall-fixture.json` | new — S1 |
| `tools/gate-legs.json` | S2's leg |
| `.memory-tree.conf` | S3's floor + its justification |
| `tools/memory-recall/selftest.py` | S4 |
| `AGENTS.md` | the gate-suite citation, or the charter signal reds |
| `memory/map/features/*` | the new leg key claimed, or coverage reds |
| `tools/govkit/registry.toml` | not owed — the fixture is under `tools/memory-recall/`, not depth-1 |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamp: `gate-legs.json` and `.memory-tree.conf` are watched |

## 5. Production-readiness checklist

- security / a11y / i18n — N/A.
- perf — `bench.py` over a small fixture against an already-built index; the leg is guarded so it
  runs only when the kit or the corpus moves.
- error / empty / loading states — an absent fixture must red by NAME, not skip. A grading leg that
  silently passes when its question set is missing is the vacuity class this unit is about.
- observability — the leg prints the score and the ceiling, so a fall says which half moved.
- risks — **the fixture going stale as the corpus legitimately changes.** A record cited as an
  expected answer can be archived or superseded, and the ceiling metric (S5) is what distinguishes
  that from a retrieval regression. Reported, not gated, for that reason.
- testing + left-shift gates — S4, and it is the unit's centre rather than its tail.
- migration / rollback — revert; the leg and the floor land together.
- user docs — the kit README gains the fixture and the floor.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-recall/bench.py` runs over the committed fixture, it reports a
  score at or above `RECALL_FLOOR`, and the value of the floor equals what the run measures at
  landing. Declared, not chosen.
- **AC2** — **The floor can FALL.** With a declared corpus source removed,
  `python tools/memory-recall/bench.py` over the same fixture scores BELOW `RECALL_FLOOR` and the
  leg exits non-zero. Observed, not argued.
- **AC3** — With `tools/memory-recall/recall-fixture.json` absent, the leg reds naming that path
  and does not skip.
- **AC4** — When `bash tools/run-gates.sh` runs, the new leg appears by name and is green.
- **AC5** — When `python tools/memory-recall/selftest.py` runs it exits 0, and inverting S4's arm
  reds it naming that arm.
- **AC6** — When `python tools/codebase-map/test_codebase_map.py` runs, coverage and freshness are
  green with the new leg key claimed in a dossier.
- **AC7** — When `python tools/drift-audit/drift_report.py --check` runs,
  `handkept_inventories_disagreeing_with_source` still reports 0 at pin 0 — the charter was told
  about the new leg.
- **AC8** — When `tools/memory-recall/recall-fixture.json` is read, every question carries a
  `from` field citing the landed spec §10 it came from. A question with no provenance is one
  somebody wrote to fit the current output.

## 7. Gates

- `python tools/memory-recall/selftest.py` · `python tools/memory-recall/bench.py` over the fixture.
- `bash tools/run-gates.test.sh` — the canary over the changed manifest.
- `python tools/codebase-map/test_codebase_map.py` — the new leg key.
- `python tools/drift-audit/drift_report.py --check` — the zero-tolerance charter signal.
- `bash skills/session-kickoff/manifest-check.sh` — two watched pathspecs move.
- `bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

none.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft. The gap was stated by `TOOL-aDeclaredCeiling-2` as a non-goal
  and again in its §5 risks, and left unrecorded outside a closed spec. The design pass found that
  the instrument already exists — `bench.py` computes recall@k, full@k, MRR and a ceiling — so the
  unit is a fixture and a pin, not a measurement harness, which is a much smaller thing than the
  non-goal implied.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "grade retrieval quality against a fixture of expected
answers"` — the seam is `tools/memory-recall/bench.py`, which is committed, stdlib-only, and already
computes every metric this unit needs. Its own header records why it exists: the original harness
lived in a session scratchpad and was lost, "which made every number it produced unfalsifiable".
This unit is the other half of that sentence — the numbers become falsifiable when a fixture and a
floor are committed beside the instrument.

`python tools/memory-recall/query.py "what stops a gate from passing by measuring nothing" --terms
"vacuous selector empty population pin floor shrink-only arm red proof fixture decoration ceiling"`
— run before writing §4, and it is where the two anti-vacuity properties come from: this corpus
already holds the rule that a gate seen only to pass is an assertion about nothing.

**Read rather than assumed:** `bench.py`'s usage block and metric definitions were read end to end
before S1 and S5 were written. The `ceiling` metric is the reason S5 exists and it was not inferred
from the name — the header states it separates "retrieval missed it" from "the data was never
there", which is exactly the distinction a stale fixture needs.
