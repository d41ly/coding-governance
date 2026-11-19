# TOOL-dTrackedAtlas-9 — a landing counts only on the default branch's first-parent line, never a run branch's prepared merge

**Status:** CLOSED · rev-1 · 2026-11-19 · node d · Tier-1 · base 9e21ac76 · streams tooling · records-only · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-19-build-TOOL-dTrackedAtlas-9-ledger.md](../build/2026-11-19-build-TOOL-dTrackedAtlas-9-ledger.md) | journal | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-8-spec-brief.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-8-spec-brief.md) | research | TOOL-dTrackedAtlas-8 TOOL-dTrackedAtlas-10 TOOL-dTrackedAtlas-11 |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-9-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-9-build-brief.md) | research | — |
| [2026-11-19-review-TOOL-dTrackedAtlas-8-9-10-11-diff-review-round2.md](../reviews/2026-11-19-review-TOOL-dTrackedAtlas-8-9-10-11-diff-review-round2.md) | diff-review | TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-4 TOOL-dTrackedAtlas-8 TOOL-dTrackedAtlas-10 TOOL-dTrackedAtlas-11 |

<!-- /gen:spec-records -->

## 1. Goal

The build-state derivation reads a run branch's prepared "land onto origin/main" merge as a landing,
so at a run-branch tip after the lander's prepare step it marks a held build done and releases its
children (closing review H2). This unit measures every landing against an explicit default-branch
ref that the state document records: a merge counts only when it lies on that ref's first-parent
line and the derived ref contains it.

## 2. Scope (IN)

- **S1** — `derive` takes a default-branch ref, `default_ref`, and the CLI takes it as
  `--default-ref <rev>`. When none is passed, the derivation resolves
  `refs/remotes/<remote>/<branch>` through the remote ladder,
  `tools/lib/resolve_remote.py#resolve_remote`. Observed by AC1, AC2 and AC4.
- **S2** — The landed predicate: a run's landing candidates are the merges on the default commit's
  first-parent line that touch the build's `RUN.md`. A candidate is kept only when the derived commit
  contains it. Observed by AC1, AC2, AC3, AC4 and AC5.
- **S3** — The state document gains `default_ref` and `default_commit`, which `TOOL-dTrackedAtlas-10`
  folds into the page's digest. Observed by AC1, AC4 and AC7.
- **S4** — A default ref that cannot be resolved is a refusal, exit 2. It never falls back to the
  derived ref. Observed by AC6.
- **S5** — The schedule and the Atlas pass no default ref and take the ladder's. Neither grows an
  option. Observed by AC2 for the schedule and AC7 for the Atlas.
- **S6** — The derivation's module docstring and the schedule's INPUTS paragraph state the new rule.
  Observed by AC8.

## 3. Non-goals (OUT)

- The page's digest and `--check --page`: `TOOL-dTrackedAtlas-10` folds this unit's two fields into
  them, in
  `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py#build_stamp` and
  `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py#check_page`.
- Any edit to the Atlas generator. Its `main` gains no option from this unit, so
  `TOOL-dTrackedAtlas-11`'s one option reader has nothing of this unit's to read.
- `scan_forks` and the spec-basename refusal, which are `TOOL-dTrackedAtlas-8`'s.
- A guard on `--ref`'s own value. This unit validates the value it adds.
- Fetching. The derivation reads the remote-tracking ref as it stands and never runs `git fetch`.
- Re-pinning the schedule instrument. This unit's docstring edit moves the schedule's blob again, and
  the open ask `TOOL-dTrackedAtlas-6` re-pins whatever blob stands when the owner acts.
- `tools/policy/check_policy.py#derive_landed_owners`, which is the open ask `TOOL-dTrackedAtlas-5`.
- A gotcha file or a suite arm. This repository's `review.left-shift` is `second-occurrence`, and
  this unit's regression observation is its acceptance, AC1 and AC3.

### Edges

- **hands-off** `TOOL-dTrackedAtlas-10` — folds the document's `default_ref` and `default_commit`
  into the stamp's digest and into `--check --page`; this unit only records them.
- **hands-off** external — the owner's re-pin of the schedule instrument, ask `TOOL-dTrackedAtlas-6`,
  now covers the blob this unit's docstring edit leaves.

## 4. Design

### What is there now

