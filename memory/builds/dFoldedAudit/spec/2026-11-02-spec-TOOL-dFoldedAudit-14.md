# TOOL-dFoldedAudit-14 — a rotated record keeps its own date floor for the fold cutoff

**Status:** CLOSED · rev-2 · 2026-11-02 · node d · Tier-2 · base f055a11b · streams tooling · order 90 · ratified 2026-11-02

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dFoldedAudit-14-ledger.md](../build/2026-11-02-build-TOOL-dFoldedAudit-14-ledger.md) | journal | — |
| [2026-11-02-build-TOOL-dFoldedAudit-9-1-promotion-notes.md](../build/2026-11-02-build-TOOL-dFoldedAudit-9-1-promotion-notes.md) | research | TOOL-dFoldedAudit-9 TOOL-dFoldedAudit-10 TOOL-dFoldedAudit-11 TOOL-dFoldedAudit-12 TOOL-dFoldedAudit-13 TOOL-dFoldedAudit-15 |
| [2026-11-02-build-TOOL-dFoldedAudit-9-2-spec-stage-returns.md](../build/2026-11-02-build-TOOL-dFoldedAudit-9-2-spec-stage-returns.md) | journal | TOOL-dFoldedAudit-9 TOOL-dFoldedAudit-10 TOOL-dFoldedAudit-11 TOOL-dFoldedAudit-12 TOOL-dFoldedAudit-13 TOOL-dFoldedAudit-15 |
| [2026-11-02-build-TOOL-dFoldedAudit-9-3-cross-read-return.md](../build/2026-11-02-build-TOOL-dFoldedAudit-9-3-cross-read-return.md) | journal | TOOL-dFoldedAudit-9 TOOL-dFoldedAudit-10 TOOL-dFoldedAudit-11 TOOL-dFoldedAudit-13 TOOL-dFoldedAudit-15 |
| [2026-11-02-prompt-TOOL-dFoldedAudit-14-build-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-14-build-brief.md) | research | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-14-spec-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-14-spec-brief.md) | research | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-9-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-9-fix-brief.md) | research | TOOL-dFoldedAudit-9 TOOL-dFoldedAudit-10 TOOL-dFoldedAudit-11 TOOL-dFoldedAudit-12 TOOL-dFoldedAudit-13 TOOL-dFoldedAudit-15 |

<!-- /gen:spec-records -->

## 1. Goal

One record gives one answer to "did this run begin past `SPEC_FOLD_CUTOFF`", through a rotation and
through its first commit, and a stub beside a record cannot move that answer. Today a legal fold row
turns into a permanent red once its record rotates, the same record answers two ways either side of
its first commit, and a stub named like an archive moves a run onto the fold rule. This closes H6, M3
and M5 of `memory/builds/dFoldedAudit/reviews/2026-11-02-review-TOOL-dFoldedAudit-1-2-3-4-5-6-7-8-closing-diff-round1.md`.

## 2. Scope (IN)

- **S1** — `read_first_commit_date` (`tools/unattended/lib-unattended.sh:1731`) takes a third value of
  its second argument, `tenancy`. Under it a rotated path is floored at the newest first touch of a
  sibling `RUN.*.md` that history places before the path's own first touch. No caller outside S2
  passes it, so every other reading keeps today's answer. Observed by AC1, AC2 and AC5.
- **S2** — `check_landed_facts_due` (`tools/unattended/lib-unattended.sh:1755`) takes an optional third
  argument and hands it to that read. `read_spec_exit_rule` (`tools/unattended/unattended.sh:12758`)
  and check 2's `rv_foldpast` read (`tools/unattended/check-unattended.sh:843`) pass `tenancy`, and no
  other caller does. Observed by AC3, AC4 and AC5.
- **S3** — `check_landed_facts_due` answers 0, ahead of its last-commit shortcut, for a path named
  `RUN.md` whose folder holds a staged added `RUN.*.md`. Observed by AC6.
- **S4** — The honest-rotation predicate reaches check 2: `check_honest_rotation`,
  `check_retired_blob`, `read_blob_fact` and `is_terminal` go from `tools/unattended/unattended.sh`
  to `tools/unattended/lib-unattended.sh` with their bodies unchanged. Observed by AC9.
