# TOOL-dFairHearing-43 — seven of the closing diff review's eight minors: caller refs refused before any agent, one cell encoding, every pin key routed, one sibling-kit resolver, and arms over every preset

**Status:** CLOSED · rev-4 · 2026-11-04 · node d · Tier-2 · base 23e1a54d · streams tooling · order 29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-TOOL-dFairHearing-1-agent-ledger.md](../build/2026-11-03-build-TOOL-dFairHearing-1-agent-ledger.md) | journal | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 TOOL-dFairHearing-20 TOOL-dFairHearing-21 TOOL-dFairHearing-22 TOOL-dFairHearing-23 TOOL-dFairHearing-25 TOOL-dFairHearing-26 TOOL-dFairHearing-27 TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-30 TOOL-dFairHearing-31 TOOL-dFairHearing-32 TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-35 TOOL-dFairHearing-36 TOOL-dFairHearing-37 TOOL-dFairHearing-38 TOOL-dFairHearing-39 TOOL-dFairHearing-40 TOOL-dFairHearing-44 TOOL-dFairHearing-45 TOOL-dFairHearing-46 |
| [2026-11-04-build-TOOL-dFairHearing-43-1-acceptance-ledger.md](../build/2026-11-04-build-TOOL-dFairHearing-43-1-acceptance-ledger.md) | journal | — |
| [2026-11-04-build-TOOL-dFairHearing-43-1-builder-return.md](../build/2026-11-04-build-TOOL-dFairHearing-43-1-builder-return.md) | journal | — |
| [2026-11-04-build-TOOL-dFairHearing-43-2-builder-return.md](../build/2026-11-04-build-TOOL-dFairHearing-43-2-builder-return.md) | journal | — |
| [2026-11-04-build-TOOL-dFairHearing-43-3-builder-return.md](../build/2026-11-04-build-TOOL-dFairHearing-43-3-builder-return.md) | journal | — |
| [2026-11-04-build-TOOL-dFairHearing-43-4-builder-return.md](../build/2026-11-04-build-TOOL-dFairHearing-43-4-builder-return.md) | journal | — |
| [2026-11-04-build-TOOL-dFairHearing-43-deviation-431.md](../build/2026-11-04-build-TOOL-dFairHearing-43-deviation-431.md) | deviation | — |
| [2026-11-04-prompt-TOOL-dFairHearing-43-1-spec-writer.md](../prompts/2026-11-04-prompt-TOOL-dFairHearing-43-1-spec-writer.md) | journal | — |
| [2026-11-04-prompt-TOOL-dFairHearing-43-2-spec-writer.md](../prompts/2026-11-04-prompt-TOOL-dFairHearing-43-2-spec-writer.md) | journal | — |
| [2026-11-04-prompt-TOOL-dFairHearing-43-build-brief.md](../prompts/2026-11-04-prompt-TOOL-dFairHearing-43-build-brief.md) | research | — |
| [2026-11-04-prompt-TOOL-dFairHearing-43-spec-brief.md](../prompts/2026-11-04-prompt-TOOL-dFairHearing-43-spec-brief.md) | research | — |
| [2026-11-04-prompt-TOOL-dFairHearing-43-split-fix-brief.md](../prompts/2026-11-04-prompt-TOOL-dFairHearing-43-split-fix-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

This batch unit closes seven of the eight confirmed findings of the build's closing diff review,
`memory/builds/dFairHearing/reviews/2026-11-04-review-TOOL-dFairHearing-1-40-diff-review.md`, round 1,
CLEAN WITH FIXES and CONVERGED: MEDIUM ids 1, 2, 3, 4 and 7 (items 1 to 5) and LOW ids 6 and 8 (items
7 and 8). LOW id 5 (item 6) is split: this unit writes its class record, and its docstrings are the
second batch unit, `TOOL-dFairHearing-44`. The build method's severity rule promotes every confirmed
finding at a diff exit and batches every MEDIUM and LOW into one unit naming them all, or two across
disjoint write sets. Each item carries the fix the skeptic judged sound, re-grounded at `23e1a54d`,
and the gate or catalogue record that keeps its class from returning. The four findings disposed `new:<class>` (ids 1, 5, 6 and 8) each gain a class record in
the bug-class catalogue.

## 2. Scope (IN)

Each item names its report id, its report item and the criterion that observes it, in the order of
the record's `## Items`. The ids S8 and AC8 are unused: id 5's docstrings moved to
`TOOL-dFairHearing-44`, and the later ids keep their numbers.

- **S1** — id 1 (item 1, MEDIUM). On the diff kind, before any agent and at every round, `base` and
  `head` must each match `REF_SHAPE`, `/^[0-9A-Za-z._\/~^][0-9A-Za-z._\/~^-]*$/`; any other value
  throws an error opening `tier2-review:` that names the field, in backticks, and the value. The check
  sits beside the diff kind's `base` requirement (`tools/workflows/tier2-review.template.js:287-296`),
  so the checklist agent's `--for-diff ${base}..${head}` line (:1428) and the resume probe's two
  `rev-parse --verify` commands (:1597) only receive a value inside the shape. The round-1 WARNING on a
  `base` that is not a pinned sha (:968-976) is unchanged. The render `tools/workflows/tier2-review.js`
  is regenerated. Observed by AC1.
- **S2** — id 2 (item 2, MEDIUM). `renderCell` (:2445) owns the encoding of the appendix the harness
  returns. The `none` branch of `checkDisposition` (:3049-3053) keeps two tests, the `unclassed`
  admission and the non-empty reason, and its comment says the returned cell is encoded by
  `renderCell`. The DISPOSITIONS prompt (:2752-2753) tells the synthesis the harness encodes that cell,
  so the returned reason is plain text, and it no longer asks for a pipe written as `\|`. The appendix
  the synthesis writes into the record is outside `renderCell`, so the appendix-copy instruction
  (:2875-2876) takes that rule: after its `none — <reason>` clause it adds a sentence opening
  `In that cell, which you write and the harness does not encode,` that asks for the reason on one
  line and each `|` written as `\|`. The workflows README's appendix sentence
  (`tools/workflows/README.md:631-635`) says the same of both copies, and that a raw `|` or a line
  break in a returned reason refuses nothing. Its reader in the review harness suite, the
  `FH23 AC23` arm (`tools/workflows/tier2-review.test.sh:3085-3097`), becomes the round-trip arm the
  Gates section declares. Observed by AC2.
- **S3** — id 3 (item 3, MEDIUM). The audit's review call
  (`tools/workflows/unattended-build.template.js:1752-1759`) forwards `twin`, `unclassed`, `fixJudge`
  and `walk` as it forwards `optIn`, `preset` and `lensNotes`: unchanged, unchecked, and no key when
  the caller passed none. `twin`, `unclassed` and `walk` are the keys `review_pin.py` prints beside
  `preset` and `optIn` (`tools/workflows/review_pin.py:122-126`), and `fixJudge` is the rest of the
  skeptic's fix. The args block (:230-239) documents the four, and the workflows README's forwarding
  sentence (`tools/workflows/README.md:555-556`) names all seven. The render
  `tools/workflows/unattended-build.js` is regenerated. Observed by AC3.
- **S4** — id 4 (item 4, MEDIUM). `spec-audit-optin.js` finds the hooks kit the way agent-cap finds
  the pack: `loadReaders` reads both readers from the directory `resolveKitDir('hooks', 'agent-cap.js',
  __dirname)` returns, and that call stands where the hard-coded sibling path stood
  (`tools/workflows/spec-audit-optin.js:24`). The resolver is an inline copy of agent-cap's, between
  the same `// >>> resolveKitDir` and `// <<< resolveKitDir` markers
  (`tools/hooks/agent-cap.js:989-1024`), since a copy-installed kit carries shared code inline. A
  refusal reaches the existing load-failure deny (:249-261), whose remedy names the resolver's message,
  the three places it looked, in place of "Install the hooks kit beside the review kit". The two
  README sentences on where the pack finds the hooks kit say so (`tools/workflows/README.md:196-200`,
  `tools/hooks/README.md:184-185`), and so do the pack's header comment (:16-20) and the comment above
  the suite's arms (`tools/workflows/spec-audit-optin.test.sh:550-554`). The suite's arm at
  `tools/workflows/spec-audit-optin.test.sh:566`, which expects `could not be loaded` with no hooks kit,
  changes with that text: its needle becomes `looked in`, words of the resolver's message. The arm
  above it (:565) still finds `agent-cap.js` in that message, and the `scratch-guard.js` arm (:573)
  still reaches the load failure at :33. Observed by AC4 and AC5.
- **S5** — id 4, the copy's parity. The python resolver suite's JS-port behaviour section
  (`tools/lib/resolve-python.test.sh:693-750`) runs its nine layouts over each marked block, the
  hook's and the pack's, and requires the two blocks byte-identical. Observed by AC5.
- **S6** — id 4, the class. A ban beside that suite's idiom bans: no tracked JS file under `tools/`
  joins `dirname(__dirname)` to a quoted name, on a line that is not a comment. Run over the tree at
  `23e1a54d`, the predicate names two lines: the pack's :24 and `tools/hooks/agent-cap.js:403`, where
  the hook builds the path of the policy kit's `policy-mirror.js`, read by the writer bound and by the
  settings-in-force rule. That second site resolves `resolveKitDir('policy', 'policy-mirror.js',
  __dirname)`, a refusal reading as the absent helper it reads as today, so a tree with no policy kit
  still falls back to `MAX_VERIFIERS` and the settings-in-force rule still stands down (F1). The
  hook's header comment (:39-40) and the hooks README (`tools/hooks/README.md:212-213`) say how the
  helper is found. Observed by AC6.
- **S7** — id 7 (item 5, MEDIUM). The review harness suite's spaced-repo quoting runs over every
  preset the harness ships, not over the diff kind alone: `unit-spec` at round 1, a `unit-spec` round-2
  fold whose subject's `prevBlob` differs from its blob, `design-audit` and `whole-design`, each with
  `repo` `C:/x y/z`. Every `git -C` match in each run equals `git -C "C:/x y/z"`, and the spec runs carry
  the probe's hash-object command and the acquire sentence's hash-object and diff commands
  (:1594, :1823, :1825). The `FH40 AC19` arm's label then claims what its runs show. Observed by AC7.
- **S9** — id 6 (item 7, LOW). The comment at `tools/workflows/kit.toml:78` names the argument
  `gateManifest`, the key the harness reads (`tools/workflows/tier2-review.template.js:896`), in place
  of `legManifest`, which nothing under `tools/` reads. Observed by AC9.
- **S10** — id 8 (item 8, LOW). `limit-hook-writer-split` (`tools/policy/check_policy.py:3018-3044`)
  gains one row in its own `judge` style: `check-review-join.js --hook <the fixture's hook copy>` over a
  case file holding `m.set(f.ref, v)`, wanting exit 1 and a stderr naming `a ref-keyed verdict join`,
  its description naming `check-review-join.js`. The `limit-hook-rules-kept` comment (:2948-2949) and
  the module docstring's sentence on the writer-split case (:122-124) then name both checkers that case
  runs: the verifier fan-out check, `check-verifier-fanout.js`, and the ref-keyed join ban,
  `check-review-join.js`. Observed by AC10.
- **S11** — the catalogue. One class record per `new:` disposition under `memory/gotchas/`, each with
  its Symptom, its Where it bit naming this review by file stem and its id, its fix, and its gate
  sentence, and `memory/gotchas/INDEX.md` regenerated with `python tools/memory-tree/gotchas.py --write`.
  Each record's backticked path tokens are exactly its anchor column below, so the selection is the
  one the table states. Id 5's fix names unit TOOL-dFairHearing-44, unbackticked. The records and the
  regeneration run `tools/memory-tree/gotchas.py` and leave that file unedited. Observed by AC11.

  | Record | Id | Anchors | Gate sentence |
  |---|---|---|---|
  | `unvalidated-arg-reaches-an-agent-shell-line` | 1 | `tools/workflows/tier2-review.template.js`, `tools/workflows/tier2-review.test.sh` | gated by `tools/workflows/tier2-review.test.sh`, its `FH43 AC1` arm |
  | `helper-whose-only-caller-is-its-selftest` | 5 | `tools/memory-tree/gotchas.py` | no machine gate: no leg reads a function's callers |
  | `doc-names-an-argument-the-code-never-reads` | 6 | `tools/workflows/kit.toml` | no machine gate: the predicate over every kit's comments found this one line (Alternatives rejected) |
  | `comment-claims-a-check-the-case-does-not-run` | 8 | `tools/policy/check_policy.py` | no machine gate for the class; S10's row executes this instance |

## 3. Non-goals (OUT)

- No re-review: the diff exit is CONVERGED, and its minors are disposed here and in
  `TOOL-dFairHearing-44`, not folded.
- No edit to `tools/memory-tree/gotchas.py`: id 5's docstrings are `TOOL-dFairHearing-44`'s scope.
- No edit to `tools/gate-legs.json`: the `policy fixtures` guard's missing `.governance/install.json`
  line predates this unit and goes to `TOOL-dFairHearing-45`.
- No change to any class record the review disposed `class:` (ids 2, 3, 4 and 7). Each class's
  left-shift is the arm its item adds: the round trip for `pipe-in-a-code-span-splits-a-table-cell`,
  the pin-key arm for `policy-value-with-no-route`, the parity and the ban for
  `two-answers-to-one-question`, and the preset arm for
  `criterion-asserts-what-its-own-command-cannot-show`.
- No refusal of every key `unattended-build.js` does not know: S3 routes the keys a pin prints and the
  one the skeptic named.
- No new grammar for an already-escaped `\|` in a returned `none` reason. Once the DISPOSITIONS prompt
  stops asking for it, a returned reason carries a pipe as written.
- Not the lexicon offender count, the replay scorer's stated-count reader or the playbook-parity leg
  guard: those are separate adopted units.
- No help page: `help/` covers none of the review harness, the build harness, the opt-in pack, the
  hook's policy lookup or the policy fixtures (its thirteen pages, read at `23e1a54d`).

### Edges

none

## 4. Design

### Why two units

The four new records share one generated file, `memory/gotchas/INDEX.md`, and ids 1, 2 and 7 share
the review harness template, its render and its suite, so those stay in this unit. Id 5's docstrings
write only `tools/memory-tree/gotchas.py`, which is the generator of that index
(`tools/memory-tree/kit.toml:504-507`), and `--dispatch` refuses an index beside its generator on the
paths alone (`tools/unattended/unattended.sh:14599-14620`). So they are `TOOL-dFairHearing-44`, whose
write set is disjoint from this one, which is the case the severity rule admits two batch units.

Disjoint paths do not make the two passes concurrent. That refusal reads every open sibling pass's
paths as well as its own (`tools/unattended/unattended.sh:14567`, :14606), so this pass and unit 44's
cannot be open together, and each is declared only after the other has committed.

### The ref shape (S1)

```js
// TOOL-dFairHearing-43 S1 - `base` and `head` reach the checklist agent's and the resume probe's shell
// lines, so each is refused outside a closed ref shape before any agent spawns, at every round.
const REF_SHAPE = /^[0-9A-Za-z._\/~^][0-9A-Za-z._\/~^-]*$/
if (!isSpec) for (const [field, v] of [['base', base], ['head', head]]) {
  if (!REF_SHAPE.test(String(v)))
    throw new Error('tier2-review: `' + field + '` must be a git revision of letters, digits and . _ / ~ ^ -, ' +
      'not opening with -, because it is pasted into the checklist agent\'s and the resume probe\'s ' +
      'shell commands. Got ' + JSON.stringify(v) + '. Refusing before any agent spawns.')
}
```

It sits after the `base` requirement, so an absent `base` keeps its own message. A pinned sha, `HEAD`,
`HEAD~1` and `origin/main` all match. The set holds no shell metacharacter, space or quote, and the
leading-`-` rule keeps the value from reading as a git option. The probe-resolved `baseSha` and
`headSha` cannot serve the checklist agent, because it spawns before the probe (:1421, :1588).

### One cell encoding (S2)

The harness's returned appendix and the record's appendix have different writers. For the returned
one, `renderCell` folds every line break to a space and escapes every `|` as `\|`, and the replay scorer's
reader splits on an unescaped `|` and unescapes `\|` (`tools/workflows/replay_scorer.py:90`, :291). A
raw `a | b` therefore reads back as `a | b`, and a raw line break as one space. The check refused
exactly those spellings, and admitted the `\|` spelling the prompt asked for, which `renderCell`
escapes a second time and the reader returns as `a \| b`. With the check's pipe arm gone from the
`none` branch and the prompt reworded, the writer's encoding and the reader's decoding are one pair.

The record's appendix is the synthesis agent's own text, copied from the block the APPENDIX paragraph
hands it (:2872-2878), and the scorer reads that text from the record's file
(`tools/workflows/replay_scorer.py:323`). `renderCell` never sees the `(synthesis)` cell the agent
fills, so a raw `|` there would split the row. The escape therefore moves to the paragraph that tells
the agent to write that cell. What this does not check: nothing verifies the agent's copy, as nothing
verifies the rest of it today (:2864-2865).

### Every pin key routed (S3)

The forwarding comment at :1752-1754 already states the rule: the callee refuses at its argument
boundary, once, so the caller forwards unchecked. `walk` takes that route like the other six rather
than a refusal by name, because the harness checks `walk` itself and a pin's whole-design line is one
call's arguments. The arm reads the population from `review_pin.py`'s own output rather than typing
it, so a key a later pin prints fails the suite until it is given a route.

### One sibling-kit resolver (S4 to S6)

The pack's `loadReaders` keeps its shape: it resolves the directory once, inside its `try`, then
requires `agent-cap.js` and `scratch-guard.js` from it, so a refusal is the same deny it is today with
a truer remedy. The ban scans `git ls-files -- 'tools/*.js'`, 24 files at `23e1a54d`, for
`dirname\(__dirname\)\s*,\s*['"\x60]` on lines whose first non-space characters are not `//` or `*`;
it requires a population above 10, fires on a planted line, and stays silent on a planted comment.
What it does not check: a sibling path built over two statements, such as the remedy text at
`tools/hooks/agent-cap.js:969`, which loads nothing, and a path joined from `__dirname` and `'..'`,
which the one tracked instance (`tools/memory-recall/recall-opened.js:135`) uses for the repository
root and not for a kit.

At :403 the constant takes the resolver's answer:

```js
function resolvePolicyHelper() {
  try { return require('path').join(resolveKitDir('policy', 'policy-mirror.js', __dirname), 'policy-mirror.js') } catch { return '' }
}
const POLICY_HELPER = resolvePolicyHelper()
```

The lookup is a named function because the lexicon reads a constant holding an invoked function
expression as a function, and `POLICY_HELPER` would then fail its camel-case cell. `resolveKitDir` is
a function declaration, so it is hoisted above :403. An empty path fails the
`existsSync` test both readers already make (:405, :776), which is today's behaviour with no policy
kit beside the hook. The python resolver suite's policy row (`tools/lib/resolve-python.test.sh:668`)
and the policy fixtures' `policy-mirror.js removed` row (`tools/policy/check_policy.py:3042-3044`) keep
their layouts: each puts the policy kit beside the hooks kit, the resolver's outer probe.

### The preset arm (S7)

The arm reuses the suite's `runReview`, `SPEC`, `DESIGN` and `WD` fixtures and the stubs each already
runs with. The round-2 fold is `SPEC` at round 2 with one subject whose `prevBlob` is 40 hex unequal to
its blob, which is the `THREE` fixture's first subject. Each run asserts a non-zero count of `git -C`
matches, so an empty trace cannot pass.

### The header's ask clause

The header carries neither `closes` nor `advances`. `memory/TEMPLATE-SPEC.md` permits both verbs
under `BACKLOG_MODE` `builds` and requires neither. Ask `TOOL-dFairHearing-19` derives CLOSED from unit
40's CLOSED header `closes TOOL-dFairHearing-19`: the backlog fold decides terminality first, from
every CLOSED spec that closes an ask, and reads no live spec when one exists
(`tools/memory-tree/backlog.py:836-842` and :933-940). The build's `BACKLOG.md` DEFERRED row holds the
ask until `TOOL-dFairHearing-40`, and the ask's accept clause reads the README's `roster:units` pair,
which lists units 1 to 18. The build README's phase rule asks a spec run's units to advance the ask;
this is the build run, which builds the unit it added rather than carrying it, so the carry-forward
term that demands a verb on a DEFERRED unit (`tools/unattended/unattended.sh:5500-5503`) never reads
this spec. With no verb, this unit's state at every status leaves the ask's derivation unread. A
`closes` would add a second closer to a closed ask, and an `advances` would link a live spec to it;
neither moves the fold, and neither answers anything the ask asks.

### Inventory

- `REF_SHAPE`, a constant in `tools/workflows/tier2-review.template.js` and its render.
- `resolvePolicyHelper`, a function in `tools/hooks/agent-cap.js`.
- The suite arm labels `FH43 AC1`, `FH43 AC2`, `FH43 AC3`, `FH43 AC4`, `FH43 AC5`, `FH43 AC6`,
  `FH43 AC7` and `FH43 AC10`, one prefix per arm the Gates section declares, apart from the arm at
  `tools/workflows/spec-audit-optin.test.sh:566`, which keeps its label and changes its needle.
- The four class slugs of S11's table, each the stem of its record and its front-matter `name`.
- The deviation record stem `2026-11-04-build-TOOL-dFairHearing-43-deviation-431`, written beside this
  spec.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`
- `tools/workflows/unattended-build.test.sh`
- `tools/workflows/spec-audit-optin.js`
- `tools/workflows/spec-audit-optin.test.sh`
- `tools/workflows/kit.toml`
- `tools/workflows/README.md`
- `tools/hooks/agent-cap.js`
- `tools/hooks/README.md`
- `tools/lib/resolve-python.test.sh`
- `tools/policy/check_policy.py`
- `memory/gotchas/`
- `memory/builds/dFairHearing/build/`

The two renders change only through the review kit's parity gate in its render mode, `kit.toml`'s
`[[regenerate]]` argv, never by hand. `memory/gotchas/INDEX.md` changes only through
`gotchas.py --write`, which this unit runs and does not edit, so no path above is the generator of
another. Under the build folder, only this unit's acceptance ledger is written.

### Alternatives rejected

- **The probe-resolved shas for the checklist agent (S1).** It spawns before the probe; reordering the
  two moves the probe's reuse of the checklist's resume key and still leaves the probe's own line
  pasting the raw values.
- **Escape `|` and line breaks in `checkDisposition` instead (S2).** A second encoder beside
  `renderCell` is the disagreement this item closes.
- **Refuse `twin`, `unclassed` and `walk` by name (S3).** The audit would then run a pinned policy at
  the default with a refusal where a forward costs one line each, and the callee already checks each.
- **A `require` of agent-cap's resolver from the pack (S4).** The pack needs the resolver to find
  agent-cap.js, so it cannot load the resolver from it.
- **A gate joining kit.toml comments to the harness's `a.<name>` reads (S9).** Run over every
  `tools/*/kit.toml` at `23e1a54d`, a backticked name followed by "argument" names one line, this one;
  a gate over one instance with no second is a copy of the fix.

## 5. Production-readiness checklist

- security — S1 closes a caller field's route into a shell-holding agent's command line, refused
  before any agent at every round; no new write path. S6 changes how the hook finds a sibling it
  reads, and an unfound helper reads as today's absent one.
- perf / scale — one regex test per field per run; one receipt read per hook process for the policy
  helper, the walk `resolveKitDir` already makes for the pack check.
- error / empty / loading states — S1 names the field and the value; S4's deny names the three places
  the resolver looked.
- observability — the pack's deny and the harness's refusal each name their cause on stderr or in the
  thrown message.
- risks — S6 changes the hook on a tree whose receipt homes the policy kit elsewhere: the writer bound
  and the settings-in-force rule then read the landed limit there, where today they fall back. S2
  gives up the refusal that caught a raw `|`, so a synthesis ignoring the appendix sentence writes a
  split row into its record.
- testing — the arms the Gates section declares, each observed RED then GREEN at the close, and the
  scratch probes of the acceptance criteria.
- migration — an adopter's caller passing a `base` or `head` outside the shape is refused; no adopter
  step otherwise.
- user docs — none: no `help/` page covers these surfaces (Non-goals); the two kit READMEs move with S2, S3,
  S4 and S6.

## 6. Acceptance criteria

A stub run is a scratch Node script that evaluates a rendered harness with stubbed `agent`,
`parallel`, `log` and `workflow`, as the review harness suite's `runReview` does, recording every
prompt and the arguments of every `workflow` call. Scratch layouts go under `$TEMP/<short name>`.

- **AC1** — When a stub run of `tools/workflows/tier2-review.js` takes the suite's diff arguments with
  `head` `HEAD;echo PWNED`, it throws a message opening `tier2-review:` and naming `head`, and records no agent;
  with `base` `abc $(echo PWNED)`, a `base` holding a backtick, or a `base` of `-x`, it throws naming
  `base` and records no agent. With `base` `origin/main` and with `head` `HEAD~1`, each at round 1, the
  run completes and its first agent is the checklist agent.
  Red when: a metacharacter value of either field reaches the checklist agent's or the probe's
  command line, as `HEAD;echo PWNED` does at `23e1a54d`.
- **AC2** — When a stub run of `tools/workflows/tier2-review.js` takes `unclassed` `reason` and a
  synthesis disposing id 1 `none` with the reason `a | b`, its `dispositions` is a list, and
  `parse_appendix_rows` in `tools/workflows/replay_scorer.py`, handed `confirmed <n>` and a newline
  before the returned appendix, `<n>` the run's confirmed count, reads id 1's disposition as
  `none — a | b`. With the reason holding a line break between `a` and `b`, it reads `none — a b`. The
  synthesis prompt carries no `a pipe written as`, and its paragraph opening
  `APPENDIX - the report's LAST section` carries `which you write and the harness does not encode`.
  Red when: the check refuses a reason `renderCell` encodes, the prompt asks for a spelling the
  renderer escapes twice, or the agent writing the record's cell is not told to escape it.
- **AC3** — When a stub run of `tools/workflows/unattended-build.js` takes the suite's minimal units
  arguments with `twin` `always`, `unclassed` `reason`, `fixJudge` `instance` and a `walk` object, the
  audit's `workflow` call carries each unchanged, and a run passing none carries none of the four. For
  each key the lines of
  `python tools/workflows/review_pin.py --subject memory/builds/dFairHearing/build/2026-11-04-build-TOOL-dFairHearing-25-replay-verdicts.md --design-record-preset whole-design --twin always --unclassed reason --opt-in '{"whole-design": {"topology": "blast-radius"}}'`
  carry, the same stub run given that line's value carries the key with that value.
  Red when: a pinned key reaches the harness and the audit runs at the callee's default.
- **AC4** — When `node` runs a copy of `tools/workflows/spec-audit-optin.js` in a scratch layout whose
  receipt homes the hooks kit's `agent-cap.js` and `scratch-guard.js` in a directory not named `hooks`,
  over the dated-opt-in payload and README the pack's own suite admits, it exits 0 with an empty
  stderr. With the receipt rows naming files that do not exist and no hooks kit beside the copy, it
  exits 2 naming `agent-cap.js`, `looked in` and the three places looked.
  Red when: the pack finds its readers by a rule other than agent-cap's, so a receipt-homed install is
  denied.
  fixture: the layout under `$TEMP/fh43k`, a `.git` directory, `.governance/install.json`, the copied
  pack and hooks files, made by the probe and removed after it.
- **AC5** — When a scratch probe slices the block between `// >>> resolveKitDir` and
  `// <<< resolveKitDir` out of `tools/workflows/spec-audit-optin.js` and out of
  `tools/hooks/agent-cap.js`, the two slices are byte-identical, and each answers the nine layouts of
  the python resolver suite's JS-port section as `k h refused k p/h h refused h h`, the canonical
  `resolve_kit_dir.py`'s answer.
  Red when: the pack carries no marked block, or its copy answers one layout differently.
- **AC6** — When `git grep -nF "dirname(__dirname), '" -- "tools/*.js"` runs, it prints nothing.
  When a copy of `tools/hooks/agent-cap.js` is required from a scratch layout whose receipt homes a
  stub `policy-mirror.js`, answering 3 from `readPolicy`, in a directory not named `policy`, its
  `readWriterBound` returns `n` 3 and the key `runtime.agents-in-flight`; with no policy kit anywhere it
  returns `n` 5 and a key opening `MAX_VERIFIERS, as no policy kit`.
  Red when: a kit file finds a sibling kit at a hard-coded path, as both lines the grep prints at
  `23e1a54d` do.
  fixture: the layout under `$TEMP/fh43p`, made by the probe and removed after it.
- **AC7** — When stub runs of `tools/workflows/tier2-review.js` take `repo` `C:/x y/z` over `unit-spec`
  at round 1, its round-2 fold with a `prevBlob` unequal to the blob, `design-audit` and `whole-design`,
  every `git -C` match in each run's prompts equals `git -C "C:/x y/z"`, each run holds at least one,
  and the `unit-spec` round-1 run's prompts hold `hash-object <path>` and `diff <blob> -- <path>`. Over
  a scratch copy of the render whose probe hash-object command reads `git -C ${repo}`, the same probe
  names that bare command. `grep -c "FH43 AC7" tools/workflows/tier2-review.test.sh` prints a number
  above 0.
  Red when: the suite asserts the quoting of the diff kind alone, so a bare spec-only site stays green.
- **AC9** — When `git grep -n legManifest -- tools` runs, it prints nothing, and
  `grep -c "gateManifest" tools/workflows/kit.toml` prints a number above 0.
  Red when: the descriptor names an argument key the harness never reads.
- **AC10** — When `python tools/policy/check_policy.py --fixture limit-hook-writer-split` runs, no line
  opening `policy-fixture: limit-hook-writer-split` carries `WRONG:`, and exactly one such line names
  `check-review-join.js` and carries `exit 1` and `a ref-keyed verdict join`;
  `grep -c "check-review-join" tools/policy/check_policy.py` prints a number above 1.
  Red when: a comment credits the case with a check the case does not run, as at `23e1a54d`, where no
  line of the case names `check-review-join.js`, or the row runs and its ban does not fire, which
  prints `WRONG:` on the row's line.
  fixture: the command's exit status is not graded. Measured at `3f2ca384f`, untouched, it exits 1 on
  the line `policy-fixture: guard-trace · WRONG .governance/install.json · not under the policy fixtures guard`,
  which belongs to no case and carries no `WRONG:`.
- **AC11** — When `python tools/memory-tree/gotchas.py --for-paths tools/workflows/tier2-review.template.js`
  runs, it prints a line naming `unvalidated-arg-reaches-an-agent-shell-line`; `--for-paths` over
  `tools/memory-tree/gotchas.py` names `helper-whose-only-caller-is-its-selftest`, over
  `tools/workflows/kit.toml` names `doc-names-an-argument-the-code-never-reads`, and over
  `tools/policy/check_policy.py` names `comment-claims-a-check-the-case-does-not-run`.
  `python tools/memory-tree/gotchas.py --check` exits 0, and
  `grep -cE "unvalidated-arg-reaches-an-agent-shell-line|helper-whose-only-caller-is-its-selftest|doc-names-an-argument-the-code-never-reads|comment-claims-a-check-the-case-does-not-run" memory/gotchas/INDEX.md`
  prints 4.
  Red when: a record is absent, its anchor reaches no path it names, or the index was not regenerated.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `hook destinations self-test` · `verifier fan-out self-test` · `review-join self-test` · `tier2-review self-test` · `unattended-build self-test` · `spec-audit opt-in pack self-test` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `harness arms (fail branches armed or pinned)` · `python resolver (behaviour + inline parity + idiom ban)` · `policy fixtures` · `gotchas selftest` · `memory-hygiene self-test` · `recall floor` · `recall floor arms` · `agent-cap restatement` · `kit version markers` · `lexicon naming predicates` · `testsuite counts (every bar self-test prints one)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · covers AC1 · stub runs whose `head` is `HEAD;echo PWNED` and whose `base` holds `$(`, a backtick or a leading `-`, staged against the harness at `23e1a54d`, where the `head` run spawns the checklist agent with the value in its command · FLOOR_ASSERTIONS in that suite, 629 at `23e1a54d`, raised by the arms added

New arm: tools/workflows/tier2-review.test.sh · covers AC2 · the `FH23 AC23` arm moved to the round trip, a `none` reason holding a raw `|` and one holding a line break each accepted and read back through `parse_appendix_rows`, and the appendix paragraph's escape sentence found in the prompt, staged against `23e1a54d`, which refuses both sets and states no such sentence · the same floor

New arm: tools/workflows/tier2-review.test.sh · covers AC7 · the spaced `repo` over `unit-spec`, its round-2 fold, `design-audit` and `whole-design`, staged by stripping the quotes from the probe's hash-object command (:1594) alone, then from the acquire sentence's (:1823) alone · the same floor

New arm: tools/workflows/unattended-build.test.sh · covers AC3 · every key the pin prints, passed to the harness and found in the audit call's arguments, staged against `23e1a54d`, whose audit call carries no `twin`, `unclassed` or `walk` · FLOOR_ASSERTIONS in that suite, 905 at `23e1a54d`, raised by the arms added

New arm: tools/workflows/spec-audit-optin.test.sh · covers AC4 · a receipt homing the hooks kit outside a sibling `hooks/`, staged against `23e1a54d`, where the pack denies the dated opt-in naming `could not be loaded` · FLOOR_ASSERTIONS in that suite, 123 at `23e1a54d`, raised by the arms added

New arm: tools/workflows/spec-audit-optin.test.sh · covers AC4 · the no-hooks-kit `specAudit` arm at :566 moved from `could not be loaded` to `looked in`, staged against `23e1a54d`, whose deny carries no `looked in` · none, a moved arm adds no assertion

New arm: tools/lib/resolve-python.test.sh · covers AC5 · the JS-port section over the pack's block and the two blocks compared, staged against `23e1a54d`, where the pack carries no marked block · none

New arm: tools/lib/resolve-python.test.sh · covers AC6 · the sibling-kit path ban with its population and its two plants, staged against `23e1a54d`, where it names the hook's :403 and the pack's :24 · none

New arm: tools/policy/check_policy.py · covers AC10 · the ref-keyed join row of `limit-hook-writer-split`, staged against a fixture copy of `check-review-join.js` whose ban matches nothing and exits 0, read on the row's own line, since the case exits 1 either way until the guard line lands · none

AC6's agent-cap half, AC9 and AC11 take no arm: the ban stops the hard-coded path from returning, the
comment changes no behaviour, and the catalogue's own check and selftest grade the records.

The `policy fixtures` leg stays on the leg line because this unit's paths trip its guard, and it reds
on the `.governance/install.json` read until `TOOL-dFairHearing-45` lands that guard line.

## 8. Open questions

- **F1 — Which tree does the sibling-kit ban read, now that its predicate names a second site?**
  Options: (a) every tracked JS file under `tools/`, with the hook's policy lookup at :403 resolved
  through its own `resolveKitDir`; (b) the workflows kit only, the hook's site filed as an ask in this
  build's `BACKLOG.md`; (c) no ban, the parity of S5 alone. (c) guards the copy and not the class, so
  the next hard-coded sibling returns unseen. (b) gates the instance and leaves a second site of the
  same defect live, where a tree whose receipt homes the policy kit elsewhere runs with the
  settings-in-force rule stood down. (a) satisfies every criterion, leaves no follow-up, reuses the
  resolver already in the hook, and widens no surface: it changes where the hook reads a sibling, and
  an unfound one reads as today. Recommendation (a). RESOLVED (agent, 2026-11-04, delegated): (a),
  rung 3, the most feature-rich option no veto discards. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-04 · initial draft, promoting the 8 confirmed minors (5 medium, 3 low) of the closing
  diff review of units 1 to 40 as one batch.
- rev-2 · 2026-11-04 · AC3 · the pin command's `--subject` names a tracked design record, unit 25's
  replay verdicts, in place of an untracked fixture path the spec token check refused; the printed
  keys are unchanged, measured at `01a9b0e02`.
- rev-3 · 2026-11-04 · S8 · AC8 · both moved to `TOOL-dFairHearing-44`, with
  `tools/memory-tree/gotchas.py` out of §4's Files touched, so no path pairs an index with its
  generator; later ids keep their numbers; brief `2026-11-04-prompt-TOOL-dFairHearing-43-2-spec-writer`.
- rev-3 · 2026-11-04 · §1 · §3 · the title, the Goal and the Non-goals say seven findings close here
  and id 5 is split; brief `2026-11-04-prompt-TOOL-dFairHearing-43-2-spec-writer`.
- rev-3 · 2026-11-04 · §4 · "Why one unit" is now "Why two units": the false claim that no split is
  disjoint corrected, and the two passes stated as never open together; brief `2026-11-04-prompt-TOOL-dFairHearing-43-2-spec-writer`.
- rev-3 · 2026-11-04 · S11 · id 5's class record and the `gotchas.py --write` regeneration stay here,
  its fix naming unit 44; brief `2026-11-04-prompt-TOOL-dFairHearing-43-2-spec-writer`.
- rev-3 · 2026-11-04 · S2 · AC2 · §4 · §5 · §7 · the appendix-copy instruction near
  `tools/workflows/tier2-review.template.js:2876` takes the escape of the record's own cell, because
  `renderCell` encodes only the returned table; brief `2026-11-04-prompt-TOOL-dFairHearing-43-2-spec-writer`.
- rev-3 · 2026-11-04 · S4 · AC4 · §4 · §7 · the arm at `tools/workflows/spec-audit-optin.test.sh:566`
  named among the text S4 changes, its needle `looked in`, with its `New arm:` line and the Inventory's
  label sentence; brief `2026-11-04-prompt-TOOL-dFairHearing-43-2-spec-writer`.
- rev-3 · 2026-11-04 · §7 · the no-arm sentence loses AC8 and the docstrings; brief `2026-11-04-prompt-TOOL-dFairHearing-43-2-spec-writer`.
- rev-4 · 2026-11-04 · AC10 · grades the case's own lines in place of the exit status, which is 1 on
  the untouched tree through the guard-trace line, and stays red on an unrun or unfired row; return `2026-11-04-build-TOOL-dFairHearing-43-3-builder-return`.
- rev-4 · 2026-11-04 · §3 · §7 · the `policy fixtures` guard line named as `TOOL-dFairHearing-45`'s,
  the leg's red until then stated, and AC10's arm read on the row's own line; return `2026-11-04-build-TOOL-dFairHearing-43-3-builder-return`.
- rev-4 · 2026-11-04 · §4 · S6 · the `POLICY_HELPER` snippet spelled `resolvePolicyHelper` then the
  constant, with the Inventory naming the function, so the lexicon count does not rise; return `2026-11-04-build-TOOL-dFairHearing-43-3-builder-return`.

## 10. Reuse audit

Every item extends a seam the base tree carries: the harness's argument boundary, the `repo` refusal
(`tools/workflows/tier2-review.template.js:257`) and the diff kind's `base` requirement (:287-296);
`renderCell` (:2445) and the scorer's cell reader; the forwarding block of
`tools/workflows/unattended-build.template.js` (:1752-1759); `resolveKitDir`
(`tools/hooks/agent-cap.js:989-1024`) with its canonical `tools/lib/resolve_kit_dir.py`, and the
python resolver suite's JS-port and ban sections; the `judge` helper of `limit-hook-writer-split`; and
the bug-class catalogue `gotchas.py --write` renders. `python tools/codebase-map/reuse_lookup.py
"find a sibling kit directory through the install receipt"` ranked `resolve_kit_dir` first, fan-in 44
and 104 installs, the canonical S4 copies through its JS port. `python tools/codebase-map/reuse_lookup.py
"refuse a caller argument before an agent spawns a shell command"` ranked the generic `refuse` and
`before` stems and no argument-shape validator, so no existing seam fits a ref grammar, and S1 adds
one constant beside the `repo` refusal. The recall query returned this build's brief, a hook-path
breakage in `TOOL-dRetiredFork-35` and the inline-block carrier `TOOL-dWitnessedBar-27` names, which is
the mechanism S4's copy rides.

Recall terms used: `python tools/memory-recall/query.py "a caller argument pasted into an agent shell command and a sibling kit found at a hard-coded path" --terms "unvalidated base head checklist agent shell line resolveKitDir sibling kit hard-coded receipt twin unclassed forward pipe cell"`
