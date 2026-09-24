# DEPL-aRepatriatedFork-17 — govkit update is safe to run and says what it did

**Status:** CLOSED · rev-3 · 2026-09-24 · node a · Tier-2 · base a7c78ad2 · streams deployer · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-24-build-DEPL-aRepatriatedFork-13-2-acceptance-ledger.md](../build/2026-09-24-build-DEPL-aRepatriatedFork-13-2-acceptance-ledger.md) | journal | DEPL-aRepatriatedFork-13 DEPL-aRepatriatedFork-21 |
| [2026-09-24-build-DEPL-aRepatriatedFork-17-1-acceptance-ledger.md](../build/2026-09-24-build-DEPL-aRepatriatedFork-17-1-acceptance-ledger.md) | journal | — |
| [2026-09-23-prompt-DEPL-aRepatriatedFork-17-build-brief.md](../prompts/2026-09-23-prompt-DEPL-aRepatriatedFork-17-build-brief.md) | journal | — |
| [2026-09-24-review-TOOL-aRepatriatedFork-1-closing-diff-round1.md](../reviews/2026-09-24-review-TOOL-aRepatriatedFork-1-closing-diff-round1.md) | diff-review | DEPL-aRepatriatedFork-1 TOOL-aRepatriatedFork-2 TOOL-aRepatriatedFork-3 TOOL-aRepatriatedFork-4 TOOL-aRepatriatedFork-5 TOOL-aRepatriatedFork-6 TOOL-aRepatriatedFork-7 TOOL-aRepatriatedFork-8 TOOL-aRepatriatedFork-9 TOOL-aRepatriatedFork-10 TOOL-aRepatriatedFork-11 TOOL-aRepatriatedFork-12 DEPL-aRepatriatedFork-13 DEPL-aRepatriatedFork-14 TOOL-aRepatriatedFork-15 TOOL-aRepatriatedFork-16 TOOL-aRepatriatedFork-18 TOOL-aRepatriatedFork-19 DEPL-aRepatriatedFork-20 DEPL-aRepatriatedFork-21 TOOL-aRepatriatedFork-21 |

<!-- /gen:spec-records -->

## 1. Goal

The 2026-09-23 pull of both adopters from fd240496 to a7c78ad2 was supposed to be one
`govkit update --write`. It became 59 hand-resolved conflict hunks, a `--no-verify` commit and a
re-measure commit per hand-resolved fork, a tree left half-rolled-back, 17 false receipt
mismatches, and 20 lone CR bytes silently stripped from shell programs. Each of those traces to a govkit mechanic rather than to either
adopter's bytes. This unit fixes the eight mechanics so a rollback leaves a consistent tree, a
conflict hands the operator a byte-exact candidate, a receipt can be re-measured in the same commit
as the fork it measures, and every report line describes the tree as it is.

## 2. Scope (IN)

- **S1** — A ROLLBACK COVERS WHAT THE RE-RENDER WROTE. Today the verify pass rolls back only
  `written_paths`, and the code says so: a kit's `[[regenerate]]` argv writes outside that set
  (`govkit.py:8728-8730`), so a rolled-back kit keeps its re-rendered `SKILL.md`, protocol, fixture
  records and `unattended-build.js`. Before the re-render step (`govkit.py:8560`), `update` snapshots
  the index entry and worktree bytes of every receipt row of that kit whose role is `rendered` or
  `generated`, plus every path an optional `[[regenerate]].writes` list names. A rollback of that
  kit restores them through the existing restore loop, and the rollback order lists them. After a
  rollback, any path of that kit whose bytes still differ from the snapshot is printed by name.
  Observed by AC1, AC2.
- **S2** — INTEGRITY IS GRADED THROUGH THE TARGET'S OWN FILTERS. `cmd_check`'s integrity arm hashes
  raw worktree bytes (`govkit.py:3758`), so a file that `checkout-index` wrote with CRLF under
  `core.autocrlf=true`, as both the landing (`govkit.py:6693`) and the rollback (`govkit.py:8930`)
  do, is reported as not matching the receipt although `git status` shows it clean. When the raw
  hash differs, the arm computes `git hash-object --path=<path> <file>` and passes the row when that
  equals the row's `oid`, counting it as `eol-only` on the integrity line. Observed by AC3, AC4.
