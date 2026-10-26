**Serves:** research TOOL-dGroundRules-86

# Spec brief — TOOL-dGroundRules-86 rev-2, the dSafePassage-26 Readers rev moves to a spec-writer pass

## The prompt

The builder of TOOL-dGroundRules-86 (rev-1, `f6af9123e`) returned a DIVERGENCE with nothing committed: its §2 S3 edits `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-26.md` (the Readers clause near :258-262, the header to rev-5, a §9 rev-5 line), and scratch-guard lets only gov-spec-writer write the spec class. Its other steps (S1, S2, S4, S5, S6) are saved as a patch in the run's scratchpad as `TOOL-dGroundRules-86-partial.patch`. It also found two drifted citations at HEAD `2550ccaa7`: the `check_policy.py` method-carrier sites are now :3489 and :3758, not :3488 and :3757; and TOOL-dGroundRules-85 moved the `manifest-check.sh` and `check-memory-hygiene.sh` lines this spec cites (15 and 14 lines lower).

## The brief

### Goal
Two spec edits, in this one pass, by this role:

1. Rev dSafePassage-26 to rev-5 exactly as TOOL-dGroundRules-86 rev-1 §2 S3 and §4 "The Readers clause" specify: the Readers clause and the §9 revision log only, status left as it is.
2. Rev `memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-86.md` to rev-2, status `DEFERRED`: S3 leaves the build unit and is recorded as landed by this spec-writer pass (which lands with the spec commit, before the build), §4 "Files touched" drops the dSafePassage path, §5 AC2's check-25 half is observed at the close over the tree this pass leaves, and the drifted citations are re-read at HEAD and corrected. §8 logs rev-2 and why.

No product code, no commit, no gate beyond memory hygiene.

### Items
1. Re-read every line this spec cites at HEAD and correct the drifted ones.
2. Keep S1, S2, S4, S5 and S6 as rev-1 has them unless a re-read shows they drifted; the builder's patch already holds them.
3. §7 "Open questions" reads exactly `none`, with no bullet under it; any follow-up goes in the §8 revision log as prose. No line anywhere in §5 starts at column 0 with `AC<n>` other than the bullets themselves; every AC bullet carries `Red when:`; keep every acceptance code span on one line and free of a `|` the bar pattern reads as a pipe; no retirement word in §2; an untracked path sits in a fenced block; never write a probe copy of a spec inside the spec folder.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); hygiene check 12 names nothing in this spec; hygiene check 25 no longer names dSafePassage-26.

### Gates
Memory hygiene only.

### Non-goals
Any clause of dSafePassage-26 other than the Readers clause and §9; any other spec.
