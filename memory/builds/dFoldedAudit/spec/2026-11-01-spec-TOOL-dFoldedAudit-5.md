# TOOL-dFoldedAudit-5 — each HIGH records its specs and a verb derives the chain's stop verdict

**Status:** CLOSED · rev-2 · 2026-11-02 · node d · Tier-2 · base 74274869 · streams tooling · order 50 · ratified 2026-11-01

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dFoldedAudit-1-3-design.md](../build/2026-11-01-build-TOOL-dFoldedAudit-1-3-design.md) | research | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8 |
| [2026-11-01-build-TOOL-dFoldedAudit-1-4-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dFoldedAudit-1-4-spec-stage-returns.md) | journal | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8 |
| [2026-11-01-build-TOOL-dFoldedAudit-5-1-cross-read-return.md](../build/2026-11-01-build-TOOL-dFoldedAudit-5-1-cross-read-return.md) | journal | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8 |
| [2026-11-01-build-TOOL-dFoldedAudit-5-2-builder-return.md](../build/2026-11-01-build-TOOL-dFoldedAudit-5-2-builder-return.md) | journal | — |
| [2026-11-02-build-TOOL-dFoldedAudit-5-ledger.md](../build/2026-11-02-build-TOOL-dFoldedAudit-5-ledger.md) | journal | — |
| [2026-11-01-prompt-TOOL-dFoldedAudit-1-brief.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-1-brief.md) | research | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8 |
| [2026-11-01-prompt-TOOL-dFoldedAudit-5-1-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-5-1-spec-writer.md) | journal | — |
| [2026-11-01-prompt-TOOL-dFoldedAudit-5-build-brief.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-5-build-brief.md) | research | — |
| [2026-11-01-prompt-TOOL-dFoldedAudit-5-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-5-fix-brief.md) | research | TOOL-dFoldedAudit-1 |
| [2026-11-01-prompt-TOOL-dFoldedAudit-5-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-5-spec-brief.md) | research | — |
| [2026-11-02-review-TOOL-dFoldedAudit-1-2-3-4-5-6-7-8-closing-diff-round1.md](../reviews/2026-11-02-review-TOOL-dFoldedAudit-1-2-3-4-5-6-7-8-closing-diff-round1.md) | diff-review | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8 |

<!-- /gen:spec-records -->

## 1. Goal

A spec audit's chain ends only when the owner stops it by hand, and "every high sits in the previous
round's own promotions" cannot be derived, because a round's record names no spec a high would
change. This unit gives each BLOCKER and HIGH a spec address, records every round's dispositions
durably in both run modes, and derives one stop verdict in the driver: CONTINUE, STOP or HOLD. The
design's tags are [chain] and [address], and the brief states the outcome as its acceptance line 5.

## 2. Scope (IN)

- **S1** — The address. On a spec subject `tools/workflows/tier2-review.template.js` asks the
  synthesis for a `specs` list on each BLOCKER or HIGH item, and for a machine line under that
  finding in the report. Observed by AC1 and AC3.
- **S2** — The synthesis refusal. A BLOCKER or HIGH item holding a confirmed id with no well-formed
  `specs` is a tally fault, so `blockers` and `highs` return null, the stated absence the build
  harness already refuses. Observed by AC2.
- **S3** — The return. The review's complete return carries `addresses` on a spec subject, one
  `{ids, severity, specs}` per BLOCKER or HIGH item. Observed by AC1.
- **S4** — The address join. Under a declared `disposal`, the harness's `deriveDispositionFault`
  refuses a `dispositions` entry over a confirmed BLOCKER or HIGH id whose `specs` differ from the
  review's address, and any unit token outside the id shape. Observed by AC13.
- **S5** — The hand-out. Under a declared `disposal`, every hand-out past the stage carries
  `chainRecord`, the one command that records this round, and `nextAction` routes on the verdict.
  Observed by AC11 and AC12.
- **S6** — The recording verb, `--record-round`, which appends one round to one build record and
  works with no run-state file. Observed by AC4 and AC5.
- **S7** — The verdict verb, `--chain-verdict`, which derives the verdict from that record and the
  roster alone, in the driver and nowhere else. Observed by AC6, AC7, AC8, AC9, AC10, AC14 and AC15.
- **S8** — The two switches. The verdict reads `read_spec_audit_switch chain-stop` and
  `read_spec_audit_switch chain-ceiling`, and a refused read is a named refusal. Observed by AC15.
- **S9** — The driver's own carriers: `VERBS_SLUG`, `VERB_REQUIRES`, the header's invocation lines
  and the argv parse. Observed by AC4 and AC14.
- **S10** — The render. `tools/workflows/tier2-review.js` and `tools/workflows/unattended-build.js`
  are regenerated from their templates in the same commit, and the `auditIds` comment says it may
  name a folded unit as well as a promoted one. Observed by AC3 and AC16.
- **S11** — The refusal budget. Both verbs refuse through one new site, and the two byte-identical
  check 41 sites become one, so the driver's census does not move. Observed by AC17.

## 3. Non-goals (OUT)

