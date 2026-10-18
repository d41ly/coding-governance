# Brief — aScoutedSeam: close fork F3 in TOOL-aScoutedSeam-1 as not adopted

**Serves:** research TOOL-aScoutedSeam-1

## The prompt

> yes, close F3 and fold it into the spec. Then show me where does this experiment stand.

## The brief

### Goal
Revise TOOL-aScoutedSeam-1 so fork F3 (draft the code and expand every cited file) is closed as NOT adopted. The revision cites the M1d trial that decided it, and keeps the precision measures the trial supported. Spec only: no product code, no commit.

### Items
1. §8 F3: close it. Record the owner's ruling (2026-10-18): not adopted. Cite `memory/builds/aScoutedSeam/build/2026-10-18-build-TOOL-aScoutedSeam-1-9-m1d-trial.md`. The draft, the cited-file definition listing and the owner grep were run on the six missed positives and the six calibration cases. They found none of the six misses, and recall matched M1c (4 of 10 solved, 8 of 28 items on the same 12 cases). Reach did not become discovery. Leave F3 in §8 with its resolution; do not delete the fork's history.
2. §3 non-goals: the item naming the draft-and-expand shape as a fork becomes a rejected non-goal: the scout does not draft code, list cited files' definitions or grep literal owners, as measured by the M1d trial.
3. §4 alternatives rejected: add the M1d shape, with the figures from item 1. Add that the misses that need code to read are left to the diff-time mode, `TOOL-aScoutedSeam-3`, which found the pooled-wall and keyed-decisions seams in the benchmark.
4. §1 or §5: cite the M1d trial as the fourth measurement. The cap of five MUSTs, the `edits` list and the MUST definition naming the duplicate are what it supports. At equal recall it bound 56 MUSTs against M1c's 80 and 76, and no decoy against 2 and 1. Note its confound in one sentence: it ran as typed role agents, M1c as plain Workflow agents.
5. Nothing else in scope moves. S1 to S10, the criteria and the gate line stay as they are, except where a sentence names F3 as open.
6. §9: one revision line naming every section, scope item and criterion moved.

### Acceptance
TOOL-aScoutedSeam-1 carries the new §9 revision line, and §8 F3 reads as closed with the owner's ruling and the trial's figures. `python tools/check-spec-tokens.py`, `python tools/memory-tree/gen_build_index.py --check` and `--check-format` pass after the main loop re-renders the indexes. The spec stays under its 49152-byte ceiling: it is 48745 bytes today, so the fold must cut at least as much as it adds.

### Gates
memory hygiene · spec tokens (a spec's own names resolve) · build README slot contract

### Non-goals
- No product code and nothing under `tools/`, `skills/` or `.claude/`.
- No other unit's spec is edited.
- No change to unit ids, order or titles.
- No commit, which is the main loop's.

### Limitations
The spec is 407 bytes under its size ceiling. Any text the fold adds must be paid for by cutting text that no longer binds, such as F3's now-moot shape description, which item 1 replaces with its resolution.

### Reuse
The M1d trial record and the offline reading `2026-10-13-build-TOOL-aScoutedSeam-1-8-precision-and-misses.md` carry every figure; the spec cites them rather than restating their tables.

## Owner confirmation

Asked: Decision needed: close fork F3 in TOOL-1 as "not adopted"?
Answer: yes, close F3 and fold it into the spec. Then show me where does this experiment stand.
