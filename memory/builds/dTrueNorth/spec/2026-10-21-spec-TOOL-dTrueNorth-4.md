# TOOL-dTrueNorth-4 — the deviation record, its population from history, and its join at the commit and at the close

**Status:** OPEN · rev-3 · 2026-10-21 · node d · Tier-2 · base 271aa59d · streams tooling · order 3

**Carries:** cl-dClosedLoop-0004@c374ccd0 whole
**Carries:** node:record-kind.deviation

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-21-prompt-TOOL-dTrueNorth-1-spec-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-1-spec-brief.md) | research | TOOL-dTrueNorth-1 TOOL-dTrueNorth-2 TOOL-dTrueNorth-3 TOOL-dTrueNorth-5 TOOL-dTrueNorth-6 TOOL-dTrueNorth-7 |
| [2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md](../reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md) | spec-audit | TOOL-dTrueNorth-1 TOOL-dTrueNorth-2 TOOL-dTrueNorth-3 TOOL-dTrueNorth-5 TOOL-dTrueNorth-6 TOOL-dTrueNorth-7 |

<!-- /gen:spec-records -->

## 1. Goal

Every departure from the frozen design, or from a spec once its code has started, becomes a typed
deviation record the product reads, and a population computed from git history is joined to those
records at the commit and at the close, so a spec and its code can no longer move together with no
reason or approver any check reads (`gap-build-07`). This is the product successor of the bootstrap
instrument `deviations.py`'s population and join, and of no other part of it.

## 2. Scope (IN)