- **S3** — A CONFLICT LEAVES A BYTE-EXACT CANDIDATE. `three_way` (`govkit.py:6701-6719`) discards
  `git merge-file`'s output on conflict, and both conflict orders (`govkit.py:8055-8069` and
  `:8188-8200`) carry only hashes. `three_way` returns the conflict-marked bytes of
  `git merge-file -p --diff3` on conflict. A new `write_conflict_candidate` writes `base`, `ours`,
  `theirs` and `candidate` with `write_bytes`, never through a text mode, under
  `.governance/outbox/update-conflict-<slug>/`, and the order names all four plus the one
  `git merge-file` line that reproduces the candidate. The target file itself stays byte-identical,
  as today. Observed by AC5, AC6.
- **S4** — LONE-CR LOSS IS A FINDING. `update`, read-only or not, compares each `engine` row's count
  of CR bytes not followed by LF against gov's blob at the row's `commit`, and prints a `lone-CR`
  row, with both counts, for every row whose target copy holds fewer. Observed by AC7.
- **S5** — THE RECEIPT CAN BE MEASURED IN THE SAME COMMIT AS THE BYTES. `adopt` refuses any index
  that differs from HEAD (`demand_adopt_index_clean`, `govkit.py:9564-9588`), while an adopter's
  staged-receipt arm grades the staged bytes against the staged receipt, so every hand-resolved
  fork needs one commit made with `--no-verify` and a second that re-measures. `adopt --staged`
  lifts that refusal for the planned destinations only, refuses when any of them differs between
  worktree and index, measures from the index as it already does (`govkit.py:9729`), and stages
  `.governance/install.json` and `.governance/install.sums` with the result. Observed by AC8, AC9.
- **S6** — A ROLE MOVE IS RESOLVED WHERE IT IS REPORTED. `update` reports `role-moved` rows and names
  `apply` as the verb that re-records them (`govkit.py:7245-7255`, `:7489-7496`). `apply` writes
  every `engine` destination raw, which both adopters forbid. `update --write --accept-role-moves`
  re-records the role of each moved row, touches no bytes in this run, and prints `role-recorded`
  per row. A move INTO a writing disposition, such as `project-owned` to `engine`, also runs the
  attribution walk `adopt` runs (`derive_attribution`) over the row, so it lands `vintage-match`
  when the target bytes descend from a gov vintage and `unattributed` when they do not; the NEXT
  `update` then grades it through the verdict table like any other engine row. Without the flag the
  row falls through on the role it landed under, exactly as today (`govkit.py:7256-7262`). `plan`
  prints `KEEP` for a `seed` destination that already exists, matching `apply`, which leaves one in
  place (`govkit.py:5704-5710`). The flag takes only a move whose new role's disposition is not
  in `KIT_WRITING_DISPOSITIONS`: a move into `rendered` is written by the kit's own regenerate in
  the same run, so it falls through to the reconcile-or-refuse path under the recorded role, and
  the flag records no role for it. Observed by AC10, AC11, AC15, AC16.
- **S7** — A KIT'S VERSION IS READ FROM THE TARGET'S BYTES. The per-kit delta prints
  `MIXED across rows` whenever receipt rows carry different `version` strings (`govkit.py:7523`),
  and a pinned row carries the version of its BASE vintage (`govkit.py:9811-9826`), so a kit whose
  pinned files were merged forward reads MIXED while every file holds the new constant. The delta
  line reads the constant from the target's own copy of the kit's `version_from` file and compares
  THAT with gov. Row versions stay in the receipt as base attribution and are printed as such.
  Observed by AC12.
- **S8** — A LEG GOV WROTE IS CLAIMED, NOT REFUSED. `write_gate_legs` raises when the target's runner
  holds a leg name the receipt does not record as emitted (`govkit.py:2927-2930`). When the
  runner's leg has the same name AND the same resolved argv as the descriptor's leg, it is gov's leg
  by construction: it is recorded as emitted and printed `claimed`. A same-named leg with a different
  argv still refuses, and the refusal now names that difference. Observed by AC13.
