**Serves:** journal TOOL-dDerivedDocket-36

# TOOL-dDerivedDocket-36 — acceptance ledger

One commit carries the unit: the kit README's backlog-modes section, its new table rows, the third
attribute line and the upgrade note; the drift arm in `gen_build_index.py --selftest`; the five agent
carriers and their renders; the memory root's backlog line; the new map dossier with the four
`backlog-shards` claims; the memory-tree move to 2.100 across the constant, four templates and four
renders; the kickoff manifest's re-stamp; the spec at rev-8, CLOSED; and this ledger.

NO MERGE BAR, NO GATE LEG AND NO SUITE FILE RAN IN THIS PASS. The direct checks were the generator's
own `--selftest` flag, run on this tree and on a scratch copy of the kit with one README line
deleted, the render commands each carrier names, the generator's and the migration tool's usage
text, and plain `git`, `grep`, `tr` and `wc` reads.

## What this ledger does NOT evidence, and why

AC4 to AC9 carry `permission:` lines and get no line here; the orchestrator writes them after the
post-build bar. The in-pass halves those lines leave the pass were read, and are recorded as prose:

- **AC4's greps and sizes.** `grep -n -- '--asks --json'` hits each of the five templates inside the
  sentence naming the `mode` fallback, and each carrier's old phrase occurs once, inside that
  sentence. Three carriers name `--asks --json --all`, the rev-8 reading. At the parent, `bfb89fa3`,
  `memory/guides/REVIEW-PROTOCOL.md` read 18062 bytes and 244 lines and reads 18180 and 245 here:
  118 bytes up. `memory/README.md` read 2483 and reads 2607: 124 up. `memory/guides/SESSION-KICKOFF.md`
  reads 25591 bytes and 305 lines at both, the re-stamp rewriting one line in place.
- **AC5's renders.** Each template was re-rendered by its own command:
  `check-protocol-parity.test.sh --render --tracked-only`, `adopt-drift-audit.sh` and
  `adopt-memory-recall.sh --scaffold`. The review protocol and the two harness renders changed only
  in the lines their templates changed; the build harness and the code-audit harness re-rendered
  byte-unchanged. A module parse of both harness renders reached the same top-level `return` it
  reaches at the parent, past the edited lines.
- **AC6's line.** The backlog line of `memory/README.md` calls the family files GENERATED views of
  the live asks filed in `builds/<slug>/BACKLOG.md`.
- **AC7's claims.** `memory/map/baseline.toml` holds an empty `backlog-shards` list, the govkit
  dossier claims none, and `memory-tree-backlog` claims all four; `gen_map.py --write` moved the four
  rows of the generated map to the new dossier.
- **AC8's reads.** After `git fetch`, `origin/main` is `869209ed` and carries 2.99; `fb07ca25`
  carries 2.78. The constant and the four template markers read 2.100, and `git grep` over the four
  renders prints `gov:kit memory-tree@2.100` and no other value. `adopt-memory-tree.sh --render`
  changed line 1 of each render and nothing else. `memory/guides/BUILD-METHOD.md` read 27559 bytes and
  349 lines at the parent and reads 27560 and 349 here: the one byte of 2.100 over 2.99.
- **AC9's stamp.** The `last-audit` datetime advanced from 03:08 to 03:32 and its sha stays the
  merge-base with `origin/main`, `869209ed`. No section B claim reads the version constant or the
  build-method render's first line, so the delta is none.

