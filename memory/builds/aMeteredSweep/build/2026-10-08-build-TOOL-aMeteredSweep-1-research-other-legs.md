# Appendix — Slow legs: where the time goes and what to change (read-only research)

**Serves:** research TOOL-aMeteredSweep-1

A read-only research pass by one of five agents on 2026-10-08, kept verbatim below its first heading. It ran no suite: every saving is an ESTIMATE from static spawn counts against the profiled bar in `2026-10-08-build-TOOL-aMeteredSweep-1-legs.tsv`, and the synthesis that ranks across all five is `2026-10-08-build-TOOL-aMeteredSweep-1-speed-research.md`. Line citations are against `fa68a767` plus this unit's fixes.


Basis: the profiled bar on node a at `fa68a767` (contended, width 8), the per-leg logs in
`ms1/.git/gate-logs/`, and the source at this worktree. Nothing was run. Every spawn count below
comes from counting call sites and arms. Every "seconds saved" figure is an estimate on the SERIAL
basis unless it says pool. Pool seconds overstate serial cost by 3-5x, so agent-cap's 1801 s pool
was 717 s serial. The cost model is about 0.15-0.3 s per spawn quiet and 1-2 s under load. `node`
and `python` cost more, and so does a python process that compiles a large uncached source.

Three of these reds are correctness problems that this worktree is already fixing (TOOL-aMeteredSweep-1).
They are not cost problems:
- **codebase-map kit selftest**: the `test_gate_coverage_passes_a_customised_gate` fixture is
  missing the `CARDS.md` tier. The uncommitted 3-line edit to `tools/codebase-map/selftest.py`
  adds it.
- **python resolver**: the idiom ban flags three expected-prompt strings at
  `tools/workflows/unattended-build.test.sh:1584,2550,2551`. The uncommitted edit adds
  `# gov:literal-python` markers to them.
- **spec-tokens self-test**: 5 of 135 covers-field arms fail. The uncommitted
  CRLF-folding edit to `tools/check-spec-tokens.py` is in flight against them.
- **foreign-prefix parity**: two reds, neither a cost problem. `row-grammar selftest` timed out
  (rc 124 at 61 s against a 60 s budget that was measured quiet). `gotchas selftest` exited 1 at
  the `scripts/` prefix. That second one is unexplained: gotchas was green at gov's own prefix in
  the same bar, and the log tail cuts off before the failing arm. **It needs a look as a possible
  real foreign-prefix defect.**

## Ranked levers

| # | leg | lever | est. s saved | effort | risk |
|---:|---|---|---:|---|---|
| 1 | foreign-prefix parity | Probe ONE shard per sharded suite. Drop `unattended driver/gate selftest shard 2..8/8` at each foreign prefix | ~500 wall per prefix, ~1500 per green run (4094 of 6709 probe leg-s per prefix) | S | low |
| 2 | foreign-prefix parity | Run the 10 whole-run rows inside the pool, bounded by `k x budget` as a hang guard instead of the quiet-measured budget. This also fixes the row-grammar rc 124 | ~300 wall per prefix, ~900 per run | S | low-med |
| 3 | agent-cap self-test | Run the S9 no-regress property (3646 tracked files x BASE hook, plus 79 x current) in ONE node process (vm.Script or worker_threads) instead of ~3727 `node` spawns | ~550 serial, ~1400 pool (about 88% of the leg) | M | med |
| 4 | foreign-prefix parity | Select rows by the `guard` paths in `gate-legs.json` that changed since the last green foreign-prefix record at a recorded sha | ~70-90% of what remains on a typical 1-3-kit build | M-L | med |
| 5 | python resolver | Replace the per-(copy, block) `grep -c` + `$(awk \| tr)` parity loop (~215 blocks) and the per-file `bare_scan` (124 `*.sh`) with one awk pass each | ~100-150 serial, ~200 pool | S-M | low |
| 6 | agent-cap self-test | Feed the ~300 Workflow-payload arms (`check`/`js`/`jso`) through one node harness, and build their JSON there, which removes ~118 python spawns | ~100 serial | M | med |
| 7 | process-monitor adopter | A test-only census-bound override (for example 15 s), so the hung-census arm stops waiting the full shipped 90 s. Pin the shipped `CENSUS_BOUND_MS` value with a separate grep arm | ~75 serial | S | low-med |
| 8 | lexicon selftest | In `run_case`, copy only the engine's runtime files, keep `__pycache__` (copy2 preserves mtime, so the pyc stays valid) and use `git init --template=` | ~60-100 serial, ~200 pool | S | low |
| 9 | micro-format gate selftest | Do the per-definition-line `printf \| grep \| grep \| sed` pipelines (~10 spawns per line) in one awk over the block. The production "micro-format definitions" leg speeds up too | ~150 pool | S-M | low |
| 10 | playbook parity selftest | Build the fixture once and `cp -r` it per arm. In the gate, collapse the 6-pair `$(eval sed \| head \| tr)` loop into one awk | ~150-200 pool | S | low |
| 11 | verdict-epoch self-test | Make `behav_in` one awk instead of git + 4 grep + sed. Seed `newrepo` from one template repo via `cp -r` instead of init + 3 configs | ~150-200 pool | S | low |
| 12 | scratch-guard self-test | Drop the python JSON builder (122 arms) and the extra outer `node` in `run()` (76 arms). One prelude node can build the payload AND spawn the hook child | ~100-150 pool | M | low-med |
| 13 | review-join / verifier fan-out | One batched `grep -l` instead of a grep per file. A hook "judge these files" mode (fail-closed on stdin, like `--print-cap`) replaces 2 node per file | ~60-100 pool each | M | med (product change) |
| 14 | spec-tokens self-test | Call `check-spec-tokens.py main()` in one python harness for the ~104 `arm` invocations | ~50-80 serial | M | med |
| 15 | install-prefix self-test | Copy govkit.py (854 KB) WITH a valid pyc (`cp -p`) into each fixture, so ~40 gate runs stop recompiling it | ~30-40 serial | S | low |
| 16 | runlog selftest | Call the CLI in-process for its ~47 `run_cli`/`run_runlog` calls (needs an env swap) | ~30-45 serial | M | med |
| 17 | cross-cutting | `resolve_python` + `resolve_kit_dir` cost 2 python starts per gate invocation, ~150+ invocations across these legs. A per-process-tree "already probed" export would skip that | ~90-180 serial total | M | med (touches the resolver contract) |
| 18 | cross-cutting | `git init --template=` everywhere, and export `GIT_AUTHOR_*`/`GIT_COMMITTER_*` once instead of `git config user.*` x2 per fixture | ~30-60 serial total | S | low |
| 19 | straggler-guard arms | UNMEASURED. Trace spawns first (`PS4=... bash -x`). Only 2 fixtures copy the 3.2 MB of kits, but 14 hook-firing commits and 8 pushes run the real 1617-line pre-push | unknown | S to measure | n/a |
| 20 | template size / line length / dead paths | Already batched once. Remaining small wins: `seq` -> `for ((..))` in the gate, one probe per run | ~20-40 pool each | S | low |
| - | playbook validity gate, codebase-map kit selftest | Leave them alone. 121 s against a 4940 s ceiling, and 60 s against 300 | 0 | - | - |

