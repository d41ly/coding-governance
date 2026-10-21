# TOOL-dTrueNorth-7 — the carry-forward of a unit a spec run adds, once, and the starting roster it rests on

**Status:** OPEN · rev-2 · 2026-10-21 · node d · Tier-2 · base 271aa59d · streams tooling · order 8

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-21-build-TOOL-dTrueNorth-7-deviation-2.md](../build/2026-10-21-build-TOOL-dTrueNorth-7-deviation-2.md) | deviation | — |
| [2026-10-21-prompt-TOOL-dTrueNorth-1-spec-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-1-spec-brief.md) | research | TOOL-dTrueNorth-1 TOOL-dTrueNorth-2 TOOL-dTrueNorth-3 TOOL-dTrueNorth-4 TOOL-dTrueNorth-5 TOOL-dTrueNorth-6 |
| [2026-10-21-prompt-TOOL-dTrueNorth-7-build-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-7-build-brief.md) | journal | — |
| [2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md](../reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md) | spec-audit | TOOL-dTrueNorth-1 TOOL-dTrueNorth-2 TOOL-dTrueNorth-3 TOOL-dTrueNorth-4 TOOL-dTrueNorth-5 TOOL-dTrueNorth-6 |

<!-- /gen:spec-records -->

## 1. Goal

Every chain build after dTrueNorth runs twice. A spec run specs every roster unit and defers each
against the ask its opening filed, and a build run then builds them (P0.5, README rule 1). Today's
carry-forward term cannot close that spec run. Its condition 2 reads the roster the run started with
from the generated `gen:build-units` region, which names no unit before a build has a spec, so every
chain spec run fails `build-complete` at `--close` (plan review H1). The same condition refuses every
unit a run added, so a spec run that promotes a review finding or adopts a discovery can neither build
that unit nor carry it (ER:314-320). This unit makes both work, as the owner approved in
`PLAY-dClosedLoop-2`. The starting roster falls back to the authored `roster:units` pair, and a spec
run carries a unit it added to its own build's next run, once. It is the execution plan's `[phase-1]`
"The extra unit", lines 732-803, whole.

## 2. Scope (IN)

- **S1 — the authored roster at a commit.** `read_roster_at` in `tools/unattended/lib-unattended.sh`
  prints the unit ids that the authored `<!-- roster:units -->` pair names in a build README at a
  named commit, one per line. It keeps only ids of that build's own slug, the way `roster_ids` scopes
  them (`unattended.sh:4600-4632`); the slug is the README's parent folder. It exits 1 with its reason
  as its only output, as `baseline_units` and `pinned_units` do, when the pair is absent, malformed or
  names no id of the slug. Observed by AC5, AC13 and AC17.
- **S2 — the fallback inside `baseline_units`.** At the baseline commit `baseline_units` already
  chooses, when the generated pair is well-formed and names no unit (`lib-unattended.sh:2014-2018`
  today), it reads S1 at that same commit and prints those ids. When S1 refuses too, it exits 1 with
  one reason naming both regions. Every earlier refusal, the `UNITS_REGION_CUTOFF` grandfather
  included, is unchanged and still comes first. Its three callers take the fallback with no edit of
  their own: condition 2 (`unattended.sh:5173`), `--rescope --act add` (`unattended.sh:13257`) and
  check 24 (`check-unattended.sh:3907`). Observed by AC5, AC11, AC12, AC13 and AC14.
- **S3 — the spec-run test.** `check_spec_run` in `tools/unattended/unattended.sh` is README rule 1
  read by the driver, and it reads both halves at the run's pinned `base:` (F2). The ask half runs
  first: the build's `BACKLOG.md` at `base:` files an ask under the build's own slug (`asks_filed_by`
  over `backlog_blob_of`), and the ask witness called `--at <base>` reads at least one of them neither
  CLOSED nor WONTDO (F8). The roster half follows: S1 at `base:` names a unit that the generated
  region at `base:` does not, which is a unit `MISSING` there. A generated pair that is absent or
  malformed at `base:` cannot answer that, so it is exit 2. Exit 0 means a spec run. Exit 1 means
  not one, and exit 2 means it cannot be read, each with its reason in `SR_WHY`. Whether the run closes
  a unit plays no part. Observed by AC1, AC4, AC6 and AC8.
