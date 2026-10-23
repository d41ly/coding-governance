# TOOL-dFairHearing-20 — a gapped whole-design walk reds the harness's returned counts, not only its prose

**Status:** OPEN · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 19 · advances TOOL-dFairHearing-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-20-deviation-201.md](../build/2026-10-23-build-TOOL-dFairHearing-20-deviation-201.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dFairHearing-20-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-20-1-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dFairHearing-20-promoted-fix-brief-2.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-20-promoted-fix-brief-2.md) | research | TOOL-dFairHearing-21 TOOL-dFairHearing-22 TOOL-dFairHearing-23 |
| [2026-10-23-prompt-TOOL-dFairHearing-20-promoted-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-20-promoted-fix-brief.md) | research | TOOL-dFairHearing-21 TOOL-dFairHearing-22 TOOL-dFairHearing-23 |
| [2026-10-23-review-TOOL-dFairHearing-20-23-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-20-23-spec-audit.md) | spec-audit | TOOL-dFairHearing-22 TOOL-dFairHearing-21 TOOL-dFairHearing-23 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit's finding id 37 (item H1, HIGH,
`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md`) is closed: a
`whole-design` run whose walk table has a gap returns `blockers`, `highs`, `roundCount` and
`roundState` as `null` and a note opening `BLOCKED:`, so no machine caller routing on the counts reads
a gapped walk as clean. Today `TOOL-dFairHearing-18` §4 "The gaps" makes the red only a synthesis
prompt instruction, and `TOOL-dFairHearing-17`'s rule returns `CONVERGED` at a count of 0 beside a
non-empty `walkGaps`.

## 2. Scope (IN)

- **S1** — One condition, `walkRed`, computed once after the walkers return and before the synthesis
  prompt is built: `true` on a `whole-design` run whose `deriveWalkGaps` result is non-empty, `false`
  on every other run. The synthesis prompt's BLOCKED sentence that `TOOL-dFairHearing-18` S4 writes is
  emitted from `walkRed` and from nothing else. Observed by AC1, AC2 and AC4.
- **S2** — With `walkRed`, the harness's return carries `blockers: null`, `highs: null`,
  `roundCount: null` and `roundState: null`, whatever the synthesis item list or the confirmed set
  holds, and its `note` opens `BLOCKED: the walk table has <n> gap(s)` and names the four null fields.
  The note ranks after the dead-synthesis `DEFERRED:` note and before the tally fault's `UNVERIFIED:`
  note. Observed by AC1 and AC2.
- **S3** — With `walkRed`, the `review-round` record line `TOOL-dFairHearing-17` S4 renders reads
  `count=-` and `state=-`, because it is rendered from the same nulls the return carries. Observed by
  AC3.
- **S4** — The args header of `tools/workflows/tier2-review.js` and the return-field list in
  `tools/workflows/README.md` state that a gapped walk nulls the four counts and why. Observed by AC4.
- **S5** — The suite arm the `New arm:` line in §7 declares. Observed by AC1, AC2 and AC3 through that
  line, RED-first at the close.

## 3. Non-goals (OUT)

- No change to `deriveWalkGaps`, the slices, the walk table or the cell sample: what a gap is stays
  `TOOL-dFairHearing-18`'s.
- No new `roundState` token. A gapped round has no state the rule computes, so the field is `null`, the
  value `TOOL-dFairHearing-17` §4 "The returns" already gives an exit it computes nothing on, and the
  parity arm's five tokens are untouched.
- No fabricated blocker count. A floor such as `blockers = walkGaps.length` would count gaps as
  findings nobody raised; `null` is the stated absence the build harness already refuses to round to
  zero (`tools/workflows/unattended-build.template.js:1764-1775`).
- No change to any preset other than `whole-design`, and no change to the diff kind.
- No unattended-build wiring of the `whole-design` preset; none exists in this build.
- No help page: `help/` holds no page on the review harness.

### Edges