**Next timeout under contention:** straggler-guard (274 s of 300, 91%), the python resolver
(307 of 350, 88%), runlog (it already timed out, 722 of 720), and agent-cap (it already timed out,
1801 of 1800). Levers 3, 5 and 6 take agent-cap and the resolver well clear. Straggler-guard needs
measuring before anything else.

## Wall-clock-timed arms (flake risks)

- `tools/run-gates/foreign-prefix.gov.test.sh:245`: `timeout -k 5 "$4"` bounds each row by its
  `selftest-budgets.txt` budget, and some of those budgets are measured quiet (row-grammar:
  60 s = 1.5 x 36 s). This **has already flaked**: row-grammar hit rc 124 at 61 s. Lever 2 fixes it.
- `tools/hooks/agent-cap.test.sh:2165-2172`: a "quadratic budget" of ≤10 s by `date +%s` for an
  8000-literal line. Node startup alone is 1-2 s under load, so the margin is thin. It is a
  medium flake risk. A ratio against a split-line control, timed in the same process, would be
  robust.
- `tools/process-monitor/adopt-process-monitor.test.sh:318-332`: the hung-census arm requires
  elapsed ≥10 s and <180 s with a 90 s bound. This is low risk.
  - Line 284-286 is a witness that must be older than a 1 s ceiling after `sleep 2`. This is also
    low risk, because the census itself takes seconds.
- `tools/hooks/agent-cap.test.sh:1266-1285`: eight bursts of 6 concurrent hooks. This is a race
  test by design, not a timed one, so it is correct when the claim is atomic.
  - Lines 1291-1316 are a TTL arm moved with `touch -d '46 minutes ago'`. It does not sleep, and
    it is safe.
- `tools/runlog/selftest.py:515,1282,5561,6665`: the timings there are report-only ("grades
  nothing"), and 6665 is a before/after bracket. None of these is flaky.

---

## agent-cap self-test (`bash tools/hooks/agent-cap.test.sh`)

**(a) What it guarantees.** The PreToolUse hook `agent-cap.js` denies an unbounded Workflow or
Agent fan-out under rules 1-5. It also loses no denial that the frozen BASE hook (`d65da7ab`)
made, across every tracked file plus its fixtures.

**(b) Measured cost.** 1801 s pool (TIMEOUT at ceiling 1800). The serial retry took 717 s.
376 assertions.

**(c) Where the time goes.**
- **S9 property arm**, `agent-cap.test.sh:2041-2149`: an embedded `nr.py` runs
  `subprocess.run(["node", base_hook])` once per file of `git ls-files` plus the fixtures. The log
  says "population 3646 scanned, 79 denied at BASE". It then runs the current hook on each of the
  79 denials, plus a re-run per marker loss. That is **~3727 node spawns in one arm**.
- **Every other arm**: `check()` at :119-125 is a subshell plus one `node`. `js()`/`jso()` at
  :130-139 and :316-324 add a python spawn to JSON-encode the script. There are 118 such sites.
  Lines :232 and :269 add a `node -e` per payload. The rule-4 Agent arms (:1240-1338) are about
  60 more node spawns, 48 of them concurrent.
- **Total**: about 4100 node + 130 python spawns. 717 s / ~4230 ≈ 0.17 s per spawn serial, which
  fits a cost that is all spawn. **The S9 arm is about 88% of the leg** (~630 s serial, ~1550 s
  pool).

**(d) Levers.**
1. **S9 in one node process**, saving ~550 s serial.
   - Write `nr.js`. Compile each hook once with `new vm.Script(src)`, then run it per payload in a
     fresh context. The context gets a `require` whose `fs.readFileSync(0)` returns the payload
     and a `process` whose `exit(code)` records the FIRST code and throws a sentinel.
   - The hook reads stdin only at :99 and ends every path in `process.exit` (:2023-2216). An
     uncaught throw maps to 1, as in real node, and "admission = exit != 2" is unchanged.
   - Alternative: `worker_threads`, one worker per payload with `fs.readFileSync` patched in the
     worker's own module registry. That keeps real `process.exit` semantics (the worker's exit
     code) at ~20-40 ms per payload instead of ~150+ ms. It also costs 3727 x ~30 ms ≈ 110 s,
     against ~5 s for vm.
   - Keep the population, the ratification re-run and the "reds on zero ratifications" floor
     exactly as they are.
