# TOOL-dWellOiledMachine-53 — admission under `runtime.admission-scope`: the node's plan and hardware ledgers, charged by every project and weighed by the profile's shares

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 0689e7fa · streams tooling · order 38 · advances TOOL-dWellOiledMachine-62

**Carries:** cl-dClosedLoop-0331@df99638c whole
**Carries:** node:policy-key.runtime.admission-scope
**Carries:** node:record-kind.node-ledger

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-a.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-a.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-56 |
| [2026-10-26-build-TOOL-dWellOiledMachine-8-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-8-spec-stage-returns.md) | journal | TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-59 |
| [2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |

<!-- /gen:spec-records -->

## 1. Goal

Admission counts one session's agents, while every project's gov on a node draws on the same plan
and cores unaware of the others, and a limit is seen only after it is hit; with several consumers on
one tight plan, admission that saw only its own share finished 48 to 54% of the work where one shared
ledger with a live reading and reservations sized at p90 finished all of it (gap-rt-40). This unit
keeps two ledgers at the node, outside every repository (I23): the plan's and the hardware's. Every
project the node serves charges both before each launch, whatever its `runtime.admission-scope`,
which narrows only what that project's own admission checks; the ledgers weigh the projects by the
node profile's shares and count free slots against its capacity (v2 P40, cloud-and-scale item 7).

## 2. Scope (IN)

- **S1** — The ledgers (I23), `<home>/ledgers/plan.json` and `<home>/ledgers/hardware.json` at
  `resolve_node_home()` (I5, TOOL-dWellOiledMachine-61), each `schema = "<major>.<minor>"` with
  `LEDGER_SCHEMA_MAJOR` 1. `hardware.json` holds `reservations`, rows `id`, `project`, `slots`,
  `kind`, `act`, `charged-utc`, `expires-utc`, `plan-source`, `plan-age-seconds`; `waiting`, rows
  `project` and `since-utc`; and `projects-seen`, project to last-charge UTC. `plan.json` holds
  `pools`, keyed by pool label, each `allowance-hours`, `source`, `read-utc` and `hold-until`, and
  `reservations`, rows `id`, `project`, `pool` and `hours`. Neither file is in any repository.
  Observed by AC1.
- **S2** — The one local writer, `tools/runtime/ledgers.py`: `charge_reservation(reservation)` and
  `release_reservation(rid)` (I23's spelling), and `write_plan_reading(pool, allowance_hours,
  source, reset_utc=None)`. Each holds `<home>/ledgers/.lock` through `hold_lock`
  (`tools/runtime/locks.py`, TOOL-dWellOiledMachine-12 S2), reads both files whole, writes each
  through a temp file and `os.replace`, and keeps every key a newer minor added. The project is
  never an argument the writer trusts: `derive_project_name(repo)` reads the basename of the
  repository's main worktree, the parent of its git common dir, and a `charge` or `release` naming
  any other project is refused `ledgers — refused · forged · project <given> is not this
  repository's <derived>`, nothing written. Observed by AC4.
- **S3** — The reader, `read_node_ledgers(home=None)`, returning both files or refusing: a file
  whose major exceeds `LEDGER_SCHEMA_MAJOR` is refused `ledgers — refused · <file> · schema <v> is
  newer than <major>`, and the refusal is journaled through `write_journal_line` (I3,
  TOOL-dWellOiledMachine-16) as class `ledger-refused` with the session or act and the file, a class
  this unit adds to `JOURNAL_CLASSES`. An admission whose read is refused admits nothing and
  prints that line, so an older install on a node a newer one has migrated never counts blind. A
  reservation past its `expires-utc` reads as released. Observed by AC5.
- **S4** — The charge at admission. `admit` (I24, TOOL-dWellOiledMachine-45) charges every
  reservation it admits through `charge_reservation` under every scope value, keyed by the id
  `add_reservation` returned, and I22's `remove_reservation` (`tools/runtime/slots.py`,
  TOOL-dWellOiledMachine-9 S4) calls `release_reservation` for the same id.
  A reservation's `slots` is `admit`'s reservation; its `hours` is that times
  `derive_estimate_hours(kind, repo)`: the nearest-rank p90 of the `Wall` field of the act records whose `Item`
  is that item kind (TOOL-dWellOiledMachine-32 S7, read through TOOL-dTotalRecall-9's `record find`)
  once `P90_MIN_ROWS` (10) such rows exist, and `runtime.act-ceiling` hours, read through `resolve`
  (I31), until then; a `trace.cost` of `tokens` or `none` writes no `Wall`, so its estimate stays at
  the ceiling. Its `expires-utc` is the charge plus those hours, a backstop for a holder that dies.
  Each reservation witnesses the pool reading it was admitted against, `plan-source` and
  `plan-age-seconds`. Observed by AC1, AC6.
- **S5** — The scope (`runtime.admission-scope`, `tools/policy/catalogue.toml:486`, values
  `session`, `project`, `node`, `pool`, default `pool`), read through `resolve` at each admission.
  `check_admission_scope(scope, ledgers, reservation, project)` adds, to `admit`'s own room under
  `runtime.agents-in-flight`, the checks its value names, cumulatively: `session` none; `project`
  this project's slots against its cap (S6); `node` every project's slots against the profile's
  `capacity` (`read_node_profile`, I6); `pool` every reservation's hours drawing on the pool the
  act's harness names (the profile's `[[harness]] pool`) against that pool's `allowance-hours`, and
  no admission on a pool whose `hold-until` lies ahead. A pool with no reading is checked against
  nothing and witnessed `plan-source none`. `python ledgers.py checks --scope <value>` prints
  `admission-scope — <value> · checks <list>`. Observed by AC2, AC3.
