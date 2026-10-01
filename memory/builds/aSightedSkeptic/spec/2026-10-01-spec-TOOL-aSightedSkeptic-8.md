# TOOL-aSightedSkeptic-8 — every finding keeps its lens, a findings ledger lands beside the report, and the confirmed set is returned

**Status:** SPECCED · rev-1 · 2026-10-01 · node a · Tier-2 · base ef1dcdb6 · streams tooling · order 8 · ratified 2026-10-01

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-01-prompt-TOOL-aSightedSkeptic-1-1-spec-brief.md](../prompts/2026-10-01-prompt-TOOL-aSightedSkeptic-1-1-spec-brief.md) | journal | TOOL-aSightedSkeptic-1 TOOL-aSightedSkeptic-2 TOOL-aSightedSkeptic-3 TOOL-aSightedSkeptic-4 TOOL-aSightedSkeptic-5 TOOL-aSightedSkeptic-6 TOOL-aSightedSkeptic-7 TOOL-aSightedSkeptic-9 |
| [2026-10-01-prompt-TOOL-aSightedSkeptic-8-2-build-brief.md](../prompts/2026-10-01-prompt-TOOL-aSightedSkeptic-8-2-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`tools/workflows/tier2-review.template.js` drops each finding's lens at the merge, writes no refuted
finding into any record, and returns the confirmed set as a count. Per-lens yield and recall cannot
be measured from what it leaves behind, and a fold's next round has to re-type the confirmed set by
hand. This unit carries the lens on every finding, returns a `ledger` of every finding and its
verdict, returns `confirmedFindings` in the shape `priorFindings` reads, and has the harness render an
appendix table of the ledger that the synthesis copies into the report.

## 2. Scope (IN)

- **S1** — `allFindings` is derived from `finderResults` BY INDEX: every non-null return that is not
  a skipped-lens sentinel of `TOOL-aSightedSkeptic-7` contributes its `findings` in `LENSES` order,
  each carrying `lens: LENSES[i].key`, the key the harness dispatched, never the lens string the agent
  echoed. `ref` and the id assignment are as at BASE, so ids and batch membership do not move.
  Observed by AC1.
- **S2** — Every finding line the harness writes into a prompt or a log carries `lens=<key>` after
  the bracketed grade: the verify prompt's lines, the synthesis prompt's CONFIRMED and UNVERIFIED
  lines, and the CONFIRMED and UNVERIFIED log lines on the deferred and synthesis-death paths. The
  `id=<n> [` opening stays first on each line, because the self-test's stubs read ids from it.
  Observed by AC2.
- **S3** — `ledger`, derived after the verify join, holds one entry per finding in id order with
  `id`, `lens`, `ref`, `severity` (the finder's), `skepticSeverity`, `verdict`, `reason`, `fixVerdict`
  and `claim`. Each value is read through `verdictById` by the integer id, never by `ref`.
  `skepticSeverity` is the standing verdict's `severity` when it is one of `blocker`, `high`,
  `medium` and `low`, else `null`. `verdict` is the standing verdict's `confirmed`, `refuted` or
  `uncertain`, and `unverified` when no verdict stands, either because none came back or because
  contradictory verdicts were demoted. `reason` is the standing verdict's, the literal
  `contradictory verdicts` for a demoted id, and `''` when none came back. `fixVerdict` is the
  standing verdict's when it is one of `sound`, `unsound` and `none`, else `null`. Observed by AC3.
- **S4** — `confirmedFindings` holds one entry per CONFIRMED finding in id order with `id`, `lens`,
  `ref`, `claim`, `severity`, `fix` and `fixVerdict`. `severity` is the binding grade
  `TOOL-aSightedSkeptic-6`'s `deriveBindingSeverity(f)` returns. `fix` is the skeptic's `fixNote`
  when `fixVerdict` is `unsound` and the note is not empty, else the finder's `fix`, so a rejected
  fix is never handed to the next round. The entry is a legal `priorFindings` element as it stands.
  Observed by AC4.
- **S5** — Every return carries `ledger`, `confirmedFindings` and `appendix`, on every exit path. The
  two paths that exit before the verify stage, every lens dead and no finding raised, carry `[]`,
  `[]` and `''`. The every-finding-refuted path carries the full ledger, an empty
  `confirmedFindings` and the rendered appendix. The deferred paths carry what was judged so far, and
  their `exit` already says it is partial. The existing `confirmed` field keeps its type on every path:
  an array on the three early returns, an integer on the partial-deferred and success returns.
  Observed by AC6.
- **S6** — `renderAppendix(ledger)` returns the markdown table: the heading
  `## Appendix — every finding`, a blank line, a header row with the eight columns
  `id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict` in that order, the
  separator row, and one row per ledger entry in id order. `renderCell(v)` writes each cell: `null`
  and `''` as `-`, every `|` as `\|`, and each run of CR or LF as one space. It is rendered once,
  after the verify stage, from the same `ledger` the return carries. Observed by AC5.
- **S7** — The synthesis prompt hands the appendix to the agent and tells it to append it VERBATIM as
  the report's last section, after everything else and unedited. The harness does not verify the copy
  (§8 F2); the return's `appendix` holds the exact text, so a caller holding a filesystem can compare
  it with the report. Observed by AC5.
- **S8** — `tools/workflows/README.md` documents the three new return fields, the eight appendix
  columns, that a refuted finding reaches a record only through the appendix, and that the
  every-finding-refuted path writes no report, so there the appendix exists in the return alone.
  Observed by AC8.
- **S9** — The arms of §6 are written into `tools/workflows/tier2-review.test.sh`, each observed RED
  against the pre-change script, and its `FLOOR_ASSERTIONS` rises by the number of assertions this
  unit adds. The suite is not run in the pass. Observed by AC1, AC2, AC3, AC4, AC5, AC6.

## 3. Non-goals (OUT)

- A synthesis on the every-finding-refuted path, so that its ledger reaches a record file. §8 F3.
- Verifying that the synthesis copied the appendix. §8 F2.
- Scoring recall. `TOOL-aSightedSkeptic-9` reads the appendix this unit renders.
- A per-lens yield summary line or table. The ledger carries every value it would be derived from.
- Changing `confirmed`, `blockers`, `highs`, `unverified` or any other existing return field;
  `tools/workflows/unattended-build.js` reads them, and it is not edited.
- A `claim` column in the appendix. The claim rides the returned ledger only (§8 F4).
- `REVIEW_SHAPE`, the kit version, `MAX_VERIFIERS` and `tools/hooks/agent-cap.js`.
- Any governance carrier. M8's invocation block in `memory/guides/BUILD-METHOD.md` does not show that
  `confirmedFindings` is what round N+1's `priorFindings` should be; the main loop parks that wording
  for the owner.

### Edges

- **consumes-from** `TOOL-aSightedSkeptic-5` — the five lens keys every finding's `lens` is one of.
- **consumes-from** `TOOL-aSightedSkeptic-2` — `fixVerdict` and `fixNote` on the verdict item, which
  S3 and S4 read; without them both are `null` and `fix` is the finder's.
- **consumes-from** `TOOL-aSightedSkeptic-6` — the verdict's `severity`, the `uncertain` verdict held
  in the join, and `deriveBindingSeverity(f)`; without them `skepticSeverity` is always `null` and
  `confirmedFindings` cannot name a binding grade.
- **consumes-from** `TOOL-aSightedSkeptic-7` — the skipped-lens sentinel S1 passes over, and the
  `intensity` and `skippedLenses` fields on the same returns S5 extends.
- **hands-off** `TOOL-aSightedSkeptic-9` — the appendix table S6 pins: its heading, its eight columns
  in order, `ref` spelled `<file>:<line>` for a diff review, and `-` for an absent value.
- **hands-off** external — M8's invocation wording, and any record of an every-finding-refuted run,
  which the caller may write from the returned `appendix`.

## 4. Design

### Evidence

Read at `ef1dcdb6` on 2026-10-01, PINNED to that sha; the render `tools/workflows/tier2-review.js`
equals the template after `{{FANOUT_CAP}}` is substituted with 5, measured by the AC7 `sed | diff`.

- `allFindings` flattens `liveResults` with `flatMap` and carries no lens (template lines 536-538);
  `liveResults` is `finderResults.filter(Boolean)` (line 528), which loses the index that names the
  lens. The finder schema carries `lens` at the top level only (lines 238-261).
- The verify prompt line is `id=${f.id} [${f.severity}] ${f.ref} — ${f.claim} | impact: ...`
  (line 612); the synthesis CONFIRMED and UNVERIFIED lines open the same way (lines 733 and 740).
  The self-test's stubs read ids with `/ids ([0-9, ]+)\)/` and `/id=(\d+) \[/g`
  (`tools/workflows/tier2-review.test.sh` lines 191 and 198).
- Refuted findings are counted (line 657) and never written into a prompt, so no record carries one.
- The returns carry `confirmed: []` at lines 551, 568 and 693, and `confirmed: confirmed.length` at
  lines 715 and 925. `tools/workflows/unattended-build.js:940` reads `Array.isArray(auRaw.confirmed)`
  and `:960` reads `Number.isInteger(auRaw.confirmed)`, so the field's per-path type is a contract.
- `priorFindings` is read as `f.ref` and `f.claim || f.title` (line 505), and joins `inputPrint`
  (line 396), so extra fields on a passed entry change the next round's key and nothing else.
- Past review records already carry other appendix headings, for example
  `memory/builds/aScouredKit/reviews/2026-08-30-review-TOOL-aScouredKit-1-wave1-report.md`'s
  `## Appendix — counts, precision, and what precision does NOT mean`. The S6 heading is the full
  literal, so a reader keying on it does not match those.

### Data model

```
finding (in memory)  + lens: string            the dispatch key, LENSES[i].key
ledger[]             { id, lens, ref, severity, skepticSeverity, verdict, reason, fixVerdict, claim }
  verdict            'confirmed' | 'refuted' | 'uncertain' | 'unverified'
  skepticSeverity    'blocker' | 'high' | 'medium' | 'low' | null
  fixVerdict         'sound' | 'unsound' | 'none' | null
confirmedFindings[]  { id, lens, ref, claim, severity, fix, fixVerdict }
appendix             string; '' when the ledger is empty
```

### Spellings

```
## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict |
|---|---|---|---|---|---|---|---|
| 1 | correctness | a.js:12 | high | medium | confirmed | reachable from run() | unsound |
| 2 | security | b.js:3 | medium | - | refuted | not reachable \| guarded at caller | - |
```

### Inventory

Minted functions, each answered `OK` by `python tools/lexicon/lexicon.py --suggest <name> --as
js.function` on 2026-10-01: `renderAppendix` and `renderCell`, both in the `js.function` cell. Minted
data: `ledger`, `confirmedFindings`, `appendix`, and the `lens` field on a finding.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js` (the render, regenerated in the same commit)
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/README.md`

### Rollout

Additive: three new return fields and a new last section in the report. No caller reads them today.
The prompts change, which `REVIEW_SHAPE` already accounts for once for the build.

### Alternatives rejected

- **Read the lens from the agent's echoed `lens` field.** A live agent can misspell it, and a reused
  file is already matched on it; the dispatch index cannot drift.
- **Key the ledger on `ref`.** That is the retired join `tools/hooks/agent-cap.js` bans, and two
  findings at one `file:line` would collapse into one row.
- **Have the synthesis compose the appendix from the lines it is shown.** Refuted findings are not
  shown to it, and a table an agent writes from prose is the copy that drifts.

## 5. Production-readiness checklist

- security — N/A: no new input reaches a shell or a path; the cells are escaped so a claim or reason
  carrying `|` cannot forge a row in the record a later tool parses.
- perf / scale — one pass over the findings after the verify stage, and one table string; the
  synthesis prompt grows by one row per finding.
- error / empty / loading states — an empty ledger renders an empty appendix and the prompt carries
  no appendix instruction; a missing optional verdict field renders `-` and is `null` in the ledger.
- observability — the ledger and the appendix are the observability this unit adds.
- risks — the synthesis may truncate or edit the appendix. The harness cannot see the report, so it
  says so in §7, and the return carries the true text for a caller to compare.
- testing — the §6 arms in `tools/workflows/tier2-review.test.sh`, each observed RED against the
  pre-change script; the suite runs once, at VERIFYING.
- migration — none: every field is new.
- user docs — `tools/workflows/README.md` (S8).

## 6. Acceptance criteria

- **AC1** — Arm `ledger: every finding carries its dispatching lens` passes: a complete run's
  `ledger` holds five entries, each `lens` the key whose stub wrote its `<lens>.js` file; a lens stub
  that echoes `lens: 'bogus'` still yields its dispatch key; and a run whose every lens file is
  reused from the probe yields the same lenses.
  Red when: the merge drops the lens, or reads the agent's echo.
- **AC2** — Arm `ledger: the skeptic and synthesis lines name the lens` passes: every `verify:`
  prompt carries `lens=<key>` on each finding's line, the `synth` prompt's CONFIRMED lines do, and
  each line still opens `id=<n> [`.
  Red when: either prompt omits the lens, or the stub id pattern stops matching.
- **AC3** — Arm `ledger: every verdict state reaches the ledger` passes: with stubs answering id 1
  `refuted` with reason `r1`, id 2 `uncertain`, id 3 nothing, id 4 two contradictory verdicts and
  id 5 `confirmed` with `severity` `low` and `fixVerdict` `unsound`, the ledger's verdicts read
  `refuted`, `uncertain`, `unverified`, `unverified` and `confirmed`; id 1's reason is `r1`, id 4's is
  `contradictory verdicts`, id 5's `skepticSeverity` is `low` and `fixVerdict` `unsound`, and the
  absent fields read `null`.
  Red when: any state is folded into another, or a refuted finding is missing from the ledger.
- **AC4** — Arm `ledger: confirmedFindings feeds the next round` passes: a complete run's
  `confirmedFindings` has as many entries as its `confirmed` count, each carrying `ref`, `claim`,
  `severity` and `fix`; a confirmed finding whose verdict carries `fixVerdict` `unsound` and
  `fixNote` `better fix` returns `fix` `better fix`; and a round-2 run given that array as
  `priorFindings` carries each `<ref> - <claim>` in every `find:` prompt.
  Red when: the return carries only a count, or a rejected fix is handed to the next round.
- **AC5** — Arm `ledger: the appendix is rendered by the harness and handed to the synthesis`
  passes: the result's `appendix` opens with `## Appendix — every finding`, carries the eight-column
  header in order and one row per ledger entry, refuted ones included; the `synth` prompt contains
  that text verbatim; and a finding whose claim and reason carry `|` and a newline leaves the row
  count unchanged.
  Red when: a refuted finding has no row, an unescaped pipe splits a row, or the synthesis is not
  handed the table.
- **AC6** — Arm `ledger: every exit path carries the ledger` passes over six runs: every lens dead,
  no finding raised, every finding refuted, one skeptic batch dead, the synthesis dead, and complete.
  Each returns `ledger` and `confirmedFindings` as arrays and `appendix` as a string; the refuted
  run's ledger lists every finding `refuted` beside an empty `confirmedFindings`; and `confirmed` is
  an array on the first three and an integer on the last three.
  Red when: a path omits a field, or `confirmed` changes type on any path.
- **AC7** — When `bash tools/workflows/check-review-join.sh`,
  `bash tools/workflows/check-verifier-fanout.sh` and `node tools/workflows/check-workflow-syntax.js`
  run, each exits 0;
  `sed 's/{{FANOUT_CAP}}/5/g' tools/workflows/tier2-review.template.js | diff - tools/workflows/tier2-review.js`
  prints nothing; and `python tools/lexicon/lexicon.py --suggest renderAppendix --as js.function`
  and the same for `renderCell` each print a line opening `OK`.
  Red when: the ledger joins on `ref` and the join gate reds, or the render was not regenerated.
- **AC8** — When `grep -c 'confirmedFindings' tools/workflows/README.md` runs it prints at least 1,
  where BASE prints 0.
  Red when: the new return fields are documented nowhere a caller reads.

## 7. Gates

`workflow script syntax` · `verifier fan-out` · `verifier fan-out self-test` · `review-join ban (no ref-keyed join)` · `review-join self-test` · `review-protocol parity (kit vs dogfood)` · `tier2-review self-test` · `unattended-build self-test` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `memory hygiene`

New arm: `tools/workflows/tier2-review.test.sh` · the six arm groups of AC1 to AC6, whole-script over stub agents, each staged RED on the pre-change script · `FLOOR_ASSERTIONS` raised by the assertions added

What no gate here can see: whether the synthesis agent copied the appendix into the report. The
harness has no filesystem and the stubs return what they are given; the return's `appendix` is the
text a caller compares against the written report, and `TOOL-aSightedSkeptic-9`'s scorer refuses a
record whose table it cannot parse.

## 8. Open questions

- **F1 — Where does a finding's lens come from?** (a) The dispatch key, `LENSES[i].key`, by index.
  (b) The top-level `lens` string the agent returned. (b) is a model's echo of its own label, and a
  misspelt echo would mislabel every finding of that lens with nothing to catch it. Recommendation
  (a). RESOLVED (agent, 2026-10-01, delegated): (a), the source that cannot drift.
- **F2 — What can the harness verify about the synthesis's copy of the appendix?** (a) Nothing, and
  §7 says so. (b) Require the synthesis to return the number of rows it wrote and compare it with the
  ledger. (c) Return the rendered appendix so a caller with a filesystem can compare it with the
  report. (b) is a self-report of the number the prompt asked for, a check that cannot fail on the
  defect it targets. (c) costs one return field and makes the copy checkable outside the harness.
  Recommendation (a) with (c). RESOLVED (agent, 2026-10-01, delegated): (a) with (c); (b) is
  rejected as a check that cannot fail.
- **F3 — Does the every-finding-refuted path run a synthesis so its ledger reaches a record?**
  (a) No; the path returns the ledger and the appendix and writes no report, as at BASE. (b) Yes.
  (b) changes a return contract `tools/workflows/unattended-build.js:940` reads to call a spec-audit
  round clean, which needs an edit outside this unit's harness and a new agent on a path the build
  harness treats as finished. Recommendation (a). RESOLVED (agent, 2026-10-01, delegated): (a); the
  caller may write the returned appendix itself.
- **F4 — Which columns does the appendix carry?** (a) Exactly the eight ledger fields the shared
  brief pins, in its order. (b) Those eight plus `claim`. The table is the join surface
  `TOOL-aSightedSkeptic-9` parses, written concurrently against the brief's eight, and a free-text
  claim is the cell most likely to break a row. Recommendation (a). RESOLVED (agent, 2026-10-01,
  delegated): (a); the claim rides the returned `ledger`.

## 9. Revision log

- rev-1 · 2026-10-01 · initial draft, from the owner's mandate, the build's spec brief, the harness
  template and its self-test read at `ef1dcdb6`, and the sibling specs of units 2, 5, 6 and 7 as
  authored in this run.

## 10. Reuse audit

The probe `python tools/codebase-map/reuse_lookup.py "carry each review finding's lens and verdict
into a ledger table appended to the report"` returned name-stem neighbours only, `report`,
`render_report`, `scan_verdicts`, all in Python kits outside `tools/workflows/`, and it reports
`unscanned layers: .sh`. No existing seam fits outside the harness, so the seams extended are its
own, read at source: the `allFindings` merge (template lines 536-538), the integer-keyed
`verdictById` join (lines 641-656) that S3 reads, the synthesis prompt (lines 726-823) that S7
extends, and the return objects at lines 548, 566, 689, 713 and 917. The recall query put
`TOOL-dTieredTribunal-16` and the run mandate's measurement-gap paragraph at the top: the first is
the precedent that a count logged to stdout is not a record, which is why the appendix goes into the
report rather than the log. No record of a findings ledger built or refused before was found.

Recall terms used: `python tools/memory-recall/query.py "where are refuted review findings and per-lens yield recorded so recall and precision can be measured" --terms "tier2-review ledger refuted findings lens label confirmed set priorFindings appendix recall precision measurement report"`
