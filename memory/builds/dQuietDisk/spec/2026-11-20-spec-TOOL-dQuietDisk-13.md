# TOOL-dQuietDisk-13 — the run-gates suites build each repeated scratch repository once and clone it per arm, where a clone saves

**Status:** CLOSED · rev-4 · 2026-11-22 · node d · Tier-2 · base 7b8c737b · streams tooling · order 3 · ratified 2026-11-22

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 TOOL-dQuietDisk-36 TOOL-dQuietDisk-37 |
| [2026-11-22-build-TOOL-dQuietDisk-13-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dQuietDisk-13-1-acceptance-ledger.md) | journal | — |
| [2026-11-22-build-TOOL-dQuietDisk-13-deviation-1.md](../build/2026-11-22-build-TOOL-dQuietDisk-13-deviation-1.md) | deviation | — |
| [2026-11-22-build-TOOL-dQuietDisk-13-widen-10.md](../build/2026-11-22-build-TOOL-dQuietDisk-13-widen-10.md) | widen | — |
| [2026-11-23-build-TOOL-dQuietDisk-1-runlog-c9768b47.md](../build/2026-11-23-build-TOOL-dQuietDisk-1-runlog-c9768b47.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-14 TOOL-dQuietDisk-16 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 TOOL-dQuietDisk-36 TOOL-dQuietDisk-37 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-13-1-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-13-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-13-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-13-build-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-6-reground-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-6-reground-task.md) | research | TOOL-dQuietDisk-6 TOOL-dQuietDisk-10 TOOL-dQuietDisk-12 TOOL-dQuietDisk-18 |
| [2026-11-22-review-TOOL-dQuietDisk-1-closing-diff-review-round1.md](../reviews/2026-11-22-review-TOOL-dQuietDisk-1-closing-diff-review-round1.md) | diff-review | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-14 TOOL-dQuietDisk-16 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 |

<!-- /gen:spec-records -->

## 1. Goal

The turnstile suite rebuilds the same scratch repository on 70 builder calls a run, and keeps every
one until it exits. This unit builds each of its two repository shapes once per run through
TOOL-dQuietDisk-7's template cache and gives each call a `--shared` clone, so the suite passes the
same arms with the same RED and GREEN results. The saving: 67 fewer git processes per run, and
about 1,200 fewer temp entries standing at its peak, both DERIVED in the design's inventory and
measured at the close. The evidence and canary suites stay per call, because a clone there saves
fewer git processes than the cache costs, or raises the peak temp entries it would have to lower.

## 2. Scope (IN)

- **S1** — `tools/run-gates/run-gates.turnstile.test.sh`: `mk_repo`
  (`tools/run-gates/run-gates.turnstile.test.sh@340ddcac21f2:343`) keeps its head, which clears
  the host beacon and queue every arm reads, then hands its destination a `build_template_clone`
  of the template that `_build_mk_repo` builds. `_build_mk_repo <dir>` is the rest of today's
  body, moved and not edited. Observed by AC1 and AC2.
- **S2** — `build_docs_repo` (`tools/run-gates/run-gates.turnstile.test.sh@340ddcac21f2:1545`)
  becomes `mk_repo "$1" _build_docs_repo`, so its two-commit shape is its own template.
  `_build_docs_repo <dir>` is `_build_mk_repo` followed by today's `NOTES.md` commit. Observed by
  AC1 and AC2.
- **S3** — A call whose destination already holds `.git` runs its builder over it, as today,
  whatever the switch, because a clone needs an absent or empty destination. The second signal
  loop builds over the first loop's three repositories
  (`tools/run-gates/run-gates.turnstile.test.sh@340ddcac21f2:987`). Observed by AC1.
