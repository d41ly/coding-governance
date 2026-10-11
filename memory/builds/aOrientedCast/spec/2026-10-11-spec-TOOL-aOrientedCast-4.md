# TOOL-aOrientedCast-4 — the build harnesses spawn their stage agents as catalogue roles

**Status:** OPEN · rev-2 · 2026-10-11 · node a · Tier-2 · base 646d4a73 · streams tooling · order 4 · ratified 2026-10-11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aOrientedCast-1-cross-read.md](../build/2026-10-11-build-TOOL-aOrientedCast-1-cross-read.md) | research | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-build-TOOL-aOrientedCast-3-agent-type-probe.md](../build/2026-10-11-build-TOOL-aOrientedCast-3-agent-type-probe.md) | research | TOOL-aOrientedCast-3 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-2-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-2-build-brief.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-3-cross-read.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-3-cross-read.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1.md) | research | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-9-1-fold-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-9-1-fold-brief.md) | journal | KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 TOOL-aOrientedCast-9 |

<!-- /gen:spec-records -->

## 1. Goal

The build harness and the unit harness spawn every agent untyped, so each one starts holding the
charter, and the craft of a spec writer or a builder lives as string literals in JavaScript the owner
cannot edit. This unit gives both harnesses the build's `roles` argument: a stage named in it spawns
as that catalogue role's agent type and its prompt leaves out the craft the role now carries, while a
stage absent from it keeps today's prompt byte for byte and the harness logs that. With a role, the
builder stops writing its spec: a divergence comes back to the caller instead of a rev bump.

## 2. Scope (IN)

- **S1** — `unattended-build.template.js` takes an optional `roles` argument: a plain object whose
  keys are drawn from `specWriter`, `committer`, `disposal`, `builder` (§8 F2), and the audit's
  `specFinder`, `skeptic` and `synthesis` (§8 F3), each value a string matching
  `AGENT_TYPE_SHAPE`, a copy of the expression `tier2-review.template.js` tests `workerType` against,
  and unequal to `none`, the review harness's reserved untyped literal. An array, a string or `null`, a
  key outside the seven, and a value failing either test each refuse by name before any agent spawns.
  `{}` and an absent `roles` both mean no stage is typed. Observed by AC2 and AC3.
- **S2** — Each `agent()` call of a stage the object names carries `agentType: roles.<stage>`: every
  spec writer of the fan (`specWriter`), the spec commit (`committer`) and the disposal (`disposal`).
  The subject resolver and the round recorder keep today's spawn options in every case. Observed by
  AC1 and AC2.
- **S3** — With a stage's role given, its prompt carries one stamp sentence after the grounding text,
  naming the type, and leaves out that stage's role spans, the table in §4 "The role spans"; every
  other sentence of it is unchanged. With the role absent, the prompt is byte-identical to base.
  Observed by AC1 and AC2.
- **S4** — At its start the build harness logs one line per key of the seven, naming the type it
  spawns or forwards, or saying the stage spawns untyped with its role prose inline because no role
  was passed; for an audit key, that the review harness keeps its own fallback for that stage.
  Observed by AC1 and AC2.
- **S5** — `dispatch.args` in the hand-out carries `roles: { builder: <type> }` when `roles.builder`
  was given, and carries no `roles` key otherwise, so a caller copying the object hands the child the
  type and nothing else. Observed by AC2.
- **S6** — `unattended-unit.js` takes an optional `roles` argument whose one legal key is `builder`,
  refused by the same shape rules with its own copy of `AGENT_TYPE_SHAPE`, because a guard in the
  parent does not travel to a child a caller composes args for. Observed by AC3.
- **S7** — With `roles.builder` given, the unit harness spawns its one agent with that `agentType`,
  its prompt carries the stamp, leaves out the builder's role span, carries the divergence hand-back
  of §4 "The builder's hand-back" in place of the order to change the spec first, and carries the
  status-only flip §4 states in place of today's status sentence. With it absent, the prompt is
  byte-identical to base. Either way the unit harness logs one line naming the builder's type or
  saying it spawns untyped. Observed by AC1 and AC4.
- **S8** — The unit harness's return gains `diverged`, true exactly when the agent returned
  `committed: false` with a `why` opening `DIVERGENCE:`, so a caller branches on a field and not on
  prose. Observed by AC4.
