# TOOL-dDeclaredLoop-14 — the default failure route: the refusal recorded and the frontier returned

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 18 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0099@60eee5d8 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-26 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-33 |

<!-- /gen:spec-records -->

## 1. Goal

A refused item routes by default: the refusal is recorded where history can read it, and `next`
returns the frontier, the unwitnessed items whose needs are witnessed, so a refusal no item's own
routes name still leaves the build somewhere to go. Until dWellOiledMachine lands `next`, its
stand-in is the driver's `--plan`, which prints the frontier beneath its `next:` line (flow-steps'
`[rules]`, `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:28-31`;
P24).

## 2. Scope (IN)

- **S1** — The frontier, `derive_frontier(position)` in `tools/loop/frontier.py`: from unit 7's
  `position`, every item of the build whose witness does not hold and each of whose declared needs
  is witnessed, in the loop definition's order, each with its actor and its instance key. An item
  with no needs is on the frontier until its witness holds. A refused instance stays on it, because
  its witness still does not hold. Observed by AC1, AC2, AC3.
- **S2** — The refusal record, a run-state row written by the driver's `park` with a new kind,
  `refusal`: `<ts> refusal · item <item tag> · step <instance key> · reason <text>`. `refusal` joins
  `PARK_KINDS` (`tools/unattended/unattended.sh:875`) and not `PARK_KINDS_OWED` (:893), because a
  refusal is history the owner is not asked to settle. Observed by AC4.
- **S3** — The recording verb, `unattended.sh --refused <slug> --item <tag> --key <instance key>
  --reason <text>`, which refuses a tag the loop definition does not declare, an empty reason and a
  key not of the shape unit 7's `derive_instance_key` writes, then calls `park`. Observed by AC4, AC5.
- **S4** — `read_refusals(run_state)` in `tools/loop/frontier.py`, the reader of S2's rows, and the
  engine's use of it: the position's `refusals` field lists the build's recorded refusals, and its
  line output prints `refusal — <item tag> · <instance key> · <reason>` for each since the last
  transition and one `frontier — <tag> · <tag> …` line, or `frontier — none`. Observed by AC3, AC6.
- **S5** — The stand-in for `next` returning the frontier: `--plan` prints one `frontier:` line
  directly beneath its `next:` line, the engine's frontier tags space-separated, or `frontier: none`.
  The `next:` line keeps its shapes. Observed by AC7.
- **S6** — Fixture cases of `python tools/loop/frontier.py --fixture`, run by the leg
  `loop frontier fixtures` in `tools/gate-legs.json`. Observed by AC1 to AC6.

## 3. Non-goals (OUT)

- The `next` command: dWellOiledMachine's. The `frontier:` line of `--plan` stands in for it (I26).
- The rework budget a re-dispatch of a refused instance draws on, and the per-item route-back limit:
  units 30 and 32. A refused instance's return to the frontier is the route; what it costs is theirs.
- A refusal its target cannot act on, routed at once to the remedy's actor (the owner's SL-7):
  flow-steps names it beside this rule, and no clause of this unit carries it.
- An item's own declared routes: an outcome a row of unit 13's tables routes is not a default
  failure route, and the engine follows the row.
- A refusal record outside a run with a run-state file: an attended session's refusal is printed and
  journaled by the runlog as today, and the frontier is still returned.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-7` — the `position`: the build's items, their witnesses and their needs, from which the frontier is derived; without it there is no witnessed set to compute it over
- **consumes-from** external — the driver's `park` (`tools/unattended/unattended.sh:12533`), its `PARK_KINDS` and the `--plan` verb, in the tree at base
- **hands-off** `TOOL-dDeclaredLoop-56` — the minors of the round-1 spec audit that land on this unit, ids 11, 26, 29, 37, 39, 41, each a scope item of that unit

## 4. Design

### Evidence

- The rule: "A refusal routes by default: it is recorded, and `next` returns the frontier, the
  unwitnessed items whose needs are witnessed. A re-dispatch of a refused instance draws on the
  build's rework budget" (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:29-31`).
