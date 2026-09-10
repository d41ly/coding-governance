**Serves:** journal TOOL-aGradedDialect-3

# Build brief — TOOL-aGradedDialect-3, the reader

Your spec is `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-3.md`, at rev-3
and through three audit rounds. Build what it says. Where you would diverge, change the spec first
with a rev bump and a §9 line, then code.

**This is the unit the whole build exists for.** Everything before it decided what to build and
froze the evidence that will grade it; everything after it declares and documents what you produce.

## What is already on disk for you

- `tools/lexicon/ts-conformance-fixtures.json` — 115 records drawn mechanically from
  `C:/projects/incms/main` at `9457e65a2`, each carrying `typescript@5.9.3`'s reading of the
  committed bytes. 122 function and 20 type definitions across 115 distinct source files. It was
  frozen at `72979248`, BEFORE any reader existed, and `git log -S'scan_ts_tokens' --
  tools/lexicon/lexicon.py` returns empty today, which is the property `TOOL-aGradedDialect-2` AC3
  exists to prove. **Your first commit touching the reader is what makes that proof observable** —
  do not squash it into anything, and do not edit the corpus.
- `tools/lexicon/selftest.py` — the loader `read_ts_fixtures`, the scorer `check_ts_reading`, the
  floor constants `TS_FIXTURE_MINIMA`, `TS_CORPUS_BAND` and `TS_FLOOR_REFUSAL_SHARE`, and 20 arms.
  The conformance arm currently prints a SKIP naming the missing extractor. Removing that skip is
  your acceptance, and the arm already handles a PARTLY armed declaration — `ts` armed without
  `tsx` is legal, since those are separate `KNOWN_EXTS` rows owned by `TOOL-aGradedDialect-4`.
- `tools/lexicon/lexicon.py:parse_shell_defs` — READ ITS HEADER FIRST. It is the ratified precedent
  this unit ports, and the thing to copy is the header's enumeration of what it REFUSES, not just
  the tokenizer loop beneath it.

## The four things that decide whether this unit is honest

- **`parser` is EARNED.** S5 and AC6: you print the mode beside the measured number that decided it.
  At or above unit 2's floor you may write `parser`; below it you write `probe` and the run reports
  incomplete every time. Both outcomes pass this unit. A `parser` label over a probe-grade reading
  is the one outcome that fails it, and it is the defect the whole build was framed around.
- **A file you cannot tokenize RAISES**, naming the construct and the line. Never a partial list and
  never an empty one — `_python_defs` raises on a `SyntaxError` for exactly this reason, and its
  header says why: returning `[]` launders a broken corpus into a clean run.
- **The armedness predicate lives at FOUR sites, not two.** §8 F1 names them: two dispatch sites
  (`extract_text`'s `probe` branch, `scan_corpus`'s refusal) and two REPORTING sites (the coverage
  fraction walk, the armed-extension tally). All four call ONE derived helper. AC7 asserts the
  printed `coverage — armed` line counts the fixture's `.ts` files, which is what catches the
  reporting half diverging from the dispatch half.
- **S8 and AC9 — the `DEAD SNIFFER` trap.** Six of your locator's definition forms do not match the
  shipped `DEFINITION_SNIFF`, so a types-only module lands in `blind` and REDS the run. Widen the
  sniffer. AC9's arm asserts a POSITIVE first — non-zero graded populations for both extensions —
  because an empty `blind` set over an unarmed fixture proves nothing.

## Bounds

- Do not add `ts`/`tsx` rows to `KNOWN_EXTS`, `LANGS` or the cell matrix. Those are
  `TOOL-aGradedDialect-4`'s, and its AC1 reads `KNOWN_EXTS` as the operand.
- Do not bump the kit version. `TOOL-aGradedDialect-5` S6 owns it; S7 here says so.
- Do not edit `tools/lexicon/ts-conformance-fixtures.json`. If a record looks wrong, that is a
  finding for the closing review, not a fixture to adjust — adjusting an expectation to make a
  reader pass is the exact defect its §4 says nothing enforces.
- `lexicon selftest` is a HELD leg. Verify with `python tools/lexicon/selftest.py` directly.
- Your declared write set is `tools/lexicon/lexicon.py`, `tools/lexicon/selftest.py`,
  `.lexicon.conf`, `.claude/skills/lexicon/SKILL.md`, your own spec, and your acceptance ledger at
  `memory/builds/aGradedDialect/build/2026-09-10-build-TOOL-aGradedDialect-3-acceptance.md`.
  Widen it through `--dispatch` BEFORE the commit if you need more.
- `.lexicon.conf` pins move only as RE-MEASURED values, never raised to absorb a new name. Your own
  new function names are graded by `lexicon naming predicates` like everything else.
