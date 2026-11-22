# TOOL-dQuietDisk-2 — the pass-order leg grades only units whose key moved since its last graded tip

**Status:** CLOSED · rev-6 · 2026-11-22 · node d · Tier-2 · base 40def53f · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 |
| [2026-11-22-build-TOOL-dQuietDisk-2-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dQuietDisk-2-1-acceptance-ledger.md) | journal | — |
| [2026-11-22-build-TOOL-dQuietDisk-2-deviation-1.md](../build/2026-11-22-build-TOOL-dQuietDisk-2-deviation-1.md) | deviation | — |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-2-1-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-2-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-2-2-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-2-2-spec-writer.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-2-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-2-build-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-2-divergence-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-2-divergence-task.md) | research | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-2-reground-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-2-reground-task.md) | research | TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/unattended/check-pass-order.sh` regrades every CLOSED unit of every build on every bar, with
one or more git processes per question. TOOL-dQuietDisk-19's before-reading of the leg counts
9,319 git processes and 1,058 s for one run at `b3f5a2bc3` [PINNED, that record's M2 row,
2026-11-21]. This unit grades a unit only when its stored verdict is absent or its key moved,
through the history verdict store TOOL-dQuietDisk-1 built. A warm run then costs a bounded, stated
number of git processes that does not grow with the unit count. Every rc, summary line and
violation line stays byte-identical.

## 2. Scope (IN)

- **S1** — The leg opens the store once per run, after the per-run reads that precede the build
  walk. It calls `init_hs pass-order` with its four code paths and starts the coprocess with
  `GIT_NO_REPLACE_OBJECTS=1 init_bh`. It resolves HEAD once, to the full sha G, through
  `read_bh_info HEAD`. Where `init_hs` or `init_bh` fails, or a store verb exits non-zero, every
  read misses and the leg grades as today. Observed by AC1, AC7, AC8, AC9 and AC10.
- **S2** — Each build's reads at HEAD go through the coprocess with `read_bh_blob`: the README once,
  for both `opened:` and the CLOSED ids, and the run-state file. The base check becomes one
  `read_bh_info "<base>^{commit}"`. Where a read returns 2 or 3, that one read falls back to
  today's `GIT show` or `GIT cat-file -e`. Observed by AC1, AC4 and AC9.
- **S3** — The folder anchor of each build with no run-state file comes from one `anchors` item
  keyed by the graded commit. The leg reads its last graded tip L with `read_hs_tip`. It carries
  L's anchors to G when L is G, or when every commit of `L..G` has one parent and the chain ends
  at L. An anchor missing from the item, an empty one, or any other shape of `L..G` is computed as
  today. Observed by AC1 and AC4.
- **S4** — Each CLOSED unit's outcome is one `unit` item under the key section 4 lists, which
  includes the unit's candidate commits read from `_SUBJ`. A hit is used as the outcome. A miss
  runs today's grading of that unit. The store never holds two cases, and each is graded afresh on
  every run as today. One is a built outcome whose in-range candidates share a committer second.
  The other is a unit whose candidate is a root commit. Observed by AC1, AC2, AC3, AC5 and AC7.
- **S5** — The unwitnessed-pass arm stores its two per-build answers. The `merge-base
  --is-ancestor` answer goes in a `bypass-range` item, and the `unchecked` verb's lines go in an
  `unchecked` item keyed by the base and G. Observed by AC1 and AC4.
- **S6** — The report lines, the waiver bookkeeping, the stale-waiver rule, the `--preview` output
  and the summary lines come from the outcomes in loop order, with today's counters. Every short
  sha a report line names is computed after the loop by one
  `GIT log --no-walk=unsorted --format=%h <sha>... --` over all of them, and is never stored. The leg prints no line of its own about the store, and it discards
  the store's stderr. Observed by AC1.
- **S7** — The leg writes with one `write_hs_items <file> G` call, after a run that exits 0 or 1 and
  is not `--preview`, and only when HEAD still reads G. The file holds every item this run
  computed that was not a hit. The call is skipped when there is nothing to write and L is G.
  Observed by AC4 and AC6.
- **S8** — The file header's "WHAT THIS DOES NOT CHECK" list gains one bullet. It names the store,
  what a stored outcome skips, the switch `tests.history-verdicts` that turns it off, and the
  date-order residual section 4 states. Observed by AC11.

## 3. Non-goals (OUT)

- No change to `tools/unattended/lib-unattended.sh`, the store's block in it included.
  `build_commit`, `read_history_range` and `read_attribution_tokens` are called as they are. The
  leg only avoids calling `build_commit` for a unit whose outcome is a hit. TOOL-dQuietDisk-3 reads
  the same library, and neither unit writes it.
- No change to `tools/unattended/commit_trailers.py` or to TOOL-dQuietDisk-1's store. A gap in the
  store is that unit's deviation, named in section 8.
- No change to the reuse cache's `head $RG_HEAD` key for history legs
  (`tools/run-gates/run-gates.sh@2e851a92d9ce:3553`). The leg still runs on every bar; it does less.
- No change to what the leg grades, its exit codes, its waiver registry, its cutoff or its summary
  fields.
- A cold run's per-unit spawns stay as today. The only cold saving is the coprocess's per-build
  reads and the batched short shas.
- No column-0 function in either file, so the codebase map's symbol index does not move.
- The unattended kit's suites are never run by this unit (owner rule, 2026-08-23).

### Edges

- **consumes-from** `TOOL-dQuietDisk-1` — the store's bash face in the unattended kit's library,
  its `cat-file --batch` coprocess and its policy key `tests.history-verdicts`. Without them every
  read misses, and the leg grades every unit as today.
- **hands-off** `TOOL-dQuietDisk-19` — the warm-run bound this spec promises, which that unit's M2
  after-reading of the pass-order leg is held to
- **consumes-from** external — dWitnessedBar's land tip `fb6f1a74c`, merged into this run at
  `b3f5a2bc3`, and its landing on main at `8b8b1374c`, merged at `40def53f7`. The land tip carries
  TOOL-dWitnessedBar-2's unwitnessed-pass arm, whose two per-build reads S5 stores.

## 4. Design

### The leg at the base

All citations are read at `40def53f7`, where the leg's blob is `638bb1d0c2a6` and the library's is
`7592fd768bc2`. The four inputs below had already landed when this re-ground was taken.

The leg builds the `_SUBJ` subject cache from one `read_attribution_tokens HEAD` call and checks
its size against `rev-list --count HEAD` (`tools/unattended/check-pass-order.sh@638bb1d0c2a6:452`).
It reads the history range once (`tools/unattended/check-pass-order.sh@638bb1d0c2a6:481`). The
unwitnessed-pass block finds its anchor with one `git log -S Commit-Checked` and reads
`hooks.bypass` at HEAD (`tools/unattended/check-pass-order.sh@638bb1d0c2a6:502`). The build walk then
runs once per build README at HEAD (`tools/unattended/check-pass-order.sh@638bb1d0c2a6:527`). Per
build it runs these:

- `git show` of the README for `opened:` (`:534`), and again for the CLOSED ids (`:600`);
- `git show` of the run-state file (`:562`), and `cat-file -e` of its base (`:566`);
- for a build with no run-state file, a whole-history `rev-list --reverse HEAD -- <folder>` (`:572`)
  and a `rev-parse` of its parent (`:574`);
- `merge-base --is-ancestor` of the bypass anchor and the base (`:579`);
- where that holds, one `commit_trailers.py unchecked <base>..HEAD` (`:581`).

Per CLOSED unit it calls `tools/unattended/lib-unattended.sh#build_commit`, which runs one
`rev-list` per range, memoised in `_BC_MEMO` (`:466`). It also runs one `git show --name-only` per
candidate commit whose tokens carry the id (`tools/unattended/lib-unattended.sh@7592fd768bc2:1410`).
A unit with a build commit then costs a `rev-parse` of the parent, a `git grep`, an `ls-tree` and a
`git show` of the spec (`:668`, `:696`, `:697`, `:699`). Each report line adds one
`rev-parse --short` per sha it names (`:656`, `:712`, `:717`).

