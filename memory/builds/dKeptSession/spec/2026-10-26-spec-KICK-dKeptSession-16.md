# KICK-dKeptSession-16 — the policy namespaces' purposes, reviewed as `memory.map-purpose`'s default says

**Status:** DEFERRED · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 7 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0154@62e72743 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-a.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-a.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-19 KICK-dKeptSession-20 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |

<!-- /gen:spec-records -->

## 1. Goal

No policy namespace declares what it is for: the catalogue gives a key an optional `summary` and
`usage` and gives a namespace nothing, so the project map's policy-namespace nodes carry no purpose
(the project map's CS4-F1, `memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md:657`,
which gives the policy namespace's purpose to dKeptSession). This unit gives each policy namespace a
purpose row in the catalogue, refuses a new namespace that declares none, holds today's purposeless
namespaces on a shrink-only list awaiting review, and reviews them as `memory.map-purpose`'s default,
`review`, says (PM-5, `...-project-map.md:660-668`), reading that key as a stand-in until
dTotalRecall lands it.

## 2. Scope (IN)

- **S1** — The purpose rows. `[[namespace]]` rows in `tools/policy/catalogue.toml`, beside its
  `[[key]]` rows, each `name = "<namespace>"` and `purpose = "<one sentence>"`, read by
  `load_namespaces(kit)` in `tools/policy/policy.py`. `load_catalogue` (GR `policy.py:116`) keeps
  reading `key` alone, so no `[[key]]` reader changes. Observed by AC4.
- **S2** — The population. `derive_policy_namespaces(rows)` in `tools/policy/policy.py`: the sorted
  distinct first segments of the `[[key]]` rows whose `name` carries a dot, a placeholder name's
  literal first segment included (`review.<stage>` is `review`, `budgets.*` is `budgets`). A dotless
  name forms no namespace: its own row's `summary` is its purpose, which `arm_summaries` already
  grades (GR `check_policy.py:265`). Observed by AC6.
- **S3** — The shape check, `check_namespaces(rows, namespaces)` in `tools/policy/policy.py`: a
  `[[namespace]]` row whose `name` is no derived namespace, a `name` written twice, an empty or
  absent `purpose`, and a field other than `name` and `purpose` are each a finding naming the row.
  Observed by AC4.
- **S4** — The awaiting list. `derive_unpurposed(rows, namespaces)` names the derived namespaces no
  `[[namespace]]` row covers, and `tools/policy/unpurposed-namespaces.txt` holds them, written and
  checked through KICK-dKeptSession-19's `write_shrink_list(kit, name, header, derived)` and
  `check_shrink_list(kit, name, derived, compare)` (I7), given this list's file name, its header and
  `derive_unpurposed`'s names, never a fourth hand-rolled list. `policy.py lists
  --check` and `lists --write` (GR `policy.py:1429`) grade and drain it beside `unsummarised-keys.txt`
  against the one compare base they already read. Observed by AC2, AC3.
- **S5** — The rule, `memory.map-purpose` read through the one Python reader `resolve` (I8,
  TOOL-dGroundRules-2 S6). Under `review`: a namespace with no purpose row that the list carries is
  printed `awaiting review` and is no finding; one the list does not carry, or carries above its
  compare base, is a new namespace and is red, naming the namespace and the remedy, a `[[namespace]]`
  row. Observed by AC1, AC2.
- **S6** — The stand-in. `ledger`, `derive` and `refuse` are dTotalRecall's to arm (v2:1377): this
  unit grades every value as `review` and prints one line, `policy purposes: memory.map-purpose
  <value> is dTotalRecall's to arm; graded as review until it lands`, for any value but `review`. A
  refused read takes the catalogue default `review` (GR `catalogue.toml:1470-1473`) with one NOTE,
  as I8 states. Observed by AC5.
- **S7** — The arm `arm_purposes` in `tools/policy/check_policy.py`'s `ARMS` (GR `:737`), its
  population the derived namespaces, announced as `<n> namespace(s), <p> purposed, <a> awaiting
  review`, with `empty = "finding"`, since the catalogue ships in the kit; findings are S3's and S4's.
  Fixture cases `purposes-new`, `purposes-listed`, `purposes-drain`, `purposes-shape` and
  `purposes-map-purpose` in its fixture table. Observed by AC1 to AC5.
- **S8** — The review, done once in this unit's build pass, as PM-5's `review` orders: for each
  listed namespace whose `[[key]]` rows carry a `summary`, a purpose derived from those summaries is
  written as its `[[namespace]]` row and the source rows are cited in the unit's journal record; the
  rest stay listed, and the build run's main loop files one ask in this build's `BACKLOG.md`
  putting them to the owner, each with what was found. `lists --write` then drains the derived ones.
  Observed by AC8.
- **S9** — `help/policy.md`, dGroundRules' page, gains a section: what a namespace purpose is, the
  awaiting list, the refusal of a new namespace, and that `memory.map-purpose` reads as `review`
  until dTotalRecall lands it. Observed by AC7.

## 3. Non-goals (OUT)

- The project map's rendering of a purpose, its `—` for a pending node and its header count:
  dTotalRecall's map, which reads these rows.
- `ledger`, `derive` and `refuse` as behaviours, and the `memory.map-purpose` key's own row and
  reader coverage: dTotalRecall's (the packet's Policy keys, "reads, owned by a later build").
