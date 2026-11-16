**Serves:** research TOOL-aMeasuredDrag-1

# Synthesis brief — the adversarial performance review of gov and its adopters

## What happened

The owner asked for an extensive adversarial review of the whole project, because gov and the repos that adopt it (incms, nicocares) deliver work extremely slowly under gov's governance. Twelve researcher lenses found about 110 findings, and five skeptic batches tried to refute every one at base `aebbb4a72`. Read these files, all beside this one in `memory/builds/aMeasuredDrag/build/`:

- `2026-11-15-build-TOOL-aMeasuredDrag-1-evidence.md` — the measured starting evidence
- `2026-11-15-build-TOOL-aMeasuredDrag-1-findings-gate.md` — githooks, legs, bar
- `2026-11-15-build-TOOL-aMeasuredDrag-1-findings-hooks.md` — session hooks, spawns
- `2026-11-15-build-TOOL-aMeasuredDrag-1-findings-records.md` — records, derived indexes, suites
- `2026-11-15-build-TOOL-aMeasuredDrag-1-findings-pipeline.md` and `...-findings-process.md` — pipeline, ceremony, contention
- `2026-11-15-build-TOOL-aMeasuredDrag-1-findings-adopters.md` — adopters
- `2026-11-15-build-TOOL-aMeasuredDrag-1-verdicts.md` — every skeptic verdict, corrected cost, prior fix and duplicate list

One more measured fact the lenses could not see, from this review's own session: the inline review workflow was refused by agent-cap rule 6. The governed route (an owner question, a build folder, one rendered handoff per agent, the main loop re-emitting each prompt byte for byte) took about 6 minutes before the first agent ran. That route then rendered 17 handoffs, about 3 KB each, of which about 1.5 KB is the same practices block. PINNED 2026-11-15

## What to write

Write ONE review record, `memory/builds/aMeasuredDrag/reviews/2026-11-15-review-TOOL-aMeasuredDrag-1-performance.md`, opening with `**Serves:** research TOOL-aMeasuredDrag-1`. Drop every REFUTED finding. Merge duplicates, citing every merged id. Always use the skeptic's corrected cost, never the finder's. Do not add hours that overlap: the same commit hook, bar or walk counts once. Sections:

1. **Diagnosis** — one paragraph naming the 4-6 systemic root causes behind most of the slowness, each tied to finding ids. Name the class, not the instance. Candidates the evidence supports (confirm or reject each): whole-tree work on every event (commit, bar, Stop, session) with no incremental cache; one unit of work paying the bar about 5 times, plus CI that is red on every run; ceremony scaled to Tier-2 for ~95% of units (spec tokens over build tokens, minors promoted to units, records commits at 3 per product commit); host contention, where a one-slot turnstile serialises bars while pass runs and suites bypass it, so legs time out, retry and get their ceilings raised; adopters frozen on an old kit vintage, paying for slowness gov already fixed; each speed fix being itself a full Tier-2 build (aTrimmedWait: 9 units plus 2 repair units). PINNED 2026-11-15
2. **Where a unit's wall-clock goes** — a small table for a typical one-unit landing (aBriskDeclaration: 5h57m end to end vs 28 min of builder time). Rows: orchestration verbs, spec and review ceremony, records commits and hooks, bar runs, queue and contention, owner turns, building. Give the arithmetic and a confidence for each row.
3. **Ranked findings** — one table, highest corrected weekly cost first: ids · title · verdict · corrected weekly cost · payer · fix · effort · what the fix trades.
4. **Quick wins** — S effort, CONFIRMED, decision-preserving (no verdict moves), as a short list with the file:line to change.
5. **Structural changes** — M/L changes that remove whole classes of cost, each naming the guarantee it trades and the owner ruling it would reverse, if any (for example BUILD-METHOD.md:144 on promoting minors).
6. **What adopters pay without benefit.**
7. **Already fixed or in flight** — what main or branch/speedups-9c2e63 already addresses, so nobody rebuilds it.
8. **Gaps** — what no lens or skeptic could measure, said plainly.

Be blunt and factual. Every figure carries its source. Return the report's path, the number of items adjudicated, and the top five items with their corrected weekly costs.
