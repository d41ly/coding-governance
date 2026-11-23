# KICK-dKeptSession-44 — the round-1 spec audit's 42 minor findings, closed after every unit they land on is built

**Status:** DEFERRED · rev-6 · 2026-11-23 · node a · Tier-2 · base ff2654fc · streams kickoff · order 30 · advances KICK-dKeptSession-29

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
| [2026-11-22-prompt-KICK-dKeptSession-44-reground-brief.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-44-reground-brief.md) | research | — |
| [2026-11-23-prompt-KICK-dKeptSession-44-1-spec-writer.md](../prompts/2026-11-23-prompt-KICK-dKeptSession-44-1-spec-writer.md) | journal | — |
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
quotes that text and answers it (F3); no sibling's spec or ledger is written.

## 2. Scope (IN)

- **S1** — id 3, M1. Met by `KICK-dKeptSession-1`: `arm_presets`' row-named half
  (`tools/policy/check_policy.py#check_preset_loads`) prints `presets-core-only · not graded ·
  TOOL-dDeclaredLoop-2 S8 admits after-release-verifies` and counts no finding; unit 1's ledger
  answers its AC6 and AC9, and this unit observes the line. Observed by AC1.
- **S2** — id 5, M2. Withdrawn: TOOL-dPlacedRequest-1 landed the renewal, retiring its premise,
  and `KICK-dKeptSession-25` keeps AC4 on its own arm's covers list, as its hands-off edge states;
  nothing is struck or answered here. Observed by AC2.
- **S3** — id 6, M3. Met by `KICK-dKeptSession-21` S2, which parses `--local` once on `--mail read`,
  and by unit 10's landed `tools/loop/loop_transition.py#read_mail_rows`, which appends it. Unit 10
  AC2's stub is superseded by AC3's real-driver read. Observed by AC3.
- **S4** — id 7, M4. Met by `KICK-dKeptSession-41` S4, whose ledger answers units 8, 11 and 17's
  ACs 8, 6 and 7 by the summaries its S1 writes; this unit observes them and answers none again.
  Observed by AC4.
- **S5** — id 34, M4. The same defect by the reuse lens: this unit's ledger cites, for each of units
  8, 11 and 17, the standing row by its `name` line in `tools/policy/catalogue.toml` and its drain
  from `unsummarised-keys.txt`. Observed by AC4.
- **S6** — id 8, M5. One platform fact, one owner. `tools/unattended/mail-notice.js`'s header states
  that PreToolUse carries `additionalContext` (`KICK-dKeptSession-13` S7 owns that channel) and that
  this PostToolUse registration exists only to cover the tools scratch-guard's matcher does not route.
  Unit 21 §8 F1 already names that channel, so none of its text is superseded. Observed by AC5.
- **S7** — id 37, M5. The fact re-probed at the build: `grep -a -c 'hookName:\`PreToolUse:'` over the
  `claude` on PATH and the `cli-version` `memory/builds/dKeptSession/RUN.md` pins, each count recorded
  with its version in this unit's ledger; read 2026-11-23, 2.1.319 counts 5 and the pin is 2.1.326
  (PINNED). Observed by AC5.
- **S8** — id 9, M6. Met by `KICK-dKeptSession-13`: `--card --boundary` moves the card's `at` to
  HEAD before any step, and `checkItemBoundary` starts it detached without waiting, none at an
  unchanged HEAD. Observed by AC6.
- **S9** — id 10, M7. `mail-notice.js` binds its build with no spawn, as
  `tools/hooks/scratch-guard.js#checkItemBoundary` does: the tree's card at `CARD_FILE_REL` whose
  `card-owner —` line names the session, its build `extractRouteUnits(text).build`, else unit 21's
  `resolveLease`. The function and constant are carried inline, never required: a kit imports no
  sibling kit (TOOL-dGroundRules-1 §4), and `tools/unattended/kit.toml`'s `requires` names no hooks
  kit. `#readCard` is not carried, since its `resolveCardBash` spawns each bash candidate and the
  engine, which AC16 and unit 21 AC5 refuse; `KICK-dKeptSession-56` S23 names it wrongly. Unit 21
  S9's hook sentence in `help/loop.md` and the `--mail` entry gain the card binding. Observed by AC7.
