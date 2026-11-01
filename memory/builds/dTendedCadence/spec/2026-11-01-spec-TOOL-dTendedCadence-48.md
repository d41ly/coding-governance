# TOOL-dTendedCadence-48 — the round-1 spec audit's 40 minors, batched: run scopes and criteria that can pass, stable filing keys, one policy adapter, committed recurrence, and the carriers each unit owes

**Status:** OPEN · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 20 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 |
| [2026-11-01-prompt-TOOL-dTendedCadence-35-promoted-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-35-promoted-fix-brief.md) | research | TOOL-dTendedCadence-35 TOOL-dTendedCadence-39 |
| [2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md) | spec-audit | TOOL-dTendedCadence-35 TOOL-dTendedCadence-37 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-47 TOOL-dTendedCadence-36 TOOL-dTendedCadence-46 TOOL-dTendedCadence-40 TOOL-dTendedCadence-38 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-39 TOOL-dTendedCadence-41 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit, `reviews/2026-11-01-review-TOOL-dTendedCadence-1-to-18-spec-audit-round1.md`,
confirmed 53 findings, and TOOL-dTendedCadence-35 to -47 take its 13 HIGH. This unit is BUILD-METHOD
M4's batch of its 30 MEDIUM and 10 LOW by raw id, one scope item per id, in report order, M1 to M29
and then L1 to L9. They land on 17 of the 18 roster units and on three promoted units, so it repairs
no unit in particular and builds last, order 20, above every unit of the build.

Every id: M1 3; M2 6; M3 7; M4 8; M5 9; M6 10; M7 11; M8 12; M9 13; M10 15; M11 21, 49; M12 23; M13
26; M14 27; M15 28; M16 32; M17 33; M18 34; M19 35; M20 36; M21 37; M22 44; M23 46; M24 47; M25 48;
M26 50; M27 51; M28 52; M29 53; L1 16; L2 17; L3 18; L4 19, 38; L5 20; L6 22; L7 24; L8 25; L9 29.

## 2. Scope (IN)

- **S1** — id 3, M1, landing on unit 1. The period run reads the `scope = "outside"` rows beside the
  `repo` rows, since they are fleet-wide, so `remote_ci_red_streak` dead past `maintain.dead-after`
  reaches `item.maintain.file`. Observed by AC1.
- **S2** — id 6, M2, landing on unit 1. The walk's order is `order_by_needs`'s sorted ready rounds,
  lease, levels, read, patch, file, record, and unit 1 AC2 is read in that order. Observed by AC2.
- **S3** — id 7, M3, landing on unit 3. Unit 3 AC3 and AC4 are observed through the node pass,
  `maintain.py --scope node`, which reads the two node-scoped direct-fix readings now that unit 16 is
  built. Observed by AC3.
- **S4** — id 8, M4, landing on units 16 and 9. Unit 16 AC7 and unit 9 AC4 run the node pass,
  `GOV_CADENCE_KEY=<period>.<node> python maintain.py --scope node`, over their node-scoped readings.
  Observed by AC3.
- **S5** — id 9, M5, landing on units 9, 16 and 17. A recurrence with no live ask is observed as unit
  8 AC8 observes it, a second receipt on one intake and no second intake, under two distinct period
  keys; a `seen` claim plants an `OPEN` ask carrying the marker. Observed by AC4.
- **S6** — id 10, M6, landing on units 15 and 6. The hashed text of `write_breach_ask` is the
  stable head and its `accept` clause alone. The band and the diagnose probe are the period's facts,
  so they go to the period's record: its Readings table gains a `Band` column, and its `## Lines`
  gain one `probe: <reading><TAB><offender key><TAB><probe record>` line per diagnose probe, so a
  band move files no second intake (§8 F4). Observed by AC5.
- **S7** — id 11, M7, landing on units 8 and 11. `write_patch_intake(root, reading, key, text=None,
  filer="item.maintain.patch")` takes the text and the filer; unit 11 calls it with its §4 text and
  `playbook-cycle-<cycle>`, and unit 11 AC6 runs against that call. Observed by AC6.
