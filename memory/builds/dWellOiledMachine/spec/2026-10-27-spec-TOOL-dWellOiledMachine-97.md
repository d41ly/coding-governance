# TOOL-dWellOiledMachine-97 — the round-3 promotions audit's 23 medium and low findings, batched: pathspecs, the fixture session, probe environments, the ask row, renders and criteria green before their build

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 68 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-97-deviation-971.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-97-deviation-971.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-95-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-95-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-95 TOOL-dWellOiledMachine-96 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-3 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-91-spec-audit.md`)
exited CONVERGED with 23 confirmed findings below HIGH. BUILD-METHOD M4 promotes every one of them,
batched into ONE unit, and this is that unit. It closes, by report id:

- MEDIUM (15): 3, 5, 6, 7, 11, 12, 13, 14, 17, 18, 19, 22, 26, 27, 28.
- LOW (8): 2, 8, 9, 16, 20, 21, 24, 30.

Several findings share a report item (M1: 3, 11, 26; M2: 6, 12, 19; M3: 7, 13, 27; M4: 14, 28), and
each keeps its own scope item here. Finding 20 (L5) is M3's defect at its skeptic's low grade and
takes M3's fix. Each finding takes the fix its skeptic judged SOUND, or the skeptic's corrected fix
where the report marks the finder's UNSOUND (findings 8, 9, 11, 17). The findings land on specs 91,
92, 93 and 94, so this unit repairs none in particular and sits after every unit of the build. One
unit, not two: findings 6, 12, 19, 24 and 27 all amend spec 91, findings 2, 9 and 18 spec 93, and
every amendment moves this build's README rev cells, a generated render two halves would both write
(M6 clause 3).

## 2. Scope (IN)

Each item names its finding, its report item and the spec it amends. "Spec N takes a rev bump" means
spec N is amended by S24's route, its §9 line naming this unit and the finding, so the unit N builds
the corrected text. Paths are those at each amended unit's order.

- **S1** — Finding 3 (M1), on TOOL-dWellOiledMachine-94 S14 and AC8. Spec 94 takes a rev bump whose S14
  rewrites 90's AC20, and whose AC8 runs,
  `git grep -nE "\[\"bash\"|\['bash'" -- tools/runtime/supervise.py tools/memory-tree/door_fixture.py`,
  90 S20's population, expecting no output; AC8's staged `['bash', 'x']` red arm stays, in a scratch
  copy of `supervise.py`. Observed by AC1.
- **S2** — Finding 11 (M1, the skeptic's corrected fix), on 94 S14. No exclusion filter is added: an
  exclusion of `resolve_shell_argv(` and TOML `argv =` lines still leaves the dict fixtures and
  `check_policy.py`'s real spawns. Spec 94's §4 Evidence records the tree-wide pathspec's 99 lines
  over 8 files at base and why it is not the population. Observed by AC1.
- **S3** — Finding 26 (M1), on 94 AC8. The scoped pathspec names its two files exactly, so the
  `tools/**/*.py` form, which skips top-level `tools/*.py` files, is gone from spec 94 and from 90's
  AC20. Observed by AC1.
- **S4** — Finding 6 (M2), on TOOL-dWellOiledMachine-91 S4. Spec 91 takes a rev bump whose S4 has 81's
  AC1 and AC2 payloads carry `session_id: 'fixture-session'` beside the clock, and the matching
  `stall-recorder.test.sh` cases pass the same session. Observed by AC2.
- **S5** — Finding 12 (M2), on 91 AC7. 91's AC7 also requires
  `grep -c "session_id: 'fixture-session'"` over spec 81 to print 1 or more. Observed by AC2.
- **S6** — Finding 19 (M2), on 91 S1 against 81 AC1. 91's AC7 also runs 81 AC1's own `node -e` with
  the session and clock after S1 is built, and requires `2026-09-10T00:26:40Z`, so S1's session test
  stands and is never relaxed to green 81's criterion. Observed by AC2.
- **S7** — Finding 7 (M3), on 94 S25. Spec 94 takes a rev bump whose S25 has each planter bind its
  lease to `fixture-session` and pass `session_id: 'fixture-session'` in the payload naming the
  dated copy, whose `sessionId` the fixture already carries (91 S4); the rev bumps S25 makes to specs
  65 and 47 say so too. Observed by AC3.
- **S8** — Finding 13 (M3), on 94 AC18. 94's AC18 requires the stall line the plant journals, which the
  beat's hold reads, to carry `limit-record=last` (91 S3). Observed by AC3.
- **S9** — Finding 27 (M3), on 91 §3 Edges. 91's hands-off line to TOOL-dWellOiledMachine-94 names
  the three conditions its reader tests: the payload's session equal to the record's `sessionId`, the
  record dated now, and the reset an hour ahead. Observed by AC3.
- **S10** — Finding 20 (L5), on 94 S25 and 91's hands-off line. The session condition is stated in
  both places by S7 and S9; no second plant shape is admitted. Observed by AC3.
- **S11** — Finding 14 (M4), on 94 AC29. Spec 94 takes a rev bump whose AC29 probe runs with its
  working directory in the scratch repository and `ROOT` exported as that repository, reads the health
  event from the scratch repository's `<common-dir>/health.log`, and requires the live checkout's
  `health.log` to hash the same before and after. Observed by AC4.
- **S12** — Finding 28 (M4), on 94 AC29. The probe exports `REMOTE_BOUND=60`, asserts it is
  non-zero, and passes as the deadline the call site's own expression, read from
  `tools/unattended/unattended.sh` by the grep half and evaluated, so a call site that drops
  `REMOTE_BOUND` or its `+ 10` moves the `until` the probe checks against now plus 70. Its staged break
  edits the call site in a scratch copy. Observed by AC4.
  **Readers:** by name: `tools/unattended/unattended.sh`, the call site the probe reads. by value: NO VALUE READERS — the exported bound is read only by the probe.
- **S13** — Finding 5 (M5), on 94 AC15. Spec 94 takes a rev bump whose AC15 counts bare `runtime.md`
  only over 90's AC14 and AC23 bullets, the lines S21 rewrites, so 90's S12 and the AC12 detector
  `VERBS.template.md runtime.md` stay as they are. Observed by AC5.
- **S14** — Finding 17 (M6, the skeptic's corrected fix), on TOOL-dWellOiledMachine-92 S1. Spec 92 takes
  a rev bump whose ask row names every dPlacedRequest spec
  `git grep -l "write_node_lock\|remove_node_lock\|node-lock-broken\|node-lock-guard-cleared" -- memory/builds/dPlacedRequest/spec/`
  lists, 13 at base (§4), and whose `accept` clause also requires every call site to pass 83 S1's
  `<until-epoch>` and `<event-stem>`, and every criterion grepping a health event to name the
  `<stem>-lock-broken` and `<stem>-guard-cleared` pair for the stem its caller passes. 92's §4
  Evidence records the grep and its count. Observed by AC6.
- **S15** — Finding 18 (M7), on TOOL-dWellOiledMachine-93 S1 and S2. Spec 93 takes a rev bump whose S1
  also moves `extract_gates` (`tools/check-spec-tokens.py:519-536`) whole into `design_lib` as
  `read_spec_gates(text)`, which `read_spec_arm_lines` calls; whose S2 binds the checker's
  `extract_gates` to it as `NOT_A_TOKEN` is bound (`tools/check-spec-tokens.py:878`), so the five
  callers read one slice; and whose §6 gains a criterion, numbered after the AC7 that
  TOOL-dWellOiledMachine-96 adds there, that the checker holds no `GATES_HEAD.search`. Observed by AC7.
- **S16** — Finding 22 (M8), on 94 §7. Spec 94 takes a rev bump whose leg line also names
  `shell hygiene (a fork spent on builtin work)`, `shell hygiene (a loop fed by a command substitution)`,
  `shell hygiene (a location probe asked from a moved directory)`,
  `shell hygiene (a fixed-name temp renamed into place)`, `spawn budget (forks per hot entrypoint)`,
  `unattended skill size` and `template size <=48KiB`, the legs that read
  `memory/project/spawn-idiom-sites.txt`, `tools/template-size-highwater.txt` and `resume-tick.sh`,
  three files its Files touched edits. Observed by AC8.
- **S17** — Finding 2 (L1), on 93 AC3. Spec 93 takes a rev bump whose AC3 reads: after this unit it
  prints no `[guards]` hit and prints the `covers` hit for AC9, and under §7's staged break, a
  `read_spec_writes` that returns arm paths, it prints the `[guards]` hit; "before and" is deleted.
  Observed by AC9.
  **Readers:** by name: `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-93.md`, the one spec spelling the deleted words. by value: NO VALUE READERS — spec prose no program reads.
- **S18** — Finding 8 (L2, the skeptic's corrected fix), on 94 AC2 and AC17. Spec 94 takes a rev bump
  whose AC2 counts `fixture-store` over spec 33, and whose AC17 counts `read as deleted` over spec 72,
  through `grep -v 'hands-off' <spec> | grep -c <term>`, each 1 or more, so the hands-off line alone
  cannot satisfy them. Observed by AC10.
- **S19** — Finding 9 (L3, the skeptic's corrected fix), on 94 S26 and AC19, and 93 S5. Spec 94 takes a
  rev bump whose AC19 also extracts spec 90's S1 paragraph, from `- **S1**` to the next `- **S`, and
  its Files touched section, and requires S1 to name TOOL-dWellOiledMachine-93 and not
  `read_spec_writes`, and Files touched to name 93's tree-wide re-render. 93 S5's rev bump of spec 90
  is deleted by TOOL-dWellOiledMachine-95, whose AC1 observes the same paragraph. Observed by AC11.
  **Readers:** by name: `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-94.md` and `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-93.md`, the specs spelling the deleted rev bump. by value: NO VALUE READERS — spec prose no program reads.
- **S20** — Finding 16 (L4), on 92 S1 and AC1. Spec 92 takes a rev bump whose S1 keys the append on
  content: before filing, it greps `memory/builds/dPlacedRequest/BACKLOG.md` for an ask row titled
  `THE NODE LOCK IS ALREADY LIFTED.` and reuses that row's id when one exists; its AC1 requires
  `grep -c "THE NODE LOCK IS ALREADY LIFTED"` to print exactly 1. Observed by AC12.
- **S21** — Finding 21 (L6), on 92 §4 Files touched and §6. Spec 92 takes a rev bump listing
  `memory/builds/dPlacedRequest/README.md`, `memory/backlog/TOOL.md` and
  `memory/builds/dWellOiledMachine/README.md` under Files touched, each re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, and adding an AC4 that
  `gen_build_index.py --check` exits 0 after the row lands. Observed by AC13.
- **S22** — Finding 24 (L7), on 91 §4 Files touched and §6. Spec 91 takes a rev bump listing
  `memory/builds/dWellOiledMachine/README.md` under Files touched, re-rendered the same way, and adding
  an AC8 that `gen_build_index.py --check` exits 0 after S4's rev bump. Observed by AC13.
- **S23** — Finding 30 (L8), on 92 AC1. Spec 92 takes a rev bump whose AC1 second grep is
  `grep -c "SEV · TOOL-dPlacedRequest-<id> · HIGH · a second write_node_lock"`, `<id>` the id S1
  derives at the pass, expecting 1, and whose Red when names the missing disposition row. Observed by
  AC14.
- **S24** — The route. Every rev bump above is made by the build run's main loop at BUILD-METHOD M2's
  cross-read, before its first code pass, as one spec pass whose commit subject names this unit, after
  the amendments of TOOL-dWellOiledMachine-95 and -96, by the route TOOL-dWellOiledMachine-95 §8 F1
  takes, so units 91 to 94 build and observe the corrected
  text. At this unit's own pass, at order 68, nothing is written: the pass runs AC1 to AC15 and
  records them. Observed by AC15.

## 3. Non-goals (OUT)

- Both HIGHs of the report: TOOL-dWellOiledMachine-95 and -96, one unit each.
- The report's left-shift gates and checklist entries: each finding here is closed by its own
  criterion, and a lint over specs or a checklist row is a separate mechanism (M2).
- No code written at this unit's pass: the code the amended specs describe is built by their own
  units (S24).
- No allowed-set table for the tree-wide bare-bash grep (S2): the population is 90 S20's two files.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-91` — S4's rev bump of spec 81, AC7, the hands-off line to unit 94 and Files touched (S4 to S6, S9, S10, S22)
- **consumes-from** `TOOL-dWellOiledMachine-92` — S1's ask row and its key, AC1, Files touched and §4 Evidence (S14, S20, S21, S23)
- **consumes-from** `TOOL-dWellOiledMachine-93` — S1's and S2's Gates slice and AC3 (S15, S17)
- **consumes-from** `TOOL-dWellOiledMachine-94` — S14, S25, AC2, AC8, AC15, AC17, AC18, AC19, AC29, §4 Evidence and the §7 leg line (S1 to S3, S7, S8, S10 to S13, S16, S18, S19)
- **consumes-from** `TOOL-dWellOiledMachine-95` — 90's rewritten S1 paragraph and the deletion of 93 S5's rev bump, which S19's criterion reads (S19)
- **hands-off** `TOOL-dWellOiledMachine-105` — S24 and §5's risks line, which state the commit pair per amended unit (round-4 promotions audit, finding 13)
- **hands-off** `TOOL-dWellOiledMachine-106` — AC15 and the §6 preamble, rewritten to call the ordering probe once per amended unit (round-4 promotions audit, finding 21)
- **hands-off** `TOOL-dWellOiledMachine-107` — §4, §5's testing line and §6, which gain the fixture and AC16 that observe the ordering check red (round-4 promotions audit, finding 31)
- **hands-off** `TOOL-dWellOiledMachine-108` — S1, S2, S15, S19, S20, §3 Edges, §4 Evidence, AC1, AC8 and AC12, amended before this unit builds (round-4 promotions audit, findings 5, 7, 8, 10, 15, 18, 25, 26, 27, 32 and 33)

## 4. Design

### Evidence

Each finding's evidence is its row of the report's appendix, which its skeptic re-read and confirmed;
the items cite the clause they correct. Probes re-run for this spec at base `0689e7fa`:

- `git grep -cE "\[\"bash\"|\['bash'" -- 'tools/**/*.py'` hits 8 files, 99 lines, among them
  `govkit/matrix.py:911`'s wrapped `resolve_shell_argv(["bash", ...])` (S1 to S3). Neither
  `tools/runtime/supervise.py` nor `tools/memory-tree/door_fixture.py` exists at base: both are built
  by earlier units of this build, before unit 94's pass.
- Spec 81's AC1 calls `extractResetUtc` with `transcript_path` alone (`spec-81.md:123`), and 91 S1
  refuses a record whose `sessionId` is not the payload's (`spec-91.md:31-37`) (S4 to S6).
- 94 S25 substitutes the reset and the timestamp only (`spec-94.md:140-145`), and 91's hands-off line
  names the date and the reset (`spec-91.md:70`) (S7 to S10).
- `REMOTE_BOUND="60"` is assigned only at `tools/unattended/unattended.sh:162`, the claim-push call
  site sits in `write_claim` (`:2396`, `:2403`), the lifted body logs through
  `resolve_health_log "$ROOT"` (`:2338`, `:2350`), and `resolve_health_log` runs `git -C "$1"`
  (`tools/unattended/lib-unattended.sh:77-82`), which for an empty `$1` resolves the working
  directory's repository (S11, S12).
- `grep -nE '(^|[^/])runtime[.]md'` over spec 90 prints lines 85, 401, 402, 407 and 425; 94 S21
  rewrites the AC14 line (407) and the AC23 line (425) only (S13).
- `git grep -l` of the four node-lock names over `memory/builds/dPlacedRequest/spec/` lists 13 specs:
  TOOL-dPlacedRequest-24, -30, -34, -36, -37, -38, -39, -43, -48, -49, -52, -56 and -58 (S14).
- `extract_gates` holds the `GATES_HEAD.search` and the slice (`tools/check-spec-tokens.py:519-536`)
  for callers at `:1340`, `:1518`, `:1552`, `:1605` and `:1609`; `NOT_A_TOKEN` is bound from the kit
  at `:878` (S15).
- `tools/gate-legs.json` names `shell hygiene (a fork spent on builtin work)` with argument
  `memory/project/spawn-idiom-sites.txt`, and `unattended skill size` and `template size <=48KiB` run
  `check-template-size.sh` (S16).
- `grep -c fixture-store` over spec 33 and `grep -c 'read as deleted'` over spec 72 each print 1, from
  each spec's hands-off line to unit 94 (S18).
- `grep -n "SEV · TOOL-dPlacedRequest-"` over `memory/builds/dPlacedRequest/BACKLOG.md` prints six rows
  at base, ids 22, 65, 66, 67, 70 and 71 (S23).

### Inventory

Nothing is minted by this unit's pass. `read_spec_gates`, a `design_lib.py` function in the `read`
lexicon cell, is minted by unit 93's pass under S15's rev bump.

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-91.md`
- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-92.md`
- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-93.md`
- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-94.md`
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since four rev cells move)

