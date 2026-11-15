# TOOL-aPiecewiseGrade-2 — `run_spec_token_check` runs the checker's incremental mode on a whole-key miss, and promotes its per-spec cache only where the whole key is recorded

**Status:** INPROGRESS · rev-2 · 2026-11-15 · node a · Tier-2 · base aebbb4a72 · streams tooling · order 3 · ratified 2026-11-15

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-prompt-TOOL-aPiecewiseGrade-1-brief.md](../prompts/2026-11-15-prompt-TOOL-aPiecewiseGrade-1-brief.md) | research | TOOL-aPiecewiseGrade-1 |
| [2026-11-15-prompt-TOOL-aPiecewiseGrade-3-forks-brief.md](../prompts/2026-11-15-prompt-TOOL-aPiecewiseGrade-3-forks-brief.md) | research | TOOL-aPiecewiseGrade-3 TOOL-aPiecewiseGrade-1 |

<!-- /gen:spec-records -->

## 1. Goal

When aLightenedLoop's whole key misses, `--dispatch` runs the spec-token checker with
`SPEC_TOKENS_CACHE` naming a per-slug directory under the sidecar root. A pass commit that moves one
spec then re-grades that spec alone, and every join still runs whole. The driver promotes the
checker's next generation only where it records the whole key, so the per-spec cache holds only
what a still tree produced. Not one printed byte of `--dispatch` moves. This unit builds third, after
TOOL-aPiecewiseGrade-3 and TOOL-aPiecewiseGrade-1, because the owner kept the incremental mode at
TOOL-aPiecewiseGrade-1's F1.

## 2. Scope (IN)

- **S1** — Every checker call that `run_spec_token_check`'s two halves make with
  `SPEC_TOKENS_INPUTS` set also sets `SPEC_TOKENS_CACHE` to `spec-tokens.<slug>.specs` under the
  sidecar root, or to nothing when the sidecar root does not resolve. The cache is one per slug,
  its only layout (F1). Observed by AC1 and AC2.
- **S2** — Where the driver writes the whole key, it then promotes `<dir>.next`, when it exists,
  into the per-slug directory's place, with the two commands §4 shows. No other branch promotes.
  Observed by AC1, AC2 and AC3.
- **S3** — The skip line, the cache-off line, the not-recorded line, the admit note and every
  refusal keep their bytes, and no line is added. Observed by AC4.
- **S4** — The verbs guide states the incremental run in both copies, which stay byte-identical.
  Observed by AC5.
- **S5** — A timed `--dispatch` on node `a` after a sequential pass commit, base against built.
  Observed by AC6.

## 3. Non-goals (OUT)

- No change to the whole key, `derive_spec_token_key`, `read_tree_state` or the conditions under which
  the whole key is recorded. Its miss is the only trigger.
- No change to `check_spec_token_hits` or any verdict, refusal, status or summary of `--dispatch`.
- No scoping of the check to the dispatching build.
- No new announcement line, such as a re-graded count. The checker's `graded.list` is the record.
- No promotion on a refusal, a moved tree, a missing record or an unreplayable one, which are the
  branches where the whole key is not recorded either.
- No change to the bar's spec-tokens leg, which keeps the plain run.
- No edit to the unattended Skill, and no kit version bump by hand.

### Edges

- **consumes-from** `TOOL-aPiecewiseGrade-1` — the incremental mode behind `SPEC_TOKENS_CACHE`, and its contract that the checker writes only `<dir>.next` and the caller promotes it. TOOL-aPiecewiseGrade-3 builds at order 1, that unit at order 2, and this one at order 3
- **consumes-from** external — aLightenedLoop's whole key reconciled onto main's two-half `run_spec_token_check`

## 4. Design

### What the code does today

Read at `d9f84ee14`, aLightenedLoop's head, and at `aebbb4a72`, this build's base. The driver's blob
is `77c9dc8b` at the first and `eb567029` at the second. The two differ, and the design is for the
tree after aLightenedLoop reconciles onto main.

- At `d9f84ee14`, `run_spec_token_check` (`tools/unattended/unattended.sh@77c9dc8b:14564`) sets the
  key and record paths under the sidecar root (`tools/unattended/unattended.sh@77c9dc8b:14572`). It
  runs the checker once with `SPEC_TOKENS_INPUTS` set
  (`tools/unattended/unattended.sh@77c9dc8b:14586`), and writes the whole key at one site, after the
  verdict admits and the tree state held (`tools/unattended/unattended.sh@77c9dc8b:14611`). Every
  other branch prints the not-recorded line (`tools/unattended/unattended.sh@77c9dc8b:14614`) or
  returns earlier.
