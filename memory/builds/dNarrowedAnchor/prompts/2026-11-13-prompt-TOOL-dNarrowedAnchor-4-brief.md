# Brief — dNarrowedAnchor: the drift baseline drops the unit that closed

**Serves:** research TOOL-dNarrowedAnchor-4

## The prompt

> Should I spec and build the one-line baseline unit?

> Yes, run it

## The brief

### Goal
Delete `TOOL-dNarrowedAnchor-1` from `BASELINES['non_terminal_specs_cited_by_product_source']` in
`tools/drift-audit/drift_signals.py`. The unit went CLOSED at `6675df24a`, so it is no longer an
offender, and the shrink-only set reds the `drift-audit records` leg with a `stale` line until the
entry goes.

### Items
1. S1: the list at `tools/drift-audit/drift_signals.py@be2a1df7:409` keeps `TOOL-aBatchedLintel-1` and loses
   `TOOL-dNarrowedAnchor-1`. The comment block above it stays true; amend it only if it names the
   deleted id.
2. Tier-1 micro-spec, authored into
   `memory/builds/dNarrowedAnchor/spec/2026-11-13-spec-TOOL-dNarrowedAnchor-4.md`, the skeleton
   `gen_build_index.py --new-spec` wrote. Author only: no product code.

### Acceptance
`python tools/drift-audit/drift_report.py --check` prints no `stale TOOL-dNarrowedAnchor-1` line for
`non_terminal_specs_cited_by_product_source`. The leg stays red overall at this base because of
`new TOOL-aNimbleMend-15`, inherited from `main` at `2ba17e9d6` and out of scope here.

### Gates
`drift-audit records` · `memory hygiene`.

### Non-goals
`TOOL-aNimbleMend-15`'s offence, which belongs to node a's live aNimbleMend build. Any other baseline
list. Any change to `drift_report.py`.

### Limitations
The drift leg cannot go green on this branch while `TOOL-aNimbleMend-15` stands, so AC1 observes the
absence of this unit's `stale` line, not a green leg.

### Reuse
None needed. The edit is a deletion from a list that already exists. The shrink-only remedy text in
`drift_report.py` names exactly this action: "delete its line from BASELINES".

## Drawn from the session

> stale TOOL-dNarrowedAnchor-1 — listed but no longer an offender: delete its line from BASELINES['non_terminal_specs_cited_by_product_source']
— agent, the drift-audit records run after the close-out

## Owner confirmation

Asked: Should I spec and build the one-line baseline unit?
Answer: Yes, run it

## route
- build: dNarrowedAnchor
- unit: TOOL-dNarrowedAnchor-4 · spec memory/builds/dNarrowedAnchor/spec/2026-11-13-spec-TOOL-dNarrowedAnchor-4.md
- brief: memory/builds/dNarrowedAnchor/prompts/2026-11-13-prompt-TOOL-dNarrowedAnchor-4-brief.md
