# TOOL-aPiecewiseGrade-2 — `run_spec_token_check` runs the checker's incremental mode on a whole-key miss, and promotes its per-spec cache only where the whole key is recorded

**Status:** SPECCED · rev-3 · 2026-11-15 · node a · Tier-2 · base aebbb4a72 · streams tooling · order 4 · ratified 2026-11-15

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-prompt-TOOL-aPiecewiseGrade-1-brief.md](../prompts/2026-11-15-prompt-TOOL-aPiecewiseGrade-1-brief.md) | research | TOOL-aPiecewiseGrade-1 |
| [2026-11-15-prompt-TOOL-aPiecewiseGrade-2-revision.md](../prompts/2026-11-15-prompt-TOOL-aPiecewiseGrade-2-revision.md) | research | — |
| [2026-11-15-prompt-TOOL-aPiecewiseGrade-3-forks-brief.md](../prompts/2026-11-15-prompt-TOOL-aPiecewiseGrade-3-forks-brief.md) | research | TOOL-aPiecewiseGrade-3 TOOL-aPiecewiseGrade-1 |
| [2026-11-15-prompt-TOOL-aPiecewiseGrade-4-forks-brief.md](../prompts/2026-11-15-prompt-TOOL-aPiecewiseGrade-4-forks-brief.md) | research | TOOL-aPiecewiseGrade-4 |

<!-- /gen:spec-records -->

## 1. Goal

When aLightenedLoop's whole key misses, `--dispatch` runs the spec-token checker with
`SPEC_TOKENS_CACHE` naming a per-slug directory under the sidecar root, and
`SPEC_TOKENS_CACHE_NEXT` naming a directory made with `mktemp -d` beside it. A pass commit that
moves one spec then re-grades that spec alone, and every join still runs whole. The driver renames
the named generation into place only where it records the whole key, so the per-spec cache holds
only what a still tree produced, and no fixed-name temp is renamed. Not one printed byte of
`--dispatch` moves. This unit builds fourth, after TOOL-aPiecewiseGrade-3, TOOL-aPiecewiseGrade-1 and
TOOL-aPiecewiseGrade-4, whose contract it promotes on.

## 2. Scope (IN)

- **S1** — Every checker call that `run_spec_token_check`'s two halves make with
  `SPEC_TOKENS_INPUTS` set also sets `SPEC_TOKENS_CACHE` to `spec-tokens.<slug>.specs` under the
  sidecar root and `SPEC_TOKENS_CACHE_NEXT` to a directory the start half made with `mktemp -d`
  beside it. Both are empty when the sidecar root does not resolve or `mktemp` fails. The start half
  carries the directory in an eighth global, `ST_NEXT`, and the read half derives the cache path
  from the record path. The cache is one per slug, its only layout (F1). Observed by AC1 and AC2.
- **S2** — Where the driver writes the whole key, it then renames the named directory over the
  per-slug directory, with the two commands §4 shows. No other branch promotes. Before it makes a
  directory, the start half removes every generation an earlier run of that slug left. Observed by
  AC1, AC2 and AC3.
- **S3** — The skip line, the cache-off line, the not-recorded line, the admit note and every
  refusal keep their bytes, and no line is added. Observed by AC4.
- **S4** — The verbs guide states the incremental run in both copies, which stay byte-identical.
  Observed by AC5.
- **S5** — A timed `--dispatch` on node `a` after a sequential pass commit, base against built.
  Observed by AC6.
- **S6** — The driver's promotion adds no `fixed` site to the shell-hygiene lint's count, so the
  registry keeps its row as it stands. Observed by AC7.

## 3. Non-goals (OUT)

- No change to the whole key, `derive_spec_token_key`, `read_tree_state` or the conditions under which
  the whole key is recorded. Its miss is the only trigger.
