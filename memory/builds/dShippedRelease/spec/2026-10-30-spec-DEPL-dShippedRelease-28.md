# DEPL-dShippedRelease-28 — `adopt.declarations`: today's flow and role customizations proposed as overlay rows, each ruled once

**Status:** OPEN · rev-2 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 23 · advances DEPL-dShippedRelease-32

**Carries:** cl-dClosedLoop-0438@088c545a whole
**Carries:** node:item.adopt.declarations

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |
| [2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-7-reuse-scout-d.md](../build/2026-10-30-build-DEPL-dShippedRelease-7-reuse-scout-d.md) | research | DEPL-dShippedRelease-7 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-20 DEPL-dShippedRelease-25 DEPL-dShippedRelease-29 DEPL-dShippedRelease-31 |
| [2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md](../prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md](../reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-10 DEPL-dShippedRelease-21 DEPL-dShippedRelease-23 DEPL-dShippedRelease-31 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-13 DEPL-dShippedRelease-4 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-6 DEPL-dShippedRelease-27 DEPL-dShippedRelease-5 DEPL-dShippedRelease-30 DEPL-dShippedRelease-3 DEPL-dShippedRelease-25 DEPL-dShippedRelease-7 DEPL-dShippedRelease-16 DEPL-dShippedRelease-20 DEPL-dShippedRelease-17 DEPL-dShippedRelease-29 DEPL-dShippedRelease-18 DEPL-dShippedRelease-24 DEPL-dShippedRelease-8 DEPL-dShippedRelease-26 DEPL-dShippedRelease-19 DEPL-dShippedRelease-22 DEPL-dShippedRelease-9 |

<!-- /gen:spec-records -->

## 1. Goal

An adopter that customized gov's flow and roles before the overlay existed holds those customizations
in files gov overwrites, or in shapes no composition reads: a hand-added manifest leg, a house file, the
run conf's extension vocabularies, its own role files. `adopt.declarations` proposes each one at install
and update, as the row or value it becomes, for the owner to rule once. A ruled proposal lands through
the overlay's door; a declined one is recorded as a drop; nothing is proposed twice.

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build, each specced and unbuilt at base
`f4597719`: the `core.py adopt` dispatcher, the `ruling` kind, the door `gov_record.py` and the owner
proof (TOOL-dLinkedLibrary-8 S1, S3, S5; PLAY-dOrderedCharter-15); `instructions_edit.py add --manifest
overlay`, its re-render through `--overlay-from` (PLAY-dOrderedCharter-15 S2, -46 S3, S4);
`read_overlay_rows`, `amends` and the schemas of each kind (PLAY-dOrderedCharter-35 S1, S3, S10);
`leg_factory.py --legacy-rows` and the `[[gate-leg]]` overlay row (TOOL-dWitnessedBar-28 S1, S7);
`[[role]]` and `[[workflow]]` overlay rows (TOOL-dBoundRoles-20 S2, S3); the three effort keys and
`read_policy_setting` (TOOL-dBoundRoles-21 S1, S2); `check_effort_floor` (TOOL-dBoundRoles-23 S5, S6);
`tools/loop/policy_edit.py set` (TOOL-dDeclaredLoop-2 S4); `item.<step>.adopter.<name>` overlay rows
(TOOL-dDeclaredLoop-24 S2); the item schema, `program = "adopt"` and the route `end`
(TOOL-dDeclaredLoop-12, TOOL-dLinkedLibrary-8 §8 F2, F5).

- **S1** — The verb, `python tools/playbook/core.py adopt declarations --build <slug> --unit <id>`,
  `declarations` an addition to the dispatcher's verbs (TOOL-dLinkedLibrary-8 S3 reserves only
  `instructions`), dispatched as a subprocess to a module of `core.py`'s own kit,
  `tools/playbook/adopt_declarations.py`, as TOOL-dLinkedLibrary-23 S1 dispatches its sibling. With no
  flag it scans (S2) and prints each unruled proposal: its key, its kind, the source it came from and
  the row or value it would write. Observed by AC1.