At the real tree the walk reaches 140 builds past the cutoff: 90 with a run-state file and 50
without. They hold 1,711 CLOSED rows [PINNED, counted at `fa1295ff4` on 2026-11-22].

### The store as built

The leg consumes the store's bash face as `tools/lib/history-store.sh` spells it, in the copy
inlined in `tools/unattended/lib-unattended.sh#init_hs`:

| Call | What it does here |
|---|---|
| `init_hs pass-order <code path>...` | sets `HS_PY`, `HS_MODULE` and `HS_ARGS`, the module found beside the library |
| `read_hs_tip` | prints this worktree's last graded tip L, or nothing |
| `read_hs_items <file>` | reads `<item id>TAB<field>...` lines and prints `<item id>TAB<hit or miss>TAB<body>` lines |
| `write_hs_items <file> <sha>` | stores each `<item id>TAB<field>...TAB<body>` line, then the tip, then the daily prune |
| `init_bh`, `read_bh_info`, `read_bh_blob`, `remove_bh` | the coprocess, `BH_OID`, `BH_TYPE`, `BH_SIZE` and `BH_TEXT`, return 0, 1, 2 or 3 |

The store lives under `<git common dir>/history-verdicts/v1/pass-order/`, as `items/<key[0:2]>/<key>`,
`tips/<scope>` and `pruned` (`tools/lib/history_store.py#resolve_store`). The key is the sha256 of
the schema, the leg, the code digest and the item's fields. The code digest hashes the working bytes
of each code path (`tools/lib/history_store.py#derive_code_digest`). The item id is a label the
store echoes and never keys. Each verb is one python process, and it resolves the store afresh. In a
tree where the policy kit resolves beside the module, that costs 8 git processes per verb: 7 for
`policy.py get tests.history-verdicts` and 1 `rev-parse --absolute-git-dir --git-common-dir`. With no
policy kit it costs 1 [PINNED, measured 2026-11-22 under `GIT_TRACE2_EVENT` in a scratch
repository]. Section 8 F1 takes that cost.

