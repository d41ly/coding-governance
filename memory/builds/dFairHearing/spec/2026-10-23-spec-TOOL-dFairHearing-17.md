# TOOL-dFairHearing-17 — each review round's state, computed by the harness and carried in its record

**Status:** OPEN · rev-3 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 17 · advances TOOL-dFairHearing-19

**Carries:** cl-dClosedLoop-0084@b793fdd5 whole

**Carries:** node:record-kind.review

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-17-deviation-171.md](../build/2026-10-23-build-TOOL-dFairHearing-17-deviation-171.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dFairHearing-1-amend-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-amend-fix-brief.md) | research | TOOL-dFairHearing-1 |
| [2026-10-23-prompt-TOOL-dFairHearing-1-repin-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-repin-brief.md) | research | TOOL-dFairHearing-1 |
| [2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-18 |
| [2026-10-23-prompt-TOOL-dFairHearing-1-token-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-token-fix-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-12 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-18 |
| [2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md) | spec-audit | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-18 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/workflows/tier2-review.js` computes each round's state, `CONVERGED`, `NON-CONVERGENT`, `BOUNDED`
or `CEILING`, against the round before from that round's blocker and high count, at the `roundLimit`
its caller passes. The state reaches the harness's return as `roundState` and the review record as one
`review-round` line. Today only the unattended driver's `review_state` computes it
(`tools/unattended/unattended.sh:12610-12618`), from blockers alone, so an attended review, a promotion
chain or a follow-up round has no rule (`gap-review-21`).

## 2. Scope (IN)

- **S1** — `deriveRoundState(priorCounts, count, roundLimit)`, a pure function in the prelude of
  `tools/workflows/tier2-review.template.js` and its render `tools/workflows/tier2-review.js`, returning
  one of `CONVERGED`, `NON-CONVERGENT`, `CEILING`, `BOUNDED` and `CONVERGING` in `review_state`'s test
  order. Observed by AC1, AC2, AC3.
- **S2** — two arguments, `roundLimit` and `priorCounts`, validated once at the argument boundary
  beside `round`, with `round` inferred from `priorCounts` when no explicit round is passed. Observed
  by AC4.
- **S3** — `roundState` and `roundCount` on every return of the harness, computed on every `complete`
  exit and `null` on every `deferred-platform` exit. Observed by AC5.
- **S4** — the record's `review-round` line, rendered by the pure `renderRoundLine` before the
  synthesis and copied verbatim by the synthesis agent below the review-shape line. This is what the
  unit builds for `record-kind.review`. Observed by AC5.
- **S5** — a parity arm in `tools/workflows/tier2-review.test.sh` holding `deriveRoundState` equal to
  the driver's `review_state` over every sequence both can see, and the driver's path added to that
  suite's leg guard in `tools/gate-legs.json`. Observed by AC6, AC8.
- **S6** — the args header of the harness and the return-field list in `tools/workflows/README.md`
  name the two arguments, the two return fields and the record line. Observed by AC7.
- **S7** — the comment at `tools/workflows/unattended-build.template.js:1675-1678`, which says no JS can
  compute a round's state, rewritten to name the harness's `roundState` and the parity arm, in the
  template and its render. Observed by AC9.
- **S8** — the suite arm the `New arm:` line in §7 declares. Observed by AC1, AC2, AC3, AC4, AC5, AC6
  through that line, RED-first at the close.

## 3. Non-goals (OUT)

- No change under `tools/unattended/`. The driver keeps `review_state` and its blocker-only rows, and
  the parity arm, not a shared call, holds the two rules equal (§8 F3).
- No loop control in the harness. It reports a round's state and never stops, re-arms or refuses a
  round on it; routing on the state is dDeclaredLoop's convergence routing.
- No read of `review.max-rounds` or any other dDeclaredLoop key. The limit is the caller's
  `roundLimit` argument, and a later build's key is used as a stand-in nowhere here.
- No reading of the precision floor, which `gap-review-21` also names. The clause states the round
  state only, and the floor's chain rule is BUILD-METHOD M4's.
- No change to what `tools/workflows/unattended-build.js` passes its callee. An unattended run records
  its rounds through the driver, as today; only the stale comment of S7 moves.
- No hygiene check grading the `review-round` line. The synthesis copy is unverified, as the
  review-shape line's is, and the return is the source of record.
- No help page: `help/` holds `help/README.md`, `help/measure-legs.md` and `help/roles.md`, and none
  describes the review harness's arguments or return.
- No kit version constant moved: the lander mints them.

### Edges

- **hands-off** `TOOL-dFairHearing-18` — the whole-design preset's rounds carry `roundState` and
  `roundCount` computed by this unit's rule over the walk's confirmed findings, and that unit adds
  nothing to the rule
- **hands-off** external — dDeclaredLoop's convergence routing passes `review.max-rounds` as
  `roundLimit` and routes on `roundState`, which is also where `RUNAWAY_CEILING` retires
- **hands-off** `TOOL-dFairHearing-20` — finding id 37 (item H1) of the round-1 spec audit: on a gapped whole-design walk `roundCount` and `roundState` read null, never this unit's rule over a count of 0
- **hands-off** `TOOL-dFairHearing-23` — finding ids 4, 14, 15, 33 and 38 of the round-1 spec audit: AC9's render-diff clause replaced by a template-and-render count (its S7, S8, AC4), AC6's parity arm asserting the four in-domain tokens with `CEILING` held directly (its S19, S20, AC11), and the kickoff manifest re-stamp after the gate-legs.json edit (its S28, AC19)

## 4. Design

### The rule

```
deriveRoundState(priorCounts, count, roundLimit)      round = priorCounts.length + 1
  count === 0                                       -> CONVERGED
  priorCounts non-empty and count >= its last entry -> NON-CONVERGENT
  roundLimit !== null and round > roundLimit        -> CEILING
  roundLimit !== null and round === roundLimit      -> BOUNDED
  otherwise                                         -> CONVERGING
```

This is `review_state`'s order (`tools/unattended/unattended.sh:12610-12618`): zero first, then the
non-decrease test against the round before, then the ceiling, then the bound. The driver's runaway
ceiling (`RUNAWAY_CEILING="8"`, `:774`) becomes one run past the caller's limit, and its bound becomes
the limit itself. A flat sequence and an oscillating one stop at the first round that does not fall,
because the test compares against the round before and never against a round further back. A strictly
falling sequence reads `BOUNDED` at the round equal to the limit and `CEILING` one run past it.
`CONVERGING`, the non-terminal state, is the driver's fifth token, kept by §8 F4.

The function lives in the prelude, beside `renderShapeLine` (`tools/workflows/tier2-review.js:78-83`),
so the suite's extraction (`tools/workflows/tier2-review.test.sh:70-81`) and a scratch slice reach it.

### The count

`roundCount` is the number of confirmed findings whose binding grade is blocker or high:
`verifiedCounts.blocker + verifiedCounts.high`, the counts built at `tools/workflows/tier2-review.js:1639-1644`
and printed as the review-shape line's `blocker=` and `high=` fields. It is known before the synthesis
runs, so the record line can carry the state, and it is untouched by the tally fault that nulls
`blockers` and `highs` (`:1973-1979`). §8 F2 settles this against the synthesis's adjudicated items.

### The arguments

Beside `priorFindings` and `round` (`tools/workflows/tier2-review.js:293-296`):

- `roundLimit`: absent reads as `null`; otherwise a JavaScript integer of 1 or more, else refused
  naming `roundLimit`. With `null`, `BOUNDED` and `CEILING` cannot be reached, and one log line says so
  before the first agent (§8 F5).
- `priorCounts`: the blocker and high counts of the rounds before this one, in round order, each the
  `roundCount` that round's return carried. Absent reads as absent; otherwise an array of JavaScript
  integers of 0 or more, else refused naming `priorCounts`.
- `round` keeps its explicit form. With no explicit round and a non-empty `priorCounts`, it is
  `priorCounts.length + 1`; otherwise today's inference stands. An explicit round that disagrees with
  `priorCounts.length + 1` is refused, naming both values.
- Round 1 with no `priorCounts` computes over `[]`. A round above 1 with no `priorCounts` computes
  nothing: `roundState` is `null` and a WARNING before the first agent names `priorCounts` (§8 F6).

Neither argument reaches a lens or skeptic prompt, so neither joins the review key's input print
(`tools/workflows/tier2-review.js:949-992`), and a resumed run still reuses its lens files.

### The returns

Every return carries `roundState` and `roundCount` beside `round` (`tools/workflows/tier2-review.js:2068`):

| Exit | Lines | `roundCount` | `roundState` |
|---|---|---|---|
| every lens dead | `:1301-1320` | `null` | `null` |
| no finding raised, complete | `:1321-1342` | `0` | the rule over 0 |
| no finding raised, deferred | `:1321-1342` | `null` | `null` |
| every finding refuted, complete | `:1654-1679` | `0` | the rule over 0 |
| every finding refuted, deferred | `:1654-1679` | `null` | `null` |
| partial fan | `:1687-1708` | `null` | `null` |
| synthesis ran | `:2015-2080` | the count | the rule |
| synthesis died | `:2015-2080` | `null` | `null` |

`roundState` is also `null` wherever §8 F6's missing `priorCounts` applies. `roundCount` stays an
integer there, so a caller can still pass it on as the next round's prior count.

### The record line

```
review-round round=<n> limit=<n|-> prior=<c1,c2,…|-> count=<n> state=<STATE|->
```

`renderRoundLine` renders it from `round`, `roundLimit`, `priorCounts`, `roundCount` and `roundState`,
a `-` standing for an absent value, never a `0`. It is computed once, before the synthesis, from the
same `roundState` the final return carries. The synthesis prompt hands it between `<<<ROUND` and
`ROUND>>>` marker lines, after the review-shape block (`tools/workflows/tier2-review.js:1902-1903`), with
the instruction to copy it verbatim, alone on its line, directly below the review-shape line. A
`review-round` line is what `record-kind.review` gains: every record a synthesis writes states its
round's state, attended or not.

### The parity arm

`tools/workflows/tier2-review.test.sh` reads the memory-tree kit's generator already
(`tools/workflows/tier2-review.test.sh:244-260`), and its leg guards that path
(`tools/gate-legs.json`, leg `tier2-review self-test`). The new arm slices `review_state()` and the
`RUNAWAY_CEILING=` line from `tools/unattended/unattended.sh`, evaluates them in bash, and compares the
token each prints with `deriveRoundState` over every sequence of 0 to 3 prior counts, each 0 to 3, a
current count of 0 to 3, and a limit of 1 to 4 with the round at or below it. Highs are 0 there, so the
driver's blocker count and the harness's count are one number. The arm also asserts each of the five
tokens appears at least once, so a slice that matched nothing cannot pass. A driver that cannot be read
or sliced fails the arm; it never skips.

The domain stops at the limit on purpose. Past it the driver refuses the round outright
(`tools/unattended/unattended.sh:12762-12765`) where the harness reports `CEILING`, so the two answer
different questions there and the arm says so in its header.

`{prefix}/unattended/unattended.sh` joins that leg's `guard` list in `tools/gate-legs.json`, so a
change to `review_state` alone selects the arm under the scoped bar.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `deriveRoundState` | function, `tools/workflows/tier2-review.js` | `js.function`, OK |
| `renderRoundLine` | function, `tools/workflows/tier2-review.js` | `js.function`, OK |
| `roundLimit`, `priorCounts` | harness arguments | none |
| `roundState`, `roundCount` | harness return fields | none |
| `review-round` | record line head | none |
| `<<<ROUND`, `ROUND>>>` | synthesis prompt markers | none |

### Migration

None. Both arguments are optional, and a caller passing neither gets today's behaviour plus two return
fields and a record line whose `limit` reads `-`.

### Rollout

The landing turns the field and the line on for every run at once. The next round of any review can
pass the previous return's `roundCount` as its `priorCounts`.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`
- `tools/workflows/README.md`
- `tools/gate-legs.json`

`tools/workflows/tier2-review.js` and `tools/workflows/unattended-build.js` are renders of their
templates (`check-protocol-parity.test.sh --render`). The template is the edit and the render its
copy.

### Alternatives rejected

- **Derive the prior counts from `priorFindings`.** BUILD-METHOD M8 passes round N only the blockers
  the fold fixed as `priorFindings` (`memory/guides/BUILD-METHOD.md:255-257`), a subset, and the
  argument carries one round, never the sequence. A count derived from it would be wrong by design.
- **Have the synthesis agent compute and write the state.** The harness already counts what an agent
  was trusted to count and could not (`tools/workflows/tier2-review.js:1879-1888`). A rule the
  harness computes cannot drift that way.
- **Append the state to the review-shape line.** That line's grammar is fixed and documented
  (`tools/workflows/README.md:288-301`). A separate line adds a field to the record without moving a
  line any reader parses.

## 5. Production-readiness checklist

- security — no new write path or surface. Both arguments are integer-checked before any agent, so no
  string reaches a prompt from them.
- perf / scale — one pure function over at most a handful of integers per run; no agent added.
- error / empty / loading states — a malformed argument refuses before the first agent; a missing
  limit and a missing prior sequence are each announced in the log, and a missing prior sequence gives
  `null`, never a guessed state.
- observability — the record line and the return carry the state on every complete run, and the log
  names each degraded input.
- risks — the record copy is the synthesis agent's and is not verified; the return is the source of
  record, as for the review-shape line. The harness's count is by binding grade, so it can differ from
  the driver's recorded blocker count where the synthesis regrades; `regraded` already names those ids.
- testing — the pass probes the function, the boundary and a stub run with scratch node scripts; the
  suite arm in §7 is observed RED then GREEN by the main loop at the close.
- migration — none, as §4 Migration says.
- user docs — `tools/workflows/README.md` is the kit's reference for arguments and return fields;
  §3 says why no help page changes.

## 6. Acceptance criteria

- **AC1** — When a scratch node probe slices `function deriveRoundState(` through its closing `}` out of
  `tools/workflows/tier2-review.js` and calls it, the planted flat sequence `deriveRoundState([3], 3, 5)`
  and the planted oscillating one `deriveRoundState([2, 1], 2, 5)` each return `NON-CONVERGENT`, and
  their strictly falling twins `deriveRoundState([3], 2, 5)` and `deriveRoundState([3, 2], 1, 5)` each
  return `CONVERGING`.
  Red when: the non-decrease test reads `>` instead of `>=`, so the flat sequence returns `CONVERGING`.
- **AC2** — When the same probe calls `deriveRoundState([3, 2], 1, 3)`, a strictly falling sequence
  reaching its caller's limit, it returns `BOUNDED`; `deriveRoundState([4, 3, 2], 1, 3)`, one run past
  it, returns `CEILING`; `deriveRoundState([3], 2, 3)` returns `CONVERGING`; and
  `deriveRoundState([3, 2], 1, null)` returns `CONVERGING`.
  Red when: the bound is tested before the ceiling as `round >= roundLimit`, so one run past reads
  `BOUNDED`.
- **AC3** — When the same probe calls `deriveRoundState` with a count of 0 after `[]`, after `[2, 1]` and
  after `[4, 3, 2]` with a limit of 3, each returns `CONVERGED`; `deriveRoundState([], 2, 1)` returns
  `BOUNDED` and `deriveRoundState([], 2, 3)` returns `CONVERGING`.
  Red when: the limit tests run before the zero test, so a clean round past its limit reads `CEILING`.
- **AC4** — When a scratch node probe evaluates the prelude of `tools/workflows/tier2-review.js`, cut as
  `tools/workflows/tier2-review.test.sh:70-92` cuts it, on a spec-audit subject, `roundLimit` of `0`,
  `2.5` or `'3'` each throws naming `roundLimit`; `priorCounts` of `'x'`, `[1, -1]` or `[1.5]` each
  throws naming `priorCounts`; `round: 3` with `priorCounts: [2]` throws naming both; `round: 3` with
  `priorCounts: [4, 2]` and `roundLimit: 3` proceeds; and with no `round` and `priorCounts: [4, 2]` the
  evaluated `round` is 3.
  Red when: the length check is missing, so `round: 3` with `priorCounts: [2]` proceeds.
- **AC5** — When a scratch AsyncFunction run of `tools/workflows/tier2-review.js`, the shape
  `tools/workflows/tier2-review.test.sh:321-340` uses, passes `round: 3`, `priorCounts: [4, 2]` and
  `roundLimit: 3`, and its stubs confirm one finding at grade high and refute the rest, the return
  carries `roundState: 'BOUNDED'` and `roundCount: 1`, and the synthesis prompt carries
  `review-round round=3 limit=3 prior=4,2 count=1 state=BOUNDED` between the `<<<ROUND` and `ROUND>>>`
  lines. The same run with one lens stub returning null returns `roundState: null`; a run at `round: 2`
  with no `priorCounts` returns `roundState: null` and logs a WARNING naming `priorCounts`; and a run
  whose lenses raise nothing returns `roundState: 'CONVERGED'` and `roundCount: 0`.
  Red when: the final return omits `roundState`, or the deferred run reports a state.
  cost: a scratch harness of about 80 lines, modelled on that suite's stub agents.
- **AC6** — When a scratch probe evaluates `review_state` sliced from `tools/unattended/unattended.sh`
  with its `RUNAWAY_CEILING`, and `deriveRoundState`, over every sequence of 0 to 3 prior counts of 0 to
  3, a count of 0 to 3 and a limit of 1 to 4 with the round at or below the limit, both print the same
  token on every row, and each of `CONVERGED`, `NON-CONVERGENT`, `BOUNDED`, `CEILING` and `CONVERGING`
  appears at least once.
  Red when: either side swaps its bound and ceiling tests, so the rows at the limit disagree.
  figure: the row count is DERIVED by the enumeration at observation time.
- **AC7** — When `grep -c` runs over `tools/workflows/README.md` for each of `roundState`, `roundCount`,
  `roundLimit`, `priorCounts` and `review-round`, each prints at least 1; and the args header of
  `tools/workflows/tier2-review.js` carries `roundLimit:` and `priorCounts:` as key lines, the shape
  `tools/workflows/tier2-review.test.sh:312` reads.
  Red when: a field read off `a` is documented in prose only, so the header arm names it missing.
- **AC8** — When `python -c` loads `tools/gate-legs.json` and prints the `guard` of the leg named
  `tier2-review self-test`, the list carries the driver's entry beside its two existing entries,
  spelled with the manifest's `{prefix}` token, which resolves here to `tools/unattended/unattended.sh`.
  Red when: the guard lacks the driver's path, so a change to `review_state` alone selects no parity
  arm under the scoped bar.
- **AC9** — When `grep -c 'no JS can compute it'` runs over `tools/workflows/unattended-build.template.js`
  and `tools/workflows/unattended-build.js`, each prints 0 and `grep -c roundState` prints at least 1 in
  each; and `sed 's/{{FANOUT_CAP}}/5/g'` over each template piped to `diff -` against its render prints
  nothing, for both `tools/workflows/tier2-review.template.js` and
  `tools/workflows/unattended-build.template.js`.
  Red when: a template is edited and its render is not re-rendered, so the diff prints the hunk.
  figure: the cap `5` is PINNED at base `3708a705`; read the render's own `boundedParallel` default if
  `.agent-cap.conf` moved it.

## 7. Gates

`tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `review-join self-test` · `verifier fan-out` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `lexicon naming predicates` · `testsuite counts (every bar self-test prints one)` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 · the planted flat, oscillating, at-limit and past-limit sequences, a round 3 with a two-short prior sequence, a stub run's return and round line, and the driver parity table, each staged against the base harness, which has no deriveRoundState · FLOOR_ASSERTIONS in that suite, raised by the arms added

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that a
  legal status?** Probe: `STATUS_TOKENS` in `tools/memory-tree/tree_lib.py:28`, which the header regex
  at `tools/memory-tree/tree_lib.py:377` joins. Observation: the set is `OPEN SPECCED INPROGRESS
  BLOCKED DEFERRED CLOSED WONTDO`, so a `DRAFT` header parses as no header and the unit reads MISSING.
  Liveness: the probe reads a tuple that would carry `DRAFT` if the vocabulary admitted it. RESOLVED
  (agent, 2026-10-23, delegated): `OPEN`, the token `memory/TEMPLATE-SPEC.md` gives drafting.
- **F2 — Which blocker and high count does the rule read: the binding grades of the confirmed
  findings, or the synthesis's adjudicated `blockers` and `highs`?** Options: (a) binding grades,
  `verifiedCounts.blocker + verifiedCounts.high`, known before the synthesis; (b) the item tally after
  it. Both meet every criterion of §6 for the return. Only (a) is known when the synthesis prompt is
  written, so only (a) lets the record carry the state, which is what `record-kind.review` gains. (b)
  is null on every tally fault and on a dead synthesis, so it leaves a complete verify stage with no
  state. RESOLVED (agent, 2026-10-23, delegated): (a), the most feature-rich option, rung 3. The
  difference from the driver's recorded count is named in §5 risks.
- **F3 — Does the unattended driver's `review_state` then read `roundState`, or stay a second answer
  (the brief's S8)?** Options: (a) the driver reads the harness's field, through a flag the recording
  agent passes; (b) the driver keeps `review_state`, and a parity arm compares the two rules over every
  sequence both can see, the charter's `[one-fact]` "or a gate compares the two". (a) moves the driver's
  input from its own derived rows to a value an agent hands it, against `[derive]`, and changes the
  convergence count of an unattended run from blockers to blockers and highs. That count is stated in
  the unattended verbs carrier, where `--blockers` is "THIS round's confirmed count" and CONVERGED is
  "zero blockers" (`memory/guides/UNATTENDED-VERBS.md:778-786`), a governance-carrier change clause
  `cl-dClosedLoop-0084` does not name, so veto 2 holds outside the grant. It also edits
  `tools/unattended/`, whose suites this landing does not read. RESOLVED (agent, 2026-10-23,
  delegated): (b), rung 3; dDeclaredLoop's convergence routing is where one rule replaces both, as
  §3 Edges hands off.
- **F4 — What state does a round take that is none of the four the clause names, such as round 1
  with blockers standing under a limit of 3?** Options: (a) `CONVERGING`, the driver's non-terminal
  token; (b) `null`. (b) makes "not terminal" and "not computable" one value, so a caller cannot tell a
  falling round from a degraded one, and the parity arm loses every non-terminal row. RESOLVED (agent,
  2026-10-23, delegated): (a), rung 3. It adds a fifth value to the brief's S8 spelling and to the
  clause's list, so it is recorded as
  `memory/builds/dFairHearing/build/2026-10-23-build-TOOL-dFairHearing-17-deviation-171.md`.
- **F5 — What does an absent `roundLimit` mean?** Options: (a) no limit, so `BOUNDED` and `CEILING`
  are unreachable and the log says so; (b) refuse, which breaks every caller today, the build method's
  closing-review call and `tools/workflows/unattended-build.js` among them; (c) a literal default, such
  as v2's `review.max-rounds` value of 3, which reads a dDeclaredLoop key the packet's Non-goals keep
  out. (b) and (c) each fail a stated bound. RESOLVED (agent, 2026-10-23, delegated): (a), rung 3.
- **F6 — What does a round above 1 with no `priorCounts` compute?** Options: (a) `null` with a
  WARNING; (b) the rule over `[]`; (c) refuse. (b) is the defect `TOOL-dCarriedReceipt-1` records: a
  sequence whose earlier rounds left no rows read `CONVERGING` because its prior count was zero
  (`memory/builds/dCarriedReceipt/BACKLOG.md:21`). (c) refuses the round-N call BUILD-METHOD M8 spells
  today, which passes no prior counts (`memory/guides/BUILD-METHOD.md:261-266`). RESOLVED (agent,
  2026-10-23, delegated): (a), rung 3.
- **F7 — The new arguments, return fields and record line change the harness's public surface; does
  the build's grant cover them?** The clause names the round state in the review report, and
  `PLAY-dClosedLoop-3` grants the public-surface changes a build's own clauses name. RESOLVED (agent,
  2026-10-23, delegated): covered, rung 3.
  grants: PLAY-dClosedLoop-3 the roundLimit and priorCounts arguments, the roundState and roundCount return fields of tier2-review.js, and the review-round line of the review record

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, from the packet's Items 17, the brief's S8, the driver's
  `review_state` and the harness's returns read at base `3708a705`.
- rev-2 · 2026-10-23 · §8 F4 · the `**Carries:**` pin moves from `5c5896a3` to `b793fdd5`, following
  the `amends cl-dClosedLoop-0084@5c5896a3` row of this spec's own deviation record,
  `2026-10-23-build-TOOL-dFairHearing-17-deviation-171`; nothing else changed.
- rev-3 · 2026-10-23 · §3 · the round-1 spec audit's disposal: hands-off edges to TOOL-dFairHearing-20 and TOOL-dFairHearing-23, naming each finding the promoted unit closes on this spec and the criterion of its own it supersedes, if any.

## 10. Reuse audit

The seam is the driver's rule, `review_state` (`tools/unattended/unattended.sh:12594-12618`), whose
order and terminal tokens the harness function takes over unchanged, its bound and ceiling re-read as
the caller's limit; the parity arm keeps the two from drifting. The record line follows the review-shape
line's pattern, a pure renderer (`tools/workflows/tier2-review.js:78-83`) handed to the synthesis between
markers (`:1902-1903`), and the count is the `verifiedCounts` tally the shape line already prints
(`:1639-1644`). The argument checks sit in the prelude the suite extracts, in the shape `intensity` uses
(`:213-217`). No new parser, counter or record writer.

`python tools/codebase-map/reuse_lookup.py "compute whether a review round converged from the prior
rounds blocker counts"` ranked `review_state` (`tools/unattended/unattended.sh`) and
`derive_review_exit` (`tools/runlog/model.py:577`); the second only reads the driver's recorded exit
token back out of a row and computes nothing, so it is no seam for this rule.
`python tools/memory-recall/query.py` returned `memory/guides/UNATTENDED-VERBS.md`'s strictly-smaller
rule (`:778-786`) and the `TOOL-aProbedUnit-6` brief's test order, which agree with source; `TOOL-dCarriedReceipt-1`,
whose defect §8 F6 avoids; and `TOOL-dCarriedReceipt-2`, which cites the terminal-round refusal at
`unattended.sh:3135`, a line number that has gone stale: the refusal is at
`tools/unattended/unattended.sh:12762-12765` today. One source disagrees with this unit once built:
`tools/workflows/unattended-build.template.js:1675-1678` says no JS can compute a round's state, which
S7 rewrites.

Recall terms used: review_state CONVERGED NON-CONVERGENT BOUNDED CEILING RUNAWAY_CEILING REVIEW_ROUNDS strictly smaller blocker count round