`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py#derive_landings`
lists each build's candidates with
`git log --first-parent --merges --format=%H%x09%s <commit> -- <MEMORY_ROOT>/builds/<slug>/RUN.md`,
where `<commit>` is the derived ref. A run branch's prepared landing merge has exactly that shape.
The lander builds it with the advertised main tip as its first parent and the run branch as its
second, and the run branch then carries on from it. So the merge sits on the run branch's own
first-parent line before main takes it, if main ever does.

Measured on 2026-11-19 with a scratch probe that swaps `derive_landings` (PINNED):

| Commit | What it is | On origin/main's first-parent line |
|---|---|---|
| `67f1ffb18` | dDeclaredLoop's prepared merge, parents `4e6ac5f7c` and `7e5c9ae76` | no |
| `5125f93ea` | dDeclaredLoop's run-branch tip, phase HELD, which carries on from `67f1ffb18` | no |
| `c1f80c002` | main's dDeclaredLoop landing, parents `4e6ac5f7c` and `5125f93ea` | yes |
| `7b42f2c47` | dFairHearing's prepared merge, parents `c0a17df12` and `c09dbfbab` | no |
| `0a760477e` | main's dFairHearing landing, parents `c0a17df12` and `b55a6494a` | yes |

At `--ref 5125f93ea` the derivation as built reads dDeclaredLoop `landed-carrying` with landing
`67f1ffb18` and next state `done`. At `--ref b55a6494a` it reads dFairHearing landed through
`7b42f2c47`.

### The default-branch ref

A new function, `resolve_default_ref(root, default_ref)`, returns `(name, commit)`:

- `default_ref` given: `name` is it as passed.
- `default_ref` is `None`: `resolve_remote(root)` runs from `tools/lib/resolve_remote.py`, loaded by
  path through
  `memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py#load_module`.
  A refusal raises `StateError` carrying the ladder's own text, then `pass --default-ref <rev>`. An
  empty remote or branch raises `StateError` saying the remote ladder names no default branch here,
  then `pass --default-ref <rev>`. Otherwise `name` is `refs/remotes/<remote>/<branch>`, the shape
  `tools/loop/claims.py#derive_card_keys` and `tools/loop/position.py#read_remote_claim` already form.
- A `name` that begins with `-` raises `StateError` `--default-ref takes a revision, not <name>`
  before any git call.
- `commit` is `git rev-parse --verify --quiet <name>^{commit}`. When that call fails, `StateError`
  names the ref, says it resolves to no commit in `root`, and ends `pass --default-ref <rev>`.

Only the 40-hex `commit` reaches a later git call, never `name`.

`derive(ref="HEAD", root=".", claims=True, detail=True, default_ref=None)` calls it once, after the
ref resolves and before `derive_landings`. `main` adds `--default-ref` with no default and passes it
through.

### The landed predicate

`derive_landings(root, commit, default_commit, m, names)` changes in two places:

1. Each build's candidate log runs at `default_commit` instead of `commit`, with the same flags and
   path.
2. One `git rev-list <commit>..<default_commit>` per derivation, through `run_git`, gives the
   default-line commits the derived commit does not contain. A candidate in that set is dropped.

The rest is unchanged: one `tools/memory-tree/tree_lib.py#read_blobs_at` batch reads the kept
merges' `RUN.md` blobs, and a run's `landings` are the kept merges whose `RUN.md` carries its
`base:`. Every default-line commit is reachable from `default_commit`, so a candidate missing from
the `rev-list` set is one the derived commit contains. When the derived commit is the default
commit, the set is empty and the predicate reads exactly what unit 1 built.

The probe applied this predicate with `--default-ref 9e21ac760` (PINNED, 2026-11-19):

| `--ref` | `landed` | the changed build |
|---|---|---|
| `9e21ac760` | the six of unit 1's AC2 | none |
| `5125f93ea` | dTrueNorth, dGroundRules, dSafePassage, dOrderedCharter, dFairHearing | dDeclaredLoop `not-landed`, `startable` |
| `b55a6494a` | dTrueNorth, dGroundRules, dSafePassage | dFairHearing `not-landed`, `startable` |

### Data model

Two fields join the state document after `subject`. `schema` stays `1`, because the change is
additive and no reader branches on the value.

| Field | Value |
|---|---|
| `default_ref` | the default-branch ref as passed, else `refs/remotes/<remote>/<branch>` |
| `default_commit` | the 40-hex commit it resolved to |

### The callers

- The schedule's
  `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py#tree_state`
  keeps calling `derive(ref, claims=False, detail=False)`, so it takes the ladder's default. Its
  signature and tuples stay as
  `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py#derive_sources`
  reads them. The schedule's code does not change.