2. **Batch the Workflow-payload arms**, saving ~100 s serial.
   - One `node arms.js` reads a TSV of (name, want, flag, script) and runs each through the same
     vm runner. That removes the python builder in `js`/`jso` and the `node -e` builders at :232
     and :269.
   - Keep the Agent-tool rule-4 arms, the env arms (:1212-1223) and `--print-cap` (:1974-1992) as
     real spawns. They test process, filesystem and concurrency behaviour.
3. **Cheap**: replace `$(apay ...)` command substitutions in rule-4 loops with precomputed
   strings. That saves about 60 forks.

**(e) Full rebuild.** Turn the leg into one `agent-cap.test.js` that owns a vm runner. About 330
arms go in-process. About 45 stay as real `node` spawns: rule 4 slots and concurrency, env/conf,
`--print-cap`, the crash and timeout posture, and one real-spawn smoke arm per rule. That smoke arm
proves the vm path and the process path agree.
- **Cost**: ~1-2 days.
- **Expected**: ~717 s serial down to ~40-60 s.
- **Risk**: the in-process path diverges from real node. Two things cover that.
  - A parity arm runs N random payloads both ways.
  - A staged break: make the vm `process.exit` stub drop the code, and observe RED.

**Flake.** :2165-2172 (see above).

## scratch-guard self-test (`bash tools/hooks/scratch-guard.test.sh`)

**(a) What it guarantees.** `scratch-guard.js` denies scratch writes into home, across seven
home-root spellings, the 8.3 forms and the env shapes. It is fail-open on junk input. It also
enforces the orientation-card (`READY`) commit check in a real primary-plus-linked-worktree
fixture.

**(b) Measured cost.** 384 s pool, ceiling 490. 168 assertions.

**(c) Where the time goes.**
- **`run()`** at :142-157, 76 call sites: a python spawn builds the JSON payload. Then a `node -e`
  prelude spawns a **second** node child for the hook. That is 3 spawns plus forks per arm.
  - The prelude exists for a reason (:135-141): MSYS rewrites `TEMP` for native node.exe, so the
    env has to be set inside node.
- **`run_card()`** at :467-500, 46 sites: python plus node. The hook itself then spawns `git diff
  --cached` and `git ls-files` per commit-shaped command (`scratch-guard.js:638-656`), so about
  4-5 spawns per arm.
- **`raw()`**: 6 arms, 1 node each. `build_comparable`: 1 node each.
- **Total**: about 600 spawns.

**(d) Levers.**
- **Merge the python builder into the node prelude**: `node -e` takes the cmd, tool and fields as
  argv, builds the JSON and spawns the hook with `input:`. That drops 1 python per arm (122
  arms) and keeps the hook as a real child process, saving ~60-120 s pool.
- **Stronger version**: ONE prelude node per section that spawns the hook child per arm from a
  table, with the per-arm env passed through `spawnSync(..., {env})`. That drops one node per arm
  too, saving ~100-150 s pool. The risk is that the env-per-arm discipline (:9-13) must survive.
  Assert each arm's env inside the child, as today.

**(e) Rebuild.** Not warranted. The hook's main() reads env and spawns git, so isolation per
process is the point.

## verifier fan-out self-test (`bash tools/workflows/check-verifier-fanout.test.sh`)

**(a) What it guarantees.** `check-verifier-fanout.sh` delegates to the agent-cap hook for every
`*.js` that exports `meta`. It refuses an empty population, and it relays `--print-cap` and conf
errors.

**(b) Measured cost.** 144 s pool, ceiling 300. 20 arms.

**(c) Where the time goes.** Each gate run costs:
- `resolve_python` (1 python) and `resolve_kit_dir` (1 python), :134;
- `git rev-parse` and `git ls-files`;
- **a `grep -qE` per candidate .js**, :172-178 (20 tracked .js);
- **2 node per meta file**, :198-206 (the node payload encoder piped into the hook);
- a `--print-cap` node, :216.

On the shipped tree that is about 35-45 spawns. Six fixture repos get git init plus 2 configs
each. Total: about 500 spawns.

**(d) Levers.**
- Replace the per-file grep with one `grep -lE ... -- $FILES` (S, ~20 spawns per whole-tree run).
- A hook mode that judges a list of files in one process removes 2 node per file. It must refuse
  if anything arrives on stdin, as `--print-cap` does, and `check-wiring.sh` must keep asserting
  that the wired command carries no flag. This is a product change.
