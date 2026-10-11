# TOOL-aOrientedCast-5 — the review harness spawns each stage as the role its caller names

**Status:** INPROGRESS · rev-2 · 2026-10-11 · node a · Tier-2 · base 646d4a73 · streams tooling · order 5 · ratified 2026-10-11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aOrientedCast-1-cross-read.md](../build/2026-10-11-build-TOOL-aOrientedCast-1-cross-read.md) | research | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-build-TOOL-aOrientedCast-3-agent-type-probe.md](../build/2026-10-11-build-TOOL-aOrientedCast-3-agent-type-probe.md) | research | TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-6 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-2-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-2-build-brief.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-3-cross-read.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-3-cross-read.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1.md) | research | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 |

<!-- /gen:spec-records -->

## 1. Goal

`tier2-review.js` spawns every finder and skeptic as one caller-chosen `workerType` and its synthesis
as the platform default, with the reviewing posture spelled inside the harness's JavaScript. This
unit lets a caller hand it a `roles` object, so finders, skeptics and the synthesis each spawn as the
rendered role agent the catalogue declares, the role's constant block carries the posture, and the
harness keeps only its stage protocol. With no `roles` the harness behaves exactly as it does at BASE.

## 2. Scope (IN)

- **S1** — A new optional arg `roles`, validated in the prelude before the resume probe spawns. Absent
  reads as `{}`. Present, it must be a plain object whose every key is one of `ROLE_KEYS`
  (`diffFinder`, `specFinder`, `skeptic`, `synthesis`, interface 10) and whose every value is a string
  matching `AGENT_TYPE_SHAPE` and unequal to `none`. Anything else throws an `Error` opening
  ``tier2-review: `roles` ``, naming the offending key or value, the legal keys and the shape, before
  any agent. Observed by AC1.
- **S2** — The agent-type shape is ONE constant, `AGENT_TYPE_SHAPE`, the literal regex the `workerType`
  refusal tests at BASE, hoisted above both refusals. The `workerType` refusal and the `roles` refusal
  both test it, and no second literal of the shape is written. Observed by AC2.
- **S3** — Each stage's spawn type is resolved once, in the prelude:
  - finders: `roles.diffFinder` on a diff review, `roles.specFinder` on a spec audit, else the type
    `workerType` resolves to today (absent reads `Plan`, `none` reads the platform default);
  - skeptic batches: `roles.skeptic`, else that same `workerType` type;
  - the synthesis: `roles.synthesis`, else no `agentType`, as at BASE;
  - the resume probe: never a role and never a type, as at BASE.

  The `agent()` options of each stage carry `agentType` set to its type, or no `agentType` when it has
  none. Observed by AC3.
- **S4** — Durability follows the judge stages' resolved types. `durable` is true only when neither the
  finder type nor the skeptic type is set; then every judge prompt keeps its DURABILITY clause, and
  otherwise every judge prompt carries `Write no file. Set path to an empty string.` The return field
  `durable`, the deferred note and `renderRerunTail` read this value. With `roles` absent it equals
  `!workerType`, the BASE predicate. Observed by AC4.
- **S5** — A stage spawned under a role omits the posture sentences that role's block carries, listed
  verbatim in §4 "Prompt variants", and keeps every protocol sentence: the acquire step, the lens
  brief, the probe policy, the checklist share, the severity rubric, the verdict rules, the schemas and
  the return line. A stage spawned without a role reads byte-identically to BASE. Observed by AC5 and
  AC7.
- **S6** — The review key's input print joins `roles: { find, verify }`, the role names this run's
  finders and skeptics spawn under, or `null` for a stage that took none, ONLY when at least one of the
  two is set. The synthesis role and the other kind's finder key never join it. A run whose judges took
  no role keeps its BASE print and so its BASE key. Observed by AC6.