- A closing diff review. The synthesis prompt, schema and return of the diff kind stay byte for byte,
  and every change here branches on the file's existing `isSpec` or on a declared `disposal`.
- The `dispositions` array, its shape and its reconciliation rows 1 to 10, which
  `TOOL-dFoldedAudit-3` owns, and `siblingEdits`, which `TOOL-dFoldedAudit-4` owns.
- `--review`'s row and check 2, which `TOOL-dFoldedAudit-2` owns. The verdict reads no `--review` row,
  because an attended run has none.
- A cutoff of its own. A run whose caller passes no `disposal` keeps today's hand-out, which is
  `TOOL-dFoldedAudit-3`'s absent state and how [cutoff] reaches this unit.
- A second copy of the verdict in JavaScript. The harness renders a command and never reads a set.
- Grading `specs-audited` by the chain. The units an `own-work` stop leaves unaudited close under a
  recorded `--override specs-audited` at `--close`, and no line of that term changes.
- A precision read. Precision bounds nothing here, and `TOOL-dFoldedAudit-1` takes the sentence out of
  M4.
- `tools/roles/agents/gov-synthesizer.agent.md`. The role says to return the shape the harness names,
  and its `returns` line stays true, so no role text moves.
- A kit version bump. A branch owes none, because the lander mints each version at the landing
  (`tools/push-main.sh:26-31`).
- `tools/loop/`, which dDeclaredLoop builds.

### Edges

- **consumes-from** `TOOL-dFoldedAudit-7` — `read_spec_audit_switch chain-stop` and `read_spec_audit_switch chain-ceiling`; without them the verdict has no stop mode and no ceiling
- **consumes-from** `TOOL-dFoldedAudit-3` — `dispositions` on the hand-out, the `disposal` arg, `deriveDispositionFault` and `nextAction`, which this unit routes on the verdict; without them a round has nothing to record
- **consumes-from** `TOOL-dFoldedAudit-4` — `siblingEdits` on the hand-out, each entry of which enters that round's folded set; without it a sibling edit never reaches the set
- **hands-off** `TOOL-dFoldedAudit-1` — the two verbs' entries in the verbs carrier, M4's naming of them, and the review kit README's return fields for the new keys

## 4. Design

### The verdict

For a chain, round N holds three sets, each read from the record:

| Set | Rows |
|---|---|
| H(N) | the distinct finding ids at BLOCKER or HIGH, each with its `specs` |
| P(N) | the `unit` of every `new-mechanism` row, whatever its severity |
| F(N) | the `unit` of every `local` row at BLOCKER or HIGH, and of every `sibling` row |

A spec folded only for a MEDIUM or LOW is not in F(N), because M4 already counts a review's own fold
as reviewed. U is the roster less the terminal specs, less every id on an `audited` row, less P(N).
§8 F1 is why P(N) leaves U. The steps run in this order after round N's disposal, N being the last
round the record holds, 0 when it holds none:

| # | Test | Verdict | Reason | Audit set |
|---|---|---|---|---|
| 1 | U is non-empty | CONTINUE | `unreviewed` | U, P(N) and F(N) |
| 2 | H(N) and P(N) are empty | STOP | `clean` | none |
| 3 | stop mode `own-work`, N >= 2, H(N) non-empty, every high's `specs` inside P(N-1) and F(N-1) | STOP | `own-work` | none |
| 4 | N >= the chain ceiling | HOLD | `ceiling` | none |
| 5 | otherwise | CONTINUE | `open` | P(N) and F(N) |

Round 0 reaches step 1 with U the whole roster, so round 1 is the whole set. Under `clean-only` step
3 is skipped, which is R1 alone.

Three consequences stand as the design states them. A HIGH naming one older spec keeps the chain
alive, because one address outside the prior round's work fails step 3. Most chains therefore end
at round 2. An empty H(N) can never read as R5, because step 3 requires a population, and step 2
answers a clean round first. That is the `fixture-passes-by-finding-nothing` class, so AC9 carries
rows in both of its populations.

At an `own-work` stop the round's own disposal has already run. Its local highs folded, and P(N) is
built from its specs unaudited, so the verdict line names those units for the override.

### The output

One line on stdout, exit 0 for each of the three verdicts:

```
unattended: chain <slug> · round <N> · <CONTINUE|STOP|HOLD> · reason <reason>[ · audit <ids>][ · override specs-audited <ids>]
```

`audit` appears on a CONTINUE, and its ids are what the caller passes as `auditIds`. `override
specs-audited` appears on an `own-work` stop with a non-empty P(N). The list is sorted, so the line
is byte-stable.

On a HOLD a second line prints the recipe, because the main loop owns the keepalive and the verb
cannot reap it. The route is a `--park` row, then `--handoff --code owner-decision`. The design's
word is `--hold`, and `--hold` refuses that code by name (`tools/unattended/unattended.sh:6879`),
because `--handoff` is its only producer and routes through the same hold with the condition fixed
at `owner`. `tools/unattended/STOPS.template.md:694` sends a kind its table does not list to a
hand-off under `owner-decision`, and `TOOL-dFoldedAudit-1` §3 names that code for this hold. The other
candidate, `host-owner-action`, names a host's state and not a decision. An attended run has
neither verb, so its main loop puts the same question to the owner. HOLD stays the answer until the
owner raises the ceiling or rules, because a re-read of the same record derives the same verdict.

