# TOOL-aMendedFleet-38 — `map_diff --converge`, its sink and its prescriptions are deleted

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 38 · closes TOOL-aScouredKit-17

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`map_diff.py --converge` is a closing loop nothing closes. No gate leg, hook, workflow or script runs
it, which its own README states; three documents prescribe it by hand; its sink, the reinvention
backlog under the git common dir, was last written on 2026-09-13 and every row in node a's copy is a
name-stem collision rather than a reinvention. Its `dead_exports` figure is the subject of an open ask
measuring it 100% false positives. This unit deletes the mode, the code only it reaches, its conf key,
its sink on node a and the prescriptions, so the kit stops advertising a check that does not run.

## 2. Scope (IN)

- **S1** — `tools/codebase-map/map_diff.py` deletes the `--converge` flag and the functions only it
  reaches: `_converge`, `_symbols_at_ref`, `_read_symbols`, `derive_backlog_path`,
  `render_legacy_note` and `_new_clones`, with the module docstring's usage line and S5 paragraphs,
  and every comment naming the mode. The range digest and `--drop-affordance-exempt` are unchanged.
  Observed by AC1 and AC2.
  **Readers:** by name: `tools/codebase-map/selftest.py`, `tools/codebase-map/README.md`,
  `WIRE-INTO-PROJECT.md`, `tools/codebase-map/reuse-lookup.agent.md`, `.codebase-map.conf`,
  `tools/codebase-map/.codebase-map.conf.example`, `tools/codebase-map/INVENTORY-DERIVATION.md`,
  `tools/codebase-map/map_lib.py`, `tools/codebase-map/reuse_lookup.py` and
  `tools/check-install-prefix.test.sh`.
  by value: NO VALUE READERS — nothing runs the mode or parses what it prints; `git grep` over
  `tools`, `.githooks`, `.claude` and `skills` finds no caller outside the kit's own self-test.
- **S2** — `tools/codebase-map/map_lib.py` deletes its closing-loop section: `CollisionFlag`,
  `detect_collisions`, `_BACKLOG_PREAMBLE`, `backlog_keys` and `append_backlog`, and
  `reference_index_for`, whose only caller is `_converge`. The docstrings and comments of what the
  lookup still shares, `stems`, `build_reference_index`, `fan_in`, `seam_fanin_threshold`,
  `load_dossier_texts`, the shared-primitives section banner and `require_adopted_root`, name the
  lookup and the digest as their consumers and no longer name the mode. Observed by AC2 and AC3.
  **Readers:** by name: `tools/codebase-map/map_diff.py` and `tools/codebase-map/selftest.py`.
  by value: `tools/codebase-map/map_diff.py` alone, through `_converge`, which S1 deletes.
- **S3** — The `CLONE_COUNT_FILE` key is deleted from `.codebase-map.conf` and from
  `tools/codebase-map/.codebase-map.conf.example`, with the comment above each, and the comment above
  `SEAM_FANIN_THRESHOLD` in the example names the lookup alone. Observed by AC2.
  **Readers:** by name: `.codebase-map.conf`, `tools/codebase-map/.codebase-map.conf.example` and
  `tools/codebase-map/selftest.py`.
  by value: `tools/codebase-map/map_diff.py` alone, through `_new_clones`, which S1 deletes.
- **S4** — The prescriptions go: the `map_diff.py` entry in `tools/codebase-map/README.md` loses its
  `--converge` sentences and the paragraph on where the record lives; the DoD paragraph of
  `WIRE-INTO-PROJECT.md` loses the "Also run" instruction and keeps the `--drop-affordance-exempt` and
  `--seed-affordances` sentences; `tools/codebase-map/reuse-lookup.agent.md` drops its last advisory
  bullet's closing-loop sentence; `tools/codebase-map/INVENTORY-DERIVATION.md` and the
  `reuse_lookup.py` docstring name the lookup alone; and the docstring quote in
  `tools/codebase-map/scen-adversarial.json` follows the docstring it quotes. Observed by AC2.
  **Readers:** by name: `tools/codebase-map/README.md`, `WIRE-INTO-PROJECT.md` and
  `tools/codebase-map/reuse-lookup.agent.md`.
  by value: NO VALUE READERS — these are instructions to people and agents, and no program parses them.