- **S4 — condition 2, rewritten.** In `check_carry_forward`, a DEFERRED unit is ADDED when this run's
  record carries its `rescope · item add <unit>` row, or when the starting roster does not carry it.
  A unit that is not added is checked as today. An added unit is carried only when `check_spec_run`
  exits 0 and the add row exists (F4). The test runs at most once per close, and only when an added
  unit is met. Its three refusals are in §4 Data model. A carried added unit prints its own
  `carried forward` line, which names it as added. Observed by AC1, AC2, AC4, AC6, AC8 and AC10.
- **S5 — once, and its witness.** `scan_landed_carry` in `tools/unattended/unattended.sh` reads the
  build's rotated `RUN.LANDED.<blob8>.md` archives tracked at the graded commit. It prints the first
  one that carries both an `add` row and a `defer` row for the unit. Condition 2 then refuses every
  DEFERRED unit, roster or added, that an archive names, and the build run must build it. An archive
  of any other phase is no witness, so an aborted run's rows do not count. Observed by AC3, AC7, AC9
  and AC10.
- **S6 — the carriers.** `tools/unattended/STOPS.template.md` §15 restates term 2.
  `tools/unattended/VERBS.template.md` close rule 9 names the spec run's added unit, carried once. The
  review-exit sentence at its line 794 stops saying that a promoted unit is never carried (F6). Both
  renders, `memory/guides/UNATTENDED-STOPS.md` and `memory/guides/UNATTENDED-VERBS.md`, are re-copied by
  `bash tools/unattended/adopt-unattended.sh`. Observed by AC15 and AC16.
- **S7 — the comments that state the rule.** The header above `check_carry_forward`
  (`unattended.sh:5132-5154`) restates condition 2 as S4 and S5 have it. Check 24's baseline comment
  (`check-unattended.sh:3893-3905`) names the fallback. Observed by AC17.
- **S8 — the standing fixtures.** The cases of AC1 to AC14 are kept as arms of the kit's own suites,
  declared under §7. The one existing arm this unit moves is TOOL-dUnstuckLanding-18's AC4 block
  (`unattended.test.sh:16716-16734`). Its base roster names `ARCH-tCarry-2` unspecced beside an open
  ask, so under S3 it would read as a spec run. Its authored roster is narrowed to `ARCH-tCarry-1`, so
  it stays the build-run case it was written for. NOT OBSERVED — README rule 8 waives the unattended
  suites' verdict for this landing; AC1 to AC14 observe every case as a targeted probe instead.

## 3. Non-goals (OUT)

- **The other carry-forward terms.** Conditions 1, 3, 4 and 5 are unchanged (plan:766), so an added
  unit is carried only with status `DEFERRED`, a defer row, and a header that advances an open ask of
  the build's own.
- **A unit added by a build run or a whole run.** It is refused as today and built in that run.
- **A region that names some of the authored roster.** The starting roster is then the region, as
  today. The union of the two was rejected in §4.
- **The spec run's own acts.** Speccing and auditing an added unit through the harness's scoped audit
  (`tools/workflows/unattended-build.js:180-183`), and writing its departure record with
  follow-through `new unit <id>`, are the run's acts. TOOL-dTrueNorth-4's population joins the `add`
  row.
- **`check_prompt_brief`'s authored-roster read** at `unattended.sh:3795`. It reads the same pair at
  base and is not routed through S1 (F7). Routing it is a follow-up.
- **The instruments.** `deviations.py`'s `derive_run_kind` (`build/…-deviations.py:580-593`) answers
  the same spec-run question for the departures report and is frozen by the packet's Non-goals.
- **The dispatch order gate** that counts a DEFERRED sibling as an unfinished step: ask
  `TOOL-aRoutedQuill-13`.
- **BUILD-METHOD M4 and the kit version constant.** Nothing in M4 forbids a deferral. The
  `KIT_UNATTENDED_VERSION` constant and the `gov:kit` markers do not move here.
- **The suites' verdict.** README rule 8 waives it; the clean reading is owed with
  `PLAY-dClosedLoop-11`.

### Edges

- **consumes-from** external — the carry-forward ask the opening filed in every chain build's
  `BACKLOG.md` but dTrueNorth's (P0.5). Without it no run passes S3's ask half.
- **hands-off** external — dGroundRules' two runs are the first to exercise the spec-run close and the
  build run's refusal of a re-deferred unit (plan:830-833); a disagreement found there is an ask in
  dClosedLoop's `BACKLOG.md`.
