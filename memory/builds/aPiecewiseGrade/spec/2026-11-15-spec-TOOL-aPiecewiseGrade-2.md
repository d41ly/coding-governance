# TOOL-aPiecewiseGrade-2 — `run_spec_token_check` runs the checker's incremental mode on a whole-key miss, and names its per-spec cache's live generation in a file only where the whole key is recorded

**Status:** CLOSED · rev-4 · 2026-11-16 · node a · Tier-2 · base aebbb4a72 · streams tooling · order 4 · ratified 2026-11-15

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-build-TOOL-aPiecewiseGrade-2-1-acceptance-ledger.md](../build/2026-11-15-build-TOOL-aPiecewiseGrade-2-1-acceptance-ledger.md) | journal | — |
| [2026-11-16-build-TOOL-aPiecewiseGrade-1-agent-ledger.md](../build/2026-11-16-build-TOOL-aPiecewiseGrade-1-agent-ledger.md) | journal | TOOL-aPiecewiseGrade-1 TOOL-aPiecewiseGrade-3 TOOL-aPiecewiseGrade-4 TOOL-aPiecewiseGrade-5 TOOL-aPiecewiseGrade-6 TOOL-aPiecewiseGrade-7 TOOL-aPiecewiseGrade-8 |
| [2026-11-16-build-TOOL-aPiecewiseGrade-1-arms-observed.md](../build/2026-11-16-build-TOOL-aPiecewiseGrade-1-arms-observed.md) | journal | TOOL-aPiecewiseGrade-1 TOOL-aPiecewiseGrade-3 TOOL-aPiecewiseGrade-4 TOOL-aPiecewiseGrade-5 TOOL-aPiecewiseGrade-6 TOOL-aPiecewiseGrade-7 TOOL-aPiecewiseGrade-8 |
| [2026-11-16-build-TOOL-aPiecewiseGrade-2-close-observations.md](../build/2026-11-16-build-TOOL-aPiecewiseGrade-2-close-observations.md) | journal | TOOL-aPiecewiseGrade-1 TOOL-aPiecewiseGrade-3 |
| [2026-11-15-prompt-TOOL-aPiecewiseGrade-1-brief.md](../prompts/2026-11-15-prompt-TOOL-aPiecewiseGrade-1-brief.md) | research | TOOL-aPiecewiseGrade-1 |
| [2026-11-15-prompt-TOOL-aPiecewiseGrade-2-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aPiecewiseGrade-2-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aPiecewiseGrade-2-forks-brief.md](../prompts/2026-11-15-prompt-TOOL-aPiecewiseGrade-2-forks-brief.md) | research | TOOL-aPiecewiseGrade-4 |
| [2026-11-15-prompt-TOOL-aPiecewiseGrade-2-revision.md](../prompts/2026-11-15-prompt-TOOL-aPiecewiseGrade-2-revision.md) | research | — |
| [2026-11-15-prompt-TOOL-aPiecewiseGrade-3-forks-brief.md](../prompts/2026-11-15-prompt-TOOL-aPiecewiseGrade-3-forks-brief.md) | research | TOOL-aPiecewiseGrade-3 TOOL-aPiecewiseGrade-1 |
| [2026-11-15-prompt-TOOL-aPiecewiseGrade-4-forks-brief.md](../prompts/2026-11-15-prompt-TOOL-aPiecewiseGrade-4-forks-brief.md) | research | TOOL-aPiecewiseGrade-4 |
| [2026-11-16-review-TOOL-aPiecewiseGrade-1-diff-review-round1.md](../reviews/2026-11-16-review-TOOL-aPiecewiseGrade-1-diff-review-round1.md) | diff-review | TOOL-aPiecewiseGrade-1 TOOL-aPiecewiseGrade-3 TOOL-aPiecewiseGrade-4 |

<!-- /gen:spec-records -->

## 1. Goal

When aLightenedLoop's whole key misses, `--dispatch` runs the spec-token checker with
`SPEC_TOKENS_CACHE` naming the per-slug cache's live generation under the sidecar root, and
`SPEC_TOKENS_CACHE_NEXT` naming a directory made with `mktemp -d` beside it. A pass commit that
moves one spec then re-grades that spec alone, and every join still runs whole. Where the driver
records the whole key, it writes the new generation's name into a name file beside the key and
removes the old generation. It renames nothing. So the live generation holds only what a still tree
produced, and the driver gains no `mv`. Not one printed byte of `--dispatch` moves. This unit builds
fourth, after TOOL-aPiecewiseGrade-3, TOOL-aPiecewiseGrade-1 and TOOL-aPiecewiseGrade-4, whose
contract it builds on.

## 2. Scope (IN)