### Alternatives rejected

- **Two batches.** Spec 91 takes findings 6, 12, 19, 24 and 27 and spec 93 takes 2, 9 and 18, so any
  split by finding item shares a spec file, and every split shares the README render (§1).
- **The rev bumps at this unit's own pass.** It is order 68, after units 91 to 94: unit 94's AC8 and
  AC15 would be red at its own pass, its AC18 plant could read `stale`, and its AC29 probe would write a
  forged event into the live shared `health.log`.
- **An allowed-set table for the tree-wide bare-bash grep (S2).** The report's other option; it lists
  99 rows outside the unit's population, which go stale as those files change.

## 5. Production-readiness checklist

- security — S11 keeps a probe's forged health event out of the live shared `health.log`, which every
  node's readers consume; S7 to S10 keep 91's session test, the guard against another session's reset.
- perf / scale — N/A — spec text and criteria change.
- error / empty / loading states — S20 makes a re-run pass reuse its own ask row.
- observability — S8's `limit-record=last` on the planted hold.
- risks — a build run that skips M2's cross-read builds units 91 to 94 as first written; AC15 is red
  at this unit's pass in that case.
- testing — AC1 to AC15.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

`<spec N>` is `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-N.md`, or
the 2026-10-26 file for specs 33 and 47, and `<BASE>` is the build run's pinned `base:` fact in
`memory/builds/dWellOiledMachine/RUN.md`. Each criterion runs at this unit's pass, after units 91 to
94 have built.