- **hands-off** `TOOL-dTrueNorth-20` — the guards-join hit `TOOL-dTrueNorth-12`'s guard makes on this spec's Files touched, which this unit's CLOSED status ends and that unit observes ended (the round-2 spec audit's id 24)

## 4. Design

### Evidence

Read at base `271aa59d`. Line numbers are PINNED to that reading, and the builder finds each by the
quoted text.

| Site | Where | What it does today |
|---|---|---|
| `baseline_units` | `lib-unattended.sh:1953-2020` | walks the run-state history to its first live-phase commit, else the caller's fallback, and prints the generated region there; refuses an id-less one at `:2014-2018` |
| live phases | `lib-unattended.sh:1982` | `BUILDING`, `RUNNING`, `VERIFYING`, `LANDING`, `LANDED`; `--preflight` writes `RUNNING` on a fresh record (`unattended.sh:7683`), so a spec run's baseline is its preflight commit |
| `pinned_units` | `lib-unattended.sh:1897-1943` | the sibling read at a named commit; the refusal shape S1 copies |
| condition 2 | `unattended.sh:5173-5185` | the roster read and its two refusals, unreadable at `:5179` and added at `:5183` |
| defer row read | `unattended.sh:5187` | the row pattern S4 and S5 reuse for `add` and `defer` |
| the one witness call | `unattended.sh:5213-5220` | condition 4's status read at HEAD |
| `run_ask_witness`, `ask_field` | `unattended.sh:4959-5024` | the witness, called `--at <rev>` |
| `asks_filed_by`, `backlog_blob_of` | `unattended.sh:5118-5130` | a build's own filings at a rev |
| `--rescope --act add` | `unattended.sh:13245-13263` | fail 48 "cannot be derived" when `baseline_units` refuses |
| check 24's ADD arm | `check-unattended.sh:3906-3943` | skips with the refusal's reason when `baseline_units` refuses |
| archive name | `unattended.sh:4373-4385`, `:8003-8016` | `RUN.<PHASE>.<8 hex>.md`, the phase the recorded one; a landed record archives as `LANDED` (`:4368-4370`) |
| `roster_ids` | `unattended.sh:4600-4632` | the working-tree roster, slug-scoped on both halves |
| STOPS §15 term 2 | `STOPS.template.md:703-704` | "a unit the run added … is never carried" |
| VERBS rule 9 | `VERBS.template.md:893-900` | unmet "when the unit was added during the run" |
| VERBS review exit | `VERBS.template.md:793-795` | "never DEFERRED to be carried forward" |

The brief and the plan cite `lib-unattended.sh:1950-2018`; the function reads at `:1953-2020` at base.
Every other line the plan cites matches.

### Data model

Condition 2, per DEFERRED unit, in this order, each refusal returning early:

1. The starting roster is read through `baseline_units`, with the pinned `base:` as fallback commit,
   as today. Unreadable refuses with the `:5179` message, unchanged.
2. The unit is ADDED when this run's record carries `rescope · item add <unit> · `, or the roster does
   not carry it. For an added unit:
   - `check_spec_run` exits 2: refused, "whether this run is a spec run cannot be read, so `<unit>`,
     which it added, cannot be carried forward: `<SR_WHY>`".
   - It exits 1: refused with the `:5183` message, unchanged, then "; this run is not a spec run, so it
     carries no unit it added: `<SR_WHY>`".
   - It exits 0 and the add row is absent: refused, "a spec run carries a unit it added only when its
     run-state file records the add, because that row is the witness the next run's once-check reads;
     record it with --rescope `<slug>` --act add --item `<unit>` --reason "<why>": `<unit>`".
3. For every DEFERRED unit, `scan_landed_carry` names an archive: refused, "a DEFERRED unit was added
   and carried forward by an earlier landed run of this build, and a unit a spec run adds is carried
   once, so this run must build it: `<unit>` in `<archive>`".

A carried added unit prints `carried forward — <unit>, added by this spec run and carried once,
DEFERRED against the open ask <ask>`. A roster unit keeps today's line byte for byte.

`SR_WHY`, in the order the halves run: the BACKLOG at `base:` files no ask under the slug; or none it
files reads open there, naming them; or S1's reason at `base:`; or every authored unit is specced at
`base:`. Exit 2 carries `AW_WHY`, names a `base:` that is absent or names no commit, or names a
generated pair at `base:` that is absent or malformed.