- At `aebbb4a72`, TOOL-aBriskDeclaration-1 split the check into a start half,
  `init_spec_token_check` (`tools/unattended/unattended.sh@eb567029:14478`), which starts the
  checker through `init_bounded` (`tools/unattended/unattended.sh@eb567029:14496`). The read half is
  `run_spec_token_check` (`tools/unattended/unattended.sh@eb567029:14506`), which reads the started
  checker or runs it synchronously through `run_bounded` when no start was made
  (`tools/unattended/unattended.sh@eb567029:14528`). It writes the key at one site
  (`tools/unattended/unattended.sh@eb567029:14539`).
- `resolve_sidecar_dir` (`tools/unattended/lib-unattended.sh#resolve_sidecar_dir`) answers
  `<git-dir>/unattended`, the worktree's own git dir, or nothing.
- `read_bounded` folds the child's stderr into `RB_OUT`
  (`tools/unattended/unattended.sh@eb567029:323`), which `check_spec_token_hits` reads. So the
  checker's mode must print nothing on stderr either, which unit 1 states.
- The driver suite's spec-token arms build a fixture with the real checker, a clean `tRun` spec and a
  `tOther` spec that reds, and call `run_spec_token_check tRun` in process
  (`tools/unattended/unattended.test.sh@4c39bc50:7815`). TOOL-aLightenedLoop-3's cache steps follow
  (`tools/unattended/unattended.test.sh@4c39bc50:7834`).

After the reconcile, the start half derives the whole-key lookup over the record, reads the tree
state and starts the checker with `SPEC_TOKENS_INPUTS` set. The read half takes the verdict,
re-reads the tree state, and writes the key at one site. This unit names its sites by those roles,
because no sha holds the reconciled text yet.

### S1 — the variable on every checker call

Beside the record path, the driver sets `_stspecs="$_stdir/spec-tokens.$slug.specs"`, or leaves it
empty when the sidecar root does not resolve. That per-slug directory is the cache's only layout:
each slug's entries sit beside that slug's whole key and record, and each slug promotes only its own
next generation. Every checker call that carries
`SPEC_TOKENS_INPUTS=$_stin`, the start half's `init_bounded` and the read half's `run_bounded`
fallback, also carries `SPEC_TOKENS_CACHE=$_stspecs`. An empty value turns the mode off, and the
checker then runs exactly the plain run.

With the cache off, meaning no fingerprint, the variable is still set. Every entry in the directory
was promoted under an earlier bracket, so reading it is sound. Nothing is promoted without a bracket.

### S2 — promotion at the whole key's one write site

Right after the line that writes the whole key, and only there:

```bash
if [ -n "$_stspecs" ] && [ -d "$_stspecs.next" ]; then
  { rm -rf "$_stspecs" && mv "$_stspecs.next" "$_stspecs"; } 2>/dev/null || :
fi
```

That site is reached only when three things hold, the conditions TOOL-aLightenedLoop-3 S6 records
the whole key under: the verdict admitted, the tree state read before the checker equals the one
read after the key's replay, and the record replays. So an entry is promoted only when nothing moved
while the checker read and keyed it. On every other branch the next generation stays where it is,
and the checker removes it before its next write. A failed `rm` or `mv` costs misses at the next
miss of the whole key, never a refusal. A crash between the two leaves no live directory, which reads
as a miss for every spec.

### S3 — every printed byte

The variable reaches only the checker, and unit 1 holds the checker's stdout, stderr and status equal
to the plain run's. Promotion prints nothing. So `check_spec_token_hits` reads the same `RB_OUT`, and
every line `run_spec_token_check` prints is unchanged: the skip line, the cache-off line, the
not-recorded line with its three reasons, the admit note naming another build's hit, and the
check-49 refusals.

### S4 — the verbs guide

`tools/unattended/VERBS.template.md` states the whole key after the reconcile in the sentence ending
"recorded under the sidecar root only when the tree and HEAD held still while it ran"
(`tools/unattended/VERBS.template.md@d92b6991:254`). One sentence follows it:

```
On a miss it runs the checker's incremental mode, which reuses each live spec's findings from a
per-spec cache under the sidecar root while that spec's own inputs hold,
re-grades the rest and runs every cross-build join whole,
so its output is the whole-tree run's; that cache moves only where the key is recorded.
```