- `git init --template=` plus env identity in the fixtures.
- Estimated saving: ~60-90 s pool.

**(e) Rebuild.** Not warranted.

## review-join self-test (`bash tools/workflows/check-review-join.test.sh`)

**(a) What it guarantees.** No workflow script keys a skeptic-verdict join on a `.ref` string (rule
5 via `agent-cap.js --only=join`). It also checks:
- untracked files are judged, and ignored files are not;
- every refusal shape (no git, no node, absent predicate, an unclassifiable status, an empty scan)
  is named;
- the shipped harness carries the integer-id join.

**(b) Measured cost.** 218 s pool, ceiling 300. 36 arms.

**(c) Where the time goes.**
- `check-review-join.sh:233-241` runs 2 node per scanned `.js` with **no meta filter**, so all 20
  tracked `.js` files go through it. That is about 40 node per whole-tree run, plus 2 python
  resolvers.
- About 6 arms run whole-tree (:194, :203, :412, :417 and the syntax arms), which is ~250 node.
- 7 fixture repos.
- 8 `grep -F` "harness" arms at :241-251. Those are cheap.
- Total: about 400-500 spawns.

**(d) Levers.**
- The same batch-judge hook mode as verifier fan-out. In one node, 40 node per run becomes 1,
  saving ~80-100 s pool.
- Fold the 8 harness greps into one awk (small).

**(e) Rebuild.** Not warranted.

## lexicon selftest (`python tools/lexicon/selftest.py`)

**(a) What it guarantees.** It covers 799 arms over the naming gate:
- the verb, suffix and cell predicates;
- the scaffold, the adopter `--render`/`--check` and the waivers;
- staged breaks via `patch`/`drop` on a copied engine;
- the TypeScript conformance corpus (115 records, exact agreement).

**(b) Measured cost.** 477 s pool, ceiling 880.

**(c) Where the time goes.** `run_case` at :296-351 is called **181 times**. Each call does four
things:
- **copytree of the whole kit** (:313), about 1 MB in 15 files. That includes `selftest.py`
  (404 KB), `README.md` (52 KB) and `ts-conformance-fixtures.json` (114 KB). The ignore pattern
  drops `__pycache__`, so every copied file is a fresh AV scan target, ~180 MB written per run;
- `git init` (it copies 14 hook templates);
- `git add`;
- `python lexicon.py`. That process **compiles the 254 KB engine from source every time**,
  because no pyc was copied, and then runs `git ls-files` and `git rev-parse` inside itself.

So each case is about 5 spawns plus 15 file copies plus a ~0.3-0.5 s compile. Ten more
scaffold/adopter sites (:878-2078) do the same. Total: about 950 spawns plus about 2700 file
copies.

**(d) Levers.**
1. Copy only what the engine imports at runtime. That is `lexicon.py`, `lexicon_conf.py`,
   `canon.py`, `subtokens.py` and `scaffold_lexicon.py`, plus `adopt-lexicon.sh` for adopter arms
   and the files a `drop` names. Keep `__pycache__`: `shutil.copytree` uses copy2, which preserves
   mtime, so the pyc validates.
   - A patched copy recompiles by itself, because patching changes its size and mtime.
   - Estimate: 40-50% off a case.
2. `git init --template=` saves the 14 sample-hook writes. `tools/codebase-map/selftest.py:1477`
   already uses this form.
3. Run the engine in-process for the non-patch cases: `chdir` plus `lexicon.main([...])` with
   captured stdout. This is M effort and medium risk, because of module globals and
   `SystemExit`. Leave the patch/drop cases as subprocesses.

Estimated saving: levers 1 and 2 save ~60-100 s serial (~200 pool). Lever 3 saves another ~50.

**(e) Rebuild.** Not warranted beyond lever 3.

## runlog selftest (`python tools/runlog/selftest.py`)

**(a) What it guarantees.** It covers 1564 assertions over the runlog extractor, the model and
the record:
- redaction, with no secret or decoy-session leak (checked after every test function, :8662-8674);
- git-call budgets;
- refusals.

**(b) Measured cost.** 722 s pool, TIMEOUT at 720. The serial retry took 151 s. **The 4.8x ratio
is contention**, not a time-waiting arm: every perf_counter use is report-only.

**(c) Where the time goes.** Mostly in-process already (102 `test_` functions).
- **Subprocess sites**: `run_cli` (24) and `run_runlog` (23), each a python start that imports the
  CLI (:392, :1512); `run_git` (53); 11 `build_scratch_clone` calls at 5 git each (:370-389);
  and `build_model` (85 sites), each spawning several `model.run_git` (`model.py:296`).
- **CPU arms**: a 100,000-line parse (:515) and a 50,000 x 200-char redaction scan (:1039, :1282).
- Total: about 400-500 spawns plus some seconds of pure CPU.

**(d) Levers.**
- Run the 47 CLI calls in-process. That needs `os.environ` swapped to `build_arm_env`, cwd set,
  stdout captured and `SystemExit` caught. Saves ~30-45 s serial. Medium risk, because the decoy
  canary depends on env isolation, so keep 2-3 real-subprocess arms as the canary's witnesses.
- Share one scratch clone across tests that only read it. Saves ~10 s.
- The real fix for the timeout is that a 720 s ceiling sat 4.8x above a 151 s serial cost and
  still breached under contention. **That is a runner-policy question, not this suite's.**

