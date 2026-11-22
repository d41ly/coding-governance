# TOOL-dQuietDisk-3 — the brief-recorded leg grades only units whose key moved since its last graded tip

**Status:** SPECCED · rev-4 · 2026-11-22 · node d · Tier-2 · base 40def53f · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-2-reground-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-2-reground-task.md) | research | TOOL-dQuietDisk-2 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 |
| [2026-11-22-prompt-TOOL-dQuietDisk-3-1-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-3-1-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`tools/unattended/check-brief-recorded.sh` regrades every CLOSED unit it reaches on every bar. The
analysis counts about 6k to 8k git processes and 404 s [PINNED] per run
(`memory/builds/dQuietDisk/build/2026-11-20-build-TOOL-dQuietDisk-19-analysis.md`, row G3). At
`8688cdbba` the leg reaches about 76 builds holding about 1,365 CLOSED units [PINNED, counted on
2026-11-22 by one read-only batch read of the build READMEs and run-state files, not by the leg].

This unit stores each unit's outcome in TOOL-dQuietDisk-1's history verdict store. The key holds the
commits and blobs the outcome reads. The leg's per-build reads at HEAD go through the store's one
`cat-file --batch` coprocess. A warm run then costs a bounded, stated number of git processes,
whatever the unit count. Every exit code and printed line stays byte-identical.

The key carries "since its last graded tip", and no stored tip does. A unit's key holds every commit
whose tokens name it. So a unit is regraded exactly when a commit naming it lands after it was
graded, or when another input in its key moves. Section 4 says why a stored tip would be unsound
here.

## 2. Scope (IN)

- **S1** — The leg opens the store once per run, after the cutoff check and before the subject
  cache. It calls `init_hs brief-recorded` with its four code paths. It starts the coprocess with
  `GIT_NO_REPLACE_OBJECTS=1 init_bh`, and resolves HEAD once, to the full sha G, through
  `read_bh_info HEAD`. It closes the coprocess with `remove_bh` on exit. Where `init_hs` or
  `init_bh` fails, or a store verb exits non-zero, every read misses and the leg grades as today.
  Observed by AC1, AC8, AC9 and AC10.
- **S2** — The loop that fills `_SUBJ` from the one `read_attribution_tokens HEAD` stream also fills
  `BR_CANDS`. That map takes each token to the commits whose line carries it, in stream order. No
  second git read fills it. In RANGE mode the leg adds one `GIT rev-list HEAD ^<HR_TIP>`. From that
  list it knows, in-process, which commits sit in the advertised tip's history. Observed by AC2 and
  AC3.
- **S3** — Each build's reads at HEAD go through the coprocess with `read_bh_blob`. The README is
  read once, for both `opened:` and the CLOSED ids, and the run-state file once. The base check becomes
  one `read_bh_info "<base>^{commit}"`, whose `BH_OID` is the full base. The builds' `ls-tree` stays
  one process and also lists blob ids. So the blob id of each `RUN.<phase>.<8hex>.md` record in a
  build folder is known in-process. Where a coprocess read returns 2 or 3, that one read falls back
  to today's `GIT show` or `GIT cat-file -e`. Observed by AC1, AC4 and AC10.
- **S4** — Each CLOSED unit's outcome is one `unit` item, under the key fields section 4 lists. One
  `read_hs_items` call looks up every item before the unit loop. A unit whose key fields hold a tab,
  a newline or a backslash is neither looked up nor stored, and is graded as today. Observed by AC1,
  AC2 and AC3.
- **S5** — A hit is replayed as its outcome. A miss is graded exactly as the code at the base grades
  it, and its outcome becomes a body in the grammar section 4 gives. A hit whose body does not parse
  is graded as a miss. An outcome is not stored when two of the unit's candidates share a committer
  timestamp, or when a cell breaks the grammar. Observed by AC1, AC5 and AC8.
- **S6** — The counters, the violation lines through `add_violation`, the `announced` lines, the
  waiver bookkeeping, the stale-waiver rule and the summary lines come from the outcomes in loop
  order, as today. Every short sha a line names is rendered after the loop, by one
  `GIT rev-parse --short` over all of them, and is never stored. The leg prints no line of its own
  about the store, and it discards the store's stderr. Observed by AC1.
- **S7** — The leg writes with one `write_hs_items` call and passes no tip. The call runs after the
  unit loop, and only when one `GIT rev-parse HEAD` still reads G. Its request holds every outcome
  this run graded that S5 allows to be stored. The call is skipped when there is none. The lookup
  and store requests pass through process substitutions, so the leg creates no temp entry. Observed
  by AC4, AC6 and AC7.
- **S8** — The file header's "WHAT THIS DOES NOT CHECK" list gains one bullet. It names the history
  verdict store, what a stored outcome skips, the switch `tests.history-verdicts` that turns it off,
  and the date-order residual section 4 states. Observed by AC12.

## 3. Non-goals (OUT)

- No change to `tools/unattended/lib-unattended.sh`, the store's block in it included.
  `build_commit`, `read_history_range`, `read_attribution_tokens` and `read_record_keys` are called
  as they are. The leg only avoids calling `build_commit` for a unit whose outcome is a hit.
  TOOL-dQuietDisk-2 reads the same library, and neither unit writes it.
- No change to `tools/unattended/commit_trailers.py` or to TOOL-dQuietDisk-1's store. A gap in the
  store is that unit's deviation, named in section 8.
- No second store. `_SUBJ` and `_BC_MEMO` stay in-run maps, and what persists is each unit's
  outcome.
- No tip is read or written, for the reason section 4 gives.
- No change to the predicate, the waiver registry, the cutoff, the exit codes or the summary fields.
- No change to the bar runner's reuse key for this leg. Its row in `tools/gate-legs.json` declares
  that it reads the remote, so the key holds HEAD
  (`tools/run-gates/run-gates.sh@2e851a92d9ce:3553`). The leg still runs on every bar; it does less.
- A cold run's per-unit spawns stay as today. The cold saving is the per-build reads and the batched
  short shas.
- No column-0 function in either file, so the codebase map's symbol index does not move.
- The unattended kit's suites are never run by this unit (owner rule, 2026-08-23).

### Edges

- **consumes-from** `TOOL-dQuietDisk-1` — the store's bash face in the unattended kit's library,
  its `cat-file --batch` coprocess and its policy key `tests.history-verdicts`. Without them every
  read misses, and the leg grades every unit as today.
- **consumes-from** external — dWitnessedBar's land tip `fb6f1a74c`, merged into this run at
  `b3f5a2bc3`, and its landing on main at `8b8b1374c`, merged at `40def53f7`. Its units 16, 27 and
  54 changed this leg: the waiver read through the ledger factory, the wrong-shell refusal and the
  generated rows' `when`.

## 4. Design

### The leg at the base

All citations are read at `40def53f7`. There the leg's blob is `a78fe6040556`, the library's
`7592fd768bc2` and the suite's `a0378d145f12`, and HEAD `8688cdbba` carries the same three blobs.

The leg checks its cutoff (`tools/unattended/check-brief-recorded.sh@a78fe6040556:455`). It builds
`_SUBJ` from one `read_attribution_tokens HEAD` call and checks its size against
`rev-list --count HEAD` (`:477` to `:486`). It declares the walk memo `_BC_MEMO` (`:491`) and reads
the history range once (`:503`). Where `cat-file -e` finds the waiver registry, it reads it through
`read_record_keys` (`:518`, `:521`). One `ls-tree -r --name-only` lists every build README at HEAD
(`:538`). Per build it runs these:

- `git show` of the README, for `opened:` (`:541`) and again for the CLOSED ids (`:570`);
- `git show` of the run-state file (`:556`), and `cat-file -e` of its base (`:560`).

Per CLOSED unit it calls `tools/unattended/lib-unattended.sh#build_commit` over
`<base>..HEAD $HR_EXCL` (`:581`). That call runs one `rev-list` per range, memoised. It also runs one
`git show --name-only` per candidate commit whose tokens carry the id
(`tools/unattended/lib-unattended.sh@7592fd768bc2:1410`). A unit with a build commit then reads the
run-state file there (`:589`). When that file's phase is terminal, the leg walks
`rev-list --reverse <build>..HEAD` for a later candidate made during a live run (`:607` to `:614`).
It then asks whether HEAD still makes the claim, in the run-state file or in a retired
`RUN.<phase>.<8hex>.md` (`:630` to `:642`). It reads the brief row's blob with one `ls-tree`
(`:704`). A unit with no row runs the pre-run probe, `build_commit` behind the base with the cap
(`:666`). Each printed line adds one `rev-parse --short` per sha it names (`:618`, `:647`, `:674`).

### The store as built

The leg consumes the store's bash face as `tools/lib/history-store.sh` spells it, in the copy
inlined in `tools/unattended/lib-unattended.sh#init_hs`:

| Call | What it does here |
|---|---|
| `init_hs brief-recorded <code path>...` | sets `HS_PY`, `HS_MODULE` and `HS_ARGS`, the module found beside the library |
| `read_hs_items <file>` | reads `<item id>TAB<field>...` lines and prints `<item id>TAB<hit or miss>TAB<body>` lines |
| `write_hs_items <file>` | stores each `<item id>TAB<field>...TAB<body>` line, then the daily prune |
| `init_bh`, `read_bh_info`, `read_bh_blob`, `remove_bh` | the coprocess, setting `BH_OID`, `BH_TYPE`, `BH_SIZE` and `BH_TEXT`, returning 0, 1, 2 or 3 |

The store lives under `<git common dir>/history-verdicts/v1/brief-recorded/`, as
`items/<key[0:2]>/<key>`, `tips/<scope>` and `pruned` (`tools/lib/history_store.py#resolve_store`).
This leg writes no file under `tips/`. The key is the sha256 of the schema, the leg, the code digest
and the item's fields. The code digest hashes the working bytes of each code path
(`tools/lib/history_store.py#derive_code_digest`). The item id is a label the store echoes and never
keys.

Each verb is one python process, and it resolves the store afresh. In a tree where the policy kit
resolves beside the module, that costs 8 git processes per verb. With no policy kit it costs 1
[PINNED, measured 2026-11-22 under `GIT_TRACE2_EVENT` in a scratch repository, as the design
section of TOOL-dQuietDisk-2 records it]. Section 8 F1 takes that cost.

The leg passes four code paths:

- `check-brief-recorded.sh`, the leg;
- `lib-unattended.sh`, which holds `build_commit`;
- the driver `unattended.sh`, whose `PHASES_TERMINAL` the leg parses;
- `commit_trailers.py`, the token reader.

Each is named relative to the repository root, through
`tools/unattended/lib-unattended.sh#derive_self_rel`, so every worktree shares the items. Where that walk fails, the absolute paths are passed, and the
items are then that checkout's own.

### The key

| Field | Why it is in the key |
|---|---|
| `unit`, the kind | names the item kind |
| the unit id and its build folder | the identity; the folder is the record surface every pick excludes, and it names the run-state path |
| the base, the full `BH_OID` of `<base>^{commit}` | the in-range walk starts there, and the pre-run probe walks behind it |
| the candidates: `BR_CANDS[<id>]` in stream order, or `-` | every commit any of the unit's three walks can select: the in-range pick, the later-live walk and the pre-run probe |
| the excluded candidates: in RANGE mode those in the advertised tip's history, else `-` | the only effect `$HR_EXCL` has on the in-range pick |
| HEAD's claim, as three fields: its base, phase and witness | the finished-run branch compares the build commit's claim with it |
| the retired records at HEAD: each `RUN.<phase>.<8hex>.md` directly in the build folder with its blob id, in `ls-tree` order, or `-` | the second place the finished-run branch finds the claim |
| `GENERATED_INDEXES` as resolved, `SHARED_RECORDS` and `PREANCHOR_CAP` | the exclusion set of every pick, and the probe's cap |

The shas are full. A RANGE run whose excluded set is empty keys like a WHOLE run, and both pick the
same commit, since an exclusion that removes no candidate changes no pick. The candidates keep the
order the token stream prints them in, so no `sort` runs. Two worktrees listing one set in another
order only miss.

### Why a stored outcome stays true

- **The in-range pick.** `build_commit` walks `<base>..HEAD ^<tip>` oldest-first. It returns the
  first commit whose tokens carry the id and that touches a path outside the record surface. Every
  other commit is skipped, so only the in-range candidates matter. Whether a candidate is in range
  depends on it, the base and the excluded set. Whether it touches outside depends on it, the
  folder and the exclusion set. All of them are in the key.
- **The later-live walk.** The walk over `<build>..HEAD` keeps only commits whose tokens carry the
  id. It asks each one the same predicate and reads the run-state phase in that commit's own tree.
  The candidates after the build commit come from the key's list, and each tree is immutable.
- **The finished-run claim.** The build commit's claim is read in its own tree. HEAD's claim and its
  retired records are in the key. Whether a retired name existed at the build commit is a fact about
  that commit.
- **The brief.** The row, its hash and the blob of its path are read at the build commit.
- **The pre-run probe.** It walks the base's own history newest-first, capped at `PREANCHOR_CAP`.
  That window is fixed by the base and the cap, and only the candidates inside it can answer.
- **The walk order.** TOOL-dQuietDisk-2 section 4 gives the argument. Wherever dates never run
  backwards along ancestry, git lists commits in committer-date order, ties broken by queue entry.
  So two candidates with different timestamps are listed in the same order in every history that
  holds both. At `8688cdbba`, 0 of the parent edges among 10,983 commits [PINNED] run backwards,
  and 84 commits share their committer second with another [PINNED, both measured 2026-11-22 from
  one `git log --format='%H %ct %P' HEAD`]. S5 keeps the tie case out of the store. A history whose
  dates run backwards is the residual S8 names.
- **Read on every run, never stored.** The build list, `opened:`, the cutoff, the CLOSED ids, the
  waiver registry and the range field are read at HEAD on every run. A unit that becomes CLOSED has
  no item, so it is graded.

Rev-3 read a tip and regraded a unit when a commit past that tip named it. The store shares items
across worktrees, and its tip is per worktree (`tools/lib/history_store.py#resolve_store`). So an
item written in one worktree could carry a build commit another worktree's history lacks, and that
worktree's commits past its own tip would not regrade it. Keying the candidates closes that, as
TOOL-dQuietDisk-2 rev-4 found for its leg. It also leaves a tip with no reader, so this leg keeps
none.

### The items

The body is space-separated cells, in this grammar:

```
body    = "unbuilt" | "postrun" SP c SP ph SP stands | [ later | unborne ] result
later   = "later" SP c0 SP c SP ph SP lph SP
unborne = "unborne" SP c SP ph SP
result  = "ok" SP c | "norow" SP c | "prebuilt" SP pre SP c | "badhash" SP c SP rest
        | "nopath" SP c SP path | "moved" SP c SP hash SP blob SP path
```

| Word | What the replay does |
|---|---|
| `unbuilt` | `unbuilt` counts it |
| `later` | `regraded` counts it, and the GRADED AT A LATER COMMIT line names `c0`, `c`, `ph` and `lph`, where a `-` prints as `no phase` |
| `postrun` | `postrun` counts it, and the NOT GRADED line names `c`, `ph` and `stands` |
| `unborne` | `unborne` counts it, and the GRADED ANYWAY line names `c` and `ph` |
| `ok` | nothing is printed |
| `norow`, `badhash`, `nopath`, `moved` | one `add_violation` call carrying today's message |
| `prebuilt` | `prebuilt` counts it, and the built-before-its-run line names `pre` and `c` |

Every word but `unbuilt` adds the id to `inrange_ids`, as today, and `graded` counts every unit, hit
or miss. The cells `c`, `c0`, `pre` and `blob` are full shas. `ph` is a terminal phase, and `lph` is
a phase matching `[A-Z]+`, or `-` for none. `hash` is the row's twelve hex. `stands`, `path` and
`rest` are the leg's own text, and only the last cell of a body may hold a space or be empty.

An outcome is not stored when any of these holds:

- a cell holds a backslash, a tab or a newline;
- a cell other than the last holds a space or is empty;
- `lph` is neither empty nor `[A-Z]+`;
- two of the unit's candidates share a committer timestamp.

So every stored body escapes to itself under `tools/lib/history_store.py#render_escaped`, and a
hit's body is read as printed. The timestamps come from the candidates' commit objects, read through the
coprocess with `read_bh_blob <sha>` and parsed at the `committer` line. A read that fails means the
outcome is not stored. That check runs only for a miss being stored, and starts no git process.

### The run

1. The per-run reads before the subject cache run as today, the cutoff check included.
2. `init_hs`, then `init_bh`, then `read_bh_info HEAD` for G.
3. The subject-cache loop fills `_SUBJ` and `BR_CANDS`, and the size check runs as today. Then
   `read_history_range` runs as today, and in RANGE mode one `GIT rev-list HEAD ^<HR_TIP>` follows.
4. The waiver read runs as today. The builds' `ls-tree -r` runs with blob ids. A first pass over the
   builds reads each README and run-state file through the coprocess. Each text drops its trailing
   newlines, as the command substitution it replaces drops them. It counts the cutoff and
   no-base builds as today and derives every unit's key. One `read_hs_items` answers all of them.
5. The unit loop takes each hit and grades each miss as today, in today's order. It holds each line
   with its full shas.
6. One `GIT rev-parse --short` renders the named shas. S7's write runs. The summary, the lines and
   the waiver rule print as today, and the leg exits as today. The `EXIT` handler closes the
   coprocess.

Today's loop prints nothing before the summary, so splitting the build walk into two passes moves
no line.

### The warm-run bound

These counts are for a warm run at an unmoved tip, with no remote.

| Source | Git processes |
|---|---|
| the toplevel (`:309`), and the kits' generated rows through one `ls-files` | 2 |
| the waiver `cat-file -e`, and the registry read where the file exists | 3 |
| `read_attribution_tokens HEAD` and `rev-list --count HEAD` | 2 |
| `read_history_range` with no remote: `git remote` | 1 |
| the builds' `ls-tree` | 1 |
| the coprocess | 1 |
| one `read_hs_items` | 8 |
| the batched `rev-parse --short`, where a line names a sha | 1 |

That makes 19, in the fixture of section 6 and in a scratch clone of the real tree with its remote
removed. This unit promises **at most 25 git processes** for such a run, whatever the unit count.
The figure is PINNED as a promise and observed by AC4. A clone with a remote adds the remote
observation, which this unit does not change, and RANGE mode adds 1.

A commit that names no unit and moves no key adds nothing, because every item still hits, and
nothing is written. A commit naming one unit adds that unit's regrade, the write's 8 and the guard's
1. The cold counts are DERIVED at observation.

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| the leg name `brief-recorded` | store leg, `[a-z0-9-]+` | none; the store's grammar owns it | `tools/lib/history_store.py#resolve_store` |
| `unit` | item kind, the first key field | none; the leg's own field value | nothing; a wrong kind only misses |
| `unbuilt`, `later`, `postrun`, `unborne`, `ok`, `norow`, `prebuilt`, `badhash`, `nopath`, `moved` | body words | none; the leg's own cell values | the replay; a body that does not parse is a miss |
| `BR_CANDS` | shell associative array, token to commits | none, a local | nothing |

No verb, flag, conf key, policy key or refusal number is minted.

### Files touched (estimate)

`tools/unattended/check-brief-recorded.sh` · `tools/unattended/check-brief-recorded.test.sh`

Neither file gains a column-0 function, so the codebase map's generated symbol index is not
regenerated. Neither path is on the kickoff manifest's `watch:` line, and the pass writes no other
path.

### Paths shared with order-2 units

None. TOOL-dQuietDisk-2 writes the pass-order leg and its suite, and TOOL-dQuietDisk-4 the
routed-commits reader. TOOL-dQuietDisk-5 writes the bar runner, its suite and the kickoff manifest's
re-stamp. TOOL-dQuietDisk-7 writes the template-cache files and their registrations, and
TOOL-dQuietDisk-8 the five snapshot readers. None of them names either path above, so this unit
builds in parallel with each.

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| Rev-3's key: the base and HEAD's claim with no candidates, regraded on commits past a stored tip | The store shares items across worktrees, and the tip is per worktree, so an item can name a build commit another worktree lacks. |
| Key each unit by HEAD | That is the reuse cache's key today, and it is why nothing is reused across commits. |
| Key the run-state file's blob at HEAD, not its claim | A live build's run-state file is rewritten at every phase and lease edit (`tools/unattended/lib-unattended.sh#check_lease_only_diff` names the lease-only edit), so its units would regrade on most runs. The claim is all the leg reads there. |
| One item per tip holding every outcome | About 160 KB per bar run [DERIVED: about 1,365 outcomes at about 120 bytes each], kept 30 days by the store's age prune. |
| Store the printed lines | A short sha's length grows with the object count, so a stored line could differ from the old leg's at the same HEAD. |
| Persist `_SUBJ` alone | It saves one log per run and leaves every per-unit spawn, which is where the 404 s [PINNED] goes. |
| A library function for the candidate map, shared with TOOL-dQuietDisk-2 | It would write `tools/unattended/lib-unattended.sh`, which neither order-2 unit writes. The map is filled inside each leg's own `_SUBJ` loop, the seam each leg already owns. |

## 5. Production-readiness checklist

- security: N/A — the store lives under the git common dir and is never pushed or rendered. Its
  write path is TOOL-dQuietDisk-1's. The coprocess is pinned against replace refs (S1, AC10).
- perf / scale: a warm run is at most 25 git processes (AC4). A cold run costs today's per-unit
  spawns, plus 18 for the coprocess, the two store verbs and the guard. It saves 4 reads per build
  the walk reaches, and every per-line `rev-parse --short` but one.
- error / empty / loading states: a missing, unreadable, truncated, foreign-version or unparsable
  item regrades its unit. A store that cannot open regrades all of them (S1, S5, AC8).
- observability: the leg's output is unchanged. The store's `lookup` verb, run by hand with the
  leg's code paths, names each hit.
- risks: a key that misses an input carries a stale outcome. The key table and the argument in
  section 4 are the defence, and AC2, AC3 and AC5 are its witnesses.
- testing: the equivalence corpus (AC1), the planted regrades (AC2, AC3, AC5), the count (AC4), the
  fallbacks and pins (AC6 to AC10), the adopter prefix (AC11).
- migration: none; a first run is a cold run.
- user docs: the leg's file header (S8). `help/reference/policy.md` already documents
  `tests.history-verdicts`, and no `help/` page documents this leg.

## 6. Acceptance criteria

The pass's probes run over a hermetic fixture repository F, which the probe builds under
`%TEMP%/<short-name>`. It takes the shape `tools/unattended/check-brief-recorded.test.sh#mkfixture`
builds, and the waiver row the shape `tools/unattended/check-brief-recorded.test.sh#write_waiver`
writes. That suite is read for its shapes and never run. F's first commit holds these:

- the kit files the leg sources and runs, with `history_store.py` beside them;
- `tools/policy/`, so the store reads its switch as it does in the real tree;
- `.unattended.conf` with `BRIEF_RECORDED_CUTOFF="2026-01-01"` and `PASS_ORDER_PREANCHOR_CAP=3`.

F's builds carry at least one unit of every outcome word in section 4's grammar, staged as the
suite's arms stage each. So over F the old leg's summary line prints a non-zero count for each of
`unbuilt-in-range`, built after their run finished, built under a claim HEAD does not bear out,
graded at the later commit, and built before their run. Its FAILED block names all four violation
messages, and the waiver registry waives one of them. The large F adds ten more builds of two or
three units each. F has no remote. F-range is a clone of F with a bare origin at an earlier commit,
in the shape `tools/unattended/check-brief-recorded.test.sh#seed_brange_fixture` builds, so the leg
runs there in RANGE mode.

"Old" is the leg at `40def53f7`, run by path from a `git clone --shared` of this repository checked
out there under `%TEMP%`. "New" is the unit's leg, run by path from the build worktree. Both run
with the fixture as the working directory, and their stdout and stderr are compared together. A reading
over the real tree is the gate's own population, which a role agent may not run (scratch-guard row
G1). Each such reading below is owed to the main loop at the close.