- **S8** — id 12, M8, landing on unit 3. drift-audit's README `## The signals` table gains the rows
  `idle_processes_past_ceiling` and `landed_branches_unpruned`. Observed by AC7.
- **S9** — id 13, M9, landing on units 3 and 4. `live_builds_without_activity`'s pin is 0, the one
  exception unit 4 S5's measured seeding names, so each dormant build reaches the act band.
  Observed by AC8.
- **S10** — id 15, M10, landing on every unit that changes `tools/drift-audit/`. Settled with S16: the
  lander mints each kit version (`tools/push-main.sh:26-31`, TOOL-aMendedFleet-65), so no unit's write
  set owes a version carrier and `kit epoch` grades the bump at the push boundary. Observed by AC9.
- **S11** — id 21, M11, landing on unit 8. The row comment in `tools/drift-audit/kit.toml` reads
  `optional: ask | patch | file, only on a row with no fix`, the set TOOL-dTendedCadence-38 owns as
  `ROUTE_VALUES`, and the README's registry section points at that table. Observed by AC10.
- **S12** — id 49, M11, landing on units 17 and 9. Unit 17 S11 and unit 9 S4 cite
  TOOL-dTendedCadence-38's set and add no value; a `route = "ask"` row passes the check. Observed by
  AC10.
- **S13** — id 23, M12, landing on unit 16. The node pass and `derive_node_reading_turn` cover all
  four node-scoped readings unit 8 registers, `dangling_pointers_in_own_ledger`,
  `legs_retried_after_timeout`, `fleet_over_budget` and `backlog_stragglers`. Observed by AC11.
- **S14** — id 26, M13, landing on units 2, 6, 13 and 4. drift-audit holds one policy adapter:
  `read_record_when`, `read_review_mode` and the `maintain.events` selector each call
  `read_policy_value("<key>", root)` and map `PolicyRefused` to their own refusal line. Observed by
  AC12.
- **S15** — id 27, M14, landing on unit 16. `measure_unrecorded_runs` asks runlog per run, `runlog.py
  record <slug>` with no `--write`, and reads its skip line, so `derive_closing_end` and
  `scan_anomalies` decide and the four new anomaly kinds count. Observed by AC13.
- **S16** — id 32, M16, landing on units 2, 11 and 13. Their "moves once per pass" sentences and
  version rows do not bind: the branch moves no `KIT_DRIFT_AUDIT_VERSION` or `KIT_UNATTENDED_VERSION`.
  Observed by AC9.
- **S17** — id 28, M15, landing on units 6 and 13. `read_newest_record(root, run=None,
  carrying=None)` returns, given `carrying`, the newest committed record whose named line is not
  `none`, and unit 13 S3 reads its base through `read_newest_record(root, run="security",
  carrying="security-head")`. Observed by AC14.
- **S18** — id 33, M17, landing on unit 6. The `## Record the run` section of
  `tools/unattended/SKILL.template.md` keeps its heading and takes one sentence no longer than the
  78-byte command line it stands in for: "The terminal verbs write the run record as
  observability.run-record says.", 75 bytes with the key in backticks. Unit 6 AC7 still finds the
  key in the render, and `.claude/skills/unattended/SKILL.md`, at 10237 bytes against a 10240 cap
  (`tools/template-size-limits.txt:154`, PINNED 2026-11-01 by `wc -c`), falls by 3. Observed by
  AC15.
- **S19** — id 34, M18, landing on unit 10. `memory/project/method-carriers.txt` gains the row
  `.claude/agents/gov-maintainer.md · rendered role agent`. Observed by AC16.
- **S20** — id 35, M19, landing on unit 18. The `TRACE_CUTOFF` row of
  `memory/project/method-carriers.txt` is re-keyed to `tools/loop/flow_layer.py`, and to its template
  where the template keeps the comment. Observed by AC16.