- **AC1** — When `git grep -nE "\[\"bash\"|\['bash'"` runs over the supervisor and the door fixture,
  `supervise.py` and `door_fixture.py`, it prints nothing; `grep -c "tools/\*\*/\*.py"` over `<spec 94>` prints 0; and
  `grep -c "door_fixture.py"` over `<spec 90>` prints 1 or more.
  Red when: a bare `bash` argv is spawned in either file, or the tree-wide pathspec remains.
- **AC2** — When `node -e` in the runtime kit's directory prints the recorder's `extractResetUtc` over
  session `fixture-session` and the stall fixture's `limit-transcript.jsonl` at `2026-09-10T00:25:20Z`,
  it prints `2026-09-10T00:26:40Z`, and `grep -c "session_id: 'fixture-session'"` over `<spec 81>`
  prints 1 or more.
  Red when: 81's criterion still omits the session, or 91's session test was relaxed to green it.
- **AC3** — When `python supervise.py --fixture --plant limit` runs from `tools/runtime/`, the stall line
  the plant journals carries `limit-record=last`, and the beat journals `limit-hold` naming a reset
  an hour ahead; and
  `grep -c "fixture-session"` over `<spec 94>` and over `<spec 91>`'s hands-off line to unit 94 each
  prints 1 or more.
  Red when: the plant's session differs from the record's and `limit-record=stale` prints.