- **S7** — The log carries one line per stage, opening `role find:`, `role verify:` and
  `role synthesis:`, naming the type and where it came from, on every run. A finder key of the other
  kind is announced as not read. The BASE `worker type` line prints only when no judge stage took a
  role; when one did, one line says the judges' results are NOT durable. Observed by AC8.
- **S8** — When `roles` names any stage this run reads, the synthesis prompt's RUN INTEGRITY block
  gains one clause opening `Roles:` naming each stage's type, after the lens-notes clause. A run with no
  role read leaves that prompt byte-identical to BASE. Observed by AC9.
- **S9** — The `args` header comment documents `roles` as a `name:` key with its four stage keys and
  its precedence over `workerType`. Observed by AC10.
- **S10** — The template and its render land in the same commit, the render regenerated and never
  hand-edited. Observed by AC11.
- **S11** — `tools/workflows/README.md` documents `roles` for this harness, inside the `roles` section
  the build-harness unit writes there: the four keys, the precedence, the durability consequence, and
  that a caller composes the object with `<prefix>/roles/handoff.py harness-args tier2-review`.
  `memory/map/features/review-harnesses.md` gains one sentence saying a judge spawned under a role
  is a named type and writes no file. Observed by AC12.
- **S12** — `tools/workflows/tier2-review.test.sh` gains `roles:` arms for S1, S3, S4, S5, S6 and S7,
  and `FLOOR_ASSERTIONS` rises by the assertions they add. Observed by AC13.

## 3. Non-goals (OUT)

- The role files and their posture text. They are `TOOL-aOrientedCast-1`'s; this unit only stops
  restating, under a role, what those files carry.
- Moving `SEVERITY_RUBRIC` or `PROBE_RULES` into a role file. Both stay in the harness as stage
  protocol, §8 F2.
- The two drift-audit harnesses. They have no entry in the workflow catalogue, their finders write a
  durability writeup that needs a Write tool no reviewing role holds, and the brief puts them out.
- Durable judges under a role. A role type is a named type, so its judges write no lens or verify file,
  §8 F3.
