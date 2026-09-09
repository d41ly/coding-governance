# TOOL-aGradedDialect-1 — the mechanism fork for reading TypeScript, resolved against the compiler

**Status:** INPROGRESS · rev-2 · 2026-09-10 · node a · Tier-2 · base d1357673 · streams tooling · order 1 · ratified 2026-09-10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-10-build-TOOL-aGradedDialect-1-typescript-extraction-research.md](../build/2026-09-10-build-TOOL-aGradedDialect-1-typescript-extraction-research.md) | research | — |
| [2026-09-10-prompt-TOOL-aGradedDialect-1-spec-brief.md](../prompts/2026-09-10-prompt-TOOL-aGradedDialect-1-spec-brief.md) | journal | TOOL-aGradedDialect-2 TOOL-aGradedDialect-3 TOOL-aGradedDialect-4 TOOL-aGradedDialect-5 |
| [2026-09-10-review-TOOL-aGradedDialect-1-round1.md](../reviews/2026-09-10-review-TOOL-aGradedDialect-1-round1.md) | spec-audit | TOOL-aGradedDialect-2 TOOL-aGradedDialect-3 TOOL-aGradedDialect-4 TOOL-aGradedDialect-5 |
| [2026-09-10-review-TOOL-aGradedDialect-1-round2.md](../reviews/2026-09-10-review-TOOL-aGradedDialect-1-round2.md) | spec-audit | TOOL-aGradedDialect-2 TOOL-aGradedDialect-3 TOOL-aGradedDialect-4 TOOL-aGradedDialect-5 |
| [2026-09-10-review-TOOL-aGradedDialect-1-round3.md](../reviews/2026-09-10-review-TOOL-aGradedDialect-1-round3.md) | spec-audit | TOOL-aGradedDialect-2 TOOL-aGradedDialect-3 TOOL-aGradedDialect-4 TOOL-aGradedDialect-5 |

<!-- /gen:spec-records -->

## 1. Goal

Decide by what MECHANISM the lexicon kit reads TypeScript, against measurement rather than
preference, and leave the losing candidates' tests on the record so the next build does not pay to
re-run them. The owner's prompt settled THAT the kit will read TypeScript; this unit settles HOW.

## 2. Scope (IN)

- **S1** — enumerate candidates that differ in MECHANISM, and write down what would make each LOSE
  before any of them is measured. Observed by **AC1**.
- **S2** — measure the adopter corpus read-only, with an oracle independent of everything this kit
  ships and everything this build will write. Observed by **AC2**.
- **S3** — score the regex family against that oracle, on recall, on precision, and on the
  disagreement between two plausible regex sets. Observed by **AC3**.
- **S4** — measure the two objections `TOOL-dScaffoldedMirror-13` raised about the VOCABULARY, since
  measuring them is what discharges them. Observed by **AC4**.
- **S5** — record the pick, the three losses with the test that killed each, and the one problem the
  pick does not solve. Observed by **AC5**.

## 3. Non-goals (OUT)

- **No extractor.** M3 forbids a probe that builds an arm of its own fork to watch it behave, and
  the reader this unit picks is `TOOL-aGradedDialect-3`'s to write.
- **No fixtures.** The oracle is demonstrated here as evidence; freezing a fixture corpus from it is
  `TOOL-aGradedDialect-2`'s, and doing it here would put the fixtures in the same pass as the
  decision they are supposed to be independent of.
- **No `parser` claim.** This unit picks a mechanism whose ceiling is a parser. Whether the artifact
  reaches it is measured by unit 3 against unit 2's floor, and asserting it here would be the
  could-not-fail shape.
- **No adoption of the kit onto the adopter tree.** `TOOL-dScaffoldedMirror-13` §3 draws that line;
  a measurement is not an installation and this build keeps the distinction.
- **No verdict on `.js`.** Reading A was scored against TypeScript files. Whether `js-regex` should
  also retire is a different population and a backlog row.

### Edges

- **consumes-from** external — `typescript@5.9.3`, present in the adopter tree as a dev dependency.
  It is the ORACLE and is used once, offline, to produce evidence; nothing this kit ships imports it,
  and without it the measurements in §4 have no ground truth and the fork falls back to argument.
- **hands-off** `TOOL-aGradedDialect-2` — the oracle procedure, for that unit to freeze into a
  fixture corpus with a declared floor.
- **hands-off** `TOOL-aGradedDialect-3` — the picked mechanism and the construct census its refusal
  list is derived from.
- **hands-off** `TOOL-aGradedDialect-4` — the casing measurement, and the `.tsx` role-split problem
  this unit states and deliberately does not solve.

## 4. Design

The work IS the record, and the record is
`memory/builds/aGradedDialect/build/2026-09-10-build-TOOL-aGradedDialect-1-typescript-extraction-research.md`.
Its §6 carries both probe snippets runnable, so every figure re-derives.

**This section POINTS rather than restating.** The tables in that record and a copy of them here
would be one fact in two carriers with no gate between them, which is the class this build's README
names as its own bar. What follows is only what a reader needs in order to know whether to open it.

### Alternatives rejected

| # | mechanism | the test that killed it |
|---|---|---|
| C1 | a `ts-regex` set in `PATTERN_SETS`, mode `probe` | two plausible regex sets disagree on 22.4% of the function population, over the 20% threshold registered before the run |
| C3 | shell out to `tsc` or `esbuild` | M3 veto 2 — a new external dependency and install location, against a kit that ships a self-containment refusal and an adopter not required to have Node |
| C4 | the same regexes proposed by `scaffold_lexicon.py` into the adopter's own declaration | C1's test, because C4 changes the carrier and not the reading |

