**Serves:** journal TOOL-dTotalRecall-2

# Brief — dTotalRecall: TOOL-dTotalRecall-2's carried clause token rejoined onto one line

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. The spec-token checker's carries join reds: clause
cl-dClosedLoop-0213's token `minted under the session rule: no claim or lease for <slug>` appears in none of its
carriers, because the rev-10 re-ground wrapped it across two lines of spec 2's §4.

## The brief

### Goal

Revise `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-2.md` in place as a rev-11 bump, with one
revision-log line naming this brief by its file stem, so the clause token stands whole on one line.

### Items

1. Rewrap the paragraph that holds `minted under the session rule: no claim or lease for <slug>` so the whole
   backticked token sits on one line, byte for byte as the clause carries it. Change no other word.
2. The status header keeps `DEFERRED`; the `**Carries:**` line stays byte-identical.

Before returning, run `python tools/check-spec-tokens.py` (whole tree; its carries join must name no dTotalRecall
carrier), `python tools/check-spec-tokens.py --spec <path>` and `bash tools/unattended/unattended.sh --check-specs
dTotalRecall TOOL-dTotalRecall-2`, and fix every finding they name in this spec. The write grant is the spec file
alone; do not commit.

### Acceptance

The carries join names no dTotalRecall spec; the other two commands exit 0.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other change to spec 2; no other spec.
