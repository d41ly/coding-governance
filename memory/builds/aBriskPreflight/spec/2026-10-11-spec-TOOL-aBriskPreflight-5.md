# TOOL-aBriskPreflight-5 — the live-run count reads every record's phase in one pass and derives each record once

**Status:** CLOSED · rev-2 · 2026-10-11 · node a · Tier-1 · base b726385f · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aBriskPreflight-1-baseline.md](../build/2026-10-11-build-TOOL-aBriskPreflight-1-baseline.md) | research | TOOL-aBriskPreflight-1 TOOL-aBriskPreflight-2 TOOL-aBriskPreflight-3 TOOL-aBriskPreflight-4 TOOL-aBriskPreflight-6 TOOL-aBriskPreflight-7 |
| [2026-10-11-build-TOOL-aBriskPreflight-5-walk-ab.md](../build/2026-10-11-build-TOOL-aBriskPreflight-5-walk-ab.md) | research | — |
| [2026-10-11-prompt-TOOL-aBriskPreflight-1-brief.md](../prompts/2026-10-11-prompt-TOOL-aBriskPreflight-1-brief.md) | research | TOOL-aBriskPreflight-1 TOOL-aBriskPreflight-2 TOOL-aBriskPreflight-3 TOOL-aBriskPreflight-4 TOOL-aBriskPreflight-6 TOOL-aBriskPreflight-7 |
| [2026-10-11-prompt-TOOL-aBriskPreflight-5-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aBriskPreflight-5-build-brief.md) | research | — |
| [2026-10-11-prompt-TOOL-aBriskPreflight-5-spec-brief.md](../prompts/2026-10-11-prompt-TOOL-aBriskPreflight-5-spec-brief.md) | research | — |
| [2026-10-12-review-TOOL-aBriskPreflight-1-2-3-4-5-6-7-10-diff-review-round1.md](../reviews/2026-10-12-review-TOOL-aBriskPreflight-1-2-3-4-5-6-7-10-diff-review-round1.md) | diff-review | TOOL-aBriskPreflight-1 TOOL-aBriskPreflight-2 TOOL-aBriskPreflight-3 TOOL-aBriskPreflight-4 TOOL-aBriskPreflight-6 TOOL-aBriskPreflight-7 TOOL-aBriskPreflight-10 |

<!-- /gen:spec-records -->

## 1. Goal

`check_single_live` in `tools/unattended/unattended.sh` calls `read_derived_phase` once for every
tracked run record, and for a LANDING record that one call starts about eight programs. The peer's
trace charges about 306 s of a 1561 s preflight to this walk. The count asks each question once for
the whole population. Every phase it derives and every line it prints stay what they are.

## 2. Scope (IN)

Line numbers are at BASE `b726385f`.

- **S1** — `read_derived_phase` gains a priming form, `read_derived_phase --prime <file>...`. It
  answers the function's sub-questions for the whole population in batched calls and keeps the
  answers in a cache that the per-record form reads. Called with no path, it empties the cache.
  Like the per-record form it prints nothing, never calls `fail`, never touches `status` and returns
  0. The batched read of the `phase` fact sits inside `read_derived_phase`, so check 39 of
  `tools/unattended/check-unattended.sh` still finds every read of that fact inside one of the two
  readers. Observed by AC1 and AC3.
- **S2** — Three sub-answers are cached, each computed once for the population. Observed by AC1,
  AC2, AC4 and AC6.
  - The `phase` and `hold-code` facts of every existing record, by one `awk` that applies `fact`'s
    section scope and value rules.
  - For each record whose phase is LANDING, or HELD under a code `check_handoff_code` admits, its
    landing commit: one `git diff --name-only HEAD` over those records, `check_lease_only_diff`
    for each record that call lists, and one `git log -1 --format=%H HEAD` per remaining record
    inside one subshell.
  - Each landing commit's ancestry against the advertised tip, by one `git rev-list` over all of
    them excluding that tip.
- **S3** — The per-record form takes each sub-answer from the cache when the cache holds it, and
  computes it exactly as today when it does not. A batched call that fails therefore leaves its
  answers uncached, and the records it covered take the old reading and nothing else. Observed by
  AC1 and AC3.
- **S4** — `check_single_live` (`tools/unattended/unattended.sh:2927`) collects its population once,
  with the same `GIT ls-files` call and the same own-slug skip, primes the cache with it, walks it,
  and announces exactly as today. It then empties the cache before its claims block, so no reader
  later in the same preflight takes an answer derived before a write. Observed by AC2 and AC5.
- **S5** — `tools/unattended/unattended.test.sh` gains one arm beside its derived-LANDED driver
  block: a record committed at RUNNING and pushed, whose working copy alone reads LANDING, still counts live; and a
  LANDING record staged and never committed still counts live. Observed by AC6.