- **S10** — id 11, M8. Met by `KICK-dKeptSession-13` S6 and `KICK-dKeptSession-8` §8 F3 (b): unit
  8's arm reads the tree's card at `CARD_FILE_REL`, which
  `skills/session-kickoff/manifest-check.sh#write_pointers` re-renders by `write_card_file` at every
  crossing under both `card.pointers` values. Owed: the `pointers-at-transitions` plant, which reads
  only the session card, gains a row reading the tree card's `item —` line; unit 8's plants stub the
  policy reader, so no value of the key reaches them. Observed by AC8.
- **S11** — id 15, M9. `tools/runlog/selftest.py#test_extract_orient` gains `orient-refuse`,
  `budgets.enforce = "refuse"`, and `orient-pinned`, `orient-calls` in `budgets.pinned`, each under
  its AC5 case's `orient.budget = "owner-ceiling"` and `"orient-calls" = 30`, with a row past 30.
  Observed by AC9.
- **S12** — id 19, M10. Met by `KICK-dKeptSession-2`, which rewrote the preset step's reason; AC10's
  class grep finds no "not applied" text in the policy kit or under `help/`. Observed by AC10.
- **S13** — id 20, M11. `adopt-policy.sh --scaffold`'s write branch, where no policy file exists,
  runs `policy.py scaffold --preset <name>` with its stderr sent to `/dev/null` and turns any failure
  into `the scaffold could not be written` and exit 1; read 2026-11-23, `--preset lax` prints that
  line and exits 1, the scaffold alone exiting 2. It passes the scaffold's exit 2 and stderr through
  as the kept-file branch's `exit "$RC"` does (`KICK-dKeptSession-4` S3), a form `check-arms.py
  --report` counts no site for, keeping exit 1 for a write failure. Observed by AC11.
- **S14** — id 21, M12. Met by `KICK-dKeptSession-9`: `tools/policy/caps.toml`'s `orient-calls` row
  carries `research = 0`, `kit` and `installed`, and `tools/policy/check_policy.py#CAP_CASES` its
  plant. Observed by AC12.
- **S15** — id 46, M12. Met with S14: `tools/policy/budgets.py#resolve_caps` reads the census
  outside its `try`, so AC13 reads a second cap. Observed by AC13.
- **S16** — id 23, M13. Met by `KICK-dKeptSession-10`: `read_mail_interrupts` reads through
  `read_mail_rows`, which runs the driver under `loop_witness.resolve_bash`, the inline copy of
  `tools/lib/resolve_bash.py#resolve_bash` (`KICK-dKeptSession-36` S1), and raises `mail unknown` on
  a `None` bash. Observed by AC14.
- **S17** — id 24, M14. Met by `KICK-dKeptSession-7`: `derive_parent_reach` reads through
  `tools/loop/breakpoints.py#run_sourced`, the same resolver, and its S4 writes the listing as `git
  ls-tree`'s bytes by `Path.write_bytes`, so CRLF and LF clones compute one key. Observed by AC14
  and AC15.
- **S18** — id 27, M15. Met by `KICK-dKeptSession-21` S3 and §8 F5 (b), which rejects this item's
  second sidecar: the stamp's first line holds both resolved values, read with the stamp, and the
  hook calls no `readPolicy`. Observed by AC16.
- **S19** — id 33, M16. The build files one ask in `memory/builds/dDeclaredLoop/BACKLOG.md`, target
  TOOL-dDeclaredLoop-7 S4, widening unit 10 §8 F3's `TOOL-dDeclaredLoop-103`: `derive_interrupts`'
  default prints no mail line once `position.py --mail-interrupts` is the one mail reader. Unit 10
  AC1's "the same plant's plain engine call prints" is answered against it in this unit's ledger.
  Observed by AC17 and AC38.
