# TOOL-dQuietDisk-2 — the pass-order leg grades only units whose key moved since its last graded tip

**Status:** SPECCED · rev-3 · 2026-11-22 · node d · Tier-2 · base 609cd40b · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md) | research | TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/unattended/check-pass-order.sh` regrades every CLOSED unit of every build on every bar, with
one or more git processes per question. The analysis counts about 11.5k git processes and 1,054 s [PINNED]
for one run (`memory/builds/dQuietDisk/build/2026-11-20-build-TOOL-dQuietDisk-19-analysis.md`, row
G3). This unit grades a unit only when its stored verdict is absent or its key moved, through the
history verdict store TOOL-dQuietDisk-1 builds, so a warm run with no new unit costs a bounded,
stated number of git processes. Every rc, summary line and violation line stays byte-identical.

## 2. Scope (IN)

- **S1** — Before the per-build loop, the leg reads its last graded tip from the store and derives
  the NEW set: the commits of `rev-list <last>..HEAD`, read once. When no tip is stored, the stored
  tip is not an ancestor of HEAD, the store is unreadable, or the policy key `tests.history-verdicts`
  reads `regraded`, the NEW set is "everything" and every unit is graded as today. The tip is read
  with `read_hs_tip` after one `init_hs`. Observed by AC1 and AC3.
- **S2** — Each graded unit's outcome is one store item, keyed by the unit's inputs that section 4
  lists. The item holds the build commit, the pre-anchor commit, the spec path found and its
  `plan_state` answer, never a printed line. Observed by AC1 and AC2.
- **S3** — A unit is regraded, exactly as the code at the base grades it, when its item is absent,
  unreadable, of a foreign version, or keyed differently. It is also regraded when a commit of the
  NEW set carries its id among its `_SUBJ` tokens. For a build graded with no run-state file, every
  unit is regraded when a commit of the NEW set touches the build folder. Every other unit takes
  its stored outcome. Observed by AC2 and AC4.
- **S4** — The report lines, the waiver bookkeeping, the stale-waiver rule, the `--preview` output and
  the two summary lines are derived from the outcomes in the same order and with the same counters
  as today. A short sha is computed at report time, never stored. Observed by AC1.
- **S5** — The per-build reads at HEAD go through `init_bh` and `read_bh_blob`, the store's one
  `cat-file --batch` coprocess: the README's `opened:` and its CLOSED rows, and the run-state file's
  `base:`. They are no longer one `git show` each. Every item is read by one `read_hs_items` call.
  Observed by AC3.
- **S6** — After a run that exits 0 or 1 with no refusal, the leg writes every regraded item and its
  new tip with one `write_hs_items` call, which writes each tmp-then-rename. A run that exits 2, or a `--preview` run, writes nothing. Observed
  by AC5.
- **S7** — The file header's "WHAT THIS DOES NOT CHECK" list gains one bullet naming the store, what
  a stored outcome skips, and the switch that turns it off. Observed by AC6.

## 3. Non-goals (OUT)

- No change to `tools/unattended/lib-unattended.sh`. `build_commit`, `read_history_range` and
  `read_attribution_tokens` are called as they are; this unit avoids calling `build_commit` for a
  unit whose outcome stands. TOOL-dQuietDisk-3 reads the same library, so neither unit writes it and
  the two stay parallel at order 2.
- No change to the reuse cache's `head $RG_HEAD` key for history legs
  (`tools/run-gates/run-gates.sh@609cd40b1:3507`). The leg still runs on every bar; it does less.
- No change to what the leg grades, its exit codes, its waiver registry or its cutoff.
- No speedup of a cold run beyond the batched HEAD reads. A cold run's per-unit spawns stay as today.
- No store of its own, and no edit of the store's block in `lib-unattended.sh`. The store, its
  reader, its pruning and `tests.history-verdicts` are TOOL-dQuietDisk-1's.
- The unattended kit's suites are never run by this unit (owner rule, 2026-08-23).

### Edges

- **consumes-from** `TOOL-dQuietDisk-1` — the history verdict store's bash face in the unattended
  kit's library, its `cat-file --batch` coprocess and its policy key. Without them nothing is
  stored, and the leg grades every unit as today.
- **hands-off** `TOOL-dQuietDisk-19` — the warm-run bound this spec promises, which that unit's
  after-reading of the pass-order leg is held to
- **consumes-from** external — dWitnessedBar's landed tip, which this unit is built on, because that
  branch changes `tools/unattended/check-pass-order.sh`.

## 4. Design

### The leg today

All citations are read at `609cd40b1`, dWitnessedBar's tip, which this unit is built on.

The leg builds the `_SUBJ` subject cache from one `read_attribution_tokens HEAD` call and checks
its size against `rev-list --count HEAD` (`tools/unattended/check-pass-order.sh@609cd40b1:452`). It
reads the history range once (`tools/unattended/check-pass-order.sh@609cd40b1:481`). Then it walks
every build README at HEAD (`tools/unattended/check-pass-order.sh@609cd40b1:496`). Per build it runs
`git show` for `opened:`, again for the run-state file, a `cat-file -e` for the base, and for a build
with no run-state file a whole-history `rev-list --reverse HEAD -- <folder>`. Per CLOSED unit it calls
`build_commit` (`tools/unattended/lib-unattended.sh#build_commit`). That walks the range and runs one
`git show --name-only` per candidate commit whose subject carries the id
(`tools/unattended/lib-unattended.sh@609cd40b1:1367`). It then runs a `rev-parse`, a `git grep`, an
`ls-tree` and a `git show` of the spec at the first parent, and a `rev-parse --short` per report line
(`tools/unattended/check-pass-order.sh@609cd40b1:648`).

