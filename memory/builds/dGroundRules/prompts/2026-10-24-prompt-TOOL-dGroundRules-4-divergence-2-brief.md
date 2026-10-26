**Serves:** research TOOL-dGroundRules-4

# Divergence brief 2 — TOOL-dGroundRules-4, v2's id out of the `policy fixtures` argv

## The prompt

> Its builder handed TOOL-dGroundRules-4 back a second time as a DIVERGENCE: S8, AC10 and §8 F7 put v2's path, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`, into the argv of the `policy fixtures` row in `tools/gate-legs.json`. That file is product source to drift-audit, the path spells the INPROGRESS id `PLAY-dClosedLoop-1`, and the held signal `non_terminal_specs_cited_by_product_source` (BASELINES in `tools/drift-audit/drift_signals.py`) may never gain an id against the base, so `drift-audit records` reds at the close with no fix but removing the citation.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-4.md` to the run's ruling (a): the `policy fixtures` argv carries `--strict-from memory/builds/dClosedLoop/build/`, a directory that spells no id, and the strict case reads the one file there whose name ends `-architecture-v2.md`, red when it finds none or more than one. Author only: no product code, no commit, no gate.

### Items
1. S8, AC10 and §8 F7 state the directory argv and the one-file rule; AC10's probe shows the `policy fixtures` argv carrying `--strict-from` and the directory, and no id-bearing path anywhere in `tools/gate-legs.json`.
2. AC9 keeps its observation (strict's cells read from `last-valid`) with `--strict-from` given the directory; it gains a red-when for a directory holding no `*-architecture-v2.md` file or two of them.
3. Verify with `ls memory/builds/dClosedLoop/build/*-architecture-v2.md` that exactly one file matches at HEAD, and say so in §4 Evidence.
4. The status header's rev rises by one, with a §9 line naming what disagreed and the ruling.

### Acceptance
`python tools/check-spec-tokens.py` exits 0; no backticked token in S8, AC9, AC10 or F7 puts an id-bearing path into a file under `tools/`; every `**Carries:**` line, the H1 and the §8 RESOLVED marks survive; every §6 code span sits on one line.

### Gates
No gate runs in this pass; the close runs the spec's §7 legs.

### Non-goals
Any other spec; product code; the spec's status cell, which stays `DEFERRED`; a change to drift-audit or its baselines.

### Limitations
Ruling (b), a pointer file under `memory/project/`, was set aside: that folder holds only the gates' row registries (AGENTS.md section 2).

### Reuse
The builder's saved work is in the session scratchpad as `TOOL-dGroundRules-4-divergence.patch` and `TOOL-dGroundRules-4-ledger.draft.md`; the next builder applies it and changes only the argv and the strict case's file lookup.