## 3. Non-goals (OUT)

- Converting `fact`, `runmd_of` or `readme_of` to fork-free readers, which is aSparedSpawn-8 S1. That
  unit converts every `$(fact …)` site and keeps the `fact <file> <key>` spelling check 39 reads.
  This unit adds no `$(fact …)` site and keeps the one in `read_derived_phase`, now its uncached
  branch, so S1 converts it where it stands. The batched `awk` is not `fact` and is no reader S1
  lists, so S1 neither needs it nor breaks it. If both units edit that one line, whoever lands second
  keeps the other's spelling inside the uncached branch.
- The gate leg's own walk in `tools/unattended/check-unattended.sh`. Its check 7 reads
  `read_landing_commit` from `tools/unattended/lib-unattended.sh`, which this unit leaves as it is,
  so the leg and preflight still agree about one record.
- `read_derived_phase`'s other callers. None of them primes, so none of them ever reads the cache.
- The `fact … abandoned`, `fact … work-landed-at` and `fact … witness` reads in `check_single_live`.
  They run per counted record, two or three at writing, and S1 of aSparedSpawn-8 converts them.
- The unattended kit's version marker, which the build moves once after the kit's last move.

## 4. Design

### Why a cache inside the reader, and not a second reader

`read_derived_phase` is "the leg's reading too, so preflight and the bar agree about one record"
(`tools/unattended/unattended.sh:2936`). A second function that derived phases in bulk would be two
answers to one question, the class `gotchas.py` selects for this path. With the cache, the
derivation itself stays one block of code: the per-record logic at
`tools/unattended/unattended.sh:1272-1298` is unchanged except that each of its three sub-questions
reads the cache first. Equality then rests on three narrow arguments, each stated below and each
observed by AC1 over the real population.

### The cache

Associative arrays declared beside `DP_PHASE` at `tools/unattended/unattended.sh:1271`. The driver
already uses `declare -A`, so bash 4 is already its floor. Presence is tested with `${X[$k]+x}`, so
a cached empty answer is told apart from no answer.

| Array | Key | Value |
|---|---|---|
| `DPC_PHASE` | record path | the `phase` fact as `fact` reads it |
| `DPC_HOLD` | record path | the `hold-code` fact as `fact` reads it |
| `DPC_LANDING` | record path | the landing commit, or empty where `read_landing_commit` returns 1 |
| `DPC_ANC` | commit | 1 when the commit is an ancestor of `ADVQ_SHA`, else 0 |

### Equality 1: the `awk` reads what `fact` reads

`fact` (`tools/unattended/unattended.sh:1217-1232`) strips one trailing CR from each line, enters
the section on a line beginning `## Run facts`, leaves it on any other line beginning `## `, and
takes the first section line beginning `<key>:`, with leading spaces and only spaces stripped. The
`awk` runs under `LC_ALL=C` over the records `[ -f ]` admits, applies the same four rules for both
keys at once, and prints `path`, `phase` and `hold-code` separated by the byte 0x1F. The shell reads
it with `IFS=$'\037'`. 0x1F is not IFS whitespace, so an empty field stays a field; the
`empty-field-collapses-unless-it-is-last` gotcha is the tab-separated form of this read. The `awk`
output is captured into a variable, split into rows by `mapfile`, and each row is read with one
`read`: no loop is fed by a here-string over that variable, the form the shell-hygiene leg bans one
assignment away. A non-zero `awk` exit caches nothing.
A path `[ -f ]` refuses is not cached, and the per-record form reads it as today.

### Equality 2: the cached landing commit is the one `read_landing_commit` returns

`read_landing_commit` (`tools/unattended/lib-unattended.sh:1565-1578`) answers in three steps:
`check_lease_only_diff`; HEAD's copy reads LANDING, or HELD under a listed hand-off code; then
`git log -1` names the commit. The batch answers each step as follows.

- **The lease-only diff.** `git diff --name-only HEAD` lists a record exactly when
  `git diff -U0 HEAD` prints something for it, because both run the same change detection. A
  record it does not list therefore passes `check_lease_only_diff` trivially. A record it does list
  is handed to `check_lease_only_diff` itself, unchanged. The listing is not `-z`: a NUL stream
  cannot ride the variable the call is captured into. Without it git quotes a path by
  `core.quotePath` exactly as the caller's `ls-files` does, so a listed path and its `ls-files` key
  are one spelling, and a path git quotes fails `[ -f ]` and was never cached. The driver runs from
  the work-tree root (`tools/unattended/unattended.sh:480`), so the listed paths and the `ls-files`
  paths share one root.