### What a unit's outcome reads

The outcome of one CLOSED unit is a pure function of the inputs below. Each is in its item key, so a
change to any of them moves the key.

| Input | Why it is in the key |
|---|---|
| the unit id and its build folder | the item's identity |
| the range base, from the run-state file or the folder anchor | `build_commit`'s range starts there |
| `HR_MODE` and `HR_TIP` | RANGE mode excludes the advertised tip's history |
| `check-pass-order.sh`, `lib-unattended.sh`, the driver `unattended.sh` and `commit_trailers.py`, passed to `init_hs` as its code paths | the grading code: `plan_state` is sliced from the driver, and attribution is the trailer reader's |
| `FORK_CUTOFF`, `GENERATED_INDEXES`, `SHARED_RECORDS` and `PREANCHOR_CAP` | the classifier's cutoff and the build-commit exclusion set |

The store's key rule, a digest of the working bytes of every code path the caller names, is
TOOL-dQuietDisk-1's. This table names the code paths and the id fields this leg passes it.

### Why a stored outcome stays true

`build_commit` returns the EARLIEST qualifying commit of `base..HEAD`. When the stored tip `L` is an
ancestor of HEAD, `base..HEAD` is `base..L` plus the NEW set. A commit outside the NEW set was already
in the range when the outcome was stored. So the earliest qualifying commit can change only when a
NEW commit qualifies, and a commit qualifies only when its subject tokens carry the id. Those units
are regraded by S3, a merged side branch's older commits included, since `rev-list <last>..HEAD`
lists them. The first parent's tree is immutable once the build commit is fixed, so the spec found
and its state cannot move. The folder anchor of a build with no run-state file can move only when a
NEW commit touches the folder, which S3 also regrades.

The CLOSED population, the waiver registry and `opened:` are read at HEAD on every run and never
stored. A unit that becomes CLOSED has no item, so it is graded.

### The warm-run bound

