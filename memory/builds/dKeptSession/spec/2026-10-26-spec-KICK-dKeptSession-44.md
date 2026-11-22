# KICK-dKeptSession-44 — the round-1 spec audit's 42 minor findings, closed after every unit they land on is built

**Status:** DEFERRED · rev-5 · 2026-11-22 · node a · Tier-2 · base e0ac7bd2 · streams kickoff · order 30 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-30-promoted-fix-return.md](../build/2026-10-26-build-KICK-dKeptSession-30-promoted-fix-return.md) | research | KICK-dKeptSession-28 KICK-dKeptSession-36 KICK-dKeptSession-40 KICK-dKeptSession-43 KICK-dKeptSession-30 |
| [2026-10-26-build-KICK-dKeptSession-44-deviation-441.md](../build/2026-10-26-build-KICK-dKeptSession-44-deviation-441.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-44-deviation-442.md](../build/2026-10-26-build-KICK-dKeptSession-44-deviation-442.md) | deviation | — |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-41 KICK-dKeptSession-45 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-reground.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-reground.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-5 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-25 KICK-dKeptSession-36 KICK-dKeptSession-56 |
| [2026-10-26-prompt-KICK-dKeptSession-30-promoted-fix-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-30-promoted-fix-brief.md) | research | KICK-dKeptSession-28 KICK-dKeptSession-36 KICK-dKeptSession-40 KICK-dKeptSession-43 KICK-dKeptSession-30 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-30-ledger-class-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-30-ledger-class-brief.md) | research | KICK-dKeptSession-30 KICK-dKeptSession-32 KICK-dKeptSession-35 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-41 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-61-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-61-precheck-brief.md) | research | KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-56 |
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
text or answers a sibling's criterion, it does so by name here, and this unit's own acceptance
ledger, `memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-44-1-acceptance-ledger.md`,
quotes that text as it stands at that unit's rev and answers it (F3). Every unit whose text an item
answers builds before order 30 and is CLOSED when this unit builds, so neither its spec nor its
ledger is written.

## 2. Scope (IN)

- **S1** — id 3, M1. Met by `KICK-dKeptSession-1`: `arm_presets`' row-named half
  (`tools/policy/check_policy.py#check_preset_loads`) prints `presets-core-only · not graded ·
  TOOL-dDeclaredLoop-2 S8 admits after-release-verifies` and counts no finding while the expansion
  rule admits that value on a core-only register, and unit 1's own ledger observed its AC6 and AC9.
  This unit observes the line and records no second answer to unit 1's criteria. Observed by AC1.
- **S2** — id 5, M2. Withdrawn: its premise, an ask dPlacedRequest had not accepted, is gone.
  TOOL-dPlacedRequest-1 landed the renewal, and `KICK-dKeptSession-25` rev-6 keeps AC4 observable
  and on its own arm's covers list, as its hands-off edge to this batch states. No case is struck and
  no answer to unit 25's AC4 is recorded here. Observed by AC2.
- **S3** — id 6, M3. `--mail read`'s `--local` is parsed once, by `KICK-dKeptSession-21`'s addition,
  and `KICK-dKeptSession-10`'s step passes it to the real driver. Unit 10 AC2's stub is superseded by
  AC3's real-driver read. Observed by AC3.
- **S4** — id 7, M4. Met by `KICK-dKeptSession-41` S4, which answers units 8, 11 and 17's ACs 8, 6
  and 7 in its own ledger by the standing rows' summaries its S1 writes, each criterion named. This
  unit observes those summaries and records no second answer, so each criterion is answered in one
  record. Observed by AC4.
- **S5** — id 34, M4. The same defect by the reuse lens: this unit's ledger cites, for each of units
  8, 11 and 17, the standing row by its `name` line in `tools/policy/catalogue.toml` and its drain
  from `unsummarised-keys.txt`. Observed by AC4.
- **S6** — id 8, M5. One platform fact, one owner. `tools/unattended/mail-notice.js`'s header states
  that PreToolUse carries `additionalContext` (`KICK-dKeptSession-13` S7 owns that channel) and that
  this PostToolUse registration exists only to cover the tools scratch-guard's matcher does not route.
  `KICK-dKeptSession-21` rev-5 §8 F1 already records the `PreToolUse` builder and names unit 13 S7's
  channel, so no text of unit 21's is superseded here. Observed by AC5.
- **S7** — id 37, M5. The fact re-probed at the build: `grep -a -c 'hookName:\`PreToolUse:'` over the
  `claude` on PATH and, where installed, the version `RUN.md` pins, each count recorded with its
  version in this unit's ledger. Observed by AC5.
- **S8** — id 9, M6. Met by `KICK-dKeptSession-13` rev-7: S6's `--card --boundary` moves the session
  card's `at` to HEAD before any step, and S7's `checkItemBoundary` starts it detached and returns
  without waiting, so no hook bound cuts the verb and a second call at the same HEAD starts none.
  No budget constant is minted. Observed by AC6.