The leg passes four code paths: `check-pass-order.sh`, `lib-unattended.sh`, the driver
`unattended.sh`, which `plan_state` is sliced from, and `commit_trailers.py`, the token and
`unchecked` reader. The leg runs from its repository root, so a path inside it is named relative and
every worktree shares the items. About 9% of commits change one of the four: 29 of the 308
first-parent commits of the 30 days to 2026-11-22 [PINNED, counted at `fa1295ff4`]. Each such
commit starts every unit cold.

### The items

Item bodies are space-separated cells. A cell or a key field that holds a space where the grammar
below has none, a backslash, a tab or a newline is never stored or looked up, and its item is
graded as today. So every stored body escapes to itself under the store's rule
(`tools/lib/history_store.py#render_escaped`).

| Kind | Key fields after the kind | Body |
|---|---|---|
| `unit` | the id, the build folder, the base or `-`, `norun` 0 or 1, `HR_MODE`, the window tip, `FORK_CUTOFF` or `-`, `GENERATED_INDEXES`, `SHARED_RECORDS`, `PREANCHOR_CAP`, the candidate list | `unbuilt`, `truncated`, `preanchor <commit>`, `nospec <build commit> <parent>`, or `spec <build commit> <parent> <state or -> <spec path>` |
| `anchors` | `MEMORY_ROOT`, the graded commit G | one `<folder>=<base or none>` cell per build with no run-state file |
| `bypass-range` | the bypass anchor, the base | `graded` or `skipped`; any other exit is not stored |
| `unchecked` | the base, G | one `<sha>:<id>,<id>` cell per line the `unchecked` verb prints, in its order |

The fields hold full shas. The base of a run-state build is the `BH_OID` of `<base>^{commit}`.
The candidate list is the sorted set of commits in `_SUBJ` whose attribution tokens carry the id as
a whole token, or `-`. In RANGE mode it keeps only the commits outside the advertised tip's history,
read from one `GIT rev-list <HR_TIP>..HEAD`. The window tip is `-` unless all three hold: RANGE
mode, a build with no run-state file, and a base that is not in the tip's history. The leg reads that
last fact in-process, as a base present in `_SUBJ` and absent from that list; a base absent from
`_SUBJ` counts as outside. Where all three hold, the window tip is `HR_TIP`. The inverted map from id
to candidates is filled from the same token stream `_SUBJ` reads, with no second git read.

An `anchors` cell's `<folder>` is the build folder's path under `<MEMORY_ROOT>/builds/`, never its
basename `slug` (`tools/unattended/check-pass-order.sh@638bb1d0c2a6:529`). The README walk lists
every `README.md` under that root, so a nested README would give two folders one slug. For every
top-level build the path and the slug read the same, and no build folder is nested at this tree.

A unit whose candidate is a root commit has no `unit` body. Today its `rev-parse "$build_c^"` fails,
and the unit counts as unbuilt after it has joined `inrange_ids`
(`tools/unattended/check-pass-order.sh@638bb1d0c2a6:663` and `:668`). The leg never stores such a
unit and never looks it up, so it is graded afresh on every run, exactly as today.

### Why a stored outcome stays true

- **The build commit.** `build_commit` walks `base..HEAD ^tip` oldest-first. It returns the first
  commit whose tokens carry the id and that touched a path outside the record surface. A commit not
  carrying the id is skipped wherever it sits, so the answer is chosen from the in-range candidates
  alone. Whether a candidate is in range, and whether it touches outside, depend only on the
  candidate, the base, the build folder and the exclusion set, and all of them are in the key.
- **The walk order.** git pops the newest commit in its queue. Where dates never run backwards along
  ancestry, the walk lists commits in committer-date order, ties broken by queue entry. Two
  candidates with different timestamps are therefore listed in the same order in every history that
  holds both. At `fa1295ff4`, no parent edge runs backwards and 15 share a second.
  Of the 10,930 commits read, 0 edges run backwards [PINNED, measured 2026-11-22 at `fa1295ff4`].
  S4 keeps the tie case out of the store. A history whose dates run backwards is the residual S8
  names.