A warm run with an empty NEW set makes these git calls: the toplevel and HEAD reads, the waiver
`cat-file -e` and its record read, the history range read, the `rev-list --count`, the one
`read_attribution_tokens` log, the one `ls-tree` of the builds, the one `rev-list <last>..HEAD`, and
the one `init_bh` coprocess. `read_hs_items` and `write_hs_items` are python processes and start no git. The bound this unit promises is **at most 30 git processes**
for such a run, PINNED as a promise and observed by AC3. The cold count is DERIVED at observation.

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| the leg's item key fields | store item fields | none; the store's schema owns them | the store's reader |
| `PO_NEW` | shell associative array, the NEW set | none, a local | nothing |

No verb, flag, conf key, policy key or refusal number is minted.

### Files touched (estimate)

`tools/unattended/check-pass-order.sh` · `tools/unattended/check-pass-order.test.sh`

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| Drop `head $RG_HEAD` from the reuse key | The leg reads history, so a reuse across commits would carry a verdict over commits it never graded. |
| Change `build_commit` to batch its `show --name-only` | It is shared with `check-brief-recorded.sh` and the driver, so the change would collide with TOOL-dQuietDisk-3 at order 2, and a warm run never calls it. |
| Store printed violation lines | A short sha's length grows with the object count, so a stored line could differ from the old leg's at the same HEAD. |

## 5. Production-readiness checklist

- security: N/A — the store lives under the git common dir and is never pushed or rendered; its
  write path is TOOL-dQuietDisk-1's.
- perf / scale: a warm run is bounded at 30 git processes (AC3); a cold run costs today's plus one
  store read.
- error / empty / loading states: a missing, unreadable, partial or foreign-version item regrades
  that unit; an unreadable store regrades all of them (S1, S3).
- observability: the summary lines are unchanged; the store's own reader reports its hits.
- risks: a key that misses an input carries a stale outcome. The key table in section 4 is the
  defence, and AC4's planted spec edit is its witness.
- testing: the equivalence corpus (AC1), the planted change (AC2, AC4), the process count (AC3).
- migration: none; a first run is a cold run.
- user docs: the leg's file header (S7); `help/` holds no page for this leg.

## 6. Acceptance criteria

The pass's probes run over a hermetic fixture repository the probe builds under
`%TEMP%/<short-name>`, in the shape `tools/unattended/check-pass-order.test.sh#mkfixture` builds
one, read and never run: the leg, the libraries it sources and its conf copied in, two build
folders, one with a run-state `base:` and one without, five CLOSED units with their specs, and
commits whose subjects name them. "Old" is the leg's copy at `609cd40b1` and "new" the unit's, each
run there by path. Running either over the fixture is a probe of this unit's code. A reading over
the real tree is the gate's own population, which a role agent may not run (scratch-guard row G1),
so each such reading below is owed to the main loop at the close.

- **AC1** — When the old leg and the new leg each run over the fixture, first with the store cold and
  then warm, all three outputs and exit codes are byte-identical. When the main loop runs the same
  comparison, `bash tools/unattended/check-pass-order.sh` at `609cd40b1` against the new leg, over
  one scratch `git clone --shared` of the real tree at the build's base, cold then warm, all three
  are byte-identical there too.
  Red when: a stored outcome is reported differently, or a counter on the summary line moves.
  cost: about 18 minutes per cold run over the real tree, measured 1,054 s [PINNED] by the analysis.
  permission: the real-tree corpus is owed to the main loop; the pass makes the fixture comparison.
  fixture: the real-tree clone under `%TEMP%` with its own `TEMP`, and the old leg run from a
  worktree at `609cd40b1`.
- **AC2** — When the fixture gains, on a throwaway branch past the stored tip, one build folder whose
  README carries one CLOSED unit and one `git commit` that names that id and touches a product path
  with no spec at its first parent, both legs exit 1 with the same violation line for that unit.
  The new leg's store shows that one item written and every other item read, not regraded.
  Red when: the new leg stays green while the old leg reds, or it regrades units it held.
