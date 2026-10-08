# TOOL-aLevelledCopy-1 — receipt-sync grades a mismatched row through the target's clean filter

**Status:** OPEN · rev-1 · 2026-10-09 · node a · Tier-2 · base ce9192c0 · streams tooling · order 1 · ratified 2026-10-09

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aLevelledCopy-1-m12-probe.md](../build/2026-10-09-build-TOOL-aLevelledCopy-1-m12-probe.md) | research | — |
| [2026-10-09-prompt-TOOL-aLevelledCopy-1-1-spec-brief.md](../prompts/2026-10-09-prompt-TOOL-aLevelledCopy-1-1-spec-brief.md) | journal | TOOL-aLevelledCopy-2 TOOL-aLevelledCopy-3 DEPL-aLevelledCopy-1 |
| [2026-10-09-prompt-TOOL-aLevelledCopy-1.md](../prompts/2026-10-09-prompt-TOOL-aLevelledCopy-1.md) | research | TOOL-aLevelledCopy-2 TOOL-aLevelledCopy-3 DEPL-aLevelledCopy-1 |

<!-- /gen:spec-records -->

## 1. Goal

The receipt-sync leg hashes an engine row's WORKING-COPY bytes. On a Windows node with
`core.autocrlf=true`, a file whose `eol=lf` pin arrived after checkout keeps a CRLF working copy
that git never rewrites, so the leg reports `DRIFTED` although the committed blob is exactly gov's.
inCMS measured 65 such rows on 2026-10-07 and cleared them only with its pre-gov installer's
re-checkout. This unit makes the leg grade a mismatched row through the target's own clean filter,
the rule `govkit check` already applies, so a CRLF-only working copy is not drift and a real content
edit still reds. The adopters can then retire that installer duty.

## 2. Scope (IN)

- **S1 — the eol-only predicate, batched.** In `tools/run-gates/check-receipt.py`,
  `check_engine_rows` keeps its raw `sha256` compare as the first test. Every row that fails it AND
  carries an `oid` joins one list. After the loop, ONE `git -C <tree> hash-object --stdin-paths`
  spawn receives that list and returns each path's clean-filter oid. A row is `eol-only`, and counts
  as graded and clean, when its clean-filter oid equals the row's `oid` AND the blob oid of its RAW
  bytes is not the row's `oid`. Every other mismatched row is `DRIFTED` exactly as today. A row with
  no `oid`, which is a receipt below schema 3, stays `DRIFTED`. When every row matches raw, nothing
  is spawned. Observed by AC1, AC2, AC5, AC6.
- **S2 — the count is printed.** The `receipt:` summary line and the closing `ok` line each gain
  `eol-only <n>`, as `cmd_check`'s integrity line does, so a green over normalized rows reads
  differently from a green over raw-equal rows. Observed by AC1.
- **S3 — four built-in git arms.** `check_fixtures` gains four arms over temporary git
  repositories, run on every invocation like the six it has. Each asserts that it graded exactly one
  row, so an arm whose git call failed cannot pass by grading nothing. Observed by AC3, AC4.
  - **(a)** `core.autocrlf=true`, the file committed LF, its working copy unlinked and
    re-checked-out so it is CRLF, then an `eol=lf` pin committed after it: graded clean, `eol-only` 1.
  - **(b)** the same copy with one real byte changed: `DRIFTED`.
  - **(c)** `core.autocrlf=false`, no pin, a CRLF copy written by hand: `DRIFTED`.
  - **(d)** the tamper half: LF bytes equal to the committed blob and a wrong `sha256` in the row:
    `DRIFTED`.
- **S4 — git failure is named, never silent.** On the live path, a `hash-object` spawn that fails
  or cannot start leaves every candidate row `DRIFTED` and prints one line naming git's refusal, so
  the red says why the normalization was not consulted. In `check_fixtures`, a git-backed arm on a
  host where git cannot start prints `ARM FAIL` naming that cause. Observed by AC7.