- **The spec at the build commit.** The spec found and its state are read at the build commit's first
  parent, whose tree is immutable. `plan_state` reads the spec's bytes, its file name and
  `FORK_CUTOFF` (`tools/unattended/unattended.sh#plan_state`), and its code is in the digest.
- **The pre-anchor probe.** It walks the base's own history newest-first, less the tip's in RANGE
  mode, capped at `PREANCHOR_CAP`. That window is fixed by the base and the window tip.
- **Read every run, never stored.** The CLOSED population, `opened:`, the waiver registry, the
  range mode and its field, the bypass anchor and `hooks.bypass` are read at HEAD on every run. A
  unit that becomes CLOSED has no item, so it is graded.

The folder anchor is `rev-list --reverse HEAD -- <folder> | head -1`. When every commit of `L..G`
has one parent, the walk from G passes that chain one commit at a time, then walks exactly as from
L. Its last commit is L's anchor whenever L's is non-empty, so S3 carries it. A merge in `L..G`
recomputes every anchor. A run-state build's unwitnessed list is keyed by G, because a moved HEAD
adds commits to `base..HEAD`.

### The run

1. The per-run reads before the walk run as today. In RANGE mode the leg adds one `rev-list
   <HR_TIP>..HEAD`.
2. `init_hs`, then `init_bh` and `read_bh_info HEAD` for G, then `read_hs_tip` for L. Then, unless L
   is G, one `GIT rev-list --parents L..G`, whose lines decide whether the chain is linear.
3. A first `read_hs_items` with the `anchors` item at L, when S3's chain holds.
4. The walk reads each README and run-state file through the coprocess and derives every key. A
   second `read_hs_items` then carries every `unit`, `bypass-range` and `unchecked` item.
5. The loop takes each hit and grades each miss as today, in today's order. The first built miss
   with two or more candidates runs one lazy `GIT log --format='%H %ct' HEAD`. Its committer
   seconds serve S4's tie rule for every later miss, so a warm run at an unmoved tip never runs it.
   The loop holds the report rows and their shas. It renders them after one
   `GIT log --no-walk=unsorted --format=%h <sha>... --`, which prints each sha in argument order with
   git's own abbreviation. `rev-parse --short` takes a single revision and exits 128 on more. That
   log prints a repeated sha once, so each distinct sha is passed once and every row is filled from
   the sha-to-short map it yields.
6. The summary, the waiver rule and the exits run as today, with S7's write placed before the
   first exit that S7 allows. `remove_bh` joins the existing `EXIT` trap beside the `PS_DIR`
   removal. The request and answer files sit in `PS_DIR`, so the run leaves no temp entry.

### The warm-run bound

The counts below are for a run whose tip L is G, with the store warm.

| Source | Git processes |
|---|---|
| toplevel, the kits' generated rows, the liveness `ls-tree`, the waiver `cat-file -e` | 4 |
| the waiver registry read, where the file exists | 2 |
| `read_attribution_tokens HEAD` and `rev-list --count HEAD` | 2 |
| `read_history_range` with no remote: `git remote` | 1 |
| the bypass anchor's `log -S`, and `hooks.bypass` read with `--rev HEAD` | 5 |
| the builds' `ls-tree` | 1 |
| the coprocess | 1 |
| `read_hs_tip` and two `read_hs_items`, 8 each | 24 |
| the batched `log --no-walk=unsorted --format=%h`, where a report line exists | 1 |

On the fixture, which has no waiver file and whose `hooks.bypass` read spawns no git, a warm run
measured 35 git processes [PINNED, unit harness run `wf_977d5bd9-59b`, 2026-11-22].
TOOL-dQuietDisk-19's M2 clone has no remote, and there the rows sum to 41 [DERIVED from the table]. This unit promises **at most 45 git processes** for such a run, whatever the
unit count. The figure is PINNED as a promise and observed by AC4. A clone with a remote adds the
remote observation's 6 and the RANGE list's 1.

A tip moved by one commit adds three things. The `rev-list --parents` adds 1, the write adds 8, and
the `unchecked` read adds 1 for each build range the unwitnessed arm grades, B on the summary line.
The promise there is **at most 50 plus B**, PINNED and observed by AC4. B is 0 at `fa1295ff4`
[PINNED, 2026-11-22]. A run in which a built unit with two or more candidates misses adds one
lazy `log --format='%H %ct'` [DERIVED from step 5 of the run], beside that unit's grading spawns.
The cold counts are DERIVED at observation.

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| the leg name `pass-order` | store leg, `[a-z0-9-]+` | none; the store's grammar owns it | `tools/lib/history_store.py#resolve_store` |
| `unit`, `anchors`, `bypass-range`, `unchecked` | item kinds, the first key field | none; the leg's own field values | nothing; a wrong kind only misses |
| `PO_CANDS` | shell associative array, id to candidates | none, a local | nothing |

No verb, flag, conf key, policy key or refusal number is minted.

