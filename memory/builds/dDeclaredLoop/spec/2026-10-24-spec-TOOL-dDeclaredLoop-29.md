# TOOL-dDeclaredLoop-29 — an item's upstream field: commitment rows handed on, answered at the return, gating only a measured edge

**Status:** OPEN · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 22 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0114@f3e34c2f whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-readers-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-readers-fix-return.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-25 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-b.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-b.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-readers-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-readers-fix-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-25 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-33 |

<!-- /gen:spec-records -->

## 1. Goal

Every commitment one item establishes reaches the item that must honour it as a row, and that item's
return answers each row `used`, `bypassed` or `not-applicable` with a reason. Today no edge hands its
commitments as rows, and the review finder's schema drops a class silently ("a class with no hit
needs no finding"), which is the drop the night pass two's point 2 measured
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md:179-186`).
The rows' measured value was moving an advisory catch into the step that gates (:170-174), so rows
are recorded on every edge and gate only where a measurement passed.

## 2. Scope (IN)

- **S1** — The `upstream` field on an item row of the loop definition `tools/loop/loop.toml`: a list
  of entries `{ item = "<item tag>", gate = "record" | "measured" }`, `record` the default. It is a
  field of the `kind.item` schema TOOL-dDeclaredLoop-24 registers, declared `shape = "set"` with the
  widening direction that unit's §4 table gives `needs`, widening as it shrinks, since an upstream
  item fewer asks the item to answer less. Observed by
  AC5 and AC9.
- **S2** — The measured edge. An entry at `gate = "measured"` must carry `measured-by`, a path git
  tracks at the loaded revision, and `measured-line`, a literal line that record holds. The loader
  refuses the entry otherwise, naming the item, the upstream item and which half failed. No entry of
  gov's definition ships at `measured`. Observed by AC5.
- **S3** — The establishes block. An item's return declares what it establishes in a
  `## Establishes` section, one row per line, `- <row id> · <kind> · <text>`, the kind from the closed
  set `seam`, `criterion`, `interface`, `fork`, `finding`, `repair` (night pass two, :315-317). A row id
  is one segment of the tag grammar and unique within its return. Observed by AC6.
- **S4** — The rows, `derive_upstream_rows(item, definition, returns)` in the new module
  `tools/loop/upstream.py`, read only through `tools/loop/loop_lib.py` for the definition: one row per
  establishes row of each upstream item's return, its id qualified as `<upstream item>#<row id>`. A
  named upstream item with no return handed, or a return with no `## Establishes` section, refuses
  the hand-on by name. Observed by AC6.
- **S5** — The hand-on. `upstream` becomes a `reads` family: `upstream:rows` joins `READ_KEYS` in
  `tools/roles/roles_lib.py:36-40`, legal only as the optional `upstream:rows?`, and R3 in
  `tools/roles/check_roles.py:198-206` refuses it without the `?` as it refuses a bare `card:reuse`.
  `tools/roles/handoff.py`'s `render_handoff` (:312) takes `--upstream <rows file>` and renders a
  `### upstream:rows` block holding the rows and the row contract: every row id answered exactly once
  in a `## Upstream` section of the return, `- <row id> · used|bypassed|not-applicable · <reason>`,
  and no other id. Observed by AC7 and AC8.
- **S6** — The join at the return, `join_upstream(rows, answers, gate)` in S4's module, classing each
  handed row by its answer: a handed row with no answer is `dropped`, an answered id not handed is `invented`, an id answered
  twice is `doubled`, an answer outside the three words is `bad-answer`, and an answer with an empty
  reason is `no-reason`. On a `measured` edge any of these refuses the return, exit 1, which is the
  item's refusal outcome; on a `record` edge each is recorded as a finding and the return stands.
  Observed by AC1, AC2 and AC4.
