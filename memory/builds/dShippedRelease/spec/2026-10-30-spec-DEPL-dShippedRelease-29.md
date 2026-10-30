# DEPL-dShippedRelease-29 — the update's report over every kind: each row's state, every repository row, every widening, and a lost change told from an unrelated hole

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 24 · advances DEPL-dShippedRelease-32

**Carries:** cl-dClosedLoop-0439@1aecad6a whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-7-reuse-scout-d.md](../build/2026-10-30-build-DEPL-dShippedRelease-7-reuse-scout-d.md) | research | DEPL-dShippedRelease-7 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-20 DEPL-dShippedRelease-25 DEPL-dShippedRelease-28 DEPL-dShippedRelease-31 |
| [2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md](../prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |

<!-- /gen:spec-records -->

## 1. Goal

`gap-deploy-28`: no update line names an adopter's role, overlay or leg, or a restored gov leg, and an
update exits 1 on unrelated holes, so an adopter cannot tell a lost change from the exit code. This unit
extends the update's report to every registered kind: each gov row's state, every repository row, every
widening compared with the classifier, and every new gov row upstream of a repository item, and it gives
a lost change its own line and its own exit code. It owns no node; it reads `item.kits.update`.

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build, each specced and unbuilt at base `f4597719`:
`render_delta_report` and the relay (PLAY-dOrderedCharter-34 S6); `compose_rows` and its five returns,
the six states, the fixture kind (PLAY-dOrderedCharter-35 S1, S9, S11); `classify_patch`,
`derive_widenings`, `read_kind_schema` and the `ref` role `needs` (PLAY-dOrderedCharter-36 S1, S5, S6);
`tools/playbook/kinds.toml` and its `schema` key (PLAY-dOrderedCharter-35 S10); the `compose` verb and
`compose_at` (TOOL-dDeclaredLoop-26 §8 F4, F5); the restored leg's line (TOOL-dWitnessedBar-28 S9).

- **S1** — The report, I19. `derive_kit_report(rows, states, prior_tags, schemas)` in
  `tools/playbook/render_playbook.py` returns one row per line in the order of §4 "The report", and
  `render_delta_report` prints from it, so one function holds what the report says. It covers every
  kind whose `[[kind]]` row in `tools/playbook/kinds.toml` names a `schema`, read from the register and
  never typed, each through `overlay_rows.py compose`. A kind with no overlay rows still prints each gov
  row's state. Observed by AC1.
- **S2** — Every repository row, of every kind: one line under the state word `repository`, naming its
  kind, tag and edge. PLAY-dOrderedCharter-34 S6 prints repository units; this adds the rows. Observed
  by AC2.
- **S3** — Every new gov row upstream of a repository item, `derive_upstream_new_rows(rows, prior_tags,
  schemas)`: the rows whose tag `prior_tags` lacks and that a repository item reaches over every field
  whose `ref` role is `needs`, each printed under the state word `review`, naming the repository item.
  `prior_tags` is the composition's tag set at the target's `HEAD`, read through `compose_at` before the
  update's staged writes land, since `HEAD` still holds the prior release. Observed by AC3.
- **S4** — The widening comparison, `check_report_widenings(lines, rows)`: it runs `classify_patch` over
  every `amends` patch of the composition, the release's patches, one at a time, and compares the set of
  `(row, field, op)` read `widens` with the report's `widening` lines, both ways. A difference prints
  `report — missing widening <row> <field> <op>`, or `invented`, and refuses the render, exit 1. The
  comparison reaches the classifier directly and does not read `derive_widenings`' list, which is what
  the report printed, so a filter in the printing path cannot pass it. Observed by AC4.
- **S5** — A lost change. `derive_lost_changes(states, held, restored)` returns one row per change this
  update took from the repository: a row whose state is `orphaned`, a patch `compose_rows` held, and a
  gov leg TOOL-dWitnessedBar-28 S9 restored. Each prints under the state word `lost`, with `update`'s
  relay naming why. Holes, undischarged probes and red checks keep their own lines and are never `lost`.
  Observed by AC5.
- **S6** — The exit. `_cmd_update` exits 3 when any `lost` line printed and no refusal stopped the run, so
  `update`'s exits read 0 clean, 1 findings, 2 refused, 3 a change was lost, the finding lines still
  printed. USAGE states the four. `KIT_WALK_OUTCOMES` (DEPL-dShippedRelease-17 S1) gains `lost-change`,
  routed to `end`. Observed by AC5 and AC6.
- **S7** — The relay. The word list of the relay in `_cmd_update` (PLAY-dOrderedCharter-34 §4) gains
  `repository`, `review` and `lost`, so `update` prints every line under its `govkit update — composition`
  heading, and one tally of each word, zeros included. Observed by AC2.
- **S8** — The page `help/overlay-rows.md` gains a section "Reading the update's report": each word,
  what to do about `review` and `lost`, and exit 3; `WIRE-INTO-PROJECT.md`'s update section names the
  four exits. Observed by AC7.

## 3. Non-goals (OUT)

- The six states, the classifier and the widening list: PLAY-dOrderedCharter-35 and -36.
- The offer's order: DEPL-dShippedRelease-16. `kits.offer` refuses the playbook regenerate, so an
  offered update prints no report, and the adopter's own attended `update` does.
- Refusing a widening: this unit reports. A patch's refusal is PLAY-dOrderedCharter-36's.
- Versioning a record kind whose output's meaning changed: TOOL-dDeclaredLoop-24 §4.

### Edges

- **consumes-from** `DEPL-dShippedRelease-17` — `kits.update`, whose run prints this report, and `KIT_WALK_OUTCOMES`, which gains one word
- **consumes-from** external — PLAY-dOrderedCharter-34, -35 and -36, TOOL-dDeclaredLoop-26, TOOL-dWitnessedBar-28, each specced and unbuilt at base `f4597719`

## 4. Design

### Evidence

Read at `5d1c82ac0`; no product file differs from base `f4597719`.

- The tally is at `tools/govkit/govkit.py:10033`, the verdict-line width at `:10010`, and
  `Report.emit` returns 1 on any problem (`:1641-1649`), which is why a hole and a lost change read alike.
- `update` runs the playbook-render regenerate through `run_target_argv` (`:11363`), and PLAY-dOrderedCharter-34
  §4 relays the regenerate's stdout lines whose state word it knows, so this unit extends that word list
  and adds no spawn.
- `compose_rows` returns `(rows, states, held, stale, orders)` (PLAY-dOrderedCharter-35 §4), as data.
- `row_kind.py` is PLAY-dOrderedCharter-35 S11's fixture kind, one set field, one constraint set field and
  one ordered scalar, which is exactly the three directions the clause names.
- The composition reads `HEAD` (PLAY-dOrderedCharter-46 S1), and `update --write` stages and never commits,
  so inside a run `HEAD` is the prior release's overlay and kit files, and `compose_at` reads that.

### The report

```text
  unchanged          [gov:loop     ] item.build.pass
  amended            [repository   ] leg.govkit.selftest
  excluded           [gov:roles    ] role.scout
  repository         [repository   ] leg.adopter.lint-sql
  widening           [repository   ] role.gov-builder gates add leg.foo (gov: none)
  review             [gov:loop     ] item.build.new-gate · upstream of item.build.adopter.deploy-preview
  lost               [repository   ] leg.govkit.selftest · patch orphaned, its gov row ended
  composition        unchanged 41 · amended 1 · replaced 0 · excluded 1 · stale 0 · orphaned 0 · repository 3 · widening 1 · review 1 · lost 1
```

Order: the six states by kind then tag, `repository`, `widening`, `review`, `lost`, the tally last, in
`cmd_update`'s `{v:<18} [{role:<13}] {path}` widths.

### Inventory

Minted: `derive_kit_report`, `derive_upstream_new_rows`, `derive_lost_changes`, `check_report_widenings`
in `tools/playbook/render_playbook.py`; the fixture `tools/playbook/fixtures/update_report.py`; the state
words `repository`, `review`, `lost`; the exit code 3 of `update`; the outcome word `lost-change`. Naming
cell `py.function`: each OK by `python tools/lexicon/lexicon.py --suggest <name> --as py.function` at
`5d1c82ac` (`classify_lost_changes` was asked first and refused).

### Migration

Additive, but for one contract: a caller reading `update`'s exit 1 as "something is wrong" now also
meets 3. `tools/govkit/offer.py` reads exit 0 or not, and its mode prints no report, so it never sees 3.

### Rollout

Live at the first `update` after the landing. The tally prints zeros on a tree with no overlay.

### Files touched (estimate)

- `tools/playbook/render_playbook.py`: S1 to S5
- `tools/playbook/fixtures/update_report.py` (new), `tools/playbook/adopt-playbook.sh`: the plants
- `tools/playbook/kit.toml`: the fixture's row
- `tools/govkit/govkit.py`: S6, S7, USAGE
- `tools/govkit/kit_walk.py`: `lost-change`
- `tools/govkit/selftest.py`: the exit contract
- `tools/loop/loop.toml`: `item.kits.update`'s `lost-change` route
- `help/overlay-rows.md`, `WIRE-INTO-PROJECT.md`: S8

### Alternatives rejected

- **Comparing the report with `derive_widenings`.** PLAY-dOrderedCharter-36 S6 makes that list the
  report's one source, so the comparison could not fail on a list-level bug: rejected by the rule that a
  gate needs a case it can see, in favour of `classify_patch` over the patches.
- **A line and no new exit.** Rejected by `gap-deploy-28`'s own words, "from the exit code".
- **Printing from gov's process.** `update` would parse the target's overlay in gov's process; the
  relay already carries the target's composed answer.
- **A separate `kit_report.py`.** `render_delta_report` is the function PLAY-dOrderedCharter-34 S6 names,
  and splitting its lines across two modules gains no reader.

## 5. Production-readiness checklist

- security — read-only over the composition; `compose_at` runs the prior pin's code in a scratch worktree
  of the adopter's own repository, in an attended `update` only.
- perf / scale — one compose per registered kind plus one at `HEAD`, each a subprocess on a small overlay.
- error / empty / loading states — a tree with no overlay prints every gov row `unchanged` and the tally
  with zeros; an empty kind list refuses, since a report over no kind is an empty population.
- observability — the tally line prints every word, zeros included.
- risks — a large gov release prints many `unchanged` lines; `update` already prints one per file row.
  Exit 3 is a new value for any script an adopter wrapped around `update`, which S8 states.
- testing — the arms of §7, each a planted release over the fixture kind.
- migration — §4 "Migration".
- user docs — `help/overlay-rows.md`, `WIRE-INTO-PROJECT.md`.

## 6. Acceptance criteria

- **AC1** — When `python update_report.py --plant states` runs over a planted release holding one gov row
  in each of `unchanged`, `amended`, `replaced`, `excluded`, `stale` and `orphaned`, the report prints each
  row under its word, the tally holds a `1` for each, and with a second registered kind planted its
  rows print with no code change.
  Red when: a state is missing, or a kind is typed rather than read from `kinds.toml`.
- **AC2** — When `--plant repository-rows` runs with one repository row of each of two kinds, each prints
  under `repository` naming its kind and tag, and `python tools/govkit/govkit.py update --target <a fixture>
  --write` relays them under its `composition` heading.
  Red when: a repository row is unreported, or the relay drops the word.
- **AC3** — When `--plant upstream-new` adds a gov row that a repository item reaches through two `needs`
  edges, and a second new gov row nothing reaches, the first prints under `review` naming the repository
  item and the second does not.
  Red when: an upstream row is missed through the transitive edge, or an unrelated row is listed.
- **AC4** — When `--plant drop-add`, `drop-remove` and `drop-raise` each run a release whose report drops
  one widening, an `add` to a permission set, a `remove` from a constraint set and a raised scalar, each
  exits 1 printing `report — missing widening` with that row, field and op; when `--plant all-three`
  runs the report naming all three, it exits 0.
  Red when: a missing widening of any direction passes, or the green case reds.
  fixture: each `drop-*` stubs the report's printing path, never the classifier.
- **AC5** — When `--plant lost-orphaned` runs an update whose release ends a gov row a repository patch
  names, `--plant lost-restored` restores a deleted gov leg, and `--plant unrelated-hole` plants only an
  undischarged hole, the first two print a `lost` line and exit 3, and the third prints no `lost` line
  and exits 1.
  Red when: an unrelated hole reads as lost, or a lost change exits 1, the `gap-deploy-28` case.
- **AC6** — When `python kit_walk.py --fixture --plant outcome-lost-change` runs, the last line reads
  `outcome: lost-change`, and `python loop_lib.py --check` passes its route.
  Red when: a closed outcome set has no word for exit 3.
- **AC7** — When `grep -c "exit 3" overlay-rows.md` runs from the `help` directory it prints at least `1`.
  Red when: the new exit is undocumented.

## 7. Gates

`playbook render selftest` · `govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `recall floor arms` · `policy fixtures` · `memory hygiene`

New arm: tools/playbook/adopt-playbook.sh · covers AC1 AC2 AC3 AC4 AC5 · the playbook-render selftest runs `update_report.py` under every plant, its failing case `drop-add` · none
New arm: tools/govkit/selftest.py · covers AC5 AC6 · `update`'s four exits over scratch targets, staged by a planted `lost` line with a hole beside it · none

## 8. Open questions

- **F1 — A new exit code, or a line alone?** Options: (a) a line, exit unchanged; (b) exit 3. `gap-deploy-28`
  asks that an adopter tell a lost change "from the exit code", and a wrapper script is the reader
  that matters. RESOLVED (agent, 2026-10-30, delegated): (b), rung 3. grants: PLAY-dClosedLoop-3 `update`'s
  exit 3. widens: none · relaxes: none
- **F2 — What counts as lost?** Options: (a) only an `orphaned` row; (b) `orphaned`, a held patch and a
  restored leg; (c) any repository row whose state moved. A held patch is a change that stopped applying,
  and a restored leg undoes the adopter's deletion, the two `gap-deploy-28` names; an `amended` row whose
  pin moved on an `editorial` record lost nothing. RESOLVED (agent, 2026-10-30, delegated): (b), rung 3.
  widens: none · relaxes: none
- **F3 — Where the composition at the prior release comes from.** Options: (a) `compose_at` at `HEAD`
  in the target; (b) gov's blobs at the receipt's `gov_commit`. (b) reads no overlay and no repository
  item, so it cannot answer "upstream of a repository item" alone. RESOLVED (agent, 2026-10-30,
  delegated): (a), rung 3. widens: none · relaxes: none
- **F4 — Is the report's order part of the contract?** PLAY-dOrderedCharter-34 §4 fixes the line's shape
  and not the sections' order. RESOLVED (agent, 2026-10-30, delegated): fixed as §4 "The report" states, rung
  3, so `lost` is the last thing before the tally. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, from the packet's Items 29, flow-roles-adoption item 16, `gap-deploy-28`,
  scout D's unit 29 row and the brief's I19.

## 10. Reuse audit

The seams extended are `render_delta_report` (PLAY-dOrderedCharter-34 S6), `classify_patch`
(PLAY-dOrderedCharter-36 S5) and the tally at `tools/govkit/govkit.py:10033`. `python
tools/codebase-map/reuse_lookup.py "update report of every row state and widening"` ranked name-stem
helpers (`rows`, `report`, `Report`) and the class `Report` (`tools/govkit/govkit.py:1630`), whose `emit`
is why two findings exit alike; no report over rows exists at HEAD. Scout D's unit 29 row holds, with one
correction: it names `derive_widenings` as the comparison's other side, and that list is the report's own
source, so S4 compares with `classify_patch`, the row of §4 "Alternatives rejected". Recall surfaced
flow-roles-adoption item 16 and `gap-deploy-28`'s register row.

Recall terms used: `python tools/memory-recall/query.py "how does an update report repository rows, widenings and a lost change" --terms "update report delta render_delta_report derive_widenings orphaned repository rows widening upstream needs lost change exit code"`
