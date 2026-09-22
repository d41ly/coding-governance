# The acceptance ledger — check 25 built, its arms observed directly, and the suite run owed

**Serves:** journal TOOL-dGatedProse-1

Node `d`, 2026-09-22, the build pass of `TOOL-dGatedProse-1` against spec rev-11, at order 2 on
`branch/spec-prose-gates-b41f7c`. The pass base is `9749b43e`, unit 5's closing commit. By the
owner's rule no suite and no gate leg was run. Every observation below was made by calling the
code directly from python files in the session scratchpad, which are untracked, so each line says
what was run and what it printed:

- the ARMS were observed by building the self-test's own main fixture tree with the suite's own
  construction lines, running the engine once over it as the suite does, and then running only this
  unit's assertion block and the seven scope-join rows AC15 names. It printed 44 executed
  assertions, 37 of them this unit's, and no failure. No other assertion of the suite ran.
- each arm's RED was observed by twenty-two staged breaks, each a one-line edit to a COPY of the
  engine, never the engine itself, with the same block run against the copy. Every break turned at least
  one of its own arms red, and those lines name it. In every break run the AC16 tree's `exit=0` row
  also went red for a reason that is the harness's and not the arm's: a copy outside the kit
  directory has no sibling modules. The base run, against the real kit, printed `exit=0`.
- the LIVE corpus was observed by running the engine's own preamble and its whole check-12 block,
  which now carries check 25, over this worktree, with checks 1-11 and 13-24 left out.

Everything a suite or a leg observes is OWED to the one run after all five units are built, and
each line names the break that stages it red.