- A purpose per key: the `summary` and `usage` fields and `unsummarised-keys.txt`, dGroundRules'.
- The tag namespace `policy` in `tools/playbook/namespaces.toml` and its `purpose-source`:
  TOOL-dDeclaredLoop-18 and PLAY-dOrderedCharter-22. A policy namespace here is a segment of a key
  name, never a tag namespace row.
- The shrink-only list factory itself: KICK-dKeptSession-19's, called here.

### Edges

- **consumes-from** `KICK-dKeptSession-19` — `write_shrink_list`, with its `check_shrink_list` reader, the factory S4 writes and grades `unpurposed-namespaces.txt` through; without it this list would be a fourth hand-rolled copy
- **consumes-from** external — dGroundRules' policy kit, built on its branch and not landed: `resolve`, `load_catalogue`, `cmd_lists`, `ARMS` and the catalogue's `memory.map-purpose` row, cited at `3c8c4718a`
- **hands-off** `KICK-dKeptSession-44` — the list's ordinal, the batch's S36 and S37 (ids 14, 44)

## 4. Design

### Evidence

- `load_catalogue` returns `doc.get("key", [])` (GR `policy.py:116-120`), so a `[[namespace]]` table
  in the same file is invisible to every `[[key]]` reader, `check_shape` (:261) included.
- The two shrink-only lists today are `check_list`/`write_list` (:991-1031) and the legacy-home list
  (:1251, :1291), both graded by `cmd_lists` (:1429) against one `resolve_compare_base` (:424).
- The catalogue carries `memory.map-purpose`, allowed `review`, `ledger`, `derive`, `refuse`, default
  `review`, owner dTotalRecall (GR `catalogue.toml:1470-1473`), so `resolve` already answers `review`
  from the default.
- PM-5's `review` (`...-project-map.md:660-668`, :868): a new node must declare a purpose; each
  existing node is reviewed by the unit that adds its namespace's purpose field, derived from what it
  carries with the source cited, and a node carrying nothing goes to the owner in one ask per
  namespace.

### Data model

```toml
# tools/policy/catalogue.toml, after the last [[key]] row
[[namespace]]
name = "runtime"
purpose = "How the runtime launches, bounds and records act sessions."
```

```
# unpurposed-namespaces.txt - GENERATED by `python <this kit>/policy.py lists --write`, never edited.
# The policy namespaces with no [[namespace]] row, sorted. SHRINK-ONLY, as unsummarised-keys.txt is.
actions
annotations
...
```

The population is 57 namespaces, PINNED, measured 2026-10-26 over the catalogue at dGroundRules'
`3c8c4718a`; `derive_policy_namespaces` re-derives it on every run, and three of them (`budgets`,
`policy-file`, `runtime`) have a summarised row S8 can derive from.

### The arm's lines

