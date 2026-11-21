# TOOL-dQuietDisk-7 — one suite template cache: each base repository built once, keyed by its inputs, and cloned per case

**Status:** SPECCED · rev-2 · 2026-11-22 · node d · Tier-2 · base 609cd40b · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |

<!-- /gen:spec-records -->

## 1. Goal

Kit suites buy isolation by construction: every case runs `git init`, configures and commits, or
copies a whole snapshot (`memory/builds/dQuietDisk/build/2026-11-20-build-TOOL-dQuietDisk-19-analysis.md`,
rows G1 and G1b, rework K1 and K2). This unit generalises the two existing template seams,
`tools/lib/lib-selftest.sh` and `tools/govkit/fixture_target.py`, into one template cache with a
bash face and a python face. A base repository is built once per runner invocation and keyed by
its declared inputs. A mutating case gets a `git clone --shared` of it, and a reading case gets one
read-only checkout. The unit proves the bash face on `tools/check-line-length.test.sh`, a suite
`lib-selftest.sh` already serves. Units 10 to 13 move the heavy suites onto it.

## 2. Scope (IN)

- **S1** — The protocol, stated once in `tools/lib/template_cache.py`'s module docstring and
  implemented by both faces. A template is `<cache root>/<key>/repo`, a committed non-bare
  repository, complete when `<cache root>/<key>/ready` exists. A build runs in
  `<cache root>/.stage-<key>-<pid>`, writes `ready` there and renames the directory to
  `<cache root>/<key>`. When that rename fails because the key exists, the loser cleans up its
  stage and uses the winner's template. Observed by AC4.
- **S2** — The cache root, one rule for both faces: `SELFTEST_TEMPLATE_ROOT` when it names a
  directory. Else the nearest ancestor of the process's temp dir named `gate-work.*` and holding an
  `owner` file, which is a bar's owned `$WORK`, with `templates` appended. Else the caller's own
  scratch: `$SELFTEST_ROOT/templates` for the bash face and the `root` argument for the python
  face. Each root dies with the directory that holds it. Observed by AC5.
- **S3** — The key, per face. It is the SHA-1, in git's blob form, of `template-cache v1`, the face,
  the builder's name, the builder's definition and the caller's declared inputs. The bash face
  takes the definition from `declare -f` and each declared input file's blob id from one
  `git hash-object --no-filters --stdin-paths`. The python face hashes the caller's `inputs` mapping
  in-process. Two different builders or two different input sets never share a key. Observed by AC2.
- **S4** — The build. The builder runs in the stage's `repo`. When it leaves no `.git`, the face
  runs `git init -q --template=` there. The face then stages and commits everything with
  `core.autocrlf=false`, an empty `core.hooksPath` and a pinned identity passed as `-c` options.
  It records the repository's local config, minus `core.*` and `remote.*`, in
  `<key>/config-pins`. Observed by AC1.
- **S5** — The clone. A mutating case gets
  `git clone --shared --quiet --template= -c <pin>... <template>/repo <dest>`, then
  `git -C <dest> remote remove origin`, so the case's repository carries the template's config and
  no remote, as a built one does today. A caller that declares keep-remote skips the second
  process. Objects are never copied. Observed by AC1 and AC3.
- **S6** — The bash face, the canonical block `template_cache_sh` in `tools/lib/template-cache.sh`,
  defining `resolve_template_root`, `derive_template_key`, `resolve_template` and
  `build_template_clone`. `tools/lib/lib-selftest.sh` carries it inline, and a `PARITY_ROWS` row in `tools/lib/resolve-python.test.sh` holds the copy to the
  canonical block, so a copy-installed suite can carry it in units 10, 12 and 13. Observed by AC8.
- **S7** — `lib-selftest.sh` opts in per suite. `build_fixture --template "<inputs>" <builder>`
  builds through `resolve_template`, and each arm's copy is a `build_template_clone` with
  keep-remote in place of `cp -a`. A new verb `arm_reading`, with `arm`'s five arguments, declares an arm whose subject
  writes nothing. Every such arm runs in one clone, `$SELFTEST_ROOT/read`, made on first use. After
  the run, `run_arms` FAILs the suite when `git -C "$SELFTEST_ROOT/read" status --porcelain
  --untracked-files=all` prints anything, naming the reading arms. Without `--template`,
  `build_fixture`, `arm` and `arm_reading` run exactly as `arm` runs today, on a `cp -a` copy.
  Observed by AC1, AC3 and AC6.