- **S1** — Every checker call that `run_spec_token_check`'s two halves make with
  `SPEC_TOKENS_INPUTS` set also sets `SPEC_TOKENS_CACHE` to the live generation the name file
  `spec-tokens.<slug>.live` names, and `SPEC_TOKENS_CACHE_NEXT` to a directory the start half made
  with `mktemp -d`. With no well-formed name, the cache is a name no generation carries, so every
  spec misses. Both are empty when the sidecar root does not resolve or `mktemp` fails. The start
  half carries the two in an eighth and a ninth global, `ST_NEXT` and `ST_CACHE`. The cache is one
  per slug, its only layout (F1). Observed by AC1 and AC2.
- **S2** — Where the driver writes the whole key, it then writes the new generation's name into the
  name file and removes the old generation, with the two commands §4 shows. No other branch writes
  the name file. Observed by AC1, AC2 and AC3.
- **S3** — The start half checks the shape of the name it reads back before any `rm -rf` sees it. A
  name that fails is treated as no name. Observed by AC8.
- **S4** — Before it makes a generation, the start half sweeps every generation of that slug but the
  live one. Observed by AC3 and AC8.
- **S5** — The skip line, the cache-off line, the not-recorded line, the admit note and every
  refusal keep their bytes, and no line is added. Observed by AC4.
- **S6** — The verbs guide states the incremental run in both copies, which stay byte-identical.
  Observed by AC5.
- **S7** — A timed `--dispatch` on node `a` after a sequential pass commit, base against built.
  Observed by AC6.
- **S8** — The driver gains no `mv`, so the shell-hygiene lint's counts over it do not move and the
  registry keeps its row as it stands. Observed by AC7.

## 3. Non-goals (OUT)

- No change to the whole key, `derive_spec_token_key`, `read_tree_state` or the conditions under which
  the whole key is recorded. Its miss is the only trigger.
- No change to `check_spec_token_hits` or any verdict, refusal, status or summary of `--dispatch`.
- No scoping of the check to the dispatching build.
- No new announcement line, such as a re-graded count. The checker's `graded.list` is the record.
- No new generation named live on a refusal, a moved tree, a missing record or an unreplayable one,
  which are the branches where the whole key is not recorded either.
- No `mv` of a generation directory, no row raised in `memory/project/temp-name-sites.txt`, no lint
  change, and no promotion by copying.
- No change to the bar's spec-tokens leg, which keeps the plain run.
- No edit to the unattended Skill, and no kit version bump by hand.

### Edges

- **consumes-from** `TOOL-aPiecewiseGrade-1` — the incremental mode behind `SPEC_TOKENS_CACHE`, its per-spec key and its `graded.list`. The build order is TOOL-aPiecewiseGrade-3 at order 1, TOOL-aPiecewiseGrade-1 at order 2, TOOL-aPiecewiseGrade-4 at order 3 and this unit at order 4
- **consumes-from** `TOOL-aPiecewiseGrade-4` — the contract that the checker writes its next generation into the directory `SPEC_TOKENS_CACHE_NEXT` names, made by the caller with `mktemp -d`, and never creates or removes it; without it the generation lands at a fixed name. That unit builds at order 3, before this one
- **consumes-from** external — aLightenedLoop's whole key on the two-half `run_spec_token_check`, landed at `4bd7215ce`

## 4. Design

### What the code does today

Re-read at `a07d7914f`, where the driver's blob is still `a9ff4a9c`, the suite's `24f12f1e` and the
lint's `448d62cb`. Rev-2 grounded at `aebbb4a72` and at aLightenedLoop's head `d9f84ee14`.

- The start half, `init_spec_token_check` (`tools/unattended/unattended.sh#init_spec_token_check`),
  resolves the sidecar root into its local `_stdir` and sets `ST_REC` and `ST_IN` beside it
  (`tools/unattended/unattended.sh@a9ff4a9c:14598`). It reads the recorded key back with
  `read -r _stwas <"$ST_REC" || :` (`tools/unattended/unattended.sh@a9ff4a9c:14600`). On a run it
  removes the old record and makes the sidecar directory
  (`tools/unattended/unattended.sh@a9ff4a9c:14606`), then starts the checker through `init_bounded`
  with `SPEC_TOKENS_INPUTS` set (`tools/unattended/unattended.sh@a9ff4a9c:14609`).
- It hands the read half its state through seven `ST_` globals, declared at
  `tools/unattended/unattended.sh@a9ff4a9c:14588` and emptied by `remove_spec_token_check`.
- The read half, `run_spec_token_check`, copies the globals into locals and empties them
  (`tools/unattended/unattended.sh@a9ff4a9c:14622`). It has no `_stdir`; its record path is `_strec`.
  It runs the checker synchronously through `run_bounded` when no start was made
  (`tools/unattended/unattended.sh@a9ff4a9c:14641`), derives the key over the record before the
  second tree read (`tools/unattended/unattended.sh@a9ff4a9c:14657`), and writes the whole key at
  one site, `{ printf '%s\n' "$_stkey" >"$_strec"; } 2>/dev/null || :`
  (`tools/unattended/unattended.sh@a9ff4a9c:14667`). Every other branch prints the not-recorded line
  or returns earlier.