- No change to `check_spec_token_hits` or any verdict, refusal, status or summary of `--dispatch`.
- No scoping of the check to the dispatching build.
- No new announcement line, such as a re-graded count. The checker's `graded.list` is the record.
- No promotion on a refusal, a moved tree, a missing record or an unreplayable one, which are the
  branches where the whole key is not recorded either.
- No row raised in `memory/project/temp-name-sites.txt`, and no promotion by copying.
- No change to the bar's spec-tokens leg, which keeps the plain run.
- No edit to the unattended Skill, and no kit version bump by hand.

### Edges

- **consumes-from** `TOOL-aPiecewiseGrade-1` — the incremental mode behind `SPEC_TOKENS_CACHE`, its per-spec key and its `graded.list`. The build order is TOOL-aPiecewiseGrade-3 at order 1, TOOL-aPiecewiseGrade-1 at order 2, TOOL-aPiecewiseGrade-4 at order 3 and this unit at order 4
- **consumes-from** `TOOL-aPiecewiseGrade-4` — the contract that the checker writes its next generation into the directory `SPEC_TOKENS_CACHE_NEXT` names, made by the caller with `mktemp -d`, and never creates or removes it; without it the only promotion is a fixed-name temp renamed into place. That unit builds at order 3, before this one
- **consumes-from** external — aLightenedLoop's whole key on the two-half `run_spec_token_check`, landed at `4bd7215ce`

## 4. Design

### What the code does today

Read at `dd9006677`, where aLightenedLoop has landed and the driver's blob is `a9ff4a9c`. Rev-2
grounded at `aebbb4a72` and at aLightenedLoop's head `d9f84ee14`, before the reconciled text existed.

- The start half, `init_spec_token_check` (`tools/unattended/unattended.sh#init_spec_token_check`),
  resolves the sidecar root into its local `_stdir` and sets `ST_REC` and `ST_IN` beside it
  (`tools/unattended/unattended.sh@a9ff4a9c:14598`). On a run it removes the old record and makes the
  sidecar directory (`tools/unattended/unattended.sh@a9ff4a9c:14606`), then starts the checker
  through `init_bounded` with `SPEC_TOKENS_INPUTS` set (`tools/unattended/unattended.sh@a9ff4a9c:14609`).
- It hands the read half its state through seven `ST_` globals, declared at
  `tools/unattended/unattended.sh@a9ff4a9c:14588` and emptied by `remove_spec_token_check`.
- The read half, `run_spec_token_check`, copies the globals into locals and empties them
  (`tools/unattended/unattended.sh@a9ff4a9c:14622`). It has no `_stdir`; its record path is `_strec`.
  It runs the checker synchronously through `run_bounded` when no start was made
  (`tools/unattended/unattended.sh@a9ff4a9c:14641`), derives the key over the record before the
  second tree read (`tools/unattended/unattended.sh@a9ff4a9c:14657`), and writes the whole key at
  one site (`tools/unattended/unattended.sh@a9ff4a9c:14667`). Every other branch prints the
  not-recorded line or returns earlier.
- `resolve_sidecar_dir` (`tools/unattended/lib-unattended.sh#resolve_sidecar_dir`) answers
  `<git-dir>/unattended`, the worktree's own git dir, or nothing.
- `read_bounded` folds the child's stderr into `RB_OUT`
  (`tools/unattended/unattended.sh@a9ff4a9c:324`), which `check_spec_token_hits` reads. So the
  checker's mode must print nothing on stderr either, which unit 1 states.
- `check_slug_shape` admits letters, digits and dashes only
  (`tools/unattended/unattended.sh@a9ff4a9c:3107`), so no slug carries a dot.
- The driver suite's spec-token arms build a fixture with the real checker, a clean `tRun` spec and a
  `tOther` spec that reds, and call `run_spec_token_check tRun` in process
  (`tools/unattended/unattended.test.sh@24f12f1e:7813`). Two text arms grep the driver for
  `run_bounded "$_stpy" "$SPEC_TOKENS_CLI"` and `init_bounded "$ST_PY" "$SPEC_TOKENS_CLI"`
  (`tools/unattended/unattended.test.sh@24f12f1e:4478`), which the prefixes below leave intact.
