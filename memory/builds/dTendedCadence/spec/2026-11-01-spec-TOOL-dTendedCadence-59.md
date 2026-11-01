# TOOL-dTendedCadence-59 — the round-1 spec audit of units 35 to 48, its 40 minors batched: one landing grammar for every family, ask texts that stay their own, a scaffold that unwires the old hook, criteria with lower bounds, and the prose the siblings miscite

**Status:** OPEN · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 22 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |
| [2026-11-01-prompt-TOOL-dTendedCadence-49-promoted-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-49-promoted-fix-brief.md) | research | TOOL-dTendedCadence-49 |
| [2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md) | spec-audit | TOOL-dTendedCadence-56 TOOL-dTendedCadence-55 TOOL-dTendedCadence-57 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-58 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 35 to 48,
`reviews/2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md`, confirmed 50 findings,
and TOOL-dTendedCadence-49 to -58 take its 5 BLOCKER and 5 HIGH. This unit is BUILD-METHOD M4's batch
of its 19 MEDIUM and 21 LOW by raw id, one scope item per id, in report order, M1 to M16 and then L1
to L18. They land on twelve of the fourteen audited units and on four units of the first round, so
it repairs no unit in particular and builds last, order 22, above every unit of the build. They do not
split into two disjoint write sets: almost every item writes `tools/drift-audit/selftest.py`, so one
unit carries them all.

Every id: M1 5, 24; M2 6, 29; M3 19, 50; M4 7; M5 8; M6 30; M7 31; M8 33; M9 34; M10 41; M11 44; M12
45; M13 46; M14 47; M15 48; M16 49; L1 3; L2 9; L3 10, 36; L4 11; L5 12; L6 13, 51; L7 14; L8 20;
L9 21, 53; L10 22; L11 23; L12 25; L13 26; L14 27; L15 37; L16 38; L17 39; L18 52.

A correction to a sibling spec's prose is made in that spec's text, a rev bump with a §9 line naming
the review id, in this unit's build pass, whatever the sibling's status by then: the report asks for
the text itself (its item L2), and a correction no file carries is observed by nothing.

## 2. Scope (IN)

- **S1** — id 5, M1, landing on unit 39. The maintenance record section of `tools/drift-audit/README.md`
  states one landing grammar for every family, TOOL-dTendedCadence-49's four lines, and that a
  `security-` landing's payload is the review's written record, its digest over that record's bytes,
  with no readings and no re-derivation. Observed by AC1.
- **S2** — id 24, M1, landing on units 39 and 48. One drift-audit selftest case lands one record of
  every `RECORD_KEY_FAMILIES` row through `write_record_landing` and `maintenance.py land`
  (TOOL-dTendedCadence-49, -50), the population read from the table at run time. Observed by AC2.
- **S3** — id 6, M2, landing on units 48 and 47. Unit 48 S23's live-ask recurrence re-files the live
  ask's own text: where the ask `read_marker_ask` (S35) answers carries `· regressed after <id>` in its
  TEXT, step (1)'s re-filed text carries that clause, so the receipt lands on the live ask's own
  intake. Observed by AC3.
- **S4** — id 29, M2, the same defect observed: unit 47 AC2's fixture gains an OPEN ask whose text
  carries `regressed after A`, and the closed ask A's intake gains no receipt. Observed by AC4.
- **S5** — id 19, M3, landing on unit 41. `adopt-drift-audit.sh --scaffold` unwires the node-launched
  SessionStart entry unit 2 merged before it merges unit 41's fragment, so a repository merged under
  unit 2 ends with one maintain-session entry. Unit 41 §5's migration line is corrected in place.
  Observed by AC5.