- Today a refusal is a `fail N` line and a number in `RUNLOG_CHECKS`
  (`tools/unattended/unattended.sh:790`), journaled to a machine-local log and routed nowhere.
- `park` appends one line `<ts> <kind> · item <item> · step <step> · reason <reason>` to the
  run-state file and refuses a line end inside any field (`tools/unattended/unattended.sh:12533-12555`);
  `PARK_KINDS` lists the kinds it accepts (:875), `PARK_KINDS_OWED` the ones the close holds for the
  owner (:893).
- The stand-in for `next` is `--plan`'s `next:` line (`tools/unattended/unattended.sh:6131`), which
  unit 7 renders from the engine.

### The frontier

```python
def derive_frontier(position) -> list[dict]:
    """Every item whose witness does not hold and whose needs are all witnessed, in definition order.
    Each entry: {"item": <tag>, "actor": <actor>, "key": <instance key>}."""
```

It reads the position's item witnesses and each item's declared `needs`; it reads no file of its
own, so the engine's read set is the frontier's.

### The refusal row

The `step` field carries the instance key, the one field `park` places between `item` and `reason`,
so the row's grammar is `park`'s and its two existing readers, which take the token between
` · item ` and ` · reason `, read `<item tag> · step <key>` without change. `read_refusals` is the one
reader that splits the step out.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `derive_frontier`, `read_refusals` | function | `tools/loop/frontier.py` |
| `--fixture` | CLI flag | `tools/loop/frontier.py` |
| `refusal` | park kind, a `PARK_KINDS` member | `tools/unattended/unattended.sh` |
| `--refused` | driver verb | `tools/unattended/unattended.sh` |
| `frontier:` | `--plan` output line | `tools/unattended/unattended.sh` |
| `refusals` | `Position` field | `tools/loop/position.py` |
| `loop frontier fixtures` | gate leg | `tools/gate-legs.json` |

### The fixture cases

| Case | Plant | Outcome |
|---|---|---|
| `chain` | items A, B needs A, C needs B; A witnessed | frontier B |
| `parallel` | items A and B with no needs, neither witnessed | frontier A B |
| `refused` | A refused at its key, its witness unheld | A on the frontier, and one `refusal —` line |
| `all-witnessed` | every item witnessed | `frontier — none` |
| `bad-key` | `--refused` with a key not of the instance shape | exit 1, the run-state file unchanged |

### Files touched (estimate)