- **S5** — A check 2 clause reds a tracked `RUN.*.md` added on or after `SPEC_FOLD_CUTOFF` that its
  adding commit does not show to be a rotation. It feeds `rv_bad` and adds no `fail` site. Observed
  by AC7, AC8 and AC11.
- **S6** — The comments that state the old claim are corrected: `tools/unattended/lib-unattended.sh:1711-1713`,
  `tools/unattended/check-unattended.sh:838-841` and `tools/unattended/unattended.sh:12747-12750`.
  Observed by AC10.

## 3. Non-goals (OUT)

- `SPEC_FOLD_CUTOFF`'s own source is not touched. Reading it at BASE is M4 of the report, which
  `TOOL-dFoldedAudit-9` owns, so S2 and S5 keep today's working-copy value here.
- The mirror case of M5 stays. A fresh, never-committed `RUN.md`, or a staged rotation, reads as past
  a cutoff that lies in the future, and reads grandfathered if its first commit lands before that
  cutoff. The judged fix does not reach it, and it needs a cutoff dated ahead of the run. Every
  cutoff at or before the first commit gives one answer, which is the case AC6 observes.
- A staged archive keeps today's answer. It has no committed history, so it reads as past the cutoff
  in check 2 until its first commit. The close's bar grades committed records.
- `rv_fc` (`tools/unattended/check-unattended.sh:822`) and the clauses that read it do not move.
- `tools/drift-audit/drift_report.py` does not move. Its port passes no sibling for an archive
  (`tools/drift-audit/drift_report.py:2943`), and `tools/drift-audit/selftest.py:4377` holds it to the
  library's default read, which S1 leaves alone.
- `--preflight`, `--review`'s row and every closing diff review stay as they are. S2's read reaches
  `nr` only on a spec subject (`tools/unattended/check-unattended.sh:886`).
- No verb, no conf key, no policy key and no `--dispatch` or `--close` term is added.

### Edges

- **hands-off** `TOOL-dFoldedAudit-9` — this unit ships at order 90 and that unit at order 130. That
  unit rewrites the two calls S2 changes, onto a per-record cutoff, and each must keep `tenancy`, which
  AC3's arm reds if it does not. It also takes `rv_foldcut` away, so S5 reads `SPEC_FOLD_CUTOFF` itself
  and stays on the working copy.

## 4. Design

Line citations are to the tree at the header's base.

### The date read

`--follow` takes the oldest add along the followed history, so an archive in a folder that rotated
twice dates to the slug's first run (`tools/unattended/lib-unattended.sh:1711-1713`). The floor at
`:1735` applies only to a path named exactly `RUN.md`. For most cutoffs that direction of error is
safe, because grandfathering is the laxer rule. Here it is the stricter one: the old clause reds
a fold row. So the opt-in reaches this cutoff alone, and the other cutoffs keep their grandfathering.

The existing loop serves both floors, because a second `done < <(...)` is a new site for
`tools/gate-lint/sh_hygiene.py`:

```bash
read_first_commit_date() { # record path · [nofloor|tenancy] -> YYYY-MM-DD, or nothing
  local _fd_p="${1:-}" _fd_d _fd_s _fd_h _fd_t _fd_own="" _fd_floor=""
  [ -n "$_fd_p" ] || return 0
  _fd_d=$(GIT log --follow --diff-filter=A --format=%cs -- "$_fd_p" 2>/dev/null | tail -1)
  if [ "${_fd_p##*/}" != RUN.md ] && [ "${2:-}" = tenancy ]; then
    _fd_own=$(GIT log --full-history --format=%H -- "$_fd_p" 2>/dev/null | tail -1)
  fi
  if { [ "${_fd_p##*/}" = RUN.md ] && [ "${2:-}" != nofloor ]; } || [ -n "$_fd_own" ]; then
    while IFS= read -r _fd_s; do
      [ -n "$_fd_s" ] && [ "$_fd_s" != "$_fd_p" ] || continue
      _fd_h=$(GIT log --full-history --format='%H %cs' -- "$_fd_s" 2>/dev/null | tail -1)
      [ -n "$_fd_h" ] || continue
      if [ -n "$_fd_own" ]; then
        [ "${_fd_h%% *}" != "$_fd_own" ] || continue
        GIT merge-base --is-ancestor "${_fd_h%% *}" "$_fd_own" 2>/dev/null || continue
      fi
      _fd_t=${_fd_h#* }
      if [ -z "$_fd_floor" ] || [[ "$_fd_t" > "$_fd_floor" ]]; then _fd_floor=$_fd_t; fi
    done < <(GIT ls-files -- "${_fd_p%/*}/RUN.*.md" 2>/dev/null)
  fi
  if [ -n "$_fd_floor" ] && { [ -z "$_fd_d" ] || [[ "$_fd_floor" > "$_fd_d" ]]; }; then _fd_d=$_fd_floor; fi
  printf '%s' "$_fd_d"
}
```

