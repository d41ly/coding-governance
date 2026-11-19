# Spec brief — dLandedOwners: TOOL-dLandedOwners-6, the two legs the close's bar read red

**Serves:** research TOOL-dLandedOwners-6

## The prompt

> Fix the Ask 5, remove the ask TOOL-dTrackedAtlas-19

The owner's go for this build, of 2026-11-19. The merge bar at the build's tip `fcbd7efe2` read two legs red, each
caused by this build's own units; units 1 and 3 are CLOSED and their specs frozen, so the fix is a new unit on top.

## The brief

### Goal
Spec one unit, `TOOL-dLandedOwners-6`, that turns both reds green by removing their cause, each red observed first on
the real tree and green after.

### Items
1. The `python reads` leg prints `RED guard · policy fixtures · tools/memory-tree/commit_trailers.py is imported and
   outside its guard`. Unit 1 made `tools/policy/check_policy.py` import `gen_build_index`, whose static import closure
   reaches `routed_commits` and through it `tools/memory-tree/commit_trailers.py`, a path the `policy fixtures` leg's
   `guard` list in `tools/gate-legs.json` does not name. `python tools/run-gates/py_reads.py --guards "policy fixtures"`
   prints the closure and the red. Decide by the build method's M3 whether the guard gains the path or the closure
   loses it, and say why.
2. The `drift-audit records` leg (`python tools/drift-audit/drift_report.py --check`) reads
   `non_terminal_specs_cited_by_product_source` over its baseline: a new offender `PLAY-dClosedLoop-1`, an offender
   the shrink-only set says to remove the cause of and never list. Unit 3's row in `tools/policy/unscanned-readers.txt`
   names the dClosedLoop instrument's path, which carries that id in its file name; the row declares where a key is
   read, and claims no spec's work shipped. `tools/drift-audit/drift_signals.py#EVIDENCE_GLOBS` already excludes the
   size registries for the same reason. Decide by M3 how the cause goes (an exclusion with its reason beside it, or
   another route) and say why.
3. Files touched names the acceptance ledger
   `memory/builds/dLandedOwners/build/2026-11-19-build-TOOL-dLandedOwners-6-ledger.md`, the hook-rendered records,
   and section 7 every leg `check-spec-tokens.py --legs-for -` says each touched path trips.
4. Every figure before a unit word carries a pin on its line, outside a code span; every citation is
   `<repository path>#<symbol>` or blob-pinned.
5. Header: Tier-2, order 5, base at HEAD.

### Acceptance
Each item has an AC naming a direct observation with no gate, suite or bar: the guard check and the drift report's
`--check`, each red at the spec's base and green after. `python tools/check-spec-tokens.py --spec <path>` and
`check-memory-hygiene.sh --only 12 --spec <path>` are clean; `unattended.sh --plan dLandedOwners --paths` grades the
unit READY.

### Gates
The spec-format, spec-token and naming-lexicon checks the role allows; no other gate.

### Non-goals
Any change to units 1 to 4's mechanisms; any other drift signal or baseline; the flagged bar.