- **AC3** — When the new leg runs warm over the fixture with an empty NEW set under
  `GIT_TRACE2_EVENT=<dir>`, the directory holds at most 30 files [PINNED], and the cold run's file count is
  printed beside it. The main loop takes the same count over the real tree at the close, as subject
  M2 of TOOL-dQuietDisk-19's record.
  Red when: a per-unit or per-build git call survives on the warm path.
  figure: 30 is PINNED as the promise, and a warm run's count does not grow with the unit count, so
  the fixture reads the bound; the cold counts are DERIVED at observation.
  permission: the real-tree count is owed to the main loop.
- **AC4** — When a `git commit` naming one CLOSED unit's id in its subject and touching a path
  outside the record surface is added to the fixture past the stored tip, the new leg regrades that
  unit and no other, and its output equals the old leg's. When a commit edits one build's run-state
  `base:`, the new leg regrades that build's units and no other build's.
  Red when: a NEW commit carrying the id, or a moved base, does not regrade its units.
- **AC5** — When the new leg exits 2 over the fixture on a planted unreadable `PASS_ORDER_CUTOFF`, or
  runs under `--preview`, the store's tip and items are unchanged, read before and after through the
  store's reader.
  Red when: a refused or preview run writes an item.
- **AC6** — When `grep -c 'history verdict store' tools/unattended/check-pass-order.sh` runs, it
  prints 1 or more.
  Red when: the header does not name what a stored outcome skips.

## 7. Gates

`unattended kit gate` · `line length` · `testsuite counts (every bar self-test prints one)` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/check-pass-order.test.sh · covers AC2 AC4 · a fixture build whose stored item is planted with a moved key or a NEW commit naming its id; its failing case is staged by skipping the regrade and reading the stored outcome · none

The arm is observed by the main loop, never by a unit pass. The real-tree halves of AC1 and AC3
are the main loop's one-time observations at the close; no standing arm compares against a literal
sha, which is `memory/gotchas/test-oracle-read-from-a-historical-sha.md`'s class.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft.
- rev-2 · 2026-11-22 · under `2026-11-22-prompt-TOOL-dQuietDisk-1-divergence-task`. The store's bash
  face is spelled as TOOL-dQuietDisk-1 rev-3 renames it: `init_hs`, `read_hs_tip`, `read_hs_items`,
  `write_hs_items`, `init_bh` and `read_bh_blob`. Section 6 no longer has the pass run the leg over
  the real tree: AC1 to AC5 run old and new over a hermetic fixture, and the real-tree corpus of
  AC1 and the real-tree count of AC3 are owed to the main loop at the close. This spec mints no
  function, so no name of its own needed a rename.
- rev-3 · 2026-11-22 · wording only, under `2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task`. In section
  1 and section 6 the analysis's wall-time figure is marked PINNED, as read from a record, and AC3's
  warm bound PINNED as the promise its `figure:` line already makes. Design, scope and acceptance
  unchanged.

## 10. Reuse audit

The seam extended is the leg's own per-unit loop and its walk memo `_BC_MEMO`
(`tools/unattended/check-pass-order.sh@609cd40b1:466`), which already answers repeated ranges inside
one run. This unit persists that answer across runs through TOOL-dQuietDisk-1's store rather than a
second store. The chain build owning the area is dWitnessedBar (Test: gate health), whose branch
changes this file, and dScopedBuild (Build: the history-derived exit base). TOOL-dUnstuckLanding-17's
RANGE mode is kept as it is and becomes a key input.

`python tools/codebase-map/reuse_lookup.py "grade only units new since the last graded tip of a history leg"`
returned name-token neighbours only (`legs`, `leg`, `units`, `parse_unit_rows`). No existing seam
fits beyond the leg's own loop and the store this build adds. Recall returned TOOL-dBriefedPass-3,
the leg's origin, TOOL-dUnstuckLanding-17 and -7 for RANGE mode, and this build's brief. The source
agreed with each hit.

Recall terms used: check-pass-order build_commit history leg RANGE WHOLE subject cache _SUBJ plan_state incremental last graded tip
