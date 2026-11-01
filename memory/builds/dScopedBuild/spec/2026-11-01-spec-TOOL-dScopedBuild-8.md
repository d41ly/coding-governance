# TOOL-dScopedBuild-8 — `build.unit-pass` and `build.scope` draining the legacy a unit touches as `retrofit.drain` says, and claiming the baselined map keys its write set holds as `retrofit.claim-on-touch` says

**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 6 · advances TOOL-dScopedBuild-16

**Carries:** cl-dClosedLoop-0406@c1850071 whole
**Carries:** node:item.build.unit-pass
**Carries:** node:policy-key.retrofit.drain
**Carries:** node:policy-key.retrofit.drain-cap
**Carries:** node:policy-key.retrofit.claim-on-touch
**Carries:** node:policy-key.retrofit.claim-cap

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-build-TOOL-dScopedBuild-3-reuse-scout-b.md](../build/2026-11-01-build-TOOL-dScopedBuild-3-reuse-scout-b.md) | research | TOOL-dScopedBuild-3 TOOL-dScopedBuild-5 TOOL-dScopedBuild-9 |
| [2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |

<!-- /gen:spec-records -->

## 1. Goal

gap-build-05 (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:366`):
baselines are not tied to touch. Five kits stay baselined after 14 to 278 touches each, and the
per-file count ratchet let 29 of 129 encoding sites persist on edited lines (PINNED,
`research-retrofit-b.md:118`, `research-retrofit-a.md:102`). The registries are per-(path, arm)
counts with no line key (`tools/gate-lint/encoding_posture.py:40`, "THE REGISTRY"), `baseline.toml`
shrinks only by hand (`memory/map/baseline.toml:1-5`), and no deriver maps a baselined map key to the
paths that realize it (`KEYED_ATTRIBUTORS = ()`, `tools/codebase-map/map_extractors.py:408`).

This unit makes the builder's pass, `build.unit-pass`, drain the baselined sites a unit touches and
claim the baselined map keys its write set holds, and makes `build.scope`'s touch join grade both:
the sites inside the unit's changed hunks under `hunk`, every baselined site in each touched file
under `file`, both under `retrofit.drain-cap`, nothing owed under `off`; and the held keys claimed
under `retrofit.claim-cap`, carried with an ask, or neither, as `retrofit.claim-on-touch` says
(`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md:378-417`).

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build: TOOL-dScopedBuild-9's frame in
`tools/memory-tree/routed_commits.py` (`check_touch_join`, `check_claim_arm`, `read_touched_hunks`),
TOOL-dScopedBuild-3's `build.scope` value and reduced write set, TOOL-dScopedBuild-14's I4 read
`read_gate_value` and I5 renderer `render_gate_outcome` with its filer `write_gate_asks`, and the legacy ledger factory with its memory-tree copy
`tools/memory-tree/legacy_ledger.py` (`read_registrations`, `read_rows`, the `[[ledger]]` registration
and its dispositions; TOOL-dWitnessedBar-13 S1, S2, S8, a parent).

- **S1** — The four reads. `retrofit.drain` (`hunk`, `file`, `off`; default `hunk`),
  `retrofit.drain-cap` (`5`, `20`, `50`; default `20`), `retrofit.claim-on-touch` (`claim`, `carry`,
  `off`; default `claim`) and `retrofit.claim-cap` (`1`, `3`, `5`; default `3`), each read once per
  run through I4 from the landed revision, its key a string literal at the call, its values verbatim
  from `tools/policy/catalogue.toml:1488-1510`. Observed by AC1 to AC5 and AC9.
- **S2** — The drain arm, `check_drain_arm(repo, unit, shas, hunks, drain, cap)` in `routed_commits.py`,
  run by `check_touch_join` for every registration whose `drain` is `hunk`. The sites a unit owes at
  its tip: under `hunk`, each site S3 reports inside the unit's hunk set; under `file`, each site of a
  ledger row whose path the unit touched, by the row's count; under `off`, none, and the arm prints
  `drain off` while the work order's legacy slot still renders (TOOL-dFurnishedOrders-11 S3). Where
  the memory-tree kit carries no `legacy_ledger.py`, or no registration's `drain` is `hunk`, the arm
  prints one `drain · not-installed: <why>` line and owes nothing, and a registered population with no
  ledger file at its `home` prints `not-seeded`. Observed by AC2 and AC7.
- **S3** — The site lines, `read_site_lines(repo, reg, paths)`: the registration's `seed` argv with
  `--sites` and the touched paths appended, run by subprocess at the graded tree, each output line
  `<path> TAB <line>`. A seed that exits non-zero or prints any other line makes that population
  `not-installed: its seed prints no sites`, never clean, and under `hunk` it owes nothing until its
  check answers `--sites` (§8 F1). Observed by AC2 and AC7.
- **S4** — Drained, carried, owed. `drained` is the sum, over the ledger rows of the unit's touched
  paths, of the row's count at the unit's base, the first parent of its oldest own commit, less its
  count at the tip, both ledgers read in one `git cat-file --batch`. A site sits on a carried row when
  its disposition is `deferred:<ask>`, `keep:<ask>` or `carried:<unit>`. The findings, each to the I5
  renderer under `build.scope`: `undrained`, an owed site on a `seeded` row; `carried under the cap`,
  an owed site on a `deferred:` row while `drained` is below the lesser of `retrofit.drain-cap` and
  `drained` plus the owed count; and `deferral names no ask`, a `deferred:<ask>` whose ask the build's
  `BACKLOG.md` at the tip does not hold. Observed by AC2 and AC3.
- **S5** — The claim arm's key half, `check_key_claims(repo, unit, writes, claim, cap)`, called by
  `check_claim_arm` where the map is installed. A key is held when the map's `--key-paths` mode (S6)
  prints a realizing path the unit's write set covers, by `design_lib.check_writes_intersect`, and
  the map's baseline at the unit's base lists it. A held key is claimed when the baseline at the tip
  no longer lists it, and carried when an ask row of the build's `BACKLOG.md` at the tip names it as
  `` `<inventory>:<key>` ``. Under `claim`: `unclaimed`, a held key neither claimed nor carried; and
  `carried under the cap`, a carried key while the claimed count is below the lesser of
  `retrofit.claim-cap` and the held count. Under `carry`: `uncarried`, a held key neither claimed nor
  carried. Under `off`: one `claim off` line. Observed by AC4 and AC5.
- **S6** — The map's side of the claim. `derive_key_paths(rows)` in
  `tools/codebase-map/map_lib.py`, pure, returns `{inventory: {key: [path, ...]}}` from the project
  layer's `KEY_PATHS` table, one callable per inventory in the shape of `EXTRACTORS`
  (`map_extractors.py:193`). gov's `tools/codebase-map/map_extractors.py` declares rows for the five
  inventories its baseline holds keys in at base, `gate-legs`, `kits`, `git-hooks`, `rendered-skills`
  and `gotcha-classes` (§4 "The key paths"), and `tools/codebase-map/map_extractors.template.py`
  declares an empty table with its comment. `python map_diff.py --key-paths` prints
  `<inventory> TAB <key> TAB <path>` per realization and one `# baseline <path>` line naming the
  baseline file; an inventory the baseline holds keys in with no row prints
  `# underived <inventory> <n>`, which the claim arm lists. Observed by AC6.
- **S7** — `build.unit-pass`, the builder's side. `tools/roles/agents/gov-builder.agent.md` gains one
  bullet: drain the baselined sites inside the hunks you change, or in each file you touch, as
  `retrofit.drain` says, and claim the baselined map keys your write set holds as
  `retrofit.claim-on-touch` says, writing the claiming dossier and taking the key's line out of the
  baseline, each within its cap; carry what you do not, with an ask, its id in the ledger row's
  `deferred:` disposition or its row naming the key. The body stays under its 4096-byte ceiling
  (`tools/roles/check_roles.py:87-91`) and `.claude/agents/gov-builder.md` re-renders. Observed by AC8.
- **S8** — The catalogue. The four rows gain `summary` and `usage`, and
  `python tools/policy/policy.py lists --write` re-renders `tools/policy/unsummarised-keys.txt`
  without them. Observed by AC9.
- **S9** — The docs: a section "The drain and the claim" on `help/build-scope.md`, the four keys, their
  values and what each owes; and the `map_diff.py` line of `tools/codebase-map/README.md` naming
  `--key-paths`. Observed by AC10.
- **S10** — The ask, filed by the main loop: §8 F1's, in dWitnessedBar's `BACKLOG.md`. NOT OBSERVED by
  a criterion: the main loop files it after the writers return.

## 3. Non-goals (OUT)

- The hunk set, the join's frame, the grace half of the claim arm and the `not-installed` state when
  the map is absent: TOOL-dScopedBuild-9.
- The ledger factory, its registrations, dispositions and rename carry: TOOL-dWitnessedBar-13. Each
  population's conversion into a ledger, and its scanner answering `--sites`: TOOL-dWitnessedBar-16
  and its siblings, through §8 F1's ask.
- The work order's legacy slot and its four states: TOOL-dFurnishedOrders-11 S3. This unit says what
  the builder does with it.
- Populating `KEYED_ATTRIBUTORS`, which decides map attribution, not which key a path realizes
  (§8 F2).
- The map's coverage gate grading a claim's dossier: the map's own gate.

### Edges

- **consumes-from** `TOOL-dScopedBuild-9` — `read_touched_hunks`, the hunk set the drain grades, and `check_touch_join` and `check_claim_arm`, the frame the drain arm and the key half run in; without them nothing calls either arm

## 4. Design

### Evidence

- The ledger keys a site by its fields and a count, and refuses a line number in a key field
  (`memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-13.md`, §4 "The ledger file"),
  so no ledger says where a site sits; a registration's `drain` is `hunk`, `key` or `none` and its
  `seed` is an argv (§4 "The registration").
- Each count-ratchet scanner already knows each site's line (`encoding_posture.scan_tree`,
  `tools/gate-lint/encoding_posture.py:130`; `sh_hygiene.scan_spawn_tree`, `scan_temp_tree`).
- `attribute_paths` takes a keyed attributor's claimants and stops at the first matching pattern, so
  a populated `KEYED_ATTRIBUTORS` row moves every path of a claimed key off its glob owners
  (`tools/codebase-map/map_lib.py:1792-1799`).
- gov's baseline holds 36 keys at base: 19 `gate-legs`, 5 `kits`, 1 `git-hooks`, 1 `rendered-skills`
  and 10 `gotcha-classes` (PINNED at `5f0b11f12`, `memory/map/baseline.toml`).
- A kit imports no sibling kit (`memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-1.md:113`):
  the memory-tree kit reads the ledger through its own inline copy, and the map and each scanner by
  subprocess.

### The lines

```
routed-commits: touch · TOOL-tFix-1 · drain · encoding-posture · hunk · 2 owed · 3 drained · cap 20
routed-commits: touch · TOOL-tFix-1 · drain · encoding-posture · tools/a:14 · undrained
routed-commits: touch · TOOL-tFix-1 · drain · sh-spawn · not-installed: its seed prints no sites
routed-commits: touch · TOOL-tFix-1 · claim · keys · 4 held · 1 claimed · 2 carried · cap 3
routed-commits: touch · TOOL-tFix-1 · claim · kits:workflows · unclaimed
routed-commits: touch · TOOL-tFix-1 · claim · gate-legs:template size <=48KiB · carried under the cap
```

A `drain off` or `claim off` line replaces its arm's lines under `off`.

### The key paths

| Inventory | A path realizes key `<k>` when it is |
|---|---|
| `gate-legs` | a script the leg's `argv` names in `tools/gate-legs.json`, `{prefix}` read as the tool root |
| `kits` | under `tools/<k>/` |
| `git-hooks` | `.githooks/<k>` |
| `rendered-skills` | under `.claude/skills/<k>/`, or the `SKILL.template.md` of `tools/<k>/` |
| `gotcha-classes` | `memory/gotchas/<k>` |

Each row is a zero-argument callable returning `{key: [path, ...]}`, read from the tree as the
inventory's extractor reads it. A write set covers a realizing path by `check_writes_intersect`, so
a unit declaring `tools/workflows/` holds `kits:workflows`.

### The caps

A unit owes at most the cap: it drains or claims up to the cap and carries the rest, each carry
naming an ask. `carried under the cap` is the one way a unit can carry what the cap obliged it to
do, and it is a finding. The caps are modelled at 20 sites (0.18% of gov's code commits binding) and
3 claims (the measured p90), both gov's (`retrofit.md:407-417`).

### What it does not check

Whether a drained site was fixed rather than moved out of the hunk; a site a scanner does not report;
whether a claiming dossier describes the key, which the map's coverage gate grades; an ask's content
beyond its id or its key token; and a key no `KEY_PATHS` row derives, which is listed `underived`.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_drain_arm`, `read_site_lines`, `check_key_claims` | functions in `routed_commits.py` | `py.function`, OK at `--suggest` |
| `derive_key_paths` | function in `map_lib.py` | `py.function`, OK at `--suggest` |
| `KEY_PATHS` | table in `map_extractors.py` and its template | none |
| `--key-paths` | flag of `map_diff.py` | none |
| `--sites` | the scanner convention §8 F1 asks for | none |
| `undrained`, `unclaimed`, `uncarried`, `carried under the cap`, `deferral names no ask` | findings | none |

### Migration

None: no population is a ledger at base, so the drain arm reads `not-installed` in gov until
TOOL-dWitnessedBar-16 converts one; the claim arm reads gov's 36 baselined keys from landing.

### Rollout

Live at landing at the catalogue defaults, `hunk`, `20`, `claim`, `3`, graded by `build.scope`'s
default `warn-and-ask`: an owed site or key warns and files an ask.

### Files touched (estimate)

- `tools/memory-tree/routed_commits.py`: S1 to S5, and their self-test arms
- `tools/codebase-map/map_lib.py`, `tools/codebase-map/map_extractors.py`, `tools/codebase-map/map_extractors.template.py`, `tools/codebase-map/map_diff.py`, `tools/codebase-map/selftest.py`: S6
- `tools/roles/agents/gov-builder.agent.md`, render `.claude/agents/gov-builder.md`: S7
- `tools/policy/catalogue.toml`, render `tools/policy/unsummarised-keys.txt`: S8
- `help/build-scope.md`, `tools/codebase-map/README.md`: S9

### Alternatives rejected

- **A `sites` field on `[[ledger]]`** — lost to the parent rule: it edits TOOL-dWitnessedBar-13's
  grammar, so it must land there first; the `seed` argv already names the scanner (§8 F1)
- **Hunk read at file grain until a scanner reports lines** — lost to the clause: `hunk` and `file`
  are two values, and the substitute would read `hunk` as `file` silently
- **Populating `KEYED_ATTRIBUTORS`** — lost to its effect: every path of a claimed key would leave its
  glob owners in every map digest · `tools/codebase-map/map_lib.py:1792-1799`
- **A disposition column in `baseline.toml` for a carried key** — lost to the map's grammar: the
  baseline is a shrink-only list of keys per inventory, and its parser reads no row field
  · `tools/codebase-map/map_lib.py:1107`

## 5. Production-readiness checklist

- security — each scanner's argv comes from a tracked registration and runs as a list, the paths
  appended as arguments; the map runs by subprocess with `CODEBASE_MAP_ROOT` the graded tree.
- perf / scale — one `--sites` subprocess per touched population, one `--key-paths` subprocess and one
  `cat-file --batch` per graded unit.
- error / empty / loading states — `not-installed` per population; `drain off`, `claim off`;
  `underived <inventory>`; a scanner exit outside 0 is that population's `not-installed`, never a
  refusal of the leg.
- observability — one line per owed site and per held key, naming its arm, value and cap.
- risks — `file` can owe many sites in a hot legacy file; the cap bounds what one unit owes.
- testing — each value of each key on a planted unit, the scanner's `--sites` refusal, the key paths.
- migration — none.
- user docs — `help/build-scope.md` (S9).

## 6. Acceptance criteria

- **AC1** — When `python -c` runs `check_policy.scan_reader_keys(".")` in this tree, the set holds
  `retrofit.drain`, `retrofit.drain-cap`, `retrofit.claim-on-touch` and `retrofit.claim-cap`.
  Red when: a read is not a literal call.
- **AC2** — When `check_routed_commits` runs on a planted unit whose commit changes line 14 of
  `tools/a` in a fixture registering one `hunk` population, its ledger row `tools/a` seeded at 2,
  and its seed answering `--sites` with lines 14 and 40: under planted `retrofit.drain` `hunk` it
  lists `tools/a:14 · undrained` and not line 40; under `file` it lists both; under `off` it prints
  `drain off` and no finding; and with a merge into the unit's range of a commit editing line 40, `hunk`
  still owes line 14 alone (`retrofit.md:402-403`).
  Red when: a value owes the wrong set, `off` owes anything, or a merged commit's hunk is owed.
  fixture: a scratch history from `routed_commits.build_fixture`, a fixture `kit.toml` `[[ledger]]` row
  read by `legacy_ledger.read_registrations`, and the policy file on the fixture's `main`.
- **AC3** — When the AC2 fixture plants 25 owed sites under `file`, the unit draining 5 and deferring
  the rest to an ask its `BACKLOG.md` holds, `retrofit.drain-cap` `5` lists no finding and `20` lists
  `carried under the cap`; draining 20 and deferring 5, `20` lists none and `50` lists it; and a
  `deferred:` id the `BACKLOG.md` lacks lists `deferral names no ask` under every cap.
  Red when: a cap value does not move the verdict, or a dangling deferral passes.
- **AC4** — When `check_routed_commits` runs on a planted map-adopting unit whose write set holds six
  baselined keys, claiming one and carrying five with asks naming each `<inventory>:<key>`: under
  `retrofit.claim-on-touch` `claim`, `retrofit.claim-cap` `1` lists no finding and `3` lists
  `carried under the cap`; claiming three, `3` lists none and `5` lists it; claiming five and
  carrying one, `5` lists none.
  Red when: a cap value does not move the verdict.
  fixture: the codebase-map kit's adopter fixture shape, `CODEBASE_MAP_ROOT` the fixture.
- **AC5** — When the AC4 unit claims none and carries five of six: under `carry` it lists one
  `uncarried`; with the sixth carried, none; under `claim` with none carried, six `unclaimed`; under
  `off` it prints `claim off` and no finding.
  Red when: `carry` owes a claim, or `off` owes anything.
- **AC6** — When `python map_diff.py --key-paths` runs in this tree, it prints a `kits` row
  `workflows` whose path is `tools/workflows/`, a `git-hooks` row `pre-commit` whose path is
  `.githooks/pre-commit`, a `gate-legs` row for `run-gates canary` naming its argv script, and the
  `# baseline memory/map/baseline.toml` line, and no `# underived` line; with gov's `gate-legs` row
  taken out of `KEY_PATHS` in a scratch copy, it prints `# underived gate-legs 19`.
  Red when: a baselined inventory has no row and no line says so.
  figure: 19 is DERIVED, the `gate-legs` count `baseline.toml` lists when it runs, 19 at `5f0b11f12`.
- **AC7** — When the AC2 fixture's seed exits 2 under `--sites`, the arm prints `not-installed: its seed
  prints no sites` for that population, lists no finding for it under `hunk`, and the leg's exit is
  the scope arm's alone; with the fixture's `legacy_ledger.py` resolution stubbed to fail, it prints
  one `drain · not-installed` line; and with the population's ledger file absent, `not-seeded`.
  Red when: a population whose scanner gives no lines, or a tree with no ledger, reads clean or owes
  sites.
- **AC8** — When `grep -n "retrofit.drain" gov-builder.agent.md` runs, the bullet names
  `retrofit.drain` and `retrofit.claim-on-touch`; the body after the front matter, CR stripped, is at
  most 4096 bytes; and `.claude/agents/gov-builder.md` carries the same bullet.
  Red when: the builder is not told, or the body passes its ceiling.
- **AC9** — When `python -c` loads `catalogue.toml` with `tomllib`, each of the four `retrofit.*` rows
  this build owns carries `summary` and `usage`, and `grep -c "^retrofit\.\(drain\|drain-cap\|claim-on-touch\|claim-cap\)$"
  unsummarised-keys.txt` prints 0.
  Red when: a row is still unsummarised.
- **AC10** — When `grep -n "retrofit.claim-cap" build-scope.md` runs, the section names the four keys and
  their values; `grep -n "key-paths" tools/codebase-map/README.md` finds the flag.
  Red when: a page is silent.

## 7. Gates

`routed commits name a specced unit` · `routed-commits selftest` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `policy fixtures` · `check-wiring self-test` · `roles catalogue` · `roles render wiring` · `roles render selftest` · `memory hygiene` · `kit/dogfood doc parity` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/memory-tree/routed_commits.py · covers AC2 AC3 AC4 AC5 AC7 · a planted unit per value of each `retrofit.*` key, its sites and keys counted against each cap, staged by draining one fewer site than the cap obliges · none
New arm: tools/codebase-map/selftest.py · covers AC6 · `--key-paths` over a fixture inventory with one row withheld, staged by withholding it · none
New arm: tools/policy/check_policy.py · covers AC1 · reader coverage over the four `retrofit.*` keys once dScopedBuild lands, staged by renaming one literal · none

## 8. Open questions

- **F1 — The ledger keys sites by fields and count, never by line. Where does the `hunk` drain read a
  site's line?** Options: (a) the registration's own `seed` argv with `--sites` appended, a scanner
  convention each converting unit answers, asked of dWitnessedBar, a population whose scanner does not
  yet answer reading `not-installed`; (b) a `sites` field on `[[ledger]]`, an edit of
  TOOL-dWitnessedBar-13's grammar that must land there first; (c) a sibling `[[drain]]` table in each
  kit descriptor, a second declaration of one population; (d) count only, `hunk` read at file grain,
  which fails the clause's two values. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the
  most feature-rich survivor, tie-broken by reuse of the registration's `seed`. Ask for the main loop
  to file, target build dWitnessedBar: "TOOL-dScopedBuild-8's `hunk` drain reads each site's line from
  a `[[ledger]]` population's `seed` argv with `--sites` appended, `<path> TAB <line>` per site, and
  TOOL-dWitnessedBar-13 §4 states no such convention" · accept TOOL-dWitnessedBar-13 §4 states the `--sites` convention for every `drain = "hunk"` registration and each converting unit's scanner answers it, seen on one converted population's `--sites` lines matching its ledger counts. widens: none · relaxes: none
- **F2 — Which paths realize a baselined map key?** Options: (a) a `KEY_PATHS` table in the project
  layer, read by a pure `derive_key_paths` and printed by `map_diff.py --key-paths`; (b) gov's
  `KEYED_ATTRIBUTORS` rows, which move every path of a claimed key off its glob owners in every
  digest; (c) a stand-in reading every key `underived`, which leaves gap-build-05's five kits
  unclaimable. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the most feature-rich survivor. grants: PLAY-dClosedLoop-3 the `--key-paths` flag and the `KEY_PATHS` table of the map's project layer. widens: none · relaxes: none
- **F3 — Where is a carried key recorded?** Options: (a) an ask row of the build's `BACKLOG.md` naming
  `` `<inventory>:<key>` ``; (b) a disposition on the baseline's key, which its grammar has no field
  for; (c) a ledger row, which holds sites, not keys. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the one record the clause names, "carrying them with an ask". widens: none · relaxes: none
- **F4 — What does the cap bound?** Options: (a) what one unit owes, the rest carried, carrying below
  the cap a finding; (b) what one unit may drain at most. RESOLVED (agent, 2026-11-01, delegated): (a), rung 1, `retrofit.md:389-391`, "What it does not drain within the caps, it carries, with a deferral row that names an ask". widens: none · relaxes: none
- **F5 — Does the builder's instruction live in its role body or only in its work order?** Options:
  (a) one bullet in `gov-builder.agent.md`, the work order's legacy slot carrying the counts; (b) the
  slot alone, which TOOL-dFurnishedOrders-11 S3 renders and whose text says counts, not what to do.
  RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the most feature-rich survivor. grants: PLAY-dClosedLoop-3 the builder role's body. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from the packet's Items 8, gap-build-05, retrofit `[drain]`,
  v2:1380-1383, scout B's row for this unit and its interfaces 5 to 8, TOOL-dWitnessedBar-13 §4 and
  TOOL-dFurnishedOrders-11 S3.

## 10. Reuse audit

The seams extended are TOOL-dScopedBuild-9's join frame in `routed_commits.py`, TOOL-dWitnessedBar-13's
ledger reader and registration (read through the memory-tree inline copy), the map's baseline and
extractor table (`tools/codebase-map/map_extractors.py:193`, `map_lib.py:1107`) and the map's CLI
`map_diff.py`; each line verified at `5f0b11f12`. Scout B's row holds there, with one correction: the
catalogue rows run `:1488-1510`, not `:1487-1509`. `python tools/codebase-map/reuse_lookup.py "drain
baselined legacy sites a unit touches and claim baselined map keys"` ranked name stems (`key`,
`claims`, `map_root`, `load_map_tree`, `derive_baseline_additions`, `baseline_units`):
`derive_baseline_additions` derives the keys a branch adds to the baseline, not the paths realizing
a key, so no existing seam fits the key-to-path deriver and S6 adds it beside the extractors whose
table it mirrors; `KEYED_ATTRIBUTORS` is the near miss, rejected in §4.

Recall terms used: `python tools/memory-recall/query.py "how does a unit drain baselined legacy sites it touches and claim baselined map keys" --terms "retrofit drain hunk file off drain-cap claim-on-touch claim-cap ledger baseline dossier carry ask"`.
The query's first run refused at `ensure_cache` with `PermissionError` (WinError 32) on the shared
recall cache; the retry's top hits were scout B's row, the packet, this build's brief and the night
pass instruments, none naming a site-line reader or a key-to-path deriver.
