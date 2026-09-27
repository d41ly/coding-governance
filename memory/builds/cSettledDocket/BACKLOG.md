# cSettledDocket — asks

## Asks

- KICK-cSettledDocket-1 · filed 2026-08-16 · builds/aHonedRuleset/ · the manifest stamp rule could not satisfy its own check 5 on a feature branch: merge-base PREDATES any watched file the branch changed, so check 5 failed until you stamped HEAD. Cost 3 attempts. Fixed: the rule is now `HEAD on any branch`
- TOOL-cSettledDocket-7 · filed 2026-08-17 · `tools/memory-recall/recall-opened.test.sh` is tracked and NO gate leg runs it, so `check-testsuite-counts` cannot see it. A suite nobody runs is one nobody notices going quiet — wire it or record why not
- TOOL-cSettledDocket-8 · filed 2026-08-17 · `DIRECTIVES_EXTRA_TABLE` has one reader, check 16. Unit 2's 'shown to the agent' half is unmet: the rendered Skill does not point at the project's table, so a declared extra is joined but never displayed
- TOOL-cSettledDocket-9 · filed 2026-08-17 · a terminal spec whose Open-questions section is present but EMPTY stays silent: the `q == 0` refusal fires only when the range never opens. Present-and-empty still reads as resolved
- TOOL-cSettledDocket-10 · filed 2026-08-17 · `check-testsuite-counts` says 'every bar self-test' and grades only `*.test.sh`; eleven python self-tests on the manifest are out of population. Widen the selector or narrow the sentence
- TOOL-cSettledDocket-11 · filed 2026-08-17 · check 8 exempts a TERMINAL record by clearing `rd`, skipping the malformed-MARKER refusal as well as the emptiness one — the over-wide scoping cBriefedPilot-36 shipped. Scope it to emptiness alone
- TOOL-cSettledDocket-12 · filed 2026-08-17 · `tools/lexicon/selftest.py` failed the bar on a `shutil.rmtree` traceback and passed on re-run — a Windows temp-dir race, not a defect
- TOOL-cSettledDocket-13 · filed 2026-08-17 · `unattended.test.sh` loops the verb set across three carriers, all inside the driver, so a verb no agent is told about is invisible to it — that gap shipped `--park` as a blocker
- TOOL-cSettledDocket-14 · filed 2026-08-17 · the same gate on the conf axis: every key the engine READS must appear in the protocol's key table and the shipped conf example. `DIRECTIVES_EXTRA_TABLE` landed with one reader and no catalogue entry
- TOOL-cSettledDocket-15 · filed 2026-08-17 · citing a non-terminal spec id from product source has red the bar three times; the remedy (paraphrase, never cite) is recorded and nothing enforces it
- TOOL-cSettledDocket-16 · filed 2026-08-17 · the TOOL index was at its 20480-byte cap with nothing terminal left to rotate, so new rows were paid for by shortening old ones. Closed by TOOL-aRelaxedShard-1: the bound is now a declared 61440 and the index sits at 33%

## Dispositions

- CLOSED · KICK-cSettledDocket-1 · by 42163e645a2a65792a72296dc895e6a5997bc833 · builds/aHonedRuleset/ · the manifest stamp rule could not satisfy its own check 5 on a feature branch: merge-base PREDATES any watched file the branch changed, so check 5 failed until you stamped HEAD. Cost 3 attempts. Fixed: the rule is now `HEAD on any branch`
- CLOSED · TOOL-cSettledDocket-16 · by TOOL-aRelaxedShard-1 · the TOOL index was at its 20480-byte cap with nothing terminal left to rotate, so new rows were paid for by shortening old ones. Closed by TOOL-aRelaxedShard-1: the bound is now a declared 61440 and the index sits at 33%