- **S2** — The scan, `scan_declarations(root)`, read-only, returning one proposal per customization over
  the five inputs of §4 "The inputs", through `derive_leg_proposals`, `derive_house_proposals`,
  `derive_conf_proposals` and `derive_role_proposals`. A proposal key is `<source>#<name>`, stable
  across runs, so a ruled key is never asked again. An input absent from the tree proposes nothing and
  prints one line naming it. Observed by AC1 to AC5.
- **S3** — The ruling, `--rule <key> accept|decline --reason <text>`, on the owner path
  TOOL-dLinkedLibrary-8 S5 uses, writes one `ruling` record through `gov_record.py new ruling` with
  `Subject` the key. A second ruling for one key exits 2 naming the first. Each proposal is one owner
  item, the item's route in §4 "The item". Observed by AC6.
- **S4** — `accept` applies, `write_ruled_proposal(proposal)`: an overlay row through
  `instructions_edit.py add --manifest overlay`, which validates the would-be tree and re-renders with
  `--overlay-from` so the render shows the row in the same command (PLAY-dOrderedCharter-46 S4); a
  `roles.effort.*` value through `python tools/loop/policy_edit.py set <key> <value>`, the guarded door.
  `decline` applies nothing and the ruling is the record. A write the door refuses leaves the ruling
  unwritten, naming the refusal. Observed by AC2, AC3 and AC6.
- **S5** — The floor. A house value below `medium` is proposed as it stands, marked `below-floor`, and
  accepted only under TOOL-dBoundRoles-23's owner authorization: `policy_edit.py set` at the owner's
  terminal, `policy-file.guard` at `owner-only`, which `check_effort_floor` reads. Under another guard
  value the proposal prints `held: policy-file.guard is <value>` and `accept` exits 2 naming the key.
  §8 F1. Observed by AC4.
- **S6** — The hook. `KIT_HOOKS` (DEPL-dShippedRelease-20 S2) already names `adopt declarations` for an
  update; this unit adds the same verb to the `install` rows, so `kits.install-attended` and
  `kits.update-attended` run it in the owner's session. Observed by AC7.
- **S7** — `[[item]]` `item.adopt.declarations` in `tools/loop/loop.toml`, §4 "The item", transcribed
  from `flow-steps.md:719`, `program = "adopt"`. Observed by AC8.
- **S8** — The page `help/adopt.md` (TOOL-dLinkedLibrary-8 S12) gains a section "Your own legs, roles and
  run vocabularies": what is proposed, what `below-floor` means, and how to rule. Observed by AC9.

## 3. Non-goals (OUT)

- Each row's schema, composition and refusals: their kinds' units. This unit proposes and calls doors.
- `core.py`, the `ruling` kind and the dispatcher: TOOL-dLinkedLibrary-8.
- Running itself: `kits.update-attended` runs it. It never runs under `kits.offer`.
- The report of what the overlay holds after an update: DEPL-dShippedRelease-29.
- Instruction files: TOOL-dLinkedLibrary-23's `adopt instructions`.
- Choosing a repository role's `shapes` or `budget` for the owner: a proposal carries what the role
  file declares, and a field it lacks is named for the owner to supply at `--rule`.

### Edges

- **consumes-from** `DEPL-dShippedRelease-17` — `kits.update`, whose attended hook runs this verb, and `kits.install`'s the same
- **consumes-from** external — TOOL-dLinkedLibrary-8, PLAY-dOrderedCharter-15, -35 and -46, TOOL-dWitnessedBar-28, TOOL-dBoundRoles-20, -21 and -23, TOOL-dDeclaredLoop-2, -12 and -24, each specced and unbuilt at base `f4597719`
- **hands-off** `DEPL-dShippedRelease-78` — the input count and the ruling's key, which the minors batch repairs (review ids 17, 109)

## 4. Design

### Evidence

Read at `5d1c82ac0`; no product file differs from base `f4597719`.

- `tools/roles/house/policy.toml` holds `[effort] default`, `[effort.roles]`, `[effort.stages.<workflow>]`
  and `[gates]`, read through `load_policy` (`tools/roles/roles_lib.py:398`); `EFFORT_LEVELS` is `:45`.
- `tools/unattended/.unattended.conf.example` declares the extension vocabularies `DIRECTIVES_EXTRA`
  (`:265`), `DIRECTIVES_EXTRA_TABLE` (`:270`), `PHASES_EXTRA` (`:366`), `DOD_EXTRA` (`:367`),
  `HALT_CODES_EXTRA` (`:373`) and `HOLD_CODES_EXTRA` (`:382`), each blank as shipped.