- `verb_dispatch` runs `check_slug` at its head (`tools/unattended/unattended.sh@a9ff4a9c:14677`)
  and calls the start half far below it (`tools/unattended/unattended.sh@a9ff4a9c:14965`).
  `check_slug_shape` admits letters, digits and dashes only
  (`tools/unattended/unattended.sh@a9ff4a9c:3107`), so no slug carries a dot or a slash.
- `resolve_sidecar_dir` (`tools/unattended/lib-unattended.sh#resolve_sidecar_dir`) answers
  `<git-dir>/unattended`, the worktree's own git dir, or nothing.
- `read_bounded` folds the child's stderr into `RB_OUT`
  (`tools/unattended/unattended.sh@a9ff4a9c:324`), which `check_spec_token_hits` reads. So the
  checker's mode must print nothing on stderr either, which unit 1 states.
- The checker reads a missing `SPEC_TOKENS_CACHE` directory as a miss for every spec: its lookup
  answers None on any `OSError` (`tools/check-spec-tokens.py#read_spec_cache`). Unit 4 keeps that
  lookup and runs the plain run when either variable is empty.
- The driver suite's spec-token arms build a fixture with the real checker, a clean `tRun` spec and a
  `tOther` spec that reds, and call `run_spec_token_check tRun` in process
  (`tools/unattended/unattended.test.sh@24f12f1e:7813`). Two text arms grep the driver for
  `run_bounded "$_stpy" "$SPEC_TOKENS_CLI"` and `init_bounded "$ST_PY" "$SPEC_TOKENS_CLI"`
  (`tools/unattended/unattended.test.sh@24f12f1e:4478`), which the prefixes below leave intact.
- `scan_temp_file` (`tools/gate-lint/sh_hygiene.py#scan_temp_file`) classifies every `mv` in a shell
  source and nothing else. Over the driver it reports 2 `fixed`, 6 `admitted` and 0 `unfollowed`
  (PINNED a07d7914f), and the registry row `tools/unattended/unattended.sh fixed-temp 2` declares
  the 2.

### The sidecar layout

Every name sits in `_stdir`, beside the whole key `spec-tokens.<slug>.key` and its record
`spec-tokens.<slug>.inputs`.

| name | what it is | who writes it |
|---|---|---|
| `spec-tokens.<slug>.live` | the name file: one line, the live generation's base name | the read half, only where the whole key is recorded |
| `spec-tokens.<slug>.specs.XXXXXXXX` | one generation, eight letters or digits from `mktemp -d` | the start half makes it, the checker fills it |
| `spec-tokens.<slug>.specs.none` | the cache's name when no name is well-formed; no generation carries it, because `mktemp` gives eight characters | nobody; the sweep removes one planted there |

The name file holds a base name, not a path, so its shape check is one anchored pattern and the
directory it names can only sit in `_stdir`.

### S1 and S3 — the variables, resolved through the name file

The start half gains the locals `_stlive` and `_stold`. Where it removes the record and makes the
sidecar directory, it reads the name file, checks its shape, sweeps, and makes the next generation:

```bash
  if [ -n "$ST_IN" ]; then
    rm -f "$ST_IN" 2>/dev/null; mkdir -p "$_stdir" 2>/dev/null
    { read -r _stlive <"${ST_REC%.key}.live"; } 2>/dev/null || :
    [[ $_stlive =~ ^"spec-tokens.$1.specs."[A-Za-z0-9]{8}$ ]] || _stlive=""
    for _stold in "$_stdir/spec-tokens.$1.specs."*; do
      [ "$_stold" = "$_stdir/$_stlive" ] || [ ! -d "$_stold" ] || rm -rf "$_stold" 2>/dev/null
    done
    ST_NEXT=$(mktemp -d "$_stdir/spec-tokens.$1.specs.XXXXXXXX" 2>/dev/null) || ST_NEXT=""
    [ -z "$ST_NEXT" ] || ST_CACHE="$_stdir/${_stlive:-spec-tokens.$1.specs.none}"
  fi
  SPEC_TOKENS_INPUTS=$ST_IN SPEC_TOKENS_CACHE=$ST_CACHE SPEC_TOKENS_CACHE_NEXT=$ST_NEXT init_bounded "$ST_PY" "$SPEC_TOKENS_CLI" && ST_HANDLE=$RB_HANDLE
```

The name file is the one read-back site, and the pattern is S3's shape check. A missing file, an
empty or truncated line, a path, a `..` and another slug's name all fail it, and each leaves
`_stlive` empty. Only a checked name then reaches the sweep's comparison or `ST_CACHE`, and
`ST_CACHE` is the one path the read half later removes. The `{ … } 2>/dev/null` wrapper keeps a
missing file's redirection error off stderr, so S5 holds.

