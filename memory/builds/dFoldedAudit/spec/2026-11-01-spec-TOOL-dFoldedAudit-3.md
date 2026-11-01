# TOOL-dFoldedAudit-3 — the DISPOSAL stage disposes by nature and reconciles folds to their specs

**Status:** CLOSED · rev-2 · 2026-11-02 · node d · Tier-2 · base 74274869 · streams tooling · order 30

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dFoldedAudit-1-3-design.md](../build/2026-11-01-build-TOOL-dFoldedAudit-1-3-design.md) | research | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8 |
| [2026-11-01-build-TOOL-dFoldedAudit-1-4-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dFoldedAudit-1-4-spec-stage-returns.md) | journal | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8 |
| [2026-11-01-build-TOOL-dFoldedAudit-5-1-cross-read-return.md](../build/2026-11-01-build-TOOL-dFoldedAudit-5-1-cross-read-return.md) | journal | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8 |
| [2026-11-02-build-TOOL-dFoldedAudit-3-ledger.md](../build/2026-11-02-build-TOOL-dFoldedAudit-3-ledger.md) | journal | — |
| [2026-11-01-prompt-TOOL-dFoldedAudit-1-brief.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-1-brief.md) | research | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8 |
| [2026-11-01-prompt-TOOL-dFoldedAudit-3-build-brief.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-3-build-brief.md) | research | — |
| [2026-11-01-prompt-TOOL-dFoldedAudit-3-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-3-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The build harness disposes a spec audit by nature instead of by severity. A LOCAL finding folds into
the spec or specs it touches, a finding that NEEDS A NEW MECHANISM is promoted, and each disposition
joins to a unit and a rev, so no HIGH can vanish into prose. The reason disposal stopped being by
nature stays answered: the stage still runs on the outstanding count, never on the verdict.

## 2. Scope (IN)

- **S1** — The argument. `tools/workflows/unattended-build.template.js` takes a new `disposal` arg, a
  closed pair `by-nature` and `promote-all`, with the three states §4 "The three states" tables.
  A present value outside the pair refuses before any agent spawns. Observed by AC7 and AC8.
- **S2** — The by-nature prompt. Under `by-nature` the disposal prompt states the predicate of §4 "The
  by-nature prompt" and orders a LOCAL finding folded, a BLOCKER included, with a rev bump and a §9
  line naming the review record by its file stem and the finding id. Observed by AC1 and AC3.
- **S3** — The return. `DISPOSAL_SCHEMA` declares `dispositions`, the array §4 "Data model" shapes, and
  the stage returns it under either declared value. Observed by AC1 and AC2.
- **S4** — The reconciliation. A new `deriveDispositionFault` refuses a return whose `dispositions`
  do not join to its counts, to the review's confirmed ids and severities, or to a spec and a rev.
  Observed by AC2 and AC4.
- **S5** — The unit bounds. Under `by-nature` the floor and ceiling count the new-mechanism findings
  in `dispositions`, so a BLOCKER or HIGH needing a mechanism takes its own unit and the minors
  among them batch into one unit or two. Observed by AC5.
- **S6** — The record order. Under a declared value the disposal precedes the record at every exit,
  because the row carries what the disposal did. At a positive blocker count the first `--review`
  call is the probe, and a refusal naming an exit holds the record for after the stage. Observed by
  AC3.
- **S7** — The row. `writeRound` passes `--folded` and `--promoted` on a spec exit under a declared
  value, and the disposition is `promote` when `promoted` is above 0, `fold` when `promoted` is 0 and
  `folded` is above 0, and absent when nothing stood. Observed by AC1, AC3 and AC6.
- **S8** — The hoist. `dispositions` rides the stage's hoist onto the hand-out, the DEGRADED return
  and the attended every-unit-terminal return, as a stated `[]` on a skip. Observed by AC1 and AC2.
- **S9** — The file's own account. The `meta.phases` Disposal detail, the header's M4 paragraph, the
  STAGE 3 comment, the reconciliation comment and the CONVERGING `nextAction` say what the file now
  does under each state, and the engine marker moves 1.12 to 1.13 with its arm literal. Observed by
  AC9.
- **S10** — The render. `tools/workflows/unattended-build.js` is regenerated from the template in the
  same commit. Observed by AC9.

## 3. Non-goals (OUT)

- A closing diff review, its exit rows, `closing-review-recorded` and M8. That review is
  `tier2-review` called from the main loop, and no line this unit changes sits on its path. This
  harness's audit is a spec audit by construction, so its DISPOSAL stage is the spec branch [scope]
  names and no shared branch is reworded.
- The stop verdict, the two verbs that read `dispositions`, the record they append to, and the
  `nextAction` that routes a chain round. This unit's `nextAction` sentences stay as they stand
  except the one clause S9 names.
- A sibling edit and its refusal of a built unit.
- `--review`'s acceptance of the new row, check 2's grading and the cutoff key. The harness passes
  the flags and the driver decides.
- The policy keys themselves. The harness has no filesystem and reads none of them.
- Every prose carrier: M4, the review protocol, the verbs guide, the `/build` Skill and
  `tools/workflows/README.md`.
- Proving the §9 line exists. This runtime cannot read a spec, as `DISPOSAL_SCHEMA`'s own comment at
  `unattended-build.template.js:836-840` says of `edges`. TOOL-dFoldedAudit-6's deviation join reads
  the tree and reports a rev move whose §9 line cites no spec-audit record.
- Retiring or refolding a unit an older run promoted. Nothing here is retroactive.

### Edges

- **consumes-from** `TOOL-dFoldedAudit-7` — the key `review.spec-audit.disposal` and its two values, `by-nature` and `promote-all`, which the caller reads and hands over as `disposal`, and `SPEC_FOLD_CUTOFF`, which decides who passes it; without them the arg has no source and every caller stays on the undeclared path.
- **consumes-from** `TOOL-dFoldedAudit-2` — `--review`'s `--folded` and `--promoted` flags and its acceptance of `--disposition fold` at a spec exit; without them every declared exit is refused at the record.
- **hands-off** `TOOL-dFoldedAudit-4` — `dispositions`, `deriveDispositionFault` and `deriveReadRev`, which the sibling-edit list and the frozen-unit join extend.
- **hands-off** `TOOL-dFoldedAudit-5` — `dispositions` on the hand-out, which the main loop records through that unit's verb, and `nextAction`, which that unit routes on the verdict.
- **hands-off** `TOOL-dFoldedAudit-1` — the `disposal` arg, which the verbs guide and the build Skill tell a caller to pass, and every prose carrier of the new rule.

## 4. Design

### The three states

A Workflow script has no filesystem, so the value arrives as an argument, as `specAudit` and
`runStateExists` do (`unattended-build.template.js:22-27`). `disposal` joins `TYPED` at
`unattended-build.template.js:322-327`, refused by name when present and outside the pair.

| `disposal` | Who passes it | Rule | Row | `dispositions` |
|---|---|---|---|---|
| absent | a run preflighted before `SPEC_FOLD_CUTOFF` | today's, byte for byte | today's | not read |
| `promote-all` | a run past it whose key holds the old rule | today's, `folded` refused | new, `folded 0` | required |
| `by-nature` | a run past it, the default | [nature] | new | required |

Absent is today's path because [cutoff] has in-flight runs finish under the old rule, and a caller
that predates this unit composes no such arg. The file's own idiom is the same:
`unattended-build.template.js:205` keeps today's prompt byte for byte on an absent key. This also
fails loud in the direction that matters. A post-cutoff run that forgets the arg writes the old row,
and TOOL-dFoldedAudit-2's `--review` refuses it before any spec is wrong. The opposite default would
fold specs first and meet the refusal afterwards. `disposal` is not audit-shaped: with the audit
off the stage never reads it, so a caller may pass it on every call.

The owner's default is the key's: `policy.py get review.spec-audit.disposal` reports `by-nature`, and
a caller following the carriers passes what it reports. [switches] is about the key, and the arg is how its value crosses
into a runtime that cannot read it.

### Data model

One array, returned by the stage and carried on the hand-out. [address] fixes the keys.

```
{ id: <integer raw finding id>, severity: 'BLOCKER'|'HIGH'|'MEDIUM'|'LOW',
  nature: 'local'|'new-mechanism', specs: [<unit id>, ...], unit: <unit id>, rev: <integer> }
```

| Key | Meaning |
|---|---|
| `id` | The raw id of the ledger and of `confirmedFindings` (`tier2-review.template.js:1609-1615`), an integer as the synthesis `ids` are (`tier2-review.template.js:1932`). |
| `severity` | The grade the report gives, or the grade adjudicated for an UNVERIFIED finding. |
| `nature` | `local` folds and `new-mechanism` promotes. Under `promote-all` every entry is `new-mechanism`, because that rule reads every finding as one. |
| `specs` | The address: the non-empty set of unit ids the fix would change. The stage copies the report's machine line where one is printed, which TOOL-dFoldedAudit-5 adds, and reads the finding's address otherwise. |
| `unit` | For `local`, the spec this entry folded into. For `new-mechanism`, the promoted unit. |
| `rev` | That spec's rev after this disposal, the integer N of its header's `rev-N`. |

A LOCAL finding that folds into two specs is two entries with one `id`, because a fold names its
target and one entry can name only one. [survive] 2 joins every folded id to a unit and that unit's
new rev. Entries sharing an `id` agree on `severity`, `nature` and `specs`. A refuted UNVERIFIED
finding has no entry, so distinct ids count `folded + promoted` exactly.

`DISPOSAL_SCHEMA` at `unattended-build.template.js:841-878` declares the array under `properties`
and leaves it out of `required`, because an undeclared run's prompt never asks for it. Absence is
refused in the reconciliation, as `edges === null` is. `id` is spelled `{ type: 'integer' }` and
`rev` `{ type: 'integer', minimum: 1 }`, because the arm at `unattended-build.test.sh:1289` pins
exactly 3 occurrences of `type: 'integer', minimum: 0` in the render.

### The by-nature prompt

The predicate is [nature]'s, and it is M2's one-mechanism test. The sentences below replace the
named ones under `by-nature`, and everything else in the prompt at
`unattended-build.template.js:2054-2112` stays. The absent path keeps every sentence unchanged, so
the arms at `unattended-build.test.sh:1275-1281` keep reading it. `promote-all` is the absent text
plus the return sentence.

| Today's sentence, by template line | Under `by-nature` |
|---|---|
| 2063-2066, `Each BLOCKER or HIGH id is its own unit` | `Each NEW MECHANISM BLOCKER or HIGH id is its own unit`, the rest of the sentence unchanged |
| 2068-2069, `BUILD-METHOD M4 disposes BY SEVERITY and admits no third route. PROMOTE every BLOCKER and every HIGH:` | the block below, ending `PROMOTE every NEW MECHANISM finding:` |
| 2085, `PROMOTE every MEDIUM and every LOW too, BATCHED:` | `PROMOTE every NEW MECHANISM MEDIUM and LOW too, BATCHED:` |
| 2093, the sentence opening `Nothing is folded` | no sentence |

```
BUILD-METHOD M4 disposes a spec audit BY NATURE, independent of severity. A finding NEEDS A NEW
MECHANISM when its fix adds a document, gate, adopter, generated artifact, verb or write path that
no unit's Scope names; every other finding is LOCAL: a wording or citation, a missing witness, an
edge mirror, a criterion's reach, any small fix. FOLD every LOCAL finding, a BLOCKER included, into
the spec or specs it touches: bump each spec's rev and add a section 9 line naming `<report stem>`
and the finding id.
```

The return sentence joins the prompt's return block under either declared value:

```
Return in `dispositions` one entry per finding per spec as {id, severity, nature, specs, unit, rev}:
`id` the integer raw id, `nature` exactly `local` or `new-mechanism`, `specs` the unit ids on the
finding's `**Specs:**` line, or where none is printed the non-empty unit ids the fix would change,
`unit` the spec folded into or the unit promoted to, and `rev` that spec's rev now. A refuted finding
has no entry.
```

The in-loop fold at `unattended-build.template.js:1997-1998` stays. [fold-stage] keeps non-exit rounds
folding as they do. Its last clause reads `only a terminal exit disposes, and it disposes by nature`
under `by-nature`, and is unchanged otherwise. The log at `unattended-build.template.js:2045-2047`
reads `disposing by nature` under `by-nature` and is unchanged otherwise, so the arm at
`unattended-build.test.sh:768` stays green on the absent path.

A fold stays the caller's to commit (`unattended-build.template.js:130`). `<report stem>` is the file
name `lastReport` ends in, less `.md`, because TOOL-dFoldedAudit-6's predicate joins a §9 entry to a
record by its file stem as a whole token. M8 tells a caller to rename a free-named report to hygiene
check 5's grammar, so a caller renaming one renames the citation in the same commit, or that
predicate reports the fold as an unrecorded move.

### The record order

Today the record precedes the disposal at a positive blocker count, and the agent's retry appends
`--disposition promote` (`unattended-build.template.js:1871-1873`). That order cannot carry a row
counting folds, because the counts do not exist until the stage has run. The driver's refusal is
already a side-effect-free probe of whether the round ended: `fail 37` at `unattended.sh:12790`
returns before the `park` at `unattended.sh:12850` writes the row.

| Blockers | Outstanding | First call under a declared value | Then |
|---|---|---|---|
| 0 | 0 | `writeRound` records with `--folded 0 --promoted 0` | no stage |
| 0 | above 0 | none, as `disposeFirst` does today | the stage, then the record |
| above 0, not an exit | any | the driver prints `CONVERGING` and the row is written | caller folds, as today |
| above 0, an exit | any | the driver refuses and the record agent reports the exit | the stage, then the record |

Under a declared value the record prompt's retry sentence is replaced. On a refusal naming
`--disposition`, `--highs` or `--minors` the agent does not retry. It returns `terminalExit: true` and
`exitState`, the state word of the `exits <state>` clause that TOOL-dFoldedAudit-2 keeps in every such
refusal. `REVIEW_RECORD_SCHEMA` at
`unattended-build.template.js:733-743` declares both. `writeRound` returns that word as the token
after testing it against `NON-CONVERGENT`, `CEILING` and `BOUNDED`, and a word outside the three
throws by name. So `verdict` holds the exit and `audit` reads as it does today.

A `recordAfter` const replaces the test at `unattended-build.template.js:2309`. It is `disposeFirst`,
or a declared value with a positive blocker count and a verdict other than `CONVERGING`. Attended mode
never reaches the second half, because `writeRound` answers `CONVERGING` at any positive count there.

`writeRound(disposition, adjudicated, tally)` takes the counts as its third argument, because
`folded` and `promoted` are `let` bindings at `unattended-build.template.js:2037`, in their temporal
dead zone when line 1938 calls it. A non-empty `tally` carries the `--highs` and `--minors` counts at
any blocker count. The post-disposal call at a positive count spawns under the stage name
`record-exit`, so the two spawns are told apart in a trace, and its token must equal the held
`verdict` or the harness throws by name.

The DEGRADED note at `unattended-build.template.js:2288-2296` extends to a held exit, and its
by-hand record spells the row's actual `--verdict`, `--blockers`, `--folded` and `--promoted`.

### The row

| Term | Value |
|---|---|
| `tally` | ` --folded <f> --promoted <p>`, empty on the absent path |
| disposition | ` --disposition promote` when `promoted > 0`, ` --disposition fold` when `promoted` is 0 and `folded > 0`, else empty |
| `adjudicated` | `Math.max(promoted + folded - au.confirmed, 0)` under a declared value |

The third row keeps `f + p = b + h + m` true, because `--minors` adds `adjudicated` to the confirmed
minors at `unattended-build.template.js:1856`. The absent path keeps
`Math.max(promoted - au.confirmed, 0)`.

### The reconciliation

`deriveDispositionFault(d, promotedIds)` returns a reason or `''`. It joins the guard at
`unattended-build.template.js:2219-2224` under a declared value, after the sum arm, and its reason
takes the same place in the `why` chain, ahead of the unit bounds that read the same array. The arms
`d.folded !== 0` and `d.promoted < au.confirmed` apply under `promote-all` and the absent path only,
and the refusal text at `unattended-build.template.js:2236-2238` stands, because it is what
`promote-all` restores.

| # | Refused | Why |
|---|---|---|
| 1 | `dispositions` not an array | An absent list and a declared empty one are different answers. |
| 2 | an entry whose `id`, `severity`, `nature`, `specs`, `unit` or `rev` is missing or outside its shape | [survive] 2, a fold names its target. An empty `specs` reads `names no spec`. |
| 3 | one `id` with two severities, natures or addresses | One finding has one disposition. |
| 4 | distinct `local` ids unequal to `d.folded`, or distinct `new-mechanism` ids unequal to `d.promoted` | The integers and the list must be one fact. |
| 5 | `auRaw.confirmedFindings` not an array, or a confirmed id with no entry | Every confirmed finding is disposed by id, and the callee returns this array on every path (`tier2-review.template.js:2078`). |
| 6 | entries over confirmed ids whose BLOCKER count differs from `au.blockers`, or whose HIGH count differs from `au.highs` | [survive] 3, a grade cannot be lowered to hide a HIGH. Both counts are over raw confirmed ids. |
| 7 | a `local` entry whose `unit` is outside `specs` or the roster, or a `local` id whose `unit`s are not exactly its `specs` | A fold short of its address leaves a spec wrong. |
| 8 | a `local` entry whose `rev` is not above `deriveReadRev(unit)` | A fold is a rev bump. |
| 9 | a `new-mechanism` entry whose `unit` is not in `promotedIds`, or a promoted id no entry names | A promotion names its unit and a unit names its finding. |
| 10 | a `specs` member in neither `ordered` nor `promotedIds` | An address outside the roster is a stray, as `auditIds` refuses at `unattended-build.template.js:413-423`. |

Rule 6 reads `au`, not the `severity` of `confirmedFindings`, because the synthesis may regrade with a
justification and `au` holds that adjudication (`tier2-review.template.js:1955-1986`).

`deriveReadRev(unit)` returns the rev the audit read: the matching `subjects` entry joined by
`specPath` as `unattended-build.template.js:2560-2562` does, else 1. So a scoped round, which holds no
subject for a sibling, still requires a rev above 1.

Under `by-nature` the bounds at `unattended-build.template.js:2207-2211` read the entries. With `H`
the distinct new-mechanism BLOCKER and HIGH ids and `M` the distinct new-mechanism minors, the floor
is `H + (M > 0 ? 1 : 0)` and the ceiling `H + (M > 0 ? 2 : 0)`. With rule 9's set equality, two HIGHs
sharing a unit fall below the floor, and five minors in five units rise past the ceiling, so neither
needs a rule of its own. The refusal text at `unattended-build.template.js:2242-2248` keeps its shape
over those counts. The comment at `unattended-build.template.js:2213-2218` calling two arms
unreachable stays true under `by-nature`, by the same arithmetic over the entries, and it says so.

### Inventory

| Minted | Cell | Grade |
|---|---|---|
| `deriveDispositionFault` | `js.function` | `lexicon.py --suggest` answers OK |
| `deriveReadRev` | `js.function` | `lexicon.py --suggest` answers OK |
| `disposal` | Workflow arg | `TYPED` |
| `dispositions` | schema key and hand-out key | `DISPOSAL_SCHEMA` |
| `terminalExit`, `exitState` | schema keys | `REVIEW_RECORD_SCHEMA` |
| `record-exit` | agent stage name | `renderAgentLabel` |

### Rollout

The template is the source. The render comes from `check-protocol-parity.test.sh --render`, as the
marker at `unattended-build.template.js:3` says. That render is the main loop's or the pass's own
tool use, not a verdict, and the parity leg grades it at the close. The engine marker moves once in
this build, here, and TOOL-dFoldedAudit-4 and TOOL-dFoldedAudit-5 do not move it again. It is the one
version a pass of this build moves by hand: `unattended-build` is no kit entry, because the entry that
claims this directory is `review-harness` (`tools/workflows/kit.toml:3`), so the lander's mint
(`tools/push-main.sh:26-31`) never reaches the marker, and every kit version still waits for that mint.
The arm at `unattended-build.test.sh:1960` pins the literal and moves with it.

No run changes behaviour until a caller passes `disposal`. The key's default reaches runs through
the carriers TOOL-dFoldedAudit-1 writes.

### Files touched (estimate)

`tools/workflows/unattended-build.template.js`, `tools/workflows/unattended-build.js` and
`tools/workflows/unattended-build.test.sh`.

### Alternatives rejected

- **The disposal agent reads the key itself.** The prompt depends on the value, so the value must
  exist before the agent spawns. A resolver agent before every disposal adds a spawn to read one
  word the caller can pass.
- **`disposal` absent means `by-nature`.** It would rewrite the fixtures of every arm that returns
  `"folded":0`, and an in-flight run that merged this harness would fold specs before the driver
  refused its row. S1's table fails before the write instead.
- **A `--review --dry-run` flag to learn the exit.** It adds a surface for a fact the existing
  refusal already states without writing.
- **Keep record-first and amend the row after the stage.** A row is an append-only history entry, and
  two rows for one round read as two rounds to `review_state`.
- **Compare `dispositions` severities to `confirmedFindings`.** It would refuse an honest synthesis
  regrade. Rule 6 compares to the adjudicated counts.
- **`nature` as `fold` and `promote`.** That names the act and not the predicate, and [nature]
  defines the predicate.

## 5. Production-readiness checklist

- security: no new write path. The disposal agent already writes specs as `gov-spec-writer`
  (`tools/roles/workflows.toml:37`), and a fold is that same write.
- perf / scale: no new spawn on the absent path. A declared exit at a positive blocker count adds
  one `record-exit` agent. The reconciliation is linear in the entries.
- error / empty / loading states: an empty `dispositions` reconciles only when `folded` and
  `promoted` are 0 and nothing was confirmed. A dead stage keeps today's refusal, with the round
  unrecorded on every declared path.
- observability: `dispositions` rides every return past the stage, and the `disposal: done` log keeps
  its counts, so a caller never infers what a fold touched.
- risks: the arg is only as good as its caller, which the driver's refusal of the old row bounds for
  an unattended run and which `/build`'s carrier sentence bounds for an attended one. The prompt is
  a claim, so the §9 line stays unproved here and TOOL-dFoldedAudit-6 is what reads the tree. The
  record agent parses a refusal, so a reworded driver sentence that drops `exits` makes `exitState`
  fail its enum and throw rather than pass.
- testing: the arms extend `tools/workflows/unattended-build.test.sh` and its `run_wf` double. Each
  new case is one or two `run_wf` sites, and the leg's ceiling of 700 s holds them.
- migration: none. The absent path is the migration, and no landed row or spec moves.
- user docs: N/A here. TOOL-dFoldedAudit-1 owns every prose carrier, `help/` included where it names
  the rule.

## 6. Acceptance criteria

Every case runs `node disposal-fixture.js <case>`, a stub runner the pass writes under the run's
scratch from the AsyncFunction shape of `run_wf`, evaluating `tools/workflows/unattended-build.js`
with `RUN_WF_SCHEMA=strict`, so a schema that loses a key loses it in the fixture. Its fixture args
are the suite's `UNITS` plus the named `disposal`, and its review double carries
`confirmedFindings`.

- **AC1** — When `node disposal-fixture.js local-high` runs `disposal: 'by-nature'` over one confirmed
  HIGH, id 7, and a double returning `folded: 1`, `promoted: 0` and one `local` entry for `A-tB-1` at
  rev 2, the trace holds `disposal: done — promoted 0 · folded 1`, and the RESULT carries that entry
  in `dispositions` and a non-empty roster. The `record` prompt carries
  `--highs 1 --minors 0 --folded 1 --promoted 0 --disposition fold`, and the `dispose` prompt carries
  `BY NATURE, independent of severity` and `a section 9 line naming`.
  Red when: the disposal arm still refuses `folded`, or the row omits a count.
- **AC2** — When `node disposal-fixture.js no-spec` runs AC1's return four ways, with `specs: []`, with
  `unit` absent, with `rev: 1` and with `dispositions` absent, each trace holds `disposal: NOT done`,
  the RESULT carries `"roster":[]` and a `DEGRADED` note, and no `record` agent runs. The first reads
  `names no spec` and the last names the absent list.
  Red when: a fold return with no target reaches the hand-out, which is cluster D's shape at
  `unattended-build.template.js:2131-2133`.
- **AC3** — When `node disposal-fixture.js local-blocker-exit` runs one confirmed BLOCKER with a
  `record` double answering `terminalExit: true`, `exitState: 'BOUNDED'`, the `dispose` agent precedes
  a `record-exit` agent, and the RESULT verdict is `BOUNDED`. The `record-exit` prompt carries
  `--blockers 1 --highs 0 --minors 0 --folded 1 --promoted 0 --disposition fold`. A `record-exit`
  double answering `CEILING` throws, and an `exitState` of `DONE` throws.
  Red when: the first `record` prompt still orders the retry, so the row is written before the counts
  exist.
- **AC4** — When `node disposal-fixture.js hidden-high` runs two confirmed HIGHs with the disposal's
  entries grading one MEDIUM, then with `folded: 2` beside one entry, then with one confirmed id
  unnamed, each trace holds `disposal: NOT done` and `"roster":[]`.
  Red when: a return reconciles on the sum alone, so a HIGH leaves the count that names it.
- **AC5** — When `node disposal-fixture.js new-mechanism` runs one new-mechanism HIGH to `A-tB-4` and
  two new-mechanism MEDIUMs to `A-tB-5`, the trace holds `disposal: done — promoted 3 · folded 0` and
  the `record` prompt carries `--disposition promote`. The same HIGH sharing `A-tB-5` refuses below
  the floor, and five minors in five units refuse above the ceiling.
  Red when: the bounds still read `au.highs`, so a folded HIGH demands a unit.
- **AC6** — When `node disposal-fixture.js promote-all` runs `disposal: 'promote-all'` with `folded`
  at 1, the trace holds `a spec audit's MEDIUM and LOW are PROMOTED`. With every finding promoted and
  each entry `new-mechanism` it holds `disposal: done` and the `record` prompt carries `--folded 0`.
  Red when: `promote-all` admits a fold, or writes today's row.
- **AC7** — When `node disposal-fixture.js undeclared` runs one confirmed BLOCKER at a `BOUNDED` token
  with no `disposal` key and a double returning no `dispositions`, the trace holds `disposal: done`
  and no prompt carries `--folded`. The `dispose` prompt carries `disposes BY SEVERITY`, and the
  `record` prompt carries `--disposition promote appended`.
  Red when: a path meant to be byte for byte today's requires the new list or writes the new row.
- **AC8** — When `node disposal-fixture.js bad-value` runs `disposal: 'fold'`, the run throws a message
  naming `disposal` and no `agent:` line precedes it.
  Red when: an unknown value folds to a default, which selects a rule nobody supplied.
- **AC9** — When `grep -c "disposes a spec audit BY NATURE" tools/workflows/unattended-build.js` runs
  it prints 1, and `sed -n 3p tools/workflows/unattended-build.js` prints a line carrying
  `unattended-build@1.13`.
  Red when: the template moved and the render did not, or the marker stayed.

## 7. Gates

`unattended-build self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `policy fixtures` · `workflow script syntax` · `harness arms (fail branches armed or pinned)` · `review-protocol parity (kit vs dogfood)` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/unattended-build.test.sh · covers AC1 · a local HIGH folded under `by-nature`, its failing case the `d.folded !== 0` arm left ungated, which refuses it · none
New arm: tools/workflows/unattended-build.test.sh · covers AC2 AC4 · the four no-target returns and the three hidden-HIGH returns, their failing case `deriveDispositionFault` stubbed to return `''`, which hands the roster out · none
New arm: tools/workflows/unattended-build.test.sh · covers AC3 · a local BLOCKER at a BOUNDED exit, its failing case the record prompt's retry sentence restored, which records before the stage · none
New arm: tools/workflows/unattended-build.test.sh · covers AC5 · new-mechanism bounds, its failing case the floor reading `au.highs`, which refuses AC1 · none
New arm: tools/workflows/unattended-build.test.sh · covers AC6 AC7 AC8 · the `promote-all`, absent and malformed states, its failing case the `disposal` branch inverted, which folds under `promote-all` · none

The version arm's literal at `unattended-build.test.sh:1960` moves with the marker. That is a moved
pin, not a new arm.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from `build/2026-11-01-build-TOOL-dFoldedAudit-1-3-design.md`
  tags [scope], [nature], [survive], [fold-stage] and [address]. The tag [address] is split with
  TOOL-dFoldedAudit-5: this unit owns the `dispositions` return and that unit owns the review's
  `specs` line and both verbs.
- rev-2 · 2026-11-01 · §4 · S9 · M2's cross-read found two disagreements. `TOOL-dFoldedAudit-5` says
  the disposal reads the report's `**Specs:**` line and refuses a differing address at its row 17,
  and this prompt never named that line, so the return sentence now does. This Rollout called the
  marker it moves a kit marker, where units 1, 5, 6 and 7 say no kit version moves by hand; it is an
  engine marker no mint reaches, and S9 and AC9 stand.

## 10. Reuse audit

The seam extended is the DISPOSAL stage at `tools/workflows/unattended-build.template.js:2004`,
through `DISPOSAL_SCHEMA` at `:841` and the guard at `:2219`, plus `writeRound` at `:1855` and the
`TYPED` table at `:322`. `tools/codebase-map/reuse_lookup.py` over the phrase below ranked name-stem
helpers and no reconciliation of a disposal, because a workflow script is one file that cannot import, so the stage's own guard is the
only seam. The driver's refusal at `tools/unattended/unattended.sh:12790` is reused as the exit
probe rather than minting a flag. `tools/memory-tree/gotchas.py --for-paths` selected
`fixture-passes-by-finding-nothing`, `guard-above-a-fold-makes-its-fallback-dead` and
`degradation-known-but-unreported`, which AC2's population, §4's note on the two unreachable arms and
S8's hoist answer. The recall probe surfaced TOOL-aProbedUnit-7, TOOL-aEvidencedLens-17 and the
scout's three survival properties, and they agree with [survive]. The scout's cites were re-read
against source: line numbers held at this base, and it did not say that `confirmedFindings` lets the
harness join by raw id, which §4 rule 5 adds.

Probe phrase: `dispose a spec audit finding by fold or promote and reconcile the counts`.

Recall terms used: `python tools/memory-recall/query.py "why did spec audit disposal stop being by nature and how must fold reconcile to its spec" --terms "disposal promote fold severity nature reconciliation spec-audit outstanding CONVERGED aProbedUnit aEvidencedLens"`
