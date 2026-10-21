# TOOL-dTrueNorth-19 — the audit-writer reader takes one glob pathspec, refuses a failed git call, and grades a record whose harness is missing

**Status:** OPEN · rev-1 · 2026-10-21 · node d · Tier-2 · base 271aa59d · streams tooling · order 4

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-21-build-TOOL-dTrueNorth-19-deviation-18.md](../build/2026-10-21-build-TOOL-dTrueNorth-19-deviation-18.md) | deviation | — |
| [2026-10-21-prompt-TOOL-dTrueNorth-19-build-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-19-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dTrueNorth/reviews/2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md`)
confirmed finding **id 38 at HIGH**, its item **H3**. `TOOL-dTrueNorth-14` S1 puts every graded
`spec-audit` record's path on one `git log … -- <rels>` command line, which nothing bounds; the
audit's probe raised `[WinError 206]` at 509 paths of about 69 characters, and tracked review paths
average about 98 bytes, so the cap falls near 330 graded records, a few months of growth on the
primary platform. A failed spawn is unspecified, so `cmd_print_bindings` would raise and check 21
would fail for everyone with no named reason; and a harness blob missing at the adding commit would
read as text lacking `renderAuditBinding`, exempting its record. This unit takes the skeptic's
corrected fix. It repairs `TOOL-dTrueNorth-14`.

## 2. Scope (IN)

- **S1** — The adding-commit read in `derive_audit_writers` is one spawn whose argv does not grow
  with the population: `git log --no-renames --diff-filter=A --reverse --format=%x00%H --name-only --
  ':(glob)<MEMORY_ROOT>/builds/*/reviews/**'`, `<MEMORY_ROOT>` the conf's value. Python keeps the
  first add each graded path shows, its oldest, and ignores every other path. This supersedes
  `TOOL-dTrueNorth-14` S1's `-- <rels>` and states its tie-break for a record added twice.
  Observed by AC1 and AC2.
- **S2** — A git call that fails, the log or the `cat-file --batch` read, by a non-zero exit or an
  `OSError` at the spawn, raises `Problem` naming the command and git's first stderr line, so
  `--print-bindings` exits 2. It never yields an empty exempt set and never exempts a record.
  Observed by AC3.
- **S3** — Deny by default on the harness read: a record whose adding commit's `cat-file` answer is
  `missing`, or not a blob, is graded. Only a present blob whose text lacks `renderAuditBinding`
  exempts its record. This supersedes `TOOL-dTrueNorth-14` S1's "a record whose harness text lacks
  `renderAuditBinding`" for the absent case. Observed by AC4.

## 3. Non-goals (OUT)

- The harness path's spelling in the `<sha>:<path>` request, the repo-relative POSIX form the
  resolver's absolute result must become: the round-2 audit's id 12, which shares S3's fail-open half
  and is batched into `TOOL-dTrueNorth-20`.
- Lifting the adding-commit reader into `tools/memory-tree/tree_lib.py` for the deviation join's
  ported arm too: id 18, in `TOOL-dTrueNorth-20`.
- The `Q` row's four fields and check 21's line, `TOOL-dTrueNorth-14` S2 and S3, unchanged.
- A bug-class checklist entry for an unbounded argv, the finding's left-shift: AC1 is the arm that
  would have caught this instance, and the class has its gotcha record once the close left-shifts it.
- This unit's own departure record: the close writes one for each member recorded by nobody
  (README build-level rule 4).

### Edges

- **consumes-from** `TOOL-dTrueNorth-14` — `derive_audit_writers`, its harness read and the exempt set `cmd_print_bindings` reads; without it there is no reader to bound
- **hands-off** `TOOL-dTrueNorth-20` — S1's reader, which that unit lifts into `tree_lib.py` (id 18), and S3's harness read, whose request path it makes repo-relative POSIX (id 12)

## 4. Design

### Evidence

- The audit's probe: 281 synthetic 69-character paths gave rc 0 and 509 raised `[WinError 206] The
  filename or extension is too long` (the record, id 38's row).
- `git log --no-renames --diff-filter=A --reverse --format=%x00%H --name-only -- ':(glob)memory/builds/*/reviews/**'`
  ran at base in under a second and listed 167 spec-audit adds against the 162
  `git ls-files 'memory/builds/*/reviews/*spec-audit*'` tracks, so a path is added more than once and
  the filter must keep one: PINNED, measured 2026-10-21.
- `run()` (`tools/memory-tree/gen_build_index.py:248-252`) passes `check=True`, so a failed call
  raises `CalledProcessError` rather than `Problem`, and `main` turns only `Problem` into exit 2.
- `read_blobs_at_rev` (`:2934-2970`) maps a `missing` header to `None`, the value S3 grades.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`

### Alternatives rejected

- **Batching the paths into argv chunks.** It bounds each spawn and still grows the spawn count with
  the population, and the chunk size is a platform guess.
- **Exempting on a missing blob, as written.** It fails open, which is the defect the pin exists to
  remove.

## 5. Production-readiness checklist

- security — no new surface; the same two read-only git calls, one of them now constant in argv.
- perf / scale — one log over the reviews folders whatever the record count, filtered in memory;
  at base 167 adds.
- error / empty / loading states — no graded record makes no call, as `TOOL-dTrueNorth-14` S1 says; a
  failed call is exit 2 with its reason; a missing blob grades.
- observability — the `Problem` names the git command and its stderr line.
- risks — a record re-added after a delete keeps its oldest add, so a branch that re-adds an old
  record under a new harness is graded by the old one; the record's bytes are the same file.
- testing — AC1 to AC4 as probes of a fixture repository; the arm under §7, observed at the close.
- migration — none.
- user docs — the function's docstring; no page under `help/`.

## 6. Acceptance criteria

- **AC1** — When a probe builds a fixture git repository under `%TEMP%` whose one commit adds 601
  unpinned `spec-audit` records under `memory/builds/<slug>/reviews/`, each path at least 98 bytes,
  beside a fixture harness carrying `renderAuditBinding`, and calls `cmd_print_bindings` in-process,
  it returns without `OSError` and prints 601 `P` rows and a `Q` row whose exempt field is 0.
  Red when: the record paths go on argv, which raises `[WinError 206]` past about 330 on Windows.
  cost: seconds, for 601 small files and one commit.
  fixture: a fixture repository under a short `%TEMP%` path; the tree holds none.
- **AC2** — When the same fixture deletes one record on a branch and re-adds it in a later commit, the
  probe's `derive_audit_writers` keys that record to its first adding commit.
  Red when: the re-add's commit is read, so the tie-break is the newest.
- **AC3** — When the probe runs `cmd_print_bindings` in that fixture with `git` resolving to a stub
  that exits 128 on `log`, it raises `Problem` naming `git log` and the stub's stderr line, and
  `python3 tools/memory-tree/gen_build_index.py --print-bindings` there exits 2.
  Red when: the failure becomes an empty exempt set, or a traceback.
- **AC4** — When the fixture's harness file is absent at a record's adding commit, the call prints a
  `P` row for that record.
  Red when: an absent blob reads as text lacking `renderAuditBinding` and exempts the record.

## 7. Gates

`build-index selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gen_build_index.py (its selftest) · covers AC1 AC2 AC3 AC4 · 601 long record paths, a re-added record, a failing git and an absent harness, each staged against the base reader that passes the paths as argv and exempts an absent blob · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join of
  `TOOL-dTrueNorth-2` reds a chain spec carrying nothing and derived from nothing. (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, the owner's ruling that a run carries the units it adds (ER:320).
  (b) None. (c) A `part k/n` carry of the repaired unit's clause. (b) reds `unbound` and (c) reds
  `parts`; veto 1 discards both. Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-21,
  delegated): (a). widens: none · relaxes: none
- **F2 — Oldest or newest add for a record added twice?** (a) Oldest, the `scan_spec_adds` shape the
  round-2 audit's id 18 names as the one reader. (b) Newest. (b) would leave id 18's lift two
  tie-breaks to reconcile. Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-21, delegated): (a).
  widens: none · relaxes: none
- **F3 — Does the build's grant lift veto 2 for the generator edit here?** `cl-dClosedLoop-0005`
  names the pin and its grading, and this unit bounds the grader's read. RESOLVED (agent, 2026-10-21,
  delegated): lifted by `PLAY-dClosedLoop-3`, rung 3. grants: PLAY-dClosedLoop-3 the audit-pin arm's
  writer read cl-dClosedLoop-0005 names · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-21 · initial draft, promoted from the round-2 spec audit's id 38 (HIGH, item H3).

## 10. Reuse audit

Probe: `python tools/codebase-map/reuse_lookup.py "list added files by a glob pathspec instead of
argv paths"` ranked `add_health_event`, `add_scratch_worktree`, `corpus_files` and `read_id_list` by
name stem, none an adding-commit reader. The seams that fit are `migrate_backlog.scan_spec_adds`
(`tools/memory-tree/migrate_backlog.py:408`), the oldest-add `--reverse` shape S1 follows, and
`read_blobs_at_rev` (`tools/memory-tree/gen_build_index.py:2934`) for the batch read; the probe did
not surface either, found by reading source.

Recall terms used: `python tools/memory-recall/query.py "how does a spec audit's promoted repair unit
close a defect a pass before it would hit" --terms "spec-audit promoted unit repairs order transition
re-render as-built view argv pathspec supersedes amends"`