- **S6** — id 50, M3, the unwire's join: `python <prefix>/settings-merge.py --unwire --fragment
  <scratch fragment>`, the scratch fragment unit 41's with `marker` set to `maintain_session.py` and
  `hook_path` to `{kit}/drift-audit/maintain_session.py`, so `check_ours`'s join of marker and
  basename (`tools/settings-merge.py:393-400`) matches the node entry and nothing else, and an absent
  entry is exit 0 (`:32-34`). Observed by AC6.
- **S7** — id 7, M4, landing on unit 48. The walk's order is the order `order_by_needs` derives from
  the kit's `[[item]]` rows, `item.maintain.direct` included between read and patch, and unit 48 AC2's
  observation is made with the expected order derived from those rows, never typed. Observed by AC7.
- **S8** — id 8, M5, landing on unit 48. The one-adapter rule is observed with a lower bound: an `ast`
  probe over `tools/drift-audit/*.py` finds every call whose argument list holds a string ending
  `policy.py`, at least one, every one inside `read_policy_value`. Observed by AC8.
- **S9** — id 30, M6, landing on units 41 and 48. The re-keyed hook, `SessionStart
  tools/drift-audit/maintain-session.sh`, is claimed by the dossier of S29, no dossier names the
  `.py` hook, and `memory/map/generated/` is re-rendered. Unit 41's §4 Files touched gains
  `memory/map/`, and its §7 the `codebase-map coverage + freshness` leg, in place. Observed by AC9.
- **S10** — id 31, M7, landing on unit 48. Unit 48's §7 leg line gains `unattended skill wiring`,
  `unattended kit gate`, `roles catalogue`, `roles render wiring` and `drift-audit wiring`, the legs
  its S11, S18 and S37 edits trip, in place. Observed by AC10.
- **S11** — id 33, M8, landing on unit 48. The roles kit's spelled-count criterion reads files:
  `git grep -n -i "the ten\|ten declared\|one of the ten" -- tools/roles` exits 1 printing nothing,
  where at base it prints five lines (`README.md:4`, `:275`, `check_roles.py:31`, `workflows.toml:1`,
  `:4`, PINNED 2026-11-01 by that command). Observed by AC11.
- **S12** — id 34, M9, landing on unit 48. The manifest criterion reads the `watch:` value of
  `memory/guides/SESSION-KICKOFF.md` and tests every commit touching any of its pathspecs, over
  TOOL-dTendedCadence-58's population and the prepared merge. Because a mint moves
  `tools/memory-tree/check-memory-hygiene.sh` inside the prepared merge and re-stamps nothing
  (`tools/push-main.sh:26-31`), the build's last commit after the last `--prepare` re-stamps
  `last-audit` when the prepared merge moved a watched path. Observed by AC12.
- **S13** — id 41, M10, landing on units 44, 45 and 8. `write_patch_intake` answers `seen`, filing
  nothing, when `read_caused_by_build` (TOOL-dTendedCadence-53 S1) finds the key's build in any status
  but CLOSED or WONTDO; a committed README is seen by every node, so a second node files no second
  intake for an open target. Observed by AC13.
- **S14** — id 44, M11, landing on unit 48. A scratch tree's liveness is a lock, never a pid probe:
  the run holds an exclusive lock on `<tree>.lock` (`fcntl.flock` on POSIX, `msvcrt.locking` on
  Windows) while the tree lives, a prune removes only a tree whose lock it acquires, and a lock error
  other than contention counts as alive. No `os.kill` probe is written. Observed by AC14.
  **Readers:** by name: `2026-11-01-spec-TOOL-dTendedCadence-48.md`, S25 and AC21, the only text
  that spells the pid-alive prune this item replaces; READER NOT IN TREE for `resolve_reading_tree`,
  which unit 48 has not built yet, so no code at HEAD reads the pid probe.
  by value: NO VALUE READERS — the probe's alive-or-dead answer only gates the prune in the same
  call and is never written anywhere.
- **S15** — id 45, M12, landing on unit 48. The re-run journal: `--dry-run` neither reads nor writes
  it; `item.maintain.file` appends one line per filed offender, `<item tag>\t<key hash>` and a newline
  in one write, and a re-run skips the offenders on record; a last line without its newline is
  ignored. Observed by AC15.
- **S16** — id 46, M13, landing on unit 47. A failed generator read in step (1) or in unit 47 S1
  prints its line and exits 1, filing nothing, so the lease is handed over. Unit 47 §5's fallback is
  not built. Observed by AC16.
- **S17** — id 47, M14, landing on unit 47. A WONTDO ask carrying the marker is a decline: the breach
  files nothing and prints `file — <reading> · key <key hash> · declined <ask id>`; only a CLOSED ask
  is re-filed as a regression. Observed by AC17.
- **S18** — id 48, M15, landing on unit 46. `item.maintain.direct`'s row gains `survivor`, routed to
  `item.maintain.file`, and `run_dormant_fix` hands a `survivor` answer on as unit 8 S7 does.
  Observed by AC18.
- **S19** — id 49, M16, landing on unit 43. `read_breach_records` (TOOL-dTendedCadence-55 S1) also
  returns every event record committed after the newest period record, and the leg counts distinct
  `over-pin:` lines across them. Observed by AC19.
- **S20** — id 3, L1, landing on unit 37. `maintenance.py write` refuses a reading object carrying a
  `signal` member, a raw `--readings` record, naming it, and the README states that the stdin
  `route` is the walk's outcome while `--readings`' `route` is the row's declared route. Observed by
  AC20.
- **S21** — id 9, L2, landing on unit 48. The two corrections unit 48 S38 and S39 state are made in
  place: unit 15's citations of the over-pin status lines (spec-15:24, :156) read
  `drift_report.py:4427-4438`, and unit 5's rejected alternative (spec-5:140) reads 32 dossiers.
  Observed by AC21.
- **S22** — id 10, L3, landing on unit 35. The refusal line renders its family list from
  `RECORD_KEY_FAMILIES`' rows in table order, and unit 35 S2 and AC2 read "every family of the table"
  in place. Observed by AC22.
- **S23** — id 36, L3, landing on unit 39. The README's maintenance record section names every
  family, `security` among them, and unit 39's §4 Files touched lists `tools/drift-audit/README.md`
  in place. Observed by AC23.
- **S24** — id 11, L4, landing on unit 35. Unit 35 §4's `node` row escapes its pipe as `\|`, in place.
  Observed by AC24.
- **S25** — id 12, L5, landing on unit 38. `gen_build_index.py` escapes each `|` of a unit's title as
  `\|` in the build-units row it renders (`tools/memory-tree/gen_build_index.py:1564-1567`), so unit
  38's row keeps six cells. Observed by AC25.
- **S26** — id 13, L6, landing on unit 41. The shim forwards its own argv verbatim, `"$@"`, to
  `maintain_session.py`, and the merged command passes none; unit 41 §5's security line is corrected
  in place. Observed by AC26.
- **S27** — id 51, L6, the same defect's other half: the shim takes no argument from the payload, so a
  session id shaped like a flag reaches python on stdin only. Observed by AC27.
- **S28** — id 14, L7, landing on unit 48. A `probe:` line is parsed as its three values: the reading
  before the first TAB, the probe record after the last TAB, and the offender key between them, TAB
  included. Observed by AC28.
- **S29** — id 20, L8, landing on unit 48. A new dossier, `memory/map/features/drift-audit.md`,
  carries `tools/drift-audit/` in its `[paths]` and claims the leg `maintain breach record` and the
  hook of S9; unit 48 S21's sentence on the kickoff dossier is corrected in place. Observed by AC29.
- **S30** — id 21, L9, landing on unit 35. Every `RECORD_KEY_FAMILIES` pattern is compiled with
  `re.ASCII`. Observed by AC30.
- **S31** — id 53, L9, the same defect's cases: unit 35 AC2's refused keys gain an Arabic-Indic and
  a full-width date. Observed by AC30.
- **S32** — id 22, L10, landing on unit 41. Unit 41 §4 Evidence reads "one of three fragments that
  do", naming `skills/session-kickoff/orientation-card.fragment.json` and
  `orientation-replay.fragment.json`, in place. Observed by AC31.
- **S33** — id 23, L11, landing on unit 38. Unit 38 §1 cites spec-8 :131 and :156 and spec-17 :288, in
  place. Observed by AC31.
- **S34** — id 25, L12, landing on unit 48. The journal of S15 carries a `ponytail:` comment naming
  `position.py` keyed by (cadence, period), ask TOOL-dTendedCadence-28, as its upgrade, and unit 48 §8
  F2 cites that ask, in place. Observed by AC32.
- **S35** — id 26, L13, landing on unit 47. `read_marker_ask(root, key_hash)` in `maintain_file.py`
  answers `(ask_id, state, text)` for the newest ask carrying the marker, from one `gen_build_index.py
  --asks --build <home> --all` call, or None; step (1) and unit 47 S1 branch on its state, and
  `read_closed_marker_ask` is not built. Observed by AC33.
- **S36** — id 27, L14, landing on unit 41. Unit 41 §5's migration line names the real join, marker
  and basename, and points at S5, in place. Observed by AC34.
- **S37** — id 37, L15, landing on unit 48. The version criterion covers every carrier: each
  `version_from` `file` and `pattern` the kits' `kit.toml` rows declare, graded over
  TOOL-dTendedCadence-58's population; and `.claude/skills/unattended/SKILL.md` measures the base's
  10237 bytes less S18's 3. Observed by AC35.
- **S38** — id 38, L16, landing on units 36, 43, 45, 46 and 47. `help/maintain.md` holds each section
  those units' user-docs lines edit, each naming its unit's fact, and each unit's §4 Files touched
  lists `help/maintain.md`, in place. Observed by AC36.
- **S39** — id 39, L17, landing on unit 48. Unit 6's stdin carries `readings[].band` and
  `fields.probe`, a list of `[reading, offender key, probe record]`; the README's record section and
  unit 48's §4 Inventory name the `Band` column and the `probe:` line, the latter in place. Observed
  by AC37.
- **S40** — id 52, L18, landing on unit 42. The adopter-instruction criterion reads each numbered
  step and paragraph of `WIRE-INTO-PROJECT.md` and `tools/drift-audit/README.md` as one unit, its
  continuation lines joined, so a rewrap cannot split the two names. Observed by AC38.

## 3. Non-goals (OUT)

- Every BLOCKER and HIGH: TOOL-dTendedCadence-49 to -58.
- The left-shift gates the report names beside each minor: each is a gate of its own, outside the one
  mechanism M4 admits for this batch.
- Re-reviewing a sibling spec corrected in place: a correction moves the cited prose and nothing
  else.

### Edges

- **consumes-from** `TOOL-dTendedCadence-35` — the family table's refusal line, its `\d` patterns and the `node` row (S22, S24, S30, S31)
- **consumes-from** `TOOL-dTendedCadence-37` — the stdin `route` the writer reads (S20)
- **consumes-from** `TOOL-dTendedCadence-38` — the title and §1 citations (S25, S33)
- **consumes-from** `TOOL-dTendedCadence-39` — the security landing and its README (S1, S2, S23)
- **consumes-from** `TOOL-dTendedCadence-41` — the shim, the migration and the map key (S5, S6, S9, S26, S27, S32, S36)
- **consumes-from** `TOOL-dTendedCadence-42` — the adopter-instruction criterion (S40)
- **consumes-from** `TOOL-dTendedCadence-43` — the leg's event records (S19)
- **consumes-from** `TOOL-dTendedCadence-44` — the sweep's cross-node dedupe (S13)
- **consumes-from** `TOOL-dTendedCadence-45` — the repeat intake's cross-node dedupe (S13)
- **consumes-from** `TOOL-dTendedCadence-46` — the direct row's `survivor` (S18)
- **consumes-from** `TOOL-dTendedCadence-47` — the marker reader, the failure path and the decline (S3, S4, S16, S17, S35)
- **consumes-from** `TOOL-dTendedCadence-48` — its criteria, scratch tree, journal, `probe:` line, dossier and §7 (S7 to S12, S14, S15, S21, S28, S29, S34, S37, S39)
- **consumes-from** `TOOL-dTendedCadence-5` — the rejected alternative's dossier count (S21)
- **consumes-from** `TOOL-dTendedCadence-8` — `write_patch_intake`'s `seen` answer (S13)
- **consumes-from** `TOOL-dTendedCadence-15` — the over-pin status citations (S21)
- **consumes-from** `TOOL-dTendedCadence-49` — `write_record_landing`, through which every family lands (S1, S2)
- **consumes-from** `TOOL-dTendedCadence-50` — `maintenance.py land`, the verb every family lands by (S2)
- **consumes-from** `TOOL-dTendedCadence-53` — `read_caused_by_build`, the committed source the dedupe reads (S13)
- **consumes-from** `TOOL-dTendedCadence-55` — `read_breach_records`, whose population S19 extends
- **consumes-from** `TOOL-dTendedCadence-58` — the population of the build's own commits (S12, S37)
- **consumes-from** `TOOL-dTendedCadence-36` — the help section and Files touched line of its docs edit (S38)
- **hands-off** `TOOL-dTendedCadence-72` — S37 and AC35, whose carrier population that unit reads from govkit's registry (review id 24)
- **hands-off** `TOOL-dTendedCadence-73` — S11 and AC11, whose grep that unit widens to every file spelling a role count (review id 29)
- **hands-off** `TOOL-dTendedCadence-74` — S13, S14, S28, S33, AC34, AC35, AC36 and Files touched, repaired by the minors batch (review ids 6, 43, 44, 12, 8, 9, 33, 7, 34)

## 4. Design

### Evidence

Each item's finding, its cited lines and its skeptic verdict are the report's, by id; ids 5 and 50
carry the skeptic's corrected fix, which S1 and S6 take, and id 46's corrected fix is S16. Read at base
for this unit: `tools/settings-merge.py:32-34` and `:393-400` (the unwire and the join),
`tools/run-gates/measure_legs.py:1465-1495` (a pid alone is not proof), `memory/map/features/session-kickoff.md:10-14`
(its claims), `memory/map/baseline.toml:21-23` (drift-audit's legs, grandfathered), the five roles
lines of S11, `memory/guides/SESSION-KICKOFF.md:6` (the `watch:` line, eleven pathspecs),
`.claude/skills/unattended/SKILL.md` at 10237 bytes against `tools/template-size-limits.txt:154`'s
10240 (PINNED 2026-11-01 by `wc -c`), and the sixteen `version_from` rows naming a `file` in
`tools/*/kit.toml` (DERIVED by `git grep -h "^version_from = { file" -- 'tools/*/kit.toml'`).

### Why a lock and not the pid probe

`read_process_created` (`tools/run-gates/measure_legs.py:1474`) proves a Windows owner dead by
`OpenProcess` and creation time through `ctypes`, and lives in run-gates, which a copy-installed
drift-audit cannot import. A held lock is released by the operating system when its holder exits, so
it answers "alive" with no pid at all, which closes both the pid-reuse case and the MSYS pid
namespace (`tools/process-monitor/reap.py:228-238`) in stdlib on both platforms.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `read_marker_ask` | function, `maintain_file.py` | `py.function`, OK by `lexicon.py --suggest` at writing |
| `declined` | breach route line word | none |
| `<tree>.lock` | lock file beside a scratch tree | none |
| `drift-audit` | codebase-map feature dossier | none |

### Files touched (estimate)

- `tools/drift-audit/maintenance.py`: S20, S22, S28, S30, S39
- `tools/drift-audit/maintain.py`: S15, S34
- `tools/drift-audit/maintain_file.py`: S3, S16, S17, S19, S35
- `tools/drift-audit/readings.py`: S13
- `tools/drift-audit/drift_report.py`: S14
- `tools/drift-audit/kit.toml`: S18
- `tools/drift-audit/adopt-drift-audit.sh`: S5, S6
- `tools/drift-audit/maintain-session.sh`: S26, S27
- `tools/drift-audit/README.md`: S1, S20, S23, S39
- `tools/drift-audit/selftest.py`: the arm of §7
- `tools/memory-tree/gen_build_index.py`: S25
- `memory/map/features/drift-audit.md` (new) and `memory/map/generated/`: S9, S29
- `help/maintain.md`: S38
- `memory/builds/dTendedCadence/spec/`: the in-place corrections of S5, S9, S10, S21 to S24, S26,
  S29, S32 to S34, S36, S38 and S39

## 5. Production-readiness checklist

- security — S6's unwire removes only an entry carrying both the old marker and the old basename; S14
  never signals a process; S27 keeps the payload off argv.
- perf / scale — S13 adds one `git grep -F` per filing; S2 lands one record per family in the arm.
- error / empty / loading states — S16 exits 1 on a failed read; S15 ignores a torn last line; S20
  refuses a raw `--readings` record by name.
- observability — S17 prints `declined`; S19's offender lines name their record.
- risks — an in-place correction to a terminal sibling moves prose only, never its status or scope;
  S13's committed source sees a build only once its README lands, so two nodes filing in the same
  minute can still file twice, the receipt dedupe's case.
- testing — the criteria of §6, in the arms of §7.
- migration — S5 and S6 migrate a repository merged under unit 2; nothing else exists at base.
- user docs — `help/maintain.md`, S38.

## 6. Acceptance criteria

The fixtures are the landing units' own, named by each criterion; the walk fixture is unit 1's.

- **AC1** — When `grep -n "land maintenance-record" README.md` runs in `tools/drift-audit/`, it prints
  one line, and the same section matches `grep -c "security-"`.
  Red when: the README names a second landing grammar, or none for the security family.
- **AC2** — When the every-family case runs, it lands one record per row of `RECORD_KEY_FAMILIES`,
  their count equal to the table's and at least six, each `land` exiting 0.
  Red when: a family's landing is refused, or the table reads empty.
- **AC3** — When `python maintain_file.py route` runs a breach whose live OPEN ask's text carries `·
  regressed after A`, with a recording filer, the recorded text is byte-equal to that ask's text.
  Red when: the re-filed text drops the clause.
- **AC4** — When the same run files into a scratch intake store holding A's intake and the live
  ask's, the receipt lands on the live ask's intake and A's receipt count is unchanged:
  `python intake.py show <key>` prints one receipt more for the live ask's key and the same count
  for A's.
  Red when: a live regressed ask's recurrence lands on the closed ask's intake.
- **AC5** — When `bash adopt-drift-audit.sh --scaffold` runs in a scratch repository whose
  `.claude/settings.json` carries unit 2's `node ".../maintain_session.py"` entry, `grep -c
  'maintain_session.py\|maintain-session.sh' .claude/settings.json` prints 1 and that line names
  `bash`.
  Red when: the stale node entry survives beside the new one.
- **AC6** — When `--scaffold` runs a second time, and over a settings file holding a foreign
  SessionStart entry, the second run changes nothing and the foreign entry is kept.
  Red when: the unwire removes an entry it does not own, or the migration is not idempotent.
- **AC7** — When `GOV_CADENCE_KEY=2026-11-01 python maintain.py --dry-run` runs over unit 1's fixture
  with unit 3's row, the item lines' order equals `order_by_needs` over the fixture's rows, and
  `item.maintain.direct` prints between read and patch.
  Red when: the criterion's order is typed and a correct walk fails it.
- **AC8** — When the `ast` probe of S8 runs, it prints a count of at least 1 and every call it names
  sits inside `read_policy_value`; with a second adapter staged whose argv spans two lines, it names
  that call.
  Red when: the probe prints 0 and passes, or misses a split argv.
- **AC9** — When `grep -l "SessionStart .*/maintain-session\.sh"
  memory/map/features/*.md` runs, it names `drift-audit.md` alone, and `grep -l "maintain_session.py"
  memory/map/features/*.md` prints nothing.
  Red when: the re-keyed hook is unclaimed, or a dossier claims the old key.
- **AC10** — When `grep -n "roles render wiring" 2026-11-01-spec-TOOL-dTendedCadence-48.md` runs in
  the spec folder, it matches on the §7 leg line beside the four other legs S10 names.
  Red when: a leg its edits trip is missing from unit 48's §7.
- **AC11** — When `git grep -n -i "the ten\|ten declared\|one of the ten" -- tools/roles` runs, it
  exits 1 and prints nothing.
  Red when: a spelled count survives the eleventh entry.
  figure: the five hits at base are PINNED 2026-11-01.
- **AC12** — When the `watch:` value is read from `memory/guides/SESSION-KICKOFF.md` and each commit
  of TOOL-dTendedCadence-58's population and the prepared merge touching one of its pathspecs is
  passed to `git merge-base --is-ancestor <c> <restamp>`, each exits 0, and the pathspecs read number
  at least eleven.
  Red when: a watched file moves after the re-stamp, or the watch list is typed.
  figure: eleven is DERIVED from the line at base.
- **AC13** — When two runs on two scratch intake stores file one target and the fixture commits an
  OPEN build README naming its key, the second run prints `seen` and its store holds no intake.
  Red when: a second node files a second intake for an open target.
- **AC14** — When `resolve_reading_tree` prunes beside a tree whose lock a live sibling process
  holds, the tree survives and the sibling still runs; a tree whose holder exited is pruned; and `git
  grep -n "os.kill" -- tools/drift-audit/` prints nothing.
  Red when: a live run's tree is pruned, or a dead one wedges the reading.
- **AC15** — When a stub `file` body raises after the first of two filings and the walk re-runs under
  the same key, the recording filer holds one receipt per offender; a `--dry-run` run first leaves
  the real run filing both; a journal whose last line lacks its newline resumes at the line before.
  Red when: a re-run re-files an offender, or a dry run skips a real one.
- **AC16** — When the generator is replaced by a stub exiting 1 with a CLOSED marker ask planted,
  `python maintain_file.py route` exits 1 and never prints `seen`.
  Red when: a failed read absorbs the regression.
- **AC17** — When the marker's only ask reads WONTDO, the run prints `declined <that id>` and the
  recording filer records nothing.
  Red when: a decline is re-filed as a regression.
- **AC18** — When a CLOSED disposal build is planted for a slug that still reads dormant,
  `GOV_CADENCE_KEY=2026-11-01 python maintain.py --dry-run` routes that slug to
  `item.maintain.file`.
  Red when: the `survivor` answer has no route.
- **AC19** — When unit 55's worktree commits a clean period record and then an event record carrying
  one `over-pin:` line, `python maintain_file.py leg` exits 1; with the event record committed before
  the period record it exits 0.
  Red when: a newer event record's hold is unread, or an older one is counted.
- **AC20** — When `python maintenance.py write` runs with a reading carrying `signal` in place of
  `reading`, it exits 2 naming a `--readings` record, and `grep -n "declared route" README.md` matches
  in `tools/drift-audit/`.
  Red when: a raw `--readings` object is written or refused without its name.
- **AC21** — When `grep -c "4427-4438"` runs over spec 15 and `grep -n "32 dossiers"` over spec 5 in
  the spec folder, the first prints 2 and the second matches.
  Red when: either correction is in no file.
- **AC22** — When `python maintenance.py write --key ../x` runs with the `security` row present, its
  refusal line names six families, `security` last.
  Red when: the line is typed and misses a family.
- **AC23** — When `grep -n "security-\[0-9a-f\]{12}\|security-<head12>" README.md` runs in
  `tools/drift-audit/`, it matches.
  Red when: the README names five families.
- **AC24** — When the `node` row of spec 35's families table is split on pipes not preceded by a
  backslash, it yields three cells.
  Red when: the pattern's pipe splits the cell.
- **AC25** — When the build-units row of TOOL-dTendedCadence-38 in the build README, rendered by
  `gen_build_index.py --write`, is split on pipes not preceded by a backslash, it yields six cells.
  Red when: a title's pipe shifts the Order, Tier and Status cells.
- **AC26** — When `bash maintain-session.sh --dry-run` runs in `tools/drift-audit/` with a
  SessionStart payload on stdin, it prints unit 2 S6's dry-run output and exits 0.
  Red when: the shim drops its argv.
- **AC27** — When the shim runs with a stub hook that prints its argv and a payload whose session id
  is `--x`, the stub prints no argument.
  Red when: a payload value reaches argv.
- **AC28** — When a planted line `probe: rA<TAB>rA<TAB>detail-key<TAB>probe-7` is parsed, it yields
  the reading `rA`, the offender key `rA<TAB>detail-key` and the probe record `probe-7`.
  Red when: a fixed-count split takes the detail key as the probe record.
- **AC29** — When `grep -l "maintain breach record" memory/map/features/*.md` runs, it names
  `drift-audit.md` alone.
  Red when: the leg is claimed by the kickoff dossier or by none.
- **AC30** — When `python maintenance.py write` runs with `--key ٢٠٢٦-١١-٠١` and with `--key
  ２０２６-１１-０１`, it exits 2 each time and writes nothing.
  Red when: a non-ASCII digit key is admitted.
- **AC31** — When `grep -n "one of three fragments"` runs over spec 41 and `grep -n ":131, :156"` over
  spec 38 in the spec folder, each matches.
  Red when: a miscount or miscitation is in no corrected file.
- **AC32** — When `grep -n "ponytail:.*position.py" maintain.py` runs in `tools/drift-audit/`, it
  matches, and `grep -n "TOOL-dTendedCadence-28"` over spec 48's §8 matches.
  Red when: the journal states no upgrade.
- **AC33** — When a marker is carried by an older CLOSED ask and a newer OPEN one, `python
  maintain_file.py route` prints `seen`, and `grep -c "gen_build_index.py" maintain_file.py` prints 1.
  Red when: two readers disagree on "the" ask, or a second generator call exists.
- **AC34** — When `grep -n "by name" 2026-11-01-spec-TOOL-dTendedCadence-41.md` runs in the spec
  folder, it prints nothing.
  Red when: the migration prose still cites a name join.
- **AC35** — When each `version_from` row is read from `tools/*/kit.toml` and its carrier's added
  lines matching its `pattern` are listed over TOOL-dTendedCadence-58's population, none is listed,
  over a population of at least sixteen carriers; and `wc -c .claude/skills/unattended/SKILL.md`
  prints 10234.
  Red when: a hand-bump in an unlisted kit passes, or the Skill's fall is not observed.
  figure: sixteen is DERIVED from the rows naming a `file` at base; 10234 is DERIVED from the pinned
  10237 less S18's 3.
- **AC36** — When `grep -n "^## " maintain.md` runs in `help/`, it lists "The Maintain run",
  "When a reading breaches its pin", "Cyclic playbooks" and "The safe fixes", and
  `grep -c "help/maintain.md"` over each of specs 36, 43, 45, 46 and 47 counts its Files touched line.
  Red when: a unit's docs edit was dropped.
- **AC37** — When `python maintenance.py write` runs with a reading carrying `band` `diagnose` and
  `fields.probe` holding one triple, the record's Readings table carries `diagnose` in its `Band`
  cell and one `probe:` line.
  Red when: the band or the probe is recorded nowhere.
- **AC38** — When the S40 probe joins each list item's continuation lines in `WIRE-INTO-PROJECT.md`
  and `tools/drift-audit/README.md`, no item names both `drift_signals.py` and `PRODUCT_GLOBS`, and
  the item naming `PRODUCT_GLOBS` names `flow_layer.py`; with step 3 rewrapped to split the two names,
  it still reports the planted pair.
  Red when: a rewrap hides a stale instruction.

## 7. Gates

`drift-audit selftest` · `drift-audit wiring` · `policy fixtures` · `tier2-review self-test` · `build-index selftest` · `settings-merge selftest` · `codebase-map coverage + freshness` · `kickoff-manifest ratchet` · `unattended skill size` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC13 AC14 AC15 AC16 AC17 AC18 AC19 AC20 AC22 AC26 AC27 AC28 AC30 AC33 AC37 AC38 · one plant per item over the fixtures its landing unit's arm builds, staged against each unit's text as the audit read it · none

New arm: tools/memory-tree/gen_build_index.py · covers AC25 · a planted unit whose title carries a code-span pipe, staged against the unescaped label · none

## 8. Open questions

- **F1 — Liveness of a scratch tree (id 44): reuse the pid probe, or a lock?** Options: (a) a lock
  beside the tree; (b) `read_process_created` with an owner file; (c) `os.kill(pid, 0)`. (c) kills a
  live process on Windows. (b) is `ctypes` code in run-gates, which a copy-installed kit cannot
  import, and its port is Windows-only. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, stdlib
  on both platforms and free of pid reuse. widens: none · relaxes: none
- **F2 — A partially filed item on a re-run (id 45)?** Options: (a) a journal line per filed
  offender; (b) the item re-files whole and the receipt dedupe absorbs it. (b) is the second receipt
  unit 48 AC23 forbids. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3. widens: none · relaxes:
  none
- **F3 — A WONTDO ask (id 47)?** Options: (a) a decline, printed and filed nowhere; (b) a regression,
  as unit 47 S1 reads it. (b) answers every owner decline with a fresh ask. RESOLVED (agent,
  2026-11-01, delegated): (a), rung 3, the report's fix. widens: none · relaxes: none
- **F4 — The table pipe in a unit's title (id 12)?** Options: (a) the generator escapes it; (b) unit
  38's title spells the set in words. (b) fixes one title and leaves the class; (a) fixes every
  rendered title. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the report's left-shift form.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from the 19 MEDIUM and 21 LOW of the round-1 spec audit
  of units 35 to 48, one scope item per raw id.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 spec audit of units 49 to 59 declare toward this unit (units 72, 73, 74); no scope, design or criterion moved.

## 10. Reuse audit

Every item extends a seam its landing unit already names: units 49 and 50's landing for S1 and S2,
unit 53's `read_caused_by_build` for S13, unit 55's `read_breach_records` for S19, unit 58's
population for S12 and S37, and `settings-merge.py --unwire` for S6. `python
tools/codebase-map/reuse_lookup.py "find an ask carrying a marker and whether it is closed"` ranked
the shell helpers `ask_filed_in` and `asks_filed_in`, which answer filing and not state, so S35's
reader is one Python function over the generator. `python tools/codebase-map/reuse_lookup.py "tell
whether the process holding a scratch tree is still alive"` ranked `add_scratch_worktree`
(`tools/run-gates/lib-attribute.sh`) and `check_pid_alive` (`tools/unattended/lib-unattended.sh`),
both shell, the second a pid, image and start-time probe a copy-installed Python kit cannot call; §4
records why `read_process_created`, the Python form, is not reused either.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch maintenance record key grammar over-pin"`