- **S5** — `tools/codebase-map/selftest.py` deletes the arms whose subject S1 to S3 delete:
  `test_detect_collisions_and_backlog`, `test_new_clones_reader`,
  `test_symbols_at_ref_absent_is_not_empty`, `test_backlog_path_is_outside_the_worktree`,
  `test_backlog_path_follows_the_common_dir_not_the_git_dir`,
  `test_legacy_backlog_is_named_and_never_deleted`,
  `test_legacy_note_is_silent_when_it_would_name_its_own_destination` and
  `test_no_tracked_carrier_still_names_the_old_backlog_destination`, with their rows in `main`. The
  unadopted-root refusal arm, `test_clis_refuse_an_unadopted_root`, keeps its `map_diff.py` half by
  invoking the range digest instead of the deleted mode. Observed by AC2 and AC4.
  **Readers:** by name: `tools/codebase-map/selftest.py` alone spells the arm names.
  by value: NO VALUE READERS — an arm's name is printed by its own suite and nothing parses it.
- **S6** — Two registries follow the deletion in the same commit. The census loop in
  `tools/check-install-prefix.test.sh` drops its `gd.resolve()` site and the fixture line spelling that
  shape, because the only tree site of it is `derive_backlog_path`, which S1 deletes, and the census
  exists to refuse a homonym arm for a spelling nobody writes. The `tools/codebase-map/selftest.py`
  row of `memory/project/encoding-posture-sites.txt` takes the count the scan measures after S5,
  since that registry is set-equal in both directions. Observed by AC5.
  **Readers:** by name: `tools/check-install-prefix.test.sh` alone spells the census site.
  by value: NO VALUE READERS — the site string is matched against the tree and nothing else reads it.
- **S7** — Node a's sink, the file `reinvention-backlog.md` in the `codebase-map` directory of this
  clone's git common dir, is deleted after the unit's acceptance ledger records how many rows it held.
  One sentence in the `map_diff.py` entry of `tools/codebase-map/README.md` names that path as
  obsolete for any other clone, where it is untracked and local and no tool will write it again.
  Observed by AC6.
  **Readers:** by name: `tools/codebase-map/map_diff.py` and `tools/codebase-map/map_lib.py`, which S1
  and S2 change.
  by value: NO VALUE READERS — no program reads the rows; the mode only appended to them.
- **S8** — `memory/map/generated/symbols.json` is regenerated after S1, S2 and S5, and the
  prose of the `codebase-map` and `install-prefix` dossiers is refreshed in the same commit, since
  this unit touches paths each claims. Observed by AC7.

## 3. Non-goals (OUT)

- `fan_in`, `build_reference_index`, `seam_fanin_threshold`, `parse_affordance` and
  `load_dossier_texts`. The lookup reads every one of them, so they stay; AC3 observes the lookup.
- The ranking noise `TOOL-aScouredKit-16` describes. Deleting the mode removes one of its two
  consumers and fixes nothing in the ranking, so that ask stays open and this unit does not advance it.
- The drift-audit README's sentence about the upstream repo's `collision_flags` signal. It is the
  kit's founding example of a probe that cannot move, a record of history and not a prescription.
- Sinks in other clones. Each is untracked and local to its machine; S7's README note names the path.
- Bumping the codebase-map kit version. Several units of this build move the kit, and the bump is
  owed once, after the last move, at the close.

### Edges

- **consumes-from** `TOOL-aMendedFleet-37` — AC7 observes the refreshed dossiers through the
  `--stale-dossiers` mode that unit adds to the same file; sequenced after it by `order`.

## 4. Design

### Inventory

