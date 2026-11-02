# TOOL-dFoldedAudit-12 — the DEGRADED by-hand route ends in the chain record and verdict

**Status:** CLOSED · rev-1 · 2026-11-02 · node d · Tier-2 · base 74274869 · streams tooling · order 140

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dFoldedAudit-12-1-builder-return.md](../build/2026-11-02-build-TOOL-dFoldedAudit-12-1-builder-return.md) | journal | — |
| [2026-11-02-build-TOOL-dFoldedAudit-12-ledger.md](../build/2026-11-02-build-TOOL-dFoldedAudit-12-ledger.md) | journal | — |
| [2026-11-02-build-TOOL-dFoldedAudit-9-1-promotion-notes.md](../build/2026-11-02-build-TOOL-dFoldedAudit-9-1-promotion-notes.md) | research | TOOL-dFoldedAudit-9 TOOL-dFoldedAudit-10 TOOL-dFoldedAudit-11 TOOL-dFoldedAudit-13 TOOL-dFoldedAudit-14 TOOL-dFoldedAudit-15 |
| [2026-11-02-build-TOOL-dFoldedAudit-9-2-spec-stage-returns.md](../build/2026-11-02-build-TOOL-dFoldedAudit-9-2-spec-stage-returns.md) | journal | TOOL-dFoldedAudit-9 TOOL-dFoldedAudit-10 TOOL-dFoldedAudit-11 TOOL-dFoldedAudit-13 TOOL-dFoldedAudit-14 TOOL-dFoldedAudit-15 |
| [2026-11-02-prompt-TOOL-dFoldedAudit-12-build-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-12-build-brief.md) | research | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-12-spec-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-12-spec-brief.md) | research | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-9-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-9-fix-brief.md) | research | TOOL-dFoldedAudit-9 TOOL-dFoldedAudit-10 TOOL-dFoldedAudit-11 TOOL-dFoldedAudit-13 TOOL-dFoldedAudit-14 TOOL-dFoldedAudit-15 |

<!-- /gen:spec-records -->

## 1. Goal

Under a declared `disposal`, a dead or refused disposal's note orders the by-hand `--record-round` and
then `--chain-verdict`, not a dispatch, so a hand disposal cannot build around the chain. Every sentence
that orders the chain record also orders it committed, so it never rides into a unit's pass commit.
This closes items H4 and M10 of the closing review, round 1.

## 2. Scope (IN)

- **S1** — `auditedIds` moves above the DISPOSAL stage, so the stage's DEGRADED return can read it. Its
  value does not change. Observed by AC1.
- **S2** — `renderChainStep(command)` is the one sentence that runs a round's command and commits the
  record it staged. Observed by AC6, AC7 and AC8.
- **S3** — Under `disposalDeclared`, the DEGRADED note's by-hand branch ends with the commit of the
  disposal's folds and specs, the `--record-round` shape through S2, and the `--chain-verdict` route.
  Observed by AC1, AC2 and AC3.
- **S4** — That shape names the `--finding` and `--sibling` row grammars and renders none of the
  refused stage's rows, and the return still carries no `chainRecord` key. Observed by AC4.
- **S5** — With no `disposal`, the note keeps every byte, the resume route included. Observed by AC5.
- **S6** — `nextAction` at the hand-out and the clean round's sentence both order the record through
  S2. Observed by AC6 and AC7.
- **S7** — The render regenerates in the same commit. Observed by AC8.

## 3. Non-goals (OUT)

- The driver. `--record-round` keeps its bytes, and so does its printed line. See "Alternatives
  rejected".
- `--dispatch` refusing what this note no longer orders. `TOOL-dFoldedAudit-9` owns that gate, and this
  note is right with or without it.
- The attended every-unit-terminal return, item M11. It carries `chainRecord` and no `nextAction`.
- The note's `--review` clause, which an attended run cannot follow. Item H4 leaves it, and it predates
  this build's chain.
- A dead disposal's `recordAfter` being false. Under a declared `disposal` the stage runs only where
  `recordAfter` is true, since `disposeFirst` covers zero blockers and a held exit covers the rest.
