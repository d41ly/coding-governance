# Fix brief — TOOL-dFoldedAudit-17 at rev-4

**Serves:** research TOOL-dFoldedAudit-17

## The brief

### Goal
Revise TOOL-dFoldedAudit-17's spec to rev-4 to clear its one spec-token hit. Keep the status at INPROGRESS. Commit nothing.

### Items
1. `tools/check-spec-tokens.py` reads AC9's code span token `2>"$P/drift.err"` as a path that `git ls-files` does not track, and `--dispatch` refuses the unit on it. Spell AC9's observation so that no code-span token is path-shaped and untracked. One way is to pipe stderr straight into the count rather than through a file. The probe text in S1 and in §8's rev-3 line may name the scratch folder in prose. Any code span holding a slash-bearing scratch path is the same hit.
2. Rev-3 was committed in `f0f766def`, under a records subject, with this hit present. §8's rev-4 line says so in one clause.

### Acceptance
Rev-4 with one §8 line. AC9 keeps the same observation, and no code span in the spec holds an untracked path.

### Gates
`tools/check-spec-tokens.py`, run by the main loop after this pass.

### Non-goals
No other change to the spec, and no write outside this build's `spec/`.