- **AC1** — When old and new each run over F, the outputs and exit codes are byte-identical at each
  of four points:
  - cold;
  - warm at an unmoved tip;
  - warm after one single-parent commit that names no unit;
  - warm after a merge commit.

  This holds for both sizes of F and for F-range. The main loop also runs
  `bash tools/unattended/check-brief-recorded.sh` old against new in a scratch `git clone --shared`
  of the real tree at the build's base, its remote removed, cold then warm. The two are
  byte-identical there too.
  Red when: a stored outcome is reported differently, or a counter on the summary line moves.
  cost: seconds over F; about 7 minutes per cold run over the real tree, 404 s [PINNED] by the
  analysis.
  permission: the real-tree corpus is owed to the main loop; the pass makes the F comparison.
- **AC2** — F gains, past a warm run, one build folder with a pinned `base:` and one CLOSED unit,
  and one `git commit` that names that id, touches a product path and leaves no brief row in the
  run-state file. Both legs then exit 1 with the same violation line for it. Under
  `GIT_TRACE2_EVENT=<dir>`, the new leg's trace holds a `show --name-only` of that commit and of no
  other commit.
  Red when: the new leg stays green while the old leg reds, or it regrades a unit whose key held.
- **AC3** — Three plants are each made over a warm F, and after each the new leg's output equals the
  old leg's:
  - a `git commit` naming one CLOSED unit in its subject and touching a path outside the record
    surface, after which the trace holds a `show --name-only` for that unit's candidates only;
  - a commit adding a retired `RUN.LANDED.<8hex>.md` that makes the claim of the build whose claim
    HEAD did not bear out, after which that unit reads as built after its run finished;
  - a commit moving the live build's run-state phase.

  After the second and third plants, every `show` in the trace naming a run-state file names that
  build's folder.
  Red when: a moved candidate list, retired record or claim does not regrade its units, or regrades
  another build's.
