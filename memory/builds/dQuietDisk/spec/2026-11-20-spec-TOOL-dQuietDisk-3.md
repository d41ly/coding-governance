# TOOL-dQuietDisk-3 — the brief-recorded leg grades only units whose key moved since its last graded tip

**Status:** SPECCED · rev-1 · 2026-11-20 · node d · Tier-2 · base 609cd40b · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/unattended/check-brief-recorded.sh` regrades every CLOSED unit built during a run on every
bar. The analysis counts about 6k to 8k git processes and 404 s per run
(`memory/builds/dQuietDisk/build/2026-11-20-build-TOOL-dQuietDisk-19-analysis.md`, row G3). Its
`_SUBJ` subject cache already removed the per-commit subject reads inside one run. This unit
persists each unit's outcome through TOOL-dQuietDisk-1's history verdict store, so a warm run with no
new unit costs a bounded, stated number of git processes. Every rc and printed line stays
byte-identical.

## 2. Scope (IN)

- **S1** — Before the per-build loop, the leg reads its last graded tip from the store and derives
  the NEW set, the commits of `rev-list <last>..HEAD`, read once. No tip, a tip that is not an
  ancestor of HEAD, an unreadable store, or `tests.history-verdicts` at `regraded` makes the NEW set
  "everything", and every unit is graded as today. The tip is read with `hs_tip_read` after one
  `hs_open`. Observed by AC1 and AC3.
- **S2** — Each graded unit's outcome is one store item, keyed by the inputs section 4 lists. The
  item holds the outcome class and the commits and paths its lines name, never a printed line.
  Observed by AC1 and AC2.
- **S3** — A unit is regraded, exactly as the code at the base grades it, when its item is absent,
  unreadable, of a foreign version or keyed differently, or when a commit of the NEW set carries its
  id among its `_SUBJ` tokens. Every other unit takes its stored outcome. Observed by AC2 and AC4.
- **S4** — The violation lines, the `announced` lines, the waiver bookkeeping, the stale rule and the
  three summary lines are derived from the outcomes in today's order and with today's counters. A
  short sha is computed at report time. Observed by AC1.
- **S5** — The per-build reads at HEAD go through `bh_open` and `bh_read`, the store's one
  `cat-file --batch` coprocess: the README's `opened:` and CLOSED rows, and the run-state file's
  `base:` and claim. Every item is read by one `hs_lookup` call. Observed by AC3.
- **S6** — A run that exits 0 or 1 writes every regraded item and its new tip with one `hs_store`
  call, each tmp-then-rename.
  A run that exits 2 writes nothing. Observed by AC5.
- **S7** — The header's account of what the leg does not check gains one sentence naming the store,
  what a stored outcome skips, and the switch that turns it off. Observed by AC6.

## 3. Non-goals (OUT)

- No change to `tools/unattended/lib-unattended.sh`, the store's block in it included, which is
  TOOL-dQuietDisk-1's. TOOL-dQuietDisk-2 reads the same library, so neither unit writes it and both
  stay at order 2.
- No second store. The `_SUBJ` cache stays an in-run map; what persists is each unit's outcome, in
  TOOL-dQuietDisk-1's store, as the brief for this unit requires.
- No change to the predicate, the waiver registry, the cutoff, the exit codes, or the reuse cache's
  `head $RG_HEAD` key (`tools/run-gates/run-gates.sh@609cd40b1:3507`).
- The unattended kit's suites are never run by this unit (owner rule, 2026-08-23).

### Edges

- **consumes-from** `TOOL-dQuietDisk-1` — the history verdict store's bash face in the unattended
  kit's library, its `cat-file --batch` coprocess and its policy key. Without them every unit is
  graded as today.
- **consumes-from** external — dWitnessedBar's landed tip, which this unit is built on, because that
  branch changes `tools/unattended/check-brief-recorded.sh`.

## 4. Design

### The leg today

All citations are read at `609cd40b1`.

The leg builds `_SUBJ` once (`tools/unattended/check-brief-recorded.sh@609cd40b1:477`) and reads the
history range once (`tools/unattended/check-brief-recorded.sh@609cd40b1:503`). It walks every build
README at HEAD (`tools/unattended/check-brief-recorded.sh@609cd40b1:538`), with two `git show` reads
and a `cat-file -e` per build. Per CLOSED unit it calls `build_commit`
(`tools/unattended/lib-unattended.sh#build_commit`), reads the run-state file at the build commit,
and, when that phase is terminal, walks `rev-list --reverse <build>..HEAD` for a later commit made
during a live run (`tools/unattended/check-brief-recorded.sh@609cd40b1:607`). Then it reads the
brief row, the `ls-tree` blob it joins to, and a `rev-parse --short` per printed line.