- **S9** — `unattended-build.js` is re-rendered from its template by the workflows kit's render step,
  and stays in parity. Observed by AC5.
- **S10** — The workflows kit's protocol-parity script gains the agent-type shape arm of §4: every
  literal a workflow script of the kit tests an agent type name against equals the one
  `tier2-review.template.js` owns. Observed by AC6.
- **S11** — The arms of AC1 to AC4 and AC7 live in `tools/workflows/unattended-build.test.sh`, whose
  `run_wf` traces each agent call's `agentType` and each `workflow()` call's `roles`; each is observed
  RED on a staged break first, and `FLOOR_ASSERTIONS` moves by the count added. Observed by AC1, AC2,
  AC3, AC4 and AC7.
- **S12** — The template's `args` header block, the unit harness's header and a new
  `tools/workflows/README.md` section, headed "roles — stage agents spawned as catalogue roles",
  document `roles`, its keys, the fallback, the hand-back and the parity arm; the review harness's
  paragraph joins that section later. NOT OBSERVED by a criterion: prose. The review reads it
  against §4.
- **S13** — The audit's `workflow()` call into the review harness carries `roles` holding those of
  `specFinder`, `skeptic` and `synthesis` this harness was given, beside its `workerType: 'none'`, and
  no `roles` key when it was given none of them. Its deferred-platform hand-back keeps the sentence
  promising a reuse of every returned lens only when the review returned `durable: true`, and
  otherwise says the re-run dispatches every judge again (§4 "The audit's roles"). Observed by AC2 and
  AC7.

## 3. Non-goals (OUT)

- The review harness's `roles`, its precedence over `workerType` and its resume key, which are
  `TOOL-aOrientedCast-5`'s. This unit's audit call forwards the audit's three review keys into it
  (S13); that harness reads them from its landing at order 5 and ignores an argument it does not
  know before then. That unit edits `tier2-review.template.js` after this one: the S10 arm reads the
  owner's literal in either of the two line forms §4 names and refuses by name when it finds neither,
  so a refactor there is loud rather than silent.
- Choosing which role a stage takes. The workflow table's `stages` mapping and the verb that prints it
  are `TOOL-aOrientedCast-1`'s and `TOOL-aOrientedCast-2`'s; this unit checks a type's shape only.
- The write gate that makes the builder's status-only flip the one spec edit it may make.
- Any role's text. The spans this unit leaves out were copied into the role files by
  `TOOL-aOrientedCast-1`, which also leaves the committer with no role.
- The drift-audit harnesses and the orientation counterfactual, which take no `roles`.
- A kit version bump. The workflows kit moves once, after its last unit.

### Edges

- **consumes-from** `TOOL-aOrientedCast-1` — the spec-writer, disposal and builder craft the role files
  now carry, and the stage keys: the `spec-write` entry's `stages` table maps `builder` and the
  audit's three review keys beside the spec writer and the disposal (§8 F2 and F3). Without it a
  role-typed prompt that leaves the spans out hands its agent less than today.
- **consumes-from** `TOOL-aOrientedCast-2` — the harness-arguments output a caller passes as `roles`
  for each of the two harnesses, whose `unattended-build` object carries all six typed stage keys.
  This unit checks that object's shape and nothing more, so the mapping of a stage to a role stays the
  catalogue's.
- **consumes-from** `TOOL-aOrientedCast-3` — the rendered agent types a `roles` value names. The stub
  criteria here need none of them; a live run spawning a type needs it rendered in a session started
  after the render.
- **hands-off** `TOOL-aOrientedCast-5` — the review harness's own `roles`, which reads the three keys
  this unit's audit forwards, its hoisted copy of the shape constant, which the parity arm here reads
  as the owner's one literal, and its paragraph in the README section on `roles` this unit opens.
- **hands-off** `TOOL-aOrientedCast-6` — the write gate's role arm, which refuses the builder's spec
  content and admits the status-only flip this unit's builder prompt asks for.
- **hands-off** `KICK-aOrientedCast-2` — the attended caller's composition: pass the harness arguments
  the catalogue prints for each harness, and on a unit returning diverged, dispatch a spec-writer
  revision of that unit's spec before dispatching the unit again.