- **S4** — The key and the root. Each builder's key is `derive_template_key <builder>` over five
  inputs named under `$ROOT`: the runner, `gate-profiles.txt`, `gate-fingerprint.sh` and
  `resolve-python.sh` where each is a file, and the suite file itself. Each key and template path
  is resolved once per builder per run and held in a shell variable. The root is
  `resolve_template_root` with `SELFTEST_ROOT=$tmp`, so a direct run's templates sit under the
  suite's own trapped scratch and a bar's under its owned `$WORK`. Observed by AC1 and AC3.
- **S5** — The switch, `tests.fixture-templates`, read once per suite run through
  `read_template_mode`. At `per-case` every call runs its builder, as today. Observed by AC5.
- **S6** — `read_template_mode <python> <policy.py>` joins the canonical `template_cache_sh` block
  in `tools/lib/template-cache.sh`. It prints `per-case` when `<python> <policy.py> get
  tests.fixture-templates` prints exactly that, and `shared` on any other answer, on an empty
  `<python>`, on a missing `<policy.py>` or on a failed launch. The block's inline copy in
  `tools/lib/lib-selftest.sh` carries it byte-identical, under the existing `template_cache_sh` row
  of `PARITY_ROWS` (`tools/lib/resolve-python.test.sh@76c8f4628980:447`), which names the marker and
  the two paths and so does not move. `build_fixture`'s own read
  (`tools/lib/lib-selftest.sh@4d0ce956a80b:172-185`) calls it, keeping its resolver, its
  `refuse_wrong_shell` and its policy path. Observed by AC5 and AC7.
- **S7** — The rows of the turnstile suite, `tools/lib/template-cache.sh` and
  `tools/lib/lib-selftest.sh` in the shell-line ledger are widened through the ledger factory's door,
  never hand-edited. Observed by AC6.
- **S8** — The arm set, its verdicts and the saving are observed on the whole suite. Observed by
  AC4.

## 3. Non-goals (OUT)

- `tools/run-gates/run-gates.evidence.test.sh`. Its arms hold one fixture at a time, each removed
  by `rec_done` or `ru_done`, so two standing templates of about 57 entries each raise its peak by
  more than one clone's saving of about 20 lowers it (DERIVED from the probe figures in the
  design). It would save 37 git processes a run: `rec_repo` 21, `ru_repo` 24, less the switch
  read's 8. A clone has no remote (`tools/lib/template-cache.sh#build_template_clone`), so both
  builders would re-run their `remote add`, `update-ref` and `symbolic-ref` per call.
  `fresh_gitdir` is a bare repository, which the factory does not build.
- `tools/run-gates/run-gates.test.sh`, the canary. Its 17 `build_hv_repo` calls would save 6 git
  processes, against the 8 the switch read costs (DERIVED in the design).
- `tools/run-gates/run-gates.gov.test.sh`, which holds three `mktemp -d` scratch directories and no
  `git init`, clone or worktree at `7b8c737b0`. `tools/run-gates/run-gates.runlog.test.sh`, which
  builds its one repository once (`build_scratch`).
- A hand-made copy of a template that shares its objects without a clone, which would cost no git
  process per call. It is a new hand-out verb on a CLOSED factory, filed by the main loop as ask
  TOOL-dQuietDisk-32; the design's alternatives give its figures.
- The nested bars the arms run. Each is the subject under test, and the runner's fixed cost is K9,
  which the prompt does not ask for.
- The sweep after a kill. The templates sit under the suite's `$tmp`, which its EXIT trap clears as
  it clears every fixture today; a scratch root a kill leaves is TOOL-dQuietDisk-9's.
- The factory's key composition, its root rule, its clone and its switch's catalogue row:
  TOOL-dQuietDisk-7. This unit adds only the reader S6 names.

### Edges

- **consumes-from** `TOOL-dQuietDisk-7` — the bash face `resolve_template_root`, `derive_template_key`, `resolve_template` and `build_template_clone` in `tools/lib/template-cache.sh`, and the switch key `tests.fixture-templates`. Without them there is no template to clone.

## 4. Design

### Inventory at `7b8c737b0`