- `tools/loop/frontier.py`
- `tools/loop/position.py`
- `tools/loop/kit.toml`
- `tools/unattended/unattended.sh`
- `tools/unattended/VERBS.template.md`
- `tools/unattended/PROTOCOL.template.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `tools/gate-legs.json`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **A refusal record kind through the record factory.** One file per refusal in the build folder,
  for a fact the run-state file already holds rows of; and `park` already guards the line grammar.
- **A refused instance kept off the frontier.** Then a single refusal strands the build, which is the
  failure this route exists to prevent; the cost of retrying is the budget's.

## 5. Production-readiness checklist

- security — one new run-state row kind written through `park`, which refuses line ends; the verb
  refuses an undeclared tag and a malformed key.
- perf / scale — the frontier is one pass over the position the engine already built.
- error / empty / loading states — no item unwitnessed prints `frontier — none`; a run with no
  run-state file records nothing and still prints the frontier.
- observability — each refusal is a dated run-state row, and the engine prints every one since the
  last transition.
- risks — a reader that counts parked rows by kind: the close's owed set excludes `refusal`, so no
  close is held by one.
- testing — the five fixture cases and a `--refused` then `--plan` probe.
- migration — none.
- user docs — the parked-kinds table of `tools/unattended/PROTOCOL.template.md` and its dogfood copy
  `memory/guides/UNATTENDED-PROTOCOL.md`, and the `--refused` row of `tools/unattended/VERBS.template.md`.

## 6. Acceptance criteria

- **AC1** — When `python frontier.py --fixture --plant chain` runs, the frontier is exactly B.
  Red when: C, whose need is unwitnessed, is on the frontier, or B is missing.
- **AC2** — When `python frontier.py --fixture --plant parallel` runs, the frontier is A and B.
  Red when: an item with no needs is left off.
- **AC3** — When `python frontier.py --fixture --plant refused` runs, A is on the frontier and one
  `refusal —` line names A, its key and its reason.
  Red when: the refused instance is dropped from the frontier or its refusal is not printed.
- **AC4** — When `bash tools/unattended/unattended.sh --refused <slug> --item <tag> --key <key> --reason probe`
  runs in a fixture run, the run-state file gains one line matching
  `refusal · item <tag> · step <key> · reason probe`.
  Red when: no row is written, or it is written in another grammar.
  fixture: a scratch run under `%TEMP%`; the unattended kit's own suites are waived for this landing
  (README rule 8), so this probe is the observation.
- **AC5** — When `python frontier.py --fixture --plant bad-key` runs, `--refused` exits 1 and the
  run-state file's bytes are unchanged.
  Red when: a malformed key is recorded.
- **AC6** — When `python frontier.py --fixture --plant all-witnessed` runs, it prints
  `frontier — none`.
  Red when: a witnessed item appears, or the line is absent.
- **AC7** — When `bash tools/unattended/unattended.sh --plan <slug>` runs over the `refused` fixture,
  the line after `next:` is `frontier:` naming A.
  Red when: `--plan` prints no frontier.
  fixture: the `refused` fixture repository.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `recall floor` · `recall floor arms` · `memory hygiene`

New arm: tools/loop/frontier.py · covers AC1 AC2 AC3 AC5 AC6 · each `--plant` case, and `chain` red with the needs test removed · none

## 8. Open questions

- **F1 — Where is the refusal recorded?** (a) A run-state row through `park`, kind `refusal`; (b) a
  record-factory kind, one file per refusal; (c) the runlog, as today. (c) is machine-local and no
  committed history reads it, and (b) adds a record kind for a row the run-state file holds. (a)
  reuses the one line writer the driver guards. Recommendation (a). Rung 3. RESOLVED (agent,
  2026-10-24, delegated): (a). grants: PLAY-dClosedLoop-3 the driver's `refusal` park kind and its
  `--refused` verb · widens: none · relaxes: none
- **F2 — Does a refused instance stay on the frontier?** flow-steps says a re-dispatch of a refused
  instance draws on the budget, so a re-dispatch is a route this rule allows. Rung 1. RESOLVED (agent,
  2026-10-24, delegated): it stays; its cost is unit 30's draw. widens: none · relaxes: none
- **F3 — How does the stand-in return the frontier?** (a) A `frontier:` line beneath `next:`; (b) the
  `next:` line rewritten to name the frontier. (b) breaks the shapes three readers match.
  Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-24, delegated): (a). grants:
  PLAY-dClosedLoop-3 the `--plan` output's `frontier:` line · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft.
- rev-2 · 2026-10-24 · §3 · the Edges block gains a hands-off TOOL-dDeclaredLoop-56, the mirror of each unit the round-1 spec audit
  promoted (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md); no scope moved.

## 10. Reuse audit

The seams extended are `park` (`tools/unattended/unattended.sh:12533`), the run-state line writer,
which takes a new kind and no new grammar; `PARK_KINDS` (:875); and unit 7's engine, whose position
the frontier reads and whose line output prints it. For the frontier function itself no seam fits:
`python tools/codebase-map/reuse_lookup.py "list the items whose dependencies are all witnessed after
a refusal"` ranked name-stem hits only (`refusal` in `recall_conf.py`, `DesignRefusal`,
`all_inventories`), none a dependency walk over witnesses. The scout cited the `fail` line and
`RUNLOG_CHECKS` at :790 and the stand-in at :6131; both agreed with source.

Recall terms used: `python tools/memory-recall/query.py "what happens after an item is refused and
what runs next" --terms "refusal recorded frontier next unwitnessed items needs witnessed failure
route re-dispatch budget"`
