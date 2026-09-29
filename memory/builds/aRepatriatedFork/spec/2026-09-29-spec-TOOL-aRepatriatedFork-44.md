# TOOL-aRepatriatedFork-44 — the adopter-ic receipt fixture carries no adopter name

**Status:** SPECCED · rev-1 · 2026-09-29 · node a · Tier-1 · base d6e1749c · streams tooling · order 7

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aRepatriatedFork-35` scrubbed inCMS's name from gov's shipped files as `adopter ic` and kept
the frozen receipt's filename, `tools/govkit/fixtures/incms-2cff5855.receipt.json`, because no
shipped file named it. `TOOL-aRepatriatedFork-23` widens the install-prefix ledger to row that
fixture by path, and the ledger ships, so `govkit.py selfcheck` arm 10 would refuse it. The fixture
takes the neutral name, and every reader follows.

## 2. Scope (IN)

- **S1** — `git mv` the fixture to `tools/govkit/fixtures/adopter-ic-2cff5855.receipt.json`, the
  registry key `ic` that `TOOL-aRepatriatedFork-35` §8 F1 gave inCMS. Its bytes do not move: the
  blob is a record of what a real install wrote. Observed by AC1.
- **S2** — Every reader outside `memory/` names the new path: the generator's `--out` default in
  `tools/govkit/fixtures/make_adopter_receipt.py`, the S13 arms of `tools/govkit/selftest.py`, and
  the four rows of `tools/dead-path-waivers.txt` keyed on the fixture. Observed by AC1, AC2, AC3.

## 3. Non-goals (OUT)

- The receipt's contents, which stay frozen, and the provenance prose in the two govkit readers,
  which no descriptor ships.
- Gov's records under `memory/` that cite the old path. They are records of a moment;
  `tools/check-dead-paths.sh` excludes `memory/` and hygiene check 15 does not grade them.

### Edges

- **hands-off** `TOOL-aRepatriatedFork-23` — its widened ledger `tools/install-prefix-carried.txt`
  rows the fixture by path; that row is re-keyed to the new name in `TOOL-aRepatriatedFork-23`'s own
  commit, with its count unchanged.

## 4. Design

### Evidence

At base `git grep -n 'incms-2cff5855'` outside `memory/` hit three files: the generator default,
the selftest's `json.loads` path, and four waiver rows. A trial rename followed by
`python tools/memory-tree/corpus_ids.py --check` exited 0 with no receipt finding, so the nine
`memory/` citations of the old path stay legal.

### Inventory

No new function, file or arm. One file renamed, three readers re-pointed.

### Files touched (estimate)

- `tools/govkit/fixtures/adopter-ic-2cff5855.receipt.json` (renamed)
- `tools/govkit/fixtures/make_adopter_receipt.py`
- `tools/govkit/selftest.py`
- `tools/dead-path-waivers.txt`

### Alternatives rejected

- Waive the ledger row in arm 10. The ban became pure in `TOOL-aRepatriatedFork-35` exactly so
  that no carry path exists; a waiver would rebuild one.
- Drop the fixture's row from `TOOL-aRepatriatedFork-23`'s ledger. The row counts real prefix
  sites, and a ledger that skips a file is the gap that unit closes.

## 5. Production-readiness checklist

- security — none; a rename of a test fixture.
- perf / scale — none.
- error / empty / loading states — a stale reader fails loudly: the selftest's `json.loads` raises.
- observability — the S13 LIVENESS arms print the fixture's row count every run.
- risks — the old name becomes a dead-path needle; any later carrier outside `memory/` reds.
- testing — AC1 to AC4.
- migration — none.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `git grep -n 'incms-2cff5855' -- ':!memory/'` runs on the built tree it prints
  nothing, and `git ls-files tools/govkit/fixtures/` lists `adopter-ic-2cff5855.receipt.json` with
  the blob of the old file. Red when: a reader outside `memory/` still names the old path.
- **AC2** — When the selftest's S13 path expression is evaluated on the built tree, `json.loads` of the
  renamed `adopter-ic-2cff5855.receipt.json` returns 52 `files` rows, each carrying
  `gov_oid`, `oid` and `lf_oid`. Red when: the reader names a path that does not exist.
- **AC3** — `bash tools/check-dead-paths.sh` exits 0. Red when: a waiver row keyed on the old path
  resolves to nothing and goes stale, or a carrier outside `memory/` names the old basename.
- **AC4** — `python tools/govkit/govkit.py selfcheck` exits 0, `python tools/govkit/govkit.py epoch`
  reports no FAILED entry, and `bash tools/check-kit-versions.sh` exits 0. Red when: the rename moved
  a shipped byte without a version bump.

## 7. Gates

`dead-path carriers (deleted files still named)` · `govkit selfcheck` · `kit epoch (shipped bytes move, the version moves)` · `govkit selftest` · `recall floor arms` · `govkit refusal join` · `govkit acceptance matrix` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)`

New arm: none · the old basename becomes a dead-path needle by git's own derivation · none

## 8. Open questions

- none

## 9. Revision log

- rev-1 · 2026-09-29 · initial draft, adopted per the unattended protocol §11 when
  `TOOL-aRepatriatedFork-23`'s widened ledger named the fixture.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "rename a committed test fixture whose filename names an
adopter"` ranked `adopt`, `require_adopted_root` and `derive_rename_map`, none of which renames a
repo file; no existing seam fits, and none is needed for a `git mv`. The naming seam is
`TOOL-aRepatriatedFork-35`'s: the `ic` key and its `make_adopter_receipt.py` rename.

Recall terms used: `frozen receipt fixture filename adopter ic scrub shipped selfcheck arm dead-path
waiver rename`.