- The shell-hygiene lint counts 2 `fixed` sites in the driver, which the registry row
  `tools/unattended/unattended.sh fixed-temp 2` declares, and 0 unfollowed (PINNED dd9006677).

### S1 — the variables on every checker call

The start half gains the locals `_stspecs` and `_stold`. Where it removes the record and makes the
sidecar directory, it also sweeps and makes the next generation:

```bash
  if [ -n "$ST_IN" ]; then
    rm -f "$ST_IN" 2>/dev/null; mkdir -p "$_stdir" 2>/dev/null
    for _stold in "$_stdir/spec-tokens.$1.specs."*; do [ ! -d "$_stold" ] || rm -rf "$_stold" 2>/dev/null; done
    ST_NEXT=$(mktemp -d "$_stdir/spec-tokens.$1.specs.XXXXXXXX" 2>/dev/null) || ST_NEXT=""
    [ -z "$ST_NEXT" ] || _stspecs="$_stdir/spec-tokens.$1.specs"
  fi
  SPEC_TOKENS_INPUTS=$ST_IN SPEC_TOKENS_CACHE=$_stspecs SPEC_TOKENS_CACHE_NEXT=$ST_NEXT init_bounded "$ST_PY" "$SPEC_TOKENS_CLI" && ST_HANDLE=$RB_HANDLE
```

`ST_NEXT` joins the seven globals at their declaration, at every line that empties them, in
`remove_spec_token_check` and in the read half's copy line, as `_stnext=$ST_NEXT`. The header
comment's "seven ST_ globals" becomes eight. The read half derives the cache path from the record
path rather than carrying a ninth global, because both come from one `_stdir` and one slug:

```bash
  [ -z "$_stnext" ] || _stspecs="${_strec%.key}.specs"
```

Its `run_bounded` fallback carries `SPEC_TOKENS_CACHE=$_stspecs SPEC_TOKENS_CACHE_NEXT=$_stnext`
beside `SPEC_TOKENS_INPUTS=$_stin`. When the sidecar root does not resolve, or `mktemp` fails, both
are empty and TOOL-aPiecewiseGrade-4's checker runs exactly the plain run.

With the cache off, meaning no fingerprint, the variables are still set, as rev-2 set the one.
Every entry in the cache was promoted under an earlier bracket, so reading it is sound. The read
half returns before the key's write site, so that generation is never promoted, and the next start
sweeps it.

### S2 — promotion at the whole key's one write site

Right after the line that writes the whole key, and only there:

```bash
    if [ -n "$_stnext" ] && [ -d "$_stnext" ]; then
      { rm -rf "$_stspecs" && mv "$_stnext" "$_stspecs"; } 2>/dev/null || :
    fi
```

That site is reached only when three things hold, the conditions TOOL-aLightenedLoop-3 S6 records
the whole key under: the verdict admitted, the tree state read before the checker equals the one
read after the key's replay, and the record replays. So an entry is promoted only when nothing moved
while the checker read and keyed it. On every other branch the generation stays in its own
directory, and the next start's sweep removes it. A failed `rm` or `mv` costs misses at the next
miss of the whole key, never a refusal. A crash between the two leaves no live directory, which
reads as a miss for every spec, and one generation the sweep removes.

This is TOOL-aPiecewiseGrade-4's F1 recommendation (a). The lint follows a binding one hop inside
one function, and the directory is bound in the start half and renamed in the read half, so it
reads the `mv` as unfollowed: counted, printed, never gated, and no coverage. AC3 and AC7 observe
the name instead. If the owner picks that fork's (b), this section is rewritten before the build.

### S3 — every printed byte

