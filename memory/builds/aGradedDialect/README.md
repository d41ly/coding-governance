---
slug: aGradedDialect
node: a
opened: 2026-09-10
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-aGradedDialect-1 TOOL-aGradedDialect-2 TOOL-aGradedDialect-3 TOOL-aGradedDialect-4 TOOL-aGradedDialect-5
---

# aGradedDialect — the lexicon kit cannot read TypeScript, and the one repo that would adopt it is 20% TypeScript by file

## The problem this build exists to solve
The lexicon kit ships three extractors: a Python AST parser, a shell tokenizer, and one regex probe
set for `.js`. Nothing reads `.ts` or `.tsx`. An adopter running `--scaffold` gets `ts::dark
tsx::dark` written into their own declaration by the tool, with no refusal and no note, and the gate
then prints `lexicon OK` over the fraction of the tree it can see.

That absence is a ratified decision, `TOOL-dScaffoldedMirror-13`, and not an oversight. It was
measured against `C:/projects/incms/main`: 6168 tracked files, 1198 of them `.ts`/`.tsx`, armed
coverage 19.3%. The decision named its own revisit test, and both halves now hold - `-8` closed on
2026-08-25, and that corpus is present on this node. This build is the session that test asked for.

## Expected improvements
- The kit reads the language its only real adopter is written in, so the vocabulary and convention
  apparatus grades something rather than reporting a fraction.
- The fixtures that prove the reading come from real adopter files, so the conformance claim stops
  round-tripping through the reader it is meant to grade.
- The `.ts`/`.tsx` ruling in `LEXICON.md` becomes a description of what ships instead of a refusal.

## Detriments if this is not built
- A kit whose product is a naming vocabulary stays blind to the language its adopter writes, and the
  coverage fraction keeps reporting that honestly and uselessly.
- `-13` stays DEFERRED with its revisit condition met, which is the state a deferral is least
  readable in: satisfied, unacted, and indistinguishable from forgotten.
- Every future adopter keeps meeting a silent `dark` seed written by the tool they just installed.

## Build-level rules
- **THE RECORDED OBJECTIONS ARE THE ACCEPTANCE BAR.** `-13` refused a probe for four reasons, and a
  design that does not answer all four is a reopening rather than a revisit: it would arm a casing
  rule over 1072 PascalCase React components; it would arm a synonym predicate over a TypeScript
  corpus nobody has measured; its conformance fixture would round-trip through its own reading;
  and it would multiply `js-regex`'s vacuity defect before that defect was closed.
- **FIXTURES BEFORE THE EXTRACTOR, and that ORDER is the answer to the tautology objection.** A
  fixture extracted before the reader exists cannot have been extracted by it. Sequencing is the
  mechanism here; an assertion that the author was careful is not.
- **MEASURE ON THE REAL CORPUS, READ-ONLY.** Every figure this build states about TypeScript comes
  from a read of `C:/projects/incms/main`. That tree is not this repo's, is not modified, and is not
  adopted onto - a measurement is not an installation.
- **NO COUNT OF A DERIVED POPULATION IS WRITTEN IN PROSE** that a checker could derive instead. The
  figures above are cited from a dated measurement and carry their date.
- **THE COVERAGE MODE IS A CLAIM WITH TEETH.** Whatever ships declares `parser` or `probe` and lives
  by that row's standing: `parser` means complete over its extension and owes a refusal on anything
  it cannot read; `probe` means incomplete by construction and says so every run. Splitting the
  difference is what the modes table exists to forbid.

## Parked decisions

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aGradedDialect-1` | PLANNED | the research and the pick: candidates for reading TypeScript definitions, each tested by what would make it LOSE, measured against the real adopter corpus, with the rejected candidates' tests recorded |
| 2 | `TOOL-aGradedDialect-2` | PLANNED | the conformance corpus: definition-site fixtures EXTRACTED from real adopter files by an oracle independent of anything this build ships, frozen, and authored BEFORE the extractor exists |
| 3 | `TOOL-aGradedDialect-3` | PLANNED | the extractor unit 1 picked, with its refusals enumerated in its own header and its coverage mode declared and defended |
| 4 | `TOOL-aGradedDialect-4` | PLANNED | the declaration surface: `KNOWN_EXTS`, the scaffold's proposal for a TypeScript tree, and the cell matrix that answers the PascalCase-component objection without a per-name exception list |
| 5 | `TOOL-aGradedDialect-5` | PLANNED | the records: the `LEXICON.md` ruling replaced rather than amended, the kit README, and `TOOL-dScaffoldedMirror-13` closed against its own revisit test |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 5 unit(s) · node a · opened 2026-09-10 · streams tooling
ids TOOL-aGradedDialect-1 TOOL-aGradedDialect-2 TOOL-aGradedDialect-3 TOOL-aGradedDialect-4 TOOL-aGradedDialect-5

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aGradedDialect-1 — the mechanism fork for reading TypeScript, resolved against the compiler](spec/2026-09-10-spec-TOOL-aGradedDialect-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-09-10 |
| [TOOL-aGradedDialect-2 — the conformance corpus: fixtures a compiler extracted, frozen before the reader exists](spec/2026-09-10-spec-TOOL-aGradedDialect-2.md) | 2 | 2 | SPECCED | rev-4 | 2026-09-10 |
| [TOOL-aGradedDialect-3 — the TypeScript extractor: a tokenizer, a definition locator, and a coverage mode it has to earn](spec/2026-09-10-spec-TOOL-aGradedDialect-3.md) | 3 | 2 | SPECCED | rev-3 | 2026-09-10 |
| [TOOL-aGradedDialect-4 — the declaration surface for TypeScript, and the `.tsx` casing row as a declared refusal](spec/2026-09-10-spec-TOOL-aGradedDialect-4.md) | 4 | 2 | SPECCED | rev-4 | 2026-09-10 |
| [TOOL-aGradedDialect-5 — the records: the darkness ruling retired where it is actually carried](spec/2026-09-10-spec-TOOL-aGradedDialect-5.md) | 5 | 1 | SPECCED | rev-4 | 2026-09-10 |
<!-- /gen:build-units -->

Records: 8 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aGradedDialect-1` | no |
| 2 | `TOOL-aGradedDialect-2` | no |
| 3 | `TOOL-aGradedDialect-3` | no |
| 4 | `TOOL-aGradedDialect-4` | no |
| 5 | `TOOL-aGradedDialect-5` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
