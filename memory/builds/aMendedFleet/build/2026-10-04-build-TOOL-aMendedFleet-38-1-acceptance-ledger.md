# TOOL-aMendedFleet-38 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-38

**Evidences:** TOOL-aMendedFleet-38
- AC1 — `unrecognized arguments` — at the worktree root after the edit, `map_diff.py HEAD~1..HEAD --converge` exited 2 with `map_diff.py: error: unrecognized arguments: --converge` on stderr, and the same range without the flag exited 0 opening `# map-diff HEAD~1..HEAD`. Red first: the pre-change `map_diff.py` and `map_lib.py`, read from HEAD into the scratchpad and run with `CODEBASE_MAP_ROOT` at this worktree, parsed the flag and exited 0 printing `# map-diff --converge HEAD~1..HEAD`
- AC2 — `reinvention-backlog` — the word-bounded `git grep` over the ten deleted names in `tools` and `.codebase-map.conf` printed nothing (exit 1); the `--converge` grep over `tools`, `WIRE-INTO-PROJECT.md` and `.codebase-map.conf` printed nothing (exit 1) once the second docstring quote in `scen-adversarial.json` was rewritten, which the first run of it named; the `reinvention-backlog` grep printed one line, `tools/codebase-map/README.md:47`, the obsolete-path sentence. Red first: before the edit the first grep named the definitions, the selftest arms and both conf files
- AC3 — `SEAM` — `reuse_lookup.py "normalise a display name into a url slug" --budget 0` exited 0, printed one `## candidates` section, and its first row read `slug [function | tools/hooks/agent-cap.js | fan-in 41 | SEAM]`
- AC4 — `refused` — with `CODEBASE_MAP_ROOT` naming an empty scratchpad directory, `map_diff.py HEAD~1..HEAD` exited 2, stderr opened `map-diff refused: no .codebase-map.conf at the resolved repo root`, and stdout was 0 bytes
- AC5 — `encoding_posture.py` — exited 1 after the selftest deletion, naming `tools/codebase-map/selftest.py` at 4 declared `subprocess` sites against 1 measured; with the registry row lowered to 1 it exited 0 (`143 declared site(s) in 17 row(s)`). `git grep -n -F "gd.resolve() /" -- tools` then printed nothing (exit 1)
- AC6 — `reinvention-backlog.md` — the file under `git rev-parse --git-common-dir` at `codebase-map/` held 21 data rows (22 table lines starting `| `, one of them the header; last written 2026-09-13), matching the pinned 21; it was deleted after this line was written, and a copy sits in the run's scratchpad, never tracked
- AC7 — `--stale-dossiers` — before the commit, at HEAD, it listed `install-prefix` 4 behind and not `codebase-map`. `gen_map.py --check` exited 0 after `--write`. On a commit object of the staged tree (`git commit-tree` over `git write-tree`, parent HEAD), `map_diff.py HEAD..<that commit> --stale-dossiers` printed `1 of 3 dossiers` and named only `gate-lint`, whose dossier was already stale at HEAD and claims the encoding registry this unit lowered; neither `codebase-map` nor `install-prefix` appeared

## The arm

`test_clis_refuse_an_unadopted_root` in `tools/codebase-map/selftest.py` now drives the range digest
at the unadopted root and asserts empty stdout. Run ALONE through a scratchpad script calling the
suite's own `check`: `ok`. Staged red by deleting the `return 2` after the refusal print in
`map_diff.main`: `FAIL ... map_diff exited 0, not a refusal`; restored, `ok`. The census and fixture
edit in `tools/check-install-prefix.test.sh` was not run: it is a `*.test.sh` suite. Neither suite ran.

The post-commit bug-class pass (retirement-inventory-misses-readers-by-value) found that suite's
`FLOOR_ASSERTIONS` at 40 against an executed count, enumerated statically from every `good` and
`run_arm` call site and loop width, of 40 before the census site left and 39 after. The floor falls
to 39 in a second commit, with spec rev-3 naming it in S6; the suite's own count is the close's.

## Owed at the close

- `codebase-map kit selftest`, `codebase-map gate coverage`, `codebase-map adopter e2e`,
  `codebase-map coverage + freshness`, `install-prefix self-test`, `install-prefix (shipped
  surface)`, `encoding posture`, `dead-path carriers`, `recall floor`, `recall floor arms`,
  `lexicon naming predicates`, `memory hygiene` and `spec tokens`.
- The codebase-map kit version bump, per the brief; `kit epoch` is the close's.