- **HEAD's phase.** When the lease-only diff passes, every line that differs is one of the seven
  lease-fact lines. The `phase` and `hold-code` lines and every `## ` heading are therefore the same
  bytes in HEAD's copy and the working copy, so HEAD's phase is the cached phase and no `git show` is
  needed. One spelling differs between the two readers. The library's `tr -d '\r'` deletes every CR
  in the value, while `fact` strips one trailing CR. The per-record form gates on the working copy's
  `fact` reading before it calls the library at all, so a value carrying a stray CR never reaches
  this step in either form.
- **The commit.** One `git log -1 --format=%H HEAD -- <path>` per record, the library's own command,
  all inside one subshell, with each answer keyed to its path. An empty answer is cached as empty,
  as `[ -n "$_lc_c" ] || return 1` reads it.

If the `git diff` call fails, nothing is cached for any record it covered.

### Equality 3: the rev-list exclusion is the ancestry test

`git rev-list C1 … Cn ^T` prints every commit reachable from a candidate and not from `T`.
A candidate is an ancestor of `T`, `T` itself included, exactly when it is absent from that output,
which is the question `git merge-base --is-ancestor C T` answers. The call goes through `GIT`, so the
replace and graft pins are the ones the per-record call carries. It runs only when at least one
cached landing commit is non-empty, and only after `read_advertised_tip` succeeded. That is the
condition under which the per-record form observes the remote, so a preflight with no landed record
makes no observation it did not make before. If `rev-list` fails, nothing is cached, and each record
takes its own `merge-base` call as today.

### Spawn arithmetic, DERIVED from the population at observation time

| Per record | Before | After |
|---|---|---|
| any record | one fork for `$(fact … phase)` | none; one `awk` for the whole population |
| LANDING or hand-off HELD | `git diff`, the five-program `git show` pipeline, `git log`, `git merge-base`, about eight programs (thirteen for a hand-off HELD) | one `git log`; one `git diff` and one `git rev-list` for the whole population |
| counted live, at the announcement | the whole derivation again | none |

The tree held 88 records at writing, 17 LANDING and one HELD under `owner-decision`, read by a census
`awk` with `fact`'s rules on 2026-10-11.

### Inventory

A `--prime` form of the existing `read_derived_phase`, and four cache arrays, `DPC_PHASE`, `DPC_HOLD`,
`DPC_LANDING` and `DPC_ANC`. No new function, so the lexicon's `sh.function` cell grades nothing new
and `memory/map/generated/symbols.json` does not move.

### Hazards this path carries

- `two-answers-to-one-question`, answered by the cache design above.
- `staged-break-substitutes-a-synthetic-value`: each staged break in §5 mutates the batched step
  under test, never a fixture constant.
- `decision-re-derived-by-a-second-process`: the cache lives in the driver's own process and is
  emptied before anything in that process writes a record.