- A kit or engine version move. `unattended-build@1.13` stands, as it did through
  TOOL-dFoldedAudit-5's edit of this file, and the lander mints kit versions (`tools/push-main.sh:26-31`).
- `tools/unattended/VERBS.template.md`. Its `:284` already says the caller commits the record.

### Edges

- **consumes-from** external — `renderChainRecord`, `renderChainRoute`, `disposalDeclared` and the held-exit note, built by CLOSED units of this build whose frozen specs take no mirror; without them this note has nothing to render

## 4. Design

### The note

The branch at `tools/workflows/unattended-build.template.js:2690` becomes:

```js
(disposalDeclared
  ? ' — then commit the disposal\'s folds and specs, ' +
    renderChainStep(renderChainRecord(subject, auditedIds, [], []) +
      ' --finding <id>/<severity>/<nature>/<spec>[,<spec>]/<unit>/<rev>') +
    'One `--finding` per finding you disposed, and one `--sibling <unit>@rev-<n>` per sibling edit. ' +
    renderChainRoute('dispatch every unit `' + DRIVER + ' --plan ' + slug + ' --paths` lists as READY, ' +
      'one main-loop Workflow call each')
  : ' — and dispatch from `' + DRIVER + ' --plan ' + slug + ' --paths`, the resume route.')
```

The `--finding` placeholder is the grammar `write_chain_round` holds at
`tools/unattended/unattended.sh:13526`, spelled as that refusal spells it.

- **Empty lists, on purpose.** `dispositions` and `siblingEdits` on this return are what a refused
  stage said, so rendering them would print rows for findings nobody disposed. The caller writes its
  own, which is what `--folded <folded>` already asks of the same note.
- **`--blockers` and `--highs` are the review's counts.** `renderChainRecord` reads `au`, and
  `write_chain_round` compares its rows with them.
- **`renderChainRoute` is the route, unchanged.** It keeps "dispatch nothing" under CONTINUE, and its
  STOP clause is the conditional dispatch the owner's chain rule allows. The clean round's words are
  used, because this return carries no roster and no `dispatch` key.
- **The word `chainRecord` stays out of the note.** The FA5 AC13 arms read `hasnt_ "chainRecord"` over
  the whole RESULT of a refused return, and the comment at `:2737` stays true: no command is rendered
  over findings nobody disposed. The note carries a shape with placeholders.

### The hoist

`const auditedIds` at `:2731` sits below the stage, so a read from the return at `:2645` is a
temporal-dead-zone ReferenceError. It moves above the `let stood` line at `:2366`, its comment with it.
Nothing it reads changes after that line: `specRefused` is set at `:1186`, `auditUnits` at `:1458`, and
`subjects` for the last time at `:1646`, and `specPath` is written only at `:1369`.

### The commit order

```js
function renderChainStep(command) {
  return 'run `' + command + '`, then commit the chain record it staged. '
}
```

`write_chain_round` stages and never commits, at `tools/unattended/unattended.sh:13550`. The three
callers:

| Site | Sentence |
|---|---|
| `:2894`, the hand-out | `'RECORD this round: commit the disposal\'s folds and specs, ' + renderChainStep(chainRecord) + renderChainRoute(...)` |
| `:3014`, the clean round | `'Commit the record, then ' + renderChainStep(chainRecord) + renderChainRoute(cleanDispatch) + ' '` |
| `:2690`, the DEGRADED note | above |

`renderChainRoute` opens `Then run`, so each sentence reads in order. The opening words
`RECORD this round: commit the disposal` and `Commit the record, then run` stay, so the arms at
`tools/workflows/unattended-build.test.sh:3250` and `:3272` keep reading. `renderChainStep` sits between
`renderChainRecord` and `renderChainRoute`. The comment at `:2299` gains the commit, and the comment at
`:2737` gains that the note's by-hand shape is no command.

### Files touched (estimate)

`tools/workflows/unattended-build.template.js` · `tools/workflows/unattended-build.js` ·
`tools/workflows/unattended-build.test.sh`

### Rollout