- **S9** — AN UNATTRIBUTED ROW GETS A SUGGESTED PIN. `adopt --suggest-pins` prints, per
  `unattributed` row, the gov revision whose blob of the row's source is nearest the target bytes
  by changed-line count, the count, and a ready `--pin <path>=<rev>` when the count is at most a
  declared fraction of the target file's lines. Past that fraction it prints no pin and names
  `adopter-owned` as the remedy. The search is `nearest.py`'s algorithm, promoted from the pull's
  scratch directory into govkit. Observed by AC14.

## 3. Non-goals (OUT)

- Wiring new hook fragments into `settings.json` during `update`. That is `TOOL-aRepatriatedFork-11`,
  which owns the fragment class the stall-recorder and stop-guard hooks exposed.
- Making `apply` safe at a forked adopter. S6 removes the one reason an adopter was told to run it.
- Auto-resolving conflicts. S3 hands the operator a correct starting file and nothing else.
- LF-pinning every kit file in the target's `.gitattributes`. It would override each adopter's own
  line-ending convention to fix what S2 fixes by reading the target's filters.
- Changing what `unattributed` withholds. The `gov_commit` re-stamp rule at `govkit.py:9461-9471`
  stands; S9 and the adopter-owned role give its rows an exit.

### Edges

- **hands-off** `TOOL-aRepatriatedFork-11` — wiring a newly shipped hook fragment during an update,
  which item (h) of this unit's brief names and this spec does not build.
- **consumes-from** `DEPL-aRepatriatedFork-13` — the `adopter-owned` role that S9 names as the remedy
  when no vintage is near. Without it S9 can only say that no pin fits.
- **hands-off** `TOOL-aRepatriatedFork-18` — the suites that unit moves from `project-owned` to
  `engine`, which S6's move into a writing disposition re-records and attributes, and which that
  unit's own acceptance then observes arriving at an adopter.

## 4. Design

### Evidence

| Mechanic | Measured | When |
|---|---|---|
| S1 | a verify rollback restored sources and left the kit's re-rendered outputs modified | the 2026-09-23 pull, reported by the operator |
| S2 | `govkit check` reported 17 receipt mismatches after a rollback under `core.autocrlf=true`; both adopters' clones carry `core.autocrlf=true` | the pull; the config read 2026-09-23 |
| S3 | 59 conflict hunks reconstructed by hand from the hashes in each order | the pull |
| S4 | 20 lone CR bytes lost across three files, 4, 4 and 12, by a CR-normalising reconstruction, restored since | audit-C cross-cutting finding 1; the restored counts re-measured 2026-09-23 |
| S5 | inCMS commit pairs `7e28395d4`/`2bbd7b99b`, `247572de8`/`042387eab` and `6ca2d0b38`/`51b1cec59`: a fork edit, then a receipt re-measure | inCMS log, 2026-09-23 |
| S6 | `role-moved` for `map_extractors.py` and `drift_signals.py` at both adopters; inCMS's `plan` lists 164 `write [engine]` rows and `write [seed]` for both seeds | read-only `update` and `plan`, 2026-09-23 |
| S7 | `MIXED` on codebase-map and lexicon at both adopters, and on unattended at nc, whose stored rows read 1.17 and 1.28 | read-only `update`, 2026-09-23 |
| S8 | the gate-leg step refused on nc's `agent-instructions wiring` leg, which carries the descriptor's argv and which nc's receipt does not record as emitted | the pull; nc's runner and receipt read 2026-09-23 |
| S9 | a nearest-vintage search found usable pins for 31 of 32 nc rows | the pull |

Every figure in the table is PINNED at the date its row names. S7's figure is re-derived by AC12.

### Data model

```toml
[[regenerate]]
argv = ["bash", "{kit}/adopt-unattended.sh", "--render"]
writes = [".claude/skills/unattended/SKILL.md", "{memory_root}/guides/UNATTENDED-PROTOCOL.md"]   # optional, S1
```

