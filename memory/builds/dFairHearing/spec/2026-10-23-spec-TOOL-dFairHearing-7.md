# TOOL-dFairHearing-7 — refuted claims and same-address twins handed to the synthesizer to flag

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 8 · advances TOOL-dFairHearing-19

**Carries:** cl-dClosedLoop-0074@51869353 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |
| [2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md) | spec-audit | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |

<!-- /gen:spec-records -->

## 1. Goal

The synthesis is handed every refuted finding's claim and reason and every pair of a confirmed and a
refuted finding citing one address, and is told to flag a refuted twin of a confirmed finding, which
it returns as `twinFlags` the harness checks. It can note a twin and never overturn a verdict. Today
the synthesizer sees refuted rows only as appendix cells with no claim, and none is pointed at a twin:
9 verified refutations by design sat beside a confirmed twin, and both runtime reports missed A59
against A38 and B61 against B43 (PINNED 2026-10-15,
`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-review-adjudication.md:37-40`,
:101-104). It ships behind a default-off argument, so `TOOL-dFairHearing-1`'s replay can run it
against today's synthesis.

## 2. Scope (IN)

- **S1** — `deriveTwinPairs(confirmed, refuted)`, pure, in the prelude of
  `tools/workflows/tier2-review.template.js`: each pair of a confirmed and a refuted finding that
  `checkSameAddress` reads as one address over `deriveAddressKey`, merged duplicates never among the
  refuted. Observed by AC1, AC6.
- **S2** — the `addressTwins` argument, a closed set `hidden` or `shown`, default `hidden`, refused
  outside the set before any agent, and documented in the `args` header. Observed by AC2.
- **S3** — under `shown`, the synthesis prompt gains a REFUTED findings block and a SAME-ADDRESS PAIRS
  block with the flag instruction, and its schema requires `twinFlags`; under `hidden` the prompt and
  schema are unchanged. Observed by AC3.
- **S4** — the harness keeps a returned flag only when its refuted id stands refuted and its confirmed
  id confirmed, marks each kept flag `sameAddress`, names every discarded one in a warning, and returns
  `twinFlags` and the handed pair count under `shown`. Observed by AC4.
- **S5** — no flag moves a verdict, a grade, an item or a count. Observed by AC5.
- **S6** — `tools/workflows/README.md` documents the argument and the two return fields. Observed by
  AC7.
- **S7** — the suite arms the `New arm:` line in §7 declares. Observed by AC1, AC2, AC3, AC4, AC5, AC6
  through that line, RED-first at the close.

## 3. Non-goals (OUT)

- No verdict overturned. A flagged refuted finding stays refuted in the ledger, the appendix and every
  count, and a flagged confirmed finding keeps its binding grade.
- No twin merge. The twin merge `review.twin` opts into is a second, independent review run merged
  with the first, which is `TOOL-dFairHearing-11`'s; the twins here are two findings of one run.
- No default flip. `addressTwins` stays `hidden` until `TOOL-dFairHearing-1`'s replay records a hit.
- No pairing across rounds: a previous round's findings reach the synthesis only as `priorFindings`
  already, and the review system record leaves cross-round twins to synthesis reading
  (`2026-10-15-build-PLAY-dClosedLoop-1-review-system.md:215-216`).
- No edit to `tools/roles/agents/gov-synthesizer.agent.md`. Its input line, which says it is handed
  confirmed findings, is the record `TOOL-dFairHearing-10`'s clause brings in line after this unit.
- No read of the synthesis items' `grades`: §8 F6.
- No twin pairs in the drift-audit harnesses: the clause names the review's synthesizer.
- No help page: no page under `help/` describes the review harness.
- No kit version moved: the lander mints them (`tools/push-main.sh:26-32`).

### Edges

- **consumes-from** `TOOL-dFairHearing-4` — `deriveAddressKey` and `checkSameAddress` decide which
  findings cite one address; without them no pair can be derived
- **consumes-from** `TOOL-dFairHearing-5` — `refuted` no longer holds a `merged` duplicate; without it a
  duplicate would be shown as a twin of the original it already names
- **hands-off** `TOOL-dFairHearing-1` — the replay runs the shown synthesis through this unit's
  default-off argument, reads the flags it returns, and owns the verdict that would flip its default

## 4. Design

### The pairs

```js
function deriveTwinPairs(confirmed, refuted) {
  const out = []
  for (const c of confirmed)
    for (const r of refuted)
      if (checkSameAddress(deriveAddressKey(c), deriveAddressKey(r))) out.push({ confirmed: c.id, refuted: r.id })
  return out
}
```

