# TOOL-aTrimmedHook-6 — the hygiene-side minors of the closing review, batched

**Status:** CLOSED · rev-1 · 2026-10-11 · node a · Tier-2 · base b726385f · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aTrimmedHook-6-1-acceptance-ledger.md](../build/2026-10-11-build-TOOL-aTrimmedHook-6-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-prompt-TOOL-aTrimmedHook-6-1-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aTrimmedHook-6-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing review's mediums M1 and M2 and lows L3 and L4, the four that land in the hygiene leg and
its self-test. Two are wrong skips a commit can cause: a staged edit to `legacy-files.txt` or the conf
no longer grades names, and a staged rename of a grandfathered path no longer runs the stale-line
guard. Two are missing arms. The batch closes all four.

## 2. Scope (IN)

All in `tools/memory-tree/check-memory-hygiene.sh` and its self-test.

- **S1 — M1, the name checks' other inputs.** The staged set is read over the memory root AND
  `.memory-tree.conf` in the same one `git diff`, the conf kept out of `STAGED_MD`. When
  `memory/project/legacy-files.txt` or the conf is staged, `FILES` is the whole listing and checks 1, 3,
  4 and 5 run over it, because the grandfather list and the conf decide which names pass. The comment's
  premise is corrected. Observed by AC1.
- **S2 — M2, a renamed listed path.** The `git diff` carries `-M`, so an adopter with
  `diff.renames=false` still sees an `R` row. A staged rename whose SOURCE path is in the legacy or
  curation-debt registry arms the stale-line guard as a staged list does, and the guard's comment no
  longer claims only a deletion can make a line stale. Observed by AC2.
- **S3 — L3, the check 9 relay.** The SKIPPED relay matches per line, not as a prefix of the merged
  output, and two self-test arms observe it: a no-id edit to a non-structural memory file prints
  `check 9: render SKIPPED`, and a line citing a new id in that file prints no skip. Observed by AC3.
- **S4 — L4, a rename through the parse.** A self-test arm moves a correctly named recording file to
  a malformed name and expects check 5 to name the NEW path. Observed by AC4.

## 3. Non-goals (OUT)

- **N1** — no change to the full run (`STAGED=0`).
- **N2** — the generator and manifest-check minors are TOOL-aTrimmedHook-7's.
- **N3** — a staged DELETION is still graded by nothing under `--staged`, as at BASE.

### Edges

none

## 4. Design

S1 reads the conf in the same call because `.githooks/pre-commit` reaches this leg only when
`memory/**` is staged, so the conf matters exactly when it is staged beside memory. Grading the whole
listing on those commits is the BASE behavior for them, and they are rare. S2's lookup reads
`LEGACY_SET` and `DEBT_SET`, which are built before the parse, so it costs no process. S3 replaces the
`case` over the whole capture with a loop over its lines, so a warning printed first no longer hides the
skip line.

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`

### Rollout

Order 3, disjoint from units 5 and 8's files. Arms are observed through a slice of the self-test, as
TOOL-aTrimmedHook-2's were, and the floor rises by what is added.

### Alternatives rejected

- **Grade only the paths whose legacy rows were removed.** Precise, but it needs a HEAD-versus-index
  diff of the list; the whole listing on a rare commit is simpler and is what BASE did.

## 5. Production-readiness checklist

- security — N/A — selection logic of a local gate.
- perf / scale — a commit staging the legacy list or the conf pays the whole-listing name checks.
- error / empty / loading states — unchanged.
- observability — the S3 relay is now observed by an arm.
- risks — none beyond the whole-listing cost on rare commits.
- testing — AC1 to AC4 are self-test arms run through a slice.
- migration — none.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `check-memory-hygiene.sh --staged` runs in the self-test's fixture tree and the arm
  stages only a `legacy-files.txt` edit dropping the row for a committed free-named recording file,
  check 5 names that file.
  Red when: it prints the no-new-name line and reports nothing.
- **AC2** — When `check-memory-hygiene.sh --staged` runs in that fixture tree and the arm stages a
  `git mv` of a legacy-listed file to a conforming name, the stale-line guard reports the old path.
  Red when: the guard prints HELD.
- **AC3** — When `check-memory-hygiene.sh --staged` runs in that fixture tree with a no-id edit staged
  to a non-structural memory file, it prints `check 9: render SKIPPED`; with a line citing a new id
  staged instead, it prints no such line.
  Red when: either expectation fails.
- **AC4** — When `check-memory-hygiene.sh --staged` runs in that fixture tree and the arm stages a
  `git mv` of a correctly named recording file to a malformed name, check 5 names the new path.
  Red when: check 5 names the old path or nothing.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `harness arms (fail branches armed or pinned)` · `check-arms selftest`

New arm: tools/memory-tree/check-memory-hygiene.test.sh staged minors · covers AC1 AC2 AC3 AC4 · the legacy and conf trigger removed, the rename lookup removed, the relay matched as a prefix · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, promoted from the closing review's M1, M2, L3 and L4.

## 10. Reuse audit

No new mechanism: the unit reuses the leg's `LEGACY_SET`, `DEBT_SET` and `STAGED_SET` lookups and its
HELD convention, all extended by TOOL-aTrimmedHook-2. `python tools/codebase-map/reuse_lookup.py
"narrow the hygiene file list to the staged set"` returned only name-stem matches.

Recall terms used: staged pre-commit hygiene check 9 gen_build_index fork spawn cost manifest-check C6 commit-msg check-commit
