# TOOL-dPlacedRequest-10 — a build's scenarios chosen at `entry.place`, every admission predicate re-evaluated by `placement.check`

**Status:** DEFERRED · rev-2 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 17 · advances TOOL-dPlacedRequest-22

**Carries:** cl-dClosedLoop-0128@e0109d47 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-b.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-b.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 |

<!-- /gen:spec-records -->

## 1. Goal

A build runs the scenarios its request was placed under, chosen once at `entry.place` from the request's facts
and checked by code, so a scout that names a scenario whose predicate does not hold is refused before the build
is claimed (the owner's NT-2, "Scout, rechecked (Recommended)",
`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md:104-106` and `:636`).
TOOL-dDeclaredLoop-27 S5 ships the selection function with the request's facts typed on its CLI as a
stand-in; this unit supplies them from the placement and makes the check re-evaluate every predicate.

## 2. Scope (IN)

- **S1** — The scout's return gains two keys (shared interface I19): `scenarios: <tag>+<tag>…`, each scenario
  the orientation scout finds admitted, in the declared order, and `facts: <name>=<value>; …`, the request
  facts it read, each with its evidence row in `evidence:`. `tools/roles/agents/gov-orienter.agent.md`'s
  `returns:` line reads `disposition · reason · evidence · observations · scenarios · facts`, and the body
  paragraph TOOL-dPlacedRequest-4 adds names the two. Observed by AC5.
- **S2** — The `entry` fact is derived, never typed. `derive_entry_fact(disposition)` in
  `tools/loop/placement.py` maps shared interface I20: `new` to `feature`, `amend` to `amendment`, `patch`
  to `patch`, `repeat` to `playbook-run`, the values TOOL-dDeclaredLoop-27 S4's scenarios admit. A return
  whose `facts:` carries an `entry` value that disagrees with its disposition is refused naming both. The
  five other dispositions select no scenario: a return naming scenarios for one of them is refused
  `scenario-not-placed`. Observed by AC3 and AC4.
- **S3** — `placement.check` re-evaluates every predicate. For a block whose disposition selects scenarios,
  `check_placement` (TOOL-dPlacedRequest-4 S5) calls TOOL-dDeclaredLoop-27 S5's `select_scenarios(facts,
  composition)` in `tools/loop/scenario.py` over the block's facts, the derived `entry` among them, and the
  repository's composition (gov's pack and the overlay, no build's recorded changes yet). Each named
  scenario whose predicate fails is a failed fact `scenario-predicate <tag>`; each admitted scenario the
  return did not name is a failed fact `scenario-missing <tag>`; a different order is `scenario-order`.
  Under `placement.check` = `refuse` each refuses and routes back to `entry.place`; under `record` each is
  recorded and the block's `scenarios:` is rewritten to the selection's answer. Observed by AC1 and AC2.
- **S4** — No admitting scenario. When `select_scenarios` admits none, it returns `flow.scenario-default`'s
  value (TOOL-dDeclaredLoop-27 S5, default `scenario.feature`), and `check` writes `scenarios: <tag>
  (default)` into the block, so the build is placed under the default by name. A return naming no scenario
  for such a request passes. Observed by AC6.
- **S5** — The record. The placement record (TOOL-dPlacedRequest-4 S4) gains the keys `scenarios:` and
  `facts:`, and `placement.py record` prints them after `reason:`, the lines TOOL-dPlacedRequest-21's
  `entry.claim` carries into the claim commit and into the build's first transition record as
  ` · scenario=<tag>+<tag>…`, through TOOL-dDeclaredLoop-3 S5's `write_transition --field` with the field
  TOOL-dDeclaredLoop-27 S8 adds. That record is the pin TOOL-dDeclaredLoop-27 S8 lets the build's first
  record stand in for until `entry.claim` lands. Observed by AC7.
- **S6** — The fixture plants of §6, run by `python tools/loop/placement.py --fixture`, under the leg
  TOOL-dPlacedRequest-4 declares. Observed by AC1 to AC7.

## 3. Non-goals (OUT)

- The scenario kind, its rows, `select_scenarios`, composition, conflicts and the per-step switch:
  TOOL-dDeclaredLoop-27's.
- The planner's re-pick at Plan (NT-2's third clause): dRankedPlan's Plan items.
- A repository's own facts beyond `entry` and `design-only`: a predicate naming a fact the scout does not
  supply does not hold, as TOOL-dDeclaredLoop-27's §5 risk line states; this unit adds no fact catalogue.
- The `--fact` CLI of `scenario.py`: kept as the command interface; this unit changes where a placement's
  facts come from, not how the CLI takes them.
- The claim commit and the first transition record's write: TOOL-dPlacedRequest-21's.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-4` — `disposition`, the placement record and `check_placement` this unit extends; without them the predicates have no facts and no verdict line
- **hands-off** `TOOL-dPlacedRequest-3` — `select_scenarios`, the selection `entry.place` names as part of its body and `placement.check` re-runs
- **hands-off** `TOOL-dPlacedRequest-21` — `scenarios`, the checked selection `entry.claim` pins on the claim commit and the build's first transition record
- **hands-off** `TOOL-dPlacedRequest-34` — the round-1 spec audit's minors this unit's code carries, which that unit amends in place as its §2 names