### What a unit's outcome reads

| Input | Why it is in the key |
|---|---|
| the unit id and its build folder | the item's identity |
| the run-state `base:` at HEAD | `build_commit`'s range starts there |
| `HR_MODE` and `HR_TIP` | RANGE mode excludes the advertised tip's history |
| the claim the run-state file makes at HEAD, and the blob ids of the folder's retired `RUN.*.md` files at HEAD | the finished-run branch compares the build commit's claim with what HEAD still bears out (`tools/unattended/check-brief-recorded.sh@609cd40b1:630`) |
| `check-brief-recorded.sh`, `lib-unattended.sh`, the driver `unattended.sh` and `commit_trailers.py`, passed to `hs_open` as its code paths | the grading code: the terminal phase set is read from the driver |
| `GENERATED_INDEXES`, `SHARED_RECORDS` and `PREANCHOR_CAP` | the build-commit exclusion set and the pre-run probe's cap |

An active build's run-state file changes at every phase, so its units are regraded on every run
while it is live. That cost is bounded to the live builds.

### Why a stored outcome stays true

`build_commit` returns the earliest qualifying commit of `base..HEAD`. With the stored tip an
ancestor of HEAD, only a NEW commit carrying the id can change that answer. The later-live-commit
walk of `<build>..HEAD` likewise can change only through a NEW commit carrying the id, which S3
regrades. The brief row and its blob are read at the build commit, which is immutable. The pre-run
probe reads the ancestors of `base`, which the key pins.

### The warm-run bound

A warm run with an empty NEW set and no live build makes the toplevel and HEAD reads, the waiver
`cat-file -e` and record read, the history range read, the `rev-list --count`, the one
`read_attribution_tokens` log, the one `ls-tree`, the one `rev-list <last>..HEAD` and the one
`bh_open` coprocess. `hs_lookup` and `hs_store` are python processes and start no git. The bound promised is **at most 30 git processes**, PINNED as a promise and observed
by AC3. A live build adds its own units' regrades, which AC3 counts apart.

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| the leg's item key fields | store item fields | none; the store's schema owns them | the store's reader |
| `BR_NEW` | shell associative array, the NEW set | none, a local | nothing |

No verb, flag, conf key, policy key or refusal number is minted.

### Files touched (estimate)

`tools/unattended/check-brief-recorded.sh` · `tools/unattended/check-brief-recorded.test.sh`

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| Persist `_SUBJ` alone | It removes one log pass per run and leaves every per-unit spawn, which is where the 404 s goes. |
| Key the item on HEAD | That is the reuse cache's key today, and it is why nothing is reused across commits. |
| Store the printed lines | A short sha's length can grow between runs, so a stored line could differ from the old leg's. |

## 5. Production-readiness checklist

- security: N/A — the store is under the git common dir, never pushed; its write path is
  TOOL-dQuietDisk-1's.
- perf / scale: a warm run is bounded at 30 git processes with no live build (AC3).
- error / empty / loading states: a missing, partial or foreign-version item regrades its unit; an
  unreadable store regrades all of them.