| Builder | Calls | git per call today | git after, per call | Today | After | Saved |
|---|---|---|---|---|---|---|
| `mk_repo` | 59 | 4 | 3 fresh (56), 4 onto a repository (3) | 236 | 191 | 45 |
| `build_docs_repo` | 11 | 7 | 3 | 77 | 47 | 30 |
| the switch read | 1 | 0 | 8 | 0 | 8 | -8 |

Calls are counted from the call sites at `7b8c737b0`, each signal loop at its three iterations.
`mk_repo` has 55 call sites (PINNED, counted at `7b8c737b0` on 2026-11-22).
Its 59 calls are those sites with each signal loop's two extra iterations (DERIVED).
Its 56 fresh destinations are those calls less the second loop's three (DERIVED).
A builder's after cost is its key's 2
git processes, one template build, and a clone per call: the template build is the builder's own
processes plus the 5 the face adds (`git add`, `commit`, `rev-parse`, `diff --cached`,
`config --local --list`). The suite saves 67 git processes per run. DERIVED from those counts.

The per-command figures are PINNED, measured in a scratch repository by `GIT_TRACE2_EVENT` file
count on 2026-11-22 under git 2.54.0.windows.1, with the suite's own `GIT_CONFIG_COUNT` and identity
exported:

| Act | git processes | Entries |
|---|---|---|
| `init`, `add`, `commit`, as `mk_repo` builds; `commit` spawns `git maintenance run --auto` | 4 | 54 |
| `build_docs_repo`'s shape built | 7 | 61 |
| `derive_template_key` with input files | 2 | 0 |
| `resolve_template` building the `mk_repo` shape | 9 | 57 under its key |
| `resolve_template` on a built key | 0 | 0 |
| `build_template_clone` of either shape | 3 | 34, or 35 for the docs shape |
| `policy.py get tests.fixture-templates` | 8 | 0 |

Every repository the suite builds stands until its EXIT trap: no arm clears an `R` directory. So the
peak falls by about 20 entries per fresh `mk_repo` clone and 26 per docs clone, less the two
templates, about 1,200 in all. DERIVED from the table; the close measures it.

### The call half

The shape, not the text:

```bash
mk_repo() { # <dir> [<builder>] — a scratch repository carrying the runner and its table
  local d=$1 b=${2:-_build_mk_repo} v t
  rm -rf "$GATE_TURNSTILE_DIR"/gate-bar-beacon "$GATE_TURNSTILE_DIR"/gate-bar-beacon.* \
         "$GATE_TURNSTILE_DIR/gate-bar-queue" 2>/dev/null
  if [ "$TS_TEMPLATES" != shared ] || [ -e "$d/.git" ]; then "$b" "$d"; return; fi
  v=TS_TEMPLATE$b; t=${!v:-}
  if [ -z "$t" ]; then
    t=$(resolve_template "$TS_TEMPLATE_ROOT" "$(derive_template_key "$b" "${TS_TEMPLATE_INPUTS[@]}")" "$b" .) \
      || return 1
    printf -v "$v" '%s' "$t"
  fi
  build_template_clone "$t" "$d" >/dev/null 2>&1
}
build_docs_repo() { mk_repo "$1" _build_docs_repo; }
```

The prologue, after `LIB_DIR` and `$tmp` are set, sources `"$ROOT/$LIB_DIR/template-cache.sh"`, as
`tools/check-line-length.test.sh` sources `lib-selftest.sh` from gov's lib dir. The suite is
`project-owned` (`tools/run-gates/kit.toml@eb6f4f2b5706:45-46`), so no install carries it and no
inline copy is owed. The prologue sets `TS_TEMPLATE_ROOT` and `TS_TEMPLATE_INPUTS` once, and
`TS_TEMPLATES` from `read_template_mode "$_rkd_py" "$ROOT/<policy dir>/policy.py"`. The policy dir
is `resolve_kit_dir "$_rkd_py" policy policy.py "$HERE"`, as the suite already finds its lib dir; it
spends no git process (probed 2026-11-22), and a refusal leaves an empty dir, so the reader prints
`shared`. A failed key or build returns 1 from `mk_repo`, which the first call site already turns
into exit 2. The face's one `template: <key8> built` line per builder reaches the suite's stderr; it
is no arm line.