```text
.governance/outbox/update-conflict-<slug>/base
.governance/outbox/update-conflict-<slug>/ours
.governance/outbox/update-conflict-<slug>/theirs
.governance/outbox/update-conflict-<slug>/candidate     # git merge-file -p --diff3 ours base theirs
```

### Inventory

- `write_conflict_candidate(outbox, row, base, ours, theirs, candidate)` — `py.function`, verb `write`.
- `measure_lone_cr(data)` — `py.function`, verb `measure`.
- `derive_nearest_vintage(root, src, ours, to_commit)` — `py.function`, verb `derive`.
- `read_target_kit_version(target, desc, receipt)` — `py.function`, verb `read`.
- `check_leg_claimable(argv, runner_leg)` — `py.function`, verb `check`.
- `read_worktree_status(target)` — `py.function`, verb `read`; S1's status snapshot.
- constants `MERGE_FILE_ARGS` (S3), `ADOPT_STAGED_RECEIPT` (S5), `NEAREST_PIN_FRACTION` (S9, §8 F1).
- flags `--staged` on `adopt`, `--accept-role-moves` on `update`, `--suggest-pins` on `adopt`.
- `[[regenerate]].writes` — a new optional descriptor key.

### Files touched (estimate)

`tools/govkit/govkit.py` · `tools/govkit/selftest.py` · `WIRE-INTO-PROJECT.md`. The verb's own
`USAGE` text carries the flags; this tree has no `tools/govkit/README.md`. No shipped descriptor
declares `[[regenerate]].writes`: every regenerate output a shipped kit writes is already one of its
`rendered` or `generated` receipt rows, which S1 snapshots without the key.

### Adopter deletions this unit enables

None of these mechanics is forked in either adopter, so no divergence row or carve-out retires. What
the adopters stop doing is the hand procedure the pull needed: reconstructing base, ours and theirs
from hashes, committing forks with `--no-verify`, restoring re-rendered outputs by hand after a
rollback, and restoring lone CR bytes with `restore_cr.py` from the pull's scratch directory.

### Rollout

S3, S4 and S7 change report output and outbox content only. S5, S6 and S9 are opt-in flags. S1 and
S2 change what a write run restores and what `check` reports, and each is observed against a fixture
whose pre-change behaviour is recorded red first. No default-off flag guards them, because each
narrows a destructive or false outcome rather than adding one.

### Alternatives rejected

- Normalising line endings in `land_through_index`. It writes through the index so the target's
  own smudge filter decides the worktree bytes, a deliberate property recorded at
  `govkit.py:6661-6697`. S2 reads the same filters instead of fighting them.
- Writing the conflict candidate into the target file. The byte-identical invariant is what lets
  the operator re-run `update` safely; the candidate belongs beside the order.
- Auto-pinning every suggestion. A pin is an operator's assertion about a base (`evidence: "pinned"`),
  and S9 keeps it one.

## 5. Production-readiness checklist

- security — S3 writes four files under `.governance/outbox/`, a path govkit already writes and both
  adopters ignore. `<slug>` comes from `render_order_slug`, which is already injective and contained.
  S8 claims a leg only on an exact argv match, so a target cannot launder a different command into
  gov's receipt. No new target-supplied value reaches an argv.
- perf / scale — S4 reads one gov blob per engine row, which `classify_row` already fetches. S9
  walks `git log` per unattributed row, up to 193 revisions for one nc row, and is opt-in for
  that reason.
- error / empty / loading states — S5 refuses when a planned destination is dirty relative to the
  index. S8 still refuses a real collision and says what differs.
- observability — `lone-CR`, `eol-only`, `role-recorded`, `claimed` and the unrestored-path list are
  each a named line, so no mechanic changes an outcome silently.
- risks — S1 widens what a rollback touches. It restores only paths it snapshotted, and a path it
  cannot restore is printed, which is the current loop's contract.
- testing — one `govkit selftest` fixture per scope item, each observed red against a7c78ad2's
  `govkit.py` first.
- migration — none. Receipt shape is unchanged; the new flags are additive.
- user docs — `tools/govkit/README.md` and `WIRE-INTO-PROJECT.md`'s maintenance section.

## 6. Acceptance criteria