- **S9** — id 10, M7. `mail-notice.js` binds its build through `readCard` and `extractRouteUnits`, and
  falls back to `resolveLease`. The two functions are `tools/hooks/scratch-guard.js#readCard` and
  `#extractRouteUnits`, which its `module.exports` lists, carried inline in `mail-notice.js` as
  KICK-dKeptSession-56 S23 states, never required: a kit imports no sibling kit (TOOL-dGroundRules-1
  §4; TOOL-dDeclaredLoop-12 S4), and the unattended kit's `requires` in `tools/unattended/kit.toml`
  names no hooks kit. Observed by AC7.
- **S10** — id 11, M8. The local rewrite is met by `KICK-dKeptSession-13` S6 and AC3: the `item —`
  line is rewritten at every crossing under both values of `card.pointers`, and `at-transitions`
  gates only the publish. What stays owed is that unit 8's plants run under both values. Observed by
  AC8.
- **S11** — id 15, M9. `KICK-dKeptSession-9`'s plant `orient-refuse` sets `budgets.enforce =
  "refuse"`, and `orient-pinned` names `orient-calls` in `budgets.pinned`, each with a row past 30.
  Observed by AC9.
- **S12** — id 19, M10. Met at this base: `KICK-dKeptSession-2` rewrote the preset step's reason, and
  no "not applied" text stands in the policy kit or under `help/`. AC10's class grep observes it; unit
  2's own criteria are not answered here. Observed by AC10.
- **S13** — id 20, M11. `adopt-policy.sh --scaffold`'s write branch, where no policy file exists,
  runs `policy.py scaffold --preset <name>` with its stderr sent to `/dev/null` and turns any failure
  into `the scaffold could not be written` and exit 1; read 2026-11-22, `--preset lax` prints that
  line and exits 1. It passes the scaffold's exit 2 and its stderr through, as the kept-file branch
  already does (`KICK-dKeptSession-4` S3), keeping exit 1 for a write failure. Observed by AC11.
- **S14** — id 21, M12. The `orient-calls` row of `tools/policy/caps.toml` carries every census
  field: `research = 0`, the header gaining "0 names a cap no row of the caps research measured";
  `kit = "runlog"`; `installed = "{prefix}/runlog/runlog.py"`. `CAP_CASES` in `check_policy.py`
  gains `budgets-cap-orient-calls`. Observed by AC12.
- **S15** — id 46, M12. The blast radius: `resolve_caps` reads the census outside its `try`, so one
  incomplete row refuses every cap; AC13 reads a second cap after the row lands. Observed by AC13.
- **S16** — id 23, M13. `read_mail_interrupts` in `tools/loop/position.py` runs the driver through
  the loop kit's one resolver, `tools/loop/loop_witness.py#resolve_bash`, the inline copy of the
  canonical `tools/lib/resolve_bash.py#resolve_bash` that `KICK-dKeptSession-36` S1 observes, and the
  driver `resolve_kit_dir` locates, both imported inside the function as
  `tools/loop/loop_transition.py#write_card_follow` imports them. A `None` bash is a refusal naming
  the driver, never a bare `bash`. Observed by AC14.
- **S17** — id 24, M14. `derive_parent_reach`'s `--claims` read runs through `resolve_bash`, and the
  interface listing unit 7 S3 derives is written in binary mode, LF bytes, so a CRLF clone and an LF
  clone compute one key. Observed by AC14 and AC15.