Defined in the prelude beside `TOOL-dFairHearing-4`'s address functions, so a slice reaches it. It is
called once after the verdict partition (template :1512-1513 at base), on `confirmed` and on `refuted`,
which after `TOOL-dFairHearing-5` excludes every `merged` duplicate. Pairs come in confirmed-id order,
then refuted-id order, and the key never reads `ref`, so no join is keyed on a `.ref` string
(`tools/hooks/agent-cap.js:1780-1784`). The loop is O(confirmed × refuted), tens by tens on the
corpus the research parsed (1,122 findings over 50 reports, 150 refuted).

### The argument

`addressTwins` is read beside `intensity` (template :210-217): absent reads `hidden`, and anything but
the strings `hidden` and `shown` throws, naming the field and its two values, before the resume probe
spawns. The `args` header (template :91-139) gains an `addressTwins:` key line, which the suite's D9
arm requires (`tools/workflows/tier2-review.test.sh:303-313`). It does not join the review key's input
print: the synthesis writes no keyed file (template :955-957).

### The synthesis prompt

Under `shown`, after the UNVERIFIED block (template :1736-1744), two blocks:

- `REFUTED findings`, one line per refuted finding:
  `- id=<n> [<finder grade>] lens=<lens> <ref> — <claim> | refuted because: <reason>`, the claim and
  reason folded by `renderPromptLine` (template :1619-1623), or `  (none)`. The header says these were
  refuted by a skeptic and are shown so a twin can be seen, and that none may be reinstated, regraded or
  counted.
- `SAME-ADDRESS PAIRS`, one line per pair: `- confirmed id=<c> and refuted id=<r>, both at <file>
  <at>`, or `  (none)`.

Then the instruction: for each pair, and for any refuted finding whose claim reads as the same defect
as a confirmed one, decide whether the two describe one defect; where they do, note the refuted one as
a twin beside the confirmed finding in the report and return the pair in `twinFlags` as
`{refuted, confirmed}`; two different defects at one address are not twins and get no flag; a flag
changes no verdict, grade, item or count. RUN INTEGRITY gains `refuted findings shown: <m>; same-address
pairs shown: <k>.` Under `hidden` none of this is in the prompt.

The synthesis schema (template :1914-1936) gains, under `shown` only, the property
`twinFlags: { type: 'array', items: { type: 'object', required: ['refuted', 'confirmed'], properties:
{ refuted: { type: 'integer' }, confirmed: { type: 'integer' } } } }` and the key in `required`.

### The flags

After the tally (template :1951-1992), under `shown` and with a synthesis:

- a flag is KEPT when its `refuted` is the id of a finding in `refuted` and its `confirmed` the id of
  one in `confirmed`, and a repeat of a kept pair is dropped;
- each kept flag carries `sameAddress`, true when the pair is one `deriveTwinPairs` handed;
- every other flag is DISCARDED, and a `WARNING:` line names them:
  `<k> twin flag(s) named an id that is not refuted or not confirmed — discarded: <refuted>/<confirmed>, …`.

The success return gains, under `shown` only, `twinPairs`, the number of pairs handed, and `twinFlags`,
the kept flags; under `hidden` neither key is present, as `regraded` is absent where no synthesis ran
(template :2047). Nothing downstream of the flags reads them: the counts, `confirmedFindings`, the
ledger and the appendix are computed before and apart from them.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `deriveTwinPairs` | function, `tools/workflows/tier2-review.template.js` | `js.function`, OK |
| `addressTwins` | harness argument | none |
| `twinFlags`, `twinPairs` | synthesis return field and harness return fields | none |
| `sameAddress` | field of a kept flag | none |

The function name was asked of `python tools/lexicon/lexicon.py --suggest deriveTwinPairs --as
js.function` and answered OK.

### Migration

None. A caller passing nothing gets today's synthesis prompt and return.

### Rollout

Dark: `hidden` is the default, and the replay passes `addressTwins: 'shown'`.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`, its render
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/README.md`: an `addressTwins` paragraph beside `intensity`'s (:270-276) and the two
  fields in the return-field list (:288-322)

The render comes from `bash tools/workflows/check-protocol-parity.test.sh --render`.

### Alternatives rejected

- **The flag left to the report's prose.** A replay could only grade it by reading text, and
  TOOL-dMergedTally-1 already moved one synthesis fact from prompt-held prose to returned ids because
  the prose did not hold (template :1879-1888).
- **Every same-address pair, whatever the verdicts.** Two confirmed findings at one address are the
  item merge `TOOL-dFairHearing-6` serves, and two refuted ones have no confirmed defect to be the twin
  of; the record asks for a refuted twin of a confirmed finding (`…-review-system.md:231-233`).