With no checked name, `SPEC_TOKENS_CACHE` names `spec-tokens.<slug>.specs.none`. It is never empty
there, because unit 4 runs the plain run on an empty cache, which writes no generation, so a cache
that started empty would never fill. The sweep has just removed any directory at that name, so every
spec misses and the run writes a whole generation.

`ST_NEXT` and `ST_CACHE` join the seven globals at their declaration, at every line that empties
them, in `remove_spec_token_check`, and in the read half's copy line, as `_stnext=$ST_NEXT` and
`_stcache=$ST_CACHE`. The header comment's "seven ST_ globals" becomes nine. The read half's
`run_bounded` fallback carries `SPEC_TOKENS_CACHE=$_stcache SPEC_TOKENS_CACHE_NEXT=$_stnext` beside
`SPEC_TOKENS_INPUTS=$_stin`. So every reader of the cache, the checker on either path, the sweep and
the removal below, resolves the live generation through the one read of the name file. When the
sidecar root does not resolve, or `mktemp` fails, both variables are empty and the checker runs
exactly the plain run.

With the cache off, meaning no fingerprint, the variables are still set, as rev-2 set the one.
Every entry in the live generation was named under an earlier bracket, so reading it is sound. The
read half returns before the key's write site, so the new generation is never named, and the next
start sweeps it.

### S4 — the sweep

The loop above removes every directory matching `spec-tokens.<slug>.specs.*` but the live one. Its
names come from the glob, never from a file, and the slug carries no dot or slash, so the glob
reaches no other slug's generation and nothing outside `_stdir`. It runs only on a run, never on a
skip, so a leftover waits for the next miss. It reclaims every generation no name file names: one a
refusal, a moved tree, a cache-off run or a killed run left, and one an older checker wrote with a
`.next` suffix.

### S2 — naming the new generation where the whole key is recorded

Right after the line that writes the whole key, and only there:

```bash
    if [ -n "$_stnext" ] && [ -d "$_stnext" ]; then
      { printf '%s\n' "${_stnext##*/}" >"${_strec%.key}.live" && rm -rf "$_stcache"; } 2>/dev/null || :
    fi
```

The name written is the base name `mktemp -d` gave, so it passes S3's check by construction. That
site is reached only when three things hold, the conditions TOOL-aLightenedLoop-3 S6 records the
whole key under: the verdict admitted, the tree state read before the checker equals the one read
after the key's replay, and the record replays. So a generation goes live only when nothing moved
while the checker read and keyed it. On every other branch the new generation stays unnamed, and
the next start's sweep removes it. The old generation is removed only after the name write
succeeds, so a failed write leaves the old name live and the new generation for the sweep. Neither
failure prints anything or refuses.

The name file is a direct write at a fixed destination, as the whole key's record is. No `mv`
exists, so the lint has nothing to read here, and AC7 observes that its counts over the driver do
not move.

### A run killed partway

The checker writes its whole generation before it exits, and the read half reads it only after
`read_bounded` or `run_bounded` has waited for it. So every generation the read half names is
complete.

| killed | what it leaves | why the next run is correct |
|---|---|---|
| inside the checker | a partial generation no name file names | the next start's sweep removes it, and the old name still reads a generation named under its own bracket |
| between the key's write and the name's | the key recorded, the old name live, the new generation unnamed | a skip reads nothing; a later miss reads the old generation, which is sound and costs misses only, and the sweep removes the new one |
| inside the name's write | a name file with an empty or truncated line | S3's check fails, so the next run reads `spec-tokens.<slug>.specs.none`, every spec misses once, and the sweep removes every generation |
| between the name's write and the old generation's removal | the name file naming the new, complete generation, and the old generation unnamed beside it | the next start reads the new generation as its cache, and its sweep removes the old one, because no name file names it |
| inside the removal | the new generation live, and part of the old one unnamed | as the row above |

In every row the name file names a complete generation the read half named under a held bracket, or
fails the shape check. The unnamed directory a kill leaves is the same state a moved tree leaves,
which AC3 observes the sweep reclaiming.

### S5 — every printed byte

The variables reach only the checker, and units 1 and 4 hold the checker's stdout, stderr and
status equal to the plain run's. The read of the name file, the sweep, `mktemp`, the name's write and
the removal print nothing. So `check_spec_token_hits` reads the same `RB_OUT`, and every line
`run_spec_token_check` prints is unchanged: the skip line, the cache-off line, the not-recorded line
with its three reasons, the admit note naming another build's hit, and the check-49 refusals.

### S6 — the verbs guide

`tools/unattended/VERBS.template.md` states the whole key in the clause ending "recorded under the
sidecar root only when the tree and HEAD held still while it ran", and that sentence continues to
"runs the checker." (`tools/unattended/VERBS.template.md@c70b591a:258`). The new sentence goes
after "runs the checker." and before "A blank or absent key is an ANNOUNCED skip":

