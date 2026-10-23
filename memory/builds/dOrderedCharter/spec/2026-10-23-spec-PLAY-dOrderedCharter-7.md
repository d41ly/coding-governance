# PLAY-dOrderedCharter-7 — the core: principle registry, meta-check, kinds register, exception register and the core policies

**Status:** OPEN · rev-3 · 2026-10-24 · node d · Tier-2 · base ce13efbe · streams playbook · order 11 · advances PLAY-dOrderedCharter-38

**Carries:** cl-dClosedLoop-0037@0b2c8bff whole

**Carries:** node:policy-key.core.bypass

**Carries:** node:policy-key.core.exceptions

**Carries:** node:record-kind.exception

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return-2.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return-2.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-b.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-b.md) | research | PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-28 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-build-PLAY-dOrderedCharter-7-deviation-71.md](../build/2026-10-23-build-PLAY-dOrderedCharter-7-deviation-71.md) | deviation | — |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-edge-fix-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-edge-fix-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md](../reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md) | spec-audit | PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-37 |

<!-- /gen:spec-records -->

## 1. Goal

No principle declares its enforcement today: 22 of the charter's 36 practices are cited by no code file
and none of the 142 rows of `tools/gate-legs.json` names a principle (gap-found-07), and factories exist for
3 of 13 extension kinds (gap-found-08). P16 says the core cannot be built around. This unit builds the core
the foundations record places in this build (foundations, "Settled design for the core"): the principle
registry, the meta-check joining it both ways to the checks that enforce it, the kinds register with each
kind's owning build, the conformance-gate contract, the typed build-folder record factory and its
exception kind, the exception register, the `core.*` policies, and the factories and gates of the kinds this
build owns.

## 2. Scope (IN)

- **S1** — The principle registry, `tools/playbook/principles.toml`: one `[[principle]]` row per v2
  principle, `P1` to `P42`, with `tag` (`principle.p<n>`, the `principle` namespace unit 10 registers),
  `id` (`P<n>`), `line` (its bold title, one line) and `clauses` (its v2 `[enforcement]` row). The rows
  are written once from v2's `[principles]` and `[enforcement]` and are the namespace's declaring source.
  Principles are fixed: no policy key reads or writes a row. Observed by AC1.
- **S2** — The `enforces` key. A row of `tools/gate-legs.json` may carry `"enforces": [<tag>, …]`, each a
  `principle.*` or `practice.*` tag. This unit's own legs carry it, and unit 16's layer gate leg gains
  `["principle.p28", "principle.p16"]`. Observed by AC2.
- **S3** — The meta-check, `python tools/playbook/core.py meta-check`, joined both ways through S2's join
  factory (`compute_coverage`, carried inline as its canonical copy under the `PARITY_ROWS` row unit 19
  adds): a principle no leg's `enforces` and no kind's `binds` names is red; an `enforces` or `binds` tag no
  registry row holds is red; a leg carrying no `enforces` is red. Each red is excused only by a row of the
  shrink-only pending list `tools/playbook/core-pending.txt`, keyed `principle`, `practice` or `leg` and
  the name, with the build that arms it; a pending row whose item is now enforced is red as stale. The
  practice population is the rows of `tools/playbook/practices.toml` (S15), `unarmed` until unit 1 writes
  it. Every run prints each pending count. Observed by AC2 and AC3.
- **S4** — The kinds register, `tools/playbook/kinds.toml`: one `[[kind]]` row for each of the seventeen
  kinds of foundations C3, with `tag` (`kind.<name>`), `owner` (the chain build that lands its factory, as
  the foundations record assigns it), `binds` (principle tags), `population` (a tracked-path glob or a
  reader command), `factory` and `gate`. A kind whose factory or gate has not landed is a `kind` row of the
  pending list naming its owner; the register is the `kind` namespace's declaring source, so a `kind.*` tag
  the register lacks fails unit 19's resolver. Observed by AC4.
- **S5** — The conformance-gate contract, checked by `core.py kinds`: a kind row out of the pending list
  names a `factory` command that exists and a `gate` leg of `tools/gate-legs.json` whose `enforces` holds
  every tag of the kind's `binds`. The gate reads the kind's whole population both ways and is seen red
  on a planted instance before it is trusted, which its unit records as a `New arm:` line. Observed by AC4.
