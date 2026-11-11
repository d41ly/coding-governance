# Fix brief — TOOL-dFairHearing-1: where replays 3 and 4 take each finding's text from

**Serves:** research TOOL-dFairHearing-1

## The prompt

> /unattended dFairHearing

— owner, 2026-11-02, the invocation that started this build run.

## The brief

### Goal
Revise `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-1.md` so replays 3 and 4 can be built from committed records. The builder's second return is `memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-1-2-builder-return.md`; read it first. Commit nothing; the main loop commits.

### Items
1. §8, a new fork in the template's shape: where a finding's claim, impact, fix and evidence come from for replays 3 and 4, given the runtime-a and runtime-b appendices carry none and the runs' find and verify files are gone. Options: (a) a confirmed finding's text from the report item that holds its id, a refuted finding's from its appendix `reason`, aRoutedQuill #23's from its round-1 item; the stand-in recorded as a departure; (b) re-run the find stage on a clone; (c) judge flags from the SAME-ADDRESS PAIRS block alone, restating AC7. Resolve it `RESOLVED (agent, 2026-11-03, delegated)` as (a), with M3's reason: (b) yields new findings, so the ids A59, A38, B61, B43 that AC7 names would not exist and AC7 fails; (c) fails AC7's negative-pair half as written, since claims are what tell two defects apart; both fall to veto 1. Carry `widens:` and `relaxes:` as README rule 5 requires; the stand-in relaxes what the replay tests (a synthesizer sees report prose, not finder returns), so `relaxes:` names that and a deviation record is owed — name its path in §4 Files touched.
2. Write (a) into §4 "The other three replays" (Twins and Fix verdict) and S7 and S8: the exact source of each field, and that the harness's own render functions format them (`id=N [sev] lens=… <ref> — <claim> | impact: … | fix: …` and the REFUTED block). Where a field has no source (impact or fix for a refuted finding), say what stands in, or that it is left empty.
3. Record replay 2's measured result as data, not a change: the builder's deterministic probe gave 0 of 8 twins sharing a batch under `id` and 4 of 8 under `address`, with A59 and A38 split at a batch boundary. Do not alter S6's bar; pass (b) records the verdict.
4. Rev bump and one §9 line per change, naming this brief. Leave the status header's state as it is.

### Acceptance
The spec at its next rev names a committed source for every field replays 3 and 4 render, with §8's mark and the deviation record in §4.

### Gates
None you run.

### Non-goals
No change to replay 1 (unit 25's), to the bars, or to the two-pass split. No other spec, no code.
