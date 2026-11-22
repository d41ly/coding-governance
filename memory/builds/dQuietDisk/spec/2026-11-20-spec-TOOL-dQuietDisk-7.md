# TOOL-dQuietDisk-7 — one suite template cache: each base repository built once, keyed by its inputs, and cloned per case

**Status:** CLOSED · rev-6 · 2026-11-22 · node d · Tier-2 · base 40def53f · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 |
| [2026-11-22-build-TOOL-dQuietDisk-7-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dQuietDisk-7-1-acceptance-ledger.md) | journal | — |
| [2026-11-22-build-TOOL-dQuietDisk-7-deviation-1.md](../build/2026-11-22-build-TOOL-dQuietDisk-7-deviation-1.md) | deviation | — |
| [2026-11-22-build-TOOL-dQuietDisk-7-widen-7.md](../build/2026-11-22-build-TOOL-dQuietDisk-7-widen-7.md) | widen | — |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-divergence-2-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-divergence-2-task.md) | research | TOOL-dQuietDisk-1 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-2-reground-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-2-reground-task.md) | research | TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-8 |
| [2026-11-22-prompt-TOOL-dQuietDisk-7-1-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-7-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-7-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-7-build-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-7-divergence-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-7-divergence-task.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Kit suites buy isolation by construction: every case runs `git init`, configures and commits, or
copies a whole snapshot (`memory/builds/dQuietDisk/build/2026-11-20-build-TOOL-dQuietDisk-19-analysis.md`,
rows G1 and G1b, rework K1 and K2). This unit generalises the two existing template seams,
`tools/lib/lib-selftest.sh` and `tools/govkit/fixture_target.py`, into one template cache with a
bash face and a python face. A base repository is built once per runner invocation and keyed by
its declared inputs. A mutating case gets a `git clone --shared` of it, and a reading case gets one
read-only checkout. The unit proves both faces with the harness suite's own arms and the probes of
section 6. Units 10 to 13, whose suites build a git repository per case, move onto it.

## 2. Scope (IN)

- **S1** — The protocol, stated once in `tools/lib/template_cache.py`'s module docstring and
  implemented by both faces. A template is `<cache root>/<key>/repo`, a committed non-bare
  repository, complete when `<cache root>/<key>/ready` exists. A build runs in
  `<cache root>/.stage-<key>-<pid>`, writes `ready` there and renames the directory to
  `<cache root>/<key>`. The bash face renames with `mv -T <stage> <key dir>`, because a plain `mv`
  into an existing directory nests the stage inside it rather than failing. The python face renames
  with `os.rename`, which fails onto the key directory because that directory is never empty. When
  the rename fails because the key exists, the loser reads it as another run having built it: it
  cleans up its stage and uses the winner's template. Observed by AC4.
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
  It records the repository's local config in `<key>/config-pins`, minus `remote.*`, `branch.*`
  and the seven keys git writes itself at init: `core.repositoryformatversion`, `core.filemode`,
  `core.bare`, `core.logallrefupdates`, `core.symlinks`, `core.ignorecase` and
  `core.precomposeunicode`. Every other `core.*` key a builder sets is a pin, so
  `build_scratch_gov`'s `core.autocrlf` and `core.hooksPath` reach each clone. Observed by AC1 and
  AC7.
- **S5** — The clone. A mutating case gets
  `git -c core.autocrlf=false clone --shared --quiet --template= -c <pin>... <template>/repo <dest>`,
  then `git -C <dest> remote remove origin`, so the case's repository carries the template's config
  and no remote, as the `cp -a` copy it replaces does. Every clone drops the remote, and no caller
  can keep it. The leading `-c core.autocrlf=false` binds the clone
  process alone. Its checkout writes the committed bytes, as `cp -a` copies them today, whatever
  the global line-ending setting, and nothing is persisted that the builder did not set. Objects are
  never copied. Git's trace2 event log records a local clone as `git` and `git-upload-pack`, so a
  clone and its remote step cost three git processes (PINNED, measured by the builder 2026-11-22).
  Observed by AC1, AC3 and AC7.
- **S6** — The bash face, the canonical block `template_cache_sh` in `tools/lib/template-cache.sh`,
  defining `resolve_template_root`, `derive_template_key`, `resolve_template` and
  `build_template_clone`. `tools/lib/lib-selftest.sh` carries it inline, and a `PARITY_ROWS` row in `tools/lib/resolve-python.test.sh` holds the copy to the
  canonical block, so a copy-installed suite can carry it in units 10, 12 and 13. The
  `[[exempt_leg]]` row `selftest harness self-test` in `tools/govkit/registry.toml` gains both new
  `tools/lib/` files in its guard, so an edit to either runs the suite holding their arms, and
  `tools/gate-legs.json` is re-rendered by `python tools/run-gates/leg_factory.py --write`, never
  edited. Observed by AC8 and AC11.
- **S7** — `lib-selftest.sh` opts in per suite. `build_fixture --template "<inputs>" <builder>`
  builds through `resolve_template`, and each arm's copy is a `build_template_clone` in place of
  `cp -a`. `--template` is the one option `build_fixture` gains. A new verb `arm_reading`, with `arm`'s five arguments, declares an arm whose subject
  writes nothing. Every such arm runs in one clone, `$SELFTEST_ROOT/read`, made on first use. After
  the run, `run_arms` FAILs the suite when `git -C "$SELFTEST_ROOT/read" status --porcelain
  --untracked-files=all` prints anything, naming the reading arms. Without `--template`,
  `build_fixture`, `arm` and `arm_reading` run exactly as `arm` runs today, on a `cp -a` copy.
  Observed by AC1, AC3 and AC6.
- **S8** — The python face, `tools/lib/template_cache.py`: `TemplateCache(root=None)` with
  `derive_key(builder_id, inputs)`, `resolve_template(builder_id, inputs, build)` and
  `build_clone(template, dest)`, whose clone carries no remote, as S5 states, and which takes no
  option to keep one. `fixture_target.build_target` gains an optional
  `template` keyword. Given a `TemplateCache`, it ensures a base from its `README.md`, its `deploy`
  text and its `files`, and clones it to `tmp/<name>` in place of the eight processes
  `build_scratch_gov`, its `add` and its commit spend. A cached call costs the clone's three
  git processes (PINNED, measured by the builder 2026-11-22). Without the keyword it builds as
  today. Observed by AC7.
- **S9** — The switch, the policy key `tests.fixture-templates`, read once per cache through
  `policy.py get`. `shared`, the default, is S1 to S8. `per-case` is today: `build_fixture
  --template` copies with `cp -a`, `arm_reading` runs as `arm`, and `build_target` builds per call.
  The bash face finds its python by sourcing `tools/lib/resolve-python.sh` beside `lib-selftest.sh`
  and calling `resolve_python`, and a copy-installed suite carries that block inline beside
  `template_cache_sh`, as the kit rules already require of it. An absent policy kit, an unreadable
  key or no usable python reads as the default. The key lands with its catalogue
  row in the shape of `tests.history-verdicts`: `allowed = ["shared", "per-case"]`,
  `default = "shared"`, a `summary`, a `usage` and `owner = "dQuietDisk"`. `help/reference/policy.md`
  is re-rendered from it. Observed by AC6.
- **S10** — The proof is the harness suite's own. `tools/lib/lib-selftest.test.sh` gains the
  template mode's arms: a clone that copies objects or keeps its remote, two builders colliding on
  one key, a racing stage left behind, a reading arm that writes, and one suite run under
  `--template` in both values of `tests.fixture-templates`. No existing suite moves onto the cache
  here. Observed by AC3 and AC9.
- **S11** — The shell-line ledger. `memory/project/shell-role.txt` is shrink-only, read by the
  unguarded leg `portability (shell lines only shrink)`, and a new shell file or a grown one is red
  there. The new `tools/lib/template-cache.sh` has no row. `tools/lib/lib-selftest.sh` grows by the
  inline block and `arm_reading`, and `tools/lib/lib-selftest.test.sh` and
  `tools/lib/resolve-python.test.sh` grow by their arms and their row. `lib-selftest.sh` also gains
  the line that sources the resolver. Each key whose measured count
  rises above its row is widened through the ledger factory's door,
  `python tools/memory-tree/ratchet.py widen shell-role --key <path>... --reason <one line> --unit TOOL-dQuietDisk-7`,
  as TOOL-dQuietDisk-1 widened its keys (`2026-11-22-build-TOOL-dQuietDisk-1-widen-2`). The door
  writes the next widen record of this build under `memory/builds/dQuietDisk/build/` and marks each
  row `widened:<record stem>`, and no row is hand-edited. The Reason gives the lines this unit adds
  per key. It names no base excess, because every one of these rows equals its file's measured count
  at `8688cdbba` (PINNED, `sh_hygiene.py --shell-role --measure`, 2026-11-22). A key that does not
  grow is not named. Observed by AC10.

## 3. Non-goals (OUT)

- No existing suite moves onto the cache in this unit. `tools/check-line-length.test.sh` stays on
  `cp -a`. Its arms copy the fixture and spawn no git, so a clone per arm would add git processes
  where it spends none: at least 38 against its 20 `cp` (PINNED, the builder's count, 2026-11-22).
  `tools/check-wiring.test.sh`, its `NEWREPO_SEED` included, is unit 10's. `tools/govkit/selftest.py` is unit 11's, which passes
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

Every citation is at `40def53f7`, the merge of main at `8b8b1374c` (dWitnessedBar's landing), by
symbol or as `<path>@<blob>:<line>`. Each cited blob is the same at `8688cdbba`, which adds records
only. None of `tools/lib/lib-selftest.sh`, `tools/lib/lib-selftest.test.sh`,
`tools/govkit/fixture_target.py`, `tools/check-line-length.test.sh` or `tools/check-wiring.test.sh`
moved in `59e882afd..40def53f7`.

### The seams today

- `build_fixture` runs a builder once into `$SELFTEST_ROOT/snapshot`, and `_st_run_one` copies it
  per arm with `cp -a` (`tools/lib/lib-selftest.sh#_st_run_one`). The copy is what makes the pool
  safe, by the file's own account, and it copies every object and every hook sample per arm.
- `tools/govkit/fixture_target.py#build_target` builds a target per call through
  `tools/govkit/fixture_target.py#build_scratch_gov`: an `init`, five `config` calls, an `add` and a
  `commit`, each a process. Two of the five pin `core.autocrlf false` and
  `core.hooksPath .git/hooks` in the repository's own config, which is why S4 keeps `core.*` pins.
- Two local templates already build once and copy per case: `NEWREPO_SEED` in
  `tools/check-wiring.test.sh@8d0af8c91b34:45`, copied with `cp -a` (`:51`), and `TEMPLATE` in
  `skills/session-kickoff/manifest-check.test.sh@c9fc270ea5c2:68`, copied with `cp -r` (`:74`).
- A bar's `$WORK` is a `gate-work.*` directory with an `owner` file, and its legs' `TMPDIR` is
  `$WORK/tmp` (`tools/run-gates/run-gates.sh#write_work_owner`,
  `tools/run-gates/run-gates.sh@2e851a92d9ce:2465`). Its trap removes it, and each later bar sweeps a
  dead one. Under a bar, `run-selftests.sh` makes its sweep root under that `TMPDIR` and gives each
  suite `TMPDIR="$d/tmp"` below it (`tools/run-gates/run-selftests.sh@c9d39e4a1284:1578`), so S2's
  ancestor walk from any suite reaches `$WORK`.
- The `selftest harness self-test` leg is declared as an `[[exempt_leg]]` row
  (`tools/govkit/registry.toml@5c649ae4f967:1640`), and `tools/gate-legs.json` is rendered from it.

### Why a reading case needs a declaration

A case's subject can write, and nothing in the harness can tell. So sharing a checkout is opt-in,
per arm, and S7 checks the claim after the run: a reading arm that wrote fails the suite rather than
leaking into its neighbours unseen.

### Why the clone drops its remote

A built fixture has no remote, and subjects read remotes. `check-wiring.sh` and `push-main.sh`
read them directly. Every reader of the policy kit reads one through its landed revision, which is
`refs/remotes/<remote>/<branch>` whenever a remote exists, and the local branch only when none does
(`tools/policy/policy.py#derive_landed_revision`). A clone left with `origin` would have that
reader grade the template's commit on the remote ref instead of the case's own commit on `main`.
A subject that seems to run `git rev-parse` alone can still reach the policy on one branch, as the
line-length gate does at its first breach (`tools/check-line-length.sh#read_line_mode`). So no caller can safely declare its subject remote-free, and
every clone drops the remote.

### Why the clone pins line endings for itself alone

`cp -a` copies bytes, and a checkout writes them through `core.autocrlf`, which a Windows git
install sets `true` globally. `build_scratch_gov`'s own comment records eight arms gone red on
that alone. A `-c` after `clone` would persist `core.autocrlf=false` into every case's config,
which a bash builder never set. A `-c` before `clone` governs that one process and its checkout,
and is gone after it.

### The consumers

The cache saves processes only where a suite builds a git repository per case today, since a clone
replaces that build. A suite whose arms copy a fixture with `cp -a` and spawn no git spends more
on the cache, which is why the line-length suite stays off it. The consumers are units 10 to 13:

- TOOL-dQuietDisk-10 moves `tools/check-wiring.test.sh`, folding its `NEWREPO_SEED` onto the bash
  face;
- TOOL-dQuietDisk-11 moves `tools/govkit/selftest.py`, passing a `TemplateCache` to `build_target`;
- TOOL-dQuietDisk-12 moves `.githooks/pre-push.test.sh` onto the bash face;
- TOOL-dQuietDisk-13 moves the `run-gates*.test.sh` suites onto the bash face.

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
`tools/lib/lib-selftest.test.sh` · `tools/govkit/fixture_target.py` · `tools/lib/resolve-python.test.sh` ·
`tools/policy/catalogue.toml` · `help/reference/policy.md` · `tools/govkit/registry.toml` ·
`tools/gate-legs.json` · `memory/guides/SESSION-KICKOFF.md` · `memory/project/shell-role.txt` ·
`memory/map/generated/symbols.json` ·
`memory/builds/dQuietDisk/build/<date>-build-TOOL-dQuietDisk-7-widen-<n>.md`

The guard lands in the `[[exempt_leg]]` row of `tools/govkit/registry.toml`, and
`tools/gate-legs.json` is its rendering (S6). The kickoff manifest's `watch:` line names
`tools/gate-legs.json`, so that commit also re-stamps the `last-audit` of
`memory/guides/SESSION-KICKOFF.md`. The widen record's name is the door's: its date is the day the
pass runs it and its number is one past the highest widen record in the build folder, which holds
three at this revision. The new module, the new shell file and `lib-selftest.sh` add column-0
definitions, so the codebase map's generator, run with `--write`, rewrites the symbol index. No leg,
kit or dossier is added, so the map's other generated files do not move, and a pass that sees one
move records it as a deviation.

### Shared paths at order 2

On the order-2 specs as they read at this re-ground, TOOL-dQuietDisk-5 shares three paths with this
unit: `memory/guides/SESSION-KICKOFF.md` (its `last-audit` re-stamp), `memory/project/shell-role.txt`
(its own widen) and `memory/map/generated/symbols.json`. So the two build in sequence, and the later
one's widen record takes the next number. TOOL-dQuietDisk-2, 3, 4 and 8 name no path of this unit's.
TOOL-dQuietDisk-2 and 3 grow shell files the ledger holds. Where their Files touched comes to name
the ledger, they share it with this unit and are sequenced with it too.

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
- perf / scale: a template costs one build per root. A mutating case costs one clone and one remote
  removal, three git processes in all, as S5 states. A reading case costs nothing after the first.
- error / empty / loading states: a failed build refuses as `build_fixture` refuses today, exit 2
  naming the builder. A failed clone fails that arm with the copy's existing `ERR` line.
- observability: `build_fixture --template` prints `template: <key8> built` or
  `template: <key8> reused` once.
- risks: two cases cloned from one template share its base commit id, where two built fixtures differ
  by their timestamps. An arm comparing commit ids across fixtures would read them equal; unit 11
  checks its arms for that. The gotcha `suite-invalidated-by-a-commit-under-it` does not reach the
  cache, because its root dies with the run. A builder that commits a `.gitattributes` with `text`
  or `eol` rules has each clone checked out through them, where `cp -a` copied bytes. The builders
  of this unit's own arms write none, and a consuming unit whose builder writes one re-checks its
  arms.
- testing: the arms `tools/lib/lib-selftest.test.sh` gains and the probes of section 6.
- migration: N/A — opt-in per suite; a suite that does not pass `--template` is unchanged.
- user docs: the policy key's help row is rendered from its catalogue row.

## 6. Acceptance criteria

- **AC1** — When a bash probe under `%TEMP%/<short-name>` sources `lib-selftest.sh` from
  `tools/lib/`, builds a fixture with `build_fixture --template` whose builder runs `git init` and
  `git config user.email t@t`, and clones it twice with `build_template_clone`, each clone's `git config
  user.email` prints `t@t`, `git remote` prints nothing, and its tracked files equal the builder's.
  The template's `.git/objects` holds every object, and neither clone's does: each holds an
  `objects/info/alternates` naming it. With `GIT_CONFIG_GLOBAL` naming a file that sets
  `core.autocrlf = true`, a builder file written with LF endings reads byte-identical in each clone
  (`cmp`), and `git -C <clone> config --local core.autocrlf` prints nothing.
  Red when: the clone copies objects, keeps `origin`, loses the builder's config, converts a line
  ending, or persists a pin the builder never set.
- **AC2** — When the probe calls `derive_template_key` for one builder with two input sets that differ by one
  byte of one input file, and for two builders whose names match but whose `declare -f` bodies
  differ, the four keys are distinct. The same builder and inputs give the same key twice.
  Red when: a key omits the definition or the inputs' blob ids.
- **AC3** — When a probe script under `%TEMP%/<short-name>` sources `lib-selftest.sh` from
  `tools/lib/` and declares three arms under `build_fixture --template`, whose builder commits an
  input file and whose subjects read it, two green and one red, it runs once with
  `tests.fixture-templates` at its default and once at `per-case`. Both runs print the same `ok`
  lines in the same order, and the same arm goes red. With one byte of the input file changed, the
  key moves, and in both modes the arm that reads it sees the new bytes.
  Red when: an arm's result differs between the modes, or a changed input reuses the old template.
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
  `core.hooksPath`, and no remote. With `GIT_TRACE2_EVENT` set, a second cached call costs three
  git processes, against the eight of an uncached call.
  Red when: the cached target differs in a config pin or carries `origin`.
  figure: DERIVED at observation for the uncached count; PINNED at three for the cached call, measured by the builder 2026-11-22.
- **AC8** — When the parity table's `blk` awk extracts `template_cache_sh` from `template-cache.sh`
  and from `lib-selftest.sh`, the two compare equal.
  Red when: the inline copy drifts by one byte, which the new `PARITY_ROWS` row then reports.
- **AC9** — A bash probe under `%TEMP%/<short-name>` builds the same base for each of a run of
  cases in two ways. The per-case way runs `git init`, two `git config` calls, `git add` and
  `git commit` in every case, the shape units 10 to 13 replace. The cached way runs one
  `resolve_template` and a `build_template_clone` per case. The base commits five files in two
  directories. Each way runs with `GIT_TRACE2_EVENT` naming its own empty directory and with
  `TEMP`, `TMP` and `TMPDIR` pointed at an empty directory sampled every 0.5 s. The cached way
  writes fewer trace files and reaches a lower peak entry count, and the residual is 0 for both
  once each way's root is removed.
  Red when: the cached way spends as many git processes or entries as the per-case way, or a
  template outlives the run.
  figure: DERIVED at observation, for both process counts and both peaks.
- **AC10** — When
  `python tools/gate-lint/sh_hygiene.py --shell-role memory/project/shell-role.txt .` runs after
  the widen, it prints `sh-hygiene: OK`. `grep -n -P '^tools/lib/template-cache\.sh\t' memory/project/shell-role.txt`
  prints one row ending `widened:<stem>`, and every other row `git diff -- memory/project/shell-role.txt`
  shows ends with that same stem and names a file this unit writes. The stem names a file under
  `memory/builds/dQuietDisk/build/` whose Keys field lists exactly the changed rows' paths, whose
  Caused-by is `TOOL-dQuietDisk-7`, and whose Reason gives the lines this unit adds per key.
  Red when: a row is edited by hand with no record, a row for a file this unit does not touch moves,
  or a grown key has no row.
- **AC11** — When `python tools/run-gates/leg_factory.py --check` runs, it exits 0.
  `grep -n -A16 '"name": "selftest harness self-test"' tools/gate-legs.json` prints a guard
  naming the python face S8 adds and the bash face S6 adds, each under the manifest's prefix
  token, beside the two paths it names today.
  Red when: the rendered manifest differs from the registry row, or an edit to either new file
  trips no leg holding its arms.

## 7. Gates

`selftest harness self-test` · `extract-arms self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `gate-leg conformance` · `policy check` · `policy fixtures` · `scratch-guard self-test` · `routed-commits selftest` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `testsuite counts (every bar self-test prints one)` · `portability (shell lines only shrink)` · `ratchet (never gains)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `line length`

New arm: tools/lib/lib-selftest.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC9 · the template mode's arms S10 names: a clone that copies objects or keeps its remote, two builders colliding on one key, a racing stage left behind, a reading arm that writes, and a suite whose result differs between the two values of the switch; each failing case is staged by that break in the harness · its FLOOR_ASSERTIONS rises by the arms added
New arm: tools/lib/resolve-python.test.sh · covers AC8 · the template_cache_sh row; its failing case is staged by one changed byte in the copy lib-selftest.sh carries · none

The bar runs once at the close. The harness suite's arms are the `New arm:` line's, observed RED
and then GREEN by the main loop at the close, because a role agent runs no suite, whichever kit
holds it. The pass makes the probes of AC3 and AC9. The leg line no longer names
`line-length gate selftest`, because the line-length suite leaves Files touched.

The leg line names `portability (shell lines only shrink)` and `ratchet (never gains)`, which grade
the ledger S11 widens, and `gate-leg conformance`, which grades the registry row S6 edits. None of
the three is guarded, so the guards join does not ask for them. It no longer names
`history-store selftest`: rev-3 added it for a bare `tools/lib/` in section 4, and section 4 now
names no path its guard holds.

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
- rev-3 · 2026-11-22 · §7 · under `2026-11-22-prompt-TOOL-dQuietDisk-1-divergence-2-task`. Section
  4 names `tools/lib/`, which trips the guard of `history-store selftest`, the leg TOOL-dQuietDisk-1
  adds, so §7's leg line names that leg.
- rev-4 · 2026-11-22 · wording only, under `2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task`. In section
  4 the one symbol citation naming the fixture-target module by its bare basename now names
  `tools/govkit/fixture_target.py`. Design, scope and acceptance unchanged.
- rev-5 · 2026-11-22 · S4 · S5 · S6 · S9 · S11 · §4 · §5 · AC1 · AC10 · AC11 · §7 · §10 ·
  re-grounded at 40def53f7 (order 1 built, dWitnessedBar landed), under
  `2026-11-22-prompt-TOOL-dQuietDisk-2-reground-task`. What moved: the run-gates `TMPDIR` export
  is now line 2465 and the manifest-check template line 68, and every citation is re-pinned to a
  blob. The harness, the fixture target and the two suites did not move. Re-reading the code moved
  four facts and the scope with them. (1) The guard's source is the `[[exempt_leg]]` row in
  `tools/govkit/registry.toml`, rendered by `leg_factory.py --write`, so S6 and Files touched name
  the registry and AC11 observes the rendering. (2) `memory/project/shell-role.txt` is shrink-only,
  and this unit adds a shell file and grows three, so S11 widens them through the door
  TOOL-dQuietDisk-1 used, and §7 names the two legs that grade the ledger. (3) `build_scratch_gov`
  pins `core.autocrlf` and `core.hooksPath` in local config, which S4's old `core.*` exclusion
  dropped against AC7, so S4 now excludes only the keys git writes at init. (4) A clone checks out
  through the global `core.autocrlf` where `cp -a` copied bytes, so S5 pins it for the clone
  process alone and AC1 observes the bytes. Files touched also gains the symbol index, and §4
  names the three paths shared at order 2, all with TOOL-dQuietDisk-5. §7 also drops
  `history-store selftest`, which no path of section 4 trips any longer. No goal moved.
- rev-6 · 2026-11-22 · §1 · S1 · S5 · S7 · S8 · S9 · S10 · S11 · §3 · §4 · §5 · AC3 · AC7 · AC9 · §7 ·
  under `2026-11-22-prompt-TOOL-dQuietDisk-7-divergence-task`, the first build pass's probe of
  rev-5, ruled. (1) Every clone drops its remote, and keep-remote is gone: the line-length gate
  reaches the policy kit, whose landed revision follows the remote. (2) `build_fixture` gains
  `--template` alone, and `build_clone` takes no keep option. (3) A cached clone costs three git
  processes, `git-upload-pack` included, in S5, S8 and AC7. (4) The line-length suite stays on
  `cp -a`, since a clone per arm costs it git processes it does not spend, so it leaves Files
  touched, scope and §7. S10 is now the harness suite's own proving arms, AC3 and AC9 are probes
  those arms re-observe, and section 4 names units 10 to 13 as the consumers. (5) S9's bash face finds
  python by sourcing `tools/lib/resolve-python.sh`. (6) S1's bash rename is `mv -T`. The goal does
  not move; §1 drops only the line-length suite as its proof.

## 10. Reuse audit

The seams extended: `tools/lib/lib-selftest.sh`'s `build_fixture` and `_st_run_one`, whose snapshot
becomes a template, `tools/govkit/fixture_target.py#build_target`, which gains the cache, the
copy rule of `PARITY_ROWS` (`tools/lib/resolve-python.test.sh@2a7b736449e3:405`), the bar's owned
`$WORK` (`tools/run-gates/run-gates.sh#write_work_owner`), which S2 finds rather than re-creates,
and the ledger factory's widen door that TOOL-dQuietDisk-1 used, which S11 calls as it is. The
local templates of `tools/check-wiring.test.sh` and `skills/session-kickoff/manifest-check.test.sh`
are the shape S1 generalises; their suites move in other units.

`python tools/codebase-map/reuse_lookup.py "build a fixture repository once and clone it per test case"`
ranked `build`, `fixture`, `build_records`, `run_selftest_cases`, `run_fixture_git` and
`write_fixture_files`. `run_fixture_git` is a git runner for fixtures in five files and builds no
template; `run_selftest_cases` in `tools/loop/loop_lib.py` runs cases and builds none. No existing
seam clones a template.

Recall returned TOOL-aSparedSpawn-9, which built `NEWREPO_SEED` once and copied it per call, and
TOOL-aQuenchedHarness-5, the harness's own spec, whose per-arm copy this unit replaces with a clone.
The owning chain build is dWitnessedBar (Test: gate health and budgets), now landed. Re-read at
this re-ground, `git log 59e882afd..8b8b1374c` holds no commit to `tools/lib/lib-selftest.sh`,
`tools/govkit/fixture_target.py` or `tools/check-line-length.test.sh`. Of its specs, only
TOOL-dWitnessedBar-55 and -109 name `build_target` or a `build_fixture`. The first builds its
targets through `build_target` unchanged, and the second's `build_fixture` is
`tools/memory-tree/routed_commits.py`'s own. Neither changes either seam, so no unit of it did any
of this unit's work and there is nothing of it to extend.

Recall terms used: fixture template snapshot build_fixture lib-selftest build_target fixture_target newrepo seed clone shared