- **hands-off** `TOOL-aOrientedCast-9` — the unattended caller's composition, which must change, and
  the unit that makes the unattended caller pass these stage keys. From the spawn guard's landing a
  harness call carrying no roles is refused, so the unattended verbs' "Drive the build as ONE program"
  bullet must pass roles from the catalogue's harness-arguments verb and branch on diverged, where
  today it says a child returning uncommitted stops the loop. The M2 cross-read moved this from a
  parked owner decision into that unit, inside the build's brief item 5.
- **hands-off** `TOOL-aOrientedCast-7` — the `roles` argument the spawn guard requires on every call
  to the two harnesses this unit teaches to read it.

## 4. Design

### Evidence

Read at `646d4a73` on 2026-10-11, node a.

- The build harness spawns five agents: the spec writers inside the bounded fan
  (`tools/workflows/unattended-build.template.js:849-879`), the spec commit (`:1056-1095`), the subject
  resolver (`:1285-1305`), the round recorder (`:1665-1683`) and the disposal (`:1856-1914`). None
  passes `agentType`. Every prompt opens with `GROUND` (`:761-788`), which the child also receives as
  `ground` through `dispatch.args` (`:2279`).
- The unit harness spawns one agent with label and schema only
  (`tools/workflows/unattended-unit.js:229`). Its prompt orders the builder to change the spec first on
  a divergence (`:183-184`) and to set the status header to CLOSED or WONTDO in the pass commit
  (`:220-223`), and it re-validates `mode` itself because the parent's guard does not travel
  (`:107-120`).
- `tier2-review.template.js` refuses a `workerType` failing `/^[A-Za-z][A-Za-z0-9_-]{0,63}$/` before any
  agent spawns (`tools/workflows/tier2-review.template.js:208-209`), and both drift-audit templates
  carry the same expression inline (`tools/workflows/drift-audit-code.template.js:92`,
  `tools/workflows/drift-audit-state.template.js:91`). Nothing compares the copies today: no suite
  names the literal.
- A workflow script cannot import, so a shared value is copied with its owner named, as
  `boundedParallel` is (`tools/workflows/unattended-build.template.js:137-155`), or rendered.
  `unattended-unit.js` ships verbatim and is never rendered.
- The protocol-parity script exits on a pair out of parity before any later arm runs
  (`tools/workflows/check-protocol-parity.test.sh:356`), and it already runs a cross-file parity arm,
  the by-design head (`:406-418`).
- A resume replays the cached answer of each agent call whose prompt is unchanged
  (`tools/workflows/unattended-build.template.js:448-450`). Whether the cache key also covers the
  options is UNVERIFIED; the stamp of S3 makes a typed prompt differ from an untyped one either way.
- `TOOL-aOrientedCast-1` leaves the committer in no `stages` table, so the catalogue's verb types the
  spec writers and the disposal as `gov-spec-writer`, the builder as `gov-builder` and the audit's
  three review keys as `gov-spec-reviewer`, `gov-skeptic` and `gov-synthesizer`, and the committer
  stays untyped; its role bodies carry the craft its §4 "What every body says" lists.
- The audit calls the review harness with `workerType: 'none'` and no `roles`
  (`tools/workflows/unattended-build.template.js:1454-1477`), and its deferred-platform hand-back
  tells the caller the re-run "reuses every lens and skeptic batch that returned" (`:1520-1550`). The
  review harness returns `durable` on every deferred return, false whenever a judge ran under a type
  (`tools/workflows/tier2-review.template.js:213-216`, `:1143`), and at base it reads no `roles` and
  refuses no argument it does not know.
- `TOOL-aOrientedCast-6` resolves its status-flip fork to an edit of the status and date cells alone,
  admitted from a `product` role on its routed unit's spec, and leaves a WONTDO, whose tail pointer
  moves a cell, to the spec writer.
- `TOOL-aOrientedCast-7` refuses a `Workflow` call whose args carry no `roles` object of known roles.

### Data model

```js
// both harnesses, beside the other args refusals; the literal is copied, not retyped
const AGENT_TYPE_SHAPE = /^[A-Za-z][A-Za-z0-9_-]{0,63}$/ // owner: tier2-review.template.js `workerType`
// unattended-build: ROLE_KEYS = ['specWriter', 'committer', 'disposal', 'builder', 'specFinder', 'skeptic', 'synthesis']
// unattended-unit:  no ROLE_KEYS; Object.keys(roles).join(',') must be '' or 'builder'
```