### The switch reader

The shape, not the text, inside the `template_cache_sh` markers of both carriers:

```bash
read_template_mode() { # <python> <policy.py> -> per-case or shared: tests.fixture-templates, shared unless the reader says per-case
  local _tc_v
  if [ -n "${1:-}" ] && [ -f "${2:-}" ] && _tc_v=$("$1" "$2" get tests.fixture-templates 2>/dev/null) \
     && [ "${_tc_v%$'\r'}" = per-case ]; then echo per-case; else echo shared; fi
}
```

`build_fixture` keeps everything around its read: the one-per-suite-run guard on `_st_tmode`, the
sourcing of `resolve-python.sh` and `refuse-wrong-shell.sh`, `refuse_wrong_shell`, and its policy
path through `_st_pk`. Only the `get` and its comparison become
`_st_tmode=$(read_template_mode "$_st_r" "$_st_x")`, with `_st_r` empty where `resolve_python`
fails. Its value under each input is today's. A later suite that reads the switch calls this reader
and orders after this unit.

### Why the key's inputs are named under `$ROOT`

`git hash-object --stdin-paths` reads its paths from stdin, so MSYS never converts them, and it
refuses a `/c/...` path (probed 2026-11-22). `$HERE` comes from `pwd` and has that form; `$ROOT`
comes from `git rev-parse --show-toplevel` and has the `C:/` form. Naming each input by its absolute
path also carries the install prefix and the clone root into the key. That matters under a bar: the
foreign-prefix leg runs this suite at three moved prefixes with `TMPDIR` under the bar's owned
`$WORK` (`tools/run-gates/foreign-prefix.gov.test.sh@3e9396ffa339:607`), so those runs share one
cache root with the bar's own run. The suite file is an input so that `_build_mk_repo`'s text, which
`_build_docs_repo` calls and `declare -f` does not read, moves both keys.

### Why a clone, and not `cp -a` of the template

A `cp -a` copy costs no git process, but it copies the template's objects, so each copy holds as
many entries as today's build and the two templates are extra: the peak would rise by about 120
entries. The re-ground task moves a suite only where git processes and temp entries both fall. A
clone writes an `objects/info/alternates` line in place of the objects.

### What a clone reads differently

The probe compared a built and a cloned repository of each shape, with the suite's
`GIT_CONFIG_COUNT` exported: equal tree, equal `git config --local --list`, refs `refs/heads/main`
alone, `HEAD~1` resolving for the docs shape, and equal work-tree bytes. Four things differ, and no
turnstile arm reads them: the commit ids and dates, the clone's `objects/info/alternates` and
`packed-refs`, its reflog line, and the absence of `COMMIT_EDITMSG`. Every clone of one template
carries one HEAD commit. The turnstile names a holder by its repository path
(`tools/run-gates/run-gates.sh#check_worktree_unheld`), and two calls in one second already share a
HEAD today. The one `git worktree add` an arm runs
(`tools/run-gates/run-gates.turnstile.test.sh@340ddcac21f2:1628`) works over a `--shared` clone.

### Inventory of minted identifiers

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `_build_mk_repo`, `_build_docs_repo` | shell functions | `sh.function`, lexicon `--suggest` OK | `tools/lexicon/lexicon.py --check` |
| `read_template_mode` | shell function in `template_cache_sh` | `sh.function`: `python tools/lexicon/lexicon.py --suggest read_template_mode --as sh.function` prints OK, leading with the declared verb `read` (2026-11-22) | `tools/lexicon/lexicon.py --check`; the `template_cache_sh` parity row |
| `TS_TEMPLATES`, `TS_TEMPLATE_ROOT`, `TS_TEMPLATE_INPUTS`, `TS_TEMPLATE_<builder>` | shell variables | none | none |