This unit mints no identifier. Every name it deletes is listed in §2 with its readers; the measured
claim that only `_converge` calls `reference_index_for` was re-run at writing with `git grep -n -w
reference_index_for -- tools`, which names its definition in `map_lib.py` and its one call in
`map_diff.py`.

### Files touched (estimate)

- `tools/codebase-map/map_diff.py`
- `tools/codebase-map/map_lib.py`
- `tools/codebase-map/selftest.py`
- `tools/codebase-map/README.md`
- `tools/codebase-map/reuse-lookup.agent.md`
- `tools/codebase-map/INVENTORY-DERIVATION.md`
- `tools/codebase-map/reuse_lookup.py`
- `tools/codebase-map/scen-adversarial.json`
- `tools/codebase-map/.codebase-map.conf.example`
- `.codebase-map.conf`
- `WIRE-INTO-PROJECT.md`
- `tools/check-install-prefix.test.sh`
- `memory/project/encoding-posture-sites.txt`
- `memory/map/generated/symbols.json`
- `memory/map/features/codebase-map.md`
- `memory/map/features/install-prefix.md`

### Alternatives rejected

- Wiring the mode into the close instead of deleting it. Its `collision_flags` is a token-stem match
  whose 21 rows on node a are all false positives, and `dead_exports` is the 100% false-positive figure
  of `TOOL-aScouredKit-17`; putting either in front of a closing run teaches it to ignore the block.
  Unit 37's freshness rule is the signal the report asks the close to carry.
- Keeping `reference_index_for` for a future caller. Nothing calls it once `_converge` is gone, and a
  helper kept for a caller that does not exist is the dead code this unit removes.

## 5. Production-readiness checklist

- security — N/A — deletion of a read-only report and a local file it wrote.
- perf / scale — N/A — nothing that runs on any path is slower or faster.
- error / empty / loading states — passing `--converge` now ends in argparse's own usage error at
  exit 2, the refusal any unknown flag gets.
- observability — N/A — the mode reported to nobody; unit 37's signal is the observation that stays.
- risks — an adopter's script calling `--converge` fails loudly at exit 2. None exists in this tree,
  and the kit README states the mode was never on a gate or hook.
- testing — AC1 to AC5 observe the deletion directly; S5's arm changes run in the suite at the close.
- migration — node a's sink is deleted by S7; another clone's copy is left for its owner, as S7 says.
- user docs — the kit README and `WIRE-INTO-PROJECT.md`, per S4.

## 6. Acceptance criteria

- **AC1** — When `python tools/codebase-map/map_diff.py HEAD~1..HEAD --converge` runs at the
  worktree root, it exits 2 with `unrecognized arguments` on stderr, and `python
  tools/codebase-map/map_diff.py HEAD~1..HEAD` exits 0 printing its `# map-diff` header.
  Red when: the flag still parses, or the digest broke with it.
- **AC2** — When `git grep -n -w -e detect_collisions -e append_backlog -e backlog_keys -e
  CollisionFlag -e reference_index_for -e derive_backlog_path -e render_legacy_note -e _new_clones -e
  _symbols_at_ref -e CLONE_COUNT_FILE -- tools .codebase-map.conf` runs, it prints nothing, and
  `git grep -n -e "--converge" -e "reinvention-backlog" -- tools WIRE-INTO-PROJECT.md
  .codebase-map.conf` prints nothing.
  Red when: a reader still spells a deleted name, or a document still prescribes the mode.
- **AC3** — When `python tools/codebase-map/reuse_lookup.py "normalise a display name into a url
  slug"` runs, it exits 0 and prints its `## candidates` section with at least one row marked `SEAM`.
  Red when: the deletion took a helper the lookup still reads.
- **AC4** — When `CODEBASE_MAP_ROOT` names an empty directory and `python
  tools/codebase-map/map_diff.py HEAD~1..HEAD` runs, it exits 2 with `refused` on stderr and prints
  nothing on stdout.
  Red when: retargeting the refusal arm lost the refusal it covers.