- `flow-roles-adoption.md` items 17 and 18 and `flow-steps.md:719` state the proposal and its routes.
- Witness classes are `history`, `hook-record` and `remote-verdict` (TOOL-dDeclaredLoop-5), and a
  computed witness is one read from a ref, a commit or a tracked file, the first class.
- The dispatcher reserves `instructions` only (TOOL-dLinkedLibrary-8 S3), so `declarations` adds a verb.

### The inputs

| Input | Read by | Proposed as | Door |
|---|---|---|---|
| a hand-added manifest leg | `leg_factory.py --legacy-rows` | a `[[gate-leg]]` row `leg.adopter.<name>`, `pack = "adopter"` | `instructions_edit.py add` |
| a leg's ceiling or argument override | a manifest row differing from gov's composed row in `ceiling` or `argv` | a `[[gate-leg]]` patch, `edges = ["amends=<gov leg tag>@<hash8>"]`, the changed field alone | `instructions_edit.py add` |
| the house file's efforts | `[effort.roles]`, `[effort.stages.*]`, each differing from the role's declared `effort` | `roles.effort.<slot>`, `roles.effort.<workflow>.<stage>` values | `policy_edit.py set` |
| the house file's `default` | `[effort] default` other than `medium` | a `roles.effort.default` value | `policy_edit.py set` |
| the house file's grants | `[gates]` rows naming a leg the role's `gates` field lacks | a `[[role]]` patch, `amends=role.<slot>@<hash8>`, `gates` with `add` | `instructions_edit.py add` |
| the run conf's vocabularies | each non-blank `*_EXTRA` term of `.unattended.conf` | an `[[item]]` row with a computed witness, §8 F2, or a drop | `instructions_edit.py add` |
| an adopter's role files | a `tools/roles/agents/*.agent.md` no receipt row names, with the `workflows.toml` entries naming its slot | a `[[role]]` row `role.adopter.<slug>` and its `[[workflow]]` rows `workflow.adopter.<name>` | `instructions_edit.py add` |

A value equal to gov's reading is no customization and proposes nothing: a `default` of `medium`, an
effort equal to the role's declared one, an `[effort.roles]` row gov's seed already holds.

### The item

```toml
[[item]]
tag = "item.adopt.declarations"
program = "adopt"
actor = "command:adopt.declarations"
needs = []
inputs = ["layer.distribution:the manifest, the house file, the run conf and the role files"]
allowance = "the overlay, the policy file and ruling records, each through its door"
returns = "record-kind.ruling@1"
outcomes = ["proposed", "ruled", "declined"]
witness = { class = "history", by = "one ruling record per customization" }
owner = "dShippedRelease"
[item.routes]
proposed = "end"
ruled = "end"
declined = "end"
```

`flow-steps.md:719` names `kits.install` or `kits.update` as the Needs cell, and the core's own command,
and `check_program` refuses a need naming no row, so `needs` is empty, as TOOL-dLinkedLibrary-23 S8 rules
for its sibling. Each proposal is one owner item, resolved as `[breakpoint]`'s owner gate is: the
`proposed` outcome ends the command, and the owner's `--rule` is the ruling.

### Inventory

Minted: `tools/playbook/adopt_declarations.py` with `scan_declarations`, `derive_leg_proposals`,
`derive_house_proposals`, `derive_conf_proposals`, `derive_role_proposals`, `write_ruled_proposal`, its verb
`--fixture`, `--plant`; the dispatcher verb `declarations`; the marks `below-floor`, `held:`; the key
grammar `<source>#<name>`. Naming cell `py.function`: each OK by `python tools/lexicon/lexicon.py
--suggest <name> --as py.function` at `5d1c82ac`.

### Migration

None: the verb reads what exists and writes only through doors. A kept house file stays a fallback
(TOOL-dBoundRoles-21 S2) until the owner accepts or declines, so nothing changes under an unruled tree.

### Rollout

Live with DEPL-dShippedRelease-17's hooks. Gov itself proposes nothing while its house file reads gov's
own seed and its conf's vocabularies are as the census left them.

### Files touched (estimate)