- **S1** — The record grammar (brief S6). A record is
  `<MEMORY_ROOT>/builds/<build>/build/<date>-build-<unit id>-deviation-<n>.md`, kept in the
  departing build's `build/` folder, `<n>` unique within its build, its id the file's stem. Its
  fields are bold-key bullets in the instrument's form (`deviations.py:123`): `**Departs from:**`,
  `**Hand-off:**`, `**Before:**`, `**After:**`, `**Cause:**`, `**Reason:**`, `**Evidence:**`,
  `**Risk:**`, `**Approver:**` (the approver and where the approval is recorded), `**Follow-through:**`
  and `**Caused-by:**` (the id of what caused it, the clause's `caused-by` field, P35), with
  `**Bound:**`, `**Tier:**` and `**Surface:**` optional. `read_record` in
  `tools/memory-tree/deviation_join.py` parses one and names each malformed field. Observed by AC7.
- **S2** — The kind. `deviation` joins `RECORD_KIND_TOKENS` (`tools/memory-tree/gen_build_index.py:550`),
  so check 21 grades `**Serves:** deviation <unit id>`. The binding is joined to the file name both
  ways inside `read_bindings`: a file named `…-deviation-<n>.md` under a `build/` folder must carry
  kind `deviation`, and a `deviation` record must be so named, each mismatch an `A` row with its
  reason. The kind list in `tools/memory-tree/HYGIENE.template.md:574` gains the kind, and
  `memory/HYGIENE.md` is re-rendered from it. Observed by AC8 and AC9.
- **S3** — The three other spellings of the kind list point at `memory/HYGIENE.md`, "Record
  bindings", in place of their own enumeration: `WIRE-INTO-PROJECT.md:418`,
  `tools/memory-tree/adopt-memory-tree.sh:724` and
  `memory/gotchas/record-without-serves-or-with-a-round-counter.md:28`. Observed by AC9.
- **S4** — The population, computed from history and never declared, over the chain builds' specs,
  the chain builds being the Build column of `DESIGN_VIEW` (brief S2). Six arms, each member carrying
  an address, its hand-off and its departing commit:
  - each spec revision that is not an ancestor of its unit's first attributed pass, addressed
    `<unit>@rev-N` with N the header revision it changed;
  - each spec revision that is not an ancestor of the commit adding the newest `spec-audit` record
    whose `**Serves:**` pins `<unit>@rev-N` (brief S7), addressed `<unit>@rev-N`;
  - each `amended rev-N` ledger line under an `**Evidences:** <unit>` block of a `journal` record,
    addressed `<unit>@rev-<N-1>` (the clause's AMENDED acceptance line);
  - each divergence hand-back, a `prompts/` record whose `### Goal` opens `DIVERGENCE:`;
  - each rescope row of a chain build's `RUN.md` or rotated `RUN.*.md` but a `defer` row, as
    `deviations.py:383-404` reads them;
  - each clause-hash move: a clause of `DESIGN_RECORD`'s `[chain]` whose hash at HEAD differs from
    its hash at `DESIGN_BASELINE`, or that is new or absent at HEAD, and a `Baseline:` line that
    differs from `DESIGN_BASELINE`, listed first and joined by no record.
  Both revision arms exempt a revision whose text is unchanged once its `**Status:**` line and every
  generated region are stripped (P0.1 row 8a), the strip being `GEN_REGION_AWK` read from
  `tools/unattended/lib-unattended.sh:1045`, never copied. Observed by AC1, AC2, AC3, AC5 and AC6.
- **S5** — The first attributed pass, through the routed-commit attribution: the oldest commit, by
  committer date, among the commits `read_routed_commits` (`tools/memory-tree/routed_commits.py:219`)
  returns for HEAD that either carry a `Pass:` trailer naming the unit (`Pass: none` names none) or
  carry no `Pass:` trailer, name the unit as a whole token of the subject and write a path under
  `ROUTED_PATHS`. Observed by AC1 and AC6.
- **S6** — The join and the approver. A member joins the record departing from its address, an `add`
  member the record whose `**Follow-through:**` is `new unit <id>`. Each record's approver is graded
  under one of two approval values, `author-recorded` by default, the chain's value (deviation-1),
  or `by-risk`, the table final-questions `[deviation]` sets
  (`final-questions.md:191-194`). Both refuse an approver opening with no role the grammar names,
  and an owner approver citing no decision id whose row `memory/DECISIONS.md` holds at
  `origin/main` and names the record's departed clause or its new unit (P0.1 row 6). `by-risk` also
  refuses a role below its risk class. Observed by AC4, AC6 and AC14.
- **S7** — The join at the commit and at the close, hosted in `routed_commits.py` over the two
  populations it already grades: at the commit, its RANGE half (`$GATE_PUSH_BASE..HEAD`), each member
  whose departing commit lies in the range must be joined by a record present in that commit's tree;
  at the close, its WHOLE half, every member at HEAD is joined and every record's approver graded.
  The host runs the chain's gate value, `report`: it lists and never changes the leg's exit, so the
  leg exits as it does today. Observed by AC10 and AC11.
- **S8** — The two policies on `deviation_join.py`'s own CLI, `--policy report|refuse` (default
  `report`) and `--approval author-recorded|by-risk` (default `author-recorded`), and the two states
  that are not a verdict: the join is OFF, one line and no history read, unless the three S2 keys
  `DESIGN_RECORD`, `DESIGN_BASELINE` and `DESIGN_VIEW` are all declared; and it exits 2, nothing
  measured, when the declared `DESIGN_BASELINE` names no commit and no chain-build spec exists. The
  spec population is `scan_chain_specs` over the view's builds with an empty cutoff, every chain-build
  spec as the instrument reads them, so this unit reads no date key (`SPEC_CARRIES_CUTOFF` has one
  reader, `read_cutoff_key`). Observed by AC12 and AC13.
- **S9** — The `[chain]` row reader, one parser: `read_chain_clauses` joins
  `tools/memory-tree/design_lib.py` beside `derive_clause_hash`, returning
  `(build, clause id, text, hash8)` in row order as `deviations.py:159-170` reads them. The clause-move arm and TOOL-dTrueNorth-6's
  generator both import it. Observed by AC6 (the `clause` and `baseline` plants).
- **S10** — The two deviation records this unit's spec owes, deviation-1 and deviation-4, written
  verbatim from §4 "### The records this unit owes" into `memory/builds/dTrueNorth/build/`, in this
  spec's commit or, failing that, this unit's build pass. Observed by AC14.
- **S11** — The docs: the `tools/memory-tree/README.md` "What's here" rows for `deviation_join.py`
  and `routed_commits.py`, and a "Deviation records" paragraph in `HYGIENE.template.md`'s "Record
  bindings" naming the grammar of S1 and the two values of S6. Observed by AC9.

## 3. Non-goals (OUT)

- The departures report, `deviations.py --report`. It stays the instrument's and keeps running at
  each close (execution plan, the retirement table); this unit ports the population and the join only.
- The as-built view and any reading of `**Follow-through:**` rows into it: TOOL-dTrueNorth-6.
- The audit pin's grammar and writer, and check 21's grading of it: TOOL-dTrueNorth-5. This unit
  reads the pin.
- A refusing gate. `refuse` is reachable on `deviation_join.py`'s CLI and in its fixtures; the leg
  host runs `report`, the chain's value (`PLAY-dClosedLoop-4`), until dScopedBuild's `deviation.gate`
  lands and re-points it.
- The risk classifier and the approval route: the risk class is read from the record, a stand-in
  until dOrderedCharter's classifier and dDeclaredLoop's `deviation.approval` land.
- The by-risk table's "re-audit at the new revision" for the spec writer. A re-audit moves the audit
  pin, which takes the revision out of the population, so the pin arm already reads it.
- Rewriting another unit's record to the grammar beyond its kind (§4 "### Migration"); a grammar
  finding on one is listed under `report` for its writer.
- Any edit under `tools/unattended/`, of v2, of the instruments, of the as-built view file or of the
  packet. A new gate leg: both joins live in an existing leg.
- A help page under `help/`: §5 user docs says why.

### Edges

- **consumes-from** `TOOL-dTrueNorth-1` — `design_lib.py`: `derive_clause_hash`, `read_design_view`, whose Build column names the chain builds, `scan_chain_specs` and `DESIGN_KEYS`; without them the population has no chain builds, no chain-build specs and no clause hashes
- **consumes-from** `TOOL-dTrueNorth-5` — the `pins` map each `read_bindings` record gains, the `@rev-N` audit pin per id (brief S7); without it the pinned-revision arm has no pin to read and every unit prints under "no audit pin"
- **hands-off** `TOOL-dTrueNorth-6` — the record reader, `read_record`, with its `**After:**` and `**Follow-through:**` values, and `read_chain_clauses` in `design_lib.py`, which the as-built generator renders from
- **hands-off** external — dScopedBuild's `deviation.gate`, dDeclaredLoop's `deviation.approval` and dOrderedCharter's classifier re-point the stand-in values and the risk reading this unit ships
- **hands-off** `TOOL-dTrueNorth-10` — deviation-2 and deviation-3, written in the grammar `read_record` grades (the round-1 spec audit's id 12)
- **hands-off** `TOOL-dTrueNorth-12` — `deviation_join.py`'s strip read and fixture design, made reachable and hermetic for the shipped self-test (the round-1 spec audit's id 30)
- **hands-off** `TOOL-dTrueNorth-16` — `read_population`, `read_record` and the fixture's plants, which that unit amends for the round-1 spec audit's ids 5, 20, 21, 46 and 47
- **hands-off** `TOOL-dTrueNorth-17` — the order-3 transition: if this pass lands after `TOOL-dTrueNorth-6`, it runs `gen_build_index.py --write` and stages `DESIGN_VIEW` over deviation-1 and deviation-4 in its own commit, the view on its `--dispatch --writes` (the round-2 spec audit's id 1)
- **hands-off** `TOOL-dTrueNorth-18` — `read_record`'s optional `**Supersedes:**` field, which that unit adds to order two amends of one clause (the round-2 spec audit's id 34)

## 4. Design

### Data model

The record, one file, its fields `- **<Key>:** <value>` on one line each, read with the instrument's
field regex (`deviations.py:123`) so the two read one value:

| Field | Closed set or shape |
|---|---|
| `**Departs from:**` | `<clause id>@<hash8>`, `<unit>@rev-N`, or a build slug for a design-to-spec add; optional backticks; an optional ` [<section>]` tail is cut before the join |
| `**Hand-off:**` | `design-to-spec` · `design-revised` · `spec-revised` · `spec-to-code` · `code-to-record` |
| `**Before:**`, `**After:**` | non-empty text, one line; `**After:**` is the clause's whole text as built on an `amends` record |
| `**Cause:**` | `design defect` · `owner ruling` · `builder discovery` · `review finding` · `external` |
| `**Reason:**`, `**Evidence:**` | non-empty text |
| `**Risk:**` | `editorial` · `additive` · `stricter` · `loosening` · `breaking` |
| `**Approver:**` | opens with `author`, `spec writer` or `owner`, then where the approval is recorded |
| `**Follow-through:**` | `amends <clause id>@<hash8>` · `supersedes <clause id>@<hash8> by <clause id>` · `new unit <id>` · `gap <key>` · `ask <id>` · `usage <key>`, unquoted |
| `**Caused-by:**` | one id: a decision, a record, an ask or a unit |
| `**Bound:**`, `**Tier:**`, `**Surface:**` | optional; a `relaxes:` choice's record carries the first two, a `widens:` choice's the third |

A member is `{kind, build, address, hand, departing sha, what}`. The by-risk table, as
final-questions `[deviation]` states it:

| Risk, or cause | Least approver |
|---|---|
| `editorial` | `author` |
| `additive`, `stricter` | `spec writer` |
| `loosening`, `breaking` | `owner` |
| cause `owner ruling`, whatever the risk | `owner` |

The roles rank `author` < `spec writer` < `owner`; an approver meets a class when its role ranks at
or above the class's.

### The module, `tools/memory-tree/deviation_join.py`

One core, with `routed_commits.py` its only host. Its parts, each named so the host and
TOOL-dTrueNorth-6 call one function:

- `read_record(path, text)` → the record's fields and the list of its malformed fields by name,
  graded against the filename grammar, the closed sets above, the one-line `**After:**`, and an
  `amends` or `supersedes` row naming a clause at an eight-hex hash. The fields are returned whatever
  the list holds, so the as-built view reads a malformed record as the instrument does.
- `read_records(root, conf)` → every file matching `<MEMORY_ROOT>/builds/*/build/*-deviation-*.md`,
  the instrument's glob, so TOOL-dTrueNorth-6 counts the population the instrument counts, each
  parsed, plus a finding for a misnamed file and for a `<n>` two files of one build share.
- `read_population(root, conf, commits)` → the members of S4, `commits` being the WHOLE list
  `read_routed_commits` already read, so the host reads history once. The arms port
  `deviations.py:279-468` with three changes: the chain builds come from `DESIGN_VIEW` through
  `design_lib`, the pin from `DESIGN_BASELINE`, and the product-path test of the first pass is
  `test_routed_path` over `ROUTED_PATHS` (`routed_commits.py:172`). The audit pins come from
  `gen_build_index.read_bindings`, each `spec-audit` record's `pins` map (`{id: N}`), which
  TOOL-dTrueNorth-5 adds there; this unit parses no `**Serves:**` line itself.
- `derive_joins(members, records)` and `check_approvers(records, rows, approval)`, porting
  `deviations.py:477-536`, with the by-risk compare added under `by-risk` only.
- `check_commit_join(root, members, records, range_shas)` → for each member whose departing commit is
  in `range_shas`, the joining record's path asked of that commit's tree in ONE
  `git cat-file --batch-check` call, as `routed_commits.py:283-289` batches its own; a record absent
  there is "recorded after its departure at <sha8>".
- `render_lines(...)` → the summary line and one line per member, refused record and malformed file,
  every line prefixed `deviation:`.

The departing commit per arm: the revising commit; the commit adding the ledger line, the rescope row
or the hand-back record (`git log --reverse -S`, as `deviations.py:378-380` finds a row's commit);
and for a clause move, the oldest commit on HEAD's history since `DESIGN_BASELINE` touching
`DESIGN_RECORD` at which that clause's hash differs from the pin. The moved `Baseline:` line has no
departing commit and no record, and is listed first.

Its CLI, from the worktree root:

```
python3 tools/memory-tree/deviation_join.py [--policy report|refuse] [--approval author-recorded|by-risk] [--range <a>..<b>]
python3 tools/memory-tree/deviation_join.py --fixture [--plant <case>] [--policy …] [--approval …]
python3 tools/memory-tree/deviation_join.py [--fixture [--plant <case>]] --host routed-commits
python3 tools/memory-tree/deviation_join.py --selftest
```

With no `--range` the commit join reads every commit. `--host routed-commits` calls
`routed_commits.check_routed_commits` in-process and prints the host's lines: over the fixture, with
`GATE_PUSH_BASE` set to the fixture's base in the environment dict it passes; over the current tree,
with the process environment. It is the probe of the host's code a build pass may run, since the
host's own leg is not on the builder's gate list (`tools/roles/house/policy.toml`). Exit 0 green or
`report`, 1 on any finding under `refuse`, 2 nothing measured.

### The host, `routed_commits.py`

`check_routed_commits` (`routed_commits.py:233-319`) calls the core once per population it already
grades (`:249-251`): the RANGE half runs the commit join over the range's shas; the WHOLE half runs
the close join and the commit join over every sha. Its lines join the leg's output under the
`routed-commits: deviation …` prefix. The leg's exit code is unchanged under `report`; a declared
design whose pin cannot be read raises the host's `Refusal`, exit 2, as an unarmed conf does there.
Off, the arm makes no git call, so the self-test fixtures, which declare no design keys, keep their
spawn counts. Armed, the arm's spawns grow with the chain-build specs' revisions, and the docstring
and the README row say so beside "Constant git spawns".

### The fixture

A temporary git repository, ported from `deviations.py:849-1191`: a conf declaring the fixture
family `FIX`, `ROUTED_PATHS="tools/"` and the three S2 keys, with
`DESIGN_BASELINE` the fixture's pin commit, written in a second commit; the tree's `DESIGN_RECORD`
`[chain]` section and its `DESIGN_VIEW` file copied in whole, never a synthetic chain; the decision
rows of `deviations.py:876-885`. Its base history joins every member, and each base record's approver
meets its risk under both approval values. The instrument's base records that serve only its report
plants, the ER:240 and ER:328 choices, are not ported, because the report mode is not. Every plant is
its own unit, clause or row, so plants compose. Plants: the instrument's 26 (`deviations.py:851-854`)
and `pass-revision`, `below-risk`, `owner-cause`, `status-only`, `malformed-field`, `malformed-risk`,
`malformed-follow`, `duplicate-n`, `record-late` and `unmeasured`.

### The records this unit owes

Written byte for byte beside this spec, in this spec's commit, the clause's "written in the departing
unit's own commit"; a spec commit that lacks them is followed by this unit's build pass writing them in
its own commit. Both amend `cl-dClosedLoop-0004` with an `**After:**` that is the clause's text
unchanged, as deviation-3 does for `cl-dClosedLoop-0002` (TOOL-dTrueNorth-2, §8 F3): the view's row
cites the record and the clause's hash stays `c374ccd0`, the pin `carries.py` reads at the Design exit
and the product join reads in the view (§8 F6). Each departure is stated in its `**Reason:**`. The
view applies one row per clause and the later file by path supplies the citation, so the row cites
deviation-4.

`memory/builds/dTrueNorth/build/2026-10-21-build-TOOL-dTrueNorth-4-deviation-1.md`:

```markdown
# TOOL-dTrueNorth-4 deviation 1 — the stand-in join reads the chain's values

**Serves:** deviation TOOL-dTrueNorth-4

- **Departs from:** `cl-dClosedLoop-0004@c374ccd0` [approval]
- **Hand-off:** design-to-spec
- **Before:** the deviation record, its kind joined to check 21's kinds, kept in its departing build's `build/` folder as the owner's word on the open readings sets, written in the departing unit's own commit, and its fields its id, the hand-off, the departure's address, before and after, cause class, reason, evidence, risk class, approver and where the approval is recorded, follow-through and its `caused-by` (P35), and its population computed from history: each spec revision after its unit's first attributed pass commit or after its pinned audited revision, each AMENDED acceptance line, each divergence hand-back, each rescope row and each clause-hash move, joined at the commit through the routed-commit attribution and at the close to a record whose approver meets its risk class by the by-risk table final-questions `[deviation]` sets, the risk class read from the record, a stand-in until dOrderedCharter's classifier and dDeclaredLoop's `deviation.approval` land and re-point it, seen red on a planted revision after a pass with no record, an AMENDED line with no record, a mismatched pin and an approver below the risk, and green on a status-only edit (the owner's FQ-3, P41)
- **After:** the deviation record, its kind joined to check 21's kinds, kept in its departing build's `build/` folder as the owner's word on the open readings sets, written in the departing unit's own commit, and its fields its id, the hand-off, the departure's address, before and after, cause class, reason, evidence, risk class, approver and where the approval is recorded, follow-through and its `caused-by` (P35), and its population computed from history: each spec revision after its unit's first attributed pass commit or after its pinned audited revision, each AMENDED acceptance line, each divergence hand-back, each rescope row and each clause-hash move, joined at the commit through the routed-commit attribution and at the close to a record whose approver meets its risk class by the by-risk table final-questions `[deviation]` sets, the risk class read from the record, a stand-in until dOrderedCharter's classifier and dDeclaredLoop's `deviation.approval` land and re-point it, seen red on a planted revision after a pass with no record, an AMENDED line with no record, a mismatched pin and an approver below the risk, and green on a status-only edit (the owner's FQ-3, P41)
- **Cause:** owner ruling
- **Reason:** The clause joins each member to a record whose approver meets its risk class by the by-risk table. The stand-in join this unit ships runs the chain's values until dScopedBuild's `deviation.gate` and dDeclaredLoop's `deviation.approval` land: `report`, so it lists every member and refuses none, and `author-recorded`, so an approver passes when it opens with a role the record grammar names, an owner approver only when it cites a decision row naming the departure. The by-risk table ships beside them as the `by-risk` value, so the clause's red case for an approver below the risk is still observed; the text stands, and what ships runs the chain's values.
- **Evidence:** the owner's "A deviation, your values (Recommended)" (ER:189), quoting answer 3 (ER:103-104); the decision row `PLAY-dClosedLoop-4` (`memory/DECISIONS.md:232`); the execution plan's `[deviations]` table, deviation record 1 (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:1278`); TOOL-dTrueNorth-4 §8 F3
- **Risk:** loosening
- **Approver:** owner, `PLAY-dClosedLoop-4`, the decision row recording ER:189, as P0.1 row 6 requires
- **Follow-through:** amends cl-dClosedLoop-0004@c374ccd0
- **Caused-by:** PLAY-dClosedLoop-4
```

`memory/builds/dTrueNorth/build/2026-10-21-build-TOOL-dTrueNorth-4-deviation-4.md`:

```markdown
# TOOL-dTrueNorth-4 deviation 4 — the product join takes the instrument's plant suite as its acceptance

**Serves:** deviation TOOL-dTrueNorth-4

- **Departs from:** `cl-dClosedLoop-0004@c374ccd0` [acceptance]
- **Hand-off:** design-to-spec
- **Before:** the deviation record, its kind joined to check 21's kinds, kept in its departing build's `build/` folder as the owner's word on the open readings sets, written in the departing unit's own commit, and its fields its id, the hand-off, the departure's address, before and after, cause class, reason, evidence, risk class, approver and where the approval is recorded, follow-through and its `caused-by` (P35), and its population computed from history: each spec revision after its unit's first attributed pass commit or after its pinned audited revision, each AMENDED acceptance line, each divergence hand-back, each rescope row and each clause-hash move, joined at the commit through the routed-commit attribution and at the close to a record whose approver meets its risk class by the by-risk table final-questions `[deviation]` sets, the risk class read from the record, a stand-in until dOrderedCharter's classifier and dDeclaredLoop's `deviation.approval` land and re-point it, seen red on a planted revision after a pass with no record, an AMENDED line with no record, a mismatched pin and an approver below the risk, and green on a status-only edit (the owner's FQ-3, P41)
- **After:** the deviation record, its kind joined to check 21's kinds, kept in its departing build's `build/` folder as the owner's word on the open readings sets, written in the departing unit's own commit, and its fields its id, the hand-off, the departure's address, before and after, cause class, reason, evidence, risk class, approver and where the approval is recorded, follow-through and its `caused-by` (P35), and its population computed from history: each spec revision after its unit's first attributed pass commit or after its pinned audited revision, each AMENDED acceptance line, each divergence hand-back, each rescope row and each clause-hash move, joined at the commit through the routed-commit attribution and at the close to a record whose approver meets its risk class by the by-risk table final-questions `[deviation]` sets, the risk class read from the record, a stand-in until dOrderedCharter's classifier and dDeclaredLoop's `deviation.approval` land and re-point it, seen red on a planted revision after a pass with no record, an AMENDED line with no record, a mismatched pin and an approver below the risk, and green on a status-only edit (the owner's FQ-3, P41)
- **Cause:** review finding
- **Reason:** The product join takes the bootstrap instrument `deviations.py`'s population plants, P0.1's escapes included, as its acceptance (D3), each with the verdict its execution-plan row states, which is stricter than the clause's four red cases. Beside them it names P0.1 row 8a's exception, so the product inherits it openly: a revision that changes only its `**Status:**` line and generated regions is no member, since a generated region is not authored text and TEMPLATE-SPEC moves a revision only on a material change. The clause's text stands: the product does what it says and more.
- **Evidence:** the execution plan's `[deviations]`, "Carried, not asked, for the owner's walk" (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:1289-1294`); its P0.1 table, rows 3 to 8a (`:163-170`); the instrument's plants (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py:851-854`); TOOL-dTrueNorth-4 AC6
- **Risk:** stricter
- **Approver:** spec writer, the gov-spec-writer role of dTrueNorth's whole run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); carried for the owner's walk unless it rules otherwise
- **Follow-through:** amends cl-dClosedLoop-0004@c374ccd0
- **Caused-by:** PLAY-dClosedLoop-1
```

### Inventory

Minted: the module `tools/memory-tree/deviation_join.py`; the record kind `deviation`; the
function `read_chain_clauses` in `design_lib.py`; the CLI flags `--policy`, `--approval`, `--range`,
`--fixture`, `--plant`, `--host` and `--selftest` on the new module; the output prefix `deviation:`.
No conf key, no gate leg, no policy key. Naming cells: each minted function passes `py.function`
(`tools/lexicon/lexicon.py --suggest <name> --as py.function`, OK for all eight); a module file and
a kind token fall in no declared cell.

### Migration

Additive, with one upgrade step. The records written before this unit's pass carry the kind from
their first commit; check 21, which runs only unstaged, reads them as malformed until the pass adds
the kind, and no bar runs between the two (the merge bar runs once, at the close). The upgrade step,
in the pass that adds the kind: every `-deviation-<n>.md` file already under a `build/` folder whose
`**Serves:**` names another kind is set to `deviation`, its ids unchanged, so S2's both-ways join
reads the tree clean; at the spec stage that is
`memory/builds/dTrueNorth/build/2026-10-21-build-TOOL-dTrueNorth-7-deviation-2.md`, written as
`research`. The step writes no other field: a record lacking `**Caused-by:**`, as deviation-2 and
deviation-3 do at the spec stage, is listed under `report` for its writer to complete.

### Rollout

Live at landing in the dogfood tree, under `report`, so it changes no exit. In an adopter it stays
off until the three S2 keys are declared, and adding the kind changes nothing for a tree that
writes no `deviation` record.

### Files touched (estimate)

- `tools/memory-tree/deviation_join.py` (new)
- `tools/memory-tree/design_lib.py`
- `tools/memory-tree/routed_commits.py`
- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/HYGIENE.template.md`
- `memory/HYGIENE.md`
- `tools/memory-tree/README.md`
- `tools/memory-tree/adopt-memory-tree.sh`
- `WIRE-INTO-PROJECT.md`
- `memory/gotchas/record-without-serves-or-with-a-round-counter.md`
- `memory/builds/dTrueNorth/build/2026-10-21-build-TOOL-dTrueNorth-4-deviation-1.md` (new, at the spec commit)
- `memory/builds/dTrueNorth/build/2026-10-21-build-TOOL-dTrueNorth-4-deviation-4.md` (new, at the spec commit)
- `memory/builds/dTrueNorth/build/2026-10-21-build-TOOL-dTrueNorth-7-deviation-2.md` (its kind only, the upgrade step)

### Alternatives rejected

- **A leg of its own for the join.** It owes the meta-gates a new leg trips
  (`memory/gotchas/a-new-leg-trips-a-growing-set-of-meta-gates.md`), and the clause names the
  routed-commit attribution as the commit-time seam. Rejected for the host arm, §8 F2.
- **The commit join in the `pre-commit` hook.** A hook is a governance carrier no clause names, and
  `--no-verify` skips it; the RANGE half reads the same commits at the push and in CI.
- **A typed record-surface path list for the first pass**, as `deviations.py:119-120` types one. It is
  a second statement of what `ROUTED_PATHS` declares; §8 F4.
- **Deviation records under kind `research`**, as the instrument's fixture writes them. The clause
  joins the kind to check 21's kinds, and an untyped record cannot be told from research.

## 5. Production-readiness checklist

- security: the approver arm denies by default, an owner approval passing only on a decision row read at `origin/main`, so a run cannot approve itself with a row it minted on its own branch; no new write path, the join reads only.
- perf / scale: one extra log pass is avoided by reading `routed_commits.py`'s WHOLE list; the remaining cost is one `git log` per chain-build spec and two `git show` and one ancestor test per revision, DERIVED from the chain-build spec count, re-measured by the host's leg time at the close.
- error / empty / loading states: off is one line and reads no history (the host arm makes no git call at all); nothing measured is exit 2 with its reason; an unreadable `origin/main` decision file is one line saying every owner citation is refused, as `deviations.py:553-554` prints it.
- observability: every member, refused record and malformed file is its own `deviation:` line under the host's summary.
- risks: two records of one build sharing a `<n>`, and a record misnamed so the glob misses it; both are findings. The instrument and the product can disagree on a first pass that writes only paths outside `ROUTED_PATHS` (§8 F4); a disagreement becomes an ask in dScopedBuild's `BACKLOG.md` (execution plan, `[phase-1]`).
- testing: `deviation_join.py --fixture` with every plant, `--host routed-commits`, and the scratch-clone probes of AC8 and AC12; the arms join `routed_commits.py`'s self-test (§7).
- migration: additive; §4 "### Migration".
- user docs: `memory/HYGIENE.md`'s "Record bindings" and the kit README; N/A for `help/`, since no command a person runs changes, and help pages for record kinds are dSafePassage's (the owner's FQ-5).

## 6. Acceptance criteria

The plant names are the fixture's; each `refuse` criterion also holds under `report`, where the same
plant exits 0 and lists its member.

- **AC1** — When `python3 tools/memory-tree/deviation_join.py --fixture --plant pass-revision --policy refuse`
  runs, it exits 1 and prints the planted unit's `@rev-1` member as recorded by nobody; the plants
  `subject-pass` and `two-branch` exit 1 the same way, and the base alone exits 0.
  Red when: the first pass is read only from a `Pass:` trailer, or a revision counts only when it
  descends from the pass, so a revision merged from another branch is no member.
- **AC2** — When `python3 tools/memory-tree/deviation_join.py --fixture --plant amended --policy refuse`
  runs, it exits 1 naming `<unit>@rev-2` from the ledger's `amended rev-3` line, and
  `--plant amended-joined` exits 0.
  Red when: the ledger arm reads `AMENDED` on spec lines, or addresses the member at rev-3.
- **AC3** — When `python3 tools/memory-tree/deviation_join.py --fixture --plant audit-pin --policy refuse`
  runs, it exits 1 naming the revision past the pinned `@rev-1`, and `--plant audit-nopin` exits 0
  printing `no audit pin:` with that unit.
  Red when: the pin arm reads no `@rev-N` from the audit record's `**Serves:**`, so the edit after the
  audit is no member.
- **AC4** — When `python3 tools/memory-tree/deviation_join.py --fixture --plant below-risk --approval by-risk --policy refuse`
  runs, it exits 1 with a `refused:` line naming the planted `loosening` record approved by `author`
  and the role its risk requires; `--plant owner-cause` (cause `owner ruling`, approver
  `spec writer`) exits 1 the same way; and both plants exit 0 under the default `author-recorded`.
  Red when: the by-risk compare is absent, or `author-recorded` grades the risk too, which would
  undo deviation-1.
- **AC5** — When `python3 tools/memory-tree/deviation_join.py --fixture --plant status-only --policy refuse`
  runs, a post-pass commit changing only the `**Status:**` line exits 0; the plants `header-rev`,
  `gen` and `status-gen` exit 0, and `gen-text` exits 1.
  Red when: the strip is not `GEN_REGION_AWK` read from `lib-unattended.sh`, or a revision is
  addressed by commit count rather than its header `rev-N`.
- **AC6** — When `python3 tools/memory-tree/deviation_join.py --fixture --plant <case> --policy refuse`
  runs for each of the instrument's 26 plants, each exits as this table states, and under
  `--policy report` each exits 0 listing its member.
  Red when: any plant's exit differs from the table.
  figure: the 26 are PINNED from `deviations.py:851-854` at blob `93e7a492`.

  | Exit 1 | Exit 0 |
  |---|---|
  | `baseline` `clause` `subject-pass` `two-branch` `gen-text` `amended` `approver-none` `owner-bare` `owner-er` `owner-row5` `owner-row1-added` `owner-unknown-id` `add` `handback` `audit-pin` | `pass-none` `status-flip` `header-rev` `gen` `status-gen` `quote` `amended-joined` `approver` `defer` `fix-record` `audit-nopin` |

- **AC7** — When `python3 tools/memory-tree/deviation_join.py --fixture --plant malformed-field --policy refuse`
  runs, a record without `**Caused-by:**` exits 1 naming the file and the field; `malformed-risk`
  (a risk outside the five), `malformed-follow` (an `amends` row with no hash) and `duplicate-n`
  (two records of one build at one `<n>`) each exit 1 naming theirs.
  Red when: `read_record` accepts a missing field or a value outside its closed set.
- **AC8** — When `python3 tools/memory-tree/gen_build_index.py --print-bindings` runs in a scratch
  clone carrying this unit's two records, it prints no `A` row for either; with one record's
  `**Serves:**` kind set to `research`, and separately with a `deviation`-kind record renamed off
  the `-deviation-<n>.md` grammar, it prints an `A` row naming that file and the mismatch.
  Red when: `deviation` is missing from `RECORD_KIND_TOKENS`, or the name join reads one way only.
  fixture: a scratch clone under `%TEMP%`, since the planted renames must not touch the worktree.
- **AC9** — When `git grep -n -e "deviation" -- tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md`
  runs, the "Record bindings" kind list of both names `deviation`, and `git grep -n "Record bindings"`
  finds the pointer in `WIRE-INTO-PROJECT.md`, `adopt-memory-tree.sh` and the gotcha file, none of
  which still spells the four-kind list.
  Red when: one copy keeps its own enumeration of the kinds.
- **AC10** — When `python3 tools/memory-tree/deviation_join.py --fixture --plant record-late --host routed-commits`
  runs, the host's RANGE lines name the planted revision as recorded after its departure at its
  revising commit, its WHOLE lines show the same member joined, and the host exits 0.
  Red when: the arm is not called from `check_routed_commits`, or the commit join asks HEAD's tree
  instead of the departing commit's.
- **AC11** — When `python3 tools/memory-tree/deviation_join.py` runs on the tree after the pass, it
  prints its summary with a non-zero chain-build spec count and exits 0 under `report`, and
  `python3 tools/memory-tree/deviation_join.py --host routed-commits` prints the same members under
  the host's `routed-commits: deviation` lines, the host's own verdict lines unchanged from a run of
  the same call with the arm off.
  Red when: the host's exit moves under `report`, or the summary reports zero chain-build specs.
- **AC12** — When `python3 tools/memory-tree/deviation_join.py` runs in a scratch clone whose
  `.memory-tree.conf` blanks `DESIGN_VIEW`, it prints one `off` line naming the key and exits 0, and
  `python3 tools/memory-tree/deviation_join.py --host routed-commits` there prints the host's
  `deviation join off` line beside an otherwise unchanged summary.
  Red when: the off state reads history or prints a green verdict over nothing measured.
  fixture: the same scratch clone as AC8.
- **AC13** — When `python3 tools/memory-tree/deviation_join.py --fixture --plant unmeasured` runs,
  its `DESIGN_BASELINE` naming no commit and no chain-build spec in the fixture, it exits 2 naming
  why, under both policies.
  Red when: nothing measured reads as exit 0.
- **AC14** — When `python3 tools/memory-tree/deviation_join.py --approval by-risk` runs on the tree,
  no `refused:` or malformed line names
  `2026-10-21-build-TOOL-dTrueNorth-4-deviation-1` or `2026-10-21-build-TOOL-dTrueNorth-4-deviation-4`.
  Red when: deviation-1's owner citation names a row that does not name `cl-dClosedLoop-0004`, or
  a field of either record falls outside its closed set.

## 7. Gates

`memory hygiene` · `routed commits name a specced unit` · `routed-commits selftest` · `build-index selftest` · `memory-hygiene self-test` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/routed_commits.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC10 AC13 · `routed_commits.py`'s self-test calls `deviation_join.py`'s fixture over every plant and asserts each exit, its failing case staged by the plant itself · none
New arm: tools/memory-tree/gen_build_index.py · covers AC8 · `gen_build_index.py`'s self-test gains a mis-kinded and a misnamed deviation record, each an `A` row · none

## 8. Open questions

- **F1 — The brief gives the status header `DRAFT`; the format's vocabulary has no such token.**
  `STATUS_TOKENS` (`tools/memory-tree/tree_lib.py:25`) is OPEN, SPECCED, INPROGRESS, BLOCKED,
  DEFERRED, CLOSED and WONTDO, and the header regex would not parse `DRAFT`, so the spec would read
  as MISSING. Options: `DRAFT` as written; `OPEN`, the format's drafting token. RESOLVED (agent,
  2026-10-21, delegated): `OPEN` — the spec format owns the header (`memory/TEMPLATE-SPEC.md`,
  "The status header"), so the brief's token is an error in the brief, not a choice.
  widens: none · relaxes: none
- **F2 — Where the join at the commit and at the close runs.** Options: a leg of its own; an arm of
  `routed_commits.py` over its RANGE and WHOLE halves; a check in `check-memory-hygiene.sh`; an
  edit of the unattended driver's `--close`. The driver is TOOL-dTrueNorth-7's alone and builds
  last; hygiene has no RANGE half; a leg of its own trips the new-leg meta-gates. RESOLVED (agent,
  2026-10-21, delegated): the `routed_commits.py` arm, the seam the clause and the deviation research
  name (`final-questions.md:285`, `research-final-deviation.md:112`), with the core in
  `deviation_join.py`. grants: PLAY-dClosedLoop-3 the memory-tree kit's routed-commits leg gains
  the deviation join the clause names · widens: none · relaxes: none
- **F3 — Which gate value and approval value the shipped join runs.** Options: `refuse` and
  `by-risk`, as the clause's table reads; `report` and `author-recorded`, the chain's values.
  RESOLVED (agent, 2026-10-21, delegated): `report` and `author-recorded` in the host, both values
  and `refuse` on the module's CLI so every red case is still observed — the owner's ruling
  ER:189, decision row `PLAY-dClosedLoop-4`, recorded as deviation-1. widens: none · relaxes: none
- **F4 — The first pass's product-path test.** Options: the instrument's typed record-surface list
  (`deviations.py:119-120`); `ROUTED_PATHS`, the routed-commit attribution's own declaration. Both
  agree on every plant. RESOLVED (agent, 2026-10-21, delegated): `ROUTED_PATHS`, since the clause
  names the routed-commit attribution and a second typed list is one fact twice; the difference, a
  pass writing only unrouted paths outside the record surface, is stated in §5 risks.
  widens: none · relaxes: none
- **F5 — Where the `[chain]` row reader lives.** TOOL-dTrueNorth-1 ships the view reader
  `read_design_view`, `derive_clause_hash`, the retired-id reader and the binding-line parser in
  `design_lib.py` (its S2 to S6), and no reader of
  `DESIGN_RECORD`'s `[chain]` rows, which this unit's clause-move arm and TOOL-dTrueNorth-6's
  generator both need. Options: each unit parses `[chain]` itself; this unit adds one reader to
  `design_lib.py`. RESOLVED (agent, 2026-10-21, delegated): `read_chain_clauses` in `design_lib.py`,
  added by this unit, which builds first of the two. If TOOL-dTrueNorth-1's spec already ships one,
  the M2 cross-read amends this spec to import it. widens: none · relaxes: none
- **F6 — The `**Follow-through:**` and `**After:**` of deviation-1 and deviation-4.** (a) `amends`
  with a new clause text: the view's hash for `cl-dClosedLoop-0004` moves, so the product join,
  reading the view (brief S2), wants a new pin while `carries.py`, reading v2, wants `c374ccd0` at
  the Design exit, and one of the two reds whichever pin this spec carries. (b) a non-row
  follow-through such as `usage deviation.approval`: the view's "deviation with no row" finding
  (`asbuilt.py:58-62`) reds at every close. (c) `amends cl-dClosedLoop-0004@c374ccd0` with an
  `**After:**` that is the clause's text unchanged, the departure stated in `**Reason:**`: the view
  cites the record, the hash stays, and both joins agree on the pin. Veto 1 discards (a) and (b).
  RESOLVED (agent, 2026-10-21, delegated): (c), the reading TOOL-dTrueNorth-2's §8 F3 takes for
  deviation-3, so the set agrees. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-21 · initial draft.
- rev-2 · 2026-10-21 · §3 · the Edges block gains a hands-off to each unit the round-1 spec audit
  promoted against this one, TOOL-dTrueNorth-10, TOOL-dTrueNorth-12 and TOOL-dTrueNorth-16, the
  mirror of its consumes-from; no other section moves.
- rev-3 · 2026-10-21 · §3 · the Edges block gains a hands-off to TOOL-dTrueNorth-17 and TOOL-dTrueNorth-18,
  promoted by the round-2 spec audit, the mirror of their consumes-from; no other section moves.

## 10. Reuse audit

The seam extended is `tools/memory-tree/routed_commits.py`: its `read_routed_commits` log pass
(`:219-230`), its `derive_commit_range` RANGE and WHOLE populations (`:204-216`, `:249-251`), its
`test_routed_path` and its batched `cat-file` lookup (`:283-289`); and
`tools/memory-tree/gen_build_index.py`'s binding classifier (`:550`, `:680-695`). The population and
the join port the bootstrap instrument `deviations.py`, whose blob `93e7a492` the packet pins.
`reuse_lookup.py "join each spec revision after its unit's first pass commit to a deviation record"`
ranked `records` (`gotchas.py`), `build_commit`, `pass_commit` and `read_pass_declarations`
(`lib-unattended.sh`) and `parse_spec_h1`; `"the first pass commit attributed to a unit by its Pass
trailer"` ranked `pass_commit`, `read_attribution_tokens`' neighbours and `baseline_units`. None of
them grades a deviation: the shell readers decide which commit is a pass for the unattended driver,
where a trailer replaces the subject (`routed_commits.py:22-26`), and the map does not scan
`memory/`, so it cannot see the instrument at all. The hits disagree with source on one point only:
the map ranks no Python first-pass reader, and `deviations.py:279-289` is one, outside its scan.
The recall probe found the clause, the instrument's research (`research-final-deviation.md:103-112`),
which names `routed_commits.py` and check 21 as the gate seams, and decision row
`PLAY-dClosedLoop-4`.

Recall terms used: `python tools/memory-recall/query.py "how is a deviation from the frozen design recorded, approved by risk and joined to spec revisions after a pass" --terms "deviation record approver risk population first pass revision audit pin amended ledger rescope hand-back clause hash"`
