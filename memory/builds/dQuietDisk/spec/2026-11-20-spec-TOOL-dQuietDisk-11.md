# TOOL-dQuietDisk-11 — govkit's scratch targets come from the template cache, so `selftest.py` builds each distinct target once

**Status:** CLOSED · rev-4 · 2026-11-22 · node d · Tier-2 · base c3c0811b · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 TOOL-dQuietDisk-36 TOOL-dQuietDisk-37 |
| [2026-11-22-build-TOOL-dQuietDisk-11-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dQuietDisk-11-1-acceptance-ledger.md) | journal | — |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-11-1-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-11-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-11-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-11-build-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-11-reground-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-11-reground-task.md) | research | TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-26 |
| [2026-11-22-review-TOOL-dQuietDisk-1-closing-diff-review-round1.md](../reviews/2026-11-22-review-TOOL-dQuietDisk-1-closing-diff-review-round1.md) | diff-review | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-16 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/govkit/selftest.py` builds a scratch target per `build_target` call, and 70 of its calls
[DERIVED, the section 4 walk at `c3c0811b8`] fall in seven argument sets that recur, each build
spending 9 git processes [PINNED, measured 2026-11-22]. This unit passes TOOL-dQuietDisk-7's
`TemplateCache` to those calls, so each recurring target is built once per run and cloned per call,
with every arm's verdict unchanged.

## 2. Scope (IN)

- **S1** — One cache per run. `selftest.py` loads `TemplateCache` from
  `tools/lib/template_cache.py` by path through `importlib.util.spec_from_file_location`, the way it
  already loads its other modules (`tools/govkit/selftest.py@71cc88c0dcb2:160`). It binds a module
  constant `TEMPLATES = None`. `main` sets it to `TemplateCache(root=tmp / "templates")` right after
  it makes its scratch root (`tools/govkit/selftest.py@71cc88c0dcb2:6425-6426`). The face's own
  root order stands: `SELFTEST_TEMPLATE_ROOT`, else a bar's owned `gate-work.*`, else that argument
  (`tools/lib/template_cache.py#TemplateCache`). Observed by AC2 and AC6.
- **S2** — The opt-in. A `build_target` call passes `template=TEMPLATES` when its `(deploy, files)`
  source text recurs at another call and its `deploy` is not a parameter of its enclosing function.
  At `c3c0811b8` that is 70 calls [DERIVED] over seven sets, tabled in section 4. No other call
  passes it. Observed by AC1.
- **S3** — The per-call path is unit 7's as built. With a cache whose switch reads `shared`,
  `build_target` resolves the template once per key and returns its `build_clone`
  (`tools/govkit/fixture_target.py#build_target`). With `TEMPLATES` at `None`, or a switch at
  `per-case`, it builds per call as today. This unit writes no line of `fixture_target.py` or
  `template_cache.py`. Observed by AC2, AC3 and AC4.
- **S4** — A liveness arm. Right after the first opt-in call in `main`, one `check` labelled
  `[dQuietDisk-11] a recurring target is a clone of its template` holds two things: `TEMPLATES` is
  set, and the target carries `.git/objects/info/alternates` exactly when `TEMPLATES.mode` reads
  `shared`. Observed by AC5.
- **S5** — The leg's guard. The `govkit selftest` leg's guard gains an entry for
  `tools/lib/template_cache.py`, spelled under the `{prefix}` token as its siblings are. It lands in
  its row of `tools/govkit/registry.toml` (`tools/govkit/registry.toml@ce589cc09912:796-811`) and in
  `tools/gate-legs.json` (`tools/gate-legs.json@c45520cdd326:2507`), as unit 7 widened the harness
  leg's. The suite now reads that file, and `tools/run-gates/py_reads.py`'s import walk cannot see a
  load by path: its docstring names a `dynamic` row of the walk as unread
  (`tools/run-gates/py_reads.py@19b628883a3c:22-26`). The kickoff manifest watches
  `tools/gate-legs.json`, so the commit re-stamps its `last-audit`. Observed by AC7.
- **S6** — The saving is counted, and every arm keeps its verdict. Observed by AC6.

## 3. Non-goals (OUT)