### Files touched (estimate)

`tools/run-gates/run-gates.turnstile.test.sh` · `tools/lib/template-cache.sh` ·
`tools/lib/lib-selftest.sh` · `memory/project/shell-role.txt` ·
`memory/builds/dQuietDisk/build/<date>-build-TOOL-dQuietDisk-13-widen-<n>.md` ·
`memory/map/generated/symbols.json`

`tools/lib/resolve-python.test.sh` is not touched: its `template_cache_sh` row names the marker and
the two paths, and a function added inside the markers moves none of them.

Each of the three shell files sits at its ledger row: the turnstile suite at 1,185 code lines,
`tools/lib/template-cache.sh` at 64 and `tools/lib/lib-selftest.sh` at 243 (PINNED,
`sh_hygiene.py --shell-role --measure`, 2026-11-22). The call half and the docs builder add about 15
lines to the suite, and the reader about 5 to each carrier (DERIVED estimates), so the three rows are
widened in one call:
`python tools/memory-tree/ratchet.py widen shell-role --key tools/run-gates/run-gates.turnstile.test.sh tools/lib/template-cache.sh tools/lib/lib-selftest.sh --reason <one line> --unit TOOL-dQuietDisk-13`,
which writes the widen record. Its number is the door's, and a key that does not grow is not named.
The three new functions join the codebase map's symbol index, re-rendered by `gen_map.py --write`.
No path here is on the kickoff manifest's `watch:` line.

Other order-3 units sharing a path: TOOL-dQuietDisk-28 writes `memory/project/shell-role.txt` and
`memory/map/generated/symbols.json`, and TOOL-dQuietDisk-18 writes the symbol index. Those are the
ledger and the generated index every widening unit writes, so `--dispatch`, which records both path
lists, sequences the passes (M6). The order stays 3. No order-3 unit writes either lib file, and a
suite that later reads the switch through `read_template_mode` orders after this unit.

### Alternatives rejected

- `cp -a` of the template: no git process per call, which would save 268 a run (DERIVED), but
  the peak rises by the two templates. Rejected above.
- A hand-made shared copy, the template's files less `.git/objects` plus an alternates line: no git
  process per call and the clone's entries. It is a third hand-out verb on TOOL-dQuietDisk-7's
  CLOSED factory, so it is its own work (M2), filed as ask TOOL-dQuietDisk-32, and a Windows-form
  alternates path written by hand is unproven here.
- One template for both shapes: the docs shape's second commit would then cost 3 git processes per
  call, which its own template makes 0.

## 5. Production-readiness checklist

- security: N/A — no new write path; templates and clones land under the suite's own scratch or a
  bar's owned `$WORK`.
- perf / scale: 67 fewer git processes and about 1,200 fewer standing temp entries per turnstile run,
  DERIVED in the design and measured by AC4.
- error / empty / loading states: a failed key, template build or clone returns 1 from `mk_repo`,
  which the first call site turns into exit 2, as a failed build does today.
- observability: the face prints `template: <key8> built` once per builder on stderr.
- risks: a commit moving the tree under a running suite
  (`memory/gotchas/suite-invalidated-by-a-commit-under-it.md`); the key holds each input's blob id,
  so a moved runner builds a new template. A clone reads its objects from the template, which lives
  under the same root and is cleared after every clone of it.
- testing: AC1, AC2, AC3, AC5, AC6 and AC7 are probes of this unit's code; AC4 runs the suite and
  is the main loop's.
- migration: N/A — templates live for one suite run or one bar.
- user docs: N/A — test fixtures; no `help/` page describes them.

## 6. Acceptance criteria

