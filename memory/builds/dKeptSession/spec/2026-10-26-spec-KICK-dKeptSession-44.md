# KICK-dKeptSession-44 — the round-1 spec audit's 42 minor findings, closed after every unit they land on is built

**Status:** DEFERRED · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 30 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-30-promoted-fix-return.md](../build/2026-10-26-build-KICK-dKeptSession-30-promoted-fix-return.md) | research | KICK-dKeptSession-28 KICK-dKeptSession-36 KICK-dKeptSession-40 KICK-dKeptSession-43 KICK-dKeptSession-30 |
| [2026-10-26-build-KICK-dKeptSession-44-deviation-441.md](../build/2026-10-26-build-KICK-dKeptSession-44-deviation-441.md) | deviation | — |
| [2026-10-26-prompt-KICK-dKeptSession-30-promoted-fix-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-30-promoted-fix-brief.md) | research | KICK-dKeptSession-28 KICK-dKeptSession-36 KICK-dKeptSession-40 KICK-dKeptSession-43 KICK-dKeptSession-30 |
| [2026-10-26-review-KICK-dKeptSession-30-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md) | spec-audit | KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-32 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-41 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build's spec set
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md`)
confirmed 33 findings at MEDIUM and 9 at LOW. BUILD-METHOD M4 promotes them into one batch, and this
is it. Each finding is its own §2 item, named by report id beside its report item:

- MEDIUM: ids 3 (M1), 5 (M2), 6 (M3), 7 and 34 (M4), 8 and 37 (M5), 9 (M6), 10 (M7), 11 (M8),
  15 (M9), 19 (M10), 20 (M11), 21 and 46 (M12), 23 (M13), 24 (M14), 27 (M15), 33 (M16), 35 (M17),
  36 (M18), 40 (M19), 48 (M20), 49 (M21), 50 (M22), 51 (M23), 52 (M24), 56 (M25), 59 (M26),
  60 (M27), 61 (M28), 62 (M29), 63 (M30);
- LOW: ids 12 (L1), 13 (L2), 14 and 44 (L3), 18 (L4), 41 (L5), 42 (L6), 43 (L7), 53 (L8).

Ids 7 and 34 are the defect of id 45 at HIGH, item H8, which `KICK-dKeptSession-41` fixes; their
items here observe that fix. The minors land on many units, so this unit is one write set and takes
the order past every unit of the build (order 30): each item amends code its unit has built, and the
three close-time records, the refusal census, the kickoff re-stamp and the map, are written once,
after the last driver, watched file and symbol has moved. Where an item supersedes a sibling spec's
text, it does so by name here, and that unit's acceptance ledger answers the superseded criterion.

## 2. Scope (IN)

- **S1** — id 3, M1. `arm_presets`' row-named half (`KICK-dKeptSession-1` S5) prints
  `presets-core-only · not graded · TOOL-dDeclaredLoop-2 S8 admits after-release-verifies` and counts
  no finding while `check_expansion_value` admits `after-release-verifies` on a core-only fixture;
  the moment it refuses, the half grades. Unit 1 AC6 and AC9 are answered NOT OBSERVED, naming the
  ask, until then. Observed by AC1.
- **S2** — id 5, M2. `KICK-dKeptSession-25` §7's covers list loses AC4: no suite case for the lease
  renewed while waiting is added until dPlacedRequest accepts unit 25 §8 F4's ask, and unit 25's
  ledger answers AC4 NOT OBSERVED naming the ask. Observed by AC2.
- **S3** — id 6, M3. `--mail read`'s `--local` is parsed once, by `KICK-dKeptSession-21`'s addition,
  and `KICK-dKeptSession-10`'s step passes it to the real driver. Unit 10 AC2's stub is superseded by
  AC3's real-driver read. Observed by AC3.
- **S4** — id 7, M4. Units 8, 11 and 17 ACs 8, 6 and 7 are answered by the standing rows'
  summaries `KICK-dKeptSession-41` S1 writes, never by `r[0]`'s owner and default. Observed by AC4.
- **S5** — id 34, M4. The same defect by the reuse lens: each unit's ledger cites the standing row,
  `catalogue.toml:223`, `:543` and `:60` on dGroundRules' branch, and its drain from
  `unsummarised-keys.txt`. Observed by AC4.
- **S6** — id 8, M5. One platform fact, one owner. `tools/unattended/mail-notice.js`'s header states
  that PreToolUse carries `additionalContext` (`KICK-dKeptSession-13` S7 owns that channel) and that
  this PostToolUse registration exists only to cover the tools scratch-guard's matcher does not route.
  `KICK-dKeptSession-21` §8 F1's "no such builder was seen" is superseded by name. Observed by AC5.
- **S7** — id 37, M5. The fact re-probed at the build: `grep -a -c 'hookName:\`PreToolUse:'` over the
  `claude` on PATH and, where installed, the version `RUN.md` pins, each count recorded in unit 21's
  ledger with its version. Observed by AC5.
- **S8** — id 9, M6. One budget for the boundary verb. `--card --boundary` moves the session card's
  `at` to HEAD first, then runs every step under one deadline, `CARD_BOUNDARY_BUDGET=8` seconds, under
  `BOUNDARY_BOUND_S`' 10: each step's timeout is the lesser of its own bound and the time left, the
  mail reads of units 5 and 21 run with `--local`, and a publish with less than its bound left is
  skipped with one line. Observed by AC6.
- **S9** — id 10, M7. `mail-notice.js` binds its build through `readCard` and `extractRouteUnits`,
  exported by `tools/hooks/scratch-guard.js:1615`, and falls back to `resolveLease`. Observed by AC7.
- **S10** — id 11, M8. `KICK-dKeptSession-13` S6 rewrites the `item —` line locally, in the session
  card and the build card file, at every crossing under both values of `card.pointers`;
  `at-transitions` gates only the publish. Unit 8's plants run under both values. Observed by AC8.
- **S11** — id 15, M9. `KICK-dKeptSession-9`'s plant `orient-refuse` sets `budgets.enforce =
  "refuse"`, and `orient-pinned` names `orient-calls` in `budgets.pinned`, each with a row past 30.
  Observed by AC9.
- **S12** — id 19, M10. The stale "not applied" texts go: dGroundRules' `policy.py` docstring at
  lines 689-690 and `tools/policy/README.md` lines 235 and 455 at `3c8c4718a`. Unit 2 AC6's one-phrase
  grep is superseded by AC10's class. Observed by AC10.
- **S13** — id 20, M11. `adopt-policy.sh --scaffold` (lines 99-103 at `3c8c4718a`) passes the
  scaffold's exit 2 and its stderr through, keeping exit 1 for a write failure. Observed by AC11.
- **S14** — id 21, M12. The `orient-calls` row of `tools/policy/caps.toml` carries every census
  field: `research = 0`, the header gaining "0 names a cap no row of the caps research measured";
  `kit = "runlog"`; `installed = "{prefix}/runlog/runlog.py"`. `CAP_CASES` in `check_policy.py`
  (`:3487` at `3c8c4718a`) gains `budgets-cap-orient-calls`. Observed by AC12.
- **S15** — id 46, M12. The blast radius: `resolve_caps` reads the census outside its `try`, so one
  incomplete row refuses every cap; AC13 reads a second cap after the row lands. Observed by AC13.
- **S16** — id 23, M13. `read_mail_interrupts` in `tools/loop/position.py` runs the driver through
  `KICK-dKeptSession-36`'s `resolve_bash`, imported from `loop_lib.py`. Observed by AC14.
- **S17** — id 24, M14. `derive_parent_reach`'s `--claims` read runs through `resolve_bash`, and the
  interface listing unit 7 S3 derives is written in binary mode, LF bytes, so a CRLF clone and an LF
  clone compute one key. Observed by AC14 and AC15.
- **S18** — id 27, M15. The boundary verb writes the resolved `mailbox.notice` and
  `mailbox.fetch-seconds` into the per-worktree sidecar beside the stamp (unit 21 §8 F2's file), and
  the hook reads them with the stamp's read and calls no `readPolicy`. Unit 21 S5's "spawns no git" and
  §4's cost paragraph then hold. Observed by AC16.
- **S19** — id 33, M16. The build files one ask in `memory/builds/dDeclaredLoop/BACKLOG.md`, target
  TOOL-dDeclaredLoop-7 S4, widening unit 10 §8 F3's: `derive_interrupts`' default prints no mail
  line once `position.py --mail-interrupts` is the one mail reader. Unit 10 AC1's plain-call clause
  is answered against that text in its ledger. Observed by AC17.
- **S20** — id 35, M17. `read_dependents` is dropped. The dependents are the parent README's
  rendered `<!-- gen:build-edges -->` "Child builds" line, the inversion
  `tools/memory-tree/gen_build_index.py:2615-2626` derives and refuses a dangling parent in. Observed
  by AC18.
  **Readers:** by name: READER NOT IN TREE — the function is minted by unit 7 in the loop kit, unbuilt
  at this base · by value: NO VALUE READERS — its one caller, unit 7's notices, is re-pointed here.
- **S21** — id 36, M18. `print_replay` opens with `derive_map_block`'s lines (PLAY-dOrderedCharter-4),
  then the stored card, `now —` and the computed lines. Observed by AC19.
- **S22** — id 40, M19. The `records —` line names only the base kinds, `RECORD_KIND_TOKENS` less
  `TYPED_RECORD_KINDS`, so typed kinds the chain mints never lengthen it. Observed by AC20.
- **S23** — id 48, M20. The driver's refusal census, read once after every driver unit by `python
  tools/memory-tree/check-arms.py --report`. A new refusal routes through `fail` where it can; a
  census still past `REFUSAL_CEILINGS`' 323 takes the retirement review the memory-tree README's
  "The ceiling" names, and the ceiling rises only to the census left, under a dated decision id in
  `memory/DECISIONS.md`, with the `.memory-tree.conf` rows of `REFUSAL_CEILINGS` and `ARMS_FLOORS`.
  Observed by AC21.
- **S24** — id 49, M21. One kickoff re-stamp. `memory/guides/SESSION-KICKOFF.md`'s `last-audit` is
  re-stamped after the build's last edit to any `watch:` path, with its delta line, as
  TOOL-dGroundRules-86 did for its build. Observed by AC22.
- **S25** — id 50, M22. `memory/map/features/unattended.md` claims `PostToolUse
  tools/unattended/mail-notice.js`, and the map is regenerated once by the command `map_lib.regen_cmd()`
  prints, `python tools/codebase-map/gen_map.py --write`. Observed by AC23.
- **S26** — id 51, M23. `tools/govkit/entries/kickoff-manifest.kit.toml` ships
  `card-compaction.fixture.sh` as a `[[files]]` row. Observed by AC24.
- **S27** — id 52, M24. `tools/unattended/kit.toml`'s `requires` gains `playbook-render`, the kit
  `check_mail_recipient`'s `render_playbook.py --fleet-tags` call reads (`KICK-dKeptSession-28` S3).
  Observed by AC24.
- **S28** — id 56, M25. `--mail post` refuses `--kind ack` and `--kind answer` with exit 2, naming
  `--mail ack` and `--mail answer`. Observed by AC25.
- **S29** — id 59, M26. The transition guard refuses, exit 2, on any read exit but 0, printing the
  exit code and the first stderr line; only `mail — off` and a missing driver pass. Observed by AC26.
- **S30** — id 60, M27. A failed or timed-out fetch in `--mail post` refuses with exit 2 and the
  fetch's cause before any commit. Observed by AC27.
- **S31** — id 61, M28. The hook's detached spawn sets `windowsHide: true`, as
  `tools/hooks/format-guard.js:248` and `tools/unattended/stop-guard.js:113` do. Observed by AC28.
- **S32** — id 62, M29. `validate` refuses a `[presets.<shipped name>]` table, naming its line and
  the name. Observed by AC29.
- **S33** — id 63, M30. `emit_progress` runs under `timeout` with a new `PROGRESS_BOUND=10`; a
  non-zero exit or a timeout prints `NOTE — progress not emitted: <why>` and never moves the verb's
  exit or lines. Observed by AC30.
- **S34** — id 12, L1. Unit 18 AC3 observes the build, the route by path on `help/loop.md`, and the
  filed ask leaves its §6. Observed by AC31.
- **S35** — id 13, L2. Unit 14 AC7 is withdrawn; its S5 cites `KICK-dKeptSession-13` AC5, which
  observes the `agent_type` skip. NOT OBSERVED here: the criterion moves to the unit that owns the
  check, and unit 14's ledger answers AC7 by that citation.
- **S36** — id 14, L3. What unit 16 writes calls its list the fourth, beside `unsummarised-keys.txt`,
  `legacy-homes.txt` and `KICK-dKeptSession-19`'s `unnamed-keys.txt`. Observed by AC32.
- **S37** — id 44, L3. The same ordinal in unit 16's §10 text, superseded by name. Observed by AC32.
- **S38** — id 18, L4. `presets.toml`'s never-list comment cites v2:1424-1437. Observed by AC33.
- **S39** — id 41, L5. Unit 14's fixture is a `context-fill` scenario of
  `tools/runlog/fixtures/transcripts.json`, and `context-fill.jsonl` is deleted. Observed by AC34.
  **Readers:** by name: READER NOT IN TREE — the file's one reader is unit 14's selftest case, unbuilt
  at this base · by value: NO VALUE READERS — its bytes are read only by that case, re-pointed here.
- **S40** — id 42, L6. Unit 9's quartiles call `_derive_quartiles` (`tools/runlog/runlog.py:210`), and
  the four-field token sum is one function, `derive_spent_tokens`, beside `derive_context_tokens`,
  called by `print_ready` (`:226`) and unit 9's reader. Observed by AC35.
- **S41** — id 43, L7. `check_preset_pairs(assignment, pairs)` in `tools/policy/presets.py` is the one
  pair rule, called by `check_presets`, `check_repo_presets` and, through `python
  <prefix>/policy/presets.py pairs` with a JSON assignment on stdin, unit 20's
  `check_scenario_policy` in `tools/loop/scenario.py`. Observed by AC36.
- **S42** — id 53, L8. No `subject-pins.tsv` regen is written: units 6, 7, 21, 24 and 25's Files
  touched lines naming it are superseded, as spec 5 rev-1 already says. Observed by AC37.

## 3. Non-goals (OUT)

- The fixes of ids 45, 1, 2, 4, 16, 17, 22, 26, 32, 47, 54, 55, 57 and 58: units 30 to 43.
- Rewording sibling specs: each superseded text is named here and answered in its unit's ledger.
- The report's left-shift checklist entries and lints: no clause of this build names the bug-class
  checklist; where an item's criterion is the class arm, it says so.
- S23, S24 and S25 take no edge: they are close-time renders over whatever the earlier units left,
  sequenced by order 30, and nothing in them breaks if an earlier unit wrote less.

### Edges

- **consumes-from** `KICK-dKeptSession-1` — `arm_presets`, `check_repo_presets` and the presets comment, which S1, S32, S38 and S41 amend
- **consumes-from** `KICK-dKeptSession-2` — the reason text and AC6, which S12 replaces
- **consumes-from** `KICK-dKeptSession-4` — `adopt-policy.sh --scaffold`'s refusal path, S13
- **consumes-from** `KICK-dKeptSession-5` — `--mail post` and the transition guard, S28 to S30
- **consumes-from** `KICK-dKeptSession-7` — `derive_parent_reach`, the listing and `read_dependents`, S17 and S20
- **consumes-from** `KICK-dKeptSession-8` — the `actions.free` plants run under both pointer values, S10
- **consumes-from** `KICK-dKeptSession-9` — the orient report, its cap row and its sums, S11, S14, S15 and S40
- **consumes-from** `KICK-dKeptSession-10` — `read_mail_interrupts` and its `--local` step, S3, S16 and S19
- **consumes-from** `KICK-dKeptSession-11` — `emit_progress`, S33
- **consumes-from** `KICK-dKeptSession-12` — `print_replay`'s order and the fixture's shipping, S21 and S26
- **consumes-from** `KICK-dKeptSession-13` — the boundary verb, its local pointer rewrite and the `records —` line, S8, S10 and S22
- **consumes-from** `KICK-dKeptSession-14` — AC7 and the fill fixture, S35 and S39
- **consumes-from** `KICK-dKeptSession-16` — the list's ordinal, S36 and S37
- **consumes-from** `KICK-dKeptSession-18` — AC3, S34
- **consumes-from** `KICK-dKeptSession-20` — `check_scenario_policy`'s pair rule, S41
- **consumes-from** `KICK-dKeptSession-21` — `mail-notice.js`, its binding, reads and spawn, and `--local`, S3, S6 to S9, S18 and S31
- **consumes-from** `KICK-dKeptSession-25` — §7's covers list, S2
- **consumes-from** `KICK-dKeptSession-28` — `check_mail_recipient`'s cross-kit call, S27
- **consumes-from** `KICK-dKeptSession-36` — `resolve_bash`, which S16 and S17 route the engine's reads through
- **consumes-from** `KICK-dKeptSession-41` — the standing rows' summaries and the drained list, which S4 and S5 observe
- **hands-off** `KICK-dKeptSession-56` — S7, S16, S17, S20 and S33, §4's citations and §7's legs, the batch's S3, S19, S20, S23, S24, S34, S43, S26 and S27 (ids 5, 25, 27, 31, 32, 54, 42, 35, 36)

## 4. Design

### Evidence

Each item's evidence is the audit's appendix row for its id, re-read for this spec on 2026-10-26.
The claims re-verified at this base: `REFUSAL_CEILINGS` reads `unattended.sh:323` and `ARMS_FLOORS`
`unattended.sh:318:309` (`.memory-tree.conf:633`, `:649`); `SESSION-KICKOFF.md`'s `watch:` names
`tools/gate-legs.json`, `manifest-check.sh`, `.memory-tree.conf` and the charter template (line 6);
`memory/map/features/unattended.md:14` claims three harness hooks and not `mail-notice.js`;
`kickoff-manifest.kit.toml` is `kind = "flat"` with explicit `[[files]]`; `tools/unattended/kit.toml:12`
requires four kits and not `playbook-render`; `REMOTE_BOUND` is 60 seconds (`unattended.sh:162`), too
long for a lander's note, hence S33's own bound. dGroundRules' files are read at `3c8c4718a`.

### The boundary budget, S8

```
--card --boundary: at := HEAD (first) · deadline := now + CARD_BOUNDARY_BUDGET
  each step: timeout min(<its bound>, deadline - now) · mail reads --local · publish only if its bound fits