```
On a miss it runs the checker's incremental mode, which reuses each live spec's findings from a
per-spec cache under the sidecar root while that spec's own inputs hold,
re-grades the rest and runs every cross-build join whole,
so its output is the whole-tree run's; a new generation of that cache goes live only where the key is recorded.
```

The phrase `re-grades the rest and runs every cross-build join whole` is spelled on one line, as
written. `memory/guides/UNATTENDED-VERBS.md` takes the identical edit, because the two files are
byte-identical at `a07d7914f`, blob `c70b591a`. No `help/` page names the dispatch cache, grepped at
`aebbb4a72`.

### What the design does not check

Carried from TOOL-aLightenedLoop-3's "What the key does not check", for the whole key that triggers
this run: a path probed only for existence, the environment beyond the recorded delta, and a
package upgraded in place. Unit 1's own list holds for the per-spec keys, and unit 4's for the named
directory.

New with this design:

- **Two dispatches of one slug running at once in one worktree.** The second start's sweep removes
  the first's new generation, and the first's naming then finds no directory and names nothing. The
  first's removal can take the old generation the second's checker is reading, which reads as
  misses. Nothing serializes them, as nothing serializes the whole key's record today. The main loop
  runs each dispatch in the foreground, one at a time, which is what `dispatch.declare` tells it.
- **The bracket's reach.** It reads the run-gates fingerprint and HEAD, before the checker and
  after the replay. An edit made and undone inside the run leaves both reads equal. If the checker
  graded the edited bytes and keyed the restored ones, the named entry holds findings over bytes the
  tree no longer has, and a later lookup over the restored bytes hits it. The whole key carries the
  same gap today, for the same reason.
- **The name file's provenance.** S3 checks the name's shape, not that the driver wrote it, nor that
  the directory it names holds a generation the driver named. A forged name of the right shape
  beside a forged directory can hide findings from a dispatch only, and the bar's plain run still
  grades them.
- **The lint.** It reads `mv` alone, so it says nothing about this design's `rm -rf` or the name
  file. AC7 observes only that no `mv` was added.

### The pass probe, `$SCRATCH/pg2.sh`

The probe builds a fixture repository at `$TEMP/pg2`, as TOOL-aLightenedLoop-3's `l3.sh` does,
holding the built checker, the memory-tree kit and the run-gates fingerprint script copied into its
tool root. It sources the built driver, loads its conf, and sets `SPEC_TOKENS_CLI` to the copied
checker. The seed has two live specs in build `tA`, one in `tB` that reds, and an empty waiver file.
`D` is the fixture's sidecar root, `N` is `$D/spec-tokens.tA.live`, and `L` is `$D/` followed by
N's one line.

| step | what happens | the line it prints |
|---|---|---|
| `first` | `run_spec_token_check tA`, no sidecar state | `first graded <lines of $L/graded.list> live <.json files in $L> gens <n> named <0|1>` |
| `same` | the same call again | `same skipped <count of the skip line>` |
| `onespec` | one `tA` spec's prose edited and committed, then the call | `onespec graded <n> gens <n> newname <0|1>` |
| `moved` | the checker wrapped by a stub that calls the real module's `main`, then appends to a file the record names before exiting | `moved said <count of the moved reason> kept <0|1> gens <n>` |
| `refused` | the real checker back, a `tA` spec made to red, then the call | `refused kept <0|1> gens <n>` |
| `planted` | the red edit undone, `$D/spec-tokens.tA.key` removed, N overwritten with `../planted`, and `$D/../planted/keep` written, then the call | `planted spared <0|1> graded <n> gens <n> named <0|1>` |
| `lint` | `scan_temp_file` over the built driver's text | `lint fixed <n> admitted <n> unfollowed <n>` |

`gens` counts the directories matching `$D/spec-tokens.tA.specs.*` after the call. `named` is 1 when
N's one line is `spec-tokens.tA.specs.` followed by eight letters or digits and names a directory.
`newname` is 1 when N's bytes differ from the ones before the call and `named` holds. `kept` is 1
when N's bytes and `find "$L" -type f -exec sha1sum {} +` print the same before and after the call.
`spared` is 1 when `$D/../planted/keep` still exists. The `lint` row reads
`tools/gate-lint/sh_hygiene.py#scan_temp_file` through an import, which runs no leg. The probe then
repeats the first five steps over a fresh fixture with the base driver, the one before this unit,
from a worktree at that base under `%TEMP%/pg2b`. It prints `lines same <0|1>`, from `cmp` over the
two drivers' captured output, every step concatenated.

### Inventory

| identifier | kind | lexicon |
|---|---|---|
| `ST_NEXT` and `ST_CACHE` | the eighth and ninth globals between the two halves | no declared cell for a shell global |
| `_stlive`, `_stold`, `_stnext` and `_stcache` | locals of the two halves | no declared cell for a shell local |
| `spec-tokens.<slug>.live` | the sidecar name file | no declared cell |
| `spec-tokens.<slug>.specs.XXXXXXXX` and `spec-tokens.<slug>.specs.none` | sidecar generation names | no declared cell |