- **S6** — The factories and gates of this unit's two kinds, through one verb,
  `python tools/playbook/core.py new <kind> <name> …`, which runs the kind row's `factory`:
  - **Skill**: `new skill <name> --description <text>` writes `skills/<name>/SKILL.md` with front matter
    `name` and `description`; the gate `core skills conformance` reds a `skills/*/` directory whose
    `SKILL.md` is missing, whose `name` differs from its directory or breaks `seg`, or whose `description`
    is empty or over 1024 characters;
  - **practice**: `new practice <name> --line <text>` appends a `[[practice]]` row to
    `tools/playbook/practices.toml` (S15), `tag` `practice.<name>`; the gate `core practices conformance`
    reds a row whose tag is outside the `practice` namespace or repeats, or whose `line` is not one line of
    at most 200 bytes, and reads `unarmed` until unit 1 writes the catalogue.
  The layer kind is registered with unit 16's factory and gate; the instruction-unit kind's factory and
  gate land with unit 20 (deviation 71). Observed by AC5 and AC6.
- **S7** — The typed build-folder record factory (S12), `tools/memory-tree/build_records.py`, extracted
  from `tools/memory-tree/deviation_join.py` at this, its second instance: the name grammar
  `<date>-build-<unit id>-<kind>-<n>.md` in a build's `build/` folder, the `**Key:**` field regex
  (`FIELD`), each kind's required fields and closed sets, `read_record`'s duplicate, missing and
  closed-set refusals, the tracked population and the `<n>` collision. `deviation_join.py` imports it and
  keeps its deviation-only rules (the `**After:**` pipe, `DEPARTS`, `FOLLOW`, `**Supersedes:**`), its
  verdicts unchanged, and `tools/memory-tree/check-verdict-epoch.sh`'s `DELEGATES` gains the new module,
  whose import closure that script grades. Observed by AC7.
- **S8** — The exception record kind and its stand-in door. `python tools/memory-tree/build_records.py new
  exception --build <slug> --unit <id> --principle <tag> --excuses <part> --reason <text> [--expires
  <date>]` writes `<date>-build-<unit id>-exception-<n>.md` in the build's `build/` folder of the
  session's own tree, with `**Serves:** exception <unit id>` and the fields `Principle`, `Excuses`,
  `Reason`, `Expires` (optional) and `Caused-by`, for the recording session's commit. It is the stand-in
  door memory-plan `[doors]` lists until dTotalRecall's record door adopts it. Observed by AC8.
- **S9** — The exception register and `core.exceptions`, read by `core.py exceptions` and by every core
  gate: a red whose principle and part match an admitted record prints as `excepted`, naming the record.
  `any-session-recorded`, the default, admits every well-formed record; `owner-only-expiring` admits one
  that carries `**Expires:**` in the future and was written through the door's owner path, the TTY proof
  of dGroundRules' minimal guard (`cl-dClosedLoop-0012`), and reds an expired one or one without the
  field; `none` admits none and reds every record. Observed by AC8 and AC9.
- **S10** — `core.bypass`. `with-hooks-report`, the default, and `with-hooks-block` let a bypass skip the
  core legs with every other leg; `never` makes the meta-check red any leg whose `enforces` is non-empty and
  which carries a `guard`, so no leg guard can skip a core check. Both keys are read through dGroundRules'
  one reader (`cl-dClosedLoop-0008`) once it lands, and until then with v2's catalogue defaults,
  `with-hooks-report` and `any-session-recorded` (v2:1144-1145). Observed by AC10.
- **S11** — The legs and plants. Legs `core meta-check`, `core kinds`, `core skills conformance` and `core
  practices conformance` in `tools/gate-legs.json`, each carrying `enforces`, and one `core selftest` leg;
  `python tools/playbook/core.py fixture --plant <case>` builds a throwaway repository in the system temp
  directory with its own registry, legs, records and `.governance/policy.toml`, and runs the case. Observed
  by AC1 to AC10.

## 3. Non-goals (OUT)

- The charter's core block rendered from the registry: unit 2 (`cl-dClosedLoop-0032`).
- The factories and gates of kinds other builds own (command, policy key, preset, stage, hook, role,
  workflow, item and scenario in dDeclaredLoop; gate leg in dWitnessedBar; kit in dShippedRelease; record
  kind in dConvergedCharter; lens in dCalibratedLens): each sits on the pending list naming its build.
- The report-after and block-after handling of a core red a bypass let land, and the run of the core legs
  on the landed tree: dShippedRelease's lander (foundations, "Confirmed, 2026-10-15"). This unit reads
  `core.bypass` where a leg guard could skip a core check.
