# Brief — aClearedLedger: the nine asks aNimbleMend's close left open

**Serves:** research TOOL-aClearedLedger-1 TOOL-aClearedLedger-2 TOOL-aClearedLedger-3 TOOL-aClearedLedger-4 TOOL-aClearedLedger-5 TOOL-aClearedLedger-6 TOOL-aClearedLedger-7 TOOL-aClearedLedger-8 TOOL-aClearedLedger-9 TOOL-aClearedLedger-10

## The prompt

> Work through the open asks TOOL-aNimbleMend-16 to TOOL-aNimbleMend-26 in `memory/builds/aNimbleMend/BACKLOG.md` (ask 27 was a unit and 28 is out of scope). Read each ask's row first: it carries the `seen … run … accept …` probe that defines done.
>
> Start with `/session-kickoff`, on a fresh branch from origin/main. This is a new build with its own slug and build folder, not more units of aNimbleMend; follow `memory/guides/BUILD-METHOD.md` for specs, builders and the closing review.
>
> 1. Ask 24 first, because it needs the owner: present the two sentences, the options for each, and your recommendation, and ASK the owner to rule on each separately (the owner wants each fork asked on its own). Then write the ruling into the carrier that states it (the charter's `[spec]` practice changes only at its source, the practice catalogue, never in `AGENTS.md` text; the protocol sentence in `tools/unattended/PROTOCOL.template.md`), and close the ask.
> 2. Asks 25 and 26: verify on origin/main's tip that `python3 tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . ':!*.test.sh' ':!memory/'` exits 0 and `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt .` prints `0 red`, then dispose of both asks as cured by TOOL-aNimbleMend-27, in the backlog's own disposition grammar (`memory/HYGIENE.md`).
> 3. Asks 16, 17, 18, 19, 20: for each, reproduce the red with the ask's `run` command, find the cause (a stale fixture or parity list is likely for 16, 18 and 20; the write gate's refusal text or its arms for 17; the conf example and check 26's cache for 19), fix it at the cause, and show the ask's `accept` line holding. Do not raise a floor or waive an arm to make a suite pass.
> 4. Ask 21: find why `ALFORM` is unbound under `--staged` in `tools/memory-tree/check-memory-hygiene.sh`, whether a check ends early with no verdict because of it, and fix it with an arm that reds on the old behaviour.
> 5. Ask 22: re-measure the four suites ALONE on a quiet node (unattended-build self-test, run-gates canary, run-gates evidence, hygiene self-test), rewrite their rows in `tools/run-gates/selftest-budgets.txt` at the file's stated margin, then run `GOV_NODE=a python tools/run-gates/derive-ceilings.py --write --observed "<leg>=<seconds>" --how "<text>"` and `python tools/run-gates/pass_legs.py --apply`; a moved `tools/gate-legs.json` owes a `last-audit` re-stamp of `memory/guides/SESSION-KICKOFF.md` in the same commit.
> 6. Ask 23: decide what a path-less `Red-fix:` commit owes (the door or the join must say), implement it, and add a plant case under `python tools/memory-tree/build_records.py --fixture --plant red-fix-join`.
>
> Done means: each of the eleven asks is either closed with its `accept` observation recorded, or parked with the reason it could not be closed; every new or changed gate arm was seen red and then green; the build's bar is green; and the work is landed on main through `bash tools/push-main.sh` ONLY after the owner says to merge and push. Report anything you could not verify.

## The brief

### Goal
Close asks TOOL-aNimbleMend-16 to TOOL-aNimbleMend-24, each at its cause, as ten units of one build. Asks 25 and 26 need no unit: the main loop verified both legs green at `8db6f4bef` and disposed of them in this build's `BACKLOG.md`.

### Items
1. Unit 1, ask 24, first sentence. The owner ruled: the `[spec]` practice gains an exception for an inline red fix. Write it at the source, `tools/playbook/practices.toml`, as a clause of the one-line rule saying an inline red fix under `bar.inline-red-fixes` commits no spec and owes its typed record; re-render `AGENTS.md`, the template where it carries the line, and the role agents under `.claude/agents/`. The line stays one line and inside the template's size cap.
2. Unit 2, ask 24, second sentence. The owner ruled: the fix's record stays the next commit. `tools/unattended/PROTOCOL.template.md` section 12, the paragraph opening `Two switches act BETWEEN passes`, gains the reason: the record names its fix commit's sha, so it cannot ride that commit. Re-render the protocol's rendered copy.
3. Unit 3, ask 16. `bash tools/unattended/gate-guard.test.sh` prints two FAIL lines opening `parity:`. Its parity arm feeds every `chunk = selftests` argv of `tools/gate-legs.json` to the hook's predicate in `tools/unattended/gate-guard.js`. The legs it reports: four of the form `python {prefix}/playbook/core.py fixture` and `python {prefix}/policy/check_policy.py --fixture …`, which no deny row matches, and two `--selftest` legs whose ceilings rose past the 300 s bound, `routed_commits.py` at 660 s and `measure_legs.py` at 500 s. (PINNED, 2026-11-13) Find the cause and fix it there: the hook denies what the manifest declares a suite, or the arm's rule is wrong, and the spec says which and why. No exemption is added to make the arm pass.
4. Unit 4, ask 17. `bash tools/hooks/scratch-guard.test.sh` prints seven FAIL lines, `S-AC2` twice, `S-AC3` twice, `S-AC5` once, `S-AC8` twice. Each says the refusal's context is three lines where the arm wants one, or is not byte-identical to the bare one, and the `S-AC5` line shows the last line reading `[/.claude/orientation-card.md]`: the context now carries an instruction envelope's opening and closing lines. Find which landing wrapped it, and fix the side that is wrong: the arms where the envelope is intended, the refusal where it is not.
5. Unit 5, ask 18. `bash tools/check-spec-tokens.test.sh` prints `arm FAIL  parity: a manifest suite invocation BAR does not match`, naming the three playbook `fixture` legs and `routed_commits.py --selftest` at ceiling 660 s, then `graded 57 + exempt 16 != the manifest's 74`. (PINNED, 2026-11-13) The matcher is `BAR` in `tools/check-spec-tokens.py`. Same class as unit 3, a second reader; fix this reader at its cause.
6. Unit 6, ask 19. `bash tools/memory-tree/check-memory-hygiene.test.sh` prints eight FAIL lines: the scoped runs do not partition the unscoped run's lines on a `cache hits` figure of check 26, the conf example does not declare `OSTYPE`, and it does not declare six `RECALL_` keys a module reads. The suite must exit 0 and print its assertion total.
7. Unit 7, ask 20. `python tools/policy/check_policy.py --fixture` prints 33 wrong: guard-census and guard-trace rows for playbook files, `tools/memory-tree/id_grammar.py` and `tools/govkit/upgrade_steps.py` that the leg's guard in `tools/gate-legs.json` does not name, one `budgets-reader-refused` row, and three `budgets-cap-recall-export` rows. The leg must print `0 wrong`. A changed manifest owes `python tools/run-gates/pass_legs.py --apply`.
8. Unit 8, ask 21. Find why `tools/memory-tree/check-memory-hygiene.sh --staged` printed `ALFORM: unbound variable` from the acceptance-ledger block on every pre-commit of aNimbleMend, and whether a check ended early with no verdict. The main loop could not reproduce it with nothing staged, nor with one CLOSED spec staged (check 23 graded one unit, no error); two replays of aNimbleMend commits as staged sets are recorded below. Fix it, and add an arm to the hygiene self-test that reds on the old behaviour.
9. Unit 9, ask 23. `tools/memory-tree/build_records.py`: the door refuses a red-fix record whose `Files` is empty, so a merge or an empty commit carrying a `Red-fix:` trailer is a permanent J1. Decide what a path-less fix commit owes, state it in the door or the join, implement it, and add a plant case under `--fixture --plant red-fix-join`.
10. Unit 10, ask 22, last. Four rows of `tools/run-gates/selftest-budgets.txt` are re-measured by the main loop, each suite alone on a quiet node, after every other unit is CLOSED. The spec states the procedure and the margin the file declares; the readings are the main loop's, and the builder writes the rows from them, then runs the two commands the prompt names and re-stamps the kickoff manifest where `tools/gate-legs.json` moved.
11. Every spec is Tier-2 where it changes a kit's contract or the governance template's rules and Tier-1 otherwise, per `memory/guides/SESSION-KICKOFF.md`. Each spec's status header carries `closes` with its ask. Every spec line stating a figure with a unit carries the word PINNED or a commit sha on the same line. The acceptance section cites no path the unit has not built yet. A criterion that needs a suite, a gate leg or the bar is the main loop's, and the spec says so in that criterion.

### Acceptance
- Ask 16: the gate guard's suite prints no FAIL line opening `parity:`.
- Ask 17: the scratch guard's suite prints no FAIL line opening `S-AC2`, `S-AC3`, `S-AC5` or `S-AC8`.
- Ask 18: the spec-token suite prints no `arm FAIL` line naming parity.
- Ask 19: the hygiene self-test exits 0 and prints its assertion total.
- Ask 20: the policy fixtures leg prints `0 wrong`.
- Ask 21: a `--staged` hygiene run prints no `unbound variable` line, and a new arm reds on the old script.
- Ask 22: each of the four rows names a reading taken alone on a quiet node after this build, at its declared margin.
- Ask 23: the door or the join states what a path-less fix commit owes, and a plant case holds it.
- Ask 24: `tools/playbook/practices.toml` and the protocol's section 12 say what the owner ruled.

### Gates
The plain bar, `bash tools/run-gates/run-gates.sh`, once after the last unit, and the full bar at the push boundary. The five suites and the policy fixtures leg are run by the main loop on a frozen clone.

### Non-goals
- Ask TOOL-aNimbleMend-28, the drain of three suites' fork idioms.
- Any floor raised or arm waived to make a suite pass.
- A record that rides its own fix commit: the owner ruled against it.
- Any kit version, which the lander's mint moves.

### Limitations
- A role agent's pass runs no suite, no gate leg and no bar; the main loop runs them.
- aNimbleMend's specs are CLOSED and frozen; a correction to one is stated in this build's own spec.
- `tools/unattended/check-unattended.sh` carries raw CR bytes; edit it in binary mode if a unit must touch it.
- Units 6 and 8 both write `tools/memory-tree/check-memory-hygiene.sh` or its suite, so they are sequenced.
- The merge and the push wait for the owner's explicit ask.

### Reuse
- Seams: `tools/playbook/practices.toml`, `tools/unattended/PROTOCOL.template.md`, `tools/unattended/gate-guard.js`, `tools/hooks/scratch-guard.js`, `tools/check-spec-tokens.py`, `tools/memory-tree/check-memory-hygiene.sh`, `tools/policy/check_policy.py`, `tools/memory-tree/build_records.py`, `tools/run-gates/selftest-budgets.txt`, `tools/run-gates/derive-ceilings.py`, `tools/run-gates/pass_legs.py`.
- The reproduction outputs, each suite run at `8db6f4bef` on a frozen clone, are on node a under `C:/Users/daily-agent/AppData/Local/Temp/nm16out/`: `a16.out` to `a21.out`, named for the ask.

## Drawn from the session

> Ask 24, sentence 1 […] How do you rule? — "Carve out the lane (Recommended)"
— owner, 2026-11-13, answering the kickoff's first question

> Ask 24, sentence 2 […] How do you rule? — "Next commit only (Recommended)"
— owner, 2026-11-13, answering the kickoff's second question

> FAIL S-AC5 the last line does not name the card and the 102 route lines left out: [/.claude/orientation-card.md]
— agent, `bash tools/hooks/scratch-guard.test.sh` at `8db6f4bef`, 2026-11-13

## Owner confirmation

Asked: Ready — say go and I'll start, or adjust any field.
Answer: not asked as a separate turn — the prompt above orders the work through to the bar, and the owner answered the kickoff's two questions on ask 24 in this session; the merge and the push still wait for the owner's ask.