- **S20** — id 35, M17. `read_dependents` is dropped. The dependents are the parent README's
  rendered `<!-- gen:build-edges -->` "Child builds" line (`tools/memory-tree/gen_build_index.py#render_edges`),
  the inversion of `parents:` that `tools/memory-tree/gen_build_index.py#plan` derives and refuses a
  dangling parent in. Observed by AC18.
  **Readers:** by name: READER NOT IN TREE — unit 7 S9 mints the function in
  `tools/loop/loop_transition.py`, unbuilt at this base · by value: NO VALUE READERS — its one
  caller, unit 7's notices, is re-pointed here.
- **S21** — id 36, M18. Met by `KICK-dKeptSession-12` S5:
  `skills/session-kickoff/manifest-check.sh#print_replay` opens with `derive_map_block`'s lines and
  ends with `now —`, as its comment states, and the `replay-order` plant replays it. Observed by AC19.
- **S22** — id 40, M19. The `records —` line `KICK-dKeptSession-13` S5 prints names only the base
  kinds: its one source, `tools/memory-tree/gen_build_index.py#cmd_latest_records`, keeps
  `RECORD_KIND_TOKENS` less `TYPED_RECORD_KINDS` (`tools/memory-tree/tree_lib.py`), so typed kinds
  never lengthen it; today it prints `red-fix` and `widen` rows. Its docstring, the module's usage
  line, the section comment above `run_item_boundary` and `help/orientation-card.md`'s `records —`
  bullet read "each base kind". Unit 13's `pointers-cap` plant gains one record of every typed kind.
  Observed by AC20.
- **S23** — id 48, M20. The driver's refusal census, read once after every driver unit by `python
  tools/memory-tree/check-arms.py --report`. A census past its `REFUSAL_CEILINGS` row takes the
  retirement review the memory-tree README's "The ceiling" names, the ceiling rising only to the
  census left, under a dated decision id in `memory/DECISIONS.md`, with both `.memory-tree.conf`
  rows. Observed by AC21.
- **S24** — id 49, M21. One kickoff re-stamp per write set: `memory/guides/SESSION-KICKOFF.md`'s
  `last-audit` is re-stamped after this unit's last edit to a `watch:` path, with its delta line, as
  TOOL-dGroundRules-86 did; `KICK-dKeptSession-56` and later units re-stamp for their own edits.
  Observed by AC22.
- **S25** — id 50, M22. The claim is met by `KICK-dKeptSession-21` S5, which adds `PostToolUse
  tools/unattended/mail-notice.js` to the `harness-hooks` list of `memory/map/features/unattended.md`.
  This unit regenerates the map once, by `map_lib.regen_cmd()`'s `python
  tools/codebase-map/gen_map.py --write`, moving `memory/map/generated/symbols.json`. Observed by AC23.
- **S26** — id 51, M23. Met by `KICK-dKeptSession-12` S1 and §8 F4: `tools/govkit/registry.toml`
  exempts `card-compaction.fixture.sh`, unshipped by PLAY-dOrderedCharter-77 S7, and an adopter's
  engine reads its absence as `red: no fixture installed`
  (`skills/session-kickoff/manifest-check.sh#read_card_fixture_verdict`). No `[[files]]` row is
  added. Observed by AC24.
- **S27** — id 52, M24. `tools/unattended/kit.toml`'s `requires` gains `playbook-render`, the kit
  whose `read_fleet` the landed `tools/unattended/unattended.sh#check_fleet_tag` reads through for
  `check_mail_recipient` (`KICK-dKeptSession-28` S3). Observed by AC24.
