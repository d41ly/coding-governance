# DEPL-dShippedRelease-11 — a dependent's landing held until its parent lands

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 5 · advances DEPL-dShippedRelease-32

**Carries:** cl-dClosedLoop-0421@62dc6590 whole
**Carries:** node:item.deploy.parents
**Carries:** node:policy-key.deps.landing

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-11-reuse-scout-b.md](../build/2026-10-30-build-DEPL-dShippedRelease-11-reuse-scout-b.md) | research | DEPL-dShippedRelease-12 DEPL-dShippedRelease-27 DEPL-dShippedRelease-30 |
| [2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md](../prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |

<!-- /gen:spec-records -->

## 1. Goal

A build that names a parent can land before that parent does, and nothing at Deploy reads the other
build's state: `read_landing_commit` and `check_work_landed` read only the run's own record. This
unit builds `deploy.parents`, the item between `deploy.mandate` and `deploy.land`, which reads each
parent's state and holds, routes or admits the landing as `deps.landing` says.

## 2. Scope (IN)

- **S1** — `read_parent_state(slug, root)` (I7) in `tools/loop/deploy_items.py`, the module pin C1
  names, which this unit, the first of the ten to reach it, creates. It answers `(state, link)`,
  `state` one of `landed`, `held`, `withdrawn`, `superseded` or `absent` and `link` the replacement's
  slug on `superseded`, read at the advertised tip as §4 "The state read" states. Observed by AC1,
  AC2, AC3 and AC4.
- **S2** — `run_deploy_parents(build, root)`, the item's program, and `python
  tools/loop/deploy_items.py parents --build <slug>`, one line per parent and one verdict line, per
  §4 "The program". It reads `deps.landing` by `read_policy_value("deps.landing", root)`, the literal
  call the reader-coverage arm counts. Observed by AC5, AC6, AC7 and AC8.
- **S3** — `hold-until-parent-lands`, the default: every parent `landed` answers `land`; any parent
  `held` or `absent` answers `awaiting`; `withdrawn` answers `route`. Observed by AC5 and AC7.
- **S4** — `test-decides`: a parent not `landed` admits the landing when `check_carries_unlanded`
  finds the build's head holds none of that parent's unlanded commits and the runner-written verdict
  for the head's tree is green (TOOL-dWitnessedBar-4 S1); otherwise it answers as the default does.
  Observed by AC6.
- **S5** — The wait. A `WAIT_KINDS` row `parent-landing` in `tools/runtime/waits.py`
  (TOOL-dWellOiledMachine-18 S7), wake none, default outcome `parent-route`, a `WAIT_OUTCOMES` row
  flagged `holder-only`. `run_deploy_parents` declares one wait per held parent, `on` the build's
  mailbox prefix `refs/gov/mail/<build>/`, where the `landed` notice arrives (KICK-dKeptSession-7 S5),
  the deadline `flow.wait-ceiling`. Its `parent-route` outcome runs `derive_parent_route`
  (TOOL-dDeclaredLoop-15 S6). Observed by AC9.
- **S6** — The link move. On `superseded`, `write_parent_link` rewrites the build's `parents:` front
  matter to the replacement in the run's branch, as flow-steps:77 gives this item, and the read
  repeats on the replacement once, a chain being followed to its end with a cycle refused. Observed
  by AC4.
- **S7** — The item armed. The `[[stand-in]]` row for `item.deploy.parents` leaves
  `tools/loop/loop.toml` (TOOL-dDeclaredLoop-13 S8), and the row carries `deadline =
  "policy.flow.wait-ceiling"` and `on-deadline` for its `awaiting` outcome (TOOL-dDeclaredLoop-33 S5).
  Observed by AC10.
- **S8** — The key. The `deps.landing` row (`tools/policy/catalogue.toml:580`) gains `summary` and
  `usage`, its allowed values and default untouched, and `python tools/policy/policy.py lists --write`
  drains the name from `tools/policy/unsummarised-keys.txt`. Observed by AC11 and AC12.
- **S9** — The docs: `help/loop.md` gains the hold, its five states and the two values. NOT OBSERVED
  as behaviour: prose.

## 3. Non-goals (OUT)

- The landing itself and its queue: DEPL-dShippedRelease-12, which reads `read_parent_state` to drop
  a build not yet admissible.
- The landing record: this unit reads nothing DEPL-dShippedRelease-1 writes (scout B F3).
- `deps.on-parent-withdrawn`'s values and the P1 move: TOOL-dDeclaredLoop-15.
- `deps.coordination` and `deps.early-build`, which gate Build and not the landing:
  KICK-dKeptSession-7.
- A `paused` parent as a sixth state: it reads `held`, which is what flow-steps:436's "unlanded or
  paused" asks.

### Edges

- **hands-off** `DEPL-dShippedRelease-12` — `read_parent_state`, which the queue reads so it never admits a build whose parents have not landed
- **consumes-from** external — TOOL-dDeclaredLoop-12 and -13 (the `item.deploy.parents` row, `[[stand-in]]`), TOOL-dDeclaredLoop-15 (`read_withdrawn_parents`, `derive_parent_route`), TOOL-dDeclaredLoop-33 (`deadline`), TOOL-dWellOiledMachine-18 (`WAIT_KINDS`, `WAIT_OUTCOMES`, `declare_wait`), KICK-dKeptSession-7 S5 (the `landed` notice), TOOL-dTotalRecall-6 (`parse_relations`, `supersedes`), TOOL-dWitnessedBar-4 (the per-tree verdict), each specced and unbuilt at this base, so each is a build-run precondition

## 4. Design

### Evidence

Read at `5d1c82ac`; no product file differs from base `f4597719`.

- `parents:` is parsed at `tools/memory-tree/gen_build_index.py:1212`.
- `read_landing_commit` (`tools/unattended/lib-unattended.sh:1688`) names the commit carrying a run
  record at `phase: LANDING`, and `check_work_landed` (`:1814`) tests a run's own witness on a tip;
  neither reads another build's state.
- The `deps.landing` row is `tools/policy/catalogue.toml:580`, on `unsummarised-keys.txt:49`.
- flow-steps:436 gives the outcomes; flow-roles:228 records the owner's FR-7, hold by default.
- TOOL-dDeclaredLoop-15 S5 reads `phase: ABORTED` from a parent's `RUN.md` as the `withdrawn` stand-in
  and §4 there leaves the hold past `flow.wait-ceiling` to TOOL-dDeclaredLoop-33.
- A build README may declare `supersedes` (TOOL-dTotalRecall-6 S1, `parse_relations`).

### The state read

Read from the advertised tip, fetched first, never from a local branch:

| State | Test, first match wins |
|---|---|
| `absent` | `memory/builds/<slug>/README.md` is not in the tip's tree |
| `landed` | the tip's README reads `**Build status:** CLOSED`, or the tip's run record for the slug reads `phase: LANDING` or later, or a rotated `RUN.LANDED.<hash>.md` sits in its folder |
| `superseded` | a README in the tip's tree declares `supersedes` naming the slug, read through `parse_relations`; `link` is that README's slug. The `merged` terminal reads the same way, by a `patches` or `amends` relation |
| `withdrawn` | `read_withdrawn_parents` names it, or its terminal state is `deferred`, `retired`, `refused` or `answered` (flow-steps:436) |
| `held` | none of the above |

The tip is `git ls-remote` for the default branch through the remote ladder. An unreachable remote
answers `held` with its reason, so a network fault never admits a landing.

### The program

```
deploy.parents — <parent> · <state> · <detail>                       per parent
deploy.parents — land|awaiting|route · <n> parent(s) (deps.landing: <value>)
```

| Outcome | Route on the row |
|---|---|
| `land` | `item.deploy.land` |
| `awaiting` | held; past the deadline as `deps.on-parent-withdrawn` says |
| `route` | `transition`, through P1 where `derive_parent_route` answers a move |

`run_deploy_parents` exits 0 for `land`, 3 for `awaiting` and 4 for `route`, so the verb's caller
never reads a hold as a pass, and 2 on a refused read.

### The `test-decides` read

`check_carries_unlanded(head, parent, tip, root)` resolves the parent's kept branch from its run
record's `run-branch:` fact, as TOOL-dDeclaredLoop-15 §4 does, and asks whether `<tip>..<parent tip>`
and `<tip>..<head>` share a commit. A parent with no such ref cannot be proved clear, so it reads as
carrying: the hold stands.

### The wait

```python
# tools/runtime/waits.py
WAIT_KINDS["parent-landing"] = {"outcome": "parent-route", "wake": None}
WAIT_OUTCOMES["parent-route"] = {"holder-only": True, "run": "<runs derive_parent_route>"}
```

`record` is the parent's slug and `deadline-seconds` the ceiling's hours times 3600. The hold survives
a supervisor's death: the wait is a ref a second node's sweep reads.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `tools/loop/deploy_items.py` | module | none |
| `read_parent_state`, `run_deploy_parents`, `check_carries_unlanded`, `write_parent_link`, `read_policy_value` | functions | `py.function`, each OK by `--suggest` at `5d1c82ac` |
| `parents` | verb of `deploy_items.py` | none |
| `parent-landing`, `parent-route` | wait kind and outcome | none |

`read_policy_value` here is the loop kit's own thin adapter over `policy.py get`, the shape
PLAY-dOrderedCharter-7 §4 and KICK-dKeptSession-7 S6 give theirs, since a kit imports no sibling kit.

### Migration

None. A build with no `parents:` answers `land` with `0 parent(s)`.

### Rollout

Live at landing, under the default `hold-until-parent-lands`.

### Files touched (estimate)

- `tools/loop/deploy_items.py` (new): S1 to S4, S6
- `tools/loop/loop.toml`: S7
- `tools/runtime/waits.py`: S5
- `tools/policy/catalogue.toml`, `tools/policy/unsummarised-keys.txt`: S8
- `help/loop.md`: S9

### Alternatives rejected

- **Reading the landing record for `landed`.** DEPL-dShippedRelease-1 lands after this unit, and the
  record is a claim a reader must check, so the tip's own tree is the witness and the notice the wake.
- **Reading the parent's build lease.** TOOL-dPlacedRequest-16 S2 and pin C4 hold it live until
  `deploy.unlease`, well after the push, so a lease reads a landed parent as unlanded for hours.
- **Extending `derive_parent_reach`.** It answers a three-way `landed`, `reachable`, `unreachable` for
  Build's gate, and tests no withdrawal or supersession; this unit's read is the wider question, so
  that function may call this one once both exist, which is left to a later unit.
- **A new `tools/deploy/` kit**, scout B's home. Pin C1 rejects a new core kit.

## 5. Production-readiness checklist

- security — no new write beyond the run's own branch and a wait ref; a read refusal holds.
- perf / scale — one `ls-remote`, one fetch and one tree read per parent, per run of the item.
- error / empty / loading states — an unreachable remote and a parent with no kept branch each hold,
  never admit; no parents answers `land` and says `0 parent(s)`.
- observability — the per-parent lines and the verdict line; a wait's I29 line.
- risks — the `landed` test reads a tree, so a parent whose README status generator has not run reads
  `held` until its landing's regen; holds are safe and a false `landed` is not.
- testing — the plants of §6, over a fixture with a bare remote.
- migration — none.
- user docs — `help/loop.md`.

## 6. Acceptance criteria

- **AC1** — When `python deploy_items.py --fixture --plant parent-landed` runs, a bare remote whose tip
  holds the parent's `RUN.LANDED.<hash>.md`, `read_parent_state` answers `landed`; with the status read
  from a README reading `**Build status:** CLOSED` and no run record it answers `landed` too.
  Red when: a landing on the tip reads unlanded.
- **AC2** — When `--plant parent-branch-only` runs, the parent's landing commit on a local branch and
  not the advertised tip, it answers `held`.
  Red when: a local tip is read, so a dependent lands past an unpushed parent.
- **AC3** — When `--plant parent-withdrawn` and `--plant parent-deferred` run each answers `withdrawn`;
  `--plant parent-absent` answers `absent`.
  Red when: a build that ended without landing reads held for ever, or a missing folder reads landed.
- **AC4** — When `--plant parent-superseded` runs, a README on the tip declaring `supersedes`, it
  answers `superseded` with the replacement's slug, `write_parent_link` rewrites the fixture's
  `parents:`, and the read follows it; `--plant supersede-cycle` exits 2 naming the cycle.
  Red when: the hold keeps reading a dead parent, or a loop of links spins.
- **AC5** — When `python deploy_items.py parents --build fx` runs on a fixture with one landed parent it
  exits 0 printing `land`; with one held parent it exits 3 printing `awaiting` and `(deps.landing:
  hold-until-parent-lands)`.
  Red when: a held parent admits the landing under the default.
- **AC6** — When a committed `.governance/policy.toml` sets `deps.landing = "test-decides"`: with a held
  parent, a head sharing no parent commit and a green tree verdict it exits 0 printing `land`; with a
  head holding a parent commit it exits 3; with a red verdict it exits 3; with no kept branch it
  exits 3.
  Red when: `test-decides` lands a build carrying its parent's unlanded work, or on a red verdict.
  fixture: the policy kit beside the loop kit; `get` reads the landed revision.
- **AC7** — When a parent reads `withdrawn`, the verb exits 4 under each `deps.landing` value and names
  the `deps.on-parent-withdrawn` route.
  Red when: a withdrawn parent holds rather than routes.
- **AC8** — When `python deploy_items.py parents --build fx` runs on a build with no `parents:` it exits
  0 printing `0 parent(s)`.
  Red when: a build with no parent is held or refused.
- **AC9** — When a held fixture parent lands and `python waits.py sweep` runs, the `parent-landing` wait
  reads `woken` from the `landed` notice; with the deadline passed and no notice it reads `raised` and
  `derive_parent_route` is called once; a second sweep writes nothing.
  Red when: the hold has no wake, or a ceiling raises twice.
  fixture: TOOL-dWellOiledMachine-18 S10's `waits_fixture.py`.
- **AC10** — When `python loop_lib.py --check` and `python loop_table.py check` run on the tree, each
  exits 0 with `item.deploy.parents` no `[[stand-in]]` row and its `deadline` declared.
  Red when: the item stays a stand-in, or a wait row carries no deadline.
- **AC11** — When `python tools/policy/policy.py get deps.landing` runs with no policy file it prints
  `hold-until-parent-lands`; `grep -c "deps.landing" unsummarised-keys.txt` prints 0, and `git grep -c
  'read_policy_value("deps.landing"'` over the loop kit prints at least 1.
  Red when: the row lacks `summary` or `usage`, or no literal reader exists.
- **AC12** — When `check_policy.py`'s value check meets a committed `deps.landing = "loose"`,
  `read_policy_value` raises and the verb exits 2 naming the key.
  Red when: an invalid value grades as the default.

## 7. Gates

`policy fixtures` · `policy check` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_items.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC12 · its `--selftest` running every plant over a bare remote, its failing case `parent-branch-only` read as landed · none
New arm: tools/runtime/waits_fixture.py · covers AC9 · the `parent-landing` case, its failing case a second sweep raising twice · none

## 8. Open questions

- **F1 — What witnesses a parent `landed`.** Options: (a) the advertised tip's own tree, the parent's
  landing commit, the notice being the wake; (b) the landing record; (c) the lease. (b) is a later
  unit's record and (c) stays live past the push under pin C4. RESOLVED (agent, 2026-10-30, delegated):
  (a), rung 3, the brief's reading of scout B F3. widens: none · relaxes: none
- **F2 — What "verdict without the parents' unlanded work" means under `test-decides`.** Options: (a)
  the build's head shares no commit with `<tip>..<parent tip>` and its tree's verdict is green; (b) any
  green verdict; (c) a fresh bar on a tree with the parent's commits removed. (b) lands the parent's
  work inside the dependent, which FR-7 refused. (c) builds a tree nothing else grades. RESOLVED
  (agent, 2026-10-30, delegated): (a), rung 3. widens: none · relaxes: none
- **F3 — What happens past `flow.wait-ceiling`.** Options: (a) a `parent-landing` wait whose outcome is
  `derive_parent_route`, on the declared deadline; (b) a new sweep. TOOL-dWellOiledMachine-18 declares
  one sweep and TOOL-dDeclaredLoop-33 the row's deadline. RESOLVED (agent, 2026-10-30, delegated):
  (a), rung 1, flow-steps:436. widens: none · relaxes: none
- **FACT-QUESTION · F4 — Does a `supersedes` relation exist at a tip for this read to find?** Probe:
  `git grep -n "supersedes" -- memory/builds/*/README.md` at the pass, and TOOL-dTotalRecall-6 S1's row;
  the observation that decides is a tracked README or a fixture declaring the key through
  `parse_relations`; the probe can read negative, since at `5d1c82ac` the tree holds no such key.
  RESOLVED (agent, 2026-10-30, delegated): the fixture of AC4 supplies the positive, and the tree's
  negative reads as no `superseded` parent. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, from the packet's Items 11, flow-steps:436, flow-roles:228, :246,
  v2:1232, scout B's row and fork F3, and the spec brief's I7 and pin C1.

## 10. Reuse audit

The seams extended are TOOL-dWellOiledMachine-18's `WAIT_KINDS` and `WAIT_OUTCOMES`,
TOOL-dDeclaredLoop-15's `read_withdrawn_parents` and `derive_parent_route`, the `parents:` front matter
through `parse_relations`, and KICK-dKeptSession-7's `landed` notice as the wake. `python
tools/codebase-map/reuse_lookup.py "read whether another build has landed on the default branch"`
ranked name-stem hits (`read`, `build_commit`, `read_journal`); the two readers scout B names,
`read_landing_commit` and `check_work_landed`, each read a run's own record, so neither is this read. Scout B's row holds with two corrections: pin C1 replaces
its proposed `tools/deploy/parents.py` with `tools/loop/deploy_items.py`, and `read_parent_state`
returns a link with the state, since `superseded` alone could not move one. Its `:1212` for `parents:`
holds where TOOL-dDeclaredLoop-30's `:1204` does not.

Recall terms used: `python tools/memory-recall/query.py "how does a dependent build's landing wait for its parent" --terms "deps.landing deploy.parents parent state landed notice wait kind hold-until-parent-lands test-decides withdrawn superseded"`
