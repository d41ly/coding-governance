# KICK-dKeptSession-65 — the round-5 minors batch's audit's 26 minor findings, closed after the batch they land on is built

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 36 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 |
| [2026-10-26-build-KICK-dKeptSession-65-deviation-651.md](../build/2026-10-26-build-KICK-dKeptSession-65-deviation-651.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-65-promoted-fix-return.md](../build/2026-10-26-build-KICK-dKeptSession-65-promoted-fix-return.md) | research | — |
| [2026-10-26-prompt-KICK-dKeptSession-65-promoted-fix-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-65-promoted-fix-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of `KICK-dKeptSession-64`
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-64-spec-audit.md`)
confirmed 13 findings at MEDIUM and 13 at LOW, with no blocker and no high. BUILD-METHOD M4 promotes
them into one batch, and this is it. Each finding is its own §2 item, named by report id beside the
report item it shares:

- MEDIUM: ids 1, 11 and 21 (M1), 10 and 24 (M2), 9 (M3), 15 (M4), 2 (M5), 3 (M6), 4 (M7), 16 (M8),
  20 (M9), 23 (M10);
- LOW: ids 6 and 17 (L1), 5 (L2), 12 (L3), 7 (L4), 8 (L5), 13 (L6), 14 (L7), 18 (L8), 19 (L9),
  22 (L10), 25 (L11), 26 (L12).

Ids sharing a report item describe one defect, so each takes its own item and one edit closes the
group. Every finding lands on unit 64, so this unit builds one step after it (order 36) and amends
what that unit built. Where an item supersedes a text of unit 64, of unit 63 or of a sibling, it
does so by name, and that unit's acceptance ledger answers the superseded text by this unit's id
(AC13).

## 2. Scope (IN)

- **S1** — id 1, M1. The "already acked" predicate of `KICK-dKeptSession-64` S1 reads as: a cached
  message of kind `ack` sent by `<slug>` names the id in its `answers` column. It is read from the
  rows of `read_mailbox <slug> cache sent` (`KICK-dKeptSession-63` S11), whatever their `state`
  column says. An id that is answered and acked is therefore skipped like any acked id. Observed by
  AC1.
- **S2** — id 11, M1. `KICK-dKeptSession-5` S7's state precedence stands unchanged: a row has one
  state, and `answered` is tested before `acked`. Unit 64's §4 alternative calling the `acked` state
  "the one predicate that says an ack exists" reads as false, because a row both answered and acked
  reads `answered`. The skip of S1 never reads the `state` column. Observed by AC1.
- **S3** — id 21, M1. Unit 64 S3's promise, that an id already acked never refuses a batch, holds
  for an answered-and-acked id too: `--mail ack <slug> <a>` and `--mail ack <slug> <a> <c>`, with
  `<a>` answered by `--mail answer` and then acked, each exit 0 and print `mail — already acked <a>`,
  and `<a>` never reaches `check_mail_duplicate`. Observed by AC1.
- **S4** — id 10, M2. Unit 64 S10's scrub reads as
  `for _k in ("GOV_REMOTE", "GOV_DEFAULT_BRANCH"): os.environ.pop(_k, None)` at module level in
  `tools/runlog/selftest.py`, beside the `GIT_*` loop (`:355-356`). It tolerates an unset variable,
  which is the ordinary case, where a bare `del os.environ[...]` raises `KeyError` at import.
  Observed by AC4.
- **S5** — id 24, M2. Unit 64 §7's `tools/runlog/selftest.py` arm reads as two processes: one
  started with both `GOV_REMOTE` and `GOV_DEFAULT_BRANCH` planted, in which no case sees either, and
  one started with neither, which imports cleanly. Observed by AC4.
- **S6** — id 9, M3. Unit 64 AC8's fixture recipe reads as the spec-tokens self-test's guards
  fixture: the `scratch` builder (`tools/check-spec-tokens.test.sh:199-207`), which writes the
  waiver file `memory/project/spec-token-waivers.txt`, and the guards arm's manifest and conf
  (`:591-592`). The conf sets `SPEC_GUARD_LEGS_CUTOFF` on or before 2026-10-26, so the guards join is
  armed (`tools/check-spec-tokens.py:1468`) and a missing leg prints a `guards` hit rather than a
  NEAR line (`:1572-1579`). Observed by AC5.
- **S7** — id 15, M4. Unit 64 S7's "the lines of units 58 to 61" reads as unit 64 S6's derived
  population, never lines fixed in advance. Units 64 and 65 are members of it, since their Files
  touched names `tools/workflows/unattended-build.template.js`, a non-broad guard of
  `policy fixtures` at `origin/main`. Each owes a `NOT RUN — policy fixtures not declared` line until
  the reconcile. Unit 64 AC8's fixture declares `{prefix}/memory-tree/gen_build_index.py` as a
  second guard of `policy fixtures` and holds a copy of unit 64, so the probe shows a file-level
  hit. Observed by AC5.
- **S8** — id 2, M5. `KICK-dKeptSession-63` AC14's clause "`build_arm_env` under
  `GOV_REMOTE=planted` returns an environment without `GOV_REMOTE`" and 63 §7's
  `tools/runlog/selftest.py` arm line are superseded by name, as unit 64 S10's subject. The clause
  reads as "a process started under `GOV_REMOTE=planted` reaches no case with `GOV_REMOTE` set".
  Unit 64 AC17's list of superseded 63 texts gains both. Observed by AC13.
- **S9** — id 3, M6. Unit 64 AC11's rise reads as derived from its diff range: the effective
  `FLOOR_ASSERTIONS` pin rises by the counted assertions of every case the diff adds, less those it
  takes out. That covers 63's whole `tools/unattended/unattended.test.sh` arm, unit 64's S1, S3 and
  S5 cases and this unit's cases. Every `FLOOR_SHARD_<k>` line whose region holds a changed case
  moves by that region's share, and the shares sum to the effective rise. Observed by AC7.
- **S10** — id 4, M7. Unit 64 AC9's loop half gets its subject: AC8's fixture also holds copies of
  units 61 and 64, whose Files touched name the loop kit's paths, with tracked stubs at
  `tools/loop/loop_transition.py` and `tools/loop/selftest.py` inside the fixture repository.
  Observed by AC6.
- **S11** — id 16, M8. Unit 64 S5's by-name readers gain `tools/loop/loop_transition.py`, whose
  `write_consumed_acks` and `derive_mail_chain` (`KICK-dKeptSession-61` S2) consumed the parent's
  `--mail chain` rows. Where a `--mail chain` call survives there, this unit's pass re-points it to
  `--mail read <parent> --cached --sent`, as `KICK-dKeptSession-63` S6 states. Unit 64 AC5's
  hand-listed grep reads as one `git grep` over the tracked tree. Observed by AC8.
- **S12** — id 20, M9. The batch fetches before it reads. Its first row is one
  `read_mailbox <slug> strict` (`KICK-dKeptSession-5` S6): one bounded fetch of every mail ref, then
  `add_feed_sightings`, then the rows addressed to `<slug>`, which the addressed-to check reads. A
  failed fetch exits 2 with nothing built, per §8 F1. The skip of S1 and `check_mail_duplicate`
  (`KICK-dKeptSession-22` S3, "its caller fetches first") then read the cache that fetch filled.
  Observed by AC2.
- **S13** — id 23, M10. The ask row unit 64 S13 rewrites reads: for a create or an update,
  `TOOL-dPlacedRequest-13 S4`'s walk takes the place of `TOOL-dPlacedRequest-13 S3`'s
  `add_feed_event`, the walk appending the landed tip as its newest event; a deletion keeps the single
  `add_feed_event`. The row's accept clause adds that a three-message chained landing appends exactly
  three events, each key once, and that `--feed check` then passes, seen by a chained
  `write_gov_ref` in a scratch repository. §8 F3 records the choice. Observed by AC9.
- **S14** — id 6, L1. Unit 64 AC10 reads as accepting either no-raise form at module level: an
  `os.environ.pop(<name>, None)` call, or a `del` guarded by `<name> in os.environ`. Observed by AC4.
- **S15** — id 17, L1. Unit 64 AC10 reads as also executing the scrub: the module-level statements
  that name either variable, run in a child with neither set, raise nothing. A bare `del` fails
  that run. Observed by AC4.
- **S16** — id 5, L2. Unit 64 §4 Evidence's sentence on what the probe of AC8 relies on names
  `SPEC_GUARD_LEGS_CUTOFF` beside `derive_legs_path`, and AC8 carries a `fixture:` line naming that
  key as the TEMPLATE-SPEC §6 rule asks of a criterion observing a gate arm. Observed by AC5.
- **S17** — id 12, L3. Unit 64 §4 Evidence's `policy fixtures` sentence reads as: at `origin/main`
  (`c53e4eb3`) the leg carries 65 guards, and its non-broad paths include `{prefix}/policy/`,
  `{prefix}/workflows/unattended-build.template.js` and `{prefix}/memory-tree/gen_build_index.py`,
  which unit 64's Files touched trips. Unit 64 §7's reconcile note reads: the reconcile adds
  `policy fixtures` to unit 64's leg line as well as `loop selftest`. Observed by AC13.
- **S18** — id 7, L4. Every reference to another spec's item in the ask row and in unit 64 S18 and
  AC18 is spelled with its id in full, `TOOL-dPlacedRequest-13 S3` and `TOOL-dPlacedRequest-13 S4`,
  never a bare `S3` or `S4`, which in unit 64 name its own items. Observed by AC9.
- **S19** — id 8, L5. Unit 64 S17's citations read as the `def` lines, with the call and glob lines
  said as such: `scan_preflights` at `tools/runlog/extract.py:991` calls `_check_inside` at `:1004`;
  `measure_tree` at `:1131` and `measure_ready_tree` at `:1204` glob without it, at `:1135` and
  `:1209`. 63's ledger answer to its `_check_inside` sentence carries these. Observed by AC13.
- **S20** — id 13, L6. Unit 64 §3's left-shift bullet names an owner for each gate it defers. This
  unit's pass files one ask row per gate of §4's left-shift table in
  `memory/builds/dKeptSession/BACKLOG.md`, each with a `SEV ·` row, and unit 64's ledger answers the
  bullet with the minted ids. Observed by AC10.
- **S21** — id 14, L7. Unit 64 S16's reword of the prompt string at line 2078 is made in
  `tools/workflows/unattended-build.template.js` alone, then rendered into
  `tools/workflows/unattended-build.js` by the kit's `[[regenerate]]` argv
  (`tools/workflows/kit.toml:115-116`), never typed into the render. Unit 64's leg line gains
  `review-protocol parity (kit vs dogfood)`. Observed by AC11.
- **S22** — id 18, L8. The write set of the dPlacedRequest ask row is
  `memory/builds/dPlacedRequest/BACKLOG.md` (the row and, when newly filed, its `SEV ·` row),
  `memory/backlog/TOOL.md` and `memory/builds/dPlacedRequest/README.md`, both regenerated by
  `python tools/memory-tree/gen_build_index.py --write`. A newly filed row takes the next free
  `TOOL-dPlacedRequest-<n>` by `memory/HYGIENE.md`'s id rule, the maximum in that family plus one,
  read at the pass. Observed by AC14.
- **S23** — id 19, L9. The rev bumps of unit 64 S9 and of S26 here move the rev column of
  `memory/builds/dKeptSession/README.md`, which `gen_build_index.py --write` re-renders in the same
  commit, with `memory/backlog/KICK.md` for S20's rows. Observed by AC14.
- **S24** — id 22, L10. The grammar is stated once, `--mail ack <slug> [<id> ...]`, and unit 64 §4's
  sketch reads with it and a row "no ids given -> exit 0, nothing written". The `--mail ack` line of
  `tools/unattended/VERBS.template.md` and its render spell that grammar. Observed by AC3.
- **S25** — id 25, L11. Unit 64 S14's `blk` extractor (`tools/lib/resolve-python.test.sh:213`)
  reads both markers through `MARKER_LEAD`, the opener `>>> ` and the closer `<<< `. Observed by AC12.
- **S26** — id 26, L12. Unit 64 S9 compares the two manifests both ways. A name the base declares
  and HEAD's did not is added where the guards join names it, as unit 64 S9 states. A name HEAD's
  declares and the base does not is taken off every backtick leg line of a non-terminal spec of this
  build that names it. A renamed leg is the pair of the two: its old name comes off, and the guards
  join puts its new name on. Each edit is a rev bump with its §9 line. Observed by AC6.

## 3. Non-goals (OUT)

- Rewording unit 64 or a sibling spec: each superseded text is named here and answered in its
  unit's ledger.
- Building any gate of §4's left-shift table: each is an ask S20 files, owned by that row.
- A `soft` or `strict` argument on `--mail ack`: §8 F1.
- A gate leg that runs `tools/unattended/unattended.test.sh`: the leg is withheld by the ruling
  `tools/unattended/kit.toml:47-50` records.
- Renumbering any order.

### Edges

- **consumes-from** `KICK-dKeptSession-64` — the batched `--mail ack`'s skip and order, S5's retirement, S7's and S9's reconcile rules, S10's scrub, S13's and S18's ask row, S14's marker lead, S16's reword, S17's citations, §3's left-shift bullet, §4's Evidence and sketch and AC5, AC8 to AC11, AC17 and AC18, which every item here amends (all 26 ids)
- **consumes-from** `KICK-dKeptSession-63` — AC14's `build_arm_env` clause, §7's runlog arm line and the `unattended.test.sh` arm whose count S9 derives (ids 2, 3)
- **consumes-from** `KICK-dKeptSession-5` — S6's strict fetch and its rows, S7's state precedence and S8's addressed-to check, which S1, S2 and S12 read (ids 1, 11, 21, 20)
- **consumes-from** `KICK-dKeptSession-22` — S3's cache-only `check_mail_duplicate`, whose caller S12 makes fetch first (id 20)
- **consumes-from** `KICK-dKeptSession-61` — S2's `write_consumed_acks` and `derive_mail_chain` in the loop kit's transition, which S11 re-points, and its spec, which S10's fixture copies (ids 16, 4)
- **consumes-from** external — TOOL-dPlacedRequest-13 S2's keyed `add_feed_event`, S3's success exit and S4's `add_feed_sightings`, which the amended ask row names (S13, S18)
- **hands-off** external — the amended ask row in `memory/builds/dPlacedRequest/BACKLOG.md`, for dPlacedRequest to build (S13, S18, S22)

## 4. Design

### Evidence

Each item's evidence is the audit's appendix row for its id, re-read for this spec on 2026-10-26.
Re-verified at this base: `tools/runlog/selftest.py:355-356` deletes only the `GIT_*` keys it finds,
and `build_arm_env` (`:1515-1520`) copies `os.environ`. `tools/check-spec-tokens.test.sh:199-207`
is the `scratch` builder and writes the waiver file at `:207`; `:316` writes `SPEC_LEGLINE_CUTOFF`;
`:591` writes the guards arm's manifest and `:592` sets `SPEC_GUARD_LEGS_CUTOFF="2026-09-01"`.
`tools/check-spec-tokens.py` arms the guards join at `:1468`, sends an unarmed missing leg to NEAR
at `:1576-1579`, excludes a guard carried by more than `BROAD_LEG_FLOOR = 5` legs (`:331`), and
prints a `leg` hit for a §7 name the manifest lacks (`:1502`). At `origin/main` (`c53e4eb3`)
`policy fixtures` carries 65 guards, among them `{prefix}/policy/`, `{prefix}/lib/`,
`{prefix}/workflows/unattended-build.template.js` and `{prefix}/memory-tree/gen_build_index.py`;
neither manifest declares `loop selftest`, and `tools/loop/` does not exist at this base.
`tools/workflows/kit.toml:62-65` declares `unattended-build.js` rendered from its template and
`:115-116` the `[[regenerate]]` argv; both copies carry "a parallel group" at line 2078.
`tools/runlog/extract.py` defines `_check_inside` at `:176`, `scan_preflights` at `:991`,
`measure_tree` at `:1131` and `measure_ready_tree` at `:1204`, with the `root.glob` lines at `:1135`
and `:1209`. `tools/lib/resolve-python.test.sh:213` holds `blk` with the opener `^# >>> ` and the
closer `^# <<< `. `tools/unattended/unattended.test.sh` holds the SHADOWED pin at `:17665`, the
effective `FLOOR_ASSERTIONS=2776` at `:17940` and `FLOOR_SHARD_1` at `:18077`.
`memory/builds/dKeptSession/BACKLOG.md` holds only `KICK-dKeptSession-29` and its `SEV ·` row, and
`memory/builds/dPlacedRequest/BACKLOG.md` holds no chained-landing row yet.

### The ack batch, in order

This sketch takes the place of unit 64 §4's.

```
--mail ack <slug> [<id> ...]                      no ids given -> exit 0, nothing written
  read_mailbox <slug> strict                      -> fetch fails: exit 2, nothing built (F1)
  ids deduped, the first of each kept
  per id: addressed-to check, on those rows       -> fails: exit 2, nothing built
          an ack from <slug> answering the id, in
          read_mailbox <slug> cache sent          -> found: skip, `mail — already acked <id>`
          derive_message_id, check_mail_duplicate -> rc 1 or 2: exit 2, nothing built
  no id left                                      -> exit 0, nothing written
  write_mail_ref <ref> <tip read> <ack> ...       -> 0 landed · 1 lost write · 2 not completed
```

### The left-shift table

S20 files one ask row per gate. Rows 1 to 6 are what unit 64 §3 defers from the round-4 audit;
rows 7 to 9 are this audit's own gates, which this unit does not build.

| Row | Gate | Source |
|---|---|---|
| 1 | ledger lint: a ledger line names a leg absent from that pass's `tools/gate-legs.json` | round-4 audit |
| 2 | spec-tokens: a "superseded" or "reads as" clause naming a sibling text sits in the ledger-answer criterion | round-4 audit |
| 3 | spec-tokens: a §7 arm's suite is run by a leg, or is marked withheld with its runner | round-4 audit |
| 4 | spec-tokens: Files touched naming a template with a declared render names the render | round-4 audit |
| 5 | spec-tokens: an Inventory adding a top-level symbol in a mapped file names `symbols.json` | round-4 audit |
| 6 | the reconcile step in the lander: diff the leg names of two bases and run the guards join | round-4 audit |
| 7 | ledger lint: a superseded item's criterion whose subject the superseding spec moves is listed | this audit, M5 |
| 8 | spec-tokens: a bare `S<n>` in a sentence naming another spec's id carries that id | this audit, L4 |
| 9 | the bug-class checklist entries the round-4 and round-5 audits name | both audits |

### Inventory

None minted in code. S20's rows and, if S22 files it, the dPlacedRequest row each take the next free
id of their family at the pass. Each other name an item uses is minted by unit 5, 22, 61, 63, 64 or
TOOL-dPlacedRequest-13.

### Migration

None: no stored record changes shape. The skip writes nothing, and the ask row changes only which
feed lines a later unit appends.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: S1, S12, S24
- `tools/unattended/unattended.test.sh`: S1, S3, S12 and S24's cases, S9's floors
- `tools/unattended/VERBS.template.md`, `memory/guides/UNATTENDED-VERBS.md`: S12, S24
- `tools/loop/loop_transition.py`: S11, only if a `--mail chain` call survives
- `tools/runlog/selftest.py`: S4, S5
- `tools/lib/resolve-python.test.sh`: S25
- `tools/workflows/unattended-build.template.js`, `tools/workflows/unattended-build.js`: S21
- `memory/builds/dKeptSession/build/`: the ledger answers of S2, S7, S8, S17, S19 and S20
- `memory/builds/dKeptSession/spec/`: S26's leg lines, at reconcile
- `memory/builds/dKeptSession/BACKLOG.md`, `memory/backlog/KICK.md`,
  `memory/builds/dKeptSession/README.md`: S20, S23
- `memory/builds/dPlacedRequest/BACKLOG.md`, `memory/backlog/TOOL.md`,
  `memory/builds/dPlacedRequest/README.md`: S13, S18, S22

### Alternatives rejected

- **Two batches.** The mail items and the rest both write `tools/unattended/unattended.test.sh`
  (S1 and S9) and the ledgers under `memory/builds/dKeptSession/build/`, and S20 writes an authored
  backlog shard, so the two write sets are not disjoint by M6's clauses.
- **Making unit 5 S7's precedence explicit and superseding it, for S1.** §8 F2.
- **Keeping `add_feed_event` after the walk, for S13.** §8 F3.
- **The renderer for S21 as a separate adopter.** `tools/workflows/kit.toml:96` records that this kit
  has none: the parity gate's `--render` mode is the renderer.

## 5. Production-readiness checklist

- security — S12 refuses on a failed fetch before any commit; a skip writes nothing.
- perf / scale — the batch makes one fetch and reads the cache once per mode; S26 compares two name
  sets.
- error / empty / loading states — an empty list exits 0 (S24); a failed fetch exits 2 (S12); a
  fully skipped batch exits 0 and writes nothing.
- observability — each skipped id is named on stderr; each ledger answer names this unit's id.
- risks — S13's ask changes the success exit every governance-ref writer shares; a deletion keeps its
  one event, and a single-commit update still appends one.
- testing — the criteria of §6 and the arms of §7.
- migration — §4.
- user docs — the `--mail ack` line of `tools/unattended/VERBS.template.md` and its render state the
  grammar, the fetch and its exit (S12, S24).

## 6. Acceptance criteria

Fixtures are each repaired unit's own, named by that unit's spec, under `%TEMP%`.

- **AC1** — When `<a>` is answered by `--mail answer` and then acked in `KICK-dKeptSession-5`'s
  fixture repository, and `--mail ack <slug> <a>` and `--mail ack <slug> <a> <c>` then run through
  unit 64 AC1's scratch copy of `unattended.sh`, each prints `mail — already acked <a>` and no
  `DUPCHECK <a>` and exits `0`; the second lands only `<c>`'s ack.
  Red when: the skip reads the `state` column, which reads `answered`, and the batch exits 2.
- **AC2** — When a second clone's session acks `<a>` and pushes, and the first clone then runs
  `--mail ack <slug> <a>` through a scratch copy of `unattended.sh` printing `FETCH` on stderr at
  `read_mailbox`'s fetch, `FETCH` prints before any `DUPCHECK`, `mail — already acked <a>` prints,
  the exit is `0` and `git rev-parse` of the session ref is unchanged; with the remote's URL pointed
  at an absent directory the same call exits `2` and the tip is unchanged.
  Red when: the batch reads the cache unfetched and lands a second ack of `<a>`.
- **AC3** — When `grep -n -F -- "--mail ack <slug> [<id> ...]"` runs over
  `tools/unattended/VERBS.template.md`, it prints the one `--mail ack` line, and `--mail ack <slug>`
  with no ids exits `0` with the session ref's tip, read by `git rev-parse`, unchanged.
  Red when: the empty call exits 2 or moves the tip.
- **AC4** — When a `python -c` probe parses the runlog kit's selftest module with `ast`, every
  module-level statement holding the string `GOV_REMOTE` or `GOV_DEFAULT_BRANCH` is an
  `os.environ.pop(<name>, None)` call, alone or in a loop, or a `del` under an `in os.environ`
  guard; executed in a child with neither variable set they raise nothing, and in a child with both
  planted they leave neither in `os.environ`.
  Red when: a bare `del os.environ[...]` raises `KeyError` in the child with neither set.
- **AC5** — When `python <repo>/tools/check-spec-tokens.py` runs in a scratch repository under
  `%TEMP%` built by `tools/check-spec-tokens.test.sh:199-207` and `:591-592`, whose
  `tools/gate-legs.json` declares `policy fixtures` with guards `{prefix}/policy/` and
  `tools/memory-tree/gen_build_index.py` in its `{prefix}` spelling, with tracked stubs at both and copies of units 58 to 64,
  it prints the `guards` hit `policy fixtures <- tools/memory-tree/gen_build_index.py` for unit 64's
  copy with the name off its leg line, prints no `SPEC_GUARD_LEGS_CUTOFF blank (arm off)` line, and
  prints neither once the name is on it.
  Red when: the conf leaves the key blank and the hit lands in NEAR.
  fixture: built by the probe, its `.memory-tree.conf` arming `SPEC_GUARD_LEGS_CUTOFF` at
  2026-09-01; the tree holds none today.
- **AC6** — When AC5's fixture also declares `loop selftest` with guard `{prefix}/loop/` in a
  reconciled manifest, with stubs at the loop kit's two paths and units 61 and 64 copied, the checker
  prints a `guards` hit `loop selftest <-` naming unit 61's loop-kit path before the step and none
  after it; and when a reconciled manifest renames `real leg` to `real leg two` over a copy naming
  `real leg`, the checker prints a `leg` hit for `real leg` before the step and neither a `leg` nor
  a `guards` hit after it.
  Red when: the step only adds names, so the old name's `leg` hit stands.
  fixture: AC5's, armed the same way.
- **AC7** — When `git diff <parent of 63's pass>..HEAD -- tools/unattended/unattended.test.sh` is
  read at this unit's pass, the line marked `SHADOWED` is unchanged, the effective
  `FLOOR_ASSERTIONS=` line rises by the counted assertions the diff adds less those it takes out,
  and the `FLOOR_SHARD_<k>=` lines that move sum to that rise.
  Red when: the rise counts a subset of the diff's cases.
  figure: PINNED, `2776` read at base on 2026-10-26; the rise DERIVED off the diff.
- **AC8** — When
  `git grep -n -e read_mail_chain -e "--mail chain" -- tools memory/guides ':!tools/unattended/unattended.test.sh'`
  runs at this unit's pass, it prints nothing.
  Red when: the loop kit's transition still calls `--mail chain`, a verb that no longer exists.
- **AC9** — When `grep -n` reads the ask row in `memory/builds/dPlacedRequest/BACKLOG.md`, it says
  the walk takes the place of `add_feed_event` for a create or an update, that a deletion keeps the
  single `add_feed_event`, and that a three-message chained landing appends exactly three events
  with `--feed check` passing; and `grep -o -E '(^|[^0-9]) S[0-9]+'` over the row prints nothing.
  Red when: the row leaves the walk's order open, or a bare `S3` names the wrong unit's item.
- **AC10** — When `grep -n "SEV · KICK-dKeptSession-"` runs over
  `memory/builds/dKeptSession/BACKLOG.md`, it prints one row for each of the nine gates of §4's
  left-shift table beside the existing one, each id with its ask row, and unit 64's ledger answer to
  its §3 left-shift bullet names those ids.
  Red when: a gate of the table has no row.
- **AC11** — When `git diff HEAD~1 -- tools/workflows/unattended-build.template.js` and the same diff
  of `tools/workflows/unattended-build.js` are read at this unit's pass commit, their changed lines
  are the same, and `grep -c 'candidates for one parallel group'` prints `1` over each.
  Red when: the render's change differs from its template's, so the parity leg reds at the close.
- **AC12** — When `blk s <file>`, copied from the resolver kit's test file, runs with
  `MARKER_LEAD='(# |// )'` over a scratch file holding a `// >>> s` ... `// <<< s` block followed by
  trailing lines, it prints the block and none of the trailing lines.
  Red when: the closer still reads `^# <<< `, so the block runs to the end of the file.
- **AC13** — When `grep -n "KICK-dKeptSession-65"` runs over unit 64's acceptance ledger, it prints
  an answer to each unit 64 text superseded here: S1, S3, S5, S7, S9, S10, S13, S14, S16, S17, S18,
  §3's left-shift bullet, §4's Evidence, sketch, Files touched and S1 alternative, §7's leg line,
  runlog arm and reconcile note, AC5, AC8,
  AC9, AC10, AC11, AC17 and AC18; and over 63's ledger, answers to AC14's `build_arm_env` clause,
  §7's runlog arm line and the `_check_inside` sentence carrying `:991`, `:1131` and `:1204`.
  Red when: a superseded text has no answer.
- **AC14** — When `python tools/memory-tree/gen_build_index.py --write` runs after this unit's pass
  commit, `git status --porcelain -- memory/backlog memory/builds/dKeptSession/README.md memory/builds/dPlacedRequest/README.md`
  prints nothing.
  Red when: a rev bump or a new ask row was committed without its render.

## 7. Gates

`build-index selftest` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `review-join self-test` · `review-protocol parity (kit vs dogfood)` · `pre-push run-log line` · `run-gates run-log line` · `runlog selftest` · `recall floor` · `recall floor arms` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The reconcile adds `policy fixtures`, and `loop selftest` once dDeclaredLoop lands it, to the line
above, by unit 64 S9 and S26 here.

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 · an answered-and-acked id, a pushed ack seen only after the fetch, an unreachable remote and the empty list, staged red by a scratch `unattended.sh` whose skip reads the `state` column and whose batch skips the fetch · the effective `FLOOR_ASSERTIONS` pin and its region's `FLOOR_SHARD_<k>` rise by the counted cases, derived off the diff; a withheld suite run by the shard runner, not by a leg
New arm: tools/runlog/selftest.py · covers AC4 · the suite started with neither variable and with both planted, staged red by a copy whose scrub is a bare `del` · none
New arm: tools/lib/resolve-python.test.sh · covers AC12 · a `// >>> s` block followed by trailing lines, staged red by a `blk` whose closer reads `^# <<< ` · none

## 8. Open questions

- **F1 — What does `--mail ack` do when its fetch fails, id 20?** Options: (a) read the local copy,
  named on stderr, as unit 5 §8 F3 rules for the transition guard; (b) exit 2 with nothing built, as
  `read_mailbox <slug> strict` does; (c) give the verb a `soft` or `strict` argument. (c) adds a
  public surface, so veto 2 discards it. (a) lets a stale cache pass a second session's ack and
  lands a duplicate, the consequence id 20 names. (b) costs an offline build nothing, because
  `write_mail_ref` pushes and fails offline anyway. RESOLVED (agent, 2026-10-26, delegated): (b),
  rung 3. widens: none · relaxes: none
- **F2 — Where does the "already acked" skip read, ids 1, 11 and 21?** Options: (a) the `kind` and
  `answers` columns of `read_mailbox <slug> cache sent`, whatever the state; (b) make unit 5 S7's
  precedence give `acked` its own column and supersede S7 by name. (b) changes a reader every
  transition guard shares, to serve one verb. (a) reads a fact that already exists and changes no
  reader. RESOLVED (agent, 2026-10-26, delegated): (a), rung 2. widens: none · relaxes: none
- **F3 — Does the walk take the place of `add_feed_event`, or run before it, id 23?** Options: (a)
  for a create or an update the walk alone appends, the tip as its newest event, and a deletion
  keeps `add_feed_event`; (b) the walk runs first and `add_feed_event` still runs after it. (b)
  works, since `add_feed_event` is keyed and appends nothing twice, but it leaves two appenders on
  one exit and an order a later edit can flip. (a) leaves one appender per input shape. RESOLVED
  (agent, 2026-10-26, delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, the round-5 minors batch's audit's minors batch.

## 10. Reuse audit

Every item extends the seam its repaired unit names: `read_mailbox`'s `strict` fetch and its
`cache sent` rows (unit 5 S6, unit 63 S11) for S1, S2, S3 and S12; the `GIT_*` scrub loop
(`tools/runlog/selftest.py:355-356`) and `os.environ.pop` for S4 and S14; the spec-tokens self-test's
`scratch` builder and guards fixture (`tools/check-spec-tokens.test.sh:199-207`, `:591-592`) for S6,
S7 and S10; the guards join (`tools/check-spec-tokens.py:1543-1579`) for S26; the kit's
`[[regenerate]]` argv (`tools/workflows/kit.toml:115-116`) for S21; `gen_build_index.py --write` for
S22 and S23; and TOOL-dPlacedRequest-13 S4's `add_feed_sightings` for S13.
`python tools/codebase-map/reuse_lookup.py "unset an environment variable only when it is present"`
ranked `present`, `check_gen_region_only` and `check_lease_only_diff` by name stem only, and none of
them scrubs an environment, so no existing seam fits the scrub beyond the `GIT_*` loop beside it.

Recall terms used:
`python tools/memory-recall/query.py "how does a minors batch amend an earlier batch unit's acceptance and fixture recipes" --terms "promoted batch minors ledger superseded skip fetch cache reconcile renamed leg scrub render"`