The variables reach only the checker, and units 1 and 4 hold the checker's stdout, stderr and
status equal to the plain run's. The sweep, `mktemp` and the promotion print nothing. So
`check_spec_token_hits` reads the same `RB_OUT`, and every line `run_spec_token_check` prints is
unchanged: the skip line, the cache-off line, the not-recorded line with its three reasons, the
admit note naming another build's hit, and the check-49 refusals.

### S4 — the verbs guide

`tools/unattended/VERBS.template.md` states the whole key in the clause ending "recorded under the
sidecar root only when the tree and HEAD held still while it ran", and that sentence continues to
"runs the checker." (`tools/unattended/VERBS.template.md@c70b591a:258`). The new sentence goes
after "runs the checker." and before "A blank or absent key is an ANNOUNCED skip":

```
On a miss it runs the checker's incremental mode, which reuses each live spec's findings from a
per-spec cache under the sidecar root while that spec's own inputs hold,
re-grades the rest and runs every cross-build join whole,
so its output is the whole-tree run's; that cache moves only where the key is recorded.
```

The phrase `re-grades the rest and runs every cross-build join whole` is spelled on one line, as
written. `memory/guides/UNATTENDED-VERBS.md` takes the identical edit, because the two files are
byte-identical at `dd9006677`, blob `c70b591a`. No `help/` page names the dispatch cache, grepped at
`aebbb4a72`.

### What the design does not check

Carried from TOOL-aLightenedLoop-3's "What the key does not check", for the whole key that triggers
this run: a path probed only for existence, the environment beyond the recorded delta, and a
package upgraded in place. Unit 1's own list holds for the per-spec keys, and unit 4's for the named
directory.

New with this design:

- **Two dispatches of one slug running at once in one worktree.** The second start's sweep removes
  the first's generation, and the first's promotion then finds no directory and leaves the cache
  empty. Nothing serializes them, as nothing serializes the whole key's record today. The main loop
  runs each dispatch in the foreground, one at a time, which is what `dispatch.declare` tells it.
- **The bracket's reach.** It reads the run-gates fingerprint and HEAD, before the checker and
  after the replay. An edit made and undone inside the run leaves both reads equal. If the checker
  graded the edited bytes and keyed the restored ones, the promoted entry holds findings over bytes
  the tree no longer has, and a later lookup over the restored bytes hits it. The whole key carries
  the same gap today, for the same reason.
- **The rename's name, to the lint.** The lint reads the promotion as unfollowed and so says nothing
  about it. AC3's `named` field is what observes that the directory came from `mktemp`.
- **A promotion that fails halfway** leaves no live directory. Every spec re-grades at the next miss.

### The pass probe, `$SCRATCH/pg2.sh`

The probe builds a fixture repository at `$TEMP/pg2`, as TOOL-aLightenedLoop-3's `l3.sh` does,
holding the built checker, the memory-tree kit and the run-gates fingerprint script copied into its
tool root. It sources the built driver, loads its conf, and sets `SPEC_TOKENS_CLI` to the copied
checker. The seed has two live specs in build `tA`, one in `tB` that reds, and an empty waiver file.
`S` is the sidecar's `spec-tokens.tA.specs`.

| step | what happens | the line it prints |
|---|---|---|
| `first` | `run_spec_token_check tA` | `first graded <lines of $S/graded.list> live <.json files in $S> next <n>` |
| `same` | the same call again | `same skipped <count of the skip line>` |
| `onespec` | one `tA` spec's prose edited and committed, then the call | `onespec graded <n> next <n>` |
| `moved` | the checker wrapped by a stub that calls the real module's `main`, then appends to a file the record names before exiting | `moved said <count of the moved reason> kept <0|1> next <n> named <0|1>` |
| `refused` | a `tA` spec made to red, then the call | `refused kept <0|1> next <n>` |
| `lint` | `scan_temp_file` over the built driver's text | `lint fixed <count> unfollowed <each unfollowed source>` |

