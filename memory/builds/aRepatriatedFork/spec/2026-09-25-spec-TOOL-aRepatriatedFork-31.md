# TOOL-aRepatriatedFork-31 — gov's shipped files carry no adopter name

**Status:** CLOSED · rev-2 · 2026-09-25 · node a · Tier-1 · base a58011ef · streams tooling · order 16

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-25-build-TOOL-aRepatriatedFork-31-1-acceptance-ledger.md](../build/2026-09-25-build-TOOL-aRepatriatedFork-31-1-acceptance-ledger.md) | journal | — |
| [2026-09-26-review-TOOL-aRepatriatedFork-36-closing-diff-round1.md](../reviews/2026-09-26-review-TOOL-aRepatriatedFork-36-closing-diff-round1.md) | diff-review | TOOL-aRepatriatedFork-32 TOOL-aRepatriatedFork-35 TOOL-aRepatriatedFork-36 TOOL-aRepatriatedFork-37 TOOL-aRepatriatedFork-38 |

<!-- /gen:spec-records -->

## 1. Goal

inCMS's brand gate reds six files gov ships it, because each names another adopter in a provenance
comment. Gov scrubs every such name from what it ships and bans the class, so an adopter registered
tomorrow is covered the day its row lands. Owner ruling, `DEPL-aRepatriatedFork-20` §8 F8.

## 2. Scope (IN)

- **S1** — Every `NicoCares` in a file `python tools/govkit/govkit.py shipped` lists becomes
  `adopter nc`, keeping the record id beside it. That covers 31 sites in 17 files, the one self-test
  arm label in `row_grammar.py` among them. Observed by AC1, AC2.
- **S2** — A gov-internal declaration, `tools/govkit/adopters.toml`, names the trees gov ships into:
  a `key` for the neutral spelling and the `names` the ban refuses. Not `registry.toml`, which the
  playbook renderer ships to every adopter. Observed by AC1.
- **S3** — `govkit.py selfcheck` gains arm 10: no shipped file names a declared adopter,
  case-insensitively, beyond what `[adopter.carried]` counts for it. The carried set is SET-EQUAL
  with the measurement in both directions and by count. Observed by AC1, AC3, AC4.
- **S4** — inCMS's own name is carried, not drained: 131 sites in 43 shipped files, measured
  2026-09-25 by arm 10. The drain is `TOOL-aRepatriatedFork-35`. Observed by AC1.
- **S5** — memory-tree, unattended, review-harness and check-wiring take their version bump in every
  carrier. push-main declares no version. Observed by AC5.

## 3. Non-goals (OUT)

- Gov's own records under `memory/` and the deployer under `tools/govkit/`, which ship nowhere.
- Draining the carried inCMS sites; that is `TOOL-aRepatriatedFork-35`.

### Edges

- **hands-off** `DEPL-aRepatriatedFork-20` — the six vendored files inCMS's brand gate reds, which
  its update from gov HEAD then lands clean.

## 4. Design

### Evidence

`git grep -i -c nicocares 3cf05f29 -- tools .githooks skills '*.template.*'` counted 49 hits in 21
files. Of those, 31 sit in the 17 files the shipped listing names; the rest are in `tools/govkit/`,
which no descriptor ships. The listing already covers `.githooks/` and the root template.

### Inventory

No new function. Arm 10 is inline in `selfcheck`, beside arms 8 and 9.

### Files touched (estimate)

`tools/govkit/govkit.py`, `tools/govkit/adopters.toml`, `tools/memory-tree/`, `tools/unattended/`,
`tools/workflows/`, `.githooks/`, the check-wiring and memory-recall self-tests, and the version
carriers of the four bumped kits.

### Alternatives rejected

- A literal brand list inside the check. A new adopter would then need a code change to be covered.
- A leg of its own. `selfcheck` already derives the shipped population and runs on every bar.
- Leaving inCMS unregistered. Its name reaches nc and swydee through the same files, so a ban
  without it leaves the class open for the adopter that ships the most provenance.

## 5. Production-readiness checklist

- security — none; a read-only scan over tracked files.
- perf / scale — one read per shipped file inside a check that already resolves every descriptor.
- error / empty / loading states — an empty or absent declaration is a refusal, never a pass.
- observability — arm 10 prints its name count, file count, sites and carried total on every run.
- risks — a brand spelled across a line break is not seen. The header says so.
- testing — the staged-break observations in AC3 and AC4.
- migration — none.
- user docs — none; `adopters.toml` carries its own contract in its header.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py selfcheck` runs on the built tree, it exits 0 and
  prints `adopter names: 3 from 3 adopters.toml row(s)` with every site carried.
  Red when: a `NicoCares` survives in a shipped file, or the carried set misses an inCMS site.
- **AC2** — When `python3 tools/memory-tree/row_grammar.py --selftest` runs, the renamed arm label
  still passes. Red when: the label rename broke the arm or its expectation.
- **AC3** — When one staged line naming `NicoCares` is added to `tools/hooks/README.md`,
  `python tools/govkit/govkit.py selfcheck` exits 1 naming that file and the adopter.
  Red when: the arm stays silent on a new adopter name.
- **AC4** — When one carried inCMS site in `tools/push-main.sh` is rewritten,
  `python tools/govkit/govkit.py selfcheck` exits 1 saying the count can only fall.
  Red when: a drained site leaves its carried row standing.
- **AC5** — `bash tools/check-kit-versions.sh` exits 0 and `python tools/govkit/govkit.py epoch`
  reports no FAILED entry. Red when: a moved kit kept its old value in any carrier.

## 7. Gates

`govkit selfcheck` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `row-grammar selftest` · `kit/dogfood doc parity` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `harness arms (fail branches armed or pinned)`

New arm: `tools/govkit/govkit.py` selfcheck arm 10 · a staged adopter name in a shipped file · none

## 8. Open questions

- **F1 — inCMS's own name.** Registering inCMS reds 131 sites; leaving it out leaves its name
  reaching nc and swydee. RESOLVED (agent, 2026-09-25): register it and carry every site, counted
  and shrink-only, with the drain filed as `TOOL-aRepatriatedFork-35`. The owner's F8 ruling named
  only the nc provenance, so this pick is surfaced for confirmation.

## 9. Revision log

- rev-1 · 2026-09-25 · initial draft, from `DEPL-aRepatriatedFork-20` §8 F8.
- rev-2 · 2026-09-25 · §2 S2 · S4 · §8 F1 · the declaration moved out of `registry.toml` once the
  build found the playbook renderer ships that file. Built: arm 10 red on the staged hit and on a
  drained site, green on the tree.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "list the files gov ships to an adopter"` ranked
`adopt`, `corpus_files` and `require_adopted_root`, none of which lists what gov ships. The seam is
`cmd_shipped` in `tools/govkit/govkit.py`, found by reading it: `TOOL-aRepatriatedFork-16` made it
the one derivation of the shipped set. Arm 10 reads the same `resolve_entry` survivors, so the ban
and the listing cannot disagree about the population.

Recall terms used: `shipped adopter provenance brand gate selfcheck registry descriptor survivors
carried ratchet install-prefix`.