A live `RUN.md` keeps today's floor, because `_fd_own` stays empty and the self-comparison never
holds for it. "At or before" is read from history and not from `%cs`. Two rotations can land on one
day, `%cs` cannot order them, and a day compare would let the first archive floor itself on the
second. That would read its pre-cutoff run as past the cutoff and red its old-shape rows, the same
permanent red H6 names.

The report's scratch history, as a table:

| Path | Its first touch | `--follow` date | `tenancy` date |
|---|---|---|---|
| first archive | 2026-11-20 | 2026-10-20 | 2026-10-20, no earlier sibling |
| second archive | 2026-11-25 | 2026-10-20 | 2026-11-20, the first archive's first touch |
| live `RUN.md` | n/a | 2026-10-20 | 2026-11-25, today's floor |

`check_landed_facts_due` reads `_ld_d=$(read_first_commit_date "$1" "${3:-}")`, and an empty third
argument is today's call. The shortcut at `tools/unattended/lib-unattended.sh:1758-1759` stands: a
path nothing wrote at or after the cutoff cannot have begun after it.

### The staged rotation

`--preflight` stages the rotation and the spec commit uses `git commit --only`, so `RUN.md` can reach
a spec exit uncommitted. The shortcut then reads the previous tenant's last commit. Ahead of it:

```bash
if [ "${1##*/}" = RUN.md ] \
   && [ -n "$(GIT diff --cached --name-only --diff-filter=A -- "${1%/*}/RUN.*.md" 2>/dev/null)" ]; then
  return 0
fi
```

The spelling is `read_pinned_base`'s (`tools/unattended/unattended.sh:8178`). A staged archive means
the record is a new tenant with no committed history, which is what this function already grades
("nothing that has not been committed yet can predate a cutoff that has"). The branch needs no
opt-in, and no other caller can reach it. `tools/unattended/unattended.sh:7480` runs before the
rotation is staged, and `tools/unattended/check-unattended.sh:2238` needs a `LANDED` or `LANDING`
population, which a new tenant's record is not.

A `--name-status` test for `RUN.md` as added never fires: a staged rotation records `RUN.md` as `M`,
the shape `tools/unattended/unattended.test.sh:2570-2571` already states for a committed one.

### The stub clause

The floor reads an archive's first touch, so a file named like an archive moves the record beside it.
Only a stub whose first touch is on or after the cutoff can carry a record across, so the clause
exempts by cutoff and never by list. That is also what keeps the suites' fixture archives with fake
names green: `tools/unattended/check-unattended.test.sh:249` pins `SPEC_FOLD_CUTOFF="2099-01-01"`.

The clause sits after the loop at `tools/unattended/check-unattended.sh:761-987` and before the
`fail 2` at `:988`, because a stub carries no review row and the loop's first test skips such a file:

```bash
case "$SPEC_FOLD_CUTOFF" in
  [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9])
    for rvf in $(GIT ls-files ":(glob)$M/builds/*/RUN.*.md" 2>/dev/null); do
      rv_add=$(GIT log -1 --diff-filter=A --format='%H %cs' -- "$rvf" 2>/dev/null)
      [ -n "$rv_add" ] || continue
      [[ "${rv_add#* }" < "$SPEC_FOLD_CUTOFF" ]] && continue
      rv_rel=${rvf%/*}/RUN.md
      if ! check_honest_rotation "${rv_add%% *}" "$rv_rel" \
         || [ -z "$(GIT diff-tree --root --no-commit-id --no-renames -r --name-only "${rv_add%% *}" -- "$rv_rel" 2>/dev/null)" ]; then
        rv_bad="$rv_bad
  $rvf (an archive added on or after SPEC_FOLD_CUTOFF that no rotation wrote: its name is not the blob it added, the record it retired was not finished, or its commit left the run-state file alone, and the date floor reads an archive's first touch, so it would move the record beside it across the cutoff)"
      fi
    done ;;
esac
```

