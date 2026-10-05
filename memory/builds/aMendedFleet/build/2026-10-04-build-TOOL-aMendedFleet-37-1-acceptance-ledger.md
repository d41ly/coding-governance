# TOOL-aMendedFleet-37 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-37

**Evidences:** TOOL-aMendedFleet-37
- AC1 — `map_diff.py --stale-dossiers --json` — at the worktree root before the commit: exit 0, `live` true, `of` 27 against 27 lines from `git ls-files memory/map/features` and an empty `note`, `stale` 26; the `codebase-map` row's `refreshed` equalled `git log -1 --format=%H -- memory/map/features/codebase-map.md`, 584bb02d. 1.7 s wall
- AC2 — `map_diff.py --stale-dossiers --json` — in a full clone of the unit's staged tree under `%TEMP%/af37`: after a commit touching only `memory/map/features/codebase-map.md` the row read `stale` false; after a comment line appended to `tools/codebase-map/rank_harness.py` it read `stale` true, `behind` 1, `newest` that commit's sha; after a commit adding only `memory/map/generated/probe.json` it still read `behind` 1
- AC3 — `map_diff.py <base>..HEAD --stale-dossiers` — in that clone, from the dossier-only commit over the code and map-root commits: one `- codebase-map` line; after a further commit refreshing the dossier, the same range printed `0 of 1` and no `codebase-map` line
- AC4 — `drift_report.py --json` — at the worktree root: the `dossiers_older_than_their_paths` record read `gateable` false, `live` true, `value` 26 equal to AC1's `stale`, `of` 27, `tolerance` and `pin` 26 equal to its `PINS` entry
- AC5 — `git clone --depth 1` — from a `file://` URL under `%TEMP%/af37`, `rev-parse --is-shallow-repository` true: `map_diff.py --stale-dossiers --json` printed `live` false with a `note` naming the shallow history, and `drift_report.py --base-ref HEAD` printed `DEAD PROBE — signal cannot move` on the signal's row. The explicit base ref is the clone's, which carries no `origin` tracking ref
- AC6 — `.codebase-map.conf` — deleted in the full clone: `drift_report.py --json --base-ref HEAD` gave the record `not_asked` true with the note `no codebase map is adopted at this root (map-diff refused: no .codebase-map.conf ...)`, and the human table printed `not asked — ...` on the row, never a value or DEAD PROBE
- AC7 — `CODEBASE_MAP_ROOT` — naming an empty directory: `map_diff.py --stale-dossiers` exited 2, stderr opened `map-diff refused: no .codebase-map.conf`, stdout was 0 bytes
- AC8 — `drift_report.py --check --base-ref HEAD` — in the full clone, whose HEAD carries the pin at 26: raising it to 27 with no comment exited 1 with `RATCHET WEAKENED — ... dossiers_older_than_their_paths moved 26 -> 27`; restoring the line returned exit 1 with no ratchet line, the prior exit, which is `non_terminal_specs_cited_by_product_source = 4 (pin 2)`, four foreign specs none of this unit's
- AC9 — `grep -c` — `dossiers_older_than_their_paths` in `tools/drift-audit/README.md` printed 1, and `-e "--stale-dossiers"` in `tools/codebase-map/README.md` printed 1
- AC10 — `gen_map.py --check` — in the full clone of the staged tree, exit 0; `map_diff.py --stale-dossiers` there printed `26 of 27` and no `codebase-map` line

## The arms

`test_dossier_staleness_from_git` in `tools/codebase-map/selftest.py`, a real git fixture with a
seed, a dossier refresh, a code commit, a map-root-only commit and a second refresh, read whole and
by range, plus an uncommitted dossier and the shallow and untouched answers. Run ALONE through a
scratchpad script calling `check`: `ok`. Staged red twice and restored: with the map-root exclusion
removed, `behind` read 2; with the ancestry pass disabled, the dossier read stale at its own
refresh. `test_clis_refuse_an_unadopted_root` gained the `--stale-dossiers` refusal: `ok` alone.

`test_stale_dossiers` in `tools/drift-audit/selftest.py`, six checks over canned output for a value,
a `live` false object, unparseable text, an exit 2 and an absent kit. Run ALONE: six `ok`. Staged red
by sending exit 2 down the parse branch: the not-asked check FAILED as DEAD PROBE; restored.
`CHECK_FLOOR` 289 -> 295. Neither suite ran.

The clones are of the staged tree written as a commit object (`git commit-tree`) whose only
difference from the unit's commit is this ledger.

## Owed at the close

- `codebase-map kit selftest`, `codebase-map gate coverage`, `codebase-map adopter e2e`,
  `codebase-map coverage + freshness`, `drift-audit selftest`, `drift-audit records`, `drift-audit
  wiring`, `recall floor`, `recall floor arms`, `lexicon naming predicates` and `spec tokens`.
- The codebase-map and drift-audit kit version bumps, per the brief; `kit epoch` is the close's.