S2's both-refused reason: "the baseline roster names no unit in its generated region, and the
authored roster:units pair at the same commit `<is absent | is malformed | names no unit of this
build>`, so every unit this build has would read as added and the comparison would accuse rather
than check".

Under the fallback `baseline_units` prints ids, one per line, not region rows: two output shapes from
one producer, the `format-derived-from-arity` class. Every reader is safe with both. Condition 2,
`--rescope` and check 24's ADD arm ask membership through `id_in`. Check 24's RETIRE fallback asks
`id_rows … | grep '| WONTDO |'`, finds no status, and takes its strict direction. That is right,
because a region naming no unit held no WONTDO unit.

The witness at `base:` overwrites `AW_ROWS`. `check_spec_run` reads its statuses at once, before
condition 4's own call at HEAD.

### Fixtures

Each fixture is a scratch repository under `%TEMP%/tn7` (a short path: a clone under the scratchpad
fails with Filename too long). It is built the way the driver suite's carry-forward block builds
`tCarry`: a bare origin, `main` and a run branch, the suite's `mkconf` conf with `GATE_CMD="true"`
and `LANDER="echo land"`, and its ask stub as `ASKS_CMD`. A "before" reading runs the same fixture
under the kit as it stands at base, extracted by `git archive 271aa59d tools/unattended` under the
run's scratchpad.

| Name | State |
|---|---|
| FX-spec | `main` holds build `tSpec`: an authored roster naming `ARCH-tSpec-1` and `ARCH-tSpec-2`, a well-formed `gen:build-units` pair naming no unit, no spec, and a `BACKLOG.md` filing `EXMP-tSpec-9` open. The run: `--preflight tSpec`, a DEFERRED spec per roster unit carrying `advances EXMP-tSpec-9`, the region rendered with their rows, and one `--rescope --act defer` row each |
| FX-added | FX-spec, plus `--rescope tSpec --act add --item ARCH-tSpec-3`, its DEFERRED spec advancing `EXMP-tSpec-9` and its defer row |
| FX-landed | FX-added's record set to `phase: LANDED`, its branch merged to `main`, and the next `--preflight tSpec` rotating it into `RUN.LANDED.<blob8>.md`: a build run, since every roster unit is specced at its base |
| FX-whole | FX-spec with no ask filed at base; the run files `EXMP-tSpec-9` itself |
| FX-clone | a clone of this repository at the build commit under `%TEMP%/tn7c` (at base for the before reading), where `dGroundRules` stands as the opening left it: 11 authored units, no spec, `TOOL-dGroundRules-12` filed; its `.unattended.conf` declares `GATE_CMD="true"`, so `--close` runs no bar |

`BASELINE_PROBE` is check 24's roster read, run without the checker: a `bash` shell in the fixture
that sources `tools/unattended/lib-unattended.sh`, defines `region` as `check-unattended.sh:211-216`
defines it between its `kickoff_region` markers, and calls `baseline_units <RUN.md> <README> "" <base>`, the arguments
`check-unattended.sh:3907` passes. It is the unit's own code over a fixture, and it is no gate.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `read_roster_at` | shell function, `lib-unattended.sh` | `sh.function`; `python tools/lexicon/lexicon.py --suggest read_roster_at --as sh.function` answered OK |
| `check_spec_run` | shell function, `unattended.sh` | `sh.function`; the lexicon answered OK, and refused `is_spec_run` for `check` |
| `scan_landed_carry` | shell function, `unattended.sh` | `sh.function`; the lexicon answered OK, and refused `find_landed_carry` for `scan` |
| `SR_WHY` | shell global, `unattended.sh` | none; the `AW_WHY` and `RPB_WHY` shape |

### Rollout

1. S1 and S2 in the library, then S3, S5 and S4 in the driver, then S7.
2. S6, then `bash tools/unattended/adopt-unattended.sh` to re-copy both renders.
3. S8's arms, then each criterion observed as its targeted probe, before (the base kit) and after.
4. One commit with the unit id in the subject. The deviation record `deviation-2` was written with
   this spec and is not the build's.

### Files touched (estimate)