**(e) Rebuild.** Not warranted.

## codebase-map kit selftest (`python3 tools/codebase-map/selftest.py`)

**(a) What it guarantees.** It covers 58 arms over `gen_map.py`: the scaffold, gate coverage,
freshness, the reuse-lookup and identifier-token floors.

**(b) Measured cost.** 60 s pool, ceiling 300. It **FAILED on correctness, not cost**: a
customised-gate fixture lacks `CARDS.md` (:2237), and the uncommitted edit in this worktree fixes
it.

**(c) Where the time goes.** 11 subprocess sites. One copytree of the kit (:446). It already uses
`git init --template=` (:1477, :1573).

**(d) Levers.** None worth the effort.

**(e) Rebuild.** No.

## playbook parity selftest (`bash tools/check-playbook-parity.test.sh`)

**(a) What it guarantees.** `check-playbook-parity.sh` reds on four kinds of drift:
- a kit the playbook never names;
- a stale or useless waiver;
- a stated value disagreeing with its owning source (6 pairs);
- a lost or uncreatable results file.

**(b) Measured cost.** 419 s pool, ceiling 1380. 17 arms.

**(c) Where the time goes.**
- **Per arm, `fixture()`** at :146-188: `git init`, 2 x `git config`, `cp`, `sed`, `git add` and
  `git commit`, plus about 12 file writes. That is about 8 spawns.
- **Then** the mutator, `git add` and the gate.
- **The gate**: 3 python (`resolve_python`, `resolve_kit_dir`, registry parse at :170-179) and
  `git ls-files`. Two `grep` per kit (:219-232). Per pair (:275-288), 2 x `$(eval sed < f | head
  -1 | tr)`, which is 6 processes plus 2 forks, and there are 6 pairs, so ~50.
- About 80 spawns per arm, about 1400 in total.

**(d) Levers.**
- Build the fixture once under `$TMP/base`, then `cp -r` it per arm. The commit is already in the
  copied `.git`. Saves ~8 spawns per arm.
- In the gate, run all 6 pair extractions as `sed -n '…;q'` with bash `read`, or as one awk over
  the two files. That takes ~50 spawns to ~8, and the production "playbook parity" leg benefits
  too.
- Estimated saving: ~150-200 s pool.
- The risk is low. The S2 sentinel/results-file arms (:300, :303) must stay staged, and they do,
  because they patch the gate copy.

**(e) Rebuild.** Not warranted.

## playbook validity gate (`bash tools/unattended/check-playbook.sh`)

**(a) What it guarantees.** Every tracked PLAYBOOK block is well-formed:
- coverage mode, gates resolvable and sections present;
- piece records hash-verified;
- the bypass-flag readback.

**(b) Measured cost.** 121 s pool, ceiling 4940. The population is 1 playbook with 2 pieces.

**(c) Where the time goes.** The corpus discovery is already batched (TOOL-aScouredKit-6,
:155-198, previously 941 spawns). What remains:
- about 57 `$(...)` sites, many as `printf | grep -c` per field (:400-500);
- per piece, `sed | head` and `git hash-object`;
- `_conf_key` sourcing.

That is roughly 150-250 spawns.

**(d) Levers.** Swap the `printf '%s\n' "$body" | grep -c` sites for bash `[[ =~ ]]` or one awk
pass. That saves perhaps 50-70 s pool, at low risk. **Low priority**: the leg is 2% of its ceiling
and is not near any boundary.

**(e) Rebuild.** No.

## verdict-epoch self-test (`bash tools/memory-tree/check-verdict-epoch.test.sh`)

**(a) What it guarantees.** An engine (or delegate) behaviour change in a range carries a
`KIT_MEMORY_TREE_VERSION` bump in the right topological place:
- comment-only edits never count;
- a receipt vouching for the blobs reads clean;
- a live run on gov's tree.

**(b) Measured cost.** 410 s pool, ceiling 1130. 27 arms.

**(c) Where the time goes.**
- **Per fixture repo**: `newrepo` (:65-71) runs `git init` plus 3 `git config`.
  `commit_engine` runs `git add` plus `git commit` per commit.
- **Per gate run**: 2 python (`resolve_python`, `resolve_kit_dir` for memory-recall at
  `check-verdict-epoch.sh:174-176`). Then `git cat-file`, `rev-list`, `log -G` and `show`.
  `verat` (`sed|head`) runs per candidate.
- **`behav_in`** (:212-215) is **6 processes per call** (`git diff-tree`, 4 x `grep`, `sed`).
  It is called per commit in the range, and `moved_files` calls it per (commit, file) on the
  failure path (:222).
- The suite also runs the live tree once (:261).
- Total: about 30 spawns per arm, about 800-900 in total.

**(d) Levers.**
- `behav_in` as `git diff-tree ... | awk '...'`. That is 2 processes instead of 6. `moved_files`
  can parse one diff-tree for all files by its `diff --git` headers, which is 1 call instead of
  one per file.
- `newrepo` from a pre-initialised template dir via `cp -r`, or set config by writing
  `.git/config` directly.
- Estimated saving: ~150-200 s pool.
- The risk is low, but the "touching the constant LINE without its VALUE" and "comment-only"
  arms must stay red-proven through the awk.

**(e) Rebuild.** No.

## dead-path carriers self-test (`bash tools/check-dead-paths.test.sh`)