### Files touched (estimate)

`tools/unattended/check-pass-order.sh` · `tools/unattended/check-pass-order.test.sh`

Neither file gains a column-0 function, so the codebase map's generated symbol index is not
regenerated, and the pass writes no other path.

### Paths shared with order-2 units

None. TOOL-dQuietDisk-3 writes the brief-recorded leg and its suite, TOOL-dQuietDisk-4 the
routed-commits reader, TOOL-dQuietDisk-5 the bar runner, its suite and the kickoff manifest,
TOOL-dQuietDisk-7 the template-cache files and their registrations, and TOOL-dQuietDisk-8 the five
snapshot readers. None of them names either path above, so this unit builds in parallel with each.

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| rev-3's key, the base without the candidates, regraded on NEW-set id tokens | Items are shared by every worktree and the tip is per worktree. An item written in one worktree can then name a build commit another worktree's history lacks. |
| Key each unit item by the graded tip | Every tip move rewrites about 1,700 items, the file churn this build exists to remove. |
| One item per tip holding every outcome | About 200 KB per bar run [DERIVED: about 1,700 outcomes at about 120 bytes each], kept 30 days by the store's age prune. |
| Drop `head $RG_HEAD` from the reuse key | The leg reads history, so a reuse across commits would carry a verdict over commits it never graded. |
| Batch `build_commit`'s `show --name-only` | It is shared with `check-brief-recorded.sh` and the driver, so the change would collide with TOOL-dQuietDisk-3, and a warm run never calls it. |
| Store printed violation lines | A short sha's length grows with the object count, so a stored line could differ from the old leg's at the same HEAD. |
| Key the driver's `plan_state` slice instead of the whole driver | The leg's own bytes carry the kit version the driver's do, so a driver change moves the leg's bytes too, and nothing is saved. |

## 5. Production-readiness checklist

- security: N/A — the store lives under the git common dir and is never pushed or rendered. Its
  write path is TOOL-dQuietDisk-1's. The coprocess is pinned against replace refs (S1, AC9).
- perf / scale: a warm run is at most 45 git processes and a tip moved by one commit at most 50
  plus B (AC4). A cold run costs today's per-unit spawns plus 32 store processes, and saves the
  per-build reads.
- error / empty / loading states: a missing, unreadable, truncated or foreign-version item regrades
  its unit. A store that cannot open regrades all of them (S1, AC7, AC8).
- observability: the leg's output is unchanged; the store's `lookup` verb, run by hand with the
  leg's code paths, names each hit.
- risks: a key that misses an input carries a stale outcome. The key table and the date-order
  argument in section 4 are the defence, and AC2, AC3 and AC5 are its witnesses.
- testing: the equivalence corpus (AC1), the planted regrades (AC2, AC3, AC5), the counts (AC4),
  the fallbacks (AC6 to AC9), the adopter prefix (AC10).
- migration: none; a first run is a cold run.
- user docs: the leg's file header (S8). `help/reference/policy.md` already documents
  `tests.history-verdicts`, and no `help/` page documents this leg.

## 6. Acceptance criteria

The pass's probes run over a hermetic fixture repository F, which the probe builds under
`%TEMP%/<short-name>` in the shape `tools/unattended/check-pass-order.test.sh#seed_witness_fixture`
builds one. That suite is read for its shape and never run. F's first commit holds these:

- a copy of the driver at `tools/unattended/unattended.sh`, which carries `Commit-Checked`, so the
  bypass anchor is that commit;
- `.unattended.conf` with `PASS_ORDER_CUTOFF="2026-01-01"` and `PASS_ORDER_PREANCHOR_CAP=3`;
- `.governance/policy.toml` with `hooks.bypass` allowed.

Build `tA` carries a run-state `base:` and four CLOSED units: one built after its spec, one built
before it, one against a THIN spec, and one never built. Build `tB` has no run-state file and three
CLOSED units: one built conformingly, one built before its folder existed, and one whose probe
truncates. One pass commit names a `tA` unit with no `Commit-Checked:` trailer. The large F also
holds ten more builds of two or three units each.

"Old" is the leg at `40def53f7`, run by path from a `git clone --shared` of this repository checked
out there under `%TEMP%`. "New" is the unit's leg, run by path from the build worktree. Both run
with F as the working directory, and their stdout and stderr are compared together. A reading over
the real tree is the gate's own population, which a role agent may not run (scratch-guard row G1).
Each such reading below is owed to the main loop at the close.