- **S28** — id 56, M25. `--mail post` refuses `--kind ack` and `--kind answer` with exit 2, naming
  `--mail ack` and `--mail answer` (`KICK-dKeptSession-25` S2), in the dispatch arm's `post` branch
  through `_rl_rc=2`; `write_mail_post` keeps both kinds, since
  `tools/unattended/unattended.sh#write_mail_ack` posts through it. The `--mail` entry of
  `tools/unattended/VERBS.template.md`, its copy `memory/guides/UNATTENDED-VERBS.md` copied whole, and
  `help/loop.md`'s `--mail post` paragraph state the refusal; no usage row, so no anchor, moves.
  Observed by AC25.
- **S29** — id 59, M26. Met by `KICK-dKeptSession-5` S9: a non-zero read with no row raises
  `ValueError`, which `record` prints after `loop: unanswered`, exit 2. This unit observes it with one
  plant, `mail-read-crash`, whose planted reader exits 3 with no output. Observed by AC26.
- **S30** — id 60, M27. Met by `KICK-dKeptSession-5`: `tools/unattended/unattended.sh#write_mail_post`
  returns 2 naming a failed or timed-out fetch before any commit; no arm reads it, so AC27's is
  added. Observed by AC27.
- **S31** — id 61, M28. The hook's detached spawn sets `windowsHide: true`, as those of
  `tools/hooks/format-guard.js`, `tools/unattended/stop-guard.js` and `checkItemBoundary`, which unit
  21 S6 copies, do; this unit adds it where the landed spawn lacks it. Observed by AC28.
- **S32** — id 62, M29. `validate` refuses a `[presets.<shipped name>]` table, naming its line and
  the name, in `tools/policy/presets.py#check_repo_presets`. Its docstring, the module docstring's
  "THE REPOSITORY SIDE" paragraph and the closing sentence of `help/policy.md`'s "Declare your own
  preset" bullet gain the refusal. Observed by AC29.
- **S33** — id 63, M30. `print_progress`, `KICK-dKeptSession-11` S5's driver emitter, runs bounded by
  a new `PROGRESS_BOUND=10`: it calls `RB_BOUND=$PROGRESS_BOUND run_loop_verb …`, and
  `tools/unattended/unattended.sh#run_loop_verb`, the one runner of loop kit verbs, runs its command
  through `run_bounded` where `RB_BOUND` is set and as today where not, its "ONE RUNNER" comment
  saying so. `KICK-dKeptSession-56` S24's `run_bounded print_progress` cannot run: `init_bounded`
  runs its argv in a child `bash -c`, where no driver function exists. A fired bound prints `NOTE —
  progress not emitted: <why>` in place of unit 11 S5's lines and never moves the verb's exit or
  lines. Observed by AC30.
- **S34** — id 12, L1. Met by `KICK-dKeptSession-18`: its AC5 observes the route by path on
  `help/loop.md`, and its AC3 prints the filed ask, `TOOL-dIndexedDesign-19`. This unit observes the
  page. Observed by AC31.
- **S35** — id 13, L2. Unit 14 AC7 is withdrawn; its S6 cites `KICK-dKeptSession-13` AC5, which
  observes the `agent_type` skip. NOT OBSERVED here: the criterion moves to the unit owning the
  check, and this unit's ledger answers it by quoting unit 14 §8 F4's "AC7 withdrawn and S6 citing
  KICK-dKeptSession-13 AC5".
- **S36** — id 14, L3. Met by `KICK-dKeptSession-16`: its spec calls `unpurposed-namespaces.txt` the
  fourth list, and the policy kit's `README.md`, as `KICK-dKeptSession-69` rewrote it, names each
  list by file and no ordinal. Observed by AC32.
- **S37** — id 44, L3. Met by the same unit: its §10 already says the fourth, so no text is
  superseded. Observed by AC32.
- **S38** — id 18, L4. Met by `KICK-dKeptSession-1`: the landed `never` list's comment in
  `tools/policy/presets.toml` cites no line range of the design record, so none can stop before the
  list's end. Observed by AC33.
