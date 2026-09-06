**Serves:** journal TOOL-aSurfacedLexicon-4 TOOL-aSurfacedLexicon-5 TOOL-aSurfacedLexicon-9

# Build pass, steps 2 and 3 — the declaration grammar, the convention predicate, the PATTERNS block

Node `a` · 2026-09-05 · build `aSurfacedLexicon` · streams tooling. Three units, SEQUENCED: the
dispatch verb REFUSED to declare them as one group because all three claim `tools/lexicon/lexicon.py`,
and that refusal is the M6 clause-1 disjointness proof rather than an obstacle to route around.

**This pass is where the kit finally gets the half it always promised.** The convention predicate did
not exist in any form before it — no camel, snake, kebab or pascal rule anywhere in the kit, against a
README that advertised one.

**Evidences:** TOOL-aSurfacedLexicon-4
- AC1 — `lexicon_conf.py --print-rows CELLS` — a CELLS row parses to a convention and its flags; reverting the block-key tuple made the same conf refuse the header.
- AC2 — `python tools/lexicon/lexicon.py --check` — a scratch CELLS row naming an extension LANGS omits — RED observed, naming the extension AND the row's line. The line half was added this pass; the first cut named only the file.
- AC3 — `tools/lexicon/selftest.py` — a non-integer pin count — refused at parse time naming the line; the integer form parses to an int rather than a string.
- AC4 — `tools/lexicon/selftest.py` — an unknown block header — still refused after the block-key tuple widened.
- AC5 — `tools/lexicon/selftest.py` — a real two-branch git merge over a blank-separated block — two branches draining ADJACENT cells merge at rc 0 with no conflict markers, and both drains survive.
- AC6 — `python tools/lexicon/lexicon.py --check` — a scratch PINS row for a cell with no CELLS row — RED observed naming the cell; green once the cell is declared.
- AC7 — amended rev-5 — STRUCK with its number retained. Adding the conf to a leg guard reds `govkit selfcheck`, and the kit descriptor had already refused that edit in writing. Its property is carried by AC11 and AC12.
- AC8 — `map_extractors.all_inventories()` — the verb inventory is unchanged at 23 keys.
- AC9 — `bash tools/lexicon/adopt-lexicon.sh --check` — rc 0 on the pristine tracked conf.
- AC10 — `python tools/lexicon/lexicon.py --check` — the pin set one below and one above the measured count — BOTH directions RED against the TRACKED conf. The fall case prints the replacement row to paste, which is what makes an unrecorded drain impossible rather than merely discouraged.
- AC11 — `bash tools/lexicon/adopt-lexicon.sh --check` — two adjacent PINS rows staged into the TRACKED conf — RED naming both line numbers; one blank line between them returns it to green.
- AC12 — `python tools/codebase-map/test_codebase_map.py` — the failing case was observed first, then the generated artifacts were regenerated in this same commit.

**Evidences:** TOOL-aSurfacedLexicon-5
- AC1 — a camel-cased function staged into a tracked `.py` file — RED naming the convention it satisfies and the one it was declared to satisfy.
- AC2 — `tools/lexicon/selftest.py` — a snake-cased class staged — RED on the type cell, same shape.
- AC3 — `python tools/lexicon/lexicon.py --check` — a scratch declaration with nothing staged — zero violations over the measured population; the denominator corrected to what the tree prints rather than what the spec predicted.
- AC4 — `python tools/lexicon/lexicon.py --check` — the file cells graded against the tracked tree — the in-tree failing case, observed without staging anything.
- AC5 — `tools/lexicon/selftest.py` — a name whose convention set is empty — RED as AMBIGUOUS and NOT as a violation.
- AC6 — `tools/lexicon/selftest.py` — the teeth run, re-declaring the cell as camel — the violation count moves to the measured figure, which is what makes AC3's zero a measurement rather than an assertion about nothing.
- AC7 — amended rev-6 — the universal claim that all 49 tracked shell test scripts pass first-dot kebab is FALSE. 48 of 49 pass; one does not. Struck rather than restated, and the exception is named.
- AC8 — the classifier called directly on `run` and on an underscore-affixed name — the set contract is gated at the seam, not only through the report.
- AC9 — `bash tools/lexicon/adopt-lexicon.sh --check` — rc 0; this unit changes no placeholder.
- AC10 — `tools/lexicon/selftest.py` — a definition named only with underscores — RED as AMBIGUOUS. Its in-corpus population is NINE dot-leading basenames, latent behind four dark cells, and every report of this arm says nine rather than zero.
- AC11 — `python tools/lexicon/lexicon.py --check` after the pin moved — the pin rose by exactly one, with a RAISED-by-name comment naming `classify` as the sole arrival and the command that measured it.
- AC12 — `python tools/codebase-map/test_codebase_map.py` — green after the regeneration in this commit.

