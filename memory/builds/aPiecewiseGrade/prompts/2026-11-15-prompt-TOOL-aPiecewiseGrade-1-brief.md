# Brief — aPiecewiseGrade: the spec-token checker re-grades only the specs whose inputs moved

**Serves:** research TOOL-aPiecewiseGrade-1 TOOL-aPiecewiseGrade-2

## The prompt

> Open a new build in coding-governance, through `/session-kickoff`, for an incremental, per-spec `tools/check-spec-tokens.py` mode. It must let `--dispatch` (`run_spec_token_check` in `tools/unattended/unattended.sh`) grade only what a pass commit moved, without changing any verdict. Build aLightenedLoop, unit TOOL-aLightenedLoop-3, found that scoping the check to the dispatching build moves cross-build joins: stale waiver rows, chain carries findings and packet runs. The owner therefore declined scoping there. Read `memory/builds/aLightenedLoop/spec/2026-11-14-spec-TOOL-aLightenedLoop-3.md`, §4 "Why the check is not scoped" and §3. Done means a READY card and specs that state how per-spec inputs are keyed and how cross-build joins stay whole. Stop at READY for the owner's go.

> aLightenedLoop (branch `branch/alightenedloop-eb7b8b`, not yet landed) re-keyed `--dispatch`'s spec-token cache on a digest of the inputs the checker read (`--input-key`, `SPEC_TOKENS_INPUTS`), replacing HEAD. A pass that moves any input the whole-tree checker reads still misses the cache and pays the full check, which runs for about a minute. The next step is a checker that re-grades only the specs whose inputs moved, with identical verdicts, refusal text and bytes. Wait for aLightenedLoop to land before basing on it.

The task came from the session that started this one, on the owner's behalf. Both passages are quoted whole.

## The brief

### Goal
A `--dispatch` after a pass commit runs the spec-token checker in a mode that re-grades only the specs whose own inputs moved, and rebuilds every cross-build join whole from the full set of per-spec findings, so its stdout bytes and exit status equal the whole-tree run's on every tree.

### Items
1. aLightenedLoop is not on main. Read its checker and driver at its head `d9f84ee14`, through `git show d9f84ee14:<path>` or its worktree `C:/projects/coding-governance/.claude/worktrees/alightenedloop-eb7b8b`, and main's at `aebbb4a72`, where aBriskDeclaration has split `run_spec_token_check` into a start half and a read half. Both files differ between the two; the design is for the tree after aLightenedLoop reconciles onto main, and each spec names what it read at which sha. Cite by blob-pinned line `<path>@<oid>:<n>` or `path#symbol`.
2. Read TOOL-aLightenedLoop-3 at `d9f84ee14`, `memory/builds/aLightenedLoop/spec/2026-11-14-spec-TOOL-aLightenedLoop-3.md`: §3, §4 "Why the check is not scoped", "When the cache hits" and "What the key does not check". This build is the follow-up its §3 names.
3. Split the whole-tree run of `main` in `tools/check-spec-tokens.py` into two classes, by reading the code: per-spec grading, whose result is a function of one spec and the inputs it reads; and cross-spec joins, whose result depends on several specs, such as the live and terminal sort, the stale waiver rows, the carries join, the packet join, the supersede and handoff scans, the size high-water mark and the uid set. Give every step a row: its function, its class, and every input it reads, files, listings and git answers.
4. Measure first, at `d9f84ee14` on node a: the whole-tree wall, and how it divides between per-spec grading and the joins. If the joins cost most of the run, say so plainly, with the figure, as the spec's first finding; the build is then not worth building as briefed, and that is a fork for the owner.
5. Unit 1, TOOL-aPiecewiseGrade-1: the checker's incremental mode. State how each spec's inputs are keyed: what one cache entry holds (a spec's raw findings before any waiver or join is applied), what its key digests (that spec's bytes, every file, listing and git answer its grading read, the checker, its kit modules and the conf keys it read), and how those inputs are recorded. Reuse aLightenedLoop's tracer, `arm_input_trace` and `read_open_py`, and its replay, `derive_input_digest`, per spec rather than per run, unless the code shows a better seam; say which. A key derivation that cannot be replayed means a re-grade, never a hit.
6. State how every cross-build join stays whole: each join runs on every incremental run over the full finding set, cached and fresh alike, and the spec shows for each join why its answer equals the whole-tree run's. The stale waiver rows, the carries finding that names a chain build bare and the packet runs are named one by one.
7. The incremental run's stdout lists every finding in the whole-tree run's order and spelling, and ends with the same summary line and exit status. A cache entry is written only when the tree and HEAD did not move while the checker ran, as TOOL-aLightenedLoop-3 S6 records its key.
8. Unit 2, TOOL-aPiecewiseGrade-2: `run_spec_token_check` runs the incremental mode on a miss of aLightenedLoop's whole key, with the per-spec cache under the sidecar root `resolve_sidecar_dir` names; the skip line, the cache-off line and every refusal keep their bytes; the verbs guide states the new run in both copies.
9. Acceptance rests on a differential arm: the plain and the incremental checker run over the same sequence of fixture trees, and their stdout and exit status are compared byte for byte at every step. Plants: a spec flipped CLOSED so a waiver row turns stale; a waiver whose only hit is retired; a chain carries finding naming a chain build bare; a live chain run with a packet; an edit to a file one spec cites; a tracked file appearing at a path probed only by `is_file`; a kit module edit; a conf cutoff moved. Plus one count: after a commit that moves one spec, the incremental run re-grades one spec.
10. Name each new function, flag, variable and file through `python tools/lexicon/lexicon.py --suggest`, and state what the change owes beyond the code: the codebase map, the symbols index, the kit version, the verbs guide, a `help/` page.
11. Each spec states what its design does not check, starting from TOOL-aLightenedLoop-3's "What the key does not check".
12. A choice that is not derivable is a fork in the spec's open questions with options and a recommendation. Where a per-spec cache is shared between slugs, and whether the bar's spec-tokens leg may later use the mode, are candidates.
13. Write two specs, `memory/builds/aPiecewiseGrade/spec/2026-11-15-spec-TOOL-aPiecewiseGrade-1.md` and `-2.md`, Tier-2, status SPECCED, rev-1, node a, base `aebbb4a72`, streams tooling, orders 1 and 2, in the shape `memory/TEMPLATE-SPEC.md` states. Work only in this worktree.
14. Before returning, stage both specs and clear `python tools/check-spec-tokens.py --spec` over each and `python tools/playbook/positional.py check`. Run no whole-tree hygiene, no merge bar and no self-test suite, and do not commit. Return each spec's path and status line, each criterion's id with one line, every fork with its recommendation, the item-4 measurement, and the checker's final line.