- **AC4** — When the new leg runs warm at an unmoved tip under `GIT_TRACE2_EVENT=<dir>`, the
  directory holds at most 25 files [PINNED] at each size of F, and the two counts are equal. The
  same bound holds warm after one single-parent commit that names no unit. Each cold count, and the
  old leg's count, is printed beside the warm count. The main loop takes the unmoved-tip count over
  the real tree at the close, in AC1's clone, held to the same 25.
  Red when: a per-build or per-unit git call survives on the warm path, or the count grows with F.
  figure: 25 is PINNED as a promise; the cold and old counts are DERIVED at observation.
  permission: the real-tree count is owed to the main loop.
- **AC5** — Two commits name one unit, carry the same `GIT_COMMITTER_DATE`, and both sit in range
  touching product paths. The new leg's output then equals the old leg's, cold and warm, and the
  warm run's trace still holds that unit's `show --name-only`.
  Red when: a unit whose candidates tie is served from the store.
- **AC6** — The listing of `<git common dir>/history-verdicts/v1/brief-recorded/` is identical
  before and after two runs, each file's name, size and mtime compared. In one, the new leg exits 2 on a
  planted `BRIEF_RECORDED_CUTOFF="soon"`. In the other, a `git` shim placed first on `PATH` makes
  one commit in F while the builds' `ls-tree` runs.
  Red when: a refused run, or a run whose HEAD moved, writes an item.