- `tools/unattended/lib-unattended.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/STOPS.template.md`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-STOPS.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/check-unattended.test.sh`

### Alternatives rejected

- **The union of the region and the authored roster as the starting roster.** A unit planned in the
  authored roster but unspecced at the baseline would stop owing check 24 an `add` row on every build,
  not only on one whose region names nothing. That changes check 24 and condition 2 beyond the reading
  the approval names, "the reading the approved condition needs to work at all" (plan:763-764).
- **A run-kind fact pinned at `--preflight`.** The run would declare itself a spec run, and the plan
  wants "the README's rule … read by the driver" (plan:735).
- **The once-witness read from the run-state file's history** rather than from rotated archives. An
  aborted run's rows are in that history too, and the plan's witness excludes them (plan:745-747;
  review fold-a id 7).
- **One witness call per close.** Condition 4 grades HEAD and S3 grades `base:`, two revisions one
  call cannot ask.

## 5. Production-readiness checklist

- security — no new write path. The new reads are git blobs and the declared ask witness. A
  run-written fact cannot make a run a spec run: both halves of S3 read the pinned `base:`.
- perf / scale — one extra witness call per close, and only when an added DEFERRED unit is present;
  one `ls-tree` and one blob read per LANDED archive of the build.
- error / empty / loading states — an unreadable spec-run test, an empty authored roster and an absent
  one each refuse with their reason; none reads as met.
- observability — each refusal names the unit and the condition; a carried added unit prints its own
  line, which the departures report lists.
- risks — `check_spec_run` and `deviations.py`'s `derive_run_kind` answer one question two ways: a
  status from the witness against a BACKLOG parse, and a region at `base:` against spec H1s. They
  agree while hygiene check 9 keeps the index fresh. A disagreement goes to an ask under the plan's
  instrument-successor rule (plan:838-841). An existing suite arm whose fixture newly reads as a spec
  run reds unseen at this landing. The one found by reading moves under S8, and the owner's run under
  `PLAY-dClosedLoop-11` reads the rest.
- testing — AC1 to AC14 as targeted probes over the fixtures in §4, each before and after, with the
  staged break each names; the arms under §7.
- migration — none. A build with no added DEFERRED unit and a non-empty region grades as before.
- user docs — `memory/guides/UNATTENDED-STOPS.md` §15 and `memory/guides/UNATTENDED-VERBS.md`; no page
  under `help/` covers the carry-forward term.

## 6. Acceptance criteria

- **AC1** — When `unattended.sh --close tSpec` runs over FX-added, with the add row's reason "promoted
  by the closing diff review", `build-complete` meets. It prints
  `carried forward — ARCH-tSpec-3, added by this spec run and carried once` and a plain carried line
  for each roster unit.
  Red when: the base kit refuses it; and with S4's spec-run branch alone staged out, the close is
  unmet naming `ARCH-tSpec-3` with the `:5183` message while both roster units pass.
  fixture: FX-added, in a scratch repository; the tree holds none today.
- **AC2** — When the same close runs over FX-added with the add row's reason "an adopted discovery",
  it meets and prints the same added line for `ARCH-tSpec-3`.
  Red when: the base kit refuses it; and the same staged break as AC1 refuses it.
- **AC3** — When `unattended.sh --close tSpec` runs over FX-landed, where the build run closes
  `ARCH-tSpec-1` and `ARCH-tSpec-2` and defers `ARCH-tSpec-3` again, `build-complete` is unmet. Its
  message is the once refusal naming `ARCH-tSpec-3` and the `RUN.LANDED.` archive.
  Red when: the base kit carries `ARCH-tSpec-3`; and with `scan_landed_carry` staged to print nothing,
  it is carried.
- **AC4** — When the build run of FX-landed, having closed a unit, adds `ARCH-tSpec-4` with
  `--rescope --act add` and defers it, `unattended.sh --close tSpec` is unmet. The message is the
  `:5183` text naming `ARCH-tSpec-4`, then "this run is not a spec run".
  Red when: S3's roster half is staged out, so the build run reads as a spec run and `ARCH-tSpec-4`
  is carried; the base kit refuses it too.
- **AC5** — When FX-clone follows README rule 1 in full, `unattended.sh --close dGroundRules` names
  no unmet `build-complete` item. It prints one `carried forward` line for each of
  `TOOL-dGroundRules-1` to `TOOL-dGroundRules-11`. The run specs every roster unit `DEFERRED` with
  `advances TOOL-dGroundRules-12` and a defer row each, then closes. The `BASELINE_PROBE` of §4, run
  over the same record with check 24's arguments, prints the same eleven ids, so check 24 and the
  driver read one roster.
  Red when: the base kit fails term 2 with "the roster this run started with … cannot be read"; and
  with S2's fallback alone removed, it fails the same way and the probe exits 1 with "the baseline
  roster names no unit".
  cost: minutes, for a clone and eleven specs.
  fixture: FX-clone; `dGroundRules` is in that state at base.
  permission: check 24's own verdict is `check-unattended.sh`'s, the `unattended kit gate` leg's
  command, which a build pass does not run; the main loop reads it over this fixture at the close.
- **AC6** — When a build run of FX-landed closes no unit and defers `ARCH-tSpec-4`, which it added,
  `unattended.sh --close tSpec` is unmet with the AC4 message.
  Red when: S3's roster half is staged to read "this run closed no unit" instead, so `ARCH-tSpec-4` is
  carried; the base kit refuses it too.
- **AC7** — When a build run of FX-landed closes no unit and re-defers all three units,
  `unattended.sh --close tSpec` is unmet. The message is the once refusal naming `ARCH-tSpec-3`, and
  no refusal names a roster unit (F3).
  Red when: the base kit carries all three; and with `scan_landed_carry` staged to match a `defer` row
  alone, the refusal names `ARCH-tSpec-1`.
- **AC8** — When FX-whole's closing review promotes `ARCH-tSpec-3`, which the run adds and defers
  against the ask it filed itself, `unattended.sh --close tSpec` is unmet. The message is the `:5183`
  text with "this run is not a spec run" and the no-ask reason.
  Red when: S3's ask half is staged to read HEAD's `BACKLOG.md`, so the run's own ask counts and
  `ARCH-tSpec-3` is carried; the base kit refuses with "cannot be read".
- **AC9** — When FX-added's run is set to `phase: ABORTED` after its defer rows and rotated by
  `--preflight tSpec`, and the second run re-adds `ARCH-tSpec-3` and defers all three,
  `unattended.sh --close tSpec` meets with all three carried.
  Red when: `scan_landed_carry` is staged to read every rotated `RUN.*.md`, so the close refuses
  `ARCH-tSpec-3` naming the `RUN.ABORTED.` archive; the base kit refuses with "cannot be read".
- **AC10** — When FX-clone adds `missing:TOOL-dGroundRules-13` beside the eleven, `--close dGroundRules` prints
  the added line for it and plain lines for the eleven. The build run that follows the landed spec run
  re-defers it, and its `--close` is unmet with the once refusal naming it.
  Red when: S4 is staged to print the roster line for every unit, so the added line is absent; and with
  `scan_landed_carry` staged to print nothing, the build run carries it.
  cost: minutes, as AC5.
- **AC11** — When FX-spec specs `ARCH-tSpec-3` with no `add` row, the `BASELINE_PROBE` over its record
  exits 0 and prints `ARCH-tSpec-1` and `ARCH-tSpec-2` but not `ARCH-tSpec-3`. Check 24's ADD arm
  compares that output with the executing region at `check-unattended.sh:3937-3942` unchanged, so it
  owes an `add` row for `ARCH-tSpec-3` where it skipped before.
  Red when: the base kit's `baseline_units` exits 1 with "the baseline roster names no unit", the
  reason check 24 prints as "ADD arm skipped".
  permission: the fail 24 line itself is `check-unattended.sh`'s; the main loop reads it over this
  fixture at the close, through the `New arm:` in §7.
- **AC12** — When FX-spec has `ARCH-tSpec-3`'s spec in the region and runs
  `unattended.sh --rescope tSpec --act add --item ARCH-tSpec-3`, it prints
  `LATE record — ARCH-tSpec-3 entered the roster after this run went live` and writes the row.
  Red when: the base kit fails 48 with "cannot be derived"; and with S2's fallback removed, it fails
  the same way.
- **AC13** — When FX-spec's authored pair encloses no row, and again when it is absent, the
  `BASELINE_PROBE` exits 1 and prints S2's both-refused reason naming that state, which check 24's
  ADD arm reports as a skip.
  Red when: S1 is staged to treat an empty pair as an empty success, so the probe exits 0 with no id
  and check 24 would fail 24 on both specced units.
  permission: the skip line itself is `check-unattended.sh`'s; the main loop reads it at the close.
- **AC14** — When FX-spec is built with one roster unit, `ARCH-tSpec-1`, alone, `unattended.sh --close
  tSpec` meets and prints one `carried forward` line for it.
  Red when: the base kit fails term 2 with "cannot be read" naming `ARCH-tSpec-1`; and with S2's
  fallback removed, it fails the same way.
- **AC15** — When `sed -n '/^## 15\./,$p' memory/guides/UNATTENDED-STOPS.md` runs, term 2 names the
  spec run, the authored `roster:units` fallback and `RUN.LANDED.`.
  `cmp tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md` exits 0.
  Red when: term 2 still says an added unit is never carried, or the render was not re-copied.
- **AC16** — When `grep -n 'spec run' tools/unattended/VERBS.template.md` runs, it prints a line of
  close rule 9 and a line of the review-exit paragraph near its line 794.
  `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` exits 0.
  Red when: either sentence still says only a roster unit is carried, or the render was not re-copied.
- **AC17** — When `grep -c '^read_roster_at()' tools/unattended/lib-unattended.sh` runs it prints 1,
  and the same grep over `tools/unattended/unattended.sh` and `tools/unattended/check-unattended.sh`
  prints 0. The non-comment `baseline_units ` call counts stay 2 in the driver and 1 in the checker.
  `grep -n 'spec run' tools/unattended/unattended.sh` prints a line inside the comment above
  `check_carry_forward`.
  Red when: a second definition exists, or the comment still says an added unit is never carried.
  figure: the counts 2 and 1 are DERIVED from base, where they stand today.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `harness arms (fail branches armed or pinned)` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a fork spent on builtin work)` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 AC10 AC12 AC14 AC17 · the spec-run block's FX fixtures, each case staged by its own fixture edit, and the moved TOOL-dUnstuckLanding-18 AC4 block · none

