**Serves:** research TOOL-dGroundRules-86

# Spec brief — TOOL-dGroundRules-86, dSafePassage-26's Readers clause re-applied over origin's trimmed rev-5

## The prompt

The landing's `--prepare` conflicted with origin/main at `fafa12ef4`. Our side wrote dSafePassage-26 rev-5 in `8b0492fe2`: S30's Readers clause names `read_legacy_fanout`, `FANOUT_LINE`, `LEGACY_FANOUT` and `derive_lowered_limit` in `tools/policy/policy.py`, because TOOL-dGroundRules-10 (`2ebafd441`) removed `loadDeclaredCap` from `tools/hooks/agent-cap.js`. origin/main's `1e9b2dad5` wrote its own rev-5 of the same spec, trimming every section under the class cap; its S30 still names `loadDeclaredCap`, which hygiene check 25 reds. The main loop is mid-merge on the run branch and has taken origin's side of `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-26.md` whole; our rev-5 text is at `8b0492fe2`.

## The brief

### Goal
Edit that spec, as it now stands in the working tree, to rev-6: rewrite only S30's **Readers:** clause to name the code that reads `FANOUT_CAP` now, in origin's trimmed style (the same readers our `8b0492fe2` rev-5 named; confirm each by grep at HEAD), bump the header to rev-6 with today's date and the status unchanged, and add a §9 rev-6 line saying the clause was re-applied over the trimmed rev-5 and why. No other edit, no commit, no `git add`, no gate beyond memory hygiene.

### Items
1. Keep origin's trimmed text everywhere else, byte for byte.
2. Keep every line within the spec's existing width; no line anywhere starts at column 0 with `AC<n>`; an untracked path sits in a fenced block; never write a probe copy of a spec inside the spec folder.

### Acceptance
Hygiene check 25 names nothing in this spec and check 12 names nothing in it (the main loop runs memory hygiene after the merge's index is re-rendered).

### Gates
Memory hygiene only.

### Non-goals
Any other clause of this spec; any other file; resolving the merge.