The render comes from `tools/workflows/check-protocol-parity.test.sh` in its `--render` mode, as units
3 and 5 ran it. It reaches a run only under a declared `disposal`, so a blank `SPEC_FOLD_CUTOFF` changes
nothing.

### Inventory

| Minted | Cell | Graded by |
|---|---|---|
| `renderChainStep` | `js.function` | `lexicon.py --suggest` answered OK on 2026-11-02 |

### Alternatives rejected

- **Have `--record-round` print the commit step**, the judged fix's other form. It writes a file
  outside this unit's write set, and a caller reading `nextAction` still commits nothing until the
  verb has run. The sentence orders it ahead of the verdict.
- **Commit inside `renderChainRoute`.** The route opens with the verdict and has one more caller
  shape, and the commit belongs to the step that staged the file.
- **Render the refused stage's rows into the note.** A refused return's list is what reconciliation
  refused, and the rows would read as disposed.
- **A `chainRecord` key on the DEGRADED return.** The comment at `:2737` rules it out, and a caller
  acting on the key would record a round over a dead disposal.
- **A function computing `auditedIds` at the note.** It is a second caller of one join, where a hoist
  keeps one value.

## 5. Production-readiness checklist

- security: no new surface. The note is text for the caller, and `renderChainRecord` already composed
  this string from values row 18 checked. Under `DEGRADED` no row reached it, so `subject`, `slug` and
  the audited ids are the only values in the command, and each passed the args table or the roster.
  The `--finding` placeholders are not a command anyone runs as written, and `write_chain_round`
  refuses them if they are.
- perf / scale: none. One string, built on a path that already returns.
- error / empty / loading states: `auditedIds` empty on a DEGRADED note renders `--audited ""`, which
  the verb refuses by name, the state the clean round throws on and unit 5's builder recorded as loud.
- observability: the note is the record of the route, and `disposal: NOT done` stays in the trace.
- risks: the note grows by about 500 bytes on a path that only runs on a failure. The two helpers keep
  its text from drifting from the hand-out's.
- testing: fixtures per §6 with no gate, and arms on `New arm:` lines in §7.
- migration: none. No record moves, and an undeclared run keeps its note.
- user docs: N/A. `help/` documents neither `--review` nor the spec audit.

## 6. Acceptance criteria

Every case runs `node degraded-fixture.js <case>`, a stub runner the pass writes under the run's
scratch from the AsyncFunction shape of `run_wf`, evaluating `tools/workflows/unattended-build.js` with
`RUN_WF_SCHEMA=strict`. Its args are the suite's `UNITS` plus `disposal: 'by-nature'` unless a case says
otherwise, and its doubles are the FA3 doubles, so the RESULT's quotes are JSON-escaped. `note` below
is the RESULT's `note`.

- **AC1** — When `node degraded-fixture.js held-exit` runs a confirmed BLOCKER at a held `BOUNDED` with a
  dead stage, the run returns, `disposal: NOT done` is in the trace, and `note` holds
  `--record-round tB --subject tB-spec-set-r1 --audited`, `--blockers 1 --highs 0`, `--chain-verdict tB`
  and `--finding <id>/<severity>/<nature>/<spec>[,<spec>]/<unit>/<rev>`.
  Red when: `auditedIds` stays below the stage, so the run throws a ReferenceError.
- **AC2** — When `node degraded-fixture.js refused-return` runs one confirmed HIGH at zero blockers with
  a stage return the reconciliation refuses, `note` holds `--blockers 0 --highs 1` and
  `--chain-verdict tB`, and lacks `the resume route` and `and dispatch from`.
  Red when: the branch still ends in the dispatch, which is the failure H4 names.
- **AC3** — When `held-exit` runs, `commit the disposal's folds and specs` comes before the first
  `--record-round` in `note`, that before `commit the chain record it staged`, and that before
  `--chain-verdict`. `note` also holds `CONTINUE: re-invoke this harness with round: 2`,
  `STOP: dispatch every unit` and `HOLD: run the recipe it prints`.
  Red when: the note names the verbs out of order, or drops a word's route.