## 4. Design

### The check, in order

```
block := newest placement block for the content key
if block.disposition not in {new, amend, patch, repeat}:
    block.scenarios set  -> refused scenario-not-placed
    else                 -> no scenario check
facts := block.facts + { entry: derive_entry_fact(block.disposition) }
block.facts.entry present and != derived -> refused entry-mismatch <typed> <derived>
want := select_scenarios(facts, composition)        # default when none admits
for tag in block.scenarios - want: refused scenario-predicate <tag>
for tag in want - block.scenarios: refused scenario-missing <tag>
order differs: refused scenario-order
```

Every failed fact is printed on its own line, so a scout's return with two wrong scenarios learns both in one
round trip, and the round trip draws once on the pre-claim budget (TOOL-dPlacedRequest-14).

### Data model

The placement block of TOOL-dPlacedRequest-4 S4, with two keys added:

```
disposition: patch
build: dLandedThing
reason: the landed fix regressed the lander's retry
scenarios: scenario.patch
facts: entry=patch; design-only=false
check: pass
```

`facts` is a `; `-joined list of `name=value` pairs, each name and value one `seg`-shaped word, so no free text
reaches the claim commit through it.

### Inventory

| Minted | Kind |
|---|---|
| `derive_entry_fact` | function, `tools/loop/placement.py` |
| `scenarios`, `facts` | placement record keys and orienter return fields |
| `scenario-predicate`, `scenario-missing`, `scenario-order`, `scenario-not-placed`, `entry-mismatch` | failed-fact words of `check` |

`derive_entry_fact` is put to `python tools/lexicon/lexicon.py --suggest derive_entry_fact --as py.function`
in the build pass.

### Migration

None. A placement block written before this unit carries no `scenarios:`; `check` reads it as naming none and
compares it with the selection, so a pending block re-checked after landing is graded like a new one.

### Rollout

Live at landing. Every gov request places under `scenario.feature` or the scenario its disposition's `entry`
admits, and gov's shipped scenarios activate nothing beyond their own rows (TOOL-dDeclaredLoop-27 Rollout),
so no gov build's flow moves.

### Files touched (estimate)

- `tools/loop/placement.py`: `derive_entry_fact`, the scenario arm of `check_placement`, the two record keys
- `tools/roles/agents/gov-orienter.agent.md`: the `returns:` line and the body paragraph's two fields
- `.claude/agents/gov-orienter.md`: its render, by `tools/roles/render_agents.py`
- `tools/roles/README.md`: the catalogue region re-rendered by `tools/roles/check_roles.py`
- `help/loop.md`: the placement section names how scenarios are chosen and checked

### Alternatives rejected

- **The scout's `entry` fact taken as written.** It is the one fact the disposition already decides, and a
  typed copy is the drift `[derive]` forbids.
- **A table from request labels to scenarios.** NT-2's third option; the owner chose the scout, rechecked.
- **Re-check only the named scenarios.** A missed admitted scenario would run a build without a variant
  its request admits, which the clause's "naming each scenario whose admission predicate holds" forbids.

## 5. Production-readiness checklist

- security — facts are closed-shape words; no free text from the request reaches a record through them.
- perf / scale — one `select_scenarios` call per check over an in-memory composition.
- error / empty / loading states — no admitting scenario places the default by name; an unregistered default
  refuses as TOOL-dDeclaredLoop-27 AC6 states, and that refusal is printed by `check`.
- observability — the block carries the facts read and the scenarios checked; the claim and first
  transition record carry the pin.
- risks — a repository predicate on a fact the scout never supplies never admits; `check` prints the facts
  it evaluated so the gap is visible.
- testing — the fixture plants of AC1 to AC7; the suite arm in §7 at the close.
- migration — none.
- user docs — `help/loop.md`'s placement section names the selection, the default and the re-check.

## 6. Acceptance criteria

- **AC1** — When `python placement.py --fixture --plant predicate-fails` checks a `new` placement whose return
  names `scenario.patch` over the derived fact `entry=feature`, under `placement.check` = `refuse` it exits 1
  printing `scenario-predicate scenario.patch`, and with the return naming `scenario.feature` it passes.
  Red when: the check reads the scout's named scenarios without re-running the predicates, so the planted
  placement passes.
