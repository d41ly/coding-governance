**Serves:** research TOOL-dGroundRules-34

# Fold and size brief — TOOL-dGroundRules-34's wrapped span, and room under the spec ceiling

## The prompt

> `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-34.md` still wraps a §6 code span across lines 464-465 (AC8), which hygiene check 23 tokenizes one line at a time, and it measures 49136 bytes, 16 under the 49152-byte ceiling the spec-tokens `[size]` arm grades; its generated records region grows at the pass commit and would push it over.

## The brief

### Goal
Rejoin AC8's wrapped code span onto one line and bring the spec to at most 48600 bytes measured with `wc -c`, after its rev bump and §9 line. Author only: no product code, no commit, no gate.

### Items
1. In §6, move the line break before the span's opening backtick or after its closing one; never split a span, change a token's bytes, or reword a criterion. Re-scan §6 for any other line with an odd backtick count outside a fence and fix it the same way.
2. Shorten prose outside §6 without moving meaning: drop repetition between §1, §2 and §4, and compress each resolved §8 fork to its decision and reason.
3. Never touch the H1, the status header's fields other than the rev, any `**Carries:**`/`**Derived:**` line, an acceptance criterion's command, the §8 RESOLVED marks, or the generated records region between its markers.
4. The status header's rev rises by one, with one §9 line: a criterion code span rejoined onto one line and prose shortened under the spec ceiling; no design change.

### Acceptance
`wc -c` on the spec prints at most 48600; every §6 line outside a fence carries an even number of backticks; `python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it).

### Gates
No gate runs in this pass.

### Non-goals
Any other spec; product code; the status cell, which stays `DEFERRED`.

### Limitations
None beyond the items.

### Reuse
`memory/builds/dGroundRules/prompts/2026-10-24-prompt-TOOL-dGroundRules-3-span-fold-brief.md` for the fold; TOOL-dGroundRules-21 rev-7 for the trim.