- **consumes-from** `TOOL-dFairHearing-18` — `deriveWalkGaps`, `walkGaps` on the return and the synthesis prompt's BLOCKED sentence, which S1 gates on one condition; without them there is no gap to red on
- **consumes-from** `TOOL-dFairHearing-17` — `roundCount`, `roundState` and `renderRoundLine`, which S2 and S3 null on a gapped walk; without them the round fields this unit nulls do not exist
- **hands-off** `TOOL-dFairHearing-27` — finding ids 7 and 8 of the spec audit of units 20 to 23: AC2's absence half read as the walk-gap line (its S25, AC20) and S4's args-header half observed (its S26, AC21)

## 4. Design

### Evidence

- The return's counts are nulled today on exactly one condition past the synthesis, the tally fault:
  `blockers` and `highs` stay `null` and the note reads `UNVERIFIED: ... so blockers and highs are
  null` (`tools/workflows/tier2-review.template.js:1972-1979`, `:2057-2058`). S2 is a second condition
  of that kind, in the same return.
- The build harness reads a non-integer `blockers` as a DEGRADED run and throws rather than rounding it
  to zero (`tools/workflows/unattended-build.template.js:1764-1775`), so `null` reaches every machine
  caller as not-clean.
- `TOOL-dFairHearing-17` §4 "The count" computes `roundCount` from the confirmed blocker and high
  counts before the synthesis, and its rule returns `CONVERGED` when that count is 0; a no-finding walk
  under `TOOL-dFairHearing-18` S6 still synthesizes, so without this unit its return reads
  `roundState: 'CONVERGED'` beside a non-empty `walkGaps`.

### The condition

```
walkRed = preset === 'whole-design' && walkGaps.length > 0
```

It is a `const` defined once, beside the `walkGaps` computation `TOOL-dFairHearing-18` adds. Three
readers use it, and no reader re-derives it from `walkGaps`: the synthesis prompt's BLOCKED sentence,
the round line's inputs, and the final return. A walker death defers the run before this line, as
every lens death does, so `walkRed` is never computed over a partial set of walker returns.

### The return

| Field | `walkRed` false | `walkRed` true |
|---|---|---|
| `blockers`, `highs` | as today, from the item list | `null` |
| `roundCount` | `TOOL-dFairHearing-17`'s count | `null` |
| `roundState` | `TOOL-dFairHearing-17`'s rule | `null` |
| `walkGaps` | `[]` | the gaps, unchanged |
| `note` | as today | `BLOCKED: the walk table has <n> gap(s); blockers, highs, roundCount and roundState are null` |