- **AC4** — When 94's AC29 probe runs from the checkout,
  `git hash-object` over the common git directory's `health.log` prints the
  same before and after, or the file is absent both times, and the scratch repository's `health.log`
  holds `claim-push-lock-broken`; with the probe pointed at a scratch copy of `unattended.sh` whose
  call site drops `REMOTE_BOUND`, the probe fails.
  Red when: the probe writes the live `health.log`, or its deadline check compares the probe's own
  argument with itself.
- **AC5** — When 94's rewritten AC15 command runs over `<spec 90>`, it prints 0, and
  `grep -c "VERBS.template.md runtime.md"` over `<spec 90>` prints 1.
  Red when: AC15 still counts the whole file, or the AC12 detector was reworded to green it.
- **AC6** — When `grep "THE NODE LOCK IS ALREADY LIFTED" memory/builds/dPlacedRequest/BACKLOG.md` runs,
  its row names each of the 13 dPlacedRequest spec ids §4 lists and an accept clause naming call
  sites; and `grep -c "git grep -l"` over `<spec 92>` prints 1 or more.
  Red when: the ask hands the factory to two specs while thirteen spell it.
- **AC7** — When `grep -c "GATES_HEAD.search" tools/check-spec-tokens.py` runs, it prints 0, and
  `grep -c "def read_spec_gates" tools/memory-tree/design_lib.py` prints 1.
  Red when: the checker keeps its own Gates slice beside the kit's.