- **AC2** — When `python placement.py --fixture --plant scenario-missing` checks a `new` placement with
  `design-only=true` whose return names only `scenario.feature`, it refuses `scenario-missing
  scenario.design-only`, and under `record` it exits 0 with `scenarios:` rewritten to
  `scenario.feature+scenario.design-only`.
  Red when: an admitted scenario the scout omitted is silently dropped.
- **AC3** — When `python placement.py --fixture --plant entry-mismatch` checks a `new` placement whose facts
  carry `entry=patch`, it refuses naming `entry-mismatch patch feature`.
  Red when: the typed `entry` fact is evaluated in place of the disposition's.
- **AC4** — When `python placement.py --fixture --plant continue-with-scenario` checks a `continue`
  placement naming `scenario.feature`, it refuses `scenario-not-placed`.
  Red when: a scenario is recorded for a request that opens and re-enters no build.
- **AC5** — When `grep -n "scenarios · facts" gov-orienter.agent.md` runs at this unit's commit, it finds the
  `returns:` line, and `python check_roles.py` reports the catalogue region current.
  Red when: the scout's return carries no facts, so the check has nothing to evaluate.
- **AC6** — When `python placement.py --fixture --plant no-admit` checks an `amend` placement in a fixture
  whose pack carries no scenario admitting `entry=amendment`, the block's `scenarios:` reads
  `scenario.feature (default)` and the check passes.
  Red when: a request no scenario admits is placed with an empty scenario list.
- **AC7** — When `python placement.py --fixture --plant claim-lines` runs `record` on a passed `patch` block,
  its output carries the `scenarios:` and `facts:` lines after `reason:`.
  Red when: the checked selection never reaches the claim, so the build's first record reads the default.

## 7. Gates

`roles catalogue` · `roles render selftest` · `check-wiring self-test` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/placement.py · covers AC1 AC2 AC3 AC4 AC6 AC7 · the `loop placement fixtures` leg's plants, its failing case staged by `predicate-fails` with the predicate re-run removed · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that a legal
  status?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:28`. Observation, 2026-10-25: `DRAFT` is
  not in the tuple. Liveness: the tuple would list it if the vocabulary admitted it. RESOLVED (agent,
  2026-10-25, delegated): `OPEN`, rung 2. widens: none · relaxes: none
- **F2 — Is a scout's omitted admitted scenario a refusal, or filled in by the check?** Options: (a) refused
  under `refuse` and filled in under `record`; (b) always filled in; (c) ignored. (b) makes `refuse` weaker
  than its name for one class of wrong return; (c) drops a variant the clause says is named. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 1, the clause's "naming each scenario whose admission predicate holds"
  with `placement.check`'s two values as v2:1171 defines them. widens: none · relaxes: none
- **F3 — Where is the checked selection pinned before a build exists?** Options: (a) in the placement block,
  carried by `entry.claim` into the claim commit and the build's first transition record; (b) a new record
  kind; (c) re-selected at the first transition from the claim's facts. (b) mints a kind no clause names;
  (c) re-derives what was checked, so a pack change between claim and first record moves the variant.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, reusing TOOL-dDeclaredLoop-27 S8's field.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 10, the brief's shared interfaces I19 and I20,
  scout B's row for TOOL-dPlacedRequest-10, the night pass two's point 1 and TOOL-dDeclaredLoop-27 S3 to S8,
  read at base `c63aabbb`.
- rev-2 · 2026-10-25 · §3 · the round-1 spec audit's disposal: hands-off TOOL-dPlacedRequest-34,
  each the mirror of that promoted unit's own edge.

## 10. Reuse audit

The seam is TOOL-dDeclaredLoop-27 S5's `select_scenarios(facts, composition)` in `tools/loop/scenario.py`,
which this unit calls and never re-specs, and TOOL-dPlacedRequest-4's `check_placement`, which it extends.
`python tools/codebase-map/reuse_lookup.py "re-evaluate scenario admission predicates over request facts at
placement"` ranked `extract_run_facts` and `fact` in the unattended kit, run-state readers with no predicate,
so no other selector exists; the parent's module is not built at base, and scout B records the same. Where the
scout record and source disagree: none for this unit, its only code citation being the role file's `returns:`
line, which sits at line 11 (`tools/roles/agents/gov-orienter.agent.md:11`), not :10 as I19 says.
`python tools/memory-recall/query.py "how does placement choose a build's scenarios"` returned scout B's row,
the packet's Items 10 and the brief's row.

Recall terms used: scenario select_scenarios admission predicate facts entry.place placement.check flow.scenario-default orientation scout
