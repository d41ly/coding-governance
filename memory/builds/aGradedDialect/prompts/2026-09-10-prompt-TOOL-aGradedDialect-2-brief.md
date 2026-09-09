**Serves:** journal TOOL-aGradedDialect-2

# Build brief — TOOL-aGradedDialect-2, the conformance corpus

Your spec is `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-2.md`, at rev-4
and CLEAN through three audit rounds. Build what it says. Where you would diverge, change the spec
first with a rev bump and a §9 line, then code.

## What you are handed that the spec assumes

**The oracle exists and has been run.** `typescript@5.9.3` is installed in the adopter tree at
`C:/projects/incms/main/node_modules/typescript`. The extraction script is reproduced runnable in
`memory/builds/aGradedDialect/build/2026-09-10-build-TOOL-aGradedDialect-1-typescript-extraction-research.md`
§6, together with the invocation. `require` resolves relative to the SCRIPT, not the cwd, so pass the
module path explicitly — the research record's snippet already reads `process.env.TS_MODULE` for
exactly this reason, and rediscovering it costs a confusing `Cannot find module` failure.

**The adopter tree is READ-ONLY and is not this repository.** 6550 tracked files, 656 `.ts`, 601
`.tsx`. Write nothing there, and do not `git add` anything in it.

## The three things this unit gets wrong if you are not careful

- **The freeze ORDER is the whole point, and it is the answer to a ratified objection.** The corpus
  is committed in a pass that precedes the first commit touching the reader. `TOOL-aGradedDialect-3`
  has not been built, so this is free — but it means you commit the corpus and STOP, rather than
  reaching ahead to make the conformance arm pass. §4's proof block and AC3 are how a later reader
  checks you did. Note AC3's two traps: the extractor half is a `-S` pickaxe over `lexicon.py`,
  not a `--diff-filter=A` over a file that unit does not create, and the two shas must DIFFER,
  because `--is-ancestor` is reflexive and would pass a single commit carrying both.
- **The corpus must CONTAIN the hard readings or it grades nothing.** §4's minima are not decoration;
  they are the `fixture-passes-by-finding-nothing` class answered. Template literals with nested
  `${}`, JSX, generics and regex literals appear in 90.3%, 72.2%, 56.6% and 24.9% of the adopter's
  files respectively, and the corpus is selected to carry them in proportion rather than to be easy.
- **`selftest.py` is a HELD leg.** `lexicon selftest` is `subject = kit`, `chunk = selftests`, so an
  ordinary `bash tools/run-gates/run-gates.sh` does NOT run your arms. Verify with
  `python tools/lexicon/selftest.py` directly, or `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`.
  A green ordinary bar is not evidence about anything you wrote.

## Bounds

- Do not build the extractor. It is `TOOL-aGradedDialect-3`'s and building it here destroys the
  ordering property above.
- Do not touch `KNOWN_EXTS`, `LANGS` or the cell matrix. Those are `TOOL-aGradedDialect-4`'s.
- Your declared write set is exactly: `tools/lexicon/ts-conformance-fixtures.json`,
  `tools/lexicon/selftest.py`, `tools/lexicon/kit.toml`, `.gitattributes`, your own spec, and your
  acceptance ledger at
  `memory/builds/aGradedDialect/build/2026-09-10-build-TOOL-aGradedDialect-2-acceptance.md`.
  Anything else needs a re-declaration through `--dispatch` with the WIDER set before you commit.
- The acceptance ledger carries `**Serves:** journal TOOL-aGradedDialect-2` and an `**Evidences:**`
  block, one line per criterion AC1 to AC6, each sharing a backticked token with the criterion it
  answers. The grammar is `memory/HYGIENE.md`, "Acceptance ledger".