- **AC8** — When `grep -c "spawn budget (forks per hot entrypoint)"`, `grep -c "unattended skill size"`
  and `grep -c "shell hygiene (a fork spent on builtin work)"` run over `<spec 94>`, each prints 1 or
  more.
  Red when: 94's leg line omits a leg that reads a file it edits.
- **AC9** — When `grep -c "before and after this" <spec 93>` runs, it prints 0, and the AC3 bullet of
  `<spec 93>` names the staged break.
  Red when: AC3 still asks for a state its own Goal calls red.
- **AC10** — When `grep -v 'hands-off' <spec 33> | grep -c fixture-store` and
  `grep -v 'hands-off' <spec 72> | grep -c 'read as deleted'` run, each prints 1 or more, and
  `grep -c "grep -v 'hands-off'"` over `<spec 94>` prints 2 or more.
  Red when: a skipped rev bump of spec 33 or 72 still passes on the hands-off line alone.
- **AC11** — When `awk '/^- \*\*S1\*\*/{p=1} /^- \*\*S2\*\*/{p=0} p' <spec 90>` runs, its output
  names `TOOL-dWellOiledMachine-93` and, piped to `grep -c read_spec_writes`, prints 0; and the Files
  touched section of `<spec 90>` names 93's re-render.
  Red when: a skipped rev bump of spec 90 still passes 94's AC19.