It reads the key itself and not `rv_foldcut`, for §3's edge. A blank key is announced at
`tools/unattended/check-unattended.sh:725-727` and a malformed one named at `:756-760`, so the `case`
needs no third arm.

`check_honest_rotation` (`tools/unattended/unattended.sh:8206`) already answers the name and the
retired record, for `read_pinned_base`. It does not test that the adding commit rewrites `RUN.md`, and
a stub beside a `HELD` record passes it, so that test sits here. `check_honest_rotation` keeps its
bytes, so `read_pinned_base` keeps its answer. §8 F1 records why the name is tested against the blob
the commit added and not against the file's current bytes.

**What the clause does not check.** An archive with no add commit is not graded: one still staged, or
a rotation landing inside a merge, which records no add at all
(`tools/unattended/lib-unattended.sh:1718-1719`). A complete hand rotation of a finished record, with
the true blob name and `RUN.md` rewritten, passes. §5 carries that as a closing-review matter. The
key is the working copy's, so a run that blanks it turns the clause off, in its diff.

### The hoist

`tools/unattended/check-unattended.sh` cannot call a driver function, and the library is where the
two already share a predicate (`tools/unattended/lib-unattended.sh:1766`). The moved bodies are
`check_honest_rotation` (`:8206`), `check_retired_blob` (`:8221`), `read_blob_fact` (`:8228`) and
`is_terminal` (`:1121`). Their callees are `GIT` and `extract_run_facts`, both in the library.
`is_terminal` reads `PHASES_TERMINAL`, which the driver sets at `tools/unattended/unattended.sh:868`
and the leg at `tools/unattended/check-unattended.sh:423`, ahead of check 2. None of the four carries a
`fail`, so neither ceiling moves. No suite greps a definition of any of them out of the driver:
`tools/unattended/check-unattended.test.sh:4828` mutates a call inside `verb_preflight`, which stays.

### Inventory

| Minted | Cell | Graded by |
|---|---|---|
| `tenancy` | value of an existing positional argument | S1's arms; `nofloor` is its sibling |
| `rv_add`, `rv_rel`, `_fd_h`, `_fd_own` | variables | none |

No function, verb, flag, conf key or check number is minted.

### Rollout

The clause and the opt-in are dark while `SPEC_FOLD_CUTOFF` is blank, which `.unattended.conf:488`
is until this build's close writes the landing date. Every tracked archive predates that date.

### Files touched (estimate)

- `tools/unattended/lib-unattended.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/check-unattended.test.sh`
- `tools/unattended/unattended.test.sh`

The driver and the leg hold their `KIT_UNATTENDED_VERSION` lines unchanged, as units 1 to 8 did.

### Alternatives rejected

- **A row's own shape selects the rule.** A `folded` row on a pre-cutoff record would stop redding, so
  a hand-appended row grants itself the fold. That is a guard sharing state with what it guards, and
  both skeptics refused it.
- **`tenancy` as the default.** It moves every archive under `LANDED_FACTS_CUTOFF` and into a graded
  set no verb can repair.
- **The floor skips a dishonest sibling, and no gate reds.** The date read would run the honest test
  on every read, for every cutoff, and a stub would stay in the tree unreported. The judged fix reds it.
- **A day compare for "at or before".** The same-day tie above, which AC2 observes.

## 5. Production-readiness checklist

- **security** — No new write path. The clause closes the stub lever. The remaining lever is a run
  able to perform a full rotation of a finished record by hand, which the clause passes and the
  closing review reads in the diff. Spec 7's security line would hold this, and that spec is CLOSED,
  so it is stated here. `SPEC_FOLD_CUTOFF` itself stays a working-copy read for this clause.
- **perf / scale** — `tenancy` adds one `git log` for the path and two calls per sibling, on an
  archive read by check 2 alone. The staged test adds one `git diff --cached` per call: 93 tracked
  `RUN.md` carry a review row, PINNED 2026-11-02, so check 2 adds 93 spawns where it already spends
  several per record, and only under a dated cutoff. The clause adds one `git log` per tracked archive,
  10 PINNED 2026-11-02, and only under a dated cutoff.