- The one-door check and its door list: unit 29 (`cl-dClosedLoop-0059`). This unit names its stand-in door.
- The override and change record kinds: units 2 and 15, each a kind of S7's factory.
- The Loop Review's audit of the register: a later build reads `core.py exceptions`.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-19` — the join factory `compute_coverage` and its `PARITY_ROWS` row, the resolver and the `tags` pack
- **consumes-from** `PLAY-dOrderedCharter-10` — the `principle`, `practice` and `kind` namespaces and the tag shape check S1 and S4 write under
- **consumes-from** `PLAY-dOrderedCharter-16` — the layer kind's factory and gate leg, which S4 registers and S2 marks
- **hands-off** `PLAY-dOrderedCharter-20` — the instruction-unit kind's factory and gate, registered here as pending
- **hands-off** `PLAY-dOrderedCharter-1` — the practice catalogue's rows, which arm S6's practice gate and S3's practice population
- **hands-off** `PLAY-dOrderedCharter-29` — the exception door, added to the one-door check's list, and the `enforces` key and the meta-check that grades its pairings both ways
- **hands-off** `PLAY-dOrderedCharter-2` — the principle registry the charter's core block renders from, and S7's factory the override kind joins
- **hands-off** `PLAY-dOrderedCharter-15` — S7's factory the change record kind joins
- **hands-off** `PLAY-dOrderedCharter-35` — the kinds register a row kind's schema is found through
- **hands-off** `PLAY-dOrderedCharter-36` — the kinds register's optional `schema` key, and the principle registry its `principle=` sources resolve against
- **hands-off** `PLAY-dOrderedCharter-30` — the `enforces` key, the meta-check and the pending list its rule-to-leg pairs live in
- **hands-off** `PLAY-dOrderedCharter-32` — the principle registry a `principle.` unit's fixed class reads
- **hands-off** `PLAY-dOrderedCharter-37` — the kinds register's rows its reference pages render
- **hands-off** `PLAY-dOrderedCharter-12` — the `enforces` key the grammar leg carries
- **hands-off** `PLAY-dOrderedCharter-13` — the `enforces` key the ladder leg carries, and the meta-check that joins it
- **consumes-from** external — dGroundRules' one policy reader (`cl-dClosedLoop-0008`) and its minimal guard's TTY proof (`cl-dClosedLoop-0012`), landed by the chain before this build run
- **hands-off** external — dShippedRelease runs the core legs on the landed tree and acts on a bypassed red as `core.bypass` says; dTotalRecall's record door adopts the exception door
- **hands-off** `PLAY-dOrderedCharter-42` — the three typed record kinds admitted by the bindings reader and joined to their file names, and the factory's kind list made the reader's (finding 31)
- **hands-off** `PLAY-dOrderedCharter-49` — the round-1 spec audit's minors on this spec, findings 4, 5, 40, 61, 66, 67 and 85, which that batch unit corrects after this unit lands, each by the item its report id names
- **consumes-from** `PLAY-dOrderedCharter-50` — `enforces` already in both canary key sets at order 10, and the owed-rows probe: this pass runs `python tools/run-gates/owed_rows.py --base HEAD` before its commit and writes every row it names in that commit (round-2 id 23)

## 4. Design

### Data model

```toml
# tools/playbook/principles.toml
[[principle]]
tag = "principle.p16"
id = "P16"
line = "The core cannot be built around."
clauses = ["cl-dClosedLoop-0037", "cl-dClosedLoop-0091", "cl-dClosedLoop-0212", "cl-dClosedLoop-0349", "cl-dClosedLoop-0480"]

# tools/playbook/kinds.toml
[[kind]]
tag = "kind.skill"
owner = "dOrderedCharter"
binds = ["principle.p16"]
population = "skills/*/SKILL.md"
factory = "python {prefix}/playbook/core.py new skill"
gate = "core skills conformance"
```

```
core-pending.txt row := <principle|practice|leg|kind> <TAB> <name> <TAB> <arming build>
exception record     := - **Principle:** <tag> · - **Excuses:** <part> · - **Reason:** <text>
                        [· - **Expires:** <YYYY-MM-DD>] · - **Caused-by:** <id>
```

### Inventory