- **S8** — The python face, `tools/lib/template_cache.py`: `TemplateCache(root=None)` with
  `derive_key(builder_id, inputs)`, `resolve_template(builder_id, inputs, build)` and
  `build_clone(template, dest, keep_remote=False)`. `fixture_target.build_target` gains an optional
  `template` keyword. Given a `TemplateCache`, it ensures a base from its `README.md`, its `deploy`
  text and its `files`, and clones it to `tmp/<name>` in place of the eight processes
  `build_scratch_gov`, its `add` and its commit spend. Without the keyword it builds as today. Observed by AC7.
- **S9** — The switch, the policy key `tests.fixture-templates`, read once per cache through
  `policy.py get`. `shared`, the default, is S1 to S8. `per-case` is today: `build_fixture
  --template` copies with `cp -a`, `arm_reading` runs as `arm`, and `build_target` builds per call.
  An absent policy kit or an unreadable key reads as the default. The key lands with its catalogue
  row, `owner = "dQuietDisk"`, a `summary` and a `usage`, and `help/reference/policy.md` is
  re-rendered from it. Observed by AC6.
- **S10** — `tools/check-line-length.test.sh` builds with `build_fixture --template` naming its
  gate, its policy files and its prefix as inputs, with keep-remote, and declares its two arms
  whose setup is `true` with `arm_reading`. Every arm keeps its label, its want-rc and its
  want-substring. Observed by AC3 and AC9.

## 3. Non-goals (OUT)

- No suite move beyond `tools/check-line-length.test.sh`. `tools/check-wiring.test.sh`, its
  `NEWREPO_SEED` included, is unit 10's. `tools/govkit/selftest.py` is unit 11's, which passes
  `template` to `build_target`. `.githooks/pre-push.test.sh` and the `run-gates*.test.sh` suites
  are units 12 and 13's.
- No move of `skills/session-kickoff/manifest-check.test.sh`'s local template. TOOL-dQuietDisk-6
  changes `manifest-check.sh` at order 2 and may add arms to that suite, and no unit here owns its
  arms. The template there maps onto S7 unchanged; its move is a follow-up.
- No `git worktree add` per case. It writes the template's own `.git/worktrees`, which every
  concurrent case would then share, and a detached HEAD differs from the `main` a built fixture
  holds.
- No runner change. The cache root follows the runner's owned `$WORK` by S2's ancestor rule, and
  `run-gates.sh` and `run-selftests.sh` are not written.
- No cross-face key parity. A bash builder and a python builder are different builders, so their
  keys never meet.

### Edges

- **hands-off** `TOOL-dQuietDisk-10` — the check-wiring suite on the bash face, carrying the block
  inline and folding its own seed repository onto it
- **hands-off** `TOOL-dQuietDisk-11` — the govkit self-test on the python face, passing a cache to
  `build_target`
- **hands-off** `TOOL-dQuietDisk-12` — the pre-push suite on the bash face
- **hands-off** `TOOL-dQuietDisk-13` — the run-gates suites on the bash face

## 4. Design

### Where the code was read

Every citation is at `609cd40b1`, the tip of `branch/unattended-dwitnessedbar-2ed3b3`, by symbol or
as `<path>@609cd40b1:<line>`.

### The seams today

- `build_fixture` runs a builder once into `$SELFTEST_ROOT/snapshot`, and `_st_run_one` copies it
  per arm with `cp -a` (`tools/lib/lib-selftest.sh#_st_run_one`). The copy is what makes the pool
  safe, by the file's own account, and it copies every object and every hook sample per arm.
- `fixture_target.py#build_target` builds a target per call through `build_scratch_gov`: an
  `init`, five `config` calls, an `add` and a `commit`, each a process.
- Two local templates already build once and copy per case: `NEWREPO_SEED` in
  `tools/check-wiring.test.sh@609cd40b1:45` and `TEMPLATE` in
  `skills/session-kickoff/manifest-check.test.sh@609cd40b1:65`. Both copy with `cp`.
- A bar's `$WORK` is a `gate-work.*` directory with an `owner` file, and its legs' `TMPDIR` is
  `$WORK/tmp` (`tools/run-gates/run-gates.sh#write_work_owner`,
  `tools/run-gates/run-gates.sh@609cd40b1:2464`). Its trap removes it.

### Why a reading case needs a declaration