- The build harness's AUDIT stage. Its call into this harness is `TOOL-aOrientedCast-4`'s, which the
  M2 cross-read had forward `specFinder`, `skeptic` and `synthesis` beside its `workerType: 'none'`
  (that spec's §8 F3), so the gap this bullet recorded at rev-1 is closed there and not here.
- `REVIEW_SHAPE`. It does not move: a run with no judge role is byte-identical to BASE, and a run with
  one is keyed apart by S6 and writes no file a later run could reuse.
- The review protocol and BUILD-METHOD M8's call shape. Neither changes here; once the spawn guard
  requires `roles` on every harness call, the main loop's M8 composition must carry one, which is the
  attended router's and the spawn guard's concern.
- A kit-version bump. The review-harness kit moves once, after this build's last unit touching it.
- The spawn guard's rule that a harness call carry a roles object. `TOOL-aOrientedCast-7` owns it, and
  its Rollout section names this unit as a precondition of its landing; the Edges below carry the
  hands-off.

### Edges

- **consumes-from** `TOOL-aOrientedCast-1` — the four review role files whose blocks carry the posture
  this harness omits under a role: the finders' concreteness and scope discipline, and the skeptic's
  try-to-refute stance. Without them a roled stage runs with that posture stated nowhere.
- **consumes-from** `TOOL-aOrientedCast-2` — the harness-arguments verb's output for this harness,
  whose four stage keys are the closed set S1 accepts. Without it a caller has no derived object to
  pass, and composes one by hand.
- **consumes-from** `TOOL-aOrientedCast-4` — the protocol-parity script's agent-type shape arm, which
  reads this harness as the owner of the one shape literal, from a line that declares the shared
  constant or tests `workerType`; and the README section on `roles` this unit extends. Without the
  arm, S2's single literal is held by nothing after this pass.
- **hands-off** `KICK-aOrientedCast-2` — composing the closing review's call with a roles object
  printed by the handoff renderer's harness-arguments verb.
- **hands-off** `TOOL-aOrientedCast-9` — the same composition for an unattended run's closing review,
  which the unattended verbs carry.
- **hands-off** `TOOL-aOrientedCast-7` — the `roles` argument the spawn guard requires on every call
  to this harness.
- **hands-off** external — giving the drift-audit harnesses roles. It needs a catalogue entry for them
  and a reviewing role that may write its own writeup, and both sit outside this build.

## 4. Design

### Evidence

Read at HEAD `744e55db` of the run branch, whose `tools/` tree equals base `646d4a73` (`git diff
--stat 646d4a73 HEAD -- tools skills` prints nothing).

- `workerType` is resolved and refused at `tools/workflows/tier2-review.template.js:207-209`; the
  refusal tests `/^[A-Za-z][A-Za-z0-9_-]{0,63}$/` inline and spells the same shape again inside its
  message. `judgeOpts` (line 210) is the only spawn option derived from it, and it is passed to every
  `find:` call (line 1054) and every `verify:` call (line 1263), never to `resume:probe` or `synth`.
- `durable` is `!workerType` (line 214); `renderRerunTail` (215-219) reads it; the `worker type` log
  line (220-221) prints when a type is named.
- Every finder prompt chooses DURABILITY or "Write no file" on `workerType` (1048-1050); so does every
  skeptic prompt (1255-1258).
- The posture sentences sit at lines 1025 and 1031 (finder identity), 1041 and 1042 (the "No
  speculation, no style nits" clause), 1217 and 1227 (the skeptic's "You are an adversarial skeptic.
  For EACH finding below, try hard to REFUTE it").
- `inputPrint` (823-824) joins `workerType` only when it names a type, so a `none` key equals every
  pre-type key. That is the precedent S6 follows.
- The synthesis is spawned at line 1720 with `{ label: 'synth', phase: 'Synthesize', schema }` and no
  `agentType`. Its RUN INTEGRITY block's lens-notes clause ends at line 1616.
- `LENSES` is the marked ternary over two sibling array literals (line 686), the one dialect
  `tools/hooks/agent-cap.js` admits. Nothing here touches either receiver or `batches`.
- `tools/workflows/tier2-review.test.sh` evaluates the render as an `AsyncFunction` with recording
  `agent` stubs (`runReview`, line 252) and records each spawn's `agentType`. Its D9 arm (around line 226)
  asserts every field read off the `a` alias is documented as a `name:` key in the header block.
  `FLOOR_ASSERTIONS` is 273 at BASE (line 1901), PINNED at that read.
- The role catalogue (`TOOL-aOrientedCast-1`, its "workflow table") maps `diffFinder`, `skeptic` and
  `synthesis` to `gov-diff-reviewer`, `gov-skeptic` and `gov-synthesizer` under `closing-review`, and
  `specFinder` to `gov-spec-reviewer` under `spec-review`; both entries name this harness. Its role
  table gives the three judges Read, Grep, Glob and Bash and no Write, and gives the synthesizer Write.
  Its hands-off to this unit says the rubric and the probe rules stay here as stage protocol.
- The agent-type probe (`memory/builds/aOrientedCast/build/2026-10-11-build-TOOL-aOrientedCast-3-agent-type-probe.md`)
  measured that a `Workflow` `agent()` given `agentType` reports that name in every hook payload.

### Prelude — the argument and the resolved types

Placed directly after the `workerType` refusal and before `const context`:

```js
const AGENT_TYPE_SHAPE = /^[A-Za-z][A-Za-z0-9_-]{0,63}$/   // hoisted; the workerType refusal tests it too
const ROLE_KEYS = ['diffFinder', 'specFinder', 'skeptic', 'synthesis']
const roles = a.roles === undefined ? {} : a.roles
// refuse: not a plain object; a key outside ROLE_KEYS; a value that is not a string,
// fails AGENT_TYPE_SHAPE, or is 'none'. One throw per offence, each opening "tier2-review: `roles`".
const finderKey = isSpec ? 'specFinder' : 'diffFinder'
const otherFinderKey = isSpec ? 'diffFinder' : 'specFinder'
const findType = roles[finderKey] || workerType
const verifyType = roles.skeptic || workerType
const synthType = roles.synthesis || ''
const roledJudges = !!(roles[finderKey] || roles.skeptic)
const findOpts = findType ? { agentType: findType } : {}
const verifyOpts = verifyType ? { agentType: verifyType } : {}
const synthOpts = synthType ? { agentType: synthType } : {}
const durable = !findType && !verifyType
```

The `workerType` refusal's message interpolates `AGENT_TYPE_SHAPE.source` rather than retyping the
shape, so its text stays byte-identical. The constant's name is the one `TOOL-aOrientedCast-4` gives
its copies in the two build harnesses, and that unit's protocol-parity arm reads this file's
`const AGENT_TYPE_SHAPE =` line as the owner's one literal; a line that only calls the constant
contributes nothing there, so the owner still yields exactly one. `judgeOpts` gives way to the two
per-stage option objects; under no role both equal it.

The precedence is §8 F1's: a role names a stage, `workerType` covers a judge stage no role names, and
the synthesis, which `workerType` never governed, takes a role or nothing.

### Prompt variants — what a roled stage omits

Each variant is chosen per stage by whether that stage's type came from `roles`: `roles[finderKey]` for
finders, `roles.skeptic` for skeptics. The unroled text is BASE's, byte for byte.

| Stage, kind | BASE text kept unroled | Under a role |
|---|---|---|
| finder, diff | `You are the ${L.key} reviewer. Review ONLY the diff named under SUBJECT above (…)` | the opening `You are the ${L.key} reviewer. ` omitted |
| finder, spec | `You are the ${L.key} reviewer of a SPEC SET. For EACH subject listed under SUBJECT above: …` | the opening `You are the ${L.key} reviewer of a SPEC SET. ` omitted |
| finder emit, diff | `… a proposed fix. No speculation, no style nits, nothing outside the diff. If nothing real, …` | `… a proposed fix. Nothing outside the diff. If nothing real, …` |
| finder emit, spec | `… at HEAD. No speculation, no style nits. If nothing real, …` | `… at HEAD. If nothing real, …` |
| skeptic, spec | `You are an adversarial skeptic. For EACH finding below, try hard to REFUTE it. Read the cited spec …` | `For EACH finding below, read the cited spec …` |
| skeptic, diff | `You are an adversarial skeptic. For EACH finding below, try hard to REFUTE it — read the actual code …` | `For EACH finding below, read the actual code …` |

The `LENS:` line still opens with the lens's own name, so a roled finder knows which lens it is. The
synthesis prompt has no posture sentence; under a role only its options and S8's clause move.

### Durability and the re-run texts

`renderRerunTail` keeps its two BASE strings and reads `durable`. A run where any judge took a type
writes no judge file, so "this run wrote no result file" stays true: the untyped judge stage of a mixed
run is told to write no file as well (§8 F3). The `worker type ${workerType} — …` line prints under
`if (workerType && !roledJudges)`; under `if (!durable && roledJudges)` this line prints instead:

```
judges under a named type — no finder or skeptic writes a find-*.json or verify-*.json, so this run's lens and batch results are NOT durable and a resume re-dispatches them
```

### Log lines

```
role find: <findType, or the platform default> — <roles.<finderKey> | workerType | no roles.<finderKey>, and workerType is none>
role verify: <verifyType, or the platform default> — <roles.skeptic | workerType | no roles.skeptic, and workerType is none>
role synthesis: <synthType, or the platform default> — <roles.synthesis | no roles.synthesis, as before roles>
role find: roles.<otherFinderKey> is not read on a <kind>        (only when that key is present)
```

### The input print

```js
Object.assign({ shape: REVIEW_SHAPE, …BASE keys… }, workerType ? { workerType } : {},
  roledJudges ? { roles: { find: roles[finderKey] || null, verify: roles.skeptic || null } } : {})
```

The KEY comment block above `REVIEW_SHAPE` gains one sentence naming `roles` and why the synthesis
role stays out: no keyed file is written by the synthesis, so its role cannot make a file stale.

### RUN INTEGRITY clause

When `roles` names a stage this run reads (the kind's finder key, `skeptic` or `synthesis`), one clause
follows the lens-notes clause:

```
Roles: finders <findType or the platform default>, skeptic batches <verifyType or the platform default>, synthesis <synthType or the platform default>.
```

### Rollout

This session read its agent registry before `.claude/agents/` existed, so no pass of this run can
spawn a rendered role type; every criterion here is observed against stub runtimes. A real roled
review first runs in a session started after `TOOL-aOrientedCast-3`'s render lands. Until a caller
passes `roles`, nothing changes for anyone: the build harness's audit, M8's closing review and the
drift harnesses all call with none.

### Inventory

Mints the constants `AGENT_TYPE_SHAPE` and `ROLE_KEYS` and the locals `roles`, `finderKey`,
`otherFinderKey`, `findType`, `verifyType`, `synthType`, `roledJudges`, `findOpts`, `verifyOpts` and
`synthOpts`. No function is minted, so no `js.function` cell is graded and the map's symbol inventory
does not move. No codebase-map inventory key moves.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/README.md`
- `memory/map/features/review-harnesses.md`

### Alternatives rejected

- **Joining the whole `roles` object into the print.** A change to the synthesis role, or to the other
  kind's finder key a caller composes with every call, would re-key a run whose durable lens files are
  still correct, and re-dispatch every lens for nothing.
- **Keeping the posture sentences under a role.** The owner edits a role's block to change how its
  agent behaves; a harness sentence restating the old posture beside it would contradict the edit in
  the same context. Two copies of one rule is the defect.
- **A per-stage durability, the untyped stage writing its files in a mixed run.** A finder re-dispatch
  renumbers the findings, so a skeptic file keyed on the old ids is never reused, and the rerun texts
  would need a third and fourth string for a gain that only a finders-unroled, skeptics-roled run sees.

## 5. Production-readiness checklist

- security — `roles` reaches only `agentType` options and log text; no value is interpolated into an
  agent prompt except S8's clause, which carries names `AGENT_TYPE_SHAPE` admits, so no control
  character or newline can forge a prompt line. A role's tool grant is the catalogue's, not this
  harness's.
- perf / scale — none: the spawn count, the fan-out receivers and the batches are unchanged.
- error / empty / loading states — an absent `roles` and `{}` behave as BASE; a malformed one refuses
  before any agent. A well-formed role the platform does not know comes back as a dead agent, which the
  harness already counts and defers on.
- observability — S7's three lines on every run and S8's clause in the record name every stage's type
  and its source, so a reader can tell a roled review from a classic one.
- risks — a role file without the posture this harness omits runs a softer finder or skeptic; that is
  `TOOL-aOrientedCast-1`'s acceptance to hold. Bug classes the checklist selects for these paths:
  `two-answers-to-one-question` (one shape constant, S2), `degradation-known-but-unreported` (S7, S8)
  and `fold-text-is-unreviewed-surface`.
- testing — the stub-run criteria below in the pass; the `roles:` suite arms run once at the close.
- migration — none for data. Every existing caller passes no `roles` and is unchanged.
- user docs — S11's README section and dossier sentence.

## 6. Acceptance criteria

The stub run is `tools/workflows/tier2-review.js` evaluated as an `AsyncFunction` with recording `agent`
doubles, the `runReview` shape of `tools/workflows/tier2-review.test.sh`, copied into a scratch driver
`t2roles.js` under the session scratchpad and run with `node`. It is not the suite and runs in seconds.
The full-role arg set is `roles: { diffFinder: 'gov-diff-reviewer', specFinder: 'gov-spec-reviewer',
skeptic: 'gov-skeptic', synthesis: 'gov-synthesizer' }`.

- **AC1** — When the stub run evaluates diff args carrying each of `roles: null`, `[]`, `'gov-skeptic'`,
  `{ finder: 'x' }`, `{ skeptic: '' }`, `{ skeptic: '1bad' }`, `{ skeptic: 'none' }`, `{ skeptic: 7 }`
  and `{ synthesis: 'a b' }`, each throws a message opening ``tier2-review: `roles` `` that names the
  offending key or value, and the trace holds no spawn; `{}` and the full-role set proceed.
  Red when: a malformed value reaches a spawn, or a refusal names nothing.
- **AC2** — When `grep -c "AGENT_TYPE_SHAPE.test(" tools/workflows/tier2-review.template.js` runs it
  prints 2, and `grep -c "{0,63}\$/" tools/workflows/tier2-review.template.js` prints 1; and the
  workflows kit's protocol-parity script, run in its check mode, prints its agent-type shape line with
  this file as the owner of one literal.
  Red when: the `roles` refusal tests a literal of its own, the `workerType` refusal still does, or the
  hoist left the shape arm with zero or two owner literals.
- **AC3** — When the stub run evaluates diff args with the full-role set and no `workerType`, every
  `find:` spawn carries `agentType` `gov-diff-reviewer`, every `verify:` spawn `gov-skeptic`, `synth`
  `gov-synthesizer` and `resume:probe` none; the same over spec args gives `find:` spawns
  `gov-spec-reviewer`. With `roles: { skeptic: 'gov-skeptic' }` and no `workerType`, `find:` spawns
  carry `Plan`, `verify:` spawns `gov-skeptic` and `synth` none. With `roles: { synthesis:
  'gov-synthesizer' }` and `workerType: 'none'`, `find:` and `verify:` spawns carry none and `synth`
  carries `gov-synthesizer`.
  Red when: a role is ignored, a stage it does not name moves, or the probe takes a type.
- **AC4** — When the stub run evaluates diff args with `roles: { diffFinder: 'gov-diff-reviewer' }` and
  `workerType: 'none'`, every `find:` and `verify:` prompt carries `Write no file` and none carries
  `DURABILITY`, and with every `find:` stub returning null the result carries `durable: false` and the
  note says every finder and skeptic is dispatched again; with `roles: { synthesis: 'gov-synthesizer' }`
  and `workerType: 'none'` every judge prompt carries `DURABILITY` and the same dead-lens run returns
  `durable: true`.
  Red when: a roled judge is told to write a lens file, or `durable` ignores the role.
- **AC5** — When the stub run evaluates diff and spec args with the full-role set, no `find:` prompt
  contains `You are the ` or `No speculation, no style nits`, and no `verify:` prompt contains
  `You are an adversarial skeptic` or `try hard to REFUTE`; every diff `find:` prompt still contains
  `Review ONLY the diff named under SUBJECT above` and `Nothing outside the diff.`, every spec `find:`
  prompt `For EACH subject listed under SUBJECT above` and `PROBE POLICY`, every `verify:` prompt
  `SEVERITY RUBRIC` and `WHEN YOU CANNOT ESTABLISH A FINDING`. With `roles: { skeptic: 'gov-skeptic' }`
  alone, the `find:` prompts still contain `You are the `.
  Red when: a roled stage restates its role's posture, or a protocol sentence went with it.
- **AC6** — When the stub run returns `result.key` for diff args, the keys of `roles` absent, `{}`,
  `{ synthesis: 'gov-synthesizer' }` and `{ specFinder: 'gov-spec-reviewer' }` are equal; the key of
  `{ skeptic: 'gov-skeptic' }` differs from them; and two full-role runs differing only in the
  `diffFinder` value return different keys.
  Red when: a judge role does not join the print, or the synthesis role or the other kind's finder does.
- **AC7** — When `t2roles.js --compare base.js tools/workflows/tier2-review.js` runs diff args at round
  1 with `checklist` and `specs`, diff args at round 2 with `priorFindings`, and spec args at round 1,
  each under `workerType` absent, `'none'` and `'Plan'` and no `roles`, every traced prompt, every
  `agentType` and every `result.key` is byte-identical between the two renders, and the logs are
  identical once lines opening `role ` are set aside.
  Red when: a no-role run moved anywhere, which is the regression this unit must not ship.
  fixture: `base.js` is `tools/workflows/tier2-review.js` as `git show` prints it at base `646d4a73`,
  saved to the scratchpad, never read from a working copy.
- **AC8** — When the stub run evaluates diff args with `roles: { skeptic: 'gov-skeptic', specFinder:
  'x' }` and no `workerType`, the log holds `role find: Plan — workerType`, a `role verify:` line
  naming `gov-skeptic` and `roles.skeptic`, a `role synthesis:` line naming `no roles.synthesis`, the
  line `role find: roles.specFinder is not read on a diff-review`, the `judges under a named type` line,
  and no line opening `worker type`.
  Red when: a stage's source goes unlogged, or the BASE line claims every judge spawns as `Plan`.
- **AC9** — When the stub run evaluates diff args with `roles: { synthesis: 'gov-synthesizer' }`, the
  `synth` prompt contains `Roles: finders` once, after `lens notes`; with `roles` absent it contains
  no `Roles:`.
  Red when: the record cannot say a review ran under roles, or a classic run's prompt moved.
- **AC10** — When the self-test's header predicate (every field read off the `a` alias has a `name:`
  key in the block from `// --- inputs (via Workflow` to `// S5 (TOOL-aGuardedTally-1)`) runs over
  `tools/workflows/tier2-review.template.js` in a scratch `node -e` probe, it reports no missing field.
  Red when: `a.roles` is read and the header lacks `roles:`.
- **AC11** — When the template is rendered with `{{FANOUT_CAP}}` replaced by the value
  `bash tools/workflows/check-verifier-fanout.sh --print-cap` prints, the result equals
  `tools/workflows/tier2-review.js` byte for byte with carriage returns stripped from both, and
  `bash tools/check-install-prefix.sh --offenders` prints no key naming a file this unit touched.
  Red when: the render was hand-edited, or the README spells a sibling kit's path by literal.
  figure: the cap is DERIVED from the hook at observation time.
- **AC12** — When `grep -c "harness-args tier2-review" tools/workflows/README.md` runs it prints at
  least 1 where BASE prints 0, the same section names `diffFinder`, `specFinder`, `skeptic` and
  `synthesis`, and `grep -c "under a role" memory/map/features/review-harnesses.md` prints at least 1
  where BASE prints 0.
  Red when: the arg ships undocumented.
- **AC13** — When a scratch slice of the review suite (its prologue and the new `roles:` block, with
  `HERE` pointed at the kit directory, run as a file outside the tree) runs against the new render it passes, and
  against a scratch render whose `roles` refusal is commented out it fails at least one `roles:` arm;
  `grep -c "roles:" tools/workflows/tier2-review.test.sh` prints at least 8 where BASE prints 0, and
  the `FLOOR_ASSERTIONS` line reads its BASE value plus the assertions the new block adds, with a
  `RAISED` comment line counting them.
  Red when: an arm cannot fail, or the floor did not move with the arms.
  figure: DERIVED from the pass's own diff; BASE's floor is 273.
  permission: the whole suite runs once at the close, never in this pass.

## 7. Gates

`tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `review-join self-test` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `install-prefix (shipped surface)` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · covers AC1 AC3 AC4 AC5 AC6 AC8 · a `roles:` block over the stub runner, each arm against a render lacking the refusal, the routing or the variant · `FLOOR_ASSERTIONS` raised by the assertions added

## 8. Open questions

- **F1 — When a caller passes both `workerType` and `roles`, which decides a stage's type?**
  (a) A role decides the stage it names; `workerType` keeps every judge stage no role names; the
  synthesis takes a role or nothing. (b) `workerType`, when given, wins over every role. (c) Refuse
  the pair. Option (b) cannot tell an explicit `Plan` from the absent default that reads as `Plan`, so
  every roles-only caller would have its roles overridden. Option (c) forbids the one mixed call that
  has a use, a caller pinning `workerType: 'none'` for durable judges while naming a synthesis role,
  and interface 10 already says a stage absent from `roles` keeps today's spawn options, which is (a).
  Recommendation: (a).
  RESOLVED (agent, 2026-10-11, delegated): (a), as S3 is written.
- **F2 — Do the severity rubric and the probe rules move into the finder role block?** The brief's
  unit paragraph says the finder role carries what every lens shares, naming those two. (a) Move
  them, the harness omitting them under a role. (b) Keep both in the harness on every path; the role
  block carries the craft and points at them. Option (a) is rejected by a probe, not a preference:
  `grep -n "SEVERITY_RUBRIC +" tools/workflows/tier2-review.template.js` finds the rubric interpolated
  into the finder, skeptic and synthesis prompts, worded per kind, and `gov-skeptic` and
  `gov-synthesizer` each serve both kinds, so a role file would need both wordings and the disposal
  stage would read grades from a text the harness cannot see. `PROBE_RULES` joins the input print
  (line 823), which no role file can. `TOOL-aOrientedCast-1`'s hands-off to this unit already reads
  the same way.
  Recommendation: (b).
  RESOLVED (agent, 2026-10-11, delegated): (b); S5 omits posture only.
- **F3 — Are judges spawned under a role durable?** (a) No: a role is a named type, and every judge of
  a run with any roled judge writes no file. (b) Yes: tell roled judges to write their files, which
  needs a Write tool on the finder and skeptic roles. Option (b) widens the reviewing roles' write
  surface beyond what the catalogue grants them, M3's veto 3, and the catalogue gives them none.
  Recommendation: (a). A durable roled review needs the owner to grant reviewing roles a Write tool.
  RESOLVED (agent, 2026-10-11, delegated): (a), as S4 is written.

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, from the template and its render at base `646d4a73`, the
  self-test's stub runner, the role catalogue's workflow and role tables, and the agent-type probe.
- rev-2 · 2026-10-11 · §3 · the M2 cross-read's findings 3 and 5, reciprocated here: the spawn guard
  and the unattended caller each declare a consumes-from naming this unit, so the Edges carry both
  hands-offs, and the audit non-goal names `TOOL-aOrientedCast-4` §8 F3 as where the audit's roles are
  now forwarded. No design moves.

## 10. Reuse audit

Three seams are extended and none is rebuilt. The `workerType` refusal's shape is hoisted into one
constant both refusals test (`tools/workflows/tier2-review.template.js:207-209`, `TOOL-aMendedFleet-67`).
The per-stage options follow `judgeOpts` (line 210), split by stage. The print join follows the
`workerType` precedent at line 823, which joins only when a type is named so a classic key never moves.
`python tools/codebase-map/reuse_lookup.py "spawn each review stage's agents as a caller-named agent
type, per stage"` returned only name-stem matches, `measure_typed_counts`, `stage_or_fail` and
`derive_review_exit` among them, none a spawn-type seam: the harness's `judgeOpts` is a constant, not a
symbol, and the lookup reads symbols, so the seam was found by reading the source. Recall returned
`TOOL-aMendedFleet-67` (the `workerType` arg and its print rule), `TOOL-aMendedFleet-93` (absent reads
`Plan`), `TOOL-aMendedFleet-111` (true re-run texts under a named type), `TOOL-dDerivedDocket-29` (the
review key) and `TOOL-aEvidencedLens-13` (a diff-kind prompt observed unmoved against BASE, the shape
AC7 copies).

Recall terms used: workerType agentType judges Plan durable review key inputPrint lens skeptic synthesis resume