**(a) What it guarantees.** Any tracked carrier naming a deleted or renamed-away file reds. It
needs a deletion sentinel and a rename sentinel in history, so that an empty needle set refuses.
Waivers must be live.

**(b) Measured cost.** 215 s pool, ceiling 2070. 35 assertions.

**(c) Where the time goes.** Already restructured to ONE history repo (:96-112, "eleven `git
init`s made this suite the slowest leg"). What remains is about 32 gate runs. Each runs:
- `git rev-parse` x2, `git ls-files`, `git log -D` and `git log -R`;
- about 6 `sed`/`sort`/`tr` pipelines;
- two `git grep` calls;
- per waiver row, `awk`.

That is about 20-25 spawns, about 750 in total.

**(d) Levers.** Fold the `$(printf | grep -c)` count sites (:245-258) into bash, and the
needle-building pipeline (:120-150) into one awk. This saves perhaps 30-50 s pool, at low risk.

**(e) Rebuild.** No.

## template size gate selftest (`bash tools/check-template-size.test.sh`)

**(a) What it guarantees.** Per-subject size ceilings come from the declaration. The precedence is
positional, then declared, then env, then default. The high-water `--bump` works, and named
failures carry exit codes.

**(b) Measured cost.** 194 s pool, ceiling 710. 29 arms.

**(c) Where the time goes.** About 29 gate runs at about 12-15 spawns each:
- `git rev-parse`;
- `$(seq ...)` at `check-template-size.sh:51`, which runs **on every invocation with args**;
- `awk|tr`, `tr|wc|tr` and `tr|grep`.

Plus `mkfile`, which is `head|tr` per fixture.

**(d) Levers.**
- `for ((i=0;i<_n;i++))` instead of `seq`. One spawn per run.
- `wc -c` via a bash read, or one awk for bytes plus the budget line.
- Estimated saving: ~30-50 s pool, at low risk.

**(e) Rebuild.** No.

## line-length gate selftest (`bash tools/check-line-length.test.sh`)

**(a) What it guarantees.** It enforces a declared maximum line length on agent-instruction prose,
with code fences exempt. A dead interpreter, one that passes the resolver probe and then dies, is
named.

**(b) Measured cost.** 181 s pool, ceiling 930. 19 arms.

**(c) Where the time goes.** The fixture is already built once (:149-171). Each gate run is
2 python (the resolver probe plus the scanner) plus 2 git and a few forks. That is about 8
spawns, about 160 in total, and it is python-start dominated.

**(d) Levers.** Pass the already-resolved python as `LINELEN_PY`. That only helps if the resolver
stops re-probing an override it was handed (see cross-cutting lever 17). Estimated saving: ~30-40
s pool.

**(e) Rebuild.** No.

## micro-format gate selftest (`bash tools/check-microformats.test.sh`)

**(a) What it guarantees.** The charter's micro-format definition block parses. It must have
exactly one fence pair and ≥1 definition, and each line needs one keyword, one ` — ` joiner,
`·`-separated tails and well-formed placeholders.

**(b) Measured cost.** 216 s pool, ceiling 560. 19 arms.

**(c) Where the time goes.** Each arm is a `sed -i` plus the gate. The gate runs ~6 setup spawns,
then **about 10 spawns per definition line**: `printf|grep -o|grep -c`, `printf|sed` x2, and the
`grep -oE` placeholder loop (`check-microformats.sh:61-112`). With 3 lines in the fixture that is
about 40 per arm, about 750 in total.

**(d) Levers.** Do the per-line checks in one awk program over the block, with the same messages.
That is about 5 spawns per run instead of ~40. Estimated saving: ~150 s pool, and the production
"micro-format definitions" leg (11 shapes) gets faster too. The risk is low, because 19 staged
breaks already pin every message.

**(e) Rebuild.** No.

## straggler-guard arms (`bash .githooks/straggler-guard.test.sh`)

**(a) What it guarantees.** The shards-to-builds straggler layer refuses stale shard edits on
commit, rebase and push in real fixture repos with linked worktrees and a bare origin. It also
covers recipe parity and conf-reader agreement.

**(b) Measured cost.** 274 s pool against a **300 s ceiling (91%)**. 84 assertions. This is the
next timeout.

**(c) Where the time goes. Unmeasured.** The structure:
- 2 full `init_repo` fixtures. Only one `write_kits` (:137-146), which copies 3.2 MB in 62 files.
- About 6 inline repos with bare origins (:392-560).
- **14 hook-firing commits and 8 pushes** that run the real `pre-commit` (199 lines) and
  `pre-push` (1617 lines).
- `check-wiring.sh --session` twice (:352, :361).

**(d) Levers.** First count spawns per hook call with a `PS4` trace, as
`memory/gotchas/process-creation-is-the-suite-cost.md` prescribes. The likely mass is in
`pre-push`'s feature-push path and `check-wiring --session`. Candidates:
- seed the inline repos from one template via `cp -r`;
- skip `check-wiring --session` per arm if it is idempotent.

Until it is measured, **raise nothing and fix nothing blind**. Per §7, re-declare the ceiling only
with a reason.

**(e) Rebuild.** No.

## process-monitor adopter selftest (`bash tools/process-monitor/adopt-process-monitor.test.sh`)

**(a) What it guarantees.** The adopter's `--check` enforces the roots and temp-root rules. The
SessionStart/PostToolUse hook reports a flagged process, throttles, and fails open on a hung
census.

**(b) Measured cost.** 253 s pool, ceiling 420. 37 assertions.

**(c) Where the time goes.**
- **The hung-census arm waits the full shipped 90 s.** The bound is `CENSUS_BOUND_MS = 90000` at
  `procmon-hook.js:38`, and the log says "bounded at 90s". That is about 35% of the leg.
- **About 6-8 real census runs**: hook, then `reap.py`, then `powershell Get-CimInstance
  Win32_Process` (`census.py:53,232`) plus `ps -W`. That is several seconds each.
- About 24 `run_hook`/`run_against` calls.

**(d) Levers.**
- Add a test-only override, for example `PROCMON_CENSUS_BOUND_MS`, read only when set. Run the arm
  at ~15 s and keep the ≥10 s "it actually waited" floor. Add an arm that greps the shipped
  constant, so the 90 s value stays pinned. Saves ~75 s.
  - The risk is low-medium: a new env knob on a shipped hook. Fail closed to 90000 on a non-integer.
- Census runs: no safe lever. Each one is the subject.

**(e) Rebuild.** No.

## install-prefix self-test (`bash tools/check-install-prefix.test.sh`)

**(a) What it guarantees.** A kit source names other kits only in drained forms (`{prefix}`/derived).
The graded population is non-empty and counted, and waivers are line-keyed.

**(b) Measured cost.** 136 s pool, ceiling 1670. 40 arms.

**(c) Where the time goes.** Each fixture (:57-74) runs `git init`, 2 `config`, copies, and `git
add`. Each gate run (`check-install-prefix.sh:197-227`) is 2-3 python, and that includes **`python
govkit.py shipped` over an 854 KB govkit.py copied without a pyc**. That is a full compile per
arm, about 0.5-1.5 s CPU.

**(d) Levers.**
- Pre-compile govkit.py once in `$TMP`, then `cp -p` both the source and
  `__pycache__/govkit.*.pyc` into each fixture. Saves ~30-40 s serial at low risk.
- `git init --template=`.

**(e) Rebuild.** No.

## spec-tokens self-test (`bash tools/check-spec-tokens.test.sh`)

**(a) What it guarantees.** A live spec's backticked tokens resolve:
- paths against `git ls-files`;
- legs against `gate-legs.json`;
- covers-ids, hand-offs and guard joins.

Waivers must be shrink-only and live.

**(b) Measured cost.** 151 s pool, ceiling 330. It FAILED 5 of 135 assertions. That is the
covers-field arms, against an in-flight CRLF edit to the checker. It is not a cost problem.

**(c) Where the time goes.**
- About 104 `arm` calls (:209-229). Each is one `python check-spec-tokens.py` (84 KB, which
  compiles fast), and the checker runs `git ls-files`/`git log` inside itself (:396, :608).
- The fixtures come from `scratch()` (:183-205), which runs init, 2 config, add and commit.
- About 400-500 spawns in total.

**(d) Levers.**
- Batch the arms through one python harness that calls `main(argv)` per arm, with cwd swapped and
  stdout captured. Saves ~50-80 s serial. Medium risk, because the checker's module-level regexes
  are stateless but `sys.exit` must be caught.
- Keep the `check_break_refuses` staged-break arms (:1104) as real subprocesses.

**(e) Rebuild.** No.

## python resolver (`bash tools/lib/resolve-python.test.sh`)

**(a) What it guarantees.** Three things:
- the resolver RUNS each candidate, and the MS-Store stub is refused;
- every inline copy of 11 shared blocks is byte-identical to its canonical copy;
- no tracked `*.sh` invokes a bare python launcher.

**(b) Measured cost.** 307 s pool against a **350 s ceiling (88%)**. It FAILED on correctness: 3
expected-prompt strings, fixed in flight.

**(c) Where the time goes.**
- **Parity** (:197-218): 11 rows, with ~215 blocks over ~210 files (resolve_python 67,
  resolve_kit_dir 68, derive_self_rel 47, and others). Per copy, `grep -c`. **Per block,
  `$(blk)`**, which is a fork plus `awk` plus `tr`. That is about 5 spawns per block, ~1000 in
  total, plus 11 x `git grep | grep`.
- **The ban** (:333-336): `bare_scan`, one awk **per tracked `*.sh`** (124 files).
- The {prefix} contract loops (:237-270) and the 2 x 2 start loops.
- Total: about 1300-1500 spawns.

**(d) Levers.**
- One `git grep -l` for all stems. Then ONE awk run over all copies plus all canonicals that
  extracts every (stem, file, k) block, compares each against its canonical with CR stripped, and
  prints the drifted ones. Also ONE awk over all 124 `*.sh` for the ban, using `FILENAME`.
- That cuts ~1100 spawns to ~5. Estimated saving: ~100-150 s serial (~200+ pool).
- The risk is low, with one requirement. Re-observe RED for the drift arm, by staging a one-byte
  drift in a copy, and for the ban, where the existing `plant` arm at :340-345 already stages it.
- Keep the per-row non-empty-population arm.

**(e) Rebuild.** Not needed. The two awk passes are the rebuild.

## foreign-prefix parity (`bash tools/run-gates/foreign-prefix.gov.test.sh`)

**(a) What it guarantees.** Every declared self-test still FINDS ITS SUBJECT once gov's tool root
moves to `scripts/`, `vendor/gov/` and the repo root. Its probe is prologue plus one arm through
`FOREIGN_PREFIX_PROBE=1`, honoured at 63 files. Whole-run rows are declared, both directions red,
and the clone must stay clean.

**(b) Measured cost.** 1658 s pool, FAILED at the first prefix. The first prefix was red, so
`vendor/gov` and the root never ran, which makes this a ~1/3 reading. A green run is ~4500-5000 s
against a 7500 s ceiling.

**(c) Where the time goes.** Measured from the `[scripts]` rows in the log:

| class | rows | leg-s |
|---|---:|---:|
| probe rows, shards 2-8 of the two sharded unattended suites | 14 | **4094** |
| other probe rows | 54 | 2615 |
| whole-run rows, run **serially** after the pool drains (`:285`) | 10 | 611 (corpus-ids 300, build-index 125, gotchas 70, row-grammar 61, check-arms 37) |

At width 8 the probes take ≈ 840 s wall, the whole rows add 611 s serial, and the clone plus move
take about 200 s. That gives ≈ 1650 s per prefix.

The shard probes cost 100-394 s each because every shard pays the suite's whole prologue before
its first arm. They are 24-73 s quiet according to `selftest-budgets.txt:114-121`. The question,
"does the prologue find its subject", is **identical across shards**: `--shard k/8` only selects
arms.

**(d) Levers.**
1. **Probe only shard 1/8** of `unattended.test.sh` and `check-unattended.test.sh` at foreign
   prefixes. Declare it like `WHOLE_RUN`, for example a `SHARD_REP` array with a reason, red in
   both directions. A declared row that no longer exists reds.
   - Saves ~4094 leg-s per prefix. That is ≈ 500 s wall per prefix, ~1500 s per green run.
   - The risk is low. A shard-specific prologue path would be missed, so assert in one arm that
     `--shard` parsing happens after subject resolution.
2. **Whole-run rows into the pool.** They are serial only because their budget was "measured one
   suite at a time". At a foreign prefix the bound is a hang guard, not a cost verdict, because
   the bar's own leg grades cost at gov's prefix.
   - Bound them at `k x budget` (k = 3) and dispatch them first, longest first, in the pool.
   - Saves ≈ 300 s per prefix (611 serial against a ~300 s corpus-ids floor), ~900 per run.
   - **It also removes the realized row-grammar flake**: rc 124 at 61 s against 60 s, from the
     timeout at `:245`.
3. **Change-scoped selection.** Run a row only when a path in its `gate-legs.json` `guard` list, or
   in the move machinery itself (this file, `run-selftests.sh` or `selftest-budgets.txt`), changed
   since the last foreign-prefix run recorded green at a sha. A full run is forced when there is
   no record.
   - A typical build touching 1-3 kits runs ~10-25% of rows.
   - The risk is medium:
     - a suite reading an undeclared sibling kit escapes. The guard lists are the declared
       dependency set, and §12's "names nothing outside itself" ban backs them;
     - it is a new record to keep honest. Print every skipped row with its reason; never let a
       skip read as a pass.
4. **Optional, higher risk**: drop one of `scripts/` and `vendor/gov/`. They differ in depth (1
   and 2), and a `..`-counting prologue can pass one and fail the other, so this saves a third at
   a real coverage cost. **Not recommended.**
5. **Outside this list, but visible here**: the memory-hygiene self-test probe (309 s), run-gates
   turnstile (190 s), hook destinations (163 s) and run-gates canary (153 s) have expensive
   prologues before the probe site. Moving each site earlier, to the first arm that touches the
   subject, cuts the probe floor.

With levers 1 and 2: per prefix ≈ (2615 + 611)/8 ≈ 400 s wall, floored by the longest row at about
343 s. That is against ~1450 s now, **≈ 1050 s saved per prefix and ≈ 3000 s per green run**.
Lever 3 then multiplies on top.

**(e) Rebuild.** Not needed. Levers 1 to 3 keep every row's question and every declaration's
both-directions red.

## Cross-cutting

- **The resolver probe tax.** Every shell gate and test that carries `resolve_python` RUNS each
  candidate (`"$c" -c "import sys"`), and most also run `resolve_kit_dir` (a second python).
  That is 2 python starts per gate invocation even when the caller already holds a verified
  launcher. These legs make about 150+ gate invocations.
  - Lever: an exported `GOV_PYTHON_VERIFIED=<candidate>` honoured only when it equals the first
    candidate. The resolver suite would gain an arm proving a stale export, under a mangled PATH,
    is still re-probed.
  - Saves ~90-180 s serial across the legs. The risk is medium, because it touches the contract
    "being on PATH is not evidence". Only the export, never PATH, is trusted.
- **Fixture git cost.** Use `git init --template=`, as codebase-map already does, and export
  `GIT_AUTHOR_NAME/EMAIL` and `GIT_COMMITTER_NAME/EMAIL` once per suite instead of two `git
  config` calls per fixture. That saves about 3 spawns and 14 file writes per fixture across
  ~100 fixtures, ~30-60 s serial, at low risk.
- **Python compile per arm.** A copied engine with no pyc recompiles every run: govkit.py is
  854 KB and lexicon.py is 254 KB. Copy with mtime preserved (`cp -p` / copy2) together with its
  `__pycache__`.