A case's subject can write, and nothing in the harness can tell. So sharing a checkout is opt-in,
per arm, and S7 checks the claim after the run: a reading arm that wrote fails the suite rather than
leaking into its neighbours unseen.

### Why the clone drops its remote

A built fixture has no remote, and subjects such as `check-wiring.sh` and `push-main.sh` read
remotes. A clone left with `origin` would hand them a state no arm was written against. Only a
caller that knows its subject reads no remote declares keep-remote. `check-line-length.sh` runs
`git rev-parse` alone (`tools/check-line-length.sh@609cd40b1:54` and `:58`), so S10 declares it.

### Why a committed template is the same fixture for this suite

`build_repo` in the line-length suite runs `git init` and writes files without committing them.
The template commits them. The gate reads the top level and the prefix through `rev-parse` and the
files from disk, never the index, so a committed file and an untracked one with the same bytes
grade alike. AC3 observes it on every arm.

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `tests.fixture-templates` | policy key, values `shared` and `per-case` | the catalogue | `policy.py check` |
| `template_cache_sh` | parity block marker | `PARITY_ROWS` | `tools/lib/resolve-python.test.sh` |
| `resolve_template_root`, `derive_template_key`, `resolve_template`, `build_template_clone` | shell functions | `sh.function`, lexicon `--suggest` OK | `tools/lib/lib-selftest.test.sh` |
| `arm_reading` | `lib-selftest.sh` verb, a shell function | `sh.function`, lexicon `--suggest` OK | `tools/lib/lib-selftest.test.sh` |
| `--template` | `build_fixture` option | none | `tools/lib/lib-selftest.test.sh` |
| `SELFTEST_TEMPLATE_ROOT` | environment variable | none | `tools/lib/lib-selftest.test.sh` |
| `TemplateCache` | Python class | `py.type`, lexicon `--suggest` OK | the probes of section 6 |
| `derive_key`, `resolve_template`, `build_clone` | `TemplateCache` methods | `py.function`, lexicon `--suggest` OK | the probes of section 6 |
| `template` | keyword of `build_target` | none | the probes of section 6 |

`.lexicon.conf` pins `VERB_OFFENDER_PIN` at the full offender count, so every function, method and
shell function above leads with a declared verb, checked by
`python tools/lexicon/lexicon.py --suggest <name> --as <cell>`; `TemplateCache` defines no
`__enter__` or `__exit__`, which the lexicon grades as functions.

### Files touched (estimate)

`tools/lib/template_cache.py` · `tools/lib/template-cache.sh` · `tools/lib/lib-selftest.sh` ·
`tools/lib/lib-selftest.test.sh` · `tools/check-line-length.test.sh` ·
`tools/govkit/fixture_target.py` · `tools/lib/resolve-python.test.sh` ·
`tools/policy/catalogue.toml` · `help/reference/policy.md` · `tools/gate-legs.json` ·
`memory/guides/SESSION-KICKOFF.md`

`tools/gate-legs.json` gains the two new `tools/lib/` files in the guard of `selftest harness
self-test`, so an edit to either runs the suite that holds their arms. The kickoff manifest's
`watch:` line names `tools/gate-legs.json`, so that commit also re-stamps the `last-audit` of
`memory/guides/SESSION-KICKOFF.md`.

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| `git worktree add --detach` per case | It writes the shared template, and a detached HEAD is not the fixture's `main`. |
| `clone --no-checkout` plus a sparse checkout | A case's subject reads paths the harness cannot predict, so the sparse set would be a guess per suite. |
| A key from the template's own tree id | It is known only after the build, which is the cost the key exists to skip. |
| A cache per suite only | Suites in one bar that build the same base would each build it; S2 shares it across the bar. |
| `git bundle` per template | It still unpacks objects into every case, which `--shared` avoids. |

## 5. Production-readiness checklist

- security: the cache lives under the owned scratch of the run that made it and is removed with it.
  No new input crosses a trust boundary; the inputs are the suite's own files.
- perf / scale: a template costs one build per root. A mutating case costs one `clone`, plus one
  `remote remove` unless keep-remote. A reading case costs nothing after the first.
- error / empty / loading states: a failed build refuses as `build_fixture` refuses today, exit 2
  naming the builder. A failed clone fails that arm with the copy's existing `ERR` line.
- observability: `build_fixture --template` prints `template: <key8> built` or
  `template: <key8> reused` once.