The unit harness tests its one legal key by comparing the joined key list with `''` and `'builder'`,
so it gains no loop and no arrow, the shape its header keeps.

The refusals, in this order, each opening with the harness's own name:

| Input | Refusal names |
|---|---|
| `roles` not a plain object | `roles`, the type received, and that it maps a stage key to an agent type |
| a key outside `ROLE_KEYS` | the key, the legal keys, and that an untyped spawn of a misspelt stage is what the refusal prevents |
| a value not a string, or failing `AGENT_TYPE_SHAPE` | `roles.<key>`, the pattern spelled out as `workerType`'s refusal spells it, and the value |
| the value `none` | `roles.<key>`, and that an untyped stage is spelled by leaving its key out, as the review harness's `roles` refusal says |

`ROLE_KEYS` is an array literal and not a definition, and the unit harness adds none, so the
codebase-map JS floor still counts that file's one top-level function.

The stamp sentence, appended to the prompt right after its grounding text:
`This stage runs as the <type> agent type: your role is your system prompt, and this message is your task. `

The hand-out's `dispatch.args` gains `roles` only when given:
`args: { repo, slug, scratch, mode, driver, ground, checklist, ...(roles.builder ? { roles: { builder: roles.builder } } : {}) }`.
The unit harness returns `{ committed, sha, why, summary, diverged }`.

### The role spans

Left out of a stage's prompt when its role is given, and kept verbatim when it is not. The sentence
around a span is rejoined so it still reads; the stage protocol, every schema, the roster, the brief
list, the `closes` lines, the `authored` naming, `AUTHOR ONLY — DO NOT COMMIT`, the commit block, the
disposal procedure with its `edges` and `placements` contract, the driver steps, the prebuild line,
the Pass trailer and the checklist stay in every case.

| Stage | Span, by its opening words | Where | Prompt with the role |
|---|---|---|---|
| `specWriter` | "against `memory/TEMPLATE-SPEC.md` at the tier the kickoff engine assigns, satisfy its section 10 reuse obligation with a real probe rather than a claim" | `unattended-build.template.js:863-865` | "Otherwise author it, and give its status header the `order` verb this roster names." |
| `specWriter` | "Every acceptance criterion names a DIRECT observation", to "stalls for hours." | `:866-868` | left out |
| `specWriter` | "DO NOT WRITE PRODUCT CODE in this stage.", to "exists to remove." | `:869-870` | left out |
| `committer` | none: the whole prompt is the commit block and its return | `:1056-1093` | unchanged but for the stamp |
| `disposal` | "A bullet written at one end only reds the hygiene gate's §3 edge join", to "the whole reason that join exists." | `:1897-1899` | left out; the rule before it and the `edges` return stay |
| `builder` | "and you read both whole before you touch code" | `unattended-unit.js:181-182` | "You are handed two documents: the BRIEF at … and the SPEC at …." |

### The builder's hand-back

With `roles.builder` given, two sentences of the unit prompt change, and this is the whole of the
change beyond the span above.

1. In place of "The spec is the design; where you must diverge, CHANGE THE SPEC FIRST as a rev-N bump
   with its section 9 line, then write the code.": "The spec is the design and you do not edit it.
   Where the code you are about to write would diverge from it, stop before writing that code, restore
   every path you changed, commit nothing, and return committed:false with a why that opens
   DIVERGENCE: and names the spec section and what it would have to say. The caller has the spec
   revised by the spec-writer role and dispatches this unit again."
2. In place of "IN THAT SAME COMMIT, set this unit's spec status header to CLOSED — or to WONTDO with
   a reason.": "IN THAT SAME COMMIT, set this unit's spec status header to CLOSED and its date to
   today, in an edit that changes nothing else in the spec: that is the one spec edit a builder makes.
   A unit you would close as WONTDO is a divergence, returned as one, because WONTDO carries a tail
   pointer only the spec writer writes." The sentence that follows today, on the header being the only
   fact `--plan` reads, stays.

The caller, not this harness, dispatches the revision: a workflow script has no filesystem and the
revision is a spec write, which is the spec-writer role's alone. §8 F1 is why the hand-back is tied to
`roles.builder` and not unconditional.

### The audit's roles