- **AC7** — With `TEMP`, `TMP` and `TMPDIR` pointed at an empty scratch directory, that directory
  holds 0 entries after the new leg's cold run and after its warm run over F. A watcher listing it
  every 0.5 s sees no more entries during either run than during the old leg's.
  Red when: the leg or the store leaves an entry there, or adds one the old leg did not.
- **AC8** — Four plants each leave the new leg's output equal to the old leg's:
  - every item file under `items/` cut one byte short;
  - each item header changed to read `history-verdict v2`;
  - each body replaced by `garbage`, with its header's length fixed;
  - `history_store.py` removed from a `%TEMP%` copy of the new kit, and that copy run.

  Under the first three, the trace holds each built unit's `show --name-only` again.
  Red when: a torn, foreign, unparsable or absent store gives a verdict instead of a regrade.
- **AC9** — When F commits `tests.history-verdicts = "regraded"` in `.governance/policy.toml`, a
  second run of the new leg equals the old leg's output. Its trace holds each built unit's
  `show --name-only`, and neither run writes a file under `items/`.
  Red when: the switch at `regraded` still serves or writes an item.
- **AC10** — F holds a `git replace` of one build README's blob, by a blob that marks that build's
  units OPEN. Old and new then print the same output, cold and warm, each grading those units as
  CLOSED.
  Red when: the coprocess reads the replacement bytes.