- `build_scratch_gov`. `selftest.py` calls it once [DERIVED, the section 4 walk], so nothing
  recurs, and unit 7 built no cached branch for it.
- The 29 calls [DERIVED] whose set occurs once. A template used once costs 4 more git processes and
  27 more entries [DERIVED] than the build it replaces.
- The four calls [DERIVED] whose `deploy` is a parameter: `run_fixture` twice, `check_roles_install`
  and `stale_target`. Whether their values recur is decided at runtime, which the source text cannot
  show.
- The other callers of `build_target`: `tools/govkit/docs_leg.py`, `tools/govkit/upgrade_walk.py`,
  `tools/govkit/upgrade_steps.py` and the two fixture modules under `tools/govkit/fixtures/`. Each
  passes no cache and builds per call as today.
- The 60 inline `"init"` sites [DERIVED, `grep -c '"init"'` at `c3c0811b8`] of `selftest.py`, each
  building a distinct base in a local helper.
- A hand-made copy without objects: backlog ask TOOL-dQuietDisk-32 (section 4, Alternatives
  rejected).
- The clone of gov the suite makes for its walk: TOOL-dQuietDisk-8. Tree removal handlers:
  TOOL-dQuietDisk-9.
- `tools/run-gates/adopt-run-gates.test.sh`'s own bash `build_target`, a different function.
- A direct run killed mid-way. Its `TemporaryDirectory` and the templates in it stay behind, as its
  targets do today. Under a bar the templates sit under the owned `$WORK`, which the next bar sweeps.

### Edges

- **consumes-from** `TOOL-dQuietDisk-7` — `TemplateCache` and `build_target`'s `template` keyword
  as built at `360d706f6`, whose cached call costs one clone. Without it there is nothing to pass.
- **hands-off** `TOOL-dQuietDisk-19` — the `selftest.py` readings, held to this unit's bound.

## 4. Design

### Where the code was read

Every citation is at `c3c0811b8`, by symbol or as `<path>@<blob>:<line>`. TOOL-dQuietDisk-18's
arms in `selftest.py` (`87bd02fec`, `e8f0e7d31`) add no `build_target` call: their targets come
from the suite's local `runner_target`.

### What a call costs, measured

A probe imported `tools/govkit/fixture_target.py` and `tools/lib/template_cache.py` and called
`build_target(tmp, deploy_text, name)` under `GIT_TRACE2_EVENT=<absolute dir>`, counting the trace
files per call. It counted every file and directory under each result with `os.walk`.

| Shape | Git processes | Entries |
|---|---|---|
| Today's build | 9 [PINNED] | 31 [PINNED] |
| Template build, once per key | 10 [PINNED] | 34 [PINNED] |
| Cached clone, each call | 3 [PINNED] | 24 [PINNED] |
| `TemplateCache()` and its switch read, once per run | 3 [PINNED] | 0 [PINNED] |

All figures were measured 2026-11-22 with git 2.54.0.windows.1. Today's ninth process is the
commit's `git maintenance run --auto`. The clone's three match TOOL-dQuietDisk-7 rev-6 AC7. A
trace directory given as a relative path counts nothing, because each `git -C` resolves it in the
target.

### The opt-in population

An AST walk of `selftest.py` groups every `build_target` call by the source text of its `deploy`
and `files` arguments. It finds 103 calls [DERIVED] in 37 groups [DERIVED]. Seven groups recur
without a parameter `deploy`:

| `deploy` | `files` | Calls |
|---|---|---|
| `None` | none | 26 [DERIVED] |
| `DEPLOY_FULL` | none | 26 [DERIVED] |
| the `demo` kit at the `PFX` prefix, an f-string | none | 7 [DERIVED] |
| `SAFE_DEPLOY` | none | 4 [DERIVED] |
| the `demo` kit at prefix `pinned` | none | 3 [DERIVED] |
| `OWN_DEPLOY.format(...)` | none | 2 [DERIVED] |
| `DEPLOY_FULL` at prefix `scripts` | none | 2 [DERIVED] |

Each of the 70 sites names its own destination. 67 [DERIVED] of them take the default name under a
distinct `tmp / <tag>`. Ten of the enclosing functions are local builders the suite calls more than
once, so 70 is a floor on the calls made at runtime. The same text gives the same value here,
because every name in the table is a module constant. Where two texts give one value, the cache
keys by value and saves more.