- **AC1** — When a `govkit selftest` fixture kit declares a `[[regenerate]]` that rewrites a
  `rendered` row and a `[check]` that reds only after the run, `update --write` restores that
  rendered row, and the rollback order lists it as restored.
  Red when: the rendered row keeps the re-rendered bytes, which a7c78ad2 does, recorded red first.
- **AC2** — When the fixture's `[[regenerate]]` also writes a path its `writes` list omits, the run
  prints that path as still differing after the rollback.
  Red when: an undeclared write survives a rollback with no line naming it.
- **AC3** — When a fixture clone with `core.autocrlf=true` holds a CRLF worktree copy of an LF engine
  row, `python tools/govkit/govkit.py check --target <fixture>` counts it `eol-only` and reports no
  mismatch.
  Red when: the arm reports a mismatch for a clean file, which a7c78ad2 does, recorded red first.
- **AC4** — When the same fixture's file differs by a real byte, `check` still reports the mismatch.
  Red when: `eol-only` hides a content change.
- **AC5** — When a fixture row diverges with a conflicting three-way, `update --write` leaves the
  target file byte-identical and writes the four candidate files, and `git merge-file -p --diff3`
  over the written `ours`, `base` and `theirs` reproduces `candidate` byte for byte.
  Red when: the order carries hashes only, which a7c78ad2's does.
- **AC6** — When the conflicting fixture file carries a lone CR inside an awk program, `candidate`
  carries it at the same offset.
  Red when: any of the four files is written through a text mode.
- **AC7** — When a fixture engine row's target copy holds 0 lone CRs against gov's 4,
  `python tools/govkit/govkit.py update --target <fixture>` prints a `lone-CR` row naming 4 and 0.
  Red when: the loss is silent, which it is at a7c78ad2.
- **AC8** — When a fixture has a staged edit to an engine row,
  `python tools/govkit/govkit.py adopt --target <fixture> --re-adopt --staged --write` exits 0, and
  the staged receipt's `oid` for that row equals `git rev-parse :<path>`.
  Red when: `adopt` refuses the staged tree, which a7c78ad2 does without the flag.
- **AC9** — When the same fixture also has an UNSTAGED edit at a planned destination, the `--staged`
  run refuses naming that path.
  Red when: the receipt records bytes the next commit will not carry.
- **AC10** — When a fixture receipt holds a `role-moved` row whose new role is `seed`,
  `update --write --accept-role-moves` re-records the role, the file's bytes and index entry are
  unchanged, and the row prints `role-recorded`.
  Red when: any byte moves, or the next read-only run still prints `role-moved` for that row.
- **AC11** — When `python tools/govkit/govkit.py plan --target <fixture>` runs where a seed
  destination exists, the row prints `KEEP`, not `write`.
  Red when: `plan` promises a write `apply` will not make.
- **AC12** — When `update` runs read-only against a scratch clone of the nc worktree, the
  `unattended` delta line reads the constant from the clone's own `unattended.sh` and is not `MIXED`.
  Red when: row base versions still decide the verdict.
  fixture: a `--shared` clone of the nc worktree.
  figure: the verdict is DERIVED from the clone's bytes at observation time.
- **AC13** — When a fixture runner already holds `agent-instructions wiring` with the descriptor's
  resolved argv and the receipt records no emitted legs, `update --write` records it as emitted and
  prints `claimed`; with a different argv it refuses naming both argvs.
  Red when: the identical leg is refused, which a7c78ad2 does.
- **AC14** — When `python tools/govkit/govkit.py adopt --target <fixture> --suggest-pins` runs on a
  fixture with one row drifted slightly from an old gov vintage and one unrelated program, it prints
  a `--pin` for the first and names `adopter-owned` for the second.
  Red when: an unrelated program is offered a pin.
- **AC15** — When a fixture receipt holds a `project-owned` row whose descriptor now declares it
  `engine`, and its bytes equal a gov vintage, `update --write --accept-role-moves` records it
  `engine` with `evidence: "vintage-match"` and writes no byte; the next `update --write` lands gov's
  newer bytes through the verdict table.
  Red when: the move into a writing role is skipped, which a7c78ad2 does, or bytes move in the
  run that re-records it.