```
policy-check: arm_purposes · 0 finding(s) · 57 namespace(s), 3 purposed, 54 awaiting review
policy purposes: memory.map-purpose refuse is dTotalRecall's to arm; graded as review until it lands
  zz: a new policy namespace declares no purpose: add a [[namespace]] row
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `load_namespaces`, `derive_policy_namespaces`, `check_namespaces`, `derive_unpurposed` | functions, `tools/policy/policy.py` | `py.function`, asked at the pass |
| `arm_purposes` | arm, `tools/policy/check_policy.py` | `py.function`, asked at the pass |
| `[[namespace]]` | catalogue table | none |
| `unpurposed-namespaces.txt` | shrink-only list | none |
| `purposes-new`, `purposes-listed`, `purposes-drain`, `purposes-shape`, `purposes-map-purpose` | fixture cases | none |

### Migration

Additive. The list is seeded by the first `lists --write` with every derived namespace S8 does not
purpose, so no landed tree goes red; a catalogue with no `[[namespace]]` row reads as all awaiting.

### Rollout

Live at landing, in the policy kit's own leg once dGroundRules lands it (`policy check`), and in an
adopter the arm grades the adopter's catalogue copy the same way.

### Files touched (estimate)

- `tools/policy/catalogue.toml`: the `[[namespace]]` rows S8 derives
- `tools/policy/policy.py`: S1 to S6, and `cmd_lists` grading the third list
- `tools/policy/check_policy.py`: `arm_purposes` and its five fixture cases
- `tools/policy/unpurposed-namespaces.txt` (new)
- `tools/policy/kit.toml`: the list in the kit's shipped files
- `help/policy.md`: S9's section

### Alternatives rejected

- **A purpose on the tag namespace row.** `tools/playbook/namespaces.toml` has one `policy` row for
  every key; it cannot say what `runtime.*` is for apart from `review.*`.
- **A separate namespaces file in the policy kit.** A second file read beside the catalogue would
  join the same names twice; one file keeps the population and its purposes in one read.
- **The awaiting set as the catalogue's own purposeless rows**, PLAY-dOrderedCharter-22 S4's form.
  There the existing set is fixed by the design baseline; here a namespace appears whenever a key is
  added, so only a list against a compare base can tell an old purposeless namespace from a new one.

## 5. Production-readiness checklist

- security — no new write path: the list is written only by `lists --write`, the catalogue is
  authored, and nothing reads a value from outside the kit.
- perf / scale — one more TOML table read per arm run; the population is tens of names.
- error / empty / loading states — a catalogue with no dotted key derives 0 namespaces, a finding
  under `empty = "finding"`; an absent list is seeded by `lists --write` and named by `--check`.
- observability — the arm's population line and the stand-in line on every run.
- risks — S8's derived purposes are only as good as three summarised namespaces' rows; the owner ask
  carries the rest.
- testing — S7's five fixture cases, red and green.
- migration — none beyond the seeded list.
- user docs — `help/policy.md`, S9.

## 6. Acceptance criteria

- **AC1** — When `python check_policy.py --fixture purposes-new` runs, a planted key `zz.knob`
  whose namespace `zz` has no `[[namespace]]` row and is on no list at the compare base reds
  `arm_purposes`, naming `zz` and the `[[namespace]]` remedy.
  Red when: the arm admits a new namespace that declares no purpose.
- **AC2** — When `python check_policy.py --fixture purposes-listed` runs, a namespace on
  `unpurposed-namespaces.txt` at the base, with no row, is printed `awaiting review` and the arm is
  green.
  Red when: a listed namespace reds, or is graded without being printed.
- **AC3** — When `python check_policy.py --fixture purposes-drain` gives a listed namespace a row,
  `policy.py lists --check` reds it as stale, `lists --write` drains it, and `--check` then exits 0.
  Red when: a purposed namespace stays listed, or a written list gains a name its base lacked.
- **AC4** — When `python check_policy.py --fixture purposes-shape` plants a `[[namespace]]` row naming
  no key's namespace, a duplicate `name`, an empty `purpose` and an unknown field, `check_namespaces`
  prints four findings, one per row, and no `[[key]]` arm changes its verdict.
  Red when: any of the four passes, or `load_catalogue` reads a `[[namespace]]` row as a key.
- **AC5** — When `python check_policy.py --fixture purposes-map-purpose` sets `memory.map-purpose =
  "refuse"` in the planted policy file, the arm prints the stand-in line naming `refuse` and its
  verdict equals AC2's.
  Red when: another value changes the grading, or changes it silently.
- **AC6** — When `python policy.py lists --check` runs in the policy kit, its line for
  `unpurposed-namespaces.txt` names the base and the count, and the count equals the derived
  namespaces minus the `[[namespace]]` rows.
  Red when: the list and the derivation disagree and the line is green.
  figure: DERIVED at observation, from the catalogue as built.
- **AC7** — When `grep -n "unpurposed-namespaces.txt" policy.md` runs over the help page, it finds
  S9's section, and the section names `memory.map-purpose`.
  Red when: the page does not describe the awaiting list.
- **AC8** — When the build pass ends, `grep -A1 "^\[\[namespace\]\]" catalogue.toml` in the kit
  prints a row for each namespace S8 derived, `budgets`, `policy-file` and `runtime` as the
  catalogue then carries them, the unit's journal record cites each one's source rows, and this
  build's `BACKLOG.md` holds one ask listing the namespaces left awaiting review.
  Red when: a derived purpose cites no source, or a namespace with nothing to derive from is
  purposed without the owner.
  figure: the three summarised namespaces are PINNED at `3c8c4718a`; the build pass re-derives them.

## 7. Gates

`lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The policy kit's own legs, `policy check` and `policy fixtures`, arrive with dGroundRules' landing and
are not in this tree's manifest at base; once landed, the close runs them as the bar does.