- **AC11** — This criterion covers the adopter install. No fixture under `tools/govkit/fixtures/`
  installs the unattended kit (`tools/govkit/fixtures/release-0/deploy.toml` takes it out). So the
  unit's kit files and the policy kit are copied into F at the prefix `scripts/` and committed as an
  adopter's vendored copy. When that vendored leg runs cold then warm, its output equals the base
  kit's copy at the same prefix, and the store's `items/` under F's git dir is non-empty. Also,
  `python tools/govkit/govkit.py check --target C:/projects/incms/main`, and the same with
  `C:/projects/nicocares/main`, run read-only from gov before and after the unit. Each prints the
  same bytes and exit code both times.
  Red when: the store does not resolve beside a renamed kit dir, or either check reads differently.
  permission: read-only against the adopters' main checkouts, never their `gov-upgrade` worktrees.
  fixture: the adopters reach the change only after a minted version and their own `govkit update`.
- **AC12** — When `grep -c 'history verdict store' tools/unattended/check-brief-recorded.sh` runs,
  it prints 1 or more.
  Red when: the header does not name what a stored outcome skips.

## 7. Gates

`unattended kit gate` · `line length` · `testsuite counts (every bar self-test prints one)` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/check-brief-recorded.test.sh · covers AC2 AC3 AC8 · a fixture whose store is warm gains a commit that moves one unit's candidates, its build's claim or its retired records, and a fixture whose items are cut short; its failing case is staged by serving the stored outcome without the key · none