hook: BOUNDARY_BOUND_S = 10 > CARD_BOUNDARY_BUDGET = 8
```

### Inventory

| Minted | Kind | Home |
|---|---|---|
| `CARD_BOUNDARY_BUDGET`, `PROGRESS_BOUND` | constants | `manifest-check.sh`, `unattended.sh` |
| `derive_spent_tokens` | function | `tools/runlog/extract.py` |
| `check_preset_pairs`, `presets.py pairs` | function and verb | `tools/policy/presets.py` |
| `orient-refuse`, `orient-pinned` | plants | `tools/runlog/selftest.py` |
| `boundary-slow-remote` | plant | `skills/session-kickoff/card-store.fixture.sh` |
| `budgets-cap-orient-calls` | fixture case | `tools/policy/check_policy.py` |

### Migration

The decision row S23 may write, and the re-stamp S24 writes, are additive records. No stored state
changes shape.

### Files touched (estimate)

- `tools/policy/policy.py`, `tools/policy/check_policy.py`, `tools/policy/README.md`,
  `tools/policy/adopt-policy.sh`, `tools/policy/caps.toml`, `tools/policy/presets.py`,
  `tools/policy/presets.toml`
- `tools/loop/position.py`, `tools/loop/loop_transition.py`, `tools/loop/scenario.py`,
  `tools/loop/selftest.py`
- `tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`,
  `tools/unattended/mail-notice.js`, `tools/unattended/kit.toml`
- `tools/hooks/scratch-guard.js`, `tools/hooks/actions-free.fixture.sh`,
  `tools/hooks/scratch-guard.test.sh`
- `skills/session-kickoff/manifest-check.sh`, `skills/session-kickoff/card-store.fixture.sh`,
  `skills/session-kickoff/manifest-check.test.sh`
- `tools/runlog/runlog.py`, `tools/runlog/extract.py`, `tools/runlog/selftest.py`,
  `tools/runlog/fixtures/transcripts.json`, `tools/runlog/fixtures/context-fill.jsonl` (deleted)
- `tools/govkit/entries/kickoff-manifest.kit.toml`
- `.memory-tree.conf`, `memory/DECISIONS.md`, `memory/guides/SESSION-KICKOFF.md`
- `memory/map/features/unattended.md`, `memory/map/generated/`
- `memory/builds/dDeclaredLoop/BACKLOG.md`: S19's ask row
- `help/policy.md`, `help/loop.md`

### Alternatives rejected

- **Two batches.** S8, S10 and S18 each cross the kickoff and unattended kits, and S23 to S25 read
  every other item's output, so no two write sets are disjoint by M6's clauses.
- **Placing the batch beside each unit it lands on.** A batch is one unit with one order; past the
  last unit is the one place every item's code exists.

## 5. Production-readiness checklist

- security — S28 closes a release of another build's question; S29 and S30 fail closed; S31 hides a
  console window; S32 refuses a shadowed name.
- perf / scale — S8 bounds the boundary verb under the hook; S18 removes four spawns per tool call.
- error / empty / loading states — S29, S30 and S33 name every non-zero exit they meet.
- observability — S1 prints what it does not grade; S8 prints a skipped publish.
- risks — S23 may need a raise; the decision row records the review that admits it.
- testing — the criteria of §6 and the arms of §7.
- migration — §4.
- user docs — `help/policy.md` (S12, S32) and `help/loop.md` (S29, S34).

## 6. Acceptance criteria

Fixtures are each repaired unit's own, named by that unit's spec, under `%TEMP%`.

- **AC1** — When `python check_policy.py --repo .` runs while the ask is open, it prints
  `presets-core-only · not graded` and `arm_presets · 0 finding(s)`. Red when: the arm reds on the
  shipped tree for the ask's absence, or prints the half as graded.
- **AC2** — When `grep -n "renews: yes" tools/unattended/unattended.test.sh` runs, it prints no unit
  25 AC4 case, and unit 25's ledger answers AC4 `NOT OBSERVED`. Red when: a case that cannot pass
  ships red.
- **AC3** — When `bash unattended.sh --mail read fx --open --local` runs in unit 22's fixture, it
  exits 0, and `python position.py fx --mail-interrupts --local` against that real driver prints its
  mail line. Red when: the driver refuses `--local` as an unknown option.
- **AC4** — When a `tomllib` probe prints each of `actions.free`, `notify.owner` and `attendance`'s
  `summary`, each is `KICK-dKeptSession-41` S1's text, and `grep -cx` of the three names over
  `unsummarised-keys.txt` prints `0`. Red when: a row carries no summary, the base state.
- **AC5** — When `grep -n "PreToolUse" mail-notice.js` runs in the unattended kit, its header names
  `KICK-dKeptSession-13` S7 and the non-Bash tools, and unit 21's ledger records the probe's count per
  version. Red when: the hook states the false negative.
- **AC6** — When `bash card-store.fixture.sh --plant boundary-slow-remote` runs two Bash payloads with
  an unreachable remote, the first prints its advice within 10 s and the second spawns no verb.
  Red when: the hook kills the verb and prints nothing, or every call re-runs it.
- **AC7** — When `node mail-notice.js` reads a payload for an attended, card-routed
  session with no lease and one unread id, it prints `additionalContext` naming the id.
  Red when: a session routed by its card hears nothing.
- **AC8** — When `bash actions-free.fixture.sh` runs its plants under `card.pointers =
  "at-transitions"` after a crossing with no transition, a write inside the new item is admitted.
  Red when: the arm judges against the stale pointer.
- **AC9** — When `python runlog.py extract --orient` runs the `orient-refuse` and `orient-pinned`
  plants, each prints `orient REFUSED` and exits 1. Red when: a build ignoring `budgets.enforce`
  passes.
- **AC10** — When `grep -rnE "not applied|unapplied|no step applies" tools/policy help` runs, it
  prints nothing. Red when: a stale sentence survives in another wording.
- **AC11** — When `bash adopt-policy.sh --scaffold --preset lax --target <dir>` runs, it exits 2 and
  its stderr names `lax` and the four shipped presets. Red when: it exits 1 with the generic line.
- **AC12** — When `python budgets.py resolve orient-calls=default:0` runs in the policy kit, it exits
  0, and `python check_policy.py --fixture budgets-cap-orient-calls` passes. Red when: the census
  refuses the row.
- **AC13** — When `python budgets.py resolve AGENTS.md=default:0` runs after the row lands, it exits
  0. Red when: one incomplete row refuses every cap.
- **AC14** — When a probe stubs `subprocess.run` and calls `position.py`'s `read_mail_interrupts` and
  `derive_parent_reach` over a fixture build, each recorded `argv[0]` is `resolve_bash()`'s path.
  Red when: either read launches bare `bash`.
- **AC15** — When a probe writes unit 7's listing in a clone with `core.autocrlf=true` and in an LF
  clone, `python -c "import sys; print(b'\r' in open(sys.argv[1], 'rb').read())"` prints `False` for
  both and `check_interface_notice` confirms across them. Red when: the two keys differ.
- **AC16** — When one `mail-notice.js` call runs with logging stubs named `git` and `bash` first on
  PATH, neither stub logs a call. Red when: the hook reaches `readPolicy`'s spawns.
- **AC17** — When `python gen_build_index.py --asks --build dDeclaredLoop` runs, it lists the ask
  naming `--mail-interrupts` and TOOL-dDeclaredLoop-7 S4. Red when: the slot is removed with no
  parent text, or left armed by nobody.
- **AC18** — When `grep -n "def read_dependents" position.py` runs in the loop kit, it prints
  nothing, and a parent whose rendered edges name two children posts two notices. Red when: a
  second reader of `parents:` survives.
- **AC19** — When `--plant replay-order` replays, its first output line is the map block's first.
  Red when: the 10,000-character cap can cut the map.
- **AC20** — When `--plant pointers-cap` holds one record of every typed kind, the `records —` line
  names only base kinds and the card stays under `CARD_CAP_BYTES`. Red when: typed kinds grow the
  line until the pointers write is refused.
- **AC21** — When `python tools/memory-tree/check-arms.py --report` runs, `unattended.sh`'s census is
  at or under its `REFUSAL_CEILINGS` value, and any raise names a decision row in `DECISIONS.md`.
  Red when: the census passes its ceiling, or the ceiling moved with no review.
- **AC22** — When `git rev-list <the last-audit sha>..HEAD -- <each watch: path>` runs, it prints
  nothing. Red when: a watched file moved after the stamp.
- **AC23** — When `grep -n "mail-notice" memory/map/features/unattended.md` runs, it prints the
  claim, and a second `python tools/codebase-map/gen_map.py --write` leaves `git status --short
  memory/map` empty. Red when: the key is unclaimed or the render is stale.
- **AC24** — When `grep -n "card-compaction.fixture.sh" tools/govkit/entries/kickoff-manifest.kit.toml`
  and `grep -n "playbook-render" tools/unattended/kit.toml` run, each prints its row.
  Red when: an adopter installs a kit whose read file or required kit is absent.
  cost: a scratch install through the deployer is the full observation; the grep is the free one.
- **AC25** — When `bash unattended.sh --mail post fx --to build:dB --kind ack --answers <id> body`
  runs, it exits 2 naming `--mail ack`, and the row stays `open`. Red when: a third build's reply
  releases the row.
- **AC26** — When the guard's planted reader exits 3 with no output, the transition exits 2 naming
  `rc 3` and writes nothing. Red when: a crashed read passes as zero rows.
- **AC27** — When the fixture's origin is unreachable, `--mail post` exits 2 naming the fetch and
  builds no commit. Red when: a stale cache admits a duplicate.
- **AC28** — When a probe requires `mail-notice.js` with `child_process.spawn` stubbed, one spawn is
  recorded, `argv[1]` the driver and `windowsHide` `true`. Red when: the spawn opens a console.
- **AC29** — When the `presets-repo` case commits `[presets.strict]`, `python policy.py check` exits 1
  naming the line and `strict`. Red when: the declaration is silently ignored.
- **AC30** — When the progress verb is stubbed to sleep 30 s, `bash unattended.sh --landed <slug>`
  exits 0 within 12 s printing `progress not emitted`. Red when: the lander waits on the reader.
- **AC31** — When `grep -n "by path" loop.md` runs in `help/`, it prints the `repeat` route line.
  Red when: the criterion can only observe a record filed before the build.
- **AC32** — When `grep -rn "third list" tools/policy` runs, it prints nothing. Red when: the wrong
  ordinal ships.
- **AC33** — When `grep -n "v2:1424-1437" presets.toml` runs in the policy kit, it prints the
  comment. Red when: the cited range stops before the list's end.
- **AC34** — When `test -e context-fill.jsonl` runs in the runlog kit's fixtures, it exits 1, and
  `grep -c '"context-fill"' tools/runlog/fixtures/transcripts.json` prints `1`. Red when: a second
  fixture format survives.
- **AC35** — When `grep -c 'r\["in"\] + r\["out"\]' tools/runlog/runlog.py` runs, it prints `0`, and
  `grep -n "def derive_spent_tokens" tools/runlog/extract.py` prints one line. Red when: the sum is
  written twice.
- **AC36** — When `grep -c "def check_preset_pairs" presets.py` prints `1` in the policy kit and
  `grep -n "presets.py pairs" scenario.py` prints the call in the loop kit, a pair broken in a
  scenario slot is refused naming the pair. Red when: a third evaluation of the rule exists.
- **AC37** — When `git log --format=%h 462d20f3..HEAD -- tools/govkit/subject-pins.tsv` runs, each
  commit it prints also touches `tools/gate-legs.json`. Red when: a no-op regen is committed.

## 7. Gates

`kickoff-manifest ratchet` · `harness arms (fail branches armed or pinned)` · `codebase-map coverage + freshness` · `unattended kit gate` · `python resolver (behaviour + inline parity + idiom ban)` · `manifest-check self-test` · `scratch-guard self-test` · `agent-cap self-test` · `format-guard self-test` · `hook destinations self-test` · `review-join self-test` · `verifier fan-out self-test` · `runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `straggler-guard arms` · `transition-audit arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC25 AC27 AC30 · a third build's ack, an unreachable origin and a sleeping progress verb, each staged against the unit's base behaviour · `FLOOR_ASSERTIONS` and its shard floor rise by the arm's count, counted off the diff
New arm: tools/loop/selftest.py · covers AC14 AC15 AC18 AC26 · recorded argv, a CRLF clone, rendered edges and a reader exiting 3 · none
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC6 AC19 AC20 · the slow remote, the map-first replay and every typed kind · none
New arm: tools/hooks/scratch-guard.test.sh · covers AC8 · the `actions.free` plants under `at-transitions` · none
New arm: tools/policy/check_policy.py · covers AC12 AC29 AC36 · the orient cap case, a shadowed preset and a scenario's broken pair · none
New arm: tools/runlog/selftest.py · covers AC9 AC34 · the two orient plants and the scenario-written fill · none

## 8. Open questions

- **F1 — What does the `orient-calls` row carry as `research`, S14?** Options: (a) `0`, the header
  saying it names a cap outside the caps research; (b) a schema change making `research` optional;
  (c) `ships = false`. (c) is false, since the runlog kit ships the enforcer; (b) widens dGroundRules'
  schema for one row. (a) meets AC12 and AC13 with the census's presence-only check. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — Where does the boundary verb's budget come from, S8?** Options: (a) one deadline under the
  hook's bound, `at` moved first; (b) every networked step detached; (c) the hook's bound raised.
  (b) loses the advice the verb prints; (c) slows every Bash call on a slow remote. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3, the skeptic's first option. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, the round-1 spec audit's minors batch.
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-56` mirrored, the other ends of
  the edges the round-1 promotions' audit's disposal declared

## 10. Reuse audit

Every item extends the seam its repaired unit names, and the cross-cutting ones extend existing
mechanisms: `fail` and the retirement review for S23 (`tools/memory-tree/README.md` "The ceiling"),
the re-stamp of TOOL-dGroundRules-86 for S24, `map_lib.regen_cmd()` for S25
(`tools/codebase-map/map_lib.py:149`), `readCard` and `extractRouteUnits` for S9, `_derive_quartiles`
for S40, and the index generator's inversion of `parents:` for S20. `python
tools/codebase-map/reuse_lookup.py "resolve the bash that shares this filesystem by running each
candidate"` ranked the eight `resolve_bash` copies, so S16 and S17 take unit 36's rather than a ninth.
No item mints a mechanism where one of these fits.

Recall terms used: `python tools/memory-recall/query.py "how are a spec audit's confirmed findings
promoted into repair units placed after the unit they repair" --terms "spec-audit promoted repair unit
order hands-off consumes-from minors batch BLOCKER HIGH rescope add"`