- **S6** — The shares. `derive_project_caps(capacity, ledgers, profile)`: a project is contending
  when it holds a live reservation or a `waiting` row, which `admit` writes through the writer while
  a call of that project waits; with one contending project its cap is the capacity, and with more
  each one's is `floor(capacity * share / sum of the contending shares)`, at least 1, the shares the
  profile's `[[project]] share`, 1 where absent (TOOL-dWellOiledMachine-61 S3). Observed by AC3.
- **S7** — A project whose gov predates the ledgers. `python ledgers.py status` prints the pools,
  the reservations by project and one `unaccounted — <project>` line for each profile project with
  no `projects-seen` entry, and its count is what the node beat publishes
  (TOOL-dWellOiledMachine-52), never its name. Observed by AC7.
- **S8** — The plan reading at a limit. The supervisor's limit hold (`tools/runtime/supervise.py`,
  TOOL-dWellOiledMachine-6 S9), on a stall line naming a session limit with its reset time, calls
  `write_plan_reading(<the act's pool>, 0, "limit-hold", <reset utc>)`, so every project on the node
  stops admitting on that pool until the reset. Observed by AC2.
- **S9** — The page `help/runtime.md` gains the two ledgers, their home and schema, the four scope
  values and what each checks, the shares, the estimate and `ledgers.py status`. Observed by AC8.

## 3. Non-goals (OUT)

- The FIFO, the hold and the agent-count room: TOOL-dWellOiledMachine-45's `admit`, which this unit
  grows.
- A plan allowance read from a harness account: no source exists at this base, so the reading's
  only writer here is the limit hold (S8); a later reading source calls `write_plan_reading`.
- A plan shared with another machine: the fleet's pool ledger, a later build's (cloud-and-scale
  item 7, "planned as its pool ledger").
- Publishing the free slots and load: TOOL-dWellOiledMachine-52's beat.
- Counting a pre-ledger project by reading its repository's beats: the node knows a project's name
  from its profile, not its path, so S7 reports it unaccounted, the clause's other branch.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-45` — `admit`, which charges both ledgers and asks the scope's checks before it admits
- **consumes-from** `TOOL-dWellOiledMachine-61` — `resolve_node_home` and `read_node_profile`, the ledgers' home and the capacity, shares and pool labels they are weighed by
- **consumes-from** `TOOL-dWellOiledMachine-32` — `act`, the act records whose `Wall` per item kind gives the p90 estimate
- **consumes-from** `TOOL-dWellOiledMachine-16` — `write_journal_line`, with the `ledger-refused` class this unit adds
- **consumes-from** `TOOL-dWellOiledMachine-12` — `hold_lock`, the lock every ledger write holds
- **hands-off** `TOOL-dWellOiledMachine-52` — `charge_reservation` and `read_node_ledgers`, the reservations and pool readings the node beat counts free slots and plan allowance from
- **consumes-from** external — TOOL-dTotalRecall-9's `record find`, which reads the act records

## 4. Design

### Data model