`kept` is 1 when `find "$S" -type f -exec sha1sum {} +` prints the same bytes before and after the
call. `next` counts the directories matching `$S.*` after the call. `named` is 1 when the one left
is `$S.` followed by eight letters or digits, the shape `mktemp` gives, and not `$S.next`. The `lint`
row reads `tools/gate-lint/sh_hygiene.py#scan_temp_file` through an import, which runs no leg. The
probe then repeats the first five steps over a fresh fixture with the base driver, the one before
this unit, from a worktree at that base under `%TEMP%/pg2b`. It prints `lines same <0|1>`, from `cmp`
over the two drivers' captured output, every step concatenated.

### Inventory

| identifier | kind | lexicon |
|---|---|---|
| `ST_NEXT` | the eighth global between the two halves | no declared cell for a shell global |
| `_stspecs`, `_stold` and `_stnext` | locals of the two halves | no declared cell for a shell local |
| `spec-tokens.<slug>.specs` and `spec-tokens.<slug>.specs.XXXXXXXX` | sidecar directories | no declared cell |

No shell function, conf key, check number or refusal line is minted. `SPEC_TOKENS_CACHE` is unit 1's
and `SPEC_TOKENS_CACHE_NEXT` is unit 4's.

### Docs, and what the change owes beyond the code

- The verbs guide in both copies, per S4.
- No `help/` page, per S4.
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

- **Promote from the fixed name `<dir>.next`.** Rev-2's design. `scan_temp_file` reads its `mv` as
  `fixed`, the gated class, so the registry row would have to rise from 2 to 3 against its
  shrink-only rule. The builder's divergence record shows it, and the owner chose unit 4 instead.
- **Promote on every run where the tree held still, refusals included.** The entries would be sound.
  But the brief keys the write on the conditions TOOL-aLightenedLoop-3 S6 records its key under, and
  one rule for both caches is one fact. A re-dispatch after a refusal then reuses the last admitted
  generation and re-grades what moved since.
- **Remove the generation on each branch that does not promote.** Four sites, the refusals and
  `remove_spec_token_check` among them, and a killed run would still leave one behind. One sweep at
  the start covers every case.
- **Carry the cache path as a ninth global.** It is the record path with another suffix, so it is
  derived where it is read.
- **A promotion helper function.** It would have one caller and two lines.
- **Let the checker promote itself.** Rejected at unit 4 by its tests: it keeps a fixed name, out of
  the lint's sight, and costs a third checker process.
- **One cache per worktree, shared by every slug.** Two slugs' dispatches would sweep and promote
  each other's generations outside the other's bracket. The owner chose one per slug (F1).
- **Set the variables only when the cache is on.** Reading entries promoted under an earlier bracket
  is sound with no fingerprint, so withholding them only costs time.

## 5. Production-readiness checklist

- security — the cache lives in the worktree's git dir beside the whole key and its record, which
  only the driver writes. Each generation is a `mktemp -d` directory, so no name is known before it
  exists. Unit 1's per-spec replay runs no process. A forged generation can hide findings from a
  dispatch only, and the bar's plain run still grades them.