§8 F3. The audit's `workflow()` call gains one spread after `workerType: 'none'`:
`...(auditRoles ? { roles: auditRoles } : {})`, where `auditRoles` holds those of `specFinder`,
`skeptic` and `synthesis` this harness was given, and is `null` when it was given none of them.
`workerType: 'none'` stays: under the review harness's precedence it governs only a judge stage no
role names.

The deferred-platform hand-back reads the review's `durable`. When it is `false`, the clause "the
review reuses every lens and skeptic batch that returned and dispatches only <pending>" of `next`
becomes "this audit ran its judges under a role, so none wrote a lens or verify file and the re-run
dispatches every judge again"; every other sentence of `next` and `note` is unchanged. When it is
`true` or absent, `next` is base's byte for byte.

### The agent-type shape arm

In the workflows kit's protocol-parity script, after the pair loop has passed and beside the
by-design arm, with no new shell function so the generated symbol map does not move.

- Population: every tracked `*.js` directly in the kit directory, except a render whose
  `<name>.template.js` is tracked beside it, because the pair loop already holds a render to its
  template.
- From each, the `/^…$/` regex literal on every line that tests `a.workerType` or declares
  `const AGENT_TYPE_SHAPE =`. A line of either form carrying no literal, such as one calling the
  constant, contributes nothing.
- The owner is `tier2-review.template.js`. It must yield exactly one distinct literal; zero is a DEAD
  PROBE and two are an ambiguity, and both exit 1 naming the file.
- Every other literal must equal the owner's byte for byte; a difference exits 1 naming the file, the
  line and both literals. No copy at all exits 1, because a parity over the owner alone compares
  nothing.
- Green prints `protocol-parity: agent-type shape — <n> literal(s) in <m> file(s) agree with the owner`,
  both counts derived.