```json
// <node home>/ledgers/hardware.json
{"schema": "1.0",
 "reservations": [{"id": "r-3f2a9c01", "project": "coding-governance", "slots": 3, "kind": "item.build.unit",
                   "act": "act-0a1b2c3d4e5f", "charged-utc": "2026-10-26T21:00:00Z",
                   "expires-utc": "2026-10-26T22:30:00Z", "plan-source": "limit-hold", "plan-age-seconds": 840}],
 "waiting": [{"project": "another-repo", "since-utc": "2026-10-26T21:01:00Z"}],
 "projects-seen": {"coding-governance": "2026-10-26T21:00:00Z"}}

// <node home>/ledgers/plan.json
{"schema": "1.0",
 "pools": {"personal": {"allowance-hours": 0, "source": "limit-hold", "read-utc": "2026-10-26T20:46:00Z",
                        "hold-until": "2026-10-27T02:00:00Z"}},
 "reservations": [{"id": "r-3f2a9c01", "project": "coding-governance", "pool": "personal", "hours": 4.5}]}
```

### What each scope checks

| `runtime.admission-scope` | Charges | Checks before admitting |
|---|---|---|
| `session` | both ledgers | the session's agents in flight (I24's room) |
| `project` | both ledgers | the above, and this project's slots against its cap |
| `node` | both ledgers | the above, and every project's slots against the profile's `capacity` |
| `pool` | both ledgers | the above, and the pool's hours against its allowance and hold |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `charge_reservation`, `release_reservation` | functions, `tools/runtime/ledgers.py` | I23's spelling; `charge` and `release` are no declared verbs, two `VERB_OFFENDER_PIN` arrivals |
| `read_node_ledgers`, `write_plan_reading`, `derive_project_name`, `derive_estimate_hours`, `derive_project_caps`, `check_admission_scope` | functions | `read`, `write`, `derive`, `check`, OK |
| `LEDGER_SCHEMA_MAJOR`, `P90_MIN_ROWS` | constants | none |
| `ledger-refused` | journal class in `JOURNAL_CLASSES` | none |
| `checks`, `status`, `fixture` | `ledgers.py` verbs | none |

### Migration

None: an absent ledger reads as empty, and the first charge creates the home's `ledgers/` directory.
A later minor adds keys the writer keeps; a later major is refused by S3 until the older install
upgrades.

### Files touched (estimate)

- `tools/runtime/ledgers.py` — S1 to S8 (new)
- `tools/runtime/admission.py` — S4's charge, S5's checks, S6's `waiting` rows
- `tools/runtime/slots.py` — S4's release
- `tools/runtime/journal.py` — the `ledger-refused` class
- `tools/runtime/supervise.py` — S8
- `tools/runtime/selftest.py` — the arm in §7
- `.lexicon.conf` — the pin
- `help/runtime.md` — S9

### Alternatives rejected

- **One ledger per repository.** Two projects on one node would each see only their own draw, the
  48 to 54% case gap-rt-40 measured.
- **The scope deciding whether to charge.** A `session`-scoped project would then draw on the plan
  unseen by its neighbours; v2:1217 has every project charge whatever its scope.
- **The project passed by the caller.** Any caller could charge or release in another project's
  name; deriving it from the repository makes a forged reservation a refusal.

## 5. Production-readiness checklist

- security — the ledgers carry counts, hours, act ids, item kinds and project names, no credential and
  no request text; a project writes and releases only its own rows; a newer schema is refused, not
  guessed at.
- perf / scale — two small files read whole under one lock per admission; the p90 reads act records
  once per admission of a kind.
- error / empty / loading states — an absent ledger is empty; a refused read admits nothing; an
  expired reservation reads released.
- observability — the `ledgers —` lines, `status`, the `ledger-refused` journal line and each
  reservation's plan witness.
- risks — the only plan reading is the limit hold until a reading source lands, so `pool` checks an
  allowance only while a hold stands (§3).
- testing — the criteria of §6 and the arm in §7.
- migration — none (§4).
- user docs — `help/runtime.md` (S9).

## 6. Acceptance criteria

Each case runs `python ledgers.py fixture --case <name>` from the runtime kit directory over a scratch
`GOV_NODE_HOME` holding a planted profile and two scratch repositories, `pa` and `pb`, on one node.

- **AC1** — When `--case charge` admits a fan-three call in `pa`, `hardware.json` holds one reservation
  of `slots` 3 for `pa` and `plan.json` one of `hours` 4.5, the act ceiling of 1.5 times three, both
  with the same id, the hardware row carrying `plan-source` and `plan-age-seconds`, and `release`
  empties both.
  Red when: either file is written inside a repository, the two rows differ in id, or the
  reservation carries no plan witness.