- **S39** — id 41, L5. Met by `KICK-dKeptSession-14`: its fixture is the `context-fill` scenario of
  `tools/runlog/fixtures/transcripts.json`, and no other fill fixture stands in that folder.
  Observed by AC34.
- **S40** — id 42, L6. Unit 9's quartiles already call `tools/runlog/runlog.py#_derive_quartiles`.
  The four-field token sum becomes one function, `derive_spent_tokens` in `tools/runlog/extract.py`,
  beside `derive_context_tokens`, called by `tools/runlog/runlog.py#print_ready`, whose
  `spent_tokens` row spells the sum today, and by `tools/runlog/extract.py#measure_orient_tree`,
  which spells it again. Observed by AC35.
- **S41** — id 43, L7. Met by `KICK-dKeptSession-1` and `KICK-dKeptSession-20`: the one pair rule,
  `tools/policy/presets.py#check_pairs`, runs in `check_presets` and in the `pairs` verb
  (`tools/policy/presets.py#run_pairs`) that `tools/loop/scenario.py` runs as a subprocess;
  `check_repo_presets` judges no pair (unit 1 §8 F10). Observed by AC36.
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
- **consumes-from** `KICK-dKeptSession-5` — `--mail post`, its fetch refusal and the transition guard, S28 to S30
- **consumes-from** `KICK-dKeptSession-7` — `derive_parent_reach`, the listing and `read_dependents`, S17 and S20
- **consumes-from** `KICK-dKeptSession-8` — §8 F3 (b)'s read of the tree's card file, which S10 observes
- **consumes-from** `KICK-dKeptSession-9` — the orient report, its cap row and its sums, S11, S14, S15 and S40
- **consumes-from** `KICK-dKeptSession-10` — `read_mail_interrupts` and its `--local`, S3, S16 and S19
- **consumes-from** `KICK-dKeptSession-11` — `print_progress`, S33
- **consumes-from** `KICK-dKeptSession-12` — `print_replay`'s order and the fixture's shipping, S21 and S26
- **consumes-from** `KICK-dKeptSession-13` — the boundary verb, its pointer rewrite, the `records —` line and the two `pointers-` plants, S8, S10 and S22
- **consumes-from** `KICK-dKeptSession-14` — AC7 and the fill fixture, S35 and S39
- **consumes-from** `KICK-dKeptSession-16` — the list's ordinal, S36 and S37
- **consumes-from** `KICK-dKeptSession-18` — AC3 and AC5, S34
- **consumes-from** `KICK-dKeptSession-20` — the scenario check's `presets.py pairs` call, which S41 observes
- **consumes-from** `KICK-dKeptSession-21` — `mail-notice.js`, its stamp, binding and spawn, and `--local`, S3, S6 to S9, S18, S25 and S31
- **consumes-from** `KICK-dKeptSession-25` — §7's covers list, S2, and `--mail answer`, which S28 names
- **consumes-from** `KICK-dKeptSession-28` — `check_mail_recipient`'s cross-kit call, S27
- **consumes-from** `KICK-dKeptSession-36` — the loop kit's `resolve_bash`, which S16 and S17 observe
- **consumes-from** `KICK-dKeptSession-41` — the standing rows' summaries and the drained list, which S4 and S5 observe
- **hands-off** `KICK-dKeptSession-56` — S7, S16, S17, S20 and S33, §4's citations and §7's legs, the batch's S3, S19, S20, S23, S24, S34, S43, S26 and S27 (ids 5, 25, 27, 31, 32, 54, 42, 35, 36)

## 4. Design

### Evidence