- **AC1** — When old and new each run over F, the outputs and exit codes are byte-identical at each
  of four points:
  - cold;
  - warm at an unmoved tip;
  - warm after one single-parent commit that names no unit;
  - warm after a merge commit.

  This holds for both sizes of F. When the main loop runs `bash tools/unattended/check-pass-order.sh`
  old against new in TOOL-dQuietDisk-19's M2 clone of the real tree, cold then warm, the two are
  byte-identical there too.
  Red when: a stored outcome is reported differently, or a counter on the summary line moves.
  cost: seconds over F; about 18 minutes per cold run over the real tree, 1,058 s [PINNED] in
  TOOL-dQuietDisk-19's M2 row.
  permission: the real-tree corpus is owed to the main loop; the pass makes the F comparison.
- **AC2** — When F gains, past the stored tip, one build folder with a README carrying one CLOSED
  unit, both legs exit 1 with the same violation line for it. The same commit range holds one
  `git commit` that names that id and touches a product path with no spec at its first parent.
  Under `GIT_TRACE2_EVENT=<dir>`, the new leg's trace holds a `git grep` naming that id and no other,
  and a `rev-list --reverse` over that build's range and no other.
  Red when: the new leg stays green while the old leg reds, or it regrades a unit whose key held.
- **AC3** — When a commit moves `tA`'s run-state `base:` to an earlier commit, both legs exit 1 with
  the same violation line, and the new leg's trace regrades `tA`'s units and no other build's.
  Before that earlier commit sits a commit that names a `tA` unit and touches a product path with
  no spec at its parent. Separately, when a `git commit` naming one CLOSED unit in its subject and
  touching a path outside the record surface is added past the stored tip, the new leg's trace holds
  that unit's `git grep` and no other unit's, and its output equals the old leg's.
  Red when: a moved base or a moved candidate list does not regrade its units, or regrades others.
- **AC4** — When the new leg runs warm at an unmoved tip under `GIT_TRACE2_EVENT=<dir>`, the
  directory holds at most 45 files [PINNED] at each size of F, and the two counts are equal. When it
  runs warm after one single-parent commit naming no unit, it holds at most 50 plus B [PINNED]. B is
  the build-range count the summary line prints for the unwitnessed arm. Each cold count is printed
  beside its warm count. The main loop takes the unmoved-tip count over the real tree at the close,
  as TOOL-dQuietDisk-19's M2 after-reading, held to the same 45.
  Red when: a per-build or per-unit git call survives on the warm path.
  figure: 45 and 50 are PINNED as promises; the cold counts are DERIVED at observation.
  permission: the real-tree count is owed to the main loop.
- **AC5** — When two commits naming one `tA` unit carry the same `GIT_COMMITTER_DATE`, the new leg's
  output equals the old leg's, cold and warm. Both commits are in range and touch product paths.
  The warm run's trace still holds that unit's `git grep`.
  Red when: a unit whose candidates tie is served from the store.
- **AC6** — When the new leg exits 2 on a planted unreadable `PASS_ORDER_CUTOFF`, or runs under
  `--preview`, the listing of `<git common dir>/history-verdicts/v1/pass-order/` is identical before
  and after: each file's name, size and mtime. The same holds when a `git` shim placed first on
  `PATH` makes one commit in F as the builds' `ls-tree` runs.
  Red when: a refused run, a preview run or a run whose HEAD moved writes an item or the tip.
- **AC7** — Three plants each leave the new leg's output equal to the old leg's. In the first,
  every item file under `items/` is cut one byte short. In the second, each header reads
  `history-verdict v2`. In the third, `history_store.py` is removed from a `%TEMP%` copy of the new
  kit and that copy is run. Under the first two, the trace holds each built unit's `git grep` again.
  Red when: a torn, foreign or absent store gives a verdict instead of a regrade.
- **AC8** — When F commits `tests.history-verdicts = "regraded"` in `.governance/policy.toml`, a
  second run of the new leg equals the old leg's output, its trace holds each built unit's
  `git grep`, and no file under `items/` was written by either run.
  Red when: the switch at `regraded` still serves or writes an item.
- **AC9** — When F holds a `git replace` of `tA`'s README blob by one that marks its units OPEN, old
  and new print the same output cold and warm, each grading the units as CLOSED.
  Red when: the coprocess reads the replacement bytes.
- **AC10** — This criterion covers the adopter install. No fixture under `tools/govkit/fixtures/`
  installs the unattended kit (`tools/govkit/fixtures/release-0/deploy.toml` takes it out). So the
  unit's kit files and the policy kit are copied into F at the prefix `scripts/`, and committed as
  an adopter's vendored copy. When that vendored copy of the leg runs cold then warm, its output equals the base kit's copy at the same prefix, and the store's `items/`
  under F's git dir is non-empty. When `python tools/govkit/govkit.py check --target C:/projects/incms/main`
  and the same with `C:/projects/nicocares/main` run read-only from gov before and after the unit,
  each prints the same bytes and exit code.
  Red when: the store does not resolve beside a renamed kit dir, or either check reads differently.
  permission: read-only against the adopters' main checkouts, never their `gov-upgrade` worktrees.
  fixture: the adopters reach the change only after a minted version and their own `govkit update`.