Minted: the files `tools/playbook/principles.toml`, `tools/playbook/kinds.toml`,
`tools/playbook/core-pending.txt`, `tools/playbook/core.py` (verbs `meta-check`, `kinds`, `new`,
`exceptions`, `fixture`) and `tools/memory-tree/build_records.py` (verbs `new`, `read`); the leg key
`enforces`; the record kind `exception`; the legs `core meta-check`, `core kinds`, `core skills
conformance`, `core practices conformance` and `core selftest`. The pending list's seed is DERIVED at the
build pass by the meta-check over the tree; at `4e8f80cdf` it would hold 142 `leg` rows and the 40
principles no landed leg enforces (PINNED, 2026-10-23).

### Migration

`deviation_join.py` moves onto S7's factory with its verdicts unchanged; its suite re-observes it. The
pending list is written once at the build pass and only shrinks after.

### Rollout

Live at landing, at order 11: after units 10 (order 5), 16 (order 2) and 19 (order 4), and before units 20
(order 15) and 1 (order 17), whose populations arm S3 and S6 when they land.

### Files touched (estimate)

- `tools/playbook/core.py`
- `tools/playbook/principles.toml`
- `tools/playbook/kinds.toml`
- `tools/playbook/core-pending.txt`
- `tools/memory-tree/build_records.py`
- `tools/memory-tree/deviation_join.py`
- `tools/memory-tree/check-verdict-epoch.sh`
- `tools/gate-legs.json`

### Alternatives rejected

- **`binds` on the principle rows.** C3 lists, per kind, the principles that bind it; one fact in one
  place puts it on the kind row and derives the principle's view.
- **A new `chunk` value for core legs.** `chunk` groups the runner's scheduling; whether a leg is core is
  the fact `enforces` already states.
- **A fourth record reader copied from `deviation_join.py`.** The `[reuse]` rule extracts at the second
  instance, and units 2 and 15 bring the third and fourth.

## 5. Production-readiness checklist

- security: principles are fixed and no key reads them; `core.exceptions: owner-only-expiring` reuses the
  minimal guard's TTY proof; the door writes only under the session's own `build/` folder.
- perf / scale: one TOML read per registry and one JSON read of the legs; the join is set arithmetic.
- error / empty / loading states: an absent registry or legs file is red; the practice population reads
  `unarmed`, never green; each pending count prints on every run.
- observability: every red names the principle, kind or leg, the remedy and the build that arms a pending
  row.
- risks: a hand-written exception record bypasses the door until unit 29's one-door check reads it; an
  `owner-only-expiring` record is only as owner-written as the door's proof.
- testing: S11's plants both ways; `deviation_join.py`'s suite over the extracted factory.
- migration: §4 Migration.
- user docs: N/A — unit 37 renders the kinds register's and the principle registry's pages.

## 6. Acceptance criteria

- **AC1** — When `python core.py fixture --plant registry` runs, the registry's `id` set
  equals the `P<n>` heads of the fixture's design `[principles]` both ways, and a planted extra `P43` row
  and a planted missing `P7` row each exit 1 naming it.
  Red when: the registry drifts from v2's principle set.
- **AC2** — When `python core.py fixture --plant unenforced` runs, a principle no leg and no
  kind names, and not on the pending list, reds `meta-check`, as does an `enforces` naming
  `principle.p99`; both pass with the principle's enforcing leg restored.
  Red when: a principle nothing enforces passes.
- **AC3** — When `python core.py fixture --plant pending` runs, a leg with no `enforces` and
  no pending row reds `meta-check`, a pending row for an enforced principle reds as stale, and the run prints
  each pending count.
  Red when: the pending list hides an enforced item or grows silently.
- **AC4** — When `python core.py fixture --plant kinds` runs, `core.py kinds` reds a kind row
  whose `gate` names no leg, a gate leg whose `enforces` lacks a tag of the kind's `binds`, and a
  `kind.widget` tag that no register row holds.
  Red when: a kind conforms without a gate that enforces its principles.
- **AC5** — When `python core.py fixture --plant skill` runs, `new skill demo --description x`
  writes a `SKILL.md` the gate passes, and a planted Skill with an empty `description`, and one whose `name`
  differs from its directory, each red `core skills conformance`.
  Red when: the factory's output fails its gate, or a broken Skill passes.
- **AC6** — When `python core.py fixture --plant practice` runs, `new practice demo --line x`
  appends a row the gate passes, a two-line `line` and a repeated tag each red it, and with no catalogue the
  gate prints `unarmed`.
  Red when: a malformed practice passes, or an absent catalogue reads as green.