- **AC16** — When a fixture receipt holds an operator-edited `engine` row whose descriptor now
  declares it `rendered` under a real `[[regenerate]]`, `update --write --accept-role-moves` exits
  non-zero naming the three-way conflict, prints no `role-recorded`, and the operator's bytes stand
  in the target's index.
  Red when: the flag re-records the role and the regenerate overwrites the edit unreported.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit runbook parity` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: `tools/govkit/selftest.py` · one fixture per scope item, each first run against a7c78ad2's `govkit.py` to record its red · none

## 8. Open questions

- **F1 — what fraction makes a nearest vintage "usable" for S9?** The pull's nc rows needing a pin
  ran from 2 to 810 changed lines, and inCMS's four parallel programs from 250 to 2364.
  Recommendation: a pin is suggested when the changed-line count is at most half the target file's
  line count, declared as a constant beside `derive_nearest_vintage` and printed with every
  suggestion.
  RESOLVED (owner, 2026-09-23): suggest a pin when at most half the target's lines changed, the
  fraction a constant beside `derive_nearest_vintage`, printed with every suggestion, as
  recommended.
- **F2 — should `--accept-role-moves` be the default for a move into a non-writing disposition?**
  Nothing is written, so the only effect is the receipt agreeing with the descriptor.
  Recommendation: keep it opt-in for one release. The existing report says choosing is not gov's to
  do on the operator's behalf, and a release of opt-in use tests that stance.
  RESOLVED (owner, 2026-09-23): opt-in for one release, as recommended.
- **F3 — should S4's `lone-CR` row be `r.fail` rather than a report?** Recommendation: `r.fail` on a
  `--write` run and a report on a read-only one. A write run that lands over a damaged program is the
  moment the loss becomes permanent.
  RESOLVED (owner, 2026-09-23): `r.fail` on `--write`, a report on a read-only run, as recommended.

## 9. Revision log

- rev-1 · 2026-09-23 · initial draft, grounded at a7c78ad2 on the pull's reported defects, audit-C's
  lone-CR measurement, and read-only `update` and `plan` runs at both adopters on 2026-09-23.
- rev-2 · 2026-09-24 · build-time divergences, no scope moved. Section 4 inventory: `check_leg_claimable`
  takes the resolved argv and the runner row, which is all S8 compares; `derive_nearest_vintage`
  takes the measuring commit, as `derive_attribution` does; `read_worktree_status` is added for S1's
  undeclared-write naming. S1: a restored path that is no receipt row is printed `reverted` in the
  rollback order, apart from `restored`, and a path still differing is printed `still differs`.
  S2: a row passes as `eol-only` only when the target's filter changed the bytes, so a tampered
  `sha256` over untouched bytes still reds. S3: the reap removes a stale order's candidate
  directory with it. Section 4 files touched: no `tools/unattended/kit.toml` edit and no
  `tools/govkit/README.md`. AC13 is observed in the selftest's `-13` gate-leg block, which already
  builds a manifest runner, and that block's older refusal arm now carries a differing argv.
- rev-3 · 2026-09-24 · closing review round 1 M2. S6: `--accept-role-moves` takes only a move whose
  new disposition is not in `KIT_WRITING_DISPOSITIONS`, so a move into `rendered` keeps the
  reconcile-or-refuse path; AC16 added, observed in `tools/govkit/matrix.py`'s role-move block,
  whose `rr-edited` fixture it reuses. That block's remedy arm now reads `--accept-role-moves`,
  the remedy S6 put in place of `apply`.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "write a conflict-marked merge candidate and roll back re-rendered outputs"`
ranked `gotchas.write`, `gen_build_index.write_text` and the two `merge` functions, none of which
govkit may import across a kit edge. No existing seam fits as a mapped symbol. The live seams are
extended in place: `three_way`'s `git merge-file` call, the verify pass's `snap_rows` restore loop,
`render_order_slug` for the candidate directory, and `resolve_entry_version_at` for S7.

Recall terms used: `govkit update rollback regenerate snap_rows conflict three_way merge-file
autocrlf checkout-index lone CR role-moved MIXED unattributed pin`.