- **S18** — id 27, M15. The boundary verb writes the resolved `mailbox.notice` and
  `mailbox.fetch-seconds` into the per-worktree sidecar beside the stamp (unit 21 §8 F2's file), and
  the hook reads them with the stamp's read and calls no `readPolicy`. Unit 21 S5's "spawns no git" and
  §4's cost paragraph then hold. Observed by AC16.
- **S19** — id 33, M16. The build files one ask in `memory/builds/dDeclaredLoop/BACKLOG.md`, target
  TOOL-dDeclaredLoop-7 S4, widening unit 10 §8 F3's: `derive_interrupts`' default prints no mail
  line once `position.py --mail-interrupts` is the one mail reader. Unit 10 AC1's plain-call clause,
  "the same plant's plain engine call prints", is answered against that text in this unit's ledger.
  Observed by AC17 and AC38.
- **S20** — id 35, M17. `read_dependents` is dropped. The dependents are the parent README's
  rendered `<!-- gen:build-edges -->` "Child builds" line (`tools/memory-tree/gen_build_index.py#render_edges`),
  the inversion of `parents:` that `tools/memory-tree/gen_build_index.py#plan` derives and refuses a
  dangling parent in. Observed by AC18.
  **Readers:** by name: READER NOT IN TREE — the function is minted by unit 7 in the loop kit, unbuilt
  at this base · by value: NO VALUE READERS — its one caller, unit 7's notices, is re-pointed here.
- **S21** — id 36, M18. Met by `KICK-dKeptSession-12` S5: `print_replay`
  (`skills/session-kickoff/manifest-check.sh#print_replay`) opens with `derive_map_block`'s lines
  (PLAY-dOrderedCharter-4), then the stored card, the computed lines and `now —` last, the order its
  comment states, and the landed `replay-order` plant of `card-store.fixture.sh` replays it. This unit
  observes it. Observed by AC19.
- **S22** — id 40, M19. The `records —` line `KICK-dKeptSession-13` S5 prints names only the base
  kinds, `RECORD_KIND_TOKENS` less `TYPED_RECORD_KINDS` (`tools/memory-tree/tree_lib.py`), so typed
  kinds the chain mints never lengthen it. The plant `pointers-cap` of `card-store.fixture.sh` holds
  one record of every typed kind. Observed by AC20.
- **S23** — id 48, M20. The driver's refusal census, read once after every driver unit by `python
  tools/memory-tree/check-arms.py --report`. A new refusal routes through `fail` where it can; a
  census still past the driver's `REFUSAL_CEILINGS` row takes the retirement review the memory-tree README's
  "The ceiling" names, and the ceiling rises only to the census left, under a dated decision id in
  `memory/DECISIONS.md`, with the `.memory-tree.conf` rows of `REFUSAL_CEILINGS` and `ARMS_FLOORS`.
  Observed by AC21.
- **S24** — id 49, M21. One kickoff re-stamp per write set. `memory/guides/SESSION-KICKOFF.md`'s
  `last-audit` is re-stamped after this unit's last edit to any `watch:` path, with its delta line, as
  TOOL-dGroundRules-86 did for its build. `KICK-dKeptSession-56` and the units after it edit watched
  files too, so each re-stamps for its own edits. Observed by AC22.
- **S25** — id 50, M22. `memory/map/features/unattended.md`'s `harness-hooks` list claims `PostToolUse
  tools/unattended/mail-notice.js`, and the map is regenerated once by the command `map_lib.regen_cmd()`
  prints, `python tools/codebase-map/gen_map.py --write`, which moves `memory/map/generated/symbols.json`
  by every function the items add. Observed by AC23.
- **S26** — id 51, M23. Met by `KICK-dKeptSession-12` S1 and an exemption another build recorded (§8
  F4): `tools/govkit/registry.toml` exempts `card-compaction.fixture.sh` as gov's live fixture,
  deliberately not shipped (PLAY-dOrderedCharter-77 S7), and an adopter's engine reads its absence
  as `red: no fixture installed` (`skills/session-kickoff/manifest-check.sh#read_card_fixture_verdict`),
  never as a missing file. No `[[files]]` row is added. Observed by AC24.
- **S27** — id 52, M24. `tools/unattended/kit.toml`'s `requires` gains `playbook-render`, the kit
  `check_mail_recipient`'s call to the landed `check_fleet_tag` reads through `read_fleet`
  (`KICK-dKeptSession-28` S3; `tools/unattended/unattended.sh#check_fleet_tag`). Observed by AC24.
- **S28** — id 56, M25. `--mail post` refuses `--kind ack` and `--kind answer` with exit 2, naming
  `--mail ack` and `--mail answer`. Observed by AC25.
- **S29** — id 59, M26. Met by `KICK-dKeptSession-5` rev-11 S9: a read exiting non-zero with no row
  raises its `ValueError` naming the exit and the first line, which `record` prints after `loop:
  unanswered` and exits 2 on, and only `mail — off`, the locator's `LookupError`, a root with no
  `.unattended.conf` and zero rows pass. This unit observes it with one plant, `mail-read-crash`,
  whose planted reader exits 3 with no output. Observed by AC26.
- **S30** — id 60, M27. A failed or timed-out fetch in `--mail post` refuses with exit 2 and the
  fetch's cause before any commit. Observed by AC27.
- **S31** — id 61, M28. The hook's detached spawn sets `windowsHide: true`, as the spawns of
  `tools/hooks/format-guard.js` and `tools/unattended/stop-guard.js` do. Observed by AC28.
- **S32** — id 62, M29. `validate` refuses a `[presets.<shipped name>]` table, naming its line and
  the name. Observed by AC29.
- **S33** — id 63, M30. `print_progress`, `KICK-dKeptSession-11` S5's driver emitter, runs bounded by
  a new `PROGRESS_BOUND=10` through `run_bounded`, as `KICK-dKeptSession-56` S24 spells the call; a
  non-zero exit or a timeout prints `NOTE — progress not emitted: <why>` and never moves the verb's
  exit or lines. Observed by AC30.
- **S34** — id 12, L1. Met by `KICK-dKeptSession-18` rev-5: its AC5 observes the build, the route by
  path on `help/loop.md`, and its AC3 reads the filed ask as met at base. This unit observes the page.
  Observed by AC31.
- **S35** — id 13, L2. Unit 14 AC7 is withdrawn; its S5 cites `KICK-dKeptSession-13` AC5, which
  observes the `agent_type` skip. NOT OBSERVED here: the criterion moves to the unit that owns the
  check, and this unit's ledger answers it by that citation, quoting unit 14 §8 F4's "AC7 withdrawn
  and S6 citing KICK-dKeptSession-13 AC5", which lands both at unit 14's own build.
- **S36** — id 14, L3. Met by `KICK-dKeptSession-16`: its spec and the policy kit's `README.md` call
  `unpurposed-namespaces.txt` the fourth list, beside `unsummarised-keys.txt`, `legacy-homes.txt` and
  `KICK-dKeptSession-19`'s `unnamed-keys.txt`. Observed by AC32.
- **S37** — id 44, L3. Met by the same unit: its §10 already says the fourth, so no text is
  superseded. Observed by AC32.
- **S38** — id 18, L4. Met by `KICK-dKeptSession-1`: the landed `never` list's comment in
  `tools/policy/presets.toml` cites no line range of the design record, so none can stop before the
  list's end. Observed by AC33.
- **S39** — id 41, L5. Unit 14's fixture is a `context-fill` scenario of
  `tools/runlog/fixtures/transcripts.json`, and `context-fill.jsonl` is deleted. Observed by AC34.
  **Readers:** by name: READER NOT IN TREE — the file's one reader is unit 14's selftest case, unbuilt
  at this base · by value: NO VALUE READERS — its bytes are read only by that case, re-pointed here.
- **S40** — id 42, L6. Unit 9's quartiles call `tools/runlog/runlog.py#_derive_quartiles`, and the
  four-field token sum is one function, `derive_spent_tokens` in `tools/runlog/extract.py`, beside
  `KICK-dKeptSession-14`'s `derive_context_tokens`, called by `tools/runlog/runlog.py#print_ready`,
  whose `spent_tokens` row spells the sum today, and unit 9's reader. Observed by AC35.
- **S41** — id 43, L7. Met by `KICK-dKeptSession-1` and `KICK-dKeptSession-20`: the one pair rule is
  `tools/policy/presets.py#check_pairs`, called by `check_presets` and by the `pairs` verb
  (`tools/policy/presets.py#run_pairs`) that `tools/loop/scenario.py` runs as a subprocess on a
  scenario slot's assignment; `check_repo_presets` judges no pair, as unit 1 §8 F10 ruled. No
  `check_preset_pairs` is minted. Observed by AC36.
- **S42** — id 53, L8. No `subject-pins.tsv` regen is written: units 6, 7, 21, 24 and 25's Files
  touched lines naming it are superseded, as spec 5 rev-1 already says. Observed by AC37.

## 3. Non-goals (OUT)

- The fixes of ids 45, 1, 2, 4, 16, 17, 22, 26, 32, 47, 54, 55, 57 and 58: units 30 to 43.
- Rewording sibling specs: each superseded text is named here and answered in this unit's own
  ledger (F3).
- The report's left-shift checklist entries and lints: no clause of this build names the bug-class
  checklist; where an item's criterion is the class arm, it says so.
- S23, S24 and S25 take no edge: they are close-time renders over whatever the earlier units left,
  sequenced by order 30, and nothing in them breaks if an earlier unit wrote less.

### Edges

- **consumes-from** `KICK-dKeptSession-1` — `check_repo_presets`, which S32 amends, and `arm_presets`, the presets comment and `check_pairs`, which S1, S38 and S41 observe
- **consumes-from** `KICK-dKeptSession-2` — the rewritten reason text, which S12 observes
- **consumes-from** `KICK-dKeptSession-4` — `adopt-policy.sh --scaffold`'s refusal path, S13
- **consumes-from** `KICK-dKeptSession-5` — `--mail post` and the transition guard, S28 to S30
- **consumes-from** `KICK-dKeptSession-7` — `derive_parent_reach`, the listing and `read_dependents`, S17 and S20
- **consumes-from** `KICK-dKeptSession-8` — the `actions.free` plants run under both pointer values, S10
- **consumes-from** `KICK-dKeptSession-9` — the orient report, its cap row and its sums, S11, S14, S15 and S40
- **consumes-from** `KICK-dKeptSession-10` — `read_mail_interrupts` and its `--local` step, S3, S16 and S19
- **consumes-from** `KICK-dKeptSession-11` — `print_progress`, S33
- **consumes-from** `KICK-dKeptSession-12` — `print_replay`'s order and the fixture's shipping, S21 and S26
- **consumes-from** `KICK-dKeptSession-13` — the boundary verb, its local pointer rewrite and the `records —` line, S8, S10 and S22
- **consumes-from** `KICK-dKeptSession-14` — AC7 and the fill fixture, S35 and S39
- **consumes-from** `KICK-dKeptSession-16` — the list's ordinal, S36 and S37
- **consumes-from** `KICK-dKeptSession-18` — AC3, S34
- **consumes-from** `KICK-dKeptSession-20` — the scenario check's `presets.py pairs` call, which S41 observes
- **consumes-from** `KICK-dKeptSession-21` — `mail-notice.js`, its binding, reads and spawn, and `--local`, S3, S6 to S9, S18 and S31
- **consumes-from** `KICK-dKeptSession-25` — §7's covers list, S2
- **consumes-from** `KICK-dKeptSession-28` — `check_mail_recipient`'s cross-kit call, S27
- **consumes-from** `KICK-dKeptSession-36` — the loop kit's `resolve_bash`, which S16 and S17 route the engine's reads through
- **consumes-from** `KICK-dKeptSession-41` — the standing rows' summaries and the drained list, which S4 and S5 observe
- **hands-off** `KICK-dKeptSession-56` — S7, S16, S17, S20 and S33, §4's citations and §7's legs, the batch's S3, S19, S20, S23, S24, S34, S43, S26 and S27 (ids 5, 25, 27, 31, 32, 54, 42, 35, 36)

## 4. Design

### Evidence

Each item's evidence is the audit's appendix row for its id, re-read for this spec on 2026-10-26,
and re-checked against the landed tree at `e0ac7bd2` on 2026-11-22. The driver's rows of
`.memory-tree.conf#REFUSAL_CEILINGS` and `.memory-tree.conf#ARMS_FLOORS` are read by key, the ceiling
dated with its decision (PINNED 2026-11-22: 343); `SESSION-KICKOFF.md`'s `watch:` line names
`manifest-check.sh`, `.memory-tree.conf`, `tools/gate-legs.json` and the charter template among its
paths; `memory/map/features/unattended.md`'s `harness-hooks` list claims three hooks and not
`mail-notice.js`; `tools/unattended/kit.toml`'s `requires` names five kits (PINNED 2026-11-22) and not
`playbook-render`; `REMOTE_BOUND` is 60 seconds, too long for a lander's note, hence S33's own
bound. Items S1, S4, S8, S12, S21, S26, S29, S34, S36 to S38 and S41 are met by landed or earlier
units, each item naming the unit, and are reduced to their observation.

### Inventory

| Minted | Kind | Home |
|---|---|---|
| `PROGRESS_BOUND` | constant | `unattended.sh` |
| `derive_spent_tokens` | function | `tools/runlog/extract.py` |
| `orient-refuse`, `orient-pinned` | plants | `tools/runlog/selftest.py` |
| `pointers-cap` | plant | `skills/session-kickoff/card-store.fixture.sh` |
| `mail-read-crash` | plant | `tools/loop/loop_transition.py` |
| `budgets-cap-orient-calls` | fixture case | `tools/policy/check_policy.py` |

### Migration

The decision row S23 may write, and the re-stamp S24 writes, are additive records. No stored state
changes shape.

### Files touched (estimate)

- `tools/policy/check_policy.py`, `tools/policy/adopt-policy.sh`, `tools/policy/caps.toml`,
  `tools/policy/presets.py`: S13, S14, S32
- `tools/loop/position.py`: S16, S17, S20; `tools/loop/loop_transition.py`: S29's `mail-read-crash`
  plant, a branch of `run_transition_fixture`
- `tools/run-gates/selftest-budgets.txt`: the `loop transition record` row's `plants=` token one above
  its count at the unit's base and its note's re-read (DERIVED: `len(PLANTS)`), moved in place, since
  the check refuses a note carrying two `plants=` tokens; `position.py` gains no plant
- `tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`,
  `tools/unattended/mail-notice.js`, `tools/unattended/kit.toml`
- `tools/hooks/actions-free.fixture.sh`, `tools/hooks/scratch-guard.test.sh`: S10
- `skills/session-kickoff/manifest-check.sh`, `skills/session-kickoff/card-store.fixture.sh`,
  `skills/session-kickoff/manifest-check.test.sh`: S22
- `tools/runlog/runlog.py`, `tools/runlog/extract.py`, `tools/runlog/selftest.py`,
  `tools/runlog/fixtures/transcripts.json`, `tools/runlog/fixtures/context-fill.jsonl` (deleted)
- `.memory-tree.conf`, `memory/DECISIONS.md`, `memory/guides/SESSION-KICKOFF.md`: S23, S24
- `memory/map/features/unattended.md`, `memory/map/generated/symbols.json` and the rest of
  `memory/map/generated/`: S25's render
- `memory/builds/dDeclaredLoop/BACKLOG.md`: S19's ask row
- `memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-44-1-acceptance-ledger.md`:
  every answer §1 and the items name, beside the criteria observed
- `help/policy.md`, `help/loop.md`

### Alternatives rejected

- **Two batches.** S10 and S18 each cross the hooks, kickoff and unattended kits, and S23 to S25 read
  every other item's output, so no two write sets are disjoint by M6's clauses.
- **Placing the batch beside each unit it lands on.** A batch is one unit with one order; past the
  last unit is the one place every item's code exists.

## 5. Production-readiness checklist

- security — S28 closes a release of another build's question; S29 and S30 fail closed; S31 hides a
  console window; S32 refuses a shadowed name.
- perf / scale — S18 removes four spawns per tool call; S33 bounds the lander's progress line.
- error / empty / loading states — S29, S30 and S33 name every non-zero exit they meet.
- observability — S1's line names what the arm does not grade; S33's `NOTE` names a progress line not
  emitted.
- risks — S23 may need a raise; the decision row records the review that admits it.
- testing — the criteria of §6 and the arms of §7.
- migration — §4.
- user docs — `help/policy.md` (S32) and `help/loop.md`, which unit 5 S14 and unit 18 S6 write and S29
  and S34 observe.

## 6. Acceptance criteria

Fixtures are each repaired unit's own, named by that unit's spec, under `%TEMP%`.

- **AC1** — When `python check_policy.py --repo .` runs in the policy kit while the ask is open, it
  prints `policy-check: arm_presets · 0 finding(s)` and the row-named half's `presets-core-only · not
  graded` line. Red when: the arm reds on the shipped tree for the ask's absence, or prints the half
  as graded.
- **AC2** — When `grep -n 'covers AC2 AC3 AC4 AC5' memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-25.md`
  runs, it prints unit 25's `New arm:` line, and this unit's ledger, read, records no answer to unit
  25's AC4. Red when: a criterion unit 25's own arm observes is struck or answered here.
- **AC3** — When `bash unattended.sh --mail read fx --open --local` runs in unit 22's fixture, it
  exits 0, and `python position.py fx --mail-interrupts --local` against that real driver prints its
  mail line. Red when: the driver refuses `--local` as an unknown option.
- **AC4** — When a `tomllib` probe prints each of `actions.free`, `notify.owner` and `attendance`'s
  `summary`, each is `KICK-dKeptSession-41` S1's text, and `grep -cx` of the three names over
  `unsummarised-keys.txt` prints `0`. Red when: a row carries no summary, the state before unit 41.
- **AC5** — When `grep -n "PreToolUse" mail-notice.js` runs in the unattended kit, its header names
  `KICK-dKeptSession-13` S7 and the non-Bash tools, and this unit's ledger records the probe's count
  per version. Red when: the hook states the false negative.
- **AC6** — `KICK-dKeptSession-13` AC2 and AC5 hold: the boundary verb moves `at` before its steps,
  and `checkItemBoundary` records one detached call that it does not wait on, none at an unchanged
  HEAD. Red when: the hook waits on the verb, or every call re-runs it.
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
  `derive_parent_reach` over a fixture build, each recorded `argv[0]` is the answer of
  `loop_witness.resolve_bash(<driver>)` for the driver the call names. Red when: either read launches
  bare `bash`.
- **AC15** — When a probe writes unit 7's listing in a clone with `core.autocrlf=true` and in an LF
  clone, `python -c "import sys; print(b'\r' in open(sys.argv[1], 'rb').read())"` prints `False` for
  both and `check_interface_notice` confirms across them. Red when: the two keys differ.
- **AC16** — When one `mail-notice.js` call runs with logging stubs named `git` and `bash` first on
  PATH, neither stub logs a call. Red when: the hook reaches `readPolicy`'s spawns.
- **AC17** — When `python gen_build_index.py --asks --build dDeclaredLoop` runs, it lists the ask
  naming `--mail-interrupts` and TOOL-dDeclaredLoop-7 S4. Red when: the slot is removed with no
  parent text, or left armed by nobody.
- **AC18** — When `grep -rn "def read_dependents" tools/loop` runs, it prints nothing, and
  `KICK-dKeptSession-35`'s `notices-two-dependents` plant, whose parent README's rendered edges name
  two children, still prints its two notices. Red when: a second reader of `parents:` survives.
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
- **AC24** — When `grep -n "playbook-render" tools/unattended/kit.toml` runs, it prints the `requires`
  row; `grep -n "card-compaction.fixture.sh" tools/govkit/registry.toml` prints its `[[exempt]]` row;
  and `grep -c "no fixture installed" skills/session-kickoff/manifest-check.sh` prints `1`.
  Red when: an adopter installs a kit whose required kit is absent, or reads an absent fixture as
  anything but a named red.
  cost: a scratch install through the deployer is the full observation; the grep is the free one.
- **AC25** — When `bash unattended.sh --mail post fx --to build:dB --kind ack --answers <id> body`
  runs, it exits 2 naming `--mail ack`, and the row stays `open`. Red when: a third build's reply
  releases the row.
- **AC26** — When `python tools/loop/loop_transition.py --fixture --plant mail-read-crash` has the
  guard's planted reader exit 3 with no output, `record` exits 2 printing `loop: unanswered · ` and
  the read's exit, and `loop: fixture · commits unchanged`. Red when: a crashed read passes as zero
  rows.
- **AC27** — When the fixture's origin is unreachable, `--mail post` exits 2 naming the fetch and
  builds no commit. Red when: a stale cache admits a duplicate.
- **AC28** — When a probe requires `mail-notice.js` with `child_process.spawn` stubbed, one spawn is
  recorded, `argv[1]` the driver and `windowsHide` `true`. Red when: the spawn opens a console.
- **AC29** — When the `presets-repo` case commits `[presets.strict]`, `python policy.py check` exits 1
  naming the line and `strict`. Red when: the declaration is silently ignored.
- **AC30** — When the progress verb is stubbed to sleep 30 s, `bash unattended.sh --landed <slug>`
  exits 0 within 12 s printing `progress not emitted`. Red when: the lander waits on the reader.
- **AC31** — When `grep -n "by path" loop.md` runs in `help/`, it prints the `repeat` route line unit
  18 S6 writes. Red when: the page omits the route by path.
- **AC32** — When `grep -rn "third list" tools/policy` runs, it prints nothing. Red when: the wrong
  ordinal ships.
- **AC33** — When `grep -n "presets never touch" presets.toml` runs in the policy kit, it prints the
  `never` list's comment, and `grep -c "1424" presets.toml` prints `0`. Red when: a cited range stops
  before the list's end.
- **AC34** — When `test -e context-fill.jsonl` runs in the runlog kit's fixtures, it exits 1, and
  `grep -c '"context-fill"' tools/runlog/fixtures/transcripts.json` prints `1`. Red when: a second
  fixture format survives.
- **AC35** — When `grep -c 'r\["in"\] + r\["out"\]' tools/runlog/runlog.py` runs, it prints `0`, and
  `grep -n "def derive_spent_tokens" tools/runlog/extract.py` prints one line. Red when: the sum is
  written twice.
- **AC36** — When `grep -c "def check_pairs" presets.py` prints `1` in the policy kit and `grep -n
  '"pairs"' scenario.py` prints the subprocess call in the loop kit, a pair broken in a scenario slot
  is refused by `presets.py pairs` naming the pair. Red when: a second evaluation of the rule exists.
- **AC37** — When `git log --format=%h 462d20f3..HEAD -- tools/govkit/subject-pins.tsv` runs, each
  commit it prints also touches `tools/gate-legs.json`. Red when: a no-op regen is committed.
- **AC38** — `tr -s ' \r\n' ' '` over this unit's acceptance ledger piped into `grep -c` prints `1`
  for each of "the same plant's plain engine call prints" and "AC7 withdrawn and S6 citing
  KICK-dKeptSession-13 AC5", the two sibling passages this unit still answers; and `git diff
  --name-only <pass base> HEAD --` over the specs and acceptance ledgers of units 1, 8, 10, 11, 14,
  17, 21 and 25 prints nothing. Red when: an answer lands in a record of a unit it names, or this
  unit's ledger leaves a quoted passage out.

## 7. Gates

`kickoff-manifest ratchet` · `loop transition record` · `loop position fixtures` · `every held leg is budgeted, every budget row resolves` · `harness arms (fail branches armed or pinned)` · `codebase-map coverage + freshness` · `unattended kit gate` · `python resolver (behaviour + inline parity + idiom ban)` · `manifest-check self-test` · `scratch-guard self-test` · `agent-cap self-test` · `format-guard self-test` · `hook destinations self-test` · `review-join self-test` · `verifier fan-out self-test` · `runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `kit/dogfood doc parity` · `policy fixtures` · `build-index selftest` · `gotchas selftest` · `routed-commits selftest` · `memory-recall kit selftest` · `tier2-review self-test` · `recall floor` · `recall floor arms` · `straggler-guard arms` · `transition-audit arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC25 AC27 AC30 · a third build's ack, an unreachable origin and a sleeping progress verb, each staged against the unit's base behaviour · `FLOOR_ASSERTIONS` and its shard floor rise by the arm's count, counted off the diff
New arm: tools/loop/loop_transition.py · covers AC26 · the `mail-read-crash` plant, a reader exiting 3 with no output, staged red by a scratch copy of the guard reading a crashed read as zero rows · the `loop transition record` row's `plants=<n>` token rises by one
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC20 · the `pointers-cap` plant holding every typed kind · none
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
  At rev-5 the question is moot: `KICK-dKeptSession-13` rev-7 moves `at` first and starts the verb
  detached, so the hook's 10 s bound rev-4 budgeted under applies to nothing, and S8 is reduced to
  its observation.
- **F3 — Where are the answers to the sibling texts and criteria the items name recorded?** Every
  unit whose text an item answers builds before order 30, so each is CLOSED when this unit builds,
  and their
  ledgers are in neither this unit's Files touched nor its write set. (a) Each named unit's
  acceptance ledger, a record of a closed unit written by a later one; (b) this unit's own
  acceptance ledger, quoting each sibling text it answers. Recommendation (b). RESOLVED (agent,
  2026-11-21, delegated): (b), rung 3; a CLOSED unit's records are never written by a later unit, as
  KICK-dKeptSession-49 rev-6 ruled. Rejected: (a), writing the other unit's ledger. The main loop's
  ruling, in `2026-11-21-prompt-KICK-dKeptSession-30-ledger-class-brief`.
  widens: none · relaxes: none
- **F4 — Does the kickoff kit ship `card-compaction.fixture.sh`, S26?** The audit read an adopter
  installing an engine whose read file is absent. Options: (a) a `[[files]]` row in
  `kickoff-manifest.kit.toml`, removing the registry's `[[exempt]]` row; (b) no row: the exemption
  stands and the engine's landed verdict names the absence. (a) reverses PLAY-dOrderedCharter-77 S7, a
  decision of another build, and ships a fixture that spends minutes of model time on a target with
  no build card to prove; (b) leaves no silent read, since `read_card_fixture_verdict` answers `red: no
  fixture installed` (`KICK-dKeptSession-12` S1). Recommendation (b). RESOLVED (agent, 2026-11-21,
  delegated): (b), rung 3; the absence is already read and named, and the exemption is another
  build's recorded decision. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, the round-1 spec audit's minors batch.
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-56` mirrored, the other ends of
  the edges the round-1 promotions' audit's disposal declared
- rev-3 · 2026-10-26 · S9 · §10 · re-grounded on the cross-check record
  `2026-10-26-build-KICK-dKeptSession-1-parents-crosscheck`, row 105: `mail-notice.js` carries
  `readCard` and `extractRouteUnits` inline, aligned with KICK-dKeptSession-56 S23, and requires no
  file of the hooks kit.
- rev-4 · 2026-11-21 · §1 · S1 · S2 · S4 · S5 · S7 · S19 · S35 · §3 · §4 · AC2 · AC5 · AC38 ·
  §7 · §8 · every answer the items placed in units 1, 8, 10, 11, 14, 17, 21 and 25's ledgers
  moves to this unit's own acceptance ledger, which joins Files touched, F3 resolved (b) and AC38
  observing the quoted passages, under the brief
  `2026-11-21-prompt-KICK-dKeptSession-30-ledger-class-brief`; the class KICK-dKeptSession-49 rev-6
  first resolved. S5's line citations re-cited to the rows' `name` lines; S35 quotes unit 14 rev-5's
  F4, which withdraws AC7 at that unit's own build. The ledger's path trips the two `recall floor`
  legs, already on §7's leg line. §7's line gains the six legs the spec-token checker's guards join
  named at rev-3 over `tools/policy/policy.py` and `tools/unattended/unattended.sh`, `policy
  fixtures` among them.

- rev-5 · 2026-11-22 · §1 · S1 · S2 · S4 · S6 · S8 to S10 · S12 · S13 · S14 · S16 · S20 to S27 · S29 ·
  S31 · S33 · S34 · S36 to S38 · S40 · S41 · §3 · §4 · §5 · AC1 · AC2 · AC4 · AC6 · AC14 · AC18 ·
  AC24 · AC26 · AC31 · AC33 · AC36 · AC38 · §7 · §8 F2 F4 · §10 · checked for behaviour by
  `2026-11-21-prompt-KICK-dKeptSession-61-precheck-brief` against `e0ac7bd2`: items met by landed or
  earlier units reduced to their observation (S1 and S38 by unit 1, S12 by unit 2, S21 by unit 12, S36
  and S37 by unit 16, S41 by units 1 and 20, S4 by unit 41's own ledger, S8 and half of S10 by unit
  13 rev-7, S29 by unit 5 S9, S34 by unit 18 rev-5), and their quotes leave AC38; S2 withdrawn, unit
  25's edge having retired its premise; S6, S12, S36 and S37 name no supersession their sources
  already carry; S26 ruled by F4 against shipping the live fixture; S27's reason re-pointed to
  `check_fleet_tag` and S33's emitter spelled `print_progress`; S16 and S17 read the loop kit's
  resolver in `loop_witness.py`; the absent `tools/loop/selftest.py` arm moved to a
  `loop_transition.py` plant, whose `plants=` token joins Files touched, and `symbols.json` named;
  every `path:number` citation re-cited by symbol, key or description, and the base moved to
  `e0ac7bd2`.

## 10. Reuse audit

Every item extends the seam its repaired unit names, and the cross-cutting ones extend existing
mechanisms: `fail` and the retirement review for S23 (`tools/memory-tree/README.md` "The ceiling"),
the re-stamp of TOOL-dGroundRules-86 for S24, `map_lib.regen_cmd()` for S25
(`tools/codebase-map/map_lib.py#regen_cmd`), `readCard` and `extractRouteUnits` for S9, carried inline as
`tools/unattended/gate-guard.js#buildHeredocView` carries its copy of a `scratch-guard.js` function, `_derive_quartiles`
for S40, and the index generator's inversion of `parents:` for S20. `python
tools/codebase-map/reuse_lookup.py "resolve the bash that shares this filesystem by running each
candidate"` ranked the `resolve_bash` copies, so S16 and S17 take the loop kit's inline copy of the
canonical in `loop_witness.py` rather than another.
No item mints a mechanism where one of these fits.

Recall terms used: `python tools/memory-recall/query.py "how are a spec audit's confirmed findings
promoted into repair units placed after the unit they repair" --terms "spec-audit promoted repair unit
order hands-off consumes-from minors batch BLOCKER HIGH rescope add"`