- **S7** — A `bypassed` answer is a finding on either edge: the join prints
  `upstream · finding · bypassed · <row id> · <reason>`, and the item's outcome becomes `finding`. An
  item whose `upstream` is non-empty must declare a route for the outcome `finding` in its closed
  outcome set (TOOL-dDeclaredLoop-12's routes), or the loader refuses it. Observed by AC3 and AC9.
- **S8** — The record on every edge. `python tools/loop/upstream.py join --write <slug> <unit id>`
  writes the answered rows and the findings into
  `memory/builds/<slug>/build/<date>-build-<unit id>-upstream-<n>.md`, opening
  `**Serves:** journal <unit id>`. Observed by AC10.
- **S9** — The fixture: `python tools/loop/upstream.py --fixture --plant <case>` builds a scratch
  definition holding one item with one upstream entry on each gate, a role file reading
  `upstream:rows?`, and the planted returns §6 names, each run against its expected observation by
  `--fixture` alone; the leg `loop upstream fixtures` in `tools/gate-legs.json`, argv
  `python {prefix}/loop/upstream.py --fixture`, declared in `tools/loop/kit.toml`. Observed by AC1 to
  AC10.
- **S10** — The page `help/loop.md` (TOOL-dDeclaredLoop-1 S7) gains a section on the `upstream`
  field, the three answers and when an edge gates. Observed by AC11.

## 3. Non-goals (OUT)

- No gov item ships an `upstream` entry at `measured`. The reuse edge, the first to gate, is armed by
  dScopedBuild once its `build.reuse-check` reproduces the measured figures through gov's own route
  (night pass two, :186-191); this unit ships the field, the join and the refusal it gates with.
- No population of gov's own items' `upstream` lists. Which edges hand which commitments is each
  owning build's: dIndexedDesign's reuse scout contract, dScopedBuild's reuse check and closing-review
  rows, dBoundRoles' prompt frame that places the upstream rows in the skeleton (:192-194).
- No per-order return schema rendered by the harness. The row contract is rendered into the task, and
  the join refuses the dropped, invented and doubled rows the per-order schema would (:322-324).
- No commit queue and no trail write: the return's writer is dWellOiledMachine's (:337-338). The
  journal record is the stand-in record of the join.
- No change to a role's `returns` key or to any shipped role's `reads`; a role reads `upstream:rows?`
  when its build places it in an item that names upstream items.
- No edit of `help/roles.md`: it describes the task's parts in prose (`help/roles.md:12-30`) and names
  no `reads` family, so no sentence there goes stale; the loop page carries the field.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-24` — `kind.item`, the item kind's schema this unit adds the `upstream` field to; without its `schema` file the field has no row to sit in and no widening direction to declare
- **hands-off** external — dScopedBuild arms the reuse edge at `measured` with its measurement record; dBoundRoles places the `upstream:rows` block in its prompt frame
- **hands-off** `TOOL-dDeclaredLoop-56` — the minors of the round-1 spec audit that land on this unit, ids 9, 33, 39, each a scope item of that unit

## 4. Design

### Data model

```toml
[[item]]
tag = "item.build.reuse-check"
upstream = [
  { item = "item.design.reuse-scout", gate = "record" },
  { item = "item.design.spec", gate = "measured",
    measured-by = "memory/builds/<slug>/build/<record>.md", measured-line = "## Verdict: CLEAN" },
]
```

The rows file the hand-on reads and the join takes is plain text, one row per line:

```
item.design.reuse-scout#seam-1 · seam · tools/lib/resolve_kit_dir.py resolves a sibling kit
item.design.reuse-scout#must-2 · criterion · no second copy of the remote ladder
```

The return's answer section:

```
## Upstream
- item.design.reuse-scout#seam-1 · used · the renderer calls it at handoff.py:241
- item.design.reuse-scout#must-2 · not-applicable · this unit adds no remote read
```

### The join

`join_upstream(rows, answers, gate)` returns `(verdict, lines)`. It walks the handed ids in order and
the answered ids in order, and every id lands in exactly one of `answered`, `dropped`, `invented` or
`doubled`; an answered row is then graded `bad-answer` or `no-reason` where it fails. Findings print as
`upstream · finding · <class> · <row id> · <reason or the class's sentence>`, answered rows as
`upstream · <row id> · <answer> · <reason>`. `verdict` is `refused` on a `measured` edge with any
finding other than `bypassed`, else `finding` when any finding stands, else `clean`. The CLI exits 1 on
`refused` and 0 otherwise; the item program reads `finding` as the outcome it routes.

### Where each part sits

| Part | Home | Kit |
|---|---|---|
| the field and its load checks (S1, S2, S7) | `tools/loop/upstream.py`, called from `tools/loop/loop_lib.py`'s load | loop |
| the rows and the join (S4, S6, S8) | `tools/loop/upstream.py` | loop |
| the `reads` family and R3 (S5) | `tools/roles/roles_lib.py`, `tools/roles/check_roles.py` | roles |
| the rendered block (S5) | `tools/roles/handoff.py` | roles |

The roles kit never imports the loop kit: the caller derives the rows file with `upstream.py rows`
and hands it to `handoff.py render --upstream`, as it hands `--card`. The loop owns WHAT is handed,
roles WHO is handed it (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-walkthrough.md:119-125`).

### Inventory

| Minted | Kind |
|---|---|
| `upstream`, `gate`, `measured-by`, `measured-line` | item row keys in `tools/loop/loop.toml` |
| `upstream:rows` | `READ_KEYS` member |
| `derive_upstream_rows`, `join_upstream`, `check_upstream_rows` | functions, `tools/loop/upstream.py` |
| `## Establishes`, `## Upstream` | return section headings |
| `upstream` | journal record tail, `<date>-build-<unit id>-upstream-<n>.md` |

Each function name is put to `python tools/lexicon/lexicon.py --suggest <name> --as py.function` in
the build pass before it lands.

### Migration

None. A role that does not read `upstream:rows?` renders byte-identical, and an item with no
`upstream` key loads as before.

### Rollout

Live at landing. With every gov edge at `record`, the only effect on a gov build is the journal record
and the finding route a `bypassed` row takes.

### Files touched (estimate)

- `tools/loop/upstream.py` (new)
- `tools/loop/loop_lib.py`: the load calls `check_upstream_rows`
- the `kind.item` schema file TOOL-dDeclaredLoop-24 names, gaining the `upstream` field
- `tools/roles/roles_lib.py`
- `tools/roles/check_roles.py`
- `tools/roles/handoff.py`
- `tools/roles/README.md`: the `upstream:` family beside `task:`, `card:`, `brief:` and `input:` (:44-49)
- `tools/loop/kit.toml`: the module and the leg declared
- `tools/gate-legs.json`: the leg `loop upstream fixtures`
- `help/loop.md`: the section of S10

### Alternatives rejected

- **A static return schema per role.** Dispatch 133's probe passed a dropped, an invented and a doubled
  row through a static schema; a contract rendered from the order's own row ids refused all three
  (night pass two, :322-324).
- **Gating every edge at once.** The re-derivation found the rows added no union recall on the tuning
  set and their value was where they gate (:170-174); gating an unmeasured edge would refuse work on a
  hypothesis.
- **The handoff deriving the rows itself.** That makes the roles kit read the loop definition and the
  returns, which is the loop's question; the rows file keeps one owner per fact.

## 5. Production-readiness checklist

- security — no new write path but the journal record under the build's own `build/` folder; row text
  is printed, never executed; a row id is one tag segment, so no separator forges a row.
- perf / scale — one pass over the handed and answered ids; no agent.
- error / empty / loading states — an item with no upstream renders and joins nothing; a missing
  return or establishes section refuses the hand-on by name; an unproven `measured` entry refuses the
  load.
- observability — every answer and finding is a line in the journal record.
- risks — a role that ignores the contract on a `record` edge only adds findings; nothing gates until
  a later build arms an edge with its measurement.
- testing — the fixture plants of S9, run by the pass; the suite arm in §7 at the close.
- migration — none, as §4 says.
- user docs — `help/loop.md` gains the field's section and `tools/roles/README.md` the family.

## 6. Acceptance criteria

- **AC1** — When `python upstream.py --fixture --plant drop-gating` runs, a return answering two of
  three rows handed on a `measured` edge exits 1 and prints
  `upstream · finding · dropped · item.fix.scout#must-2`.
  Red when: the join walks only the answered ids, so the dropped row is never seen and the return
  exits 0.
- **AC2** — When `python upstream.py --fixture --plant drop-recorded` runs, the same return on a
  `record` edge exits 0 and prints the same `dropped` finding line.
  Red when: a `record` edge refuses, so an unmeasured edge gates.
- **AC3** — When `python upstream.py --fixture --plant bypassed` runs, a return answering every row,
  one of them `bypassed` with a reason, exits 0 on both edges, prints
  `upstream · finding · bypassed · item.fix.scout#seam-1 · <its reason>` and the verdict `finding`.
  Red when: a `bypassed` row is counted as answered and the verdict reads `clean`.
- **AC4** — When the plants `invented`, `doubled`, `bad-answer` and `no-reason` each run through
  `python upstream.py --fixture --plant <case>` on the `measured` edge, each exits 1 naming its class
  and the row id.
  Red when: `doubled` is read as one answer, the later one winning.
- **AC5** — When `python upstream.py --fixture --plant measured-unproven` loads an entry at
  `gate = "measured"` whose `measured-by` record lacks its `measured-line`, the load refuses naming the
  item, the upstream item and `measured-line`.
  Red when: the gate is read from the declaration alone and the edge gates with no measurement.
- **AC6** — When `python upstream.py --fixture --plant no-establishes` derives rows from an upstream
  return carrying no `## Establishes` section, it refuses the hand-on naming that upstream item.
  Red when: the missing section yields zero rows and the hand-on renders an empty block.
- **AC7** — When the fixture role reading `upstream:rows?` is rendered by
  `python tools/roles/handoff.py render` with `--upstream` naming the fixture's rows file, the task
  carries a `### upstream:rows` block listing every row id and the contract line naming `used`,
  `bypassed` and `not-applicable`.
  Red when: the family is admitted by `READ_KEYS` and the renderer has no source for it, so the key
  refuses as not supplied.
- **AC8** — When `python tools/roles/check_roles.py` grades a scratch roles kit holding one role with
  `reads: upstream:rows` and one with `reads: upstream:other?`, each is an R3 defect naming its key.
  Red when: R3 admits the bare `upstream:rows`, so a role demands rows on items that hand none.
- **AC9** — When `python upstream.py --fixture --plant no-finding-route` loads an item with a
  non-empty `upstream` and no route for the outcome `finding`, the load refuses naming the item.
  Red when: a `bypassed` row produces an outcome nothing routes.
- **AC10** — When `python upstream.py --fixture --plant bypassed` runs with `--write`, the record it
  writes under the fixture build's own folder opens `**Serves:** journal FIX-dUpstream-1` and holds
  every answered row and the finding.
  Red when: only the findings are written, so a clean edge leaves no record.
- **AC11** — When `grep -n "not-applicable" loop.md` runs over the help page at this unit's commit, it
  finds the section naming `upstream`, the three answers and the `measured` gate.
  Red when: the field ships and the page says nothing of it, so an adopter cannot learn the contract.

## 7. Gates

`roles catalogue` · `roles render selftest` · `roles adopter self-test` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/upstream.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC9 AC10 · the `loop upstream fixtures` leg's plants, its failing case staged by `drop-gating` with the join reading only the answered ids · none
New arm: tools/roles/adopt-roles.test.sh · covers AC7 AC8 · the base `READ_KEYS`, which holds no `upstream:` family and so refuses the key · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that a
  legal status?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:28`. Observation,
  2026-10-24: `DRAFT` is not in the tuple, so a `DRAFT` header parses as no header and the unit reads
  MISSING. Liveness: the tuple would list it if the vocabulary admitted it. RESOLVED (agent,
  2026-10-24, delegated): `OPEN`, the token `memory/TEMPLATE-SPEC.md` gives a spec in drafting.
- **F2 — What proves an edge's measurement passed?** Options: (a) a tracked record path plus a literal
  line it must hold; (b) a tracked record path alone; (c) a boolean on the entry. (c) gates on a
  declaration, the actor-typed witness `cl-dClosedLoop-0102` refuses; (b) admits a record that
  measured and failed. RESOLVED (agent, 2026-10-24, delegated): (a), by rung 3, the most
  feature-rich option, since it alone refuses both. widens: none. relaxes: none.
- **F3 — Where are the answered rows recorded?** Options: (a) a `journal` record under the build's
  `build/` folder, a kind `tools/memory-tree/tree_lib.py:406` already admits; (b) a new record kind;
  (c) the trail's commit, which is dWellOiledMachine's commit queue. (b) widens the kinds check 21
  grades and (c) is a later build's surface. RESOLVED (agent, 2026-10-24, delegated): (a), by rung 3,
  the commit queue taking it over when it lands. widens: none. relaxes: none.
- **F4 — Does the roles kit derive the rows?** Options: (a) the caller derives them with the loop kit
  and hands a file; (b) `handoff.py` imports the loop kit. (b) puts the loop's question in the roles
  kit, against the walkthrough's split (:119-125). RESOLVED (agent, 2026-10-24, delegated): (a), by
  rung 1.

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 29, the night pass two's point 2 and its
  storage point's row contract, and the roles kit read at base `ed497191`.
- rev-2 · 2026-10-24 · §3 · the Edges block gains a hands-off TOOL-dDeclaredLoop-56, the mirror of each unit the round-1 spec audit
  promoted (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md); no scope moved.

## 10. Reuse audit

The seams extended are the roles kit's closed `reads` vocabulary, `READ_KEYS`
(`tools/roles/roles_lib.py:36-40`), its R3 grade (`tools/roles/check_roles.py:198-206`), and the
handoff renderer's per-family value resolution (`tools/roles/handoff.py:337-399`), whose bounded
lookups this unit's `--upstream` file joins as one more source; the item row is TOOL-dDeclaredLoop-24's
`kind.item` schema. For `used`, `bypassed` and `not-applicable` no existing seam fits:
`python tools/codebase-map/reuse_lookup.py "answer each handed commitment row used bypassed or not-applicable at an agent return"`
ranked only name stems (`rows`, `row`, `build_commit`, `extract_row`) with no join of handed to
returned ids, and scout B's grep for the two words in `tools/` matched prose only
(`memory/builds/dDeclaredLoop/build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-b.md:24`).
`python tools/memory-recall/query.py` returned the brief's row, the night pass instruments' clause text
and scout B's row; scout B cites `READ_KEYS` at `roles_lib.py:36` and `returns` at :32-33, which agree
with source at base.

Recall terms used: upstream rows used bypassed not-applicable commitment edge gating measurement reuse scout MUST seams
