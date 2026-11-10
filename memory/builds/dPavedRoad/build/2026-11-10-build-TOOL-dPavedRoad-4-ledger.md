**Serves:** journal TOOL-dPavedRoad-4

# TOOL-dPavedRoad-4 — acceptance ledger

The unit as built, at spec rev-1. Under `--staged`, `tools/memory-tree/check-memory-hygiene.sh` tags
`J` every unstaged spec in a staged spec's build folder; the batched awk reads a `J` spec through
`extract_edges` for its E and U records only, each record's new last field saying whether its spec
is staged; the edge-join awk reports a reciprocity or order finding when either end is staged and a
payload finding when its own file is. Check 23 runs under `--staged`: both listings keep only the
`_SBUILD` folders, and the `alsel` awk keeps a unit whose spec is staged (`sfiles`) or whose id a
staged record's `**Evidences:**` line names (`only`). Both hold lines became announce lines, the
script header no longer lists check 23 as held, and the four prose copies carry the spec's
section 4 text. The suite gains the section 4 fixture block and its floor moves 670 to 685.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Every criterion below was
observed over the spec's section 4 fixture, built by a scratch script at `%TEMP%/pr4`, with this
unit's working tree; the same fixture run against the base script at `ae6735c1` failed AC1, AC2's
announce, AC3 and AC4's announce, so the probe can move.

Owed at the close: the `memory-hygiene self-test` leg's new arm (the scratch-tree block in
`tools/memory-tree/check-memory-hygiene.test.sh`, AC1 to AC4) with its RED-first observation by
restoring the two holds, and the section 7 legs: `memory hygiene`, `memory-hygiene self-test`,
`check-arms selftest`, `policy fixtures`, `kit/dogfood doc parity`, `recall floor`, `recall floor
arms`, `spec tokens (a spec's own names resolve)`.

**Evidences:** TOOL-dPavedRoad-4
- AC1 — with only `2026-11-10-spec-ARCH-tPair-2.md` staged, `bash tools/memory-tree/check-memory-hygiene.sh --staged` printed under `HYGIENE check 12` the line `memory/builds/tPair/spec/2026-11-10-spec-ARCH-tPair-1.md (§3 declares **hands-off** `ARCH-tPair-2` and that unit declares no matching **consumes-from** `ARCH-tPair-1` back)`; with only spec 1 staged it printed the same line.
- AC2 — with specs 2 and 5 staged, `bash tools/memory-tree/check-memory-hygiene.sh --staged` named no `ARCH-tPair-4` or `ARCH-tPair-5` edge, no `2026-11-10-spec-ARCH-tPair-6.md (` and no `2026-11-10-spec-ARCH-tPair-8.md (`, and printed the first announce line, `memory-hygiene: the §3 edge JOINS grade each staged spec against its own build's specs as they stand in the worktree`, and not `the §3 edge JOINS are held under --staged`.
- AC3 — with only spec 3 staged the `HYGIENE check 23` line opening `a CLOSED unit numbers an acceptance criterion that no journal record evidences` named `ARCH-tPair-3/AC2`; with only spec 9's ledger record staged the line opening `a journal record evidences a criterion label its own spec does not number` named `ARCH-tPair-9/AC9`.
- AC4 — neither run of AC3 named `ARCH-tPair-10/AC9` or `ARCH-tPair-9/AC8` or printed `check 23 HELD under --staged`, and each printed `memory-hygiene: check 23 graded 1 unit(s)` that a staged spec or journal record names.
- AC5 — with nothing staged, `bash tools/memory-tree/check-memory-hygiene.sh` in full from this unit's tree and from a `git clone --shared` checked out at `ae6735c1` in `%TEMP%/pr4b`, each repository path replaced by one token, gave a `diff` that printed nothing; both named the one-way edges of specs 1 and 6, spec 8's missing Edges block, and `ARCH-tPair-3/AC2`, `ARCH-tPair-9/AC8`, `ARCH-tPair-9/AC9` and `ARCH-tPair-10/AC9`. The clone's FIRST run differed in one line only, check 26's `cache hits 0` against `cache hits 4`, a cold cache; its second run diffed empty.
- AC6 — `grep -cF 'are JOINS and are HELD'` over `memory/TEMPLATE-SPEC.md` and `tools/memory-tree/SPEC-TEMPLATE.template.md`, and `grep -cF 'JOINS are held there'` over `memory/HYGIENE.md` and `tools/memory-tree/HYGIENE.template.md`, each printed 0; each section 4 replacement sentence counted 1 in each of the four; `grep -nF '23 and 26'` over `tools/memory-tree/check-memory-hygiene.sh` printed nothing.