- **AC11** — When `grep -c 'history verdict store' tools/unattended/check-pass-order.sh` runs, it
  prints 1 or more.
  Red when: the header does not name what a stored outcome skips.

## 7. Gates

`unattended kit gate` · `line length` · `testsuite counts (every bar self-test prints one)` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/check-pass-order.test.sh · covers AC2 AC3 AC7 · a fixture whose store is warm gains a commit that moves one unit's candidates or its build's base, and a fixture whose items are cut short; its failing case is staged by serving the stored outcome without the key · none

The arm is observed by the main loop, never by a unit pass. The real-tree halves of AC1 and AC4
are the main loop's one-time observations at the close. No standing arm compares against a literal
sha, which is `memory/gotchas/test-oracle-read-from-a-historical-sha.md`'s class.

The pass grows `tools/unattended/check-pass-order.sh` past its row in
`memory/project/shell-role.txt`. The pass does not edit that ledger. The main loop widens the row
after the pass, as it did for TOOL-dQuietDisk-1, so Files touched does not name it.

## 8. Open questions

- **F1 — Each store verb costs 8 git processes in a tree where the policy kit resolves.**
  TOOL-dQuietDisk-1's CLI resolves the git dir and reads `tests.history-verdicts` once per verb
  (`tools/lib/history_store.py#main`), and this leg needs three verbs per warm run.
  - (a) Take the cost: the bound in section 4 counts 24 for it, and the main loop files an ask
    against TOOL-dQuietDisk-1 for one mode read per leg run.
  - (b) Import the module from a python helper of the leg's own. That is a second face of the
    store, beside the one unit 1 gated byte-identical across its copies.
  - Recommendation: (a). It is bounded and does not grow with the unit count.
  RESOLVED (agent, 2026-11-22, delegated): (a), under the re-ground task's rule that a consuming
  unit follows the store as built.
- **F2 — `init_bh` starts `git cat-file --batch` without the library's replace-ref pin.** The leg's
  header requires every dereference to go through `GIT`
  (`tools/unattended/check-pass-order.sh@638bb1d0c2a6:47`), the pinned wrapper
  (`tools/unattended/lib-unattended.sh@7592fd768bc2:62`).
  - (a) The leg calls `GIT_NO_REPLACE_OBJECTS=1 init_bh`, so the coprocess ignores replace refs.
    The exported `GIT_GRAFT_FILE=/dev/null` already reaches it.
  - (b) Read the per-build blobs through `GIT show` as today, and give up S2's saving.
  - Recommendation: (a), observed by AC9.
  RESOLVED (agent, 2026-11-22, delegated): (a).
- **F3 — An item that is hit is never refreshed.** `HistoryStore.write` skips a body it already
  holds, and `remove_aged` drops items by mtime after 30 days. So a unit hit on every run is
  regraded 30 days after it was first written.
  - (a) Take the monthly regrade, and the main loop files an ask against TOOL-dQuietDisk-1 to touch
    an item on a hit.
  - (b) Rewrite hit items from the leg. The store skips an identical body, so this changes nothing.
  - Recommendation: (a). The cost is one cold grade per unit per 30 days, spread by write date.
  RESOLVED (agent, 2026-11-22, delegated): (a).
- **F4 — The CLI splits its input lines on tabs.** A key field holding a tab would join another
  field list's key text.
  - (a) The leg neither looks up nor stores an item whose fields or body hold a tab, a newline, a
    backslash or a stray space, as section 4 states.
  - (b) Escape fields in the leg. The store unescapes only bodies, so an escaped field still keys.
  - Recommendation: (a).
  RESOLVED (agent, 2026-11-22, delegated): (a).

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
- rev-4 · 2026-11-22 · §1 §2 §3 §4 §5 §6 §7 §8 §10 · S1 to S8 · AC1 to AC11 · re-grounded at
  69c9c5cb8 (order 1 built), under `2026-11-22-prompt-TOOL-dQuietDisk-2-reground-task`. Every code
  fact is re-cited by blob or symbol at `69c9c5cb8`. These moved:
  - TOOL-dWitnessedBar-2's unwitnessed-pass arm landed in the build walk, with a `merge-base` and an
    `unchecked` read per build, so S5 stores both.
  - The store as built spawns 8 git processes per verb where the policy kit resolves, where rev-3
    said its verbs start no git. The warm bound therefore moves from 30 to 45, with its tally in
    section 4, and F1 records the gap.
  - Rev-3 keyed a unit by its base and regraded it on NEW-set id tokens. The store shares items
    across worktrees, and its tip is per worktree, so that key was unsound. The key now holds the
    unit's candidate commits, the tip serves only the folder anchors (S3), and the date-order
    residual is stated (S8).
  - The coprocess's missing replace-ref pin, a hit item's 30-day expiry and the CLI's tab framing
    are F2 to F4.
  - The goal is unchanged, and acceptance grew for two reasons. The spec brief's adopter clause,
    which rev-3 lacked, is AC10. The design's new fallbacks and pins are observed by AC5 to AC9.
  - The fixture's base leg is now the copy at `69c9c5cb8`.