Each item's evidence is the audit's appendix row for its id, re-read on 2026-10-26 and re-checked
at `ff2654fc` on 2026-11-23, units 7, 8, 11, 13, 18, 21, 25 and 41 read as landed. The driver's
`.memory-tree.conf#REFUSAL_CEILINGS` and `.memory-tree.conf#ARMS_FLOORS` rows are read by key, and
`check-arms.py --report` prints it at 347/347 (PINNED 2026-11-23). `SESSION-KICKOFF.md`'s `watch:`
line names `manifest-check.sh` and `.memory-tree.conf`; `tools/unattended/kit.toml`'s `requires`
names five kits (PINNED 2026-11-23), not `playbook-render`; `REMOTE_BOUND`, 60 seconds, is too long
for a lander's note. Items met by landed or earlier units name the unit and keep their observation.

The ceiling holds: S28 refuses through `_rl_rc=2`, S33's bound returns through `run_loop_verb`'s
code, and no item adds a `fail`, `exit 1` or `status=1` site.

### Inventory

| Minted | Kind | Home |
|---|---|---|
| `PROGRESS_BOUND` | constant | `unattended.sh` |
| `derive_spent_tokens` | function | `tools/runlog/extract.py` |
| `orient-refuse`, `orient-pinned` | checks of `test_extract_orient` | `tools/runlog/selftest.py` |
| `mail-read-crash` | plant | `tools/loop/loop_transition.py` |

### Migration

The decision row S23 may write, and the re-stamp S24 writes, are additive records. No stored state
changes shape.

### Files touched (estimate)

- `tools/policy/check_policy.py`, `tools/policy/adopt-policy.sh`, `tools/policy/presets.py`,
  `help/policy.md`: S13, S32 and the `presets-repo` case
- `tools/loop/loop_transition.py`: S20's `read_dependents` and unit 7's notices re-pointed, and S29's
  `mail-read-crash` plant, a branch of `run_transition_fixture`
- `tools/run-gates/selftest-budgets.txt`: the `loop transition record` row's one `plants=` token
  raised in place to `len(PLANTS)` (DERIVED), its note re-read; `runlog selftest` and `unattended
  driver selftest shard 8/8` re-priced by their arms' direct readings
- `tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`,
  `tools/unattended/mail-notice.js`, `tools/unattended/kit.toml`,
  `tools/unattended/VERBS.template.md`, `memory/guides/UNATTENDED-VERBS.md`, `help/loop.md`: S9, S27,
  S28, S31, S33
- `tools/memory-tree/gen_build_index.py`, `skills/session-kickoff/manifest-check.sh`,
  `skills/session-kickoff/card-store.fixture.sh`, `help/orientation-card.md`: S10, S22
- `tools/runlog/runlog.py`, `tools/runlog/extract.py`, `tools/runlog/selftest.py`: S11, S40
- `.memory-tree.conf`, `memory/DECISIONS.md`, `memory/guides/SESSION-KICKOFF.md`: S23, S24
- `memory/map/features/unattended.md`, `memory/map/generated/symbols.json` and the rest of
  `memory/map/generated/`: S25's render
- `memory/builds/dDeclaredLoop/BACKLOG.md`: S19's ask row
- `memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-44-1-acceptance-ledger.md`:
  every answer §1 and the items name, beside the criteria observed

The texts that stay: `help/loop.md`'s sentence that `--mail post` refuses any other kind stays true;
the `presets-repo` docstring, "admitted and refused", holds; `scratch-guard.js` is only read.

### Alternatives rejected

- **Two batches.** S10 and S28 each cross kits, and S23 to S25 read every other item's output, so no
  two write sets are disjoint by M6's clauses.
- **Placing the batch beside each unit it lands on.** A batch is one unit with one order; past the
  last unit is the one place every item's code exists.

## 5. Production-readiness checklist

- security — S28 closes a release of another build's question; S29 and S30 fail closed; S31 hides a
  console window; S32 refuses a shadowed name.
- perf / scale — S9 binds with one file read and no spawn; S33 bounds the lander's progress line.
- error / empty / loading states — S29, S30 and S33 name every non-zero exit they meet.
- observability — S1's line names what the arm does not grade; S33's `NOTE` names a progress line not
  emitted.