**Evidences:** TOOL-dGatedProse-1
- AC1 — `tFixture-200` — OWED to the full self-test run. Observed directly: the check-25 block names it with `S1` and the spelling `NO VALUE READERS`, matched as one exact line. Red when: the arm is gone, which removes the only line naming it.
- AC2 — `tFixture-201` — OWED to the full self-test run. Observed directly: no line names it. The tail-strip break and the call-suffix break each turned that absence red.
- AC3 — `tFixture-202` — OWED to the full self-test run. Observed directly: 202 is silent, and 203's bare escape is named under the by-value message. The break that accepts an escape with no reason silenced 203.
- AC4 — `tFixture-208` — OWED to the full self-test run. Observed directly: one exact line names 208, the token `tAbsentReader` and the spelling `READER NOT IN TREE`. The break that counts every candidate file as a reader silenced it, and so did the break that kills the resolution awk, which then printed the completion finding in its place.
- AC5 — `tFixture-209` — OWED to the full self-test run. Observed directly: check 25's block does not name 209, and a notice line names the covered token and the file. The break that drops the notice turned the notice row red.
- AC6 — `tFixture-206` — OWED to the full self-test run. Observed directly: one exact line names 206 under the message that says the by value half is missing.
- AC7 — `tFixture-204` — OWED to the full self-test run. Observed directly: silent. The break that admits a bare word unconditionally named it.
- AC8 — `tFixture-205` — OWED to the full self-test run. Observed directly: silent. The break that deletes the family-slug-seq exclusion named it.
- AC9 — `tFixture-211` — OWED to the full self-test run. Observed directly: silent. The break that deletes the space exclusion named it.
- AC10 — `tFixture-212` — OWED to the full self-test run. Observed directly: named with both labels, `S1, S2`, as one exact line. The break that restores an exclusion for markdown tails lost that line.
- AC11 — `tFixture-207` — OWED to the full self-test run for the fixture half, which is named, and the kind-noun break lost it. The grep half was observed directly at rev-10's reading: over the engine each of the six phrases returns exactly one line this unit adds, line 1445, the same line for all six and the one right after the verb list. The only other lines are `enum value` and `status token` at the base, one phrase each. Each conf spells `enum value` once, in its comment on the families key, and neither conf is touched.
- AC12 — `tFixture-210` — OWED to the full self-test run. Observed directly: silent in the same run that names 200. The break that sets liveness true for every spec named it.
- AC13 — `SPEC_FORMAT_CUTOFF` — OWED to the full self-test run. Observed directly: with the key blank, 200 is absent and exactly one line names check 25 and the key, matched whole, with no failure prefix. With the key armed and the scope-join key blank, 200 is named and the notice is gone. The break that narrows the accumulator's guard back to the scope-join date lost 200 in the second run, and the break that drops the notice turned the first run red.
- AC14 — `## 2. Scope (IN)` — OWED to the full self-test run. Observed directly: 200 carries that heading and no acceptance heading, check 25 names it, and check 12's scope-join arm is silent for the same file.
- AC15 — `tFixture-115` — OWED to the full self-test run. Observed directly: the seven existing scope-join rows kept their verdicts, 110 and 114 named and 111, 112, 113, 115 and 116 not, and the named-cutoff line still matched, in the same run.
- AC16 — `CLOSED|WONTDO` — OWED to the full self-test run. Observed directly: over a tree whose one spec is CLOSED the notice names that test, check 25 names nothing, and the run printed `exit=0`. The liveness break named the spec and lost the notice, and the break that drops the notice lost it alone.
- AC17 — `python tools/memory-tree/check-arms.py --report` — run directly: check 25 branch 1 of the hygiene engine reads ARMED, and `memory/project/unarmed-branches.txt` carries no row for it. The `--check` leg is OWED to the post-build run.
- AC18 — `grep -n 'Readers' memory/HYGIENE.md` — observed directly after the re-render, and every required sentence is in entry 25. The per-half grading words, the control, the trust sentence and the word six are each there. So is the case and past tense sentence, the markdown sentence and the two unreached classes with no size. So is the reader and record sentence and the disarming key. No kind-noun phrase is listed. Line 18 of the kit README reads 25 checks with 20 and 24 under `row_grammar.py`.
- AC19 — `grep -n '^FLOOR_ASSERTIONS=' tools/memory-tree/check-memory-hygiene.test.sh` — observed statically: 374 at the base and 411 now, a delta of 37. The assertion block between its two marker comments holds 37 helper calls, the fixture block none, and the comment above the constant names this unit and the raise.
- AC20 — `grep -c 'Readers:' tools/memory-tree/SPEC-TEMPLATE.template.md` — observed directly: 1 in the template and 1 in the render, both at line 295, inside the section 2 skeleton that spans lines 281 to 304. The render was made by the parity script's render mode and never by hand.
- AC21 — `bash tools/memory-tree/check-memory-hygiene.sh` — OWED to the post-build memory hygiene run. Observed directly over this worktree before the commit: check 25 named no item on any node, and printed one covered-name notice, for `reuse-discovery.js` on `bConvergentLodestar-1` S3. A probe line spliced into a copy of the arm showed the trigger firing on 37 items across 19 specs, label for label unit 5's census set. A staged break hid one of unit 5's clause markers in `aGradedDoorway-7` S2, and check 25 then named that spec and exited 1. The file was restored after.
- AC22 — `KIT_MEMORY_TREE_VERSION` — observed directly: the constant does not move in the diff from the base, no marker moves, and line 1 of each of the four renders byte-matches its template. The verdict epoch leg is expected RED from this commit until unit 3's, as the spec's section 7 states.
- AC23 — `tFixture-213` — OWED to the full self-test run. Observed directly: named under the by-value message, as one exact line. The break that grades a clause only where the trigger fired silenced it.
- AC24 — `tFixture-214` — OWED to the full self-test run. Observed directly: named with `S1, S2` as one exact line, and the one engine line carrying the gawk case flag's name is a comment. The break that drops the fold lost 214 and 215.
- AC25 — `tFixture-215` — OWED to the full self-test run. Observed directly: named with exactly `S1, S2, S3, S4, S5`. The break that drops the past tense lost the line, and the break that drops the word boundary added S6 to it.
- AC26 — `tFixture-216` — OWED to the full self-test run. Observed directly: the six record-only names are each named, and neither the guide's name nor the bare filename is. The reader-filter break silenced the six, and the identity-suffix break named the filename.
- AC27 — `tFixture-217` — OWED to the full self-test run. Observed directly: named with `S1, S2` as one exact line. The break that drops the whitespace squeeze lost the line, and so did the kind-noun break, which S2 alone needs.