### The saving

The 70 calls cost 630 git processes today [DERIVED, 70 × 9]. On the cache they cost 70 for seven
templates, 210 for the clones and 3 for the switch read: 283 [DERIVED]. That is 347 fewer [DERIVED]
per full run, more where a local builder repeats. Entries held fall from 2,170 [DERIVED, 70 × 31]
to 1,918 [DERIVED], seven templates of 34 and 70 clones of 24: 252 fewer [DERIVED] while every
target lives. The targets under `main`'s root live until it closes, and those under a nested root
close earlier, so the peak saving is at most 252.

### What the clone changes, and why no arm reads it

A probe compared a cloned target with a built one, each with no `files` and with a `deploy` text.
`git status --porcelain`, `git show -s --format=%T%x20%s HEAD` and `git config --local --list` read
identical, and `git fsck` exits 0 on both. The clone differs in three places no govkit path reads:

- It carries `.git/objects/info/alternates`. `govkit.py`, `selftest.py` and `upgrade_steps.py` hold
  no `alternates` reader, by grep at `c3c0811b8`.
- Its `HEAD` reflog opens with a clone line. None of the three reads a reflog or `@{`, by grep.
- Every clone of one key holds the same commit, where two builds in different seconds hold two.
  None of the three reads a commit time (`%ct`, `%at`, `%cI` or `--since`, by grep). Two builds in
  the same second already share a commit today.

A destination that exists and is not empty fails the clone with `OSError` naming the argv, where
today's build initialised into it. A probe saw the clone take an empty destination and create a
missing parent, as today's `mkdir(parents=True)` does. AC6's full run is the observation that no
opt-in site writes its destination before the call.

### Concurrency

The face names its stage `.stage-<key>-<pid>`, so two threads of one process building one key
would share a stage. No `build_target` call runs on a thread at `c3c0811b8`. The suite's four
`ThreadPoolExecutor` blocks run `apply` or a case runner over targets already built
(`tools/govkit/selftest.py@71cc88c0dcb2:8310`, `:20717`, `:20763` and `:20826`). Separate
processes under a bar rename into place as the face's protocol states.

### Order

TOOL-dQuietDisk-18 wrote arms into `selftest.py`, and it is CLOSED at `87bd02fec`. This unit edits
call sites beside those arms and none of them. Of the other order-4 units, none shares a file with
this one except TOOL-dQuietDisk-15, whose Files touched also names the kickoff manifest's
`last-audit` re-stamp. The two restamp one line, so they commit in sequence and the later one
re-stamps over the earlier. TOOL-dQuietDisk-16 writes `tools/govkit/govkit.py` and
`tools/govkit/upgrade_steps.py`, and TOOL-dQuietDisk-26 writes the check-wiring pair; neither
touches a path here.

### Files touched (estimate)

`tools/govkit/selftest.py` · `tools/govkit/registry.toml` · `tools/gate-legs.json` ·
`memory/guides/SESSION-KICKOFF.md` (its `last-audit` re-stamp)

No generated file moves: the symbol index records functions and classes, and this unit adds
neither. The switch's catalogue row already covers a self-test that opts in
(`tools/policy/catalogue.toml@3c136d9f8dbe:1815-1820`), so no row changes and no `help/` page
re-renders.

### Alternatives rejected

| Option | Why not |
|---|---|
| Pass the cache at every call | The 29 single-set calls would cost 116 more git processes and 783 more entries [DERIVED], so peak entries would rise. |
| Re-bind `build_target` once in `selftest.py` to a partial carrying the cache | It is the same as passing it at every call, with a second meaning for one name. |
| A copy of the template without objects, borrowing through `alternates` | It would save 557 git processes and 392 entries [DERIVED], against 347 and 252. It is a new hand-out verb on the cache, which backlog ask TOOL-dQuietDisk-32 files as its own unit. When it lands, `build_target`'s shared branch takes it and these 70 sites need no edit. |
| Cache `build_scratch_gov` | One call, so nothing recurs. |

## 5. Production-readiness checklist

- security: N/A. No new write path: each clone lands at the destination its caller names, and each
  template under the face's root.