- risks — S23 may need a raise; the decision row records the review that admits it.
- testing — the criteria of §6 and the arms of §7.
- migration — §4.
- user docs — `help/policy.md`, `help/orientation-card.md` and `help/loop.md`, by S9, S22, S28 and
  S32.

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
- **AC6** — `KICK-dKeptSession-13` AC2 and AC5 hold: `at` moves before the verb's steps, and
  `checkItemBoundary` starts one detached call, none at an unchanged HEAD. Red when: the hook waits
  on the verb, or every call re-runs it.
- **AC7** — When `node mail-notice.js` reads a payload for an attended session that the tree card's
  `card-owner —` line names, with no lease and one unread id, it prints `additionalContext` naming
  the id, and `grep -c 'spawnSync\|execFileSync' mail-notice.js` prints `0`.
  Red when: a session routed by its card hears nothing, or its binding spawns a process.
- **AC8** — When `bash card-store.fixture.sh --plant pointers-at-transitions` runs, its row reading
  the tree card at `CARD_FILE_REL` after the crossing holds `item — <K1>`. Red when: under
  `at-transitions` the tree card keeps the stale item unit 8's arm judges against.
- **AC9** — When `python runlog.py extract --orient` runs the `orient-refuse` and `orient-pinned`
  cases of `test_extract_orient`, each prints `orient REFUSED` and exits 1. Red when: a build ignoring
  `budgets.enforce` or `budgets.pinned` passes.
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
- **AC16** — When one `mail-notice.js` call for a card-routed session runs over a fresh stamp with
  logging stubs named `git` and `bash` first on PATH, neither stub logs a call. Red when: the hook
  reaches `readPolicy`'s spawns or `resolveCardBash`'s probes.
- **AC17** — When `python gen_build_index.py --asks --build dDeclaredLoop` runs, it lists the ask
  naming `--mail-interrupts` and TOOL-dDeclaredLoop-7 S4. Red when: the slot is removed with no
  parent text, or left armed by nobody.
- **AC18** — When `grep -rn "def read_dependents" tools/loop` runs, it prints nothing, and
  `KICK-dKeptSession-35`'s `notices-two-dependents` plant still prints its two notices. Red when: a
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
- **AC24** — When `grep -n "playbook-render" tools/unattended/kit.toml` runs, it prints the `requires`
  row; `grep -n "card-compaction.fixture.sh" tools/govkit/registry.toml` prints its `[[exempt]]` row;
  and `grep -c "no fixture installed" skills/session-kickoff/manifest-check.sh` prints `1`. Red when:
  a required kit is absent at install, or an absent fixture reads as anything but a named red.
- **AC25** — When `bash unattended.sh --mail post fx --to build:dB --kind ack --answers <id> body`
  runs, it exits 2 naming `--mail ack`, and the row stays `open`, while `--mail ack fx <id>` posts.
  Red when: a third build's reply releases the row, or the refusal stops `--mail ack`.
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
- **AC30** — When the progress verb is stubbed to sleep 30 s (PINNED), `bash unattended.sh --landed <slug>`
  exits 0 within 12 s (PINNED) printing `progress not emitted`. Red when: the lander waits on it.
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
- **AC35** — When `grep -c 'r\["in"\] + r\["out"\]' tools/runlog/runlog.py` runs, it prints `0`,
  `grep -c '\["in"\] + ' tools/runlog/extract.py` prints `1`, and `grep -n "def derive_spent_tokens"
  tools/runlog/extract.py` prints one line. Red when: the sum is written twice.
- **AC36** — When `grep -c "def check_pairs" presets.py` prints `1` in the policy kit,
  `python scenario.py --fixture --plant slot-refused` in the loop kit prints its `held` line, its
  `pair` row a slot's broken pair refused by `presets.py pairs` naming the pair. Red when: a second
  evaluation of the rule exists.
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

