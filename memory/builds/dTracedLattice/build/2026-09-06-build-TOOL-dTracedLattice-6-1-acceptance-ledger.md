# TOOL-dTracedLattice-6 — acceptance ledger

**Serves:** journal TOOL-dTracedLattice-6

The unit is a rescue, so the interesting evidence is negative: what the rescued copy does NOT do
differently. AC1's arm is a live parity comparison against the original for as long as both exist,
which is the strongest form available and expires by design when `TOOL-aSurfacedLexicon-2` lands.

**Evidences:** TOOL-dTracedLattice-6
- AC1 — `python3 tools/codebase-map/selftest.py` — the arm `map_imports: same candidates as the kit it was rescued from (AC1)` loads the lexicon kit's copy by path and asserts an identical candidate list for twelve `(target, importer)` pairs plus an identical module index. Observed RED by dropping the language branch in the rescued copy: `'lodash.debounce' from 'web/consumer/a.js': rescued ['lodash/debounce'] vs original ['lodash.debounce']`. It raises `Skipped` with a named reason once the original is gone, rather than passing on an absent comparison
- AC2 — `python3 tools/codebase-map/selftest.py` — the arm `map_imports: the rescued resolver's case table` asserts `resolve_import("lodash.debounce", "web/consumer/a.js", idx) == ["lodash.debounce"]`, so the importer's extension decides and the JS specifier is one name rather than a dotted module path. Observed RED by the same staged break
- AC3 — `python tools/lexicon/selftest.py` and `python tools/lexicon/lexicon.py` — both green at this commit with `.lexicon.conf`'s `LAYERS` rule `tools/lexicon/* -> tools/codebase-map/*` byte-unchanged and P3 still armed. The rule keeps refusing what it refused: nothing was removed from the lexicon kit, so the direction it forbids and the third-file case it permits are both exactly as before. This unit's own diff touches no file under `tools/lexicon/`
- AC4 — `memory/builds/aSurfacedLexicon/spec/2026-09-04-spec-aSurfacedLexicon-2.md` at rev-2 — S1's deletion list gains the pointer naming `tools/codebase-map/map_imports.py` as where four of the eight functions went, that `ext_of` is not on the list and stays, and that the arms travelled too; the §9 line logs it. A reader of the deletion is told the capability moved rather than died
- AC5 — `tools/codebase-map/map_imports.py` header — states the CANDIDATE-SET contract (an empty return is external or unresolvable, never an error), the branch on the IMPORTER's extension, and within Python that a dotted target gets no directory precedence, a leading dot is relative-to-package, and a bare name PREFERS the importer's directory but falls back to every stem hit. It states what the module is not — import statements only, no call sites, no receivers, no counting — and routes the 554/9112 attribute-site figures to the research prototype that produced them instead of claiming them
- AC6 — `python tools/lexicon/selftest.py` · `python tools/lexicon/lexicon.py` — the two legs `TOOL-aSurfacedLexicon-2` would break are green at the commit this unit lands, which is what proves the three live callers at `lexicon.py:527`/`:536`/`:595` still reach a resolver. Both are held on a plain bar (`lexicon selftest` is `subject: kit`), so they were run directly rather than through one
- AC7 — `python3 tools/codebase-map/selftest.py` — the arm `map_imports: no sibling-kit import (AC7)` scans the rescued module's own source and refuses any `import`/`from` line naming a sibling kit. Observed RED with a function-local `import lexicon`: `map_imports.py:96 imports a sibling kit`. A module-level break was tried first and crashes the suite at import instead of reporting, which is why the staged break is function-local

## The negative rows are not vacuous, proven

`gotchas.py` selected `fixture-passes-by-finding-nothing` over this diff, and three of the case
table's rows are negatives — a same-stem file of another extension resolving to nothing, a
repo-escaping relative specifier resolving to nothing, and a boundary case that must not land on
`thingamajig/thing.js`. A negative row passes on an empty corpus, so each was proven able to FAIL by
a staged break rather than argued about:

- extension scoping removed from the bare-name branch (`hits` unfiltered) — RED with
  `['src/pkg/shared_core/notes.md']`, so `notes.md` is really in the fixture and really excluded by
  the code rather than by absence.
- the repo-escape return replaced with a clamp (`continue` instead of `return []`) — RED with
  `['outside/thing.js']`, so the escape row is deciding on behaviour, not on an empty corpus.

Both restored, all three arms green after.

## What this ledger does not evidence

The `dead-path carriers` and `install-prefix` legs were not run in isolation for this unit; they are
on the push-boundary bar and are named here so a green ledger is not read as a full bar. The rescued
module ships to adopters by `tools/codebase-map/kit.toml`'s `include = "**"` engine rule, which is
correct — it carries no corpus dependency — and no `[[files]]` claim was added for it.