New arm: tools/unattended/check-unattended.test.sh · covers AC11 AC13 · check 24 over FX-spec with an unrecorded added unit, an empty authored pair and an absent one · none

README rule 8 waives both suites' verdict at this landing. The close's red-then-green observation of
each arm is therefore the targeted probe its covered criteria name, run before and after. The suites'
own clean reading is owed with `PLAY-dClosedLoop-11`.

## 8. Open questions

- **FACT-QUESTION · F1 — Is `DRAFT`, the status the spec brief names, a legal spec status?** Probe:
  `grep -n 'OPEN · SPECCED' memory/HYGIENE.md` prints the seven tokens spec headers reuse (HYGIENE.md
  lines 104-109). Liveness: the line would print `DRAFT` if the vocabulary declared it. Observed: it
  does not, so a `DRAFT` header fails check 12. RESOLVED (agent, 2026-10-21, delegated): `OPEN`, which
  TEMPLATE-SPEC gives as "drafting".
- **F2 — Which commit does the spec-run test read?** (a) The pinned `base:`, for both halves. (b) The
  commit `baseline_units` chooses. Under (b) an ask the run filed while `SPECCING`, before its first
  live-phase commit, would count, against "an ask the run files itself does not count" (plan:738),
  and the driver would disagree with `deviations.py`'s run kind, which reads `base:`
  (`build/…-deviations.py:580-593`). Veto 1 discards (b). Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-21, delegated): (a).