- **error / empty / loading states** — A staged archive has no own first touch, so it takes no floor
  and reads as today. A folder with one archive has no eligible sibling.
- **observability** — The clause's line names the path and all three causes. A blank cutoff keeps
  check 2's existing announcement at `tools/unattended/check-unattended.sh:725-727`.
- **risks** — Four function bodies move and two change in the file every driver verb sources. The
  hoist is byte-for-byte, and AC9 and the existing `read_pinned_base` arms hold it. `--follow` needs
  a rename it can detect, so a fixture record needs filler lines, or AC1's no-token read stays at the
  archive's own add and proves nothing.
- **testing** — Fixture repositories with committer dates pinned, true blob names on every honest
  archive, and a green control beside each red. The `second-implementation-is-not-a-second-opinion`
  class stands as check 2 calls the driver's function: the arms pin the answer, not the agreement.
- **migration** — None. No tracked record changes grade: the date read moves only a rotated path in a
  folder with two archives, and no folder holds two today.
- **user docs** — `grep -ln -e 'rotat' help/*.md` prints nothing, so no page moves.

## 6. Acceptance criteria

Fixture T is a scratch git repository at `%TEMP%/fa14t` on branch `main` with no remote and
`core.autocrlf` false, holding a copy of `tools/unattended/` whole, a `.unattended.conf` carrying
`MEMORY_ROOT=memory`, `DISPOSITION_CUTOFF="2000-01-01"`, `REVIEW_ROUNDS="1"` and
`SPEC_FOLD_CUTOFF="2026-11-02"`, and a build `memory/builds/tFix/` with a README carrying a
`gen:build-units` region, as the suites' `mkdisp` writes one. Every `RUN.md` a criterion writes carries
`base:` at the commit holding that conf, as `mkdisp` writes it, because `TOOL-dFoldedAudit-9`, at order
130, reds a spec row on a record with none. Every commit is dated at noon UTC with
`GIT_COMMITTER_DATE`, and every command runs with `GOV_REMOTE` and `GOV_DEFAULT_BRANCH` cleared.
`$D` and `$G` are `bash "$F/tools/unattended/unattended.sh"` and
`bash "$F/tools/unattended/check-unattended.sh"`, run with the fixture as the working directory, and
only their `UNATTENDED check 2` and `check 37` lines are read. `$L` is a subshell that first runs
`. "$F/tools/unattended/lib-unattended.sh"`.

History H: on 2026-10-20 `RUN.md` is added with `phase: LANDED`, a `## Run facts` section and twenty
filler lines no other record carries. On 2026-11-20 it moves to `$A`, named
`RUN.LANDED.<first eight of its blob>.md`, and a new `RUN.md` with `phase: LANDED` is added in the same
commit. On 2026-11-21 that record gains the fold row `2026-11-21T01:00:00Z review · item S1 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED · highs 1 · minors 2 · folded 3 · promoted 0 · disposition fold`.
On 2026-11-25 it moves to `$B`, named the same way, and a new `RUN.md` with `phase: RUNNING` joins it.

- **AC1** — When `$L` runs `read_first_commit_date "$B" tenancy` over H, it prints `2026-11-20`. With no
  second argument it prints `2026-10-20`, and `read_first_commit_date "$A" tenancy` prints `2026-10-20`.
  Red when: `tenancy` is unread, or the floor reaches the first archive.
- **AC2** — When H's last two commits are dated 2026-11-20 as well, `$L` prints `2026-11-20` for `$B`
  and `2026-10-20` for `$A`, each under `tenancy`.
  Red when: the floor compares `%cs` days, so `$A` floors itself on `$B`.
- **AC3** — When `$G` runs over H, it prints no `UNATTENDED check 2 FAILED` line.
  Red when: `rv_foldpast`'s call passes no `tenancy`, which prints both
  `record a terminal row with no highs and minors counts or with disposition fold` and
  `record disposition fold on a row carrying highs and minors`.
