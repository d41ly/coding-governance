**Serves:** research TOOL-dGroundRules-25

# Size brief — TOOL-dGroundRules-25 back under the spec ceiling

## The prompt

> A sweep of this build's specs read as INPROGRESS found `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-25.md` at 49006 bytes, 146 under, the 49152-byte ceiling the spec-tokens `[size]` arm grades; its generated records region grows at the pass commit and would push it over.

## The brief

### Goal
Bring the spec to at most 48600 bytes measured with `wc -c`, after its rev bump and §9 line, so the records region can grow at the pass commit without crossing the ceiling. Author only: no product code, no commit, no gate.

### Items
1. Shorten prose without moving meaning: drop repetition between §1, §2 and §4, and compress each resolved §8 fork to its decision and reason.
2. Never touch the H1, the status header's fields other than the rev, any `**Carries:**`/`**Derived:**` line, an acceptance criterion's command, any §6 code span, the §8 RESOLVED marks, or the generated records region between its markers.
3. The status header's rev rises by one, with one §9 line: prose shortened under the spec ceiling; no design change.

### Acceptance
`wc -c` on the spec prints at most 48600; `python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); every §6 code span sits on one line.

### Gates
No gate runs in this pass.

### Non-goals
Any other spec; product code; the status cell, which stays `DEFERRED`.

### Limitations
None beyond the items.

### Reuse
TOOL-dGroundRules-21 rev-7 is the precedent.