- **F3 — Does "once" bind a roster unit an earlier landed run carried?** (a) Only a unit that run
  added, so its archive carries both an `add` and a `defer` row. (b) Any unit an earlier landed run
  deferred. (b) refuses a roster unit set aside against a still-open ask over two runs, which
  TOOL-dUnstuckLanding-18 permits and the plan keeps (plan:766). The plan names the witness as the
  spec run's add and defer rows (plan:745), and red case 10 says "as an added unit, not a roster unit".
  Veto 1 discards (b), and red case 7 reads as an added unit. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-21, delegated): (a).
- **F4 — Must an added unit's add row stand in this run's record for it to be carried?** (a) Yes.
  (b) No, absence from the starting roster suffices. Under (b) the next run's once-check finds no add
  row and carries the unit a second time, against "once has a witness" (plan:745). Veto 1 discards
  (b). Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-21, delegated): (a).
- **F5 — What does `baseline_units` print under the fallback?** (a) The slug-scoped ids, one per line.
  (b) The authored pair verbatim. Under (b) a foreign id in the Carries or Clause column, as
  dTrueNorth's README carries `PLAY-dClosedLoop-2` on its line 67, makes an id-less roster read
  non-empty and answers membership for a non-unit. Both shapes answer `id_in` alike. Recommendation
  (a), on `roster_ids`' slug-scope precedent. Rung 3.
  RESOLVED (agent, 2026-10-21, delegated): (a).
