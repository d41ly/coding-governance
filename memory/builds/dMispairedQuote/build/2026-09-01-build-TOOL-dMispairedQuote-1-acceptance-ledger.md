# The acceptance ledger for the two code units

**Serves:** journal TOOL-dMispairedQuote-1 TOOL-dMispairedQuote-3

Every observation below was made in this worktree against the built tree. The suite reports
150 passed / 0 failed; the property arm reports population 1273, 48 denied at BASE, 0 lost.

**Evidences:** TOOL-dMispairedQuote-1

- AC1 — `bash tools/hooks/agent-cap.test.sh` arm `mispaired quote: SAME LINE is the load-bearing part` — the reported probe exits 2; it exited 0 at BASE, recorded in `2026-09-01-red-TOOL-dMispairedQuote-1.txt`
- AC2 — `bash tools/hooks/agent-cap.test.sh` arms `apostrophe in a DOUBLE-quoted string`, `in a BLOCK COMMENT`, `in a TEMPLATE literal`, `LOOSE apostrophe opening a word` — all four exit 2, all four exited 0 at BASE
- AC3 — `bash tools/hooks/agent-cap.test.sh` arm `rule 2 counter loses the agent(` — exits 2 with its no-apostrophe control beside it
- AC4 — `bash tools/hooks/agent-cap.test.sh` arms `rule 3 loses a declared cap of 50` and `rule 3, an unpaired double quote swallows the bound` — both exit 2
- AC5 — `bash tools/hooks/agent-cap.test.sh` arms `a legal log() with a contraction in its trailing comment` (exit 0) and the `B26` admit half, measured DENY under the rev-1 design and DENY here
- AC6 — `bash tools/hooks/agent-cap.test.sh` arm `aLexedStripper-5's own fixture stays legal` — exit 0 before and after
- AC7 — `bash tools/hooks/agent-cap.test.sh` — 150 passed, 0 failed, against 105 at BASE
- AC8 — `memory/builds/dMispairedQuote/build/2026-09-01-red-TOOL-dMispairedQuote-1.txt` — 15 arms FAILED against the tip without the fix; every ADMIT-direction arm and every control passed there
- AC9 — `diff .claude/hooks/agent-cap.js tools/hooks/agent-cap.js` is empty, and the suite's two-copy parity arm passes
- AC10 — `bash tools/check-kit-versions.sh` exits 0 with all four `gov:kit agent-cap@1.10` carriers agreeing
- AC11 — `python tools/lexicon/lexicon.py --check` reports `P1 verb graded=1032 offenders=461`, under the pin, and `--suggest` answers OK for both names
- AC12 — `bash tools/hooks/agent-cap.test.sh` keyword sweep — one arm per member of `LITERAL_OPENERS` plus the three dropped connectives, every verdict recorded; eleven admit as the stated residual, the three connectives deny

**Evidences:** TOOL-dMispairedQuote-3

- AC1 — `bash tools/hooks/agent-cap.test.sh` arm `no-regress: a backtick inside a regex, above a multi-line cap-50 call` — exit 2; exit 0 with unit 1 alone, recorded in `2026-09-01-red-TOOL-dMispairedQuote-3.txt`
- AC2 — `bash tools/hooks/agent-cap.test.sh` arm `no-regress: an exposed backtick leaks the template mode` — exit 2, and the regex-borne `)` shape reproduced at exit 0 without this unit
- AC3 — `bash tools/hooks/agent-cap.test.sh` arm `no-regress: a quoted URL inside a same-line template` — exit 2
- AC4 — `bash tools/hooks/agent-cap.test.sh` arm `no-regress: no denial lost against BASE` — the rule-2 shape is inside its population and inside `2026-09-01-red-TOOL-dMispairedQuote-3.txt`, which names the lost denials without this unit
- AC5 — amended rev-6 — the rule-5 arms landed in unit 1's block (`rule 5 join hidden by an apostrophe`, `rule 5 verdictByRef hidden by an apostrophe`, plus a control), because the apostrophe defeats rule 5 at BASE and that is unit 1's mechanism, not this unit's. `--only=join` was verified to still select that rule alone. Logged in section 9.
- AC6 — `bash tools/hooks/agent-cap.test.sh` arm `no-regress: no denial lost against BASE` — population 1273, 48 denied at BASE, 0 lost; the same arm names three lost denials when run against unit 1 alone
- AC7 — `bash tools/hooks/agent-cap.test.sh` arm `no-regress: the three renderShipped* bodies are the BASE bytes`
- AC8 — `bash tools/hooks/agent-cap.test.sh` — 150 passed, strictly above the 140 the same suite reported with unit 1 alone
- AC9 — `python tools/lexicon/lexicon.py --check` reports `offenders=461`, below the 463 measured at BASE, and `.lexicon.conf` now pins `461`
- AC10 — `memory/builds/dMispairedQuote/build/2026-09-01-red-TOOL-dMispairedQuote-3.txt` — all six arms FAILED against unit 1 alone, the property arm and the byte arm included
- AC11 — the arm prints `skip no-regress byte arm — <sha>:<derived path> does not resolve in this tree`; the path is derived with `git ls-files --full-name` rather than spelled, which is what `bash tools/check-install-prefix.sh` refuses
- AC12 — `grep -nE '(^|[^A-Za-z0-9_$])(stripStrings|blankLiterals)\s*[(=]' tools/hooks/agent-cap.js` reports nothing; both tokens survive only in comments, which AC7's byte freeze requires

## What the closing review changed after these were first observed

Three folds, each re-verified above rather than assumed: `checkLiteralOpen` became a backward
identifier walk (8000 literals on one line: 33.8 s to 83 ms, and a hook that times out does not
block); `runBothViews` isolates both passes and DENIES when neither can scan; and the property arm
scores admission as `exit != 2` rather than `exit == 0`, which is what the hook actually does.