The phrase `re-grades the rest and runs every cross-build join whole` is spelled on one line, as
written. `memory/guides/UNATTENDED-VERBS.md` takes the identical edit, because the two files are
byte-identical at `aebbb4a72` and at `d9f84ee14`. No `help/` page names the dispatch cache, grepped
at `aebbb4a72`.

### What the design does not check

Carried from TOOL-aLightenedLoop-3's "What the key does not check", for the whole key that triggers
this run: a path probed only for existence, the environment beyond the recorded delta, and a
package upgraded in place. Unit 1's own list holds for the per-spec keys.

New with this design:

- **Two dispatches of one slug running at once in one worktree** share one `<dir>.next`. Nothing
  serializes them, as nothing serializes the whole key's record today. The main loop runs each
  dispatch in the foreground, one at a time, which is what `dispatch.declare` tells it.
- **The bracket's reach.** It reads the run-gates fingerprint and HEAD, before the checker and
  after the replay. An edit made and undone inside the run leaves both reads equal. If the checker
  graded the edited bytes and keyed the restored ones, the promoted entry holds findings over bytes
  the tree no longer has, and a later lookup over the restored bytes hits it. The whole key carries
  the same gap today, for the same reason.
- **A promotion that fails halfway** leaves no live directory. Every spec re-grades at the next miss.

### The pass probe, `$SCRATCH/pg2.sh`

The probe builds a fixture repository at `$TEMP/pg2`, as TOOL-aLightenedLoop-3's `l3.sh` does,
holding the built checker, the memory-tree kit and the run-gates fingerprint script copied into its
tool root. It sources the built driver, loads its conf, and sets `SPEC_TOKENS_CLI` to the copied
checker. The seed has two live specs in build `tA`, one in `tB` that reds, and an empty waiver file.
`S` is the sidecar's `spec-tokens.tA.specs`.

| step | what happens | the line it prints |
|---|---|---|
| `first` | `run_spec_token_check tA` | `first graded <lines of $S/graded.list> live <.json files in $S> next <0|1>` |
| `same` | the same call again | `same skipped <count of the skip line>` |
| `onespec` | one `tA` spec's prose edited and committed, then the call | `onespec graded <n> next <0|1>` |
| `moved` | the checker wrapped by a stub that calls the real module's `main`, then appends to a file the record names before exiting | `moved said <count of the moved reason> kept <0|1> next <0|1>` |
| `refused` | a `tA` spec made to red, then the call | `refused kept <0|1>` |

`kept` is 1 when `find "$S" -type f -exec sha1sum {} +` prints the same bytes before and after the
call. `next` is 1 when `$S.next` exists after the call. The probe then repeats the five steps over a
fresh fixture with the base driver, the reconciled one before this unit, from a worktree at that
base under `%TEMP%/pg2b`. It prints `lines same <0|1>`, from `cmp` over the two drivers' captured
output, every step concatenated.

### Inventory

| identifier | kind | lexicon |
|---|---|---|
| `_stspecs` | local in `run_spec_token_check` and its start half | no declared cell for a shell local |
| `spec-tokens.<slug>.specs` and `spec-tokens.<slug>.specs.next` | sidecar directories | no declared cell |

No shell function, conf key, check number or refusal line is minted. `SPEC_TOKENS_CACHE` is unit 1's.

### Docs, and what the change owes beyond the code

- The verbs guide in both copies, per S4.
- No `help/` page, per S4.
- No new function, so the codebase map's symbol index does not move. The `unattended` dossier names
  the driver's paths, which do not move.
- The kit epoch leg sees shipped bytes move, and the lander's mint moves the version.

### Rollout

