# Revision — dRedressedBar: TOOL-dRedressedBar-18, the builder's divergence (an alias launcher escapes the job)

**Serves:** research TOOL-dRedressedBar-18 TOOL-dRedressedBar-19

## The brief

### Goal
DIVERGENCE: spec 18's Job Object mechanism (S3; §4 candidates row 1 and "Measured on node d"; §5 risks; AC1, AC2) fails its own test on node d, and §5 rules on that case: "a breakaway there parks the unit rather than shipping a census-only count". The cause is one the spec did not consider. The runner's resolve_python resolves PYBIN to `python3`, which on node d is a Microsoft Store App Execution Alias (C:\Users\d41ly\AppData\Local\Microsoft\WindowsApps\python3.exe, starting pythoncore-3.14-64). Everything started through that alias leaves a job created with no limit flags. Evidence: on serial.json every leg read procs_total 1 (the bash root only), so spawn six minus spawn none = 0, not 6 (AC1 fails), and memio read peak_job_mem_b 6950912 with write_bytes 0 against at least 200 MiB (AC2 fails). In a scratch manifest, a bash leg running only sleeps counted 7 (bash-forked processes DO stay in, so the escape §4 feared does not happen), a plain Python312 python.exe running spawn.py 2 1 counted 4, and the `python3` and `py` aliases counted 1 each. With no bash in the path, a plain python.exe kept its child in the job (2) while the alias kept only its stub (1). The spec has to choose how an alias launcher is handled, which is a design fork, not a build choice: (a) a preflight that runs PYBIN and each distinct launcher once in a test job and refuses with exit 2 naming the alias, remedy GOV_PYTHON set to a non-alias interpreter, which the runner honours too so the bar and the profile still run one python; (b) resolving the alias to its real interpreter for the legs, which drops the alias's own extra process from every reading so they are no longer the bar's; or (c) a per-leg escape check, the census tree compared against job membership, that marks the job totals unknown. AC1 and AC2 must also name the python they run under. Every path I changed is restored; the work is saved in the scratchpad's unit18-wip/ for the redispatch.

### Items
1. **TOOL-dRedressedBar-18** — bump the rev. The owner resolved the fork as option **(b)**, 2026-10-15: the profiler resolves an alias launcher to its real interpreter for the legs. Record it as a §8 entry marked `RESOLVED (owner, 2026-10-15): (b)`. Specify how the resolution is made and observed: which launchers are probed (PYBIN and each distinct launcher a leg's argv names), how an alias is detected (a launcher whose children leave the test job, or a path under `WindowsApps`, whichever the code can prove), how the real interpreter is found, and that the run record names every substitution it made (alias path, resolved path) so no reading is presented as the bar's own when it is not. State in §5 that the alias's own extra process per launch is not in any reading, and that this is the owner's accepted cost. AC1 and AC2 name the interpreter they run under, and gain a red half: with the resolution disabled on node d, `spawn six` minus `spawn none` reads 0, as the builder observed.
2. **The builder's three notes, each into the spec:**
   - Unit 19's S11 path conversion (`cygpath -m` for the scratch dir and the turnstile key) is needed in unit 18 already, since native Python cannot open bash's `/tmp/...` scratch path. Move what unit 18 needs into unit 18 and say what is left for unit 19. Spec 19 is unbuilt, so revise it in this pass too (its own rev bump and §9 line) so its S11 and criteria no longer claim the moved part, and keep its `<w19>` pass as it is.
   - The pre-commit kickoff-manifest ratchet refuses a commit that stages `tools/gate-legs.json` or `tools/run-gates/run-gates.sh` without a last-audit re-stamp of `memory/guides/SESSION-KICKOFF.md` (unit 17's `6057a55c1` did this). Add that file to Files touched, while unit 19's S1 keeps its reviewed second commit.
   - `test_row_contract_is_complete` in the process-monitor selftest compares exact key sets, so it changes in the same commit that adds the census row keys.
3. **The set-aside work.** The builder's code is kept verbatim in `memory/builds/dRedressedBar/build/2026-10-15-build-TOOL-dRedressedBar-18-1-set-aside-work.md`. Say in §4 that the redispatch restores it from that record and changes it only where this revision requires, and list the record in §10.

### Acceptance
`bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades units 18 and 19 READY. §8 carries the owner's mark. AC1 and AC2 name their interpreter and a red half for the resolution.

### Gates
`memory hygiene`

### Non-goals
- No code. No edit to any spec but 18 and 19. No status change.
- No merge to local main and no push without the owner's ask.