New arm: tools/policy/check_policy.py · covers AC1 AC2 AC3 AC4 AC5 · the five `purposes-*` fixture cases, the failing case `purposes-new` staged by a key whose namespace has no row and no base listing · none

## 8. Open questions

- **F1 — Where does a policy namespace's purpose live?** Options: (a) `[[namespace]]` rows in
  `tools/policy/catalogue.toml`; (b) a second file in the policy kit; (c) a field on the tag
  namespace row in `tools/playbook/namespaces.toml`. (c) cannot hold one purpose per key segment, and
  (b) splits one population across two reads. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3,
  the most feature-rich survivor, invisible to every `[[key]]` reader by `load_catalogue`'s own read.
  widens: none · relaxes: none
- **F2 — Is a dotless key a namespace?** Seven catalogue names carry no dot (`preset`, `autonomy`,
  `attendance`, `floor`, `leases`, `placement`, `verdict`), and two of them are also the first
  segment of dotted names. Options: (a) every name's first segment is a namespace; (b) only dotted
  names form one. RESOLVED (agent, 2026-10-26, delegated): (b), rung 3: a dotless key's purpose is
  its own `summary`, already graded, so (a) would ask the same fact twice; `leases` and `verdict`
  stay namespaces through their dotted keys. widens: none · relaxes: none
- **F3 — What does this unit do under a `memory.map-purpose` value other than `review`?** Options:
  (a) grade as `review` and say so; (b) refuse the run; (c) build the other three behaviours. (c)
  is dTotalRecall's surface (the packet's Non-goals), and (b) reds a repository for a value its
  catalogue admits. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, the clause's "reviewed as
  `memory.map-purpose`'s default, `review`, says, a stand-in until dTotalRecall lands the key".
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 16, the project map's CS4-F1 and PM-5,
  v2:1377 and scout A's row for this unit.
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-44` mirrored, the other ends of
  the edges the round-1 spec audit's promoted units declare; no other section moved.

## 10. Reuse audit

The seams extended are dGroundRules' shrink-only list machinery and its arm table, read on its branch
at `3c8c4718a`: `check_list` and `write_list` (`policy.py:991-1031`), which KICK-dKeptSession-19
extracts into `write_shrink_list` and this unit calls; `cmd_lists` (:1429), which grades the third
list against the compare base it already reads; and `ARMS` (`check_policy.py:737`), whose
`arm_summaries` (:265) is the shape `arm_purposes` follows. `python tools/codebase-map/reuse_lookup.py
"declare a purpose for each group of policy keys and hold the missing ones on a shrink-only list"`
ranked name stems only (`key`, `keys`, `read_conf_key`, `declares` in `tools/memory-tree/gotchas.py`,
`load_policy` in `tools/roles/roles_lib.py`); none declares a namespace purpose, because the policy
kit is not on this tree's map at base. Scout A's row agrees with the branch source on every cite; its
count of 60 first segments counts dotless names too, and the dotted population is 57 (§8 F2). The
recall query returned scout A's row and the brief's line for this unit, nothing older.

Recall terms used: `python tools/memory-recall/query.py "where does each policy namespace declare its purpose and who reviews the missing ones" --terms "policy namespace purpose memory.map-purpose review shrink-only list catalogue unsummarised PM-5 CS4-F1"`