- **Flags outside the handed pairs discarded.** The refuted claims are handed so the synthesizer can
  see a twin the address key misses, as across files; such a flag is kept and marked
  `sameAddress: false`.

## 5. Production-readiness checklist

- security — no new write path. Refuted claims and reasons, agent text, reach one more prompt through
  `renderPromptLine`, as confirmed claims already do; the returned flags are integers checked against
  the run's own id sets.
- perf / scale — one O(confirmed × refuted) pass, and two prompt blocks whose length grows with the
  refuted count, 3 per report on the research's corpus.
- error / empty / loading states — both blocks print `(none)` when empty; a dead synthesis returns no
  flags; a malformed flag is discarded and named.
- observability — RUN INTEGRITY states both counts under `shown`, and the return carries the handed
  pair count beside the kept flags, so a run that flagged nothing is told from one handed nothing.
- risks — a synthesizer may flag two defects at one address as twins; a flag moves nothing, and the
  replay's negative pair measures it.
- testing — the pass probes S1 and S2 by a prelude slice and S3 to S5 by a stub-agent run; the suite
  arm in §7 is observed RED then GREEN by the main loop at the close.
- migration — none, as §4 Migration says.
- user docs — none owed: no page under `help/` describes the review harness.

## 6. Acceptance criteria

- **AC1** — When a scratch node probe evaluates the prelude of `tools/workflows/tier2-review.js` for a
  diff review, cut as `tools/workflows/tier2-review.test.sh:67-81` cuts it and returning
  `deriveTwinPairs` as `tools/workflows/tier2-review.test.sh:237` returns a function, a confirmed
  finding at `a.js` line 10 and refuted findings at `a.js` lines 12 and 14 and at `b.js` line 10 give
  exactly `[{confirmed: 1, refuted: 2}]` for ids 1, 2, 3 and 4. For a spec audit, findings whose `where`
  reads `section 2 S5` and `§2` pair, and one reading `status header` pairs with nothing.
  Red when: the pair is read from `ref` equality, so lines 10 and 12 do not pair.
- **AC2** — When the prelude is evaluated as the suite's `arm` does (`tools/workflows/tier2-review.test.sh:89-99`),
  `addressTwins` absent, `'hidden'` and `'shown'` each proceed, absent resolving to `'hidden'`; `'on'`
  and `true` each throw naming `addressTwins`.
  Red when: the refusal is removed and `'on'` proceeds as hidden.
- **AC3** — When a scratch stub-agent run of `tools/workflows/tier2-review.js`, shaped as
  `tools/workflows/tier2-review.test.sh:333-357`, has a diff review's skeptics confirm id 1 at `a.js`
  line 10 and refute id 2 at `a.js` line 12 with reason `by design`, the run with
  `addressTwins: 'shown'` hands a synthesis prompt carrying `REFUTED findings` with id 2's claim and
  reason, and `SAME-ADDRESS PAIRS` with `confirmed id=1 and refuted id=2`, and its schema requires
  `twinFlags`. The run without the argument hands a prompt carrying neither block and a schema without
  `twinFlags`.
  Red when: the blocks are added on every run, so the default synthesis prompt moves.
  cost: a scratch runner of about 60 lines, modelled on that suite's stubs.
- **AC4** — When the AC3 shown run's synthesis stub returns `twinFlags`
  `[{refuted: 2, confirmed: 1}, {refuted: 2, confirmed: 1}, {refuted: 1, confirmed: 2}, {refuted: 9,
  confirmed: 1}]`, the return's `twinFlags` is `[{refuted: 2, confirmed: 1, sameAddress: true}]`, its
  `twinPairs` is 1, and a `WARNING:` line names `1/2` and `9/1` as discarded. A refuted id 5 at
  `c.js` flagged against id 1 is kept with `sameAddress: false`.
  Red when: the flags are returned as the agent gave them, so `{refuted: 1, confirmed: 2}` survives.
- **AC5** — When the AC3 stubs run once hidden and once shown with that flag list, the two returns
  agree on `confirmed`, `refuted`, `merged`, `precision`, `blockers`, `highs`, `confirmedFindings` and
  `ledger`.
  Red when: a flag reinstates its refuted finding, so the shown run reads one more confirmed.
- **AC6** — When the AC3 shown run instead has id 2 refuted as `duplicate of id=1` in id 1's batch,
  `twinPairs` is 0 and the SAME-ADDRESS PAIRS block reads `(none)`.
  Red when: the pairs are built over every refuted verdict, so a `merged` duplicate is handed as a twin
  of its own original.