- The Atlas's
  `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py#derive_actual`
  keeps calling `derive(ref, root=str(REPO), claims=claims, detail=True)`. The Atlas embeds the
  document whole, so both new fields reach the page's data. The Atlas does not change.
- A fixture clone passes its own default by setting its own `refs/remotes/origin/main` and
  `refs/remotes/origin/HEAD`, which is what a push and a fetch leave behind. It can instead pass
  `--default-ref` to the derivation's CLI. It never writes the real repository's refs.

Unit 1's AC4 merged its plant onto the clone's checkout and derived at HEAD. After this unit, that
merge counts only once the clone's default ref holds it, which is this spec's AC2.

### The docstrings

- `memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py`: the usage
  line gains `[--default-ref <rev>]`. THE LANDED PREDICATE says a run's landings are the merges on the
  default branch's first-parent history that the ref contains, whose diff against their first parent
  touches the build's RUN.md, and whose RUN.md carries the run's base. It also says the default branch
  is `--default-ref`, else the remote-tracking ref `refs/remotes/<remote>/<branch>` that
  `tools/lib/resolve_remote.py` names, and that the document records both. WHAT IT DOES NOT CHECK
  gains: that the default-branch ref is current, because a landing the remote took and this
  repository has not fetched reads not-landed.
- The schedule's INPUTS paragraph, at
  `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py@9720474ef1f123c419d6ddcf9ab9e636f2191881:21`:
  `and a first-parent merge of --ref carried it.` becomes
  `and a merge on the default branch's first-parent line, which --ref contains, carried it (the derivation's THE LANDED PREDICATE).`
  The rule is then stated in one place, and the schedule points at it.

### Inventory

| Name | Kind | Cell |
|---|---|---|
| `resolve_default_ref` | function | `py.function`, leading verb `resolve`, checked with `tools/lexicon/lexicon.py --suggest` |
| `default_ref`, `default_commit` | state document fields | none |
| `--default-ref` | CLI option of the derivation | none |

### Files touched (estimate)

`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py`
`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py`
`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-9-ledger.md`

### Alternatives rejected

- **The skeptic's literal wording**: count a merge on the first-parent line of
  `git merge-base <ref> <default-ref>`. This is refuted by measurement. Main's `c1f80c002` took
  `5125f93ea` as its second parent, so the merge base of `5125f93ea` and `9e21ac760` is `5125f93ea`
  itself. Its first-parent line still holds `67f1ffb18`, and dDeclaredLoop still reads landed. The
  same holds at `b55a6494a`.
- **A `--default-ref` option on the schedule and on the Atlas.** No caller needs one now. A fixture
  passes its own through its clone's remote-tracking ref or through the derivation's CLI, and the
  option would be one more value for `TOOL-dTrackedAtlas-11`'s reader to read.
- **A literal `origin/main`.** `tools/lib/resolve_remote.py` exists because probes that read a literal
  `origin` refused on, or graded a stale branch of, a node whose remote has another name.
- **Falling back to the derived ref when no default resolves.** That fallback is the H2 defect
  itself.
- **A `git merge-base --is-ancestor` call per candidate.** The probe used it and it gives the same
  answer. The one `rev-list` answers every candidate in one call and keeps `run_git`'s error path,
  where `--is-ancestor` uses exit 1 for "no" and would need a second exit reader.

## 5. Acceptance criteria

The commands run from the worktree root, with these names set and the ladder's two environment
overrides unset:

```bash
. tools/lib/resolve-python.sh && PY=$(resolve_python)
WT=$(pwd)
STATE=memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py
SCHED=memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py
ATLAS=memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py
FX="$TEMP/ta9fx"
unset GOV_REMOTE GOV_DEFAULT_BRANCH
```

The fixture clone sits at `%TEMP%/ta9fx`. The pass plants it, and removes it after AC6. Its default
branch is its own `refs/remotes/origin/main`, and the real repository's refs are never written. The
plant leaves a run branch whose tip `T` carries on from a prepared merge `P`, which main has not
taken:

```bash
git clone -q --shared "$WT" "$FX" && cd "$FX"
git update-ref refs/remotes/origin/main 9e21ac760
git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main
git checkout -q -B run 9e21ac760
git mv memory/builds/dWitnessedBar/RUN.md memory/builds/dWitnessedBar/RUN.LANDED.00000001.md
printf '# dWitnessedBar run\n\n## Run facts\n\nphase: LANDING\nbase: %s\n' "$(git rev-parse 9e21ac760)" \
  > memory/builds/dWitnessedBar/RUN.md
git add memory/builds/dWitnessedBar && git commit -q -m "records(dWitnessedBar): the build run"
git checkout -q -B prep 9e21ac760
git merge -q --no-ff run -m "merge: dWitnessedBar — land onto origin/main at 9e21ac76"
P=$(git rev-parse HEAD)
git checkout -q -B run "$P" && git commit -q --allow-empty -m "records(dWitnessedBar): after the prepare"
T=$(git rev-parse HEAD)
```

- **AC1** — When `"$PY" "$WT/$STATE" --ref "$T" --claims none` runs in the clone, with its
  `refs/remotes/origin/main` at `9e21ac760` and no `--default-ref`, it exits 0. `landed` names the six
  builds of unit 1's AC2. dWitnessedBar's `build_run.state` is `not-landed`, its `landing` is null, and
  its `RUN.md` record's `landings` is empty. `startable` is dPlacedRequest, dWitnessedBar.
  `default_ref` is `refs/remotes/origin/main` and `default_commit` is `9e21ac760`'s full sha.
  Red when: the derivation as it stood at the unit's start, observed before the change with the same
  `--ref "$T" --claims none`, reads seven `landed` with dWitnessedBar's `landing.sha` the prepared
  merge `$P`.
  figure: PINNED at `9e21ac760`.
  fixture: planted by the pass, as above.
- **AC2** — When the clone's main takes `P` exactly, as the lander pushes it
  (`git update-ref refs/remotes/origin/main "$P"`), `"$PY" "$WT/$STATE" --ref "$P" --claims none`
  names seven `landed` builds, dWitnessedBar's `landing.sha` is `$P`, `startable` is dPlacedRequest
  alone, and `default_commit` is `$P`. The same command at `--ref "$T"` reads dWitnessedBar landed too.
  `"$PY" "$WT/$SCHED" --ref "$P"`, run in the clone with no new option, prints `builds landed 7`.
  Red when: the predicate ignores the moved default ref, which the same derivation pinned with
  `--default-ref 9e21ac760` shows by reading six landed.
  figure: PINNED at `9e21ac760`.
- **AC3** — When main instead takes the run tip through a merge of its own, the `c1f80c002` shape,
  made by `git checkout -q -B main2 9e21ac760`,
  `git merge -q --no-ff run -m "merge: dWitnessedBar — land onto origin/main at 9e21ac76"`,
  `L=$(git rev-parse HEAD)` and `git update-ref refs/remotes/origin/main "$L"`, then
  `"$PY" "$WT/$STATE" --ref "$T" --claims none` reads dWitnessedBar `not-landed`. The same command at
  `--ref "$L"` reads it landed, with `landing.sha` `$L` and its `RUN.md` record's `landings` listing
  `$L` alone, not `$P`.
  Red when: a probe that loads `"$WT/$STATE"` by path and swaps `derive_landings` for the merge-base
  reading, the first-parent line of `git merge-base "$T" "$L"`, which is `$T` itself, reads
  dWitnessedBar landed at `$T` through `$P`.
- **AC4** — When `"$PY" "$STATE" --ref 5125f93ea --default-ref 9e21ac760 --claims none` runs in the
  worktree, `landed` is dTrueNorth, dGroundRules, dSafePassage, dOrderedCharter, dFairHearing.
  dDeclaredLoop reads `not-landed` with `landing` null and `next.state` `startable`. `default_ref`
  is `9e21ac760` and `default_commit` is `9e21ac760dc0a43d6ed007396922722ccee98d57`. At `--ref b55a6494a`
  with the same options, `landed` is dTrueNorth, dGroundRules, dSafePassage, and dFairHearing reads
  `not-landed`.
  Red when: the derivation at the unit's start, `--ref 5125f93ea --claims none`, reads dDeclaredLoop
  `landed-carrying` with landing `67f1ffb18`, and at `b55a6494a` reads dFairHearing landed through
  `7b42f2c47`.
  figure: PINNED at `5125f93ea`, `b55a6494a` and `9e21ac760`, measured on 2026-11-19 by a scratch probe.