- **AC1** — When a probe sources `tools/lib/template-cache.sh` and the edited suite's prologue
  variables and fixture functions into a scratch script, and replays the suite's builder calls under
  `GIT_TRACE2_EVENT=<dir>`, 56 `mk_repo` calls onto fresh paths, 3 onto paths already holding
  `.git`, and 11 `build_docs_repo` calls, once with `TS_TEMPLATES=per-case` and once at `shared`:
  the first shared `mk_repo` call adds 14 trace files and the first `build_docs_repo` 17, each later
  fresh call adds 3, each call onto a repository adds 4, and the shared total is at least 75 below
  the per-case total. After the scratch script exits through its EXIT trap, no entry remains under
  its `TMPDIR`.
  Red when: a repeated call rebuilds, a call onto a repository clones, or a template outlives the
  scratch root.
  figure: 75 is DERIVED from the call sites at `7b8c737b0` and the PINNED per-command costs; the
  switch read's 8 is AC5's.
- **AC2** — When the same probe builds each shape once per case and once from its template, each at
  a fresh path, `git for-each-ref --format='%(refname) %(objecttype)'`, `git config --local --list`,
  `git ls-files -s`, `git status --porcelain --untracked-files=all`, `git rev-parse HEAD^{tree}`,
  `git rev-list --count HEAD`, `git log --format='%an %ae %cn %ce %s'` and the name and bytes of
  every work-tree file outside `.git` are byte-identical between the two.
  Red when: a clone differs in a ref, a config value, the index, the status, the tree, the history
  or a file.
- **AC3** — When the probe changes one byte of `_build_mk_repo` in a scratch copy of the suite, then
  one byte of the copied runner in a scratch `git clone --shared` of the tree, and asks for the
  template after each, the face prints `template: <key8> built` with a new key each time. When the
  same suite text runs from a second clone root, its keys differ from the first root's.
  Red when: the key omits the builder's text, an input's bytes or its path, and an old template is
  reused.
- **AC4** — When the main loop runs `tools/lib/extract-arms.sh` over the turnstile suite at the build
  base and at this unit's commit, each in a scratch `git clone --shared` with `GIT_TRACE2_EVENT`,
  `TEMP`, `TMP` and `TMPDIR` pointed at scratch dirs and a 0.5 s entry watcher, both runs print the
  same arm inventory and the same assertion count. The summed git process count and the peak temp
  entries are lower at this unit's commit, and residual temp entries are 0 both times.
  Red when: an arm line changes, either count does not fall, or an entry remains.
  permission: a role pass may not run a `.test.sh` suite (`tools/unattended/gate-guard.js` row D4);
  the main loop observes this at VERIFYING.
  cost: two runs of a suite whose ceiling `tools/gate-legs.json` declares.
  figure: the 67 and the 1,200 are DERIVED in the design; the nested bars' own git counts vary run to
  run, so the suite-level fall is recorded beside its instrument, not held to them.
- **AC5** — When a probe runs the edited suite's prologue in a scratch `git clone --shared` of the
  tree whose `policy.py get tests.fixture-templates` reads `per-case`, `TS_TEMPLATES` reads
  `per-case`, and a `mk_repo` call adds 4 trace files, prints no `template:` line and makes no
  `templates` directory under its root. In a clone reading the default, `TS_TEMPLATES` reads
  `shared`, and in a clone with the policy kit's directory absent, `shared` too. Called directly,
  `read_template_mode` prints `shared` for an empty python, for a missing `policy.py` and for a
  launcher that exits 9009.
  Red when: the read ignores `per-case`, or reads a missing policy kit, an empty python or a failed
  launch as anything but `shared`.
  fixture: the tree commits no `per-case` value; the probe commits `.governance/policy.toml` in its
  clone, as TOOL-dQuietDisk-7's AC3 did.
