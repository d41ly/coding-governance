**Serves:** research TOOL-dGroundRules-52 TOOL-dGroundRules-45 TOOL-dGroundRules-60 TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-57 TOOL-dGroundRules-58

# Edge-repair brief — the §3 edges the step 15-20 revisions and retirements left unmatched

## The prompt

> Memory hygiene check 12, run over the tree at 97194a758, reports ten §3 edges with no matching edge back, all left by the revisions and WONTDO retirements of steps 15 to 20.

## The brief

### Goal
Make every §3 edge between these specs reciprocal, editing only the §3 Edges lines and the revision log of `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-52.md`, `-45.md`, `-60.md`, `-53.md`, `-54.md`, `-57.md` and `-58.md`. Author only: no product code, no commit, no gate beyond memory hygiene.

### Items
1. TOOL-dGroundRules-52 adds a consumes-from edge on TOOL-dGroundRules-32 naming `check_writes_intersect` (its S21, closed by the arm TOOL-dGroundRules-32 built and TOOL-dGroundRules-40 re-tabled), matching -32's hands-off line; and drops its consumes-from edge on TOOL-dGroundRules-25, which is CLOSED and declares no hands-off back; S4 keeps naming `derive_parallel_step` in prose.
2. TOOL-dGroundRules-45 drops its hands-off edge to TOOL-dGroundRules-52 (52 rev-5 no longer consumes `PAIRS_TABLE`) and adds a hands-off edge to TOOL-dGroundRules-60 naming `PAIRS_TABLE`, matching -60's consumes-from line.
3. TOOL-dGroundRules-60 drops its consumes-from edge on TOOL-dGroundRules-40, which is CLOSED and declares no hands-off back; the trap row stays named in its §4 prose.
4. TOOL-dGroundRules-53, -54, -57 and -58 are WONTDO (8eab342e0): withdraw each of their §3 edges, leaving the Edges section reading `none — retired WONTDO, superseded`; the status cell stays `WONTDO`.
5. Each edited spec's rev rises by one with a revision-log line (§9 in a Tier-2 spec, §8 in a Tier-1 one) naming the edge change; no other line moves.

### Acceptance
`bash tools/memory-tree/check-memory-hygiene.sh` reports no check 12 line naming any of these seven specs; `python tools/check-spec-tokens.py` exits 0 with the live specs read as INPROGRESS (the main loop runs it).

### Gates
Memory hygiene only.

### Non-goals
Any other line of these specs; any other spec; product code; status cells.

### Limitations
TOOL-dGroundRules-44 is building while this runs and does not touch these specs.

### Reuse
The check 12 edge join in `tools/memory-tree/check-memory-hygiene.sh`.