**Evidences:** TOOL-aSurfacedLexicon-9
RE-KEYED onto the spec's own numbering. The first cut numbered two lines against criteria they did
not describe — the capturing-group refusal is AC6 and not AC1 — and left seven criteria with no line
at all, so nothing said which observation answered which. Every line below names the arm or the
command that made the observation; the whole suite is `python tools/lexicon/selftest.py`, green at
509 arms on this tree.

- AC1 — `tools/lexicon/selftest.py` — the `ts` fixture declares `ts:ts-regex:probe` plus two `PATTERNS` rows, and the run grades its `.ts` definitions, exits 0, and names the two declared extractor rows. The language is reachable ONLY through the declaration, which is the whole capability.
- AC2 — `tools/lexicon/selftest.py` — a definition in the DECLARED language whose leading token is outside `VERBS` reds, and the red names the file and the line (`web/widget.ts:3`).
- AC3 — amended rev-3 — the DEAD PROBE scope item already shipped before this unit, so the criterion as written could not fail. Restated at rev-3 onto WHICH refusal fires: a declared set matching nothing reds as DEAD PROBE and NOT for the unshipped-set reason. Logged in the rev-3 line of section 9.
- AC4 — `tools/lexicon/selftest.py` — an armed extension with no tracked file of its own is reported `INERT DECLARATION`, NOT `DEAD PROBE`, and it is a report rather than a refusal, so an empty population cannot satisfy the DEAD PROBE arm.
- AC5 — `tools/lexicon/selftest.py` — with no `PATTERNS:` block declared, `resolve_pattern_sets({})` compares equal to the shipped `PATTERN_SETS` in-process, so an adopter who writes no block is on exactly the previous behaviour.
- AC6 — `tools/lexicon/selftest.py` — zero capturing groups, two capturing groups and an uncompilable regex each refuse at parse time naming the file and the line, asserted through the engine AND through `lexicon_conf.py --print-rows PATTERNS`, so a refusal cannot fire on one reader and not the other.
- AC7 — `tools/lexicon/selftest.py` — both states observed: the `LANGS` triple alone is refused as an unshipped set, and adding the two rows with NOTHING else changed moves the armed coverage numerator by exactly one while the denominator holds.
- AC8 — `tools/lexicon/selftest.py` — the shipped-sentinel arm still passes and the merge does not mutate the shipped constant, asserted against `lex.PATTERN_SETS` in the same process.
- AC9 — `tools/lexicon/selftest.py` — two rows naming the same `<pset-id>.<part>` key refuse and name the first line, rather than last-wins silently retiring the row the owner believes is live.
- AC10 — `python tools/drift-audit/drift_report.py` — the resolution reverted at the FIRST call site — RED observed, naming the signal and the verb that stops being unused.
- AC11 — `python tools/lexicon/scaffold_lexicon.py` — the resolution reverted in the scaffolder — RED observed in both flavours: dropping the resolved sets makes the language invisible, dropping only the resolution makes it refused as unextractable, and the two print different failures.
- AC12 — `tools/lexicon/selftest.py` — the per-key merge over the SHIPPED `js-regex.types` key, observed by the H4 arm: the run prints `PATTERNS REPLACES a SHIPPED extractor key` naming `js-regex.types`, the unnamed keys of that set stand, and deleting the computation reds the arm. STATED PLAINLY: the criterion asks for the row in THIS repo's own `.lexicon.conf`, and this repo declares no `PATTERNS:` block — the row is a fixture declaration, so the merge behaviour is evidenced and the tracked-tree reading is not.
- AC13 — `bash tools/lexicon/adopt-lexicon.sh --check` — rc 0 with the commented example in place; the red section 7 predicted does not occur.

## The defect this pass exists to warn about

**Two mechanisms landed UNGATED and both units reported them satisfied.** A verifier reverted the
pattern-set resolution at each call site and watched both suites stay green — 251 lexicon arms and the
whole drift-audit suite, all passing over code that had been switched off.

A second re-verification then found the first fix had closed only ONE of the two sites. Reverting the
other alone still left everything green, because the arm written to cover it read a different signal.
The second site is inside the marginal-offense-rate signal, and the arm that now covers it asserts the
POPULATION grows when a language armed only through a declared pattern row is added — an operand that
cannot move unless the resolution actually ran. Proven by reverting that site alone, watching the arm
red, and restoring.

That is the difference between an arm and a decoration, and it took two adversarial passes to find,
because a green suite looks identical either way.

**A certification probe also could not fail.** The sweep certifying that no prose still promised the
retired shrink-only pin ran a basic regular expression with a literal pipe in it, which matches
nothing on any tree. It reported clean while four carriers were still standing — one of them a line
the scaffolder writes into every adopter's declaration, telling them the count may fall but never
rise, about a pin this pass made a two-sided equality. Re-run with an extended regex, it found all
four.