The arm is observed by the main loop, never by a unit pass. The real-tree halves of AC1 and AC4
are the main loop's one-time observations at the close. No standing arm compares against a literal
sha, which is `memory/gotchas/test-oracle-read-from-a-historical-sha.md`'s class.

## 8. Open questions

- **F1 — Each store verb costs 8 git processes in a tree where the policy kit resolves.**
  TOOL-dQuietDisk-1's CLI resolves the git dir and reads `tests.history-verdicts` once per verb
  (`tools/lib/history_store.py#main`). This leg runs one verb on a warm run and two on a run that
  writes.
  - (a) Take the cost. Section 4's bound counts 8 for it, and the main loop files an ask against
    TOOL-dQuietDisk-1 for one mode read per leg run, as TOOL-dQuietDisk-2 F1 does.
  - (b) Import the module from a python helper of the leg's own. That would be a second face of the
    store, beside the one unit 1 holds byte-identical across its copies.
  - Recommendation: (a). The cost is bounded and does not grow with the unit count.
  RESOLVED (agent, 2026-11-22, delegated): (a), under the re-ground task's rule that a consuming
  unit follows the store as built.
- **F2 — `init_bh` starts `git cat-file --batch` without the library's replace-ref pin.** The leg's
  header requires every dereference to go through `GIT`
  (`tools/unattended/check-brief-recorded.sh@a78fe6040556:119`), the pinned wrapper
  (`tools/unattended/lib-unattended.sh@7592fd768bc2:62`).
  - (a) The leg calls `GIT_NO_REPLACE_OBJECTS=1 init_bh`, so the coprocess ignores replace refs.
    The exported `GIT_GRAFT_FILE=/dev/null` (`:118`) already reaches it.
  - (b) Read the per-build blobs through `GIT show` as today, and give up S3's saving.
  - Recommendation: (a), observed by AC10, as TOOL-dQuietDisk-2 F2 resolved it.
  RESOLVED (agent, 2026-11-22, delegated): (a).