- Its header says what it does not check: a script that tests an agent type under another variable
  name, a render (the pair loop's), and whether the expression is a good one.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `roles` | harness argument, both harnesses | none: an argument key carries no naming cell |
| `AGENT_TYPE_SHAPE` | regex constant, one copy per harness | none: no constant cell is declared in `.lexicon.conf` |
| `ROLE_KEYS` | array constant, the build harness only | none: no constant cell is declared in `.lexicon.conf` |
| `auditRoles` | local, the build harness's forwarded audit keys | none: a local carries no naming cell |
| `diverged` | return field of the unit harness | none |
| `DIVERGENCE:` | the `why` prefix the field keys on | none |

No function is defined: the unit harness keeps its one top-level `check`, and the build harness's
additions are constants and conditional concatenation.

### Rollout

Lands at order 4, after the roles exist and their types are rendered. One commit carries both
harnesses, the re-render, the parity arm, the suite arms and the documentation. No caller passes
`roles` in this run: this session's registry predates the rendered types, so its own passes call the
harnesses untyped and see today's prompts byte for byte, which AC1 asserts. The attended router passes
`roles` from its landing, and the unattended Skill and verbs from `TOOL-aOrientedCast-9`'s, both at
order 6; from the spawn guard's landing, an untyped call is refused at the tool call.

### Files touched (estimate)

`tools/workflows/unattended-build.template.js` · `tools/workflows/unattended-build.js` · `tools/workflows/unattended-unit.js` · `tools/workflows/check-protocol-parity.test.sh` · `tools/workflows/unattended-build.test.sh` · `tools/workflows/README.md`

### Alternatives rejected

- **Leaving out the gate paragraph and the bound paragraph of the unit prompt with the role.** The
  builder role names the same discipline, but those paragraphs spell the harness's own refusals and
  timeouts and override a spec's §7, which a role body only points at. They are the stage's run rules
  and stay.
- **Treating the whole of `GROUND` as role prose.** It carries the repository, the build, the scratch
  root and the mode, which differ per run, and the unit harness refuses a `ground` that does not name
  its scratch root.
- **One shared refusal predicate rendered into both files.** The unit harness ships verbatim and is
  never rendered, so a render token reaches only one of the two; a named copy with a parity arm
  reaches both and the three that exist already.
- **The parity arm in the unit-build suite.** That suite is held off every automatic bar, so a drifted
  copy would wait for someone to run it; the protocol-parity leg runs on every bar.
- **Refusing an empty `roles` object.** The spawn guard refuses an empty object at the tool call, where
  the caller's intent is visible; inside the harness `{}` and an absent key mean the same thing, and a
  second refusal of it here would be a second answer.

## 5. Production-readiness checklist

- security — A `roles` value reaches only the `agentType` option, after the shape check, and the stamp
  sentence spells it inside a prompt; the shape admits no space, quote or backtick, so it cannot carry
  an instruction into the prompt. No new write path.
- perf / scale — One object read and at most four string tests per invocation; no added spawn.
- error / empty / loading states — Every malformed `roles` refuses before any agent spawns, naming the
  key; an absent or empty object is the logged fallback, never a silent one.
- observability — One log line per stage key says typed, forwarded or untyped; the unit harness
  returns `diverged` as a field.
- risks — A role file that lost the craft a span carried weakens a typed stage; the edge to
  `TOOL-aOrientedCast-1` and the review hold that pair. A caller that ignores `diverged` reads an
  uncommitted unit as a stop, which is today's behaviour and not a regression. A roled audit is not
  durable, so a platform deferral re-dispatches every judge; S13's hand-back says so.
- testing — The suite arms of S11 over the stub runtime, AC1's byte comparison against base, and the
  parity arm's staged breaks.
- migration — None: `roles` is optional and absent from every caller today, and its absence is
  byte-identical to base.
- user docs — The README section of S12.

## 6. Acceptance criteria

Every stub-run criterion evaluates the RENDER `tools/workflows/unattended-build.js` or
`tools/workflows/unattended-unit.js` with `node`, in the `run_wf` AsyncFunction shape of the build
harness's self-test, copied into a scratch script under the run's scratch directory and extended by
one `type:<label>:<agentType or ->` trace line per agent call and one `wfroles:<roles JSON or ->`
line per `workflow()` call; it never runs the suite. The base copies are the same two files written
from `git show 646d4a73:<path>` into the scratch directory. Inputs are the self-test's `UNITS`,
`CHILD_ARGS` and `returns` doubles; `ROLES` is
`{"specWriter":"gov-spec-writer","committer":"gov-x","disposal":"gov-spec-writer","builder":"gov-builder","specFinder":"gov-spec-reviewer","skeptic":"gov-skeptic","synthesis":"gov-synthesizer"}`.

- **AC1** — When the stub runs `UNITS` with `returns CONVERGED 0`, `UNITS` without `subjects` and
  `UNITS` with `returns NON-CONVERGENT 2`, each with no `roles`, every `promptjson:` line equals the
  base render's for the same input, byte for byte; every `type:` and `wfroles:` line reads `-`; the
  trace carries one `log:` line per key of `ROLES` saying it is untyped; and the child under
  `CHILD_ARGS` with no `roles` matches base the same way and logs one line saying its builder is
  untyped.
  Red when: any prompt byte moves with `roles` absent, a spawn carries a type nobody passed, or a stage
  falls back without a log line.
- **AC2** — When the same three runs carry `ROLES`, the `type:` lines of every `spec:`, `commit:` and
  `dispose:` agent read their stage's value and the `audit:subjects` and `audit:record` agents read
  `-`; each typed prompt carries the stamp naming its type; the `spec:` prompts lack `stalls for hours`,
  `DO NOT WRITE PRODUCT CODE` and `real probe rather than a claim` and still carry the `order` sentence
  and `Name every unit in`; the `dispose:` prompt lacks `the whole reason that join exists` and still
  asks for `edges`; the audit's `wfroles:` line reads
  `{"skeptic":"gov-skeptic","specFinder":"gov-spec-reviewer","synthesis":"gov-synthesizer"}` while its
  args still carry `workerType` `none`; and the RESULT's `dispatch.args.roles` is
  `{"builder":"gov-builder"}`. With `ROLES` minus `builder` the RESULT's `dispatch.args` has no `roles`
  key, and with `ROLES` minus the three audit keys the audit's `wfroles:` line reads `-`.
  Red when: a named stage spawns untyped, an unnamed one spawns typed, a span survives a typed prompt,
  the audit's review roles are dropped or invented, or the builder type is lost or invented on the way
  to the child.
- **AC3** — When `roles` is `[]`, `"gov-x"`, `{"specwriter":"gov-x"}`, `{"disposal":"bad name"}` or
  `{"committer":"none"}`, the parent stub THROWS a message opening `unattended-build:` that names
  `roles` or the offending key, and its trace holds no `agent:` line; when the child gets
  `{"specWriter":"gov-x"}`, `{"builder":"x y"}` or `{"builder":"none"}`, it throws opening
  `unattended-unit:` and naming the key, with no `agent:` line.
  Red when: a malformed or misspelt role reaches a spawn in either harness.
- **AC4** — When the child runs `CHILD_ARGS` with `roles` `{"builder":"gov-builder"}`, its one `type:`
  line reads `gov-builder` and its prompt carries `DIVERGENCE:` and `changes nothing else in the spec`
  and lacks `CHANGE THE SPEC FIRST` and `or to WONTDO with a reason`; with a `unit:` double returning
  `{"committed":false,"sha":"","why":"DIVERGENCE: §4 names a verb the code lacks","summary":"s"}` the
  RESULT carries `"diverged":true`, and with `why` `tests red` it carries `"diverged":false`.
  Red when: the typed builder is still told to edit its spec, or a divergence cannot be told from a
  failure by the field.
- **AC5** — When the workflows kit's render step has run, the protocol-parity script in its `--check`
  mode exits 0, `node tools/workflows/check-workflow-syntax.js` exits 0, and a `grep -c` of
  `AGENT_TYPE_SHAPE` over `tools/workflows/unattended-build.js` equals the count over
  `tools/workflows/unattended-build.template.js`, with no `{{` on any line carrying it.
  Red when: the render was not regenerated, or a token survived in it.
- **AC6** — When `{0,63}` is staged to `{0,64}` in `AGENT_TYPE_SHAPE` of `unattended-unit.js` and the
  protocol-parity script runs in its `--check` mode, it exits 1 naming `unattended-unit.js` and
  `tier2-review.template.js`; when the `a.workerType` test is staged under another variable name in
  `tier2-review.template.js` and its render alike, it exits 1 naming the owner as yielding no literal;
  and restored, it exits 0 printing the agreement line.
  Red when: a drifted copy reads in parity, or an owner that yields nothing passes.
  figure: DERIVED — both counts on the agreement line come from the population at observation time.
- **AC7** — When the stub runs `UNITS` with `ROLES` and its `workflow` double returns
  `{"exit":"deferred-platform","pending":["find:a"],"durable":false,"key":"k"}`, the RESULT's `exit` is
  `deferred-platform` and its `next` carries `dispatches every judge again` and lacks
  `reuses every lens`; when the same double returns `"durable":true` and the run carries no `roles`,
  the RESULT's `next` equals the base render's for the same input, byte for byte.
  Red when: a roled audit's deferral promises a reuse its judges never wrote, or an untyped one's moved.

## 7. Gates

`unattended-build self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `verifier fan-out` · `review-join ban (no ref-keyed join)` · `codebase-map coverage + freshness` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/unattended-build.test.sh · covers AC1 AC2 AC3 AC4 AC7 · the base harnesses, which read no roles, spawn every stage untyped and tell the builder to edit its spec · FLOOR_ASSERTIONS raised by the assertions added
New arm: tools/workflows/check-protocol-parity.test.sh agent-type shape · covers AC6 · a copy widened to {0,64}, and an owner whose test is renamed away · none

AC5 is a direct observation of the render and adds no arm.

## 8. Open questions

- **F1 — Is the builder's hand-back tied to `roles.builder`, or does it replace today's sentences in
  every call?**
  - (a) Tied to the role. Untyped, the builder keeps today's text and edits its spec as it does now.
    The fallback is byte-identical, which the brief asks of an absent role, and a repository without
    the roles kit, where no spec-writer role exists to make the revision, keeps a builder that can
    still finish a unit.
  - (b) Every call. The builder never edits spec content, typed or not. In a repository without the
    roles kit nothing revises the spec, so every divergence stops the run.
  Recommendation: (a). (b) fails the brief's fallback rule and strands every caller without the kit.
  Under the write gate an untyped builder's spec edit is refused anyway, so (a) loses nothing where
  the gate is armed.
  RESOLVED (agent, 2026-10-11, delegated): (a), S7 and §4 "The builder's hand-back".
- **F2 — Does `unattended-build` take `builder` and forward it through `dispatch.args`?** Interface 10
  of the build's spec brief pins `specWriter`, `committer` and `disposal` for this harness and
  `builder` for the unit harness alone, while the brief's paragraph for this unit says the build
  harness passes `roles.builder` on through `dispatch.args`. The M2 cross-read found the attended
  router dispatching its units untyped in that gap.
  - (a) Take `builder` and forward it as `dispatch.args.roles`, S1 and S5. A caller copying the
    hand-out hands the child its type, and the catalogue's `spec-write` entry and the
    harness-arguments verb print the key beside the other stage keys. Interface 10 gains one key for
    this harness.
  - (b) Keep interface 10. Every caller composes each unit dispatch's `roles` from a second verb call,
    the `unattended-unit` object, which is the step the cross-read found missing.
  Recommendation: (a). It satisfies this unit's own brief paragraph, which (b) cannot, and it widens
  no surface beyond the optional object this unit adds.
  RESOLVED (agent, 2026-10-11, delegated): (a), as S1 and S5 are written; the catalogue's stages
  table and the harness-arguments verb print `builder` (`TOOL-aOrientedCast-1`,
  `TOOL-aOrientedCast-2`).
- **F3 — Does the audit stage spawn its review agents as catalogue roles?** Interface 10 names no
  audit key for this harness, and the audit calls the review harness with `workerType: 'none'` and no
  `roles`, so spec review would run outside role agents, against the build's goal that spec review
  runs only in its role agents.
  - (a) Forward `specFinder`, `skeptic` and `synthesis` from this harness's `roles` into the review
    harness call's `roles`, keeping `workerType: 'none'` for a stage no role names, which is the
    review harness's precedence (`TOOL-aOrientedCast-5` §8 F1). A roled judge writes no lens or verify
    file (`TOOL-aOrientedCast-5` §8 F3), so the deferred-platform hand-back promises a reuse only when
    the review returns `durable: true`.
  - (b) Keep the audit untyped. Spec review stays outside role agents, which fails the build's goal.
  - (c) Pass `workerType: 'gov-spec-reviewer'`. Finders and skeptics spawn as one type, the skeptic
    not as `gov-skeptic` and the synthesis untyped, and the judges lose durability all the same.
  Recommendation: (a), the most feature-rich: every audit stage runs as its catalogue role, and the
  cost, a deferral that is not durable, is said in the hand-back rather than promised away. It adds no
  surface beyond the `roles` object and widens no write: the reviewing roles hold no Write tool.
  RESOLVED (agent, 2026-10-11, delegated): (a), S13 and §4 "The audit's roles"; interface 10 gains
  the three keys for this harness.

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.
- rev-2 · 2026-10-11 · S1 · S4 · S11 · S13 · §3 · §4 · AC1 · AC2 · AC7 · the M2 cross-read's findings 2
  and 5. §8 F2 raises and resolves `builder` on this harness against interface 10, and §8 F3 has the
  audit forward its three review keys into the review harness, with the deferral hand-back following
  the review's `durable`. The Edges name the catalogue and the renderer for the stage keys, and the
  parked owner decision on the unattended verbs becomes a hands-off to `TOOL-aOrientedCast-9`, with
  the reciprocal of the spawn guard's new consumes-from.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py`, asked "a workflow harness spawns each stage agent as a
caller-named agent type and refuses a malformed type name", found no existing seam that fits: it
ranked refusal classes of the process-monitor kit, the driver's `stage_or_fail` and the
`PreToolUse tools/hooks/agent-cap.js` key, none of which spawns a typed agent. The probe is blind here
and disagreed with the source: the seam is a variable in a workflow script, not a function, and the
symbol tier indexes functions. Read from source instead, the seam extended is `workerType` in
`tools/workflows/tier2-review.template.js:201-210` (`TOOL-aMendedFleet-67`): its shape expression is
copied as `AGENT_TYPE_SHAPE` and its `agentType` option shape is reused, and the closed-set argument
the child re-validates is `mode` (`TOOL-aStagedLane-2`, `tools/workflows/unattended-unit.js:107-120`).

`tools/memory-recall/query.py` was asked "how does a workflow harness choose the agent type its stage
agents spawn as, and what replaced the builder editing its own spec". It surfaced this build's brief
and agent-type probe, `TOOL-aMendedFleet-67`'s `workerType` spec, `TOOL-aMendedFleet-93`, and
`TOOL-dRetiredFork-41` and `TOOL-dRetiredFork-22` on the build harness's sidechain limits.

Recall terms used: `workerType agentType harness stage agent builder spec writer divergence rev bump hand-back resume key`