- **AC4** — When `refused-return` runs a stage whose return carries a `local` entry at id 7 and a
  sibling edit, `note` lacks `--finding 7/` and `--sibling A-tB-`, and the RESULT holds no `chainRecord`.
  Red when: the note renders a refused stage's rows as disposed, or the key rides this return.
- **AC5** — When `node degraded-fixture.js undeclared` runs one HIGH at zero blockers and a dead stage
  with no `disposal`, `note` holds `--plan tB --paths` and ends `the resume route.`, and it lacks
  `--record-round` and `--chain-verdict`.
  Red when: the branch leaves `disposalDeclared`, so a pre-cutoff run's note moves.
- **AC6** — When `node degraded-fixture.js local-fold` runs a declared local fold, `nextAction` holds
  `RECORD this round: commit the disposal's folds and specs, run `, then that round's `--record-round`,
  then `, then commit the chain record it staged. Then run `, then `--chain-verdict tB`.
  Red when: `nextAction` runs the verdict with the record still staged, which is the failure M10 names.
- **AC7** — When `node degraded-fixture.js clean-round` runs the clean round, `nextAction` holds
  `Commit the record, then run `, `commit the chain record it staged` and `--chain-verdict tB`, in that
  order.
  Red when: the clean sentence keeps its own order, so the fix reaches one site of two.
- **AC8** — When `grep -c 'commit the chain record it staged' tools/workflows/unattended-build.js` runs it
  prints 1, the definition, and `grep -c 'renderChainStep(' tools/workflows/unattended-build.js` prints
  at least 4, that definition and the three callers §4 names.
  Red when: the render did not move, or a site spells the sentence by hand.
  figure: DERIVED from the three sites in §4, a floor because a later caller may join them.

## 7. Gates

`unattended-build self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `policy fixtures` · `workflow script syntax` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `kit version markers`

New arm: tools/workflows/unattended-build.test.sh · covers AC1 AC2 AC3 AC4 · a dead stage and a refused return under `by-nature`, staged by restoring the ` — and dispatch from ` ending under `disposalDeclared` · `FLOOR_ASSERTIONS` by the arm's executed count
New arm: tools/workflows/unattended-build.test.sh · covers AC5 · the same stage with no `disposal`, staged by taking the declared branch unconditionally · `FLOOR_ASSERTIONS` by the arm's executed count
New arm: tools/workflows/unattended-build.test.sh · covers AC6 AC7 AC8 · the hand-out's and the clean round's sentences, staged with `renderChainStep` returning no commit clause · `FLOOR_ASSERTIONS` by the arm's executed count

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, from items H4 and M10 of the closing review round 1, the promotion
  notes' tags and the design's [address] and [chain].

## 10. Reuse audit

`reuse_lookup.py` on "tell the caller what to run when a disposal is degraded and the findings go by
hand" ranked name stems and no seam for a hand-out sentence, so the seam is the file's own:
`renderChainRecord` at `tools/workflows/unattended-build.template.js:2303`, `renderChainRoute` at
`:2316`, and the join `auditedIds` at `:2731`, each of which this unit calls rather than copies.
`tools/memory-tree/gotchas.py --for-paths` selected `degradation-known-but-unreported`, which the note
answers by saying what the caller owes, and `test-oracle-read-from-a-historical-sha`, which is why AC5
pins the note's words and compares with no render at a sha. Unit 5's builder return records
`absence-assertion-over-whole-file-text` on the `chainRecord` key, which is why §4 keeps that word out
of the note.

Every line the review cited was re-read at `f055a11b`: H4's `:2690` and M10's `:2894` and `:3014` held,
and `tools/unattended/VERBS.template.md:284` and `tools/unattended/unattended.sh:13493` say the caller
commits the record. One thing the review did not state: `auditedIds` is declared below the DEGRADED
return, so the judged fix needs S1 first. The recall hits on the review itself and on
TOOL-dFoldedAudit-5's spec found no other route for a dead disposal.

Recall terms used: `python tools/memory-recall/query.py "how does a degraded disposal route the caller back to the chain record and verdict" --terms "DEGRADED disposal nextAction chainRecord record-round chain-verdict resume route by-hand renderChainRoute"`