- **F3 — An item that hits is never refreshed.** `HistoryStore.write` skips a body it already holds,
  and `remove_aged` drops items by mtime after 30 days. So a unit that hits on every run is regraded
  30 days after it was first written.
  - (a) Take the monthly regrade, and the main loop files an ask against TOOL-dQuietDisk-1 to touch
    an item on a hit.
  - (b) Rewrite hit items from the leg. The store skips an identical body, so this changes nothing.
  - Recommendation: (a). The cost is one cold grade per unit per 30 days, spread by write date.
  RESOLVED (agent, 2026-11-22, delegated): (a).
- **F4 — The CLI splits its input lines on tabs.** A key field holding a tab would join another
  field list's key text, and the store unescapes only bodies.
  - (a) The leg neither looks up nor stores an item whose fields hold a tab, a newline or a
    backslash, or whose body breaks section 4's cell rules (S4, S5).
  - (b) Escape fields in the leg. An escaped field still keys, so (b) adds a rule and buys nothing.
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
  1, section 4 and section 6 the analysis's wall-time figure, in the goal, the alternatives table and
  AC1's cost line, is marked PINNED, and AC3's warm bound PINNED as the promise its `figure:` line
  already makes. Design, scope and acceptance unchanged.
- rev-4 · 2026-11-22 · §1 §2 §3 §4 §5 §6 §7 §8 §10 · S1 to S8 · AC1 to AC12 · re-grounded at
  40def53f7 (order 1 built, dWitnessedBar landed), under
  `2026-11-22-prompt-TOOL-dQuietDisk-2-reground-task`. Every code fact is re-cited by blob or symbol
  at `40def53f7`. These moved:
  - The leg moved only by its kit-version line between `59e882afd` and `40def53f7`, in the mints
    `1f7a47932` and `608aa364c` and the landing merge `fcd824fed`. Every cited line holds at its new
    blob `a78fe6040556`. The library gained the store's block, the `read_record_keys` scrub,
    `resolve_fleet_tag` and a stricter row read in `resolve_generated_indexes`. None of them changes
    a call this leg makes, and the old leg at `40def53f7` reads the same library.
  - The store as built spawns 8 git processes per verb where the policy kit resolves, where rev-3
    said its verbs start no git. The warm bound is re-tallied in section 4, at 19 with a promise of
    25 where rev-3 promised 30. F1 records the gap.
  - Rev-3 keyed a unit by its base and HEAD's claim and regraded it on commits past a stored tip.
    The store shares items across worktrees and its tip is per worktree, so that key was unsound.
    TOOL-dQuietDisk-2 rev-4 found the same for its leg. The key now holds the unit's candidate
    commits, its excluded subset and the retired records' blob ids, and the leg keeps no tip. The
    date-order residual is stated (S5, S8).
  - Rev-3's S6 premise that a run exiting 2 could write was empty: every exit 2 comes before the
    loop. The write guard is now a HEAD that moved during the run (S7, AC6).
  - The coprocess's missing replace-ref pin, a hit item's 30-day expiry and the CLI's tab framing
    are F2 to F4.
  - The goal is unchanged, and acceptance grew for two reasons. The spec brief's adopter clause,
    which rev-3 lacked, is AC11. The new key, fallbacks, pins and the temp count are observed by
    AC3 and AC5 to AC10.
  - The fixture's old leg is now the copy at `40def53f7`.

