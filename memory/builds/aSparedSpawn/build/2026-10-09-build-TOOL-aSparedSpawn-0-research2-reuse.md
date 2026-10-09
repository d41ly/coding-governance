# Appendix — Content-addressed reuse and change-based selection for the gate bar: research

**Serves:** none — research that precedes this build's specs; its units await the owner's scope ruling

A read-only research pass by one of five agents on 2026-10-09, kept verbatim below its first heading. Figures are estimates from static counts and one-line timings unless marked measured; the ranked synthesis is `2026-10-09-build-TOOL-aSparedSpawn-0-research.md`.


Research only. Nothing was edited and no leg, suite or `*.test.sh` was run. Paths are relative to the
worktree `gate-runner-profiling-optimization-5d1f1e`.

Instruments, all in this scratchpad:

- `select_sim.py` and its output `select_sim.out`, which give the Q4 per-commit table.
- `shipped.tsv`, the output of `python tools/govkit/govkit.py shipped`, a read-only verb that is not a leg.

Durations come from the profiled bar at fa68a767
(`memory/builds/aMeteredSweep/build/2026-10-08-build-TOOL-aMeteredSweep-1-legs.tsv`). Each leg's
"alone cost" is its retry seconds where a ceiling fired, and its pool seconds otherwise. These
figures were measured on a contended host, so treat them as ±2x.

## 0. Findings first

1. **A soundness bug in today's key (`run-gates.sh:2140-2150`).** A guarded leg's key takes the
   index blobs (`ls-files -s`) plus the porcelain LINES of dirty guarded files. It does not take
   their content. If you edit a guarded file, run green, then edit the same file differently
   without staging, the porcelain line is still ` M tools/x.sh`. The key is unchanged, so
   `GATE_REUSE=1` reuses a green for bytes that never ran. An untracked `?? ` file is keyed the same
   way. `gate-fingerprint.sh` already hashes dirty blobs (its working-tree form), and the guarded
   branch should do the same. Impact is limited because `GATE_REUSE` is opt-in and pre-push scrubs
   it (`.githooks/pre-push:1421`). It must be fixed before any wider use.
2. **The default bar is 76% impure, so reuse of pure legs barely moves it.** Without the self-test
   tier the bar has 63 legs and 7640 alone-leg-s. The three `impure` legs make up 5780 of that:
   `unattended kit gate` 3937, `pass-order history` 1050 and `brief-recorded` 793
   (`gate-legs.json:967,979,992`). Unguarded pure legs are 1160 and guarded pure legs are 700. The
   push-path lever is therefore to make the impure trio keyable by observing the remote as an
   input (§1.5, unit U6). Reusing pure legs does not reach it.
3. **Eight legs read git history, the clock, or state outside the tree, and none of them declares
   it.** `BASE`-in-key (`run-gates.sh:2154`) partly masks this today, but a key built only on file
   bytes would be unsound for them. See §1.4.
4. **Today's guards are too broad to drive selection.** The `{prefix}/` guards fire on any change
   under `tools/`, including `tools/unattended/*.template.md`. They cover the run-gates canary,
   check-wiring, the push-main and install-prefix self-tests, foreign-prefix and others, and
   together cost 11502 leg-s. They fired on 9 of the last 30 main commits that touched only
   unattended templates or `check-remote-literals.sh`. `recall floor arms` guards on `memory/`, so
   it fires on every records-only commit.
5. **Kit-scoped selection of the held tier.** The rule: run a held suite only when its owning
   kit's shipped bytes or the suite file moved. Over the last 30 first-parent commits on main it
   would have run a mean of **4722 of 36221 held leg-s (13%)**, and **nothing at all on 23 of 30
   commits**. That is cheap enough to put the held tier back on the push boundary (§4).

## 1. What a sound per-leg input key needs

The reference model is Bazel/REAPI, from memory of the Remote Execution API. An Action digest
covers four things:

- the Command: argv, environment variables and platform properties;
- the Merkle digest of the input root;
- the timeout and `do_not_cache`;
- a salt.