- **AC7** — When `grep -n 'addressTwins'` runs over `tools/workflows/README.md` and
  `tools/workflows/tier2-review.template.js`, it finds the README's argument paragraph and the
  template's `args` header line, and `grep -n 'twinFlags'` finds the README's return-field entry.
  Red when: the argument is read off `a` and the README names it nowhere.

## 7. Gates

`tier2-review self-test` · `verifier fan-out self-test` · `unattended-build self-test` · `review-join self-test` · `review-join ban (no ref-keyed join)` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `harness arms (fail branches armed or pinned)` · `testsuite counts (every bar self-test prints one)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 · the base harness, which defines no twin pairs, refuses no addressTwins value and hands the synthesis neither refuted claims nor pairs · FLOOR_ASSERTIONS in that suite, raised by the arms added

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that a
  legal status?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:28`, joined by the header
  regex at `tools/memory-tree/tree_lib.py:377`. Observation, 2026-10-23: `DRAFT` is not in the set, so
  a `DRAFT` header parses as no header and the unit reads MISSING. Liveness: the tuple would carry it
  if the vocabulary admitted it. RESOLVED (agent, 2026-10-23, delegated): `OPEN`, the token
  `memory/TEMPLATE-SPEC.md` gives a spec in drafting.
- **F2 — How does a flag reach anything but the report's prose?** Options: (a) prose only; (b) a
  `twinFlags` return the harness checks against its own id sets. (a) leaves the replay's twins arm
  grading text, and the owed replay must show A59 and A38 flagged and a negative pair not
  (`…-review-system.md:234-235`). RESOLVED (agent, 2026-10-23, delegated): (b), by most criteria
  satisfied, rung 3.
- **F3 — Which pairs are handed?** Options: (a) a confirmed and a refuted finding at one address,
  merged duplicates out; (b) every same-address pair. The record asks the synthesizer to flag a refuted
  twin of a confirmed finding (`…-review-system.md:231-233`). RESOLVED (agent, 2026-10-23,
  delegated): (a), by rung 1.
- **F4 — Is a flag outside the handed pairs kept?** Options: (a) kept when its ids carry the right
  verdicts, marked `sameAddress: false`; (b) discarded. The clause hands refuted claims as well as
  pairs, so a twin across files is in reach; (b) would throw away the one case the address key cannot
  see. RESOLVED (agent, 2026-10-23, delegated): (a), rung 3.
- **F5 — What is the dark switch called?** Options: (a) `addressTwins`, `hidden` or `shown`, the shape
  `intensity` takes; (b) a `twins` argument. `review.twin` already names the twin run
  `TOOL-dFairHearing-11` owns, a different mechanism, and a second meaning of "twin" on the harness's
  arguments would make a caller read one for the other. RESOLVED (agent, 2026-10-23, delegated): (a),
  rung 3.
- **F6 — The brief's S6 says this unit reads the items' `grades`; does it?** Nothing here grades: the
  pairs read addresses and verdicts and the flags are checked by id. RESOLVED (agent, 2026-10-23,
  delegated): no read, as `TOOL-dFairHearing-6` §8 F4 records from the owning side, by rung 3.

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, from the packet's Items 7, the review system record's twins
  shown to the synthesizer, the brief's S4 and S9, and the synthesis prompt read at base `3708a705`.

## 10. Reuse audit

The seams extended are the synthesis's prompt blocks and schema (`tools/workflows/tier2-review.template.js:1719-1937`),
`renderPromptLine` (:1619-1623) for every agent string the new blocks carry, the argument ladder
`intensity` uses (:210-217), and `TOOL-dFairHearing-4`'s `deriveAddressKey` and `checkSameAddress`,
so the address is read once in the harness. The flag check reuses the id sets the tally already builds
(:1952). `python tools/codebase-map/reuse_lookup.py "show refuted findings and same address pairs to
the review synthesizer"` ranked name stems (`pair` in `tools/memory-tree/merge-rows.test.sh`, `same`,
`check_pair` in `tools/runlog/prose.py`) and named no seam in the review harness, so the seams were
found by reading the source. `python tools/memory-recall/query.py` returned the brief's row, the
review system record's twins change and its owed replay, and the runtime comparison's twin map
(`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-runtime-reviews-compared.md:72`)
naming A59 with A38 and B61 with B43. Each agrees with source; the review system's `[debt-fold]` row
`twins-input` records that the synthesizer is not handed refuted claims today, which the synthesis
prompt at base confirms: it lists CONFIRMED and UNVERIFIED findings and refuted rows only as the
appendix's cells, which carry no claim (template :1627-1635).

Recall terms used: refuted twin confirmed same-address pair synthesizer flag appendix claim by design A59 A38