- perf / scale: at least 347 fewer git processes and up to 252 fewer entries per full run
  [DERIVED, section 4].
- error / empty / loading states: a failed template build or clone raises `OSError` naming the argv
  (`tools/lib/template_cache.py#run_git`), which fails the arm that called it, as a failed build
  does today (`tools/govkit/fixture_target.py#run_git`).
- observability: the S4 arm prints one `ok` line on each run.
- risks: a template built while a commit moves the tree
  (`memory/gotchas/suite-invalidated-by-a-commit-under-it.md`). The builder reads no tracked file,
  and its key holds `fixture_target.py`'s own bytes, so neither a commit nor a builder edit can hand
  out a stale template.
- testing: AC1 to AC5 and AC7 are probes. AC6 is the main loop's full run.
- migration: N/A. Templates live for one run.
- user docs: N/A. Test fixtures, which no `help/` page describes.

## 6. Acceptance criteria

- **AC1** — When a probe parses the govkit suite's source with `ast` and groups each `build_target`
  call by the source text of its `deploy` and `files`, every call in a group of two or more whose
  `deploy` is no parameter of its function passes `template=TEMPLATES`, and no other call does.
  Red when: a recurring call builds per call, or a single-set call pays for a template.
  figure: the 70 calls and seven groups are DERIVED by this walk at observation.
- **AC2** — When a probe builds `build_target(tmp, deploy, name)` for each of the seven sets, once
  with `template=None` and once with a `TemplateCache` whose switch reads `shared`,
  `git ls-files -s`, `git status --porcelain`, `git config --local --list` and
  `git show -s --format=%T%x09%s HEAD` read byte-identical across each pair, and
  `git remote` prints nothing for the cached one.
  Red when: a cached target differs from a built one in any read, or carries `origin`.
- **AC3** — When the same probe counts `GIT_TRACE2_EVENT` files under an absolute directory, a
  second cached call for one set adds 3, and an uncached call adds 9.
  Red when: a repeated set builds again.
  figure: 3 PINNED by TOOL-dQuietDisk-7 rev-6 AC7; 9 PINNED, measured 2026-11-22.
- **AC4** — When the probe points `GIT_CONFIG_GLOBAL` at a planted config that signs with a failing
  program, sets `core.hooksPath` to a canary hook and names an `init.templateDir` holding one, and
  then calls `build_target` twice for one set with a `TemplateCache`, both clones hold `base` at
  `HEAD`, no canary file is written and no `.git/hooks/pre-commit` exists in either.
  Red when: a planted global config reaches a cached target.
- **AC5** — When the probe runs the S4 arm's predicate on a target cloned under `shared` and on one
  built under `per-case`, it holds for both. It fails with the cache left at `None`, and on a built
  target paired with a cache that reads `shared`.
  Red when: the arm passes on a suite that passes no cache.
- **AC6** — When the main loop runs `tools/lib/extract-arms.sh` over the `govkit selftest` leg at
  the build base and at this unit's commit, each in a scratch `git clone --shared` with
  `GIT_TRACE2_EVENT`, `TEMP`, `TMP` and `TMPDIR` pointed at scratch dirs, both inventories hold the
  same check labels with the same verdicts, plus the S4 arm's one label. The git process count falls
  by at least 347, the peak temp entries are below the base's, and residual temp entries are 0
  both times.
  Red when: a check changes verdict, the count does not fall by the bound, the peak does not fall,
  or an entry remains.
  permission: a role pass may not run the deployer's suite (`tools/unattended/gate-guard.js` row D4,
  `tools/hooks/scratch-guard.js` row G3); the main loop observes this at VERIFYING.
  cost: two full runs of the deployer's suite.
  figure: 347 is DERIVED from section 4's measured per-call costs and the AC1 walk.
- **AC7** — When a probe reads the `govkit selftest` row from `tools/gate-legs.json` and from
  `tools/govkit/registry.toml`, both guards list `tools/lib/template_cache.py` under the `{prefix}`
  token and are otherwise unchanged from `c3c0811b8`.
  Red when: either guard lacks the file, or the two disagree.

## 7. Gates

`govkit selftest` · `policy fixtures` · `recall floor arms` · `govkit refusal join` · `govkit acceptance matrix` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `recall floor`