- **AC2** — When `--case one-plan` plants `pa` scoped to `session` and `pb` to `pool`, both on pool
  `personal` with a planted reading of 6 hours, and `pa` admits a fan-three call, `pb`'s fan-two call
  waits, 4.5 and 3 hours exceeding 6, and `pa`'s reservation stands in both files; with a limit hold
  planted through `write_plan_reading` until a reset ahead, `pb` admits nothing on the pool until it.
  Red when: `--plant skip-charge-session` leaves `pa`'s call uncharged under `session` and `pb` is
  admitted past the plan's allowance.
- **AC3** — When `--case shares` plants capacity 8 and shares 3 and 1 with both projects contending
  for eight slots, `pa` is admitted 6 and `pb` 2, and `python ledgers.py checks --scope <v>` prints
  `checks session`, `checks session project`, `checks session project node` and `checks session
  project node pool` for the four values.
  Red when: the two projects are admitted 4 and 4, as if their shares were equal, or a scope prints
  another list.
- **AC4** — When `--case forged` runs `ledgers.py charge --project pb` from `pa`, and `ledgers.py
  release <id>` from `pa` on a reservation of `pb`, each exits 2 printing `forged` and both files are
  unchanged.
  Red when: either write lands.
- **AC5** — When `--case schema` plants `hardware.json` at `schema = "2.0"` and admits a call from
  `pa`, it prints `ledgers — refused · hardware.json · schema 2.0 is newer than 1`, admits nothing,
  and `runtime.log` gains one `class=ledger-refused` line.
  Red when: the older install admits, or no journal line is written.
- **AC6** — When `--case estimate` plants ten act records of item kind `item.build.unit` whose `Wall`
  runs 1 to 10 minutes, a fan-one reservation of that kind carries `hours` 0.15, the nearest-rank p90
  of 9 minutes; with nine records it carries the act ceiling, 1.5.
  figure: DERIVED, the p90 of the planted walls at observation time.
  Red when: the estimate moves off the ceiling below ten rows, or ignores the rows at ten.
- **AC7** — When `--case unaccounted` plants a profile naming a third project that never charges,
  `python ledgers.py status` prints `unaccounted — pc`.
  Red when: the third project is not reported.
- **AC8** — When `grep -n "runtime.admission-scope" runtime.md` runs over the runtime help page, it
  names the four values and the `ledgers.py status` verb.
  Red when: a value or the verb is missing.

## 7. Gates

`lexicon naming predicates` · `govkit acceptance matrix` · `straggler-guard arms` · `memory hygiene`

New arm: tools/runtime/selftest.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 · each fixture case, staged by its planted break: a charge skipped under `session`, equal caps, a forged project admitted, a newer major read, the estimate ignoring the rows · none

## 8. Open questions

- **F1 — What project name does a repository charge under?** Options: (a) the basename of the main
  worktree, matched to the profile's `[[project]] name`; (b) a project key set in each repository's
  policy; (c) the remote URL. (b) is a second carrier of the profile's name that can disagree with
  it, and (c) puts a remote into the node ledgers and the beat's neighbourhood. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3: one fact, read from where the repository already is, with a
  repository the profile lacks charged at share 1 and listed by `status`. widens: none · relaxes:
  none
- **F2 — How many act records make a p90?** Options: (a) ten; (b) any one; (c) thirty. (b) sizes
  every reservation of a kind by its first run, and (c) leaves most kinds at the ceiling for weeks.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, `P90_MIN_ROWS` declared once in
  `ledgers.py`. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.

## 10. Reuse audit

The seams extended: the node home and profile (`resolve_node_home`, `read_node_profile`,
TOOL-dWellOiledMachine-61); run-gates' move of its turnstile from the repository to a host directory
because three repositories starved each other (`tools/run-gates/run-gates.sh:1474-1479`), the
precedent for ledgers outside any one repository; `hold_lock` (TOOL-dWellOiledMachine-12); the act
records' `Wall` (TOOL-dWellOiledMachine-32); the journal writer (TOOL-dWellOiledMachine-16).
`python tools/codebase-map/reuse_lookup.py "a ledger outside the repository shared by every project
on one node with reservations and shares"` ranked `scan_shared_index_overlaps`, `load_project_layer`,
`resolve_projects_root` and `resolve_shared_records`, name-stem neighbours, none a ledger: no existing
seam fits the ledgers themselves. Scout A's row holds against source; its `~/.gov/` home is spelled
here as the node home I5 fixes.

Recall terms used: `python tools/memory-recall/query.py "where are the plan and hardware ledgers a
node's projects share" --terms "node ledger plan hardware reservation admission scope shares capacity
schema version p90 act ceiling"`