- **AC12** — When `grep -c "THE NODE LOCK IS ALREADY LIFTED" memory/builds/dPlacedRequest/BACKLOG.md`
  runs, it prints exactly 1.
  Red when: a re-run pass filed a second ask carrying the same hand-off.
- **AC13** — When `python tools/memory-tree/gen_build_index.py --check` runs, it exits 0, and
  `grep -c "dPlacedRequest/README.md"` over `<spec 92>` and
  `grep -c "dWellOiledMachine/README.md"` over `<spec 91>` each print 1 or more.
  Red when: a render moved by an ask row or a rev bump is left stale.
- **AC14** — When `grep -c "SEV · TOOL-dPlacedRequest-<id> · HIGH · a second write_node_lock" memory/builds/dPlacedRequest/BACKLOG.md`
  runs, `<id>` the ask row's id, it prints 1.
  Red when: the new disposition row is missing and only older rows print.
- **AC15** — When `git log --reverse --format=%s <BASE>..HEAD | grep -E "TOOL-dWellOiledMachine-(91|92|93|94|97)([^0-9]|$)" | head -1`
  runs, it prints this unit's amendment commit.
  Red when: the amendments land after the units they correct have built.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved at this unit's pass: each criterion above is a probe or a grep, and the arms
the amended units declare stay on their own §7 lines.

## 8. Open questions

- **F1 — When do this batch's rev bumps land, given its order is 68 and every spec it amends is
  ordered below it?** (a) at this unit's own pass; (b) at the build run's M2 cross-read, before its
  first code pass, the route TOOL-dWellOiledMachine-95 §8 F1 takes; (c) a rev bump per amended unit
  placed one step after each. (a) leaves unit 94's AC8 and AC15 red at its pass and lets its AC29 probe
  write the live `health.log`. (c) is one unit per minor, which M4 forbids. (b) has each amended unit
  build and observe the corrected text. RESOLVED (agent, 2026-10-27, delegated): (b). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, the round-3 promotions audit's 23 medium and low findings
  batched.
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-4
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-105, TOOL-dWellOiledMachine-106, TOOL-dWellOiledMachine-107, TOOL-dWellOiledMachine-108.

## 10. Reuse audit

Each item extends the seam its finding names: 90 S20's spawn population (S1 to S3), 91 S1's session
test and the stall fixture's `fixture-session` (S4 to S10), `resolve_health_log` and the claim-push
call site (S11, S12), the builds-mode ask row (S14, S20, S23), `design_lib`'s spec readers and the
`NOT_A_TOKEN` binding (S15), `tools/gate-legs.json` (S16) and `gen_build_index.py --check` (S21, S22).
The probe `python tools/codebase-map/reuse_lookup.py "batch the round-3 promotions audit minor
findings"` ranked `audit` and three `find`-stem builders, none a fix's seam, so the seams are the
per-item ones above; the recall query below ranked TOOL-dWellOiledMachine-79 and -94 first, the two
earlier batches whose shape this unit follows. No item mints a module.

Recall terms used: `python tools/memory-recall/query.py "how are the round-3 spec audit's medium and
low findings batched" --terms "minors batch spec audit medium low promoted findings session binding
pathspec probe environment ask row renders"`