- **S21** — id 36, M20, landing on units 15, 2 and 18. Each new inventory key is claimed by a
  dossier: the leg `maintain breach record` and the SessionStart hook in
  `memory/map/features/session-kickoff.md`, which claims drift-audit's legs today; the two memory legs
  in `memory/map/features/memory-tree-hygiene.md`; the two flow legs in
  `memory/map/features/playbook.md`, which unit 18 already edits, since the tree holds no loop kit
  dossier; and `memory/map/generated/` re-rendered. Observed by AC17.
- **S22** — id 37, M21, landing on units 7, 9, 15 and 18. This unit, the build's last, re-checks the
  §B claims of `memory/guides/SESSION-KICKOFF.md` and re-stamps its `last-audit` once, after every
  commit of the build touching a watched file. Observed by AC18.
- **S23** — id 44, M22, landing on unit 15. Step (1) of `write_breach_ask` writes no `BACKLOG.md`
  row: a live ask's recurrence is the re-filed stable text, whose content key is on record, so it is a
  receipt, route `seen`, and the walk leaves no tracked file dirty. Observed by AC19.
- **S24** — id 46, M23, landing on units 1 and 6. The record's landing intake carries the key, the
  base and a SHA-256 digest of the readings JSON; the patch build re-derives the readings with
  `drift_report.py --readings` at that base and refuses a digest that differs; `maintenance.py write`
  exits 2 on stdin that is empty, not JSON, or missing `read` or `readings`. Observed by AC20.
- **S25** — id 47, M24, landing on unit 18. The scratch tree's path is
  `<git-common-dir>/maintain-read/<sha12>.<pid>`, as post-merge suffixes `gate-pm.<pid>`, and stale
  `maintain-read/*` trees whose pid is not alive are pruned before an add. Observed by AC21.
- **S26** — id 48, M25, landing on unit 16. `closed_runs_with_no_run_record`'s population is the
  closed runs that served a spec unit (`derive_serves`), so an unbound run is never missing.
  Observed by AC13.
- **S27** — id 50, M26, landing on unit 3. `measure_idle_processes` gives one detail row per flagged
  row of the dry sweep's report, `{"verdict", "command"}` from the line
  `tools/process-monitor/classify.py:77-79` renders, never the `winpid`. Observed by AC22.
- **S28** — id 51, M27, landing on unit 1. The re-run contract: the walk appends each completed item
  to `<git-common-dir>/maintain-walk/<key>`, and a re-run under the same key starts after the last
  completed item, so a hand-over taken on the same node files no second receipt. Observed by AC23.
- **S29** — id 52, M28, landing on unit 12. The blame is `git blame --porcelain HEAD -- <file>`, and
  the scan reads `HEAD`'s blobs. Observed by AC24.