- **F6 — Does this unit amend the review-exit sentence at `VERBS.template.md:794`?** (a) Yes, to "never
  DEFERRED to be carried forward, except once by a spec run". (b) Leave it. (b) leaves the verb
  carrier saying a promoted unit is never carried while §15 says a spec run carries one, two answers
  to one question (charter `[one-fact]`). Veto 1 discards (b). Veto 2 on (a), a carrier change, is
  lifted by `may: PLAY-dClosedLoop-2`, which approves this unit's carry-forward condition, its carrier
  edits included (phase0-decisions `[row-1]`, `[row-2]`). Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-21, delegated): (a) · grants: PLAY-dClosedLoop-2 the VERBS.template.md
  review-exit sentence.
- **F7 — Is `check_prompt_brief`'s authored-roster read (`unattended.sh:3795`) routed through S1?**
  (a) Yes, as charter `[reuse]` asks at a second instance. (b) No. (a) changes a carrier for prompt-mode
  preflight, which the carry-forward condition does not need, so `PLAY-dClosedLoop-2` does not cover
  it and veto 2 discards it. (b) survives, and the follow-up is named in §3. Recommendation (b).
  Rung 3. RESOLVED (agent, 2026-10-21, delegated): (b).
- **F8 — How does the ask half read "open"?** (a) The witness at `--at <base>`, the driver's one
  status reader (`unattended.sh:5110-5114`). (b) Filing alone. (b) counts an ask already CLOSED at base,
  against "holds an open ask" (plan:736). Veto 1 discards (b). Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-21, delegated): (a).

## 9. Revision log

- rev-1 · 2026-10-21 · initial draft, from the spec brief, the execution plan's `[phase-1]` lines
  721-862 and `[deviations]` lines 1208-1295, decision rows `PLAY-dClosedLoop-2` and `-3`, the plan
  reviews' H1, fold-a ids 5 and 7 and fold-b M5, and the driver, library, checker, two templates and
  driver suite read at base `271aa59d`.
- rev-2 · 2026-10-21 · §3 · the Edges block gains a hands-off to TOOL-dTrueNorth-20, promoted by the
  round-2 spec audit, the mirror of its consumes-from; no other section moves.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "read the roster a run started with from the authored
roster when the generated units region is empty"` and `python tools/codebase-map/reuse_lookup.py
"carry a deferred unit forward to the next run of the same build once"` both ranked name-stem
neighbours and scanned every layer. The first surfaced `baseline_units`, `region` and
`extract_run_facts` in `tools/unattended/lib-unattended.sh`. That is the seam S2 extends, at
`lib-unattended.sh:1953-2020`, and its three callers take the change unedited. The second found no
seam for the spec-run test or the once-witness. Those extend `check_carry_forward`
(`unattended.sh:5156-5248`) with readers it already uses: `asks_filed_by`, `backlog_blob_of`,
`run_ask_witness` and `ask_field`, the `:5187` row pattern, and the archive grammar of
`archive_name_of` and `check_honest_rotation`. S1 copies `pinned_units`' refusal shape and
`roster_ids`' slug scope. `check_prompt_brief`'s read at `unattended.sh:3795` is the prior instance of
S1 and is left unrouted (F7). A hit that disagreed with source: TOOL-dUnstuckLanding-18's §4 places
`baseline_units` at `lib-unattended.sh:1277`, and the plan at `:1950-2018`, where base reads
`:1953-2020`. The recall probe returned this build's brief, the plan's red case 5, the plan review's
H1 (`reviews/2026-10-20-review-PLAY-dClosedLoop-1-execution-plan-b.md:38-44`), fold-a's id 5 (a
whole run reading as a spec run) and id 7 (an aborted record as a witness), fold-b's M5 (the plant
follows rule 1 in full), TOOL-dUnstuckLanding-18's spec, and ask `TOOL-aRoutedQuill-13`, which §3
leaves out. The bug-class probe over the touched paths selected `format-derived-from-arity` and
`two-guards-one-question-two-answers`, which §4 answers.

Recall terms used: carry-forward DEFERRED baseline_units roster:units gen:build-units spec run added unit rescope defer once rotated

The question passed with them: "may a spec run carry forward a deferred unit it added, and how is
the starting roster read when no spec exists".