- observability: the leg's lines are unchanged; the store's reader reports hits.
- risks: a key missing an input carries a stale outcome; the key table is the defence, AC2 and AC4
  its witnesses.
- testing: the equivalence corpus (AC1), the planted cases (AC2, AC4), the count (AC3).
- migration: none; a first run is a cold run.
- user docs: the leg's file header (S7); `help/` holds no page for this leg.

## 6. Acceptance criteria

- **AC1** — When the old leg, `bash tools/unattended/check-brief-recorded.sh` at `609cd40b1`, and the
  new leg each run over one scratch `git clone --shared` of the real tree at the build's base, with
  the store cold and then warm, the three outputs and exit codes are byte-identical.
  Red when: a stored outcome prints differently or a counter moves.
  cost: about 7 minutes per cold run, measured 404 s by the analysis.
  fixture: a clone under `%TEMP%` with its own `TEMP`; the old leg runs from a worktree at `609cd40b1`.
- **AC2** — When the AC1 clone gains, on a throwaway branch past the stored tip, one build with a
  pinned `base:`, one CLOSED unit and one `git commit` naming it with no brief row in its run-state
  file, both legs exit 1 with the same violation line, and the store shows only that unit written.
  Red when: the new leg stays green while the old leg reds, or it regrades units it held.
- **AC3** — When the new leg runs warm with an empty NEW set under `GIT_TRACE2_EVENT=<dir>`, the
  directory holds at most 30 files plus the live builds' regrades, which the run counts apart.
  Red when: a per-unit git call survives for a unit of a finished build.
  figure: 30 is PINNED as the promise; the cold count is DERIVED at observation.
- **AC4** — When a `git commit` naming one CLOSED unit's id and touching a path outside the record
  surface is added past the stored tip, the new leg regrades that unit only, and its output equals
  the old leg's. When a commit renames one build's `RUN.md` to a retired `RUN.<PHASE>.<sha8>.md`, the
  new leg regrades that build's units only.
  Red when: either change leaves the stored outcome standing.
- **AC5** — When the new leg exits 2 on a planted unreadable `BRIEF_RECORDED_CUTOFF`, the store's tip
  and items read the same before and after through the store's reader.
  Red when: a refused run writes an item.
- **AC6** — When `grep -c 'history verdict store' tools/unattended/check-brief-recorded.sh` runs, it
  prints 1 or more.
  Red when: the header does not name what a stored outcome skips.

## 7. Gates

`unattended kit gate` · `line length` · `testsuite counts (every bar self-test prints one)` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/check-brief-recorded.test.sh · covers AC2 AC4 · a fixture build whose stored item is planted with a moved key or a NEW commit naming its id; its failing case is staged by reading the stored outcome without the regrade · none

The arm is the main loop's to observe. AC1 and AC3 are one-time observations at the close, and no
standing arm compares against a literal sha.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft.

## 10. Reuse audit

The seam extended is the leg's `_SUBJ` cache and walk memo
(`tools/unattended/check-brief-recorded.sh@609cd40b1:491`), the in-run half the brief names, made
durable through TOOL-dQuietDisk-1's store and no second store. The chain build owning the area is
dWitnessedBar (Test: gate health), whose branch changes this file, and dScopedBuild (Build: the
history-derived exit base). The owner ruling of 2026-09-13 in dPolishedVitrine, that a unit built
after its run finished is not graded, becomes a key input through the claim at HEAD.

`python tools/codebase-map/reuse_lookup.py "grade only units new since the last graded tip of a history leg"`
returned name-token neighbours only. No existing seam fits beyond the leg's own caches and the
store this build adds. Recall returned TOOL-dPolishedVitrine-14 and -15, the post-run ruling, this
build's spec brief, and TOOL-aPiecewiseGrade-2, the incremental-cache prior art unit 1 extends. The
source agreed with each hit.

Recall terms used: check-brief-recorded brief row build commit run-state phase terminal subject cache incremental store waiver