- **AC5** — When `"$PY" "$STATE" --ref 9e21ac760 --default-ref 9e21ac760 --claims none` runs in the
  worktree, unit 1's AC2 still holds. `landed` is the six, with `landing.sha` values beginning
  `2511c1181`, `3c0318d95`, `3ada42ab1`, `9760fb746`, `0a760477e` and `9e21ac760`. dDeclaredLoop's
  build-kind run lists `c1f80c002` then `9e21ac760`. `startable` and `ready` are both dPlacedRequest,
  dWitnessedBar.
  Red when: the candidates are read as the derived ref's own line minus the default's
  (`<default>..<ref>`) instead of the default's line that the ref contains, which reads no build
  landed when the two refs are one commit.
  figure: PINNED at `9e21ac760`.
- **AC6** — When `"$PY" "$STATE" --ref 9e21ac760 --default-ref nosuchref --claims none` runs, it exits
  `2`, prints nothing on stdout, and prints one stderr line that begins `build-state:` and names
  `nosuchref`. With
  `--default-ref=-x` it exits 2, and its one `build-state:` line says `--default-ref takes a revision`.
  In the clone, after `git symbolic-ref --delete refs/remotes/origin/HEAD`,
  `"$PY" "$WT/$STATE" --ref "$T" --claims none` exits 2, and its one `build-state:` line names
  `--default-ref`.
  Red when: an unresolvable default falls back to `--ref` itself, which the last command shows by
  exiting 0 and reading dWitnessedBar landed through `$P`.
- **AC7** — When `"$PY" "$ATLAS" --ref 9e21ac760 --claims none --out <scratch>/p9.html` runs in the
  worktree, it exits 0. `grep -o '"default_ref":"[^"]*"'` over the page prints
  `"default_ref":"refs/remotes/origin/main"`, and the page's `default_commit` equals
  `git rev-parse refs/remotes/origin/main`.
  Red when: the Atlas passes its own `--ref` as the default ref, which shows as `"default_ref":"9e21ac760"`.
  figure: DERIVED, the commit is read at observation time.
  cost: one full Atlas render, about as long as unit 2's.
- **AC8** — When `grep -c "first-parent merge of --ref" "$SCHED"` runs, it prints `0`, and
  `grep -c "default branch's first-parent line" "$SCHED"` prints `1`. In the derivation,
  `grep -c -- "--default-ref" "$STATE"` and `grep -c "has not fetched" "$STATE"` each print at least
  `1`, from its module docstring.
  Red when: either docstring still states the ref's own first-parent line, the class
  `amendment-leaves-its-other-half-standing`.

## 6. Gates

The close runs the plain bar once. The schedule's docstring edit moves its blob again, so
`chain-packet self-test` keeps the CP3, CP4 and CP5 reds that ask `TOOL-dTrackedAtlas-6` already
owes under `GATE_SELFTESTS=1`. The owner's re-pin clears them for this blob as well. This unit adds
no arm. Its regression is observed by AC1 and AC3, red before the change and green after.

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `chain-packet self-test` · `policy fixtures`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-19 · initial draft, from the closing review's H2
  (2026-11-19-review-TOOL-dTrackedAtlas-1-2-3-4-diff-review-round1) and the brief
  2026-11-19-prompt-TOOL-dTrackedAtlas-8-spec-brief.

## 9. Reuse audit

The seam extended is
`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py#derive_landings`,
changed in place. The default branch comes from `tools/lib/resolve_remote.py#resolve_remote`, which is
the repository's one answer to which remote and default branch "landed" is measured on
(TOOL-dLadderedRemote-1). It is loaded by path, so no inline copy joins the population that
`tools/lib/resolve-python.test.sh`'s parity table grades.
`python tools/codebase-map/reuse_lookup.py "which remote and default branch a landing is measured on"`
ranked `resolve_remote` second, a SEAM. It also ranked `tools/unattended/lib-unattended.sh#read_landing_commit`,
which reads a landing from the working copy rather than at a ref, as unit 1's audit found. Seams read
and not taken: `tools/loop/claims.py#derive_card_keys` and `tools/loop/position.py#read_remote_claim`,
which form the same `refs/remotes/<remote>/<branch>` name for a card and a claim and carry the ladder
inline. The recall probe returned the H2 finding itself, TOOL-dUnstalledConvoy-38, where the lander
pushes the prepared merge and the run's HEAD is its second parent, and the dPlacedRequest records on
the prepared merge's shape, whose first parent is the advertised tip. That shape is the one the
predicate above relies on.

Recall terms used: `python tools/memory-recall/query.py "how is a landing told apart from a run branch's prepared merge that main never took" --terms "landed default-branch first-parent remote-tracking resolve_remote ladder prepared-merge lander push-main origin/main run-branch"`