A hit is only as sound as the input root is complete. Bazel makes that true by **sandboxing**: an
undeclared file is not visible to the action, so under-declaration fails loudly instead of caching
wrongly. Bazel's hermeticity guide warns that system binaries and timestamps are the classic leaks
([bazel.build/basics/hermeticity](https://bazel.build/basics/hermeticity)). Nx adds `runtime`
inputs (a command whose output is hashed, for example `node --version`) and `env` inputs
([nx.dev/reference/inputs](https://nx.dev/reference/inputs)). Turborepo hashes `globalDependencies`
and `env`, and in strict env mode it **withholds** any variable not declared
([turborepo docs](https://Turbo.build/repo/docs/reference/configuration),
[troubleshooting](https://turbo.build/repo/docs/troubleshooting)).

Per leg, the key should be `H(schema, ...)` over the components below.

### 1.1 Command

- The resolved argv, exactly as today (`argvs[$i]`, built at `run-gates.sh:1970`).
- The manifest row's own bytes: name, argv, guard and the read classes from §1.4. `ceiling` is
  optional, since it changes timeouts but not a pass.
- The runner's pass semantics: the blob of `run-gates.sh`, or a `REUSE_SCHEMA` constant bumped by
  hand. Without it, a runner change that redefines "ok" keeps old hits alive.

### 1.2 Input bytes, derived rather than typed

There are three derivation rungs. Take the cheapest one that is sound for a given leg.

| rung | how | cost | sound when |
|---|---|---|---|
| R1 static | the guard, plus the owning kit's `govkit shipped` srcs (`govkit.py:12317`), plus the kit dir, plus `tools/lib/` (sourced by every ported suite, see the line-length kit.toml note), plus `tools/gate-legs.json` | one `ls-files -s`, already the cost today | the leg reads nothing outside it. An unguarded leg falls back to the whole-tree fingerprint, as today (`2151-2152`) |
| R2 traced | record what the leg actually opens. For python, a `sitecustomize.py` on `PYTHONPATH` installs `sys.addaudithook` and logs the `open`, `os.listdir`, `os.scandir` and `subprocess.Popen` events (children inherit it). For bash, MSYS `/usr/bin/strace.exe` exists on node a and traces cygwin-side opens. **Native `python.exe` and `git.exe` are invisible to it**, which is why the audit hook carries the python side. Classify each `git` child by its argv: `ls-files`/`ls-tree`/`grep` means a whole-tree population; `log`/`rev-list`/`merge-base` means history (§1.4) | strace on a 751 ms-a-spawn host multiplies leg cost, so this is calibration mode only | the traced commit exercises every branch, which it never fully does. That is why §2 exists |
| R3 sandbox by subtraction | Bazel's method: run the leg in a sparse worktree holding ONLY the declared set. A matching verdict proves the declaration sufficient for that commit | a full leg run plus a sparse checkout | as a soundness probe (§2), never per run |

Whatever the rung, hash **bytes as the leg reads them**, not only blob ids. On Windows the working
copy holds CRLF (gotcha `crlf-defeats-multiline-replace`), while `ls-files -s` hashes the normalized
blob. Either key in `core.autocrlf`/`core.eol` plus the `.gitattributes` blob, or hash dirty files
with `git hash-object <path>`, which applies the same filters. The current guard key does neither
for dirty files (finding 1).

A directory enumeration is an input in its own right. `git ls-files <dir>/` already captures
additions and deletions, so a leg that walks a population needs no extra key component as long as
the walk is `git ls-files` and not `os.walk`. Under R2, an `os.scandir` on a tracked dir is keyed
as that dir's `ls-files` slice.

### 1.3 Toolchain, env and host class

Hash these into one digest, computed once per run and not once per leg:

- **bash:** `$BASH_VERSION` and `uname -r` (the MSYS/cygwin runtime, which carries awk, grep and
  sed with it).
- **python:** the `PYBIN` path (`run-gates.sh:191`) and `sys.version`, plus `sys.flags.utf8_mode`.
  The encoding-posture leg makes the encoding flags matter.
- **node:** `node --version`, for `workflow script syntax`.
- **git:** `git --version` (2.54.0.windows.1 here).
- **env, strict-mode style:** the values of every variable matching `GATE_* GOV_* *_PY GIT_*
  PYTHON* LC_* LANG TZ`, plus `PATH`. This matters concretely: the canary and the foreign-prefix
  suites drive nested runners that inherit `GATE_FULL`, `GATE_SELFTESTS` and `GATE_JOBS`. Turborepo's
  lesson is that loose env mode is how a wrong-environment artifact gets restored. The stricter
  option scrubs a leg's env to the hashed allowlist. That is a larger change, so record it as a
  follow-up.
- **host class:** `uname -s` (MINGW/MSYS vs Linux/WSL) and `core.autocrlf`. The node tag is
  deliberately left out, so worktrees on one node share entries, while a Windows verdict never
  serves Linux.

### 1.4 Impure reads: classify them, don't just flag them

Today `impure` is a boolean that means "never reuse" (`run-gates.sh:2235`). It should become a
`reads` list, with each class contributing a key component:

| class | key component | legs found reading it (bar tier unless noted) |
|---|---|---|
| `history` | `HEAD` commit sha, which fixes tree and ancestry | `check-dead-paths.sh:122,131` (`git log --diff-filter=D/R` over all history); `check-spec-tokens.py:608` (`git log -1 --pickaxe-regex`); `derive-ceilings.py:524` (`git log -1 --format=%cs`); `drift_report.py:787,1075,1340,1488`; `lexicon.py:4204` (`rev-list --merges` over a range, when given one) |
| `base` | the resolved `BASE` or `GATE_PUSH_BASE` | `check-verdict-epoch.sh:4,11` and `govkit.py epoch` (`govkit.py:12460-12478`, merge-base with `origin/<dflt>`); `test_codebase_map.py:14` (merge-base with the remote default) |
| `clock` | UTC date (day bucket) | `check-memory-hygiene.sh:202` (`date +%Y-%m-%d` against `RECORD_SERVES_CUTOFF`); `manifest-check.sh:491` (`EPOCHSECONDS` health window, which also reads `health.log` in the **git common dir**, outside the tree; confirm whether the leg's argv reaches `render_health_cell`) |
| `remote` | the OUTPUT of a declared probe, Nx-`runtime` style: `git ls-remote <origin> refs/heads/<dflt>` | the three `impure` legs (`gate-legs.json:967,979,992`). Two of them "grade only the commits HEAD carries past" the advertised tip, so their verdict is a function of (inputs, HEAD, tip) and nothing else |
| `network` (opaque) | none, never reused | none on the bar today |

Only a leg declaring `base` keeps `BASE` in its key. That removes the "misses after every landing"
defect (`run-gates.sh:2154`) for everyone else. A `history` leg reuses only at the same `HEAD`.
That covers the important case of the push re-running the sha the lander's bar just ran.

### 1.5 What the classes buy on the push path

`pass-order` and `brief-recorded` already observe the remote with one bounded `ls-remote`. Probing
the tip **first**, at about 1-2 s, and keying on it turns 1843 leg-s into a lookup whenever
`(HEAD, tip, inputs)` match a recorded executed `ok`. The 3937 s `unattended kit gate` is the same
if its only external read is that `ls-remote` (`gate-legs.json:967` says so). Verify that in its
script before trusting it.

## 2. Making declared inputs trustworthy: the soundness check

How others detect a bad hit:

- **Bazel.** Diff the execution logs of two builds. If two uncached builds disagree, the action is
  nondeterministic. If they agree with each other and disagree with the cache, the entry is
  poisoned
  ([remote cache diagnostics](https://bazel.virtuslab.com/book/5~5~3/)). Operationally the standard
  trust posture is that **only CI writes the remote cache** and developers read it.
- **Gradle.** The Develocity build-validation scripts run a build, clean, re-run, and compare
  outcomes and keys as an experiment
  ([develocity-build-validation-scripts](https://github.com/gradle/develocity-build-validation-scripts/releases?page=1),
  [build cache debugging](https://docs.gradle.org/userguide/build_cache_debugging.html)).
- **Azure Test Impact Analysis.** It is the closest analogue to selection. It
  **runs all tests every `runAllTestsAfterXBuilds` builds (default 50)** because its test-to-code
  map goes stale, and it falls back to everything for a change it cannot reason about
  ([TIA docs](https://learn.microsoft.com/en-ie/previous-versions/azure/devops/pipelines/test/test-impact-analysis?view=tfs-2017),
  [design post](https://devblogs.microsoft.com/devops/accelerated-continuous-testing-with-test-impact-analysis-part-1/)).
- **pytest-testmon.** It always re-runs last-run failures, and keeps run variants (environment)
  apart by a user expression ([pypi](https://pypi.org/project/pytest-testmon/0.9.16)).

The proposed check, in four parts:

1. **Only executed `ok` rows are ever written.** That is already the rule: red gets key `-` at
   `run-gates.sh:3607`, and `retried` is never accepted (`3594-3598`). A reused verdict is never
   re-written as a new entry, so a bad entry cannot launder itself forward. Writers are runs on a
   clean tree only, mirroring the stamp's `TREE_CLEAN` precondition (`3822-3824`).
2. **Re-run a random sample of reused legs on every reuse-enabled run.** Seed the sample from the
   run id so it is reproducible. Then:
   - If an executed `ok` matches the cache, the run proceeds.
   - If an executed red meets a cached `ok` on the same key, that is a **disagreement**. The run
     reds with `cache disagreement · <leg> · <key>`, the entry is deleted, and the leg is
     **quarantined**: never reused until its manifest row changes.
   - To separate flake from poison, the red is re-run once, as Bazel's two-uncached-builds rule
     does. Agreement means poison or under-declaration. Disagreement means the leg is
     nondeterministic and must be declared `network`/opaque.
3. **An age bound that is deterministic, not probabilistic.** A leg not executed in the last N
   reuse-enabled runs, or in D days, executes. This is TIA's `runAllTestsAfterXBuilds` and the
   hook's own `GATE_FULL_MAX_LAG=10` (`.githooks/pre-push:1068`). Use N=10 so the two bounds speak
   one number.
4. **Cheap legs never reuse.** Below about 30 s the lookup, the sampling noise and the risk are not
   worth it. Of the 63 bar legs, 54 cost under 60 s. So reuse is effectively for the roughly 25
   legs that cost minutes, which also keeps the trust surface small.

How big a sample buys what confidence. Take one under-declared leg whose cached `ok` is wrong on
every reuse from some commit on. With per-run sample rate `s`, the chance that the bug survives
`n` reuse-enabled runs is `(1-s)^n`:

| s | detected within 5 runs | within 10 runs | runs for 95% |
|---|---|---|---|
| 0.10 | 41% | 65% | 29 |
| 0.20 | 67% | 89% | 14 |
| 0.26 | 78% | 95% | 10 |
| 0.35 | 88% | 99% | 7 |

With the N=10 age bound, detection is **certain within 10 runs regardless of `s`**. The sample only
pulls the expected latency forward: about 1/s runs, so 4 at s=0.26. Recommendation: s=0.25, drawn
**cost-weighted**. Sample one of the expensive legs per run by round-robin plus 25% of the rest, so
the sample's own cost stays at about 25% of the saving.

For a population, if a fraction p of reused verdicts are wrong and a run samples k legs, the
chance of catching at least one is `1-(1-p)^k`. With k=6 and p=0.1 that is 47% per run.

R3 sandbox-by-subtraction is a stronger, rarer probe: once per manifest-row change, run the leg in
a sparse worktree of its declared set. If it reds there and is green in the full tree, the
declaration is short. That probe is the one that converts R1/R2 declarations from "observed" to
"sufficient at this commit".

## 3. Where the cache lives, eviction, and the authority rules

**Location: the git common dir, never a pushable ref.**

- Use `<git-common-dir>/gate-cache/<k[0:2]>/<key>`, one small file per key holding
  `ok \t secs \t run_id \t head \t ended`. Write it tmp-then-rename, as every record here already
  is.
- **Why the common dir.** Today's ledger is per git-dir (`run-gates.sh:336-337`) and holds one row
  per leg name (`grep -m1 -F name\t`, `2236`). So every new worktree starts cold, and an A to B to A
  tree never matches. The common dir is what `gate-full-green.shared` (`3839-3852`) and the
  turnstile (`TS_COMMON`) already use for the same reason: every worktree on a node shares it.
- **Not `refs/gate-cache/*` on origin, and not a CI artifact.** A pushable cache is a poisoning
  channel: anyone with push access could write a green that another node then trusts. The charter's
  own trust line is that the control that binds lives on the remote, and a run with full shell
  access can defeat local state anyway. Host class also differs across nodes (node a is MSYS at
  751 ms a spawn, node d is faster), so cross-node hits would be rare as well as risky. Bazel's
  "CI writes, devs read" posture is the only cross-machine variant worth considering, and only from
  `remote-ci.yml` if CI ever runs the bar authoritatively.

**Eviction.**

- Prune at run end: drop entries older than 30 days or beyond 5000 files, oldest mtime first.
  Entries are about 100 B, so this is about hygiene, not disk.
- Bump a `REUSE_SCHEMA` constant to invalidate everything at once.
- Carry the retired single-row ledger forward as the dispatch-duration hint only (`3584-3619`),
  and stop it serving as the reuse store.

**Interaction with the push boundary. These rules are kept, not loosened.**

- **`gate-full-green` still requires `reuses = 0`** (`run-gates.sh:3822`, README 133-140). A reused
  verdict never stamps a full green. That keeps the stamp's meaning: everything executed, at this
  sha, on a clean tree.
- **`GATE_FULL=1`.** It exists to catch a guard that under-declares (`pre-push:1048-1058`), and
  reuse keyed on the same declarations has the same blind spot. So a `GATE_FULL` run must not reuse
  (status quo, since pre-push scrubs `GATE_REUSE` at `1421`). The one exception worth an owner
  ruling is the `remote`/`history` exact-`HEAD` case in U6: the inputs there are the commit itself
  plus a freshly observed remote tip, so nothing a guard could under-declare is involved.
- **Inherited red.** A red row is never cached, so a reused leg can never be red. A reused leg
  contributes nothing to `check_inherited_verdict` (`pre-push:1504`), which needs executed L and R
  verdicts anyway. The inherited-green stamp also requires `reuses = 0` (`run-gates.sh:3870`), so
  keep it.
- **Where reuse is safe today with no ruling.** Branch bars, `run-selftests.sh`, the DoD's
  `--serial --attribute` runs, and a developer's iterating bar. Those runs are what this repo's
  sessions actually wait on (gotchas `unit-builder-stacks-suites-per-pass`,
  `unattended-suites-run-once-early`).
- **If authoritative reuse is ever wanted.** Add a stamp field `reused <n>` plus `sampled <k>`.
  Pre-push would then accept such a stamp only as `scoped`, never as `full`, and only if every
  reused leg executed within the lag bound. That is the same trade the scoped decision already
  makes for guards (`pre-push:1185-1248`), with stronger evidence: a key match on recorded inputs
  instead of a path diff against an older sha.

## 4. Test selection for the held (self-test) tier

**Today.** Every `chunk=selftests`/`subject=kit` leg is held unless `GATE_SELFTESTS=1`
(`run-gates.sh:2087-2090`). The switch is off at every boundary by owner ruling 2026-08-27
(`.githooks/gate-env.sh` header), so nothing runs the 63 held legs automatically. When someone asks
for them, `GATE_FULL` ignores the guards and they all run.

**Proposal.** Add `GATE_SELFTESTS=changed`. A held leg runs when any path in its selection set
moved since `BASE`. The set is:

- **(A) strict:** the owning kit's `govkit shipped` srcs in `EPOCH_ROLES`
  (`govkit.py:12340,12392-12393`), the same derivation `epoch` uses to decide that a kit moved,
  plus the suite file itself.
- **(B) wide:** A plus the leg's guard, the kit's directories, `tools/lib/` and
  `tools/gate-legs.json`.

Reuse `derive_epoch_state`'s path set directly rather than re-deriving it, so "this kit moved" has
one answer for both the version-bump rule and selection.

**What it would have run, last 30 first-parent commits on `main`** (from `select_sim.out`; held
tier = 63 legs, 36221 alone-leg-s):

| | mean leg-s per commit | share of tier | commits running nothing |
|---|---|---|---|
| everything (`GATE_SELFTESTS=1`) | 36221 | 100% | 0 / 30 |
| (A) shipped bytes + suite | **4722** | **13%** | **23 / 30** |
| (B) A + guard + kit dir + lib | 8502 | 23% | 1 / 30 |

- **Under A**, only the 7 commits that moved kit code ran anything. The big merges ran 28-34k
  (`2648f86d8`, `409b4f5db`, `1e0273418`, the mint `d608d0495`). A unit build such as `a0aa627ec`
  ran 14k, and `ff5a8b542` ran 4k. Every `records(...)` and `spec(...)` commit ran zero.
- **B's** near-total coverage comes from two declarations:
  - `{prefix}/` guards: 12 legs and 11502 s fire whenever anything under `tools/` moves. That
    includes the unattended templates (`3c41d343c`, `d6d50bf0f`, `838bb8238`, `e3d984f68`) and
    `tools/check-remote-literals.sh` (`61c3a3aa4`, `a481c2a75`), none of which those suites read
    as far as their guards can say.
  - `recall floor arms` guards on `memory/`, at 95 s on every records commit.

  R2 traces would narrow both. Until then, A is the defensible rule **plus `tools/lib/` and the
  guard** for the ten suites no kit owns. Those ten (their owner resolved to none): playbook-parity,
  template-size, python-resolver, branch-guard, hook-destinations, dead-path, spec-tokens and
  kit-placeholders self-tests, plus the selftest-harness and extract-arms self-tests. They need an
  explicit owner field, or they fall back to their guard.
- **Unattended suites are not in `gate-legs.json`.** They run through
  `run-unattended-gates.sh --selftests` and need the same rule applied there separately. The
  unattended kit moved in 5 of the 30 commits.
- **Soundness for selection** is the §2 machinery minus the cache. Keep the N=10 age bound: a full
  `GATE_SELFTESTS=1` run at least every 10 landings, the TIA analogue. When a full run reds a suite
  that the breaking commit did not select, file a declaration-miss record. That is the
  left-shift for this class.
- **Caveat.** A diffs each commit against its first parent. A branch's bar diffs against
  `BASE`, which is cumulative over the branch, so per-landing figures sit between the per-commit
  mean and the merge-commit figures.

## 5. Units, in landing order, with savings

Each unit can land and be verified on its own.

| # | unit | change | saving | risk / ruling |
|---|---|---|---|---|
| U0 | fix the dirty-file key | the guarded `input_key` branch hashes dirty and untracked guarded paths' bytes with `git hash-object` instead of porcelain text (`run-gates.sh:2140-2150`); add the §1.3 toolchain/env/host digest and `REUSE_SCHEMA` | 0, correctness only | low; arm: edit, run, edit again, and the key must move |
| U1 | `reads` classes, BASE out of the default key | manifest field `reads: [history, base, clock, remote:<probe>, network]`; `impure: <reason>` maps to `network`; key per §1.4; declare the 8 legs found in §1.4 | the prior pass's estimate for a run with a green parent: **25014 leg-s reusable** (40 guarded legs) when `GATE_SELFTESTS=1`; on the default bar, at most the 700 guarded-pure leg-s | low; opt-in path only |
| U2 | common-dir cache | `<gcd>/gate-cache/` store, executed-`ok`-on-clean-tree writers, LRU prune; the ledger stays as the duration hint | makes U1 hit in a **fresh worktree**, which is where most builds here run their first bar; same per-run figure as U1, reachable roughly every build instead of only on a second bar in one worktree | low |
| U3 | soundness sample + age bound + quarantine | §2 items 1-4 in every reuse-enabled run | negative, costs about 25% of the saving | prerequisite for U6; low |
| U4 | `GATE_SELFTESTS=changed` | selection by (A) plus `tools/lib/` and the guard, reusing `derive_epoch_state`'s path set; an owner field for the 10 unowned suites; the same in `run-unattended-gates.sh` | **mean 31.5k of 36.2k held leg-s per commit (87%) not run**; zero held legs on 23 of 30 commits; makes the held tier affordable at the push boundary again | medium; turning it ON at pre-push reverses the 2026-08-27 ruling, so the **owner decides** |
| U5 | trace-calibrated declarations | `GATE_TRACE=1`: the python audit-hook sitecustomize plus MSYS strace record observed reads into an evidence file beside `derive-ceilings`' evidence; a cheap leg asserts declared ⊇ observed for every reusable leg; then narrow the `{prefix}/` guards | shrinks B toward A: up to 11502 leg-s on the about 9 in 30 commits that touched only unrelated `tools/` files | medium; strace cost on node a is large, so run on demand only |
| U6 | remote as a runtime input; exact-`HEAD` reuse at the push | probe `ls-remote` first and key the impure trio on `(HEAD, tip, inputs)`; allow reuse at pre-push only for `history`/`remote` legs at the exact pushed sha, never under `GATE_FULL`; the stamp gains `reused`/`sampled` and reads `scoped` only | the push re-run of an already-barred sha drops **5780 leg-s**, the 3937 s contended `unattended kit gate` floor; the push bar then becomes the about 1160 leg-s unguarded-pure set (memory hygiene 129 s is the next-longest) | high; crosses "an authoritative run never reuses" (README 133-140, `pre-push:1408-1421`), so the **owner decides** |

**Order and why.** U0 comes first because U1 must not build on an unsound key. U1 and U2 are
dev-loop savings with no authority change. U3 must land before anything authoritative. U4 is the
largest per-commit saving and is independent of the cache, so it can land after U0 alone if the
owner wants it sooner. U5 tightens the declarations both U1 and U4 depend on. U6 is last because it
needs U3's evidence and a ruling.

**What was not measured.** None of these savings is an A/B wall-clock figure. They are leg-second
sums over one contended profile. The wall effect depends on the floor leg: the canary (5769 s)
runs whenever `tools/` moves, so on a kit-touching commit U1, U2 and U4 shorten the tail without
lowering the floor. Run each unit's A/B on a frozen clone with a positive per-arm artifact (gotchas
`ab-arm-must-prove-it-ran`, `run-long-suites-on-a-frozen-clone`).

## Sources

- [Bazel: hermeticity](https://bazel.build/basics/hermeticity)
- [Bazel book: remote cache diagnostics](https://bazel.virtuslab.com/book/5~5~3/)
- [Bazel book: what makes a cache hit](https://bazel.virtuslab.com/book/2~4~3/)
- [Nx: inputs and named inputs](https://nx.dev/reference/inputs)
- [Turborepo: configuration](https://Turbo.build/repo/docs/reference/configuration)
- [Turborepo: troubleshooting (hash inputs)](https://turbo.build/repo/docs/troubleshooting)
- [Gradle: build cache debugging](https://docs.gradle.org/userguide/build_cache_debugging.html)
- [Develocity build validation scripts](https://github.com/gradle/develocity-build-validation-scripts/releases?page=1)
- [Azure DevOps Test Impact Analysis](https://learn.microsoft.com/en-ie/previous-versions/azure/devops/pipelines/test/test-impact-analysis?view=tfs-2017)
- [Accelerated continuous testing with TIA, part 1](https://devblogs.microsoft.com/devops/accelerated-continuous-testing-with-test-impact-analysis-part-1/)
- [pytest-testmon](https://pypi.org/project/pytest-testmon/0.9.16)
- REAPI Action/Command digest composition and Jest `--onlyChanged` (which uses the haste import graph over VCS-changed files) are from memory, not re-fetched.