### Acceptance
- The differential arm's every step prints byte-identical stdout and the same exit status from the plain and the incremental checker, and each plant is one the arm can be seen red on.
- After a commit that moves one spec, the incremental run re-grades exactly one spec.
- A timed `--dispatch` on node a after a sequential pass commit, base against built, on one frozen clone.

### Gates
The spec-tokens self-test and the driver suite's dispatch arms, run directly. `check-arms` over the driver suite. The lexicon and codebase-map legs the change owes. The merge bar once at the close, without the self-test suites.

### Non-goals
- Scoping the check to the dispatching build.
- Any change to a verdict, a refusal line, the summary line or an exit status of the checker or of `--dispatch`.
- The bar's spec-tokens leg, which keeps the plain whole-tree run.
- aLightenedLoop's whole-key cache, except what runs on its miss.
- The unattended Skill.
- A kit version bump by hand.

### Limitations
- aLightenedLoop is not landed. No unit builds before it lands, and the specs' citations of its code are blob-pinned so they resolve before and after.
- A spec's acceptance criteria cite no path its unit has not built yet.
- Every spec line stating a measured figure carries the word PINNED or a commit sha on that line.

### Reuse
- `tools/check-spec-tokens.py#arm_input_trace`, `#derive_input_digest` and the `read_open_py` block, at `d9f84ee14`: the tracer and the replay, per run today.
- `tools/check-spec-tokens.py#read_named_specs` and the `--spec` walk: the per-spec grading path.
- `tools/unattended/unattended.sh#run_spec_token_check`, `#derive_spec_token_key` and `#resolve_sidecar_dir`: the driver's cache.
- Prior records: TOOL-aLightenedLoop-3, TOOL-aBriskDeclaration-1, TOOL-aSmoothedDispatch-1, TOOL-aSmoothedDispatch-21, TOOL-aBatchedPacket-1.

## Drawn from the session

> No incremental, per-spec checker. It is filed as a follow-up ask at the build's wrap-up.
— agent, TOOL-aLightenedLoop-3 §3 at `d9f84ee14`

> Not the next unit of a sequential run. Each pass commit sets its unit's spec CLOSED, and the checker reads every spec to sort live from terminal. That flip can change the verdict, because a waiver row whose hit came only from that spec turns stale. So a sound key must miss there.
— agent, TOOL-aLightenedLoop-3 §4 "When the cache hits" at `d9f84ee14`

## Owner confirmation

Asked: Declare `spec-audit:` for this build, so a spec reviewer audits the spec set before any build?
Answer: No audit

Asked: Go ahead and build aPiecewiseGrade once aLightenedLoop lands?
Answer: Go after it lands
