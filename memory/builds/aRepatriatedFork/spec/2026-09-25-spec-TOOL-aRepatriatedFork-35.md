# TOOL-aRepatriatedFork-35 — gov's shipped files name no adopter, inCMS included

**Status:** CLOSED · rev-2 · 2026-09-25 · node a · Tier-1 · base a84e0e66 · streams tooling · order 18

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-25-build-TOOL-aRepatriatedFork-35-1-acceptance-ledger.md](../build/2026-09-25-build-TOOL-aRepatriatedFork-35-1-acceptance-ledger.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aRepatriatedFork-31` banned every adopter name from gov's shipped files but carried inCMS's
own 131 sites in 43 files as a shrink-only count, so nc and swydee still received that name. Owner
ruling, 2026-09-25: drain them now, fixtures included, and make the ban pure.

## 2. Scope (IN)

- **S1** — Every provenance mention of inCMS in a file `python tools/govkit/govkit.py shipped` lists
  cites the registry key instead, `adopter ic`, the way `TOOL-aRepatriatedFork-31` made NicoCares
  `adopter nc`. Record ids stay beside it. Observed by AC1.
- **S2** — Fixtures take neutral names. The pre-push and lander suites' remote `incms` becomes
  `mirror`; the scratch-guard near-miss path becomes `/c/projects/app/`; the lexicon TypeScript
  corpus spells `store` where it spelled `incms`, same length, so no oracle line moves. Observed by
  AC4.
- **S3** — The gov-internal receipt generator `tools/govkit/fixtures/make_incms_receipt.py` becomes
  `make_adopter_receipt.py`, because the shipped `scen-adversarial.json` lists it by path. Its
  references, the encoding-posture row and the generated map follow. Observed by AC5.
- **S4** — `tools/govkit/adopters.toml` gives inCMS the key `ic` and drops its carry table.
  `govkit.py selfcheck` arm 10 loses the carry logic and refuses a row that still declares
  `carried`. Its finding names the row's key. Observed by AC1, AC2, AC3.
- **S5** — Every kit whose shipped bytes moved takes its version bump in every carrier. Observed by
  AC6.

## 3. Non-goals (OUT)

- Gov's own records under `memory/`, the deployer under `tools/govkit/`, and
  `WIRE-INTO-PROJECT.md`, which no descriptor ships. The frozen receipt keeps its filename.

### Edges

- **hands-off** `DEPL-aRepatriatedFork-20` — the drained provenance comments and the renamed
  fixtures, which inCMS's next update from gov lands as ordinary engine bytes.

## 4. Design

### Evidence

At base, arm 10 printed `131 site(s), 131 carried` over 267 shipped files. The sites were 118 lines
in 43 files: provenance prose, two suites keyed on a remote named `incms`, one scratch-guard
path, four TypeScript fixture records and one path in `scen-adversarial.json`.

### Inventory

No new function. Arm 10 in `selfcheck` shrinks; the `carried` refusal replaces the set-equality
loop.

### Files touched (estimate)

The 43 shipped files, `tools/govkit/adopters.toml`, `tools/govkit/govkit.py`, the renamed generator
and its four referrers, the rendered workflow copies and `memory/guides/REVIEW-PROTOCOL.md` (a
render of the edited template), the codebase map, and the version carriers of eleven kits.

### Alternatives rejected

- Keep the carry machinery for a future adopter. Nothing uses it, and an unused ratchet is dead
  code a reader has to decode.
- Rewrite the `scen-adversarial.json` path without renaming the file. The row would then name a
  file that does not exist.

## 5. Production-readiness checklist

- security — none; comment and fixture text, plus a read-only arm.
- perf / scale — arm 10 does less work than before.
- error / empty / loading states — a row declaring `carried` is a named refusal.
- observability — arm 10 prints its name count, file count and site total every run.
- risks — the key `ic` is only meaningful beside `adopters.toml`, as `nc` already was.
- testing — AC2 to AC5.
- migration — none.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py selfcheck` runs on the built tree, it exits 0 and
  prints `adopter names: 3 from 3 adopters.toml row(s) over 267 shipped file(s) · 0 site(s)`.
  Red when: any shipped file still names inCMS.
- **AC2** — When one staged line naming inCMS is appended to `tools/push-main.sh`, `selfcheck` exits 1
  naming that file and citing `adopter ic`. Red when: the ban stays silent.
- **AC3** — When `[adopter.carried]` is appended to `adopters.toml`, `selfcheck` exits 1 saying the
  ban no longer reads it. Red when: a carry table is silently ignored.
- **AC4** — The renamed fixtures pass: `.githooks/pre-push.test.sh`'s remote block as a slice,
  `bash tools/push-main.test.sh`, `bash tools/hooks/scratch-guard.test.sh`, and the TypeScript block
  of `tools/lexicon/selftest.py` as a slice. Red when: an arm keyed on the old name fails.
- **AC5** — `python3 tools/codebase-map/test_codebase_map.py`, `bash tools/check-dead-paths.sh` and
  the encoding-posture scan exit 0 after the rename. Red when: a referrer still names the old path.
- **AC6** — `bash tools/check-kit-versions.sh` exits 0 and `python tools/govkit/govkit.py epoch`
  reports no FAILED entry. Red when: a moved kit kept its old value in any carrier.

## 7. Gates

`govkit selfcheck` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `kit/dogfood doc parity` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `harness arms (fail branches armed or pinned)` · `codebase-map coverage + freshness` · `dead-path carriers (deleted files still named)`

New arm: `tools/govkit/govkit.py` selfcheck arm 10 · an adopters.toml row declaring `carried` · none

## 8. Open questions

- **F1 — the neutral spelling for inCMS.** No key existed. RESOLVED (agent, 2026-09-25): `ic`, its
  initials, the same derivation as `nc`.

## 9. Revision log

- rev-1 · 2026-09-25 · initial draft, from the backlog row this unit closes and the owner's ruling.
- rev-2 · 2026-09-25 · §2 S3 · §4 · the receipt generator's rename added once the build found
  `scen-adversarial.json` lists it by path. Built: arm 10 green at 0 sites, red on a staged site and
  on a carry table.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "ban an adopter name from every shipped file"` ranked
`adopt`, `corpus_files` and `require_adopted_root`, none of which scans the shipped set. The seam is
arm 10 itself, which `TOOL-aRepatriatedFork-31` built over `cmd_shipped`; this unit only removes
its carry path.

Recall terms used: `adopter provenance brand shipped carried ratchet selfcheck adopters.toml drain
fixture remote key`.