- risks: two cases cloned from one template share its base commit id, where two built fixtures differ
  by their timestamps. An arm comparing commit ids across fixtures would read them equal; unit 11
  checks its arms for that. The gotcha `suite-invalidated-by-a-commit-under-it` does not reach the
  cache, because its root dies with the run.
- testing: the arms `tools/lib/lib-selftest.test.sh` gains and the probes of section 6.
- migration: N/A — opt-in per suite; a suite that does not pass `--template` is unchanged.
- user docs: the policy key's help row is rendered from its catalogue row.

## 6. Acceptance criteria

- **AC1** — When a bash probe under `%TEMP%/<short-name>` sources `lib-selftest.sh` from
  `tools/lib/`, builds a fixture with `build_fixture --template` whose builder runs `git init` and
  `git config user.email t@t`, and clones it twice with `build_template_clone`, each clone's `git config
  user.email` prints `t@t`, `git remote` prints nothing, and its tracked files equal the builder's.
  The template's `.git/objects` holds every object, and neither clone's does: each holds an
  `objects/info/alternates` naming it.
  Red when: the clone copies objects, keeps `origin`, or loses the builder's config.
- **AC2** — When the probe calls `derive_template_key` for one builder with two input sets that differ by one
  byte of one input file, and for two builders whose names match but whose `declare -f` bodies
  differ, the four keys are distinct. The same builder and inputs give the same key twice.
  Red when: a key omits the definition or the inputs' blob ids.
- **AC3** — When a probe script under `%TEMP%/<short-name>` sources `lib-selftest.sh` from
  `tools/lib/` and runs three arms copied from the line-length suite S10 names, two green and one
  at the width edge, through `build_fixture --template` naming the gate, its policy files and its
  prefix as inputs, once with `tests.fixture-templates` at its default and once at `per-case`, both
  print the same `ok` lines in the same order. With the gate's 450 default changed to 449 in the
  template's input, the same arm goes red in both modes. When the main loop runs the line-length
  suite itself at the close in both modes, both print the same 20 `ok` lines in the same order and
  the same `PASS (20 arms, width <n>)` line, and the same arms go red at 449.
  Red when: an arm's result differs between the modes, or the red arms differ.
  permission: a role agent runs no suite, whichever kit holds it (scratch-guard row G3), so the
  suite's own reading is owed to the main loop; the pass makes the three-arm probe.
- **AC4** — When two shells run `resolve_template` for the same key at once in one root, one builds and one
  reuses, the root holds one `<key>` directory and no `.stage-*`, and both get the same template.
  Red when: the loser's stage is renamed over the winner or left behind.
- **AC5** — When the probe runs `resolve_template_root` with `SELFTEST_TEMPLATE_ROOT` set, it prints that
  directory. Unset, with `TMPDIR` inside a planted `gate-work.x/tmp` holding `gate-work.x/owner`,
  it prints `gate-work.x/templates`. With neither, it prints `$SELFTEST_ROOT/templates`.
  Red when: a root outside an owned or caller-owned directory is chosen, so it outlives the run.
- **AC6** — When a probe script declares one `arm_reading` whose subject writes a file, `run_arms`
  exits 1 naming that arm and the read checkout. With the write removed it exits 0. Under
  `tests.fixture-templates = "per-case"`, that arm runs in its own copy and the suite exits 0.
  Red when: a reading arm's write passes unnoticed under `shared`.
- **AC7** — When a python probe calls `build_target(tmp, deploy, name, files)` with and without a
  `TemplateCache`, the two targets hold the same tracked files, the same `HEAD` subject `base`, the
  same `git config --local` values for `user.email`, `core.autocrlf`, `commit.gpgsign` and
  `core.hooksPath`, and no remote. With `GIT_TRACE2_EVENT` set, a second cached call costs two
  git processes, against the eight of an uncached call.
  Red when: the cached target differs in a config pin or carries `origin`.
  figure: DERIVED at observation for the uncached count; PINNED at two for the cached call.
- **AC8** — When the parity table's `blk` awk extracts `template_cache_sh` from `template-cache.sh`
  and from `lib-selftest.sh`, the two compare equal.
  Red when: the inline copy drifts by one byte, which the new `PARITY_ROWS` row then reports.
- **AC9** — When AC3's probe runs with `TEMP`, `TMP` and `TMPDIR` pointed at an empty directory
  sampled every 0.5 s, once at the default and once at `per-case`, the default run's peak entry
  count is lower than the `per-case` run's and the residual is 0 for both. When the main loop runs
  the line-length suite the same way at the close, in a scratch `git clone --shared` of gov and once
  more on the base suite, the unit's peak is lower than the base's, the residual is 0 for both, and
  the unit's run spawns no more processes in total, counted by `GIT_TRACE2_EVENT` for git and by the
  arm count for `cp`.
  Red when: the peak does not fall, or a template outlives the run.
  figure: DERIVED at observation; the analysis's PINNED base reading is 57 git processes and a peak
  of 1,189 entries, measured 2026-11-20.
  permission: the suite's own reading is owed to the main loop (scratch-guard row G3); the pass
  makes the probe's.

## 7. Gates

`selftest harness self-test` · `line-length gate selftest` · `extract-arms self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `policy check` · `policy fixtures` · `scratch-guard self-test` · `routed-commits selftest` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `testsuite counts (every bar self-test prints one)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `line length`

New arm: tools/lib/lib-selftest.test.sh · covers AC1 AC2 AC4 AC5 AC6 · the template mode's arms: a clone that copies objects or keeps its remote, two builders colliding on one key, a racing stage left behind, and a reading arm that writes; each failing case is staged by that break in the harness · its FLOOR_ASSERTIONS rises by the arms added
New arm: tools/lib/resolve-python.test.sh · covers AC8 · the template_cache_sh row; its failing case is staged by one changed byte in the copy lib-selftest.sh carries · none

The bar runs once at the close. The line-length suite's own readings in AC3 and AC9 are the main
loop's at the close: a role agent runs no suite, whichever kit holds it. The pass makes their probe
halves.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft. Order 2, not the briefed 1: TOOL-dQuietDisk-1 at order 1
  also writes `tools/lib/resolve-python.test.sh`, `tools/policy/catalogue.toml`,
  `help/reference/policy.md` and `tools/gate-legs.json`. Any order-2 unit adding a policy key or a
  parity row shares those files with this one and is sequenced with it by the dispatcher.
- rev-2 · 2026-11-22 · S6 · S7 · S8 · §4 · AC1 · AC2 · AC3 · AC4 · AC5 · AC9 · §7 · under
  `2026-11-22-prompt-TOOL-dQuietDisk-1-divergence-task`. Every minted name the lexicon refused
  leads with a declared verb, each checked by `--suggest`: the bash face's `tc_root`, `tc_key`,
  `tc_ensure` and `tc_clone` are `resolve_template_root`, `derive_template_key`, `resolve_template`
  and `build_template_clone`, and `TemplateCache`'s `key`, `ensure` and `clone` are `derive_key`,
  `resolve_template` and `build_clone`. AC3 and AC9 had the pass run the line-length suite, which a
  role agent may not run; each now has the pass run a three-arm probe script, and the suite's own
  reading is owed to the main loop at the close.

## 10. Reuse audit

The seams extended: `tools/lib/lib-selftest.sh`'s `build_fixture` and `_st_run_one`, whose snapshot
becomes a template, `tools/govkit/fixture_target.py#build_target`, which gains the cache, the
copy rule of `PARITY_ROWS` (`tools/lib/resolve-python.test.sh@609cd40b1:405`), and the bar's owned
`$WORK` (`tools/run-gates/run-gates.sh#write_work_owner`), which S2 finds rather than re-creates. The
local templates of `tools/check-wiring.test.sh` and `skills/session-kickoff/manifest-check.test.sh`
are the shape S1 generalises; their suites move in other units.

`python tools/codebase-map/reuse_lookup.py "build a fixture repository once and clone it per test case"`
ranked `build`, `fixture`, `build_records`, `run_selftest_cases`, `run_fixture_git` and
`write_fixture_files`. `run_fixture_git` is a git runner for fixtures in five files and builds no
template; `run_selftest_cases` in `tools/loop/loop_lib.py` runs cases and builds none. No existing
seam clones a template.

Recall returned TOOL-aSparedSpawn-9, which built `NEWREPO_SEED` once and copied it per call, and
TOOL-aQuenchedHarness-5, the harness's own spec, whose per-arm copy this unit replaces with a clone.
The owning chain build is dWitnessedBar (Test: gate health and budgets); no spec of it at
`609cd40b1` changes `lib-selftest.sh` or `fixture_target.py`.

Recall terms used: fixture template snapshot build_fixture lib-selftest build_target fixture_target newrepo seed clone shared
