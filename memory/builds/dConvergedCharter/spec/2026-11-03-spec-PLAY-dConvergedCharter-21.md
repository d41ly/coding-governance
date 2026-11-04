# PLAY-dConvergedCharter-21 — `tools/roles/house/policy.toml` retired as a seed: a repository's unruled efforts folded into `roles.effort.*` by an upgrade step, and the house-file fallback gone

**Status:** OPEN · rev-2 · 2026-11-04 · node d · Tier-2 · base 0d1c1dda · streams playbook · order 8 · advances PLAY-dConvergedCharter-24

**Carries:** cl-dClosedLoop-0495@53f4c9b2 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md](../build/2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-03-build-PLAY-dConvergedCharter-11-reuse-scout-c.md](../build/2026-11-03-build-PLAY-dConvergedCharter-11-reuse-scout-c.md) | research | PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-22 |
| [2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md](../build/2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md) | journal | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-39 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-fix-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-fix-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md](../reviews/2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md) | spec-audit | PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-18 |

<!-- /gen:spec-records -->

## 1. Goal

The seeded `tools/roles/house/policy.toml` never receives gov's change, so the records' lowered efforts never
reach an adopter (`gap-roles-26`, gap register :178). TOOL-dBoundRoles-21 puts every reader on the
`roles.effort.*` keys and each role's declared `effort` and `gates`, and keeps the house file as a
fallback; DEPL-dShippedRelease-28 lets the owner rule each customization once. This unit retires the
seed: an upgrade step folds a repository's efforts the owner has not ruled on into the keys, a declined
one read as a drop, and the fallback leaves every reader.

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build, each specced and unbuilt at base
`0d1c1dda`: `read_policy_setting`, the role's declared `effort`, the role `gates` field and the fallback
order's step 4 (TOOL-dBoundRoles-21 S1, S3, S6, S7, §4 "The order"), with TOOL-dBoundRoles-2 and -23;
`adopt.declarations`, its proposals keyed `<source>#<name>` through `derive_house_proposals`, and one
`ruling` record per key (DEPL-dShippedRelease-28 S2, S3, S4, I8); the `ruling` kind
(TOOL-dLinkedLibrary-8); the shared step `conf_to_policy.py` (TOOL-dDeclaredLoop-21 S8) with unit 20's
home mode; and `derive_readers` (unit 11's I1).

- **S1** — The step, `roles/house-seed-to-policy`, an `[[upgrade]]` row in `tools/roles/kit.toml`, its
  program `tools/govkit/steps/house_seed.py`, a caller of `conf_to_policy.py` that hands it a reader of
  its own for the TOML home. Its up, in order: (1) `derive_house_folds(target)` reads the house file's
  customizations through `derive_house_proposals` (DEPL-dShippedRelease-28 S2), each keyed
  `<source>#<name>`; (2) `read_ruled_keys(target)` reads every `ruling` record's subject, and each ruled
  key is dropped, an `accept` already written by DEPL-dShippedRelease-28 S4 and a `decline` read as a
  drop; (3) each unruled effort is written to its key, `[effort.roles] <r>` to `roles.effort.<r>`,
  `[effort.stages.<w>] <s>` to `roles.effort.<w>.<s>` and its `default` to `roles.effort.default`, through
  `render_policy_text` behind one before-image; (4) the house file is deleted last. A value equal to
  the role's declared level, or a `default` of `medium`, is no proposal, so it goes with the file:
  gov's levels live in the role definitions every release updates. An unruled effort below the floor,
  a level under `medium` (DEPL-dShippedRelease-28 S5, TOOL-dBoundRoles-23 S5), is never written by the
  step, since `policy-file.guard` admits it only under the owner's authorization: it stops the up as an
  unruled grant does (S2), writing nothing, exit 1, naming the key and `core.py adopt declarations
  --rule <key> accept|decline`, so the level reaches the policy file only through the owner's ruling and
  `check_effort_floor` never reds a value the step wrote. `house_seed.py` spells `house/policy.toml`
  literally, as `HOUSE_MIGRATORS` requires (unit 11 S8), so the inventory still lists it.
  Observed by AC1, AC2, AC3 and AC7.
  **Readers:** by name: `tools/roles/kit.toml:39`, `tools/roles/roles_lib.py:398-411`,
  `tools/roles/check_roles.py:367`, `tools/roles/handoff.py:480`, `tools/roles/render_agents.py:140`,
  `tools/policy/policy.py:1119` (`HOUSE_ANCHOR`), `tools/policy/legacy-homes.txt` · by value: the
  fallback order's step 4 in `resolve_stage_efforts` and `resolve_effort` (TOOL-dBoundRoles-21 §4), which
  reads the file's levels where no key is set, and `derive_house_proposals`, which compares each level
  with the role's declared one.
- **S2** — The grants. An unruled `[gates]` proposal, a row naming a leg the role's `gates` field
  lacks, stops the up writing nothing, exit 1, naming each key and
  `core.py adopt declarations --rule <key> accept|decline`; the walk records the step failed and stops,
  and unit 20's exit check reads the adopter pending until the owner rules (§8 F1). A ruled grant is
  dropped like a ruled effort: an `accept` already lies in the overlay's `[[role]]` patch
  (DEPL-dShippedRelease-28 S4). Gov's two grants move into `gov-spec-writer` and `gov-builder` in
  TOOL-dBoundRoles-21 S6, so gov's own tree holds no unruled grant. Observed by AC4.
- **S3** — The seed leaves gov. `tools/roles/house/policy.toml` leaves the seed `[[files]]` include of
  `tools/roles/kit.toml:36-40` and gov's tree, and the step's `surfaces` name the member the step gate
  reads as vanished, spelled as `step_gate.py --list` prints it. Gov's own copy holds only gov's levels
  and grants, each its role's declared value, so gov's own `update` folds nothing. Observed by AC6.
  **Readers:** by name: `tools/roles/kit.toml:31-40`, `tools/roles/house/policy.toml:1-3`,
  `tools/roles/README.md:173-195`, `help/roles.md:44`, `help/roles.md:126`, `help/policy.md:234`,
  `help/policy.md:246` · by value: the receipt's `seed` row for the file, which `update` withdraws
  when the entry stops shipping it.
- **S4** — The fallback leaves every reader. `load_policy` (`tools/roles/roles_lib.py:398`) is deleted
  with its last caller; the order's step 4 leaves `resolve_stage_efforts` and `resolve_effort`, so
  after the keys a role's declared `effort` answers; `print_stage_efforts` (`tools/roles/handoff.py:474`)
  and `render_agents.py`'s `run_mode` read through that order alone; R12 leaves `check_roles.py`
  (`:42`, `:367`); `render_roles_index` reads each role's `gates` field and no house row; the house
  home leaves `derive_legacy_homes` (`HOUSE_ANCHOR`, `tools/policy/policy.py:1119`), and its two rows
  leave `tools/policy/legacy-homes.txt` by `policy.py lists --write` only. `check_gate_names`, lifted
  by TOOL-dBoundRoles-21 S6, stays for the role field. The census's effort and grant population in
  `tools/govkit/settings_census.py` (unit 22), read through `load_policy`, leaves with the file: the
  census prints one line `efforts and grants: house file retired (PLAY-dConvergedCharter-21) — the
  roles.effort.* keys and each role's gates field hold them` in place of the population, never an empty
  one, and no longer imports `load_policy`. The policy kit's README stops describing the house file as a
  legacy home. Observed by AC5, AC6 and AC8.
  **Readers:** by name: `tools/roles/roles_lib.py:398-480`, `tools/roles/check_roles.py:42`,
  `tools/roles/check_roles.py:367`, `tools/roles/handoff.py:34`, `tools/roles/handoff.py:480`,
  `tools/roles/render_agents.py:8`, `tools/roles/render_agents.py:140`, `tools/roles/render_agents.py:330`,
  `tools/roles/render_agents.py:460`, `tools/roles/render_agents.py:499-507`, `tools/policy/policy.py:1119`,
  `tools/policy/policy.py:1218`, `tools/roles/README.md:175`, `tools/policy/README.md` (`:149-157`,
  where it still names the house file a legacy home, `:385` and `:522-527`), the comment at
  `tools/govkit/selftest.py:9581`; READER NOT IN TREE: `tools/govkit/settings_census.py`, which unit 22
  creates at order 1, after base, and whose effort and grant population reads the house file through
  `load_policy` · by value: R12's
  refusal lines, which the
  roles fixtures at `tools/roles/render_agents.py:460-507` compare; the two `legacy-homes.txt` rows
  `<tool-root>/roles/house/policy.toml [effort]` and `[gates]`, which `lists --check` compares.
- **S5** — The docs: `help/roles.md` says a role's effort is the `roles.effort.*` keys, then the
  role's declared level, and a grant the role's `gates` field or an overlay patch; `help/policy.md`
  names the legacy places without the house file. NOT OBSERVED by a criterion: prose, graded by the `docs`
  leg at the close.

## 3. Non-goals (OUT)

- The keys, the declared `effort`, the `gates` field and the order with its fallback: TOOL-dBoundRoles-21.
- Proposing a customization or writing a ruling: DEPL-dShippedRelease-28's `adopt.declarations`.
- The arm that reds a planted reader still reading the house file: unit 11's, over the
  `READER_SHAPES` row it adds. This unit removes the readers that arm would find.
- The house overlays `house/gov-*.md`: TOOL-dBoundRoles-19 moves them into the overlay.
- A conf-to-policy step module of this unit's own: S1 calls the shared one.

### Edges

- **consumes-from** `PLAY-dConvergedCharter-11` — `derive_readers` and its house-file arm `arm_house_readers`, the inventory AC6 runs over the house file's path, and the two `legacy-homes.txt` rows S4 drains; without it the re-point is a typed list nothing re-derives
- **consumes-from** `PLAY-dConvergedCharter-22` — `settings_census.py`, whose effort and grant rows read the house file through `load_policy`; S4 takes that population out of the census with the file
- **consumes-from** `PLAY-dConvergedCharter-20` — `fanout_cap.py`'s shared step `conf_to_policy.py` with its home mode, which S1 calls with a TOML reader; without it the step copies the before-image and writer a third time
- **consumes-from** external — TOOL-dBoundRoles-21 (with -2 and -23), DEPL-dShippedRelease-28, TOOL-dLinkedLibrary-8 and TOOL-dDeclaredLoop-21 S8, each specced and unbuilt at base `0d1c1dda`

## 4. Design

### Evidence

Read at `d8a12f04`; no product file differs from base `0d1c1dda`.

- `tools/roles/house/policy.toml` holds `[effort] default = "medium"`, `[effort.roles]` for seven roles,
  two `[effort.stages.*]` tables and `[gates]` for `gov-spec-writer` and `gov-builder`; it ships as a
  `seed` (`tools/roles/kit.toml:31-40`), so `update` never rewrites it, which is `gap-roles-26`.
- `load_policy` (`tools/roles/roles_lib.py:398`) is called at `check_roles.py:367`, `handoff.py:480` and
  `render_agents.py:140`. `render_agents.py:330` writes the file in its own fixture, not in production;
  scout C's row reads it as the seed's writer.
- The catalogue rows `roles.effort.<role>`, `roles.effort.<workflow>.<stage>` and `roles.effort.default`
  exist (`tools/policy/catalogue.toml:296-310`), owned by dBoundRoles.
- `tools/policy/legacy-homes.txt` lists the file's two tables as owner-policy rows, and
  `derive_legacy_homes` finds the file through `HOUSE_ANCHOR` (`tools/policy/policy.py:1119`, `:1218`).

### The fold

| House value | Ruled `accept` | Ruled `decline` | Unruled |
|---|---|---|---|
| a level differing from the role's declared `effort` | dropped, already set | dropped | `roles.effort.<role>` or `roles.effort.<w>.<s>` |
| `default` other than `medium` | dropped, already set | dropped | `roles.effort.default` |
| a level equal to the declared one, `default = "medium"` | no proposal | no proposal | dropped |
| a `[gates]` row the role's field lacks | dropped, in the overlay | dropped | the up stops, S2 |
| a level below `medium`, the floor | dropped, already set under the owner's authorization | dropped | the up stops, S1, as for a grant |

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `derive_house_folds`, `read_ruled_keys` | functions, `tools/govkit/steps/house_seed.py` | `py.function`, OK by `--suggest` |
| `roles/house-seed-to-policy` | `[[upgrade]]` id | none |
| `house_seed.py` | step program | none, `py.file` is no declared cell |

### Migration

The step is the migration: up, down from the before-image, and the witness reading the house file
absent. An adopter whose house file holds an unruled grant stays at the step until the owner rules.

### Rollout

The step and S3 land in one commit, after TOOL-dBoundRoles-21 and DEPL-dShippedRelease-28; S4 lands
in the same commit, since a reader left on `load_policy` with the file gone reads an empty fallback
forever.

### Files touched (estimate)

- `tools/govkit/steps/house_seed.py` (new): S1, S2
- `tools/roles/kit.toml`, `tools/roles/house/policy.toml` (deleted): S1, S3
- `tools/roles/roles_lib.py`, `tools/roles/check_roles.py`, `tools/roles/handoff.py`,
  `tools/roles/render_agents.py`, `tools/roles/README.md`: S4
- `tools/policy/policy.py`, `tools/policy/legacy-homes.txt`, `tools/policy/README.md`: S4
- `tools/govkit/settings_census.py`: S4, the house population retired
- `tools/govkit/usage.toml`, `tools/govkit/selftest.py`: the step's `[[usage]]` rows and §6's plants
- `help/roles.md`, `help/policy.md`: S5

### Alternatives rejected

- **Folding every house value.** Rejected by `gap-roles-26` itself: gov's own levels written as an
  adopter's keys outrank each later change gov makes to a role's declared level, the defect this unit
  closes.
- **Keeping `load_policy` reading an absent file as empty.** A reader with no file to read is a
  disabled branch, and `[yagni]` deletes rather than disables.
- **A second conf-to-policy module for the TOML home.** The shared step owns the before-image and the
  writer; only the home's reader differs, so the caller supplies that.

## 5. Production-readiness checklist

- security — no grant and no below-floor effort is written without the owner's ruling (S1, S2), the
  floor being the one `policy-file.guard` holds for an automated write; efforts are levels from a closed
  set, each written through the one policy writer under `run_step_isolated`.
- perf / scale — one proposal scan and one ruling read per step.
- error / empty / loading states — no house file: the up exits 0 writing nothing; a malformed one
  refuses as `derive_house_proposals` refuses.
- observability — the up prints each key written and each key dropped, with the ruling that dropped it.
- risks — an adopter holding an unruled grant is stopped at the step; unit 20's exit check puts that
  adopter to the owner rather than letting the grant vanish.
- testing — the plants of §6 over scratch targets with planted house files and rulings.
- migration — §4.
- user docs — `help/roles.md`, `help/policy.md`, S5.

## 6. Acceptance criteria

- **AC1** — When `python house_seed.py up <target>` runs over a scratch target whose house file sets
  two roles' levels off their declared ones, one with a `decline` ruling and one with none, the policy
  file gains `roles.effort.<role>` for the unruled role only, and the house file is gone.
  Red when: the planted declined effort is written, so a decline reads as an accept.
- **AC2** — When the same up runs where the first role's ruling is `accept` and the policy file already
  holds its key, that key's line is byte-identical after the up.
  Red when: the step writes an accepted key a second time.
- **AC3** — When the up runs over a house file setting `default = "high"` and no ruling, the policy file
  gains `roles.effort.default = "high"`; over one setting `default = "medium"` it gains no line.
  Red when: gov's own default is restated as an adopter's key.
- **AC4** — When the up runs over a house file whose `[gates]` grants a role a leg its `gates` field
  lacks, with no ruling, it exits 1 naming the key and the `--rule` command, and both files are
  byte-identical; with a `decline` ruling for that key it completes.
  Red when: an unruled grant is written to the overlay or silently dropped.
- **AC5** — When `resolve_effort` runs over a scratch roles kit whose house file sets a role to `max`
  with no key set, it returns the role's declared level; and `python house_seed.py down <target>` after
  AC1 restores both files byte-identical.
  Red when: a reader still reads the house file, or the down leaves a written key.
- **AC6** — When `python check_policy.py --readers tools/roles/house/policy.toml --kind path
  --except tools/govkit/steps/house_seed.py --except tools/playbook/adopt_declarations.py --except
  tools/govkit/selftest.py` runs over the unit's tip with `house_seed.py` present, it exits 0, the three
  exempt paths being unit 11's `HOUSE_MIGRATORS` and the self-test holding their plants, each still
  spelling the path; `git grep -n load_policy -- tools` prints nothing; unit 11's `arm_house_readers`
  reads armed and names no reader; a scratch copy with `tools/roles/house/policy.toml` read in
  `tools/roles/check_roles.py` makes both the CLI and the arm red naming that file; and `python
  tools/policy/policy.py lists --check` exits 0 with the two house rows gone.
  Red when: a reader of the retired seed survives, a migrator the step needs reds, or the shrink-only
  list keeps a row no home yields.
- **AC7** — When `python house_seed.py up <target>` runs over a scratch target whose house file sets
  `gov-skeptic = "low"`, below the floor, with no ruling, it exits 1 naming `effort.roles.gov-skeptic` and
  the `--rule` command, and the house file and the policy file are byte-identical; with an `accept`
  ruling for that key it completes and writes no line for it.
  Red when: a below-floor effort reaches the policy file with no owner act.
- **AC8** — When `python settings_census.py --report` runs over the unit's tip, it prints the `house file
  retired` line in place of effort and grant rows, and `grep -c load_policy tools/govkit/settings_census.py`
  prints 0.
  Red when: the census reads an absent house file as an empty population, or still calls the deleted
  fallback.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `policy check` · `policy fixtures` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `upgrade-walk` · `step-gate` · `docs` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 AC4 AC7 AC8 · scratch targets under `house_seed.py`'s plants and the census over a seedless tree, failing cases a declined or below-floor effort written and an empty census population · none
New arm: tools/roles/render_agents.py · covers AC5 · its fixture with a planted house file and no key, failing case the house level read · none

## 8. Open questions

- **F1 — What the step does with an unruled grant.** The clause folds a repository's `[gates]` into
  each role definition's gate grant, and an adopter's role definition is an overlay `[[role]]` patch
  written through `instructions_edit.py add` (DEPL-dShippedRelease-28 S4). Options: (a) stop the up
  writing nothing until the owner rules, the ruling's `accept` writing the patch through the door;
  (b) write the patch through the door inside the step; (c) drop the grant as a decline. (b) writes an
  agent grant nobody ratified, a security surface beyond this unit's tier, and the door re-renders files
  the before-image cannot name; (c) loses an adopter's grant, failing the clause. RESOLVED (agent,
  2026-11-03, delegated): (a), rung 3, the grant reaching the role's definition through its ruling. widens: none · relaxes: none
- **F2 — Which house values the step folds.** Options: (a) the unruled customizations
  `derive_house_proposals` finds, a value equal to gov's declared level dropped with the file; (b) every
  value. (b) writes gov's own levels as adopter keys, which then outrank every later gov change to a
  role's declared level, the defect the clause closes. RESOLVED (agent, 2026-11-03, delegated): (a), rung 3. widens: none · relaxes: none
- **F3 — `load_policy` once the file is gone.** Options: (a) deleted with its last caller; (b) kept,
  reading an absent file as an empty fallback, as TOOL-dBoundRoles-21 S7 lets R12 read it. (b) is a branch
  no tree can reach. RESOLVED (agent, 2026-11-03, delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, from the packet's Items 21, `gap-roles-26`, v2:1131-1132, scout C's
  row for 0495, and the spec brief's I6 and I8.
- rev-2 · 2026-11-04 · S1 S4 §4 §5 AC6 AC7 AC8 §7 · folded
  `2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1` findings 10 (`settings_census.py` in S4's
  readers and Files touched, its retired-population line), 42 and 49 (AC6 passes unit 11's
  `HOUSE_MIGRATORS` as `--except` paths, the policy README and the selftest comment re-worded, a planted
  non-exempt reader reds) and 48 (a below-floor effort stops the up like an unruled grant).

## 10. Reuse audit

The seams are TOOL-dDeclaredLoop-21 S8's `conf_to_policy.py` with unit 20's home mode, for the
before-image and the writer; DEPL-dShippedRelease-28's `derive_house_proposals` and its `ruling`
records, for which values fold; and TOOL-dBoundRoles-21's order, from which this unit deletes step 4.
`python tools/codebase-map/reuse_lookup.py "fold a seeded house effort file into policy keys skipping
ruled proposals"` ranked `load_policy` (`tools/roles/roles_lib.py`), `read_conf_key`, `readConfKey` and
`read_design_keys`; `load_policy` is the reader this unit deletes, and the rest read other files. No
seam at HEAD reads a ruling, since the kind is TOOL-dLinkedLibrary-8's and unbuilt. Scout C's row
disagrees with source once: it names `render_agents.py:330` the seed's writer, and that line writes a
fixture's copy; the seed ships through `tools/roles/kit.toml:31-40`.

Recall terms used: `python tools/memory-recall/query.py "how does the roles house policy seed retire into roles.effort keys and role gates" --terms "house policy.toml seed roles.effort load_policy gates fallback adopt.declarations ruling decline"`