This unit builds after units 3 and 1, against the reconciled driver. Every cited line moves, so the builder
finds each site by its text: the record path's assignment, each `SPEC_TOKENS_INPUTS=` prefix, and the
whole key's `printf`. The driver suite's assertion floor rises by the new assertions, which the
close confirms from a real run.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`

### Alternatives rejected

- **Promote on every run where the tree held still, refusals included.** The entries would be sound.
  But the brief keys the write on the conditions TOOL-aLightenedLoop-3 S6 records its key under, and
  one rule for both caches is one fact. A re-dispatch after a refusal then reuses the last admitted
  generation and re-grades what moved since.
- **A promotion helper function.** It would have one caller and two lines.
- **Let the checker promote itself.** The checker cannot see the run-gates fingerprint or the replay
  window. The bracket is the driver's, so the promotion is too.
- **One cache per worktree, shared by every slug.** Two slugs' dispatches would share one
  `<dir>.next`, and one could promote the other's entries outside the other's bracket. The owner
  chose one per slug (F1).
- **Set the variable only when the cache is on.** Reading entries promoted under an earlier bracket
  is sound with no fingerprint, so withholding it only costs time.

## 5. Production-readiness checklist

- security — the directory lives in the worktree's git dir beside the whole key and its record, which
  only the driver writes. Unit 1's per-spec replay runs no process. A forged generation can hide
  findings from a dispatch only, and the bar's plain run still grades them.
- perf / scale — DERIVED from TOOL-aPiecewiseGrade-1's table, PINNED d9f84ee14: on the tree after
  TOOL-aPiecewiseGrade-3, a pass commit's dispatch on node `a` saves about 1 s (DERIVED d9f84ee14) of a checker run near
  69 s (d9f84ee14). AC6 measures the real figure.
- error / empty / loading states — no sidecar root turns the mode off. A missing or half-promoted
  directory reads as misses. A failed promotion prints nothing.
- observability — the checker's `graded.list` names what each run re-graded. No new driver line.
- risks — the promotion runs `rm -rf` on a path the driver composes from the sidecar root and the
  slug. `check_slug` has already validated the slug, and an empty sidecar root leaves `_stspecs`
  empty, which the guard tests first.
- testing — the pass probe above, and the driver suite's new arm observed RED then GREEN at the close.
- migration — none. The first miss after install grades every spec and promotes.
- user docs — the verbs guide in both copies.

## 6. Acceptance criteria

Each probe line comes from one run of `bash "$SCRATCH/pg2.sh"`, described in §4, removed after the
pass.

- **AC1** — When `bash "$SCRATCH/pg2.sh"` runs, it prints `first graded 3 live 3 next 0`.
  Red when: the driver does not set `SPEC_TOKENS_CACHE`, so no generation is written, or it leaves
  `.next` unpromoted after a recorded key.
- **AC2** — When `bash "$SCRATCH/pg2.sh"` runs, it prints `same skipped 1` and `onespec graded 1 next 0`.
  Red when: the incremental run re-grades every spec after one edit, or the whole-key skip is lost.
- **AC3** — When `bash "$SCRATCH/pg2.sh"` runs, it prints `moved said 1 kept 1 next 1` and
  `refused kept 1`.
  Red when: the driver promotes on a branch where the whole key is not recorded.
- **AC4** — When `bash "$SCRATCH/pg2.sh"` runs, it prints `lines same 1`.
  Red when: any printed line of `run_spec_token_check` moves, or a line is added.
  fixture: the base driver is a worktree at the reconciled base under `%TEMP%/pg2b`.
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

## 7. Gates

`unattended kit gate` · `spec-tokens self-test` · `scratch-guard self-test` · `tier2-review self-test` · `recall floor` · `recall floor arms` · `harness arms (fail branches armed or pinned)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a fixed-name temp renamed into place)` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `memory hygiene`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 · after TOOL-aLightenedLoop-3's cache steps: the generation promoted on an admit, one spec re-graded after a one-spec commit, and nothing promoted on a moved tree or a refusal; staged RED by promoting on every branch, then by dropping the variable from the checker call · the driver suite's assertion floor, raised by the count of new assertions, which the close confirms

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

## 10. Reuse audit

The seams this unit extends: `run_spec_token_check` and its start half, at the one site that records
the whole key (`tools/unattended/unattended.sh@77c9dc8b:14611`, `tools/unattended/unattended.sh@eb567029:14539`),
and the existing `SPEC_TOKENS_INPUTS=` call prefix, which carries the new variable beside it. The
sidecar root is `resolve_sidecar_dir`'s answer, the one spelling of it. The verbs guide's
cache sentence is TOOL-aLightenedLoop-3's, extended. `tools/codebase-map/reuse_lookup.py` for
"cache each spec's grading on the inputs it read and re-grade only the specs whose inputs moved"
ranked generic name stems only (`read_text`, `read`, `read_bytes`), so no promotion or generation
seam fits beyond these. Recall's top hits were TOOL-aSmoothedDispatch-4, the first key,
TOOL-aBriskDeclaration-1, the two halves, and TOOL-aLightenedLoop-3, the key this run sits behind.

Recall terms used: `python tools/memory-recall/query.py "how can the spec-token checker re-grade only specs whose inputs moved while cross-build joins stay whole" --terms "spec-token checker incremental per-spec cache input record replay waiver stale carries packet dispatch key"`
