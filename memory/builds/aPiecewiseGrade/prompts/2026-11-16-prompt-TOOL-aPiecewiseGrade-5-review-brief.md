# Promotion — aPiecewiseGrade: the closing review's item 2, as TOOL-aPiecewiseGrade-5

**Serves:** research TOOL-aPiecewiseGrade-5

## The prompt

> Promote, build now (Recommended)

The owner's answer, 2026-11-16, to "Build them now or file them?", put through the session's question tool after the closing review `2026-11-16-review-TOOL-aPiecewiseGrade-1-diff-review-round1` returned CLEAN WITH FIXES with two medium items.

## The brief

### Goal
The closing review's item 2 (ids 2, 3, 5, medium): `scan_live_spec`'s 24 counter names in `tools/check-spec-tokens.py` are spelled twice, once in its return dict and once in `main`'s read-back from a `collections.Counter`, which reads a misspelled name as 0 and raises nothing; cached `counts` are not checked either, and no arm asserts a nonzero value for `skipped`, `so_bare`, `ao_graded` or `ao_bad`. TOOL-aPiecewiseGrade-5 makes the names one source and every mismatch loud.

### Items
1. Write `memory/builds/aPiecewiseGrade/spec/2026-11-16-spec-TOOL-aPiecewiseGrade-5.md`, status SPECCED, rev-1, node a, base `aebbb4a72`, streams tooling, order 5, Tier-2, in the shape `memory/TEMPLATE-SPEC.md` states. Read item 2 of `memory/builds/aPiecewiseGrade/reviews/2026-11-16-review-TOOL-aPiecewiseGrade-1-diff-review-round1.md` whole; its Fix paragraph is the design to verify against HEAD, not to copy.
2. The names live once, as a module tuple; `scan_live_spec`'s return dict is built from it; `main` sums into a plain dict seeded from it, so a misspelled read-back raises; `main` checks every `got[2]`, fresh or cached, carries exactly that key set and fails loudly otherwise; `read_spec_cache` treats any other `counts` key set as a miss.
3. One new arm per counter the suite never sees nonzero: `skipped`, `so_bare`, `ao_graded`, `ao_bad`, each expecting a nonzero value, and each seen red with that name misspelled on either side.
4. Name every new constant and function through `python tools/lexicon/lexicon.py --suggest`. State what the change owes: the codebase map, the symbols index, a `two-answers-to-one-question` checklist line if no gate covers the class.
5. Stage the spec and clear `python tools/check-spec-tokens.py --spec` over it. Do not commit. Return its path and status line, each criterion's id with one line, any fork with its recommendation, and the checker's final line.

### Acceptance
- The plain and cached runs print the same bytes as before over the real tree and the PG1 fixture.
- A misspelled counter name on either side, or a cached entry with another key set, is loud or a miss, never a silent 0.
- Each of the four counters has an arm expecting it nonzero.

### Gates
`check-spec-tokens.py --spec` over the spec.

### Non-goals
- Any edit to a CLOSED spec of this build: a correction to a closed unit is this new unit's.
- Any change to a verdict, a refusal line, the summary line or an exit status of the checker or of `--dispatch`.
- A row raised in any shrink-only registry.
- `tools/unattended/unattended.sh`, which TOOL-aPiecewiseGrade-6 writes concurrently.
- Building anything: the builder follows once the spec is committed.