- **AC6** — When `python tools/gate-lint/sh_hygiene.py --shell-role` runs over the tree after the
  pass, it prints no finding for the turnstile suite, `tools/lib/template-cache.sh` or
  `tools/lib/lib-selftest.sh`, and each grown key's row in `memory/project/shell-role.txt` reads
  `widened:` and the widen record's stem.
  Red when: a grown row is left at its pinned count, or is edited without the door's record.
- **AC7** — When a probe extracts the `template_cache_sh` block from `tools/lib/template-cache.sh`
  and from `tools/lib/lib-selftest.sh` by its markers, CR bytes dropped, as the parity row's `blk`
  does, `diff` prints nothing and both hold `read_template_mode`. When the three-arm probe suite of
  TOOL-dQuietDisk-7's AC3 runs under `build_fixture --template` in a scratch clone committing no
  policy and in one committing `per-case`, both runs print the same `ok` and `FAIL` lines in the same
  order, and only the shared run prints a `template:` line.
  Red when: the two copies differ by a byte, or `build_fixture` reads `per-case` as `shared`.

## 7. Gates

`run-gates turnstile` · `recall floor` · `recall floor arms` · `selftest harness self-test` · `extract-arms self-test`

The two recall legs guard the shell-line ledger S7 widens, and the harness and extract-arms legs
guard the two lib files S6 writes. No arm is added or moved. Every
turnstile arm runs over the cloned fixtures, and the second signal loop's three arms run over S3's
fallback. The existing `template_cache_sh` row of `tools/lib/resolve-python.test.sh` and the
harness suite's switch arm re-observe S6 unchanged.

## 8. Open questions

- **F1 — Where does a suite outside `lib-selftest.sh` read `tests.fixture-templates`?** The bash
  face carries no switch reader: `template_cache_sh` holds four functions and none reads the policy
  (`tools/lib/template-cache.sh@c9e02755f426:22-89`). The one bash read is private to
  `build_fixture` (`tools/lib/lib-selftest.sh@4d0ce956a80b:172-185`). Units 10 and 12 meet the
  same question.
  - (a) A new unit, ordered before units 10, 12 and 13, adds `read_template_mode <python>
    <policy.py>` to `template_cache_sh`, printing `shared` or `per-case` and `shared` on an absent
    kit, an unreadable key or a failed launcher, and has `build_fixture` call it. The inline copy
    in `lib-selftest.sh` follows by the parity row. Each consumer then reads the switch in one line.
  - (b) This unit adds that function itself, and units 10 and 12 order after it. Their write sets
    and this one's then share `tools/lib/template-cache.sh` and `tools/lib/lib-selftest.sh`.
  - (c) Each suite carries its own `policy.py get` read and comparison. It is a copy of
    `build_fixture`'s read, which the charter's `[reuse]` rule refuses at a kind's second instance.
  - Recommendation: (a). It extracts the reader once for its three consumers, keeps one mechanism
    per unit (M2), and leaves the order-3 write sets disjoint on the factory's files.
  - RESOLVED (agent, 2026-11-22, delegated): (b). Option (a) would open a unit to hold one
    function, and (c) is refused by `[reuse]`. Unit 10 needs no reader: its F3 ruled no switch,
    because it does not use the cache. So this unit adds `read_template_mode` to
    `template_cache_sh`, its inline copy in `tools/lib/lib-selftest.sh` held byte-identical by the
    existing parity row, and any later suite that reads the switch orders after this unit (S6).

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft.
- rev-2 · 2026-11-22 · under `2026-11-22-prompt-TOOL-dQuietDisk-1-divergence-task`. Section 4's call
  half spells unit 7's bash face `resolve_template`, as TOOL-dQuietDisk-7 rev-2 renames it, in place
  of the placeholder `template_of`, which the lexicon would refuse. The moved bodies, such as
  `_build_mk_repo`, lead with `build` and pass `--suggest`. No criterion had the pass run a suite:
  AC4's suite runs were already the main loop's.