- **S30** — id 53, M29, landing on unit 13. A security finding's offender key is `<path>\t<normalized
  title>`, the title lowercased with runs of whitespace and digits squeezed, never its line.
  Observed by AC25.
- **S31** — id 16, L1, landing on unit 16. `standing_directives_not_promoted`'s row carries no
  `kind`, so its owner derives `layer.runtime` for a node-scoped row (unit 4 S1). Observed by AC26.
- **S32** — id 17, L2, landing on unit 4. Unit 4 S6's callers are units 1, 2, 3, 6, 9, 13 and 14 to
  18, closed by S14. Observed by AC12.
- **S33** — id 18, L3, landing on unit 18. The five moved signals' rows are out of the README signal
  table, and the pointer to the three legs is a prose line beneath it. Observed by AC7.
- **S34** — id 19, L4, landing on units 4 and 15. `help/README.md` carries one line for
  `help/maintain.md`. Observed by AC27.
- **S35** — id 38, L4, the same defect on unit 15 S10: the line exists, and unit 15 edits the page
  only. Observed by AC27.
- **S36** — id 20, L5, landing on unit 17. A refused policy read takes the default `file` with its
  `NOTE:` line, as unit 17 S4 says. Observed by AC28.
- **S37** — id 22, L6, landing on unit 10. The roles kit spells no count of its workflows or house
  overlays: `tools/roles/workflows.toml:1` and `:4`, `tools/roles/check_roles.py:31` and
  `tools/roles/README.md:4` and `:275` name the set without a number. Observed by AC29.
- **S38** — id 24, L7, landing on unit 15. The over-pin status lines `--check` prints sit at
  `drift_report.py:4427-4438` at base, and unit 15 §4 is read with that citation. Observed by AC30.
- **S39** — id 25, L8, landing on unit 5. The feature dossiers number 32 at base, DERIVED by `ls
  memory/map/features/*.md`, and unit 5's rejected alternative is read with that count.
  Observed by AC30.
- **S40** — id 29, L9, landing on units 13 and 18. `add_detached_worktree(root, sha, subdir)`, a
  context manager in `drift_report.py`, holds the scratch tree's add, its S25 path and its take-down;
  `resolve_reading_tree` and `security_review.py` call it with `maintain-read` and `security-review`.
  Observed by AC21.

## 3. Non-goals (OUT)

- Every HIGH: TOOL-dTendedCadence-35 to -47.
- A receipt keyed by period inside `intake.py`, the cross-node half of S28: dWellOiledMachine's.
- The left-shift gates the report suggests beside each minor: each is a gate of its own, outside the
  one mechanism M4 admits for this batch.

### Edges

- **consumes-from** `TOOL-dTendedCadence-1` — `maintain.py`'s scopes, order and landing intake (S1, S2, S24, S28)
- **consumes-from** `TOOL-dTendedCadence-2` — the `maintain.events` selector and the hook key (S14, S16, S21)
- **consumes-from** `TOOL-dTendedCadence-3` — the direct-fix readings and their README rows (S3, S8, S9, S27)
- **consumes-from** `TOOL-dTendedCadence-4` — the measured pin seeding and the adapter's callers (S9, S14, S32, S34)
- **consumes-from** `TOOL-dTendedCadence-5` — the rejected alternative's dossier count (S39)
- **consumes-from** `TOOL-dTendedCadence-6` — the record's `Band` column and `probe:` lines, `read_record_when`, `read_newest_record`, the stdin refusals and the Skill section (S6, S14, S17, S18, S24)
- **consumes-from** `TOOL-dTendedCadence-7` — the leg whose manifest edit owes the re-stamp (S22)
- **consumes-from** `TOOL-dTendedCadence-8` — `write_patch_intake` and the `route` row comment (S7, S11)
- **consumes-from** `TOOL-dTendedCadence-9` — its node-pass criterion, recurrence and route citation (S4, S5, S12, S22)
- **consumes-from** `TOOL-dTendedCadence-10` — the rendered `gov-maintainer` agent and the roles counts (S19, S37)
- **consumes-from** `TOOL-dTendedCadence-11` — the repeat filing's text and filer (S7, S16)
- **consumes-from** `TOOL-dTendedCadence-12` — `scan_annotations`' blame (S29)
- **consumes-from** `TOOL-dTendedCadence-13` — the review's mode read, base, finding key and scratch tree (S14, S16, S17, S30, S40)
- **consumes-from** `TOOL-dTendedCadence-15` — `write_breach_ask`'s text and step (1), the leg's dossier and the help index (S6, S21, S23, S34, S35, S38)
- **consumes-from** `TOOL-dTendedCadence-16` — the node pass's criteria, readings and populations (S4, S5, S13, S15, S26, S31)
- **consumes-from** `TOOL-dTendedCadence-17` — the route citation, the refused read and recurrence (S5, S12, S36)
- **consumes-from** `TOOL-dTendedCadence-18` — the scratch tree, the carriers row, the legs' dossiers and the signal table (S20, S21, S25, S33, S40)
- **consumes-from** `TOOL-dTendedCadence-38` — `ROUTE_VALUES`, the set S11 and S12 cite
- **consumes-from** `TOOL-dTendedCadence-39` — the review's base read, which S17 adds `carrying=` to
- **consumes-from** `TOOL-dTendedCadence-47` — `write_breach_ask`'s closed-ask case, beside which S23 changes step (1)
- **hands-off** `TOOL-dTendedCadence-49` — S24's landing intake, whose readings digest and re-derivation that unit replaces with the written record carried under `refs/gov/maintain-record/<key>` (review id 1)
- **hands-off** `TOOL-dTendedCadence-50` — S24's patch build, whose re-derivation that unit's `maintenance.py land` replaces with a check of commit and digest (review id 28)
- **hands-off** `TOOL-dTendedCadence-51` — S24 and AC20's round trip, which that unit's arm observes across two clones (review id 42)
- **hands-off** `TOOL-dTendedCadence-52` — S24's single landing grammar, onto whose replacement that unit puts the security review's landing (review id 43)
- **hands-off** `TOOL-dTendedCadence-58` — AC9 and AC18, which that unit grades over the build's own non-merge commits (review id 18)
- **hands-off** `TOOL-dTendedCadence-59` — its criteria, scratch tree, journal, `probe:` line, dossier, inventory and §7, which the minors batch repairs (review ids 6, 7, 8, 9, 14, 20, 24, 25, 30, 31, 33, 34, 37, 39, 44, 45)

## 4. Design

### Evidence

Each item's finding, its cited lines and its skeptic verdict are the report's, by id; ids 46 and 50
carry the skeptic's corrected fix, which S24 and S27 take. Read at base for this unit:
`tools/push-main.sh:26-31` ("A branch therefore owes no bump"), `tools/process-monitor/classify.py:77-79`
(the report row, verdict first, command last, the pid between), `help/README.md` (no `maintain.md`
line), `memory/project/method-carriers.txt:17` (the `TRACE_CUTOFF` row), `tools/roles/workflows.toml:1`
and `:4` and `tools/roles/check_roles.py:31` (the word "ten").

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `add_detached_worktree` | function, `drift_report.py` | `py.function`, OK by `lexicon.py --suggest` at writing |
| `text`, `filer` | parameters of `write_patch_intake` | none |
| `carrying` | parameter of `read_newest_record` | none |
| `maintain-walk/<key>` | node-local journal under the git common dir | none |

### Files touched (estimate)

- `tools/drift-audit/maintain.py`: S1, S2, S28
- `tools/drift-audit/maintenance.py`: S6, S14, S17, S24
- `tools/drift-audit/readings.py`: S7
- `tools/drift-audit/maintain_file.py`: S6, S23
- `tools/drift-audit/maintain_fixes.py`: S27
- `tools/drift-audit/node_readings.py`: S13, S15, S26
- `tools/drift-audit/security_review.py`: S14, S17, S30, S40
- `tools/drift-audit/cadence_events.py`: S14
- `tools/drift-audit/playbook_cycle.py`: S7
- `tools/drift-audit/drift_report.py`: S25, S29, S40
- `tools/drift-audit/kit.toml`: S11, S31
- `tools/drift-audit/README.md`: S8, S11, S33
- `tools/drift-audit/selftest.py`: the arm of §7
- `tools/unattended/SKILL.template.md` and its render `.claude/skills/unattended/SKILL.md`: S18
- `memory/project/method-carriers.txt`: S19, S20
- `memory/map/features/session-kickoff.md`, `memory/map/features/memory-tree-hygiene.md`,
  `memory/map/features/playbook.md` and `memory/map/generated/`: S21
- `memory/guides/SESSION-KICKOFF.md`: S22
- `help/README.md`: S34, S35
- `tools/roles/workflows.toml`, `tools/roles/check_roles.py` and `tools/roles/README.md`: S37

## 5. Production-readiness checklist

- security — S23 and S24 shrink the walk's write surface: no tracked edit outside an intake, and a
  machine payload no longer rides a redacting, capped text channel; S25 keeps the scratch tree under
  the common dir.
- perf / scale — S15 adds one runlog subprocess per closed run per period, bounded by the period's runs.
- error / empty / loading states — S24's three stdin refusals exit 2 before a write.
- observability — each item keeps its unit's lines; S28 prints `resume after <item>` on a re-run.
- risks — S28's journal is node-local, so a hand-over taken by another node re-runs completed items;
  `ponytail:` ceiling, the upgrade is a period-keyed receipt in `intake.py` (§3).
- testing — the criteria of §6, in the one arm of §7.
- migration — N/A — every module these items change is new in this build.
- user docs — `help/README.md` gains its line (S34).

## 6. Acceptance criteria

- **AC1** — When `GOV_CADENCE_KEY=2026-11-01 python maintain.py --dry-run` runs over a fixture with an
  `outside` reading dead past its limit, it routes that reading to `item.maintain.file`.
  Red when: no run reads the `outside` row.
- **AC2** — When `GOV_CADENCE_KEY=2026-11-01 python maintain.py --dry-run` runs over unit 1's fixture,
  the item lines print lease, levels, read, patch, file, record.
  Red when: the walk hand-orders read before levels.
- **AC3** — When `GOV_CADENCE_KEY=2026-11-01.node-a python maintain.py --scope node` runs over fixtures
  planting `idle_processes_past_ceiling`, `acts_past_ceiling_with_no_outcome` and
  `maintain.retrofit-heat`, the first reaches `item.maintain.direct` and the others are filed.
  Red when: a node-scoped reading is read by the period run or by no run.
- **AC4** — When two runs under `2026-11-01` and `2026-11-02` file one offender with no live ask into
  a scratch intake store, the store holds one intake with two receipts; with an `OPEN` ask carrying the
  marker planted, the second run prints `seen`.
  Red when: a criterion's recurrence differs from unit 8 AC8's observation.
  fixture: `intake.py` is TOOL-dWellOiledMachine-27's, absent at `f4597719`.
- **AC5** — When one offender is filed under the `diagnose` band and then the `act` band with a
  recording filer, the two recorded texts are byte-equal, and the first period's record carries its
  `Band` cell `diagnose` and one `probe:` line.
  Red when: the band moves the hashed text, or the band and probe are recorded nowhere.
- **AC6** — When `python playbook_cycle.py --cycle weekly` runs, the recorded call to
  `write_patch_intake` carries filer `playbook-cycle-weekly` and unit 11's text.
  Red when: the call takes no text or filer.
- **AC7** — When `grep -c "idle_processes_past_ceiling\|landed_branches_unpruned" README.md` runs in
  `tools/drift-audit/`, it prints 2, and `read_signal_table_names` lists none of the five moved names.
  Red when: a `SIGNALS` name has no row, or a moved one keeps its row.
- **AC8** — When `python drift_report.py --readings` runs over a fixture with three dormant builds,
  the `live_builds_without_activity` record's `tolerance` is 0 and it is `over`.
  Red when: the measured value is seeded as its pin.
- **AC9** — When `git diff f4597719..HEAD -- tools/drift-audit/drift_report.py tools/unattended/unattended.sh`
  runs at the close, it shows no line assigning `KIT_DRIFT_AUDIT_VERSION` or `KIT_UNATTENDED_VERSION`.
  Red when: a pass hand-bumps a version the lander mints.
- **AC10** — When `grep -n "ask | patch | file" kit.toml` runs in `tools/drift-audit/`, it prints the
  row comment, and a planted `route = "ask"` row passes `check_reading_rows`.
  Red when: the comment or the check names another set.
- **AC11** — When the node pass runs under `lease-holder` over a fixture planting
  `legs_retried_after_timeout`, it prints `node readings — skip`, and the period run reads it.
  Red when: one of the four is outside the turn rule.
- **AC12** — When `grep -n "policy.py.*get" tools/drift-audit/*.py` runs, it matches only inside
  `read_policy_value`, and `grep -c 'read_policy_value("maintain.security-review"'
  security_review.py` prints 1.
  Red when: a second adapter spawns `policy.py get`.
- **AC13** — When `measure_unrecorded_runs` reads a fixture whose one closed bound run carries only a
  `refusal` under `on-anomaly`, and one unbound closed run, it counts 1 of 1.
  Red when: the refusal is missed, or the unbound run is counted.
- **AC14** — When a scratch worktree commits two records, the later carrying `security-head: none`,
  `read_newest_record(root, carrying="security-head")` returns the earlier.
  Red when: the filter returns a record whose line reads `none`.
- **AC15** — When `wc -c .claude/skills/unattended/SKILL.md` runs after the render, it prints at most
  10240.
  Red when: the render passes its cap.
- **AC16** — When `grep -c "gov-maintainer.md\|flow_layer.py" memory/project/method-carriers.txt`
  runs, it prints 2, and `grep -c "drift_signals.py" memory/project/method-carriers.txt` prints 0.
  Red when: a new or moved method pointer has no row, or a stale row stays.
- **AC17** — When `grep -l "maintain breach record" memory/map/features/*.md` runs, it names one
  dossier, and the same holds for the SessionStart hook's key and the four new legs.
  Red when: a new inventory key is claimed by no dossier.
- **AC18** — When `git merge-base --is-ancestor <c> <restamp>` runs for each commit `<c>` of
  `f4597719..HEAD` touching `tools/gate-legs.json` or `skills/session-kickoff/manifest-check.sh`,
  `<restamp>` the commit moving `last-audit`, each exits 0.
  Red when: a watched file moves after the re-stamp.
- **AC19** — When a full `maintain.py` run over a fixture with a live ask carrying a marker ends,
  `git status --porcelain` prints what it printed before the run.
  Red when: the walk leaves a `BACKLOG.md` row edited.
- **AC20** — When `python maintenance.py write` runs with empty stdin, with `not json`, and with
  `{"fields": {}}`, it exits 2 each time; a 70 KiB readings set re-derived at its base lands with every
  `over-pin:` line.
  Red when: a capped or malformed payload writes a record.
- **AC21** — When `resolve_reading_tree` runs with a directory already at a dead pid's path, it prunes
  it, adds its own `<sha12>.<pid>` tree, and `git grep -n "worktree add" tools/drift-audit/*.py` matches
  only `add_detached_worktree`.
  Red when: a stale path wedges the reading, or a second copy adds a tree.
- **AC22** — When `measure_idle_processes` reads a planted sweep report naming two flagged rows, it
  returns two detail rows keyed without `winpid`, and a target that survives a stub reap is filed
  under its key.
  Red when: a reap reads `fixed` while a target survives.
- **AC23** — When a stub `file` body raises on the first run and the walk re-runs under the same key,
  the recording filer holds one receipt per offender.
  Red when: a re-run re-files a completed item.
- **AC24** — When `scan_annotations` runs over a fixture with an uncommitted edit to a note line, it
  reports that line's committed sha.
  Red when: the blame reports `0000000`.
- **AC25** — When `python security_review.py file --return <json>` files one finding re-reported at a
  shifted line, and two findings at one line, it records one key for the first and two for the second.
  Red when: a moved line files a second ask, or two findings fold.
- **AC26** — When `check_reading_rows` reads the `standing_directives_not_promoted` row, it carries no
  `kind` and `derive_reading_owner` answers `layer.runtime`.
  Red when: the row names a kind no unit declares.
- **AC27** — When `grep -c "maintain.md" help/README.md` runs, it prints 1.
  Red when: the page is unindexed.
- **AC28** — When `python maintain_file.py route` runs with the policy kit absent, the EOL breach's
  route is `file` with one `NOTE:` line.
  Red when: the refused read prints `not asked`.
- **AC29** — When `grep -n -i "the ten\|ten declared\|one of the ten" tools/roles` runs, it prints
  nothing.
  Red when: a spelled count survives the eleventh entry.
- **AC30** — When `git show "f4597719:$p" | sed -n 4427,4438p` runs with `p` set to
  `tools/drift-audit/drift_report.py`, it prints the `OVER PIN` and `over pin` status lines, and
  `ls memory/map/features/*.md | wc -l` prints 32 at base.
  Red when: either citation points at other lines or another count.
  figure: 32 is DERIVED by the listing at base.

## 7. Gates

`drift-audit selftest` · `drift-audit records` · `policy fixtures` · `check-wiring self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `method carriers (every pointer declared)` · `codebase-map coverage + freshness` · `kickoff-manifest ratchet` · `unattended skill size` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 AC3 AC5 AC6 AC8 AC10 AC11 AC12 AC13 AC14 AC19 AC20 AC21 AC22 AC23 AC24 AC25 AC26 AC28 · one plant per item over the fixtures its landing unit's arm builds, staged against each unit's text as the audit read it · none

## 8. Open questions

- **F1 — Where does a live ask's recurrence go (id 44)?** Options: (a) a receipt of the re-filed
  stable text, writing no `BACKLOG.md` row; (b) the `seen` clause carried by a records-only patch
  intake that lands it. (b) adds a patch build per recurrence per period and a period inside an intake
  text, which id 42's fix forbids. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the report's
  own second option and the one that leaves the walk no tracked write. widens: none · relaxes: none
- **F2 — What re-run contract holds a hand-over (id 51)?** Options: (a) a node-local journal of
  completed items under the git common dir; (b) a receipt keyed by period in `intake.py`. (b) changes
  an ancestor's interface. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, with (b) named in §3
  as the cross-node upgrade. widens: none · relaxes: none
- **F3 — Pin 0 or the measured pin for `live_builds_without_activity` (id 13)?** Options: (a) pin 0,
  an exception to unit 4 S5; (b) act only past the measured pin. (b) leaves the 22 builds dormant at
  base unproposed (`memory/LIVE.md`, PINNED by the finding's skeptic). RESOLVED (agent, 2026-11-01,
  delegated): (a), rung 3, the option that proposes every dormant build. widens: none · relaxes: none

- **F4 — Where do the band and the probe go once they leave the hashed text (id 10)?** Options: (a)
  the period's maintenance record, a `Band` column and `probe:` lines; (b) the intake receipt, whose
  fields are fixed by TOOL-dWellOiledMachine-27 S1 (`origin=cadence filer=<item tag>`, `received-utc`,
  `redacted`) and carry no data; (c) the ask's `seen` clause, which S23 no longer writes. RESOLVED
  (agent, 2026-11-01, delegated): (a), rung 3, the one survivor that keeps both facts on a committed
  record. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from the 30 MEDIUM and 10 LOW of the round-1 spec
  audit, one scope item per raw id.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 spec audit of units 35 to 48 declare toward this unit (units 49, 50, 51, 52, 58 and 59); no scope, design or criterion moved.

## 10. Reuse audit

Every item extends a seam its landing unit already names; the two minted names reuse existing ones.
`python tools/codebase-map/reuse_lookup.py "add a detached scratch worktree and remove it on exit"`
ranked `add_scratch_worktree` (`tools/run-gates/lib-attribute.sh`, fan-in 3, a SEAM), whose argv
`add_detached_worktree` runs, so S40 factors the Python half once rather than writing a second.
`python tools/codebase-map/reuse_lookup.py "find an ask carrying a marker and whether it is closed"`
ranked the shell helpers `ask_filed_in` and `asks_filed_in`, which answer filing and not state, so S23
keeps unit 15's own search.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch maintenance record key grammar over-pin"`
