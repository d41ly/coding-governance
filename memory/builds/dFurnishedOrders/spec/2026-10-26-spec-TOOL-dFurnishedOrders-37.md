# TOOL-dFurnishedOrders-37 — the second spec audit's 37 minors: readers that tell a missing input from an empty one, one bounded runner, the retired-key scan's shapes and conf, the card's map cell bounded and never re-derived, and criteria that read what they claim

**Status:** DEFERRED · rev-4 · 2026-10-28 · node d · Tier-2 · base 8c395e3c · streams tooling · order 23 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dFurnishedOrders-37-deviation-371.md](../build/2026-10-27-build-TOOL-dFurnishedOrders-37-deviation-371.md) | deviation | — |
| [2026-10-27-build-TOOL-dFurnishedOrders-37-deviation-372.md](../build/2026-10-27-build-TOOL-dFurnishedOrders-37-deviation-372.md) | deviation | — |
| [2026-10-28-build-TOOL-dFurnishedOrders-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dFurnishedOrders-1-agent-ledger.md) | journal | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-22 TOOL-dFurnishedOrders-23 TOOL-dFurnishedOrders-24 TOOL-dFurnishedOrders-25 TOOL-dFurnishedOrders-26 TOOL-dFurnishedOrders-27 TOOL-dFurnishedOrders-28 TOOL-dFurnishedOrders-29 TOOL-dFurnishedOrders-30 TOOL-dFurnishedOrders-31 TOOL-dFurnishedOrders-32 TOOL-dFurnishedOrders-33 TOOL-dFurnishedOrders-34 TOOL-dFurnishedOrders-35 TOOL-dFurnishedOrders-36 TOOL-dFurnishedOrders-38 TOOL-dFurnishedOrders-39 TOOL-dFurnishedOrders-40 TOOL-dFurnishedOrders-41 TOOL-dFurnishedOrders-42 TOOL-dFurnishedOrders-43 TOOL-dFurnishedOrders-44 TOOL-dFurnishedOrders-45 TOOL-dFurnishedOrders-46 TOOL-dFurnishedOrders-47 TOOL-dFurnishedOrders-48 TOOL-dFurnishedOrders-49 TOOL-dFurnishedOrders-50 TOOL-dFurnishedOrders-51 TOOL-dFurnishedOrders-52 TOOL-dFurnishedOrders-53 TOOL-dFurnishedOrders-54 TOOL-dFurnishedOrders-55 TOOL-dFurnishedOrders-56 TOOL-dFurnishedOrders-57 TOOL-dFurnishedOrders-58 TOOL-dFurnishedOrders-59 TOOL-dFurnishedOrders-60 TOOL-dFurnishedOrders-61 |
| [2026-10-28-build-TOOL-dFurnishedOrders-37-deviation-373.md](../build/2026-10-28-build-TOOL-dFurnishedOrders-37-deviation-373.md) | deviation | — |
| [2026-10-28-prompt-TOOL-dFurnishedOrders-1-parents-crosscheck.md](../prompts/2026-10-28-prompt-TOOL-dFurnishedOrders-1-parents-crosscheck.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-22 TOOL-dFurnishedOrders-23 TOOL-dFurnishedOrders-24 TOOL-dFurnishedOrders-25 TOOL-dFurnishedOrders-26 TOOL-dFurnishedOrders-27 TOOL-dFurnishedOrders-28 TOOL-dFurnishedOrders-29 TOOL-dFurnishedOrders-30 TOOL-dFurnishedOrders-31 TOOL-dFurnishedOrders-32 TOOL-dFurnishedOrders-33 TOOL-dFurnishedOrders-34 TOOL-dFurnishedOrders-39 TOOL-dFurnishedOrders-41 TOOL-dFurnishedOrders-42 TOOL-dFurnishedOrders-45 TOOL-dFurnishedOrders-46 TOOL-dFurnishedOrders-48 TOOL-dFurnishedOrders-49 TOOL-dFurnishedOrders-50 TOOL-dFurnishedOrders-52 TOOL-dFurnishedOrders-53 TOOL-dFurnishedOrders-54 TOOL-dFurnishedOrders-55 TOOL-dFurnishedOrders-56 TOOL-dFurnishedOrders-58 TOOL-dFurnishedOrders-59 TOOL-dFurnishedOrders-60 TOOL-dFurnishedOrders-61 |
| [2026-10-28-prompt-TOOL-dFurnishedOrders-1-parents-reground.md](../prompts/2026-10-28-prompt-TOOL-dFurnishedOrders-1-parents-reground.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-29 TOOL-dFurnishedOrders-42 TOOL-dFurnishedOrders-46 TOOL-dFurnishedOrders-48 TOOL-dFurnishedOrders-50 TOOL-dFurnishedOrders-58 |
| [2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md](../reviews/2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-35 TOOL-dFurnishedOrders-36 TOOL-dFurnishedOrders-31 TOOL-dFurnishedOrders-32 TOOL-dFurnishedOrders-33 TOOL-dFurnishedOrders-34 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-1 promotions
(`memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-22-spec-audit-round1.md`)
confirmed 27 MEDIUM and 10 LOW findings. BUILD-METHOD M4 batches them into one unit, and §4 "Why one
unit" shows why they do not split into two disjoint write sets. Each report id is named once below
and closed by its own scope item. The report merged some ids into one item; each id still takes its
own scope item here.

| Report item | Report id | Severity | Lands on | Scope item |
|---|---|---|---|---|
| M1 | 4 | MEDIUM | unit 28 S2, AC1; unit 16 S2 | S1 |
| M2 | 5 | MEDIUM | unit 29 AC5 | S2 |
| M2 | 14 | MEDIUM | unit 29 AC5, S6 | S3 |
| M3 | 6 | MEDIUM | unit 30 AC3 | S4 |
| M4 | 11 | MEDIUM | unit 25 S2, AC2 | S5 |
| M4 | 34 | MEDIUM | unit 25 S2, AC2 | S6 |
| M5 | 12 | MEDIUM | unit 25 S4, AC4 | S7 |
| M5 | 36 | MEDIUM | unit 25 S4 | S8 |
| M6 | 18 | MEDIUM | unit 25 S4, F2 | S9 |
| M7 | 13 | MEDIUM | unit 26 S2, AC3 | S10 |
| M8 | 23 | MEDIUM | unit 24 S3, §4, AC2 | S11 |
| M9 | 20 | MEDIUM | unit 29 S24; unit 28 S3 | S12 |
| M10 | 21 | MEDIUM | unit 30 S6, §10 | S13 |
| M10 | 41 | MEDIUM | unit 30 S6, AC5 | S14 |
| M11 | 22 | MEDIUM | unit 30 S6, F2 | S15 |
| M11 | 40 | MEDIUM | unit 30 S6; unit 13 S6 | S16 |
| M12 | 26 | MEDIUM | units 29 and 30, §4 and Files touched | S17 |
| M13 | 27 | MEDIUM | unit 24 S1, S2; unit 19 S7, AC1 | S18 |
| M14 | 31 | MEDIUM | unit 26 S2; unit 28 S2 | S19 |
| M15 | 32 | MEDIUM | unit 27 S1, S3 | S20 |
| M16 | 28 | MEDIUM | unit 30 S6, S8; unit 13 AC1, AC2, S6 | S21 |
| M17 | 33 | MEDIUM | unit 27 AC2 | S22 |
| M18 | 35 | MEDIUM | unit 25 S1, §5 | S23 |
| M19 | 38 | MEDIUM | unit 29 S19, AC14 | S24 |
| M20 | 39 | MEDIUM | unit 29 S3, AC3 | S25 |
| M21 | 37 | MEDIUM | unit 29 S24, S23 | S26 |
| M22 | 43 | MEDIUM | unit 22 S2 | S27 |
| L1 | 7 | LOW | unit 28 AC3 | S28 |
| L2 | 8 | LOW | unit 25 S2; unit 4 AC9 | S29 |
| L3 | 9 | LOW | unit 30 §4 "S3's carriers" | S30 |
| L3 | 17 | LOW | unit 30 S7 | S31 |
| L4 | 15 | LOW | unit 29 S23 | S32 |
| L5 | 16 | LOW | unit 24 S4, F4 | S33 |
| L6 | 19 | LOW | unit 25 S4, F2 | S34 |
| L7 | 24 | LOW | unit 23 S2 | S35 |
| L8 | 29 | LOW | unit 30 §7 | S36 |
| L9 | 42 | LOW | unit 30 S3, AC2 | S37 |

## 2. Scope (IN)

- **S1** — id 4. A missing transcript is not an empty one. `runlog.py turns` (`TOOL-dFurnishedOrders-16`
  S2) exits 3, printing nothing on stdout and `runlog: no transcript for session <sid>` on stderr,
  when the session's coverage reads `tree` `absent` (`tools/runlog/extract.py:756-757`); a transcript
  with no event still prints nothing and exits 0. `derive_attended` reads exit 3 as unit 28 S2's cause
  `no transcript for <sid>`. Observed by AC1.
- **S2** — id 5. The sibling-kit load check scoped. Unit 29 AC5's grep becomes
  `git grep -n -E "^\s*(import|from) (extract|gov_tag|loop_lib|runlog_lib|legacy_ledger|backlog)\b|spec_from_file_location|load_kit_module|import_module" -- 'tools/roles/*.py'`.
  It flags a bare import and a by-file load of another kit's module alike, since a by-file load is an
  in-process import (TOOL-dGroundRules-1 §4, PLAY-dOrderedCharter-7 §4). A line it prints passes only
  where a `requires_if` row of `tools/roles/kit.toml` names the kit the loaded file sits in. None does
  at this unit's pass, so it prints nothing once unit 29 S6 is built. `read_cap_answer`'s `import
  budgets` is unit 42 S7's. Unit 29's ledger answers AC5 in the AMENDED form, naming this item.
  Observed by AC2.
- **S3** — id 14. The self-kit path inserts left alone. The 13 `sys.path.insert` lines whose argument
  is `str(KIT_DIR)` or `sys.argv[1]` (`check_roles.py:83`, `handoff.py:91`, `render_agents.py:72`, three
  in `adopt-roles.sh`, seven in `adopt-roles.test.sh`, read at `8c395e3c`) load the roles kit's own
  modules and stay; the only other insert is `read_cap_answer`'s (`roles_lib.py:149`). Observed by AC2.
- **S4** — id 6. Unit 30 AC3 gets a floor. The adopt-unattended probe prints at least 3 lines and the
  unattended-build probe at least 1, so deleting the arms cannot pass it; unit 30's ledger answers AC3
  in the AMENDED form, naming this item. Observed by AC3.
- **S5** — id 11. Comments are no call site. Before `retired_dispatch_args.py` (`TOOL-dFurnishedOrders-25`
  S2) matches a key, it skips each line whose first non-blank characters are `//`, `#`, `/*` or `*`,
  and reads no further on a line past a whitespace-preceded `//` or `#`. Observed by AC4.
- **S6** — id 34. The code shapes that pass no argument. A `case "<key>":` label, and a key whose value
  opens an object (`<key>: {`, a schema property such as `tools/workflows/unattended-build.js:769`), are
  no hit; a real hand-out passes a scalar or a name (`checklist: CHECKLIST`,
  `tools/workflows/unattended-build.js:2485`). Unit 25 §4 "What it does not check" gains the residue:
  an unrelated object key spelled as a key the step names, with a scalar value, in a file naming
  `unattended-unit.js`, still hits. Observed by AC4.
- **S7** — id 12. `MEMORY_ROOT` normalised and refused as `resolve_memory_root` does
  (`tools/runlog/runlog_lib.py:393-410`): `/` stripped at both ends; a value empty after stripping, `.`,
  or holding `\`, `:` or a `..` segment refuses the step at exit 1 naming the key and the value, before
  any scan. Observed by AC5.
- **S8** — id 36. Where the reader loads from. The conf is read through S34's reader, which lives in
  `govkit.py` and loads from the step's own tool root as `TOOL-dFurnishedOrders-35` S1 loads it, never
  from the target's memory-tree home, so a target without that kit reads its conf the same way; a load
  that fails is unit 35's refusal. Observed by AC5.
- **S9** — id 18. The driver's conf first. `MEMORY_ROOT` is read from `.unattended.conf` when it
  declares the key, else from `.memory-tree.conf`, else `memory`, the rule TOOL-dDeclaredLoop-72 §4
  designs for the driver (`tools/unattended/unattended.sh:548`, `:560`); both declaring it and
  disagreeing after S7 refuses at exit 1 naming both files. Observed by AC5.
- **S10** — id 13. The window reads the seam that exists. The `turns` verb prints, after its events,
  one line `untimed <n>`, the coverage `untimed` count of the session's main file
  (`tools/runlog/extract.py:883-891`); `derive_attended` parses each event's `<utc>` and `since` to
  epoch seconds before comparing, and names `<n>` as ` (<n> unparsed)` when it is above 0. Observed by
  AC1.
- **S11** — id 23. No evaluator nobody calls. `SCHEMA_KEYWORDS` admits `anyOf`, and
  `check_return_schema` evaluates it as pass-if-any with one failure `anyOf: no branch admits outcome
  <value>`; the failing-branch reporting of unit 24 S3 and its §4 "Why the matching branch names the
  failure" is not built, or is taken out where a pass built it. `tools/roles/README.md` names TOOL-dBoundRoles-5 S1
  and TOOL-dBoundRoles-26 S2's arm checks as the source of a retry's field. Observed by AC7.
- **S12** — id 20. One runner, one bound constant. `CHECKER_BOUND_S` moves from
  `tools/roles/handoff.py:102` into `roles_lib.py` beside `run_slot_reader` (unit 29 S24), whose run
  shape is `handoff.py:268-276`'s: stdin from `DEVNULL`, captured output, `errors="replace"`, a
  timeout. Unit 28's `turns` read and unit 34's posture read go through it with `bound=10`, and the
  two checker runs of `handoff.py` with the default. Observed by AC8.
- **S13** — id 21. The map cell's bound in the card's own pattern. `skills/session-kickoff/manifest-check.sh`
  gains `CARD_MAP_BOUND=${CARD_MAP_BOUND:-10}` beside `CARD_OVERLAP_BOUND` (`:220`); unit 30 S6's level
  0 runs as `--overlaps` runs (`:560-564`): the `timeout -k` probe, then `timeout -k 2 "$CARD_MAP_BOUND"`
  with stdin from `/dev/null` and output to a scratch file under the card dir, never a `$( )` capture
  (`:405-409`). A node without a working `timeout -k` writes `project-map — unavailable: no working
  timeout -k on this node`. Observed by AC9.
- **S14** — id 41. The bound observed. A stub renderer that sleeps past the bound, and one that
  backgrounds a sleeper holding stdout and exits, each leave the append returning within the bound
  plus the kill grace, the stored card holding `project-map — unavailable: gov_map.py timed out after
  <n>s`. Observed by AC9.
- **S15** — id 22. One process decides. A READY body carrying a cell whose header passes unit 13 S4's
  grammar is accepted as the scout composed it, and the append does not run level 0 again; the append
  runs level 0 only for a body with no cell, to choose between `not-installed` and `unavailable`.
  Observed by AC10.
- **S16** — id 40. The scout's instruction for a failed run.
  `tools/roles/agents/gov-orienter.agent.md`'s job (unit 13 S6) says: where its own `gov_map.py` run
  fails, expires or finds no renderer, compose no cell, and the append writes the `not-installed` or
  `unavailable` cell itself. Observed by AC10.
- **S17** — id 26. The kickoff manifest re-stamped once. `memory/guides/SESSION-KICKOFF.md`'s
  `last-audit:` line is re-stamped by this unit, after units 29 and 30 and this unit's own S13 to S15
  and S24, at a sha at or after the last commit touching `tools/gate-legs.json` or
  `skills/session-kickoff/manifest-check.sh`, both on its `watch:` line (`:5`), which
  `manifest-check.sh:1525-1541` grades; units 29 and 30 answer their write-set claims in their ledgers,
  naming this item. Observed by AC11.
- **S18** — id 27. The shared member's readers. `handoff.py return-schema --part rows`
  (`TOOL-dFurnishedOrders-19` S7) reads `establishes` and `upstream` from the `allOf` member unit 24 S1
  and S2 move them into; unit 19's AC1 arm reads `allOf[0]` and its ledger answers AC1 in the AMENDED
  form, naming this item; unit 29 S13's `tasks` joins the shared member. Observed by AC7.
- **S19** — id 31. One classification of a `turns` line, stated in `derive_attended` and cited by unit
  28 S2: a line `<utc> owner <via>`, `<utc> keepalive` or `untimed <n>` is of the grammar; a grammar
  line whose `<utc>` does not parse is skipped and added to the unparsed count; any other line makes the
  turn half unreadable. Observed by AC1.
- **S20** — id 32. The door's failure has one outcome. When `read_owner_door` (`TOOL-dFurnishedOrders-27`
  S1) finds no `handoff.py` or python, or the door exits non-zero, prints no line, or prints a line not
  shaped `<answer> · <source>`, the helper prints `owner question — door failed: <rc> <first stderr
  line>` and returns the away status, so both callers take the away route with that cause, as unit 28
  answers an unread presence inside a window (§8 F1). Both callers branch on the helper's status,
  never on its text. Observed by AC12.
- **S21** — id 28. The respelled state's readers. Unit 13's AC1 and AC2 are answered in the AMENDED
  form in its ledger, naming this item, and no reader keeps the old spelling: the probe of AC10 over
  `skills/session-kickoff/`, `tools/roles/agents/gov-orienter.agent.md` and `help/roles.md` prints
  nothing. Observed by AC10.
- **S22** — id 33. The no-bypass probe reads the kit, not one file. Unit 27 AC2's check scans every
  `tools/unattended/*.sh` but `*.test.sh` (`unattended.sh:100-101` sources `lib-unattended.sh`, and the
  kit ships `resume-tick.sh`), skips lines whose first non-blank character is `#`, matches lines naming
  both `handoff.py` and `owner-question`, and requires each inside `read_owner_door`'s body; unit 27's
  ledger answers AC2 in the AMENDED form, naming this item. Observed by AC12.
- **S23** — id 35. The scan reads what it meets. `derive_call_sites` lists the population with
  `git ls-files -s -z` and skips gitlinks (mode `160000`); it reads each file as bytes, skips one whose
  first 8 KiB holds a NUL as binary, and decodes the rest with `errors="replace"`; a tracked path absent
  from the work tree, or one whose read raises, is counted `<u> unreadable` on unit 25 S5's line, never
  fatal. Observed by AC6.
- **S24** — id 38. The answered-call leg's guard derived from what its hook reads. The `answered-calls
  self-test` declaration, unit 6 S9's `[[exempt_leg]]` row of `tools/govkit/registry.toml` whose guard
  unit 29 S19 sets, gains `{prefix}/hooks/agent-cap.js`, which the hook reads for
  `extractHandoffMarker` (`tools/hooks/agent-cap.js:1626`; the file has no `module.exports`). Every
  file the hook `require`s or spawns falls under one of the declaration's guards.
  `tools/gate-legs.json` is re-rendered by `leg_factory.py --write`, never edited (TOOL-dWitnessedBar-11
  S1, S2); where `leg_factory.py` is not built at the pass, the pass records that a hand edit stood in
  for it. Unit 29's ledger answers AC14 in the AMENDED form, naming this item. Observed by AC13.
- **S25** — id 39. The broken-index branch's population. Unit 29 S3's step denies on a broken
  `.claude/roles.json` only a payload carrying `agent_type`; a payload with none, the main loop, is
  admitted, and the deny text names the remedy `render_agents.py --write`. Observed by AC14.
- **S26** — id 37. The class, not the list. Every subprocess the roles kit's Python runs goes through
  `run_slot_reader`, unit 1's `map_diff.py --stale-records`, unit 8's `gov_tag.py where` and unit 29
  S15's `gov_tag.py show --json` among them, the git reads of `check_roles.py:426`, `handoff.py:249`,
  `:994` and `render_agents.py:113` too; unit 29 S23 gains the cause `expired`, rendering
  ` stale=unchecked` with `<why>` `timed out`. Observed by AC8.
- **S27** — id 43. One spelling of a subject key. A `subject-reads` entry, or a member of a
  `TOOL-dFurnishedOrders-32` group, that carries `?` is an `R3` defect naming the role and the entry, so
  the index never holds `input:diff?` beside a `### input:diff` heading. Observed by AC15.
- **S28** — id 7. A docs criterion that can fail. `help/roles.md`'s paragraph on the one site carries
  the sentence unit 28 S4 writes with the phrase `presence the run cannot read is away`, and unit 28's
  ledger answers AC3 in the AMENDED form, naming this item's grep. Observed by AC16.
- **S29** — id 8. Unit 4's AC9 fixture planted in the form the narrowed matcher reads: the script
  `tools/govkit/selftest.py` plants for unit 4 AC9 passes `prebuild: 'x'` beside `unattended-unit.js`,
  an object key, and unit 25's `New arm:` covers it. Observed by AC4.
- **S30** — id 9. Six carriers, not five. `grep -n "commit messages" tools/workflows/tier2-review.template.js`
  printed six lines at `8c395e3c`, 798, 885, 1126, 1804, 1806 and 1807 (PINNED); unit 30 S3 withholds
  every one under `cold`, which AC18 observes over prompts and the log together. Observed by AC18.
- **S31** — id 17. Unit 30 S7's annotation `awk` is the one at `skills/session-kickoff/manifest-check.sh:1168-1169`
  at `8c395e3c`, which reads `$CARD_TMP/misses`, not `:1170-1171`. NOT OBSERVED: a line citation in
  another unit's text changes no behaviour, and unit 30 AC6 observes that `awk` wherever it sits.
- **S32** — id 15. Both `FACT_RE` copies widened. The pass widens `roles_lib.FACT_RE` and its
  JavaScript copy in `tools/hooks/agent-cap.js`, both minted by TOOL-dBoundRoles-13 and absent at
  `8c395e3c` (`git grep -n FACT_RE` names only `tools/runlog/model.py`), to admit ` stale=unchecked`
  beside unit 1 S6's `@<blob12>` and `@absent`. Observed by AC17.
- **S33** — id 16. Unit 24 S4's checkers are not "today's". `validate_return` and the refusal arm's
  `actor` check are TOOL-dBoundRoles-5 S1's and TOOL-dBoundRoles-26 S2's, DEFERRED and unbuilt at
  `8c395e3c` (`grep -rn "def validate_return" tools/` printed nothing); this pass re-grounds on both and
  stops naming the unbuilt unit when either is absent. Observed by AC7.
- **S34** — id 19. govkit's own conf reader. `MEMORY_ROOT` is read with `parse_conf_assignment`
  (`tools/govkit/govkit.py:5143-5155`), whose docstring is the rule that govkit does not load a kit's
  engine to read a target (TOOL-aGraftedHelix-46), not with `tree_lib.parse_conf` loaded by path; unit
  25 S4's private name `gov_tree_lib` is not minted. Observed by AC5.
- **S35** — id 24. The index's one loader validates the new key. `loadRoleIndex`
  (`tools/hooks/scratch-guard.js:952-988`) answers `broken` when a role's `subject-reads` is present and
  not a list of strings, as it answers for `gates` (`:979`); an absent key still reads `[]` for
  migration, and unit 23's ledger answers its S2 reading in the AMENDED form, naming this item.
  Observed by AC14.
- **S36** — id 29. Unit 30's two unguarded legs named. `review-protocol parity (kit vs dogfood)`, which
  pairs `tier2-review.js` with its template (`tools/workflows/check-protocol-parity.test.sh:96`), and
  `govkit selfcheck`, which walks unit 30 S10's contract clause, are on this unit's §7 leg line.
  NOT OBSERVED: a leg list is no criterion, and the bar runs every leg once at the close.
- **S37** — id 42. The log line observed. The `:885` clause sits inside `log('WARNING: ...')`
  (`tier2-review.template.js:883-887` at `8c395e3c`); AC18 records the log beside the prompts, so
  restoring that clause turns it red. Observed by AC18.

## 3. Non-goals (OUT)

- Rewording the spec text of units 4, 13, 16, 19 and 22 to 30. Each item states the built tree's end
  state; where a landed criterion cannot hold as written, that unit's ledger answers it AMENDED,
  naming the item.
- The HIGH findings of the same report: `TOOL-dFurnishedOrders-31` to `-36`.
- The report's left-shift gates: the spec-lint rules, the checklist entries and the guard gate. No
  clause of this build names them.
- Raising the card's or a Skill's size row: no item grows either beyond its row.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-22` — R3's `subject-reads` entry check, which S27 refuses a `?` in (id 43)
- **consumes-from** `TOOL-dFurnishedOrders-23` — the absent-or-malformed reading of `subject-reads`, which S35 moves into `loadRoleIndex` (id 24)
- **consumes-from** `TOOL-dFurnishedOrders-24` — the `anyOf` evaluator and the shared `allOf` member, which S11 narrows and S18 re-points the readers of, and S4's checkers, which S33 re-grounds (ids 23, 27, 16)
- **consumes-from** `TOOL-dFurnishedOrders-25` — `derive_call_sites`, its key regex, its `MEMORY_ROOT` read and its population read, which S5 to S9, S23, S29 and S34 settle (ids 11, 34, 12, 36, 18, 35, 8, 19)
- **consumes-from** `TOOL-dFurnishedOrders-26` — the window's time compare and its unparsed count, which S10 grounds on the `turns` verb's output (id 13)
- **consumes-from** `TOOL-dFurnishedOrders-27` — `read_owner_door` and its no-bypass criterion, whose failure outcome and scan S20 and S22 settle (ids 32, 33)
- **consumes-from** `TOOL-dFurnishedOrders-28` — the turn half's unread causes, its bound and its docs criterion, which S1, S12, S19 and S28 settle (ids 4, 20, 31, 7)
- **consumes-from** `TOOL-dFurnishedOrders-29` — the load check, `run_slot_reader`, the answered-call guard and the broken-index step, which S2, S3, S12, S24 to S26 and S32 settle, and the watched `tools/gate-legs.json` render S17 re-stamps after (ids 5, 14, 20, 38, 39, 37, 15, 26)
- **consumes-from** `TOOL-dFurnishedOrders-30` — the card's map cell, the cold carriers, the suite probes and the watched `manifest-check.sh`, which S4, S13 to S17, S21, S30, S31, S36 and S37 settle (ids 6, 21, 41, 22, 40, 26, 28, 9, 17, 29, 42)
- **consumes-from** `TOOL-dFurnishedOrders-32` — the `subject-reads` group, whose members S27 checks for `?` (id 43)
- **consumes-from** `TOOL-dFurnishedOrders-34` — the bounded posture read, which S12 re-points through `run_slot_reader` (id 20)
- **consumes-from** `TOOL-dFurnishedOrders-35` — the step's by-path load of `govkit.py`, through which S8 and S34 read the conf (ids 36, 19)
- **hands-off** `TOOL-dFurnishedOrders-38` — AC3's adopt-unattended arm and S4's amended answer for unit 30, which unit 38 S3 grades on content (id 29 of the third audit)
- **hands-off** `TOOL-dFurnishedOrders-39` — S12's one runner and AC8's stub readers, which unit 39 S3 bounds against a descendant holding stdout (id 27 of the third audit)
- **hands-off** `TOOL-dFurnishedOrders-41` — S23's population read and its unreadable count, which unit 41 S12 gives a link rule and a read cap (id 31 of the third audit)
- **hands-off** `TOOL-dFurnishedOrders-42` — AC2, AC3, AC7, AC8, AC9, AC11, AC12, AC14 and AC17, S1, S10, S17, S22 and S25, which unit 42 S1 to S8, S11 and S15 to S18 settle (ids 1, 2, 23, 16, 3, 22, 4, 5, 7, 13, 21, 26, 30 of the third audit)
- **hands-off** `TOOL-dFurnishedOrders-46` — AC8's first arm and S17's re-stamp, which unit 46 S2 and S1 settle (ids 3, 2 of the fourth audit)

## 4. Design

### Why one unit

M6 admits two batch units only when their write sets are disjoint by all three of its clauses, and
these minors do not split that way:

- **Clause 1.** S17's re-stamp of `memory/guides/SESSION-KICKOFF.md` answers watched edits in both
  halves a kit split would make: `tools/gate-legs.json` in the roles-and-hooks half (S24) and
  `skills/session-kickoff/manifest-check.sh` in the kickoff half (S13 to S15). Either the re-stamp line
  sits in both write sets, or it lands before one half's edit and the ratchet reds. One unit
  re-stamps once, last.
- **Clause 2.** S21 writes the roles kit's `gov-orienter.agent.md`, which moves `KIT_ROLES_VERSION`
  in `roles_lib.py`, and its criterion reads kickoff's `manifest-check.sh` and suite. The roles half
  would write the version line and the kickoff half the file S21's criterion reads.

So the minors build as one unit, at order 23, after every unit they land on.

### How an item closes

Each item states the built tree's end state, and the pass does what is missing or records that a
landed unit already left it so, as `TOOL-dFurnishedOrders-29` §4 does.

### The `turns` read after S1, S10 and S19

```
runlog.py turns --session <sid> [--transcripts <dir>]
  no transcript                     -> exit 3, stderr "runlog: no transcript for session <sid>"
  transcript                        -> "<utc> owner <via>" | "<utc> keepalive" lines, then "untimed <n>", exit 0
derive_attended
  exit 3                            -> unread: no transcript for <sid>
  grammar line, <utc> unparsed      -> skipped, counted
  non-grammar line                  -> unread: turns printed a line outside its grammar
  since given                       -> compare epoch seconds; source names " (<n> unparsed)" when n > 0
```

### The `MEMORY_ROOT` read after S7 to S9 and S34

```
for conf in .unattended.conf, .memory-tree.conf:  parse_conf_assignment per line -> MEMORY_ROOT or none
both set and differ (after normalising)   -> exit 1 naming both files
first set, else "memory"                  -> strip "/" both ends
empty | "." | holds "\" or ":" | a ".." segment  -> exit 1 naming MEMORY_ROOT and the value
```

### Inventory

Minted: `CARD_MAP_BOUND`; the stdout line `untimed <n>` and exit 3 of `runlog.py turns`; the printed
lines `owner question — door failed:` and `project-map — unavailable: no working timeout -k on this
node`; the cause `expired` of unit 29 S23. No function: `run_slot_reader` is unit 29's, and every other
item changes an existing body.

### Migration

None: no stored data changes shape. S10's `untimed` line is additive to the `turns` grammar, which S19
states once.

### Rollout

Live at landing, at order 23, after every unit it lands on. `KIT_ROLES_VERSION`, the hooks, runlog,
unattended and workflows kits' versions and `KIT_MANIFEST_VERSION` move for the kit epoch leg.

### Files touched (estimate)

- `tools/runlog/runlog.py`
- `tools/runlog/selftest.py`
- `tools/roles/roles_lib.py`
- `tools/roles/handoff.py`
- `tools/roles/check_roles.py`
- `tools/roles/render_agents.py`
- `tools/roles/agents/gov-orienter.agent.md`
- `tools/roles/adopt-roles.test.sh`
- `tools/roles/README.md`
- `tools/hooks/scratch-guard.js`
- `tools/hooks/scratch-guard.test.sh`
- `tools/hooks/agent-cap.js`
- `tools/govkit/registry.toml` (the `answered-calls self-test` declaration's guard, S24)
- `tools/gate-legs.json` (rendered by `leg_factory.py --write`, never edited)
- `tools/govkit/steps/retired_dispatch_args.py`
- `tools/govkit/selftest.py`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `skills/session-kickoff/manifest-check.sh`
- `skills/session-kickoff/manifest-check.test.sh`
- `tools/workflows/tier2-review.template.js`, rendered to `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.test.sh`
- `memory/guides/SESSION-KICKOFF.md`
- `help/roles.md`
- `.claude/agents/` and `.claude/roles.json` (renders, by `render_agents.py --write`)

### Alternatives rejected

- **Two batch units split by kit.** §4 "Why one unit": the re-stamp and the orienter's file cross the
  cut.
- **Refuse the dispatch when the door fails (S20).** An unattended run then stalls on a broken door
  exactly as it stalls on an unread presence; unit 28 F1 refused that answer.
- **Keep `tree_lib.parse_conf` loaded by path (S34).** It loads a kit's engine to read a target, which
  `parse_conf_assignment`'s rule exists to avoid, and adds a third spelling of the refusal.

## 5. Production-readiness checklist

- security — S7 refuses a records root that leaves the target; S25 keeps the main loop's writes open
  on a broken index while still denying role agents; S27 keeps the hook's exemption key one spelling.
- perf / scale — S12 and S26 cap every roles subprocess; S13 caps the card's renderer run at 10
  seconds; S15 removes a second renderer run from every append carrying a cell.
- error / empty / loading states — S1, S20, S23 and S35 each turn a failure into a named state.
- observability — S1's exit, S10's count, S20's line and S23's unreadable count name the cause.
- risks — S26 routes git reads through a bound; a slow git on a large tree reads `timed out` and names
  it, where it hung before.
- testing — AC1 to AC18 by probes, fixtures and greps a pass builds; the arms of §7 at the close.
- migration — none.
- user docs — `help/roles.md` by S21 and S28.

## 6. Acceptance criteria

- **AC1** — When `python tools/runlog/runlog.py turns --session <sid> --transcripts <dir>` runs over a
  scratch root holding no transcript for `<sid>`, it exits 3 naming the session on stderr; over one
  whose main file holds a record that would yield an owner event and carries an unparseable
  `timestamp`, it prints `untimed 1` last; and `python -c` calling
  `roles_lib.derive_attended(root, since=T1, transcripts=<dir>)` answers `False` with a source naming `no transcript` for the first, and,
  with a stub verb printing an owner line whose `<utc>` does not parse beside a valid owner line after
  T1, `True` with a source ending `(1 unparsed)`.
  Red when: a missing transcript reads as an empty one, or one malformed line is answered two ways.
  fixture: scratch transcripts roots under `%TEMP%`, so no live session is read.
- **AC2** — When `git grep -n -E "^\s*(import|from) (extract|gov_tag|loop_lib|runlog_lib|legacy_ledger|backlog)\b|spec_from_file_location|load_kit_module|import_module" -- 'tools/roles/*.py'`
  runs it prints nothing, and over a scratch copy whose `handoff.py` gains
  `importlib.util.spec_from_file_location("gov_runlog_extract", p)` it prints that line; and `git grep -n "sys.path.insert" -- tools/roles/` piped to
  `grep -v -e "str(KIT_DIR)" -e "sys.argv\[1\]"` prints only `read_cap_answer`'s line in
  `tools/roles/roles_lib.py`.
  Red when: a bare sibling import or a by-file load survives, or a faithful build must delete a
  self-kit insert to pass.
  figure: the 13 self-kit inserts are PINNED at `8c395e3c`.
- **AC3** — When `git grep -n "for-diff HEAD~1" -- tools/unattended/adopt-unattended.test.sh` runs it
  prints at least 3 lines, none opening `hit `; and
  `git grep -n "dispatch.args.checklist" -- tools/workflows/unattended-build.test.sh` prints at least 1 line, none spelling `--for-diff HEAD~1`.
  Red when: the arms are deleted and the probe passes on nothing.
- **AC4** — When `python retired_dispatch_args.py witness <target> checklist` runs over a scratch
  target whose `run.js` under `scripts` names `unattended-unit.js` and holds, one at a time,
  `// checklist: retired`, `# prebuild: x`, ` * @param checklist: the list`, `case "checklist":` and
  `checklist: { type: 'string' }`, each exits 0; holding `checklist: 'x'` it exits 1 naming the file;
  and `witness <target> prebuild` over unit 4 AC9's script, planted as
  `grep -n "prebuild: 'x'" tools/govkit/selftest.py` shows it, exits 1.
  Red when: a comment or a schema property stops `up`, or a live hand-out is missed.
- **AC5** — When the AC4 target's `.memory-tree.conf` sets `MEMORY_ROOT=memory/`, `witness` excludes
  its records; set blank, `.`, or `..\x`, it exits 1 naming `MEMORY_ROOT` and scans nothing; with
  `.unattended.conf` setting `MEMORY_ROOT=records` and `.memory-tree.conf` setting `memory`, it exits 1
  naming both files; with no memory-tree kit in the target and `MEMORY_ROOT=records`, it excludes
  `records/`; and `grep -c "tree_lib" retired_dispatch_args.py` in `tools/govkit/steps` prints 0.
  Red when: a trailing slash excludes nothing, a blank root excludes everything, or the driver's root
  is ignored.
- **AC6** — When the AC4 target also tracks a file of invalid UTF-8, a binary holding a NUL, a path
  named with a non-ASCII character, a gitlink and a path deleted from the work tree after its commit,
  `witness` exits with no traceback and its scan line counts `1 unreadable`.
  Red when: one file the scan cannot decode ends the walk.
- **AC7** — When `python -c` calls `roles_lib.check_return_schema` with unit 24's rendered schema on a
  refused return missing `remedy`, it yields exactly one failure, naming `anyOf`; when it calls
  `roles_lib.validate_return` on the same return, a defect names `remedy`; when
  `python tools/roles/handoff.py return-schema --role gov-builder --part rows --upstream d#s1` runs, it
  prints one line whose properties are exactly `establishes` and `upstream`; and
  `grep -n "def validate_return" tools/roles/roles_lib.py` prints a line.
  Red when: a branch evaluator no caller reaches is certified, the rows line reads the old top level,
  or unit 24 S4 rests on a checker that is not built.
- **AC8** — When `git grep -n -E "subprocess\.(run|Popen|check_output|call)\(" -- 'tools/roles/*.py'`
  runs it prints only `run_slot_reader`'s line; `git grep -n -E "CHECKER_BOUND_S\s*=" -- tools/roles/`
  prints one line, in `tools/roles/roles_lib.py`; and with stub `map_diff.py` and `gov_tag.py` that sleep
  past the bound, `handoff.py render` writes ` stale=unchecked` with `timed out` and a `timed out` slot
  state.
  Red when: a render subprocess runs unbounded, or two bound constants remain.
- **AC9** — When the card append runs with `CARD_MAP_BOUND=2` and a stub `gov_map.py` that sleeps 30
  seconds, and again with one that backgrounds such a sleeper holding stdout and exits 0, each append
  returns within 5 seconds and the stored card holds `project-map — unavailable: gov_map.py timed out`;
  and `grep -n "CARD_MAP_BOUND=" skills/session-kickoff/manifest-check.sh` prints the default line.
  Red when: a hung renderer hangs every READY append.
  fixture: a scratch card dir and stub renderers under `%TEMP%`.
- **AC10** — When the append receives a READY body carrying a cell whose header passes unit 13 S4's
  grammar, with a stub `gov_map.py` that exits 1 and appends one line per call to a counter file, it
  exits 0, the stored card keeps the cell, and the counter file stays empty; `grep -n "unavailable"
  tools/roles/agents/gov-orienter.agent.md` prints a line; and `git grep -n "project-map — not
  installed" -- skills/session-kickoff/ tools/roles/agents/gov-orienter.agent.md help/roles.md` prints
  nothing.
  Red when: a second run refuses a cell the scout composed, or a reader keeps the old spelling.
- **AC11** — When `git merge-base --is-ancestor` runs with the last commit touching
  `tools/gate-legs.json` or `skills/session-kickoff/manifest-check.sh` and the sha on
  `memory/guides/SESSION-KICKOFF.md`'s `last-audit:` line, it exits 0.
  Red when: a watched edit lands with no re-stamp and the ratchet reds on the bar.
- **AC12** — When `bash tools/unattended/unattended.sh --dispatch <slug> <unit>` runs in the unit 27
  AC1 fixture with the stub `handoff.py` replaced by one that exits 2 printing nothing, it prints
  `owner question — door failed: 2` and takes the away route, and `--phase` past the gated exit prints
  the same line and takes the away route too; and an `awk` probe over every `tools/unattended/*.sh`
  but `*.test.sh`, comments dropped, prints no line naming `handoff.py` and `owner-question` outside
  `read_owner_door`'s body, while a call planted in `tools/unattended/lib-unattended.sh` makes it
  print that line.
  Red when: the two paths answer a failed door two ways, or a sibling file bypasses the helper.
  fixture: unit 27 AC1's scratch clone under `%TEMP%`.
- **AC13** — When `python -c` reads the rendered `tools/gate-legs.json` and the `require(` and spawn
  lines of the roles kit's `answered-calls.js`, every required or spawned path and
  `tools/hooks/agent-cap.js` fall under a guard of the `answered-calls self-test` row; and
  `python tools/run-gates/leg_factory.py --check` exits 0.
  Red when: an edit to `extractHandoffMarker` skips the leg, or the guard is edited into the manifest
  beside its declaration.
- **AC14** — When `node scratch-guard.js` reads a `Write` payload under `memory/` with `.claude/roles.json`
  invalid, it exits 2 naming the broken index and `render_agents.py --write` when the payload carries
  `agent_type` `gov-tester`, and exits 0 when it carries none; and `node -e` calling `loadRoleIndex` on
  an index whose `gov-skeptic` entry holds `"subject-reads": "input:diff"` answers state `broken` naming
  `subject-reads`, and on one with no such key answers a loaded index.
  Red when: a broken index blocks the main loop, or a malformed key passes unreported.
- **AC15** — When `python tools/roles/check_roles.py` runs over a scratch copy of the kit in which
  `gov-skeptic.agent.md` carries `subject-reads: input:diff?`, it exits 1 with an `R3` defect naming
  `input:diff?`.
  Red when: the index can hold a key no heading equals.
  fixture: a scratch copy of `tools/roles/` under `%TEMP%`, built by the pass.
- **AC16** — When `grep -n "presence the run cannot read is away"` runs over `help/roles.md`, it prints
  a line.
  Red when: the docs criterion passes on a line the parent build wrote.
  figure: the grep prints nothing at `8c395e3c` (PINNED), so it cannot pass before unit 28 S4.
- **AC17** — When `python -c` matches `roles_lib.FACT_RE` and `node -e` matches the `FACT_RE` of
  `tools/hooks/agent-cap.js` against one fact line ending ` stale=unchecked`, both match.
  Red when: the spawn guard refuses a render's unchecked fact line.
- **AC18** — When `tier2-review.template.js` is rendered with `VERIFIER_CONTEXT` `cold` and run in a
  `vm` context over a stub `agent` recording every prompt and a stub `log` recording every line, with
  neither `specs` nor `context` passed, no recorded prompt or log line contains `commit messages`.
  Red when: the warning's clause at the template's `:885` is restored under `cold`.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `scratch-guard self-test` · `agent-cap self-test` · `format-guard self-test` · `hook destinations self-test` · `runlog selftest` · `pre-push run-log line` · `run-gates canary` · `run-gates gov canary` · `run-gates run-log line` · `measure-legs selftest` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor` · `recall floor arms` · `unattended kit gate` · `manifest-check self-test` · `kickoff-manifest ratchet` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `review-join self-test` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `check-wiring self-test` · `policy fixtures` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The leg `answered-calls self-test` is `TOOL-dFurnishedOrders-6`'s, not in the manifest at base, so it
is named here in prose; S24 edits its declaration.

New arm: tools/runlog/selftest.py · covers AC1 · a session with no transcript and one with an untimed owner record, staged by printing nothing and exiting 0 for both · none
New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC7 AC8 AC15 AC17 · stub turns, map and tag readers, a refused return and a `?` subject entry, staged by restoring the unbounded checker run · none
New arm: tools/govkit/selftest.py · covers AC4 AC5 AC6 · comment and schema shapes, the conf matrix and undecodable files, staged by matching the key regex over raw text · none
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC9 AC10 · sleeping and stdout-holding stub renderers and a body carrying a valid cell, staged by capturing the renderer with `$( )` · none
New arm: tools/hooks/scratch-guard.test.sh · covers AC14 · a broken index with and without `agent_type`, staged by denying every write on a broken index · none
New arm: tools/unattended/unattended.test.sh · covers AC12 · a failing stub door behind both paths and a planted sibling call, staged by branching on the door's text; the suite stays WAIVED at landing by the build README's rule, its arm owed with PLAY-dClosedLoop-18 · none
New arm: tools/workflows/tier2-review.test.sh · covers AC18 · a cold render with a recording `log`, staged by restoring the warning's clause · none

## 8. Open questions

- **F1 — What does a failed owner door answer?** Options: (a) away with the cause, as unit 28 answers
  an unread presence inside a window; (b) refuse the dispatch or the phase move. (b) stalls an
  unattended run on a broken door, the failure unit 28 F1 refused. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3, the survivor of veto 1 against unit 28's goal; `run.on-owner-question` keeps
  the decision the owner's. widens: none · relaxes: none
- **F2 — Where does the `MEMORY_ROOT` rule come from?** Options: (a) TOOL-dDeclaredLoop-72 §4's rule,
  `.unattended.conf` first with a refusal on disagreement, read through `parse_conf_assignment`; (b)
  `.memory-tree.conf` alone, unit 25 S4 as written. (b) keeps a second records-root rule beside the
  driver's. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the skeptic-judged fixes of ids 18 and
  19. widens: none · relaxes: none
- **F3 — How many units do the minors take?** Options: (a) one; (b) two, by kit. (b) fails M6's first
  and second clauses (§4). RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, BUILD-METHOD M4.
  widens: none · relaxes: none
- **F4 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-26,
  delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent `TOOL-dBoundRoles-39`
  §8 F1 records. widens: none · relaxes: none
- **F5 — The units this one lands on are unbuilt.** Units 4, 13, 16, 19 and 22 to 35 are specced and
  unbuilt at `8c395e3c`. RESOLVED (agent, 2026-10-26, delegated): the build run re-grounds on each at
  the pass and records any item a landed unit already closed, rung 1, the brief's rule. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, the spec audit of the round-1 promotions' 27 MEDIUM and 10 LOW
  findings batched.
- rev-2 · 2026-10-27 · §3 · the Edges block gains the **hands-off** bullet(s) mirroring TOOL-dFurnishedOrders-38, TOOL-dFurnishedOrders-39, TOOL-dFurnishedOrders-41, TOOL-dFurnishedOrders-42, promoted from the spec audit of the round-2 promotions (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md`); nothing else moved.
- rev-3 · 2026-10-27 · §3 · the Edges block gains the **hands-off** bullet mirroring TOOL-dFurnishedOrders-46, promoted from the spec audit of the round-3 promotions (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-38-spec-audit-round1.md`); nothing else moved.
- rev-4 · 2026-10-28 · §2 S2, S24; §3 Edges; §4 Files touched; §6 AC2, AC13; §7 · re-grounded on the
  parents at `1a61f21a2` by the cross-check record
  `memory/builds/dFurnishedOrders/build/2026-10-28-build-TOOL-dFurnishedOrders-1-parents-crosscheck.md`,
  rows 113 and 114.

## 10. Reuse audit

The seams extended: `_build_coverage` and its `untimed` count (`tools/runlog/extract.py:756-757`,
`:883-891`) for S1 and S10; `resolve_memory_root`'s refusal set (`tools/runlog/runlog_lib.py:393-410`)
and `parse_conf_assignment` (`tools/govkit/govkit.py:5143-5155`) for S7 to S9 and S34; `handoff.py`'s
checker run and `CHECKER_BOUND_S` (`tools/roles/handoff.py:102`, `:268-276`) under unit 29's
`run_slot_reader` for S12 and S26; the card's bounded-read pattern (`skills/session-kickoff/manifest-check.sh:220-228`,
`:405-409`, `:558-566`) for S13; `loadRoleIndex` (`tools/hooks/scratch-guard.js:952-988`) for S35.
`python tools/codebase-map/reuse_lookup.py "read the attendance posture and fail when the loop kit is
absent"` ranked `read`, `read_text`, `fail` and `absent`, and `"files a kit homes on a target with no
install receipt"` ranked `resolve_kit_dir`, `kit_rel` and `kit_dir`, none a seam beyond the ones named.
The recall probe returned the report's items and TOOL-dSafePassage-8, neither disagreeing with source.

Recall terms used: `python tools/memory-recall/query.py "which minor findings of the second
dFurnishedOrders spec audit land where" --terms "minors batch turns untimed MEMORY_ROOT
parse_conf_assignment run_slot_reader CARD_MAP_BOUND read_owner_door subject-reads loadRoleIndex"`
