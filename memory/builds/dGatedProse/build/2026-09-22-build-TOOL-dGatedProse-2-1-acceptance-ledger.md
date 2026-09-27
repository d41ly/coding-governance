# The acceptance ledger — the claims join built, its arms observed directly, and the suite run owed

**Serves:** journal TOOL-dGatedProse-2

Node `d`, 2026-09-22, the build pass of `TOOL-dGatedProse-2` against spec rev-8, closed at
rev-9, at order 3 on `branch/spec-prose-gates-b41f7c`. The pass base is `498445cc`, unit 1's
closing commit. By the owner's rule no suite and no gate leg was run. Every observation below was
made by calling the code directly from python files in the session scratchpad, which are untracked,
or by running only this unit's arm block of the self-test, so each line says what was run and what
it printed:

- the ARMS were observed by building a runner from the self-test's own prelude and this unit's
  block alone, pointed at the checker. It printed 24 executed assertions and no failure. No other
  assertion of the suite ran.
- the arms' RED was observed by pointing the same runner at the checker as it stood before this
  join: all 24 failed. Eleven further staged breaks, each a one-line edit to a COPY of the checker,
  each turned at least one arm of the block red, and the lines below name them.
- the LIVE corpus was observed by calling `scan_claims` over every tracked spec file of this tree,
  at the closing commit's working tree.

Everything a suite or a leg observes is OWED to the one run after all five units are built, and
each line names the break that stages it red. Two landing acts are not this unit's to write, and
section 3 of the spec says whose they are: the re-wording and closing of the backlog row
`TOOL-dLoggedFlight-32`, and the new row routing the dossier-count freshness arm, whose id the
landing session mints.

**Evidences:** TOOL-dGatedProse-2
- AC1 — `derive_window_closer` — OWED to the held `spec-tokens self-test` run. Observed directly: the unit-25 blob at `9f43bb26^` yields one hit, CODE SYMBOL, on `derive_window_closer` through the active arm, and the unit-27 blob one on `check_count_sources`. The block's two direct arms and its process arm were red on the pre-join checker.
- AC2 — `scan_claims` — OWED to the held self-test run. Observed directly: each of the three sentences matches an arm and yields zero hits, the wrapped one included. The break that reports every cleared object as a hit turned all three red.
- AC3 — `scan_claims` — OWED to the held self-test run. Observed directly: the unwritten key matches an arm and clears. The same break turned it red.
- AC4 — `tools/codebase-map/map_extractors.py` — OWED to the held self-test run. Observed directly: 270 keys over 10 inventories, 14 of them carrying a parenthesis, each passed through `scan_claims` as the object of a claim sentence, with zero refused and zero unmatched. The break that drops the space clause turned it red.
- AC5 — `render_doc` — OWED to the `kit/dogfood doc parity` leg. Observed directly: the render was made by the parity script's render mode and never by hand, and the template's rule bullet with its tool-root token substituted equals the render's byte for byte. Both carry the three shapes, the space clause, three citations and the six limits, and the checker's docstring names the same six. The bullet sits after the PINNED-or-DERIVED bullet, one below the verify rule, because that bullet opens "The rule above" and means the verify rule.
- AC6 — `CLAIM_CANARY` — OWED to the held self-test run. Observed directly: six broken copies, each arm matching nothing in turn, then the case fold dropped, then the space clause dropped. Each exited 1 naming `CLAIM_CANARY` and printed no claims line. Against the pre-join checker every substitution missed, the copies exited 0, and all six arms were red.
- AC7 — `scan_claims` — OWED to the held self-test run. Observed directly: one hit, on line 5, the unfenced copy. The break that removes the fence blanker turned it red.
- AC8 — `tools/check-spec-tokens.py` — OWED to the held self-test run. Observed directly in a scratch repo: the claims line prints three zeros over a tree with no claim sentence, and 4, 1 and 5 over two live specs of which one carries four sentences and five objects. `--list` prints each cleared object once as a NEAR row and none as a hit. The break that prints the line only when a run matched lost the zero line, and the break that stops a run at its first object lost the counts and the rows.
- AC9 — `FLOOR_ASSERTIONS` — observed statically: 67 at the base and 91 now, a delta of 24, against 3 `arm` calls and 21 inline increments in this unit's block. The same rule reproduces the base pin, 60 and 7. The RAISED comment names this unit and both values.
- AC10 — `memory/builds/dGatedProse/spec/` — OWED to the `spec tokens` leg at the post-build run. Observed directly at the closing commit: zero runs and zero hits over the five spec files of this folder, and zero runs and zero hits over the 26 live specs of the checker's own population. Over all 722 tracked specs there are 4 clears and no hit, and none of the four is in a live spec.
- AC11 — `memory/map/features/spec-tokens.md` — observed directly, as the documented check it is: the docstring's join table holds 6 rows, legs to claims, and the title opens "Six" and the ordinal sentence names the sixth, where the base title opened "Five". The sentence naming three resolving joins is unchanged.
- AC12 — `scan_claims` — OWED to the held self-test run. Observed directly: each of the six fixtures yields one hit carrying its designated arm, and the shouted constant is CODE SYMBOL. Each arm made to match nothing turned its own fixture red, the dropped case fold turned the uppercase fixture red, and a lowercase-only underscore test turned the shouted fixture red.