- `tools/playbook/core.py`: the `declarations` dispatch
- `tools/playbook/adopt_declarations.py` (new): S1 to S5
- `tools/playbook/adopt-playbook.sh`: the selftest runs S2's fixture under every plant
- `tools/govkit/govkit.py`: S6, `KIT_HOOKS`' `install` row
- `tools/loop/loop.toml`: S7
- `help/adopt.md`: S8

### Alternatives rejected

- **Migrating without a ruling, as an upgrade step.** The clause says "for the owner to rule once", and a
  conf vocabulary's right home is a judgment no step holds.
- **Seeding the overlay at install and letting the owner edit it.** Nobody edits a shipped or rendered
  declaration (flow-roles-adoption, item 1), and a hand edit carries no change record.
- **A proposal record per customization beside the ruling.** `flow-steps.md:719` says "one proposal
  record per customization". Rejected for a printed proposal: the scan re-derives it from the tree, so a
  stored copy is `[derive]`'s second answer, and the `ruling` is the record that must persist. §8 F3.

## 5. Production-readiness checklist

- security — every write passes a guarded door with its proof; the scan reads and spawns nothing but
  `leg_factory.py` and a `policy.py get`. A value below the floor is never written by an agent.
- perf / scale — one scan per hook run, a few files.
- error / empty / loading states — an absent input prints one line; an empty scan prints `declarations —
  none proposed` naming what it read, never a bare success.
- observability — each proposal prints its source; each ruling is a record.
- risks — a declined conf vocabulary leaves the term in `.unattended.conf`, where a kit still reads it
  until dConvergedCharter retires the seam; the ruling says so and no row is lost.
- testing — the arms of §7, one fixture holding each input.
- migration — none.
- user docs — `help/adopt.md`.

## 6. Acceptance criteria

- **AC1** — When `python adopt_declarations.py --fixture --plant all-inputs` runs over a scratch target
  holding each input of §4 "The inputs", `python core.py adopt declarations --build fx --unit fx-1` prints
  one proposal per customization with its key, source and row, and a second run prints the same keys.
  Red when: an input proposes nothing, or a key moves between runs.
- **AC2** — When the same fixture's `--rule manifest#hand-leg accept --reason r` runs on the owner path,
  the overlay holds a `leg.adopter.hand-leg` `[[gate-leg]]` row, and `manifest#ceiling-leg` writes a patch
  whose `edges` holds an `amends` naming the gov leg at its hash and whose fields hold `ceiling` alone.
  Red when: a patch copies gov's whole row, or a hand-added leg lands under a gov tag.
- **AC3** — When `--plant house-default` runs with a house file setting `default = "high"` and one role
  at `xhigh`, the scan proposes `roles.effort.default` at `high` and the role's `roles.effort.*` key at
  `xhigh`, and each `accept` writes `.governance/policy.toml` through `policy_edit.py`; with `default =
  "medium"` no `roles.effort.default` proposal appears.
  Red when: a `default` other than medium is missed, or medium is proposed as a customization.
  fixture: `--stub terminal` stands in for the owner's terminal inside the fixture process.
- **AC4** — When `--plant house-low` runs with `default = "low"`, the proposal prints `below-floor` and
  `accept` at the stubbed terminal under `policy-file.guard` `owner-only` writes the value; under a
  committed `.governance/policy.toml` naming `agents-with-reason` it prints `held:` and `accept` exits 2.
  Red when: a value below the floor reaches the policy file without the owner's authorization.
- **AC5** — When `--plant conf-vocab` runs with `DOD_EXTRA` and `HALT_CODES_EXTRA` terms, each term
  proposes an `[[item]]` row whose witness class is `history`, and `--plant role-file` proposes a
  `role.adopter.<slug>` row with its `workflow.adopter.<name>` row, naming each field the role file lacks.
  Red when: a term is dropped unruled, or a repository role lands with no workflow entry.
- **AC6** — When `--rule <key> decline --reason r` runs, one `ruling` record exists, no row or value was
  written, and the next scan omits the key; a second `--rule` on it exits 2 naming the first.
  Red when: a declined customization returns, or a key is ruled twice.