- **AC5** — When `python tools/gate-lint/encoding_posture.py memory/project/encoding-posture-sites.txt
  . tools skills` runs it exits 0, and `git grep -n -F "gd.resolve() /" -- tools` prints nothing.
  Red when: the site registry still counts a deleted subprocess call, or the install-prefix census
  still names a site no tree file carries.
- **AC6** — When `git rev-parse --git-common-dir` is resolved on node a after the unit's commit, its
  `codebase-map` directory holds no `reinvention-backlog.md`, and the unit's acceptance ledger line for
  this criterion states the row count the file held before deletion.
  Red when: the file survives, or it is gone with no count recorded.
  figure: PINNED — 21 data rows, read 2026-10-04 on node a; the report's 19 was read earlier.
- **AC7** — When `python tools/codebase-map/gen_map.py --check` runs after the unit's commit it exits
  0, and `python tools/codebase-map/map_diff.py --stale-dossiers` lists neither `codebase-map` nor
  `install-prefix`.
  Red when: the regenerated artifact is stale, or a dossier this unit touched is older than its paths.

## 7. Gates

`codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `codebase-map coverage + freshness` · `install-prefix self-test` · `install-prefix (shipped surface)` · `encoding posture (text IO names its encoding)` · `dead-path carriers (deleted files still named)` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: `tools/codebase-map/selftest.py` · `test_clis_refuse_an_unadopted_root` invokes the range digest at an unadopted root instead of the deleted mode · none
New arm: `tools/check-install-prefix.test.sh` · the census loop loses its `gd.resolve()` site and AC5's fixture loses the matching line · none

The eight arms S5 deletes are not moved anywhere: their subject is gone, so their coverage goes with it.

## 8. Open questions

- **F1** — What happens to the install-prefix census entry for the deleted site?
  RESOLVED (agent, 2026-10-04, delegated): delete the census site and the fixture line spelling the
  same shape. The census exists so that no homonym arm guards a spelling nobody writes, and
  `git grep -F "gd.resolve() /"` finds that spelling only in `derive_backlog_path` and the test itself.
- **F2** — Is node a's sink deleted or left in place?
  RESOLVED (agent, 2026-10-04, delegated): deleted, after its row count is recorded. The brief names
  the sink as part of what goes; its 21 rows were read at writing and each pairs a new name with a seam
  sharing only a verb stem, such as `render_report` with `report`, so nothing in it is a finding; and a
  file no tool writes or reads is the unmaintained record this unit deletes everywhere else.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft.

## 10. Reuse audit

No existing seam fits, because this unit adds nothing: it deletes. The probe that matters for a
deletion is the inverse one, which callers would lose, and it was run as `git grep` per deleted name
over the whole tracked tree: every reader is named in §2, and `fan_in`, `build_reference_index`,
`seam_fanin_threshold`, `parse_affordance` and `load_dossier_texts` stay because `reuse_lookup.py`
calls each. `python tools/codebase-map/reuse_lookup.py "report a new exported symbol that resembles
an existing high fan-in seam"` cannot answer it: it ranks by name stems and resolves no caller. The
recall probe returned the records that built the mode and moved its sink, `bConvergentLodestar` S5
and `TOOL-dTracedLattice-3`, and the two asks measuring its outputs as noise; none names a consumer.
Where the report and the tree disagree: the report counted 19 sink rows and node a's file holds 21 on
2026-10-04; the report's three prescription sites are confirmed, and a fourth and fifth were found,
`INVENTORY-DERIVATION.md` and the `reuse_lookup.py` docstring, plus the install-prefix census entry.

Recall terms used: `python tools/memory-recall/query.py "why does map_diff have a converge mode and a
reinvention backlog, and who reads it" --terms "map_diff converge closing loop reinvention backlog
collision_flags new_clones bConvergentLodestar S5 F7 sink git-common-dir"`
