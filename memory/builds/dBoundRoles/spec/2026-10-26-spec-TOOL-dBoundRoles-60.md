# TOOL-dBoundRoles-60 — the round-1 audit of units 52 to 58, its 37 minors: criteria that can fail and can pass, arms observed where their code lives, one read-key parse, floors moved with their arms, and write sets that name every file a pass writes

**Status:** OPEN · rev-5 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 33 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |
| [2026-10-26-build-TOOL-dBoundRoles-59-round4-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-59-round4-fix-return.md) | research | TOOL-dBoundRoles-59 |
| [2026-10-26-prompt-TOOL-dBoundRoles-59-round4-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-59-round4-fix-brief.md) | research | TOOL-dBoundRoles-59 |
| [2026-10-26-review-TOOL-dBoundRoles-59-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-59-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-59 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the seven promoted specs 52 to 58
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-52-spec-audit-round1.md`) confirmed
one HIGH finding, promoted as `TOOL-dBoundRoles-59`, and 24 MEDIUM and 13 LOW. BUILD-METHOD M4 batches the
minors into one unit: they do not split into two disjoint write sets by M6 (§4 "Why one unit"). This unit
takes all 37, report ids 1 to 9, 11 to 20 and 22 to 39, each its own scope item even where the report
merged several into one item. Id 10 was refuted by the audit and id 21 is unit 59's.

| Report item | Report id | Lands on | Scope item |
|---|---|---|---|
| M1 | 1, 12, 24 | unit 58 S18, AC18 | S1, S2, S3 |
| M2 | 2, 16 | unit 53 S2, AC3, §7 | S4, S5 |
| M3 | 3 | unit 46 AC3, unit 58 S9 | S6 |
| M4 | 4, 14, 27 | units 52 and 53 §4 Rollout | S7, S8, S9 |
| M5 | 5, 13 | unit 54 AC3 | S10, S11 |
| M6 | 7, 36 | unit 55 AC1, §7 | S12, S13 |
| M7 | 9, 29 | unit 58 AC30 | S14, S15 |
| M8 | 15 | unit 58 S5, §4, AC5 | S16 |
| M9 | 22 | unit 58 AC5 | S17 |
| M10 | 25 | unit 56 S3, §4, §7 | S18 |
| M11 | 28 | units 54 and 55 AC1, AC2, §7 | S19 |
| M12 | 30 | `tools/gate-legs.json`, unit 56 §5 | S20 |
| M13 | 33 | unit 57 S1, AC1 | S21 |
| M14 | 34 | unit 57 AC1 | S22 |
| M15 | 35 | unit 54 S1, S2, AC1 | S23 |
| M16 | 37 | units 52, 53 and 58 §7 | S24 |
| L1 | 6, 19 | unit 52 AC3, unit 58 AC6 | S25, S26 |
| L2 | 8 | unit 19 §6, unit 55 AC2 | S27 |
| L3 | 11 | unit 56 S5, §3 | S28 |
| L4 | 17, 31 | unit 56 §5, §7 | S29, S30 |
| L5 | 18 | unit 56 S2, §4 | S31 |
| L6 | 20 | unit 53 §5, unit 56 S5 | S32 |
| L7 | 23 | unit 52 S1, §3, §4 | S33 |
| L8 | 26 | unit 54 AC1 | S34 |
| L9 | 32 | units 53, 54 and 58 §4 | S35 |
| L10 | 38 | unit 58 S21, AC21 | S36 |
| L11 | 39 | unit 57 S3 | S37 |

## 2. Scope (IN)

- **S1** — id 1. 58 AC18 matches the string literally and excludes its own spec:
  `git grep -nF 'handoff.derive_section_sha'`, with an exclusion pathspec for spec 58. Observed by AC1.
- **S2** — id 12. The probe is scoped to `tools/` and the three specs it repairs, 46, 48 and 50, so no
  other spec that quotes the call can hold it red. Observed by AC1.
- **S3** — id 24. 58 S18 is reworded to name the moved function by unit and module, so spec 58 carries no
  string the probe matches. Observed by AC1.
- **S4** — id 2. 53 AC3 stages a `tools/roles/handoff.py` copy that calls `ap.error` only when a typed
  value holds the refusal span `record:TOOL-tFix-9@000000000000` and renders normally otherwise, so the
  control render passes and only S3's exit check can turn the case red. Observed by AC2.
- **S5** — id 16. 53 §7's arm line states that staging, and 53 S2 says a failed control render stops the
  case, naming that render, before the refusal render runs. Observed by AC2.
- **S6** — id 3. 46 AC3 names `tools/roles/spawn-guard.js`, where unit 25 moved the guard and 58 S8
  added `require.main === module`, and order 32; unit 46's ledger answers AC3 `amended rev-<n>`, and 58
  S9 says so. Observed by AC3.
- **S7** — id 4. 52 §4 Rollout names `TOOL-dBoundRoles-26` as a third writer of
  `tools/roles/adopt-roles.test.sh` at order 22. Observed by AC4.
- **S8** — id 14. That Rollout names the hold that kept the three apart: `--dispatch` refuses a pass whose
  declared write set intersects an open one (`tools/unattended/unattended.sh:13421`, M6 condition 1). The
  ledger shows the three order-22 pass commits never open together. Observed by AC4.
- **S9** — id 27. 53 §4 Rollout names unit 26 the same way, and neither spec gains an edge to 26, by §8
  F2. Observed by AC4.
- **S10** — id 5. 54 AC3 requires `derive_overlay_expected` or "role slot" inside 49's S3 and AC2
  bullets, a phrase those bullets lack at base. Observed by AC5.
- **S11** — id 13. 54 AC3 also requires a §9 line in spec 49 above rev-2 naming `TOOL-dBoundRoles-54`
  with `S3` or `AC2`. Where unit 54's pass left 49 unrestated, this pass makes 54 S3's bump. Observed by
  AC5.
- **S12** — id 7. 55 AC1's fixture is empty on both sides: a scratch kit with no `agents/*.agent.md` and no
  `house/*.md` include in its `kit.toml`, the failure naming the kit path. Observed by AC6.
- **S13** — id 36. 55's arm states that removing S1's length test turns that fixture green. Observed by
  AC6.
- **S14** — id 9. 58 AC30 observes by behaviour: `roles_lib.check_block_fences` on a well-formed section
  whose walk ends inside a fence yields no line. Observed by AC7.
- **S15** — id 29. The same section rendered through `render_handoff` yields exactly one refusal, 38 S5's.
  Observed by AC7.
- **S16** — id 15. 58 S5 and §4 say the control role's one card key, `card:route?`, is optional and that
  its render runs with `CLAUDE_CODE_SESSION_ID` unset; the control render in
  `tools/roles/adopt-roles.test.sh` runs under `env -u CLAUDE_CODE_SESSION_ID`. Observed by AC8.
- **S17** — id 22. 58 AC5 maps each `reads` entry through `roles_lib.parse_read_key` and asserts no native
  `task:` key and no non-optional `brief:` or `card:` key. Observed by AC9.
- **S18** — id 25. 56 §4 Files touched names `memory/guides/SESSION-KICKOFF.md`, the last-audit re-stamp
  the watched `manifest-check.sh` forces into the same commit (C5s, `manifest-check.sh:1589-1597`); its
  §7 names `kickoff-manifest ratchet`; and 56 S3 tells the pass to re-check the §B claims that file feeds
  before it re-stamps. Observed by AC10.
- **S19** — id 28. Unit 19's pass takes `derive_overlay_expected` and its compare out of
  `tools/govkit/selftest.py` (55 S2, whose Readers clause names them). 54 AC1, AC2 and 55 AC1 gain
  "observed at its own pass, before unit 19's pass". 54's and 55's §7 arm lines lose the `New arm:` prefix
  and state the arm's life, its pass to unit 19's, so M8's close stages no arm on a check that is gone.
  This pass observes both arms on the tree archived at the parent of unit 19's pass commit. Observed by
  AC11.
- **S20** — id 30. The `scratch-guard self-test` row of `tools/gate-legs.json` guards
  `{prefix}/memory-tree/tree_lib.py`, so a commit touching only `parse_spec_h1` runs 56's parity case.
  `tools/gate-legs.json` is watched too, so this pass's commit carries the re-stamp of S18. Observed by
  AC12.
- **S21** — id 33. 57's no-search-tool half reads the whole rendered Skill text; the token-presence half
  keeps reading the description. Observed by AC13.
- **S22** — id 34. The invariant lives in an undecorated `check_skill_description(text)` in
  `tools/memory-recall/selftest.py`, importing only the standard library inside its body, which the
  decorated check calls. 57 AC1 loads that one function by `ast` from the file's source, with no import of
  the module, so no suite runs. Observed by AC13.
- **S23** — id 35. 54 S1 and S2 state one path form: `<home>/house/<slot>.md`, `home` read from the
  roles descriptor the plan used, equal to each row's `src`; AC1 asserts the seeded side is non-empty on
  the default target. Observed by AC14.
- **S24** — id 37. Every `New arm:` line of 52, 53 and 58 on `tools/roles/adopt-roles.test.sh` and of 58
  on `tools/roles/spawn-guard.test.sh` names its floor move, and each suite's floor carries a
  `+<n> for <case> (<unit>)` comment per unit, `FLOOR_ASSERTIONS` raised by their sum. Observed by AC15.
- **S25** — id 6. 52 AC3 requires a §9 line in spec 47 above rev-2 naming `S1`, `AC1`, `AC2` and
  `TOOL-dBoundRoles-52`, `gov-orienter` and `input:prompt` inside 47's AC1 and AC2 bullets, and the case
  commented `TOOL-dBoundRoles-47` rendering `--role gov-orienter`. Observed by AC16.
- **S26** — id 19. 58 AC6 requires a §9 line in spec 45 above rev-2 naming `AC1` and
  `TOOL-dBoundRoles-58`, and `gov-builder` inside 45's AC1 bullet. Observed by AC16.
- **S27** — id 8. Spec 19 gains AC7, `grep -n 'derive_overlay_expected' tools/govkit/selftest.py` prints
  nothing on the tree its pass leaves; 55 AC2 names 19 AC7 as its after half; this pass writes 19's AC7
  answer in the OBSERVED form. Observed by AC17.
- **S28** — id 11. 56 S5 and §3 count from the enumeration: four fixtures hold one live H1, fixture 4
  holds none, and fixtures 1, 2 and 4 hold a fenced decoy; the admit and refuse checks apply where an id
  or a decoy exists. Observed by AC18.
- **S29** — id 17. 56 §5's risk line no longer claims the size leg reads `manifest-check.sh`: that leg
  measures `skills/session-kickoff/SKILL.md` (`tools/gate-legs.json:151-155`). Observed by AC19.
- **S30** — id 31. The risk line names the real effect, the re-stamp of S18, and 56's §7 leg line names
  `kickoff-manifest ratchet` in place of `kickoff engine size <=18KiB`, an unguarded leg over a file 56
  does not touch. Observed by AC19.
- **S31** — id 18. 56 S2 and §4 Evidence add
  `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py` (`:274`, `:608`) to
  `parse_spec_h1`'s consumers, state that its pin does not cover the change, and name AC3's
  re-derivation as its observation. Observed by AC20.
- **S32** — id 20. 53 §5 writes `"$PY" -B -c` and 56 S5 `"$TESTPY" -c`, the launchers the two suites
  resolve; neither suite holds a bare `python3 -c`. Observed by AC21.
- **S33** — id 23. 52 S1 and §4 say 14 S7 tag-spells `gov-orienter`'s line without changing what it
  reads and cite `parse_read_key` as the reader that folds it; 52's §3 gains a **consumes-from**
  `TOOL-dBoundRoles-14`, and 14's §3 its mirror, both written at this pass. Observed by AC22.
- **S34** — id 26. 54 AC1 states no typed count: one overlay per role file of the installed kit at
  observation time. Observed by AC14.
- **S35** — id 32. 53, 54 and 58 §4 Files touched name `memory/map/generated/symbols.json`, regenerated by
  `python tools/codebase-map/gen_map.py --write`, as spec 42 does. Observed by AC23.
- **S36** — id 38. 58 AC21 loops over the four shapes S22 grades, `### `, a fact line, a marker line and
  `Framed by:`, each after a `\r` in `--input question=`; the suite holds the four cases. Observed by
  AC24.
- **S37** — id 39. 57 S3 reads "NOT OBSERVED by a criterion: S3 is the §7 leg line, which the spec tokens
  leg resolves". Observed by AC25.

## 3. Non-goals (OUT)

- The HIGH finding, `TOOL-dBoundRoles-59`.
- Rewording specs 1 to 59 beyond what an item changes; §4 "How an item closes" is the one route.
- The report's left-shift gates: the self-matching grep check, the staged-break checklist, the order
  precondition check, the parallel-step file check, the base-tree criterion check, the fixture checklist,
  the function-placement check, the session-id unset, the watch-list cross-check, the arm-on-deleted-check
  gate, the `--legs-for` reader check, the span checklist, the import checklist, the path-form checklist,
  the floor check, the ledger-phrase check, the count re-derivation, the leg-argv check, the consumer
  inventory, the bare-launcher ban, the stale-citation checklist, the typed-count check, the symbols check,
  the N-shapes checklist and the observed-by checklist. No clause of this build names them; each item's
  criterion is its regression.

### Edges

- **consumes-from** `TOOL-dBoundRoles-59` — the folded `assert_role_reads`, under which S4's staged copy leaves the control render passing (ids 2 and 21)
- **consumes-from** `TOOL-dBoundRoles-14` — `parse_read_key`, through which S17 reads the control role's entries, and §3, which S33 mirrors (ids 22 and 23)
- **consumes-from** `TOOL-dBoundRoles-19` — §6, which S27 extends by the deletion's criterion (id 8)
- **consumes-from** `TOOL-dBoundRoles-46` — AC3, which S6 re-points at the moved guard (id 3)
- **consumes-from** `TOOL-dBoundRoles-52` — S1, AC3, §3, §4 Rollout and §7, which S7, S8, S24, S25 and S33 restate (ids 4, 6, 14, 23, 37)
- **consumes-from** `TOOL-dBoundRoles-53` — S2, AC3, §4, §5 and §7, which S4, S5, S9, S24, S32 and S35 restate (ids 2, 16, 20, 27, 32, 37)
- **consumes-from** `TOOL-dBoundRoles-54` — S1, S2, AC1 to AC3, §4 and §7, which S10, S11, S19, S23, S34 and S35 restate (ids 5, 13, 26, 28, 32, 35)
- **consumes-from** `TOOL-dBoundRoles-55` — AC1, AC2 and §7, which S12, S13, S19 and S27 restate (ids 7, 8, 28, 36)
- **consumes-from** `TOOL-dBoundRoles-56` — S2, S3, S5, §3, §4, §5 and §7, which S18, S20 and S28 to S32 restate (ids 11, 17, 18, 20, 25, 30, 31)
- **consumes-from** `TOOL-dBoundRoles-57` — S1, S3 and AC1, which S21, S22 and S37 restate (ids 33, 34, 39)
- **consumes-from** `TOOL-dBoundRoles-58` — S5, S9, S18, S21, AC5, AC6, AC18, AC21, AC30, §4 and §7, which S1 to S3, S6, S14 to S17, S24, S26, S35 and S36 restate (ids 1, 3, 9, 12, 15, 19, 22, 24, 29, 32, 37, 38)
- **hands-off** `TOOL-dBoundRoles-62` — S24 and AC15, which unit 62 restates per suite with a refusal for a suite holding no floor, and the spawn guard's suite, whose floor its pass keeps or mints (id 21 of the round-1 audit of units 59 and 60)
- **hands-off** `TOOL-dBoundRoles-63` — S1, S19, S24, S26, §4, AC4, AC6, AC11, AC14 and AC15, which unit 63 restates: the floor sum's base term, criteria that read the retired text, the worktree observations and the full write set (ids 2, 3, 4, 5, 6, 8, 10, 12, 13, 15, 16, 20 and 22 of the round-1 audit of units 59 and 60)
- **hands-off** `TOOL-dBoundRoles-64` — AC4, AC15, §4 Evidence and the ledger's AC15 answer, which unit 64 restates: the joined Rollout probe, units 50, 60 and 61 per suite, the cited token loop and one AC15 line carrying the base reading (ids 1, 3, 5, 6, 7, 9, 10, 14, 19, 20 and 21 of the round-1 audit of units 61 to 63)
- **hands-off** `TOOL-dBoundRoles-66` — S24 and the ledger's AC15 answer, which unit 66 restates with units 50, 60 and 61 named and parses with the deviation join's `LEDGER` (ids 16 and 21 of the round-1 audit of unit 64)
- **hands-off** `TOOL-dBoundRoles-69` — §4 "Where each item lands" and AC6's `fixture:` line, which unit 69 restates: the detached worktree of spec 63's S12 under `dbr63obs`, not an archive under `%TEMP%` (id 15 of the round-1 audit of units 65 and 66)

## 4. Design

### Why one unit

M4 admits two units only when the minors split into two disjoint write sets by M6. They do not. S24
writes specs 52, 53 and 58 and both suites; S35 writes specs 53, 54 and 58; S32 writes 53 and 56; S19
writes 54 and 55; and the roles-suite items and the memory-recall items both change indexed functions,
so both halves would regenerate `memory/map/generated/symbols.json`, a generated index together with its
generator (M6 clause 3).

### How an item closes

Each item states the built tree's end state, and the pass does what is missing or records that a landed
unit already left it. Where an item changes another unit's criterion or scope item, the pass bumps that
unit's spec FIRST with the changed text and a §9 line naming this unit (BUILD-METHOD M2, READY), and that
unit's ledger answers the criterion `amended rev-<n>`, naming the revision (58 §4 "How an item closes").

### Where each item lands at order 33

Every other unit has built. `agent-cap.js` is retired and the spawn guard lives in
`tools/roles/spawn-guard.js` with its suite. Unit 19's pass took the overlay compare out of
`tools/govkit/selftest.py`, so S12, S13, S19 and S23 observe on the tree archived at the parent of that
pass commit, extracted with `git archive` under `%TEMP%`, short-pathed.

### Evidence

Read at base `462d20f3` on 2026-10-26:

- `git grep -n 'handoff.derive_section_sha' -- tools memory/builds/dBoundRoles/spec` prints specs 46, 48,
  50 and two lines of 58.
- `tools/roles/handoff.py:359-360` resolves a card for any `card:` key, and `:262-271` runs the kickoff
  checker when `CLAUDE_CODE_SESSION_ID` is set; `gov-builder.agent.md:7` reads `card:route?`.
- `tools/roles/kit.toml:6` sets `home = "roles"`; `tools/govkit/govkit.py:322-338` returns `{home}/{s}`.
- `tools/memory-recall/selftest.py:94-103` runs each check as it is decorated; `:71` fixes `KIT`;
  `:1615-1618` reads tokens from `desc` only; `SKILL.template.md:66` holds the body's fallback.
- `memory/guides/SESSION-KICKOFF.md:6` watches `manifest-check.sh` and `tools/gate-legs.json`.
- `tools/gate-legs.json` guards `scratch-guard self-test` on `{prefix}/hooks/`, `{prefix}/lib/` and
  `skills/session-kickoff/`; `kickoff engine size <=18KiB` has no guard.
- `tools/roles/adopt-roles.test.sh:73-81`: the floor's comment terms sum to `FLOOR_ASSERTIONS=50`.

### Inventory

Minted: `check_skill_description` (`py.function`) and the cases of S16 and S36. Each name is asked of
`python tools/lexicon/lexicon.py --suggest <name> --as <cell>` at the pass.

### Migration

None: no stored data changes. S27 and the AMENDED answers add ledger lines this build's passes own.

### Rollout

Live at landing, at order 33, after every unit it repairs and after unit 59.

### Files touched (estimate)

- `tools/roles/adopt-roles.test.sh`
- `tools/roles/spawn-guard.test.sh`
- `tools/hooks/scratch-guard.test.sh`
- `tools/memory-recall/selftest.py`
- `tools/gate-legs.json`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/map/generated/symbols.json`
- the specs of units 14, 19, 46, 47, 49, 52, 53, 54, 55, 56, 57 and 58, rev bumps, and the ledgers the
  AMENDED answers and S27 write, named here for the dispatch write set

### Alternatives rejected

- **Two units.** §4 "Why one unit".
- **Keep 54's and 55's arms as `New arm:` lines.** M8 would stage each on a function unit 19 took out.
- **Run the memory-recall suite to observe 57 AC1.** A pass runs no self-test suite (M6); S22 is the
  direct form.

## 5. Production-readiness checklist

- security — S16 keeps a session's kickoff checker out of a fixture render; no new write path.
- perf / scale — greps, renders, one archive extraction and one `ast` load.
- error / empty / loading states — S12 refuses an empty roster by kit path; S5 stops on a failed control
  render.
- observability — the ledger records S8's dispatch evidence and S19's archived-tree observations.
- risks — the bumps touch eleven converged specs; each moves only the item's text.
- testing — AC1 to AC25 by grep, render, probe and archived tree; the arms of §7 at the close.
- migration — none.
- user docs — none under `help/`: no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When `git grep -nF 'handoff.derive_section_sha' -- tools memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-46.md memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-48.md memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-50.md`
  runs, it prints nothing, 58 AC18 spells that command, and `grep -cF 'handoff.derive_section_sha'` over
  spec 58 prints 1, AC18's own line.
  Red when: a correct build leaves the criterion red, or a line outside its scope holds it.
- **AC2** — When 53's case runs against a scratch `tools/roles/handoff.py` that calls `ap.error` only for a
  typed `record:TOOL-tFix-9@000000000000`, the control render passes and the case fails naming the usage
  error; with S3's exit check reduced to non-zero, the case passes.
  Red when: the staged break reds the case before S3 is reached.
- **AC3** — When `node -e "process.stdin.destroy();console.log([...require('./tools/roles/spawn-guard.js').TYPED_INPUTS].join(','))"`
  runs, it prints `question,diff` and exits 0, and `grep -n 'spawn-guard.js'` over spec 46 prints AC3.
  Red when: 46 AC3 still names a file the build retired.
- **AC4** — When `grep -n 'TOOL-dBoundRoles-26'` runs over specs 52 and 53, each prints its §4 Rollout
  naming the suite and `--dispatch`, and the ledger lists the three order-22 pass commits in sequence.
  Red when: a Rollout asserts a disjointness the Files touched contradict.
- **AC5** — When a `python -c` probe extracts 49's S3 and AC2 bullets, each holds
  `derive_overlay_expected` or "role slot", and 49's §9 holds a line above rev-2 naming
  `TOOL-dBoundRoles-54` with `S3` or `AC2`.
  Red when: 54 AC3 is green on a tree where S3 was skipped.
- **AC6** — When the archived tree's compare runs on a scratch kit with no role file and no `house/*.md`
  include, it fails naming the kit path; with S1's length test taken out of the archived copy, it passes.
  Red when: the fixture reds for a reason S1 does not own.
  fixture: the archive of §4 "Where each item lands", under `%TEMP%`.
- **AC7** — When a `python -c` probe calls `roles_lib.check_block_fences` on a section ending inside a
  fence, it returns no line, and `render_handoff` on it raises exactly one refusal.
  Red when: two functions refuse one open walk, or none does.
- **AC8** — When `grep -n 'env -u CLAUDE_CODE_SESSION_ID' tools/roles/adopt-roles.test.sh` runs, it prints
  the control render, and spec 58's S5 names `card:route?` as optional.
  Red when: the control render can run a real kickoff checker.
- **AC9** — When 58 AC5's probe reads a scratch control role holding `field.task.title`, it fails naming
  `task:title`; on the shipped role it passes.
  Red when: a raw prefix read lets a tag-spelled `task:` key through.
- **AC10** — When `grep -n 'SESSION-KICKOFF.md'` runs over spec 56, it prints §4 Files touched, its §7 line
  names `kickoff-manifest ratchet`, and `git show --stat` of unit 56's pass commit lists the manifest.
  Red when: a pass writes a file its declared set omits.
- **AC11** — When the archived tree's 54 and 55 arms are staged and restored, each reads red then green,
  and over specs 54 and 55 a `grep -c` for a line opening `New arm:` and naming govkit's self-test
  module prints 0 for each.
  Red when: M8's close is asked to stage an arm on a deleted check.
- **AC12** — When `python tools/check-spec-tokens.py --legs-for tools/memory-tree/tree_lib.py` runs, it
  lists `scratch-guard self-test`.
  Red when: a tree_lib-only commit skips the parity case on a guarded run.
- **AC13** — When a `python -c` probe loads the one function `check_skill_description` by `ast` from the
  memory-recall kit's self-test module and calls it on the template's text, it passes; with "fall back to
  `Grep`" restored in the body, or "Grep and Glob own those" in the description, it fails naming `Grep`.
  Red when: the body can name a refused tool, or the probe needs the module imported.
- **AC14** — When the archived tree's `derive_overlay_expected` runs on a default target, the seeded side is
  non-empty and the compare passes; a scratch descriptor whose `home` names a directory other than the
  default (`tools/roles/kit.toml:6`) seeds the `gov-builder` slot's house file under that home, and its row names `gov-builder`; and `grep -n 'ten at base'` over spec 54 prints nothing.
  Red when: the two sides compare different path forms.
- **AC15** — When a `python -c` probe sums the `+<n>` terms above each suite's `FLOOR_ASSERTIONS`, the sum
  equals the floor, and units 52, 53 and 58 each appear in a term.
  Red when: arms land in a floored suite and the floor stays put.
- **AC16** — When a `python -c` probe extracts 47's AC1 and AC2 and 45's AC1 bullets, the first two hold
  `gov-orienter` and `input:prompt` and the third `gov-builder`, and `grep -n -- '--role gov-orienter'
  tools/roles/adopt-roles.test.sh` prints a line of 47's case.
  Red when: a §9-line half that held before the bump is the only observation.
- **AC17** — When `grep -n 'derive_overlay_expected' tools/govkit/selftest.py` runs, it prints nothing, and
  spec 19's §6 holds AC7 with unit 19's ledger answering it.
  Red when: the deletion has no criterion in the unit that makes it.
- **AC18** — When `grep -n 'fixture 4' memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-56.md`
  runs, S5 and §3 state fixture 4 holds no live H1 and three fixtures a decoy.
  Red when: a count contradicts the enumeration.
- **AC19** — When `grep -n 'size leg'` runs over spec 56, it prints nothing, and §5's risk line names
  `SESSION-KICKOFF.md`.
  Red when: the risk line points at a budget the change cannot cross.
- **AC20** — When `grep -n 'deviations.py'` runs over spec 56, it prints S2 and §4 Evidence.
  Red when: a consumer the instrument pin hides goes unlisted.
- **AC21** — When `grep -nE '(^|[^$"A-Za-z_])python3 (-B )?-c'` runs over specs 53 and 56 and both
  suites, it prints nothing.
  Red when: a case hard-codes the Store stub's name.
- **AC22** — When `grep -n 'parse_read_key'` runs over spec 52, it prints S1 or §4 Evidence, and its §3
  holds **consumes-from** `TOOL-dBoundRoles-14`, mirrored in spec 14.
  Red when: 52 cites a line unit 14 rewrote as unchanged.
- **AC23** — When `grep -n 'symbols.json'` runs over specs 53, 54 and 58, each prints §4 Files touched.
  Red when: a pass regenerates the index outside its declared set.
- **AC24** — When the fixture renders each of the four shapes after a `\r` in `--input question=`, each
  exits 1 naming its line.
  Red when: a build strips the carriage return on the marker branch only.
- **AC25** — When `grep -n 'NOT OBSERVED'` runs over spec 57, it prints S3.
  Red when: S3 names a criterion that never reads §7.

## 7. Gates

`roles adopter self-test` · `roles catalogue` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `memory-recall kit selftest` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

`agent-cap self-test` stands for the spawn guard's suite; unit 25's pass renames it on every live §7
line when it renames the leg.

New arm: tools/roles/adopt-roles.test.sh · covers AC24 · the four CR shapes, staged by a carriage-return strip on the marker branch only, and the raised floor, staged by an early return before unit 58's cases · `FLOOR_ASSERTIONS` raised by the floored assertions S24 counts and S36 adds
New arm: tools/memory-recall/selftest.py · covers AC13 · the whole-text no-search-tool half, staged by restoring "fall back to `Grep`" in the template body · none

S20's guard is not an arm: AC12 observes it directly, red before the edit and green after.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a carry of a clause. The batch carries no clause; veto 1 discards
  (b). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1
  set. widens: none · relaxes: none
- **F2 — An edge between unit 26 and units 52 and 53, or the dispatch hold named (id 27)?** Options: (a)
  edges; (b) the Rollouts name the intersection refusal. No content flows between them, and at order 33
  all three have built, so an edge holds nothing (TEMPLATE-SPEC §3: order is not an edge). RESOLVED
  (agent, 2026-10-26, delegated): (b), rung 3, fewest follow-ups. widens: none · relaxes: none
- **F3 — 46 AC3: the guard at unit 46's pass, or AC3 re-pointed (id 3)?** Options: (a) 46's pass adds the
  guard; (b) AC3 names the moved file. Unit 46 builds at order 12, before this unit, so (a) is out of
  reach. RESOLVED (agent, 2026-10-26, delegated): (b), the report's second sound option. widens: none ·
  relaxes: none
- **F4 — 57 AC1: run the suite, or lift the invariant (id 34)?** Options: (a) one suite run read by line;
  (b) S22's undecorated function loaded by `ast`. (a) runs a self-test suite inside a pass, which M6
  refuses. RESOLVED (agent, 2026-10-26, delegated): (b). widens: none · relaxes: none
- **F5 — Widen the leg's guard, or state the gap (id 30)?** Options: (a) the guard in
  `tools/gate-legs.json`; (b) a §5 sentence. (a) closes the gap and (b) records it. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3, the most feature-rich survivor; the guard widens a leg's reach and
  grants nothing. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, the 24 MEDIUM and 13 LOW findings of the round-1 audit of units 52
  to 58, each id its own item, in one unit.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullets mirroring TOOL-dBoundRoles-62 and TOOL-dBoundRoles-63, the HIGH promotion and the minors batch of the round-1 audit of units 59 and 60; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-64, the minors batch of the round-1 audit of units 61 to 63; nothing else moved.
- rev-4 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-66, the minors batch of the round-1 audit of unit 64; nothing else moved.
- rev-5 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-69, the minors batch of the round-1 audit of units 65 and 66; nothing else moved.

## 10. Reuse audit

The seams are the units' own: 53's `assert_role_reads` as unit 59 folds it, 14's `parse_read_key`, the
suites' `FLOOR_ASSERTIONS` comment convention, `--dispatch`'s intersection refusal, the C5s re-stamp,
`check-spec-tokens.py --legs-for`, and 58's AMENDED rule, each extended rather than copied.
`python tools/codebase-map/reuse_lookup.py "keep a spec criterion observable after a later unit deletes the code it reads"`
ranked `read`, `read_text`, `units` and `read_conf`, none a criterion or arm mechanism, so no existing
seam fits beyond those named; the recall query's first hit is hygiene check 23's ledger reader, which
the AMENDED and OBSERVED answers already feed.

Recall terms used: `python tools/memory-recall/query.py "how does a spec criterion stay red before its unit builds and green after" --terms "criterion staged break floor assertions archived tree amended revision ledger dispatch write set"`