New arm: tools/unattended/unattended.test.sh · covers AC25 AC27 AC30 · a third build's ack and a sleeping progress verb against the base, an unreachable origin by a scratch copy reading a failed fetch as 0 · `FLOOR_ASSERTIONS` 4120 and `FLOOR_SHARD_8` 1337 (DERIVED: their last assignments) rise by the arms' count
New arm: tools/loop/loop_transition.py · covers AC26 · the `mail-read-crash` plant, staged by a scratch guard reading a crashed read as zero rows · the `plants=<n>` token rises by one
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC8 AC20 · the two `pointers-` plants' new rows, staged by scratch copies skipping `write_card_file` or keeping typed kinds · none, one ok row per plant
New arm: tools/policy/check_policy.py · covers AC29 · a shadowed preset in `presets-repo`, against the base · none
New arm: tools/runlog/selftest.py · covers AC9 · the two orient cases, staged by a copy reading `budgets.enforce` as `warn` · `ASSERTION_FLOOR` 1630 (DERIVED: its last assignment) rises by the counted checks

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
  At rev-5 the question is moot: unit 13 starts the verb detached, so S8 is its observation.
- **F3 — Where are the answers to the sibling texts and criteria the items name recorded?** Every
  unit whose text an item answers is CLOSED when this unit builds, and its ledger is outside this
  unit's write set. (a) Each named unit's acceptance ledger, a record of a closed unit written by a
  later one; (b) this unit's own acceptance ledger, quoting each sibling text it answers.
  Recommendation (b). RESOLVED (agent, 2026-11-21, delegated): (b), rung 3; a CLOSED unit's records
  are never written by a later unit, as KICK-dKeptSession-49 rev-6 ruled. Rejected: (a). The main
  loop's ruling, in `2026-11-21-prompt-KICK-dKeptSession-30-ledger-class-brief`.
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
- rev-6 · 2026-11-23 · S1 to S4 · S6 to S10 · S12 to S31 ·
  S33 · S35 · S36 · S39 to S41 · §3 · §4 · §5 · AC6 · AC7 · AC8 · AC9 · AC16 · AC18 · AC24 · AC25 · AC30 ·
  AC35 · AC36 · §1 · §7 · §8 F2 F3 · §10 · re-grounded at `ff2654fc` under
  `2026-11-22-prompt-KICK-dKeptSession-44-reground-brief`: items met by units 5, 7, 9, 10, 14 and 21
  reduced; S9 binds by `checkItemBoundary`'s card read, `readCard` spawning; S10's row moves to a
  kickoff plant; S22 filters in `cmd_latest_records`; S28 refuses in the dispatch arm; S33 bounds in
  `run_loop_verb`; texts made false named; the ceiling, floors and inventory corrected.

## 10. Reuse audit

Every item extends the seam its repaired unit names, and the cross-cutting ones extend existing
mechanisms: `fail` and the retirement review for S23 (`tools/memory-tree/README.md` "The ceiling"),
the re-stamp of TOOL-dGroundRules-86 for S24, `map_lib.regen_cmd()` for S25
(`tools/codebase-map/map_lib.py#regen_cmd`), `checkItemBoundary`'s card read and `extractRouteUnits`
for S9, carried inline as `tools/unattended/gate-guard.js#buildHeredocView` carries its copy of a
`scratch-guard.js` function, `run_loop_verb` and `run_bounded` for S33, `_derive_quartiles` for S40,
and the index generator's inversion of `parents:` for S20. `python
tools/codebase-map/reuse_lookup.py "resolve the bash that shares this filesystem by running each
candidate"` ranked the `resolve_bash` copies, which S16 and S17 observe in `loop_witness.py`. At rev-6
`reuse_lookup.py` over S9's and S33's seams ranked only name-token seams, so both were read in code.
No item mints a mechanism where one of these fits.

Recall terms used: `python tools/memory-recall/query.py "how are a spec audit's confirmed findings
promoted into repair units placed after the unit they repair" --terms "spec-audit promoted repair unit
order hands-off consumes-from minors batch BLOCKER HIGH rescope add"`