- **S5 — the docstring and the kit README say what the leg now reads.** The module docstring's
  last "does not check" bullet, which calls an eol-filter red "a true reading", is REWRITTEN rather
  than left beside a second answer: a mismatch the target's own clean filter explains is graded
  clean, and what still reds is named (S1, §3). The `check-receipt.py` row of
  `tools/run-gates/README.md` says the same and states no arm count; its typed count is already
  stale, four against six. Observed by AC8.

## 3. Non-goals (OUT)

- **`check-wiring.sh`'s `check_eol` population.** It stays exactly as bounded, report-only under
  `--session`; its own comment says why, and this unit is the root-cause fix that makes widening it
  unnecessary.
- **Any change to `govkit`.** `cmd_check` already grades this case and is the rule ported here.
- **Re-checkout or rewrite of any working copy.** The leg reads; it never repairs.
- **Receipt portability across install machines.** A receipt written on a CRLF box and graded on an
  LF clone reds under every surviving candidate, because there the raw bytes ARE the blob and the
  tamper half fires (§4 Alternatives rejected, case 4). That is a property of what the receipt
  records, not of this comparison.
- **A SHA-256 object-format target.** The raw-bytes blob oid is computed as git's SHA-1 `blob`
  header form, as `govkit`'s `blob_oid` is, so a SHA-256 repository keeps today's reading. Neither
  adopter is one.

### Edges

- **hands-off** external — ONE spelling of the eol-only predicate shared by this leg and
  `govkit check` under the lib parity table (`# >>>` canonical-copy markers). It needs a
  `tools/govkit/govkit.py` write, which §3 excludes and which `DEPL-aLevelledCopy-1` holds in the
  same order group; until it lands, the two spellings are pinned by their own fixture arms. Filed
  as an ask at the close (§8 F1).
- **consumes-from** external — the receipt's `oid` field, which schema 3 writes on every engine
  row. Measured 2026-10-09: 196 of 196 engine rows in inCMS and 190 of 190 in NicoCares carry it.

## 4. Design

### Data model

No receipt field changes. The predicate reads `sha256`, `oid` and `path` from an engine row, the
working file's raw bytes, and one clean-filter oid per candidate path. `check_engine_rows` returns
a third value, the eol-only count; its two callers are `main` and `check_fixtures` in the same file
(verified by `git grep check_engine_rows`, 2026-10-09).

### The predicate, ported

`govkit cmd_check` (`tools/govkit/govkit.py`, the DEPL-aRepatriatedFork-17 S2 block in its
integrity loop) decides a mismatch as follows, and this unit reproduces it clause for clause:

```text
eol-only  <=>  row.oid  and  clean_filter_oid(path) == row.oid  and  blob_oid(raw bytes) != row.oid
```

The third clause is the tamper guard. Where the filter changes nothing, the raw bytes ARE the blob,
so a matching clean oid with a mismatching `sha256` means the RECEIPT is wrong, and that stays red.