## 10. Reuse audit

The seam extended is the leg's own build walk and its two in-run caches, `_SUBJ` and `_BC_MEMO`
(`tools/unattended/check-brief-recorded.sh@a78fe6040556:477` and `:491`). This unit persists their
answers across runs through TOOL-dQuietDisk-1's store and coprocess, and adds no store of its own.
`_SUBJ`'s loop also fills the candidate map, with no second read. The key follows the shape
TOOL-dQuietDisk-2 rev-5 gives its sibling leg, so both history legs of the kit key their units the
same way.

The chain build owning the area is dWitnessedBar (Test: gate health). dScopedBuild (Build: the
history-derived exit base) shares the range rule, and TOOL-dUnstuckLanding-17's RANGE mode becomes
key input. No dWitnessedBar unit made this leg incremental. Of its specs, only units 16, 27 and 54
name this file: the waiver ledger read, the wrong-shell refusal and the generated rows' `when`. Its
non-merge commits in `git log 59e882afd..fb6f1a74c` touch the file only for two kit-version mints.
In `fb6f1a74c..8b8b1374c` only the landing merge `fcd824fed` touches it, and only for its kit-version
line.

`python tools/codebase-map/reuse_lookup.py "persist a per-unit history leg outcome keyed by the commits whose tokens name the unit"`
returned name-token neighbours only (`key`, `keys`, `leg`, `units`, `build_commit`). The one real
seam among them, `build_commit`, is called unchanged. No existing seam fits beyond the leg's own
caches and the store this build adds. Recall returned these:

- TOOL-dPolishedVitrine-15's ask on trusting a finished claim that stands at HEAD, which the header
  already states;
- TOOL-dBriefedPass-3's decision on the two-leg pass order;
- this build's spec brief, rev-3 of this spec, and TOOL-dQuietDisk-2's re-grounded spec.

The source agreed with each hit.

Recall terms used: check-brief-recorded build_commit brief row run-state claim retired record history verdict store candidate commits incremental coprocess