**Evidences:** TOOL-dDerivedDocket-36
- AC1 — `--help` — every one of the 28 flags the backlog-modes section names was found in the union of `gen_build_index.py --help`, its `--asks` usage and its `--new-build` usage, and `migrate_backlog.py --help`, which lists `--stragglers`, `--relocate`, `--ingest`, `--repair` and `--recipe`; `--new-build <slug> --asks <IDLIST>` matched the generator's usage text by name; `--asks`, `--asks --all`, `--asks --json`, `--asks --tsv` and `--asks --ready` each exited 0 on this switched tree; the section states the argument of `--build`, `--status`, `--target`, `--live-builds`, `--at`, `--probe` and `--new-build`; and its signed-records row names `Ask`, `Verdict` and `Field`.
- AC2 — `gen_build_index.py --selftest` — on this tree it printed `compared 19 verdicts and 9 kinds` and every drift arm held, the whole selftest exiting 0 with 436 arms ok. RED observed: in a scratch copy of the kit whose README had the `V7` line deleted, the positive arm failed with the one finding that V7 has no defining line. The in-suite arms stage the same break for `V7`, `V1` (not satisfied by `V10`), `KEEP` and `V19`, a code raised in the module and absent from the README, and two module extractions that yield nothing, each read as a DEAD PROBE rather than agreement.
- AC3 — `git ls-files tools/memory-tree` — 32 tracked files and 32 table rows, none unrowed and none naming an untracked file; the attribute block holds three `merge=rows` lines; `grep -c 'changes nothing until'` finds the one upgrade note, which names `BACKLOG_MODE`; the section carries the sentence on why the `memory/backlog/*.md merge=rows` line stays; and both backticked tokens of M6 clause 3 in `memory/guides/BUILD-METHOD.md`, `memory/DECISIONS.md` and `--dispatch`, occur in the README's M6 section.
- AC4 — `install-prefix (shipped surface)` — at 364278a8 the leg, `bash tools/check-install-prefix.sh`, exits 0 printing `clean — 322 shipped files, 8 declared waiver(s), 40 marked fixture line(s), no undeclared root-install spelling`, with its runtime-literal and carried-prefix passes clean too. The five carriers' greps and the size reads are the in-pass reads above.
- AC5 — `review-protocol parity (kit vs dogfood)` — at 364278a8 the leg exits 0 printing `in parity — 5 rendered pair(s) match their templates for 'tools/workflows'`, its pair list holding the review protocol and the `tier2-review` and `drift-audit-state` harnesses; the `memory-recall skill wiring` leg exits 0 printing `SKILL.md matches the conf`, and the `drift-audit wiring` leg exits 0 printing `in sync (skill rendered from template, ...)`.
- AC6 — `bash tools/memory-tree/check-memory-hygiene.sh` — exited 0 over the landing reconcile tree of
  2026-09-29, and `memory/README.md` line 20 names each build folder's `BACKLOG.md` as where an ask is
  filed and calls the family files GENERATED views.
- AC7 — `python3 tools/codebase-map/test_codebase_map.py` — as the `codebase-map coverage + freshness` leg at 364278a8 it exits 0 with all six tests ok, `test_every_inventory_key_is_claimed_or_baselined` and `test_generated_artifacts_are_fresh` among them. At that commit `memory/map/baseline.toml` lists no `backlog-shards` key, `memory-tree-backlog` claims `DEPL.md`, `KICK.md`, `PLAY.md` and `TOOL.md`, and every other dossier's `backlog-shards` list is empty.
- AC8 — `bash tools/check-kit-versions.sh` — as the `kit version markers` leg at 364278a8 it exits 0 with no finding, and the `verdict epoch (kit version dates the engine)` leg, `tools/memory-tree/check-verdict-epoch.sh`, exits 0 printing `clean` with 2 engine lines moved in `2d54cc08` and the version moved 2.99 -> 2.101 in that same commit, the build's last version sweep having carried this unit's 2.100 on. There the four templates and the four renders each carry `gov:kit memory-tree@2.101` and no other value, and the `kit/dogfood doc parity` leg exits 0 over the same four pairs. The reads against `fb07ca25`, `origin/main` and the parent are the in-pass reads above.
- AC9 — `bash skills/session-kickoff/manifest-check.sh` — as the `kickoff-manifest ratchet` leg at 364278a8 it exits 0 with no FAILED line, check 5 among the checks it passes. The `last-audit` comparison against the parent is the in-pass read above.