- rev-5 · 2026-11-22 · §3 §4 §6 §10 · AC1 · re-grounded at 40def53f7 (order 1 built, dWitnessedBar
  landed), under `2026-11-22-prompt-TOOL-dQuietDisk-2-reground-task`. Only `fb6f1a74c..8b8b1374c` was
  re-checked in the files this spec cites, and no line, symbol, argv or behaviour it relies on moved:
  - The leg, the driver and the bar runner moved only by one-line replacements: the kit-version
    line, and the bar runner's tail-keeper cut through `derive_temp_path`. The cited lines are re-cited
    at their new blobs, the leg's `638bb1d0c2a6`, the library's `7592fd768bc2` and the runner's
    `2e851a92d9ce`.
  - The library changed one line, `read_record_keys`, which now scrubs `GIT_DIR` and `GIT_WORK_TREE`
    for its `rev-parse --show-toplevel`. The waiver read it serves still costs 2 git processes, so
    the warm bound stays 45, and 50 plus B.
  - The store, its copies, `commit_trailers.py`, the leg's suite and the policy page are unchanged
    since `69c9c5cb8`.
  - AC1's old leg is now the copy at `40def53f7`. It differs from the copy at `69c9c5cb8` only in its
    kit-version line, which the leg never prints. Scope and acceptance are unchanged.
- rev-6 · 2026-11-22 · §2 §4 §7 · S4 S6 · under `2026-11-22-prompt-TOOL-dQuietDisk-2-divergence-task`,
  the run's rulings on unit 2's first-pass divergences:
  - The batched short-sha read is one `GIT log --no-walk=unsorted --format=%h <sha>... --` in S6,
    the run's step 5 and the tally, because `rev-parse --short` takes a single revision. Each
    distinct sha is passed once, because that log prints a repeated sha once.
  - A unit whose candidate is a root commit is never stored, in S4 and in section 4's items.
  - The tie rule's committer seconds come from one lazy `GIT log --format='%H %ct' HEAD`, run at the
    first built miss with two or more candidates. It is counted for a run that misses.
  - An `anchors` cell is keyed by the folder's path under `<MEMORY_ROOT>/builds/`, not its basename.
  - The fixture's warm tally is 35, as measured, where rev-5 said 39. The bound of 45 is unchanged.
  - Section 7 says the main loop widens the leg's `memory/project/shell-role.txt` row after the pass.
    Files touched is unchanged.
  - The goal, the acceptance criteria and the bounds are unchanged.

## 10. Reuse audit

The seam extended is the leg's own build walk and its two in-run caches, `_SUBJ` and `_BC_MEMO`
(`tools/unattended/check-pass-order.sh@638bb1d0c2a6:452` and `:466`). This unit persists their
answers across runs through TOOL-dQuietDisk-1's store and coprocess, and adds no store of its own.
`_SUBJ` now also feeds the candidate map, with no second read. TOOL-dWitnessedBar-2's
unwitnessed-pass arm (`:579` to `:593`) is extended in place: its two per-build reads become S5's
items, and its rule and output are unchanged.

The chain build owning the area is dWitnessedBar (Test: gate health), whose landed unit 2 changed
this file. dScopedBuild (Build: the history-derived exit base) shares the range rule, and
TOOL-dUnstuckLanding-17's RANGE mode becomes key input. No dWitnessedBar unit made this leg
incremental. Of its specs, only units 2, 16, 27 and 54 name this file. Its non-merge commits in
`git log 59e882afd..fb6f1a74c` touch the file only for unit 2 and two kit-version mints. In
`fb6f1a74c..8b8b1374c` only the landing merge `fcd824fed` touches it, and only for its kit-version
line. The same 4 dWitnessedBar specs name it at `40def53f7`.

`python tools/codebase-map/reuse_lookup.py "reuse a stored per-unit verdict keyed by the commits it reads in a history leg"`
returned name-token neighbours only (`read_text`, `key`, `read`, `leg`, `legs`). No existing seam fits
beyond the leg's own caches and the store this build adds. Recall returned TOOL-dBriefedPass-3, the
leg's origin, TOOL-aSurfacedLexicon-22's subject-cache record, TOOL-aWeldedTribunal-9's ask about
this leg's ceiling, this build's spec brief, and rev-3 of this spec. The source agreed with each hit.

Recall terms used: check-pass-order build_commit history verdict store candidate commits folder anchor incremental warm run coprocess