- rev-3 · 2026-11-22 · wording only, under `2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task`. In section
  3 and section 10 the replay and age builders' call count and dWitnessedBar's changed-line counts are
  marked PINNED. Design, scope and acceptance unchanged.
- rev-4 · 2026-11-22 · §1 · S1 · S2 · S3 · S4 · S5 · S6 · S7 · §3 · §4 · §5 · AC1 · AC2 · AC3 · AC4 ·
  AC5 · AC6 · §7 · §8 · §10 · re-grounded at 7b8c737b0 (orders 1 and 2 built), under
  `2026-11-22-prompt-TOOL-dQuietDisk-6-reground-task`. What moved: (1) the factory hands out a
  `--shared` clone with no remote, costing 3 git processes, and its key is the builder's `declare -f`
  and its input files, not a kit tree hash; the call half clones in place of `cp -a`, which the
  task's rule refuses because it raises temp entries. (2) A built repository costs 4 git processes,
  since `commit` spawns `git maintenance run --auto`, and the switch read costs 8 (both PINNED). (3)
  Counted at this base, the evidence suite saves 37 git processes but raises its peak, and the canary
  saves 6 against the read's 8, so scope narrows to the turnstile suite, its docs builder added as a
  second template; the saving is now 67 git processes and about 1,200 peak entries, from 509. (4) A
  destination already holding `.git` builds as today, because the second signal loop reuses three
  paths. (5) Key inputs are named under `$ROOT`, since `git hash-object --stdin-paths` refuses an
  MSYS path. (6) The bash face has no switch reader, now F1. (7) The `ru_repo` origin-rewrite arm is
  gone with the evidence suite, and AC6 observes the shell-line widen. The gov suite now holds three
  `mktemp -d` directories and still no repository. The goal is unchanged; its reach narrows to where
  a clone saves.
- rev-4 · 2026-11-22 · §2 · S5 · S6 · S7 · S8 · §3 · §4 · §5 · AC5 · AC6 · AC7 · §7 · §8 · §10 · the
  run ruled F1 as (b), RESOLVED in place, before any code. This unit adds `read_template_mode` to
  `template_cache_sh` (new S6), `build_fixture` calls it, and the inline copy in `lib-selftest.sh`
  stays byte-identical under the existing parity row, which does not move. Files touched gains
  `tools/lib/template-cache.sh` and `tools/lib/lib-selftest.sh`, the widen names their two keys
  beside the suite's, AC7 observes the parity and the harness's per-case read, and the ledger and
  arm-set items renumber to S7 and S8. The hand-made copy is ask TOOL-dQuietDisk-32. The rev stays
  4: the ruling folds into the re-ground's revision before it is built.

## 10. Reuse audit

The seam is TOOL-dQuietDisk-7's template factory, `tools/lib/template-cache.sh#resolve_template` and
`#build_template_clone`, which generalised `tools/lib/lib-selftest.sh#build_fixture`. The two
builders become its builder functions unchanged, and their callers do not move.
`python tools/codebase-map/reuse_lookup.py "build a scratch fixture repository once per suite run and give each test case a shared clone of it"`
ranked `build_fixture` and `build_target` as seams and not the factory's own functions, whose fan-in
is still low; the map and the code disagree there, and the code is read. The switch reader extends
the same seam: `build_fixture`'s private read (`tools/lib/lib-selftest.sh#build_fixture`) becomes
`read_template_mode` in the shared block, its first and second callers sharing it, as F1 ruled.
Chain owner: dWitnessedBar (Test), landed at `40def53f7`. This unit changes how the turnstile
suite's fixtures are built and no arm, so it contradicts none of its specs.

Recall terms used: `python tools/memory-recall/query.py "how does the turnstile suite build its scratch repositories and which template cache verbs can replace the per-call build" --terms "mk_repo build_docs_repo turnstile scratch repository template cache resolve_template build_template_clone shared clone fixture-templates per-case"`