- **AC4** — When the fold row sits in the first run's record instead, committed 2026-10-21, so that `$A`
  holds it, `$G` prints `spec subject(s) S1 record a terminal row with no highs and minors counts or with disposition fold`.
  Red when: the floor reaches a first archive, so a record begun before the cutoff takes the fold rule.
- **AC5** — When `$L` runs `check_landed_facts_due "$B" 2026-11-02` over H it returns 1, and with a third
  argument `tenancy` it returns 0. `grep -cE '^[^#]*check_landed_facts_due .*tenancy' tools/unattended/unattended.sh tools/unattended/check-unattended.sh`
  prints 1 for each file.
  Red when: `tenancy` becomes the default, so an archive under `LANDED_FACTS_CUTOFF` leaves the
  grandfathered set.
- **AC6** — When a fixture's `RUN.md` is first committed 2026-10-20 with `phase: LANDED`, then moved to
  a truly named archive and replaced by a `phase: RUNNING` record, staged and uncommitted,
  `$D --review tFix --subject S1 --verdict "CLEAN WITH FIXES" --blockers 0 --highs 1 --minors 2 --folded 3 --promoted 0 --disposition fold`
  exits 0 and `$G` prints no check 2 line. After a commit dated 2026-11-05 the same call on `--subject S2`
  exits 0 and `$G` still prints no check 2 line.
  Red when: the staged branch is absent, so the first call refuses with `--folded and --promoted are counted only`.
- **AC7** — When a fixture's `RUN.md` is first committed 2026-10-20 with `phase: RUNNING`, gains a row
  dated 2026-11-05, and a stub is committed that day, `$G` prints
  `an archive added on or after SPEC_FOLD_CUTOFF that no rotation wrote` naming the stub in each of three
  cases: a stub `RUN.ABORTED.deadbeef.md`; a stub named by its true blob in a commit that rewrites
  `RUN.md`, whose parent record is running; and a stub named by its true blob beside a `phase: HELD`
  record its commit leaves alone.
  Red when: the clause is absent, or the `diff-tree` half is lost, so the third case passes.
- **AC8** — When H stands with `$B` edited in a later commit, as two tracked archives were, `$G` prints no
  check 2 line. When AC7's first stub is dated 2026-10-30, or `SPEC_FOLD_CUTOFF` is blank, `$G` prints no
  line naming it.
  Red when: the name is tested against the file's current bytes, or the clause ignores the cutoff.
- **AC9** — When `grep -cE '^(check_honest_rotation|check_retired_blob|read_blob_fact|is_terminal)\(\) *\{' tools/unattended/lib-unattended.sh tools/unattended/unattended.sh`
  runs, it prints 4 and 0.
  Red when: a definition stays in the driver, or the leg calls a function it cannot reach.
- **AC10** — When `grep -c 'never toward a frozen red' tools/unattended/lib-unattended.sh` runs it prints
  0, and `grep -c tenancy` over `tools/unattended/check-unattended.sh` prints at least 2.
  Red when: the comment at `tools/unattended/lib-unattended.sh:1713` still claims the safe direction
  for every cutoff.
- **AC11** — When `grep -cE '(^|[^a-zA-Z_])fail [0-9]+ "' tools/unattended/unattended.sh tools/unattended/check-unattended.sh`
  runs, it prints 318 and 264.
  figure: PINNED at 2026-11-02 at this spec's base. A unit ahead of this one in order shares a site by
  the same rule, so the figures hold through the build.
  Red when: the clause adds a `fail` site instead of feeding `rv_bad`.
