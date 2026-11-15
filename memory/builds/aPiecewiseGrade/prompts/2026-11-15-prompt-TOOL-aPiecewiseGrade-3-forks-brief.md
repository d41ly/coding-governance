# Revision — aPiecewiseGrade: the owner's answers to the two F1s, and the hoist as unit 3

**Serves:** research TOOL-aPiecewiseGrade-3 TOOL-aPiecewiseGrade-1 TOOL-aPiecewiseGrade-2

## The prompt

> (c) Both

> (a) One per slug (Recommended)

The owner's answers, 2026-11-15, to the two questions the session's question tool put from the specs' §8: TOOL-aPiecewiseGrade-1's F1 first, then TOOL-aPiecewiseGrade-2's F1.

## The brief

### Goal
The owner answered both open questions on 2026-11-15. TOOL-aPiecewiseGrade-1's F1, "Build the incremental mode as briefed, or retarget the build at the overhead the first finding names?": "(c) Both". TOOL-aPiecewiseGrade-2's F1, "Is the per-spec cache one per slug or one per worktree?": "(a) One per slug (Recommended)". The overhead removal becomes a new unit, TOOL-aPiecewiseGrade-3, at order 1, and the two specced units follow it at orders 2 and 3.

### Items
1. Write `memory/builds/aPiecewiseGrade/spec/2026-11-15-spec-TOOL-aPiecewiseGrade-3.md`, status SPECCED, rev-1, node a, base `aebbb4a72`, streams tooling, order 1, at the tier `memory/guides/SESSION-KICKOFF.md`'s tier rule assigns to a change inside one kit that moves no verdict and no contract. Its mechanism: `tools/check-spec-tokens.py` resolves the memory-tree kit's `design_lib` once per run, so the guards join and every other `load_design_lib()` caller stop resolving the kit per call. Verify by reading `load_design_lib`, `load_kit_module` and each caller at `d9f84ee14` and at `aebbb4a72` before stating the design, and state what happens when the kit does not resolve, which must read as it does today.
2. Its acceptance rests on the checker's stdout and exit status, byte-identical before and after over the real tree and over a fixture, and a call count or wall figure that shows the per-call resolution gone, both observed by the pass directly. Each measured figure on a spec line carries PINNED or a sha on that line.
3. In TOOL-aPiecewiseGrade-1, F1 carries `RESOLVED (owner, 2026-11-15): (c) Both` in its own span; its order becomes 2; its expected-gain statements read against the tree after unit 3, about 1 s of about 69 s as its F1 already derives (DERIVED d9f84ee14); every other section stays. Bump its rev and add a revision-log line naming this record by its file stem.
4. In TOOL-aPiecewiseGrade-2, F1 carries `RESOLVED (owner, 2026-11-15): (a) One per slug`, its design states the per-slug cache as the only layout, and its order becomes 3. Bump its rev and add a revision-log line naming this record by its file stem.
5. Each spec's §3 edges name the order the three units build in, as the spec format states edges.
6. Stage the three specs and clear `python tools/check-spec-tokens.py --spec` over each. Do not commit. Return each spec's path and status line, each new criterion's id with one line, and the checker's final line for each.

### Acceptance
- Three specs, orders 1, 2 and 3, the two forks RESOLVED with the owner's picks, both revised specs at rev 2 with a revision-log line naming this record.
- TOOL-aPiecewiseGrade-3's criteria name the byte comparison and the removed per-call resolution as observations a pass makes directly.

### Gates
`check-spec-tokens.py --spec` over each of the three specs.

### Non-goals
- The carries join's history read: not this build; it is filed as an ask at the build's wrap-up.
- Any change to a verdict, a refusal line, the summary line or an exit status.
- The bar's spec-tokens leg, which keeps the plain whole-tree run.
- A per-worktree per-spec cache.
- Building anything: the specs stop at READY for the owner's go, and no unit builds before aLightenedLoop lands on main.