### The record

One file per build, found by `git ls-files` under the build's `build/` folder with the tail
`-chain-rounds.md`, its name `<date>-build-<id>-chain-rounds.md`, the first round's date and first
`--audited` id. That is check 5's recording grammar with a unit tail, and an id a spec defines, so
check 21 reads the binding. Two such files is a refusal.

```
# <slug> — the spec-audit chain's rounds

**Serves:** journal <id>

Appended by `--record-round` and read by `--chain-verdict`. Never edited by hand.

round 1 · subject dFix-spec-set-r1 · audited FIX-dFix-1 FIX-dFix-2
round 1 · finding 7 · HIGH · local · specs FIX-dFix-1 FIX-dFix-2 · unit FIX-dFix-1 · rev 2
round 1 · finding 7 · HIGH · local · specs FIX-dFix-1 FIX-dFix-2 · unit FIX-dFix-2 · rev 3
round 1 · finding 9 · LOW · new-mechanism · specs FIX-dFix-1 · unit FIX-dFix-9 · rev 1
round 1 · sibling · unit FIX-dFix-3 · rev 2
```

The chain round is the row's ordinal, derived by the verb as the last round plus one, and never the
harness's `round`. Under `REVIEW_ROUNDS` above 1 one generation spends several invocation rounds, so
that number would burn the ceiling faster than generations pass. `subject` is the generation key
(`tools/workflows/unattended-build.template.js:355`), and it is what refuses a replay. A build's
later run continues the same file, so its rounds count against the same ceiling.

`audited` is the harness's join of its audit units to the subjects the callee read, the join the
clean-round record already makes (`tools/workflows/unattended-build.template.js:2536-2541`). The
verdict reads this row and never a review record, because [address] says it reads only the record
and the roster. A clean round writes no report, and its row still names what it audited.

`sibling` rows sit beside the `finding` rows because `siblingEdits` is `{unit, rev}`, with no finding
id and no severity (`TOOL-dFoldedAudit-4` §4 "The sibling edit").

### The two verbs

```
unattended.sh --record-round <slug> --subject <s> --audited "<ids>" --blockers <b> --highs <h> [--finding <row>]... [--sibling <unit>@rev-<n>]...
unattended.sh --chain-verdict <slug>
```

`--finding` takes `<id>/<severity>/<nature>/<spec>[,<spec>]/<unit>/<rev>`, every id in the
`[A-Z]+-[A-Za-z0-9]+-[0-9]+` grammar `_ids_of` uses, `<nature>` either `local` or `new-mechanism`.
`--sibling` takes the `<id>@rev-<N>` spelling the binding grammar uses. A row is one shell word, so
the harness renders it with no quoting beyond the shape it has already checked. `VERB_REQUIRES`
gains `--record-round --subject --audited --blockers --highs`, each read through `check_verb_flag`.