C2 — a tokenizer plus a definition locator, the `shell-tokens` design ported — is the survivor and
the most feature-rich of them by M3's rule: the only candidate with no false positives by
construction, and the only one whose failure mode is a refusal rather than a quiet undercount.

### Inventory

This unit mints no identifier. It writes one record and one spec, and every name in it belongs to a
sibling unit.

## 5. Production-readiness checklist

- security — N/A. The unit reads an adopter tree and writes nothing to it; no surface moves.
- perf / scale — the oracle walks 1257 files in seconds. N/A as a design constraint.
- error / empty / loading states — N/A. The unit produces a record, not a runtime.
- observability — the record's §6 snippets ARE the observability: every figure re-derives.
- risks — the adopter tree is a third-party checkout that may move or vanish. The figures are
  therefore PINNED with their date and the tree's path, never presented as live.
- testing — the losing conditions were registered before the measurements ran, which is what makes
  them tests. Nothing else here is testable and §6 says so per criterion.
- migration — N/A. No artifact changes.
- user docs — N/A for this unit; `TOOL-aGradedDialect-5` owns every reader-facing carrier.

## 6. Acceptance criteria

- **AC1** — When `2026-09-10-build-TOOL-aGradedDialect-1-typescript-extraction-research.md` is read,
  its §3 table names four candidates differing in mechanism, each with a losing condition, and its
  §4 reports the outcome of applying them.
  Red when: a candidate's losing condition is written after its measurement, so the table records a
  rationalisation rather than a test.
- **AC2** — When `ts-oracle.js` from the record's §6 is run over the adopter's tracked TypeScript,
  it emits one JSON line per file and the totals match the record's §2 table.
  `figure:` DERIVED — the snippet re-derives both totals.
  `fixture:` the adopter tree at `C:/projects/incms/main` with its `node_modules/typescript`
  present; absent, this criterion cannot be observed and says so rather than passing.
  Red when: the oracle emits fewer lines than the file list, which is a read it silently skipped.
- **AC3** — When `regex_vs_oracle.py` scores both regex readings, the shipped `js-regex` types
  pattern recalls under 1% of the type population and the two readings disagree on over 20% of the
  function population.
  `figure:` DERIVED. Red when: the two readings agree closely, which would refute the pick and send
  the fork back to C1.
- **AC4** — When the record's §4.4 is read, it states the casing distribution per EXTENSION and the
  `canon.py` verb-lead rate for both, each as a measured figure with its date.
  Red when: §4.4 argues either objection away instead of reporting a number.
- **AC5** — When §3, §4 and §5 of
  `2026-09-10-build-TOOL-aGradedDialect-1-typescript-extraction-research.md` are read, §3 names the
  four losing conditions, §4.1 and §4.3 report the three losses against them, and §5 names the pick,
  the `.tsx` role-split problem the pick does not solve, and the `case:` selector refusal by the
  vacuity argument.
  Red when: the record claims the pick solves the casing split, which the `.tsx` figures refuse.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `memory hygiene`

This unit adds no gate arm — it writes a record and a spec, and the legs above are the ones its files
must not red. The extractor's arms are units 2 and 3.

## 8. Open questions

- **F1 — by what mechanism does the kit read TypeScript?** Four candidates, in §4's table and the
  record's §3. RESOLVED (agent, 2026-09-10, delegated): C2, a tokenizer plus a definition locator in
  the kit, the `shell-tokens` design ported. C1 and C4 lose to the 22.4% inter-regex disagreement
  registered as the losing condition before the run; C3 loses to M3 veto 2. The mandate for this
  build is the owner's prompt, which lifted `TOOL-dScaffoldedMirror-13`'s deferral by naming its own
  revisit test as met.
- **F2 — does `TOOL-dScaffoldedMirror-13` bind this build?** RESOLVED (agent, 2026-09-10,
  delegated): it binds as an ACCEPTANCE BAR and not as a refusal. Its four objections are the
  standard this build's design is measured against, and its non-goals were that unit's own scope
  rather than a standing prohibition. Its revisit test is met on both halves, so this is the session
  it asked for rather than an override of it.

## 9. Revision log

- rev-1 · 2026-09-10 · initial draft, authored after the research it records.
- rev-2 · 2026-09-10 · AC5 · S5 · folded spec-audit round 1. AC5 addressed §5 of the record alone
  while S5 scopes three clauses that land in §3, §4.1 and §4.3; the criterion now names the sections
  that actually carry each one, rather than inviting a fold that would copy them into §5.
  Its Red-when is unchanged and still traps a claim the record does not make. The round's blocker
  against §4 and §5 was folded in the RECORD rather than here: `regex_vs_oracle.py` is now
  reproduced in that record's §6, so this spec's "both probe snippets runnable" claim became true
  where it stood instead of needing a retraction.

## 10. Reuse audit

The seam this build extends is `tools/lexicon/lexicon.py:parse_shell_defs` together with the `mode`
dispatch in `extract_text` at the same file — the shell tokenizer is the ratified precedent for a
hand-written reader in this kit, and `reuse_lookup.py` ranked it in the candidate set for the
behaviour phrase below. `tools/codebase-map/reuse_lookup.py "extract function and type definitions
from a source file for a language the kit does not parse"` also returned `extract` and `extract_text`
in the same file as SEAM-ranked neighbours. Verified against source on 2026-09-10: both functions
exist at that path and `extract_text` dispatches on `mode`, reading `pset` only under `probe`. Note
the probe's own reported blindness — it prints `unscanned layers: .sh`, so a shell-side seam would
not have appeared and no claim here rests on its silence about shell.

Recall terms used: `lexicon typescript tsx probe parser dark PATTERN_SETS coverage extractor
PascalCase React casing tokenizer adopter`
