# TOOL-dTracedLattice-5 — acceptance ledger

**Serves:** journal TOOL-dTracedLattice-5

**Evidences:** TOOL-dTracedLattice-5
- AC1 — `python3 tools/codebase-map/selftest.py` — the arm `dark layers: an undeclared layer refuses with both remedies (AC1)` asserts the refusal carries the layer, its file count and BOTH clearing paths, and that it goes quiet once the layer is declared, so the remedy it prints is one that works. Observed RED with the remedy half replaced by "Fix it." Also observed live on this tree with an emptied declaration: `.sh (85 file(s))`, exit 2 — a figure taken before the closing review widened the population, which now reports 94; the count is derived on every run and this ledger quotes the reading it was written from
- AC2 — `python3 tools/codebase-map/selftest.py` — the arm `dark layers: the banner is derived, not declared (AC2/AC4)` renders with `.sh` declared and asserts the banner names it dark
- AC3 — `python3 tools/codebase-map/selftest.py` — the arm `dark layers: a stale declaration is reported (AC3)` asserts a declared-but-absent `.rb` lands in `stale` and NOT in `undeclared`, and that stale is a REPORT rather than a refusal: it costs an adopter nothing and blocks nothing
- AC4 — `python tools/codebase-map/reuse_lookup.py "resolve a path"` — `# scan coverage: 61 files scanned | 0 parse skips | unscanned layers: .sh`, derived from the corpus walk. The arm proves the derivation cannot be overridden: with `.nonexistent` declared, the banner still says `.sh` and never mentions the declared value
- AC5 — `python3 tools/codebase-map/selftest.py` — the arm `dark layers: every declared layer is present here (AC5)` reads THIS repo's conf and asserts every token is an extension present in the corpus. It reddened against the shipped `bash` value before the migration landed, which is the observation the criterion asks for: `RECALL_DARK_LAYERS carries the OLD language-name spelling bash … the uncovered layers present in this corpus are: .sh`
- AC6 — `python3 tools/codebase-map/selftest.py` — the arm `dark layers: the legacy spelling refuses (AC6)` asserts the old spelling REFUSES and names the extensions it could be, and that a conf carrying both an old and a new value is still a migration. Observed live before the conf was migrated
- S1 — `map_lib.derive_present_layers` — the present-layer population is the TRACKED FILE LIST (`git ls-files`), which is bounded by construction and is the same set every other check in this kit grades. It went through two wrong populations first and both are recorded in the review reports: a tally inside the reference walk, which is scoped to the SYMBOL corpus's top-level dirs and so could not see a layer anywhere else; then a bare walk from the repo root, which on a primary tree counted sixteen sibling worktrees under `.claude/` as this repository. It reads no file either way. The line this ledger carried until the closing review said the tally rode the existing walk and cost no second scan, and that is no longer true
- S2 — `map_lib.DEFINITION_CARRYING_EXTS` — derived from `_LEX_PROFILES` minus an authored data-format set, so the language half needs no maintenance and only the data exclusion is a judgement
- S6 — `.codebase-map.conf` is `.sh`, `.codebase-map.conf.example` states the extension vocabulary and tells an adopter to let the refusal name their layers rather than authoring from memory, and the kit's own selftest fixture moved from `web-ts` to `.ts`

## The arm caught a second reader, which is this unit's own defect one level down

The coverage line was derived and the `recall partial:` paragraph was not, for exactly one commit.
The AC2/AC4 arm's second half — declare `.nonexistent` and assert the output is unmoved — failed on
the paragraph while the line was already correct. Both now read one `_derive_dark`, and the fallback
to the declared tuple survives only for the case where no scan ran at all.

## The one thing this cannot see, and it is a false negative by choice

`DEFINITION_CARRYING_EXTS` is derived from the tokenizer's profile table, so a language that table
has no profile for is invisible: a `.rb` corpus would be neither covered nor reported dark. That is
chosen over the false positive of calling every unknown extension a source layer, and it is stated
in the constant's own header rather than left for a reader to discover.

`map_lib`'s data-format exclusion is a SECOND COPY of a judgement the lexicon kit also makes and
argues at greater length. It cannot be imported — this repo relies on a directional layer rule
forbidding that kit from importing this one, and the reverse direction is no better — so the two are
independent readings of one question and may diverge. Said in the code rather than discovered later.