- **AC7** — When `python tools/memory-tree/deviation_join.py --fixture --plant malformed-field`, then
  `--plant duplicate-n` and `--plant pipe-after`, run, each prints the verdict it printed before the
  extraction; `git grep -n "^FIELD = " -- tools/memory-tree/` prints one definition, in
  `build_records.py`; and `check-verdict-epoch.sh`'s `DELEGATES` names `build_records.py`.
  Red when: a second field grammar survives, a deviation verdict moves, or the import closure misses the
  new module.
- **AC8** — When `python core.py fixture --plant exception` runs, `build_records.py new
  exception` writes `<date>-build-<unit>-exception-1.md` with every field, the excused red prints
  `excepted` naming it, and a record missing `Reason` is red.
  Red when: an exception excuses without its principle, part and reason.
- **AC9** — When `python core.py fixture --plant exceptions-values` runs, a record with no
  `Expires` reds under `owner-only-expiring`, an expired one reds, a record written without the TTY proof is
  not admitted, and under `none` every record reds and excuses nothing.
  Red when: a value admits what it refuses.
- **AC10** — When `python core.py fixture --plant bypass-never` runs, a core leg carrying a
  `guard` reds `meta-check` under `core.bypass` `never`, and passes under `with-hooks-report`.
  Red when: `never` lets a guard skip a core leg.

## 7. Gates

`playbook render selftest` · `govkit acceptance matrix` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/core.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC8 AC9 AC10 · the `core selftest` leg runs every `fixture --plant` case, each failing case staged by its plant · none

New arm: tools/memory-tree/deviation_join.py · covers AC7 · its existing suite re-run over the extracted factory, its failing case a record missing a required field · none

## 8. Open questions

- **F1** — Which unit builds the instruction-unit kind's factory and gate, given the clause lists it here and
  its row schema (S10) and schema check land with units 9 and 20, after this unit?
  RESOLVED (agent, 2026-10-23, delegated): rung 1 read with the foundations record: "A factory per
  extension kind, each landing with the build that defines that kind's conformance gate". Unit 20 builds
  that gate, so its factory lands there and this unit registers the kind as pending. Recorded as
  deviation 71 (`memory/builds/dOrderedCharter/build/2026-10-23-build-PLAY-dOrderedCharter-7-deviation-71.md`).
- **F2** — Where is `core.bypass` read, given a `--no-verify` push runs no hook to read it and the
  after-landing handling is dShippedRelease's lander?
  RESOLVED (agent, 2026-10-23, delegated): rung 3, the most feature-rich survivor inside this build: the
  meta-check reads it and, under `never`, reds a core leg carrying a `guard` (S10), so the key has a
  consuming reader as `cl-dClosedLoop-0014` requires once this build lands. Editing the runner to ignore
  guards was rejected: it puts a cross-kit call from run-gates into this kit, an edge unit 16's check reds.
- **F3** — Where do the registries live? Options: `tools/playbook/`; `tools/memory-tree/`.
  RESOLVED (agent, 2026-10-23, delegated): rung 1: the brief's S4 places the instruction layer's modules in
  `tools/playbook/` (systems `[design-tags]` Owners), and the core's registries are namespaces' declaring
  sources there; the record factory stays in the record kit, `tools/memory-tree/`, as S12 says.

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the spec run's carrier of `cl-dClosedLoop-0037`.
- rev-2 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-1 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-42, PLAY-dOrderedCharter-49.
- rev-3 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-2 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-50.

## 10. Reuse audit

The seams extended are `tools/gate-legs.json`'s row grammar (a new `enforces` key beside `name`, `argv`,
`guard`, `chunk`, `subject` and `ceiling`), unit 19's `compute_coverage` (today
`tools/codebase-map/map_lib.py:1404`) through the `PARITY_ROWS` table of
`tools/lib/resolve-python.test.sh`, and the deviation record reader of
`tools/memory-tree/deviation_join.py` (`FIELD` at :145, `RECORD_NAME` at :160, `read_record` at :212,
`read_records` at :268), which S7 extracts. `python tools/codebase-map/reuse_lookup.py "refuse a principle
that no gate leg names as what it enforces"` ranked name-token matches (`legs`, `leg`, `CensusRefused`) and
no registry or meta-check, so no existing seam fits those; scout B found the same by text search. The scout's
note that govkit's `kind = "authoring"` means something else was confirmed at `tools/playbook/kit.toml`,
whose `kind = "dir"` is an install shape, so the kinds register reuses neither.

Recall terms used: `python tools/memory-recall/query.py "how is a principle joined to the checks that enforce it and how is an exception to a principle recorded" --terms "principle registry meta-check enforces kinds register factory conformance gate exception register core.exceptions core.bypass deviation record"`