- perf / scale — DERIVED from TOOL-aPiecewiseGrade-1's table, PINNED d9f84ee14: on the tree after
  TOOL-aPiecewiseGrade-3, a pass commit's dispatch on node `a` saves about 1 s (DERIVED d9f84ee14) of a checker run near
  69 s (d9f84ee14). The `mktemp -d` costs 0.022 s to 0.028 s (PINNED dd9006677, unit 4's table).
  AC6 measures the real figure.
- error / empty / loading states — no sidecar root, or a failed `mktemp`, turns the mode off. A
  missing or half-promoted directory reads as misses. A failed promotion prints nothing.
- observability — the checker's `graded.list` names what each run re-graded. No new driver line.
- risks — the sweep and the promotion run `rm -rf` on paths the driver composes from the sidecar
  root and the slug. `check_slug` has already validated the slug, which carries no dot, so the
  sweep's glob reaches no other slug's directory. An empty sidecar root leaves both variables
  empty, which the guards test first.
- testing — the pass probe above, and the driver suite's new arm observed RED then GREEN at the close.
- migration — none. The first miss after install grades every spec and promotes. A `<dir>.next` an
  earlier checker left matches the sweep's glob and is removed.
- user docs — the verbs guide in both copies.

## 6. Acceptance criteria

Each probe line comes from one run of `bash "$SCRATCH/pg2.sh"`, described in §4, removed after the
pass.

- **AC1** — When `bash "$SCRATCH/pg2.sh"` runs, it prints `first graded 3 live 3 next 0`.
  Red when: the driver does not set both variables, so no generation is written, or it leaves the
  named directory unpromoted after a recorded key.
- **AC2** — When `bash "$SCRATCH/pg2.sh"` runs, it prints `same skipped 1` and `onespec graded 1 next 0`.
  Red when: the incremental run re-grades every spec after one edit, or the whole-key skip is lost.
- **AC3** — When `bash "$SCRATCH/pg2.sh"` runs, it prints `moved said 1 kept 1 next 1 named 1` and
  `refused kept 1 next 1`.
  Red when: the driver promotes on a branch where the whole key is not recorded, the start half
  does not sweep the generation an earlier run left, so `refused` counts two, or the generation is
  named `$S.next`.
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
- **AC7** — When `bash "$SCRATCH/pg2.sh"` runs, it prints `lint fixed 2 unfollowed "$_stnext"`.
  Red when: the promotion renames a fixed name, so the count reads 3, or a second rename is added.
  figure: the 2 is the registry row's count for `tools/unattended/unattended.sh`, PINNED dd9006677.

## 7. Gates

`unattended kit gate` · `spec-tokens self-test` · `scratch-guard self-test` · `tier2-review self-test` · `recall floor` · `recall floor arms` · `harness arms (fail branches armed or pinned)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a fixed-name temp renamed into place)` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `memory hygiene`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 · after TOOL-aLightenedLoop-3's cache steps: the generation promoted on an admit, one spec re-graded after a one-spec commit, nothing promoted on a moved tree or a refusal, and one generation left after the refusal; staged RED by promoting on every branch, then by dropping the variables from the checker call, then by dropping the sweep · the driver suite's assertion floor, raised by the count of new assertions, which the close confirms

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

## 10. Reuse audit

The seams this unit extends: `run_spec_token_check` and its start half, at the one site that records
the whole key (`tools/unattended/unattended.sh@a9ff4a9c:14667`), the existing `SPEC_TOKENS_INPUTS=`
call prefix, which carries the two new variables beside it, and the `ST_` globals, which carry one
more. The sidecar root is `resolve_sidecar_dir`'s answer, the one spelling of it. The generation's
name follows the driver's own `mktemp` beside a destination
(`tools/unattended/unattended.sh@a9ff4a9c:2066`). The verbs guide's cache sentence is
TOOL-aLightenedLoop-3's, extended. `tools/codebase-map/reuse_lookup.py` for "cache each spec's
grading on the inputs it read and re-grade only the specs whose inputs moved" ranked generic name
stems only (`read_text`, `read`, `read_bytes`), so no promotion or generation seam fits beyond these.
Recall's top hits were TOOL-aSmoothedDispatch-4, the first key, TOOL-aBriskDeclaration-1, the two
halves, and TOOL-aLightenedLoop-3, the key this run sits behind; for the promotion, TOOL-dRedressedBar-24,
the lint's one-hop rule.

Recall terms used: `python tools/memory-recall/query.py "how can the spec-token checker re-grade only specs whose inputs moved while cross-build joins stay whole" --terms "spec-token checker incremental per-spec cache input record replay waiver stale carries packet dispatch key"`