- **AC7** — When `grep -c "adopt.*declarations" govkit.py` runs from `tools/govkit`, it prints at least
  `2`, and `python kit_walk.py --fixture --plant hooks-install` names `adopt declarations` on the
  install's order.
  Red when: only one verb's hook runs it, where the clause says "at install and update".
- **AC8** — When `python loop_lib.py --check` runs, `item.adopt.declarations` passes.
  Red when: a route is undeclared.
- **AC9** — When `grep -c below-floor adopt.md` runs from the `help` directory it prints at least `1`.
  Red when: the page does not say how a low effort is ruled.

## 7. Gates

`playbook render selftest` · `govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `recall floor arms` · `policy fixtures` · `memory hygiene`

New arm: tools/playbook/adopt-playbook.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 · the playbook-render selftest runs `adopt_declarations.py --fixture` under every plant, its failing case `house-default` reading no `roles.effort.default` proposal · none

## 8. Open questions

- **F1 — A house `default` below medium** (scout D fork 7). Options: (a) refuse to propose it; (b)
  propose it as it stands, marked, and let TOOL-dBoundRoles-23's owner authorization govern the write; (c)
  raise it to medium silently. TOOL-dBoundRoles-23 S5 makes a house value below medium a defect and the
  owner's write through `.governance/policy.toml` the one path below the floor, S6 holding that to
  `owner-only`. (a) leaves an owner's real setting unproposed against the clause's "its `default` as
  `roles.effort.default`", and (c) changes the owner's value unasked. RESOLVED (agent, 2026-10-30,
  delegated): (b), rung 1. widens: none · relaxes: none
- **F2 — What a conf vocabulary term becomes.** The clause says "items with computed witnesses or as
  drops", and no step is named. Options: (a) one `item.<step>.adopter.<term>` per term, the step by key:
  `DOD_EXTRA`, `HALT_CODES_EXTRA` and `HOLD_CODES_EXTRA` at `step.deploy`, `PHASES_EXTRA` and
  `DIRECTIVES_EXTRA` at `step.build`, witness class `history` by the conf term, the owner free to
  decline, which is the drop; (b) a stage per term. (b) is heavier than a one-word term carries. RESOLVED
  (agent, 2026-10-30, delegated): (a), rung 3. widens: none · relaxes: none
- **F3 — Is a proposal a record?** `flow-steps.md:719` says "one proposal record per customization", and
  the scan re-derives every proposal from the tree. Options: (a) printed proposals, the `ruling` the
  record; (b) a `proposal` record kind. The clause says "proposed as overlay rows for the owner to rule
  once", and the `returns` of `item.adopt.declarations` is the ruling, as TOOL-dLinkedLibrary-23 S8's is
  for its sibling. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, from the packet's Items 28, `flow-steps.md:719`, flow-roles-adoption
  items 17 and 18, scout D's unit 28 row and its fork 7.
- rev-2 · 2026-10-30 · §3 · the Edges gain the mirror of each edge the round-1 spec audit's promoted units declare toward this unit (units 78); no scope, design or criterion moved.

## 10. Reuse audit

The seams extended are the `core.py adopt` dispatcher (TOOL-dLinkedLibrary-8 S3), with
TOOL-dLinkedLibrary-23's `tools/playbook/adopt_instructions.py` the sibling copied in shape, propose each
item and rule once; `load_policy` (`tools/roles/roles_lib.py:398`) for the house file; `leg_factory.py
--legacy-rows` (TOOL-dWitnessedBar-28 S7) for the legs; and the doors `instructions_edit.py` and
`policy_edit.py`. `python tools/codebase-map/reuse_lookup.py "propose existing customizations as overlay
rows for an owner ruling"` ranked name-stem helpers (`rows`, `row`, `read_catalogue_row`) and no
proposal code, because none is built at HEAD. Scout D's inputs hold at `5d1c82ac0`, with one correction:
`receipt.gate_runner.emitted` alone cannot find a hand-added leg once TOOL-dWitnessedBar-28 lands, whose
`--legacy-rows` does that join and is the one reader. Recall surfaced flow-roles-adoption items 17 and 18.

Recall terms used: `python tools/memory-recall/query.py "how are an adopter's existing legs, house efforts and role files proposed as overlay rows" --terms "adopt.declarations overlay rows house file roles.effort legacy-rows gate-leg role.adopter ruling proposal floor"`