`write_chain_round` names no run-state file. It calls `refuse_if_terminal`, which passes where no
record exists (`tools/unattended/unattended.sh:12876`'s comment), so both modes reach it. It writes
in append mode and stages the file with `stage_runmd` (`tools/unattended/unattended.sh:4317`). The
caller commits it beside the disposal's folds, which stay the caller's to commit
(`tools/workflows/unattended-build.template.js:130`).

Its refusals run before any byte is written, and every one goes through `check_chain_fault`, the
budget section's one site:

| Refused | Why |
|---|---|
| a `--subject`, `--finding`, `--sibling` or `--audited` token outside its grammar, the subject's being `[A-Za-z0-9-]+` | a separator or a newline would forge a row, and a row nothing can parse is prose in a record the verdict reads |
| a `--subject` an earlier round of the record already carries | a replay would count one generation twice |
| fewer distinct BLOCKER ids than `--blockers`, or fewer HIGH ids than `--highs` | [chain]'s "every confirmed HIGH was disposed somewhere" |

The third row is why the verb takes the two counts. [chain] refuses a round with H(N) non-empty and
P(N) and F(N) both empty, and read from rows alone that test could not fail, because a row at HIGH
always names a nature and a unit. The counts are the review's, so a round whose rows dropped a HIGH
has a population to disagree with. A finding the disposal adjudicated from UNVERIFIED may add a row
above the count, so the test is "fewer", never "differs".

`print_chain_verdict` reads the roster as `{ spec_ids; roster_ids; }`
(`tools/unattended/unattended.sh:4762`, `:4600`), so a promoted unit counts once its spec is
tracked, and takes each status from `load_spec_facts` (`:4720`). CLOSED and WONTDO are terminal: a
frozen spec cannot take a fold, and a retired one is never audited, so either would hold U non-empty
for ever.

`derive_chain_verdict` is one awk over the record, handed the roster, the stop mode and the ceiling,
so the sets are computed in one place. Its refusals go through the same site:

| Refused | Why |
|---|---|
| a roster that yields no id | a verdict over nothing is the vacuous-selector shape |
| two `-chain-rounds.md` files | the rounds would be split across two readers |
| a body row outside the grammar | the record is append-only, so a row a reader cannot parse is hand-edited |
| a `read_spec_audit_switch` read that returns status 1 | the refusal is the reader's, printed through |

A record no verb has written is N = 0 and is not a refusal.

### The refusal budget

`check-arms` holds the driver's census at 323 against a ceiling of 323
(`.memory-tree.conf:653`), and `TOOL-dFoldedAudit-2` ends at 323. The census counts sites, it reds
past the ceiling, and the way up is the owner's retirement review
(`tools/memory-tree/README.md:545`), so a run may not raise it. This unit therefore adds one site
and takes one away, as `TOOL-dFoldedAudit-2` does:

```bash
check_chain_fault() { # why -> 0 when empty, else check 118 and 1
  [ -z "$1" ] && return 0
  fail 118 "the spec-audit chain record refuses this: $1"
  return 1
}
```

118 is the next free number. `check_verb_flag` is the shape, and a helper naming a literal check
number stays visible to `check-arms`. Each reason in the two tables is a value of `$1`, so one arm
quotes the signature and each criterion below observes a reason.

The site it takes away is check 41's. `tools/unattended/unattended.sh:3226` and `:3232` are the same
line, byte for byte, one under the bypass-flag `case` and one under the line-end test. One `if`
joining the two conditions holds the `fail` once. No refusal leaves, because both conditions still
refuse in the same order with the same text, and the arms at `tools/unattended/unattended.test.sh:2233`
and `:2239` read it unchanged. That makes it a merge and not a retirement, so no review row is owed.

### The review side

The synthesis item schema at `tools/workflows/tier2-review.template.js:1927-1934` gains an optional
`specs: { type: 'array', items: { type: 'string' } }`. Optional, because the object is shared with
the diff kind and `required` stays `['severity', 'ids']`. The prompt's sentence is spec-kind only, at
`:1891`, and it orders both the field and one line directly under each BLOCKER or HIGH item:

```
**Specs:** <unit id> <unit id>
```

The tally at `:1953-1987` gains one clause under `isSpec`: an item at BLOCKER or HIGH holding a
confirmed id, whose `specs` is not a non-empty array of id-shaped strings, sets `tallyFault`. That
reuses the path a misplaced id takes, so `blockers` and `highs` go null, the note reads `UNVERIFIED`
at `:2060`, and the harness throws at `tools/workflows/unattended-build.template.js:1770`. A review
cannot check an id against the roster, because it holds only the subjects and a high may name an
older spec, so the shape is all it tests. The harness's rule 10 tests the roster.

The return at `:2017` gains `...(isSpec ? { addresses } : {})`, built only where the tally accepted
the items, `[]` when no such item stands.

### The harness side

`deriveDispositionFault` gains two rows after `TOOL-dFoldedAudit-4`'s under a declared `disposal`:

| # | Refused | Why |
|---|---|---|
| 17 | a confirmed BLOCKER or HIGH id whose entry's `specs` differ as a set from the review's `addresses`, or `addresses` not an array while `au.blockers + au.highs` is above 0 | R5 reads the address, so an agent retyping it could stop a chain by narrowing it |
| 18 | a `unit`, a `specs` member or a sibling `unit` outside the id grammar | these strings reach a shell through `chainRecord`, so the shape is the write boundary |

An UNVERIFIED finding adjudicated to HIGH has no address in the review, so row 17 reads confirmed ids
only.

`renderChainRecord(subject, audited, dispositions, siblingEdits)` returns the command string. `audited`
is the units whose `specPath` is among `subjects`. The string carries `au.blockers` and `au.highs`.
`siblingEdits` reads as `[]` under `promote-all`, because `TOOL-dFoldedAudit-4`'s stage returns the
list under `by-nature` alone.
The harness reads no set and spells neither stop value, which AC16 greps.

`nextAction` branches on a declared `disposal` and `specAudit`, at
`tools/workflows/unattended-build.template.js:2454`:

```
RECORD this round: commit the disposal's folds and specs, then run `<chainRecord>`. Then run
`<DRIVER> --chain-verdict <slug>` and take what it prints. CONTINUE: re-invoke this harness with
round: <n+1>, auditIds: the ids it names, no subjectRound and no `subjects`, and dispatch nothing.
STOP: dispatch the roster below, one main-loop Workflow call per unit; any units its line names after
`override specs-audited` close under that recorded override. HOLD: run the recipe it prints; an
attended run asks the owner.
```

Both verbs answer with no run-state file, so the sentence is the same in both modes, and GROUND's
attended clause about recording verbs does not reach them. The clean-round hand-out at `:2579` gains
the same two commands ahead of its dispatch clause, after it orders the spec-audit record written.
With no declared `disposal`, `chainRecord` is absent and `nextAction` is today's, byte for byte.

Today's sentence dispatches every unit that is not promoted while the audit runs on. The new one
dispatches nothing until STOP, because a folded spec is now audited again, and dispatching it would
build a spec that round may still move. The re-invocation's roster holds every unit, so nothing is
lost.

### Inventory

| Minted | Cell | Graded by |
|---|---|---|
| `write_chain_round`, `derive_chain_verdict`, `print_chain_verdict`, `check_chain_fault` | `sh.function` | `lexicon.py --suggest` answered OK on 2026-11-01 |
| `renderChainRecord` | `js.function` | `lexicon.py --suggest` answered OK on 2026-11-01 |
| `--record-round`, `--chain-verdict` | driver verbs | `VERBS_SLUG`, spelled as `--record-piece` and `--authorization` are |
| `--audited`, `--finding`, `--sibling` | driver flags | the argv parse at `tools/unattended/unattended.sh:14432` |
| `chainRecord`, `addresses` | return keys | the suites |
| `specs` | synthesis schema key | [address] |
| `**Specs:**` | report line | none: the disposal reads it, and no gate does |
| check 118 | driver check number | `harness arms (fail branches armed or pinned)` |

`--record-round` follows `--record-piece` and `--record-set`, the two verbs that append a row to a
record. `--chain-verdict` is a noun, as the read-only `--authorization`, `--liveness` and `--status`
are. The functions take `write_`, `derive_` and `print_` from the lexicon, as `write_task_register`
and `print_liveness` do, because a new `verb_` leading token is outside the declared table.

`--blockers`, `--highs` and `--subject` reuse the parse's existing variables.

### Rollout

Dark until a caller passes `disposal`, which `TOOL-dFoldedAudit-3` makes the only door. `disposal`'s
absent state keeps every existing run on today's route.

### Files touched (estimate)

`tools/workflows/tier2-review.template.js` · `tools/workflows/tier2-review.js` ·
`tools/workflows/tier2-review.test.sh` · `tools/workflows/unattended-build.template.js` ·
`tools/workflows/unattended-build.js` · `tools/workflows/unattended-build.test.sh` ·
`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh`

The suite doubles move with the contract. `buildSynth` at `tools/workflows/tier2-review.test.sh:378`
and `buildSynthOwn` at `:1776` gain `specs`, because a spec-kind arm using them would otherwise take
the tally fault. The review double behind `TOOL-dFoldedAudit-3`'s and `TOOL-dFoldedAudit-4`'s declared
arms gains `addresses`, because row 17 reads it on any round carrying a BLOCKER or HIGH.

### Alternatives rejected

- **A verdict from `--review` rows and `--rescope` rows.** An attended run writes neither, a row names
  no spec, and the rescope reason is free prose (the scout's Q4).
- **Testing R5 against the `**Serves:**` line.** From round 2 the audit reads only the promotions, so
  the test is true by construction (the scout's Q4). It would have stopped dMindYourWords at round 2
  whatever that round found.
- **`--dispositions <file>` carrying JSON.** It needs a Python spawn in the driver and a scratch file
  from the main loop, for rows the harness can already render as one command.
- **The verdict in JavaScript.** [address] forbids it, and this runtime cannot read the roster.
- **A `chain` row kind in `RUN.md`.** An attended run has no such file.
- **A fixed-name file in the build root.** Check 4 admits `README.md`, `RUN.md` and recording-named
  files there, so a fixed name owes a hygiene change, and a `build/` record owes none.
- **`--hold --code host-owner-action`.** See "The output".
- **One `fail` site per refusal.** Eight sites past a ceiling only the owner's review moves.
- **A HOLD for every unreadable state.** It needs no site for the verdict, but `--record-round` still
  needs one, and a record nothing can parse is a fault to name, not a question for the owner.
- **A row for each folded id in `dispositions` for a sibling edit.** `TOOL-dFoldedAudit-4` rejected it
  for want of an id and a severity.

## 5. Production-readiness checklist

- security: a new write path, appending to a tracked record, and a shell string composed from an
  agent's return. Row 18 is the shape check before composition, and `write_chain_round` validates
  again at the write boundary, because the verb is callable by hand. Every token is an id, an
  integer or a closed word, so no value carries a space, a quote or a separator.
- perf / scale: `--chain-verdict` is one `git ls-files`, one spec-facts read and one awk, plus the
  policy reads `TOOL-dFoldedAudit-7` prices. It runs once per round.
- error / empty / loading states: no record reads N = 0, and an empty roster refuses. A round with no
  finding row is a legal `audited` row. A dead disposal returns DEGRADED with no `chainRecord`, so
  nothing is recorded over findings nobody disposed.
- observability: the verdict line names the reason and the sets it acts on. The record is a tracked
  file a reader can walk by hand, and the per-spec records region lists it for the one id it binds.
- risks:
  - The address is a judgment. A synthesis that names too few specs can stop a chain early, and row
    17 only holds the disposal to it. The closing diff review reads what shipped.
  - The `audited` row is the harness's claim. `specs-audited` still joins the real `spec-audit`
    records at `--close`, so a false row cannot close a unit.
  - A build's later run continues the same record, so a spec run's rounds count against a build
    run's ceiling. HOLD is then the owner's turn, which is the failure the safe way round.
  - `unattended kit gate` may red until `TOOL-dFoldedAudit-1` writes the verbs' entries. That is owed
    at the close, where it runs.
- testing: fixtures per §6, no gate, with the arms on `New arm:` lines in §7. The refusals share one
  site, so `harness arms (fail branches armed or pinned)` reads one signature, and each reason is
  observed by a criterion rather than by that leg.
- migration: additive. No landed record moves, and a build with no chain has no record.
- user docs: N/A here. `help/` documents neither `--review` nor the spec audit (`TOOL-dFoldedAudit-1`
  §3), and the verbs' prose is that unit's.

## 6. Acceptance criteria

The driver criteria run in fixture R: `TOOL-dFoldedAudit-7`'s fixture K, a scratch git repository
under `%TEMP%` with a short name, plus a build `dFix` whose README's roster region names
`FIX-dFix-1` to `FIX-dFix-7`, a tracked OPEN spec for each, and no `RUN.md`. Each criterion writes
its rounds with `--record-round`, spelled below as rows, so it exercises the write and the read. The
JavaScript criteria run a stub runner the pass writes under the run's scratch, in the AsyncFunction
shape `check-workflow-syntax.js` documents: `node address-fixture.js <case>` evaluates
`tools/workflows/tier2-review.js`, and `node chain-fixture.js <case>` evaluates
`tools/workflows/unattended-build.js`.

- **AC1** — When `node address-fixture.js specs-carried` runs a spec audit whose synthesis double
  returns one HIGH item with `specs: ['TOOL-x-1']`, the return's `addresses` holds that item's ids,
  severity and specs, and the synthesis prompt carries `**Specs:**`.
  Red when: the return omits `addresses`, or the prompt never asks for the line.
- **AC2** — When `node address-fixture.js empty-address` runs that item with `specs: []`, with the key
  absent, and with `specs: ['not an id']`, each return has `blockers: null` and `highs: null` and its
  note opens `UNVERIFIED`. A MEDIUM item with no `specs` returns integer counts.
  Red when: a HIGH with no address counts, or the rule reaches a minor.
- **AC3** — When `node address-fixture.js diff-kind` runs a diff review whose HIGH item carries no
  `specs`, the counts are integers, the prompt carries no `**Specs:**`, and the return has no
  `addresses` key; and `grep -c 'Specs:' tools/workflows/tier2-review.js` prints at least 1.
  Red when: the rule leaves its `isSpec` branch, or the render did not move.
  fixture: the diff arm's prompt is compared with the same case run against the BASE render.
- **AC4** — When `bash tools/unattended/unattended.sh --record-round dFix --subject dFix-spec-set-r1 --audited "FIX-dFix-1 FIX-dFix-2" --blockers 0 --highs 1 --finding 7/HIGH/local/FIX-dFix-1/FIX-dFix-1/2`
  runs in fixture R with no `RUN.md`, it exits 0, `git ls-files` lists one file ending
  `-chain-rounds.md` whose second non-blank line binds `journal FIX-dFix-1`, and the file holds a
  `round 1 · finding 7` row. A second round's call appends `round 2` rows and adds no file.
  Red when: the verb calls `check_run_state`, or takes its round from an argument.
- **AC5** — When `--record-round` runs with a `--finding` of five fields, with an `--audited` token
  that is no id, with a `--subject` the record already carries, and with `--highs 2` beside one HIGH
  id, each exits 1 printing `UNATTENDED check 118 FAILED` and leaves the record's bytes unchanged.
  With `--highs 1` and no `--finding` it refuses as the last case does.
  Red when: the third case records a replay, or a round reconciles with a confirmed HIGH disposed
  nowhere.
- **AC6** — When the record holds round 1 auditing `FIX-dFix-1` to `FIX-dFix-5`, a HIGH `local` into
  `FIX-dFix-2` and a HIGH `new-mechanism` to `FIX-dFix-6`, and round 2 auditing `FIX-dFix-2` and
  `FIX-dFix-6`, a HIGH with `specs` on both, folded into both, and a second HIGH on `FIX-dFix-6`
  `new-mechanism` to `FIX-dFix-7`, then `bash tools/unattended/unattended.sh --chain-verdict dFix`
  prints `STOP · reason own-work · override specs-audited FIX-dFix-7` and exits 0.
  Red when: step 1 counts P(N), and the line reads `CONTINUE · reason unreviewed`.
- **AC7** — When AC6's round 2 instead carries one more HIGH whose `specs` add `FIX-dFix-1`, folded
  there, `--chain-verdict` prints `CONTINUE · reason open · audit` followed by `FIX-dFix-1`,
  `FIX-dFix-2`, `FIX-dFix-6` and `FIX-dFix-7`.
  Red when: step 3 tests "some high" rather than "every high".
- **AC8** — When a record's round 1 audits `FIX-dFix-1` to `FIX-dFix-3`, and each of four rounds
  carries one HIGH on `FIX-dFix-1` promoted `new-mechanism` to the next unit, each later round auditing
  the unit before, with no key set, `--chain-verdict` prints `HOLD · reason ceiling` and a second line
  carrying `--handoff` and `--code owner-decision`, and exits 0. After three such rounds it prints
  CONTINUE.
  Red when: step 1 counts P(N), so a promoting round can never reach the ceiling.
  figure: DERIVED, the 4 read from `review.spec-audit.chain-ceiling`'s default.
- **AC9** — When round 1 audits all seven clean and round 2 carries a MEDIUM `new-mechanism` row and
  no HIGH, `--chain-verdict` prints `CONTINUE · reason open · audit` and that unit; when round 2
  carries a MEDIUM `local` row and no HIGH, it prints `STOP · reason clean`. Neither prints `own-work`.
  Red when: step 3 omits "H(N) non-empty", so an empty set of highs reads as a subset of anything.
- **AC10** — When round 1 audits all seven and folds a MEDIUM into `FIX-dFix-3`, and round 2's one
  HIGH names `FIX-dFix-3`, `--chain-verdict` prints `CONTINUE`; when round 1 instead carries
  `--sibling FIX-dFix-3@rev-2`, the same round 2 prints `STOP · reason own-work`.
  Red when: F(N) admits a minor's fold, or leaves out a sibling edit.
- **AC11** — When `node chain-fixture.js declared` runs `disposal: 'by-nature'` over AC1's return and
  one `local` entry, the RESULT's `chainRecord` carries `--record-round`, the subject, the audited
  ids, `--blockers 0 --highs 1` and the `--finding` row, and `nextAction` carries `--chain-verdict`
  and no `dispatch the roster below for every unit that is not one of them`. A run with
  `siblingEdits: [{unit: 'A-tB-2', rev: 3}]` carries `--sibling A-tB-2@rev-3`.
  Red when: the hand-out omits the command, or dispatches before the verdict.
- **AC12** — When `node chain-fixture.js undeclared` runs with no `disposal` key, the RESULT has no
  `chainRecord`, and its `nextAction` equals the BASE render's for the same args, a promoted case and
  a no-promotion case each.
  Red when: an in-flight run's route moves.
- **AC13** — When `node chain-fixture.js narrowed` runs a disposal whose entry for confirmed HIGH 7
  drops one spec of the review's address, and again with a promoted `unit` and `promotedIds` of
  `A-tB-9;x`, each trace holds `disposal: NOT done` and the RESULT carries `"roster":[]` and no
  `chainRecord`.
  Red when: an agent's retyped address reaches the record, or an unchecked string reaches the command.
- **AC14** — When `--chain-verdict` runs in fixture R with no record it prints `round 0 · CONTINUE · reason unreviewed`
  and all seven ids. With `FIX-dFix-7` at WONTDO and the other six audited and clean, it prints
  `STOP · reason clean`. With the roster region and the specs emptied it exits 1 printing
  `UNATTENDED check 118 FAILED`. With two `-chain-rounds.md` files it exits 1 the same way.
  Red when: an empty roster reads CONTINUE over nothing, or a retired spec holds the chain open.
- **AC15** — When fixture R commits `.governance/policy.toml` setting `chain-stop = "clean-only"`
  under `[review.spec-audit]`, AC6's record prints `CONTINUE` instead of `STOP`. Setting
  `chain-ceiling = 2`, a record whose round 1 audits `FIX-dFix-1` to `FIX-dFix-5` with a HIGH on
  `FIX-dFix-1` promoted to `FIX-dFix-6`, and whose round 2 audits that unit with a HIGH on `FIX-dFix-1`
  promoted to `FIX-dFix-7`, prints `HOLD`. Setting `chain-stop = "x"` exits 1 printing the reader's
  `policy: refused` line.
  Red when: either value is a constant in the verdict, or a refused read falls through to a default.
- **AC16** — When `grep -c 'own-work\|clean-only' tools/workflows/unattended-build.js` runs it prints
  0, and `grep -c 'read_spec_audit_switch chain-' tools/unattended/unattended.sh` prints 2.
  Red when: a second copy of the verdict lands in the harness.
- **AC17** — When `grep -c 'fail 118' tools/unattended/unattended.sh` runs it prints 1, and
  `grep -c 'fail 41 "a waiver reason may not spell' tools/unattended/unattended.sh` prints 1. A
  `--preflight --waive` reason carrying the bypass flag, and one carrying a newline, each still print
  `a waiver reason may not spell`.
  Red when: a verb adds its own `fail`, which takes the census past `.memory-tree.conf`'s ceiling, or
  the merge loses either condition.

## 7. Gates

`unattended kit gate` · `unattended-build self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `policy fixtures` · `workflow script syntax` · `harness arms (fail branches armed or pinned)` · `review-protocol parity (kit vs dogfood)` · `kit/dogfood doc parity` · `kit version markers` · `template size <=48KiB` · `policy check` · `memory hygiene` · `build README slot contract` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · covers AC1 AC2 AC3 · the spec-kind address cases and the diff-kind control, the failing case staged by dropping the `isSpec` clause from the tally · none
New arm: tools/unattended/unattended.test.sh · covers AC4 AC5 · the record written with no `RUN.md`, and each refusal, the failing case staged by a replayed subject the check does not read · none
New arm: tools/unattended/unattended.test.sh · covers AC6 AC7 AC9 AC10 · the verdict's populated rounds, the failing case staged by step 3 testing "some high", which turns AC7 into a stop · none
New arm: tools/unattended/unattended.test.sh · covers AC8 AC14 · the ceiling and the roster, the failing case staged by step 1 counting P(N), which turns AC8's HOLD into CONTINUE · none
New arm: tools/unattended/unattended.test.sh · covers AC15 · the two switches read through a committed policy file, the failing case staged by the kit constant read in place of the switch · none
New arm: tools/unattended/unattended.test.sh · covers AC17 · the census probe over the driver's own text, the failing case staged by a second `fail 118` · none
New arm: tools/workflows/unattended-build.test.sh · covers AC11 AC12 AC13 AC16 · the declared and undeclared hand-outs and rows 17 and 18, the failing case staged by row 17 returning no reason, which lets the narrowed address through · none

## 8. Open questions

- **F1 — Does step 1's U leave out this round's own promotions?** The design orders UNREVIEWED
  first, over "some roster spec is named by no `spec-audit` record". A unit round N just promoted
  is named by none, so a literal step 1 answers CONTINUE before step 3 or step 4 is read. That contradicts two owner
  rulings in the build README: at an R5 stop "a HIGH needing a new mechanism is promoted once more
  and built from its spec", and the ceiling "holds the run for the owner when neither stop has fired".
  A chain that promotes every round is the only chain that runs away, and a literal step 1 never
  holds it. The design says it may not be re-opened, and it does not mark this DERIVE, so it is
  written here rather than decided.
  - (a) Keep the order and take U as written. R5 fires only on a round that promotes nothing, and the
    ceiling never fires on a promoting chain. It fails both rulings.
  - (b) U leaves out P(N), and step 1's audit set is U with P(N) and F(N). Step 1 then fires for a
    spec nothing has reached, round 0 included, and steps 3 and 4 stay reachable. The audit set keeps
    the owner's "re-audits only the specs it folded" when step 1 fires on a folding round. §4 is
    written to this option.
  - (c) Move step 1 below step 4. A stop could then leave a roster spec no round reached, which fails
    R1's "all the specs fully reviewed".
  Recommendation: (b). It is the only option meeting both rulings and R1, and it changes one set's
  definition and no step's position. AC6 and AC8 are its discriminating arms.
  RESOLVED (agent, 2026-11-01, delegated): (b). U leaves out P(N), and step 1's audit set is U with
  P(N) and F(N), because it alone meets both owner rulings and R1.

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from the design's [chain] and [address], the brief's acceptance
  line 5, the scout's Q4 and Q5, and `TOOL-dFoldedAudit-3`, `-4` and `-7` as authored.
- rev-2 · 2026-11-01 · §4 · §8 · F1 is RESOLVED to option (b) and the header gains `ratified`. M2's
  cross-read found two disagreements with `TOOL-dFoldedAudit-4`: `renderChainRecord` read
  `siblingEdits` under any declared `disposal` where that unit returns it under `by-nature` alone,
  and the suite doubles gained `addresses` for `TOOL-dFoldedAudit-3`'s arms only, where row 17 also
  reaches that unit's.

## 10. Reuse audit

`reuse_lookup.py` on "derive a stop verdict for a review chain from append-only round records"
ranked name-stem symbols and no chain reader, so the row reader's seam is `review_counts` and
`review_last_reason` (`tools/unattended/unattended.sh:12630-12657`), one awk per projection over an
append-only ` · ` row. This unit extends the driver's verb table, `VERB_REQUIRES`, `roster_ids`,
`spec_ids`, `load_spec_facts`, `refuse_if_terminal` and `stage_runmd`. In the harness it extends the
stage's hoist, `deriveDispositionFault` and `nextAction`. In the review it extends the tally at
`tools/workflows/tier2-review.template.js:1953-1987` through the `tallyFault` the callers already
refuse. No existing verb records a round with no run-state file, because every recording verb calls
`check_run_state`, so the verb itself is new and the scout's "no new verb" gave way to [address].
`tools/memory-tree/gotchas.py --for-paths` selected `fixture-passes-by-finding-nothing`, which AC9's
populations answer, and `staged-break-substitutes-a-synthetic-value`, which is why AC8 runs the
shipped default rather than a lowered ceiling. The scout's cites were re-read against source and
held at this base. It said `tools/unattended/check-pass-order.sh` and the `--close` terms need no
change, and that stands. The recall hits on TOOL-aWokenSentinel-30, TOOL-dLoggedFlight-34 and
aEvidencedLens-8's F3 agree that no chain counter exists, and that the parked generation bound is
what this answers.

Recall terms used: `python tools/memory-recall/query.py "how does a spec audit chain stop and where is the promoted unit list durable" --terms "spec-audit chain generation promotedIds rescope review row subject round disposal BOUNDED ceiling hold"`
