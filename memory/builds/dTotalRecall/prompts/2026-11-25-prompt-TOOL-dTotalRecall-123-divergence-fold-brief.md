**Serves:** journal TOOL-dTotalRecall-123
**Caused-by:** TOOL-dTotalRecall-123

# Brief — dTotalRecall: TOOL-dTotalRecall-123's first pass diverged on its criteria, its spec folded as rev-2

## The prompt

> redesign the record under a bound it can meet, run the replay again with more runs per arm. Why weren't those decisions made under the unattended protocol?

— owner, 2026-11-25, in this run's session on node a, answering asks TOOL-dTotalRecall-109 and TOOL-dTotalRecall-111.

## The brief

### Goal

Fold the divergence of `memory/builds/dTotalRecall/build/2026-11-25-build-TOOL-dTotalRecall-123-1-builder-return.md` into
`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-123.md` as rev-2, its revision-log line naming this
brief by its file stem, so the next pass builds it as written. The design stands; no estimator, line or count moves.

### Items

1. Read the return's Why whole and verify each of its four points and the minor one over HEAD.
2. Points 1 and 2: each criterion reads what it can read; AC4's grep leaves the `review-twin runs=` line alone, and AC5's is
   scoped to the build records and anchored to the field's own line.
3. Point 3: the departures join is the close's, with its cost named, and the pass observes the record through the cheaper
   reader the return used, `deviation_join.py#read_record`.
4. Point 4: the pass lands the scorer, its arms, the deviation record and the manifest, `candidates` empty, in one commit, and
   the header STAYS `INPROGRESS`: the runs, the verdict record and the CLOSED flip are the main loop's, at the verdict commit,
   as TOOL-dTotalRecall-17's were at `cb97caf03`. §2 S5, §4 Rollout and §6 state that, and the run count stays a figure the
   main loop may change until the first clone is made.
5. The minor point: S5 names the `map` key's value before the runs.
6. The checks: `--check-specs`, `check-spec-tokens.py --spec`, hygiene check 12 over the spec. Run no gate leg.
7. Your write grant is that spec alone. Do not commit.

### Acceptance

The commands name no finding, and each criterion can be read as stated by the pass, the main loop or the close it names.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No product code. No replay run. No scope beyond the return's points.

### Limitations

Scratch goes under `C:/Temp/claude/7a8436c9e3b87ce5/9067262b-db21-4497-8ba8-ef2deab46f53/scratchpad/u123/`.

### Reuse

The draft the return names, `u123b/` in the scratch directory.
