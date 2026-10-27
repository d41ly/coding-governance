**Serves:** research TOOL-dSafePassage-34

# Brief: TOOL-dSafePassage-34's pin raise keeps its pass, and its DECISIONS row moves to the close

## The prompt

No owner prompt: the build run's builder handed TOOL-dSafePassage-34 back as a DIVERGENCE (`wf_1f4d3252-2a6`, HEAD `cb2811f6c`), and the run revises the spec under M2.

## The brief

### Goal

TOOL-dSafePassage-34 builds within the write set `--dispatch` admits. Its pass arms `SPEC_AC_ORDER_CUTOFF` and raises the drift pin `cutoff_keys_armed` 36 -> 37 in place with its comment. The `memory/DECISIONS.md` row recording that raise is written by the main loop in a `Pass: none` commit at the close.

**The defect.** §3's hands-off to TOOL-dSafePassage-46, TOOL-dSafePassage-46 S1, and TOOL-dSafePassage-42 S9/F1 all put the DECISIONS row in this unit's pass commit, with `memory/DECISIONS.md` in its `--dispatch --writes`. The verb refuses that outright, at `tools/unattended/unattended.sh:14004`: check 49 says a pass may not declare a shared mutable record, and BUILD-METHOD M6 clause 3 names `memory/DECISIONS.md` as one. TOOL-dTrueNorth-28 is the precedent. Its row raising the same pin 34 -> 36 under ER:388 is at `memory/DECISIONS.md:239` and landed at dTrueNorth's close. The ruling itself stands: spec 42 F1 resolved the raise under ER:388, so the pin raise needs no new decision.

### Items

1. **Revise TOOL-dSafePassage-34**, rev bump dated 2026-10-27, still `DEFERRED`:
   - Take `memory/DECISIONS.md` out of Files touched and out of every write-set claim.
   - The pass raises the pin in `tools/drift-audit/drift_signals.py`, with its comment naming this unit and ER:388.
   - §3's TOOL-dSafePassage-46 bullet says the DECISIONS row is the main loop's, written at the close in a `Pass: none` commit in TOOL-dTrueNorth-28's form.
   - Add one §9 line naming this brief.
2. **Fix TOOL-dSafePassage-46 S1 and AC1, and TOOL-dSafePassage-42 S9, to match.** Both are DEFERRED. 46 AC1 reads "the first commit's subject names TOOL-dSafePassage-34" and a `git show --stat`; restate it so it reads the pin raise in the pass commit and the row in the close's records commit. Each gets a rev bump and a §9 line.
3. **Cross-read TOOL-dSafePassage-41**, which consumes 34, on M2's axes. TOOL-dSafePassage-8 is CLOSED, so it needs no edit.
4. **Commit nothing.** Return the files you wrote.

### Acceptance

- `grep -n 'DECISIONS.md' memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-34.md` prints no line that puts the row in this unit's pass.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.

### Gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### Non-goals

- No product code, no edit to a CLOSED spec, no change to ER:388's ruling.
- No commit and no stage into the real index.