- Check 39 tracks the enclosing function by a column-0 `name()` line. The embedded `awk` program is
  indented, so no line of it opens a function in that tracker's eyes and every line stays attributed
  to `read_derived_phase`.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` ·
`memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-5-walk-probe.sh` ·
`memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-5-walk-ab.md`

### Alternatives rejected

- **One `git log` over every LANDING path at once.** With several paths, git simplifies history
  against the union pathspec, so a merge that is TREESAME to one parent for one record's path is
  walked on both sides. The newest commit listing that path can then be one that
  `git log -1 -- <path>` prunes. A merge that resolved a record's conflict is not listed by
  `--name-only` at all. Either way DP_LANDING would move, and the EXCLUDED line prints it.
- **`git last-modified`**, which answers every path's last commit in one process. It is recent and
  marked experimental, and adopting it raises the kit's git floor, which is veto 2.
- **Emulating per-path simplification over one `git log --parents --raw -m` stream.** This is a
  second implementation of git's own walk order, date ties and clock skew included, and no
  observation of today's tree proves it equal on a tree not yet written.
- **Reading HEAD's copies through one `git cat-file --batch`.** It is exact, but it re-implements the
  library's section reader over a byte stream, where Equality 2 shows the read is unnecessary once the
  lease-only diff passes.
- **A batched function beside `read_derived_phase`.** Its `awk` reads the `phase` fact, and check 39's
  predicate does not recognise an `awk` spelling, so it would be a third reader that the leg's
  structural arm cannot see.

## 5. Acceptance criteria

- **AC1** — When `2026-10-11-build-TOOL-aBriskPreflight-5-walk-probe.sh` runs in `--fields` mode
  against the built `tools/unattended/unattended.sh`, at the pass commit with `AREF` and `ASHA`
  taken from `origin/main` so no network is read, it derives every tracked run record twice:
  unprimed, then primed. It compares `DP_PHASE`, `DP_LANDING`, `DP_AREF`, `DP_TIP`, `DP_REASON` and
  `DP_BY` field by field and prints `records=<N> landing=<L> held=<H> differences=0`.
  Red when: `differences` is not 0; `records` differs from the count `git ls-files` gives for the
  two run-record globs; or `landing` is 0, which would be a probe that never exercised a derivation.
  figure: DERIVED. N, L and H are counted at observation time: 88, 17 and 1 at writing.
- **AC2** — When the probe runs in `--walk` mode once against BASE's driver (`git show` of
  `b726385f` written to the scratch dir) and once against the built one, the two stdouts of
  `check_single_live` are byte-identical and carry at least one `EXCLUDED` line, and the built run
  ends with `cache=0`.
  Red when: a line differs; no `EXCLUDED` line appears, so the LANDED branch went unexercised; or the
  cache is non-empty after the walk, which leaves a stale answer for a later reader.
- **AC3** — When the probe runs in `--fields --fail-batch` mode, which shadows `GIT` so the batched
  `git diff --name-only` and `git rev-list` exit 128, it still prints `differences=0`.
  Red when: a failed batched call caches an answer, empty or not, instead of leaving the record to
  the old reading.
- **AC4** — When `2026-10-11-build-TOOL-aBriskPreflight-1-run-traced.sh` traces the probe's `--walk`
  mode against BASE's driver and then the built one, and
  `memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-1-trace-spawns.py` reads
  each trace, `execs` falls by at least 6 × L − 3 and `forks` by at least N − 6, with L and N taken
  from AC1's line. Both rows, and a host-state line beside each, go to the result record.
  Red when: a per-record program survives the batch, which holds `execs` within a few of BASE's.
  figure: DERIVED from AC1's N and L.
- **AC5** — When the derived-LANDED driver block of the unattended suite runs as a sliced arm
  against the built driver, a LANDING record whose landing commit is not on the tip prints
  `1 concurrent unattended run(s)` and no `EXCLUDED` line for it, and once pushed it prints
  `EXCLUDED`. With the cached ancestry forced to 1 as a staged break, the first assertion fails.
  Restored, both pass.
  Red when: the staged break leaves the first assertion passing.
- **AC6** — When S5's arm runs as a sliced arm against the built driver, a record committed at
  RUNNING and pushed, whose working copy alone reads `phase: LANDING`, is listed under
  `concurrent unattended run(s)` with `phase LANDING` and is not `EXCLUDED`. A LANDING record staged
  and never committed is listed the same way. With the `git diff --name-only` result ignored as a
  staged break, the first record prints `EXCLUDED` and the arm fails. Restored, it passes.
  Red when: the staged break leaves the arm passing, so the arm never read the lease-only gate.
- **AC7** — When the lines calling `read_derived_phase` outside `read_derived_phase` and
  `check_single_live` are listed with `grep -n` at BASE and at the pass commit, and their text is
  compared without line numbers, the two lists are identical.
  Red when: another caller's call changed, which this unit never needs.
- **AC8** — When `python tools/codebase-map/gen_map.py --check` runs at the pass commit, it exits 0.
  Red when: the pass minted a function or left an untracked slice script under `tools/`.

## 6. Gates

`unattended kit gate` · `shell hygiene (a loop fed by a command substitution)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC6 · a record committed at RUNNING and pushed whose working copy alone reads LANDING · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-11 · initial draft.
- rev-2 · 2026-10-11 · S2 and §4 Equalities 1 and 2, the build pass: the `git diff --name-only` listing drops `-z`, because a NUL
  stream cannot ride a captured variable and the unquoted listing spells each path as `ls-files`
  does; the `awk` rows are read through `mapfile` and one `read` each, since a loop fed by a
  here-string over the captured variable is the shape the shell-hygiene leg refuses; a failed `awk`
  caches nothing. Every site the spec names was re-located after the mid-build merge and none moved.

## 9. Reuse audit

`tools/codebase-map/reuse_lookup.py "derive the phase of many run-state records in one pass and test
commit ancestry against one tip"` returned name-stem neighbours, among them `read_landing_commit`,
`extract_run_facts` and `read_run_commits` in `tools/unattended/lib-unattended.sh`. None batches a
derivation. The seams this unit extends are `read_derived_phase` itself and
`read_advertised_tip`'s once-per-process observation, which the prime reuses unchanged. One idiom is
copied: `read_files_touched` already reads many paths through one `GIT show`
(`tools/unattended/unattended.sh:3018`). The landing-commit step keeps one `git log` per record
because no batched form is exact; §4 records each rejected candidate and the reason it lost. The
recall probe returned `TOOL-dDerivedDocket-22`, whose call-site table is the source of "preflight and
the leg must agree about one record", and `TOOL-dUnstuckLanding-4` and `-14`, the HELD hand-off
derivation S2 caches.

Recall terms used: `python tools/memory-recall/query.py "how does the live-run count derive LANDED
for a LANDING record and why must preflight and the leg agree" --terms "read_derived_phase
check_single_live LANDING derived LANDED landing commit advertised tip check 7 fails closed live-run
count read_landing_commit"`