The note's precedence is worst first, the order the return's own comment states
(`tools/workflows/tier2-review.template.js:2046-2051`): a dead synthesis is `DEFERRED:`, then a gapped
walk is `BLOCKED:`, then a tally fault is `UNVERIFIED:`.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `walkRed` | constant, `tools/workflows/tier2-review.js` | none: `.lexicon.conf` declares no JS constant cell |

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/README.md`

`tools/workflows/tier2-review.js` is the render of its template: the template is the edit and the
render its copy.

### Alternatives rejected

- **A blocker floor of one per gap.** The report's fix offers it. It makes `blockers + highs` exceed
  `confirmed` on a no-finding walk, which the build harness refuses as an unreadable contract
  (`tools/workflows/unattended-build.template.js:1786-1787`), and it counts gaps as findings.
- **A `BLOCKED` roundState token.** It adds a sixth token to `TOOL-dFairHearing-17`'s rule, which its
  parity arm holds equal to the driver's `review_state`, and the driver has no such token
  (`tools/unattended/unattended.sh:12612-12619`).

## 5. Production-readiness checklist

- security — no new input, write path or surface; a stricter return on an existing run.
- perf / scale — one boolean computed once per run.
- error / empty / loading states — a gapped walk reads `null` on all four counts; a walker death still
  defers before the condition is computed.
- observability — the note names the gap count and the nulled fields; `walkGaps` still lists each gap.
- risks — a caller that read `blockers` 0 on a gapped walk as clean now reads `null`; that is the
  defect closed, and the build harness already treats `null` as degraded.
- testing — scratch AsyncFunction stub runs of the render; the arm in §7 is observed RED then GREEN by
  the main loop at the close.
- migration — none: no caller wires the preset yet.
- user docs — `tools/workflows/README.md`'s return-field list; no help page covers the harness.

## 6. Acceptance criteria

- **AC1** — When a scratch AsyncFunction run of `tools/workflows/tier2-review.js`, the stub shape of
  `TOOL-dFairHearing-18` AC4, runs `whole-design` with five walker stubs raising no finding, one of
  them returning a planted empty cell (`witness` of `'  '`), the return carries `walkGaps` of length 1,
  `blockers: null`, `highs: null`, `roundCount: null` and `roundState: null`, and its `note` opens
  `BLOCKED: the walk table has 1 gap(s)`.
  Red when: the return carries `roundState: 'CONVERGED'` or `blockers: 0` beside the non-empty
  `walkGaps`.
  cost: a scratch harness of about 100 lines, reusing `TOOL-dFairHearing-18` AC4's stubs.
- **AC2** — When the same harness runs the same walk with every table complete, the return carries
  `walkGaps: []`, `blockers: 0`, `highs: 0`, `roundCount: 0` and `roundState: 'CONVERGED'`, and the
  synthesis prompt carries no `BLOCKED` sentence; and `grep -c "const walkRed" tools/workflows/tier2-review.js`
  prints 1.
  Red when: the nulls are unconditional, so a complete walk also returns `null`, or the condition is
  re-derived at a second site.
- **AC3** — When the gapped run of AC1 builds its synthesis prompt, the line between the `<<<ROUND` and
  `ROUND>>>` markers carries `count=-` and `state=-`.
  Red when: the round line reads `state=CONVERGED` on a gapped walk.
- **AC4** — When `grep -n "walkRed\|BLOCKED:" tools/workflows/README.md` runs, it prints the return
  list's sentence naming the four nulled fields, and `grep -c "walkRed" tools/workflows/tier2-review.template.js`
  equals the same count over `tools/workflows/tier2-review.js`.
  Red when: the template is edited and the render is not, so the two counts differ.

## 7. Gates

`tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `review-join self-test` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · covers AC1 AC2 AC3 · a whole-design stub run with one planted empty cell and no finding, staged against the harness at `TOOL-dFairHearing-18`'s commit, whose return reads `roundState` CONVERGED beside the gap · FLOOR_ASSERTIONS in that suite, raised by the arms added

## 8. Open questions

- **F1 — How does the return carry the red?** Options: (a) `null` on `blockers`, `highs`, `roundCount`
  and `roundState`, with a `BLOCKED:` note; (b) a blocker floor of one per gap; (c) a new `roundState`
  token. (b) fails the build harness's `blockers + highs <= confirmed` contract on a no-finding walk,
  and (c) breaks `TOOL-dFairHearing-17`'s parity with the driver, which has no such token; (a) reuses the
  tally fault's null precedent in the same return. RESOLVED (agent, 2026-10-23, delegated): (a), rung
  3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 37 (item H1) of the round-1 spec audit.
- rev-2 · 2026-10-23 · §3 · the disposal of the spec audit of units 20 to 23: a hands-off edge to TOOL-dFairHearing-27, naming the two findings it closes on this spec and the criterion it supersedes.

## 10. Reuse audit

The seam is the harness's own tally-fault path: the return already nulls `blockers` and `highs` on a
condition past the synthesis and names it in `note` (`tools/workflows/tier2-review.template.js:1972-1979`,
`:2057-2058`), and the build harness already reads `null` as degraded
(`tools/workflows/unattended-build.template.js:1764-1775`). `python tools/codebase-map/reuse_lookup.py
"null the returned blocker and high counts when the review cannot be trusted"` ranked generic `count`
stems and `review_state` in `tools/unattended/unattended.sh`, the driver's rule `TOOL-dFairHearing-17`
mirrors; it did not surface the tally-fault return, which the source read found. The recall query
returned the audit's H1 item, `TOOL-dMergedTally-1` (the raw-id tally whose null this reuses) and
`TOOL-dRetiredFork-22`'s impossible `CONVERGING` beside `blockers: 0`, the same false-clean class.

Recall terms used: `python tools/memory-recall/query.py "when does a review harness return null blocker counts instead of a clean zero" --terms "tally fault blockers highs null synthesis BLOCKED verdict roundState converged walk gaps return"`