No shell function, conf key, check number or refusal line is minted. `SPEC_TOKENS_CACHE` is unit 1's
and `SPEC_TOKENS_CACHE_NEXT` is unit 4's. The `.live` suffix is spelled twice, once in each half,
each derived from the record path, as the record's own `.key` and `.inputs` are spelled beside it.

### Docs, and what the change owes beyond the code

- The verbs guide in both copies, per S6.
- No `help/` page, per S6.
- No new function, so the codebase map's symbol index does not move. The `unattended` dossier names
  the driver's paths, which do not move.
- The kit epoch leg sees shipped bytes move, and the lander's mint moves the version.

### Rollout

This unit builds after units 3, 1 and 4, against the driver at `a9ff4a9c`. Every cited line moves, so
the builder finds each site by its text: the record path's assignment, each `SPEC_TOKENS_INPUTS=`
prefix, the globals' declaration and copy lines, and the whole key's `printf`. The driver suite's
assertion floor rises by the new assertions, which the close confirms from a real run.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`

### Alternatives rejected

- **Rename the `mktemp -d` generation over a fixed cache directory.** Rev-3's design, and
  TOOL-aPiecewiseGrade-4's F1 option (a). The lint reads that `mv` as unfollowed, which is not
  coverage. The owner picked (b).
- **Promote from the fixed name `<dir>.next`.** Rev-2's design. `scan_temp_file` reads its `mv` as
  `fixed`, the gated class, so the registry row would rise from 2 to 3 against its shrink-only rule.
- **Leave the old generation for the next start's sweep.** One fewer `rm -rf`, but two whole
  generations then sit on disk between runs, and the owner's pick has the read half remove it.
- **Re-read the name file in the read half.** A second read-back site and a second shape check, and
  it could name a generation other than the one the checker read. `ST_CACHE` carries the one read.
- **A full path in the name file.** Its check would have to hold the directory as well as the name.
  A base name joined to `_stdir` cannot leave it.
- **An empty `SPEC_TOKENS_CACHE` when no name is well-formed.** Unit 4 then runs the plain run and
  writes no generation, so the cache never starts.
- **Name a generation on every run where the tree held still, refusals included.** The entries would
  be sound. But the brief keys the write on the conditions TOOL-aLightenedLoop-3 S6 records its key
  under, and one rule for both is one fact. A re-dispatch after a refusal then reuses the last
  admitted generation and re-grades what moved since.
- **Remove the unnamed generation on each branch that does not name it.** Four sites, the refusals
  and `remove_spec_token_check` among them, and a killed run would still leave one behind. One sweep
  at the start covers every case.
- **A helper function for the read, the check or the naming.** Each has one caller.
- **Let the checker promote itself.** Rejected at unit 4 by its tests: it keeps a fixed name, out of
  the lint's sight, and costs a third checker process.
- **One cache per worktree, shared by every slug.** Two slugs' dispatches would sweep and name each
  other's generations outside the other's bracket. The owner chose one per slug (F1).
- **Set the variables only when the cache is on.** Reading a generation named under an earlier
  bracket is sound with no fingerprint, so withholding it only costs time.

## 5. Production-readiness checklist

- security — every name sits in the worktree's git dir beside the whole key and its record, which
  only the driver writes. Each generation is a `mktemp -d` directory, so no name is known before it
  exists. The name file is read back once, and its line reaches `rm -rf` only after S3's anchored
  check, as a base name joined to `_stdir`. Unit 1's per-spec replay runs no process. A forged
  generation can hide findings from a dispatch only, and the bar's plain run still grades them.
- perf / scale — DERIVED from TOOL-aPiecewiseGrade-1's table, PINNED d9f84ee14: on the tree after
  TOOL-aPiecewiseGrade-3, a pass commit's dispatch on node `a` saves about 1 s (DERIVED d9f84ee14) of a checker run near
  69 s (d9f84ee14). The `mktemp -d` costs 0.022 s to 0.028 s (PINNED dd9006677, unit 4's table).
  The name file's read and write are builtins. AC6 measures the real figure.
- error / empty / loading states — no sidecar root, or a failed `mktemp`, turns the mode off. A
  missing, empty or malformed name file reads as misses. A failed name write leaves the old name live
  and prints nothing.
- observability — the checker's `graded.list` names what each run re-graded, and the name file names
  the live generation. No new driver line.
- risks — the sweep and the removal run `rm -rf`. The sweep's paths come from a glob confined to
  `_stdir` by a slug `check_slug` has already validated, which carries no dot or slash. The removal's
  path is `ST_CACHE`, built from a checked base name or the `.none` name. An empty sidecar root
  leaves both variables empty, which the guards test first.
- testing — the pass probe above, and the driver suite's new arm observed RED then GREEN at the close.
- migration — none. The first miss after install finds no name file, grades every spec, and names
  its generation. A `.next` directory an older checker left matches the sweep's glob and is removed.
- user docs — the verbs guide in both copies.

## 6. Acceptance criteria

Each probe line comes from one run of `bash "$SCRATCH/pg2.sh"`, described in §4, removed after the
pass.

- **AC1** — When `bash "$SCRATCH/pg2.sh"` runs, it prints `first graded 3 live 3 gens 1 named 1`.
  Red when: the driver does not set both variables, so no generation is written, or it leaves the
  name file unwritten or malformed after a recorded key.
- **AC2** — When `bash "$SCRATCH/pg2.sh"` runs, it prints `same skipped 1` and
  `onespec graded 1 gens 1 newname 1`.
  Red when: the incremental run re-grades every spec after one edit, the whole-key skip is lost, the
  name file keeps the old name, or the read half leaves the old generation on disk.
- **AC3** — When `bash "$SCRATCH/pg2.sh"` runs, it prints `moved said 1 kept 1 gens 2` and
  `refused kept 1 gens 2`.
  Red when: the driver names a generation on a branch where the whole key is not recorded, the sweep
  removes the live generation, so `refused` reads `kept 0`, or the start half does not sweep the
  generation the `moved` step left, so `refused` counts three.
- **AC4** — When `bash "$SCRATCH/pg2.sh"` runs, it prints `lines same 1`.
  Red when: any printed line of `run_spec_token_check` moves, or a line is added.
  fixture: the base driver is a worktree at the base before this unit under `%TEMP%/pg2b`.
- **AC5** — When `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` runs it
  prints nothing, and `grep -c 're-grades the rest and runs every cross-build join whole' memory/guides/UNATTENDED-VERBS.md`
  prints 1.
  Red when: one copy is edited without its twin, or the sentence is missing.
- **AC6** — When the main loop runs `bash "$SCRATCH/pg2-time.sh"` at the close on node `a`, it
  prepares one frozen shared clone at the build's tip, dispatches its last unit once to prime both
  caches, and commits that unit's spec as CLOSED, as a sequential pass commit does. It then runs one
  timed `run_spec_token_check` with the base driver and checker and one with the built ones, from
  that same commit, each from a fresh copy of the primed sidecar. Their exit statuses match, `cmp`
  over their outputs prints nothing, and the two times are recorded beside the script in the build's
  records.
  Red when: the outputs differ, or the built run re-grades more than the one spec the commit moved.
  permission: it runs the whole-tree checker, which only the main loop may run.
  cost: two primed runs and two timed runs, near 69 s each on node `a` after TOOL-aPiecewiseGrade-3. <!-- DERIVED from TOOL-aPiecewiseGrade-1's table, PINNED d9f84ee14 -->
  figure: both times are DERIVED at observation.
- **AC7** — When `bash "$SCRATCH/pg2.sh"` runs, it prints `lint fixed 2 admitted 6 unfollowed 0`.
  Red when: the driver gains an `mv` of any class, a generation renamed into place among them.
  figure: the three counts are `scan_temp_file` over the driver before this unit, PINNED a07d7914f,
  and the 2 is the registry row's count for `tools/unattended/unattended.sh`.
- **AC8** — When `bash "$SCRATCH/pg2.sh"` runs, it prints `planted spared 1 graded 3 gens 1 named 1`.
  Red when: a name read back from the name file reaches `rm -rf` without the shape check, so the
  planted directory is removed, or a malformed name leaves the cache unreplaced.

## 7. Gates

`unattended kit gate` · `spec-tokens self-test` · `scratch-guard self-test` · `tier2-review self-test` · `recall floor` · `recall floor arms` · `harness arms (fail branches armed or pinned)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a fixed-name temp renamed into place)` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `memory hygiene`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC8 · after TOOL-aLightenedLoop-3's cache steps: the name file naming a well-formed generation after an admit, one spec re-graded and one generation left after a one-spec commit, the name file and the live generation unmoved on a moved tree and on a refusal, and a planted malformed name sparing its target directory; staged RED by naming on every branch, then by dropping the shape check, then by letting the sweep remove the live generation · the driver suite's assertion floor, raised by the count of new assertions, which the close confirms

The close runs the bar once, after the last unit is terminal. This spec's author ran no gate but
the spec-token checker's `--spec` over this file and the positional check.

## 8. Open questions

- **F1 — Is the per-spec cache one per slug or one per worktree?**
  An entry depends on no slug, because the checker's output does not; only the dispatch verdict
  reads the slug. Options:
  - (a) One per slug, `spec-tokens.<slug>.specs`, beside that slug's whole key and record. A second
    slug in the same worktree grades every spec on its first miss. Its next generation is its own,
    so two slugs never promote each other's entries.
  - (b) One per worktree, `spec-tokens.specs`. A second slug reuses the first's entries. But two
    slugs' dispatches would share one `<dir>.next`, and one could promote the other's entries
    without the other's bracket.
  Recommendation: (a). The sidecar is per worktree and a run lives in one worktree, so a second
  slug there is rare, and (b) adds a cross-slug promotion race to save its first miss.
  RESOLVED (owner, 2026-11-15): (a) One per slug

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft from brief `2026-11-15-prompt-TOOL-aPiecewiseGrade-1-brief`,
  item 8, grounded at `aebbb4a72` and at aLightenedLoop's head `d9f84ee14`.
- rev-2 · 2026-11-15 · §1 · S1 · §3 · §4 · §5 · AC6 · §8 · from brief
  `2026-11-15-prompt-TOOL-aPiecewiseGrade-3-forks-brief`, item 4: F1 RESOLVED as the owner's (a), the
  per-slug cache stated as the only layout, order 2 to 3 with the ratified pointer, the build order on the edge, and the perf
  and AC6 cost lines read against the tree after TOOL-aPiecewiseGrade-3 so they agree with unit 1.
- rev-3 · 2026-11-15 · §1 · S1 · S2 · S4 · S6 · §3 · §4 · §5 · AC1 · AC3 · AC7 · §7 · from the builder's
  divergence `2026-11-15-prompt-TOOL-aPiecewiseGrade-2-revision` and brief
  `2026-11-15-prompt-TOOL-aPiecewiseGrade-4-forks-brief`, item 4: the promotion renames a `mktemp -d`
  directory named in TOOL-aPiecewiseGrade-4's `SPEC_TOKENS_CACHE_NEXT`, per that unit's F1
  recommendation, with a sweep at the start; order 3 to 4 and a consumes-from edge on
  TOOL-aPiecewiseGrade-4; the verbs-guide sentence placed after "runs the checker."; the read half
  derives the cache path from `_strec` and carries `ST_NEXT` as an eighth global; §4 regrounded on the
  reconciled driver at `a9ff4a9c`; the lint observation added as AC7.
- rev-4 · 2026-11-15 · §1 · S1 · S2 · S3 · S4 · S5 · S6 · S7 · S8 · §3 · §4 · §5 · AC1 · AC2 · AC3 ·
  AC7 · AC8 · §7 · §10 · from brief `2026-11-15-prompt-TOOL-aPiecewiseGrade-2-1-spec-writer`, the
  owner's answer (b) to TOOL-aPiecewiseGrade-4's F1: no rename. The read half writes the new
  generation's base name into `spec-tokens.<slug>.live` where the whole key is recorded and removes
  the old generation; the start half resolves the cache through that file behind an anchored shape
  check, with `spec-tokens.<slug>.specs.none` when no name passes, and sweeps every generation but
  the live one; `ST_CACHE` joins `ST_NEXT` as a ninth global; the kill-window table added; scope
  renumbered S1 to S8 with the shape check and the sweep as their own items; AC1 to AC3 read the
  name file; AC7 pins all three lint counts at `a07d7914f`; AC8 added for a planted malformed name;
  the verbs-guide sentence's last clause reworded; §4 re-read at `a07d7914f`.

## 10. Reuse audit

The seams this unit extends: `run_spec_token_check` and its start half, at the one site that records
the whole key (`tools/unattended/unattended.sh@a9ff4a9c:14667`), the existing `SPEC_TOKENS_INPUTS=`
call prefix, which carries the two new variables beside it, and the `ST_` globals, which carry two
more. The name file's write copies the whole key's own write at that site, and its read copies the
key's read-back (`tools/unattended/unattended.sh@a9ff4a9c:14600`). The sidecar root is
`resolve_sidecar_dir`'s answer, the one spelling of it. The generation's name follows the driver's
own `mktemp` beside a destination (`tools/unattended/unattended.sh@a9ff4a9c:2066`). The shape check
matches the whole line, as `check_slug_shape` matches the whole slug. The verbs guide's cache sentence
is TOOL-aLightenedLoop-3's, extended. `tools/codebase-map/reuse_lookup.py` for "cache each spec's
grading on the inputs it read and re-grade only the specs whose inputs moved" ranked generic name
stems only (`read_text`, `read`, `read_bytes`), so no promotion or generation seam fits beyond these.
Recall's top hits were TOOL-aSmoothedDispatch-4, the first key, TOOL-aBriskDeclaration-1, the two
halves, and TOOL-aLightenedLoop-3, the key this run sits behind; for the promotion, TOOL-dRedressedBar-24,
the lint's one-hop rule.

Recall terms used: `python tools/memory-recall/query.py "how can the spec-token checker re-grade only specs whose inputs moved while cross-build joins stay whole" --terms "spec-token checker incremental per-spec cache input record replay waiver stale carries packet dispatch key"`