The one deliberate difference is the spawn shape. `cmd_check` spawns `hash-object --path=<p>` once
per mismatched row. This leg pipes every candidate to `git -C <tree> hash-object --stdin-paths`,
which applies each path's own attributes and filters and prints one oid per input line, in order.
A spawn costs about 0.75 s on node a (PINNED, measured 2026-10-02, memory note "A git spawn costs
751ms"), so the 65 inCMS rows would cost about 50 s per-row and cost one spawn here. A path
carrying a newline cannot travel on `--stdin-paths`; such a row stays `DRIFTED` and is named, and no
receipt row in either adopter has one.

### Built-in arms

The arms build throwaway repositories under the process's own temporary directory, as the six
existing arms do, and pass `-c core.autocrlf=<value>` and the committer identity on the command
line, so a host's system or global config cannot decide them. They spawn git roughly eighteen
times in total, an estimate of about 14 s per invocation on node a (DERIVED at build time: AC3's
`figure:` line records the measured wall). The leg's declared ceiling is 300 s.

### Files touched (estimate)

- `tools/run-gates/check-receipt.py`
- `tools/run-gates/README.md`

### Rollout

The receipt-sync leg ships in the run-gates kit, so adopters take it with a normal `govkit update`.
The kit-version bump for run-gates happens once, after the last unit of this build, not here. The
codebase map's generated symbol inventory goes stale on a new function; it is regenerated once at
the close, because three units of this build write it and a generated index is a shared mutable
record (BUILD-METHOD M6 clause 3).

### Alternatives rejected

Measured by this build's M12 probe, `build/2026-10-09-build-TOOL-aLevelledCopy-1-m12-probe.md`,
2026-10-09 on node a. Each candidate was graded on the same throwaway repositories.

| Candidate | eol-only copy | real edit | CRLF copy, no filter | Verdict |
|---|---|---|---|---|
| A — clean-filter oid against `oid`, tamper-guarded | GREEN | RED | RED | **ratified** |
| B — `git diff --quiet`, then sha256 of the index blob | GREEN | RED | RED | survives, loses the tie-break |
| C — sha256 of the bytes with CR stripped | GREEN | RED | GREEN | **rejected** |

- **C loses on the no-filter case.** Git would commit those CRLF bytes as they are, so calling them
  gov's is a false green. The test that rejected it is case 3 of the probe.
- **B loses the tie-break, not a test.** Both A and B pass every discriminating case, and case 4, a
  CRLF-box receipt graded on an LF clone, reds under both, so it does not separate them. A reuses the
  seam `cmd_check` already applies (M3 tie-break) and needs one spawn where B needs two, a `diff`
  and a `cat-file`.

## 5. Production-readiness checklist

- security — no new write path. The new spawn is `git hash-object` without `-w`, so it writes no
  object; paths come from the receipt, are passed on stdin and never through a shell.
- perf / scale — one spawn for all mismatched rows and none when every row matches raw. The built-in
  arms add an estimated 14 s per invocation on node a, against a 300 s ceiling.
- error / empty / loading states — git absent or refusing: candidates stay `DRIFTED` with a named
  line (S4). A row with no `oid`: `DRIFTED`, unchanged.
- observability — `eol-only <n>` on the summary and closing lines (S2).
- risks — a narrowed red can hide a real defect only if the clean filter maps an edited file onto
  gov's blob, which is a content change git itself would not commit; AC2 and arm (b) pin that.
- testing — four built-in arms (S3), each with its failing case staged (AC4).
- migration — none. A receipt below schema 3 grades exactly as before.
- user docs — the module docstring and the kit README row (S5).

## 6. Acceptance criteria

- **AC1** — When a fixture repository under a short `%TEMP%` directory holds `core.autocrlf=true`,
  a file committed LF, its CRLF working copy re-checked-out, an `eol=lf` pin committed after it, and
  a receipt row carrying that file's LF `sha256` and LF blob `oid`, the BASE copy of the file,
  read with `git show` at base `ce9192c0` and run as `python <copy> <fixture>`, prints `DRIFTED`
  and exits 1, and `python tools/run-gates/check-receipt.py <fixture>` prints `ok` with
  `eol-only 1` and exits 0. Red when: the fixed file still prints `DRIFTED` for the row, or the
  working copy holds no CR byte, which the fixture script asserts before grading so that a fixture
  that staged nothing cannot pass.
  fixture: built by a script kept in this run's scratchpad; the tree holds none today.
- **AC2** — When one byte of that CRLF working copy is changed, `python
  tools/run-gates/check-receipt.py <fixture>` prints `DRIFTED` for the row and exits 1. Red when:
  the edited copy grades clean.
- **AC3** — When `python tools/run-gates/check-receipt.py --selftest` runs, it prints an
  `ARM ok` line for each of arms (a) to (d) and a `fixtures:` line whose two counts are equal, and
  exits 0. Red when: any arm prints `ARM FAIL`, or an arm graded zero rows.
  figure: the arm total is DERIVED, printed by the file itself; the wall time is measured once and
  recorded in this unit's acceptance ledger.
- **AC4** — When each new arm's failing case is staged in a scratch copy of the file and
  `python <copy> --selftest` runs, the named arm prints `ARM FAIL`: replacing the predicate with a
  CR-stripped sha256 reds arm (c), dropping the raw-blob clause reds arm (d), and dropping the
  clean-filter branch reds arm (a). Red when: a staged break leaves its arm `ok`.
- **AC5** — When a fixture holding three eol-only rows runs under `GIT_TRACE=1`, the trace shows
  exactly one more `hash-object --stdin-paths` invocation than the same command over an all-matching
  receipt. Red when: the difference is three, which is a per-row spawn.
- **AC6** — When the AC1 fixture's row has its `oid` key removed, `python
  tools/run-gates/check-receipt.py <fixture>` prints `DRIFTED` for the row. Red when: a row below
  schema 3 grades clean.
- **AC7** — When the AC1 fixture is copied without its `.git` directory and graded, the row prints
  `DRIFTED` and one line names the failed `hash-object`; and when `--selftest` runs with git absent
  from `PATH`, the git arms print `ARM FAIL` naming that cause and the file exits 1. Red when: either
  run exits 0, or the red names no cause.
- **AC8** — When `grep -c "true reading" tools/run-gates/check-receipt.py` runs, it prints 0, and
  the docstring's rewritten bullet names the clean filter. Red when: the old sentence survives
  beside the new rule.

## 7. Gates

`receipt sync (installed files match the receipt)` · `run-gates adopter e2e` · `lexicon naming predicates` · `memory hygiene`

Every guard the two touched paths trip is broad, so `check-spec-tokens.py --legs-for` owes none.

New arm: tools/run-gates/check-receipt.py · covers AC3 AC4 · each arm's break staged in a scratch copy of the file per AC4 · none

## 8. Open questions

- **F1 — where the eol-only predicate's single spelling lives.** Options: (a) a canonical block in
  `tools/lib/` carried inline by this file and by `govkit.py`'s `cmd_check`, gated by the lib parity
  table; (b) that canonical block with this file as its only copy, `govkit` adopting it later;
  (c) the predicate inline in this file, ported clause for clause, the shared block handed off.
  (a) is vetoed by M3 veto 1: it edits `tools/govkit/govkit.py`, which §3 excludes, and that file is
  `DEPL-aLevelledCopy-1`'s write set in the same order group. (b) and (c) satisfy the same criteria
  and leave the same follow-up; (b) adds a new `tools/lib/` file whose codebase-map coverage is an
  open question, so (c) wins on fewer open questions. RESOLVED (agent, 2026-10-09, delegated): (c),
  with the shared block as the §3 Edges hand-off.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, from the build's spec brief and its M12 probe record.

## 10. Reuse audit

The seam is `govkit cmd_check`'s integrity arm in `tools/govkit/govkit.py`, the
DEPL-aRepatriatedFork-17 S2 block, whose predicate S1 ports clause for clause; recall ranked
`memory/builds/aRepatriatedFork/spec/2026-09-23-spec-DEPL-aRepatriatedFork-17.md` S2 as the binding
record. `python tools/codebase-map/reuse_lookup.py "grade a receipt row through the target's eol
clean filter"` returned no seam that fits: its candidates were name-stem matches on `row` and
`target` (`classify_row`, `derive_graded_rows`, backlog row renderers), none of which grades a
working file. The lib parity table in `tools/lib/resolve-python.test.sh` is the seam for a later
single spelling (§8 F1). Where the probe and source disagreed: the kit README row still says four
built-in arms where the file has six.

Recall terms used: eol-only receipt sha256 oid hash-object clean filter autocrlf integrity check-receipt drifted cmd_check