- **AC12** — When a probe at the repo root sets `PHASES_TERMINAL="LANDED ABORTED"`, sources the library,
  and runs S5's two tests over every path `git ls-files 'memory/builds/*/RUN.*.md'` lists, with no date
  test, no path fails.
  figure: DERIVED at observation. It read 10 of 10 on 2026-11-02.
  Red when: a rotation shape the predicate never saw sits in the tree, and the clause would red it
  once the close dates the cutoff.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `routed-commits selftest` · `drift-audit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `kit version markers`

`drift-audit selftest` is named beside the guard join because it sources the library and holds its
port to the default read that S1 must leave alone.

New arm: tools/unattended/check-unattended.test.sh · covers AC1 AC2 AC5 · the twice-rotated folder and its same-day twin read through the library, staged with the `tenancy` branch deleted · `FLOOR_ASSERTIONS` raised by the executed count
New arm: tools/unattended/check-unattended.test.sh · covers AC3 AC4 · H6's left-shift gate, a twice-rotated folder whose archive holds a fold row, staged with `rv_foldpast`'s call passing no `tenancy` · `FLOOR_ASSERTIONS` raised by the executed count
New arm: tools/unattended/check-unattended.test.sh · covers AC7 AC8 · M3's left-shift gate, the three stubs beside their green controls, staged with the clause deleted · `FLOOR_ASSERTIONS` raised by the executed count
New arm: tools/unattended/unattended.test.sh · covers AC6 · M5's left-shift gate, one answer before and after the first commit, staged with the staged branch deleted · `FLOOR_ASSERTIONS` raised by the executed count

## 8. Open questions

- **FACT-QUESTION · F1 — Is an archive's name tested against its current bytes, or against the blob
  its adding commit added?** The judged fix for M3 says "the hash of its own bytes". It is a departure
  from that text, so it is stated here. The probe, read-only: for every path
  `git ls-files 'memory/builds/*/RUN.*.md'` lists, compare the name's eight hex with the blob at HEAD,
  and run `check_honest_rotation` on the commit `git log -1 --diff-filter=A` names.
  The observation, 2026-11-02: 2 of 10 names miss the blob at HEAD, the two `RUN.ABORTED` archives of
  aBoundedVerdict and aDeclaredBound, and 0 of 10 miss the blob their adding commit added. One later
  commit, 710f5a163, edited both. Liveness: the first test printed its negative twice, so the probe
  can produce one.
  - (a) Current bytes, as the judged fix reads. The date scope hides these two, but an archive added
    past the cutoff and edited later reds for good, on a record no verb repairs.
  - (b) The blob the adding commit added, through `check_honest_rotation`, with the judged fix's
    `RUN.md` test beside it. This is also stricter than the judged text, because a true blob name over
    a running record reds, which AC7's second case observes.
  Recommendation: (b). The probe refutes (a) on real records, and (b) reuses a seam M5 found.
  RESOLVED (agent, 2026-11-02, delegated): (b). The name is tested against the blob the adding commit
  added, by `check_honest_rotation`, and the clause tests that commit rewrote `RUN.md`.

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, from the closing review's H6, M3 and M5 and the promotion notes.
- rev-2 · 2026-11-02 · §3 · §6 · The Edges line reads `hands-off` `TOOL-dFoldedAudit-9` so the pair joins,
  and the header gains `ratified` for F1, which stands as written. M2's cross-read: Fixture T's records
  carried no `base:`, which that unit's read refuses once it builds, so this unit's arms would red at
  order 130.

## 10. Reuse audit

The seams are `read_first_commit_date` and `check_landed_facts_due`
(`tools/unattended/lib-unattended.sh:1731`, `:1755`), which both readers already call; the staged test
of `read_pinned_base` (`tools/unattended/unattended.sh:8178`); `check_honest_rotation` and its two
callees (`tools/unattended/unattended.sh:8206-8230`), hoisted and not copied; and `rv_bad`, the check 2
feed (`tools/unattended/check-unattended.sh:737`). `reuse_lookup.py` ranked only dossiers and name-stem
hits for this behaviour and no seam beyond those. Recall returned the closing review's H6 and
`memory/builds/dFoldedAudit/spec/2026-11-01-spec-TOOL-dFoldedAudit-2.md:80`, whose rule this unit keeps.

Where the records and the source disagreed. The report's M3 fix says "its own bytes", and two tracked
archives were edited after rotation (§8 F1). The report's H6 fix says "at or before", which a `%cs`
compare cannot order on one day (§4). The report cites spec 7's security line for M3's residue, and
that spec is CLOSED, so the sentence is §5's here. The report's M5 finding reads "the comment's
`cannot disagree` is false"; after this unit the two agree except in the mirror case §3 states.

Recall terms used: `python tools/memory-recall/query.py "how is a rotated run record dated against a cutoff, and what proves a rotation honest" --terms "rotation archive first-commit floor tenancy grandfathering cutoff follow honest-rotation staged blob8 run-state"`.
Reuse probe used: `python tools/codebase-map/reuse_lookup.py "date a rotated run record by the run that wrote it, floored at the previous rotation"`.
