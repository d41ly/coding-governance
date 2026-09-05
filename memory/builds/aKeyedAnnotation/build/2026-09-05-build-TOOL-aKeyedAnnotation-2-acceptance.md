<!-- **Serves:** journal TOOL-aKeyedAnnotation-2 -->
**Serves:** journal TOOL-aKeyedAnnotation-2

# aKeyedAnnotation unit 2 — acceptance ledger

**Evidences:** TOOL-aKeyedAnnotation-2

- AC1 — `python tools/drift-audit/selftest.py` — a spec header carrying a correction-form id, placed
  in a scratch tree, is counted as KEYED: the judgeable population rises by exactly one. Observed RED
  against the hand-typed pattern, where the same spec was absent from the population entirely rather
  than reported.
- AC2 — `python tools/drift-audit/selftest.py` — both halves, because only the pair discriminates. An
  id cited ONLY from a test file is not in the signal's detail; the same id cited from a product file
  is. Observed RED against the wide product population, which counted the test-file citation.
- AC3 — `python tools/drift-audit/drift_report.py --json` — the pin comment's file no longer appears
  in the citation set for either pinned id. Before this unit it appeared in BOTH, which is what made
  the pin undrainable by removing the annotations it described.
- AC4 — `python tools/drift-audit/selftest.py` — in a scratch tree with every remaining product
  citation deleted, the signal's VALUE reaches zero while its judgeable population does not. Two
  separate checks, because they are different fields and an arm on the population would have been
  green whatever the citations did. Observed RED against the wide population, where the value stayed
  at 1.
- AC5 — `python tools/drift-audit/drift_report.py --json` — after this unit the signal reports value
  2 against its pin of 2, with both liveness halves non-empty and live true. The two population
  figures are DERIVED by that command and not copied here. Only ONE of them can move when the globs
  narrow — the evidence-file count — and it did, twice, as the closing review tightened the
  exclusions. The judgeable population counts non-terminal keyed specs and is computed BEFORE any
  glob is read, so it moves when the grammar changes and never when the population declaration
  does. An earlier revision of this line credited the narrowing with both, which is the same
  conflation AC4 exists to keep apart.
- AC6 — `python tools/drift-audit/selftest.py` — exit 0 with eight new checks present: the five arms,
  their two control halves, and the byte-compare. Every arm observed RED against the mechanism it
  guards, by staging each pre-change form in turn and confirming which arms flipped.
- AC7 — `bash tools/run-gates/run-gates.sh` — the full bar, which binds at the close rather than per unit and is
  recorded there for all four units. The diff-scoped gates were green at this unit's own commit:
  memory hygiene, spec tokens, codebase-map coverage, drift-audit records, kit versions and the
  deployer selfcheck.
- AC8 — `python tools/drift-audit/selftest.py` — emptying the narrowed declaration in a scratch tree
  makes the signal report itself DEAD rather than a clean zero. Observed RED against the old liveness
  half, which counts specs and is computed before any glob is read, so it stayed True at full size
  while the value fell to zero.
- AC9 — `python tools/drift-audit/selftest.py` — a scratch fixture declaring a family this repo does
  not declare has its ids classified. Observed RED against a hardcoded family list. **The first break
  written for this criterion did NOT flip it**, and that is recorded rather than quietly replaced: it
  reverted the accessor to the extractor's module constants, and the fixture has no recall kit beside
  it, so that branch is never taken there. The arm guards the family enum being READ, not the import.
- AC10 — `tools/drift-audit/drift_signals.template.py` — the seed template carries the narrowed-glob
  row empty with its documentation block, and the reader takes it with getattr-and-fallback, so a
  project layer declaring neither name still runs. Because an empty row falls back to the unnarrowed
  behaviour, the kit descriptor now declares it a hole with a discharge probe, which is the fold the
  round-2 audit asked for and the thing that keeps the README's claim honest.

## The gap this ledger will not paper over

The accessor's IMPORT branch is unreachable from the self-test: its fixture installs drift-audit
alone, so the sibling kit is absent and the local fallback answers every time. Only the byte-compare
arm touches the import, and only because that arm runs in this repo rather than in a fixture.
Measured, not inferred — breaking the import flipped nothing. Closing it means a fixture that
installs two kits, which is larger than this unit, so §5 records it and this ledger names it.