New arm: tools/govkit/selftest.py · covers AC5 · leaving `TEMPLATES` at `None` while the switch reads `shared` reds it · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft. Ordered 4, not the roster's 3: TOOL-dQuietDisk-18 writes
  `tools/govkit/selftest.py`, which this unit's AC5 reads, and the spec brief orders this unit after
  18 when both touch the file. TOOL-dQuietDisk-19 at order 4 reads this unit's output.
- rev-2 · 2026-11-22 · under `2026-11-22-prompt-TOOL-dQuietDisk-1-divergence-task`. Section 4's sketch
  spells unit 7's python face as TOOL-dQuietDisk-7 rev-2 renames it, `resolve_template`, and the copy
  as `shutil.copytree`, in place of the placeholders `template_path` and `copy_template`, which the
  lexicon would refuse. AC4 had the pass run the module's `--selftest`; it now has the pass run a
  planted-config probe, the module's own run is owed to the main loop, and the `New arm:` line
  covers AC4.
- rev-3 · 2026-11-22 · wording only, under `2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task`. In section
  4 and section 10 the repeated-call count is marked DERIVED from the AST walk's two counts,
  dWitnessedBar's changed-line count PINNED, and the ordering note's build-method citation names its
  tag. Design, scope and acceptance unchanged.
- rev-4 · 2026-11-22 · §1 §2 §3 §4 §5 §6 §7 §10 · S1 to S6 · AC1 to AC7 · re-grounded at c3c0811b8
  (orders 1 to 3 built), under `2026-11-22-prompt-TOOL-dQuietDisk-11-reground-task`. Unit 7 built
  the cached path into `build_target` itself, a `template` keyword handing out a three-process
  clone, so this unit no longer edits `fixture_target.py` and passes the cache from `selftest.py`.
  The copy of rev-3 is dropped: its full `copytree` adds entries, and an objectless copy is backlog
  ask TOOL-dQuietDisk-32's own unit. The calls opt in per site, 70 over seven sets, because the 29
  single-set calls would raise peak entries. `build_scratch_gov` leaves scope, with one call. The
  saving is re-taken by a probe at 347 git processes and up to 252 entries, against the 504 derived
  before. The `govkit selftest` guard gains `tools/lib/template_cache.py`, which brings the
  registry, the leg manifest and the manifest re-stamp into Files touched, and the re-stamp is
  shared with TOOL-dQuietDisk-15. The rev-3 `fixture_target.py` arm is replaced by one in
  `selftest.py`. The goal is unchanged.

## 10. Reuse audit

The seam is `tools/govkit/fixture_target.py#build_target`'s `template` keyword and
`tools/lib/template_cache.py#TemplateCache`, both built by TOOL-dQuietDisk-7 for this consumer,
which its edges hand off to this unit. This unit extends them by passing the cache, and adds no
function. The opt-in per site follows TOOL-dQuietDisk-12, whose repeated sets opt in and whose
single-use calls stay as they were. The guard widening follows unit 7's own for the harness leg.
`python tools/codebase-map/reuse_lookup.py "pass a template cache to repeated scratch target builds and clone each case"`
ranked `build_target` and `build_scratch_gov` in `tools/govkit/fixture_target.py` as seams, beside
`build_fixture` in `tools/lib/lib-selftest.sh`, which unit 7 generalised. The recall below found
backlog ask TOOL-dQuietDisk-32, the objectless hand-out, which decides the per-call shape.

Chain owner: dWitnessedBar (Test). The deployer is dSafePassage's area, and its CLOSED unit 5 made
`fixture_target.py` the one factory per kind (S12). This unit keeps that contract, since each call
still returns a repository at the destination it names holding the same files, refs and config.
`govkit` ships to no target (`tools/govkit/selftest.py@71cc88c0dcb2:73-77`), and its leg row is an
`exempt_leg` that travels nowhere, so no adopter receives this change and no adopter fixture or
`govkit check` reading applies.

Recall terms used: `python tools/memory-recall/query.py "how does govkit selftest take its scratch targets from the template cache" --terms "TemplateCache build_target template_cache build_clone alternates objectless copy fixture-templates selftest govkit"`
